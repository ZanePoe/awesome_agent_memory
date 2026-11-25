# Guide de contribution

Les ajouts de projets et les corrections de catégorie, de nom, de licence ou de frontière fonctionnelle sont bienvenus. Un nombre d'étoiles faible n'est pas un motif de refus.

1. Modifiez `data/projects.json` ; n'éditez jamais directement les tableaux générés du README.
2. Fournissez le dépôt GitHub canonique, une catégorie principale, le positionnement, des limites claires et des preuves README lues à un commit figé.
3. Les projets homonymes doivent porter le owner/repo complet ; un fork n'est listé à part que si son implémentation ou sa ligne de maintenance diffère clairement.
4. Distinguez moteur, source fichier, graphe, plugin d'hôte, code de recherche et base de données ordinaire.
5. Distinguez ce qui est implémenté, ce qui est roadmap, le benchmark de l'auteur et les mesures de ce catalogue. Le catalogue n'a pas exécuté ni évalué tous les projets de façon uniforme.
6. Vérifiez les licences à la racine et dans les sous-répertoires. Code source visible, usage gratuit et open source OSI ne sont pas le même concept.
7. Après un ajout de dépôt, rafraîchissez toutes les métriques et régénérez :

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

Ne commitez aucune clé API, adresse interne de content factory, session privée réelle ni donnée de mémoire non désanonymisée. Les journaux de recherche et de modification se placent dans `record/`, nommés `YYYY-MM-DD-<sujet>.md` avec un sujet rédigé en chinois.

## Fichiers multilingues

- `data/projects.json` porte les données de revue canoniques, en chinois : un fait ne se corrige qu'à cet endroit.
- Le texte des autres langues vient de `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`) et de `locales/<lang>/ui.json` ; `zh` retombe directement sur `data/projects.json`, il n'existe donc pas de `locales/zh/entries.json`.
- Lors d'un ajout de projet ou d'une reformulation du positionnement, des limites ou d'une conclusion de licence, complétez les quatre locales en/es/hi/fr dans la même pull request ; sinon `python scripts/build.py --check` et `python -m unittest discover -s tests -v` échouent.
- Prose statique : l'anglais vit dans `docs/` et `CONTRIBUTING.md` à la racine, les autres langues dans les mêmes chemins relatifs sous `locales/<lang>/`. Dans une copie miroir, les liens relatifs se résolvent depuis le dossier du fichier lui-même : pointez vers la racine du dépôt avec `../../` pour `data/`, `scripts/`, `research/`, `LICENSE` et `record/` ; `docs/readme-intro.md` fait exception, car il est inséré dans le README et se résout depuis la racine de la langue.
- `record/` et `research/` conservent le texte d'origine dans la langue où ils ont été écrits, comme trace d'audit ; pas de traduction automatique.
- Les fichiers générés (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` et leurs homologues dans les miroirs de langue) ne sont jamais modifiés à la main ; ils proviennent de `python scripts/build.py`.
