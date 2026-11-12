# 检索方法、关键词与覆盖记录

调研日期：2026-11-12。目标是从三份用户报告出发，建立可持续更新的 Agent 记忆项目目录，而不是重排旧报告或简单复制外部 awesome list。

## 输入材料

- `2026-10-15-开源Agent记忆库全景整理.md`
- `2026-10-16-Honcho记忆库架构与接入调研.md`
- `2026-10-16-OpenViking与Hindsight、MemSearch、Honcho对比调研.md`

三份材料共同说明，Agent 记忆的差异不只在向量库：真正需要比较的是记忆对象、真源、捕获与加工、作用域、检索路线、证据、更正/删除、宿主集成和后台成本。

## 检索词

| 方向 | 英文关键词 | 中文关键词 |
| --- | --- | --- |
| 完整记忆层 | agent memory, long-term memory, memory layer, memory service | Agent 记忆库、长期记忆、记忆引擎 |
| 认知类型 | episodic, semantic, procedural, working memory | 情景记忆、语义记忆、程序记忆、工作记忆 |
| 文件真源 | markdown memory, file-backed, source of truth, Git-native | Markdown 真源、文件记忆、可审阅记忆 |
| 图与时间 | temporal knowledge graph, entity memory, bi-temporal | 时序图谱、实体关系、双时态记忆 |
| 编码宿主 | coding agent memory, MCP memory, Claude Code, Codex | 编码 Agent 记忆、MCP 记忆服务 |
| 经验演化 | experience memory, skill extraction, reflection, consolidation | 经验记忆、技能提炼、反思、休眠整理 |
| 治理风险 | correction, deletion, forgetting, provenance, poisoning | 更正、删除、遗忘、来源、记忆污染 |
| 评测 | LongMemEval, LoCoMo, MemoryAgentBench, BEAM | 长期记忆评测、删除残留、污染基准 |

宽查询会混入普通数据库、完整 Agent、操作系统内存和浏览器收藏工具，因此最终条目必须回到 canonical GitHub 仓库、默认分支 README 与许可证核验。

## 三轮过程

| 轮次 | 批次 | 结果 | 新来源 | 新来源率 |
| --- | ---: | ---: | ---: | ---: |
| 1 | 14 | 579 | 534 | 92.2% |
| 2 | 7 | 125 | 110 | 88.0% |
| 3 | 6 | 281 | 203 | 72.2% |

第一轮覆盖定义、官方项目、awesome 索引、GitHub 仓库、对比、benchmark、风险与近期项目，并采集 `mnemoverse/awesome-agent-memory` 作为外部覆盖基线。

第二轮根据新实体补查 Hy-Memory、TencentDB Agent Memory、openJiuwen、M-flow、MemSkill、MemT、AfterDeleteBench，以及编码 Agent/MCP 记忆与受限许可项目。

第三轮解决 Membase/Memobase、多个 Mnemosyne、Open Agent Memory 等同名与范围问题，并补入 MemoryStackBench、OWASP Agent Memory Guard、MPBench 等治理评测。最后批量登记全部 87 个项目的固定 README 和 GitHub 指标。

停止原因是预设三轮上限，不是声称全网穷尽。第三轮仍有较高新来源率，后续维护应继续关注新建项目和许可变化。

## 内容工厂

严格通过 `content-factory-search-api` 的 curl 路径调用 `/search/api/query`，正常搜索默认最近三个月。成功查询包括：

| 查询 | 选定窗口 | 记录结果 |
| --- | ---: | ---: |
| `Agent 记忆库 OR 长期记忆 OR 记忆系统` | 30 天 | 20 |
| `OpenViking OR Hindsight OR MemSearch OR Honcho` | 90 天 | 30 |
| `Mem0 OR MemOS OR MemoryOS OR ReMe OR memU` | 30 天 | 20 |
| `Hy-Memory OR BEMULA OR AfterDeleteBench OR MemT` | 30 天 | 20 |

跨查询规范化后，内容工厂贡献 72 个不同来源。它帮助发现 Hy-Memory、MemT、BEMULA、记忆遗忘和 Hermes memory provider 等近期材料。

第二轮查询 `Hy-Memory OR M-flow OR BEMULA OR MemSkill` 在 curl 内置重试后仍返回 HTTP 503，间隔后再次尝试仍失败。该失败没有记作零结果；第三轮采用替代查询并成功返回。公开仓库只记录查询、窗口和统计，不发布私有服务地址、密钥或内部正文。

## 重要新增项目

相对 2026-10-15 原报告，本轮新增或重点更新了：

- **Hy-Memory**：腾讯的双系统认知记忆引擎与 SDK；与 MemHub 产品层分工明确。
- **TencentDB Agent Memory**：将对话、文档、代码组织为 Chat Memory、Skill、LLM-Wiki 与 Code-Graph 的团队记忆中心。
- **openJiuwen Agent Memory**：提供抽取、存储、检索、迁移和多形态记忆。
- **M-flow**：以多层认知图和受控传播实现图式记忆。
- **Mnemosyne**：SQLite、本地优先、跨宿主的记忆层；注意多个完全不同的同名仓库。
- **Membase**：SDK/CLI/MCP 记忆层；与 Memobase 不同。
- **MemT-1.0**：模型原生记忆路线，采用 PolyForm Noncommercial，不与外置记忆引擎混排。
- **MemoryStackBench / MPBench / OWASP Agent Memory Guard**：覆盖删除、证据、可审计性与记忆污染。

## 同名与版本纠偏

- `MemOS`、`MemoryOS`、`EverOS` 是三个项目。
- 两个 `MemForest` 对应不同论文和实现。
- `Engram` 至少有多个互不相同的仓库，许可从 MIT/Apache 到 AGPL/商业、PolyForm 均有。
- `agent-memory`、`agentmemory` 和 `Mnemosyne` 必须带 owner。
- Zep Community Edition 已进入 legacy；当前开源时序图核心优先看 Graphiti。
- OpenViking 的虚拟文件系统与 MemSearch 的 Markdown 真源不是同一种“三层读取”。
- Hindsight 的事实/时间/反思与 Honcho 的 peer 表征/视角建模不能只用“都能合成记忆”概括。

## 许可证处理

主表区分四种状态：开放许可证已核验、复合/拆分许可、source-available、待核验。以下项目不会被默认写成普通开源：

- Katra：BSL 1.1。
- Engram App：PolyForm Small Business + 商业许可。
- MemT-1.0：PolyForm Noncommercial。
- vincents-ai/engram：AGPL-3.0-or-later 或商业许可。
- MCP servers 父仓库：Apache/MIT 迁移期，文档 CC-BY。
- Agent Memory Radar：研究内容 CC-BY，维护代码 MIT。
- MemEngine 和部分独立 benchmark：未找到明确根目录许可证。

## 覆盖与未覆盖

用户报告基线：11 个必含实体和 51 个 GitHub URL 全部进入研究台账，覆盖率 100%。

外部 `mnemoverse/awesome-agent-memory`：实体与 URL 综合覆盖率 85.6%。未覆盖项主要是商业产品网站、徽章、许可证链接和 BYOK/API-key 等通用词；这些不是遗漏的 canonical 开源记忆仓库。外部列表仍有若干小型实验项目未纳入，后续应按实际实现、许可和维护状态逐项评估。

## 不能从本目录得出的结论

本轮没有部署 87 个项目、导入真实会话、复现 benchmark 或进行安全审计。作者自报的准确率、token 节省和性能数字没有进入跨项目总榜。GitHub star、提交量和最近更新时间只能帮助判断热度与维护迹象。

公平比较应使用相同中文材料、模型、预算、写入等待时间和 judge，分别测试事实、时序、多跳、用户画像、一次性例外、更正、作用域、删除残留、污染、恢复、延迟和总成本。

## 可复核文件

- [检索日志](../research/search-log.json)
- [收录决策与固定证据](../research/decisions.json)
- [用户基线覆盖](../research/coverage-user.json)
- [外部 awesome 覆盖](../research/coverage-external.json)
- [首版 GitHub 指标](../research/initial-metrics.json)
- [调研状态](../research/status.json)
- [完整性验证](../research/verification.json)

调研台账包含 847 个来源、174 条判断和 261 条 GitHub 指标。完整网页文本与本机工具日志保留在本地，不复制到公开仓库。
