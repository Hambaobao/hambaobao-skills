#!/usr/bin/env python3
"""Read selected Codex settings and origins without a model request or raw config output."""

import argparse
import json
from pathlib import Path
import queue
import subprocess
import sys
import threading
import time


KEYS = (
    "model",
    "model_reasoning_effort",
    "service_tier",
    "model_context_window",
    "model_auto_compact_token_limit",
    "web_search",
)


class ConfigError(Exception):
    pass


class ConfigReader:
    def __init__(self, executable, timeout):
        self.timeout = timeout
        self.sequence = 0
        self.responses = queue.Queue()
        self.process = subprocess.Popen(
            [executable, "app-server", "--stdio", "--strict-config"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            bufsize=1,
        )
        threading.Thread(target=self._read_stdout, daemon=True).start()

    def _read_stdout(self):
        try:
            for line in self.process.stdout:
                try:
                    message = json.loads(line)
                    if isinstance(message, dict):
                        self.responses.put(message)
                except json.JSONDecodeError:
                    self.responses.put({"_invalid": True})
                    return
        finally:
            self.responses.put({"_eof": True})

    def request(self, method, params):
        # The helper deliberately has no mutation, thread, or turn method.
        if method not in ("initialize", "config/read"):
            raise ConfigError("Unsupported method")
        self.sequence += 1
        request_id = self.sequence
        self._send({"id": request_id, "method": method, "params": params})
        deadline = time.monotonic() + self.timeout
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ConfigError("Configuration read timed out")
            try:
                message = self.responses.get(timeout=remaining)
            except queue.Empty:
                raise ConfigError("Configuration read timed out") from None
            if message.get("_eof") or message.get("_invalid"):
                raise ConfigError("App-server ended or returned an invalid protocol response")
            if message.get("id") != request_id:
                continue
            if "error" in message:
                # Raw errors can contain configuration excerpts. Keep them local.
                raise ConfigError("App-server rejected the configuration request; inspect local diagnostics")
            result = message.get("result")
            if not isinstance(result, dict):
                raise ConfigError("Unexpected configuration response shape")
            return result

    def _send(self, value):
        self.process.stdin.write(json.dumps(value) + "\n")
        self.process.stdin.flush()

    def initialize(self):
        self.request("initialize", {
            "clientInfo": {"name": "raft-codex-config-reader", "version": "1.0"},
            "capabilities": {"experimentalApi": True},
        })
        self._send({"method": "initialized"})

    def close(self):
        if self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()


def source_summary(source):
    if not isinstance(source, dict):
        return None
    return {
        key: source[key]
        for key in ("type", "file", "dotCodexFolder", "profile")
        if key in source
    }


def summarize(cwd, result, keys):
    config, origins, layers = (result.get(k) for k in ("config", "origins", "layers"))
    if not isinstance(config, dict) or not isinstance(origins, dict) or not isinstance(layers, list):
        raise ConfigError("Expected config, origins, and layers; check the installed protocol version")
    settings = {}
    for key in keys:
        origin = origins.get(key)
        settings[key] = {
            "value": config.get(key),
            "origin": source_summary(origin.get("name")) if isinstance(origin, dict) else None,
        }
    return {
        "cwd": str(cwd),
        "settings": settings,
        "layers": [
            {
                "source": source_summary(layer.get("name")),
                "enabled": layer.get("disabledReason") is None,
            }
            for layer in layers
        ],
        "scope": "fresh app-server config/read; not proof of live Raft session reload",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cwd", action="append", required=True, help="Target workspace; repeat for multiple targets")
    parser.add_argument("--key", action="append", choices=KEYS, help="Selected field; defaults to all supported fields")
    parser.add_argument("--codex", default="codex", help="Codex executable path")
    parser.add_argument("--timeout", type=float, default=15, help="Seconds per configuration request")
    args = parser.parse_args()
    if not 0 < args.timeout <= 60:
        parser.error("--timeout must be greater than 0 and at most 60 seconds")
    directories = [Path(value).expanduser().resolve() for value in args.cwd]
    if any(not directory.is_dir() for directory in directories):
        parser.error("Every --cwd must be an existing directory")
    reader = None
    try:
        reader = ConfigReader(args.codex, args.timeout)
        reader.initialize()
        summaries = [
            summarize(directory, reader.request("config/read", {
                "cwd": str(directory), "includeLayers": True,
            }), args.key or KEYS)
            for directory in directories
        ]
        print(json.dumps({"targets": summaries}, ensure_ascii=False, indent=2))
        return 0
    except (ConfigError, OSError) as error:
        message = str(error) if isinstance(error, ConfigError) else "Could not start or communicate with Codex"
        print(json.dumps({"error": message}), file=sys.stderr)
        return 1
    finally:
        if reader is not None:
            reader.close()


if __name__ == "__main__":
    sys.exit(main())
