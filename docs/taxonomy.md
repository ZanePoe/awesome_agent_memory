# Scope and taxonomy

## Inclusion definition

We catalogue standalone repositories whose main goal is long-term agent memory: those that handle cross-session information capture, organization, querying, updating or injection; plus file memory, graph engines, coding-assistant plugins, experience Skills and evaluation tools that directly serve these flows.

Plain vector databases, graph databases, a built-in field inside an agent framework, and projects that only cache the chat window are not included as standalone memory systems. Complete agent platforms, retrieval tools and context-capture apps enter the "adjacent" category only when they are commonly used in memory setups or clearly help draw a boundary.

## Eight primary categories

| Category | Primary test |
| --- | --- |
| Memory engines and services | Does it provide a complete ingestion, storage, retrieval, update or reflection API? |
| File-backed source-of-truth and auditable memory | Are plain files the editable, portable source of facts, and can the index be rebuilt? |
| Graphs, entities and temporal memory | Does it primarily model entities, relations, temporal validity, inference or multi-hop queries? |
| Coding agents and MCP memory | Does it primarily serve hosts such as Claude Code, Codex and OpenCode and project engineering memory? |
| Experience, skills and procedural memory | Does it turn execution traces into reusable operations, strategies, Skills or workflows? |
| Research implementations and benchmarks | Does it primarily reproduce paper mechanisms, datasets, safety/forgetting issues or benchmarks? |
| Adjacent platforms, specifications and indexes | Is it a complete agent platform, retrieval component, specification or coverage index? |
| Historical, archived and restricted licenses | Is it archived/deprecated, or is the license not regular OSI open source? |

Each repository goes into exactly one primary category. Same-named projects must carry an owner; `MemOS`, `MemoryOS`, `EverOS`, and the multiple `Engram`, `MemForest` and `agent-memory` projects are distinct entities.

## Judgment boundaries

- Storing something does not mean it will be recalled correctly later, and a successful recall does not mean the agent uses it correctly.
- Reviewable Markdown does not remove summarization gaps; graphs and links do not guarantee factual correctness.
- Deleting a source record does not automatically prove that summaries, conclusions, graph edges, skills, indexes and caches were all cleaned.
- scope, bank, collection, directory and workspace are not freely interchangeable tenant security boundaries.
- Self-hosted data does not automatically mean embedding, extraction, rerank and reflection models stay off-network.
- Project benchmarks are comparable only when model, data split, budget, judge and version are the same.
- Open-source cores, hosted services, commercial editions and plugins may use different licenses or data paths.

## Layered reading

Each project entry provides "positioning, boundary, license, pinned-commit evidence". Maintenance rankings only help judge current attention and development activity. Real selection should use the same Chinese-language material and test capture, correction, project isolation, deletion, background recovery, P50/P95 latency, model cost and final task completion rate.
