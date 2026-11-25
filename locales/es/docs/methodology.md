# Método de ordenación y limitaciones

## Métricas de GitHub

`scripts/refresh_metrics.py` usa la API GraphQL de GitHub y lee todos los repositorios canonical en un instante UTC fijo. `data/metrics.json` solo se reemplaza de forma atómica cuando todos los lotes tienen éxito; un fallo parcial conserva la instantánea anterior y hace fallar la tarea.

- `stars`: proxy de atención en el momento de la recolección.
- `commits_30d / commits_90d`: conteo completo de commits del historial de la rama por defecto dentro de una ventana fija; incluye merges, bots y commits de documentación.
- `last_commit_at`: hora del commit HEAD de la rama por defecto.
- `pushed_at / updated_at`: se conservan para auditoría; no suplantan la hora de actualización del código en la rama por defecto.
- `latest_release`: release creada más recientemente; que no exista no equivale automáticamente a abandono.
- `archived / disabled`: estado del repositorio en GitHub.

## Estratos y fórmula

Primero se estratifica por estado de mantenimiento en cuatro capas: con commits en los últimos 90 días; sin commits desde hace 91–365 días; sin commits desde hace más de 365 días; y archivadas, disabled o históricas.

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
Puntuación de mantenimiento = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

Los empates se resuelven por estrellas y luego por orden estable de nombre de repositorio. Las cuatro vistas —puntuación combinada, estrellas, actividad a 90 días y último commit— estratifican primero por estado de mantenimiento. Para los valores sin estratificar, úsese el CSV.

## Qué no se puede inferir con esto

La puntuación de mantenimiento no es LongMemEval, LoCoMo, recall, precisión de respuestas, integridad del borrado, seguridad ni madurez de producción. Los monorepos y los commits automatizados amplifican la actividad aparente, una librería pequeña estable puede quedar subestimada y un repositorio de investigación tampoco necesita commits frecuentes sostenidos.

La identificación automática de licencias y la revisión manual van separadas. `NOASSERTION` nunca se escribe MIT por defecto; PolyForm, BSL, no comercial, dual y licencias divididas conservan sus fronteras originales. Los pesos de modelos, los datasets, las dependencias de terceros y los servicios gestionados pueden tener licencias propias.

## Sugerencia de evaluación de capacidades

Midiendo con el mismo modelo, presupuesto de tokens y datasets, conviene evaluar por separado: integridad de escritura, recall temporal/entidades/multihop, aciertos de evidencia, precisión de respuestas, efectividad de las correcciones del usuario, contaminación por excepciones puntuales, aislamiento entre proyectos, residuos tras el borrado, recuperación del proceso, latencia P50/P95 y coste total. No se debe montar un leaderboard combinando los mejores números autodeclarados por cada proveedor.
