# Hambaobao Skills

A collection of Agent Skills for AI coding assistants. Compatible with [Claude Code](https://claude.ai/code) and [OpenClaw](https://github.com/openclaw/openclaw).

## Skills

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
/plugin install <plugin-name>@hambaobao-skills
```

### Manual

```bash
git clone git@github.com:Hambaobao/hambaobao-skills.git
cp -r hambaobao-skills/skills/<skill-name> ~/.claude/skills/
```
