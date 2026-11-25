# Guía de contribución

Se aceptan nuevos proyectos y correcciones de categoría, nombre, licencia o fronteras funcionales. Tener pocas estrellas no es motivo de rechazo.

1. Modifica `data/projects.json`; no edites a mano las tablas del README generado.
2. Aporta el repositorio GitHub canonical, una categoría principal, el propósito funcional, fronteras explícitas y la fuente del README en un commit fijo.
3. Los proyectos homónimos deben escribirse con owner/repo completos; un fork se lista aparte solo si su implementación o su ruta de mantenimiento difieren de forma clara.
4. Distingue motores, fuente de verdad en archivos, grafos, plugins de hospedador, código de investigación y bases de datos corrientes.
5. Distingue lo implementado, lo anunciado en roadmap, los benchmarks del autor y lo que este catálogo midió realmente. La versión actual no ha ejecutado una evaluación unificada de todos los proyectos.
6. Verifica las licencias del directorio raíz y de los subdirectorios. Código fuente público, uso gratuito y OSI open source no son el mismo concepto.
7. Tras añadir un repositorio, refresca todas las métricas y regenera:

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

No subas claves de API, direcciones internas de Content Factory, sesiones privadas reales ni datos de memoria sin desidentificar. Los registros de investigación y de cambios van en `record/YYYY-MM-DD-tema-en-chino.md` (los registros de auditoría se conservan en chino, tal como se redactaron en el momento de la verificación).

## Archivos multiidioma

- `data/projects.json` son los datos de revisión canonical en chino: los hechos solo se corrigen allí una vez.
- La redacción de los demás idiomas proviene de `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`) y `locales/<lang>/ui.json`; `zh` cae directamente a `data/projects.json`, por eso no existe `locales/zh/entries.json`.
- Al añadir un proyecto o reescribir propósito, fronteras o conclusiones de licencia, completa en el mismo PR los cuatro locales en/es/hi/fr; de lo contrario fallarán `python scripts/build.py --check` y `python -m unittest discover -s tests -v`.
- Documentos estáticos: el inglés va en `docs/` y `CONTRIBUTING.md` de la raíz; los demás idiomas, en las mismas rutas relativas bajo `locales/<lang>/`. Los enlaces relativos de un mirror se residen desde el directorio del propio archivo, y los que apuntan al raíz del repositorio (`data/`, `scripts/`, `research/`, `LICENSE`, `record/`) deben escribirse con `../../`; `docs/readme-intro.md` es la excepción: se incrusta en el README y se resuelve desde la raíz del idioma.
- `record/` y `research/` conservan el texto original con el que se escribieron, como huella de auditoría; no se traducen automáticamente.
- Los artefactos generados (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` y sus homónimos en cada mirror de idioma) no se editan a mano: los produce `python scripts/build.py`.
