# Hambaobao Skills

A collection of Agent Skills for AI coding assistants, including Codex, [Claude Code](https://claude.ai/code), and [OpenClaw](https://github.com/openclaw/openclaw).

General-purpose skills live in `skills/`. Skills that depend on Raft member identities, workspaces, or collaboration workflows live in [`raft/skills/`](raft/README.md).

## Skills

### pr-writing

Write, refresh, or assess PR titles and descriptions against the actual branch changes. Focuses on changed behavior, design decisions, useful validation evidence, and reviewer context. Follows each repository's existing template and conventions; otherwise provides a default title format and sections for background, changes, and validation, with English titles and Chinese bodies.

**Use when:** preparing a PR description, updating it after substantive changes, or checking whether an existing PR is clearly written.

**Plugin name:** `pr-writing`.

### aliyun-cli

Teaches Claude how to construct and execute `aliyun` commands for managing Alibaba Cloud resources. Covers CLI setup, authentication, and resource operations.

**Triggers when you mention:** `aliyun`, `Alibaba Cloud`, `阿里云`, `ECS`, `VPC`, `OSS`, `RDS`, `SLB`, `RAM`, `ACR`, `Container Registry`, or any Alibaba Cloud product in the context of infrastructure management.

**Currently supported resources:**

| Resource | Operations |
|----------|-----------|
| Setup & Auth | install, configure, switch profiles |
| ECS | list instances, start/stop/reboot, resize disk, create snapshot, manage security groups |
| VPC | manage VPCs, VSwitches, EIPs, NAT gateways, route tables |
| OSS | buckets, upload/download, sync, presigned URLs |
| RDS | instances, databases, accounts, backups, IP whitelist |
| SLB / CLB | create LB, manage listeners, add/remove backend servers |
| RAM | users, groups, roles, policies, access keys |
| DNS | list domains, add/update/delete records |
| ACR | instances, namespaces, repositories, image tags, docker login |

## Raft skills

[team-skill-maintenance](raft/skills/team-skill-maintenance/SKILL.md) helps a team maintainer select, install, and update skills for specific Raft members, with fixed versions and runtime verification. See [Raft setup and installation](raft/README.md).

## Structure

```
hambaobao-skills/
├── .claude-plugin/
│   └── marketplace.json          # Claude Code plugin manifest
├── skills/                       # General-purpose skills
│   ├── pr-writing/
│   │   └── SKILL.md
│   └── aliyun-cli/
│       ├── SKILL.md
│       └── references/
└── raft/                         # Raft-specific workflows
    ├── README.md
    └── skills/
        └── team-skill-maintenance/
            ├── SKILL.md
            └── references/
```

## Installation

### Claude Code (plugin)

```
/plugin marketplace add Hambaobao/hambaobao-skills
/plugin install <plugin-name>@hambaobao-skills
```

For PR writing, use `/plugin install pr-writing@hambaobao-skills`. The existing Alibaba Cloud plugin is `aliyun-skills@hambaobao-skills`.

For Raft team skill maintenance, use `/plugin install raft-team-skill-maintenance@hambaobao-skills` in the intended maintainer's environment.

### Manual

```bash
git clone git@github.com:Hambaobao/hambaobao-skills.git
cp -r hambaobao-skills/skills/<skill-name> ~/.claude/skills/
```
