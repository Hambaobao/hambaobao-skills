# Hambaobao Skills

A collection of Agent Skills for AI coding assistants. Compatible with [Claude Code](https://claude.ai/code) and [OpenClaw](https://github.com/openclaw/openclaw).

## Skills

### aliyun-cli

Teaches Claude how to construct and execute `aliyun` commands for managing Alibaba Cloud resources. Covers CLI setup, authentication, and resource operations.

**Triggers when you mention:** `aliyun`, `Alibaba Cloud`, `阿里云`, `ECS`, or any Alibaba Cloud product in the context of infrastructure management.

**Currently supported resources:**

| Resource | Operations |
|----------|-----------|
| ECS | list instances, start/stop/reboot, resize disk, create snapshot, manage security groups |

## Structure

```
hambaobao-skills/
├── .claude-plugin/
│   └── marketplace.json          # Claude Code plugin manifest
└── skills/
    ├── aliyun-cli/               # Alibaba Cloud CLI skill
    │   ├── SKILL.md
    │   └── references/
    └── <skill-name>/             # More skills coming...
        └── SKILL.md
```

## Installation

### Claude Code (plugin)

```
/plugin marketplace add Hambaobao/hambaobao-skills
/plugin install <skill-name>@hambaobao-skills
```

### Manual

```bash
git clone git@github.com:Hambaobao/hambaobao-skills.git
cp -r hambaobao-skills/skills/<skill-name> ~/.claude/skills/
```
