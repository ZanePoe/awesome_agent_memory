# Search method, keywords and coverage log

Research date: 2026-11-12. The goal was to build a sustainably updatable catalogue of agent-memory projects starting from three user reports, not to reshuffle the old reports or simply copy an external awesome list.

## Input material

- `2026-10-15-开源Agent记忆库全景整理.md`
- `2026-10-16-Honcho记忆库架构与接入调研.md`
- `2026-10-16-OpenViking与Hindsight、MemSearch、Honcho对比调研.md`

Together the three reports show that agent memory differs in more than the vector store: the real comparison covers memory objects, sources of truth, capture and processing, scoping, retrieval routes, evidence, correction/deletion, host integration and background cost.

## Search keywords

| Direction | English keywords | Chinese keywords |
| --- | --- | --- |
| Complete memory layers | agent memory, long-term memory, memory layer, memory service | Agent 记忆库、长期记忆、记忆引擎 |
| Cognitive types | episodic, semantic, procedural, working memory | 情景记忆、语义记忆、程序记忆、工作记忆 |
| File sources of truth | markdown memory, file-backed, source of truth, Git-native | Markdown 真源、文件记忆、可审阅记忆 |
| Graphs and time | temporal knowledge graph, entity memory, bi-temporal | 时序图谱、实体关系、双时态记忆 |
| Coding hosts | coding agent memory, MCP memory, Claude Code, Codex | 编码 Agent 记忆、MCP 记忆服务 |
| Experience evolution | experience memory, skill extraction, reflection, consolidation | 经验记忆、技能提炼、反思、休眠整理 |
| Governance risks | correction, deletion, forgetting, provenance, poisoning | 更正、删除、遗忘、来源、记忆污染 |
| Benchmarks | LongMemEval, LoCoMo, MemoryAgentBench, BEAM | 长期记忆评测、删除残留、污染基准 |

Broad queries mix in ordinary databases, complete agents, operating-system memory and browser-booking tools, so every final entry was verified against its canonical GitHub repository, default-branch README and license.

## Three-round process

| Round | Batches | Results | New sources | New-source rate |
| --- | ---: | ---: | ---: | ---: |
| 1 | 14 | 579 | 534 | 92.2% |
| 2 | 7 | 125 | 110 | 88.0% |
| 3 | 6 | 281 | 203 | 72.2% |

Round 1 covered definitions, official projects, awesome indexes, GitHub repositories, comparisons, benchmarks, risks and recent projects, and collected `mnemoverse/awesome-agent-memory` as an external coverage baseline.

Round 2 followed up on new entities and re-checked Hy-Memory, TencentDB Agent Memory, openJiuwen, M-flow, MemSkill, MemT, AfterDeleteBench, plus coding-agent/MCP memory and restricted-license projects.

Round 3 resolved name and scope issues such as Membase/Memobase, the multiple Mnemosyne projects and Open Agent Memory, and added governance benchmarks such as MemoryStackBench, OWASP Agent Memory Guard and MPBench. Finally, pinned READMEs and GitHub metrics were registered for all projects in one batch.

The stop condition was the preset three-round limit, not a claim of internet-wide exhaustiveness. Round 3 still had a high new-source rate, so ongoing maintenance should keep watching newly created projects and license changes.

## Content factory

Queries went strictly through the `content-factory-search-api` curl path against `/search/api/query`; normal searches default to the last three months. Successful queries:

| Query | Selected window | Logged results |
| --- | ---: | ---: |
| `Agent 记忆库 OR 长期记忆 OR 记忆系统` | 30 days | 20 |
| `OpenViking OR Hindsight OR MemSearch OR Honcho` | 90 days | 30 |
| `Mem0 OR MemOS OR MemoryOS OR ReMe OR memU` | 30 days | 20 |
| `Hy-Memory OR BEMULA OR AfterDeleteBench OR MemT` | 30 days | 20 |

After cross-query normalization, the content factory contributed 72 distinct sources. It helped surface recent material such as Hy-Memory, MemT, BEMULA, memory-forgetting work and the Hermes memory provider.

The round-2 query `Hy-Memory OR M-flow OR BEMULA OR MemSkill` still returned HTTP 503 after curl's built-in retries, and a spaced re-attempt also failed. This failure was not recorded as a zero-result; round 3 used an alternative query that returned successfully. Public repositories record only the queries, windows and statistics — no private service addresses, keys or internal payloads are published.

## Notable new projects

Compared with the original 2026-10-15 report, this round added or prominently updated:

- **Hy-Memory**: Tencent's dual-system cognitive memory engine and SDK; the division of labor with the MemHub product layer is explicit.
- **TencentDB Agent Memory**: a team memory hub that organizes conversations, documents and code into Chat Memory, Skills, LLM-Wiki and Code-Graph.
- **openJiuwen Agent Memory**: extraction, storage, retrieval, migration and multi-form memory.
- **M-flow**: schematic memory via a multi-layer cognitive graph with controlled propagation.
- **Mnemosyne**: a SQLite, local-first, cross-host memory layer; beware of several completely different same-named repositories.
- **Membase**: an SDK/CLI/MCP memory layer; different from Memobase.
- **MemT-1.0**: a model-native memory route under PolyForm Noncommercial, not ranked together with external memory engines.
- **MemoryStackBench / MPBench / OWASP Agent Memory Guard**: covering deletion, evidence, auditability and memory poisoning.

## Name and version corrections

- `MemOS`, `MemoryOS` and `EverOS` are three projects.
- The two `MemForest` repositories correspond to different papers and implementations.
- `Engram` has at least several mutually distinct repositories, with licenses ranging from MIT/Apache to AGPL/commercial and PolyForm.
- `agent-memory`, `agentmemory` and `Mnemosyne` must carry owners.
- Zep Community Edition has moved to legacy; for the current open-source temporal graph core, prefer Graphiti.
- OpenViking's virtual file system and MemSearch's Markdown source of truth are not the same "three-tier reading".
- Hindsight's fact/temporal/reflection layers and Honcho's peer-representation/perspective modeling cannot be summarized just as "both can synthesize memory".

## License handling

The main table distinguishes four statuses: open license verified, compound/split license, source-available and unverified. The following projects are never written as ordinary open source by default:

- Katra: BSL 1.1.
- Engram App: PolyForm Small Business + commercial license.
- MemT-1.0: PolyForm Noncommercial.
- vincents-ai/engram: AGPL-3.0-or-later or commercial license.
- The MCP servers parent repository: an Apache/MIT transition period, docs CC-BY.
- Agent Memory Radar: research content CC-BY, maintenance code MIT.
- MemEngine and some standalone benchmarks: no explicit root-directory license found.

## Coverage and gaps

User-report baseline: all 11 required entities and 51 GitHub URLs entered the research ledger — 100% coverage.

External `mnemoverse/awesome-agent-memory`: combined entity-and-URL coverage of 85.6%. The uncovered items are mostly commercial product websites, badges, license links and generic terms such as BYOK/API-key; these are not missed canonical open-source memory repositories. Several small experimental projects in the external list are still not adopted; later maintenance should assess them one by one on actual implementation, license and maintenance status.

## What this catalogue cannot conclude

This round did not deploy the catalogued projects, import real conversations, reproduce benchmarks or run security audits. Author-reported accuracy, token-savings and performance numbers were kept out of any cross-project leaderboard. GitHub stars, commit volume and last-update time only help judge popularity and maintenance signals.

A fair comparison should use the same Chinese-language material, models, budgets, write-wait times and judges, and test facts, temporal queries, multi-hop, user profiling, one-off exceptions, corrections, scoping, deletion residue, poisoning, recovery, latency and total cost separately.

## Verifiable files

- [Search log](../research/search-log.json)
- [Inclusion decisions and pinned evidence](../research/decisions.json)
- [User baseline coverage](../research/coverage-user.json)
- [External awesome coverage](../research/coverage-external.json)
- [First-release GitHub metrics](../research/initial-metrics.json)
- [Research status](../research/status.json)
- [Completeness verification](../research/verification.json)

The research ledger contains 847 sources, 174 judgments and 261 GitHub metrics. Full web page text and local tool logs stay local and are not copied into the public repository.
