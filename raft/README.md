# Raft skills

Skills in this directory depend on Raft member identities, workspaces, or collaboration workflows. General-purpose skills stay in the repository's root `skills/` directory, even when used by Raft agents.

## Available skills

| Skill | Purpose |
|-------|---------|
| [team-skill-maintenance](skills/team-skill-maintenance/SKILL.md) | Select, maintain, install, and update skills for specific Raft members, with version records and runtime verification. |

`team-skill-maintenance` is intended for the agent maintaining the team's environment. It uses the Raft CLI and access to the target member's execution environment. Its Codex-specific installation procedure is an on-demand reference; other runtimes require their own path and discovery checks.

## Installation

The source path is `raft/skills/team-skill-maintenance`. Choose a reviewed commit and install the complete directory into the intended maintainer's runtime skill location. Installing it equips that maintainer with the workflow; later member installations follow the scope of each request.

For a Raft agent launched with Codex from its workspace, the usual destination is:

```text
<maintainer-workspace>/.agents/skills/team-skill-maintenance/
```

When using a skill installer, specify both the repository subdirectory and the destination explicitly. For example, ask the maintaining agent:

> Install `raft/skills/team-skill-maintenance` from `Hambaobao/hambaobao-skills` at the reviewed full commit SHA into the named maintainer's Codex workspace. Verify the member, computer, actual launch directory, file contents, and skill discovery result, then record the installed version.

For manual installation, copy the complete skill directory from a clean checkout of the reviewed commit after checking for an existing copy. Updates should preserve local changes and a recoverable previous version. See the [Codex workspace reference](skills/team-skill-maintenance/references/codex-workspaces.md) for the detailed procedure.

The optional Claude Code plugin is `raft-team-skill-maintenance`:

```text
/plugin marketplace add Hambaobao/hambaobao-skills
/plugin install raft-team-skill-maintenance@hambaobao-skills
```

Use the target runtime's installation scope controls when installing a plugin. Workspace copies and plugin installations have different discovery and update mechanisms; record which was used.
