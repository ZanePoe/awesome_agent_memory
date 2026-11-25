# Périmètre et taxonomie

## Définition d'admission

Sont admis les dépôts autonomes dont la mémoire à long terme des agents est l'objectif principal : capture, organisation, interrogation, mise à jour ou injection d'informations entre les sessions ; ainsi que la mémoire fichier, les moteurs de graphes, les plugins d'assistants de codage, les Skills d'expérience et les outils d'évaluation qui servent directement ces flux.

Les bases vectoristes ordinaires, les bases de graphes, un simple champ intégré à un framework d'agents et les projets qui ne gardent qu'un cache de fenêtre de chat ne sont pas admis comme systèmes de mémoire autonomes. Les plateformes d'agents complètes, les outils de récupération et les applications de collecte de contexte n'entrent dans la catégorie « adjacente » que s'ils sont fréquemment utilisés dans des solutions de mémoire ou présentent une valeur de démarcation évidente.

## Les huit catégories principales

| Catégorie | Question de classement principale |
| --- | --- |
| Moteurs et services de mémoire | Fournit une API complète d'ingestion, de stockage, de récupération, de mise à jour ou de réflexion ? |
| Source fichier et mémoire consultable | Des fichiers ordinaires sont-ils la source de vérité éditable et transportable, et l'index peut-il être reconstruit ? |
| Graphes, entités et mémoire temporelle | Modélise principalement les entités, les relations, la validité temporelle, la dérivation ou les requêtes multi-sauts ? |
| Mémoire des agents de codage et MCP | Sert principalement des hôtes tels que Claude Code, Codex, OpenCode et la mémoire d'ingénierie projet ? |
| Expérience, compétences et mémoire procédurale | Transforme les traces d'exécution en opérations, stratégies, Skills ou workflows réutilisables ? |
| Implémentations de recherche et évaluation | Reproduit principalement des mécanismes d'articles, des jeux de données, des questions de sécurité/oubli ou des benchmarks ? |
| Plateformes, spécifications et index adjacents | Relève d'une plateforme d'agents complète, d'un composant de récupération, d'une spécification ou d'un index de couverture ? |
| Historique, archivés et licences restreintes | Est archivé/déprécié, ou sa licence n'est-elle pas de l'open source OSI classique ? |

Chaque dépôt est classé dans une seule catégorie principale. Les projets homonymes doivent porter leur owner ; `MemOS`, `MemoryOS`, `EverOS`, ainsi que les multiples `Engram`, `MemForest` et `agent-memory` sont des entités distinctes.

## Frontières de jugement

- Sauvegarder avec succès ne garantit pas un rappel correct plus tard, et un rappel réussi ne garantit pas que l'agent l'utilise correctement.
- Un Markdown consultable n'élimine pas les omissions de résumé ; les graphes et les mises en relation ne garantissent pas l'exactitude des faits.
- Supprimer un enregistrement source ne prouve pas automatiquement que les résumés, conclusions, arêtes du graphe, compétences, index et caches ont été purgés.
- scope, bank, collection, répertoires et workspace ne sont pas des frontières de sécurité intervertibles entre locataires.
- L'auto-hébergement des données n'implique pas que les modèles d'embedding, d'extraction, de rerank et de réflexion restent hors réseau.
- Les benchmarks d'un projet ne sont comparables que si le modèle, la division des données, le budget, le judge et les versions sont identiques.
- Noyau open source, service managé, versions commerciales et plugins peuvent relever de licences ou de chemins de données différents.

## Lecture en couches

Les fiches projets fournissent « positionnement, limites, licence, preuves à commit figé ». Le classement de maintenance aide seulement à juger la visibilité actuelle et l'activité de développement. Pour un choix réel, testez avec les mêmes matériaux en chinois la capture, la correction, l'isolation entre projets, la suppression, la reprise après arrêt, la latence P50/P95, le coût des modèles et le taux d'achèvement des tâches finales.
