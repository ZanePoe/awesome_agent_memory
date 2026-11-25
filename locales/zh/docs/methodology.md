# 排序方法与限制

## GitHub 指标

`scripts/refresh_metrics.py` 使用 GitHub GraphQL API，一次固定 UTC 时刻读取所有 canonical 仓库。全部批次成功后才原子替换 `data/metrics.json`；部分失败会保留旧快照并让任务失败。

- `stars`：采集时的关注度代理指标。
- `commits_30d / commits_90d`：默认分支历史在固定窗口内的完整提交计数，包含合并、机器人与文档提交。
- `last_commit_at`：默认分支 HEAD 提交时间。
- `pushed_at / updated_at`：保留作审计，不冒充默认分支代码更新时间。
- `latest_release`：最近创建的 release；缺失不自动视为弃坑。
- `archived / disabled`：GitHub 仓库状态。

## 分层与公式

先按维护状态分四层：近 90 天有提交；91–365 天未提交；超过 365 天未提交；归档、disabled 或历史项目。

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
维护分 = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

同分比较 star，再按仓库名稳定排序。综合分、star、90 天活动和最新提交四种视图都先按维护状态分层。需要不分层的原始值时使用 CSV。

## 不能据此推断什么

维护分不是 LongMemEval、LoCoMo、召回率、答案准确率、删除完整性、安全性或生产成熟度。monorepo 和自动提交会放大活动量，稳定的小型库可能被低估，研究仓库也不需要持续高频提交。

许可证自动识别与人工审核分开。`NOASSERTION` 不会默认写成 MIT；PolyForm、BSL、非商业、双许可和拆分许可均保留原始边界。模型权重、数据集、第三方依赖和托管服务可能另有许可。

## 能力测评建议

在同一模型、token 预算和数据集上分别测量：写入完整性、时间/实体/多跳召回、证据命中、回答准确率、用户更正生效、一次性例外污染、跨项目隔离、删除后残留、进程恢复、P50/P95 延迟与总费用。不要用供应商各自的最佳数字拼成排行榜。
