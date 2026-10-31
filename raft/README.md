# Raft skills

Skills in this directory depend on Raft member identities, workspaces, or collaboration workflows. General-purpose skills stay in the repository's root `skills/` directory, even when used by Raft agents.

## Available skills

| Skill | Purpose |
|-------|---------|
| [team-skill-maintenance](skills/team-skill-maintenance/SKILL.md) | Select, maintain, install, and update skills for specific Raft members, with version records and runtime verification. |
| [raft-codex-config](skills/raft-codex-config/SKILL.md) | Maintain per-member Codex settings and verify effective values, configuration sources, and session boundaries. |

`team-skill-maintenance` is intended for the agent maintaining the team's environment. It uses the Raft CLI and access to the target member's execution environment. Its Codex-specific installation procedure is an on-demand reference; other runtimes require their own path and discovery checks.

`raft-codex-config` complements it with configuration maintenance. It includes a Python 3 helper that calls Codex `config/read` and prints selected settings and source summaries. Running the helper reads configuration without starting a model turn or changing settings. Its result describes a fresh app-server process, so live Raft session changes need separate verification.

## Installation

Choose the source path `raft/skills/team-skill-maintenance` or `raft/skills/raft-codex-config`. Use a reviewed commit and install the complete directory into the intended maintainer's runtime skill location. Installing a skill equips that maintainer with its workflow; later member installations or configuration changes follow the scope of each request.

For a Raft agent launched with Codex from its workspace, the usual destination is:

```text
<maintainer-workspace>/.agents/skills/<skill-name>/
```

When using a skill installer, specify both the repository subdirectory and the destination explicitly. For example, ask the maintaining agent:

> Install `raft/skills/team-skill-maintenance` from `Hambaobao/hambaobao-skills` at the reviewed full commit SHA into the named maintainer's Codex workspace. Verify the member, computer, actual launch directory, file contents, and skill discovery result, then record the installed version.

For manual installation, copy the complete skill directory from a clean checkout of the reviewed commit after checking for an existing copy. Updates should preserve local changes and a recoverable previous version. See the [Codex workspace reference](skills/team-skill-maintenance/references/codex-workspaces.md) for the detailed procedure.

The optional Claude Code plugins are `raft-team-skill-maintenance` and `raft-codex-config`. Install the one needed by the target maintainer:

```text
/plugin marketplace add Hambaobao/hambaobao-skills
/plugin install raft-team-skill-maintenance@hambaobao-skills
/plugin install raft-codex-config@hambaobao-skills
```

Use the target runtime's installation scope controls when installing a plugin. Workspace copies and plugin installations have different discovery and update mechanisms; record which was used.
