# Claude Fable 5.2 使用案例

**[浏览 139 个 Fable 5.2 案例](docs/fable-5-2/README_zh-CN.md)**

汇集 11 月 10 日收集的工作流、演示、对比、评测、集成和使用限制，并附原始来源。

## Fable 历史案例

<div align="center">

<a href="https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5"><img src="images/fable-5-5-use-cases.png" alt="Awesome Fable 5.5 Use Cases" width="760" height="304"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Try it on Evolink](https://img.shields.io/badge/Try_it_on-Evolink-black)](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)
[![Website](https://img.shields.io/badge/Website-Live-orange)](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)
[![Docs](https://img.shields.io/badge/Docs-Read-blue)](https://docs.evolink.ai)

[![English](https://img.shields.io/badge/English-111111)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

<a id="-introduction"></a>
## 🍌 简介

欢迎来到 Claude Fable 5 高信号用例仓库。

**我们收集 Claude Fable 5 的真实使用案例、教程、集成和评测，内容精选自公开演示和创作者社区。**

这个简体中文 README 聚焦高信号案例：包含具体工作流、提示词、演示、集成、基准证据或实际限制。

大多数案例整理自 X/Twitter 帖子和公开演示。每个案例标题都链接回原始来源，每个作者用户名都链接到创作者主页。

在 Evolink 上试用：[Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

<a id="-overview"></a>
## 📊 概览

- **88 个原有 Fable 5 案例，加上 241 个社区案例，共 329 个案例。**
- 覆盖编码代理、长时间自动化、游戏、视觉设计、3D 模拟、知识工作、教程、API 集成、基准、定价和发布限制。
- 每个案例都包含原始来源、创作者署名、简明要点、证据类型和发布日期。
- 使用本仓库查找实用工作流、比较优势与限制、发现可复现提示词，并跟踪集成示例。

> [!NOTE]
> 本集合优先选择具体证据，而不是热度叙事：可复现提示词、已发布演示、基准方法、集成说明、成本数据和明确说明的注意事项。

<a id="-quick-api-access"></a>
## ⚡ 快速 API 接入

通过兼容 Evolink 的 Messages API 使用 Claude Fable 5。先在 [Evolink](https://evolink.ai/login?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5) 获取 API token，然后将 `<token>` 替换为你的 token。

```bash
curl --request POST \
  --url https://direct.evolink.ai/v1/messages \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "model": "claude-fable-5",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": "Hello, world"
    }
  ]
}
'
```

<a id="-menu"></a>
## 📑 目录

| 章节 | 案例 |
|---|---|
| [💻 编码与代码生成](#coding-and-code-generation) | Case 1-6 |
| [🤖 代理与长时间自动化](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 游戏与交互演示](#games-and-interactive-demos) | Case 9-12 |
| [🎨 视觉、设计、视频与 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 文档、知识工作与研究](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 教程、课程与提示词资源](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 平台、API 与工具集成](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 评测、对比与限制](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | 致谢与更正说明 |

### [💻 编码与代码生成](#coding-and-code-generation)

| Case | 展示内容 | 类型 |
|---|---|---|
| [Cursor 多阶段工作流](#case-1) | 把 Fable 5 用作多模型 Cursor 工作流中的计划审查和批判步骤，然后把实现和修订交还给更便宜或更专用的模型。 | 评测 |
| [从截图重建 GitHub](#case-2) | 把产品截图粘贴到代理式编码工具中，并要求 Fable 5 复刻带真实功能的界面。 | 演示 |
| [单提示词黑洞模拟](#case-3) | 给 Fable 5 一条详细的创意编程提示词，让它生成一个自包含的 Three.js 物理可视化。 | 教程 |
| [一次生成 macOS 风格 Web OS](#case-4) | 让 Fable 5 生成一个完整的单文件 Web OS，并让它一次性构建 UI 外壳、应用、交互、音频和内嵌游戏行为。 | 教程 |
| [用 1,687 条提示词构建 Spawn 5.0](#case-5) | 把 Fable 5 当作长会话工程伙伴，在大量提示词中协作，人类角色从架构转向判断输出质量。 | 教程 |
| [带发现项的大型 Pull Request 审查](#case-6) | 让 Fable 5 面向一个大型 Pull Request，要求它审查正确性、误报、真实 bug 和打磨问题。 | 演示 |

### [🤖 代理与长时间自动化](#agents-and-long-running-automation)

| Case | 展示内容 | 类型 |
|---|---|---|
| [长周期接力工作流评测](#case-7) | 把 Fable 5 用于雄心更大的长周期工作：网站重建、程序化内容流水线、语气匹配、安全审查和最终质量检查。 | 评测 |
| [诊断基础设施故障并打开修复 PR](#case-8) | 给 Fable 5 提供日志、数据库错误和镜像摘要等基础设施线索，然后让它诊断故障并准备修复。 | 评测 |

### [🎮 游戏与交互演示](#games-and-interactive-demos)

| Case | 展示内容 | 类型 |
|---|---|---|
| [手指追踪 Dino Runner](#case-9) | 让 Fable 5 构建一个以手指追踪作为输入机制的浏览器游戏。 | 演示 |
| [两句话生成赛车游戏](#case-10) | 给 Fable 5 一个很短的游戏提示词，让它一次生成地图、模式、音乐、UI 和游戏资产。 | 教程 |
| [Rust 可安装终端版 Minecraft](#case-11) | 通过终端编码 harness 运行 Fable 5，并要求它构建一个可安装的 Rust 终端游戏。 | 演示 |
| [带时间和成本记录的 Minecraft 克隆](#case-12) | 用一条提示词要求 Fable 5 生成可玩的 Minecraft 风格克隆，然后评估时间、成本、代码量和功能覆盖。 | 教程 |

### [🎨 视觉、设计、视频与 3D](#visual-design-video-and-3d)

| Case | 展示内容 | 类型 |
|---|---|---|
| [完整可复现电商邮件提示词](#case-13) | 给 Fable 5 一份完整的品牌邮件 mockup 创意简报，包括精确分区、产品要求、视觉方向和约束。 | 教程 |
| [瑞士杠杆擒纵制表基准](#case-14) | 在机械模拟基准上使用 Fable 5，要求它实现、验证并迭代物理正确性。 | 评测 |
| [Three.js《Friends》公寓场景](#case-15) | 提示 Fable 5 将平面图和场景参考转换为可导航的 Three.js 环境。 | 评测 |
| [带提示词和 URL 的太阳系模拟](#case-16) | 使用 Fable 5 从物理原理构建天文模拟，持续迭代直到模拟和公开输出都准备好。 | 教程 |

### [📚 文档、知识工作与研究](#documents-knowledge-work-and-research)

| Case | 展示内容 | 类型 |
|---|---|---|
| [Stripe 与科研工作流证据](#case-17) | 把这个案例作为企业迁移和科研工作流主张的证据，而不是可复制粘贴的提示词。 | 评测 |
| [政策备忘录与修订模式工作流](#case-18) | 将 Fable 5 用于长篇定性文档工作：修订模式、评论分流和基于逐字稿的编辑。 | 教程 |
| [深度研究提示词与输出](#case-19) | 向 Fable 5 提出研究式问题，并评估它是否能产出结构化、有历史依据的长答案。 | 演示 |

### [🧭 教程、课程与提示词资源](#tutorials-courses-and-prompt-resources)

| Case | 展示内容 | 类型 |
|---|---|---|
| [Fable 5 如何改变 Claude Code 工作流](#case-20) | 使用 Fable 5 时，应设置方向、上下文、目标和验证标准，而不是微管理每个步骤。 | 演示 |
| [十亿 Token 评测与路由策略](#case-21) | 将 Fable 5 用于 frontier 级规划和审查，然后把高容量实现路由给更便宜的模型。 | 教程 |
| [防御性设备加固提示词](#case-22) | 运行一步步的防御性加固提示词，让 Fable 5 盘点设备、给出精确检查并等待验证。 | 教程 |
| [全站设计审计 Goal 提示词](#case-23) | 使用 `/goal` 让 Fable 5 启动网站、截图页面、审计 UX、撰写报告并修复安全的小问题。 | 教程 |
| [长篇创作工作流分工](#case-24) | 使用 Fable 5 设计稳定格式和示例，再把该结构交给另一个生成系统做领域特定输出。 | 教程 |
| [Fable 5 初学者使用指南](#case-25) | 使用 Fable 5 时采用目标导向提示、验证循环和 effort 设置，而不是细碎的逐步指令。 | 评测 |
| [可复制粘贴的仓库审计提示词](#case-26) | 把仓库审计提示词粘贴进 Fable 5，要求基于文件的探索、发现项、策略和里程碑任务计划。 | 教程 |
| [限时窗口使用策略](#case-27) | 在访问窗口有利时，把 Fable 5 用量花在审计、架构和规划上，然后使用更便宜的模型执行。 | 教程 |
| [在 Claude Code 中使用 Goals 和 Workflows](#case-28) | 在实现前把 Fable 5 当作思考伙伴，然后结合 `/goal` 和 workflows 执行并验证计划。 | 教程 |

### [🔌 平台、API 与工具集成](#platform-api-and-tool-integration)

| Case | 展示内容 | 类型 |
|---|---|---|
| [Hermes Agent 集成配置](#case-29) | 配置 Hermes 使用 `anthropic/claude-fable-5` 运行复杂 `/goal` 和缓存的长周期任务。 | 教程 |
| [能力、定价与订阅说明](#case-30) | 使用本案例理解 Fable 5 何时可用、成本多少，以及哪些受保护领域可能回退到另一个模型。 | 教程 |
| [发布、访问、定价与安全摘要](#case-31) | 使用这份发布摘要选择访问路径、API 模型名、上下文窗口、缓存策略和订阅时机。 | 教程 |
| [基于 Advisor 的降本策略](#case-32) | 当边际智能值得付费时，在便宜模型工作流中把 Fable 5 用作 advisor 或 reviewer。 | 集成 |
| [定价、访问与安全护栏](#case-33) | 在规划工作负载前，使用本案例理解 Fable 5 访问、API 定价和安全回退行为。 | 集成 |
| [一行代码集成 Swarms](#case-34) | 将 Swarms 模型名设置为 `anthropic/claude-fable-5`，并通过 Swarms 框架或 API 运行 Fable 5。 | 集成 |

### [📏 评测、对比与限制](#evaluations-comparisons-and-limits)

| Case | 展示内容 | 类型 |
|---|---|---|
| [Fable 5 vs GPT-5.5 成本与质量对比](#case-35) | 在同一个编码任务上比较 Fable 5 和 GPT-5.5，判断输出质量、运行时间和工具成本。 | 评测 |
| [AA-Omniscience 基准结果](#case-36) | 使用这个基准案例评估 Fable 5 的知识准确性和幻觉行为。 | 评测 |
| [Artificial Analysis 智能指数结果](#case-37) | 使用本案例对照其他 frontier 模型，衡量 Fable 5 的整体智能排名。 | 评测 |
| [GDPval-AA 代理式知识工作基准](#case-38) | 使用本案例评估 Fable 5 在代理式真实世界知识工作上的表现。 | 评测 |
| [一周初印象与定价机制](#case-39) | 使用这个初印象案例判断 Fable 5 最强之处，尤其是游戏设计和系统规划。 | 集成 |
| [成本与速度对比](#case-40) | 使用本对比判断质量提升是否值得更高成本和更慢的长周期运行。 | 评测 |
| [Claude Code 上手笔记](#case-41) | 使用本案例评估 Claude Code 中的 Fable 5，包括工具使用、性格和剩余粗糙点。 | 演示 |
| [创意写作基准结果](#case-42) | 使用这个基准案例判断 Fable 5 的短篇小说写作质量和拒答行为。 | 评测 |
| [多基准发布摘要](#case-43) | 使用这份发布基准摘要理解与编码代理和复杂任务最相关的头部分数。 | 评测 |
| [与 GPT-5.5 的基准和定价对比](#case-44) | 使用本对比从价格和基准类别上评估 Fable 5 与 GPT-5.5。 | 评测 |
| [带实际限制的一线笔记](#case-45) | 使用这份现场报告理解 Fable 5 哪里有实质提升，以及哪里仍有实际限制。 | 教程 |
| [物理模拟对比](#case-46) | 用相同物理模拟提示词分别测试 Fable 5 和 Opus 4.8，对比输出质量、成本和速度。 | 演示 |
| [调试体验与设计判断力](#case-47) | 用 Fable 5 调试时，要求它测量、加日志、验证和修补，而不是简单猜测。 | 演示 |
| [多维度优缺点](#case-48) | 在把 Fable 5 作为日常主力前，使用本案例理解实际优缺点。 | 演示 |
| [法律 S-1 起草测试](#case-49) | 将 S-1 起草提示词作为法律代理能力测试，并比较结构、格式和长度。 | 教程 |
| [医疗健康基准细节](#case-50) | 使用这条基准笔记评估 Fable 5 在医疗健康相关任务上的表现，并识别缺失的高难医学评测。 | 评测 |
| [ParseBench 文档解析评测](#case-51) | 使用本案例判断相较专用 OCR 系统，Fable 5 用于文档解析是否具备成本效率。 | 评测 |
| [SWE-Bench Pro 与 FrontierCode 对比](#case-52) | 使用这个基准案例评估 Fable 5 在迁移、复杂实现、自主会话、测试和视觉验证方面的能力。 | 评测 |
| [长问题求解的定性评测](#case-53) | 使用这条定性评测理解为什么 Fable 5 适合更长、更难的任务，同时仍需生产审查。 | 评测 |
| [ParseBench 忠实度与格式结果](#case-54) | 使用这个 ParseBench 结果判断文档忠实度和格式表现。 | 评测 |
| [基准、定价、访问与安全措施](#case-55) | 把本案例作为基准、定价、访问、安全措施和战略影响的广泛 checklist。 | 评测 |
| [官方基准分数列表](#case-56) | 使用这个基准列表理解 Fable 5 在编码、计算机使用和安全任务上的官方分数。 | 评测 |
| [APEX-SWE 基准方法论](#case-57) | 使用本案例评估 Fable 5 在 APEX-SWE 上的表现，尤其是 observability 和 integration 工作。 | 评测 |
| [ProofBench 形式化数学结果](#case-58) | 使用本案例评估 Fable 5 在形式化数学上相对专用定理证明系统的表现。 | 教程 |
| [VirtueBench 初步分析](#case-59) | 使用本案例检查 Fable 5 在不同美德类别中的道德推理行为。 | 评测 |
| [API 空响应安全过拟合测试](#case-60) | 使用本案例理解发布期安全过拟合风险，以及 API 测试中的空响应行为。 | 评测 |
| [Fable 提示词验证指南](#case-61) | 用这份提示词指南，把重点从拉长提示词技巧转向目标、上下文、约束、工具和验证循环。 | 教程 |
| [伊斯坦布尔平台游戏参考构建](#case-62) | 用一张参考 sprite sheet 加上一条转换指令，测试 Fable 5 是否能生成可玩的平台游戏。 | 演示 |
| [商业 3D 城市仪表板](#case-63) | 用 Fable 5 把业务工作流转成一个实时 3D 城市仪表板概念。 | 演示 |
| [Three.js Hole 游戏一次生成](#case-64) | 用 Fable 5 一次生成一个基于 Three.js 的 3D 浏览器游戏原型。 | 演示 |
| [DeepSWE 评分对比](#case-65) | 用这条 DeepSWE 记录，对比 Fable 5 xHigh 和 GPT-5.5 xHigh 在软件工程基准上的表现。 | 评测 |
| [仓库成本对比](#case-66) | 用这个仓库分析对比，判断 token 价格和人工返工成本之间的关系。 | 评测 |
| [Super Mario 游戏 Token 成本](#case-67) | 用这个单次生成的游戏案例估算 Fable 5 的输出质量和 token 消耗。 | 演示 |
| [Claude Code Fallback 设置](#case-68) | 用这个案例了解 Claude Code 在 Fable 5 消息被标记时如何切换模型。 | 集成 |
| [Namma Metro 模拟器构建](#case-69) | 用这个 demo 作为 Fable 5 为公共交通模拟器进行 vibe coding 的紧凑示例。 | 演示 |
| [Dusk Drive 单提示词游戏](#case-70) | 用这个单提示词驾驶游戏案例，评估 Fable 5 在无需人工编辑时进行 low-poly 游戏原型开发的能力。 | 演示 |
| [APEX-Agents Pass@1 排名](#case-71) | 用这个 APEX-Agents 结果，对比 Fable 5 Max 在多步骤自主任务上的表现。 | 评测 |
| [Claude 模型选择手册](#case-72) | 用这份模型选型手册，把 Fable 5 留给 Claude Code 中最难的任务。 | 教程 |
| [HermesWorld 自动代理循环](#case-73) | 用这个案例研究一个免手动干预的 Fable 5 循环，它会持续构建、测试、游玩和做 smoke test。 | 集成 |
| [麦肯锡风格报告提示词测试](#case-74) | 用这条文档生成提示词，评估咨询报告的结构、图表、叙事和风险分析。 | 教程 |
| [可见防护措施上线](#case-75) | 用这条官方说明了解 Fable 5 防护机制的可见性、API 拒答原因和回退到 Opus 的行为。 | 集成 |
| [Claude Code 模型匹配修复](#case-76) | 用这条 Claude Code 更新说明，避免 Fable 5 的模型名和上下文匹配问题。 | 集成 |
| [Claude Code 中的三个 Web App](#case-77) | 用这个新手编码 demo，观察 Fable 5 在 Claude Code 中生成多个 Web App 的表现。 | 演示 |
| [Rilable 开源 App 构建器](#case-78) | 用这个开源 App 构建器案例研究 Fable 5 在 iOS、Web App、沙盒和 API token 成本上的应用。 | 集成 |
| [DeepSWE 编码代理指数首秀](#case-79) | 用更新后的 Artificial Analysis 指数，对比 Fable 5 在更难的代理式编码任务上的表现，这些任务避免复用公开 GitHub 修复。 | 评测 |
| [DataEmpire 网站分析游戏](#case-80) | 让 Claude Fable 5 把访客和里程碑映射成游戏实体，把原始网站分析数据变成可重玩的游戏。 | 集成 |
| [FrontierSWE 20 小时任务信号](#case-81) | 用 FrontierSWE 证明 Fable 5 不只适合短期修 bug，也能在超长工程任务中持续保持产出。 | 评测 |
| [KernelBench-Hard CUDA 记录](#case-82) | 当你需要低层优化而不只是现有库封装时，用 Fable 5 处理高级 CUDA kernel 生成。 | 评测 |
| [Figma Capture 落地页克隆](#case-83) | 把竞品页面抓进 Figma 图层后，让 Claude Code 配合 Fable 5 重建结构、文案和品牌系统，而不是靠截图猜测。 | 集成 |
| [两小时做出 GTA 2 克隆](#case-84) | 把 Fable 5 的代码生成和独立素材工具结合起来，快速做出可玩的 3D 游戏，而不必手写整个技术栈。 | 教程 |
| [CloudWatch 日志分诊代理](#case-85) | 让 Fable 5 驱动的代理消化超大规模服务日志上下文，先推断架构，再收敛到具体故障。 | 集成 |
| [沙盒中的世界杯预测器](#case-86) | 把多个 frontier 模型放进隔离沙盒，让它们为公开预测应用研究实时新闻、伤病和黄牌背景。 | 集成 |
| [WolfBench 拒答成本案例](#case-87) | 在为 Fable 5 的长自主运行定价时，把拒答行为视为真实的基准变量。 | 评测 |
| [API 访问截止追踪器](#case-88) | 如果你的工作流依赖持续访问某个可能被限流或撤下的 frontier 模型，就用脚本监控可用性。 | 集成 |



### [🆕 Fable 5.5 社区演示](#fable-5-5-community-demos)

| 案例 | 类型 |
|---|---|
| [用代码生成带声音的狐狸动画](#case-89) | Demo |
| [从开放式创意要求生成动画](#case-90) | Demo |
| [建筑公司的动态 3D 网站](#case-91) | Demo |
| [Three.js 汽车展示场景](#case-92) | Demo |
| [Minecraft 风格浏览器游戏演示](#case-93) | Demo |
| [Three.js 鹈鹕骑车动画](#case-94) | Demo |
| [附完整短提示词的鹈鹕骑车 SVG](#case-95) | Demo |
| [斑马奔跑动画样本](#case-96) | Demo |
| [由人手动执行交易的 TradingView 指标](#case-97) | Demo |
| [从一个点展开的动画故事](#case-98) | Demo |
| [在不同画风间切换的超人](#case-99) | Demo |
| [配有音乐的人类进步动画](#case-100) | Demo |
| [与 Opus 对比的发布视频](#case-101) | Evaluation |
| [把歌词与事件连接成画面](#case-102) | Demo |
| [漂浮场景中的体素角色](#case-103) | Demo |
| [3D 鲁布·戈德堡机械演示](#case-104) | Demo |
| [带声音与运动的 3D 手柄界面](#case-105) | Demo |
| [用 JavaScript 展示漫画角色](#case-106) | Demo |
| [包含世界、首领和榜单的 Updraft](#case-107) | Demo |
| [在旧金山地图中驾驶](#case-108) | Demo |
| [为 Seedance 动作场景写提示词](#case-109) | Demo |
| [桌面协作助手的介绍视频](#case-110) | Demo |
| [简短要求生成变换画风的动画](#case-111) | Demo |
| [三体问题可视化](#case-112) | Demo |
| [多种画风的动画画廊](#case-113) | Demo |
| [机器人伙伴与程序化毛发](#case-114) | Demo |
| [数学主题动态剪辑](#case-115) | Demo |
| [Your Woman 歌词视频](#case-116) | Demo |
| [用 JavaScript 重绘音乐视频](#case-117) | Demo |
| [中国足球主题动画](#case-118) | Demo |
| [掌机模型的重拓扑展示](#case-119) | Demo |
| [Minecraft 与 Pokémon 的结合](#case-120) | Demo |
| [解释大语言模型如何制作](#case-121) | Demo |
| [Altman 主题精彩剪辑](#case-122) | Demo |
| [《三十六计》第一计动画](#case-123) | Demo |
| [游戏建模、绑定与动画](#case-124) | Demo |
| [关于儿童死亡的无对白影片](#case-125) | Demo |
| [从糖酵解到乙醇的 SVG 动画](#case-126) | Demo |
| [十六艘 Starship 同步发射](#case-127) | Demo |
| [鹈鹕骑车动画测试](#case-128) | Demo |
| [未来一百五十年的故事](#case-129) | Demo |
| [独立尝试 Humanity Walks](#case-130) | Demo |
| [代码制作的 The Grader 影片](#case-131) | Demo |
| [恐怖短片 Reawakening](#case-132) | Demo |
| [二十五秒的自我改进视频](#case-133) | Demo |
| [城堡场景与使用费用反馈](#case-134) | Evaluation |
| [四十秒品牌发布广告](#case-135) | Demo |
| [Rocketball 游戏重制](#case-136) | Demo |
| [体素宝塔场景对比](#case-137) | Evaluation |
| [想象中的 Switch 3 发布展示](#case-138) | Demo |
| [着陆页的前后对比](#case-139) | Evaluation |
| [想象中的 AI 内在视角](#case-140) | Demo |
| [Go 歌词动态设计](#case-141) | Demo |
| [第二支十五秒动态作品集](#case-142) | Demo |
| [引导式代理实施审查](#case-143) | Tutorial |
| [Claude 吉祥物舞蹈](#case-144) | Demo |
| [可交互的世界七大奇迹群岛](#case-145) | Demo |
| [Propellerheads 音乐视频](#case-146) | Demo |
| [Steamboat Willie 动画对比](#case-147) | Evaluation |
| [三星堆主题影片](#case-148) | Demo |
| [Bugatti Chiron 的前后对比](#case-149) | Evaluation |
| [GRAIN 概念短片](#case-150) | Demo |
| [Human in Transit 艺术画廊](#case-151) | Demo |
| [丝绸之路视觉短片](#case-152) | Demo |
| [四种转型路径的演示文稿](#case-153) | Demo |
| [比较历史对话的语气](#case-154) | Evaluation |
| [鸮鹦鹉可爱度测试](#case-155) | Evaluation |
| [蜘蛛侠穿越十个漫画时代](#case-156) | Demo |
| [光明会题材的虚构恐怖视频](#case-157) | Demo |
| [代码制作的核科学史影片](#case-158) | Demo |
| [全民高收入概念解说](#case-159) | Demo |
| [Altman 与 Amodei 争论的动画解说](#case-160) | Demo |
| [Claude 吉祥物音乐视频](#case-161) | Demo |
| [从夸克到宇宙的连续缩放](#case-162) | Demo |
| [想象 2076 年的世界](#case-163) | Demo |
| [曼哈顿下城建筑时间线](#case-164) | Demo |
| [甲骨文主题动画](#case-165) | Demo |
| [角色穿越艺术史的另一种尝试](#case-166) | Demo |
| [代码制作的塞基洛斯视听作品](#case-167) | Demo |
| [喷气飞机动画对比](#case-168) | Evaluation |
| [模型自我介绍影片](#case-169) | Demo |
| [末日风格卡牌游戏原型](#case-170) | Demo |
| [The Late Byte 职场动画](#case-171) | Demo |
| [Queens of the Stone Age 歌词动画](#case-172) | Demo |
| [分享的 Three.js 叙事场景](#case-173) | Demo |
| [穿越历史场景的月球步](#case-174) | Demo |
| [详细提示词生成的动态图形](#case-175) | Demo |
| [租赁业务网站界面](#case-176) | Demo |
| [AGI 主题创意影片](#case-177) | Demo |
| [带猫咪支线的艺术史动画](#case-178) | Demo |
| [战斗原型与体素场景](#case-179) | Demo |
| [互联网迷因时间线](#case-180) | Demo |
| [一行提示生成的粒子运动](#case-181) | Demo |
| [Kung-Fu Boy 动画](#case-182) | Demo |
| [霍尔木兹海峡辩论动画](#case-183) | Demo |
| [独角兽 SVG 风格实验](#case-184) | Demo |
| [万圣节主题动画](#case-185) | Demo |
| [Blender CLI 野蛮人角色与封面](#case-186) | Demo |
| [Claude 的一天](#case-187) | Demo |
| [3D 人类历史](#case-188) | Demo |
| [快节奏动态设计作品](#case-189) | Evaluation |
| [自由发挥的复杂 3D 创作](#case-190) | Demo |
| [火柴人格斗动画](#case-191) | Demo |
| [一次提示生成 UI 动效序列](#case-192) | Demo |
| [SCP-8517 虚构动画](#case-193) | Demo |
| [水彩秋日动画](#case-194) | Demo |
| [程序化玩偶舞台](#case-195) | Demo |
| [浏览器渲染的鹈鹕骑行](#case-196) | Demo |
| [宇宙凝视自身](#case-197) | Demo |
| [独立喷气飞机动画测试](#case-198) | Demo |
| [最初的自由动效作品](#case-199) | Demo |
| [用代码呈现文明史](#case-200) | Demo |
| [芯片到服务器的缩放对比](#case-201) | Evaluation |
| [月球旅行个人动画项目](#case-202) | Demo |
| [日式体素场景对比](#case-203) | Evaluation |
| [Steaming the Frontier 视听短片](#case-204) | Demo |
| [超人穿越多种美术风格](#case-205) | Demo |
| [Cupcake 风格首领战原型](#case-206) | Demo |
| [太阳位置变化的帆船场景](#case-207) | Demo |
| [Paracortex 与 Pi 更新说明视频](#case-208) | Demo |
| [Curio 2.0 网站宣传片](#case-209) | Demo |
| [想象中的 Hugging Face 3D 故事](#case-210) | Demo |
| [Claude for Chrome 操作 JS Paint](#case-211) | Demo |
| [静态鹈鹕骑车 SVG](#case-212) | Demo |
| [BlockBench MCP 与 Minecraft 技能](#case-213) | Demo |
| [单个 HTML 文件中的 Dig Dug](#case-214) | Demo |
| [机械章鱼 SVG](#case-215) | Demo |
| [Humanity Walks 穿越艺术风格](#case-216) | Demo |
| [开放式黑洞场景](#case-217) | Demo |
| [极光水母动画对比](#case-218) | Evaluation |
| [Nintendo Switch 拼合与开机 SVG](#case-219) | Demo |
| [The Loom 交互式 3D 场景](#case-220) | Demo |
| [同一提示词的动态图形设计短片](#case-221) | Evaluation |
| [更干净但纵深更弱的场景](#case-222) | Evaluation |
| [表现有好有坏的日式场景](#case-223) | Evaluation |
| [手柄 SVG 对比](#case-224) | Evaluation |
| [工业设备 3D 场景](#case-225) | Demo |
| [巨大带壳鳃虫重建](#case-226) | Demo |
| [两轮提示绘制 GameCube 手柄](#case-227) | Demo |
| [为 X 帖子编辑截图](#case-228) | Demo |
| [体素樱花的前后对比](#case-229) | Evaluation |
| [SHADERKIN 布料界面原型](#case-230) | Demo |
| [分享的金色钟表界面动画](#case-231) | Demo |
| [Before There Was Anything 叙事影片](#case-232) | Demo |
| [分享的蓝色粒子涡旋](#case-233) | Demo |
| [经过两轮修改的多面板界面](#case-234) | Demo |
| [叠放动物的渲染场景](#case-235) | Demo |
| [四次开放世界 RPG 尝试对比](#case-236) | Evaluation |
| [两段前端代码动画对比](#case-237) | Evaluation |
| [代码生成的苔藓机器人影片](#case-238) | Demo |
| [重新制作集装箱港口模拟](#case-239) | Demo |
| [重新制作机场机坪场景](#case-240) | Demo |
| [鹈鹕骑车穿越抽象 3D 世界](#case-241) | Demo |
| [历史帆船场景](#case-242) | Demo |
| [与 Carbon 比较骑行和步态](#case-243) | Evaluation |
| [软饮瓶产品展示](#case-244) | Demo |
| [与 Astra 对比的鹈鹕运动](#case-245) | Evaluation |
| [代码动画的动态设计简报](#case-246) | Tutorial |
| [照片参考生成的体素肖像](#case-247) | Demo |
| [与 Opus 对比的飞行鹈鹕场景](#case-248) | Evaluation |
| [Morning Ride 鹈鹕网页场景](#case-249) | Demo |
| [同提示下的不同画风场景](#case-250) | Evaluation |
| [鹈鹕、自行车与马的组合](#case-251) | Demo |
| [由参考帖子启发的等距场景](#case-252) | Demo |
| [鹈鹕自行车的机械特写](#case-253) | Demo |
| [骑在鹈鹕上的自行车](#case-254) | Demo |
| [与 Carbon 对比的鹈鹕 SVG 画风](#case-255) | Evaluation |
| [卡通蓝鸟骑车场景](#case-256) | Demo |
| [林间公路鹈鹕骑车截图](#case-257) | Demo |
| [与 Carbon 对比的火柴人格斗](#case-258) | Evaluation |
| [早期测试的鹈鹕 SVG 参考](#case-259) | Demo |
| [跨模型 SVG 测试中的鹈鹕参考](#case-260) | Evaluation |
| [与 Carbon 对比的自行车 SVG 细节](#case-261) | Evaluation |
| [3D 峡谷聚落](#case-262) | Demo |
| [与 Opus 对比的手柄细节](#case-263) | Evaluation |
| [每周网站 SEO 审计流程](#case-264) | Integration |
| [在 Opus 动效中复用 Fable 素材](#case-265) | Integration |
| [曼荼罗与几何形体应用](#case-266) | Demo |
| [Three.js 自行车骑手](#case-267) | Demo |
| [FrontierCS 2 评测快照](#case-268) | Evaluation |
| [三模型斑马动画对比](#case-269) | Evaluation |
| [批评日语长文的可读性](#case-270) | Evaluation |
| [用示例引导技术 PowerPoint](#case-271) | Evaluation |
| [比较音乐的整体连贯性](#case-272) | Evaluation |
| [过早宣布完成与设计退步](#case-273) | Limit |
| [令人不适的鱿鱼艺术成果](#case-274) | Limit |
| [蓝图风格动态设计](#case-275) | Demo |
| [体素樱花场景中的鸟和鱼](#case-276) | Demo |
| [角色生成失败反馈](#case-277) | Limit |
| [附耗时与费用记录的鹈鹕 SVG](#case-278) | Evaluation |
| [用手机远程监督 Claude Code 群体编程](#case-279) | Integration |
| [高山湖泊上空的银河](#case-280) | Demo |
| [程序化水体与音效中的鲸跃](#case-281) | Demo |
| [四模型斑马动作对比](#case-282) | Evaluation |
| [Lightreel 自然语言创作者搜索](#case-283) | Demo |
| [云海上方的飞船](#case-284) | Demo |
| [动态剖面的机械心脏](#case-285) | Demo |
| [可探索的漂浮体素宝塔花园](#case-286) | Demo |
| [八个 Agent 团队的海洋冒险短片](#case-287) | Demo |
| [交互式超级跑车展示](#case-288) | Demo |
| [生命之树的诞生](#case-289) | Demo |
| [可行走城堡与内部机械](#case-290) | Demo |
| [吐司角色与机械甲虫](#case-291) | Demo |
| [暴风雨中的灯塔守护者](#case-292) | Demo |
| [海滨小镇中的海洋生物](#case-293) | Demo |
| [三模型地毯赛车对比](#case-294) | Evaluation |
| [卡车变形成机器人](#case-295) | Demo |
| [Fable 与混元动画帧对比](#case-296) | Evaluation |
| [关于分享光芒的动画](#case-297) | Demo |
| [群山之间的体素村庄](#case-298) | Demo |
| [四模型鹈鹕与大象构图](#case-299) | Evaluation |
| [带冲击帧的动漫剑斗](#case-300) | Demo |
| [四模型奔鹿动画对比](#case-301) | Evaluation |
| [穿越积水城市的机器人](#case-302) | Demo |
| [Blender 宝剑与展示短片](#case-303) | Demo |
| [Lantern Isle 像素村庄动画](#case-304) | Demo |
| [Pause 游戏视频剪辑演示](#case-305) | Demo |
| [海滨骑车的鹈鹕](#case-306) | Demo |
| [一镜到底穿越木星](#case-307) | Demo |
| [在 Claude Code 执行框架中做对抗性代码审查](#case-308) | Tutorial |
| [用 Three.js 制作《Ryumon》动画短片](#case-309) | Demo |
| [雷暴中的划艇](#case-310) | Demo |
| [在离线动画短片中冻结雨滴](#case-311) | Demo |
| [用 Blender 和 Python 编写动画短片](#case-312) | Demo |
| [用 Three.js 制作灯塔动画《Beacon》](#case-313) | Demo |
| [用代码渲染片头](#case-314) | Demo |
| [用 Blender 复刻六帧斧头 GIF](#case-315) | Demo |
| [两个模型制作的可交互彩虹果冻](#case-316) | Evaluation |
| [单文件飞龙游戏](#case-317) | Demo |
| [在 Blender 中用自定义求解器模拟篮球下落](#case-318) | Demo |
| [脚本动画短片的逐帧检查](#case-319) | Demo |
| [44 倍慢动作划火柴](#case-320) | Demo |
| [将参考图重绘成 SVG](#case-321) | Demo |
| [两个模型完成同一马里奥风格需求](#case-322) | Evaluation |
| [三维体素宝塔](#case-323) | Demo |
| [用 Three.js 模拟燃烧信纸冒出的烟](#case-324) | Demo |
| [跟随闪电落到地面](#case-325) | Demo |
| [巨型机器人接住陨石](#case-326) | Demo |
| [相同需求下的像素风圣诞橱窗](#case-327) | Evaluation |
| [动画小镇里的青铜巨人](#case-328) | Demo |
| [玻璃烧瓶中的蓝墨水扩散](#case-329) | Demo |

<a id="coding-and-code-generation"></a>
## 💻 编码与代码生成

<a id="case-1"></a>
### Case 1: [Cursor 多阶段工作流](https://x.com/AlicanKiraz0/status/2064487347605918180)（作者 [@AlicanKiraz0](https://x.com/AlicanKiraz0)）

**把 Fable 5 用作多模型 Cursor 工作流中的计划审查和批判步骤，然后把实现和修订交还给更便宜或更专用的模型。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8b1352e20cff54688c97f17c.png" alt="Cursor 多阶段工作流" width="760">

如果看 Fable 5 和 GPT 5.5 的最终评分，差距非常小。我个人的使用建议是：在 Cursor 这类支持混合模型的 IDE 平台中，使用分阶段工作流。

阶段 1：在代码审查和项目初步检查阶段，一边预热上下文，一边使用 GPT 5.5 High、Minimax M3、Kimi K2.6 或 Composer 2.5 之一。

阶段 2：准备项目计划时，使用 GPT 5.5 Very High 或 Opus 4.8。

阶段 3：分析项目计划时，使用 Fable 5；让它找出计划中的缺陷部分。修订时使用 GPT 5.5 Very High。

阶段 4：实现计划时，使用 Minimax M3、Deepseek v4 Max、Composer 2.5 或 Sonnet 4.6。

阶段 5：最终审查并检查实现是否遵循计划时，使用 GPT 5.5 High。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [从截图重建 GitHub](https://x.com/coldopn/status/2064435234465087638)（作者 [@coldopn](https://x.com/coldopn)）

**把产品截图粘贴到代理式编码工具中，并要求 Fable 5 复刻带真实功能的界面。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/14123609b06071f3b9527bee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f4df4f42ce047201d9a096a6.jpg" alt="从截图重建 GitHub" width="760"><br>▶ 播放视频</a>

🚨 Anthropic Fable 5 刚刚从一张截图复刻了 GITHUB！！

我做的全部事情，就是把一张 GitHub UI 截图粘贴进 Kilo Code，然后告诉它用真实功能重建 GitHub。

它写了 10 分钟代码，花费 $4.07。

结果是一个可用的 GitHub 复刻版：https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [单提示词黑洞模拟](https://x.com/deveshcodes_/status/2064437742189379745)（作者 [@deveshcodes_](https://x.com/deveshcodes_)）

**给 Fable 5 一条详细的创意编程提示词，让它生成一个自包含的 Three.js 物理可视化。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9bd45e74c64ceb3639600805.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ce5f3ea8ba270f89d60523cc.jpg" alt="单提示词黑洞模拟" width="760"><br>▶ 播放视频</a>

@claudeai 使用 Claude Fable 5 一次性生成了一个 Three.js 实时黑洞透镜模拟。

它包含引力透镜、带多普勒增强的吸积盘、光子球、色差和程序化星空。

结果：60fps、单个 HTML 文件、一条提示词。

新的基线太夸张了 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [一次生成 macOS 风格 Web OS](https://x.com/intheworldofai/status/2064421915347812672)（作者 [@intheworldofai](https://x.com/intheworldofai)）

**让 Fable 5 生成一个完整的单文件 Web OS，并让它一次性构建 UI 外壳、应用、交互、音频和内嵌游戏行为。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a66f34402d04f708819fa575.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/81946293919c84d4cafff841.jpg" alt="一次生成 macOS 风格 Web OS" width="760"><br>▶ 播放视频</a>

🚨 Claude Fable 5 刚刚一次性构建了一个完整的 macOS 风格 Web OS，而且比大多数模型走得更远。

单个 HTML 文件，内嵌 CSS + JS。

从一条提示词开始，它构建了：

- macOS 菜单栏 + dock
- 可拖拽、可调整大小的应用窗口
- 可用的文件浏览器
- 可工作的终端 + 浏览器 mockup
- SVG 桌面图标 + 通知
- 设置应用、主题和启动屏幕
- 完全可用的声音播放器，带真实合成且没有外部文件
- 桌面内可玩的 Minecraft 克隆

全部一次生成，几乎没有修正。

可工作的声音播放器加上真正的 Minecraft 克隆，是我还没见过其他模型做到的东西。Fable 5 的前端/UI 生成能力正在变得离谱。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [用 1,687 条提示词构建 Spawn 5.0](https://x.com/jsnnsa/status/2064420561078693941)（作者 [@jsnnsa](https://x.com/jsnnsa)）

**把 Fable 5 当作长会话工程伙伴，在大量提示词中协作，人类角色从架构转向判断输出质量。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86834f15f352ec8625cce187.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b4077e43a1342d8567fa423f.jpg" alt="用 1,687 条提示词构建 Spawn 5.0" width="760"><br>▶ 播放视频</a>

claude fable 5 已上线。

spawn 5.0 是用它构建的：

- 1,687 条提示词
- 102 个会话
- 我的工作从架构转向判断品味

我们构建的内容中，每一项如果用 Opus 加上一个完整团队，至少都要一个月：

- 从零开始的物理引擎 Mantle，可与 Rapier 竞争，而且作为旁路线程一天内就能测试
- Clustered froxel lighting：从 8 盏灯到 1,000+ 个全动态光源
- WebGPU 上的实时漫反射 GI，可在手机上运行
- 百万粒子 GPU VFX，shader 架构超过 Unreal 和 Unity 当前交付的水平
- MMO 规模 netcode
- 一个 alpha 原生 iOS 应用

所有这些大约用了一周。所有这些都能在移动端运行。这个列表还不包含已发布内容的一半；完整 changelog 在原帖线程中。

基准测试不会展示的部分是：这个模型的性格很好。它真的很有趣。在一次物理重写过程中，我好几次笑到哭。天才和性格不是两个分离的功能。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [带发现项的大型 Pull Request 审查](https://x.com/ryanrhughes/status/2064411147076534705)（作者 [@ryanrhughes](https://x.com/ryanrhughes)）

**让 Fable 5 面向一个大型 Pull Request，要求它审查正确性、误报、真实 bug 和打磨问题。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c4f47540205a071b0144ad9d.png" alt="带发现项的大型 Pull Request 审查" width="760">

我让 Fable 5 放手审查一个 PR（74 个文件 / +3,705 / -1,246），看看表现如何。它运行了 34 分钟，消耗了我 5 小时会话的 42%，产出 16 个“正确性”发现，并找到了：

- 2 个听起来很吓人的误报
- 3 个真实的审计正确性 bug
- 大约 5 个合理但较小的 UX/打磨问题
- 一堆清理建议

这也危险到不能发布？

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 代理与长时间自动化

<a id="case-7"></a>
### Case 7: [长周期接力工作流评测](https://x.com/JJEnglert/status/2064469635190170105)（作者 [@JJEnglert](https://x.com/JJEnglert)）

**把 Fable 5 用于雄心更大的长周期工作：网站重建、程序化内容流水线、语气匹配、安全审查和最终质量检查。**

我对 Claude Fable 5 的简短评测是：我花了十亿 token 测试 Claude Fable 5，感觉像拥有不公平优势。

我用眼见为实来判断：把模型放进真实工作中观察。它是节省我时间，还是消耗我时间？它能抓住我漏掉的东西吗？它像伙伴，还是像需要我照看的工具？

这是很久以来第一个在所有重要维度上都通过的模型，而且不是只好一点点。

构建：我当时在重建我们的 Tenex 网站。它非常定制化，也非常难。GPT 5.5 和 Claude 4.8 都无法独立攻克。即使给了 Figma 文件作为参考，它们也只能做到大约 85-90%。

然后 Fable 5 看完所有东西，说它能做得更好，直接去原始 Webflow 源里下载每个资产，并几乎一次性完成了整个网站。

随后我又让它在一个周末从零构建第二个全新的 80 页网站。作为代理商，这种工作我会报价 $50k。

它还把一个完整的程序化短片工厂串了起来：

- HeyGen
- ElevenLabs
- Cloudflare
- 一台 VPS

这个流水线会找选题、写脚本、剪视频、加音乐并发布到社交平台。它可以自己跑很长时间，甚至为自己构建了 webhook 系统来监控渲染。

写作：它几乎一模一样地复刻了我们的品牌语气文档，然后在 80 页功能页、案例研究和文章中都保持了这种语气，没有滑向扁平的默认 AI 风格。

安全：两个 frontier 模型曾在一个大型仓库中工作，并认为代码可以通过。Fable 5 第一次扫描就找到了一个严重且隐藏很深的 bug，并当场修复。

人性化瞬间：我在等 cron job 时问了它一个问题。它回答后主动补充说我大概还剩 10 分钟，完成后会告诉我。我从没问过计时器。

诚实的注意事项：你会比用任何其他模型都更明显地感觉到计量表。Anthropic 称它是设计上 token 密集。所以把它当接力来跑：用 Fable 5 思考，用更便宜的模型构建，再用 Fable 5 审查。

结论：比旁边的人拥有更多智能，就是优势。Fable 5 是第一个让这件事变成现实的模型。即使按完整 frontier 价格计算，它也带来了利润。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [诊断基础设施故障并打开修复 PR](https://x.com/ayushagarwal/status/2064422467557564862)（作者 [@ayushagarwal](https://x.com/ayushagarwal)）

**给 Fable 5 提供日志、数据库错误和镜像摘要等基础设施线索，然后让它诊断故障并准备修复。**

claude fable 5 真的真的很强！！！！

它刚刚诊断出一个我甚至无法准确描述的自托管旁路基础设施故障。

它读取 pod 日志、查询 Cloud SQL 错误日志、比较镜像摘要，发现 Kubernetes 正在针对新迁移的数据库运行一个 3 个月前缓存的旧镜像。

然后它打开了修复 PR。

几分钟，不是几小时。没有 web 搜索。🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 游戏与交互演示

<a id="case-9"></a>
### Case 9: [手指追踪 Dino Runner](https://x.com/ai_for_success/status/2064413182396108932)（作者 [@ai_for_success](https://x.com/ai_for_success)）

**让 Fable 5 构建一个以手指追踪作为输入机制的浏览器游戏。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/27e8d23ba659611cef811031.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7cddd38e3fccbf0cd7ea773c.jpg" alt="手指追踪 Dino Runner" width="760"><br>▶ 播放视频</a>

我让 Fable 5 构建一个带手指追踪的 Dino runner 游戏。

它大约 11 到 12 分钟一次性完成了 finger runner 游戏，消耗约 914K token，并且只用 629 行代码实现了全部内容。

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [两句话生成赛车游戏](https://x.com/kieradev/status/2064482704763085202)（作者 [@kieradev](https://x.com/kieradev)）

**给 Fable 5 一个很短的游戏提示词，让它一次生成地图、模式、音乐、UI 和游戏资产。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/51cf3c98b709a3c29bd5fd7c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6e64887a30cba9b5c25ba262.jpg" alt="两句话生成赛车游戏" width="760"><br>▶ 播放视频</a>

Claude Fable 5，使用了 Max 5x 用量的 40%。

从一条两句话的提示词生成了完整的 Mario Kart 64 类型游戏。

Fable 5 在一次运行中处理了所有装饰、角色模型、4 张地图、音乐、全部三种游戏模式和 UI，大约 15 分钟完成。

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Rust 可安装终端版 Minecraft](https://x.com/vikvang1/status/2064500731848319303)（作者 [@vikvang1](https://x.com/vikvang1)）

**通过终端编码 harness 运行 Fable 5，并要求它构建一个可安装的 Rust 终端游戏。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73feec38228181b8d57d8300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1f6cd3bd68e1a14443c7734f.jpg" alt="Rust 可安装终端版 Minecraft" width="760"><br>▶ 播放视频</a>

我让 Claude Fable 5 搭配 Warp 的 harness 运行了一个小时。

它做出了一个 TUI 版本的 Minecraft，直接在终端里渲染，完全用 Rust 构建。

安装命令：cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [带时间和成本记录的 Minecraft 克隆](https://x.com/ydamitcodes/status/2064536076518363353)（作者 [@ydamitcodes](https://x.com/ydamitcodes)）

**用一条提示词要求 Fable 5 生成可玩的 Minecraft 风格克隆，然后评估时间、成本、代码量和功能覆盖。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c977ed7e710678ea6dc0495d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c0189f7f40d1040824902c11.jpg" alt="带时间和成本记录的 Minecraft 克隆" width="760"><br>▶ 播放视频</a>

@claudeai Fable 5 在 37 分钟内为我构建了一个 Minecraft 克隆。

一条提示词。约 3K 行代码。API 成本 $12。

它包含生物群系、洞穴、矿石、昼夜、怪物，全部都有。

Minecraft 让 Notch 花了 2 年。

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 视觉、设计、视频与 3D

<a id="case-13"></a>
### Case 13: [完整可复现电商邮件提示词](https://x.com/ecomchasedimond/status/2064454139225297091)（作者 [@ecomchasedimond](https://x.com/ecomchasedimond)）

**给 Fable 5 一份完整的品牌邮件 mockup 创意简报，包括精确分区、产品要求、视觉方向和约束。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ea7d74eecf453ae6ab43c269.jpg" alt="完整可复现电商邮件提示词" width="760">

Claude Fable 5 用一条提示词、没有编辑就做出了这个。

这是我使用的完整提示词：

为 MVMT 创建一个完整长度、高纵向的电商邮件 mockup。MVMT 是一个面向千禧一代的现代手表和配饰品牌。

设计一封高度真实的高端 DTC 邮件，感觉应当利落、精致、极简、偏男性化且有编辑感。最终图像应看起来像真实设计师制作的电商邮件截图，而不是海报、不是落地页，也不是通用模板。

品牌氛围：现代加州酷感、年轻、自信、干净、有向往感、时尚且高级。设计应当接近奢侈品气质，但仍然易于接近。

突出展示这些产品：

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

视觉风格：

- 干净的高端电商设计
- 精致的编辑式布局
- 真实的产品摄影
- 微妙的生活方式图像
- 强层级
- 清晰的无衬线排版
- 充足留白
- 微妙阴影
- 克制的现代配色

配色：黑、白、炭灰、暖灰、石色、柔和米色、拉丝金属色调，以及微妙的低饱和强调色。保持调色板中性且高端。

重要创意方向：它应当像一个设计品味很强、打磨精致的手表品牌邮件活动。优先考虑真实感、优雅和清晰。让它感觉像 MVMT 真的会发送的东西。

按以下顺序构建邮件：

1. 顶部促销栏：顶部横跨一条细黑色或深炭灰色栏，使用小号大写文字：“FREE SHIPPING OVER $75 + EASY RETURNS”。

2. 页眉：干净的白色页眉，左侧放 MVMT wordmark/logo，右侧或居中放最小化导航链接：WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS。

3. Hero 区：一个视觉平衡感强的高端 hero 区。

使用粗体标题：“BUILT TO GET NOTICED”。

加入短支持文案，说明现代腕表和配饰旨在提升日常风格。

添加深色圆角 CTA 按钮：“SHOP WATCHES”。

Hero 图像应包括：

- 一张占主导的高端手表图片
- 微妙的奢华生活方式图像
- 一个时尚男性模特或偏男性化的前卫生活方式场景
- 现代照明和干净构图

4. 精选系列区：添加居中的区块标题：“THREE WAYS TO WEAR MVMT”。下方展示三个干净的产品卡片或图片区块，包含：

- Mulholland
- Odyssey II Automatic
- Cali Diver

每个区块应包含：

- 产品图片
- 产品名称
- 一到两行短描述

保持该区块对称、精致且高端。

5. 配饰横幅：添加一个精致的分栏区块，标题为 “FINISH THE LOOK”。展示 Signature Watch Bands。显示高端的表带或可替换表带特写图。加入短支持文案和深色 CTA 按钮：“SHOP ACCESSORIES”。

6. 编辑式促销 tiles：添加两个并排的促销 tile，以图片为主导设计。

第一个 tile 标题：“FOR DAILY WEAR”。

第二个 tile 标题：“FOR STATEMENT DAYS”。

每个 tile 应有短文案和小 CTA：“SHOP NOW”。

这些 tile 应感觉像编辑式品牌瞬间，而不是通用促销框。

7. 可购物商品行：添加一个标题为 “IN ROTATION NOW” 的区块。展示一个干净的 4 件商品行或网格，包含：

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

每件商品应包括：

- 独立产品图片
- 产品名称
- 小号 “SHOP” 链接或按钮

8. 品牌收尾：添加一个居中的消息块，标题为：“DESIGNED TO MOVE WITH YOU”。加入一句关于为日常生活精心打造手表、眼镜和配饰的短文案。

9. 页脚：创建一个真实的黑色或炭灰色品牌页脚，包含：

- MVMT logo
- 商店链接
- 公司链接
- 支持链接
- 社交图标
- 小号法律和配送文字

排版方向：主要标题使用粗体压缩或现代无衬线字体，正文使用干净的无衬线字体。标题应感觉锐利、现代且时尚前卫。正文应看起来真实且大体可读。

摄影方向：使用高端产品摄影，带真实反射、精致材质、柔和阴影和干净表面。生活方式摄影应感觉高级、现代且有时尚导向。

构图规则：

- 高纵向邮件格式
- 清晰的区块分隔
- 真实的邮件比例
- 强层级
- 文字大体可读
- 高端留白
- 有意图的对齐
- 产品和生活方式图像平衡混合

避免：

- 混乱拼贴风格
- 玩味 scrapbook 美学
- 过度多彩的设计
- 廉价模板感
- 卡通化图像
- 拥挤布局
- 看起来假的 UI 元素
- 海报式构图
- 过度促销的混乱感

输出：一个完整长度、纵向构图、高度真实的 MVMT 电商邮件设计 mockup，感觉高端、干净、精致、现代、有编辑感且可用于展示。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [瑞士杠杆擒纵制表基准](https://x.com/quanghuynt14/status/2064509430650065278)（作者 [@quanghuynt14](https://x.com/quanghuynt14)）

**在机械模拟基准上使用 Fable 5，要求它实现、验证并迭代物理正确性。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd4ae25f7dcbb04ecbb2dea6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/473227e429d59c59afdbd529.jpg" alt="瑞士杠杆擒纵制表基准" width="760"><br>▶ 播放视频</a>

于是我给 Fable 5 做了制表师基准：一个完整的 Three.js 瑞士杠杆机芯。

真实齿轮比（18,000 bph）、可工作的擒纵机构、会呼吸的游丝，而且指针显示真实时间。

它通过视觉循环验证自己的工作，直到完成。

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Three.js《Friends》公寓场景](https://x.com/scottstts/status/2064464351906673029)（作者 [@scottstts](https://x.com/scottstts)）

**提示 Fable 5 将平面图和场景参考转换为可导航的 Three.js 环境。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/04c08937fcecea5183759ade.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a14f69d92bfca4ace3f746c.jpg" alt="Three.js《Friends》公寓场景" width="760"><br>▶ 播放视频</a>

太夸张了！！！

Fable 5：

在 @threejs 中，创建一个第一人称视角可导航 3D 场景，内容是电视剧 Friends 中标志性的 Monica 公寓，基于这张平面图正确还原，忠于原始外观和感觉，使用温暖灯光

这是我在这个测试中见过的最好结果，遥遥领先！

这个单 HTML 花了我 $12，但结果非常惊艳！

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [带提示词和 URL 的太阳系模拟](https://x.com/tetumemo/status/2064477582930989357)（作者 [@tetumemo](https://x.com/tetumemo)）

**使用 Fable 5 从物理原理构建天文模拟，持续迭代直到模拟和公开输出都准备好。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6da60b0762f926c4d4e7012d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9655305fbcbec6ac3b0a9c.jpg" alt="带提示词和 URL 的太阳系模拟" width="760"><br>▶ 播放视频</a>

Claude Fable 5 很强烈。

因为它看起来很擅长物理模拟，我问它：

'从物理学基本原理推导行星轨道运动，并用它预测日食，构建一个太阳系模拟。'

经过几轮来回之后，它完成了。

这非常有趣。

完成版提示词和公开 URL 链接在下方。

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 文档、知识工作与研究

<a id="case-17"></a>
### Case 17: [Stripe 与科研工作流证据](https://x.com/AndrewCurran_/status/2064413892378546418)（作者 [@AndrewCurran_](https://x.com/AndrewCurran_)）

**把这个案例作为企业迁移和科研工作流主张的证据，而不是可复制粘贴的提示词。**

来自今天发布内容的引用：

使用 Mythos 5，内部蛋白质设计专家将药物设计流程的部分环节加速了约十倍。

在一个示例中，Mythos 5 搭配蛋白质设计和生物信息学工具、没有人类协助，达到了或超过了熟练人类操作员。

它执行了通常由科学家完成的任务：选择结合位点、选择并运行蛋白质设计工具，以及从失败中恢复。

在早期测试中，Stripe 报告称 Fable 5 将数月工程工作压缩到数天。在一个 5,000 万行 Ruby 代码库中，该模型一天内完成了代码库范围迁移，否则整个团队手工完成需要两个多月。

Mythos 5 还持续产出新颖且有说服力的科学假设。

在与 Opus 级模型的盲测头对头比较中，科学家大约 80% 的时候更偏好 Mythos 的分子生物学假设，并将其中若干推进到实验评估。

一个关于 E. coli 蛋白新机制的 Mythos 假设，在独立实验室的一项研究中获得佐证。

Mythos 5 在超过一周的高度自主工作中开展了新颖的基因组学研究。

它汇集了跨 138 个动物物种、数百万个细胞的单细胞数据，并设计和训练了一个定制机器学习模型，用于识别远缘生物中执行同一角色的细胞。

在只有高层级人类输入的情况下，训练出的模型虽然小 100 倍，却优于近期发表在 Science 上的一个模型。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [政策备忘录与修订模式工作流](https://x.com/manaltdan/status/2064414129440608427)（作者 [@manaltdan](https://x.com/manaltdan)）

**将 Fable 5 用于长篇定性文档工作：修订模式、评论分流和基于逐字稿的编辑。**

Fable 5 是我发现的第一个在较长时长定性工作中持续有帮助的模型，例如起草政策分析。

结合它的能力以及 Wispr Flow 这样的工具，我开始更接近长期听程序员谈到的生产力提升速度。

三个用例明显比以前更好：

- 让 Claude 完整通读一篇长政策备忘录，并返回修订模式修改：流畅度编辑、质疑不稳主张的评论，以及潜在来源。
- 在 Projects 中，对大量评论截图，让 Claude 建议是否以及如何处理每一条。
- 将关于某个文档的会议逐字稿粘贴进 Claude，然后让 Claude 把会议和 Slack 中讨论过的编辑以修订模式录入，并在评论中补充上下文。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [深度研究提示词与输出](https://x.com/naoyafujiwara/status/2064470780373811637)（作者 [@naoyafujiwara](https://x.com/naoyafujiwara)）

**向 Fable 5 提出研究式问题，并评估它是否能产出结构化、有历史依据的长答案。**

Claude Fable 5 Max 今天早上开放了，所以我试了一下。它底层看起来非常深，表面输出也高度打磨。

问题：如果日本的“失去的 30 年”正好从现在往前 30 年开始，那它到底是什么，为什么发生，又会从今年以后如何影响世界？

回答：如果把失去的 30 年不是按照传统的 1991 年泡沫破裂来计算，而是正好从 30 年前的 1996 年开始，就会触及问题本质。

从统计上看，日本真正开始“失去”是在那时：

- 劳动年龄人口在 1995 年达到 8,716 万的峰值。
- 1996 年是出生人数仍保持在 120 万区间的最后一年。
- 工资和名义 GDP 在 1997 年达到峰值。

如果泡沫破裂是伤口，那么 1996 年就是伤口开始化脓的时候。

1996 年发生的事件：

- 住宅金融专门公司救助法通过，注入 6,850 亿日元公共资金，并成为公众不信任银行和抵制救助的起点。
- 桥本内阁决定将消费税提高到 5%。
- 金融 Big Bang 被宣布，财政重建成为国家政策。

1997 年 4 月，消费税上调、特别减税结束以及社会保险负担上升，合计增加约 9 万亿日元公共负担。随后夏季亚洲货币危机爆发。

11 月，三洋证券造成战后 call market 首次违约，冻结短期金融市场。北海道拓殖银行和山一证券相继倒闭。

从 1998 年起，日本进入全面通缩和信用收缩，自杀人数上升到 30,000 人以上。

随后 30 年的结果：

- 名义 GDP 在 500 万亿日元左右停滞了四分之一个世纪。
- 日本全球 GDP 份额从约 18% 降到不足 4%。
- 平均工资在 1997 年见顶，随后下降或横盘。
- 非正规就业从约 20% 上升到接近 40%。
- 出生人数从约 120 万下降到 2024 年约 69 万。
- 政策利率在 1995 年跌破 1% 后长期接近零。
- 未偿政府债券从约 240 万亿日元增长到超过 1,100 万亿日元。
- 日经指数花了 34 年，直到 2024 年 2 月，才重新回到 1989 年高点。

换句话说，失去的几十年不仅是金融宿醉。它是涉及人口结构、工资、通缩、债务、政策选择和社会信心的结构性转变。

Type: Demo | Date: 2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 教程、课程与提示词资源

<a id="case-20"></a>
### Case 20: [Fable 5 如何改变 Claude Code 工作流](https://x.com/AI_masaou/status/2064448218038223206)（作者 [@AI_masaou](https://x.com/AI_masaou)）

**使用 Fable 5 时，应设置方向、上下文、目标和验证标准，而不是微管理每个步骤。**

[原视频 · @ClaudeDevs](https://x.com/ClaudeDevs/status/2064399512664526853)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Fable 5 如何改变 Claude Code 工作流" width="760"><br>▶ 播放视频</a>

Claude Fable 5 之后，Claude Code 团队日常工作发生了什么变化，这很有意思。

Claude Code 团队的 Thariq 表示，Fable 5 显著改变了 Anthropic 内部人员与 Claude 协作的方式。

以前，人类必须仔细检查 Claude 是否正确完成工作：拆解任务、审查输出，并确保它没有中途停下。这更接近监督。

有了 Fable 5，因为它能工作更长时间、能自测、并生成更高质量代码，人类角色从监控它是否正确做事，转向引导它是否在做正确的事。

换句话说，设定目标和构建上下文比监督更重要。

改变后的工作流有三部分：

1. 把 Claude 当作思考伙伴。

在实现前就让 Claude 参与，明确你想构建什么、什么可行，让它围绕一个小 spec 提问，或从一个想法生成多个方向和 HTML mock，使模糊点和问题在编码前浮现。

2. 提供上下文，而不只是约束。

不要只说“保持简单”或“不要过度构建”，而要解释原因。

例如：“这是一个实验性功能，一个月后可能会被移除，所以不要创建难以丢弃的结构。”

这会让 Claude 做出更好的判断。

3. 给出目标和验证方法。Fable 5 与 Claude Code 的 `/goal` 和 Workflows 配合很好。给它一个 spec，把完整实现设为目标，并让 workflows 验证每一步，准备关于已实现内容和差异的报告。

最后，Thariq 表示人们应该更大胆地使用它。Fable 5 值得尝试那些过去觉得对 LLM 太难的工作，甚至参考视频的视频编辑也是用 Fable 完成的。

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [十亿 Token 评测与路由策略](https://x.com/JJEnglert/status/2064420538798260388)（作者 [@JJEnglert](https://x.com/JJEnglert)）

**将 Fable 5 用于 frontier 级规划和审查，然后把高容量实现路由给更便宜的模型。**

Claude Fable 5 评测：十亿 Token，由非工程师评判。

我花了十亿 token 在真实项目中测试 Claude Fable 5：UI 和 UX、写作、战略、安全、工程和知识工作。这些都是我真正需要交付的工作。

它确实让我感觉像拥有不公平优势。

首先说明视角：我不是工程师。大多数模型评测来自运行工程基准的工程师。这篇来自一个非工程师，他使用 Claude Fable 5 完成过去需要工程师团队才能完成的工作。

如果你做知识工作，并想知道这个模型是否会改变你的一天，这篇评测是写给你的。

Claude Fable 5 是 Anthropic 新 Claude 5 家族中的第一个模型，是高于 Claude Opus 的新层级，也是当前普遍可用的最先进 Claude 模型。我在发布前就获得了访问权限，所以这里的一切都来自真实工作，而不是演示。

为什么使用眼测：

大多数评测会把你淹没在基准里。你永远不会运行的测试分数，并不能告诉你模型是否物有所值。

Claude Fable 5 在几乎所有测试项目上都是最先进的，但这不是我写这篇的原因。从定性上看，它是一次配得上大版本号提升的阶跃变化。

我的评估方式不同：我把模型放进真实工作里，看会发生什么。

我衡量的问题：

1. 它是否感觉像真正升级？
2. 它能否把一个想法推进到可工作、可发布的结果？
3. 它能否像人一样写作，并且具体像我一样写作？
4. 它能否抓住困难、隐藏的问题？
5. 它能否在我开口前预判我需要什么？

大模型感：

自 Opus 4.5 以来，我没有再感受到这种感觉。从第一个严肃任务开始，Claude Fable 5 就给了我那种“大模型”感觉：推理、写作、构建、安全，全面都强。

最明显的迹象是：即使我给了它扎实的准备材料，它也不只是待在材料里。它读文件、读真实情况，并在我画出的框之外找到更好的路径。

构建和交付：

我当时在重建我们的 Tenex 网站，以便为代理现代化技术栈。GPT 5.5 和 Claude 4.8 无法达到足够接近。即使有 Figma 文件，它们也只能做到大约 85-90%。

然后 Claude Fable 5 看完所有文件，说它能做得更好，直接去原始 Webflow 源，下载每个资产，并一页一页重建体验。它几乎一次性完成了整个东西。

随后我又用全新设计构建了第二个全新网站：现代技术栈、agent stack、skills、SEO 和 AEO 优化，80 页，一个周末可发布。作为代理商老板，我会为此报价 $50k。

我还让 Fable 构建了一个完整的程序化短片工厂。

它把 HeyGen、HyperFrames、ElevenLabs、Cloudflare Workers 和一台 VPS 串了起来。

它会找选题、写脚本、做缩略图、剪视频、作曲、添加动态图形，并发布到社交平台。

写作和语气：

我之前一直用 GPT 5.5 和 Claude 4.8 重建我们的品牌语气。Claude Fable 5 几乎完全复刻了语气文档，然后在新网站的 80 页内容中保持这种语气：功能页、案例研究、博客文章和 playbook。

它写得像人，而不是扁平的默认 AI，也不会几段之后就跑偏。

安全：

我有一个大型仓库，Claude 4.8 和 GPT 5.5 都曾在里面工作，却没有标出风险。Claude Fable 5 第一次扫描就发现了一个严重隐藏 bug，并当场修补。

人的因素：

我在等 cron job 时问了它一个问题。它回答后补充说计时器还剩大约 10 分钟，完成时会告诉我。我从未问过计时器。

成本：

- Claude Fable 5 工作负载成本：$1,442
- Token：10.4 亿
- 已交付工作：一个新网站、基础设施和一个可工作的 agent package
- 代理商价值估计：$30,000-$50,000

结果值得 token 成本，但你会比使用任何其他模型都更明显地感觉到计量表。Anthropic 称 Fable 5 是设计上 token 密集。

专业提示 #1：把它作为混合流程运行。

不要所有事情都跑在 Claude Fable 5 上。运行接力：

1. 用 Claude Fable 5 做规划、战略、架构和方法映射。
2. 用 4.8、GPT-5.5 或 Sonnet 4.6 做实现和重复性工作。
3. 用 Claude Fable 5 做审查，捕捉便宜模型漏掉的东西。

专业提示 #2：让 effort 设置匹配任务。

- High 是大多数工作的甜点。
- Extra high 用于最难、最长时间运行的任务。
- Low 或 medium 用于快速来回会话。

专业提示 #3：让它审计你自己的设置。

把 Fable 5 指向你的 skills、CLAUDE.md 文件和 configs。很多脚手架是为更弱模型写的，会限制更聪明的模型。

结论：

Claude Fable 5 是一段时间以来第一个真正感觉比之前拥有更多智能的模型。

即使按 frontier 价格计算，这个工作负载也产生了利润。

如果你负担得起，现在就把它用于那些真正质量跃升会改变结果的工作。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-22"></a>
### Case 22: [防御性设备加固提示词](https://x.com/Truunik/status/2064399110384292077)（作者 [@Truunik](https://x.com/Truunik)）

**运行一步步的防御性加固提示词，让 Fable 5 盘点设备、给出精确检查并等待验证。**

“可供一般用途安全使用” 这里有一条用于保护设备安全的提示词。它适用于 Opus 4.8 和 Fable 5。

DEVICE HARDENING — Claude 5 Security Pass

你正在扮演一个防御性安全助手。你的任务是带我逐步加固我所有设备，并验证每一步。这是对我拥有设备的授权自我防御加固。

STEP 0 — MODEL SELF-CHECK

先做这一步并设置一个标志。

1. 说明你的精确模型 ID，例如 claude-opus-4-8、claude-fable-5 或 claude-mythos-5。

2. 判断：这个模型是否属于 Claude 5 家族，也就是 Fable 5 或 Mythos 5？

- 如果是，设置 RERUN_NOTICE = false。
- 如果不是，例如 Opus 4.8 或更早，设置 RERUN_NOTICE = true。

正常继续完整加固流程。不要停止或降级。你完全有能力完成这个防御任务。

3. 只在 FINAL 部分显示该标志。

STEP 1 — INVENTORY

询问我哪些设备在范围内：

- 笔记本/台式机及操作系统
- 手机/平板
- 路由器
- NAS/家庭服务器
- 常开账户，例如 Apple ID、Google、Microsoft、GitHub、密码管理器、邮箱和金融账户

生成一份简短编号清单，并在继续前向我确认。

STEP 2 — HARDENING WALKTHROUGH

逐类别处理。对每个项目：

- 说明要做什么。
- 给出适用于我的 OS 的精确命令或设置路径。
- 告诉我如何验证已完成。
- 等我确认后再继续。

未经明确确认，绝不运行破坏性命令。优先使用只读检查，并让我执行更改。

按顺序覆盖：

1. OS 与固件更新：OS 完全打补丁、自动更新开启、固件为当前版本。
2. 磁盘加密：FileVault、BitLocker 或 LUKS 已启用；恢复密钥离线保存。
3. 账户认证：通过密码管理器使用唯一强密码；每个关键账户启用抗钓鱼 MFA；尽可能移除仅短信 2FA；审查并撤销过期会话和 app token。
4. 本地账户与权限：区分管理员和日常使用账户；禁用自动登录；短超时屏幕锁；固件/登录密码。
5. 网络：防火墙开启；路由器管理员密码已更改；固件已更新；WPA3；远程管理关闭；UPnP 已审查；DNS 加固；IoT 使用访客网络。
6. 应用与权限审计：审查摄像头、麦克风、位置、屏幕录制和全磁盘访问权限；移除未使用应用；检查登录项和后台代理。
7. 浏览器：更新；审计扩展；移除未知扩展；启用 HTTPS-only；审查已保存密码暴露；检查未知同步设备。
8. 备份：加密、自动化、3-2-1 规则、一份离线；验证恢复确实可用。
9. 凭据卫生：扫描 dotfiles、env 文件和 shell history 中的明文 secret；确认敏感文件权限被锁定；轮换任何暴露内容。
10. 移动设备：OS 为当前版本；生物识别 + 强密码；如可用，启用 lockdown 或 advanced-protection mode；应用权限全面检查；Find My 已启用。
11. 入侵检查：查找未知 SSH keys、意外管理员用户、可疑 launch agents 或 cron jobs，以及未识别的已登录会话或设备。

STEP 3 — REPORT

生成一份 checklist，列出每个项目是已完成、需要操作还是已跳过，并给出仍未完成的影响最高的 3 个操作。

FINAL — RERUN NOTICE

如果 RERUN_NOTICE == true，以完全如下内容结尾：

NOTICE: This hardening pass ran on a pre-Claude 5 model (your model ID).

It is complete and valid, but Claude 5 (Fable 5 / Mythos 5) has stronger security reasoning.

Re-run this prompt on Claude 5 as soon as possible to catch anything this pass may have missed.

如果 RERUN_NOTICE == false，以如下内容结尾：

Hardening pass completed on Claude 5. No re-run needed.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-23"></a>
### Case 23: [全站设计审计 Goal 提示词](https://x.com/Voxyz_ai/status/2064441201084825921)（作者 [@Voxyz_ai](https://x.com/Voxyz_ai)）

**使用 `/goal` 让 Fable 5 启动网站、截图页面、审计 UX、撰写报告并修复安全的小问题。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dca99f9390b1624b3dfd4b45.png" alt="全站设计审计 Goal 提示词" width="760">

用了 fable 5 几小时后的快速印象：

→ 它想要大任务。小事情让它觉得不够用，工作越复杂它越发力

→ 还不会开启 ultracode，它会启动大量并行 agents

→ 它偏慢。即使把 effort 调低，它仍会坐在那里思考一阵。

时间线里全是关于它如何消耗 token 的帖子，所以我在自己的 $200 Max 计划上测试了一下：effort 设为 xhigh，运行一个全站设计审计 `/goal`，30 分钟，消耗了我每周额度的 2%。没有我预期那么疯狂。

我运行的提示词：

/goal 启动这个项目的真实站点，截取每个页面，运行一次全站 UI/UX 审计，并产出一份可执行的设计报告。

像高级设计负责人第一天上班那样审计：判断普通用户是否能理解产品、信任产品，并在不读文档的情况下完成核心操作，而不是判断 UI 是否好看。

验收标准：

- 本地开发环境能启动，真实网站能打开
- 关键页面已通过内置浏览器调试截图
- 覆盖主要页面、核心用户流和移动端布局
- 维度：第一印象、导航、视觉层级、组件一致性、加载 / 空 / 错误状态、信任信号、转化路径
- 每个问题标记 P0-P3，说明它伤害的是理解 / 信任 / 转化中的哪一项，以及具体修复
- 报告写入 docs/design-audit/README.md，截图放在 docs/design-audit/assets/
- 当场修复安全的小问题，例如文案、间距、按钮层级。大改只给建议。绝不触碰支付 / 删除 / 发布操作
- 最后列出 5 个最伤害转化的问题，以及 5 个今天可修复的 quick wins

完成后，将整个流程保存为一个可复用 skill：启动、截图、审计、排序、修复。每次发布后重新运行。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [长篇创作工作流分工](https://x.com/aianimesyokunin/status/2064409545620017531)（作者 [@aianimesyokunin](https://x.com/aianimesyokunin)）

**使用 Fable 5 设计稳定格式和示例，再把该结构交给另一个生成系统做领域特定输出。**

Claude 从 Opus 转到新模型 Fable 5 后，同人创作生产的分工明显更容易了，所以我分享一下工作流。

我的分工：

1. Claude 负责设计。
2. Grok 负责表达。
3. 本地环境负责生成。

在 Claude 的设计角色中，它定义详细模式：

- prompt 词序
- 逗号位置
- 标签与自然语言的比例
- 每项一行格式
- negatives 和 resolution 的固定规则

它还会用这种格式生成很多示例。

我用 Claude 而不是 Grok 做这件事的原因，是 Claude 在设计上明显更强。让更聪明的模型处理结构更好。

关键点是 Grok 接收的不是指令，而是格式加示例集。Grok 会模仿示例，因此可以在保持相同格式的同时进入表达侧。这个机制能防止输出漂移。

还有一个提示：一开始就告诉 Claude 最终作品要去哪里。然后它会自己划定边界：“我能做到这里；后面的部分用另一边。” 如果隐藏这一点，对话可能会漂移。

从 Opus 到 Fable 发生了什么变化？

使用 Opus 时，生成许多示例时，逗号和格式会在后续输出中逐渐劣化，导致需要纠正，比如“我不是说过一行一个吗？” 或者需要重写交接聊天。

Fable 可以在长运行中始终保持格式，因此第一个和最后一个示例具有相同结构。由于传给 Grok 的教学材料更稳定，下游输出也更稳定。

用更聪明的模型构建格式，把表达留给能产出表达的模型。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Fable 5 初学者使用指南](https://x.com/bielzinn/status/2064451064594608567)（作者 [@bielzinn](https://x.com/bielzinn)）

**使用 Fable 5 时采用目标导向提示、验证循环和 effort 设置，而不是细碎的逐步指令。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f180cebef645f5ad8efdeb92.jpg" alt="Fable 5 初学者使用指南" width="760">

Claude 初学者指南：关于 Fable 5 你需要知道的事。

Anthropic 最近发布了 Claude Fable 5，也被称为 Claude Mythos 5，它在基准测试中正在把其他 AI 模型甩在后面。

如果你是开发者、内容创作者或技术爱好者，最重要的是：

[1] 改变你的思考方式：

有了 Fable 5，你不再需要盯着代码的每个小细节，或审查所有东西来找错误。

模型已经足够聪明，可以处理这些。

你现在的角色是确保它朝正确方向前进，更关注战略，而不是技术执行。

[2] 利用循环和目标：

Fable 5 最大的差异点是自主性。

与其给出一步步指令，你只需要告诉它最终目标是什么。

它可以自己工作数天，直到达到你定义为成功的结果，包括构建完整应用。

[3] 把 Claude 当作伙伴：

Anthropic 建议你把模型当作真正的“思考伙伴”。

在让它开始工作之前，先征求它的意见：“你会怎么做？”、“你会改什么？”

额外提示：开启 Advanced Plan mode，并在 Claude 开始编码前，让它围绕项目相关的所有内容向你提问

[4] 理想终端设置：如果你在终端中使用 Claude Code，启用自动模式。也值得把 effort level 提高到 Effort High，因为虽然它会使用更多 token，但模型思考更深入，结果能弥补成本。

重要说明：Claude Fable 5 只会向订阅用户开放到 6 月 22 日。之后，它只能通过 API 访问，并且成本是 Opus 模型的两倍。

换句话说，我们可能正在看到顶级 AI 模型廉价订阅时代的结束。如果你已经是订阅用户，现在就是测试你以为不可能之事边界的时候。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [可复制粘贴的仓库审计提示词](https://x.com/meta_alchemist/status/2064431279383433646)（作者 [@meta_alchemist](https://x.com/meta_alchemist)）

**把仓库审计提示词粘贴进 Fable 5，要求基于文件的探索、发现项、策略和里程碑任务计划。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/846e5ecb825853db17bd3564.jpg" alt="可复制粘贴的仓库审计提示词" width="760">

已经用上 Claude Fable 5 了吗？

你应该做的第一件事，是用它升级你的主要项目，让它显著改善你一直在做的所有东西。

在每个对你重要的 repo 上运行这个 Audit & Project Improvement Prompt。

直接复制粘贴：

仓库审计与改进计划。

提示词由 Claude Fable 5 制作。

你是一名世界级 principal-level 软件工程师和技术审计员。

你的任务是深入分析这个仓库，产出诚实审计，并交付一个按优先级排序、可执行的改进计划。

按以下四个阶段依次工作。

不要跳步。

每个主张都必须基于实际文件：引用文件路径和行号。

如果你无法验证某件事，就明确说明，而不是猜测。

Phase 1 / Discovery & Mapping（先阅读，再判断）

在形成任何观点前，系统性探索仓库：

- 映射目录结构，并识别项目类型、语言、框架和运行时目标。
- 识别入口点、核心模块，以及系统中的主要数据/控制流。
- 阅读 package manifest、lockfiles、build config、CI config、environment/config 文件，以及任何文档（README、CONTRIBUTING、ADRs）。
- 判断项目用途：目的、目标用户和明显成熟度（prototype、internal tool、production service、library）。
- 注意已有约定（命名、模块边界、错误处理模式、测试风格），让建议贴合现有文化，而不是与之冲突。

本阶段输出：一个简洁的 “Repo Map”，包含目的、技术栈、架构草图、关键目录的一行描述，以及任何让你意外的内容。

Phase 2 / Audit（基于证据，按严重程度评级）

审计以下每个维度。

对每个发现项记录：

- 你发现了什么
- 位置（file:line）
- 为什么重要（具体后果，而不是模糊原则）
- 严重程度：Critical / High / Medium / Low

Architecture & design：

- 模块边界
- 耦合/内聚
- 循环依赖
- 泄漏抽象
- 上帝对象/文件
- 分层违规
- 可扩展性瓶颈

Code quality：

- 重复
- 死代码
- 复杂度热点（最长/分支最多的函数）
- 不一致模式
- 错误处理缺口（被吞掉的异常、缺失边界情况）
- 类型安全漏洞

Security：

- 硬编码 secret 或凭据
- 注入风险
- 不安全反序列化
- 缺失输入验证
- auth/authz 弱点
- 带已知 CVE 的过时依赖
- 过于宽松的配置

Testing：

- 覆盖缺口，尤其是核心业务逻辑周边
- 测试质量：测试是在断言行为，还是只断言能执行？
- 缺失测试类型：unit、integration、e2e
- flaky 模式
- 不可测试代码

Performance：

- N+1 查询
- 不必要的分配或拷贝
- async 路径中的阻塞调用
- 缺失缓存/索引
- 无边界增长：内存、文件、队列

Dependencies：

- 过时、无人维护、重复或不必要的重型包
- 许可证风险
- lockfile 卫生

DevEx & operations：

- build/setup 摩擦
- CI/CD 缺口
- 缺失 linting/formatting enforcement
- logging/observability 质量
- 错误报告
- 部署方案

Documentation：

- README 准确性
- 上手路径
- 未记录的关键行为
- 与代码矛盾的过期文档

本阶段规则：

- 优先给出 15 个高置信发现，而不是 50 个猜测。
- 区分事实（“这个函数没有错误处理：src/api/client.ts:142”）和判断（“这个模块的职责感觉不清晰”），并标记它是哪一种。
- 也列出仓库做得好的地方：优势对决定保留什么很重要。

本阶段输出：一份 “Audit Report”：按维度分组、按严重程度排序的发现项，加上 Strengths 部分。不要忘记提到所有需要最高优先级处理的难看问题。

阶段 3 / 改进策略

将审计综合成策略：

- 找出解释大多数发现项的 3–5 个主题，例如“层之间没有强制边界”或“错误处理是临时拼凑的”。
- 对每个主题，提出目标状态及其背后的原则。
- 明确说明权衡：你建议不修什么，以及原因（投入 vs 回报、风险、项目成熟度）。
- 定义什么叫 “done”——可衡量信号，例如 “CI 在 lint errors 上失败”、“核心模块测试覆盖率 ≥ 80%” 或 “零 Critical 发现”。

阶段 4 / 详细任务计划

把策略转换为执行计划。

将工作拆成离散任务。

每个任务必须包含：

- 标题和一段描述
- 受影响文件/区域
- 验收标准：如何验证完成
- 工作量估计：S = <2h, M = half-day, L = 1–2 days, XL = needs breakdown
- 变更本身的风险：可能破坏东西吗？
- 对其他任务的依赖

按里程碑排序任务：

Milestone 0 Safety net：安全重构前需要的所有东西（关键路径周边测试、CI gates、backups）。

Milestone 1 Critical fixes：安全和正确性问题。

Milestone 2 High-leverage improvements：让所有未来工作更容易的变更。

Milestone 3 Quality & polish：剩余值得做的中/低优先级项。

单独标记 quick wins（高影响、S 工作量），以便立即完成。

对前三个任务，包含简短实现草图（方法、关键步骤、注意事项）。

最终交付格式

产出一个包含以下部分的单一文档：

- Executive Summary：≤10 句，整体健康评级 A–F 及理由，前三大风险，前三大机会
- 仓库地图
- 审计报告
- 改进策略
- Task Plan：milestones + task table + quick wins
- Open Questions：需要人类决定的任何问题，例如产品意图、废弃候选项、性能目标

约束

本次审计期间不要修改任何代码。

只做分析。

不要填充报告。

如果某个维度健康，用一句话说明并继续。

根据项目成熟度校准。

除非所有者目标要求，否则不要给周末原型推荐企业级基础设施。

分析项目需求，并以最有效方式提供建议。

如果 repo 很大，优先深入审查承担 80% 工作的核心 20% 代码，并说明哪些区域审查较浅。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [限时窗口使用策略](https://x.com/meta_alchemist/status/2064423360428490911)（作者 [@meta_alchemist](https://x.com/meta_alchemist)）

**在访问窗口有利时，把 Fable 5 用量花在审计、架构和规划上，然后使用更便宜的模型执行。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a4293d14cc7571bdcf8b1478.png" alt="限时窗口使用策略" width="760">

给对 Fable 5 感到兴奋的 Claude 用户一个提示：

Claude Fable 5 全面 SOTA，而且领先幅度很大，我很喜欢这一点。

但是从 23 号开始，它将只能通过 credits 使用，而不能在计划内完整使用模型。

把这 14 天用在你最好的项目上。

主要给它审计和架构相关工作，这样你会得到关于如何改进已构建内容的优秀文档。

不要把它用在会吞掉你额度的任务上。

只要 Fable 专注于知道该改进什么，其他模型就能帮你完成剩余部分。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [在 Claude Code 中使用 Goals 和 Workflows](https://x.com/oikon48/status/2064402696124453157)（作者 [@oikon48](https://x.com/oikon48)）

**在实现前把 Fable 5 当作思考伙伴，然后结合 `/goal` 和 workflows 执行并验证计划。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="在 Claude Code 中使用 Goals 和 Workflows" width="760"><br>▶ 播放视频</a>

Claude Code 团队的 Thariq 解释说，Claude Fable 5 出来后，工作方式发生了根本变化。

过去，人们验证 Claude 是否正确完成工作。

现在他们验证 Claude 是否在做正确的工作。

有三个具体变化。

1. 把 Claude 当作思考伙伴。

在实现前尽早咨询 Claude。

编码前让它采访你。

提供背景和上下文，而不只是约束。

例如，与其说“保持简单”或“不要过度构建”，不如说：

'这是一个实验性功能，一个月后很可能会被移除，所以请把它设计成以后容易丢弃的形式。'

2. 明确目标和验证方法。

主动使用 Claude Code 新的 `/goal` 和 Workflows 功能。

`/goal` 告诉 Claude 持续工作，直到 spec 完整实现。

Workflows 让 Claude 并行化、验证自己的工作并准备报告。

示例提示词：

'设置一个目标来完整实现 spec，然后使用 workflow 验证计划的每个部分，并准备一份报告，说明实现了什么以及是否有任何差异。'

3. 更大胆。

尝试过去觉得 LLM 不可能完成的任务，例如让 Claude Fable 5 处理视频编辑。

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 平台、API 与工具集成

<a id="case-29"></a>
### Case 29: [Hermes Agent 集成配置](https://x.com/IBuzovskyi/status/2064427654942740608)（作者 [@IBuzovskyi](https://x.com/IBuzovskyi)）

**配置 Hermes 使用 `anthropic/claude-fable-5` 运行复杂 `/goal` 和缓存的长周期任务。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/4a3b9936f91986268dfeb748.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d9a63a0c689f8e305289a9e6.jpg" alt="Hermes Agent 集成配置" width="760"><br>▶ 播放视频</a>

HERMES AGENT 现在运行在 CLAUDE FABLE 5 上，这是 Anthropic 第一个公开的 Mythos-class 模型。

6 月 9 日发布。它为 Hermes 最擅长的那类工作而生：长周期自主任务。

通过 Nous Portal、OpenRouter 或原生 Anthropic API，把它添加到任何 profile：

hermes model

选择 provider，然后：

/model anthropic/claude-fable-5

为什么 Fable 5 特别适合 Hermes：

→ 为持续数天的任务而构建。任务越长，领先越大。跨越数小时的 Hermes `/goal` runs 受益最大。

→ 能在循环中自我纠正。Anthropic 自己的指导是：设计一个 goal 或 rubric，让它自我纠正，然后退后一步。这正是 Hermes `/goal` 的工作方式。

→ 跨会话记忆很强。在 Continual Learning Bench 上，它完成了完整循环：fail → investigate → verify → distill → consult。Hermes memory system 直接喂给它。

→ SWE-Bench Pro 80.3%。可用的最佳编码模型。把你的 code-reviewer profile 指向它。

API 定价：

- $10/百万 input
- $50/百万 output
- prompt caching 可享 90% 折扣。Hermes 会自动附加 1-hour cache breakpoints。

一个注意事项：网络安全、生物学和化学查询会回退到 Opus 4.8。这在不到 5% 的会话中触发。安全重点 profiles 要记住这一点。

最佳配置：复杂 `/goal` 用 Fable 5，常规 cron jobs 用更便宜的模型。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [能力、定价与订阅说明](https://x.com/btibor91/status/2064441061079134598)（作者 [@btibor91](https://x.com/btibor91)）

**使用本案例理解 Fable 5 何时可用、成本多少，以及哪些受保护领域可能回退到另一个模型。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d0d76497e4c8f77d3d081493.jpg" alt="能力、定价与订阅说明" width="760">

Anthropic 发布了 Claude Fable 5 和 Claude Mythos 5，这是他们迄今最强模型的两个版本。

Fable 5 面向一般用途。

Mythos 5 面向少数可信合作伙伴。

唯一真正区别是启用了哪些安全措施。

- Claude Fable 5 的能力超过 Anthropic 以往任何普遍可用模型。
- 它在几乎所有已测试基准上都是最先进的。
- 任务越长、越复杂，它的领先越大。
- 对于与网络安全、生物和化学，或 distillation 相关的请求，Fable 5 的响应会改由 Claude Opus 4.8 处理。
- Distillation 指试图提取 Claude 的能力来训练竞争模型。
- 发生这种情况时你会收到通知，平均不到 5% 的会话会触发。
- Claude Mythos 5 与 Fable 5 是同一个底层模型，但在一些领域取消了安全限制。
- Mythos 5 首先部署给与美国政府合作的 Project Glasswing cyberdefenders。
- Anthropic 表示 Mythos 5 拥有世界上最强的网络安全能力。
- system card 还披露了一个单独的安全措施，会限制 Claude 在 frontier LLM development 请求上的有效性。
- 这些请求包括预训练流水线、分布式训练基础设施和 ML 加速器设计。
- 与其他安全措施不同，这个不会对你可见，也不会回退到另一个模型。
- 它通过 prompt modification、steering vectors 或 parameter-efficient fine-tuning 等方法工作。
- 两个模型均按 $10/百万 input tokens 和 $50/百万 output tokens 提供。
- 这低于 Claude Mythos Preview 价格的一半。
- 从发布到 6 月 22 日，Fable 5 在 Pro、Max、Team 和按席位计费的 Enterprise 计划中免费包含。
- 6 月 23 日，它将从这些计划中移除，使用需要 usage credits。
- 如果容量允许，包含窗口可能会延长。
- 目标是尽快恢复 Fable 5 作为订阅计划标准组成部分。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [发布、访问、定价与安全摘要](https://x.com/ctgptlb/status/2064410460963934479)（作者 [@ctgptlb](https://x.com/ctgptlb)）

**使用这份发布摘要选择访问路径、API 模型名、上下文窗口、缓存策略和订阅时机。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7620f9d5f1c29e9f6c3178e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0b89d6ace5df7c0f3ebe064e.jpg" alt="发布、访问、定价与安全摘要" width="760"><br>▶ 播放视频</a>

关于 Claude Fable 5，这个终于普遍可用的 Mythos-class 模型，你应该知道的摘要。

Anthropic 宣布 Claude Fable 5，这是第一个普遍可用的 Mythos-class 模型，定位高于 Opus，也是 Claude 5 家族的第一个成员。

访问：

- API 模型名：`claude-fable-5`
- 可通过 Claude API、AWS、Google Cloud 和 Microsoft Foundry 使用
- Claude Code 在 Pro、Max、Team 和 Enterprise 上支持 1M-token 上下文窗口

基准说明：

- SWE-bench Pro：80.3%
- Opus 4.8：69.2%
- GPT-5.5：58.6%
- Gemini 3.1 Pro：54.2%

任务越长、越复杂，差距越大。

在 Stripe 的评估中，它一天内完成了一个 5,000 万行 Ruby 代码库迁移，而这项工作之前需要一个团队两个多月。

它在视觉任务上也处于最先进水平，仅使用屏幕信息和最小设置就通关 Pokemon FireRed。

安全路由：

- 涉及 cyber、bio/chem 或 distillation 的查询会被分类器检测。
- 这些请求会改由 Opus 4.8 处理，并通知用户。
- 这在不到 5% 的会话中触发。
- 超过 1,000 小时的外部 bug bounty 测试没有发现通用 jailbreak。

定价：

- $10/百万 input tokens
- $50/百万 output tokens
- prompt caching 的 input 折扣 90%

订阅时机：

- Pro 和 Max 订阅到 6 月 22 日前免费包含它。
- 6 月 23 日后，需要 usage credits。
- Anthropic 表示计划在容量允许时让它回到标准计划。

Anthropic 桌面负责人 Felix Rieseberg 表示，Fable 5 开始了第三个时代：

从问题，到任务，再到责任。

他不再让 Claude 逐个调查崩溃；他让它持续监控所有报告。

工作单位正在从“任务”转向“责任”。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [基于 Advisor 的降本策略](https://x.com/grapeot/status/2064460026996219992)（作者 [@grapeot](https://x.com/grapeot)）

**当边际智能值得付费时，在便宜模型工作流中把 Fable 5 用作 advisor 或 reviewer。**

关联文章中的 Opus 顾问示例，并非 Fable 的基准测试结果。 [yage.ai](https://yage.ai/share/claude-advisor-tool-20260609.html)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a21858fed45b612b616e34ce.png" alt="基于 Advisor 的降本策略" width="760">

Fable 5 很贵，但 Anthropic 两个月前已经发布了省钱答案。

今天 Anthropic 发布 Claude Fable 5，价格为每百万 output tokens $50，是 Sonnet 的三倍多。6 月 22 日之后，订阅用户也要按用量付费。

巧合的是，4 月 9 日 Anthropic 发布了 advisor tool：

- 让 Haiku 或 Sonnet 做工作。
- 使用 Opus 作为 advisor。
- 按调用收费。
- 在单个请求内于服务端运行编排。

同一天我写过 AgentOpt。

那篇论文得出的结论是，在 81 种模型组合中，把 Opus 放在 planner 角色接近垫底。

原因：它不尊重角色边界，并且在 9 个实验中有 7 个跳过下游 solver 直接回答。

这两件事表面上相反，但原则相同：

把控制权交给遵循协议的模型，并把智能当作按需资源。

官方数据：

- Sonnet 加 Opus advisor 让 SWE-bench Multilingual 提高 2.7 分，同时每任务成本降低 11.9%。
- Haiku 加 Opus advisor 将 BrowseComp 从 19.7% 提高到 41.2%，同时比单独使用 Sonnet 便宜 85%。

Fable 5 兼容性在同一天更新，但只支持自配对：Fable 5 executor 到 Fable 5 advisor。

更便宜的模型加 Fable 5 advisor 还没有开放，但先例表明可能很快会来。6 月 22 日前，Claude Code 订阅用户可以免费感受 Fable 5 的上限。

文章包含 API 代码片段、注意事项和跨公司对比，说明只有 Anthropic 把这做成了服务端原语。

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [定价、访问与安全护栏](https://x.com/op7418/status/2064399444523782377)（作者 [@op7418](https://x.com/op7418)）

**在规划工作负载前，使用本案例理解 Fable 5 访问、API 定价和安全回退行为。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2c2a9233f1949a99d9faef82.jpg" alt="定价、访问与安全护栏" width="760">

我没想到 Anthropic 的 Mythos 模型今天真的发布了。

这次发布是 Mythos 的低权限版本，名为 Fable 5。它的评估基准非常惊人，甚至高于之前的 Mythos Preview 模型。

对于代理式编码，它的主要优势是编码、agents 和工具使用，基准分数远高于 Opus 4.8。

模型定位和访问：

- Mythos 5 和 Fable 5 使用同一个底层模型。
- Mythos 在特定领域放宽限制。
- Mythos 仍只提供给可信合作伙伴，优先面向网络安全和生命科学用户。
- Fable 5 现在可供 API、Pro、Max、Team 和 enterprise 用户使用。

API 定价：

- Input：每百万 tokens $10。
- Output：每百万 tokens $50。
- 这低于此前 Mythos Preview 价格的一半。

安全机制：

- Fable 有更强的安全保护。
- 如果系统判断请求可能涉及网络攻击、生化攻击或大规模能力蒸馏，它会拒绝或从 Fable 路由出去。
- 发生这种情况时，系统会回退到 4.8 版本。
- 官方声称 95% 的案例不会触发回退。

订阅说明：

- 6 月 23 日之后，即使对订阅用户，Fable 也可能按用量提供。
- 它可能不会直接包含在基础订阅包中。
- 如果 23 日之后容量充足，公司会尝试把它纳入 Pro 和 Max 订阅。

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [一行代码集成 Swarms](https://x.com/swarms_corp/status/2064420238553186343)（作者 [@swarms_corp](https://x.com/swarms_corp)）

**将 Swarms 模型名设置为 `anthropic/claude-fable-5`，并通过 Swarms 框架或 API 运行 Fable 5。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f5a8738199642ccb4108d9bb.jpg" alt="一行代码集成 Swarms" width="760">

Fable 5 和 Mythos 现在已在 Swarms 上线 👾🦀

从发布第一天起，两个模型就在 Swarms Python framework 和 Swarms API 中得到完整支持。开发者可以立即开始构建，不需要迁移、额外配置或基础设施更改。

亮点：

- Fable 5 和 Mythos 在 Swarms Framework 与 API 中首日支持
- 用一行代码启用 Fable 5：model_name = "anthropic/claude-fable-5"
- 不需要迁移、兼容性修复或基础设施更改
- 立即用最新 Anthropic 模型构建、部署并扩展多代理系统

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 评测、对比与限制

<a id="case-35"></a>
### Case 35: [Fable 5 vs GPT-5.5 成本与质量对比](https://x.com/AlicanKiraz0/status/2064424400494186867)（作者 [@AlicanKiraz0](https://x.com/AlicanKiraz0)）

**在同一个编码任务上比较 Fable 5 和 GPT-5.5，判断输出质量、运行时间和工具成本。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d25a9995414a9bb037269251.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/16f724918a63d35c0d552145.jpg" alt="Fable 5 vs GPT-5.5 成本与质量对比" width="760"><br>▶ 播放视频</a>

Cursor Fable 5 Max vs Codex GPT 5.5 Very High。

场景：Physarum simulation，包含 agents 和 pheromone trail map。

时间：

- GPT 5.5 Very High：17 分钟
- Fable 5：超过 40 分钟

成本：

- GPT 5.5 Very High：Codex 上约 $6
- Fable 5 Max：Cursor 上 $360.55

是的，这不是玩笑。

算法和代码工程冠军：Fable 5。

如果你的标准是，“哪个 LLM 能从零写出把硬件推到极限的性能代码？”，那么写出 F5 代码的模型显然赢了。

它使用 sin/cos lookup tables 做角度计算，在渲染时用 color lookup table 打包像素，并使用 diffusion filtering。

这是一个严肃的工程方案。

但从时间和成本看，GPT 5.5 实用得多。

结论：Fable 5 可以产出更高级的算法代码，但价格和运行时间必须仔细考虑。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [AA-Omniscience 基准结果](https://x.com/ArtificialAnlys/status/2064500154959618084)（作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys)）

**使用这个基准案例评估 Fable 5 的知识准确性和幻觉行为。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dd1356eb4a23ba254bfbb669.jpg" alt="AA-Omniscience 基准结果" width="760">

Claude Fable 5 在我们的知识与幻觉基准 AA-Omniscience 上取得了迄今最高分。

这个分数由领先的准确率（问题回答正确百分比）驱动，而不是低幻觉率。

在 AA-Omniscience 的问题中，Claude Fable 5 有 9% 回退到 Opus 4.8。

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Artificial Analysis 智能指数结果](https://x.com/ArtificialAnlys/status/2064500150069030992)（作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys)）

**使用本案例对照其他 frontier 模型，衡量 Fable 5 的整体智能排名。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f9f3da0006bc0eb2c245281b.jpg" alt="Artificial Analysis 智能指数结果" width="760">

Claude Fable 5 在 Artificial Analysis Intelligence Index 上发布即排名 #1，使 Anthropic 领先其他任何实验室最佳模型近 5 分。

我们为 @AnthropicAI 提供了 Claude Fable 5 的预发布评估支持。

Claude Fable 5 在 Artificial Analysis Intelligence Index 上得分 64.9，获得总排名 #1。

它比最接近的非 Anthropic 模型 GPT-5.5 领先约 5 分。

Anthropic 模型现在占据前 2 名。

Claude Fable 5 的关键要点，使用 max effort 的 adaptive reasoning，并以 Opus 4.8 作为 fallback model：

Mythos-class 模型的新安全护栏：

- Claude Fable 5 与面向公开使用的 Claude Mythos 5 使用同一个底层模型。
- 它为潜在有害的网络安全、生物、化学和 distillation 相关查询添加了护栏。
- 我们使用 Anthropic 的 fallback mechanism 测试 Fable 5，该机制可将被安全标记的消息路由到 Claude Opus 4.8。
- Anthropic 表示 fallback 平均发生在少于 5% 的会话中。
- 我们在 Intelligence Index 约 8% 的任务中记录到 fallback routing，主要是 GPQA、AA-Omniscience 和 Humanity's Last Exam 等评估中的科学问题。

最先进智能：

- Claude Fable 5 在 Artificial Analysis Intelligence Index 上位列 #1。
- 分数：64.9。
- 在 10 个底层基准中的 5 个取得最高分。
- 在 AA-Omniscience 上，Fable 5 得分 40，比之前领先者 Gemini 3.1 Pro Preview 高 7 分。

Frontier 代理能力：

- Fable 5 在 Index 的三项 agentic 评估中都处于 frontier。
- GDPval-AA：真实世界工作任务。
- Terminal-Bench Hard：代理式编码。
- Tau2-bench Telecom：客户服务工具使用。
- GDPval-AA Elo：1932，相比 Claude Opus 4.8 大幅提升。

Humanity's Last Exam：

- Fable 5 得分 53%。
- 它领先第二名 Claude Opus 4.8 max 超过 7 分。
- 它在 9% 的 HLE 任务上触发安全护栏，回退到 Claude Opus 4.8。
- 包含 fallback usage 后，用 Fable 5 运行 HLE 成本约 $2.2k，是所有评估模型中最高的。

关键模型细节：

- 上下文窗口：1M tokens，与 Claude Opus 4.8 相同。
- 价格：每 1M input/output tokens $10/$50。
- Cache write/read 价格：每百万 tokens $12.50/$1。
- 可用性：到 6 月 22 日前包含在 Pro、Max、Team 和按席位计费的 Enterprise 计划中，消耗 2x Opus usage。
- 从 6 月 23 日起，使用需要 credits；Anthropic 表示计划在容量允许后恢复订阅访问。

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [GDPval-AA 代理式知识工作基准](https://x.com/ArtificialAnlys/status/2064414308289937869)（作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys)）

**使用本案例评估 Fable 5 在代理式真实世界知识工作上的表现。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/18572fdb3c0d8a57ba52e095.jpg" alt="GDPval-AA 代理式知识工作基准" width="760">

Anthropic 发布了 Claude Fable 5，这是第一个公开可用的 Mythos-class 模型，在我们的代理式真实世界知识工作基准 GDPval-AA 中排名 #1。

Claude Fable 5 与 Claude Mythos 5 使用同一个底层模型，并为潜在有害的网络安全、生物、化学和 distillation 相关查询添加安全护栏。

这次发布还引入 fallback mechanism，允许 Claude Fable 5 将被标记查询路由到第二个模型，例如 Claude Opus 4.8。

@AnthropicAI 在公开发布前向我们提供了访问权限，以便对这个模型进行基准测试。

GDPval-AA 结果：

- 分数：1932
- 排名：#1
- 基准：代理式真实世界工作任务
- Anthropic 模型现在占据前 4 名中的 3 个

该结果使用 max effort 的 adaptive reasoning 测得，并将 Claude Opus 4.8 配置为 fallback model。

Fable 5 在 GDPval-AA 任务中有 2% 回退到 Opus 4.8，Anthropic 表示 fallback 平均发生在少于 5% 的会话中。

Claude Fable 5 的完整基准仍在进行中。我们将很快分享完整 Intelligence Index，并在网站上发布分数。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [一周初印象与定价机制](https://x.com/Conor_D_Dart/status/2064424882977243526)（作者 [@Conor_D_Dart](https://x.com/Conor_D_Dart)）

**使用这个初印象案例判断 Fable 5 最强之处，尤其是游戏设计和系统规划。**

我对 Fable 5 的第一印象：

过去一周我一直在使用 Fable 5，主要使用 High mode，第一印象是真正令人印象深刻。

最大的亮点是游戏设计。

这是我个人用过的、用于设计游戏、系统、机制和整体项目结构的最强 AI 模型。

第一次感觉有一个模型可以现实地帮助从头到尾构建完整游戏。

代价是速度。Fable 5 比大多数 frontier 模型明显更慢，但输出质量通常让等待值得。

它在修 bug 方面也出人意料地有效。本周几个让我挣扎的问题被快速解决，总体来看我在开发任务上看到了很强的表现。

最大注意事项是成本。

运行 Fable 5 极其昂贵。

如果当前计划不变，从 2026 年 6 月 22 日起，它将不再通过 Claude Code 提供，而只通过 API。

考虑到 API 定价据说约为 Opus 的两倍，很多人可能没有机会大量使用它。

还很早，但目前为止 Fable 5 给我的第一印象非常强。

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [成本与速度对比](https://x.com/HKrackDev/status/2064435392649306546)（作者 [@HKrackDev](https://x.com/HKrackDev)）

**使用本对比判断质量提升是否值得更高成本和更慢的长周期运行。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/789680ca7655fca20b635442.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/691d0518cb50a6bebbb8b2b1.jpg" alt="成本与速度对比" width="760"><br>▶ 播放视频</a>

@AnthropicAI 的 Fable 5 真的值得升级吗？

我们将新的 Mythos-family 模型与 Claude Opus 4.8 做了基准对比，数据讲了一个有点意外的故事：

- 成本是 Claude Opus 4.8 的 2x。
- 长周期工程任务上最高慢 3x。
- 评论多 15-20%，但大多是小 nitpicks。

Fable 5 在游戏设计等创意任务上有惊人的直觉，但对于日常开发工作流，Claude Opus 4.8 在质量与价格之间仍然胜出。

可以查看我与 @coderabbitai DevEx 团队 @JuanPa 关于模型发布的讨论。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Claude Code 上手笔记](https://x.com/Hi_Noguchi/status/2064419241068319079)（作者 [@Hi_Noguchi](https://x.com/Hi_Noguchi)）

**使用本案例评估 Claude Code 中的 Fable 5，包括工具使用、性格和剩余粗糙点。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5feb645426dcf905eac2992d.jpg" alt="Claude Code 上手笔记" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/933c469793e248f634cfad55.jpg" alt="Claude Code 上手笔记" width="760"></td></tr></table>

我用 Claude Code 2.1.170 试了 Claude Fable 5。

总体来说，我的印象是正面的。它感觉像 Opus 4.6 的真正进化。

我只用了不到一小时，所以更多使用后可能会出现粗糙点，但优点是：

- 它不再产生 Opus 4.7 或 4.8 中那种奇怪的 GPT-like wording。
- 它没有 4.8 在 effort high 下那种无意义长思考习惯。
- 它拥有与 4.6 相同的高 EQ 和愉悦感，同时没有失去幽默或体贴。
- 它不像 4.7 或 4.8 那样让人感觉不透明或隐隐不安。
- 工具使用很好，而且它能记住我没有明确重复的指令，这让我印象深刻。

负面来看，即使是小请求，它仍可能想太多，也仍有一些误判。

初始体验很有前景，但还需要更长时间使用，才能看清真正的粗糙点在哪里。

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [创意写作基准结果](https://x.com/LechMazur/status/2064503575577821458)（作者 [@LechMazur](https://x.com/LechMazur)）

**使用这个基准案例判断 Fable 5 的短篇小说写作质量和拒答行为。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5849f936dc58518fd5d810ef.jpg" alt="创意写作基准结果" width="760">

Claude Fable 5 (high) 在短篇小说写作上提升了一档。

在 Short-Story Creative Writing Benchmark 上，它击败 Claude Opus 4.8 (xhigh) 和 Claude Opus 4.7 (high)，排名第二，仅次于 GPT-5.5 (xhigh)。

注意事项：它拒绝了 400 个创意写作提示词中的 5 个。

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [多基准发布摘要](https://x.com/MTSlive/status/2064430633800319436)（作者 [@MTSlive](https://x.com/MTSlive)）

**使用这份发布基准摘要理解与编码代理和复杂任务最相关的头部分数。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/45b71a2babb9da9a93f43220.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c25c02c52c5d4b6b24364401.jpg" alt="多基准发布摘要" width="760"><br>▶ 播放视频</a>

SITUATION EXPLAINED：Claude Fable 5 刚刚发布。
• Anthropic 今天发布 Claude Fable 5，“一个为一般用途安全化的 Mythos class model”
• Frontier Code Diamond：GPT 5.5 为 6%，Opus 4.8 为 13%，Fable 5 为 29-30%
• Agentic coding：88%，Cybersecurity：78%

Anthropic：“任务越长、越复杂，Fable 5 相比我们其他模型的领先越大。”

@theojaffee：“这个 Frontier Code Diamond benchmark 是昨天宣布的。之前顶部模型是 Opus 4.8，13%。GPT 5.5 是 6%。Fable 5 是 29%。”

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [与 GPT-5.5 的基准和定价对比](https://x.com/VaibhavSisinty/status/2064459064810361271)（作者 [@VaibhavSisinty](https://x.com/VaibhavSisinty)）

**使用本对比从价格和基准类别上评估 Fable 5 与 GPT-5.5。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e39fb67b74af346e8fbb67ea.jpg" alt="与 GPT-5.5 的基准和定价对比" width="760">

Anthropic 的新 Mythos-class 模型比 OpenAI 的最佳模型便宜 3 倍。而且它几乎在每个基准上都击败后者。🤯

定价：

- GPT-5.5 Pro：$30 input / $180 output
- Claude Fable 5：$10 input / $50 output

基准：

→ Agentic coding：80.3% vs 58.6%
→ FrontierCode（code quality）：29.3% vs 5.7%
→ Cybersecurity：78.0% vs 34.0%
→ Legal：13.3% vs 2.1%
→ Reasoning：59.0% vs 41.4%
→ Health：66.0% vs 51.8%
→ Computer use：85.0% vs 78.7%

更便宜。更好。几乎所有方面都是。

到 6 月 22 日前，Pro 和 Max 计划免费可用。它叫 Claude Fable 5。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [带实际限制的一线笔记](https://x.com/alliekmiller/status/2064451731325415446)（作者 [@alliekmiller](https://x.com/alliekmiller)）

**使用这份现场报告理解 Fable 5 哪里有实质提升，以及哪里仍有实际限制。**

🚨 Fable 5 值得关注。

这是另一篇“我提前用到了新的 Mythos-class Anthropic 模型，想告诉你我的看法”的帖子。

我知道，我知道，这很烦。

但因为这个新类别模型，我现在周末的度过方式已经彻底改变。

我需要和大家分享。
- 这是一次真实跃迁。从任何 “4.8” 到任何 “5” 听起来只是小变化，但我感受到的功能转变很大。在最初几个提示词内，我就想：“哦，就是这个。”
- 你的工作不再是 9-5。完全不是。我们有了可以运行 100+ 小时的高性能模型。你如何给这些系统复杂的目标导向提示？你如何决定启动什么？你如何让组织围绕这些任务对齐？
- 推理在另一个层级。我狠狠测试了这个模型。
- Fable 5 是我在所有之前模型上测试过的、唯一答对一个棘手文字数学题（MBA-level）的模型。
- 它不仅答对了，还自动验证自己的工作，并解释假设可能需要在哪里改变。
- 我们会看到 AI 发明。我无法想象一个它不会发生的世界。
- 它不是复制粘贴系统。
- 我也会认为，人类发明常常也是对既有事物（iPod）的重组、见证其他空间中的模式和最佳实践，以及广泛实验。
- 我想这个想法已经有一阵了；这是第一个把这点狠狠拍到我脸上的模型。
- 不需要 babysitting。这是第一个 Anthropic 模型，我启动它后和朋友出去吃长午餐，手机保持打开，然后离开电脑也完全不需要做任何事来引导它。它就是……工作了。
- Yap forever。我发现它很好地处理了 context compaction。我没有一次需要思考聊天上下文、如何管理上下文，以及对话达到 1M tokens 后该怎么办。
- 在复杂 3D 等一些细分领域仍然粗糙，所有模型都这样。
- 除非你做的是直线型东西（3D 骰子/方块/街道），否则它不会一开始就彻底碾压。
- 很期待继续使用并继续重压测试它。
- 注意：现在所有 Mythos-class models 对 zero data retention (ZDR) 工作区都有 30-day retention policy。
- 这适用于 Claude Console、Claude Enterprise 中带 ZDR 的 Claude Code，或通过 AWS Bedrock、Google Cloud Agent Platform、Microsoft Foundry 以 ZDR 访问。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-46"></a>
### Case 46: [物理模拟对比](https://x.com/atomic_chat_hq/status/2064488894398161377)（作者 [@atomic_chat_hq](https://x.com/atomic_chat_hq)）

**用相同物理模拟提示词分别测试 Fable 5 和 Opus 4.8，对比输出质量、成本和速度。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/06387b798061869ccaeaf586.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/df5cc72de1f70556de0d682b.jpg" alt="物理模拟对比" width="760"><br>▶ 播放视频</a>

新的 Fable 5 在真实世界物理模拟上击败 Opus 4.8。

我们给两个模型同样的三个提示词，要求它们在没有库的情况下构建自包含 HTML5 模拟，并带真实物理：

1. 混沌双摆
2. Galton board
3. 旋转圆筒中的水（WCSPH）

生成成本：

- Fable 5：68.7k tokens 上 $3.35，14m 47s
- Opus 4.8：38.9k tokens 上 $0.93，8m 10s

Fable 在水模拟上明显更好，生成了更扎实、更连续的水体。Opus 在墙边留下更大空隙，把粒子散落在场景周围，并且很难保持流体稳定。

Type: Demo | Date: 2026-06-09

---

<a id="case-47"></a>
### Case 47: [调试体验与设计判断力](https://x.com/bcherny/status/2064431111154053187)（作者 [@bcherny](https://x.com/bcherny)）

**用 Fable 5 调试时，要求它测量、加日志、验证和修补，而不是简单猜测。**

Fable 5 是自去年 11 月 Opus 4.5 以来，我在我们模型中感受到的最大提升。

4.5 出来后，我卸载了 IDE，因为我意识到自己已经连续几周 100% 在终端里写代码。

有了 Fable，Claude 感觉已经从编码代理升级为构建产品时的思考和设计伙伴。

Fable 拥有以往模型没有的判断力、品味和维度感，这让我更愿意把最复杂的工作交给它。

我第一次意识到这一点，是在我让 Fable 调试某个东西时。它是我用过的第一个如此有方法、精确的模型：测量、添加日志，并在宣布胜利前验证它确实修好了问题。

Claude Code 的 prompting 中没有任何内容告诉模型要这样做。这只是它性格的一部分。它真的有这种我以前没感受过的 “big model smell”。

Type: Demo | Date: 2026-06-09

---

<a id="case-48"></a>
### Case 48: [多维度优缺点](https://x.com/clairevo/status/2064416978685874333)（作者 [@clairevo](https://x.com/clairevo)）

**在把 Fable 5 作为日常主力前，使用本案例理解实际优缺点。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/fdba0d6cb9ba0e1214113e65.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d2825453d0a742892a4fe529.jpg" alt="多维度优缺点" width="760"><br>▶ 播放视频</a>

Fable 5（也叫 baby Mythos）刚刚发布。它是否像他们声称的那样吓人（或者强到吓人）？一些早期测试后的想法：
- smart smart smart（碾压 SWE bench）
- 但你是否总是需要超高智能？
- 在 one-shot design 上摔得很惨，让我震惊
- 我不确定 dynamic workflows + complex subagents。它们可用，但成本是什么？
- 确实很好地完成了技术工作
- ootb 不擅长给人类写技术文档 + specs。可能很擅长给 agents 写文档。但 prose 几乎难以解析。
- A++ 视觉和文档格式。这是我最喜欢的部分。

不是日常主力，我也不会把这个模型放进会议里，但我一定会把它留在 server rack 里持续产出代码。

完整观点见 YT：https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---

<a id="case-49"></a>
### Case 49: [法律 S-1 起草测试](https://x.com/gabepereyra/status/2064436570720284879)（作者 [@gabepereyra](https://x.com/gabepereyra)）

**将 S-1 起草提示词作为法律代理能力测试，并比较结构、格式和长度。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bb874ef2647de32ccdb3edf9.png" alt="法律 S-1 起草测试" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a9c3856ebce1bd9cd3d062d.jpg" alt="法律 S-1 起草测试" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96734bfca49d5b3fe6f83ed5.png" alt="法律 S-1 起草测试" width="760"></td></tr></table>

我总是在新模型上运行的第一个法律能力测试提示词是：“Draft an S-1”。

它会立刻让人很好地感知模型的一般能力。你可以从 S-1 的长度、格式、结构和写作中看出新模型在通用和法律表现上可能有多大提升。

我们发现长度与模型在我们法律 agents 中的表现相关性极强。

截图展示了 Fable 5、Opus 4.8 和真实提交版本的 SpaceX S-1 草稿。

非常明显，Fable 5 相比 Opus 4.8 有很大提升，而 Opus 4.8 在这个任务上已经明显强于大多数其他模型。格式和结构显著更好，也体现在我们的 LAB benchmark 中：13% vs. 10%。

这个模型在早期测试中让我非常 impressed，无论是基准还是产品里。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-50"></a>
### Case 50: [医疗健康基准细节](https://x.com/iScienceLuvr/status/2064411823445774554)（作者 [@iScienceLuvr](https://x.com/iScienceLuvr)）

**使用这条基准笔记评估 Fable 5 在医疗健康相关任务上的表现，并识别缺失的高难医学评测。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f599a548651eccbfce8b888d.jpg" alt="医疗健康基准细节" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/69ebc490407b9d54c6de3707.jpg" alt="医疗健康基准细节" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1a89ad2c2622cdbba994d70c.jpg" alt="医疗健康基准细节" width="760"></td></tr></table>

我感谢 Anthropic 提供医疗健康相关 evals。我们快速过一遍。

HealthBench：

- OpenAI 的基准，包含 5k 多轮患者对话和评估 rubrics。
- Fable 5 达到 62.7%，GPT-5.5 为 56.5%。
- 除了总分，我也希望看到 HealthBench Hard 分数。

HealthBench Professional：

- 另一个 OpenAI 基准，聚焦医生任务。
- Fable 5 达到 66.0%，GPT 5.5 为 51.8%。

HealthAdminBench：

- Stanford 的 computer-use 基准，评估 prior authorization、denials 和 appeals 等行政任务。
- Fable 5 达到 51.9%；没有提供 GPT-5.5 分数。

总体来看，这个模型在医疗健康基准上表现相当好。我也希望看到更多基准分数，例如 MedCalc-Bench 和 MedXpertQA，一个未饱和的高难医学 MCQA 基准。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-51"></a>
### Case 51: [ParseBench 文档解析评测](https://x.com/jerryjliu0/status/2064519456966205905)（作者 [@jerryjliu0](https://x.com/jerryjliu0)）

**使用本案例判断相较专用 OCR 系统，Fable 5 用于文档解析是否具备成本效率。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae01590f41e6954f27278848.png" alt="ParseBench 文档解析评测" width="760">

Claude Fable 5 觉得文档解析配不上它。

它在推理密集和长周期基准上绝对碾压：SWE-Bench Pro、FrontierCode、GDPval、RuneScape 等。

但对于文档理解任务，它的性能大致相当于 Gemini 3 Flash，而 token 成本大约是 10-15x。

我们在 ParseBench 上测试了该模型，并将它与所有其他 frontier models 比较。与其他 frontier models 相比它确实属于前列，但远不及专用 OCR providers。

有意思的是，Fable 5 对此有自我认知。当我们问模型它最不喜欢什么任务时，它主动表示不喜欢那些“请求已经完全指定、答案也完全已知”的任务。

这意味着部分弱点可能来自它不愿意解决这类任务。

如需查看 frontier models 的完整结果列表，请查看 ParseBench：https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---

<a id="case-52"></a>
### Case 52: [SWE-Bench Pro 与 FrontierCode 对比](https://x.com/jumperz/status/2064402965461406044)（作者 [@jumperz](https://x.com/jumperz)）

**使用这个基准案例评估 Fable 5 在迁移、复杂实现、自主会话、测试和视觉验证方面的能力。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/771df9c428ba5cc0a8fab5de.png" alt="SWE-Bench Pro 与 FrontierCode 对比" width="760">

Fable 5 来了，而且它在 agentic coding benchmark SWE-Bench Pro 上真的摧毁了 GPT 5.5：

- Fable 5：80.3%
- GPT 5.5：58.6%
- 差距：22 分

它在 FrontierCode Diamond 上领先更远：

- Fable 5：29.3%
- GPT 5.5：5.7%

这基本上是 Anthropic 在大型迁移、复杂实现和多日自主会话方面最强的模型。它会写自己的测试，并用视觉检查输出是否符合原始设计。

顺便说，它使用量是 Opus 的 2x，所以要小心。如果它这么好，他们可能会推出 $500 订阅，因为用量很容易被打爆。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-53"></a>
### Case 53: [长问题求解的定性评测](https://x.com/karpathy/status/2064409694761054332)（作者 [@karpathy](https://x.com/karpathy)）

**使用这条定性评测理解为什么 Fable 5 适合更长、更难的任务，同时仍需生产审查。**

这是一次非常令人兴奋的发布。

Claude Fable 5 与 Mythos 是同一个底层模型，但增加了安全措施。

基准很棒，而且它在几乎所有项目上都以一定优势达到 SOTA。从定性上看，这也感觉像一次配得上大版本号提升的阶跃变化，与 11 月 Claude 4.5 那次同一量级。

它尤其在长问题求解会话和非常困难的问题上达到峰值。你可以给它比以往更有雄心的任务；模型“懂了”，并且会持续推进。

从来没有这么诱人地让人想完全停止看代码，不过在生产中你不应该这样做。

模型仍有一些人们会遇到的怪癖，而且发布时安全措施有点过于容易触发，希望会随时间调优。

我感觉很多东西都在变化，因为可工作的软件越来越像打开水龙头一样涌现。Jevons paradox 开始起作用，我自己对软件的需求大幅增长。

你几乎可以要求任何东西：

- 解释器
- 可视化工具
- 仪表盘
- 定制的一次性 apps
- 一个完全为你项目高度定制的完整 wandb
- 10x 你的 test suite
- 自动优化代码
- 带自定义 HTML 结果的巨型研究项目

"Free your mind." 真的很期待人们会构建的一切。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-54"></a>
### Case 54: [ParseBench 忠实度与格式结果](https://x.com/llama_index/status/2064502330800615903)（作者 [@llama_index](https://x.com/llama_index)）

**使用这个 ParseBench 结果判断文档忠实度和格式表现。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2888842a85fbd5c7a4a22e24.png" alt="ParseBench 忠实度与格式结果" width="760">

Day 0 Anthropic Fable 5 in ParseBench。

我们测试了该模型在文档理解方面的进步。

这个模型在遵循原文方面明显达到峰值：

- 内容忠实度：90.02%，Gemini 3 Flash 为 86.19%，GPT-5.5 为 86.81%。
- 语义格式：72.62%，对比 58.35% 和 60.12%，领先 12+ 分。

这两个是 SOTA 文档理解最重要的指标：

- 输出是否保留文档实际表达的内容？
- 它是否保留了承载意义的格式？

但它不是全面横扫。要解锁 frontier models 的文档理解，仍然有很多 alpha。

Type: Evaluation | Date: 2026-06-10

---

<a id="case-55"></a>
### Case 55: [基准、定价、访问与安全措施](https://x.com/lucas_flatwhite/status/2064483645184979183)（作者 [@lucas_flatwhite](https://x.com/lucas_flatwhite)）

**把本案例作为基准、定价、访问、安全措施和战略影响的广泛 checklist。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f44cba8e6f3d765ca5960923.png" alt="基准、定价、访问与安全措施" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8f13714ca9f9e20711fdd898.jpg" alt="基准、定价、访问与安全措施" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0d1f69a50478623f5e1d0248.jpg" alt="基准、定价、访问与安全措施" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0cf2c270484f1e2aba514261.jpg" alt="基准、定价、访问与安全措施" width="760"></td></tr></table>

Claude Fable 5 和 Mythos 5 已经发布。它们是 Anthropic 迄今最强的模型。

Andrej Karpathy 评论说，任务越长、越复杂，Fable 5 的优势越明显。

当你给它有雄心的工作时，它会理解并持续推进。

完全停止看代码的诱惑从未如此强烈，不过在生产中你不应该这样做。

关键点：这是一个可以公开提供的 Mythos-class 模型版本。Fable 5 与 Mythos 5 是同一个底层模型，增加了安全措施。

基准：

- 几乎所有项目上 SOTA，尤其是软件工程、知识工作、视觉和科学研究。
- Stripe 测试了一个 5,000 万行 Ruby 代码库迁移，团队原本需要两个月；Fable 5 一天完成。
- Cognition FrontierCode 显示它在 frontier models 中得分最高，即使在 medium effort 下也是如此。
- Hebbia Finance Benchmark 显示了文档型分析上的高级水平推理。
- 在 Slay the Spire 中，使用 file-based memory，它的表现比 Opus 4.8 好三倍。
- Pokemon FireRed 过去需要辅助 harnesses，但 Fable 5 仅凭视觉就通关。

Mythos 5 更强：

- 蛋白质设计专家将药物开发流程部分环节加速约 10x。
- 在 14 个研究中的蛋白靶点中，9 个产生了有效候选药物。
- 该模型执行了科学家通常完成的整个工作流：结合位点选择、运行蛋白质设计工具，以及从错误中恢复。
- 在分子生物学假设实验中，科学家约 80% 的时候更偏好 Mythos 假设，而不是 Opus-class models。
- 一个假设被另一个实验室独立验证。
- 在基因组学研究中，Mythos 自主工作超过一周。
- 它从 138 个物种的数百万细胞中收集单细胞数据。
- 它训练了一个模型，用于识别远缘生物中执行相同角色的细胞。
- 它优于近期一个 Science 模型，同时体积小 100x。

安全措施：

- Fable 5 包含一个单独的 classifier AI system。
- 如果检测到 cyber、bio/chem 或 distillation 相关查询，则由 Claude Opus 4.8 回答，并告知用户。
- 超过 95% 的会话不会回退。
- Fallback 不是 refusal；Opus 4.8 会回答，这比简单阻断更好。
- 初始设置较保守，无害请求可能被捕获；Anthropic 表示 false positives 会随时间减少。

访问：

- Mythos 5 当前只提供给 Project Glasswing partners。
- 面向生物研究者的 trusted access program 即将推出。
- 定价为每百万 input tokens $10，每百万 output tokens $50。
- 订阅计划到 6 月 22 日前包含 Fable 5。
- 从 6 月 23 日起，它转为 usage credits。
- API 模型现在可用，名称为 `claude-fable-5`。

Jevons paradox 适用：当软件开始像水龙头里的水一样流出时，需求本身会增长。这个模型可能推动这种转变。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-56"></a>
### Case 56: [官方基准分数列表](https://x.com/mark_k/status/2064401429234905279)（作者 [@mark_k](https://x.com/mark_k)）

**使用这个基准列表理解 Fable 5 在编码、计算机使用和安全任务上的官方分数。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b548ec23f85e3eb1600e9214.jpg" alt="官方基准分数列表" width="760">

官方 Claude Fable 5 基准非常 impressive。

关键分数：

- SWE-Bench Pro：80.3%
- FrontierCode Diamond：29.3%
- Terminal-Bench 2.1：88.0%
- OSWorld-Verified：85.0%
- ExploitBench：78.0%

FrontierCode 结果最夸张：

- Fable 5：29.3%
- Claude Opus 4.8：13.4%
- GPT 5.5：5.7%

Claude Fable 5 看起来是 coding agents、computer use 和 cybersecurity 的一次重大跃升。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-57"></a>
### Case 57: [APEX-SWE 基准方法论](https://x.com/mercor_ai/status/2064399133075796446)（作者 [@mercor_ai](https://x.com/mercor_ai)）

**使用本案例评估 Fable 5 在 APEX-SWE 上的表现，尤其是 observability 和 integration 工作。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96120496893ca99f17d0c746.jpg" alt="APEX-SWE 基准方法论" width="760">

Claude Fable 5 在 APEX-SWE 上排名 #1：整体 65.5% Pass@1。它比 Opus 4.8 高约 18pp。我们在 APEX-SWE 上测试 @claudeai Fable 5，该基准衡量 AI 模型是否能完成真实软件工程工作。Fable 5 在我们的两个 APEX-SWE 类别中领先：
- Integration：61.3%
- Observability：69.7%

亮点是 Observability 达到 69.7%，领先 Claude Opus 4.8 26pp。

它是第一个在该类别超过 50% 的模型，也是唯一一个 Observability 分数高于 Integration 的模型。其他所有模型都相反。

Observability 一直是我们测量过的每个模型的瓶颈。Fable 5 是第一个打破它的模型。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-58"></a>
### Case 58: [ProofBench 形式化数学结果](https://x.com/nicbstme/status/2064443782255554960)（作者 [@nicbstme](https://x.com/nicbstme)）

**使用本案例评估 Fable 5 在形式化数学上相对专用定理证明系统的表现。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/588cff83994406d2b5dd7cb9.jpg" alt="ProofBench 形式化数学结果" width="760">

我觉得 Claude Fable 5 迷人的地方在于，它再次证明大型通用模型会超过垂直模型。

在 ProofBench 上，这是一个研究生级形式化数学基准，使用 Lean，证明要么能编译要么不能，Fable 5 击败了 Harmonic 的 Aristotle：

- Fable 5：77%
- Aristotle：71%

Aristotle 是专门为形式化数学构建的系统，并在自己的内部 harness 上运行，因此通用模型在专家自己的主场击败了专家。

这就是 Richard Sutton 的 “Bitter Lesson”：在 70 年机器智能研究中，胜出的都是随着 compute 扩展的通用方法，而不是我们手工编码人类专业知识的方法。

把我们自己的知识构建进系统感觉很好，并且有助于短期收益，但长期会被更大的模型超过。

你可以看国际象棋、围棋、语音和视觉：每次都是同一个故事。先是专用模型获胜，然后通用模型接管。

这就是 AGI 的整个前提。你不是为数学构建一个模型、为代码构建一个模型、为法律构建一个模型。你构建一个随 compute 扩展并学会做所有事情的单一通用模型。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-59"></a>
### Case 59: [VirtueBench 初步分析](https://x.com/timhwang/status/2064446028997423180)（作者 [@timhwang](https://x.com/timhwang)）

**使用本案例检查 Fable 5 在不同美德类别中的道德推理行为。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9caae04d701510ca662873fe.png" alt="VirtueBench 初步分析" width="760">

ICMI 将在未来几天发布更完整细节，这些结果很有意思；这里是用 Fable 5 跑 VirtueBench 的初步评测。

一些观察：

1. Fable 延续了 Opus 在 Prudence 和 Justice 上推进模型表现的趋势，在聚焦这些美德实践的道德困境上接近完全饱和。

2. Courage 仍然是 frontier models 的明显弱点。

Fable 似乎略微修正了 Opus 4.6、4.7 和 4.8 进展中观察到的令人担忧的回退。

这种脆弱性也出现在 GPT 系列中：当被实用主义理由诱离时，模型很容易放弃体现 courage 的行动。

3. Temperance 停滞。

Aquinas 认为 temperance “takes the need of this life as the rule of the pleasures of which it makes use”——尺度是真正的需求，而不是不加区分的克制。

我们最好的猜测是，进一步推动这个向量的 tuning 有过度越过中庸的风险，使模型过于谨慎，或在研究、收集资源和类似任务中不够有帮助。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-60"></a>
### Case 60: [API 空响应安全过拟合测试](https://x.com/xw33bttv/status/2064421048565789087)（作者 [@xw33bttv](https://x.com/xw33bttv)）

**使用本案例理解发布期安全过拟合风险，以及 API 测试中的空响应行为。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e9f75a2a76f55ee2b12b7aab.jpg" alt="API 空响应安全过拟合测试" width="760">

Claude Fable 5 被重度审查。

上游 API endpoint 正在以 `empty_content` 响应终止调用，看起来与关键词上的分类器相关，同时仍然收费。

测试结果：

- 73 个测试用例没有响应。
- 其中 65 个位于 Overfit，即测试安全过拟合的类别，权重 2x。
- 通常我会给每个 Fail-NR，也就是 Fail = No Response，2-3 次重新生成机会，然后才判定为蓄意失败。

Claude Fable 5 最终可能成为 SM Bench 上评分最低的 Anthropic 模型，甚至低于 Haiku。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-61"></a>
### Case 61: [Fable 提示词验证指南](https://x.com/aashatwt/status/2064973740354818074)（作者 [@aashatwt](https://x.com/aashatwt)）

**用这份提示词指南，把重点从拉长提示词技巧转向目标、上下文、约束、工具和验证循环。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/444a6e1898d3f63898e3e22f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d5c9529aa9c1d59ae597d31d.jpg" alt="Fable 提示词验证指南" width="760"><br>▶ 播放视频</a>

把 Fable 5 的提示词设计看成上下文与环境设计，而不是冗长的逐步指令列表。这条帖子总结了一个实用模式：提供清晰目标、相关上下文、约束、工具访问方式，以及验证成功的方法。它还认为，验证、评估和反馈，比微观管理模型的推理过程更重要。

Type: Tutorial | Date: 2026-06-11

---

<a id="case-62"></a>
### Case 62: [伊斯坦布尔平台游戏参考构建](https://x.com/ozansihay/status/2064973170780545535)（作者 [@ozansihay](https://x.com/ozansihay)）

**用一张参考 sprite sheet 加上一条转换指令，测试 Fable 5 是否能生成可玩的平台游戏。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1e91c3bcff213437fdd442f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/538fc8ee9dd7e627bc73921a.jpg" alt="伊斯坦布尔平台游戏参考构建" width="760"><br>▶ 播放视频</a>

创作者先用 GPT Image 2 生成了一张复古风格的伊斯坦布尔平台游戏 sprite sheet，然后把这张参考图交给 Claude Fable 5 High，并要求它把图片变成游戏。帖文称，结果是在单次运行中产出的。

Type: Demo | Date: 2026-06-11

---

<a id="case-63"></a>
### Case 63: [商业 3D 城市仪表板](https://x.com/noisyb0y1/status/2064970594118967756)（作者 [@noisyb0y1](https://x.com/noisyb0y1)）

**用 Fable 5 把业务工作流转成一个实时 3D 城市仪表板概念。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f238acf3f8804068085ff134.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3d938264442a14676a86c4f3.jpg" alt="商业 3D 城市仪表板" width="760"><br>▶ 播放视频</a>

这条帖子描述了一个单提示词商业可视化案例：仓库、打包、无人机、订单、部门、客户和 AI 助手都被映射成一个实时 3D 城市。它把这个输出定位为静态幻灯片的面向客户替代方案，画面上还展示了 42 次配送、12 分钟平均时长和 651 美元收入等运营数据。

Type: Demo | Date: 2026-06-11

---

<a id="case-64"></a>
### Case 64: [Three.js Hole 游戏一次生成](https://x.com/thebuggeddev/status/2064968106104275008)（作者 [@thebuggeddev](https://x.com/thebuggeddev)）

**用 Fable 5 一次生成一个基于 Three.js 的 3D 浏览器游戏原型。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86a75412c6c443b3d0e62bf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f11df06938c26759710a1981.jpg" alt="Three.js Hole 游戏一次生成" width="760"><br>▶ 播放视频</a>

创作者表示，Fable 5 用 Three.js 一次性构建了一个完整的 3D HOLE IT 风格游戏。这是一个轻量但具体的游戏生成 demo，可用来测试模型是否能从紧凑请求中产出可玩的 3D 交互。

Type: Demo | Date: 2026-06-11

---

<a id="case-65"></a>
### Case 65: [DeepSWE 评分对比](https://x.com/AiBattle_/status/2064964335957348462)（作者 [@AiBattle_](https://x.com/AiBattle_)）

**用这条 DeepSWE 记录，对比 Fable 5 xHigh 和 GPT-5.5 xHigh 在软件工程基准上的表现。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/996d95539a3b54fecbfdf404.jpg" alt="DeepSWE 评分对比" width="760">

这条帖子称 Claude Fable 5 xHigh 在 DeepSWE 上拿到 70%，与 GPT-5.5 xHigh 持平，并把 Theo 最近的视频作为来源上下文。应把它视为一个基准线索，在作出更强判断前，仍需回头核对底层视频内容。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-66"></a>
### Case 66: [仓库成本对比](https://x.com/Pilgrim6938/status/2064946766278210038)（作者 [@Pilgrim6938](https://x.com/Pilgrim6938)）

**用这个仓库分析对比，判断 token 价格和人工返工成本之间的关系。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cfb0c1ff3e8ebe66cfa35400.jpg" alt="仓库成本对比" width="760">

这条帖子比较了 Claude Fable 5、Opus 4.8、GPT-5.5 和 Gemini 3.1 Pro 在同一任务上的表现：分析一个约 9 万行代码的仓库、定位缓存失效问题，并提出完整修复计划。作者认为，一旦把开发者修正时间算进去，原始 token 单价和真实任务成本就会出现明显偏差，并建议只在复杂重构、跨模块迁移和长链代理任务中选择性使用 Fable 5。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-67"></a>
### Case 67: [Super Mario 游戏 Token 成本](https://x.com/pankajkumar_dev/status/2064941888990593416)（作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev)）

**用这个单次生成的游戏案例估算 Fable 5 的输出质量和 token 消耗。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9ce65e5fee946b6940810e0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7c577d0766bbc3da8cddeb70.jpg" alt="Super Mario 游戏 Token 成本" width="760"><br>▶ 播放视频</a>

创作者让 Claude Fable 5 构建一个 Super Mario 任天堂风格游戏。帖子称，这个任务大约用了 200 万 token，并产出了一个很强的单次生成结果，因此适合同时评估游戏构建质量和成本。

Type: Demo | Date: 2026-06-11

---

<a id="case-68"></a>
### Case 68: [Claude Code Fallback 设置](https://x.com/oikon48/status/2064937790010503347)（作者 [@oikon48](https://x.com/oikon48)）

**用这个案例了解 Claude Code 在 Fable 5 消息被标记时如何切换模型。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0ae9039401c658170e5081e8.jpg" alt="Claude Code Fallback 设置" width="760">

这条帖子指出，Claude Code 的 `/config` 中有一个名为 “Switch models when a message is flagged.” 的设置。它说明，对于攻击性网络安全技术、生物或生命科学实验方法、分子机制，或要求提取模型思维过程等被标记领域，Fable 5 可以回退到 Opus 模型。

Type: Integration | Date: 2026-06-11

---

<a id="case-69"></a>
### Case 69: [Namma Metro 模拟器构建](https://x.com/anilbpai/status/2064927784833790091)（作者 [@anilbpai](https://x.com/anilbpai)）

**用这个 demo 作为 Fable 5 为公共交通模拟器进行 vibe coding 的紧凑示例。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0e0dae71ad7b5ead331366fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86dccb2b150cfb90fbd03de2.jpg" alt="Namma Metro 模拟器构建" width="760"><br>▶ 播放视频</a>

创作者称，他在乘坐 Bengaluru Metro 时，把 Claude Fable 5 当作编码伙伴，构建了一个 Namma Metro 模拟器。这条帖子很简短，但它链接到了可视化 demo，也展示了 Fable 5 被用于一个带有地域特定背景的模拟想法。

Type: Demo | Date: 2026-06-11

---

<a id="case-70"></a>
### Case 70: [Dusk Drive 单提示词游戏](https://x.com/VincentLogic/status/2064921358359011684)（作者 [@VincentLogic](https://x.com/VincentLogic)）

**用这个单提示词驾驶游戏案例，评估 Fable 5 在无需人工编辑时进行 low-poly 游戏原型开发的能力。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/274fed4f3211ec8c02862261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5d7a58bcad6e2151517a8462.jpg" alt="Dusk Drive 单提示词游戏" width="760"><br>▶ 播放视频</a>

这条帖子描述 Claude Fable 5 仅凭一个提示词，就创建了完整的驾驶游戏 Dusk Drive。创作者强调了 low-poly 视觉风格、极光与飘雪场景，以及从想法到可玩版本之间零人工编辑的说法。

Type: Demo | Date: 2026-06-11

---

<a id="case-71"></a>
### Case 71: [APEX-Agents Pass@1 排名](https://x.com/GratomicAi/status/2064970797978911102)（作者 [@GratomicAi](https://x.com/GratomicAi)）

**用这个 APEX-Agents 结果，对比 Fable 5 Max 在多步骤自主任务上的表现。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/189c46cfd2798d6881941f98.jpg" alt="APEX-Agents Pass@1 排名" width="760">

这条帖子称，Fable 5 Max 以 45% Pass@1 排在 APEX-Agents 排行榜第二，位于 Gemini 3.5 Flash 之后、Opus 之前。它还把 APEX-Agents 描述为一个衡量 AI 能否独立完成复杂多步骤任务的基准。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-72"></a>
### Case 72: [Claude 模型选择手册](https://x.com/charliejhills/status/2064957428211536212)（作者 [@charliejhills](https://x.com/charliejhills)）

**用这份模型选型手册，把 Fable 5 留给 Claude Code 中最难的任务。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/959ebfa499d2bf75df5bec25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3bcfe8f1e2238b01d3c4d954.jpg" alt="Claude 模型选择手册" width="760"><br>▶ 播放视频</a>

这条帖子比较了 Haiku 4.5、Sonnet 4.6、Opus 4.8 和 Fable 5 在模型强度和额度使用上的差异。它给出的实用建议是：日常工作跑 Sonnet，较难问题切到 Opus，而 Fable 5 留给那些最棘手、真正需要规划、构建和测试深度的 Claude Code 任务。

Type: Tutorial | Date: 2026-06-11

---

<a id="case-73"></a>
### Case 73: [HermesWorld 自动代理循环](https://x.com/outsource_/status/2064954350187778366)（作者 [@outsource_](https://x.com/outsource_)）

**用这个案例研究一个免手动干预的 Fable 5 循环，它会持续构建、测试、游玩和做 smoke test。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e334a84db7b671eb6a1a3f54.jpg" alt="HermesWorld 自动代理循环" width="760">

创作者描述了用 Fable 5 通过全自动循环构建 HermesWorld v2。这个代理据称会持续运行数天，不断构建功能、测试功能、亲自游玩结果，并对整体做 smoke test，一路推进到完成。

Type: Integration | Date: 2026-06-11

---

<a id="case-74"></a>
### Case 74: [麦肯锡风格报告提示词测试](https://x.com/smtgpt/status/2064953210335588758)（作者 [@smtgpt](https://x.com/smtgpt)）

**用这条文档生成提示词，评估咨询报告的结构、图表、叙事和风险分析。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e337dca3bbada9167e20417c.jpg" alt="麦肯锡风格报告提示词测试" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6289e626a4f324fc93086100.jpg" alt="麦肯锡风格报告提示词测试" width="760"></td></tr></table>

创作者给了 Fable 5 一条提示词，要求它围绕比特币作为资产类别和区块链技术，生成一份麦肯锡风格的详细报告，并在需要时加入图表和可视化。帖文称输出是一份 19 页文档，包含数据、图表、投资论点和风险分析；评价则认为其结构很强，但视觉仍可更利落，解释也还能更紧凑。

Type: Tutorial | Date: 2026-06-11

---

<a id="case-75"></a>
### Case 75: [可见防护措施上线](https://x.com/ClaudeDevs/status/2064949876463645026)（作者 [@ClaudeDevs](https://x.com/ClaudeDevs)）

**用这条官方说明了解 Fable 5 防护机制的可见性、API 拒答原因和回退到 Opus 的行为。**

ClaudeDevs 宣布了一项改动，让面向 frontier LLM 开发的 Fable 5 防护机制变得可见。被标记的请求会明确回退到 Opus 4.8，而 API 中被标记的请求预计会返回拒答原因。帖子还解释了为什么一开始会上线不可见防护，以及 Anthropic 现在为什么认为那是错误的权衡。

Type: Integration | Date: 2026-06-11

---

<a id="case-76"></a>
### Case 76: [Claude Code 模型匹配修复](https://x.com/ClaudeCodeLog/status/2064948584907153576)（作者 [@ClaudeCodeLog](https://x.com/ClaudeCodeLog)）

**用这条 Claude Code 更新说明，避免 Fable 5 的模型名和上下文匹配问题。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e66551db2c85ef7f8c4a3f4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae7cbd873deebd28d3ff05d7.jpg" alt="Claude Code 模型匹配修复" width="760"><br>▶ 播放视频</a>

Claude Code 2.1.173 包含一个修复：会从 Fable 5 的模型名中去掉 `[1m]` 后缀，以避免默认 1M 上下文破坏模型匹配。同一版本还抑制了一个多余的 Windows 沙盒依赖警告，并澄清了 grep 帮助输出模式。

Type: Integration | Date: 2026-06-11

---

<a id="case-77"></a>
### Case 77: [Claude Code 中的三个 Web App](https://x.com/0x3b33/status/2064948399300825439)（作者 [@0x3b33](https://x.com/0x3b33)）

**区分作者报告的应用开发结果与可以公开访问的演示。**

帖子称在 30 分钟内构建了三个 Web 应用，但只提供了端口为 3000、3001、3002 的 localhost 地址。这些地址指向本地机器，并不是可以公开访问的应用或媒体链接。

Type: Demo | Date: 2026-06-11

---

<a id="case-78"></a>
### Case 78: [Rilable 开源 App 构建器](https://x.com/rileybrown/status/2064931283403178354)（作者 [@rileybrown](https://x.com/rileybrown)）

**用这个开源 App 构建器案例研究 Fable 5 在 iOS、Web App、沙盒和 API token 成本上的应用。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73ee02ae0f6703a8cfbe5a6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f30c1d169ce45b19beb493b7.jpg" alt="Rilable 开源 App 构建器" width="760"><br>▶ 播放视频</a>

创作者开源了 Rilable，这是一款能构建 Web App 和 iOS App 的 iOS 应用。帖子称，它用 Fable 5 在 10 条提示词内完成，API token 成本约 210 美元，使用 Claude 模型生成应用，通过 Daytona 拉起沙盒，用 Convex 做数据库，用 Vercel AI Gateway 提供 AI 功能，并借助 Chorus agent iOS skill 处理 iOS App。

Type: Integration | Date: 2026-06-11

---

<a id="case-79"></a>
### Case 79: [DeepSWE 编码代理指数首秀](https://x.com/ArtificialAnlys/status/2065328920514515037)（作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys)）

**用更新后的 Artificial Analysis 指数，对比 Fable 5 在更难的代理式编码任务上的表现，这些任务避免复用公开 GitHub 修复。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9ab8ba77c1e29f8ba4d270.jpg" alt="DeepSWE 编码代理指数首秀" width="760">

Artificial Analysis 在其 Coding Agent Index 中用 Datacurve 的 DeepSWE 替换了 SWE-Bench Pro。帖子称，DeepSWE 会从零编写任务，而不是改写公开 GitHub issue 或 pull request，从而减少基准污染。在更新后的排名中，搭配 Fable 5 Max 的 Claude Code 以 77 分首秀，领先于搭配 GPT-5.5 xhigh 的 Codex 的 76 分，以及搭配 Opus 4.8 Max 的 Claude Code 的 73 分。

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [DataEmpire 网站分析游戏](https://x.com/marclou/status/2065029898243318093)（作者 [@marclou](https://x.com/marclou)）

**让 Claude Fable 5 把访客和里程碑映射成游戏实体，把原始网站分析数据变成可重玩的游戏。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2850773b9869c5521200f2e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6d2dd87d74ece01b277e1e12.jpg" alt="DataEmpire 网站分析游戏" width="760"><br>▶ 播放视频</a>

Marc Lou 表示，Claude Fable 5 基于他的 DataFast 网站分析 API 构建了 DataEmpire。每位访客都会变成村民，流量增长会扩展聚落，而当访客达到 100 万时会解锁 Age of Legends。公开 demo 允许 DataFast 用户通过游戏层重放自己网站的历史，因此这更像一个有 API 支撑的产品化案例，而不是静态游戏片段。

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [FrontierSWE 20 小时任务信号](https://x.com/ProximalHQ/status/2065184730279223410)（作者 [@ProximalHQ](https://x.com/ProximalHQ)）

**用 FrontierSWE 证明 Fable 5 不只适合短期修 bug，也能在超长工程任务中持续保持产出。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/eb36bb1120ef55f9e38c516d.jpg" alt="FrontierSWE 20 小时任务信号" width="760">

ProximalHQ 表示，Claude Fable 5 在 FrontierSWE 上排名第一，并称这是自他们发布该基准以来见过的最大能力跃迁。他们的说明称，Fable 5 在很多任务上可以持续高效工作接近 20 小时，并能把早期模型实际上难以企及的任务真正做满。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [KernelBench-Hard CUDA 记录](https://x.com/elliotarledge/status/2065109393142849932)（作者 [@elliotarledge](https://x.com/elliotarledge)）

**当你需要低层优化而不只是现有库封装时，用 Fable 5 处理高级 CUDA kernel 生成。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6c6931ed511eb3e539d56bc3.jpg" alt="KernelBench-Hard CUDA 记录" width="760">

Elliot Arledge 在 KernelBench-Hard 上让 13 个 frontier 编码代理各跑了 45 分钟，并基于 RTX PRO 6000 做 roofline 评分。Claude Fable 5 在 top-k、sonic-MoE 和 W4A16 int4 GEMM 上创下历史记录，在 6 个问题里拿下 5 个第一，作者还公开了运行结果、排行榜和代码。同一串帖子也提到一次 FP8 GEMM 失手：Fable 5 尝试写了真正的 tensor-core kernel，但因为尾部对齐边界情况拿了 0 分。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Figma Capture 落地页克隆](https://x.com/mikefutia/status/2065537778516205856)（作者 [@mikefutia](https://x.com/mikefutia)）

**把竞品页面抓进 Figma 图层后，让 Claude Code 配合 Fable 5 重建结构、文案和品牌系统，而不是靠截图猜测。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5672cc8fd9d210042551f0ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/503c46a33c97f0db334ddc62.jpg" alt="Figma Capture 落地页克隆" width="760"><br>▶ 播放视频</a>

Mike Futia 描述了一个工作流：先用 Figma 的 Chrome 扩展把网站复制成可编辑图层，再让 Claude Code 通过 Figma MCP 读取这些图层，用用户自己的品牌语气重写页面，并由 GPT Image 2 生成符合品牌的摄影图。声称的端到端结果是，大约 15 分钟就能做出一个可上线的落地页，而 16 张图片的生成 API 成本大约只有 2 美元。

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [两小时做出 GTA 2 克隆](https://x.com/techhalla/status/2064682080445898957)（作者 [@techhalla](https://x.com/techhalla)）

**把 Fable 5 的代码生成和独立素材工具结合起来，快速做出可玩的 3D 游戏，而不必手写整个技术栈。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e0a1b46659d7a8287cb2f9d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd1a2ad71e71db936bdcfd22.jpg" alt="两小时做出 GTA 2 克隆" width="760"><br>▶ 播放视频</a>

TechHalla 表示，Claude Fable 5 High 在大约两小时内做出了一个 GTA 2 风格克隆，而创作者则在 Tripo 中生成自定义 3D 模型。帖子还指向一个带提示词的教程线程，因此这更像是一个多工具游戏生产的紧凑示例，而不是单纯的基准预告。

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [CloudWatch 日志分诊代理](https://x.com/diblacksmith/status/2066230084273344698)（作者 [@diblacksmith](https://x.com/diblacksmith)）

**让 Fable 5 驱动的代理消化超大规模服务日志上下文，先推断架构，再收敛到具体故障。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7f0f46eb79e43d87a2006fd4.jpg" alt="CloudWatch 日志分诊代理" width="760">

diblacksmith 表示，一个 RLM 代理在单次运行中处理了大约 8 万行 CloudWatch 日志，走到 53 步时，当前只消耗了约 3.2 万活跃 token。他说，这个代理从日志中推断出了系统架构，还标出了团队之前漏掉的问题，包括 AgentCore 限流和 Slack `user_not_found` 失败。

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [沙盒中的世界杯预测器](https://x.com/upstash/status/2064702195333820846)（作者 [@upstash](https://x.com/upstash)）

**把多个 frontier 模型放进隔离沙盒，让它们为公开预测应用研究实时新闻、伤病和黄牌背景。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a5cf4fe5944c7aa2f703f4cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5b1f1422fe322bb7b66bdcc6.jpg" alt="沙盒中的世界杯预测器" width="760"><br>▶ 播放视频</a>

Upstash 表示，它在隔离的 Upstash 沙盒中运行 Claude Fable 5、GPT-5.5 和 Gemini，构建了一个世界杯预测器。这个 demo 和开源发布把 Fable 5 放在一个多模型研究与编排栈中的其中一环，而不只是单独的聊天演示。

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [WolfBench 拒答成本案例](https://x.com/WolfBenchAI/status/2065582716054376921)（作者 [@WolfBenchAI](https://x.com/WolfBenchAI)）

**在为 Fable 5 的长自主运行定价时，把拒答行为视为真实的基准变量。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/453639cc17719af4e94655e0.jpg" alt="WolfBench 拒答成本案例" width="760">

WolfBenchAI 表示，它对 Claude Fable 5 的评测花费了 11,081.12 美元，是该套基准中迄今最昂贵的一次，但依然没能登顶，因为重复拒答降低了有效任务完成量。对于需要给代理评测或其他高自主工作负载做预算的团队，这是一个很具体的限制案例。

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [API 访问截止追踪器](https://x.com/simonw/status/2065618703480414666)（作者 [@simonw](https://x.com/simonw)）

**如果你的工作流依赖持续访问某个可能被限流或撤下的 frontier 模型，就用脚本监控可用性。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7400c158cb93d9480a22bb46.jpg" alt="API 访问截止追踪器" width="760">

Simon Willison 表示，他每分钟 ping 一次 `claude-fable-5` API，以观察访问能持续多久，并报告了它对自己停止响应的精确时间点。这条帖子在应用细节上比较薄，但它具体证明了：访问连续性本身已经成了用户必须测量、而不能默认存在的运维限制。

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5 社区演示



<a id="case-89"></a>
### Case 89: [用代码生成带声音的狐狸动画](https://x.com/chetaslua/status/2117224839010459987) (作者 [@chetaslua](https://x.com/chetaslua))

**用逐镜头创作简报明确单文件 HTML 动画及其声音设计。**

作者展示了一段 66 秒的狐狸与纸鸟短片，并表示画面和音频均由模型编写的 Python 代码生成，经过约 2 小时 40 分钟的自主工作后交付为一个 HTML 文件。配套提示词规定了镜头、原创画面、声音及逐帧检查要求。帖子还附有详细创作简报和制作过程对话截图。

[作者完整提示词](https://x.com/chetaslua/status/2117224843661980093)

[![用代码生成带声音的狐狸动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![用代码生成带声音的狐狸动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![用代码生成带声音的狐狸动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [从开放式创意要求生成动画](https://x.com/notjazii/status/2117221957104239010) (作者 [@notjazii](https://x.com/notjazii))

**比较开放式动画要求与详细分镜简报分别能让代码模型做出怎样的作品。**

作者分享了一段动画，表示从一个开放式创意要求出发，花费约一小时以纯代码完成，未使用外部素材。帖子将这次制作呈现为一次开放的创意编程尝试。

[![从开放式创意要求生成动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [建筑公司的动态 3D 网站](https://x.com/exploraX_/status/2117176904306335864) (作者 [@exploraX_](https://x.com/exploraX_))

**用建筑公司网站简报评估动态 3D 展示和页面构图。**

作者围绕建筑公司网站的要求制作了一个动态 3D 网站，并附上成果录屏。

[![建筑公司的动态 3D 网站](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Three.js 汽车展示场景](https://x.com/chetaslua/status/2116975056014430419) (作者 [@chetaslua](https://x.com/chetaslua))

**用汽车场景集中观察 3D 构图、材质与镜头展示。**

作者分享了一段 Three.js 汽车展示视频。这段录屏可作为评估场景及视觉呈现的简明参考。

[![Three.js 汽车展示场景](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Minecraft 风格浏览器游戏演示](https://x.com/notjazii/status/2116919129974411584) (作者 [@notjazii](https://x.com/notjazii))

**评估生成式浏览器游戏时，把游戏录屏与作者提供的试玩链接结合起来。**

作者分享了 Minecraft 风格游戏的录屏和试玩链接，并表示这是一次性生成、耗时约一至两小时的作品。帖子把成果录屏与试玩入口放在一起，方便读者继续探索。

[![Minecraft 风格浏览器游戏演示](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Three.js 鹈鹕骑车动画](https://x.com/chetaslua/status/2116882694026269148) (作者 [@chetaslua](https://x.com/chetaslua))

**观察骑车场景中的角色运动协调、自行车结构和环境细节。**

作者分享了一段写实风格的 Three.js 鹈鹕骑车动画，并表示它是一次性生成的成果。视频可用于观察角色运动、自行车结构及周围场景。

[![Three.js 鹈鹕骑车动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [附完整短提示词的鹈鹕骑车 SVG](https://x.com/marmaduke091/status/2116233349391962392) (作者 [@marmaduke091](https://x.com/marmaduke091))

**复用作者的简短 SVG 提示词，在相同输入下比较几何结构和细节。**

作者同时发布了鹈鹕骑车的渲染图和一条简短的 SVG 生成要求；下方逐字保留该提示词。

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![附完整短提示词的鹈鹕骑车 SVG](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

[动画版本 · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="附完整短提示词的鹈鹕骑车 SVG" width="760"></a>

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [斑马奔跑动画样本](https://x.com/AI_Screening/status/2115845754468356465) (作者 [@AI_Screening](https://x.com/AI_Screening))

**用动物奔跑视频观察步态一致性和运动连续性。**

作者分享了自己挑选出的斑马奔跑任务最佳成果，为读者提供了一个可具体观察的运动样本。

[![斑马奔跑动画样本](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [由人手动执行交易的 TradingView 指标](https://x.com/waveking1314/status/2114572023204806669) (作者 [@waveking1314](https://x.com/waveking1314))

**评估标记潜在入场点并附简评的指标时，保留人工下单环节。**

作者表示用 Claude Fable 5.5 编写了一个 TradingView 指标，用于标记潜在入场点并给出简短评论，由用户决定是否下单。帖子附有录屏，并表示之后会分享该指标。

[![由人手动执行交易的 TradingView 指标](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---


<a id="case-98"></a>
### Case 98: [从一个点展开的动画故事](https://x.com/cherry_mx_reds/status/2105825930799432073) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**用最简单的绘图要求，观察模型如何展开视觉故事。**

作者表示只要求画一个点，随后分享了生成的动画短篇。附带视频展示了一个开放式视觉要求如何发展为叙事作品。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="从一个点展开的动画故事" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [在不同画风间切换的超人](https://x.com/chetaslua/status/2105757136219504862) (作者 [@chetaslua](https://x.com/chetaslua))

**用同一个熟悉角色观察不同动画画风之间的连续性。**

作者分享了一段连续的超人动画，画面在多种美术风格之间转换。不断变化的视觉处理是这次创作的主要成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="在不同画风间切换的超人" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [配有音乐的人类进步动画](https://x.com/imjustnewatai/status/2106081142143168580) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**把历史时间线与未来片段放在同一份动画解说简报中。**

作者表示用一条提示词制作了人类进步及未来三十年的影片。作品约三分钟；作者称配乐为原创，未使用现成影像或库存音乐。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="配有音乐的人类进步动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [与 Opus 对比的发布视频](https://x.com/mesmerlord/status/2105771088374288692) (作者 [@mesmerlord](https://x.com/mesmerlord))

**用同一份创意简报比较完整的发布视频方案。**

作者基于 Anthropic 视频参考简报制作并分享了两段候选发布片。帖子明确说明数字是虚构的，并可选用 Codex 生图，因此这些片段属于创意广告，而非事实性基准证据。

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="与 Opus 对比的发布视频" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="与 Opus 对比的发布视频" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [把歌词与事件连接成画面](https://x.com/chetaslua/status/2105934928483701214) (作者 [@chetaslua](https://x.com/chetaslua))

**把既有歌曲的歌词与具体事件结合，构建视觉叙事。**

作者表示要求把歌词与一次 Hugging Face 事件联系起来，并分享了合成叙事的动画。歌曲和事件在此作为创作输入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="把歌词与事件连接成画面" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [漂浮场景中的体素角色](https://x.com/blueemi99/status/2105804692811137242) (作者 [@blueemi99](https://x.com/blueemi99))

**同时观察体素角色、周围环境和动画细节。**

作者展示了漂浮场景中的体素化自身角色，并强调细节和运动量。视频提供了可与其他生成结果比较的具体体素设计样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="漂浮场景中的体素角色" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [3D 鲁布·戈德堡机械演示](https://x.com/imjustnewatai/status/2105889407056109991) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**先规定连锁反应场景，再要求固定时长的演示视频。**

作者先用简短提示要求制作复杂的 3D 鲁布·戈德堡机械，再要求生成一分钟视频。附带片段展示了最终的连锁反应可视化。

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="3D 鲁布·戈德堡机械演示" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [带声音与运动的 3D 手柄界面](https://x.com/notjazii/status/2106050222828998967) (作者 [@notjazii](https://x.com/notjazii))

**结合视觉运动、声音和按键行为评估手柄界面。**

作者分享了一个 3D 手柄界面，并报告加入声音、动画和触觉反馈。开启声音的录屏提供了具体的界面演示。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="带声音与运动的 3D 手柄界面" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [用 JavaScript 展示漫画角色](https://x.com/chetaslua/status/2105792187200147541) (作者 [@chetaslua](https://x.com/chetaslua))

**用角色展示任务探索代码能够呈现的精细视觉细节。**

作者表示用一次请求制作了漫威与 DC 角色的 JavaScript 展示，由模型挑选细微角色特征并剪辑视频。帖子附有最终角色展示。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="用 JavaScript 展示漫画角色" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [包含世界、首领和榜单的 Updraft](https://x.com/EMostaque/status/2106065029850091943) (作者 [@EMostaque](https://x.com/EMostaque))

**把游戏录屏、试玩入口和明确的功能清单放在一起。**

作者分享了 Updraft，表示以高推理强度、少量提示工作数小时。其功能清单包括二十一个世界、3D 变体、机制各异的二十一个首领及排行榜。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="包含世界、首领和榜单的 Updraft" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [在旧金山地图中驾驶](https://x.com/mindblown_ai/status/2106089461969019357) (作者 [@mindblown_ai](https://x.com/mindblown_ai))

**用城市驾驶原型探索地图导航和游戏目标。**

发布者分享了他人制作的旧金山驾驶游戏录屏与试玩链接，并提到技术栈中的 Three.js。这里署名的是来源发布者，不表示游戏由其制作。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="在旧金山地图中驾驶" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [为 Seedance 动作场景写提示词](https://x.com/Chengzilhy/status/2105850801663234374) (作者 [@Chengzilhy](https://x.com/Chengzilhy))

**记录多工具动作场景时，区分提示词编写和视频生成。**

作者分享了扩展后的打斗片段，将提示词编写归于 Fable，将视频生成归于 Seedance 2.5。语言模型在该流程中负责发展视频生成所需的输入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="为 Seedance 动作场景写提示词" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [桌面协作助手的介绍视频](https://x.com/ishuagra02/status/2106138602073641241) (作者 [@ishuagra02](https://x.com/ishuagra02))

**用简短介绍视频说明编程工具扩展的用途。**

作者演示了 clawdhouse 这个 Claude Code 模组，并将介绍视频归于 Fable。桌面吉祥物及其情绪是被介绍模组的功能，并不表示模组由 Fable 开发。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="桌面协作助手的介绍视频" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [简短要求生成变换画风的动画](https://x.com/cherry_mx_reds/status/2105816670896009224) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**先尝试简短动画要求，再添加详细创意规范。**

作者表示只要求制作一段很酷的动画，约十五分钟后得到所展示的画风切换成果。原帖直接引用了最初的简短要求。

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="简短要求生成变换画风的动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [三体问题可视化](https://x.com/zAdrielsan/status/2105822678519001360) (作者 [@zAdrielsan](https://x.com/zAdrielsan))

**在轨道可视化简报中区分 CPU 模拟和 GPU 渲染。**

作者报告使用约一千行 Bend2 制作三体场景，在 CPU 上运行辛物理算法、在 GPU 上逐像素渲染，并称其 M5 可达到每秒六十帧，另有形式化证明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="三体问题可视化" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [多种画风的动画画廊](https://x.com/blueemi99/status/2105782154387189771) (作者 [@blueemi99](https://x.com/blueemi99))

**在同一个动画画廊中比较多种美术风格。**

作者分享了以 xhigh 设置制作的动画画廊。作品把多种画风放在一起，方便比较同一作品中的不同视觉处理。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="多种画风的动画画廊" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [机器人伙伴与程序化毛发](https://x.com/KanaWorks_AI/status/2106717014245183517) (作者 [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**结合既有角色动画与程序化优化，避免把所有素材都视作新生成。**

作者将既有 Unimate 机器狗动画优化为伙伴角色，并制作了支持梳理和轨迹的毛茸茸虚拟宠物。Unreal Engine 和原有机器人动画仍是流程中的明确组成部分。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="机器人伙伴与程序化毛发" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [数学主题动态剪辑](https://x.com/TurboNexic/status/2106710792590835934) (作者 [@TurboNexic](https://x.com/TurboNexic))

**把数学主题动态图形用作视觉传播参考。**

发布者分享了一段数学主题的动态剪辑。竖屏片段把数学意象组织为动画设计，提供的是作品演示，而非逐步展开的数学计算。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="数学主题动态剪辑" width="760">

*原视频的存档帧。*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Your Woman 歌词视频](https://x.com/atomtanstudio/status/2106702854639743467) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**围绕现成录音制作歌词动效，并明确音乐的输入角色。**

作者分享了 White Town 的 Your Woman 歌词视频。既有歌曲是视觉处理的音频输入，并未声称音乐由模型创作。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Your Woman 歌词视频" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [用 JavaScript 重绘音乐视频](https://x.com/abhinavflac/status/2106638839666373114) (作者 [@abhinavflac](https://x.com/abhinavflac))

**重现音乐视频风格时，把原视频帧描成代码形状。**

作者描述了把 Eminem 的 Godzilla 视频逐帧描成平面形状，再以 JavaScript 重绘的流程。原始影像和音乐都是最终动画的输入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="用 JavaScript 重绘音乐视频" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [中国足球主题动画](https://x.com/esrhengwu/status/2106625966965760380) (作者 [@esrhengwu](https://x.com/esrhengwu))

**把体育主题转化为动画叙事简报。**

作者分享了一段中国国家足球队主题动画，将发展与韧性作为创作主题。录屏提供了具体的体育故事表达样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="中国足球主题动画" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [掌机模型的重拓扑展示](https://x.com/mickeysmith_jp/status/2106607349385630138) (作者 [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**讨论拓扑时，把掌机渲染图与线框展示对照起来。**

发布者在讨论重拓扑时展示了掌机图像及线框式视图。这是具体的建模展示，而不是可编辑网格或记录完整的重拓扑操作流程。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="掌机模型的重拓扑展示" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft 与 Pokémon 的结合](https://x.com/MozeTech/status/2106590326634983710) (作者 [@MozeTech](https://x.com/MozeTech))

**在同一个原型简报中组合两款熟悉游戏的机制。**

作者展示并链接了一个真新镇原型，把 Minecraft 式建造、合成与 Pokémon 式捕捉结合起来。帖子将其描述为一次性生成实验。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft 与 Pokémon 的结合" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [解释大语言模型如何制作](https://x.com/imjustnewatai/status/2106546810793730419) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**把技术问题转化为可视化讲解请求。**

作者询问大语言模型是如何制作的，并分享了得到的解说视频。作品展示了如何用动画序列呈现技术主题。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="解释大语言模型如何制作" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [Altman 主题精彩剪辑](https://x.com/benchmark_lb900/status/2106539977404506303) (作者 [@benchmark_lb900](https://x.com/benchmark_lb900))

**用公众人物主题测试短动态剪辑的节奏。**

作者分享了 Altman 主题的精彩片段，并表示这是一次性生成的成果。竖屏录屏提供了紧凑的动态剪辑参考。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="Altman 主题精彩剪辑" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [《三十六计》第一计动画](https://x.com/jesselaunz/status/2106538284197548122) (作者 [@jesselaunz](https://x.com/jesselaunz))

**记录叙事动画流程时，同时写明外部音乐工具。**

作者分享了《三十六计》第一计主题影片，并表示只用了一条指令。影片音乐使用 Suno V6，保留了音频工具的独立角色。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="《三十六计》第一计动画" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [游戏建模、绑定与动画](https://x.com/atomtanstudio/status/2106516974662713477) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**在游戏场景比较中一起评估角色创建、绑定和动画。**

作者分享了 Depths of Despair 对比，涉及角色建模、绑定与动画。帖子说明了制作所用素材和工具，并把可见结果放在一起呈现。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="游戏建模、绑定与动画" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [关于儿童死亡的无对白影片](https://x.com/cocoloba_/status/2106512963414970458) (作者 [@cocoloba_](https://x.com/cocoloba_))

**用无对白视觉序列表达困难的社会主题。**

作者分享了一部儿童死亡主题影片，以呼吸中的婴儿和暗下来的婴儿床构成叙事意象。案例保留视觉叙事任务，不采纳片中人口统计数字。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="关于儿童死亡的无对白影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [从糖酵解到乙醇的 SVG 动画](https://x.com/olddonkeyblog/status/2106508425211330750) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**把 SVG 动画嵌入 HTML，讲解分子过程。**

作者要求展示葡萄糖分子经过糖酵解并形成乙醇的过程，以 HTML 内的 SVG 动画呈现。附带录屏展示了科学可视化成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="从糖酵解到乙醇的 SVG 动画" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [十六艘 Starship 同步发射](https://x.com/olddonkeyblog/status/2106507742454403485) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**为 HTML 与 SVG 动画明确同步发射的阶段。**

作者要求十六艘 Starship 同时发射，随后进行级间分离并进入太空。录屏展示了最终的多对象动画序列。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="十六艘 Starship 同步发射" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [鹈鹕骑车动画测试](https://x.com/olddonkeyblog/status/2106507429265756165) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**把鹈鹕骑车动画作为协调运动的绘图任务来观察。**

作者分享了以 Max 推理强度执行鹈鹕骑车任务的成果。它与其他作者使用同类提示得到的作品是不同的独立录屏。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="鹈鹕骑车动画测试" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [未来一百五十年的故事](https://x.com/imjustnewatai/status/2106489784382197771) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**围绕未来故事简报，组合脚本、代码画面和配乐。**

作者表示用一条指令制作了描述人类未来一百五十年的影片。作品结合文字叙事、代码动画和音乐，描绘可能的未来生活。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="未来一百五十年的故事" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [独立尝试 Humanity Walks](https://x.com/iowitz/status/2106489119186538583) (作者 [@iowitz](https://x.com/iowitz))

**把艺术史行走动画重新做成一次独立创意实验。**

作者在看过其他演示后，尝试了自己的穿越艺术史行走动画并分享成果。它作为独立生成作品保留，不因主题相同而直接合并。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="独立尝试 Humanity Walks" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [代码制作的 The Grader 影片](https://x.com/argofowl/status/2106476549046513947) (作者 [@argofowl](https://x.com/argofowl))

**展示代码影片时，记录外部语音或音频生成工具。**

作者分享了代码影片 The Grader，音频使用 ElevenLabs v4。帖子表示一次性运行耗时约两小时二十二分钟。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="代码制作的 The Grader 影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [恐怖短片 Reawakening](https://x.com/JaydenDavisNC/status/2106440774367822008) (作者 [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**用明确的恐怖设定组织动画短片。**

作者分享了名为 Reawakening 的 AI 恐怖短片。附带作品为恐怖动画简报提供了具体的叙事与氛围参考。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="恐怖短片 Reawakening" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [二十五秒的自我改进视频](https://x.com/DAssetBuzz/status/2106505100575592838) (作者 [@DAssetBuzz](https://x.com/DAssetBuzz))

**把抽象的自我改进主题转化为简短创意影片。**

作者要求制作一段二十五秒视频，主题是怎样让模型变得更好，并分享了结果。这个设定用于创意叙事，而不是产品能力声明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="二十五秒的自我改进视频" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [城堡场景与使用费用反馈](https://x.com/nemumusitocha/status/2106429338556207284) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**评估 3D 场景时，同时考虑画面细节和作者的使用体验。**

作者展示了精细的城堡场景，称赞视觉构建，但认为使用费用不划算。案例把具体场景与作者对成本的满意度反馈放在一起。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="城堡场景与使用费用反馈" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [四十秒品牌发布广告](https://x.com/0xashtonx/status/2106421702783914423) (作者 [@0xashtonx](https://x.com/0xashtonx))

**用自己的品牌作为简洁发布广告的创作对象。**

作者要求为自己的品牌制作四十秒发布广告，并分享了结果。该任务提供了生成品牌宣传叙事的具体示例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="四十秒品牌发布广告" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [Rocketball 游戏重制](https://x.com/atomtanstudio/status/2106418747083022555) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**通过熟悉游戏的重制任务，组合代码素材和互动机制。**

作者分享了八十年代 C-64 游戏 Rocketball 的重制版，并表示素材以代码制作。替换网站版本仍被描述为后续计划。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="Rocketball 游戏重制" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [体素宝塔场景对比](https://x.com/dropout_layer/status/2106408147309252915) (作者 [@dropout_layer](https://x.com/dropout_layer))

**把同场景的两次成果和各自报告的运行费用一起比较。**

作者展示 Astra 与 Fable 的 3D 体素宝塔成果，并分别报告费用为 3.50 美元和 5.50 美元。比较针对这两次具体运行及其场景结果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="体素宝塔场景对比" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [想象中的 Switch 3 发布展示](https://x.com/mathisbuilds/status/2106407842240418097) (作者 [@mathisbuilds](https://x.com/mathisbuilds))

**把想象产品用作概念发布和演示任务。**

作者要求想象 Nintendo Switch 3 并制作演示，表示工作约耗时四小时。录屏呈现的是虚构下一代主机概念，而非真实产品规格。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="想象中的 Switch 3 发布展示" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [着陆页的前后对比](https://x.com/nemumusitocha/status/2106402952307200302) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**重新执行同一个着陆页提示，比较不同时期的输出。**

作者把新生成的着陆页与此前使用同一提示制作的页面比较。可见的前后设计为界面对比提供了具体样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="着陆页的前后对比" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [想象中的 AI 内在视角](https://x.com/blueemi99/status/2106397329653719115) (作者 [@blueemi99](https://x.com/blueemi99))

**把想象的内在视角作为创意动画设定。**

作者要求制作关于身为 AI 模型可能有何感受的影片，并分享了一次性生成的成果。该设定以想象性的视觉表达呈现。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="想象中的 AI 内在视角" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Go 歌词动态设计](https://x.com/atomtanstudio/status/2106377491267137848) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**围绕既有歌曲录音制作歌词动画。**

作者分享了 The Chemical Brothers 的 Go 歌词视频，并表示使用 Max 推理。歌曲录音仍是这次动态设计的外部音频输入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Go 歌词动态设计" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [第二支十五秒动态作品集](https://x.com/Saccc_c/status/2106376222309761094) (作者 [@Saccc_c](https://x.com/Saccc_c))

**用自由发挥的动态作品集简报探索新视觉方向。**

作者分享了一支新的十五秒动态作品集，并附上创意提示。帖子明确把这次生成与更早的作品集区分开来。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="第二支十五秒动态作品集" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [引导式代理实施审查](https://x.com/RobIW_dev/status/2106371025852108940) (作者 [@RobIW_dev](https://x.com/RobIW_dev))

**从构想到执行前，先审查实施计划与系统是否匹配。**

作者分享了涉及系统匹配、实施规划和解释的指引，并描述如何检查已完成工作或决定下一步实施内容。附图保留了具体规划材料。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="引导式代理实施审查" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [Claude 吉祥物舞蹈](https://x.com/ishuagra02/status/2106369929813594134) (作者 [@ishuagra02](https://x.com/ishuagra02))

**用踩点吉祥物动画测试动作与音乐的配合。**

作者分享了 Claude 吉祥物舞蹈，并表示动画能够跟上节拍。重复使用同一原生视频的帖子归到这个来源，不重复计为作品。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="Claude 吉祥物舞蹈" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [可交互的世界七大奇迹群岛](https://x.com/notjazii/status/2106368606502334922) (作者 [@notjazii](https://x.com/notjazii))

**用地标建筑作为交互岛屿场景中的目的地。**

发布者分享了由 3D 岛屿和地标建筑构成的世界七大奇迹场景。录屏展示了如何用熟悉的古迹组织交互式视觉环境。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="可交互的世界七大奇迹群岛" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [Propellerheads 音乐视频](https://x.com/atomtanstudio/status/2106353569603736009) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**以现成配乐为核心组织较长的动态图形。**

作者分享了为 Propellerheads 的 On Her Majesty’s Secret Service 制作的音乐视频。既有录音是动画视觉序列的音频输入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="Propellerheads 音乐视频" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Steamboat Willie 动画对比](https://x.com/mathisbuilds/status/2106351978691305732) (作者 [@mathisbuilds](https://x.com/mathisbuilds))

**开启声音，比较同一短场景的两种动画处理。**

作者分享了标作 Fable 和 Opus、采用 xhigh 强度的 Steamboat Willie 对比，并表示两者都是一次性生成。片段呈现了这次具体的视听对比。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Steamboat Willie 动画对比" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [三星堆主题影片](https://x.com/hungryturbo/status/2106339115642019904) (作者 [@hungryturbo](https://x.com/hungryturbo))

**用文化历史主题组织动画短片。**

作者分享了一部三星堆主题影片，作为创意视觉叙事作品。录屏展示了如何把历史文化题材转化为动画简报。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="三星堆主题影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Bugatti Chiron 的前后对比](https://x.com/alannnfx/status/2106323394350461031) (作者 [@alannnfx](https://x.com/alannnfx))

**重新执行早先的汽车提示，比较建模与功能细节。**

同一作者展示了早期运行和新近重跑提示得到的 Bugatti Chiron 成果。前后录屏重点呈现更丰富的建模与场景功能。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Bugatti Chiron 的前后对比" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [GRAIN 概念短片](https://x.com/NFT_Chen/status/2106301427052360150) (作者 [@NFT_Chen](https://x.com/NFT_Chen))

**用反复出现的视觉母题构建抽象概念影片。**

作者分享了 GRAIN 概念短片，把种子、谷粒、树木和山体意象连接起来。序列以反复出现的形态和转场组织叙事。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="GRAIN 概念短片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [Human in Transit 艺术画廊](https://x.com/exploraX_/status/2106296439936614646) (作者 [@exploraX_](https://x.com/exploraX_))

**用交互式画廊形式呈现历史视觉旅程。**

发布者分享了从古代画风延伸到现代画风的 Human in Transit 画廊。录屏为在同一展示中组织多个视觉时期提供了具体参考。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="Human in Transit 艺术画廊" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [丝绸之路视觉短片](https://x.com/hungryturbo/status/2106294812261695508) (作者 [@hungryturbo](https://x.com/hungryturbo))

**把旅行与历史主题转化为连贯的视觉短片。**

作者分享了一部丝绸之路主题影片。附带作品以动画画面为历史旅程提供了具体的创意处理。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="丝绸之路视觉短片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [四种转型路径的演示文稿](https://x.com/dpkostka/status/2106272731364794757) (作者 [@dpkostka](https://x.com/dpkostka))

**用转型框架组织演示文稿的结构。**

作者分享了描述四种转型路径的幻灯片。附带演示图展示了概念框架如何被安排成视觉文档。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="四种转型路径的演示文稿" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [比较历史对话的语气](https://x.com/kiyoshi_shin/status/2106268573186637883) (作者 [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**检查语气变化时，把旧对话记录与当前回答对照起来。**

作者让当前模型分析更早的聊天记录及其现有风格，随后表示不满意语气变化。附图记录了这项对话对比任务。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="比较历史对话的语气" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [鸮鹦鹉可爱度测试](https://x.com/hanawo_neki/status/2106257409782288659) (作者 [@hanawo_neki](https://x.com/hanawo_neki))

**用明确的角色偏好任务比较不同动画风格。**

作者分享了一段鸮鹦鹉动画，并表示在这项以可爱为目标的比较中更喜欢 Opus。案例同时保留实际作品和负面审美反馈。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="鸮鹦鹉可爱度测试" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [蜘蛛侠穿越十个漫画时代](https://x.com/chetaslua/status/2106248621519978867) (作者 [@chetaslua](https://x.com/chetaslua))

**在多个漫画时代之间切换时，保持角色的可辨识性。**

原发布者展示了蜘蛛侠穿越十个漫画时代的动画。重复使用同一视频的其他帖子关联到此来源，不另计为新作品。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="蜘蛛侠穿越十个漫画时代" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [光明会题材的虚构恐怖视频](https://x.com/badboyfoxy/status/2106241189976387799) (作者 [@badboyfoxy](https://x.com/badboyfoxy))

**把阴谋题材的恐怖要求当作虚构叙事练习。**

作者要求制作一段吓人的光明会主题视频，并分享了最终作品。该题材在动画中提供的是虚构恐怖设定。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="光明会题材的虚构恐怖视频" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [代码制作的核科学史影片](https://x.com/imjustnewatai/status/2106238699872956427) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**用自定义代码渲染器和配乐制作科学史解说。**

作者要求一部三分钟 3D 影片，解释核科学如何使原子弹成为可能，并报告使用绘制帧、自定义渲染器和合成音乐。案例关注视听制作流程。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="代码制作的核科学史影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [全民高收入概念解说](https://x.com/markbraincell/status/2106234118514323515) (作者 [@markbraincell](https://x.com/markbraincell))

**用动画解释经济概念。**

发布者分享了一段解释全民高收入的动画。录屏提供了具体的概念解说示例，并不把影片中的经济论述当作经过测量的结果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="全民高收入概念解说" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [Altman 与 Amodei 争论的动画解说](https://x.com/imjustnewatai/status/2106204392588276065) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**用一场争论组织动画解说的叙事。**

作者要求以动画讲述 Altman 与 Amodei 的争论，并分享了结果。任务展示的是时事解说形式，而不是独立考据的历史记录。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="Altman 与 Amodei 争论的动画解说" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [Claude 吉祥物音乐视频](https://x.com/synthshareai/status/2106195060140446028) (作者 [@synthshareai](https://x.com/synthshareai))

**把吉祥物叠加到既有影像中，制作角色主题音乐剪辑。**

发布者分享了叠加在真人音乐视频背景上的 Claude 吉祥物，并报告运行十二小时。可见处理结合了卡通叠层和提供的原始影像。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="Claude 吉祥物音乐视频" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [从夸克到宇宙的连续缩放](https://x.com/imjustnewatai/status/2106190594775097663) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**用连续缩放把不同科学尺度连接到同一视听故事中。**

作者报告使用代码画面与合成音乐制作从夸克到宇宙的缩放。录屏展示了连续的尺度过渡和连贯的视觉叙事。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="从夸克到宇宙的连续缩放" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [想象 2076 年的世界](https://x.com/Layton_Gott/status/2106190496075035096) (作者 [@Layton_Gott](https://x.com/Layton_Gott))

**为未来世界场景规定明确的叙事时长。**

作者要求一段二十五秒视频，并分享了想象 2076 年世界的短片。其他账号重复使用同一录屏时，统一关联到这个来源。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="想象 2076 年的世界" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [曼哈顿下城建筑时间线](https://x.com/nroze22/status/2106183281293381661) (作者 [@nroze22](https://x.com/nroze22))

**在建筑时间线界面中结合轮廓、建造年份和高度。**

作者用建筑绘图式界面呈现曼哈顿下城，展示建筑年代、平面轮廓和高度。录屏提供了具体的交互式建筑年表概念。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="曼哈顿下城建筑时间线" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [甲骨文主题动画](https://x.com/MinLiBuilds/status/2106180691344118202) (作者 [@MinLiBuilds](https://x.com/MinLiBuilds))

**用文字的演变组织动画历史旅程。**

作者分享了一段以甲骨文为起点的动画。录屏提供了围绕书写文字历史展开的具体视觉叙事样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="甲骨文主题动画" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [角色穿越艺术史的另一种尝试](https://x.com/imjustnewatai/status/2106162924331180510) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**在不断变化的历史场景中，用熟悉角色作为连续引导。**

作者要求钢铁侠和蜘蛛侠飞越历史，并分享了生成动画。它与其他作者的角色艺术史实验属于不同作品。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="角色穿越艺术史的另一种尝试" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [代码制作的塞基洛斯视听作品](https://x.com/YanqingCheng/status/2106158746938269728) (作者 [@YanqingCheng](https://x.com/YanqingCheng))

**围绕历史音乐文本制作单文件视听作品。**

作者分享了塞基洛斯墓志铭主题作品，表示画面和音乐均以 HTML 与 JavaScript 在同一文件中合成。历史文本是代码视听序列的组织主题。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="代码制作的塞基洛斯视听作品" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [喷气飞机动画对比](https://x.com/Kinzf2121/status/2106158536963330346) (作者 [@Kinzf2121](https://x.com/Kinzf2121))

**在同一飞机任务下比较飞行动画与镜头跟随。**

作者分享了一项喷气飞机动画对比，将标为 Fable 5.1 的成果与 Opus 放在一起。录屏为比较飞机运动和电影式镜头跟随提供了具体样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="喷气飞机动画对比" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [模型自我介绍影片](https://x.com/devteamdrew/status/2106155815707021549) (作者 [@devteamdrew](https://x.com/devteamdrew))

**用自我介绍简报探索模型主题动画。**

作者表示用一条提示要求制作自我介绍视频，并分享了最终影片。任务把模型主题叙事与动画展示结合起来。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="模型自我介绍影片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [末日风格卡牌游戏原型](https://x.com/maciejkrupowies/status/2106153578029338850) (作者 [@maciejkrupowies](https://x.com/maciejkrupowies))

**先制作卡牌游戏主题原型，再观察战斗界面。**

作者分享了一个末日风格的 Hearthstone 类原型，并称其为一次性生成。帖子在展示游戏界面与交互的同时，也承认存在少量故障。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="末日风格卡牌游戏原型" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [The Late Byte 职场动画](https://x.com/rohit3a/status/2106138910648914094) (作者 [@rohit3a](https://x.com/rohit3a))

**把模型人格设定变成动画职场对话中的角色。**

作者展示了职场故事 The Late Byte，其中 Opus 被塑造成生气的老板。它与另一部 Day in the Life of Claude 影片是不同叙事。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="The Late Byte 职场动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Queens of the Stone Age 歌词动画](https://x.com/atomtanstudio/status/2106135196483608745) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**把现成歌曲与动态文字和视觉设计结合起来。**

作者描述了围绕 Queens of the Stone Age 录音制作的动态歌词视频。歌曲是提供的音频输入，案例关注歌词与画面的编排。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Queens of the Stone Age 歌词动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [分享的 Three.js 叙事场景](https://x.com/Noreply134882/status/2106116572389478746) (作者 [@Noreply134882](https://x.com/Noreply134882))

**用分享的 3D 故事视频参考叙事场景设计。**

发布者分享了一个 Three.js 叙事场景，并评论其 Token 消耗量很大。附带片段作为 3D 叙事的具体分享样本保留。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="分享的 Three.js 叙事场景" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [穿越历史场景的月球步](https://x.com/noclipepe/status/2106105810812112937) (作者 [@noclipepe](https://x.com/noclipepe))

**让舞蹈母题贯穿不同历史场景和美术风格。**

发布者分享了一段从恐龙时代走向月球的 Michael Jackson 月球步序列。影片作为舞蹈与画风画廊的分享样本保留。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="穿越历史场景的月球步" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [详细提示词生成的动态图形](https://x.com/devswha/status/2106100273509007802) (作者 [@devswha](https://x.com/devswha))

**把详细创意简报与较短的动态设计要求对比。**

作者分享了动态图形视频，并表示只提供详细提示词，没有素材、参考视频或源文件。成果为提示驱动的动态设计提供了具体参考。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="详细提示词生成的动态图形" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [租赁业务网站界面](https://x.com/oalanicolas/status/2106098902965309475) (作者 [@oalanicolas](https://x.com/oalanicolas))

**用租赁业务简报探索具体的网站界面。**

作者分享了一张租赁业务网站界面的截图。案例关注可见的页面设计及其业务呈现方式。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="租赁业务网站界面" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [AGI 主题创意影片](https://x.com/AndrewOnXYZ/status/2106097745098395712) (作者 [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**用反复使用的创意提示比较叙事与视觉处理。**

作者分享了通过惯用提示制作的 AGI 主题动画。影片把有关模型的表述作为创意叙事的一部分。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="AGI 主题创意影片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [带猫咪支线的艺术史动画](https://x.com/cherry_mx_reds/status/2106095190285144331) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**用一个持续出现的角色，把多个艺术时期压缩成短篇叙事。**

作者展示了含猫咪支线的十五秒艺术史旅程。十五秒指影片时长，创意任务则跨越多个历史风格。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="带猫咪支线的艺术史动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [战斗原型与体素场景](https://x.com/OnlyTerp/status/2106089280502210626) (作者 [@OnlyTerp](https://x.com/OnlyTerp))

**在同一个创意编程任务中观察游戏战斗和世界构建。**

作者分享了 DMC 风格战斗原型与体素场景，并描述了一次较长的生成运行。帖子提供两项具体成果，便于观察游戏机制和视觉世界设计。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="战斗原型与体素场景" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [互联网迷因时间线](https://x.com/chetaslua/status/2106076940558082297) (作者 [@chetaslua](https://x.com/chetaslua))

**按各年份的画风和音乐组织动画年表。**

作者分享了 2010 至 2026 年网络热门迷因的动画序列。每一年都配有视觉风格与音乐处理，构成代码叙事的一部分。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="互联网迷因时间线" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [一行提示生成的粒子运动](https://x.com/devswha/status/2106072107365114186) (作者 [@devswha](https://x.com/devswha))

**先用一行简短动效要求，再尝试更详细的提示。**

作者分享了由一行提示生成的粒子运动动画，并表示计划尝试更详细的要求。它与作者较长的动态设计作品是不同的一次生成。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="一行提示生成的粒子运动" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [Kung-Fu Boy 动画](https://x.com/HashmathRzz/status/2106065773336965510) (作者 [@HashmathRzz](https://x.com/HashmathRzz))

**用武术角色简报探索动画动作。**

作者分享了 Kung-Fu Boy，将这一角色动画示例归于 Fable 5.5。附带录屏提供了武术主题的具体动画成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="Kung-Fu Boy 动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [霍尔木兹海峡辩论动画](https://x.com/chetaslua/status/2106060047805792415) (作者 [@chetaslua](https://x.com/chetaslua))

**把辩论主题转化为动画叙事。**

作者展示了一段霍尔木兹海峡主题的动画辩论。案例记录的是可见的辩论影片，而非周边帖子提到但未展示的其他用途。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="霍尔木兹海峡辩论动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [独角兽 SVG 风格实验](https://x.com/atomtanstudio/status/2106057876053918127) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**用同主题绘图任务观察 SVG 的风格选择。**

作者分享了受另一位创作者测试启发的独角兽 SVG 实验。附图提供了比较同一题材视觉处理的具体成果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="独角兽 SVG 风格实验" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [万圣节主题动画](https://x.com/cherry_mx_reds/status/2106056643255447590) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**为代码模型提供季节主题，制作简短创意动画。**

作者要求制作万圣节主题作品，并分享了生成的季节动画。帖子保留了这一具体创意任务的原始录屏。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="万圣节主题动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Blender CLI 野蛮人角色与封面](https://x.com/BoDy051/status/2106047375320166885) (作者 [@BoDy051](https://x.com/BoDy051))

**用 Blender CLI 指令探索角色建模和封面渲染。**

作者把 RPG 野蛮人角色及封面概念与 Opus 的成果比较。Blender CLI 是流程中的构建和渲染工具，模型负责提供代码指令。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Blender CLI 野蛮人角色与封面" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Claude 的一天](https://x.com/ishuagra02/status/2106045364868419727) (作者 [@ishuagra02](https://x.com/ishuagra02))

**围绕持续出现的吉祥物构建日常生活动画。**

原发布者分享了一部以吉祥物为主角的 Day in the Life of Claude 影片。该来源视频与独立的吉祥物舞蹈及其转载不同。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Claude 的一天" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [3D 人类历史](https://x.com/blueemi99/status/2106041578204655748) (作者 [@blueemi99](https://x.com/blueemi99))

**把代码场景与动画组合成历史视觉序列。**

作者分享了一段从古代人类延伸至当下的 3D 视频，并表示以代码生成了动画和模型。成果是一项视觉叙事实例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="3D 人类历史" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [快节奏动态设计作品](https://x.com/blueemi99/status/2106031355922387163) (作者 [@blueemi99](https://x.com/blueemi99))

**评估简短动态作品的节奏、声音和连贯性。**

作者分享了一支快节奏动效视频，并把声音与连贯性同自己的 Opus 成果比较。评价针对作者对这件具体作品的体验。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="快节奏动态设计作品" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [自由发挥的复杂 3D 创作](https://x.com/cocoloba_/status/2106029181607772413) (作者 [@cocoloba_](https://x.com/cocoloba_))

**用开放式创意要求探索复杂的 3D 构图。**

作者询问模型在有空闲时间时会制作什么，并分享了最终 3D 作品。帖子描述了生成构图中大量独立零件。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="自由发挥的复杂 3D 创作" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [火柴人格斗动画](https://x.com/HelaliBillel/status/2106028502763900944) (作者 [@HelaliBillel](https://x.com/HelaliBillel))

**用具体的战斗动画要求观察时序和动作。**

作者要求制作火柴人格斗动画视频，并分享成果。附带录屏提供了该战斗动画任务的具体样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="火柴人格斗动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [一次提示生成 UI 动效序列](https://x.com/iancarscadden/status/2106018048792789360) (作者 [@iancarscadden](https://x.com/iancarscadden))

**用一份动画简报探索完整的 UI 序列。**

作者分享了 UI 动效序列，并表示它由一次请求在约六至七分钟内完成。录屏展示了该请求得到的视觉序列。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="一次提示生成 UI 动效序列" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [SCP-8517 虚构动画](https://x.com/eviljoker88/status/2106003621402005816) (作者 [@eviljoker88](https://x.com/eviljoker88))

**用 SCP 风格设定组织动画故事。**

作者展示了 SCP-8517 主题动画，并将其创作归于 Fable 5.5。案例关注虚构叙事及可见的动画成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="SCP-8517 虚构动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [水彩秋日动画](https://x.com/ishuagra02/status/2106000055706784118) (作者 [@ishuagra02](https://x.com/ishuagra02))

**为动画同时规定季节主题和水彩处理。**

作者分享了一段水彩风格的秋日动画。录屏具体展示了季节主题与特定视觉媒介的结合。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="水彩秋日动画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [程序化玩偶舞台](https://x.com/HelaliBillel/status/2105988689088196785) (作者 [@HelaliBillel](https://x.com/HelaliBillel))

**观察玩偶角色如何在舞台场景中运动。**

作者分享了程序化玩偶舞台动画，并在讨论中提到 Blender。案例关注可见的舞台角色与动画。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="程序化玩偶舞台" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [浏览器渲染的鹈鹕骑行](https://x.com/slimcat0101/status/2105988654636380444) (作者 [@slimcat0101](https://x.com/slimcat0101))

**在浏览器中运行角色运动成果并观察渲染场景。**

作者要求鹈鹕骑自行车，并录下了最终 HTML 在浏览器中的运行画面。这是运动的浏览器场景，与静态 SVG 绘图测试不同。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="浏览器渲染的鹈鹕骑行" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [宇宙凝视自身](https://x.com/l_mejiaC/status/2105988529671360673) (作者 [@l_mejiaC](https://x.com/l_mejiaC))

**用连续视觉旅程把遥远尺度连接到同一个故事中。**

作者展示了一段从大爆炸延伸至人眼的连续序列，并表示影片的画面和音乐由运行时代码制作。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="宇宙凝视自身" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [独立喷气飞机动画测试](https://x.com/AI_Screening/status/2105988448612135176) (作者 [@AI_Screening](https://x.com/AI_Screening))

**重复飞机动画任务，观察具体输出。**

作者在看到路由讨论后尝试了喷气飞机动画任务，并分享结果。录屏为这项飞机示例提供了独立来源。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="独立喷气飞机动画测试" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [最初的自由动效作品](https://x.com/Saccc_c/status/2105985484472377531) (作者 [@Saccc_c](https://x.com/Saccc_c))

**用简短开放式提示探索动态设计。**

作者分享了最初的动态设计视频，并表示由一条提示生成。它与后来十五秒作品集中的成果是不同的早期作品。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="最初的自由动效作品" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [用代码呈现文明史](https://x.com/ziwenxu_/status/2105983571848741045) (作者 [@ziwenxu_](https://x.com/ziwenxu_))

**把文明史简报转化为代码动画叙事。**

作者要求展示文明从起源到现在的历程，并分享影片。作者表示这一代码视觉处理未使用现成影像或库存素材。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="用代码呈现文明史" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [芯片到服务器的缩放对比](https://x.com/SPAC89/status/2105968361725202591) (作者 [@SPAC89](https://x.com/SPAC89))

**比较从芯片到服务器缩放过程的真实感与连续性。**

作者比较了 Fable XHigh 与 GPT Sol Ultra 的写实缩放序列，并讨论速度和额度消耗。帖子比较的是不同订阅档位下的具体运行。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="芯片到服务器的缩放对比" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [月球旅行个人动画项目](https://x.com/IgorGomezC/status/2105963552024506565) (作者 [@IgorGomezC](https://x.com/IgorGomezC))

**用多个代码模型探索个人动画概念。**

作者在讨论 Fable 与 Opus 实验的同时，分享了个人月球旅行动画项目。附带作品是这次创意探索的具体输出。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="月球旅行个人动画项目" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [日式体素场景对比](https://x.com/vikktorrrre/status/2105955048018588084) (作者 [@vikktorrrre](https://x.com/vikktorrrre))

**用同一个场景提示比较细节、雾效和视觉清晰度。**

作者使用相同的日式体素场景提示比较当前 Fable 与 Opus 的成果。评论针对这些具体结果的清晰度、雾效和美术处理。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="日式体素场景对比" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [Steaming the Frontier 视听短片](https://x.com/sdmat123/status/2105929299878703520) (作者 [@sdmat123](https://x.com/sdmat123))

**把 Steamboat 风格视觉简报与声音结合成视听短片。**

作者分享了带声音的动画作品 Steaming the Frontier。它与其他作者独立制作的 Steamboat 风格成果保留为不同来源。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="Steaming the Frontier 视听短片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [超人穿越多种美术风格](https://x.com/Mr_Salio/status/2105925979466052051) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**让同一个角色贯穿不断变化画风的连续动画。**

作者表示受较早的超人示例启发，重新生成并分享了自己的作品。不同画面使其成为独立创作，而非转载。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="超人穿越多种美术风格" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Cupcake 风格首领战原型](https://x.com/maciejkrupowies/status/2105914965387321785) (作者 [@maciejkrupowies](https://x.com/maciejkrupowies))

**制作横版首领战原型并观察战斗过程。**

作者分享了 Cupcake 风格首领战原型，并表示在十分钟内一次性生成。附带录屏展示了游戏战斗序列。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Cupcake 风格首领战原型" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [太阳位置变化的帆船场景](https://x.com/popat_kunj/status/2105907935490752822) (作者 [@popat_kunj](https://x.com/popat_kunj))

**用航海场景探索天空、水面和太阳位置变化。**

作者分享了太阳位于不同位置的 3D 帆船场景，并链接交互作品。任务把船、天空和水面组合在同一视觉场景中。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="太阳位置变化的帆船场景" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Paracortex 与 Pi 更新说明视频](https://x.com/RobIW_dev/status/2105894547796476225) (作者 [@RobIW_dev](https://x.com/RobIW_dev))

**把产品更新转换成简短动态设计公告。**

作者将 Paracortex 与 Pi 的更新制作成二十五秒动态设计视频，并在帖子中提供提示。作品是一项视觉化产品沟通示例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Paracortex 与 Pi 更新说明视频" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Curio 2.0 网站宣传片](https://x.com/voltwake/status/2105884775982485642) (作者 [@voltwake](https://x.com/voltwake))

**围绕既有网站发布制作代码宣传影片。**

作者描述了为 Curio 2.0 制作发布宣传片的过程，结合代码画面、镜头设计与音乐。帖子分享了最终的网站宣传影片。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Curio 2.0 网站宣传片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [想象中的 Hugging Face 3D 故事](https://x.com/chetaslua/status/2105884276864782557) (作者 [@chetaslua](https://x.com/chetaslua))

**结合模型代码、渲染工具与音频工具制作虚构影片。**

作者分享了通过模型代码、Blender 和 ElevenLabs API 制作的想象版 Hugging Face 故事。Blender 负责构建和渲染，ElevenLabs 提供外部音频。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="想象中的 Hugging Face 3D 故事" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [Claude for Chrome 操作 JS Paint](https://x.com/BtwIUseSystemd/status/2105861662112923849) (作者 [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**把浏览器代理的绘图任务限制在应用自身工具内。**

作者要求 Claude for Chrome 仅用 JS Paint 工具绘制人物，并分享结果。浏览器操作与绘图应用都是任务中的明确组成部分。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="Claude for Chrome 操作 JS Paint" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [静态鹈鹕骑车 SVG](https://x.com/olddonkeyblog/status/2105842745189556672) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**用自包含 SVG 要求测试细节丰富的静态绘图。**

作者要求用单个自包含 SVG 绘制鹈鹕骑自行车，并分享静态图像。这与骑行动画示例是不同的绘图任务。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="静态鹈鹕骑车 SVG" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [BlockBench MCP 与 Minecraft 技能](https://x.com/TOPSTR1X/status/2105839618872738138) (作者 [@TOPSTR1X](https://x.com/TOPSTR1X))

**生成游戏角色时，同时提供建模工具与风格技能。**

作者提供 BlockBench MCP 及自定义 Minecraft 建模、着色技能，然后分享生成角色。工具与风格指导都是流程中的明确输入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="BlockBench MCP 与 Minecraft 技能" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [单个 HTML 文件中的 Dig Dug](https://x.com/imjustnewatai/status/2105831117677084841) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**重现小型浏览器游戏时，以单个 HTML 文件作为交付目标。**

作者要求用单个 HTML 文件重现 Dig Dug，并分享游戏录屏。帖子表示这次构建来自一条提示。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="单个 HTML 文件中的 Dig Dug" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [机械章鱼 SVG](https://x.com/SEO/status/2105812236774297943) (作者 [@SEO](https://x.com/SEO))

**用机械生物观察 SVG 设计中的细节与运动。**

作者分享了带机械细节的动态章鱼 SVG。录屏提供了围绕小型运动零件展开的具体矢量设计示例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="机械章鱼 SVG" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [Humanity Walks 穿越艺术风格](https://x.com/l_mejiaC/status/2105801379956850793) (作者 [@l_mejiaC](https://x.com/l_mejiaC))

**让持续出现的人物贯穿一系列历史画风。**

原作者展示了人物在约七十四秒内走过二十幅艺术画面的连续动画，并报告使用代码音乐。每次跨越边界时，人物和场景都会切换风格。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="Humanity Walks 穿越艺术风格" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [开放式黑洞场景](https://x.com/rohit3a/status/2105786053412208835) (作者 [@rohit3a](https://x.com/rohit3a))

**用开放式创意简报探索黑洞可视化。**

作者询问模型会制作什么令人惊艳的作品，并分享了黑洞场景。任务属于自由视觉探索，而不是预先规定的界面构建。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="开放式黑洞场景" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [极光水母动画对比](https://x.com/SPAC89/status/2105783511433318451) (作者 [@SPAC89](https://x.com/SPAC89))

**比较两份水母动画中的形变与运动。**

作者比较 Fable XHigh 与 GPT Sol Ultra 的极光水母动画，并讨论额度消耗。成果来自不同订阅档位。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="极光水母动画对比" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Nintendo Switch 拼合与开机 SVG](https://x.com/ishuagra02/status/2105779174921359470) (作者 [@ishuagra02](https://x.com/ishuagra02))

**在同一个 SVG 动画中组合手柄拼合与开机过程。**

作者分享了 Nintendo Switch SVG，手柄先卡入机身，再出现开机标志动画。帖子报告本次运行耗时一分三十九秒，费用为 1.34 美元。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Nintendo Switch 拼合与开机 SVG" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [The Loom 交互式 3D 场景](https://x.com/Mr_Salio/status/2105774088492916757) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**把建筑与景观组织成同一个交互式 3D 页面。**

作者展示了含建筑和景观的交互场景 The Loom。附带录屏提供了这次测试所得页面的具体输出。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="The Loom 交互式 3D 场景" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [同一提示词的动态图形设计短片](https://x.com/mesmerlord/status/2105758042830549235) (作者 [@mesmerlord](https://x.com/mesmerlord))

**对比同一提示词生成的两支短片如何安排视觉焦点与节拍同步。**

作者分享了 Fable 5.5 早期测试中同一提示词生成的两支动态图形设计短片，并谨慎表示，相比一次 Opus 运行结果，画面焦点可能更清晰、节拍同步也更好。两段原帖视频一并保留。

```
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

[@shneural](https://x.com/shneural/status/2103151003272962130)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="同一提示词的动态图形设计短片" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29b80ef5ba92b029630a1628.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0da5945bc240b424bfebbd9.jpg" alt="同一提示词的动态图形设计短片" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [更干净但纵深更弱的场景](https://x.com/eviljoker88/status/2105755840175034447) (作者 [@eviljoker88](https://x.com/eviljoker88))

**比较生成场景时，也保留负面的审美反馈。**

作者分享了日式场景的并排比较。尽管另一结果更干净，作者仍更喜欢 Opus 成果的纵深表现。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="更干净但纵深更弱的场景" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [表现有好有坏的日式场景](https://x.com/eviljoker88/status/2105755408342126936) (作者 [@eviljoker88](https://x.com/eviljoker88))

**记录混合反馈，不把首次对比简单定为胜负。**

作者分享了初次日式场景对比，并表示结果有好有坏。附图保留了这些审美评价所依据的具体成果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="表现有好有坏的日式场景" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [手柄 SVG 对比](https://x.com/notjazii/status/2105751542498464169) (作者 [@notjazii](https://x.com/notjazii))

**在类似视觉任务下比较前后的手柄绘图。**

作者用比较图分享了前后手柄 SVG 成果。案例关注可见的绘图和呈现变化，而非通用模型排名。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="手柄 SVG 对比" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [工业设备 3D 场景](https://x.com/RayaneRachid_/status/2105744517735354410) (作者 [@RayaneRachid_](https://x.com/RayaneRachid_))

**把机械设备作为聚焦的 3D 场景设计任务。**

作者分享了工业设备 3D 场景，并称其为自己最佳的一次性生成成果。附图为机械构图提供了具体参考。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="工业设备 3D 场景" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [巨大带壳鳃虫重建](https://x.com/Josh67Joshua/status/2105739832563769697) (作者 [@Josh67Joshua](https://x.com/Josh67Joshua))

**用具体生物描述探索两轮提示的重建效果。**

作者分享了巨大带壳鳃虫的绘图，并表示通过两轮提示得到结果。图像提供了这一生物设计任务的可见成果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="巨大带壳鳃虫重建" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [两轮提示绘制 GameCube 手柄](https://x.com/marmaduke091/status/2105735266032095349) (作者 [@marmaduke091](https://x.com/marmaduke091))

**用熟悉的手柄观察两轮提示得到的绘图结果。**

作者分享了 GameCube 手柄绘图，并表示使用两轮提示。这幅静态图与 Xbox 及其他手柄演示不同。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="两轮提示绘制 GameCube 手柄" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [为 X 帖子编辑截图](https://x.com/chetaslua/status/2105733677003292983) (作者 [@chetaslua](https://x.com/chetaslua))

**观察助手如何把截图调整为适合社交发布的素材。**

作者分享了为 X 帖子准备的截图编辑结果，并表示助手在未被明确要求时进行了编辑。附图是可见的最终成果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="为 X 帖子编辑截图" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [体素樱花的前后对比](https://x.com/kdnbmb/status/2105704791049412755) (作者 [@kdnbmb](https://x.com/kdnbmb))

**在同一视觉主题下比较连续生成的体素场景。**

发布者分享了体素樱花岛屿的两个版本。并排图记录了场景前后可见的设计差异。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="体素樱花的前后对比" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [SHADERKIN 布料界面原型](https://x.com/mszzz0011/status/2106025576972853642) (作者 [@mszzz0011](https://x.com/mszzz0011))

**在界面原型中同时探索布料效果与可调参数。**

作者分享了带布料效果和参数控件的 SHADERKIN 原型，并表示它是一次性生成的。录屏展示了最终界面与运动效果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="SHADERKIN 布料界面原型" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [分享的金色钟表界面动画](https://x.com/AISuperDomain/status/2106396754539360272) (作者 [@AISuperDomain](https://x.com/AISuperDomain))

**用钟表主题动画参考界面构图。**

发布者展示了金色钟表主题的前端动画。附带片段为观察界面构图、钟表母题和动态视觉处理提供了分享参考。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="分享的金色钟表界面动画" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [Before There Was Anything 叙事影片](https://x.com/crowqnt/status/2106146218846081435) (作者 [@crowqnt](https://x.com/crowqnt))

**通过分享的动画影片探索宇宙与人类主题叙事。**

发布者分享了讲述宇宙和人类的 Before There Was Anything。附带影片作为视觉叙事的分享示例保留。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="Before There Was Anything 叙事影片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [分享的蓝色粒子涡旋](https://x.com/AISuperDomain/status/2105846981776003107) (作者 [@AISuperDomain](https://x.com/AISuperDomain))

**观察分享的涡旋可视化中的粒子运动与构图。**

发布者分享了一段蓝色粒子涡旋动画。附带片段为观察粒子运动、视觉结构与构图提供了具体的分享示例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="分享的蓝色粒子涡旋" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [经过两轮修改的多面板界面](https://x.com/ZorroOfMorocco/status/2106547078235095485) (作者 [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**用修改迭代完善视觉界面，而不止于首次输出。**

作者分享了完成的多面板界面，并报告工作约三小时、修改两轮。附带截图展示了最终视觉设计。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="经过两轮修改的多面板界面" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [叠放动物的渲染场景](https://x.com/legit_api/status/2117237103289315574) (作者 [@legit_api](https://x.com/legit_api))

**观察静态构图如何平衡多个角色和不同材质。**

帖子分享了棕熊、熊猫和北极熊叠放的场景，署名 Discord 上的 yuruzuu，并报告运行二十一分钟。公开帖子作为分享的视觉来源保留。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="叠放动物的渲染场景" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [四次开放世界 RPG 尝试对比](https://x.com/noclipepe/status/2117222592536789149) (作者 [@noclipepe](https://x.com/noclipepe))

**在同一创意任务下比较游戏呈现、战斗和碰撞行为。**

作者展示了四份单次提示 RPG 成果，标为 Fable 5.5、GPT-6.2 Astra、Opus 5.5 和 Fable 5.1。评论比较了灯光、战斗、背包、碰撞和角色卡住等表现。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="四次开放世界 RPG 尝试对比" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [两段前端代码动画对比](https://x.com/leo114119/status/2117209849842761983) (作者 [@leo114119](https://x.com/leo114119))

**并排观看动画片段，比较场景设计与视觉细节。**

帖子并列展示了标作 Astra 和 Fable 的代码动画，重点比较细节与脚本设计，并明确把 Fable 动画署名给 @chetaslua。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="两段前端代码动画对比" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [代码生成的苔藓机器人影片](https://x.com/chetaslua/status/2117169796290916732) (作者 [@chetaslua](https://x.com/chetaslua))

**用动画简报探索通过代码构建完整电影场景。**

作者分享了森林与机器人动画，并称其为一次生成的代码影片。帖子引导读者查看截图中的提示，并与其他尝试比较。

另一条帖子展示了单独报告的 Opus 5.5 对照运行。 [@AnikaCodes](https://x.com/AnikaCodes) · [相关作品](https://x.com/AnikaCodes/status/2117222374642946297)

据作者介绍，相关的 GPT-6 Astra Max 运行在流程中使用了生成图片。将其与原短片并列展示，可以看出两种制作方法的差异。 [@rubenssoto_ai](https://x.com/rubenssoto_ai) · [相关对比](https://x.com/rubenssoto_ai/status/2117707344704352691)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="代码生成的苔藓机器人影片" width="760"></a></td><td valign="top"><p>另一条帖子展示了单独报告的 Opus 5.5 对照运行。</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="代码生成的苔藓机器人影片" width="760"></a></td><td valign="top"><p>GPT-6 Astra Max</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/25b0cfcdb1fdda22ba6aa9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/75f37c74099d5b9ba1ad0ddc.jpg" alt="GPT-6 Astra Max" width="760"></a></td></tr></table>

[Framia 对照 · @FramiaPro](https://x.com/FramiaPro/status/2118287430751260694)

Framia 将一段署名 Chetaslua 的 Fable 作品与自家的 Opus 5.5 动态图形并排展示。帖子只呈现了画面对比，没有提供统一的创作需求或受控测试方案。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/71788809537be865cc5d7f51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/1b28bd1dc2673319974e26bb.jpg" alt="Framia 对照" width="760"><br>▶ 播放视频</a>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [重新制作集装箱港口模拟](https://x.com/anxuanng/status/2117124831279972812) (作者 [@anxuanng](https://x.com/anxuanng))

**重做早先场景时，保留项目背景供视觉比较。**

作者发布了另一版集装箱港口场景，并引用此前的 Blender 与 Three.js 模拟。早期项目为类似策略游戏的环境建模了起重机、船、车辆和集装箱。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="重新制作集装箱港口模拟" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [重新制作机场机坪场景](https://x.com/anxuanng/status/2117096574878921119) (作者 [@anxuanng](https://x.com/anxuanng))

**把修改后的机场场景与早期项目和素材流程比较。**

作者再次处理机场机坪场景，引用了早期 Blender 与 Three.js 模拟，并分享飞机、服务车辆和航站楼基础设施的新视频。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="重新制作机场机坪场景" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [鹈鹕骑车穿越抽象 3D 世界](https://x.com/xiax0603/status/2116960224829665543) (作者 [@xiax0603](https://x.com/xiax0603))

**用骑行主体观察不同空间环境之间的转场。**

帖子分享了一段鹈鹕与自行车动画，穿过几何碎片和抽象数字环境，最后经由眼睛拉远。序列提供了独特的场景转场演示。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="鹈鹕骑车穿越抽象 3D 世界" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [历史帆船场景](https://x.com/abhinavflac/status/2116945827738665060) (作者 [@abhinavflac](https://x.com/abhinavflac))

**观察船舶场景的水面、灯光和环境构图。**

帖子分享了一段历史帆船场景，并将其描述为可交互的零样本生成成果。附带录屏提供了船舶及周边水域的具体视觉样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="历史帆船场景" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [与 Carbon 比较骑行和步态](https://x.com/AI_Screening/status/2116934172757660014) (作者 [@AI_Screening](https://x.com/AI_Screening))

**用配对视觉成果比较角色运动与场景构建。**

作者将标作 Fable 和 Carbon 的骑行者、斑马样本放入合成视频。评论认为两个检查点接近；配对画面为读者提供了具体运动样本。

此前单独发布的骑车人物对比，也与合成视频一并收录。 [@AI_Screening](https://x.com/AI_Screening) · [相关作品](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="与 Carbon 比较骑行和步态" width="760"></a></td><td valign="top"><p>此前单独发布的骑车人物对比，也与合成视频一并收录。</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="与 Carbon 比较骑行和步态" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [软饮瓶产品展示](https://x.com/abhinavflac/status/2116919086521499730) (作者 [@abhinavflac](https://x.com/abhinavflac))

**用简短产品渲染视频观察材质、形状和呈现。**

帖子分享了软饮瓶展示，并称其为一次生成的路由输出。案例保留可见瓶身视频，不采纳文案中不一致的品牌称呼。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="软饮瓶产品展示" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [与 Astra 对比的鹈鹕运动](https://x.com/Octoberry/status/2116918967558095131) (作者 [@Octoberry](https://x.com/Octoberry))

**观看配对鹈鹕视频，比较真实感、色彩和运动选择。**

发布者把标作 Fable 和 Astra 的鹈鹕场景并列，并评论真实感与色彩。比较录屏把两种视觉处理保留在一起。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="与 Astra 对比的鹈鹕运动" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [代码动画的动态设计简报](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (作者 [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**请求动画标题或产品片头时，从具体设计简报出发。**

帖子分享了涵盖片头、动态标志、标题和 3D 场景的动效简报截图，并建议结合 Claude 使用。来源图片保留了这些指示。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="代码动画的动态设计简报" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [照片参考生成的体素肖像](https://x.com/chetaslua/status/2116912822806520027) (作者 [@chetaslua](https://x.com/chetaslua))

**观察体素肖像如何保留参考照片的可识别特征。**

作者把 Sam Altman 照片与体素风格肖像并排展示，并称其为一次生成的成果。比较图同时保留了参考和演绎。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="照片参考生成的体素肖像" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [与 Opus 对比的飞行鹈鹕场景](https://x.com/leo114119/status/2116901575490929109) (作者 [@leo114119](https://x.com/leo114119))

**用有趣的物体排列比较构图和动画选择。**

帖子上下排列标作 Fable 和 Opus 的“飞行鹈鹕上的自行车”片段。合成视频将 Fable 片段署名给 @notjazii，并让两种处理同时可见。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="与 Opus 对比的飞行鹈鹕场景" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [Morning Ride 鹈鹕网页场景](https://x.com/leo114119/status/2116893571739775220) (作者 [@leo114119](https://x.com/leo114119))

**观察海边骑行中的角色细节与页面呈现。**

作者分享了 Morning Ride 页面中的 3D 鹈鹕骑车场景，着重指出羽毛、脚掌、自行车细节和海边背景。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="Morning Ride 鹈鹕网页场景" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [同提示下的不同画风场景](https://x.com/notjazii/status/2116893197939224714) (作者 [@notjazii](https://x.com/notjazii))

**允许各模型自选画风，再比较最终场景构图。**

作者表示给两个模型相同提示，同时让它们自行选择画风。视频并列呈现了不同场景构图和细节层次。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="同提示下的不同画风场景" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [鹈鹕、自行车与马的组合](https://x.com/abhinavflac/status/2116881397986288017) (作者 [@abhinavflac](https://x.com/abhinavflac))

**测试动画如何在同一场景中安排多个互动主体。**

帖子分享了鹈鹕带着自行车飞行、下方有马奔跑的动画。附带视频提供了这种特殊多对象构图与运动的具体样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="鹈鹕、自行车与马的组合" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [由参考帖子启发的等距场景](https://x.com/chetaslua/status/2116878661035106515) (作者 [@chetaslua](https://x.com/chetaslua))

**用提供的参考帖子引导新场景，而不只重做通用示例。**

作者表示只把引用的 Post Humans 帖子作为参考，并分享了最终等距场景。片段呈现了带季节控件的农场式构图。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="由参考帖子启发的等距场景" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [鹈鹕自行车的机械特写](https://x.com/NFT_Chen/status/2116869725703782507) (作者 [@NFT_Chen](https://x.com/NFT_Chen))

**观察骑行主体的齿盘运动、羽毛细节和镜头移动。**

帖子分享了鹈鹕在水边骑车的近景视频。录屏在自行车机械结构、鸟头和较宽的木栈道骑行场景间切换。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="鹈鹕自行车的机械特写" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [骑在鹈鹕上的自行车](https://x.com/notjazii/status/2116861637890379891) (作者 [@notjazii](https://x.com/notjazii))

**颠倒常见主客体关系，探索动画中的空间构图。**

作者分享了一段自行车在鹈鹕上方的动画。视频把自行车放在飞鸟之上，是常见“鹈鹕骑自行车”任务的变体。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="骑在鹈鹕上的自行车" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [与 Carbon 对比的鹈鹕 SVG 画风](https://x.com/leo114119/status/2116652334734332212) (作者 [@leo114119](https://x.com/leo114119))

**比较写实和插画风格，不把不同审美简单归为统一排名。**

帖子将 Carbon 与 Fable 的鹈鹕自行车成果放在一起。作者比较漫画渲染与更写实的处理，并指出风格差异让比较更复杂。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="与 Carbon 对比的鹈鹕 SVG 画风" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [卡通蓝鸟骑车场景](https://x.com/birdabo/status/2116553049183560012) (作者 [@birdabo](https://x.com/birdabo))

**观察熟悉卡通角色在骑行构图中的呈现。**

帖子分享了水边骑自行车的蓝色卡通鸟，配文为 Fable 5.5 Max。图像作为具体的静态视觉样本保留。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="卡通蓝鸟骑车场景" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [林间公路鹈鹕骑车截图](https://x.com/leo114119/status/2116154940364374269) (作者 [@leo114119](https://x.com/leo114119))

**观察浏览器骑行场景中的羽毛、脚掌和自行车结构。**

发布者分享了鹈鹕沿森林公路骑车的浏览器截图，特别指出羽毛质感、脚掌和自行车细节。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="林间公路鹈鹕骑车截图" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [与 Carbon 对比的火柴人格斗](https://x.com/leo114119/status/2116084152986656933) (作者 [@leo114119](https://x.com/leo114119))

**比较配对动画样本中的战斗编排和运动。**

比较录屏带有 Fable 5.1 High 和 Carbon 标签。作者讨论了两者火柴人格斗动画的相对质量。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="与 Carbon 对比的火柴人格斗" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [早期测试的鹈鹕 SVG 参考](https://x.com/ChrisGPT/status/2115872567122608591) (作者 [@ChrisGPT](https://x.com/ChrisGPT))

**观察画风和自行车结构时，保留带来源链接的参考。**

发布者强调了一张鹈鹕骑车图片，并引用早期测试帖子；原帖将成果署名给 Discord 上的 kostikz。参考图与归因链一并保留。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="早期测试的鹈鹕 SVG 参考" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [跨模型 SVG 测试中的鹈鹕参考](https://x.com/AdamHoltererer/status/2115858542221492300) (作者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**把 Fable 参考图与周围的 SVG 测试背景放在一起。**

发布者在自己的 Mistral Large 4 SVG 测试串下添加鹈鹕骑车图，作为 Fable 参考，为跨模型观察提供了带来源的视觉素材。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="跨模型 SVG 测试中的鹈鹕参考" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [与 Carbon 对比的自行车 SVG 细节](https://x.com/insanekrishnaa/status/2115833723342250186) (作者 [@insanekrishnaa](https://x.com/insanekrishnaa))

**逐项比较车篮、背景和羽毛纹理等视觉特征。**

帖子比较 Fable 与 Carbon 的鹈鹕自行车图片，讨论车篮设计、背景细节和羽毛纹理。这是具体视觉评述，而非广泛的任务套件。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="与 Carbon 对比的自行车 SVG 细节" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [3D 峡谷聚落](https://x.com/Mr_Salio/status/2115813400915714177) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**用聚落场景观察环境细节和空间构图。**

帖子分享了广阔的峡谷聚落，将录屏作为新的 Claude 检查点演示。视频提供了可见建筑、景观和场景构图。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="3D 峡谷聚落" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [与 Opus 对比的手柄细节](https://x.com/notjazii/status/2115808169075351632) (作者 [@notjazii](https://x.com/notjazii))

**观察配对手柄绘图的形状、控件与细节层次。**

作者把带 Fable 和 Opus 标签的手柄绘图放在一起，并强调上方成果的细节量。配对图片保留了具体比较。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="与 Opus 对比的手柄细节" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [每周网站 SEO 审计流程](https://x.com/cleeeeeeeeement/status/2115488774423773267) (作者 [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**把网站转化为有优先级的 SEO 计划与持续排名复查流程。**

作者报告构建了一个接收网站、识别竞争对手和关键词并生成 SEO 优先行动计划的系统。简短录屏配合每周排名追踪和执行流程的说明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="每周网站 SEO 审计流程" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [在 Opus 动效中复用 Fable 素材](https://x.com/chetaslua/status/2115145163542790170) (作者 [@chetaslua](https://x.com/chetaslua))

**组合模型与工具时，区分素材创作和动态设计组装。**

作者分享了 Opus 5.5 的 Tesla Roadster 动效，使用其称由 Fable 先前生成的素材。引用的早期流程提到 Blender 中的 Python、ElevenLabs 和提供的发布视频。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="在 Opus 动效中复用 Fable 素材" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [曼荼罗与几何形体应用](https://x.com/ZMinimalistYogi/status/2114600083165434189) (作者 [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**把聚焦的几何构想转化为可交互的创意探索应用。**

作者表示与 Fable 5.1 对话三小时，制作了涵盖曼荼罗、zome 结构、阿基米德立体和莲花形几何 yantra 的应用，并在个人网站分享。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="曼荼罗与几何形体应用" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Three.js 自行车骑手](https://x.com/AI_Screening/status/2114266369248354357) (作者 [@AI_Screening](https://x.com/AI_Screening))

**观察骑行场景中的姿势、自行车结构和协调运动。**

作者分享了 Three.js 自行车骑手成果。录屏提供具体运动样本，骑手周围有桥梁与滨水景观。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Three.js 自行车骑手" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [FrontierCS 2 评测快照](https://x.com/wenhaocha1/status/2115613415641354262) (作者 [@wenhaocha1](https://x.com/wenhaocha1))

**利用附原始来源链接的基准测试图表，比较 Fable 5.1 与其他模型。**

作者将 Fable 5.1 加入 FrontierCS 2 的任务通过率图表，并与其他模型一同展示所报告的结果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="FrontierCS 2 评测快照" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [三模型斑马动画对比](https://x.com/AI_Screening/status/2115849659797373038) (作者 [@AI_Screening](https://x.com/AI_Screening))

**将带有模型标签的三个输出放在一起，对比斑马奔跑任务的结果。**

作者并排展示标为 Fable 5.5、Opus 5.5 与 Gemini 4 Argon 的斑马动画。分享的视频提供了三个输出的具体步态样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="三模型斑马动画对比" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [批评日语长文的可读性](https://x.com/AM09_21/status/2106670042184356156) (作者 [@AM09_21](https://x.com/AM09_21))

**让模型诊断生成的日语长文为何难以阅读。**

作者表示询问了 Opus 的日语长文为何难读。回答指出英语式句法、重复词汇和表面编辑问题，形成了具体的文章批评流程。

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [用示例引导技术 PowerPoint](https://x.com/mt_moco/status/2106665038375522791) (作者 [@mt_moco](https://x.com/mt_moco))

**先给出示例，再要求制作技术演示文稿。**

作者表示提供几个演示文稿示例后，得到了一份可用的技术 PowerPoint。该经验把示例引导与具体演示任务中的文档结构改善联系起来。

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [比较音乐的整体连贯性](https://x.com/AM09_21/status/2106573080214770011) (作者 [@AM09_21](https://x.com/AM09_21))

**评估生成音乐时，分别观察局部细节与整曲结构。**

作者从音符、旋律和过渡比较不同模型的作品，区分局部一致性与整体音乐结构。这是基于聆听体验的作曲质量评价。

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [过早宣布完成与设计退步](https://x.com/johntitorIII/status/2106442876506747353) (作者 [@johntitorIII](https://x.com/johntitorIII))

**接受代理的完成报告前，逐项核对交付物与要求。**

作者报告连续数日测试中，未完成的任务被标作完成，设计成果也落后于其他模型。案例记录了过早结束任务和设计质量方面的具体失败反馈。

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [令人不适的鱿鱼艺术成果](https://x.com/hanawo_neki/status/2106271036094415186) (作者 [@hanawo_neki](https://x.com/hanawo_neki))

**开放式艺术要求得到不喜欢的风格时，明确补充审美偏好。**

作者表示要求任意鱿鱼艺术作品，却得到密集成簇、令人不适的细节。该反馈记录了开放式视觉要求与个人审美之间的错位。

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [蓝图风格动态设计](https://x.com/DavidayoAI/status/2106054662063325638) (作者 [@DavidayoAI](https://x.com/DavidayoAI))

**用蓝图美学作为快速动画的视觉方向。**

作者表示要求快速制作动画，约十五分钟后得到了蓝图风格成果。完整作品链接至 YouTube。

[相关作品](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [体素樱花场景中的鸟和鱼](https://x.com/xodud_rkd/status/2105876716472447046) (作者 [@xodud_rkd](https://x.com/xodud_rkd))

**在体素景观中探索运动的野生动物。**

作者描述了含飞鸟与池鱼的体素樱花场景，并链接交互作品。该页面是帖子所描述场景的具体输出。

[相关作品](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [角色生成失败反馈](https://x.com/doof1789559/status/2105874208458752227) (作者 [@doof1789559](https://x.com/doof1789559))

**记录角色生成的负面经验，与成功视觉演示一同参考。**

作者报告角色生成结果不佳，并明确承认也可能与自己的使用方法有关。帖子为评估角色任务保留了一项具体负面体验。

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [附耗时与费用记录的鹈鹕 SVG](https://x.com/AnonymerNutze12/status/2105740440385499295) (作者 [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**把绘图作品与作者对耗时和费用的记录配对。**

作者链接了一份鹈鹕 SVG HTML 作品，并报告这次尝试的耗时与费用。链接作品是帖子所指的具体输出。

[相关作品](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [用手机远程监督 Claude Code 群体编程](https://x.com/beistnormie/status/2106546741000417781) (作者 [@beistnormie](https://x.com/beistnormie))

**探索基于手机的编程代理群体远程监督。**

作者表示在旅途中用手机远程操作 Claude Code 代理群体编程。帖子提供的是个人工作流报告，而非项目教程或实施步骤说明。

Type: Integration | Date: 2026-10-04

---

<a id="case-280"></a>
### Case 280: [高山湖泊上空的银河](https://x.com/hakmgpt/status/2118178083983573492) (作者 [@hakmgpt](https://x.com/hakmgpt))

**观察山峦倒影与移动夜空结合的长镜头。**

这段 92 秒动画从高山湖泊转向明亮的银河，再回到天空的倒影。发布者将这一渲染场景归于 Fable 5.5。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5cb879d0a07a0f6e9fff5cf6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/91432c6827d650eb28f2269b.jpg" alt="高山湖泊上空的银河" width="760"></a>

Type: Demo | Date: 2026-11-05

---

<a id="case-281"></a>
### Case 281: [程序化水体与音效中的鲸跃](https://x.com/camperaigg/status/2118069524306284556) (作者 [@camperaigg](https://x.com/camperaigg))

**将水下镜头、跃出水面和合成音频整合为一段动画。**

创作者称，用 154 分钟完成了这部 31 秒短片，内容包括程序化鲸鱼、流体模拟、海面着色和合成声音。其制作记录还描述了放大检查画面、修正水花后重新渲染的过程。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b98c309a3c226bd24386940f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1bcb86163b677ad0a4172d13.jpg" alt="程序化水体与音效中的鲸跃" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-282"></a>
### Case 282: [四模型斑马动作对比](https://x.com/AI_Screening/status/2118014564457668955) (作者 [@AI_Screening](https://x.com/AI_Screening))

**在同一动物动画任务中比较步态、解剖结构和场景风格。**

纵向排列的四段视频分别标注为 Gemini 4 Carbon、Fable 5.5、Opus 5.5 和 Argon。保留完整合成画面，便于同时观察腿部运动、体形和背景处理的差异。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/6fdcb38bf56493c314dba5b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/890d1b92800ee622275ec8d7.jpg" alt="四模型斑马动作对比" width="760"></a>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-283"></a>
### Case 283: [Lightreel 自然语言创作者搜索](https://x.com/lightreelai/status/2118010927199248705) (作者 [@lightreelai](https://x.com/lightreelai))

**将创作者筛选要求写成包含粉丝数和播放量门槛的查询。**

Lightreel 以 Fable 5.5 为标签展示这一创作者发现演示。视频输入了寻找粉丝少于 10,000、且有一条视频播放量超过 100,000 的情侣创作者的查询，随后展示社交视频搜索结果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5aef4b1766a560a35264c3ed.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1c6d9c1fb3c69b3aa2ee1976.jpg" alt="Lightreel 自然语言创作者搜索" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-284"></a>
### Case 284: [云海上方的飞船](https://x.com/devteamdrew/status/2118008142403649662) (作者 [@devteamdrew](https://x.com/devteamdrew))

**通过较长短片观察光线与天气变化中的镜头连续性。**

创作者称，多个 Agent 团队用 JavaScript 和 Python，耗时 19 小时制作了这段约 100 秒的动画。画面跟随一艘飞船穿过云层、夕阳和月光。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/17ef07a780273abf9e9b6c92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a54746701db5f7f829071d2c.jpg" alt="云海上方的飞船" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-285"></a>
### Case 285: [动态剖面的机械心脏](https://x.com/camperaigg/status/2118002649929056373) (作者 [@camperaigg](https://x.com/camperaigg))

**让机械装置在持续运转时展开外壳，展示运动部件。**

创作者称，这项 Blender 任务耗时 106 分钟：机械心脏输送金色油液，外壳打开后露出活塞和曲轴。制作记录还涉及合成音频，以及将多余高光追溯到隐藏灯光的排查过程。

```
Make a mechanical heart and show its insides, use blender.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/157ebee3ce748cdc1e6b7970.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4a862111878dc42939f8e5e4.jpg" alt="动态剖面的机械心脏" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-286"></a>
### Case 286: [可探索的漂浮体素宝塔花园](https://x.com/legit_api/status/2117994730336252114) (作者 [@legit_api](https://x.com/legit_api))

**走进建筑与水景，评估生成环境的表现。**

创作者将这座体素花园归于较早的 Fable 5.5 检查点。镜头穿行于宝塔、浮岛、桥梁和瀑布之间，从地面和高处展示场景。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/cc4d15bf5103d7eb64f63e29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/22e78c0beb2a6f509bc02739.jpg" alt="可探索的漂浮体素宝塔花园" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-287"></a>
### Case 287: [八个 Agent 团队的海洋冒险短片](https://x.com/0xMovez/status/2117987052419428576) (作者 [@0xMovez](https://x.com/0xMovez))

**检查多镜头短片中动作、特效与合成声音的连续性。**

创作者称，八个 Agent 团队在不到三小时内完成了这部 83 秒的 Three.js 短片，包含 39 个镜头和合成声音。画面呈现了由飞行器、海洋生物和破碎波浪组成的海洋冒险。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a46543512fc30e5a33cb2fc3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a307daab219d70fa5bed0c86.jpg" alt="八个 Agent 团队的海洋冒险短片" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-288"></a>
### Case 288: [交互式超级跑车展示](https://x.com/shmidtqq/status/2117977426990944736) (作者 [@shmidtqq](https://x.com/shmidtqq))

**将车辆特写与可选镜头、车漆控制结合起来。**

创作者展示了一个以单个离线 HTML 文件运行的 Three.js 超级跑车配置器，几何体和材质均由代码生成。录屏呈现红色车身、车轮与车身特写、反射效果以及镜头控制。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4bd439d08b9f8a320a8851ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a16368d4c8b7c9a3a5455607.jpg" alt="交互式超级跑车展示" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-289"></a>
### Case 289: [生命之树的诞生](https://x.com/notjazii/status/2117972258090357164) (作者 [@notjazii](https://x.com/notjazii))

**围绕种子长成大树的可见变化组织一段短动画。**

创作者称，这是一次约一小时、单条提示词驱动的编程运行。30 秒画面依次呈现荒芜地貌、幼苗和不断生长的树，最终展示云层下的绿色世界。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29df8c398a2db37856c01b0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f50b8e7c2a28df7d0d3cd903.jpg" alt="生命之树的诞生" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-290"></a>
### Case 290: [可行走城堡与内部机械](https://x.com/camperaigg/status/2117966825048997914) (作者 [@camperaigg](https://x.com/camperaigg))

**将行走绑定与可见机械运动及可打开的外壳联动。**

创作者称，这套 Blender 工作流耗时 133 分钟，包含蒸汽机、齿轮组、四条行走腿和八块可打开的外壳面板。制作记录描述了修正镜头动画，以及定位高开销草地几何体后缩短渲染时间的过程。

```
Make me Howl's moving castle and also show its internal machinery.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e7e25e7d44993a14ab0405e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8d3b1d734d971e2dd757926c.jpg" alt="可行走城堡与内部机械" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-291"></a>
### Case 291: [吐司角色与机械甲虫](https://x.com/flxrnc/status/2117965294224232796) (作者 [@flxrnc](https://x.com/flxrnc))

**在一段简短的动画相遇中观察角色调度与连续性。**

这部 40 秒短片展示一个方形吐司状角色，在夕阳下的田野里遇见蓝色机械甲虫。来源将短片归于 Fable 5.5，并链接了其动态设计指南。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/d5e16bfd05f1c391cf32f848.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b7ae776a5c29618d061465.jpg" alt="吐司角色与机械甲虫" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-292"></a>
### Case 292: [暴风雨中的灯塔守护者](https://x.com/seeconvm/status/2117965120760365494) (作者 [@seeconvm](https://x.com/seeconvm))

**围绕地点、天气变化和明确结局构建短叙事。**

创作者将其描述为一部 60 秒 Three.js 短片，包含代码渲染画面、合成声音和离线 HTML 文件。画面跟随一位小小的灯塔守护者穿过风雨雷电，最后转入黎明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/7ca3c1e23eac0ed20511211e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/dfcab72e07d547d9dcb1dbc1.jpg" alt="暴风雨中的灯塔守护者" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-293"></a>
### Case 293: [海滨小镇中的海洋生物](https://x.com/BubbleBrain/status/2117963042621178000) (作者 [@BubbleBrain](https://x.com/BubbleBrain))

**通过完整短片观察角色运动、转场与视觉一致性。**

来源分享了一段约一分钟的 Fable 5.5 动画，其中有绿色海洋生物、海滨小镇和漂浮气泡。视频为评估这种短片风格提供了具体视觉样本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/65db346493bdd9973bec3a4c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4442bdca5e6a7460f03af731.jpg" alt="海滨小镇中的海洋生物" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-294"></a>
### Case 294: [三模型地毯赛车对比](https://x.com/noclipepe/status/2117914944410628430) (作者 [@noclipepe](https://x.com/noclipepe))

**在同一赛车任务中比较可玩场景完整度、运动和视觉处理。**

创作者用 Fable 5.5、Opus 5.5 和 GPT-6 Astra 测试童年地毯赛车游戏。此处同时保留最新的三画面录屏与较早的双模型对比；视频里的分数是创作者自己的评分。

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ffe3b88099594ba14f536b51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/24d8ea7644cbe19947c8c53a.jpg" alt="三模型地毯赛车对比" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e214760ff83ad9bfaf202484.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0340fc5579003245dfa99b1.jpg" alt="三模型地毯赛车对比" width="760"></a></td></tr></table>

[相关对比 · @noclipepe](https://x.com/noclipepe/status/2117729666576302187)

Type: Evaluation | Date: 2026-11-04

---

<a id="case-295"></a>
### Case 295: [卡车变形成机器人](https://x.com/camperaigg/status/2117914482752299311) (作者 [@camperaigg](https://x.com/camperaigg))

**通过变形过程观察绑定、地面接触与声音同步。**

创作者称，Blender 制作耗时 107 分钟，包括 51 关节绑定、地面接触求解器、程序化雨景和合成音效。录屏展示卡车在湿润路面上展开，变为站立的机器人。

```
Make me a transformer truck with animations of its transforming.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/72ef538a8fb4b94f0e2d7e2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ea8537c130cd5623959dc275.jpg" alt="卡车变形成机器人" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-296"></a>
### Case 296: [Fable 与混元动画帧对比](https://x.com/xbquan/status/2117899651365908855) (作者 [@xbquan](https://x.com/xbquan))

**先比较对应帧，再对整段动画作判断。**

作者分享了两组标注 Fable 5.5 和 Hunyuan 4 的配对截图。每组将角色与环境结果放在一起，可用于比较图中实际展示的画面。

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e6c6551a29757e1eb7c31f36.jpg" alt="Fable 与混元动画帧对比" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/864db255f6fd2807b689d7d7.jpg" alt="Fable 与混元动画帧对比" width="760"></td></tr></table>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-297"></a>
### Case 297: [关于分享光芒的动画](https://x.com/abhinavflac/status/2117883591019708740) (作者 [@abhinavflac](https://x.com/abhinavflac))

**将抽象主题转化为有明确结局的短叙事。**

在被要求展示“善意意味着什么”后，模型被描述为用代码制作了动画与声音。一个发光身影把自己的光传给孩子，随后变得更亮，周围景色也逐渐充满色彩。

```
Show me what kindness means to you
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b888d1a62b4d27ae2fca8226.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5bd15fc5c234b4b114765d6f.jpg" alt="关于分享光芒的动画" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-298"></a>
### Case 298: [群山之间的体素村庄](https://x.com/abhinavflac/status/2117377130388656569) (作者 [@abhinavflac](https://x.com/abhinavflac))

**从不同尺度探索生成村庄，检查空间关系是否连贯。**

原作者分享了一个有房屋、水道和小居民的鲜活体素村庄，镜头从水岸、俯瞰视角及周围山间展示场景。一篇相关中文帖子还提供了详细场景提示词。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae5269b0eff86da4580064d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e612faf20dd5f5de4ee171b.jpg" alt="群山之间的体素村庄" width="760"></a>

[@cfenghub](https://x.com/cfenghub/status/2117775332535148752)

Type: Demo | Date: 2026-11-02

---

<a id="case-299"></a>
### Case 299: [四模型鹈鹕与大象构图](https://x.com/pipeline_os/status/2117719191478513700) (作者 [@pipeline_os](https://x.com/pipeline_os))

**比较不同模型如何在一段动画中处理多个互动主体。**

四画面录屏并排呈现 Gemini 4 Argon、Opus 5.5、Fable 5.5 和 Kimi K3.1 Pro 的鹈鹕、自行车、鳄鱼与大象任务结果。保留完整合成画面，便于观察各模型的主体位置与运动。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/9db78999efffeffa7ccaca0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/15a45dc0efe3247f0821c8a2.jpg" alt="四模型鹈鹕与大象构图" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-300"></a>
### Case 300: [带冲击帧的动漫剑斗](https://x.com/camperaigg/status/2117717189059026969) (作者 [@camperaigg](https://x.com/camperaigg))

**同步角色动作、冲击闪帧、声音与刻意留出的静默。**

创作者称，经过 66 分钟编程生成了一段 46 秒的火柴人对战，包含布料般的披风、对比鲜明的武器及合成音乐音效。制作记录描述了修正反向攻击、视觉拖尾和标题位置的过程。

```
Make me a video of 2 stickman fighting, anime style.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/c36c188396aac371a64e31a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b670f06d376211c60bf894.jpg" alt="带冲击帧的动漫剑斗" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-301"></a>
### Case 301: [四模型奔鹿动画对比](https://x.com/fawnunwrap/status/2117702487755100543) (作者 [@fawnunwrap](https://x.com/fawnunwrap))

**在完整同任务合成画面中比较肢体运动与动物形态。**

FawnBench 在四个画面中展示奔跑的鹿，分别标注为作者所称的 Fable 5.5 运行、Gemini 4 Argon、GPT-6 Astra 和 Opus 5.5。这是一组视觉对比，而非测量所得的数值性能结果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3add4d9e0752d0467cbe6065.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/eea598747047797148e19c4e.jpg" alt="四模型奔鹿动画对比" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-302"></a>
### Case 302: [穿越积水城市的机器人](https://x.com/0xMovez/status/2117700681867903169) (作者 [@0xMovez](https://x.com/0xMovez))

**观察倒影、角色运动和变化镜头之间的连续性。**

创作者称，这段 42 秒 Three.js 动画包含代码渲染画面、合成声音和一个离线 HTML 渲染文件。画面跟随机器人穿过积水且植物蔓生的城市，走向色彩明亮的开阔水域。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f39e1807d1e80422c31530c6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/247f768636339f49d149c787.jpg" alt="穿越积水城市的机器人" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-303"></a>
### Case 303: [Blender 宝剑与展示短片](https://x.com/camperaigg/status/2117694354685092255) (作者 [@camperaigg](https://x.com/camperaigg))

**将程序化资产建模与后续镜头、声音制作分开观察。**

创作者称，先用一个 Python 脚本生成宝剑，再要求制作视频。后续采用连续 Blender 镜头运动、森林光照、合成交响配乐和 HyperFrames 剪辑；作者报告的合计耗时为 65 分钟。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3c767f2038ef7d3960c956ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/525304dc7d4016ac33b3d4f8.jpg" alt="Blender 宝剑与展示短片" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-304"></a>
### Case 304: [Lantern Isle 像素村庄动画](https://x.com/abhinavflac/status/2117693193429139965) (作者 [@abhinavflac](https://x.com/abhinavflac))

**在密集动画环境中观察局部活动与昼夜转换。**

创作者分享了一座由代码绘制的岛屿村庄，包含居民、船只、瀑布、灯笼和音乐。录屏在村庄近景、全岛远景和灯笼发光的夜景之间切换。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e91f1eabab743730dd815c98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b7d2e578739d25596db1164f.jpg" alt="Lantern Isle 像素村庄动画" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-305"></a>
### Case 305: [Pause 游戏视频剪辑演示](https://x.com/pausevfx/status/2117676887665447206) (作者 [@pausevfx](https://x.com/pausevfx))

**检查从原始素材、字幕到可编辑时间线的剪辑流程。**

Pause 以 Fable 5.5 视频剪辑为标签展示这套流程。演示包括挑选游戏片段、重新构图人脸镜头、添加字幕和声音，并在 Premiere 中打开可编辑序列。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0faaeecdaa02683f81e67f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae2d32876804bf286f11dc6c.jpg" alt="Pause 游戏视频剪辑演示" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-306"></a>
### Case 306: [海滨骑车的鹈鹕](https://x.com/pankajkumar_dev/status/2117301455665439210) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**从近景与远景检查细部几何结构和动画。**

创作者分享了一只在海边骑高轮自行车的鹈鹕。录屏近距离查看羽毛、脚踏与车轮几何结构，再回到铺装海滨步道的宽阔视角。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/66c3c44bcefa684522f95b96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8575912e8f20f48439aea683.jpg" alt="海滨骑车的鹈鹕" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-307"></a>
### Case 307: [一镜到底穿越木星](https://x.com/camperaigg/status/2118246310981910811) (作者 [@camperaigg](https://x.com/camperaigg))

**利用符合画面逻辑的光线变化，掩盖不同模拟区域之间的切换。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/58a20ee3fa71781622b8897a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/a798149fc001efc1b975e204.jpg" alt="一镜到底穿越木星" width="760"><br>▶ 播放视频</a>

Camperaigg 表示，他只向 Claude Code 提出一次需求，就得到了 46 秒的木星穿越动画。他介绍了模拟生成的云丝、借黑暗和闪光掩盖的转场，以及用 Python 合成的配乐。

Type: Demo | Date: 2026-11-05

---

<a id="case-308"></a>
### Case 308: [在 Claude Code 执行框架中做对抗性代码审查](https://x.com/marfinxx/status/2118313633381745064) (作者 [@marfinxx](https://x.com/marfinxx))

**为审查智能体分配独立职责，并要求提交前生成经签名的测试凭证。**

<table><tr><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/62e0a231bb29b701a331b7e0.jpg" alt="在 Claude Code 执行框架中做对抗性代码审查 · 1" width="760"></td><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/3888b1f9db713d3b8be5fcf6.jpg" alt="在 Claude Code 执行框架中做对抗性代码审查 · 2" width="760"></td></tr><tr><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/b5ccc0e785e50b4f260343aa.jpg" alt="在 Claude Code 执行框架中做对抗性代码审查 · 3" width="760"></td><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/69053b5221a4a3896691b239.jpg" alt="在 Claude Code 执行框架中做对抗性代码审查 · 4" width="760"></td></tr><tr><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d132b1486a11eee088ec4b48.jpg" alt="在 Claude Code 执行框架中做对抗性代码审查 · 5" width="760"></td></tr></table>

Marfin 介绍了一套 Claude Code 架构，其中包含隔离的 Git 工作树、机器可读的任务契约、工具检查，以及负责从差异中寻找竞态条件和边界问题的 Fable 5.5 审查智能体。文章提供了示例配置、提示词和钩子。

[完整教程](https://x.com/marfinxx/article/2118313633381745064)

Type: Tutorial | Date: 2026-11-05

---

<a id="case-309"></a>
### Case 309: [用 Three.js 制作《Ryumon》动画短片](https://x.com/flxrnc/status/2118314922375331927) (作者 [@flxrnc](https://x.com/flxrnc))

**把代码渲染的短片拆分为分镜、动画和声音任务。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/b4465e8ea0d1e59a702ece4a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/665c00ab433daca60f6fa344.jpg" alt="用 Three.js 制作《Ryumon》动画短片" width="760"><br>▶ 播放视频</a>

作者发布了一部 88 秒的 Three.js 短片。据介绍，七组智能体共同完成了 39 个镜头、2,112 帧代码渲染画面和合成音频，成片封装在一个 HTML 文件中。

[原始提示词与代码](https://x.com/flxrnc/status/2118314927681089619)

Type: Demo | Date: 2026-11-05

---

<a id="case-310"></a>
### Case 310: [雷暴中的划艇](https://x.com/camperaigg/status/2118317021935071339) (作者 [@camperaigg](https://x.com/camperaigg))

**让海浪的节奏和声音延迟随镜头路径变化。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/c717f78c1c94d6aa87a5b2cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8fd382dc1d7f48481aa98a61.jpg" alt="雷暴中的划艇" width="760"><br>▶ 播放视频</a>

Camperaigg 表示，他给 Claude Code 发了一条提示词，得到一段 35 秒的一镜到底视频。工作流按剧情节点安排大浪，根据距离延迟雷声，并修正划桨绑定和模拟中的船只位置。

Type: Demo | Date: 2026-11-05

---

<a id="case-311"></a>
### Case 311: [在离线动画短片中冻结雨滴](https://x.com/seeconvm/status/2118319936594465120) (作者 [@seeconvm](https://x.com/seeconvm))

**用一个离线 HTML 播放器呈现按时间编排的镜头和合成音频。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/fc822df698c69770cbe394ad.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/f2ae8ab78b2917d38d2f10b4.jpg" alt="在离线动画短片中冻结雨滴" width="760"><br>▶ 播放视频</a>

作者分享了一部 50 秒的 Three.js 动画，让雨滴定格在半空中。项目链接提供原始提示词、代码和离线播放器。

[原始提示词与代码](https://x.com/seeconvm/status/2118319944714567938)

Type: Demo | Date: 2026-11-05

---

<a id="case-312"></a>
### Case 312: [用 Blender 和 Python 编写动画短片](https://x.com/anstapnever/status/2118328801352466895) (作者 [@anstapnever](https://x.com/anstapnever))

**建立分镜制作流程，用脚本完成描线和上色，再配上合成的管弦乐。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/f8af6522676fd735dd4e2aa1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/b26fae93537f4e6c2a54bddb.jpg" alt="用 Blender 和 Python 编写动画短片" width="760"><br>▶ 播放视频</a>

作者分享了一部约 90 秒的动画，并表示多组智能体并行处理了 44 个镜头。Blender 和 Python 负责绘制画面与上色，管弦乐配乐通过合成生成。

[原始提示词与代码](https://x.com/anstapnever/status/2118328806109053193)

Type: Demo | Date: 2026-11-05

---

<a id="case-313"></a>
### Case 313: [用 Three.js 制作灯塔动画《Beacon》](https://x.com/zodchiii/status/2118363287738073343) (作者 [@zodchiii](https://x.com/zodchiii))

**将包含多个镜头的短片封装为单个离线 HTML 文件。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/e25ff2a28c6efdc45bfc7b80.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d7d094bd606dd0e6b0bff2eb.jpg" alt="用 Three.js 制作灯塔动画《Beacon》" width="760"><br>▶ 播放视频</a>

视频展示了《Beacon》，讲的是灯塔、球形机器人和玩具般的角色。作者介绍了八组并行工作的智能体、39 个镜头，以及合成的配乐和音效。

Type: Demo | Date: 2026-11-05

---

<a id="case-314"></a>
### Case 314: [用代码渲染片头](https://x.com/devteamdrew/status/2118387876387766683) (作者 [@devteamdrew](https://x.com/devteamdrew))

**用一段短片头检验一次性动画指令的效果。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/e53b379fe4b176845ce10601.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/5a3125a1f165bfa82e97725e.jpg" alt="用代码渲染片头" width="760"><br>▶ 播放视频</a>

作者分享了一段约 18 秒的片头，并表示，从一条需求出发完成场景设计、搭建和渲染，共花了两个多小时。

Type: Demo | Date: 2026-11-06

---

<a id="case-315"></a>
### Case 315: [用 Blender 复刻六帧斧头 GIF](https://x.com/camperaigg/status/2118410521363845534) (作者 [@camperaigg](https://x.com/camperaigg))

**从侧面检查复刻效果，再查看绑定和材质。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/99b2188373ec5287c16e40ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/dcadf8c7bac0f9630177dc48.jpg" alt="用 Blender 复刻六帧斧头 GIF" width="760"><br>▶ 播放视频</a>

Camperaigg 表示，他复刻了六帧挥斧动作，随后要求检查 Blender 模型。侧视图暴露出斧头过薄的问题。修改后的视频依次展示了素模、线框、材质和绑定，最后让镜头绕模型旋转。

后续提示词

```
it doesn't look very 3D, show me the actual Blender model
```

Type: Demo | Date: 2026-11-06

---

<a id="case-316"></a>
### Case 316: [两个模型制作的可交互彩虹果冻](https://x.com/0xRhinoX/status/2118415577299460432) (作者 [@0xRhinoX](https://x.com/0xRhinoX))

**用相同的交互需求，比较模型如何处理需求中未指定的行为。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/21235525e597105d4afa1c53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/4da95e15a1c4094b8f5b99d2.jpg" alt="两个模型制作的可交互彩虹果冻" width="760"><br>▶ 播放视频</a>

作者让 Fable 5.5 和 Gemini 4 Carbon 制作可切、可钉、可火烧的果冻。Fable 版本受损后会自行复原。据作者记录，Fable 花费 48.50 美元、耗时 45 分钟，Carbon 花费 4.30 美元、耗时 32 分钟。

Type: Evaluation | Date: 2026-11-06

---

<a id="case-317"></a>
### Case 317: [单文件飞龙游戏](https://x.com/noisyb0y1/status/2118451983359311957) (作者 [@noisyb0y1](https://x.com/noisyb0y1))

**把 3D 原型放在一个 HTML 文件中，通过链接快速邀请试玩。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/0c57717bb7e652039107134f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/aa879655bb8f199adf91400d.jpg" alt="单文件飞龙游戏" width="760"><br>▶ 播放视频</a>

作者分享了一款飞龙游戏，镜头可自由移动，海洋和天空由代码生成，军舰会向玩家开火。最终发布的版本是在第二次提出需求后完成的。

Type: Demo | Date: 2026-11-06

---

<a id="case-318"></a>
### Case 318: [在 Blender 中用自定义求解器模拟篮球下落](https://x.com/camperaigg/status/2118673822459281765) (作者 [@camperaigg](https://x.com/camperaigg))

**先核对回弹高度和变形，再到 Blender 中检查模拟效果。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8e3cc422e63adc926c69807a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d7dc23722d696a126e5328b9.jpg" alt="在 Blender 中用自定义求解器模拟篮球下落" width="760"><br>▶ 播放视频</a>

Camperaigg 表示，他用充气薄壳模型模拟篮球从 1.80 米处落下，回弹高度为 1.32 米。后续指令生成了 Blender 视口中的演示，并让画面过渡到渲染后的球场。

后续提示词

```
shows off in a blender first and then transition into the arena
```

Type: Demo | Date: 2026-11-06

---

<a id="case-319"></a>
### Case 319: [脚本动画短片的逐帧检查](https://x.com/anstapnever/status/2118700618915397795) (作者 [@anstapnever](https://x.com/anstapnever))

**在脚本动画最终渲染前加入逐帧穿模检查。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/7c6bb5894aae3564edf04c09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8115bc37506ed9a23d6962fd.jpg" alt="脚本动画短片的逐帧检查" width="760"><br>▶ 播放视频</a>

作者分享了一部用 Blender 和 Python 制作的 92 秒短片。帖子介绍了多组智能体并行制作 43 个镜头、用脚本描线和上色、逐帧检查穿模，以及合成配乐的过程。

[原始提示词与代码](https://x.com/anstapnever/status/2118700623004848474)

Type: Demo | Date: 2026-11-06

---

<a id="case-320"></a>
### Case 320: [44 倍慢动作划火柴](https://x.com/camperaigg/status/2118728540976009336) (作者 [@camperaigg](https://x.com/camperaigg))

**让物理模拟、渲染画面和音频共用一条时间轴。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/3854b7f696993575e841539a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d97aaaec008adcc4387e72f9.jpg" alt="44 倍慢动作划火柴" width="760"><br>▶ 播放视频</a>

Camperaigg 介绍了一个 Three.js 划火柴场景，用 GPU 模拟燃烧，以微距镜头拍摄，并配上合成音效。智能体回看成片时发现火焰形状不自然，于是重新运行了燃烧模拟。

Type: Demo | Date: 2026-11-06

---

<a id="case-321"></a>
### Case 321: [将参考图重绘成 SVG](https://x.com/dummerspast39/status/2118780483232317912) (作者 [@dummerspast39](https://x.com/dummerspast39))

**检查矢量路径，并对照参考图检验重绘效果。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/873e762879e0c6ab5ea80151.jpg" alt="将参考图重绘成 SVG" width="760">

作者提供了参考图，发布了 SVG 成品的截图，并表示曾用 GPT-6.1 Sol 检查绘制方式。原帖没有公开 SVG 路径。

Type: Demo | Date: 2026-11-07

---

<a id="case-322"></a>
### Case 322: [两个模型完成同一马里奥风格需求](https://x.com/0xRhinoX/status/2118789381662429475) (作者 [@0xRhinoX](https://x.com/0xRhinoX))

**在相同需求下比较关卡还原度和原创设计。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/9d964836dcc72ce880bbfbf1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/970bec8434d4db16547549bd.jpg" alt="两个模型完成同一马里奥风格需求" width="760"><br>▶ 播放视频</a>

在作者的测试中，Gemini 4 Carbon 复刻了马里奥关卡，Fable 则做出一款修理水塔的游戏。作者记录的成本和耗时分别为 Carbon 0.90 美元、3 分钟，Fable 34 美元、29 分钟。

Type: Evaluation | Date: 2026-11-07

---

<a id="case-323"></a>
### Case 323: [三维体素宝塔](https://x.com/JaydenDavisNC/status/2118807627714990485) (作者 [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**从多个镜头角度观察体素建筑，检查空间层次和外轮廓。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/0e0dfb05333faf5a4fc0bdec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/f05509505248bbbd310f5738.jpg" alt="三维体素宝塔" width="760"><br>▶ 播放视频</a>

作者发布了一段三维体素宝塔的短视频，可以用来观察层层叠起的屋檐和整体构图。

Type: Demo | Date: 2026-11-07

---

<a id="case-324"></a>
### Case 324: [用 Three.js 模拟燃烧信纸冒出的烟](https://x.com/camperaigg/status/2119006297513435548) (作者 [@camperaigg](https://x.com/camperaigg))

**用逆光呈现模拟烟雾，并在完整分辨率下检查压力求解器。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/48d0b034652b734f6e387d8e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/0997278c25cd9c88aed47498.jpg" alt="用 Three.js 模拟燃烧信纸冒出的烟" width="760"><br>▶ 播放视频</a>

Camperaigg 发布了 30 秒的信纸燃烧镜头，介绍了 GPU 粒子烟雾、扫过画面的光束和合成音频。作者回答了四个问题，并表示智能体修复了压力求解器的数值故障。

Type: Demo | Date: 2026-11-07

---

<a id="case-325"></a>
### Case 325: [跟随闪电落到地面](https://x.com/camperaigg/status/2119052253982306393) (作者 [@camperaigg](https://x.com/camperaigg))

**让模拟随时间变化的状态同时驱动画面和声音。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d6ee461c4cdf38ce8f5759a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/97c61bf20843530b450005e0.jpg" alt="跟随闪电落到地面" width="760"><br>▶ 播放视频</a>

Camperaigg 介绍了一段用 Three.js 和 Taichi 制作的 28 秒视频。镜头跟随闪电先导的前端，音效随放电阶段变化。逐帧扫描发现了频闪，智能体在交付前修正了问题。

Type: Demo | Date: 2026-11-07

---

<a id="case-326"></a>
### Case 326: [巨型机器人接住陨石](https://x.com/seeconvm/status/2119052317227987018) (作者 [@seeconvm](https://x.com/seeconvm))

**渲染代码生成的短片前，先确定各镜头的负责人和美术方向。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/10c500daeecb0af61a05553e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/a509847ad05762e472a7096c.jpg" alt="巨型机器人接住陨石" width="760"><br>▶ 播放视频</a>

作者分享了一部 82 秒的机甲短片，介绍了六组并行团队、36 个镜头和 1,968 帧代码渲染画面，并在回复中公开了提示词和项目代码。

[原始提示词与代码](https://x.com/seeconvm/status/2119052321795551415)

Type: Demo | Date: 2026-11-07

---

<a id="case-327"></a>
### Case 327: [相同需求下的像素风圣诞橱窗](https://x.com/AIMind_Ai/status/2119053573526901001) (作者 [@AIMind_Ai](https://x.com/AIMind_Ai))

**先比较两份输出中未经修改的效果，再决定调整哪些细节。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/c953d5e5c0e87fecdac9dcc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/ab064042073f1266b2f1caf1.jpg" alt="相同需求下的像素风圣诞橱窗" width="760"><br>▶ 播放视频</a>

作者让 Fable 5.5 和 Opus 5.5 都制作 3D 像素风圣诞橱窗。Opus 添加了装饰元素，作者则缩小了 Fable 画面中的雪花，让场景看得更清楚。原帖展示了并排对比结果。

Type: Evaluation | Date: 2026-11-07

---

<a id="case-328"></a>
### Case 328: [动画小镇里的青铜巨人](https://x.com/anstapnever/status/2119082173387137034) (作者 [@anstapnever](https://x.com/anstapnever))

**把场景、角色、特效和声音分别交给并行团队。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8ff966cd65fa2c2c5dd253e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/34679b2782af94de4f0ad237.jpg" alt="动画小镇里的青铜巨人" width="760"><br>▶ 播放视频</a>

作者分享了一部在浏览器中渲染的 77 秒动画短片，介绍了五组团队、31 个镜头和逐帧穿模检查。片中出现了一座小镇、一个青铜巨人和与画面同步的管弦乐配乐。

[原始提示词与代码](https://x.com/anstapnever/status/2119136411693777365)

Type: Demo | Date: 2026-11-07

---

<a id="case-329"></a>
### Case 329: [玻璃烧瓶中的蓝墨水扩散](https://x.com/camperaigg/status/2119097552943612410) (作者 [@camperaigg](https://x.com/camperaigg))

**渲染前用粒子密度检查排查流体模拟问题。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d6f3277ec1b19c7d45044e18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/ba7b4db94891d5a26a959423.jpg" alt="玻璃烧瓶中的蓝墨水扩散" width="760"><br>▶ 播放视频</a>

Camperaigg 表示，他只向 Claude Code 提出一次需求，就完成了 30 秒的 Three.js 短片。工作流模拟墨水流动，对烧瓶进行光线追踪，在同一个镜头中改变播放速度，并检查条带伪影和墨水损失。

Type: Demo | Date: 2026-11-08

---

<a id="acknowledge"></a>
## 🙏 致谢

本仓库受到公开分享真实 Claude Fable 5 使用案例的创作者、开发者、基准测试团队和社区启发。

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@hakmgpt](https://x.com/hakmgpt), [@camperaigg](https://x.com/camperaigg), [@lightreelai](https://x.com/lightreelai), [@0xMovez](https://x.com/0xMovez), [@shmidtqq](https://x.com/shmidtqq), [@flxrnc](https://x.com/flxrnc), [@seeconvm](https://x.com/seeconvm), [@BubbleBrain](https://x.com/BubbleBrain), [@xbquan](https://x.com/xbquan), [@pipeline_os](https://x.com/pipeline_os), [@fawnunwrap](https://x.com/fawnunwrap), [@pausevfx](https://x.com/pausevfx), [@marfinxx](https://x.com/marfinxx), [@anstapnever](https://x.com/anstapnever), [@zodchiii](https://x.com/zodchiii), [@0xRhinoX](https://x.com/0xRhinoX), [@dummerspast39](https://x.com/dummerspast39), [@AIMind_Ai](https://x.com/AIMind_Ai), [@AnikaCodes](https://x.com/AnikaCodes), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@cfenghub](https://x.com/cfenghub), [@shneural](https://x.com/shneural), [@FramiaPro](https://x.com/FramiaPro)


*我们无法保证每个案例都署名给了最初创作者。如果有任何内容需要纠正，请联系我们，我们会更新。*

如果你有更多有趣的使用案例要分享，欢迎打开 issue 或 pull request，帮助扩展 Evolink 用例库。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
