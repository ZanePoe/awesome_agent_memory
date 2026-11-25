# Contributing guide

New projects and corrections to category, naming, license or feature boundary are welcome. A low star count is not a reason for rejection.

1. Edit `data/projects.json`; do not edit the generated README tables directly.
2. Provide the canonical GitHub repository, one primary category, functional positioning, an explicit boundary and README sources at a pinned commit.
3. Same-named projects must be written with the full owner/repo; a fork is listed separately only when its implementation or maintenance path clearly differs.
4. Distinguish engines, file sources of truth, graphs, host plugins, research code and plain databases.
5. Distinguish implemented features, roadmaps, author benchmarks and this catalogue's own testing. The current catalogue has not run a unified capability evaluation of all projects.
6. Verify licenses in the root and in subdirectories. Public source code, free use and OSI open source are not the same concept.
7. After adding a repository, refresh the full metrics and regenerate:

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

Do not commit API keys, internal content-factory addresses, real private sessions or unredacted memory data. Research and change records go under `record/` as `YYYY-MM-DD-<chinese-topic>.md`.

## Multilingual files

- `data/projects.json` is the canonical reviewed data in Chinese: a fact changes there exactly once.
- Wording for other languages comes from `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`) and `locales/<lang>/ui.json`; `zh` falls back directly to `data/projects.json`, so there is no `locales/zh/entries.json`.
- When you add a project or re-word its positioning, boundary or license verdict, complete the en/es/hi/fr locales in the same pull request; otherwise `python scripts/build.py --check` and `python -m unittest discover -s tests -v` fail.
- Static prose: English lives in root `docs/` and `CONTRIBUTING.md`; other languages live at the same relative paths under `locales/<lang>/`. Relative links inside a mirror resolve from that file's own directory — from `locales/<lang>/docs/` a link to the repository root (`data/`, `scripts/`, `research/`, `LICENSE`, `record/`) needs `../../../`, while from `locales/<lang>/CONTRIBUTING.md` it needs `../../`; `docs/readme-intro.md` is the exception, because it is inlined into the README and resolves from the locale root.
- `record/` and `research/` keep the original language used when they were written, as audit trails; they are not machine-translated.
- Generated files (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` and the same-named files in each locale mirror) are never edited by hand; they are produced by `python scripts/build.py`.
