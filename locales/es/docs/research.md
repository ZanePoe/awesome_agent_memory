# Método de búsqueda, palabras clave y registro de cobertura

Fecha de investigación: 2026-11-12. El objetivo era partir de los tres informes del usuario y construir un catálogo de proyectos de memoria para agentes mantenible en el tiempo, no reordenar los informes antiguos ni copiar listas awesome externas.

## Materiales de entrada

- `2026-10-15-开源Agent记忆库全景整理.md`
- `2026-10-16-Honcho记忆库架构与接入调研.md`
- `2026-10-16-OpenViking与Hindsight、MemSearch、Honcho对比调研.md`

Los tres materiales coinciden en que las diferencias de la memoria para agentes no se reducen a la base vectorial: lo que hay que comparar son los objetos de memoria, la fuente de verdad, la captura y el procesamiento, el alcance, las rutas de recuperación, la evidencia, la corrección/borrado, la integración con el hospedador y el coste en segundo plano.

## Términos de búsqueda

| Dirección | Palabras clave en inglés | Palabras clave en chino |
| --- | --- | --- |
| Capa de memoria completa | agent memory, long-term memory, memory layer, memory service | Agent 记忆库、长期记忆、记忆引擎 |
| Tipos cognitivos | episodic, semantic, procedural, working memory | 情景记忆、语义记忆、程序记忆、工作记忆 |
| Archivos como fuente de verdad | markdown memory, file-backed, source of truth, Git-native | Markdown 真源、文件记忆、可审阅记忆 |
| Grafos y tiempo | temporal knowledge graph, entity memory, bi-temporal | 时序图谱、实体关系、双时态记忆 |
| Hospedadores de programación | coding agent memory, MCP memory, Claude Code, Codex | 编码 Agent 记忆、MCP 记忆服务 |
| Evolución de experiencia | experience memory, skill extraction, reflection, consolidation | 经验记忆、技能提炼、反思、休眠整理 |
| Gobernanza y riesgo | correction, deletion, forgetting, provenance, poisoning | 更正、删除、遗忘、来源、记忆污染 |
| Evaluación | LongMemEval, LoCoMo, MemoryAgentBench, BEAM | 长期记忆评测、删除残留、污染基准 |

Las consultas amplias mezclan bases de datos corrientes, agentes completos, memoria de sistemas operativos y herramientas de guardado de navegador; por eso cada entrada final volvió al repositorio GitHub canonical, al README de la rama por defecto y a la licencia para su verificación.

## Proceso en tres rondas

| Ronda | Lotes | Resultados | Nuevas fuentes | Tasa de nuevas fuentes |
| --- | ---: | ---: | ---: | ---: |
| 1 | 14 | 579 | 534 | 92.2% |
| 2 | 7 | 125 | 110 | 88.0% |
| 3 | 6 | 281 | 203 | 72.2% |

La primera ronda cubrió definiciones, proyectos oficiales, índices awesome, repositorios de GitHub, comparativas, benchmarks, riesgos y proyectos recientes, y recogió `mnemoverse/awesome-agent-memory` como línea base de cobertura externa.

La segunda ronda completó, a partir de las entidades nuevas, Hy-Memory, TencentDB Agent Memory, openJiuwen, M-flow, MemSkill, MemT, AfterDeleteBench, además de memoria para agentes de programación/MCP y proyectos de licencia restringida.

La tercera ronda resolvió homónimos y problemas de alcance como Membase/Memobase, los varios Mnemosyne y Open Agent Memory, e incorporó evaluaciones de gobernanza como MemoryStackBench, OWASP Agent Memory Guard y MPBench. Al final se registraron en lote los README fijados a commit y las métricas de GitHub de todos los proyectos.

La razón de parar fue el límite de tres rondas fijado de antemano, no la pretensión de haber agotado todo lo existente. La tercera ronda aún tenía una tasa alta de nuevas fuentes, así que el mantenimiento posterior debe seguir atento a proyectos recién creados y cambios de licencia.

## Content Factory

Se llamó a `/search/api/query` exclusivamente por la ruta curl de `content-factory-search-api`; las búsquedas normales cubren por defecto los últimos tres meses. Las consultas con éxito fueron:

| Consulta | Ventana elegida | Resultados registrados |
| --- | ---: | ---: |
| `Agent 记忆库 OR 长期记忆 OR 记忆系统` | 30 días | 20 |
| `OpenViking OR Hindsight OR MemSearch OR Honcho` | 90 días | 30 |
| `Mem0 OR MemOS OR MemoryOS OR ReMe OR memU` | 30 días | 20 |
| `Hy-Memory OR BEMULA OR AfterDeleteBench OR MemT` | 30 días | 20 |

Tras normalizar entre consultas, Content Factory aportó 72 fuentes distintas. Ayudó a encontrar materiales recientes como Hy-Memory, MemT, BEMULA, olvido de memorias y el proveedor de memoria de Hermes.

La consulta de la segunda ronda `Hy-Memory OR M-flow OR BEMULA OR MemSkill` devolvió HTTP 503 incluso con los reintentos integrados de curl, y volvió a fallar tras un intervalo. Ese fallo no se registró como cero resultados; la tercera ronda usó consultas alternativas que sí tuvieron éxito. El repositorio público solo registra consultas, ventanas y estadísticas: no publica direcciones de servicios privados, claves ni cuerpos internos.

## Proyectos nuevos destacados

Frente al informe original del 2026-10-15, en esta ronda se añadieron o actualizaron en profundidad:

- **Hy-Memory**: motor de memoria cognitiva de doble sistema y SDK de Tencent; la división de funciones con la capa de producto MemHub es clara.
- **TencentDB Agent Memory**: centro de memoria para equipos que organiza conversaciones, documentos y código en Chat Memory, Skills, LLM-Wiki y Code-Graph.
- **openJiuwen Agent Memory**: ofrece extracción, almacenamiento, recuperación, migración y memoria en múltiples formas.
- **M-flow**: memoria en grafo con niveles cognitivos múltiples y propagación controlada.
- **Mnemosyne**: capa de memoria SQLite, local-first y entre hospedadores; ojo con varios repositorios homónimos completamente distintos.
- **Membase**: capa de memoria SDK/CLI/MCP; no es Memobase.
- **MemT-1.0**: ruta de memoria nativa del modelo, bajo PolyForm Noncommercial; no se mezcla con los motores de memoria externa.
- **MemoryStackBench / MPBench / OWASP Agent Memory Guard**: cubren borrado, evidencia, auditabilidad y contaminación de memoria.

## Homónimos y correcciones de versión

- `MemOS`, `MemoryOS` y `EverOS` son tres proyectos.
- Los dos `MemForest` corresponden a papers e implementaciones distintos.
- `Engram` tiene al menos varios repositorios mutuamente distintos, con licencias que van de MIT/Apache a AGPL/comercial y PolyForm.
- `agent-memory`, `agentmemory` y `Mnemosyne` deben escribirse con owner.
- Zep Community Edition pasó a legacy; para el núcleo de grafos temporales open source actual, la referencia prioritaria es Graphiti.
- El sistema de archivos virtual de OpenViking y la fuente de verdad Markdown de MemSearch no son la misma "lectura en tres capas".
- La doble faceta hecho/tiempo/reflexión de Hindsight y el modelado de representaciones/perspectivas de pares de Honcho no se pueden resumir en "los dos sintetizan memoria".

## Tratamiento de licencias

La tabla principal distingue cuatro estados: licencia abierta verificada, licencia compuesta/dividida, source-available y pendiente de verificación. Los siguientes proyectos no se escriben como open source corriente por defecto:

- Katra: BSL 1.1.
- Engram App: PolyForm Small Business + licencia comercial.
- MemT-1.0: PolyForm Noncommercial.
- vincents-ai/engram: AGPL-3.0-or-later o licencia comercial.
- Repositorio padre de MCP servers: periodo de transición Apache/MIT, documentación CC-BY.
- Agent Memory Radar: contenido de investigación CC-BY, código de mantenimiento MIT.
- MemEngine y varios benchmarks independientes: no se encontró licencia explícita en la raíz.

## Cobertura y no cobertura

Línea base de los informes del usuario: las 11 entidades obligatorias y las 51 URLs de GitHub entraron todas en el registro de investigación; cobertura del 100%.

Frente al índice externo `mnemoverse/awesome-agent-memory`: la cobertura combinada de entidades y URLs es del 85.6%. Los no cubiertos son sobre todo sitios de productos comerciales, badges, enlaces de licencia y términos genéricos como BYOK/API-key; no son repositorios canonical de memoria open source que se hayan pasado por alto. La lista externa también tiene varios proyectos experimentales pequeños sin incluir; más adelante deben evaluarse uno por uno según implementación real, licencia y estado de mantenimiento.

## Conclusiones que no pueden extraerse de este catálogo

En esta ronda no se desplegaron los proyectos del catálogo, no se importaron sesiones reales, no se replicaron benchmarks ni se hicieron auditorías de seguridad. Las cifras autodeclaradas de precisión, ahorro de tokens y rendimiento no entran en ninguna tabla comparativa. Las estrellas, los commits y la hora de actualización en GitHub solo ayudan a juzgar popularidad y señales de mantenimiento.

Una comparación justa debe usar los mismos materiales en chino, los mismos modelos, presupuesto, espera de escritura y judge, y probar por separado hechos, temporalidad, multihop, perfil de usuario, excepciones puntuales, corrección, alcance, residuos tras el borrado, contaminación, recuperación, latencia y coste total.

## Archivos verificables

- [Registro de búsquedas](../../../research/search-log.json)
- [Decisiones de inclusión y evidencia fijada](../../../research/decisions.json)
- [Cobertura de la línea base del usuario](../../../research/coverage-user.json)
- [Cobertura del awesome externo](../../../research/coverage-external.json)
- [Métricas iniciales de GitHub](../../../research/initial-metrics.json)
- [Estado de la investigación](../../../research/status.json)
- [Verificación de integridad](../../../research/verification.json)

El registro de investigación contiene 847 fuentes, 174 juicios y 261 métricas de GitHub. El texto web completo y los logs de herramientas locales se conservan en la máquina local y no se copian al repositorio público.
