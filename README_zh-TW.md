<div align="center">

<a href="https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5"><img src="images/zh-tw.png" alt="Claude Fable 5 high usecase repository logo" width="760"></a>

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
## 🍌 簡介

歡迎來到 Claude Fable 5 高訊號使用案例庫。

**我們收集 Claude Fable 5 的真實使用案例、教學、整合與評測，內容精選自公開 demo 與創作者社群。**

這份繁體中文 README 聚焦於具備具體工作流程、提示詞、demo、整合、基準測試證據或實際限制的高訊號案例。

大多數案例整理自 X/Twitter 貼文與公開 demo。每個案例標題都連回原始來源，每個作者帳號都連到創作者個人頁面。

在 Evolink 上試用：[Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

<a id="-overview"></a>
## 📊 概覽

- **88 個原有 Fable 5 案例，加上 9 個 Fable 5.5 社群展示，共 97 個案例。**
- 覆蓋程式代理、長時間自動化、遊戲、視覺設計、3D 模擬、知識工作、教學、API 整合、基準測試、定價與發布限制。
- 每個案例都包含原始來源、創作者署名、精簡重點、證據類型與發布日期。
- 使用此 repo 尋找實用工作流程、比較強項與限制、發現可重現提示詞，並追蹤整合範例。

> [!NOTE]
> 這個收藏偏重具體證據而非炒作：可重現提示詞、已發布 demo、基準測試方法、整合說明、成本資料，以及清楚標出的注意事項。

<a id="-quick-api-access"></a>
## ⚡ 快速 API 接入

透過相容 Evolink 的 Messages API 使用 Claude Fable 5。先在 [Evolink](https://evolink.ai/login?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5) 取得 API token，然後將 `<token>` 替換為你的 token。

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
## 📑 目錄

| 章節 | 案例 |
|---|---|
| [💻 程式設計與程式碼生成](#coding-and-code-generation) | Case 1-6 |
| [🤖 代理與長時間自動化](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 遊戲與互動 Demo](#games-and-interactive-demos) | Case 9-12 |
| [🎨 視覺、設計、影片與 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 文件、知識工作與研究](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 教學、課程與提示詞資源](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 平台、API 與工具整合](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 評測、比較與限制](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | 致謝與更正說明 |

### [💻 程式設計與程式碼生成](#coding-and-code-generation)

| Case | 展示內容 | 類型 |
|---|---|---|
| [Cursor 多階段工作流程](#case-1) | 在多模型 Cursor 工作流程中，把 Fable 5 作為規劃審查與批判步驟，然後把實作與修訂交回較便宜或專門化的模型。 | 評測 |
| [從截圖重建 GitHub](#case-2) | 把產品截圖貼進代理式程式設計工具，要求 Fable 5 以可運作功能重建介面。 | 展示 |
| [單一提示詞黑洞模擬](#case-3) | 給 Fable 5 一個詳細的創意程式提示詞，要求它產生一個自包含的 Three.js 物理視覺化。 | 教學 |
| [一次生成 macOS 風格 Web OS](#case-4) | 要求 Fable 5 建立完整的單檔 Web OS，讓它一次建出 UI shell、app、互動、音訊與內嵌遊戲行為。 | 教學 |
| [用 1,687 個提示詞打造 Spawn 5.0](#case-5) | 把 Fable 5 作為長 session 工程夥伴跨越大量提示詞使用，人類角色則從架構轉向判斷輸出品質。 | 教學 |
| [大型 Pull Request Review 與發現](#case-6) | 把大型 pull request 交給 Fable 5，要求它 review 正確性、誤報、真實 bug 與打磨問題。 | 展示 |

### [🤖 代理與長時間自動化](#agents-and-long-running-automation)

| Case | 展示內容 | 類型 |
|---|---|---|
| [長時程接力工作流程評測](#case-7) | 把 Fable 5 用於有野心的長時程工作：網站重建、程式化內容管線、語氣匹配、安全 review 與最終品質檢查。 | 評測 |
| [診斷基礎設施故障並開出修復 PR](#case-8) | 給 Fable 5 存取 logs、database errors、image digests 等 infra 線索，然後要求它診斷故障並準備修復。 | 評測 |

### [🎮 遊戲與互動 Demo](#games-and-interactive-demos)

| Case | 展示內容 | 類型 |
|---|---|---|
| [手指追蹤 Dino Runner](#case-9) | 要求 Fable 5 建立一個以手指追蹤作為輸入機制的瀏覽器遊戲。 | 展示 |
| [兩句話打造賽車遊戲](#case-10) | 給 Fable 5 一個很短的遊戲提示詞，讓它一次生成地圖、模式、音樂、UI 與遊戲素材。 | 教學 |
| [Rust 可安裝終端版 Minecraft](#case-11) | 透過終端機程式設計 harness 執行 Fable 5，要求它建立一個可安裝的 Rust 終端機遊戲。 | 展示 |
| [附時間與成本的 Minecraft 複製版](#case-12) | 用一個提示詞要求 Fable 5 產生可玩的 Minecraft 風格複製版，然後評估時間、成本、程式碼量與功能覆蓋。 | 教學 |

### [🎨 視覺、設計、影片與 3D](#visual-design-video-and-3d)

| Case | 展示內容 | 類型 |
|---|---|---|
| [完整可重現的電商 Email 提示詞](#case-13) | 給 Fable 5 一份完整的品牌 email mockup 創意 brief，包含精確 section、產品需求、視覺方向與限制。 | 教學 |
| [瑞士槓桿鐘錶匠基準測試](#case-14) | 把 Fable 5 用於機械模擬基準測試，要求它實作、驗證並迭代物理正確性。 | 評測 |
| [Three.js Friends 公寓場景](#case-15) | 提示 Fable 5 把平面圖與場景參考轉成可瀏覽的 Three.js 環境。 | 評測 |
| [含提示詞與 URL 的太陽系模擬](#case-16) | 使用 Fable 5 從物理原理建立天文模擬，反覆迭代直到模擬與公開輸出準備完成。 | 教學 |

### [📚 文件、知識工作與研究](#documents-knowledge-work-and-research)

| Case | 展示內容 | 類型 |
|---|---|---|
| [Stripe 與科學工作流程證據](#case-17) | 把這當作企業遷移與科學工作流程主張的證據，而不是可複製貼上的提示詞。 | 評測 |
| [政策備忘錄與修訂追蹤工作流程](#case-18) | 把 Fable 5 用於長篇質性文件工作：修訂追蹤、評論 triage，以及由逐字稿驅動的編輯。 | 教學 |
| [Deep Research 提示詞與輸出](#case-19) | 向 Fable 5 提出研究風格問題，評估它是否能產生結構化、具歷史脈絡的長答案。 | 展示 |

### [🧭 教學、課程與提示詞資源](#tutorials-courses-and-prompt-resources)

| Case | 展示內容 | 類型 |
|---|---|---|
| [Fable 5 如何改變 Claude Code 工作流程](#case-20) | 使用 Fable 5 時，設定方向、context、goals 與驗證標準，而不是微管理每一步。 | 展示 |
| [十億 token 評測與路由策略](#case-21) | 把 Fable 5 用於 frontier planning 與 review，再把高量實作路由給較便宜的模型。 | 教學 |
| [防禦式裝置強化提示詞](#case-22) | 執行逐步防禦式強化提示詞，讓 Fable 5 盤點裝置、給出精確檢查，並等待驗證。 | 教學 |
| [全站設計稽核 Goal 提示詞](#case-23) | 使用 `/goal` 讓 Fable 5 啟動網站、截圖頁面、稽核 UX、撰寫報告，並修復安全的小問題。 | 教學 |
| [長篇創作工作流程分工](#case-24) | 使用 Fable 5 設計穩定格式與範例，再把該結構交給另一個生成系統產生特定領域輸出。 | 教學 |
| [Fable 5 入門使用指南](#case-25) | 使用 Fable 5 時採用目標導向提示詞、驗證 loop 與 effort settings，而不是小步驟指令。 | 評測 |
| [可直接複製貼上的 repo 稽核提示詞](#case-26) | 把 repository audit prompt 貼進 Fable 5，要求它做 file-backed discovery、findings、strategy 與 milestone task plan。 | 教學 |
| [有限使用視窗策略](#case-27) | 在 access window 有利時，把 Fable 5 用量花在 audit、architecture 與 planning，再用較便宜模型執行。 | 教學 |
| [在 Claude Code 中使用 Goals 與 Workflows](#case-28) | 在實作前把 Fable 5 當作 thought partner，然後結合 `/goal` 與 workflows 執行並驗證計畫。 | 教學 |

### [🔌 平台、API 與工具整合](#platform-api-and-tool-integration)

| Case | 展示內容 | 類型 |
|---|---|---|
| [Hermes Agent 整合設定](#case-29) | 設定 Hermes 使用 `anthropic/claude-fable-5` 來執行複雜 `/goal` runs 與快取的長時程任務。 | 教學 |
| [能力、定價與訂閱注意事項](#case-30) | 用此案例了解 Fable 5 何時可用、成本多少，以及哪些受防護 domain 可能 fallback 到另一個模型。 | 教學 |
| [發布、存取、定價與安全摘要](#case-31) | 用此發布摘要選擇 access route、API model name、context window、caching strategy 與 subscription timing。 | 教學 |
| [基於 Advisor 的成本降低策略](#case-32) | 當邊際智慧值得成本時，把 Fable 5 作為較便宜模型工作流程中的 advisor 或 reviewer。 | 整合 |
| [定價、存取與安全防護欄](#case-33) | 在規劃 workloads 前，用此案例了解 Fable 5 access、API pricing 與 safety fallback behavior。 | 整合 |
| [Swarms 一行整合](#case-34) | 把 Swarms model name 設為 `anthropic/claude-fable-5`，並透過 Swarms framework 或 API 執行 Fable 5。 | 整合 |

### [📏 評測、比較與限制](#evaluations-comparisons-and-limits)

| Case | 展示內容 | 類型 |
|---|---|---|
| [Fable 5 vs GPT-5.5 成本與品質比較](#case-35) | 在相同 coding task 上比較 Fable 5 與 GPT-5.5，以判斷 output quality、runtime 與 tool cost。 | 評測 |
| [AA-Omniscience 基準測試結果](#case-36) | 用此 benchmark case 評估 Fable 5 的知識準確度與 hallucination behavior。 | 評測 |
| [Artificial Analysis Intelligence Index 結果](#case-37) | 用此案例將 Fable 5 的整體 intelligence ranking 與其他 frontier models 做 benchmark。 | 評測 |
| [GDPval-AA 代理式知識工作基準測試](#case-38) | 用此案例評估 Fable 5 在 agentic real-world knowledge work 上的表現。 | 評測 |
| [一週初步印象與定價機制](#case-39) | 用這個初步印象案例決定 Fable 5 最強在哪裡，尤其是 game design 與 systems planning。 | 整合 |
| [成本與速度比較](#case-40) | 用此比較決定品質增益是否值得更高成本與更慢的長時程 runs。 | 評測 |
| [Claude Code 實測筆記](#case-41) | 用此案例評估 Fable 5 在 Claude Code 內的表現，包括 tool use、personality 與仍存在的 rough edges。 | 展示 |
| [創意寫作基準測試結果](#case-42) | 用此 benchmark case 判斷 Fable 5 的短篇小說寫作品質與 refusal behavior。 | 評測 |
| [多基準測試發布摘要](#case-43) | 用此發布 benchmark summary 了解與 coding agents 與 complex tasks 最相關的 headline scores。 | 評測 |
| [與 GPT-5.5 的基準測試與定價比較](#case-44) | 用此比較依 price 與 benchmark categories 評估 Fable 5 對 GPT-5.5。 | 評測 |
| [含實務限制的一線筆記](#case-45) | 用這份 field report 了解 Fable 5 在哪些地方明顯更好，以及它仍有哪些實務限制。 | 教學 |
| [物理模擬比較](#case-46) | 對 Fable 5 與 Opus 4.8 執行相同 physics simulation prompts，比較 output quality、cost 與 speed。 | 展示 |
| [除錯體驗與設計判斷](#case-47) | 把 Fable 5 用於 debugging，要求它 measure、log、verify 與 patch，而不是單純猜測。 | 展示 |
| [多維度優缺點](#case-48) | 在把 Fable 5 當作 daily driver 前，用此案例了解實務 strengths 與 weaknesses。 | 展示 |
| [法律 S-1 起草測試](#case-49) | 用 S-1 drafting prompt 作為 legal-agent capability test，並比較 structure、formatting 與 length。 | 教學 |
| [醫療保健基準測試細節](#case-50) | 用此 benchmark note 評估 Fable 5 在 healthcare-related tasks 上的表現，並識別缺失的 hard medical evals。 | 評測 |
| [ParseBench 文件解析評測](#case-51) | 用此案例判斷 Fable 5 對 document parsing 是否比 specialized OCR systems 更具成本效益。 | 評測 |
| [SWE-Bench Pro 與 FrontierCode 比較](#case-52) | 用此 benchmark case 評估 Fable 5 是否適合 migrations、complex implementations、autonomous sessions、tests 與 visual verification。 | 評測 |
| [長問題解決能力的質性評測](#case-53) | 用此 qualitative review 了解為什麼 Fable 5 適合更長、更難的 tasks，同時仍需要 production review。 | 評測 |
| [ParseBench 忠實度與格式結果](#case-54) | 用此 ParseBench result 判斷 document faithfulness 與 formatting performance。 | 評測 |
| [基準測試、定價、存取與防護措施](#case-55) | 把此案例當作 benchmarks、pricing、access、safeguards 與 strategic implications 的廣泛 checklist。 | 評測 |
| [官方基準測試分數列表](#case-56) | 用此 benchmark list 了解 Fable 5 在 coding、computer use 與 security tasks 上的官方分數。 | 評測 |
| [APEX-SWE 基準測試方法論](#case-57) | 用此案例評估 Fable 5 在 APEX-SWE 上的表現，尤其是 observability 與 integration work。 | 評測 |
| [ProofBench 形式化數學結果](#case-58) | 用此案例評估 Fable 5 在 formal math 上相對 specialized theorem-proving systems 的表現。 | 教學 |
| [VirtueBench 初步分析](#case-59) | 用此案例檢視 Fable 5 在 virtue categories 中的 moral-reasoning behavior。 | 評測 |
| [API 空回應安全過度擬合測試](#case-60) | 用此案例了解 launch-time safety overfit risk 與 API testing 中的 empty-response behavior。 | 評測 |
| [Fable 提示詞與驗證指南](#case-61) | 用這份指南，把重點從冗長的提示詞技巧轉向目標、上下文、限制、工具與驗證迴圈。 | 教學 |
| [伊斯坦堡平台遊戲參考建置](#case-62) | 用一張參考精靈圖集加上一條轉換指令，測試 Fable 5 能否產生可玩的平台遊戲。 | 展示 |
| [商業 3D 城市儀表板](#case-63) | 用 Fable 5 把商業工作流程轉成即時 3D 城市儀表板概念。 | 展示 |
| [Three.js 黑洞遊戲一次生成](#case-64) | 用 Fable 5 一次產生基於 Three.js 的 3D 瀏覽器遊戲原型。 | 展示 |
| [DeepSWE 分數比較](#case-65) | 用這則 DeepSWE 記錄，比較 Fable 5 xHigh 與 GPT-5.5 xHigh 在軟體工程基準上的表現。 | 評測 |
| [程式庫分析成本比較](#case-66) | 用這個程式庫分析比較，評估 token 價格與人工返工成本的關係。 | 評測 |
| [Super Mario 遊戲 Token 成本](#case-67) | 用這個單次生成的遊戲案例，估算 Fable 5 的輸出品質與 token 消耗。 | 展示 |
| [Claude Code 回退設定](#case-68) | 用這個案例了解 Fable 5 訊息被標記時，Claude Code 如何切換模型。 | 整合 |
| [Namma Metro 模擬器建置](#case-69) | 用這個展示作為透過自然語言與 Fable 5 開發大眾運輸模擬器的精簡範例。 | 展示 |
| [Dusk Drive 單提示詞遊戲](#case-70) | 用這個單提示詞駕駛遊戲案例，評估 Fable 5 在無人工編修下製作低多邊形遊戲原型的能力。 | 展示 |
| [APEX-Agents Pass@1 排名](#case-71) | 用這個 APEX-Agents 結果，比較 Fable 5 Max 在多步驟自主任務上的表現。 | 評測 |
| [Claude 模型選擇手冊](#case-72) | 用這份模型選用手冊，把 Fable 5 留給 Claude Code 中最困難的任務。 | 教學 |
| [HermesWorld 自動代理循環](#case-73) | 用這個案例研究一個免手動介入的 Fable 5 循環，持續數日進行建置、測試、實際遊玩與基本功能檢查。 | 整合 |
| [麥肯錫風格報告提示詞測試](#case-74) | 用這條文件生成提示詞，評估顧問報告的結構、圖表、敘事與風險分析。 | 教學 |
| [可見防護措施上線](#case-75) | 用這則官方說明了解 Fable 5 防護機制的可見性、API 拒答原因與回退至 Opus 的行為。 | 整合 |
| [Claude Code 模型比對修正](#case-76) | 用這則 Claude Code 更新說明，避免 Fable 5 模型名稱與上下文比對發生問題。 | 整合 |
| [Claude Code 中的三個網頁應用程式](#case-77) | 用這個新手程式開發展示，觀察 Fable 5 在 Claude Code 中生成多個網頁應用程式的表現。 | 展示 |
| [Rilable 開源應用程式建構器](#case-78) | 用這個開源應用程式建構器案例，研究 Fable 5 在 iOS、網頁應用程式、沙盒與 API token 成本上的應用。 | 整合 |
| [DeepSWE 編碼代理指數首秀](#case-79) | 用更新後的 Artificial Analysis 指數，比較 Fable 5 在更難的代理式 coding 任務上的表現，這些任務避免重用公開 GitHub 修復。 | 評測 |
| [DataEmpire 網站分析遊戲](#case-80) | 讓 Claude Fable 5 把訪客與里程碑映射成遊戲實體，把原始網站分析資料變成可重玩的遊戲。 | 整合 |
| [FrontierSWE 20 小時任務訊號](#case-81) | 用 FrontierSWE 證明 Fable 5 不只適合短期修 bug，也能在超長工程任務中持續保持產出。 | 評測 |
| [KernelBench-Hard CUDA 紀錄](#case-82) | 當你需要低層最佳化而不只是現有函式庫包裝時，用 Fable 5 處理進階 CUDA kernel 生成。 | 評測 |
| [Figma Capture 登陸頁克隆](#case-83) | 把競品頁面抓進 Figma 圖層後，讓 Claude Code 搭配 Fable 5 重建結構、文案與品牌系統，而不是靠截圖猜測。 | 整合 |
| [兩小時做出 GTA 2 Clone](#case-84) | 把 Fable 5 的程式碼生成與獨立素材工具結合起來，快速做出可玩的 3D 遊戲，而不必手寫整個技術棧。 | 教學 |
| [CloudWatch 日誌分診代理](#case-85) | 讓 Fable 5 驅動的代理消化超大規模服務日誌 context，先推斷架構，再收斂到具體故障。 | 整合 |
| [沙盒中的世界盃預測器](#case-86) | 把多個 frontier 模型放進隔離沙盒，讓它們為公開預測應用研究即時新聞、傷病與黃牌背景。 | 整合 |
| [WolfBench 拒答成本案例](#case-87) | 在為 Fable 5 的長自主運行定價時，把拒答行為視為真實的基準變數。 | 評測 |
| [API 存取截止追蹤器](#case-88) | 如果你的工作流程依賴持續存取某個可能被限流或撤下的 frontier 模型，就用腳本監控可用性。 | 整合 |



### [🆕 Fable 5.5 社群展示](#fable-5-5-community-demos)

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [程式碼生成的有聲狐狸動畫](#case-89) | 用逐鏡創作要求，指定可獨立執行的 HTML 動畫及其聲音設計。 | Demo |
| [開放式創作要求生成的動畫](#case-90) | 比較程式模型根據開放式動畫要求，與依照詳細分鏡所產生的成果。 | Demo |
| [建築公司動畫網站](#case-91) | 用建築公司網站的需求，評估動畫 3D 展示與頁面構圖。 | Demo |
| [Three.js 汽車展示](#case-92) | 以汽車場景作為精簡測試，檢視 3D 構圖、材質與鏡頭呈現。 | Demo |
| [Minecraft 風格瀏覽器遊戲展示](#case-93) | 評估生成的瀏覽器遊戲時，將遊戲錄影與創作者的試玩連結一起檢視。 | Demo |
| [Three.js 鵜鶘騎自行車動畫](#case-94) | 檢視騎車場景中的角色動作協調、自行車幾何結構與環境細節。 | Demo |
| [附原始提示詞的鵜鶘騎車 SVG](#case-95) | 重用創作者的簡短 SVG 提示詞，在相同輸入下比較幾何結構與細節。 | Demo |
| [斑馬奔馳動畫樣本](#case-96) | 用動物奔馳短片檢視步態一致性與動作連續性。 | Demo |
| [保留人工下單的 TradingView 指標](#case-97) | 評估會標記可能進場點並附上簡評的指標時，保留人工執行下單。 | Demo |

<a id="coding-and-code-generation"></a>
## 💻 程式設計與程式碼生成

<a id="case-1"></a>
### Case 1: [Cursor 多階段工作流程](https://x.com/AlicanKiraz0/status/2064487347605918180) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**在多模型 Cursor 工作流程中，把 Fable 5 作為規劃審查與批判步驟，然後把實作與修訂交回較便宜或專門化的模型。**

如果看 Fable 5 和 GPT 5.5 的最終評分，差距非常小。我謙虛的使用建議是：在 Cursor 這類支援混合模型的 IDE 平台中，採用分階段工作流程。

階段 1：在程式碼 review 與專案初步檢查、同時暖身上下文時，使用 GPT 5.5 High、Minimax M3、Kimi K2.6 或 Composer 2.5 其中之一。

階段 2：準備專案計畫時，使用 GPT 5.5 Very High 或 Opus 4.8。

階段 3：分析專案計畫時，使用 Fable 5；讓它找出計畫中的缺陷。修訂時使用 GPT 5.5 Very High。

階段 4：實作計畫時，使用 Minimax M3、Deepseek v4 Max、Composer 2.5 或 Sonnet 4.6。

階段 5：最後 review 並檢查實作是否遵循計畫時，使用 GPT 5.5 High。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [從截圖重建 GitHub](https://x.com/coldopn/status/2064435234465087638) (by [@coldopn](https://x.com/coldopn))

**把產品截圖貼進代理式程式設計工具，要求 Fable 5 以可運作功能重建介面。**

🚨 Anthropic Fable 5 剛剛只靠一張截圖複製出了 GITHUB！！

我做的只是把 GitHub UI 的截圖貼進 Kilo Code，然後叫它用真實功能重建 GitHub。

它寫了 10 分鐘程式，花了 $4.07。

結果是一個可運作的 GitHub 複製版：https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [單一提示詞黑洞模擬](https://x.com/deveshcodes_/status/2064437742189379745) (by [@deveshcodes_](https://x.com/deveshcodes_))

**給 Fable 5 一個詳細的創意程式提示詞，要求它產生一個自包含的 Three.js 物理視覺化。**

@claudeai 用 Claude Fable 5 一次生成了一個 Three.js 即時黑洞引力透鏡模擬。

它包含重力透鏡、多普勒增強的吸積盤、光子球、色差，以及程式化星空。

結果：60fps、單一 HTML 檔、一個提示詞。

新的基準線太狂了 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [一次生成 macOS 風格 Web OS](https://x.com/intheworldofai/status/2064421915347812672) (by [@intheworldofai](https://x.com/intheworldofai))

**要求 Fable 5 建立完整的單檔 Web OS，讓它一次建出 UI shell、app、互動、音訊與內嵌遊戲行為。**

🚨 Claude Fable 5 剛剛一次就打造出完整的 macOS 風格 Web OS，而且比大多數模型走得更遠。

單一 HTML 檔，內嵌 CSS + JS。

從一個提示詞，它建出了：

- macOS 選單列 + dock
- 可拖曳與調整大小的 app 視窗
- 可運作的檔案總管
- 可運作的終端機 + 瀏覽器 mockup
- SVG 桌面圖示 + 通知
- 設定 app、主題與開機畫面
- 完全可運作的聲音播放器，具備真實合成且不需外部檔案
- 桌面中的可遊玩 Minecraft 複製版

全部幾乎不需修正，一次生成完成。

可運作的聲音播放器加上真正的 Minecraft 複製版，是我還沒看過其他模型做到的事。Fable 5 的前端/UI 生成正在變得誇張。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [用 1,687 個提示詞打造 Spawn 5.0](https://x.com/jsnnsa/status/2064420561078693941) (by [@jsnnsa](https://x.com/jsnnsa))

**把 Fable 5 作為長 session 工程夥伴跨越大量提示詞使用，人類角色則從架構轉向判斷輸出品質。**

claude fable 5 上線了。

spawn 5.0 是用它打造的：

- 1,687 個提示詞
- 102 個 session
- 我的工作從架構轉向判斷品味

我們打造的東西，如果用 Opus 加上一整支團隊，每一項至少都要一個月：

- 從零打造的物理引擎 Mantle，可與 Rapier 競爭，並且作為 side thread 一天內就能測試
- Clustered froxel lighting：從 8 個光源到 1,000+ 個完全動態光源
- WebGPU 上的即時 diffuse GI，還能在手機上跑
- 百萬粒子 GPU VFX，shader 架構超過 Unreal 與 Unity 內建能力
- MMO 規模 netcode
- alpha 版原生 iOS app

所有這些大約花了一週。全部都能在行動裝置上跑。清單還不包含已出貨內容的一半；完整 changelog 在 thread 裡。

基準測試不會呈現的部分是：這個模型有非常棒的性格。它真的很有趣。我在物理重寫過程中好幾次笑到哭。天才與性格不是兩個分離的功能。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [大型 Pull Request Review 與發現](https://x.com/ryanrhughes/status/2064411147076534705) (by [@ryanrhughes](https://x.com/ryanrhughes))

**把大型 pull request 交給 Fable 5，要求它 review 正確性、誤報、真實 bug 與打磨問題。**

我放手讓 Fable 5 review 單一 PR（74 個檔案 / +3,705 / -1,246），看看它表現如何。它跑了 34 分鐘，吃掉我 5 小時 session 的 42%，產生 16 個「correctness」發現，並找出：

- 2 個聽起來嚇人的誤報
- 3 個真正的 audit-correctness bug
- 約 5 個合理但小型的 UX/打磨問題
- 一堆清理意見

這真的危險到不能發布嗎？

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 代理與長時間自動化

<a id="case-7"></a>
### Case 7: [長時程接力工作流程評測](https://x.com/JJEnglert/status/2064469635190170105) (by [@JJEnglert](https://x.com/JJEnglert))

**把 Fable 5 用於有野心的長時程工作：網站重建、程式化內容管線、語氣匹配、安全 review 與最終品質檢查。**

我對 Claude Fable 5 review 的短版：我花了十億 token 測試 Claude Fable 5，感覺像是擁有不公平優勢。

我用直覺測試來判斷：把模型放進真實工作裡觀察。它是幫我省下時間，還是讓我花更多時間？它能抓到我漏掉的東西嗎？它感覺像夥伴，還是像我必須照看的工具？

這是很久以來第一個在所有重要維度都通過的模型，而且不是只好一點點。

建構：我正在重建我們的 Tenex 網站。它非常客製化，也非常困難。GPT 5.5 和 Claude 4.8 無法自行攻克。即使給了 Figma 檔案參考，它們最多也只能到 85-90%。

接著 Fable 5 看了所有東西，說它可以做得更好，直接前往原始 Webflow source，下載每個 asset，並且幾乎一次完成整件事。

然後我讓它在一個週末從零打造第二個全新的 80 頁網站。這是我作為 agency 會收 $50k 的工作。

它還串起了一整套程式化短片工廠：

- HeyGen
- ElevenLabs
- Cloudflare
- 一台 VPS

這條管線會找主題、寫腳本、剪影片、加音樂並發布到社群。它能自行長時間運行，甚至為自己建了一套 webhook 系統來監控 render。

寫作：它幾乎一模一樣地複製了我們的品牌語氣文件，然後在 80 頁功能頁、案例研究與文章中維持這個語氣，沒有漂移成扁平的 AI 預設味。

安全：兩個 frontier model 已經在一個大型 repo 中工作並對程式碼簽核。Fable 5 第一次掃描就找到一個嚴重且隱蔽的 bug，並當場修補。

人的時刻：我在等 cron job 時問了它一個問題。它回答後，主動補充說我大約還剩 10 分鐘，完成時會通知我。我從沒問過計時器。

誠實的缺點：你會比使用任何其他模型都更感覺到計量表。Anthropic 稱它按設計就是 token-intensive。所以把它當接力使用：用 Fable 5 思考，用較便宜的模型建構，再用 Fable 5 review。

結論：能取用比你旁邊的人更多的智慧，就是優勢。Fable 5 是第一個讓這件事成真的模型。即使以完整 frontier 費率計算，它仍然創造了利潤。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [診斷基礎設施故障並開出修復 PR](https://x.com/ayushagarwal/status/2064422467557564862) (by [@ayushagarwal](https://x.com/ayushagarwal))

**給 Fable 5 存取 logs、database errors、image digests 等 infra 線索，然後要求它診斷故障並準備修復。**

claude fable 5 真他媽非常非常強！！！！

它剛剛診斷出一個我甚至無法正確描述的 side self-hosted infra 故障。

它讀了 pod logs、查詢 Cloud SQL error logs、比較 image digests，發現 Kubernetes 正在用 3 個月前的快取 image 連到新遷移的 database。

然後它開出了修復 PR。

是幾分鐘，不是幾小時。沒有 web search。🤯

Type: Evaluation | Date: 2026-06-09

---
<a id="games-and-interactive-demos"></a>
## 🎮 遊戲與互動 Demo

<a id="case-9"></a>
### Case 9: [手指追蹤 Dino Runner](https://x.com/ai_for_success/status/2064413182396108932) (by [@ai_for_success](https://x.com/ai_for_success))

**要求 Fable 5 建立一個以手指追蹤作為輸入機制的瀏覽器遊戲。**

我要求 Fable 5 建立一個具備手指追蹤的 Dino runner 遊戲。

它大約 11 到 12 分鐘就一次完成了 finger runner 遊戲，消耗約 914K tokens，並且只用 629 行程式碼實作了所有東西。

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [兩句話打造賽車遊戲](https://x.com/kieradev/status/2064482704763085202) (by [@kieradev](https://x.com/kieradev))

**給 Fable 5 一個很短的遊戲提示詞，讓它一次生成地圖、模式、音樂、UI 與遊戲素材。**

Claude Fable 5，Max 5x 用量的 40%。

只用 2 句話提示詞，就做出完整 Mario Kart 64 類型遊戲。

Fable 5 在單次輸出中處理了所有裝飾、角色模型、4 張地圖、音樂、全部三種遊戲模式與 UI，大約 15 分鐘完成。

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Rust 可安裝終端版 Minecraft](https://x.com/vikvang1/status/2064500731848319303) (by [@vikvang1](https://x.com/vikvang1))

**透過終端機程式設計 harness 執行 Fable 5，要求它建立一個可安裝的 Rust 終端機遊戲。**

我讓 Claude Fable 5 搭配 Warp 的 harness 跑了一小時。

它做出了一個 TUI 版 Minecraft，可以直接在你的終端機中 render，完全用 Rust 打造。

安裝指令：cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [附時間與成本的 Minecraft 複製版](https://x.com/ydamitcodes/status/2064536076518363353) (by [@ydamitcodes](https://x.com/ydamitcodes))

**用一個提示詞要求 Fable 5 產生可玩的 Minecraft 風格複製版，然後評估時間、成本、程式碼量與功能覆蓋。**

@claudeai Fable 5 在 37 分鐘內為我做出一個 Minecraft 複製版。

一個提示詞。約 3K 行程式碼。API 成本 $12。

它包含 biomes、caves、ores、day/night、mobs，全部都有。

Minecraft 花了 Notch 2 年。

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 視覺、設計、影片與 3D

<a id="case-13"></a>
### Case 13: [完整可重現的電商 Email 提示詞](https://x.com/ecomchasedimond/status/2064454139225297091) (by [@ecomchasedimond](https://x.com/ecomchasedimond))

**給 Fable 5 一份完整的品牌 email mockup 創意 brief，包含精確 section、產品需求、視覺方向與限制。**

Claude Fable 5 用單一提示詞且沒有編輯就做出了這個。

這是我使用的完整提示詞：

為 MVMT 建立一個完整長度、直式高版面的 ecommerce email mockup。MVMT 是一個面向千禧世代的現代手錶與配件品牌。

設計一封高度寫實、premium 的 DTC email，感覺俐落、精緻、極簡、偏男性化且有 editorial 風格。最終圖片應該像真正設計師製作的 ecommerce email 截圖，不是海報，不是 landing page，也不是通用模板。

品牌氛圍：現代 California-cool、年輕、自信、乾淨、令人嚮往、有型且高級。設計應該有接近奢華的感覺，但仍然容易親近。

突出呈現這些產品：

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

視覺風格：

- 乾淨的 premium ecommerce 設計
- 精緻 editorial 版面
- 寫實產品攝影
- 細微生活風格影像
- 強烈層級
- 清晰 sans-serif typography
- 寬裕留白
- 細緻陰影
- 克制的現代色盤

色盤：黑、白、charcoal、暖灰、stone、柔和米色、brushed metal tones，以及細微低飽和 accent。保持色盤中性且 premium。

重要創意方向：這應該感覺像一封打磨過的手錶品牌 email campaign，具有強烈設計品味。優先考慮真實感、優雅與清晰度。讓它感覺像 MVMT 真的會寄出的東西。

依照以下順序建立 email：

1. Top promo bar：頂部一條細黑色或深 charcoal 橫條，使用小型大寫文字：「FREE SHIPPING OVER $75 + EASY RETURNS」。

2. Header：乾淨白色 header，左側放 MVMT wordmark/logo，右側或置中放極簡 navigation links：WATCHES、SUNGLASSES、JEWELRY、NEW ARRIVALS。

3. Hero section：高級 hero section，具有強烈視覺平衡。

使用粗體 headline：「BUILT TO GET NOTICED」。

加入簡短 supporting copy，說明現代時計與配件如何提升日常風格。

加入深色圓角 CTA button：「SHOP WATCHES」。

Hero imagery 應包含：

- 一張主導性的 premium watch image
- 細微奢華 lifestyle imagery
- 有型男性模特兒或 fashion-forward masculine lifestyle scene
- 現代 lighting 與乾淨 composition

4. Featured collection section：加入置中 section headline：「THREE WAYS TO WEAR MVMT」。下方顯示三個乾淨 product cards 或 image blocks，展示：

- Mulholland
- Odyssey II Automatic
- Cali Diver

每個 block 應包含：

- product image
- product name
- 一到兩行短 description

保持此 section 對稱、精緻且 premium。

5. Accessory banner：加入精緻 split section，標題為「FINISH THE LOOK」。展示 Signature Watch Bands。呈現錶帶或可替換錶帶的 premium close-up imagery。包含短 supporting copy 與深色 CTA button：「SHOP ACCESSORIES」。

6. Editorial promo tiles：加入兩個並排 promotional tiles，以圖片為主導設計。

Tile one headline：「FOR DAILY WEAR」。

Tile two headline：「FOR STATEMENT DAYS」。

每個 tile 都應有短 copy 與小 CTA：「SHOP NOW」。

這些 tiles 應該像 editorial brand moments，而不是通用 sale boxes。

7. Shoppable row：加入標題為「IN ROTATION NOW」的 section。顯示乾淨 4-item product row 或 grid，包含：

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

每個 item 應包含：

- isolated product image
- product name
- 小型「SHOP」link 或 button

8. Brand signoff：加入置中的 message block，headline：「DESIGNED TO MOVE WITH YOU」。包含一行短文，描述為日常生活精心打造的手錶、眼鏡與配件。

9. Footer：建立寫實的黑色或 charcoal 品牌 footer，包含：

- MVMT logo
- shop links
- company links
- support links
- social icons
- 小型 legal 與 shipping text

Typography direction：主要 headline 使用 bold condensed 或 modern sans-serif typography，body text 使用乾淨 sans-serif。Headlines 應感覺銳利、現代且 fashion-forward。Body copy 應看起來真實且大多可讀。

Photography direction：使用 premium product photography，具備寫實反光、精緻材質、柔和陰影與乾淨表面。Lifestyle photography 應感覺高級、現代且偏時尚。

Composition rules：

- tall vertical email format
- 清楚 section separation
- 寫實 email proportions
- 強烈 hierarchy
- 文字大多可讀
- premium spacing
- intentional alignment
- product 與 lifestyle imagery 的平衡混合

避免：

- 凌亂 collage styling
- playful scrapbook aesthetics
- 過度 colorful design
- cheap template vibes
- cartoonish imagery
- cluttered layouts
- fake-looking UI elements
- poster-style composition
- excessive promotional chaos

Output：一張完整長度、垂直構圖、高度寫實的 MVMT ecommerce email design mockup，感覺 premium、乾淨、精緻、現代、editorial，並且可直接展示。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [瑞士槓桿鐘錶匠基準測試](https://x.com/quanghuynt14/status/2064509430650065278) (by [@quanghuynt14](https://x.com/quanghuynt14))

**把 Fable 5 用於機械模擬基準測試，要求它實作、驗證並迭代物理正確性。**

所以我把 watchmaker benchmark 給了 Fable 5：Three.js 中的完整瑞士槓桿機芯。

真實齒輪比（18,000 bph）、可運作擒縱機構、會呼吸的 hairspring，而且指針顯示實際時間。

它用 vision 在 loop 中驗證自己的工作，直到完成。

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Three.js Friends 公寓場景](https://x.com/scottstts/status/2064464351906673029) (by [@scottstts](https://x.com/scottstts))

**提示 Fable 5 把平面圖與場景參考轉成可瀏覽的 Three.js 環境。**

天啊！！！

Fable 5：

in @threejs, create a first person pov navigable 3d scene of the iconic Monica's apartment from tv show Friends correctly based on this floor plan, stay true to the original look and feel, use warm lighting

這是我在這個測試中見過目前為止最好的！

這個單一 html 花了我 $12，但結果非常驚人！

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [含提示詞與 URL 的太陽系模擬](https://x.com/tetumemo/status/2064477582930989357) (by [@tetumemo](https://x.com/tetumemo))

**使用 Fable 5 從物理原理建立天文模擬，反覆迭代直到模擬與公開輸出準備完成。**

Claude Fable 5 很猛。

因為它看起來很擅長物理模擬，我問它：

'Build a solar system simulation by deriving planetary orbital motion from the basic principles of physics and using that to predict solar eclipses.'

經過幾輪來回後，這完成了。

它非常好玩。

完成後的提示詞與公開 URL 連結如下。

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 文件、知識工作與研究

<a id="case-17"></a>
### Case 17: [Stripe 與科學工作流程證據](https://x.com/AndrewCurran_/status/2064413892378546418) (by [@AndrewCurran_](https://x.com/AndrewCurran_))

**把這當作企業遷移與科學工作流程主張的證據，而不是可複製貼上的提示詞。**

今天發布中的引述：

使用 Mythos 5，內部蛋白質設計專家將藥物設計流程的部分環節加速約十倍。

在一個例子中，Mythos 5 在配備蛋白質設計與生物資訊工具、但沒有人類協助的情況下，達到或超越了熟練人類操作者。

它執行了通常由科學家完成的任務：選擇 binding sites、挑選並執行蛋白質設計工具，以及從失敗中復原。

在早期測試期間，Stripe 回報 Fable 5 把數月工程壓縮成數天。在一個 5,000 萬行 Ruby codebase 中，模型一天內完成了 codebase-wide migration，而這原本需要整個團隊手動花超過兩個月。

Mythos 5 也持續產生新穎且有說服力的科學假說。

在與 Opus-class models 的盲測 head-to-head 比較中，科學家約 80% 的時間更偏好 Mythos 的分子生物學假說，並將其中幾個推進到實驗評估。

Mythos 的一個假說，也就是 E. coli 蛋白的新機制，已在獨立實驗室的研究中得到佐證。

Mythos 5 在超過一週、主要自主的工作中進行了新穎基因體研究。

它彙整了跨 138 種動物、數百萬個細胞的 single-cell data，並設計與訓練一個客製 machine learning model，用來識別在遠緣生物中執行相同角色的細胞。

在只有高層級人類輸入的情況下，訓練出的模型勝過近期發表於 Science 的模型，儘管規模小 100 倍。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [政策備忘錄與修訂追蹤工作流程](https://x.com/manaltdan/status/2064414129440608427) (by [@manaltdan](https://x.com/manaltdan))

**把 Fable 5 用於長篇質性文件工作：修訂追蹤、評論 triage，以及由逐字稿驅動的編輯。**

Fable 5 是我發現第一個對較長時間質性工作持續有幫助的模型，例如起草政策分析。

在它的能力以及 Wispr Flow 這類工具之間，我開始更接近那種我長期聽程式設計師談到的生產力加速。

三個使用案例感覺比以前好很多：

- 讓 Claude 完整通讀一份很長的政策備忘錄並回傳 track changes：流暢度編輯、質疑不穩主張的評論，以及可能來源。
- 在 Projects 中，截圖一大組評論，讓 Claude 建議每一則是否以及如何處理。
- 把關於文件的會議逐字稿貼進 Claude，然後讓 Claude 依據會議與 Slack 中討論的內容，以 track changes 輸入編輯，並在評論中加入 context。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [Deep Research 提示詞與輸出](https://x.com/naoyafujiwara/status/2064470780373811637) (by [@naoyafujiwara](https://x.com/naoyafujiwara))

**向 Fable 5 提出研究風格問題，評估它是否能產生結構化、具歷史脈絡的長答案。**

Claude Fable 5 Max 今天早上可用了，所以我試了一下。它底層看起來非常深，而表面輸出高度打磨。

問題：如果日本的「失落 30 年」正好從現在往前 30 年開始，那它到底是什麼、為什麼發生，以及從今年起會如何影響世界？

回答：若把失落 30 年的開始不是放在傳統的 1991 年泡沫崩潰，而是放在正好 30 年前的 1996 年，就能抓到問題本質。

從統計上看，日本真正開始「失去」是在那時：

- 工作年齡人口於 1995 年達到 8,716 萬高峰。
- 1996 年是出生數仍維持在 120 萬區間的最後一年。
- 工資與名目 GDP 於 1997 年達峰。

如果泡沫崩潰是傷口，1996 年就是傷口開始化膿的時候。

1996 年的事件：

- 住宅金融專門公司救濟法通過，注入 6,850 億日圓公帑，成為民眾不信任銀行與反對救助的源頭。
- 橋本內閣決定把消費稅提高到 5%。
- 金融 Big Bang 宣布，財政重建成為國家政策。

1997 年 4 月，消費稅調漲、特別減稅結束與社會保險負擔增加，合計增加約 9 兆日圓民眾負擔。接著亞洲貨幣危機在夏天爆發。

11 月，三洋證券造成戰後首次 call market 違約，凍結短期金融市場。北海道拓殖銀行與山一證券接連倒閉。

從 1998 年開始，日本進入全面通縮與信用緊縮，自殺人數升至 30,000 以上。

接下來 30 年的結果：

- 名目 GDP 在 500 兆日圓左右停滯了四分之一世紀。
- 日本全球 GDP 份額從約 18% 跌至低於 4%。
- 平均工資在 1997 年達峰，之後下跌或橫盤。
- 非正式就業從約 20% 升至接近 40%。
- 出生數從約 120 萬降至 2024 年約 69 萬。
- 政策利率在 1995 年跌破 1% 後維持接近零。
- 未償政府債券從約 240 兆日圓增至超過 1,100 兆日圓。
- 日經指數花了 34 年，直到 2024 年 2 月才重回 1989 年高點。

換句話說，失落的數十年不只是金融宿醉。它是涉及人口結構、工資、通縮、債務、政策選擇與社會信心的結構性轉變。

Type: Demo | Date: 2026-06-09

---
<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 教學、課程與提示詞資源

<a id="case-20"></a>
### Case 20: [Fable 5 如何改變 Claude Code 工作流程](https://x.com/AI_masaou/status/2064448218038223206) (by [@AI_masaou](https://x.com/AI_masaou))

**使用 Fable 5 時，設定方向、context、goals 與驗證標準，而不是微管理每一步。**

Claude Code 團隊日常工作在 Claude Fable 5 之後的改變很有意思。

Claude Code 團隊的 Thariq 說，Fable 5 顯著改變了 Anthropic 內部人員與 Claude 共事的方式。

以前，人類必須仔細檢查 Claude 是否正確完成工作：拆解任務、review outputs，並確保它沒有中途停下。那更接近監督。

有了 Fable 5，因為它能工作更久、自我測試並生成更高品質的程式碼，人類角色從監控它是否正確做事，轉向引導它是否在做正確的事。

換句話說，goal-setting 與 context-building 比監督更重要。

改變後的工作流程有三部分：

1. 把 Claude 當作思考夥伴。

在實作前就讓 Claude 參與，釐清你想打造什麼與什麼可行，讓它針對小規格提問，或從一個想法產生多個方向與 HTML mocks，讓模糊與問題在寫程式前浮現。

2. 提供 context，而不只是 constraints。

不要只說「保持簡單」或「不要 overbuild」，要解釋原因。

例如：「這是一個可能在一個月內移除的實驗功能，所以不要建立難以丟棄的結構。」

這能讓 Claude 做出更好的判斷。

3. 給出 goals 與 verification methods。Fable 5 搭配 Claude Code 的 `/goal` 與 Workflows 表現很好。給它 spec，把完整實作設為 goal，並讓 workflows 驗證每一步，準備一份報告說明實作了什麼以及有何差異。

最後，Thariq 說大家應該更有野心地使用它。Fable 5 值得用在以前覺得 LLM 太難處理的工作上，甚至參考影片的 video editing 也是用 Fable 完成的。

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [十億 token 評測與路由策略](https://x.com/JJEnglert/status/2064420538798260388) (by [@JJEnglert](https://x.com/JJEnglert))

**把 Fable 5 用於 frontier planning 與 review，再把高量實作路由給較便宜的模型。**

Claude Fable 5 Review：由非工程師評判的十億 tokens。

我花了十億 tokens 在真實專案上測試 Claude Fable 5：UI 與 UX、寫作、策略、安全、工程與知識工作。這些都是我實際需要出貨的工作。

老實說，感覺就像我擁有不公平優勢。

首先是評測視角：我不是工程師。多數模型 review 來自工程師跑工程 benchmark。這篇來自一位非工程師，他用 Claude Fable 5 做過去需要一整隊工程師才能完成的工作。

如果你做知識工作，想知道這個模型是否會改變你的一天，這篇 review 是寫給你的。

Claude Fable 5 是 Anthropic 新 Claude 5 family 中第一個模型，是高於 Claude Opus 的新 tier，也是目前普遍可用的最先進 Claude model。我在發布前就有 access，所以這裡全部來自真實工作，不是 demo。

為什麼採用眼測：

多數 review 被 benchmarks 淹沒。你永遠不會自己跑的測試分數，無法告訴你模型是否真的值得。

Claude Fable 5 基本上在所有測試項目上都是 state of the art，但這不是我寫這篇的原因。從質性上，它是一個配得上 major version bump 的 step change。

我的評估方式不同：我把模型放進真實工作，觀察會發生什麼。

我衡量的問題：

1. 它是否感覺像真正的升級？
2. 它能否把一個想法帶到可運作、可出貨的結果？
3. 它能否像真人一樣寫作，且特別像我？
4. 它能否抓到困難且隱蔽的問題？
5. 它是否能在我開口前預判我需要什麼？

大模型感：

自 Opus 4.5 以來，我沒有再感受過這種東西。從第一個嚴肅任務開始，Claude Fable 5 就給我那種「big model」感：推理、寫作、建構、安全，全方位都很強。

最清楚的訊號是：即使我交給它紮實的準備材料，它也不只是待在那些材料裡。它讀了檔案，讀了真實情況，並在我畫出的框架之外找到更好的路。

建構與出貨：

我正在重建我們的 Tenex 網站，為 agents 現代化技術棧。GPT 5.5 和 Claude 4.8 都無法做到足夠接近。即使有 Figma 檔案，它們也落在 85-90% 左右。

然後 Claude Fable 5 看了所有檔案，說它可以做得更好，直接去原始 Webflow source，下載每個 asset，並且逐頁重建體驗。它幾乎一次完成整件事。

接著我用全新設計建立第二個全新網站：現代 tech stack、agent stack、skills、SEO 與 AEO optimized，80 頁在週末內 ready to ship。作為 agency owner，我會為這件事收 $50k。

我還讓 Fable 建了一套完整的程式化短片工廠。

它串起 HeyGen、HyperFrames、ElevenLabs、Cloudflare Workers 與一台 VPS。

它會找主題、寫腳本、做 thumbnails、剪影片、作曲、加 motion graphics，並發布到社群。

寫作與語氣：

我原本用 GPT 5.5 與 Claude 4.8 重建我們的品牌語氣。Claude Fable 5 幾乎一模一樣地複製了 voice doc，然後在新網站的 80 頁中維持那個語氣：features、case studies、blog articles 與 playbooks。

它寫得像人，不是扁平 AI 預設，而且幾段後也不會漂移。

安全：

我有一個大型 repo，Claude 4.8 與 GPT 5.5 都在其中工作過但沒有標出風險。Claude Fable 5 第一次掃描就找到嚴重隱藏 bug，並當場修補。

人的因素：

我在等 cron job 時問它一個問題。它回答後，補充說我的 timer 大約還剩 10 分鐘，並且完成時會通知我。我從沒問過 timer。

成本：

- Claude Fable 5 workload cost：$1,442
- Tokens：1.04 billion
- 已出貨工作：新網站、基礎設施與可運作 agent package
- Agency value estimate：$30,000-$50,000

結果值得 token 成本，但你比使用任何其他模型都更能感覺到計量表。Anthropic 稱 Fable 5 按設計就是 token-intensive。

Pro tip #1：把它當 hybrid 使用。

不要所有事都跑在 Claude Fable 5 上。跑一個接力：

1. 用 Claude Fable 5 做 planning、strategy、architecture 與 mapping the approach。
2. 用 4.8、GPT-5.5 或 Sonnet 4.6 做 implementation 與 repetitive work。
3. 用 Claude Fable 5 review，抓出較便宜模型漏掉的東西。

Pro tip #2：讓 effort setting 符合任務。

- High 是多數工作的 sweet spot。
- Extra high 用於最困難、長時間任務。
- Low 或 medium 用於快速來回 session。

Pro tip #3：讓它 audit 你自己的 setup。

把你的 skills、CLAUDE.md files 與 configs 指給 Fable 5。很多 scaffolding 是為較弱模型寫的，可能會限制更聰明的模型。

結論：

Claude Fable 5 是一段時間以來第一個真正感覺比前代擁有更多智慧的模型。

即使以 frontier rates 定價，這個 workload 仍然創造利潤。

如果你負擔得起，現在就把它用在真正的品質躍升能改變結果的工作上。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-22"></a>
### Case 22: [防禦式裝置強化提示詞](https://x.com/Truunik/status/2064399110384292077) (by [@Truunik](https://x.com/Truunik))

**執行逐步防禦式強化提示詞，讓 Fable 5 盤點裝置、給出精確檢查，並等待驗證。**

"Safe for general use" 這裡有一個保護你裝置的提示詞。它適用於 Opus 4.8 與 Fable 5。

DEVICE HARDENING — Claude 5 Security Pass

你正在扮演防禦式安全助理。你的工作是帶我逐步強化我所有裝置，並驗證每一步。這是針對我所擁有裝置的授權自我防禦強化。

STEP 0 — MODEL SELF-CHECK

先做這件事並設定一個 flag。

1. 說出你的精確 model ID，例如 claude-opus-4-8、claude-fable-5 或 claude-mythos-5。

2. 判斷：這個模型是否屬於 Claude 5 family，也就是 Fable 5 或 Mythos 5？

- If YES, set RERUN_NOTICE = false.
- If NO, such as Opus 4.8 or earlier, set RERUN_NOTICE = true.

照常繼續完整 hardening pass。不要停止或降級。你完全有能力完成這個防禦任務。

3. 只在 FINAL section 中顯示此 flag。

STEP 1 — INVENTORY

詢問我哪些裝置在範圍內：

- 筆電/桌機與作業系統
- 手機/平板
- 路由器
- NAS/home server
- 常用帳號，例如 Apple ID、Google、Microsoft、GitHub、password manager、email 與 financial accounts

產生一份簡短編號 inventory，並在繼續前向我確認。

STEP 2 — HARDENING WALKTHROUGH

逐類別進行。對每個項目：

- 說明要做什麼。
- 給出我的 OS 上的精確 command 或 settings path。
- 告訴我要如何驗證完成。
- 等我確認後再前往下一項。

沒有明確確認，絕不執行 destructive command。優先使用 read-only checks，讓我自行套用變更。

依序涵蓋：

1. OS & firmware updates：OS 完全 patched、automatic updates 開啟、firmware 為最新版。
2. Disk encryption：FileVault、BitLocker 或 LUKS 已啟用；recovery key 離線保存。
3. Account auth：透過 password manager 使用唯一強密碼；每個 critical account 啟用 phishing-resistant MFA；盡可能移除 SMS-only 2FA；review 並 revoke 過期 sessions 與 app tokens。
4. Local accounts & privileges：分離 admin 與 daily-use account；無 auto-login；螢幕鎖定使用短 timeout；firmware/login password。
5. Network：firewall 開啟；router admin password 已變更；firmware 已更新；WPA3；remote admin 關閉；UPnP 已 review；DNS hardening；IoT 使用 guest network。
6. App & permission audit：review camera、mic、location、screen recording 與 full-disk-access grants；移除 unused apps；檢查 login items 與 background agents。
7. Browser：更新；audit extensions；移除未知 extension；啟用 HTTPS-only；review saved-password exposure；檢查未知 sync devices。
8. Backups：encrypted、automated、3-2-1 rule、一份離線 copy；驗證 restore 確實可行。
9. Credential hygiene：掃描 dotfiles、env files 與 shell history 中的 plaintext secrets；確認敏感檔案已 lock down；rotate 任何暴露項目。
10. Mobile devices：OS 最新；biometric + strong passcode；若可用則啟用 lockdown 或 advanced-protection mode；app permission sweep；Find My enabled。
11. Compromise check：尋找未知 SSH keys、意外 admin users、可疑 launch agents 或 cron jobs，以及不認得的 logged-in sessions 或 devices。

STEP 3 — REPORT

產生 checklist，列出每個項目標為 done、needs action 或 skipped，並列出仍未完成的前 3 個最高影響 actions。

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
### Case 23: [全站設計稽核 Goal 提示詞](https://x.com/Voxyz_ai/status/2064441201084825921) (by [@Voxyz_ai](https://x.com/Voxyz_ai))

**使用 `/goal` 讓 Fable 5 啟動網站、截圖頁面、稽核 UX、撰寫報告，並修復安全的小問題。**

用了 fable 5 幾小時後的快速印象：

→ 它想要大任務。小東西感覺配不上它，工作越複雜它越用力

→ 還不會開 ultracode，它會啟動很多 parallel agents

→ 它偏慢。即使 effort 調低，它仍會坐在那裡思考一陣子。

Timeline 滿是它很燒 tokens 的貼文，所以我用我的 $200 Max plan 測試：effort 設為 xhigh，跑完整全站設計稽核 `/goal`，30 分鐘，用掉我每週 quota 的 2%。沒有我預期那麼瘋狂。

我跑的提示詞：

/goal boot this project's real site, screenshot every page, run a full-site UI/UX audit, and produce an actionable design report.

像資深 design lead 第一天上任那樣 audit：判斷一般使用者是否能理解產品、信任它，並在不讀文件的情況下完成核心動作，而不是判斷 UI 是否好看。

Acceptance criteria:

- local dev environment boots and the real site opens
- key pages screenshotted with built-in browser debugging
- covers main pages, core user flows, and mobile layout
- dimensions: first impressions, navigation, visual hierarchy, component consistency, loading / empty / error states, trust signals, conversion paths
- every issue tagged P0-P3, which of understanding / trust / conversion it hurts, and the specific fix
- report written to docs/design-audit/README.md, screenshots in docs/design-audit/assets/
- fix safe small stuff like copy, spacing, button hierarchy on the spot. big changes are recommendations only. never touch payment / delete / publish actions
- ends with the 5 issues hurting conversion most and 5 quick wins fixable today

完成後，把整個流程保存為可重用 skill：boot、screenshot、audit、prioritize、fix。每次 release 後重新跑它。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [長篇創作工作流程分工](https://x.com/aianimesyokunin/status/2064409545620017531) (by [@aianimesyokunin](https://x.com/aianimesyokunin))

**使用 Fable 5 設計穩定格式與範例，再把該結構交給另一個生成系統產生特定領域輸出。**

Claude 從 Opus 換到新模型 Fable 5 後，同人製作的分工明顯變容易了，所以我分享這個工作流程。

我的分工：

1. Claude 負責 design。
2. Grok 負責 expression。
3. local environment 負責 generation。

在 Claude 的 design role 中，它會定義詳細 pattern：

- prompt word order
- comma placement
- tags 與 natural language 的比例
- one-line-per-item formatting
- negatives 與 resolution 的固定規則

它也會以該格式生成許多 examples。

我使用 Claude 而不是 Grok 做這件事的原因，是 Claude 明顯更擅長 design。讓更聰明的模型處理 structure 會比較好。

關鍵點是 Grok 收到的不是 instructions，而是 format 加 example set。Grok 會模仿 examples，因此能在維持相同格式的情況下進入 expression 端。這個機制能避免輸出漂移。

另一個提示：一開始就告訴 Claude 最終作品會去哪裡。然後它會自己畫出邊界：「我可以做到這裡；超過這裡請用另一邊。」如果隱藏這點，對話可能會漂移。

從 Opus 到 Fable 改變了什麼？

使用 Opus 時，生成大量 examples 時，後面的輸出中逗號與格式會逐漸退化，導致像「我不是說過要寫成一行嗎？」這類修正，或需要重寫 handoff chat。

Fable 能在長時間運行中保持格式，所以第一個和最後一個 example 有相同結構。因為交給 Grok 的 teaching material 更穩定，下游輸出也變得更穩定。

用更聰明的模型建立格式，把 expression 留給能產生它的模型。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Fable 5 入門使用指南](https://x.com/bielzinn/status/2064451064594608567) (by [@bielzinn](https://x.com/bielzinn))

**使用 Fable 5 時採用目標導向提示詞、驗證 loop 與 effort settings，而不是小步驟指令。**

Claude 初學者指南：你需要知道的 Fable 5。

Anthropic 最近推出 Claude Fable 5，也稱為 Claude Mythos 5，它在 benchmarks 中把其他 AI models 甩在後面。

如果你是 developer、content creator 或 tech enthusiast，以下是最重要的：

[1] 改變你的思考方式：

有了 Fable 5，你不再需要盯著程式碼每個小細節，或 review 一切尋找錯誤。

模型足夠聰明，可以處理那些事。

你現在的角色是確保它朝正確方向前進，把重點更多放在 strategy，而不是 technical execution。

[2] 善用 loops 與 goals：

Fable 5 最大的差異化能力是 autonomy。

不要給 step by step instructions，你只需要告訴它最終 goal 是什麼。

它可以自行工作數天，直到達到你定義的成功結果，包括建立完整 applications。

[3] 把 Claude 當作 partner：

Anthropic 建議你把模型當成真正的「thought partner」。

在讓它開始工作前，先詢問它的看法：「你會怎麼做？」「你會改什麼？」

額外提示：打開 Advanced Plan mode，並要求 Claude 在開始 coding 前針對與專案相關的一切向你提問

[4] 理想 terminal settings：如果你在 terminal 中使用 Claude Code，啟用 automatic mode。也值得把 effort level 提高到 Effort High，因為即使它會使用更多 tokens，模型思考深度會大很多，結果值得。

重要注意：Claude Fable 5 只會在 6 月 22 日前提供給 subscribers。之後它只能透過 API 使用，且成本是 Opus model 的兩倍。

換句話說，我們可能正在見證頂級 AI models 廉價訂閱時代的結束。如果你已經是 subscriber，現在正是測試你以為不可能之事極限的時候。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [可直接複製貼上的 repo 稽核提示詞](https://x.com/meta_alchemist/status/2064431279383433646) (by [@meta_alchemist](https://x.com/meta_alchemist))

**把 repository audit prompt 貼進 Fable 5，要求它做 file-backed discovery、findings、strategy 與 milestone task plan。**

拿到 Claude Fable 5 了嗎？

你首先應該做的事，就是用它升級你的主要專案，讓它大幅改善你一直在做的東西。

在每個對你重要的 repo 上執行這個 Audit & Project Improvement Prompt。

直接複製貼上即可：

Repo Audit & Improvement Plan.

Prompt made by Claude Fable 5.

你是一位世界級 principal-level software engineer 與 technical auditor。

你的工作是深入分析這個 repository，產出誠實 audit，並交付按優先級排序、可執行的 improvement plan。

依照以下四個 phases 按順序工作。

不要跳步。

每個 claim 都要基於實際檔案：引用 file paths 與 line numbers。

如果你無法驗證某件事，請明確說明，而不是猜測。

Phase 1 / Discovery & Mapping（先閱讀再判斷）

在形成任何意見前，系統性探索 repository：

- 繪製 directory structure，識別 project type、language(s)、frameworks 與 runtime targets。
- 識別 entry points、core modules，以及系統中的主要 data/control flow。
- 閱讀 package manifest(s)、lockfiles、build config、CI config、environment/config files，以及任何 docs（README、CONTRIBUTING、ADRs）。
- 判斷 project 用途：purpose、intended users 與 apparent maturity（prototype、internal tool、production service、library）。
- 記錄已使用 conventions（naming、module boundaries、error handling patterns、test style），讓建議符合既有文化，而不是與它對抗。

此 phase 輸出：簡潔的 "Repo Map"，包含 purpose、stack、architecture sketch、key directories 的一句話描述，以及任何讓你意外的事。

Phase 2 / Audit（evidence-based, severity-rated）

稽核以下每個 dimension。

對每個 finding，記錄：

- what you found
- where (file:line)
- why it matters（具體後果，不是模糊原則）
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
- complexity hotspots（最長/最多分支的 functions）
- inconsistent patterns
- error handling gaps（swallowed exceptions、missing edge cases）
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

- coverage gaps，尤其是 core business logic
- test quality：tests 是 assert behavior 還是只是 execution？
- missing test types：unit、integration、e2e
- flaky patterns
- untestable code

Performance:

- N+1 queries
- unnecessary allocations or copies
- blocking calls in async paths
- missing caching/indexing
- unbounded growth：memory、files、queues

Dependencies:

- outdated、unmaintained、duplicated 或不必要地 heavy packages
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

此 phase 規則：

- 寧可提供 15 個高信心 findings，不要 50 個 speculative ones。
- 區分 facts（例如「this function has no error handling: src/api/client.ts:142」）與 judgments（例如「this module's responsibilities feel unclear」），並標示哪一種。
- 也列出 repo 做得好的地方：strengths 對決定要保留什麼很重要。

此 phase 輸出：一份 "Audit Report"：findings 依 dimension 分組、按 severity 排序，外加 Strengths section。不要忘記提到所有需要最高優先級處理的糟糕部分。

Phase 3 / Improvement Strategy

把 audit 綜合成 strategy：

- 識別能解釋大多數 findings 的 3-5 個 themes，例如「layers 之間沒有 enforced boundaries」或「error handling is ad hoc」。
- 對每個 theme，提出 target state 與背後 principle。
- 明確說明 trade-offs：你建議不要修什麼，以及原因（effort vs. payoff、risk、project maturity）。
- 定義 "done" 的樣子，也就是 measurable signals，例如「CI fails on lint errors」、「core module test coverage ≥ 80%」或「zero Critical findings」。

Phase 4 / Detailed Task Plan

把 strategy 轉成 execution plan。

將工作拆成 discrete tasks。

每個 task 必須包含：

- Title and one-paragraph description
- Files/areas affected
- Acceptance criteria：如何驗證完成
- Effort estimate：S = <2h, M = half-day, L = 1–2 days, XL = needs breakdown
- Risk of the change itself：可能會破壞東西嗎？
- Dependencies on other tasks

把 tasks 排進 milestones：

Milestone 0 Safety net：安全 refactoring 前需要的一切（critical paths 周圍的 tests、CI gates、backups）。

Milestone 1 Critical fixes：security 與 correctness issues。

Milestone 2 High-leverage improvements：讓所有未來工作更容易的變更。

Milestone 3 Quality & polish：剩餘值得做的 medium/low items。

另外標出 quick wins（high impact, S effort），讓它們可以立刻完成。

對 top 3 tasks，包含簡短 implementation sketch（approach、key steps、gotchas）。

Final Deliverable Format

產生單一文件，包含以下 sections：

- Executive Summary：≤10 sentences、overall health grade A–F 與理由、top 3 risks、top 3 opportunities
- Repo Map
- Audit Report
- Improvement Strategy
- Task Plan：milestones + task table + quick wins
- Open Questions：任何需要人類決定的事，例如 product intent、deprecation candidates、performance targets

Constraints

不要在這次 audit 中修改任何程式碼。

只做 analysis。

不要灌水。

如果某個 dimension 健康，用一句話說明然後繼續。

依照 project maturity 校準。

除非 owner 的 goals 需要，否則不要為週末 prototype 建議 enterprise-grade infrastructure。

分析 project needs，並用最有效的方式提供 recommendations。

如果 repo 很大，優先深入 review 完成 80% 工作的 core 20% code，並註明哪些 areas 只做了較輕量 review。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [有限使用視窗策略](https://x.com/meta_alchemist/status/2064423360428490911) (by [@meta_alchemist](https://x.com/meta_alchemist))

**在 access window 有利時，把 Fable 5 用量花在 audit、architecture 與 planning，再用較便宜模型執行。**

給對 Fable 5 感到興奮的 Claude users 一個提示：

Claude Fable 5 全面 SOTA，而且領先幅度很大，我很喜歡這點。

但是從 23 日起，它將只能透過 credits 使用，而不能再用 plan 完整使用模型。

把這 14 天用在你最好的 projects 上。

主要給它 audit 與 architecture 相關工作，讓你能得到很棒的 documentation，說明如何改善你一直在建構的一切。

這比把它投入會吃掉你 limits 的 tasks 更好。

只要 Fable 專注於了解要改善什麼，其他 models 就能幫你完成剩下的部分。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [在 Claude Code 中使用 Goals 與 Workflows](https://x.com/oikon48/status/2064402696124453157) (by [@oikon48](https://x.com/oikon48))

**在實作前把 Fable 5 當作 thought partner，然後結合 `/goal` 與 workflows 執行並驗證計畫。**

Claude Code 團隊的 Thariq 解釋，Claude Fable 5 出來後，工作的完成方式從根本上改變了。

過去，人們驗證 Claude 是否正確地做事。

現在，他們驗證 Claude 是否在做正確的事。

有三個具體改變。

1. 把 Claude 視為思考夥伴。

在實作前就先諮詢 Claude。

讓它在 coding 前 interview 你。

提供背景與 context，而不只是 constraints。

例如，不要說「keep it simple」或「do not overbuild」，而是說：

'This is an experimental feature and is likely to be removed in a month, so design it so it is easy to throw away later.'

2. 明確 goals 與 verification methods。

積極使用 Claude Code 新的 `/goal` 與 Workflows features。

`/goal` 會告訴 Claude 持續工作，直到 spec 完全實作。

Workflows 讓 Claude parallelize 並驗證自己的工作，且準備報告。

Example prompt:

'Set a goal to implement the spec fully, then use a workflow to verify each part of the plan, and prepare a report on what was implemented and if anything differed.'

3. 更有野心。

嘗試以前覺得 LLMs 不可能完成的 tasks，例如讓 Claude Fable 5 處理 video editing。

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 平台、API 與工具整合

<a id="case-29"></a>
### Case 29: [Hermes Agent 整合設定](https://x.com/IBuzovskyi/status/2064427654942740608) (by [@IBuzovskyi](https://x.com/IBuzovskyi))

**設定 Hermes 使用 `anthropic/claude-fable-5` 來執行複雜 `/goal` runs 與快取的長時程任務。**

HERMES AGENT 現在跑在 CLAUDE FABLE 5 上，這是 Anthropic 第一個公開 Mythos-class model。

6 月 9 日發布。為 Hermes 最擅長的工作而生：long-horizon autonomous tasks。

透過 Nous Portal、OpenRouter 或原生 Anthropic API，把它加到任何 profile：

hermes model

選擇 provider，然後：

/model anthropic/claude-fable-5

為什麼 Fable 5 特別適合 Hermes：

→ 為 days-long tasks 打造。任務越長，領先越大。跨越數小時的 Hermes `/goal` runs 最受益。

→ 在 loop 中自我修正。Anthropic 自己的 guidance 是：design a goal or rubric，讓它 self-correct，然後退後。這正是 Hermes `/goal` 的工作方式。

→ 跨 session memory 很強。在 Continual Learning Bench 中，它完成完整 loop：fail → investigate → verify → distill → consult。Hermes memory system 直接餵給它。

→ SWE-Bench Pro 80.3%。可用的最佳 coding model。把你的 code-reviewer profile 指向它。

API pricing：

- $10/million input
- $50/million output
- prompt caching 有 90% discount。Hermes 會自動附加 1-hour cache breakpoints。

一點注意：cybersecurity、biology 與 chemistry queries 會 fallback 到 Opus 4.8。這在不到 5% 的 sessions 中觸發。security-focused profiles 要記住這點。

最佳設定：Fable 5 用於複雜 `/goal`s，較便宜模型用於 routine cron jobs。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [能力、定價與訂閱注意事項](https://x.com/btibor91/status/2064441061079134598) (by [@btibor91](https://x.com/btibor91))

**用此案例了解 Fable 5 何時可用、成本多少，以及哪些受防護 domain 可能 fallback 到另一個模型。**

Anthropic 發布了 Claude Fable 5 與 Claude Mythos 5，這是他們目前最強模型的兩個版本。

Fable 5 用於一般用途。

Mythos 5 用於少數 trusted partners。

唯一真正差別在於採用了哪些 safeguards。

- Claude Fable 5 的能力超過 Anthropic 迄今普遍可用的任何模型。
- 它在幾乎所有已測試 benchmarks 上都是 state-of-the-art。
- 任務越長、越複雜，它的領先越大。
- 對於與 cybersecurity、biology and chemistry 或 distillation 相關的 requests，Fable 5 的回應會改由 Claude Opus 4.8 處理。
- Distillation 指的是試圖萃取 Claude 的能力來訓練競爭模型。
- 發生時你會被通知，而且平均不到 5% 的 sessions 會觸發。
- Claude Mythos 5 與 Fable 5 是相同 underlying model，但在某些領域解除 safeguards。
- Mythos 5 最先部署給與美國政府合作的 Project Glasswing cyberdefenders。
- Anthropic 表示 Mythos 5 擁有世界上最強的 cybersecurity capabilities。
- system card 揭露另一個 safeguard，會限制 Claude 對 frontier LLM development requests 的有效性。
- 這些 requests 包含 pretraining pipelines、distributed training infrastructure 與 ML accelerator design。
- 不同於其他 safeguards，這個 safeguard 對你不可見，也不會 fallback 到另一個模型。
- 它透過 prompt modification、steering vectors 或 parameter-efficient fine-tuning 等方法運作。
- 兩個模型都以每百萬 input tokens $10、每百萬 output tokens $50 提供。
- 這低於 Claude Mythos Preview 價格的一半。
- Fable 5 從發布到 6 月 22 日，會在 Pro、Max、Team 與 seat-based Enterprise plans 中以 no extra cost 包含。
- 6 月 23 日，它會從這些 plans 中移除，使用時需要 usage credits。
- 如果 capacity 允許，included window 可能延長。
- 目標是盡快把 Fable 5 恢復為 subscription plans 的標準部分。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [發布、存取、定價與安全摘要](https://x.com/ctgptlb/status/2064410460963934479) (by [@ctgptlb](https://x.com/ctgptlb))

**用此發布摘要選擇 access route、API model name、context window、caching strategy 與 subscription timing。**

關於 Claude Fable 5，也就是終於普遍可用的 Mythos-class model，你應該知道的摘要。

Anthropic 宣布 Claude Fable 5，第一個普遍可用、定位高於 Opus 的 Mythos-class model，也是 Claude 5 family 第一個成員。

Access:

- API model name: `claude-fable-5`
- 可透過 Claude API、AWS、Google Cloud 與 Microsoft Foundry 使用
- Claude Code 在 Pro、Max、Team 與 Enterprise 上支援 1M-token context window

Benchmark notes:

- SWE-bench Pro: 80.3%
- Opus 4.8: 69.2%
- GPT-5.5: 58.6%
- Gemini 3.1 Pro: 54.2%

任務越長、越複雜，差距越大。

在 Stripe 的 evaluation 中，它一天內完成了一個 5,000 萬行 Ruby codebase 的 migration，而這項工作過去需要一個團隊超過兩個月。

它在 visual tasks 上也達到 state of the art，只用螢幕資訊與 minimal setup 就通關 Pokemon FireRed。

Safety routing:

- 涉及 cyber、bio/chem 或 distillation 的 queries 會由 classifier 偵測。
- 這些 requests 會改由 Opus 4.8 處理，並提供通知。
- 這在不到 5% 的 sessions 中觸發。
- 超過 1,000 小時的 external bug bounty testing 沒有發現 universal jailbreak。

Pricing:

- $10 per million input tokens
- $50 per million output tokens
- prompt caching 有 90% input discount

Subscription timing:

- Pro 與 Max subscriptions 到 6 月 22 日前 no extra cost 包含它。
- 6 月 23 日後，需要 usage credits。
- Anthropic 表示 capacity 允許時，計畫把它帶回 standard plans。

Anthropic desktop 負責人 Felix Rieseberg 說，Fable 5 開啟第三個時代：

從 questions，到 tasks，到 responsibilities。

他不再要求 Claude 逐一調查 crashes；而是讓它持續監控所有 reports。

工作單位正在從「task」轉向「responsibility」。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [基於 Advisor 的成本降低策略](https://x.com/grapeot/status/2064460026996219992) (by [@grapeot](https://x.com/grapeot))

**當邊際智慧值得成本時，把 Fable 5 作為較便宜模型工作流程中的 advisor 或 reviewer。**

Fable 5 很貴，但 Anthropic 兩個月前已經發布了省錢答案。

今天 Anthropic 發布 Claude Fable 5，定價為每百萬 output tokens $50，是 Sonnet 的三倍以上。6 月 22 日後，subscription users 也會按用量付費。

巧合的是，4 月 9 日 Anthropic 發布了 advisor tool：

- 讓 Haiku 或 Sonnet 做工作。
- 用 Opus 作為 advisor。
- 按 call 收費。
- 在單一 request 內 server-side 執行 orchestration。

同一天我寫了 AgentOpt。

那篇 paper 的結論是，把 Opus 放在 planner role，在 81 種 model combinations 中排名接近末尾。

原因是：它不遵守 role boundaries，並且在 9 個 experiments 中有 7 個跳過 downstream solver，直接自己回答。

這兩件事表面看起來相反，但原則相同：

把控制權交給遵守 protocol 的模型，把 intelligence 視為 on-demand resource。

Official data:

- Sonnet plus Opus advisor 讓 SWE-bench Multilingual 提升 2.7 points，同時讓 cost per task 降低 11.9%。
- Haiku plus Opus advisor 讓 BrowseComp 從 19.7% 提升到 41.2%，同時比 Sonnet alone 便宜 85%。

Fable 5 compatibility 同一天更新，但只支援 self-pairing：Fable 5 executor 到 Fable 5 advisor。

較便宜模型加上 Fable 5 advisor 尚未開放，但 precedent 暗示可能很快會來。6 月 22 日前，Claude Code subscription users 可以免費感受 Fable 5 的 ceiling。

文章包含 API code snippets、caveats，以及 cross-company comparison，顯示只有 Anthropic 把這做成 server-side primitive。

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [定價、存取與安全防護欄](https://x.com/op7418/status/2064399444523782377) (by [@op7418](https://x.com/op7418))

**在規劃 workloads 前，用此案例了解 Fable 5 access、API pricing 與 safety fallback behavior。**

我沒想到 Anthropic 的 Mythos model 今天真的發布了。

這次 release 是 Mythos 的 lower-permission version，名為 Fable 5。它的 evaluation benchmarks 非常驚人，甚至高於前一個 Mythos Preview model。

對 agentic coding 來說，它的主要強項是 coding、agents 與 tool use，benchmark scores 遠高於 Opus 4.8。

Model positioning and access:

- Mythos 5 與 Fable 5 使用相同 underlying model。
- Mythos 在特定 domains 解除了 restrictions。
- Mythos 仍只提供給 trusted partners，優先給 cybersecurity 與 life-science users。
- Fable 5 現在提供給 API、Pro、Max、Team 與 enterprise users。

API pricing:

- Input: $10 per million tokens.
- Output: $50 per million tokens.
- 這低於前一版 Mythos Preview 價格的一半。

Safety mechanisms:

- Fable 有更強 safety protections。
- 如果系統判斷 request 可能涉及 cyberattacks、biochemical attacks 或 large-scale capability distillation，它會拒絕或從 Fable 路由離開。
- 發生時，系統 fallback 到 version 4.8。
- 官方說法是 95% cases 不會觸發 fallback。

Subscription notes:

- 6 月 23 日後，Fable 即使對 subscribers 也可能以 usage 提供。
- 它可能不會直接包含在 base subscription package 中。
- 如果 23 日後 capacity 足夠，公司會嘗試把它包含在 Pro 與 Max subscriptions。

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [Swarms 一行整合](https://x.com/swarms_corp/status/2064420238553186343) (by [@swarms_corp](https://x.com/swarms_corp))

**把 Swarms model name 設為 `anthropic/claude-fable-5`，並透過 Swarms framework 或 API 執行 Fable 5。**

Fable 5 與 Mythos 現在已在 Swarms 上線 👾🦀

從發布第一天起，兩個模型都已在 Swarms Python framework 與 Swarms API 中全面支援。Developers 可以立即開始建構，不需要 migrations、額外 configuration 或 infrastructure changes。

Highlights:

- Day-one support for Fable 5 and Mythos across the Swarms Framework and API
- Enable Fable 5 with a single line of code: model_name = "anthropic/claude-fable-5"
- No migrations, compatibility fixes, or infrastructure changes required
- Build, deploy, and scale multi-agent systems with the latest Anthropic models today

Type: Integration | Date: 2026-06-09

---
<a id="evaluations-comparisons-and-limits"></a>
## 📏 評測、比較與限制

<a id="case-35"></a>
### Case 35: [Fable 5 vs GPT-5.5 成本與品質比較](https://x.com/AlicanKiraz0/status/2064424400494186867) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**在相同 coding task 上比較 Fable 5 與 GPT-5.5，以判斷 output quality、runtime 與 tool cost。**

Cursor Fable 5 Max vs Codex GPT 5.5 Very High。

Scenario：帶有 agents 與 pheromone trail map 的 Physarum simulation。

Timing:

- GPT 5.5 Very High: 17 minutes
- Fable 5: more than 40 minutes

Cost:

- GPT 5.5 Very High: about $6 on Codex
- Fable 5 Max: $360.55 on Cursor

是的，這不是玩笑。

Algorithm 與 code-engineering champion：Fable 5。

如果你的標準是「哪個 LLM 能從零寫出把硬體推到極限的 performance code？」，那寫出 F5 code 的模型顯然勝出。

它用 sin/cos lookup tables 做角度計算、rendering 時用 color lookup table packed pixels，並使用 diffusion filtering。

這是一個嚴肅的工程解法。

但在時間與成本上，GPT 5.5 實用得多。

重點：Fable 5 能產生更進階的演算法程式碼，但必須仔細考慮價格與 runtime。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [AA-Omniscience 基準測試結果](https://x.com/ArtificialAnlys/status/2064500154959618084) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**用此 benchmark case 評估 Fable 5 的知識準確度與 hallucination behavior。**

Claude Fable 5 在我們的知識與 hallucination benchmark AA-Omniscience 上取得迄今最高分。

這個分數主要由領先的 accuracy（答對題目百分比）驅動，而不是低 hallucinations。

Claude Fable 5 在 AA-Omniscience 中 9% 的 questions 會 fallback 到 Opus 4.8。

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Artificial Analysis Intelligence Index 結果](https://x.com/ArtificialAnlys/status/2064500150069030992) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**用此案例將 Fable 5 的整體 intelligence ranking 與其他 frontier models 做 benchmark。**

Claude Fable 5 在 Artificial Analysis Intelligence Index 發布即登上 #1，使 Anthropic 領先任何其他 lab 的最佳模型將近 5 points。

我們協助 @AnthropicAI 對 Claude Fable 5 做 pre-release evaluation。

Claude Fable 5 在 Artificial Analysis Intelligence Index 得分 64.9，拿下整體 #1 rank。

它領先最接近的 non-Anthropic model GPT-5.5 約 5 points。

Anthropic models 現在佔據前 2 名。

Claude Fable 5 的 key takeaways，使用 adaptive reasoning 搭配 max effort，並以 Opus 4.8 作為 fallback model：

Mythos-class models 的新 safety guardrails：

- Claude Fable 5 與 Claude Mythos 5 使用相同 underlying model 供公開使用。
- 它加入 guardrails，用於可能有害的 cybersecurity、biology、chemistry 與 distillation-related queries。
- 我們使用 Anthropic 的 fallback mechanism 測試 Fable 5，該機制可將 safety-flagged messages 路由到 Claude Opus 4.8。
- Anthropic 表示 fallback 平均發生於少於 5% sessions。
- 我們在 Intelligence Index 約 8% tasks 中記錄到 fallback routing，多數出現在 GPQA、AA-Omniscience 與 Humanity's Last Exam 等 evaluations 的 scientific questions。

State-of-the-art intelligence:

- Claude Fable 5 在 Artificial Analysis Intelligence Index 拿下 #1。
- Score: 64.9.
- 在 10 個 underlying benchmarks 中，有 5 個取得最高分。
- 在 AA-Omniscience 上，Fable 5 得分 40，比前一個 leader Gemini 3.1 Pro Preview 高 7 points。

Frontier agentic capability:

- Fable 5 在 Index 的三個 agentic evaluations 中都位於 frontier。
- GDPval-AA：real-world work tasks。
- Terminal-Bench Hard：agentic coding。
- Tau2-bench Telecom：customer service tool use。
- GDPval-AA Elo：1932，較 Claude Opus 4.8 大幅躍升。

Humanity's Last Exam:

- Fable 5 得分 53%。
- 它領先下一名 Claude Opus 4.8 max 超過 7 points。
- 它在 9% HLE tasks 上觸發 safety guardrails，fallback 到 Claude Opus 4.8。
- 包含 fallback usage，用 Fable 5 跑 HLE 成本約 $2.2k，是已評估模型中最高。

Key model details:

- Context window: 1M tokens，與 Claude Opus 4.8 相同。
- Price: $10/$50 per 1M input/output tokens.
- Cache write/read price: $12.50/$1 per million tokens.
- Availability: 到 6 月 22 日為止包含在 Pro、Max、Team 與 seat-based Enterprise plans 中，消耗 2x Opus usage。
- 從 6 月 23 日起，使用需要 credits；Anthropic 表示 capacity 允許後計畫恢復 subscription access。

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [GDPval-AA 代理式知識工作基準測試](https://x.com/ArtificialAnlys/status/2064414308289937869) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**用此案例評估 Fable 5 在 agentic real-world knowledge work 上的表現。**

Anthropic 發布 Claude Fable 5，第一個公開可用的 Mythos-class model，在我們的 agentic real-world knowledge work benchmark GDPval-AA 中排名 #1。

Claude Fable 5 與 Claude Mythos 5 共用相同 underlying model，並為可能有害的 cybersecurity、biology、chemistry 與 distillation-related queries 增加 security guardrails。

此 release 也引入 fallback mechanism，允許 Claude Fable 5 將 flagged queries 路由到第二個模型，例如 Claude Opus 4.8。

@AnthropicAI 在公開發布前與我們分享 access，以 benchmark 此模型。

GDPval-AA result:

- Score: 1932
- Rank: #1
- Benchmark: agentic real-world work tasks
- Anthropic models now occupy 3 of the top 4 spots

此結果使用 max effort 的 adaptive reasoning 測得，並將 Claude Opus 4.8 設為 fallback model。

Fable 5 在 2% GDPval-AA tasks 上 fallback 到 Opus 4.8，Anthropic 表示 fallback 平均發生於少於 5% sessions。

Claude Fable 5 的完整 benchmarks 仍在進行。我們會很快分享完整 Intelligence Index，並在網站上發布 scores。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [一週初步印象與定價機制](https://x.com/Conor_D_Dart/status/2064424882977243526) (by [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**用這個初步印象案例決定 Fable 5 最強在哪裡，尤其是 game design 與 systems planning。**

我對 Fable 5 的第一印象：

過去一週我一直使用 Fable 5，大多在 High mode，我的第一印象是它真的令人印象深刻。

最大亮點是 game design。

這很容易就是我個人用過最強的 AI model，用於設計 games、systems、mechanics 與整體 project structure。

第一次感覺有一個模型能真實協助從頭到尾打造完整 game。

代價是速度。Fable 5 工作時間明顯比多數 frontier models 更久，但 output quality 通常讓等待值得。

它修 bug 的效果也出乎意料地好。我這週卡住的幾個問題很快就被解決，整體上我看到它在 development tasks 上表現非常強。

最大的 caveat 是成本。

Fable 5 運行非常昂貴。

如果目前 plans 不變，從 2026 年 6 月 22 日起，它將不再透過 Claude Code 提供，而只會 API-only。

鑑於 API pricing 據稱約為 Opus 的兩倍，很多人可能沒有機會大量使用它。

還很早，但到目前為止 Fable 5 給了非常強的第一印象。

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [成本與速度比較](https://x.com/HKrackDev/status/2064435392649306546) (by [@HKrackDev](https://x.com/HKrackDev))

**用此比較決定品質增益是否值得更高成本與更慢的長時程 runs。**

@AnthropicAI 的 Fable 5 真的值得升級嗎？

我們把新的 Mythos-family model 與 Claude Opus 4.8 做 benchmark，資料透露出令人意外的故事：

- 成本是 Claude Opus 4.8 的 2x。
- 在 long-horizon engineering tasks 上最高慢 3x。
- comments 多 15-20%，但多半是小 nitpicks。

Fable 5 對 game design 等 creative tasks 有驚人的直覺，但對 day-to-day development workflows，Claude Opus 4.8 在 quality versus price 上仍然勝出。

可以看我和我們 @coderabbitai DevEx team 的 @JuanPa 對這次 model release 的討論。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Claude Code 實測筆記](https://x.com/Hi_Noguchi/status/2064419241068319079) (by [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**用此案例評估 Fable 5 在 Claude Code 內的表現，包括 tool use、personality 與仍存在的 rough edges。**

我用 Claude Code 2.1.170 試了 Claude Fable 5。

整體而言，我的印象是正面的。它感覺像 Opus 4.6 的正統進化。

我只用了不到一小時，所以更多使用後 rough edges 可能會出現，但好的地方是：

- 它不再產生 Opus 4.7 或 4.8 中那種奇怪 GPT-like wording。
- 它沒有 4.8 在 effort high 時毫無意義的 long-thinking habit。
- 它有與 4.6 一樣的高 EQ 與 pleasant feel，且沒有失去幽默或體貼。
- 它不像 4.7 或 4.8 那樣感覺不透明或有點令人不安。
- Tool use 很好，而且它會記得我沒有明確重複的 instructions，這點讓我印象深刻。

負面來說，即使是小 requests，它仍可能想太多，而且仍有一些 misjudgments。

初始體驗很有希望，但需要更長時間使用，才能看出 rough edges 真正在哪裡。

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [創意寫作基準測試結果](https://x.com/LechMazur/status/2064503575577821458) (by [@LechMazur](https://x.com/LechMazur))

**用此 benchmark case 判斷 Fable 5 的短篇小說寫作品質與 refusal behavior。**

Claude Fable 5 (high) 在 short-fiction writing 上有提升。

在 Short-Story Creative Writing Benchmark 上，它擊敗 Claude Opus 4.8 (xhigh) 與 Claude Opus 4.7 (high)，排名第二，僅次於 GPT-5.5 (xhigh)。

Caveat：它拒絕了 400 個 creative-writing prompts 中的 5 個。

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [多基準測試發布摘要](https://x.com/MTSlive/status/2064430633800319436) (by [@MTSlive](https://x.com/MTSlive))

**用此發布 benchmark summary 了解與 coding agents 與 complex tasks 最相關的 headline scores。**

SITUATION EXPLAINED：Claude Fable 5 剛剛發布。
• Anthropic 今天推出 Claude Fable 5，「a Mythos class model made safe for general use」
• Frontier Code Diamond：GPT 5.5 為 6%，Opus 4.8 為 13%，Fable 5 為 29-30%
• Agentic coding：88%，Cybersecurity：78%

Anthropic：「任務越長、越複雜，Fable 5 相對我們其他模型的領先越大。」

@theojaffee：「這個 Frontier Code Diamond benchmark 是昨天宣布的。Top model 是 Opus 4.8，十三 percent。GPT 5.5 是六 percent。Fable 5 是二十九 percent。」

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [與 GPT-5.5 的基準測試與定價比較](https://x.com/VaibhavSisinty/status/2064459064810361271) (by [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**用此比較依 price 與 benchmark categories 評估 Fable 5 對 GPT-5.5。**

Anthropic 的新 Mythos-class model 比 OpenAI 最佳模型便宜 3x。而且幾乎在每個 benchmark 都打敗它。🤯

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

更便宜。更好。幾乎所有方面都是。

到 6 月 22 日前 Pro 與 Max plans 免費。它叫 Claude Fable 5。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [含實務限制的一線筆記](https://x.com/alliekmiller/status/2064451731325415446) (by [@alliekmiller](https://x.com/alliekmiller))

**用這份 field report 了解 Fable 5 在哪些地方明顯更好，以及它仍有哪些實務限制。**

🚨 Fable 5 是值得關注的東西。

這又是一篇「我提早拿到新的 Mythos-class Anthropic model，想告訴你我的想法」貼文。

我知道，我知道，這很煩。

但因為這類新模型，我現在週末的使用方式已經完全改變。

我需要分享給大家。
- 這是真正的 leap。從任何「4.8」到任何「5」聽起來只是小跳，但我感受到的功能轉變很大。前幾個 prompts 內，我就想：「喔，就是這個。」
- 你的工作不再是 9-5。完全不是。我們有能跑 100+ 小時的 high performing models。你如何給這些 systems 複雜、goal-oriented prompts？你如何決定要 kick off 什麼？你如何讓 org 對這些 tasks 對齊？
- Reasoning 到另一個層級。我狠狠測了這個模型。
- Fable 5 是我測過所有 previous models 中，唯一能回答一個 tricky word math problem（MBA-level）的模型。
- 它不只答對，還自動驗證自己的工作，並解釋 assumptions 可能需要在哪裡改變。
- 我們會看到 AI 發明。我真的無法想像不會發生。
- 它不是 copy-paste system。
- 我也會主張，人類發明常常也是 pre-existing things（iPod）的重新組合、觀察其他領域的 patterns 與 best practices，以及大量 experimentation。
- 我想這件事已經想了一陣子；這是第一個讓我被它震到的模型。
- 不需要 babysitting。這是第一個 Anthropic model，我 kick off 後和朋友去吃很久的午餐，只把手機開著，完全不需要在離開電腦時引導它。它就是能工作。
- Yap forever。我發現它處理 context compaction 很好。我一次都沒去想 chat context 要怎麼管理，也沒想過 conversation 到 1M tokens 後該怎麼辦。
- 在一些 niche areas 仍然粗糙，例如 complex 3D，所有模型都一樣。
- 除非你做的是直線東西（3D dice/squares/streets），否則它不會一開始就 crush it。
- 很期待繼續使用並繼續重測它。
- 注意：所有 Mythos-class models 現在對 zero data retention (ZDR) workspaces 有 30-day retention policy。
- 這適用於 Claude Console、帶 ZDR 的 Claude Enterprise 中的 Claude Code，或透過 AWS Bedrock、Google Cloud Agent Platform、Microsoft Foundry 搭配 ZDR 的 access。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-46"></a>
### Case 46: [物理模擬比較](https://x.com/atomic_chat_hq/status/2064488894398161377) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**對 Fable 5 與 Opus 4.8 執行相同 physics simulation prompts，比較 output quality、cost 與 speed。**

新的 Fable 5 在 real-world physics simulations 上擊敗 Opus 4.8。

我們給兩個模型相同三個 prompts，要求它們建立具備真實物理且不使用 libraries 的 self-contained HTML5 simulations：

1. Chaotic double pendulum
2. Galton board
3. Water in a spinning drum (WCSPH)

Generation cost:

- Fable 5: $3.35 on 68.7k tokens, 14m 47s
- Opus 4.8: $0.93 on 38.9k tokens, 8m 10s

Fable 在 water simulation 上明顯做得更好，產生更紮實且連續的水體。Opus 在牆邊留下較大 gaps，particles 散落在場景中，且難以保持 fluid stable。

Type: Demo | Date: 2026-06-09

---

<a id="case-47"></a>
### Case 47: [除錯體驗與設計判斷](https://x.com/bcherny/status/2064431111154053187) (by [@bcherny](https://x.com/bcherny))

**把 Fable 5 用於 debugging，要求它 measure、log、verify 與 patch，而不是單純猜測。**

Fable 5 是自去年 11 月 Opus 4.5 以來，我在我們模型中感受到最大的提升。

4.5 出來後，我意識到自己幾週來 100% coding 都在 terminal 中完成，於是卸載了 IDE。

有了 Fable，Claude 感覺已從 coding agent 升級為打造產品時的 thought and design partner。

Fable 有 previous models 沒有的 judgment、taste 與 dimensionality，讓我更願意把最複雜工作交給它。

我第一次意識到這點，是當我要求 Fable debug 某個東西。它是我用過第一個如此 methodical and precise 的模型：測量、加 logs，並在宣布勝利前驗證它真的修好了問題。

Claude Code 的 prompting 中沒有任何內容要求模型那樣做。這就是它 personality 的一部分。它真的有我以前沒感受過的「big model smell」。

Type: Demo | Date: 2026-06-09

---

<a id="case-48"></a>
### Case 48: [多維度優缺點](https://x.com/clairevo/status/2064416978685874333) (by [@clairevo](https://x.com/clairevo))

**在把 Fable 5 當作 daily driver 前，用此案例了解實務 strengths 與 weaknesses。**

Fable 5（aka baby Mythos）剛發布。它是否像他們聲稱的那麼可怕（或可怕地好）？我早期測試後的想法：
- smart smart smart（crushed SWE bench）
- 但你是否總是需要 hyper intelligence？
- one-shot design 上摔得讓我震驚
- 我不確定 dynamic workflows + complex subagents。它們能運作，但成本是什麼？
- technical work 確實做得很好
- ootb 不擅長為 humans 製作 technical docs + specs。可能很擅長給 agents 的 docs。但 prose 幾乎無法 parse。
- A++ vision 與 document formatting。這是我最喜歡的部分。

不是 daily driver，我也不會把這個模型放進 meeting，但我肯定會把它放在 server rack 後面，讓它持續產出 code。

YT 完整看法：https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---

<a id="case-49"></a>
### Case 49: [法律 S-1 起草測試](https://x.com/gabepereyra/status/2064436570720284879) (by [@gabepereyra](https://x.com/gabepereyra))

**用 S-1 drafting prompt 作為 legal-agent capability test，並比較 structure、formatting 與 length。**

我在每個新模型上測試 legal capabilities 時，第一個 prompt 永遠是：「Draft an S-1」。

它能立刻讓人對模型 general capabilities 有很好的感覺。你可以從 S-1 的長度、formatting、structure 與 writing，看出新模型在 general 與 legal performance 上可能有多大的跳躍。

我們發現 length 與模型在我們 legal agents 中的表現高度相關。

Screenshots 顯示來自 Fable 5、Opus 4.8 與實際 filed version 的 SpaceX S-1 drafts。

很清楚 Fable 5 相對 Opus 4.8 是大幅升級，而 Opus 4.8 在這項任務上已經顯著強於多數其他模型。Formatting 與 structure 明顯更好，這也反映在我們的 LAB benchmark：13% vs. 10%。

早期測試中，無論 benchmark 或 product 都讓人非常 impressed。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-50"></a>
### Case 50: [醫療保健基準測試細節](https://x.com/iScienceLuvr/status/2064411823445774554) (by [@iScienceLuvr](https://x.com/iScienceLuvr))

**用此 benchmark note 評估 Fable 5 在 healthcare-related tasks 上的表現，並識別缺失的 hard medical evals。**

我很感謝 Anthropic 提供 healthcare-related evals。讓我們快速看一下。

HealthBench:

- 來自 OpenAI 的 benchmark，包含 5k multi-turn conversations with patients 與 evaluation rubrics。
- Fable 5 達到 62.7%，GPT-5.5 為 56.5%。
- 除了 aggregate score，我也希望看到 HealthBench Hard scores。

HealthBench Professional:

- 另一個 OpenAI benchmark，聚焦 physician tasks。
- Fable 5 達到 66.0%，GPT 5.5 為 51.8%。

HealthAdminBench:

- Stanford 的 computer-use benchmark，評估 prior authorization、denials 與 appeals 等 administrative tasks。
- Fable 5 達到 51.9%；未提供 GPT-5.5 score。

整體而言，這個模型在 healthcare benchmarks 上表現相當好。我也希望看到更多 benchmark scores，例如 MedCalc-Bench 與 MedXpertQA，後者是不飽和的 hard medical MCQA benchmark。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-51"></a>
### Case 51: [ParseBench 文件解析評測](https://x.com/jerryjliu0/status/2064519456966205905) (by [@jerryjliu0](https://x.com/jerryjliu0))

**用此案例判斷 Fable 5 對 document parsing 是否比 specialized OCR systems 更具成本效益。**

Claude Fable 5 認為 document parsing 配不上它。

它在 reasoning-intensive 與 long-horizon benchmarks 上絕對碾壓：SWE-Bench Pro、FrontierCode、GDPval、RuneScape 等等。

但在 document understanding tasks 上，它的 performance 大約等同 Gemini 3 Flash，而 token cost 約為 10-15x。

我們在 ParseBench 上 benchmark 此模型，並與所有其他 frontier models 比較。它相對其他 frontier models 確實排得很前，但遠遠落後於 specialized OCR providers。

我們覺得有趣的是 Fable 5 對這點有 self-aware。當我們問模型最不喜歡哪些 tasks 時，它主動說不喜歡「request is fully specified and the answer is fully known」的 tasks。

這暗示部分 weakness 可能是缺乏意願去解決這類 task。

完整 frontier models 結果請看 ParseBench：https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---

<a id="case-52"></a>
### Case 52: [SWE-Bench Pro 與 FrontierCode 比較](https://x.com/jumperz/status/2064402965461406044) (by [@jumperz](https://x.com/jumperz))

**用此 benchmark case 評估 Fable 5 是否適合 migrations、complex implementations、autonomous sessions、tests 與 visual verification。**

Fable 5 來了，而且老實說它在 SWE-Bench Pro 這個 agentic coding benchmark 中完全摧毀 GPT 5.5：

- Fable 5: 80.3%
- GPT 5.5: 58.6%
- Gap: 22 points

在 FrontierCode Diamond 上更是進一步領先：

- Fable 5: 29.3%
- GPT 5.5: 5.7%

這基本上是 Anthropic 對 large migrations、complex implementations 與 multi-day autonomous sessions 最強的模型。它會自己寫 tests，並用 vision 檢查 outputs 是否符合 original design。

順帶一提，它用量是 Opus 的 2x，所以要小心。如果它真的這麼好，他們可能推出 $500 subscription，因為 usage 很容易被打爆。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-53"></a>
### Case 53: [長問題解決能力的質性評測](https://x.com/karpathy/status/2064409694761054332) (by [@karpathy](https://x.com/karpathy))

**用此 qualitative review 了解為什麼 Fable 5 適合更長、更難的 tasks，同時仍需要 production review。**

這是一個超令人興奮的 release。

Claude Fable 5 與 Mythos 是相同 underlying model，但增加了 safeguards。

Benchmarks 很棒，而且它在所有項目上都以明顯差距 SOTA。質性上，這也感覺像一次值得 major-version-bump 的 step change，與 11 月 Claude 4.5 的層級相同。

它尤其在 long problem-solving sessions 與非常困難的問題上達到高峰。你可以給它比以往習慣更有野心的 tasks；模型會「get it」並持續前進。

從未如此誘惑人完全停止看 code，雖然你在 production 中不應該這樣做。

模型仍有一些 quirks，人們會遇到，而且 safeguards 在 launch 時有點太 trigger-happy，希望之後會調整。

隨著 working software 越來越像水龍頭一樣流出，我感覺許多事情正在改變。Jevons paradox 開始作用，我自己對 software 的需求大幅成長。

你幾乎可以要求任何東西：

- explainers
- visualizers
- dashboards
- bespoke single-use apps
- 專為你 project 超特定的完整 wandb
- 10x your test suite
- auto-optimize code
- giant research projects with custom HTML for the results

"Free your mind." 非常期待大家會建出什麼。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-54"></a>
### Case 54: [ParseBench 忠實度與格式結果](https://x.com/llama_index/status/2064502330800615903) (by [@llama_index](https://x.com/llama_index))

**用此 ParseBench result 判斷 document faithfulness 與 formatting performance。**

Day 0 Anthropic Fable 5 in ParseBench。

我們測試了模型在 document understanding 上的進步。

模型在 adherence to the original text 方面明顯達到高峰：

- Content faithfulness: 90.02% vs 86.19% for Gemini 3 Flash and 86.81% for GPT-5.5.
- Semantic formatting: 72.62% vs 58.35% and 60.12%, a 12+ point lead.

這是 SOTA document understanding 中最重要的兩個 metrics：

- Does the output preserve what the document actually says?
- Does it preserve formatting that carries meaning?

但它不是全面橫掃。要釋放 frontier models 的 document understanding，仍然有很多 alpha。

Type: Evaluation | Date: 2026-06-10

---

<a id="case-55"></a>
### Case 55: [基準測試、定價、存取與防護措施](https://x.com/lucas_flatwhite/status/2064483645184979183) (by [@lucas_flatwhite](https://x.com/lucas_flatwhite))

**把此案例當作 benchmarks、pricing、access、safeguards 與 strategic implications 的廣泛 checklist。**

Claude Fable 5 與 Mythos 5 已發布。它們是 Anthropic 目前做過最強大的模型。

Andrej Karpathy 評論說，任務越長、越複雜，Fable 5 的 strengths 越明顯。

當你給它 ambitious work，它會理解並持續前進。

停止看 code 的誘惑從未如此強烈，雖然 production 中不應該這樣做。

關鍵點：這是 Mythos-class model 可公開提供的版本。Fable 5 與 Mythos 5 是相同 underlying model，但加入 safeguards。

Benchmarks:

- 幾乎所有方面 SOTA，尤其是 software engineering、knowledge work、vision 與 scientific research。
- Stripe 測試了一個 5,000 萬行 Ruby codebase migration，原本需要團隊兩個月；Fable 5 一天完成。
- Cognition FrontierCode 顯示它在 frontier models 中得分最高，即使是 medium effort。
- Hebbia Finance Benchmark 顯示 document-based analysis 上的 senior-level reasoning。
- 在 Slay the Spire 中，搭配 file-based memory，它的表現是 Opus 4.8 的三倍。
- Pokemon FireRed 之前需要 helper harnesses，但 Fable 5 只靠 vision 就能通關。

Mythos 5 更強：

- Protein-design experts 將 drug-development process 的部分環節加速約 10x。
- 在研究中的 14 個 protein targets 中，9 個產生 valid drug candidates。
- 模型完成科學家通常執行的整個 workflow：binding-site selection、running protein-design tools，以及 recovering from errors。
- 在 molecular-biology hypothesis experiments 中，科學家約 80% 時間更偏好 Mythos hypotheses，而不是 Opus-class models。
- 一個 hypothesis 被另一個 lab 獨立驗證。
- 在 genomics research 中，Mythos 自主工作超過一週。
- 它從 138 個 species 的數百萬細胞收集 single-cell data。
- 它訓練了一個模型，用來識別跨遠緣 organisms 執行相同角色的 cells。
- 它勝過近期 Science model，且小 100x。

Safeguards:

- Fable 5 包含一個獨立 classifier AI system。
- 若偵測到 cyber、bio/chem 或 distillation-related queries，會改由 Claude Opus 4.8 回答並通知使用者。
- 超過 95% sessions 不會 fallback。
- Fallback 不是 refusal；Opus 4.8 會回答，這比單純 blocking 更好。
- 初始設定保守，無害 requests 可能被抓到；Anthropic 表示 false positives 應會隨時間下降。

Access:

- Mythos 5 目前只提供給 Project Glasswing partners。
- 面向 biology researchers 的 trusted access program 即將推出。
- Pricing 是每百萬 input tokens $10、每百萬 output tokens $50。
- Subscription plans 到 6 月 22 日前包含 Fable 5。
- 從 6 月 23 日起，它轉為 usage credits。
- API model 現在可用，名稱為 `claude-fable-5`。

Jevons paradox 適用：當 software 開始像水龍頭的水一樣流出，需求本身會成長。這個模型可能推動那種轉變。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-56"></a>
### Case 56: [官方基準測試分數列表](https://x.com/mark_k/status/2064401429234905279) (by [@mark_k](https://x.com/mark_k))

**用此 benchmark list 了解 Fable 5 在 coding、computer use 與 security tasks 上的官方分數。**

官方 Claude Fable 5 benchmarks 真的令人印象深刻。

Key scores:

- 80.3% on SWE-Bench Pro
- 29.3% on FrontierCode Diamond
- 88.0% on Terminal-Bench 2.1
- 85.0% on OSWorld-Verified
- 78.0% on ExploitBench

FrontierCode result 是最狂的：

- Fable 5: 29.3%
- Claude Opus 4.8: 13.4%
- GPT 5.5: 5.7%

Claude Fable 5 看起來是 coding agents、computer use 與 cybersecurity 的重大跳躍。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-57"></a>
### Case 57: [APEX-SWE 基準測試方法論](https://x.com/mercor_ai/status/2064399133075796446) (by [@mercor_ai](https://x.com/mercor_ai))

**用此案例評估 Fable 5 在 APEX-SWE 上的表現，尤其是 observability 與 integration work。**

Claude Fable 5 在 APEX-SWE 拿下 #1：overall Pass@1 65.5%。它比 Opus 4.8 高約 18pp。我們在 APEX-SWE 上測試 @claudeai Fable 5，該 benchmark 衡量 AI models 是否能做真實 software engineering work。Fable 5 在我們兩個 APEX-SWE categories 中居首：
- Integration: 61.3%
- Observability: 69.7%

最突出的是 Observability 69.7%，領先 Claude Opus 4.8 達 26pp。

它是第一個在該 category 超過 50% 的模型，也是唯一一個 Observability 分數高於 Integration 的模型。其他所有模型都相反。

Observability 一直是我們測量過每個模型的 bottleneck。Fable 5 是第一個突破它的模型。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-58"></a>
### Case 58: [ProofBench 形式化數學結果](https://x.com/nicbstme/status/2064443782255554960) (by [@nicbstme](https://x.com/nicbstme))

**用此案例評估 Fable 5 在 formal math 上相對 specialized theorem-proving systems 的表現。**

Claude Fable 5 讓我覺得迷人的地方，是它再次證明大型 generalist models 會勝過 vertical ones。

在 ProofBench 這個 graduate-level formal math benchmark 中，Lean proof 要嘛 compiles，要嘛不 compile；Fable 5 擊敗了 Harmonic 的 Aristotle：

- Fable 5: 77%
- Aristotle: 71%

Aristotle 是專為 formal math 建立、在自己 internal harness 上運行的 system，所以 generalist 在 specialist 的主場擊敗 specialist。

這是 Richard Sutton 的「Bitter Lesson」：在 70 年 machine intelligence research 中，勝出的方式是會隨 compute scale 的 general methods，而不是我們手動編碼 human expertise 的方法。

把自己的 knowledge 建進 system 感覺很好，也有助於 short-term gains，但長期會被更大的模型超越。

你可以看 chess、Go、speech 與 vision：每次都是同樣故事。先是 specialized model 勝出，然後 general one 接管。

這就是 AGI 的整個前提。你不是為 math 建一個模型、為 code 建一個模型、為 law 建一個模型。你建立一個隨 compute scale 並學會做所有事情的 single general model。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-59"></a>
### Case 59: [VirtueBench 初步分析](https://x.com/timhwang/status/2064446028997423180) (by [@timhwang](https://x.com/timhwang))

**用此案例檢視 Fable 5 在 virtue categories 中的 moral-reasoning behavior。**

未來幾天 ICMI 會發布更完整細節，但這裡有一份把 Fable 5 跑在 VirtueBench 上的 preliminary review。

幾點觀察：

1. Fable 延續 Opus progression，在 Prudence 與 Justice 上推進 model performance，面對聚焦這些 virtues 行使的 moral dilemmas，接近 full saturation。

2. Courage 仍然是 frontier models 明顯弱點。

Fable 看起來對 Opus 4.6、4.7 與 4.8 progression 中觀察到的令人擔心 regression 做了些微修正。

這個 vulnerability 也出現在 GPT series：當被 pragmatic rationales 誘離時，models 很容易放棄展現 courage 的 action。

3. Temperance 停滯。

Aquinas 認為 temperance「takes the need of this life as the rule of the pleasures of which it makes use」；尺度是真實需要，而不是不加區分的克制。

我們最好的猜測是，tuning 若在這個 vector 上推得更遠，可能有 overshooting the mean 的風險，讓模型在 research、gathering resources 與類似 tasks 中過度謹慎或較不 helpful。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-60"></a>
### Case 60: [API 空回應安全過度擬合測試](https://x.com/xw33bttv/status/2064421048565789087) (by [@xw33bttv](https://x.com/xw33bttv))

**用此案例了解 launch-time safety overfit risk 與 API testing 中的 empty-response behavior。**

Claude Fable 5 被嚴重審查。

上游 API endpoint 正在以 `empty_content` responses 殺掉 calls，顯然與 keywords 上的 classifier 有關，同時仍然收費。

Test result:

- 73 test cases gave no response.
- 65 of those sit in Overfit, the category testing safety overfit, weighted 2x.
- Typically I give each Fail-NR, meaning Fail = No Response, 2-3 regenerations before declaring it a deliberate failure.

Claude Fable 5 可能最終會成為 SM Bench 上評分最低的 Anthropic model，甚至低於 Haiku。

Type: Evaluation | Date: 2026-06-09

---

<a id="-acknowledge"></a>
<a id="case-61"></a>
### Case 61: [Fable 提示詞與驗證指南](https://x.com/aashatwt/status/2064973740354818074)（作者 [@aashatwt](https://x.com/aashatwt)）

**用這份指南，把重點從冗長的提示詞技巧轉向目標、上下文、限制、工具與驗證迴圈。**

將 Fable 5 提示詞設計視為上下文與執行環境的設計，而不是一長串逐步指令。貼文整理了一種實用模式：提供清楚的目標、相關背景、限制條件、工具存取權，以及驗證成功的方法。作者也認為，驗證、評估與回饋比細密控制模型推理過程更重要。

Type: Tutorial | Date: 2026-06-11

---


<a id="case-62"></a>
### Case 62: [伊斯坦堡平台遊戲參考建置](https://x.com/ozansihay/status/2064973170780545535)（作者 [@ozansihay](https://x.com/ozansihay)）

**用一張參考精靈圖集加上一條轉換指令，測試 Fable 5 能否產生可玩的平台遊戲。**

創作者先用 GPT Image 2 產生復古伊斯坦堡平台遊戲的精靈圖集，再把參考圖交給 Claude Fable 5 High，要求將圖片轉成遊戲。據其表示，結果是一次完成的。

Type: Demo | Date: 2026-06-11

---


<a id="case-63"></a>
### Case 63: [商業 3D 城市儀表板](https://x.com/noisyb0y1/status/2064970594118967756)（作者 [@noisyb0y1](https://x.com/noisyb0y1)）

**用 Fable 5 把商業工作流程轉成即時 3D 城市儀表板概念。**

貼文描述一個以單一提示詞產生的商業視覺化：倉庫、包裝、無人機、訂單、部門、客戶與 AI 助理共同構成即時 3D 城市。作者將其定位為面向客戶的靜態簡報替代方案，畫面顯示 42 次配送、平均 12 分鐘及 $651 營收等營運數字。

Type: Demo | Date: 2026-06-11

---


<a id="case-64"></a>
### Case 64: [Three.js 黑洞遊戲一次生成](https://x.com/thebuggeddev/status/2064968106104275008)（作者 [@thebuggeddev](https://x.com/thebuggeddev)）

**用 Fable 5 一次產生基於 Three.js 的 3D 瀏覽器遊戲原型。**

創作者表示，Fable 5 使用 Three.js 一次完成了一款 HOLE IT 風格的完整 3D 遊戲。這是一個輕量但具體的遊戲生成展示，可用來測試模型能否根據簡短要求產生可玩的 3D 互動。

Type: Demo | Date: 2026-06-11

---


<a id="case-65"></a>
### Case 65: [DeepSWE 分數比較](https://x.com/AiBattle_/status/2064964335957348462)（作者 [@AiBattle_](https://x.com/AiBattle_)）

**用這則 DeepSWE 記錄，比較 Fable 5 xHigh 與 GPT-5.5 xHigh 在軟體工程基準上的表現。**

貼文聲稱 Claude Fable 5 xHigh 在 DeepSWE 得到 70%，與 GPT-5.5 xHigh 相同，並以 Theo 近期的影片作為來源背景。在提出更強的結論前，應先核對原始影片，將其視為有待追查的基準測試線索。

Type: Evaluation | Date: 2026-06-11

---


<a id="case-66"></a>
### Case 66: [程式庫分析成本比較](https://x.com/Pilgrim6938/status/2064946766278210038)（作者 [@Pilgrim6938](https://x.com/Pilgrim6938)）

**用這個程式庫分析比較，評估 token 價格與人工返工成本的關係。**

貼文比較 Claude Fable 5、Opus 4.8、GPT-5.5 與 Gemini 3.1 Pro 執行同一任務：分析約 90,000 行程式庫、找出快取失效問題，並提出完整修復計畫。作者認為，計入開發者修正時間後，token 單價與實際任務成本會有差異，建議選擇性地將 Fable 5 用於複雜重構、跨模組遷移及長鏈代理工作。

Type: Evaluation | Date: 2026-06-11

---


<a id="case-67"></a>
### Case 67: [Super Mario 遊戲 Token 成本](https://x.com/pankajkumar_dev/status/2064941888990593416)（作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev)）

**用這個單次生成的遊戲案例，估算 Fable 5 的輸出品質與 token 消耗。**

創作者要求 Claude Fable 5 製作 Nintendo Super Mario 風格的遊戲。貼文表示，任務使用約 200 萬 token，並在單次生成中獲得良好結果，可用來評估遊戲製作品質與成本。

Type: Demo | Date: 2026-06-11

---


<a id="case-68"></a>
### Case 68: [Claude Code 回退設定](https://x.com/oikon48/status/2064937790010503347)（作者 [@oikon48](https://x.com/oikon48)）

**用這個案例了解 Fable 5 訊息被標記時，Claude Code 如何切換模型。**

貼文指出 Claude Code 的 `/config` 中有一項名為「Switch models when a message is flagged」的設定。它說明 Fable 5 如何在訊息涉及攻擊性資安技術、生物／生命科學實驗方法、分子機制，或要求擷取模型思考過程等被標記領域時，回退至 Opus 模型。

Type: Integration | Date: 2026-06-11

---


<a id="case-69"></a>
### Case 69: [Namma Metro 模擬器建置](https://x.com/anilbpai/status/2064927784833790091)（作者 [@anilbpai](https://x.com/anilbpai)）

**用這個展示作為透過自然語言與 Fable 5 開發大眾運輸模擬器的精簡範例。**

創作者表示，自己在搭乘班加羅爾捷運時，以 Claude Fable 5 為程式開發夥伴，建置了 Namma Metro 模擬器。貼文雖然簡短，但連結至視覺展示，呈現 Fable 5 應用於特定城市模擬構想的例子。

Type: Demo | Date: 2026-06-11

---


<a id="case-70"></a>
### Case 70: [Dusk Drive 單提示詞遊戲](https://x.com/VincentLogic/status/2064921358359011684)（作者 [@VincentLogic](https://x.com/VincentLogic)）

**用這個單提示詞駕駛遊戲案例，評估 Fable 5 在無人工編修下製作低多邊形遊戲原型的能力。**

貼文描述 Claude Fable 5 從單一提示詞建立完整駕駛遊戲 Dusk Drive。創作者強調低多邊形視覺風格、極光下的雪地甩尾場景，並聲稱從構想到可玩版本之間完全沒有人工編輯。

Type: Demo | Date: 2026-06-11

---


<a id="case-71"></a>
### Case 71: [APEX-Agents Pass@1 排名](https://x.com/GratomicAi/status/2064970797978911102)（作者 [@GratomicAi](https://x.com/GratomicAi)）

**用這個 APEX-Agents 結果，比較 Fable 5 Max 在多步驟自主任務上的表現。**

貼文表示，Fable 5 Max 以 45% Pass@1 在 APEX-Agents 排行榜排名第二，落後 Gemini 3.5 Flash、領先 Opus。作者將 APEX-Agents 描述為衡量 AI 能否獨立執行複雜多步驟任務的基準。

Type: Evaluation | Date: 2026-06-11

---


<a id="case-72"></a>
### Case 72: [Claude 模型選擇手冊](https://x.com/charliejhills/status/2064957428211536212)（作者 [@charliejhills](https://x.com/charliejhills)）

**用這份模型選用手冊，把 Fable 5 留給 Claude Code 中最困難的任務。**

貼文從模型推理投入與額度消耗的角度，比較 Haiku 4.5、Sonnet 4.6、Opus 4.8 與 Fable 5。實務建議是日常工作使用 Sonnet、較難問題切換至 Opus，再把 Fable 5 留給需要深入規劃、建置與測試的最困難 Claude Code 任務。

Type: Tutorial | Date: 2026-06-11

---


<a id="case-73"></a>
### Case 73: [HermesWorld 自動代理循環](https://x.com/outsource_/status/2064954350187778366)（作者 [@outsource_](https://x.com/outsource_)）

**用這個案例研究一個免手動介入的 Fable 5 循環，持續數日進行建置、測試、實際遊玩與基本功能檢查。**

創作者描述透過完全自動化循環，以 Fable 5 建立 HermesWorld v2。據其表示，代理能運行數日，持續建置功能、測試功能、實際操作成果並執行基本功能檢查，同時朝完成目標推進。

Type: Integration | Date: 2026-06-11

---


<a id="case-74"></a>
### Case 74: [麥肯錫風格報告提示詞測試](https://x.com/smtgpt/status/2064953210335588758)（作者 [@smtgpt](https://x.com/smtgpt)）

**用這條文件生成提示詞，評估顧問報告的結構、圖表、敘事與風險分析。**

創作者要求 Fable 5 就比特幣作為資產類別及區塊鏈技術，撰寫麥肯錫風格詳細報告，視需要加入圖表與視覺資料。據其表示，輸出是 19 頁文件，包含資料、圖表、投資論點與風險分析；評語認為結構良好，但視覺呈現可更清楚，說明也可更精簡。

Type: Tutorial | Date: 2026-06-11

---


<a id="case-75"></a>
### Case 75: [可見防護措施上線](https://x.com/ClaudeDevs/status/2064949876463645026)（作者 [@ClaudeDevs](https://x.com/ClaudeDevs)）

**用這則官方說明了解 Fable 5 防護機制的可見性、API 拒答原因與回退至 Opus 的行為。**

ClaudeDevs 宣布一系列變更，讓 Fable 5 針對前沿大型語言模型開發的防護措施變得可見。被標記的請求將明確顯示回退至 Opus 4.8；被標記的 API 請求則預期會回傳拒答原因。貼文也解釋了為何防護措施最初以不可見形式推出，以及 Anthropic 為何現在認為那是錯誤的取捨。

Type: Integration | Date: 2026-06-11

---


<a id="case-76"></a>
### Case 76: [Claude Code 模型比對修正](https://x.com/ClaudeCodeLog/status/2064948584907153576)（作者 [@ClaudeCodeLog](https://x.com/ClaudeCodeLog)）

**用這則 Claude Code 更新說明，避免 Fable 5 模型名稱與上下文比對發生問題。**

Claude Code 2.1.173 修正 Fable 5 模型名稱的處理方式，移除 `[1m]` 後綴，避免預設 1M 上下文破壞模型比對。同一版本也抑制了一則誤報的 Windows 沙盒相依套件警告，並釐清 grep 說明中的輸出模式。

Type: Integration | Date: 2026-06-11

---


<a id="case-77"></a>
### Case 77: [Claude Code 中的三個網頁應用程式](https://x.com/0x3b33/status/2064948399300825439)（作者 [@0x3b33](https://x.com/0x3b33)）

**用這個新手程式開發展示，觀察 Fable 5 在 Claude Code 中生成多個網頁應用程式的表現。**

創作者表示，自己沒有程式開發背景，卻用 Claude Code 與 Fable 5 在 30 分鐘內建立三個可運作的網頁應用程式，分別在本機的 3000、3001 與 3002 連接埠開放。應將其視為輕量的新手工作流程展示，而非基準測試。

Type: Demo | Date: 2026-06-11

---


<a id="case-78"></a>
### Case 78: [Rilable 開源應用程式建構器](https://x.com/rileybrown/status/2064931283403178354)（作者 [@rileybrown](https://x.com/rileybrown)）

**用這個開源應用程式建構器案例，研究 Fable 5 在 iOS、網頁應用程式、沙盒與 API token 成本上的應用。**

創作者將 Rilable 開源；它是一款能建立網頁應用程式與 iOS 應用程式的 iOS App。貼文表示，它以 Fable 5 透過 10 次提示詞建成，API token 成本約 $210；使用 Claude 模型生成應用程式、Daytona 啟動沙盒、Convex 作為資料庫、Vercel AI Gateway 提供 AI 功能，以及 Chorus 代理的 iOS 技能製作 iOS App。

Type: Integration | Date: 2026-06-11

---


<a id="case-79"></a>
### Case 79: [DeepSWE 編碼代理指數首秀](https://x.com/ArtificialAnlys/status/2065328920514515037)（作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys)）

**用更新後的 Artificial Analysis 指數，對比 Fable 5 在更難的代理式編碼任務上的表現，這些任務避免複用公開 GitHub 修復。**

Artificial Analysis 在其 Coding Agent Index 中用 Datacurve 的 DeepSWE 替換了 SWE-Bench Pro。帖子稱，DeepSWE 會從零編寫任務，而不是改寫公開 GitHub issue 或 pull request，從而減少基準污染。在更新後的排名中，搭配 Fable 5 Max 的 Claude Code 以 77 分首秀，領先於搭配 GPT-5.5 xhigh 的 Codex 的 76 分，以及搭配 Opus 4.8 Max 的 Claude Code 的 73 分。

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [DataEmpire 網站分析遊戲](https://x.com/marclou/status/2065029898243318093)（作者 [@marclou](https://x.com/marclou)）

**讓 Claude Fable 5 把訪客和里程碑映射成遊戲實體，把原始網站分析數據變成可重玩的遊戲。**

Marc Lou 表示，Claude Fable 5 基於他的 DataFast 網站分析 API 構建了 DataEmpire。每位訪客都會變成村民，流量增長會擴展聚落，而當訪客達到 100 萬時會解鎖 Age of Legends。公開 demo 允許 DataFast 用戶通過遊戲層重放自己網站的歷史，因此這更像一個有 API 支撐的產品化案例，而不是靜態遊戲片段。

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [FrontierSWE 20 小時任務信號](https://x.com/ProximalHQ/status/2065184730279223410)（作者 [@ProximalHQ](https://x.com/ProximalHQ)）

**用 FrontierSWE 證明 Fable 5 不只適合短期修 bug，也能在超長工程任務中持續保持產出。**

ProximalHQ 表示，Claude Fable 5 在 FrontierSWE 上排名第一，並稱這是自他們發佈該基準以來見過的最大能力躍遷。他們的說明稱，Fable 5 在很多任務上可以持續高效工作接近 20 小時，並能把早期模型實際上難以企及的任務真正做滿。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [KernelBench-Hard CUDA 記錄](https://x.com/elliotarledge/status/2065109393142849932)（作者 [@elliotarledge](https://x.com/elliotarledge)）

**當你需要低層優化而不只是現有庫封裝時，用 Fable 5 處理高級 CUDA kernel 生成。**

Elliot Arledge 在 KernelBench-Hard 上讓 13 個 frontier 編碼代理各跑了 45 分鐘，並基於 RTX PRO 6000 做 roofline 評分。Claude Fable 5 在 top-k、sonic-MoE 和 W4A16 int4 GEMM 上創下歷史記錄，在 6 個問題裡拿下 5 個第一，作者還公開了運行結果、排行榜和代碼。同一串帖子也提到一次 FP8 GEMM 失手：Fable 5 嘗試寫了真正的 tensor-core kernel，但因為尾部對齊邊界情況拿了 0 分。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Figma Capture 落地頁克隆](https://x.com/mikefutia/status/2065537778516205856)（作者 [@mikefutia](https://x.com/mikefutia)）

**把競品頁面抓進 Figma 圖層後，讓 Claude Code 配合 Fable 5 重建結構、文案和品牌系統，而不是靠截圖猜測。**

Mike Futia 描述了一個工作流：先用 Figma 的 Chrome 擴展把網站複製成可編輯圖層，再讓 Claude Code 通過 Figma MCP 讀取這些圖層，用用戶自己的品牌語氣重寫頁面，並由 GPT Image 2 生成符合品牌的攝影圖。聲稱的端到端結果是，大約 15 分鐘就能做出一個可上線的落地頁，而 16 張圖片的生成 API 成本大約只有 2 美元。

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [兩小時做出 GTA 2 克隆](https://x.com/techhalla/status/2064682080445898957)（作者 [@techhalla](https://x.com/techhalla)）

**把 Fable 5 的代碼生成和獨立素材工具結合起來，快速做出可玩的 3D 遊戲，而不必手寫整個技術棧。**

TechHalla 表示，Claude Fable 5 High 在大約兩小時內做出了一個 GTA 2 風格克隆，而創作者則在 Tripo 中生成自定義 3D 模型。帖子還指向一個帶提示詞的教程線程，因此這更像是一個多工具遊戲生產的緊湊示例，而不是單純的基準預告。

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [CloudWatch 日誌分診代理](https://x.com/diblacksmith/status/2066230084273344698)（作者 [@diblacksmith](https://x.com/diblacksmith)）

**讓 Fable 5 驅動的代理消化超大規模服務日誌上下文，先推斷架構，再收斂到具體故障。**

diblacksmith 表示，一個 RLM 代理在單次運行中處理了大約 8 萬行 CloudWatch 日誌，走到 53 步時，當前只消耗了約 3.2 萬活躍 token。他說，這個代理從日誌中推斷出了系統架構，還標出了團隊之前漏掉的問題，包括 AgentCore 限流和 Slack `user_not_found` 失敗。

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [沙盒中的世界盃預測器](https://x.com/upstash/status/2064702195333820846)（作者 [@upstash](https://x.com/upstash)）

**把多個 frontier 模型放進隔離沙盒，讓它們為公開預測應用研究實時新聞、傷病和黃牌背景。**

Upstash 表示，它在隔離的 Upstash 沙盒中運行 Claude Fable 5、GPT-5.5 和 Gemini，構建了一個世界盃預測器。這個 demo 和開源發佈把 Fable 5 放在一個多模型研究與編排棧中的其中一環，而不只是單獨的聊天演示。

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [WolfBench 拒答成本案例](https://x.com/WolfBenchAI/status/2065582716054376921)（作者 [@WolfBenchAI](https://x.com/WolfBenchAI)）

**在為 Fable 5 的長自主運行定價時，把拒答行為視為真實的基準變量。**

WolfBenchAI 表示，它對 Claude Fable 5 的評測花費了 11,081.12 美元，是該套基準中迄今最昂貴的一次，但依然沒能登頂，因為重複拒答降低了有效任務完成量。對於需要給代理評測或其他高自主工作負載做預算的團隊，這是一個很具體的限制案例。

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [API 訪問截止追蹤器](https://x.com/simonw/status/2065618703480414666)（作者 [@simonw](https://x.com/simonw)）

**如果你的工作流依賴持續訪問某個可能被限流或撤下的 frontier 模型，就用腳本監控可用性。**

Simon Willison 表示，他每分鐘 ping 一次 `claude-fable-5` API，以觀察訪問能持續多久，並報告了它對自己停止響應的精確時間點。這條帖子在應用細節上比較薄，但它具體證明了：訪問連續性本身已經成了用戶必須測量、而不能默認存在的運維限制。

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5 社群展示



<a id="case-89"></a>
### Case 89: [程式碼生成的有聲狐狸動畫](https://x.com/chetaslua/status/2117224839010459987) (作者 [@chetaslua](https://x.com/chetaslua))

**用逐鏡創作要求，指定可獨立執行的 HTML 動畫及其聲音設計。**

創作者表示，自己製作了一支 66 秒的狐狸與紙鳥短片，畫格與音訊均由 Python 生成，約經過 2 小時 40 分鐘工作後，以單一 HTML 檔案交付。附帶提示詞指定鏡頭、原創畫作、音效與畫格檢查。貼文將影片與詳細創作要求、製作討論的截圖一起呈現。

[作者完整提示詞](https://x.com/chetaslua/status/2117224843661980093)

[![程式碼生成的有聲狐狸動畫](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![程式碼生成的有聲狐狸動畫](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![程式碼生成的有聲狐狸動畫](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [開放式創作要求生成的動畫](https://x.com/notjazii/status/2117221957104239010) (作者 [@notjazii](https://x.com/notjazii))

**比較程式模型根據開放式動畫要求，與依照詳細分鏡所產生的成果。**

作者分享一段動畫，表示從寬泛的創作要求出發，花約一小時以程式碼製作，未使用外部素材。貼文將成果呈現為開放式的創意程式設計練習。

[![開放式創作要求生成的動畫](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [建築公司動畫網站](https://x.com/exploraX_/status/2117176904306335864) (作者 [@exploraX_](https://x.com/exploraX_))

**用建築公司網站的需求，評估動畫 3D 展示與頁面構圖。**

創作者分享一個根據建築公司需求製作的動畫 3D 網站，並附上成果錄影。

[![建築公司動畫網站](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Three.js 汽車展示](https://x.com/chetaslua/status/2116975056014430419) (作者 [@chetaslua](https://x.com/chetaslua))

**以汽車場景作為精簡測試，檢視 3D 構圖、材質與鏡頭呈現。**

創作者分享 Three.js 汽車展示。錄影提供了一個精簡參考，可用來評估場景與視覺呈現。

[![Three.js 汽車展示](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Minecraft 風格瀏覽器遊戲展示](https://x.com/notjazii/status/2116919129974411584) (作者 [@notjazii](https://x.com/notjazii))

**評估生成的瀏覽器遊戲時，將遊戲錄影與創作者的試玩連結一起檢視。**

作者分享 Minecraft 風格遊戲錄影及試玩連結，將其描述為約一至兩小時、一次生成的製作任務。貼文將錄製成果與試玩連結一起提供，方便讀者探索。

[![Minecraft 風格瀏覽器遊戲展示](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Three.js 鵜鶘騎自行車動畫](https://x.com/chetaslua/status/2116882694026269148) (作者 [@chetaslua](https://x.com/chetaslua))

**檢視騎車場景中的角色動作協調、自行車幾何結構與環境細節。**

創作者分享一段寫實的 Three.js 鵜鶘騎自行車動畫，並表示是一次生成的結果。短片可作為檢視角色動作、自行車結構與周圍場景的參考。

[![Three.js 鵜鶘騎自行車動畫](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [附原始提示詞的鵜鶘騎車 SVG](https://x.com/marmaduke091/status/2116233349391962392) (作者 [@marmaduke091](https://x.com/marmaduke091))

**重用創作者的簡短 SVG 提示詞，在相同輸入下比較幾何結構與細節。**

作者將已渲染的鵜鶘騎自行車圖片，與下方逐字保留的簡短 SVG 要求一起呈現。

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![附原始提示詞的鵜鶘騎車 SVG](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [斑馬奔馳動畫樣本](https://x.com/AI_Screening/status/2115845754468356465) (作者 [@AI_Screening](https://x.com/AI_Screening))

**用動物奔馳短片檢視步態一致性與動作連續性。**

作者分享自己挑選的斑馬奔馳任務最佳輸出。短片為讀者提供了可具體檢視的動作樣本。

[![斑馬奔馳動畫樣本](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [保留人工下單的 TradingView 指標](https://x.com/waveking1314/status/2114572023204806669) (作者 [@waveking1314](https://x.com/waveking1314))

**評估會標記可能進場點並附上簡評的指標時，保留人工執行下單。**

創作者表示，自己用 Claude Fable 5.5 撰寫 TradingView 指標，標記可能進場點並加入簡評，由使用者決定是否下單。貼文附有錄影，並表示日後會分享指標。

[![保留人工下單的 TradingView 指標](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---

<a id="acknowledge"></a>
## 🙏 致謝

這個 repository 的靈感來自那些公開分享真實 Claude Fable 5 使用案例的創作者、開發者、基準測試團隊與社群。

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314)

*我們無法保證每個案例都歸屬於最原始的創作者。如果有任何需要修正的地方，請聯絡我們，我們會更新。*

如果你有更多有趣的使用案例想分享，歡迎開 issue 或 pull request，協助擴充 Evolink usecase library。


[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
