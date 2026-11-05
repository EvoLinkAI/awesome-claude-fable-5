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
## 🍌 簡介

歡迎來到 Claude Fable 5 高訊號使用案例庫。

**我們收集 Claude Fable 5 的真實使用案例、教學、整合與評測，內容精選自公開 demo 與創作者社群。**

這份繁體中文 README 聚焦於具備具體工作流程、提示詞、demo、整合、基準測試證據或實際限制的高訊號案例。

大多數案例整理自 X/Twitter 貼文與公開 demo。每個案例標題都連回原始來源，每個作者帳號都連到創作者個人頁面。

在 Evolink 上試用：[Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

<a id="-overview"></a>
## 📊 概覽

- **88 個原有 Fable 5 案例，加上 218 個社群案例，共 306 個案例。**
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

| 案例 | 類型 |
|---|---|
| [程式碼生成的有聲狐狸動畫](#case-89) | Demo |
| [開放式創作要求生成的動畫](#case-90) | Demo |
| [建築公司動畫網站](#case-91) | Demo |
| [Three.js 汽車展示](#case-92) | Demo |
| [Minecraft 風格瀏覽器遊戲展示](#case-93) | Demo |
| [Three.js 鵜鶘騎自行車動畫](#case-94) | Demo |
| [附原始提示詞的鵜鶘騎車 SVG](#case-95) | Demo |
| [斑馬奔馳動畫樣本](#case-96) | Demo |
| [保留人工下單的 TradingView 指標](#case-97) | Demo |
| [從一個點發展成動畫故事](#case-98) | Demo |
| [穿越不同美術風格的超人](#case-99) | Demo |
| [附配樂的人類進步動畫短片](#case-100) | Demo |
| [與 Opus 比較的發布影片](#case-101) | Evaluation |
| [把歌詞與事件連成視覺敘事](#case-102) | Demo |
| [漂浮場景中的體素角色](#case-103) | Demo |
| [3D 魯布·戈德堡機械演示](#case-104) | Demo |
| [結合聲音與動態的 3D 控制器介面](#case-105) | Demo |
| [以 JavaScript 展示漫畫角色](#case-106) | Demo |
| [Updraft：世界、頭目與排行榜](#case-107) | Demo |
| [在舊金山地圖中駕駛](#case-108) | Demo |
| [為 Seedance 動作場面撰寫提示詞](#case-109) | Demo |
| [介紹桌面工作夥伴的影片](#case-110) | Demo |
| [以短提示詞生成風格轉換動畫](#case-111) | Demo |
| [三體問題視覺化](#case-112) | Demo |
| [多種美術風格的動畫畫廊](#case-113) | Demo |
| [機器夥伴與程序化毛髮](#case-114) | Demo |
| [數學主題動態剪輯](#case-115) | Demo |
| [Your Woman 歌詞影片](#case-116) | Demo |
| [以 JavaScript 重繪音樂影片](#case-117) | Demo |
| [中國足球主題動畫](#case-118) | Demo |
| [掌上主機重拓樸展示](#case-119) | Demo |
| [Minecraft 結合 Pokémon](#case-120) | Demo |
| [解說大型語言模型如何製成](#case-121) | Demo |
| [Altman 精華動態剪輯](#case-122) | Demo |
| [三十六計第一計的影片](#case-123) | Demo |
| [遊戲建模、綁定與動畫](#case-124) | Demo |
| [兒童死亡主題無言影片](#case-125) | Demo |
| [糖解至乙醇的 SVG 動畫](#case-126) | Demo |
| [十六艘 Starship 同步發射](#case-127) | Demo |
| [鵜鶘騎車動畫測試](#case-128) | Demo |
| [未來一百五十年的故事](#case-129) | Demo |
| [獨立重做 Humanity Walks](#case-130) | Demo |
| [The Grader 程式影片](#case-131) | Demo |
| [Reawakening 恐怖短片](#case-132) | Demo |
| [二十五秒自我改善影片](#case-133) | Demo |
| [城堡場景與使用成本回饋](#case-134) | Evaluation |
| [四十秒品牌發布廣告](#case-135) | Demo |
| [重製 Rocketball](#case-136) | Demo |
| [體素寶塔比較](#case-137) | Evaluation |
| [想像中的 Switch 3 發表展示](#case-138) | Demo |
| [前後兩版登陸頁](#case-139) | Evaluation |
| [想像 AI 的內在視角](#case-140) | Demo |
| [Go 歌詞動態設計](#case-141) | Demo |
| [第二支十五秒動態作品集](#case-142) | Demo |
| [有引導的代理實作審查](#case-143) | Tutorial |
| [Claude 吉祥物舞蹈](#case-144) | Demo |
| [可互動的七大奇景島嶼](#case-145) | Demo |
| [Propellerheads 音樂影片](#case-146) | Demo |
| [Steamboat Willie 動畫比較](#case-147) | Evaluation |
| [三星堆主題影片](#case-148) | Demo |
| [Bugatti Chiron 前後比較](#case-149) | Evaluation |
| [GRAIN 概念短片](#case-150) | Demo |
| [Human in Transit 藝術畫廊](#case-151) | Demo |
| [絲綢之路視覺短片](#case-152) | Demo |
| [四種轉型路徑簡報](#case-153) | Demo |
| [比較歷史對話語氣](#case-154) | Evaluation |
| [鴞鸚鵡可愛度測試](#case-155) | Evaluation |
| [蜘蛛人穿越十個漫畫年代](#case-156) | Demo |
| [光明會題材的虛構恐怖影片](#case-157) | Demo |
| [程式製作的核科學史影片](#case-158) | Demo |
| [全民高收入解說動畫](#case-159) | Demo |
| [Altman 與 Amodei 爭議解說](#case-160) | Demo |
| [Claude 吉祥物音樂影片](#case-161) | Demo |
| [從夸克連續縮放到宇宙](#case-162) | Demo |
| [想像二〇七六年的世界](#case-163) | Demo |
| [下曼哈頓建築時間線](#case-164) | Demo |
| [甲骨文主題動畫](#case-165) | Demo |
| [另一支角色穿越藝術史動畫](#case-166) | Demo |
| [以程式製作 Seikilos 影音作品](#case-167) | Demo |
| [噴射機動畫比較](#case-168) | Evaluation |
| [模型自我介紹影片](#case-169) | Demo |
| [末日後卡牌遊戲原型](#case-170) | Demo |
| [The Late Byte 辦公室動畫](#case-171) | Demo |
| [Queens of the Stone Age 歌詞動畫](#case-172) | Demo |
| [分享的 Three.js 敘事場景](#case-173) | Demo |
| [在歷史場景中月球漫步](#case-174) | Demo |
| [詳細提示詞生成動態圖像](#case-175) | Demo |
| [租賃企業網站介面](#case-176) | Demo |
| [AGI 題材創意影片](#case-177) | Demo |
| [帶貓咪支線的藝術史](#case-178) | Demo |
| [戰鬥原型與體素場景](#case-179) | Demo |
| [網路迷因年代記](#case-180) | Demo |
| [一行要求生成粒子動態](#case-181) | Demo |
| [Kung-Fu Boy 動畫](#case-182) | Demo |
| [荷姆茲海峽辯論動畫](#case-183) | Demo |
| [獨角獸 SVG 風格實驗](#case-184) | Demo |
| [萬聖節主題動畫](#case-185) | Demo |
| [Blender CLI 野蠻人與封面](#case-186) | Demo |
| [Claude 的一天](#case-187) | Demo |
| [3D 人類歷史](#case-188) | Demo |
| [快速動態設計短片](#case-189) | Evaluation |
| [自由發揮的複雜 3D 創作](#case-190) | Demo |
| [火柴人打鬥動畫](#case-191) | Demo |
| [一條提示詞的 UI 動態序列](#case-192) | Demo |
| [SCP-8517 虛構動畫](#case-193) | Demo |
| [水彩秋日動畫](#case-194) | Demo |
| [程序化人偶舞台](#case-195) | Demo |
| [瀏覽器中的鵜鶘騎車](#case-196) | Demo |
| [宇宙看見自己](#case-197) | Demo |
| [獨立噴射機動畫測試](#case-198) | Demo |
| [最初的自由動態短片](#case-199) | Demo |
| [以程式呈現文明](#case-200) | Demo |
| [晶片至伺服器縮放比較](#case-201) | Evaluation |
| [月球旅行動畫計畫](#case-202) | Demo |
| [日式體素場景比較](#case-203) | Evaluation |
| [Steaming the Frontier 影音短片](#case-204) | Demo |
| [超人穿越多種美術風格](#case-205) | Demo |
| [Cupcake 風格頭目戰原型](#case-206) | Demo |
| [太陽位置變化的帆船](#case-207) | Demo |
| [Paracortex 與 Pi 更新影片](#case-208) | Demo |
| [Curio 2.0 網站宣傳片](#case-209) | Demo |
| [想像中的 Hugging Face 3D 故事](#case-210) | Demo |
| [Claude for Chrome 操作 JS Paint](#case-211) | Demo |
| [靜態鵜鶘騎車 SVG](#case-212) | Demo |
| [BlockBench MCP 與 Minecraft 技能](#case-213) | Demo |
| [單一 HTML 檔案的 Dig Dug](#case-214) | Demo |
| [機械章魚 SVG](#case-215) | Demo |
| [Humanity Walks 藝術風格之旅](#case-216) | Demo |
| [開放式黑洞場景](#case-217) | Demo |
| [極光水母動畫比較](#case-218) | Evaluation |
| [Nintendo Switch 拼接與啟動 SVG](#case-219) | Demo |
| [The Loom 互動 3D 場景](#case-220) | Demo |
| [同一提示詞的動態圖形設計短片](#case-221) | Evaluation |
| [更乾淨但較缺乏深度的景物](#case-222) | Evaluation |
| [日式場景的好壞參半結果](#case-223) | Evaluation |
| [控制器 SVG 比較](#case-224) | Evaluation |
| [工業裝置場景](#case-225) | Demo |
| [巨型帶殼鰓蟲重建](#case-226) | Demo |
| [兩條提示詞的 GameCube 控制器](#case-227) | Demo |
| [為 X 帖子編輯截圖](#case-228) | Demo |
| [前後兩版體素櫻花](#case-229) | Evaluation |
| [SHADERKIN 布料介面原型](#case-230) | Demo |
| [分享的金色時鐘介面動畫](#case-231) | Demo |
| [Before There Was Anything 敘事影片](#case-232) | Demo |
| [分享的藍色粒子漩渦](#case-233) | Demo |
| [兩次修改後的多面板介面](#case-234) | Demo |
| [渲染場景中的動物疊疊樂](#case-235) | Demo |
| [四種開放世界 RPG 成果比較](#case-236) | Evaluation |
| [兩段前端動畫比較](#case-237) | Evaluation |
| [以程式生成的苔蘚機器人影片](#case-238) | Demo |
| [重新製作貨櫃港模擬](#case-239) | Demo |
| [重新製作機場停機坪場景](#case-240) | Demo |
| [鵜鶘騎車穿越抽象 3D 世界](#case-241) | Demo |
| [歷史帆船場景](#case-242) | Demo |
| [與 Carbon 比較騎車及步態](#case-243) | Evaluation |
| [汽水瓶展示](#case-244) | Demo |
| [與 Astra 比較鵜鶘動作](#case-245) | Evaluation |
| [程式動畫的動態設計簡報](#case-246) | Tutorial |
| [由照片參考製作體素肖像](#case-247) | Demo |
| [與 Opus 比較飛行鵜鶘場景](#case-248) | Evaluation |
| [Morning Ride 鵜鶘網頁場景](#case-249) | Demo |
| [同一提示詞的不同風格場景](#case-250) | Evaluation |
| [鵜鶘、自行車與馬的構圖](#case-251) | Demo |
| [參考推文啟發的等角場景](#case-252) | Demo |
| [鵜鶘自行車的機械特寫](#case-253) | Demo |
| [自行車騎在鵜鶘上](#case-254) | Demo |
| [與 Carbon 比較鵜鶘 SVG 風格](#case-255) | Evaluation |
| [卡通藍鳥騎車場景](#case-256) | Demo |
| [林間道路鵜鶘騎車截圖](#case-257) | Demo |
| [與 Carbon 比較火柴人戰鬥](#case-258) | Evaluation |
| [早期測試的鵜鶘 SVG 參考](#case-259) | Demo |
| [跨模型 SVG 測試中的鵜鶘參考](#case-260) | Evaluation |
| [與 Carbon 比較自行車 SVG 細節](#case-261) | Evaluation |
| [3D 峽谷聚落](#case-262) | Demo |
| [與 Opus 比較控制器細節](#case-263) | Evaluation |
| [每週網站 SEO 稽核流程](#case-264) | Integration |
| [在 Opus 動態設計重用 Fable 素材](#case-265) | Integration |
| [曼陀羅與幾何形體應用程式](#case-266) | Demo |
| [Three.js 自行車騎士](#case-267) | Demo |
| [FrontierCS 2 評測快照](#case-268) | Evaluation |
| [三模型斑馬動畫對比](#case-269) | Evaluation |
| [評論日文長篇文章](#case-270) | Evaluation |
| [以範例引導技術簡報](#case-271) | Evaluation |
| [比較音樂整體連貫性](#case-272) | Evaluation |
| [提早宣告完成與較弱的設計](#case-273) | Limit |
| [令人不適的魷魚藝術結果](#case-274) | Limit |
| [藍圖風格動態設計](#case-275) | Demo |
| [體素櫻花場景中的鳥魚](#case-276) | Demo |
| [角色生成失敗回饋](#case-277) | Limit |
| [附執行時間與成本的鵜鶘 SVG](#case-278) | Evaluation |
| [手機遠端管理 Claude Code 群集](#case-279) | Integration |
| [高山湖泊上空的銀河](#case-280) | Demo |
| [程序化水體與音效中的鯨躍](#case-281) | Demo |
| [四模型斑馬動作比較](#case-282) | Evaluation |
| [Lightreel 自然語言創作者搜尋](#case-283) | Demo |
| [雲海上方的飛船](#case-284) | Demo |
| [動態剖面的機械心臟](#case-285) | Demo |
| [可探索的漂浮體素寶塔花園](#case-286) | Demo |
| [八個 Agent 團隊的海洋冒險短片](#case-287) | Demo |
| [互動式超級跑車展示](#case-288) | Demo |
| [生命之樹的誕生](#case-289) | Demo |
| [可行走城堡與內部機械](#case-290) | Demo |
| [吐司角色與機械甲蟲](#case-291) | Demo |
| [暴風雨中的燈塔守護者](#case-292) | Demo |
| [海濱小鎮中的海洋生物](#case-293) | Demo |
| [三模型地毯賽車比較](#case-294) | Evaluation |
| [卡車變形成機器人](#case-295) | Demo |
| [Fable 與混元動畫影格比較](#case-296) | Evaluation |
| [關於分享光芒的動畫](#case-297) | Demo |
| [群山之間的體素村莊](#case-298) | Demo |
| [四模型鵜鶘與大象構圖](#case-299) | Evaluation |
| [帶衝擊影格的動漫劍鬥](#case-300) | Demo |
| [四模型奔鹿動畫比較](#case-301) | Evaluation |
| [穿越積水城市的機器人](#case-302) | Demo |
| [Blender 寶劍與展示短片](#case-303) | Demo |
| [Lantern Isle 像素村莊動畫](#case-304) | Demo |
| [Pause 遊戲影片剪輯示範](#case-305) | Demo |
| [海濱騎車的鵜鶘](#case-306) | Demo |

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

[動畫版本 · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="附原始提示詞的鵜鶘騎車 SVG" width="760"></a>

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


<a id="case-98"></a>
### Case 98: [從一個點發展成動畫故事](https://x.com/cherry_mx_reds/status/2105825930799432073) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**用最簡單的繪圖要求，觀察模型如何延伸視覺故事。**

作者表示原本只要求畫一個點，並分享最後形成的短篇動畫。附上的影片呈現開放式視覺要求轉變成敘事的具體成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="從一個點發展成動畫故事" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [穿越不同美術風格的超人](https://x.com/chetaslua/status/2105757136219504862) (作者 [@chetaslua](https://x.com/chetaslua))

**用同一個熟悉角色，觀察動畫風格改變時的連貫性。**

創作者分享一段連續的超人動畫，畫面在不同美術風格之間轉換。不同風格的視覺處理是這次作品的主要創意成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="穿越不同美術風格的超人" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [附配樂的人類進步動畫短片](https://x.com/imjustnewatai/status/2106081142143168580) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**規劃動畫解說時，把歷史時間線與未來段落一起寫入簡報。**

作者表示用一條提示詞製作人類進步及未來三十年的影片，並分享約三分鐘的動畫。他們稱作品使用原創配樂，沒有採用現成影像或音樂素材。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="附配樂的人類進步動畫短片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [與 Opus 比較的發布影片](https://x.com/mesmerlord/status/2105771088374288692) (作者 [@mesmerlord](https://x.com/mesmerlord))

**比較根據同一創作簡報製作的完整發布影片。**

作者根據 Anthropic 影片參考簡報，分享兩支發布影片候選作。原帖明確說明數字為虛構，也允許使用 Codex 生圖，因此這些影片屬於創意廣告，而非基準測試證據。

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="與 Opus 比較的發布影片" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="與 Opus 比較的發布影片" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [把歌詞與事件連成視覺敘事](https://x.com/chetaslua/status/2105934928483701214) (作者 [@chetaslua](https://x.com/chetaslua))

**結合既有歌曲的歌詞與特定事件，建立視覺故事。**

創作者表示要求模型把歌詞與一宗 Hugging Face 事件連結，並分享形成的動畫。歌曲和事件都是這段敘事的創作輸入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="把歌詞與事件連成視覺敘事" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [漂浮場景中的體素角色](https://x.com/blueemi99/status/2105804692811137242) (作者 [@blueemi99](https://x.com/blueemi99))

**同時觀察體素角色、周圍景物與動畫細節。**

作者分享漂浮場景中的體素自我角色，強調細節和動態。影片提供一個可與其他生成結果比較的體素設計範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="漂浮場景中的體素角色" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [3D 魯布·戈德堡機械演示](https://x.com/imjustnewatai/status/2105889407056109991) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**先描述連鎖反應場景，再要求固定長度的演示影片。**

作者先以短提示詞要求一套複雜的 3D 魯布·戈德堡機械，再要求一分鐘影片。附上的片段展示形成的連鎖反應視覺化。

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="3D 魯布·戈德堡機械演示" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [結合聲音與動態的 3D 控制器介面](https://x.com/notjazii/status/2106050222828998967) (作者 [@notjazii](https://x.com/notjazii))

**綜合視覺動態、聲音與按鈕行為評估控制器介面。**

創作者分享 3D 控制器介面，並表示加入聲音、動畫與觸覺回饋。錄影開啟聲音，呈現具體的介面演示。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="結合聲音與動態的 3D 控制器介面" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [以 JavaScript 展示漫畫角色](https://x.com/chetaslua/status/2105792187200147541) (作者 [@chetaslua](https://x.com/chetaslua))

**用角色展示，探索程式碼可以提供哪些精細視覺細節。**

作者表示一次生成 Marvel 與 DC 角色的 JavaScript 展示，模型自行選取細微角色特徵並剪輯影片。原帖附上完整角色展示成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="以 JavaScript 展示漫畫角色" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [Updraft：世界、頭目與排行榜](https://x.com/EMostaque/status/2106065029850091943) (作者 [@EMostaque](https://x.com/EMostaque))

**把遊戲錄影、試玩連結與明確功能清單放在一起。**

作者分享 Updraft，表示以高推理強度、少量提示詞工作數小時。功能清單包括二十一個世界、3D 變體、二十一個機制不同的頭目與排行榜。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="Updraft：世界、頭目與排行榜" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [在舊金山地圖中駕駛](https://x.com/mindblown_ai/status/2106089461969019357) (作者 [@mindblown_ai](https://x.com/mindblown_ai))

**用城市駕駛原型，探索地圖導航與遊戲目標。**

來源發帖者分享他人製作的舊金山駕駛遊戲錄影與試玩連結，並提到 Three.js。這裡署名的是來源發帖者，並不表示對方製作了遊戲。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="在舊金山地圖中駕駛" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [為 Seedance 動作場面撰寫提示詞](https://x.com/Chengzilhy/status/2105850801663234374) (作者 [@Chengzilhy](https://x.com/Chengzilhy))

**記錄多工具動作場面時，區分提示詞撰寫與影片生成。**

作者分享擴展後的打鬥場面，表示提示詞由 Fable 撰寫，影片則由 Seedance 2.5 生成。這個流程使用語言模型準備影片生成的輸入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="為 Seedance 動作場面撰寫提示詞" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [介紹桌面工作夥伴的影片](https://x.com/ishuagra02/status/2106138602073641241) (作者 [@ishuagra02](https://x.com/ishuagra02))

**用短介紹影片說明程式開發工具的擴充功能。**

創作者展示 clawdhouse Claude Code 模組，並表示其介紹影片由 Fable 製作。吉祥物工作夥伴及情緒是被介紹模組的功能，並非宣稱 Fable 開發了該模組。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="介紹桌面工作夥伴的影片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [以短提示詞生成風格轉換動畫](https://x.com/cherry_mx_reds/status/2105816670896009224) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**先測試簡短動畫要求，再增加詳細創作規格。**

作者表示要求製作一段酷炫動畫，約十五分鐘後得到畫面風格轉換的成果。原帖直接引用了最初的簡短要求。

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="以短提示詞生成風格轉換動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [三體問題視覺化](https://x.com/zAdrielsan/status/2105822678519001360) (作者 [@zAdrielsan](https://x.com/zAdrielsan))

**在軌道視覺化簡報中，區分 CPU 模擬與 GPU 渲染。**

作者表示用約一千行 Bend2 製作三體場景，CPU 以辛積分處理物理運算，GPU 負責像素渲染。他們另稱作品在 M5 上達到六十 FPS，並附有形式化證明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="三體問題視覺化" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [多種美術風格的動畫畫廊](https://x.com/blueemi99/status/2105782154387189771) (作者 [@blueemi99](https://x.com/blueemi99))

**在同一座動畫畫廊中比較多種美術風格。**

作者分享以 xhigh 設定製作的動畫畫廊。作品把多種美術風格放在一起，方便在單一成果中比較不同視覺處理。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="多種美術風格的動畫畫廊" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [機器夥伴與程序化毛髮](https://x.com/KanaWorks_AI/status/2106717014245183517) (作者 [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**把既有角色動畫與程序化細化結合，保留原始素材的角色。**

作者將既有 Unimate 機器狗動畫細化為夥伴，也製作了具有梳毛與軌跡功能的毛絨虛擬寵物。Unreal Engine 與原有機器狗動畫都是明確的流程組成。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="機器夥伴與程序化毛髮" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [數學主題動態剪輯](https://x.com/TurboNexic/status/2106710792590835934) (作者 [@TurboNexic](https://x.com/TurboNexic))

**把數學主題動態圖像當成視覺溝通範例。**

來源發帖者分享數學主題的動態剪輯。直式片段將數學意象變成動畫設計，提供的是視覺演示，而非完整數學推導。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="數學主題動態剪輯" width="760">

*原影片的存檔影格。*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Your Woman 歌詞影片](https://x.com/atomtanstudio/status/2106702854639743467) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**圍繞指定錄音製作歌詞動態，保留音樂的輸入角色。**

創作者分享 White Town 的 Your Woman 歌詞影片。既有歌曲是視覺創作使用的音訊輸入，而不是宣稱由模型創作的音樂。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Your Woman 歌詞影片" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [以 JavaScript 重繪音樂影片](https://x.com/abhinavflac/status/2106638839666373114) (作者 [@abhinavflac](https://x.com/abhinavflac))

**重製音樂影片時，把指定來源影格轉描成程式圖形。**

作者描述把 Eminem 的 Godzilla 影片影格轉描為平面形狀，再用 JavaScript 重繪。原始影像與音樂都是這段動畫的輸入素材。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="以 JavaScript 重繪音樂影片" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [中國足球主題動畫](https://x.com/esrhengwu/status/2106625966965760380) (作者 [@esrhengwu](https://x.com/esrhengwu))

**把體育題材轉換為動畫敘事簡報。**

作者分享中國國家足球隊主題動畫，以發展及韌性作為創作方向。錄影提供一個具體的體育故事視覺化範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="中國足球主題動畫" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [掌上主機重拓樸展示](https://x.com/mickeysmith_jp/status/2106607349385630138) (作者 [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**討論拓樸時，把掌上主機渲染圖與線框呈現一起比較。**

來源發帖者在討論重拓樸時，並列掌上主機圖片和線框風格畫面。這是具體的建模展示，而非可編輯網格或完整重拓樸步驟。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="掌上主機重拓樸展示" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft 結合 Pokémon](https://x.com/MozeTech/status/2106590326634983710) (作者 [@MozeTech](https://x.com/MozeTech))

**在同一原型簡報中結合兩款熟悉遊戲的機制。**

作者展示真新鎮原型，結合 Minecraft 式建造與合成，以及 Pokémon 式捕捉，並提供演示連結。原帖將這次製作描述為一次生成的實驗。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft 結合 Pokémon" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [解說大型語言模型如何製成](https://x.com/imjustnewatai/status/2106546810793730419) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**把技術問題轉成視覺解說要求。**

作者詢問大型語言模型如何製成，並分享生成的解說影片。這項作品具體展示了以動畫序列呈現技術主題的方式。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="解說大型語言模型如何製成" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [Altman 精華動態剪輯](https://x.com/benchmark_lb900/status/2106539977404506303) (作者 [@benchmark_lb900](https://x.com/benchmark_lb900))

**用公眾人物題材測試短篇動態剪輯的節奏。**

作者分享 Altman 主題精華影片，並描述為一次生成的成果。直式錄影提供一個精簡的動態剪輯範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="Altman 精華動態剪輯" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [三十六計第一計的影片](https://x.com/jesselaunz/status/2106538284197548122) (作者 [@jesselaunz](https://x.com/jesselaunz))

**呈現敘事動畫流程時，一併記錄外部音樂工具。**

作者分享三十六計第一計主題影片，表示只使用一條指令。影片音樂明確使用 Suno V6，保留音訊工具的獨立角色。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="三十六計第一計的影片" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [遊戲建模、綁定與動畫](https://x.com/atomtanstudio/status/2106516974662713477) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**在遊戲場景比較中，一起評估角色建立、骨架綁定與動畫。**

作者分享 Depths of Despair 比較，內容包括角色建模、綁定與動畫。原帖說明作品使用的素材與工具，並將可見成果一起展示。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="遊戲建模、綁定與動畫" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [兒童死亡主題無言影片](https://x.com/cocoloba_/status/2106512963414970458) (作者 [@cocoloba_](https://x.com/cocoloba_))

**用沒有對白的視覺序列傳達沉重社會主題。**

作者分享兒童死亡主題影片，以呼吸中的嬰兒和逐漸變暗的嬰兒床形成敘事。案例保留視覺說故事任務，不採用片中的人口統計作為事實。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="兒童死亡主題無言影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [糖解至乙醇的 SVG 動畫](https://x.com/olddonkeyblog/status/2106508425211330750) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**在 HTML 中嵌入動態 SVG，解說分子過程。**

作者要求葡萄糖分子經歷糖解與乙醇形成，以 HTML 內的動態 SVG 呈現。錄影展示產生的科學視覺化處理。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="糖解至乙醇的 SVG 動畫" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [十六艘 Starship 同步發射](https://x.com/olddonkeyblog/status/2106507742454403485) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**為 HTML 與 SVG 動畫明確描述同步發射階段。**

作者要求十六艘 Starship 同時發射，之後進行級間分離並進入太空。錄影呈現形成的多物件動畫序列。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="十六艘 Starship 同步發射" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [鵜鶘騎車動畫測試](https://x.com/olddonkeyblog/status/2106507429265756165) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**把鵜鶘騎車場景當成協調動作的繪圖任務來觀察。**

作者分享以 Max 推理完成的鵜鶘騎車成果。這是一段獨立錄製的輸出，與其他作者對同類提示詞的版本分開保留。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="鵜鶘騎車動畫測試" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [未來一百五十年的故事](https://x.com/imjustnewatai/status/2106489784382197771) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**圍繞推想未來的簡報，結合腳本、程式視覺與配樂。**

作者表示一條指令生成了描繪人類未來一百五十年的影片。作品結合文字敘事、程式動畫與音樂，呈現可能的未來生活。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="未來一百五十年的故事" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [獨立重做 Humanity Walks](https://x.com/iowitz/status/2106489119186538583) (作者 [@iowitz](https://x.com/iowitz))

**把穿越藝術史的動畫構想重新做成獨立創作實驗。**

作者看到其他演示後，嘗試自己的穿越藝術史步行動畫並分享成果。這段影片作為獨立生成保留，不因題材相似就合併。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="獨立重做 Humanity Walks" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [The Grader 程式影片](https://x.com/argofowl/status/2106476549046513947) (作者 [@argofowl](https://x.com/argofowl))

**介紹程式生成影片時，明確記錄外部語音或音訊工具。**

作者分享以程式製作的 The Grader，並指出音訊使用 ElevenLabs v4。原帖表示這是一次生成、耗時約兩小時二十二分鐘的作品。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="The Grader 程式影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [Reawakening 恐怖短片](https://x.com/JaydenDavisNC/status/2106440774367822008) (作者 [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**用明確命名的恐怖題材，塑造短篇動畫。**

作者分享名為 Reawakening 的恐怖 AI 短片。附上的作品提供具體敘事與氣氛範例，可供恐怖動畫簡報參考。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="Reawakening 恐怖短片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [二十五秒自我改善影片](https://x.com/DAssetBuzz/status/2106505100575592838) (作者 [@DAssetBuzz](https://x.com/DAssetBuzz))

**把抽象的自我改善主題轉成短篇創作簡報。**

作者要求一支二十五秒影片，主題是什麼能讓模型變得更好，並分享成果。這個設定屬於創意敘事，而不是產品能力聲明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="二十五秒自我改善影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [城堡場景與使用成本回饋](https://x.com/nemumusitocha/status/2106429338556207284) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**評估 3D 場景時，同時考慮畫面細節與創作者的使用經驗。**

作者分享細節豐富的城堡場景，稱讚視覺構成，但認為使用成本不划算。案例將具體場景與作者的成本滿意度回饋放在一起。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="城堡場景與使用成本回饋" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [四十秒品牌發布廣告](https://x.com/0xashtonx/status/2106421702783914423) (作者 [@0xashtonx](https://x.com/0xashtonx))

**以自己的品牌作為精簡發布廣告的主題。**

創作者要求為自己的品牌製作四十秒發布廣告，並分享生成的影片。這是一個品牌宣傳敘事的具體任務範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="四十秒品牌發布廣告" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [重製 Rocketball](https://x.com/atomtanstudio/status/2106418747083022555) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**重製熟悉遊戲，將程式素材與互動機制結合。**

作者分享重製自一九八〇年代 C-64 遊戲的 Rocketball，表示素材以程式生成。替換網站版本仍被描述為未來計畫。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="重製 Rocketball" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [體素寶塔比較](https://x.com/dropout_layer/status/2106408147309252915) (作者 [@dropout_layer](https://x.com/dropout_layer))

**把同一場景的兩次成果與各自回報的成本一起比較。**

作者展示 Astra 與 Fable 的 3D 體素寶塔，分別回報 3.50 與 5.50 美元成本。比較針對這兩次執行及其畫面成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="體素寶塔比較" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [想像中的 Switch 3 發表展示](https://x.com/mathisbuilds/status/2106407842240418097) (作者 [@mathisbuilds](https://x.com/mathisbuilds))

**把想像中的產品當成概念簡報及演示任務。**

作者要求想像一款 Nintendo Switch 3 並製作演示，表示耗時約四小時。錄影呈現虛構的下一代主機概念，而非真實產品規格。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="想像中的 Switch 3 發表展示" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [前後兩版登陸頁](https://x.com/nemumusitocha/status/2106402952307200302) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**重跑同一登陸頁提示詞，比較不同時間的輸出變化。**

作者把新生成的登陸頁與先前以相同提示詞製作的頁面比較。可見的前後兩版設計提供實際介面比較範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="前後兩版登陸頁" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [想像 AI 的內在視角](https://x.com/blueemi99/status/2106397329653719115) (作者 [@blueemi99](https://x.com/blueemi99))

**把想像中的內在視角作為動畫創意題材。**

作者要求一支影片描繪身為 AI 模型可能有什麼感覺，並分享一次生成的成果。這個設定屬於想像性的視覺表達。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="想像 AI 的內在視角" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Go 歌詞動態設計](https://x.com/atomtanstudio/status/2106377491267137848) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**圍繞既有歌曲錄音製作動態歌詞。**

創作者分享 The Chemical Brothers 的 Go 歌詞影片，表示使用 Max 推理。歌曲錄音是這個動態設計任務的外部音訊輸入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Go 歌詞動態設計" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [第二支十五秒動態作品集](https://x.com/Saccc_c/status/2106376222309761094) (作者 [@Saccc_c](https://x.com/Saccc_c))

**用自由發揮的動態作品集簡報，探索新的視覺方向。**

作者分享一支新的十五秒動態作品集，並提供創作提示詞。原帖明確區分這次生成與先前的作品集。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="第二支十五秒動態作品集" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [有引導的代理實作審查](https://x.com/RobIW_dev/status/2106371025852108940) (作者 [@RobIW_dev](https://x.com/RobIW_dev))

**從構想到執行之前，先審查實作計畫是否適合現有系統。**

作者分享涵蓋系統適配、實作規劃及解釋方式的指引，說明如何審查完成的工作或決定下一步實作。附圖保留了具體規劃產物。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="有引導的代理實作審查" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [Claude 吉祥物舞蹈](https://x.com/ishuagra02/status/2106369929813594134) (作者 [@ishuagra02](https://x.com/ishuagra02))

**用跟拍吉祥物動畫，測試動作與音樂的關係。**

創作者分享 Claude 吉祥物舞蹈，表示動畫能踩準節拍。重用同一原生影片的轉發會併入這個來源，不重複計算。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="Claude 吉祥物舞蹈" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [可互動的七大奇景島嶼](https://x.com/notjazii/status/2106368606502334922) (作者 [@notjazii](https://x.com/notjazii))

**把知名建築當成互動島嶼場景中的目的地。**

來源發帖者分享以 3D 島嶼和地標建築排列的七大奇景場景。錄影具體展示如何用熟悉的紀念建築組織互動視覺環境。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="可互動的七大奇景島嶼" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [Propellerheads 音樂影片](https://x.com/atomtanstudio/status/2106353569603736009) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**以指定配樂作為延伸動態圖像的核心。**

創作者分享 Propellerheads 的 On Her Majesty’s Secret Service 音樂影片處理。既有錄音是這段動畫視覺序列的音訊輸入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="Propellerheads 音樂影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Steamboat Willie 動畫比較](https://x.com/mathisbuilds/status/2106351978691305732) (作者 [@mathisbuilds](https://x.com/mathisbuilds))

**開啟聲音，比較同一短場景的兩種動畫處理。**

作者分享標示為 Fable 與 Opus、使用 xhigh 推理強度的 Steamboat Willie 比較，並稱兩者都是一次生成。影片呈現這次具體的影音比較。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Steamboat Willie 動畫比較" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [三星堆主題影片](https://x.com/hungryturbo/status/2106339115642019904) (作者 [@hungryturbo](https://x.com/hungryturbo))

**用文化歷史題材組織動畫短片。**

作者分享三星堆主題影片，作為視覺說故事的創作。錄影提供把歷史文化題材轉成動畫簡報的具體範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="三星堆主題影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Bugatti Chiron 前後比較](https://x.com/alannnfx/status/2106323394350461031) (作者 [@alannnfx](https://x.com/alannnfx))

**重跑先前的汽車提示詞，比較建模與功能細節。**

同一作者展示 Bugatti Chiron 先前執行與重新生成的成果。前後比較錄影著重更豐富的建模和場景功能。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Bugatti Chiron 前後比較" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [GRAIN 概念短片](https://x.com/NFT_Chen/status/2106301427052360150) (作者 [@NFT_Chen](https://x.com/NFT_Chen))

**以反覆出現的視覺母題構成抽象概念影片。**

創作者分享 GRAIN 概念短片，連結種子、穀物、樹木與山景。序列以重複的形態及轉場建立敘事結構。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="GRAIN 概念短片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [Human in Transit 藝術畫廊](https://x.com/exploraX_/status/2106296439936614646) (作者 [@exploraX_](https://x.com/exploraX_))

**用互動式藝術畫廊呈現歷史視覺旅程。**

來源發帖者分享 Human in Transit，畫廊從古代一路移向現代藝術風格。錄製的介面提供在同一展示中組織多個視覺時期的參考。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="Human in Transit 藝術畫廊" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [絲綢之路視覺短片](https://x.com/hungryturbo/status/2106294812261695508) (作者 [@hungryturbo](https://x.com/hungryturbo))

**把旅行與歷史主題轉成連貫的視覺短片。**

作者分享絲綢之路主題影片。作品以動畫意象呈現歷史旅程，提供具體的創作處理範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="絲綢之路視覺短片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [四種轉型路徑簡報](https://x.com/dpkostka/status/2106272731364794757) (作者 [@dpkostka](https://x.com/dpkostka))

**把轉型框架當成簡報的組織結構。**

作者分享描述四種轉型路徑的投影片。附上的簡報圖片展示概念框架如何被整理成視覺文件。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="四種轉型路徑簡報" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [比較歷史對話語氣](https://x.com/kiyoshi_shin/status/2106268573186637883) (作者 [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**檢查語氣變化時，把較早對話紀錄與目前回應比較。**

作者要求目前模型分析較早聊天紀錄及現有文風，並對語氣變化表達不滿。附圖記錄了這項對話比較任務。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="比較歷史對話語氣" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [鴞鸚鵡可愛度測試](https://x.com/hanawo_neki/status/2106257409782288659) (作者 [@hanawo_neki](https://x.com/hanawo_neki))

**用特定角色偏好任務，比較生成動畫的風格。**

作者分享鴞鸚鵡動畫，表示在這次以可愛度為重點的比較中更喜歡 Opus。案例將負面審美回饋與實際動畫一起保留。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="鴞鸚鵡可愛度測試" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [蜘蛛人穿越十個漫畫年代](https://x.com/chetaslua/status/2106248621519978867) (作者 [@chetaslua](https://x.com/chetaslua))

**穿越多個漫畫年代時，保持同一角色可辨認。**

原始發帖者分享蜘蛛人穿越十個漫畫年代的動畫。其他重用相同影片的帖子併入這個來源，不另算作品。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="蜘蛛人穿越十個漫畫年代" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [光明會題材的虛構恐怖影片](https://x.com/badboyfoxy/status/2106241189976387799) (作者 [@badboyfoxy](https://x.com/badboyfoxy))

**把陰謀題材恐怖簡報當成虛構敘事練習。**

作者要求一支恐怖的光明會題材影片，並分享生成成果。這個主題為動畫提供的是虛構恐怖設定。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="光明會題材的虛構恐怖影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [程式製作的核科學史影片](https://x.com/imjustnewatai/status/2106238699872956427) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**結合自製程式渲染器與配樂，製作科學史解說。**

作者要求一支三分鐘 3D 影片，說明核科學如何使原子彈成為可能，之後表示使用手繪影格、自製渲染器與合成音樂。案例重點是影音製作流程。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="程式製作的核科學史影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [全民高收入解說動畫](https://x.com/markbraincell/status/2106234118514323515) (作者 [@markbraincell](https://x.com/markbraincell))

**用動畫解說傳達經濟概念。**

來源發帖者分享介紹全民高收入的動畫。錄影提供具體概念解說範例，不把片中的經濟論點當成已量測成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="全民高收入解說動畫" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [Altman 與 Amodei 爭議解說](https://x.com/imjustnewatai/status/2106204392588276065) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**以爭議事件作為動畫解說的敘事結構。**

作者要求以動畫講述 Altman 與 Amodei 的爭議，並分享成果。這個任務展示時事解說格式，而非獨立查證的歷史記錄。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="Altman 與 Amodei 爭議解說" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [Claude 吉祥物音樂影片](https://x.com/synthshareai/status/2106195060140446028) (作者 [@synthshareai](https://x.com/synthshareai))

**把吉祥物疊圖與指定影像結合，形成角色主導的音樂影片剪輯。**

來源發帖者分享真人音樂影片背景上的 Claude 吉祥物，並表示執行十二小時。可見的處理方式結合卡通疊圖與指定影像。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="Claude 吉祥物音樂影片" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [從夸克連續縮放到宇宙](https://x.com/imjustnewatai/status/2106190594775097663) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**用連續縮放，把不同科學尺度串成同一影音故事。**

作者表示以程式視覺和合成音樂製作從夸克到宇宙的縮放。錄影呈現連續的尺度轉換與連貫視覺敘事。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="從夸克連續縮放到宇宙" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [想像二〇七六年的世界](https://x.com/Layton_Gott/status/2106190496075035096) (作者 [@Layton_Gott](https://x.com/Layton_Gott))

**要求未來世界場景時，同時明確指定敘事長度。**

作者要求二十五秒影片後，分享想像二〇七六年世界的短片。其他帳號重用的相同錄影併入這個來源。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="想像二〇七六年的世界" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [下曼哈頓建築時間線](https://x.com/nroze22/status/2106183281293381661) (作者 [@nroze22](https://x.com/nroze22))

**在建築時間線介面中結合建築輪廓、年代與高度。**

作者以建築繪圖風格介面呈現下曼哈頓，展示建築年代、輪廓及高度。錄影提供具體的互動年代記概念。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="下曼哈頓建築時間線" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [甲骨文主題動畫](https://x.com/MinLiBuilds/status/2106180691344118202) (作者 [@MinLiBuilds](https://x.com/MinLiBuilds))

**用文字演變作為動畫歷史旅程的主題。**

作者分享以甲骨文開場的動畫。錄影提供以文字歷史為核心的具體視覺敘事範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="甲骨文主題動畫" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [另一支角色穿越藝術史動畫](https://x.com/imjustnewatai/status/2106162924331180510) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**讓熟悉角色持續引導觀眾穿越變化的歷史場景。**

作者要求鋼鐵人與蜘蛛人飛越歷史，並分享生成動畫。它與其他作者的角色穿越藝術史實驗是不同作品。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="另一支角色穿越藝術史動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [以程式製作 Seikilos 影音作品](https://x.com/YanqingCheng/status/2106158746938269728) (作者 [@YanqingCheng](https://x.com/YanqingCheng))

**圍繞歷史音樂文本，製作單一檔案影音作品。**

作者分享 Seikilos 墓誌銘作品，表示用單一 HTML 與 JavaScript 檔案合成畫面及音樂。歷史文本是這段程式影音序列的組織主題。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="以程式製作 Seikilos 影音作品" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [噴射機動畫比較](https://x.com/Kinzf2121/status/2106158536963330346) (作者 [@Kinzf2121](https://x.com/Kinzf2121))

**以同一飛機任務，比較飛行動畫與鏡頭追蹤。**

作者分享標示 Fable 5.1 與 Opus 的噴射機動畫比較。錄製場景提供比較飛機動作與電影式鏡頭追蹤的具體範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="噴射機動畫比較" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [模型自我介紹影片](https://x.com/devteamdrew/status/2106155815707021549) (作者 [@devteamdrew](https://x.com/devteamdrew))

**用自我介紹簡報，探索模型主題動畫。**

創作者表示以一條提示詞要求自我介紹影片，並分享成果。這個任務將模型主題敘事與動畫展示結合。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="模型自我介紹影片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [末日後卡牌遊戲原型](https://x.com/maciejkrupowies/status/2106153578029338850) (作者 [@maciejkrupowies](https://x.com/maciejkrupowies))

**先建立卡牌遊戲題材原型，再檢查戰鬥介面。**

作者分享一款末日後 Hearthstone 風格原型，描述為一次生成。原帖承認存在小問題，同時展示遊戲介面與互動。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="末日後卡牌遊戲原型" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [The Late Byte 辦公室動畫](https://x.com/rohit3a/status/2106138910648914094) (作者 [@rohit3a](https://x.com/rohit3a))

**把模型人格轉成動畫辦公室對話中的角色。**

創作者展示 The Late Byte 辦公室動畫故事，將 Opus 描繪為暴躁老闆。它與另一部 Day in the Life of Claude 是不同敘事。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="The Late Byte 辦公室動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Queens of the Stone Age 歌詞動畫](https://x.com/atomtanstudio/status/2106135196483608745) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**把指定歌曲與動態字體及圖像設計結合。**

創作者描述以 Queens of the Stone Age 錄音製作動態字體音樂影片。歌曲是指定音訊輸入，案例重點是安排歌詞與畫面。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Queens of the Stone Age 歌詞動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [分享的 Three.js 敘事場景](https://x.com/Noreply134882/status/2106116572389478746) (作者 [@Noreply134882](https://x.com/Noreply134882))

**把分享的 3D 故事片段作為敘事場景設計參考。**

發帖者分享 Three.js 敘事場景，並評論大量 token 消耗。影片作為分享的 3D 故事視覺範例保留。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="分享的 Three.js 敘事場景" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [在歷史場景中月球漫步](https://x.com/noclipepe/status/2106105810812112937) (作者 [@noclipepe](https://x.com/noclipepe))

**讓同一舞蹈母題穿越不同歷史背景與視覺風格。**

發帖者分享 Michael Jackson 月球漫步序列，場景從恐龍一路移到月球。影片作為舞蹈與風格畫廊範例保留。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="在歷史場景中月球漫步" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [詳細提示詞生成動態圖像](https://x.com/devswha/status/2106100273509007802) (作者 [@devswha](https://x.com/devswha))

**把詳細創作簡報與較短的動態設計要求比較。**

作者分享動態圖像影片，表示僅提供詳細提示詞，沒有素材、參考影片或原始檔。成果提供提示詞驅動動態設計的具體參考。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="詳細提示詞生成動態圖像" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [租賃企業網站介面](https://x.com/oalanicolas/status/2106098902965309475) (作者 [@oalanicolas](https://x.com/oalanicolas))

**用租賃業務簡報探索具體網站介面。**

創作者分享租賃企業網站介面截圖。這個案例呈現可見的頁面設計與業務展示方式。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="租賃企業網站介面" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [AGI 題材創意影片](https://x.com/AndrewOnXYZ/status/2106097745098395712) (作者 [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**用反覆採用的創作提示詞，比較敘事與視覺處理。**

作者分享以固定創作提示詞生成的 AGI 題材動畫。影片把模型的說法作為創意敘事內容。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="AGI 題材創意影片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [帶貓咪支線的藝術史](https://x.com/cherry_mx_reds/status/2106095190285144331) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**用持續出現的角色，把多個藝術時期濃縮成短篇敘事。**

創作者展示十五秒藝術史旅程，附有貓咪支線。十五秒指影片長度，而創作內容跨越多個歷史風格。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="帶貓咪支線的藝術史" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [戰鬥原型與體素場景](https://x.com/OnlyTerp/status/2106089280502210626) (作者 [@OnlyTerp](https://x.com/OnlyTerp))

**在創意編程任務中，同時檢查遊戲戰鬥及世界建構成果。**

作者分享 DMC 風格戰鬥原型與體素場景，並描述長時間生成。原帖提供兩項具體成果，可觀察遊戲機制與視覺世界設計。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="戰鬥原型與體素場景" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [網路迷因年代記](https://x.com/chetaslua/status/2106076940558082297) (作者 [@chetaslua](https://x.com/chetaslua))

**以每年的視覺風格與音樂，組織動畫時間線。**

創作者分享二〇一〇至二〇二六年熱門網路迷因動畫。每一年各有視覺風格與音樂處理，串成程式敘事。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="網路迷因年代記" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [一行要求生成粒子動態](https://x.com/devswha/status/2106072107365114186) (作者 [@devswha](https://x.com/devswha))

**先用一行動態簡報起步，再細化詳細提示詞。**

創作者分享由一行提示詞生成的粒子動畫，並表示之後想嘗試更詳細要求。它與作者較長提示詞的動態設計是不同生成。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="一行要求生成粒子動態" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [Kung-Fu Boy 動畫](https://x.com/HashmathRzz/status/2106065773336965510) (作者 [@HashmathRzz](https://x.com/HashmathRzz))

**用武術角色簡報探索動畫動作。**

作者分享歸因於 Fable 5.5 的 Kung-Fu Boy 角色動畫。附上的錄影呈現這個武術主題的具體成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="Kung-Fu Boy 動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [荷姆茲海峽辯論動畫](https://x.com/chetaslua/status/2106060047805792415) (作者 [@chetaslua](https://x.com/chetaslua))

**把辯論主題轉換為動畫敘事。**

創作者展示荷姆茲海峽的動畫辯論。這個案例記錄可見的辯論影片，不計入周邊帖子提及但未展示的其他用途。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="荷姆茲海峽辯論動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [獨角獸 SVG 風格實驗](https://x.com/atomtanstudio/status/2106057876053918127) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**用同一主題繪圖任務，觀察 SVG 風格選擇。**

作者分享受另一位創作者測試啟發的獨角獸 SVG 實驗。附圖提供可比較同一題材視覺處理的具體成果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="獨角獸 SVG 風格實驗" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [萬聖節主題動畫](https://x.com/cherry_mx_reds/status/2106056643255447590) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**為程式模型指定節慶題材，製作短篇創意動畫。**

創作者要求萬聖節主題作品，並分享生成的節慶動畫。原帖提供這個特定創作任務的原始錄影。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="萬聖節主題動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Blender CLI 野蠻人與封面](https://x.com/BoDy051/status/2106047375320166885) (作者 [@BoDy051](https://x.com/BoDy051))

**用 Blender CLI 指令探索角色建模與封面渲染。**

作者將 RPG 野蠻人角色和封面概念與 Opus 成果比較。Blender CLI 負責建構與渲染，模型提供程式指令。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Blender CLI 野蠻人與封面" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Claude 的一天](https://x.com/ishuagra02/status/2106045364868419727) (作者 [@ishuagra02](https://x.com/ishuagra02))

**圍繞持續出現的吉祥物建立日常動畫故事。**

原始發帖者分享以吉祥物為主角的 Day in the Life of Claude。這支來源影片與獨立的吉祥物舞蹈及其轉發不同。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Claude 的一天" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [3D 人類歷史](https://x.com/blueemi99/status/2106041578204655748) (作者 [@blueemi99](https://x.com/blueemi99))

**把程式場景與動畫串成人類歷史的視覺序列。**

創作者分享從古代人類到當代的 3D 影片，表示動畫與模型均以程式生成。成果提供視覺敘事範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="3D 人類歷史" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [快速動態設計短片](https://x.com/blueemi99/status/2106031355922387163) (作者 [@blueemi99](https://x.com/blueemi99))

**在精簡動態影片中評估節奏、聲音與連貫性。**

作者分享快速節奏的動態短片，將聲音及連貫性與自己的 Opus 成果比較。判斷反映創作者對這次作品的使用經驗。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="快速動態設計短片" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [自由發揮的複雜 3D 創作](https://x.com/cocoloba_/status/2106029181607772413) (作者 [@cocoloba_](https://x.com/cocoloba_))

**用開放式創作要求探索複雜的 3D 構圖。**

創作者詢問模型有空時會做什麼，並分享形成的 3D 作品。原帖描述生成構圖包含許多獨立部件。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="自由發揮的複雜 3D 創作" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [火柴人打鬥動畫](https://x.com/HelaliBillel/status/2106028502763900944) (作者 [@HelaliBillel](https://x.com/HelaliBillel))

**用具體戰鬥動畫要求觀察節奏與動作。**

創作者要求一段火柴人打鬥動畫影片，並分享成果。錄影提供這項戰鬥動畫任務的具體範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="火柴人打鬥動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [一條提示詞的 UI 動態序列](https://x.com/iancarscadden/status/2106018048792789360) (作者 [@iancarscadden](https://x.com/iancarscadden))

**以一份動畫簡報探索 UI 動態序列。**

作者分享 UI 動態序列，描述為一次生成、約六至七分鐘完成。錄影呈現這項要求形成的視覺序列。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="一條提示詞的 UI 動態序列" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [SCP-8517 虛構動畫](https://x.com/eviljoker88/status/2106003621402005816) (作者 [@eviljoker88](https://x.com/eviljoker88))

**用 SCP 題材作為動畫故事簡報。**

創作者展示 SCP-8517 主題動畫，並將製作歸因於 Fable 5.5。案例聚焦虛構敘事及其可見動畫。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="SCP-8517 虛構動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [水彩秋日動畫](https://x.com/ishuagra02/status/2106000055706784118) (作者 [@ishuagra02](https://x.com/ishuagra02))

**為動畫明確指定季節題材與水彩處理。**

作者分享水彩風格的秋日動畫。作品具體展示如何把季節主題與特定視覺媒材結合。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="水彩秋日動畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [程序化人偶舞台](https://x.com/HelaliBillel/status/2105988689088196785) (作者 [@HelaliBillel](https://x.com/HelaliBillel))

**觀察類人偶角色如何在舞台場景中活動。**

作者分享程序化人偶舞台動畫，並在討論中提及 Blender。案例重點是可見的舞台角色與動畫。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="程序化人偶舞台" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [瀏覽器中的鵜鶘騎車](https://x.com/slimcat0101/status/2105988654636380444) (作者 [@slimcat0101](https://x.com/slimcat0101))

**在瀏覽器執行角色動態成果，觀察渲染場景。**

創作者要求鵜鶘騎自行車，並錄製 HTML 在瀏覽器中執行的成果。這是會動的瀏覽器場景，與靜態 SVG 繪圖測試不同。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="瀏覽器中的鵜鶘騎車" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [宇宙看見自己](https://x.com/l_mejiaC/status/2105988529671360673) (作者 [@l_mejiaC](https://x.com/l_mejiaC))

**用連續視覺旅程，把遙遠尺度串成同一敘事。**

創作者呈現從大爆炸一路到人眼的連續序列。作者描述影片的畫面與音樂由執行期程式碼產生。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="宇宙看見自己" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [獨立噴射機動畫測試](https://x.com/AI_Screening/status/2105988448612135176) (作者 [@AI_Screening](https://x.com/AI_Screening))

**重複飛機動畫任務，觀察具體輸出。**

作者看到路由討論後，嘗試噴射機動畫任務並分享成果。錄影為這個飛機範例提供獨立來源。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="獨立噴射機動畫測試" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [最初的自由動態短片](https://x.com/Saccc_c/status/2105985484472377531) (作者 [@Saccc_c](https://x.com/Saccc_c))

**以簡短開放式提示詞探索動態設計。**

創作者分享最初的動態設計短片，表示以一條提示詞生成。它是較早的獨立成果，與後來十五秒作品集不同。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="最初的自由動態短片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [以程式呈現文明](https://x.com/ziwenxu_/status/2105983571848741045) (作者 [@ziwenxu_](https://x.com/ziwenxu_))

**把文明史簡報轉成程式動畫敘事。**

作者要求從文明起源到當代的影片，並分享成果。創作者表示這段程式視覺作品沒有使用現成影像或素材。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="以程式呈現文明" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [晶片至伺服器縮放比較](https://x.com/SPAC89/status/2105968361725202591) (作者 [@SPAC89](https://x.com/SPAC89))

**在晶片至伺服器的縮放任務中比較寫實感與連續性。**

作者比較 Fable XHigh 與 GPT Sol Ultra 的寫實縮放序列，並討論速度與額度消耗。原帖比較的是不同訂閱等級下的特定執行。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="晶片至伺服器縮放比較" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [月球旅行動畫計畫](https://x.com/IgorGomezC/status/2105963552024506565) (作者 [@IgorGomezC](https://x.com/IgorGomezC))

**用多個程式模型探索個人的動畫構想。**

創作者在討論 Fable 與 Opus 實驗時，分享個人月球旅行動畫計畫。附上的作品是這次創意探索的具體成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="月球旅行動畫計畫" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [日式體素場景比較](https://x.com/vikktorrrre/status/2105955048018588084) (作者 [@vikktorrrre](https://x.com/vikktorrrre))

**用同一場景提示詞比較細節、霧氣與畫面清晰度。**

作者以相同日式體素場景提示詞比較目前的 Fable 與 Opus。觀察針對這些特定成果的清晰度、霧氣及審美處理。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="日式體素場景比較" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [Steaming the Frontier 影音短片](https://x.com/sdmat123/status/2105929299878703520) (作者 [@sdmat123](https://x.com/sdmat123))

**把 Steamboat 風格視覺簡報與聲音結合成影音短片。**

創作者分享帶聲音的動畫 Steaming the Frontier。它與其他創作者獨立製作的 Steamboat 風格作品保持不同來源。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="Steaming the Frontier 影音短片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [超人穿越多種美術風格](https://x.com/Mr_Salio/status/2105925979466052051) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**讓同一角色在連續動畫中穿越不同美術風格。**

創作者表示先前的超人範例啟發了新的生成，並分享自己的成果。不同畫面使它成為獨立創作，而不是轉發。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="超人穿越多種美術風格" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Cupcake 風格頭目戰原型](https://x.com/maciejkrupowies/status/2105914965387321785) (作者 [@maciejkrupowies](https://x.com/maciejkrupowies))

**建立橫向卷軸頭目戰原型，觀察戰鬥成果。**

作者分享 Cupcake 風格頭目戰原型，表示不到十分鐘一次生成。附上的錄影展示遊戲戰鬥序列。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Cupcake 風格頭目戰原型" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [太陽位置變化的帆船](https://x.com/popat_kunj/status/2105907935490752822) (作者 [@popat_kunj](https://x.com/popat_kunj))

**用航行場景探索天空、水面與太陽位置變化。**

創作者分享太陽位於不同位置的 3D 帆船場景，並連結互動產物。這項視覺任務將船、天空與水面結合。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="太陽位置變化的帆船" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Paracortex 與 Pi 更新影片](https://x.com/RobIW_dev/status/2105894547796476225) (作者 [@RobIW_dev](https://x.com/RobIW_dev))

**把產品更新轉成短篇動態公告。**

作者把 Paracortex 與 Pi 更新轉成二十五秒動態設計影片，並在原帖附提示詞。作品展示視覺化產品溝通方式。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Paracortex 與 Pi 更新影片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Curio 2.0 網站宣傳片](https://x.com/voltwake/status/2105884775982485642) (作者 [@voltwake](https://x.com/voltwake))

**圍繞既有網站發布製作程式宣傳短片。**

創作者描述為 Curio 2.0 製作發布宣傳片，結合程式視覺、鏡頭與音樂。原帖分享形成的網站宣傳影片。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Curio 2.0 網站宣傳片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [想像中的 Hugging Face 3D 故事](https://x.com/chetaslua/status/2105884276864782557) (作者 [@chetaslua](https://x.com/chetaslua))

**結合模型程式碼、渲染與音訊工具製作虛構影片。**

創作者分享以模型程式碼、Blender 及 ElevenLabs API 製作的想像 Hugging Face 故事。Blender 負責建構與渲染，ElevenLabs 提供外部音訊。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="想像中的 Hugging Face 3D 故事" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [Claude for Chrome 操作 JS Paint](https://x.com/BtwIUseSystemd/status/2105861662112923849) (作者 [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**要求瀏覽器代理僅使用應用程式本身工具繪圖。**

作者要求 Claude for Chrome 只用 JS Paint 工具畫人，並分享成果。瀏覽器互動及繪畫應用程式都是明確的任務組成。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="Claude for Chrome 操作 JS Paint" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [靜態鵜鶘騎車 SVG](https://x.com/olddonkeyblog/status/2105842745189556672) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**用獨立完整 SVG 要求，測試精細靜態繪圖。**

創作者要求單一、自包含的鵜鶘騎自行車 SVG，並分享靜態圖片。這是與騎車動畫不同的繪圖任務。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="靜態鵜鶘騎車 SVG" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [BlockBench MCP 與 Minecraft 技能](https://x.com/TOPSTR1X/status/2105839618872738138) (作者 [@TOPSTR1X](https://x.com/TOPSTR1X))

**生成遊戲角色時，提供建模工具與風格技能。**

作者提供 BlockBench MCP 和自訂 Minecraft 建模及上色技能，再分享角色成果。這些工具與風格指引都是流程的明確輸入。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="BlockBench MCP 與 Minecraft 技能" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [單一 HTML 檔案的 Dig Dug](https://x.com/imjustnewatai/status/2105831117677084841) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**重製精簡瀏覽器遊戲時，把單一 HTML 當成交付目標。**

創作者要求在單一 HTML 檔案中重製 Dig Dug，並分享遊戲錄影。原帖表示這次製作來自一條提示詞。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="單一 HTML 檔案的 Dig Dug" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [機械章魚 SVG](https://x.com/SEO/status/2105812236774297943) (作者 [@SEO](https://x.com/SEO))

**用機械生物觀察 SVG 設計的細節與動作。**

作者分享帶機械細節的章魚 SVG 動畫。錄影提供以小型動態零件為核心的向量設計範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="機械章魚 SVG" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [Humanity Walks 藝術風格之旅](https://x.com/l_mejiaC/status/2105801379956850793) (作者 [@l_mejiaC](https://x.com/l_mejiaC))

**讓固定角色穿越一連串歷史視覺風格。**

原始創作者呈現約七十四秒、穿越二十幅藝術畫面的連續步行，並表示音樂以程式生成。每個分界將角色與場景轉成不同風格。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="Humanity Walks 藝術風格之旅" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [開放式黑洞場景](https://x.com/rohit3a/status/2105786053412208835) (作者 [@rohit3a](https://x.com/rohit3a))

**用開放式創作簡報探索黑洞視覺化。**

創作者詢問模型會做什麼來讓自己驚豔，並分享黑洞場景。這是自由視覺探索，而不是預先指定的介面建置。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="開放式黑洞場景" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [極光水母動畫比較](https://x.com/SPAC89/status/2105783511433318451) (作者 [@SPAC89](https://x.com/SPAC89))

**比較兩種水母動畫成果的形變與動作。**

作者比較 Fable XHigh 與 GPT Sol Ultra 的極光水母動畫，並討論額度使用。成果來自不同訂閱等級。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="極光水母動畫比較" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Nintendo Switch 拼接與啟動 SVG](https://x.com/ishuagra02/status/2105779174921359470) (作者 [@ishuagra02](https://x.com/ishuagra02))

**在同一 SVG 動畫中結合控制器移動與啟動序列。**

創作者分享 Nintendo Switch SVG，控制器先拼接，再播放啟動標誌動畫。原帖回報這次執行一分三十九秒，成本為 1.34 美元。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Nintendo Switch 拼接與啟動 SVG" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [The Loom 互動 3D 場景](https://x.com/Mr_Salio/status/2105774088492916757) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**把景觀與建築作為同一互動 3D 頁面探索。**

作者展示具有建築及景觀的 The Loom 互動場景。附上的錄影提供這次測試的具體頁面成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="The Loom 互動 3D 場景" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [同一提示詞的動態圖形設計短片](https://x.com/mesmerlord/status/2105758042830549235) (作者 [@mesmerlord](https://x.com/mesmerlord))

**比較同一提示詞生成的兩支短片如何安排視覺焦點與節拍同步。**

作者分享了 Fable 5.5 早期測試中同一提示詞生成的兩支動態圖形設計短片，並謹慎表示，相較於一次 Opus 執行結果，畫面焦點可能更清晰、節拍同步也更好。兩段原貼文影片一併保留。

```
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

[@shneural](https://x.com/shneural/status/2103151003272962130)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="同一提示詞的動態圖形設計短片" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29b80ef5ba92b029630a1628.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0da5945bc240b424bfebbd9.jpg" alt="同一提示詞的動態圖形設計短片" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [更乾淨但較缺乏深度的景物](https://x.com/eviljoker88/status/2105755840175034447) (作者 [@eviljoker88](https://x.com/eviljoker88))

**比較生成場景時，保留負面審美回饋。**

作者分享並排的日式場景比較，雖然另一成果較乾淨，仍更喜歡 Opus 輸出的縱深。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="更乾淨但較缺乏深度的景物" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [日式場景的好壞參半結果](https://x.com/eviljoker88/status/2105755408342126936) (作者 [@eviljoker88](https://x.com/eviljoker88))

**記錄好壞參半的回饋，不把首次比較當成明確勝負。**

作者分享初次日式場景比較，表示結果好壞參半。附圖保留支撐這項審美回饋的具體成果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="日式場景的好壞參半結果" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [控制器 SVG 比較](https://x.com/notjazii/status/2105751542498464169) (作者 [@notjazii](https://x.com/notjazii))

**在類似視覺任務下，比較前後控制器繪圖。**

作者以比較圖片分享前後控制器 SVG 成果。案例重點是繪圖與呈現的可見變化，而非整體模型排名。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="控制器 SVG 比較" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [工業裝置場景](https://x.com/RayaneRachid_/status/2105744517735354410) (作者 [@RayaneRachid_](https://x.com/RayaneRachid_))

**用機械裝置作為聚焦的 3D 場景設計任務。**

創作者分享 3D 工業裝置場景，稱其為自己最好的一次生成。附圖提供機械構圖的具體參考。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="工業裝置場景" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [巨型帶殼鰓蟲重建](https://x.com/Josh67Joshua/status/2105739832563769697) (作者 [@Josh67Joshua](https://x.com/Josh67Joshua))

**用具體生物描述探索兩輪提示詞的重建成果。**

作者分享巨型帶殼鰓蟲繪圖，表示以兩條提示詞完成。圖片呈現這項生物設計任務的可見成果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="巨型帶殼鰓蟲重建" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [兩條提示詞的 GameCube 控制器](https://x.com/marmaduke091/status/2105735266032095349) (作者 [@marmaduke091](https://x.com/marmaduke091))

**用熟悉的控制器，觀察兩條提示詞的繪圖成果。**

作者分享 GameCube 控制器繪圖，表示使用兩條提示詞。這張靜態控制器圖片與 Xbox 及其他控制器演示不同。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="兩條提示詞的 GameCube 控制器" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [為 X 帖子編輯截圖](https://x.com/chetaslua/status/2105733677003292983) (作者 [@chetaslua](https://x.com/chetaslua))

**觀察助理如何調整截圖以配合社群帖子。**

創作者分享為 X 帖子準備的截圖編輯，表示助理未經明確要求便執行。附圖是這次編輯的可見成果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="為 X 帖子編輯截圖" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [前後兩版體素櫻花](https://x.com/kdnbmb/status/2105704791049412755) (作者 [@kdnbmb](https://x.com/kdnbmb))

**以同一視覺題材比較連續兩次體素場景成果。**

發帖者分享體素櫻花島的兩個版本。並排圖片記錄場景前後兩版可見的設計差異。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="前後兩版體素櫻花" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [SHADERKIN 布料介面原型](https://x.com/mszzz0011/status/2106025576972853642) (作者 [@mszzz0011](https://x.com/mszzz0011))

**在介面原型中，同時探索布料效果與可調控制。**

作者分享帶布料效果與參數控制的 SHADERKIN 原型，描述為一次生成。錄影展示介面及動態成果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="SHADERKIN 布料介面原型" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [分享的金色時鐘介面動畫](https://x.com/AISuperDomain/status/2106396754539360272) (作者 [@AISuperDomain](https://x.com/AISuperDomain))

**用時鐘主題動畫作為介面構圖參考。**

發帖者展示金色時鐘主題前端動畫。附上的片段提供觀察介面構圖、時鐘母題與動態呈現的參考。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="分享的金色時鐘介面動畫" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [Before There Was Anything 敘事影片](https://x.com/crowqnt/status/2106146218846081435) (作者 [@crowqnt](https://x.com/crowqnt))

**透過分享的動畫，探索宇宙與人類敘事。**

發帖者分享描繪宇宙與人類的敘事影片 Before There Was Anything。作品作為視覺說故事範例保留。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="Before There Was Anything 敘事影片" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [分享的藍色粒子漩渦](https://x.com/AISuperDomain/status/2105846981776003107) (作者 [@AISuperDomain](https://x.com/AISuperDomain))

**在分享的漩渦視覺化中觀察粒子運動與構圖。**

發帖者分享藍色粒子漩渦動畫。附上的片段提供觀察粒子運動、視覺結構與構圖的具體範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="分享的藍色粒子漩渦" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [兩次修改後的多面板介面](https://x.com/ZorroOfMorocco/status/2106547078235095485) (作者 [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**透過修改循環細化視覺介面，不停在第一次成果。**

作者分享完成的多面板介面，表示約三小時、經兩次修改。附上的截圖展示最終視覺設計。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="兩次修改後的多面板介面" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [渲染場景中的動物疊疊樂](https://x.com/legit_api/status/2117237103289315574) (作者 [@legit_api](https://x.com/legit_api))

**觀察靜態構圖如何平衡多個角色與不同材質。**

原帖分享熊、熊貓與北極熊堆疊的場景，署名給 Discord 上的 yuruzuu，並回報執行二十一分鐘。公開帖子作為這個視覺成果的分享來源保留。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="渲染場景中的動物疊疊樂" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [四種開放世界 RPG 成果比較](https://x.com/noclipepe/status/2117222592536789149) (作者 [@noclipepe](https://x.com/noclipepe))

**在同一創作任務中比較遊戲呈現、戰鬥與碰撞行為。**

創作者展示標示 Fable 5.5、GPT-6.2 Astra、Opus 5.5 和 Fable 5.1 的四次單提示詞 RPG 嘗試，評論光照、戰鬥、背包、碰撞及角色卡住的差異。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="四種開放世界 RPG 成果比較" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [兩段前端動畫比較](https://x.com/leo114119/status/2117209849842761983) (作者 [@leo114119](https://x.com/leo114119))

**把動畫片段放在一起，觀察場景設計與視覺細節。**

原帖並列標示 Astra 與 Fable 的程式生成動畫，著重細節和腳本設計，並明確將 Fable 動畫署名給 @chetaslua。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="兩段前端動畫比較" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [以程式生成的苔蘚機器人影片](https://x.com/chetaslua/status/2117169796290916732) (作者 [@chetaslua](https://x.com/chetaslua))

**用動畫簡報探索以程式建立的完整電影式場景。**

創作者分享森林與機器人動畫，描述為一次生成的程式影片。原帖引導讀者查看截圖中的提示詞，並與其他嘗試比較。

另一則貼文展示了單獨報告的 Opus 5.5 對照執行。 [@AnikaCodes](https://x.com/AnikaCodes) · [相關作品](https://x.com/AnikaCodes/status/2117222374642946297)

據作者介紹，相關的 GPT-6 Astra Max 執行在流程中使用了生成圖片。將其與原短片並列展示，可以看出兩種製作方法的差異。 [@rubenssoto_ai](https://x.com/rubenssoto_ai) · [相關比較](https://x.com/rubenssoto_ai/status/2117707344704352691)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="以程式生成的苔蘚機器人影片" width="760"></a></td><td valign="top"><p>另一則貼文展示了單獨報告的 Opus 5.5 對照執行。</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="以程式生成的苔蘚機器人影片" width="760"></a></td><td valign="top"><p>GPT-6 Astra Max</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/25b0cfcdb1fdda22ba6aa9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/75f37c74099d5b9ba1ad0ddc.jpg" alt="GPT-6 Astra Max" width="760"></a></td></tr></table>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [重新製作貨櫃港模擬](https://x.com/anxuanng/status/2117124831279972812) (作者 [@anxuanng](https://x.com/anxuanng))

**重做舊場景時，保留專案脈絡以便視覺比較。**

作者發布另一版貨櫃港場景，引用先前以 Blender 和 Three.js 製作的模擬，其起重機、船隻、車輛與貨櫃皆為策略遊戲式環境建模。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="重新製作貨櫃港模擬" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [重新製作機場停機坪場景](https://x.com/anxuanng/status/2117096574878921119) (作者 [@anxuanng](https://x.com/anxuanng))

**把修改後的機場場景與舊專案及素材流程比較。**

作者回到機場停機坪場景，引用先前的 Blender 和 Three.js 模擬，分享飛機、服務車輛與航廈設施的新錄影。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="重新製作機場停機坪場景" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [鵜鶘騎車穿越抽象 3D 世界](https://x.com/xiax0603/status/2116960224829665543) (作者 [@xiax0603](https://x.com/xiax0603))

**用騎車主題觀察不同空間環境之間的轉場。**

原帖分享鵜鶘與自行車動畫，穿過幾何碎片和抽象數位環境，最後從眼睛拉遠。序列提供獨立的場景轉換演示。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="鵜鶘騎車穿越抽象 3D 世界" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [歷史帆船場景](https://x.com/abhinavflac/status/2116945827738665060) (作者 [@abhinavflac](https://x.com/abhinavflac))

**在船隻場景中觀察水面、光照與環境構圖。**

原帖分享歷史帆船場景，描述為零樣本互動成果。附上的錄影提供船隻及周圍水面的具體視覺樣本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="歷史帆船場景" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [與 Carbon 比較騎車及步態](https://x.com/AI_Screening/status/2116934172757660014) (作者 [@AI_Screening](https://x.com/AI_Screening))

**用成對視覺成果比較角色運動與場景建構。**

作者把標示 Fable 與 Carbon 的騎車者和斑馬範例放入合成影片，評論兩個檢查點表現接近。並排畫面讓讀者觀察具體動作樣本。

先前單獨發布的騎車人物對比，也與合成影片一併收錄。 [@AI_Screening](https://x.com/AI_Screening) · [相關作品](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="與 Carbon 比較騎車及步態" width="760"></a></td><td valign="top"><p>先前單獨發布的騎車人物對比，也與合成影片一併收錄。</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="與 Carbon 比較騎車及步態" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [汽水瓶展示](https://x.com/abhinavflac/status/2116919086521499730) (作者 [@abhinavflac](https://x.com/abhinavflac))

**用精簡產品渲染片段觀察材質、形狀與呈現。**

原帖分享汽水瓶展示，描述為一次生成的路由成果。案例保留可見的瓶身片段，不採用標題中不一致的品牌名稱。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="汽水瓶展示" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [與 Astra 比較鵜鶘動作](https://x.com/Octoberry/status/2116918967558095131) (作者 [@Octoberry](https://x.com/Octoberry))

**觀看成對鵜鶘片段，比較寫實感、色彩及動作選擇。**

發帖者並列標示 Fable 與 Astra 的鵜鶘場景，評論寫實感與色彩。比較錄影把兩種視覺處理保留在一起。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="與 Astra 比較鵜鶘動作" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [程式動畫的動態設計簡報](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (作者 [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**要求動畫標題或產品開場時，以具體設計簡報起步。**

原帖分享一份動態設計簡報截圖，涵蓋開場、動態標誌、標題和 3D 場景，並提議搭配 Claude 使用。來源圖片保留完整指示。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="程式動畫的動態設計簡報" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [由照片參考製作體素肖像](https://x.com/chetaslua/status/2116912822806520027) (作者 [@chetaslua](https://x.com/chetaslua))

**觀察體素肖像如何保留參考照片中可辨識的特徵。**

創作者把 Sam Altman 照片與體素肖像並列，描述為一次生成成果。並排圖片同時提供參考與轉繪版本。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="由照片參考製作體素肖像" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [與 Opus 比較飛行鵜鶘場景](https://x.com/leo114119/status/2116901575490929109) (作者 [@leo114119](https://x.com/leo114119))

**用有趣物件排列比較構圖與動畫選擇。**

原帖上下排列標示 Fable 與 Opus 的自行車騎在飛行鵜鶘上的片段。合成畫面將 Fable 片段署名給 @notjazii，並保留兩種處理。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="與 Opus 比較飛行鵜鶘場景" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [Morning Ride 鵜鶘網頁場景](https://x.com/leo114119/status/2116893571739775220) (作者 [@leo114119](https://x.com/leo114119))

**觀察海邊騎車場景的角色細節與周圍網頁呈現。**

作者分享 Morning Ride 頁面中的 3D 鵜鶘騎車場景，著重羽毛、腳部、自行車細節與海邊背景。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="Morning Ride 鵜鶘網頁場景" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [同一提示詞的不同風格場景](https://x.com/notjazii/status/2116893197939224714) (作者 [@notjazii](https://x.com/notjazii))

**讓每個模型自行選擇風格，再比較場景構圖。**

作者表示以相同提示詞測試兩個模型，同時允許各自選擇視覺風格。影片並列不同場景構圖與細節程度。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="同一提示詞的不同風格場景" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [鵜鶘、自行車與馬的構圖](https://x.com/abhinavflac/status/2116881397986288017) (作者 [@abhinavflac](https://x.com/abhinavflac))

**測試動畫如何在同一場景安排多個互動主體。**

原帖分享一隻帶著自行車飛行的鵜鶘，下方有馬奔跑。片段提供不尋常的多物件構圖與動作範例。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="鵜鶘、自行車與馬的構圖" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [參考推文啟發的等角場景](https://x.com/chetaslua/status/2116878661035106515) (作者 [@chetaslua](https://x.com/chetaslua))

**用指定參考帖子引導新場景，而不是重做一般範例。**

創作者表示只引用一則 Post Humans 推文作為參考，並分享生成的等角場景。片段呈現帶季節控制的農場式構圖。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="參考推文啟發的等角場景" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [鵜鶘自行車的機械特寫](https://x.com/NFT_Chen/status/2116869725703782507) (作者 [@NFT_Chen](https://x.com/NFT_Chen))

**觀察騎車主題中的齒盤運動、羽毛細節與鏡頭移動。**

原帖分享鵜鶘在水邊騎自行車的特寫。錄影在自行車機械、鳥頭及較廣的木棧道騎行畫面之間切換。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="鵜鶘自行車的機械特寫" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [自行車騎在鵜鶘上](https://x.com/notjazii/status/2116861637890379891) (作者 [@notjazii](https://x.com/notjazii))

**反轉常見主體關係，測試動畫中的空間構圖。**

創作者分享自行車騎在鵜鶘上的動畫。片段把自行車放在飛鳥上方，變化了熟悉的鵜鶘騎自行車題目。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="自行車騎在鵜鶘上" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [與 Carbon 比較鵜鶘 SVG 風格](https://x.com/leo114119/status/2116652334734332212) (作者 [@leo114119](https://x.com/leo114119))

**比較寫實與插畫風格，不把不同美學當成單一總排名。**

原帖把 Carbon 與 Fable 的鵜鶘騎車成果放在一起。作者對照漫畫式渲染與較寫實的處理，指出風格差異使比較更複雜。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="與 Carbon 比較鵜鶘 SVG 風格" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [卡通藍鳥騎車場景](https://x.com/birdabo/status/2116553049183560012) (作者 [@birdabo](https://x.com/birdabo))

**觀察熟悉卡通角色在騎車構圖中的呈現。**

原帖分享藍色卡通鳥在水岸騎自行車的圖片，標示 Fable 5.5 Max。圖片作為具體靜態視覺樣本保留。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="卡通藍鳥騎車場景" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [林間道路鵜鶘騎車截圖](https://x.com/leo114119/status/2116154940364374269) (作者 [@leo114119](https://x.com/leo114119))

**在瀏覽器渲染場景中，觀察羽毛、腳部與自行車結構。**

發帖者分享鵜鶘沿林間道路騎車的瀏覽器截圖，著重羽毛材質、腳部及自行車細節。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="林間道路鵜鶘騎車截圖" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [與 Carbon 比較火柴人戰鬥](https://x.com/leo114119/status/2116084152986656933) (作者 [@leo114119](https://x.com/leo114119))

**在成對動畫樣本中比較打鬥編排與動作。**

比較錄影標示 Fable 5.1 High 與 Carbon。作者討論火柴人打鬥動畫的相對品質。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="與 Carbon 比較火柴人戰鬥" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [早期測試的鵜鶘 SVG 參考](https://x.com/ChrisGPT/status/2115872567122608591) (作者 [@ChrisGPT](https://x.com/ChrisGPT))

**觀察風格化及自行車結構時，保留有來源連結的參考。**

發帖者介紹鵜鶘騎車圖片，引用一則早期測試帖子，該帖將成果署名給 Discord 上的 kostikz。案例保留參考圖與署名脈絡。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="早期測試的鵜鶘 SVG 參考" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [跨模型 SVG 測試中的鵜鶘參考](https://x.com/AdamHoltererer/status/2115858542221492300) (作者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**把 Fable 參考與周圍 SVG 測試脈絡放在一起。**

發帖者在自己的 Mistral Large 4 SVG 測試討論串下，加入鵜鶘騎車圖片作為 Fable 參考，供跨模型視覺觀察。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="跨模型 SVG 測試中的鵜鶘參考" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [與 Carbon 比較自行車 SVG 細節](https://x.com/insanekrishnaa/status/2115833723342250186) (作者 [@insanekrishnaa](https://x.com/insanekrishnaa))

**比較車籃、背景及羽毛材質等個別視覺特徵。**

原帖比較 Fable 與 Carbon 的鵜鶘騎車圖片，討論車籃設計、背景細節及羽毛材質。它是一項具體視覺評論，而非廣泛任務測試。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="與 Carbon 比較自行車 SVG 細節" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [3D 峽谷聚落](https://x.com/Mr_Salio/status/2115813400915714177) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**用聚落場景觀察環境細節與空間構圖。**

原帖分享寬廣的峽谷聚落場景，將錄影呈現為新 Claude 檢查點演示。片段展示可見的建築、景觀及場景構圖。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="3D 峽谷聚落" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [與 Opus 比較控制器細節](https://x.com/notjazii/status/2115808169075351632) (作者 [@notjazii](https://x.com/notjazii))

**比較成對控制器繪圖的形狀、按鍵與細節程度。**

作者並列標示 Fable 與 Opus 的控制器繪圖，強調上方版本的細節量。並排圖片保留這次比較。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="與 Opus 比較控制器細節" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [每週網站 SEO 稽核流程](https://x.com/cleeeeeeeeement/status/2115488774423773267) (作者 [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**把網站轉成有優先順序的 SEO 計畫及定期排名檢視流程。**

創作者表示建立了一套系統，可接收網站、識別競爭者與關鍵字，並產生有優先順序的 SEO 行動計畫。短錄影配合每週排名追蹤與執行的描述。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="每週網站 SEO 稽核流程" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [在 Opus 動態設計重用 Fable 素材](https://x.com/chetaslua/status/2115145163542790170) (作者 [@chetaslua](https://x.com/chetaslua))

**結合模型與工具時，區分素材創作及動態設計組裝。**

創作者分享 Opus 5.5 的 Tesla Roadster 動態設計，使用據稱先前由 Fable 生成的素材。引用的早期流程提及 Blender 中的 Python、ElevenLabs 及指定發布影片。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="在 Opus 動態設計重用 Fable 素材" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [曼陀羅與幾何形體應用程式](https://x.com/ZMinimalistYogi/status/2114600083165434189) (作者 [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**把聚焦的幾何構想做成可供創作探索的互動應用。**

創作者表示與 Fable 5.1 對話三小時，製作可生成曼陀羅、zome、阿基米德立體及蓮花形幾何壇城的應用，之後在個人網站分享。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="曼陀羅與幾何形體應用程式" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Three.js 自行車騎士](https://x.com/AI_Screening/status/2114266369248354357) (作者 [@AI_Screening](https://x.com/AI_Screening))

**觀察騎車場景中的姿勢、自行車結構與協調動作。**

創作者分享 Three.js 自行車騎士成果。錄影提供具體運動樣本，騎士周圍有橋梁與水岸景觀。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Three.js 自行車騎士" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [FrontierCS 2 評測快照](https://x.com/wenhaocha1/status/2115613415641354262) (作者 [@wenhaocha1](https://x.com/wenhaocha1))

**利用附原始來源連結的基準測試圖表，比較 Fable 5.1 與其他模型。**

作者將 Fable 5.1 加入 FrontierCS 2 的任務通過率圖表，並與其他模型一同展示所報告的結果。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="FrontierCS 2 評測快照" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [三模型斑馬動畫對比](https://x.com/AI_Screening/status/2115849659797373038) (作者 [@AI_Screening](https://x.com/AI_Screening))

**將附有模型標籤的三個輸出放在一起，對比斑馬奔跑任務的結果。**

作者並排展示標為 Fable 5.5、Opus 5.5 與 Gemini 4 Argon 的斑馬動畫。分享的影片提供了三個輸出的具體步態樣本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="三模型斑馬動畫對比" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [評論日文長篇文章](https://x.com/AM09_21/status/2106670042184356156) (作者 [@AM09_21](https://x.com/AM09_21))

**要求模型診斷生成式日文文章的可讀性問題。**

作者表示詢問為何 Opus 的日文長文難讀。回覆指出類似英文的語法、詞語重複與表面修飾，構成一個具體的文章評論流程。

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [以範例引導技術簡報](https://x.com/mt_moco/status/2106665038375522791) (作者 [@mt_moco](https://x.com/mt_moco))

**先提供範例，再要求製作技術簡報。**

作者表示提供幾份範例簡報後，得到可用的技術 PowerPoint。這次經驗把範例引導的提示方式，與特定簡報任務的文件結構改善連結起來。

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [比較音樂整體連貫性](https://x.com/AM09_21/status/2106573080214770011) (作者 [@AM09_21](https://x.com/AM09_21))

**評估生成音樂時，分別比較局部細節與整體連貫性。**

作者從音符、旋律與轉折比較模型生成的樂曲，區分局部一致性和整體音樂結構。這是一項以聆聽為基礎的作曲品質評估。

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [提早宣告完成與較弱的設計](https://x.com/johntitorIII/status/2106442876506747353) (作者 [@johntitorIII](https://x.com/johntitorIII))

**接受代理的完成報告前，先對照任務要求檢查交付成果。**

作者表示連續數日測試中，出現未完成任務被標記完成，以及設計成果不如其他模型的情形。案例將提早結束與設計品質記錄為實際失敗模式。

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [令人不適的魷魚藝術結果](https://x.com/hanawo_neki/status/2106271036094415186) (作者 [@hanawo_neki](https://x.com/hanawo_neki))

**開放式美術要求得到不喜歡的風格時，補充具體審美偏好。**

作者表示要求任意魷魚藝術品後，得到讓自己不舒服的密集群聚細節。這是一個開放式視覺要求與個人審美不合的經驗。

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [藍圖風格動態設計](https://x.com/DavidayoAI/status/2106054662063325638) (作者 [@DavidayoAI](https://x.com/DavidayoAI))

**把藍圖美學當成快速動畫的視覺方向。**

作者表示要求一段快速動畫，約十五分鐘後得到藍圖風格成果。完整作品連結至 YouTube。

[相關作品](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [體素櫻花場景中的鳥魚](https://x.com/xodud_rkd/status/2105876716472447046) (作者 [@xodud_rkd](https://x.com/xodud_rkd))

**在體素景觀中探索會動的野生動物。**

作者描述有飛鳥與池中魚的體素櫻花場景，並連結互動產物。分享頁面是這個場景對應的成果。

[相關作品](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [角色生成失敗回饋](https://x.com/doof1789559/status/2105874208458752227) (作者 [@doof1789559](https://x.com/doof1789559))

**在成功視覺演示旁，也記錄負面角色生成經驗。**

作者回報角色生成成果不佳，並明確承認可能是自己的方法造成。原帖為評估角色任務的讀者保留具體負面經驗。

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [附執行時間與成本的鵜鶘 SVG](https://x.com/AnonymerNutze12/status/2105740440385499295) (作者 [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**把繪圖產物與創作者的時間及成本觀察放在一起。**

作者連結鵜鶘 SVG HTML 產物，並回報這次嘗試的執行時間和成本。連結產物就是原帖指向的具體成果。

[相關作品](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [手機遠端管理 Claude Code 群集](https://x.com/beistnormie/status/2106546741000417781) (作者 [@beistnormie](https://x.com/beistnormie))

**探索以手機遠端監督程式代理群集的方式。**

作者表示旅行時，以手機遠端使用 Claude Code 群集編程。原帖提供個人流程經驗，而非專案教學或實作步驟。

Type: Integration | Date: 2026-10-04

---

<a id="case-280"></a>
### Case 280: [高山湖泊上空的銀河](https://x.com/hakmgpt/status/2118178083983573492) (作者 [@hakmgpt](https://x.com/hakmgpt))

**觀察山巒倒影與移動夜空結合的長鏡頭。**

這段 92 秒動畫從高山湖泊轉向明亮的銀河，再回到天空的倒影。發布者將這個算圖場景歸於 Fable 5.5。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5cb879d0a07a0f6e9fff5cf6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/91432c6827d650eb28f2269b.jpg" alt="高山湖泊上空的銀河" width="760"></a>

Type: Demo | Date: 2026-11-05

---

<a id="case-281"></a>
### Case 281: [程序化水體與音效中的鯨躍](https://x.com/camperaigg/status/2118069524306284556) (作者 [@camperaigg](https://x.com/camperaigg))

**將水下鏡頭、躍出水面和合成音訊整合為一段動畫。**

創作者表示，用 154 分鐘完成了這部 31 秒短片，內容包括程序化鯨魚、流體模擬、海面著色和合成聲音。製作紀錄也描述了放大檢查畫面、修正水花後重新算圖的過程。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b98c309a3c226bd24386940f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1bcb86163b677ad0a4172d13.jpg" alt="程序化水體與音效中的鯨躍" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-282"></a>
### Case 282: [四模型斑馬動作比較](https://x.com/AI_Screening/status/2118014564457668955) (作者 [@AI_Screening](https://x.com/AI_Screening))

**在同一動物動畫任務中比較步態、解剖結構和場景風格。**

縱向排列的四段影片分別標示為 Gemini 4 Carbon、Fable 5.5、Opus 5.5 和 Argon。保留完整合成畫面，便於同時觀察腿部運動、體形和背景處理的差異。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/6fdcb38bf56493c314dba5b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/890d1b92800ee622275ec8d7.jpg" alt="四模型斑馬動作比較" width="760"></a>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-283"></a>
### Case 283: [Lightreel 自然語言創作者搜尋](https://x.com/lightreelai/status/2118010927199248705) (作者 [@lightreelai](https://x.com/lightreelai))

**將創作者篩選要求寫成包含粉絲數與觀看數門檻的查詢。**

Lightreel 以 Fable 5.5 為標籤展示這項創作者探索示範。影片輸入尋找粉絲少於 10,000、且有一支影片觀看數超過 100,000 的情侶創作者的查詢，接著展示社群影片搜尋結果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5aef4b1766a560a35264c3ed.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1c6d9c1fb3c69b3aa2ee1976.jpg" alt="Lightreel 自然語言創作者搜尋" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-284"></a>
### Case 284: [雲海上方的飛船](https://x.com/devteamdrew/status/2118008142403649662) (作者 [@devteamdrew](https://x.com/devteamdrew))

**透過較長短片觀察光線與天氣變化中的鏡頭連續性。**

創作者表示，多個 Agent 團隊使用 JavaScript 和 Python，耗時 19 小時製作了這段約 100 秒的動畫。畫面跟隨一艘飛船穿過雲層、夕陽和月光。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/17ef07a780273abf9e9b6c92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a54746701db5f7f829071d2c.jpg" alt="雲海上方的飛船" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-285"></a>
### Case 285: [動態剖面的機械心臟](https://x.com/camperaigg/status/2118002649929056373) (作者 [@camperaigg](https://x.com/camperaigg))

**讓機械裝置持續運轉，同時展開外殼展示運動零件。**

創作者表示，這項 Blender 任務耗時 106 分鐘：機械心臟輸送金色油液，外殼打開後露出活塞和曲軸。製作紀錄也涵蓋合成音訊，以及把多餘高光追溯到隱藏燈光的排查過程。

```
Make a mechanical heart and show its insides, use blender.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/157ebee3ce748cdc1e6b7970.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4a862111878dc42939f8e5e4.jpg" alt="動態剖面的機械心臟" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-286"></a>
### Case 286: [可探索的漂浮體素寶塔花園](https://x.com/legit_api/status/2117994730336252114) (作者 [@legit_api](https://x.com/legit_api))

**走進建築與水景，評估生成環境的表現。**

創作者將這座體素花園歸於較早的 Fable 5.5 檢查點。鏡頭穿行於寶塔、浮島、橋梁和瀑布之間，從地面與高處展示場景。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/cc4d15bf5103d7eb64f63e29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/22e78c0beb2a6f509bc02739.jpg" alt="可探索的漂浮體素寶塔花園" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-287"></a>
### Case 287: [八個 Agent 團隊的海洋冒險短片](https://x.com/0xMovez/status/2117987052419428576) (作者 [@0xMovez](https://x.com/0xMovez))

**檢查多鏡頭短片中動作、特效與合成聲音的連續性。**

創作者表示，八個 Agent 團隊在不到三小時內完成這部 83 秒的 Three.js 短片，包含 39 個鏡頭和合成聲音。畫面呈現由飛行器、海洋生物和碎浪組成的海洋冒險。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a46543512fc30e5a33cb2fc3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a307daab219d70fa5bed0c86.jpg" alt="八個 Agent 團隊的海洋冒險短片" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-288"></a>
### Case 288: [互動式超級跑車展示](https://x.com/shmidtqq/status/2117977426990944736) (作者 [@shmidtqq](https://x.com/shmidtqq))

**將車輛特寫與可選鏡頭、車漆控制結合起來。**

創作者展示了一個以單一離線 HTML 檔案執行的 Three.js 超級跑車配置器，幾何體與材質都由程式碼生成。螢幕錄影呈現紅色車身、車輪與車身特寫、反射效果及鏡頭控制。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4bd439d08b9f8a320a8851ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a16368d4c8b7c9a3a5455607.jpg" alt="互動式超級跑車展示" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-289"></a>
### Case 289: [生命之樹的誕生](https://x.com/notjazii/status/2117972258090357164) (作者 [@notjazii](https://x.com/notjazii))

**圍繞種子長成大樹的可見變化，組織一段短動畫。**

創作者表示，這是一次約一小時、由單一提示詞驅動的程式編寫執行。30 秒畫面依序呈現荒蕪地貌、幼苗和持續生長的樹，最後展示雲層下的綠色世界。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29df8c398a2db37856c01b0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f50b8e7c2a28df7d0d3cd903.jpg" alt="生命之樹的誕生" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-290"></a>
### Case 290: [可行走城堡與內部機械](https://x.com/camperaigg/status/2117966825048997914) (作者 [@camperaigg](https://x.com/camperaigg))

**將行走綁定與可見機械運動及可開啟外殼連動。**

創作者表示，這套 Blender 工作流程耗時 133 分鐘，包含蒸汽機、齒輪組、四條行走腿和八塊可開啟的外殼面板。製作紀錄描述了修正鏡頭動畫，以及找出高運算成本的草地幾何體後縮短算圖時間的過程。

```
Make me Howl's moving castle and also show its internal machinery.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e7e25e7d44993a14ab0405e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8d3b1d734d971e2dd757926c.jpg" alt="可行走城堡與內部機械" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-291"></a>
### Case 291: [吐司角色與機械甲蟲](https://x.com/flxrnc/status/2117965294224232796) (作者 [@flxrnc](https://x.com/flxrnc))

**在一段簡短的動畫相遇中觀察角色調度與連續性。**

這部 40 秒短片展示一個方形吐司狀角色，在夕陽下的田野裡遇見藍色機械甲蟲。來源將短片歸於 Fable 5.5，並連結其動態設計指南。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/d5e16bfd05f1c391cf32f848.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b7ae776a5c29618d061465.jpg" alt="吐司角色與機械甲蟲" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-292"></a>
### Case 292: [暴風雨中的燈塔守護者](https://x.com/seeconvm/status/2117965120760365494) (作者 [@seeconvm](https://x.com/seeconvm))

**圍繞地點、天氣變化與明確結局建立短篇敘事。**

創作者將其描述為一部 60 秒 Three.js 短片，包含程式碼算出的畫面、合成聲音和離線 HTML 檔案。畫面跟隨一位小小的燈塔守護者穿過風雨雷電，最後轉入黎明。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/7ca3c1e23eac0ed20511211e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/dfcab72e07d547d9dcb1dbc1.jpg" alt="暴風雨中的燈塔守護者" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-293"></a>
### Case 293: [海濱小鎮中的海洋生物](https://x.com/BubbleBrain/status/2117963042621178000) (作者 [@BubbleBrain](https://x.com/BubbleBrain))

**透過完整短片觀察角色運動、轉場與視覺一致性。**

來源分享一段約一分鐘的 Fable 5.5 動畫，其中有綠色海洋生物、海濱小鎮和漂浮氣泡。影片為評估這種短片風格提供具體的視覺樣本。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/65db346493bdd9973bec3a4c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4442bdca5e6a7460f03af731.jpg" alt="海濱小鎮中的海洋生物" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-294"></a>
### Case 294: [三模型地毯賽車比較](https://x.com/noclipepe/status/2117914944410628430) (作者 [@noclipepe](https://x.com/noclipepe))

**在同一賽車任務中比較可玩場景完整度、運動與視覺處理。**

創作者使用 Fable 5.5、Opus 5.5 和 GPT-6 Astra 測試童年地毯賽車遊戲。此處同時保留最新的三畫面螢幕錄影與較早的雙模型比較；影片中的分數是創作者自己的評分。

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ffe3b88099594ba14f536b51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/24d8ea7644cbe19947c8c53a.jpg" alt="三模型地毯賽車比較" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e214760ff83ad9bfaf202484.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0340fc5579003245dfa99b1.jpg" alt="三模型地毯賽車比較" width="760"></a></td></tr></table>

[相關比較 · @noclipepe](https://x.com/noclipepe/status/2117729666576302187)

Type: Evaluation | Date: 2026-11-04

---

<a id="case-295"></a>
### Case 295: [卡車變形成機器人](https://x.com/camperaigg/status/2117914482752299311) (作者 [@camperaigg](https://x.com/camperaigg))

**透過變形過程觀察綁定、地面接觸與聲音同步。**

創作者表示，Blender 製作耗時 107 分鐘，包括 51 關節綁定、地面接觸求解器、程序化雨景和合成音效。螢幕錄影展示卡車在濕潤路面上展開，變成站立的機器人。

```
Make me a transformer truck with animations of its transforming.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/72ef538a8fb4b94f0e2d7e2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ea8537c130cd5623959dc275.jpg" alt="卡車變形成機器人" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-296"></a>
### Case 296: [Fable 與混元動畫影格比較](https://x.com/xbquan/status/2117899651365908855) (作者 [@xbquan](https://x.com/xbquan))

**先比較對應影格，再對完整動畫作判斷。**

作者分享兩組標示 Fable 5.5 和 Hunyuan 4 的配對螢幕截圖。每組將角色與環境結果放在一起，可用來比較圖中實際展示的畫面。

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e6c6551a29757e1eb7c31f36.jpg" alt="Fable 與混元動畫影格比較" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/864db255f6fd2807b689d7d7.jpg" alt="Fable 與混元動畫影格比較" width="760"></td></tr></table>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-297"></a>
### Case 297: [關於分享光芒的動畫](https://x.com/abhinavflac/status/2117883591019708740) (作者 [@abhinavflac](https://x.com/abhinavflac))

**將抽象主題轉化為有明確結局的短篇敘事。**

在被要求展示「善意意味著什麼」後，模型被描述為用程式碼製作了動畫與聲音。一個發光身影把自己的光傳給孩子，隨後變得更亮，周圍景色也逐漸充滿色彩。

```
Show me what kindness means to you
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b888d1a62b4d27ae2fca8226.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5bd15fc5c234b4b114765d6f.jpg" alt="關於分享光芒的動畫" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-298"></a>
### Case 298: [群山之間的體素村莊](https://x.com/abhinavflac/status/2117377130388656569) (作者 [@abhinavflac](https://x.com/abhinavflac))

**從不同尺度探索生成村莊，檢查空間關係是否連貫。**

原作者分享一個有房屋、水道和小居民的鮮活體素村莊，鏡頭從水岸、俯瞰視角與周圍山間展示場景。一篇相關中文貼文也提供詳細場景提示詞。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae5269b0eff86da4580064d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e612faf20dd5f5de4ee171b.jpg" alt="群山之間的體素村莊" width="760"></a>

[@cfenghub](https://x.com/cfenghub/status/2117775332535148752)

Type: Demo | Date: 2026-11-02

---

<a id="case-299"></a>
### Case 299: [四模型鵜鶘與大象構圖](https://x.com/pipeline_os/status/2117719191478513700) (作者 [@pipeline_os](https://x.com/pipeline_os))

**比較不同模型如何在一段動畫中處理多個互動主體。**

四畫面螢幕錄影並排呈現 Gemini 4 Argon、Opus 5.5、Fable 5.5 和 Kimi K3.1 Pro 的鵜鶘、腳踏車、鱷魚與大象任務結果。保留完整合成畫面，便於觀察各模型的主體位置與運動。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/9db78999efffeffa7ccaca0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/15a45dc0efe3247f0821c8a2.jpg" alt="四模型鵜鶘與大象構圖" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-300"></a>
### Case 300: [帶衝擊影格的動漫劍鬥](https://x.com/camperaigg/status/2117717189059026969) (作者 [@camperaigg](https://x.com/camperaigg))

**同步角色動作、衝擊閃格、聲音與刻意保留的靜默。**

創作者表示，經過 66 分鐘程式編寫，生成一段 46 秒的火柴人對戰，包含布料般的披風、對比鮮明的武器及合成音樂與音效。製作紀錄描述了修正反向攻擊、視覺拖尾和標題位置的過程。

```
Make me a video of 2 stickman fighting, anime style.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/c36c188396aac371a64e31a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b670f06d376211c60bf894.jpg" alt="帶衝擊影格的動漫劍鬥" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-301"></a>
### Case 301: [四模型奔鹿動畫比較](https://x.com/fawnunwrap/status/2117702487755100543) (作者 [@fawnunwrap](https://x.com/fawnunwrap))

**在完整同任務合成畫面中比較肢體運動與動物形態。**

FawnBench 在四個畫面中展示奔跑的鹿，分別標示為作者所稱的 Fable 5.5 執行、Gemini 4 Argon、GPT-6 Astra 和 Opus 5.5。這是一組視覺比較，而非測量所得的數值效能結果。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3add4d9e0752d0467cbe6065.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/eea598747047797148e19c4e.jpg" alt="四模型奔鹿動畫比較" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-302"></a>
### Case 302: [穿越積水城市的機器人](https://x.com/0xMovez/status/2117700681867903169) (作者 [@0xMovez](https://x.com/0xMovez))

**觀察倒影、角色運動與變化鏡頭之間的連續性。**

創作者表示，這段 42 秒 Three.js 動畫包含程式碼算出的畫面、合成聲音和一個離線 HTML 算圖檔案。畫面跟隨機器人穿過積水且植物蔓生的城市，走向色彩明亮的開闊水域。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f39e1807d1e80422c31530c6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/247f768636339f49d149c787.jpg" alt="穿越積水城市的機器人" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-303"></a>
### Case 303: [Blender 寶劍與展示短片](https://x.com/camperaigg/status/2117694354685092255) (作者 [@camperaigg](https://x.com/camperaigg))

**將程序化資產建模與後續鏡頭、聲音製作分開觀察。**

創作者表示，先用一個 Python 腳本生成寶劍，再要求製作影片。後續採用連續 Blender 鏡頭運動、森林光照、合成管弦配樂和 HyperFrames 剪輯；作者報告的合計耗時為 65 分鐘。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3c767f2038ef7d3960c956ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/525304dc7d4016ac33b3d4f8.jpg" alt="Blender 寶劍與展示短片" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-304"></a>
### Case 304: [Lantern Isle 像素村莊動畫](https://x.com/abhinavflac/status/2117693193429139965) (作者 [@abhinavflac](https://x.com/abhinavflac))

**在密集動畫環境中觀察局部活動與晝夜轉換。**

創作者分享一座由程式碼繪製的島嶼村莊，包含居民、船隻、瀑布、燈籠和音樂。螢幕錄影在村莊近景、全島遠景與燈籠發光的夜景之間切換。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e91f1eabab743730dd815c98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b7d2e578739d25596db1164f.jpg" alt="Lantern Isle 像素村莊動畫" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-305"></a>
### Case 305: [Pause 遊戲影片剪輯示範](https://x.com/pausevfx/status/2117676887665447206) (作者 [@pausevfx](https://x.com/pausevfx))

**檢查從原始素材、字幕到可編輯時間軸的剪輯流程。**

Pause 以 Fable 5.5 影片剪輯為標籤展示這套流程。示範包括挑選遊戲片段、重新構圖臉部攝影畫面、加入字幕與聲音，並在 Premiere 中開啟可編輯序列。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0faaeecdaa02683f81e67f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae2d32876804bf286f11dc6c.jpg" alt="Pause 遊戲影片剪輯示範" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-306"></a>
### Case 306: [海濱騎車的鵜鶘](https://x.com/pankajkumar_dev/status/2117301455665439210) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**從近景與遠景檢查細部幾何結構和動畫。**

創作者分享一隻在海邊騎高輪腳踏車的鵜鶘。螢幕錄影近距離查看羽毛、踏板與車輪幾何結構，再回到鋪面海濱步道的寬闊視角。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/66c3c44bcefa684522f95b96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8575912e8f20f48439aea683.jpg" alt="海濱騎車的鵜鶘" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="acknowledge"></a>
## 🙏 致謝

這個 repository 的靈感來自那些公開分享真實 Claude Fable 5 使用案例的創作者、開發者、基準測試團隊與社群。

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@hakmgpt](https://x.com/hakmgpt), [@camperaigg](https://x.com/camperaigg), [@lightreelai](https://x.com/lightreelai), [@0xMovez](https://x.com/0xMovez), [@shmidtqq](https://x.com/shmidtqq), [@flxrnc](https://x.com/flxrnc), [@seeconvm](https://x.com/seeconvm), [@BubbleBrain](https://x.com/BubbleBrain), [@xbquan](https://x.com/xbquan), [@pipeline_os](https://x.com/pipeline_os), [@fawnunwrap](https://x.com/fawnunwrap), [@pausevfx](https://x.com/pausevfx), [@AnikaCodes](https://x.com/AnikaCodes), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@cfenghub](https://x.com/cfenghub), [@shneural](https://x.com/shneural)

*我們無法保證每個案例都歸屬於最原始的創作者。如果有任何需要修正的地方，請聯絡我們，我們會更新。*

如果你有更多有趣的使用案例想分享，歡迎開 issue 或 pull request，協助擴充 Evolink usecase library。


[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
