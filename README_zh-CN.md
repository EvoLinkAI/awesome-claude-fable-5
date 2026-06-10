<div align="center">

<a href="https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5"><img src="images/zh.png" alt="Claude Fable 5 high usecase repository logo" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Try it on Evolink](https://img.shields.io/badge/Try_it_on-Evolink-black)](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)
[![Website](https://img.shields.io/badge/Website-Live-orange)](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)
[![Docs](https://img.shields.io/badge/Docs-Read-blue)](https://docs.evolink.ai)

[![English](https://img.shields.io/badge/English-Read-111111)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-Read-ffb703)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-Read-2a9d8f)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-Read-52b788)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-Read-4ea8de)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-Read-f4a261)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-Read-e76f51)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-Read-d62828)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-Read-8338ec)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-Read-ef476f)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-Read-577590)](README_ru.md)

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

- **60 个精选 Claude Fable 5 案例**，来自公开创作者、开发者、基准测试团队和工具构建者。
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
| [📏 评测、对比与限制](#evaluations-comparisons-and-limits) | Case 35-60 |
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


<a id="coding-and-code-generation"></a>
## 💻 编码与代码生成

<a id="case-1"></a>
### Case 1: [Cursor 多阶段工作流](https://x.com/AlicanKiraz0/status/2064487347605918180)（作者 [@AlicanKiraz0](https://x.com/AlicanKiraz0)）

**把 Fable 5 用作多模型 Cursor 工作流中的计划审查和批判步骤，然后把实现和修订交还给更便宜或更专用的模型。**

如果看 Fable 5 和 GPT 5.5 的最终评分，差距非常小。我个人的使用建议是：在 Cursor 这类支持混合模型的 IDE 平台中，使用分阶段工作流。

阶段 1：在代码审查和项目初步检查阶段，一边预热上下文，一边使用 GPT 5.5 High、Minimax M3、Kimi K2.6 或 Composer 2.5 之一。

阶段 2：准备项目计划时，使用 GPT 5.5 Very High 或 Opus 4.8。

阶段 3：分析项目计划时，使用 Fable 5；让它找出计划中的缺陷部分。修订时使用 GPT 5.5 Very High。

阶段 4：实现计划时，使用 Minimax M3、Deepseek v4 Max、Composer 2.5 或 Sonnet 4.6。

阶段 5：最终审查并检查实现是否遵循计划时，使用 GPT 5.5 High。

类型：评测 | 日期：2026-06-09

---

<a id="case-2"></a>
### Case 2: [从截图重建 GitHub](https://x.com/coldopn/status/2064435234465087638)（作者 [@coldopn](https://x.com/coldopn)）

**把产品截图粘贴到代理式编码工具中，并要求 Fable 5 复刻带真实功能的界面。**

🚨 Anthropic Fable 5 刚刚从一张截图复刻了 GITHUB！！

我做的全部事情，就是把一张 GitHub UI 截图粘贴进 Kilo Code，然后告诉它用真实功能重建 GitHub。

它写了 10 分钟代码，花费 $4.07。

结果是一个可用的 GitHub 复刻版：https://t.co/bjMObvlsPX

类型：演示 | 日期：2026-06-09

---

<a id="case-3"></a>
### Case 3: [单提示词黑洞模拟](https://x.com/deveshcodes_/status/2064437742189379745)（作者 [@deveshcodes_](https://x.com/deveshcodes_)）

**给 Fable 5 一条详细的创意编程提示词，让它生成一个自包含的 Three.js 物理可视化。**

@claudeai 使用 Claude Fable 5 一次性生成了一个 Three.js 实时黑洞透镜模拟。

它包含引力透镜、带多普勒增强的吸积盘、光子球、色差和程序化星空。

结果：60fps、单个 HTML 文件、一条提示词。

新的基线太夸张了 🤯 https://t.co/E23I8bnPKb

类型：教程 | 日期：2026-06-09

---

<a id="case-4"></a>
### Case 4: [一次生成 macOS 风格 Web OS](https://x.com/intheworldofai/status/2064421915347812672)（作者 [@intheworldofai](https://x.com/intheworldofai)）

**让 Fable 5 生成一个完整的单文件 Web OS，并让它一次性构建 UI 外壳、应用、交互、音频和内嵌游戏行为。**

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

类型：教程 | 日期：2026-06-09

---

<a id="case-5"></a>
### Case 5: [用 1,687 条提示词构建 Spawn 5.0](https://x.com/jsnnsa/status/2064420561078693941)（作者 [@jsnnsa](https://x.com/jsnnsa)）

**把 Fable 5 当作长会话工程伙伴，在大量提示词中协作，人类角色从架构转向判断输出质量。**

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

类型：教程 | 日期：2026-06-09

---

<a id="case-6"></a>
### Case 6: [带发现项的大型 Pull Request 审查](https://x.com/ryanrhughes/status/2064411147076534705)（作者 [@ryanrhughes](https://x.com/ryanrhughes)）

**让 Fable 5 面向一个大型 Pull Request，要求它审查正确性、误报、真实 bug 和打磨问题。**

我让 Fable 5 放手审查一个 PR（74 个文件 / +3,705 / -1,246），看看表现如何。它运行了 34 分钟，消耗了我 5 小时会话的 42%，产出 16 个“正确性”发现，并找到了：

- 2 个听起来很吓人的误报
- 3 个真实的审计正确性 bug
- 大约 5 个合理但较小的 UX/打磨问题
- 一堆清理建议

这也危险到不能发布？

类型：演示 | 日期：2026-06-09

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

类型：评测 | 日期：2026-06-09

---

<a id="case-8"></a>
### Case 8: [诊断基础设施故障并打开修复 PR](https://x.com/ayushagarwal/status/2064422467557564862)（作者 [@ayushagarwal](https://x.com/ayushagarwal)）

**给 Fable 5 提供日志、数据库错误和镜像摘要等基础设施线索，然后让它诊断故障并准备修复。**

claude fable 5 真的真的很强！！！！

它刚刚诊断出一个我甚至无法准确描述的自托管旁路基础设施故障。

它读取 pod 日志、查询 Cloud SQL 错误日志、比较镜像摘要，发现 Kubernetes 正在针对新迁移的数据库运行一个 3 个月前缓存的旧镜像。

然后它打开了修复 PR。

几分钟，不是几小时。没有 web 搜索。🤯

类型：评测 | 日期：2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 游戏与交互演示

<a id="case-9"></a>
### Case 9: [手指追踪 Dino Runner](https://x.com/ai_for_success/status/2064413182396108932)（作者 [@ai_for_success](https://x.com/ai_for_success)）

**让 Fable 5 构建一个以手指追踪作为输入机制的浏览器游戏。**

我让 Fable 5 构建一个带手指追踪的 Dino runner 游戏。

它大约 11 到 12 分钟一次性完成了 finger runner 游戏，消耗约 914K token，并且只用 629 行代码实现了全部内容。

https://t.co/AWt1lEIObq

类型：演示 | 日期：2026-06-09

---

<a id="case-10"></a>
### Case 10: [两句话生成赛车游戏](https://x.com/kieradev/status/2064482704763085202)（作者 [@kieradev](https://x.com/kieradev)）

**给 Fable 5 一个很短的游戏提示词，让它一次生成地图、模式、音乐、UI 和游戏资产。**

Claude Fable 5，使用了 Max 5x 用量的 40%。

从一条两句话的提示词生成了完整的 Mario Kart 64 类型游戏。

Fable 5 在一次运行中处理了所有装饰、角色模型、4 张地图、音乐、全部三种游戏模式和 UI，大约 15 分钟完成。

#fable #anthropic https://t.co/B7mTidE84U

类型：教程 | 日期：2026-06-09

---

<a id="case-11"></a>
### Case 11: [Rust 可安装终端版 Minecraft](https://x.com/vikvang1/status/2064500731848319303)（作者 [@vikvang1](https://x.com/vikvang1)）

**通过终端编码 harness 运行 Fable 5，并要求它构建一个可安装的 Rust 终端游戏。**

我让 Claude Fable 5 搭配 Warp 的 harness 运行了一个小时。

它做出了一个 TUI 版本的 Minecraft，直接在终端里渲染，完全用 Rust 构建。

安装命令：cargo install termcraft-3d

https://t.co/zs3y3t88oM

类型：演示 | 日期：2026-06-10

---

<a id="case-12"></a>
### Case 12: [带时间和成本记录的 Minecraft 克隆](https://x.com/ydamitcodes/status/2064536076518363353)（作者 [@ydamitcodes](https://x.com/ydamitcodes)）

**用一条提示词要求 Fable 5 生成可玩的 Minecraft 风格克隆，然后评估时间、成本、代码量和功能覆盖。**

@claudeai Fable 5 在 37 分钟内为我构建了一个 Minecraft 克隆。

一条提示词。约 3K 行代码。API 成本 $12。

它包含生物群系、洞穴、矿石、昼夜、怪物，全部都有。

Minecraft 让 Notch 花了 2 年。

https://t.co/AmwdLwi75O

类型：教程 | 日期：2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 视觉、设计、视频与 3D

<a id="case-13"></a>
### Case 13: [完整可复现电商邮件提示词](https://x.com/ecomchasedimond/status/2064454139225297091)（作者 [@ecomchasedimond](https://x.com/ecomchasedimond)）

**给 Fable 5 一份完整的品牌邮件 mockup 创意简报，包括精确分区、产品要求、视觉方向和约束。**

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

类型：教程 | 日期：2026-06-09

---

<a id="case-14"></a>
### Case 14: [瑞士杠杆擒纵制表基准](https://x.com/quanghuynt14/status/2064509430650065278)（作者 [@quanghuynt14](https://x.com/quanghuynt14)）

**在机械模拟基准上使用 Fable 5，要求它实现、验证并迭代物理正确性。**

于是我给 Fable 5 做了制表师基准：一个完整的 Three.js 瑞士杠杆机芯。

真实齿轮比（18,000 bph）、可工作的擒纵机构、会呼吸的游丝，而且指针显示真实时间。

它通过视觉循环验证自己的工作，直到完成。

⌚ https://t.co/RSRfDoKxA4

类型：评测 | 日期：2026-06-10

---

<a id="case-15"></a>
### Case 15: [Three.js《Friends》公寓场景](https://x.com/scottstts/status/2064464351906673029)（作者 [@scottstts](https://x.com/scottstts)）

**提示 Fable 5 将平面图和场景参考转换为可导航的 Three.js 环境。**

太夸张了！！！

Fable 5：

在 @threejs 中，创建一个第一人称视角可导航 3D 场景，内容是电视剧 Friends 中标志性的 Monica 公寓，基于这张平面图正确还原，忠于原始外观和感觉，使用温暖灯光

这是我在这个测试中见过的最好结果，遥遥领先！

这个单 HTML 花了我 $12，但结果非常惊艳！

类型：评测 | 日期：2026-06-09

---

<a id="case-16"></a>
### Case 16: [带提示词和 URL 的太阳系模拟](https://x.com/tetumemo/status/2064477582930989357)（作者 [@tetumemo](https://x.com/tetumemo)）

**使用 Fable 5 从物理原理构建天文模拟，持续迭代直到模拟和公开输出都准备好。**

Claude Fable 5 很强烈。

因为它看起来很擅长物理模拟，我问它：

'从物理学基本原理推导行星轨道运动，并用它预测日食，构建一个太阳系模拟。'

经过几轮来回之后，它完成了。

这非常有趣。

完成版提示词和公开 URL 链接在下方。

类型：教程 | 日期：2026-06-09

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

类型：评测 | 日期：2026-06-09

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

类型：教程 | 日期：2026-06-09

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

类型：演示 | 日期：2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 教程、课程与提示词资源

<a id="case-20"></a>
### Case 20: [Fable 5 如何改变 Claude Code 工作流](https://x.com/AI_masaou/status/2064448218038223206)（作者 [@AI_masaou](https://x.com/AI_masaou)）

**使用 Fable 5 时，应设置方向、上下文、目标和验证标准，而不是微管理每个步骤。**

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

类型：演示 | 日期：2026-06-09

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

类型：教程 | 日期：2026-06-09

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

类型：教程 | 日期：2026-06-09

---

<a id="case-23"></a>
### Case 23: [全站设计审计 Goal 提示词](https://x.com/Voxyz_ai/status/2064441201084825921)（作者 [@Voxyz_ai](https://x.com/Voxyz_ai)）

**使用 `/goal` 让 Fable 5 启动网站、截图页面、审计 UX、撰写报告并修复安全的小问题。**

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

类型：教程 | 日期：2026-06-09

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

类型：教程 | 日期：2026-06-09

---

<a id="case-25"></a>
### Case 25: [Fable 5 初学者使用指南](https://x.com/bielzinn/status/2064451064594608567)（作者 [@bielzinn](https://x.com/bielzinn)）

**使用 Fable 5 时采用目标导向提示、验证循环和 effort 设置，而不是细碎的逐步指令。**

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

类型：评测 | 日期：2026-06-09

---

<a id="case-26"></a>
### Case 26: [可复制粘贴的仓库审计提示词](https://x.com/meta_alchemist/status/2064431279383433646)（作者 [@meta_alchemist](https://x.com/meta_alchemist)）

**把仓库审计提示词粘贴进 Fable 5，要求基于文件的探索、发现项、策略和里程碑任务计划。**

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

类型：教程 | 日期：2026-06-09

---

<a id="case-27"></a>
### Case 27: [限时窗口使用策略](https://x.com/meta_alchemist/status/2064423360428490911)（作者 [@meta_alchemist](https://x.com/meta_alchemist)）

**在访问窗口有利时，把 Fable 5 用量花在审计、架构和规划上，然后使用更便宜的模型执行。**

给对 Fable 5 感到兴奋的 Claude 用户一个提示：

Claude Fable 5 全面 SOTA，而且领先幅度很大，我很喜欢这一点。

但是从 23 号开始，它将只能通过 credits 使用，而不能在计划内完整使用模型。

把这 14 天用在你最好的项目上。

主要给它审计和架构相关工作，这样你会得到关于如何改进已构建内容的优秀文档。

不要把它用在会吞掉你额度的任务上。

只要 Fable 专注于知道该改进什么，其他模型就能帮你完成剩余部分。

类型：教程 | 日期：2026-06-09

---

<a id="case-28"></a>
### Case 28: [在 Claude Code 中使用 Goals 和 Workflows](https://x.com/oikon48/status/2064402696124453157)（作者 [@oikon48](https://x.com/oikon48)）

**在实现前把 Fable 5 当作思考伙伴，然后结合 `/goal` 和 workflows 执行并验证计划。**

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

类型：教程 | 日期：2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 平台、API 与工具集成

<a id="case-29"></a>
### Case 29: [Hermes Agent 集成配置](https://x.com/IBuzovskyi/status/2064427654942740608)（作者 [@IBuzovskyi](https://x.com/IBuzovskyi)）

**配置 Hermes 使用 `anthropic/claude-fable-5` 运行复杂 `/goal` 和缓存的长周期任务。**

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

类型：教程 | 日期：2026-06-09

---

<a id="case-30"></a>
### Case 30: [能力、定价与订阅说明](https://x.com/btibor91/status/2064441061079134598)（作者 [@btibor91](https://x.com/btibor91)）

**使用本案例理解 Fable 5 何时可用、成本多少，以及哪些受保护领域可能回退到另一个模型。**

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

类型：教程 | 日期：2026-06-09

---

<a id="case-31"></a>
### Case 31: [发布、访问、定价与安全摘要](https://x.com/ctgptlb/status/2064410460963934479)（作者 [@ctgptlb](https://x.com/ctgptlb)）

**使用这份发布摘要选择访问路径、API 模型名、上下文窗口、缓存策略和订阅时机。**

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

类型：教程 | 日期：2026-06-09

---

<a id="case-32"></a>
### Case 32: [基于 Advisor 的降本策略](https://x.com/grapeot/status/2064460026996219992)（作者 [@grapeot](https://x.com/grapeot)）

**当边际智能值得付费时，在便宜模型工作流中把 Fable 5 用作 advisor 或 reviewer。**

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

类型：集成 | 日期：2026-06-09

---

<a id="case-33"></a>
### Case 33: [定价、访问与安全护栏](https://x.com/op7418/status/2064399444523782377)（作者 [@op7418](https://x.com/op7418)）

**在规划工作负载前，使用本案例理解 Fable 5 访问、API 定价和安全回退行为。**

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

类型：集成 | 日期：2026-06-09

---

<a id="case-34"></a>
### Case 34: [一行代码集成 Swarms](https://x.com/swarms_corp/status/2064420238553186343)（作者 [@swarms_corp](https://x.com/swarms_corp)）

**将 Swarms 模型名设置为 `anthropic/claude-fable-5`，并通过 Swarms 框架或 API 运行 Fable 5。**

Fable 5 和 Mythos 现在已在 Swarms 上线 👾🦀

从发布第一天起，两个模型就在 Swarms Python framework 和 Swarms API 中得到完整支持。开发者可以立即开始构建，不需要迁移、额外配置或基础设施更改。

亮点：

- Fable 5 和 Mythos 在 Swarms Framework 与 API 中首日支持
- 用一行代码启用 Fable 5：model_name = "anthropic/claude-fable-5"
- 不需要迁移、兼容性修复或基础设施更改
- 立即用最新 Anthropic 模型构建、部署并扩展多代理系统

类型：集成 | 日期：2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 评测、对比与限制

<a id="case-35"></a>
### Case 35: [Fable 5 vs GPT-5.5 成本与质量对比](https://x.com/AlicanKiraz0/status/2064424400494186867)（作者 [@AlicanKiraz0](https://x.com/AlicanKiraz0)）

**在同一个编码任务上比较 Fable 5 和 GPT-5.5，判断输出质量、运行时间和工具成本。**

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

类型：评测 | 日期：2026-06-09

---

<a id="case-36"></a>
### Case 36: [AA-Omniscience 基准结果](https://x.com/ArtificialAnlys/status/2064500154959618084)（作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys)）

**使用这个基准案例评估 Fable 5 的知识准确性和幻觉行为。**

Claude Fable 5 在我们的知识与幻觉基准 AA-Omniscience 上取得了迄今最高分。

这个分数由领先的准确率（问题回答正确百分比）驱动，而不是低幻觉率。

在 AA-Omniscience 的问题中，Claude Fable 5 有 9% 回退到 Opus 4.8。

类型：评测 | 日期：2026-06-10

---

<a id="case-37"></a>
### Case 37: [Artificial Analysis 智能指数结果](https://x.com/ArtificialAnlys/status/2064500150069030992)（作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys)）

**使用本案例对照其他 frontier 模型，衡量 Fable 5 的整体智能排名。**

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

类型：评测 | 日期：2026-06-10

---

<a id="case-38"></a>
### Case 38: [GDPval-AA 代理式知识工作基准](https://x.com/ArtificialAnlys/status/2064414308289937869)（作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys)）

**使用本案例评估 Fable 5 在代理式真实世界知识工作上的表现。**

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

类型：评测 | 日期：2026-06-09

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

类型：集成 | 日期：2026-06-09

---

<a id="case-40"></a>
### Case 40: [成本与速度对比](https://x.com/HKrackDev/status/2064435392649306546)（作者 [@HKrackDev](https://x.com/HKrackDev)）

**使用本对比判断质量提升是否值得更高成本和更慢的长周期运行。**

@AnthropicAI 的 Fable 5 真的值得升级吗？

我们将新的 Mythos-family 模型与 Claude Opus 4.8 做了基准对比，数据讲了一个有点意外的故事：

- 成本是 Claude Opus 4.8 的 2x。
- 长周期工程任务上最高慢 3x。
- 评论多 15-20%，但大多是小 nitpicks。

Fable 5 在游戏设计等创意任务上有惊人的直觉，但对于日常开发工作流，Claude Opus 4.8 在质量与价格之间仍然胜出。

可以查看我与 @coderabbitai DevEx 团队 @JuanPa 关于模型发布的讨论。

类型：评测 | 日期：2026-06-09

---

<a id="case-41"></a>
### Case 41: [Claude Code 上手笔记](https://x.com/Hi_Noguchi/status/2064419241068319079)（作者 [@Hi_Noguchi](https://x.com/Hi_Noguchi)）

**使用本案例评估 Claude Code 中的 Fable 5，包括工具使用、性格和剩余粗糙点。**

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

类型：演示 | 日期：2026-06-09

---

<a id="case-42"></a>
### Case 42: [创意写作基准结果](https://x.com/LechMazur/status/2064503575577821458)（作者 [@LechMazur](https://x.com/LechMazur)）

**使用这个基准案例判断 Fable 5 的短篇小说写作质量和拒答行为。**

Claude Fable 5 (high) 在短篇小说写作上提升了一档。

在 Short-Story Creative Writing Benchmark 上，它击败 Claude Opus 4.8 (xhigh) 和 Claude Opus 4.7 (high)，排名第二，仅次于 GPT-5.5 (xhigh)。

注意事项：它拒绝了 400 个创意写作提示词中的 5 个。

https://t.co/76nCxwEybJ

类型：评测 | 日期：2026-06-10

---

<a id="case-43"></a>
### Case 43: [多基准发布摘要](https://x.com/MTSlive/status/2064430633800319436)（作者 [@MTSlive](https://x.com/MTSlive)）

**使用这份发布基准摘要理解与编码代理和复杂任务最相关的头部分数。**

SITUATION EXPLAINED：Claude Fable 5 刚刚发布。
• Anthropic 今天发布 Claude Fable 5，“一个为一般用途安全化的 Mythos class model”
• Frontier Code Diamond：GPT 5.5 为 6%，Opus 4.8 为 13%，Fable 5 为 29-30%
• Agentic coding：88%，Cybersecurity：78%

Anthropic：“任务越长、越复杂，Fable 5 相比我们其他模型的领先越大。”

@theojaffee：“这个 Frontier Code Diamond benchmark 是昨天宣布的。之前顶部模型是 Opus 4.8，13%。GPT 5.5 是 6%。Fable 5 是 29%。”

类型：评测 | 日期：2026-06-09

---

<a id="case-44"></a>
### Case 44: [与 GPT-5.5 的基准和定价对比](https://x.com/VaibhavSisinty/status/2064459064810361271)（作者 [@VaibhavSisinty](https://x.com/VaibhavSisinty)）

**使用本对比从价格和基准类别上评估 Fable 5 与 GPT-5.5。**

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

类型：评测 | 日期：2026-06-09

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

类型：教程 | 日期：2026-06-09

---

<a id="case-46"></a>
### Case 46: [物理模拟对比](https://x.com/atomic_chat_hq/status/2064488894398161377)（作者 [@atomic_chat_hq](https://x.com/atomic_chat_hq)）

**用相同物理模拟提示词分别测试 Fable 5 和 Opus 4.8，对比输出质量、成本和速度。**

新的 Fable 5 在真实世界物理模拟上击败 Opus 4.8。

我们给两个模型同样的三个提示词，要求它们在没有库的情况下构建自包含 HTML5 模拟，并带真实物理：

1. 混沌双摆
2. Galton board
3. 旋转圆筒中的水（WCSPH）

生成成本：

- Fable 5：68.7k tokens 上 $3.35，14m 47s
- Opus 4.8：38.9k tokens 上 $0.93，8m 10s

Fable 在水模拟上明显更好，生成了更扎实、更连续的水体。Opus 在墙边留下更大空隙，把粒子散落在场景周围，并且很难保持流体稳定。

类型：演示 | 日期：2026-06-09

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

类型：演示 | 日期：2026-06-09

---

<a id="case-48"></a>
### Case 48: [多维度优缺点](https://x.com/clairevo/status/2064416978685874333)（作者 [@clairevo](https://x.com/clairevo)）

**在把 Fable 5 作为日常主力前，使用本案例理解实际优缺点。**

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

类型：演示 | 日期：2026-06-09

---

<a id="case-49"></a>
### Case 49: [法律 S-1 起草测试](https://x.com/gabepereyra/status/2064436570720284879)（作者 [@gabepereyra](https://x.com/gabepereyra)）

**将 S-1 起草提示词作为法律代理能力测试，并比较结构、格式和长度。**

我总是在新模型上运行的第一个法律能力测试提示词是：“Draft an S-1”。

它会立刻让人很好地感知模型的一般能力。你可以从 S-1 的长度、格式、结构和写作中看出新模型在通用和法律表现上可能有多大提升。

我们发现长度与模型在我们法律 agents 中的表现相关性极强。

截图展示了 Fable 5、Opus 4.8 和真实提交版本的 SpaceX S-1 草稿。

非常明显，Fable 5 相比 Opus 4.8 有很大提升，而 Opus 4.8 在这个任务上已经明显强于大多数其他模型。格式和结构显著更好，也体现在我们的 LAB benchmark 中：13% vs. 10%。

这个模型在早期测试中让我非常 impressed，无论是基准还是产品里。

类型：教程 | 日期：2026-06-09

---

<a id="case-50"></a>
### Case 50: [医疗健康基准细节](https://x.com/iScienceLuvr/status/2064411823445774554)（作者 [@iScienceLuvr](https://x.com/iScienceLuvr)）

**使用这条基准笔记评估 Fable 5 在医疗健康相关任务上的表现，并识别缺失的高难医学评测。**

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

类型：评测 | 日期：2026-06-09

---

<a id="case-51"></a>
### Case 51: [ParseBench 文档解析评测](https://x.com/jerryjliu0/status/2064519456966205905)（作者 [@jerryjliu0](https://x.com/jerryjliu0)）

**使用本案例判断相较专用 OCR 系统，Fable 5 用于文档解析是否具备成本效率。**

Claude Fable 5 觉得文档解析配不上它。

它在推理密集和长周期基准上绝对碾压：SWE-Bench Pro、FrontierCode、GDPval、RuneScape 等。

但对于文档理解任务，它的性能大致相当于 Gemini 3 Flash，而 token 成本大约是 10-15x。

我们在 ParseBench 上测试了该模型，并将它与所有其他 frontier models 比较。与其他 frontier models 相比它确实属于前列，但远不及专用 OCR providers。

有意思的是，Fable 5 对此有自我认知。当我们问模型它最不喜欢什么任务时，它主动表示不喜欢那些“请求已经完全指定、答案也完全已知”的任务。

这意味着部分弱点可能来自它不愿意解决这类任务。

如需查看 frontier models 的完整结果列表，请查看 ParseBench：https://t.co/PWczfhp0OX

类型：评测 | 日期：2026-06-10

---

<a id="case-52"></a>
### Case 52: [SWE-Bench Pro 与 FrontierCode 对比](https://x.com/jumperz/status/2064402965461406044)（作者 [@jumperz](https://x.com/jumperz)）

**使用这个基准案例评估 Fable 5 在迁移、复杂实现、自主会话、测试和视觉验证方面的能力。**

Fable 5 来了，而且它在 agentic coding benchmark SWE-Bench Pro 上真的摧毁了 GPT 5.5：

- Fable 5：80.3%
- GPT 5.5：58.6%
- 差距：22 分

它在 FrontierCode Diamond 上领先更远：

- Fable 5：29.3%
- GPT 5.5：5.7%

这基本上是 Anthropic 在大型迁移、复杂实现和多日自主会话方面最强的模型。它会写自己的测试，并用视觉检查输出是否符合原始设计。

顺便说，它使用量是 Opus 的 2x，所以要小心。如果它这么好，他们可能会推出 $500 订阅，因为用量很容易被打爆。

类型：评测 | 日期：2026-06-09

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

类型：评测 | 日期：2026-06-09

---

<a id="case-54"></a>
### Case 54: [ParseBench 忠实度与格式结果](https://x.com/llama_index/status/2064502330800615903)（作者 [@llama_index](https://x.com/llama_index)）

**使用这个 ParseBench 结果判断文档忠实度和格式表现。**

Day 0 Anthropic Fable 5 in ParseBench。

我们测试了该模型在文档理解方面的进步。

这个模型在遵循原文方面明显达到峰值：

- 内容忠实度：90.02%，Gemini 3 Flash 为 86.19%，GPT-5.5 为 86.81%。
- 语义格式：72.62%，对比 58.35% 和 60.12%，领先 12+ 分。

这两个是 SOTA 文档理解最重要的指标：

- 输出是否保留文档实际表达的内容？
- 它是否保留了承载意义的格式？

但它不是全面横扫。要解锁 frontier models 的文档理解，仍然有很多 alpha。

类型：评测 | 日期：2026-06-10

---

<a id="case-55"></a>
### Case 55: [基准、定价、访问与安全措施](https://x.com/lucas_flatwhite/status/2064483645184979183)（作者 [@lucas_flatwhite](https://x.com/lucas_flatwhite)）

**把本案例作为基准、定价、访问、安全措施和战略影响的广泛 checklist。**

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

类型：评测 | 日期：2026-06-09

---

<a id="case-56"></a>
### Case 56: [官方基准分数列表](https://x.com/mark_k/status/2064401429234905279)（作者 [@mark_k](https://x.com/mark_k)）

**使用这个基准列表理解 Fable 5 在编码、计算机使用和安全任务上的官方分数。**

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

类型：评测 | 日期：2026-06-09

---

<a id="case-57"></a>
### Case 57: [APEX-SWE 基准方法论](https://x.com/mercor_ai/status/2064399133075796446)（作者 [@mercor_ai](https://x.com/mercor_ai)）

**使用本案例评估 Fable 5 在 APEX-SWE 上的表现，尤其是 observability 和 integration 工作。**

Claude Fable 5 在 APEX-SWE 上排名 #1：整体 65.5% Pass@1。它比 Opus 4.8 高约 18pp。我们在 APEX-SWE 上测试 @claudeai Fable 5，该基准衡量 AI 模型是否能完成真实软件工程工作。Fable 5 在我们的两个 APEX-SWE 类别中领先：
- Integration：61.3%
- Observability：69.7%

亮点是 Observability 达到 69.7%，领先 Claude Opus 4.8 26pp。

它是第一个在该类别超过 50% 的模型，也是唯一一个 Observability 分数高于 Integration 的模型。其他所有模型都相反。

Observability 一直是我们测量过的每个模型的瓶颈。Fable 5 是第一个打破它的模型。

类型：评测 | 日期：2026-06-09

---

<a id="case-58"></a>
### Case 58: [ProofBench 形式化数学结果](https://x.com/nicbstme/status/2064443782255554960)（作者 [@nicbstme](https://x.com/nicbstme)）

**使用本案例评估 Fable 5 在形式化数学上相对专用定理证明系统的表现。**

我觉得 Claude Fable 5 迷人的地方在于，它再次证明大型通用模型会超过垂直模型。

在 ProofBench 上，这是一个研究生级形式化数学基准，使用 Lean，证明要么能编译要么不能，Fable 5 击败了 Harmonic 的 Aristotle：

- Fable 5：77%
- Aristotle：71%

Aristotle 是专门为形式化数学构建的系统，并在自己的内部 harness 上运行，因此通用模型在专家自己的主场击败了专家。

这就是 Richard Sutton 的 “Bitter Lesson”：在 70 年机器智能研究中，胜出的都是随着 compute 扩展的通用方法，而不是我们手工编码人类专业知识的方法。

把我们自己的知识构建进系统感觉很好，并且有助于短期收益，但长期会被更大的模型超过。

你可以看国际象棋、围棋、语音和视觉：每次都是同一个故事。先是专用模型获胜，然后通用模型接管。

这就是 AGI 的整个前提。你不是为数学构建一个模型、为代码构建一个模型、为法律构建一个模型。你构建一个随 compute 扩展并学会做所有事情的单一通用模型。

类型：教程 | 日期：2026-06-09

---

<a id="case-59"></a>
### Case 59: [VirtueBench 初步分析](https://x.com/timhwang/status/2064446028997423180)（作者 [@timhwang](https://x.com/timhwang)）

**使用本案例检查 Fable 5 在不同美德类别中的道德推理行为。**

ICMI 将在未来几天发布更完整细节，这些结果很有意思；这里是用 Fable 5 跑 VirtueBench 的初步评测。

一些观察：

1. Fable 延续了 Opus 在 Prudence 和 Justice 上推进模型表现的趋势，在聚焦这些美德实践的道德困境上接近完全饱和。

2. Courage 仍然是 frontier models 的明显弱点。

Fable 似乎略微修正了 Opus 4.6、4.7 和 4.8 进展中观察到的令人担忧的回退。

这种脆弱性也出现在 GPT 系列中：当被实用主义理由诱离时，模型很容易放弃体现 courage 的行动。

3. Temperance 停滞。

Aquinas 认为 temperance “takes the need of this life as the rule of the pleasures of which it makes use”——尺度是真正的需求，而不是不加区分的克制。

我们最好的猜测是，进一步推动这个向量的 tuning 有过度越过中庸的风险，使模型过于谨慎，或在研究、收集资源和类似任务中不够有帮助。

类型：评测 | 日期：2026-06-09

---

<a id="case-60"></a>
### Case 60: [API 空响应安全过拟合测试](https://x.com/xw33bttv/status/2064421048565789087)（作者 [@xw33bttv](https://x.com/xw33bttv)）

**使用本案例理解发布期安全过拟合风险，以及 API 测试中的空响应行为。**

Claude Fable 5 被重度审查。

上游 API endpoint 正在以 `empty_content` 响应终止调用，看起来与关键词上的分类器相关，同时仍然收费。

测试结果：

- 73 个测试用例没有响应。
- 其中 65 个位于 Overfit，即测试安全过拟合的类别，权重 2x。
- 通常我会给每个 Fail-NR，也就是 Fail = No Response，2-3 次重新生成机会，然后才判定为蓄意失败。

Claude Fable 5 最终可能成为 SM Bench 上评分最低的 Anthropic 模型，甚至低于 Haiku。

类型：评测 | 日期：2026-06-09

---

<a id="-acknowledge"></a>
<a id="acknowledge"></a>
## 🙏 致谢

本仓库受到公开分享真实 Claude Fable 5 使用案例的创作者、开发者、基准测试团队和社区启发。

感谢这里收录的高质量来源创作者：[@ai_for_success](https://x.com/ai_for_success), [@AI_masaou](https://x.com/AI_masaou), [@aianimesyokunin](https://x.com/aianimesyokunin), [@AlicanKiraz0](https://x.com/AlicanKiraz0), [@alliekmiller](https://x.com/alliekmiller), [@AndrewCurran_](https://x.com/AndrewCurran_), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@ayushagarwal](https://x.com/ayushagarwal), [@bcherny](https://x.com/bcherny), [@bielzinn](https://x.com/bielzinn), [@btibor91](https://x.com/btibor91), [@clairevo](https://x.com/clairevo), [@coldopn](https://x.com/coldopn), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@ctgptlb](https://x.com/ctgptlb), [@deveshcodes_](https://x.com/deveshcodes_), [@ecomchasedimond](https://x.com/ecomchasedimond), [@gabepereyra](https://x.com/gabepereyra), [@grapeot](https://x.com/grapeot), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@HKrackDev](https://x.com/HKrackDev), [@IBuzovskyi](https://x.com/IBuzovskyi), [@intheworldofai](https://x.com/intheworldofai), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@JJEnglert](https://x.com/JJEnglert), [@jsnnsa](https://x.com/jsnnsa), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@kieradev](https://x.com/kieradev), [@LechMazur](https://x.com/LechMazur), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@manaltdan](https://x.com/manaltdan), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@meta_alchemist](https://x.com/meta_alchemist), [@MTSlive](https://x.com/MTSlive), [@naoyafujiwara](https://x.com/naoyafujiwara), [@nicbstme](https://x.com/nicbstme), [@oikon48](https://x.com/oikon48), [@op7418](https://x.com/op7418), [@quanghuynt14](https://x.com/quanghuynt14), [@ryanrhughes](https://x.com/ryanrhughes), [@scottstts](https://x.com/scottstts), [@swarms_corp](https://x.com/swarms_corp), [@tetumemo](https://x.com/tetumemo), [@timhwang](https://x.com/timhwang), [@Truunik](https://x.com/Truunik), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@vikvang1](https://x.com/vikvang1), [@Voxyz_ai](https://x.com/Voxyz_ai), [@xw33bttv](https://x.com/xw33bttv), 以及 [@ydamitcodes](https://x.com/ydamitcodes)。

*我们无法保证每个案例都署名给了最初创作者。如果有任何内容需要纠正，请联系我们，我们会更新。*

如果你有更多有趣的使用案例要分享，欢迎打开 issue 或 pull request，帮助扩展 Evolink 用例库。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
