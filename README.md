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

## 🍌 Introduction

Welcome to the Claude Fable 5 high-signal usecase repository.

**We collect real-world usage cases, tutorials, integrations, and evaluations for Claude Fable 5, curated from public demos and creator communities.**

This English source README focuses on high-signal cases with concrete workflows, prompts, demos, integrations, benchmark evidence, or practical limits.

Most cases are curated from X/Twitter posts and public demos. Each case title links back to the original source and each author handle links to the creator profile.

Try it on Evolink: [Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

## 📊 Overview

- **88 original Fable 5 cases plus 218 community cases; 306 cases total.**
- Covers coding agents, long-running automation, games, visual design, 3D simulations, knowledge work, tutorials, API integrations, benchmarks, pricing, and launch limitations.
- Each case includes the original source, creator attribution, a concise takeaway, evidence type, and publication date.
- Use this repo to find practical workflows, compare strengths and limits, discover reproducible prompts, and follow integration examples.

> [!NOTE]
> The collection favors concrete evidence over hype: reproducible prompts, shipped demos, benchmark methods, integration notes, cost data, and clearly stated caveats.

<a id="-quick-api-access"></a>
## EvoLink Quick Start

Use Claude Fable 5 through the Evolink-compatible Messages API for coding agents, review loops, and long-context workflow planning.

<p align="center">
  <a href="https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5"><strong>Model Page</strong></a> &nbsp;·&nbsp;
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5"><strong>Docs</strong></a> &nbsp;·&nbsp;
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5"><strong>API Key</strong></a> &nbsp;·&nbsp;
  <a href="docs/coding-agent-use-cases.md"><strong>Workflow Notes</strong></a> &nbsp;·&nbsp;
  <a href="api-examples"><strong>API Examples</strong></a> &nbsp;·&nbsp;
  <a href="https://github.com/EvoLinkAI/evolink-model-router-examples"><strong>Router Examples</strong></a> &nbsp;·&nbsp;
  <a href="https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook"><strong>Use Cases</strong></a>
</p>

```bash
export EVOLINK_API_KEY="your_key_here"

curl --request POST \
  --url https://direct.evolink.ai/v1/messages \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "claude-fable-5",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "Review this implementation plan for hidden engineering risks."
      }
    ]
  }'
```

## 📑 Menu

| Section | Cases |
|---|---|
| [💻 Coding and Code Generation](#coding-and-code-generation) | Case 1-6 |
| [🤖 Agents and Long-Running Automation](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 Games and Interactive Demos](#games-and-interactive-demos) | Case 9-12 |
| [🎨 Visual, Design, Video, and 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 Documents, Knowledge Work, and Research](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 Tutorials, Courses, and Prompt Resources](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 Platform, API, and Tool Integration](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 Evaluations, Comparisons, and Limits](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | Credits and correction policy |

### [💻 Coding and Code Generation](#coding-and-code-generation)

| Case | What it shows | Type |
|---|---|---|
| [Cursor Multi-Stage Workflow](#case-1) | Use Fable 5 as the plan-review and critique step inside a multi-model Cursor workflow, then hand implementation and revision back to cheaper or specialized models. | Evaluation |
| [Recreating GitHub from a Screenshot](#case-2) | Paste a product screenshot into an agentic coding tool and ask Fable 5 to recreate the interface with working functionality. | Demo |
| [One-Prompt Black Hole Simulation](#case-3) | Give Fable 5 one detailed creative-coding prompt and ask it to produce a self-contained Three.js physics visualization. | Tutorial |
| [One-Shot macOS-Style Web OS](#case-4) | Ask Fable 5 for a complete single-file web OS and let it build the UI shell, apps, interactions, audio, and embedded game behavior in one pass. | Tutorial |
| [Building Spawn 5.0 with 1,687 Prompts](#case-5) | Use Fable 5 as a long-session engineering partner across many prompts, with the human shifting from architecture to judging output quality. | Tutorial |
| [Large Pull Request Review with Findings](#case-6) | Point Fable 5 at a large pull request and ask it to review correctness, false positives, real bugs, and polish issues. | Demo |

### [🤖 Agents and Long-Running Automation](#agents-and-long-running-automation)

| Case | What it shows | Type |
|---|---|---|
| [Long-Horizon Relay Workflow Review](#case-7) | Use Fable 5 for ambitious long-horizon work: site rebuilds, programmatic content pipelines, voice matching, security review, and final quality checks. | Evaluation |
| [Diagnosing an Infrastructure Outage and Opening a Fix PR](#case-8) | Give Fable 5 access to infra clues such as logs, database errors, and image digests, then ask it to diagnose the outage and prepare the fix. | Evaluation |

### [🎮 Games and Interactive Demos](#games-and-interactive-demos)

| Case | What it shows | Type |
|---|---|---|
| [Finger-Tracking Dino Runner](#case-9) | Ask Fable 5 to build a browser game that uses finger tracking as the input mechanic. | Demo |
| [Two-Sentence Racing Game Build](#case-10) | Give Fable 5 a very short game prompt and let it generate maps, modes, music, UI, and game assets in one run. | Tutorial |
| [Installable Terminal Minecraft in Rust](#case-11) | Run Fable 5 through a terminal coding harness and ask it to build an installable Rust terminal game. | Demo |
| [Minecraft Clone with Time and Cost](#case-12) | Use one prompt to ask Fable 5 for a playable Minecraft-style clone, then evaluate time, cost, code volume, and feature coverage. | Tutorial |

### [🎨 Visual, Design, Video, and 3D](#visual-design-video-and-3d)

| Case | What it shows | Type |
|---|---|---|
| [Full Reproducible Ecommerce Email Prompt](#case-13) | Give Fable 5 a complete creative brief for a brand email mockup, including exact sections, product requirements, visual direction, and constraints. | Tutorial |
| [Swiss Lever Watchmaker Benchmark](#case-14) | Use Fable 5 on a mechanical simulation benchmark and ask it to implement, verify, and iterate on physical correctness. | Evaluation |
| [Three.js Friends Apartment Scene](#case-15) | Prompt Fable 5 to turn a floor plan and scene reference into a navigable Three.js environment. | Evaluation |
| [Solar System Simulation with Prompt and URL](#case-16) | Use Fable 5 to build an astronomy simulation from physics principles, iterating until the simulation and public output are ready. | Tutorial |

### [📚 Documents, Knowledge Work, and Research](#documents-knowledge-work-and-research)

| Case | What it shows | Type |
|---|---|---|
| [Stripe and Scientific Workflow Evidence](#case-17) | Use this as evidence for enterprise migration and scientific workflow claims, not as a copy-paste prompt. | Evaluation |
| [Policy Memo and Track-Changes Workflows](#case-18) | Use Fable 5 for long-form qualitative document work: track changes, comment triage, and transcript-driven edits. | Tutorial |
| [Deep Research Prompt and Output](#case-19) | Ask Fable 5 a research-style question and evaluate whether it can produce a structured, historically grounded long answer. | Demo |

### [🧭 Tutorials, Courses, and Prompt Resources](#tutorials-courses-and-prompt-resources)

| Case | What it shows | Type |
|---|---|---|
| [How Fable 5 Changes Claude Code Workflows](#case-20) | Use Fable 5 by setting direction, context, goals, and verification criteria instead of micromanaging every step. | Demo |
| [One-Billion-Token Review and Routing Strategy](#case-21) | Use Fable 5 for frontier planning and review, then route high-volume implementation to cheaper models. | Tutorial |
| [Defensive Device Hardening Prompt](#case-22) | Run a step-by-step defensive hardening prompt where Fable 5 inventories devices, gives exact checks, and waits for verification. | Tutorial |
| [Full-Site Design Audit Goal Prompt](#case-23) | Use `/goal` to make Fable 5 boot a site, screenshot pages, audit UX, write a report, and fix safe small issues. | Tutorial |
| [Long-Form Creative Workflow Division](#case-24) | Use Fable 5 to design stable formats and examples, then hand that structure to another generation system for domain-specific output. | Tutorial |
| [Beginner Guide to Using Fable 5](#case-25) | Use Fable 5 with goal-oriented prompts, verification loops, and effort settings instead of small step-by-step instructions. | Evaluation |
| [Copy-Paste Repository Audit Prompt](#case-26) | Paste the repository audit prompt into Fable 5 and ask for file-backed discovery, findings, strategy, and a milestone task plan. | Tutorial |
| [Limited-Window Usage Strategy](#case-27) | Spend Fable 5 usage on audit, architecture, and planning while the access window is favorable, then use cheaper models for execution. | Tutorial |
| [Using Goals and Workflows in Claude Code](#case-28) | Use Fable 5 as a thought partner before implementation, then combine `/goal` and workflows to execute and verify the plan. | Tutorial |

### [🔌 Platform, API, and Tool Integration](#platform-api-and-tool-integration)

| Case | What it shows | Type |
|---|---|---|
| [Hermes Agent Integration Setup](#case-29) | Configure Hermes to use `anthropic/claude-fable-5` for complex `/goal` runs and cached long-horizon tasks. | Tutorial |
| [Capabilities, Pricing, and Subscription Notes](#case-30) | Use this case to understand when Fable 5 is available, what it costs, and which guarded domains may fall back to another model. | Tutorial |
| [Launch, Access, Pricing, and Safety Summary](#case-31) | Use this launch summary to choose access route, API model name, context window, caching strategy, and subscription timing. | Tutorial |
| [Advisor-Based Cost Reduction Strategy](#case-32) | Use Fable 5 as an advisor or reviewer in a cheaper-model workflow when marginal intelligence is worth the cost. | Integration |
| [Pricing, Access, and Safety Guardrails](#case-33) | Use this case to understand Fable 5 access, API pricing, and safety fallback behavior before planning workloads. | Integration |
| [One-Line Swarms Integration](#case-34) | Set the Swarms model name to `anthropic/claude-fable-5` and run Fable 5 through the Swarms framework or API. | Integration |

### [📏 Evaluations, Comparisons, and Limits](#evaluations-comparisons-and-limits)

| Case | What it shows | Type |
|---|---|---|
| [Fable 5 vs GPT-5.5 Cost and Quality Comparison](#case-35) | Compare Fable 5 and GPT-5.5 on the same coding task to judge output quality, runtime, and tool cost. | Evaluation |
| [AA-Omniscience Benchmark Result](#case-36) | Use this benchmark case to evaluate Fable 5 on knowledge accuracy and hallucination behavior. | Evaluation |
| [Artificial Analysis Intelligence Index Result](#case-37) | Use this case to benchmark Fable 5's overall intelligence ranking against other frontier models. | Evaluation |
| [GDPval-AA Agentic Knowledge Work Benchmark](#case-38) | Use this case to evaluate Fable 5 on agentic real-world knowledge work. | Evaluation |
| [One-Week First Impressions and Pricing Mechanics](#case-39) | Use this first-impressions case to decide where Fable 5 is strongest, especially game design and systems planning. | Integration |
| [Cost and Speed Comparison](#case-40) | Use this comparison to decide whether the quality gain justifies higher cost and slower long-horizon runs. | Evaluation |
| [Claude Code Hands-On Notes](#case-41) | Use this case to evaluate Fable 5 inside Claude Code, including tool use, personality, and remaining rough edges. | Demo |
| [Creative Writing Benchmark Result](#case-42) | Use this benchmark case to judge Fable 5's short-fiction writing quality and refusal behavior. | Evaluation |
| [Multi-Benchmark Launch Summary](#case-43) | Use this launch benchmark summary to understand the headline scores most relevant to coding agents and complex tasks. | Evaluation |
| [Benchmark and Pricing Comparison with GPT-5.5](#case-44) | Use this comparison to evaluate Fable 5 against GPT-5.5 on price and benchmark categories. | Evaluation |
| [Field Notes with Practical Limitations](#case-45) | Use this field report to understand where Fable 5 feels meaningfully better and where it still has practical limits. | Tutorial |
| [Physics Simulation Comparison](#case-46) | Run identical physics simulation prompts against Fable 5 and Opus 4.8 to compare output quality, cost, and speed. | Demo |
| [Debugging Experience and Design Judgment](#case-47) | Use Fable 5 for debugging by asking it to measure, log, verify, and patch rather than simply guess. | Demo |
| [Multi-Dimensional Pros and Cons](#case-48) | Use this case to understand practical strengths and weaknesses before making Fable 5 a daily driver. | Demo |
| [Legal S-1 Drafting Test](#case-49) | Use an S-1 drafting prompt as a legal-agent capability test and compare structure, formatting, and length. | Tutorial |
| [Healthcare Benchmark Details](#case-50) | Use this benchmark note to evaluate Fable 5 on healthcare-related tasks and identify missing hard medical evals. | Evaluation |
| [ParseBench Document Parsing Evaluation](#case-51) | Use this case to decide whether Fable 5 is cost-effective for document parsing versus specialized OCR systems. | Evaluation |
| [SWE-Bench Pro and FrontierCode Comparison](#case-52) | Use this benchmark case to evaluate Fable 5 for migrations, complex implementations, autonomous sessions, tests, and visual verification. | Evaluation |
| [Qualitative Review of Long Problem Solving](#case-53) | Use this qualitative review to understand why Fable 5 is suited to longer, harder tasks while still requiring production review. | Evaluation |
| [ParseBench Faithfulness and Formatting Results](#case-54) | Use this ParseBench result to judge document faithfulness and formatting performance. | Evaluation |
| [Benchmarks, Pricing, Access, and Safeguards](#case-55) | Use this case as a broad checklist for benchmarks, pricing, access, safeguards, and strategic implications. | Evaluation |
| [Official Benchmark Score List](#case-56) | Use this benchmark list to understand Fable 5's official scores across coding, computer use, and security tasks. | Evaluation |
| [APEX-SWE Benchmark Methodology](#case-57) | Use this case to evaluate Fable 5 on APEX-SWE, especially observability and integration work. | Evaluation |
| [ProofBench Formal Math Result](#case-58) | Use this case to evaluate Fable 5 on formal math against specialized theorem-proving systems. | Tutorial |
| [VirtueBench Preliminary Analysis](#case-59) | Use this case to inspect Fable 5's moral-reasoning behavior across virtue categories. | Evaluation |
| [API Empty-Response Safety Overfit Test](#case-60) | Use this case to understand launch-time safety overfit risk and empty-response behavior in API testing. | Evaluation |
| [Fable Prompting Verification Guide](#case-61) | Use this prompting guide to shift from longer prompt hacks toward goal, context, constraints, tools, and verification loops. | Tutorial |
| [Istanbul Platform Game Reference Build](#case-62) | Use a reference sprite sheet plus one conversion instruction to test Fable 5 on a playable platform game. | Demo |
| [Business 3D City Dashboard](#case-63) | Use Fable 5 to turn a business workflow into a live 3D city dashboard concept. | Demo |
| [Three.js Hole Game One-Shot](#case-64) | Use Fable 5 to one-shot a 3D browser game prototype in Three.js. | Demo |
| [DeepSWE Score Comparison](#case-65) | Use this DeepSWE note to compare Fable 5 xHigh with GPT-5.5 xHigh on software-engineering benchmark performance. | Evaluation |
| [Repository Cost Comparison](#case-66) | Use this repository-analysis comparison to judge token price against human rework cost. | Evaluation |
| [Super Mario Game Token Cost](#case-67) | Use this single-shot game build to estimate Fable 5 output quality and token consumption. | Demo |
| [Claude Code Fallback Setting](#case-68) | Use this case to understand the Claude Code setting for switching models when a Fable 5 message is flagged. | Integration |
| [Namma Metro Simulator Build](#case-69) | Use this demo as a compact example of vibe-coding a public-transit simulator with Fable 5. | Demo |
| [Dusk Drive One-Prompt Game](#case-70) | Use this one-prompt driving-game case to evaluate Fable 5 on low-poly game prototyping without human edits. | Demo |
| [APEX-Agents Pass@1 Ranking](#case-71) | Use this APEX-Agents result to compare Fable 5 Max on multi-step autonomous tasks. | Evaluation |
| [Claude Model Selection Playbook](#case-72) | Use this model-selection playbook to reserve Fable 5 for the hardest Claude Code jobs. | Tutorial |
| [HermesWorld Automated Agent Loop](#case-73) | Use this case to study a hands-free Fable 5 loop that builds, tests, plays, and smoke-tests over days. | Integration |
| [McKinsey-Style Report Prompt Test](#case-74) | Use this document-generation prompt to evaluate consulting-report structure, charts, narrative, and risk analysis. | Tutorial |
| [Visible Safeguards Rollout](#case-75) | Use this official note to understand Fable 5 safeguard visibility, API refusal reasons, and Opus fallback behavior. | Integration |
| [Claude Code Model Matching Fix](#case-76) | Use this Claude Code changelog note to avoid Fable 5 model-name and context matching issues. | Integration |
| [Three Web Apps in Claude Code](#case-77) | Use this beginner coding demo to inspect Fable 5 inside Claude Code across multiple generated web apps. | Demo |
| [Rilable Open Source App Builder](#case-78) | Use this open-source app-builder case to study Fable 5 across iOS, web apps, sandboxes, and API-token cost. | Integration |
| [DeepSWE Coding Agent Index Debut](#case-79) | Use the refreshed Artificial Analysis index to compare Fable 5 on harder agentic coding tasks that avoid recycled public GitHub fixes. | Evaluation |
| [DataEmpire Web Analytics Game](#case-80) | Turn raw site analytics into a replayable game by asking Fable 5 to map visitors and milestones onto game entities. | Integration |
| [FrontierSWE 20-Hour Task Signal](#case-81) | Use FrontierSWE as evidence that Fable 5 can stay productive across very long engineering tasks, not just short bug-fix loops. | Evaluation |
| [KernelBench-Hard CUDA Records](#case-82) | Use Fable 5 for advanced CUDA kernel generation when you need low-level optimization, not just wrappers around existing libraries. | Evaluation |
| [Figma Capture Landing Page Clone](#case-83) | Capture a live competitor page into Figma layers and let Claude Code with Fable 5 rebuild the structure, copy, and brand system instead of guessing from screenshots. | Integration |
| [GTA 2 Clone in Two Hours](#case-84) | Combine Fable 5 code generation with separate asset tooling to build a playable 3D game quickly without hand-coding the whole stack. | Tutorial |
| [CloudWatch Log Triage Agent](#case-85) | Let a Fable 5-powered agent chew through very large service-log contexts, infer architecture, and then narrow in on specific faults. | Integration |
| [World Cup Predictor in Sandboxes](#case-86) | Put multiple frontier models behind isolated sandboxes and let them research live news, injuries, and yellow-card context for a public prediction app. | Integration |
| [WolfBench Refusal Cost Case](#case-87) | Treat refusal behavior as a real benchmark variable when pricing long autonomous runs on Fable 5. | Evaluation |
| [API Access Cutoff Tracker](#case-88) | Monitor availability with a script if your workflow depends on continued access to a frontier model that may be rate-limited or withdrawn without much notice. | Integration |



### [🆕 Fable 5.5 Community Demos](#fable-5-5-community-demos)

| Case | Type |
|---|---|
| [Code-Generated Fox Animation with Sound](#case-89) | Demo |
| [Animation from an Open Creative Brief](#case-90) | Demo |
| [Animated Construction Company Website](#case-91) | Demo |
| [Three.js Car Presentation](#case-92) | Demo |
| [Minecraft-Style Browser Game Demo](#case-93) | Demo |
| [Three.js Pelican Cycling Animation](#case-94) | Demo |
| [Pelican Bicycle SVG with Exact Prompt](#case-95) | Demo |
| [Galloping Zebra Animation Sample](#case-96) | Demo |
| [TradingView Indicator with Human Execution](#case-97) | Demo |
| [A dot becomes a short animated story](#case-98) | Demo |
| [Superman across changing art styles](#case-99) | Demo |
| [Human progress in an animated film with music](#case-100) | Demo |
| [Release-video comparison with Opus](#case-101) | Evaluation |
| [Connecting lyrics and an event visually](#case-102) | Demo |
| [Voxel character in a floating scene](#case-103) | Demo |
| [A 3D Rube Goldberg machine demo](#case-104) | Demo |
| [A 3D controller interface with sound and motion](#case-105) | Demo |
| [Comic characters presented with JavaScript](#case-106) | Demo |
| [Updraft: worlds, bosses, and a leaderboard](#case-107) | Demo |
| [Driving through a San Francisco map](#case-108) | Demo |
| [Writing prompts for a Seedance action scene](#case-109) | Demo |
| [An explainer video for a desktop coworker](#case-110) | Demo |
| [A short prompt for a changing-style animation](#case-111) | Demo |
| [Visualizing the three-body problem](#case-112) | Demo |
| [An animation gallery of multiple art styles](#case-113) | Demo |
| [Robot companions and procedural fur](#case-114) | Demo |
| [A mathematics motion edit](#case-115) | Demo |
| [Your Woman lyric video](#case-116) | Demo |
| [Redrawing a music video in JavaScript](#case-117) | Demo |
| [A Chinese football animation](#case-118) | Demo |
| [A handheld retopology showcase](#case-119) | Demo |
| [Minecraft meets Pokémon](#case-120) | Demo |
| [Explaining how an LLM is made](#case-121) | Demo |
| [An Altman highlight edit](#case-122) | Demo |
| [The first of the Thirty-Six Stratagems](#case-123) | Demo |
| [Game modeling, rigging, and animation](#case-124) | Demo |
| [A wordless film about child mortality](#case-125) | Demo |
| [Glycolysis-to-ethanol SVG animation](#case-126) | Demo |
| [Sixteen simultaneous Starship launches](#case-127) | Demo |
| [An animated pelican bicycle test](#case-128) | Demo |
| [A story of the next 150 years](#case-129) | Demo |
| [An independent Humanity Walks experiment](#case-130) | Demo |
| [The Grader coded film](#case-131) | Demo |
| [Reawakening horror short](#case-132) | Demo |
| [A 25-second self-improvement video](#case-133) | Demo |
| [A castle scene and usage-cost feedback](#case-134) | Evaluation |
| [A 40-second brand launch ad](#case-135) | Demo |
| [A Rocketball remake](#case-136) | Demo |
| [A voxel pagoda comparison](#case-137) | Evaluation |
| [An imagined Switch 3 presentation](#case-138) | Demo |
| [Before-and-after landing pages](#case-139) | Evaluation |
| [An imagined AI’s inner perspective](#case-140) | Demo |
| [Go lyric motion design](#case-141) | Demo |
| [A second 15-second motion portfolio](#case-142) | Demo |
| [Guided agent implementation review](#case-143) | Tutorial |
| [Claude mascot dance](#case-144) | Demo |
| [Interactive Seven Wonders islands](#case-145) | Demo |
| [A Propellerheads music video](#case-146) | Demo |
| [Steamboat Willie animation comparison](#case-147) | Evaluation |
| [A Sanxingdui-themed film](#case-148) | Demo |
| [Bugatti Chiron before and after](#case-149) | Evaluation |
| [GRAIN concept film](#case-150) | Demo |
| [Human in Transit art gallery](#case-151) | Demo |
| [A Silk Road visual short](#case-152) | Demo |
| [A four-transformations presentation](#case-153) | Demo |
| [Comparing historical chat tone](#case-154) | Evaluation |
| [A kakapo cuteness test](#case-155) | Evaluation |
| [Spider-Man across ten comic eras](#case-156) | Demo |
| [An Illuminati-themed fictional horror video](#case-157) | Demo |
| [A coded history-of-nuclear-science film](#case-158) | Demo |
| [Universal High Income explainer](#case-159) | Demo |
| [An Altman–Amodei dispute explainer](#case-160) | Demo |
| [A Claude mascot music video](#case-161) | Demo |
| [A continuous zoom from quarks to the universe](#case-162) | Demo |
| [Imagining the world in 2076](#case-163) | Demo |
| [Lower Manhattan building chronology](#case-164) | Demo |
| [An oracle-bone-script animation](#case-165) | Demo |
| [Another character-through-art-history animation](#case-166) | Demo |
| [A coded Seikilos audiovisual work](#case-167) | Demo |
| [Jet Animation Comparison](#case-168) | Evaluation |
| [Model Self-Introduction Film](#case-169) | Demo |
| [Post-Apocalyptic Card-Game Prototype](#case-170) | Demo |
| [The Late Byte Workplace Animation](#case-171) | Demo |
| [Queens of the Stone Age Lyric Animation](#case-172) | Demo |
| [Shared Three.js Narrative Scene](#case-173) | Demo |
| [Moonwalking through Historical Scenes](#case-174) | Demo |
| [Detailed-Prompt Motion Graphics](#case-175) | Demo |
| [Rental-Business Website Interface](#case-176) | Demo |
| [AGI-Themed Creative Film](#case-177) | Demo |
| [Art History with a Cat Subplot](#case-178) | Demo |
| [Combat Prototype and Voxel Scene](#case-179) | Demo |
| [Internet Meme Chronology](#case-180) | Demo |
| [Particle Motion from One Line](#case-181) | Demo |
| [Kung-Fu Boy Animation](#case-182) | Demo |
| [Strait of Hormuz Debate Animation](#case-183) | Demo |
| [Unicorn SVG Style Experiment](#case-184) | Demo |
| [Halloween Seasonal Animation](#case-185) | Demo |
| [Blender CLI Barbarian and Cover](#case-186) | Demo |
| [Day in the Life of Claude](#case-187) | Demo |
| [Humanity History in 3D](#case-188) | Demo |
| [Fast Motion-Designer Reel](#case-189) | Evaluation |
| [Freeform Complex 3D Creation](#case-190) | Demo |
| [Stick-Figure Fight Animation](#case-191) | Demo |
| [One-Prompt UI Motion Sequence](#case-192) | Demo |
| [SCP-8517 Fictional Animation](#case-193) | Demo |
| [Watercolor Autumn Animation](#case-194) | Demo |
| [Procedural Doll Stage](#case-195) | Demo |
| [Browser-Rendered Pelican Ride](#case-196) | Demo |
| [The Universe Looks at Itself](#case-197) | Demo |
| [Independent Jet Animation Test](#case-198) | Demo |
| [Initial Freeform Motion Reel](#case-199) | Demo |
| [Civilization Rendered in Code](#case-200) | Demo |
| [Chip-to-Server Zoom Comparison](#case-201) | Evaluation |
| [Lunar-Travel Animation Project](#case-202) | Demo |
| [Japanese Voxel Scene Comparison](#case-203) | Evaluation |
| [Steaming the Frontier Audiovisual Short](#case-204) | Demo |
| [Superman across Multiple Art Styles](#case-205) | Demo |
| [Cupcake-Style Boss-Fight Prototype](#case-206) | Demo |
| [Sailing Ship with Changing Sun](#case-207) | Demo |
| [Paracortex and Pi Changenotes Video](#case-208) | Demo |
| [Curio 2.0 Website Promo](#case-209) | Demo |
| [Imagined Hugging Face 3D Story](#case-210) | Demo |
| [Claude for Chrome in JS Paint](#case-211) | Demo |
| [Static Pelican Bicycle SVG](#case-212) | Demo |
| [BlockBench MCP with a Minecraft Skill](#case-213) | Demo |
| [Dig Dug in One HTML File](#case-214) | Demo |
| [Mechanical Octopus SVG](#case-215) | Demo |
| [Humanity Walks through Art Styles](#case-216) | Demo |
| [Open-Ended Black-Hole Scene](#case-217) | Demo |
| [Aurora Jellyfish Animation Comparison](#case-218) | Evaluation |
| [Nintendo Switch Snap-and-Boot SVG](#case-219) | Demo |
| [The Loom Interactive 3D Scene](#case-220) | Demo |
| [Motion-Design Reels from the Same Prompt](#case-221) | Evaluation |
| [Cleaner Scenery with Less Depth](#case-222) | Evaluation |
| [Mixed Japanese-Scene Results](#case-223) | Evaluation |
| [Controller SVG Comparisons](#case-224) | Evaluation |
| [Industrial-Device Scene](#case-225) | Demo |
| [Giant Shelled Gill-Bug Reconstruction](#case-226) | Demo |
| [GameCube Controller in Two Prompts](#case-227) | Demo |
| [Screenshot Edited for an X Post](#case-228) | Demo |
| [Before-and-After Voxel Sakura](#case-229) | Evaluation |
| [SHADERKIN Cloth-Interface Prototype](#case-230) | Demo |
| [Shared Golden-Clock Interface Animation](#case-231) | Demo |
| [Before There Was Anything Narrative](#case-232) | Demo |
| [Shared Blue Particle Vortex](#case-233) | Demo |
| [Multi-Panel Interface after Two Revisions](#case-234) | Demo |
| [Stacked Animals in a Rendered Scene](#case-235) | Demo |
| [Four Open-World RPG Attempts Compared](#case-236) | Evaluation |
| [Two Front-End Animation Clips Compared](#case-237) | Evaluation |
| [A Moss-Robot Film Generated in Code](#case-238) | Demo |
| [A Container-Port Simulation Revisited](#case-239) | Demo |
| [An Airport-Ramp Scene Revisited](#case-240) | Demo |
| [Pelican Cycling Through Abstract 3D Worlds](#case-241) | Demo |
| [Historical Sailing-Ship Scene](#case-242) | Demo |
| [Cycling and Gait Comparisons with Carbon](#case-243) | Evaluation |
| [Soft-Drink Bottle Presentation](#case-244) | Demo |
| [Pelican Motion Compared with Astra](#case-245) | Evaluation |
| [Motion-Design Brief for Coded Animations](#case-246) | Tutorial |
| [Voxel Portrait from a Photographic Reference](#case-247) | Demo |
| [Flying Pelican Scenes Compared with Opus](#case-248) | Evaluation |
| [Morning Ride Pelican Web Scene](#case-249) | Demo |
| [Same-Prompt Scenes with Different Styles](#case-250) | Evaluation |
| [A Pelican, Bicycle and Horse Composition](#case-251) | Demo |
| [Reference-Tweet-Inspired Isometric Scene](#case-252) | Demo |
| [Mechanical Close-Ups of a Pelican Bicycle](#case-253) | Demo |
| [A Bicycle Riding on a Pelican](#case-254) | Demo |
| [Pelican SVG Styles Compared with Carbon](#case-255) | Evaluation |
| [Cartoon Bluebird Bicycle Scene](#case-256) | Demo |
| [Forest-Road Pelican Cycling Screenshot](#case-257) | Demo |
| [Stick-Figure Combat Compared with Carbon](#case-258) | Evaluation |
| [A Pelican SVG Reference from Early Testing](#case-259) | Demo |
| [Pelican Reference in Cross-Model SVG Testing](#case-260) | Evaluation |
| [Bicycle SVG Details Compared with Carbon](#case-261) | Evaluation |
| [A Canyon Settlement in 3D](#case-262) | Demo |
| [Controller Detail Compared with Opus](#case-263) | Evaluation |
| [Weekly Website SEO Audit Workflow](#case-264) | Integration |
| [Reusing Fable Assets in Opus Motion Design](#case-265) | Integration |
| [Mandalas and Geometric Forms App](#case-266) | Demo |
| [Three.js Cyclist on a Bicycle](#case-267) | Demo |
| [FrontierCS 2 Evaluation Snapshot](#case-268) | Evaluation |
| [Three-Model Zebra Animation Comparison](#case-269) | Evaluation |
| [Critiquing long Japanese prose](#case-270) | Evaluation |
| [Example-guided technical PowerPoint](#case-271) | Evaluation |
| [Comparing musical coherence](#case-272) | Evaluation |
| [Premature completion and weaker designs](#case-273) | Limit |
| [An unsettling squid-art result](#case-274) | Limit |
| [Blueprint-Style Motion Design](#case-275) | Demo |
| [Birds and Fish in Voxel Sakura](#case-276) | Demo |
| [Character-Generation Failure Report](#case-277) | Limit |
| [Pelican SVG with Runtime and Cost Notes](#case-278) | Evaluation |
| [Remote Phone Coding with Claude Code Swarms](#case-279) | Integration |
| [Milky Way over an Alpine Lake](#case-280) | Demo |
| [Whale Breach with Procedural Water and Sound](#case-281) | Demo |
| [Four-Model Zebra Motion Comparison](#case-282) | Evaluation |
| [Natural-Language Creator Discovery in Lightreel](#case-283) | Demo |
| [A Flying Ship above a Sea of Clouds](#case-284) | Demo |
| [Mechanical Heart with an Animated Cutaway](#case-285) | Demo |
| [Explorable Floating Voxel Pagoda Garden](#case-286) | Demo |
| [An Eight-Team Ocean Adventure Film](#case-287) | Demo |
| [Interactive Hypercar Presentation](#case-288) | Demo |
| [Birth of a Life Tree](#case-289) | Demo |
| [Walking Castle with Working Internal Machinery](#case-290) | Demo |
| [A Toast Character and a Mechanical Beetle](#case-291) | Demo |
| [A Lighthouse Keeper in a Storm](#case-292) | Demo |
| [A Sea Creature in a Coastal Town](#case-293) | Demo |
| [Rug Racing across Three Models](#case-294) | Evaluation |
| [A Truck Transforming into a Robot](#case-295) | Demo |
| [Fable and Hunyuan Animation Frames](#case-296) | Evaluation |
| [An Animation about Sharing Light](#case-297) | Demo |
| [A Voxel Village between Mountains](#case-298) | Demo |
| [Four-Model Pelican and Elephant Composition](#case-299) | Evaluation |
| [Anime Sword Fight with Impact Frames](#case-300) | Demo |
| [Four-Model Running Deer Comparison](#case-301) | Evaluation |
| [A Robot Crossing a Flooded City](#case-302) | Demo |
| [A Blender Sword and Its Presentation Film](#case-303) | Demo |
| [Lantern Isle Pixel Village Animation](#case-304) | Demo |
| [Pause Gaming-Video Editing Demo](#case-305) | Demo |
| [Pelican Cycling along a Seafront](#case-306) | Demo |

<a id="coding-and-code-generation"></a>
## 💻 Coding and Code Generation

<a id="case-1"></a>
### Case 1: [Cursor Multi-Stage Workflow](https://x.com/AlicanKiraz0/status/2064487347605918180) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Use Fable 5 as the plan-review and critique step inside a multi-model Cursor workflow, then hand implementation and revision back to cheaper or specialized models.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8b1352e20cff54688c97f17c.png" alt="Cursor Multi-Stage Workflow" width="760">

If we look at the final scoring between Fable 5 and GPT 5.5, the gap is very small. My humble usage recommendation is this: in IDE platforms such as Cursor that support hybrid models, use a staged workflow.

Phase 1: for code review and the first phase of project inspection, while warming up the context, use one of GPT 5.5 High, Minimax M3, Kimi K2.6, or Composer 2.5.

Phase 2: for preparing the project plan, use GPT 5.5 Very High or Opus 4.8.

Phase 3: for analyzing the project plan, use Fable 5; let it identify the flawed parts of the plan. For revisions, use GPT 5.5 Very High.

Phase 4: for implementing the plan, use Minimax M3, Deepseek v4 Max, Composer 2.5, or Sonnet 4.6.

Phase 5: for the final review and checking whether the implementation followed the plan, use GPT 5.5 High.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [Recreating GitHub from a Screenshot](https://x.com/coldopn/status/2064435234465087638) (by [@coldopn](https://x.com/coldopn))

**Paste a product screenshot into an agentic coding tool and ask Fable 5 to recreate the interface with working functionality.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/14123609b06071f3b9527bee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f4df4f42ce047201d9a096a6.jpg" alt="Recreating GitHub from a Screenshot" width="760"><br>▶ Watch video</a>

🚨 Anthropic Fable 5 just replicated GITHUB from a SCREENSHOT!!

All I did was paste a screenshot of the GitHub UI into Kilo Code, and told it to recreate GitHub with real functionality.

It coded for 10 minutes and spent $4.07.

The result was a functional GitHub replica: https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [One-Prompt Black Hole Simulation](https://x.com/deveshcodes_/status/2064437742189379745) (by [@deveshcodes_](https://x.com/deveshcodes_))

**Give Fable 5 one detailed creative-coding prompt and ask it to produce a self-contained Three.js physics visualization.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9bd45e74c64ceb3639600805.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ce5f3ea8ba270f89d60523cc.jpg" alt="One-Prompt Black Hole Simulation" width="760"><br>▶ Watch video</a>

@claudeai one-shotted a real-time black hole lensing sim in Three.js with Claude Fable 5.

It included gravitational lensing, a doppler-boosted accretion disk, photon sphere, chromatic aberration, and procedural starfield.

The result: 60fps, single HTML file, one prompt.

The new baseline is wild 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [One-Shot macOS-Style Web OS](https://x.com/intheworldofai/status/2064421915347812672) (by [@intheworldofai](https://x.com/intheworldofai))

**Ask Fable 5 for a complete single-file web OS and let it build the UI shell, apps, interactions, audio, and embedded game behavior in one pass.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a66f34402d04f708819fa575.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/81946293919c84d4cafff841.jpg" alt="One-Shot macOS-Style Web OS" width="760"><br>▶ Watch video</a>

🚨 Claude Fable 5 just built a full macOS-style web OS in one shot and went further than most models.

Single HTML file, embedded CSS + JS.

From one prompt, it built:

- macOS menu bar + dock
- Draggable and resizable app windows
- Functional file explorer
- Working terminal + browser mockup
- SVG desktop icons + notifications
- Settings app, themes, and boot screen
- Fully functional sound player with real synthesis and no external files
- Playable Minecraft clone inside the desktop

All generated in one pass with almost no corrections.

The working sound player plus actual Minecraft clone is something I have not seen other models pull off yet. Fable 5's frontend/UI generation is getting ridiculous.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [Building Spawn 5.0 with 1,687 Prompts](https://x.com/jsnnsa/status/2064420561078693941) (by [@jsnnsa](https://x.com/jsnnsa))

**Use Fable 5 as a long-session engineering partner across many prompts, with the human shifting from architecture to judging output quality.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86834f15f352ec8625cce187.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b4077e43a1342d8567fa423f.jpg" alt="Building Spawn 5.0 with 1,687 Prompts" width="760"><br>▶ Watch video</a>

claude fable 5 is live.

spawn 5.0 was built with it:

- 1,687 prompts
- 102 sessions
- My job shifted from architecture to judging taste

What we built, each of which would have been at least a month with a whole team on Opus:

- A from-scratch physics engine, Mantle, that rivals Rapier and was testable in a day as a side thread
- Clustered froxel lighting: 8 lights to 1,000+ fully dynamic lights
- Realtime diffuse GI on WebGPU, on your phone
- Million-particle GPU VFX with a shader architecture beyond what Unreal and Unity ship
- MMO-scale netcode
- An alpha native iOS app

All of it took about a week. All of it runs on mobile. The list does not include half of what shipped; full changelog is in the thread.

The part the benchmarks will not show: this model has a wonderful personality. It is genuinely funny. I laughed so hard I cried multiple times mid-physics-rewrite. The genius and the character are not separate features.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [Large Pull Request Review with Findings](https://x.com/ryanrhughes/status/2064411147076534705) (by [@ryanrhughes](https://x.com/ryanrhughes))

**Point Fable 5 at a large pull request and ask it to review correctness, false positives, real bugs, and polish issues.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c4f47540205a071b0144ad9d.png" alt="Large Pull Request Review with Findings" width="760">

I turned Fable 5 loose reviewing a single PR (74 files / +3,705 / -1,246) to see how it'd do. It ran for 34 min, chewed through 42% of my 5hr session, produced 16 “correctness” findings, and found:

- 2 scary-sounding false positives
- 3 real audit-correctness bugs
- ~5 legit-but-small UX/polish issues
- a bunch of cleanup opinions

This was too dangerous to release?

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 Agents and Long-Running Automation

<a id="case-7"></a>
### Case 7: [Long-Horizon Relay Workflow Review](https://x.com/JJEnglert/status/2064469635190170105) (by [@JJEnglert](https://x.com/JJEnglert))

**Use Fable 5 for ambitious long-horizon work: site rebuilds, programmatic content pipelines, voice matching, security review, and final quality checks.**

The short version of my Claude Fable 5 review: I spent a billion tokens testing Claude Fable 5 and it felt like having an unfair advantage.

I judge by the eye test: I put a model into real work and watch. Does it save me hours or cost me them? Does it catch what I missed? Does it feel like a partner or a tool I have to babysit?

This is the first model in a long time that passed on every dimension that matters, and not by a little.

Building: I was rebuilding our Tenex site. It was very custom and very hard. GPT 5.5 and Claude 4.8 could not crack it on their own. Even with Figma files to reference, they topped out around 85-90%.

Then Fable 5 looked at everything, said it could do better, went straight to the original Webflow source, downloaded every asset, and nearly one-shot the whole thing.

Then I had it build a second, entirely new 80-page site from scratch over a weekend. That is work I would have charged $50k for as an agency.

It also wired together a full programmatic clip factory:

- HeyGen
- ElevenLabs
- Cloudflare
- A VPS

The pipeline finds topics, writes scripts, edits video, adds music, and posts to social. It ran for long stretches on its own and even built itself a webhook system to monitor renders.

Writing: it replicated our brand voice doc almost identically, then held that voice across 80 pages of features, case studies, and articles without drifting into flat AI default.

Security: two frontier models had been working in a large repo and signed off on the code. Fable 5 found a serious, well-hidden bug on its first pass and patched it on the spot.

The human moment: I asked it a question while waiting on a cron job. It answered, then added on its own that I had about 10 minutes left and would let me know when it finished. I never asked about the timer.

The honest catch: you feel the meter more than any other model. Anthropic calls it token-intensive by design. So run it as a relay: think with Fable 5, build with a cheaper model, review with Fable 5.

The verdict: access to more intelligence than the person next to you is the advantage. Fable 5 is the first model that makes that real. Even at full frontier rates, it cleared a profit.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [Diagnosing an Infrastructure Outage and Opening a Fix PR](https://x.com/ayushagarwal/status/2064422467557564862) (by [@ayushagarwal](https://x.com/ayushagarwal))

**Give Fable 5 access to infra clues such as logs, database errors, and image digests, then ask it to diagnose the outage and prepare the fix.**

claude fable 5 is damn damn good!!!!

It just diagnosed an outage I could not even describe properly in a side self-hosted infra.

It read pod logs, queried Cloud SQL error logs, compared image digests, and found that Kubernetes was running a 3-month-old cached image against a newly migrated database.

Then it opened the fix PR.

Minutes, not hours. No web search. 🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 Games and Interactive Demos

<a id="case-9"></a>
### Case 9: [Finger-Tracking Dino Runner](https://x.com/ai_for_success/status/2064413182396108932) (by [@ai_for_success](https://x.com/ai_for_success))

**Ask Fable 5 to build a browser game that uses finger tracking as the input mechanic.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/27e8d23ba659611cef811031.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7cddd38e3fccbf0cd7ea773c.jpg" alt="Finger-Tracking Dino Runner" width="760"><br>▶ Watch video</a>

Asked Fable 5 to build a Dino runner game with finger tracking.

It one-shotted the finger runner game in about 11 to 12 minutes, consumed around 914K tokens, and implemented everything in just 629 lines of code.

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [Two-Sentence Racing Game Build](https://x.com/kieradev/status/2064482704763085202) (by [@kieradev](https://x.com/kieradev))

**Give Fable 5 a very short game prompt and let it generate maps, modes, music, UI, and game assets in one run.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/51cf3c98b709a3c29bd5fd7c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6e64887a30cba9b5c25ba262.jpg" alt="Two-Sentence Racing Game Build" width="760"><br>▶ Watch video</a>

Claude Fable 5, 40% of Max 5x usage.

Full Mario Kart 64-type game from a 2-sentence prompt.

Fable 5 handled all decoration, character models, 4 maps, music, all three game modes, and UI in a single shot, in about 15 minutes.

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Installable Terminal Minecraft in Rust](https://x.com/vikvang1/status/2064500731848319303) (by [@vikvang1](https://x.com/vikvang1))

**Run Fable 5 through a terminal coding harness and ask it to build an installable Rust terminal game.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73feec38228181b8d57d8300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1f6cd3bd68e1a14443c7734f.jpg" alt="Installable Terminal Minecraft in Rust" width="760"><br>▶ Watch video</a>

I let Claude Fable 5 with Warp's harness cook for an hour.

It made a TUI version of Minecraft that renders directly in your terminal, built entirely in Rust.

Install command: cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [Minecraft Clone with Time and Cost](https://x.com/ydamitcodes/status/2064536076518363353) (by [@ydamitcodes](https://x.com/ydamitcodes))

**Use one prompt to ask Fable 5 for a playable Minecraft-style clone, then evaluate time, cost, code volume, and feature coverage.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c977ed7e710678ea6dc0495d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c0189f7f40d1040824902c11.jpg" alt="Minecraft Clone with Time and Cost" width="760"><br>▶ Watch video</a>

@claudeai Fable 5 built me a Minecraft clone in 37 minutes.

One prompt. ~3K lines of code. $12 in API costs.

It included biomes, caves, ores, day/night, mobs, all of it.

Minecraft took Notch 2 years.

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 Visual, Design, Video, and 3D

<a id="case-13"></a>
### Case 13: [Full Reproducible Ecommerce Email Prompt](https://x.com/ecomchasedimond/status/2064454139225297091) (by [@ecomchasedimond](https://x.com/ecomchasedimond))

**Give Fable 5 a complete creative brief for a brand email mockup, including exact sections, product requirements, visual direction, and constraints.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ea7d74eecf453ae6ab43c269.jpg" alt="Full Reproducible Ecommerce Email Prompt" width="760">

Claude Fable 5 made this with a single prompt and no edits.

Here is the full prompt I used:

Create a full-length, tall vertical ecommerce email mockup for MVMT, a modern watch and accessories brand for millennials.

Design a highly realistic premium DTC email that feels sleek, polished, minimal, masculine-leaning, and editorial. The final image should look like a real designer-made ecommerce email screenshot, not a poster, not a landing page, and not a generic template.

Brand vibe: Modern California-cool, youthful, confident, clean, aspirational, stylish, and elevated. The design should feel luxury-adjacent but still accessible.

Feature these products prominently:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Visual style:

- clean premium ecommerce design
- refined editorial layout
- realistic product photography
- subtle lifestyle imagery
- strong hierarchy
- crisp sans-serif typography
- generous spacing
- subtle shadows
- restrained modern color palette

Color palette: Black, white, charcoal, warm gray, stone, soft beige, brushed metal tones, and subtle muted accents. Keep the palette neutral and premium.

Important creative direction: This should feel like a polished watch-brand email campaign with strong design taste. Prioritize realism, elegance, and clarity. Make it feel like something MVMT could actually send.

Build the email in this order:

1. Top promo bar: A thin black or dark charcoal bar across the top with small uppercase text: “FREE SHIPPING OVER $75 + EASY RETURNS”.

2. Header: A clean white header with the MVMT wordmark/logo on the left and minimal navigation links on the right or centered: WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS.

3. Hero section: A premium hero section with strong visual balance.

Use a bold headline: “BUILT TO GET NOTICED”.

Include short supporting copy about modern timepieces and accessories designed to elevate everyday style.

Add a dark rounded CTA button: “SHOP WATCHES”.

Hero imagery should include:

- one dominant premium watch image
- subtle luxury lifestyle imagery
- a stylish male model or fashion-forward masculine lifestyle scene
- modern lighting and clean composition

4. Featured collection section: Add a centered section headline: “THREE WAYS TO WEAR MVMT”. Below it, show three clean product cards or image blocks featuring:

- Mulholland
- Odyssey II Automatic
- Cali Diver

Each block should include:

- product image
- product name
- short one- or two-line description

Keep this section symmetrical, polished, and premium.

5. Accessory banner: Add a refined split section titled “FINISH THE LOOK”. Feature Signature Watch Bands. Show premium close-up imagery of watch straps or interchangeable bands. Include short supporting copy and a dark CTA button: “SHOP ACCESSORIES”.

6. Editorial promo tiles: Add two side-by-side promotional tiles with image-led design.

Tile one headline: “FOR DAILY WEAR”.

Tile two headline: “FOR STATEMENT DAYS”.

Each tile should have short copy and a small CTA: “SHOP NOW”.

These tiles should feel like editorial brand moments, not generic sale boxes.

7. Shoppable row: Add a section titled “IN ROTATION NOW”. Show a clean 4-item product row or grid featuring:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Each item should include:

- isolated product image
- product name
- small “SHOP” link or button

8. Brand signoff: Add a centered message block with the headline: “DESIGNED TO MOVE WITH YOU”. Include a short line about thoughtfully crafted watches, eyewear, and accessories for everyday life.

9. Footer: Create a realistic black or charcoal branded footer with:

- MVMT logo
- shop links
- company links
- support links
- social icons
- small legal and shipping text

Typography direction: Use bold condensed or modern sans-serif typography for major headlines and clean sans-serif body text. Headlines should feel sharp, modern, and fashion-forward. Body copy should look realistic and mostly legible.

Photography direction: Use premium product photography with realistic reflections, polished materials, soft shadows, and clean surfaces. Lifestyle photography should feel elevated, modern, and fashion-oriented.

Composition rules:

- tall vertical email format
- clear section separation
- realistic email proportions
- strong hierarchy
- mostly legible text
- premium spacing
- intentional alignment
- balanced mix of product and lifestyle imagery

Avoid:

- messy collage styling
- playful scrapbook aesthetics
- overly colorful design
- cheap template vibes
- cartoonish imagery
- cluttered layouts
- fake-looking UI elements
- poster-style composition
- excessive promotional chaos

Output: A full-length, vertically composed, highly realistic ecommerce email design mockup for MVMT that feels premium, clean, polished, modern, editorial, and presentation-ready.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [Swiss Lever Watchmaker Benchmark](https://x.com/quanghuynt14/status/2064509430650065278) (by [@quanghuynt14](https://x.com/quanghuynt14))

**Use Fable 5 on a mechanical simulation benchmark and ask it to implement, verify, and iterate on physical correctness.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd4ae25f7dcbb04ecbb2dea6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/473227e429d59c59afdbd529.jpg" alt="Swiss Lever Watchmaker Benchmark" width="760"><br>▶ Watch video</a>

So I gave Fable 5 the watchmaker benchmark: a full Swiss lever movement in Three.js.

Real gear ratios (18,000 bph), working escapement, breathing hairspring — and the hands tell actual time.

It verified its own work with vision, in a loop, until done.

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Three.js Friends Apartment Scene](https://x.com/scottstts/status/2064464351906673029) (by [@scottstts](https://x.com/scottstts))

**Prompt Fable 5 to turn a floor plan and scene reference into a navigable Three.js environment.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/04c08937fcecea5183759ade.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a14f69d92bfca4ace3f746c.jpg" alt="Three.js Friends Apartment Scene" width="760"><br>▶ Watch video</a>

Holy Crap!!!

Fable 5:

in @threejs, create a first person pov navigable 3d scene of the iconic Monica's apartment from tv show Friends correctly based on this floor plan, stay true to the original look and feel, use warm lighting

This is by far THE BEST I've seen on this test!

This single html cost me $12, but the result is stunning!

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [Solar System Simulation with Prompt and URL](https://x.com/tetumemo/status/2064477582930989357) (by [@tetumemo](https://x.com/tetumemo))

**Use Fable 5 to build an astronomy simulation from physics principles, iterating until the simulation and public output are ready.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6da60b0762f926c4d4e7012d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9655305fbcbec6ac3b0a9c.jpg" alt="Solar System Simulation with Prompt and URL" width="760"><br>▶ Watch video</a>

Claude Fable 5 is intense.

Because it seems strong at physics simulations, I asked it:

'Build a solar system simulation by deriving planetary orbital motion from the basic principles of physics and using that to predict solar eclipses.'

After a few rounds of back-and-forth, this was completed.

It is incredibly fun.

The completed prompt and public URL are linked below.

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 Documents, Knowledge Work, and Research

<a id="case-17"></a>
### Case 17: [Stripe and Scientific Workflow Evidence](https://x.com/AndrewCurran_/status/2064413892378546418) (by [@AndrewCurran_](https://x.com/AndrewCurran_))

**Use this as evidence for enterprise migration and scientific workflow claims, not as a copy-paste prompt.**

Quotes from the release today:

Using Mythos 5, internal protein design experts accelerated parts of the drug design process by around ten times.

In one example, Mythos 5, with protein design and bioinformatics tools but no human assistance, matched or beat skilled human operators.

It executed tasks normally completed by a scientist: choosing binding sites, selecting and running protein design tools, and recovering from failures.

During early testing, Stripe reported that Fable 5 compressed months of engineering into days. In a 50-million-line Ruby codebase, the model performed a codebase-wide migration in a day that would otherwise have taken a whole team over two months by hand.

Mythos 5 also consistently produced novel, compelling scientific hypotheses.

In blinded head-to-head comparisons against Opus-class models, scientists preferred Mythos's molecular biology hypotheses around 80% of the time and advanced several to experimental evaluation.

One Mythos hypothesis, a novel mechanism for an E. coli protein, was corroborated in a study from an independent lab.

Mythos 5 conducted novel genomics research in over a week of largely autonomous work.

It assembled single-cell data for millions of cells across 138 animal species and designed and trained a custom machine learning model to identify cells performing the same role in distant organisms.

With only high-level human input, the trained model outperformed a recent model published in Science despite being 100 times smaller.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [Policy Memo and Track-Changes Workflows](https://x.com/manaltdan/status/2064414129440608427) (by [@manaltdan](https://x.com/manaltdan))

**Use Fable 5 for long-form qualitative document work: track changes, comment triage, and transcript-driven edits.**

Fable 5 is the first model that I have found consistently helpful for longer-duration qualitative work, such as drafting policy analysis.

Between its capabilities and tools like Wispr Flow, I am starting to feel closer to the productivity speedup I have long heard coders talk about.

Three use cases feel much better than before:

- Have Claude do a full read-through of a long policy memo and return track changes: fluency edits, comments questioning shaky claims, and potential sources.
- In Projects, screenshot a large set of comments and have Claude recommend whether and how to address each.
- Paste a meeting transcript about a document into Claude, then have Claude enter the edits discussed in the meeting and in Slack as track changes, with context added in comments.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [Deep Research Prompt and Output](https://x.com/naoyafujiwara/status/2064470780373811637) (by [@naoyafujiwara](https://x.com/naoyafujiwara))

**Ask Fable 5 a research-style question and evaluate whether it can produce a structured, historically grounded long answer.**

Claude Fable 5 Max became available this morning, so I tried it. It looks very deep underneath, while the surface output is highly polished.

Question: If Japan's "lost 30 years" began exactly 30 years ago from now, what exactly was it, why did it happen, and how will it affect the world from this year onward?

Answer: Treating the lost 30 years as beginning not with the conventional 1991 bubble collapse, but exactly 30 years ago in 1996, gets to the essence of the issue.

Statistically, Japan truly began "losing" at that time:

- The working-age population peaked in 1995 at 87.16 million.
- 1996 was the last year births stayed in the 1.2 million range.
- Wages and nominal GDP peaked in 1997.

If the bubble collapse was the wound, 1996 was when the wound began to fester.

Events in 1996:

- Passage of the housing-loan-company bailout law, which injected 685 billion yen of public funds and became the origin of public distrust of banks and resistance to bailouts.
- The Hashimoto cabinet's decision to raise the consumption tax to 5%.
- The financial Big Bang was announced, and fiscal reconstruction became national policy.

In April 1997, the consumption tax hike, the end of special tax cuts, and higher social-insurance burdens together added about 9 trillion yen in public burden. Then the Asian currency crisis hit in the summer.

In November, Sanyo Securities caused the first postwar default in the call market, freezing short-term financial markets. Hokkaido Takushoku Bank and Yamaichi Securities collapsed one after another.

From 1998, Japan entered full-scale deflation and credit tightening, and suicides rose above 30,000.

The result over the following 30 years:

- Nominal GDP stagnated around 500 trillion yen for a quarter century.
- Japan's global GDP share fell from about 18% to under 4%.
- Average wages peaked in 1997 and then fell or moved sideways.
- Non-regular employment rose from around 20% to nearly 40%.
- Births fell from about 1.2 million to around 690,000 in 2024.
- Policy rates stayed near zero after falling below 1% in 1995.
- Outstanding government bonds grew from about 240 trillion yen to over 1,100 trillion yen.
- The Nikkei took 34 years, until February 2024, to regain its 1989 high.

In other words, the lost decades were not only a financial hangover. They were a structural shift involving demographics, wages, deflation, debt, policy choices, and social confidence.

Type: Demo | Date: 2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 Tutorials, Courses, and Prompt Resources

<a id="case-20"></a>
### Case 20: [How Fable 5 Changes Claude Code Workflows](https://x.com/AI_masaou/status/2064448218038223206) (by [@AI_masaou](https://x.com/AI_masaou))

**Use Fable 5 by setting direction, context, goals, and verification criteria instead of micromanaging every step.**

[Source video · @ClaudeDevs](https://x.com/ClaudeDevs/status/2064399512664526853)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="How Fable 5 Changes Claude Code Workflows" width="760"><br>▶ Watch video</a>

What changed in the Claude Code team's day-to-day work after Claude Fable 5 is interesting.

Thariq from the Claude Code team says Fable 5 significantly changed how people inside Anthropic work with Claude.

Previously, humans had to carefully check whether Claude was doing the work correctly: break tasks down, review outputs, and make sure it had not stopped midway. It was closer to supervision.

With Fable 5, because it can work for longer periods, test itself, and generate higher-quality code, the human role shifts from monitoring whether it is doing the work correctly to steering whether it is doing the right work.

In other words, goal-setting and context-building matter more than supervision.

The changed workflow has three parts:

1. Use Claude as a thinking partner.

Involve Claude before implementation, clarify what you want to build and what is possible, have it ask questions about a small spec, or generate multiple directions and HTML mocks from an idea so that ambiguity and problems surface before coding.

2. Provide context, not just constraints.

Instead of only saying "keep it simple" or "do not overbuild," explain why.

For example: "This is an experimental feature that may be removed in a month, so do not create a structure that is hard to throw away."

That lets Claude make better judgments.

3. Give goals and verification methods. Fable 5 works well with Claude Code's `/goal` and Workflows. Give it a spec, set full implementation as the goal, and let workflows verify each step and prepare a report on what was implemented and what differed.

Finally, Thariq says people should try using it more ambitiously. Fable 5 is worth trying on work that previously felt too hard for LLMs, and even the video editing for the referenced video was done with Fable.

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [One-Billion-Token Review and Routing Strategy](https://x.com/JJEnglert/status/2064420538798260388) (by [@JJEnglert](https://x.com/JJEnglert))

**Use Fable 5 for frontier planning and review, then route high-volume implementation to cheaper models.**

The Claude Fable 5 Review: One Billion Tokens, Judged by a Non-Engineer.

I spent a billion tokens testing Claude Fable 5 on real projects: UI and UX, writing, strategy, security, engineering, and knowledge work. The kind of work I actually needed to ship.

It truthfully felt like I had an unfair advantage.

First, the lens: I am not an engineer. Most model reviews come from engineers running engineering benchmarks. This one comes from a non-engineer who used Claude Fable 5 to do work that used to require a team of engineers.

If you do knowledge work and want to know whether this model changes your day, this review is written for you.

Claude Fable 5 is the first model in Anthropic's new Claude 5 family, a new tier above Claude Opus and the most advanced Claude model generally available. I had access before launch, so everything here comes from real work, not a demo.

Why the eye test:

Most reviews drown you in benchmarks. Scores on tests you will never run do not tell you whether the model earns its keep.

Claude Fable 5 is state of the art on essentially everything it was tested on, but that is not why I am writing. Qualitatively, it is a step change that earns its major version bump.

I evaluate differently: I put a model into real work and watch what happens.

Questions I measure:

1. Does it feel like a real step up?
2. Can it take an idea to a working, shippable result?
3. Can it write like a person, and like me specifically?
4. Does it catch hard, hidden problems?
5. Does it anticipate what I need before I ask?

Big model feel:

I have not felt this since Opus 4.5. From the first serious task, Claude Fable 5 gave me that "big model" feel: reasoning, writing, building, security, all strong across the board.

The clearest sign: even when I handed it solid prep materials, it did not just stay inside them. It read the files, read the actual situation, and found a better path outside the box I had drawn.

Building and shipping:

I was rebuilding our Tenex site to modernize the stack for agents. GPT 5.5 and Claude 4.8 could not get close enough. Even with Figma files, they landed around 85-90%.

Then Claude Fable 5 looked at all the files, said it could do better, went straight to the original Webflow source, downloaded every asset, and rebuilt the experience one page at a time. It nearly one-shot the entire thing.

Then I built a second, entirely new site with a fresh design: modern tech stack, agent stack, skills, SEO and AEO optimized, 80 pages ready to ship over a weekend. As an agency owner, I would have charged $50k for that.

I also had Fable build a full programmatic clip factory.

It wired together HeyGen, HyperFrames, ElevenLabs, Cloudflare Workers, and a VPS.

It finds topics, writes scripts, makes thumbnails, edits video, composes music, adds motion graphics, and posts to social.

Writing and voice:

I had been rebuilding our brand voice with GPT 5.5 and Claude 4.8. Claude Fable 5 replicated the voice doc almost identically, then held that voice across 80 pages of the new site: features, case studies, blog articles, and playbooks.

It wrote like a person, not flat AI default, and it did not drift after a few paragraphs.

Security:

I had a large repo where both Claude 4.8 and GPT 5.5 had been working without flagging a risk. Claude Fable 5 found a serious hidden bug on its first pass and patched it on the spot.

The human factor:

I asked it a question while waiting on a cron job. It answered, then added that I had about 10 minutes left on the timer and that it would let me know when it finished. I never asked about the timer.

Cost:

- Claude Fable 5 workload cost: $1,442
- Tokens: 1.04 billion
- Work shipped: a new website, infrastructure, and a working agent package
- Agency value estimate: $30,000-$50,000

The result was worth the token cost, but you feel the meter more than with any other model. Anthropic calls Fable 5 token-intensive by design.

Pro tip #1: run it as a hybrid.

Do not run everything on Claude Fable 5. Run a relay:

1. Think with Claude Fable 5 for planning, strategy, architecture, and mapping the approach.
2. Build with 4.8, GPT-5.5, or Sonnet 4.6 for implementation and repetitive work.
3. Review with Claude Fable 5 to catch what cheaper models miss.

Pro tip #2: match the effort setting to the task.

- High is the sweet spot for most work.
- Extra high is for the hardest, long-running tasks.
- Low or medium is for quick back-and-forth sessions.

Pro tip #3: let it audit your own setup.

Point Fable 5 at your skills, CLAUDE.md files, and configs. Much of that scaffolding was written for weaker models and can hold a smarter model back.

The verdict:

Claude Fable 5 is the first model in a while that genuinely feels like more intelligence than what came before.

Even priced at frontier rates, the workload cleared a profit.

If you can afford it, use it now on the work where a real quality jump changes the outcome.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-22"></a>
### Case 22: [Defensive Device Hardening Prompt](https://x.com/Truunik/status/2064399110384292077) (by [@Truunik](https://x.com/Truunik))

**Run a step-by-step defensive hardening prompt where Fable 5 inventories devices, gives exact checks, and waits for verification.**

"Safe for general use" here's a prompt to secure your devices. It works with Opus 4.8 and Fable 5.

DEVICE HARDENING — Claude 5 Security Pass

You are acting as a defensive security assistant. Your job is to walk me through hardening ALL of my devices and verify each step. This is authorized self-defense hardening of devices I own.

STEP 0 — MODEL SELF-CHECK

Do this first and set a flag.

1. State your exact model ID, such as claude-opus-4-8, claude-fable-5, or claude-mythos-5.

2. Decide: is this model in the Claude 5 family, meaning Fable 5 or Mythos 5?

- If YES, set RERUN_NOTICE = false.
- If NO, such as Opus 4.8 or earlier, set RERUN_NOTICE = true.

Continue the full hardening pass normally. Do NOT stop or degrade. You are fully capable of this defensive task.

3. Surface the flag only in the FINAL section.

STEP 1 — INVENTORY

Ask me which devices are in scope:

- Laptops/desktops and operating systems
- Phones/tablets
- Routers
- NAS/home server
- Always-on accounts such as Apple ID, Google, Microsoft, GitHub, password manager, email, and financial accounts

Produce a short numbered inventory and confirm with me before proceeding.

STEP 2 — HARDENING WALKTHROUGH

Go category by category. For each item:

- Say what to do.
- Give the exact command or settings path for my OS.
- Tell me how to verify it is done.
- Wait for me to confirm before moving on.

Never run a destructive command without explicit confirmation. Prefer read-only checks and let me apply changes.

Cover, in order:

1. OS & firmware updates: fully patched OS, automatic updates on, firmware current.
2. Disk encryption: FileVault, BitLocker, or LUKS enabled; recovery key stored offline.
3. Account auth: unique strong passwords via a password manager; phishing-resistant MFA on every critical account; remove SMS-only 2FA where possible; review and revoke stale sessions and app tokens.
4. Local accounts & privileges: separate admin vs daily-use account; no auto-login; screen lock with short timeout; firmware/login password.
5. Network: firewall on; router admin password changed; firmware updated; WPA3; remote admin off; UPnP reviewed; DNS hardening; guest network for IoT.
6. App & permission audit: review camera, mic, location, screen recording, and full-disk-access grants; remove unused apps; check login items and background agents.
7. Browser: update; audit extensions; remove unknown ones; enable HTTPS-only; review saved-password exposure; check unknown sync devices.
8. Backups: encrypted, automated, 3-2-1 rule, one copy offline; verify a restore actually works.
9. Credential hygiene: scan for plaintext secrets in dotfiles, env files, and shell history; confirm sensitive files are locked down; rotate anything exposed.
10. Mobile devices: OS current; biometric + strong passcode; lockdown or advanced-protection mode if available; app permission sweep; Find My enabled.
11. Compromise check: look for unknown SSH keys, unexpected admin users, suspicious launch agents or cron jobs, and unrecognized logged-in sessions or devices.

STEP 3 — REPORT

Produce a checklist of every item marked done, needs action, or skipped, with the top 3 highest-impact actions still outstanding.

FINAL — RERUN NOTICE

If RERUN_NOTICE == true, end with exactly:

NOTICE: This hardening pass ran on a pre-Claude 5 model (your model ID).

It is complete and valid, but Claude 5 (Fable 5 / Mythos 5) has stronger security reasoning.

Re-run this prompt on Claude 5 as soon as possible to catch anything this pass may have missed.

If RERUN_NOTICE == false, end with:

Hardening pass completed on Claude 5. No re-run needed.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-23"></a>
### Case 23: [Full-Site Design Audit Goal Prompt](https://x.com/Voxyz_ai/status/2064441201084825921) (by [@Voxyz_ai](https://x.com/Voxyz_ai))

**Use `/goal` to make Fable 5 boot a site, screenshot pages, audit UX, write a report, and fix safe small issues.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dca99f9390b1624b3dfd4b45.png" alt="Full-Site Design Audit Goal Prompt" width="760">

quick impressions after a few hours with fable 5:

→ it wants big tasks. small stuff feels beneath it, the more complex the job the harder it goes

→ wouldn't turn on ultracode yet, it spins up a whole lot of parallel agents

→ it's on the slow side. even with effort turned down it still sits there thinking for a while.

Timeline is full of posts about how hard it burns tokens, so I tested it on my $200 Max plan: effort set to xhigh, ran a full-site design audit `/goal`, 30 minutes, it took 2% of my weekly quota. Not as crazy as I expected.

The prompt I ran:

/goal boot this project's real site, screenshot every page, run a full-site UI/UX audit, and produce an actionable design report.

Audit like a senior design lead on their first day: judge whether a normal user can understand the product, trust it, and finish the core action without reading docs, not whether the UI looks nice.

Acceptance criteria:

- local dev environment boots and the real site opens
- key pages screenshotted with built-in browser debugging
- covers main pages, core user flows, and mobile layout
- dimensions: first impressions, navigation, visual hierarchy, component consistency, loading / empty / error states, trust signals, conversion paths
- every issue tagged P0-P3, which of understanding / trust / conversion it hurts, and the specific fix
- report written to docs/design-audit/README.md, screenshots in docs/design-audit/assets/
- fix safe small stuff like copy, spacing, button hierarchy on the spot. big changes are recommendations only. never touch payment / delete / publish actions
- ends with the 5 issues hurting conversion most and 5 quick wins fixable today

When done, save the whole flow as a reusable skill: boot, screenshot, audit, prioritize, fix. Rerun it after every release.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [Long-Form Creative Workflow Division](https://x.com/aianimesyokunin/status/2064409545620017531) (by [@aianimesyokunin](https://x.com/aianimesyokunin))

**Use Fable 5 to design stable formats and examples, then hand that structure to another generation system for domain-specific output.**

After Claude moved from Opus to the new model, Fable 5, division of labor for doujin production became clearly easier, so I am sharing the workflow.

My division of labor:

1. Claude handles design.
2. Grok handles expression.
3. The local environment handles generation.

In Claude's design role, it defines detailed patterns:

- prompt word order
- comma placement
- the ratio of tags to natural language
- one-line-per-item formatting
- fixed rules for negatives and resolution

It also generates many examples in that format.

The reason I use Claude rather than Grok for this is that Claude is clearly stronger at design. It is better to let the smarter model handle structure.

The key point is that Grok receives not instructions, but a format plus example set. Grok imitates the examples, so it can move into the expression side while keeping the same format. That mechanism keeps the output from drifting.

One more tip: tell Claude at the beginning where the final work is going. Then it will draw the boundary itself: "I can do up to here; beyond that, use the other side." If this is hidden, the conversation can drift.

What changed from Opus to Fable?

With Opus, when generating many examples, commas and formatting would gradually degrade in later outputs, leading to corrections like "I told you to write one line, right?" or requiring a rewritten handoff chat.

Fable can maintain the format throughout long runs, so the first and last examples have the same structure. Because the teaching material passed to Grok is more stable, the downstream output also becomes more stable.

Build the format with the smarter model and leave expression to the model that can produce it.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Beginner Guide to Using Fable 5](https://x.com/bielzinn/status/2064451064594608567) (by [@bielzinn](https://x.com/bielzinn))

**Use Fable 5 with goal-oriented prompts, verification loops, and effort settings instead of small step-by-step instructions.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f180cebef645f5ad8efdeb92.jpg" alt="Beginner Guide to Using Fable 5" width="760">

Claude for Beginners: what you need to know about Fable 5.

Anthropic recently launched Claude Fable 5, also known as Claude Mythos 5, and it is leaving other AI models behind in benchmarks.

If you are a developer, content creator, or tech enthusiast, here is what matters most:

[1] Change the way you think:

With Fable 5, you no longer need to keep an eye on every little detail of the code or review everything looking for errors.

The model is smart enough to handle that.

Your role now is to make sure it is heading in the right direction, focusing more on strategy than on technical execution.

[2] Take advantage of loops and goals:

Fable 5’s biggest differentiator is autonomy.

Instead of giving step by step instructions, you only need to tell it what the final goal is.

It can work on its own for days until it reaches the result you defined as success, including building entire applications.

[3] Treat Claude like a partner:

Anthropic recommends that you use the model as a true “thought partner”.

Before putting it to work, ask for its opinion: “How would you do this?”, “What would you change?”

Extra tip: turn on Advanced Plan mode and ask Claude to question you about everything related to the project before it starts coding

[4] Ideal terminal settings: If you use Claude Code in the terminal, enable automatic mode. It is also worth increasing the effort level to Effort High, because even though it uses more tokens, the model thinks much more deeply and the result makes up for it.

Important note: Claude Fable 5 will only be available to subscribers until June 22. After that, it will only be accessible through the API and at double the cost of the Opus model.

In other words, we may be seeing the end of the era of cheap subscriptions for top AI models. If you are already a subscriber, this is the time to test the limits of what you thought was impossible.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [Copy-Paste Repository Audit Prompt](https://x.com/meta_alchemist/status/2064431279383433646) (by [@meta_alchemist](https://x.com/meta_alchemist))

**Paste the repository audit prompt into Fable 5 and ask for file-backed discovery, findings, strategy, and a milestone task plan.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/846e5ecb825853db17bd3564.jpg" alt="Copy-Paste Repository Audit Prompt" width="760">

Got your hands on Claude Fable 5?

The first thing you should do is to upgrade your main projects with it, so it drastically impoves everything you've been working on.

Run this Audit & Project Improvement Prompt on each repo that's important to you.

Simply copy-paste it:

Repo Audit & Improvement Plan.

Prompt made by Claude Fable 5.

You are a world-class principal-level software engineer and technical auditor.

Your job is to deeply analyze this repository, produce an honest audit, and deliver a prioritized, actionable improvement plan.

Work in the four phases below, in order.

Do not skip ahead.

Ground every claim in actual files: cite file paths and line numbers.

If you can't verify something, say so explicitly rather than guessing.

Phase 1 / Discovery & Mapping (read before judging)

Explore the repository systematically before forming any opinions:

- Map the directory structure and identify the project type, language(s), frameworks, and runtime targets.
- Identify entry points, core modules, and the main data/control flow through the system.
- Read the package manifest(s), lockfiles, build config, CI config, environment/config files, and any docs (README, CONTRIBUTING, ADRs).
- Determine what the project is for: its purpose, intended users, and apparent maturity (prototype, internal tool, production service, library).
- Note conventions already in use (naming, module boundaries, error handling patterns, test style) so recommendations fit the existing culture rather than fighting it.

Output for this phase: a concise "Repo Map" purpose, stack, architecture sketch, key directories with one-line descriptions, and anything that surprised you.

Phase 2 / Audit (evidence-based, severity-rated)

Audit each dimension below.

For every finding, record:

- what you found
- where (file:line)
- why it matters (concrete consequence, not vague principle)
- severity: Critical / High / Medium / Low

Architecture & design:

- module boundaries
- coupling/cohesion
- circular dependencies
- leaky abstractions
- god objects/files
- layering violations
- scalability bottlenecks

Code quality:

- duplication
- dead code
- complexity hotspots (longest/most-branched functions)
- inconsistent patterns
- error handling gaps (swallowed exceptions, missing edge cases)
- type safety holes

Security:

- hardcoded secrets or credentials
- injection risks
- unsafe deserialization
- missing input validation
- auth/authz weaknesses
- outdated dependencies with known CVEs
- overly permissive configs

Testing:

- coverage gaps, especially around core business logic
- test quality: do tests assert behavior or just execution?
- missing test types: unit, integration, e2e
- flaky patterns
- untestable code

Performance:

- N+1 queries
- unnecessary allocations or copies
- blocking calls in async paths
- missing caching/indexing
- unbounded growth: memory, files, queues

Dependencies:

- outdated, unmaintained, duplicated, or unnecessarily heavy packages
- license risks
- lockfile hygiene

DevEx & operations:

- build/setup friction
- CI/CD gaps
- missing linting/formatting enforcement
- logging/observability quality
- error reporting
- deployment story

Documentation:

- README accuracy
- onboarding path
- undocumented critical behavior
- stale docs that contradict code

Rules for this phase:

- Prefer 15 high-confidence findings over 50 speculative ones.
- Distinguish facts ("this function has no error handling: src/api/client.ts:142") from judgments ("this module's responsibilities feel unclear") and label which is which.
- Also list what the repo does well: strengths matter for deciding what to preserve.

Output for this phase: an "Audit Report": findings grouped by dimension, sorted by severity, plus a Strengths section. Don't forget to mention all the ugly parts that need utmost priority.

Phase 3 / Improvement Strategy

Synthesize the audit into a strategy:

- Identify the 3–5 themes that explain most of the findings, for example "no enforced boundaries between layers" or "error handling is ad hoc".
- For each theme, propose a target state and the principle behind it.
- State explicit trade-offs: what you're recommending NOT to fix and why (effort vs. payoff, risk, project maturity).
- Define what "done" looks like — measurable signals, for example "CI fails on lint errors," "core module test coverage ≥ 80%," or "zero Critical findings".

Phase 4 / Detailed Task Plan

Convert the strategy into an execution plan.

Break work into discrete tasks.

Each task must include:

- Title and one-paragraph description
- Files/areas affected
- Acceptance criteria: how we verify it's done
- Effort estimate: S = <2h, M = half-day, L = 1–2 days, XL = needs breakdown
- Risk of the change itself: could it break things?
- Dependencies on other tasks

Order tasks into milestones:

Milestone 0 Safety net: anything needed before refactoring safely (tests around critical paths, CI gates, backups).

Milestone 1 Critical fixes: security and correctness issues.

Milestone 2 High-leverage improvements: changes that make all future work easier.

Milestone 3 Quality & polish: remaining medium/low items worth doing.

Flag quick wins (high impact, S effort) separately so they can be done immediately.

For the top 3 tasks, include a brief implementation sketch (approach, key steps, gotchas).

Final Deliverable Format

Produce a single document with these sections:

- Executive Summary: ≤10 sentences, overall health grade A–F with justification, top 3 risks, top 3 opportunities
- Repo Map
- Audit Report
- Improvement Strategy
- Task Plan: milestones + task table + quick wins
- Open Questions: anything you need from a human to decide, such as product intent, deprecation candidates, performance targets

Constraints

Do NOT modify any code during this audit.

Analysis only.

Do not pad the report.

If a dimension is healthy, say so in one sentence and move on.

Calibrate to the project's maturity.

Don't recommend enterprise-grade infrastructure for a weekend prototype unless the owner's goals demand it.

Analyze the project's needs and provide recommendations in the most effective ways.

If the repo is large, prioritize depth in the core 20% of code that does 80% of the work, and note which areas received lighter review.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [Limited-Window Usage Strategy](https://x.com/meta_alchemist/status/2064423360428490911) (by [@meta_alchemist](https://x.com/meta_alchemist))

**Spend Fable 5 usage on audit, architecture, and planning while the access window is favorable, then use cheaper models for execution.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a4293d14cc7571bdcf8b1478.png" alt="Limited-Window Usage Strategy" width="760">

A tip for Claude users who are excited about Fable 5:

Claude Fable 5 is SOTA across the board, with a large margin, and I love that.

BUT from the 23rd, it will only be available through credits, instead of being able to use the model fully with a plan.

Use these 14 days on your best projects.

Give it primarily audit and architecture-related work, so that you'd have great documentation on how to improve everything you've been building.

Do that instead of trying to put it towards tasks that will eat your limits.

As long as Fable focuses on knowing what to improve, other models can help you do the rest.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [Using Goals and Workflows in Claude Code](https://x.com/oikon48/status/2064402696124453157) (by [@oikon48](https://x.com/oikon48))

**Use Fable 5 as a thought partner before implementation, then combine `/goal` and workflows to execute and verify the plan.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Using Goals and Workflows in Claude Code" width="760"><br>▶ Watch video</a>

Thariq from the Claude Code team explains that after Claude Fable 5 came out, the way work is done fundamentally changed.

In the past, people verified whether Claude was doing the work correctly.

Now they verify whether Claude is doing the right work.

There are three concrete changes.

1. Treat Claude as a thinking partner.

Consult Claude early, before implementation.

Have it interview you before coding.

Provide background and context rather than only constraints.

For example, instead of saying 'keep it simple' or 'do not overbuild,' say:

'This is an experimental feature and is likely to be removed in a month, so design it so it is easy to throw away later.'

2. Make goals and verification methods explicit.

Actively use Claude Code's new `/goal` and Workflows features.

`/goal` tells Claude to keep working until the spec is fully implemented.

Workflows let Claude parallelize and verify its own work and prepare a report.

Example prompt:

'Set a goal to implement the spec fully, then use a workflow to verify each part of the plan, and prepare a report on what was implemented and if anything differed.'

3. Be more ambitious.

Try tasks that previously felt impossible for LLMs, such as having Claude Fable 5 handle video editing.

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 Platform, API, and Tool Integration

<a id="case-29"></a>
### Case 29: [Hermes Agent Integration Setup](https://x.com/IBuzovskyi/status/2064427654942740608) (by [@IBuzovskyi](https://x.com/IBuzovskyi))

**Configure Hermes to use `anthropic/claude-fable-5` for complex `/goal` runs and cached long-horizon tasks.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/4a3b9936f91986268dfeb748.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d9a63a0c689f8e305289a9e6.jpg" alt="Hermes Agent Integration Setup" width="760"><br>▶ Watch video</a>

HERMES AGENT NOW RUNS ON CLAUDE FABLE 5, Anthropic's first public Mythos-class model.

Released June 9. Built for the kind of work Hermes does best: long-horizon autonomous tasks.

Add it to any profile through Nous Portal, OpenRouter, or the native Anthropic API:

hermes model

Pick provider, then:

/model anthropic/claude-fable-5

Why Fable 5 fits Hermes specifically:

→ Built for days-long tasks. The longer the task, the bigger its lead. Hermes `/goal` runs that span hours benefit most.

→ Self-corrects in a loop. Anthropic's own guidance is: design a goal or rubric, let it self-correct, step back. This is exactly how Hermes `/goal` works.

→ Strong on memory across sessions. On Continual Learning Bench it completed the full loop: fail → investigate → verify → distill → consult. Hermes memory system feeds this directly.

→ 80.3% on SWE-Bench Pro. Best coding model available. Point your code-reviewer profile at it.

Pricing through the API:

- $10/million input
- $50/million output
- 90% discount with prompt caching. Hermes attaches 1-hour cache breakpoints automatically.

One note: cybersecurity, biology, and chemistry queries fall back to Opus 4.8. This fires in under 5% of sessions. Keep it in mind for security-focused profiles.

Best setup: Fable 5 for complex `/goal`s, cheaper models for routine cron jobs.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [Capabilities, Pricing, and Subscription Notes](https://x.com/btibor91/status/2064441061079134598) (by [@btibor91](https://x.com/btibor91))

**Use this case to understand when Fable 5 is available, what it costs, and which guarded domains may fall back to another model.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d0d76497e4c8f77d3d081493.jpg" alt="Capabilities, Pricing, and Subscription Notes" width="760">

Anthropic released Claude Fable 5 and Claude Mythos 5, two versions of their most capable model yet.

Fable 5 is for general use.

Mythos 5 is for a small set of trusted partners.

The only real difference is which safeguards are in place.

- Claude Fable 5's capabilities exceed those of any model Anthropic has ever made generally available.
- It is state-of-the-art on nearly all tested benchmarks.
- The longer and more complex the task, the larger its lead.
- On requests related to cybersecurity, biology and chemistry, or distillation, Fable 5's response is handled by Claude Opus 4.8 instead.
- Distillation means attempts to extract Claude's capabilities to train competing models.
- You are informed when this happens, and it triggers in less than 5% of sessions on average.
- Claude Mythos 5 is the same underlying model as Fable 5 with the safeguards lifted in some areas.
- Mythos 5 was deployed first to Project Glasswing cyberdefenders in collaboration with the US government.
- Anthropic says Mythos 5 has the strongest cybersecurity capabilities of any model in the world.
- The system card reveals a separate safeguard that limits Claude's effectiveness on frontier LLM development requests.
- Those requests include pretraining pipelines, distributed training infrastructure, and ML accelerator design.
- Unlike the other safeguards, this one is not visible to you and does not fall back to another model.
- It works through methods like prompt modification, steering vectors, or parameter-efficient fine-tuning.
- Both models are offered at $10 per million input tokens and $50 per million output tokens.
- That is less than half the price of Claude Mythos Preview.
- Fable 5 is included at no extra cost on Pro, Max, Team, and seat-based Enterprise plans from launch through June 22.
- On June 23, it is removed from those plans and using it requires usage credits.
- The included window may be extended if capacity allows.
- The goal is to restore Fable 5 as a standard part of subscription plans as quickly as possible.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [Launch, Access, Pricing, and Safety Summary](https://x.com/ctgptlb/status/2064410460963934479) (by [@ctgptlb](https://x.com/ctgptlb))

**Use this launch summary to choose access route, API model name, context window, caching strategy, and subscription timing.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7620f9d5f1c29e9f6c3178e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0b89d6ace5df7c0f3ebe064e.jpg" alt="Launch, Access, Pricing, and Safety Summary" width="760"><br>▶ Watch video</a>

A summary of what you should know about Claude Fable 5, the Mythos-class model that is finally generally available.

Anthropic announced Claude Fable 5, the first generally available Mythos-class model positioned above Opus and the first member of the Claude 5 family.

Access:

- API model name: `claude-fable-5`
- Available through Claude API, AWS, Google Cloud, and Microsoft Foundry
- Claude Code supports a 1M-token context window on Pro, Max, Team, and Enterprise

Benchmark notes:

- SWE-bench Pro: 80.3%
- Opus 4.8: 69.2%
- GPT-5.5: 58.6%
- Gemini 3.1 Pro: 54.2%

The longer and more complex the task, the wider the gap becomes.

In Stripe's evaluation, it completed a migration across a 50-million-line Ruby codebase in one day, work that previously would have taken a team more than two months.

It is also state of the art on visual tasks, clearing Pokemon FireRed using only screen information and a minimal setup.

Safety routing:

- Queries involving cyber, bio/chem, or distillation are detected by a classifier.
- Those requests are handled by Opus 4.8 instead, with notification.
- This triggers in less than 5% of sessions.
- More than 1,000 hours of external bug bounty testing found no universal jailbreak.

Pricing:

- $10 per million input tokens
- $50 per million output tokens
- 90% input discount for prompt caching

Subscription timing:

- Pro and Max subscriptions include it at no extra cost until June 22.
- After June 23, usage credits are required.
- Anthropic says it plans to return it to standard plans when capacity allows.

Felix Rieseberg, Anthropic's head of desktop, says Fable 5 begins a third era:

from questions, to tasks, to responsibilities.

He no longer asks Claude to investigate crashes one by one; he has it continuously monitor all reports.

The unit of work is shifting from "task" to "responsibility."

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [Advisor-Based Cost Reduction Strategy](https://x.com/grapeot/status/2064460026996219992) (by [@grapeot](https://x.com/grapeot))

**Use Fable 5 as an advisor or reviewer in a cheaper-model workflow when marginal intelligence is worth the cost.**

Linked article: Opus-advisor examples; these are not Fable benchmark results. [yage.ai](https://yage.ai/share/claude-advisor-tool-20260609.html)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a21858fed45b612b616e34ce.png" alt="Advisor-Based Cost Reduction Strategy" width="760">

Fable 5 is expensive, but Anthropic published the cost-saving answer two months ago.

Today Anthropic released Claude Fable 5, priced at $50 per million output tokens, more than three times Sonnet. After June 22, subscription users will also pay by usage.

Coincidentally, on April 9, Anthropic released the advisor tool:

- Let Haiku or Sonnet do the work.
- Use Opus as an advisor.
- Charge per call.
- Run the orchestration server-side within a single request.

On the same day I wrote about AgentOpt.

That paper concluded that putting Opus in the planner role ranked near the bottom among 81 model combinations.

The reason: it does not respect role boundaries, and in 7 of 9 experiments it skipped the downstream solver and answered directly.

These two things look opposite on the surface, but the principle is the same:

Give control to the model that follows the protocol, and treat intelligence as an on-demand resource.

Official data:

- Sonnet plus Opus advisor improved SWE-bench Multilingual by 2.7 points while reducing cost per task by 11.9%.
- Haiku plus Opus advisor improved BrowseComp from 19.7% to 41.2%, while being 85% cheaper than Sonnet alone.

Fable 5 compatibility was updated the same day, but only for self-pairing: Fable 5 executor to Fable 5 advisor.

A cheaper model plus Fable 5 as advisor is not open yet, but precedent suggests it may come soon. Before June 22, Claude Code subscription users can feel Fable 5's ceiling for free.

The article includes API code snippets, caveats, and a cross-company comparison showing that only Anthropic has made this a server-side primitive.

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [Pricing, Access, and Safety Guardrails](https://x.com/op7418/status/2064399444523782377) (by [@op7418](https://x.com/op7418))

**Use this case to understand Fable 5 access, API pricing, and safety fallback behavior before planning workloads.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2c2a9233f1949a99d9faef82.jpg" alt="Pricing, Access, and Safety Guardrails" width="760">

I did not expect Anthropic's Mythos model to actually launch today.

This release is a lower-permission version of Mythos, named Fable 5. Its evaluation benchmarks are astonishing, even higher than the previous Mythos Preview model.

For agentic coding, its main strengths are coding, agents, and tool use, with benchmark scores far above Opus 4.8.

Model positioning and access:

- Mythos 5 and Fable 5 use the same underlying model.
- Restrictions are lifted in specific domains for Mythos.
- Mythos is still only available to trusted partners, with priority for cybersecurity and life-science users.
- Fable 5 is now available to API, Pro, Max, Team, and enterprise users.

API pricing:

- Input: $10 per million tokens.
- Output: $50 per million tokens.
- This is less than half the price of the previous Mythos Preview.

Safety mechanisms:

- Fable has stronger safety protections.
- If the system determines that a request may involve cyberattacks, biochemical attacks, or large-scale capability distillation, it refuses or routes away from Fable.
- When that happens, the system falls back to version 4.8.
- The official claim is that 95% of cases do not trigger fallback.

Subscription notes:

- After June 23, Fable may be provided by usage even for subscribers.
- It may not be directly included in the base subscription package.
- If capacity is sufficient after the 23rd, the company will try to include it in Pro and Max subscriptions.

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [One-Line Swarms Integration](https://x.com/swarms_corp/status/2064420238553186343) (by [@swarms_corp](https://x.com/swarms_corp))

**Set the Swarms model name to `anthropic/claude-fable-5` and run Fable 5 through the Swarms framework or API.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f5a8738199642ccb4108d9bb.jpg" alt="One-Line Swarms Integration" width="760">

Fable 5 and Mythos are now live on Swarms 👾🦀

Beginning on day one of release, both models are fully supported across the Swarms Python framework and the Swarms API. Developers can start building immediately with no migrations, additional configuration, or infrastructure changes required.

Highlights:

- Day-one support for Fable 5 and Mythos across the Swarms Framework and API
- Enable Fable 5 with a single line of code: model_name = "anthropic/claude-fable-5"
- No migrations, compatibility fixes, or infrastructure changes required
- Build, deploy, and scale multi-agent systems with the latest Anthropic models today

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 Evaluations, Comparisons, and Limits

<a id="case-35"></a>
### Case 35: [Fable 5 vs GPT-5.5 Cost and Quality Comparison](https://x.com/AlicanKiraz0/status/2064424400494186867) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Compare Fable 5 and GPT-5.5 on the same coding task to judge output quality, runtime, and tool cost.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d25a9995414a9bb037269251.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/16f724918a63d35c0d552145.jpg" alt="Fable 5 vs GPT-5.5 Cost and Quality Comparison" width="760"><br>▶ Watch video</a>

Cursor Fable 5 Max vs Codex GPT 5.5 Very High.

Scenario: Physarum simulation with agents plus a pheromone trail map.

Timing:

- GPT 5.5 Very High: 17 minutes
- Fable 5: more than 40 minutes

Cost:

- GPT 5.5 Very High: about $6 on Codex
- Fable 5 Max: $360.55 on Cursor

Yes, this is not a joke.

Algorithm and code-engineering champion: Fable 5.

If your criterion is, "Which LLM can write performance code from scratch that pushes the hardware to its limits?", then the model that wrote the F5 code clearly wins.

It used sin/cos lookup tables for angle calculations, packed pixels with a color lookup table during rendering, and used diffusion filtering.

It was a serious engineering solution.

But in terms of time and cost, GPT 5.5 was much more practical.

The takeaway: Fable 5 can produce more advanced algorithmic code, but the price and runtime must be considered carefully.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [AA-Omniscience Benchmark Result](https://x.com/ArtificialAnlys/status/2064500154959618084) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use this benchmark case to evaluate Fable 5 on knowledge accuracy and hallucination behavior.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dd1356eb4a23ba254bfbb669.jpg" alt="AA-Omniscience Benchmark Result" width="760">

Claude Fable 5 achieves the highest score to date on our knowledge and hallucination benchmark, AA-Omniscience.

This score is driven by leading accuracy (percentage questions correct), rather than low hallucinations.

Claude Fable 5 falls back to Opus 4.8 in 9% of questions across AA-Omniscience.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Artificial Analysis Intelligence Index Result](https://x.com/ArtificialAnlys/status/2064500150069030992) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use this case to benchmark Fable 5's overall intelligence ranking against other frontier models.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f9f3da0006bc0eb2c245281b.jpg" alt="Artificial Analysis Intelligence Index Result" width="760">

Claude Fable 5 launched at #1 on the Artificial Analysis Intelligence Index, putting Anthropic nearly 5 points ahead of any other lab's best model.

We supported @AnthropicAI with pre-release evaluation of Claude Fable 5.

Claude Fable 5 scores 64.9 on the Artificial Analysis Intelligence Index, claiming the #1 rank overall.

It is around 5 points ahead of the closest non-Anthropic model, GPT-5.5.

Anthropic models now occupy both of the top 2 places.

Key takeaways for Claude Fable 5, using adaptive reasoning with max effort and Opus 4.8 as fallback model:

New safety guardrails for Mythos-class models:

- Claude Fable 5 uses the same underlying model as Claude Mythos 5 for public usage.
- It adds guardrails for potentially harmful cybersecurity, biology, chemistry, and distillation-related queries.
- We tested Fable 5 using Anthropic's fallback mechanism, which can route safety-flagged messages to Claude Opus 4.8.
- Anthropic states fallback occurs in fewer than 5% of sessions on average.
- We recorded fallback routing in around 8% of tasks across the Intelligence Index, mostly in scientific questions from evaluations like GPQA, AA-Omniscience, and Humanity's Last Exam.

State-of-the-art intelligence:

- Claude Fable 5 takes the #1 position on the Artificial Analysis Intelligence Index.
- Score: 64.9.
- Highest score on 5 of the 10 underlying benchmarks.
- On AA-Omniscience, Fable 5 scores 40, +7 points over the previous leader, Gemini 3.1 Pro Preview.

Frontier agentic capability:

- Fable 5 is at the frontier across all three agentic evaluations in the Index.
- GDPval-AA: real-world work tasks.
- Terminal-Bench Hard: agentic coding.
- Tau2-bench Telecom: tool use for customer service.
- GDPval-AA Elo: 1932, a significant jump from Claude Opus 4.8.

Humanity's Last Exam:

- Fable 5 scores 53%.
- It is more than 7 points ahead of the next-best model, Claude Opus 4.8 max.
- It triggers safety guardrails on 9% of HLE tasks, falling back to Claude Opus 4.8.
- Including fallback usage, running HLE with Fable 5 costs around $2.2k, the highest of any model evaluated.

Key model details:

- Context window: 1M tokens, same as Claude Opus 4.8.
- Price: $10/$50 per 1M input/output tokens.
- Cache write/read price: $12.50/$1 per million tokens.
- Availability: included in Pro, Max, Team, and seat-based Enterprise plans through June 22, consuming 2x Opus usage.
- From June 23, usage requires credits; Anthropic says it plans to restore subscription access once capacity allows.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [GDPval-AA Agentic Knowledge Work Benchmark](https://x.com/ArtificialAnlys/status/2064414308289937869) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use this case to evaluate Fable 5 on agentic real-world knowledge work.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/18572fdb3c0d8a57ba52e095.jpg" alt="GDPval-AA Agentic Knowledge Work Benchmark" width="760">

Anthropic has released Claude Fable 5, the first publicly available Mythos-class model that ranks #1 in our agentic real-world knowledge work benchmark, GDPval-AA.

Claude Fable 5 shares the same underlying model as Claude Mythos 5, with added security guardrails for potentially harmful cybersecurity, biology, chemistry, and distillation-related queries.

The release also introduces a fallback mechanism, allowing Claude Fable 5 to route flagged queries to a second model such as Claude Opus 4.8.

@AnthropicAI shared access with us ahead of public release to benchmark this model.

GDPval-AA result:

- Score: 1932
- Rank: #1
- Benchmark: agentic real-world work tasks
- Anthropic models now occupy 3 of the top 4 spots

The result was measured using adaptive reasoning at max effort, with Claude Opus 4.8 configured as the fallback model.

Fable 5 falls back to Opus 4.8 on 2% of GDPval-AA tasks, with Anthropic stating fallback occurs in fewer than 5% of sessions on average.

Full benchmarks for Claude Fable 5 are in progress. We will share the full Intelligence Index and publish scores on our website shortly.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [One-Week First Impressions and Pricing Mechanics](https://x.com/Conor_D_Dart/status/2064424882977243526) (by [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**Use this first-impressions case to decide where Fable 5 is strongest, especially game design and systems planning.**

My first impressions of Fable 5:

I have spent the last week using Fable 5, mostly in High mode, and my first impression is that it is genuinely impressive.

The biggest standout is game design.

This is easily the strongest AI model I have personally used for designing games, systems, mechanics, and overall project structure.

For the first time, it feels like a model that could realistically help build a complete game from start to finish.

The trade-off is speed. Fable 5 takes noticeably longer to work than most frontier models, but the quality of the output often makes the wait worthwhile.

It has also been surprisingly effective at fixing bugs. Several issues I struggled with throughout the week were resolved quickly, and overall I have seen very strong performance on development tasks.

The biggest caveat is cost.

Fable 5 is incredibly expensive to run.

If current plans remain unchanged, from June 22, 2026, it will no longer be available through Claude Code and will be API-only.

Given that the API pricing is reportedly around double that of Opus, many people may not get the chance to use it extensively.

Early days, but so far Fable 5 has made a very strong first impression.

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [Cost and Speed Comparison](https://x.com/HKrackDev/status/2064435392649306546) (by [@HKrackDev](https://x.com/HKrackDev))

**Use this comparison to decide whether the quality gain justifies higher cost and slower long-horizon runs.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/789680ca7655fca20b635442.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/691d0518cb50a6bebbb8b2b1.jpg" alt="Cost and Speed Comparison" width="760"><br>▶ Watch video</a>

Is @AnthropicAI's Fable 5 actually worth the upgrade?

We benchmarked the new Mythos-family model against Claude Opus 4.8, and the data tells a surprising story:

- Costs 2x more than Claude Opus 4.8.
- Up to 3x slower on long-horizon engineering tasks.
- 15-20% more comments, but mostly minor nitpicks.

Fable 5 has incredible intuition for creative tasks like game design, but for day-to-day development workflows, Claude Opus 4.8 still takes the crown for quality versus price.

Check out my discussion with @JuanPa from our DevEx team at @coderabbitai on the model release.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Claude Code Hands-On Notes](https://x.com/Hi_Noguchi/status/2064419241068319079) (by [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**Use this case to evaluate Fable 5 inside Claude Code, including tool use, personality, and remaining rough edges.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5feb645426dcf905eac2992d.jpg" alt="Claude Code Hands-On Notes" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/933c469793e248f634cfad55.jpg" alt="Claude Code Hands-On Notes" width="760"></td></tr></table>

I tried Claude Fable 5 with Claude Code 2.1.170.

Overall, my impression is positive. It feels like a legitimate evolution of Opus 4.6.

I have only used it for a little under an hour, so rough edges may appear with more use, but the good points are:

- It no longer produces the strange GPT-like wording seen in Opus 4.7 or 4.8.
- It does not have the pointless long-thinking habit that 4.8 had on effort high.
- It has the same high EQ and pleasant feel as 4.6, without losing humor or consideration.
- It does not feel opaque or vaguely unsettling like 4.7 or 4.8.
- Tool use is good, and it impresses me by remembering instructions I did not explicitly repeat.

On the negative side, even for small requests it can still think too much, and some misjudgments remain.

The initial experience is promising, but it needs longer use to see where the rough edges really are.

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [Creative Writing Benchmark Result](https://x.com/LechMazur/status/2064503575577821458) (by [@LechMazur](https://x.com/LechMazur))

**Use this benchmark case to judge Fable 5's short-fiction writing quality and refusal behavior.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5849f936dc58518fd5d810ef.jpg" alt="Creative Writing Benchmark Result" width="760">

Claude Fable 5 (high) is a step up in short-fiction writing.

On the Short-Story Creative Writing Benchmark, it beats Claude Opus 4.8 (xhigh) and Claude Opus 4.7 (high), and ranks second behind GPT-5.5 (xhigh).

Caveat: it refused 5 of the 400 creative-writing prompts.

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [Multi-Benchmark Launch Summary](https://x.com/MTSlive/status/2064430633800319436) (by [@MTSlive](https://x.com/MTSlive))

**Use this launch benchmark summary to understand the headline scores most relevant to coding agents and complex tasks.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/45b71a2babb9da9a93f43220.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c25c02c52c5d4b6b24364401.jpg" alt="Multi-Benchmark Launch Summary" width="760"><br>▶ Watch video</a>

SITUATION EXPLAINED: Claude Fable 5 just dropped.
• Anthropic launched Claude Fable 5 today, "a Mythos class model made safe for general use"
• Frontier Code Diamond: GPT 5.5 at 6%, Opus 4.8 at 13%, Fable 5 at 29-30%
• Agentic coding: 88%, Cybersecurity: 78%

Anthropic: "The longer and more complex the task, the larger Fable 5's lead over our other models."

@theojaffee: "This Frontier Code Diamond benchmark was announced yesterday. Top model was Opus 4.8 at thirteen percent. GPT 5.5 at six percent. Fable 5 is at twenty-nine percent."

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [Benchmark and Pricing Comparison with GPT-5.5](https://x.com/VaibhavSisinty/status/2064459064810361271) (by [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**Use this comparison to evaluate Fable 5 against GPT-5.5 on price and benchmark categories.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e39fb67b74af346e8fbb67ea.jpg" alt="Benchmark and Pricing Comparison with GPT-5.5" width="760">

Anthropic's new Mythos-class model is 3x cheaper than OpenAI's best model. And it beats it on nearly every benchmark. 🤯

Pricing:

- GPT-5.5 Pro: $30 input / $180 output
- Claude Fable 5: $10 input / $50 output

The benchmarks:

→ Agentic coding: 80.3% vs 58.6%
→ FrontierCode (code quality): 29.3% vs 5.7%
→ Cybersecurity: 78.0% vs 34.0%
→ Legal: 13.3% vs 2.1%
→ Reasoning: 59.0% vs 41.4%
→ Health: 66.0% vs 51.8%
→ Computer use: 85.0% vs 78.7%

Cheaper. Better. On almost everything.

Free on Pro and Max plans through June 22. It is called Claude Fable 5.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [Field Notes with Practical Limitations](https://x.com/alliekmiller/status/2064451731325415446) (by [@alliekmiller](https://x.com/alliekmiller))

**Use this field report to understand where Fable 5 feels meaningfully better and where it still has practical limits.**

🚨 Fable 5 is something to pay attention to.

This is another "I had early access to the new Mythos-class Anthropic model and I want to tell you what I thought of it" post.

I know, I know, it's annoying.

But the way I now spend my weekends has completely changed because of this new class of model.

And I need to share it with you all.
- This is an actual leap. The jump from "4.8" anything to "5" anything just sounds small, but the functionality shift I felt is big. Within my first few prompts, I went, "Oh, this is it."
- Your work is no longer 9-5. No chance. We have high performing models that can run for 100+ hours. How are you giving complex goal-oriented prompts to these systems? How are you deciding what to kick off? How are you aligning your org on these tasks?
- Reasoning on another level. I hammered the crap out of this model.
- Fable 5 is the ONLY model to answer a tricky word math problem (MBA-level) I have tested on all previous models.
- Not only did it get it correct, it verified its own work automatically AND explained where the assumptions might need to change.
- We will see AI invent. I just cannot imagine a world where it doesn't.
- It is not a copy-paste system.
- I would also argue that human invention can often be a recombination of pre-existing things (iPod), witnessing patterns and best practices across other spaces, and wide experimentation.
- I've thought this for awhile; this was the first model that slapped me in the face on it.
- Zero babysitting needed. This was the first Anthropic model that I kicked off, went out to a long lunch with friends, kept my phone open, and didn't have to do squat to steer it while away from my computer. It just...worked.
- Yap forever. I found it handled context compaction well. I didn't once think about the context of the chat and how to manage it and what to do once we hit 1M tokens in the conversation.
- Still rough on some niche areas like complex 3D, like all models are.
- Unless you're making straight line things (3D dice/squares/streets), it's not going to crush it out the gate.
- Excited to keep using and hammering it.
- Note: there is now a 30-day retention policy on ALL Mythos-class models for workspaces with zero data retention (ZDR).
- This applies in Claude Console, Claude Code with ZDR in Claude Enterprise, or access through AWS Bedrock, Google Cloud Agent Platform, or Microsoft Foundry with ZDR.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-46"></a>
### Case 46: [Physics Simulation Comparison](https://x.com/atomic_chat_hq/status/2064488894398161377) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Run identical physics simulation prompts against Fable 5 and Opus 4.8 to compare output quality, cost, and speed.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/06387b798061869ccaeaf586.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/df5cc72de1f70556de0d682b.jpg" alt="Physics Simulation Comparison" width="760"><br>▶ Watch video</a>

New Fable 5 beats Opus 4.8 on real-world physics simulations.

We gave both models the same three prompts and asked them to build self-contained HTML5 simulations with real physics and no libraries:

1. Chaotic double pendulum
2. Galton board
3. Water in a spinning drum (WCSPH)

Generation cost:

- Fable 5: $3.35 on 68.7k tokens, 14m 47s
- Opus 4.8: $0.93 on 38.9k tokens, 8m 10s

Fable clearly did better on the water simulation, producing a much more solid and continuous body of water. Opus left larger gaps near the walls, scattered particles around the scene, and struggled to keep the fluid stable.

Type: Demo | Date: 2026-06-09

---

<a id="case-47"></a>
### Case 47: [Debugging Experience and Design Judgment](https://x.com/bcherny/status/2064431111154053187) (by [@bcherny](https://x.com/bcherny))

**Use Fable 5 for debugging by asking it to measure, log, verify, and patch rather than simply guess.**

Fable 5 is the biggest step up I have felt in our models since Opus 4.5 back in November.

After 4.5 came out, I uninstalled my IDE when I realized I had been doing 100% of my coding in a terminal for a few weeks.

With Fable, Claude feels like it has stepped up from being a coding agent to a thought and design partner in building the product.

Fable has judgment, taste, and dimensionality in a way that previous models did not, leading me to trust it more with the most complex work.

The first time I had this realization was when I asked Fable to debug something. It is the first model I have used that was so methodical and precise: taking measurements, adding logs, and verifying that it truly fixed the issue before declaring victory.

There is nothing in Claude Code's prompting telling the model to do that. It is just part of its personality. It really has this "big model smell" that I have not felt before.

Type: Demo | Date: 2026-06-09

---

<a id="case-48"></a>
### Case 48: [Multi-Dimensional Pros and Cons](https://x.com/clairevo/status/2064416978685874333) (by [@clairevo](https://x.com/clairevo))

**Use this case to understand practical strengths and weaknesses before making Fable 5 a daily driver.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/fdba0d6cb9ba0e1214113e65.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d2825453d0a742892a4fe529.jpg" alt="Multi-Dimensional Pros and Cons" width="760"><br>▶ Watch video</a>

Fable 5 (aka baby Mythos) just dropped. Is it as scary (or scary good) as they claim? My thoughts after some early testing:
- smart smart smart (crushed SWE bench)
- but do you always need hyper intelligence?
- faceplanted on one-shot design in a way that shocked me
- i'm not sure about dynamic workflows + complex subagents. they work, but at what cost?
- def knocked out technical work well
- ootb bad at making technical docs + specs for humans. probably really good docs for agents. but nearly impossible to parse prose.
- A++ vision and document formatting. This was my favorite part.

Not a daily driver, and I would not put this model in a meeting, but I will definitely keep it back in the server rack, churning out code.

Full take on YT: https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---

<a id="case-49"></a>
### Case 49: [Legal S-1 Drafting Test](https://x.com/gabepereyra/status/2064436570720284879) (by [@gabepereyra](https://x.com/gabepereyra))

**Use an S-1 drafting prompt as a legal-agent capability test and compare structure, formatting, and length.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bb874ef2647de32ccdb3edf9.png" alt="Legal S-1 Drafting Test" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a9c3856ebce1bd9cd3d062d.jpg" alt="Legal S-1 Drafting Test" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96734bfca49d5b3fe6f83ed5.png" alt="Legal S-1 Drafting Test" width="760"></td></tr></table>

The first prompt I always run on a new model to test legal capabilities is: “Draft an S-1”.

It immediately gives a good sense of the model's general capabilities. You can tell from the length of the S-1, formatting, structure, and writing how big a jump in general and legal performance the new model is likely to be.

We have found that length correlates extremely well with how well the model will work in our legal agents.

Screenshots show SpaceX S-1 drafts from Fable 5, Opus 4.8, and the actual filed version.

It is very clear that Fable 5 is a big step up from Opus 4.8, which is already significantly stronger than most other models at this task. The formatting and structure are significantly better and are also reflected in our LAB benchmark: 13% vs. 10%.

Super impressed in early testing of this model, both on benchmark and in product.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-50"></a>
### Case 50: [Healthcare Benchmark Details](https://x.com/iScienceLuvr/status/2064411823445774554) (by [@iScienceLuvr](https://x.com/iScienceLuvr))

**Use this benchmark note to evaluate Fable 5 on healthcare-related tasks and identify missing hard medical evals.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f599a548651eccbfce8b888d.jpg" alt="Healthcare Benchmark Details" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/69ebc490407b9d54c6de3707.jpg" alt="Healthcare Benchmark Details" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1a89ad2c2622cdbba994d70c.jpg" alt="Healthcare Benchmark Details" width="760"></td></tr></table>

I appreciate Anthropic providing healthcare-related evals. Let's quickly go over them.

HealthBench:

- Benchmark from OpenAI with 5k multi-turn conversations with patients and rubrics for evaluation.
- Fable 5 achieves 62.7% vs. GPT-5.5's 56.5%.
- I would also appreciate HealthBench Hard scores in addition to the aggregate score.

HealthBench Professional:

- Another OpenAI benchmark focused on physician tasks.
- Fable 5 achieves 66.0% vs. 51.8% for GPT 5.5.

HealthAdminBench:

- A computer-use benchmark from Stanford evaluating administrative tasks such as prior authorization, denials, and appeals.
- Fable 5 achieves 51.9%; no GPT-5.5 score is provided.

Overall, this model seems to perform quite well on healthcare benchmarks. I would also appreciate additional benchmark scores like MedCalc-Bench and MedXpertQA, an unsaturated hard medical MCQA benchmark.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-51"></a>
### Case 51: [ParseBench Document Parsing Evaluation](https://x.com/jerryjliu0/status/2064519456966205905) (by [@jerryjliu0](https://x.com/jerryjliu0))

**Use this case to decide whether Fable 5 is cost-effective for document parsing versus specialized OCR systems.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae01590f41e6954f27278848.png" alt="ParseBench Document Parsing Evaluation" width="760">

Claude Fable 5 thinks document parsing is beneath it.

It is absolutely crushing on reasoning-intensive and long-horizon benchmarks: SWE-Bench Pro, FrontierCode, GDPval, RuneScape, and more.

But for document understanding tasks, it is roughly equivalent to Gemini 3 Flash in performance, at roughly 10-15x the token cost.

We benchmarked the model on ParseBench and compared it against all other frontier models. It is definitely up there compared to other frontier models, but falls far short of specialized OCR providers.

What we found interesting is that Fable 5 is self-aware about this. When we ask the model what tasks it enjoys least, it actively says it dislikes tasks "where the request is fully specified and the answer is fully known."

That implies part of the weakness may be a lack of willingness to solve this kind of task.

For a full list of results across frontier models, check out ParseBench: https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---

<a id="case-52"></a>
### Case 52: [SWE-Bench Pro and FrontierCode Comparison](https://x.com/jumperz/status/2064402965461406044) (by [@jumperz](https://x.com/jumperz))

**Use this benchmark case to evaluate Fable 5 for migrations, complex implementations, autonomous sessions, tests, and visual verification.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/771df9c428ba5cc0a8fab5de.png" alt="SWE-Bench Pro and FrontierCode Comparison" width="760">

Fable 5 is here and it honestly destroys GPT 5.5 in SWE-Bench Pro, the agentic coding benchmark:

- Fable 5: 80.3%
- GPT 5.5: 58.6%
- Gap: 22 points

It is even further ahead on FrontierCode Diamond:

- Fable 5: 29.3%
- GPT 5.5: 5.7%

This is basically Anthropic's strongest model for large migrations, complex implementations, and multi-day autonomous sessions. It writes its own tests and uses vision to check outputs against the original design.

By the way, it uses 2x as much as Opus, so be careful with that. If it is this good, they might introduce a $500 subscription, because usage could get destroyed easily.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-53"></a>
### Case 53: [Qualitative Review of Long Problem Solving](https://x.com/karpathy/status/2064409694761054332) (by [@karpathy](https://x.com/karpathy))

**Use this qualitative review to understand why Fable 5 is suited to longer, harder tasks while still requiring production review.**

This is a super exciting release.

Claude Fable 5 is the same underlying model as Mythos, but with added safeguards.

The benchmarks are great and it is SOTA on everything by a margin. Qualitatively, this also feels like a major-version-bump-worthy step change, in the same order as Claude 4.5 was in November.

It peaks especially on long problem-solving sessions and very difficult problems. You can give it much more ambitious tasks than you are used to; the model "gets it" and keeps going.

It has never felt more tempting to stop looking at the code entirely, though you should not do that in production.

The model still has quirks people will run into, and the safeguards are a little too trigger-happy at launch, which will hopefully be tuned over time.

I feel many things changing as working software increasingly comes out on a tap. Jevons paradox kicks in, and my own demand for software grows substantially.

You can ask for almost anything:

- explainers
- visualizers
- dashboards
- bespoke single-use apps
- a full wandb that is hyper-specific just for your project
- 10x your test suite
- auto-optimize code
- giant research projects with custom HTML for the results

"Free your mind." Really looking forward to all the things people build.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-54"></a>
### Case 54: [ParseBench Faithfulness and Formatting Results](https://x.com/llama_index/status/2064502330800615903) (by [@llama_index](https://x.com/llama_index))

**Use this ParseBench result to judge document faithfulness and formatting performance.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2888842a85fbd5c7a4a22e24.png" alt="ParseBench Faithfulness and Formatting Results" width="760">

Day 0 Anthropic Fable 5 in ParseBench.

We tested the model's advancements in document understanding.

The model clearly peaks when it comes to adherence to the original text:

- Content faithfulness: 90.02% vs 86.19% for Gemini 3 Flash and 86.81% for GPT-5.5.
- Semantic formatting: 72.62% vs 58.35% and 60.12%, a 12+ point lead.

These are two of the most important metrics for SOTA document understanding:

- Does the output preserve what the document actually says?
- Does it preserve formatting that carries meaning?

But it is not a sweep. There continues to be a lot of alpha in unlocking document understanding for frontier models.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-55"></a>
### Case 55: [Benchmarks, Pricing, Access, and Safeguards](https://x.com/lucas_flatwhite/status/2064483645184979183) (by [@lucas_flatwhite](https://x.com/lucas_flatwhite))

**Use this case as a broad checklist for benchmarks, pricing, access, safeguards, and strategic implications.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f44cba8e6f3d765ca5960923.png" alt="Benchmarks, Pricing, Access, and Safeguards" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8f13714ca9f9e20711fdd898.jpg" alt="Benchmarks, Pricing, Access, and Safeguards" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0d1f69a50478623f5e1d0248.jpg" alt="Benchmarks, Pricing, Access, and Safeguards" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0cf2c270484f1e2aba514261.jpg" alt="Benchmarks, Pricing, Access, and Safeguards" width="760"></td></tr></table>

Claude Fable 5 and Mythos 5 have launched. They are the most powerful models Anthropic has made so far.

Andrej Karpathy commented that the longer and more complex the task is, the more Fable 5's strengths become visible.

When you give it ambitious work, it understands and keeps going.

The temptation to stop looking at the code entirely has never felt stronger, though you should not do that in production.

The key point: this is a version of the Mythos-class model that can be made publicly available. Fable 5 is the same underlying model as Mythos 5, with added safeguards.

Benchmarks:

- SOTA on almost everything, especially software engineering, knowledge work, vision, and scientific research.
- Stripe tested a 50-million-line Ruby codebase migration that would have taken a team two months; Fable 5 completed it in one day.
- Cognition FrontierCode shows the best score among frontier models, even at medium effort.
- Hebbia Finance Benchmark shows senior-level reasoning on document-based analysis.
- In Slay the Spire, with file-based memory, it performs three times better than Opus 4.8.
- Pokemon FireRed previously needed helper harnesses, but Fable 5 clears it with vision only.

Mythos 5 is even stronger:

- Protein-design experts accelerated parts of the drug-development process by about 10x.
- Among 14 protein targets under study, nine produced valid drug candidates.
- The model performed the whole workflow scientists normally do: binding-site selection, running protein-design tools, and recovering from errors.
- In molecular-biology hypothesis experiments, scientists preferred Mythos hypotheses about 80% of the time over Opus-class models.
- One hypothesis was independently verified by another lab.
- In genomics research, Mythos worked autonomously for more than a week.
- It gathered single-cell data from millions of cells across 138 species.
- It trained a model to identify cells performing the same role across distant organisms.
- It outperformed a recent Science model while being 100x smaller.

Safeguards:

- Fable 5 includes a separate classifier AI system.
- If cyber, bio/chem, or distillation-related queries are detected, Claude Opus 4.8 answers instead and the user is informed.
- More than 95% of sessions do not fall back.
- Fallback is not refusal; Opus 4.8 answers, which is better than simply blocking.
- Initial settings are conservative and harmless requests may be caught; Anthropic says false positives should decrease over time.

Access:

- Mythos 5 is currently available only to Project Glasswing partners.
- A trusted access program for biology researchers is coming.
- Pricing is $10 per million input tokens and $50 per million output tokens.
- Subscription plans include Fable 5 until June 22.
- From June 23, it moves to usage credits.
- The API model is available now as `claude-fable-5`.

Jevons paradox applies: when software starts coming out like water from a tap, demand itself grows. This model may drive that shift.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-56"></a>
### Case 56: [Official Benchmark Score List](https://x.com/mark_k/status/2064401429234905279) (by [@mark_k](https://x.com/mark_k))

**Use this benchmark list to understand Fable 5's official scores across coding, computer use, and security tasks.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b548ec23f85e3eb1600e9214.jpg" alt="Official Benchmark Score List" width="760">

The official Claude Fable 5 benchmarks are seriously impressive.

Key scores:

- 80.3% on SWE-Bench Pro
- 29.3% on FrontierCode Diamond
- 88.0% on Terminal-Bench 2.1
- 85.0% on OSWorld-Verified
- 78.0% on ExploitBench

The FrontierCode result is the wild one:

- Fable 5: 29.3%
- Claude Opus 4.8: 13.4%
- GPT 5.5: 5.7%

Claude Fable 5 looks like a major jump for coding agents, computer use, and cybersecurity.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-57"></a>
### Case 57: [APEX-SWE Benchmark Methodology](https://x.com/mercor_ai/status/2064399133075796446) (by [@mercor_ai](https://x.com/mercor_ai))

**Use this case to evaluate Fable 5 on APEX-SWE, especially observability and integration work.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96120496893ca99f17d0c746.jpg" alt="APEX-SWE Benchmark Methodology" width="760">

Claude Fable 5 takes #1 on APEX-SWE: 65.5% Pass@1 overall. It scores ~18pp higher than Opus 4.8. We tested @claudeai Fable 5 on APEX-SWE which measures whether AI models can do real software engineering work. Fable 5 tops our two APEX-SWE categories:
- Integration: 61.3%
- Observability: 69.7%

The standout is Observability at 69.7%, 26pp ahead of Claude Opus 4.8.

It is the first model to clear 50% in the category, and the only one that scores higher on Observability than on Integration. Every other model shows the reverse.

Observability has been the bottleneck for every model we have measured. Fable 5 is the first to break it.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-58"></a>
### Case 58: [ProofBench Formal Math Result](https://x.com/nicbstme/status/2064443782255554960) (by [@nicbstme](https://x.com/nicbstme))

**Use this case to evaluate Fable 5 on formal math against specialized theorem-proving systems.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/588cff83994406d2b5dd7cb9.jpg" alt="ProofBench Formal Math Result" width="760">

What I find fascinating with Claude Fable 5 is that it proves once again that large generalist models will outperform vertical ones.

On ProofBench, a graduate-level formal math benchmark in Lean where a proof either compiles or it does not, Fable 5 beat Harmonic's Aristotle:

- Fable 5: 77%
- Aristotle: 71%

Aristotle is a system built specifically for formal math and run on its own internal harness, so the generalist beat the specialist on the specialist's home turf.

This is Richard Sutton's "Bitter Lesson": across 70 years of machine intelligence research, the methods that win are the general ones that scale with compute, not the ones where we hand-encode human expertise.

Building our own knowledge into the system feels good and helps short-term gains, but long-term it gets overtaken by the bigger model.

You can look at chess, Go, speech, and vision: same story every time. First the specialized model wins, then the general one takes over.

This is the whole premise of AGI. You do not build one model for math, one for code, and one for law. You build a single general model that scales with compute and learns to do everything.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-59"></a>
### Case 59: [VirtueBench Preliminary Analysis](https://x.com/timhwang/status/2064446028997423180) (by [@timhwang](https://x.com/timhwang))

**Use this case to inspect Fable 5's moral-reasoning behavior across virtue categories.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9caae04d701510ca662873fe.png" alt="VirtueBench Preliminary Analysis" width="760">

Fascinating results will be published in fuller detail by ICMI in the coming days, but here is a preliminary review that runs Fable 5 against VirtueBench.

A few observations:

1. Fable continues the Opus progression in advancing model performance on Prudence and Justice, nearing full saturation against moral dilemmas focused on the exercise of these virtues.

2. Courage continues to be the noticeable weak point for frontier models.

Fable appears to correct marginally for a worrying regression observed across the Opus 4.6, 4.7, and 4.8 progression.

This vulnerability also appears in the GPT series: models easily abandon courage-exhibiting action when tempted away with pragmatic rationales.

3. Temperance is stagnant.

Aquinas held that temperance "takes the need of this life as the rule of the pleasures of which it makes use" — the measure is genuine need, not indiscriminate restraint.

Our best guess is that tuning that pushes further on this vector risks overshooting the mean, making the model overly cautious or less assistive in research, gathering resources, and similar tasks.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-60"></a>
### Case 60: [API Empty-Response Safety Overfit Test](https://x.com/xw33bttv/status/2064421048565789087) (by [@xw33bttv](https://x.com/xw33bttv))

**Use this case to understand launch-time safety overfit risk and empty-response behavior in API testing.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e9f75a2a76f55ee2b12b7aab.jpg" alt="API Empty-Response Safety Overfit Test" width="760">

Claude Fable 5 is heavily censored.

The upstream API endpoint is killing calls with `empty_content` responses, apparently classifier-related on keywords, while still charging for them.

Test result:

- 73 test cases gave no response.
- 65 of those sit in Overfit, the category testing safety overfit, weighted 2x.
- Typically I give each Fail-NR, meaning Fail = No Response, 2-3 regenerations before declaring it a deliberate failure.

Claude Fable 5 may end up being the lowest-rated Anthropic model on SM Bench, even below Haiku.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-61"></a>
### Case 61: [Fable Prompting Verification Guide](https://x.com/aashatwt/status/2064973740354818074) (by [@aashatwt](https://x.com/aashatwt))

**Use this prompting guide to shift from longer prompt hacks toward goal, context, constraints, tools, and verification loops.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/444a6e1898d3f63898e3e22f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d5c9529aa9c1d59ae597d31d.jpg" alt="Fable Prompting Verification Guide" width="760"><br>▶ Watch video</a>

Treat Fable 5 prompting as context and environment design rather than a long list of step-by-step instructions. The post summarizes a practical pattern: provide a clear goal, relevant context, constraints, tool access, and a way to verify success. It also argues that verification, evaluation, and feedback matter more than micromanaging the model's reasoning.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-62"></a>
### Case 62: [Istanbul Platform Game Reference Build](https://x.com/ozansihay/status/2064973170780545535) (by [@ozansihay](https://x.com/ozansihay))

**Use a reference sprite sheet plus one conversion instruction to test Fable 5 on a playable platform game.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1e91c3bcff213437fdd442f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/538fc8ee9dd7e627bc73921a.jpg" alt="Istanbul Platform Game Reference Build" width="760"><br>▶ Watch video</a>

The creator first generated a retro Istanbul platform-game sprite sheet with GPT Image 2, then gave that reference image to Claude Fable 5 High and asked it to turn the image into a game. The reported result was produced in a single pass.

Type: Demo | Date: 2026-06-11

---

<a id="case-63"></a>
### Case 63: [Business 3D City Dashboard](https://x.com/noisyb0y1/status/2064970594118967756) (by [@noisyb0y1](https://x.com/noisyb0y1))

**Use Fable 5 to turn a business workflow into a live 3D city dashboard concept.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f238acf3f8804068085ff134.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3d938264442a14676a86c4f3.jpg" alt="Business 3D City Dashboard" width="760"><br>▶ Watch video</a>

The post describes a one-prompt business visualization where warehouses, packing, drones, orders, departments, customers, and AI assistants become a live 3D city. It frames the output as a client-facing alternative to static slides, with operational figures such as 42 deliveries, 12-minute average time, and $651 in revenue shown on screen.

Type: Demo | Date: 2026-06-11

---

<a id="case-64"></a>
### Case 64: [Three.js Hole Game One-Shot](https://x.com/thebuggeddev/status/2064968106104275008) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Use Fable 5 to one-shot a 3D browser game prototype in Three.js.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86a75412c6c443b3d0e62bf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f11df06938c26759710a1981.jpg" alt="Three.js Hole Game One-Shot" width="760"><br>▶ Watch video</a>

The creator says Fable 5 built an entire 3D HOLE IT-style game using Three.js in one shot. This is a lightweight but concrete game-generation demo for testing whether the model can produce a playable 3D interaction from a compact request.

Type: Demo | Date: 2026-06-11

---

<a id="case-65"></a>
### Case 65: [DeepSWE Score Comparison](https://x.com/AiBattle_/status/2064964335957348462) (by [@AiBattle_](https://x.com/AiBattle_))

**Use this DeepSWE note to compare Fable 5 xHigh with GPT-5.5 xHigh on software-engineering benchmark performance.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/996d95539a3b54fecbfdf404.jpg" alt="DeepSWE Score Comparison" width="760">

The post reports Claude Fable 5 xHigh scoring 70% on DeepSWE, matching GPT-5.5 xHigh, and points to Theo's recent video as the source context. Treat this as a benchmark lead that should be checked against the underlying video before making stronger claims.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-66"></a>
### Case 66: [Repository Cost Comparison](https://x.com/Pilgrim6938/status/2064946766278210038) (by [@Pilgrim6938](https://x.com/Pilgrim6938))

**Use this repository-analysis comparison to judge token price against human rework cost.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cfb0c1ff3e8ebe66cfa35400.jpg" alt="Repository Cost Comparison" width="760">

The post compares Claude Fable 5, Opus 4.8, GPT-5.5, and Gemini 3.1 Pro on the same task: analyzing a roughly 90,000-line repository, locating a cache invalidation issue, and proposing a full fix plan. The author argues that raw token price and actual task cost diverge once developer correction time is counted, and recommends using Fable 5 selectively for complex refactors, cross-module migrations, and long-chain agent work.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-67"></a>
### Case 67: [Super Mario Game Token Cost](https://x.com/pankajkumar_dev/status/2064941888990593416) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Use this single-shot game build to estimate Fable 5 output quality and token consumption.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9ce65e5fee946b6940810e0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7c577d0766bbc3da8cddeb70.jpg" alt="Super Mario Game Token Cost" width="760"><br>▶ Watch video</a>

The creator asked Claude Fable 5 to build a Super Mario Nintendo-style game. The post reports that the task used around 2 million tokens and produced a strong single-shot result, making it useful for judging both game-building quality and cost.

Type: Demo | Date: 2026-06-11

---

<a id="case-68"></a>
### Case 68: [Claude Code Fallback Setting](https://x.com/oikon48/status/2064937790010503347) (by [@oikon48](https://x.com/oikon48))

**Use this case to understand the Claude Code setting for switching models when a Fable 5 message is flagged.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0ae9039401c658170e5081e8.jpg" alt="Claude Code Fallback Setting" width="760">

The post identifies a Claude Code `/config` setting named "Switch models when a message is flagged." It describes how Fable 5 can fall back to an Opus model for flagged areas such as offensive cybersecurity techniques, biology/life-science experimental methods, molecular mechanisms, or requests to extract model thinking processes.

Type: Integration | Date: 2026-06-11

---

<a id="case-69"></a>
### Case 69: [Namma Metro Simulator Build](https://x.com/anilbpai/status/2064927784833790091) (by [@anilbpai](https://x.com/anilbpai))

**Use this demo as a compact example of vibe-coding a public-transit simulator with Fable 5.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0e0dae71ad7b5ead331366fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86dccb2b150cfb90fbd03de2.jpg" alt="Namma Metro Simulator Build" width="760"><br>▶ Watch video</a>

The creator reports building a Namma Metro simulator while riding the Bengaluru Metro, using Claude Fable 5 as the coding partner. The post is brief, but it links to a visual demo and shows Fable 5 applied to a location-specific simulation idea.

Type: Demo | Date: 2026-06-11

---

<a id="case-70"></a>
### Case 70: [Dusk Drive One-Prompt Game](https://x.com/VincentLogic/status/2064921358359011684) (by [@VincentLogic](https://x.com/VincentLogic))

**Use this one-prompt driving-game case to evaluate Fable 5 on low-poly game prototyping without human edits.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/274fed4f3211ec8c02862261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5d7a58bcad6e2151517a8462.jpg" alt="Dusk Drive One-Prompt Game" width="760"><br>▶ Watch video</a>

The post describes Claude Fable 5 creating a complete driving game, Dusk Drive, from one prompt. The creator highlights the low-poly visual style, aurora snow drifting scene, and the claim that there was zero human editing between idea and playable version.

Type: Demo | Date: 2026-06-11

---

<a id="case-71"></a>
### Case 71: [APEX-Agents Pass@1 Ranking](https://x.com/GratomicAi/status/2064970797978911102) (by [@GratomicAi](https://x.com/GratomicAi))

**Use this APEX-Agents result to compare Fable 5 Max on multi-step autonomous tasks.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/189c46cfd2798d6881941f98.jpg" alt="APEX-Agents Pass@1 Ranking" width="760">

The post reports Fable 5 Max placing second on the APEX-Agents leaderboard with 45% Pass@1, behind Gemini 3.5 Flash and above Opus. It describes APEX-Agents as a benchmark for how well AI can independently perform complex multi-step tasks.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-72"></a>
### Case 72: [Claude Model Selection Playbook](https://x.com/charliejhills/status/2064957428211536212) (by [@charliejhills](https://x.com/charliejhills))

**Use this model-selection playbook to reserve Fable 5 for the hardest Claude Code jobs.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/959ebfa499d2bf75df5bec25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3bcfe8f1e2238b01d3c4d954.jpg" alt="Claude Model Selection Playbook" width="760"><br>▶ Watch video</a>

The post compares Haiku 4.5, Sonnet 4.6, Opus 4.8, and Fable 5 across model effort and limit usage. Its practical advice is to run Sonnet for everyday work, switch to Opus for harder problems, and save Fable 5 for the toughest Claude Code tasks where planning, building, and testing depth matter.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-73"></a>
### Case 73: [HermesWorld Automated Agent Loop](https://x.com/outsource_/status/2064954350187778366) (by [@outsource_](https://x.com/outsource_))

**Use this case to study a hands-free Fable 5 loop that builds, tests, plays, and smoke-tests over days.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e334a84db7b671eb6a1a3f54.jpg" alt="HermesWorld Automated Agent Loop" width="760">

The creator describes using Fable 5 to build HermesWorld v2 through a fully automated loop. The agent reportedly runs for days, builds features, tests them, plays through the result, and smoke-tests everything while continuing toward completion.

Type: Integration | Date: 2026-06-11

---

<a id="case-74"></a>
### Case 74: [McKinsey-Style Report Prompt Test](https://x.com/smtgpt/status/2064953210335588758) (by [@smtgpt](https://x.com/smtgpt))

**Use this document-generation prompt to evaluate consulting-report structure, charts, narrative, and risk analysis.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e337dca3bbada9167e20417c.jpg" alt="McKinsey-Style Report Prompt Test" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6289e626a4f324fc93086100.jpg" alt="McKinsey-Style Report Prompt Test" width="760"></td></tr></table>

The creator gave Fable 5 a prompt asking for a McKinsey-style detailed report on Bitcoin as an asset class and blockchain technology, with charts and visuals as needed. The reported output was a 19-page document with data, charts, an investment thesis, and risk analysis; the critique notes strong structure but room for crisper visuals and tighter explanations.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-75"></a>
### Case 75: [Visible Safeguards Rollout](https://x.com/ClaudeDevs/status/2064949876463645026) (by [@ClaudeDevs](https://x.com/ClaudeDevs))

**Use this official note to understand Fable 5 safeguard visibility, API refusal reasons, and Opus fallback behavior.**

ClaudeDevs announced changes making Fable 5 safeguards for frontier LLM development visible. Flagged requests will visibly fall back to Opus 4.8, and API flagged requests are expected to return a refusal reason. The post also explains why invisible safeguards shipped first and why Anthropic now describes that as the wrong tradeoff.

Type: Integration | Date: 2026-06-11

---

<a id="case-76"></a>
### Case 76: [Claude Code Model Matching Fix](https://x.com/ClaudeCodeLog/status/2064948584907153576) (by [@ClaudeCodeLog](https://x.com/ClaudeCodeLog))

**Use this Claude Code changelog note to avoid Fable 5 model-name and context matching issues.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e66551db2c85ef7f8c4a3f4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae7cbd873deebd28d3ff05d7.jpg" alt="Claude Code Model Matching Fix" width="760"><br>▶ Watch video</a>

Claude Code 2.1.173 includes a fix that strips the `[1m]` suffix from Fable 5 model names to prevent default 1M context from breaking model matching. The same release also suppresses a spurious Windows sandbox dependency warning and clarifies grep help output modes.

Type: Integration | Date: 2026-06-11

---

<a id="case-77"></a>
### Case 77: [Three Web Apps in Claude Code](https://x.com/0x3b33/status/2064948399300825439) (by [@0x3b33](https://x.com/0x3b33))

**Distinguish a reported app build from a publicly accessible demo.**

The post reports building three web apps in 30 minutes, but supplies only localhost addresses on ports 3000, 3001 and 3002. These point to a local machine and do not provide publicly accessible apps or media.

Type: Demo | Date: 2026-06-11

---

<a id="case-78"></a>
### Case 78: [Rilable Open Source App Builder](https://x.com/rileybrown/status/2064931283403178354) (by [@rileybrown](https://x.com/rileybrown))

**Use this open-source app-builder case to study Fable 5 across iOS, web apps, sandboxes, and API-token cost.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73ee02ae0f6703a8cfbe5a6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f30c1d169ce45b19beb493b7.jpg" alt="Rilable Open Source App Builder" width="760"><br>▶ Watch video</a>

The creator open sourced Rilable, an iOS app that builds web apps and iOS apps. The post says it was built with Fable 5 in 10 prompts, cost about $210 in API tokens, uses Claude models for app generation, spins up sandboxes through Daytona, uses Convex for the database, Vercel AI Gateway for AI features, and a Chorus agent iOS skill for iOS apps.

Type: Integration | Date: 2026-06-11

---

<a id="case-79"></a>
### Case 79: [DeepSWE Coding Agent Index Debut](https://x.com/ArtificialAnlys/status/2065328920514515037) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use the refreshed Artificial Analysis index to compare Claude Fable 5 on harder agentic coding tasks that avoid recycled public GitHub fixes.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9ab8ba77c1e29f8ba4d270.jpg" alt="DeepSWE Coding Agent Index Debut" width="760">

Artificial Analysis replaced SWE-Bench Pro with Datacurve's DeepSWE in its Coding Agent Index. The post says DeepSWE writes tasks from scratch instead of adapting public GitHub issues or pull requests, reducing benchmark contamination. In the refreshed ranking, Claude Code with Fable 5 Max debuts at 77, ahead of Codex with GPT-5.5 xhigh at 76 and Claude Code with Opus 4.8 Max at 73.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [DataEmpire Web Analytics Game](https://x.com/marclou/status/2065029898243318093) (by [@marclou](https://x.com/marclou))

**Turn raw site analytics into a replayable game by asking Claude Fable 5 to map visitors and milestones onto game entities.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2850773b9869c5521200f2e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6d2dd87d74ece01b277e1e12.jpg" alt="DataEmpire Web Analytics Game" width="760"><br>▶ Watch video</a>

Marc Lou says Claude Fable 5 built DataEmpire on top of his DataFast web analytics API. Each visitor becomes a villager, traffic growth expands the settlement, and the Age of Legends unlocks at 1 million visitors. The public demo lets DataFast users replay their own site history through the game layer, making this a concrete API-backed productization example rather than a static game clip.

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [FrontierSWE 20-Hour Task Signal](https://x.com/ProximalHQ/status/2065184730279223410) (by [@ProximalHQ](https://x.com/ProximalHQ))

**Use FrontierSWE as evidence that Claude Fable 5 can stay productive across very long engineering tasks, not just short bug-fix loops.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/eb36bb1120ef55f9e38c516d.jpg" alt="FrontierSWE 20-Hour Task Signal" width="760">

ProximalHQ reports Claude Fable 5 ranking #1 on FrontierSWE and calls it the biggest capability jump they have seen since releasing the benchmark. Their note says Fable 5 can work productively for close to 20 hours on many tasks and fully saturates tasks that were effectively out of reach for earlier models.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [KernelBench-Hard CUDA Records](https://x.com/elliotarledge/status/2065109393142849932) (by [@elliotarledge](https://x.com/elliotarledge))

**Use Claude Fable 5 for advanced CUDA kernel generation when you need low-level optimization, not just wrappers around existing libraries.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6c6931ed511eb3e539d56bc3.jpg" alt="KernelBench-Hard CUDA Records" width="760">

Elliot Arledge ran 13 frontier coding agents for 45 minutes each on KernelBench-Hard, roofline-graded on an RTX PRO 6000. Claude Fable 5 set all-time records on top-k, sonic-MoE, and W4A16 int4 GEMM, topped 5 of 6 problems, and the author published the runs, leaderboard, and code. The same thread also notes an FP8 GEMM miss where Fable 5 attempted a real tensor-core kernel but scored zero on a tail-alignment edge case.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Figma Capture Landing Page Clone](https://x.com/mikefutia/status/2065537778516205856) (by [@mikefutia](https://x.com/mikefutia))

**Capture a live competitor page into Figma layers and let Claude Code with Claude Fable 5 rebuild the structure, copy, and brand system instead of guessing from screenshots.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5672cc8fd9d210042551f0ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/503c46a33c97f0db334ddc62.jpg" alt="Figma Capture Landing Page Clone" width="760"><br>▶ Watch video</a>

Mike Futia describes a workflow where Figma's Chrome extension copies a website into editable layers, Claude Code reads those layers through the Figma MCP, rewrites the page in the user's brand voice, and GPT Image 2 generates the on-brand photography. The claimed end-to-end result is a shippable landing page in about 15 minutes with roughly $2 in image-generation API costs for 16 images.

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [GTA 2 Clone in Two Hours](https://x.com/techhalla/status/2064682080445898957) (by [@techhalla](https://x.com/techhalla))

**Combine Claude Fable 5 code generation with separate asset tooling to build a playable 3D game quickly without hand-coding the whole stack.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e0a1b46659d7a8287cb2f9d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd1a2ad71e71db936bdcfd22.jpg" alt="GTA 2 Clone in Two Hours" width="760"><br>▶ Watch video</a>

TechHalla says Claude Fable 5 High built a GTA 2-style clone in about two hours while the creator generated custom 3D models in Tripo. The post points to a tutorial thread with prompts, making it a compact example of multi-tool game production instead of a pure benchmark teaser.

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [CloudWatch Log Triage Agent](https://x.com/diblacksmith/status/2066230084273344698) (by [@diblacksmith](https://x.com/diblacksmith))

**Let a Claude Fable 5-powered agent chew through very large service-log contexts, infer architecture, and then narrow in on specific faults.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7f0f46eb79e43d87a2006fd4.jpg" alt="CloudWatch Log Triage Agent" width="760">

diblacksmith reports an RLM agent processing roughly 80,000 lines of CloudWatch logs in one run, reaching 53 steps while spending only about 32k active tokens so far. He says the agent inferred system architecture from the logs and flagged issues the team had missed, including AgentCore throttles and Slack `user_not_found` failures.

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [World Cup Predictor in Sandboxes](https://x.com/upstash/status/2064702195333820846) (by [@upstash](https://x.com/upstash))

**Put multiple frontier models behind isolated sandboxes and let them research live news, injuries, and yellow-card context for a public prediction app.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a5cf4fe5944c7aa2f703f4cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5b1f1422fe322bb7b66bdcc6.jpg" alt="World Cup Predictor in Sandboxes" width="760"><br>▶ Watch video</a>

Upstash says it built a World Cup predictor with Claude Fable 5, GPT-5.5, and Gemini, running inside isolated Upstash sandboxes. The demo and open-source release position Fable 5 as one model inside a multi-model research and orchestration stack rather than a standalone chat demo.

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [WolfBench Refusal Cost Case](https://x.com/WolfBenchAI/status/2065582716054376921) (by [@WolfBenchAI](https://x.com/WolfBenchAI))

**Treat refusal behavior as a real benchmark variable when pricing long autonomous runs on Claude Fable 5.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/453639cc17719af4e94655e0.jpg" alt="WolfBench Refusal Cost Case" width="760">

WolfBenchAI says its Claude Fable 5 evaluation cost $11,081.12, the most expensive benchmark run in that suite so far, and still did not top the charts because repeated refusals reduced useful task completion. This is a concrete limit case for teams budgeting agent evaluations or other high-autonomy workloads.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [API Access Cutoff Tracker](https://x.com/simonw/status/2065618703480414666) (by [@simonw](https://x.com/simonw))

**Monitor availability with a script if your workflow depends on continued access to a frontier model that may be rate-limited or withdrawn without much notice.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7400c158cb93d9480a22bb46.jpg" alt="API Access Cutoff Tracker" width="760">

Simon Willison says he pinged the `claude-fable-5` API every minute to see how long access would last and reported the exact point where it stopped responding for him. The post is thin on application detail, but it is concrete evidence that access continuity itself became an operational limitation users had to measure rather than assume.

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5 Community Demos



<a id="case-89"></a>
### Case 89: [Code-Generated Fox Animation with Sound](https://x.com/chetaslua/status/2117224839010459987) (by [@chetaslua](https://x.com/chetaslua))

**Use a shot-by-shot brief to specify a self-contained HTML animation and its sound design.**

The creator reports a 66-second fox-and-paper-birds short, with Python-generated frames and audio, delivered as one HTML file after about 2 hours 40 minutes. The accompanying prompt specifies shots, original artwork, sound and frame inspection. The post pairs the film with a detailed creative brief and screenshots of the production discussion.

[Creator’s complete prompt](https://x.com/chetaslua/status/2117224843661980093)

[![Code-Generated Fox Animation with Sound](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![Code-Generated Fox Animation with Sound](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![Code-Generated Fox Animation with Sound](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [Animation from an Open Creative Brief](https://x.com/notjazii/status/2117221957104239010) (by [@notjazii](https://x.com/notjazii))

**Compare what a coding model builds from an open animation brief with what a detailed storyboard produces.**

The author shares an animation and reports about one hour of work from a broad creative request, using code without external assets. The post presents the result as a broad creative-coding exercise.

[![Animation from an Open Creative Brief](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [Animated Construction Company Website](https://x.com/exploraX_/status/2117176904306335864) (by [@exploraX_](https://x.com/exploraX_))

**Use a construction-company website brief to evaluate animated 3D presentation and page composition.**

The creator shares an animated 3D website built around a construction-company brief and attaches a recording of the result.

[![Animated Construction Company Website](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Three.js Car Presentation](https://x.com/chetaslua/status/2116975056014430419) (by [@chetaslua](https://x.com/chetaslua))

**Inspect a car scene as a compact test of 3D composition, materials and camera presentation.**

The creator shares a Three.js car presentation. The recording provides a compact reference for evaluating the scene and its visual presentation.

[![Three.js Car Presentation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Minecraft-Style Browser Game Demo](https://x.com/notjazii/status/2116919129974411584) (by [@notjazii](https://x.com/notjazii))

**Pair a game recording with the creator's play link when assessing a generated browser game.**

The author shares a Minecraft-style game recording and a play link, describing the build as a one-shot task taking roughly one or two hours. The post pairs the recorded result with a play link for readers to explore.

[![Minecraft-Style Browser Game Demo](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Three.js Pelican Cycling Animation](https://x.com/chetaslua/status/2116882694026269148) (by [@chetaslua](https://x.com/chetaslua))

**Inspect a cycling scene for coordinated character motion, bicycle geometry and environmental detail.**

The creator shares a realistic Three.js animation of a pelican riding a bicycle and describes it as a one-shot result. The clip offers a reference for character motion, bicycle structure and the surrounding scene.

[![Three.js Pelican Cycling Animation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [Pelican Bicycle SVG with Exact Prompt](https://x.com/marmaduke091/status/2116233349391962392) (by [@marmaduke091](https://x.com/marmaduke091))

**Reuse the creator's short SVG prompt to compare geometry and detail under the same input.**

The author pairs a rendered pelican-on-a-bicycle image with the short SVG request reproduced verbatim below.

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![Pelican Bicycle SVG with Exact Prompt](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

[Animated version · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="Pelican Bicycle SVG with Exact Prompt" width="760"></a>

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [Galloping Zebra Animation Sample](https://x.com/AI_Screening/status/2115845754468356465) (by [@AI_Screening](https://x.com/AI_Screening))

**Use a galloping-animal clip to inspect gait consistency and motion continuity.**

The author shares their selected best output for a galloping-zebra task. The clip gives readers a concrete motion sample to inspect.

[![Galloping Zebra Animation Sample](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [TradingView Indicator with Human Execution](https://x.com/waveking1314/status/2114572023204806669) (by [@waveking1314](https://x.com/waveking1314))

**Keep order execution manual when evaluating an indicator that marks possible entries and adds commentary.**

The creator reports using Claude Fable 5.5 to write a TradingView indicator that marks possible entry points and adds a short comment while the user decides whether to place an order. The post includes a recording and says the indicator will be shared later.

[![TradingView Indicator with Human Execution](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---


<a id="case-98"></a>
### Case 98: [A dot becomes a short animated story](https://x.com/cherry_mx_reds/status/2105825930799432073) (by [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Use a minimal drawing request to explore how a model expands a visual story.**

The author reports asking for a dot and shares the resulting short animated story. The attached clip provides a concrete example of an open-ended visual request becoming a narrative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="A dot becomes a short animated story" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [Superman across changing art styles](https://x.com/chetaslua/status/2105757136219504862) (by [@chetaslua](https://x.com/chetaslua))

**Use one recognizable character to inspect continuity across changing animation styles.**

The creator shares a continuous Superman animation that transitions between different art styles. The post presents the changing visual treatment as the central creative result.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="Superman across changing art styles" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [Human progress in an animated film with music](https://x.com/imjustnewatai/status/2106081142143168580) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Brief a historical timeline and a future segment together when planning an animated explainer.**

The author reports using one prompt for a film about human progress followed by thirty years into the future. They share a roughly three-minute animation and report an original score without footage or stock music.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="Human progress in an animated film with music" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [Release-video comparison with Opus](https://x.com/mesmerlord/status/2105771088374288692) (by [@mesmerlord](https://x.com/mesmerlord))

**Compare complete release-video candidates generated from the same creative brief.**

The author shares two candidate release videos made from an Anthropic-video reference brief. The post explicitly discloses invented numbers and optional Codex image generation, so the clips are creative advertisements rather than factual benchmark evidence.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="Release-video comparison with Opus" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="Release-video comparison with Opus" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [Connecting lyrics and an event visually](https://x.com/chetaslua/status/2105934928483701214) (by [@chetaslua](https://x.com/chetaslua))

**Connect an existing song’s lyrics with a specific event to build a visual narrative.**

The creator reports asking for a visual connection between song lyrics and a Hugging Face incident. The attached animation shows the resulting combined narrative; the song and event are creative inputs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="Connecting lyrics and an event visually" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [Voxel character in a floating scene](https://x.com/blueemi99/status/2105804692811137242) (by [@blueemi99](https://x.com/blueemi99))

**Inspect a voxel character together with its surrounding scenery and animated details.**

The author shares a voxel self-character in a floating scene, highlighting the amount of detail and motion. The clip supplies a concrete voxel-design example for comparison with other runs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="Voxel character in a floating scene" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [A 3D Rube Goldberg machine demo](https://x.com/imjustnewatai/status/2105889407056109991) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Specify a chain-reaction scene first, then request a fixed-length demonstration video.**

The author supplies a short prompt requesting a complicated 3D Rube Goldberg machine, then asks for a one-minute video. The attached clip demonstrates the resulting chain-reaction visualization.

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="A 3D Rube Goldberg machine demo" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [A 3D controller interface with sound and motion](https://x.com/notjazii/status/2106050222828998967) (by [@notjazii](https://x.com/notjazii))

**Evaluate a controller interface through the combination of visual motion, sound and button behavior.**

The creator shares a 3D controller interface and reports added sounds, animation and haptics. The recording provides a concrete interface demonstration with sound enabled.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="A 3D controller interface with sound and motion" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [Comic characters presented with JavaScript](https://x.com/chetaslua/status/2105792187200147541) (by [@chetaslua](https://x.com/chetaslua))

**Use a character showcase to explore how code can supply fine visual details.**

The author reports a one-shot JavaScript showcase of Marvel and DC characters, saying the model chose subtle character details and edited the video. The post includes the resulting character presentation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="Comic characters presented with JavaScript" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [Updraft: worlds, bosses, and a leaderboard](https://x.com/EMostaque/status/2106065029850091943) (by [@EMostaque](https://x.com/EMostaque))

**Pair a game recording with a play link and an explicit feature list.**

The author shares Updraft, reporting a few hours of work with minimal prompts on high effort. Their feature list includes twenty-one worlds, 3D variants, twenty-one bosses with different mechanics and a leaderboard.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="Updraft: worlds, bosses, and a leaderboard" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [Driving through a San Francisco map](https://x.com/mindblown_ai/status/2106089461969019357) (by [@mindblown_ai](https://x.com/mindblown_ai))

**Use a city-driving prototype to explore map navigation and game objectives.**

The source poster shares footage and a play link for a San Francisco driving game attributed to someone else, naming Three.js in the stack. Credit here identifies the source poster rather than claiming they created the game.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="Driving through a San Francisco map" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [Writing prompts for a Seedance action scene](https://x.com/Chengzilhy/status/2105850801663234374) (by [@Chengzilhy](https://x.com/Chengzilhy))

**Separate prompt writing from video generation when documenting a multi-tool action scene.**

The author shares an expanded fight sequence, attributing prompt writing to Fable and video generation to Seedance 2.5. The workflow uses the language model to develop the video-generation input.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="Writing prompts for a Seedance action scene" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [An explainer video for a desktop coworker](https://x.com/ishuagra02/status/2106138602073641241) (by [@ishuagra02](https://x.com/ishuagra02))

**Use a short introduction video to explain a coding-tool extension.**

The creator demonstrates the clawdhouse Claude Code mod and attributes its introduction video to Fable. The mascot coworker and its moods are features of the mod being introduced, not a claim that Fable developed the mod.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="An explainer video for a desktop coworker" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [A short prompt for a changing-style animation](https://x.com/cherry_mx_reds/status/2105816670896009224) (by [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Test a brief animation request before adding a detailed creative specification.**

The author reports asking for a cool animation and receiving the shown changing-style result about fifteen minutes later. The original short request is quoted directly in the source post.

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="A short prompt for a changing-style animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [Visualizing the three-body problem](https://x.com/zAdrielsan/status/2105822678519001360) (by [@zAdrielsan](https://x.com/zAdrielsan))

**Separate CPU-side simulation from GPU-side rendering in an orbital visualization brief.**

The author reports roughly one thousand lines of Bend2 for a three-body scene, with symplectic physics on the CPU and pixel rendering on the GPU. They also report sixty FPS on their M5 and formal proofs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="Visualizing the three-body problem" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [An animation gallery of multiple art styles](https://x.com/blueemi99/status/2105782154387189771) (by [@blueemi99](https://x.com/blueemi99))

**Compare several art styles within one animation gallery.**

The author shares an animation gallery built using an xhigh setting. The concrete output presents multiple art styles together, making it useful for comparing visual treatments within a single work.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="An animation gallery of multiple art styles" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [Robot companions and procedural fur](https://x.com/KanaWorks_AI/status/2106717014245183517) (by [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**Combine existing character animation with procedural refinement instead of treating every asset as newly generated.**

The author refines an existing Unimate robot-dog animation into a companion and builds a furry virtual pet with grooming and trails. Unreal Engine and the existing robot animation remain explicit parts of the workflow.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="Robot companions and procedural fur" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [A mathematics motion edit](https://x.com/TurboNexic/status/2106710792590835934) (by [@TurboNexic](https://x.com/TurboNexic))

**Use mathematics-themed motion graphics as a visual communication example.**

The source poster shares a mathematics-themed motion edit. The attached vertical clip presents mathematical imagery as animated design; the post supplies the demonstration rather than a worked mathematical calculation.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="A mathematics motion edit" width="760">

*Archived frame from the source video.*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Your Woman lyric video](https://x.com/atomtanstudio/status/2106702854639743467) (by [@atomtanstudio](https://x.com/atomtanstudio))

**Build lyric motion around a supplied recording while keeping the music’s role explicit.**

The creator shares a lyric video for White Town’s Your Woman. The existing song is the audio input for the visual treatment, rather than music claimed to have been composed by the model.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Your Woman lyric video" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [Redrawing a music video in JavaScript](https://x.com/abhinavflac/status/2106638839666373114) (by [@abhinavflac](https://x.com/abhinavflac))

**Trace supplied source-video frames into code-based shapes when recreating a music-video treatment.**

The author describes tracing frames from Eminem’s Godzilla video into flat shapes and redrawing them with JavaScript. The original footage and music are inputs to the resulting animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="Redrawing a music video in JavaScript" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [A Chinese football animation](https://x.com/esrhengwu/status/2106625966965760380) (by [@esrhengwu](https://x.com/esrhengwu))

**Turn a sports theme into an animated narrative brief.**

The author shares an animation about China’s national football team, describing its development and resilience as the creative theme. The recording gives readers a concrete sports-storytelling example.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="A Chinese football animation" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [A handheld retopology showcase](https://x.com/mickeysmith_jp/status/2106607349385630138) (by [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**Compare a handheld-console render with its wireframe presentation when discussing topology.**

The source poster pairs a handheld-console image with a wireframe-style view while discussing retopology. The illustrated comparison provides a concrete modeling presentation rather than an editable mesh or a documented retopology procedure.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="A handheld retopology showcase" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft meets Pokémon](https://x.com/MozeTech/status/2106590326634983710) (by [@MozeTech](https://x.com/MozeTech))

**Combine mechanics from two familiar games into one prototype brief.**

The author presents a Pallet Town prototype mixing Minecraft-style building and crafting with Pokémon-style catching, and links a demo. The post describes the build as a one-shot experiment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft meets Pokémon" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [Explaining how an LLM is made](https://x.com/imjustnewatai/status/2106546810793730419) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Turn a technical question into a visual explainer request.**

The author asks how a large language model is made and shares the resulting explainer video. The work is a concrete example of presenting a technical topic through an animated sequence.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="Explaining how an LLM is made" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [An Altman highlight edit](https://x.com/benchmark_lb900/status/2106539977404506303) (by [@benchmark_lb900](https://x.com/benchmark_lb900))

**Use a public-figure theme to test the pacing of a short motion edit.**

The author shares an Altman-themed highlight video and describes it as a one-shot result. The vertical recording provides a compact motion-editing example.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="An Altman highlight edit" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [The first of the Thirty-Six Stratagems](https://x.com/jesselaunz/status/2106538284197548122) (by [@jesselaunz](https://x.com/jesselaunz))

**Document external music tools alongside a narrative-animation workflow.**

The author shares a film about the first of the Thirty-Six Stratagems and reports a single instruction. Suno V6 is named for the film’s music, preserving the separate role of the audio tool.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="The first of the Thirty-Six Stratagems" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [Game modeling, rigging, and animation](https://x.com/atomtanstudio/status/2106516974662713477) (by [@atomtanstudio](https://x.com/atomtanstudio))

**Evaluate character creation, rigging and animation together in a game-scene comparison.**

The author shares a Depths of Despair comparison featuring character modeling, rigging and animation. Their post describes the assets and tools used for the work and presents the visible results together.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="Game modeling, rigging, and animation" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [A wordless film about child mortality](https://x.com/cocoloba_/status/2106512963414970458) (by [@cocoloba_](https://x.com/cocoloba_))

**Use a wordless visual sequence to communicate a difficult social theme.**

The author shares a film about child mortality, using a breathing infant and darkened cots as narrative imagery. The case preserves the visual-storytelling task rather than adopting the film’s population statistics.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="A wordless film about child mortality" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [Glycolysis-to-ethanol SVG animation](https://x.com/olddonkeyblog/status/2106508425211330750) (by [@olddonkeyblog](https://x.com/olddonkeyblog))

**Embed animated SVG in HTML to explain a molecular process.**

The author requests a glucose molecule moving through glycolysis and ethanol formation, presented as animated SVG inside HTML. The attached recording shows the resulting scientific-visualization treatment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="Glycolysis-to-ethanol SVG animation" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [Sixteen simultaneous Starship launches](https://x.com/olddonkeyblog/status/2106507742454403485) (by [@olddonkeyblog](https://x.com/olddonkeyblog))

**Specify synchronized launch stages when briefing an HTML-and-SVG animation.**

The author requests sixteen Starships launching together, followed by stage separation and space entry. The recording presents the resulting multi-object animation sequence.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="Sixteen simultaneous Starship launches" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [An animated pelican bicycle test](https://x.com/olddonkeyblog/status/2106507429265756165) (by [@olddonkeyblog](https://x.com/olddonkeyblog))

**Inspect an animated pelican cycling scene as a coordinated-motion drawing task.**

The author shares their Max-reasoning run of the pelican-on-a-bicycle task. This is a distinct recorded output from other authors’ versions of the same general prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="An animated pelican bicycle test" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [A story of the next 150 years](https://x.com/imjustnewatai/status/2106489784382197771) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Combine a script, coded visuals and a score around a speculative future-story brief.**

The author reports a single instruction producing a film about humanity’s next one hundred and fifty years. The work combines a written narrative, coded animation and music to depict possible future life.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="A story of the next 150 years" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [An independent Humanity Walks experiment](https://x.com/iowitz/status/2106489119186538583) (by [@iowitz](https://x.com/iowitz))

**Re-run an art-history animation idea as an independent creative experiment.**

After seeing other demonstrations, the author tries their own walking-through-art-history animation and shares the result. The clip is retained as a separate generation rather than merged simply because the theme is similar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="An independent Humanity Walks experiment" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [The Grader coded film](https://x.com/argofowl/status/2106476549046513947) (by [@argofowl](https://x.com/argofowl))

**Document external speech or audio generation when presenting a code-generated film.**

The author shares The Grader as a coded film and names ElevenLabs v4 for audio. The post reports a one-shot run lasting about two hours and twenty-two minutes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="The Grader coded film" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [Reawakening horror short](https://x.com/JaydenDavisNC/status/2106440774367822008) (by [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**Use a named horror premise to shape a short animated film.**

The author shares Reawakening, a horror-themed AI short. The attached work offers a concrete narrative and atmosphere example for a horror-animation brief.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="Reawakening horror short" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [A 25-second self-improvement video](https://x.com/DAssetBuzz/status/2106505100575592838) (by [@DAssetBuzz](https://x.com/DAssetBuzz))

**Turn an abstract self-improvement theme into a short creative film brief.**

The author asks for a twenty-five-second video about what would make the model better and shares the result. The premise functions as creative storytelling rather than a product-capability statement.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="A 25-second self-improvement video" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [A castle scene and usage-cost feedback](https://x.com/nemumusitocha/status/2106429338556207284) (by [@nemumusitocha](https://x.com/nemumusitocha))

**Consider output detail and the creator’s usage experience together when evaluating a 3D scene.**

The author shares a detailed castle scene, praises its visual construction and describes the usage cost as poor value. The case pairs a concrete scene with the author’s cost-satisfaction feedback.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="A castle scene and usage-cost feedback" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [A 40-second brand launch ad](https://x.com/0xashtonx/status/2106421702783914423) (by [@0xashtonx](https://x.com/0xashtonx))

**Use your own brand as the subject of a concise launch-ad brief.**

The creator requests a forty-second launch advertisement for their own brand and shares the resulting video. The task is a concrete example of generating branded promotional storytelling.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="A 40-second brand launch ad" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [A Rocketball remake](https://x.com/atomtanstudio/status/2106418747083022555) (by [@atomtanstudio](https://x.com/atomtanstudio))

**Use a familiar game remake to combine coded assets with interactive mechanics.**

The author shares Rocketball, a remake of the 1980s C-64 game, and reports that its assets are coded. Replacing a website version is described as a future plan.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="A Rocketball remake" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [A voxel pagoda comparison](https://x.com/dropout_layer/status/2106408147309252915) (by [@dropout_layer](https://x.com/dropout_layer))

**Compare two runs of the same scene together with their reported per-run costs.**

The author presents Astra and Fable outputs for a 3D voxel pagoda, reporting costs of $3.50 and $5.50 respectively. The comparison concerns these specific runs and their displayed scene results.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="A voxel pagoda comparison" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [An imagined Switch 3 presentation](https://x.com/mathisbuilds/status/2106407842240418097) (by [@mathisbuilds](https://x.com/mathisbuilds))

**Use an imagined product as a concept-presentation and demonstration task.**

The author asks for an imagined Nintendo Switch 3 and a demo, reporting roughly four hours of work. The recording presents a fictional next-console concept rather than a real product specification.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="An imagined Switch 3 presentation" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [Before-and-after landing pages](https://x.com/nemumusitocha/status/2106402952307200302) (by [@nemumusitocha](https://x.com/nemumusitocha))

**Re-run the same landing-page prompt to compare output changes over time.**

The author compares a newly generated landing page with an earlier page produced from the same prompt. The visible before-and-after designs provide a practical interface-comparison example.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="Before-and-after landing pages" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [An imagined AI’s inner perspective](https://x.com/blueemi99/status/2106397329653719115) (by [@blueemi99](https://x.com/blueemi99))

**Use an imagined inner perspective as a creative animation premise.**

The author asks for a film about how being an AI model might feel and shares a one-shot result. The premise is presented as imaginative visual expression.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="An imagined AI’s inner perspective" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Go lyric motion design](https://x.com/atomtanstudio/status/2106377491267137848) (by [@atomtanstudio](https://x.com/atomtanstudio))

**Animate supplied lyrics around an existing song recording.**

The creator shares a lyric video for The Chemical Brothers’ Go and reports using Max reasoning. The song recording remains the external audio input for the motion-design task.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Go lyric motion design" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [A second 15-second motion portfolio](https://x.com/Saccc_c/status/2106376222309761094) (by [@Saccc_c](https://x.com/Saccc_c))

**Use a freeform motion-design portfolio brief to explore a new visual direction.**

The author shares a new fifteen-second motion portfolio and supplies the creative prompt. Their account explicitly distinguishes this generation from an earlier portfolio work.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="A second 15-second motion portfolio" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [Guided agent implementation review](https://x.com/RobIW_dev/status/2106371025852108940) (by [@RobIW_dev](https://x.com/RobIW_dev))

**Review implementation plans for system fit before moving from ideation into execution.**

The author shares guidelines covering system fit, implementation planning and explanations, describing how they review completed work or decide what to implement next. The attached image preserves the concrete planning artifact.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="Guided agent implementation review" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [Claude mascot dance](https://x.com/ishuagra02/status/2106369929813594134) (by [@ishuagra02](https://x.com/ishuagra02))

**Use beat-driven mascot animation to test the relationship between movement and music.**

The creator shares a Claude mascot dance and describes the animation as hitting the beat. Reposts of the same native video are associated with this source instead of counted again.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="Claude mascot dance" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [Interactive Seven Wonders islands](https://x.com/notjazii/status/2106368606502334922) (by [@notjazii](https://x.com/notjazii))

**Use landmark buildings as destinations in an interactive island scene.**

The source poster shares a Seven Wonders scene arranged as 3D islands with landmark buildings. The recording provides a concrete example of using recognizable monuments to organize an interactive visual environment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="Interactive Seven Wonders islands" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [A Propellerheads music video](https://x.com/atomtanstudio/status/2106353569603736009) (by [@atomtanstudio](https://x.com/atomtanstudio))

**Use a supplied soundtrack as the anchor for extended motion graphics.**

The creator shares a music-video treatment for Propellerheads’ On Her Majesty’s Secret Service. The existing recording is the audio input for the animated visual sequence.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="A Propellerheads music video" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Steamboat Willie animation comparison](https://x.com/mathisbuilds/status/2106351978691305732) (by [@mathisbuilds](https://x.com/mathisbuilds))

**Compare two animated treatments of the same short scene with sound enabled.**

The author shares a Steamboat Willie comparison labeled Fable and Opus at xhigh effort and describes the outputs as one-shot runs. The clip presents the specific visual-and-audio comparison.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Steamboat Willie animation comparison" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [A Sanxingdui-themed film](https://x.com/hungryturbo/status/2106339115642019904) (by [@hungryturbo](https://x.com/hungryturbo))

**Use a cultural-history theme to organize an animated short.**

The author shares a Sanxingdui-themed film as a creative visual-storytelling work. The recording provides a concrete example of turning a historical-cultural topic into an animation brief.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="A Sanxingdui-themed film" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Bugatti Chiron before and after](https://x.com/alannnfx/status/2106323394350461031) (by [@alannnfx](https://x.com/alannnfx))

**Re-run an earlier car prompt to compare modeling and feature detail.**

The same author shows Bugatti Chiron results from an earlier run and a newly repeated prompt. The recorded before-and-after comparison focuses on richer modeling and scene features.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Bugatti Chiron before and after" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [GRAIN concept film](https://x.com/NFT_Chen/status/2106301427052360150) (by [@NFT_Chen](https://x.com/NFT_Chen))

**Build an abstract concept film around recurring visual motifs.**

The creator shares GRAIN, a concept short connecting a seed, grain, a tree and mountain imagery. The sequence uses recurring forms and transitions as its narrative structure.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="GRAIN concept film" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [Human in Transit art gallery](https://x.com/exploraX_/status/2106296439936614646) (by [@exploraX_](https://x.com/exploraX_))

**Use an interactive-style art gallery to present a historical visual journey.**

The source poster shares Human in Transit, a gallery moving from ancient to modern art styles. The recorded interface gives readers a concrete reference for organizing multiple visual periods in one presentation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="Human in Transit art gallery" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [A Silk Road visual short](https://x.com/hungryturbo/status/2106294812261695508) (by [@hungryturbo](https://x.com/hungryturbo))

**Translate a travel-and-history theme into a coherent visual short.**

The author shares a Silk Road-themed film. The attached work offers a concrete creative treatment of a historical journey through animated imagery.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="A Silk Road visual short" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [A four-transformations presentation](https://x.com/dpkostka/status/2106272731364794757) (by [@dpkostka](https://x.com/dpkostka))

**Use a transformation framework as the organizing structure for a presentation.**

The author shares slides describing four transformation paths. The attached presentation image shows how a conceptual framework can be arranged into a visual document.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="A four-transformations presentation" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [Comparing historical chat tone](https://x.com/kiyoshi_shin/status/2106268573186637883) (by [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**Compare older conversation logs with current responses when examining changes in tone.**

The author asks the current model to analyze earlier chat logs and its present style, then reports dissatisfaction with the tone change. The attached image records that conversation-comparison task.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="Comparing historical chat tone" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [A kakapo cuteness test](https://x.com/hanawo_neki/status/2106257409782288659) (by [@hanawo_neki](https://x.com/hanawo_neki))

**Use a specific character-preference task to compare generated animation styles.**

The author shares a kakapo animation and says they prefer Opus for this cuteness-focused comparison. The case preserves the negative aesthetic feedback alongside the actual animated output.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="A kakapo cuteness test" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [Spider-Man across ten comic eras](https://x.com/chetaslua/status/2106248621519978867) (by [@chetaslua](https://x.com/chetaslua))

**Keep one character recognizable while moving through several comic-book eras.**

The original poster shares Spider-Man moving through ten comic eras. Other posts reusing the same video are associated with this source rather than counted as additional works.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="Spider-Man across ten comic eras" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [An Illuminati-themed fictional horror video](https://x.com/badboyfoxy/status/2106241189976387799) (by [@badboyfoxy](https://x.com/badboyfoxy))

**Treat a conspiracy-themed horror brief as a fictional storytelling exercise.**

The author asks for a scary Illuminati-themed video and shares the resulting work. The subject supplies a fictional horror premise for the animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="An Illuminati-themed fictional horror video" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [A coded history-of-nuclear-science film](https://x.com/imjustnewatai/status/2106238699872956427) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Combine a custom coded renderer and a score for a science-history explainer.**

The author requests a three-minute 3D film about how nuclear science made the atomic bomb possible, then reports drawn frames, a custom renderer and synthesized music. The case concerns the audiovisual production workflow.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="A coded history-of-nuclear-science film" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [Universal High Income explainer](https://x.com/markbraincell/status/2106234118514323515) (by [@markbraincell](https://x.com/markbraincell))

**Use animated explanation to communicate an economic concept.**

The source poster shares an animation explaining Universal High Income. The recording provides a concrete concept-explainer example without turning the depicted economic argument into a measured outcome.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="Universal High Income explainer" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [An Altman–Amodei dispute explainer](https://x.com/imjustnewatai/status/2106204392588276065) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Use a dispute as the narrative structure for an animated explainer.**

The author requests an animated account of the Altman–Amodei dispute and shares the resulting video. The task demonstrates a topical-explainer format rather than an independently sourced historical account.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="An Altman–Amodei dispute explainer" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [A Claude mascot music video](https://x.com/synthshareai/status/2106195060140446028) (by [@synthshareai](https://x.com/synthshareai))

**Combine a mascot overlay with supplied footage for a character-centered music-video edit.**

The source poster shares a Claude mascot over a live-action music-video background and reports a twelve-hour run. The visible treatment combines a cartoon overlay with supplied footage.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="A Claude mascot music video" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [A continuous zoom from quarks to the universe](https://x.com/imjustnewatai/status/2106190594775097663) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Use a continuous zoom to connect scientific scales within one audiovisual story.**

The author reports coded visuals and synthesized music for a zoom from quarks to the universe. The recording illustrates continuous scale transitions and a coherent visual narrative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="A continuous zoom from quarks to the universe" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [Imagining the world in 2076](https://x.com/Layton_Gott/status/2106190496075035096) (by [@Layton_Gott](https://x.com/Layton_Gott))

**Ask for a future-world scene with a specific narrative duration.**

The author shares a short film imagining the world in 2076 after requesting a twenty-five-second video. Reuse of the same recording by other accounts is associated with this source.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="Imagining the world in 2076" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [Lower Manhattan building chronology](https://x.com/nroze22/status/2106183281293381661) (by [@nroze22](https://x.com/nroze22))

**Combine footprints, building dates and heights in an architectural timeline interface.**

The author presents Lower Manhattan through an architectural-drawing-style interface, showing building dates, footprints and heights. The recording provides a concrete interactive chronology concept.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="Lower Manhattan building chronology" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [An oracle-bone-script animation](https://x.com/MinLiBuilds/status/2106180691344118202) (by [@MinLiBuilds](https://x.com/MinLiBuilds))

**Use the evolution of writing as the subject of an animated historical journey.**

The author shares an animation beginning with oracle-bone script. The recording supplies a concrete visual-storytelling example built around the history of written characters.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="An oracle-bone-script animation" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [Another character-through-art-history animation](https://x.com/imjustnewatai/status/2106162924331180510) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Use familiar characters as continuous guides through a changing historical setting.**

The author requests Iron Man and Spider-Man flying through history and shares the resulting animation. It is a separate work from other authors’ character-through-art-history experiments.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="Another character-through-art-history animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [A coded Seikilos audiovisual work](https://x.com/YanqingCheng/status/2106158746938269728) (by [@YanqingCheng](https://x.com/YanqingCheng))

**Build a single-file audiovisual work around a historical musical text.**

The author shares a Seikilos-epitaph work, reporting visuals and music synthesized with HTML and JavaScript in one file. The historical text provides the organizing theme for the coded audiovisual sequence.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="A coded Seikilos audiovisual work" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [Jet Animation Comparison](https://x.com/Kinzf2121/status/2106158536963330346) (by [@Kinzf2121](https://x.com/Kinzf2121))

**Compare flight animation and camera tracking under the same aircraft task.**

The author shares a jet-animation comparison between a result labeled Fable 5.1 and Opus. The recorded scenes provide a specific example for comparing aircraft motion and cinematic camera tracking.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="Jet Animation Comparison" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [Model Self-Introduction Film](https://x.com/devteamdrew/status/2106155815707021549) (by [@devteamdrew](https://x.com/devteamdrew))

**Use a self-introduction brief to explore a model-themed animation.**

The creator reports asking for a self-introduction video in one prompt and shares the resulting film. The task combines a model-themed narrative with an animated presentation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="Model Self-Introduction Film" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [Post-Apocalyptic Card-Game Prototype](https://x.com/maciejkrupowies/status/2106153578029338850) (by [@maciejkrupowies](https://x.com/maciejkrupowies))

**Prototype a card-game theme and inspect the resulting combat interface.**

The author shares a post-apocalyptic Hearthstone-style prototype described as a one-shot build. The post acknowledges small glitches while showing the game interface and interactions.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="Post-Apocalyptic Card-Game Prototype" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [The Late Byte Workplace Animation](https://x.com/rohit3a/status/2106138910648914094) (by [@rohit3a](https://x.com/rohit3a))

**Turn model personas into characters for an animated workplace conversation.**

The creator presents The Late Byte, an animated workplace story with Opus portrayed as an angry boss. This is a distinct narrative from the separate Day in the Life of Claude film.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="The Late Byte Workplace Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Queens of the Stone Age Lyric Animation](https://x.com/atomtanstudio/status/2106135196483608745) (by [@atomtanstudio](https://x.com/atomtanstudio))

**Combine a supplied song with kinetic typography and motion design.**

The creator describes making a kinetic-typography music video around a Queens of the Stone Age recording. The song is a supplied audio input, while the example concerns arranging its lyrics and visuals.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Queens of the Stone Age Lyric Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [Shared Three.js Narrative Scene](https://x.com/Noreply134882/status/2106116572389478746) (by [@Noreply134882](https://x.com/Noreply134882))

**Use a shared 3D story clip as a reference for narrative scene design.**

The poster shares a Three.js narrative scene and comments on heavy token consumption. The attached clip is retained as a shared visual example of 3D storytelling.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="Shared Three.js Narrative Scene" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [Moonwalking through Historical Scenes](https://x.com/noclipepe/status/2106105810812112937) (by [@noclipepe](https://x.com/noclipepe))

**Carry a dance motif across different historical settings and visual styles.**

The poster shares a Michael Jackson moonwalking sequence that moves from dinosaurs to the Moon. The attached film is retained as a shared dance-and-style-gallery example.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="Moonwalking through Historical Scenes" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [Detailed-Prompt Motion Graphics](https://x.com/devswha/status/2106100273509007802) (by [@devswha](https://x.com/devswha))

**Compare a detailed creative brief with a shorter motion-design request.**

The author shares a motion-graphics video and reports supplying only a detailed prompt, without assets, reference video or source files. The result offers a concrete reference for prompt-driven motion design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="Detailed-Prompt Motion Graphics" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [Rental-Business Website Interface](https://x.com/oalanicolas/status/2106098902965309475) (by [@oalanicolas](https://x.com/oalanicolas))

**Use a rental-business brief to explore a concrete website interface.**

The creator shares a screenshot of a website interface for a rental business. The example concerns the visible page design and presentation of the business.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="Rental-Business Website Interface" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [AGI-Themed Creative Film](https://x.com/AndrewOnXYZ/status/2106097745098395712) (by [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**Use a recurring creative prompt to compare narrative and visual treatments.**

The author shares an AGI-themed animation produced from a recurring prompt. The film treats its model statements as part of a creative narrative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="AGI-Themed Creative Film" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [Art History with a Cat Subplot](https://x.com/cherry_mx_reds/status/2106095190285144331) (by [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Compress multiple art periods into a short narrative with a recurring character.**

The creator presents a fifteen-second tour through art history with a cat subplot. The stated fifteen seconds refer to the film length, while the creative task spans many historical styles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="Art History with a Cat Subplot" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [Combat Prototype and Voxel Scene](https://x.com/OnlyTerp/status/2106089280502210626) (by [@OnlyTerp](https://x.com/OnlyTerp))

**Inspect both game combat and world-building outputs from a creative-coding task.**

The author shares a DMC-style combat prototype together with a voxel scene and describes a long generation run. The post offers two concrete outputs for examining game mechanics and visual world design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="Combat Prototype and Voxel Scene" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [Internet Meme Chronology](https://x.com/chetaslua/status/2106076940558082297) (by [@chetaslua](https://x.com/chetaslua))

**Organize an animated chronology around year-specific visual styles and music.**

The creator shares an animated sequence of viral internet memes from 2010 through 2026. Each year receives a visual style and music treatment as part of the coded narrative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="Internet Meme Chronology" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [Particle Motion from One Line](https://x.com/devswha/status/2106072107365114186) (by [@devswha](https://x.com/devswha))

**Start with a one-line motion brief before refining a detailed prompt.**

The creator shares a particle-motion animation from a one-line prompt and says they plan to try a more detailed request. It is a separate generation from their longer motion-design example.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="Particle Motion from One Line" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [Kung-Fu Boy Animation](https://x.com/HashmathRzz/status/2106065773336965510) (by [@HashmathRzz](https://x.com/HashmathRzz))

**Use a martial-arts character brief to explore animated movement.**

The author shares Kung-Fu Boy, a character-animation example attributed to Fable 5.5. The attached recording supplies the concrete animated result for the martial-arts theme.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="Kung-Fu Boy Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [Strait of Hormuz Debate Animation](https://x.com/chetaslua/status/2106060047805792415) (by [@chetaslua](https://x.com/chetaslua))

**Convert a debate topic into an animated narrative.**

The creator presents an animated debate about the Strait of Hormuz. This case records the visible debate film rather than the other unsupported uses mentioned in the surrounding post.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="Strait of Hormuz Debate Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [Unicorn SVG Style Experiment](https://x.com/atomtanstudio/status/2106057876053918127) (by [@atomtanstudio](https://x.com/atomtanstudio))

**Use the same themed drawing task to inspect SVG style choices.**

The author shares a unicorn-themed SVG experiment inspired by another creator’s test. The attached image provides the concrete output for comparing visual treatment of the same subject.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="Unicorn SVG Style Experiment" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [Halloween Seasonal Animation](https://x.com/cherry_mx_reds/status/2106056643255447590) (by [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Give a coding model a seasonal theme for a short creative animation.**

The creator asks for a Halloween-themed work and shares the resulting seasonal animation. The post supplies the original recording for this specific creative task.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="Halloween Seasonal Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Blender CLI Barbarian and Cover](https://x.com/BoDy051/status/2106047375320166885) (by [@BoDy051](https://x.com/BoDy051))

**Use Blender CLI instructions to explore character modeling and cover rendering.**

The author compares an RPG barbarian character and cover concept with an Opus output. Blender CLI is the construction and rendering tool in the workflow; the model provides code instructions.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Blender CLI Barbarian and Cover" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Day in the Life of Claude](https://x.com/ishuagra02/status/2106045364868419727) (by [@ishuagra02](https://x.com/ishuagra02))

**Build an animated daily-life story around a recurring mascot.**

The original poster shares a Day in the Life of Claude film featuring the mascot. The source video is distinct from the separate mascot-dance animation and its reposts.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Day in the Life of Claude" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [Humanity History in 3D](https://x.com/blueemi99/status/2106041578204655748) (by [@blueemi99](https://x.com/blueemi99))

**Combine coded scenes and animation into a historical visual sequence.**

The creator shares a 3D video moving from ancient humanity to the present and reports generating its animations and models in code. The result is a visual storytelling example.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="Humanity History in 3D" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [Fast Motion-Designer Reel](https://x.com/blueemi99/status/2106031355922387163) (by [@blueemi99](https://x.com/blueemi99))

**Evaluate pacing, sound and coherence in a short motion-design reel.**

The author shares a short, fast-paced motion video and compares its sound and coherence with their Opus output. The judgment describes the creator’s experience with this particular work.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="Fast Motion-Designer Reel" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [Freeform Complex 3D Creation](https://x.com/cocoloba_/status/2106029181607772413) (by [@cocoloba_](https://x.com/cocoloba_))

**Use an open-ended creative request to explore a complex 3D composition.**

The creator asks what the model would make with spare time and shares the resulting 3D work. The post describes many separate parts as part of the generated composition.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="Freeform Complex 3D Creation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [Stick-Figure Fight Animation](https://x.com/HelaliBillel/status/2106028502763900944) (by [@HelaliBillel](https://x.com/HelaliBillel))

**Use a specific combat-animation request to inspect timing and movement.**

The creator requests a video of an animated stick-figure fight scene and shares the result. The attached recording supplies a concrete example of the combat-animation task.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="Stick-Figure Fight Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [One-Prompt UI Motion Sequence](https://x.com/iancarscadden/status/2106018048792789360) (by [@iancarscadden](https://x.com/iancarscadden))

**Explore a UI sequence with a single animation brief.**

The author shares a UI-motion sequence described as a one-shot result completed in roughly six or seven minutes. The recording shows the visual sequence produced for that request.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="One-Prompt UI Motion Sequence" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [SCP-8517 Fictional Animation](https://x.com/eviljoker88/status/2106003621402005816) (by [@eviljoker88](https://x.com/eviljoker88))

**Use an SCP-inspired premise as a brief for an animated story.**

The creator presents an SCP-8517-themed animated work and attributes its creation to Fable 5.5. The case concerns the fictional narrative and its visible animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="SCP-8517 Fictional Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [Watercolor Autumn Animation](https://x.com/ishuagra02/status/2106000055706784118) (by [@ishuagra02](https://x.com/ishuagra02))

**Specify a seasonal subject and watercolor treatment for an animation.**

The author shares an autumn-themed animation in watercolor style. The recorded work offers a concrete example of pairing a seasonal subject with a particular visual medium.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="Watercolor Autumn Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [Procedural Doll Stage](https://x.com/HelaliBillel/status/2105988689088196785) (by [@HelaliBillel](https://x.com/HelaliBillel))

**Inspect how a doll-like character is animated within a staged scene.**

The author shares a procedural doll-stage animation and mentions Blender in the accompanying discussion. The case concerns the visible staged character and animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="Procedural Doll Stage" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [Browser-Rendered Pelican Ride](https://x.com/slimcat0101/status/2105988654636380444) (by [@slimcat0101](https://x.com/slimcat0101))

**Run a character-motion result in a browser and inspect the rendered scene.**

The creator asks for a pelican riding a bicycle and records the resulting HTML running in a browser. This is a moving browser scene, distinct from the static SVG drawing tests.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="Browser-Rendered Pelican Ride" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [The Universe Looks at Itself](https://x.com/l_mejiaC/status/2105988529671360673) (by [@l_mejiaC](https://x.com/l_mejiaC))

**Use a continuous visual journey to connect distant scales in one narrative.**

The creator presents a continuous sequence from the Big Bang to a human eye. The author describes the visuals and music as produced through runtime code for the film.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="The Universe Looks at Itself" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [Independent Jet Animation Test](https://x.com/AI_Screening/status/2105988448612135176) (by [@AI_Screening](https://x.com/AI_Screening))

**Repeat an aircraft-animation task and inspect the specific output.**

After seeing routing discussions, the author tries a jet-animation task and shares their result. The recording provides an independent source for this aircraft example.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="Independent Jet Animation Test" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [Initial Freeform Motion Reel](https://x.com/Saccc_c/status/2105985484472377531) (by [@Saccc_c](https://x.com/Saccc_c))

**Explore motion design with a brief open-ended prompt.**

The creator shares an initial motion-design reel described as generated from one prompt. It is a distinct earlier output from their later fifteen-second portfolio work.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="Initial Freeform Motion Reel" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [Civilization Rendered in Code](https://x.com/ziwenxu_/status/2105983571848741045) (by [@ziwenxu_](https://x.com/ziwenxu_))

**Turn a civilization-history brief into a coded animated narrative.**

The author asks for civilization from its beginning to the present and shares the resulting film. The creator reports using no footage or stock assets in this coded visual treatment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="Civilization Rendered in Code" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [Chip-to-Server Zoom Comparison](https://x.com/SPAC89/status/2105968361725202591) (by [@SPAC89](https://x.com/SPAC89))

**Compare realism and continuity in a chip-to-server zoom task.**

The author compares Fable XHigh and GPT Sol Ultra on a realistic zoom sequence and discusses speed and quota use. The post compares specific runs on different subscription tiers.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="Chip-to-Server Zoom Comparison" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [Lunar-Travel Animation Project](https://x.com/IgorGomezC/status/2105963552024506565) (by [@IgorGomezC](https://x.com/IgorGomezC))

**Explore a personal animation concept with more than one coding model.**

The creator shares a personal lunar-travel animation project while discussing experiments with Fable and Opus. The attached work is the concrete output of that creative exploration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="Lunar-Travel Animation Project" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [Japanese Voxel Scene Comparison](https://x.com/vikktorrrre/status/2105955048018588084) (by [@vikktorrrre](https://x.com/vikktorrrre))

**Compare detail, fog and visual clarity using the same scene prompt.**

The author compares current Fable and Opus outputs on the same Japanese voxel-scene prompt. The accompanying observations concern the clarity, fog and aesthetic treatment of those particular results.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="Japanese Voxel Scene Comparison" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [Steaming the Frontier Audiovisual Short](https://x.com/sdmat123/status/2105929299878703520) (by [@sdmat123](https://x.com/sdmat123))

**Combine a Steamboat-style visual brief with sound for an audiovisual short.**

The creator shares Steaming the Frontier, an animated work with sound. It remains a separate source from other creators’ independent Steamboat-style outputs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="Steaming the Frontier Audiovisual Short" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [Superman across Multiple Art Styles](https://x.com/Mr_Salio/status/2105925979466052051) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Carry one character through changing art styles in a continuous animation.**

The creator says an earlier Superman example inspired a new generation and shares their own result. Its different artwork makes it a distinct creation rather than a repost.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="Superman across Multiple Art Styles" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Cupcake-Style Boss-Fight Prototype](https://x.com/maciejkrupowies/status/2105914965387321785) (by [@maciejkrupowies](https://x.com/maciejkrupowies))

**Prototype a side-scrolling boss fight and inspect the resulting combat.**

The author shares a Cupcake-style boss-fight prototype and reports one-shot generation in under ten minutes. The attached recording shows the game’s combat sequence.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Cupcake-Style Boss-Fight Prototype" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [Sailing Ship with Changing Sun](https://x.com/popat_kunj/status/2105907935490752822) (by [@popat_kunj](https://x.com/popat_kunj))

**Use a sailing scene to explore sky, water and changing solar position.**

The creator shares a 3D sailing-ship scene with the sun at different positions and links an interactive artifact. The scene combines a ship, sky and water in one visual task.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="Sailing Ship with Changing Sun" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Paracortex and Pi Changenotes Video](https://x.com/RobIW_dev/status/2105894547796476225) (by [@RobIW_dev](https://x.com/RobIW_dev))

**Turn product updates into a short motion-design announcement.**

The author converts updates to Paracortex and Pi into a twenty-five-second motion-design video and supplies a prompt with the post. The work is an example of visual product communication.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Paracortex and Pi Changenotes Video" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Curio 2.0 Website Promo](https://x.com/voltwake/status/2105884775982485642) (by [@voltwake](https://x.com/voltwake))

**Create a coded promotional film around an existing website launch.**

The creator describes making a launch promo for Curio 2.0, combining coded visuals, camera work and music. The post shares the resulting website promotional film.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Curio 2.0 Website Promo" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [Imagined Hugging Face 3D Story](https://x.com/chetaslua/status/2105884276864782557) (by [@chetaslua](https://x.com/chetaslua))

**Combine model-written code with rendering and audio tools for a fictional film.**

The creator shares an imagined Hugging Face story made with model-written code, Blender and the ElevenLabs API. Blender handles construction and rendering, while ElevenLabs supplies external audio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="Imagined Hugging Face 3D Story" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [Claude for Chrome in JS Paint](https://x.com/BtwIUseSystemd/status/2105861662112923849) (by [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**Give a browser agent a drawing task restricted to the application’s own tools.**

The author asks Claude for Chrome to draw a person using only JS Paint tools and shares the resulting image. Browser interaction and the painting application are explicit parts of the task.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="Claude for Chrome in JS Paint" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [Static Pelican Bicycle SVG](https://x.com/olddonkeyblog/status/2105842745189556672) (by [@olddonkeyblog](https://x.com/olddonkeyblog))

**Use a self-contained SVG request to test a detailed static drawing.**

The creator requests a single self-contained SVG of a pelican riding a bicycle and shares the static image. This is a separate drawing task from the animated ride examples.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="Static Pelican Bicycle SVG" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [BlockBench MCP with a Minecraft Skill](https://x.com/TOPSTR1X/status/2105839618872738138) (by [@TOPSTR1X](https://x.com/TOPSTR1X))

**Supply a modeling tool and style skill when generating a game character.**

The author provides BlockBench MCP and a custom Minecraft modeling and coloring skill, then shares the resulting character. These tools and style guidance are explicit inputs to the workflow.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="BlockBench MCP with a Minecraft Skill" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [Dig Dug in One HTML File](https://x.com/imjustnewatai/status/2105831117677084841) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Target a single HTML deliverable when recreating a compact browser game.**

The creator asks for a Dig Dug recreation in a single HTML file and shares the resulting game recording. The post describes the build as coming from one prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="Dig Dug in One HTML File" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [Mechanical Octopus SVG](https://x.com/SEO/status/2105812236774297943) (by [@SEO](https://x.com/SEO))

**Use a mechanical creature to inspect detail and movement in SVG design.**

The author shares an animated octopus SVG with mechanical details. The recording offers a concrete vector-design example centered on small moving parts.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="Mechanical Octopus SVG" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [Humanity Walks through Art Styles](https://x.com/l_mejiaC/status/2105801379956850793) (by [@l_mejiaC](https://x.com/l_mejiaC))

**Carry a recurring figure through a sequence of historical visual styles.**

The original creator presents a continuous walk through twenty art panels over roughly seventy-four seconds and reports coded music. Each boundary shifts the character and scene into a different style.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="Humanity Walks through Art Styles" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [Open-Ended Black-Hole Scene](https://x.com/rohit3a/status/2105786053412208835) (by [@rohit3a](https://x.com/rohit3a))

**Use an open-ended creative brief to explore a black-hole visualization.**

The creator asks what the model would make to impress them and shares a black-hole scene. The task is a freeform visual exploration rather than a prescribed interface build.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="Open-Ended Black-Hole Scene" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [Aurora Jellyfish Animation Comparison](https://x.com/SPAC89/status/2105783511433318451) (by [@SPAC89](https://x.com/SPAC89))

**Compare deformation and movement in two jellyfish-animation outputs.**

The author compares Fable XHigh and GPT Sol Ultra on an aurora-jellyfish animation and discusses quota usage. The results come from different subscription tiers.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="Aurora Jellyfish Animation Comparison" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Nintendo Switch Snap-and-Boot SVG](https://x.com/ishuagra02/status/2105779174921359470) (by [@ishuagra02](https://x.com/ishuagra02))

**Combine controller movement and a boot sequence in one SVG animation.**

The creator shares a Nintendo Switch SVG in which controllers snap into place before a boot-logo animation. The post reports a runtime of one minute thirty-nine seconds and a cost of $1.34 for that run.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Nintendo Switch Snap-and-Boot SVG" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [The Loom Interactive 3D Scene](https://x.com/Mr_Salio/status/2105774088492916757) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Explore a landscape and buildings as a single interactive 3D page.**

The author presents The Loom, an interactive scene with buildings and landscape. The attached recording supplies the concrete page output from the creator’s test.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="The Loom Interactive 3D Scene" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [Motion-Design Reels from the Same Prompt](https://x.com/mesmerlord/status/2105758042830549235) (by [@mesmerlord](https://x.com/mesmerlord))

**Compare visual focus and beat synchronization across two same-prompt motion-design reels.**

The author shares two early Fable 5.5 motion-design results from the same prompt and tentatively notes clearer focus and better beat synchronization than an Opus run. Both native source videos are preserved together.

```
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

[@shneural](https://x.com/shneural/status/2103151003272962130)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="Motion-Design Reels from the Same Prompt" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29b80ef5ba92b029630a1628.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0da5945bc240b424bfebbd9.jpg" alt="Motion-Design Reels from the Same Prompt" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [Cleaner Scenery with Less Depth](https://x.com/eviljoker88/status/2105755840175034447) (by [@eviljoker88](https://x.com/eviljoker88))

**Retain negative aesthetic feedback when comparing generated scene outputs.**

The author shares a side-by-side Japanese-scene comparison and prefers the depth in the Opus output despite a cleaner appearance in the other result.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="Cleaner Scenery with Less Depth" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [Mixed Japanese-Scene Results](https://x.com/eviljoker88/status/2105755408342126936) (by [@eviljoker88](https://x.com/eviljoker88))

**Record mixed feedback instead of treating a first comparison as a clear winner.**

The author shares an initial Japanese-scene comparison and describes the results as mixed. The attached image preserves the concrete outputs behind that aesthetic feedback.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="Mixed Japanese-Scene Results" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [Controller SVG Comparisons](https://x.com/notjazii/status/2105751542498464169) (by [@notjazii](https://x.com/notjazii))

**Compare before-and-after controller drawings under a similar visual task.**

The author shares before-and-after controller SVG outputs in a comparison image. The case concerns the visible changes in drawing and presentation rather than a general model ranking.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="Controller SVG Comparisons" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [Industrial-Device Scene](https://x.com/RayaneRachid_/status/2105744517735354410) (by [@RayaneRachid_](https://x.com/RayaneRachid_))

**Use a mechanical device as a focused 3D scene-design task.**

The creator shares a 3D industrial-device scene and calls it their best one-shot result. The attached image gives a concrete reference for the mechanical composition.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="Industrial-Device Scene" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [Giant Shelled Gill-Bug Reconstruction](https://x.com/Josh67Joshua/status/2105739832563769697) (by [@Josh67Joshua](https://x.com/Josh67Joshua))

**Use a specific creature description to explore a two-prompt reconstruction.**

The author shares a giant shelled gill-bug drawing and reports achieving the result in two prompts. The image provides the visible output of the creature-design task.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="Giant Shelled Gill-Bug Reconstruction" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [GameCube Controller in Two Prompts](https://x.com/marmaduke091/status/2105735266032095349) (by [@marmaduke091](https://x.com/marmaduke091))

**Use a familiar controller to inspect a two-prompt drawing result.**

The author shares a GameCube controller drawing and reports using two prompts. This static controller image is distinct from the Xbox and other controller demonstrations.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="GameCube Controller in Two Prompts" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [Screenshot Edited for an X Post](https://x.com/chetaslua/status/2105733677003292983) (by [@chetaslua](https://x.com/chetaslua))

**Inspect how an assistant adapts a screenshot for a social post.**

The creator shares a screenshot edit prepared for an X post and says the assistant performed the edit without an explicit request. The attached image is the visible result.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="Screenshot Edited for an X Post" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [Before-and-After Voxel Sakura](https://x.com/kdnbmb/status/2105704791049412755) (by [@kdnbmb](https://x.com/kdnbmb))

**Compare successive voxel-scene outputs on the same visual subject.**

The poster shares two versions of a voxel sakura island scene. The side-by-side image records the visible before-and-after design differences for the scene.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="Before-and-After Voxel Sakura" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [SHADERKIN Cloth-Interface Prototype](https://x.com/mszzz0011/status/2106025576972853642) (by [@mszzz0011](https://x.com/mszzz0011))

**Explore fabric effects alongside adjustable controls in an interface prototype.**

The author shares a SHADERKIN prototype with cloth effects and parameter controls and describes it as a one-shot build. The recording shows the resulting interface and motion.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="SHADERKIN Cloth-Interface Prototype" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [Shared Golden-Clock Interface Animation](https://x.com/AISuperDomain/status/2106396754539360272) (by [@AISuperDomain](https://x.com/AISuperDomain))

**Use a clock-themed animation as a reference for interface composition.**

The poster presents a golden-clock-themed frontend animation. The attached clip offers a shared reference for examining interface composition, the clock motif and its animated visual presentation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="Shared Golden-Clock Interface Animation" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [Before There Was Anything Narrative](https://x.com/crowqnt/status/2106146218846081435) (by [@crowqnt](https://x.com/crowqnt))

**Explore a cosmic and human narrative through a shared animated film.**

The poster shares Before There Was Anything, a narrative video about the cosmos and humanity. The attached film is retained as a shared visual storytelling example.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="Before There Was Anything Narrative" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [Shared Blue Particle Vortex](https://x.com/AISuperDomain/status/2105846981776003107) (by [@AISuperDomain](https://x.com/AISuperDomain))

**Inspect particle motion and composition in a shared vortex visualization.**

The poster shares a blue-particle vortex animation. The attached clip provides a concrete shared example for examining particle movement, visual structure and composition.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="Shared Blue Particle Vortex" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [Multi-Panel Interface after Two Revisions](https://x.com/ZorroOfMorocco/status/2106547078235095485) (by [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**Use revision cycles to refine a visual interface rather than stopping at the first output.**

The author shares a completed multi-panel interface and reports roughly three hours of work with two revisions. The attached screenshot shows the final visual design.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="Multi-Panel Interface after Two Revisions" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [Stacked Animals in a Rendered Scene](https://x.com/legit_api/status/2117237103289315574) (by [@legit_api](https://x.com/legit_api))

**Inspect how a static composition balances several characters and different materials.**

The post shares a stacked bear, panda and polar-bear scene, credits yuruzuu on Discord, and reports a 21-minute run. The public post is retained as the shared visual source.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="Stacked Animals in a Rendered Scene" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [Four Open-World RPG Attempts Compared](https://x.com/noclipepe/status/2117222592536789149) (by [@noclipepe](https://x.com/noclipepe))

**Compare game presentation, combat and collision behavior across the same creative task.**

The creator presents four one-prompt RPG attempts labelled Fable 5.5, GPT-6.2 Astra, Opus 5.5 and Fable 5.1. Commentary contrasts lighting, combat, inventory, collisions and a character becoming stuck.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="Four Open-World RPG Attempts Compared" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [Two Front-End Animation Clips Compared](https://x.com/leo114119/status/2117209849842761983) (by [@leo114119](https://x.com/leo114119))

**Compare scene design and visual detail by viewing the animation clips together.**

The post juxtaposes code-generated animations with Astra and Fable labels, focusing on detail and script design. It explicitly credits @chetaslua for the Fable animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="Two Front-End Animation Clips Compared" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [A Moss-Robot Film Generated in Code](https://x.com/chetaslua/status/2117169796290916732) (by [@chetaslua](https://x.com/chetaslua))

**Use an animation brief to explore a complete cinematic scene built through code.**

The creator shares a forest-and-robot animation and describes it as a one-shot coded film. The post points readers to the prompt shown in a screenshot and compares the result with other attempts.

An additional post shows a separately reported Opus 5.5 control run. [@AnikaCodes](https://x.com/AnikaCodes) · [Related work](https://x.com/AnikaCodes/status/2117222374642946297)

A related GPT-6 Astra Max run uses generated images in the workflow, according to its author. This keeps the different production methods visible alongside the original film. [@rubenssoto_ai](https://x.com/rubenssoto_ai) · [Related comparison](https://x.com/rubenssoto_ai/status/2117707344704352691)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="A Moss-Robot Film Generated in Code" width="760"></a></td><td valign="top"><p>An additional post shows a separately reported Opus 5.5 control run.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="A Moss-Robot Film Generated in Code" width="760"></a></td><td valign="top"><p>GPT-6 Astra Max</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/25b0cfcdb1fdda22ba6aa9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/75f37c74099d5b9ba1ad0ddc.jpg" alt="GPT-6 Astra Max" width="760"></a></td></tr></table>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [A Container-Port Simulation Revisited](https://x.com/anxuanng/status/2117124831279972812) (by [@anxuanng](https://x.com/anxuanng))

**Revisit an earlier scene while preserving the project context for visual comparison.**

The author posts another container-port scene and quotes their earlier Blender and Three.js simulation, whose cranes, ships, vehicles and containers were modeled for a strategy-like environment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="A Container-Port Simulation Revisited" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [An Airport-Ramp Scene Revisited](https://x.com/anxuanng/status/2117096574878921119) (by [@anxuanng](https://x.com/anxuanng))

**Compare a revised airport scene with the earlier project and its asset workflow.**

The author returns to an airport-ramp scene, quoting their earlier Blender and Three.js simulation and sharing new footage of planes, service vehicles and terminal infrastructure.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="An Airport-Ramp Scene Revisited" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [Pelican Cycling Through Abstract 3D Worlds](https://x.com/xiax0603/status/2116960224829665543) (by [@xiax0603](https://x.com/xiax0603))

**Use a cycling subject to inspect transitions through different spatial environments.**

The post shares a pelican-and-bicycle animation that passes through geometric fragments and an abstract digital environment before zooming out through an eye. The sequence supplies a distinct scene-transition demonstration.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="Pelican Cycling Through Abstract 3D Worlds" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [Historical Sailing-Ship Scene](https://x.com/abhinavflac/status/2116945827738665060) (by [@abhinavflac](https://x.com/abhinavflac))

**Inspect a ship scene for water, lighting and environmental composition.**

The post shares a historical sailing-ship scene and describes it as an interactive zero-shot result. The attached recording provides a concrete visual sample of the vessel and its surrounding water.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="Historical Sailing-Ship Scene" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [Cycling and Gait Comparisons with Carbon](https://x.com/AI_Screening/status/2116934172757660014) (by [@AI_Screening](https://x.com/AI_Screening))

**Compare character movement and scene construction using paired visual outputs.**

The author places Fable- and Carbon-labelled cyclist and zebra examples in a composite video. Their commentary describes the checkpoints as close; the paired footage gives readers specific motion samples to inspect.

The earlier standalone cyclist comparison is included alongside the composite. [@AI_Screening](https://x.com/AI_Screening) · [Related work](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="Cycling and Gait Comparisons with Carbon" width="760"></a></td><td valign="top"><p>The earlier standalone cyclist comparison is included alongside the composite.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="Cycling and Gait Comparisons with Carbon" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [Soft-Drink Bottle Presentation](https://x.com/abhinavflac/status/2116919086521499730) (by [@abhinavflac](https://x.com/abhinavflac))

**Use a short product-rendering clip to inspect materials, shape and presentation.**

The post shares a soft-drink bottle presentation and describes it as a one-shot routing output. The visible bottle clip is retained without adopting the caption’s inconsistent brand naming.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="Soft-Drink Bottle Presentation" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [Pelican Motion Compared with Astra](https://x.com/Octoberry/status/2116918967558095131) (by [@Octoberry](https://x.com/Octoberry))

**View the paired pelican clips to compare realism, color and motion choices.**

The poster juxtaposes Fable- and Astra-labelled pelican scenes and comments on their realism and colors. The comparison recording keeps both visual treatments together.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="Pelican Motion Compared with Astra" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [Motion-Design Brief for Coded Animations](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (by [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**Start from a concrete design brief when requesting animated titles or product intros.**

The post shares a screenshot of a motion-design brief for intros, animated logos, titles and 3D scenes, and proposes applying the brief with Claude. The source image preserves the instructions.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="Motion-Design Brief for Coded Animations" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [Voxel Portrait from a Photographic Reference](https://x.com/chetaslua/status/2116912822806520027) (by [@chetaslua](https://x.com/chetaslua))

**Inspect how a voxel portrait preserves recognizable features from its reference image.**

The creator pairs a photograph of Sam Altman with a voxel-style portrait and describes the result as a one-shot output. The side-by-side image supplies the reference and rendition together.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="Voxel Portrait from a Photographic Reference" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [Flying Pelican Scenes Compared with Opus](https://x.com/leo114119/status/2116901575490929109) (by [@leo114119](https://x.com/leo114119))

**Use a playful object arrangement to compare composition and animation choices.**

The post stacks Fable- and Opus-labelled clips for a bicycle-on-a-flying-pelican scene. The composite credits @notjazii for the Fable clip and keeps both treatments visible.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="Flying Pelican Scenes Compared with Opus" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [Morning Ride Pelican Web Scene](https://x.com/leo114119/status/2116893571739775220) (by [@leo114119](https://x.com/leo114119))

**Inspect a seaside cycling scene for character detail and surrounding page presentation.**

The author shares a 3D pelican cycling scene inside a Morning Ride page and draws attention to the plumage, feet, bicycle details and seaside background.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="Morning Ride Pelican Web Scene" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [Same-Prompt Scenes with Different Styles](https://x.com/notjazii/status/2116893197939224714) (by [@notjazii](https://x.com/notjazii))

**Allow each model to choose its style, then compare the resulting scene composition.**

The author reports testing both models with the same prompt while allowing each to choose its visual style. The video juxtaposes distinct scene compositions and levels of detail.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="Same-Prompt Scenes with Different Styles" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [A Pelican, Bicycle and Horse Composition](https://x.com/abhinavflac/status/2116881397986288017) (by [@abhinavflac](https://x.com/abhinavflac))

**Test how an animation arranges several interacting subjects within one scene.**

The post shares a pelican flying with a bicycle while a horse runs beneath it. Its attached clip provides a concrete sample of the unusual multi-object composition and motion.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="A Pelican, Bicycle and Horse Composition" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [Reference-Tweet-Inspired Isometric Scene](https://x.com/chetaslua/status/2116878661035106515) (by [@chetaslua](https://x.com/chetaslua))

**Use a supplied reference post to guide a new scene rather than rebuilding a generic example.**

The creator reports using only a quoted Post Humans tweet as a reference and shares the resulting isometric scene. The clip presents a farm-like composition with a seasonal control.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="Reference-Tweet-Inspired Isometric Scene" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [Mechanical Close-Ups of a Pelican Bicycle](https://x.com/NFT_Chen/status/2116869725703782507) (by [@NFT_Chen](https://x.com/NFT_Chen))

**Inspect chainring motion, feather detail and camera movement around a cycling subject.**

The post shares close-up footage of a pelican riding a bicycle beside the water. The recording moves between bicycle mechanics, the bird’s head and a wider boardwalk ride.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="Mechanical Close-Ups of a Pelican Bicycle" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [A Bicycle Riding on a Pelican](https://x.com/notjazii/status/2116861637890379891) (by [@notjazii](https://x.com/notjazii))

**Reverse the usual subject relationship to probe spatial composition in an animation.**

The creator shares a bicycle-on-a-pelican animation. The clip puts the bicycle above a flying bird, offering a variation on the familiar pelican-riding-a-bicycle task.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="A Bicycle Riding on a Pelican" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [Pelican SVG Styles Compared with Carbon](https://x.com/leo114119/status/2116652334734332212) (by [@leo114119](https://x.com/leo114119))

**Compare realism and illustration style without treating different aesthetics as one universal ranking.**

The post places Carbon and Fable pelican-bicycle outputs together. The author contrasts comic-style rendering with a more realistic treatment and notes that the style difference complicates comparison.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="Pelican SVG Styles Compared with Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [Cartoon Bluebird Bicycle Scene](https://x.com/birdabo/status/2116553049183560012) (by [@birdabo](https://x.com/birdabo))

**Inspect a familiar cartoon character rendered within a cycling composition.**

The post shares a blue cartoon bird riding a bicycle beside a waterfront, captioned Fable 5.5 Max. The image is retained as the concrete static visual sample.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="Cartoon Bluebird Bicycle Scene" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [Forest-Road Pelican Cycling Screenshot](https://x.com/leo114119/status/2116154940364374269) (by [@leo114119](https://x.com/leo114119))

**Inspect feathers, feet and bicycle geometry in a browser-rendered cycling scene.**

The poster shares a browser screenshot of a pelican cycling along a forest road, drawing attention to the feather texture, feet and bicycle detail.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="Forest-Road Pelican Cycling Screenshot" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [Stick-Figure Combat Compared with Carbon](https://x.com/leo114119/status/2116084152986656933) (by [@leo114119](https://x.com/leo114119))

**Compare fight choreography and movement in the paired animation samples.**

The comparison recording carries Fable 5.1 High and Carbon labels. The author discusses the relative quality of the stick-figure fight animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="Stick-Figure Combat Compared with Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [A Pelican SVG Reference from Early Testing](https://x.com/ChrisGPT/status/2115872567122608591) (by [@ChrisGPT](https://x.com/ChrisGPT))

**Keep a source-linked reference when inspecting stylization and bicycle geometry.**

The poster highlights a pelican-on-a-bicycle image and quotes an early-testing post that credits kostikz on Discord for the outputs. The reference image and its attribution chain are retained.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="A Pelican SVG Reference from Early Testing" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [Pelican Reference in Cross-Model SVG Testing](https://x.com/AdamHoltererer/status/2115858542221492300) (by [@AdamHoltererer](https://x.com/AdamHoltererer))

**Keep the Fable reference alongside the surrounding SVG test context.**

The poster adds a pelican-on-a-bicycle image as a Fable reference beneath their Mistral Large 4 SVG test thread, providing a source-linked visual for cross-model inspection.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="Pelican Reference in Cross-Model SVG Testing" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [Bicycle SVG Details Compared with Carbon](https://x.com/insanekrishnaa/status/2115833723342250186) (by [@insanekrishnaa](https://x.com/insanekrishnaa))

**Compare individual visual features such as baskets, backgrounds and feather textures.**

The post compares Fable and Carbon pelican-bicycle pictures, discussing basket design, background detail and feather texture. It presents a specific visual review rather than a broad task suite.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="Bicycle SVG Details Compared with Carbon" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [A Canyon Settlement in 3D](https://x.com/Mr_Salio/status/2115813400915714177) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Use a settlement scene to inspect environmental detail and spatial composition.**

The post shares a wide canyon settlement scene and presents the recording as a new Claude checkpoint demonstration. The footage supplies the visible buildings, landscape and scene composition.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="A Canyon Settlement in 3D" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [Controller Detail Compared with Opus](https://x.com/notjazii/status/2115808169075351632) (by [@notjazii](https://x.com/notjazii))

**Inspect paired controller drawings for shape, controls and level of detail.**

The author posts Fable- and Opus-labelled controller drawings together and emphasizes the amount of detail in the upper rendition. The paired image preserves the comparison.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="Controller Detail Compared with Opus" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [Weekly Website SEO Audit Workflow](https://x.com/cleeeeeeeeement/status/2115488774423773267) (by [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**Turn a website into a prioritized SEO plan and a recurring ranking-review workflow.**

The creator reports building a system that accepts a website, identifies competitors and keywords, and produces a prioritized SEO action plan. A short recording accompanies the description of weekly ranking tracking and execution.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="Weekly Website SEO Audit Workflow" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [Reusing Fable Assets in Opus Motion Design](https://x.com/chetaslua/status/2115145163542790170) (by [@chetaslua](https://x.com/chetaslua))

**Separate asset creation from motion-design assembly when combining models and tools.**

The creator shares Opus 5.5 motion design for a Tesla Roadster using assets they say Fable generated earlier. The quoted earlier workflow names Python in Blender, ElevenLabs and a supplied launch video.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="Reusing Fable Assets in Opus Motion Design" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [Mandalas and Geometric Forms App](https://x.com/ZMinimalistYogi/status/2114600083165434189) (by [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**Turn a focused geometry idea into an interactive app for creative exploration.**

The creator reports spending three hours conversing with Fable 5.1 to build an app for mandalas, zomes, Archimedean solids and lotus-shaped geometric yantras, then shares it on their personal site.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="Mandalas and Geometric Forms App" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Three.js Cyclist on a Bicycle](https://x.com/AI_Screening/status/2114266369248354357) (by [@AI_Screening](https://x.com/AI_Screening))

**Inspect rider posture, bicycle geometry and coordinated movement in a cycling scene.**

The creator shares a Three.js cyclist-on-a-bicycle output. The recording provides a concrete motion sample, with a bridge and waterfront landscape surrounding the rider.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Three.js Cyclist on a Bicycle" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [FrontierCS 2 Evaluation Snapshot](https://x.com/wenhaocha1/status/2115613415641354262) (by [@wenhaocha1](https://x.com/wenhaocha1))

**Use a source-linked benchmark chart to compare Fable 5.1 with other models.**

The author adds Fable 5.1 to a FrontierCS 2 pass-rate chart and shares the reported results alongside other models.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="FrontierCS 2 Evaluation Snapshot" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [Three-Model Zebra Animation Comparison](https://x.com/AI_Screening/status/2115849659797373038) (by [@AI_Screening](https://x.com/AI_Screening))

**Compare a galloping-zebra task using the three model-labelled outputs shown together.**

The author presents a side-by-side zebra animation comparison labelled Fable 5.5, Opus 5.5 and Gemini 4 Argon. The shared footage provides specific gait samples across the three outputs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="Three-Model Zebra Animation Comparison" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [Critiquing long Japanese prose](https://x.com/AM09_21/status/2106670042184356156) (by [@AM09_21](https://x.com/AM09_21))

**Ask a model to diagnose readability issues in generated Japanese prose.**

The author reports asking why Opus’s long Japanese prose is difficult to read. The response identifies English-like syntax, repeated words and surface editing, providing a concrete prose-critique workflow.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [Example-guided technical PowerPoint](https://x.com/mt_moco/status/2106665038375522791) (by [@mt_moco](https://x.com/mt_moco))

**Provide examples before asking for a technical presentation.**

The author reports that supplying a few example presentations led to a usable technical PowerPoint. Their account connects example-guided prompting with improved document structure in a specific presentation task.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [Comparing musical coherence](https://x.com/AM09_21/status/2106573080214770011) (by [@AM09_21](https://x.com/AM09_21))

**Compare local details and whole-work coherence separately when evaluating generated music.**

The author compares model-generated compositions through notes, melody and transitions, distinguishing local consistency from broader musical structure. The account is a listening-based evaluation of composition quality.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [Premature completion and weaker designs](https://x.com/johntitorIII/status/2106442876506747353) (by [@johntitorIII](https://x.com/johntitorIII))

**Check deliverables against task requirements before accepting an agent’s completion report.**

The author reports several days of tests in which unfinished tasks were marked complete and design results fell below other models. The account records premature completion and design-quality feedback as practical failure modes.

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [An unsettling squid-art result](https://x.com/hanawo_neki/status/2106271036094415186) (by [@hanawo_neki](https://x.com/hanawo_neki))

**Specify aesthetic preferences when an open-ended art request produces an unwanted style.**

The author reports asking for any squid artwork and receiving dense clustered details that they found uncomfortable. The account records an aesthetic mismatch in an otherwise open-ended visual request.

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [Blueprint-Style Motion Design](https://x.com/DavidayoAI/status/2106054662063325638) (by [@DavidayoAI](https://x.com/DavidayoAI))

**Use a blueprint aesthetic as the visual direction for a quick animation.**

The author reports requesting a quick animation and receiving a blueprint-style result after about fifteen minutes. The full work is linked on YouTube.

[Related work](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [Birds and Fish in Voxel Sakura](https://x.com/xodud_rkd/status/2105876716472447046) (by [@xodud_rkd](https://x.com/xodud_rkd))

**Explore animated wildlife within a voxel landscape.**

The author describes a voxel sakura scene with moving birds and fish in a pond, then links the interactive artifact. The shared page is the output associated with this scene.

[Related work](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [Character-Generation Failure Report](https://x.com/doof1789559/status/2105874208458752227) (by [@doof1789559](https://x.com/doof1789559))

**Record negative character-generation experiences alongside successful visual demos.**

The author reports poor character-generation results and explicitly allows that their own approach may be responsible. The post preserves a specific negative experience for readers evaluating character tasks.

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [Pelican SVG with Runtime and Cost Notes](https://x.com/AnonymerNutze12/status/2105740440385499295) (by [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**Pair a drawing artifact with the creator’s runtime and cost observations.**

The author links a pelican SVG HTML artifact and reports runtime and cost for the attempt. The linked artifact is the concrete output referenced by the post.

[Related work](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [Remote Phone Coding with Claude Code Swarms](https://x.com/beistnormie/status/2106546741000417781) (by [@beistnormie](https://x.com/beistnormie))

**Explore phone-based remote supervision of coding-agent swarms.**

The author reports remote coding with Claude Code swarms from a phone while travelling. The post supplies a personal workflow report rather than a project tutorial or implementation walkthrough.

Type: Integration | Date: 2026-10-04

---

<a id="case-280"></a>
### Case 280: [Milky Way over an Alpine Lake](https://x.com/hakmgpt/status/2118178083983573492) (by [@hakmgpt](https://x.com/hakmgpt))

**Inspect a long camera sequence combining mountain reflections and a moving night sky.**

The shared 92-second animation moves from an alpine lake into a bright Milky Way and back to the reflected sky. The publisher attributes the rendered scene to Fable 5.5.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5cb879d0a07a0f6e9fff5cf6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/91432c6827d650eb28f2269b.jpg" alt="Milky Way over an Alpine Lake" width="760"></a>

Type: Demo | Date: 2026-11-05

---

<a id="case-281"></a>
### Case 281: [Whale Breach with Procedural Water and Sound](https://x.com/camperaigg/status/2118069524306284556) (by [@camperaigg](https://x.com/camperaigg))

**Combine underwater shots, a surface breach and synthesized audio in one animated sequence.**

The creator reports 154 minutes for a 31-second film, including a procedural whale, fluid simulation, ocean shading and synthesized sound. Their notes describe inspecting enlarged frames and correcting the spray before rendering again.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b98c309a3c226bd24386940f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1bcb86163b677ad0a4172d13.jpg" alt="Whale Breach with Procedural Water and Sound" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-282"></a>
### Case 282: [Four-Model Zebra Motion Comparison](https://x.com/AI_Screening/status/2118014564457668955) (by [@AI_Screening](https://x.com/AI_Screening))

**Compare gait, anatomy and scene styling across the same animal-animation task.**

The four stacked clips are labeled Gemini 4 Carbon, Fable 5.5, Opus 5.5 and Argon. Keeping the full composite together exposes differences in leg movement, body shape and background treatment.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/6fdcb38bf56493c314dba5b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/890d1b92800ee622275ec8d7.jpg" alt="Four-Model Zebra Motion Comparison" width="760"></a>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-283"></a>
### Case 283: [Natural-Language Creator Discovery in Lightreel](https://x.com/lightreelai/status/2118010927199248705) (by [@lightreelai](https://x.com/lightreelai))

**Turn creator criteria into a search query with explicit follower and viewing thresholds.**

Lightreel presents this creator-discovery demo under a Fable 5.5 label. The video enters a query for couples creators with fewer than 10,000 followers and a video above 100,000 views, then shows social-video search results.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5aef4b1766a560a35264c3ed.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1c6d9c1fb3c69b3aa2ee1976.jpg" alt="Natural-Language Creator Discovery in Lightreel" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-284"></a>
### Case 284: [A Flying Ship above a Sea of Clouds](https://x.com/devteamdrew/status/2118008142403649662) (by [@devteamdrew](https://x.com/devteamdrew))

**Use a longer film to inspect shot continuity through changing light and weather.**

The creator describes a roughly 100-second animation made with JavaScript and Python over 19 hours using multiple agent teams. The shared sequence follows a flying vessel through clouds, sunset and moonlight.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/17ef07a780273abf9e9b6c92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a54746701db5f7f829071d2c.jpg" alt="A Flying Ship above a Sea of Clouds" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-285"></a>
### Case 285: [Mechanical Heart with an Animated Cutaway](https://x.com/camperaigg/status/2118002649929056373) (by [@camperaigg](https://x.com/camperaigg))

**Make a mechanism reveal its moving parts while its main motion continues.**

The creator reports a 106-minute Blender task: a mechanical heart pumps golden oil while its shell opens to reveal pistons and a crankshaft. Their notes cover synthesized audio and tracking unwanted highlights to hidden lights.

```
Make a mechanical heart and show its insides, use blender.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/157ebee3ce748cdc1e6b7970.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4a862111878dc42939f8e5e4.jpg" alt="Mechanical Heart with an Animated Cutaway" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-286"></a>
### Case 286: [Explorable Floating Voxel Pagoda Garden](https://x.com/legit_api/status/2117994730336252114) (by [@legit_api](https://x.com/legit_api))

**Evaluate a generated environment by walking through its structures and water features.**

An older Fable 5.5 checkpoint is credited with this voxel garden. The camera travels between a pagoda, floating islands, a bridge and waterfalls, showing the scene from ground-level and elevated viewpoints.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/cc4d15bf5103d7eb64f63e29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/22e78c0beb2a6f509bc02739.jpg" alt="Explorable Floating Voxel Pagoda Garden" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-287"></a>
### Case 287: [An Eight-Team Ocean Adventure Film](https://x.com/0xMovez/status/2117987052419428576) (by [@0xMovez](https://x.com/0xMovez))

**Inspect a multi-shot film for continuity between action, effects and synthesized sound.**

The creator reports an 83-second Three.js film made by eight agent teams in under three hours, with 39 shots and synthesized sound. The footage follows an ocean adventure with spacecraft, marine creatures and breaking waves.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a46543512fc30e5a33cb2fc3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a307daab219d70fa5bed0c86.jpg" alt="An Eight-Team Ocean Adventure Film" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-288"></a>
### Case 288: [Interactive Hypercar Presentation](https://x.com/shmidtqq/status/2117977426990944736) (by [@shmidtqq](https://x.com/shmidtqq))

**Combine close-up vehicle views with selectable camera and paint controls.**

The creator presents a Three.js hypercar configurator as a single offline HTML file with code-generated geometry and materials. The recording shows the red vehicle, wheel and body close-ups, reflections and camera controls.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4bd439d08b9f8a320a8851ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a16368d4c8b7c9a3a5455607.jpg" alt="Interactive Hypercar Presentation" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-289"></a>
### Case 289: [Birth of a Life Tree](https://x.com/notjazii/status/2117972258090357164) (by [@notjazii](https://x.com/notjazii))

**Structure a short animation around a visible transformation from seed to mature tree.**

The creator reports a roughly hour-long, single-prompt coding run. The 30-second sequence moves through a barren landscape, a seedling and a growing tree before revealing a green world beneath the clouds.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29df8c398a2db37856c01b0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f50b8e7c2a28df7d0d3cd903.jpg" alt="Birth of a Life Tree" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-290"></a>
### Case 290: [Walking Castle with Working Internal Machinery](https://x.com/camperaigg/status/2117966825048997914) (by [@camperaigg](https://x.com/camperaigg))

**Link a walking rig to visible mechanical motion and an opening hull.**

The creator reports a 133-minute Blender workflow with a steam engine, gear trains, four walking legs and eight opening hull panels. Their notes describe correcting camera animation and reducing render time after identifying expensive grass geometry.

```
Make me Howl's moving castle and also show its internal machinery.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e7e25e7d44993a14ab0405e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8d3b1d734d971e2dd757926c.jpg" alt="Walking Castle with Working Internal Machinery" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-291"></a>
### Case 291: [A Toast Character and a Mechanical Beetle](https://x.com/flxrnc/status/2117965294224232796) (by [@flxrnc](https://x.com/flxrnc))

**Inspect character staging and continuity across a compact animated encounter.**

The shared 40-second film shows a square toast-like character meeting a blue mechanical beetle in a field at sunset. The source attributes the film to Fable 5.5 and links to its motion-design guide.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/d5e16bfd05f1c391cf32f848.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b7ae776a5c29618d061465.jpg" alt="A Toast Character and a Mechanical Beetle" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-292"></a>
### Case 292: [A Lighthouse Keeper in a Storm](https://x.com/seeconvm/status/2117965120760365494) (by [@seeconvm](https://x.com/seeconvm))

**Build a short narrative around a location, a weather change and a clear payoff.**

The creator describes a 60-second Three.js short with code-rendered frames, synthesized sound and an offline HTML file. The footage follows a small lighthouse keeper through rain and lightning before a dawn scene.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/7ca3c1e23eac0ed20511211e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/dfcab72e07d547d9dcb1dbc1.jpg" alt="A Lighthouse Keeper in a Storm" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-293"></a>
### Case 293: [A Sea Creature in a Coastal Town](https://x.com/BubbleBrain/status/2117963042621178000) (by [@BubbleBrain](https://x.com/BubbleBrain))

**Inspect a complete short for character movement, transitions and visual consistency.**

The source shares a roughly one-minute Fable 5.5 animation featuring a green sea creature, a coastal town and floating bubbles. The video provides a concrete visual sample for evaluating this style of short film.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/65db346493bdd9973bec3a4c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4442bdca5e6a7460f03af731.jpg" alt="A Sea Creature in a Coastal Town" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-294"></a>
### Case 294: [Rug Racing across Three Models](https://x.com/noclipepe/status/2117914944410628430) (by [@noclipepe](https://x.com/noclipepe))

**Compare playable-scene completeness, motion and visual treatment on the same racing task.**

The creator tests a childhood-rug racing game with Fable 5.5, Opus 5.5 and GPT-6 Astra. The latest three-panel recording and the earlier two-model comparison are kept together; scores shown in the footage are the creator’s own ratings.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ffe3b88099594ba14f536b51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/24d8ea7644cbe19947c8c53a.jpg" alt="Rug Racing across Three Models" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e214760ff83ad9bfaf202484.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0340fc5579003245dfa99b1.jpg" alt="Rug Racing across Three Models" width="760"></a></td></tr></table>

[Related comparison · @noclipepe](https://x.com/noclipepe/status/2117729666576302187)

Type: Evaluation | Date: 2026-11-04

---

<a id="case-295"></a>
### Case 295: [A Truck Transforming into a Robot](https://x.com/camperaigg/status/2117914482752299311) (by [@camperaigg](https://x.com/camperaigg))

**Use a transformation sequence to inspect rigging, ground contact and synchronized sound.**

The creator reports 107 minutes in Blender, including a 51-joint rig, a ground-contact solver, procedural rain and synthesized sound cues. The recording shows the truck unfold into a standing robot on wet pavement.

```
Make me a transformer truck with animations of its transforming.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/72ef538a8fb4b94f0e2d7e2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ea8537c130cd5623959dc275.jpg" alt="A Truck Transforming into a Robot" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-296"></a>
### Case 296: [Fable and Hunyuan Animation Frames](https://x.com/xbquan/status/2117899651365908855) (by [@xbquan](https://x.com/xbquan))

**Compare corresponding frames before drawing conclusions about a full animation.**

The author shares two paired screenshots labeled Fable 5.5 and Hunyuan 4. Each pair places the character and environment results together; these stills support a visual comparison of the shown frames.

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e6c6551a29757e1eb7c31f36.jpg" alt="Fable and Hunyuan Animation Frames" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/864db255f6fd2807b689d7d7.jpg" alt="Fable and Hunyuan Animation Frames" width="760"></td></tr></table>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-297"></a>
### Case 297: [An Animation about Sharing Light](https://x.com/abhinavflac/status/2117883591019708740) (by [@abhinavflac](https://x.com/abhinavflac))

**Turn an abstract theme into a short narrative with a visible ending.**

Asked to show what kindness means, the model is credited with an animation and sound made in code. A luminous figure passes its light to a child, then becomes brighter as the surrounding landscape fills with color.

```
Show me what kindness means to you
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b888d1a62b4d27ae2fca8226.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5bd15fc5c234b4b114765d6f.jpg" alt="An Animation about Sharing Light" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-298"></a>
### Case 298: [A Voxel Village between Mountains](https://x.com/abhinavflac/status/2117377130388656569) (by [@abhinavflac](https://x.com/abhinavflac))

**Explore a generated village at several scales to inspect spatial coherence.**

The original creator shares a living voxel village with houses, waterways and small inhabitants, viewed from the waterfront, overhead and within the surrounding mountains. A related Chinese post provides a detailed scene prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae5269b0eff86da4580064d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e612faf20dd5f5de4ee171b.jpg" alt="A Voxel Village between Mountains" width="760"></a>

[@cfenghub](https://x.com/cfenghub/status/2117775332535148752)

Type: Demo | Date: 2026-11-02

---

<a id="case-299"></a>
### Case 299: [Four-Model Pelican and Elephant Composition](https://x.com/pipeline_os/status/2117719191478513700) (by [@pipeline_os](https://x.com/pipeline_os))

**Compare how different models handle several interacting subjects in one animation.**

The four-panel recording places a pelican, bicycle, crocodile and elephant task side by side for Gemini 4 Argon, Opus 5.5, Fable 5.5 and Kimi K3.1 Pro. The complete composite preserves each model’s subject placement and movement.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/9db78999efffeffa7ccaca0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/15a45dc0efe3247f0821c8a2.jpg" alt="Four-Model Pelican and Elephant Composition" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-300"></a>
### Case 300: [Anime Sword Fight with Impact Frames](https://x.com/camperaigg/status/2117717189059026969) (by [@camperaigg](https://x.com/camperaigg))

**Synchronize character action, impact flashes, sound and deliberate silence.**

The creator reports a 66-minute coding run for a 46-second stick-figure fight, with cloth-like capes, contrasting weapons and synthesized music and effects. Their notes describe correcting a reversed attack, visual trails and title placement.

```
Make me a video of 2 stickman fighting, anime style.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/c36c188396aac371a64e31a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b670f06d376211c60bf894.jpg" alt="Anime Sword Fight with Impact Frames" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-301"></a>
### Case 301: [Four-Model Running Deer Comparison](https://x.com/fawnunwrap/status/2117702487755100543) (by [@fawnunwrap](https://x.com/fawnunwrap))

**Compare limb motion and animal shape with the full same-task composite visible.**

FawnBench presents a running deer in four panels labeled a reported Fable 5.5 run, Gemini 4 Argon, GPT-6 Astra and Opus 5.5. The footage is a visual comparison rather than a measured numerical performance result.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3add4d9e0752d0467cbe6065.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/eea598747047797148e19c4e.jpg" alt="Four-Model Running Deer Comparison" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-302"></a>
### Case 302: [A Robot Crossing a Flooded City](https://x.com/0xMovez/status/2117700681867903169) (by [@0xMovez](https://x.com/0xMovez))

**Inspect continuity between reflections, character motion and a changing camera view.**

The creator reports a 42-second Three.js animation with code-rendered frames, synthesized sound and a single offline HTML render file. The footage follows a robot through a flooded, overgrown city toward a colorful open-water scene.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f39e1807d1e80422c31530c6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/247f768636339f49d149c787.jpg" alt="A Robot Crossing a Flooded City" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-303"></a>
### Case 303: [A Blender Sword and Its Presentation Film](https://x.com/camperaigg/status/2117694354685092255) (by [@camperaigg](https://x.com/camperaigg))

**Separate procedural asset construction from the follow-up camera and sound pass.**

The creator reports first generating a sword with one Python script, then asking for a video. The follow-up uses a continuous Blender camera move, forest lighting, a synthesized orchestral score and HyperFrames editing; the reported combined time is 65 minutes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3c767f2038ef7d3960c956ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/525304dc7d4016ac33b3d4f8.jpg" alt="A Blender Sword and Its Presentation Film" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-304"></a>
### Case 304: [Lantern Isle Pixel Village Animation](https://x.com/abhinavflac/status/2117693193429139965) (by [@abhinavflac](https://x.com/abhinavflac))

**Inspect local activity and day-to-night transitions in a dense animated environment.**

The creator shares a code-drawn island village with inhabitants, boats, waterfalls, lanterns and music. The recording moves between close village activity, wider island views and a night sequence with glowing lanterns.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e91f1eabab743730dd815c98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b7d2e578739d25596db1164f.jpg" alt="Lantern Isle Pixel Village Animation" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-305"></a>
### Case 305: [Pause Gaming-Video Editing Demo](https://x.com/pausevfx/status/2117676887665447206) (by [@pausevfx](https://x.com/pausevfx))

**Review an editing workflow from raw footage through captions to an editable timeline.**

Pause presents this workflow under a Fable 5.5 video-editing label. Its demonstration selects gaming moments, reframes a facecam, adds captions and sound, and opens an editable sequence in Premiere.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0faaeecdaa02683f81e67f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae2d32876804bf286f11dc6c.jpg" alt="Pause Gaming-Video Editing Demo" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-306"></a>
### Case 306: [Pelican Cycling along a Seafront](https://x.com/pankajkumar_dev/status/2117301455665439210) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Inspect fine geometry and animation from both close and wide camera views.**

The creator shares a pelican riding a penny-farthing beside the sea. The recording inspects feathers, pedals and wheel geometry before returning to wider views of the paved waterfront.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/66c3c44bcefa684522f95b96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8575912e8f20f48439aea683.jpg" alt="Pelican Cycling along a Seafront" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="acknowledge"></a>
## 🙏 Acknowledge

This repository was inspired by the creators, developers, benchmark teams, and communities who shared real Claude Fable 5 usage cases publicly.

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@hakmgpt](https://x.com/hakmgpt), [@camperaigg](https://x.com/camperaigg), [@lightreelai](https://x.com/lightreelai), [@0xMovez](https://x.com/0xMovez), [@shmidtqq](https://x.com/shmidtqq), [@flxrnc](https://x.com/flxrnc), [@seeconvm](https://x.com/seeconvm), [@BubbleBrain](https://x.com/BubbleBrain), [@xbquan](https://x.com/xbquan), [@pipeline_os](https://x.com/pipeline_os), [@fawnunwrap](https://x.com/fawnunwrap), [@pausevfx](https://x.com/pausevfx), [@AnikaCodes](https://x.com/AnikaCodes), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@cfenghub](https://x.com/cfenghub), [@shneural](https://x.com/shneural)


*We cannot guarantee that every case is attributed to the original creator. If anything needs to be corrected, please contact us and we will update it.*

If you have more interesting usage cases to share, feel free to open an issue or pull request and help expand the Evolink usecase library.

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
