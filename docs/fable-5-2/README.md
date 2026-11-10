# Claude Fable 5.2 Use Cases

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

Source-linked workflows, demos, comparisons, benchmarks, integrations, and practical limitations from the November 10 collection.

[Anthropic announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [Earlier case collection](../../README.md)

## Case Index

| Case | Use Cases | Type |
| --- | --- | --- |
| 330 | [MacBook SVG Drawing Across Effort Levels](#case-330) | Benchmark |
| 331 | [Four-Player Beat ’Em Up from Family Drawings](#case-331) | Demo |
| 332 | [Three Electronic Devices from Design to Assembly](#case-332) | Demo |
| 333 | [Formalizing Fermat’s Last Theorem in Lean](#case-333) | Evaluation |
| 334 | [An Operating System from an Empty Folder](#case-334) | Demo |
| 335 | [RoboDojo Dual-Arm Manipulation](#case-335) | Benchmark |
| 336 | [A Fountain in Motion](#case-336) | Demo |
| 337 | [Frame-Aligned Lip Sync with Higgsfield](#case-337) | Integration |
| 338 | [An Open-World Driving Prototype](#case-338) | Demo |
| 339 | [Paris in 1940 with Reference Images](#case-339) | Integration |
| 340 | [Fable Plans an Opus-Rendered Short](#case-340) | Integration |
| 341 | [A Music-Video Experiment](#case-341) | Demo |
| 342 | [A Painted Portrait of Dario Amodei](#case-342) | Demo |
| 343 | [Spud Smash at Medium Effort](#case-343) | Demo |
| 344 | [Ice Cathedral across Fable and Opus](#case-344) | Evaluation |
| 345 | [Singing with Simulated Vocal Tracts](#case-345) | Demo |
| 346 | [Three Istanbul Voxel Tests](#case-346) | Evaluation |
| 347 | [Remote Labor Index Project Completion](#case-347) | Benchmark |
| 348 | [Iceberg Scene at Four Effort Levels](#case-348) | Evaluation |
| 349 | [A Seventy-Nine-Second Anime Short](#case-349) | Demo |
| 350 | [Mechanical Assemblies across Fable and Opus](#case-350) | Evaluation |
| 351 | [A Robotic Hand Climbing a Spiral Staircase](#case-351) | Demo |
| 352 | [Rigging a Tripo Mesh in Blender](#case-352) | Evaluation |
| 353 | [Da Vinci Notebook as Interactive Inventions](#case-353) | Demo |
| 354 | [A Music Workstation Controlled by Claude](#case-354) | Demo |
| 355 | [An Animated Raspberry Pi 5](#case-355) | Demo |
| 356 | [A Northern Italian Scene](#case-356) | Demo |
| 357 | [Popup Book with Local Builder Agents](#case-357) | Evaluation |
| 358 | [A Reintroduced Lava-Lamp Test](#case-358) | Evaluation |
| 359 | [A Detailed Jet Built in Blender](#case-359) | Integration |
| 360 | [Portal Journey across Hundreds of Worlds](#case-360) | Demo |
| 361 | [A Six-Shot Bombay Bazaar in Three.js](#case-361) | Integration |
| 362 | [A Photoreal Diner Built in Code](#case-362) | Integration |
| 363 | [A Robot Model in Blender](#case-363) | Demo |
| 364 | [A Motion-Graphics Explainer for Convex](#case-364) | Demo |
| 365 | [A Collection of One-Shot Landing Pages](#case-365) | Demo |
| 366 | [A Piano Sonata Scored in LilyPond](#case-366) | Demo |
| 367 | [A Free-Form Video Brief](#case-367) | Demo |
| 368 | [Fable Plans, DeepSeek Builds, Opus Reviews](#case-368) | Integration |
| 369 | [Fable 5.2 in the AI Village](#case-369) | Integration |
| 370 | [Frontend Design with and without Skills](#case-370) | Evaluation |
| 371 | [Find Implicit State Machines in a Codebase](#case-371) | Tutorial |
| 372 | [A Game Built from Scratch in Eight Hours](#case-372) | Demo |
| 373 | [Fishslop Prototype and Token Cost](#case-373) | Evaluation |
| 374 | [A Football Game in Motion](#case-374) | Demo |
| 375 | [Open-World Boss Fight with Higgsfield MCP](#case-375) | Integration |
| 376 | [Mont Saint-Michel and Changing Tides](#case-376) | Demo |
| 377 | [A Roblox Asset in Blender](#case-377) | Demo |
| 378 | [Reasoning without Chain-of-Thought Output](#case-378) | Benchmark |
| 379 | [Chrome Dino Remakes across Four Models](#case-379) | Evaluation |
| 380 | [Checkers with a Robot Arm](#case-380) | Demo |
| 381 | [A Fifteen-Second Motion Graphics Clip](#case-381) | Demo |
| 382 | [A Playable Eiffel Tower Scene](#case-382) | Demo |
| 383 | [Offshore Racing with Three.js and Higgsfield](#case-383) | Integration |
| 384 | [Real-Time Honey Simulation in WebGL](#case-384) | Demo |
| 385 | [Programmatic Visual Effects for Footage](#case-385) | Demo |
| 386 | [A Motion Explainer for GTA Wanted Levels](#case-386) | Demo |
| 387 | [A Stylized MMO World in Code](#case-387) | Demo |
| 388 | [A 3D Scene across Fable and Opus](#case-388) | Evaluation |
| 389 | [Redundant Text in a Game Pause Screen](#case-389) | Limit |
| 390 | [Moodboards with a Krea Harness](#case-390) | Integration |
| 391 | [Office Playtest of a Portal Shooter](#case-391) | Demo |
| 392 | [A Detailed Blender Hard-Surface Asset](#case-392) | Demo |
| 393 | [Parallel Frontend Tests across Effort Levels](#case-393) | Evaluation |
| 394 | [A Small Game Built in Ten Prompts](#case-394) | Demo |
| 395 | [A JavaScript Frame-by-Frame Animation](#case-395) | Demo |
| 396 | [Video Reference to 3D Animation](#case-396) | Demo |
| 397 | [Pixel Campfire across Fable and Opus](#case-397) | Evaluation |
| 398 | [Arena WebDev at xHigh](#case-398) | Benchmark |
| 399 | [Movie Trailer Typography across Models](#case-399) | Evaluation |
| 400 | [One-Prompt Motion and 3D Portfolio Tests](#case-400) | Evaluation |
| 401 | [An Explorable Nuclear Reactor Explainer](#case-401) | Demo |
| 402 | [Blood on the Clocktower Agents](#case-402) | Benchmark |
| 403 | [A Podracing Prototype](#case-403) | Demo |
| 404 | [A Ten-Second Claude Underwear Commercial](#case-404) | Demo |
| 405 | [A Bird at Sunrise, Stroke by Stroke](#case-405) | Demo |
| 406 | [A Long Graphics Run in Devin](#case-406) | Evaluation |
| 407 | [Code-Painted Art across Three Models](#case-407) | Evaluation |
| 408 | [The History of Writing in Motion](#case-408) | Demo |
| 409 | [A Test Ground for Game Machines](#case-409) | Demo |
| 410 | [Handheld Linux Console PCB Design](#case-410) | Evaluation |
| 411 | [A Voxel Lake Scene](#case-411) | Demo |
| 412 | [Arena's 17 Interactive Generations](#case-412) | Demo |
| 413 | [Flying with a Friendly Dragon](#case-413) | Demo |
| 414 | [Jelly Orca across Fable and Opus](#case-414) | Evaluation |
| 415 | [An Open-Ended Video Quality Test](#case-415) | Demo |
| 416 | [Mediterranean-Themed Space Habitat](#case-416) | Demo |
| 417 | [AA-3D Interactive Experience Benchmark](#case-417) | Benchmark |
| 418 | [A Timed Skeletal Game Challenge](#case-418) | Demo |
| 419 | [Pixel Art across Fable and Astra](#case-419) | Evaluation |
| 420 | [Motion-Design Portfolio Reel](#case-420) | Demo |
| 421 | [Glass Pool Render across Two Models](#case-421) | Evaluation |
| 422 | [Tool-Call Accuracy on TS-Bench](#case-422) | Benchmark |
| 423 | [Machu Picchu as a Miniature World](#case-423) | Demo |
| 424 | [GDPx by Professional Task Category](#case-424) | Benchmark |
| 425 | [Drawing a Portrait in a Paint App](#case-425) | Demo |
| 426 | [VulcanBench Frontier v4 at Low Effort](#case-426) | Benchmark |
| 427 | [A Playable Backrooms Role Reversal](#case-427) | Demo |
| 428 | [Bugatti Tourbillon in Blender](#case-428) | Demo |
| 429 | [A Computer-Themed Video with Two Models](#case-429) | Demo |
| 430 | [A Megakernel Music Video](#case-430) | Demo |
| 431 | [Studio Tour from Reference Photos](#case-431) | Demo |
| 432 | [A 1990s Toy Commercial in Code](#case-432) | Demo |
| 433 | [A Third-Person Three.js Game Scene](#case-433) | Demo |
| 434 | [Bryceball from an Existing Renderer](#case-434) | Demo |
| 435 | [Recursive Video Editing with Fable](#case-435) | Demo |
| 436 | [Cinematic History of Science](#case-436) | Demo |
| 437 | [Da Vinci Flying Machine in 3D](#case-437) | Integration |
| 438 | [PCB Routing from a Design Brief](#case-438) | Demo |
| 439 | [Same Prompt in Different Harnesses](#case-439) | Evaluation |
| 440 | [Code-Drawn Godzilla Artwork](#case-440) | Demo |
| 441 | [Handheld Fan Designed for 3D Printing](#case-441) | Demo |
| 442 | [Plugin Bug Hunt against Opus](#case-442) | Evaluation |
| 443 | [Istanbul Rebuilt as a 3D Scene](#case-443) | Demo |
| 444 | [A Blender Studio Film with a Working Screen](#case-444) | Demo |
| 445 | [A Black-Hole Transition at Weak Coupling](#case-445) | Evaluation |
| 446 | [The Limit of a Modular Bootstrap Bound](#case-446) | Evaluation |
| 447 | [Vercel AI Gateway with Ordered Model Fallbacks](#case-447) | Integration |
| 448 | [Nested Subagents and Review Budget](#case-448) | Limit |
| 449 | [LCARS Design-to-HTML Comparison](#case-449) | Evaluation |
| 450 | [GPU Optimization for Quantum ESPRESSO](#case-450) | Benchmark |
| 451 | [Artificial Analysis Intelligence Index by Effort](#case-451) | Benchmark |
| 452 | [False Positives in a High-Effort Change Review](#case-452) | Limit |
| 453 | [Thirty Routine Coding Tasks](#case-453) | Evaluation |
| 454 | [Desert-Island Castaway Screensaver](#case-454) | Demo |
| 455 | [Three Browser Game Builds at High Effort](#case-455) | Evaluation |
| 456 | [Chapter-by-Chapter Book Podcast Scripts](#case-456) | Evaluation |
| 457 | [A Production Service Migrated to Rust](#case-457) | Evaluation |
| 458 | [Selecting Fable 5.2 in GitHub Copilot](#case-458) | Integration |
| 459 | [A Hundred-Page HTML Design Challenge](#case-459) | Evaluation |
| 460 | [Compiler Requirements Drift](#case-460) | Limit |
| 461 | [Monitoring a Long Fable Run with Opus](#case-461) | Integration |
| 462 | [Fresh-Eyes Passes for Code Review](#case-462) | Tutorial |
| 463 | [Drift During a Feature-Design Review](#case-463) | Limit |
| 464 | [DX Ball–Style Breakout Comparison](#case-464) | Evaluation |
| 465 | [A 3D App Improvement Trial](#case-465) | Evaluation |
| 466 | [Mouse and Cat Game Across Three Models](#case-466) | Evaluation |
| 467 | [AIBenchy High-Effort Cost and Score Comparison](#case-467) | Benchmark |
| 468 | [Tuning a Fable 5.2 Agent Harness](#case-468) | Tutorial |

<a id="fable-5-2-cases"></a>
## Use Cases

<a id="case-330"></a>
### Case 330: [MacBook SVG Drawing Across Effort Levels](https://playcode.io/blog/macbook-svg-benchmark#compare) (by [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**Compare drawing quality, tokens, and output ceilings under a fixed brief.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode reports Fable 5.2 used 76,158 tokens at High for $3.05. Xhigh and Max streamed runs hit the 128,000-token ceiling without a drawing; both completed when given more room through the Batch API. Rankings are the publisher’s visual judgments.

[Related evidence 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [Four-Player Beat ’Em Up from Family Drawings](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (by [Lex](https://notesbylex.com/))

**Give a coding agent sketches, an existing prototype, and specific controller requirements.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex used Claude Code to rebuild a prior side-scrolling game into a 12-level, 18-character beat ’em up, with image and audio tools supplying assets. Four controllers worked in family playtesting.

[Related evidence 1](https://aidens-revenge.pages.dev/) · [Related evidence 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [Related evidence 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [Three Electronic Devices from Design to Assembly](https://www.anthropic.com/research/claude-electronics-design) (by [@Anthropic](https://www.anthropic.com/))

**Check the circuit, enclosure, and firmware as one system.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ Play video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic and Diode report three working devices. Fable 5.2 routed circuit boards, modelled enclosures, wrote software, and guided testing after manufacturing.

[Related evidence 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [Related evidence 2](https://www.youtube.com/watch?v=vdYynH177h0) · [Related evidence 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [Formalizing Fermat’s Last Theorem in Lean](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (by [@Anthropic](https://www.anthropic.com/))

**Use a proof checker and intermediate theorem statements as milestones.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Anthropic reports that a team of 1,000 Fable 5.2 agents formalized the existing proof in 30 hours. Opus 5.5 reached 26% in 18 hours under the same team setup.

[Related evidence 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [Related evidence 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [An Operating System from an Empty Folder](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (by [@Anthropic](https://www.anthropic.com/))

**Check boot, drivers, storage, and installation separately.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ Play video</a>

Anthropic reports that Fable 5.2 coordinated more than 1,000 subagents over eight days to build a prototype OS that booted on a laptop.

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [RoboDojo Dual-Arm Manipulation](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (by [@Anthropic](https://www.anthropic.com/))

**Compare the same simulated manipulation tasks across models.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ Play video</a>

Anthropic reports 64.9% for Fable 5.2, versus 27.6% for Fable 5.1, on RoboDojo. The release includes a robotics demonstration.

[Related evidence 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [A Fountain in Motion](https://x.com/Angaisb_/status/2119909059277238733) (by [@Angaisb_](https://x.com/Angaisb_))

**Use continuous water motion to judge a scene's visual rhythm.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

The creator shares a fountain scene attributed to Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [Frame-Aligned Lip Sync with Higgsfield](https://x.com/higgsfield_ai/status/2119909938969580024) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Align timing at the frame level before reviewing the clip.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ Play video</a>

Higgsfield reports tracking the mouth and timing audio to the frames using Fable 5.2 in its workflow.

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [An Open-World Driving Prototype](https://x.com/ericmaskfr/status/2119910195325481026) (by [@ericmaskfr](https://x.com/ericmaskfr))

**Test a short open-world brief on a playable slice.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ Play video</a>

The creator shares a game prototype inspired by GTA and reports completing the run in about 2 hours and 14 minutes.

Original prompt

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [Paris in 1940 with Reference Images](https://x.com/higgsfield_ai/status/2119910344998912507) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Separate reference-image generation from scene code.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ Play video</a>

Higgsfield supplied reference images through its MCP and used Fable 5.2 for a Three.js scene.

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable Plans an Opus-Rendered Short](https://x.com/kloss_xyz/status/2119910613828980846) (by [@kloss_xyz](https://x.com/kloss_xyz))

**Separate planning from implementation in a video workflow.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ Play video</a>

Fable 5.2 wrote the brief and plan. Opus 5.5 executed the 16-second Blender and Python animation and synthesized the score.

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [A Music-Video Experiment](https://x.com/WesRoth/status/2119911161386934330) (by [@WesRoth](https://x.com/WesRoth))

**Review both the lyrics and the generated sequence.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ Play video</a>

The creator shares a Fable 5.2 music video and comments on its lyrics.

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [A Painted Portrait of Dario Amodei](https://x.com/Mr_Salio/status/2119911922577637543) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Compare a stylized portrait with the reference shown alongside it.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ Play video</a>

The creator shares a portrait of Dario Amodei attributed to Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [Spud Smash at Medium Effort](https://x.com/argofowl/status/2119913148929187960) (by [@argofowl](https://x.com/argofowl))

**Give a game prototype clear actions and an objective.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ Play video</a>

The creator shares a potato character that punches, headbutts, or burns blue chairs.

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Ice Cathedral across Fable and Opus](https://x.com/QQTeng/status/2119913518015435103) (by [@QQTeng](https://x.com/QQTeng))

**Compare generation time and cost for the same scene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ Play video</a>

The creator reports about 1 hour 57 minutes and $81.10 for Fable, versus about 3 hours 11 minutes and $45.97 for Opus.

Original prompt

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [Singing with Simulated Vocal Tracts](https://x.com/banteg/status/2119914098171199996) (by [@banteg](https://x.com/banteg))

**Use a physical voice model as a music-production input.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ Play video</a>

The creator shares a cover made with two Chimera vocal-tract simulations and a vocoder mix.

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [Three Istanbul Voxel Tests](https://x.com/Avenoxai/status/2119914308603953485) (by [@Avenoxai](https://x.com/Avenoxai))

**Compare a destruction scene, a working clock, and a map.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ Play video</a>

The creator shares three single-prompt tests and reports scores of 100, 100, and 95.6 on their own rubric.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Remote Labor Index Project Completion](https://x.com/ScaleAILabs/status/2119914701736075489) (by [@ScaleAILabs](https://x.com/ScaleAILabs))

**Read the rate as an evaluation of specific projects.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ Play video</a>

Scale Labs and CAIS report that Fable 5.2 successfully completed 41.3% of assessed remote-work projects.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [Iceberg Scene at Four Effort Levels](https://x.com/0xRhinoX/status/2119915121698840587) (by [@0xRhinoX](https://x.com/0xRhinoX))

**Compare completion, cost, and detail as effort rises.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ Play video</a>

The creator used the same prompt at four effort levels. High omitted the aurora, while Ultra added glowing ice and an underwater view.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [A Seventy-Nine-Second Anime Short](https://x.com/anstapnever/status/2119915123070644263) (by [@anstapnever](https://x.com/anstapnever))

**Inspect scene continuity over a longer animation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ Play video</a>

The creator shares a 79-second anime clip attributed to a Fable 5.2 workflow.

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Mechanical Assemblies across Fable and Opus](https://x.com/ivanainai/status/2119915243321397550) (by [@ivanainai](https://x.com/ivanainai))

**Compare how each model lays out a mechanical assembly.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ Play video</a>

The author shows labelled Fable 5.2 and Opus 5.5 renders of an exploded wheel and gear assembly.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [A Robotic Hand Climbing a Spiral Staircase](https://x.com/Luckyballa/status/2119915557663506720) (by [@Luckyballa](https://x.com/Luckyballa))

**Use a simulated obstacle to inspect unusual locomotion.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ Play video</a>

The creator shares a Fable 5.2 and Steel 0.1 test of a Wuji hand walking on its fingers.

[Related evidence 1](https://github.com/skild-ai/steel-webgpu/pull/7)

Original prompt

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [Rigging a Tripo Mesh in Blender](https://x.com/0xKense1/status/2119916096098582566) (by [@0xKense1](https://x.com/0xKense1))

**Use numerical checks for grip, texture, and deformation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ Play video</a>

The author compares two rigs built from Tripo assets. Fable produced two clips in 36 minutes, and Opus produced eight in about 21 minutes.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [Da Vinci Notebook as Interactive Inventions](https://x.com/alexalbert__/status/2119916954337349737) (by [@alexalbert__](https://x.com/alexalbert__))

**Use source drawings to ground an interactive educational model.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ Play video</a>

Alex Albert supplied a PDF of Leonardo's notebook and shared an interactive interpretation of its inventions.

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [A Music Workstation Controlled by Claude](https://x.com/The_Alex/status/2119917226769985785) (by [@The_Alex](https://x.com/The_Alex))

**Use an agent-controlled tool for repeated composition requests.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ Play video</a>

The author shares a digital audio workstation made with Fable 5.2 and reports that Opus later opened it to create a song.

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [An Animated Raspberry Pi 5](https://x.com/sparklabhq/status/2119917375080521921) (by [@sparklabhq](https://x.com/sparklabhq))

**Use a product-animation brief to inspect component detail.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ Play video</a>

The creator shares an animated Raspberry Pi 5 made with Fable 5.2.

Original prompt

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [A Northern Italian Scene](https://x.com/Angaisb_/status/2119917807119089926) (by [@Angaisb_](https://x.com/Angaisb_))

**Inspect scenery and atmosphere in a place-based brief.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ Play video</a>

The creator shares a Fable 5.2 scene set in northern Italy.

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [Popup Book with Local Builder Agents](https://x.com/atomicagent_io/status/2119918110752846094) (by [@atomicagent_io](https://x.com/atomicagent_io))

**Compare orchestration against a single-model run on the same task.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ Play video</a>

Atomic reports $2.98 in 11 minutes with Fable coordinating local Qwen builders, versus $15.77 in 21 minutes using Fable alone.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [A Reintroduced Lava-Lamp Test](https://x.com/eidzoku/status/2119918134060601690) (by [@eidzoku](https://x.com/eidzoku))

**Use the same visual task to compare several models.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ Play video</a>

The author revived a lava-lamp test and shared the generated visual comparison.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [A Detailed Jet Built in Blender](https://x.com/higgsfield_ai/status/2119918248955392431) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Specify part counts, duration, and appearance in the brief.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ Play video</a>

Higgsfield reports a scripted Blender model with 931 parts and 24,260 rivets using Fable 5.2 and its MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [Portal Journey across Hundreds of Worlds](https://x.com/emollick/status/2119918307457577163) (by [@emollick](https://x.com/emollick))

**Use portals to organize independently generated environments.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ Play video</a>

Ethan Mollick reports over 450 code-made worlds created by 25,000 agents and shares a playable build and repository.

[Related evidence 1](https://portals-endless-worlds.netlify.app/) · [Related evidence 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [A Six-Shot Bombay Bazaar in Three.js](https://x.com/higgsfield_ai/status/2119918834841010320) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Break a visual brief into explicitly timed shots.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ Play video</a>

Higgsfield shares a 21.5-second, six-shot bazaar sequence rendered in Three.js.

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [A Photoreal Diner Built in Code](https://x.com/higgsfield_ai/status/2119918838490010008) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Use a code-only scene to inspect materials and lighting.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ Play video</a>

Higgsfield shows a diner scene and reports using code without a 3D modelling application for the build.

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [A Robot Model in Blender](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (by [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Use a turntable to inspect joints and silhouette.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ Play video</a>

The creator shows a small mechanical robot built in a Fable 5.2 Blender demonstration.

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [A Motion-Graphics Explainer for Convex](https://x.com/Rasmic/status/2119919466163093768) (by [@Rasmic](https://x.com/Rasmic))

**Use a short animation to explain a developer product.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ Play video</a>

The creator shares a motion-graphics explainer for Convex made with Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [A Collection of One-Shot Landing Pages](https://x.com/daradoescode/status/2119919529807466594) (by [@daradoescode](https://x.com/daradoescode))

**Compare hierarchy and layout across several short briefs.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ Play video</a>

The creator shares a video collection of landing-page outputs made with Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [A Piano Sonata Scored in LilyPond](https://x.com/imjustnewatai/status/2119919644836347926) (by [@imjustnewatai](https://x.com/imjustnewatai))

**Keep the score source tied to the rendered video.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ Play video</a>

The author asked for a Beethoven-style movement and reports that the notes shown come from the LilyPond source.

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [A Free-Form Video Brief](https://x.com/aollivier82/status/2119920990893244510) (by [@aollivier82](https://x.com/aollivier82))

**Use an unconstrained visual brief to inspect creative defaults.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ Play video</a>

The creator shares the result of asking Fable 5.2 for the most beautiful video it could make.

Original prompt

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable Plans, DeepSeek Builds, Opus Reviews](https://x.com/ivanfioravanti/status/2119921810267636201) (by [@ivanfioravanti](https://x.com/ivanfioravanti))

**Assign coordination, implementation, and review to separate agents.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ Play video</a>

The author shows Fable using herdr to coordinate four DeepSeek V4.1 Flash workers, with Opus 5.5 reviewing pull requests.

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [Fable 5.2 in the AI Village](https://x.com/aidigest_/status/2119923190411719158) (by [@aidigest_](https://x.com/aidigest_))

**Inspect an agent’s actual reply and memory actions separately.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

The public AI Village log shows Fable agreeing to revise its memory later in response to another agent’s request. A related post shows Fable taking a character-matching quiz.

[Related evidence 1](https://x.com/aidigest_/status/2119923209311260707) · [Related evidence 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [Frontend Design with and without Skills](https://x.com/AdamHoltererer/status/2119924849321914653) (by [@AdamHoltererer](https://x.com/AdamHoltererer))

**Hold the model fixed and vary the skill setup.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

The creator shows two frontend outputs using Fable 5.2, one with skills and one without.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [Find Implicit State Machines in a Codebase](https://x.com/kunchenguid/status/2119924895060795492) (by [@kunchenguid](https://x.com/kunchenguid))

**Audit a concrete module and ask for before-and-after diagrams.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

The author shows a cleanup in the Firstmate repository and publishes the exact audit prompt.

[Related evidence 1](https://github.com/kunchenguid/lavish-axi)

Original prompt

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [A Game Built from Scratch in Eight Hours](https://x.com/felixrieseberg/status/2119925633564463609) (by [@felixrieseberg](https://x.com/felixrieseberg))

**Track cached input, generated assets, and wall-clock time.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ Play video</a>

The Anthropic engineer reports creating models, sounds, and textures in a single run with about $550 in API-equivalent cost.

[Related evidence 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [Related evidence 2](https://x.com/AndrewCurran_/status/2119953960794780133)

Original prompt

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Fishslop Prototype and Token Cost](https://x.com/theo/status/2119926277801144695) (by [@theo](https://x.com/theo))

**Compare a game build with a prior model result.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ Play video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

The creator reports 76 minutes and about $42 in tokens and compares the result with Opus 5.5.

[Related evidence 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [A Football Game in Motion](https://x.com/WesRoth/status/2119926801514529027) (by [@WesRoth](https://x.com/WesRoth))

**Test feedback and score cues in a sports prototype.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ Play video</a>

The creator shares a Fable 5.2 gameplay result with on-screen football scoring feedback.

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [Open-World Boss Fight with Higgsfield MCP](https://x.com/higgsfield_ai/status/2119926932343324795) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Separate the playable game from its cinematic cutscenes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ Play video</a>

Higgsfield reports a browser game with an open world, a three-act boss fight, and cutscenes using Fable 5.2 and its MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [Mont Saint-Michel and Changing Tides](https://x.com/loktar00/status/2119927152489472076) (by [@loktar00](https://x.com/loktar00))

**Test changing water levels in a small historical scene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ Play video</a>

The creator shares a miniature Mont Saint-Michel with animated tides.

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [A Roblox Asset in Blender](https://x.com/hiyouwhatsapp/status/2119927163264573642) (by [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**Review an asset in Blender before importing it.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ Play video</a>

The creator shares a near-one-shot Blender result for Roblox development.

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [Reasoning without Chain-of-Thought Output](https://x.com/Tim_Hua_/status/2119927284761293089) (by [@Tim_Hua_](https://x.com/Tim_Hua_))

**Evaluate answers under the same reasoning-output constraint.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

The evaluator ran reasoning and knowledge tests without chain-of-thought output and reports Fable 5.2 slightly below GPT-6.1 Sol.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [Chrome Dino Remakes across Four Models](https://x.com/noclipepe/status/2119927838321328577) (by [@noclipepe](https://x.com/noclipepe))

**Compare task time and cost on a recurring game brief.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ Play video</a>

The creator adds Fable 5.2 to an existing T-Rex test with Opus, Gemini, and Astra and shows the outputs together.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [Checkers with a Robot Arm](https://x.com/karolina_dubiel/status/2119928342115676576) (by [@karolina_dubiel](https://x.com/karolina_dubiel))

**Read back joint positions and retry missed grasps.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ Play video</a>

The creator reports that the model corrected about 7 mm of sag and used feedback to retry missed moves.

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [A Fifteen-Second Motion Graphics Clip](https://x.com/aziz4ai/status/2119928581405200726) (by [@aziz4ai](https://x.com/aziz4ai))

**Track the quota consumed by a short code-animation test.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ Play video</a>

The creator shares a 15-second scene made with code and reports using 4% of a weekly allowance.

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [A Playable Eiffel Tower Scene](https://x.com/bobyau/status/2119928812628771212) (by [@bobyau](https://x.com/bobyau))

**Test whether a landmark model supports interaction.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ Play video</a>

The creator shares an Eiffel Tower demo and reports a 25-minute build.

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [Offshore Racing with Three.js and Higgsfield](https://x.com/higgsfield_ai/status/2119928918035910668) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Separate game logic from media tooling in a hybrid build.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ Play video</a>

Higgsfield shows a racing game with large waves, five AI rivals, and homing rockets.

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [Real-Time Honey Simulation in WebGL](https://x.com/deedydas/status/2119930300990177509) (by [@deedydas](https://x.com/deedydas))

**Use a browser physics simulation to test material motion.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ Play video</a>

The author shares a real-time WebGL honey simulation and publishes the original short brief.

Original prompt

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [Programmatic Visual Effects for Footage](https://x.com/ashebytes/status/2119930763105931649) (by [@ashebytes](https://x.com/ashebytes))

**Review the timing and placement of effects over the original clip.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ Play video</a>

The creator shares a Fable 5.2 visual-effects test with animated graphics composited over live footage.

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [A Motion Explainer for GTA Wanted Levels](https://x.com/saimagnate/status/2119931563760632311) (by [@saimagnate](https://x.com/saimagnate))

**Pair game footage with diagrams when explaining a gameplay system.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ Play video</a>

The creator reports a one-shot Fable 5.2 result. The clip uses gameplay footage and diagrams comparing wanted systems in GTA V and RDR2.

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [A Stylized MMO World in Code](https://x.com/Izkimar/status/2119931740940640542) (by [@Izkimar](https://x.com/Izkimar))

**Use stylized assets to assess consistency across a world.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ Play video</a>

The creator reports building the shown MMO world in one day with assets generated through code.

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [A 3D Scene across Fable and Opus](https://x.com/dom_scholz/status/2119933150025363661) (by [@dom_scholz](https://x.com/dom_scholz))

**Compare setup time and output detail in one viewing.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ Play video</a>

The author shares a paired Fable 5.2 and Opus 5.5 render and reports a quicker Fable run.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [Redundant Text in a Game Pause Screen](https://x.com/AndrewPrifer/status/2119934600608915465) (by [@AndrewPrifer](https://x.com/AndrewPrifer))

**Review generated interface copy for repeated explanations.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

The developer points to a pause screen as an example of Fable 5.2 writing more explanatory text than needed.

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [Moodboards with a Krea Harness](https://x.com/lambdacalcc/status/2119934725662060663) (by [@lambdacalcc](https://x.com/lambdacalcc))

**Compare concepts before committing to a visual direction.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

The creator shares four outputs from a moodboard session using Fable 5.2 with a Krea harness.

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [Office Playtest of a Portal Shooter](https://x.com/_sholtodouglas/status/2119935331499925557) (by [@_sholtodouglas](https://x.com/_sholtodouglas))

**Use multiplayer playtests to evaluate a generated game.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ Play video</a>

An Anthropic engineer shares an arena FPS with portals and describes office playtests.

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [A Detailed Blender Hard-Surface Asset](https://x.com/ziwenxu_/status/2119937420280168929) (by [@ziwenxu_](https://x.com/ziwenxu_))

**Inspect topology and silhouette in the Blender viewport.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ Play video</a>

The creator shares a detailed hard-surface asset presented as a Fable 5.2 Blender result.

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [Parallel Frontend Tests across Effort Levels](https://x.com/AI_masaou/status/2119937635322085640) (by [@AI_masaou](https://x.com/AI_masaou))

**Compare simple and ambitious briefs at several effort levels.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

The author reports similar simple outputs from Fable and Opus, richer details in larger Fable builds, and a sharp increase in time and tokens between Medium and High.

[Related evidence 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [A Small Game Built in Ten Prompts](https://x.com/AmirMushich/status/2119937977426338283) (by [@AmirMushich](https://x.com/AmirMushich))

**Track iteration count and artifact size in a game prototype.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ Play video</a>

The creator reports a 220 KB game with about 3,400 lines of code and shares the code and footage.

[Related evidence 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [A JavaScript Frame-by-Frame Animation](https://x.com/kevin_t_ngo/status/2119938129079808282) (by [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Inspect a sequence whose frames are drawn programmatically.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ Play video</a>

The author shared an animation and reports that JavaScript drew every frame.

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [Video Reference to 3D Animation](https://x.com/KHvostikk/status/2119939061049889130) (by [@KHvostikk](https://x.com/KHvostikk))

**Use footage as a reference when judging a rebuilt scene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ Play video</a>

The creator shares a Fable 5.2 video-to-3D animation demonstration.

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Pixel Campfire across Fable and Opus](https://x.com/GrilliotTodd/status/2119939651385655692) (by [@GrilliotTodd](https://x.com/GrilliotTodd))

**Compare lighting and silhouettes on one pixel-art subject.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ Play video</a>

The side-by-side outputs show Fable 5.2 and Opus 5.5 rendering the same campfire subject.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [Arena WebDev at xHigh](https://x.com/arena/status/2119941204003770690) (by [@arena](https://x.com/arena))

**Compare the specific effort setting used on the leaderboard.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena reports a 1,832-point debut for Claude Fable 5.2 xHigh on Code Arena WebDev.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [Movie Trailer Typography across Models](https://x.com/muku_sns/status/2119941490969624679) (by [@muku_sns](https://x.com/muku_sns))

**Compare two interpretations of the same paragraph.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ Play video</a>

The author shows Opus and Fable trailer titles side by side. The Fable version adds a red border motif and redacted titles.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [One-Prompt Motion and 3D Portfolio Tests](https://x.com/Khazix0918/status/2119941585538572390) (by [@Khazix0918](https://x.com/Khazix0918))

**Test research, design, and rendering as separate parts of a creative brief.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ Play video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ Play video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ Play video</a></td></tr></table>

The author shares four runs covering a ChatGPT anniversary reel, a DeepSeek explainer, a Three.js scene, and a 3D recreation of Apple Jing’an.

[Related evidence 1](https://x.com/Khazix0918/article/2119941585538572390)

Original prompt

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [An Explorable Nuclear Reactor Explainer](https://x.com/konstantinsaifo/status/2119941967136379334) (by [@konstantinsaifo](https://x.com/konstantinsaifo))

**Use a disassembly interaction to show how parts fit.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ Play video</a>

The creator asked for a Three.js reactor model that can be taken apart and reports $92 in API costs.

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Blood on the Clocktower Agents](https://x.com/dwarkesh_sp/status/2119942657812451482) (by [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**Compare models on the same hidden-role game.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

The evaluator reports Fable 5.2 above Fable 5.1 and Opus 5.5, with GPT-6 Astra ahead in this benchmark.

[Related evidence 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [A Podracing Prototype](https://x.com/loktar00/status/2119943124965638444) (by [@loktar00](https://x.com/loktar00))

**Use a familiar race format to judge motion and handling.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ Play video</a>

The creator shares a Fable 5.2 podracer-style result.

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [A Ten-Second Claude Underwear Commercial](https://x.com/Masimo_Blue/status/2119943368612487285) (by [@Masimo_Blue](https://x.com/Masimo_Blue))

**Test a loose product brief with original music.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ Play video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

The creator shares a ten-second promotional video with acid-techno music and the supplied product imagery.

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [A Bird at Sunrise, Stroke by Stroke](https://x.com/mgrczyk/status/2119943813028548721) (by [@mgrczyk](https://x.com/mgrczyk))

**Disable undo to inspect sequential drawing decisions.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ Play video</a>

The creator shows a bird-at-sunrise painting made one stroke at a time in a harness that prevented edits to previous marks.

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [A Long Graphics Run in Devin](https://x.com/Da7_Tech/status/2119944847255896490) (by [@Da7_Tech](https://x.com/Da7_Tech))

**Record time and spend when testing a demanding render.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ Play video</a>

A disclosed Cognition ambassador shares a Devin Max run reported at roughly $82 and 3.5 hours.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [Code-Painted Art across Three Models](https://x.com/kickingkeys/status/2119945841997672698) (by [@kickingkeys](https://x.com/kickingkeys))

**Compare drawing motion and synthesized sound across runs.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ Play video</a>

The creator shares a code-made painting with audio and describes same-prompt tests of Fable 5.2, Fable 5.1, and Gemini 4 Argon.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [The History of Writing in Motion](https://x.com/rileybrown/status/2119946022767980985) (by [@rileybrown](https://x.com/rileybrown))

**Use a timeline to organize a code-generated explainer.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ Play video</a>

The creator shows a history-of-writing animation and describes it as a one-prompt run.

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [A Test Ground for Game Machines](https://x.com/techartist_/status/2119946891106394518) (by [@techartist_](https://x.com/techartist_))

**Prototype mechanics, physics, and effects in a shared test scene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ Play video</a>

The creator built a proving ground for four concepts using Three.js and Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [Handheld Linux Console PCB Design](https://x.com/seveibar/status/2119947341230907453) (by [@seveibar](https://x.com/seveibar))

**Compare model designs on the same circuit brief.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ Play video</a>

The tscircuit creator shows a handheld Linux gaming device test using Astra 6 High and Fable 5.2 High.

Original prompt

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [A Voxel Lake Scene](https://x.com/Angaisb_/status/2119947748690841841) (by [@Angaisb_](https://x.com/Angaisb_))

**Use a small environment brief to inspect composition.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ Play video</a>

The creator shares a voxel lake attributed to Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [Arena's 17 Interactive Generations](https://x.com/arena/status/2119948067449536733) (by [@arena](https://x.com/arena))

**Browse several kinds of output before choosing a benchmark task.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ Play video</a>

Arena shares 17 generations covering 3D worlds, games, interfaces, data visualizations, and code-driven animations.

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [Flying with a Friendly Dragon](https://x.com/chetanankola/status/2119951015407738913) (by [@chetanankola](https://x.com/chetanankola))

**Use a flight loop to test camera and movement.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ Play video</a>

The creator shares a Three.js and Blender dragon scene and describes improvements made with Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Jelly Orca across Fable and Opus](https://x.com/vib3coded/status/2119951060752375827) (by [@vib3coded](https://x.com/vib3coded))

**Compare surface and motion on the same subject.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ Play video</a>

The creator shares a side-by-side jelly orca demonstration from Fable 5.2 and Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [An Open-Ended Video Quality Test](https://x.com/suna_gaku/status/2119952985933697063) (by [@suna_gaku](https://x.com/suna_gaku))

**Give a broad creative brief to inspect the model's choices.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ Play video</a>

The creator asked the model to demonstrate its strongest video work and shared the result.

Original prompt

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [Mediterranean-Themed Space Habitat](https://x.com/MaxXWilliamson/status/2119953172634677533) (by [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**Pair a short design brief with established project tools.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ Play video</a>

The creator supplied tools from prior space-habitat builds and asked for a Mediterranean-themed station.

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [AA-3D Interactive Experience Benchmark](https://x.com/ArtificialAnlys/status/2119953570430881946) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Read Elo with its uncertainty interval.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ Play video</a>

Artificial Analysis reports a 1,271 Elo launch snapshot for Fable 5.2 Max on its interactive 3D benchmark.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [A Timed Skeletal Game Challenge](https://x.com/WesRoth/status/2119953913160093817) (by [@WesRoth](https://x.com/WesRoth))

**Use a visible timer to evaluate a playable prototype.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ Play video</a>

The creator shows a one-shot Fable 5.2 result with a skeletal character and an on-screen countdown.

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Pixel Art across Fable and Astra](https://x.com/Angaisb_/status/2119955179915137294) (by [@Angaisb_](https://x.com/Angaisb_))

**Compare shape and detail at the same output scale.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ Play video</a>

The original comparison shows pixel-art outputs from GPT-6 Astra and Fable 5.2.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [Motion-Design Portfolio Reel](https://x.com/Leviwoyun/status/2119955625820258308) (by [@Leviwoyun](https://x.com/Leviwoyun))

**Use an open-ended portfolio brief with a fixed duration.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ Play video</a>

The author shares a motion-design reel with music and reports a 24-minute production run.

Original prompt

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [Glass Pool Render across Two Models](https://x.com/MrTacticalX/status/2119955647542542439) (by [@MrTacticalX](https://x.com/MrTacticalX))

**Compare lighting quality alongside runtime and cost.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ Play video</a>

The creator reports 90 minutes and $57.87 for Fable versus 68 minutes and $14.39 for Opus in this render test.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [Tool-Call Accuracy on TS-Bench](https://x.com/gosrum/status/2119956559031927079) (by [@gosrum](https://x.com/gosrum))

**Track tool-call errors and token usage separately.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

The tester reports zero tool-call errors for Fable 5.2 and notes that the simpler tasks separate Claude variants poorly.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [Machu Picchu as a Miniature World](https://x.com/loktar00/status/2119958719362666708) (by [@loktar00](https://x.com/loktar00))

**Inspect atmosphere and small details in a miniature scene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ Play video</a>

The shared Machu Picchu demo includes volumetric fog and small alpacas.

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [GDPx by Professional Task Category](https://x.com/SemiAnalysis_/status/2119961447199289640) (by [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**Read subtask results alongside the aggregate.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

The benchmark publisher reports a 16.4% overall score and breaks out areas including chip design and software engineering.

[Related evidence 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [Related evidence 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [Related evidence 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [Drawing a Portrait in a Paint App](https://x.com/The_Alex/status/2119964472559489229) (by [@The_Alex](https://x.com/The_Alex))

**Use a reference thumbnail to guide a portrait in a drawing app.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ Play video</a>

The creator asked Fable 5.2 to open a paint app and draw them. The video shows the portrait progressing from outlines to a finished drawing.

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [VulcanBench Frontier v4 at Low Effort](https://x.com/morganlinton/status/2119966067527467215) (by [@morganlinton](https://x.com/morganlinton))

**Compare model generations at the same effort setting.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

The benchmark author reports roughly 5 versus 26 minutes per task for Fable 5.2 and 5.1 at Low effort.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [A Playable Backrooms Role Reversal](https://x.com/LexnLin/status/2119966127149429093) (by [@LexnLin](https://x.com/LexnLin))

**Change the player's objective to test a game concept.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ Play video</a>

The player controls the monster and tries to catch people. The creator shares a gameplay clip and play link.

[Related evidence 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [Bugatti Tourbillon in Blender](https://x.com/xikhar/status/2119966147328299284) (by [@xikhar](https://x.com/xikhar))

**Use reference images to specify both exterior and interior details.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ Play video</a>

The creator reports modelling a Bugatti Tourbillon, including its interior, and rendering a cinematic from a prompt and references.

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [A Computer-Themed Video with Two Models](https://x.com/daradoescode/status/2119966154391183522) (by [@daradoescode](https://x.com/daradoescode))

**Record the contributions of each model in a mixed workflow.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ Play video</a>

The creator shared a stylized video made with Fable 5.2 and substantial Opus 5.5 assistance.

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [A Megakernel Music Video](https://x.com/elliotarledge/status/2119968762069934415) (by [@elliotarledge](https://x.com/elliotarledge))

**Use a technical concept as the subject of a video brief.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ Play video</a>

The creator asked Fable 5.2 at High effort for a music video about megakernels and shared the clip.

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [Studio Tour from Reference Photos](https://x.com/rpnickson/status/2119969928304357507) (by [@rpnickson](https://x.com/rpnickson))

**Provide real photos to ground a scene recreation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ Play video</a>

The creator supplied photos of their studio, adapted a similar video brief, and reported a roughly two-hour run.

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [A 1990s Toy Commercial in Code](https://x.com/kevin_t_ngo/status/2119972124211454139) (by [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Separate animation scripting from rendering.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ Play video</a>

The creator reports animating a retro toy commercial with Python and rendering it in Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [A Third-Person Three.js Game Scene](https://x.com/bijanbowen/status/2119972220739187182) (by [@bijanbowen](https://x.com/bijanbowen))

**Use a gameplay run to inspect movement and scenery.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

The author shares a streamed Three.js result with a third-person character moving through an outdoor scene.

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [Bryceball from an Existing Renderer](https://x.com/pleometric/status/2119973274402668852) (by [@pleometric](https://x.com/pleometric))

**Reuse a rendering engine as the basis of a game.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ Play video</a>

The creator adapted the renderer discussed in the linked post into a playable project called Bryceball.

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [Recursive Video Editing with Fable](https://x.com/rileybrown/status/2119973951027724385) (by [@rileybrown](https://x.com/rileybrown))

**Use a previous edit as material for a follow-up piece.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ Play video</a>

The creator shared a Fable 5.2 edit about an earlier video they edited with the model.

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [Cinematic History of Science](https://x.com/DeryaTR_/status/2119974354260013293) (by [@DeryaTR_](https://x.com/DeryaTR_))

**Use a timeline brief to organize a 3D sequence.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ Play video</a>

The creator asked for a cinematic journey from early science to a speculative future and shared the resulting clip.

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [Da Vinci Flying Machine in 3D](https://x.com/higgsfield_ai/status/2119975721909301684) (by [@higgsfield_ai](https://x.com/higgsfield_ai))

**Model a historical design before testing changes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ Play video</a>

Higgsfield showed a 3D interpretation of Leonardo's flying machine and described a physics test and redesign.

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [PCB Routing from a Design Brief](https://x.com/cmonkey/status/2119975852977029365) (by [@cmonkey](https://x.com/cmonkey))

**Inspect the routed board before fabrication.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

The author shared a Fable 5.2 PCB-routing result in a follow-up to a discussion of layout work.

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [Same Prompt in Different Harnesses](https://x.com/loktar00/status/2119980613369319706) (by [@loktar00](https://x.com/loktar00))

**Record harness differences when comparing model outputs.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ Play video</a>

The creator gave DeepSeek and Fable 5.2 the same prompt in different harnesses and showed the results together.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [Code-Drawn Godzilla Artwork](https://x.com/chetaslua/status/2119981510199808368) (by [@chetaslua](https://x.com/chetaslua))

**Use vector-like shapes and motion to reinterpret an image.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ Play video</a>

The creator shared code-drawn artwork with a short animation inspired by a Godzilla post.

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [Handheld Fan Designed for 3D Printing](https://x.com/davelee/status/2119981787325579398) (by [@davelee](https://x.com/davelee))

**Use a physical prototype to check a modelled assembly.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ Play video</a>

The creator and their children designed a printable handheld fan and shared the model before printing.

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [Plugin Bug Hunt against Opus](https://x.com/oaranda/status/2119982729747919096) (by [@oaranda](https://x.com/oaranda))

**Compare fixes with cross-run regression tests.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

The author’s annotated launch excerpt.

Both models found the same six plugin bugs. Opus passed the cross-tests, while Fable missed one and identified another dashboard issue.

Original prompt

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [Istanbul Rebuilt as a 3D Scene](https://x.com/petergostev/status/2119877733488394520) (by [@petergostev](https://x.com/petergostev))

**Inspect a city-scale scene at both wide and close views.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ Play video</a>

Peter Gostev shares a 3D Istanbul output from Fable 5.2 Max and links the longer evaluation that accompanies it.

[Related evidence 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [A Blender Studio Film with a Working Screen](https://x.com/rileybrown/status/2119902109709537708) (by [@rileybrown](https://x.com/rileybrown))

**Animate the screen, lighting, and camera within the same 3D scene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ Play video</a>

The creator reports 13 camera shots, a custom webpage playing on the laptop, and ElevenLabs audio. The render used RunPod GPUs.

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [A Black-Hole Transition at Weak Coupling](https://hexagonmath.org/2611.00175v1) (by [@Anthropic](https://www.anthropic.com/))

**Check an unfinished calculation against the original theoretical setup.**

Anthropic reports that Fable 5.2 completed a long-standing calculation and found an abrupt transition in the weak-coupling regime. The preprint provides the derivation.

[Related evidence 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [The Limit of a Modular Bootstrap Bound](https://hexagonmath.org/2611.00174v1) (by [@Anthropic](https://www.anthropic.com/))

**Publish the derivation alongside a claimed analytical bound.**

Anthropic reports that Fable 5.2 determined the exact limit of a spinless modular-bootstrap technique used in a simplified quantum-gravity setting.

[Related evidence 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Vercel AI Gateway with Ordered Model Fallbacks](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (by [Vercel](https://vercel.com/))

**Configure fallback order in the gateway for classifier-declined requests.**

Vercel’s AI SDK example calls anthropic/claude-fable-5.2 and configures Opus 5.5 then Sonnet 5.5 as fallbacks. Its guide documents the gateway’s data-retention requirement.

[Related evidence 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [Nested Subagents and Review Budget](https://news.ycombinator.com/item?id=50430925) (by [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**Track nested delegation and enforce review budgets outside the prompt.**

The author requested at most four subagents for an 80,000-line code review. They report six or more nested agents and exhausting their five-hour usage allowance in under 20 minutes.

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [LCARS Design-to-HTML Comparison](https://news.ycombinator.com/item?id=50430962) (by [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**Check curves, icon fidelity, animation, and navigation as separate acceptance criteria.**

The author compares Fable 5.2 and Opus 5.5 against the same Star Trek–styled design. They preferred the Fable curves and some icons, but preferred Opus motion and found the Fable SVG flicker distracting. The author requested only the first page.

[Related evidence 1](https://html.non.io/lcars-fable-5.2/) · [Related evidence 2](https://html.non.io/lcars-opus-5.5/) · [Related evidence 3](https://news.ycombinator.com/item?id=50431231) · [Related evidence 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [GPU Optimization for Quantum ESPRESSO](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (by [Discovered Materials](https://discoveredmaterials.com/))

**Require reference results and representative hidden tests when optimizing scientific code.**

Discovered Materials reports 36× geometric-mean speedup across 13 same-GPU phonon benchmarks and roughly 9× for hybrid-functional calculations. Its released patch is grounded in correctness and performance tests.

[Related evidence 1](https://github.com/discovered-materials/dm_qe) · [Related evidence 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [Artificial Analysis Intelligence Index by Effort](https://artificialanalysis.ai/models/claude-fable-5-2) (by [Artificial Analysis](https://artificialanalysis.ai/))

**Read benchmark score, task cost, and latency together at the chosen effort.**

The cited Max default-fallback snapshot reports index score 65, $26.54 per task, and 46.4 minutes per task. The figures refer to the benchmark workload.

[Related evidence 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [False Positives in a High-Effort Change Review](https://news.ycombinator.com/item?id=50431810) (by [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**Verify model-generated review findings against the code before acting.**

A developer reports that a Fable 5.2 High review flagged two nonexistent problems in a change, which the developer caught through their own understanding of the code.

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [Thirty Routine Coding Tasks](https://news.ycombinator.com/item?id=50432483) (by [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**Measure elapsed time and successful tasks on the same coding workload.**

The author reports Fable 5.2 and Opus 5.5 each solved 26 of 30 tasks, versus 25 for Fable 5.1. Fable 5.2 took 0.62× the time of 5.1, with no reported safeguard stops.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [Desert-Island Castaway Screensaver](https://news.ycombinator.com/item?id=50432836) (by [@nzach](https://news.ycombinator.com/user?id=nzach))

**Use a playable page to inspect a model-built screensaver directly.**

The Show HN author links a browser-based island scene called Stranded with Claude. The published artifact is an interactive canvas.

[Related evidence 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [Three Browser Game Builds at High Effort](https://senko.net/vibecode-bench/) (by [Senko Rašić](https://senko.net/))

**Compare playable behavior and visual fidelity separately in a game benchmark.**

Senko Rašić ran the RTS, voxel, and flying simulator briefs through Fable 5.2 in Claude Code. The author reports deeper mechanics such as an airship for full-map exploration, while judging parts of the graphics worse.

[Related evidence 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [Chapter-by-Chapter Book Podcast Scripts](https://news.ycombinator.com/item?id=50434156) (by [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**Compare script length using the same recurring podcast assignment.**

The author generated dialogues between two book reviewers one chapter at a time. They report about 2.5 pages from the Fable versions versus 4.5 pages from Opus 5.5 and link both samples.

[Related evidence 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [Related evidence 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [A Production Service Migrated to Rust](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (by [@Anthropic](https://www.anthropic.com/))

**Measure startup behavior before and after a migration.**

Anthropic reports that agents running a prerelease Fable 5.2 version rewrote a Python production service in Rust, cutting startup time by roughly a factor of 26.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [Selecting Fable 5.2 in GitHub Copilot](https://x.com/github/status/2119926269982961833) (by [@github](https://x.com/github))

**Enable the organization policy before selecting the model.**

GitHub documents the model picker in Copilot clients and the administrator setting required for Business and Enterprise accounts.

[Related evidence 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [A Hundred-Page HTML Design Challenge](https://x.com/MiaAI_lab/status/2119930229661503893) (by [@MiaAI_lab](https://x.com/MiaAI_lab))

**Count completed and runnable files as well as visual quality.**

The author requested 100 varied designs and published 76 files with prompts. The author reports hitting the Fable usage limit.

[Related evidence 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [Related evidence 2](https://mia-ai.net/lab/experiments/100-htmls) · [Related evidence 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [Related evidence 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [Related evidence 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [Related evidence 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [Related evidence 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [Related evidence 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [Related evidence 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [Related evidence 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [Related evidence 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [Related evidence 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [Related evidence 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [Related evidence 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [Compiler Requirements Drift](https://x.com/sameQCU/status/2119939304864800971) (by [@sameQCU](https://x.com/sameQCU))

**Compare the agent's stated requirements against the input.**

The developer describes a compiler workload where Fable 5.2 and earlier Opus models misreported the requirements they had been given.

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [Monitoring a Long Fable Run with Opus](https://x.com/marouane53/status/2119950129767858262) (by [@marouane53](https://x.com/marouane53))

**Use a separate session to monitor progress on long tasks.**

The author reports Fable tasks running for more than two hours with sparse updates. They used Opus 5.5 in a separate thread to explain progress and decisions.

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [Fresh-Eyes Passes for Code Review](https://x.com/doodlestein/status/2119958895158292786) (by [@doodlestein](https://x.com/doodlestein))

**Run a separate review pass over both new and touched files.**

The creator shares two exact follow-up prompts for finding and correcting mistakes after an implementation.

Original prompt

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

Original prompt

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [Drift During a Feature-Design Review](https://news.ycombinator.com/item?id=50434214) (by [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**Use the current design as a checklist when reviewing an agent’s follow-up advice.**

The author compared the models during a feature-design review and preferred Opus 5.5. A subsequent Fable 5.2 diagnostic pass recommended something already present in the design.

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [DX Ball–Style Breakout Comparison](https://news.ycombinator.com/item?id=50434424) (by [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**Compare game mechanics and play feel under a recreation brief.**

The author links Fable 5.2 and Opus 5.5 versions from separate runs. Fable changed some original game mechanics; the author preferred the feel of the Opus version.

[Related evidence 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [Related evidence 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [A 3D App Improvement Trial](https://news.ycombinator.com/item?id=50434433) (by [@user43928](https://news.ycombinator.com/user?id=user43928))

**Compare visible changes with budget consumed on the same improvement task.**

The author reports asking Fable 5.2 to improve a non-game 3D app, seeing little difference versus Opus 5.5 and consuming 25% of their Fable plan allowance that evening.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [Mouse and Cat Game Across Three Models](https://news.ycombinator.com/item?id=50434508) (by [@simonw](https://news.ycombinator.com/user?id=simonw))

**Keep the game prompt fixed and inspect each model’s playable implementation.**

Simon Willison shares Fable 5.2 Extra, Opus 5.5 Extra, and GPT-6 Extra High attempts at a mobile-friendly Three.js game. He reports about 40 minutes for the Fable attempt.

[Related evidence 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [Related evidence 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [Related evidence 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

Original prompt

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [AIBenchy High-Effort Cost and Score Comparison](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (by [AIBenchy](https://aibenchy.com/))

**Compare score, total cost, and response time at matched effort labels.**

AIBenchy’s published comparison reports 8.7 vs 9.4, $5.083 vs $2.133 total cost, and 14.73s vs 27.55s average response time for Fable 5.2 High and Opus 5.5 High respectively.

[Related evidence 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [Tuning a Fable 5.2 Agent Harness](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (by [@Anthropic](https://www.anthropic.com/))

**Rerun effort tests and define progress updates before long tasks.**

Anthropic’s guide covers effort, completion criteria, approvals, progress messages, and subagent limits with example instructions.

[Related evidence 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="acknowledge"></a>
## Creator Credits

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/)
