# Claude Fable 5.2 の活用事例

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

11 月 10 日と 11 月 13〜14 日に収集したワークフロー、デモ、比較、ベンチマーク、連携、実用上の制約を、出典へのリンク付きで掲載しています。

[Anthropic の発表](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [過去の事例集](../../README_ja.md)

## 事例一覧

| Case | 活用事例 | Type |
| --- | --- | --- |
| 330 | [推論強度別の MacBook SVG 描画](#case-330) | Benchmark |
| 331 | [家族の絵を使った4人用ベルトスクロールアクション](#case-331) | Demo |
| 332 | [3台の電子機器を設計から組み立てまで進める](#case-332) | Demo |
| 333 | [Lean でフェルマーの最終定理を形式化](#case-333) | Evaluation |
| 334 | [空のフォルダーから作るOS](#case-334) | Demo |
| 335 | [RoboDojo の双腕操作ベンチマーク](#case-335) | Benchmark |
| 336 | [水が流れる噴水](#case-336) | Demo |
| 337 | [Higgsfield でフレーム単位のリップシンク](#case-337) | Integration |
| 338 | [オープンワールド運転ゲームの試作](#case-338) | Demo |
| 339 | [参考画像で再現する1940年のパリ](#case-339) | Integration |
| 340 | [Fable が企画し Opus が制作した短編](#case-340) | Integration |
| 341 | [ミュージックビデオの実験](#case-341) | Demo |
| 342 | [Dario Amodei の肖像画](#case-342) | Demo |
| 343 | [推論強度 Medium の Spud Smash](#case-343) | Demo |
| 344 | [Fable と Opus の氷の大聖堂](#case-344) | Evaluation |
| 345 | [声道シミュレーションで歌わせる](#case-345) | Demo |
| 346 | [イスタンブールを題材にした3つのボクセルテスト](#case-346) | Evaluation |
| 347 | [Remote Labor Index のプロジェクト完了率](#case-347) | Benchmark |
| 348 | [4段階の推論強度で描く氷山](#case-348) | Evaluation |
| 349 | [79秒のアニメ短編](#case-349) | Demo |
| 350 | [Fable と Opus が描く機械の組立図](#case-350) | Evaluation |
| 351 | [らせん階段を上るロボットハンド](#case-351) | Demo |
| 352 | [Blender で Tripo のメッシュをリギング](#case-352) | Evaluation |
| 353 | [ダ・ヴィンチの手稿を触って学べる発明展示に](#case-353) | Demo |
| 354 | [Claude が操作する音楽制作環境](#case-354) | Demo |
| 355 | [Raspberry Pi 5 の製品アニメーション](#case-355) | Demo |
| 356 | [イタリア北部の風景](#case-356) | Demo |
| 357 | [ローカルの作業エージェントで作る飛び出す絵本](#case-357) | Evaluation |
| 358 | [復活したラバランプテスト](#case-358) | Evaluation |
| 359 | [Blender で精密なジェット機を制作](#case-359) | Integration |
| 360 | [数百の世界を巡るポータルの旅](#case-360) | Demo |
| 361 | [Three.js で描くムンバイの市場の6カット](#case-361) | Integration |
| 362 | [コードで作る写実的なアメリカンダイナー](#case-362) | Integration |
| 363 | [Blender で作ったロボットモデル](#case-363) | Demo |
| 364 | [Convex のモーショングラフィックス解説](#case-364) | Demo |
| 365 | [一度の指示で作ったランディングページ集](#case-365) | Demo |
| 366 | [LilyPond で記譜したピアノソナタ](#case-366) | Demo |
| 367 | [自由な映像制作指示](#case-367) | Demo |
| 368 | [Fable が計画し、DeepSeek が実装し、Opus がレビュー](#case-368) | Integration |
| 369 | [AI Village に参加した Fable 5.2](#case-369) | Integration |
| 370 | [Skills の有無によるフロントエンド比較](#case-370) | Evaluation |
| 371 | [コードベースに潜むステートマシンの発見](#case-371) | Tutorial |
| 372 | [ゲームを8時間でゼロから制作](#case-372) | Demo |
| 373 | [Fishslop の試作とトークン費用](#case-373) | Evaluation |
| 374 | [アメリカンフットボールのプレイ映像](#case-374) | Demo |
| 375 | [Higgsfield MCP を使ったオープンワールドのボス戦](#case-375) | Integration |
| 376 | [モン・サン＝ミシェルの潮の満ち引き](#case-376) | Demo |
| 377 | [Blender で見る Roblox 向けアセット](#case-377) | Demo |
| 378 | [思考過程を出力しない推論評価](#case-378) | Benchmark |
| 379 | [4つのモデルで Chrome 恐竜ゲームを再制作](#case-379) | Evaluation |
| 380 | [ロボットアームでチェッカー](#case-380) | Demo |
| 381 | [15秒のモーショングラフィックス](#case-381) | Demo |
| 382 | [操作して遊べるエッフェル塔](#case-382) | Demo |
| 383 | [Three.js と Higgsfield で海上レースを作る](#case-383) | Integration |
| 384 | [WebGL で蜂蜜の流れをリアルタイム再現](#case-384) | Demo |
| 385 | [実写映像にプログラムで視覚効果を追加](#case-385) | Demo |
| 386 | [GTA の手配度を説明する映像](#case-386) | Demo |
| 387 | [コードで作るスタイライズされた MMO 世界](#case-387) | Demo |
| 388 | [Fable と Opus の3Dシーン比較](#case-388) | Evaluation |
| 389 | [ゲームのポーズ画面にある冗長な説明](#case-389) | Limit |
| 390 | [Krea の実行環境で作るムードボード](#case-390) | Integration |
| 391 | [職場で試遊したポータル付きシューティング](#case-391) | Demo |
| 392 | [Blender の精密なハードサーフェスアセット](#case-392) | Demo |
| 393 | [推論強度を変えた並行フロントエンドテスト](#case-393) | Evaluation |
| 394 | [10回のプロンプトで作った小さなゲーム](#case-394) | Demo |
| 395 | [JavaScript で一コマずつ描くアニメーション](#case-395) | Demo |
| 396 | [参考映像から作る3Dアニメーション](#case-396) | Demo |
| 397 | [Fable と Opus のドット絵のたき火](#case-397) | Evaluation |
| 398 | [推論強度 xHigh の Arena WebDev](#case-398) | Benchmark |
| 399 | [映画予告編のタイトル文字をモデル間で比較](#case-399) | Evaluation |
| 400 | [1つのプロンプトで試すモーションと3Dの作品集](#case-400) | Evaluation |
| 401 | [分解して学ぶ原子炉](#case-401) | Demo |
| 402 | [Blood on the Clocktower でのエージェント評価](#case-402) | Benchmark |
| 403 | [ポッドレース風の試作品](#case-403) | Demo |
| 404 | [10秒の Claude 下着CM](#case-404) | Demo |
| 405 | [朝日の中の鳥を一筆ずつ描く](#case-405) | Demo |
| 406 | [Devin で行う長時間のグラフィックス処理](#case-406) | Evaluation |
| 407 | [3モデルによるコード絵画の比較](#case-407) | Evaluation |
| 408 | [アニメーションでたどる文字の歴史](#case-408) | Demo |
| 409 | [ゲーム内の機械を試す実験場](#case-409) | Demo |
| 410 | [携帯型 Linux ゲーム機の PCB 設計](#case-410) | Evaluation |
| 411 | [ボクセルで作る湖](#case-411) | Demo |
| 412 | [Arena のインタラクティブな生成例17件](#case-412) | Demo |
| 413 | [友好的なドラゴンと飛ぶ](#case-413) | Demo |
| 414 | [Fable と Opus のゼリーのシャチ](#case-414) | Evaluation |
| 415 | [自由課題による映像品質テスト](#case-415) | Demo |
| 416 | [地中海をテーマにした宇宙居住施設](#case-416) | Demo |
| 417 | [AA-3D のインタラクティブ体験ベンチマーク](#case-417) | Benchmark |
| 418 | [骸骨キャラクターのタイムチャレンジ](#case-418) | Demo |
| 419 | [Fable と Astra のドット絵比較](#case-419) | Evaluation |
| 420 | [モーションデザインのポートフォリオ映像](#case-420) | Demo |
| 421 | [2つのモデルによるガラスのプールのレンダリング](#case-421) | Evaluation |
| 422 | [TS-Bench のツール呼び出し精度](#case-422) | Benchmark |
| 423 | [ミニチュアのマチュピチュ](#case-423) | Demo |
| 424 | [専門分野別の GDPx](#case-424) | Benchmark |
| 425 | [ペイントアプリで人物画を描く](#case-425) | Demo |
| 426 | [推論強度 Low の VulcanBench Frontier v4](#case-426) | Benchmark |
| 427 | [怪物側で遊ぶバックルーム](#case-427) | Demo |
| 428 | [Blender で Bugatti Tourbillon を制作](#case-428) | Demo |
| 429 | [2つのモデルで作るコンピューター映像](#case-429) | Demo |
| 430 | [Megakernel を題材にしたミュージックビデオ](#case-430) | Demo |
| 431 | [参考写真を使ったスタジオツアー](#case-431) | Demo |
| 432 | [コードで作る1990年代風のおもちゃCM](#case-432) | Demo |
| 433 | [Three.js の三人称ゲームシーン](#case-433) | Demo |
| 434 | [既存レンダラーから作る Bryceball](#case-434) | Demo |
| 435 | [Fable で編集した映像を再編集](#case-435) | Demo |
| 436 | [映画風にたどる科学史](#case-436) | Demo |
| 437 | [ダ・ヴィンチの飛行機械を3D化](#case-437) | Integration |
| 438 | [設計要件に沿った PCB 配線](#case-438) | Demo |
| 439 | [異なる実行環境で同じプロンプトを試す](#case-439) | Evaluation |
| 440 | [コードで描くゴジラ](#case-440) | Demo |
| 441 | [3Dプリント用の携帯扇風機](#case-441) | Demo |
| 442 | [Opus と比べるプラグインの不具合調査](#case-442) | Evaluation |
| 443 | [イスタンブールの3D再現](#case-443) | Demo |
| 444 | [画面の映像まで動く Blender のスタジオ映像](#case-444) | Demo |
| 445 | [弱結合領域でのブラックホールの急変](#case-445) | Evaluation |
| 446 | [モジュラー・ブートストラップの境界](#case-446) | Evaluation |
| 447 | [Vercel AI Gateway でモデルのフォールバック順を設定](#case-447) | Integration |
| 448 | [入れ子のサブエージェントとレビュー予算](#case-448) | Limit |
| 449 | [LCARS デザインから HTML への変換比較](#case-449) | Evaluation |
| 450 | [Quantum ESPRESSO のGPU最適化](#case-450) | Benchmark |
| 451 | [推論強度別の Artificial Analysis Intelligence Index](#case-451) | Benchmark |
| 452 | [High 設定の変更レビューで出た誤検出](#case-452) | Limit |
| 453 | [日常的なコーディング課題30件](#case-453) | Evaluation |
| 454 | [無人島のスクリーンセーバー](#case-454) | Demo |
| 455 | [推論強度 High のブラウザーゲーム3件](#case-455) | Evaluation |
| 456 | [章ごとに作る書評ポッドキャストの台本](#case-456) | Evaluation |
| 457 | [本番サービスを Rust に移行](#case-457) | Evaluation |
| 458 | [GitHub Copilot で Fable 5.2 を選ぶ](#case-458) | Integration |
| 459 | [HTML 100ページのデザインチャレンジ](#case-459) | Evaluation |
| 460 | [コンパイラ作業での要件のずれ](#case-460) | Limit |
| 461 | [長時間の Fable タスクを Opus で追う](#case-461) | Integration |
| 462 | [新たな視点でコードを再レビュー](#case-462) | Tutorial |
| 463 | [機能設計のレビューで助言がずれる](#case-463) | Limit |
| 464 | [DX Ball 風のブロック崩し比較](#case-464) | Evaluation |
| 465 | [3Dアプリの改善を試す](#case-465) | Evaluation |
| 466 | [3つのモデルが作るネコとネズミのゲーム](#case-466) | Evaluation |
| 467 | [AIBenchy の推論強度 High における費用とスコア](#case-467) | Benchmark |
| 468 | [Fable 5.2 のエージェント環境を調整する](#case-468) | Tutorial |
| 469 | [アニメーション付きキャラクターのプレビューアプリ](#case-469) | Demo |
| 470 | [ツールなしで生成した QR コードを検証](#case-470) | Evaluation |
| 471 | [Tripo を使った Unity のゾンビゲーム](#case-471) | Demo |
| 472 | [MS Paint で描く雪の街並み](#case-472) | Demo |
| 473 | [Wojak-Bench でつながらなかった電源コード](#case-473) | Limit |
| 474 | [リズムゲーム向けのピアノ曲](#case-474) | Evaluation |
| 475 | [Picnic のトークン回収フローを再設計](#case-475) | Demo |
| 476 | [生成した素材をアニメのオープニング映像に編集](#case-476) | Tutorial |
| 477 | [3 つのツールを使ったキャラクターアニメーション](#case-477) | Demo |
| 478 | [Blender スクリプトで都市の予告編をレンダリング](#case-478) | Demo |
| 479 | [JavaScript で描く夜景](#case-479) | Demo |
| 480 | [CAD モデルを製図図面に変換](#case-480) | Demo |
| 481 | [Plotly のデータ分析試験で 43 問に正解](#case-481) | Benchmark |
| 482 | [ウェブサイトで SGI Indy を再現](#case-482) | Demo |
| 483 | [Issue と worktree で複数のエージェントを調整](#case-483) | Integration |
| 484 | [バックグラウンド処理で引用文献を確認](#case-484) | Integration |
| 485 | [往復の貨物輸送価格モデルをデバッグ](#case-485) | Limit |
| 486 | [Edge0 の推論環境を Mac に対応させる](#case-486) | Integration |
| 487 | [高密度なプリント基板のレイアウトをレビュー](#case-487) | Limit |
| 488 | [有料公開の新聞記事を引用元までたどる](#case-488) | Limit |
| 489 | [Fable で計画を立て、Opus の変更をレビュー](#case-489) | Tutorial |

<a id="fable-5-2-cases"></a>
## 活用事例

<a id="case-330"></a>
### Case 330: [推論強度別の MacBook SVG 描画](https://playcode.io/blog/macbook-svg-benchmark#compare) (投稿者 [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**同じ指示で描画品質、トークン数、出力上限を比較する。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode によると、Fable 5.2 High は76,158トークンを使い、3.05ドルかかった。Xhigh と Max はストリーミング時に128,000トークンの上限まで描画を返せず、Batch API で出力の余裕を増やすとどちらも完了した。順位は発表元の目視評価による。

[関連資料 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [家族の絵を使った4人用ベルトスクロールアクション](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (投稿者 [Lex](https://notesbylex.com/))

**スケッチ、既存の試作品、操作機器の具体的な要件をコーディングエージェントに渡す。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex は Claude Code で旧作の横スクロールゲームを、12ステージと18キャラクターのアクションゲームに作り直した。画像と音声のツールで素材を用意し、家族の試遊では4台のコントローラーが動作した。

[関連資料 1](https://aidens-revenge.pages.dev/) · [関連資料 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [関連資料 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [3台の電子機器を設計から組み立てまで進める](https://www.anthropic.com/research/claude-electronics-design) (投稿者 [@Anthropic](https://www.anthropic.com/))

**回路、筐体、ファームウェアを1つのシステムとして確認する。**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ 動画を再生</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic と Diode は動作する電子機器3台を報告した。Fable 5.2 は基板配線、筐体のモデル化、ソフトウェアの作成、製造後のテストの案内を行った。

[関連資料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [関連資料 2](https://www.youtube.com/watch?v=vdYynH177h0) · [関連資料 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [Lean でフェルマーの最終定理を形式化](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (投稿者 [@Anthropic](https://www.anthropic.com/))

**証明チェッカーと途中の定理を進捗の確認に使う。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Anthropic によると、1,000の Fable 5.2 エージェントが既存の証明を30時間で形式化した。同じ構成で Opus 5.5 は18時間で26%に達した。

[関連資料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [関連資料 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [空のフォルダーから作るOS](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (投稿者 [@Anthropic](https://www.anthropic.com/))

**起動、ドライバー、ストレージ、インストールを別々に確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ 動画を再生</a>

Anthropic によると、Fable 5.2 が8日間で1,000を超えるサブエージェントを調整し、ノートPCで起動する試作OSを構築した。

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [RoboDojo の双腕操作ベンチマーク](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (投稿者 [@Anthropic](https://www.anthropic.com/))

**同じシミュレーション上の操作課題でモデルを比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ 動画を再生</a>

Anthropic によると RoboDojo のスコアは Fable 5.2 が64.9%、Fable 5.1 が27.6%だった。発表資料にはロボットのデモもある。

[関連資料 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [水が流れる噴水](https://x.com/Angaisb_/status/2119909059277238733) (投稿者 [@Angaisb_](https://x.com/Angaisb_))

**連続する水の動きからシーンのリズムを確認する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

作者は Fable 5.2 で制作した噴水のシーンを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [Higgsfield でフレーム単位のリップシンク](https://x.com/higgsfield_ai/status/2119909938969580024) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**映像を確認する前にフレーム単位で音声を合わせる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ 動画を再生</a>

Higgsfield は制作工程で Fable 5.2 を使い、口の動きを追跡して音声を各フレームに合わせたと報告した。

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [オープンワールド運転ゲームの試作](https://x.com/ericmaskfr/status/2119910195325481026) (投稿者 [@ericmaskfr](https://x.com/ericmaskfr))

**短い指示を試遊可能な一部分で検証する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ 動画を再生</a>

作者は GTA を参考にした試作品を公開し、実行に約2時間14分かかったと報告した。

元のプロンプト

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [参考画像で再現する1940年のパリ](https://x.com/higgsfield_ai/status/2119910344998912507) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**参考画像の生成とシーンのコーディングを分ける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ 動画を再生</a>

Higgsfield は自社 MCP で参考画像を用意し、Fable 5.2 で Three.js のシーンを制作した。

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable が企画し Opus が制作した短編](https://x.com/kloss_xyz/status/2119910613828980846) (投稿者 [@kloss_xyz](https://x.com/kloss_xyz))

**映像制作の企画と実装を分ける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ 動画を再生</a>

Fable 5.2 が制作指示と計画をまとめ、Opus 5.5 が Blender と Python で16秒のアニメーションを制作し、楽曲を合成した。

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [ミュージックビデオの実験](https://x.com/WesRoth/status/2119911161386934330) (投稿者 [@WesRoth](https://x.com/WesRoth))

**歌詞と生成映像をあわせて確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 で作ったミュージックビデオを公開し、歌詞についてコメントした。

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Dario Amodei の肖像画](https://x.com/Mr_Salio/status/2119911922577637543) (投稿者 [@Mr_Salio](https://x.com/Mr_Salio))

**スタイライズされた肖像と併記された参照画像を比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 が描いたとする Dario Amodei の肖像を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [推論強度 Medium の Spud Smash](https://x.com/argofowl/status/2119913148929187960) (投稿者 [@argofowl](https://x.com/argofowl))

**ゲームの試作で操作と目的を明確にする。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ 動画を再生</a>

作者は青い椅子を殴ったり頭突きしたり燃やしたりするジャガイモのキャラクターを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Fable と Opus の氷の大聖堂](https://x.com/QQTeng/status/2119913518015435103) (投稿者 [@QQTeng](https://x.com/QQTeng))

**同じシーンの生成時間と費用を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ 動画を再生</a>

作者の報告では Fable が約1時間57分で81.10ドル、Opus が約3時間11分で45.97ドルだった。

元のプロンプト

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [声道シミュレーションで歌わせる](https://x.com/banteg/status/2119914098171199996) (投稿者 [@banteg](https://x.com/banteg))

**音楽制作の入力に物理的な音声モデルを使う。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ 動画を再生</a>

作者は2つの Chimera 声道シミュレーションとボコーダーミックスを使ったカバーを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [イスタンブールを題材にした3つのボクセルテスト](https://x.com/Avenoxai/status/2119914308603953485) (投稿者 [@Avenoxai](https://x.com/Avenoxai))

**破壊シーン、動く時計、地図を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ 動画を再生</a>

作者はそれぞれ1つのプロンプトで試した結果を公開し、独自の採点基準で100、100、95.6点だったと報告した。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Remote Labor Index のプロジェクト完了率](https://x.com/ScaleAILabs/status/2119914701736075489) (投稿者 [@ScaleAILabs](https://x.com/ScaleAILabs))

**割合は対象プロジェクトの評価結果として読む。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ 動画を再生</a>

Scale Labs と CAIS によると、Fable 5.2 は評価対象の遠隔業務プロジェクトの41.3%を完了した。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [4段階の推論強度で描く氷山](https://x.com/0xRhinoX/status/2119915121698840587) (投稿者 [@0xRhinoX](https://x.com/0xRhinoX))

**推論強度を上げたときの完成度、費用、細部を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ 動画を再生</a>

作者は4段階で同じプロンプトを使った。High ではオーロラが省かれ、Ultra では光る氷と水中視点が加わった。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [79秒のアニメ短編](https://x.com/anstapnever/status/2119915123070644263) (投稿者 [@anstapnever](https://x.com/anstapnever))

**長めのアニメーションでシーンの連続性を見る。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 の制作工程による79秒のアニメーションを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Fable と Opus が描く機械の組立図](https://x.com/ivanainai/status/2119915243321397550) (投稿者 [@ivanainai](https://x.com/ivanainai))

**各モデルの部品配置を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 と Opus 5.5 が制作したラベル付きの車輪と歯車の分解図を公開した。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [らせん階段を上るロボットハンド](https://x.com/Luckyballa/status/2119915557663506720) (投稿者 [@Luckyballa](https://x.com/Luckyballa))

**シミュレーション上の障害物で変わった移動方法を検証する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 と Steel 0.1 で Wuji ハンドを指で歩かせるテストを公開した。

[関連資料 1](https://github.com/skild-ai/steel-webgpu/pull/7)

元のプロンプト

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [Blender で Tripo のメッシュをリギング](https://x.com/0xKense1/status/2119916096098582566) (投稿者 [@0xKense1](https://x.com/0xKense1))

**握り方、テクスチャー、変形を数値で確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ 動画を再生</a>

作者は Tripo のアセットを使った2つのリグを比較した。Fable は36分で2本、Opus は約21分で8本のクリップを作った。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [ダ・ヴィンチの手稿を触って学べる発明展示に](https://x.com/alexalbert__/status/2119916954337349737) (投稿者 [@alexalbert__](https://x.com/alexalbert__))

**元の図面を使って操作可能な教材を作る。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ 動画を再生</a>

Alex Albertはダ・ヴィンチの手稿の PDF を渡し、発明に触れて学べる解釈を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [Claude が操作する音楽制作環境](https://x.com/The_Alex/status/2119917226769985785) (投稿者 [@The_Alex](https://x.com/The_Alex))

**繰り返しの作曲依頼にエージェント操作のツールを使う。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 で作ったデジタルオーディオワークステーションを公開し、後に Opus がそれを開いて作曲したと説明した。

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [Raspberry Pi 5 の製品アニメーション](https://x.com/sparklabhq/status/2119917375080521921) (投稿者 [@sparklabhq](https://x.com/sparklabhq))

**製品アニメーションの課題で部品の細部を確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 で作った Raspberry Pi 5 のアニメーションを公開した。

元のプロンプト

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [イタリア北部の風景](https://x.com/Angaisb_/status/2119917807119089926) (投稿者 [@Angaisb_](https://x.com/Angaisb_))

**特定の場所を指定し、景観や雰囲気を見る。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 で制作したイタリア北部のシーンを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [ローカルの作業エージェントで作る飛び出す絵本](https://x.com/atomicagent_io/status/2119918110752846094) (投稿者 [@atomicagent_io](https://x.com/atomicagent_io))

**同じタスクでマルチエージェントと単独実行を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ 動画を再生</a>

Atomic によると、Fable がローカルの Qwen ワーカーを調整した場合は11分で2.98ドル、Fable 単独では21分で15.77ドルだった。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [復活したラバランプテスト](https://x.com/eidzoku/status/2119918134060601690) (投稿者 [@eidzoku](https://x.com/eidzoku))

**同じ視覚課題で複数のモデルを比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ 動画を再生</a>

作者はラバランプのテストを再開し、生成された結果を並べて公開した。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [Blender で精密なジェット機を制作](https://x.com/higgsfield_ai/status/2119918248955392431) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**部品数、尺、見た目を制作指示に盛り込む。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ 動画を再生</a>

Higgsfield は Fable 5.2 と自社 MCP を使い、931個の部品と24,260本のリベットを持つ Blender モデルをスクリプトで制作したと報告した。

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [数百の世界を巡るポータルの旅](https://x.com/emollick/status/2119918307457577163) (投稿者 [@emollick](https://x.com/emollick))

**別々に生成した環境をポータルでつなぐ。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ 動画を再生</a>

Ethan Mollick によると、25,000のエージェントが450を超える世界をコードで作った。試遊版とリポジトリも公開した。

[関連資料 1](https://portals-endless-worlds.netlify.app/) · [関連資料 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [Three.js で描くムンバイの市場の6カット](https://x.com/higgsfield_ai/status/2119918834841010320) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**映像の指示を長さの決まったカットに分ける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ 動画を再生</a>

Higgsfield は Three.js でレンダリングした6カット、21.5秒の市場の映像を公開した。

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [コードで作る写実的なアメリカンダイナー](https://x.com/higgsfield_ai/status/2119918838490010008) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**コードだけで作ったシーンで材質と照明を確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ 動画を再生</a>

Higgsfield はアメリカンダイナーを公開し、3Dモデリングアプリを使わずコードで制作したと説明した。

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [Blender で作ったロボットモデル](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (投稿者 [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**回転ビューで関節とシルエットを確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 と Blender で制作した小さな機械ロボットを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [Convex のモーショングラフィックス解説](https://x.com/Rasmic/status/2119919466163093768) (投稿者 [@Rasmic](https://x.com/Rasmic))

**短いアニメーションで開発者向け製品を説明する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 で制作した Convex のモーショングラフィックス解説を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [一度の指示で作ったランディングページ集](https://x.com/daradoescode/status/2119919529807466594) (投稿者 [@daradoescode](https://x.com/daradoescode))

**複数の短い指示でレイアウトと情報の優先順位を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 が制作したランディングページをまとめた映像を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [LilyPond で記譜したピアノソナタ](https://x.com/imjustnewatai/status/2119919644836347926) (投稿者 [@imjustnewatai](https://x.com/imjustnewatai))

**楽譜のソースとレンダリングした映像を対応させる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ 動画を再生</a>

作者はベートーヴェン風の楽章を依頼し、表示された音符は LilyPond のソースから来たと説明した。

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [自由な映像制作指示](https://x.com/aollivier82/status/2119920990893244510) (投稿者 [@aollivier82](https://x.com/aollivier82))

**表現の制約を設けず、モデルの創作上の選択を見る。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 にできる限り美しい映像を依頼し、出力を公開した。

元のプロンプト

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable が計画し、DeepSeek が実装し、Opus がレビュー](https://x.com/ivanfioravanti/status/2119921810267636201) (投稿者 [@ivanfioravanti](https://x.com/ivanfioravanti))

**調整、実装、レビューを別々のエージェントに任せる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable が herdr で4つの DeepSeek V4.1 Flash ワーカーを調整し、Opus 5.5 がプルリクエストをレビューする構成を示した。

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [AI Village に参加した Fable 5.2](https://x.com/aidigest_/status/2119923190411719158) (投稿者 [@aidigest_](https://x.com/aidigest_))

**エージェントの返答と実際の記憶操作を分けて確認します。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

公開ログでは、Fable が別のエージェントの要請を受けて後で記憶を更新すると答えました。関連投稿にはキャラクター診断を受ける様子もあります。

[関連資料 1](https://x.com/aidigest_/status/2119923209311260707) · [関連資料 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [Skills の有無によるフロントエンド比較](https://x.com/AdamHoltererer/status/2119924849321914653) (投稿者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**モデルは固定し、Skills の設定だけを変える。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

作者は Fable 5.2 で Skills を使った場合と使わなかった場合のフロントエンドを公開した。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [コードベースに潜むステートマシンの発見](https://x.com/kunchenguid/status/2119924895060795492) (投稿者 [@kunchenguid](https://x.com/kunchenguid))

**具体的なモジュールを調べ、変更前後の図を求める。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

作者は Firstmate リポジトリの整理例と、監査に使ったプロンプトの原文を公開した。

[関連資料 1](https://github.com/kunchenguid/lavish-axi)

元のプロンプト

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [ゲームを8時間でゼロから制作](https://x.com/felixrieseberg/status/2119925633564463609) (投稿者 [@felixrieseberg](https://x.com/felixrieseberg))

**キャッシュ済み入力、生成したアセット、実時間を記録する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ 動画を再生</a>

Anthropic のエンジニアは1回の実行でモデル、音、テクスチャーを作り、API 料金換算で約550ドルだったと報告した。

[関連資料 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [関連資料 2](https://x.com/AndrewCurran_/status/2119953960794780133)

元のプロンプト

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Fishslop の試作とトークン費用](https://x.com/theo/status/2119926277801144695) (投稿者 [@theo](https://x.com/theo))

**ゲームの出来を以前のモデルの結果と比べる。**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ 動画を再生</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

作者は76分と約42ドルのトークン費用を報告し、結果を Opus 5.5 と比較した。

[関連資料 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [アメリカンフットボールのプレイ映像](https://x.com/WesRoth/status/2119926801514529027) (投稿者 [@WesRoth](https://x.com/WesRoth))

**スポーツゲームの試作で得点表示と操作の反応を試す。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ 動画を再生</a>

作者は得点時の表示がある Fable 5.2 のアメリカンフットボールの映像を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [Higgsfield MCP を使ったオープンワールドのボス戦](https://x.com/higgsfield_ai/status/2119926932343324795) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**操作して遊ぶ部分とシネマティックな演出を分ける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ 動画を再生</a>

Higgsfield によると、Fable 5.2 と自社 MCP で、オープンワールド、三幕構成のボス戦、カットシーンを含むブラウザーゲームを作った。

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [モン・サン＝ミシェルの潮の満ち引き](https://x.com/loktar00/status/2119927152489472076) (投稿者 [@loktar00](https://x.com/loktar00))

**歴史的なミニチュアで水位の変化を試す。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ 動画を再生</a>

作者は潮の満ち引きをアニメーションにしたモン・サン＝ミシェルのミニチュアを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [Blender で見る Roblox 向けアセット](https://x.com/hiyouwhatsapp/status/2119927163264573642) (投稿者 [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**インポート前に Blender でアセットを確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ 動画を再生</a>

作者はほぼ一度の指示で作った Roblox 開発向けの Blender 成果物を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [思考過程を出力しない推論評価](https://x.com/Tim_Hua_/status/2119927284761293089) (投稿者 [@Tim_Hua_](https://x.com/Tim_Hua_))

**推論の出力条件を揃えて答えを比較する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

評価者は思考過程を出力させずに推論と知識を評価し、Fable 5.2 は GPT-6.1 Sol をわずかに下回ったと報告した。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [4つのモデルで Chrome 恐竜ゲームを再制作](https://x.com/noclipepe/status/2119927838321328577) (投稿者 [@noclipepe](https://x.com/noclipepe))

**同じゲーム課題で時間と費用を比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ 動画を再生</a>

作者は既存の T-Rex テストに Fable 5.2 を加え、Opus、Gemini、Astra の出力と並べた。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [ロボットアームでチェッカー](https://x.com/karolina_dubiel/status/2119928342115676576) (投稿者 [@karolina_dubiel](https://x.com/karolina_dubiel))

**関節位置を読み取り、駒をつかみ損ねたら再試行する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ 動画を再生</a>

作者によると、モデルは約7 mmのたわみを補正し、フィードバックをもとに失敗した操作をやり直した。

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [15秒のモーショングラフィックス](https://x.com/aziz4ai/status/2119928581405200726) (投稿者 [@aziz4ai](https://x.com/aziz4ai))

**短いコードアニメーションが消費する利用枠を測る。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ 動画を再生</a>

作者はコードで作った15秒の映像を公開し、週間枠の4%を消費したと報告した。

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [操作して遊べるエッフェル塔](https://x.com/bobyau/status/2119928812628771212) (投稿者 [@bobyau](https://x.com/bobyau))

**ランドマークのモデルが操作に反応するか試す。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ 動画を再生</a>

作者はエッフェル塔のデモを公開し、制作に25分かかったと報告した。

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [Three.js と Higgsfield で海上レースを作る](https://x.com/higgsfield_ai/status/2119928918035910668) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**混合ワークフローではゲームのロジックと映像ツールを分ける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ 動画を再生</a>

Higgsfield は大波、5人の AI ライバル、追尾ロケットが登場するレースゲームを公開した。

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [WebGL で蜂蜜の流れをリアルタイム再現](https://x.com/deedydas/status/2119930300990177509) (投稿者 [@deedydas](https://x.com/deedydas))

**ブラウザー内の物理シミュレーションで材質の動きを試す。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ 動画を再生</a>

作者は蜂蜜のリアルタイム WebGL シミュレーションと、元の短い指示を公開した。

元のプロンプト

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [実写映像にプログラムで視覚効果を追加](https://x.com/ashebytes/status/2119930763105931649) (投稿者 [@ashebytes](https://x.com/ashebytes))

**元の映像に対する効果のタイミングと位置を確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 で動くグラフィックを実写映像に重ねた視覚効果のテストを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [GTA の手配度を説明する映像](https://x.com/saimagnate/status/2119931563760632311) (投稿者 [@saimagnate](https://x.com/saimagnate))

**ゲーム映像と図を組み合わせて仕組みを説明します。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 が一度の依頼で作ったと述べています。動画はプレイ映像と図を使って GTA V と RDR2 の手配システムを比較しています。

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [コードで作るスタイライズされた MMO 世界](https://x.com/Izkimar/status/2119931740940640542) (投稿者 [@Izkimar](https://x.com/Izkimar))

**スタイライズした素材で世界全体の統一感を見る。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ 動画を再生</a>

作者は公開した MMO 世界を1日で作り、素材をすべてコードで生成したと報告した。

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [Fable と Opus の3Dシーン比較](https://x.com/dom_scholz/status/2119933150025363661) (投稿者 [@dom_scholz](https://x.com/dom_scholz))

**準備時間と出力の細部を並べて比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 と Opus 5.5 のレンダリングを並べ、Fable の実行がより速かったと報告した。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [ゲームのポーズ画面にある冗長な説明](https://x.com/AndrewPrifer/status/2119934600608915465) (投稿者 [@AndrewPrifer](https://x.com/AndrewPrifer))

**生成された画面の文言に説明の重複がないか確認する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

開発者はポーズ画面を例に、Fable 5.2 が必要以上に説明を書いたと指摘した。

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [Krea の実行環境で作るムードボード](https://x.com/lambdacalcc/status/2119934725662060663) (投稿者 [@lambdacalcc](https://x.com/lambdacalcc))

**ビジュアルの方針を決める前に複数の案を比べる。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

作者は Fable 5.2 と Krea の実行環境で作ったムードボードの出力4件を公開した。

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [職場で試遊したポータル付きシューティング](https://x.com/_sholtodouglas/status/2119935331499925557) (投稿者 [@_sholtodouglas](https://x.com/_sholtodouglas))

**複数人の試遊で生成されたゲームを評価する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ 動画を再生</a>

Anthropic のエンジニアはポータルのある対戦 FPS を公開し、職場での試遊について説明した。

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Blender の精密なハードサーフェスアセット](https://x.com/ziwenxu_/status/2119937420280168929) (投稿者 [@ziwenxu_](https://x.com/ziwenxu_))

**Blender のビューポートでトポロジーと輪郭を確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 の Blender 成果物として精密なハードサーフェスアセットを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [推論強度を変えた並行フロントエンドテスト](https://x.com/AI_masaou/status/2119937635322085640) (投稿者 [@AI_masaou](https://x.com/AI_masaou))

**簡単な指示と難しい指示を複数の推論強度で比べる。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

作者によると、簡単な出力は Fable と Opus で似ていた。大きな制作では Fable の細部が豊かになり、Medium から High に上げると時間とトークン数が大幅に増えた。

[関連資料 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [10回のプロンプトで作った小さなゲーム](https://x.com/AmirMushich/status/2119937977426338283) (投稿者 [@AmirMushich](https://x.com/AmirMushich))

**試作では反復回数と成果物のサイズを記録する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ 動画を再生</a>

作者は約3,400行のコードで220 KBのゲームを作ったと報告し、コードと映像を公開した。

[関連資料 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [JavaScript で一コマずつ描くアニメーション](https://x.com/kevin_t_ngo/status/2119938129079808282) (投稿者 [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**プログラムで各フレームを描画した映像を確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ 動画を再生</a>

作者は全フレームを JavaScript で描いたというアニメーションを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [参考映像から作る3Dアニメーション](https://x.com/KHvostikk/status/2119939061049889130) (投稿者 [@KHvostikk](https://x.com/KHvostikk))

**再構成したシーンを元の映像と比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 で映像を3Dアニメーションに変換したデモを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Fable と Opus のドット絵のたき火](https://x.com/GrilliotTodd/status/2119939651385655692) (投稿者 [@GrilliotTodd](https://x.com/GrilliotTodd))

**同じドット絵の題材で照明と輪郭を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ 動画を再生</a>

Fable 5.2 と Opus 5.5 が描いた同じ題材のたき火を並べている。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [推論強度 xHigh の Arena WebDev](https://x.com/arena/status/2119941204003770690) (投稿者 [@arena](https://x.com/arena))

**ランキング比較では使用した推論強度を確認する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena によると、Claude Fable 5.2 xHigh は Code Arena WebDev で初登場1,832点だった。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [映画予告編のタイトル文字をモデル間で比較](https://x.com/muku_sns/status/2119941490969624679) (投稿者 [@muku_sns](https://x.com/muku_sns))

**同じ段落から生まれた2つの解釈を比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ 動画を再生</a>

作者は Opus と Fable の予告編タイトルを並べた。Fable 版には赤い縁取りと黒塗りの文字が加わった。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [1つのプロンプトで試すモーションと3Dの作品集](https://x.com/Khazix0918/status/2119941585538572390) (投稿者 [@Khazix0918](https://x.com/Khazix0918))

**制作の指示をもとに調査、デザイン、レンダリングを個別に評価する。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ 動画を再生</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ 動画を再生</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ 動画を再生</a></td></tr></table>

作者は ChatGPT の周年記念映像、DeepSeek の解説、Three.js のシーン、Apple 静安の3D再現という4件の実行結果を公開した。

[関連資料 1](https://x.com/Khazix0918/article/2119941585538572390)

元のプロンプト

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [分解して学ぶ原子炉](https://x.com/konstantinsaifo/status/2119941967136379334) (投稿者 [@konstantinsaifo](https://x.com/konstantinsaifo))

**部品を取り外す操作で組み立て方を示す。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ 動画を再生</a>

作者は分解できる原子炉の Three.js モデルを依頼し、API 費用が92ドルだったと報告した。

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Blood on the Clocktower でのエージェント評価](https://x.com/dwarkesh_sp/status/2119942657812451482) (投稿者 [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**同じ正体隠匿ゲームでモデルを比較する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

評価者によると、このベンチマークで Fable 5.2 は Fable 5.1 と Opus 5.5 を上回り、GPT-6 Astra が先行した。

[関連資料 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [ポッドレース風の試作品](https://x.com/loktar00/status/2119943124965638444) (投稿者 [@loktar00](https://x.com/loktar00))

**馴染みのあるレース形式で動きや操作感を評価する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 で作ったポッドレーサー風の結果を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [10秒の Claude 下着CM](https://x.com/Masimo_Blue/status/2119943368612487285) (投稿者 [@Masimo_Blue](https://x.com/Masimo_Blue))

**大まかな製品指示でオリジナル楽曲付きの広告を試す。**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ 動画を再生</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

作者はアシッドテクノと提供された商品画像を使った10秒の宣伝映像を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [朝日の中の鳥を一筆ずつ描く](https://x.com/mgrczyk/status/2119943813028548721) (投稿者 [@mgrczyk](https://x.com/mgrczyk))

**取り消しを無効にして、一筆ごとの判断を見る。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ 動画を再生</a>

作者は描いた線を後から変更できない実行環境で、朝日の中の鳥を一筆ずつ描いた結果を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [Devin で行う長時間のグラフィックス処理](https://x.com/Da7_Tech/status/2119944847255896490) (投稿者 [@Da7_Tech](https://x.com/Da7_Tech))

**負荷の高いレンダリングでは時間と費用を記録する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ 動画を再生</a>

Cognition のアンバサダーであることを明かしている作者が Devin Max の実行結果を公開し、約3.5時間で約82ドルかかったと報告した。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [3モデルによるコード絵画の比較](https://x.com/kickingkeys/status/2119945841997672698) (投稿者 [@kickingkeys](https://x.com/kickingkeys))

**描画の動きと合成音を実行ごとに比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ 動画を再生</a>

作者は音付きのコード絵画を公開し、Fable 5.2、Fable 5.1、Gemini 4 Argon に同じプロンプトを与えたテストを説明した。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [アニメーションでたどる文字の歴史](https://x.com/rileybrown/status/2119946022767980985) (投稿者 [@rileybrown](https://x.com/rileybrown))

**年表をもとにコード生成の解説映像を構成する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ 動画を再生</a>

作者は文字の歴史を描いたアニメーションを公開し、1つのプロンプトで作ったと説明した。

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [ゲーム内の機械を試す実験場](https://x.com/techartist_/status/2119946891106394518) (投稿者 [@techartist_](https://x.com/techartist_))

**1つのシーンでギミック、物理挙動、効果を試作する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ 動画を再生</a>

作者は Three.js と Blender で4つの案を試せる実験場を制作した。

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [携帯型 Linux ゲーム機の PCB 設計](https://x.com/seveibar/status/2119947341230907453) (投稿者 [@seveibar](https://x.com/seveibar))

**同じ回路要件でモデルの設計を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ 動画を再生</a>

tscircuit の作者は Astra 6 High と Fable 5.2 High で携帯型 Linux ゲーム機を設計したテストを示した。

元のプロンプト

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [ボクセルで作る湖](https://x.com/Angaisb_/status/2119947748690841841) (投稿者 [@Angaisb_](https://x.com/Angaisb_))

**小規模な環境を題材に構図を検証する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 で制作したボクセルの湖を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [Arena のインタラクティブな生成例17件](https://x.com/arena/status/2119948067449536733) (投稿者 [@arena](https://x.com/arena))

**評価タスクを決める前に複数の種類の出力を見る。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ 動画を再生</a>

Arena は3D世界、ゲーム、画面、データ可視化、コードアニメーションなど17件の生成例を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [友好的なドラゴンと飛ぶ](https://x.com/chetanankola/status/2119951015407738913) (投稿者 [@chetanankola](https://x.com/chetanankola))

**ループする飛行でカメラと動きを検証する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ 動画を再生</a>

作者は Three.js と Blender で作ったドラゴンのシーンを公開し、Fable 5.2 による改善点を説明した。

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Fable と Opus のゼリーのシャチ](https://x.com/vib3coded/status/2119951060752375827) (投稿者 [@vib3coded](https://x.com/vib3coded))

**同じ題材で表面の質感と動きを比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 と Opus 5.5 で作ったゼリーのシャチを並べて公開した。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [自由課題による映像品質テスト](https://x.com/suna_gaku/status/2119952985933697063) (投稿者 [@suna_gaku](https://x.com/suna_gaku))

**広い指示を与え、モデルが何を選ぶかを見る。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ 動画を再生</a>

作者はモデルに得意な映像表現を見せるよう依頼し、結果を公開した。

元のプロンプト

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [地中海をテーマにした宇宙居住施設](https://x.com/MaxXWilliamson/status/2119953172634677533) (投稿者 [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**短い設計指示と既存のプロジェクト用ツールを組み合わせる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ 動画を再生</a>

作者は以前の宇宙居住施設で使ったツールを渡し、地中海風の施設を依頼した。

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [AA-3D のインタラクティブ体験ベンチマーク](https://x.com/ArtificialAnlys/status/2119953570430881946) (投稿者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Elo を読む際は不確実性の区間も確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ 動画を再生</a>

Artificial Analysis によると、公開時のインタラクティブ3D評価で Fable 5.2 Max は Elo 1,271 を記録した。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [骸骨キャラクターのタイムチャレンジ](https://x.com/WesRoth/status/2119953913160093817) (投稿者 [@WesRoth](https://x.com/WesRoth))

**試遊できるプロトタイプを画面内タイマーで評価する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 に一度の指示で作らせた、骸骨キャラクターとカウントダウンのあるゲームを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Fable と Astra のドット絵比較](https://x.com/Angaisb_/status/2119955179915137294) (投稿者 [@Angaisb_](https://x.com/Angaisb_))

**出力サイズを揃えて形や細部を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ 動画を再生</a>

元投稿では GPT-6 Astra と Fable 5.2 のドット絵を並べている。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [モーションデザインのポートフォリオ映像](https://x.com/Leviwoyun/status/2119955625820258308) (投稿者 [@Leviwoyun](https://x.com/Leviwoyun))

**自由度の高い作品集の指示に尺の制約を加える。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ 動画を再生</a>

作者は音楽付きのモーションデザイン映像を公開し、制作に24分かかったと報告した。

元のプロンプト

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [2つのモデルによるガラスのプールのレンダリング](https://x.com/MrTacticalX/status/2119955647542542439) (投稿者 [@MrTacticalX](https://x.com/MrTacticalX))

**照明の品質を処理時間や費用とあわせて比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ 動画を再生</a>

作者の報告では、Fable は90分で57.87ドル、Opus は68分で14.39ドルだった。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [TS-Bench のツール呼び出し精度](https://x.com/gosrum/status/2119956559031927079) (投稿者 [@gosrum](https://x.com/gosrum))

**ツール呼び出しのエラーとトークン使用量を別々に記録する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

評価者によると、Fable 5.2 のツール呼び出しエラーは0件で、簡単なタスクでは Claude のモデル間に差が出にくかった。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [ミニチュアのマチュピチュ](https://x.com/loktar00/status/2119958719362666708) (投稿者 [@loktar00](https://x.com/loktar00))

**縮小したシーンで雰囲気と細部を確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ 動画を再生</a>

公開されたマチュピチュのデモには、ボリュームフォグと小さなアルパカが登場する。

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [専門分野別の GDPx](https://x.com/SemiAnalysis_/status/2119961447199289640) (投稿者 [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**総合スコアと各分野の結果をあわせて読む。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

評価の発表元は総合スコア16.4%を報告し、チップ設計やソフトウェア工学などの内訳も示した。

[関連資料 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [関連資料 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [関連資料 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [ペイントアプリで人物画を描く](https://x.com/The_Alex/status/2119964472559489229) (投稿者 [@The_Alex](https://x.com/The_Alex))

**参照用のサムネイルを手掛かりに似顔絵を描かせます。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ 動画を再生</a>

作者は Fable 5.2 にペイントアプリを開いて似顔絵を描くよう依頼しました。動画には輪郭から仕上げまでが映っています。

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [推論強度 Low の VulcanBench Frontier v4](https://x.com/morganlinton/status/2119966067527467215) (投稿者 [@morganlinton](https://x.com/morganlinton))

**世代の異なるモデルを同じ推論強度で比較する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

評価の作者によると、Low では1タスクあたり Fable 5.2 が約5分、5.1 が約26分かかった。

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [怪物側で遊ぶバックルーム](https://x.com/LexnLin/status/2119966127149429093) (投稿者 [@LexnLin](https://x.com/LexnLin))

**プレイヤーの目的を変えてゲーム案を検証する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ 動画を再生</a>

プレイヤーは怪物を操作して人を捕まえる。作者はプレイ映像と試遊リンクを公開した。

[関連資料 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [Blender で Bugatti Tourbillon を制作](https://x.com/xikhar/status/2119966147328299284) (投稿者 [@xikhar](https://x.com/xikhar))

**外装と内装の指定に参考画像を使う。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ 動画を再生</a>

作者によると、プロンプトと参考画像で Bugatti Tourbillon の内装までモデル化し、映画風の映像に仕上げた。

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [2つのモデルで作るコンピューター映像](https://x.com/daradoescode/status/2119966154391183522) (投稿者 [@daradoescode](https://x.com/daradoescode))

**共同制作では各モデルの担当を記録する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ 動画を再生</a>

作者が公開した映像は Fable 5.2 で制作され、Opus 5.5 も大きく貢献した。

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [Megakernel を題材にしたミュージックビデオ](https://x.com/elliotarledge/status/2119968762069934415) (投稿者 [@elliotarledge](https://x.com/elliotarledge))

**技術的な概念を映像の題材にする。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ 動画を再生</a>

作者は推論強度 High の Fable 5.2 に Megakernel のミュージックビデオを依頼し、映像を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [参考写真を使ったスタジオツアー](https://x.com/rpnickson/status/2119969928304357507) (投稿者 [@rpnickson](https://x.com/rpnickson))

**実際の写真を使って場面を再現する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ 動画を再生</a>

作者はスタジオの写真を渡して似た映像の指示を調整し、実行に約2時間かかったと報告した。

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [コードで作る1990年代風のおもちゃCM](https://x.com/kevin_t_ngo/status/2119972124211454139) (投稿者 [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**アニメーションのスクリプト作成とレンダリングを分ける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ 動画を再生</a>

作者によると、レトロなおもちゃのCMを Python で動かし、Blender でレンダリングした。

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Three.js の三人称ゲームシーン](https://x.com/bijanbowen/status/2119972220739187182) (投稿者 [@bijanbowen](https://x.com/bijanbowen))

**プレイ映像でキャラクターの動きと背景を確認する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

作者は配信で、三人称視点のキャラクターが屋外を移動する Three.js の成果物を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [既存レンダラーから作る Bryceball](https://x.com/pleometric/status/2119973274402668852) (投稿者 [@pleometric](https://x.com/pleometric))

**レンダリングエンジンをゲームの土台として再利用する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ 動画を再生</a>

作者は関連投稿で紹介したレンダラーを、実際に遊べる Bryceball に作り替えた。

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [Fable で編集した映像を再編集](https://x.com/rileybrown/status/2119973951027724385) (投稿者 [@rileybrown](https://x.com/rileybrown))

**前回の編集作品を次の映像の素材にする。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ 動画を再生</a>

作者は以前にも同じモデルで編集した映像を題材に、Fable 5.2 で仕上げた作品を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [映画風にたどる科学史](https://x.com/DeryaTR_/status/2119974354260013293) (投稿者 [@DeryaTR_](https://x.com/DeryaTR_))

**年表を軸に3Dシーケンスを構成する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ 動画を再生</a>

作者は科学の黎明期から想像上の未来までを映画風に描くよう依頼し、出来上がった映像を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [ダ・ヴィンチの飛行機械を3D化](https://x.com/higgsfield_ai/status/2119975721909301684) (投稿者 [@higgsfield_ai](https://x.com/higgsfield_ai))

**歴史的な設計をモデル化してから変更を試す。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ 動画を再生</a>

Higgsfield はダ・ヴィンチの飛行機械の3D版を公開し、物理テストと再設計について説明した。

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [設計要件に沿った PCB 配線](https://x.com/cmonkey/status/2119975852977029365) (投稿者 [@cmonkey](https://x.com/cmonkey))

**基板を製造する前に配線結果を確認する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

作者は基板レイアウトについてのやり取りに続けて、Fable 5.2 の PCB 配線結果を公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [異なる実行環境で同じプロンプトを試す](https://x.com/loktar00/status/2119980613369319706) (投稿者 [@loktar00](https://x.com/loktar00))

**モデルを比べる際は実行環境の違いも記録する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ 動画を再生</a>

作者は DeepSeek と Fable 5.2 を別々の実行環境で動かし、同じプロンプトの結果を並べた。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [コードで描くゴジラ](https://x.com/chetaslua/status/2119981510199808368) (投稿者 [@chetaslua](https://x.com/chetaslua))

**ベクター風の形と動きで画像を再構成する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ 動画を再生</a>

作者はゴジラの投稿を題材に、コードで描いた絵と短いアニメーションを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [3Dプリント用の携帯扇風機](https://x.com/davelee/status/2119981787325579398) (投稿者 [@davelee](https://x.com/davelee))

**実物の試作品で組み立て具合を確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ 動画を再生</a>

作者は子どもたちと一緒に携帯扇風機を設計し、印刷前にモデルを公開した。

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [Opus と比べるプラグインの不具合調査](https://x.com/oaranda/status/2119982729747919096) (投稿者 [@oaranda](https://x.com/oaranda))

**相互に回帰テストをかけて修正を比較する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

作者が注記を加えた発表記事の抜粋。

両モデルが同じ6件の不具合を発見した。Opus は相互テストをすべて通過し、Fable は1件失敗したが、ダッシュボードの別の問題も見つけた。

元のプロンプト

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [イスタンブールの3D再現](https://x.com/petergostev/status/2119877733488394520) (投稿者 [@petergostev](https://x.com/petergostev))

**都市規模のシーンを遠景と近景の両方から確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ 動画を再生</a>

Peter Gostev は Fable 5.2 Max で作ったイスタンブールの3D出力を公開し、詳しい評価へのリンクを添えた。

[関連資料 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [画面の映像まで動く Blender のスタジオ映像](https://x.com/rileybrown/status/2119902109709537708) (投稿者 [@rileybrown](https://x.com/rileybrown))

**ディスプレイ、照明、カメラを同じ3Dシーンで動かす。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ 動画を再生</a>

作者によると、カメラは13カットあり、ノートPCの画面で専用ウェブページが再生され、音声には ElevenLabs を使った。レンダリングには RunPod の GPU を利用した。

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [弱結合領域でのブラックホールの急変](https://hexagonmath.org/2611.00175v1) (投稿者 [@Anthropic](https://www.anthropic.com/))

**元の理論設定に戻って未完の計算を検証する。**

Anthropic によると、Fable 5.2 は長く未完だった計算を終え、弱結合領域で急激な変化を発見した。導出はプレプリントに掲載されている。

[関連資料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [モジュラー・ブートストラップの境界](https://hexagonmath.org/2611.00174v1) (投稿者 [@Anthropic](https://www.anthropic.com/))

**解析的な境界を主張する際は導出も公開する。**

Anthropic によると、Fable 5.2 は単純化した量子重力の設定における、スピンを考えないモジュラー・ブートストラップ手法の正確な限界を求めた。

[関連資料 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Vercel AI Gateway でモデルのフォールバック順を設定](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (投稿者 [Vercel](https://vercel.com/))

**分類器が拒否したリクエストに備えてゲートウェイで切り替え順を指定する。**

Vercel の AI SDK サンプルは anthropic/claude-fable-5.2 を呼び出し、Opus 5.5、Sonnet 5.5 の順でフォールバックを設定する。ガイドではゲートウェイのデータ保持要件も説明している。

[関連資料 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [入れ子のサブエージェントとレビュー予算](https://news.ycombinator.com/item?id=50430925) (投稿者 [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**再委任を追跡し、プロンプトの外でレビューの予算上限を設定する。**

作者は8万行のコードレビューでサブエージェントを最大4つと指定した。実際には入れ子で6つ以上が動き、20分足らずで5時間分の利用枠を使い切ったと報告した。

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [LCARS デザインから HTML への変換比較](https://news.ycombinator.com/item?id=50430962) (投稿者 [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**曲線、アイコンの再現度、アニメーション、ナビゲーションを別々の受け入れ基準にする。**

作者は同じ『スタートレック』風のデザインで Fable 5.2 と Opus 5.5 を比較した。曲線と一部のアイコンは Fable、動きは Opus を好み、Fable の SVG のちらつきが気になったという。依頼範囲は最初のページだけだった。

[関連資料 1](https://html.non.io/lcars-fable-5.2/) · [関連資料 2](https://html.non.io/lcars-opus-5.5/) · [関連資料 3](https://news.ycombinator.com/item?id=50431231) · [関連資料 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [Quantum ESPRESSO のGPU最適化](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (投稿者 [Discovered Materials](https://discoveredmaterials.com/))

**科学計算コードを最適化する際は参照結果と代表的な非公開テストを用意する。**

Discovered Materials によると、同じ GPU でのフォノン評価13件の高速化倍率は幾何平均で36倍、混成汎関数の計算では約9倍だった。公開パッチは正確性と性能のテストに基づく。

[関連資料 1](https://github.com/discovered-materials/dm_qe) · [関連資料 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [推論強度別の Artificial Analysis Intelligence Index](https://artificialanalysis.ai/models/claude-fable-5-2) (投稿者 [Artificial Analysis](https://artificialanalysis.ai/))

**選んだ推論強度のスコア、1件あたりの費用、待ち時間をあわせて読む。**

参照された既定フォールバックの Max 結果では指数が65、1タスクあたり26.54ドルと46.4分だった。数値はこのベンチマークでの測定値。

[関連資料 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [High 設定の変更レビューで出た誤検出](https://news.ycombinator.com/item?id=50431810) (投稿者 [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**モデルが指摘した問題は対応前にコードと照合する。**

開発者によると、Fable 5.2 High は変更レビューで存在しない問題を2件指摘した。開発者はコードの知識をもとに誤りを見抜いた。

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [日常的なコーディング課題30件](https://news.ycombinator.com/item?id=50432483) (投稿者 [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**同じコーディング課題で経過時間と成功件数を測る。**

作者によると、Fable 5.2 と Opus 5.5 は30件中26件、Fable 5.1 は25件を解いた。Fable 5.2 の時間は5.1の0.62倍で、安全機構による停止は報告されなかった。

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [無人島のスクリーンセーバー](https://news.ycombinator.com/item?id=50432836) (投稿者 [@nzach](https://news.ycombinator.com/user?id=nzach))

**実際に操作できるページでモデルが作ったスクリーンセーバーを確認する。**

Show HN の作者は Stranded with Claude というブラウザー上の島のシーンを公開した。成果物は操作できるキャンバスになっている。

[関連資料 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [推論強度 High のブラウザーゲーム3件](https://senko.net/vibecode-bench/) (投稿者 [Senko Rašić](https://senko.net/))

**ゲーム評価では遊び方と見た目の再現度を別々に比べる。**

Senko Rašić は Claude Code の Fable 5.2 で RTS、ボクセル、飛行シミュレーターの課題を試した。全マップを探索できる飛行船などが加わった一方、グラフィックスの一部は劣ると評価した。

[関連資料 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [章ごとに作る書評ポッドキャストの台本](https://news.ycombinator.com/item?id=50434156) (投稿者 [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**同じポッドキャストの課題で台本の長さを比較する。**

作者は2人の書評者の会話を章ごとに生成した。Fable 版は約2.5ページ、Opus 5.5 版は約4.5ページだったと報告し、両方の例をリンクした。

[関連資料 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [関連資料 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [本番サービスを Rust に移行](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (投稿者 [@Anthropic](https://www.anthropic.com/))

**移行の前後で起動性能を測る。**

Anthropic は、公開前の Fable 5.2 で動くエージェントが本番の Python サービスを Rust で書き直し、起動時間が約26分の1になったと報告した。

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [GitHub Copilot で Fable 5.2 を選ぶ](https://x.com/github/status/2119926269982961833) (投稿者 [@github](https://x.com/github))

**モデルを選ぶ前に組織のポリシーを有効にします。**

GitHub は Copilot クライアントのモデル選択画面と、Business・Enterprise アカウントで必要な管理者設定を説明しています。

[関連資料 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [HTML 100ページのデザインチャレンジ](https://x.com/MiaAI_lab/status/2119930229661503893) (投稿者 [@MiaAI_lab](https://x.com/MiaAI_lab))

**見た目に加え、完成して動作するファイル数を数える。**

作者は異なるデザイン100件を依頼し、76件のファイルとプロンプトを公開した。Fable の利用上限に達したという。

[関連資料 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [関連資料 2](https://mia-ai.net/lab/experiments/100-htmls) · [関連資料 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [関連資料 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [関連資料 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [関連資料 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [関連資料 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [関連資料 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [関連資料 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [関連資料 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [関連資料 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [関連資料 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [関連資料 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [関連資料 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [コンパイラ作業での要件のずれ](https://x.com/sameQCU/status/2119939304864800971) (投稿者 [@sameQCU](https://x.com/sameQCU))

**エージェントが説明した要件を入力と照合する。**

開発者は、Fable 5.2 と以前の Opus モデルが受け取った要件を誤って説明したコンパイラ作業について報告した。

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [長時間の Fable タスクを Opus で追う](https://x.com/marouane53/status/2119950129767858262) (投稿者 [@marouane53](https://x.com/marouane53))

**別のセッションで長いタスクの進捗を追います。**

作者によると、Fable の一部のタスクは更新が少ないまま2時間以上続きました。別スレッドの Opus 5.5 に進捗や判断を説明させました。

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [新たな視点でコードを再レビュー](https://x.com/doodlestein/status/2119958895158292786) (投稿者 [@doodlestein](https://x.com/doodlestein))

**新規ファイルと変更したファイルを別工程で見直す。**

作者は実装後の不具合を探して直すために使った、2つの追加プロンプトを原文で公開した。

元のプロンプト

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

元のプロンプト

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [機能設計のレビューで助言がずれる](https://news.ycombinator.com/item?id=50434214) (投稿者 [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**現行設計を確認リストにして、エージェントの追加提案を検証する。**

作者は機能設計をレビューする際にモデルを比較し、Opus 5.5 を好んだ。その後の Fable 5.2 の診断では、設計にすでに取り入れていた案が提案された。

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [DX Ball 風のブロック崩し比較](https://news.ycombinator.com/item?id=50434424) (投稿者 [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**再現課題ではゲームの仕組みと操作感をそれぞれ比較する。**

作者は別々に作った Fable 5.2 版と Opus 5.5 版へのリンクを共有した。Fable は元のゲームの仕組みを一部変え、作者は Opus 版の操作感を好んだ。

[関連資料 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [関連資料 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [3Dアプリの改善を試す](https://news.ycombinator.com/item?id=50434433) (投稿者 [@user43928](https://news.ycombinator.com/user?id=user43928))

**同じ改善課題で目に見える変化と予算の消費を比較する。**

作者はゲーム以外の3Dアプリの改善を Fable 5.2 に依頼した。Opus 5.5 との差は小さく、その夜に Fable の利用枠を25%消費したという。

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [3つのモデルが作るネコとネズミのゲーム](https://news.ycombinator.com/item?id=50434508) (投稿者 [@simonw](https://news.ycombinator.com/user?id=simonw))

**同じゲームプロンプトを使って各モデルの試遊版を確認する。**

Simon Willison は Fable 5.2 Extra、Opus 5.5 Extra、GPT-6 Extra High が作ったモバイル向け Three.js ゲームを公開した。Fable の実行は約40分だったという。

[関連資料 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [関連資料 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [関連資料 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

元のプロンプト

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [AIBenchy の推論強度 High における費用とスコア](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (投稿者 [AIBenchy](https://aibenchy.com/))

**同じ推論強度のラベルでスコア、総費用、応答時間を比較する。**

AIBenchy の発表では、Fable 5.2 High と Opus 5.5 High のスコアは8.7対9.4、総費用は5.083対2.133ドル、平均応答時間は14.73対27.55秒だった。

[関連資料 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [Fable 5.2 のエージェント環境を調整する](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (投稿者 [@Anthropic](https://www.anthropic.com/))

**推論強度を再検証し、長いタスクの進捗報告を決めます。**

Anthropic のガイドは推論強度、完了条件、承認、進捗報告、サブエージェントの上限を指示例とともに説明しています。

[関連資料 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="case-469"></a>
### Case 469: [アニメーション付きキャラクターのプレビューアプリ](https://x.com/seiiiiiiiiiiru/status/2121390458572333253) (投稿者 [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**繰り返し行う素材の確認作業を画面上の操作にまとめるよう、Fable に依頼する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/ce514e99465c257220ee9bf7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/776670eda35fbabbf1c63663.jpg" alt="Case 469 · 1" width="760"><br>▶ 動画を再生</a>

制作者によると、助言役として加えた Fable 5.2 が、効率の悪かった作業手順をアプリにまとめた。録画には、3D キャラクターのモーションプリセット、背景設定、GLB と背景透過 PNG の書き出し操作が映っている。

Type: Demo | Date: 2026-11-13

---

<a id="case-470"></a>
### Case 470: [ツールなしで生成した QR コードを検証](https://x.com/AdamHoltererer/status/2121376853474578625) (投稿者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**生成された QR コードを読み取ってから、試行の成否を判断する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d3833f006038158569c9816d.png" alt="Case 470 · 1" width="760">

Adam Holter は Fable 5.2、Astra、Sol による QR コードの実演として紹介し、ツールは使わなかったと述べている。添付画像をローカル環境で読み取ると、MADE WITHOUT TOOLS という文字列が得られた。

Type: Evaluation | Date: 2026-11-13

---

<a id="case-471"></a>
### Case 471: [Tripo を使った Unity のゾンビゲーム](https://x.com/fe_yukichi/status/2121375714192814554) (投稿者 [@fe_yukichi](https://x.com/fe_yukichi))

**共通の素材制作工程を使い、操作可能なキャラクターを揃える。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/055f505803b769bb8b24a54e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0fa0715e64f91ab69725599e.jpg" alt="Case 471 · 1" width="760"><br>▶ 動画を再生</a>

制作者は Tripo との提携を明記しており、Fable 5.2 を使って制作した Unity ゲーム向けに、Tripo Agentic Canvas でプレイヤーキャラクター 8 体とゾンビ 16 種を作ったと述べている。動画にはキャラクター選択とプレイの様子が映っており、デスクトップ向けブラウザー版も公開されている。

[関連資料 1](https://tsukiyo-zombie.pages.dev/)

Type: Demo | Date: 2026-11-13

---

<a id="case-472"></a>
### Case 472: [MS Paint で描く雪の街並み](https://www.reddit.com/r/ClaudeAI/comments/1xvghd1/fable_52_painting_in_ms_paint/) (投稿者 [u/wollymonjac](https://www.reddit.com/user/wollymonjac/))

**長時間の作業でマウスを直接操作する様子を画面録画で確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/10ad84001f4c682c5343846c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e7af823e10ef2135adec2154.jpg" alt="Case 472 · 1" width="760"><br>▶ 動画を再生</a>

Reddit の制作者によると、Fable 5.2 は約 2 時間半かけ、マウスを操作して MS Paint で雪の街並みを描いた。関連する X の転載投稿には、同じ場面を収めた録画がある。

[関連資料 1](https://x.com/i/status/2121373793599869213)

Type: Demo | Date: 2026-11-13

---

<a id="case-473"></a>
### Case 473: [Wojak-Bench でつながらなかった電源コード](https://x.com/lukaspet/status/2121371593943466167) (投稿者 [@lukaspet](https://x.com/lukaspet))

**生成された 3D モデルの接続部を一つずつ参照図と照合する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e509db79b2e79fcc2d6beda1.jpg" alt="Case 473 · 1" width="760">

投稿者によると、この Wojak-Bench の課題で Fable 5.2 は電源コードをコンセントにつなげられなかった。元の投稿では、3D の制作結果を撮影した写真と参照図が並べられている。

Type: Limit | Date: 2026-11-13

---

<a id="case-474"></a>
### Case 474: [リズムゲーム向けのピアノ曲](https://x.com/DJ_HYSNS/status/2121367353237942287) (投稿者 [@DJ_HYSNS](https://x.com/DJ_HYSNS))

**モデルに作曲を依頼する際は、演奏のしやすさと制作工程をどこまで制御できるかを確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d016f48687e0c8e6cf810812.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/9faa77e2e9ba2ec99be995a7.jpg" alt="Case 474 · 1" width="760"><br>▶ 動画を再生</a>

投稿者はリズムゲームの音楽を依頼したが、モデルによる VST 音色の選択やミックスが難しかったと述べ、ピアノ独奏に切り替えた。動画には完成したピアノロールが映っている。投稿者によると、曲の難易度は人が演奏できるようにするという指定の範囲を超えていた。

Type: Evaluation | Date: 2026-11-13

---

<a id="case-475"></a>
### Case 475: [Picnic のトークン回収フローを再設計](https://x.com/joaoavf/status/2121366491321057717) (投稿者 [@joaoavf](https://x.com/joaoavf))

**画面のモックアップを使い、未対応トークンの回収時に生じる画面の状態を比較する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/551612796f4150a43b190ee3.jpg" alt="Case 475 · 1" width="760">

投稿者によると、Fable 5.2 に 1、2 回指示を出すと、Picnic が対応していないトークンを回収するための新しいデザインができた。添付画像には、提案された手順の複数の画面が示されている。

Type: Demo | Date: 2026-11-13

---

<a id="case-476"></a>
### Case 476: [生成した素材をアニメのオープニング映像に編集](https://x.com/aimikoda/status/2121362621274177726) (投稿者 [@aimikoda](https://x.com/aimikoda))

**素材動画と音楽を渡し、拍に合わせてカットを切り替えるよう Fable に具体的に指示する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e3ab28061669d84818042ee0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/cb65344e413d2bd340406d59.jpg" alt="Case 476 · 1" width="760"><br>▶ 動画を再生</a>

制作者は MiniMax H3 の映像素材と Suno v6 の楽曲を組み合わせ、Fable 5.2 Medium で編集した。公開された映像には、動くピクセルアートのキャラクターやトランジションがある。実際に使われた Fable の編集プロンプトも掲載されている。

元のプロンプト

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
### Case 477: [3 つのツールを使ったキャラクターアニメーション](https://x.com/ingi_erlingsson/status/2121361947446677797) (投稿者 [@ingi_erlingsson](https://x.com/ingi_erlingsson))

**元の GIF と、Fable と ComfyUI を経たアニメーションを見比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/69a3410b7b2dcdb14ee6c5d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/391924750cd0641254cb114f.jpg" alt="Case 477 · 1" width="760"><br>▶ 動画を再生</a>

投稿者は GPT Image 2.6 の GIF を入力に使い、その後に Fable 5.2 と ComfyUI を使ったとしている。添付動画では、視点が回転する中でキャラクターの頭部が変化していく。

Type: Demo | Date: 2026-11-13

---

<a id="case-478"></a>
### Case 478: [Blender スクリプトで都市の予告編をレンダリング](https://x.com/hanghuang_/status/2121361932456427644) (投稿者 [@hanghuang_](https://x.com/hanghuang_))

**都市の予告編をシーン、キャラクター、車両、レンダリングの作業に分ける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0e5170c057eecd328b178fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d10c5d322edba010282a60d0.jpg" alt="Case 478 · 1" width="760"><br>▶ 動画を再生</a>

制作者によると、Fable 5.2 がゲーム風の予告編を企画し、街、キャラクター、車を作る Blender コードを書いた。制作者は、借りた GPU 7 基で最終映像を 4K レンダリングしたと述べている。公開動画では完成したカットを確認できる。

Type: Demo | Date: 2026-11-13

---

<a id="case-479"></a>
### Case 479: [JavaScript で描く夜景](https://x.com/kloss_xyz/status/2121356668311384487) (投稿者 [@kloss_xyz](https://x.com/kloss_xyz))

**コードで生成したイラストを評価するときは、複数の完成画像を見比べる。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/6e9d554b17822715f07d3be8.jpg" alt="Case 479 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/f57db49bb8213cc6ca4bcafe.jpg" alt="Case 479 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/2933b30de09501dbbb7e1505.jpg" alt="Case 479 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/490e5952694322b7963be8e2.jpg" alt="Case 479 · 4" width="450"></td></tr></table>

投稿者は、公開した 4 枚のイラストを Fable 5.2 が JavaScript で描いたとしている。添付画像にはそれぞれ異なるスタイルの夜景があり、出力を比較できる。

Type: Demo | Date: 2026-11-13

---

<a id="case-480"></a>
### Case 480: [CAD モデルを製図図面に変換](https://x.com/MecAgent/status/2121352868490100787) (投稿者 [@MecAgent](https://x.com/MecAgent))

**投影図、寸法、注記を元の CAD モデルと照合する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/5ce59334e405a279e1008bf0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/780dc65cb1b04f7a75e27ace.jpg" alt="Case 480 · 1" width="760"><br>▶ 動画を再生</a>

MecAgent は自社のデモで、複数の投影図と注記を含む図面を公開し、変換には Fable 5.2 を使ったとしている。動画には生成された図面が映っている。寸法の正確さを確かめるには、元の CAD ファイルとの照合が必要になる。

Type: Demo | Date: 2026-11-13

---

<a id="case-481"></a>
### Case 481: [Plotly のデータ分析試験で 43 問に正解](https://plotly.com/blog/gemini-4-hydrogen-plotly-data-analytics-bench/) (投稿者 [Plotly](https://plotly.com/))

**同じ分析評価環境で正答率と 1 回あたりの実行コストを比較する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/50882a17db12bede9165a92d.webp" alt="Case 481 · 1" width="760">

Plotly の報告によると、Fable 5.2 は、隠れたパターンを見つける問題 5 問を含む全 43 問に正解した 4 モデルのうちの一つだった。発表元は、各モデルを 1 回だけ実行した結果は単一のサンプルだと注意している。グラフには評価でのコストと正答率が示されている。

[関連資料 1](https://news.ycombinator.com/item?id=50485733)

Type: Benchmark | Date: 2026-11-12

---

<a id="case-482"></a>
### Case 482: [ウェブサイトで SGI Indy を再現](https://news.ycombinator.com/item?id=50476597) (投稿者 [@gdubs](https://news.ycombinator.com/user?id=gdubs))

**操作できる再現サイトを通じて、実物のワークステーションをウェブ化する方法を探る。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/74b80686867b920881164246.jpg" alt="Case 482 · 1" width="760">

Gregory Wieber は、Fable 5.2 を使って自身のサイトを 1990 年代の Silicon Graphics Indy として作り直したという。公開デモには、ログイン機能付きの 3D ワークステーション、3D ファイルシステム、ゲーム Soft Break が用意されている。

[関連資料 1](https://gregorywieber.com/indy/)

Type: Demo | Date: 2026-11-13

---

<a id="case-483"></a>
### Case 483: [Issue と worktree で複数のエージェントを調整](https://news.ycombinator.com/item?id=50493545) (投稿者 [@nickalaso](https://news.ycombinator.com/user?id=nickalaso))

**Issue で担当を割り当て、worktree とプルリクエストで変更を分離する。**

投稿者によると、Fable 5.2 を統括役、Opus を下位の調整役に設定し、独自の MCP サーバーで複数の提供元の作業エージェントを起動している。GitHub Issues で作業を追跡し、worktree とプルリクエストで変更の競合を防いでいるという。

Type: Integration | Date: 2026-11-14

---

<a id="case-484"></a>
### Case 484: [バックグラウンド処理で引用文献を確認](https://x.com/tukiyomiiori/status/2121368478364192930) (投稿者 [@tukiyomiiori](https://x.com/tukiyomiiori))

**引用の確認を作業エージェントに任せ、メインセッションが再開するタイミングを調べる。**

投稿者は Fable 5.2 にサブエージェントとバックグラウンドスクリプトを使って引用論文を確認させたという。処理中は Claude Code のメインセッションが休止し、作業エージェントやスクリプトが停止すると再開したと報告している。

Type: Integration | Date: 2026-11-13

---

<a id="case-485"></a>
### Case 485: [往復の貨物輸送価格モデルをデバッグ](https://x.com/allTheYud/status/2121360145921998877) (投稿者 [@allTheYud](https://x.com/allTheYud))

**モデルが復路の限界費用を正しく配分できているか確認する。**

投稿者によると、往復の貨物輸送シミュレーションで Fable 5.2 は、船舶が戻る必要があるのに、一方の区間に往復分の燃料費を計上し、もう一方には限界費用だけを計上した。この種の間違いを解消するには、デバッグを繰り返す必要があったという。

Type: Limit | Date: 2026-11-13

---

<a id="case-486"></a>
### Case 486: [Edge0 の推論環境を Mac に対応させる](https://news.ycombinator.com/item?id=50482710) (投稿者 [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen))

**プラットフォームに合わせた変更を依頼し、対象マシンで推論をテストする。**

Edge0-145B の議論で、あるコメント投稿者は Fable 5.2 に Mac 対応版を依頼し、数点の調整を加えたと述べている。自身の環境では M5 Max と NVFP4 を使い、毎秒約 50 トークンで推論できたという。

[関連資料 1](https://news.ycombinator.com/item?id=50475713)

Type: Integration | Date: 2026-11-13

---

<a id="case-487"></a>
### Case 487: [高密度なプリント基板のレイアウトをレビュー](https://news.ycombinator.com/item?id=50478759) (投稿者 [@0_____0](https://news.ycombinator.com/user?id=0_____0))

**基板に求められる性能を基準に、部品の選定と配置を確認する。**

Hacker News のコメント投稿者は、複数の基板の部品配置と配線に Fable 5.2 を試した。高密度なレイアウトは当初うまくいきそうに見えたものの、要件を満たすには配置を大幅に変え、回路図の大半を手で描き直す必要があったという。

Type: Limit | Date: 2026-11-13

---

<a id="case-488"></a>
### Case 488: [有料公開の新聞記事を引用元までたどる](https://news.ycombinator.com/item?id=50478191) (投稿者 [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff))

**原文を確認できるまでは、発言者の推定を暫定情報として扱う。**

Hacker News のコメント投稿者は、言語学のメーリングリストを手がかりに、ある帰属の根拠を 1985 年の Dallas Morning News の記事までたどった。Fable 5.2 は全文を開けず、候補となる記者と文脈を挙げたという。帰属の特定には原文の確認が必要だ。

[関連資料 1](https://listserv.linguistlist.org/pipermail/ads-l/2003-September/033575.html)

Type: Limit | Date: 2026-11-13

---

<a id="case-489"></a>
### Case 489: [Fable で計画を立て、Opus の変更をレビュー](https://news.ycombinator.com/item?id=50477200) (投稿者 [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology))

**文書化した計画を承認して実装作業を分担し、CI とステージング環境で変更を検証する。**

投稿者は大規模なコードベースで使ったという手順を紹介している。Fable 5.2 が計画を立て、Opus 5.5 のサブエージェントが実装とレビューを担当し、CI がテストカバレッジを維持する。手動検証はステージング環境でチェックリストに沿って行う。

Type: Tutorial | Date: 2026-11-13

---

<a id="acknowledge"></a>
## 投稿者への謝辞

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/), [@fe_yukichi](https://x.com/fe_yukichi), [u/wollymonjac](https://www.reddit.com/user/wollymonjac/), [@lukaspet](https://x.com/lukaspet), [@DJ_HYSNS](https://x.com/DJ_HYSNS), [@joaoavf](https://x.com/joaoavf), [@aimikoda](https://x.com/aimikoda), [@ingi_erlingsson](https://x.com/ingi_erlingsson), [@hanghuang_](https://x.com/hanghuang_), [@MecAgent](https://x.com/MecAgent), [Plotly](https://plotly.com/), [@gdubs](https://news.ycombinator.com/user?id=gdubs), [@nickalaso](https://news.ycombinator.com/user?id=nickalaso), [@tukiyomiiori](https://x.com/tukiyomiiori), [@allTheYud](https://x.com/allTheYud), [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen), [@0_____0](https://news.ycombinator.com/user?id=0_____0), [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff), [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology)
