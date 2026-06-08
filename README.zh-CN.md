# 缠论研究展示版

这是一个更大交易研究系统的公开展示版仓库。

它的公开范围被有意限制在以下内容：

- 数据组织与研究流程
- 基于案例的验证方式
- 精选案例的 5m K 线绘图
- 基于公开案例的报告生成
- 通用研究基础设施与私有 alpha 逻辑之间的工程边界

本仓库不会公开私有 alpha 核心。以下内容不在开源范围内：

- 买点识别逻辑
- 信号过滤条件
- 参数组合与执行阈值
- 实盘执行与风控细节

## 仓库目的

这个仓库的目标，是在保护交易优势的前提下，对外展示可复用的研究基础设施，并向开源社区贡献一部分工程化能力。

这个公开版采用 verifier 思路：

- 公开内容负责展示案例如何组织、可视化和评估
- 私有内容负责生成原始信号与执行决策

## 仓库结构

```text
docs/                   架构、方法论与公开范围说明
examples/               公开案例格式与案例元数据模板
public_core/            通用绘图与案例读取辅助模块
reports/                手工整理或程序生成的汇总报告
verifier/               只针对公开案例做绘图和评估的脚本
```

## 快速开始

1. 将筛选后的公开案例导出到 `examples/cases/`
2. 填写 `examples/metadata.csv`
3. 修改脚本内配置变量后直接运行 verifier 脚本

```powershell
python verifier/plot_public_cases.py
python verifier/evaluate_public_cases.py
```

脚本遵循原项目约定：

- 不使用 `argparse`
- 采用文件内配置变量
- 支持直接在 IDE 中运行

## 公开案例约定

每个公开案例包含：

- 一份 OHLCV csv 文件
- `examples/metadata.csv` 中的一行元数据
- 可选的案例备注信息

verifier 只接收预先导出的公开 bars，并产出：

- 5m 案例图
- 单案例评估明细
- 聚合汇总 csv

## 实盘验证

这个仓库本身不是实盘程序。

如果需要做尽调、面试验证或进一步交流，可以通过以下方式联系：

- `1625059268@qq.com`

实盘策略服务在私有环境中持续运行。验证可以通过精选案例导出、运行截图和脱敏日志完成，但不会公开 alpha 核心。

## 文档

- [公开与私有边界](docs/open-private-boundary.md)
- [架构说明](docs/architecture.md)
- [方法论](docs/methodology.md)
- [实盘说明](docs/live-trading-note.md)

## 许可证

MIT，见 [LICENSE](LICENSE)。
