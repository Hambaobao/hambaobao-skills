# aliyun-skill

A [Claude Code](https://claude.ai/code) skill repository for managing Alibaba Cloud resources using the [Aliyun CLI](https://github.com/aliyun/aliyun-cli).

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
aliyun-cli/
├── SKILL.md              # Skill entry point
└── references/
    ├── setup.md          # CLI installation and authentication
    └── ecs.md            # ECS operations reference
```
