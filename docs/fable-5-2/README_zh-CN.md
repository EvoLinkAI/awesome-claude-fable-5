# Claude Fable 5.2 使用案例

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

汇集 11 月 10 日和 11 月 13–14 日收集的工作流、演示、对比、评测、集成与使用限制，并附原始来源。

[Anthropic 发布公告](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [历史案例库](../../README_zh-CN.md)

## 案例目录

| Case | 使用案例 | Type |
| --- | --- | --- |
| 330 | [不同推理力度下的 MacBook SVG 绘图](#case-330) | Benchmark |
| 331 | [用全家人的画做四人清版动作游戏](#case-331) | Demo |
| 332 | [三件电子设备从设计到装配](#case-332) | Demo |
| 333 | [用 Lean 形式化费马大定理](#case-333) | Evaluation |
| 334 | [从空文件夹开始构建操作系统](#case-334) | Demo |
| 335 | [RoboDojo 双臂操作评测](#case-335) | Benchmark |
| 336 | [运动中的喷泉](#case-336) | Demo |
| 337 | [用 Higgsfield 做逐帧对齐的口型同步](#case-337) | Integration |
| 338 | [开放世界驾驶游戏原型](#case-338) | Demo |
| 339 | [用参考图呈现 1940 年的巴黎](#case-339) | Integration |
| 340 | [Fable 规划、Opus 渲染的短片](#case-340) | Integration |
| 341 | [音乐视频实验](#case-341) | Demo |
| 342 | [Dario Amodei 的绘画肖像](#case-342) | Demo |
| 343 | [Medium 推理力度下的 Spud Smash](#case-343) | Demo |
| 344 | [Fable 与 Opus 的冰之教堂](#case-344) | Evaluation |
| 345 | [用声道仿真演唱](#case-345) | Demo |
| 346 | [伊斯坦布尔主题的三项体素测试](#case-346) | Evaluation |
| 347 | [Remote Labor Index 的项目完成率](#case-347) | Benchmark |
| 348 | [四种推理力度下的冰山场景](#case-348) | Evaluation |
| 349 | [七十九秒动画短片](#case-349) | Demo |
| 350 | [Fable 和 Opus 的机械总成对照](#case-350) | Evaluation |
| 351 | [机械手攀爬螺旋楼梯](#case-351) | Demo |
| 352 | [在 Blender 中为 Tripo 网格绑定骨骼](#case-352) | Evaluation |
| 353 | [把达芬奇手稿做成交互式发明展示](#case-353) | Demo |
| 354 | [由 Claude 操控的音乐工作站](#case-354) | Demo |
| 355 | [树莓派 5 产品动画](#case-355) | Demo |
| 356 | [意大利北部场景](#case-356) | Demo |
| 357 | [由本地工作智能体制作立体书](#case-357) | Evaluation |
| 358 | [重新启用熔岩灯测试](#case-358) | Evaluation |
| 359 | [在 Blender 中制作细节丰富的喷气机](#case-359) | Integration |
| 360 | [穿越数百个世界的传送门之旅](#case-360) | Demo |
| 361 | [用 Three.js 呈现孟买集市的六个镜头](#case-361) | Integration |
| 362 | [用代码构建写实美式餐馆](#case-362) | Integration |
| 363 | [在 Blender 中制作机器人模型](#case-363) | Demo |
| 364 | [为 Convex 制作动态解说片](#case-364) | Demo |
| 365 | [一次生成的落地页合集](#case-365) | Demo |
| 366 | [用 LilyPond 为钢琴奏鸣曲记谱](#case-366) | Demo |
| 367 | [自由发挥的视频需求](#case-367) | Demo |
| 368 | [Fable 规划、DeepSeek 实现、Opus 审查](#case-368) | Integration |
| 369 | [Fable 5.2 接入 AI Village](#case-369) | Integration |
| 370 | [有无 Skills 的前端设计对照](#case-370) | Evaluation |
| 371 | [查找代码库中的隐式状态机](#case-371) | Tutorial |
| 372 | [八小时从零做出一款游戏](#case-372) | Demo |
| 373 | [Fishslop 原型与 token 成本](#case-373) | Evaluation |
| 374 | [实机演示美式橄榄球游戏](#case-374) | Demo |
| 375 | [用 Higgsfield MCP 制作开放世界首领战](#case-375) | Integration |
| 376 | [潮汐变化中的圣米歇尔山](#case-376) | Demo |
| 377 | [在 Blender 中查看 Roblox 资产](#case-377) | Demo |
| 378 | [不输出思维链的推理评测](#case-378) | Benchmark |
| 379 | [四款模型重制 Chrome 恐龙游戏](#case-379) | Evaluation |
| 380 | [用机械臂下西洋跳棋](#case-380) | Demo |
| 381 | [十五秒动效短片](#case-381) | Demo |
| 382 | [可交互游玩的埃菲尔铁塔场景](#case-382) | Demo |
| 383 | [用 Three.js 和 Higgsfield 制作海上竞速](#case-383) | Integration |
| 384 | [WebGL 实时蜂蜜模拟](#case-384) | Demo |
| 385 | [给实拍视频添加程序化特效](#case-385) | Demo |
| 386 | [GTA 通缉等级的动态解说](#case-386) | Demo |
| 387 | [用代码搭建风格化 MMO 世界](#case-387) | Demo |
| 388 | [Fable 和 Opus 的 3D 场景对照](#case-388) | Evaluation |
| 389 | [游戏暂停界面的冗余文案](#case-389) | Limit |
| 390 | [在 Krea 运行框架中制作情绪板](#case-390) | Integration |
| 391 | [在办公室试玩传送门射击游戏](#case-391) | Demo |
| 392 | [Blender 硬表面资产细节](#case-392) | Demo |
| 393 | [不同推理力度的并行前端测试](#case-393) | Evaluation |
| 394 | [十条提示词做出一款小游戏](#case-394) | Demo |
| 395 | [用 JavaScript 逐帧绘制动画](#case-395) | Demo |
| 396 | [根据参考视频制作 3D 动画](#case-396) | Demo |
| 397 | [Fable 和 Opus 的像素篝火对照](#case-397) | Evaluation |
| 398 | [Arena WebDev 的 xHigh 评测](#case-398) | Benchmark |
| 399 | [两款模型制作的电影预告片字幕](#case-399) | Evaluation |
| 400 | [单提示词动效与 3D 作品测试](#case-400) | Evaluation |
| 401 | [可交互拆解的核反应堆解说](#case-401) | Demo |
| 402 | [Blood on the Clocktower 智能体测试](#case-402) | Benchmark |
| 403 | [飞梭竞速原型](#case-403) | Demo |
| 404 | [十秒 Claude 内裤广告](#case-404) | Demo |
| 405 | [一笔一笔绘制日出中的鸟](#case-405) | Demo |
| 406 | [在 Devin 中运行高负荷图形任务](#case-406) | Evaluation |
| 407 | [三个模型的代码绘画对照](#case-407) | Evaluation |
| 408 | [动画演绎书写史](#case-408) | Demo |
| 409 | [游戏机械装置试验场](#case-409) | Demo |
| 410 | [手持 Linux 游戏机的 PCB 设计](#case-410) | Evaluation |
| 411 | [体素湖泊场景](#case-411) | Demo |
| 412 | [Arena 的 17 个交互生成作品](#case-412) | Demo |
| 413 | [和友善的龙一起飞行](#case-413) | Demo |
| 414 | [Fable 和 Opus 的果冻虎鲸对照](#case-414) | Evaluation |
| 415 | [开放式视频质量测试](#case-415) | Demo |
| 416 | [地中海主题太空居住站](#case-416) | Demo |
| 417 | [AA-3D 交互体验基准](#case-417) | Benchmark |
| 418 | [带倒计时的骷髅角色游戏](#case-418) | Demo |
| 419 | [Fable 与 Astra 的像素画对照](#case-419) | Evaluation |
| 420 | [动态设计作品集短片](#case-420) | Demo |
| 421 | [两个模型渲染玻璃泳池](#case-421) | Evaluation |
| 422 | [TS-Bench 工具调用准确率](#case-422) | Benchmark |
| 423 | [微缩马丘比丘](#case-423) | Demo |
| 424 | [按专业任务分类的 GDPx 结果](#case-424) | Benchmark |
| 425 | [在绘图应用里画肖像](#case-425) | Demo |
| 426 | [Low 推理力度下的 VulcanBench Frontier v4](#case-426) | Benchmark |
| 427 | [可玩的后室角色反转游戏](#case-427) | Demo |
| 428 | [在 Blender 中制作 Bugatti Tourbillon](#case-428) | Demo |
| 429 | [用两个模型制作电脑主题视频](#case-429) | Demo |
| 430 | [关于 Megakernel 的音乐视频](#case-430) | Demo |
| 431 | [根据参考照片制作工作室导览](#case-431) | Demo |
| 432 | [用代码制作 1990 年代风格的玩具广告](#case-432) | Demo |
| 433 | [Three.js 第三人称游戏场景](#case-433) | Demo |
| 434 | [基于现有渲染器制作 Bryceball](#case-434) | Demo |
| 435 | [用 Fable 二次剪辑视频](#case-435) | Demo |
| 436 | [电影式科学史](#case-436) | Demo |
| 437 | [达芬奇飞行器的 3D 模型](#case-437) | Integration |
| 438 | [按设计要求完成 PCB 布线](#case-438) | Demo |
| 439 | [在不同运行框架中使用同一提示词](#case-439) | Evaluation |
| 440 | [用代码绘制哥斯拉](#case-440) | Demo |
| 441 | [面向 3D 打印的手持风扇](#case-441) | Demo |
| 442 | [与 Opus 对比排查插件缺陷](#case-442) | Evaluation |
| 443 | [以 3D 场景重建伊斯坦布尔](#case-443) | Demo |
| 444 | [带动态屏幕的 Blender 工作室短片](#case-444) | Demo |
| 445 | [弱耦合下的黑洞跃迁](#case-445) | Evaluation |
| 446 | [模自举方法的界限](#case-446) | Evaluation |
| 447 | [Vercel AI Gateway 中按顺序回退模型](#case-447) | Integration |
| 448 | [嵌套子智能体与代码审查预算](#case-448) | Limit |
| 449 | [将 LCARS 设计转换为 HTML 的对照](#case-449) | Evaluation |
| 450 | [Quantum ESPRESSO 的 GPU 优化](#case-450) | Benchmark |
| 451 | [按推理力度查看 Artificial Analysis 智能指数](#case-451) | Benchmark |
| 452 | [High 推理力度下变更审查的误报](#case-452) | Limit |
| 453 | [三十项常规编程任务](#case-453) | Evaluation |
| 454 | [荒岛求生屏保](#case-454) | Demo |
| 455 | [High 推理力度下的三项浏览器游戏测试](#case-455) | Evaluation |
| 456 | [逐章生成书评播客脚本](#case-456) | Evaluation |
| 457 | [用 Rust 迁移生产服务](#case-457) | Evaluation |
| 458 | [在 GitHub Copilot 中选择 Fable 5.2](#case-458) | Integration |
| 459 | [百页 HTML 设计挑战](#case-459) | Evaluation |
| 460 | [编译器任务中的需求偏移](#case-460) | Limit |
| 461 | [用 Opus 跟踪长时间运行的 Fable 任务](#case-461) | Integration |
| 462 | [用全新视角复查代码](#case-462) | Tutorial |
| 463 | [功能设计审查中的偏移](#case-463) | Limit |
| 464 | [DX Ball 风格打砖块游戏对比](#case-464) | Evaluation |
| 465 | [改进 3D 应用的试验](#case-465) | Evaluation |
| 466 | [三个模型制作猫鼠游戏](#case-466) | Evaluation |
| 467 | [AIBenchy 的 High 推理力度成本与得分](#case-467) | Benchmark |
| 468 | [调整 Fable 5.2 的 Agent 运行配置](#case-468) | Tutorial |
| 469 | [动态角色预览应用](#case-469) | Demo |
| 470 | [测试无工具生成的二维码](#case-470) | Evaluation |
| 471 | [用 Tripo 制作 Unity 僵尸游戏](#case-471) | Demo |
| 472 | [用 MS Paint 绘制雪中街景](#case-472) | Demo |
| 473 | [Wojak-Bench 中未接上的插头](#case-473) | Limit |
| 474 | [为节奏游戏创作钢琴曲](#case-474) | Evaluation |
| 475 | [重新设计 Picnic 的代币找回流程](#case-475) | Demo |
| 476 | [把生成的片段剪成动画片头](#case-476) | Tutorial |
| 477 | [用三种工具制作角色动画](#case-477) | Demo |
| 478 | [用 Blender 脚本渲染城市预告片](#case-478) | Demo |
| 479 | [用 JavaScript 绘制夜景](#case-479) | Demo |
| 480 | [将 CAD 模型转换为工程图](#case-480) | Demo |
| 481 | [完成 Plotly 数据分析测试的 43 道题](#case-481) | Benchmark |
| 482 | [在网页中复刻 SGI Indy 工作站](#case-482) | Demo |
| 483 | [用 GitHub 议题和 Git 工作树协作](#case-483) | Integration |
| 484 | [用后台执行器核查引用](#case-484) | Integration |
| 485 | [排查往返货运定价模型](#case-485) | Limit |
| 486 | [让 Edge0 推理环境适配 Mac](#case-486) | Integration |
| 487 | [评审高密度电路板布局](#case-487) | Limit |
| 488 | [追查付费墙后的报纸出处](#case-488) | Limit |
| 489 | [用 Fable 规划并评审 Opus 的改动](#case-489) | Tutorial |

<a id="fable-5-2-cases"></a>
## 使用案例

<a id="case-330"></a>
### Case 330: [不同推理力度下的 MacBook SVG 绘图](https://playcode.io/blog/macbook-svg-benchmark#compare) (作者 [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**在固定需求下比较绘画质量、token 用量和输出上限。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode 报告称，Fable 5.2 High 使用 76,158 个 token，花费 3.05 美元。Xhigh 和 Max 的流式调用达到 128,000 token 上限时还未产出图像。通过 Batch API 提供更多输出空间后，两者均完成了任务。排名依据发布者的视觉判断。

[相关资料 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [用全家人的画做四人清版动作游戏](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (作者 [Lex](https://notesbylex.com/))

**把草图、现有原型和具体手柄要求交给编程智能体。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex 用 Claude Code 把旧的横版游戏重做为有 12 关、18 个角色的清版动作游戏，图像和音频工具负责提供素材。家庭试玩时四个手柄均能使用。

[相关资料 1](https://aidens-revenge.pages.dev/) · [相关资料 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [相关资料 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [三件电子设备从设计到装配](https://www.anthropic.com/research/claude-electronics-design) (作者 [@Anthropic](https://www.anthropic.com/))

**把电路、外壳和固件作为一个系统检查。**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ 播放视频</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic 和 Diode 报告了三件可工作的设备。Fable 5.2 完成了电路板布线、外壳建模和软件编写，并在制造后指导测试。

[相关资料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [相关资料 2](https://www.youtube.com/watch?v=vdYynH177h0) · [相关资料 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [用 Lean 形式化费马大定理](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (作者 [@Anthropic](https://www.anthropic.com/))

**用证明检查器和中间定理作为检查节点。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Anthropic 报告称，由 1,000 个 Fable 5.2 智能体组成的团队在 30 小时内完成了对现有证明的形式化。在相同团队设置下，Opus 5.5 在 18 小时内完成了 26%。

[相关资料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [相关资料 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [从空文件夹开始构建操作系统](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (作者 [@Anthropic](https://www.anthropic.com/))

**分别检查启动、驱动、存储和安装。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ 播放视频</a>

Anthropic 报告称，Fable 5.2 在八天里协调了 1,000 多个子智能体，构建出能在笔记本电脑上启动的原型操作系统。

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [RoboDojo 双臂操作评测](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (作者 [@Anthropic](https://www.anthropic.com/))

**让不同模型执行同样的模拟操作任务。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ 播放视频</a>

Anthropic 报告称，Fable 5.2 在 RoboDojo 上得分为 64.9%，Fable 5.1 为 27.6%。发布内容包含机器人演示。

[相关资料 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [运动中的喷泉](https://x.com/Angaisb_/status/2119909059277238733) (作者 [@Angaisb_](https://x.com/Angaisb_))

**通过持续的水流运动判断场景的视觉节奏。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

创作者分享了归因于 Fable 5.2 的喷泉场景。

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [用 Higgsfield 做逐帧对齐的口型同步](https://x.com/higgsfield_ai/status/2119909938969580024) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**看片前先在帧级别对齐音画。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ 播放视频</a>

Higgsfield 称在工作流中使用 Fable 5.2 跟踪嘴部，并把音频对齐到各帧。

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [开放世界驾驶游戏原型](https://x.com/ericmaskfr/status/2119910195325481026) (作者 [@ericmaskfr](https://x.com/ericmaskfr))

**用可玩的短片段检验开放世界需求。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了一款受 GTA 启发的游戏原型，称完成这次运行约用了 2 小时 14 分钟。

原始提示词

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [用参考图呈现 1940 年的巴黎](https://x.com/higgsfield_ai/status/2119910344998912507) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**将参考图生成与场景代码编写分开。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ 播放视频</a>

Higgsfield 通过自家的 MCP 提供参考图，并用 Fable 5.2 制作 Three.js 场景。

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable 规划、Opus 渲染的短片](https://x.com/kloss_xyz/status/2119910613828980846) (作者 [@kloss_xyz](https://x.com/kloss_xyz))

**在视频工作流中把规划和制作分开。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ 播放视频</a>

Fable 5.2 撰写需求和计划。Opus 5.5 用 Blender 和 Python 制作了 16 秒的动画，并合成配乐。

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [音乐视频实验](https://x.com/WesRoth/status/2119911161386934330) (作者 [@WesRoth](https://x.com/WesRoth))

**同时检查歌词和生成的画面。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了一段 Fable 5.2 音乐视频，并对歌词作了评论。

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Dario Amodei 的绘画肖像](https://x.com/Mr_Salio/status/2119911922577637543) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**将风格化肖像和旁边的参考图对照。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了归因于 Fable 5.2 的 Dario Amodei 肖像。

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [Medium 推理力度下的 Spud Smash](https://x.com/argofowl/status/2119913148929187960) (作者 [@argofowl](https://x.com/argofowl))

**为游戏原型设定清楚的操作和目标。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了一个马铃薯角色，可以拳打、头撞或烧毁蓝色椅子。

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Fable 与 Opus 的冰之教堂](https://x.com/QQTeng/status/2119913518015435103) (作者 [@QQTeng](https://x.com/QQTeng))

**比较同一场景的生成时间和成本。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ 播放视频</a>

创作者称 Fable 耗时约 1 小时 57 分钟、花费 81.10 美元，Opus 耗时约 3 小时 11 分钟、花费 45.97 美元。

原始提示词

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [用声道仿真演唱](https://x.com/banteg/status/2119914098171199996) (作者 [@banteg](https://x.com/banteg))

**将物理人声模型作为音乐制作的输入。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了一段翻唱，使用了两组 Chimera 声道模拟和声码器混音。

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [伊斯坦布尔主题的三项体素测试](https://x.com/Avenoxai/status/2119914308603953485) (作者 [@Avenoxai](https://x.com/Avenoxai))

**比较破坏场景、可运行的时钟和地图。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了三项单提示词测试，按自己的标准分别给出 100、100 和 95.6 分。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Remote Labor Index 的项目完成率](https://x.com/ScaleAILabs/status/2119914701736075489) (作者 [@ScaleAILabs](https://x.com/ScaleAILabs))

**将比例解读为针对特定项目的评估结果。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ 播放视频</a>

Scale Labs 和 CAIS 报告称，Fable 5.2 成功完成了被评估的远程工作项目中的 41.3%。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [四种推理力度下的冰山场景](https://x.com/0xRhinoX/status/2119915121698840587) (作者 [@0xRhinoX](https://x.com/0xRhinoX))

**随着推理力度提高，比较任务完成情况、成本和细节。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ 播放视频</a>

创作者在四种推理力度下使用同一提示词。High 漏了极光，Ultra 加入了发光冰块和水下视角。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [七十九秒动画短片](https://x.com/anstapnever/status/2119915123070644263) (作者 [@anstapnever](https://x.com/anstapnever))

**观察较长动画中的场景连续性。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了一段 79 秒的动画片段，归因于 Fable 5.2 工作流。

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Fable 和 Opus 的机械总成对照](https://x.com/ivanainai/status/2119915243321397550) (作者 [@ivanainai](https://x.com/ivanainai))

**比较两款模型如何安排机械总成的零件。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ 播放视频</a>

作者展示了 Fable 5.2 和 Opus 5.5 各自制作、带标签的车轮和齿轮总成爆炸图。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [机械手攀爬螺旋楼梯](https://x.com/Luckyballa/status/2119915557663506720) (作者 [@Luckyballa](https://x.com/Luckyballa))

**用仿真障碍检验非常规移动方式。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了用 Fable 5.2 和 Steel 0.1 测试 Wuji 机械手以手指行走的演示。

[相关资料 1](https://github.com/skild-ai/steel-webgpu/pull/7)

原始提示词

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [在 Blender 中为 Tripo 网格绑定骨骼](https://x.com/0xKense1/status/2119916096098582566) (作者 [@0xKense1](https://x.com/0xKense1))

**对握持、纹理和变形使用量化检查。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ 播放视频</a>

作者比较了用 Tripo 资产制作的两个骨骼绑定成果。Fable 在 36 分钟内制作两段动画，Opus 在约 21 分钟内制作八段。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [把达芬奇手稿做成交互式发明展示](https://x.com/alexalbert__/status/2119916954337349737) (作者 [@alexalbert__](https://x.com/alexalbert__))

**用原始图纸构建交互式教学模型。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ 播放视频</a>

Alex Albert提供了达芬奇手稿的 PDF，并分享了对其中发明的交互式演绎。

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [由 Claude 操控的音乐工作站](https://x.com/The_Alex/status/2119917226769985785) (作者 [@The_Alex](https://x.com/The_Alex))

**让智能体反复使用同一工具处理作曲请求。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ 播放视频</a>

作者分享了 Fable 5.2 制作的数字音频工作站，并称 Opus 后来打开它创作了一首曲子。

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [树莓派 5 产品动画](https://x.com/sparklabhq/status/2119917375080521921) (作者 [@sparklabhq](https://x.com/sparklabhq))

**用产品动画需求检验部件细节。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了 Fable 5.2 制作的树莓派 5 动画。

原始提示词

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [意大利北部场景](https://x.com/Angaisb_/status/2119917807119089926) (作者 [@Angaisb_](https://x.com/Angaisb_))

**观察指定地点的风景与氛围。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了 Fable 5.2 制作的意大利北部场景。

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [由本地工作智能体制作立体书](https://x.com/atomicagent_io/status/2119918110752846094) (作者 [@atomicagent_io](https://x.com/atomicagent_io))

**在同一任务上比较多智能体编排和单模型运行。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ 播放视频</a>

Atomic 称，Fable 协调本地 Qwen 工作者耗时 11 分钟、花费 2.98 美元，而单用 Fable 耗时 21 分钟、花费 15.77 美元。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [重新启用熔岩灯测试](https://x.com/eidzoku/status/2119918134060601690) (作者 [@eidzoku](https://x.com/eidzoku))

**用相同的视觉任务比较多个模型。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ 播放视频</a>

作者重启了一项熔岩灯测试，并分享了生成结果的视觉对照。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [在 Blender 中制作细节丰富的喷气机](https://x.com/higgsfield_ai/status/2119918248955392431) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**在需求里写明部件数量、时长和外观。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ 播放视频</a>

Higgsfield 称使用 Fable 5.2 与自家的 MCP 编写 Blender 脚本，生成了包含 931 个零件和 24,260 枚铆钉的模型。

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [穿越数百个世界的传送门之旅](https://x.com/emollick/status/2119918307457577163) (作者 [@emollick](https://x.com/emollick))

**用传送门串联独立生成的环境。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ 播放视频</a>

Ethan Mollick 称 25,000 个智能体用代码创建了 450 多个世界，并分享了试玩版本和仓库。

[相关资料 1](https://portals-endless-worlds.netlify.app/) · [相关资料 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [用 Three.js 呈现孟买集市的六个镜头](https://x.com/higgsfield_ai/status/2119918834841010320) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**把视觉需求拆成明确时长的镜头。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ 播放视频</a>

Higgsfield 分享了一段用 Three.js 渲染的集市片段，长 21.5 秒，包含六个镜头。

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [用代码构建写实美式餐馆](https://x.com/higgsfield_ai/status/2119918838490010008) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**用纯代码场景检查材质和光照。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ 播放视频</a>

Higgsfield 展示了一个美式餐馆场景，称全程使用代码，未使用 3D 建模应用。

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [在 Blender 中制作机器人模型](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (作者 [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**通过转台视图检查关节和轮廓。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ 播放视频</a>

创作者展示了用 Fable 5.2 配合 Blender 制作的小型机械机器人。

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [为 Convex 制作动态解说片](https://x.com/Rasmic/status/2119919466163093768) (作者 [@Rasmic](https://x.com/Rasmic))

**用短动画介绍面向开发者的产品。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了 Fable 5.2 制作的 Convex 动态解说片。

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [一次生成的落地页合集](https://x.com/daradoescode/status/2119919529807466594) (作者 [@daradoescode](https://x.com/daradoescode))

**比较多个简短需求对应的布局和信息层级。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了一段视频，展示了 Fable 5.2 生成的多款落地页。

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [用 LilyPond 为钢琴奏鸣曲记谱](https://x.com/imjustnewatai/status/2119919644836347926) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**让乐谱源文件和渲染视频保持对应。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ 播放视频</a>

作者要求创作一个贝多芬风格的乐章，并称展示的音符来自 LilyPond 源文件。

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [自由发挥的视频需求](https://x.com/aollivier82/status/2119920990893244510) (作者 [@aollivier82](https://x.com/aollivier82))

**用不设视觉限制的需求观察模型默认选择。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ 播放视频</a>

创作者要求 Fable 5.2 尽可能制作最美的视频，并分享了输出。

原始提示词

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable 规划、DeepSeek 实现、Opus 审查](https://x.com/ivanfioravanti/status/2119921810267636201) (作者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**让不同智能体负责协调、实现和审查。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ 播放视频</a>

作者展示了 Fable 用 herdr 协调四个 DeepSeek V4.1 Flash 工作智能体，由 Opus 5.5 审查 PR。

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [Fable 5.2 接入 AI Village](https://x.com/aidigest_/status/2119923190411719158) (作者 [@aidigest_](https://x.com/aidigest_))

**分别检查智能体的实际回复和记忆操作。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

AI Village 公开记录显示，Fable 同意稍后应另一智能体的请求更新记忆。相关帖子还展示了 Fable 完成角色匹配问卷。

[相关资料 1](https://x.com/aidigest_/status/2119923209311260707) · [相关资料 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [有无 Skills 的前端设计对照](https://x.com/AdamHoltererer/status/2119924849321914653) (作者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**固定模型，仅改变 Skills 配置。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

创作者展示了 Fable 5.2 在启用和未启用 Skills 时分别生成的前端。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [查找代码库中的隐式状态机](https://x.com/kunchenguid/status/2119924895060795492) (作者 [@kunchenguid](https://x.com/kunchenguid))

**审查具体模块，并要求提供修改前后的示意图。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

作者展示了 Firstmate 仓库的一次代码清理，并公布了原始审查提示词。

[相关资料 1](https://github.com/kunchenguid/lavish-axi)

原始提示词

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [八小时从零做出一款游戏](https://x.com/felixrieseberg/status/2119925633564463609) (作者 [@felixrieseberg](https://x.com/felixrieseberg))

**记录缓存输入、生成的资产和实际耗时。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ 播放视频</a>

这位 Anthropic 工程师称一次运行就创建了模型、音效和纹理，按 API 计价约 550 美元。

[相关资料 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [相关资料 2](https://x.com/AndrewCurran_/status/2119953960794780133)

原始提示词

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Fishslop 原型与 token 成本](https://x.com/theo/status/2119926277801144695) (作者 [@theo](https://x.com/theo))

**把游戏成品与此前的模型输出比较。**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ 播放视频</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

创作者称耗时 76 分钟，token 成本约 42 美元，并将结果与 Opus 5.5 比较。

[相关资料 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [实机演示美式橄榄球游戏](https://x.com/WesRoth/status/2119926801514529027) (作者 [@WesRoth](https://x.com/WesRoth))

**在体育原型中测试反馈和得分提示。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了 Fable 5.2 的实机画面，展示了美式橄榄球得分提示。

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [用 Higgsfield MCP 制作开放世界首领战](https://x.com/higgsfield_ai/status/2119926932343324795) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**区分可玩的游戏部分和过场动画。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ 播放视频</a>

Higgsfield 称用 Fable 5.2 与自家的 MCP 制作了一款浏览器游戏，包括开放世界、三幕首领战和过场动画。

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [潮汐变化中的圣米歇尔山](https://x.com/loktar00/status/2119927152489472076) (作者 [@loktar00](https://x.com/loktar00))

**在微缩历史场景里测试水位变化。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了带潮汐动画的微缩圣米歇尔山。

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [在 Blender 中查看 Roblox 资产](https://x.com/hiyouwhatsapp/status/2119927163264573642) (作者 [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**导入前先在 Blender 中检查资产。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了面向 Roblox 开发、接近一次提示完成的 Blender 成果。

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [不输出思维链的推理评测](https://x.com/Tim_Hua_/status/2119927284761293089) (作者 [@Tim_Hua_](https://x.com/Tim_Hua_))

**在同样的推理输出限制下比较答案。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

评测者执行了不输出思维链的推理与知识测试，称 Fable 5.2 略低于 GPT-6.1 Sol。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [四款模型重制 Chrome 恐龙游戏](https://x.com/noclipepe/status/2119927838321328577) (作者 [@noclipepe](https://x.com/noclipepe))

**用同一个游戏需求比较任务耗时和成本。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ 播放视频</a>

创作者在已有的 T-Rex 测试中加入 Fable 5.2，并并排展示它与 Opus、Gemini 和 Astra 的结果。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [用机械臂下西洋跳棋](https://x.com/karolina_dubiel/status/2119928342115676576) (作者 [@karolina_dubiel](https://x.com/karolina_dubiel))

**读取关节位置，对未抓住的棋子重试。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ 播放视频</a>

创作者称模型修正了约 7 毫米的下垂，并根据反馈重试未成功的动作。

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [十五秒动效短片](https://x.com/aziz4ai/status/2119928581405200726) (作者 [@aziz4ai](https://x.com/aziz4ai))

**记录短篇代码动画测试消耗的额度。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了一段用代码制作的 15 秒片段，称用了每周额度的 4%。

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [可交互游玩的埃菲尔铁塔场景](https://x.com/bobyau/status/2119928812628771212) (作者 [@bobyau](https://x.com/bobyau))

**检验地标模型能否支持交互。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了埃菲尔铁塔演示，称构建耗时 25 分钟。

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [用 Three.js 和 Higgsfield 制作海上竞速](https://x.com/higgsfield_ai/status/2119928918035910668) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**在混合制作流程中区分游戏逻辑和媒体工具。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ 播放视频</a>

Higgsfield 展示了一款有大浪、五名 AI 对手和追踪火箭的竞速游戏。

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [WebGL 实时蜂蜜模拟](https://x.com/deedydas/status/2119930300990177509) (作者 [@deedydas](https://x.com/deedydas))

**用浏览器内的物理模拟测试材质运动。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ 播放视频</a>

作者分享了实时 WebGL 蜂蜜模拟，并公开了原始简短需求。

原始提示词

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [给实拍视频添加程序化特效](https://x.com/ashebytes/status/2119930763105931649) (作者 [@ashebytes](https://x.com/ashebytes))

**检查特效在原视频中的时机和位置。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了 Fable 5.2 特效测试，将动画图形合成到实拍画面上。

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [GTA 通缉等级的动态解说](https://x.com/saimagnate/status/2119931563760632311) (作者 [@saimagnate](https://x.com/saimagnate))

**用游戏画面配合图示解释游戏机制。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ 播放视频</a>

作者称这是 Fable 5.2 一次生成的结果。短片用游戏画面和图示对比了 GTA V 与 RDR2 的通缉机制。

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [用代码搭建风格化 MMO 世界](https://x.com/Izkimar/status/2119931740940640542) (作者 [@Izkimar](https://x.com/Izkimar))

**通过风格化资产判断整个世界的视觉一致性。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ 播放视频</a>

创作者称在一天内构建了演示中的 MMO 世界，资产均由代码生成。

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [Fable 和 Opus 的 3D 场景对照](https://x.com/dom_scholz/status/2119933150025363661) (作者 [@dom_scholz](https://x.com/dom_scholz))

**并排比较准备耗时和输出细节。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ 播放视频</a>

作者分享了 Fable 5.2 和 Opus 5.5 的两段渲染，称 Fable 运行更快。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [游戏暂停界面的冗余文案](https://x.com/AndrewPrifer/status/2119934600608915465) (作者 [@AndrewPrifer](https://x.com/AndrewPrifer))

**检查生成的界面文案是否重复解释。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

开发者以暂停界面为例，指出 Fable 5.2 写了超出需要的说明文字。

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [在 Krea 运行框架中制作情绪板](https://x.com/lambdacalcc/status/2119934725662060663) (作者 [@lambdacalcc](https://x.com/lambdacalcc))

**选定视觉方向前先比较几组概念。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

创作者分享了使用 Fable 5.2 配合 Krea 运行框架制作的四个情绪板输出。

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [在办公室试玩传送门射击游戏](https://x.com/_sholtodouglas/status/2119935331499925557) (作者 [@_sholtodouglas](https://x.com/_sholtodouglas))

**通过多人试玩评估生成的游戏。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ 播放视频</a>

一位 Anthropic 工程师分享了带传送门的第一人称竞技场射击游戏，并介绍了办公室试玩。

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Blender 硬表面资产细节](https://x.com/ziwenxu_/status/2119937420280168929) (作者 [@ziwenxu_](https://x.com/ziwenxu_))

**在 Blender 视口检查拓扑和轮廓。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了作为 Fable 5.2 Blender 成果展示的硬表面资产。

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [不同推理力度的并行前端测试](https://x.com/AI_masaou/status/2119937635322085640) (作者 [@AI_masaou](https://x.com/AI_masaou))

**在多个推理力度下比较简单和复杂需求。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

作者称 Fable 与 Opus 在简单任务中的成果相近，Fable 在规模更大的构建中细节更丰富，从 Medium 提升到 High 时耗时和 token 用量明显增加。

[相关资料 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [十条提示词做出一款小游戏](https://x.com/AmirMushich/status/2119937977426338283) (作者 [@AmirMushich](https://x.com/AmirMushich))

**记录游戏原型的迭代次数和产物大小。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ 播放视频</a>

创作者称游戏大小为 220 KB，约有 3,400 行代码，并分享了代码和视频。

[相关资料 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [用 JavaScript 逐帧绘制动画](https://x.com/kevin_t_ngo/status/2119938129079808282) (作者 [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**检查由程序逐帧绘制的序列。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ 播放视频</a>

作者分享了动画，称每一帧都由 JavaScript 绘制。

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [根据参考视频制作 3D 动画](https://x.com/KHvostikk/status/2119939061049889130) (作者 [@KHvostikk](https://x.com/KHvostikk))

**判断重建场景时与原始视频对照。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了 Fable 5.2 将视频转成 3D 动画的演示。

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Fable 和 Opus 的像素篝火对照](https://x.com/GrilliotTodd/status/2119939651385655692) (作者 [@GrilliotTodd](https://x.com/GrilliotTodd))

**比较同一像素画题材中的光照和轮廓。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ 播放视频</a>

并排结果展示了 Fable 5.2 和 Opus 5.5 对同一篝火题材的绘制。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [Arena WebDev 的 xHigh 评测](https://x.com/arena/status/2119941204003770690) (作者 [@arena](https://x.com/arena))

**比较榜单结果时核对所用推理力度。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena 报告，Claude Fable 5.2 xHigh 首次登上 Code Arena WebDev 时获得 1,832 分。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [两款模型制作的电影预告片字幕](https://x.com/muku_sns/status/2119941490969624679) (作者 [@muku_sns](https://x.com/muku_sns))

**比较对同一段文字的两种演绎。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ 播放视频</a>

作者并排展示了 Opus 和 Fable 设计的预告片字幕。Fable 版本加入了红色边框元素和涂黑遮盖的文字。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [单提示词动效与 3D 作品测试](https://x.com/Khazix0918/status/2119941585538572390) (作者 [@Khazix0918](https://x.com/Khazix0918))

**在创作需求中分别考察调研、设计和渲染。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ 播放视频</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ 播放视频</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ 播放视频</a></td></tr></table>

作者分享了四次运行，分别制作 ChatGPT 周年短片、DeepSeek 解说、Three.js 场景和 Apple 静安的 3D 复刻。

[相关资料 1](https://x.com/Khazix0918/article/2119941585538572390)

原始提示词

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [可交互拆解的核反应堆解说](https://x.com/konstantinsaifo/status/2119941967136379334) (作者 [@konstantinsaifo](https://x.com/konstantinsaifo))

**通过拆解交互展示各零件如何组合。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ 播放视频</a>

创作者要求制作可拆解的 Three.js 反应堆模型，称 API 花费为 92 美元。

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Blood on the Clocktower 智能体测试](https://x.com/dwarkesh_sp/status/2119942657812451482) (作者 [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**让多个模型参与同一款隐藏身份游戏。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

评测者称，这项基准中 Fable 5.2 高于 Fable 5.1 和 Opus 5.5，GPT-6 Astra 则领先。

[相关资料 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [飞梭竞速原型](https://x.com/loktar00/status/2119943124965638444) (作者 [@loktar00](https://x.com/loktar00))

**用熟悉的竞速形式判断运动表现和操控。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了 Fable 5.2 生成的飞梭竞速风格作品。

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [十秒 Claude 内裤广告](https://x.com/Masimo_Blue/status/2119943368612487285) (作者 [@Masimo_Blue](https://x.com/Masimo_Blue))

**用宽泛的产品需求测试原创配乐的广告制作。**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ 播放视频</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

创作者分享了一段十秒宣传视频，其中使用了 Acid Techno 音乐和提供的产品图像。

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [一笔一笔绘制日出中的鸟](https://x.com/mgrczyk/status/2119943813028548721) (作者 [@mgrczyk](https://x.com/mgrczyk))

**禁用撤销，观察逐笔绘画的决策。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ 播放视频</a>

创作者展示了一幅逐笔绘制的日出鸟景，运行框架禁止修改已经落下的笔画。

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [在 Devin 中运行高负荷图形任务](https://x.com/Da7_Tech/status/2119944847255896490) (作者 [@Da7_Tech](https://x.com/Da7_Tech))

**测试复杂渲染时记录耗时和花费。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ 播放视频</a>

一位公开身份的 Cognition 推广大使分享了 Devin Max 的运行结果，称耗时约 3.5 小时、花费约 82 美元。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [三个模型的代码绘画对照](https://x.com/kickingkeys/status/2119945841997672698) (作者 [@kickingkeys](https://x.com/kickingkeys))

**比较绘画动作和合成音效。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了一段带声音的代码绘画，并介绍了对 Fable 5.2、Fable 5.1 和 Gemini 4 Argon 使用相同提示词的测试。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [动画演绎书写史](https://x.com/rileybrown/status/2119946022767980985) (作者 [@rileybrown](https://x.com/rileybrown))

**用时间线组织代码生成的解说片。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ 播放视频</a>

创作者展示了书写史动画，称只用了一条提示词。

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [游戏机械装置试验场](https://x.com/techartist_/status/2119946891106394518) (作者 [@techartist_](https://x.com/techartist_))

**在同一场景中测试玩法机制、物理和特效。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ 播放视频</a>

创作者用 Three.js 和 Blender 搭建了可试验四个概念的场地。

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [手持 Linux 游戏机的 PCB 设计](https://x.com/seveibar/status/2119947341230907453) (作者 [@seveibar](https://x.com/seveibar))

**在相同电路需求下比较两款模型的设计。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ 播放视频</a>

tscircuit 创作者展示了使用 Astra 6 High 和 Fable 5.2 High 设计手持 Linux 游戏设备的测试。

原始提示词

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [体素湖泊场景](https://x.com/Angaisb_/status/2119947748690841841) (作者 [@Angaisb_](https://x.com/Angaisb_))

**用小型环境需求测试构图。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了归因于 Fable 5.2 的体素湖泊。

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [Arena 的 17 个交互生成作品](https://x.com/arena/status/2119948067449536733) (作者 [@arena](https://x.com/arena))

**选定评测任务前先浏览多种输出。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ 播放视频</a>

Arena 分享了 17 个生成作品，涵盖 3D 世界、游戏、界面、数据可视化和代码动画。

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [和友善的龙一起飞行](https://x.com/chetanankola/status/2119951015407738913) (作者 [@chetanankola](https://x.com/chetanankola))

**用一段循环飞行测试镜头和运动。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了以 Three.js 和 Blender 制作的龙场景，并描述了用 Fable 5.2 改进的部分。

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Fable 和 Opus 的果冻虎鲸对照](https://x.com/vib3coded/status/2119951060752375827) (作者 [@vib3coded](https://x.com/vib3coded))

**比较同一主体的表面质感和运动。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ 播放视频</a>

创作者并排展示了 Fable 5.2 和 Opus 5.5 的果冻虎鲸效果。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [开放式视频质量测试](https://x.com/suna_gaku/status/2119952985933697063) (作者 [@suna_gaku](https://x.com/suna_gaku))

**给出宽泛的创作需求，观察模型如何取舍。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ 播放视频</a>

创作者让模型展示其最拿手的视频作品，并分享了结果。

原始提示词

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [地中海主题太空居住站](https://x.com/MaxXWilliamson/status/2119953172634677533) (作者 [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**将简短设计需求与现有项目工具结合。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ 播放视频</a>

创作者提供了以往制作太空居住站时用过的工具，要求制作一座地中海主题空间站。

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [AA-3D 交互体验基准](https://x.com/ArtificialAnlys/status/2119953570430881946) (作者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**结合不确定区间解读 Elo。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ 播放视频</a>

Artificial Analysis 报告，Fable 5.2 Max 在其交互式 3D 基准中发布时的 Elo 为 1,271。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [带倒计时的骷髅角色游戏](https://x.com/WesRoth/status/2119953913160093817) (作者 [@WesRoth](https://x.com/WesRoth))

**给可玩原型加上可见的计时器。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ 播放视频</a>

创作者展示了 Fable 5.2 一次生成的结果，画面有骷髅角色和倒计时。

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Fable 与 Astra 的像素画对照](https://x.com/Angaisb_/status/2119955179915137294) (作者 [@Angaisb_](https://x.com/Angaisb_))

**在同一输出尺寸下比较形状和细节。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ 播放视频</a>

原帖展示了 GPT-6 Astra 与 Fable 5.2 的像素画作品。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [动态设计作品集短片](https://x.com/Leviwoyun/status/2119955625820258308) (作者 [@Leviwoyun](https://x.com/Leviwoyun))

**给出开放式作品集需求，同时限定时长。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ 播放视频</a>

作者分享了一段带配乐的动效作品集短片，称制作耗时 24 分钟。

原始提示词

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [两个模型渲染玻璃泳池](https://x.com/MrTacticalX/status/2119955647542542439) (作者 [@MrTacticalX](https://x.com/MrTacticalX))

**结合耗时与成本比较光照效果。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ 播放视频</a>

创作者称，这次渲染测试中 Fable 耗时 90 分钟、花费 57.87 美元，Opus 耗时 68 分钟、花费 14.39 美元。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [TS-Bench 工具调用准确率](https://x.com/gosrum/status/2119956559031927079) (作者 [@gosrum](https://x.com/gosrum))

**分别记录工具调用错误和 token 用量。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

测试者称 Fable 5.2 没有工具调用错误，并指出较简单的任务难以区分 Claude 各型号。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [微缩马丘比丘](https://x.com/loktar00/status/2119958719362666708) (作者 [@loktar00](https://x.com/loktar00))

**观察微缩场景的氛围和细节。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ 播放视频</a>

分享的马丘比丘演示包含体积雾和小羊驼。

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [按专业任务分类的 GDPx 结果](https://x.com/SemiAnalysis_/status/2119961447199289640) (作者 [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**查看总分的同时比较子任务结果。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

评测发布方报告总分为 16.4%，并列出芯片设计、软件工程等领域的细分结果。

[相关资料 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [相关资料 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [相关资料 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [在绘图应用里画肖像](https://x.com/The_Alex/status/2119964472559489229) (作者 [@The_Alex](https://x.com/The_Alex))

**用参考缩略图辅助绘制肖像。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ 播放视频</a>

作者让 Fable 5.2 打开绘图应用为自己画肖像。视频展示了从轮廓到成稿的过程。

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [Low 推理力度下的 VulcanBench Frontier v4](https://x.com/morganlinton/status/2119966067527467215) (作者 [@morganlinton](https://x.com/morganlinton))

**在相同推理力度下比较不同代模型。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

评测作者称，在 Low 推理力度下，Fable 5.2 和 5.1 每项任务分别约耗时 5 分钟和 26 分钟。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [可玩的后室角色反转游戏](https://x.com/LexnLin/status/2119966127149429093) (作者 [@LexnLin](https://x.com/LexnLin))

**改变玩家目标来检验游戏创意。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ 播放视频</a>

玩家操控怪物抓人。创作者分享了实机片段和试玩链接。

[相关资料 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [在 Blender 中制作 Bugatti Tourbillon](https://x.com/xikhar/status/2119966147328299284) (作者 [@xikhar](https://x.com/xikhar))

**用参考图说明外观和内饰细节。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ 播放视频</a>

创作者称使用提示词和参考图完成了 Bugatti Tourbillon 的建模，包括内饰，并渲染了电影式片段。

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [用两个模型制作电脑主题视频](https://x.com/daradoescode/status/2119966154391183522) (作者 [@daradoescode](https://x.com/daradoescode))

**记录每个模型在混合工作流中的贡献。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了使用 Fable 5.2 制作的风格化视频，其中 Opus 5.5 也承担了大量工作。

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [关于 Megakernel 的音乐视频](https://x.com/elliotarledge/status/2119968762069934415) (作者 [@elliotarledge](https://x.com/elliotarledge))

**用技术概念作为视频主题。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ 播放视频</a>

创作者以 High 推理力度让 Fable 5.2 制作 Megakernel 主题的音乐视频，并分享了片段。

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [根据参考照片制作工作室导览](https://x.com/rpnickson/status/2119969928304357507) (作者 [@rpnickson](https://x.com/rpnickson))

**用真实照片辅助还原场景。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ 播放视频</a>

创作者提供了工作室的照片，改编了类似的视频需求，并称运行约两小时。

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [用代码制作 1990 年代风格的玩具广告](https://x.com/kevin_t_ngo/status/2119972124211454139) (作者 [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**将动画脚本编写与渲染分开。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ 播放视频</a>

创作者称使用 Python 为复古玩具广告制作动画，再用 Blender 渲染。

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Three.js 第三人称游戏场景](https://x.com/bijanbowen/status/2119972220739187182) (作者 [@bijanbowen](https://x.com/bijanbowen))

**用一段实机游玩检查运动与场景。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

作者分享了直播中的 Three.js 成果，显示第三人称角色在户外环境中移动。

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [基于现有渲染器制作 Bryceball](https://x.com/pleometric/status/2119973274402668852) (作者 [@pleometric](https://x.com/pleometric))

**复用渲染引擎作为游戏的基础。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ 播放视频</a>

创作者将关联帖文中介绍的渲染器改造成了可玩的 Bryceball。

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [用 Fable 二次剪辑视频](https://x.com/rileybrown/status/2119973951027724385) (作者 [@rileybrown](https://x.com/rileybrown))

**把此前的剪辑用作后续作品的素材。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ 播放视频</a>

创作者分享了一段 Fable 5.2 剪辑的视频，内容围绕其此前用该模型剪辑的另一段视频。

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [电影式科学史](https://x.com/DeryaTR_/status/2119974354260013293) (作者 [@DeryaTR_](https://x.com/DeryaTR_))

**用时间线组织 3D 叙事。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ 播放视频</a>

创作者要求呈现一段从早期科学走向想象中未来的电影式旅程，并分享了成片。

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [达芬奇飞行器的 3D 模型](https://x.com/higgsfield_ai/status/2119975721909301684) (作者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**先建模还原历史设计，再测试改动。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ 播放视频</a>

Higgsfield 展示了达芬奇飞行器的 3D 版本，并介绍了物理测试与重新设计的过程。

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [按设计要求完成 PCB 布线](https://x.com/cmonkey/status/2119975852977029365) (作者 [@cmonkey](https://x.com/cmonkey))

**在制作电路板前检查布线。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

作者在讨论电路布局的后续帖中分享了 Fable 5.2 的 PCB 布线结果。

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [在不同运行框架中使用同一提示词](https://x.com/loktar00/status/2119980613369319706) (作者 [@loktar00](https://x.com/loktar00))

**比较模型输出时记录运行框架的差异。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ 播放视频</a>

创作者在不同运行框架中给 DeepSeek 和 Fable 5.2 同一提示词，并展示了两组结果。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [用代码绘制哥斯拉](https://x.com/chetaslua/status/2119981510199808368) (作者 [@chetaslua](https://x.com/chetaslua))

**用近似矢量的形状和动态效果重新演绎图像。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ 播放视频</a>

创作者受一则哥斯拉帖文启发，分享了代码绘制的画面和短动画。

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [面向 3D 打印的手持风扇](https://x.com/davelee/status/2119981787325579398) (作者 [@davelee](https://x.com/davelee))

**用实体原型检查建模后的装配效果。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ 播放视频</a>

创作者与孩子们一起设计了可打印的手持风扇，并在打印前分享了模型。

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [与 Opus 对比排查插件缺陷](https://x.com/oaranda/status/2119982729747919096) (作者 [@oaranda](https://x.com/oaranda))

**用交叉回归测试比较修复结果。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

作者标注的发布公告节选。

两个模型找到了相同的六个插件缺陷。Opus 通过了交叉测试，Fable 有一项未通过，但另外发现了仪表盘的问题。

原始提示词

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [以 3D 场景重建伊斯坦布尔](https://x.com/petergostev/status/2119877733488394520) (作者 [@petergostev](https://x.com/petergostev))

**从远景和近景检查城市规模的场景。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ 播放视频</a>

Peter Gostev 分享了 Fable 5.2 Max 制作的伊斯坦布尔 3D 场景，并附上更详尽的评估。

[相关资料 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [带动态屏幕的 Blender 工作室短片](https://x.com/rileybrown/status/2119902109709537708) (作者 [@rileybrown](https://x.com/rileybrown))

**在同一 3D 场景中制作屏幕内容、灯光和镜头动画。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ 播放视频</a>

创作者称使用了 13 个镜头、笔记本屏幕上播放的定制网页和 ElevenLabs 音频，并用 RunPod GPU 渲染。

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [弱耦合下的黑洞跃迁](https://hexagonmath.org/2611.00175v1) (作者 [@Anthropic](https://www.anthropic.com/))

**回到原始理论设定检查一项未完成的推导。**

Anthropic 报告称，Fable 5.2 完成了一项长期未解的计算，并在弱耦合区间发现突变。预印本给出了推导。

[相关资料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [模自举方法的界限](https://hexagonmath.org/2611.00174v1) (作者 [@Anthropic](https://www.anthropic.com/))

**在提出解析界限时一并公开推导。**

Anthropic 报告称，Fable 5.2 确定了在简化量子引力设定中使用的无自旋模自举方法的精确极限。

[相关资料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Vercel AI Gateway 中按顺序回退模型](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (作者 [Vercel](https://vercel.com/))

**为被分类器拒绝的请求设置网关回退顺序。**

Vercel 的 AI SDK 示例调用 anthropic/claude-fable-5.2，将 Opus 5.5 和 Sonnet 5.5 依次设为回退模型。文档说明了网关的数据保留要求。

[相关资料 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [嵌套子智能体与代码审查预算](https://news.ycombinator.com/item?id=50430925) (作者 [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**跟踪嵌套委派，并在提示词之外设置审查预算上限。**

作者审查 80,000 行代码时要求最多使用四个子智能体，称实际上出现了六个或更多嵌套智能体，不到 20 分钟便耗尽五小时用量额度。

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [将 LCARS 设计转换为 HTML 的对照](https://news.ycombinator.com/item?id=50430962) (作者 [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**将曲线、图标还原度、动画和导航分别设为验收项。**

作者用相同的《星际迷航》风格设计比较 Fable 5.2 和 Opus 5.5。作者更喜欢 Fable 的曲线和部分图标，也更喜欢 Opus 的动画，认为 Fable 的 SVG 闪烁影响体验。要求仅制作第一页。

[相关资料 1](https://html.non.io/lcars-fable-5.2/) · [相关资料 2](https://html.non.io/lcars-opus-5.5/) · [相关资料 3](https://news.ycombinator.com/item?id=50431231) · [相关资料 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [Quantum ESPRESSO 的 GPU 优化](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (作者 [Discovered Materials](https://discoveredmaterials.com/))

**优化科学软件时要求提供参考结果和有代表性的隐藏测试。**

Discovered Materials 报告称，同一 GPU 上的 13 项声子基准测试的加速比几何平均值为 36 倍，混合泛函计算约为 9 倍。公开的补丁以正确性和性能测试为依据。

[相关资料 1](https://github.com/discovered-materials/dm_qe) · [相关资料 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [按推理力度查看 Artificial Analysis 智能指数](https://artificialanalysis.ai/models/claude-fable-5-2) (作者 [Artificial Analysis](https://artificialanalysis.ai/))

**在所选推理力度下同时查看得分、任务成本与延迟。**

引用的 Max 默认回退快照显示指数为 65，单项任务成本 26.54 美元，耗时 46.4 分钟。这些数字对应评测任务。

[相关资料 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [High 推理力度下变更审查的误报](https://news.ycombinator.com/item?id=50431810) (作者 [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**采取行动前，先对照代码核实模型的审查结论。**

开发者称 Fable 5.2 High 在审查变更时标出了两个不存在的问题，开发者凭对代码的了解识别了误报。

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [三十项常规编程任务](https://news.ycombinator.com/item?id=50432483) (作者 [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**用同一批编程任务比较耗时和完成数。**

作者称 Fable 5.2 和 Opus 5.5 均完成了 30 项中的 26 项，Fable 5.1 完成 25 项。Fable 5.2 的耗时为 5.1 的 0.62 倍，作者未报告安全机制导致的中断。

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [荒岛求生屏保](https://news.ycombinator.com/item?id=50432836) (作者 [@nzach](https://news.ycombinator.com/user?id=nzach))

**直接打开可玩的页面检查模型制作的屏保。**

Show HN 作者链接了名为 Stranded with Claude 的浏览器荒岛场景，作品以可交互的画布呈现。

[相关资料 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [High 推理力度下的三项浏览器游戏测试](https://senko.net/vibecode-bench/) (作者 [Senko Rašić](https://senko.net/))

**在游戏评测中分开衡量玩法和画面还原度。**

Senko Rašić 在 Claude Code 中用 Fable 5.2 测试了即时战略、体素和飞行模拟需求。作者称它做出了飞艇等可探索全地图的机制，但认为部分画面表现较差。

[相关资料 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [逐章生成书评播客脚本](https://news.ycombinator.com/item?id=50434156) (作者 [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**对同样的播客任务比较脚本篇幅。**

作者逐章生成两位书评人之间的对话，称 Fable 版本约 2.5 页，Opus 5.5 版本约 4.5 页，并附上两组示例。

[相关资料 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [相关资料 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [用 Rust 迁移生产服务](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (作者 [@Anthropic](https://www.anthropic.com/))

**对比迁移前后的启动表现。**

Anthropic 报告称，运行预发布版 Fable 5.2 的智能体用 Rust 重写了一项 Python 生产服务，将启动耗时缩短到原来的约 1/26。

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [在 GitHub Copilot 中选择 Fable 5.2](https://x.com/github/status/2119926269982961833) (作者 [@github](https://x.com/github))

**先启用组织策略，再选择模型。**

GitHub 文档说明了 Copilot 客户端的模型选择器，以及 Business 和 Enterprise 账户所需的管理员设置。

[相关资料 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [百页 HTML 设计挑战](https://x.com/MiaAI_lab/status/2119930229661503893) (作者 [@MiaAI_lab](https://x.com/MiaAI_lab))

**除了视觉质量，也要统计完成且能运行的文件。**

作者要求制作 100 个不同设计，发布了 76 个文件及提示词，并称用完了 Fable 使用额度。

[相关资料 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [相关资料 2](https://mia-ai.net/lab/experiments/100-htmls) · [相关资料 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [相关资料 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [相关资料 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [相关资料 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [相关资料 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [相关资料 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [相关资料 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [相关资料 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [相关资料 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [相关资料 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [相关资料 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [相关资料 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [编译器任务中的需求偏移](https://x.com/sameQCU/status/2119939304864800971) (作者 [@sameQCU](https://x.com/sameQCU))

**把智能体复述的需求与输入逐项对照。**

开发者描述了一个编译器任务，其中 Fable 5.2 和较早的 Opus 模型都错误复述了收到的要求。

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [用 Opus 跟踪长时间运行的 Fable 任务](https://x.com/marouane53/status/2119950129767858262) (作者 [@marouane53](https://x.com/marouane53))

**用单独会话跟踪长任务的进展。**

作者称，Fable 的一些任务运行超过两小时，进度更新很少。他在另一个会话里用 Opus 5.5 解读任务进展和决策。

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [用全新视角复查代码](https://x.com/doodlestein/status/2119958895158292786) (作者 [@doodlestein](https://x.com/doodlestein))

**单独复查新增和改动过的文件。**

创作者分享了两条原始后续提示词，用于在实现完成后查找并修正问题。

原始提示词

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

原始提示词

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [功能设计审查中的偏移](https://news.ycombinator.com/item?id=50434214) (作者 [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**用现有设计作为清单检查智能体的后续建议。**

作者在功能设计审查中比较模型，更喜欢 Opus 5.5。后续 Fable 5.2 的诊断提出了一项设计中已存在的建议。

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [DX Ball 风格打砖块游戏对比](https://news.ycombinator.com/item?id=50434424) (作者 [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**在复刻需求中分别比较游戏机制和手感。**

作者链接了 Fable 5.2 与 Opus 5.5 的独立运行版本。Fable 改动了原作部分机制，作者更喜欢 Opus 版本的手感。

[相关资料 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [相关资料 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [改进 3D 应用的试验](https://news.ycombinator.com/item?id=50434433) (作者 [@user43928](https://news.ycombinator.com/user?id=user43928))

**在相同的改进任务中比较可见变化和预算消耗。**

作者称让 Fable 5.2 改进一款非游戏 3D 应用，结果与 Opus 5.5 差异不大，并在当晚用掉 Fable 套餐额度的 25%。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [三个模型制作猫鼠游戏](https://news.ycombinator.com/item?id=50434508) (作者 [@simonw](https://news.ycombinator.com/user?id=simonw))

**固定游戏提示词，检查每个模型的可玩成果。**

Simon Willison 分享了 Fable 5.2 Extra、Opus 5.5 Extra 和 GPT-6 Extra High 制作的移动端友好 Three.js 游戏，称 Fable 版本耗时约 40 分钟。

[相关资料 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [相关资料 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [相关资料 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

原始提示词

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [AIBenchy 的 High 推理力度成本与得分](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (作者 [AIBenchy](https://aibenchy.com/))

**在相同力度标签下比较得分、总成本与响应时间。**

AIBenchy 公布的结果显示，Fable 5.2 High 和 Opus 5.5 High 的得分分别为 8.7 和 9.4，总成本为 5.083 和 2.133 美元，平均响应时间为 14.73 和 27.55 秒。

[相关资料 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [调整 Fable 5.2 的 Agent 运行配置](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (作者 [@Anthropic](https://www.anthropic.com/))

**重新测试推理强度，并为长任务设定进度更新规则。**

Anthropic 的指南提供示例指令，涵盖推理强度、完成标准、审批、进度更新和子智能体限制。

[相关资料 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="case-469"></a>
### Case 469: [动态角色预览应用](https://x.com/seiiiiiiiiiiru/status/2121390458572333253) (作者 [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**让 Fable 把重复的素材检查做成可操作的界面。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/ce514e99465c257220ee9bf7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/776670eda35fbabbf1c63663.jpg" alt="Case 469 · 1" width="760"><br>▶ 播放视频</a>

创作者称，他们请 Fable 5.2 担任顾问，模型把原先效率较低的流程做成了应用。录屏展示了 3D 角色的动作预设、背景设置，以及 GLB 和透明 PNG 的导出选项。

Type: Demo | Date: 2026-11-13

---

<a id="case-470"></a>
### Case 470: [测试无工具生成的二维码](https://x.com/AdamHoltererer/status/2121376853474578625) (作者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**解码生成的二维码，再判断测试是否成功。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d3833f006038158569c9816d.png" alt="Case 470 · 1" width="760">

Adam Holter 将这项二维码演示归功于 Fable 5.2、Astra 和 Sol，并称生成时未使用工具。我们在本地扫描附件，确认二维码编码的文字是 MADE WITHOUT TOOLS。

Type: Evaluation | Date: 2026-11-13

---

<a id="case-471"></a>
### Case 471: [用 Tripo 制作 Unity 僵尸游戏](https://x.com/fe_yukichi/status/2121375714192814554) (作者 [@fe_yukichi](https://x.com/fe_yukichi))

**通过统一的素材制作流程打造一组可玩角色。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/055f505803b769bb8b24a54e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0fa0715e64f91ab69725599e.jpg" alt="Case 471 · 1" width="760"><br>▶ 播放视频</a>

创作者披露了与 Tripo 的合作，并称使用 Tripo Agentic Canvas 为一款借助 Fable 5.2 制作的 Unity 游戏生成了 8 名玩家角色和 16 种僵尸。视频展示了角色选择和游戏过程，作者还提供了桌面浏览器版。

[相关资料 1](https://tsukiyo-zombie.pages.dev/)

Type: Demo | Date: 2026-11-13

---

<a id="case-472"></a>
### Case 472: [用 MS Paint 绘制雪中街景](https://www.reddit.com/r/ClaudeAI/comments/1xvghd1/fable_52_painting_in_ms_paint/) (作者 [u/wollymonjac](https://www.reddit.com/user/wollymonjac/))

**用录屏评估模型长时间直接操控鼠标的表现。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/10ad84001f4c682c5343846c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e7af823e10ef2135adec2154.jpg" alt="Case 472 · 1" width="760"><br>▶ 播放视频</a>

Reddit 创作者称，Fable 5.2 用鼠标在 MS Paint 中画出了一幅雪中街景，用时约两个半小时。附带的 X 转发帖提供了同一场景的录屏。

[相关资料 1](https://x.com/i/status/2121373793599869213)

Type: Demo | Date: 2026-11-13

---

<a id="case-473"></a>
### Case 473: [Wojak-Bench 中未接上的插头](https://x.com/lukaspet/status/2121371593943466167) (作者 [@lukaspet](https://x.com/lukaspet))

**逐一对照参考图，检查生成的 3D 装配中各连接处是否正确。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e509db79b2e79fcc2d6beda1.jpg" alt="Case 473 · 1" width="760">

作者称，Fable 5.2 在这项 Wojak-Bench 任务中没有把电线接到插座上。原帖配图将 3D 成品照片和参考图并列展示。

Type: Limit | Date: 2026-11-13

---

<a id="case-474"></a>
### Case 474: [为节奏游戏创作钢琴曲](https://x.com/DJ_HYSNS/status/2121367353237942287) (作者 [@DJ_HYSNS](https://x.com/DJ_HYSNS))

**让模型作曲时，检查作品能否演奏，以及模型能否控制制作环节。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d016f48687e0c8e6cf810812.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/9faa77e2e9ba2ec99be995a7.jpg" alt="Case 474 · 1" width="760"><br>▶ 播放视频</a>

作者先让模型创作节奏游戏配乐，随后称模型在选择 VST 音色和混音时遇到困难，便改做钢琴独奏。视频展示了生成的钢琴卷帘。作者认为，曲子的难度超出了其要求的人类可演奏范围。

Type: Evaluation | Date: 2026-11-13

---

<a id="case-475"></a>
### Case 475: [重新设计 Picnic 的代币找回流程](https://x.com/joaoavf/status/2121366491321057717) (作者 [@joaoavf](https://x.com/joaoavf))

**用界面原型对比找回不受支持的代币时会遇到的不同状态。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/551612796f4150a43b190ee3.jpg" alt="Case 475 · 1" width="760">

作者称，给 Fable 5.2 一两轮提示，就得到了找回 Picnic 不支持的代币的新设计。配图展示了拟议流程中的多个界面。

Type: Demo | Date: 2026-11-13

---

<a id="case-476"></a>
### Case 476: [把生成的片段剪成动画片头](https://x.com/aimikoda/status/2121362621274177726) (作者 [@aimikoda](https://x.com/aimikoda))

**把片段、配乐和明确的踩点剪辑要求交给 Fable。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e3ab28061669d84818042ee0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/cb65344e413d2bd340406d59.jpg" alt="Case 476 · 1" width="760"><br>▶ 播放视频</a>

创作者将 MiniMax H3 生成的素材和 Suno v6 的配乐交给 Fable 5.2 Medium 剪辑。发布的成片包含动态像素风角色和转场，案例附有原始 Fable 剪辑提示词。

原始提示词

```
Using these clips and the song, create a highly polished, professional anime opening / music video (MV) edit, perfectly synchronized with the music's beats and rhythm.
Incorporate dynamic kinetic typography, creative transitions, stylish visual effects, speed ramps, match cuts and impactful beat-synced editing.
Design pixel-art versions of the characters and animate them dancing to the music. Get creative with different visual styles, motion graphics and playful sequences while maintaining a cohesive anime opening aesthetic.
Carefully review all the footage and select only the best moments. Trim and rearrange the clips to match the song's energy, pacing and emotional progression. Avoid any frames with incorrect anatomy, awkward poses, visual glitches or animation errors.
Make the final result feel like a professionally directed, high-budget anime opening with exceptional timing, seamless transitions, strong visual storytelling and meticulous attention to detail.
```

Type: Tutorial | Date: 2026-11-13

---

<a id="case-477"></a>
### Case 477: [用三种工具制作角色动画](https://x.com/ingi_erlingsson/status/2121361947446677797) (作者 [@ingi_erlingsson](https://x.com/ingi_erlingsson))

**对照源 GIF 和经过 Fable 与 ComfyUI 处理后的动画。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/69a3410b7b2dcdb14ee6c5d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/391924750cd0641254cb114f.jpg" alt="Case 477 · 1" width="760"><br>▶ 播放视频</a>

作者将 GPT Image 2.6 生成的 GIF 列为输入，之后依次使用 Fable 5.2 和 ComfyUI。附件视频展示了旋转视角下不断变化的角色头像。

Type: Demo | Date: 2026-11-13

---

<a id="case-478"></a>
### Case 478: [用 Blender 脚本渲染城市预告片](https://x.com/hanghuang_/status/2121361932456427644) (作者 [@hanghuang_](https://x.com/hanghuang_))

**将城市预告片拆成场景、角色、车辆和渲染任务。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0e5170c057eecd328b178fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d10c5d322edba010282a60d0.jpg" alt="Case 478 · 1" width="760"><br>▶ 播放视频</a>

创作者称，Fable 5.2 规划了一部游戏风格的预告片，并为城市、角色和汽车编写了 Blender 代码。创作者表示，最终的 4K 画面使用 7 张租用的 GPU 渲染。发布的视频展示了成片镜头。

Type: Demo | Date: 2026-11-13

---

<a id="case-479"></a>
### Case 479: [用 JavaScript 绘制夜景](https://x.com/kloss_xyz/status/2121356668311384487) (作者 [@kloss_xyz](https://x.com/kloss_xyz))

**评估代码生成的插画时，对比多张完成图。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/6e9d554b17822715f07d3be8.jpg" alt="Case 479 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/f57db49bb8213cc6ca4bcafe.jpg" alt="Case 479 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/2933b30de09501dbbb7e1505.jpg" alt="Case 479 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/490e5952694322b7963be8e2.jpg" alt="Case 479 · 4" width="450"></td></tr></table>

作者称，发布的 4 张插画由 Fable 5.2 用 JavaScript 绘制。附件展示了不同的风格化夜景，可供对照。

Type: Demo | Date: 2026-11-13

---

<a id="case-480"></a>
### Case 480: [将 CAD 模型转换为工程图](https://x.com/MecAgent/status/2121352868490100787) (作者 [@MecAgent](https://x.com/MecAgent))

**对照原始 CAD 模型检查视图、尺寸和标注。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/5ce59334e405a279e1008bf0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/780dc65cb1b04f7a75e27ace.jpg" alt="Case 480 · 1" width="760"><br>▶ 播放视频</a>

MecAgent 的演示展示了带有多视图和标注的工程图纸，并称转换由 Fable 5.2 完成。视频呈现了生成的图纸，尺寸精度仍需对照 CAD 文件检查。

Type: Demo | Date: 2026-11-13

---

<a id="case-481"></a>
### Case 481: [完成 Plotly 数据分析测试的 43 道题](https://plotly.com/blog/gemini-4-hydrogen-plotly-data-analytics-bench/) (作者 [Plotly](https://plotly.com/))

**在同一套分析评测环境中比较准确率与单次运行成本。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/50882a17db12bede9165a92d.webp" alt="Case 481 · 1" width="760">

Plotly 报告称，Fable 5.2 是答对全部 43 道题的 4 个模型之一，其中也完成了全部 5 道隐藏模式题。发布者提醒，每个模型只跑一次属于单次抽样。图表展示了这项评测的成本和准确率。

[相关资料 1](https://news.ycombinator.com/item?id=50485733)

Type: Benchmark | Date: 2026-11-12

---

<a id="case-482"></a>
### Case 482: [在网页中复刻 SGI Indy 工作站](https://news.ycombinator.com/item?id=50476597) (作者 [@gdubs](https://news.ycombinator.com/user?id=gdubs))

**通过交互式复刻探索如何把实体工作站做成网站。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/74b80686867b920881164246.jpg" alt="Case 482 · 1" width="760">

Gregory Wieber 称，他借助 Fable 5.2 将自己的网站改造成 20 世纪 90 年代的 Silicon Graphics Indy。公开演示包含可登录的 3D 工作站、3D 文件系统和 Soft Break 游戏。

[相关资料 1](https://gregorywieber.com/indy/)

Type: Demo | Date: 2026-11-13

---

<a id="case-483"></a>
### Case 483: [用 GitHub 议题和 Git 工作树协作](https://news.ycombinator.com/item?id=50493545) (作者 [@nickalaso](https://news.ycombinator.com/user?id=nickalaso))

**用议题分派任务，用工作树和拉取请求隔离改动。**

作者称，他们用 Fable 5.2 担任总协调器，用 Opus 担任子协调器，通过自定义 MCP 服务器启动来自不同供应商的执行代理。他们用 GitHub 议题跟踪工作，用 Git 工作树和拉取请求避免改动冲突。

Type: Integration | Date: 2026-11-14

---

<a id="case-484"></a>
### Case 484: [用后台执行器核查引用](https://x.com/tukiyomiiori/status/2121368478364192930) (作者 [@tukiyomiiori](https://x.com/tukiyomiiori))

**将引用核查交给执行代理，并观察主会话何时恢复。**

作者称，他们让 Fable 5.2 使用子代理和后台脚本核查引用的论文。他们观察到，后台工作运行时 Claude Code 主会话会暂停，子代理或脚本停止时会唤醒主会话。

Type: Integration | Date: 2026-11-13

---

<a id="case-485"></a>
### Case 485: [排查往返货运定价模型](https://x.com/allTheYud/status/2121360145921998877) (作者 [@allTheYud](https://x.com/allTheYud))

**检查模型是否为返程正确分配了边际成本。**

作者在双向货运仿真中发现，尽管货船必须返航，Fable 5.2 仍将双程燃油计入其中一程，只按边际成本计算另一程。作者称，这类错误需要反复调试。

Type: Limit | Date: 2026-11-13

---

<a id="case-486"></a>
### Case 486: [让 Edge0 推理环境适配 Mac](https://news.ycombinator.com/item?id=50482710) (作者 [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen))

**请模型做平台适配，再在目标设备上测试推理。**

在 Edge0-145B 的讨论中，一位评论者称，他们让 Fable 5.2 提供 Mac 兼容版本，并做了少量调整。据其自述，他们在 M5 Max 上使用 NVFP4 时，推理速度约为每秒 50 个 token。

[相关资料 1](https://news.ycombinator.com/item?id=50475713)

Type: Integration | Date: 2026-11-13

---

<a id="case-487"></a>
### Case 487: [评审高密度电路板布局](https://news.ycombinator.com/item?id=50478759) (作者 [@0_____0](https://news.ycombinator.com/user?id=0_____0))

**按电路板的性能要求检查元件选型和布局。**

一位 Hacker News 评论者尝试用 Fable 5.2 为多块电路板布局和布线。据其自述，一块高密度板的布局初看颇有希望，但要达到要求，仍需大幅调整布局并手动重画大部分原理图。

Type: Limit | Date: 2026-11-13

---

<a id="case-488"></a>
### Case 488: [追查付费墙后的报纸出处](https://news.ycombinator.com/item?id=50478191) (作者 [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff))

**查到原文前，将推测的人物归属视为待核线索。**

一位 Hacker News 评论者通过语言学邮件列表，将一处归属追溯到《达拉斯晨报》1985 年的一篇报道。据其自述，Fable 5.2 无法访问报道全文，只给出了一位可能的记者和报道背景，相关归属仍有待原文核验。

[相关资料 1](https://listserv.linguistlist.org/pipermail/ads-l/2003-September/033575.html)

Type: Limit | Date: 2026-11-13

---

<a id="case-489"></a>
### Case 489: [用 Fable 规划并评审 Opus 的改动](https://news.ycombinator.com/item?id=50477200) (作者 [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology))

**批准书面计划，划分实施任务，再通过 CI 和预发布环境验证改动。**

作者分享了他们据称用于大型代码库的工作流程。Fable 5.2 负责规划，Opus 5.5 子代理负责实现和评审，CI 守住测试覆盖率，人工则按清单在预发布环境中核验。

Type: Tutorial | Date: 2026-11-13

---

<a id="acknowledge"></a>
## 作者致谢

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/), [@fe_yukichi](https://x.com/fe_yukichi), [u/wollymonjac](https://www.reddit.com/user/wollymonjac/), [@lukaspet](https://x.com/lukaspet), [@DJ_HYSNS](https://x.com/DJ_HYSNS), [@joaoavf](https://x.com/joaoavf), [@aimikoda](https://x.com/aimikoda), [@ingi_erlingsson](https://x.com/ingi_erlingsson), [@hanghuang_](https://x.com/hanghuang_), [@MecAgent](https://x.com/MecAgent), [Plotly](https://plotly.com/), [@gdubs](https://news.ycombinator.com/user?id=gdubs), [@nickalaso](https://news.ycombinator.com/user?id=nickalaso), [@tukiyomiiori](https://x.com/tukiyomiiori), [@allTheYud](https://x.com/allTheYud), [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen), [@0_____0](https://news.ycombinator.com/user?id=0_____0), [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff), [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology)
