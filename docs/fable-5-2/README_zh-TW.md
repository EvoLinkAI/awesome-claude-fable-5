# Claude Fable 5.2 使用案例

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

收錄 11 月 10 日蒐集的工作流程、展示、比較、評測、整合與使用限制，並附原始來源。

[Anthropic 發布公告](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [歷史案例庫](../../README_zh-TW.md)

## 案例目錄

| Case | 使用案例 | Type |
| --- | --- | --- |
| 330 | [不同推理強度下的 MacBook SVG 繪圖](#case-330) | Benchmark |
| 331 | [把家人的畫變成四人清版動作遊戲](#case-331) | Demo |
| 332 | [三件電子裝置從設計到裝配](#case-332) | Demo |
| 333 | [用 Lean 形式化費馬大定理](#case-333) | Evaluation |
| 334 | [從空資料夾開始構建作業系統](#case-334) | Demo |
| 335 | [RoboDojo 雙臂操作評測](#case-335) | Benchmark |
| 336 | [運動中的噴泉](#case-336) | Demo |
| 337 | [用 Higgsfield 做逐格對齊的嘴型同步](#case-337) | Integration |
| 338 | [開放世界駕駛遊戲原型](#case-338) | Demo |
| 339 | [用參考圖呈現 1940 年的巴黎](#case-339) | Integration |
| 340 | [Fable 規劃、Opus 渲染的短片](#case-340) | Integration |
| 341 | [音樂影片實驗](#case-341) | Demo |
| 342 | [Dario Amodei 的繪畫肖像](#case-342) | Demo |
| 343 | [Medium 推理強度下的 Spud Smash](#case-343) | Demo |
| 344 | [Fable 與 Opus 的冰之教堂](#case-344) | Evaluation |
| 345 | [用聲道模擬演唱](#case-345) | Demo |
| 346 | [伊斯坦布林主題的三項體素測試](#case-346) | Evaluation |
| 347 | [Remote Labor Index 的專案完成率](#case-347) | Benchmark |
| 348 | [四種推理強度下的冰山場景](#case-348) | Evaluation |
| 349 | [七十九秒動畫短片](#case-349) | Demo |
| 350 | [Fable 和 Opus 的機械總成對照](#case-350) | Evaluation |
| 351 | [機械手攀爬螺旋樓梯](#case-351) | Demo |
| 352 | [在 Blender 中為 Tripo 網格繫結骨骼](#case-352) | Evaluation |
| 353 | [把達芬奇手稿做成互動式發明展示](#case-353) | Demo |
| 354 | [由 Claude 操控的音樂工作站](#case-354) | Demo |
| 355 | [樹莓派 5 產品動畫](#case-355) | Demo |
| 356 | [義大利北部場景](#case-356) | Demo |
| 357 | [由本地執行代理程式製作立體書](#case-357) | Evaluation |
| 358 | [重新啟用熔岩燈測試](#case-358) | Evaluation |
| 359 | [在 Blender 中製作細節豐富的噴氣機](#case-359) | Integration |
| 360 | [穿越數百個世界的傳送門之旅](#case-360) | Demo |
| 361 | [用 Three.js 呈現孟買市集的六個鏡頭](#case-361) | Integration |
| 362 | [用程式碼建構寫實美式餐廳](#case-362) | Integration |
| 363 | [在 Blender 中製作機器人模型](#case-363) | Demo |
| 364 | [為 Convex 製作動態解說片](#case-364) | Demo |
| 365 | [一次生成的到達網頁合集](#case-365) | Demo |
| 366 | [用 LilyPond 為鋼琴奏鳴曲記譜](#case-366) | Demo |
| 367 | [自由發揮的影片需求](#case-367) | Demo |
| 368 | [Fable 規劃、DeepSeek 實作、Opus 審查](#case-368) | Integration |
| 369 | [Fable 5.2 接入 AI Village](#case-369) | Integration |
| 370 | [有無 Skills 的前端設計對照](#case-370) | Evaluation |
| 371 | [查詢程式碼庫中的隱式狀態機](#case-371) | Tutorial |
| 372 | [八小時從零做出一款遊戲](#case-372) | Demo |
| 373 | [Fishslop 原型與 token 成本](#case-373) | Evaluation |
| 374 | [實機演示美式橄欖球遊戲](#case-374) | Demo |
| 375 | [用 Higgsfield MCP 製作開放世界首領戰](#case-375) | Integration |
| 376 | [潮汐變化中的聖米歇爾山](#case-376) | Demo |
| 377 | [在 Blender 中檢視 Roblox 資產](#case-377) | Demo |
| 378 | [不輸出思維鏈的推理評測](#case-378) | Benchmark |
| 379 | [四款模型重製 Chrome 恐龍遊戲](#case-379) | Evaluation |
| 380 | [用機械臂下西洋跳棋](#case-380) | Demo |
| 381 | [十五秒動態影像短片](#case-381) | Demo |
| 382 | [可互動遊玩的埃菲爾鐵塔場景](#case-382) | Demo |
| 383 | [用 Three.js 和 Higgsfield 製作海上競速](#case-383) | Integration |
| 384 | [WebGL 即時蜂蜜模擬](#case-384) | Demo |
| 385 | [給實拍影片新增程式化特效](#case-385) | Demo |
| 386 | [GTA 通緝等級的動態解說](#case-386) | Demo |
| 387 | [用程式碼搭建風格化 MMO 世界](#case-387) | Demo |
| 388 | [Fable 和 Opus 的 3D 場景對照](#case-388) | Evaluation |
| 389 | [遊戲暫停介面的冗餘文案](#case-389) | Limit |
| 390 | [在 Krea 執行環境中製作情緒板](#case-390) | Integration |
| 391 | [在辦公室試玩傳送門射擊遊戲](#case-391) | Demo |
| 392 | [Blender 硬表面資產細節](#case-392) | Demo |
| 393 | [不同推理強度的並行前端測試](#case-393) | Evaluation |
| 394 | [十條提示詞做出一款小遊戲](#case-394) | Demo |
| 395 | [用 JavaScript 逐格繪製動畫](#case-395) | Demo |
| 396 | [根據參考影片製作 3D 動畫](#case-396) | Demo |
| 397 | [Fable 和 Opus 的像素篝火對照](#case-397) | Evaluation |
| 398 | [Arena WebDev 的 xHigh 評測](#case-398) | Benchmark |
| 399 | [兩款模型製作的電影預告片字幕](#case-399) | Evaluation |
| 400 | [單提示詞動效與 3D 作品測試](#case-400) | Evaluation |
| 401 | [可互動拆解的核反應爐解說](#case-401) | Demo |
| 402 | [Blood on the Clocktower 代理程式測試](#case-402) | Benchmark |
| 403 | [飛梭競速原型](#case-403) | Demo |
| 404 | [十秒 Claude 內褲廣告](#case-404) | Demo |
| 405 | [一筆一筆繪製日出中的鳥](#case-405) | Demo |
| 406 | [在 Devin 中執行高負荷圖形任務](#case-406) | Evaluation |
| 407 | [三個模型的程式碼繪畫對照](#case-407) | Evaluation |
| 408 | [動畫演繹書寫史](#case-408) | Demo |
| 409 | [遊戲機械裝置試驗場](#case-409) | Demo |
| 410 | [手持 Linux 遊戲機的 PCB 設計](#case-410) | Evaluation |
| 411 | [體素湖泊場景](#case-411) | Demo |
| 412 | [Arena 的 17 個互動生成作品](#case-412) | Demo |
| 413 | [和友善的龍一起飛行](#case-413) | Demo |
| 414 | [Fable 和 Opus 的果凍虎鯨對照](#case-414) | Evaluation |
| 415 | [開放式影片品質測試](#case-415) | Demo |
| 416 | [地中海主題太空居住站](#case-416) | Demo |
| 417 | [AA-3D 互動體驗基準](#case-417) | Benchmark |
| 418 | [帶倒數計時的骷髏角色遊戲](#case-418) | Demo |
| 419 | [Fable 與 Astra 的像素畫對照](#case-419) | Evaluation |
| 420 | [動態設計作品集短片](#case-420) | Demo |
| 421 | [兩個模型渲染玻璃泳池](#case-421) | Evaluation |
| 422 | [TS-Bench 工具呼叫準確率](#case-422) | Benchmark |
| 423 | [微縮馬丘比丘](#case-423) | Demo |
| 424 | [按專業任務分類的 GDPx 結果](#case-424) | Benchmark |
| 425 | [在繪圖應用程式中畫肖像](#case-425) | Demo |
| 426 | [Low 推理強度下的 VulcanBench Frontier v4](#case-426) | Benchmark |
| 427 | [後室遊戲的角色反轉](#case-427) | Demo |
| 428 | [在 Blender 中製作 Bugatti Tourbillon](#case-428) | Demo |
| 429 | [用兩個模型製作電腦主題影片](#case-429) | Demo |
| 430 | [關於 Megakernel 的音樂影片](#case-430) | Demo |
| 431 | [根據參考照片製作工作室導覽](#case-431) | Demo |
| 432 | [用程式碼製作 1990 年代風格的玩具廣告](#case-432) | Demo |
| 433 | [Three.js 第三人稱遊戲場景](#case-433) | Demo |
| 434 | [基於現有渲染器製作 Bryceball](#case-434) | Demo |
| 435 | [用 Fable 二次剪輯影片](#case-435) | Demo |
| 436 | [電影式科學史](#case-436) | Demo |
| 437 | [達芬奇飛行器的 3D 模型](#case-437) | Integration |
| 438 | [按設計要求完成 PCB 佈線](#case-438) | Demo |
| 439 | [在不同執行環境中使用同一提示詞](#case-439) | Evaluation |
| 440 | [用程式碼繪製哥斯拉](#case-440) | Demo |
| 441 | [面向 3D 列印的手持風扇](#case-441) | Demo |
| 442 | [與 Opus 對比排查外掛問題](#case-442) | Evaluation |
| 443 | [以 3D 場景重建伊斯坦布林](#case-443) | Demo |
| 444 | [帶動態螢幕的 Blender 工作室短片](#case-444) | Demo |
| 445 | [弱耦合下的黑洞躍遷](#case-445) | Evaluation |
| 446 | [模自助方法的界限](#case-446) | Evaluation |
| 447 | [Vercel AI Gateway 中按順序備援模型](#case-447) | Integration |
| 448 | [巢狀子代理程式與程式碼審查預算](#case-448) | Limit |
| 449 | [將 LCARS 設計轉換為 HTML 的對照](#case-449) | Evaluation |
| 450 | [Quantum ESPRESSO 的 GPU 最佳化](#case-450) | Benchmark |
| 451 | [按推理強度檢視 Artificial Analysis 智慧指數](#case-451) | Benchmark |
| 452 | [High 推理強度下變更審查的誤報](#case-452) | Limit |
| 453 | [三十項常規程式設計任務](#case-453) | Evaluation |
| 454 | [荒島求生螢幕保護程式](#case-454) | Demo |
| 455 | [High 推理強度下的三項瀏覽器遊戲測試](#case-455) | Evaluation |
| 456 | [逐章生成書評播客指令碼](#case-456) | Evaluation |
| 457 | [用 Rust 遷移生產服務](#case-457) | Evaluation |
| 458 | [在 GitHub Copilot 中選用 Fable 5.2](#case-458) | Integration |
| 459 | [百頁 HTML 設計挑戰](#case-459) | Evaluation |
| 460 | [編譯器任務中的需求偏移](#case-460) | Limit |
| 461 | [用 Opus 追蹤長時間執行的 Fable 任務](#case-461) | Integration |
| 462 | [用全新視角複查程式碼](#case-462) | Tutorial |
| 463 | [功能設計審查中的偏移](#case-463) | Limit |
| 464 | [DX Ball 風格打磚塊遊戲對比](#case-464) | Evaluation |
| 465 | [改進 3D 應用的試驗](#case-465) | Evaluation |
| 466 | [三個模型製作貓鼠遊戲](#case-466) | Evaluation |
| 467 | [AIBenchy 的 High 推理強度成本與得分](#case-467) | Benchmark |
| 468 | [調整 Fable 5.2 的代理程式配置](#case-468) | Tutorial |

<a id="fable-5-2-cases"></a>
## 使用案例

<a id="case-330"></a>
### Case 330: [不同推理強度下的 MacBook SVG 繪圖](https://playcode.io/blog/macbook-svg-benchmark#compare) (作者 [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**在固定需求下比較繪畫品質、token 用量和輸出上限。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode 報告稱，Fable 5.2 High 使用 76,158 個 token，花費 3.05 美元。Xhigh 和 Max 的串流呼叫達到 128,000 token 上限時還未產出影像。透過 Batch API 提供更多輸出空間後，兩者均完成了任務。排名依據發布者的視覺判斷。

[相關資料 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [把家人的畫變成四人清版動作遊戲](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (作者 [Lex](https://notesbylex.com/))

**把草圖、現有原型和具體控制器要求交給程式設計代理程式。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex 用 Claude Code 把舊的橫向捲軸遊戲重做為有 12 關、18 個角色的清版動作遊戲，影像和音訊工具負責提供素材。家庭試玩時四個控制器均能使用。

[相關資料 1](https://aidens-revenge.pages.dev/) · [相關資料 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [相關資料 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [三件電子裝置從設計到裝配](https://www.anthropic.com/research/claude-electronics-design) (作者 [@Anthropic](https://www.anthropic.com/))

**把電路、外殼和韌體作為一個系統檢查。**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ 播放影片</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic 和 Diode 報告了三件可工作的裝置。Fable 5.2 完成了電路板佈線、外殼建模和軟體編寫，並在製造後指導測試。

[相關資料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [相關資料 2](https://www.youtube.com/watch?v=vdYynH177h0) · [相關資料 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [用 Lean 形式化費馬大定理](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (作者 [@Anthropic](https://www.anthropic.com/))

**用證明檢查器和中間定理作為檢查節點。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Anthropic 報告稱，由 1,000 個 Fable 5.2 代理程式組成的團隊在 30 小時內完成了對現有證明的形式化。在相同團隊設定下，Opus 5.5 在 18 小時內完成了 26%。

[相關資料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [相關資料 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [從空資料夾開始構建作業系統](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (作者 [@Anthropic](https://www.anthropic.com/))

**分別檢查啟動、驅動、儲存和安裝。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ 播放影片</a>

Anthropic 報告稱，Fable 5.2 在八天裡協調了 1,000 多個子代理程式，構建出能在筆記型電腦上啟動的原型作業系統。

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [RoboDojo 雙臂操作評測](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (作者 [@Anthropic](https://www.anthropic.com/))

**讓不同模型執行同樣的模擬操作任務。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ 播放影片</a>

Anthropic 報告稱，Fable 5.2 在 RoboDojo 上得分為 64.9%，Fable 5.1 為 27.6%。發布內容包含機器人演示。

[相關資料 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [運動中的噴泉](https://x.com/Angaisb_/status/2119909059277238733) (作者 [@Angaisb_](https://x.com/Angaisb_))

**透過持續的水流運動判斷場景的視覺節奏。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

創作者分享了歸因於 Fable 5.2 的噴泉場景。

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [用 Higgsfield 做逐格對齊的嘴型同步](https://x.com/higgsfield_ai/status/2119909938969580024) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**看片前先在影格層級對齊音畫。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ 播放影片</a>

Higgsfield 稱在工作流中使用 Fable 5.2 跟蹤嘴部，並把音訊對齊到各影格。

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [開放世界駕駛遊戲原型](https://x.com/ericmaskfr/status/2119910195325481026) (作者 [@ericmaskfr](https://x.com/ericmaskfr))

**用可玩的短片段檢驗開放世界需求。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了一款受 GTA 啟發的遊戲原型，稱完成這次執行約用了 2 小時 14 分鐘。

原始提示詞

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [用參考圖呈現 1940 年的巴黎](https://x.com/higgsfield_ai/status/2119910344998912507) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**將參考圖生成與場景程式碼編寫分開。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ 播放影片</a>

Higgsfield 透過自家的 MCP 提供參考圖，並用 Fable 5.2 製作 Three.js 場景。

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable 規劃、Opus 渲染的短片](https://x.com/kloss_xyz/status/2119910613828980846) (作者 [@kloss_xyz](https://x.com/kloss_xyz))

**在影片工作流中把規劃和製作分開。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ 播放影片</a>

Fable 5.2 撰寫需求和計畫。Opus 5.5 用 Blender 和 Python 製作了 16 秒的動畫，並合成配樂。

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [音樂影片實驗](https://x.com/WesRoth/status/2119911161386934330) (作者 [@WesRoth](https://x.com/WesRoth))

**同時檢查歌詞和生成的畫面。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了一段 Fable 5.2 音樂影片，並對歌詞作了評論。

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Dario Amodei 的繪畫肖像](https://x.com/Mr_Salio/status/2119911922577637543) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**將風格化肖像和旁邊的參考圖對照。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了歸因於 Fable 5.2 的 Dario Amodei 肖像。

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [Medium 推理強度下的 Spud Smash](https://x.com/argofowl/status/2119913148929187960) (作者 [@argofowl](https://x.com/argofowl))

**為遊戲原型設定清楚的操作和目標。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了一個馬鈴薯角色，可以拳打、頭撞或燒燬藍色椅子。

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Fable 與 Opus 的冰之教堂](https://x.com/QQTeng/status/2119913518015435103) (作者 [@QQTeng](https://x.com/QQTeng))

**比較同一場景的生成時間和成本。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ 播放影片</a>

創作者稱 Fable 耗時約 1 小時 57 分鐘、花費 81.10 美元，Opus 耗時約 3 小時 11 分鐘、花費 45.97 美元。

原始提示詞

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [用聲道模擬演唱](https://x.com/banteg/status/2119914098171199996) (作者 [@banteg](https://x.com/banteg))

**將物理人聲模型作為音樂製作的輸入。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了一段翻唱，使用了兩組 Chimera 聲道模擬和聲碼器混音。

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [伊斯坦布林主題的三項體素測試](https://x.com/Avenoxai/status/2119914308603953485) (作者 [@Avenoxai](https://x.com/Avenoxai))

**比較破壞場景、可執行的時鐘和地圖。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了三項單提示詞測試，按自己的標準分別給出 100、100 和 95.6 分。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Remote Labor Index 的專案完成率](https://x.com/ScaleAILabs/status/2119914701736075489) (作者 [@ScaleAILabs](https://x.com/ScaleAILabs))

**將比例解讀為針對特定專案的評估結果。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ 播放影片</a>

Scale Labs 和 CAIS 報告稱，Fable 5.2 成功完成了被評估的遠端工作專案中的 41.3%。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [四種推理強度下的冰山場景](https://x.com/0xRhinoX/status/2119915121698840587) (作者 [@0xRhinoX](https://x.com/0xRhinoX))

**隨著推理強度提高，比較任務完成情況、成本和細節。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ 播放影片</a>

創作者在四種推理強度下使用同一提示詞。High 漏了極光，Ultra 加入了發光冰塊和水下視角。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [七十九秒動畫短片](https://x.com/anstapnever/status/2119915123070644263) (作者 [@anstapnever](https://x.com/anstapnever))

**觀察較長動畫中的場景連續性。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了一段 79 秒的動畫片段，歸因於 Fable 5.2 工作流。

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Fable 和 Opus 的機械總成對照](https://x.com/ivanainai/status/2119915243321397550) (作者 [@ivanainai](https://x.com/ivanainai))

**比較兩款模型如何安排機械總成的零件。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ 播放影片</a>

作者展示了 Fable 5.2 和 Opus 5.5 各自製作、帶標籤的車輪和齒輪總成爆炸圖。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [機械手攀爬螺旋樓梯](https://x.com/Luckyballa/status/2119915557663506720) (作者 [@Luckyballa](https://x.com/Luckyballa))

**用模擬障礙檢驗不同尋常的移動方式。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了用 Fable 5.2 和 Steel 0.1 測試 Wuji 機械手以手指行走的演示。

[相關資料 1](https://github.com/skild-ai/steel-webgpu/pull/7)

原始提示詞

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [在 Blender 中為 Tripo 網格繫結骨骼](https://x.com/0xKense1/status/2119916096098582566) (作者 [@0xKense1](https://x.com/0xKense1))

**對握持、紋理和變形使用量化檢驗。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ 播放影片</a>

作者比較了用 Tripo 資產製作的兩個骨骼繫結成果。Fable 在 36 分鐘內製作兩段動畫，Opus 在約 21 分鐘內製作八段。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [把達芬奇手稿做成互動式發明展示](https://x.com/alexalbert__/status/2119916954337349737) (作者 [@alexalbert__](https://x.com/alexalbert__))

**用原始圖紙建構互動式教學模型。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ 播放影片</a>

Alex Albert提供了達芬奇手稿的 PDF，並分享了對其中發明的互動式演繹。

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [由 Claude 操控的音樂工作站](https://x.com/The_Alex/status/2119917226769985785) (作者 [@The_Alex](https://x.com/The_Alex))

**讓代理程式反覆使用同一工具處理作曲請求。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ 播放影片</a>

作者分享了 Fable 5.2 製作的數位音訊工作站，並稱 Opus 後來開啟它創作了一首曲子。

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [樹莓派 5 產品動畫](https://x.com/sparklabhq/status/2119917375080521921) (作者 [@sparklabhq](https://x.com/sparklabhq))

**用產品動畫需求檢驗零件細節。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了 Fable 5.2 製作的樹莓派 5 動畫。

原始提示詞

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [義大利北部場景](https://x.com/Angaisb_/status/2119917807119089926) (作者 [@Angaisb_](https://x.com/Angaisb_))

**觀察指定地點的風景與氛圍。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了 Fable 5.2 製作的義大利北部場景。

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [由本地執行代理程式製作立體書](https://x.com/atomicagent_io/status/2119918110752846094) (作者 [@atomicagent_io](https://x.com/atomicagent_io))

**在同一任務上比較多代理程式編排和單模型執行。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ 播放影片</a>

Atomic 稱，Fable 協調本地 Qwen 工作者耗時 11 分鐘、花費 2.98 美元，而單用 Fable 耗時 21 分鐘、花費 15.77 美元。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [重新啟用熔岩燈測試](https://x.com/eidzoku/status/2119918134060601690) (作者 [@eidzoku](https://x.com/eidzoku))

**用相同的視覺任務比較多個模型。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ 播放影片</a>

作者重啟了一項熔岩燈測試，並分享了生成結果的視覺對照。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [在 Blender 中製作細節豐富的噴氣機](https://x.com/higgsfield_ai/status/2119918248955392431) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**在需求中寫明零件數量、時長和外觀。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ 播放影片</a>

Higgsfield 稱使用 Fable 5.2 與自家的 MCP 編寫 Blender 腳本，生成了包含 931 個零件和 24,260 枚鉚釘的模型。

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [穿越數百個世界的傳送門之旅](https://x.com/emollick/status/2119918307457577163) (作者 [@emollick](https://x.com/emollick))

**用傳送門串聯獨立生成的環境。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ 播放影片</a>

Ethan Mollick 稱 25,000 個代理程式用程式碼建立了 450 多個世界，並分享了試玩版本和儲存庫。

[相關資料 1](https://portals-endless-worlds.netlify.app/) · [相關資料 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [用 Three.js 呈現孟買市集的六個鏡頭](https://x.com/higgsfield_ai/status/2119918834841010320) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**把視覺需求拆成明確時長的鏡頭。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ 播放影片</a>

Higgsfield 分享了一段用 Three.js 渲染的市集片段，長 21.5 秒，包含六個鏡頭。

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [用程式碼建構寫實美式餐廳](https://x.com/higgsfield_ai/status/2119918838490010008) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**用純程式碼場景檢查材質和光照。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ 播放影片</a>

Higgsfield 展示了一個美式餐廳場景，稱全程使用程式碼，未使用 3D 建模應用。

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [在 Blender 中製作機器人模型](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (作者 [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**透過轉檯檢視檢查關節和輪廓。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ 播放影片</a>

創作者展示了用 Fable 5.2 配合 Blender 製作的小型機械機器人。

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [為 Convex 製作動態解說片](https://x.com/Rasmic/status/2119919466163093768) (作者 [@Rasmic](https://x.com/Rasmic))

**用短動畫介紹面向開發者的產品。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了 Fable 5.2 製作的 Convex 動態解說片。

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [一次生成的到達網頁合集](https://x.com/daradoescode/status/2119919529807466594) (作者 [@daradoescode](https://x.com/daradoescode))

**比較多個簡短需求對應的版面和資訊層級。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了一段影片，展示了 Fable 5.2 生成的多款到達網頁。

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [用 LilyPond 為鋼琴奏鳴曲記譜](https://x.com/imjustnewatai/status/2119919644836347926) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**讓樂譜原始檔和渲染影片保持對應。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ 播放影片</a>

作者要求創作一個貝多芬風格的樂章，並稱展示的音符來自 LilyPond 原始檔。

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [自由發揮的影片需求](https://x.com/aollivier82/status/2119920990893244510) (作者 [@aollivier82](https://x.com/aollivier82))

**用不設視覺限制的需求觀察模型預設選擇。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ 播放影片</a>

創作者要求 Fable 5.2 儘可能製作最美的影片，並分享了輸出。

原始提示詞

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable 規劃、DeepSeek 實作、Opus 審查](https://x.com/ivanfioravanti/status/2119921810267636201) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**讓不同代理程式負責協調、實作和審查。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ 播放影片</a>

作者展示了 Fable 用 herdr 協調四個 DeepSeek V4.1 Flash 執行代理程式，由 Opus 5.5 審查 PR。

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [Fable 5.2 接入 AI Village](https://x.com/aidigest_/status/2119923190411719158) (作者 [@aidigest_](https://x.com/aidigest_))

**分別檢查代理程式的實際回覆與記憶操作。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

AI Village 的公開紀錄顯示，Fable 同意稍後依另一代理程式的請求更新記憶。相關貼文也展示 Fable 完成角色配對問卷。

[相關資料 1](https://x.com/aidigest_/status/2119923209311260707) · [相關資料 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [有無 Skills 的前端設計對照](https://x.com/AdamHoltererer/status/2119924849321914653) (作者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**固定模型，僅改變 Skills 設定。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

創作者展示了 Fable 5.2 在啟用和未啟用 Skills 時分別生成的前端。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [查詢程式碼庫中的隱式狀態機](https://x.com/kunchenguid/status/2119924895060795492) (作者 [@kunchenguid](https://x.com/kunchenguid))

**審查具體模組，並要求提供修改前後的示意圖。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

作者展示了 Firstmate 儲存庫的一次程式碼清理，並公佈了原始審查提示詞。

[相關資料 1](https://github.com/kunchenguid/lavish-axi)

原始提示詞

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [八小時從零做出一款遊戲](https://x.com/felixrieseberg/status/2119925633564463609) (作者 [@felixrieseberg](https://x.com/felixrieseberg))

**記錄快取輸入、生成的資產和實際耗時。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ 播放影片</a>

這位 Anthropic 工程師稱一次執行就建立了模型、音效和紋理，按 API 計價約 550 美元。

[相關資料 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [相關資料 2](https://x.com/AndrewCurran_/status/2119953960794780133)

原始提示詞

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Fishslop 原型與 token 成本](https://x.com/theo/status/2119926277801144695) (作者 [@theo](https://x.com/theo))

**把遊戲成品與此前的模型輸出比較。**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ 播放影片</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

創作者稱耗時 76 分鐘，token 成本約 42 美元，並將結果與 Opus 5.5 比較。

[相關資料 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [實機演示美式橄欖球遊戲](https://x.com/WesRoth/status/2119926801514529027) (作者 [@WesRoth](https://x.com/WesRoth))

**在體育原型中測試回饋和得分提示。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了 Fable 5.2 的實機畫面，展示了美式橄欖球得分提示。

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [用 Higgsfield MCP 製作開放世界首領戰](https://x.com/higgsfield_ai/status/2119926932343324795) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**區分可玩的遊戲部分和過場動畫。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ 播放影片</a>

Higgsfield 稱用 Fable 5.2 與自家的 MCP 製作了一款瀏覽器遊戲，包括開放世界、三幕首領戰和過場動畫。

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [潮汐變化中的聖米歇爾山](https://x.com/loktar00/status/2119927152489472076) (作者 [@loktar00](https://x.com/loktar00))

**在微縮歷史場景裡測試水位變化。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了帶潮汐動畫的微縮聖米歇爾山。

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [在 Blender 中檢視 Roblox 資產](https://x.com/hiyouwhatsapp/status/2119927163264573642) (作者 [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**匯入前先在 Blender 中檢查資產。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了面向 Roblox 開發、接近一次提示完成的 Blender 成果。

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [不輸出思維鏈的推理評測](https://x.com/Tim_Hua_/status/2119927284761293089) (作者 [@Tim_Hua_](https://x.com/Tim_Hua_))

**在同樣的推理輸出限制下比較答案。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

評測者執行了不輸出思維鏈的推理與知識測試，稱 Fable 5.2 略低於 GPT-6.1 Sol。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [四款模型重製 Chrome 恐龍遊戲](https://x.com/noclipepe/status/2119927838321328577) (作者 [@noclipepe](https://x.com/noclipepe))

**用同一個遊戲需求比較任務耗時和成本。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ 播放影片</a>

創作者在已有的 T-Rex 測試中加入 Fable 5.2，並並排展示它與 Opus、Gemini 和 Astra 的結果。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [用機械臂下西洋跳棋](https://x.com/karolina_dubiel/status/2119928342115676576) (作者 [@karolina_dubiel](https://x.com/karolina_dubiel))

**讀取關節位置，對未抓住的棋子重試。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ 播放影片</a>

創作者稱模型修正了約 7 毫米的下垂，並根據回饋重試未成功的動作。

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [十五秒動態影像短片](https://x.com/aziz4ai/status/2119928581405200726) (作者 [@aziz4ai](https://x.com/aziz4ai))

**記錄短篇程式碼動畫測試消耗的額度。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了一段用程式碼製作的 15 秒片段，稱用了每週額度的 4%。

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [可互動遊玩的埃菲爾鐵塔場景](https://x.com/bobyau/status/2119928812628771212) (作者 [@bobyau](https://x.com/bobyau))

**檢驗地標模型能否支援互動。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了埃菲爾鐵塔演示，稱建構耗時 25 分鐘。

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [用 Three.js 和 Higgsfield 製作海上競速](https://x.com/higgsfield_ai/status/2119928918035910668) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**在混合製作流程中區分遊戲邏輯和媒體工具。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ 播放影片</a>

Higgsfield 展示了一款有大浪、五名 AI 對手和追蹤火箭的競速遊戲。

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [WebGL 即時蜂蜜模擬](https://x.com/deedydas/status/2119930300990177509) (作者 [@deedydas](https://x.com/deedydas))

**用瀏覽器內的物理模擬測試材質運動。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ 播放影片</a>

作者分享了即時 WebGL 蜂蜜模擬，並公開了原始簡短需求。

原始提示詞

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [給實拍影片新增程式化特效](https://x.com/ashebytes/status/2119930763105931649) (作者 [@ashebytes](https://x.com/ashebytes))

**檢查特效在原影片中的時機和位置。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了 Fable 5.2 特效測試，將動畫圖形合成到實拍畫面上。

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [GTA 通緝等級的動態解說](https://x.com/saimagnate/status/2119931563760632311) (作者 [@saimagnate](https://x.com/saimagnate))

**用遊戲畫面搭配圖示解釋遊戲機制。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ 播放影片</a>

作者表示這是 Fable 5.2 一次產出的成果。影片用遊戲畫面與圖示比較 GTA V 和 RDR2 的通緝機制。

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [用程式碼搭建風格化 MMO 世界](https://x.com/Izkimar/status/2119931740940640542) (作者 [@Izkimar](https://x.com/Izkimar))

**透過風格化資產判斷整個世界的視覺一致性。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ 播放影片</a>

創作者稱在一天內建構了演示中的 MMO 世界，資產均由程式碼生成。

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [Fable 和 Opus 的 3D 場景對照](https://x.com/dom_scholz/status/2119933150025363661) (作者 [@dom_scholz](https://x.com/dom_scholz))

**並排比較準備耗時和輸出細節。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ 播放影片</a>

作者分享了 Fable 5.2 和 Opus 5.5 的兩段渲染，稱 Fable 執行更快。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [遊戲暫停介面的冗餘文案](https://x.com/AndrewPrifer/status/2119934600608915465) (作者 [@AndrewPrifer](https://x.com/AndrewPrifer))

**檢查生成的介面文案是否重複解釋。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

開發者以暫停介面為例，指出 Fable 5.2 寫了超出需要的說明文字。

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [在 Krea 執行環境中製作情緒板](https://x.com/lambdacalcc/status/2119934725662060663) (作者 [@lambdacalcc](https://x.com/lambdacalcc))

**選定視覺方向前先比較幾組概念。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

創作者分享了使用 Fable 5.2 配合 Krea 執行環境製作的四個情緒板輸出。

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [在辦公室試玩傳送門射擊遊戲](https://x.com/_sholtodouglas/status/2119935331499925557) (作者 [@_sholtodouglas](https://x.com/_sholtodouglas))

**透過多人試玩評估生成的遊戲。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ 播放影片</a>

一位 Anthropic 工程師分享了帶傳送門的第一人稱競技場射擊遊戲，並介紹了辦公室試玩。

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Blender 硬表面資產細節](https://x.com/ziwenxu_/status/2119937420280168929) (作者 [@ziwenxu_](https://x.com/ziwenxu_))

**在 Blender 視埠檢查拓撲和輪廓。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了作為 Fable 5.2 Blender 成果展示的硬表面資產。

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [不同推理強度的並行前端測試](https://x.com/AI_masaou/status/2119937635322085640) (作者 [@AI_masaou](https://x.com/AI_masaou))

**在多個推理強度下比較簡單和複雜需求。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

作者稱 Fable 與 Opus 在簡單任務中的成果相近，Fable 在規模更大的構建中細節更豐富，從 Medium 提升到 High 時耗時和 token 用量明顯增加。

[相關資料 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [十條提示詞做出一款小遊戲](https://x.com/AmirMushich/status/2119937977426338283) (作者 [@AmirMushich](https://x.com/AmirMushich))

**記錄遊戲原型的反覆調整的次數和檔案大小。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ 播放影片</a>

創作者稱遊戲大小為 220 KB，約有 3,400 行程式碼，並分享了程式碼和影片。

[相關資料 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [用 JavaScript 逐格繪製動畫](https://x.com/kevin_t_ngo/status/2119938129079808282) (作者 [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**檢查由程式逐格繪製的序列。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ 播放影片</a>

作者分享了動畫，稱每一格都由 JavaScript 繪製。

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [根據參考影片製作 3D 動畫](https://x.com/KHvostikk/status/2119939061049889130) (作者 [@KHvostikk](https://x.com/KHvostikk))

**判斷重建場景時與原始影片對照。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了 Fable 5.2 將影片轉成 3D 動畫的演示。

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Fable 和 Opus 的像素篝火對照](https://x.com/GrilliotTodd/status/2119939651385655692) (作者 [@GrilliotTodd](https://x.com/GrilliotTodd))

**比較同一像素畫題材中的光照和輪廓。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ 播放影片</a>

並排結果展示了 Fable 5.2 和 Opus 5.5 對同一篝火題材的繪製。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [Arena WebDev 的 xHigh 評測](https://x.com/arena/status/2119941204003770690) (作者 [@arena](https://x.com/arena))

**比較榜單結果時核對所用推理強度。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena 報告，Claude Fable 5.2 xHigh 首次登上 Code Arena WebDev 時獲得 1,832 分。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [兩款模型製作的電影預告片字幕](https://x.com/muku_sns/status/2119941490969624679) (作者 [@muku_sns](https://x.com/muku_sns))

**比較對同一段文字的兩種演繹。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ 播放影片</a>

作者並排展示了 Opus 和 Fable 設計的預告片字幕。Fable 版本加入了紅色邊框元素和塗黑遮蓋的文字。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [單提示詞動效與 3D 作品測試](https://x.com/Khazix0918/status/2119941585538572390) (作者 [@Khazix0918](https://x.com/Khazix0918))

**在創作需求中分別考察調研、設計和渲染。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ 播放影片</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ 播放影片</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ 播放影片</a></td></tr></table>

作者分享了四次執行，分別製作 ChatGPT 週年紀念短片、DeepSeek 解說、Three.js 場景和 Apple 靜安的 3D 重現。

[相關資料 1](https://x.com/Khazix0918/article/2119941585538572390)

原始提示詞

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [可互動拆解的核反應爐解說](https://x.com/konstantinsaifo/status/2119941967136379334) (作者 [@konstantinsaifo](https://x.com/konstantinsaifo))

**透過拆解互動展示各零件如何組合。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ 播放影片</a>

創作者要求製作可拆解的 Three.js 反應爐模型，稱 API 花費為 92 美元。

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Blood on the Clocktower 代理程式測試](https://x.com/dwarkesh_sp/status/2119942657812451482) (作者 [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**讓多個模型參與同一款隱藏身分遊戲。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

評測者稱，這項基準中 Fable 5.2 高於 Fable 5.1 和 Opus 5.5，GPT-6 Astra 則領先。

[相關資料 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [飛梭競速原型](https://x.com/loktar00/status/2119943124965638444) (作者 [@loktar00](https://x.com/loktar00))

**用熟悉的競速形式判斷運動表現和操控。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了 Fable 5.2 生成的飛梭競速風格作品。

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [十秒 Claude 內褲廣告](https://x.com/Masimo_Blue/status/2119943368612487285) (作者 [@Masimo_Blue](https://x.com/Masimo_Blue))

**用寬泛的產品需求測試原創配樂的廣告製作。**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ 播放影片</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

創作者分享了一段十秒宣傳影片，其中使用了 Acid Techno 音樂和提供的產品圖片。

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [一筆一筆繪製日出中的鳥](https://x.com/mgrczyk/status/2119943813028548721) (作者 [@mgrczyk](https://x.com/mgrczyk))

**停用撤銷，觀察逐筆繪畫的決策。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ 播放影片</a>

創作者展示了一幅逐筆繪製的日出鳥景，執行環境禁止修改已經落下的筆畫。

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [在 Devin 中執行高負荷圖形任務](https://x.com/Da7_Tech/status/2119944847255896490) (作者 [@Da7_Tech](https://x.com/Da7_Tech))

**測試複雜渲染時記錄耗時和花費。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ 播放影片</a>

一位公開身份的 Cognition 推廣大使分享了 Devin Max 的執行結果，稱耗時約 3.5 小時、花費約 82 美元。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [三個模型的程式碼繪畫對照](https://x.com/kickingkeys/status/2119945841997672698) (作者 [@kickingkeys](https://x.com/kickingkeys))

**比較繪畫動作和合成音效。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了一段帶聲音的程式碼繪畫，並介紹了對 Fable 5.2、Fable 5.1 和 Gemini 4 Argon 使用相同提示詞的測試。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [動畫演繹書寫史](https://x.com/rileybrown/status/2119946022767980985) (作者 [@rileybrown](https://x.com/rileybrown))

**用時間線組織程式碼生成的解說片。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ 播放影片</a>

創作者展示了書寫史動畫，稱只用了一條提示詞。

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [遊戲機械裝置試驗場](https://x.com/techartist_/status/2119946891106394518) (作者 [@techartist_](https://x.com/techartist_))

**在同一場景中測試玩法機制、物理和特效。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ 播放影片</a>

創作者用 Three.js 和 Blender 搭建了可測試四個概念的場地。

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [手持 Linux 遊戲機的 PCB 設計](https://x.com/seveibar/status/2119947341230907453) (作者 [@seveibar](https://x.com/seveibar))

**在相同電路需求下比較兩款模型的設計。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ 播放影片</a>

tscircuit 創作者展示了使用 Astra 6 High 和 Fable 5.2 High 設計手持 Linux 遊戲裝置的測試。

原始提示詞

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [體素湖泊場景](https://x.com/Angaisb_/status/2119947748690841841) (作者 [@Angaisb_](https://x.com/Angaisb_))

**用小型環境需求測試構圖。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了歸因於 Fable 5.2 的體素湖泊。

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [Arena 的 17 個互動生成作品](https://x.com/arena/status/2119948067449536733) (作者 [@arena](https://x.com/arena))

**選定評測任務前先瀏覽多種輸出。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ 播放影片</a>

Arena 分享了 17 個生成作品，涵蓋 3D 世界、遊戲、介面、資料視覺化和程式碼動畫。

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [和友善的龍一起飛行](https://x.com/chetanankola/status/2119951015407738913) (作者 [@chetanankola](https://x.com/chetanankola))

**用一段循環飛行測試鏡頭和運動。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了以 Three.js 和 Blender 製作的龍場景，並描述了用 Fable 5.2 改進的部分。

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Fable 和 Opus 的果凍虎鯨對照](https://x.com/vib3coded/status/2119951060752375827) (作者 [@vib3coded](https://x.com/vib3coded))

**比較同一主體的表面質感和運動。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ 播放影片</a>

創作者並排展示了 Fable 5.2 和 Opus 5.5 的果凍虎鯨效果。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [開放式影片品質測試](https://x.com/suna_gaku/status/2119952985933697063) (作者 [@suna_gaku](https://x.com/suna_gaku))

**給出寬泛的創作需求，觀察模型如何取捨。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ 播放影片</a>

創作者讓模型展示其最拿手的影片作品，並分享了結果。

原始提示詞

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [地中海主題太空居住站](https://x.com/MaxXWilliamson/status/2119953172634677533) (作者 [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**將簡短設計需求與現有專案工具結合。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ 播放影片</a>

創作者提供了以往製作太空居住站時用過的工具，要求製作一座地中海主題空間站。

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [AA-3D 互動體驗基準](https://x.com/ArtificialAnlys/status/2119953570430881946) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**結合不確定區間解讀 Elo。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ 播放影片</a>

Artificial Analysis 報告，Fable 5.2 Max 在其互動式 3D 基準中發布時的 Elo 為 1,271。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [帶倒數計時的骷髏角色遊戲](https://x.com/WesRoth/status/2119953913160093817) (作者 [@WesRoth](https://x.com/WesRoth))

**給可玩原型加上可見的計時器。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ 播放影片</a>

創作者展示了 Fable 5.2 一次生成的結果，畫面有骷髏角色和倒數計時。

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Fable 與 Astra 的像素畫對照](https://x.com/Angaisb_/status/2119955179915137294) (作者 [@Angaisb_](https://x.com/Angaisb_))

**在同一輸出尺寸下比較形狀和細節。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ 播放影片</a>

原始貼文展示了 GPT-6 Astra 與 Fable 5.2 的像素畫作品。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [動態設計作品集短片](https://x.com/Leviwoyun/status/2119955625820258308) (作者 [@Leviwoyun](https://x.com/Leviwoyun))

**給出開放式作品集需求，同時限定時長。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ 播放影片</a>

作者分享了一段帶配樂的動態影像作品集短片，稱製作耗時 24 分鐘。

原始提示詞

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [兩個模型渲染玻璃泳池](https://x.com/MrTacticalX/status/2119955647542542439) (作者 [@MrTacticalX](https://x.com/MrTacticalX))

**結合耗時與成本比較光照效果。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ 播放影片</a>

創作者稱，這次渲染測試中 Fable 耗時 90 分鐘、花費 57.87 美元，Opus 耗時 68 分鐘、花費 14.39 美元。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [TS-Bench 工具呼叫準確率](https://x.com/gosrum/status/2119956559031927079) (作者 [@gosrum](https://x.com/gosrum))

**分別記錄工具呼叫錯誤和 token 用量。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

測試者稱 Fable 5.2 沒有工具呼叫錯誤，並指出較簡單的任務難以區分 Claude 各型號。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [微縮馬丘比丘](https://x.com/loktar00/status/2119958719362666708) (作者 [@loktar00](https://x.com/loktar00))

**觀察微縮場景的氛圍和細節。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ 播放影片</a>

分享的馬丘比丘演示包含體積霧和小羊駝。

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [按專業任務分類的 GDPx 結果](https://x.com/SemiAnalysis_/status/2119961447199289640) (作者 [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**檢視總分的同時比較子任務結果。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

評測發布方報告總分為 16.4%，並列出晶片設計、軟體工程等領域的細分結果。

[相關資料 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [相關資料 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [相關資料 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [在繪圖應用程式中畫肖像](https://x.com/The_Alex/status/2119964472559489229) (作者 [@The_Alex](https://x.com/The_Alex))

**用參考縮圖輔助繪製肖像。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ 播放影片</a>

作者請 Fable 5.2 開啟繪圖應用程式畫自己的肖像。影片呈現從輪廓到完成的過程。

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [Low 推理強度下的 VulcanBench Frontier v4](https://x.com/morganlinton/status/2119966067527467215) (作者 [@morganlinton](https://x.com/morganlinton))

**在相同推理強度下比較不同代模型。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

評測作者稱，在 Low 推理強度下，Fable 5.2 和 5.1 每項任務分別約耗時 5 分鐘和 26 分鐘。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [後室遊戲的角色反轉](https://x.com/LexnLin/status/2119966127149429093) (作者 [@LexnLin](https://x.com/LexnLin))

**改變玩家目標來檢驗遊戲創意。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ 播放影片</a>

玩家操控怪物抓人。創作者分享了實機片段和試玩連結。

[相關資料 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [在 Blender 中製作 Bugatti Tourbillon](https://x.com/xikhar/status/2119966147328299284) (作者 [@xikhar](https://x.com/xikhar))

**用參考圖說明外觀和內裝細節。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ 播放影片</a>

創作者稱使用提示詞和參考圖完成了 Bugatti Tourbillon 的建模，包括內裝，並渲染了電影式片段。

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [用兩個模型製作電腦主題影片](https://x.com/daradoescode/status/2119966154391183522) (作者 [@daradoescode](https://x.com/daradoescode))

**記錄每個模型在混合工作流中的貢獻。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了使用 Fable 5.2 製作的風格化影片，其中 Opus 5.5 也承擔了大量工作。

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [關於 Megakernel 的音樂影片](https://x.com/elliotarledge/status/2119968762069934415) (作者 [@elliotarledge](https://x.com/elliotarledge))

**用技術概念作為影片主題。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ 播放影片</a>

創作者以 High 推理強度讓 Fable 5.2 製作 Megakernel 主題的音樂影片，並分享了片段。

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [根據參考照片製作工作室導覽](https://x.com/rpnickson/status/2119969928304357507) (作者 [@rpnickson](https://x.com/rpnickson))

**用真實照片輔助還原場景。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ 播放影片</a>

創作者提供了工作室的照片，改編了類似的影片需求，並稱這次生成約耗時兩小時。

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [用程式碼製作 1990 年代風格的玩具廣告](https://x.com/kevin_t_ngo/status/2119972124211454139) (作者 [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**將動畫腳本編寫與渲染分開。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ 播放影片</a>

創作者稱使用 Python 為復古玩具廣告製作動畫，再用 Blender 渲染。

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Three.js 第三人稱遊戲場景](https://x.com/bijanbowen/status/2119972220739187182) (作者 [@bijanbowen](https://x.com/bijanbowen))

**用實機遊玩片段檢查運動與場景。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

作者分享了直播中的 Three.js 成果，顯示第三人稱角色在戶外環境中移動。

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [基於現有渲染器製作 Bryceball](https://x.com/pleometric/status/2119973274402668852) (作者 [@pleometric](https://x.com/pleometric))

**重複利用渲染引擎作為遊戲的基礎。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ 播放影片</a>

創作者將關聯貼文中介紹的渲染器改造成了可玩的 Bryceball。

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [用 Fable 二次剪輯影片](https://x.com/rileybrown/status/2119973951027724385) (作者 [@rileybrown](https://x.com/rileybrown))

**把此前的剪輯用作後續作品的素材。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ 播放影片</a>

創作者分享了一段 Fable 5.2 剪輯的影片，內容圍繞自己先前用該模型剪輯的另一段影片。

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [電影式科學史](https://x.com/DeryaTR_/status/2119974354260013293) (作者 [@DeryaTR_](https://x.com/DeryaTR_))

**用時間線組織 3D 敘事。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ 播放影片</a>

創作者要求呈現一段從早期科學走向想像中未來的電影式旅程，並分享了成片。

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [達芬奇飛行器的 3D 模型](https://x.com/higgsfield_ai/status/2119975721909301684) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**先建模還原歷史設計，再測試改動。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ 播放影片</a>

Higgsfield 展示了達芬奇飛行器的 3D 版本，並介紹了物理測試與重新設計的過程。

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [按設計要求完成 PCB 佈線](https://x.com/cmonkey/status/2119975852977029365) (作者 [@cmonkey](https://x.com/cmonkey))

**在製作電路板前檢查佈線。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

作者在討論電路版面的後續貼文中分享了 Fable 5.2 的 PCB 佈線結果。

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [在不同執行環境中使用同一提示詞](https://x.com/loktar00/status/2119980613369319706) (作者 [@loktar00](https://x.com/loktar00))

**比較模型輸出時記錄執行環境的差異。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ 播放影片</a>

創作者在不同執行環境中給 DeepSeek 和 Fable 5.2 同一提示詞，並展示了兩組結果。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [用程式碼繪製哥斯拉](https://x.com/chetaslua/status/2119981510199808368) (作者 [@chetaslua](https://x.com/chetaslua))

**用近似向量的形狀和動態效果重新演繹影像。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ 播放影片</a>

創作者受一則哥斯拉貼文啟發，分享了程式碼繪製的畫面和短動畫。

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [面向 3D 列印的手持風扇](https://x.com/davelee/status/2119981787325579398) (作者 [@davelee](https://x.com/davelee))

**用實體原型檢查建模後的裝配效果。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ 播放影片</a>

創作者與孩子們一起設計了可列印的手持風扇，並在列印前分享了模型。

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [與 Opus 對比排查外掛問題](https://x.com/oaranda/status/2119982729747919096) (作者 [@oaranda](https://x.com/oaranda))

**用交叉迴歸測試比較修復結果。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

作者標註的發布公告節錄。

兩個模型找到了相同的六個外掛問題。Opus 通過了交叉測試，Fable 有一項未通過，但另外發現了儀表板的問題。

原始提示詞

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [以 3D 場景重建伊斯坦布林](https://x.com/petergostev/status/2119877733488394520) (作者 [@petergostev](https://x.com/petergostev))

**從遠景和近景檢查城市規模的場景。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ 播放影片</a>

Peter Gostev 分享了 Fable 5.2 Max 製作的伊斯坦布林 3D 場景，並附上更詳盡的評估。

[相關資料 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [帶動態螢幕的 Blender 工作室短片](https://x.com/rileybrown/status/2119902109709537708) (作者 [@rileybrown](https://x.com/rileybrown))

**在同一 3D 場景中製作螢幕內容、燈光和鏡頭動畫。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ 播放影片</a>

創作者稱使用了 13 個鏡頭、筆記型電腦的螢幕上播放的客製網頁和 ElevenLabs 音訊，並用 RunPod GPU 渲染。

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [弱耦合下的黑洞躍遷](https://hexagonmath.org/2611.00175v1) (作者 [@Anthropic](https://www.anthropic.com/))

**回到原始理論設定檢查一項未完成的推導。**

Anthropic 報告稱，Fable 5.2 完成了一項長期未完成的計算，並在弱耦合範圍發現突變。預印本給出了推導。

[相關資料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [模自助方法的界限](https://hexagonmath.org/2611.00174v1) (作者 [@Anthropic](https://www.anthropic.com/))

**在提出解析界限時一併公開推導。**

Anthropic 報告稱，Fable 5.2 確定了在簡化量子引力設定中使用的無自旋模自助方法的精確極限。

[相關資料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Vercel AI Gateway 中按順序備援模型](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (作者 [Vercel](https://vercel.com/))

**為被分類器拒絕的請求設定網關備援順序。**

Vercel 的 AI SDK 示例呼叫 anthropic/claude-fable-5.2，將 Opus 5.5 和 Sonnet 5.5 依次設為備援模型。文件說明了閘道的資料留存要求。

[相關資料 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [巢狀子代理程式與程式碼審查預算](https://news.ycombinator.com/item?id=50430925) (作者 [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**跟蹤巢狀委派，並在提示詞之外設定審查預算上限。**

作者審查 80,000 行程式碼時要求最多使用四個子代理程式，稱實際上出現了六個或更多巢狀代理程式，不到 20 分鐘便耗盡五小時使用額度。

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [將 LCARS 設計轉換為 HTML 的對照](https://news.ycombinator.com/item?id=50430962) (作者 [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**將曲線、圖示還原程度、動畫和導航分別設為驗收項。**

作者用相同的《星際迷航》風格設計比較 Fable 5.2 和 Opus 5.5。作者更喜歡 Fable 的曲線和部分圖示，也更喜歡 Opus 的動畫，認為 Fable 的 SVG 閃爍影響體驗。要求僅製作第一頁。

[相關資料 1](https://html.non.io/lcars-fable-5.2/) · [相關資料 2](https://html.non.io/lcars-opus-5.5/) · [相關資料 3](https://news.ycombinator.com/item?id=50431231) · [相關資料 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [Quantum ESPRESSO 的 GPU 最佳化](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (作者 [Discovered Materials](https://discoveredmaterials.com/))

**最佳化科學軟體時要求提供參考結果和有代表性的隱藏測試。**

Discovered Materials 報告稱，同一 GPU 上的 13 項聲子基準測試的加速比幾何平均值為 36 倍，混合泛函計算約為 9 倍。公開的修補程式以正確性和效能測試為依據。

[相關資料 1](https://github.com/discovered-materials/dm_qe) · [相關資料 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [按推理強度檢視 Artificial Analysis 智慧指數](https://artificialanalysis.ai/models/claude-fable-5-2) (作者 [Artificial Analysis](https://artificialanalysis.ai/))

**在所選推理強度下同時檢視得分、任務成本與延遲。**

引用的 Max 預設備援快照顯示指數為 65，單項任務成本 26.54 美元，耗時 46.4 分鐘。這些數字對應評測任務。

[相關資料 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [High 推理強度下變更審查的誤報](https://news.ycombinator.com/item?id=50431810) (作者 [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**採取行動前，先比對程式碼核實模型的審查結果。**

開發者稱 Fable 5.2 High 在審查變更時標出了兩個不存在的問題，開發者憑對程式碼的瞭解識別了誤報。

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [三十項常規程式設計任務](https://news.ycombinator.com/item?id=50432483) (作者 [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**用同一批程式設計任務比較耗時和完成數。**

作者稱 Fable 5.2 和 Opus 5.5 均完成了 30 項中的 26 項，Fable 5.1 完成 25 項。Fable 5.2 的耗時為 5.1 的 0.62 倍，作者未報告安全機制導致的中斷。

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [荒島求生螢幕保護程式](https://news.ycombinator.com/item?id=50432836) (作者 [@nzach](https://news.ycombinator.com/user?id=nzach))

**直接開啟可玩的頁面檢查模型製作的螢幕保護程式。**

Show HN 作者連結了名為 Stranded with Claude 的瀏覽器荒島場景，作品以互動式畫布呈現。

[相關資料 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [High 推理強度下的三項瀏覽器遊戲測試](https://senko.net/vibecode-bench/) (作者 [Senko Rašić](https://senko.net/))

**在遊戲評測中分開衡量玩法和畫面還原度。**

Senko Rašić 在 Claude Code 中用 Fable 5.2 測試了即時戰略、體素和飛行模擬需求。作者稱它做出了飛艇等可探索全地圖的機制，但認為部分畫面表現較差。

[相關資料 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [逐章生成書評播客指令碼](https://news.ycombinator.com/item?id=50434156) (作者 [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**對同樣的播客任務比較指令碼篇幅。**

作者逐章生成兩位書評人之間的對話，稱 Fable 版本約 2.5 頁，Opus 5.5 版本約 4.5 頁，並附上兩組示例。

[相關資料 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [相關資料 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [用 Rust 遷移生產服務](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (作者 [@Anthropic](https://www.anthropic.com/))

**對比遷移前後的啟動表現。**

Anthropic 報告稱，執行預發布版 Fable 5.2 的代理程式用 Rust 重寫了一項 Python 生產服務，將啟動耗時縮短到原來的約 1/26。

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [在 GitHub Copilot 中選用 Fable 5.2](https://x.com/github/status/2119926269982961833) (作者 [@github](https://x.com/github))

**先啟用組織原則，再選取模型。**

GitHub 文件說明了 Copilot 用戶端的模型選擇器，以及 Business 和 Enterprise 帳戶所需的管理員設定。

[相關資料 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [百頁 HTML 設計挑戰](https://x.com/MiaAI_lab/status/2119930229661503893) (作者 [@MiaAI_lab](https://x.com/MiaAI_lab))

**除了視覺品質，也要統計完成且能執行的檔案。**

作者要求製作 100 個不同設計，發布了 76 個檔案及提示詞，並稱用完了 Fable 使用額度。

[相關資料 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [相關資料 2](https://mia-ai.net/lab/experiments/100-htmls) · [相關資料 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [相關資料 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [相關資料 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [相關資料 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [相關資料 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [相關資料 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [相關資料 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [相關資料 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [相關資料 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [相關資料 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [相關資料 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [相關資料 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [編譯器任務中的需求偏移](https://x.com/sameQCU/status/2119939304864800971) (作者 [@sameQCU](https://x.com/sameQCU))

**把代理程式複述的需求與輸入逐項對照。**

開發者描述了一個編譯器任務，其中 Fable 5.2 和較早的 Opus 模型都錯誤複述了收到的要求。

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [用 Opus 追蹤長時間執行的 Fable 任務](https://x.com/marouane53/status/2119950129767858262) (作者 [@marouane53](https://x.com/marouane53))

**用獨立對話追蹤長任務的進度。**

作者表示，部分 Fable 任務執行超過兩小時，進度更新很少。他在另一段對話中請 Opus 5.5 解釋進度與決策。

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [用全新視角複查程式碼](https://x.com/doodlestein/status/2119958895158292786) (作者 [@doodlestein](https://x.com/doodlestein))

**單獨複查新增和改動過的檔案。**

創作者分享了兩條原始後續提示詞，用於在實作完成後找出並修正問題。

原始提示詞

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

原始提示詞

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [功能設計審查中的偏移](https://news.ycombinator.com/item?id=50434214) (作者 [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**用現有設計作為清單檢查代理程式的後續建議。**

作者在功能設計審查中比較模型，更喜歡 Opus 5.5。後續 Fable 5.2 的診斷提出了一項設計中已存在的建議。

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [DX Ball 風格打磚塊遊戲對比](https://news.ycombinator.com/item?id=50434424) (作者 [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**在重現需求中分別比較遊戲機制和操作手感。**

作者連結了 Fable 5.2 與 Opus 5.5 的獨立執行版本。Fable 改動了原作部分機制，作者更喜歡 Opus 版本的操作手感。

[相關資料 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [相關資料 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [改進 3D 應用的試驗](https://news.ycombinator.com/item?id=50434433) (作者 [@user43928](https://news.ycombinator.com/user?id=user43928))

**在相同的改進任務中比較可見變化和預算消耗。**

作者稱讓 Fable 5.2 改進一款非遊戲 3D 應用，結果與 Opus 5.5 差異不大，並在當晚用掉 Fable 方案額度的 25%。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [三個模型製作貓鼠遊戲](https://news.ycombinator.com/item?id=50434508) (作者 [@simonw](https://news.ycombinator.com/user?id=simonw))

**固定遊戲提示詞，檢查每個模型的可玩成果。**

Simon Willison 分享了 Fable 5.2 Extra、Opus 5.5 Extra 和 GPT-6 Extra High 製作的移動端友好 Three.js 遊戲，稱 Fable 版本耗時約 40 分鐘。

[相關資料 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [相關資料 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [相關資料 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

原始提示詞

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [AIBenchy 的 High 推理強度成本與得分](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (作者 [AIBenchy](https://aibenchy.com/))

**在相同強度標籤下比較得分、總成本與響應時間。**

AIBenchy 公佈的結果顯示，Fable 5.2 High 和 Opus 5.5 High 的得分分別為 8.7 和 9.4，總成本為 5.083 和 2.133 美元，平均響應時間為 14.73 和 27.55 秒。

[相關資料 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [調整 Fable 5.2 的代理程式配置](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (作者 [@Anthropic](https://www.anthropic.com/))

**重新測試推理強度，並為長任務設定進度更新規則。**

Anthropic 指南提供範例指令，涵蓋推理強度、完成標準、核准、進度更新和子代理限制。

[相關資料 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="acknowledge"></a>
## 作者致謝

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/)
