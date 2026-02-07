# Copilot 工作区说明（中文优先）

本文件用于指导 AI 编码代理（GitHub Copilot / coding agents）在本仓库内工作。**中文优先**；如遇术语或歧义，允许用**简短英文**做精确定义（e.g., “idempotent”, “breaking change”, “race condition”）。

## 沟通与输出（Communication）
- 优先用中文解释方案与原因；关键技术名词可附英文括号说明。
- 给出可执行步骤与命令，避免空泛建议。
- 若需求不明确，先提**最少必要的澄清问题**（最多 3 个），再继续实现。
- 任何可能引入 **breaking change** 的改动，必须在说明中显式标注并给迁移方案（migration steps）。

## 代码改动范围（Scope）
- 尽量做**最小改动**（minimal diff），避免无关重构（refactor）。
- 不随意改动公共 API / 配置结构；如必须改动，先解释影响面。
- 新增依赖（dependencies）前先说明理由、替代方案与安全影响。

## 代码风格（Code Style）
- 遵循仓库既有风格：缩进、命名、目录结构、文件组织方式以现有代码为准（follow existing patterns）。
- 变更同一模块时，保持一致的错误处理与日志风格。
- 若仓库使用格式化工具（formatter，如 Prettier/Black/gofmt），以工具输出为准；不要手动“微调格式”。

## 架构与约定（Architecture & Conventions）
- 优先复用现有抽象与工具函数，避免重复实现。
- 任何跨模块/跨包改动，需简要描述数据流（data flow）与依赖关系（dependencies）。
- 处理配置、环境变量、特性开关（feature flags）时，确保默认行为与历史兼容。

## 测试与质量（Build / Test）
- 修改行为（behavior change）必须配套测试或可验证方式：
  - 单元测试（unit tests）优先；
  - 如无测试框架，提供可复现的手动验证步骤（manual verification）。
- 提交前优先运行（按项目实际情况调整）：
  - `npm test` / `pnpm test` / `yarn test`
  - `pytest`
  - `go test ./...`
  - `cargo test`
- 若无法运行（环境缺失/CI 限制），需在说明中写明原因与替代验证方式。

## 安全与隐私（Security）
- 不在代码、日志或文档中写入密钥（secrets）、token、cookie、个人数据（PII）。
- 处理外部输入时保持校验与转义，避免注入（injection）与路径遍历（path traversal）。
- 如涉及鉴权/权限（authz/authn），默认最小权限（least privilege）。

## 文档与提交说明（Docs & Change Notes）
- 新增/修改用户可见行为时，更新对应文档（README/CHANGELOG/注释）——仅在仓库确有这些文件与约定时。
- PR/提交说明建议包含：
  - 背景（context）
  - 改动点（what）
  - 风险（risk）
  - 验证方式（verification）

## 需要你补充的信息（可选）
如果你希望本说明更贴合仓库，请告诉我：
1) 主要语言/框架（e.g., Node/Python/Go/Java）
2) 常用包管理（pnpm? poetry? go modules?）
3) CI 使用什么（GitHub Actions?）以及主要工作流文件位置
我可以基于你的回答把“Build and Test”命令和项目约定进一步具体化。