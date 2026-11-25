# Alcance y categorías

## Definición de inclusión

Se incluyen repositorios independientes cuya meta principal sea la memoria de largo plazo de agentes: los que gestionan captura, organización, consulta, actualización o inyección de información entre sesiones; así como la memoria en archivos, los motores de grafos, los complementos para agentes de programación, las Skills de experiencia y las herramientas de evaluación que sirven directamente a esos flujos.

Las bases de datos vectoriales y de grafos corrientes, un campo de memoria integrado dentro de un framework de agentes y los proyectos que solo guardan la caché de la ventana de chat no se incluyen como sistemas de memoria independientes. Las plataformas completas de agentes, las herramientas de recuperación y las aplicaciones de captura de contexto entran en la categoría "adyacente" solo si se usan habitualmente en soluciones de memoria o aportan un valor de frontera claro.

## Las ocho categorías principales

| Categoría | Pregunta decisiva principal |
| --- | --- |
| Motores y servicios de memoria | ¿Ofrece una API completa de ingesta, almacenamiento, recuperación, actualización o reflexión? |
| Archivos como fuente de verdad y memoria auditable | ¿Son los archivos corrientes la fuente de verdad editable y migrable, y se puede reconstruir el índice? |
| Grafos, entidades y memoria temporal | ¿Modela principalmente entidades, relaciones, validez temporal, inferencia o consultas multihop? |
| Agentes de programación y memoria MCP | ¿Sirve principalmente a hospedadores como Claude Code, Codex u OpenCode y a la memoria de ingeniería de proyecto? |
| Experiencia, habilidades y memoria procedimental | ¿Convierte trayectorias de ejecución en operaciones, estrategias, Skills o flujos de trabajo reutilizables? |
| Implementaciones de investigación y evaluación | ¿Reproduce principalmente mecanismos de papers, conjuntos de datos, problemas de seguridad/olvido o benchmarks? |
| Plataformas adyacentes, especificaciones e índices | ¿Pertenece a una plataforma completa de agentes, a componentes de recuperación, a especificaciones o a índices de cobertura? |
| Histórico, archivado y licencias restringidas | ¿Está archivado o abandonado, o su licencia no es open source OSI convencional? |

Cada repositorio se coloca en una sola categoría principal. Los proyectos homónimos deben llevar owner; `MemOS`, `MemoryOS` y `EverOS`, así como los varios `Engram`, `MemForest` y `agent-memory`, son entidades distintas.

## Fronteras de juicio

- Que algo se guarde bien no significa que luego se recuerde bien, y recuperar con éxito tampoco garantiza que el agente lo use correctamente.
- Que Markdown sea auditable no elimina las omisiones del resumen; los grafos y las asociaciones tampoco garantizan que los hechos sean correctos.
- Borrar el registro de origen no prueba por sí solo que se hayan limpiado resúmenes, conclusiones, aristas del grafo, skills, índices y cachés.
- scope, bank, collection, los directorios y el workspace no son fronteras de seguridad de inquilinos intercambiables a voluntad.
- Datos autoalojados no implican por sí mismos que los modelos de embedding, extracción, rerank y reflexión no salgan de la red.
- Los benchmarks de un proyecto solo son comparables cuando coinciden modelo, split de datos, presupuesto, judge y versión.
- El núcleo open source, el servicio gestionado, la versión comercial y los plugins pueden usar licencias o rutas de datos distintas.

## Lectura por capas

Las entradas ofrecen "propósito, frontera, licencia y evidencia en un commit fijo". El ranking de mantenimiento solo ayuda a juzgar atención actual y actividad de desarrollo. Una selección real debe usar los mismos materiales en chino y probar captura, corrección, aislamiento entre proyectos, borrado, recuperación en segundo plano, latencia P50/P95, coste de modelos y tasa de finalización de tareas.
