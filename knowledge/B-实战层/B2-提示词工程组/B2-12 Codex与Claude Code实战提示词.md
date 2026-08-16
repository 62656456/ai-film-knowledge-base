# Codex与Claude Code实战提示词
> 用途（直接用模板）：Codex和Claude Code日常使用的实战提示词模板，含月度复盘、第一性原理、对抗式审查、CLAUDE.md配置、四阶段工作流

---

## 一、Codex 提示词模板

### 月度复盘Prompt（直接复制）
> 来源：今日头条自媒体，未独立核实·可信度低

```
Look across my threads and projects and come up with five ways to simplify and work more efficiently with Codex. Use sub-agents.
```

### 第一性原理（直接复制）
> 来源：今日头条自媒体，未独立核实·可信度低

```
请从第一性原理出发，分析这个问题的根本原因，不要只做表面修复。
```

### 对抗式审查（直接复制）
```
请对刚才的代码进行对抗式审查，重点检查边界情况、异常输入、并发、性能、安全风险和可能导致线上故障的问题。
```

### 组合Prompt
```
请先从第一性原理出发，分析这个问题的根本原因；再对方案做一轮对抗式审查，找出潜在风险和更稳的实现方式。
```

---

## 二、Claude Code 配置模板

### CLAUDE.md 配置模板
> 来源：Claude Code 官方最佳实践文档（已核对）：https://code.claude.com/docs/en/best-practices

```markdown
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

要点：只写Claude猜不到的命令和与默认不同的代码风格；用`IMPORTANT`或`YOU MUST`强调关键规则；可用`@path/to/file`导入其他文件。

### 分层配置体系
- 个人级：`~/.claude/CLAUDE.md` — 个人偏好，适用所有项目
- 项目级：`./CLAUDE.md` — 项目核心规范，适用当前仓库
- 模块级：`./src/api/CLAUDE.md` — 模块专属规则

CLAUDE.md要写"是什么、为什么"，而不是"怎么做"。

### 四阶段工作流（官方推荐）

Phase 1 - Explore（探索）：
```
read /src/auth and understand how we handle sessions and login. also look at how we manage environment variables for secrets.
```

Phase 2 - Plan（规划）：
```
I want to add Google OAuth. What files need to change? What's the session flow? Create a plan.
```

Phase 3 - Implement（实现）：
```
implement the OAuth flow from your plan. write tests for the callback handler, run the test suite and fix any failures.
```

Phase 4 - Commit（提交）：
```
commit with a descriptive message and open a PR
```

判断标准：能用一句话描述diff就跳过计划直接做。涉及3个及以上文件时必须开计划模式。

### 验证驱动开发Prompt对比

| Before（差） | After（好） |
|---|---|
| `implement a function that validates email addresses` | `write a validateEmail function. example test cases: user@example.com is true, invalid is false, user@.com is false. run the tests after implementing` |
| `make the dashboard look better` | `[paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them` |
| `the build is failing` | `the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error` |
