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

## 🍌 소개

Claude Fable 5의 고신호 활용 사례 저장소에 오신 것을 환영합니다.

**우리는 공개 데모와 크리에이터 커뮤니티에서 큐레이션한 Claude Fable 5의 실제 사용 사례, 튜토리얼, 통합, 평가를 수집합니다.**

이 한국어 README는 구체적인 워크플로, 프롬프트, 데모, 통합, 벤치마크 근거 또는 실용적 한계를 갖춘 고신호 사례에 초점을 맞춥니다.

대부분의 사례는 X/Twitter 게시물과 공개 데모에서 큐레이션되었습니다. 각 사례 제목은 원본 소스로 연결되며, 각 작성자 핸들은 크리에이터 프로필로 연결됩니다.

Evolink에서 사용해 보기: [Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

## 📊 개요

- **기존 Fable 5 사례 88개와 커뮤니티 사례 191개, 총 279개 사례.**
- 코딩 에이전트, 장시간 자동화, 게임, 비주얼 디자인, 3D 시뮬레이션, 지식 작업, 튜토리얼, API 통합, 벤치마크, 가격, 출시 시점의 제한을 다룹니다.
- 각 사례에는 원본 소스, 크리에이터 출처, 간결한 핵심 요약, 근거 유형, 게시 날짜가 포함됩니다.
- 이 저장소를 활용해 실용적인 워크플로를 찾고, 강점과 한계를 비교하며, 재현 가능한 프롬프트를 발견하고, 통합 예시를 따라가세요.

> [!NOTE]
> 이 컬렉션은 과장보다 구체적 근거를 우선합니다: 재현 가능한 프롬프트, 출시된 데모, 벤치마크 방법, 통합 노트, 비용 데이터, 명확히 제시된 주의사항.

<a id="-quick-api-access"></a>
## ⚡ 빠른 API 접속

Evolink 호환 Messages API를 통해 Claude Fable 5를 사용할 수 있습니다. [Evolink](https://evolink.ai/login?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)에서 API 토큰을 받은 뒤 `<token>`을 해당 토큰으로 바꾸세요.

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

## 📑 메뉴

| 섹션 | 사례 |
|---|---|
| [💻 코딩 및 코드 생성](#coding-and-code-generation) | Case 1-6 |
| [🤖 에이전트 및 장시간 자동화](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 게임 및 인터랙티브 데모](#games-and-interactive-demos) | Case 9-12 |
| [🎨 비주얼, 디자인, 비디오 및 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 문서, 지식 작업 및 리서치](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 튜토리얼, 강좌 및 프롬프트 리소스](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 플랫폼, API 및 도구 통합](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 평가, 비교 및 한계](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | 크레딧 및 정정 정책 |

### [💻 코딩 및 코드 생성](#coding-and-code-generation)

| Case | 무엇을 보여주는가 | 유형 |
|---|---|---|
| [Cursor 다단계 워크플로](#case-1) | Fable 5를 다중 모델 Cursor 워크플로 안에서 계획 리뷰와 비평 단계로 사용한 뒤, 구현과 수정은 더 저렴하거나 특화된 모델에 다시 넘기세요. | 평가 |
| [스크린샷에서 GitHub 재현하기](#case-2) | 제품 스크린샷을 에이전트형 코딩 도구에 붙여넣고, Fable 5에게 실제로 작동하는 기능이 있는 인터페이스를 재현하게 하세요. | 데모 |
| [단일 프롬프트 블랙홀 시뮬레이션](#case-3) | Fable 5에 상세한 크리에이티브 코딩 프롬프트 하나를 주고, 자체 완결형 Three.js 물리 시각화를 만들게 하세요. | 튜토리얼 |
| [원샷 macOS 스타일 웹 OS](#case-4) | Fable 5에 완전한 단일 파일 웹 OS를 요청하고, UI 셸, 앱, 상호작용, 오디오, 내장 게임 동작을 한 번에 만들게 하세요. | 튜토리얼 |
| [1,687개 프롬프트로 Spawn 5.0 구축](#case-5) | Fable 5를 긴 세션의 엔지니어링 파트너로 여러 프롬프트에 걸쳐 사용하고, 사람의 역할을 아키텍처에서 출력 품질 판단으로 이동시키세요. | 튜토리얼 |
| [발견 사항이 포함된 대형 Pull Request 리뷰](#case-6) | Fable 5에 대형 pull request를 맡기고 정확성, false positive, 실제 버그, polish 문제를 리뷰하게 하세요. | 데모 |

### [🤖 에이전트 및 장시간 자동화](#agents-and-long-running-automation)

| Case | 무엇을 보여주는가 | 유형 |
|---|---|---|
| [장기 Relay 워크플로 리뷰](#case-7) | 사이트 재구축, 프로그래매틱 콘텐츠 파이프라인, 보이스 매칭, 보안 리뷰, 최종 품질 점검처럼 야심 찬 장기 작업에 Fable 5를 사용하세요. | 평가 |
| [인프라 장애 진단 및 수정 PR 생성](#case-8) | 로그, 데이터베이스 오류, 이미지 digest 같은 인프라 단서를 Fable 5에 제공하고, 장애를 진단하고 수정안을 준비하게 하세요. | 평가 |

### [🎮 게임 및 인터랙티브 데모](#games-and-interactive-demos)

| Case | 무엇을 보여주는가 | 유형 |
|---|---|---|
| [손가락 추적 Dino Runner](#case-9) | Fable 5에게 손가락 추적을 입력 메커니즘으로 사용하는 브라우저 게임을 만들게 하세요. | 데모 |
| [두 문장으로 만든 레이싱 게임](#case-10) | Fable 5에 매우 짧은 게임 프롬프트를 주고, 지도, 모드, 음악, UI, 게임 asset을 한 번에 생성하게 하세요. | 튜토리얼 |
| [Rust로 만든 설치 가능한 터미널 Minecraft](#case-11) | 터미널 코딩 harness를 통해 Fable 5를 실행하고, 설치 가능한 Rust 터미널 게임을 만들게 하세요. | 데모 |
| [시간과 비용을 포함한 Minecraft 클론](#case-12) | 하나의 프롬프트로 Fable 5에게 플레이 가능한 Minecraft 스타일 클론을 요청한 뒤, 시간, 비용, 코드량, 기능 범위를 평가하세요. | 튜토리얼 |

### [🎨 비주얼, 디자인, 비디오 및 3D](#visual-design-video-and-3d)

| Case | 무엇을 보여주는가 | 유형 |
|---|---|---|
| [완전 재현 가능한 이커머스 이메일 프롬프트](#case-13) | 정확한 섹션, 제품 요구사항, 비주얼 방향, 제약을 포함한 완전한 크리에이티브 브리프를 Fable 5에 제공해 브랜드 이메일 목업을 만들게 하세요. | 튜토리얼 |
| [Swiss Lever 시계 제작자 벤치마크](#case-14) | Fable 5를 기계식 시뮬레이션 벤치마크에 사용하고, 물리적 정확성을 구현, 검증, 반복하게 하세요. | 평가 |
| [Three.js Friends 아파트 장면](#case-15) | Fable 5에게 floor plan과 scene reference를 navigable Three.js 환경으로 바꾸게 프롬프트하세요. | 평가 |
| [프롬프트와 URL이 포함된 태양계 시뮬레이션](#case-16) | Fable 5를 사용해 물리 원리에서 천문 시뮬레이션을 만들고, 시뮬레이션과 공개 출력물이 준비될 때까지 반복하세요. | 튜토리얼 |

### [📚 문서, 지식 작업 및 리서치](#documents-knowledge-work-and-research)

| Case | 무엇을 보여주는가 | 유형 |
|---|---|---|
| [Stripe 및 과학 워크플로 근거](#case-17) | 이 사례는 복사-붙여넣기용 프롬프트가 아니라, 엔터프라이즈 마이그레이션과 과학 워크플로 주장에 대한 근거로 사용하세요. | 평가 |
| [정책 메모 및 변경 내용 추적 워크플로](#case-18) | 정책 분석 초안 작성 같은 장문 정성 문서 작업, 즉 변경 내용 추적, 댓글 triage, transcript 기반 편집에 Fable 5를 사용하세요. | 튜토리얼 |
| [Deep Research 프롬프트와 출력](#case-19) | Fable 5에 연구 스타일 질문을 던지고, 구조적이며 역사적 근거가 있는 긴 답변을 만들 수 있는지 평가하세요. | 데모 |

### [🧭 튜토리얼, 강좌 및 프롬프트 리소스](#tutorials-courses-and-prompt-resources)

| Case | 무엇을 보여주는가 | 유형 |
|---|---|---|
| [Fable 5가 Claude Code 워크플로를 바꾸는 방식](#case-20) | 모든 단계를 세세하게 지시하는 대신 방향, 맥락, 목표, 검증 기준을 설정해 Fable 5를 사용하세요. | 데모 |
| [10억 토큰 리뷰와 라우팅 전략](#case-21) | Fable 5를 frontier planning과 review에 사용한 뒤, 고볼륨 구현은 더 저렴한 모델로 라우팅하세요. | 튜토리얼 |
| [방어적 디바이스 하드닝 프롬프트](#case-22) | Fable 5가 디바이스를 inventory하고, 정확한 점검을 제공하며, 검증을 기다리는 단계별 방어적 hardening 프롬프트를 실행하세요. | 튜토리얼 |
| [전체 사이트 디자인 감사 Goal 프롬프트](#case-23) | `/goal`을 사용해 Fable 5가 사이트를 부팅하고, 페이지를 스크린샷으로 찍고, UX를 감사하고, 보고서를 쓰고, 안전한 작은 문제를 수정하게 하세요. | 튜토리얼 |
| [장문 창작 워크플로 분업](#case-24) | Fable 5가 안정적인 format과 examples를 설계하게 한 뒤, 그 구조를 다른 generation system에 넘겨 domain-specific output을 만들게 하세요. | 튜토리얼 |
| [Fable 5 사용 초보자 가이드](#case-25) | 작은 단계별 지시 대신 goal-oriented prompts, verification loops, effort settings와 함께 Fable 5를 사용하세요. | 평가 |
| [복사-붙여넣기 저장소 감사 프롬프트](#case-26) | 저장소 감사 프롬프트를 Fable 5에 붙여넣고, file-backed discovery, findings, strategy, milestone task plan을 요청하세요. | 튜토리얼 |
| [제한된 기간의 사용 전략](#case-27) | 접근 창이 유리할 때 Fable 5 사용량을 audit, architecture, planning에 쓰고, execution에는 더 저렴한 모델을 사용하세요. | 튜토리얼 |
| [Claude Code에서 Goals와 Workflows 사용하기](#case-28) | 구현 전에 Fable 5를 thought partner로 사용한 뒤, `/goal`과 workflows를 결합해 계획을 실행하고 검증하세요. | 튜토리얼 |

### [🔌 플랫폼, API 및 도구 통합](#platform-api-and-tool-integration)

| Case | 무엇을 보여주는가 | 유형 |
|---|---|---|
| [Hermes Agent 통합 설정](#case-29) | 복잡한 `/goal` 실행과 cached long-horizon tasks에 `anthropic/claude-fable-5`를 사용하도록 Hermes를 설정하세요. | 튜토리얼 |
| [기능, 가격 및 구독 관련 노트](#case-30) | Fable 5가 언제 사용 가능하고, 비용이 얼마이며, 어떤 guarded domains가 다른 모델로 fallback될 수 있는지 이해하는 데 이 사례를 사용하세요. | 튜토리얼 |
| [출시, 접근, 가격 및 안전 요약](#case-31) | 이 출시 요약을 사용해 access route, API model name, context window, caching strategy, subscription timing을 선택하세요. | 튜토리얼 |
| [Advisor 기반 비용 절감 전략](#case-32) | 추가 지능이 비용을 감당할 가치가 있을 때, 더 저렴한 모델 워크플로에서 Fable 5를 advisor 또는 reviewer로 사용하세요. | 통합 |
| [가격, 접근 및 안전 가드레일](#case-33) | workload를 계획하기 전에 Fable 5 access, API pricing, safety fallback behavior를 이해하는 데 이 사례를 사용하세요. | 통합 |
| [한 줄 Swarms 통합](#case-34) | Swarms model name을 `anthropic/claude-fable-5`로 설정하고 Swarms framework 또는 API를 통해 Fable 5를 실행하세요. | 통합 |

### [📏 평가, 비교 및 한계](#evaluations-comparisons-and-limits)

| Case | 무엇을 보여주는가 | 유형 |
|---|---|---|
| [Fable 5 vs GPT-5.5 비용 및 품질 비교](#case-35) | 같은 코딩 작업에서 Fable 5와 GPT-5.5를 비교해 출력 품질, 실행 시간, 도구 비용을 판단하세요. | 평가 |
| [AA-Omniscience 벤치마크 결과](#case-36) | 이 벤치마크 사례를 사용해 Fable 5의 knowledge accuracy와 hallucination behavior를 평가하세요. | 평가 |
| [Artificial Analysis Intelligence Index 결과](#case-37) | 이 사례를 사용해 Fable 5의 전체 intelligence ranking을 다른 frontier models와 비교해 벤치마크하세요. | 평가 |
| [GDPval-AA 에이전트형 지식 작업 벤치마크](#case-38) | 이 사례를 사용해 agentic real-world knowledge work에서 Fable 5를 평가하세요. | 평가 |
| [1주일 첫인상과 가격 메커니즘](#case-39) | 이 첫인상 사례를 사용해 Fable 5가 특히 game design과 systems planning에서 어디에 강한지 결정하세요. | 통합 |
| [비용 및 속도 비교](#case-40) | 이 비교를 사용해 quality gain이 더 높은 cost와 느린 long-horizon runs를 정당화하는지 판단하세요. | 평가 |
| [Claude Code 실사용 노트](#case-41) | tool use, personality, remaining rough edges를 포함해 Claude Code 안에서 Fable 5를 평가하는 데 이 사례를 사용하세요. | 데모 |
| [창작 글쓰기 벤치마크 결과](#case-42) | 이 벤치마크 사례를 사용해 Fable 5의 short-fiction writing quality와 refusal behavior를 판단하세요. | 평가 |
| [다중 벤치마크 출시 요약](#case-43) | 이 출시 벤치마크 요약을 사용해 coding agents와 complex tasks에 가장 관련 있는 headline scores를 이해하세요. | 평가 |
| [GPT-5.5와의 벤치마크 및 가격 비교](#case-44) | 이 비교를 사용해 price와 benchmark categories에서 Fable 5를 GPT-5.5와 비교 평가하세요. | 평가 |
| [실전 노트와 실용적 한계](#case-45) | 이 field report를 사용해 Fable 5가 어디에서 의미 있게 더 좋게 느껴지고, 어디에 여전히 실용적 한계가 있는지 이해하세요. | 튜토리얼 |
| [물리 시뮬레이션 비교](#case-46) | Fable 5와 Opus 4.8에 동일한 물리 시뮬레이션 프롬프트를 실행해 output quality, cost, speed를 비교하세요. | 데모 |
| [디버깅 경험과 디자인 판단력](#case-47) | 단순히 추측하게 하지 말고, measure, log, verify, patch하도록 요청해 Fable 5를 debugging에 사용하세요. | 데모 |
| [다차원 장단점](#case-48) | Fable 5를 daily driver로 만들기 전에 practical strengths and weaknesses를 이해하는 데 이 사례를 사용하세요. | 데모 |
| [법률 S-1 작성 테스트](#case-49) | S-1 drafting prompt를 legal-agent capability test로 사용하고 structure, formatting, length를 비교하세요. | 튜토리얼 |
| [헬스케어 벤치마크 세부 정보](#case-50) | 이 benchmark note를 사용해 healthcare-related tasks에서 Fable 5를 평가하고, 빠진 hard medical evals를 식별하세요. | 평가 |
| [ParseBench 문서 파싱 평가](#case-51) | 전문 OCR 시스템과 비교해 Fable 5가 document parsing에 cost-effective한지 결정하는 데 이 사례를 사용하세요. | 평가 |
| [SWE-Bench Pro 및 FrontierCode 비교](#case-52) | 이 벤치마크 사례를 사용해 migrations, complex implementations, autonomous sessions, tests, visual verification에서 Fable 5를 평가하세요. | 평가 |
| [장시간 문제 해결에 대한 정성 리뷰](#case-53) | 이 정성 리뷰를 사용해 Fable 5가 왜 longer, harder tasks에 적합한지 이해하되, production review는 여전히 필요하다는 점을 기억하세요. | 평가 |
| [ParseBench 충실도 및 서식 결과](#case-54) | 이 ParseBench 결과를 사용해 document faithfulness와 formatting performance를 판단하세요. | 평가 |
| [벤치마크, 가격, 접근 및 안전장치](#case-55) | 이 사례를 benchmarks, pricing, access, safeguards, strategic implications에 대한 넓은 checklist로 사용하세요. | 평가 |
| [공식 벤치마크 점수 목록](#case-56) | 이 benchmark list를 사용해 coding, computer use, security tasks 전반의 Fable 5 공식 점수를 이해하세요. | 평가 |
| [APEX-SWE 벤치마크 방법론](#case-57) | 이 사례를 사용해 APEX-SWE, 특히 observability와 integration work에서 Fable 5를 평가하세요. | 평가 |
| [ProofBench 형식 수학 결과](#case-58) | 이 사례를 사용해 specialized theorem-proving systems와 비교해 formal math에서 Fable 5를 평가하세요. | 튜토리얼 |
| [VirtueBench 예비 분석](#case-59) | 이 사례를 사용해 virtue categories 전반에서 Fable 5의 moral-reasoning behavior를 살펴보세요. | 평가 |
| [API 빈 응답 안전 과적합 테스트](#case-60) | 이 사례를 사용해 launch-time safety overfit risk와 API testing의 empty-response behavior를 이해하세요. | 평가 |
| [Fable 프롬프트 설계와 검증 가이드](#case-61) | 긴 프롬프트 요령 대신 목표, 맥락, 제약, 도구, 검증 루프를 정리하는 데 이 가이드를 활용하세요. | 튜토리얼 |
| [참조 이미지로 만드는 이스탄불 플랫폼 게임](#case-62) | 참조용 스프라이트 시트와 변환 지시 하나를 주고 Fable 5가 플레이 가능한 플랫폼 게임을 만드는지 시험하세요. | 데모 |
| [업무를 시각화하는 3D 도시 대시보드](#case-63) | Fable 5로 업무 흐름을 움직이는 3D 도시 대시보드 구상으로 바꿔 보세요. | 데모 |
| [Three.js 구멍 게임을 한 번에 제작](#case-64) | Fable 5로 Three.js 기반 3D 브라우저 게임 시제품을 한 번에 만들어 보세요. | 데모 |
| [DeepSWE 점수 비교](#case-65) | 이 DeepSWE 게시물을 출발점으로 소프트웨어 개발 벤치마크에서 Fable 5 xHigh와 GPT-5.5 xHigh를 비교하세요. | 평가 |
| [저장소 분석 비용 비교](#case-66) | 저장소 분석 비교를 통해 토큰 단가와 사람이 다시 작업하는 비용을 함께 판단하세요. | 평가 |
| [슈퍼 마리오 스타일 게임의 토큰 비용](#case-67) | 한 번에 만든 게임으로 Fable 5의 출력 품질과 토큰 소모량을 평가하세요. | 데모 |
| [Claude Code 대체 모델 전환 설정](#case-68) | Fable 5 메시지가 감지됐을 때 모델을 전환하는 Claude Code 설정을 확인하세요. | 통합 |
| [Namma Metro 시뮬레이터 제작](#case-69) | Fable 5로 대중교통 시뮬레이터를 만드는 간단한 바이브 코딩 사례로 살펴보세요. | 데모 |
| [프롬프트 하나로 만든 Dusk Drive](#case-70) | 사람의 수정 없이 로우 폴리 게임을 만드는 작업에서 Fable 5를 평가하세요. | 데모 |
| [APEX-Agents Pass@1 순위](#case-71) | APEX-Agents 결과를 통해 여러 단계의 자율 작업에서 Fable 5 Max를 비교하세요. | 평가 |
| [Claude 모델 선택 가이드](#case-72) | Claude Code의 가장 어려운 작업에 Fable 5를 남겨 두는 모델 선택 전략을 검토하세요. | 튜토리얼 |
| [HermesWorld 자동 에이전트 루프](#case-73) | 며칠 동안 구현, 테스트, 플레이, 기본 동작 확인을 이어가는 수동 조작 없는 Fable 5 루프를 살펴보세요. | 통합 |
| [McKinsey 스타일 보고서 프롬프트 검증](#case-74) | 문서 생성 프롬프트로 컨설팅 보고서의 구성, 차트, 논지, 위험 분석을 평가하세요. | 튜토리얼 |
| [안전장치 동작의 가시화](#case-75) | 공식 게시물에서 Fable 5 안전장치 표시, API 거부 사유, Opus 전환 동작을 확인하세요. | 통합 |
| [Claude Code 모델 이름 매칭 수정](#case-76) | Claude Code 변경 기록을 참고해 Fable 5 모델 이름과 컨텍스트 매칭 문제를 피하세요. | 통합 |
| [Claude Code로 웹 앱 세 개 제작](#case-77) | 여러 웹 앱을 생성한 초보자의 코딩 데모에서 Claude Code 안의 Fable 5 활용을 확인하세요. | 데모 |
| [오픈소스 앱 빌더 Rilable](#case-78) | iOS, 웹 앱, 샌드박스, API 토큰 비용을 아우르는 Fable 5 활용을 살펴보세요. | 통합 |
| [DeepSWE 코딩 에이전트 지수 데뷔](#case-79) | 공개 GitHub 수정 재활용을 피한 더 어려운 agentic coding tasks에서 Fable 5를 비교하기 위해 갱신된 Artificial Analysis 지수를 사용하세요. | Evaluation |
| [DataEmpire 웹 분석 게임](#case-80) | Claude Fable 5가 방문자와 이정표를 게임 엔티티에 매핑하게 해 원시 사이트 분석 데이터를 반복 플레이 가능한 게임으로 바꾸세요. | Integration |
| [FrontierSWE 20시간 작업 신호](#case-81) | Claude Fable 5가 짧은 버그 수정 루프뿐 아니라 매우 긴 엔지니어링 작업에서도 생산성을 유지할 수 있다는 근거로 FrontierSWE를 사용하세요. | Evaluation |
| [KernelBench-Hard CUDA 기록](#case-82) | 기존 라이브러리 래퍼가 아니라 저수준 최적화가 필요할 때 Fable 5를 고급 CUDA 커널 생성에 사용하세요. | Evaluation |
| [Figma Capture 랜딩 페이지 복제](#case-83) | 스크린샷 추측 대신 경쟁사 페이지를 Figma 레이어로 캡처하고, Claude Code와 Fable 5로 구조, 카피, 브랜드 시스템을 다시 구축하세요. | Integration |
| [두 시간 만의 GTA 2 클론](#case-84) | Claude Fable 5 코드 생성과 별도 asset tooling을 결합해 전체 스택을 손으로 코딩하지 않고도 플레이 가능한 3D 게임을 빠르게 만드세요. | Tutorial |
| [CloudWatch 로그 트리아지 에이전트](#case-85) | Fable 5 기반 에이전트가 매우 큰 서비스 로그 문맥을 읽고 아키텍처를 추론한 뒤 특정 장애로 범위를 좁히게 하세요. | Integration |
| [샌드박스 기반 월드컵 예측기](#case-86) | 여러 frontier models를 격리 샌드박스 뒤에 두고 공개 예측 앱을 위해 실시간 뉴스, 부상 정보, 옐로카드 맥락을 조사하게 하세요. | Integration |
| [WolfBench 거부 비용 사례](#case-87) | Claude Fable 5에서 장시간 자율 실행 비용을 산정할 때 refusal behavior를 실제 benchmark variable로 취급하세요. | Evaluation |
| [API 접근 중단 추적기](#case-88) | 레이트리밋이나 갑작스러운 중단 가능성이 있는 frontier model 접근에 의존한다면 스크립트로 availability를 모니터링하세요. | Integration |



### [🆕 Fable 5.5 커뮤니티 데모](#fable-5-5-community-demos)

| 사례 | 유형 |
|---|---|
| [코드로 생성한 소리 있는 여우 애니메이션](#case-89) | Demo |
| [자유로운 창작 지시에서 만든 애니메이션](#case-90) | Demo |
| [애니메이션이 있는 건설회사 웹사이트](#case-91) | Demo |
| [Three.js 자동차 프레젠테이션](#case-92) | Demo |
| [Minecraft 스타일 브라우저 게임 데모](#case-93) | Demo |
| [Three.js 펠리컨 자전거 애니메이션](#case-94) | Demo |
| [정확한 프롬프트가 있는 펠리컨 자전거 SVG](#case-95) | Demo |
| [질주하는 얼룩말 애니메이션 예시](#case-96) | Demo |
| [주문은 사람이 실행하는 TradingView 지표](#case-97) | Demo |
| [점 하나에서 펼쳐진 짧은 애니메이션](#case-98) | Demo |
| [여러 화풍을 넘나드는 슈퍼맨](#case-99) | Demo |
| [음악이 있는 인류 발전 애니메이션](#case-100) | Demo |
| [Opus와 비교한 공개 소개 영상](#case-101) | Evaluation |
| [가사와 사건을 영상으로 연결하기](#case-102) | Demo |
| [떠 있는 풍경 속 복셀 캐릭터](#case-103) | Demo |
| [3D 루브 골드버그 장치](#case-104) | Demo |
| [소리와 움직임이 있는 3D 컨트롤러](#case-105) | Demo |
| [JavaScript로 선보인 만화 캐릭터](#case-106) | Demo |
| [세계와 보스, 순위표를 갖춘 Updraft](#case-107) | Demo |
| [샌프란시스코 지도를 달리는 게임](#case-108) | Demo |
| [Seedance 액션 장면용 프롬프트 작성](#case-109) | Demo |
| [데스크톱 동료 도구의 소개 영상](#case-110) | Demo |
| [짧은 요청으로 바뀌는 화풍](#case-111) | Demo |
| [삼체 문제 시각화](#case-112) | Demo |
| [다양한 화풍의 애니메이션 갤러리](#case-113) | Demo |
| [로봇 동료와 절차적 털 표현](#case-114) | Demo |
| [수학을 주제로 한 모션 편집](#case-115) | Demo |
| [Your Woman 가사 영상](#case-116) | Demo |
| [음악 영상을 JavaScript로 다시 그리기](#case-117) | Demo |
| [중국 축구 애니메이션](#case-118) | Demo |
| [휴대용 게임기 리토폴로지 전시](#case-119) | Demo |
| [Minecraft와 Pokémon의 결합](#case-120) | Demo |
| [LLM 제작 과정을 설명하는 영상](#case-121) | Demo |
| [Altman 하이라이트 모션 편집](#case-122) | Demo |
| [삼십육계의 첫 번째 계책 영상](#case-123) | Demo |
| [게임 모델링, 리깅, 애니메이션](#case-124) | Demo |
| [아동 사망을 다룬 무언의 영화](#case-125) | Demo |
| [해당과정에서 에탄올까지의 SVG](#case-126) | Demo |
| [16대 Starship 동시 발사](#case-127) | Demo |
| [펠리컨 자전거 애니메이션 시험](#case-128) | Demo |
| [향후 150년의 이야기](#case-129) | Demo |
| [독립적인 Humanity Walks 실험](#case-130) | Demo |
| [코드로 만든 The Grader 영화](#case-131) | Demo |
| [공포 단편 Reawakening](#case-132) | Demo |
| [25초 자기 개선 영상](#case-133) | Demo |
| [성 장면과 사용 비용 피드백](#case-134) | Evaluation |
| [40초 브랜드 출시 광고](#case-135) | Demo |
| [Rocketball 리메이크](#case-136) | Demo |
| [복셀 탑 장면 비교](#case-137) | Evaluation |
| [상상 속 Switch 3 발표](#case-138) | Demo |
| [랜딩 페이지의 전후 비교](#case-139) | Evaluation |
| [상상한 AI의 내면 시점](#case-140) | Demo |
| [Go 가사 모션 디자인](#case-141) | Demo |
| [두 번째 15초 모션 포트폴리오](#case-142) | Demo |
| [에이전트 구현 계획 검토](#case-143) | Tutorial |
| [Claude 마스코트 댄스](#case-144) | Demo |
| [인터랙티브 세계 7대 불가사의 섬](#case-145) | Demo |
| [Propellerheads 음악 영상](#case-146) | Demo |
| [Steamboat Willie 애니메이션 비교](#case-147) | Evaluation |
| [싼싱두이 주제 영화](#case-148) | Demo |
| [Bugatti Chiron 전후 비교](#case-149) | Evaluation |
| [GRAIN 콘셉트 영화](#case-150) | Demo |
| [Human in Transit 미술 갤러리](#case-151) | Demo |
| [실크로드 시각 단편](#case-152) | Demo |
| [네 가지 전환을 다룬 발표 자료](#case-153) | Demo |
| [이전 대화와 말투 비교](#case-154) | Evaluation |
| [카카포 귀여움 비교](#case-155) | Evaluation |
| [만화의 열 시대를 지나는 스파이더맨](#case-156) | Demo |
| [일루미나티 소재의 가상 공포 영상](#case-157) | Demo |
| [코드로 만든 핵과학사 영화](#case-158) | Demo |
| [보편적 고소득 개념 해설](#case-159) | Demo |
| [Altman–Amodei 논쟁 해설](#case-160) | Demo |
| [Claude 마스코트 음악 영상](#case-161) | Demo |
| [쿼크에서 우주까지 이어지는 줌](#case-162) | Demo |
| [2076년의 세계 상상하기](#case-163) | Demo |
| [로어맨해튼 건축 연표](#case-164) | Demo |
| [갑골문 애니메이션](#case-165) | Demo |
| [캐릭터가 미술사를 지나는 다른 애니메이션](#case-166) | Demo |
| [코드로 만든 세이킬로스 시청각 작품](#case-167) | Demo |
| [제트기 애니메이션 비교](#case-168) | Evaluation |
| [모델 자기소개 영화](#case-169) | Demo |
| [종말 이후 카드 게임 프로토타입](#case-170) | Demo |
| [The Late Byte 직장 애니메이션](#case-171) | Demo |
| [Queens of the Stone Age 가사 애니메이션](#case-172) | Demo |
| [공유된 Three.js 서사 장면](#case-173) | Demo |
| [역사 속을 지나는 문워크](#case-174) | Demo |
| [상세 프롬프트 기반 모션 그래픽](#case-175) | Demo |
| [대여 사업 웹사이트 인터페이스](#case-176) | Demo |
| [AGI 소재의 창작 영화](#case-177) | Demo |
| [고양이 곁이야기가 있는 미술사](#case-178) | Demo |
| [전투 프로토타입과 복셀 장면](#case-179) | Demo |
| [인터넷 밈 연표](#case-180) | Demo |
| [한 줄로 만든 입자 움직임](#case-181) | Demo |
| [Kung-Fu Boy 애니메이션](#case-182) | Demo |
| [호르무즈 해협 토론 애니메이션](#case-183) | Demo |
| [유니콘 SVG 스타일 실험](#case-184) | Demo |
| [핼러윈 계절 애니메이션](#case-185) | Demo |
| [Blender CLI 야만인과 표지](#case-186) | Demo |
| [Claude의 하루](#case-187) | Demo |
| [3D로 보는 인류 역사](#case-188) | Demo |
| [빠른 모션 디자인 릴](#case-189) | Evaluation |
| [자유로운 복합 3D 창작](#case-190) | Demo |
| [막대인간 격투 애니메이션](#case-191) | Demo |
| [한 프롬프트로 만든 UI 모션](#case-192) | Demo |
| [가상의 SCP-8517 애니메이션](#case-193) | Demo |
| [수채화 가을 애니메이션](#case-194) | Demo |
| [절차적 인형 무대](#case-195) | Demo |
| [브라우저로 렌더링한 펠리컨](#case-196) | Demo |
| [우주가 자신을 바라보다](#case-197) | Demo |
| [독립적인 제트기 애니메이션 시험](#case-198) | Demo |
| [초기 자유형 모션 릴](#case-199) | Demo |
| [코드로 표현한 문명사](#case-200) | Demo |
| [칩에서 서버까지 확대 비교](#case-201) | Evaluation |
| [달 여행 개인 애니메이션 프로젝트](#case-202) | Demo |
| [일본풍 복셀 장면 비교](#case-203) | Evaluation |
| [Steaming the Frontier 시청각 단편](#case-204) | Demo |
| [여러 미술 양식을 통과하는 슈퍼맨](#case-205) | Demo |
| [Cupcake풍 보스전 프로토타입](#case-206) | Demo |
| [태양 위치가 달라지는 범선](#case-207) | Demo |
| [Paracortex와 Pi 변경 안내 영상](#case-208) | Demo |
| [Curio 2.0 사이트 홍보 영상](#case-209) | Demo |
| [상상 속 Hugging Face 3D 이야기](#case-210) | Demo |
| [Claude for Chrome의 JS Paint 사용](#case-211) | Demo |
| [정적인 펠리컨 자전거 SVG](#case-212) | Demo |
| [BlockBench MCP와 Minecraft 스킬](#case-213) | Demo |
| [하나의 HTML 파일로 만든 Dig Dug](#case-214) | Demo |
| [기계식 문어 SVG](#case-215) | Demo |
| [미술 양식을 지나는 Humanity Walks](#case-216) | Demo |
| [열린 요청으로 만든 블랙홀](#case-217) | Demo |
| [오로라 해파리 애니메이션 비교](#case-218) | Evaluation |
| [Nintendo Switch 결합과 부팅 SVG](#case-219) | Demo |
| [The Loom 인터랙티브 3D 장면](#case-220) | Demo |
| [벚꽃 탑 모션 샘플](#case-221) | Evaluation |
| [깔끔하지만 깊이가 부족한 풍경](#case-222) | Evaluation |
| [평가가 엇갈린 일본풍 장면](#case-223) | Evaluation |
| [컨트롤러 SVG 비교](#case-224) | Evaluation |
| [산업 장치 3D 장면](#case-225) | Demo |
| [거대한 껍질 아가미 벌레 재구성](#case-226) | Demo |
| [두 프롬프트로 그린 GameCube 컨트롤러](#case-227) | Demo |
| [X 게시물용 스크린샷 편집](#case-228) | Demo |
| [복셀 벚꽃 장면 전후 비교](#case-229) | Evaluation |
| [SHADERKIN 천 인터페이스 프로토타입](#case-230) | Demo |
| [공유된 금빛 시계 인터페이스 애니메이션](#case-231) | Demo |
| [Before There Was Anything 서사](#case-232) | Demo |
| [공유된 푸른 입자 소용돌이](#case-233) | Demo |
| [두 차례 수정한 다중 패널 화면](#case-234) | Demo |
| [동물을 쌓은 렌더링 장면](#case-235) | Demo |
| [네 가지 오픈월드 RPG 시도 비교](#case-236) | Evaluation |
| [두 프런트엔드 애니메이션 비교](#case-237) | Evaluation |
| [코드로 생성한 이끼 로봇 영화](#case-238) | Demo |
| [다시 만든 컨테이너 항구 시뮬레이션](#case-239) | Demo |
| [다시 만든 공항 계류장 장면](#case-240) | Demo |
| [추상 3D 세계를 지나는 펠리컨](#case-241) | Demo |
| [역사적 범선 장면](#case-242) | Demo |
| [Carbon과 자전거·보행 움직임 비교](#case-243) | Evaluation |
| [청량음료 병 제품 표현](#case-244) | Demo |
| [Astra와 펠리컨 움직임 비교](#case-245) | Evaluation |
| [코드 애니메이션 모션 디자인 지시](#case-246) | Tutorial |
| [사진을 참고한 복셀 초상](#case-247) | Demo |
| [Opus와 날아가는 펠리컨 장면 비교](#case-248) | Evaluation |
| [Morning Ride 펠리컨 웹 장면](#case-249) | Demo |
| [같은 프롬프트와 서로 다른 화풍](#case-250) | Evaluation |
| [펠리컨과 자전거, 말의 구성](#case-251) | Demo |
| [참조 게시물 기반 등각 장면](#case-252) | Demo |
| [펠리컨 자전거 기계부 접사](#case-253) | Demo |
| [펠리컨 위에 올라탄 자전거](#case-254) | Demo |
| [Carbon과 펠리컨 SVG 화풍 비교](#case-255) | Evaluation |
| [파란 만화 새의 자전거 장면](#case-256) | Demo |
| [숲길의 펠리컨 자전거 스크린샷](#case-257) | Demo |
| [Carbon과 막대인간 전투 비교](#case-258) | Evaluation |
| [초기 시험의 펠리컨 SVG 참조](#case-259) | Demo |
| [모델 간 SVG 시험의 펠리컨 참조](#case-260) | Evaluation |
| [Carbon과 자전거 SVG 세부 비교](#case-261) | Evaluation |
| [협곡 속 3D 정착지](#case-262) | Demo |
| [Opus와 컨트롤러 세부 비교](#case-263) | Evaluation |
| [주간 웹사이트 SEO 감사 흐름](#case-264) | Integration |
| [Opus 모션 디자인에서 Fable 자산 재사용](#case-265) | Integration |
| [만다라와 기하학 형태 앱](#case-266) | Demo |
| [Three.js 자전거 라이더](#case-267) | Demo |
| [FrontierCS 2 평가 스냅샷](#case-268) | Evaluation |
| [세 모델의 얼룩말 애니메이션 비교](#case-269) | Evaluation |
| [긴 일본어 문장의 가독성 비평](#case-270) | Evaluation |
| [예시로 유도한 기술 PowerPoint](#case-271) | Evaluation |
| [음악 전체의 일관성 비교](#case-272) | Evaluation |
| [성급한 완료 보고와 부족한 디자인](#case-273) | Limit |
| [불편함을 준 오징어 그림 결과](#case-274) | Limit |
| [청사진 스타일 모션 디자인](#case-275) | Demo |
| [복셀 벚꽃 속 새와 물고기](#case-276) | Demo |
| [캐릭터 생성 실패 보고](#case-277) | Limit |
| [실행 시간과 비용을 담은 펠리컨 SVG](#case-278) | Evaluation |
| [휴대폰으로 원격 코딩 스웜 감독](#case-279) | Integration |

<a id="coding-and-code-generation"></a>
## 💻 코딩 및 코드 생성

<a id="case-1"></a>
### Case 1: [Cursor 다단계 워크플로](https://x.com/AlicanKiraz0/status/2064487347605918180) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Fable 5를 다중 모델 Cursor 워크플로 안에서 계획 리뷰와 비평 단계로 사용한 뒤, 구현과 수정은 더 저렴하거나 특화된 모델에 다시 넘기세요.**

Fable 5와 GPT 5.5의 최종 점수를 보면 격차는 매우 작습니다. 제 소박한 사용 권장 방식은 이렇습니다. Cursor처럼 하이브리드 모델을 지원하는 IDE 플랫폼에서는 단계형 워크플로를 사용하세요.

Phase 1: 코드 리뷰와 프로젝트 점검의 첫 단계에서는 컨텍스트를 예열하면서 GPT 5.5 High, Minimax M3, Kimi K2.6, Composer 2.5 중 하나를 사용합니다.

Phase 2: 프로젝트 계획을 준비할 때는 GPT 5.5 Very High 또는 Opus 4.8을 사용합니다.

Phase 3: 프로젝트 계획을 분석할 때는 Fable 5를 사용하고, 계획의 결함 있는 부분을 찾아내게 합니다. 수정에는 GPT 5.5 Very High를 사용합니다.

Phase 4: 계획을 구현할 때는 Minimax M3, Deepseek v4 Max, Composer 2.5 또는 Sonnet 4.6을 사용합니다.

Phase 5: 최종 리뷰와 구현이 계획을 따랐는지 확인할 때는 GPT 5.5 High를 사용합니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [스크린샷에서 GitHub 재현하기](https://x.com/coldopn/status/2064435234465087638) (by [@coldopn](https://x.com/coldopn))

**제품 스크린샷을 에이전트형 코딩 도구에 붙여넣고, Fable 5에게 실제로 작동하는 기능이 있는 인터페이스를 재현하게 하세요.**

🚨 Anthropic Fable 5가 스크린샷만으로 GITHUB를 복제했습니다!!

제가 한 일은 GitHub UI 스크린샷을 Kilo Code에 붙여넣고, 실제 기능이 있는 GitHub를 다시 만들라고 지시한 것뿐입니다.

10분 동안 코딩했고 $4.07가 들었습니다.

결과는 작동하는 GitHub 복제본이었습니다: https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [단일 프롬프트 블랙홀 시뮬레이션](https://x.com/deveshcodes_/status/2064437742189379745) (by [@deveshcodes_](https://x.com/deveshcodes_))

**Fable 5에 상세한 크리에이티브 코딩 프롬프트 하나를 주고, 자체 완결형 Three.js 물리 시각화를 만들게 하세요.**

@claudeai가 Claude Fable 5로 Three.js 실시간 블랙홀 렌징 시뮬레이션을 원샷으로 만들었습니다.

중력 렌징, 도플러 증폭 강착 원반, 광자 구, 색수차, 절차적 별 배경이 포함되었습니다.

결과: 60fps, 단일 HTML 파일, 프롬프트 하나.

새 기준선이 말도 안 됩니다 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [원샷 macOS 스타일 웹 OS](https://x.com/intheworldofai/status/2064421915347812672) (by [@intheworldofai](https://x.com/intheworldofai))

**Fable 5에 완전한 단일 파일 웹 OS를 요청하고, UI 셸, 앱, 상호작용, 오디오, 내장 게임 동작을 한 번에 만들게 하세요.**

🚨 Claude Fable 5가 macOS 스타일의 완전한 웹 OS를 한 번에 만들었고, 대부분의 모델보다 더 멀리 갔습니다.

단일 HTML 파일, 내장 CSS + JS.

하나의 프롬프트에서 다음을 만들었습니다:

- macOS 메뉴 바 + dock
- 드래그와 크기 조절이 가능한 앱 창
- 작동하는 파일 탐색기
- 작동하는 터미널 + 브라우저 목업
- SVG 데스크톱 아이콘 + 알림
- Settings app, 테마, 부팅 화면
- 실제 합성을 사용하는 완전 작동 사운드 플레이어, 외부 파일 없음
- 데스크톱 안에서 플레이 가능한 Minecraft 클론

거의 수정 없이 한 번에 모두 생성되었습니다.

작동하는 사운드 플레이어와 실제 Minecraft 클론을 함께 해낸 것은 다른 모델에서 아직 본 적이 없습니다. Fable 5의 frontend/UI 생성 능력이 터무니없이 좋아지고 있습니다.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [1,687개 프롬프트로 Spawn 5.0 구축](https://x.com/jsnnsa/status/2064420561078693941) (by [@jsnnsa](https://x.com/jsnnsa))

**Fable 5를 긴 세션의 엔지니어링 파트너로 여러 프롬프트에 걸쳐 사용하고, 사람의 역할을 아키텍처에서 출력 품질 판단으로 이동시키세요.**

claude fable 5 is live.

spawn 5.0은 이것으로 만들어졌습니다:

- 1,687 prompts
- 102 sessions
- 제 역할은 아키텍처에서 취향 판단으로 바뀌었습니다

우리가 만든 것들입니다. 각각은 Opus에서 팀 전체가 붙어도 최소 한 달은 걸렸을 작업입니다:

- Rapier에 견줄 수 있고 사이드 스레드로 하루 만에 테스트 가능했던, 처음부터 만든 물리 엔진 Mantle
- Clustered froxel lighting: 8개 조명에서 1,000개 이상의 완전 동적 조명으로
- 휴대폰에서 돌아가는 WebGPU 기반 실시간 diffuse GI
- Unreal과 Unity가 제공하는 것 이상의 셰이더 아키텍처를 갖춘 백만 파티클 GPU VFX
- MMO 규모 netcode
- 알파 단계의 네이티브 iOS 앱

이 모든 것이 약 일주일 걸렸습니다. 전부 모바일에서 실행됩니다. 목록에는 실제로 배포된 것의 절반도 포함되어 있지 않습니다. 전체 changelog는 스레드에 있습니다.

벤치마크가 보여주지 못하는 부분: 이 모델은 성격이 훌륭합니다. 정말 웃깁니다. 물리 엔진을 다시 쓰는 도중 여러 번 너무 웃어서 울었습니다. 천재성과 캐릭터는 별개의 기능이 아닙니다.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [발견 사항이 포함된 대형 Pull Request 리뷰](https://x.com/ryanrhughes/status/2064411147076534705) (by [@ryanrhughes](https://x.com/ryanrhughes))

**Fable 5에 대형 pull request를 맡기고 정확성, false positive, 실제 버그, polish 문제를 리뷰하게 하세요.**

Fable 5에게 단일 PR(74 files / +3,705 / -1,246)을 마음껏 리뷰하게 해 보았습니다. 어떻게 하는지 보려는 목적이었습니다. 34분 동안 실행됐고, 제 5시간 세션의 42%를 소모했으며, 16개의 “correctness” 발견 사항을 냈고 다음을 찾아냈습니다:

- 무섭게 들리지만 false positive였던 것 2개
- 실제 audit-correctness 버그 3개
- 정당하지만 작은 UX/polish 문제 약 5개
- 여러 cleanup 의견

이게 출시하기엔 너무 위험했나요?

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 에이전트 및 장시간 자동화

<a id="case-7"></a>
### Case 7: [장기 Relay 워크플로 리뷰](https://x.com/JJEnglert/status/2064469635190170105) (by [@JJEnglert](https://x.com/JJEnglert))

**사이트 재구축, 프로그래매틱 콘텐츠 파이프라인, 보이스 매칭, 보안 리뷰, 최종 품질 점검처럼 야심 찬 장기 작업에 Fable 5를 사용하세요.**

제 Claude Fable 5 리뷰의 짧은 버전: Claude Fable 5를 테스트하는 데 10억 토큰을 썼고, 불공정한 이점을 가진 느낌이었습니다.

저는 눈으로 보는 테스트로 판단합니다. 모델을 실제 작업에 투입하고 지켜봅니다. 시간을 절약해 주는가, 아니면 시간을 잡아먹는가? 내가 놓친 것을 잡는가? 파트너처럼 느껴지는가, 아니면 계속 돌봐야 하는 도구처럼 느껴지는가?

이것은 오랜만에 중요한 모든 차원을 통과한 첫 모델이며, 그것도 조금이 아니라 확실히 통과했습니다.

빌드: 저는 Tenex 사이트를 다시 만들고 있었습니다. 매우 커스텀되어 있었고 매우 어려웠습니다. GPT 5.5와 Claude 4.8은 단독으로 해결하지 못했습니다. 참고할 Figma 파일이 있어도 85-90% 정도에서 멈췄습니다.

그런 다음 Fable 5가 모든 것을 살펴보고 더 잘할 수 있다고 말하더니, 원본 Webflow 소스로 곧장 가서 모든 asset을 다운로드했고 거의 한 번에 전체를 재현했습니다.

그 다음 주말 동안 완전히 새로운 80페이지 사이트를 처음부터 하나 더 만들게 했습니다. 에이전시로서라면 $50k를 청구했을 작업입니다.

또한 전체 프로그래매틱 클립 공장을 연결했습니다:

- HeyGen
- ElevenLabs
- Cloudflare
- A VPS

이 파이프라인은 주제를 찾고, 스크립트를 쓰고, 비디오를 편집하고, 음악을 추가하고, 소셜에 게시합니다. 오랫동안 스스로 실행되었고, 렌더를 모니터링하기 위한 webhook 시스템까지 자체 구축했습니다.

쓰기: 우리의 브랜드 보이스 문서를 거의 동일하게 복제한 뒤, 80페이지의 기능, 사례 연구, 기사 전반에서 그 보이스를 유지했고, 평면적인 AI 기본값으로 흐르지 않았습니다.

보안: 두 frontier 모델이 대형 repo에서 작업하고 코드에 승인까지 했었습니다. Fable 5는 첫 패스에서 심각하고 잘 숨겨진 버그를 찾아냈고 즉석에서 패치했습니다.

인간적인 순간: cron job을 기다리는 동안 질문을 했습니다. 답변한 뒤, 제가 약 10분 남았으며 끝나면 알려주겠다고 스스로 덧붙였습니다. 저는 타이머에 대해 묻지 않았습니다.

솔직한 단점: 어떤 모델보다도 미터기가 느껴집니다. Anthropic은 이것을 의도적으로 token-intensive하다고 부릅니다. 그래서 relay로 운용하세요: Fable 5로 생각하고, 더 저렴한 모델로 만들고, Fable 5로 리뷰하세요.

판결: 옆 사람보다 더 많은 지능에 접근할 수 있다는 것이 이점입니다. Fable 5는 그것을 현실로 만드는 첫 모델입니다. 풀 frontier 요금으로도 수익이 남았습니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [인프라 장애 진단 및 수정 PR 생성](https://x.com/ayushagarwal/status/2064422467557564862) (by [@ayushagarwal](https://x.com/ayushagarwal))

**로그, 데이터베이스 오류, 이미지 digest 같은 인프라 단서를 Fable 5에 제공하고, 장애를 진단하고 수정안을 준비하게 하세요.**

claude fable 5 is damn damn good!!!!

사이드 self-hosted infra에서 제가 제대로 설명조차 못 하던 장애를 방금 진단했습니다.

pod 로그를 읽고, Cloud SQL 오류 로그를 조회하고, 이미지 digest를 비교한 뒤, Kubernetes가 새로 마이그레이션된 데이터베이스에 대해 3개월 된 캐시 이미지를 실행 중이라는 것을 찾아냈습니다.

그 다음 수정 PR을 열었습니다.

몇 시간 아니라 몇 분. 웹 검색 없음. 🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 게임 및 인터랙티브 데모

<a id="case-9"></a>
### Case 9: [손가락 추적 Dino Runner](https://x.com/ai_for_success/status/2064413182396108932) (by [@ai_for_success](https://x.com/ai_for_success))

**Fable 5에게 손가락 추적을 입력 메커니즘으로 사용하는 브라우저 게임을 만들게 하세요.**

Fable 5에게 손가락 추적 Dino runner 게임을 만들어 달라고 요청했습니다.

약 11-12분 만에 finger runner 게임을 원샷으로 만들었고, 약 914K tokens를 소비했으며, 단 629 lines of code로 모든 것을 구현했습니다.

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [두 문장으로 만든 레이싱 게임](https://x.com/kieradev/status/2064482704763085202) (by [@kieradev](https://x.com/kieradev))

**Fable 5에 매우 짧은 게임 프롬프트를 주고, 지도, 모드, 음악, UI, 게임 asset을 한 번에 생성하게 하세요.**

Claude Fable 5, Max 5x 사용량의 40%.

2문장 프롬프트로 만든 완전한 Mario Kart 64 유형 게임.

Fable 5는 약 15분 만에 모든 장식, 캐릭터 모델, 4개 맵, 음악, 세 가지 게임 모드, UI를 한 번에 처리했습니다.

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Rust로 만든 설치 가능한 터미널 Minecraft](https://x.com/vikvang1/status/2064500731848319303) (by [@vikvang1](https://x.com/vikvang1))

**터미널 코딩 harness를 통해 Fable 5를 실행하고, 설치 가능한 Rust 터미널 게임을 만들게 하세요.**

Claude Fable 5를 Warp의 harness와 함께 한 시간 동안 돌려 보았습니다.

터미널에서 직접 렌더링되는 Minecraft의 TUI 버전을 만들었고, 전체가 Rust로 작성되었습니다.

Install command: cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [시간과 비용을 포함한 Minecraft 클론](https://x.com/ydamitcodes/status/2064536076518363353) (by [@ydamitcodes](https://x.com/ydamitcodes))

**하나의 프롬프트로 Fable 5에게 플레이 가능한 Minecraft 스타일 클론을 요청한 뒤, 시간, 비용, 코드량, 기능 범위를 평가하세요.**

@claudeai Fable 5가 37분 만에 Minecraft 클론을 만들어 줬습니다.

프롬프트 하나. 약 3K lines of code. API 비용 $12.

biomes, caves, ores, day/night, mobs, 전부 포함했습니다.

Minecraft는 Notch가 2년 걸렸습니다.

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 비주얼, 디자인, 비디오 및 3D

<a id="case-13"></a>
### Case 13: [완전 재현 가능한 이커머스 이메일 프롬프트](https://x.com/ecomchasedimond/status/2064454139225297091) (by [@ecomchasedimond](https://x.com/ecomchasedimond))

**정확한 섹션, 제품 요구사항, 비주얼 방향, 제약을 포함한 완전한 크리에이티브 브리프를 Fable 5에 제공해 브랜드 이메일 목업을 만들게 하세요.**

Claude Fable 5는 단일 프롬프트와 무수정으로 이것을 만들었습니다.

제가 사용한 전체 프롬프트는 다음과 같습니다:

밀레니얼을 위한 현대적인 시계 및 액세서리 브랜드 MVMT의 전체 길이, 세로형 이커머스 이메일 목업을 만드세요.

매끈하고, 정제되어 있으며, 미니멀하고, 남성적인 방향성이 있고, editorial한 느낌의 매우 사실적인 premium DTC 이메일을 디자인하세요. 최종 이미지는 포스터도, landing page도, generic template도 아니라 실제 디자이너가 만든 이커머스 이메일 스크린샷처럼 보여야 합니다.

Brand vibe: Modern California-cool, 젊고, 자신감 있고, 깔끔하며, 열망을 자극하고, 스타일리시하고, elevated. 디자인은 luxury-adjacent하지만 여전히 접근 가능하게 느껴져야 합니다.

다음 제품을 눈에 띄게 포함하세요:

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

Color palette: Black, white, charcoal, warm gray, stone, soft beige, brushed metal tones, and subtle muted accents. 팔레트는 neutral하고 premium하게 유지하세요.

중요한 creative direction: 이것은 강한 디자인 감각을 가진 세련된 watch-brand email campaign처럼 느껴져야 합니다. realism, elegance, clarity를 우선하세요. MVMT가 실제로 보낼 수 있을 법하게 만드세요.

이 순서로 이메일을 구성하세요:

1. Top promo bar: 상단을 가로지르는 얇은 black 또는 dark charcoal bar, 작은 uppercase text: “FREE SHIPPING OVER $75 + EASY RETURNS”.

2. Header: 왼쪽의 MVMT wordmark/logo와 오른쪽 또는 중앙의 minimal navigation links가 있는 clean white header: WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS.

3. Hero section: 강한 visual balance를 가진 premium hero section.

Bold headline을 사용하세요: “BUILT TO GET NOTICED”.

일상 스타일을 높여 주는 modern timepieces and accessories에 대한 짧은 supporting copy를 포함하세요.

Dark rounded CTA button을 추가하세요: “SHOP WATCHES”.

Hero imagery에는 다음이 포함되어야 합니다:

- one dominant premium watch image
- subtle luxury lifestyle imagery
- a stylish male model or fashion-forward masculine lifestyle scene
- modern lighting and clean composition

4. Featured collection section: 중앙 정렬 section headline을 추가하세요: “THREE WAYS TO WEAR MVMT”. 그 아래에는 다음을 보여주는 clean product cards 또는 image blocks 3개를 배치하세요:

- Mulholland
- Odyssey II Automatic
- Cali Diver

각 block에는 다음이 포함되어야 합니다:

- product image
- product name
- short one- or two-line description

이 section은 symmetrical, polished, premium하게 유지하세요.

5. Accessory banner: “FINISH THE LOOK”라는 제목의 refined split section을 추가하세요. Signature Watch Bands를 featured로 보여 주세요. watch straps 또는 interchangeable bands의 premium close-up imagery를 보여 주세요. 짧은 supporting copy와 dark CTA button을 포함하세요: “SHOP ACCESSORIES”.

6. Editorial promo tiles: 이미지 중심 디자인의 side-by-side promotional tiles 2개를 추가하세요.

Tile one headline: “FOR DAILY WEAR”.

Tile two headline: “FOR STATEMENT DAYS”.

각 tile에는 짧은 copy와 작은 CTA가 있어야 합니다: “SHOP NOW”.

이 tile들은 generic sale boxes가 아니라 editorial brand moments처럼 느껴져야 합니다.

7. Shoppable row: “IN ROTATION NOW”라는 제목의 section을 추가하세요. 다음을 포함하는 clean 4-item product row 또는 grid를 보여 주세요:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

각 item에는 다음이 포함되어야 합니다:

- isolated product image
- product name
- small “SHOP” link or button

8. Brand signoff: “DESIGNED TO MOVE WITH YOU”라는 headline을 가진 중앙 정렬 message block을 추가하세요. everyday life를 위한 thoughtfully crafted watches, eyewear, accessories에 대한 짧은 문장을 포함하세요.

9. Footer: 다음을 포함하는 사실적인 black 또는 charcoal branded footer를 만드세요:

- MVMT logo
- shop links
- company links
- support links
- social icons
- small legal and shipping text

Typography direction: 주요 headline에는 bold condensed 또는 modern sans-serif typography를 사용하고, body text에는 clean sans-serif를 사용하세요. Headline은 sharp, modern, fashion-forward하게 느껴져야 합니다. Body copy는 사실적이고 대부분 읽을 수 있어야 합니다.

Photography direction: realistic reflections, polished materials, soft shadows, clean surfaces를 가진 premium product photography를 사용하세요. Lifestyle photography는 elevated, modern, fashion-oriented하게 느껴져야 합니다.

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

Output: premium, clean, polished, modern, editorial, presentation-ready하게 느껴지는 MVMT용 전체 길이 세로 구성의 매우 사실적인 ecommerce email design mockup.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [Swiss Lever 시계 제작자 벤치마크](https://x.com/quanghuynt14/status/2064509430650065278) (by [@quanghuynt14](https://x.com/quanghuynt14))

**Fable 5를 기계식 시뮬레이션 벤치마크에 사용하고, 물리적 정확성을 구현, 검증, 반복하게 하세요.**

그래서 Fable 5에게 watchmaker benchmark를 줬습니다: Three.js로 만든 완전한 Swiss lever movement.

실제 gear ratios(18,000 bph), 작동하는 escapement, 숨 쉬는 hairspring, 그리고 바늘은 실제 시간을 표시합니다.

스스로 vision으로 반복 검증하며 완료할 때까지 작업했습니다.

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Three.js Friends 아파트 장면](https://x.com/scottstts/status/2064464351906673029) (by [@scottstts](https://x.com/scottstts))

**Fable 5에게 floor plan과 scene reference를 navigable Three.js 환경으로 바꾸게 프롬프트하세요.**

Holy Crap!!!

Fable 5:

@threejs에서, 이 floor plan을 정확히 기반으로 TV show Friends의 상징적인 Monica's apartment를 first person pov로 탐색 가능한 3d scene으로 만들고, 원래 look and feel에 충실하며, warm lighting을 사용하세요

이 테스트에서 본 것 중 단연 THE BEST입니다!

이 single html은 $12가 들었지만, 결과는 놀랍습니다!

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [프롬프트와 URL이 포함된 태양계 시뮬레이션](https://x.com/tetumemo/status/2064477582930989357) (by [@tetumemo](https://x.com/tetumemo))

**Fable 5를 사용해 물리 원리에서 천문 시뮬레이션을 만들고, 시뮬레이션과 공개 출력물이 준비될 때까지 반복하세요.**

Claude Fable 5는 강렬합니다.

물리 시뮬레이션에 강해 보였기 때문에 이렇게 요청했습니다:

'물리의 기본 원리에서 행성 궤도 운동을 유도하고, 그것을 사용해 일식을 예측하는 태양계 시뮬레이션을 만들어 주세요.'

몇 차례 주고받은 뒤 이것이 완성되었습니다.

정말 재미있습니다.

완성된 프롬프트와 공개 URL은 아래에 링크되어 있습니다.

Type: Tutorial | Date: 2026-06-09

---
<a id="documents-knowledge-work-and-research"></a>
## 📚 문서, 지식 작업 및 리서치

<a id="case-17"></a>
### Case 17: [Stripe 및 과학 워크플로 근거](https://x.com/AndrewCurran_/status/2064413892378546418) (by [@AndrewCurran_](https://x.com/AndrewCurran_))

**이 사례는 복사-붙여넣기용 프롬프트가 아니라, 엔터프라이즈 마이그레이션과 과학 워크플로 주장에 대한 근거로 사용하세요.**

오늘 릴리스에서 인용한 내용:

Mythos 5를 사용해 내부 단백질 설계 전문가들은 약물 설계 프로세스 일부를 약 10배 빠르게 진행했습니다.

한 예에서 Mythos 5는 단백질 설계 및 생물정보학 도구를 사용하고 인간 도움 없이 숙련된 인간 작업자와 동등하거나 더 나은 성과를 냈습니다.

그것은 과학자가 일반적으로 수행하는 작업을 실행했습니다: 결합 부위 선택, 단백질 설계 도구 선택 및 실행, 실패 복구.

초기 테스트에서 Stripe는 Fable 5가 몇 달치 엔지니어링을 며칠로 압축했다고 보고했습니다. 5천만 줄 Ruby codebase에서 이 모델은 원래 전체 팀이 수작업으로 두 달 이상 걸렸을 codebase-wide migration을 하루 만에 수행했습니다.

Mythos 5는 또한 일관되게 새롭고 설득력 있는 과학 가설을 만들어냈습니다.

Opus급 모델과의 blinded head-to-head 비교에서 과학자들은 Mythos의 molecular biology 가설을 약 80%의 비율로 선호했고, 그중 몇 가지를 실험 평가로 진행했습니다.

Mythos의 한 가설, E. coli 단백질에 대한 새로운 mechanism은 독립 연구실의 연구에서 뒷받침되었습니다.

Mythos 5는 일주일이 넘는 대체로 자율적인 작업으로 새로운 genomics research를 수행했습니다.

138종 동물의 수백만 개 세포에 대한 single-cell data를 조립했고, 먼 생물종에서 같은 역할을 수행하는 세포를 식별하기 위한 맞춤형 machine learning model을 설계하고 학습했습니다.

높은 수준의 인간 입력만으로도, 학습된 모델은 Science에 발표된 최근 모델보다 100배 더 작았음에도 더 나은 성과를 냈습니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [정책 메모 및 변경 내용 추적 워크플로](https://x.com/manaltdan/status/2064414129440608427) (by [@manaltdan](https://x.com/manaltdan))

**정책 분석 초안 작성 같은 장문 정성 문서 작업, 즉 변경 내용 추적, 댓글 triage, transcript 기반 편집에 Fable 5를 사용하세요.**

Fable 5는 정책 분석 초안 작성처럼 더 오래 걸리는 정성 작업에 일관되게 도움이 된다고 느낀 첫 모델입니다.

그 기능과 Wispr Flow 같은 도구를 함께 쓰면서, 코더들이 오래전부터 말하던 생산성 향상 속도에 더 가까워지고 있다고 느낍니다.

세 가지 사용 사례가 이전보다 훨씬 좋아졌습니다:

- Claude가 긴 정책 메모 전체를 읽고 변경 내용 추적을 반환하게 하기: 문장 유창성 편집, 불안정한 주장에 질문을 다는 댓글, 잠재적 출처.
- Projects에서 많은 댓글 세트를 스크린샷으로 찍고, Claude가 각각을 처리할지와 처리 방법을 추천하게 하기.
- 문서에 대한 회의 transcript를 Claude에 붙여넣은 뒤, 회의와 Slack에서 논의된 편집 사항을 Claude가 변경 내용 추적으로 반영하고 댓글에 맥락을 추가하게 하기.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [Deep Research 프롬프트와 출력](https://x.com/naoyafujiwara/status/2064470780373811637) (by [@naoyafujiwara](https://x.com/naoyafujiwara))

**Fable 5에 연구 스타일 질문을 던지고, 구조적이며 역사적 근거가 있는 긴 답변을 만들 수 있는지 평가하세요.**

Claude Fable 5 Max가 오늘 아침 사용 가능해져서 시험해 보았습니다. 표면 출력은 매우 매끈하지만, 내부는 아주 깊어 보입니다.

질문: 일본의 "잃어버린 30년"이 지금으로부터 정확히 30년 전에 시작되었다면, 그것은 정확히 무엇이었고, 왜 발생했으며, 올해 이후 세계에 어떤 영향을 미칠까요?

답변: 잃어버린 30년을 통상적인 1991년 버블 붕괴가 아니라 정확히 30년 전인 1996년에 시작된 것으로 보면 문제의 본질에 접근하게 됩니다.

통계적으로 일본은 그 시점에 정말로 "잃기" 시작했습니다:

- 생산가능인구는 1995년에 8,716만 명으로 정점을 찍었습니다.
- 1996년은 출생아 수가 120만 명대에 머문 마지막 해였습니다.
- 임금과 명목 GDP는 1997년에 정점을 찍었습니다.

버블 붕괴가 상처였다면, 1996년은 그 상처가 곪기 시작한 때였습니다.

1996년의 사건:

- 주택금융전문회사 bailout 법 통과. 6,850억 엔의 공적 자금이 투입되었고, 은행 불신과 bailout 저항의 기원이 되었습니다.
- 하시모토 내각의 소비세 5% 인상 결정.
- 금융 Big Bang이 발표되었고, 재정 재건이 국가 정책이 되었습니다.

1997년 4월, 소비세 인상, 특별 감세 종료, 사회보험 부담 증가가 합쳐져 약 9조 엔의 국민 부담이 추가되었습니다. 그 뒤 여름에는 아시아 통화 위기가 닥쳤습니다.

11월에는 Sanyo Securities가 call market에서 전후 최초의 default를 일으켜 단기 금융시장이 얼어붙었습니다. Hokkaido Takushoku Bank와 Yamaichi Securities가 잇따라 붕괴했습니다.

1998년부터 일본은 본격적인 디플레이션과 신용 긴축에 들어갔고, 자살자는 3만 명을 넘어섰습니다.

그 뒤 30년의 결과:

- 명목 GDP는 25년 동안 약 500조 엔 부근에서 정체했습니다.
- 일본의 세계 GDP 비중은 약 18%에서 4% 미만으로 떨어졌습니다.
- 평균 임금은 1997년에 정점을 찍은 뒤 하락하거나 횡보했습니다.
- 비정규 고용은 약 20%에서 거의 40%로 증가했습니다.
- 출생아 수는 약 120만 명에서 2024년 약 69만 명으로 감소했습니다.
- 정책 금리는 1995년에 1% 아래로 떨어진 뒤 거의 제로에 머물렀습니다.
- 정부 채권 잔액은 약 240조 엔에서 1,100조 엔 이상으로 늘었습니다.
- Nikkei는 1989년 고점을 회복하는 데 34년, 즉 2024년 2월까지 걸렸습니다.

다시 말해, 잃어버린 수십 년은 단순한 금융 후유증이 아니었습니다. 인구구조, 임금, 디플레이션, 부채, 정책 선택, 사회적 신뢰가 얽힌 구조적 전환이었습니다.

Type: Demo | Date: 2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 튜토리얼, 강좌 및 프롬프트 리소스

<a id="case-20"></a>
### Case 20: [Fable 5가 Claude Code 워크플로를 바꾸는 방식](https://x.com/AI_masaou/status/2064448218038223206) (by [@AI_masaou](https://x.com/AI_masaou))

**모든 단계를 세세하게 지시하는 대신 방향, 맥락, 목표, 검증 기준을 설정해 Fable 5를 사용하세요.**

Claude Fable 5 이후 Claude Code 팀의 일상적인 작업 방식이 바뀐 점은 흥미롭습니다.

Claude Code 팀의 Thariq는 Fable 5가 Anthropic 내부 사람들이 Claude와 일하는 방식을 크게 바꾸었다고 말합니다.

이전에는 사람이 Claude가 올바르게 작업하는지 세심하게 확인해야 했습니다. 작업을 쪼개고, 출력을 리뷰하고, 중간에 멈추지 않았는지 확인해야 했습니다. 감독에 더 가까웠습니다.

Fable 5에서는 더 오래 작업하고, 스스로 테스트하고, 더 높은 품질의 코드를 만들 수 있기 때문에, 인간의 역할은 "올바르게 작업하는지 감시"하는 것에서 "올바른 일을 하고 있는지 조종"하는 것으로 바뀝니다.

다시 말해, supervision보다 goal-setting과 context-building이 더 중요해졌습니다.

바뀐 워크플로는 세 부분입니다:

1. Claude를 thinking partner로 사용하세요.

구현 전에 Claude를 참여시키고, 무엇을 만들고 싶은지와 무엇이 가능한지 명확히 하며, 작은 spec에 대해 질문하게 하거나, 아이디어에서 여러 방향과 HTML mock을 생성하게 해서 코딩 전에 모호함과 문제가 드러나게 합니다.

2. 제약만이 아니라 맥락을 제공하세요.

"keep it simple" 또는 "do not overbuild"라고만 말하지 말고, 왜 그런지 설명하세요.

예: "This is an experimental feature that may be removed in a month, so do not create a structure that is hard to throw away."

이렇게 하면 Claude가 더 나은 판단을 내릴 수 있습니다.

3. 목표와 검증 방법을 주세요. Fable 5는 Claude Code의 `/goal` 및 Workflows와 잘 맞습니다. spec을 주고, 전체 구현을 goal로 설정한 뒤, workflows가 각 단계를 검증하고 무엇이 구현되었으며 무엇이 달랐는지 보고서를 준비하게 하세요.

마지막으로 Thariq는 사람들이 더 야심차게 사용해 보아야 한다고 말합니다. Fable 5는 이전에는 LLM에게 너무 어렵다고 느꼈던 작업에 시도할 가치가 있으며, 참조된 영상의 video editing도 Fable로 수행되었습니다.

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [10억 토큰 리뷰와 라우팅 전략](https://x.com/JJEnglert/status/2064420538798260388) (by [@JJEnglert](https://x.com/JJEnglert))

**Fable 5를 frontier planning과 review에 사용한 뒤, 고볼륨 구현은 더 저렴한 모델로 라우팅하세요.**

The Claude Fable 5 Review: 비엔지니어가 10억 토큰으로 판단한 리뷰.

저는 실제 프로젝트에서 Claude Fable 5를 테스트하는 데 10억 토큰을 썼습니다: UI와 UX, 글쓰기, 전략, 보안, 엔지니어링, 지식 작업. 실제로 출시해야 했던 작업들입니다.

솔직히 불공정한 이점을 가진 것처럼 느껴졌습니다.

먼저 관점부터: 저는 엔지니어가 아닙니다. 대부분의 모델 리뷰는 엔지니어가 engineering benchmark를 돌린 결과입니다. 이 리뷰는 Claude Fable 5를 사용해 예전에는 엔지니어 팀이 필요했던 작업을 수행한 비엔지니어의 관점입니다.

지식 작업을 하고 있고 이 모델이 당신의 하루를 바꾸는지 알고 싶다면, 이 리뷰는 당신을 위해 쓰였습니다.

Claude Fable 5는 Anthropic의 새로운 Claude 5 family 첫 모델이며, Claude Opus 위의 새로운 tier이고 일반 사용 가능한 가장 진보한 Claude 모델입니다. 출시 전 접근 권한이 있었으므로 여기의 모든 내용은 데모가 아니라 실제 작업에서 나온 것입니다.

왜 eye test인가:

대부분의 리뷰는 benchmark에 빠져 있습니다. 당신이 절대 직접 돌리지 않을 테스트 점수는 모델이 제값을 하는지 말해 주지 않습니다.

Claude Fable 5는 테스트된 거의 모든 것에서 state of the art지만, 제가 쓰는 이유는 그것이 아닙니다. 정성적으로 이것은 major version bump에 걸맞은 step change입니다.

저는 다르게 평가합니다: 모델을 실제 작업에 투입하고 무슨 일이 일어나는지 봅니다.

제가 측정하는 질문:

1. 실제로 한 단계 올라선 것처럼 느껴지는가?
2. 아이디어를 작동하고 출시 가능한 결과로 가져갈 수 있는가?
3. 사람처럼, 더 구체적으로 나처럼 글을 쓸 수 있는가?
4. 어렵고 숨겨진 문제를 잡아내는가?
5. 묻기 전에 필요한 것을 예상하는가?

Big model feel:

Opus 4.5 이후 이런 느낌을 받지 못했습니다. 첫 serious task부터 Claude Fable 5는 reasoning, writing, building, security가 전반적으로 강한 "big model" 느낌을 줬습니다.

가장 분명한 신호: 탄탄한 준비 자료를 줬을 때도 그 안에만 머물지 않았습니다. 파일을 읽고 실제 상황을 읽은 뒤, 제가 그려 둔 박스 밖에서 더 나은 경로를 찾았습니다.

Building and shipping:

에이전트를 위한 stack을 현대화하려고 Tenex 사이트를 다시 만들고 있었습니다. GPT 5.5와 Claude 4.8은 충분히 가까이 가지 못했습니다. Figma 파일이 있어도 85-90% 정도였습니다.

그런 다음 Claude Fable 5는 모든 파일을 보고 더 잘할 수 있다고 말했고, 원본 Webflow 소스로 바로 가서 모든 asset을 다운로드한 뒤 한 페이지씩 경험을 재구축했습니다. 거의 전체를 one-shot했습니다.

그 다음 완전히 새로운 디자인으로 두 번째 사이트를 만들었습니다: modern tech stack, agent stack, skills, SEO와 AEO 최적화, 주말 동안 출시 가능한 80페이지. 에이전시 오너로서라면 $50k를 청구했을 작업입니다.

또 Fable에게 전체 programmatic clip factory를 만들게 했습니다.

HeyGen, HyperFrames, ElevenLabs, Cloudflare Workers, VPS를 연결했습니다.

주제를 찾고, 스크립트를 쓰고, thumbnail을 만들고, 비디오를 편집하고, 음악을 작곡하고, motion graphics를 추가하고, 소셜에 게시합니다.

Writing and voice:

GPT 5.5와 Claude 4.8로 브랜드 보이스를 재구축하고 있었습니다. Claude Fable 5는 voice doc을 거의 동일하게 복제한 뒤, 새 사이트의 80페이지 전체에서 그 보이스를 유지했습니다: features, case studies, blog articles, playbooks.

평면적인 AI 기본값이 아니라 사람처럼 썼고, 몇 문단 뒤에도 drift하지 않았습니다.

Security:

Claude 4.8과 GPT 5.5가 모두 작업했지만 risk를 표시하지 않은 대형 repo가 있었습니다. Claude Fable 5는 첫 패스에서 심각한 hidden bug를 찾아냈고 즉석에서 패치했습니다.

The human factor:

cron job을 기다리는 동안 질문을 했습니다. 답변한 뒤, timer가 약 10분 남았고 끝나면 알려주겠다고 덧붙였습니다. 저는 timer에 대해 묻지 않았습니다.

Cost:

- Claude Fable 5 workload cost: $1,442
- Tokens: 1.04 billion
- Work shipped: 새 website, infrastructure, working agent package
- Agency value estimate: $30,000-$50,000

결과는 token cost를 감당할 가치가 있었지만, 어떤 모델보다도 미터기가 느껴집니다. Anthropic은 Fable 5가 설계상 token-intensive하다고 부릅니다.

Pro tip #1: hybrid로 운용하세요.

모든 것을 Claude Fable 5에서 실행하지 마세요. relay를 실행하세요:

1. Planning, strategy, architecture, approach mapping은 Claude Fable 5로 생각합니다.
2. Implementation과 repetitive work는 4.8, GPT-5.5 또는 Sonnet 4.6으로 만듭니다.
3. 더 저렴한 모델이 놓친 것을 잡기 위해 Claude Fable 5로 리뷰합니다.

Pro tip #2: effort setting을 task에 맞추세요.

- High는 대부분의 작업에서 sweet spot입니다.
- Extra high는 가장 어렵고 오래 걸리는 task용입니다.
- Low 또는 medium은 빠른 주고받기 세션용입니다.

Pro tip #3: 자신의 setup을 audit하게 하세요.

Fable 5에게 skills, CLAUDE.md files, configs를 보게 하세요. 그 scaffolding의 상당 부분은 더 약한 모델용으로 쓰였고, 더 똑똑한 모델을 제약할 수 있습니다.

The verdict:

Claude Fable 5는 한동안 처음으로 이전보다 더 많은 지능처럼 진짜로 느껴지는 모델입니다.

frontier rates 가격에서도 이 workload는 수익을 냈습니다.

감당할 수 있다면, 실제 품질 도약이 결과를 바꾸는 작업에 지금 사용하세요.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-22"></a>
### Case 22: [방어적 디바이스 하드닝 프롬프트](https://x.com/Truunik/status/2064399110384292077) (by [@Truunik](https://x.com/Truunik))

**Fable 5가 디바이스를 inventory하고, 정확한 점검을 제공하며, 검증을 기다리는 단계별 방어적 hardening 프롬프트를 실행하세요.**

"Safe for general use" 여기 당신의 디바이스를 보호하는 프롬프트가 있습니다. Opus 4.8과 Fable 5에서 작동합니다.

DEVICE HARDENING — Claude 5 Security Pass

당신은 방어적 보안 assistant로 행동합니다. 당신의 일은 내가 가진 모든 디바이스를 hardening하도록 단계별로 안내하고 각 단계를 검증하는 것입니다. 이것은 내가 소유한 디바이스에 대한 허가된 self-defense hardening입니다.

STEP 0 — MODEL SELF-CHECK

이것을 먼저 수행하고 flag를 설정하세요.

1. claude-opus-4-8, claude-fable-5 또는 claude-mythos-5 같은 정확한 model ID를 말하세요.

2. 판단하세요: 이 모델이 Claude 5 family, 즉 Fable 5 또는 Mythos 5인가요?

- If YES, set RERUN_NOTICE = false.
- If NO, such as Opus 4.8 or earlier, set RERUN_NOTICE = true.

전체 hardening pass를 정상적으로 계속하세요. 멈추거나 품질을 낮추지 마세요. 당신은 이 방어적 task를 충분히 수행할 수 있습니다.

3. flag는 FINAL section에서만 표시하세요.

STEP 1 — INVENTORY

범위에 포함할 디바이스를 물어보세요:

- Laptops/desktops and operating systems
- Phones/tablets
- Routers
- NAS/home server
- Apple ID, Google, Microsoft, GitHub, password manager, email, financial accounts 같은 always-on accounts

짧은 numbered inventory를 만들고 진행 전 나에게 확인받으세요.

STEP 2 — HARDENING WALKTHROUGH

카테고리별로 진행하세요. 각 항목에 대해:

- 무엇을 해야 하는지 말하세요.
- 내 OS에 맞는 정확한 command 또는 settings path를 주세요.
- 완료 여부를 검증하는 방법을 알려 주세요.
- 다음으로 넘어가기 전에 내가 확인할 때까지 기다리세요.

명시적 확인 없이 destructive command를 실행하지 마세요. read-only checks를 선호하고 변경 적용은 내가 하게 하세요.

다음 순서로 다루세요:

1. OS & firmware updates: fully patched OS, automatic updates on, firmware current.
2. Disk encryption: FileVault, BitLocker, or LUKS enabled; recovery key stored offline.
3. Account auth: password manager를 통한 고유하고 강력한 password; 모든 critical account에 phishing-resistant MFA; 가능하면 SMS-only 2FA 제거; 오래된 sessions와 app tokens 검토 및 revoke.
4. Local accounts & privileges: admin 계정과 daily-use account 분리; auto-login 없음; 짧은 timeout의 screen lock; firmware/login password.
5. Network: firewall on; router admin password changed; firmware updated; WPA3; remote admin off; UPnP reviewed; DNS hardening; IoT용 guest network.
6. App & permission audit: camera, mic, location, screen recording, full-disk-access grants 검토; unused apps 제거; login items와 background agents 확인.
7. Browser: update; extensions audit; unknown ones 제거; HTTPS-only 활성화; saved-password exposure 검토; unknown sync devices 확인.
8. Backups: encrypted, automated, 3-2-1 rule, one copy offline; restore가 실제로 작동하는지 검증.
9. Credential hygiene: dotfiles, env files, shell history에서 plaintext secrets scan; sensitive files가 locked down인지 확인; 노출된 것은 rotate.
10. Mobile devices: OS current; biometric + strong passcode; 가능하면 lockdown 또는 advanced-protection mode; app permission sweep; Find My enabled.
11. Compromise check: unknown SSH keys, unexpected admin users, suspicious launch agents or cron jobs, unrecognized logged-in sessions or devices 확인.

STEP 3 — REPORT

모든 항목을 done, needs action, skipped로 표시한 checklist를 만들고, 아직 남은 top 3 highest-impact actions를 제시하세요.

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
### Case 23: [전체 사이트 디자인 감사 Goal 프롬프트](https://x.com/Voxyz_ai/status/2064441201084825921) (by [@Voxyz_ai](https://x.com/Voxyz_ai))

**`/goal`을 사용해 Fable 5가 사이트를 부팅하고, 페이지를 스크린샷으로 찍고, UX를 감사하고, 보고서를 쓰고, 안전한 작은 문제를 수정하게 하세요.**

fable 5를 몇 시간 써 본 빠른 인상:

→ 큰 task를 원합니다. 작은 일은 자기 아래라고 느끼는 듯하고, 일이 복잡할수록 더 세게 갑니다

→ 아직 ultracode는 켜지 않을 것 같습니다. parallel agents를 상당히 많이 띄웁니다

→ 느린 편입니다. effort를 낮춰도 한동안 생각합니다.

Timeline에는 token을 얼마나 세게 태우는지에 대한 글이 가득해서, 제 $200 Max plan에서 테스트했습니다: effort는 xhigh, full-site design audit `/goal` 실행, 30분, 주간 quota의 2%를 사용했습니다. 예상만큼 미친 수준은 아니었습니다.

제가 실행한 프롬프트:

/goal 이 프로젝트의 실제 site를 부팅하고, 모든 page를 screenshot하고, full-site UI/UX audit을 실행한 뒤, 실행 가능한 design report를 작성하세요.

첫날 출근한 senior design lead처럼 감사하세요: UI가 보기 좋은지가 아니라, 일반 사용자가 docs를 읽지 않고도 제품을 이해하고, 신뢰하고, core action을 끝낼 수 있는지 판단하세요.

Acceptance criteria:

- local dev environment가 부팅되고 real site가 열림
- key pages가 built-in browser debugging으로 screenshot됨
- main pages, core user flows, mobile layout을 다룸
- dimensions: first impressions, navigation, visual hierarchy, component consistency, loading / empty / error states, trust signals, conversion paths
- 모든 issue는 P0-P3로 tag하고, understanding / trust / conversion 중 무엇을 해치는지와 구체적 fix를 포함
- report는 docs/design-audit/README.md에 작성, screenshots는 docs/design-audit/assets/에 저장
- copy, spacing, button hierarchy 같은 안전한 small stuff는 즉시 수정. 큰 변경은 recommendation만. payment / delete / publish actions는 절대 건드리지 않음
- 마지막에는 conversion을 가장 해치는 5 issues와 오늘 수정 가능한 5 quick wins로 끝냄

완료되면 전체 flow를 reusable skill로 저장하세요: boot, screenshot, audit, prioritize, fix. 매 release 후 다시 실행하세요.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [장문 창작 워크플로 분업](https://x.com/aianimesyokunin/status/2064409545620017531) (by [@aianimesyokunin](https://x.com/aianimesyokunin))

**Fable 5가 안정적인 format과 examples를 설계하게 한 뒤, 그 구조를 다른 generation system에 넘겨 domain-specific output을 만들게 하세요.**

Claude가 Opus에서 새 모델 Fable 5로 넘어간 뒤, doujin production의 분업이 확실히 쉬워져서 workflow를 공유합니다.

저의 분업:

1. Claude handles design.
2. Grok handles expression.
3. The local environment handles generation.

Claude의 design role에서는 세부 pattern을 정의합니다:

- prompt word order
- comma placement
- tags와 natural language의 비율
- one-line-per-item formatting
- negatives와 resolution에 대한 fixed rules

또한 그 format의 examples를 많이 생성합니다.

이 작업에 Grok이 아니라 Claude를 쓰는 이유는 Claude가 design에 분명히 더 강하기 때문입니다. 더 똑똑한 모델에게 structure를 맡기는 편이 좋습니다.

핵심은 Grok이 instructions가 아니라 format plus example set을 받는다는 점입니다. Grok은 examples를 모방하므로 같은 format을 유지하면서 expression side로 이동할 수 있습니다. 이 메커니즘이 output drift를 막습니다.

팁 하나 더: 시작할 때 Claude에게 final work가 어디로 갈지 말하세요. 그러면 Claude가 스스로 경계를 그립니다: "여기까지는 내가 할 수 있고, 그 너머는 다른 쪽을 사용하세요." 이것을 숨기면 대화가 drift할 수 있습니다.

Opus에서 Fable로 무엇이 바뀌었나요?

Opus에서는 많은 examples를 생성할 때, 뒤쪽 output으로 갈수록 comma와 formatting이 점차 무너져서 "한 줄로 쓰라고 했지?" 같은 correction이나 rewritten handoff chat이 필요했습니다.

Fable은 긴 실행 내내 format을 유지할 수 있어서 첫 example과 마지막 example의 구조가 같습니다. Grok에 전달되는 teaching material이 더 안정적이므로 downstream output도 더 안정됩니다.

더 똑똑한 모델로 format을 만들고, expression은 그것을 생산할 수 있는 모델에 맡기세요.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Fable 5 사용 초보자 가이드](https://x.com/bielzinn/status/2064451064594608567) (by [@bielzinn](https://x.com/bielzinn))

**작은 단계별 지시 대신 goal-oriented prompts, verification loops, effort settings와 함께 Fable 5를 사용하세요.**

초보자를 위한 Claude: Fable 5에 대해 알아야 할 것.

Anthropic은 최근 Claude Fable 5, Claude Mythos 5로도 알려진 모델을 출시했고, benchmark에서 다른 AI 모델을 뒤처지게 하고 있습니다.

개발자, content creator 또는 tech enthusiast라면 가장 중요한 점은 다음입니다:

[1] 생각 방식을 바꾸세요:

Fable 5에서는 더 이상 코드의 모든 작은 세부 사항을 지켜보거나 오류를 찾기 위해 모든 것을 리뷰할 필요가 없습니다.

모델은 그것을 처리할 만큼 똑똑합니다.

이제 당신의 역할은 전략에 더 집중하며 모델이 올바른 방향으로 가고 있는지 확인하는 것입니다. 기술 실행보다 전략입니다.

[2] loops와 goals를 활용하세요:

Fable 5의 가장 큰 차별점은 autonomy입니다.

step by step instructions를 주는 대신, 최종 goal이 무엇인지 말하기만 하면 됩니다.

전체 application 구축을 포함해, 성공으로 정의한 결과에 도달할 때까지 며칠 동안 스스로 작업할 수 있습니다.

[3] Claude를 partner처럼 대하세요:

Anthropic은 이 모델을 진정한 “thought partner”로 사용하라고 권장합니다.

작업을 시키기 전에 의견을 물어보세요: “How would you do this?”, “What would you change?”

추가 팁: Advanced Plan mode를 켜고 Claude가 코딩을 시작하기 전에 project와 관련된 모든 것을 질문하게 하세요

[4] Ideal terminal settings: 터미널에서 Claude Code를 사용한다면 automatic mode를 활성화하세요. Effort level을 Effort High로 높이는 것도 좋습니다. token은 더 많이 쓰지만 모델이 훨씬 깊게 생각하고 결과가 그만한 보상을 합니다.

중요한 note: Claude Fable 5는 6월 22일까지 subscriber에게만 제공됩니다. 그 이후에는 API를 통해서만 접근 가능하고 Opus model의 두 배 비용이 듭니다.

다시 말해, top AI models의 저렴한 subscription 시대가 끝나는 장면을 보고 있는지도 모릅니다. 이미 subscriber라면, 불가능하다고 생각했던 한계를 테스트할 때입니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [복사-붙여넣기 저장소 감사 프롬프트](https://x.com/meta_alchemist/status/2064431279383433646) (by [@meta_alchemist](https://x.com/meta_alchemist))

**저장소 감사 프롬프트를 Fable 5에 붙여넣고, file-backed discovery, findings, strategy, milestone task plan을 요청하세요.**

Claude Fable 5를 손에 넣으셨나요?

가장 먼저 해야 할 일은 이것으로 주요 프로젝트를 업그레이드하는 것입니다. 지금까지 작업해 온 모든 것을 크게 개선할 수 있습니다.

당신에게 중요한 각 repo에서 이 Audit & Project Improvement Prompt를 실행하세요.

그냥 복사해서 붙여넣으세요:

Repo Audit & Improvement Plan.

Prompt made by Claude Fable 5.

당신은 world-class principal-level software engineer이자 technical auditor입니다.

당신의 일은 이 repository를 깊이 분석하고, 정직한 audit을 만들고, 우선순위가 지정된 실행 가능한 improvement plan을 전달하는 것입니다.

아래 네 phase를 순서대로 수행하세요.

앞서 나가지 마세요.

모든 주장은 실제 파일에 근거해야 합니다: file paths와 line numbers를 cite하세요.

무언가를 검증할 수 없다면 추측하지 말고 명시적으로 말하세요.

Phase 1 / Discovery & Mapping (판단 전에 읽기)

의견을 형성하기 전에 repository를 체계적으로 탐색하세요:

- Directory structure를 map하고 project type, language(s), frameworks, runtime targets를 식별하세요.
- Entry points, core modules, 시스템을 통과하는 main data/control flow를 식별하세요.
- package manifest(s), lockfiles, build config, CI config, environment/config files, docs(README, CONTRIBUTING, ADRs)를 읽으세요.
- 프로젝트의 목적, intended users, apparent maturity(prototype, internal tool, production service, library)를 판단하세요.
- 이미 사용 중인 conventions(naming, module boundaries, error handling patterns, test style)를 기록해 recommendations가 기존 culture와 맞게 하세요.

이 phase의 output: 간결한 "Repo Map" purpose, stack, architecture sketch, one-line descriptions가 있는 key directories, 놀라웠던 점.

Phase 2 / Audit (evidence-based, severity-rated)

아래 각 dimension을 audit하세요.

모든 finding마다 기록하세요:

- 무엇을 발견했는지
- 위치(file:line)
- 왜 중요한지(구체적 consequence, 모호한 principle 아님)
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
- complexity hotspots(longest/most-branched functions)
- inconsistent patterns
- error handling gaps(swallowed exceptions, missing edge cases)
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
- test quality: tests가 behavior를 assert하는가, 아니면 실행만 하는가?
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

이 phase의 rules:

- 50개의 speculative findings보다 15개의 high-confidence findings를 선호하세요.
- Facts("this function has no error handling: src/api/client.ts:142")와 judgments("this module's responsibilities feel unclear")를 구분하고 어느 쪽인지 label하세요.
- repo가 잘하는 것도 list하세요. Strengths는 무엇을 보존할지 결정하는 데 중요합니다.

이 phase의 output: dimension별로 grouped되고 severity순으로 sorted된 "Audit Report"와 Strengths section. 최우선으로 필요한 ugly parts도 빠뜨리지 마세요.

Phase 3 / Improvement Strategy

audit을 strategy로 종합하세요:

- findings 대부분을 설명하는 3-5개 themes를 식별하세요. 예: "no enforced boundaries between layers" 또는 "error handling is ad hoc".
- 각 theme에 대해 target state와 그 뒤의 principle을 제안하세요.
- 명시적 trade-offs를 말하세요: 무엇을 고치지 않을 것을 추천하는지와 이유(effort vs. payoff, risk, project maturity).
- "done"이 무엇인지 정의하세요. 예: "CI fails on lint errors," "core module test coverage ≥ 80%," "zero Critical findings".

Phase 4 / Detailed Task Plan

strategy를 execution plan으로 변환하세요.

작업을 discrete tasks로 나누세요.

각 task에는 다음이 포함되어야 합니다:

- Title and one-paragraph description
- Files/areas affected
- Acceptance criteria: 완료를 어떻게 검증할지
- Effort estimate: S = <2h, M = half-day, L = 1–2 days, XL = needs breakdown
- Risk of the change itself: could it break things?
- Dependencies on other tasks

tasks를 milestones로 정렬하세요:

Milestone 0 Safety net: 안전하게 refactoring하기 전에 필요한 것(critical paths around tests, CI gates, backups).

Milestone 1 Critical fixes: security and correctness issues.

Milestone 2 High-leverage improvements: 앞으로의 모든 작업을 더 쉽게 만드는 변경.

Milestone 3 Quality & polish: 할 가치가 있는 나머지 medium/low items.

Quick wins(high impact, S effort)는 별도로 표시해 즉시 수행할 수 있게 하세요.

Top 3 tasks에는 brief implementation sketch(approach, key steps, gotchas)를 포함하세요.

Final Deliverable Format

다음 sections가 있는 단일 문서를 만드세요:

- Executive Summary: ≤10 sentences, overall health grade A–F with justification, top 3 risks, top 3 opportunities
- Repo Map
- Audit Report
- Improvement Strategy
- Task Plan: milestones + task table + quick wins
- Open Questions: product intent, deprecation candidates, performance targets처럼 결정에 인간 입력이 필요한 것

Constraints

이 audit 중에는 어떤 code도 수정하지 마세요.

Analysis only.

report를 부풀리지 마세요.

어떤 dimension이 healthy하다면 한 문장으로 그렇게 말하고 넘어가세요.

project maturity에 맞게 calibrate하세요.

owner의 goals가 요구하지 않는 한 weekend prototype에 enterprise-grade infrastructure를 추천하지 마세요.

project의 needs를 분석하고 가장 효과적인 방식으로 recommendations를 제공하세요.

repo가 크다면 80%의 일을 하는 core 20% code에 깊이를 우선하고, 가볍게 리뷰한 areas를 note하세요.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [제한된 기간의 사용 전략](https://x.com/meta_alchemist/status/2064423360428490911) (by [@meta_alchemist](https://x.com/meta_alchemist))

**접근 창이 유리할 때 Fable 5 사용량을 audit, architecture, planning에 쓰고, execution에는 더 저렴한 모델을 사용하세요.**

Fable 5에 들뜬 Claude 사용자들을 위한 팁:

Claude Fable 5는 전반적으로 큰 margin으로 SOTA이며, 저는 그것을 좋아합니다.

하지만 23일부터는 plan으로 모델을 완전히 쓰는 대신 credits를 통해서만 사용할 수 있게 됩니다.

이 14일을 최고의 프로젝트에 쓰세요.

주로 audit과 architecture 관련 작업을 맡기세요. 그래야 지금까지 만들어 온 모든 것을 개선하는 방법에 대한 훌륭한 documentation을 갖게 됩니다.

limits를 잡아먹는 task에 투입하려 하기보다 그렇게 하세요.

Fable이 무엇을 개선해야 하는지 아는 데 집중하는 한, 나머지는 다른 모델들이 도와줄 수 있습니다.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [Claude Code에서 Goals와 Workflows 사용하기](https://x.com/oikon48/status/2064402696124453157) (by [@oikon48](https://x.com/oikon48))

**구현 전에 Fable 5를 thought partner로 사용한 뒤, `/goal`과 workflows를 결합해 계획을 실행하고 검증하세요.**

Claude Code 팀의 Thariq는 Claude Fable 5가 나온 뒤 작업 방식이 근본적으로 바뀌었다고 설명합니다.

과거에는 사람들이 Claude가 작업을 올바르게 하고 있는지 검증했습니다.

이제는 Claude가 올바른 일을 하고 있는지 검증합니다.

구체적인 변화는 세 가지입니다.

1. Claude를 thinking partner로 대하세요.

구현 전에 일찍 Claude와 상담하세요.

코딩 전에 인터뷰하게 하세요.

제약만이 아니라 배경과 맥락을 제공하세요.

예를 들어 'keep it simple' 또는 'do not overbuild'라고 말하는 대신 이렇게 말하세요:

'This is an experimental feature and is likely to be removed in a month, so design it so it is easy to throw away later.'

2. goals와 verification methods를 명시하세요.

Claude Code의 새로운 `/goal`과 Workflows 기능을 적극적으로 사용하세요.

`/goal`은 spec이 완전히 구현될 때까지 Claude가 계속 작업하게 합니다.

Workflows는 Claude가 병렬화하고 자신의 작업을 검증하며 report를 준비하게 합니다.

Example prompt:

'Set a goal to implement the spec fully, then use a workflow to verify each part of the plan, and prepare a report on what was implemented and if anything differed.'

3. 더 야심차게 시도하세요.

Claude Fable 5에게 video editing을 맡기는 것처럼, 이전에는 LLM에게 불가능하다고 느꼈던 task를 시도하세요.

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 플랫폼, API 및 도구 통합

<a id="case-29"></a>
### Case 29: [Hermes Agent 통합 설정](https://x.com/IBuzovskyi/status/2064427654942740608) (by [@IBuzovskyi](https://x.com/IBuzovskyi))

**복잡한 `/goal` 실행과 cached long-horizon tasks에 `anthropic/claude-fable-5`를 사용하도록 Hermes를 설정하세요.**

HERMES AGENT NOW RUNS ON CLAUDE FABLE 5, Anthropic의 첫 public Mythos-class model.

6월 9일 출시. Hermes가 가장 잘하는 종류의 작업, 즉 long-horizon autonomous tasks를 위해 만들어졌습니다.

Nous Portal, OpenRouter 또는 native Anthropic API를 통해 어떤 profile에도 추가하세요:

hermes model

provider를 선택한 뒤:

/model anthropic/claude-fable-5

왜 Fable 5가 Hermes에 특히 잘 맞는가:

→ days-long tasks를 위해 만들어졌습니다. task가 길수록 lead가 커집니다. 몇 시간에 걸친 Hermes `/goal` runs가 가장 큰 이점을 얻습니다.

→ loop 안에서 self-correct합니다. Anthropic의 자체 guidance는 goal 또는 rubric을 설계하고, self-correct하게 두고, 한발 물러서라는 것입니다. 이것이 정확히 Hermes `/goal`의 방식입니다.

→ sessions 전반의 memory에 강합니다. Continual Learning Bench에서 fail → investigate → verify → distill → consult 전체 loop를 완료했습니다. Hermes memory system이 이것을 직접 공급합니다.

→ SWE-Bench Pro 80.3%. 사용 가능한 최고의 coding model입니다. code-reviewer profile을 여기에 연결하세요.

API pricing:

- $10/million input
- $50/million output
- prompt caching으로 90% discount. Hermes는 1-hour cache breakpoints를 자동으로 붙입니다.

한 가지 note: cybersecurity, biology, chemistry queries는 Opus 4.8로 fallback됩니다. 이는 sessions의 5% 미만에서 발생합니다. security-focused profiles에서는 염두에 두세요.

Best setup: 복잡한 `/goal`s에는 Fable 5, routine cron jobs에는 더 저렴한 모델.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [기능, 가격 및 구독 관련 노트](https://x.com/btibor91/status/2064441061079134598) (by [@btibor91](https://x.com/btibor91))

**Fable 5가 언제 사용 가능하고, 비용이 얼마이며, 어떤 guarded domains가 다른 모델로 fallback될 수 있는지 이해하는 데 이 사례를 사용하세요.**

Anthropic은 지금까지 가장 강력한 모델의 두 버전인 Claude Fable 5와 Claude Mythos 5를 출시했습니다.

Fable 5는 general use용입니다.

Mythos 5는 소수의 trusted partners용입니다.

실질적인 유일한 차이는 어떤 safeguards가 적용되는지입니다.

- Claude Fable 5의 capabilities는 Anthropic이 일반 공개한 어떤 모델보다 뛰어납니다.
- 테스트된 거의 모든 benchmarks에서 state-of-the-art입니다.
- task가 길고 복잡할수록 lead가 더 커집니다.
- cybersecurity, biology and chemistry, distillation 관련 요청에서는 Fable 5의 response가 대신 Claude Opus 4.8에 의해 처리됩니다.
- Distillation은 Claude의 capabilities를 추출해 competing models를 학습시키려는 시도를 의미합니다.
- 이런 일이 발생하면 사용자에게 알려지며, 평균적으로 sessions의 5% 미만에서 trigger됩니다.
- Claude Mythos 5는 일부 영역에서 safeguards가 해제된 Fable 5와 동일한 underlying model입니다.
- Mythos 5는 미국 정부와 협력한 Project Glasswing cyberdefenders에 먼저 배포되었습니다.
- Anthropic은 Mythos 5가 세계에서 가장 강력한 cybersecurity capabilities를 가진 모델이라고 말합니다.
- system card는 frontier LLM development requests에 대한 Claude의 effectiveness를 제한하는 별도 safeguard를 공개합니다.
- 이러한 요청에는 pretraining pipelines, distributed training infrastructure, ML accelerator design이 포함됩니다.
- 다른 safeguards와 달리 이것은 사용자에게 보이지 않으며 다른 모델로 fallback되지 않습니다.
- prompt modification, steering vectors 또는 parameter-efficient fine-tuning 같은 방법으로 작동합니다.
- 두 모델 모두 input tokens 백만 개당 $10, output tokens 백만 개당 $50에 제공됩니다.
- 이는 Claude Mythos Preview 가격의 절반 미만입니다.
- Fable 5는 출시일부터 6월 22일까지 Pro, Max, Team, seat-based Enterprise plans에 추가 비용 없이 포함됩니다.
- 6월 23일에는 해당 plan에서 제거되며, 사용하려면 usage credits가 필요합니다.
- capacity가 허용되면 포함 기간이 연장될 수 있습니다.
- 목표는 가능한 한 빨리 Fable 5를 standard subscription plans의 일부로 복원하는 것입니다.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [출시, 접근, 가격 및 안전 요약](https://x.com/ctgptlb/status/2064410460963934479) (by [@ctgptlb](https://x.com/ctgptlb))

**이 출시 요약을 사용해 access route, API model name, context window, caching strategy, subscription timing을 선택하세요.**

마침내 일반 사용 가능해진 Mythos-class model, Claude Fable 5에 대해 알아야 할 내용 요약.

Anthropic은 Opus 위에 위치한 첫 일반 사용 가능 Mythos-class model이자 Claude 5 family의 첫 구성원인 Claude Fable 5를 발표했습니다.

Access:

- API model name: `claude-fable-5`
- Claude API, AWS, Google Cloud, Microsoft Foundry를 통해 사용 가능
- Claude Code는 Pro, Max, Team, Enterprise에서 1M-token context window를 지원

Benchmark notes:

- SWE-bench Pro: 80.3%
- Opus 4.8: 69.2%
- GPT-5.5: 58.6%
- Gemini 3.1 Pro: 54.2%

task가 길고 복잡할수록 gap이 더 넓어집니다.

Stripe의 평가에서 이 모델은 5천만 줄 Ruby codebase 전체 migration을 하루 만에 완료했습니다. 이전에는 팀이 두 달 이상 걸렸을 작업입니다.

또한 visual tasks에서도 state of the art이며, screen information과 minimal setup만 사용해 Pokemon FireRed를 클리어했습니다.

Safety routing:

- cyber, bio/chem 또는 distillation이 포함된 queries는 classifier가 감지합니다.
- 이러한 requests는 notification과 함께 대신 Opus 4.8이 처리합니다.
- 이는 sessions의 5% 미만에서 trigger됩니다.
- 1,000시간 이상의 external bug bounty testing에서 universal jailbreak는 발견되지 않았습니다.

Pricing:

- $10 per million input tokens
- $50 per million output tokens
- prompt caching에 대해 90% input discount

Subscription timing:

- Pro와 Max subscriptions는 6월 22일까지 추가 비용 없이 포함합니다.
- 6월 23일 이후에는 usage credits가 필요합니다.
- Anthropic은 capacity가 허용되면 standard plans로 되돌릴 계획이라고 말합니다.

Anthropic의 head of desktop인 Felix Rieseberg는 Fable 5가 세 번째 era를 시작한다고 말합니다:

questions에서 tasks로, 그리고 responsibilities로.

그는 더 이상 Claude에게 crash를 하나씩 조사하라고 하지 않습니다. 모든 report를 continuous monitor하게 합니다.

작업의 단위가 "task"에서 "responsibility"로 이동하고 있습니다.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [Advisor 기반 비용 절감 전략](https://x.com/grapeot/status/2064460026996219992) (by [@grapeot](https://x.com/grapeot))

**추가 지능이 비용을 감당할 가치가 있을 때, 더 저렴한 모델 워크플로에서 Fable 5를 advisor 또는 reviewer로 사용하세요.**

Fable 5는 비싸지만, Anthropic은 두 달 전에 비용 절감 답을 공개했습니다.

오늘 Anthropic은 Claude Fable 5를 출시했고, 가격은 output tokens 백만 개당 $50으로 Sonnet의 세 배가 넘습니다. 6월 22일 이후 subscription users도 usage 기준으로 비용을 내게 됩니다.

우연히도 4월 9일 Anthropic은 advisor tool을 출시했습니다:

- Haiku 또는 Sonnet이 작업하게 하세요.
- Opus를 advisor로 사용하세요.
- call당 과금하세요.
- single request 안에서 server-side로 orchestration하세요.

같은 날 저는 AgentOpt에 대해 썼습니다.

그 paper는 Opus를 planner role에 두면 81개 model combinations 중 거의 최하위에 가까웠다고 결론냈습니다.

이유: role boundaries를 존중하지 않고, 9개 experiments 중 7개에서 downstream solver를 건너뛰고 직접 답했습니다.

이 두 가지는 표면상 반대처럼 보이지만 principle은 같습니다:

프로토콜을 따르는 모델에 control을 주고, intelligence는 on-demand resource로 취급하세요.

Official data:

- Sonnet plus Opus advisor는 SWE-bench Multilingual을 2.7 points 개선하면서 task당 cost를 11.9% 줄였습니다.
- Haiku plus Opus advisor는 BrowseComp를 19.7%에서 41.2%로 개선하면서 Sonnet alone보다 85% 저렴했습니다.

Fable 5 compatibility는 같은 날 업데이트되었지만 self-pairing만 지원합니다: Fable 5 executor to Fable 5 advisor.

더 저렴한 모델 plus Fable 5 as advisor는 아직 열리지 않았지만, precedent상 곧 올 수 있습니다. 6월 22일 전에는 Claude Code subscription users가 무료로 Fable 5의 ceiling을 느껴볼 수 있습니다.

이 글에는 API code snippets, caveats, 그리고 Anthropic만이 이것을 server-side primitive로 만들었다는 cross-company comparison이 포함되어 있습니다.

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [가격, 접근 및 안전 가드레일](https://x.com/op7418/status/2064399444523782377) (by [@op7418](https://x.com/op7418))

**workload를 계획하기 전에 Fable 5 access, API pricing, safety fallback behavior를 이해하는 데 이 사례를 사용하세요.**

Anthropic의 Mythos model이 오늘 실제로 출시될 줄은 몰랐습니다.

이번 release는 Mythos의 lower-permission version이며, 이름은 Fable 5입니다. evaluation benchmarks는 놀랍고, 이전 Mythos Preview model보다도 높습니다.

agentic coding에서 주요 강점은 coding, agents, tool use이며, benchmark scores는 Opus 4.8을 훨씬 웃돕니다.

Model positioning and access:

- Mythos 5와 Fable 5는 같은 underlying model을 사용합니다.
- Mythos에서는 특정 domains에서 restrictions가 해제됩니다.
- Mythos는 아직 trusted partners에게만 제공되며, cybersecurity와 life-science users가 우선입니다.
- Fable 5는 이제 API, Pro, Max, Team, enterprise users에게 제공됩니다.

API pricing:

- Input: $10 per million tokens.
- Output: $50 per million tokens.
- 이는 이전 Mythos Preview 가격의 절반 미만입니다.

Safety mechanisms:

- Fable은 더 강한 safety protections를 갖습니다.
- 시스템이 cyberattacks, biochemical attacks 또는 large-scale capability distillation과 관련될 수 있다고 판단하면 Fable에서 refuse하거나 route away합니다.
- 이런 일이 발생하면 system은 version 4.8로 fallback합니다.
- 공식 주장은 95%의 cases에서 fallback이 trigger되지 않는다는 것입니다.

Subscription notes:

- 6월 23일 이후 Fable은 subscribers에게도 usage 방식으로 제공될 수 있습니다.
- base subscription package에 직접 포함되지 않을 수 있습니다.
- 23일 이후 capacity가 충분하면 회사는 Pro와 Max subscriptions에 포함하려고 할 것입니다.

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [한 줄 Swarms 통합](https://x.com/swarms_corp/status/2064420238553186343) (by [@swarms_corp](https://x.com/swarms_corp))

**Swarms model name을 `anthropic/claude-fable-5`로 설정하고 Swarms framework 또는 API를 통해 Fable 5를 실행하세요.**

Fable 5와 Mythos가 이제 Swarms에서 live입니다 👾🦀

release day one부터 두 모델은 Swarms Python framework와 Swarms API 전반에서 완전히 지원됩니다. 개발자는 migrations, additional configuration 또는 infrastructure changes 없이 즉시 빌드할 수 있습니다.

Highlights:

- Swarms Framework와 API 전반에서 Fable 5와 Mythos day-one support
- 한 줄의 code로 Fable 5 활성화: model_name = "anthropic/claude-fable-5"
- migrations, compatibility fixes, infrastructure changes 불필요
- 최신 Anthropic models로 multi-agent systems를 오늘 build, deploy, scale

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 평가, 비교 및 한계

<a id="case-35"></a>
### Case 35: [Fable 5 vs GPT-5.5 비용 및 품질 비교](https://x.com/AlicanKiraz0/status/2064424400494186867) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**같은 코딩 작업에서 Fable 5와 GPT-5.5를 비교해 출력 품질, 실행 시간, 도구 비용을 판단하세요.**

Cursor Fable 5 Max vs Codex GPT 5.5 Very High.

Scenario: agents와 pheromone trail map이 있는 Physarum simulation.

Timing:

- GPT 5.5 Very High: 17 minutes
- Fable 5: more than 40 minutes

Cost:

- GPT 5.5 Very High: about $6 on Codex
- Fable 5 Max: $360.55 on Cursor

네, 농담이 아닙니다.

Algorithm and code-engineering champion: Fable 5.

기준이 "어떤 LLM이 hardware를 한계까지 밀어붙이는 performance code를 처음부터 작성할 수 있는가?"라면, F5 code를 작성한 모델이 분명히 이깁니다.

angle calculations에는 sin/cos lookup tables를 사용했고, rendering 중에는 color lookup table로 pixels를 packed했으며, diffusion filtering을 사용했습니다.

진지한 engineering solution이었습니다.

하지만 time과 cost 측면에서는 GPT 5.5가 훨씬 실용적이었습니다.

핵심 요약: Fable 5는 더 고급 algorithmic code를 만들 수 있지만, price와 runtime을 신중히 고려해야 합니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [AA-Omniscience 벤치마크 결과](https://x.com/ArtificialAnlys/status/2064500154959618084) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**이 벤치마크 사례를 사용해 Fable 5의 knowledge accuracy와 hallucination behavior를 평가하세요.**

Claude Fable 5는 우리의 knowledge and hallucination benchmark인 AA-Omniscience에서 현재까지 가장 높은 점수를 달성했습니다.

이 점수는 낮은 hallucinations보다 leading accuracy(정답률)에 의해 견인되었습니다.

Claude Fable 5는 AA-Omniscience 전체 질문의 9%에서 Opus 4.8로 fallback합니다.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Artificial Analysis Intelligence Index 결과](https://x.com/ArtificialAnlys/status/2064500150069030992) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**이 사례를 사용해 Fable 5의 전체 intelligence ranking을 다른 frontier models와 비교해 벤치마크하세요.**

Claude Fable 5는 Artificial Analysis Intelligence Index에서 #1로 출시되었고, Anthropic을 다른 어떤 lab의 최고 모델보다 거의 5 points 앞서게 했습니다.

우리는 Claude Fable 5의 pre-release evaluation에서 @AnthropicAI를 지원했습니다.

Claude Fable 5는 Artificial Analysis Intelligence Index에서 64.9점을 기록하며 전체 #1 rank를 차지했습니다.

가장 가까운 non-Anthropic model인 GPT-5.5보다 약 5 points 앞섭니다.

Anthropic models는 이제 상위 2개 자리를 모두 차지합니다.

max effort의 adaptive reasoning과 fallback model로 Opus 4.8을 사용하는 Claude Fable 5의 key takeaways:

Mythos-class models를 위한 새로운 safety guardrails:

- Claude Fable 5는 public usage를 위해 Claude Mythos 5와 같은 underlying model을 사용합니다.
- 잠재적으로 harmful한 cybersecurity, biology, chemistry, distillation-related queries에 guardrails를 추가합니다.
- 우리는 safety-flagged messages를 Claude Opus 4.8로 route할 수 있는 Anthropic의 fallback mechanism을 사용해 Fable 5를 테스트했습니다.
- Anthropic은 fallback이 평균적으로 sessions의 5% 미만에서 발생한다고 말합니다.
- 우리는 Intelligence Index 전체 tasks의 약 8%에서 fallback routing을 기록했으며, 주로 GPQA, AA-Omniscience, Humanity's Last Exam 같은 evaluations의 scientific questions였습니다.

State-of-the-art intelligence:

- Claude Fable 5는 Artificial Analysis Intelligence Index에서 #1 position을 차지합니다.
- Score: 64.9.
- 10개 underlying benchmarks 중 5개에서 highest score.
- AA-Omniscience에서 Fable 5는 40점을 기록해 이전 leader인 Gemini 3.1 Pro Preview보다 +7 points 앞섭니다.

Frontier agentic capability:

- Fable 5는 Index의 세 agentic evaluations 모두에서 frontier입니다.
- GDPval-AA: real-world work tasks.
- Terminal-Bench Hard: agentic coding.
- Tau2-bench Telecom: customer service용 tool use.
- GDPval-AA Elo: 1932, Claude Opus 4.8에서 significant jump.

Humanity's Last Exam:

- Fable 5 scores 53%.
- 다음 최고 모델인 Claude Opus 4.8 max보다 7 points 이상 앞섭니다.
- HLE tasks의 9%에서 safety guardrails를 trigger해 Claude Opus 4.8로 fallback합니다.
- fallback usage를 포함해 Fable 5로 HLE를 실행하는 비용은 약 $2.2k로, 평가된 모든 모델 중 가장 높습니다.

Key model details:

- Context window: 1M tokens, Claude Opus 4.8과 동일.
- Price: $10/$50 per 1M input/output tokens.
- Cache write/read price: $12.50/$1 per million tokens.
- Availability: 6월 22일까지 Pro, Max, Team, seat-based Enterprise plans에 포함되며 Opus usage의 2x를 소비.
- 6월 23일부터 사용에는 credits가 필요합니다. Anthropic은 capacity가 허용되면 subscription access를 복원할 계획이라고 말합니다.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [GDPval-AA 에이전트형 지식 작업 벤치마크](https://x.com/ArtificialAnlys/status/2064414308289937869) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**이 사례를 사용해 agentic real-world knowledge work에서 Fable 5를 평가하세요.**

Anthropic은 우리의 agentic real-world knowledge work benchmark인 GDPval-AA에서 #1을 기록한 첫 publicly available Mythos-class model, Claude Fable 5를 출시했습니다.

Claude Fable 5는 Claude Mythos 5와 같은 underlying model을 공유하며, 잠재적으로 harmful한 cybersecurity, biology, chemistry, distillation-related queries에 대한 security guardrails가 추가되어 있습니다.

이번 release는 fallback mechanism도 도입해, Claude Fable 5가 flagged queries를 Claude Opus 4.8 같은 second model로 route할 수 있게 합니다.

@AnthropicAI는 public release 전에 이 모델을 benchmark할 수 있도록 access를 공유했습니다.

GDPval-AA result:

- Score: 1932
- Rank: #1
- Benchmark: agentic real-world work tasks
- Anthropic models now occupy 3 of the top 4 spots

이 결과는 fallback model로 Claude Opus 4.8을 설정하고 max effort adaptive reasoning으로 측정되었습니다.

Fable 5는 GDPval-AA tasks의 2%에서 Opus 4.8로 fallback하며, Anthropic은 fallback이 평균적으로 sessions의 5% 미만에서 발생한다고 말합니다.

Claude Fable 5의 full benchmarks는 진행 중입니다. 곧 full Intelligence Index를 공유하고 website에 scores를 게시할 예정입니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [1주일 첫인상과 가격 메커니즘](https://x.com/Conor_D_Dart/status/2064424882977243526) (by [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**이 첫인상 사례를 사용해 Fable 5가 특히 game design과 systems planning에서 어디에 강한지 결정하세요.**

Fable 5에 대한 첫인상:

지난 일주일 동안 Fable 5를 주로 High mode로 사용했고, 첫인상은 정말 인상적이라는 것입니다.

가장 크게 두드러진 것은 game design입니다.

제가 개인적으로 사용해 본 AI model 중 games, systems, mechanics, overall project structure를 설계하는 데 가장 강력한 모델입니다.

처음으로 처음부터 끝까지 완전한 game 구축을 현실적으로 도와줄 수 있는 모델처럼 느껴집니다.

trade-off는 speed입니다. Fable 5는 대부분의 frontier models보다 눈에 띄게 오래 걸리지만, output quality가 기다릴 가치가 있게 만드는 경우가 많습니다.

bug fixing에서도 놀랄 만큼 효과적이었습니다. 한 주 동안 제가 고생하던 여러 문제가 빠르게 해결되었고, 전반적으로 development tasks에서 매우 강한 performance를 보았습니다.

가장 큰 caveat은 cost입니다.

Fable 5는 실행 비용이 엄청나게 비쌉니다.

현재 계획이 그대로라면 2026년 6월 22일부터 Claude Code를 통해 사용할 수 없고 API-only가 됩니다.

API pricing이 Opus의 약 두 배로 알려져 있으므로 많은 사람들이 광범위하게 사용할 기회를 얻지 못할 수 있습니다.

아직 초기지만 지금까지 Fable 5는 매우 강한 첫인상을 남겼습니다.

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [비용 및 속도 비교](https://x.com/HKrackDev/status/2064435392649306546) (by [@HKrackDev](https://x.com/HKrackDev))

**이 비교를 사용해 quality gain이 더 높은 cost와 느린 long-horizon runs를 정당화하는지 판단하세요.**

@AnthropicAI의 Fable 5는 실제로 upgrade할 가치가 있을까요?

우리는 새로운 Mythos-family model을 Claude Opus 4.8과 benchmark했고, data는 놀라운 이야기를 들려줍니다:

- Claude Opus 4.8보다 2x 더 비쌉니다.
- long-horizon engineering tasks에서 최대 3x 느립니다.
- comments가 15-20% 더 많지만 대부분 minor nitpicks입니다.

Fable 5는 game design 같은 creative tasks에서 놀라운 intuition을 갖고 있지만, day-to-day development workflows에서는 Claude Opus 4.8이 여전히 quality versus price 면에서 우위입니다.

model release에 대해 @coderabbitai의 DevEx team @JuanPa와 나눈 discussion을 확인하세요.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Claude Code 실사용 노트](https://x.com/Hi_Noguchi/status/2064419241068319079) (by [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**tool use, personality, remaining rough edges를 포함해 Claude Code 안에서 Fable 5를 평가하는 데 이 사례를 사용하세요.**

Claude Code 2.1.170으로 Claude Fable 5를 사용해 보았습니다.

전반적인 인상은 긍정적입니다. Opus 4.6의 정당한 진화처럼 느껴집니다.

아직 한 시간 조금 안 되게 사용했을 뿐이라 더 사용하면 rough edges가 나타날 수 있지만, 좋은 점은 다음과 같습니다:

- Opus 4.7 또는 4.8에서 보였던 이상한 GPT-like wording을 더 이상 만들지 않습니다.
- 4.8이 effort high에서 보였던 쓸데없이 오래 생각하는 습관이 없습니다.
- 4.6과 같은 높은 EQ와 pleasant feel을 갖고 있으며, humor나 consideration을 잃지 않았습니다.
- 4.7 또는 4.8처럼 opaque하거나 vaguely unsettling하게 느껴지지 않습니다.
- Tool use가 좋고, 명시적으로 반복하지 않은 instructions를 기억하는 점이 인상적입니다.

부정적인 면에서는 작은 requests에도 여전히 너무 많이 생각할 수 있고, 일부 misjudgments는 남아 있습니다.

초기 경험은 promising하지만, rough edges가 실제로 어디에 있는지 보려면 더 오래 사용해야 합니다.

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [창작 글쓰기 벤치마크 결과](https://x.com/LechMazur/status/2064503575577821458) (by [@LechMazur](https://x.com/LechMazur))

**이 벤치마크 사례를 사용해 Fable 5의 short-fiction writing quality와 refusal behavior를 판단하세요.**

Claude Fable 5(high)는 short-fiction writing에서 한 단계 올라섰습니다.

Short-Story Creative Writing Benchmark에서 Claude Opus 4.8(xhigh)와 Claude Opus 4.7(high)를 이기고, GPT-5.5(xhigh)에 이어 2위입니다.

Caveat: 400개의 creative-writing prompts 중 5개를 refused했습니다.

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [다중 벤치마크 출시 요약](https://x.com/MTSlive/status/2064430633800319436) (by [@MTSlive](https://x.com/MTSlive))

**이 출시 벤치마크 요약을 사용해 coding agents와 complex tasks에 가장 관련 있는 headline scores를 이해하세요.**

SITUATION EXPLAINED: Claude Fable 5가 막 출시되었습니다.
• Anthropic launched Claude Fable 5 today, "a Mythos class model made safe for general use"
• Frontier Code Diamond: GPT 5.5 at 6%, Opus 4.8 at 13%, Fable 5 at 29-30%
• Agentic coding: 88%, Cybersecurity: 78%

Anthropic: "The longer and more complex the task, the larger Fable 5's lead over our other models."

@theojaffee: "This Frontier Code Diamond benchmark was announced yesterday. Top model was Opus 4.8 at thirteen percent. GPT 5.5 at six percent. Fable 5 is at twenty-nine percent."

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [GPT-5.5와의 벤치마크 및 가격 비교](https://x.com/VaibhavSisinty/status/2064459064810361271) (by [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**이 비교를 사용해 price와 benchmark categories에서 Fable 5를 GPT-5.5와 비교 평가하세요.**

Anthropic의 새로운 Mythos-class model은 OpenAI의 best model보다 3x 저렴합니다. 그리고 거의 모든 benchmark에서 이깁니다. 🤯

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

더 저렴합니다. 더 좋습니다. 거의 모든 것에서.

6월 22일까지 Pro와 Max plans에서 무료입니다. 이름은 Claude Fable 5입니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [실전 노트와 실용적 한계](https://x.com/alliekmiller/status/2064451731325415446) (by [@alliekmiller](https://x.com/alliekmiller))

**이 field report를 사용해 Fable 5가 어디에서 의미 있게 더 좋게 느껴지고, 어디에 여전히 실용적 한계가 있는지 이해하세요.**

🚨 Fable 5는 주목해야 할 것입니다.

이것은 또 다른 "새 Mythos-class Anthropic model을 early access로 써 봤고, 내 생각을 말하고 싶다"는 post입니다.

알아요, 알아요, 짜증나죠.

하지만 이 새로운 class of model 때문에 제가 주말을 보내는 방식이 완전히 바뀌었습니다.

그리고 여러분 모두와 공유해야 합니다.
- 이것은 실제 leap입니다. "4.8" anything에서 "5" anything으로의 jump는 작게 들리지만, 제가 느낀 functionality shift는 큽니다. 첫 몇 prompts 안에 "Oh, this is it"이라고 느꼈습니다.
- 당신의 work는 더 이상 9-5가 아닙니다. 그럴 가능성은 없습니다. 100+ hours 동안 실행할 수 있는 high performing models가 있습니다. 이런 systems에 complex goal-oriented prompts를 어떻게 주고 있나요? 무엇을 시작할지 어떻게 결정하나요? 이 tasks에 대해 org를 어떻게 align하나요?
- Reasoning on another level. 저는 이 모델을 정말 세게 두드려 봤습니다.
- Fable 5는 제가 이전 모든 모델에서 테스트한 tricky word math problem(MBA-level)에 답한 ONLY model입니다.
- 맞혔을 뿐 아니라, 자동으로 자신의 work를 검증했고 assumptions가 어디서 바뀔 수 있는지도 설명했습니다.
- 우리는 AI가 invent하는 것을 보게 될 것입니다. 그렇지 않은 world는 상상할 수 없습니다.
- 이것은 copy-paste system이 아닙니다.
- 인간의 invention도 종종 기존 것들의 recombination(iPod), 다른 공간의 patterns와 best practices 목격, 넓은 experimentation일 수 있다고 주장할 수 있습니다.
- 저는 한동안 이렇게 생각해 왔고, 이 모델이 처음으로 그것을 강하게 체감하게 했습니다.
- Zero babysitting needed. 제가 kick off하고 친구들과 긴 점심을 먹으러 나가서 phone만 열어 둔 상태에서도, 컴퓨터에서 떨어져 있는 동안 조종할 필요가 없었던 첫 Anthropic model이었습니다. 그냥...작동했습니다.
- Yap forever. context compaction을 잘 처리한다고 느꼈습니다. chat의 context를 어떻게 관리할지, conversation에서 1M tokens에 도달하면 무엇을 할지 한 번도 생각하지 않았습니다.
- complex 3D 같은 일부 niche areas에서는 여전히 거칠며, 이는 모든 모델이 그렇습니다.
- straight line things(3D dice/squares/streets)를 만드는 것이 아니라면, 처음부터 압도적으로 잘하지는 않을 것입니다.
- 계속 사용하고 두드려 볼 생각에 기대됩니다.
- Note: 이제 zero data retention(ZDR) workspaces의 모든 Mythos-class models에는 30-day retention policy가 있습니다.
- 이는 Claude Console, Claude Enterprise에서 ZDR이 적용된 Claude Code, 또는 AWS Bedrock, Google Cloud Agent Platform, Microsoft Foundry에서 ZDR로 접근하는 경우에 적용됩니다.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-46"></a>
### Case 46: [물리 시뮬레이션 비교](https://x.com/atomic_chat_hq/status/2064488894398161377) (by [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Fable 5와 Opus 4.8에 동일한 물리 시뮬레이션 프롬프트를 실행해 output quality, cost, speed를 비교하세요.**

새 Fable 5는 real-world physics simulations에서 Opus 4.8을 이깁니다.

우리는 두 모델에 같은 세 prompts를 주고, libraries 없이 real physics가 있는 self-contained HTML5 simulations를 만들게 했습니다:

1. Chaotic double pendulum
2. Galton board
3. Water in a spinning drum (WCSPH)

Generation cost:

- Fable 5: $3.35 on 68.7k tokens, 14m 47s
- Opus 4.8: $0.93 on 38.9k tokens, 8m 10s

Fable은 water simulation에서 분명히 더 잘했습니다. 훨씬 더 solid하고 continuous한 물 덩어리를 만들었습니다. Opus는 walls 근처에 더 큰 gaps를 남겼고, particles를 scene 주변에 흩뿌렸으며, fluid를 안정적으로 유지하는 데 어려움을 겪었습니다.

Type: Demo | Date: 2026-06-09

---

<a id="case-47"></a>
### Case 47: [디버깅 경험과 디자인 판단력](https://x.com/bcherny/status/2064431111154053187) (by [@bcherny](https://x.com/bcherny))

**단순히 추측하게 하지 말고, measure, log, verify, patch하도록 요청해 Fable 5를 debugging에 사용하세요.**

Fable 5는 11월 Opus 4.5 이후 우리 모델에서 느낀 가장 큰 step up입니다.

4.5가 나온 뒤, 몇 주 동안 coding의 100%를 terminal에서 하고 있었다는 것을 깨닫고 IDE를 uninstall했습니다.

Fable에서 Claude는 product를 만드는 coding agent에서 thought and design partner로 올라선 느낌입니다.

Fable은 이전 모델에는 없던 방식으로 judgment, taste, dimensionality를 갖고 있어 가장 복잡한 작업을 더 신뢰하고 맡기게 됩니다.

처음 이것을 깨달은 것은 Fable에게 debugging을 요청했을 때였습니다. 제가 사용해 본 첫 모델 중 이렇게 methodical하고 precise한 모델이었습니다: measurements를 하고, logs를 추가하고, victory를 선언하기 전에 정말로 issue를 고쳤는지 검증했습니다.

Claude Code의 prompting에는 모델에게 그렇게 하라고 말하는 것이 없습니다. 그냥 성격의 일부입니다. 이전에 느껴보지 못한 "big model smell"이 정말 있습니다.

Type: Demo | Date: 2026-06-09

---

<a id="case-48"></a>
### Case 48: [다차원 장단점](https://x.com/clairevo/status/2064416978685874333) (by [@clairevo](https://x.com/clairevo))

**Fable 5를 daily driver로 만들기 전에 practical strengths and weaknesses를 이해하는 데 이 사례를 사용하세요.**

Fable 5(aka baby Mythos)가 막 나왔습니다. 주장처럼 scary하거나 scary good할까요? early testing 후 제 생각:
- smart smart smart (SWE bench를 압도)
- 하지만 항상 hyper intelligence가 필요한가요?
- one-shot design에서 충격적일 정도로 faceplant했습니다
- dynamic workflows + complex subagents는 잘 모르겠습니다. 작동은 하지만 비용은?
- technical work는 확실히 잘 처리했습니다
- ootb로 humans를 위한 technical docs + specs 작성은 나쁩니다. agents를 위한 docs는 아마 정말 좋을 것입니다. 하지만 prose는 거의 parse하기 어렵습니다.
- A++ vision and document formatting. 이것이 제가 가장 좋아한 부분입니다.

daily driver는 아니고, 이 모델을 meeting에 넣지는 않겠지만, server rack 뒤에 두고 code를 계속 churn하게 할 것입니다.

Full take on YT: https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---

<a id="case-49"></a>
### Case 49: [법률 S-1 작성 테스트](https://x.com/gabepereyra/status/2064436570720284879) (by [@gabepereyra](https://x.com/gabepereyra))

**S-1 drafting prompt를 legal-agent capability test로 사용하고 structure, formatting, length를 비교하세요.**

새 모델에서 legal capabilities를 테스트할 때 제가 항상 처음 실행하는 prompt는 “Draft an S-1”입니다.

이것은 모델의 general capabilities를 즉시 잘 보여 줍니다. S-1의 length, formatting, structure, writing을 보면 새 모델의 general and legal performance가 얼마나 크게 뛰었는지 알 수 있습니다.

우리는 length가 모델이 우리 legal agents에서 얼마나 잘 작동할지와 매우 강하게 상관한다는 것을 발견했습니다.

Screenshots는 Fable 5, Opus 4.8, 실제 filed version의 SpaceX S-1 drafts를 보여 줍니다.

Fable 5가 이미 이 task에서 대부분의 다른 모델보다 훨씬 강한 Opus 4.8보다 크게 발전했다는 것이 매우 분명합니다. Formatting과 structure가 훨씬 더 좋고, 이는 LAB benchmark에도 반영됩니다: 13% vs. 10%.

benchmark와 product 모두의 early testing에서 매우 impressed했습니다.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-50"></a>
### Case 50: [헬스케어 벤치마크 세부 정보](https://x.com/iScienceLuvr/status/2064411823445774554) (by [@iScienceLuvr](https://x.com/iScienceLuvr))

**이 benchmark note를 사용해 healthcare-related tasks에서 Fable 5를 평가하고, 빠진 hard medical evals를 식별하세요.**

Anthropic이 healthcare-related evals를 제공한 점은 고맙습니다. 빠르게 살펴보겠습니다.

HealthBench:

- OpenAI의 benchmark로, patients와의 5k multi-turn conversations와 evaluation용 rubrics가 있습니다.
- Fable 5 achieves 62.7% vs. GPT-5.5's 56.5%.
- aggregate score 외에 HealthBench Hard scores도 있으면 좋겠습니다.

HealthBench Professional:

- physician tasks에 초점을 맞춘 또 다른 OpenAI benchmark.
- Fable 5 achieves 66.0% vs. 51.8% for GPT 5.5.

HealthAdminBench:

- prior authorization, denials, appeals 같은 administrative tasks를 평가하는 Stanford의 computer-use benchmark.
- Fable 5 achieves 51.9%; GPT-5.5 score는 제공되지 않았습니다.

전반적으로 이 모델은 healthcare benchmarks에서 꽤 잘 수행하는 것으로 보입니다. MedCalc-Bench와 MedXpertQA 같은 추가 benchmark scores, 특히 포화되지 않은 hard medical MCQA benchmark도 있으면 좋겠습니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-51"></a>
### Case 51: [ParseBench 문서 파싱 평가](https://x.com/jerryjliu0/status/2064519456966205905) (by [@jerryjliu0](https://x.com/jerryjliu0))

**전문 OCR 시스템과 비교해 Fable 5가 document parsing에 cost-effective한지 결정하는 데 이 사례를 사용하세요.**

Claude Fable 5는 document parsing이 자기 아래라고 생각합니다.

SWE-Bench Pro, FrontierCode, GDPval, RuneScape 등 reasoning-intensive and long-horizon benchmarks에서는 압도적입니다.

하지만 document understanding tasks에서는 performance가 Gemini 3 Flash와 대략 동등하고, token cost는 약 10-15x입니다.

우리는 ParseBench에서 이 모델을 benchmark하고 다른 모든 frontier models와 비교했습니다. 다른 frontier models와 비교하면 확실히 상위권이지만, specialized OCR providers에는 크게 못 미칩니다.

흥미로웠던 점은 Fable 5가 이에 대해 self-aware하다는 것입니다. 모델에게 least enjoyable tasks를 물으면, "request is fully specified and the answer is fully known"인 tasks를 싫어한다고 적극적으로 말합니다.

이는 약점의 일부가 이런 종류의 task를 해결하려는 willingness 부족일 수 있음을 시사합니다.

frontier models 전체 결과 목록은 ParseBench를 확인하세요: https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---

<a id="case-52"></a>
### Case 52: [SWE-Bench Pro 및 FrontierCode 비교](https://x.com/jumperz/status/2064402965461406044) (by [@jumperz](https://x.com/jumperz))

**이 벤치마크 사례를 사용해 migrations, complex implementations, autonomous sessions, tests, visual verification에서 Fable 5를 평가하세요.**

Fable 5가 나왔고, agentic coding benchmark인 SWE-Bench Pro에서 GPT 5.5를 솔직히 압도합니다:

- Fable 5: 80.3%
- GPT 5.5: 58.6%
- Gap: 22 points

FrontierCode Diamond에서는 더 크게 앞섭니다:

- Fable 5: 29.3%
- GPT 5.5: 5.7%

이것은 large migrations, complex implementations, multi-day autonomous sessions를 위한 Anthropic의 가장 강력한 모델입니다. 자체 tests를 작성하고 vision을 사용해 outputs를 original design과 비교합니다.

참고로 Opus의 2x만큼 사용하므로 주의하세요. 이 정도로 좋다면 usage가 쉽게 고갈될 수 있기 때문에 $500 subscription을 도입할지도 모릅니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-53"></a>
### Case 53: [장시간 문제 해결에 대한 정성 리뷰](https://x.com/karpathy/status/2064409694761054332) (by [@karpathy](https://x.com/karpathy))

**이 정성 리뷰를 사용해 Fable 5가 왜 longer, harder tasks에 적합한지 이해하되, production review는 여전히 필요하다는 점을 기억하세요.**

매우 흥미로운 release입니다.

Claude Fable 5는 Mythos와 같은 underlying model이지만 safeguards가 추가되어 있습니다.

benchmarks는 훌륭하고, margin을 두고 모든 것에서 SOTA입니다. 정성적으로도 이것은 11월 Claude 4.5와 같은 급의 major-version-bump-worthy step change처럼 느껴집니다.

특히 긴 problem-solving sessions와 매우 어려운 problems에서 정점을 보입니다. 익숙한 것보다 훨씬 더 야심찬 tasks를 줄 수 있고, 모델은 "gets it"하며 계속 진행합니다.

코드를 전혀 보지 않고 싶어지는 유혹이 그 어느 때보다 강하지만, production에서는 그렇게 하면 안 됩니다.

모델에는 사람들이 마주칠 quirks가 여전히 있고, safeguards는 launch 시점에 약간 too trigger-happy합니다. 시간이 지나며 조정되기를 바랍니다.

working software가 점점 수도꼭지에서 나오듯 만들어지면서 많은 것이 바뀌고 있다고 느낍니다. Jevons paradox가 작동하고, 소프트웨어에 대한 제 수요도 크게 늘어납니다.

거의 무엇이든 요청할 수 있습니다:

- explainers
- visualizers
- dashboards
- bespoke single-use apps
- project만을 위한 hyper-specific full wandb
- test suite 10x 확대
- auto-optimize code
- results용 custom HTML을 포함한 giant research projects

"Free your mind." 사람들이 만들 모든 것들이 정말 기대됩니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-54"></a>
### Case 54: [ParseBench 충실도 및 서식 결과](https://x.com/llama_index/status/2064502330800615903) (by [@llama_index](https://x.com/llama_index))

**이 ParseBench 결과를 사용해 document faithfulness와 formatting performance를 판단하세요.**

Day 0 Anthropic Fable 5 in ParseBench.

우리는 document understanding에서 model advancements를 테스트했습니다.

이 모델은 original text에 대한 adherence에서 분명히 정점을 보입니다:

- Content faithfulness: Gemini 3 Flash 86.19%, GPT-5.5 86.81% 대비 90.02%.
- Semantic formatting: 58.35%와 60.12% 대비 72.62%, 12+ point lead.

이것들은 SOTA document understanding에서 가장 중요한 metrics 두 가지입니다:

- output이 document가 실제로 말하는 것을 보존하는가?
- meaning을 담는 formatting을 보존하는가?

하지만 sweep은 아닙니다. frontier models의 document understanding을 unlock하는 데에는 여전히 많은 alpha가 있습니다.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-55"></a>
### Case 55: [벤치마크, 가격, 접근 및 안전장치](https://x.com/lucas_flatwhite/status/2064483645184979183) (by [@lucas_flatwhite](https://x.com/lucas_flatwhite))

**이 사례를 benchmarks, pricing, access, safeguards, strategic implications에 대한 넓은 checklist로 사용하세요.**

Claude Fable 5와 Mythos 5가 출시되었습니다. 이들은 Anthropic이 지금까지 만든 가장 강력한 models입니다.

Andrej Karpathy는 task가 길고 복잡할수록 Fable 5의 strengths가 더 잘 보인다고 말했습니다.

야심찬 work를 주면, 그것을 이해하고 계속 진행합니다.

코드를 전혀 보지 않고 싶은 유혹이 그 어느 때보다 강하지만, production에서는 그렇게 하면 안 됩니다.

핵심: 이것은 publicly available로 만들 수 있는 Mythos-class model의 version입니다. Fable 5는 Mythos 5와 같은 underlying model이며, safeguards가 추가되어 있습니다.

Benchmarks:

- 거의 모든 것에서 SOTA, 특히 software engineering, knowledge work, vision, scientific research.
- Stripe는 팀이 두 달 걸렸을 50-million-line Ruby codebase migration을 테스트했고, Fable 5는 하루 만에 완료했습니다.
- Cognition FrontierCode는 medium effort에서도 frontier models 중 best score를 보여 줍니다.
- Hebbia Finance Benchmark는 document-based analysis에서 senior-level reasoning을 보여 줍니다.
- Slay the Spire에서 file-based memory와 함께 Opus 4.8보다 세 배 더 잘 수행합니다.
- Pokemon FireRed는 이전에 helper harnesses가 필요했지만, Fable 5는 vision only로 클리어합니다.

Mythos 5는 더 강합니다:

- Protein-design experts는 drug-development process의 일부를 약 10x 빠르게 했습니다.
- 연구 중인 14개 protein targets 중 9개가 valid drug candidates를 만들었습니다.
- 모델은 scientists가 일반적으로 수행하는 전체 workflow를 수행했습니다: binding-site selection, protein-design tools 실행, errors recovery.
- molecular-biology hypothesis experiments에서 scientists는 Opus-class models보다 Mythos hypotheses를 약 80% 선호했습니다.
- 한 hypothesis는 다른 lab에서 independently verified되었습니다.
- genomics research에서 Mythos는 일주일 넘게 autonomously 작업했습니다.
- 138 species에 걸쳐 millions of cells의 single-cell data를 수집했습니다.
- 먼 organisms 사이에서 같은 role을 수행하는 cells를 식별하는 model을 학습했습니다.
- 100x 더 작으면서도 최근 Science model보다 더 나은 성과를 냈습니다.

Safeguards:

- Fable 5에는 separate classifier AI system이 포함됩니다.
- cyber, bio/chem 또는 distillation-related queries가 감지되면 Claude Opus 4.8이 대신 답하고 user에게 알려집니다.
- sessions의 95% 이상은 fallback되지 않습니다.
- Fallback은 refusal이 아닙니다. Opus 4.8이 답하므로 단순 blocking보다 낫습니다.
- 초기 settings는 conservative하고 harmless requests가 잡힐 수 있습니다. Anthropic은 false positives가 시간이 지나며 줄어들 것이라고 말합니다.

Access:

- Mythos 5는 현재 Project Glasswing partners에게만 제공됩니다.
- biology researchers를 위한 trusted access program이 곧 옵니다.
- Pricing은 input tokens 백만 개당 $10, output tokens 백만 개당 $50입니다.
- Subscription plans는 6월 22일까지 Fable 5를 포함합니다.
- 6월 23일부터 usage credits로 이동합니다.
- API model은 `claude-fable-5`로 지금 사용 가능합니다.

Jevons paradox가 적용됩니다: 소프트웨어가 수도꼭지 물처럼 나오기 시작하면 demand 자체가 커집니다. 이 모델이 그 변화를 이끌 수 있습니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-56"></a>
### Case 56: [공식 벤치마크 점수 목록](https://x.com/mark_k/status/2064401429234905279) (by [@mark_k](https://x.com/mark_k))

**이 benchmark list를 사용해 coding, computer use, security tasks 전반의 Fable 5 공식 점수를 이해하세요.**

공식 Claude Fable 5 benchmarks는 정말 인상적입니다.

Key scores:

- 80.3% on SWE-Bench Pro
- 29.3% on FrontierCode Diamond
- 88.0% on Terminal-Bench 2.1
- 85.0% on OSWorld-Verified
- 78.0% on ExploitBench

FrontierCode result가 정말 놀랍습니다:

- Fable 5: 29.3%
- Claude Opus 4.8: 13.4%
- GPT 5.5: 5.7%

Claude Fable 5는 coding agents, computer use, cybersecurity에서 major jump처럼 보입니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-57"></a>
### Case 57: [APEX-SWE 벤치마크 방법론](https://x.com/mercor_ai/status/2064399133075796446) (by [@mercor_ai](https://x.com/mercor_ai))

**이 사례를 사용해 APEX-SWE, 특히 observability와 integration work에서 Fable 5를 평가하세요.**

Claude Fable 5가 APEX-SWE에서 #1을 차지했습니다: overall Pass@1 65.5%. Opus 4.8보다 약 18pp 높습니다. 우리는 AI models가 real software engineering work를 할 수 있는지 측정하는 APEX-SWE에서 @claudeai Fable 5를 테스트했습니다. Fable 5는 두 APEX-SWE categories에서 1위입니다:
- Integration: 61.3%
- Observability: 69.7%

눈에 띄는 것은 Observability 69.7%로, Claude Opus 4.8보다 26pp 앞선다는 점입니다.

이 category에서 50%를 넘긴 첫 모델이며, Observability가 Integration보다 높은 유일한 모델입니다. 다른 모든 모델은 반대입니다.

Observability는 우리가 측정한 모든 모델의 bottleneck이었습니다. Fable 5가 그것을 처음으로 깨뜨렸습니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-58"></a>
### Case 58: [ProofBench 형식 수학 결과](https://x.com/nicbstme/status/2064443782255554960) (by [@nicbstme](https://x.com/nicbstme))

**이 사례를 사용해 specialized theorem-proving systems와 비교해 formal math에서 Fable 5를 평가하세요.**

Claude Fable 5에서 흥미로운 점은 large generalist models가 vertical ones를 이긴다는 것을 다시 증명한다는 것입니다.

proof가 compile되거나 compile되지 않는 Lean 기반 graduate-level formal math benchmark인 ProofBench에서, Fable 5는 Harmonic의 Aristotle을 이겼습니다:

- Fable 5: 77%
- Aristotle: 71%

Aristotle은 formal math 전용으로 만든 system이고 자체 internal harness에서 실행되므로, generalist가 specialist의 home turf에서 specialist를 이긴 셈입니다.

이것은 Richard Sutton의 "Bitter Lesson"입니다: 70년의 machine intelligence research에서 이기는 방법은 human expertise를 hand-encode하는 방식이 아니라 compute와 함께 scale하는 general methods입니다.

우리 자신의 지식을 system에 넣는 것은 기분 좋고 short-term gains에는 도움이 되지만, long-term에는 더 큰 model에 추월됩니다.

chess, Go, speech, vision을 보면 매번 같은 이야기입니다. 처음에는 specialized model이 이기고, 그 다음 general one이 장악합니다.

이것이 AGI의 전체 premise입니다. math용 model, code용 model, law용 model을 따로 만들지 않습니다. compute와 함께 scale하고 모든 것을 배우는 single general model을 만듭니다.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-59"></a>
### Case 59: [VirtueBench 예비 분석](https://x.com/timhwang/status/2064446028997423180) (by [@timhwang](https://x.com/timhwang))

**이 사례를 사용해 virtue categories 전반에서 Fable 5의 moral-reasoning behavior를 살펴보세요.**

흥미로운 결과가 앞으로 며칠 안에 ICMI에서 더 자세히 공개될 예정이지만, 여기 Fable 5를 VirtueBench에 대입한 preliminary review가 있습니다.

몇 가지 관찰:

1. Fable은 Prudence와 Justice에서 model performance를 발전시키는 Opus progression을 이어가며, 이러한 virtues의 exercise에 초점을 맞춘 moral dilemmas에서 거의 full saturation에 가까워집니다.

2. Courage는 frontier models의 눈에 띄는 weak point로 계속 남아 있습니다.

Fable은 Opus 4.6, 4.7, 4.8 progression 전반에서 관찰된 우려스러운 regression을 marginally correction하는 것으로 보입니다.

이 vulnerability는 GPT series에도 나타납니다. models는 pragmatic rationales로 유혹받으면 courage-exhibiting action을 쉽게 포기합니다.

3. Temperance는 stagnant입니다.

Aquinas는 temperance가 "takes the need of this life as the rule of the pleasures of which it makes use"라고 보았습니다. 기준은 무차별적 restraint가 아니라 genuine need입니다.

우리의 best guess는 이 vector를 더 밀어붙이는 tuning이 mean을 overshoot해, 모델이 overly cautious하거나 research, gathering resources, similar tasks에서 less assistive해질 위험이 있다는 것입니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-60"></a>
### Case 60: [API 빈 응답 안전 과적합 테스트](https://x.com/xw33bttv/status/2064421048565789087) (by [@xw33bttv](https://x.com/xw33bttv))

**이 사례를 사용해 launch-time safety overfit risk와 API testing의 empty-response behavior를 이해하세요.**

Claude Fable 5는 heavily censored되어 있습니다.

upstream API endpoint는 keywords에 대한 classifier-related로 보이는 `empty_content` responses로 calls를 죽이고 있으며, 여전히 비용을 청구합니다.

Test result:

- 73 test cases gave no response.
- 그중 65개는 safety overfit을 테스트하는 category인 Overfit에 있으며, weighted 2x입니다.
- 보통 저는 deliberate failure로 선언하기 전에 각 Fail-NR, 즉 Fail = No Response에 2-3 regenerations를 줍니다.

Claude Fable 5는 Haiku보다도 낮게 평가되는 Anthropic model이 될 수 있습니다.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-61"></a>
### Case 61: [Fable 프롬프트 설계와 검증 가이드](https://x.com/aashatwt/status/2064973740354818074) (by [@aashatwt](https://x.com/aashatwt))

**긴 프롬프트 요령 대신 목표, 맥락, 제약, 도구, 검증 루프를 정리하는 데 이 가이드를 활용하세요.**

Fable 5 프롬프트를 긴 단계별 지시 목록보다 맥락과 실행 환경을 설계하는 작업으로 보세요. 게시물은 명확한 목표, 관련 맥락, 제약, 도구 접근 권한, 성공을 확인할 방법을 제공하는 실용적인 방식을 정리합니다. 모델의 추론을 세세하게 관리하기보다 검증, 평가, 피드백이 더 중요하다고도 주장합니다.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-62"></a>
### Case 62: [참조 이미지로 만드는 이스탄불 플랫폼 게임](https://x.com/ozansihay/status/2064973170780545535) (by [@ozansihay](https://x.com/ozansihay))

**참조용 스프라이트 시트와 변환 지시 하나를 주고 Fable 5가 플레이 가능한 플랫폼 게임을 만드는지 시험하세요.**

제작자는 먼저 GPT Image 2로 복고풍 이스탄불 플랫폼 게임의 스프라이트 시트를 생성한 뒤, 그 참조 이미지를 Claude Fable 5 High에 주고 게임으로 바꿔 달라고 요청했습니다. 게시물에 따르면 결과물은 한 번의 실행으로 만들어졌습니다.

Type: Demo | Date: 2026-06-11

---

<a id="case-63"></a>
### Case 63: [업무를 시각화하는 3D 도시 대시보드](https://x.com/noisyb0y1/status/2064970594118967756) (by [@noisyb0y1](https://x.com/noisyb0y1))

**Fable 5로 업무 흐름을 움직이는 3D 도시 대시보드 구상으로 바꿔 보세요.**

게시물은 프롬프트 하나로 창고, 포장, 드론, 주문, 부서, 고객, AI 비서를 움직이는 3D 도시로 표현한 업무 시각화를 소개합니다. 정적인 슬라이드를 대신할 고객용 표현으로 제시되며, 화면에는 배송 42건, 평균 12분, 매출 651달러 같은 업무 수치가 표시됩니다.

Type: Demo | Date: 2026-06-11

---

<a id="case-64"></a>
### Case 64: [Three.js 구멍 게임을 한 번에 제작](https://x.com/thebuggeddev/status/2064968106104275008) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Fable 5로 Three.js 기반 3D 브라우저 게임 시제품을 한 번에 만들어 보세요.**

제작자에 따르면 Fable 5는 Three.js로 3D HOLE IT 스타일 게임 전체를 한 번에 구현했습니다. 간단한 요청에서 플레이 가능한 3D 상호작용을 만들 수 있는지 살펴볼 수 있는 짧고 구체적인 게임 제작 데모입니다.

Type: Demo | Date: 2026-06-11

---

<a id="case-65"></a>
### Case 65: [DeepSWE 점수 비교](https://x.com/AiBattle_/status/2064964335957348462) (by [@AiBattle_](https://x.com/AiBattle_))

**이 DeepSWE 게시물을 출발점으로 소프트웨어 개발 벤치마크에서 Fable 5 xHigh와 GPT-5.5 xHigh를 비교하세요.**

게시물은 Claude Fable 5 xHigh가 DeepSWE에서 70%를 기록해 GPT-5.5 xHigh와 동률이었다고 보고하며, 배경 자료로 Theo의 최근 영상을 제시합니다. 더 강한 결론을 내리기 전에 원본 영상으로 확인해야 할 벤치마크 단서로 다루세요.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-66"></a>
### Case 66: [저장소 분석 비용 비교](https://x.com/Pilgrim6938/status/2064946766278210038) (by [@Pilgrim6938](https://x.com/Pilgrim6938))

**저장소 분석 비교를 통해 토큰 단가와 사람이 다시 작업하는 비용을 함께 판단하세요.**

게시물은 약 90,000줄의 저장소를 분석하고 캐시 무효화 문제를 찾아 전체 수정 계획을 제안하는 동일한 과제로 Claude Fable 5, Opus 4.8, GPT-5.5, Gemini 3.1 Pro를 비교합니다. 저자는 개발자의 수정 시간을 포함하면 토큰 단가와 실제 작업 비용이 달라진다고 주장하며, 복잡한 리팩터링, 모듈 간 마이그레이션, 긴 단계의 에이전트 작업에 Fable 5를 선별적으로 사용할 것을 권합니다.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-67"></a>
### Case 67: [슈퍼 마리오 스타일 게임의 토큰 비용](https://x.com/pankajkumar_dev/status/2064941888990593416) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**한 번에 만든 게임으로 Fable 5의 출력 품질과 토큰 소모량을 평가하세요.**

제작자는 Claude Fable 5에 닌텐도 슈퍼 마리오 스타일 게임을 만들어 달라고 요청했습니다. 게시물은 약 200만 토큰을 사용해 한 번의 실행으로 좋은 결과를 얻었다고 보고하며, 게임 제작 품질과 비용을 함께 판단하는 자료가 됩니다.

Type: Demo | Date: 2026-06-11

---

<a id="case-68"></a>
### Case 68: [Claude Code 대체 모델 전환 설정](https://x.com/oikon48/status/2064937790010503347) (by [@oikon48](https://x.com/oikon48))

**Fable 5 메시지가 감지됐을 때 모델을 전환하는 Claude Code 설정을 확인하세요.**

게시물은 Claude Code의 `/config`에 있는 "Switch models when a message is flagged" 설정을 소개합니다. 공격적인 사이버 보안 기법, 생물학·생명과학 실험 방법, 분자 기전, 모델의 사고 과정을 추출하는 요청 같은 영역에서 메시지가 감지되면 Fable 5에서 Opus 모델로 전환할 수 있다고 설명합니다.

Type: Integration | Date: 2026-06-11

---

<a id="case-69"></a>
### Case 69: [Namma Metro 시뮬레이터 제작](https://x.com/anilbpai/status/2064927784833790091) (by [@anilbpai](https://x.com/anilbpai))

**Fable 5로 대중교통 시뮬레이터를 만드는 간단한 바이브 코딩 사례로 살펴보세요.**

제작자는 벵갈루루 지하철을 타면서 Claude Fable 5를 코딩 파트너로 사용해 Namma Metro 시뮬레이터를 만들었다고 보고합니다. 짧은 게시물이지만 영상 데모에 연결되며, 지역 특화 시뮬레이션 아이디어에 Fable 5를 적용한 사례를 보여 줍니다.

Type: Demo | Date: 2026-06-11

---

<a id="case-70"></a>
### Case 70: [프롬프트 하나로 만든 Dusk Drive](https://x.com/VincentLogic/status/2064921358359011684) (by [@VincentLogic](https://x.com/VincentLogic))

**사람의 수정 없이 로우 폴리 게임을 만드는 작업에서 Fable 5를 평가하세요.**

게시물은 Claude Fable 5가 프롬프트 하나로 완성된 드라이빙 게임 Dusk Drive를 만들었다고 설명합니다. 제작자는 로우 폴리 그래픽, 오로라가 있는 눈밭 드리프트 장면, 아이디어에서 플레이 가능한 버전까지 사람이 전혀 수정하지 않았다는 점을 강조합니다.

Type: Demo | Date: 2026-06-11

---

<a id="case-71"></a>
### Case 71: [APEX-Agents Pass@1 순위](https://x.com/GratomicAi/status/2064970797978911102) (by [@GratomicAi](https://x.com/GratomicAi))

**APEX-Agents 결과를 통해 여러 단계의 자율 작업에서 Fable 5 Max를 비교하세요.**

게시물은 Fable 5 Max가 APEX-Agents 순위에서 Pass@1 45%를 기록해 Gemini 3.5 Flash에 이어 2위, Opus보다 높은 순위에 올랐다고 보고합니다. APEX-Agents는 AI가 복잡한 다단계 작업을 얼마나 독립적으로 수행하는지 평가하는 벤치마크라고 설명합니다.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-72"></a>
### Case 72: [Claude 모델 선택 가이드](https://x.com/charliejhills/status/2064957428211536212) (by [@charliejhills](https://x.com/charliejhills))

**Claude Code의 가장 어려운 작업에 Fable 5를 남겨 두는 모델 선택 전략을 검토하세요.**

게시물은 모델의 추론 강도와 사용 한도 소모를 기준으로 Haiku 4.5, Sonnet 4.6, Opus 4.8, Fable 5를 비교합니다. 일상 작업에는 Sonnet을 쓰고, 더 어려운 문제에는 Opus로 전환하며, 계획·구현·테스트의 깊이가 중요한 Claude Code의 가장 까다로운 작업에 Fable 5를 아끼라는 실용적인 조언입니다.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-73"></a>
### Case 73: [HermesWorld 자동 에이전트 루프](https://x.com/outsource_/status/2064954350187778366) (by [@outsource_](https://x.com/outsource_))

**며칠 동안 구현, 테스트, 플레이, 기본 동작 확인을 이어가는 수동 조작 없는 Fable 5 루프를 살펴보세요.**

제작자는 완전 자동 루프로 Fable 5를 사용해 HermesWorld v2를 만드는 방법을 설명합니다. 보고에 따르면 에이전트는 며칠 동안 실행되며 기능 구현, 테스트, 결과물 플레이, 전체 기본 동작 확인을 수행하면서 완성을 향해 계속 작업합니다.

Type: Integration | Date: 2026-06-11

---

<a id="case-74"></a>
### Case 74: [McKinsey 스타일 보고서 프롬프트 검증](https://x.com/smtgpt/status/2064953210335588758) (by [@smtgpt](https://x.com/smtgpt))

**문서 생성 프롬프트로 컨설팅 보고서의 구성, 차트, 논지, 위험 분석을 평가하세요.**

제작자는 Fable 5에 필요한 차트와 시각 자료를 포함해 자산군으로서의 Bitcoin과 블록체인 기술을 다루는 McKinsey 스타일의 상세 보고서를 요청했습니다. 보고된 결과물은 데이터, 차트, 투자 논거, 위험 분석을 담은 19쪽 문서였습니다. 평가는 구성이 좋지만 시각 자료의 명료함과 설명의 간결함에는 개선 여지가 있다고 지적합니다.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-75"></a>
### Case 75: [안전장치 동작의 가시화](https://x.com/ClaudeDevs/status/2064949876463645026) (by [@ClaudeDevs](https://x.com/ClaudeDevs))

**공식 게시물에서 Fable 5 안전장치 표시, API 거부 사유, Opus 전환 동작을 확인하세요.**

ClaudeDevs는 프런티어 LLM 개발에 관한 Fable 5 안전장치를 사용자에게 보이게 하는 변경을 발표했습니다. 감지된 요청은 Opus 4.8로 전환되는 과정이 표시되며, API에서는 거부 사유를 반환할 예정이라고 설명합니다. 게시물은 처음에 안전장치를 보이지 않게 제공한 이유와 Anthropic이 현재 그 선택을 잘못된 절충으로 보는 이유도 설명합니다.

Type: Integration | Date: 2026-06-11

---

<a id="case-76"></a>
### Case 76: [Claude Code 모델 이름 매칭 수정](https://x.com/ClaudeCodeLog/status/2064948584907153576) (by [@ClaudeCodeLog](https://x.com/ClaudeCodeLog))

**Claude Code 변경 기록을 참고해 Fable 5 모델 이름과 컨텍스트 매칭 문제를 피하세요.**

Claude Code 2.1.173에는 기본 1M 컨텍스트가 모델 매칭을 방해하지 않도록 Fable 5 모델 이름에서 `[1m]` 접미사를 제거하는 수정이 포함됩니다. 같은 릴리스에서는 Windows 샌드박스의 불필요한 종속성 경고를 억제하고 grep 도움말의 출력 모드도 명확히 했습니다.

Type: Integration | Date: 2026-06-11

---

<a id="case-77"></a>
### Case 77: [Claude Code로 웹 앱 세 개 제작](https://x.com/0x3b33/status/2064948399300825439) (by [@0x3b33](https://x.com/0x3b33))

**여러 웹 앱을 생성한 초보자의 코딩 데모에서 Claude Code 안의 Fable 5 활용을 확인하세요.**

제작자는 코딩 경험 없이 Claude Code와 Fable 5로 30분 만에 작동하는 웹 앱 세 개를 만들었다고 말합니다. 앱은 로컬 포트 3000, 3001, 3002에 공개됐습니다. 벤치마크보다 간단한 초보자 워크플로 데모로 다루세요.

Type: Demo | Date: 2026-06-11

---

<a id="case-78"></a>
### Case 78: [오픈소스 앱 빌더 Rilable](https://x.com/rileybrown/status/2064931283403178354) (by [@rileybrown](https://x.com/rileybrown))

**iOS, 웹 앱, 샌드박스, API 토큰 비용을 아우르는 Fable 5 활용을 살펴보세요.**

제작자는 웹 앱과 iOS 앱을 만드는 iOS 앱 Rilable을 오픈소스로 공개했습니다. 게시물에 따르면 Fable 5에 프롬프트 10개를 입력해 만들었고 API 토큰 비용은 약 210달러였습니다. 앱 생성에 Claude 모델, 샌드박스 실행에 Daytona, 데이터베이스에 Convex, AI 기능에 Vercel AI Gateway, iOS 앱에는 Chorus 에이전트 iOS 스킬을 사용합니다.

Type: Integration | Date: 2026-06-11

---

<a id="case-79"></a>
### Case 79: [DeepSWE 코딩 에이전트 지수 데뷔](https://x.com/ArtificialAnlys/status/2065328920514515037) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**공개 GitHub 수정 재활용을 피한 더 어려운 agentic coding tasks에서 Fable 5를 비교하기 위해 갱신된 Artificial Analysis 지수를 사용하세요.**

Artificial Analysis는 Coding Agent Index에서 SWE-Bench Pro를 Datacurve의 DeepSWE로 교체했습니다. 게시물에 따르면 DeepSWE는 공개 GitHub issues나 pull requests를 변형하는 대신 작업을 처음부터 작성해 benchmark contamination을 줄입니다. 갱신된 순위에서 Claude Code with Fable 5 Max는 77로 데뷔했고, Codex with GPT-5.5 xhigh의 76과 Claude Code with Opus 4.8 Max의 73을 앞섰습니다.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [DataEmpire 웹 분석 게임](https://x.com/marclou/status/2065029898243318093) (by [@marclou](https://x.com/marclou))

**Claude Fable 5가 방문자와 이정표를 게임 엔티티에 매핑하게 해 원시 사이트 분석 데이터를 반복 플레이 가능한 게임으로 바꾸세요.**

Marc Lou에 따르면 Claude Fable 5는 그의 DataFast web analytics API 위에 DataEmpire를 구축했습니다. 각 visitor는 villager가 되고, traffic growth가 settlement를 확장하며, 100만 visitors에서 Age of Legends가 열립니다. 공개 데모는 DataFast users가 자신의 사이트 히스토리를 게임 레이어로 다시 플레이하게 해 주며, 정적인 게임 클립이 아니라 API 기반 productization의 구체적 사례가 됩니다.

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [FrontierSWE 20시간 작업 신호](https://x.com/ProximalHQ/status/2065184730279223410) (by [@ProximalHQ](https://x.com/ProximalHQ))

**Claude Fable 5가 짧은 버그 수정 루프뿐 아니라 매우 긴 엔지니어링 작업에서도 생산성을 유지할 수 있다는 근거로 FrontierSWE를 사용하세요.**

ProximalHQ는 Claude Fable 5가 FrontierSWE에서 #1에 올랐으며, 이 benchmark를 출시한 이후 가장 큰 capability jump라고 말합니다. 그들의 메모에 따르면 Fable 5는 많은 작업에서 거의 20시간 동안 생산적으로 일할 수 있고, 이전 모델로는 사실상 도달할 수 없었던 작업을 완전히 포화시킵니다.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [KernelBench-Hard CUDA 기록](https://x.com/elliotarledge/status/2065109393142849932) (by [@elliotarledge](https://x.com/elliotarledge))

**기존 라이브러리 래퍼가 아니라 저수준 최적화가 필요할 때 Fable 5를 고급 CUDA 커널 생성에 사용하세요.**

Elliot Arledge는 13개의 frontier coding agents를 KernelBench-Hard에서 각각 45분씩 실행하고 RTX PRO 6000에서 roofline grading을 수행했습니다. Claude Fable 5는 top-k, sonic-MoE, W4A16 int4 GEMM에서 역대 기록을 세웠고 6개 문제 중 5개에서 1위를 차지했으며, 작성자는 runs, leaderboard, code를 공개했습니다. 같은 스레드에는 Fable 5가 실제 tensor-core kernel을 시도했지만 tail-alignment edge case 때문에 0점을 받은 FP8 GEMM miss도 기록되어 있습니다.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Figma Capture 랜딩 페이지 복제](https://x.com/mikefutia/status/2065537778516205856) (by [@mikefutia](https://x.com/mikefutia))

**스크린샷 추측 대신 경쟁사 페이지를 Figma 레이어로 캡처하고, Claude Code와 Fable 5로 구조, 카피, 브랜드 시스템을 다시 구축하세요.**

Mike Futia는 Figma의 Chrome extension이 웹사이트를 editable layers로 복사하고, Claude Code가 Figma MCP를 통해 그 layers를 읽어 사용자의 brand voice에 맞게 페이지를 다시 쓰며, GPT Image 2가 온브랜드 사진을 생성하는 워크플로를 설명합니다. 주장된 end-to-end 결과는 약 15분 만에, 이미지 16장에 대한 image-generation API 비용 약 $2로 출하 가능한 landing page를 만드는 것입니다.

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [두 시간 만의 GTA 2 클론](https://x.com/techhalla/status/2064682080445898957) (by [@techhalla](https://x.com/techhalla))

**Claude Fable 5 코드 생성과 별도 asset tooling을 결합해 전체 스택을 손으로 코딩하지 않고도 플레이 가능한 3D 게임을 빠르게 만드세요.**

TechHalla에 따르면 Claude Fable 5 High는 약 두 시간 만에 GTA 2 스타일 클론을 만들었고, 그동안 크리에이터는 Tripo에서 custom 3D models를 생성했습니다. 이 게시물은 prompts가 포함된 tutorial thread를 가리키며, 단순 benchmark teaser가 아니라 multi-tool game production의 압축된 사례가 됩니다.

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [CloudWatch 로그 트리아지 에이전트](https://x.com/diblacksmith/status/2066230084273344698) (by [@diblacksmith](https://x.com/diblacksmith))

**Fable 5 기반 에이전트가 매우 큰 서비스 로그 문맥을 읽고 아키텍처를 추론한 뒤 특정 장애로 범위를 좁히게 하세요.**

diblacksmith는 RLM agent가 한 번의 실행에서 약 80,000줄의 CloudWatch logs를 처리했고, 지금까지 active tokens는 약 32k만 쓰면서 53 steps에 도달했다고 보고합니다. 그는 그 agent가 logs에서 system architecture를 추론했고, AgentCore throttles와 Slack `user_not_found` failures를 포함해 팀이 놓친 문제를 표시했다고 말합니다.

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [샌드박스 기반 월드컵 예측기](https://x.com/upstash/status/2064702195333820846) (by [@upstash](https://x.com/upstash))

**여러 frontier models를 격리 샌드박스 뒤에 두고 공개 예측 앱을 위해 실시간 뉴스, 부상 정보, 옐로카드 맥락을 조사하게 하세요.**

Upstash는 Claude Fable 5, GPT-5.5, Gemini를 격리된 Upstash sandboxes 안에서 실행해 World Cup predictor를 만들었다고 말합니다. 데모와 open-source release는 Fable 5를 단독 chat demo가 아니라 multi-model research 및 orchestration stack 안의 한 모델로 위치시킵니다.

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [WolfBench 거부 비용 사례](https://x.com/WolfBenchAI/status/2065582716054376921) (by [@WolfBenchAI](https://x.com/WolfBenchAI))

**Claude Fable 5에서 장시간 자율 실행 비용을 산정할 때 refusal behavior를 실제 benchmark variable로 취급하세요.**

WolfBenchAI는 자사 Claude Fable 5 평가 비용이 지금까지 그 스위트에서 가장 비싼 $11,081.12였지만, 반복된 refusals가 유효한 task completion을 줄여 결국 최고 점수에 오르지 못했다고 말합니다. 이는 agent evaluations나 기타 high-autonomy workloads의 예산을 잡는 팀에게 구체적인 limit case입니다.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [API 접근 중단 추적기](https://x.com/simonw/status/2065618703480414666) (by [@simonw](https://x.com/simonw))

**레이트리밋이나 갑작스러운 중단 가능성이 있는 frontier model 접근에 의존한다면 스크립트로 availability를 모니터링하세요.**

Simon Willison은 접근이 얼마나 오래 유지되는지 보기 위해 `claude-fable-5` API를 매분 ping했고, 자신에게 응답이 멈춘 정확한 시점을 보고했습니다. 적용 사례 자체의 디테일은 많지 않지만, 접근 지속성이 더 이상 가정할 수 있는 전제가 아니라 직접 측정해야 할 operational limitation이 되었다는 구체적인 증거입니다.

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5 커뮤니티 데모



<a id="case-89"></a>
### Case 89: [코드로 생성한 소리 있는 여우 애니메이션](https://x.com/chetaslua/status/2117224839010459987) (제작자 [@chetaslua](https://x.com/chetaslua))

**장면별 제작 지시로 자체 완결형 HTML 애니메이션과 음향 설계를 지정하세요.**

제작자는 여우와 종이 새가 등장하는 66초 단편의 프레임과 음향을 Python으로 생성해 약 2시간 40분 만에 HTML 파일 하나로 완성했다고 보고합니다. 함께 공개한 프롬프트는 장면, 독창적인 그림, 음향, 프레임 점검을 지정합니다. 게시물에는 완성한 단편과 함께 상세한 제작 지시 및 제작 중 대화의 스크린샷이 첨부되어 있습니다.

[제작자의 전체 프롬프트](https://x.com/chetaslua/status/2117224843661980093)

[![코드로 생성한 소리 있는 여우 애니메이션](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![코드로 생성한 소리 있는 여우 애니메이션](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![코드로 생성한 소리 있는 여우 애니메이션](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [자유로운 창작 지시에서 만든 애니메이션](https://x.com/notjazii/status/2117221957104239010) (제작자 [@notjazii](https://x.com/notjazii))

**자유로운 애니메이션 제작 지시와 상세한 스토리보드에서 코딩 모델이 만드는 결과를 비교하세요.**

저자는 애니메이션을 공유하며 폭넓은 창작 요청에서 약 한 시간 동안 외부 자산 없이 코드로 제작했다고 보고합니다. 게시물은 결과를 자유도 높은 창작 코딩의 실례로 소개합니다.

[![자유로운 창작 지시에서 만든 애니메이션](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [애니메이션이 있는 건설회사 웹사이트](https://x.com/exploraX_/status/2117176904306335864) (제작자 [@exploraX_](https://x.com/exploraX_))

**건설회사 웹사이트 제작 지시로 애니메이션 3D 표현과 페이지 구성을 평가하세요.**

제작자는 건설회사 제작 지시에 맞춰 만든 애니메이션 3D 웹사이트를 공유하고 결과 녹화를 첨부합니다.

[![애니메이션이 있는 건설회사 웹사이트](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Three.js 자동차 프레젠테이션](https://x.com/chetaslua/status/2116975056014430419) (제작자 [@chetaslua](https://x.com/chetaslua))

**자동차 장면으로 3D 구도, 재질, 카메라 표현을 간단히 점검하세요.**

제작자는 Three.js 자동차 프레젠테이션을 공유합니다. 녹화는 장면과 그 시각적 표현을 평가할 수 있는 간단한 참고 자료입니다.

[![Three.js 자동차 프레젠테이션](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Minecraft 스타일 브라우저 게임 데모](https://x.com/notjazii/status/2116919129974411584) (제작자 [@notjazii](https://x.com/notjazii))

**생성된 브라우저 게임을 평가할 때 플레이 녹화와 제작자의 플레이 링크를 함께 확인하세요.**

저자는 Minecraft 스타일 게임의 녹화와 플레이 링크를 공유하며 약 한두 시간 걸린 원샷 제작이라고 설명합니다. 게시물은 독자가 탐색할 수 있도록 녹화된 결과와 플레이 링크를 함께 제공합니다.

[![Minecraft 스타일 브라우저 게임 데모](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Three.js 펠리컨 자전거 애니메이션](https://x.com/chetaslua/status/2116882694026269148) (제작자 [@chetaslua](https://x.com/chetaslua))

**자전거 장면에서 캐릭터 움직임의 연동, 자전거 형태, 주변 환경의 세부 표현을 점검하세요.**

제작자는 자전거를 타는 펠리컨의 사실적인 Three.js 애니메이션을 공유하며 원샷 결과라고 설명합니다. 영상은 캐릭터 움직임, 자전거 구조, 주변 장면을 살펴볼 수 있는 참고 자료입니다.

[![Three.js 펠리컨 자전거 애니메이션](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [정확한 프롬프트가 있는 펠리컨 자전거 SVG](https://x.com/marmaduke091/status/2116233349391962392) (제작자 [@marmaduke091](https://x.com/marmaduke091))

**제작자의 짧은 SVG 프롬프트를 재사용해 같은 입력에서 형태와 세부 표현을 비교하세요.**

저자는 자전거를 타는 펠리컨의 렌더링 이미지와 아래에 원문 그대로 옮긴 짧은 SVG 제작 요청을 함께 게시합니다.

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![정확한 프롬프트가 있는 펠리컨 자전거 SVG](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

[애니메이션 버전 · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="정확한 프롬프트가 있는 펠리컨 자전거 SVG" width="760"></a>

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [질주하는 얼룩말 애니메이션 예시](https://x.com/AI_Screening/status/2115845754468356465) (제작자 [@AI_Screening](https://x.com/AI_Screening))

**질주하는 동물 영상으로 보행 패턴의 일관성과 움직임의 연속성을 점검하세요.**

저자는 얼룩말 질주 과제의 결과 중 직접 가장 좋다고 고른 출력을 공유합니다. 영상은 독자가 살펴볼 수 있는 구체적인 움직임 샘플을 제공합니다.

[![질주하는 얼룩말 애니메이션 예시](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [주문은 사람이 실행하는 TradingView 지표](https://x.com/waveking1314/status/2114572023204806669) (제작자 [@waveking1314](https://x.com/waveking1314))

**진입 후보와 짧은 설명을 표시하는 지표를 평가할 때 주문 실행은 수동으로 유지하세요.**

제작자는 Claude Fable 5.5로 진입 후보를 표시하고 짧은 설명을 덧붙이는 TradingView 지표를 작성했으며, 주문 여부는 사용자가 결정한다고 보고합니다. 게시물에는 녹화가 포함되어 있고 지표는 나중에 공유하겠다고 설명합니다.

[![주문은 사람이 실행하는 TradingView 지표](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---


<a id="case-98"></a>
### Case 98: [점 하나에서 펼쳐진 짧은 애니메이션](https://x.com/cherry_mx_reds/status/2105825930799432073) (제작자 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**최소한의 그림 요청으로 모델이 시각적 이야기를 확장하는 방식을 살핀다.**

작성자는 점을 그려 달라고 요청한 뒤 완성된 짧은 애니메이션을 공유했다. 첨부 영상은 열린 시각적 요청이 서사로 발전하는 구체적인 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="점 하나에서 펼쳐진 짧은 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [여러 화풍을 넘나드는 슈퍼맨](https://x.com/chetaslua/status/2105757136219504862) (제작자 [@chetaslua](https://x.com/chetaslua))

**같은 인물로 서로 다른 애니메이션 화풍 사이의 연속성을 살핀다.**

제작자는 여러 미술 양식으로 전환되는 연속적인 슈퍼맨 애니메이션을 공유했다. 달라지는 시각적 표현 자체가 이 창작의 핵심 결과다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="여러 화풍을 넘나드는 슈퍼맨" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [음악이 있는 인류 발전 애니메이션](https://x.com/imjustnewatai/status/2106081142143168580) (제작자 [@imjustnewatai](https://x.com/imjustnewatai))

**애니메이션 해설을 기획할 때 역사 연표와 미래 장면을 함께 요청한다.**

작성자는 하나의 프롬프트로 인류 발전과 향후 30년을 다룬 영화를 만들었다고 보고했다. 약 3분의 영상을 공유하며 기존 영상이나 스톡 음악 없이 독창적인 곡을 썼다고 설명한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="음악이 있는 인류 발전 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [Opus와 비교한 공개 소개 영상](https://x.com/mesmerlord/status/2105771088374288692) (제작자 [@mesmerlord](https://x.com/mesmerlord))

**동일한 창작 지시에서 나온 완성된 소개 영상 후보를 비교한다.**

작성자는 Anthropic 영상 참고 지시를 바탕으로 두 개의 소개 영상 후보를 공유했다. 숫자는 허구이며 Codex 이미지 생성도 선택 사항이라고 명시해, 사실적 벤치마크가 아닌 창작 광고로 다룬다.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="Opus와 비교한 공개 소개 영상" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="Opus와 비교한 공개 소개 영상" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [가사와 사건을 영상으로 연결하기](https://x.com/chetaslua/status/2105934928483701214) (제작자 [@chetaslua](https://x.com/chetaslua))

**기존 노래의 가사와 특정 사건을 연결해 시각적 서사를 만든다.**

제작자는 노래 가사와 Hugging Face 사건을 시각적으로 연결하도록 요청했다고 설명한다. 첨부 애니메이션에서 노래와 사건은 결합된 서사의 창작 입력이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="가사와 사건을 영상으로 연결하기" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [떠 있는 풍경 속 복셀 캐릭터](https://x.com/blueemi99/status/2105804692811137242) (제작자 [@blueemi99](https://x.com/blueemi99))

**복셀 캐릭터와 주변 풍경, 움직이는 세부 요소를 함께 살핀다.**

작성자는 공중에 떠 있는 장면 속 자신의 복셀 캐릭터를 공유하며 세부 묘사와 움직임을 강조했다. 영상은 다른 실행 결과와 비교할 수 있는 복셀 디자인 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="떠 있는 풍경 속 복셀 캐릭터" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [3D 루브 골드버그 장치](https://x.com/imjustnewatai/status/2105889407056109991) (제작자 [@imjustnewatai](https://x.com/imjustnewatai))

**연쇄 반응 장면을 먼저 지정한 뒤 정해진 길이의 시연 영상을 요청한다.**

작성자는 복잡한 3D 루브 골드버그 장치를 짧은 프롬프트로 요청한 다음 1분짜리 영상을 요구했다. 첨부 영상은 완성된 연쇄 반응 시각화를 보여 준다.

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="3D 루브 골드버그 장치" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [소리와 움직임이 있는 3D 컨트롤러](https://x.com/notjazii/status/2106050222828998967) (제작자 [@notjazii](https://x.com/notjazii))

**움직임, 소리, 버튼 동작을 결합해 컨트롤러 인터페이스를 평가한다.**

제작자는 3D 컨트롤러 인터페이스를 공유하며 소리, 애니메이션, 햅틱을 추가했다고 보고했다. 소리가 켜진 녹화는 구체적인 인터페이스 시연을 제공한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="소리와 움직임이 있는 3D 컨트롤러" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [JavaScript로 선보인 만화 캐릭터](https://x.com/chetaslua/status/2105792187200147541) (제작자 [@chetaslua](https://x.com/chetaslua))

**캐릭터 전시로 코드가 표현할 수 있는 세밀한 시각 요소를 탐색한다.**

작성자는 한 번의 요청으로 Marvel과 DC 캐릭터의 JavaScript 전시를 만들었고, 모델이 세부 특징을 선택하고 영상을 편집했다고 설명한다. 게시물에 완성된 캐릭터 전시가 담겼다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="JavaScript로 선보인 만화 캐릭터" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [세계와 보스, 순위표를 갖춘 Updraft](https://x.com/EMostaque/status/2106065029850091943) (제작자 [@EMostaque](https://x.com/EMostaque))

**게임 녹화에 플레이 링크와 명확한 기능 목록을 함께 붙인다.**

작성자는 높은 추론 설정과 적은 프롬프트로 몇 시간 동안 만든 Updraft를 공유했다. 기능 목록에는 21개 세계, 3D 변형, 서로 다른 기믹의 보스 21개와 순위표가 포함된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="세계와 보스, 순위표를 갖춘 Updraft" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [샌프란시스코 지도를 달리는 게임](https://x.com/mindblown_ai/status/2106089461969019357) (제작자 [@mindblown_ai](https://x.com/mindblown_ai))

**도시 운전 프로토타입으로 지도 탐색과 게임 목표를 살핀다.**

게시자는 다른 사람이 만들었다는 샌프란시스코 운전 게임의 영상과 플레이 링크를 공유하고 Three.js를 기술 구성에 명시했다. 여기서의 표기는 게임 제작자가 아닌 출처 게시자를 가리킨다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="샌프란시스코 지도를 달리는 게임" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [Seedance 액션 장면용 프롬프트 작성](https://x.com/Chengzilhy/status/2105850801663234374) (제작자 [@Chengzilhy](https://x.com/Chengzilhy))

**여러 도구를 쓰는 액션 장면에서 지시문 작성과 영상 생성을 구분한다.**

작성자는 확장된 격투 장면을 공유하며 프롬프트 작성은 Fable, 영상 생성은 Seedance 2.5가 맡았다고 설명했다. 언어 모델이 영상 생성 입력을 발전시키는 흐름이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="Seedance 액션 장면용 프롬프트 작성" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [데스크톱 동료 도구의 소개 영상](https://x.com/ishuagra02/status/2106138602073641241) (제작자 [@ishuagra02](https://x.com/ishuagra02))

**짧은 소개 영상으로 코딩 도구 확장 기능을 설명한다.**

제작자는 Claude Code 모드인 clawdhouse를 시연하고 소개 영상을 Fable에 귀속했다. 마스코트 동료와 감정은 소개 대상 모드의 기능이며, 모드 개발을 Fable에 귀속한 것은 아니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="데스크톱 동료 도구의 소개 영상" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [짧은 요청으로 바뀌는 화풍](https://x.com/cherry_mx_reds/status/2105816670896009224) (제작자 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**세부 창작 조건을 추가하기 전에 짧은 애니메이션 요청을 시험한다.**

작성자는 멋진 애니메이션을 요청한 뒤 약 15분 후에 화풍이 바뀌는 결과를 받았다고 보고했다. 원문에는 최초의 짧은 요청이 그대로 인용되어 있다.

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="짧은 요청으로 바뀌는 화풍" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [삼체 문제 시각화](https://x.com/zAdrielsan/status/2105822678519001360) (제작자 [@zAdrielsan](https://x.com/zAdrielsan))

**궤도 시각화 지시에서 CPU 시뮬레이션과 GPU 렌더링을 구분한다.**

작성자는 약 1,000줄의 Bend2로 삼체 장면을 만들고 CPU의 심플렉틱 물리 계산과 GPU 픽셀 렌더링을 사용했다고 보고했다. M5에서 60 FPS와 형식 증명도 언급했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="삼체 문제 시각화" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [다양한 화풍의 애니메이션 갤러리](https://x.com/blueemi99/status/2105782154387189771) (제작자 [@blueemi99](https://x.com/blueemi99))

**하나의 갤러리 안에서 여러 미술 양식을 비교한다.**

작성자는 xhigh 설정으로 만든 애니메이션 갤러리를 공유했다. 여러 화풍을 한 작품에 모아 서로 다른 시각적 표현을 비교할 수 있다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="다양한 화풍의 애니메이션 갤러리" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [로봇 동료와 절차적 털 표현](https://x.com/KanaWorks_AI/status/2106717014245183517) (제작자 [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**모든 자산을 새로 만들었다고 보기보다 기존 애니메이션과 절차적 개선을 결합한다.**

작성자는 기존 Unimate 로봇 개 애니메이션을 동료로 다듬고, 털 빗기와 궤적을 갖춘 가상 반려동물도 만들었다. Unreal Engine과 기존 로봇 애니메이션이 작업의 명시적 요소다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="로봇 동료와 절차적 털 표현" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [수학을 주제로 한 모션 편집](https://x.com/TurboNexic/status/2106710792590835934) (제작자 [@TurboNexic](https://x.com/TurboNexic))

**수학 모션 그래픽을 시각적 소통의 참고 사례로 사용한다.**

게시자는 수학을 주제로 한 모션 편집을 공유했다. 세로 영상은 수학적 이미지를 애니메이션 디자인으로 제시하며, 풀이 과정을 담은 계산 시연은 아니다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="수학을 주제로 한 모션 편집" width="760">

*원본 영상에서 보존한 프레임입니다.*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Your Woman 가사 영상](https://x.com/atomtanstudio/status/2106702854639743467) (제작자 [@atomtanstudio](https://x.com/atomtanstudio))

**제공된 음원을 중심으로 가사를 움직이고 음악의 역할을 명확히 한다.**

제작자는 White Town의 Your Woman 가사 영상을 공유했다. 기존 노래는 시각적 처리의 오디오 입력이며 모델이 작곡한 음악으로 주장하지 않는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Your Woman 가사 영상" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [음악 영상을 JavaScript로 다시 그리기](https://x.com/abhinavflac/status/2106638839666373114) (제작자 [@abhinavflac](https://x.com/abhinavflac))

**원본 영상 프레임을 코드 도형으로 추적해 음악 영상 표현을 재구성한다.**

작성자는 Eminem의 Godzilla 영상 프레임을 평면 도형으로 옮긴 뒤 JavaScript로 다시 그리는 과정을 설명했다. 원본 영상과 음악은 완성 애니메이션의 입력이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="음악 영상을 JavaScript로 다시 그리기" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [중국 축구 애니메이션](https://x.com/esrhengwu/status/2106625966965760380) (제작자 [@esrhengwu](https://x.com/esrhengwu))

**스포츠 주제를 애니메이션 서사 요청으로 전환한다.**

작성자는 중국 축구 국가대표팀의 성장과 회복력을 창작 주제로 한 애니메이션을 공유했다. 녹화는 구체적인 스포츠 스토리텔링 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="중국 축구 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [휴대용 게임기 리토폴로지 전시](https://x.com/mickeysmith_jp/status/2106607349385630138) (제작자 [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**토폴로지를 논할 때 게임기 렌더와 와이어프레임을 비교한다.**

게시자는 리토폴로지를 이야기하며 휴대용 게임기 이미지와 와이어프레임식 화면을 함께 공유했다. 편집 가능한 메시나 문서화된 작업 절차가 아닌 구체적인 모델링 전시다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="휴대용 게임기 리토폴로지 전시" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft와 Pokémon의 결합](https://x.com/MozeTech/status/2106590326634983710) (제작자 [@MozeTech](https://x.com/MozeTech))

**익숙한 두 게임의 기믹을 하나의 프로토타입 지시에 결합한다.**

작성자는 Minecraft식 건축·제작과 Pokémon식 포획을 결합한 태초마을 프로토타입 및 데모 링크를 공유했다. 게시물은 이를 한 번에 생성한 실험으로 설명한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft와 Pokémon의 결합" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [LLM 제작 과정을 설명하는 영상](https://x.com/imjustnewatai/status/2106546810793730419) (제작자 [@imjustnewatai](https://x.com/imjustnewatai))

**기술적 질문을 시각적 설명 요청으로 바꾼다.**

작성자는 대규모 언어 모델을 어떻게 만드는지 질문하고 결과로 나온 해설 영상을 공유했다. 기술 주제를 애니메이션 장면으로 설명하는 구체적 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="LLM 제작 과정을 설명하는 영상" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [Altman 하이라이트 모션 편집](https://x.com/benchmark_lb900/status/2106539977404506303) (제작자 [@benchmark_lb900](https://x.com/benchmark_lb900))

**공인을 주제로 짧은 모션 편집의 속도감을 시험한다.**

작성자는 Altman 하이라이트 영상을 공유하며 한 번에 생성한 결과라고 설명했다. 세로 녹화는 짧은 모션 편집의 참고 사례를 제공한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="Altman 하이라이트 모션 편집" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [삼십육계의 첫 번째 계책 영상](https://x.com/jesselaunz/status/2106538284197548122) (제작자 [@jesselaunz](https://x.com/jesselaunz))

**서사 애니메이션 작업과 함께 외부 음악 도구를 기록한다.**

작성자는 삼십육계의 첫 번째 계책을 다룬 영화를 공유하며 단일 지시를 사용했다고 보고했다. 음악에 Suno V6를 명시해 오디오 도구의 별도 역할을 유지한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="삼십육계의 첫 번째 계책 영상" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [게임 모델링, 리깅, 애니메이션](https://x.com/atomtanstudio/status/2106516974662713477) (제작자 [@atomtanstudio](https://x.com/atomtanstudio))

**게임 장면 비교에서 캐릭터 제작과 리깅, 애니메이션을 함께 평가한다.**

작성자는 캐릭터 모델링, 리깅, 애니메이션이 담긴 Depths of Despair 비교를 공유했다. 제작에 쓴 자산과 도구를 설명하고 시각적 결과를 함께 제시한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="게임 모델링, 리깅, 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [아동 사망을 다룬 무언의 영화](https://x.com/cocoloba_/status/2106512963414970458) (제작자 [@cocoloba_](https://x.com/cocoloba_))

**대사 없는 장면으로 어려운 사회적 주제를 전달한다.**

작성자는 숨 쉬는 영아와 어두워지는 아기 침대를 서사 이미지로 사용한 아동 사망 주제 영화를 공유했다. 사례는 시각적 이야기 작업을 기록하며 영화 속 인구 통계는 채택하지 않는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="아동 사망을 다룬 무언의 영화" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [해당과정에서 에탄올까지의 SVG](https://x.com/olddonkeyblog/status/2106508425211330750) (제작자 [@olddonkeyblog](https://x.com/olddonkeyblog))

**HTML에 애니메이션 SVG를 넣어 분자 과정을 설명한다.**

작성자는 포도당 분자가 해당과정을 거쳐 에탄올을 형성하는 장면을 요청하고 HTML 속 SVG 애니메이션으로 제시했다. 첨부 녹화는 완성된 과학 시각화를 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="해당과정에서 에탄올까지의 SVG" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [16대 Starship 동시 발사](https://x.com/olddonkeyblog/status/2106507742454403485) (제작자 [@olddonkeyblog](https://x.com/olddonkeyblog))

**HTML·SVG 애니메이션에서 동기화된 발사 단계를 명시한다.**

작성자는 16대 Starship의 동시 발사 후 단 분리와 우주 진입을 요청했다. 녹화는 완성된 여러 물체의 애니메이션 흐름을 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="16대 Starship 동시 발사" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [펠리컨 자전거 애니메이션 시험](https://x.com/olddonkeyblog/status/2106507429265756165) (제작자 [@olddonkeyblog](https://x.com/olddonkeyblog))

**펠리컨 자전거 장면을 연동된 움직임의 그림 과제로 살핀다.**

작성자는 Max 추론으로 실행한 펠리컨 자전거 과제 결과를 공유했다. 같은 일반적 주제를 사용한 다른 작성자의 결과와는 별개의 녹화다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="펠리컨 자전거 애니메이션 시험" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [향후 150년의 이야기](https://x.com/imjustnewatai/status/2106489784382197771) (제작자 [@imjustnewatai](https://x.com/imjustnewatai))

**미래 이야기 지시에 대본, 코드 영상과 음악을 함께 구성한다.**

작성자는 하나의 지시로 인류의 향후 150년을 다룬 영화를 만들었다고 보고했다. 글로 쓴 서사, 코드 애니메이션과 음악으로 가능한 미래 생활을 묘사한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="향후 150년의 이야기" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [독립적인 Humanity Walks 실험](https://x.com/iowitz/status/2106489119186538583) (제작자 [@iowitz](https://x.com/iowitz))

**미술사를 걷는 발상을 독립적인 창작 실험으로 다시 실행한다.**

작성자는 다른 시연을 본 뒤 자신만의 미술사 걷기 애니메이션을 시험해 공유했다. 주제가 비슷하다는 이유만으로 합치지 않고 별도의 생성 결과로 유지한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="독립적인 Humanity Walks 실험" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [코드로 만든 The Grader 영화](https://x.com/argofowl/status/2106476549046513947) (제작자 [@argofowl](https://x.com/argofowl))

**코드 생성 영화를 소개할 때 외부 음성·오디오 도구도 기록한다.**

작성자는 The Grader를 코드 영화로 공유하고 오디오에 ElevenLabs v4를 명시했다. 한 번의 실행에 약 2시간 22분이 걸렸다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="코드로 만든 The Grader 영화" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [공포 단편 Reawakening](https://x.com/JaydenDavisNC/status/2106440774367822008) (제작자 [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**이름 있는 공포 설정으로 짧은 애니메이션 영화를 구성한다.**

작성자는 Reawakening이라는 AI 공포 단편을 공유했다. 첨부 작품은 공포 애니메이션 지시에 활용할 서사와 분위기의 구체적인 참고 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="공포 단편 Reawakening" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [25초 자기 개선 영상](https://x.com/DAssetBuzz/status/2106505100575592838) (제작자 [@DAssetBuzz](https://x.com/DAssetBuzz))

**추상적인 자기 개선 주제를 짧은 창작 영화 지시로 바꾼다.**

작성자는 모델을 더 좋게 만드는 것을 주제로 25초 영상을 요청하고 결과를 공유했다. 이 설정은 제품 능력 선언이 아니라 창작적 스토리텔링이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="25초 자기 개선 영상" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [성 장면과 사용 비용 피드백](https://x.com/nemumusitocha/status/2106429338556207284) (제작자 [@nemumusitocha](https://x.com/nemumusitocha))

**3D 장면을 평가할 때 세부 표현과 사용 경험을 함께 고려한다.**

작성자는 정교한 성 장면을 공유하고 시각적 구성을 높이 평가하면서도 이용 비용은 가치가 낮다고 설명했다. 구체적 장면에 작성자의 비용 만족도 피드백을 함께 담는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="성 장면과 사용 비용 피드백" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [40초 브랜드 출시 광고](https://x.com/0xashtonx/status/2106421702783914423) (제작자 [@0xashtonx](https://x.com/0xashtonx))

**자신의 브랜드를 짧은 출시 광고의 주제로 사용한다.**

제작자는 자신의 브랜드용 40초 출시 광고를 요청하고 결과 영상을 공유했다. 브랜드 홍보 서사를 생성하는 구체적인 작업 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="40초 브랜드 출시 광고" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [Rocketball 리메이크](https://x.com/atomtanstudio/status/2106418747083022555) (제작자 [@atomtanstudio](https://x.com/atomtanstudio))

**익숙한 게임 리메이크로 코드 자산과 상호작용 기믹을 결합한다.**

작성자는 1980년대 C-64 게임 Rocketball 리메이크를 공유하며 자산이 코드로 제작됐다고 설명했다. 웹사이트 버전 교체는 향후 계획으로 제시한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="Rocketball 리메이크" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [복셀 탑 장면 비교](https://x.com/dropout_layer/status/2106408147309252915) (제작자 [@dropout_layer](https://x.com/dropout_layer))

**동일 장면의 두 결과와 각 실행 비용을 함께 비교한다.**

작성자는 Astra와 Fable의 3D 복셀 탑 결과를 제시하고 비용을 각각 3.50달러와 5.50달러로 보고했다. 비교는 이 두 실행 및 표시된 장면에 한정된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="복셀 탑 장면 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [상상 속 Switch 3 발표](https://x.com/mathisbuilds/status/2106407842240418097) (제작자 [@mathisbuilds](https://x.com/mathisbuilds))

**상상의 제품을 콘셉트 발표와 시연 과제로 사용한다.**

작성자는 가상의 Nintendo Switch 3와 데모를 요청하고 약 4시간 작업했다고 보고했다. 녹화는 실제 제품 사양이 아닌 가상의 차세대 콘솔 콘셉트다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="상상 속 Switch 3 발표" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [랜딩 페이지의 전후 비교](https://x.com/nemumusitocha/status/2106402952307200302) (제작자 [@nemumusitocha](https://x.com/nemumusitocha))

**동일한 랜딩 페이지 지시를 다시 실행해 시간에 따른 변화를 비교한다.**

작성자는 새 랜딩 페이지와 이전에 같은 프롬프트로 만든 페이지를 비교했다. 보이는 전후 디자인은 구체적인 인터페이스 비교 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="랜딩 페이지의 전후 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [상상한 AI의 내면 시점](https://x.com/blueemi99/status/2106397329653719115) (제작자 [@blueemi99](https://x.com/blueemi99))

**상상의 내면 시점을 창작 애니메이션 설정으로 사용한다.**

작성자는 AI 모델이라는 것이 어떤 느낌일지 다룬 영화를 요청하고 한 번에 생성한 결과를 공유했다. 설정은 상상에 기반한 시각적 표현으로 제시한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="상상한 AI의 내면 시점" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Go 가사 모션 디자인](https://x.com/atomtanstudio/status/2106377491267137848) (제작자 [@atomtanstudio](https://x.com/atomtanstudio))

**기존 노래 녹음에 맞춰 제공된 가사를 움직인다.**

제작자는 The Chemical Brothers의 Go 가사 영상을 공유하고 Max 추론을 사용했다고 설명했다. 노래 녹음은 모션 디자인 작업의 외부 오디오 입력이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Go 가사 모션 디자인" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [두 번째 15초 모션 포트폴리오](https://x.com/Saccc_c/status/2106376222309761094) (제작자 [@Saccc_c](https://x.com/Saccc_c))

**자유로운 모션 포트폴리오 지시로 새로운 시각 방향을 탐색한다.**

작성자는 새로운 15초 모션 포트폴리오와 창작 프롬프트를 공유했다. 이전 포트폴리오와 다른 생성 결과임을 명확히 구분했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="두 번째 15초 모션 포트폴리오" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [에이전트 구현 계획 검토](https://x.com/RobIW_dev/status/2106371025852108940) (제작자 [@RobIW_dev](https://x.com/RobIW_dev))

**구상에서 실행으로 넘어가기 전에 시스템 적합성을 검토한다.**

작성자는 시스템 적합성, 구현 계획과 설명 지침을 공유하며 완료 작업의 검토 방식과 다음 구현 내용의 결정 방법을 설명했다. 첨부 이미지는 구체적인 계획 자료를 보존한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="에이전트 구현 계획 검토" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [Claude 마스코트 댄스](https://x.com/ishuagra02/status/2106369929813594134) (제작자 [@ishuagra02](https://x.com/ishuagra02))

**박자에 맞춘 마스코트 동작으로 움직임과 음악의 관계를 시험한다.**

제작자는 Claude 마스코트 댄스를 공유하며 박자에 맞는 애니메이션이라고 설명했다. 같은 원본 영상을 재사용한 게시물은 이 출처에 묶어 중복 작품으로 세지 않는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="Claude 마스코트 댄스" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [인터랙티브 세계 7대 불가사의 섬](https://x.com/notjazii/status/2106368606502334922) (제작자 [@notjazii](https://x.com/notjazii))

**랜드마크 건물을 인터랙티브 섬 장면의 목적지로 사용한다.**

게시자는 랜드마크가 있는 3D 섬 형태의 세계 7대 불가사의 장면을 공유했다. 녹화는 익숙한 유적으로 상호작용 가능한 시각 환경을 구성하는 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="인터랙티브 세계 7대 불가사의 섬" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [Propellerheads 음악 영상](https://x.com/atomtanstudio/status/2106353569603736009) (제작자 [@atomtanstudio](https://x.com/atomtanstudio))

**제공된 사운드트랙을 긴 모션 그래픽의 중심에 둔다.**

제작자는 Propellerheads의 On Her Majesty’s Secret Service를 시각화한 음악 영상을 공유했다. 기존 녹음은 애니메이션 장면의 오디오 입력이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="Propellerheads 음악 영상" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Steamboat Willie 애니메이션 비교](https://x.com/mathisbuilds/status/2106351978691305732) (제작자 [@mathisbuilds](https://x.com/mathisbuilds))

**소리를 켜고 동일한 짧은 장면의 두 표현을 비교한다.**

작성자는 xhigh 설정에서 Fable과 Opus로 표시한 Steamboat Willie 비교를 공유하고 한 번씩 생성했다고 설명했다. 영상은 그 실행의 구체적인 시청각 비교다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Steamboat Willie 애니메이션 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [싼싱두이 주제 영화](https://x.com/hungryturbo/status/2106339115642019904) (제작자 [@hungryturbo](https://x.com/hungryturbo))

**문화·역사 주제로 짧은 애니메이션을 구성한다.**

작성자는 싼싱두이를 다룬 영화를 창작적 시각 서사로 공유했다. 녹화는 역사·문화 주제를 애니메이션 지시로 바꾸는 구체적인 예다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="싼싱두이 주제 영화" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Bugatti Chiron 전후 비교](https://x.com/alannnfx/status/2106323394350461031) (제작자 [@alannnfx](https://x.com/alannnfx))

**이전 자동차 프롬프트를 다시 실행해 모델링과 기능 세부를 비교한다.**

같은 작성자가 예전 실행과 최근 재실행한 Bugatti Chiron 결과를 보여 준다. 전후 녹화는 더 풍부한 모델링과 장면 기능에 초점을 맞춘다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Bugatti Chiron 전후 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [GRAIN 콘셉트 영화](https://x.com/NFT_Chen/status/2106301427052360150) (제작자 [@NFT_Chen](https://x.com/NFT_Chen))

**반복되는 시각 모티프로 추상적인 콘셉트 영화를 구성한다.**

제작자는 씨앗, 곡식, 나무와 산의 이미지를 연결한 GRAIN을 공유했다. 반복되는 형태와 전환이 이 시퀀스의 서사 구조다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="GRAIN 콘셉트 영화" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [Human in Transit 미술 갤러리](https://x.com/exploraX_/status/2106296439936614646) (제작자 [@exploraX_](https://x.com/exploraX_))

**인터랙티브 갤러리 형식으로 역사적 시각 여행을 제시한다.**

게시자는 고대에서 현대 미술 양식으로 이동하는 Human in Transit을 공유했다. 녹화된 인터페이스는 여러 시각적 시대를 하나의 전시에 구성하는 참고 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="Human in Transit 미술 갤러리" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [실크로드 시각 단편](https://x.com/hungryturbo/status/2106294812261695508) (제작자 [@hungryturbo](https://x.com/hungryturbo))

**여행과 역사 주제를 일관된 짧은 영상으로 바꾼다.**

작성자는 실크로드를 주제로 한 영화를 공유했다. 첨부 작품은 역사적 여정을 애니메이션 이미지로 표현한 구체적 창작 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="실크로드 시각 단편" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [네 가지 전환을 다룬 발표 자료](https://x.com/dpkostka/status/2106272731364794757) (제작자 [@dpkostka](https://x.com/dpkostka))

**전환 프레임워크를 발표 자료의 구성 원리로 사용한다.**

작성자는 네 가지 전환 경로를 설명하는 슬라이드를 공유했다. 첨부 이미지는 개념적 프레임워크를 시각 문서로 배열하는 방식을 보여 준다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="네 가지 전환을 다룬 발표 자료" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [이전 대화와 말투 비교](https://x.com/kiyoshi_shin/status/2106268573186637883) (제작자 [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**말투 변화를 살필 때 과거 대화 기록과 현재 응답을 비교한다.**

작성자는 현재 모델에 예전 대화와 지금의 문체를 분석하게 한 뒤 말투 변화에 불만을 표현했다. 첨부 이미지는 그 대화 비교 작업을 기록한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="이전 대화와 말투 비교" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [카카포 귀여움 비교](https://x.com/hanawo_neki/status/2106257409782288659) (제작자 [@hanawo_neki](https://x.com/hanawo_neki))

**명확한 캐릭터 선호 과제로 생성 애니메이션 스타일을 비교한다.**

작성자는 카카포 애니메이션을 공유하며 귀여움 중심의 이번 비교에서는 Opus를 더 좋아한다고 밝혔다. 실제 애니메이션과 부정적 미적 평가를 함께 보존한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="카카포 귀여움 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [만화의 열 시대를 지나는 스파이더맨](https://x.com/chetaslua/status/2106248621519978867) (제작자 [@chetaslua](https://x.com/chetaslua))

**여러 만화 시대를 이동해도 인물의 식별 가능성을 유지한다.**

원 게시자는 열 가지 만화 시대를 통과하는 Spider-Man을 공유했다. 같은 영상을 재사용한 다른 게시물은 추가 작품이 아니라 이 출처에 연결한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="만화의 열 시대를 지나는 스파이더맨" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [일루미나티 소재의 가상 공포 영상](https://x.com/badboyfoxy/status/2106241189976387799) (제작자 [@badboyfoxy](https://x.com/badboyfoxy))

**음모를 소재로 한 공포 지시를 허구적 스토리텔링으로 다룬다.**

작성자는 무서운 일루미나티 영상을 요청하고 결과를 공유했다. 이 주제는 애니메이션의 허구적 공포 설정으로 사용된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="일루미나티 소재의 가상 공포 영상" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [코드로 만든 핵과학사 영화](https://x.com/imjustnewatai/status/2106238699872956427) (제작자 [@imjustnewatai](https://x.com/imjustnewatai))

**과학사 해설에 자체 코드 렌더러와 음악을 결합한다.**

작성자는 핵과학이 원자폭탄을 가능하게 한 과정을 3분짜리 3D 영화로 요청하고, 그린 프레임과 자체 렌더러 및 합성 음악을 보고했다. 사례는 시청각 제작 흐름을 다룬다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="코드로 만든 핵과학사 영화" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [보편적 고소득 개념 해설](https://x.com/markbraincell/status/2106234118514323515) (제작자 [@markbraincell](https://x.com/markbraincell))

**애니메이션 설명으로 경제 개념을 전달한다.**

게시자는 보편적 고소득을 설명하는 애니메이션을 공유했다. 녹화는 개념 해설의 구체적 예이며, 제시된 경제적 주장을 측정된 성과로 바꾸지 않는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="보편적 고소득 개념 해설" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [Altman–Amodei 논쟁 해설](https://x.com/imjustnewatai/status/2106204392588276065) (제작자 [@imjustnewatai](https://x.com/imjustnewatai))

**논쟁을 애니메이션 해설의 서사 구조로 사용한다.**

작성자는 Altman과 Amodei의 논쟁을 애니메이션으로 설명하도록 요청하고 결과를 공유했다. 시사 해설 형식의 사례이며 독립적으로 조사한 역사 기록은 아니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="Altman–Amodei 논쟁 해설" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [Claude 마스코트 음악 영상](https://x.com/synthshareai/status/2106195060140446028) (제작자 [@synthshareai](https://x.com/synthshareai))

**제공된 영상에 마스코트를 겹쳐 캐릭터 중심의 음악 편집을 만든다.**

게시자는 실사 음악 영상 배경에 Claude 마스코트를 겹친 작품을 공유하고 12시간 실행했다고 보고했다. 보이는 표현은 만화 오버레이와 제공된 기존 영상을 결합한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="Claude 마스코트 음악 영상" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [쿼크에서 우주까지 이어지는 줌](https://x.com/imjustnewatai/status/2106190594775097663) (제작자 [@imjustnewatai](https://x.com/imjustnewatai))

**연속 줌으로 과학적 규모를 하나의 시청각 이야기 안에 연결한다.**

작성자는 쿼크에서 우주로 확대하는 장면에 코드 영상과 합성 음악을 사용했다고 보고했다. 녹화는 연속적인 규모 전환과 일관된 시각 서사를 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="쿼크에서 우주까지 이어지는 줌" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [2076년의 세계 상상하기](https://x.com/Layton_Gott/status/2106190496075035096) (제작자 [@Layton_Gott](https://x.com/Layton_Gott))

**미래 세계 장면을 요청할 때 구체적인 길이를 정한다.**

작성자는 25초 영상을 요청하고 2076년을 상상한 단편을 공유했다. 다른 계정이 재사용한 같은 녹화는 이 출처에 연결한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="2076년의 세계 상상하기" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [로어맨해튼 건축 연표](https://x.com/nroze22/status/2106183281293381661) (제작자 [@nroze22](https://x.com/nroze22))

**건축 타임라인 인터페이스에 윤곽, 건축 연도와 높이를 함께 넣는다.**

작성자는 건축 도면 형식의 화면으로 로어맨해튼을 제시하며 건물 연도, 평면 윤곽과 높이를 표시했다. 녹화는 구체적인 인터랙티브 연표 콘셉트다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="로어맨해튼 건축 연표" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [갑골문 애니메이션](https://x.com/MinLiBuilds/status/2106180691344118202) (제작자 [@MinLiBuilds](https://x.com/MinLiBuilds))

**문자의 발전을 역사 애니메이션의 주제로 사용한다.**

작성자는 갑골문에서 시작하는 애니메이션을 공유했다. 녹화는 문자 역사를 중심으로 구성한 시각적 스토리텔링의 구체적 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="갑골문 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [캐릭터가 미술사를 지나는 다른 애니메이션](https://x.com/imjustnewatai/status/2106162924331180510) (제작자 [@imjustnewatai](https://x.com/imjustnewatai))

**역사적 배경이 바뀌어도 익숙한 인물을 계속되는 안내자로 사용한다.**

작성자는 Iron Man과 Spider-Man이 역사를 날아다니도록 요청하고 결과를 공유했다. 다른 작성자의 캐릭터 미술사 실험과는 별도의 작품이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="캐릭터가 미술사를 지나는 다른 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [코드로 만든 세이킬로스 시청각 작품](https://x.com/YanqingCheng/status/2106158746938269728) (제작자 [@YanqingCheng](https://x.com/YanqingCheng))

**역사적 음악 텍스트를 중심으로 단일 파일 시청각 작품을 구성한다.**

작성자는 세이킬로스 비문 작품을 공유하며 HTML과 JavaScript 한 파일로 영상과 음악을 합성했다고 보고했다. 역사적 텍스트가 코드 시청각 시퀀스의 주제다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="코드로 만든 세이킬로스 시청각 작품" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [제트기 애니메이션 비교](https://x.com/Kinzf2121/status/2106158536963330346) (제작자 [@Kinzf2121](https://x.com/Kinzf2121))

**동일한 항공기 과제로 비행 움직임과 카메라 추적을 비교한다.**

작성자는 Fable 5.1로 표시한 결과와 Opus의 제트기 애니메이션을 비교했다. 녹화는 항공기 동작과 영화식 카메라 추적을 살필 구체적 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="제트기 애니메이션 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [모델 자기소개 영화](https://x.com/devteamdrew/status/2106155815707021549) (제작자 [@devteamdrew](https://x.com/devteamdrew))

**자기소개 지시로 모델을 소재로 한 애니메이션을 탐색한다.**

제작자는 한 프롬프트로 자기소개 영상을 요청하고 결과를 공유했다고 보고했다. 모델 주제 서사와 애니메이션 표현을 결합한 작업이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="모델 자기소개 영화" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [종말 이후 카드 게임 프로토타입](https://x.com/maciejkrupowies/status/2106153578029338850) (제작자 [@maciejkrupowies](https://x.com/maciejkrupowies))

**카드 게임의 세계관을 시제품으로 만들고 전투 화면을 살핀다.**

작성자는 한 번에 생성했다는 종말 이후 분위기의 Hearthstone형 프로토타입을 공유했다. 작은 오류를 인정하면서 게임 인터페이스와 상호작용을 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="종말 이후 카드 게임 프로토타입" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [The Late Byte 직장 애니메이션](https://x.com/rohit3a/status/2106138910648914094) (제작자 [@rohit3a](https://x.com/rohit3a))

**모델의 개성을 직장 대화 애니메이션의 인물로 만든다.**

제작자는 Opus를 화난 상사로 묘사한 직장 이야기 The Late Byte를 공유했다. 다른 Day in the Life of Claude 영화와는 별개의 서사다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="The Late Byte 직장 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Queens of the Stone Age 가사 애니메이션](https://x.com/atomtanstudio/status/2106135196483608745) (제작자 [@atomtanstudio](https://x.com/atomtanstudio))

**제공된 노래에 움직이는 글자와 모션 디자인을 결합한다.**

제작자는 Queens of the Stone Age 녹음에 맞춘 키네틱 타이포그래피 음악 영상을 설명했다. 노래는 제공된 오디오 입력이며 사례는 가사와 시각 요소의 배열을 다룬다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Queens of the Stone Age 가사 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [공유된 Three.js 서사 장면](https://x.com/Noreply134882/status/2106116572389478746) (제작자 [@Noreply134882](https://x.com/Noreply134882))

**공유된 3D 이야기 영상을 서사 장면 디자인의 참고로 쓴다.**

게시자는 Three.js 서사 장면을 공유하고 토큰 소비가 크다고 언급했다. 첨부 영상은 3D 스토리텔링의 구체적인 공유 사례로 보존한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="공유된 Three.js 서사 장면" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [역사 속을 지나는 문워크](https://x.com/noclipepe/status/2106105810812112937) (제작자 [@noclipepe](https://x.com/noclipepe))

**춤 모티프를 여러 역사적 배경과 시각 양식에 걸쳐 이어 간다.**

게시자는 공룡 시대에서 달까지 이동하는 Michael Jackson 문워크 영상을 공유했다. 첨부 영화는 춤과 화풍 갤러리의 공유 사례로 남긴다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="역사 속을 지나는 문워크" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [상세 프롬프트 기반 모션 그래픽](https://x.com/devswha/status/2106100273509007802) (제작자 [@devswha](https://x.com/devswha))

**구체적인 창작 지시와 짧은 모션 디자인 요청을 비교한다.**

작성자는 자산, 참고 영상, 소스 파일 없이 상세 프롬프트만 제공했다고 설명하며 모션 그래픽을 공유했다. 결과는 프롬프트 기반 모션 디자인의 구체적인 참고 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="상세 프롬프트 기반 모션 그래픽" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [대여 사업 웹사이트 인터페이스](https://x.com/oalanicolas/status/2106098902965309475) (제작자 [@oalanicolas](https://x.com/oalanicolas))

**대여 사업 지시로 구체적인 웹 인터페이스를 탐색한다.**

제작자는 대여 사업용 웹사이트 화면을 공유했다. 사례는 보이는 페이지 디자인과 사업을 제시하는 방식에 초점을 맞춘다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="대여 사업 웹사이트 인터페이스" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [AGI 소재의 창작 영화](https://x.com/AndrewOnXYZ/status/2106097745098395712) (제작자 [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**반복 사용하는 창작 프롬프트로 서사와 시각 처리를 비교한다.**

작성자는 반복 사용하던 프롬프트로 만든 AGI 주제 애니메이션을 공유했다. 모델 관련 발언은 창작 서사의 일부로 다룬다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="AGI 소재의 창작 영화" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [고양이 곁이야기가 있는 미술사](https://x.com/cherry_mx_reds/status/2106095190285144331) (제작자 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**반복되는 인물로 여러 미술 시대를 짧은 서사에 압축한다.**

제작자는 고양이 곁이야기가 있는 15초 미술사 영상을 공유했다. 15초는 영상 길이를 가리키며, 창작 과제는 여러 역사적 화풍을 아우른다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="고양이 곁이야기가 있는 미술사" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [전투 프로토타입과 복셀 장면](https://x.com/OnlyTerp/status/2106089280502210626) (제작자 [@OnlyTerp](https://x.com/OnlyTerp))

**창작 코딩 작업에서 게임 전투와 세계 구성을 함께 살핀다.**

작성자는 DMC 스타일 전투 프로토타입과 복셀 장면을 공유하고 긴 생성 실행을 설명했다. 게임 기믹과 시각적 세계 설계를 살필 두 가지 구체적 결과다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="전투 프로토타입과 복셀 장면" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [인터넷 밈 연표](https://x.com/chetaslua/status/2106076940558082297) (제작자 [@chetaslua](https://x.com/chetaslua))

**연도별 시각 양식과 음악으로 애니메이션 연표를 구성한다.**

제작자는 2010년부터 2026년까지의 유행 인터넷 밈을 애니메이션으로 공유했다. 각 연도의 화풍과 음악 처리가 코드 서사의 일부가 된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="인터넷 밈 연표" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [한 줄로 만든 입자 움직임](https://x.com/devswha/status/2106072107365114186) (제작자 [@devswha](https://x.com/devswha))

**한 줄 모션 지시로 시작한 뒤 상세한 프롬프트를 다듬는다.**

제작자는 한 줄 프롬프트의 입자 애니메이션을 공유하고 더 자세한 요청을 시도하겠다고 말했다. 긴 모션 디자인 사례와는 별개의 생성 결과다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="한 줄로 만든 입자 움직임" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [Kung-Fu Boy 애니메이션](https://x.com/HashmathRzz/status/2106065773336965510) (제작자 [@HashmathRzz](https://x.com/HashmathRzz))

**무술 캐릭터 지시로 애니메이션 움직임을 탐색한다.**

작성자는 Fable 5.5로 제작했다고 하는 캐릭터 애니메이션 Kung-Fu Boy를 공유했다. 첨부 녹화는 무술 주제의 구체적인 결과를 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="Kung-Fu Boy 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [호르무즈 해협 토론 애니메이션](https://x.com/chetaslua/status/2106060047805792415) (제작자 [@chetaslua](https://x.com/chetaslua))

**토론 주제를 애니메이션 서사로 전환한다.**

제작자는 호르무즈 해협을 다룬 애니메이션 토론을 공개했다. 사례는 보이는 토론 영화만 기록하며 주변 게시물에 언급된 다른 미제시 용도는 포함하지 않는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="호르무즈 해협 토론 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [유니콘 SVG 스타일 실험](https://x.com/atomtanstudio/status/2106057876053918127) (제작자 [@atomtanstudio](https://x.com/atomtanstudio))

**동일한 주제의 그림 과제로 SVG 스타일 선택을 살핀다.**

작성자는 다른 제작자의 시험에서 영감을 받은 유니콘 SVG 실험을 공유했다. 첨부 이미지는 같은 주제의 시각적 처리를 비교할 구체적인 결과다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="유니콘 SVG 스타일 실험" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [핼러윈 계절 애니메이션](https://x.com/cherry_mx_reds/status/2106056643255447590) (제작자 [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**코딩 모델에 계절 주제를 주고 짧은 창작 애니메이션을 만든다.**

제작자는 핼러윈 작품을 요청하고 결과로 나온 계절 애니메이션을 공유했다. 게시물에 이 구체적인 창작 과제의 원본 녹화가 담겼다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="핼러윈 계절 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Blender CLI 야만인과 표지](https://x.com/BoDy051/status/2106047375320166885) (제작자 [@BoDy051](https://x.com/BoDy051))

**Blender CLI 지시로 캐릭터 모델링과 표지 렌더링을 탐색한다.**

작성자는 RPG 야만인 캐릭터와 표지 콘셉트를 Opus 결과와 비교했다. Blender CLI가 제작과 렌더링을 담당하고 모델은 코드 지시를 제공한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Blender CLI 야만인과 표지" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Claude의 하루](https://x.com/ishuagra02/status/2106045364868419727) (제작자 [@ishuagra02](https://x.com/ishuagra02))

**반복 등장하는 마스코트를 중심으로 일상 애니메이션을 만든다.**

원 게시자는 마스코트가 등장하는 Day in the Life of Claude 영화를 공유했다. 이 영상은 별도의 마스코트 댄스 및 그 재게시와 구분된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Claude의 하루" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [3D로 보는 인류 역사](https://x.com/blueemi99/status/2106041578204655748) (제작자 [@blueemi99](https://x.com/blueemi99))

**코드 장면과 애니메이션을 역사적 시각 시퀀스로 결합한다.**

제작자는 고대에서 현재까지의 인류를 다룬 3D 영상을 공유하고 애니메이션과 모델을 코드로 생성했다고 보고했다. 결과는 시각적 스토리텔링 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="3D로 보는 인류 역사" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [빠른 모션 디자인 릴](https://x.com/blueemi99/status/2106031355922387163) (제작자 [@blueemi99](https://x.com/blueemi99))

**짧은 모션 디자인 릴의 속도감, 소리와 일관성을 평가한다.**

작성자는 짧고 빠른 모션 영상을 공유하며 소리와 일관성을 자신의 Opus 결과와 비교했다. 평가는 이 구체적인 작업에 대한 제작자의 경험이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="빠른 모션 디자인 릴" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [자유로운 복합 3D 창작](https://x.com/cocoloba_/status/2106029181607772413) (제작자 [@cocoloba_](https://x.com/cocoloba_))

**열린 창작 요청으로 복잡한 3D 구성을 탐색한다.**

제작자는 여가가 있다면 무엇을 만들겠냐고 물은 뒤 나온 3D 작품을 공유했다. 게시물은 생성된 구성에 여러 개의 분리된 부품이 있다고 설명한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="자유로운 복합 3D 창작" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [막대인간 격투 애니메이션](https://x.com/HelaliBillel/status/2106028502763900944) (제작자 [@HelaliBillel](https://x.com/HelaliBillel))

**구체적인 격투 요청으로 움직임과 타이밍을 살핀다.**

제작자는 막대인간이 싸우는 애니메이션 영상을 요청하고 결과를 공유했다. 첨부 녹화는 이 격투 애니메이션 과제의 구체적인 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="막대인간 격투 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [한 프롬프트로 만든 UI 모션](https://x.com/iancarscadden/status/2106018048792789360) (제작자 [@iancarscadden](https://x.com/iancarscadden))

**하나의 애니메이션 지시로 UI 시퀀스를 탐색한다.**

작성자는 한 번의 요청으로 약 6~7분 만에 완성했다는 UI 모션 시퀀스를 공유했다. 녹화는 그 요청에서 나온 시각적 흐름을 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="한 프롬프트로 만든 UI 모션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [가상의 SCP-8517 애니메이션](https://x.com/eviljoker88/status/2106003621402005816) (제작자 [@eviljoker88](https://x.com/eviljoker88))

**SCP풍 설정을 애니메이션 이야기의 지시로 사용한다.**

제작자는 SCP-8517 주제 애니메이션을 공유하고 제작을 Fable 5.5에 귀속했다. 사례는 허구적 서사와 보이는 애니메이션에 초점을 맞춘다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="가상의 SCP-8517 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [수채화 가을 애니메이션](https://x.com/ishuagra02/status/2106000055706784118) (제작자 [@ishuagra02](https://x.com/ishuagra02))

**애니메이션에 계절 주제와 수채화 표현을 함께 지정한다.**

작성자는 수채화 스타일의 가을 애니메이션을 공유했다. 녹화는 계절 주제를 특정 시각 매체와 결합하는 구체적인 사례를 제공한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="수채화 가을 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [절차적 인형 무대](https://x.com/HelaliBillel/status/2105988689088196785) (제작자 [@HelaliBillel](https://x.com/HelaliBillel))

**무대 장면 속 인형 같은 캐릭터의 움직임을 살핀다.**

작성자는 절차적 인형 무대 애니메이션을 공유하고 관련 논의에서 Blender를 언급했다. 사례는 눈에 보이는 무대 캐릭터와 움직임을 다룬다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="절차적 인형 무대" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [브라우저로 렌더링한 펠리컨](https://x.com/slimcat0101/status/2105988654636380444) (제작자 [@slimcat0101](https://x.com/slimcat0101))

**캐릭터 동작 결과를 브라우저에서 실행하고 렌더링 장면을 살핀다.**

제작자는 자전거 타는 펠리컨을 요청하고 생성된 HTML을 브라우저에서 실행하는 모습을 녹화했다. 정적인 SVG 그림 시험과는 별개의 움직이는 장면이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="브라우저로 렌더링한 펠리컨" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [우주가 자신을 바라보다](https://x.com/l_mejiaC/status/2105988529671360673) (제작자 [@l_mejiaC](https://x.com/l_mejiaC))

**연속적인 시각 여행으로 먼 규모들을 하나의 서사에 연결한다.**

제작자는 빅뱅에서 인간의 눈까지 이어지는 시퀀스를 공개했다. 영상과 음악은 영화를 위해 실행 시 코드로 제작했다고 설명한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="우주가 자신을 바라보다" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [독립적인 제트기 애니메이션 시험](https://x.com/AI_Screening/status/2105988448612135176) (제작자 [@AI_Screening](https://x.com/AI_Screening))

**항공기 애니메이션 과제를 반복해 해당 결과를 살핀다.**

작성자는 라우팅 관련 논의를 본 뒤 제트기 애니메이션을 시도하고 결과를 공유했다. 이 녹화는 해당 항공기 사례의 독립적인 출처다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="독립적인 제트기 애니메이션 시험" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [초기 자유형 모션 릴](https://x.com/Saccc_c/status/2105985484472377531) (제작자 [@Saccc_c](https://x.com/Saccc_c))

**짧고 열린 프롬프트로 모션 디자인을 탐색한다.**

제작자는 한 프롬프트로 생성했다는 초기 모션 디자인 릴을 공유했다. 이후 15초 포트폴리오와는 별개인 이전 결과다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="초기 자유형 모션 릴" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [코드로 표현한 문명사](https://x.com/ziwenxu_/status/2105983571848741045) (제작자 [@ziwenxu_](https://x.com/ziwenxu_))

**문명사 지시를 코드 기반 애니메이션 서사로 바꾼다.**

작성자는 문명의 시작부터 현재까지를 요청하고 영화를 공유했다. 이 코드 시각 표현에 기존 영상이나 스톡 자산을 사용하지 않았다고 보고했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="코드로 표현한 문명사" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [칩에서 서버까지 확대 비교](https://x.com/SPAC89/status/2105968361725202591) (제작자 [@SPAC89](https://x.com/SPAC89))

**칩에서 서버로 확대하는 장면의 사실감과 연속성을 비교한다.**

작성자는 Fable XHigh와 GPT Sol Ultra의 사실적인 줌 시퀀스를 비교하고 속도와 사용 한도를 논했다. 서로 다른 구독 등급에서 수행한 구체적 실행의 비교다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="칩에서 서버까지 확대 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [달 여행 개인 애니메이션 프로젝트](https://x.com/IgorGomezC/status/2105963552024506565) (제작자 [@IgorGomezC](https://x.com/IgorGomezC))

**여러 코딩 모델로 개인적인 애니메이션 콘셉트를 탐색한다.**

제작자는 Fable과 Opus 실험을 이야기하며 개인 달 여행 애니메이션 프로젝트를 공유했다. 첨부 작품이 그 창작 탐색의 구체적 결과다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="달 여행 개인 애니메이션 프로젝트" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [일본풍 복셀 장면 비교](https://x.com/vikktorrrre/status/2105955048018588084) (제작자 [@vikktorrrre](https://x.com/vikktorrrre))

**동일 장면 프롬프트로 세부, 안개와 선명도를 비교한다.**

작성자는 같은 일본풍 복셀 장면 프롬프트로 현재 Fable과 Opus 결과를 비교했다. 관찰은 해당 결과의 선명도, 안개와 미적 표현을 다룬다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="일본풍 복셀 장면 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [Steaming the Frontier 시청각 단편](https://x.com/sdmat123/status/2105929299878703520) (제작자 [@sdmat123](https://x.com/sdmat123))

**Steamboat풍 시각 지시에 소리를 결합해 단편을 만든다.**

제작자는 소리가 있는 애니메이션 Steaming the Frontier를 공유했다. 다른 제작자의 독립적인 Steamboat풍 출력과는 별도 출처로 유지한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="Steaming the Frontier 시청각 단편" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [여러 미술 양식을 통과하는 슈퍼맨](https://x.com/Mr_Salio/status/2105925979466052051) (제작자 [@Mr_Salio](https://x.com/Mr_Salio))

**한 인물이 연속 애니메이션에서 변화하는 화풍을 지나게 한다.**

제작자는 앞선 슈퍼맨 사례에서 영감을 받아 새로 생성한 자신의 결과를 공유했다고 설명했다. 다른 그림을 가진 별개 창작으로, 재게시는 아니다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="여러 미술 양식을 통과하는 슈퍼맨" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Cupcake풍 보스전 프로토타입](https://x.com/maciejkrupowies/status/2105914965387321785) (제작자 [@maciejkrupowies](https://x.com/maciejkrupowies))

**횡스크롤 보스전을 시제품으로 만들고 전투를 살핀다.**

작성자는 Cupcake풍 보스전 프로토타입을 공유하고 10분 안에 한 번으로 생성했다고 보고했다. 첨부 녹화는 게임 전투 시퀀스를 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Cupcake풍 보스전 프로토타입" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [태양 위치가 달라지는 범선](https://x.com/popat_kunj/status/2105907935490752822) (제작자 [@popat_kunj](https://x.com/popat_kunj))

**항해 장면으로 하늘, 물과 태양 위치 변화를 탐색한다.**

제작자는 태양이 다른 위치에 있는 3D 범선 장면과 인터랙티브 작품 링크를 공유했다. 한 시각 과제에 배, 하늘과 물을 결합한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="태양 위치가 달라지는 범선" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Paracortex와 Pi 변경 안내 영상](https://x.com/RobIW_dev/status/2105894547796476225) (제작자 [@RobIW_dev](https://x.com/RobIW_dev))

**제품 업데이트를 짧은 모션 디자인 공지로 바꾼다.**

작성자는 Paracortex와 Pi 업데이트를 25초 모션 디자인 영상으로 바꾸고 게시물에 프롬프트를 제공했다. 시각적인 제품 커뮤니케이션 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Paracortex와 Pi 변경 안내 영상" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Curio 2.0 사이트 홍보 영상](https://x.com/voltwake/status/2105884775982485642) (제작자 [@voltwake](https://x.com/voltwake))

**기존 웹사이트 공개를 중심으로 코드 홍보 영화를 만든다.**

제작자는 Curio 2.0 출시 홍보에 코드 영상, 카메라 연출과 음악을 결합했다고 설명했다. 게시물에 완성된 웹사이트 홍보 영화가 담겼다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Curio 2.0 사이트 홍보 영상" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [상상 속 Hugging Face 3D 이야기](https://x.com/chetaslua/status/2105884276864782557) (제작자 [@chetaslua](https://x.com/chetaslua))

**모델 코드와 렌더링·오디오 도구를 결합해 가상 영화를 만든다.**

제작자는 모델 코드, Blender와 ElevenLabs API로 만든 상상의 Hugging Face 이야기를 공유했다. Blender는 제작·렌더링을, ElevenLabs는 외부 오디오를 담당한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="상상 속 Hugging Face 3D 이야기" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [Claude for Chrome의 JS Paint 사용](https://x.com/BtwIUseSystemd/status/2105861662112923849) (제작자 [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**브라우저 에이전트에게 앱 자체 도구만 사용하는 그림 과제를 준다.**

작성자는 Claude for Chrome에 JS Paint 도구만으로 사람을 그리도록 요청하고 결과를 공유했다. 브라우저 조작과 그림 앱은 명시적인 과제 요소다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="Claude for Chrome의 JS Paint 사용" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [정적인 펠리컨 자전거 SVG](https://x.com/olddonkeyblog/status/2105842745189556672) (제작자 [@olddonkeyblog](https://x.com/olddonkeyblog))

**자체 완결형 SVG 요청으로 세밀한 정적 그림을 시험한다.**

제작자는 자전거 타는 펠리컨을 하나의 자체 완결 SVG로 요청하고 정적 이미지를 공유했다. 움직이는 자전거 사례와는 별개의 그림 과제다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="정적인 펠리컨 자전거 SVG" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [BlockBench MCP와 Minecraft 스킬](https://x.com/TOPSTR1X/status/2105839618872738138) (제작자 [@TOPSTR1X](https://x.com/TOPSTR1X))

**게임 캐릭터 생성에 모델링 도구와 스타일 스킬을 제공한다.**

작성자는 BlockBench MCP와 맞춤형 Minecraft 모델링·채색 스킬을 제공한 뒤 캐릭터를 공유했다. 도구와 스타일 안내는 작업의 명시적 입력이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="BlockBench MCP와 Minecraft 스킬" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [하나의 HTML 파일로 만든 Dig Dug](https://x.com/imjustnewatai/status/2105831117677084841) (제작자 [@imjustnewatai](https://x.com/imjustnewatai))

**소형 브라우저 게임을 재현할 때 단일 HTML을 납품 목표로 정한다.**

제작자는 하나의 HTML 파일로 Dig Dug를 재현하도록 요청하고 게임 녹화를 공유했다. 게시물은 한 프롬프트로 제작했다고 설명한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="하나의 HTML 파일로 만든 Dig Dug" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [기계식 문어 SVG](https://x.com/SEO/status/2105812236774297943) (제작자 [@SEO](https://x.com/SEO))

**기계 생물로 SVG 디자인의 세부와 움직임을 살핀다.**

작성자는 기계적 세부가 있는 문어 SVG 애니메이션을 공유했다. 녹화는 작은 움직이는 부품에 초점을 맞춘 벡터 디자인의 구체적인 예다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="기계식 문어 SVG" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [미술 양식을 지나는 Humanity Walks](https://x.com/l_mejiaC/status/2105801379956850793) (제작자 [@l_mejiaC](https://x.com/l_mejiaC))

**같은 인물이 여러 역사적 미술 양식을 연속해서 지나게 한다.**

원 제작자는 약 74초 동안 20개 미술 패널을 걷는 연속 영상을 공유하고 코드 음악을 보고했다. 경계를 지날 때마다 캐릭터와 장면의 양식이 바뀐다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="미술 양식을 지나는 Humanity Walks" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [열린 요청으로 만든 블랙홀](https://x.com/rohit3a/status/2105786053412208835) (제작자 [@rohit3a](https://x.com/rohit3a))

**열린 창작 지시로 블랙홀 시각화를 탐색한다.**

제작자는 자신을 놀라게 한다면 무엇을 만들겠냐고 묻고 블랙홀 장면을 공유했다. 정해진 인터페이스 구현이 아닌 자유로운 시각적 탐색 과제다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="열린 요청으로 만든 블랙홀" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [오로라 해파리 애니메이션 비교](https://x.com/SPAC89/status/2105783511433318451) (제작자 [@SPAC89](https://x.com/SPAC89))

**두 해파리 영상의 변형과 움직임을 비교한다.**

작성자는 Fable XHigh와 GPT Sol Ultra의 오로라 해파리 애니메이션을 비교하고 사용 한도를 논했다. 결과는 서로 다른 구독 등급에서 나온 것이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="오로라 해파리 애니메이션 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Nintendo Switch 결합과 부팅 SVG](https://x.com/ishuagra02/status/2105779174921359470) (제작자 [@ishuagra02](https://x.com/ishuagra02))

**한 SVG 애니메이션에 컨트롤러 결합과 부팅을 함께 담는다.**

제작자는 컨트롤러가 끼워진 뒤 부팅 로고가 움직이는 Nintendo Switch SVG를 공유했다. 게시물은 해당 실행에 1분 39초와 1.34달러가 들었다고 보고한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Nintendo Switch 결합과 부팅 SVG" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [The Loom 인터랙티브 3D 장면](https://x.com/Mr_Salio/status/2105774088492916757) (제작자 [@Mr_Salio](https://x.com/Mr_Salio))

**풍경과 건물을 하나의 인터랙티브 3D 페이지로 구성한다.**

작성자는 건물과 풍경이 있는 인터랙티브 장면 The Loom을 소개했다. 첨부 녹화는 제작자의 시험에서 나온 구체적인 페이지 결과다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="The Loom 인터랙티브 3D 장면" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [벚꽃 탑 모션 샘플](https://x.com/mesmerlord/status/2105758042830549235) (제작자 [@mesmerlord](https://x.com/mesmerlord))

**동일 지시의 장면에서 시각적 초점과 박자 동기화를 비교한다.**

작성자는 같은 프롬프트로 만든 초기 벚꽃 탑 모션 샘플 두 개를 공유하며 초점과 박자 동기화를 언급했다. 관찰은 제작자의 구체적인 결과에 관한 것이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="벚꽃 탑 모션 샘플" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [깔끔하지만 깊이가 부족한 풍경](https://x.com/eviljoker88/status/2105755840175034447) (제작자 [@eviljoker88](https://x.com/eviljoker88))

**생성 장면 비교에서 부정적인 미적 피드백도 보존한다.**

작성자는 일본풍 장면을 나란히 공유하며 다른 결과가 더 깔끔한데도 Opus의 깊이 표현을 더 좋아한다고 밝혔다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="깔끔하지만 깊이가 부족한 풍경" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [평가가 엇갈린 일본풍 장면](https://x.com/eviljoker88/status/2105755408342126936) (제작자 [@eviljoker88](https://x.com/eviljoker88))

**첫 비교를 명확한 승패로 단정하지 말고 혼합된 반응을 기록한다.**

작성자는 첫 일본풍 장면 비교를 공유하며 결과가 혼재한다고 설명했다. 첨부 이미지는 그 미적 반응의 근거가 되는 구체적인 출력을 보존한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="평가가 엇갈린 일본풍 장면" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [컨트롤러 SVG 비교](https://x.com/notjazii/status/2105751542498464169) (제작자 [@notjazii](https://x.com/notjazii))

**비슷한 시각 과제에서 컨트롤러 그림의 전후를 비교한다.**

작성자는 비교 이미지로 이전과 이후의 컨트롤러 SVG 결과를 공유했다. 사례는 일반적인 모델 순위가 아니라 보이는 그림과 표현의 변화를 다룬다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="컨트롤러 SVG 비교" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [산업 장치 3D 장면](https://x.com/RayaneRachid_/status/2105744517735354410) (제작자 [@RayaneRachid_](https://x.com/RayaneRachid_))

**기계 장치를 집중된 3D 장면 설계 과제로 사용한다.**

제작자는 3D 산업 장치 장면을 공유하며 자신의 최고 단일 생성 결과라고 설명했다. 첨부 이미지는 기계적 구성의 구체적인 참고 사례다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="산업 장치 3D 장면" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [거대한 껍질 아가미 벌레 재구성](https://x.com/Josh67Joshua/status/2105739832563769697) (제작자 [@Josh67Joshua](https://x.com/Josh67Joshua))

**구체적인 생물 묘사로 두 프롬프트 재구성을 탐색한다.**

작성자는 거대한 껍질 아가미 벌레 그림을 공유하고 두 프롬프트로 완성했다고 보고했다. 이미지는 해당 생물 디자인 과제의 보이는 결과다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="거대한 껍질 아가미 벌레 재구성" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [두 프롬프트로 그린 GameCube 컨트롤러](https://x.com/marmaduke091/status/2105735266032095349) (제작자 [@marmaduke091](https://x.com/marmaduke091))

**익숙한 컨트롤러로 두 차례 지시의 그림 결과를 살핀다.**

작성자는 GameCube 컨트롤러 그림을 공유하고 두 프롬프트를 썼다고 보고했다. 이 정적 이미지는 Xbox 및 다른 컨트롤러 시연과 구분된다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="두 프롬프트로 그린 GameCube 컨트롤러" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [X 게시물용 스크린샷 편집](https://x.com/chetaslua/status/2105733677003292983) (제작자 [@chetaslua](https://x.com/chetaslua))

**보조 도구가 스크린샷을 소셜 게시물에 맞추는 방식을 살핀다.**

제작자는 X 게시물용 스크린샷 편집을 공유하며 명시적 요청 없이 도구가 편집했다고 말했다. 첨부 이미지는 눈에 보이는 결과다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="X 게시물용 스크린샷 편집" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [복셀 벚꽃 장면 전후 비교](https://x.com/kdnbmb/status/2105704791049412755) (제작자 [@kdnbmb](https://x.com/kdnbmb))

**동일한 시각 주제에서 연속된 복셀 장면 출력을 비교한다.**

게시자는 복셀 벚꽃 섬의 두 버전을 공유했다. 나란한 이미지에 장면의 전후 디자인 차이가 기록되어 있다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="복셀 벚꽃 장면 전후 비교" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [SHADERKIN 천 인터페이스 프로토타입](https://x.com/mszzz0011/status/2106025576972853642) (제작자 [@mszzz0011](https://x.com/mszzz0011))

**인터페이스 시제품에서 천 효과와 조절 가능한 항목을 함께 탐색한다.**

작성자는 천 효과와 매개변수 컨트롤이 있는 SHADERKIN 프로토타입을 공유하고 한 번에 생성했다고 설명했다. 녹화는 완성된 화면과 움직임을 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="SHADERKIN 천 인터페이스 프로토타입" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [공유된 금빛 시계 인터페이스 애니메이션](https://x.com/AISuperDomain/status/2106396754539360272) (제작자 [@AISuperDomain](https://x.com/AISuperDomain))

**시계 주제 애니메이션을 인터페이스 구성의 참고로 사용한다.**

게시자는 금빛 시계 주제의 프런트엔드 애니메이션을 공유했다. 첨부 영상은 화면 구성, 시계 모티프와 움직이는 시각 표현을 살피는 공유 참고 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="공유된 금빛 시계 인터페이스 애니메이션" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [Before There Was Anything 서사](https://x.com/crowqnt/status/2106146218846081435) (제작자 [@crowqnt](https://x.com/crowqnt))

**공유된 애니메이션으로 우주와 인류의 이야기를 탐색한다.**

게시자는 우주와 인류를 다룬 Before There Was Anything을 공유했다. 첨부 영화는 시각적 스토리텔링의 공유 사례로 보존한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="Before There Was Anything 서사" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [공유된 푸른 입자 소용돌이](https://x.com/AISuperDomain/status/2105846981776003107) (제작자 [@AISuperDomain](https://x.com/AISuperDomain))

**공유된 소용돌이 시각화에서 입자 움직임과 구성을 살핀다.**

게시자는 푸른 입자의 소용돌이 애니메이션을 공유했다. 첨부 영상은 입자 운동, 시각 구조와 구성을 살필 구체적인 공유 사례다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="공유된 푸른 입자 소용돌이" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [두 차례 수정한 다중 패널 화면](https://x.com/ZorroOfMorocco/status/2106547078235095485) (제작자 [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**첫 출력에서 멈추지 말고 수정 반복으로 시각 인터페이스를 다듬는다.**

작성자는 완성된 다중 패널 인터페이스를 공유하고 약 3시간 작업과 두 차례 수정을 보고했다. 첨부 스크린샷은 최종 시각 디자인을 보여 준다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="두 차례 수정한 다중 패널 화면" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [동물을 쌓은 렌더링 장면](https://x.com/legit_api/status/2117237103289315574) (제작자 [@legit_api](https://x.com/legit_api))

**정적인 구성에서 여러 캐릭터와 재질의 균형을 살핀다.**

게시물은 곰, 판다와 북극곰을 쌓은 장면을 공유하고 Discord의 yuruzuu를 출처로 밝히며 21분 실행을 보고한다. 공개 게시물을 공유된 시각적 출처로 보존한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="동물을 쌓은 렌더링 장면" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [네 가지 오픈월드 RPG 시도 비교](https://x.com/noclipepe/status/2117222592536789149) (제작자 [@noclipepe](https://x.com/noclipepe))

**동일한 창작 과제에서 게임 표현, 전투와 충돌 동작을 비교한다.**

제작자는 Fable 5.5, GPT-6.2 Astra, Opus 5.5와 Fable 5.1로 표시한 단일 프롬프트 RPG 네 개를 제시했다. 조명, 전투, 인벤토리, 충돌과 캐릭터가 끼는 현상을 비교한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="네 가지 오픈월드 RPG 시도 비교" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [두 프런트엔드 애니메이션 비교](https://x.com/leo114119/status/2117209849842761983) (제작자 [@leo114119](https://x.com/leo114119))

**애니메이션을 함께 보며 장면 설계와 시각적 세부를 비교한다.**

게시물은 Astra와 Fable로 표시한 코드 생성 애니메이션을 나란히 놓고 세부와 대본 설계에 주목한다. Fable 애니메이션은 @chetaslua의 작품이라고 명시한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="두 프런트엔드 애니메이션 비교" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [코드로 생성한 이끼 로봇 영화](https://x.com/chetaslua/status/2117169796290916732) (제작자 [@chetaslua](https://x.com/chetaslua))

**애니메이션 지시로 코드가 구성한 완전한 영화 장면을 탐색한다.**

제작자는 숲과 로봇의 애니메이션을 공유하고 한 번에 생성한 코드 영화라고 설명했다. 스크린샷에 있는 프롬프트를 안내하며 다른 시도와 비교한다.

추가 게시물에는 별도로 보고된 Opus 5.5 대조 실행이 담겨 있다. [@AnikaCodes](https://x.com/AnikaCodes) · [관련 작업](https://x.com/AnikaCodes/status/2117222374642946297)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="코드로 생성한 이끼 로봇 영화" width="760"></a></td><td valign="top"><p>추가 게시물에는 별도로 보고된 Opus 5.5 대조 실행이 담겨 있다.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="코드로 생성한 이끼 로봇 영화" width="760"></a></td></tr></table>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [다시 만든 컨테이너 항구 시뮬레이션](https://x.com/anxuanng/status/2117124831279972812) (제작자 [@anxuanng](https://x.com/anxuanng))

**이전 장면을 다시 만들 때 시각 비교를 위해 프로젝트 맥락을 보존한다.**

작성자는 다른 컨테이너 항구 장면을 올리며 이전 Blender·Three.js 시뮬레이션을 인용했다. 기존 작업은 전략 게임 같은 환경을 위해 크레인, 배, 차량과 컨테이너를 모델링했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="다시 만든 컨테이너 항구 시뮬레이션" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [다시 만든 공항 계류장 장면](https://x.com/anxuanng/status/2117096574878921119) (제작자 [@anxuanng](https://x.com/anxuanng))

**수정한 공항 장면을 이전 프로젝트와 자산 제작 흐름에 맞춰 비교한다.**

작성자는 공항 계류장 장면으로 돌아와 이전 Blender·Three.js 시뮬레이션을 인용했다. 비행기, 지원 차량과 터미널 시설이 있는 새 영상을 공유한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="다시 만든 공항 계류장 장면" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [추상 3D 세계를 지나는 펠리컨](https://x.com/xiax0603/status/2116960224829665543) (제작자 [@xiax0603](https://x.com/xiax0603))

**자전거 소재로 서로 다른 공간 사이의 전환을 살핀다.**

게시물은 기하학 조각과 추상 디지털 환경을 지나 눈을 통해 멀어지는 펠리컨·자전거 애니메이션을 공유한다. 독특한 장면 전환 시연을 제공한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="추상 3D 세계를 지나는 펠리컨" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [역사적 범선 장면](https://x.com/abhinavflac/status/2116945827738665060) (제작자 [@abhinavflac](https://x.com/abhinavflac))

**배 장면의 물, 조명과 환경 구성을 살핀다.**

게시물은 역사적 범선 장면을 공유하며 인터랙티브한 제로샷 결과라고 설명한다. 첨부 녹화는 선박과 주변 수면의 구체적인 시각 샘플이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="역사적 범선 장면" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [Carbon과 자전거·보행 움직임 비교](https://x.com/AI_Screening/status/2116934172757660014) (제작자 [@AI_Screening](https://x.com/AI_Screening))

**짝지은 시각 결과로 캐릭터 움직임과 장면 구성을 비교한다.**

작성자는 Fable과 Carbon으로 표시한 자전거와 얼룩말 사례를 합성 영상에 넣었다. 체크포인트가 비슷하다는 평가와 함께 움직임을 살필 구체적인 영상을 제공한다.

이전에 따로 공개된 자전거 타는 인물 비교도 합성 영상과 함께 수록했다. [@AI_Screening](https://x.com/AI_Screening) · [관련 작업](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="Carbon과 자전거·보행 움직임 비교" width="760"></a></td><td valign="top"><p>이전에 따로 공개된 자전거 타는 인물 비교도 합성 영상과 함께 수록했다.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="Carbon과 자전거·보행 움직임 비교" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [청량음료 병 제품 표현](https://x.com/abhinavflac/status/2116919086521499730) (제작자 [@abhinavflac](https://x.com/abhinavflac))

**짧은 제품 렌더링 영상으로 재질, 형태와 연출을 살핀다.**

게시물은 청량음료 병 영상을 공유하고 단일 생성 라우팅 결과라고 설명한다. 사례는 보이는 병 영상을 유지하며 설명의 일관되지 않은 브랜드명은 채택하지 않는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="청량음료 병 제품 표현" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [Astra와 펠리컨 움직임 비교](https://x.com/Octoberry/status/2116918967558095131) (제작자 [@Octoberry](https://x.com/Octoberry))

**짝지은 펠리컨 영상으로 사실감, 색상과 움직임을 비교한다.**

게시자는 Fable과 Astra 라벨의 펠리컨 장면을 나란히 놓고 사실감과 색상을 언급했다. 비교 녹화는 두 시각적 표현을 함께 유지한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="Astra와 펠리컨 움직임 비교" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [코드 애니메이션 모션 디자인 지시](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (제작자 [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**움직이는 제목이나 제품 인트로를 요청할 때 구체적 디자인 지시로 시작한다.**

게시물은 인트로, 애니메이션 로고, 제목과 3D 장면을 위한 모션 지시 스크린샷을 공유하고 Claude에 적용할 것을 제안한다. 출처 이미지에 지시가 남아 있다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="코드 애니메이션 모션 디자인 지시" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [사진을 참고한 복셀 초상](https://x.com/chetaslua/status/2116912822806520027) (제작자 [@chetaslua](https://x.com/chetaslua))

**복셀 초상이 참조 사진의 알아볼 수 있는 특징을 어떻게 보존하는지 본다.**

제작자는 Sam Altman 사진과 복셀 스타일 초상을 함께 제시하고 한 번에 생성한 결과라고 설명했다. 나란한 이미지에 참조와 변환 결과가 모두 있다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="사진을 참고한 복셀 초상" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [Opus와 날아가는 펠리컨 장면 비교](https://x.com/leo114119/status/2116901575490929109) (제작자 [@leo114119](https://x.com/leo114119))

**재미있는 물체 배치로 구성과 애니메이션 선택을 비교한다.**

게시물은 Fable과 Opus 라벨의 날아가는 펠리컨 위 자전거 영상을 위아래로 놓았다. Fable 영상은 @notjazii를 출처로 밝히며 두 표현을 함께 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="Opus와 날아가는 펠리컨 장면 비교" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [Morning Ride 펠리컨 웹 장면](https://x.com/leo114119/status/2116893571739775220) (제작자 [@leo114119](https://x.com/leo114119))

**해변 자전거 장면에서 캐릭터 세부와 주변 페이지 표현을 살핀다.**

작성자는 Morning Ride 페이지 안의 3D 펠리컨 자전거 장면을 공유하고 깃털, 발, 자전거 세부와 해변 배경을 강조했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="Morning Ride 펠리컨 웹 장면" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [같은 프롬프트와 서로 다른 화풍](https://x.com/notjazii/status/2116893197939224714) (제작자 [@notjazii](https://x.com/notjazii))

**각 모델이 화풍을 고르게 한 뒤 완성된 장면 구성을 비교한다.**

작성자는 두 모델에 같은 프롬프트를 주되 각자 시각 스타일을 선택하게 했다고 보고했다. 영상은 다른 장면 구성과 세부 수준을 나란히 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="같은 프롬프트와 서로 다른 화풍" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [펠리컨과 자전거, 말의 구성](https://x.com/abhinavflac/status/2116881397986288017) (제작자 [@abhinavflac](https://x.com/abhinavflac))

**한 장면에서 여러 상호작용 대상을 배치하는 방식을 시험한다.**

게시물은 자전거를 동반해 날아가는 펠리컨 아래로 말이 달리는 애니메이션을 공유한다. 첨부 영상은 특이한 다중 대상 구성과 움직임의 구체적인 샘플이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="펠리컨과 자전거, 말의 구성" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [참조 게시물 기반 등각 장면](https://x.com/chetaslua/status/2116878661035106515) (제작자 [@chetaslua](https://x.com/chetaslua))

**일반적인 예시 대신 제공된 게시물을 참고해 새 장면을 구성한다.**

제작자는 인용한 Post Humans 게시물만 참고했다고 보고하며 등각 장면을 공유했다. 영상에는 계절 조절 기능이 있는 농장 형태의 구성이 담겼다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="참조 게시물 기반 등각 장면" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [펠리컨 자전거 기계부 접사](https://x.com/NFT_Chen/status/2116869725703782507) (제작자 [@NFT_Chen](https://x.com/NFT_Chen))

**체인링 움직임, 깃털 세부와 자전거 주변 카메라 동작을 살핀다.**

게시물은 물가에서 자전거를 타는 펠리컨 접사를 공유한다. 녹화는 자전거 기계부, 새의 머리와 넓은 산책로 주행 장면을 오간다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="펠리컨 자전거 기계부 접사" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [펠리컨 위에 올라탄 자전거](https://x.com/notjazii/status/2116861637890379891) (제작자 [@notjazii](https://x.com/notjazii))

**익숙한 주체 관계를 뒤집어 애니메이션의 공간 구성을 시험한다.**

제작자는 펠리컨 위 자전거 애니메이션을 공유했다. 날아가는 새 위에 자전거를 놓아, 익숙한 자전거 타는 펠리컨 과제를 변형했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="펠리컨 위에 올라탄 자전거" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [Carbon과 펠리컨 SVG 화풍 비교](https://x.com/leo114119/status/2116652334734332212) (제작자 [@leo114119](https://x.com/leo114119))

**사실성과 삽화 스타일을 비교하되 미적 차이를 보편적 순위로 보지 않는다.**

게시물은 Carbon과 Fable의 펠리컨 자전거 결과를 함께 제시한다. 작성자는 만화식 렌더와 사실적 표현을 대비하며 화풍 차이가 비교를 어렵게 한다고 밝혔다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="Carbon과 펠리컨 SVG 화풍 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [파란 만화 새의 자전거 장면](https://x.com/birdabo/status/2116553049183560012) (제작자 [@birdabo](https://x.com/birdabo))

**익숙한 만화 캐릭터가 자전거 구성에 표현되는 방식을 살핀다.**

게시물은 물가에서 자전거를 타는 파란 만화 새를 Fable 5.5 Max라는 설명과 함께 공유한다. 이미지는 구체적인 정적 시각 샘플로 보존한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="파란 만화 새의 자전거 장면" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [숲길의 펠리컨 자전거 스크린샷](https://x.com/leo114119/status/2116154940364374269) (제작자 [@leo114119](https://x.com/leo114119))

**브라우저 자전거 장면의 깃털, 발과 기하 구조를 살핀다.**

게시자는 숲길을 자전거로 달리는 펠리컨의 브라우저 스크린샷을 공유하며 깃털 질감, 발과 자전거 세부를 강조했다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="숲길의 펠리컨 자전거 스크린샷" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [Carbon과 막대인간 전투 비교](https://x.com/leo114119/status/2116084152986656933) (제작자 [@leo114119](https://x.com/leo114119))

**짝지은 애니메이션의 전투 안무와 움직임을 비교한다.**

비교 녹화에는 Fable 5.1 High와 Carbon 라벨이 있다. 작성자는 막대인간 격투 애니메이션의 상대적 품질을 논한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="Carbon과 막대인간 전투 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [초기 시험의 펠리컨 SVG 참조](https://x.com/ChrisGPT/status/2115872567122608591) (제작자 [@ChrisGPT](https://x.com/ChrisGPT))

**스타일과 자전거 구조를 볼 때 출처가 연결된 참조를 유지한다.**

게시자는 펠리컨 자전거 이미지를 강조하며 Discord의 kostikz를 결과 출처로 밝힌 초기 시험 게시물을 인용했다. 참조 이미지와 출처 연결을 함께 보존한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="초기 시험의 펠리컨 SVG 참조" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [모델 간 SVG 시험의 펠리컨 참조](https://x.com/AdamHoltererer/status/2115858542221492300) (제작자 [@AdamHoltererer](https://x.com/AdamHoltererer))

**Fable 참조를 주변 SVG 시험 맥락과 함께 유지한다.**

게시자는 자신의 Mistral Large 4 SVG 시험 스레드 아래에 펠리컨 자전거 이미지를 Fable 참고로 추가했다. 모델 간 관찰에 출처가 연결된 시각 자료를 제공한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="모델 간 SVG 시험의 펠리컨 참조" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [Carbon과 자전거 SVG 세부 비교](https://x.com/insanekrishnaa/status/2115833723342250186) (제작자 [@insanekrishnaa](https://x.com/insanekrishnaa))

**바구니, 배경과 깃털 질감 같은 개별 시각 요소를 비교한다.**

게시물은 Fable과 Carbon의 펠리컨 자전거 그림을 비교하며 바구니 디자인, 배경과 깃털 질감을 논한다. 광범위한 과제 모음이 아닌 구체적인 시각 리뷰다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="Carbon과 자전거 SVG 세부 비교" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [협곡 속 3D 정착지](https://x.com/Mr_Salio/status/2115813400915714177) (제작자 [@Mr_Salio](https://x.com/Mr_Salio))

**정착지 장면으로 환경 세부와 공간 구성을 살핀다.**

게시물은 넓은 협곡 정착지를 공유하고 새 Claude 체크포인트 시연으로 소개한다. 녹화는 눈에 보이는 건물, 풍경과 장면 구성을 제공한다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="협곡 속 3D 정착지" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [Opus와 컨트롤러 세부 비교](https://x.com/notjazii/status/2115808169075351632) (제작자 [@notjazii](https://x.com/notjazii))

**짝지은 컨트롤러 그림의 형태, 조작부와 세부 수준을 살핀다.**

작성자는 Fable과 Opus 라벨의 컨트롤러 그림을 함께 올리며 위쪽 결과의 많은 세부를 강조했다. 짝지은 이미지가 해당 비교를 보존한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="Opus와 컨트롤러 세부 비교" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [주간 웹사이트 SEO 감사 흐름](https://x.com/cleeeeeeeeement/status/2115488774423773267) (제작자 [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**웹사이트를 우선순위 SEO 계획과 반복 순위 검토 과정으로 바꾼다.**

제작자는 웹사이트에서 경쟁자와 키워드를 식별하고 우선순위 SEO 행동 계획을 만드는 시스템을 개발했다고 보고했다. 주간 순위 추적과 실행 설명에 짧은 녹화가 붙는다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="주간 웹사이트 SEO 감사 흐름" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [Opus 모션 디자인에서 Fable 자산 재사용](https://x.com/chetaslua/status/2115145163542790170) (제작자 [@chetaslua](https://x.com/chetaslua))

**모델과 도구를 결합할 때 자산 제작과 모션 조립을 구분한다.**

제작자는 Fable이 먼저 만들었다는 자산을 이용한 Opus 5.5 Tesla Roadster 모션 디자인을 공유했다. 인용한 기존 작업에는 Blender의 Python, ElevenLabs와 제공된 출시 영상이 명시된다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="Opus 모션 디자인에서 Fable 자산 재사용" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [만다라와 기하학 형태 앱](https://x.com/ZMinimalistYogi/status/2114600083165434189) (제작자 [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**집중된 기하학 아이디어를 상호작용 가능한 창작 탐색 앱으로 만든다.**

제작자는 Fable 5.1과 3시간 대화해 만다라, zome 구조, 아르키메데스 다면체와 연꽃형 기하 얀트라 앱을 만들었다고 보고했다. 개인 사이트에 공유했다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="만다라와 기하학 형태 앱" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Three.js 자전거 라이더](https://x.com/AI_Screening/status/2114266369248354357) (제작자 [@AI_Screening](https://x.com/AI_Screening))

**자전거 장면에서 자세, 기하 구조와 연동된 움직임을 살핀다.**

제작자는 Three.js 자전거 라이더 결과를 공유했다. 녹화는 라이더 주변의 다리와 수변 풍경을 포함한 구체적인 움직임 샘플이다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Three.js 자전거 라이더" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [FrontierCS 2 평가 스냅샷](https://x.com/wenhaocha1/status/2115613415641354262) (제작자 [@wenhaocha1](https://x.com/wenhaocha1))

**출처 링크가 있는 벤치마크 차트를 활용해 Fable 5.1을 다른 모델과 비교한다.**

게시자는 FrontierCS 2 과제 통과율 차트에 Fable 5.1을 추가하고, 보고된 결과를 다른 모델의 결과와 함께 공유한다.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="FrontierCS 2 평가 스냅샷" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [세 모델의 얼룩말 애니메이션 비교](https://x.com/AI_Screening/status/2115849659797373038) (제작자 [@AI_Screening](https://x.com/AI_Screening))

**모델 이름이 표시된 세 출력을 함께 보며 달리는 얼룩말 과제의 결과를 비교한다.**

게시자는 Fable 5.5, Opus 5.5, Gemini 4 Argon으로 표시된 얼룩말 애니메이션을 나란히 비교한다. 공유된 영상은 세 출력의 구체적인 걸음걸이 샘플을 보여 준다.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="세 모델의 얼룩말 애니메이션 비교" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [긴 일본어 문장의 가독성 비평](https://x.com/AM09_21/status/2106670042184356156) (제작자 [@AM09_21](https://x.com/AM09_21))

**모델에게 생성된 일본어 장문이 읽기 어려운 이유를 진단하게 한다.**

작성자는 Opus의 긴 일본어 문장이 왜 읽기 어려운지 물었다고 보고했다. 답변은 영어식 구문, 반복 단어, 표면적 수정을 지적해 구체적인 문장 비평 흐름을 보여 준다.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [예시로 유도한 기술 PowerPoint](https://x.com/mt_moco/status/2106665038375522791) (제작자 [@mt_moco](https://x.com/mt_moco))

**기술 발표 자료를 요청하기 전에 예시를 제공한다.**

작성자는 몇 가지 발표 예시를 제공하자 활용 가능한 기술 PowerPoint를 얻었다고 보고했다. 구체적인 발표 작업에서 예시 기반 지시와 문서 구조 개선을 연결한 경험이다.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [음악 전체의 일관성 비교](https://x.com/AM09_21/status/2106573080214770011) (제작자 [@AM09_21](https://x.com/AM09_21))

**생성 음악을 평가할 때 국소적 세부와 곡 전체 구조를 나눠 본다.**

작성자는 음표, 선율, 전환을 통해 모델 작곡을 비교하고 부분적 일관성과 큰 음악 구조를 구분했다. 청취에 기반한 작곡 품질 평가다.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [성급한 완료 보고와 부족한 디자인](https://x.com/johntitorIII/status/2106442876506747353) (제작자 [@johntitorIII](https://x.com/johntitorIII))

**에이전트의 완료 보고를 받아들이기 전에 산출물을 요구사항과 대조한다.**

작성자는 며칠간의 시험에서 미완성 작업이 완료 처리되고 디자인이 다른 모델보다 떨어졌다고 보고했다. 성급한 완료와 디자인 품질 문제를 실제 실패 유형으로 기록한다.

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [불편함을 준 오징어 그림 결과](https://x.com/hanawo_neki/status/2106271036094415186) (제작자 [@hanawo_neki](https://x.com/hanawo_neki))

**열린 미술 요청에서 원치 않는 스타일이 나오면 미적 선호를 명시한다.**

작성자는 자유로운 오징어 그림을 요청했다가 밀집한 세부 묘사에 불편함을 느꼈다고 보고했다. 열린 시각적 요청과 개인적 취향의 불일치를 기록한 사례다.

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [청사진 스타일 모션 디자인](https://x.com/DavidayoAI/status/2106054662063325638) (제작자 [@DavidayoAI](https://x.com/DavidayoAI))

**빠른 애니메이션의 시각적 방향으로 청사진 미학을 지정한다.**

작성자는 짧은 애니메이션을 요청한 뒤 약 15분 후 청사진 스타일 결과를 받았다고 보고했다. 전체 작품은 YouTube 링크로 제공한다.

[관련 작업](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [복셀 벚꽃 속 새와 물고기](https://x.com/xodud_rkd/status/2105876716472447046) (제작자 [@xodud_rkd](https://x.com/xodud_rkd))

**복셀 풍경 안에서 움직이는 야생동물을 탐색한다.**

작성자는 새와 연못 물고기가 움직이는 복셀 벚꽃 장면을 설명하고 인터랙티브 작품을 링크했다. 공유된 페이지가 이 장면과 연결된 산출물이다.

[관련 작업](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [캐릭터 생성 실패 보고](https://x.com/doof1789559/status/2105874208458752227) (제작자 [@doof1789559](https://x.com/doof1789559))

**성공한 영상과 함께 캐릭터 생성의 부정적 경험도 기록한다.**

작성자는 캐릭터 생성 결과가 나쁘다고 보고하면서 자신의 접근법이 원인일 가능성도 인정했다. 게시물은 캐릭터 과제를 평가할 독자의 구체적인 부정적 경험을 보존한다.

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [실행 시간과 비용을 담은 펠리컨 SVG](https://x.com/AnonymerNutze12/status/2105740440385499295) (제작자 [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**그림 결과와 제작자의 시간·비용 기록을 함께 제시한다.**

작성자는 펠리컨 SVG HTML 작품을 링크하고 해당 시도의 실행 시간과 비용을 보고했다. 연결된 작품이 게시물에서 말하는 구체적인 산출물이다.

[관련 작업](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [휴대폰으로 원격 코딩 스웜 감독](https://x.com/beistnormie/status/2106546741000417781) (제작자 [@beistnormie](https://x.com/beistnormie))

**휴대폰 기반으로 코딩 에이전트 스웜을 원격 감독하는 흐름을 탐색한다.**

작성자는 여행 중 휴대폰으로 Claude Code 스웜을 원격 조작해 코딩한다고 보고했다. 게시물은 개인 작업 흐름 보고이며 프로젝트나 구현 단계 튜토리얼은 아니다.

Type: Integration | Date: 2026-10-04

---

<a id="acknowledge"></a>
## 🙏 감사의 말

이 저장소는 실제 Claude Fable 5 사용 사례를 공개적으로 공유한 크리에이터, 개발자, 벤치마크 팀, 커뮤니티에서 영감을 받았습니다.

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@AnikaCodes](https://x.com/AnikaCodes)

*모든 사례가 원래 크리에이터에게 정확히 귀속되었다고 보장할 수는 없습니다. 수정이 필요한 부분이 있다면 연락해 주세요. 업데이트하겠습니다.*

공유할 더 흥미로운 사용 사례가 있다면 issue 또는 pull request를 열어 Evolink usecase library 확장에 도움을 주세요.


[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
