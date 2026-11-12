"""Generate the Agent-memory catalogue and transparent GitHub rankings."""
from __future__ import annotations
import argparse,csv,io,json,re
from datetime import datetime
from pathlib import Path
from ranking import dt,age_days,score,tier,status,rank,table

ROOT=Path(__file__).resolve().parents[1]
CATEGORIES={
 'engines':'记忆引擎与服务',
 'file_memory':'文件真源与可审阅记忆',
 'graph_temporal':'图谱、实体与时序记忆',
 'coding_memory':'编码 Agent 与 MCP 记忆',
 'procedural':'经验、技能与程序性记忆',
 'research_eval':'研究实现与评测',
 'adjacent':'相邻平台、规范与索引',
 'historical_restricted':'历史、归档与受限许可',
}
SCOPES={'core':'核心候选','adjacent':'相邻基础设施','research':'研究/评测','historical':'历史参考','restricted':'受限许可'}
LICENSE_STATUS={'verified':'开放许可证已核验','custom':'复合/拆分许可','source_available':'源码可见但非 OSI 开源','unverified':'许可待核验'}

def validate(projects,snapshot):
    assert snapshot['schema_version']==1;dt(snapshot['as_of'])
    repos=[p['repo'] for p in projects]
    assert len(repos)==len(set(x.lower() for x in repos)),'Duplicate canonical repo'
    assert set(repos)==set(snapshot['repositories']),'Snapshot/catalogue mismatch'
    for p in projects:
        assert re.fullmatch(r'[\w.-]+/[\w.-]+',p['repo']),p['repo']
        assert p['category'] in CATEGORIES and p['scope'] in SCOPES
        assert p['description'] and p['boundary'] and p['evidence']
        datetime.strptime(p['reviewed_at'],'%Y-%m-%d')
        assert re.fullmatch(r'[a-f0-9]{40}',p['evidence_commit'])
        assert p['license_review']['status'] in LICENSE_STATUS
        assert all(e['url'].startswith('https://') for e in p['evidence'])
        m=snapshot['repositories'][p['repo']]
        assert m['canonical_repo'].lower()==p['repo'].lower(),'Resolve redirects explicitly'
        assert all(type(m[k]) is int and m[k]>=0 for k in ['stars','forks','commits_30d','commits_90d'])
        assert m['commits_30d']<=m['commits_90d'];dt(m['last_commit_at'])
        assert re.fullmatch(r'[a-f0-9]{40}',m['head_sha'])
    assert sum(bool(p['baseline']) for p in projects)>=50

def render(projects,snapshot):
    metrics=snapshot['repositories'];as_of=snapshot['as_of'];reviewed=max(p['reviewed_at'] for p in projects)
    ordered=rank(projects,metrics,as_of)
    intro=(ROOT/'docs/readme-intro.md').read_text(encoding='utf-8').strip()
    readme=[intro,f'## 当前收录\n\n**{len(projects)} 个项目，其中 {sum(bool(p["baseline"]) for p in projects)} 个来自三份原始调研，{len(projects)-sum(bool(p["baseline"]) for p in projects)} 个为本轮新增。** 功能核验：{reviewed}；指标快照：`{as_of}`（UTC）。\n\n每个分类先按维护状态分层，再综合 star（40%）、90 天默认分支提交（35%）和最近提交（25%）排序。归档项目后置。维护分只描述 GitHub 热度与活动迹象，不代表记忆准确率、成本、安全性或生产成熟度。',
    '## 活跃核心项目速览\n\n只展示核心候选、许可证已核验且近 90 天有提交的项目；研究实现、检索组件、受限许可和历史项目不进入此表。']
    shortlist=[p for p in ordered if p['scope']=='core' and p['license_review']['status']=='verified' and tier(p,metrics[p['repo']],as_of)==0]
    readme.append(table(['项目','定位','Stars','90天提交','最近提交 UTC','维护分'],[[f"[{p['name']}](https://github.com/{p['repo']})",p['description'],f"{metrics[p['repo']]['stars']:,}",f"{metrics[p['repo']]['commits_90d']:,}",metrics[p['repo']]['last_commit_at'][:10],f"{score(metrics[p['repo']],as_of):.1f}"] for p in shortlist[:12]]))
    readme.append('## 分类目录\n\n`★报告基线` 表示项目来自用户提供的三份调研。每项只有一个主分类，避免同一仓库重复参与排序。')
    overview=[]
    for key,label in CATEGORIES.items():
        group=[p for p in ordered if p['category']==key]
        overview.append([label,len(group),'、'.join(p['name'] for p in group[:3])])
    readme.append(table(['分类','数量','维护排序靠前的项目'],overview))
    detail=['# 项目说明与证据\n\n功能判断来自固定提交的官方 README，未安装运行全部项目。每日指标刷新不会自动重新审核功能和许可证。\n']
    for key,label in CATEGORIES.items():
        group=[p for p in ordered if p['category']==key];readme.append('### '+label)
        rows=[]
        for p in group:
            m=metrics[p['repo']];lic=p['license_review'];tags=[]
            if p['baseline']:tags.append('★报告基线')
            if tier(p,m,as_of)==3:tags.append('归档/历史')
            if lic['status']!='verified':tags.append('许可注意')
            suffix=(' · '+' · '.join(tags)) if tags else ''
            rows.append([f"[{p['name']}](https://github.com/{p['repo']}){suffix}",p['description'],f"{m['stars']:,}",f"{m['commits_90d']:,}",m['last_commit_at'][:10],f"{score(m,as_of):.1f}",lic['label']])
            evidence=' · '.join(f"[来源{i+1}]({e['url']})" for i,e in enumerate(p['evidence']))
            detail.extend([f"## [{p['name']}](https://github.com/{p['repo']})",p['description'],f"- 分类：{label}；{SCOPES[p['scope']]}。\n- 适用边界：{p['boundary']}\n- 维护状态：{status(p,m,as_of)}；30 天提交 {m['commits_30d']} 次，90 天提交 {m['commits_90d']} 次。\n- 许可：[{lic['label']}]({lic['source']})；{LICENSE_STATUS[lic['status']]}。{lic['note']}\n- 功能核验：{p['reviewed_at']}；{evidence}。"])
        readme.append(table(['项目','定位','Stars','90天提交','最近提交 UTC','维护分','许可'],rows))
    readme.extend(['## 选择入口\n\n- 需要完整外置记忆 API：先看记忆引擎与服务。\n- 需要可直接审阅、修改、Git 管理：看文件真源记忆。\n- 需要实体关系、时间有效性和多跳：看图谱与时序记忆。\n- 需要 Claude Code、Codex、OpenCode 等跨宿主记忆：看编码 Agent/MCP。\n- 需要把成功与失败沉淀成可执行方法：看经验、技能与程序性记忆。\n- 需要验证效果、污染、删除与遗忘：看研究实现与评测。\n\n完整边界和证据见 [项目详表](docs/projects.md)，分类口径见 [范围与分类](docs/taxonomy.md)。',
    '## 数据与维护\n\n- [综合、Star、活跃度、最近提交排序](docs/rankings.md)\n- [排序方法与限制](docs/methodology.md)\n- [检索关键词、来源与覆盖](docs/research.md)\n- [项目 JSON](data/projects.json) · [指标 JSON](data/metrics.json) · [排序 CSV](data/rankings.csv)\n- [贡献指南](CONTRIBUTING.md)\n\n```sh\npython scripts/refresh_metrics.py\npython scripts/build.py\npython -m unittest discover -s tests -v\npython scripts/build.py --check\n```\n\nGitHub Actions 每日刷新 GitHub 指标。新增项目、功能、分类和许可判断必须人工核验。',
    '## 许可与致谢\n\n本目录的原创整理和脚本采用 [MIT](LICENSE)，所链接项目遵循各自许可。未知、复合、非商业或 BSL/PolyForm 项目均保留原始边界。\n\n初始分类与项目地图来自用户提供的三份本地调研；本轮另参考 [mnemoverse/awesome-agent-memory](https://github.com/mnemoverse/awesome-agent-memory) 进行覆盖校验，并回到各项目官方仓库核验。'])
    rankings=[f'# 排序视图\n\n快照：`{as_of}`。这是 GitHub 维护元数据排序，不是记忆系统能力排行榜。所有视图先按维护状态分层；原始值见 [CSV](../data/rankings.csv)。']
    for mode,label in [('balanced','综合维护分'),('stars','Star 优先'),('activity','90 天提交优先'),('recent','最近默认分支提交优先')]:
        rows=[]
        for p in rank(projects,metrics,as_of,mode):
            m=metrics[p['repo']];rows.append([f"[{p['name']}](https://github.com/{p['repo']})",CATEGORIES[p['category']],status(p,m,as_of),m['stars'],m['commits_90d'],m['last_commit_at'][:10],score(m,as_of)])
        rankings.extend(['## '+label,table(['项目','分类','维护层','Stars','90天提交','最近提交 UTC','维护分'],rows)])
    buf=io.StringIO(newline='');w=csv.writer(buf,lineterminator='\n')
    w.writerow(['repo','name','category','scope','baseline','license','license_status','stars','commits_30d','commits_90d','last_commit_at','maintenance_status','score','as_of'])
    for p in ordered:
        m=metrics[p['repo']];w.writerow([p['repo'],p['name'],p['category'],p['scope'],p['baseline'],p['license_review']['label'],p['license_review']['status'],m['stars'],m['commits_30d'],m['commits_90d'],m['last_commit_at'],status(p,m,as_of),score(m,as_of),as_of])
    return {'README.md':'\n\n'.join(readme)+'\n','docs/projects.md':'\n\n'.join(detail)+'\n','docs/rankings.md':'\n\n'.join(rankings)+'\n','data/rankings.csv':buf.getvalue()}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true');args=ap.parse_args()
    read=lambda p:json.loads((ROOT/p).read_text(encoding='utf-8'))
    projects,snapshot=read('data/projects.json'),read('data/metrics.json');validate(projects,snapshot);outputs=render(projects,snapshot)
    for name,content in outputs.items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=content:raise SystemExit(f'Stale generated file: {name}')
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
    print(f'{"Checked" if args.check else "Generated"} {len(outputs)} files; {len(projects)} projects')
if __name__=='__main__':main()
