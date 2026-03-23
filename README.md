# aliyun-skill

A skill repository for managing Alibaba Cloud resources using the [Aliyun CLI](https://github.com/aliyun/aliyun-cli). Compatible with [Claude Code](https://claude.ai/code) and [OpenClaw](https://github.com/openclaw/openclaw).

## Skills

### `aliyun-cli`

Teaches Claude how to construct and execute `aliyun` commands for managing Alibaba Cloud resources. Covers CLI setup, authentication, and resource operations.

**Triggers when you mention:** `aliyun`, `Alibaba Cloud`, `阿里云`, `ECS`, or any Alibaba Cloud product in the context of infrastructure management.

**Currently supported resources:**

| Resource | Operations |
|----------|-----------|
| ECS | list instances, start/stop/reboot, resize disk, create snapshot, manage security groups |

## Structure

```
aliyun-skill/
├── .claude-plugin/
│   └── plugin.json       # Claude Code plugin manifest
└── skills/
    └── aliyun-cli/
        ├── SKILL.md              # Skill entry point
        └── references/
            ├── setup.md          # CLI installation and authentication
            └── ecs.md            # ECS operations reference
```

## Installation

### Claude Code (plugin)

```
/plugin marketplace add Hambaobao/aliyun-skill
/plugin install aliyun-skill@aliyun-skill
```

### Manual

```bash
git clone git@github.com:Hambaobao/aliyun-skill.git
cp -r aliyun-skill/skills/aliyun-cli ~/.claude/skills/
```
