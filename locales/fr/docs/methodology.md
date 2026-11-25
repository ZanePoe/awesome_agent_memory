# Méthode de classement et limites

## Métriques GitHub

`scripts/refresh_metrics.py` utilise l'API GraphQL de GitHub et lit tous les dépôts canoniques à un instant UTC fixe. `data/metrics.json` n'est remplacé atomiquement qu'après la réussite de tous les lots ; un échec partiel conserve l'ancien instantané et fait échouer la tâche.

- `stars` : indicateur proxy de l'attention au moment de la collecte.
- `commits_30d / commits_90d` : comptage complet des commits de l'historique de la branche par défaut sur une fenêtre fixe, fusions, bots et commits documentaires inclus.
- `last_commit_at` : horodatage du commit HEAD de la branche par défaut.
- `pushed_at / updated_at` : conservés pour l'audit ; ils ne simulent pas une mise à jour du code de la branche par défaut.
- `latest_release` : la release créée la plus récente ; son absence n'indique pas automatiquement l'abandon.
- `archived / disabled` : état du dépôt sur GitHub.

## Strates et formule

Quatre strates selon l'état de maintenance : commits sur les 90 derniers jours ; aucun commit depuis 91–365 jours ; aucun commit depuis plus de 365 jours ; archives, disabled ou projets historiques.

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
score_de_maintenance = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

À score égal, on compare les étoiles, puis on trie stablement par nom de dépôt. Les quatre vues — composite, étoiles, activité 90 jours, dernier commit — stratifient d'abord par état de maintenance. Utilisez le CSV lorsque vous avez besoin des valeurs brutes sans strates.

## Ce qu'on ne peut pas en déduire

Le score de maintenance n'est ni LongMemEval, ni LoCoMo, ni un taux de rappel, une précision de réponse, une intégrité de suppression, une sécurité ou une maturité de production. Les monorepos et les commits automatiques gonflent l'activité ; une petite bibliothèque stable peut être sous-évaluée, et un dépôt de recherche n'a pas besoin de commits fréquents et continus.

La détection automatique des licences et la revue humaine sont séparées. `NOASSERTION` ne devient jamais MIT par défaut ; PolyForm, BSL, non commercial, double licence et licences segmentées conservent leurs frontières d'origine. Les poids de modèles, les jeux de données, les dépendances tierces et les services managés peuvent relever d'autres licences.

## Recommandations d'évaluation des capacités

Mesurez, sur le même modèle, le même budget de tokens et les mêmes jeux de données : intégrité de l'écriture, rappel temporel/entityel/multi-sauts, réussite sur les preuves, exactitude des réponses, effet des corrections utilisateur, pollution par exceptions ponctuelles, isolation entre projets, résidus après suppression, reprise de processus, latence P50/P95 et coût total. Ne composez pas un palmarès avec les meilleurs chiffres auto-déclarés par chaque fournisseur.
