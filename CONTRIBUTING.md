# 贡献指南

欢迎新增项目、修正分类、重命名、许可证或功能边界。低 star 不是拒绝理由。

1. 修改 `data/projects.json`，不要直接改生成的 README 表格。
2. 提供 canonical GitHub 仓库、一个主分类、功能定位、明确边界及固定提交的 README 来源。
3. 同名项目必须写完整 owner/repo；fork 只有在实现或维护路线有明确差异时单列。
4. 区分引擎、文件真源、图谱、宿主插件、研究代码和普通数据库。
5. 区分已实现、路线图、作者 benchmark 和本目录实测。当前目录未对全部项目做统一运行测评。
6. 核验根目录及子目录许可证。公开源码、免费使用和 OSI 开源不是同一概念。
7. 新增仓库后刷新完整指标并重新生成：

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

不要提交 API key、内部内容工厂地址、真实私密会话或未脱敏记忆数据。调研和变更记录放在 `record/YYYY-MM-DD-中文主题.md`。
