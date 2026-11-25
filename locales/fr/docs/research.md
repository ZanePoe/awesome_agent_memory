# Méthode de recherche, mots-clés et journal de couverture

Date de recherche : 2026-11-12. L'objectif était de partir des trois rapports fournis par l'utilisateur pour construire un catalogue de projets de mémoire pour agents, maintenable dans la durée, et non de réordonner d'anciens rapports ou de copier une awesome list externe.

## Matériaux d'entrée

- `2026-10-15-开源Agent记忆库全景整理.md`
- `2026-10-16-Honcho记忆库架构与接入调研.md`
- `2026-10-16-OpenViking与Hindsight、MemSearch、Honcho对比调研.md`

Ces trois matériaux montrent ensemble que les différences ne se limitent pas à la base vectoriste : ce qu'il faut vraiment comparer, ce sont les objets de mémoire, la source de vérité, la capture et le traitement, le périmètre, les routes de récupération, les preuves, la correction/suppression, l'intégration à l'hôte et le coût des tâches de fond.

## Mots-clés

| Direction | Mots-clés anglais | Mots-clés chinois |
| --- | --- | --- |
| Couche mémoire complète | agent memory, long-term memory, memory layer, memory service | Agent 记忆库、长期记忆、记忆引擎 |
| Types cognitifs | episodic, semantic, procedural, working memory | 情景记忆、语义记忆、程序记忆、工作记忆 |
| Source fichier | markdown memory, file-backed, source of truth, Git-native | Markdown 真源、文件记忆、可审阅记忆 |
| Graphes et temps | temporal knowledge graph, entity memory, bi-temporal | 时序图谱、实体关系、双时态记忆 |
| Hôtes de codage | coding agent memory, MCP memory, Claude Code, Codex | 编码 Agent 记忆、MCP 记忆服务 |
| Évolution de l'expérience | experience memory, skill extraction, reflection, consolidation | 经验记忆、技能提炼、反思、休眠整理 |
| Gouvernance et risques | correction, deletion, forgetting, provenance, poisoning | 更正、删除、遗忘、来源、记忆污染 |
| Évaluation | LongMemEval, LoCoMo, MemoryAgentBench, BEAM | 长期记忆评测、删除残留、污染基准 |

Les requêtes larges mélangent bases de données ordinaires, agents complets, mémoire système et outils de favoris de navigateur ; les entrées finales sont donc toutes revérifiées sur le dépôt GitHub canonique, le README de la branche par défaut et la licence.

## Processus en trois passes

| Passe | Lots | Résultats | Nouvelles sources | Taux de nouvelles sources |
| --- | ---: | ---: | ---: | ---: |
| 1 | 14 | 579 | 534 | 92.2% |
| 2 | 7 | 125 | 110 | 88.0% |
| 3 | 6 | 281 | 203 | 72.2% |

La première passe a couvert la définition, les projets officiels, les index awesome, les dépôts GitHub, les comparaisons, les benchmarks, les risques et les projets récents, et a collecté `mnemoverse/awesome-agent-memory` comme base de couverture externe.

La deuxième passe a recherché, à partir des nouvelles entités, Hy-Memory, TencentDB Agent Memory, openJiuwen, M-flow, MemSkill, MemT, AfterDeleteBench, ainsi que la mémoire des agents de codage/MCP et les projets à licence restreinte.

La troisième passe a résolu les homonymes et les questions de périmètre entre Membase/Memobase, les multiples Mnemosyne et Open Agent Memory, puis a ajouté les évaluations de gouvernance MemoryStackBench, OWASP Agent Memory Guard et MPBench. Elle s'est terminée par l'enregistrement en lot des README figés et des métriques GitHub de tous les projets.

La raison d'arrêt est la limite de trois passes fixée à l'avance, pas une prétention d'exhaustivité sur tout le web. Le taux de nouvelles sources restant élevé à la troisième passe, la maintenance devra continuer à suivre les nouveaux projets et les changements de licence.

## Content factory

Appels strictement via le chemin curl de `content-factory-search-api` sur `/search/api/query` ; la fenêtre par défaut d'une recherche normale est le dernier trimestre. Les requêtes retenues :

| Requête | Fenêtre retenue | Résultats enregistrés |
| --- | ---: | ---: |
| `Agent 记忆库 OR 长期记忆 OR 记忆系统` | 30 jours | 20 |
| `OpenViking OR Hindsight OR MemSearch OR Honcho` | 90 jours | 30 |
| `Mem0 OR MemOS OR MemoryOS OR ReMe OR memU` | 30 jours | 20 |
| `Hy-Memory OR BEMULA OR AfterDeleteBench OR MemT` | 30 jours | 20 |

Après normalisation entre requêtes, la content factory a contribué 72 sources distinctes. Elle a aidé à découvrir des matériaux récents tels que Hy-Memory, MemT, BEMULA, l'oubli des mémoires et le fournisseur de mémoire Hermes.

La requête de la deuxième passe `Hy-Memory OR M-flow OR BEMULA OR MemSkill` a renvoyé HTTP 503 même après les retries intégrés de curl, et a échoué à nouveau après une pause. Cet échec n'a pas été consigné comme un résultat nul ; la troisième passe a utilisé des requêtes de substitution qui ont réussi. Le dépôt public n'enregistre que les requêtes, les fenêtres et les statistiques — jamais d'adresse de service privé, de clé ou de contenu interne.

## Principaux ajouts

Par rapport au rapport initial du 2026-10-15, cette passe a ajouté ou mis à jour en priorité :

- **Hy-Memory** : moteur de mémoire cognitive à deux systèmes de Tencent avec SDK Python ; répartition claire des rôles avec la couche produit MemHub.
- **TencentDB Agent Memory** : centre de mémoire d'équipe organisant conversations, documents et code en Chat Memory, Skills, LLM-Wiki et Code-Graph.
- **openJiuwen Agent Memory** : extraction, stockage, récupération, migration et mémoires multi-formes.
- **M-flow** : mémoire schématique par graphe cognitif multi-couches avec propagation contrôlée.
- **Mnemosyne** : couche de mémoire SQLite, locale par défaut, inter-hôtes ; attention à plusieurs dépôts homonymes totalement différents.
- **Membase** : couche de mémoire SDK/CLI/MCP ; distincte de Memobase.
- **MemT-1.0** : ligne de mémoire native du modèle, sous PolyForm Noncommercial ; ne pas mélanger avec les moteurs de mémoire externes.
- **MemoryStackBench / MPBench / OWASP Agent Memory Guard** : couvrent la suppression, les preuves, l'auditabilité et la pollution de mémoire.

## Homonymes et corrections de version

- `MemOS`, `MemoryOS` et `EverOS` sont trois projets distincts.
- Les deux `MemForest` correspondent à des articles et des implémentations différents.
- `Engram` compte au moins plusieurs dépôts mutuellement distincts, avec des licences allant de MIT/Apache à AGPL/commercial et PolyForm.
- `agent-memory`, `agentmemory` et `Mnemosyne` doivent toujours porter leur owner.
- Zep Community Edition est passé en legacy ; pour le graphe temporel open source actuel de l'écosystème Zep, regardez d'abord Graphiti.
- Le système de fichiers virtuel d'OpenViking et la source Markdown de MemSearch ne sont pas la même forme de « lecture à trois niveaux ».
- Les faits/temps/réflexion de Hindsight et la modélisation des représentations et points de vue par peer de Honcho ne se résument pas à « tous deux composent de la mémoire ».

## Traitement des licences

Le tableau principal distingue quatre états : licence ouverte vérifiée, licence composite/segmentée, code source visible, et à vérifier. Les projets suivants ne sont jamais présentés comme de l'open source ordinaire :

- Katra : BSL 1.1.
- Engram App : PolyForm Small Business + licence commerciale.
- MemT-1.0 : PolyForm Noncommercial.
- vincents-ai/engram : AGPL-3.0-or-later ou licence commerciale.
- Dépôt parent des serveurs MCP : transition Apache/MIT, documentation CC-BY.
- Agent Memory Radar : contenu de recherche CC-BY, code de maintenance MIT.
- MemEngine et certains benchmarks autonomes : aucune licence racine trouvée.

## Couverture et non-couverture

Base des rapports utilisateur : les 11 entités obligatoires et les 51 URLs GitHub sont toutes passées dans le registre de recherche, taux de couverture 100 %.

`mnemoverse/awesome-agent-memory` externe : couverture combinée entités + URLs de 85.6 %. Les éléments non couverts sont surtout des sites de produits commerciaux, des badges, des liens de licence et des termes génériques comme BYOK/clé d'API ; ce ne sont pas des dépôts canoniques de mémoire open source oubliés. La liste externe contient encore quelques petits projets expérimentaux non retenus, à évaluer un par un selon l'implémentation réelle, la licence et l'état de maintenance.

## Ce que ce catalogue ne permet pas de conclure

Cette passe n'a déployé aucun projet de la collection, n'a importé aucune session réelle, n'a reproduit aucun benchmark et n'a mené aucun audit de sécurité. Les chiffres d'exactitude, d'économie de tokens et de performance auto-déclarés par les auteurs n'entrent dans aucun classement transversal. Les étoiles GitHub, les volumes de commits et les dates de mise à jour ne renseignent que sur la visibilité et les signes de maintenance.

Une comparaison équitable exigerait les mêmes matériaux en chinois, le même modèle, le même budget, le même délai d'écriture et le même judge, pour tester séparément les faits, le temporel, le multi-sauts, le profil utilisateur, les exceptions ponctuelles, la correction, le périmètre, les résidus de suppression, la pollution, la reprise, la latence et le coût total.

## Fichiers vérifiables

- [Journal de recherche](../../../research/search-log.json)
- [Décisions d'admission et preuves figées](../../../research/decisions.json)
- [Couverture de la base utilisateur](../../../research/coverage-user.json)
- [Couverture de l'awesome externe](../../../research/coverage-external.json)
- [Premier instantané des métriques GitHub](../../../research/initial-metrics.json)
- [État de la recherche](../../../research/status.json)
- [Vérification de complétude](../../../research/verification.json)

Le registre de recherche contient 847 sources, 174 jugements et 261 entrées de métriques GitHub. Les textes web complets et les journaux d'outils locaux restent sur la machine d'audit et ne sont pas copiés dans le dépôt public.
