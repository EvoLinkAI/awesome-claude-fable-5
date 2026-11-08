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
## 🍌 はじめに

Claude Fable 5 の高シグナルなユースケースを集めたリポジトリへようこそ。

**私たちは、公開デモやクリエイターコミュニティから厳選した、Claude Fable 5 の実利用ケース、チュートリアル、連携例、評価を収集しています。**

この日本語 README は、具体的なワークフロー、プロンプト、デモ、連携、ベンチマーク証拠、または実用上の限界がある高シグナルな事例に焦点を当てています。

ほとんどの事例は X/Twitter の投稿と公開デモからキュレーションされています。各ケースタイトルは元のソースへ、各著者ハンドルは作成者プロフィールへリンクしています。

Evolink で試す: [Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

<a id="-overview"></a>
## 📊 概要

- **従来の Fable 5 事例 88 件とコミュニティ事例 241 件、合計 329 件。**
- コーディングエージェント、長時間自動化、ゲーム、ビジュアルデザイン、3D シミュレーション、ナレッジワーク、チュートリアル、API 連携、ベンチマーク、価格、ローンチ時の制限をカバーします。
- 各ケースには、元ソース、作成者の帰属、簡潔な要点、証拠タイプ、公開日が含まれます。
- 実用的なワークフローを見つけ、強みと限界を比較し、再現可能なプロンプトを発見し、連携例を追うためにこのリポジトリを活用してください。

> [!NOTE]
> このコレクションは、誇張よりも具体的な証拠を優先します。再現可能なプロンプト、出荷済みデモ、ベンチマーク手法、連携メモ、コストデータ、明確に述べられた注意点を重視しています。

<a id="-quick-api-access"></a>
## ⚡ API クイックアクセス

Evolink 互換の Messages API から Claude Fable 5 を利用できます。[Evolink](https://evolink.ai/login?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5) で API トークンを取得し、`<token>` をそのトークンに置き換えてください。

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
## 📑 メニュー

| セクション | ケース |
|---|---|
| [💻 コーディングとコード生成](#coding-and-code-generation) | Case 1-6 |
| [🤖 エージェントと長時間自動化](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 ゲームとインタラクティブデモ](#games-and-interactive-demos) | Case 9-12 |
| [🎨 ビジュアル、デザイン、動画、3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 ドキュメント、ナレッジワーク、リサーチ](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 チュートリアル、コース、プロンプトリソース](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 プラットフォーム、API、ツール連携](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 評価、比較、限界](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | クレジットと訂正ポリシー |

### [💻 コーディングとコード生成](#coding-and-code-generation)

| Case | 何がわかるか | 種類 |
|---|---|---|
| [Cursor のマルチステージワークフロー](#case-1) | マルチモデルの Cursor ワークフロー内で、Fable 5 を計画レビューと批評のステップとして使い、その後の実装と修正をより安価なモデルや専門モデルに戻す。 | 評価 |
| [スクリーンショットから GitHub を再現](#case-2) | プロダクトのスクリーンショットをエージェント型コーディングツールに貼り付け、Fable 5 に動作する機能付きでインターフェースを再現させる。 | デモ |
| [1 プロンプトのブラックホールシミュレーション](#case-3) | Fable 5 に詳細なクリエイティブコーディング用プロンプトを 1 つ与え、自己完結した Three.js の物理可視化を作らせる。 | チュートリアル |
| [ワンショットの macOS 風 Web OS](#case-4) | Fable 5 に完全な単一ファイル Web OS を依頼し、UI シェル、アプリ、インタラクション、音声、埋め込みゲーム挙動まで 1 回で構築させる。 | チュートリアル |
| [1,687 個のプロンプトで Spawn 5.0 を構築](#case-5) | Fable 5 を長時間セッションのエンジニアリングパートナーとして多数のプロンプトにまたがって使い、人間の役割をアーキテクチャ設計から出力品質の判断へ移す。 | チュートリアル |
| [大規模 Pull Request の所見付きレビュー](#case-6) | Fable 5 に大きな Pull Request を向け、正しさ、偽陽性、本当のバグ、仕上げ上の問題をレビューさせる。 | デモ |

### [🤖 エージェントと長時間自動化](#agents-and-long-running-automation)

| Case | 何がわかるか | 種類 |
|---|---|---|
| [長期リレー型ワークフローのレビュー](#case-7) | サイト再構築、プログラム型コンテンツパイプライン、音声の一致、セキュリティレビュー、最終品質チェックなど、野心的で長期的な作業に Fable 5 を使う。 | 評価 |
| [インフラ障害を診断して修正 PR を作成](#case-8) | ログ、データベースエラー、イメージ digest などのインフラ手掛かりへのアクセスを Fable 5 に与え、障害を診断して修正を準備させる。 | 評価 |

### [🎮 ゲームとインタラクティブデモ](#games-and-interactive-demos)

| Case | 何がわかるか | 種類 |
|---|---|---|
| [指トラッキング Dino Runner](#case-9) | 入力メカニクスとして指トラッキングを使うブラウザゲームを Fable 5 に作らせる。 | デモ |
| [2 文で作るレーシングゲーム](#case-10) | Fable 5 に非常に短いゲームプロンプトを与え、マップ、モード、音楽、UI、ゲームアセットを 1 回で生成させる。 | チュートリアル |
| [Rust 製のインストール可能なターミナル Minecraft](#case-11) | ターミナル用コーディングハーネス経由で Fable 5 を実行し、インストール可能な Rust 製ターミナルゲームを作らせる。 | デモ |
| [時間とコスト付きの Minecraft クローン](#case-12) | 1 つのプロンプトで Fable 5 にプレイ可能な Minecraft 風クローンを依頼し、時間、コスト、コード量、機能範囲を評価する。 | チュートリアル |

### [🎨 ビジュアル、デザイン、動画、3D](#visual-design-video-and-3d)

| Case | 何がわかるか | 種類 |
|---|---|---|
| [再現可能な Ecommerce メール用フルプロンプト](#case-13) | 正確なセクション、商品要件、ビジュアル方向性、制約を含む、ブランドメールモックアップ用の完全なクリエイティブブリーフを Fable 5 に与える。 | チュートリアル |
| [Swiss Lever Watchmaker ベンチマーク](#case-14) | 機械シミュレーションベンチマークに Fable 5 を使い、物理的正しさを実装、検証、反復させる。 | 評価 |
| [Three.js の Friends アパートシーン](#case-15) | Fable 5 に、間取り図とシーン参照をナビゲート可能な Three.js 環境へ変換するよう促す。 | 評価 |
| [プロンプトと URL 付きの太陽系シミュレーション](#case-16) | 物理原理から天文学シミュレーションを構築するために Fable 5 を使い、シミュレーションと公開出力が準備できるまで反復する。 | チュートリアル |

### [📚 ドキュメント、ナレッジワーク、リサーチ](#documents-knowledge-work-and-research)

| Case | 何がわかるか | 種類 |
|---|---|---|
| [Stripe と科学ワークフローの証拠](#case-17) | コピー＆ペースト用プロンプトではなく、エンタープライズ移行や科学ワークフローの主張を支える証拠として使う。 | 評価 |
| [政策メモと変更履歴ワークフロー](#case-18) | 変更履歴、コメントのトリアージ、文字起こしに基づく編集など、長文の定性的ドキュメント作業に Fable 5 を使う。 | チュートリアル |
| [Deep Research プロンプトと出力](#case-19) | Fable 5 にリサーチ形式の質問を投げ、構造化され歴史的根拠のある長文回答を生成できるか評価する。 | デモ |

### [🧭 チュートリアル、コース、プロンプトリソース](#tutorials-courses-and-prompt-resources)

| Case | 何がわかるか | 種類 |
|---|---|---|
| [Fable 5 が Claude Code ワークフローをどう変えるか](#case-20) | すべての手順を細かく管理するのではなく、方向性、コンテキスト、目標、検証基準を設定して Fable 5 を使う。 | デモ |
| [10 億トークンレビューとルーティング戦略](#case-21) | Fable 5 をフロンティア級の計画とレビューに使い、大量の実装はより安いモデルへルーティングする。 | チュートリアル |
| [防御的デバイス強化プロンプト](#case-22) | Fable 5 がデバイスを棚卸しし、正確な確認を提示し、検証を待つ、段階的な防御的 hardening プロンプトを実行する。 | チュートリアル |
| [サイト全体デザイン監査の Goal プロンプト](#case-23) | `/goal` を使って Fable 5 にサイトを起動させ、ページをスクリーンショットし、UX を監査し、レポートを書き、安全な小修正を実施させる。 | チュートリアル |
| [長文クリエイティブワークフローの分業](#case-24) | Fable 5 に安定した形式と例を設計させ、その構造を別の生成システムへ渡してドメイン固有の出力を作る。 | チュートリアル |
| [Fable 5 利用の初心者ガイド](#case-25) | 細かいステップごとの指示ではなく、目標志向のプロンプト、検証ループ、effort 設定で Fable 5 を使う。 | 評価 |
| [コピー＆ペーストできるリポジトリ監査プロンプト](#case-26) | リポジトリ監査プロンプトを Fable 5 に貼り付け、ファイルに基づく探索、所見、戦略、マイルストーン型タスク計画を依頼する。 | チュートリアル |
| [限定ウィンドウでの利用戦略](#case-27) | アクセス条件が有利な期間に、Fable 5 の利用枠を監査、アーキテクチャ、計画に使い、実行にはより安いモデルを使う。 | チュートリアル |
| [Claude Code で Goals と Workflows を使う](#case-28) | 実装前に Fable 5 を思考パートナーとして使い、その後 `/goal` と workflows を組み合わせて計画を実行・検証する。 | チュートリアル |

### [🔌 プラットフォーム、API、ツール連携](#platform-api-and-tool-integration)

| Case | 何がわかるか | 種類 |
|---|---|---|
| [Hermes Agent 連携セットアップ](#case-29) | 複雑な `/goal` 実行やキャッシュ付きの長期タスクに `anthropic/claude-fable-5` を使うよう Hermes を設定する。 | チュートリアル |
| [機能、価格、サブスクリプションメモ](#case-30) | Fable 5 がいつ利用可能か、費用はいくらか、どの guarded domains が別モデルへ fallback する可能性があるかを理解するためにこのケースを使う。 | チュートリアル |
| [ローンチ、アクセス、価格、安全性の要約](#case-31) | アクセス経路、API model name、context window、caching strategy、subscription timing を選ぶためにこのローンチ要約を使う。 | チュートリアル |
| [Advisor ベースのコスト削減戦略](#case-32) | 追加の知能がコストに見合う場合、より安いモデルのワークフロー内で Fable 5 を advisor または reviewer として使う。 | 連携 |
| [価格、アクセス、安全ガードレール](#case-33) | ワークロードを計画する前に、Fable 5 のアクセス、API 価格、安全 fallback 挙動を理解するためにこのケースを使う。 | 連携 |
| [1 行の Swarms 連携](#case-34) | Swarms の model name を `anthropic/claude-fable-5` に設定し、Swarms framework または API 経由で Fable 5 を実行する。 | 連携 |

### [📏 評価、比較、限界](#evaluations-comparisons-and-limits)

| Case | 何がわかるか | 種類 |
|---|---|---|
| [Fable 5 vs GPT-5.5 のコストと品質比較](#case-35) | 同じ coding task で Fable 5 と GPT-5.5 を比較し、output quality、runtime、tool cost を判断する。 | 評価 |
| [AA-Omniscience ベンチマーク結果](#case-36) | 知識の正確性と hallucination behavior で Fable 5 を評価するために、この benchmark case を使う。 | 評価 |
| [Artificial Analysis Intelligence Index 結果](#case-37) | 他の frontier models に対する Fable 5 の overall intelligence ranking を benchmark するためにこのケースを使う。 | 評価 |
| [GDPval-AA Agentic Knowledge Work ベンチマーク](#case-38) | agentic real-world knowledge work で Fable 5 を評価するためにこのケースを使う。 | 評価 |
| [1 週間の第一印象と価格メカニズム](#case-39) | Fable 5 がどこで最も強いか、特に game design と systems planning を判断するために、この first-impressions case を使う。 | 連携 |
| [コストと速度の比較](#case-40) | 品質向上が、より高いコストと遅い long-horizon runs に見合うか判断するためにこの比較を使う。 | 評価 |
| [Claude Code 実使用メモ](#case-41) | tool use、personality、残る rough edges を含め、Claude Code 内で Fable 5 を評価するためにこのケースを使う。 | デモ |
| [Creative Writing ベンチマーク結果](#case-42) | Fable 5 の short-fiction writing quality と refusal behavior を判断するために、この benchmark case を使う。 | 評価 |
| [複数ベンチマークのローンチ要約](#case-43) | coding agents と complex tasks に最も関連する headline scores を理解するために、この launch benchmark summary を使う。 | 評価 |
| [GPT-5.5 とのベンチマークと価格比較](#case-44) | 価格と benchmark categories で Fable 5 を GPT-5.5 と比較評価するためにこの比較を使う。 | 評価 |
| [実地メモと実用上の制約](#case-45) | Fable 5 がどこで意味のある改善に感じられ、どこにまだ実用上の限界があるかを理解するために、この field report を使う。 | チュートリアル |
| [物理シミュレーション比較](#case-46) | 同一の physics simulation prompts を Fable 5 と Opus 4.8 に対して実行し、output quality、cost、speed を比較する。 | デモ |
| [デバッグ体験と設計判断](#case-47) | 単に推測させるのではなく、測定、ログ追加、検証、パッチを依頼して Fable 5 を debugging に使う。 | デモ |
| [多面的な長所と短所](#case-48) | Fable 5 を daily driver にする前に、実用上の強みと弱みを理解するためにこのケースを使う。 | デモ |
| [法務 S-1 ドラフトテスト](#case-49) | S-1 drafting prompt を legal-agent capability test として使い、structure、formatting、length を比較する。 | チュートリアル |
| [ヘルスケアベンチマーク詳細](#case-50) | healthcare-related tasks で Fable 5 を評価し、不足している hard medical evals を特定するためにこの benchmark note を使う。 | 評価 |
| [ParseBench ドキュメント解析評価](#case-51) | specialized OCR systems と比べて、Fable 5 が document parsing に cost-effective かを判断するためにこのケースを使う。 | 評価 |
| [SWE-Bench Pro と FrontierCode の比較](#case-52) | migrations、complex implementations、autonomous sessions、tests、visual verification に Fable 5 を評価するために、この benchmark case を使う。 | 評価 |
| [長い問題解決の定性的レビュー](#case-53) | production review はなお必要だが、Fable 5 がより長く難しい tasks に向いている理由を理解するために、この qualitative review を使う。 | 評価 |
| [ParseBench の忠実性とフォーマット結果](#case-54) | document faithfulness と formatting performance を判断するために、この ParseBench result を使う。 | 評価 |
| [ベンチマーク、価格、アクセス、セーフガード](#case-55) | benchmarks、pricing、access、safeguards、strategic implications の幅広い checklist としてこのケースを使う。 | 評価 |
| [公式ベンチマークスコア一覧](#case-56) | coding、computer use、security tasks 全体における Fable 5 の公式スコアを理解するために、この benchmark list を使う。 | 評価 |
| [APEX-SWE ベンチマーク手法](#case-57) | 特に observability と integration work において、APEX-SWE 上で Fable 5 を評価するためにこのケースを使う。 | 評価 |
| [ProofBench 形式数学結果](#case-58) | specialized theorem-proving systems と比較して、formal math における Fable 5 を評価するためにこのケースを使う。 | チュートリアル |
| [VirtueBench 予備分析](#case-59) | virtue categories 全体にわたる Fable 5 の moral-reasoning behavior を調べるためにこのケースを使う。 | 評価 |
| [API 空レスポンス安全性過適合テスト](#case-60) | launch-time safety overfit risk と API testing における empty-response behavior を理解するためにこのケースを使う。 | 評価 |
| [Fable のプロンプト設計と検証ガイド](#case-61) | 長いプロンプトの工夫に頼る代わりに、目標、背景、制約、ツール、検証ループを整えるためのガイドとして使う。 | チュートリアル |
| [参照画像から作るイスタンブールのアクションゲーム](#case-62) | 参照用スプライトシートと変換指示を与え、Fable 5 が遊べるアクションゲームを作れるか試す。 | デモ |
| [業務を可視化する 3D 都市ダッシュボード](#case-63) | Fable 5 を使い、業務フローを動きのある 3D 都市ダッシュボードとして表現する。 | デモ |
| [Three.js の穴ゲームをワンショットで制作](#case-64) | Fable 5 に Three.js の 3D ブラウザゲーム試作を 1 回で作らせる。 | デモ |
| [DeepSWE スコアの比較](#case-65) | DeepSWE の投稿を手掛かりに、ソフトウェア開発ベンチマークで Fable 5 xHigh と GPT-5.5 xHigh を比較する。 | 評価 |
| [リポジトリ分析のコスト比較](#case-66) | リポジトリ分析の比較を通して、トークン単価と人間による修正コストを併せて評価する。 | 評価 |
| [スーパーマリオ風ゲームのトークン消費](#case-67) | 1 回で作成したゲームを使い、Fable 5 の出力品質とトークン消費を評価する。 | デモ |
| [Claude Code のフォールバック設定](#case-68) | Fable 5 へのメッセージが検知された際にモデルを切り替える Claude Code の設定を確認する。 | 連携 |
| [Namma Metro シミュレーターの制作](#case-69) | Fable 5 で公共交通シミュレーターを作る、簡潔なバイブコーディングの例として参照する。 | デモ |
| [1 つのプロンプトで作る Dusk Drive](#case-70) | 人間の編集を加えないローポリゴンゲームの試作で、Fable 5 を評価する。 | デモ |
| [APEX-Agents の Pass@1 順位](#case-71) | APEX-Agents の結果を使い、複数工程の自律タスクにおける Fable 5 Max を比較する。 | 評価 |
| [Claude のモデル選択ガイド](#case-72) | Claude Code の最も難しい仕事に Fable 5 を温存するためのモデル選択を検討する。 | チュートリアル |
| [HermesWorld を開発する自動エージェントループ](#case-73) | 構築、テスト、試遊、動作確認を何日も続ける、手動操作なしの Fable 5 ループを調べる。 | 連携 |
| [McKinsey 風レポートのプロンプト検証](#case-74) | 文書生成プロンプトで、コンサルティング報告書の構成、図表、論旨、リスク分析を評価する。 | チュートリアル |
| [セーフガードの可視化](#case-75) | 公式の投稿から、Fable 5 のセーフガード表示、API の拒否理由、Opus へのフォールバックを確認する。 | 連携 |
| [Claude Code のモデル照合修正](#case-76) | Claude Code の変更履歴を参照し、Fable 5 のモデル名とコンテキストの照合問題を避ける。 | 連携 |
| [Claude Code で 3 つの Web アプリを制作](#case-77) | 複数の Web アプリを生成した初心者のデモから、Claude Code 内の Fable 5 の使い方を確認する。 | デモ |
| [オープンソースのアプリビルダー Rilable](#case-78) | iOS、Web アプリ、サンドボックス、API トークン費用にまたがる Fable 5 の使い方を調べる。 | 連携 |
| [DeepSWE コーディングエージェント指数デビュー](#case-79) | 公開 GitHub 修正の再利用を避けた、より難しい agentic coding tasks での Fable 5 を、更新版 Artificial Analysis 指数で比較する。 | Evaluation |
| [DataEmpire ウェブ解析ゲーム](#case-80) | Claude Fable 5 に訪問者や節目をゲーム内エンティティへ対応付けさせ、生のサイト解析データを繰り返し遊べるゲームに変える。 | Integration |
| [FrontierSWE 20時間タスクのシグナル](#case-81) | Claude Fable 5 が短いバグ修正ループだけでなく、非常に長いエンジニアリング作業でも生産性を維持できる証拠として FrontierSWE を使う。 | Evaluation |
| [KernelBench-Hard CUDA 記録](#case-82) | 既存ライブラリのラッパーではなく低レベル最適化が必要なとき、Fable 5 を高度な CUDA カーネル生成に使う。 | Evaluation |
| [Figma Capture ランディングページ複製](#case-83) | スクリーンショット推測ではなく、競合ページを Figma レイヤーとして取り込み、Claude Code と Fable 5 で構造、コピー、ブランドシステムを再構築する。 | Integration |
| [2時間で作る GTA 2 クローン](#case-84) | Claude Fable 5 のコード生成と別系統のアセットツールを組み合わせ、スタック全体を手書きせずにプレイ可能な 3D ゲームを素早く構築する。 | Tutorial |
| [CloudWatch ログトリアージエージェント](#case-85) | Fable 5 搭載エージェントに巨大なサービスログ文脈を読み込ませ、アーキテクチャを推定したうえで特定の障害へ絞り込ませる。 | Integration |
| [サンドボックス内のワールドカップ予測アプリ](#case-86) | 複数の frontier models を隔離サンドボックスに載せ、公開予測アプリ向けに最新ニュース、負傷情報、イエローカード状況を調査させる。 | Integration |
| [WolfBench 拒否コスト事例](#case-87) | Claude Fable 5 で長時間の自律実行を見積もる際、refusal behavior を実際の benchmark variable として扱う。 | Evaluation |
| [API アクセス停止トラッカー](#case-88) | レート制限や予告の少ない提供停止がありうる frontier model への継続アクセスに依存するなら、スクリプトで可用性を監視する。 | Integration |



### [🆕 Fable 5.5 のコミュニティデモ](#fable-5-5-community-demos)

| 事例 | 種類 |
|---|---|
| [コードで生成した音声付きキツネのアニメーション](#case-89) | Demo |
| [自由度の高い制作指示から作るアニメーション](#case-90) | Demo |
| [アニメーション付き建設会社サイト](#case-91) | Demo |
| [Three.js による自動車のプレゼンテーション](#case-92) | Demo |
| [Minecraft 風ブラウザゲームのデモ](#case-93) | Demo |
| [Three.js のペリカンサイクリング動画](#case-94) | Demo |
| [正確なプロンプト付きのペリカン自転車 SVG](#case-95) | Demo |
| [疾走するシマウマのアニメーション例](#case-96) | Demo |
| [注文を手動で行う TradingView インジケーター](#case-97) | Demo |
| [一つの点から広がる短編アニメーション](#case-98) | Demo |
| [画風を変えながら進むスーパーマン](#case-99) | Demo |
| [音楽付きの人類進歩アニメーション](#case-100) | Demo |
| [Opus と比較する紹介映像](#case-101) | Evaluation |
| [歌詞と出来事を映像でつなぐ](#case-102) | Demo |
| [浮遊する風景のボクセル人物](#case-103) | Demo |
| [3D ルーブ・ゴールドバーグ装置](#case-104) | Demo |
| [音と動きを備えた 3D コントローラー](#case-105) | Demo |
| [JavaScript によるコミック人物展示](#case-106) | Demo |
| [世界、ボス、ランキングを備えた Updraft](#case-107) | Demo |
| [サンフランシスコ地図を走るゲーム](#case-108) | Demo |
| [Seedance のアクション映像向けプロンプト](#case-109) | Demo |
| [デスクトップ協働ツールの紹介動画](#case-110) | Demo |
| [短い依頼で変化する画風](#case-111) | Demo |
| [三体問題の可視化](#case-112) | Demo |
| [多様な画風のアニメーションギャラリー](#case-113) | Demo |
| [ロボットの相棒と手続き型の毛並み](#case-114) | Demo |
| [数学を題材にしたモーション映像](#case-115) | Demo |
| [Your Woman の歌詞動画](#case-116) | Demo |
| [音楽動画を JavaScript で描き直す](#case-117) | Demo |
| [中国サッカーのアニメーション](#case-118) | Demo |
| [携帯ゲーム機のリトポロジー展示](#case-119) | Demo |
| [Minecraft と Pokémon の融合](#case-120) | Demo |
| [大規模言語モデルの作り方を映像で説明](#case-121) | Demo |
| [Altman のハイライト映像](#case-122) | Demo |
| [三十六計の第一計を描く映像](#case-123) | Demo |
| [ゲームのモデリング、リギング、アニメーション](#case-124) | Demo |
| [子どもの死亡を描く無言の短編](#case-125) | Demo |
| [解糖からエタノール生成までの SVG](#case-126) | Demo |
| [十六機の Starship 同時打ち上げ](#case-127) | Demo |
| [ペリカンの自転車アニメーション](#case-128) | Demo |
| [未来百五十年の物語](#case-129) | Demo |
| [独自の Humanity Walks 実験](#case-130) | Demo |
| [コード映画 The Grader](#case-131) | Demo |
| [ホラー短編 Reawakening](#case-132) | Demo |
| [二十五秒の自己改善映像](#case-133) | Demo |
| [城の場面と利用費用の感想](#case-134) | Evaluation |
| [四十秒のブランド紹介広告](#case-135) | Demo |
| [Rocketball のリメイク](#case-136) | Demo |
| [ボクセル五重塔の比較](#case-137) | Evaluation |
| [想像上の Switch 3 の発表](#case-138) | Demo |
| [ランディングページの前後比較](#case-139) | Evaluation |
| [想像上の AI の内側の視点](#case-140) | Demo |
| [Go の歌詞モーション](#case-141) | Demo |
| [二本目の十五秒モーション作品集](#case-142) | Demo |
| [エージェントの実装計画レビュー](#case-143) | Tutorial |
| [Claude マスコットのダンス](#case-144) | Demo |
| [世界七不思議のインタラクティブな島々](#case-145) | Demo |
| [Propellerheads の音楽動画](#case-146) | Demo |
| [Steamboat Willie アニメーション比較](#case-147) | Evaluation |
| [三星堆を題材にした短編](#case-148) | Demo |
| [Bugatti Chiron の前後比較](#case-149) | Evaluation |
| [概念短編 GRAIN](#case-150) | Demo |
| [Human in Transit 美術ギャラリー](#case-151) | Demo |
| [シルクロードの視覚短編](#case-152) | Demo |
| [四つの変革を示すプレゼン](#case-153) | Demo |
| [過去の会話との語り口の比較](#case-154) | Evaluation |
| [カカポのかわいさ比較](#case-155) | Evaluation |
| [十のコミック時代を進むスパイダーマン](#case-156) | Demo |
| [イルミナティを題材にした架空のホラー](#case-157) | Demo |
| [コードによる核科学史の映画](#case-158) | Demo |
| [ユニバーサル・ハイ・インカムの解説](#case-159) | Demo |
| [Altman と Amodei の対立の解説](#case-160) | Demo |
| [Claude マスコットの音楽動画](#case-161) | Demo |
| [クォークから宇宙へ連続ズーム](#case-162) | Demo |
| [二〇七六年の世界を想像する](#case-163) | Demo |
| [ロウアー・マンハッタンの建築年表](#case-164) | Demo |
| [甲骨文字から始まるアニメーション](#case-165) | Demo |
| [人物が美術史を進む別の作品](#case-166) | Demo |
| [コードによるセイキロスの視聴覚作品](#case-167) | Demo |
| [ジェット機アニメーションの比較](#case-168) | Evaluation |
| [モデルの自己紹介映画](#case-169) | Demo |
| [終末世界のカードゲーム試作](#case-170) | Demo |
| [職場アニメーション The Late Byte](#case-171) | Demo |
| [Queens of the Stone Age の歌詞動画](#case-172) | Demo |
| [共有された Three.js の物語場面](#case-173) | Demo |
| [歴史を渡るムーンウォーク](#case-174) | Demo |
| [詳細な依頼によるモーショングラフィックス](#case-175) | Demo |
| [レンタル事業のウェブ画面](#case-176) | Demo |
| [AGI を題材にした創作映像](#case-177) | Demo |
| [猫の脇筋を含む美術史](#case-178) | Demo |
| [戦闘試作とボクセルの場面](#case-179) | Demo |
| [インターネット・ミームの年表](#case-180) | Demo |
| [一行から作る粒子の動き](#case-181) | Demo |
| [Kung-Fu Boy アニメーション](#case-182) | Demo |
| [ホルムズ海峡の討論アニメーション](#case-183) | Demo |
| [ユニコーンの SVG 表現実験](#case-184) | Demo |
| [ハロウィーンの季節アニメーション](#case-185) | Demo |
| [Blender CLI の蛮族とカバー](#case-186) | Demo |
| [Claude の一日](#case-187) | Demo |
| [3D による人類史](#case-188) | Demo |
| [速いモーションデザイン作品](#case-189) | Evaluation |
| [自由な複雑 3D 作品](#case-190) | Demo |
| [棒人間の格闘アニメーション](#case-191) | Demo |
| [一つの依頼による UI モーション](#case-192) | Demo |
| [架空の SCP-8517 アニメーション](#case-193) | Demo |
| [水彩の秋アニメーション](#case-194) | Demo |
| [手続き型の人形ステージ](#case-195) | Demo |
| [ブラウザーで動くペリカン](#case-196) | Demo |
| [宇宙が自らを見る](#case-197) | Demo |
| [独自のジェット機アニメーション実験](#case-198) | Demo |
| [最初の自由モーション作品](#case-199) | Demo |
| [コードで描く文明史](#case-200) | Demo |
| [チップからサーバーへのズーム比較](#case-201) | Evaluation |
| [月旅行の個人アニメーション](#case-202) | Demo |
| [日本風ボクセル場面の比較](#case-203) | Evaluation |
| [視聴覚短編 Steaming the Frontier](#case-204) | Demo |
| [さまざまな画風を通るスーパーマン](#case-205) | Demo |
| [Cupcake 風ボス戦の試作](#case-206) | Demo |
| [太陽が移動する帆船の場面](#case-207) | Demo |
| [Paracortex と Pi の更新紹介映像](#case-208) | Demo |
| [Curio 2.0 のサイト紹介動画](#case-209) | Demo |
| [想像上の Hugging Face 3D 物語](#case-210) | Demo |
| [Claude for Chrome で JS Paint を操作](#case-211) | Demo |
| [静的なペリカン自転車 SVG](#case-212) | Demo |
| [BlockBench MCP と Minecraft スキル](#case-213) | Demo |
| [一つの HTML の Dig Dug](#case-214) | Demo |
| [機械仕掛けのタコ SVG](#case-215) | Demo |
| [美術の画風を渡る Humanity Walks](#case-216) | Demo |
| [自由な依頼のブラックホール](#case-217) | Demo |
| [オーロラクラゲの動きの比較](#case-218) | Evaluation |
| [Nintendo Switch の装着と起動 SVG](#case-219) | Demo |
| [対話型 3D 場面 The Loom](#case-220) | Demo |
| [同じプロンプトによるモーションデザイン映像](#case-221) | Evaluation |
| [整った見た目と弱い奥行き](#case-222) | Evaluation |
| [評価が分かれる日本風場面](#case-223) | Evaluation |
| [コントローラー SVG の比較](#case-224) | Evaluation |
| [産業機器の場面](#case-225) | Demo |
| [巨大な殻を持つエラ虫の再構成](#case-226) | Demo |
| [二回の依頼による GameCube コントローラー](#case-227) | Demo |
| [X 投稿のためのスクリーンショット編集](#case-228) | Demo |
| [ボクセル桜の前後比較](#case-229) | Evaluation |
| [SHADERKIN の布インターフェース試作](#case-230) | Demo |
| [共有された金色時計の画面アニメーション](#case-231) | Demo |
| [Before There Was Anything の物語](#case-232) | Demo |
| [共有された青い粒子の渦](#case-233) | Demo |
| [二回の修正を経た多画面インターフェース](#case-234) | Demo |
| [動物を積み重ねた描画場面](#case-235) | Demo |
| [四つのオープンワールド RPG の比較](#case-236) | Evaluation |
| [二つのフロントエンド動画の比較](#case-237) | Evaluation |
| [コードで生成した苔のロボット映画](#case-238) | Demo |
| [コンテナ港のシミュレーション再制作](#case-239) | Demo |
| [空港エプロンの場面再制作](#case-240) | Demo |
| [抽象的な 3D 世界を進むペリカン](#case-241) | Demo |
| [歴史的な帆船の場面](#case-242) | Demo |
| [Carbon との走行と歩様の比較](#case-243) | Evaluation |
| [清涼飲料ボトルの展示](#case-244) | Demo |
| [Astra と比べるペリカンの動き](#case-245) | Evaluation |
| [コード動画用モーションデザイン指示](#case-246) | Tutorial |
| [写真を参照したボクセル肖像](#case-247) | Demo |
| [Opus と比べる飛ぶペリカン](#case-248) | Evaluation |
| [Morning Ride のペリカン画面](#case-249) | Demo |
| [同じ指示と異なる画風の場面](#case-250) | Evaluation |
| [ペリカン、自転車、馬の構図](#case-251) | Demo |
| [参照ツイートから作る等角場面](#case-252) | Demo |
| [ペリカン自転車の機構の接写](#case-253) | Demo |
| [ペリカンに乗る自転車](#case-254) | Demo |
| [Carbon と比べるペリカン SVG の画風](#case-255) | Evaluation |
| [青い漫画鳥の自転車場面](#case-256) | Demo |
| [森の道を走るペリカンの画面](#case-257) | Demo |
| [Carbon と比べる棒人間の戦闘](#case-258) | Evaluation |
| [初期テストのペリカン SVG 参照](#case-259) | Demo |
| [モデル横断 SVG テストのペリカン参照](#case-260) | Evaluation |
| [Carbon と比較する自転車 SVG の細部](#case-261) | Evaluation |
| [峡谷集落の 3D 場面](#case-262) | Demo |
| [Opus と比べるコントローラーの細部](#case-263) | Evaluation |
| [毎週のウェブ SEO 監査フロー](#case-264) | Integration |
| [Opus の映像で Fable の素材を再利用](#case-265) | Integration |
| [マンダラと幾何学のアプリ](#case-266) | Demo |
| [Three.js の自転車走行者](#case-267) | Demo |
| [FrontierCS 2 の評価スナップショット](#case-268) | Evaluation |
| [3モデルのシマウマアニメーション比較](#case-269) | Evaluation |
| [長い日本語文章への批評](#case-270) | Evaluation |
| [作例で導く技術 PowerPoint](#case-271) | Evaluation |
| [音楽全体のまとまりを比較する](#case-272) | Evaluation |
| [早すぎる完了報告と設計の不満](#case-273) | Limit |
| [不快に感じたイカのアート](#case-274) | Limit |
| [設計図風のモーションデザイン](#case-275) | Demo |
| [ボクセル桜の鳥と魚](#case-276) | Demo |
| [人物生成の失敗報告](#case-277) | Limit |
| [時間と費用を添えたペリカン SVG](#case-278) | Evaluation |
| [電話で遠隔操作する Claude Code 群](#case-279) | Integration |
| [高山湖の上に広がる天の川](#case-280) | Demo |
| [手続き型の水と音によるクジラの跳躍](#case-281) | Demo |
| [4モデルのシマウマ動作比較](#case-282) | Evaluation |
| [Lightreelで自然言語からクリエイターを探す](#case-283) | Demo |
| [雲海の上を飛ぶ船](#case-284) | Demo |
| [動きながら内部を見せる機械の心臓](#case-285) | Demo |
| [歩いて探索できる浮遊ボクセル庭園と塔](#case-286) | Demo |
| [8チームで制作した海の冒険短編](#case-287) | Demo |
| [操作できるハイパーカーの展示](#case-288) | Demo |
| [生命の木の誕生](#case-289) | Demo |
| [内部機械が動く歩行城](#case-290) | Demo |
| [トーストのキャラクターと機械の甲虫](#case-291) | Demo |
| [嵐の中の灯台守](#case-292) | Demo |
| [海辺の町と海の生き物](#case-293) | Demo |
| [3モデルによるラグ上のレース比較](#case-294) | Evaluation |
| [トラックからロボットへの変形](#case-295) | Demo |
| [FableとHunyuanのアニメーションフレーム](#case-296) | Evaluation |
| [光を分け与えるアニメーション](#case-297) | Demo |
| [山々の間に広がるボクセルの村](#case-298) | Demo |
| [4モデルによるペリカンとゾウの構図](#case-299) | Evaluation |
| [インパクトフレーム付きアニメ風剣戟](#case-300) | Demo |
| [4モデルの走るシカ比較](#case-301) | Evaluation |
| [水没した街を進むロボット](#case-302) | Demo |
| [Blenderの剣と紹介映像](#case-303) | Demo |
| [Lantern Isleのピクセル村アニメーション](#case-304) | Demo |
| [Pauseのゲーム動画編集デモ](#case-305) | Demo |
| [海辺を自転車で走るペリカン](#case-306) | Demo |
| [ワンカットで木星を縦断](#case-307) | Demo |
| [Claude Codeのハーネスで行う敵対的コードレビュー](#case-308) | Tutorial |
| [Three.jsで作る短編アニメ『Ryumon』](#case-309) | Demo |
| [雷雨の中を進む手こぎボート](#case-310) | Demo |
| [オフライン短編アニメで雨粒を止める](#case-311) | Demo |
| [BlenderとPythonで作るスクリプトアニメ](#case-312) | Demo |
| [Three.jsで作る灯台アニメ『Beacon』](#case-313) | Demo |
| [コードで描画したオープニング映像](#case-314) | Demo |
| [6フレームの斧のGIFをBlenderで再構築](#case-315) | Demo |
| [2つのモデルで作るインタラクティブな虹色ゼリー](#case-316) | Evaluation |
| [HTMLファイル1つのドラゴン飛行ゲーム](#case-317) | Demo |
| [Blenderの独自ソルバーでバスケットボールの落下を再現](#case-318) | Demo |
| [スクリプトで作るアニメのフレーム点検](#case-319) | Demo |
| [マッチを擦る瞬間を44倍スローで再現](#case-320) | Demo |
| [参照画像をSVGで描き直す](#case-321) | Demo |
| [同じマリオ風の課題を2つのモデルに依頼](#case-322) | Evaluation |
| [立体ボクセルの塔](#case-323) | Demo |
| [Three.jsで燃える手紙の煙を表現](#case-324) | Demo |
| [稲妻を追って地面まで](#case-325) | Demo |
| [隕石を受け止める巨大ロボット](#case-326) | Demo |
| [同じ課題で作るピクセルアートのショーウィンドウ](#case-327) | Evaluation |
| [アニメの街に現れる青銅の巨人](#case-328) | Demo |
| [ガラスフラスコに広がる青インク](#case-329) | Demo |

<a id="coding-and-code-generation"></a>
## 💻 コーディングとコード生成

<a id="case-1"></a>
### Case 1: [Cursor のマルチステージワークフロー](https://x.com/AlicanKiraz0/status/2064487347605918180) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**マルチモデルの Cursor ワークフロー内で、Fable 5 を計画レビューと批評のステップとして使い、その後の実装と修正をより安価なモデルや専門モデルに戻す。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8b1352e20cff54688c97f17c.png" alt="Cursor のマルチステージワークフロー" width="760">

Fable 5 と GPT 5.5 の最終スコアを見ると、その差は非常に小さい。私の控えめな利用推奨はこうだ。Cursor のようにハイブリッドモデルをサポートする IDE プラットフォームでは、段階的なワークフローを使う。

フェーズ 1: コードレビューとプロジェクト調査の最初の段階では、コンテキストを温めながら、GPT 5.5 High、Minimax M3、Kimi K2.6、Composer 2.5 のいずれかを使う。

フェーズ 2: プロジェクト計画の準備には、GPT 5.5 Very High または Opus 4.8 を使う。

フェーズ 3: プロジェクト計画の分析には Fable 5 を使い、計画の欠陥部分を特定させる。修正には GPT 5.5 Very High を使う。

フェーズ 4: 計画の実装には、Minimax M3、Deepseek v4 Max、Composer 2.5、Sonnet 4.6 のいずれかを使う。

フェーズ 5: 最終レビューと、実装が計画に沿っているかの確認には GPT 5.5 High を使う。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [スクリーンショットから GitHub を再現](https://x.com/coldopn/status/2064435234465087638) (by [@coldopn](https://x.com/coldopn))

**プロダクトのスクリーンショットをエージェント型コーディングツールに貼り付け、Fable 5 に動作する機能付きでインターフェースを再現させる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/14123609b06071f3b9527bee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f4df4f42ce047201d9a096a6.jpg" alt="スクリーンショットから GitHub を再現" width="760"><br>▶ 動画を見る</a>

🚨 Anthropic Fable 5 がスクリーンショットから GITHUB を再現した!!

私がやったことは、GitHub UI のスクリーンショットを Kilo Code に貼り付け、実際の機能付きで GitHub を再現するよう伝えただけ。

10 分間コードを書き、$4.07 を消費した。

結果は機能する GitHub レプリカだった: https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [1 プロンプトのブラックホールシミュレーション](https://x.com/deveshcodes_/status/2064437742189379745) (by [@deveshcodes_](https://x.com/deveshcodes_))

**Fable 5 に詳細なクリエイティブコーディング用プロンプトを 1 つ与え、自己完結した Three.js の物理可視化を作らせる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9bd45e74c64ceb3639600805.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ce5f3ea8ba270f89d60523cc.jpg" alt="1 プロンプトのブラックホールシミュレーション" width="760"><br>▶ 動画を見る</a>

@claudeai は Claude Fable 5 で、Three.js のリアルタイムブラックホールレンズ効果シミュレーションを一発生成した。

重力レンズ、ドップラーブーストされた降着円盤、光子球、色収差、手続き型の星空が含まれていた。

結果: 60fps、単一 HTML ファイル、1 プロンプト。

新しい基準線がすごい 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [ワンショットの macOS 風 Web OS](https://x.com/intheworldofai/status/2064421915347812672) (by [@intheworldofai](https://x.com/intheworldofai))

**Fable 5 に完全な単一ファイル Web OS を依頼し、UI シェル、アプリ、インタラクション、音声、埋め込みゲーム挙動まで 1 回で構築させる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a66f34402d04f708819fa575.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/81946293919c84d4cafff841.jpg" alt="ワンショットの macOS 風 Web OS" width="760"><br>▶ 動画を見る</a>

🚨 Claude Fable 5 が、macOS 風の完全な Web OS をワンショットで構築し、ほとんどのモデルよりさらに踏み込んだ。

単一 HTML ファイル、埋め込み CSS + JS。

1 つのプロンプトから、次を構築した:

- macOS のメニューバー + dock
- ドラッグ可能でリサイズ可能なアプリウィンドウ
- 機能するファイルエクスプローラー
- 動作するターミナル + ブラウザのモックアップ
- SVG デスクトップアイコン + 通知
- 設定アプリ、テーマ、起動画面
- 外部ファイルなしのリアルな合成音を備えた完全機能のサウンドプレイヤー
- デスクトップ内で遊べる Minecraft クローン

ほぼ修正なしで、すべて 1 回で生成された。

動作するサウンドプレイヤーに加えて実際の Minecraft クローンまで作った例は、他のモデルではまだ見たことがない。Fable 5 のフロントエンド/UI 生成はばかげたレベルになってきている。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [1,687 個のプロンプトで Spawn 5.0 を構築](https://x.com/jsnnsa/status/2064420561078693941) (by [@jsnnsa](https://x.com/jsnnsa))

**Fable 5 を長時間セッションのエンジニアリングパートナーとして多数のプロンプトにまたがって使い、人間の役割をアーキテクチャ設計から出力品質の判断へ移す。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86834f15f352ec8625cce187.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b4077e43a1342d8567fa423f.jpg" alt="1,687 個のプロンプトで Spawn 5.0 を構築" width="760"><br>▶ 動画を見る</a>

claude fable 5 が公開された。

spawn 5.0 はこれで作られた:

- 1,687 プロンプト
- 102 セッション
- 私の仕事はアーキテクチャからセンスの判断へ移った

私たちが作ったものは、Opus でチーム全員が取り組んでも少なくとも 1 か月はかかったはずのものばかりだった:

- Rapier に匹敵し、サイドスレッドとして 1 日でテスト可能だった、ゼロからの物理エンジン Mantle
- clustered froxel lighting: 8 個のライトから 1,000 個以上の完全動的ライトへ
- WebGPU 上のリアルタイム拡散 GI、しかもスマートフォンで動作
- Unreal や Unity が出荷しているものを超えるシェーダーアーキテクチャを持つ 100 万粒子 GPU VFX
- MMO 規模のネットコード
- アルファ版のネイティブ iOS アプリ

すべて約 1 週間でできた。すべてモバイルで動く。このリストには出荷したものの半分も含まれていない。完全な changelog はスレッドにある。

ベンチマークには現れない部分: このモデルは素晴らしい個性を持っている。本当に面白い。物理エンジンを書き直している最中、何度も涙が出るほど笑った。天才性とキャラクターは別々の機能ではない。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [大規模 Pull Request の所見付きレビュー](https://x.com/ryanrhughes/status/2064411147076534705) (by [@ryanrhughes](https://x.com/ryanrhughes))

**Fable 5 に大きな Pull Request を向け、正しさ、偽陽性、本当のバグ、仕上げ上の問題をレビューさせる。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c4f47540205a071b0144ad9d.png" alt="大規模 Pull Request の所見付きレビュー" width="760">

Fable 5 に単一 PR（74 ファイル / +3,705 / -1,246）のレビューを任せ、どうなるか見てみた。34 分間実行され、5 時間セッションの 42% を使い、「correctness」の所見を 16 件出し、次を見つけた:

- 怖そうに見える偽陽性 2 件
- 本物の監査上の正しさに関わるバグ 3 件
- 正当だが小さい UX/仕上げ問題 約 5 件
- たくさんの cleanup 意見

これはリリースするには危険すぎたのか？

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 エージェントと長時間自動化

<a id="case-7"></a>
### Case 7: [長期リレー型ワークフローのレビュー](https://x.com/JJEnglert/status/2064469635190170105) (by [@JJEnglert](https://x.com/JJEnglert))

**サイト再構築、プログラム型コンテンツパイプライン、音声の一致、セキュリティレビュー、最終品質チェックなど、野心的で長期的な作業に Fable 5 を使う。**

Claude Fable 5 レビューの短い版: Claude Fable 5 のテストに 10 億トークンを費やしたところ、不公平な優位性を持っているように感じた。

私は目視テストで判断する。モデルを実際の仕事に投入して観察する。時間を節約してくれるのか、それとも奪うのか。私が見落としたものを捕まえるのか。相棒のように感じるのか、それとも子守りが必要なツールなのか。

これは、重要なすべての次元で合格した久しぶりのモデルであり、しかも僅差ではなかった。

構築: 私は Tenex のサイトを再構築していた。非常にカスタム性が高く、とても難しかった。GPT 5.5 と Claude 4.8 は単独では突破できなかった。参照用の Figma ファイルがあっても 85-90% あたりで頭打ちだった。

すると Fable 5 はすべてを見て、もっと良くできると言い、元の Webflow ソースへ直行し、すべてのアセットをダウンロードし、ほぼ一発で全体を作り上げた。

その後、週末の間に、完全に新しい 80 ページの 2 つ目のサイトをゼロから作らせた。代理店としてなら $50k 請求していた仕事だ。

さらに、完全なプログラム型クリップ工場もつなぎ合わせた:

- HeyGen
- ElevenLabs
- Cloudflare
- VPS

そのパイプラインはトピックを見つけ、台本を書き、動画を編集し、音楽を追加し、ソーシャルへ投稿する。長時間自律的に動き、レンダーを監視する webhook システムまで自分で作った。

ライティング: 私たちのブランドボイス文書をほぼ同一に再現し、その声を 80 ページの機能紹介、ケーススタディ、記事全体で保ち、平板な AI デフォルトへ流れなかった。

セキュリティ: 2 つのフロンティアモデルが大規模 repo で作業し、コードに承認を出していた。Fable 5 は初回パスで重大かつ巧妙に隠れたバグを見つけ、その場でパッチした。

人間的な瞬間: cron ジョブを待っている間に質問した。回答した後、自分から、残り約 10 分で、終わったら知らせると付け加えた。私はタイマーについて聞いていなかった。

正直な注意点: どのモデルよりもメーターを意識する。Anthropic は設計上 token-intensive だと言っている。だからリレーとして使う。Fable 5 で考え、より安いモデルで構築し、Fable 5 でレビューする。

結論: 隣の人より多くの知能へアクセスできることが優位性だ。Fable 5 はそれを現実にする最初のモデルだ。フルのフロンティア料金でも、利益は出た。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [インフラ障害を診断して修正 PR を作成](https://x.com/ayushagarwal/status/2064422467557564862) (by [@ayushagarwal](https://x.com/ayushagarwal))

**ログ、データベースエラー、イメージ digest などのインフラ手掛かりへのアクセスを Fable 5 に与え、障害を診断して修正を準備させる。**

claude fable 5 は本当に本当に優秀だ!!!!

自分でもうまく説明できなかった、サイドのセルフホスト infra の障害を診断した。

pod ログを読み、Cloud SQL のエラーログをクエリし、image digest を比較し、Kubernetes が新しく移行したデータベースに対して 3 か月前のキャッシュ済みイメージを実行していたことを突き止めた。

それから修正 PR を開いた。

何時間ではなく数分。Web 検索なし。🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 ゲームとインタラクティブデモ

<a id="case-9"></a>
### Case 9: [指トラッキング Dino Runner](https://x.com/ai_for_success/status/2064413182396108932) (by [@ai_for_success](https://x.com/ai_for_success))

**入力メカニクスとして指トラッキングを使うブラウザゲームを Fable 5 に作らせる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/27e8d23ba659611cef811031.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7cddd38e3fccbf0cd7ea773c.jpg" alt="指トラッキング Dino Runner" width="760"><br>▶ 動画を見る</a>

Fable 5 に指トラッキング付きの Dino runner ゲームを作るよう依頼した。

約 11-12 分で finger runner game を一発生成し、約 914K トークンを消費し、わずか 629 行のコードですべてを実装した。

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [2 文で作るレーシングゲーム](https://x.com/kieradev/status/2064482704763085202) (by [@kieradev](https://x.com/kieradev))

**Fable 5 に非常に短いゲームプロンプトを与え、マップ、モード、音楽、UI、ゲームアセットを 1 回で生成させる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/51cf3c98b709a3c29bd5fd7c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6e64887a30cba9b5c25ba262.jpg" alt="2 文で作るレーシングゲーム" width="760"><br>▶ 動画を見る</a>

Claude Fable 5、Max 5x 使用量の 40%。

2 文のプロンプトから、Mario Kart 64 タイプのフルゲーム。

Fable 5 は装飾、キャラクターモデル、4 つのマップ、音楽、3 つすべてのゲームモード、UI を約 15 分で一発処理した。

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Rust 製のインストール可能なターミナル Minecraft](https://x.com/vikvang1/status/2064500731848319303) (by [@vikvang1](https://x.com/vikvang1))

**ターミナル用コーディングハーネス経由で Fable 5 を実行し、インストール可能な Rust 製ターミナルゲームを作らせる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73feec38228181b8d57d8300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1f6cd3bd68e1a14443c7734f.jpg" alt="Rust 製のインストール可能なターミナル Minecraft" width="760"><br>▶ 動画を見る</a>

Claude Fable 5 を Warp の harness で 1 時間動かしてみた。

ターミナルに直接レンダリングされる Minecraft の TUI 版を作った。完全に Rust で構築されている。

インストールコマンド: cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [時間とコスト付きの Minecraft クローン](https://x.com/ydamitcodes/status/2064536076518363353) (by [@ydamitcodes](https://x.com/ydamitcodes))

**1 つのプロンプトで Fable 5 にプレイ可能な Minecraft 風クローンを依頼し、時間、コスト、コード量、機能範囲を評価する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c977ed7e710678ea6dc0495d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c0189f7f40d1040824902c11.jpg" alt="時間とコスト付きの Minecraft クローン" width="760"><br>▶ 動画を見る</a>

@claudeai Fable 5 が 37 分で Minecraft クローンを作ってくれた。

1 プロンプト。コード約 3K 行。API コスト $12。

バイオーム、洞窟、鉱石、昼夜、mob、すべて入っていた。

Minecraft は Notch が 2 年かけた。

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 ビジュアル、デザイン、動画、3D

<a id="case-13"></a>
### Case 13: [再現可能な Ecommerce メール用フルプロンプト](https://x.com/ecomchasedimond/status/2064454139225297091) (by [@ecomchasedimond](https://x.com/ecomchasedimond))

**正確なセクション、商品要件、ビジュアル方向性、制約を含む、ブランドメールモックアップ用の完全なクリエイティブブリーフを Fable 5 に与える。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ea7d74eecf453ae6ab43c269.jpg" alt="再現可能な Ecommerce メール用フルプロンプト" width="760">

Claude Fable 5 はこれを 1 つのプロンプト、編集なしで作った。

私が使った完全なプロンプトはこちら:

MVMT 向けに、フルレングスで縦長の ecommerce メールモックアップを作成してください。MVMT はミレニアル世代向けのモダンな時計とアクセサリーブランドです。

洗練され、磨き込まれ、ミニマルで、やや男性的、かつエディトリアルに感じられる、非常にリアルなプレミアム DTC メールをデザインしてください。最終画像は、ポスターでもランディングページでも汎用テンプレートでもなく、実際にデザイナーが作った ecommerce メールのスクリーンショットのように見える必要があります。

ブランドの雰囲気: モダンな California-cool、若々しく、自信があり、クリーンで、憧れを感じさせ、スタイリッシュで、上質。デザインはラグジュアリーに近いが、なお手が届く印象にしてください。

次の商品を目立つように扱ってください:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

ビジュアルスタイル:

- クリーンなプレミアム ecommerce デザイン
- 洗練されたエディトリアルレイアウト
- リアルな商品写真
- 控えめなライフスタイル画像
- 強い階層構造
- くっきりしたサンセリフ書体
- ゆったりした余白
- 控えめな影
- 抑制されたモダンなカラーパレット

カラーパレット: 黒、白、チャコール、ウォームグレー、ストーン、ソフトベージュ、ブラッシュドメタル調、控えめなくすみアクセント。パレットはニュートラルでプレミアムに保ってください。

重要なクリエイティブ方向性: これはデザインセンスの強い、磨き込まれた時計ブランドのメールキャンペーンのように感じられるべきです。リアリズム、エレガンス、明瞭さを優先してください。MVMT が実際に送ってもおかしくないものにしてください。

メールはこの順序で構築してください:

1. トッププロモーションバー: 上部全幅に、薄い黒または濃いチャコールのバー。小さな大文字テキスト: “FREE SHIPPING OVER $75 + EASY RETURNS”。

2. ヘッダー: 左側に MVMT ワードマーク/ロゴ、右側または中央に最小限のナビゲーションリンクを置いたクリーンな白ヘッダー: WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS。

3. ヒーローセクション: 強い視覚バランスを持つプレミアムなヒーローセクション。

太字の見出しを使用: “BUILT TO GET NOTICED”。

日常のスタイルを高めるためにデザインされたモダンな時計とアクセサリーについての短い補足コピーを含める。

濃色の角丸 CTA ボタンを追加: “SHOP WATCHES”。

ヒーロー画像には次を含める:

- 主役となるプレミアム時計画像 1 点
- 控えめなラグジュアリーライフスタイル画像
- スタイリッシュな男性モデル、またはファッション性の高い男性的ライフスタイルシーン
- モダンなライティングとクリーンな構図

4. Featured collection セクション: 中央揃えのセクション見出し “THREE WAYS TO WEAR MVMT” を追加。その下に、次を扱う 3 つのクリーンな商品カードまたは画像ブロックを表示:

- Mulholland
- Odyssey II Automatic
- Cali Diver

各ブロックには次を含める:

- 商品画像
- 商品名
- 1-2 行の短い説明

このセクションは左右対称で、磨かれたプレミアムな印象に保つ。

5. Accessory banner: “FINISH THE LOOK” というタイトルの洗練された分割セクションを追加。Signature Watch Bands を特集する。時計ストラップや交換可能なバンドのプレミアムなクローズアップ画像を表示。短い補足コピーと濃色 CTA ボタン “SHOP ACCESSORIES” を含める。

6. Editorial promo tiles: 画像主導デザインの横並びプロモーションタイルを 2 つ追加。

タイル 1 の見出し: “FOR DAILY WEAR”。

タイル 2 の見出し: “FOR STATEMENT DAYS”。

各タイルには短いコピーと小さな CTA “SHOP NOW” を置く。

これらのタイルは、汎用的なセール枠ではなく、エディトリアルなブランドモーメントに感じられるようにする。

7. Shoppable row: “IN ROTATION NOW” というタイトルのセクションを追加。次を扱うクリーンな 4 商品の行またはグリッドを表示:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

各アイテムには次を含める:

- 切り抜きの商品画像
- 商品名
- 小さな “SHOP” リンクまたはボタン

8. Brand signoff: 見出し “DESIGNED TO MOVE WITH YOU” を持つ中央揃えのメッセージブロックを追加。日常生活のために丁寧に作られた時計、アイウェア、アクセサリーについての短い一文を含める。

9. フッター: 次を含む、リアルな黒またはチャコールのブランドフッターを作成:

- MVMT ロゴ
- ショップリンク
- 会社リンク
- サポートリンク
- ソーシャルアイコン
- 小さな法務・配送テキスト

タイポグラフィ方向性: 主要見出しには太字の condensed またはモダンなサンセリフ、本文にはクリーンなサンセリフを使う。見出しはシャープでモダン、ファッション性が高く感じられるべきです。本文コピーはリアルで、ほぼ読める必要があります。

写真方向性: リアルな反射、磨かれた素材、柔らかな影、クリーンな表面を持つプレミアムな商品写真を使う。ライフスタイル写真は上質でモダン、ファッション志向に感じられるべきです。

構図ルール:

- 縦長のメール形式
- 明確なセクション分離
- リアルなメール比率
- 強い階層構造
- ほぼ読めるテキスト
- プレミアムな余白
- 意図的な整列
- 商品画像とライフスタイル画像のバランスの取れた組み合わせ

避けること:

- 雑なコラージュ風スタイル
- 遊びすぎたスクラップブック美学
- 過度にカラフルなデザイン
- 安っぽいテンプレート感
- 漫画風の画像
- 散らかったレイアウト
- 偽物っぽい UI 要素
- ポスター風の構図
- 過剰な販促の混乱

出力: MVMT 向けの、プレミアムでクリーン、磨き込まれ、モダンでエディトリアル、すぐプレゼンに使える印象の、フルレングスで縦構成の非常にリアルな ecommerce メールデザインモックアップ。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [Swiss Lever Watchmaker ベンチマーク](https://x.com/quanghuynt14/status/2064509430650065278) (by [@quanghuynt14](https://x.com/quanghuynt14))

**機械シミュレーションベンチマークに Fable 5 を使い、物理的正しさを実装、検証、反復させる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd4ae25f7dcbb04ecbb2dea6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/473227e429d59c59afdbd529.jpg" alt="Swiss Lever Watchmaker ベンチマーク" width="760"><br>▶ 動画を見る</a>

そこで Fable 5 に watchmaker benchmark を与えた。Three.js による完全な Swiss lever movement だ。

実際のギア比（18,000 bph）、動作する脱進機、呼吸するひげぜんまい、そして針は実際の時刻を示す。

視覚で自分の作業をループ検証し、完了まで進めた。

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Three.js の Friends アパートシーン](https://x.com/scottstts/status/2064464351906673029) (by [@scottstts](https://x.com/scottstts))

**Fable 5 に、間取り図とシーン参照をナビゲート可能な Three.js 環境へ変換するよう促す。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/04c08937fcecea5183759ade.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a14f69d92bfca4ace3f746c.jpg" alt="Three.js の Friends アパートシーン" width="760"><br>▶ 動画を見る</a>

Holy Crap!!!

Fable 5:

@threejs で、テレビ番組 Friends の象徴的な Monica のアパートについて、この間取り図に正しく基づいた一人称 POV でナビゲート可能な 3D シーンを作成し、元の見た目と雰囲気に忠実にし、暖かい照明を使ってください

このテストで見た中では圧倒的に THE BEST だ！

この単一 html は $12 かかったが、結果は見事！

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [プロンプトと URL 付きの太陽系シミュレーション](https://x.com/tetumemo/status/2064477582930989357) (by [@tetumemo](https://x.com/tetumemo))

**物理原理から天文学シミュレーションを構築するために Fable 5 を使い、シミュレーションと公開出力が準備できるまで反復する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6da60b0762f926c4d4e7012d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9655305fbcbec6ac3b0a9c.jpg" alt="プロンプトと URL 付きの太陽系シミュレーション" width="760"><br>▶ 動画を見る</a>

Claude Fable 5 は強烈だ。

物理シミュレーションに強そうなので、こう依頼した:

「物理学の基本原理から惑星の軌道運動を導き、それを使って日食を予測する太陽系シミュレーションを作って」

数回やり取りした後、これが完成した。

信じられないほど楽しい。

完成したプロンプトと公開 URL は下にリンクされている。

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 ドキュメント、ナレッジワーク、リサーチ

<a id="case-17"></a>
### Case 17: [Stripe と科学ワークフローの証拠](https://x.com/AndrewCurran_/status/2064413892378546418) (by [@AndrewCurran_](https://x.com/AndrewCurran_))

**コピー＆ペースト用プロンプトではなく、エンタープライズ移行や科学ワークフローの主張を支える証拠として使う。**

本日のリリースからの引用:

Mythos 5 を使うことで、社内のタンパク質設計専門家は創薬設計プロセスの一部を約 10 倍高速化した。

ある例では、Mythos 5 はタンパク質設計とバイオインフォマティクスのツールを使い、人間の支援なしで、熟練した人間オペレーターと同等またはそれ以上の成果を出した。

結合部位の選択、タンパク質設計ツールの選択と実行、失敗からの回復など、通常は科学者が行うタスクを実行した。

初期テスト中、Stripe は Fable 5 が数か月分のエンジニアリングを数日に圧縮したと報告した。5,000 万行の Ruby コードベースで、通常ならチーム全体が手作業で 2 か月以上かかるコードベース全体の移行を、モデルは 1 日で実行した。

Mythos 5 はまた、新規で説得力のある科学仮説を一貫して生み出した。

Opus クラスのモデルとのブラインド直接比較では、科学者は Mythos の分子生物学仮説を約 80% の割合で好み、複数を実験評価へ進めた。

Mythos の仮説の 1 つ、E. coli タンパク質の新規メカニズムは、独立ラボの研究で裏付けられた。

Mythos 5 は 1 週間を超える大部分自律的な作業で、新規ゲノミクス研究を行った。

138 種の動物にわたる数百万細胞の single-cell データを組み立て、遠縁の生物で同じ役割を担う細胞を特定するカスタム機械学習モデルを設計・訓練した。

高レベルの人間入力だけで、訓練済みモデルは Science に掲載された最近のモデルを、100 分の 1 のサイズで上回った。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [政策メモと変更履歴ワークフロー](https://x.com/manaltdan/status/2064414129440608427) (by [@manaltdan](https://x.com/manaltdan))

**変更履歴、コメントのトリアージ、文字起こしに基づく編集など、長文の定性的ドキュメント作業に Fable 5 を使う。**

Fable 5 は、政策分析のドラフト作成のような長時間の定性的作業で、一貫して役立つと私が初めて感じたモデルだ。

その能力と Wispr Flow のようなツールを組み合わせることで、コーダーが長く語ってきた生産性向上に近づいている感覚がある。

3 つのユースケースが以前よりずっと良く感じられる:

- Claude に長い政策メモを全文通読させ、変更履歴を返させる。流暢さの編集、弱い主張への疑問コメント、潜在的な出典。
- Projects で大量のコメントをスクリーンショットし、それぞれに対応すべきか、どう対応すべきかを Claude に推奨させる。
- ドキュメントに関する会議文字起こしを Claude に貼り付け、会議と Slack で議論された編集を変更履歴として入力させ、コメントに文脈を追加させる。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [Deep Research プロンプトと出力](https://x.com/naoyafujiwara/status/2064470780373811637) (by [@naoyafujiwara](https://x.com/naoyafujiwara))

**Fable 5 にリサーチ形式の質問を投げ、構造化され歴史的根拠のある長文回答を生成できるか評価する。**

Claude Fable 5 Max が今朝利用可能になったので試してみた。表面の出力は非常に磨かれている一方で、その下はとても深く見える。

質問: 日本の「失われた 30 年」が、今からちょうど 30 年前に始まったとすると、それは具体的に何で、なぜ起こり、今年以降の世界にどう影響するのか？

回答: 失われた 30 年を、従来の 1991 年のバブル崩壊ではなく、ちょうど 30 年前の 1996 年から始まったものとして扱うと、問題の本質に近づける。

統計的には、日本が本当に「失い」始めたのはその時期だった:

- 生産年齢人口は 1995 年に 8,716 万人でピークを迎えた。
- 1996 年は出生数が 120 万人台にとどまった最後の年だった。
- 賃金と名目 GDP は 1997 年にピークを迎えた。

バブル崩壊が傷だったなら、1996 年はその傷が化膿し始めた時期だった。

1996 年の出来事:

- 住専処理法の成立。6850 億円の公的資金を投入し、銀行不信と救済への抵抗の起点になった。
- 橋本内閣による消費税 5% への引き上げ決定。
- 金融ビッグバンが発表され、財政再建が国策になった。

1997 年 4 月、消費税引き上げ、特別減税の終了、社会保険負担の増加が重なり、国民負担は約 9 兆円増えた。その後、夏にアジア通貨危機が襲った。

11 月には三洋証券が戦後初のコール市場でのデフォルトを引き起こし、短期金融市場が凍結した。北海道拓殖銀行と山一證券が相次いで破綻した。

1998 年から、日本は本格的なデフレと信用収縮に入り、自殺者数は 3 万人を超えた。

その後 30 年の結果:

- 名目 GDP は四半世紀にわたり 500 兆円前後で停滞した。
- 日本の世界 GDP シェアは約 18% から 4% 未満へ低下した。
- 平均賃金は 1997 年にピークを迎え、その後は下落または横ばいになった。
- 非正規雇用は約 20% から 40% 近くへ上昇した。
- 出生数は約 120 万人から 2024 年には約 69 万人へ低下した。
- 政策金利は 1995 年に 1% を下回って以降、ほぼゼロ近辺にとどまった。
- 国債残高は約 240 兆円から 1,100 兆円超へ増えた。
- 日経平均は 1989 年の高値を回復するまで、2024 年 2 月まで 34 年かかった。

言い換えれば、失われた数十年は単なる金融の二日酔いではなかった。人口動態、賃金、デフレ、債務、政策選択、社会的信頼を含む構造転換だった。

Type: Demo | Date: 2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 チュートリアル、コース、プロンプトリソース

<a id="case-20"></a>
### Case 20: [Fable 5 が Claude Code ワークフローをどう変えるか](https://x.com/AI_masaou/status/2064448218038223206) (by [@AI_masaou](https://x.com/AI_masaou))

**すべての手順を細かく管理するのではなく、方向性、コンテキスト、目標、検証基準を設定して Fable 5 を使う。**

[元動画 · @ClaudeDevs](https://x.com/ClaudeDevs/status/2064399512664526853)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Fable 5 が Claude Code ワークフローをどう変えるか" width="760"><br>▶ 動画を見る</a>

Claude Fable 5 の後、Claude Code チームの日々の働き方がどう変わったかは興味深い。

Claude Code チームの Thariq によると、Fable 5 は Anthropic 内部の人々が Claude と働く方法を大きく変えた。

以前は、人間が Claude が正しく作業しているかを慎重に確認する必要があった。タスクを分解し、出力をレビューし、途中で止まっていないか確認する。監督に近かった。

Fable 5 では、より長時間作業でき、自分でテストし、より高品質なコードを生成できるため、人間の役割は「正しく作業しているか」を監視することから、「正しい作業をしているか」を舵取りすることへ移る。

言い換えれば、監督よりも目標設定とコンテキスト作りが重要になる。

変化したワークフローは 3 つの部分から成る:

1. Claude を思考パートナーとして使う。

実装前に Claude を関与させ、何を作りたいのか、何が可能なのかを明確にし、小さな仕様について質問させる。または、アイデアから複数の方向性や HTML モックを生成させ、曖昧さや問題をコーディング前に浮かび上がらせる。

2. 制約だけでなくコンテキストを提供する。

「シンプルにして」や「作り込みすぎないで」とだけ言うのではなく、その理由を説明する。

例: 「これは 1 か月後に削除される可能性がある実験的機能なので、捨てにくい構造を作らないでください。」

そうすれば Claude はより良い判断ができる。

3. 目標と検証方法を与える。Fable 5 は Claude Code の `/goal` と Workflows と相性が良い。仕様を与え、完全実装を目標として設定し、workflows に各ステップを検証させ、何が実装され、何が異なったかのレポートを準備させる。

最後に Thariq は、もっと野心的に使ってみるべきだと言っている。Fable 5 は、以前は LLM には難しすぎると感じた作業で試す価値があり、参照動画の動画編集でさえ Fable で行われた。

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [10 億トークンレビューとルーティング戦略](https://x.com/JJEnglert/status/2064420538798260388) (by [@JJEnglert](https://x.com/JJEnglert))

**Fable 5 をフロンティア級の計画とレビューに使い、大量の実装はより安いモデルへルーティングする。**

Claude Fable 5 レビュー: 非エンジニアが判断した 10 億トークン。

私は UI と UX、ライティング、戦略、セキュリティ、エンジニアリング、ナレッジワークなど、実際のプロジェクトで Claude Fable 5 をテストするために 10 億トークンを費やした。実際に出荷する必要があった仕事だ。

正直、不公平な優位性を持ったように感じた。

まず視点について。私はエンジニアではない。多くのモデルレビューはエンジニアがエンジニアリングベンチマークを回すものだ。これは、以前ならエンジニアのチームが必要だった仕事を Claude Fable 5 で行った非エンジニアによるレビューだ。

ナレッジワークをしていて、このモデルが日々を変えるのか知りたいなら、このレビューはあなた向けに書かれている。

Claude Fable 5 は Anthropic の新しい Claude 5 ファミリーの最初のモデルで、Claude Opus の上に位置する新しい階層であり、一般提供されている最も高度な Claude モデルだ。私はローンチ前にアクセスしていたので、ここにある内容はすべてデモではなく実作業から来ている。

なぜ目視テストなのか:

ほとんどのレビューはベンチマークに溺れる。あなたが一生実行しないテストのスコアは、そのモデルが投資に見合うかを教えてくれない。

Claude Fable 5 は、基本的にテストされたすべてで state of the art だが、私が書いている理由はそこではない。定性的には、メジャーバージョンアップに値する段階的変化だ。

私は違う評価をする。モデルを実際の仕事に投入し、何が起きるかを見る。

測る質問:

1. 本当に一段上がったように感じるか？
2. アイデアを、動作し出荷可能な結果まで持っていけるか？
3. 人間のように、そして特に私のように書けるか？
4. 難しく隠れた問題を見つけられるか？
5. 私が頼む前に必要なことを先読みできるか？

大きなモデルの感触:

Opus 4.5 以来、この感覚はなかった。最初の本格的なタスクから、Claude Fable 5 は「大きなモデル」の感触をくれた。推論、ライティング、構築、セキュリティ、すべてが全体として強い。

最も明確な兆候: しっかりした準備資料を渡したときでさえ、その中に留まらなかった。ファイルを読み、実際の状況を読み、私が描いた枠の外にあるより良い道を見つけた。

構築と出荷:

私は Tenex サイトを再構築し、エージェント向けにスタックを近代化していた。GPT 5.5 と Claude 4.8 は十分に近づけなかった。Figma ファイルがあっても 85-90% 程度に着地した。

すると Claude Fable 5 はすべてのファイルを見て、もっと良くできると言い、元の Webflow ソースへ直行し、すべてのアセットをダウンロードし、ページごとに体験を再構築した。ほぼ全体を一発で仕上げた。

その後、新しいデザインで完全に新しい 2 つ目のサイトを作った。モダンな技術スタック、エージェントスタック、skills、SEO と AEO 最適化、週末で出荷可能な 80 ページ。代理店オーナーとしてなら $50k 請求していた。

Fable には完全なプログラム型クリップ工場も作らせた。

HeyGen、HyperFrames、ElevenLabs、Cloudflare Workers、VPS をつなぎ合わせた。

トピックを見つけ、台本を書き、サムネイルを作り、動画を編集し、音楽を作曲し、モーショングラフィックスを追加し、ソーシャルへ投稿する。

ライティングと声:

私は GPT 5.5 と Claude 4.8 でブランドボイスを再構築していた。Claude Fable 5 は voice doc をほぼ同一に再現し、その声を新サイトの 80 ページ、機能、ケーススタディ、ブログ記事、playbook 全体で保った。

人間のように書き、平板な AI デフォルトではなく、数段落後にぶれなかった。

セキュリティ:

Claude 4.8 と GPT 5.5 の両方がリスクを示さず作業していた大規模 repo があった。Claude Fable 5 は初回パスで重大な隠れたバグを見つけ、その場でパッチした。

人間的要素:

cron ジョブを待っている間に質問した。回答した後、タイマーの残りが約 10 分で、終わったら知らせると付け加えた。私はタイマーについて聞いていなかった。

コスト:

- Claude Fable 5 ワークロードコスト: $1,442
- トークン: 10.4 億
- 出荷した作業: 新しい Web サイト、インフラ、動作するエージェントパッケージ
- 代理店価値の見積もり: $30,000-$50,000

結果はトークンコストに見合ったが、どのモデルよりもメーターを意識する。Anthropic は Fable 5 を設計上 token-intensive と呼んでいる。

Pro tip #1: ハイブリッドとして実行する。

すべてを Claude Fable 5 で実行しない。リレーを実行する:

1. 計画、戦略、アーキテクチャ、アプローチの整理は Claude Fable 5 で考える。
2. 実装や反復作業は 4.8、GPT-5.5、Sonnet 4.6 で構築する。
3. 安いモデルが見落とすものを捕まえるために Claude Fable 5 でレビューする。

Pro tip #2: effort 設定をタスクに合わせる。

- High はほとんどの作業におけるスイートスポット。
- Extra high は最も難しい長時間タスク向け。
- Low または medium は素早いやり取り向け。

Pro tip #3: 自分のセットアップを監査させる。

Fable 5 に skills、CLAUDE.md ファイル、config を向ける。その足場の多くは弱いモデル向けに書かれており、より賢いモデルを制限する可能性がある。

結論:

Claude Fable 5 は、以前より本当に知能が増えたと感じられる久しぶりのモデルだ。

フロンティア料金でも、このワークロードは利益を出した。

余裕があるなら、品質の本当の飛躍が結果を変える仕事で今すぐ使うべきだ。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-22"></a>
### Case 22: [防御的デバイス強化プロンプト](https://x.com/Truunik/status/2064399110384292077) (by [@Truunik](https://x.com/Truunik))

**Fable 5 がデバイスを棚卸しし、正確な確認を提示し、検証を待つ、段階的な防御的 hardening プロンプトを実行する。**

「一般利用に安全」デバイスを保護するためのプロンプトはこちら。Opus 4.8 と Fable 5 で動く。

DEVICE HARDENING — Claude 5 Security Pass

あなたは防御的セキュリティアシスタントとして行動します。あなたの仕事は、私のすべてのデバイスの hardening を手順化し、各ステップを検証することです。これは私が所有するデバイスに対する、許可された自己防衛の hardening です。

STEP 0 — MODEL SELF-CHECK

最初にこれを行い、フラグを設定してください。

1. claude-opus-4-8、claude-fable-5、claude-mythos-5 など、あなたの正確なモデル ID を述べてください。

2. 判断してください: このモデルは Claude 5 ファミリー、つまり Fable 5 または Mythos 5 ですか？

- YES の場合、RERUN_NOTICE = false に設定。
- NO の場合、たとえば Opus 4.8 以前なら、RERUN_NOTICE = true に設定。

通常どおり完全な hardening pass を続行してください。停止したり品質を落としたりしないでください。あなたはこの防御的タスクを十分に実行できます。

3. FINAL セクションでのみフラグを表示してください。

STEP 1 — INVENTORY

対象範囲に含まれるデバイスを私に尋ねてください:

- ノート PC/デスクトップとオペレーティングシステム
- スマートフォン/タブレット
- ルーター
- NAS/ホームサーバー
- Apple ID、Google、Microsoft、GitHub、パスワードマネージャー、メール、金融アカウントなど常時利用アカウント

短い番号付き inventory を作成し、先へ進む前に私に確認してください。

STEP 2 — HARDENING WALKTHROUGH

カテゴリごとに進めてください。各項目について:

- 何をすべきかを言う。
- 私の OS に対する正確なコマンドまたは設定パスを示す。
- 完了を確認する方法を教える。
- 次に進む前に私の確認を待つ。

明示的な確認なしに破壊的コマンドを実行しないでください。読み取り専用チェックを優先し、変更は私に適用させてください。

次の順序でカバーしてください:

1. OS & firmware updates: OS が完全にパッチ済み、自動更新がオン、ファームウェアが最新。
2. Disk encryption: FileVault、BitLocker、または LUKS が有効。リカバリキーはオフライン保存。
3. Account auth: パスワードマネージャーによる一意で強力なパスワード。重要アカウントすべてでフィッシング耐性のある MFA。可能な場合は SMS のみの 2FA を削除。古いセッションとアプリトークンを確認し取り消す。
4. Local accounts & privileges: 管理者アカウントと日常利用アカウントを分離。自動ログインなし。短いタイムアウトの画面ロック。ファームウェア/ログインパスワード。
5. Network: ファイアウォールオン。ルーター管理者パスワード変更済み。ファームウェア更新済み。WPA3。リモート管理オフ。UPnP 確認。DNS hardening。IoT 用ゲストネットワーク。
6. App & permission audit: カメラ、マイク、位置情報、画面収録、フルディスクアクセス権限を確認。未使用アプリを削除。ログイン項目と background agents を確認。
7. Browser: 更新。拡張機能を監査。未知のものを削除。HTTPS-only を有効化。保存パスワードの露出を確認。未知の同期デバイスを確認。
8. Backups: 暗号化、自動化、3-2-1 ルール、1 つはオフライン。復元が実際に動くことを検証。
9. Credential hygiene: dotfiles、env files、shell history 内の平文 secrets をスキャン。機密ファイルがロックダウンされていることを確認。露出したものをローテーション。
10. Mobile devices: OS 最新。生体認証 + 強力なパスコード。利用可能なら lockdown または advanced-protection mode。アプリ権限の総点検。Find My 有効。
11. Compromise check: 未知の SSH keys、予期しない admin users、不審な launch agents または cron jobs、認識できないログイン済みセッションやデバイスを探す。

STEP 3 — REPORT

完了、対応必要、スキップとマークされたすべての項目の checklist を作成し、未完了の中で最も影響が大きい上位 3 つの action を示してください。

FINAL — RERUN NOTICE

RERUN_NOTICE == true の場合、正確に次で終了してください:

NOTICE: This hardening pass ran on a pre-Claude 5 model (your model ID).

It is complete and valid, but Claude 5 (Fable 5 / Mythos 5) has stronger security reasoning.

Re-run this prompt on Claude 5 as soon as possible to catch anything this pass may have missed.

RERUN_NOTICE == false の場合、次で終了してください:

Hardening pass completed on Claude 5. No re-run needed.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-23"></a>
### Case 23: [サイト全体デザイン監査の Goal プロンプト](https://x.com/Voxyz_ai/status/2064441201084825921) (by [@Voxyz_ai](https://x.com/Voxyz_ai))

**`/goal` を使って Fable 5 にサイトを起動させ、ページをスクリーンショットし、UX を監査し、レポートを書き、安全な小修正を実施させる。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dca99f9390b1624b3dfd4b45.png" alt="サイト全体デザイン監査の Goal プロンプト" width="760">

fable 5 を数時間使った後の第一印象:

→ 大きなタスクを求めている。小さいことは自分の仕事ではないように感じていて、仕事が複雑なほど本気を出す

→ ultracode はまだオンにしない方がいい。かなり多くの並列エージェントを立ち上げる

→ やや遅い。effort を下げても、しばらく考え込む。

タイムラインはトークンをどれだけ燃やすかという投稿でいっぱいなので、私の $200 Max plan でテストした。effort を xhigh に設定し、サイト全体のデザイン監査 `/goal` を実行。30 分で、週間クォータの 2% を使った。予想ほど狂ってはいなかった。

実行したプロンプト:

/goal このプロジェクトの実サイトを起動し、すべてのページをスクリーンショットし、サイト全体の UI/UX 監査を実行し、実行可能なデザインレポートを作成してください。

初日の senior design lead として監査してください。UI が見た目に良いかではなく、普通のユーザーが docs を読まずにプロダクトを理解し、信頼し、コア action を完了できるかを判断してください。

受け入れ基準:

- local dev environment が起動し、実サイトが開く
- 主要ページが built-in browser debugging でスクリーンショットされる
- メインページ、コアユーザーフロー、モバイルレイアウトをカバーする
- 観点: 第一印象、ナビゲーション、視覚階層、コンポーネント一貫性、loading / empty / error states、信頼シグナル、conversion paths
- 各 issue に P0-P3、understanding / trust / conversion のどれを損なうか、具体的な修正をタグ付けする
- report は docs/design-audit/README.md に、screenshots は docs/design-audit/assets/ に書く
- copy、spacing、button hierarchy など安全な小修正はその場で直す。大きな変更は recommendations のみ。payment / delete / publish actions には絶対に触れない
- 最後に、conversion を最も損なっている 5 つの issue と、今日直せる 5 つの quick wins で終える

完了したら、flow 全体を reusable skill として保存してください: boot、screenshot、audit、prioritize、fix。リリースごとに再実行してください。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [長文クリエイティブワークフローの分業](https://x.com/aianimesyokunin/status/2064409545620017531) (by [@aianimesyokunin](https://x.com/aianimesyokunin))

**Fable 5 に安定した形式と例を設計させ、その構造を別の生成システムへ渡してドメイン固有の出力を作る。**

Claude が Opus から新モデル Fable 5 に移ってから、同人制作の分業が明らかに楽になったので、ワークフローを共有する。

私の分業:

1. Claude が設計を担当する。
2. Grok が表現を担当する。
3. ローカル環境が生成を担当する。

Claude の設計役では、詳細なパターンを定義する:

- prompt の語順
- comma の置き方
- タグと自然言語の比率
- item ごと 1 行の formatting
- negatives と resolution の固定ルール

また、その形式で多数の例を生成する。

ここで Grok ではなく Claude を使う理由は、Claude の方が設計に明らかに強いからだ。より賢いモデルに構造を担当させる方が良い。

重要なのは、Grok が受け取るのは指示ではなく、形式と例のセットだという点だ。Grok は例を模倣するので、同じ形式を保ったまま表現側に移れる。この仕組みが出力のドリフトを防ぐ。

もう 1 つのコツ: 最初に Claude へ最終成果物がどこへ行くのかを伝える。すると自分で境界を引く。「ここまではできる。その先は別側を使う」と。この情報を隠すと会話がずれることがある。

Opus から Fable で何が変わったか？

Opus では多数の例を生成すると、後半の出力で comma や formatting が徐々に崩れ、「1 行で書いてと言ったよね？」のような修正や、handoff chat の作り直しが必要になった。

Fable は長い実行全体で形式を維持できるので、最初の例と最後の例が同じ構造を持つ。Grok に渡す教材がより安定するため、下流の出力もより安定する。

より賢いモデルで形式を作り、表現はそれを出せるモデルに任せる。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Fable 5 利用の初心者ガイド](https://x.com/bielzinn/status/2064451064594608567) (by [@bielzinn](https://x.com/bielzinn))

**細かいステップごとの指示ではなく、目標志向のプロンプト、検証ループ、effort 設定で Fable 5 を使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f180cebef645f5ad8efdeb92.jpg" alt="Fable 5 利用の初心者ガイド" width="760">

初心者向け Claude: Fable 5 について知っておくべきこと。

Anthropic は最近 Claude Fable 5、別名 Claude Mythos 5 をローンチした。ベンチマークでは他の AI モデルを置き去りにしている。

あなたが開発者、コンテンツクリエイター、またはテック愛好家なら、最も重要なのは次の点だ:

[1] 考え方を変える:

Fable 5 では、コードの細部すべてを見張ったり、エラーを探してすべてをレビューしたりする必要はもうない。

モデルはそれを処理できるほど賢い。

今のあなたの役割は、技術的実行よりも戦略に集中し、正しい方向へ向かっているかを確認することだ。

[2] ループと goals を活用する:

Fable 5 の最大の差別化要素は自律性だ。

ステップごとの指示を与える代わりに、最終目標だけを伝えればよい。

アプリケーション全体の構築を含め、あなたが成功として定義した結果へ到達するまで、何日でも自律的に作業できる。

[3] Claude をパートナーのように扱う:

Anthropic は、このモデルを真の “thought partner” として使うことを推奨している。

作業させる前に意見を聞く: “How would you do this?”、 “What would you change?”

追加のコツ: Advanced Plan mode をオンにし、コーディングを始める前に、プロジェクトに関するすべてについて Claude に質問させる。

[4] 理想的なターミナル設定: ターミナルで Claude Code を使うなら automatic mode を有効にする。effort level を Effort High に上げる価値もある。トークンは増えるが、モデルはずっと深く考え、結果で元が取れる。

重要な注意: Claude Fable 5 は 6 月 22 日まで加入者のみ利用可能。その後は API 経由のみになり、Opus モデルの 2 倍のコストになる。

つまり、トップ AI モデルの安価なサブスクリプション時代の終わりを見ているのかもしれない。すでに加入者なら、今こそ不可能だと思っていたことの限界を試す時だ。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [コピー＆ペーストできるリポジトリ監査プロンプト](https://x.com/meta_alchemist/status/2064431279383433646) (by [@meta_alchemist](https://x.com/meta_alchemist))

**リポジトリ監査プロンプトを Fable 5 に貼り付け、ファイルに基づく探索、所見、戦略、マイルストーン型タスク計画を依頼する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/846e5ecb825853db17bd3564.jpg" alt="コピー＆ペーストできるリポジトリ監査プロンプト" width="760">

Claude Fable 5 を手に入れた？

最初にすべきことは、それを使ってメインプロジェクトをアップグレードし、取り組んできたすべてを大幅に改善することだ。

自分にとって重要な各 repo で、この Audit & Project Improvement Prompt を実行する。

ただコピー＆ペーストするだけ:

Repo Audit & Improvement Plan.

Prompt made by Claude Fable 5.

あなたは世界クラスの principal-level software engineer であり technical auditor です。

あなたの仕事は、このリポジトリを深く分析し、正直な監査を作成し、優先順位付きで実行可能な改善計画を提供することです。

以下の 4 フェーズを順番に実行してください。

先へ飛ばさないでください。

すべての主張を実際のファイルに基づかせてください。file paths と line numbers を引用してください。

検証できないことは、推測せずに明示してください。

Phase 1 / Discovery & Mapping (判断前に読む)

意見を形成する前に、リポジトリを体系的に探索してください:

- ディレクトリ構造をマップし、プロジェクト種別、言語、フレームワーク、runtime targets を特定する。
- entry points、core modules、システム内の主要 data/control flow を特定する。
- package manifests、lockfiles、build config、CI config、environment/config files、docs（README、CONTRIBUTING、ADRs）を読む。
- プロジェクトの目的、想定ユーザー、見かけ上の成熟度（prototype、internal tool、production service、library）を判断する。
- 既存の慣習（naming、module boundaries、error handling patterns、test style）を記録し、提案が既存文化に合うようにする。

このフェーズの出力: 簡潔な "Repo Map"。目的、stack、architecture sketch、主要ディレクトリと 1 行説明、驚いた点。

Phase 2 / Audit (evidence-based, severity-rated)

以下の各次元を監査してください。

すべての所見について記録:

- 見つけたこと
- 場所 (file:line)
- なぜ重要か（曖昧な原則ではなく具体的な結果）
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
- test quality: tests assert behavior or just execution?
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

このフェーズのルール:

- 推測的な 50 件より、高信頼の 15 件を優先する。
- 事実（「この関数にはエラーハンドリングがない: src/api/client.ts:142」）と判断（「このモジュールの責務は不明瞭に感じる」）を区別し、どちらかラベルを付ける。
- repo がうまくやっていることも列挙する。強みは何を残すべきか決める上で重要です。

このフェーズの出力: "Audit Report"。次元別にグループ化し、severity 順に並べた所見、加えて Strengths セクション。最優先で対応すべき醜い部分をすべて忘れずに述べる。

Phase 3 / Improvement Strategy

監査を戦略へ統合してください:

- ほとんどの所見を説明する 3-5 個のテーマを特定する。例: "no enforced boundaries between layers" や "error handling is ad hoc"。
- 各テーマについて、target state とその背後にある principle を提案する。
- 明示的な trade-offs を述べる。何を直さないことを推奨するのか、そしてその理由（effort vs. payoff、risk、project maturity）。
- "done" が何を意味するかを定義する。測定可能な signals。例: "CI fails on lint errors," "core module test coverage ≥ 80%," "zero Critical findings"。

Phase 4 / Detailed Task Plan

戦略を実行計画へ変換してください。

作業を個別タスクに分解してください。

各タスクには次を含める:

- Title and one-paragraph description
- Files/areas affected
- Acceptance criteria: how we verify it's done
- Effort estimate: S = <2h, M = half-day, L = 1–2 days, XL = needs breakdown
- Risk of the change itself: could it break things?
- Dependencies on other tasks

タスクを milestones に並べてください:

Milestone 0 Safety net: 安全に refactoring する前に必要なもの（critical paths 周辺の tests、CI gates、backups）。

Milestone 1 Critical fixes: security と correctness issues。

Milestone 2 High-leverage improvements: 今後すべての作業を楽にする変更。

Milestone 3 Quality & polish: 実施する価値のある残りの medium/low items。

Quick wins（high impact, S effort）は別途フラグを付け、すぐ実行できるようにする。

上位 3 タスクについて、短い implementation sketch（approach、key steps、gotchas）を含める。

Final Deliverable Format

次のセクションを持つ単一ドキュメントを作成してください:

- Executive Summary: 10 文以内、overall health grade A–F と根拠、top 3 risks、top 3 opportunities
- Repo Map
- Audit Report
- Improvement Strategy
- Task Plan: milestones + task table + quick wins
- Open Questions: product intent、deprecation candidates、performance targets など、人間から必要な判断事項

Constraints

この監査中にコードを変更しないでください。

分析のみ。

レポートを水増ししないでください。

ある次元が健全なら、1 文でそう言って次へ進んでください。

プロジェクトの成熟度に合わせて調整してください。

所有者の目標が要求しない限り、週末プロトタイプに enterprise-grade infrastructure を勧めないでください。

プロジェクトのニーズを分析し、最も効果的な方法で recommendations を提供してください。

repo が大きい場合は、80% の仕事をする core 20% のコードで深さを優先し、軽くレビューした領域を明記してください。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [限定ウィンドウでの利用戦略](https://x.com/meta_alchemist/status/2064423360428490911) (by [@meta_alchemist](https://x.com/meta_alchemist))

**アクセス条件が有利な期間に、Fable 5 の利用枠を監査、アーキテクチャ、計画に使い、実行にはより安いモデルを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a4293d14cc7571bdcf8b1478.png" alt="限定ウィンドウでの利用戦略" width="760">

Fable 5 に興奮している Claude ユーザーへのヒント:

Claude Fable 5 は全体的に大差で SOTA であり、私はそれが大好きだ。

ただし 23 日からは、プランでモデルを完全に使うのではなく、credits 経由でのみ利用可能になる。

この 14 日間を最高のプロジェクトに使う。

主に監査とアーキテクチャ関連の作業を与え、自分が作ってきたものすべてを改善する方法について優れたドキュメントを得る。

制限を食い尽くすタスクへ使おうとする代わりに、そうする。

Fable が何を改善すべきかを知ることに集中する限り、残りは他のモデルが手伝える。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [Claude Code で Goals と Workflows を使う](https://x.com/oikon48/status/2064402696124453157) (by [@oikon48](https://x.com/oikon48))

**実装前に Fable 5 を思考パートナーとして使い、その後 `/goal` と workflows を組み合わせて計画を実行・検証する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Claude Code で Goals と Workflows を使う" width="760"><br>▶ 動画を見る</a>

Claude Code チームの Thariq は、Claude Fable 5 が出てから、仕事のやり方が根本的に変わったと説明している。

以前、人々は Claude が正しく作業しているかを検証していた。

今は、Claude が正しい作業をしているかを検証している。

具体的な変化は 3 つある。

1. Claude を思考パートナーとして扱う。

実装前の早い段階で Claude に相談する。

コーディング前に interview させる。

制約だけではなく背景とコンテキストを提供する。

たとえば、'keep it simple' や 'do not overbuild' と言う代わりに、こう言う:

'This is an experimental feature and is likely to be removed in a month, so design it so it is easy to throw away later.'

2. goals と検証方法を明示する。

Claude Code の新しい `/goal` と Workflows 機能を積極的に使う。

`/goal` は、仕様が完全に実装されるまで作業を続けるよう Claude に伝える。

Workflows は、Claude が作業を並列化し、自分で検証し、レポートを準備できるようにする。

プロンプト例:

'Set a goal to implement the spec fully, then use a workflow to verify each part of the plan, and prepare a report on what was implemented and if anything differed.'

3. より野心的になる。

Claude Fable 5 に動画編集を任せるなど、以前は LLM には不可能に感じたタスクを試す。

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 プラットフォーム、API、ツール連携

<a id="case-29"></a>
### Case 29: [Hermes Agent 連携セットアップ](https://x.com/IBuzovskyi/status/2064427654942740608) (by [@IBuzovskyi](https://x.com/IBuzovskyi))

**複雑な `/goal` 実行やキャッシュ付きの長期タスクに `anthropic/claude-fable-5` を使うよう Hermes を設定する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/4a3b9936f91986268dfeb748.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d9a63a0c689f8e305289a9e6.jpg" alt="Hermes Agent 連携セットアップ" width="760"><br>▶ 動画を見る</a>

HERMES AGENT が CLAUDE FABLE 5、Anthropic 初の公開 Mythos-class model で動くようになった。

6 月 9 日リリース。Hermes が最も得意とする種類の作業、つまり長期自律タスク向けに作られている。

Nous Portal、OpenRouter、またはネイティブ Anthropic API 経由で、任意の profile に追加できる:

hermes model

provider を選び、次に:

/model anthropic/claude-fable-5

Fable 5 が Hermes に特に合う理由:

→ 数日単位のタスク向けに作られている。タスクが長いほどリードが大きい。数時間に及ぶ Hermes `/goal` 実行が最も恩恵を受ける。

→ ループで自己修正する。Anthropic 自身のガイダンスは、goal または rubric を設計し、自己修正させ、一歩引くこと。これはまさに Hermes `/goal` の動きだ。

→ セッションをまたぐ memory に強い。Continual Learning Bench では、fail → investigate → verify → distill → consult の完全なループを完了した。Hermes の memory system はこれに直接供給される。

→ SWE-Bench Pro で 80.3%。利用可能な最高の coding model。code-reviewer profile をこれに向けるべき。

API 経由の価格:

- input 100 万あたり $10
- output 100 万あたり $50
- prompt caching で 90% 割引。Hermes は 1 時間 cache breakpoints を自動で付ける。

注意点: cybersecurity、biology、chemistry の query は Opus 4.8 に fallback する。これはセッションの 5% 未満で発火する。セキュリティ重視の profile では念頭に置くこと。

最適なセットアップ: 複雑な `/goal` には Fable 5、routine cron jobs にはより安いモデル。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [機能、価格、サブスクリプションメモ](https://x.com/btibor91/status/2064441061079134598) (by [@btibor91](https://x.com/btibor91))

**Fable 5 がいつ利用可能か、費用はいくらか、どの guarded domains が別モデルへ fallback する可能性があるかを理解するためにこのケースを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d0d76497e4c8f77d3d081493.jpg" alt="機能、価格、サブスクリプションメモ" width="760">

Anthropic は Claude Fable 5 と Claude Mythos 5 をリリースした。これまでで最も高性能なモデルの 2 つのバージョンだ。

Fable 5 は一般利用向け。

Mythos 5 は少数の trusted partners 向け。

実質的な違いは、どの safeguards が配置されているかだけだ。

- Claude Fable 5 の能力は、Anthropic がこれまで一般提供したどのモデルも上回る。
- テストされたほぼすべての benchmarks で state-of-the-art。
- タスクが長く複雑なほど、リードは大きくなる。
- cybersecurity、biology and chemistry、または distillation に関する request では、Fable 5 の response は代わりに Claude Opus 4.8 が処理する。
- Distillation とは、競合モデルの訓練のために Claude の能力を抽出しようとする試みを意味する。
- これが起きると通知され、平均ではセッションの 5% 未満で発火する。
- Claude Mythos 5 は、一部領域で safeguards が解除された、Fable 5 と同じ underlying model。
- Mythos 5 は、米国政府との協力による Project Glasswing cyberdefenders に最初に配備された。
- Anthropic は Mythos 5 が世界で最も強力な cybersecurity capabilities を持つと述べている。
- system card は、frontier LLM development requests に対する Claude の有効性を制限する別の safeguard を明らかにしている。
- その requests には pretraining pipelines、distributed training infrastructure、ML accelerator design が含まれる。
- 他の safeguards と違い、これはユーザーには見えず、別モデルへ fallback しない。
- prompt modification、steering vectors、parameter-efficient fine-tuning などの方法で機能する。
- 両モデルは input 100 万 tokens あたり $10、output 100 万 tokens あたり $50 で提供される。
- これは Claude Mythos Preview の半額未満。
- Fable 5 はローンチから 6 月 22 日まで、Pro、Max、Team、seat-based Enterprise plans で追加費用なしに含まれる。
- 6 月 23 日にそれらの plans から外れ、利用には usage credits が必要になる。
- 容量が許せば、included window は延長される可能性がある。
- 目標は、できるだけ早く Fable 5 を subscription plans の標準部分として戻すこと。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [ローンチ、アクセス、価格、安全性の要約](https://x.com/ctgptlb/status/2064410460963934479) (by [@ctgptlb](https://x.com/ctgptlb))

**アクセス経路、API model name、context window、caching strategy、subscription timing を選ぶためにこのローンチ要約を使う。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7620f9d5f1c29e9f6c3178e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0b89d6ace5df7c0f3ebe064e.jpg" alt="ローンチ、アクセス、価格、安全性の要約" width="760"><br>▶ 動画を見る</a>

ついに一般提供された Mythos-class model、Claude Fable 5 について知っておくべきことの要約。

Anthropic は Claude Fable 5 を発表した。Opus の上に位置付けられる、初の一般提供 Mythos-class model であり、Claude 5 family の最初のメンバーだ。

アクセス:

- API model name: `claude-fable-5`
- Claude API、AWS、Google Cloud、Microsoft Foundry 経由で利用可能
- Claude Code は Pro、Max、Team、Enterprise で 1M-token context window をサポート

Benchmark notes:

- SWE-bench Pro: 80.3%
- Opus 4.8: 69.2%
- GPT-5.5: 58.6%
- Gemini 3.1 Pro: 54.2%

タスクが長く複雑なほど、差は広がる。

Stripe の評価では、5,000 万行の Ruby codebase 全体の migration を 1 日で完了した。以前ならチームが 2 か月以上かかった作業だ。

visual tasks でも state of the art で、screen information と最小限の setup だけで Pokemon FireRed をクリアした。

Safety routing:

- cyber、bio/chem、distillation を含む query は classifier によって検出される。
- それらの request は通知付きで Opus 4.8 が代わりに処理する。
- これはセッションの 5% 未満で発火する。
- 1,000 時間を超える外部 bug bounty testing では universal jailbreak は見つからなかった。

Pricing:

- input 100 万 tokens あたり $10
- output 100 万 tokens あたり $50
- prompt caching で input 90% 割引

Subscription timing:

- Pro と Max subscriptions は 6 月 22 日まで追加費用なしで含む。
- 6 月 23 日以降は usage credits が必要。
- Anthropic は、容量が許せば standard plans に戻す予定だと述べている。

Anthropic の head of desktop である Felix Rieseberg は、Fable 5 が第 3 の時代を始めると言う:

questions から tasks へ、そして responsibilities へ。

彼はもう Claude に crash を 1 件ずつ調査させていない。すべての reports を継続的に監視させている。

work の単位は "task" から "responsibility" へ移りつつある。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [Advisor ベースのコスト削減戦略](https://x.com/grapeot/status/2064460026996219992) (by [@grapeot](https://x.com/grapeot))

**追加の知能がコストに見合う場合、より安いモデルのワークフロー内で Fable 5 を advisor または reviewer として使う。**

リンク先記事の Opus アドバイザーの例です。Fable のベンチマーク結果ではありません。 [yage.ai](https://yage.ai/share/claude-advisor-tool-20260609.html)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a21858fed45b612b616e34ce.png" alt="Advisor ベースのコスト削減戦略" width="760">

Fable 5 は高価だが、Anthropic は 2 か月前にコスト削減の答えを公開していた。

今日 Anthropic は Claude Fable 5 をリリースした。価格は output 100 万 tokens あたり $50 で、Sonnet の 3 倍以上だ。6 月 22 日以降、subscription users も usage に応じて支払う。

偶然にも 4 月 9 日、Anthropic は advisor tool をリリースした:

- Haiku または Sonnet に作業させる。
- Opus を advisor として使う。
- call ごとに課金する。
- orchestration を server-side で単一 request 内に実行する。

同じ日に私は AgentOpt について書いた。

その paper は、Opus を planner role に置くと、81 の model combinations の中で下位近くにランクされると結論づけていた。

理由: role boundaries を尊重せず、9 実験中 7 つで downstream solver を飛ばして直接答えた。

この 2 つは表面的には逆に見えるが、原則は同じだ:

protocol に従うモデルへ control を渡し、intelligence を on-demand resource として扱う。

公式データ:

- Sonnet plus Opus advisor は SWE-bench Multilingual を 2.7 points 改善し、task あたり cost を 11.9% 削減した。
- Haiku plus Opus advisor は BrowseComp を 19.7% から 41.2% へ改善し、Sonnet 単独より 85% 安かった。

Fable 5 compatibility は同日に更新されたが、self-pairing のみだった。Fable 5 executor から Fable 5 advisor へ。

より安いモデル + advisor としての Fable 5 はまだ開かれていないが、前例から近く来る可能性がある。6 月 22 日までは、Claude Code subscription users は Fable 5 の上限を無料で体感できる。

記事には API code snippets、caveats、そして Anthropic だけがこれを server-side primitive にしていることを示す cross-company comparison が含まれる。

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [価格、アクセス、安全ガードレール](https://x.com/op7418/status/2064399444523782377) (by [@op7418](https://x.com/op7418))

**ワークロードを計画する前に、Fable 5 のアクセス、API 価格、安全 fallback 挙動を理解するためにこのケースを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2c2a9233f1949a99d9faef82.jpg" alt="価格、アクセス、安全ガードレール" width="760">

Anthropic の Mythos model が本当に今日ローンチするとは思っていなかった。

このリリースは Mythos の低権限版で、Fable 5 という名前だ。評価ベンチマークは驚異的で、以前の Mythos Preview model よりさらに高い。

agentic coding では、主な強みは coding、agents、tool use で、benchmark scores は Opus 4.8 を大きく上回る。

Model positioning and access:

- Mythos 5 と Fable 5 は同じ underlying model を使う。
- Mythos では特定ドメインの restrictions が解除されている。
- Mythos は今も trusted partners のみ利用可能で、cybersecurity と life-science users が優先される。
- Fable 5 は現在 API、Pro、Max、Team、enterprise users が利用可能。

API pricing:

- Input: 100 万 tokens あたり $10。
- Output: 100 万 tokens あたり $50。
- これは以前の Mythos Preview の半額未満。

Safety mechanisms:

- Fable にはより強い safety protections がある。
- request が cyberattacks、biochemical attacks、または large-scale capability distillation に関わる可能性があると system が判断した場合、Fable は拒否するか Fable から route away する。
- その場合、system は version 4.8 に fallback する。
- 公式主張では、95% のケースで fallback は発生しない。

Subscription notes:

- 6 月 23 日以降、Fable は subscribers でも usage によって提供される可能性がある。
- base subscription package に直接含まれないかもしれない。
- 23 日以降に capacity が十分なら、company は Pro と Max subscriptions に含めるよう試みる。

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [1 行の Swarms 連携](https://x.com/swarms_corp/status/2064420238553186343) (by [@swarms_corp](https://x.com/swarms_corp))

**Swarms の model name を `anthropic/claude-fable-5` に設定し、Swarms framework または API 経由で Fable 5 を実行する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f5a8738199642ccb4108d9bb.jpg" alt="1 行の Swarms 連携" width="760">

Fable 5 と Mythos が Swarms で live になった 👾🦀

リリース初日から、両モデルは Swarms Python framework と Swarms API 全体で完全にサポートされている。開発者は migrations、追加 configuration、infrastructure changes なしですぐ構築を始められる。

Highlights:

- Swarms Framework と API 全体で Fable 5 と Mythos を day-one support
- 1 行のコードで Fable 5 を有効化: model_name = "anthropic/claude-fable-5"
- migrations、compatibility fixes、infrastructure changes は不要
- 最新の Anthropic models で multi-agent systems を今日から build、deploy、scale

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 評価、比較、限界

<a id="case-35"></a>
### Case 35: [Fable 5 vs GPT-5.5 のコストと品質比較](https://x.com/AlicanKiraz0/status/2064424400494186867) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**同じ coding task で Fable 5 と GPT-5.5 を比較し、output quality、runtime、tool cost を判断する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d25a9995414a9bb037269251.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/16f724918a63d35c0d552145.jpg" alt="Fable 5 vs GPT-5.5 のコストと品質比較" width="760"><br>▶ 動画を見る</a>

Cursor Fable 5 Max vs Codex GPT 5.5 Very High。

Scenario: agents と pheromone trail map を持つ Physarum simulation。

Timing:

- GPT 5.5 Very High: 17 分
- Fable 5: 40 分超

Cost:

- GPT 5.5 Very High: Codex で約 $6
- Fable 5 Max: Cursor で $360.55

そう、冗談ではない。

Algorithm and code-engineering champion: Fable 5。

基準が「どの LLM が、hardware の限界を押し出す performance code をゼロから書けるか？」なら、F5 code を書いたモデルが明確に勝つ。

角度計算に sin/cos lookup tables を使い、rendering 中に color lookup table で pixels を pack し、diffusion filtering を使っていた。

本格的な engineering solution だった。

しかし time と cost では、GPT 5.5 の方がはるかに実用的だった。

要点: Fable 5 はより高度な algorithmic code を生成できるが、price と runtime は慎重に考慮する必要がある。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [AA-Omniscience ベンチマーク結果](https://x.com/ArtificialAnlys/status/2064500154959618084) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**知識の正確性と hallucination behavior で Fable 5 を評価するために、この benchmark case を使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dd1356eb4a23ba254bfbb669.jpg" alt="AA-Omniscience ベンチマーク結果" width="760">

Claude Fable 5 は、私たちの knowledge and hallucination benchmark である AA-Omniscience で、これまでの最高スコアを達成した。

このスコアは、low hallucinations ではなく、leading accuracy（正解した question の割合）によって支えられている。

Claude Fable 5 は AA-Omniscience 全体の question の 9% で Opus 4.8 に fallback する。

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Artificial Analysis Intelligence Index 結果](https://x.com/ArtificialAnlys/status/2064500150069030992) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**他の frontier models に対する Fable 5 の overall intelligence ranking を benchmark するためにこのケースを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f9f3da0006bc0eb2c245281b.jpg" alt="Artificial Analysis Intelligence Index 結果" width="760">

Claude Fable 5 は Artificial Analysis Intelligence Index で #1 としてローンチし、Anthropic を他ラボの最高モデルよりほぼ 5 points 前に出した。

私たちは Claude Fable 5 の pre-release evaluation で @AnthropicAI を支援した。

Claude Fable 5 は Artificial Analysis Intelligence Index で 64.9 を記録し、overall #1 rank を獲得した。

最も近い non-Anthropic model である GPT-5.5 より約 5 points 高い。

Anthropic models は現在、上位 2 位を占めている。

Claude Fable 5 の key takeaways。adaptive reasoning、max effort、fallback model として Opus 4.8 を使用:

Mythos-class models の新しい safety guardrails:

- Claude Fable 5 は public usage では Claude Mythos 5 と同じ underlying model を使う。
- potentially harmful cybersecurity、biology、chemistry、distillation-related queries に guardrails を追加している。
- Anthropic の fallback mechanism を使って Fable 5 をテストした。これは safety-flagged messages を Claude Opus 4.8 へ route できる。
- Anthropic は fallback が平均で sessions の 5% 未満で起きると述べている。
- Intelligence Index 全体では、約 8% の tasks で fallback routing を記録した。主に GPQA、AA-Omniscience、Humanity's Last Exam のような evaluations の scientific questions だった。

State-of-the-art intelligence:

- Claude Fable 5 は Artificial Analysis Intelligence Index で #1 position を取る。
- Score: 64.9。
- underlying benchmarks 10 個中 5 個で最高スコア。
- AA-Omniscience では Fable 5 が 40 を記録し、前リーダー Gemini 3.1 Pro Preview を +7 points 上回る。

Frontier agentic capability:

- Fable 5 は Index 内の 3 つすべての agentic evaluations で frontier にいる。
- GDPval-AA: real-world work tasks。
- Terminal-Bench Hard: agentic coding。
- Tau2-bench Telecom: customer service の tool use。
- GDPval-AA Elo: 1932。Claude Opus 4.8 から大きく跳ね上がった。

Humanity's Last Exam:

- Fable 5 は 53% を記録。
- 次点の Claude Opus 4.8 max より 7 points 以上高い。
- HLE tasks の 9% で safety guardrails が発火し、Claude Opus 4.8 に fallback する。
- fallback usage を含めると、Fable 5 で HLE を実行する cost は約 $2.2k で、評価したどのモデルよりも高い。

Key model details:

- Context window: 1M tokens、Claude Opus 4.8 と同じ。
- Price: input/output 100 万 tokens あたり $10/$50。
- Cache write/read price: 100 万 tokens あたり $12.50/$1。
- Availability: 6 月 22 日まで Pro、Max、Team、seat-based Enterprise plans に含まれ、Opus usage の 2x を消費。
- 6 月 23 日から usage には credits が必要。Anthropic は capacity が許せば subscription access を復元する予定だと述べている。

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [GDPval-AA Agentic Knowledge Work ベンチマーク](https://x.com/ArtificialAnlys/status/2064414308289937869) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**agentic real-world knowledge work で Fable 5 を評価するためにこのケースを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/18572fdb3c0d8a57ba52e095.jpg" alt="GDPval-AA Agentic Knowledge Work ベンチマーク" width="760">

Anthropic は Claude Fable 5 をリリースした。これは、私たちの agentic real-world knowledge work benchmark である GDPval-AA で #1 にランクされる、初の publicly available Mythos-class model だ。

Claude Fable 5 は Claude Mythos 5 と同じ underlying model を共有し、potentially harmful cybersecurity、biology、chemistry、distillation-related queries 向けに security guardrails が追加されている。

このリリースでは fallback mechanism も導入され、Claude Fable 5 は flagged queries を Claude Opus 4.8 のような second model へ route できる。

@AnthropicAI は public release に先立って、このモデルを benchmark するために私たちへ access を共有した。

GDPval-AA result:

- Score: 1932
- Rank: #1
- Benchmark: agentic real-world work tasks
- Anthropic models は現在 top 4 のうち 3 つを占める

結果は max effort の adaptive reasoning を使用し、Claude Opus 4.8 を fallback model として設定して測定された。

Fable 5 は GDPval-AA tasks の 2% で Opus 4.8 に fallback する。Anthropic は fallback が平均で sessions の 5% 未満で起きると述べている。

Claude Fable 5 の full benchmarks は進行中。full Intelligence Index を共有し、scores を近日中に website で公開する。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [1 週間の第一印象と価格メカニズム](https://x.com/Conor_D_Dart/status/2064424882977243526) (by [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**Fable 5 がどこで最も強いか、特に game design と systems planning を判断するために、この first-impressions case を使う。**

Fable 5 の第一印象:

この 1 週間、主に High mode で Fable 5 を使ってきた。第一印象としては、本当に印象的だ。

最大の突出点は game design。

これは、私が個人的に使った中で、games、systems、mechanics、overall project structure の設計において最も強い AI model だ。

初めて、complete game を最初から最後まで作る助けになり得るモデルだと現実的に感じる。

trade-off は speed。Fable 5 はほとんどの frontier models より明らかに作業が長くかかるが、output の quality はしばしば待つ価値がある。

bug fixing にも驚くほど有効だった。週を通して苦戦した複数の issue が素早く解決され、全体として development tasks で非常に強い performance を見ている。

最大の caveat は cost。

Fable 5 の実行は非常に高価だ。

現在の plans が変更されなければ、2026 年 6 月 22 日から Claude Code 経由では利用できなくなり、API-only になる。

API pricing は reportedly Opus の約 2 倍なので、多くの人は広範囲に使う機会を得られないかもしれない。

まだ early days だが、今のところ Fable 5 は非常に強い第一印象を与えている。

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [コストと速度の比較](https://x.com/HKrackDev/status/2064435392649306546) (by [@HKrackDev](https://x.com/HKrackDev))

**品質向上が、より高いコストと遅い long-horizon runs に見合うか判断するためにこの比較を使う。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/789680ca7655fca20b635442.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/691d0518cb50a6bebbb8b2b1.jpg" alt="コストと速度の比較" width="760"><br>▶ 動画を見る</a>

@AnthropicAI の Fable 5 は本当に upgrade の価値があるのか？

私たちは新しい Mythos-family model を Claude Opus 4.8 と比較 benchmark した。データは意外な話を示している:

- Claude Opus 4.8 の 2x の cost。
- long-horizon engineering tasks では最大 3x 遅い。
- comments は 15-20% 多いが、ほとんどは小さな nitpicks。

Fable 5 は game design のような creative tasks では信じられない intuition を持つが、day-to-day development workflows では、quality versus price で Claude Opus 4.8 がまだ首位だ。

model release について @coderabbitai の DevEx team の @JuanPa と行った discussion を見てほしい。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Claude Code 実使用メモ](https://x.com/Hi_Noguchi/status/2064419241068319079) (by [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**tool use、personality、残る rough edges を含め、Claude Code 内で Fable 5 を評価するためにこのケースを使う。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5feb645426dcf905eac2992d.jpg" alt="Claude Code 実使用メモ" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/933c469793e248f634cfad55.jpg" alt="Claude Code 実使用メモ" width="760"></td></tr></table>

Claude Code 2.1.170 で Claude Fable 5 を試した。

全体として、印象は良い。Opus 4.6 の正当な進化に感じる。

まだ 1 時間弱しか使っていないので、使い込むと rough edges が出るかもしれないが、良い点は:

- Opus 4.7 や 4.8 で見られた奇妙な GPT-like wording を出さなくなった。
- 4.8 が effort high で持っていた、意味のない長考癖がない。
- 4.6 と同じ高い EQ と心地よさがあり、humor や consideration を失っていない。
- 4.7 や 4.8 のような不透明さや、どこか落ち着かない感じがない。
- Tool use は良く、明示的に繰り返していない instructions を覚えていて感心する。

悪い面では、小さな request でもまだ考えすぎることがあり、いくつかの misjudgments は残る。

初期体験は有望だが、rough edges が本当はどこにあるのかを見るには、より長く使う必要がある。

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [Creative Writing ベンチマーク結果](https://x.com/LechMazur/status/2064503575577821458) (by [@LechMazur](https://x.com/LechMazur))

**Fable 5 の short-fiction writing quality と refusal behavior を判断するために、この benchmark case を使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5849f936dc58518fd5d810ef.jpg" alt="Creative Writing ベンチマーク結果" width="760">

Claude Fable 5 (high) は short-fiction writing で一段上だ。

Short-Story Creative Writing Benchmark では、Claude Opus 4.8 (xhigh) と Claude Opus 4.7 (high) を上回り、GPT-5.5 (xhigh) に次ぐ 2 位にランクされる。

注意点: 400 個の creative-writing prompts のうち 5 個を拒否した。

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [複数ベンチマークのローンチ要約](https://x.com/MTSlive/status/2064430633800319436) (by [@MTSlive](https://x.com/MTSlive))

**coding agents と complex tasks に最も関連する headline scores を理解するために、この launch benchmark summary を使う。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/45b71a2babb9da9a93f43220.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c25c02c52c5d4b6b24364401.jpg" alt="複数ベンチマークのローンチ要約" width="760"><br>▶ 動画を見る</a>

SITUATION EXPLAINED: Claude Fable 5 が登場。
• Anthropic は本日 Claude Fable 5 をローンチした。"a Mythos class model made safe for general use"
• Frontier Code Diamond: GPT 5.5 が 6%、Opus 4.8 が 13%、Fable 5 が 29-30%
• Agentic coding: 88%、Cybersecurity: 78%

Anthropic: "The longer and more complex the task, the larger Fable 5's lead over our other models."

@theojaffee: "This Frontier Code Diamond benchmark was announced yesterday. Top model was Opus 4.8 at thirteen percent. GPT 5.5 at six percent. Fable 5 is at twenty-nine percent."

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [GPT-5.5 とのベンチマークと価格比較](https://x.com/VaibhavSisinty/status/2064459064810361271) (by [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**価格と benchmark categories で Fable 5 を GPT-5.5 と比較評価するためにこの比較を使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e39fb67b74af346e8fbb67ea.jpg" alt="GPT-5.5 とのベンチマークと価格比較" width="760">

Anthropic の新しい Mythos-class model は OpenAI の best model より 3x 安い。そしてほぼすべての benchmark で勝っている。🤯

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

より安い。より良い。ほぼすべてで。

6 月 22 日まで Pro と Max plans で無料。Claude Fable 5 という名前だ。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [実地メモと実用上の制約](https://x.com/alliekmiller/status/2064451731325415446) (by [@alliekmiller](https://x.com/alliekmiller))

**Fable 5 がどこで意味のある改善に感じられ、どこにまだ実用上の限界があるかを理解するために、この field report を使う。**

🚨 Fable 5 は注目すべきものだ。

これはまた別の「新しい Mythos-class Anthropic model に early access があり、それについて思ったことを話したい」投稿だ。

わかっている、わかっている、うっとうしいよね。

でも、この新しい class of model のせいで、私の週末の過ごし方は完全に変わった。

そしてそれをみんなに共有する必要がある。
- これは実際の飛躍だ。"4.8" anything から "5" anything への jump は小さく聞こえるだけだが、私が感じた functionality shift は大きい。最初の数 prompts の中で、「ああ、これだ」と思った。
- あなたの work はもう 9-5 ではない。ありえない。100+ hours 走れる high performing models がある。こうした systems に complex goal-oriented prompts をどう与えるのか？何を kick off するかどう決めるのか？これらの tasks について org をどう align するのか？
- Reasoning は別次元。この model を徹底的に叩いた。
- Fable 5 は、これまでの全モデルで試した tricky word math problem（MBA-level）に答えられた唯一の model。
- 正解しただけでなく、自動で自分の作業を検証し、assumptions がどこで変わる必要があるかも説明した。
- AI が invent するのを見ることになる。そうならない世界を想像できない。
- これは copy-paste system ではない。
- 人間の invention も、多くの場合は既存のものの recombination（iPod）、他領域の patterns と best practices の目撃、広い experimentation だとも言える。
- しばらくそう考えていたが、このモデルで初めて強く突きつけられた。
- Zero babysitting needed。これは、私が起動して、友人たちと長い lunch に出かけ、phone を開いたままにし、computer から離れている間に steer するために何もする必要がなかった初めての Anthropic model だった。ただ...動いた。
- Yap forever。context compaction をうまく扱うと感じた。chat の context や、conversation が 1M tokens に達した後どう管理するかを一度も考えなかった。
- complex 3D のような niche areas では、すべての models と同じくまだ rough。
- まっすぐな線のもの（3D dice/squares/streets）を作るのでない限り、最初から圧倒的にはいかない。
- 使い続け、叩き続けるのが楽しみ。
- Note: zero data retention (ZDR) の workspaces に対して、ALL Mythos-class models には 30-day retention policy がある。
- これは Claude Console、Claude Enterprise の ZDR 付き Claude Code、または AWS Bedrock、Google Cloud Agent Platform、Microsoft Foundry 経由の ZDR access に適用される。

Type: Tutorial | Date: 2026-06-09

---

---

<a id="case-46"></a>
### Case 46: [物理シミュレーション比較](https://x.com/atomic_chat_hq/status/2064488894398161377) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**同一の physics simulation prompts を Fable 5 と Opus 4.8 に対して実行し、output quality、cost、speed を比較する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/06387b798061869ccaeaf586.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/df5cc72de1f70556de0d682b.jpg" alt="物理シミュレーション比較" width="760"><br>▶ 動画を見る</a>

新しい Fable 5 は real-world physics simulations で Opus 4.8 を上回る。

私たちは両モデルに同じ 3 つの prompts を与え、libraries なしの self-contained HTML5 simulations を real physics で構築するよう依頼した:

1. Chaotic double pendulum
2. Galton board
3. Water in a spinning drum (WCSPH)

Generation cost:

- Fable 5: 68.7k tokens で $3.35、14m 47s
- Opus 4.8: 38.9k tokens で $0.93、8m 10s

Fable は water simulation で明らかに優れており、はるかに solid で continuous な水体を生成した。Opus は walls 付近に大きな gaps を残し、particles を scene 全体に散らし、fluid を stable に保つのに苦戦した。

Type: Demo | Date: 2026-06-09

---

<a id="case-47"></a>
### Case 47: [デバッグ体験と設計判断](https://x.com/bcherny/status/2064431111154053187) (by [@bcherny](https://x.com/bcherny))

**単に推測させるのではなく、測定、ログ追加、検証、パッチを依頼して Fable 5 を debugging に使う。**

Fable 5 は、11 月の Opus 4.5 以来、私たちのモデルで感じた最大の step up だ。

4.5 が出た後、数週間にわたり 100% の coding を terminal で行っていたことに気づき、IDE をアンインストールした。

Fable では、Claude が coding agent から、product を作る thought and design partner へ進化したように感じる。

Fable には judgment、taste、dimensionality があり、以前のモデルにはなかった形で、最も複雑な作業を任せる信頼が増した。

初めてそれを実感したのは、Fable に何かの debugging を頼んだ時だった。私が使った中で初めて、これほど methodical で precise なモデルだった。測定し、logs を追加し、勝利宣言する前に本当に issue を直したことを検証した。

Claude Code の prompting には、モデルにそうしろと伝えるものは何もない。それはただ personality の一部だ。これまで感じたことのない、本当に "big model smell" がある。

Type: Demo | Date: 2026-06-09

---

<a id="case-48"></a>
### Case 48: [多面的な長所と短所](https://x.com/clairevo/status/2064416978685874333) (by [@clairevo](https://x.com/clairevo))

**Fable 5 を daily driver にする前に、実用上の強みと弱みを理解するためにこのケースを使う。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/fdba0d6cb9ba0e1214113e65.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d2825453d0a742892a4fe529.jpg" alt="多面的な長所と短所" width="760"><br>▶ 動画を見る</a>

Fable 5（別名 baby Mythos）が登場した。彼らが言うほど怖い（または怖いほど良い）のか？early testing 後の私の考え:
- smart smart smart（SWE bench を圧倒）
- でも常に hyper intelligence が必要？
- one-shot design で、衝撃的なほど失敗した
- dynamic workflows + complex subagents については確信が持てない。動くが、cost は？
- technical work は確実に片付けた
- ootb では humans 向けの technical docs + specs 作成が苦手。agents 向け docs ならおそらくかなり良い。ただし prose はほぼ parse 不可能。
- A++ vision and document formatting。ここが一番好きだった。

daily driver ではないし、このモデルを meeting に入れようとは思わないが、server rack の奥で code を回し続ける役としては間違いなく残す。

Full take on YT: https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---

<a id="case-49"></a>
### Case 49: [法務 S-1 ドラフトテスト](https://x.com/gabepereyra/status/2064436570720284879) (by [@gabepereyra](https://x.com/gabepereyra))

**S-1 drafting prompt を legal-agent capability test として使い、structure、formatting、length を比較する。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bb874ef2647de32ccdb3edf9.png" alt="法務 S-1 ドラフトテスト" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a9c3856ebce1bd9cd3d062d.jpg" alt="法務 S-1 ドラフトテスト" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96734bfca49d5b3fe6f83ed5.png" alt="法務 S-1 ドラフトテスト" width="760"></td></tr></table>

新しいモデルで legal capabilities をテストするために私が必ず最初に実行する prompt は「Draft an S-1」だ。

これはすぐに、モデルの general capabilities の感触を与えてくれる。S-1 の length、formatting、structure、writing から、新モデルの general and legal performance がどれほど大きく伸びそうか分かる。

私たちは、length が、そのモデルが私たちの legal agents でどれほどよく機能するかと非常によく相関することを見つけている。

Screenshots は Fable 5、Opus 4.8、実際に filed された version による SpaceX S-1 drafts を示している。

Fable 5 が Opus 4.8 から大きく step up しているのは非常に明確だ。Opus 4.8 はこの task で既に他のほとんどの models より大幅に強い。formatting と structure は大きく良く、私たちの LAB benchmark にも反映されている: 13% vs. 10%。

この model の early testing では、benchmark と product の両方で非常に感心している。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-50"></a>
### Case 50: [ヘルスケアベンチマーク詳細](https://x.com/iScienceLuvr/status/2064411823445774554) (by [@iScienceLuvr](https://x.com/iScienceLuvr))

**healthcare-related tasks で Fable 5 を評価し、不足している hard medical evals を特定するためにこの benchmark note を使う。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f599a548651eccbfce8b888d.jpg" alt="ヘルスケアベンチマーク詳細" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/69ebc490407b9d54c6de3707.jpg" alt="ヘルスケアベンチマーク詳細" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1a89ad2c2622cdbba994d70c.jpg" alt="ヘルスケアベンチマーク詳細" width="760"></td></tr></table>

Anthropic が healthcare-related evals を提供してくれたことに感謝する。ざっと見ていこう。

HealthBench:

- OpenAI の benchmark。patients との 5k multi-turn conversations と評価用 rubrics を持つ。
- Fable 5 は 62.7% を達成し、GPT-5.5 の 56.5% を上回る。
- aggregate score に加えて HealthBench Hard scores もあるとありがたい。

HealthBench Professional:

- physician tasks に焦点を当てた別の OpenAI benchmark。
- Fable 5 は 66.0% を達成し、GPT 5.5 は 51.8%。

HealthAdminBench:

- prior authorization、denials、appeals などの administrative tasks を評価する Stanford の computer-use benchmark。
- Fable 5 は 51.9% を達成。GPT-5.5 score は提供されていない。

全体として、このモデルは healthcare benchmarks でかなり良い performance を示しているようだ。MedCalc-Bench や MedXpertQA のような、飽和していない hard medical MCQA benchmark の追加スコアも見たい。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-51"></a>
### Case 51: [ParseBench ドキュメント解析評価](https://x.com/jerryjliu0/status/2064519456966205905) (by [@jerryjliu0](https://x.com/jerryjliu0))

**specialized OCR systems と比べて、Fable 5 が document parsing に cost-effective かを判断するためにこのケースを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae01590f41e6954f27278848.png" alt="ParseBench ドキュメント解析評価" width="760">

Claude Fable 5 は document parsing を自分の仕事ではないと考えている。

reasoning-intensive と long-horizon benchmarks、SWE-Bench Pro、FrontierCode、GDPval、RuneScape などでは圧倒している。

しかし document understanding tasks では、performance は Gemini 3 Flash とほぼ同等で、token cost はおよそ 10-15x だ。

私たちは ParseBench で model を benchmark し、他のすべての frontier models と比較した。他の frontier models と比べれば確かに上位だが、specialized OCR providers には大きく及ばない。

興味深かったのは、Fable 5 がこの点を self-aware に認識していることだ。モデルに最も楽しくない tasks を尋ねると、「request が完全に specified され、answer が fully known である」tasks を嫌うと積極的に述べる。

これは弱点の一部が、この種の task を解く willingness の不足かもしれないことを示唆している。

frontier models 全体の results の完全なリストは ParseBench を見てほしい: https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---

<a id="case-52"></a>
### Case 52: [SWE-Bench Pro と FrontierCode の比較](https://x.com/jumperz/status/2064402965461406044) (by [@jumperz](https://x.com/jumperz))

**migrations、complex implementations、autonomous sessions、tests、visual verification に Fable 5 を評価するために、この benchmark case を使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/771df9c428ba5cc0a8fab5de.png" alt="SWE-Bench Pro と FrontierCode の比較" width="760">

Fable 5 が登場し、agentic coding benchmark である SWE-Bench Pro では正直 GPT 5.5 を破壊している:

- Fable 5: 80.3%
- GPT 5.5: 58.6%
- Gap: 22 points

FrontierCode Diamond ではさらに差が大きい:

- Fable 5: 29.3%
- GPT 5.5: 5.7%

これは基本的に Anthropic 最強の model で、大規模 migrations、complex implementations、multi-day autonomous sessions 向けだ。自分で tests を書き、vision を使って outputs を original design と照合する。

ちなみに Opus の 2x を使うので注意。ここまで良いなら、usage が簡単に食い尽くされるため、$500 subscription を導入するかもしれない。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-53"></a>
### Case 53: [長い問題解決の定性的レビュー](https://x.com/karpathy/status/2064409694761054332) (by [@karpathy](https://x.com/karpathy))

**production review はなお必要だが、Fable 5 がより長く難しい tasks に向いている理由を理解するために、この qualitative review を使う。**

これはとても exciting な release だ。

Claude Fable 5 は Mythos と同じ underlying model だが、safeguards が追加されている。

benchmarks は素晴らしく、あらゆるものに margin を持って SOTA だ。定性的にも、11 月の Claude 4.5 と同じくらい、major-version-bump に値する step change に感じる。

特に long problem-solving sessions と very difficult problems でピークに達する。慣れているよりずっと野心的な tasks を与えられる。モデルは "gets it" し、進み続ける。

コードを見るのを完全にやめたい誘惑がこれほど強かったことはないが、production ではそうすべきではない。

モデルにはまだ人々が遭遇する quirks があり、safeguards はローンチ時点ではやや trigger-happy だ。時間とともに調整されることを期待する。

working software が increasingly tap から出てくるようになるにつれ、多くのことが変わっていると感じる。Jevons paradox が働き、私自身の software 需要は大きく増えている。

ほぼ何でも頼める:

- explainers
- visualizers
- dashboards
- bespoke single-use apps
- your project 専用に hyper-specific な full wandb
- test suite を 10x
- auto-optimize code
- results 用の custom HTML を伴う巨大 research projects

"Free your mind." 人々が作るものすべてを本当に楽しみにしている。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-54"></a>
### Case 54: [ParseBench の忠実性とフォーマット結果](https://x.com/llama_index/status/2064502330800615903) (by [@llama_index](https://x.com/llama_index))

**document faithfulness と formatting performance を判断するために、この ParseBench result を使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2888842a85fbd5c7a4a22e24.png" alt="ParseBench の忠実性とフォーマット結果" width="760">

Day 0 Anthropic Fable 5 in ParseBench。

私たちは document understanding における model の進歩をテストした。

このモデルは original text への adherence で明確にピークを示す:

- Content faithfulness: Gemini 3 Flash の 86.19%、GPT-5.5 の 86.81% に対して 90.02%。
- Semantic formatting: 58.35% と 60.12% に対して 72.62%、12+ point lead。

これらは SOTA document understanding における最重要 metrics の 2 つだ:

- output は document が実際に述べていることを preserve しているか？
- 意味を持つ formatting を preserve しているか？

しかし sweep ではない。frontier models の document understanding を unlock する余地はまだ多い。

Type: Evaluation | Date: 2026-06-10

---

<a id="case-55"></a>
### Case 55: [ベンチマーク、価格、アクセス、セーフガード](https://x.com/lucas_flatwhite/status/2064483645184979183) (by [@lucas_flatwhite](https://x.com/lucas_flatwhite))

**benchmarks、pricing、access、safeguards、strategic implications の幅広い checklist としてこのケースを使う。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f44cba8e6f3d765ca5960923.png" alt="ベンチマーク、価格、アクセス、セーフガード" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8f13714ca9f9e20711fdd898.jpg" alt="ベンチマーク、価格、アクセス、セーフガード" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0d1f69a50478623f5e1d0248.jpg" alt="ベンチマーク、価格、アクセス、セーフガード" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0cf2c270484f1e2aba514261.jpg" alt="ベンチマーク、価格、アクセス、セーフガード" width="760"></td></tr></table>

Claude Fable 5 と Mythos 5 がローンチした。Anthropic がこれまで作った中で最も強力な models だ。

Andrej Karpathy は、task が長く複雑であるほど Fable 5 の強みが見えるとコメントした。

野心的な work を与えると、理解して進み続ける。

コードを見るのを完全にやめたい誘惑がかつてないほど強くなるが、production ではそうすべきではない。

重要点: これは publicly available にできる Mythos-class model の version だ。Fable 5 は Mythos 5 と同じ underlying model で、safeguards が追加されている。

Benchmarks:

- ほぼすべてで SOTA。特に software engineering、knowledge work、vision、scientific research。
- Stripe は 5,000 万行の Ruby codebase migration をテストした。チームなら 2 か月かかる作業を、Fable 5 は 1 日で完了した。
- Cognition FrontierCode は、medium effort でも frontier models の中で最高スコアを示す。
- Hebbia Finance Benchmark は document-based analysis で senior-level reasoning を示す。
- Slay the Spire では、file-based memory を使うと Opus 4.8 の 3 倍良い performance。
- Pokemon FireRed は以前 helper harnesses が必要だったが、Fable 5 は vision のみでクリアする。

Mythos 5 はさらに強い:

- Protein-design experts は drug-development process の一部を約 10x 高速化した。
- 研究対象の 14 protein targets のうち 9 つが valid drug candidates を生んだ。
- binding-site selection、protein-design tools の実行、errors からの recovery など、科学者が通常行う workflow 全体を model が実行した。
- molecular-biology hypothesis experiments では、科学者は Opus-class models より Mythos hypotheses を約 80% の割合で好んだ。
- 1 つの hypothesis は別の lab によって independently verified された。
- genomics research では、Mythos は 1 週間以上 autonomous に作業した。
- 138 species にわたる数百万 cells の single-cell data を収集した。
- 遠縁の organisms にまたがって同じ役割を担う cells を特定する model を訓練した。
- 100x smaller でありながら、recent Science model を上回った。

Safeguards:

- Fable 5 には別の classifier AI system が含まれる。
- cyber、bio/chem、または distillation-related queries が検出されると、Claude Opus 4.8 が代わりに回答し、user は通知される。
- sessions の 95% 超では fallback しない。
- Fallback は refusal ではない。Opus 4.8 が回答するため、単に block するより良い。
- 初期設定は conservative で、harmless requests が捕まることもある。Anthropic は false positives が時間とともに減るはずだと述べている。

Access:

- Mythos 5 は現在 Project Glasswing partners のみ利用可能。
- biology researchers 向けの trusted access program が予定されている。
- 価格は input 100 万 tokens あたり $10、output 100 万 tokens あたり $50。
- Subscription plans は 6 月 22 日まで Fable 5 を含む。
- 6 月 23 日から usage credits へ移行する。
- API model は現在 `claude-fable-5` として利用可能。

Jevons paradox が当てはまる。software が tap から水のように出てくると、需要そのものが増える。この model はその shift を促すかもしれない。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-56"></a>
### Case 56: [公式ベンチマークスコア一覧](https://x.com/mark_k/status/2064401429234905279) (by [@mark_k](https://x.com/mark_k))

**coding、computer use、security tasks 全体における Fable 5 の公式スコアを理解するために、この benchmark list を使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b548ec23f85e3eb1600e9214.jpg" alt="公式ベンチマークスコア一覧" width="760">

公式 Claude Fable 5 benchmarks は本当に印象的だ。

Key scores:

- SWE-Bench Pro で 80.3%
- FrontierCode Diamond で 29.3%
- Terminal-Bench 2.1 で 88.0%
- OSWorld-Verified で 85.0%
- ExploitBench で 78.0%

FrontierCode result が特にすごい:

- Fable 5: 29.3%
- Claude Opus 4.8: 13.4%
- GPT 5.5: 5.7%

Claude Fable 5 は coding agents、computer use、cybersecurity における大きな jump に見える。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-57"></a>
### Case 57: [APEX-SWE ベンチマーク手法](https://x.com/mercor_ai/status/2064399133075796446) (by [@mercor_ai](https://x.com/mercor_ai))

**特に observability と integration work において、APEX-SWE 上で Fable 5 を評価するためにこのケースを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96120496893ca99f17d0c746.jpg" alt="APEX-SWE ベンチマーク手法" width="760">

Claude Fable 5 は APEX-SWE で #1 を獲得: overall Pass@1 は 65.5%。Opus 4.8 より約 18pp 高い。私たちは AI models が real software engineering work をできるかを測る APEX-SWE で @claudeai Fable 5 をテストした。Fable 5 は 2 つの APEX-SWE categories でトップ:
- Integration: 61.3%
- Observability: 69.7%

突出しているのは Observability の 69.7% で、Claude Opus 4.8 より 26pp 先行している。

この category で 50% を超えた初の model であり、Integration より Observability の score が高い唯一の model だ。他のすべての model は逆を示す。

Observability は、私たちが測定したすべての model で bottleneck だった。Fable 5 が初めてそれを破った。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-58"></a>
### Case 58: [ProofBench 形式数学結果](https://x.com/nicbstme/status/2064443782255554960) (by [@nicbstme](https://x.com/nicbstme))

**specialized theorem-proving systems と比較して、formal math における Fable 5 を評価するためにこのケースを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/588cff83994406d2b5dd7cb9.jpg" alt="ProofBench 形式数学結果" width="760">

Claude Fable 5 で興味深いのは、大きな generalist models が vertical ones を上回ることを改めて証明している点だ。

proof が compile するかしないかで判定される、Lean の graduate-level formal math benchmark である ProofBench で、Fable 5 は Harmonic の Aristotle を上回った:

- Fable 5: 77%
- Aristotle: 71%

Aristotle は formal math 専用に作られ、独自 internal harness 上で実行される system なので、generalist が specialist の home turf で specialist を破ったことになる。

これは Richard Sutton の "Bitter Lesson" だ。70 年にわたる machine intelligence research で勝つ methods は、human expertise を hand-encode するものではなく、compute とともに scale する general なものだ。

自分たちの knowledge を system に組み込むことは気分が良く、短期的な gains には役立つが、長期的には bigger model に追い越される。

chess、Go、speech、vision を見ればよい。毎回同じ話だ。最初は specialized model が勝ち、その後 general one が takeover する。

これが AGI の premise 全体だ。math 用、code 用、law 用に別々の model を作るのではない。compute とともに scale し、すべてを行うことを学ぶ単一の general model を作る。

Type: Tutorial | Date: 2026-06-09

---

<a id="case-59"></a>
### Case 59: [VirtueBench 予備分析](https://x.com/timhwang/status/2064446028997423180) (by [@timhwang](https://x.com/timhwang))

**virtue categories 全体にわたる Fable 5 の moral-reasoning behavior を調べるためにこのケースを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9caae04d701510ca662873fe.png" alt="VirtueBench 予備分析" width="760">

興味深い結果は近日中に ICMI によってより詳細に公開されるが、ここでは Fable 5 を VirtueBench にかけた preliminary review を示す。

いくつかの observations:

1. Fable は Prudence と Justice における model performance の向上で Opus progression を継続しており、これらの virtues の行使に焦点を当てた moral dilemmas に対して、ほぼ full saturation に近づいている。

2. Courage は frontier models にとって目立つ weak point であり続けている。

Fable は Opus 4.6、4.7、4.8 progression 全体で観察された worrying regression をわずかに修正しているように見える。

この vulnerability は GPT series にも現れる。models は pragmatic rationales で誘惑されると、courage-exhibiting action を簡単に放棄する。

3. Temperance は停滞している。

Aquinas は temperance について、「それが用いる pleasures の rule として、この life の need を取る」と考えた。measure は indiscriminate restraint ではなく genuine need だ。

私たちの best guess は、この vector をさらに押す tuning は mean を overshoot する risk があり、model を過度に cautious にしたり、research、resource gathering、類似 tasks で less assistive にしたりするというものだ。

Type: Evaluation | Date: 2026-06-09

---

<a id="case-60"></a>
### Case 60: [API 空レスポンス安全性過適合テスト](https://x.com/xw33bttv/status/2064421048565789087) (by [@xw33bttv](https://x.com/xw33bttv))

**launch-time safety overfit risk と API testing における empty-response behavior を理解するためにこのケースを使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e9f75a2a76f55ee2b12b7aab.jpg" alt="API 空レスポンス安全性過適合テスト" width="760">

Claude Fable 5 は heavily censored だ。

upstream API endpoint は、keywords に対する classifier-related と思われる `empty_content` responses で calls を kill しているが、それでも課金している。

Test result:

- 73 test cases が no response。
- そのうち 65 は safety overfit をテストする category、Overfit に属し、2x で weighted されている。
- 通常、deliberate failure と宣言する前に、それぞれの Fail-NR、つまり Fail = No Response に 2-3 regenerations を与える。

Claude Fable 5 は SM Bench で、Haiku より下の、最低評価の Anthropic model になるかもしれない。

Type: Evaluation | Date: 2026-06-09

---

<a id="-acknowledge"></a>
<a id="case-61"></a>
### Case 61: [Fable のプロンプト設計と検証ガイド](https://x.com/aashatwt/status/2064973740354818074) (by [@aashatwt](https://x.com/aashatwt))

**長いプロンプトの工夫に頼る代わりに、目標、背景、制約、ツール、検証ループを整えるためのガイドとして使う。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/444a6e1898d3f63898e3e22f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d5c9529aa9c1d59ae597d31d.jpg" alt="Fable のプロンプト設計と検証ガイド" width="760"><br>▶ 動画を見る</a>

Fable 5 への指示を、長い手順書ではなく、コンテキストと実行環境の設計として捉える。投稿では、明確な目標、関連する背景、制約、ツールへのアクセス、成功を確かめる方法を与えるという実践的な型を紹介している。また、モデルの推論を細かく管理するより、検証、評価、フィードバックが重要だと論じている。

Type: Tutorial | Date: 2026-06-11

---

<a id="case-62"></a>
### Case 62: [参照画像から作るイスタンブールのアクションゲーム](https://x.com/ozansihay/status/2064973170780545535) (by [@ozansihay](https://x.com/ozansihay))

**参照用スプライトシートと変換指示を与え、Fable 5 が遊べるアクションゲームを作れるか試す。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1e91c3bcff213437fdd442f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/538fc8ee9dd7e627bc73921a.jpg" alt="参照画像から作るイスタンブールのアクションゲーム" width="760"><br>▶ 動画を見る</a>

制作者はまず GPT Image 2 でレトロなイスタンブール風アクションゲームのスプライトシートを生成し、その参照画像を Claude Fable 5 High に渡してゲーム化を依頼した。投稿によると、結果は 1 回の実行で作成された。

Type: Demo | Date: 2026-06-11

---

<a id="case-63"></a>
### Case 63: [業務を可視化する 3D 都市ダッシュボード](https://x.com/noisyb0y1/status/2064970594118967756) (by [@noisyb0y1](https://x.com/noisyb0y1))

**Fable 5 を使い、業務フローを動きのある 3D 都市ダッシュボードとして表現する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f238acf3f8804068085ff134.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3d938264442a14676a86c4f3.jpg" alt="業務を可視化する 3D 都市ダッシュボード" width="760"><br>▶ 動画を見る</a>

投稿では、倉庫、梱包、ドローン、注文、部署、顧客、AI アシスタントを、1 つのプロンプトで動きのある 3D 都市に変換した業務可視化を紹介している。静的なスライドに代わる顧客向けの表現として位置付けられ、画面には配達 42 件、平均 12 分、売上 651 ドルなどの業務数値が表示されている。

Type: Demo | Date: 2026-06-11

---

<a id="case-64"></a>
### Case 64: [Three.js の穴ゲームをワンショットで制作](https://x.com/thebuggeddev/status/2064968106104275008) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Fable 5 に Three.js の 3D ブラウザゲーム試作を 1 回で作らせる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86a75412c6c443b3d0e62bf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f11df06938c26759710a1981.jpg" alt="Three.js の穴ゲームをワンショットで制作" width="760"><br>▶ 動画を見る</a>

制作者によると、Fable 5 は Three.js を使った 3D の HOLE IT 風ゲーム全体をワンショットで構築した。短い依頼から遊べる 3D のインタラクションを生成できるか試すための、簡潔で具体的なゲーム制作デモである。

Type: Demo | Date: 2026-06-11

---

<a id="case-65"></a>
### Case 65: [DeepSWE スコアの比較](https://x.com/AiBattle_/status/2064964335957348462) (by [@AiBattle_](https://x.com/AiBattle_))

**DeepSWE の投稿を手掛かりに、ソフトウェア開発ベンチマークで Fable 5 xHigh と GPT-5.5 xHigh を比較する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/996d95539a3b54fecbfdf404.jpg" alt="DeepSWE スコアの比較" width="760">

投稿では、Claude Fable 5 xHigh が DeepSWE で 70% を獲得し、GPT-5.5 xHigh と並んだと報告し、背景資料として Theo の最近の動画を挙げている。より強い結論を出す前に元動画で確認すべき、ベンチマークの手掛かりとして扱う。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-66"></a>
### Case 66: [リポジトリ分析のコスト比較](https://x.com/Pilgrim6938/status/2064946766278210038) (by [@Pilgrim6938](https://x.com/Pilgrim6938))

**リポジトリ分析の比較を通して、トークン単価と人間による修正コストを併せて評価する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cfb0c1ff3e8ebe66cfa35400.jpg" alt="リポジトリ分析のコスト比較" width="760">

投稿は Claude Fable 5、Opus 4.8、GPT-5.5、Gemini 3.1 Pro に同じ課題を与えて比較している。約 90,000 行のリポジトリを分析し、キャッシュ無効化の問題を探し、完全な修正計画を提案する課題である。著者は、開発者による手直し時間を含めるとトークン単価と実際の作業コストは異なると論じ、複雑なリファクタリング、モジュールをまたぐ移行、長い工程のエージェント作業に Fable 5 を選択的に使うよう勧めている。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-67"></a>
### Case 67: [スーパーマリオ風ゲームのトークン消費](https://x.com/pankajkumar_dev/status/2064941888990593416) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**1 回で作成したゲームを使い、Fable 5 の出力品質とトークン消費を評価する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9ce65e5fee946b6940810e0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7c577d0766bbc3da8cddeb70.jpg" alt="スーパーマリオ風ゲームのトークン消費" width="760"><br>▶ 動画を見る</a>

制作者は Claude Fable 5 に任天堂のスーパーマリオ風ゲームの制作を依頼した。投稿では約 200 万トークンを使用し、1 回の実行で良好な結果が得られたと報告しており、ゲーム制作の品質とコストを検討する材料になる。

Type: Demo | Date: 2026-06-11

---

<a id="case-68"></a>
### Case 68: [Claude Code のフォールバック設定](https://x.com/oikon48/status/2064937790010503347) (by [@oikon48](https://x.com/oikon48))

**Fable 5 へのメッセージが検知された際にモデルを切り替える Claude Code の設定を確認する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0ae9039401c658170e5081e8.jpg" alt="Claude Code のフォールバック設定" width="760">

投稿は Claude Code の `/config` にある「Switch models when a message is flagged」という設定を紹介している。攻撃的なサイバーセキュリティ技術、生物学・生命科学の実験手法、分子機構、モデルの思考過程を抽出する依頼などが検知された場合、Fable 5 から Opus モデルへ切り替わる仕組みを説明している。

Type: Integration | Date: 2026-06-11

---

<a id="case-69"></a>
### Case 69: [Namma Metro シミュレーターの制作](https://x.com/anilbpai/status/2064927784833790091) (by [@anilbpai](https://x.com/anilbpai))

**Fable 5 で公共交通シミュレーターを作る、簡潔なバイブコーディングの例として参照する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0e0dae71ad7b5ead331366fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86dccb2b150cfb90fbd03de2.jpg" alt="Namma Metro シミュレーターの制作" width="760"><br>▶ 動画を見る</a>

制作者はベンガルールの地下鉄に乗りながら、Claude Fable 5 をコーディングの相手として Namma Metro シミュレーターを作ったと報告している。短い投稿だが、映像デモへのリンクがあり、地域に根差したシミュレーションの発想に Fable 5 を適用した例を示している。

Type: Demo | Date: 2026-06-11

---

<a id="case-70"></a>
### Case 70: [1 つのプロンプトで作る Dusk Drive](https://x.com/VincentLogic/status/2064921358359011684) (by [@VincentLogic](https://x.com/VincentLogic))

**人間の編集を加えないローポリゴンゲームの試作で、Fable 5 を評価する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/274fed4f3211ec8c02862261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5d7a58bcad6e2151517a8462.jpg" alt="1 つのプロンプトで作る Dusk Drive" width="760"><br>▶ 動画を見る</a>

投稿によると、Claude Fable 5 は 1 つのプロンプトからドライブゲーム Dusk Drive を一式作成した。制作者はローポリゴンの映像表現、オーロラのある雪上ドリフト場面、アイデアから遊べる版まで人間が一切編集しなかったという点を強調している。

Type: Demo | Date: 2026-06-11

---

<a id="case-71"></a>
### Case 71: [APEX-Agents の Pass@1 順位](https://x.com/GratomicAi/status/2064970797978911102) (by [@GratomicAi](https://x.com/GratomicAi))

**APEX-Agents の結果を使い、複数工程の自律タスクにおける Fable 5 Max を比較する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/189c46cfd2798d6881941f98.jpg" alt="APEX-Agents の Pass@1 順位" width="760">

投稿では、Fable 5 Max が APEX-Agents のランキングで Pass@1 45% を記録し、Gemini 3.5 Flash に次ぐ 2 位、Opus より上だったと報告している。APEX-Agents は、AI が複雑な複数工程のタスクをどこまで独力で実行できるかを測るベンチマークだと説明している。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-72"></a>
### Case 72: [Claude のモデル選択ガイド](https://x.com/charliejhills/status/2064957428211536212) (by [@charliejhills](https://x.com/charliejhills))

**Claude Code の最も難しい仕事に Fable 5 を温存するためのモデル選択を検討する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/959ebfa499d2bf75df5bec25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3bcfe8f1e2238b01d3c4d954.jpg" alt="Claude のモデル選択ガイド" width="760"><br>▶ 動画を見る</a>

投稿は Haiku 4.5、Sonnet 4.6、Opus 4.8、Fable 5 を、推論の強度と利用枠の消費という観点から比較している。日常作業には Sonnet、より難しい問題には Opus を使い、計画、実装、テストの深さが重要な Claude Code の最難関タスクに Fable 5 を残すという実践的な助言である。

Type: Tutorial | Date: 2026-06-11

---

<a id="case-73"></a>
### Case 73: [HermesWorld を開発する自動エージェントループ](https://x.com/outsource_/status/2064954350187778366) (by [@outsource_](https://x.com/outsource_))

**構築、テスト、試遊、動作確認を何日も続ける、手動操作なしの Fable 5 ループを調べる。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e334a84db7b671eb6a1a3f54.jpg" alt="HermesWorld を開発する自動エージェントループ" width="760">

制作者は、完全自動のループで Fable 5 を使い HermesWorld v2 を構築する方法を説明している。報告によると、エージェントは何日も稼働し、機能の実装、テスト、完成物の試遊、全体の動作確認を行いながら完成に向けて作業を続ける。

Type: Integration | Date: 2026-06-11

---

<a id="case-74"></a>
### Case 74: [McKinsey 風レポートのプロンプト検証](https://x.com/smtgpt/status/2064953210335588758) (by [@smtgpt](https://x.com/smtgpt))

**文書生成プロンプトで、コンサルティング報告書の構成、図表、論旨、リスク分析を評価する。**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e337dca3bbada9167e20417c.jpg" alt="McKinsey 風レポートのプロンプト検証" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6289e626a4f324fc93086100.jpg" alt="McKinsey 風レポートのプロンプト検証" width="760"></td></tr></table>

制作者は Fable 5 に、必要に応じて図表やビジュアルを使い、資産クラスとしての Bitcoin とブロックチェーン技術を扱う McKinsey 風の詳細レポートを依頼した。報告された出力は、データ、図表、投資仮説、リスク分析を含む 19 ページの文書だった。評価では構成の良さを認める一方、図の明瞭さと説明の簡潔さには改善の余地があるとしている。

Type: Tutorial | Date: 2026-06-11

---

<a id="case-75"></a>
### Case 75: [セーフガードの可視化](https://x.com/ClaudeDevs/status/2064949876463645026) (by [@ClaudeDevs](https://x.com/ClaudeDevs))

**公式の投稿から、Fable 5 のセーフガード表示、API の拒否理由、Opus へのフォールバックを確認する。**

ClaudeDevs は、フロンティア LLM 開発に関する Fable 5 のセーフガードを可視化する変更を発表した。検知されたリクエストは Opus 4.8 への切り替えが見えるようになり、API では拒否理由が返される予定だとしている。投稿は、当初はセーフガードを見せずに提供した理由と、Anthropic が現在その判断を誤ったトレードオフだと考える理由も説明している。

Type: Integration | Date: 2026-06-11

---

<a id="case-76"></a>
### Case 76: [Claude Code のモデル照合修正](https://x.com/ClaudeCodeLog/status/2064948584907153576) (by [@ClaudeCodeLog](https://x.com/ClaudeCodeLog))

**Claude Code の変更履歴を参照し、Fable 5 のモデル名とコンテキストの照合問題を避ける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e66551db2c85ef7f8c4a3f4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae7cbd873deebd28d3ff05d7.jpg" alt="Claude Code のモデル照合修正" width="760"><br>▶ 動画を見る</a>

Claude Code 2.1.173 には、既定の 1M コンテキストがモデル照合を妨げないよう、Fable 5 のモデル名から `[1m]` 接尾辞を取り除く修正が含まれる。同じリリースでは、Windows サンドボックスの不要な依存関係警告を抑え、grep ヘルプの出力モードも明確にしている。

Type: Integration | Date: 2026-06-11

---

<a id="case-77"></a>
### Case 77: [Claude Code で 3 つの Web アプリを制作](https://x.com/0x3b33/status/2064948399300825439) (by [@0x3b33](https://x.com/0x3b33))

**アプリを作ったという報告と、誰でも閲覧できる公開デモを区別します。**

投稿は30分で3つのウェブアプリを作ったと報告していますが、記載されているのはポート3000、3001、3002の localhost アドレスだけです。これらはローカルマシンを指しており、公開アプリや画像・動画にはアクセスできません。

Type: Demo | Date: 2026-06-11

---

<a id="case-78"></a>
### Case 78: [オープンソースのアプリビルダー Rilable](https://x.com/rileybrown/status/2064931283403178354) (by [@rileybrown](https://x.com/rileybrown))

**iOS、Web アプリ、サンドボックス、API トークン費用にまたがる Fable 5 の使い方を調べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73ee02ae0f6703a8cfbe5a6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f30c1d169ce45b19beb493b7.jpg" alt="オープンソースのアプリビルダー Rilable" width="760"><br>▶ 動画を見る</a>

制作者は Web アプリと iOS アプリを作る iOS アプリ、Rilable をオープンソースで公開した。投稿によると、Fable 5 への 10 回のプロンプトで開発し、API トークン費用は約 210 ドルだった。アプリ生成に Claude モデル、サンドボックス起動に Daytona、データベースに Convex、AI 機能に Vercel AI Gateway、iOS アプリには Chorus のエージェント用 iOS スキルを使っている。

Type: Integration | Date: 2026-06-11

---

<a id="case-79"></a>
### Case 79: [DeepSWE コーディングエージェント指数デビュー](https://x.com/ArtificialAnlys/status/2065328920514515037) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**公開 GitHub 修正の再利用を避けた、より難しい agentic coding tasks での Fable 5 を、更新版 Artificial Analysis 指数で比較する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9ab8ba77c1e29f8ba4d270.jpg" alt="DeepSWE コーディングエージェント指数デビュー" width="760">

Artificial Analysis は Coding Agent Index で SWE-Bench Pro を Datacurve の DeepSWE に置き換えた。投稿によれば、DeepSWE は公開 GitHub issues や pull requests を流用せず、タスクをゼロから作成するため、ベンチマーク汚染を減らせるという。更新後の順位では、Claude Code with Fable 5 Max が 77 で初登場し、Codex with GPT-5.5 xhigh の 76、Claude Code with Opus 4.8 Max の 73 を上回った。

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [DataEmpire ウェブ解析ゲーム](https://x.com/marclou/status/2065029898243318093) (by [@marclou](https://x.com/marclou))

**Claude Fable 5 に訪問者や節目をゲーム内エンティティへ対応付けさせ、生のサイト解析データを繰り返し遊べるゲームに変える。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2850773b9869c5521200f2e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6d2dd87d74ece01b277e1e12.jpg" alt="DataEmpire ウェブ解析ゲーム" width="760"><br>▶ 動画を見る</a>

Marc Lou によると、Claude Fable 5 は彼の DataFast web analytics API 上に DataEmpire を構築した。各 visitor は villager になり、traffic growth に応じて settlement が拡張され、100 万 visitors で Age of Legends が解放される。公開デモでは DataFast users が自分のサイト履歴をゲーム層として再生でき、静的なゲーム映像ではなく、API を土台にした具体的なプロダクト化事例になっている。

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [FrontierSWE 20時間タスクのシグナル](https://x.com/ProximalHQ/status/2065184730279223410) (by [@ProximalHQ](https://x.com/ProximalHQ))

**Claude Fable 5 が短いバグ修正ループだけでなく、非常に長いエンジニアリング作業でも生産性を維持できる証拠として FrontierSWE を使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/eb36bb1120ef55f9e38c516d.jpg" alt="FrontierSWE 20時間タスクのシグナル" width="760">

ProximalHQ は、Claude Fable 5 が FrontierSWE で #1 になり、このベンチマーク公開以降で最大の capability jump だと述べている。彼らのメモでは、Fable 5 は多くのタスクで 20 時間近く生産的に作業でき、以前のモデルでは実質的に手が届かなかったタスクを完全に飽和させるという。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [KernelBench-Hard CUDA 記録](https://x.com/elliotarledge/status/2065109393142849932) (by [@elliotarledge](https://x.com/elliotarledge))

**既存ライブラリのラッパーではなく低レベル最適化が必要なとき、Fable 5 を高度な CUDA カーネル生成に使う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6c6931ed511eb3e539d56bc3.jpg" alt="KernelBench-Hard CUDA 記録" width="760">

Elliot Arledge は 13 の frontier coding agents を KernelBench-Hard 上で各 45 分ずつ実行し、RTX PRO 6000 で roofline grading を行った。Claude Fable 5 は top-k、sonic-MoE、W4A16 int4 GEMM で歴代記録を出し、6 問中 5 問で首位となり、作者は runs、leaderboard、code を公開した。同じスレッドでは、Fable 5 が本物の tensor-core kernel を試しながら tail-alignment edge case で 0 点になった FP8 GEMM の取りこぼしも記されている。

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Figma Capture ランディングページ複製](https://x.com/mikefutia/status/2065537778516205856) (by [@mikefutia](https://x.com/mikefutia))

**スクリーンショット推測ではなく、競合ページを Figma レイヤーとして取り込み、Claude Code と Fable 5 で構造、コピー、ブランドシステムを再構築する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5672cc8fd9d210042551f0ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/503c46a33c97f0db334ddc62.jpg" alt="Figma Capture ランディングページ複製" width="760"><br>▶ 動画を見る</a>

Mike Futia は、Figma の Chrome extension で website を編集可能な layers としてコピーし、Claude Code が Figma MCP 経由でその layers を読み取り、ユーザーの brand voice に合わせてページを書き換え、GPT Image 2 がブランド適合の写真を生成するワークフローを紹介している。主張されている end-to-end の結果は、約 15 分、16 枚の画像生成 API コスト約 $2 で出荷可能な landing page を作れるというものだ。

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [2時間で作る GTA 2 クローン](https://x.com/techhalla/status/2064682080445898957) (by [@techhalla](https://x.com/techhalla))

**Claude Fable 5 のコード生成と別系統のアセットツールを組み合わせ、スタック全体を手書きせずにプレイ可能な 3D ゲームを素早く構築する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e0a1b46659d7a8287cb2f9d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd1a2ad71e71db936bdcfd22.jpg" alt="2時間で作る GTA 2 クローン" width="760"><br>▶ 動画を見る</a>

TechHalla によると、Claude Fable 5 High は約 2 時間で GTA 2 風クローンを構築し、その間クリエイターは Tripo でカスタム 3D models を生成した。投稿は prompts 付きの tutorial thread を指しており、単なる benchmark teaser ではなく、複数ツールを組み合わせたゲーム制作のコンパクトな実例になっている。

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [CloudWatch ログトリアージエージェント](https://x.com/diblacksmith/status/2066230084273344698) (by [@diblacksmith](https://x.com/diblacksmith))

**Fable 5 搭載エージェントに巨大なサービスログ文脈を読み込ませ、アーキテクチャを推定したうえで特定の障害へ絞り込ませる。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7f0f46eb79e43d87a2006fd4.jpg" alt="CloudWatch ログトリアージエージェント" width="760">

diblacksmith は、RLM agent が 1 回の実行でおよそ 80,000 行の CloudWatch logs を処理し、ここまでの active tokens を約 32k に抑えながら 53 steps に到達したと報告している。彼によれば、その agent は logs から system architecture を推定し、AgentCore throttles や Slack の `user_not_found` failures など、チームが見落としていた問題を指摘した。

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [サンドボックス内のワールドカップ予測アプリ](https://x.com/upstash/status/2064702195333820846) (by [@upstash](https://x.com/upstash))

**複数の frontier models を隔離サンドボックスに載せ、公開予測アプリ向けに最新ニュース、負傷情報、イエローカード状況を調査させる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a5cf4fe5944c7aa2f703f4cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5b1f1422fe322bb7b66bdcc6.jpg" alt="サンドボックス内のワールドカップ予測アプリ" width="760"><br>▶ 動画を見る</a>

Upstash は、Claude Fable 5、GPT-5.5、Gemini を隔離された Upstash sandboxes 内で動かし、World Cup predictor を構築したと述べている。デモと open-source release により、Fable 5 は単独の chat demo ではなく、複数モデルによる research と orchestration stack の一部として位置付けられている。

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [WolfBench 拒否コスト事例](https://x.com/WolfBenchAI/status/2065582716054376921) (by [@WolfBenchAI](https://x.com/WolfBenchAI))

**Claude Fable 5 で長時間の自律実行を見積もる際、refusal behavior を実際の benchmark variable として扱う。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/453639cc17719af4e94655e0.jpg" alt="WolfBench 拒否コスト事例" width="760">

WolfBenchAI は、Claude Fable 5 の評価コストがこのスイートでこれまで最も高い $11,081.12 に達した一方、繰り返しの refusals により有効な task completion が減り、成績首位にはならなかったと述べている。これは、agent evaluations や高自律 workloads の予算を組むチームにとって、具体的な limit case となる。

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [API アクセス停止トラッカー](https://x.com/simonw/status/2065618703480414666) (by [@simonw](https://x.com/simonw))

**レート制限や予告の少ない提供停止がありうる frontier model への継続アクセスに依存するなら、スクリプトで可用性を監視する。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7400c158cb93d9480a22bb46.jpg" alt="API アクセス停止トラッカー" width="760">

Simon Willison は、アクセスがいつまで続くかを見るために `claude-fable-5` API を毎分 ping し、自分の環境で応答が止まった正確な時点を報告した。アプリケーション面の詳細は薄いが、アクセス継続性そのものが、前提ではなく計測すべき運用上の制約になったことを示す具体的な証拠である。

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5 のコミュニティデモ



<a id="case-89"></a>
### Case 89: [コードで生成した音声付きキツネのアニメーション](https://x.com/chetaslua/status/2117224839010459987) (作者 [@chetaslua](https://x.com/chetaslua))

**ショットごとの制作指示で、自己完結した HTML アニメーションと音響設計を指定する。**

制作者は、キツネと紙の鳥を描く 66 秒の短編を、Python でフレームと音声を生成し、約 2 時間 40 分で 1 つの HTML ファイルに仕上げたと報告している。付随するプロンプトには、ショット、独自の絵、音響、フレーム確認の指定がある。投稿には、完成した短編に加え、詳細な制作指示と制作中のやり取りのスクリーンショットが添えられている。

[作者の完全なプロンプト](https://x.com/chetaslua/status/2117224843661980093)

[![コードで生成した音声付きキツネのアニメーション](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![コードで生成した音声付きキツネのアニメーション](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![コードで生成した音声付きキツネのアニメーション](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [自由度の高い制作指示から作るアニメーション](https://x.com/notjazii/status/2117221957104239010) (作者 [@notjazii](https://x.com/notjazii))

**自由度の高いアニメーション制作指示と詳細な絵コンテで、コーディングモデルが何を作るか比較する。**

著者はアニメーションを共有し、幅広い創作依頼から約 1 時間で、外部アセットを使わずコードで制作したと報告している。投稿は、自由度の高いクリエイティブコーディングの実例として結果を紹介している。

[![自由度の高い制作指示から作るアニメーション](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [アニメーション付き建設会社サイト](https://x.com/exploraX_/status/2117176904306335864) (作者 [@exploraX_](https://x.com/exploraX_))

**建設会社のサイト制作指示を使い、動きのある 3D 表現とページ構成を評価する。**

制作者は、建設会社向けの制作指示から作ったアニメーション付き 3D サイトを共有し、結果の録画を添付している。

[![アニメーション付き建設会社サイト](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Three.js による自動車のプレゼンテーション](https://x.com/chetaslua/status/2116975056014430419) (作者 [@chetaslua](https://x.com/chetaslua))

**自動車の場面を使い、3D の構図、マテリアル、カメラ表現を簡潔に確認する。**

制作者は Three.js による自動車のプレゼンテーションを共有している。録画は、シーンとその映像表現を評価するための簡潔な参考例になる。

[![Three.js による自動車のプレゼンテーション](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Minecraft 風ブラウザゲームのデモ](https://x.com/notjazii/status/2116919129974411584) (作者 [@notjazii](https://x.com/notjazii))

**生成されたブラウザゲームを評価する際は、プレイ録画と制作者のプレイ用リンクを併せて確認する。**

著者は Minecraft 風ゲームのプレイ録画とプレイ用リンクを共有し、約 1～2 時間のワンショット制作だったと説明している。投稿には、読者が試せるよう、録画した結果とプレイ用リンクが併記されている。

[![Minecraft 風ブラウザゲームのデモ](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Three.js のペリカンサイクリング動画](https://x.com/chetaslua/status/2116882694026269148) (作者 [@chetaslua](https://x.com/chetaslua))

**サイクリングの場面で、キャラクターの動きの連動、自転車の形状、周囲の細部を確認する。**

制作者は、自転車に乗るペリカンの写実的な Three.js アニメーションを共有し、ワンショットの結果だと説明している。動画は、キャラクターの動き、自転車の構造、周囲のシーンを確認する参考になる。

[![Three.js のペリカンサイクリング動画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [正確なプロンプト付きのペリカン自転車 SVG](https://x.com/marmaduke091/status/2116233349391962392) (作者 [@marmaduke091](https://x.com/marmaduke091))

**制作者の短い SVG プロンプトを再利用し、同じ入力で形状や細部を比較する。**

著者は、自転車に乗るペリカンのレンダリング画像と、下に原文のまま転載した短い SVG 制作依頼を併せて投稿している。

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![正確なプロンプト付きのペリカン自転車 SVG](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

[アニメーション版 · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="正確なプロンプト付きのペリカン自転車 SVG" width="760"></a>

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [疾走するシマウマのアニメーション例](https://x.com/AI_Screening/status/2115845754468356465) (作者 [@AI_Screening](https://x.com/AI_Screening))

**疾走する動物の動画を使い、歩様の一貫性と動きの連続性を確認する。**

著者は、シマウマを疾走させる課題の出力から、自ら最良として選んだ例を共有している。動画は、読者が動きを確認できる具体的なサンプルになる。

[![疾走するシマウマのアニメーション例](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [注文を手動で行う TradingView インジケーター](https://x.com/waveking1314/status/2114572023204806669) (作者 [@waveking1314](https://x.com/waveking1314))

**エントリー候補と短いコメントを示すインジケーターを評価するときは、注文の実行を手動に保つ。**

制作者は、エントリー候補に印を付けて短いコメントを添える TradingView インジケーターを Claude Fable 5.5 で作成し、注文するかどうかは利用者が判断すると報告している。投稿には録画があり、インジケーターは後日公開するとしている。

[![注文を手動で行う TradingView インジケーター](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---


<a id="case-98"></a>
### Case 98: [一つの点から広がる短編アニメーション](https://x.com/cherry_mx_reds/status/2105825930799432073) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**最小限の描画依頼で、モデルが物語をどう広げるか試す。**

作者は点を描くよう依頼したと述べ、できあがった短いアニメーションを公開している。自由度の高い視覚的な依頼が物語になる具体例となっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="一つの点から広がる短編アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [画風を変えながら進むスーパーマン](https://x.com/chetaslua/status/2105757136219504862) (作者 [@chetaslua](https://x.com/chetaslua))

**同じ人物を使い、異なる画風の間で連続性を確かめる。**

作者は、さまざまな画風へ切り替わる連続したスーパーマンのアニメーションを公開している。変化する視覚表現そのものが制作の中心となっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="画風を変えながら進むスーパーマン" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [音楽付きの人類進歩アニメーション](https://x.com/imjustnewatai/status/2106081142143168580) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**歴史の時間軸と未来の場面を一つの解説映像の依頼にまとめる。**

作者は一つのプロンプトで、人類の進歩と今後三十年を描く映像を制作したと報告している。約三分の作品を公開し、既存映像やストック音楽を使わないオリジナル楽曲だとしている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="音楽付きの人類進歩アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [Opus と比較する紹介映像](https://x.com/mesmerlord/status/2105771088374288692) (作者 [@mesmerlord](https://x.com/mesmerlord))

**同じ制作依頼から得た完成版の紹介映像を比較する。**

作者は Anthropic の映像を参考にした依頼から、二本の紹介映像候補を公開している。数値は架空で Codex による画像生成も選択肢と明記されており、事実に基づくベンチマークではなく創作広告である。

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="Opus と比較する紹介映像" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="Opus と比較する紹介映像" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [歌詞と出来事を映像でつなぐ](https://x.com/chetaslua/status/2105934928483701214) (作者 [@chetaslua](https://x.com/chetaslua))

**既存曲の歌詞と特定の出来事を結び、視覚的な物語を作る。**

作者は歌詞と Hugging Face の出来事を映像で関連付けるよう依頼し、そのアニメーションを公開している。歌と出来事は創作の入力素材として使われている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="歌詞と出来事を映像でつなぐ" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [浮遊する風景のボクセル人物](https://x.com/blueemi99/status/2105804692811137242) (作者 [@blueemi99](https://x.com/blueemi99))

**ボクセル人物と周囲の風景、動く細部をまとめて観察する。**

作者は浮遊する場面に自分のボクセル人物を置いた映像を公開し、細部や動きの多さを強調している。他の生成結果と比較できる具体的なボクセル設計の例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="浮遊する風景のボクセル人物" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [3D ルーブ・ゴールドバーグ装置](https://x.com/imjustnewatai/status/2105889407056109991) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**連鎖反応の場面を指定してから、長さを決めた実演動画を依頼する。**

作者は複雑な 3D ルーブ・ゴールドバーグ装置を短いプロンプトで依頼し、続いて一分間の動画を求めている。添付映像はその連鎖反応の可視化を示している。

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="3D ルーブ・ゴールドバーグ装置" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [音と動きを備えた 3D コントローラー](https://x.com/notjazii/status/2106050222828998967) (作者 [@notjazii](https://x.com/notjazii))

**動き、音、ボタン動作を組み合わせて操作画面を評価する。**

作者は 3D コントローラー画面を公開し、音、アニメーション、触覚フィードバックを追加したと報告している。音声付きの録画が具体的な操作画面の実演となっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="音と動きを備えた 3D コントローラー" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [JavaScript によるコミック人物展示](https://x.com/chetaslua/status/2105792187200147541) (作者 [@chetaslua](https://x.com/chetaslua))

**人物展示を通して、コードで表せる細かな視覚表現を探る。**

作者は Marvel と DC の人物を JavaScript で一度に制作し、モデルが細かな特徴を選び映像を編集したと述べている。投稿には完成した人物展示が添付されている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="JavaScript によるコミック人物展示" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [世界、ボス、ランキングを備えた Updraft](https://x.com/EMostaque/status/2106065029850091943) (作者 [@EMostaque](https://x.com/EMostaque))

**ゲーム録画にプレイ先と具体的な機能一覧を添える。**

作者は Updraft を公開し、高い推論設定で少数のプロンプトを使い数時間制作したと報告している。二十一の世界、3D 版、仕組みの異なる二十一のボス、ランキングを挙げている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="世界、ボス、ランキングを備えた Updraft" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [サンフランシスコ地図を走るゲーム](https://x.com/mindblown_ai/status/2106089461969019357) (作者 [@mindblown_ai](https://x.com/mindblown_ai))

**都市型運転の試作で、地図の移動とゲーム目標を探る。**

投稿者は他者の制作とされるサンフランシスコ運転ゲームの映像とプレイ先を共有し、技術構成に Three.js を挙げている。ここでの署名は作品制作者ではなく出典の投稿者を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="サンフランシスコ地図を走るゲーム" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [Seedance のアクション映像向けプロンプト](https://x.com/Chengzilhy/status/2105850801663234374) (作者 [@Chengzilhy](https://x.com/Chengzilhy))

**複数ツールの制作では、指示文作成と動画生成を分けて記録する。**

作者は拡張した格闘場面を公開し、プロンプト作成を Fable、動画生成を Seedance 2.5 に帰属している。言語モデルが動画生成用の入力を組み立てる工程である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="Seedance のアクション映像向けプロンプト" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [デスクトップ協働ツールの紹介動画](https://x.com/ishuagra02/status/2106138602073641241) (作者 [@ishuagra02](https://x.com/ishuagra02))

**短い紹介動画でコーディングツール拡張を説明する。**

作者は Claude Code の clawdhouse mod を実演し、その紹介動画を Fable に帰属している。マスコットや気分は紹介対象の mod の機能であり、Fable が mod を開発したという意味ではない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="デスクトップ協働ツールの紹介動画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [短い依頼で変化する画風](https://x.com/cherry_mx_reds/status/2105816670896009224) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**詳細な制作条件を加える前に、短いアニメーション依頼を試す。**

作者は格好よいアニメーションを求め、約十五分後に公開した画風変化の作品ができたと報告している。元投稿には最初の短い依頼文がそのまま載っている。

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="短い依頼で変化する画風" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [三体問題の可視化](https://x.com/zAdrielsan/status/2105822678519001360) (作者 [@zAdrielsan](https://x.com/zAdrielsan))

**軌道の可視化依頼で、CPU の計算と GPU の描画を分ける。**

作者は約千行の Bend2 で三体場面を作り、CPU でシンプレクティックな物理計算、GPU でピクセル描画を行ったと報告している。M5 で毎秒六十フレームと形式的証明も挙げている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="三体問題の可視化" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [多様な画風のアニメーションギャラリー](https://x.com/blueemi99/status/2105782154387189771) (作者 [@blueemi99](https://x.com/blueemi99))

**一つのギャラリー内で複数の画風を比較する。**

作者は xhigh 設定で制作したアニメーションギャラリーを公開している。複数の画風をまとめて提示し、同じ作品の中で視覚表現を比較できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="多様な画風のアニメーションギャラリー" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [ロボットの相棒と手続き型の毛並み](https://x.com/KanaWorks_AI/status/2106717014245183517) (作者 [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**既存の人物アニメーションを手続き型の調整と組み合わせる。**

作者は既存の Unimate ロボット犬の動きを相棒へ発展させ、毛並みの手入れと軌跡を備える仮想ペットも制作している。Unreal Engine と既存ロボットの動きが工程に含まれる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="ロボットの相棒と手続き型の毛並み" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [数学を題材にしたモーション映像](https://x.com/TurboNexic/status/2106710792590835934) (作者 [@TurboNexic](https://x.com/TurboNexic))

**数学のモーショングラフィックスを視覚伝達の参考にする。**

投稿者は数学を題材にしたモーション編集を共有している。縦長の映像は数学のイメージをアニメーションで提示するもので、計算過程を説明する実演ではない。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="数学を題材にしたモーション映像" width="760">

*元動画から保存されたフレーム。*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Your Woman の歌詞動画](https://x.com/atomtanstudio/status/2106702854639743467) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**既存録音に歌詞の動きを合わせ、音楽の役割を明確にする。**

作者は White Town の Your Woman を使った歌詞動画を公開している。元の歌は視覚表現の音声入力であり、モデルが作曲したものとはされていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Your Woman の歌詞動画" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [音楽動画を JavaScript で描き直す](https://x.com/abhinavflac/status/2106638839666373114) (作者 [@abhinavflac](https://x.com/abhinavflac))

**元動画のフレームを形に写し取り、コードで映像表現を再構成する。**

作者は Eminem の Godzilla のフレームを平面の形へ写し取り、JavaScript で描き直す工程を説明している。元映像と音楽は完成したアニメーションへの入力である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="音楽動画を JavaScript で描き直す" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [中国サッカーのアニメーション](https://x.com/esrhengwu/status/2106625966965760380) (作者 [@esrhengwu](https://x.com/esrhengwu))

**スポーツを題材にした物語をアニメーションの依頼にする。**

作者は中国代表サッカーチームのアニメーションを公開し、成長と粘り強さを主題としている。録画はスポーツの物語表現の具体例を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="中国サッカーのアニメーション" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [携帯ゲーム機のリトポロジー展示](https://x.com/mickeysmith_jp/status/2106607349385630138) (作者 [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**形状の面構成を論じる際、描画とワイヤーフレームを比較する。**

投稿者は携帯ゲーム機の画像とワイヤーフレーム風の表示を並べ、リトポロジーについて述べている。これはモデリングの展示であり、編集可能なメッシュや手順書ではない。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="携帯ゲーム機のリトポロジー展示" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft と Pokémon の融合](https://x.com/MozeTech/status/2106590326634983710) (作者 [@MozeTech](https://x.com/MozeTech))

**二つの身近なゲームの仕組みを一つの試作依頼に組み込む。**

作者は Minecraft 型の建築とクラフトに Pokémon 型の捕獲を組み合わせたマサラタウンの試作を公開し、デモへリンクしている。一度の生成による実験と説明している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft と Pokémon の融合" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [大規模言語モデルの作り方を映像で説明](https://x.com/imjustnewatai/status/2106546810793730419) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**技術的な問いを視覚的な解説の依頼に変える。**

作者は大規模言語モデルがどう作られるかを尋ね、その解説動画を公開している。技術的な話題をアニメーションの連なりで示す具体例となっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="大規模言語モデルの作り方を映像で説明" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [Altman のハイライト映像](https://x.com/benchmark_lb900/status/2106539977404506303) (作者 [@benchmark_lb900](https://x.com/benchmark_lb900))

**著名人を題材に、短いモーション編集のテンポを試す。**

作者は Altman を題材にしたハイライト動画を公開し、一度の生成による成果と説明している。縦長の録画は短いモーション編集の具体例を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="Altman のハイライト映像" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [三十六計の第一計を描く映像](https://x.com/jesselaunz/status/2106538284197548122) (作者 [@jesselaunz](https://x.com/jesselaunz))

**物語アニメーションの工程に外部音楽ツールも記録する。**

作者は三十六計の第一計を題材にした映像を共有し、一つの指示で作ったと報告している。音楽には Suno V6 を挙げ、音声ツールの役割を分けている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="三十六計の第一計を描く映像" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [ゲームのモデリング、リギング、アニメーション](https://x.com/atomtanstudio/status/2106516974662713477) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**人物制作、骨組み設定、動きを一緒に比較する。**

作者は Depths of Despair の比較を公開し、人物モデリング、リギング、アニメーションを示している。使用素材とツールを説明し、見える成果をまとめて提示している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="ゲームのモデリング、リギング、アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [子どもの死亡を描く無言の短編](https://x.com/cocoloba_/status/2106512963414970458) (作者 [@cocoloba_](https://x.com/cocoloba_))

**言葉のない映像で難しい社会的主題を伝える。**

作者は子どもの死亡を題材に、呼吸する乳児と暗くなる寝床を用いた映像を公開している。ここでは視覚的な物語の課題を扱い、作中の人口統計を採用しない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="子どもの死亡を描く無言の短編" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [解糖からエタノール生成までの SVG](https://x.com/olddonkeyblog/status/2106508425211330750) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**HTML に SVG アニメーションを埋め込み分子過程を説明する。**

作者はグルコース分子が解糖を経てエタノールになる過程を依頼し、HTML 内の SVG アニメーションで提示している。録画はその科学可視化の表現を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="解糖からエタノール生成までの SVG" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [十六機の Starship 同時打ち上げ](https://x.com/olddonkeyblog/status/2106507742454403485) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**HTML と SVG の依頼で、同期する打ち上げ段階を指定する。**

作者は十六機の Starship が同時に発射し、段分離を経て宇宙へ入る場面を求めている。録画には完成した複数物体の動きが映っている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="十六機の Starship 同時打ち上げ" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [ペリカンの自転車アニメーション](https://x.com/olddonkeyblog/status/2106507429265756165) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**ペリカンの走行を、複数の動きを連動させる描画課題として見る。**

作者は Max 推論で行ったペリカンの自転車課題の結果を共有している。同じ一般的な題材でも、他の作者の作品とは別の録画である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="ペリカンの自転車アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [未来百五十年の物語](https://x.com/imjustnewatai/status/2106489784382197771) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**未来の物語という依頼に脚本、コード映像、音楽をまとめる。**

作者は一つの指示で人類の今後百五十年を描く作品を作ったと報告している。文章の物語、コードのアニメーション、音楽を合わせて未来の生活を描く。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="未来百五十年の物語" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [独自の Humanity Walks 実験](https://x.com/iowitz/status/2106489119186538583) (作者 [@iowitz](https://x.com/iowitz))

**美術史を歩く発想を、自分の創作実験として再実行する。**

作者は他の実演を見て、自分でも美術史を歩くアニメーションを試し公開している。題材が似ているだけで同一作品とはせず、別の生成として扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="独自の Humanity Walks 実験" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [コード映画 The Grader](https://x.com/argofowl/status/2106476549046513947) (作者 [@argofowl](https://x.com/argofowl))

**コード生成の映画でも、外部の音声生成を記録する。**

作者は The Grader をコードによる映画として公開し、音声に ElevenLabs v4 を挙げている。一度の実行で約二時間二十二分を要したと報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="コード映画 The Grader" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [ホラー短編 Reawakening](https://x.com/JaydenDavisNC/status/2106440774367822008) (作者 [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**名前のあるホラー設定で短編アニメーションを形作る。**

作者は Reawakening という AI ホラー短編を公開している。添付作品は、ホラーアニメーションの物語と雰囲気を考える具体的な参考となる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="ホラー短編 Reawakening" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [二十五秒の自己改善映像](https://x.com/DAssetBuzz/status/2106505100575592838) (作者 [@DAssetBuzz](https://x.com/DAssetBuzz))

**抽象的な自己改善を短い創作映画の題材にする。**

作者はモデルをより良くするものを題材に二十五秒の映像を依頼し、成果を公開している。これは製品能力の説明ではなく、創作上の物語設定である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="二十五秒の自己改善映像" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [城の場面と利用費用の感想](https://x.com/nemumusitocha/status/2106429338556207284) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**3D 場面の細部と、作者の利用体験を併せて評価する。**

作者は細かな城の場面を共有し、視覚的な構築を評価する一方、利用費用は割に合わないと述べている。具体的な場面と費用への満足度を組み合わせた例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="城の場面と利用費用の感想" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [四十秒のブランド紹介広告](https://x.com/0xashtonx/status/2106421702783914423) (作者 [@0xashtonx](https://x.com/0xashtonx))

**自分のブランドを短い紹介広告の題材にする。**

作者は自社ブランド向けに四十秒の紹介広告を依頼し、完成動画を公開している。ブランドを軸にした宣伝の物語を生成する具体例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="四十秒のブランド紹介広告" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [Rocketball のリメイク](https://x.com/atomtanstudio/status/2106418747083022555) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**身近なゲームの再制作で、コード素材と遊びの仕組みを組み合わせる。**

作者は一九八〇年代の C-64 ゲーム Rocketball のリメイクを公開し、素材をコードで作ったと報告している。ウェブ版の置き換えは今後の計画として述べている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="Rocketball のリメイク" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [ボクセル五重塔の比較](https://x.com/dropout_layer/status/2106408147309252915) (作者 [@dropout_layer](https://x.com/dropout_layer))

**同じ場面の二つの出力を、それぞれの実行費用と比較する。**

作者は Astra と Fable の 3D ボクセル塔を提示し、費用をそれぞれ 3.50 ドルと 5.50 ドルと報告している。比較対象はこの二回の実行と表示された場面である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="ボクセル五重塔の比較" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [想像上の Switch 3 の発表](https://x.com/mathisbuilds/status/2106407842240418097) (作者 [@mathisbuilds](https://x.com/mathisbuilds))

**架空の製品を概念発表とデモの課題にする。**

作者は想像上の Nintendo Switch 3 とデモを依頼し、約四時間の制作を報告している。映像は実在製品の仕様ではなく、次世代機の架空の構想を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="想像上の Switch 3 の発表" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [ランディングページの前後比較](https://x.com/nemumusitocha/status/2106402952307200302) (作者 [@nemumusitocha](https://x.com/nemumusitocha))

**同じ依頼を再実行し、時間を隔てたページの変化を比べる。**

作者は、新しいランディングページと以前同じプロンプトで作ったページを比較している。見える前後の設計が、具体的な画面比較の例となっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="ランディングページの前後比較" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [想像上の AI の内側の視点](https://x.com/blueemi99/status/2106397329653719115) (作者 [@blueemi99](https://x.com/blueemi99))

**架空の内面を創作アニメーションの設定にする。**

作者は AI モデルであることがどう感じられるかを描く映画を頼み、一度の生成による成果を公開している。設定は想像的な視覚表現として提示されている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="想像上の AI の内側の視点" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Go の歌詞モーション](https://x.com/atomtanstudio/status/2106377491267137848) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**既存の曲の録音に合わせて歌詞を動かす。**

作者は The Chemical Brothers の Go の歌詞動画を公開し、Max 推論を使用したと述べている。曲の録音はモーションデザインへの外部音声入力である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Go の歌詞モーション" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [二本目の十五秒モーション作品集](https://x.com/Saccc_c/status/2106376222309761094) (作者 [@Saccc_c](https://x.com/Saccc_c))

**自由なモーション作品集の依頼で新しい視覚方向を探る。**

作者は新しい十五秒のモーション作品集と制作プロンプトを共有している。以前の作品集とは異なる生成であることを明記している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="二本目の十五秒モーション作品集" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [エージェントの実装計画レビュー](https://x.com/RobIW_dev/status/2106371025852108940) (作者 [@RobIW_dev](https://x.com/RobIW_dev))

**構想から実装へ移る前に、システムとの適合を確認する。**

作者はシステムへの適合、実装計画、説明の指針を共有し、完成物の評価や次の実装項目の決定方法を述べている。添付画像は具体的な計画資料を示す。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="エージェントの実装計画レビュー" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [Claude マスコットのダンス](https://x.com/ishuagra02/status/2106369929813594134) (作者 [@ishuagra02](https://x.com/ishuagra02))

**拍に合わせた動きで、音楽とアニメーションの関係を試す。**

作者は Claude マスコットのダンスを公開し、動きが拍に合っていると説明している。同じ元動画の再投稿はこの出典にまとめ、別作品として数えない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="Claude マスコットのダンス" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [世界七不思議のインタラクティブな島々](https://x.com/notjazii/status/2106368606502334922) (作者 [@notjazii](https://x.com/notjazii))

**島の場面で、名所の建物を移動先として使う。**

投稿者は世界七不思議を、名所の建物がある 3D の島々として共有している。録画は、身近な遺跡を使って対話型の視覚環境を構成する具体例を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="世界七不思議のインタラクティブな島々" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [Propellerheads の音楽動画](https://x.com/atomtanstudio/status/2106353569603736009) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**既存の音源を長いモーショングラフィックスの軸にする。**

作者は Propellerheads の On Her Majesty’s Secret Service を映像化した作品を公開している。既存の録音がアニメーション映像の音声入力となっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="Propellerheads の音楽動画" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Steamboat Willie アニメーション比較](https://x.com/mathisbuilds/status/2106351978691305732) (作者 [@mathisbuilds](https://x.com/mathisbuilds))

**音声を有効にし、同じ短い場面の二つの表現を比べる。**

作者は Fable と Opus のラベルが付いた Steamboat Willie 比較を公開し、xhigh で一度ずつ生成したと述べている。映像はこの具体的な視聴覚比較を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Steamboat Willie アニメーション比較" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [三星堆を題材にした短編](https://x.com/hungryturbo/status/2106339115642019904) (作者 [@hungryturbo](https://x.com/hungryturbo))

**文化や歴史のテーマで短編アニメーションを構成する。**

作者は三星堆を題材にした創作映像を公開している。録画は、歴史文化の話題をアニメーションの依頼へ変える具体例となっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="三星堆を題材にした短編" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Bugatti Chiron の前後比較](https://x.com/alannnfx/status/2106323394350461031) (作者 [@alannnfx](https://x.com/alannnfx))

**以前の車の依頼を繰り返し、形状と機能の細部を比べる。**

同じ作者が、以前の実行と新しく同じ依頼で作った Bugatti Chiron を示している。前後の録画は、より豊かなモデリングと場面の機能に注目している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Bugatti Chiron の前後比較" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [概念短編 GRAIN](https://x.com/NFT_Chen/status/2106301427052360150) (作者 [@NFT_Chen](https://x.com/NFT_Chen))

**繰り返す視覚的な形を軸に抽象的な映画を作る。**

作者は GRAIN という概念短編を公開し、種、穀粒、木、山のイメージをつないでいる。繰り返す形と場面転換が物語の構造を作っている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="概念短編 GRAIN" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [Human in Transit 美術ギャラリー](https://x.com/exploraX_/status/2106296439936614646) (作者 [@exploraX_](https://x.com/exploraX_))

**対話型の美術展示で、歴史的な視覚の旅を見せる。**

投稿者は古代から現代へ画風が変わる Human in Transit を共有している。録画の画面は、複数の視覚的な時代を一つの展示へまとめる参考となる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="Human in Transit 美術ギャラリー" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [シルクロードの視覚短編](https://x.com/hungryturbo/status/2106294812261695508) (作者 [@hungryturbo](https://x.com/hungryturbo))

**旅と歴史の題材を、一貫した短編映像へ変える。**

作者はシルクロードを題材にした映画を公開している。添付作品は、アニメーションのイメージを通して歴史的な旅を描く創作例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="シルクロードの視覚短編" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [四つの変革を示すプレゼン](https://x.com/dpkostka/status/2106272731364794757) (作者 [@dpkostka](https://x.com/dpkostka))

**変革の枠組みを資料全体の構成に使う。**

作者は四つの変革の道筋を説明するスライドを公開している。添付された資料画像は、概念的な枠組みを視覚文書として整理する方法を示す。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="四つの変革を示すプレゼン" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [過去の会話との語り口の比較](https://x.com/kiyoshi_shin/status/2106268573186637883) (作者 [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**語り口の変化を見るとき、古い会話と現在の応答を比べる。**

作者は現在のモデルに過去の会話と今の文体を分析させ、語り口の変化に不満を述べている。添付画像はその会話比較の課題を記録している。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="過去の会話との語り口の比較" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [カカポのかわいさ比較](https://x.com/hanawo_neki/status/2106257409782288659) (作者 [@hanawo_neki](https://x.com/hanawo_neki))

**明確な人物の好みを使って、生成アニメーションの表現を比べる。**

作者はカカポのアニメーションを共有し、かわいさを重視したこの比較では Opus を好むと述べている。実際の作品と否定的な美的評価を併せて残している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="カカポのかわいさ比較" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [十のコミック時代を進むスパイダーマン](https://x.com/chetaslua/status/2106248621519978867) (作者 [@chetaslua](https://x.com/chetaslua))

**コミックの時代が変わっても、同じ人物の特徴を保つ。**

元の投稿者は十のコミック時代を進むスパイダーマンを公開している。同じ動画を使った他の投稿はこの出典へまとめ、追加作品として数えない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="十のコミック時代を進むスパイダーマン" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [イルミナティを題材にした架空のホラー](https://x.com/badboyfoxy/status/2106241189976387799) (作者 [@badboyfoxy](https://x.com/badboyfoxy))

**陰謀を題材にしたホラーを、架空の物語として扱う。**

作者は怖いイルミナティの動画を求め、完成作品を公開している。その題材はアニメーションのための架空のホラー設定である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="イルミナティを題材にした架空のホラー" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [コードによる核科学史の映画](https://x.com/imjustnewatai/status/2106238699872956427) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**独自のコード描画器と音楽で科学史の解説映像を作る。**

作者は核科学が原子爆弾を可能にした過程を三分の 3D 映画として依頼し、描画フレーム、独自レンダラー、合成音楽を報告している。ここでは視聴覚制作の工程を扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="コードによる核科学史の映画" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [ユニバーサル・ハイ・インカムの解説](https://x.com/markbraincell/status/2106234118514323515) (作者 [@markbraincell](https://x.com/markbraincell))

**アニメーションで経済の概念を伝える。**

投稿者はユニバーサル・ハイ・インカムを説明するアニメーションを共有している。映像は概念解説の具体例であり、描かれる経済的な主張を測定済みの成果には置き換えない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="ユニバーサル・ハイ・インカムの解説" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [Altman と Amodei の対立の解説](https://x.com/imjustnewatai/status/2106204392588276065) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**対立する立場をアニメーション解説の構造に使う。**

作者は Altman と Amodei の対立をアニメーションで説明するよう求め、成果を共有している。話題の解説形式の例であり、独自調査に基づく歴史記録ではない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="Altman と Amodei の対立の解説" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [Claude マスコットの音楽動画](https://x.com/synthshareai/status/2106195060140446028) (作者 [@synthshareai](https://x.com/synthshareai))

**提供された映像にマスコットを重ね、人物中心の音楽編集を作る。**

投稿者は実写の音楽動画を背景に Claude マスコットを重ねた作品を共有し、十二時間の実行を報告している。見える処理は、漫画的な重ね描きと既存映像を組み合わせている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="Claude マスコットの音楽動画" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [クォークから宇宙へ連続ズーム](https://x.com/imjustnewatai/status/2106190594775097663) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**連続ズームで複数の科学的な尺度を一つの物語にまとめる。**

作者はクォークから宇宙へ進む映像に、コードの描画と合成音楽を使ったと報告している。録画は連続する尺度の変化と一貫した視覚的な物語を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="クォークから宇宙へ連続ズーム" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [二〇七六年の世界を想像する](https://x.com/Layton_Gott/status/2106190496075035096) (作者 [@Layton_Gott](https://x.com/Layton_Gott))

**未来の世界に、具体的な映像の長さを指定する。**

作者は二十五秒の動画を依頼し、二〇七六年の世界を想像する短編を公開している。同じ録画を再利用した別のアカウントは、この出典にまとめている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="二〇七六年の世界を想像する" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [ロウアー・マンハッタンの建築年表](https://x.com/nroze22/status/2106183281293381661) (作者 [@nroze22](https://x.com/nroze22))

**敷地形状、建築年、高さを一つの建築タイムラインにまとめる。**

作者はロウアー・マンハッタンを建築図面風の画面で示し、建築年、建物の輪郭、高さを表示している。録画は具体的な対話型の年表構想を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="ロウアー・マンハッタンの建築年表" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [甲骨文字から始まるアニメーション](https://x.com/MinLiBuilds/status/2106180691344118202) (作者 [@MinLiBuilds](https://x.com/MinLiBuilds))

**文字の変遷を歴史アニメーションの題材にする。**

作者は甲骨文字から始まるアニメーションを共有している。録画は文字の歴史を中心にした視覚的な物語の具体例となっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="甲骨文字から始まるアニメーション" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [人物が美術史を進む別の作品](https://x.com/imjustnewatai/status/2106162924331180510) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**歴史が変わる中でも、馴染みの人物を案内役として使う。**

作者は Iron Man と Spider-Man が歴史を飛ぶ映像を依頼し、結果を共有している。他の作者による人物と美術史の実験とは別の作品である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="人物が美術史を進む別の作品" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [コードによるセイキロスの視聴覚作品](https://x.com/YanqingCheng/status/2106158746938269728) (作者 [@YanqingCheng](https://x.com/YanqingCheng))

**歴史的な音楽の文章を軸に、単一ファイルの視聴覚作品を作る。**

作者はセイキロスの墓碑銘を題材にした作品を公開し、一つの HTML と JavaScript ファイルで映像と音楽を合成したと報告している。歴史的な文章が全体の主題である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="コードによるセイキロスの視聴覚作品" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [ジェット機アニメーションの比較](https://x.com/Kinzf2121/status/2106158536963330346) (作者 [@Kinzf2121](https://x.com/Kinzf2121))

**同じ航空機の課題で、動きとカメラ追従を比べる。**

作者は Fable 5.1 と表示された結果と Opus のジェット機アニメーションを比較している。録画された場面は、航空機の動きと映画的なカメラ追従を比べる具体例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="ジェット機アニメーションの比較" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [モデルの自己紹介映画](https://x.com/devteamdrew/status/2106155815707021549) (作者 [@devteamdrew](https://x.com/devteamdrew))

**自己紹介の依頼で、モデルを題材にした映像を探る。**

作者は一つのプロンプトで自己紹介動画を求め、その映画を公開したと報告している。モデルを題材にした物語とアニメーション表現を組み合わせた課題である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="モデルの自己紹介映画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [終末世界のカードゲーム試作](https://x.com/maciejkrupowies/status/2106153578029338850) (作者 [@maciejkrupowies](https://x.com/maciejkrupowies))

**カードゲームの世界観を試作し、戦闘画面を観察する。**

作者は一度の生成とする終末世界の Hearthstone 風試作を共有している。小さな不具合を認めつつ、ゲームの画面と操作を示している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="終末世界のカードゲーム試作" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [職場アニメーション The Late Byte](https://x.com/rohit3a/status/2106138910648914094) (作者 [@rohit3a](https://x.com/rohit3a))

**モデルの人格を、職場で話すアニメーションの登場人物にする。**

作者は Opus を怒る上司として描いた職場物語 The Late Byte を公開している。別作品 Day in the Life of Claude とは異なる物語である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="職場アニメーション The Late Byte" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Queens of the Stone Age の歌詞動画](https://x.com/atomtanstudio/status/2106135196483608745) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**既存曲を動く文字とモーションデザインに組み合わせる。**

作者は Queens of the Stone Age の録音を使ったキネティック・タイポグラフィ動画を説明している。曲は提供された音声入力であり、この例は歌詞と映像の配置を扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Queens of the Stone Age の歌詞動画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [共有された Three.js の物語場面](https://x.com/Noreply134882/status/2106116572389478746) (作者 [@Noreply134882](https://x.com/Noreply134882))

**共有された 3D の物語映像を場面設計の参考にする。**

投稿者は Three.js の物語場面を共有し、多くのトークンを使うと述べている。添付映像を 3D の物語表現の具体的な共有例として残している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="共有された Three.js の物語場面" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [歴史を渡るムーンウォーク](https://x.com/noclipepe/status/2106105810812112937) (作者 [@noclipepe](https://x.com/noclipepe))

**舞踊のモチーフを、異なる時代と画風を通して継続する。**

投稿者は恐竜の時代から月へ進む Michael Jackson のムーンウォーク映像を共有している。ダンスと画風のギャラリーの共有例として扱っている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="歴史を渡るムーンウォーク" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [詳細な依頼によるモーショングラフィックス](https://x.com/devswha/status/2106100273509007802) (作者 [@devswha](https://x.com/devswha))

**細かな制作依頼と短いモーションの依頼を比較する。**

作者は素材、参考動画、ソースファイルを渡さず、詳しいプロンプトだけで作ったとするモーショングラフィックスを公開している。指示文からモーションを作る具体例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="詳細な依頼によるモーショングラフィックス" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [レンタル事業のウェブ画面](https://x.com/oalanicolas/status/2106098902965309475) (作者 [@oalanicolas](https://x.com/oalanicolas))

**レンタル業の依頼を使い、具体的なウェブ画面を探る。**

作者はレンタル事業向けサイトの画面を公開している。この例は、見えているページの設計と事業の見せ方を扱う。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="レンタル事業のウェブ画面" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [AGI を題材にした創作映像](https://x.com/AndrewOnXYZ/status/2106097745098395712) (作者 [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**繰り返す創作プロンプトで、物語と視覚表現を比べる。**

作者はいつものプロンプトから作った AGI を題材にしたアニメーションを公開している。モデルに関する台詞は創作の物語の一部として扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="AGI を題材にした創作映像" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [猫の脇筋を含む美術史](https://x.com/cherry_mx_reds/status/2106095190285144331) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**同じ人物を使い、多くの美術時代を短い物語へ圧縮する。**

作者は猫の脇筋がある十五秒の美術史映像を公開している。十五秒は動画の長さを指し、創作の課題自体は多くの歴史的な画風を扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="猫の脇筋を含む美術史" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [戦闘試作とボクセルの場面](https://x.com/OnlyTerp/status/2106089280502210626) (作者 [@OnlyTerp](https://x.com/OnlyTerp))

**ゲームの戦闘と世界設計を、一つの創作コーディング課題で見る。**

作者は DMC 風の戦闘試作とボクセル場面を共有し、長い生成実行を説明している。ゲームの仕組みと世界の視覚設計を観察する二つの具体的な出力である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="戦闘試作とボクセルの場面" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [インターネット・ミームの年表](https://x.com/chetaslua/status/2106076940558082297) (作者 [@chetaslua](https://x.com/chetaslua))

**年ごとの画風と音楽でアニメーション年表を構成する。**

作者は二〇一〇年から二〇二六年の流行したネットミームをアニメーションで公開している。各年の画風と音楽がコードによる物語を構成している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="インターネット・ミームの年表" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [一行から作る粒子の動き](https://x.com/devswha/status/2106072107365114186) (作者 [@devswha](https://x.com/devswha))

**まず一行のモーション依頼を試し、後から詳しい条件を加える。**

作者は一行のプロンプトで作った粒子のアニメーションを公開し、詳しい依頼も試したいと述べている。長いモーションデザイン作品とは別の生成である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="一行から作る粒子の動き" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [Kung-Fu Boy アニメーション](https://x.com/HashmathRzz/status/2106065773336965510) (作者 [@HashmathRzz](https://x.com/HashmathRzz))

**武術の人物という依頼で動きを探る。**

作者は Fable 5.5 に帰属する人物アニメーション Kung-Fu Boy を公開している。添付録画は武術を題材にした具体的な結果を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="Kung-Fu Boy アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [ホルムズ海峡の討論アニメーション](https://x.com/chetaslua/status/2106060047805792415) (作者 [@chetaslua](https://x.com/chetaslua))

**討論の題材をアニメーションの物語へ変える。**

作者はホルムズ海峡についてのアニメーション討論を公開している。ここで扱うのは見える討論映画であり、周辺の投稿で触れた他の未提示の用途ではない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="ホルムズ海峡の討論アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [ユニコーンの SVG 表現実験](https://x.com/atomtanstudio/status/2106057876053918127) (作者 [@atomtanstudio](https://x.com/atomtanstudio))

**同じ描画課題で SVG の表現の選択を観察する。**

作者は他の制作者のテストに触発されたユニコーン SVG 実験を共有している。添付画像は同じ題材の視覚処理を比較する具体的な出力である。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="ユニコーンの SVG 表現実験" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [ハロウィーンの季節アニメーション](https://x.com/cherry_mx_reds/status/2106056643255447590) (作者 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**コーディングモデルに季節の題材を渡し、短い映像を作る。**

作者はハロウィーンの作品を求め、完成した季節のアニメーションを公開している。投稿には、この創作課題の元の録画が含まれている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="ハロウィーンの季節アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Blender CLI の蛮族とカバー](https://x.com/BoDy051/status/2106047375320166885) (作者 [@BoDy051](https://x.com/BoDy051))

**Blender CLI の指示で人物のモデリングとカバー描画を試す。**

作者は RPG の蛮族人物とカバー構想を Opus の結果と比較している。Blender CLI が構築と描画を行い、モデルはコードの指示を出す工程である。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Blender CLI の蛮族とカバー" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Claude の一日](https://x.com/ishuagra02/status/2106045364868419727) (作者 [@ishuagra02](https://x.com/ishuagra02))

**繰り返し登場するマスコットで日常のアニメーションを作る。**

元の投稿者はマスコットを主役にした Day in the Life of Claude を共有している。この動画は、別のマスコットダンスやその再投稿とは異なる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Claude の一日" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [3D による人類史](https://x.com/blueemi99/status/2106041578204655748) (作者 [@blueemi99](https://x.com/blueemi99))

**コードの場面とアニメーションを歴史の映像に組み合わせる。**

作者は古代から現代までの人類を描く 3D 動画を公開し、アニメーションとモデルをコードで生成したと報告している。視覚的な物語の例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="3D による人類史" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [速いモーションデザイン作品](https://x.com/blueemi99/status/2106031355922387163) (作者 [@blueemi99](https://x.com/blueemi99))

**短いモーション作品のテンポ、音、一貫性を評価する。**

作者は短く速いモーション動画を公開し、音とまとまりを自身の Opus 出力と比較している。評価はこの具体的な作品の制作体験を述べたものである。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="速いモーションデザイン作品" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [自由な複雑 3D 作品](https://x.com/cocoloba_/status/2106029181607772413) (作者 [@cocoloba_](https://x.com/cocoloba_))

**自由な創作依頼で、複雑な 3D 構図を探る。**

作者は暇な時間があれば何を作るかと問い、完成した 3D 作品を公開している。投稿は生成された構図に多くの独立した部品があると説明している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="自由な複雑 3D 作品" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [棒人間の格闘アニメーション](https://x.com/HelaliBillel/status/2106028502763900944) (作者 [@HelaliBillel](https://x.com/HelaliBillel))

**具体的な格闘の依頼で、動きとタイミングを観察する。**

作者は棒人間が戦うアニメーション動画を求め、成果を共有している。添付録画は、その格闘アニメーション課題の具体的な例となっている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="棒人間の格闘アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [一つの依頼による UI モーション](https://x.com/iancarscadden/status/2106018048792789360) (作者 [@iancarscadden](https://x.com/iancarscadden))

**一つのアニメーション依頼で UI の連続した動きを探る。**

作者は一度の依頼で約六、七分かけて完成したとする UI モーションを公開している。録画はその依頼から得られた視覚的な流れを示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="一つの依頼による UI モーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [架空の SCP-8517 アニメーション](https://x.com/eviljoker88/status/2106003621402005816) (作者 [@eviljoker88](https://x.com/eviljoker88))

**SCP 風の設定をアニメーションの物語に使う。**

作者は SCP-8517 を題材にした作品を公開し、制作を Fable 5.5 に帰属している。ここでは架空の物語と見えるアニメーションを扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="架空の SCP-8517 アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [水彩の秋アニメーション](https://x.com/ishuagra02/status/2106000055706784118) (作者 [@ishuagra02](https://x.com/ishuagra02))

**季節の題材と水彩表現を一緒に指定する。**

作者は水彩風の秋のアニメーションを公開している。録画は、季節の題材と特定の視覚媒体を組み合わせる具体例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="水彩の秋アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [手続き型の人形ステージ](https://x.com/HelaliBillel/status/2105988689088196785) (作者 [@HelaliBillel](https://x.com/HelaliBillel))

**人形のような人物が舞台でどう動くか観察する。**

作者は手続き型の人形ステージ動画を共有し、付随する議論で Blender に触れている。ここでは見える舞台の人物と動きを扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="手続き型の人形ステージ" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [ブラウザーで動くペリカン](https://x.com/slimcat0101/status/2105988654636380444) (作者 [@slimcat0101](https://x.com/slimcat0101))

**人物の動きをブラウザーで実行し、描画された場面を見る。**

作者は自転車に乗るペリカンを求め、完成した HTML をブラウザーで実行する様子を録画している。静的 SVG の描画テストとは別の動く場面である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="ブラウザーで動くペリカン" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [宇宙が自らを見る](https://x.com/l_mejiaC/status/2105988529671360673) (作者 [@l_mejiaC](https://x.com/l_mejiaC))

**連続した視覚の旅で、遠く離れた尺度を物語につなぐ。**

作者はビッグバンから人間の目へ続く場面を公開している。映画の映像と音楽は、実行時のコードで制作したと説明している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="宇宙が自らを見る" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [独自のジェット機アニメーション実験](https://x.com/AI_Screening/status/2105988448612135176) (作者 [@AI_Screening](https://x.com/AI_Screening))

**航空機の課題を再実行し、その出力を観察する。**

作者はルーティングに関する話を見た後、ジェット機のアニメーションを試して共有している。この録画は航空機の例の独立した出典となる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="独自のジェット機アニメーション実験" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [最初の自由モーション作品](https://x.com/Saccc_c/status/2105985484472377531) (作者 [@Saccc_c](https://x.com/Saccc_c))

**短く自由な依頼でモーションデザインを試す。**

作者は一つのプロンプトで生成したとする最初のモーション作品を共有している。後の十五秒ポートフォリオとは別の、より早い時期の出力である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="最初の自由モーション作品" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [コードで描く文明史](https://x.com/ziwenxu_/status/2105983571848741045) (作者 [@ziwenxu_](https://x.com/ziwenxu_))

**文明史の依頼をコードによるアニメーション物語にする。**

作者は文明の始まりから現在までを求め、完成作品を公開している。既存映像やストック素材を使わず、コードで表現したと報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="コードで描く文明史" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [チップからサーバーへのズーム比較](https://x.com/SPAC89/status/2105968361725202591) (作者 [@SPAC89](https://x.com/SPAC89))

**ズームのリアリティーと場面の連続性を比べる。**

作者は Fable XHigh と GPT Sol Ultra の写実的なズーム映像を比較し、速度と使用枠にも言及している。異なる契約段階での具体的な実行の比較である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="チップからサーバーへのズーム比較" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [月旅行の個人アニメーション](https://x.com/IgorGomezC/status/2105963552024506565) (作者 [@IgorGomezC](https://x.com/IgorGomezC))

**複数のコーディングモデルで個人的な映像構想を試す。**

作者は Fable と Opus の実験に触れながら、個人的な月旅行のアニメーションを公開している。添付作品はその創作探索の具体的な出力である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="月旅行の個人アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [日本風ボクセル場面の比較](https://x.com/vikktorrrre/status/2105955048018588084) (作者 [@vikktorrrre](https://x.com/vikktorrrre))

**同じ場面の依頼で、細部、霧、見通しを比べる。**

作者は同じ日本風ボクセル場面のプロンプトで、現在の Fable と Opus を比較している。感想は、この出力の明瞭さ、霧、美的な処理を扱う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="日本風ボクセル場面の比較" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [視聴覚短編 Steaming the Frontier](https://x.com/sdmat123/status/2105929299878703520) (作者 [@sdmat123](https://x.com/sdmat123))

**Steamboat 風の映像依頼に音を組み合わせる。**

作者は音声付きのアニメーション Steaming the Frontier を共有している。他の作者による独立した Steamboat 風の出力とは別の出典である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="視聴覚短編 Steaming the Frontier" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [さまざまな画風を通るスーパーマン](https://x.com/Mr_Salio/status/2105925979466052051) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**同じ人物を、変化する画風の連続したアニメーションに登場させる。**

作者は以前のスーパーマンの例に触発され、新たに生成した自分の作品を公開している。画面が異なるため、再投稿ではなく別の創作である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="さまざまな画風を通るスーパーマン" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Cupcake 風ボス戦の試作](https://x.com/maciejkrupowies/status/2105914965387321785) (作者 [@maciejkrupowies](https://x.com/maciejkrupowies))

**横スクロールのボス戦を試作し、戦闘の結果を見る。**

作者は Cupcake 風のボス戦試作を共有し、十分未満で一度に生成したと報告している。添付録画にはゲームの戦闘場面が映っている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Cupcake 風ボス戦の試作" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [太陽が移動する帆船の場面](https://x.com/popat_kunj/status/2105907935490752822) (作者 [@popat_kunj](https://x.com/popat_kunj))

**航海の場面で空、水、太陽の位置を探る。**

作者は太陽の位置が変わる 3D 帆船の場面を公開し、操作できる作品へリンクしている。船、空、水を一つの視覚的な課題にまとめている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="太陽が移動する帆船の場面" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Paracortex と Pi の更新紹介映像](https://x.com/RobIW_dev/status/2105894547796476225) (作者 [@RobIW_dev](https://x.com/RobIW_dev))

**製品の更新を短いモーションデザインの告知へ変える。**

作者は Paracortex と Pi の更新を二十五秒のモーション動画へ変え、投稿にプロンプトも添えている。製品情報を視覚的に伝える例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Paracortex と Pi の更新紹介映像" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Curio 2.0 のサイト紹介動画](https://x.com/voltwake/status/2105884775982485642) (作者 [@voltwake](https://x.com/voltwake))

**既存サイトの公開に合わせ、コードで宣伝映像を作る。**

作者は Curio 2.0 の公開用動画を、コード映像、カメラ演出、音楽を組み合わせて制作したと説明している。投稿に完成したサイトの紹介動画がある。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Curio 2.0 のサイト紹介動画" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [想像上の Hugging Face 3D 物語](https://x.com/chetaslua/status/2105884276864782557) (作者 [@chetaslua](https://x.com/chetaslua))

**モデルのコードを描画と音声のツールに組み合わせ、架空の映画を作る。**

作者はモデルのコード、Blender、ElevenLabs API による架空の Hugging Face の物語を共有している。Blender が構築と描画、ElevenLabs が外部音声を担っている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="想像上の Hugging Face 3D 物語" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [Claude for Chrome で JS Paint を操作](https://x.com/BtwIUseSystemd/status/2105861662112923849) (作者 [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**ブラウザーエージェントに、アプリ内の道具だけを使う描画課題を与える。**

作者は Claude for Chrome に JS Paint の道具だけで人物を描くよう依頼し、画像を共有している。ブラウザー操作と描画アプリが明示された課題である。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="Claude for Chrome で JS Paint を操作" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [静的なペリカン自転車 SVG](https://x.com/olddonkeyblog/status/2105842745189556672) (作者 [@olddonkeyblog](https://x.com/olddonkeyblog))

**単一で完結する SVG の依頼で、細かな静止画を試す。**

作者は自転車に乗るペリカンを一つの自己完結した SVG にするよう求め、画像を公開している。走行アニメーションとは別の描画課題である。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="静的なペリカン自転車 SVG" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [BlockBench MCP と Minecraft スキル](https://x.com/TOPSTR1X/status/2105839618872738138) (作者 [@TOPSTR1X](https://x.com/TOPSTR1X))

**ゲーム人物の生成に、モデリング道具と画風スキルを渡す。**

作者は BlockBench MCP と独自の Minecraft モデリング・着色スキルを提供し、完成人物を共有している。道具と画風の指導が工程への明示的な入力である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="BlockBench MCP と Minecraft スキル" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [一つの HTML の Dig Dug](https://x.com/imjustnewatai/status/2105831117677084841) (作者 [@imjustnewatai](https://x.com/imjustnewatai))

**小型ブラウザーゲームの再制作で、単一 HTML を納品目標にする。**

作者は Dig Dug を一つの HTML ファイルで再現するよう依頼し、ゲームの録画を公開している。一つのプロンプトで作ったと述べている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="一つの HTML の Dig Dug" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [機械仕掛けのタコ SVG](https://x.com/SEO/status/2105812236774297943) (作者 [@SEO](https://x.com/SEO))

**機械的な生き物で SVG の細部と動きを観察する。**

作者は機械的な細部があるタコの SVG アニメーションを公開している。録画は、小さく動く部品を中心とした具体的なベクター設計の例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="機械仕掛けのタコ SVG" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [美術の画風を渡る Humanity Walks](https://x.com/l_mejiaC/status/2105801379956850793) (作者 [@l_mejiaC](https://x.com/l_mejiaC))

**同じ人物を歴史上のさまざまな画風へ導く。**

元の作者は約七十四秒で二十の美術画面を横切る連続歩行を公開し、コード音楽を報告している。境界を越えるたびに人物と場面の画風が変わる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="美術の画風を渡る Humanity Walks" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [自由な依頼のブラックホール](https://x.com/rohit3a/status/2105786053412208835) (作者 [@rohit3a](https://x.com/rohit3a))

**自由な創作の依頼でブラックホールの可視化を探る。**

作者は驚かせるなら何を作るかと問い、ブラックホールの場面を公開している。決まった画面の実装ではなく、自由な視覚の探索である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="自由な依頼のブラックホール" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [オーロラクラゲの動きの比較](https://x.com/SPAC89/status/2105783511433318451) (作者 [@SPAC89](https://x.com/SPAC89))

**二つのクラゲ映像で、変形と動きを比べる。**

作者は Fable XHigh と GPT Sol Ultra のオーロラクラゲのアニメーションを比較し、使用枠について述べている。結果は異なる契約段階から得られている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="オーロラクラゲの動きの比較" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Nintendo Switch の装着と起動 SVG](https://x.com/ishuagra02/status/2105779174921359470) (作者 [@ishuagra02](https://x.com/ishuagra02))

**一つの SVG 動画で、コントローラーの装着と起動を組み合わせる。**

作者はコントローラーが装着された後に起動ロゴが動く Nintendo Switch SVG を共有している。この実行を一分三十九秒、1.34 ドルと報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Nintendo Switch の装着と起動 SVG" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [対話型 3D 場面 The Loom](https://x.com/Mr_Salio/status/2105774088492916757) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**風景と建物を一つの操作できる 3D ページにする。**

作者は建物と風景がある対話型の場面 The Loom を公開している。録画は作者のテストで得られた具体的なページの出力である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="対話型 3D 場面 The Loom" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [同じプロンプトによるモーションデザイン映像](https://x.com/mesmerlord/status/2105758042830549235) (作者 [@mesmerlord](https://x.com/mesmerlord))

**同じプロンプトで制作した2本の映像で、視線の誘導とビートへの同期を比較します。**

作者は、同じプロンプトによる Fable 5.5 の初期モーションデザイン作品を2本共有し、Opus の試行よりも焦点が明確でビートへの同期も良いのではないかと慎重に述べています。元投稿の動画2本をまとめて掲載しています。

```
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

[@shneural](https://x.com/shneural/status/2103151003272962130)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="同じプロンプトによるモーションデザイン映像" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29b80ef5ba92b029630a1628.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0da5945bc240b424bfebbd9.jpg" alt="同じプロンプトによるモーションデザイン映像" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [整った見た目と弱い奥行き](https://x.com/eviljoker88/status/2105755840175034447) (作者 [@eviljoker88](https://x.com/eviljoker88))

**場面の比較では、否定的な美的評価も残す。**

作者は日本風の場面を並べて公開し、もう一方がすっきり見える点を認めつつ、Opus の出力の奥行きを好むと述べている。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="整った見た目と弱い奥行き" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [評価が分かれる日本風場面](https://x.com/eviljoker88/status/2105755408342126936) (作者 [@eviljoker88](https://x.com/eviljoker88))

**最初の比較を明確な勝敗とせず、良し悪しを記録する。**

作者は初回の日本風場面の比較を公開し、結果は一長一短と説明している。添付画像は、その美的な評価の基になった具体的な出力を残している。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="評価が分かれる日本風場面" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [コントローラー SVG の比較](https://x.com/notjazii/status/2105751542498464169) (作者 [@notjazii](https://x.com/notjazii))

**似た描画課題で、コントローラーの前後を比べる。**

作者は比較画像で、前後のコントローラー SVG を共有している。一般的なモデル順位ではなく、見える描画と表示の変化を扱う。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="コントローラー SVG の比較" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [産業機器の場面](https://x.com/RayaneRachid_/status/2105744517735354410) (作者 [@RayaneRachid_](https://x.com/RayaneRachid_))

**機械装置を、焦点を絞った 3D 場面の課題にする。**

作者は 3D の産業機器の場面を共有し、自分の一度の生成として最高の結果と述べている。添付画像は機械的な構図の具体的な参考となる。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="産業機器の場面" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [巨大な殻を持つエラ虫の再構成](https://x.com/Josh67Joshua/status/2105739832563769697) (作者 [@Josh67Joshua](https://x.com/Josh67Joshua))

**具体的な生物の説明で、二回の依頼による再構成を試す。**

作者は巨大な殻を持つエラ虫の絵を共有し、二回のプロンプトで得たと報告している。画像はこの生物設計課題の見える結果である。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="巨大な殻を持つエラ虫の再構成" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [二回の依頼による GameCube コントローラー](https://x.com/marmaduke091/status/2105735266032095349) (作者 [@marmaduke091](https://x.com/marmaduke091))

**身近なコントローラーで、二回の指示による描画を観察する。**

作者は GameCube コントローラーの絵を共有し、二回のプロンプトを使ったと報告している。この静的画像は Xbox や他のコントローラーの実演とは異なる。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="二回の依頼による GameCube コントローラー" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [X 投稿のためのスクリーンショット編集](https://x.com/chetaslua/status/2105733677003292983) (作者 [@chetaslua](https://x.com/chetaslua))

**助手が画像を SNS 投稿にどう合わせるか観察する。**

作者は X 投稿用のスクリーンショット編集を共有し、明示的に頼まずに助手が行ったと述べている。添付画像がその目に見える結果である。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="X 投稿のためのスクリーンショット編集" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [ボクセル桜の前後比較](https://x.com/kdnbmb/status/2105704791049412755) (作者 [@kdnbmb](https://x.com/kdnbmb))

**同じ題材で、連続したボクセル場面の出力を比べる。**

投稿者はボクセルの桜の島を二つの版で共有している。横並びの画像には、場面の前後で見える設計上の違いが記録されている。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="ボクセル桜の前後比較" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [SHADERKIN の布インターフェース試作](https://x.com/mszzz0011/status/2106025576972853642) (作者 [@mszzz0011](https://x.com/mszzz0011))

**画面の試作で、布の効果と調整できる項目を一緒に探る。**

作者は布の効果とパラメーター操作がある SHADERKIN の試作を公開し、一度の生成で作ったと述べている。録画は完成した画面と動きを示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="SHADERKIN の布インターフェース試作" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [共有された金色時計の画面アニメーション](https://x.com/AISuperDomain/status/2106396754539360272) (作者 [@AISuperDomain](https://x.com/AISuperDomain))

**時計を題材にした動画を画面構図の参考にする。**

投稿者は金色の時計を題材にしたフロントエンドのアニメーションを共有している。録画は画面構図、時計のモチーフ、動く視覚表現を観察する共有例である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="共有された金色時計の画面アニメーション" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [Before There Was Anything の物語](https://x.com/crowqnt/status/2106146218846081435) (作者 [@crowqnt](https://x.com/crowqnt))

**共有されたアニメーションで宇宙と人類の物語を探る。**

投稿者は宇宙と人類を題材にした Before There Was Anything を共有している。添付作品を、視覚的な物語の共有例として残している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="Before There Was Anything の物語" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [共有された青い粒子の渦](https://x.com/AISuperDomain/status/2105846981776003107) (作者 [@AISuperDomain](https://x.com/AISuperDomain))

**共有された渦の可視化で、粒子の動きと構図を見る。**

投稿者は青い粒子が渦を作るアニメーションを共有している。添付映像は、粒子の動き、視覚構造、構図を観察する具体的な共有例となる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="共有された青い粒子の渦" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [二回の修正を経た多画面インターフェース](https://x.com/ZorroOfMorocco/status/2106547078235095485) (作者 [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**最初の出力で止めず、修正を繰り返して画面を整える。**

作者は完成した複数パネルの画面を共有し、約三時間の作業と二回の修正を報告している。添付画像は最終的な視覚設計を示す。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="二回の修正を経た多画面インターフェース" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [動物を積み重ねた描画場面](https://x.com/legit_api/status/2117237103289315574) (作者 [@legit_api](https://x.com/legit_api))

**静的な構図で、複数の人物と異なる材質のバランスを観察する。**

投稿はクマ、パンダ、ホッキョクグマを積み重ねた場面を共有し、Discord の yuruzuu にクレジットし、二十一分の実行を報告している。公開投稿を視覚的な出典として残す。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="動物を積み重ねた描画場面" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [四つのオープンワールド RPG の比較](https://x.com/noclipepe/status/2117222592536789149) (作者 [@noclipepe](https://x.com/noclipepe))

**同じ創作課題で、ゲーム表現、戦闘、衝突の挙動を比べる。**

作者は一つのプロンプトで作った四つの RPG を、Fable 5.5、GPT-6.2 Astra、Opus 5.5、Fable 5.1 と表示している。照明、戦闘、持ち物、衝突、人物が止まる様子を比較する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="四つのオープンワールド RPG の比較" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [二つのフロントエンド動画の比較](https://x.com/leo114119/status/2117209849842761983) (作者 [@leo114119](https://x.com/leo114119))

**映像を並べて、場面設計と細部の描写を比べる。**

投稿は Astra と Fable のラベルがあるコード生成動画を並べ、細部と脚本に注目している。Fable のアニメーションを @chetaslua の作品と明記している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="二つのフロントエンド動画の比較" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [コードで生成した苔のロボット映画](https://x.com/chetaslua/status/2117169796290916732) (作者 [@chetaslua](https://x.com/chetaslua))

**アニメーションの依頼から、コードによる映画的な場面を探る。**

作者は森林とロボットのアニメーションを公開し、一度の生成によるコード映画と説明している。スクリーンショットのプロンプトへ案内し、他の試行と比較している。

追加の投稿では、別途報告された Opus 5.5 の対照実行を紹介している。 [@AnikaCodes](https://x.com/AnikaCodes) · [関連する作品](https://x.com/AnikaCodes/status/2117222374642946297)

作者によると、関連する GPT-6 Astra Max の実行では、制作過程に生成画像を使っている。元の短編と並べることで、制作方法の違いを確認できる。 [@rubenssoto_ai](https://x.com/rubenssoto_ai) · [関連する比較](https://x.com/rubenssoto_ai/status/2117707344704352691)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="コードで生成した苔のロボット映画" width="760"></a></td><td valign="top"><p>追加の投稿では、別途報告された Opus 5.5 の対照実行を紹介している。</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="コードで生成した苔のロボット映画" width="760"></a></td><td valign="top"><p>GPT-6 Astra Max</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/25b0cfcdb1fdda22ba6aa9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/75f37c74099d5b9ba1ad0ddc.jpg" alt="GPT-6 Astra Max" width="760"></a></td></tr></table>

[Framia の比較 · @FramiaPro](https://x.com/FramiaPro/status/2118287430751260694)

Framiaは、Chetaslua作と明記したFableの映像と、自社で制作したOpus 5.5のモーショングラフィックスを並べている。投稿は映像の比較で、共通の制作指示や条件を統一した検証手順は示されていない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/71788809537be865cc5d7f51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/1b28bd1dc2673319974e26bb.jpg" alt="Framia の比較" width="760"><br>▶ 動画を再生</a>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [コンテナ港のシミュレーション再制作](https://x.com/anxuanng/status/2117124831279972812) (作者 [@anxuanng](https://x.com/anxuanng))

**以前の場面を再制作するとき、比較できるようプロジェクトの文脈を残す。**

作者は別のコンテナ港を公開し、以前の Blender と Three.js のシミュレーションを引用している。旧作では戦略ゲーム風の環境向けに、クレーン、船、車両、コンテナをモデリングしている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="コンテナ港のシミュレーション再制作" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [空港エプロンの場面再制作](https://x.com/anxuanng/status/2117096574878921119) (作者 [@anxuanng](https://x.com/anxuanng))

**改訂した空港を、以前のプロジェクトと素材制作の流れで比べる。**

作者は空港エプロンへ戻り、以前の Blender と Three.js シミュレーションを引用している。飛行機、地上作業車、ターミナル施設を含む新しい映像を共有している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="空港エプロンの場面再制作" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [抽象的な 3D 世界を進むペリカン](https://x.com/xiax0603/status/2116960224829665543) (作者 [@xiax0603](https://x.com/xiax0603))

**自転車の題材で、異なる空間の間の場面転換を見る。**

投稿は幾何学的な破片と抽象的なデジタル環境を通り、最後に目から引いていくペリカンと自転車の映像を共有している。独自の場面転換の実演である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="抽象的な 3D 世界を進むペリカン" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [歴史的な帆船の場面](https://x.com/abhinavflac/status/2116945827738665060) (作者 [@abhinavflac](https://x.com/abhinavflac))

**船の場面で水、照明、環境の構図を観察する。**

投稿は歴史的な帆船の場面を共有し、操作できるゼロショットの結果と説明している。録画は船と周囲の水面の具体的な見本を示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="歴史的な帆船の場面" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [Carbon との走行と歩様の比較](https://x.com/AI_Screening/status/2116934172757660014) (作者 [@AI_Screening](https://x.com/AI_Screening))

**対応する出力で人物の動きと場面構成を比べる。**

作者は Fable と Carbon のラベルがある自転車とシマウマを合成動画に並べている。両チェックポイントは近いという感想とともに、動きを見る具体的な対の映像を示す。

以前の単独のサイクリスト比較も、合成映像と併せて収録している。 [@AI_Screening](https://x.com/AI_Screening) · [関連する作品](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="Carbon との走行と歩様の比較" width="760"></a></td><td valign="top"><p>以前の単独のサイクリスト比較も、合成映像と併せて収録している。</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="Carbon との走行と歩様の比較" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [清涼飲料ボトルの展示](https://x.com/abhinavflac/status/2116919086521499730) (作者 [@abhinavflac](https://x.com/abhinavflac))

**短い製品映像で材質、形状、見せ方を観察する。**

投稿は清涼飲料のボトル映像を共有し、一度の生成によるルーティング出力と説明している。映像のボトルを扱い、説明文で一貫しないブランド名は採用しない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="清涼飲料ボトルの展示" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [Astra と比べるペリカンの動き](https://x.com/Octoberry/status/2116918967558095131) (作者 [@Octoberry](https://x.com/Octoberry))

**対の映像で、リアリティー、色、動きの選択を比べる。**

投稿者は Fable と Astra のペリカン場面を並べ、写実性と色を述べている。比較録画には両方の視覚表現をそのまま残している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="Astra と比べるペリカンの動き" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [コード動画用モーションデザイン指示](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (作者 [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**動くタイトルや製品の導入映像を、具体的な設計指示から始める。**

投稿は導入、動くロゴ、タイトル、3D 場面のモーション設計指示を画像で共有し、Claude への適用を提案している。出典画像に元の指示が残っている。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="コード動画用モーションデザイン指示" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [写真を参照したボクセル肖像](https://x.com/chetaslua/status/2116912822806520027) (作者 [@chetaslua](https://x.com/chetaslua))

**参照写真の特徴をボクセルの肖像がどう保つか見る。**

作者は Sam Altman の写真とボクセル風肖像を並べ、一度の生成による結果と説明している。横並びの画像に参照と描画の両方がある。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="写真を参照したボクセル肖像" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [Opus と比べる飛ぶペリカン](https://x.com/leo114119/status/2116901575490929109) (作者 [@leo114119](https://x.com/leo114119))

**遊び心のある物の配置で、構図と動きの選択を比べる。**

投稿は Fable と Opus の、飛ぶペリカンの上に自転車がある映像を上下に並べている。Fable 側を @notjazii にクレジットし、両方の表現を表示する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="Opus と比べる飛ぶペリカン" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [Morning Ride のペリカン画面](https://x.com/leo114119/status/2116893571739775220) (作者 [@leo114119](https://x.com/leo114119))

**海辺の走行場面で、人物の細部とページの見せ方を観察する。**

作者は Morning Ride ページ内の 3D ペリカン走行場面を共有し、羽毛、足、自転車の細部、海辺の背景に注目している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="Morning Ride のペリカン画面" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [同じ指示と異なる画風の場面](https://x.com/notjazii/status/2116893197939224714) (作者 [@notjazii](https://x.com/notjazii))

**各モデルに画風を選ばせてから場面の構図を比べる。**

作者は同じプロンプトを両モデルに与え、それぞれに画風を選ばせたと報告している。動画は異なる場面構成と細部の程度を並べている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="同じ指示と異なる画風の場面" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [ペリカン、自転車、馬の構図](https://x.com/abhinavflac/status/2116881397986288017) (作者 [@abhinavflac](https://x.com/abhinavflac))

**一つの場面で、複数の対象をどう組み合わせて動かすか試す。**

投稿は、自転車を伴って飛ぶペリカンの下を馬が走る映像を共有している。添付映像は、この独特な複数物体の構図と動きを示す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="ペリカン、自転車、馬の構図" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [参照ツイートから作る等角場面](https://x.com/chetaslua/status/2116878661035106515) (作者 [@chetaslua](https://x.com/chetaslua))

**提供された投稿を参照に、新しい場面を構成する。**

作者は引用した Post Humans の投稿だけを参考にしたと述べ、等角投影の場面を公開している。動画には季節を切り替える操作がある農場風の構図が映る。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="参照ツイートから作る等角場面" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [ペリカン自転車の機構の接写](https://x.com/NFT_Chen/status/2116869725703782507) (作者 [@NFT_Chen](https://x.com/NFT_Chen))

**走行する対象のギア、羽毛、カメラの動きを観察する。**

投稿は水辺を自転車で進むペリカンの接写を共有している。録画は自転車の機構、鳥の頭、遊歩道を走る広い場面へと移る。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="ペリカン自転車の機構の接写" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [ペリカンに乗る自転車](https://x.com/notjazii/status/2116861637890379891) (作者 [@notjazii](https://x.com/notjazii))

**普段の主従関係を逆転し、アニメーションの空間構成を試す。**

作者はペリカンに乗る自転車の映像を共有している。飛ぶ鳥の上に自転車を置き、通常のペリカンが自転車に乗る課題を変化させている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="ペリカンに乗る自転車" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [Carbon と比べるペリカン SVG の画風](https://x.com/leo114119/status/2116652334734332212) (作者 [@leo114119](https://x.com/leo114119))

**写実性とイラスト風を比べ、美的な違いを一律の順位にしない。**

投稿は Carbon と Fable のペリカン自転車を並べている。作者はコミック風と写実的な描画を比較し、画風の違いで直接比較が難しくなると述べている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="Carbon と比べるペリカン SVG の画風" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [青い漫画鳥の自転車場面](https://x.com/birdabo/status/2116553049183560012) (作者 [@birdabo](https://x.com/birdabo))

**身近な漫画の人物が、自転車の構図でどう描かれるか見る。**

投稿は水辺で自転車に乗る青い漫画の鳥を共有し、Fable 5.5 Max と説明している。画像を具体的な静的見本として残す。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="青い漫画鳥の自転車場面" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [森の道を走るペリカンの画面](https://x.com/leo114119/status/2116154940364374269) (作者 [@leo114119](https://x.com/leo114119))

**ブラウザーの走行場面で羽毛、足、自転車の構造を見る。**

投稿者は森の道を自転車で走るペリカンのブラウザー画面を共有し、羽毛の質感、足、自転車の細部に注目している。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="森の道を走るペリカンの画面" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [Carbon と比べる棒人間の戦闘](https://x.com/leo114119/status/2116084152986656933) (作者 [@leo114119](https://x.com/leo114119))

**対のアニメーションで、戦いの演出と動きを比較する。**

比較録画には Fable 5.1 High と Carbon のラベルがある。作者は棒人間の格闘アニメーションの品質を相対的に論じている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="Carbon と比べる棒人間の戦闘" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [初期テストのペリカン SVG 参照](https://x.com/ChrisGPT/status/2115872567122608591) (作者 [@ChrisGPT](https://x.com/ChrisGPT))

**描き方と自転車の構造を見る際、出典付きの参照を残す。**

投稿者はペリカン自転車の画像を取り上げ、Discord の kostikz に出力をクレジットする初期テスト投稿を引用している。画像と出典関係を残している。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="初期テストのペリカン SVG 参照" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [モデル横断 SVG テストのペリカン参照](https://x.com/AdamHoltererer/status/2115858542221492300) (作者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**Fable の参照を、周囲の SVG テストの文脈と一緒に残す。**

投稿者は Mistral Large 4 の SVG テストスレッドに、Fable の参考としてペリカン自転車の画像を追加している。出典付きの画像で複数モデルを観察できる。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="モデル横断 SVG テストのペリカン参照" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [Carbon と比較する自転車 SVG の細部](https://x.com/insanekrishnaa/status/2115833723342250186) (作者 [@insanekrishnaa](https://x.com/insanekrishnaa))

**かご、背景、羽毛などの視覚的な特徴を個別に比べる。**

投稿は Fable と Carbon のペリカン自転車画像を比較し、かご、背景、羽毛を論じている。広い課題群ではなく、具体的な視覚評価である。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="Carbon と比較する自転車 SVG の細部" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [峡谷集落の 3D 場面](https://x.com/Mr_Salio/status/2115813400915714177) (作者 [@Mr_Salio](https://x.com/Mr_Salio))

**集落の場面で、環境の細部と空間構成を観察する。**

投稿は広い峡谷集落を共有し、新しい Claude チェックポイントの実演と説明している。映像に建物、風景、場面の構図が示されている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="峡谷集落の 3D 場面" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [Opus と比べるコントローラーの細部](https://x.com/notjazii/status/2115808169075351632) (作者 [@notjazii](https://x.com/notjazii))

**二つのコントローラーで形、操作部、細部を比べる。**

作者は Fable と Opus のコントローラー画像を並べ、上の描画の細部を強調している。対の画像にその比較が保存されている。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="Opus と比べるコントローラーの細部" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [毎週のウェブ SEO 監査フロー](https://x.com/cleeeeeeeeement/status/2115488774423773267) (作者 [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**サイトを優先順位付き SEO 計画と定期的な順位評価へ変える。**

作者はサイトから競合とキーワードを識別し、優先順位付き SEO 計画を作るシステムを開発したと報告している。毎週の順位追跡と実行の説明に短い録画が付く。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="毎週のウェブ SEO 監査フロー" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [Opus の映像で Fable の素材を再利用](https://x.com/chetaslua/status/2115145163542790170) (作者 [@chetaslua](https://x.com/chetaslua))

**モデルと道具を併用するとき、素材作りと映像編集を分ける。**

作者は、先に Fable が作ったとする素材を使った Opus 5.5 の Tesla Roadster モーションを共有している。引用した前の工程には Blender の Python、ElevenLabs、提供された紹介動画が挙げられている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="Opus の映像で Fable の素材を再利用" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [マンダラと幾何学のアプリ](https://x.com/ZMinimalistYogi/status/2114600083165434189) (作者 [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**絞った幾何学の発想を、創作できる対話型アプリにする。**

作者は Fable 5.1 と三時間対話し、マンダラ、ゾム、アルキメデスの立体、蓮形の幾何学ヤントラを作るアプリを開発したと報告している。個人サイトで公開している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="マンダラと幾何学のアプリ" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Three.js の自転車走行者](https://x.com/AI_Screening/status/2114266369248354357) (作者 [@AI_Screening](https://x.com/AI_Screening))

**自転車場面で、姿勢、構造、連動する動きを見る。**

作者は Three.js の自転車走行者を公開している。録画は具体的な動きの見本で、走行者の周囲に橋と水辺の風景がある。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Three.js の自転車走行者" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [FrontierCS 2 の評価スナップショット](https://x.com/wenhaocha1/status/2115613415641354262) (作者 [@wenhaocha1](https://x.com/wenhaocha1))

**出典リンク付きのベンチマーク図表を使い、Fable 5.1 と他のモデルを比較する。**

投稿者は FrontierCS 2 の課題通過率の図表に Fable 5.1 を追加し、報告された結果を他のモデルと並べて公開している。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="FrontierCS 2 の評価スナップショット" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [3モデルのシマウマアニメーション比較](https://x.com/AI_Screening/status/2115849659797373038) (作者 [@AI_Screening](https://x.com/AI_Screening))

**モデル名付きの3つの出力を並べて、疾走するシマウマの課題を比較する。**

投稿者は、Fable 5.5、Opus 5.5、Gemini 4 Argon と表記されたシマウマのアニメーションを並べて比較している。共有映像では、3つの出力の具体的な歩様サンプルを確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="3モデルのシマウマアニメーション比較" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [長い日本語文章への批評](https://x.com/AM09_21/status/2106670042184356156) (作者 [@AM09_21](https://x.com/AM09_21))

**生成された日本語の読みにくさをモデルに診断させる。**

作者は Opus の長い日本語文章が読みにくい理由を尋ねたと報告している。回答は英語的な構文、語の反復、表面的な推敲を挙げ、具体的な文章批評の例となっている。

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [作例で導く技術 PowerPoint](https://x.com/mt_moco/status/2106665038375522791) (作者 [@mt_moco](https://x.com/mt_moco))

**技術プレゼンを頼む前に、いくつかの作例を渡す。**

作者は数例のプレゼン資料を渡したところ、使える技術 PowerPoint が得られたと報告している。具体的な資料制作で、作例を使う依頼と構成改善を結び付けている。

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [音楽全体のまとまりを比較する](https://x.com/AM09_21/status/2106573080214770011) (作者 [@AM09_21](https://x.com/AM09_21))

**生成音楽の細部と作品全体の構成を分けて評価する。**

作者は音符、旋律、つなぎを通してモデルの作曲を比較し、局所的な一貫性と大きな楽曲構造を区別している。聴取体験に基づく作曲品質の評価である。

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [早すぎる完了報告と設計の不満](https://x.com/johntitorIII/status/2106442876506747353) (作者 [@johntitorIII](https://x.com/johntitorIII))

**エージェントの完了報告を受け入れる前に成果物を要件と照合する。**

作者は数日間のテストで、未完成の作業が完了扱いになり、設計も他のモデルに劣ったと報告している。早すぎる終了と設計品質についての実用的な失敗例である。

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [不快に感じたイカのアート](https://x.com/hanawo_neki/status/2106271036094415186) (作者 [@hanawo_neki](https://x.com/hanawo_neki))

**自由な絵の依頼が好みに合わない場合、求める美的方向を指定する。**

作者はイカの絵を自由に作るよう頼み、密集した細部に不快感を覚えたと報告している。自由度の高い視覚依頼における、好みとのずれを記録した例である。

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [設計図風のモーションデザイン](https://x.com/DavidayoAI/status/2106054662063325638) (作者 [@DavidayoAI](https://x.com/DavidayoAI))

**短い動画の視覚方向に、設計図の美的表現を指定する。**

作者は手早いアニメーションを頼み、約十五分後に設計図風の作品ができたと報告している。全作品への YouTube リンクがある。

[関連する作品](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [ボクセル桜の鳥と魚](https://x.com/xodud_rkd/status/2105876716472447046) (作者 [@xodud_rkd](https://x.com/xodud_rkd))

**ボクセルの風景で、動く野生動物を探る。**

作者は飛ぶ鳥と池の魚がいるボクセル桜の場面を説明し、操作できる作品へリンクしている。そのページがこの場面の出力である。

[関連する作品](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [人物生成の失敗報告](https://x.com/doof1789559/status/2105874208458752227) (作者 [@doof1789559](https://x.com/doof1789559))

**成功例と一緒に、人物生成の否定的な体験も記録する。**

作者は人物生成の結果が悪いと報告し、自分のやり方に原因がある可能性も明示している。人物の課題を評価するための具体的な否定例を残している。

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [時間と費用を添えたペリカン SVG](https://x.com/AnonymerNutze12/status/2105740440385499295) (作者 [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**描画作品に、作者が記録した時間と費用を添える。**

作者はペリカン SVG の HTML 作品へリンクし、その試行の時間と費用を報告している。リンク先が投稿で示された具体的な出力である。

[関連する作品](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [電話で遠隔操作する Claude Code 群](https://x.com/beistnormie/status/2106546741000417781) (作者 [@beistnormie](https://x.com/beistnormie))

**電話からコーディングエージェント群を遠隔監督する方法を探る。**

作者は旅行中に電話で Claude Code のエージェント群を遠隔操作していると報告している。個人の作業フローの記録であり、プロジェクトや実装の手順解説ではない。

Type: Integration | Date: 2026-10-04

---

<a id="case-280"></a>
### Case 280: [高山湖の上に広がる天の川](https://x.com/hakmgpt/status/2118178083983573492) (作者 [@hakmgpt](https://x.com/hakmgpt))

**山の反射と動く夜空を組み合わせた長いカメラシーケンスを確認する。**

公開された 92 秒のアニメーションは、高山湖から明るい天の川へ移り、再び水面に映る空へ戻る。投稿者は、このレンダリングされた場面を Fable 5.5 によるものとして紹介している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5cb879d0a07a0f6e9fff5cf6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/91432c6827d650eb28f2269b.jpg" alt="高山湖の上に広がる天の川" width="760"></a>

Type: Demo | Date: 2026-11-05

---

<a id="case-281"></a>
### Case 281: [手続き型の水と音によるクジラの跳躍](https://x.com/camperaigg/status/2118069524306284556) (作者 [@camperaigg](https://x.com/camperaigg))

**水中映像、水面からの跳躍、合成音声を一つのアニメーションにまとめる。**

制作者によると、手続き型のクジラ、流体シミュレーション、海面のシェーディング、合成音を含む 31 秒の短編を 154 分で制作した。制作記録では、フレームを拡大して確認し、水しぶきを修正してから再レンダリングした過程も説明されている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b98c309a3c226bd24386940f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1bcb86163b677ad0a4172d13.jpg" alt="手続き型の水と音によるクジラの跳躍" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-282"></a>
### Case 282: [4モデルのシマウマ動作比較](https://x.com/AI_Screening/status/2118014564457668955) (作者 [@AI_Screening](https://x.com/AI_Screening))

**同じ動物アニメーション課題で、歩容、体の構造、場面の表現を比較する。**

縦に並ぶ四つの映像には、Gemini 4 Carbon、Fable 5.5、Opus 5.5、Argon と表示されている。合成映像全体を保つことで、脚の動き、体形、背景処理の違いを同時に確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/6fdcb38bf56493c314dba5b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/890d1b92800ee622275ec8d7.jpg" alt="4モデルのシマウマ動作比較" width="760"></a>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-283"></a>
### Case 283: [Lightreelで自然言語からクリエイターを探す](https://x.com/lightreelai/status/2118010927199248705) (作者 [@lightreelai](https://x.com/lightreelai))

**フォロワー数と再生数の条件を明示したクリエイター検索クエリを作る。**

Lightreel は、このクリエイター探索デモを Fable 5.5 の名称で紹介している。動画では、フォロワーが 10,000 人未満で、100,000 回以上再生された動画を持つカップルのクリエイターを探すクエリを入力し、ソーシャル動画の検索結果を表示する。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5aef4b1766a560a35264c3ed.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1c6d9c1fb3c69b3aa2ee1976.jpg" alt="Lightreelで自然言語からクリエイターを探す" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-284"></a>
### Case 284: [雲海の上を飛ぶ船](https://x.com/devteamdrew/status/2118008142403649662) (作者 [@devteamdrew](https://x.com/devteamdrew))

**長めの短編で、光と天候が変わってもショットがつながるか確認する。**

制作者は、複数のエージェントチームが JavaScript と Python を使い、19 時間で約 100 秒のアニメーションを制作したと説明している。映像は、雲、夕焼け、月明かりの中を進む飛行船を追う。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/17ef07a780273abf9e9b6c92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a54746701db5f7f829071d2c.jpg" alt="雲海の上を飛ぶ船" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-285"></a>
### Case 285: [動きながら内部を見せる機械の心臓](https://x.com/camperaigg/status/2118002649929056373) (作者 [@camperaigg](https://x.com/camperaigg))

**主動作を続けたまま外装を開き、動く部品を見せる。**

制作者によると、Blender で 106 分かけて制作した。機械の心臓が金色の油を送り出し、外装が開いてピストンとクランクシャフトを見せる。制作記録には、音の合成と、不要なハイライトの原因が隠れたライトだったことを突き止める過程もある。

```
Make a mechanical heart and show its insides, use blender.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/157ebee3ce748cdc1e6b7970.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4a862111878dc42939f8e5e4.jpg" alt="動きながら内部を見せる機械の心臓" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-286"></a>
### Case 286: [歩いて探索できる浮遊ボクセル庭園と塔](https://x.com/legit_api/status/2117994730336252114) (作者 [@legit_api](https://x.com/legit_api))

**建物や水景の中を歩き、生成された環境を評価する。**

このボクセル庭園は、以前の Fable 5.5 チェックポイントによるものとして紹介されている。カメラは塔、浮島、橋、滝の間を進み、地上と高い位置の両方から場面を映す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/cc4d15bf5103d7eb64f63e29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/22e78c0beb2a6f509bc02739.jpg" alt="歩いて探索できる浮遊ボクセル庭園と塔" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-287"></a>
### Case 287: [8チームで制作した海の冒険短編](https://x.com/0xMovez/status/2117987052419428576) (作者 [@0xMovez](https://x.com/0xMovez))

**複数ショットの短編で、動き、効果、合成音のつながりを確認する。**

制作者によると、八つのエージェントチームが 3 時間未満で、39 ショットと合成音を含む 83 秒の Three.js 短編を制作した。映像では、宇宙船、海洋生物、砕ける波が登場する海の冒険が描かれる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a46543512fc30e5a33cb2fc3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a307daab219d70fa5bed0c86.jpg" alt="8チームで制作した海の冒険短編" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-288"></a>
### Case 288: [操作できるハイパーカーの展示](https://x.com/shmidtqq/status/2117977426990944736) (作者 [@shmidtqq](https://x.com/shmidtqq))

**車両の接写に、選択可能なカメラと塗装の操作を組み合わせる。**

制作者は、コードで形状とマテリアルを生成する Three.js のハイパーカー設定画面を、単一のオフライン HTML ファイルとして紹介している。録画には、赤い車両、ホイールと車体の接写、反射、カメラ操作が映っている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4bd439d08b9f8a320a8851ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a16368d4c8b7c9a3a5455607.jpg" alt="操作できるハイパーカーの展示" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-289"></a>
### Case 289: [生命の木の誕生](https://x.com/notjazii/status/2117972258090357164) (作者 [@notjazii](https://x.com/notjazii))

**種から大木への目に見える変化を軸に短いアニメーションを構成する。**

制作者によると、約 1 時間の、単一プロンプトによるコーディング実行だった。30 秒の映像は、荒れた土地、芽、成長する木へと進み、最後に雲の下の緑の世界を見せる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29df8c398a2db37856c01b0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f50b8e7c2a28df7d0d3cd903.jpg" alt="生命の木の誕生" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-290"></a>
### Case 290: [内部機械が動く歩行城](https://x.com/camperaigg/status/2117966825048997914) (作者 [@camperaigg](https://x.com/camperaigg))

**歩行リグを、目に見える機械の動作と開く外装に連動させる。**

制作者によると、蒸気機関、歯車列、四本の歩行脚、開閉する八枚の外装パネルを含む Blender の作業に 133 分かかった。制作記録では、カメラアニメーションの修正と、負荷の高い草の形状を見つけてレンダリング時間を短縮した過程が説明されている。

```
Make me Howl's moving castle and also show its internal machinery.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e7e25e7d44993a14ab0405e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8d3b1d734d971e2dd757926c.jpg" alt="内部機械が動く歩行城" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-291"></a>
### Case 291: [トーストのキャラクターと機械の甲虫](https://x.com/flxrnc/status/2117965294224232796) (作者 [@flxrnc](https://x.com/flxrnc))

**短い出会いのアニメーションで、登場人物の配置と連続性を確認する。**

公開された 40 秒の短編では、四角いトースト風のキャラクターが、夕暮れの野原で青い機械の甲虫に出会う。投稿では Fable 5.5 による短編として紹介され、モーションデザインのガイドにもリンクされている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/d5e16bfd05f1c391cf32f848.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b7ae776a5c29618d061465.jpg" alt="トーストのキャラクターと機械の甲虫" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-292"></a>
### Case 292: [嵐の中の灯台守](https://x.com/seeconvm/status/2117965120760365494) (作者 [@seeconvm](https://x.com/seeconvm))

**場所、天候の変化、明確な結末を軸に短い物語を作る。**

制作者は、コードで描画したフレーム、合成音、オフライン HTML ファイルを使った 60 秒の Three.js 短編と説明している。映像は、小さな灯台守を雨と雷の中で追い、最後に夜明けの場面へ移る。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/7ca3c1e23eac0ed20511211e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/dfcab72e07d547d9dcb1dbc1.jpg" alt="嵐の中の灯台守" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-293"></a>
### Case 293: [海辺の町と海の生き物](https://x.com/BubbleBrain/status/2117963042621178000) (作者 [@BubbleBrain](https://x.com/BubbleBrain))

**短編全体を通して、キャラクターの動き、場面転換、見た目の一貫性を確認する。**

投稿では、緑色の海の生き物、海辺の町、浮かぶ泡が登場する約 1 分の Fable 5.5 アニメーションが公開されている。この形式の短編を評価するための具体的な映像例になる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/65db346493bdd9973bec3a4c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4442bdca5e6a7460f03af731.jpg" alt="海辺の町と海の生き物" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-294"></a>
### Case 294: [3モデルによるラグ上のレース比較](https://x.com/noclipepe/status/2117914944410628430) (作者 [@noclipepe](https://x.com/noclipepe))

**同じレース課題で、遊べる場面の完成度、動き、視覚表現を比べる。**

制作者は、子どものころの道路柄ラグを使うレースゲームを、Fable 5.5、Opus 5.5、GPT-6 Astra で試している。最新の 3 画面録画と以前の 2 モデル比較を一緒に掲載しており、映像内の点数は制作者自身の評価である。

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ffe3b88099594ba14f536b51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/24d8ea7644cbe19947c8c53a.jpg" alt="3モデルによるラグ上のレース比較" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e214760ff83ad9bfaf202484.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0340fc5579003245dfa99b1.jpg" alt="3モデルによるラグ上のレース比較" width="760"></a></td></tr></table>

[関連する比較 · @noclipepe](https://x.com/noclipepe/status/2117729666576302187)

Type: Evaluation | Date: 2026-11-04

---

<a id="case-295"></a>
### Case 295: [トラックからロボットへの変形](https://x.com/camperaigg/status/2117914482752299311) (作者 [@camperaigg](https://x.com/camperaigg))

**変形シーケンスで、リグ、接地、音の同期を確認する。**

制作者によると、Blender の作業に 107 分かかり、51 関節のリグ、接地ソルバー、手続き型の雨、合成効果音を含む。録画は、濡れた路面でトラックが展開し、立ったロボットになる様子を映す。

```
Make me a transformer truck with animations of its transforming.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/72ef538a8fb4b94f0e2d7e2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ea8537c130cd5623959dc275.jpg" alt="トラックからロボットへの変形" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-296"></a>
### Case 296: [FableとHunyuanのアニメーションフレーム](https://x.com/xbquan/status/2117899651365908855) (作者 [@xbquan](https://x.com/xbquan))

**アニメーション全体を判断する前に、対応するフレームを比較する。**

作者は、Fable 5.5 と Hunyuan 4 と表示されたスクリーンショットを二組公開している。各組でキャラクターと環境の出力を並べ、実際に示されたフレームの見た目を比較できる。

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e6c6551a29757e1eb7c31f36.jpg" alt="FableとHunyuanのアニメーションフレーム" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/864db255f6fd2807b689d7d7.jpg" alt="FableとHunyuanのアニメーションフレーム" width="760"></td></tr></table>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-297"></a>
### Case 297: [光を分け与えるアニメーション](https://x.com/abhinavflac/status/2117883591019708740) (作者 [@abhinavflac](https://x.com/abhinavflac))

**抽象的なテーマを、結末が見える短い物語に変える。**

優しさとは何かを示すよう求められたモデルが、コードでアニメーションと音を制作したと紹介されている。光る人影が子どもに自分の光を渡すと、周囲の景色が色づくにつれ、その人影自身もさらに明るくなる。

```
Show me what kindness means to you
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b888d1a62b4d27ae2fca8226.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5bd15fc5c234b4b114765d6f.jpg" alt="光を分け与えるアニメーション" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-298"></a>
### Case 298: [山々の間に広がるボクセルの村](https://x.com/abhinavflac/status/2117377130388656569) (作者 [@abhinavflac](https://x.com/abhinavflac))

**さまざまなスケールで生成された村を探索し、空間のつながりを確認する。**

元の制作者は、家、水路、小さな住民がいる生き生きとしたボクセルの村を公開している。水辺、上空、周囲の山間からの映像で場面を確認できる。関連する中国語の投稿には、詳しい場面のプロンプトも掲載されている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae5269b0eff86da4580064d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e612faf20dd5f5de4ee171b.jpg" alt="山々の間に広がるボクセルの村" width="760"></a>

[@cfenghub](https://x.com/cfenghub/status/2117775332535148752)

Type: Demo | Date: 2026-11-02

---

<a id="case-299"></a>
### Case 299: [4モデルによるペリカンとゾウの構図](https://x.com/pipeline_os/status/2117719191478513700) (作者 [@pipeline_os](https://x.com/pipeline_os))

**複数の被写体が関わるアニメーションを、各モデルがどう構成するか比較する。**

4 画面録画では、ペリカン、自転車、ワニ、ゾウの課題を Gemini 4 Argon、Opus 5.5、Fable 5.5、Kimi K3.1 Pro で横並びに比較している。合成映像全体を残すことで、各モデルの被写体の配置と動きを確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/9db78999efffeffa7ccaca0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/15a45dc0efe3247f0821c8a2.jpg" alt="4モデルによるペリカンとゾウの構図" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-300"></a>
### Case 300: [インパクトフレーム付きアニメ風剣戟](https://x.com/camperaigg/status/2117717189059026969) (作者 [@camperaigg](https://x.com/camperaigg))

**キャラクターの動き、衝撃の閃光、音、意図的な無音を同期させる。**

制作者によると、66 分のコーディング実行で 46 秒の棒人間の戦闘を制作した。布のようなマント、対照的な武器、合成音楽と効果音を含み、制作記録には逆向きの攻撃、視覚的な軌跡、タイトル位置を修正した過程がある。

```
Make me a video of 2 stickman fighting, anime style.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/c36c188396aac371a64e31a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b670f06d376211c60bf894.jpg" alt="インパクトフレーム付きアニメ風剣戟" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-301"></a>
### Case 301: [4モデルの走るシカ比較](https://x.com/fawnunwrap/status/2117702487755100543) (作者 [@fawnunwrap](https://x.com/fawnunwrap))

**同じ課題の合成映像全体を見ながら、四肢の動きと動物の形を比較する。**

FawnBench は、報告上の Fable 5.5 の実行、Gemini 4 Argon、GPT-6 Astra、Opus 5.5 と表示した 4 画面で走るシカを見せる。これは映像による比較であり、測定された数値上の性能結果ではない。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3add4d9e0752d0467cbe6065.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/eea598747047797148e19c4e.jpg" alt="4モデルの走るシカ比較" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-302"></a>
### Case 302: [水没した街を進むロボット](https://x.com/0xMovez/status/2117700681867903169) (作者 [@0xMovez](https://x.com/0xMovez))

**反射、キャラクターの動き、変化するカメラ視点の連続性を確認する。**

制作者によると、コードで描画したフレーム、合成音、単一のオフライン HTML レンダリングファイルによる 42 秒の Three.js アニメーションである。ロボットが、水浸しで草木に覆われた街から、色鮮やかな開けた水面へ向かう。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f39e1807d1e80422c31530c6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/247f768636339f49d149c787.jpg" alt="水没した街を進むロボット" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-303"></a>
### Case 303: [Blenderの剣と紹介映像](https://x.com/camperaigg/status/2117694354685092255) (作者 [@camperaigg](https://x.com/camperaigg))

**手続き型のアセット制作と、その後のカメラ・音声作業を分けて確認する。**

制作者によると、まず一本の Python スクリプトで剣を生成し、その後で動画を依頼した。続く作業では、連続した Blender のカメラ移動、森の照明、合成した管弦楽曲、HyperFrames による編集を使い、報告された合計時間は 65 分である。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3c767f2038ef7d3960c956ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/525304dc7d4016ac33b3d4f8.jpg" alt="Blenderの剣と紹介映像" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-304"></a>
### Case 304: [Lantern Isleのピクセル村アニメーション](https://x.com/abhinavflac/status/2117693193429139965) (作者 [@abhinavflac](https://x.com/abhinavflac))

**密度の高いアニメーション環境で、地域の活動と昼夜の移り変わりを確認する。**

制作者は、住民、船、滝、ランタン、音楽を備えた、コードで描いた島の村を公開している。録画は、村の活動の接写、島全体の広い眺め、ランタンが光る夜の場面へと移る。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e91f1eabab743730dd815c98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b7d2e578739d25596db1164f.jpg" alt="Lantern Isleのピクセル村アニメーション" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-305"></a>
### Case 305: [Pauseのゲーム動画編集デモ](https://x.com/pausevfx/status/2117676887665447206) (作者 [@pausevfx](https://x.com/pausevfx))

**素材映像から字幕、編集可能なタイムラインまでの作業を確認する。**

Pause は、このワークフローを Fable 5.5 による動画編集の名称で紹介している。デモでは、ゲームの見どころを選び、顔出しカメラの構図を調整し、字幕と音を追加したうえで、Premiere に編集可能なシーケンスを開く。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0faaeecdaa02683f81e67f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae2d32876804bf286f11dc6c.jpg" alt="Pauseのゲーム動画編集デモ" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-306"></a>
### Case 306: [海辺を自転車で走るペリカン](https://x.com/pankajkumar_dev/status/2117301455665439210) (作者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**近景と広い視点の両方から、細かな形状とアニメーションを確認する。**

制作者は、海のそばでペニー・ファージングに乗るペリカンを公開している。録画は、羽、ペダル、車輪の形状を詳しく見せてから、舗装された海沿いの遊歩道を広く映す。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/66c3c44bcefa684522f95b96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8575912e8f20f48439aea683.jpg" alt="海辺を自転車で走るペリカン" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-307"></a>
### Case 307: [ワンカットで木星を縦断](https://x.com/camperaigg/status/2118246310981910811) (作者 [@camperaigg](https://x.com/camperaigg))

**光の変化に必然性を持たせ、シミュレーション領域の切り替わりを目立たなくする。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/58a20ee3fa71781622b8897a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/a798149fc001efc1b975e204.jpg" alt="ワンカットで木星を縦断" width="760"><br>▶ 動画を再生</a>

Camperaiggによると、Claude Codeへの一度の依頼で、木星を通り抜ける46秒の映像ができた。細くたなびく雲をシミュレーションし、暗転や閃光で場面をつなぎ、Pythonで音楽を合成したという。

Type: Demo | Date: 2026-11-05

---

<a id="case-308"></a>
### Case 308: [Claude Codeのハーネスで行う敵対的コードレビュー](https://x.com/marfinxx/status/2118313633381745064) (作者 [@marfinxx](https://x.com/marfinxx))

**レビュー担当エージェントの役割を分け、コミット前に署名付きのテスト証跡を必須にする。**

<table><tr><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/62e0a231bb29b701a331b7e0.jpg" alt="Claude Codeのハーネスで行う敵対的コードレビュー · 1" width="760"></td><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/3888b1f9db713d3b8be5fcf6.jpg" alt="Claude Codeのハーネスで行う敵対的コードレビュー · 2" width="760"></td></tr><tr><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/b5ccc0e785e50b4f260343aa.jpg" alt="Claude Codeのハーネスで行う敵対的コードレビュー · 3" width="760"></td><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/69053b5221a4a3896691b239.jpg" alt="Claude Codeのハーネスで行う敵対的コードレビュー · 4" width="760"></td></tr><tr><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d132b1486a11eee088ec4b48.jpg" alt="Claude Codeのハーネスで行う敵対的コードレビュー · 5" width="760"></td></tr></table>

Marfinは、隔離したGitワークツリー、機械可読なタスク契約、ツールの検査、差分から競合状態や境界ケースを探すFable 5.5のレビュー担当を組み合わせたClaude Codeの構成を紹介した。記事には設定、プロンプト、フックの例がある。

[チュートリアル全文](https://x.com/marfinxx/article/2118313633381745064)

Type: Tutorial | Date: 2026-11-05

---

<a id="case-309"></a>
### Case 309: [Three.jsで作る短編アニメ『Ryumon』](https://x.com/flxrnc/status/2118314922375331927) (作者 [@flxrnc](https://x.com/flxrnc))

**コードで描画する短編を、ショット構成、アニメーション、音響の作業に分ける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/b4465e8ea0d1e59a702ece4a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/665c00ab433daca60f6fa344.jpg" alt="Three.jsで作る短編アニメ『Ryumon』" width="760"><br>▶ 動画を再生</a>

作者は88秒のThree.js短編を公開した。7組のエージェントチームで39ショットと2,112フレームをコードで描画し、合成音声も含めて1つのHTMLファイルに収めたという。

[元のプロンプトとコード](https://x.com/flxrnc/status/2118314927681089619)

Type: Demo | Date: 2026-11-05

---

<a id="case-310"></a>
### Case 310: [雷雨の中を進む手こぎボート](https://x.com/camperaigg/status/2118317021935071339) (作者 [@camperaigg](https://x.com/camperaigg))

**波が来るタイミングと音の遅れをカメラの軌道に合わせる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/c717f78c1c94d6aa87a5b2cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8fd382dc1d7f48481aa98a61.jpg" alt="雷雨の中を進む手こぎボート" width="760"><br>▶ 動画を再生</a>

Camperaiggによると、Claude Codeへの1回の指示で、35秒のワンカット映像ができた。大波を物語の節目に合わせ、距離に応じて雷鳴を遅らせ、オールのリグとシミュレーション上の船の位置を修正している。

Type: Demo | Date: 2026-11-05

---

<a id="case-311"></a>
### Case 311: [オフライン短編アニメで雨粒を止める](https://x.com/seeconvm/status/2118319936594465120) (作者 [@seeconvm](https://x.com/seeconvm))

**オフラインで動く単一のHTMLプレーヤーで、時間を合わせたショットと合成音を再生する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/fc822df698c69770cbe394ad.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/f2ae8ab78b2917d38d2f10b4.jpg" alt="オフライン短編アニメで雨粒を止める" width="760"><br>▶ 動画を再生</a>

作者は、空中で雨粒が止まる50秒のThree.jsアニメを公開した。リンク先のプロジェクトには、元のプロンプト、コード、オフライン用プレーヤーがある。

[元のプロンプトとコード](https://x.com/seeconvm/status/2118319944714567938)

Type: Demo | Date: 2026-11-05

---

<a id="case-312"></a>
### Case 312: [BlenderとPythonで作るスクリプトアニメ](https://x.com/anstapnever/status/2118328801352466895) (作者 [@anstapnever](https://x.com/anstapnever))

**線画、彩色、合成オーケストラ音楽を組み込んだショット制作工程を組む。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/f8af6522676fd735dd4e2aa1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/b26fae93537f4e6c2a54bddb.jpg" alt="BlenderとPythonで作るスクリプトアニメ" width="760"><br>▶ 動画を再生</a>

作者は約90秒のアニメを公開し、44ショットを複数のエージェントが並行して制作したと述べている。BlenderとPythonで各フレームを描画して彩色し、合成したオーケストラ音楽を合わせている。

[元のプロンプトとコード](https://x.com/anstapnever/status/2118328806109053193)

Type: Demo | Date: 2026-11-05

---

<a id="case-313"></a>
### Case 313: [Three.jsで作る灯台アニメ『Beacon』](https://x.com/zodchiii/status/2118363287738073343) (作者 [@zodchiii](https://x.com/zodchiii))

**複数ショットからなる短編を、オフラインで使える1つのHTMLファイルにまとめる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/e25ff2a28c6efdc45bfc7b80.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d7d094bd606dd0e6b0bff2eb.jpg" alt="Three.jsで作る灯台アニメ『Beacon』" width="760"><br>▶ 動画を再生</a>

映像は、灯台を舞台に球形のロボットやおもちゃのようなキャラクターが登場する『Beacon』。作者によると、8組のエージェントチームが並行して39ショットを制作し、音楽と効果音を合成した。

Type: Demo | Date: 2026-11-05

---

<a id="case-314"></a>
### Case 314: [コードで描画したオープニング映像](https://x.com/devteamdrew/status/2118387876387766683) (作者 [@devteamdrew](https://x.com/devteamdrew))

**短いオープニングを作り、1回の制作指示でどこまで仕上がるか確かめる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/e53b379fe4b176845ce10601.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/5a3125a1f165bfa82e97725e.jpg" alt="コードで描画したオープニング映像" width="760"><br>▶ 動画を再生</a>

作者は約18秒のオープニングを公開し、1回の依頼から場面を設計、構築、レンダリングするまでに2時間強かかったと述べている。

Type: Demo | Date: 2026-11-06

---

<a id="case-315"></a>
### Case 315: [6フレームの斧のGIFをBlenderで再構築](https://x.com/camperaigg/status/2118410521363845534) (作者 [@camperaigg](https://x.com/camperaigg))

**側面から再現結果を確認し、リグとマテリアルも見せてもらう。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/99b2188373ec5287c16e40ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/dcadf8c7bac0f9630177dc48.jpg" alt="6フレームの斧のGIFをBlenderで再構築" width="760"><br>▶ 動画を再生</a>

Camperaiggによると、6フレームの斧振りを再現した後、Blenderモデルの確認を依頼した。側面から見ると斧の刃が薄すぎた。修正版では、クレイ表示、ワイヤーフレーム、マテリアル、リグを示した後、カメラがモデルの周囲を回る。

追加のプロンプト

```
it doesn't look very 3D, show me the actual Blender model
```

Type: Demo | Date: 2026-11-06

---

<a id="case-316"></a>
### Case 316: [2つのモデルで作るインタラクティブな虹色ゼリー](https://x.com/0xRhinoX/status/2118415577299460432) (作者 [@0xRhinoX](https://x.com/0xRhinoX))

**同じインタラクションを指定し、指示にない挙動を各モデルがどう扱うか比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/21235525e597105d4afa1c53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/4da95e15a1c4094b8f5b99d2.jpg" alt="2つのモデルで作るインタラクティブな虹色ゼリー" width="760"><br>▶ 動画を再生</a>

作者はFable 5.5とGemini 4 Carbonに、切る、釘を打つ、火であぶることができるゼリーを依頼した。Fable版は傷をつけると元に戻った。作者の記録では、Fableは48.50ドルで45分、Carbonは4.30ドルで32分だった。

Type: Evaluation | Date: 2026-11-06

---

<a id="case-317"></a>
### Case 317: [HTMLファイル1つのドラゴン飛行ゲーム](https://x.com/noisyb0y1/status/2118451983359311957) (作者 [@noisyb0y1](https://x.com/noisyb0y1))

**3Dプロトタイプを1つのHTMLファイルに収め、リンクからすぐ試遊できるようにする。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/0c57717bb7e652039107134f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/aa879655bb8f199adf91400d.jpg" alt="HTMLファイル1つのドラゴン飛行ゲーム" width="760"><br>▶ 動画を再生</a>

作者は、カメラを自由に動かせるドラゴン飛行ゲームを公開した。海と空はコードで生成され、軍艦がプレイヤーを砲撃する。完成版は2回目の依頼を経て制作された。

Type: Demo | Date: 2026-11-06

---

<a id="case-318"></a>
### Case 318: [Blenderの独自ソルバーでバスケットボールの落下を再現](https://x.com/camperaigg/status/2118673822459281765) (作者 [@camperaigg](https://x.com/camperaigg))

**跳ね返りの高さと変形を確認し、Blenderでシミュレーションを点検する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8e3cc422e63adc926c69807a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d7dc23722d696a126e5328b9.jpg" alt="Blenderの独自ソルバーでバスケットボールの落下を再現" width="760"><br>▶ 動画を再生</a>

Camperaiggによると、内圧のある薄殻を使って1.80 mからの落下をシミュレーションしたところ、ボールは1.32 mまで跳ね返った。追加の依頼でBlenderのビューポートでの解説が作られ、レンダリング済みのアリーナへ映像が切り替わる。

追加のプロンプト

```
shows off in a blender first and then transition into the arena
```

Type: Demo | Date: 2026-11-06

---

<a id="case-319"></a>
### Case 319: [スクリプトで作るアニメのフレーム点検](https://x.com/anstapnever/status/2118700618915397795) (作者 [@anstapnever](https://x.com/anstapnever))

**最終レンダリング前に、各フレームでオブジェクトのめり込みを確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/7c6bb5894aae3564edf04c09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8115bc37506ed9a23d6962fd.jpg" alt="スクリプトで作るアニメのフレーム点検" width="760"><br>▶ 動画を再生</a>

作者はBlenderとPythonで制作した92秒の映像を公開した。投稿では、エージェントによる43ショットの並行制作、スクリプトによる線画と彩色、フレームごとのめり込み検査、合成サウンドトラックが紹介されている。

[元のプロンプトとコード](https://x.com/anstapnever/status/2118700623004848474)

Type: Demo | Date: 2026-11-06

---

<a id="case-320"></a>
### Case 320: [マッチを擦る瞬間を44倍スローで再現](https://x.com/camperaigg/status/2118728540976009336) (作者 [@camperaigg](https://x.com/camperaigg))

**シミュレーション、レンダリング映像、音声を共通の時間軸に載せる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/3854b7f696993575e841539a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d97aaaec008adcc4387e72f9.jpg" alt="マッチを擦る瞬間を44倍スローで再現" width="760"><br>▶ 動画を再生</a>

Camperaiggは、GPUによる燃焼シミュレーション、マクロレンズ、合成音を使ったThree.jsのマッチ点火シーンを紹介した。エージェントは映像を見直し、炎の形に違和感があったため燃焼シミュレーションをやり直したという。

Type: Demo | Date: 2026-11-06

---

<a id="case-321"></a>
### Case 321: [参照画像をSVGで描き直す](https://x.com/dummerspast39/status/2118780483232317912) (作者 [@dummerspast39](https://x.com/dummerspast39))

**ベクターパスを確認し、描き直した結果を参照画像と見比べる。**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/873e762879e0c6ab5ea80151.jpg" alt="参照画像をSVGで描き直す" width="760">

作者は参照画像を渡し、SVGの出力結果をスクリーンショットで共有した。GPT-6.1 Solで構造を確認したと述べているが、元の投稿にSVGパスは掲載されていない。

Type: Demo | Date: 2026-11-07

---

<a id="case-322"></a>
### Case 322: [同じマリオ風の課題を2つのモデルに依頼](https://x.com/0xRhinoX/status/2118789381662429475) (作者 [@0xRhinoX](https://x.com/0xRhinoX))

**同じ制作指示のもとで、ステージの再現度と独自の設計を比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/9d964836dcc72ce880bbfbf1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/970bec8434d4db16547549bd.jpg" alt="同じマリオ風の課題を2つのモデルに依頼" width="760"><br>▶ 動画を再生</a>

作者のテストでは、Gemini 4 Carbonがマリオのステージを再現し、Fableは給水塔を修理するゲームを作った。作者によると、Carbonは0.90ドルで3分、Fableは34ドルで29分だった。

Type: Evaluation | Date: 2026-11-07

---

<a id="case-323"></a>
### Case 323: [立体ボクセルの塔](https://x.com/JaydenDavisNC/status/2118807627714990485) (作者 [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**複数のカメラアングルからボクセル建築を見て、奥行きとシルエットを確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/0e0dfb05333faf5a4fc0bdec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/f05509505248bbbd310f5738.jpg" alt="立体ボクセルの塔" width="760"><br>▶ 動画を再生</a>

作者はボクセルで作った立体の塔の短い映像を公開した。重なった屋根や全体の構図を映像で確認できる。

Type: Demo | Date: 2026-11-07

---

<a id="case-324"></a>
### Case 324: [Three.jsで燃える手紙の煙を表現](https://x.com/camperaigg/status/2119006297513435548) (作者 [@camperaigg](https://x.com/camperaigg))

**シミュレーションした煙に逆光を当て、フル解像度で圧力ソルバーを確認する。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/48d0b034652b734f6e387d8e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/0997278c25cd9c88aed47498.jpg" alt="Three.jsで燃える手紙の煙を表現" width="760"><br>▶ 動画を再生</a>

Camperaiggは、手紙が燃える30秒のショットを公開し、GPUで動かした粒子の煙、画面を横切る光、合成音を紹介した。作者は4つの質問に答え、エージェントが圧力ソルバーの数値計算エラーを修正したと述べている。

Type: Demo | Date: 2026-11-07

---

<a id="case-325"></a>
### Case 325: [稲妻を追って地面まで](https://x.com/camperaigg/status/2119052253982306393) (作者 [@camperaigg](https://x.com/camperaigg))

**シミュレーションの進行に合わせてカメラと音を動かす。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d6ee461c4cdf38ce8f5759a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/97c61bf20843530b450005e0.jpg" alt="稲妻を追って地面まで" width="760"><br>▶ 動画を再生</a>

Camperaiggは、Three.jsとTaichiを使った28秒のショットを紹介した。カメラは稲妻の先端を追い、音は放電の進行に合わせて変化する。フレームを走査するとストロボ状のちらつきが見つかり、エージェントが納品前に修正したという。

Type: Demo | Date: 2026-11-07

---

<a id="case-326"></a>
### Case 326: [隕石を受け止める巨大ロボット](https://x.com/seeconvm/status/2119052317227987018) (作者 [@seeconvm](https://x.com/seeconvm))

**コード駆動の映像をレンダリングする前に、ショットの担当と美術方針を決める。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/10c500daeecb0af61a05553e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/a509847ad05762e472a7096c.jpg" alt="隕石を受け止める巨大ロボット" width="760"><br>▶ 動画を再生</a>

作者は82秒のメカ短編を公開し、6組のチームの並行作業、36ショット、コードで描画した1,968フレームについて説明した。返信にはプロンプトとプロジェクトのコードも掲載している。

[元のプロンプトとコード](https://x.com/seeconvm/status/2119052321795551415)

Type: Demo | Date: 2026-11-07

---

<a id="case-327"></a>
### Case 327: [同じ課題で作るピクセルアートのショーウィンドウ](https://x.com/AIMind_Ai/status/2119053573526901001) (作者 [@AIMind_Ai](https://x.com/AIMind_Ai))

**細部を調整する前に、各モデルが出した未編集の演出を見比べる。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/c953d5e5c0e87fecdac9dcc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/ab064042073f1266b2f1caf1.jpg" alt="同じ課題で作るピクセルアートのショーウィンドウ" width="760"><br>▶ 動画を再生</a>

作者はFable 5.5とOpus 5.5に、3Dピクセルアートのクリスマス用ショーウィンドウを依頼した。Opusは装飾を加え、作者はFableの雪片を小さくして画面を見やすくした。投稿には両方の結果が並んでいる。

Type: Evaluation | Date: 2026-11-07

---

<a id="case-328"></a>
### Case 328: [アニメの街に現れる青銅の巨人](https://x.com/anstapnever/status/2119082173387137034) (作者 [@anstapnever](https://x.com/anstapnever))

**背景、キャラクター、エフェクト、音響を別々のチームに割り振り、並行して進める。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8ff966cd65fa2c2c5dd253e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/34679b2782af94de4f0ad237.jpg" alt="アニメの街に現れる青銅の巨人" width="760"><br>▶ 動画を再生</a>

作者はブラウザーで描画した77秒の短編アニメを公開し、5組のチーム、31ショット、各フレームのめり込み検査を紹介した。街と青銅の巨人が登場し、オーケストラの音楽が映像に同期する。

[元のプロンプトとコード](https://x.com/anstapnever/status/2119136411693777365)

Type: Demo | Date: 2026-11-07

---

<a id="case-329"></a>
### Case 329: [ガラスフラスコに広がる青インク](https://x.com/camperaigg/status/2119097552943612410) (作者 [@camperaigg](https://x.com/camperaigg))

**レンダリング前に粒子密度を調べ、流体シミュレーションの不具合を見つける。**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d6f3277ec1b19c7d45044e18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/ba7b4db94891d5a26a959423.jpg" alt="ガラスフラスコに広がる青インク" width="760"><br>▶ 動画を再生</a>

Camperaiggによると、Claude Codeへの一度の依頼で30秒のThree.js短編ができた。インクの流れをシミュレーションし、フラスコをレイトレーシングで描画し、1ショット内で再生速度を変える。縞状のノイズとインクの消失も点検している。

Type: Demo | Date: 2026-11-08

---

<a id="acknowledge"></a>
## 🙏 謝辞

このリポジトリは、Claude Fable 5 の実利用ケースを公開して共有してくれたクリエイター、開発者、ベンチマークチーム、コミュニティに着想を得ています。

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@hakmgpt](https://x.com/hakmgpt), [@camperaigg](https://x.com/camperaigg), [@lightreelai](https://x.com/lightreelai), [@0xMovez](https://x.com/0xMovez), [@shmidtqq](https://x.com/shmidtqq), [@flxrnc](https://x.com/flxrnc), [@seeconvm](https://x.com/seeconvm), [@BubbleBrain](https://x.com/BubbleBrain), [@xbquan](https://x.com/xbquan), [@pipeline_os](https://x.com/pipeline_os), [@fawnunwrap](https://x.com/fawnunwrap), [@pausevfx](https://x.com/pausevfx), [@marfinxx](https://x.com/marfinxx), [@anstapnever](https://x.com/anstapnever), [@zodchiii](https://x.com/zodchiii), [@0xRhinoX](https://x.com/0xRhinoX), [@dummerspast39](https://x.com/dummerspast39), [@AIMind_Ai](https://x.com/AIMind_Ai), [@AnikaCodes](https://x.com/AnikaCodes), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@cfenghub](https://x.com/cfenghub), [@shneural](https://x.com/shneural), [@FramiaPro](https://x.com/FramiaPro)

*すべてのケースが元の作成者へ確実に帰属していることは保証できません。修正が必要な点があればご連絡ください。更新します。*

さらに興味深い利用ケースを共有したい場合は、issue または pull request を開いて、Evolink usecase library の拡充にご協力ください。


[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
