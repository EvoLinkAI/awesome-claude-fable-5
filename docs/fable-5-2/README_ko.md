# Claude Fable 5.2 활용 사례

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

11월 10일 수집한 워크플로, 데모, 비교, 벤치마크, 통합 및 실제 사용상 한계를 원문 링크와 함께 정리했습니다.

[Anthropic 발표](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [이전 사례 모음](../../README_ko.md)

## 사례 목록

| Case | 활용 사례 | Type |
| --- | --- | --- |
| 330 | [추론 강도별 MacBook SVG 그리기](#case-330) | Benchmark |
| 331 | [가족 그림을 활용한 4인용 횡스크롤 액션 게임](#case-331) | Demo |
| 332 | [전자 기기 세 가지를 설계부터 조립까지](#case-332) | Demo |
| 333 | [Lean으로 페르마의 마지막 정리 형식화](#case-333) | Evaluation |
| 334 | [빈 폴더에서 시작한 운영체제](#case-334) | Demo |
| 335 | [RoboDojo 양팔 조작 벤치마크](#case-335) | Benchmark |
| 336 | [물이 흐르는 분수](#case-336) | Demo |
| 337 | [Higgsfield로 프레임 단위 립싱크](#case-337) | Integration |
| 338 | [오픈 월드 운전 게임 시제품](#case-338) | Demo |
| 339 | [참고 이미지로 재현한 1940년 파리](#case-339) | Integration |
| 340 | [Fable이 기획하고 Opus가 제작한 단편](#case-340) | Integration |
| 341 | [뮤직비디오 제작 실험](#case-341) | Demo |
| 342 | [Dario Amodei의 초상화](#case-342) | Demo |
| 343 | [추론 강도 Medium으로 만든 Spud Smash](#case-343) | Demo |
| 344 | [Fable과 Opus로 만든 얼음 성당](#case-344) | Evaluation |
| 345 | [성도 시뮬레이션으로 부르는 노래](#case-345) | Demo |
| 346 | [이스탄불을 주제로 한 복셀 테스트 세 가지](#case-346) | Evaluation |
| 347 | [Remote Labor Index 프로젝트 완료율](#case-347) | Benchmark |
| 348 | [추론 강도 네 단계에서 만든 빙산](#case-348) | Evaluation |
| 349 | [79초 애니메이션 단편](#case-349) | Demo |
| 350 | [Fable과 Opus의 기계 조립도 비교](#case-350) | Evaluation |
| 351 | [나선형 계단을 오르는 로봇 손](#case-351) | Demo |
| 352 | [Blender에서 Tripo 메시 리깅](#case-352) | Evaluation |
| 353 | [다빈치 수첩 속 발명품을 인터랙티브하게 재현](#case-353) | Demo |
| 354 | [Claude가 조작하는 음악 제작 환경](#case-354) | Demo |
| 355 | [Raspberry Pi 5 제품 애니메이션](#case-355) | Demo |
| 356 | [이탈리아 북부 풍경](#case-356) | Demo |
| 357 | [로컬 작업 에이전트로 만든 팝업북](#case-357) | Evaluation |
| 358 | [다시 진행한 용암 램프 테스트](#case-358) | Evaluation |
| 359 | [Blender에서 만든 정밀한 제트기](#case-359) | Integration |
| 360 | [포털로 연결한 수백 개의 세계](#case-360) | Demo |
| 361 | [Three.js로 그린 뭄바이 시장의 여섯 장면](#case-361) | Integration |
| 362 | [코드로 제작한 실사풍 미국식 식당](#case-362) | Integration |
| 363 | [Blender에서 만든 로봇 모델](#case-363) | Demo |
| 364 | [Convex를 설명하는 모션 그래픽](#case-364) | Demo |
| 365 | [한 번의 지시로 만든 랜딩 페이지 모음](#case-365) | Demo |
| 366 | [LilyPond로 기보한 피아노 소나타](#case-366) | Demo |
| 367 | [제약 없이 요청한 영상 제작](#case-367) | Demo |
| 368 | [Fable이 계획하고 DeepSeek가 구현하며 Opus가 검토](#case-368) | Integration |
| 369 | [AI Village의 Fable 5.2](#case-369) | Integration |
| 370 | [Skills 사용 여부에 따른 프런트엔드 비교](#case-370) | Evaluation |
| 371 | [코드베이스의 암묵적 상태 머신 찾기](#case-371) | Tutorial |
| 372 | [8시간 만에 처음부터 만든 게임](#case-372) | Demo |
| 373 | [Fishslop 시제품과 토큰 비용](#case-373) | Evaluation |
| 374 | [미식축구 게임의 플레이 영상](#case-374) | Demo |
| 375 | [Higgsfield MCP를 활용한 오픈 월드 보스전](#case-375) | Integration |
| 376 | [조수가 변하는 몽생미셸](#case-376) | Demo |
| 377 | [Blender에서 확인하는 Roblox 에셋](#case-377) | Demo |
| 378 | [사고 과정을 출력하지 않는 추론 평가](#case-378) | Benchmark |
| 379 | [네 모델이 다시 만든 Chrome 공룡 게임](#case-379) | Evaluation |
| 380 | [로봇 팔로 두는 체커](#case-380) | Demo |
| 381 | [15초 모션 그래픽 영상](#case-381) | Demo |
| 382 | [플레이 가능한 에펠탑 장면](#case-382) | Demo |
| 383 | [Three.js와 Higgsfield로 만든 해상 경주](#case-383) | Integration |
| 384 | [WebGL에서 실시간으로 구현한 꿀](#case-384) | Demo |
| 385 | [실사 영상에 프로그램으로 시각 효과 추가](#case-385) | Demo |
| 386 | [GTA 수배 단계 모션 설명 영상](#case-386) | Demo |
| 387 | [코드로 만든 스타일화 MMO 세계](#case-387) | Demo |
| 388 | [Fable과 Opus의 3D 장면 비교](#case-388) | Evaluation |
| 389 | [게임 일시 정지 화면의 과도한 문구](#case-389) | Limit |
| 390 | [Krea 실행 환경으로 만든 무드보드](#case-390) | Integration |
| 391 | [사무실에서 포털 슈팅 게임 시험](#case-391) | Demo |
| 392 | [Blender 하드 서피스 에셋의 디테일](#case-392) | Demo |
| 393 | [여러 추론 강도의 병렬 프런트엔드 테스트](#case-393) | Evaluation |
| 394 | [프롬프트 10개로 만든 소형 게임](#case-394) | Demo |
| 395 | [JavaScript로 매 프레임을 그린 애니메이션](#case-395) | Demo |
| 396 | [참고 영상으로 만든 3D 애니메이션](#case-396) | Demo |
| 397 | [Fable과 Opus의 픽셀 모닥불](#case-397) | Evaluation |
| 398 | [추론 강도 xHigh의 Arena WebDev](#case-398) | Benchmark |
| 399 | [두 모델의 영화 예고편 타이포그래피](#case-399) | Evaluation |
| 400 | [프롬프트 하나로 시험한 모션과 3D 포트폴리오](#case-400) | Evaluation |
| 401 | [분해하며 살펴보는 원자로](#case-401) | Demo |
| 402 | [Blood on the Clocktower 에이전트 평가](#case-402) | Benchmark |
| 403 | [포드레이서풍 경주 시제품](#case-403) | Demo |
| 404 | [10초짜리 Claude 속옷 광고](#case-404) | Demo |
| 405 | [해 뜨는 풍경 속 새를 한 획씩 그리기](#case-405) | Demo |
| 406 | [Devin에서 장시간 그래픽 작업](#case-406) | Evaluation |
| 407 | [세 모델이 코드로 그린 그림 비교](#case-407) | Evaluation |
| 408 | [애니메이션으로 보는 문자 역사](#case-408) | Demo |
| 409 | [게임 속 기계 장치 시험장](#case-409) | Demo |
| 410 | [휴대용 Linux 게임기의 PCB 설계](#case-410) | Evaluation |
| 411 | [복셀로 만든 호수](#case-411) | Demo |
| 412 | [Arena의 인터랙티브 생성 예시 17개](#case-412) | Demo |
| 413 | [친근한 용과 함께 비행](#case-413) | Demo |
| 414 | [Fable과 Opus의 젤리 범고래](#case-414) | Evaluation |
| 415 | [자유 주제로 보는 영상 품질](#case-415) | Demo |
| 416 | [지중해풍 우주 거주 시설](#case-416) | Demo |
| 417 | [AA-3D 인터랙티브 경험 벤치마크](#case-417) | Benchmark |
| 418 | [해골 캐릭터의 타임 챌린지](#case-418) | Demo |
| 419 | [Fable과 Astra의 픽셀 아트 비교](#case-419) | Evaluation |
| 420 | [모션 디자인 포트폴리오 영상](#case-420) | Demo |
| 421 | [두 모델의 유리 수영장 렌더링](#case-421) | Evaluation |
| 422 | [TS-Bench 도구 호출 정확도](#case-422) | Benchmark |
| 423 | [미니어처 마추픽추](#case-423) | Demo |
| 424 | [전문 작업 분야별 GDPx 결과](#case-424) | Benchmark |
| 425 | [그림 앱에서 초상화 그리기](#case-425) | Demo |
| 426 | [추론 강도 Low의 VulcanBench Frontier v4](#case-426) | Benchmark |
| 427 | [괴물을 조종하는 백룸 게임](#case-427) | Demo |
| 428 | [Blender에서 만든 Bugatti Tourbillon](#case-428) | Demo |
| 429 | [두 모델로 제작한 컴퓨터 테마 영상](#case-429) | Demo |
| 430 | [Megakernel을 주제로 한 뮤직비디오](#case-430) | Demo |
| 431 | [참고 사진으로 만든 스튜디오 투어](#case-431) | Demo |
| 432 | [코드로 만든 1990년대풍 장난감 광고](#case-432) | Demo |
| 433 | [Three.js 3인칭 게임 장면](#case-433) | Demo |
| 434 | [기존 렌더러로 만든 Bryceball](#case-434) | Demo |
| 435 | [Fable로 편집한 영상을 다시 편집](#case-435) | Demo |
| 436 | [영화처럼 보는 과학의 역사](#case-436) | Demo |
| 437 | [다빈치 비행 장치의 3D 모델](#case-437) | Integration |
| 438 | [설계 요구사항에 따른 PCB 배선](#case-438) | Demo |
| 439 | [서로 다른 실행 환경에 같은 프롬프트 적용](#case-439) | Evaluation |
| 440 | [코드로 그린 고질라](#case-440) | Demo |
| 441 | [3D 프린팅용 휴대용 선풍기](#case-441) | Demo |
| 442 | [Opus와 비교한 플러그인 버그 조사](#case-442) | Evaluation |
| 443 | [3D 장면으로 재현한 이스탄불](#case-443) | Demo |
| 444 | [화면까지 움직이는 Blender 스튜디오 영상](#case-444) | Demo |
| 445 | [약결합 영역에서의 블랙홀 전이](#case-445) | Evaluation |
| 446 | [모듈러 부트스트랩 경계의 한계](#case-446) | Evaluation |
| 447 | [Vercel AI Gateway의 순서 지정 모델 폴백](#case-447) | Integration |
| 448 | [중첩 하위 에이전트와 검토 예산](#case-448) | Limit |
| 449 | [LCARS 디자인을 HTML로 변환한 비교](#case-449) | Evaluation |
| 450 | [Quantum ESPRESSO의 GPU 최적화](#case-450) | Benchmark |
| 451 | [추론 강도별 Artificial Analysis Intelligence Index](#case-451) | Benchmark |
| 452 | [High 설정의 변경 검토에서 나온 오탐](#case-452) | Limit |
| 453 | [일상적인 코딩 과제 30개](#case-453) | Evaluation |
| 454 | [무인도 화면 보호기](#case-454) | Demo |
| 455 | [추론 강도 High의 브라우저 게임 3개](#case-455) | Evaluation |
| 456 | [책의 장별 팟캐스트 대본](#case-456) | Evaluation |
| 457 | [Rust로 이전한 운영 서비스](#case-457) | Evaluation |
| 458 | [GitHub Copilot에서 Fable 5.2 선택](#case-458) | Integration |
| 459 | [HTML 100페이지 디자인 도전](#case-459) | Evaluation |
| 460 | [컴파일러 작업에서 요구사항이 달라진 사례](#case-460) | Limit |
| 461 | [Opus로 긴 Fable 작업의 진행 상황 확인](#case-461) | Integration |
| 462 | [새로운 시각으로 코드를 재검토](#case-462) | Tutorial |
| 463 | [기능 설계 검토에서 조언이 빗나간 사례](#case-463) | Limit |
| 464 | [DX Ball 스타일 벽돌 깨기 비교](#case-464) | Evaluation |
| 465 | [3D 앱 개선 실험](#case-465) | Evaluation |
| 466 | [세 모델이 만든 고양이와 생쥐 게임](#case-466) | Evaluation |
| 467 | [AIBenchy의 추론 강도 High 비용 및 점수 비교](#case-467) | Benchmark |
| 468 | [Fable 5.2 에이전트 실행 환경 조정](#case-468) | Tutorial |

<a id="fable-5-2-cases"></a>
## 활용 사례

<a id="case-330"></a>
### Case 330: [추론 강도별 MacBook SVG 그리기](https://playcode.io/blog/macbook-svg-benchmark#compare) (작성자 [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**같은 지시에서 그림 품질, 토큰 사용량, 출력 상한을 비교한다.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode에 따르면 Fable 5.2 High는 토큰 76,158개를 사용해 3.05달러가 들었다. Xhigh와 Max 스트리밍 실행은 128,000개 토큰 한도까지 그림을 내지 못했지만, Batch API에서 더 많은 출력을 허용하자 두 설정 모두 완료했다. 순위는 발표자의 시각적 판단에 따른다.

[관련 자료 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [가족 그림을 활용한 4인용 횡스크롤 액션 게임](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (작성자 [Lex](https://notesbylex.com/))

**스케치, 기존 시제품, 컨트롤러 요구사항을 코딩 에이전트에 제공한다.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex는 Claude Code로 기존 횡스크롤 게임을 12개 스테이지와 18개 캐릭터를 가진 액션 게임으로 다시 만들었다. 이미지와 오디오 도구로 에셋을 준비했고 가족 플레이 테스트에서 컨트롤러 4개가 모두 작동했다.

[관련 자료 1](https://aidens-revenge.pages.dev/) · [관련 자료 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [관련 자료 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [전자 기기 세 가지를 설계부터 조립까지](https://www.anthropic.com/research/claude-electronics-design) (작성자 [@Anthropic](https://www.anthropic.com/))

**회로, 외장, 펌웨어를 하나의 시스템으로 검증한다.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ 동영상 재생</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic과 Diode는 작동하는 기기 3개를 보고했다. Fable 5.2는 기판 배선, 외장 모델링, 소프트웨어 작성, 제조 후 테스트 안내를 맡았다.

[관련 자료 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [관련 자료 2](https://www.youtube.com/watch?v=vdYynH177h0) · [관련 자료 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [Lean으로 페르마의 마지막 정리 형식화](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (작성자 [@Anthropic](https://www.anthropic.com/))

**증명 검사기와 중간 정리로 진행 상황을 확인한다.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Anthropic은 Fable 5.2 에이전트 1,000개로 이루어진 팀이 기존 증명을 30시간에 형식화했다고 보고했다. 같은 팀 구성에서 Opus 5.5는 18시간에 26%를 완료했다.

[관련 자료 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [관련 자료 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [빈 폴더에서 시작한 운영체제](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (작성자 [@Anthropic](https://www.anthropic.com/))

**부팅, 드라이버, 저장 장치, 설치를 따로 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ 동영상 재생</a>

Anthropic은 Fable 5.2가 8일간 하위 에이전트 1,000개 이상을 조율해 노트북에서 부팅되는 운영체제 시제품을 만들었다고 밝혔다.

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [RoboDojo 양팔 조작 벤치마크](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (작성자 [@Anthropic](https://www.anthropic.com/))

**여러 모델에 같은 시뮬레이션 조작 과제를 수행하게 한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ 동영상 재생</a>

Anthropic에 따르면 RoboDojo에서 Fable 5.2는 64.9%, Fable 5.1은 27.6%를 기록했다. 발표 자료에는 로봇 데모도 포함된다.

[관련 자료 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [물이 흐르는 분수](https://x.com/Angaisb_/status/2119909059277238733) (작성자 [@Angaisb_](https://x.com/Angaisb_))

**물의 연속 움직임을 보며 장면의 리듬을 판단한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

제작자는 Fable 5.2로 만들었다고 밝힌 분수 장면을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [Higgsfield로 프레임 단위 립싱크](https://x.com/higgsfield_ai/status/2119909938969580024) (작성자 [@higgsfield_ai](https://x.com/higgsfield_ai))

**영상을 검토하기 전에 프레임 단위로 음성을 맞춘다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ 동영상 재생</a>

Higgsfield는 제작 과정에서 Fable 5.2로 입 움직임을 추적하고 프레임에 맞게 음성을 정렬했다고 밝혔다.

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [오픈 월드 운전 게임 시제품](https://x.com/ericmaskfr/status/2119910195325481026) (작성자 [@ericmaskfr](https://x.com/ericmaskfr))

**짧은 오픈 월드 제작 지시를 플레이 가능한 일부분에서 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 GTA에서 영감을 받은 게임 시제품을 공개하고 실행에 약 2시간 14분이 걸렸다고 밝혔다.

원본 프롬프트

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [참고 이미지로 재현한 1940년 파리](https://x.com/higgsfield_ai/status/2119910344998912507) (작성자 [@higgsfield_ai](https://x.com/higgsfield_ai))

**참고 이미지 생성과 장면 코드 작성을 분리한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ 동영상 재생</a>

Higgsfield는 자사 MCP로 참고 이미지를 제공하고 Fable 5.2를 사용해 Three.js 장면을 만들었다.

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable이 기획하고 Opus가 제작한 단편](https://x.com/kloss_xyz/status/2119910613828980846) (작성자 [@kloss_xyz](https://x.com/kloss_xyz))

**영상 작업에서 기획과 제작을 분리한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ 동영상 재생</a>

Fable 5.2가 요구사항과 계획을 작성했다. Opus 5.5는 Blender와 Python으로 16초 애니메이션을 만들고 음악을 합성했다.

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [뮤직비디오 제작 실험](https://x.com/WesRoth/status/2119911161386934330) (작성자 [@WesRoth](https://x.com/WesRoth))

**가사와 생성된 영상을 함께 검토한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 만든 뮤직비디오를 공유하고 가사에 관해 언급했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Dario Amodei의 초상화](https://x.com/Mr_Salio/status/2119911922577637543) (작성자 [@Mr_Salio](https://x.com/Mr_Salio))

**스타일을 적용한 초상화와 나란히 표시된 참고 이미지를 대조한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 그렸다고 밝힌 Dario Amodei의 초상화를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [추론 강도 Medium으로 만든 Spud Smash](https://x.com/argofowl/status/2119913148929187960) (작성자 [@argofowl](https://x.com/argofowl))

**게임 시제품에 명확한 조작과 목표를 준다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 파란 의자를 주먹으로 치거나 박치기하거나 불태우는 감자 캐릭터를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Fable과 Opus로 만든 얼음 성당](https://x.com/QQTeng/status/2119913518015435103) (작성자 [@QQTeng](https://x.com/QQTeng))

**같은 장면의 생성 시간과 비용을 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ 동영상 재생</a>

제작자에 따르면 Fable은 약 1시간 57분에 81.10달러, Opus는 약 3시간 11분에 45.97달러였다.

원본 프롬프트

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [성도 시뮬레이션으로 부르는 노래](https://x.com/banteg/status/2119914098171199996) (작성자 [@banteg](https://x.com/banteg))

**물리 음성 모델을 음악 제작의 입력으로 활용한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Chimera 성도 시뮬레이션 두 개와 보코더 믹스를 사용한 커버 곡을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [이스탄불을 주제로 한 복셀 테스트 세 가지](https://x.com/Avenoxai/status/2119914308603953485) (작성자 [@Avenoxai](https://x.com/Avenoxai))

**파괴 장면, 움직이는 시계, 지도를 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 각각 프롬프트 하나를 사용한 테스트 세 가지를 공유하고 자체 기준으로 100점, 100점, 95.6점을 기록했다고 밝혔다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Remote Labor Index 프로젝트 완료율](https://x.com/ScaleAILabs/status/2119914701736075489) (작성자 [@ScaleAILabs](https://x.com/ScaleAILabs))

**비율을 평가에 사용한 특정 프로젝트의 결과로 해석한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ 동영상 재생</a>

Scale Labs와 CAIS는 Fable 5.2가 평가 대상 원격 업무 프로젝트의 41.3%를 성공적으로 완료했다고 보고했다.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [추론 강도 네 단계에서 만든 빙산](https://x.com/0xRhinoX/status/2119915121698840587) (작성자 [@0xRhinoX](https://x.com/0xRhinoX))

**추론 강도를 높이며 완성도, 비용, 디테일을 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 네 단계에 같은 프롬프트를 사용했다. High에서는 오로라가 빠졌고 Ultra에는 빛나는 얼음과 수중 시점이 추가됐다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [79초 애니메이션 단편](https://x.com/anstapnever/status/2119915123070644263) (작성자 [@anstapnever](https://x.com/anstapnever))

**길이가 긴 애니메이션에서 장면 연결을 살펴본다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2 작업으로 만들었다고 밝힌 79초 애니메이션을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Fable과 Opus의 기계 조립도 비교](https://x.com/ivanainai/status/2119915243321397550) (작성자 [@ivanainai](https://x.com/ivanainai))

**각 모델이 기계 부품을 어떻게 배치하는지 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 Fable 5.2와 Opus 5.5로 각각 만든, 레이블이 있는 바퀴와 기어 조립체의 분해 렌더링을 공개했다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [나선형 계단을 오르는 로봇 손](https://x.com/Luckyballa/status/2119915557663506720) (작성자 [@Luckyballa](https://x.com/Luckyballa))

**시뮬레이션 장애물에서 색다른 이동 방식을 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2와 Steel 0.1로 Wuji 로봇 손을 손가락으로 걷게 한 테스트를 공유했다.

[관련 자료 1](https://github.com/skild-ai/steel-webgpu/pull/7)

원본 프롬프트

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [Blender에서 Tripo 메시 리깅](https://x.com/0xKense1/status/2119916096098582566) (작성자 [@0xKense1](https://x.com/0xKense1))

**파지, 텍스처, 변형을 수치 기준으로 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 Tripo 에셋을 사용한 리그 2개를 비교했다. Fable은 36분에 클립 2개, Opus는 약 21분에 8개를 제작했다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [다빈치 수첩 속 발명품을 인터랙티브하게 재현](https://x.com/alexalbert__/status/2119916954337349737) (작성자 [@alexalbert__](https://x.com/alexalbert__))

**원본 도면을 이용해 조작 가능한 교육용 모델을 만든다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ 동영상 재생</a>

Alex Albert는 다빈치 수첩 PDF를 제공하고 그 안의 발명품을 체험할 수 있도록 재해석한 결과를 공개했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [Claude가 조작하는 음악 제작 환경](https://x.com/The_Alex/status/2119917226769985785) (작성자 [@The_Alex](https://x.com/The_Alex))

**반복되는 작곡 요청에 에이전트가 조작하는 도구를 활용한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 Fable 5.2로 만든 디지털 오디오 워크스테이션을 공유하고 나중에 Opus가 이를 열어 곡을 만들었다고 밝혔다.

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [Raspberry Pi 5 제품 애니메이션](https://x.com/sparklabhq/status/2119917375080521921) (작성자 [@sparklabhq](https://x.com/sparklabhq))

**제품 애니메이션 지시로 부품의 세부 표현을 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 만든 Raspberry Pi 5 애니메이션을 공유했다.

원본 프롬프트

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [이탈리아 북부 풍경](https://x.com/Angaisb_/status/2119917807119089926) (작성자 [@Angaisb_](https://x.com/Angaisb_))

**특정 장소를 지정해 경관과 분위기를 살펴본다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 만든 이탈리아 북부 장면을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [로컬 작업 에이전트로 만든 팝업북](https://x.com/atomicagent_io/status/2119918110752846094) (작성자 [@atomicagent_io](https://x.com/atomicagent_io))

**같은 과제에서 에이전트 조율 방식과 단일 모델 실행을 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ 동영상 재생</a>

Atomic에 따르면 Fable이 로컬 Qwen 작업자를 조율했을 때 11분에 2.98달러, Fable 단독 실행은 21분에 15.77달러였다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [다시 진행한 용암 램프 테스트](https://x.com/eidzoku/status/2119918134060601690) (작성자 [@eidzoku](https://x.com/eidzoku))

**같은 시각 과제로 여러 모델을 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 용암 램프 테스트를 재개하고 생성 결과를 나란히 공개했다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [Blender에서 만든 정밀한 제트기](https://x.com/higgsfield_ai/status/2119918248955392431) (작성자 [@higgsfield_ai](https://x.com/higgsfield_ai))

**제작 지시에 부품 수, 영상 길이, 외형을 명시한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ 동영상 재생</a>

Higgsfield는 Fable 5.2와 자사 MCP를 써서 부품 931개와 리벳 24,260개가 포함된 Blender 모델을 스크립트로 제작했다고 밝혔다.

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [포털로 연결한 수백 개의 세계](https://x.com/emollick/status/2119918307457577163) (작성자 [@emollick](https://x.com/emollick))

**별도로 생성한 환경을 포털로 연결한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ 동영상 재생</a>

Ethan Mollick은 에이전트 25,000개가 세계 450개 이상을 코드로 만들었다고 밝히고 체험판과 저장소를 공유했다.

[관련 자료 1](https://portals-endless-worlds.netlify.app/) · [관련 자료 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [Three.js로 그린 뭄바이 시장의 여섯 장면](https://x.com/higgsfield_ai/status/2119918834841010320) (작성자 [@higgsfield_ai](https://x.com/higgsfield_ai))

**영상 지시를 길이가 정해진 숏으로 나눈다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ 동영상 재생</a>

Higgsfield는 Three.js에서 렌더링한 21.5초 길이의 시장 영상과 그 안의 숏 6개를 공유했다.

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [코드로 제작한 실사풍 미국식 식당](https://x.com/higgsfield_ai/status/2119918838490010008) (작성자 [@higgsfield_ai](https://x.com/higgsfield_ai))

**코드로 만든 장면에서 소재와 조명을 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ 동영상 재생</a>

Higgsfield는 미국식 식당 장면을 공개하고 3D 모델링 앱 없이 코드로 제작했다고 밝혔다.

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [Blender에서 만든 로봇 모델](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (작성자 [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**회전 뷰로 관절과 실루엣을 살펴본다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2와 Blender로 제작한 소형 기계 로봇을 공개했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [Convex를 설명하는 모션 그래픽](https://x.com/Rasmic/status/2119919466163093768) (작성자 [@Rasmic](https://x.com/Rasmic))

**짧은 애니메이션으로 개발자용 제품을 설명한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 만든 Convex 모션 그래픽 설명 영상을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [한 번의 지시로 만든 랜딩 페이지 모음](https://x.com/daradoescode/status/2119919529807466594) (작성자 [@daradoescode](https://x.com/daradoescode))

**여러 짧은 지시의 결과에서 레이아웃과 정보 위계를 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 만든 랜딩 페이지를 모은 영상을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [LilyPond로 기보한 피아노 소나타](https://x.com/imjustnewatai/status/2119919644836347926) (작성자 [@imjustnewatai](https://x.com/imjustnewatai))

**악보의 소스와 렌더링한 영상을 대응시킨다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 베토벤풍 악장을 요청했고 화면에 나오는 음표가 LilyPond 소스에서 나왔다고 밝혔다.

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [제약 없이 요청한 영상 제작](https://x.com/aollivier82/status/2119920990893244510) (작성자 [@aollivier82](https://x.com/aollivier82))

**표현을 제한하지 않고 모델이 무엇을 선택하는지 살펴본다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2에 가능한 한 아름다운 영상을 만들어 달라고 요청하고 그 결과를 공유했다.

원본 프롬프트

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable이 계획하고 DeepSeek가 구현하며 Opus가 검토](https://x.com/ivanfioravanti/status/2119921810267636201) (작성자 [@ivanfioravanti](https://x.com/ivanfioravanti))

**조율, 구현, 검토를 서로 다른 에이전트에 맡긴다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 Fable이 herdr로 DeepSeek V4.1 Flash 작업자 4개를 조율하고 Opus 5.5가 PR을 검토하는 구성을 보여 줬다.

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [AI Village의 Fable 5.2](https://x.com/aidigest_/status/2119923190411719158) (작성자 [@aidigest_](https://x.com/aidigest_))

**에이전트의 실제 답변과 메모리 동작을 구분해 확인하세요.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

AI Village 공개 기록에는 Fable이 다른 에이전트의 요청을 받고 나중에 메모리를 수정하겠다고 답한 내용이 있습니다. 관련 게시물은 캐릭터 매칭 퀴즈도 보여 줍니다.

[관련 자료 1](https://x.com/aidigest_/status/2119923209311260707) · [관련 자료 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [Skills 사용 여부에 따른 프런트엔드 비교](https://x.com/AdamHoltererer/status/2119924849321914653) (작성자 [@AdamHoltererer](https://x.com/AdamHoltererer))

**같은 모델에서 Skills 설정만 바꿔 본다.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

제작자는 Fable 5.2에 Skills를 적용한 경우와 적용하지 않은 경우의 프런트엔드 결과를 공개했다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [코드베이스의 암묵적 상태 머신 찾기](https://x.com/kunchenguid/status/2119924895060795492) (작성자 [@kunchenguid](https://x.com/kunchenguid))

**구체적인 모듈을 점검하고 변경 전후의 도표를 요청한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

작성자는 Firstmate 저장소의 코드 정리 예시와 실제 점검 프롬프트 원문을 공개했다.

[관련 자료 1](https://github.com/kunchenguid/lavish-axi)

원본 프롬프트

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [8시간 만에 처음부터 만든 게임](https://x.com/felixrieseberg/status/2119925633564463609) (작성자 [@felixrieseberg](https://x.com/felixrieseberg))

**캐시된 입력, 생성된 에셋, 실제 소요 시간을 기록한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ 동영상 재생</a>

Anthropic 엔지니어는 한 번의 실행으로 모델, 소리, 텍스처를 만들었으며 API 요금 기준 약 550달러였다고 밝혔다.

[관련 자료 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [관련 자료 2](https://x.com/AndrewCurran_/status/2119953960794780133)

원본 프롬프트

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Fishslop 시제품과 토큰 비용](https://x.com/theo/status/2119926277801144695) (작성자 [@theo](https://x.com/theo))

**게임 결과물을 이전 모델의 결과와 비교한다.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ 동영상 재생</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

제작자는 실행에 76분과 약 42달러의 토큰 비용이 들었다고 밝히고 Opus 5.5의 결과와 비교했다.

[관련 자료 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [미식축구 게임의 플레이 영상](https://x.com/WesRoth/status/2119926801514529027) (작성자 [@WesRoth](https://x.com/WesRoth))

**스포츠 게임 시제품에서 조작 반응과 득점 표시를 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 화면에 미식축구 득점이 표시되는 Fable 5.2 플레이 결과를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [Higgsfield MCP를 활용한 오픈 월드 보스전](https://x.com/higgsfield_ai/status/2119926932343324795) (작성자 [@higgsfield_ai](https://x.com/higgsfield_ai))

**직접 플레이하는 부분과 컷신을 구분한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ 동영상 재생</a>

Higgsfield는 Fable 5.2와 자사 MCP로 오픈 월드, 3막 보스전, 컷신을 포함한 브라우저 게임을 만들었다고 밝혔다.

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [조수가 변하는 몽생미셸](https://x.com/loktar00/status/2119927152489472076) (작성자 [@loktar00](https://x.com/loktar00))

**축소한 역사적 풍경에서 수위 변화를 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 조수의 움직임을 애니메이션으로 구현한 몽생미셸 미니어처를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [Blender에서 확인하는 Roblox 에셋](https://x.com/hiyouwhatsapp/status/2119927163264573642) (작성자 [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**가져오기 전에 Blender에서 에셋을 검토한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Roblox 개발을 위해 거의 한 번의 지시로 만든 Blender 결과를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [사고 과정을 출력하지 않는 추론 평가](https://x.com/Tim_Hua_/status/2119927284761293089) (작성자 [@Tim_Hua_](https://x.com/Tim_Hua_))

**추론 출력 조건을 같게 두고 답을 비교한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

평가자는 사고 과정을 출력하지 않는 조건에서 추론과 지식을 시험했으며 Fable 5.2가 GPT-6.1 Sol보다 약간 낮았다고 밝혔다.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [네 모델이 다시 만든 Chrome 공룡 게임](https://x.com/noclipepe/status/2119927838321328577) (작성자 [@noclipepe](https://x.com/noclipepe))

**같은 게임 지시로 작업 시간과 비용을 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 기존 T-Rex 테스트에 Fable 5.2를 추가하고 Opus, Gemini, Astra와 결과를 나란히 보여 줬다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [로봇 팔로 두는 체커](https://x.com/karolina_dubiel/status/2119928342115676576) (작성자 [@karolina_dubiel](https://x.com/karolina_dubiel))

**관절 위치를 읽어 말 집기에 실패하면 다시 시도한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ 동영상 재생</a>

제작자에 따르면 모델은 약 7 mm 처짐을 보정하고 피드백에 따라 실패한 동작을 재시도했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [15초 모션 그래픽 영상](https://x.com/aziz4ai/status/2119928581405200726) (작성자 [@aziz4ai](https://x.com/aziz4ai))

**짧은 코드 애니메이션에 소모된 사용량을 기록한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 코드로 만든 15초 영상을 공유하면서 주간 사용량 한도의 4%를 썼다고 밝혔다.

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [플레이 가능한 에펠탑 장면](https://x.com/bobyau/status/2119928812628771212) (작성자 [@bobyau](https://x.com/bobyau))

**랜드마크 모델이 사용자 조작에 반응하는지 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 에펠탑 데모를 공유하고 제작에 25분이 걸렸다고 밝혔다.

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [Three.js와 Higgsfield로 만든 해상 경주](https://x.com/higgsfield_ai/status/2119928918035910668) (작성자 [@higgsfield_ai](https://x.com/higgsfield_ai))

**혼합 제작 과정에서 게임 로직과 미디어 도구를 분리한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ 동영상 재생</a>

Higgsfield는 큰 파도, AI 경쟁자 5명, 유도 로켓이 등장하는 경주 게임을 공개했다.

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [WebGL에서 실시간으로 구현한 꿀](https://x.com/deedydas/status/2119930300990177509) (작성자 [@deedydas](https://x.com/deedydas))

**브라우저 내 물리 시뮬레이션으로 물질의 움직임을 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 실시간 WebGL 꿀 시뮬레이션과 원래의 짧은 제작 지시를 공개했다.

원본 프롬프트

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [실사 영상에 프로그램으로 시각 효과 추가](https://x.com/ashebytes/status/2119930763105931649) (작성자 [@ashebytes](https://x.com/ashebytes))

**원본 영상에서 효과가 나타나는 타이밍과 위치를 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 실사 영상에 움직이는 그래픽을 합성한 Fable 5.2 시각 효과 테스트를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [GTA 수배 단계 모션 설명 영상](https://x.com/saimagnate/status/2119931563760632311) (작성자 [@saimagnate](https://x.com/saimagnate))

**게임 화면과 도표를 함께 사용해 게임 규칙을 설명하세요.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 Fable 5.2에 한 번 요청해 만들었다고 설명합니다. 영상은 플레이 화면과 도표로 GTA V와 RDR2의 수배 시스템을 비교합니다.

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [코드로 만든 스타일화 MMO 세계](https://x.com/Izkimar/status/2119931740940640542) (작성자 [@Izkimar](https://x.com/Izkimar))

**스타일을 적용한 에셋으로 세계 전체의 일관성을 평가한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 영상의 MMO 세계를 하루 만에 만들었으며 에셋은 모두 코드로 생성했다고 밝혔다.

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [Fable과 Opus의 3D 장면 비교](https://x.com/dom_scholz/status/2119933150025363661) (작성자 [@dom_scholz](https://x.com/dom_scholz))

**준비 시간과 결과의 디테일을 나란히 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 Fable 5.2와 Opus 5.5의 렌더링을 나란히 보여 주고 Fable 실행이 더 빨랐다고 밝혔다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [게임 일시 정지 화면의 과도한 문구](https://x.com/AndrewPrifer/status/2119934600608915465) (작성자 [@AndrewPrifer](https://x.com/AndrewPrifer))

**생성된 인터페이스 문구에 중복 설명이 있는지 확인한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

개발자는 일시 정지 화면에서 Fable 5.2가 필요 이상으로 설명을 쓴 사례를 보여 줬다.

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [Krea 실행 환경으로 만든 무드보드](https://x.com/lambdacalcc/status/2119934725662060663) (작성자 [@lambdacalcc](https://x.com/lambdacalcc))

**시각적 방향을 확정하기 전에 여러 시안을 비교한다.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

제작자는 Fable 5.2를 Krea 실행 환경과 함께 사용한 무드보드 결과 4개를 공유했다.

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [사무실에서 포털 슈팅 게임 시험](https://x.com/_sholtodouglas/status/2119935331499925557) (작성자 [@_sholtodouglas](https://x.com/_sholtodouglas))

**여러 명이 직접 플레이하며 생성된 게임을 평가한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ 동영상 재생</a>

Anthropic 엔지니어는 포털을 사용하는 아레나 FPS를 공개하고 사무실에서 진행한 플레이 테스트를 소개했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Blender 하드 서피스 에셋의 디테일](https://x.com/ziwenxu_/status/2119937420280168929) (작성자 [@ziwenxu_](https://x.com/ziwenxu_))

**Blender 뷰포트에서 토폴로지와 실루엣을 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2의 Blender 결과물로 정밀한 하드 서피스 에셋을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [여러 추론 강도의 병렬 프런트엔드 테스트](https://x.com/AI_masaou/status/2119937635322085640) (작성자 [@AI_masaou](https://x.com/AI_masaou))

**간단한 지시와 어려운 지시를 여러 추론 강도에서 비교한다.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

작성자에 따르면 간단한 결과는 Fable과 Opus가 비슷했다. 더 큰 제작 작업에서는 Fable의 디테일이 풍부했으며, Medium에서 High로 올리면 시간과 토큰 사용량이 크게 늘었다.

[관련 자료 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [프롬프트 10개로 만든 소형 게임](https://x.com/AmirMushich/status/2119937977426338283) (작성자 [@AmirMushich](https://x.com/AmirMushich))

**게임 시제품의 반복 횟수와 산출물 크기를 기록한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 약 3,400줄의 코드로 220 KB 게임을 만들었다고 밝히고 코드와 영상을 공유했다.

[관련 자료 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [JavaScript로 매 프레임을 그린 애니메이션](https://x.com/kevin_t_ngo/status/2119938129079808282) (작성자 [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**프로그램으로 프레임을 그린 시퀀스를 살펴본다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 모든 프레임을 JavaScript로 그렸다는 애니메이션을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [참고 영상으로 만든 3D 애니메이션](https://x.com/KHvostikk/status/2119939061049889130) (작성자 [@KHvostikk](https://x.com/KHvostikk))

**재현한 장면을 평가할 때 원본 영상과 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 영상을 3D 애니메이션으로 바꾼 데모를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Fable과 Opus의 픽셀 모닥불](https://x.com/GrilliotTodd/status/2119939651385655692) (작성자 [@GrilliotTodd](https://x.com/GrilliotTodd))

**같은 픽셀 아트 소재에서 조명과 실루엣을 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ 동영상 재생</a>

Fable 5.2와 Opus 5.5가 같은 모닥불을 표현한 결과가 나란히 담겨 있다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [추론 강도 xHigh의 Arena WebDev](https://x.com/arena/status/2119941204003770690) (작성자 [@arena](https://x.com/arena))

**순위를 비교할 때 적용된 추론 강도를 확인한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena에 따르면 Claude Fable 5.2 xHigh는 Code Arena WebDev에 처음 올라 1,832점을 기록했다.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [두 모델의 영화 예고편 타이포그래피](https://x.com/muku_sns/status/2119941490969624679) (작성자 [@muku_sns](https://x.com/muku_sns))

**같은 문단을 해석한 두 결과를 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 Opus와 Fable의 예고편 타이틀을 나란히 보여 줬다. Fable 버전에는 붉은 테두리와 검게 가린 문구가 추가됐다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [프롬프트 하나로 시험한 모션과 3D 포트폴리오](https://x.com/Khazix0918/status/2119941585538572390) (작성자 [@Khazix0918](https://x.com/Khazix0918))

**제작 지시의 조사, 디자인, 렌더링을 각각 평가한다.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ 동영상 재생</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ 동영상 재생</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ 동영상 재생</a></td></tr></table>

작성자는 ChatGPT 기념 영상, DeepSeek 설명 영상, Three.js 장면, Apple 징안의 3D 재현을 다룬 실행 결과 4개를 공유했다.

[관련 자료 1](https://x.com/Khazix0918/article/2119941585538572390)

원본 프롬프트

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [분해하며 살펴보는 원자로](https://x.com/konstantinsaifo/status/2119941967136379334) (작성자 [@konstantinsaifo](https://x.com/konstantinsaifo))

**부품을 분해하는 조작으로 조립 구조를 보여 준다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 분해할 수 있는 Three.js 원자로 모델을 요청했으며 API 비용이 92달러였다고 밝혔다.

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Blood on the Clocktower 에이전트 평가](https://x.com/dwarkesh_sp/status/2119942657812451482) (작성자 [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**같은 정체 은닉 게임에서 여러 모델을 비교한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

평가자는 이 벤치마크에서 Fable 5.2가 Fable 5.1과 Opus 5.5보다 높았으며 GPT-6 Astra가 앞섰다고 밝혔다.

[관련 자료 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [포드레이서풍 경주 시제품](https://x.com/loktar00/status/2119943124965638444) (작성자 [@loktar00](https://x.com/loktar00))

**익숙한 경주 형식으로 움직임과 조작감을 평가한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 만든 포드레이서풍 결과를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [10초짜리 Claude 속옷 광고](https://x.com/Masimo_Blue/status/2119943368612487285) (작성자 [@Masimo_Blue](https://x.com/Masimo_Blue))

**간단한 제품 지시로 오리지널 음악을 넣은 광고를 시험한다.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ 동영상 재생</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

제작자는 애시드 테크노 음악과 제공된 제품 이미지를 사용한 10초 홍보 영상을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [해 뜨는 풍경 속 새를 한 획씩 그리기](https://x.com/mgrczyk/status/2119943813028548721) (작성자 [@mgrczyk](https://x.com/mgrczyk))

**되돌리기를 꺼 두고 매 획에서 내리는 결정을 살펴본다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 이미 그린 획을 수정할 수 없는 실행 환경에서 해 뜨는 풍경 속 새를 한 획씩 그린 결과를 공개했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [Devin에서 장시간 그래픽 작업](https://x.com/Da7_Tech/status/2119944847255896490) (작성자 [@Da7_Tech](https://x.com/Da7_Tech))

**부하가 큰 렌더링에서 시간과 비용을 기록한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ 동영상 재생</a>

Cognition 앰배서더임을 공개한 제작자는 Devin Max 실행 결과를 공유하며 약 3.5시간에 약 82달러가 들었다고 밝혔다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [세 모델이 코드로 그린 그림 비교](https://x.com/kickingkeys/status/2119945841997672698) (작성자 [@kickingkeys](https://x.com/kickingkeys))

**실행 결과마다 그림이 그려지는 동작과 합성음을 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 소리가 포함된 코드 그림을 공유하고 Fable 5.2, Fable 5.1, Gemini 4 Argon에 같은 프롬프트를 준 테스트를 설명했다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [애니메이션으로 보는 문자 역사](https://x.com/rileybrown/status/2119946022767980985) (작성자 [@rileybrown](https://x.com/rileybrown))

**연대표를 토대로 코드로 생성한 설명 영상을 구성한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 문자 역사를 다룬 애니메이션을 공개하고 프롬프트 하나로 제작했다고 설명했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [게임 속 기계 장치 시험장](https://x.com/techartist_/status/2119946891106394518) (작성자 [@techartist_](https://x.com/techartist_))

**한 장면에서 기믹, 물리 동작, 효과를 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Three.js와 Blender로 네 가지 아이디어를 시험할 수 있는 공간을 만들었다.

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [휴대용 Linux 게임기의 PCB 설계](https://x.com/seveibar/status/2119947341230907453) (작성자 [@seveibar](https://x.com/seveibar))

**같은 회로 요구사항을 놓고 모델별 설계를 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ 동영상 재생</a>

tscircuit 제작자는 Astra 6 High와 Fable 5.2 High로 휴대용 Linux 게임기를 설계한 테스트를 보여 줬다.

원본 프롬프트

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [복셀로 만든 호수](https://x.com/Angaisb_/status/2119947748690841841) (작성자 [@Angaisb_](https://x.com/Angaisb_))

**작은 환경을 소재로 구도를 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 만들었다고 밝힌 복셀 호수를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [Arena의 인터랙티브 생성 예시 17개](https://x.com/arena/status/2119948067449536733) (작성자 [@arena](https://x.com/arena))

**평가 과제를 고르기 전에 여러 종류의 결과를 살펴본다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ 동영상 재생</a>

Arena는 3D 세계, 게임, 인터페이스, 데이터 시각화, 코드 애니메이션 등 17개 생성 예시를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [친근한 용과 함께 비행](https://x.com/chetanankola/status/2119951015407738913) (작성자 [@chetanankola](https://x.com/chetanankola))

**반복 비행으로 카메라와 움직임을 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Three.js와 Blender로 만든 용 장면을 공유하고 Fable 5.2로 개선한 부분을 설명했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Fable과 Opus의 젤리 범고래](https://x.com/vib3coded/status/2119951060752375827) (작성자 [@vib3coded](https://x.com/vib3coded))

**같은 소재의 표면 질감과 움직임을 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2와 Opus 5.5의 젤리 범고래 결과를 나란히 공유했다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [자유 주제로 보는 영상 품질](https://x.com/suna_gaku/status/2119952985933697063) (작성자 [@suna_gaku](https://x.com/suna_gaku))

**폭넓은 지시를 주고 모델이 어떤 표현을 선택하는지 본다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 모델에 가장 자신 있는 영상 작업을 보여 달라고 요청하고 결과를 공유했다.

원본 프롬프트

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [지중해풍 우주 거주 시설](https://x.com/MaxXWilliamson/status/2119953172634677533) (작성자 [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**짧은 설계 지시와 기존 프로젝트 도구를 결합한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 이전 우주 거주 시설 작업에 썼던 도구를 제공하고 지중해풍 우주 정거장을 요청했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [AA-3D 인터랙티브 경험 벤치마크](https://x.com/ArtificialAnlys/status/2119953570430881946) (작성자 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Elo를 볼 때 불확실성 구간도 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ 동영상 재생</a>

Artificial Analysis는 인터랙티브 3D 평가에서 Fable 5.2 Max의 출시 시점 Elo가 1,271이었다고 보고했다.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [해골 캐릭터의 타임 챌린지](https://x.com/WesRoth/status/2119953913160093817) (작성자 [@WesRoth](https://x.com/WesRoth))

**화면에 타이머를 표시해 플레이 가능한 시제품을 평가한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 해골 캐릭터와 카운트다운이 나오는 Fable 5.2의 원샷 결과를 공개했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Fable과 Astra의 픽셀 아트 비교](https://x.com/Angaisb_/status/2119955179915137294) (작성자 [@Angaisb_](https://x.com/Angaisb_))

**같은 출력 크기에서 형태와 디테일을 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ 동영상 재생</a>

원본 비교에는 GPT-6 Astra와 Fable 5.2의 픽셀 아트가 함께 나온다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [모션 디자인 포트폴리오 영상](https://x.com/Leviwoyun/status/2119955625820258308) (작성자 [@Leviwoyun](https://x.com/Leviwoyun))

**자유도가 높은 포트폴리오 지시에 영상 길이를 지정한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 음악이 포함된 모션 디자인 영상을 공유하며 제작에 24분이 걸렸다고 밝혔다.

원본 프롬프트

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [두 모델의 유리 수영장 렌더링](https://x.com/MrTacticalX/status/2119955647542542439) (작성자 [@MrTacticalX](https://x.com/MrTacticalX))

**조명 품질을 실행 시간 및 비용과 함께 비교한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 이 렌더링 테스트에서 Fable이 90분에 57.87달러, Opus가 68분에 14.39달러였다고 밝혔다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [TS-Bench 도구 호출 정확도](https://x.com/gosrum/status/2119956559031927079) (작성자 [@gosrum](https://x.com/gosrum))

**도구 호출 오류와 토큰 사용량을 따로 기록한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

평가자는 Fable 5.2의 도구 호출 오류가 0건이었으며, 쉬운 과제로는 Claude 모델 간 차이를 가리기 어렵다고 밝혔다.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [미니어처 마추픽추](https://x.com/loktar00/status/2119958719362666708) (작성자 [@loktar00](https://x.com/loktar00))

**축소 장면에서 분위기와 작은 요소를 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ 동영상 재생</a>

공유된 마추픽추 데모에는 볼류메트릭 안개와 작은 알파카가 등장한다.

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [전문 작업 분야별 GDPx 결과](https://x.com/SemiAnalysis_/status/2119961447199289640) (작성자 [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**종합 점수와 세부 과제 결과를 함께 본다.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

평가 발표자는 종합 점수 16.4%를 보고하고 칩 설계와 소프트웨어 공학 등의 세부 결과를 제시했다.

[관련 자료 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [관련 자료 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [관련 자료 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [그림 앱에서 초상화 그리기](https://x.com/The_Alex/status/2119964472559489229) (작성자 [@The_Alex](https://x.com/The_Alex))

**참고용 썸네일을 바탕으로 초상화를 그리게 하세요.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ 동영상 재생</a>

작성자는 Fable 5.2에 그림 앱을 열고 자신의 초상화를 그려 달라고 했습니다. 영상에는 윤곽부터 완성까지의 과정이 담겨 있습니다.

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [추론 강도 Low의 VulcanBench Frontier v4](https://x.com/morganlinton/status/2119966067527467215) (작성자 [@morganlinton](https://x.com/morganlinton))

**서로 다른 세대의 모델을 같은 추론 강도에서 비교한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

평가 작성자에 따르면 Low에서 작업당 Fable 5.2는 약 5분, 5.1은 약 26분이 걸렸다.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [괴물을 조종하는 백룸 게임](https://x.com/LexnLin/status/2119966127149429093) (작성자 [@LexnLin](https://x.com/LexnLin))

**플레이어의 목표를 바꿔 게임 아이디어를 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ 동영상 재생</a>

플레이어는 괴물을 조종해 사람을 잡는다. 제작자는 플레이 영상과 체험 링크를 공유했다.

[관련 자료 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [Blender에서 만든 Bugatti Tourbillon](https://x.com/xikhar/status/2119966147328299284) (작성자 [@xikhar](https://x.com/xikhar))

**참고 이미지로 외장과 내장 디테일을 지정한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 프롬프트와 참고 이미지로 Bugatti Tourbillon의 실내까지 모델링해 영화풍 영상을 렌더링했다고 밝혔다.

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [두 모델로 제작한 컴퓨터 테마 영상](https://x.com/daradoescode/status/2119966154391183522) (작성자 [@daradoescode](https://x.com/daradoescode))

**여러 모델을 쓸 때 각 모델의 기여를 기록한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 Fable 5.2로 만든 스타일화 영상을 공유했으며, Opus 5.5도 제작에 크게 기여했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [Megakernel을 주제로 한 뮤직비디오](https://x.com/elliotarledge/status/2119968762069934415) (작성자 [@elliotarledge](https://x.com/elliotarledge))

**기술 개념을 영상 제작의 주제로 삼는다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 추론 강도 High에서 Fable 5.2에 Megakernel 뮤직비디오를 요청하고 영상을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [참고 사진으로 만든 스튜디오 투어](https://x.com/rpnickson/status/2119969928304357507) (작성자 [@rpnickson](https://x.com/rpnickson))

**실제 사진으로 장면 재현의 기준을 잡는다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 스튜디오 사진을 제공하고 비슷한 영상 제작 지시를 조정했으며, 실행에 약 2시간이 걸렸다고 밝혔다.

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [코드로 만든 1990년대풍 장난감 광고](https://x.com/kevin_t_ngo/status/2119972124211454139) (작성자 [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**애니메이션 스크립트 작성과 렌더링을 분리한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 복고풍 장난감 광고의 애니메이션을 Python으로 만들고 Blender로 렌더링했다고 밝혔다.

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Three.js 3인칭 게임 장면](https://x.com/bijanbowen/status/2119972220739187182) (작성자 [@bijanbowen](https://x.com/bijanbowen))

**실제 플레이 영상으로 움직임과 배경을 확인한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

작성자는 3인칭 캐릭터가 야외를 이동하는 Three.js 결과를 방송에서 공개했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [기존 렌더러로 만든 Bryceball](https://x.com/pleometric/status/2119973274402668852) (작성자 [@pleometric](https://x.com/pleometric))

**렌더링 엔진을 게임의 기반으로 재사용한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 관련 게시물에서 소개한 렌더러를 실제로 플레이할 수 있는 Bryceball로 개조했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [Fable로 편집한 영상을 다시 편집](https://x.com/rileybrown/status/2119973951027724385) (작성자 [@rileybrown](https://x.com/rileybrown))

**기존 편집본을 다음 영상의 소재로 활용한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 같은 모델로 이전에 편집한 영상을 다룬 새 Fable 5.2 편집본을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [영화처럼 보는 과학의 역사](https://x.com/DeryaTR_/status/2119974354260013293) (작성자 [@DeryaTR_](https://x.com/DeryaTR_))

**연대표를 바탕으로 3D 시퀀스를 구성한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 과학의 초기부터 상상 속 미래까지 영화처럼 보여 달라고 요청하고 완성 영상을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [다빈치 비행 장치의 3D 모델](https://x.com/higgsfield_ai/status/2119975721909301684) (작성자 [@higgsfield_ai](https://x.com/higgsfield_ai))

**역사적 설계를 모델링한 뒤 변경 사항을 시험한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ 동영상 재생</a>

Higgsfield는 다빈치의 비행 장치를 3D로 구현하고 물리 테스트와 재설계 과정을 소개했다.

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [설계 요구사항에 따른 PCB 배선](https://x.com/cmonkey/status/2119975852977029365) (작성자 [@cmonkey](https://x.com/cmonkey))

**제조 전에 기판 배선을 확인한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

작성자는 회로 배치 논의에 이어 Fable 5.2의 PCB 배선 결과를 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [서로 다른 실행 환경에 같은 프롬프트 적용](https://x.com/loktar00/status/2119980613369319706) (작성자 [@loktar00](https://x.com/loktar00))

**모델 결과를 비교할 때 실행 환경의 차이를 기록한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 다른 실행 환경에서 DeepSeek와 Fable 5.2에 같은 프롬프트를 주고 결과를 나란히 보여 줬다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [코드로 그린 고질라](https://x.com/chetaslua/status/2119981510199808368) (작성자 [@chetaslua](https://x.com/chetaslua))

**벡터풍 형태와 움직임으로 이미지를 재해석한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 고질라 게시물에서 영감을 받아 코드로 그린 그림과 짧은 애니메이션을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [3D 프린팅용 휴대용 선풍기](https://x.com/davelee/status/2119981787325579398) (작성자 [@davelee](https://x.com/davelee))

**실물 시제품으로 모델링한 조립 구조를 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 아이들과 함께 출력 가능한 휴대용 선풍기를 설계하고, 출력 전에 모델을 공유했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [Opus와 비교한 플러그인 버그 조사](https://x.com/oaranda/status/2119982729747919096) (작성자 [@oaranda](https://x.com/oaranda))

**교차 회귀 테스트로 수정 결과를 비교한다.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

작성자가 주석을 단 발표문 발췌입니다.

두 모델은 동일한 플러그인 버그 6건을 찾았다. Opus는 교차 테스트를 모두 통과했고, Fable은 1건을 통과하지 못했지만 별도의 대시보드 문제도 발견했다.

원본 프롬프트

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [3D 장면으로 재현한 이스탄불](https://x.com/petergostev/status/2119877733488394520) (작성자 [@petergostev](https://x.com/petergostev))

**도시 규모 장면을 원경과 근경에서 각각 확인한다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ 동영상 재생</a>

Peter Gostev는 Fable 5.2 Max의 이스탄불 3D 결과를 공개하고 자세한 평가 링크를 첨부했다.

[관련 자료 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [화면까지 움직이는 Blender 스튜디오 영상](https://x.com/rileybrown/status/2119902109709537708) (작성자 [@rileybrown](https://x.com/rileybrown))

**한 3D 장면에서 화면, 조명, 카메라를 모두 움직인다.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ 동영상 재생</a>

제작자는 카메라 숏 13개, 노트북에서 재생되는 맞춤 웹페이지, ElevenLabs 오디오를 사용했다고 밝혔다. 렌더링에는 RunPod GPU를 사용했다.

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [약결합 영역에서의 블랙홀 전이](https://hexagonmath.org/2611.00175v1) (작성자 [@Anthropic](https://www.anthropic.com/))

**원래 이론 설정을 기준으로 미완성 계산을 확인한다.**

Anthropic은 Fable 5.2가 오랫동안 미완성이던 계산을 마치고 약결합 영역에서 급격한 전이를 발견했다고 밝혔다. 프리프린트에 유도 과정이 실려 있다.

[관련 자료 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [모듈러 부트스트랩 경계의 한계](https://hexagonmath.org/2611.00174v1) (작성자 [@Anthropic](https://www.anthropic.com/))

**해석적으로 얻은 경계를 제시할 때 유도 과정도 공개한다.**

Anthropic은 Fable 5.2가 단순화한 양자 중력 설정에서 스핀 없는 모듈러 부트스트랩 기법의 정확한 한계를 구했다고 밝혔다.

[관련 자료 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Vercel AI Gateway의 순서 지정 모델 폴백](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (작성자 [Vercel](https://vercel.com/))

**분류기가 거부한 요청에 대해 게이트웨이의 폴백 순서를 지정한다.**

Vercel의 AI SDK 예제는 anthropic/claude-fable-5.2를 호출하고 Opus 5.5, Sonnet 5.5 순으로 폴백을 설정한다. 가이드는 게이트웨이의 데이터 보존 요건을 설명한다.

[관련 자료 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [중첩 하위 에이전트와 검토 예산](https://news.ycombinator.com/item?id=50430925) (작성자 [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**중첩 위임을 추적하고 프롬프트 외부에서 검토 예산을 제한한다.**

작성자는 80,000줄의 코드 검토에 하위 에이전트를 최대 4개만 사용하라고 요청했다. 실제로는 중첩 에이전트가 6개 이상 생겼고 20분도 되기 전에 5시간 사용량 한도를 소진했다고 밝혔다.

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [LCARS 디자인을 HTML로 변환한 비교](https://news.ycombinator.com/item?id=50430962) (작성자 [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**곡선, 아이콘 재현도, 애니메이션, 탐색을 각각 인수 기준으로 삼는다.**

작성자는 같은 스타 트렉풍 디자인으로 Fable 5.2와 Opus 5.5를 비교했다. 곡선과 일부 아이콘은 Fable을, 움직임은 Opus를 선호했으며 Fable의 SVG 깜빡임이 거슬렸다고 밝혔다. 첫 페이지에 한해 요청한 작업이었다.

[관련 자료 1](https://html.non.io/lcars-fable-5.2/) · [관련 자료 2](https://html.non.io/lcars-opus-5.5/) · [관련 자료 3](https://news.ycombinator.com/item?id=50431231) · [관련 자료 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [Quantum ESPRESSO의 GPU 최적화](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (작성자 [Discovered Materials](https://discoveredmaterials.com/))

**과학 계산 코드를 최적화할 때 참조 결과와 대표적인 비공개 테스트를 요구한다.**

Discovered Materials는 같은 GPU에서 포논 벤치마크 13개 속도 향상의 기하 평균이 36배였고 혼성 범함수 계산은 약 9배 빨라졌다고 보고했다. 공개 패치는 정확성과 성능 테스트를 바탕으로 한다.

[관련 자료 1](https://github.com/discovered-materials/dm_qe) · [관련 자료 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [추론 강도별 Artificial Analysis Intelligence Index](https://artificialanalysis.ai/models/claude-fable-5-2) (작성자 [Artificial Analysis](https://artificialanalysis.ai/))

**선택한 추론 강도에서 점수, 작업 비용, 지연 시간을 함께 읽는다.**

인용된 기본 폴백 Max 스냅샷은 지수 65, 작업당 26.54달러와 46.4분을 기록했다. 수치는 해당 벤치마크 작업의 결과다.

[관련 자료 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [High 설정의 변경 검토에서 나온 오탐](https://news.ycombinator.com/item?id=50431810) (작성자 [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**모델이 지적한 문제는 조치 전에 코드와 대조한다.**

개발자에 따르면 Fable 5.2 High가 변경 검토에서 존재하지 않는 문제 2개를 지적했고 개발자가 코드에 대한 이해를 바탕으로 오류를 발견했다.

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [일상적인 코딩 과제 30개](https://news.ycombinator.com/item?id=50432483) (작성자 [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**같은 코딩 작업에서 소요 시간과 성공 건수를 측정한다.**

작성자에 따르면 Fable 5.2와 Opus 5.5는 30개 중 26개, Fable 5.1은 25개를 해결했다. Fable 5.2의 소요 시간은 5.1의 0.62배였으며 안전장치로 인한 중단은 보고되지 않았다.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [무인도 화면 보호기](https://news.ycombinator.com/item?id=50432836) (작성자 [@nzach](https://news.ycombinator.com/user?id=nzach))

**직접 조작할 수 있는 페이지에서 모델이 만든 화면 보호기를 확인한다.**

Show HN 작성자는 Stranded with Claude라는 브라우저 섬 장면을 공개했다. 결과물은 인터랙티브 캔버스다.

[관련 자료 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [추론 강도 High의 브라우저 게임 3개](https://senko.net/vibecode-bench/) (작성자 [Senko Rašić](https://senko.net/))

**게임 평가에서 플레이 방식과 시각적 재현도를 따로 비교한다.**

Senko Rašić는 Claude Code의 Fable 5.2로 RTS, 복셀, 비행 시뮬레이터 지시를 실행했다. 지도를 모두 탐험할 수 있는 비행선 등 더 깊은 게임 요소가 추가됐지만 그래픽 일부는 더 아쉬웠다고 밝혔다.

[관련 자료 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [책의 장별 팟캐스트 대본](https://news.ycombinator.com/item?id=50434156) (작성자 [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**같은 팟캐스트 과제에서 대본 길이를 비교한다.**

작성자는 장마다 두 서평가의 대화를 생성했다. Fable 버전은 약 2.5쪽, Opus 5.5 버전은 약 4.5쪽이었다고 밝히고 두 샘플을 링크했다.

[관련 자료 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [관련 자료 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [Rust로 이전한 운영 서비스](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (작성자 [@Anthropic](https://www.anthropic.com/))

**이전 전후의 시작 성능을 측정한다.**

Anthropic에 따르면 출시 전 Fable 5.2를 실행한 에이전트들이 운영 중인 Python 서비스를 Rust로 다시 작성해 시작 시간을 약 26분의 1로 줄였다.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [GitHub Copilot에서 Fable 5.2 선택](https://x.com/github/status/2119926269982961833) (작성자 [@github](https://x.com/github))

**모델을 고르기 전에 조직 정책을 활성화하세요.**

GitHub는 Copilot 클라이언트의 모델 선택기와 Business 및 Enterprise 계정에 필요한 관리자 설정을 안내합니다.

[관련 자료 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [HTML 100페이지 디자인 도전](https://x.com/MiaAI_lab/status/2119930229661503893) (작성자 [@MiaAI_lab](https://x.com/MiaAI_lab))

**시각적 품질과 함께 완성되고 실행 가능한 파일 수를 센다.**

작성자는 서로 다른 디자인 100개를 요청해 프롬프트와 함께 파일 76개를 공개했다. Fable의 사용량 한도에 도달했다고 밝혔다.

[관련 자료 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [관련 자료 2](https://mia-ai.net/lab/experiments/100-htmls) · [관련 자료 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [관련 자료 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [관련 자료 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [관련 자료 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [관련 자료 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [관련 자료 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [관련 자료 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [관련 자료 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [관련 자료 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [관련 자료 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [관련 자료 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [관련 자료 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [컴파일러 작업에서 요구사항이 달라진 사례](https://x.com/sameQCU/status/2119939304864800971) (작성자 [@sameQCU](https://x.com/sameQCU))

**에이전트가 설명하는 요구사항을 원래 입력과 대조한다.**

개발자는 Fable 5.2와 이전 Opus 모델들이 전달받은 요구사항을 잘못 설명한 컴파일러 작업을 소개했다.

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [Opus로 긴 Fable 작업의 진행 상황 확인](https://x.com/marouane53/status/2119950129767858262) (작성자 [@marouane53](https://x.com/marouane53))

**별도의 세션에서 긴 작업의 진행 상황을 확인하세요.**

작성자는 일부 Fable 작업이 진행 알림이 드문 채 두 시간 넘게 실행됐다고 설명합니다. 별도 대화의 Opus 5.5로 진행 상황과 판단을 해석했습니다.

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [새로운 시각으로 코드를 재검토](https://x.com/doodlestein/status/2119958895158292786) (작성자 [@doodlestein](https://x.com/doodlestein))

**새 파일과 수정한 파일을 별도 검토 단계에서 확인한다.**

제작자는 구현 후 실수를 찾아 고치는 데 사용한 후속 프롬프트 2개의 원문을 공유했다.

원본 프롬프트

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

원본 프롬프트

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [기능 설계 검토에서 조언이 빗나간 사례](https://news.ycombinator.com/item?id=50434214) (작성자 [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**현재 설계를 체크리스트로 삼아 에이전트의 후속 조언을 검토한다.**

작성자는 기능 설계 검토에서 모델을 비교하고 Opus 5.5를 선호했다. 이후 Fable 5.2 진단에서는 설계에 이미 반영된 내용을 다시 제안했다.

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [DX Ball 스타일 벽돌 깨기 비교](https://news.ycombinator.com/item?id=50434424) (작성자 [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**같은 재현 과제에서 게임 방식과 조작감을 따로 비교한다.**

작성자는 별도로 실행한 Fable 5.2와 Opus 5.5 버전의 링크를 공유했다. Fable은 원작의 게임 방식을 일부 바꿨고 작성자는 Opus 버전의 조작감을 선호했다.

[관련 자료 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [관련 자료 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [3D 앱 개선 실험](https://news.ycombinator.com/item?id=50434433) (작성자 [@user43928](https://news.ycombinator.com/user?id=user43928))

**같은 개선 과제에서 눈에 보이는 변화와 예산 소모를 비교한다.**

작성자는 게임이 아닌 3D 앱을 Fable 5.2로 개선해 달라고 요청했다. Opus 5.5와 차이가 거의 없었으며 그날 저녁 Fable 플랜 사용량의 25%를 소모했다고 밝혔다.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [세 모델이 만든 고양이와 생쥐 게임](https://news.ycombinator.com/item?id=50434508) (작성자 [@simonw](https://news.ycombinator.com/user?id=simonw))

**게임 프롬프트를 고정하고 각 모델의 플레이 가능한 구현을 확인한다.**

Simon Willison은 Fable 5.2 Extra, Opus 5.5 Extra, GPT-6 Extra High로 만든 모바일 친화적 Three.js 게임을 공유했다. Fable 결과에는 약 40분이 걸렸다고 밝혔다.

[관련 자료 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [관련 자료 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [관련 자료 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

원본 프롬프트

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [AIBenchy의 추론 강도 High 비용 및 점수 비교](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (작성자 [AIBenchy](https://aibenchy.com/))

**같은 추론 강도 레이블에서 점수, 총비용, 응답 시간을 비교한다.**

AIBenchy의 공개 결과에서 Fable 5.2 High와 Opus 5.5 High는 각각 점수 8.7과 9.4, 총비용 5.083달러와 2.133달러, 평균 응답 시간 14.73초와 27.55초를 기록했다.

[관련 자료 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [Fable 5.2 에이전트 실행 환경 조정](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (작성자 [@Anthropic](https://www.anthropic.com/))

**추론 강도를 다시 테스트하고 긴 작업의 진행 알림 규칙을 정하세요.**

Anthropic의 가이드는 추론 강도, 완료 기준, 승인, 진행 알림, 하위 에이전트 제한을 지시문 예시와 함께 다룹니다.

[관련 자료 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="acknowledge"></a>
## 작성자 크레딧

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/)
