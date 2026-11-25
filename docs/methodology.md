# Ranking method and limits

## GitHub metrics

`scripts/refresh_metrics.py` uses the GitHub GraphQL API to read all canonical repositories at one fixed UTC moment. `data/metrics.json` is replaced atomically only after every batch succeeds. The one exception is a repository GitHub can no longer resolve (renamed away or deleted): its previous record is carried forward and marked `missing_upstream` with a `missing_since` timestamp, so a single vanished project cannot break the daily refresh. Rate limits, transport failures and partial GraphQL responses still abort the run and keep the previous snapshot whole.

- `stars`: a proxy for attention at collection time.
- `commits_30d / commits_90d`: full commit counts over the default-branch history within the fixed windows, including merge, bot and documentation commits.
- `last_commit_at`: the commit time of the default-branch HEAD.
- `pushed_at / updated_at`: kept for audit; not passed off as default-branch code updates.
- `latest_release`: the most recently created release; its absence alone is not treated as abandonment.
- `archived / disabled`: GitHub repository status.

## Tiering and formula

Projects are first split into four maintenance tiers: commits within the last 90 days; no commits for 91–365 days; no commits for over 365 days; archived, disabled or historical projects.

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
maintenance_score = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

On ties, stars are compared first, then repositories sort stably by name. All four views — balanced, stars, 90-day activity and latest commit — tier by maintenance status first. Use the CSV when un-tiered raw values are needed.

## What cannot be inferred

The maintenance score is not LongMemEval, LoCoMo, recall rate, answer accuracy, deletion completeness, security or production maturity. Monorepos and automatic commits inflate activity, stable small libraries may be underrated, and research repositories do not need continuous high-frequency commits.

Automated license detection and manual review are kept separate. `NOASSERTION` is never written as MIT by default; PolyForm, BSL, non-commercial, dual and split licenses keep their original boundaries. Model weights, datasets, third-party dependencies and hosted services may carry additional licenses.

## Capability-testing recommendation

On the same model, token budget and dataset, measure separately: write completeness, temporal/entity/multi-hop recall, evidence hits, answer accuracy, whether user corrections take effect, one-off exception poisoning, cross-project isolation, post-deletion residue, process recovery, P50/P95 latency and total cost. Do not assemble a leaderboard from vendors' individually best numbers.
