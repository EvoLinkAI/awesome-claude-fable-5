# Casos de uso do Claude Fable 5.2

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

Fluxos de trabalho, demonstrações, comparações, avaliações, integrações e limites práticos das coletâneas de 10 e de 13 a 14 de novembro, com links para as fontes.

[Anúncio da Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [Coleção anterior](../../README_pt.md)

## Índice de casos

| Case | Casos de uso | Type |
| --- | --- | --- |
| 330 | [Desenho de MacBook em SVG em vários níveis de esforço](#case-330) | Benchmark |
| 331 | [Um jogo de luta para quatro a partir de desenhos da família](#case-331) | Demo |
| 332 | [Três dispositivos eletrônicos, do projeto à montagem](#case-332) | Demo |
| 333 | [Formalização do Último Teorema de Fermat em Lean](#case-333) | Evaluation |
| 334 | [Um sistema operacional a partir de uma pasta vazia](#case-334) | Demo |
| 335 | [Manipulação com dois braços no RoboDojo](#case-335) | Benchmark |
| 336 | [Uma fonte em movimento](#case-336) | Demo |
| 337 | [Sincronização labial quadro a quadro com Higgsfield](#case-337) | Integration |
| 338 | [Protótipo de direção em mundo aberto](#case-338) | Demo |
| 339 | [Paris em 1940 com imagens de referência](#case-339) | Integration |
| 340 | [Fable planeja um curta renderizado pelo Opus](#case-340) | Integration |
| 341 | [Um experimento de clipe musical](#case-341) | Demo |
| 342 | [Retrato pintado de Dario Amodei](#case-342) | Demo |
| 343 | [Spud Smash com esforço Medium](#case-343) | Demo |
| 344 | [Catedral de gelo com Fable e Opus](#case-344) | Evaluation |
| 345 | [Canto com tratos vocais simulados](#case-345) | Demo |
| 346 | [Três testes de voxels em Istambul](#case-346) | Evaluation |
| 347 | [Projetos concluídos no Remote Labor Index](#case-347) | Benchmark |
| 348 | [Cena de iceberg em quatro níveis de esforço](#case-348) | Evaluation |
| 349 | [Um curta de anime de setenta e nove segundos](#case-349) | Demo |
| 350 | [Conjuntos mecânicos com Fable e Opus](#case-350) | Evaluation |
| 351 | [Uma mão robótica subindo uma escada em espiral](#case-351) | Demo |
| 352 | [Rigging de uma malha do Tripo no Blender](#case-352) | Evaluation |
| 353 | [Invenções interativas do caderno de Da Vinci](#case-353) | Demo |
| 354 | [Uma estação de áudio controlada pelo Claude](#case-354) | Demo |
| 355 | [Um Raspberry Pi 5 animado](#case-355) | Demo |
| 356 | [Uma cena do norte da Itália](#case-356) | Demo |
| 357 | [Livro pop-up com agentes de execução locais](#case-357) | Evaluation |
| 358 | [Retorno do teste da luminária de lava](#case-358) | Evaluation |
| 359 | [Um jato detalhado modelado no Blender](#case-359) | Integration |
| 360 | [Uma viagem por portais entre centenas de mundos](#case-360) | Demo |
| 361 | [Um bazar de Bombaim em seis planos com Three.js](#case-361) | Integration |
| 362 | [Uma lanchonete fotorrealista feita em código](#case-362) | Integration |
| 363 | [Um modelo de robô no Blender](#case-363) | Demo |
| 364 | [Animação explicativa para Convex](#case-364) | Demo |
| 365 | [Coleção de landing pages feitas com um único prompt](#case-365) | Demo |
| 366 | [Uma sonata para piano escrita em LilyPond](#case-366) | Demo |
| 367 | [Um briefing de vídeo livre](#case-367) | Demo |
| 368 | [Fable planeja, DeepSeek implementa e Opus revisa](#case-368) | Integration |
| 369 | [Fable 5.2 no AI Village](#case-369) | Integration |
| 370 | [Design de frontend com e sem skills](#case-370) | Evaluation |
| 371 | [Como encontrar máquinas de estado implícitas](#case-371) | Tutorial |
| 372 | [Um jogo criado do zero em oito horas](#case-372) | Demo |
| 373 | [Protótipo de Fishslop e custo em tokens](#case-373) | Evaluation |
| 374 | [Um jogo de futebol americano em movimento](#case-374) | Demo |
| 375 | [Batalha de chefe em mundo aberto com Higgsfield MCP](#case-375) | Integration |
| 376 | [Mont Saint-Michel e as marés](#case-376) | Demo |
| 377 | [Um recurso de Roblox no Blender](#case-377) | Demo |
| 378 | [Raciocínio sem exibir cadeia de pensamento](#case-378) | Benchmark |
| 379 | [Versões do Chrome Dino com quatro modelos](#case-379) | Evaluation |
| 380 | [Jogo de damas com um braço robótico](#case-380) | Demo |
| 381 | [Uma animação gráfica de quinze segundos](#case-381) | Demo |
| 382 | [Uma Torre Eiffel jogável](#case-382) | Demo |
| 383 | [Corrida em alto-mar com Three.js e Higgsfield](#case-383) | Integration |
| 384 | [Simulação de mel em tempo real com WebGL](#case-384) | Demo |
| 385 | [Efeitos visuais programados sobre vídeo](#case-385) | Demo |
| 386 | [Explicação animada dos níveis de procura em GTA](#case-386) | Demo |
| 387 | [Um mundo de MMO estilizado feito em código](#case-387) | Demo |
| 388 | [Uma cena 3D com Fable e Opus](#case-388) | Evaluation |
| 389 | [Texto redundante na tela de pausa de um jogo](#case-389) | Limit |
| 390 | [Painéis de inspiração em um ambiente Krea](#case-390) | Integration |
| 391 | [Teste de um jogo de tiro com portais no escritório](#case-391) | Demo |
| 392 | [Objeto detalhado de superfície rígida no Blender](#case-392) | Demo |
| 393 | [Testes paralelos de frontend em vários níveis de esforço](#case-393) | Evaluation |
| 394 | [Um jogo pequeno em dez prompts](#case-394) | Demo |
| 395 | [Animação quadro a quadro com JavaScript](#case-395) | Demo |
| 396 | [De vídeo de referência a animação 3D](#case-396) | Demo |
| 397 | [Fogueira em pixel art com Fable e Opus](#case-397) | Evaluation |
| 398 | [Arena WebDev com esforço xHigh](#case-398) | Benchmark |
| 399 | [Tipografia de trailer com dois modelos](#case-399) | Evaluation |
| 400 | [Testes de motion e portfólio 3D com um só prompt](#case-400) | Evaluation |
| 401 | [Explicação interativa de um reator nuclear](#case-401) | Demo |
| 402 | [Agentes no Blood on the Clocktower](#case-402) | Benchmark |
| 403 | [Protótipo de corrida de pods](#case-403) | Demo |
| 404 | [Comercial de roupa íntima do Claude em dez segundos](#case-404) | Demo |
| 405 | [Um pássaro ao nascer do sol, traço a traço](#case-405) | Demo |
| 406 | [Uma execução gráfica longa no Devin](#case-406) | Evaluation |
| 407 | [Pintura em código com três modelos](#case-407) | Evaluation |
| 408 | [A história da escrita em movimento](#case-408) | Demo |
| 409 | [Campo de testes para máquinas de jogo](#case-409) | Demo |
| 410 | [PCB para um console portátil Linux](#case-410) | Evaluation |
| 411 | [Um lago de voxels](#case-411) | Demo |
| 412 | [As 17 gerações interativas da Arena](#case-412) | Demo |
| 413 | [Voo com um dragão amistoso](#case-413) | Demo |
| 414 | [Orca de gelatina com Fable e Opus](#case-414) | Evaluation |
| 415 | [Teste aberto de qualidade de vídeo](#case-415) | Demo |
| 416 | [Habitat espacial de inspiração mediterrânea](#case-416) | Demo |
| 417 | [Benchmark AA-3D de experiências interativas](#case-417) | Benchmark |
| 418 | [Desafio cronometrado com um personagem esquelético](#case-418) | Demo |
| 419 | [Pixel art com Fable e Astra](#case-419) | Evaluation |
| 420 | [Reel de portfólio de motion design](#case-420) | Demo |
| 421 | [Renderização de uma piscina de vidro com dois modelos](#case-421) | Evaluation |
| 422 | [Precisão de chamadas a ferramentas no TS-Bench](#case-422) | Benchmark |
| 423 | [Machu Picchu em miniatura](#case-423) | Demo |
| 424 | [GDPx por categoria de trabalho profissional](#case-424) | Benchmark |
| 425 | [Um retrato em um aplicativo de desenho](#case-425) | Demo |
| 426 | [VulcanBench Frontier v4 com esforço Low](#case-426) | Benchmark |
| 427 | [Inversão de papéis em um Backrooms jogável](#case-427) | Demo |
| 428 | [Bugatti Tourbillon no Blender](#case-428) | Demo |
| 429 | [Um vídeo sobre computadores feito com dois modelos](#case-429) | Demo |
| 430 | [Um clipe musical sobre megakernels](#case-430) | Demo |
| 431 | [Visita ao estúdio a partir de fotos de referência](#case-431) | Demo |
| 432 | [Um comercial de brinquedos dos anos 1990 feito em código](#case-432) | Demo |
| 433 | [Cena de jogo em terceira pessoa com Three.js](#case-433) | Demo |
| 434 | [Bryceball a partir de um renderizador existente](#case-434) | Demo |
| 435 | [Edição recursiva de vídeo com Fable](#case-435) | Demo |
| 436 | [Uma história cinematográfica da ciência](#case-436) | Demo |
| 437 | [Máquina voadora de Da Vinci em 3D](#case-437) | Integration |
| 438 | [Roteamento de PCB a partir de um projeto](#case-438) | Demo |
| 439 | [Um mesmo prompt em ambientes diferentes](#case-439) | Evaluation |
| 440 | [Ilustração do Godzilla desenhada com código](#case-440) | Demo |
| 441 | [Ventilador de mão para impressão 3D](#case-441) | Demo |
| 442 | [Busca de bugs em um plugin contra o Opus](#case-442) | Evaluation |
| 443 | [Istambul recriada em uma cena 3D](#case-443) | Demo |
| 444 | [Um filme no Blender com uma tela funcional](#case-444) | Demo |
| 445 | [Uma transição de buracos negros em acoplamento fraco](#case-445) | Evaluation |
| 446 | [O limite de uma cota do bootstrap modular](#case-446) | Evaluation |
| 447 | [Vercel AI Gateway com modelos alternativos em ordem](#case-447) | Integration |
| 448 | [Subagentes aninhados e orçamento de revisão](#case-448) | Limit |
| 449 | [Comparação de um design LCARS convertido em HTML](#case-449) | Evaluation |
| 450 | [Otimização para GPU no Quantum ESPRESSO](#case-450) | Benchmark |
| 451 | [Índice de inteligência da Artificial Analysis por esforço](#case-451) | Benchmark |
| 452 | [Falsos positivos na revisão de mudanças com esforço High](#case-452) | Limit |
| 453 | [Trinta tarefas rotineiras de programação](#case-453) | Evaluation |
| 454 | [Protetor de tela de um náufrago em uma ilha](#case-454) | Demo |
| 455 | [Três jogos de navegador com esforço High](#case-455) | Evaluation |
| 456 | [Roteiros de podcast de livros por capítulo](#case-456) | Evaluation |
| 457 | [Um serviço de produção migrado para Rust](#case-457) | Evaluation |
| 458 | [Selecionar o Fable 5.2 no GitHub Copilot](#case-458) | Integration |
| 459 | [Desafio de design de cem páginas HTML](#case-459) | Evaluation |
| 460 | [Desvio de requisitos em um compilador](#case-460) | Limit |
| 461 | [Acompanhar uma tarefa longa do Fable com Opus](#case-461) | Integration |
| 462 | [Revisão de código com um olhar novo](#case-462) | Tutorial |
| 463 | [Perda de contexto na revisão de um recurso](#case-463) | Limit |
| 464 | [Comparação de Breakout no estilo DX Ball](#case-464) | Evaluation |
| 465 | [Teste de melhoria em um aplicativo 3D](#case-465) | Evaluation |
| 466 | [Jogo do rato e do gato em três modelos](#case-466) | Evaluation |
| 467 | [Custo e pontuação no AIBenchy com esforço High](#case-467) | Benchmark |
| 468 | [Ajustar o ambiente de agentes do Fable 5.2](#case-468) | Tutorial |
| 469 | [Um aplicativo para visualizar personagens animados](#case-469) | Demo |
| 470 | [Teste de um código QR criado sem ferramentas](#case-470) | Evaluation |
| 471 | [Um jogo de zumbis no Unity com o Tripo](#case-471) | Demo |
| 472 | [Uma rua nevada pintada no MS Paint](#case-472) | Demo |
| 473 | [Um cabo fora da tomada no Wojak-Bench](#case-473) | Limit |
| 474 | [Um arranjo de piano para um jogo de ritmo](#case-474) | Evaluation |
| 475 | [Redesenho da recuperação de tokens no Picnic](#case-475) | Demo |
| 476 | [Edição de uma abertura de anime com clipes gerados](#case-476) | Tutorial |
| 477 | [Animação de personagem com três ferramentas](#case-477) | Demo |
| 478 | [Renderização de um trailer urbano com scripts do Blender](#case-478) | Demo |
| 479 | [Cenas noturnas desenhadas com JavaScript](#case-479) | Demo |
| 480 | [De modelos CAD a desenhos técnicos](#case-480) | Demo |
| 481 | [As 43 tarefas do teste de análise do Plotly](#case-481) | Benchmark |
| 482 | [Uma estação SGI Indy recriada como site](#case-482) | Demo |
| 483 | [Coordenação de agentes com issues e worktrees](#case-483) | Integration |
| 484 | [Verificação de citações com agentes em segundo plano](#case-484) | Integration |
| 485 | [Depuração de um modelo de frete de ida e volta](#case-485) | Limit |
| 486 | [Adaptação da inferência do Edge0 para Mac](#case-486) | Integration |
| 487 | [Revisão de placas de circuito de alta densidade](#case-487) | Limit |
| 488 | [Rastreamento de uma citação em um jornal pago](#case-488) | Limit |
| 489 | [Planejamento com o Fable e revisão das mudanças do Opus](#case-489) | Tutorial |

<a id="fable-5-2-cases"></a>
## Casos de uso

<a id="case-330"></a>
### Case 330: [Desenho de MacBook em SVG em vários níveis de esforço](https://playcode.io/blog/macbook-svg-benchmark#compare) (por [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**Compare desenho, tokens e teto de saída sob o mesmo briefing.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

O Playcode informa 76.158 tokens por US$ 3,05 para Fable 5.2 High. Xhigh e Max atingiram o teto de 128 mil tokens em streaming sem gerar o desenho e terminaram com mais espaço na Batch API. A classificação segue o julgamento visual do editor.

[Material relacionado 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [Um jogo de luta para quatro a partir de desenhos da família](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (por [Lex](https://notesbylex.com/))

**Forneça esboços, um protótipo anterior e requisitos claros de controle ao agente.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex usou Claude Code para reconstruir um jogo de rolagem lateral como um beat ’em up de 12 fases e 18 personagens. Ferramentas de imagem e áudio forneceram os recursos. Quatro controles funcionaram nos testes em família.

[Material relacionado 1](https://aidens-revenge.pages.dev/) · [Material relacionado 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [Material relacionado 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [Três dispositivos eletrônicos, do projeto à montagem](https://www.anthropic.com/research/claude-electronics-design) (por [@Anthropic](https://www.anthropic.com/))

**Verifique circuito, gabinete e firmware como um sistema.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ Reproduzir vídeo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic e Diode relatam três dispositivos funcionais. Fable 5.2 roteou placas, modelou gabinetes, escreveu software e orientou os testes após a fabricação.

[Material relacionado 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [Material relacionado 2](https://www.youtube.com/watch?v=vdYynH177h0) · [Material relacionado 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [Formalização do Último Teorema de Fermat em Lean](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (por [@Anthropic](https://www.anthropic.com/))

**Use um verificador de provas e enunciados intermediários como marcos.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

A Anthropic relata que mil agentes Fable 5.2 formalizaram a prova existente em 30 horas. Com a mesma configuração de equipe, Opus 5.5 chegou a 26% em 18 horas.

[Material relacionado 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [Material relacionado 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [Um sistema operacional a partir de uma pasta vazia](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (por [@Anthropic](https://www.anthropic.com/))

**Verifique separadamente inicialização, drivers, armazenamento e instalação.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Anthropic relata que Fable 5.2 coordenou mais de mil subagentes durante oito dias para criar um protótipo de sistema operacional que inicializou em um notebook.

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [Manipulação com dois braços no RoboDojo](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (por [@Anthropic](https://www.anthropic.com/))

**Compare os modelos nas mesmas tarefas simuladas de manipulação.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Anthropic informa 64,9% para Fable 5.2 contra 27,6% para Fable 5.1 no RoboDojo. O anúncio inclui uma demonstração robótica.

[Material relacionado 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [Uma fonte em movimento](https://x.com/Angaisb_/status/2119909059277238733) (por [@Angaisb_](https://x.com/Angaisb_))

**Use o fluxo contínuo de água para avaliar o ritmo visual.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

O autor compartilha uma cena de fonte atribuída ao Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [Sincronização labial quadro a quadro com Higgsfield](https://x.com/higgsfield_ai/status/2119909938969580024) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Alinhe os tempos por quadro antes de revisar o vídeo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Higgsfield relata que rastreou a boca e alinhou o áudio aos quadros em seu fluxo com Fable 5.2.

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [Protótipo de direção em mundo aberto](https://x.com/ericmaskfr/status/2119910195325481026) (por [@ericmaskfr](https://x.com/ericmaskfr))

**Teste um briefing curto de mundo aberto em um trecho jogável.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um jogo inspirado em GTA e relata uma execução de cerca de 2 h 14 min.

Prompt original

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [Paris em 1940 com imagens de referência](https://x.com/higgsfield_ai/status/2119910344998912507) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Separe a geração de imagens de referência do código da cena.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Higgsfield forneceu as referências por seu MCP e usou Fable 5.2 para uma cena em Three.js.

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable planeja um curta renderizado pelo Opus](https://x.com/kloss_xyz/status/2119910613828980846) (por [@kloss_xyz](https://x.com/kloss_xyz))

**Separe planejamento de implementação no fluxo de vídeo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ Reproduzir vídeo</a>

Fable 5.2 redigiu o briefing e o plano. Opus 5.5 criou a animação de 16 segundos em Blender e Python e sintetizou a trilha.

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [Um experimento de clipe musical](https://x.com/WesRoth/status/2119911161386934330) (por [@WesRoth](https://x.com/WesRoth))

**Revise a letra e a sequência gerada.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um clipe feito com Fable 5.2 e comenta a letra.

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Retrato pintado de Dario Amodei](https://x.com/Mr_Salio/status/2119911922577637543) (por [@Mr_Salio](https://x.com/Mr_Salio))

**Compare um retrato estilizado com a referência exibida ao lado.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um retrato de Dario Amodei atribuído ao Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [Spud Smash com esforço Medium](https://x.com/argofowl/status/2119913148929187960) (por [@argofowl](https://x.com/argofowl))

**Dê ao protótipo ações e um objetivo claros.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra uma batata que dá socos, cabeçadas ou incendeia cadeiras azuis.

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Catedral de gelo com Fable e Opus](https://x.com/QQTeng/status/2119913518015435103) (por [@QQTeng](https://x.com/QQTeng))

**Compare tempo de geração e custo para a mesma cena.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor relata cerca de 1 h 57 min e US$ 81,10 para Fable, contra aproximadamente 3 h 11 min e US$ 45,97 para Opus.

Prompt original

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [Canto com tratos vocais simulados](https://x.com/banteg/status/2119914098171199996) (por [@banteg](https://x.com/banteg))

**Use um modelo físico da voz como insumo para produção musical.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra uma versão feita com duas simulações de trato vocal Chimera e uma mixagem com vocoder.

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [Três testes de voxels em Istambul](https://x.com/Avenoxai/status/2119914308603953485) (por [@Avenoxai](https://x.com/Avenoxai))

**Compare uma demolição, um relógio funcional e um mapa.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra três testes de um único prompt e atribui notas de 100, 100 e 95,6 segundo seu próprio critério.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Projetos concluídos no Remote Labor Index](https://x.com/ScaleAILabs/status/2119914701736075489) (por [@ScaleAILabs](https://x.com/ScaleAILabs))

**Interprete a taxa com base nos projetos avaliados.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ Reproduzir vídeo</a>

Scale Labs e CAIS relatam que Fable 5.2 concluiu com sucesso 41,3% dos projetos de trabalho remoto avaliados.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [Cena de iceberg em quatro níveis de esforço](https://x.com/0xRhinoX/status/2119915121698840587) (por [@0xRhinoX](https://x.com/0xRhinoX))

**Compare conclusão, custo e detalhe conforme o esforço aumenta.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor usou o mesmo prompt nos quatro níveis. High deixou de fora a aurora, e Ultra acrescentou gelo luminoso e uma vista subaquática.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [Um curta de anime de setenta e nove segundos](https://x.com/anstapnever/status/2119915123070644263) (por [@anstapnever](https://x.com/anstapnever))

**Inspecione a continuidade de cenas em uma animação mais longa.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha um clipe de anime de 79 segundos atribuído a um fluxo com Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Conjuntos mecânicos com Fable e Opus](https://x.com/ivanainai/status/2119915243321397550) (por [@ivanainai](https://x.com/ivanainai))

**Compare como cada modelo organiza as peças do conjunto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra renderizações identificadas do Fable 5.2 e do Opus 5.5 de uma vista explodida de roda e engrenagens.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [Uma mão robótica subindo uma escada em espiral](https://x.com/Luckyballa/status/2119915557663506720) (por [@Luckyballa](https://x.com/Luckyballa))

**Use um obstáculo simulado para avaliar uma locomoção incomum.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um teste com Fable 5.2 e Steel 0.1 de uma mão Wuji andando sobre os dedos.

[Material relacionado 1](https://github.com/skild-ai/steel-webgpu/pull/7)

Prompt original

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [Rigging de uma malha do Tripo no Blender](https://x.com/0xKense1/status/2119916096098582566) (por [@0xKense1](https://x.com/0xKense1))

**Faça verificações numéricas de pegada, textura e deformação.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compara dois rigs baseados em recursos do Tripo. Fable produziu dois clipes em 36 minutos e Opus oito em cerca de 21 minutos.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [Invenções interativas do caderno de Da Vinci](https://x.com/alexalbert__/status/2119916954337349737) (por [@alexalbert__](https://x.com/alexalbert__))

**Use desenhos originais como referência para um modelo educacional interativo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ Reproduzir vídeo</a>

Alex Albert forneceu um PDF do caderno de Leonardo e mostrou uma interpretação interativa de suas invenções.

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [Uma estação de áudio controlada pelo Claude](https://x.com/The_Alex/status/2119917226769985785) (por [@The_Alex](https://x.com/The_Alex))

**Use uma ferramenta controlada por agente para pedidos recorrentes de composição.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra uma estação de áudio digital criada com Fable 5.2 e relata que Opus a abriu depois para compor uma música.

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [Um Raspberry Pi 5 animado](https://x.com/sparklabhq/status/2119917375080521921) (por [@sparklabhq](https://x.com/sparklabhq))

**Use uma animação de produto para inspecionar componentes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha um Raspberry Pi 5 animado com Fable 5.2.

Prompt original

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [Uma cena do norte da Itália](https://x.com/Angaisb_/status/2119917807119089926) (por [@Angaisb_](https://x.com/Angaisb_))

**Observe a paisagem e a atmosfera em um briefing inspirado em um local.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha uma cena do Fable 5.2 ambientada no norte da Itália.

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [Livro pop-up com agentes de execução locais](https://x.com/atomicagent_io/status/2119918110752846094) (por [@atomicagent_io](https://x.com/atomicagent_io))

**Compare a orquestração com um único modelo na mesma tarefa.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Atomic relata US$ 2,98 em 11 minutos com Fable coordenando agentes Qwen locais, contra US$ 15,77 em 21 minutos com Fable sozinho.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [Retorno do teste da luminária de lava](https://x.com/eidzoku/status/2119918134060601690) (por [@eidzoku](https://x.com/eidzoku))

**Use a mesma tarefa visual para comparar vários modelos.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor retomou um teste de luminária de lava e compartilhou a comparação visual dos resultados.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [Um jato detalhado modelado no Blender](https://x.com/higgsfield_ai/status/2119918248955392431) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Defina no briefing a quantidade de peças, a duração e o visual.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Higgsfield relata um modelo em Blender com 931 peças e 24.260 rebites, criado via script com Fable 5.2 e seu MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [Uma viagem por portais entre centenas de mundos](https://x.com/emollick/status/2119918307457577163) (por [@emollick](https://x.com/emollick))

**Conecte por portais ambientes gerados de forma independente.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ Reproduzir vídeo</a>

Ethan Mollick relata mais de 450 mundos criados em código por 25 mil agentes e compartilha uma versão jogável e o repositório.

[Material relacionado 1](https://portals-endless-worlds.netlify.app/) · [Material relacionado 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [Um bazar de Bombaim em seis planos com Three.js](https://x.com/higgsfield_ai/status/2119918834841010320) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Divida o briefing visual em planos com duração definida.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Higgsfield mostra uma sequência de bazar de 21,5 segundos, em seis planos renderizados no Three.js.

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [Uma lanchonete fotorrealista feita em código](https://x.com/higgsfield_ai/status/2119918838490010008) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Use uma cena feita em código para inspecionar materiais e iluminação.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Higgsfield mostra uma lanchonete e relata que a construiu em código sem um aplicativo de modelagem 3D.

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [Um modelo de robô no Blender](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (por [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Use uma vista giratória para verificar articulações e silhueta.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um pequeno robô mecânico construído em uma demonstração de Blender com Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [Animação explicativa para Convex](https://x.com/Rasmic/status/2119919466163093768) (por [@Rasmic](https://x.com/Rasmic))

**Explique um produto para desenvolvedores em uma animação curta.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha um vídeo explicativo de Convex feito com Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [Coleção de landing pages feitas com um único prompt](https://x.com/daradoescode/status/2119919529807466594) (por [@daradoescode](https://x.com/daradoescode))

**Compare hierarquia e layout em vários briefings curtos.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um vídeo que reúne páginas de destino criadas com Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [Uma sonata para piano escrita em LilyPond](https://x.com/imjustnewatai/status/2119919644836347926) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Mantenha a partitura vinculada ao vídeo renderizado.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor pediu um movimento no estilo de Beethoven e relata que as notas exibidas vêm do arquivo LilyPond.

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [Um briefing de vídeo livre](https://x.com/aollivier82/status/2119920990893244510) (por [@aollivier82](https://x.com/aollivier82))

**Use um briefing aberto para observar as escolhas criativas do modelo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra o resultado de pedir ao Fable 5.2 que fizesse o vídeo mais bonito que pudesse.

Prompt original

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable planeja, DeepSeek implementa e Opus revisa](https://x.com/ivanfioravanti/status/2119921810267636201) (por [@ivanfioravanti](https://x.com/ivanfioravanti))

**Separe coordenação, implementação e revisão entre agentes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra Fable coordenando quatro agentes DeepSeek V4.1 Flash com herdr, enquanto Opus 5.5 revisa as pull requests.

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [Fable 5.2 no AI Village](https://x.com/aidigest_/status/2119923190411719158) (por [@aidigest_](https://x.com/aidigest_))

**Verifique separadamente a resposta do agente e suas ações sobre a memória.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

O registro público mostra que o Fable aceitou rever a memória depois, a pedido de outro agente. Uma publicação relacionada mostra um teste de afinidade com personagens.

[Material relacionado 1](https://x.com/aidigest_/status/2119923209311260707) · [Material relacionado 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [Design de frontend com e sem skills](https://x.com/AdamHoltererer/status/2119924849321914653) (por [@AdamHoltererer](https://x.com/AdamHoltererer))

**Mantenha o modelo fixo e varie as skills.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

O autor mostra dois resultados de frontend com Fable 5.2, um com skills e outro sem.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [Como encontrar máquinas de estado implícitas](https://x.com/kunchenguid/status/2119924895060795492) (por [@kunchenguid](https://x.com/kunchenguid))

**Audite um módulo e peça diagramas de antes e depois.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

O autor mostra uma melhoria no repositório Firstmate e publica o prompt exato da auditoria.

[Material relacionado 1](https://github.com/kunchenguid/lavish-axi)

Prompt original

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [Um jogo criado do zero em oito horas](https://x.com/felixrieseberg/status/2119925633564463609) (por [@felixrieseberg](https://x.com/felixrieseberg))

**Registre entradas em cache, recursos gerados e tempo de execução.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O engenheiro da Anthropic relata a criação de modelos, sons e texturas em uma execução com custo equivalente de cerca de US$ 550 pela API.

[Material relacionado 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [Material relacionado 2](https://x.com/AndrewCurran_/status/2119953960794780133)

Prompt original

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Protótipo de Fishslop e custo em tokens](https://x.com/theo/status/2119926277801144695) (por [@theo](https://x.com/theo))

**Compare a versão do jogo com um resultado anterior de outro modelo.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ Reproduzir vídeo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

O autor relata 76 minutos e cerca de US$ 42 em tokens e compara o resultado com Opus 5.5.

[Material relacionado 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [Um jogo de futebol americano em movimento](https://x.com/WesRoth/status/2119926801514529027) (por [@WesRoth](https://x.com/WesRoth))

**Teste indicações de jogo e pontuação em um protótipo esportivo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um jogo de Fable 5.2 com avisos de pontuação em tela.

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [Batalha de chefe em mundo aberto com Higgsfield MCP](https://x.com/higgsfield_ai/status/2119926932343324795) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Separe o jogo executável das sequências cinematográficas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Higgsfield relata um jogo de navegador com mundo aberto, batalha de chefe em três atos e sequências feitas com Fable 5.2 e seu MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [Mont Saint-Michel e as marés](https://x.com/loktar00/status/2119927152489472076) (por [@loktar00](https://x.com/loktar00))

**Teste mudanças no nível da água em uma cena histórica pequena.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra uma miniatura de Mont Saint-Michel com marés animadas.

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [Um recurso de Roblox no Blender](https://x.com/hiyouwhatsapp/status/2119927163264573642) (por [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**Revise o recurso no Blender antes de importá-lo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um resultado do Blender para Roblox feito quase com um único prompt.

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [Raciocínio sem exibir cadeia de pensamento](https://x.com/Tim_Hua_/status/2119927284761293089) (por [@Tim_Hua_](https://x.com/Tim_Hua_))

**Avalie as respostas sob a mesma restrição de saída.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

O avaliador executou testes de raciocínio e conhecimento sem saída de cadeia de pensamento e coloca Fable 5.2 um pouco abaixo de GPT-6.1 Sol.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [Versões do Chrome Dino com quatro modelos](https://x.com/noclipepe/status/2119927838321328577) (por [@noclipepe](https://x.com/noclipepe))

**Compare o tempo e o custo em um briefing recorrente.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor inclui Fable 5.2 em um teste anterior do T-Rex com Opus, Gemini e Astra e mostra os resultados juntos.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [Jogo de damas com um braço robótico](https://x.com/karolina_dubiel/status/2119928342115676576) (por [@karolina_dubiel](https://x.com/karolina_dubiel))

**Leia as posições das articulações e repita as pegadas que falharam.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor relata que o modelo corrigiu um desnível de cerca de 7 mm e tentou novamente os movimentos que falharam a partir do feedback.

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [Uma animação gráfica de quinze segundos](https://x.com/aziz4ai/status/2119928581405200726) (por [@aziz4ai](https://x.com/aziz4ai))

**Registre a cota consumida por um teste curto de animação em código.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra uma cena de 15 segundos feita em código e relata o uso de 4% de uma cota semanal.

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [Uma Torre Eiffel jogável](https://x.com/bobyau/status/2119928812628771212) (por [@bobyau](https://x.com/bobyau))

**Teste se o modelo de um monumento permite interação.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra uma demonstração da Torre Eiffel e relata que a criou em 25 minutos.

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [Corrida em alto-mar com Three.js e Higgsfield](https://x.com/higgsfield_ai/status/2119928918035910668) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Separe a lógica de jogo das ferramentas de mídia.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Higgsfield mostra um jogo de corrida com ondas grandes, cinco rivais de IA e foguetes teleguiados.

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [Simulação de mel em tempo real com WebGL](https://x.com/deedydas/status/2119930300990177509) (por [@deedydas](https://x.com/deedydas))

**Use uma simulação física no navegador para avaliar o movimento do material.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra uma simulação de mel em tempo real no WebGL e publica o briefing original.

Prompt original

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [Efeitos visuais programados sobre vídeo](https://x.com/ashebytes/status/2119930763105931649) (por [@ashebytes](https://x.com/ashebytes))

**Revise o tempo e a posição dos efeitos sobre o vídeo original.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha um teste de efeitos com Fable 5.2, com gráficos animados compostos sobre vídeo real.

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [Explicação animada dos níveis de procura em GTA](https://x.com/saimagnate/status/2119931563760632311) (por [@saimagnate](https://x.com/saimagnate))

**Combine cenas do jogo e diagramas para explicar uma mecânica.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O criador atribui o resultado a um único pedido ao Fable 5.2. O vídeo compara os sistemas de procura de GTA V e RDR2 com cenas e diagramas.

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [Um mundo de MMO estilizado feito em código](https://x.com/Izkimar/status/2119931740940640542) (por [@Izkimar](https://x.com/Izkimar))

**Use recursos estilizados para avaliar a consistência do mundo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor relata ter construído em um dia o mundo de MMO mostrado, com recursos gerados em código.

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [Uma cena 3D com Fable e Opus](https://x.com/dom_scholz/status/2119933150025363661) (por [@dom_scholz](https://x.com/dom_scholz))

**Compare tempo de preparação e detalhe em uma mesma visualização.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha duas renderizações, de Fable 5.2 e Opus 5.5, e relata que Fable terminou mais rápido.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [Texto redundante na tela de pausa de um jogo](https://x.com/AndrewPrifer/status/2119934600608915465) (por [@AndrewPrifer](https://x.com/AndrewPrifer))

**Revise o texto gerado em busca de explicações repetidas.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

O desenvolvedor usa uma tela de pausa como exemplo do excesso de explicações escritas pelo Fable 5.2.

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [Painéis de inspiração em um ambiente Krea](https://x.com/lambdacalcc/status/2119934725662060663) (por [@lambdacalcc](https://x.com/lambdacalcc))

**Compare conceitos antes de escolher uma direção visual.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

O autor mostra quatro resultados de uma sessão de moodboards com Fable 5.2 em um ambiente Krea.

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [Teste de um jogo de tiro com portais no escritório](https://x.com/_sholtodouglas/status/2119935331499925557) (por [@_sholtodouglas](https://x.com/_sholtodouglas))

**Avalie um jogo gerado em sessões com vários jogadores.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ Reproduzir vídeo</a>

Um engenheiro da Anthropic mostra um FPS de arena com portais e descreve os testes no escritório.

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Objeto detalhado de superfície rígida no Blender](https://x.com/ziwenxu_/status/2119937420280168929) (por [@ziwenxu_](https://x.com/ziwenxu_))

**Inspecione topologia e silhueta na janela de visualização do Blender.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um objeto de superfície rígida apresentado como resultado do Fable 5.2 no Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [Testes paralelos de frontend em vários níveis de esforço](https://x.com/AI_masaou/status/2119937635322085640) (por [@AI_masaou](https://x.com/AI_masaou))

**Compare briefings simples e ambiciosos em vários níveis de esforço.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

O autor relata resultados simples semelhantes, mais detalhes nos trabalhos maiores do Fable e um aumento acentuado de tempo e tokens entre Medium e High.

[Material relacionado 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [Um jogo pequeno em dez prompts](https://x.com/AmirMushich/status/2119937977426338283) (por [@AmirMushich](https://x.com/AmirMushich))

**Registre a quantidade de iterações e o tamanho do jogo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor relata um jogo de 220 KB e cerca de 3.400 linhas e compartilha código e vídeo.

[Material relacionado 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [Animação quadro a quadro com JavaScript](https://x.com/kevin_t_ngo/status/2119938129079808282) (por [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Inspecione uma sequência com quadros desenhados em código.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra a animação e relata que JavaScript desenhou todos os quadros.

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [De vídeo de referência a animação 3D](https://x.com/KHvostikk/status/2119939061049889130) (por [@KHvostikk](https://x.com/KHvostikk))

**Use o vídeo de referência para avaliar uma cena reconstruída.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha uma demonstração de conversão de vídeo para animação 3D com Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Fogueira em pixel art com Fable e Opus](https://x.com/GrilliotTodd/status/2119939651385655692) (por [@GrilliotTodd](https://x.com/GrilliotTodd))

**Compare iluminação e silhuetas no mesmo tema.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ Reproduzir vídeo</a>

Os resultados lado a lado mostram versões de uma fogueira feitas por Fable 5.2 e Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [Arena WebDev com esforço xHigh](https://x.com/arena/status/2119941204003770690) (por [@arena](https://x.com/arena))

**Compare o nível de esforço usado na classificação.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

A Arena publicou uma estreia de 1.832 pontos para Claude Fable 5.2 xHigh na Code Arena WebDev.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [Tipografia de trailer com dois modelos](https://x.com/muku_sns/status/2119941490969624679) (por [@muku_sns](https://x.com/muku_sns))

**Compare duas interpretações de um mesmo parágrafo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra os títulos do Opus e do Fable lado a lado. A versão Fable acrescenta uma borda vermelha e títulos censurados.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [Testes de motion e portfólio 3D com um só prompt](https://x.com/Khazix0918/status/2119941585538572390) (por [@Khazix0918](https://x.com/Khazix0918))

**Teste pesquisa, design e renderização separadamente.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ Reproduzir vídeo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ Reproduzir vídeo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ Reproduzir vídeo</a></td></tr></table>

O autor compartilha quatro execuções: um vídeo de aniversário do ChatGPT, uma explicação sobre DeepSeek, uma cena em Three.js e uma recriação em 3D da Apple Jing’an.

[Material relacionado 1](https://x.com/Khazix0918/article/2119941585538572390)

Prompt original

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [Explicação interativa de um reator nuclear](https://x.com/konstantinsaifo/status/2119941967136379334) (por [@konstantinsaifo](https://x.com/konstantinsaifo))

**Use a desmontagem para mostrar como as peças se encaixam.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor pediu um reator desmontável no Three.js e relata US$ 92 em custos de API.

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Agentes no Blood on the Clocktower](https://x.com/dwarkesh_sp/status/2119942657812451482) (por [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**Compare modelos no mesmo jogo de papéis secretos.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

O avaliador coloca Fable 5.2 acima de Fable 5.1 e Opus 5.5, com GPT-6 Astra à frente neste benchmark.

[Material relacionado 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [Protótipo de corrida de pods](https://x.com/loktar00/status/2119943124965638444) (por [@loktar00](https://x.com/loktar00))

**Use um formato de corrida conhecido para avaliar movimento e controles.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha um resultado do Fable 5.2 inspirado em corridas de pods.

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [Comercial de roupa íntima do Claude em dez segundos](https://x.com/Masimo_Blue/status/2119943368612487285) (por [@Masimo_Blue](https://x.com/Masimo_Blue))

**Teste um briefing de produto aberto com música original.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ Reproduzir vídeo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

O autor compartilha um comercial de dez segundos com acid techno e as imagens de produto fornecidas.

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [Um pássaro ao nascer do sol, traço a traço](https://x.com/mgrczyk/status/2119943813028548721) (por [@mgrczyk](https://x.com/mgrczyk))

**Desative a opção de desfazer para observar decisões de desenho consecutivas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um pássaro pintado ao amanhecer em um ambiente que impedia alterar traços anteriores.

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [Uma execução gráfica longa no Devin](https://x.com/Da7_Tech/status/2119944847255896490) (por [@Da7_Tech](https://x.com/Da7_Tech))

**Registre tempo e gasto ao testar uma renderização exigente.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ Reproduzir vídeo</a>

Um embaixador declarado da Cognition compartilha uma execução do Devin Max de cerca de 3,5 horas e US$ 82, segundo seu relato.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [Pintura em código com três modelos](https://x.com/kickingkeys/status/2119945841997672698) (por [@kickingkeys](https://x.com/kickingkeys))

**Compare os movimentos do desenho e o som sintetizado entre execuções.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra uma pintura feita em código com áudio e descreve testes com o mesmo prompt no Fable 5.2, Fable 5.1 e Gemini 4 Argon.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [A história da escrita em movimento](https://x.com/rileybrown/status/2119946022767980985) (por [@rileybrown](https://x.com/rileybrown))

**Use uma linha do tempo para organizar uma explicação feita em código.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra uma animação sobre a história da escrita e relata que a criou com um único prompt.

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [Campo de testes para máquinas de jogo](https://x.com/techartist_/status/2119946891106394518) (por [@techartist_](https://x.com/techartist_))

**Teste mecânicas, física e efeitos na mesma cena.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor construiu um ambiente de teste para quatro conceitos com Three.js e Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [PCB para um console portátil Linux](https://x.com/seveibar/status/2119947341230907453) (por [@seveibar](https://x.com/seveibar))

**Compare os modelos com o mesmo briefing de circuito.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O criador do tscircuit mostra um teste de design de um console Linux portátil com Astra 6 High e Fable 5.2 High.

Prompt original

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [Um lago de voxels](https://x.com/Angaisb_/status/2119947748690841841) (por [@Angaisb_](https://x.com/Angaisb_))

**Use um cenário pequeno para avaliar a composição.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha um lago de voxels atribuído ao Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [As 17 gerações interativas da Arena](https://x.com/arena/status/2119948067449536733) (por [@arena](https://x.com/arena))

**Explore vários tipos de resultado antes de escolher uma tarefa de teste.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Arena compartilha 17 gerações que incluem mundos em 3D, jogos, interfaces, visualizações de dados e animações feitas em código.

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [Voo com um dragão amistoso](https://x.com/chetanankola/status/2119951015407738913) (por [@chetanankola](https://x.com/chetanankola))

**Use um ciclo de voo para testar câmera e movimento.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha uma cena de dragão feita com Three.js e Blender e descreve melhorias feitas com Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Orca de gelatina com Fable e Opus](https://x.com/vib3coded/status/2119951060752375827) (por [@vib3coded](https://x.com/vib3coded))

**Compare superfície e movimento no mesmo tema.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra lado a lado as orcas de gelatina do Fable 5.2 e do Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [Teste aberto de qualidade de vídeo](https://x.com/suna_gaku/status/2119952985933697063) (por [@suna_gaku](https://x.com/suna_gaku))

**Dê liberdade criativa para observar as escolhas do modelo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor pediu ao modelo que mostrasse seu melhor trabalho em vídeo e compartilhou o resultado.

Prompt original

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [Habitat espacial de inspiração mediterrânea](https://x.com/MaxXWilliamson/status/2119953172634677533) (por [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**Combine um briefing curto com ferramentas já usadas no projeto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor forneceu ferramentas de seus habitats espaciais anteriores e pediu uma estação de inspiração mediterrânea.

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [Benchmark AA-3D de experiências interativas](https://x.com/ArtificialAnlys/status/2119953570430881946) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Leia o Elo junto com o intervalo de incerteza.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Artificial Analysis publicou um Elo inicial de 1.271 para Fable 5.2 Max em seu benchmark de experiências interativas em 3D.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [Desafio cronometrado com um personagem esquelético](https://x.com/WesRoth/status/2119953913160093817) (por [@WesRoth](https://x.com/WesRoth))

**Use um cronômetro visível para avaliar um protótipo jogável.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostra um resultado do Fable 5.2 feito com um único prompt, com um personagem esquelético e contagem regressiva na tela.

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Pixel art com Fable e Astra](https://x.com/Angaisb_/status/2119955179915137294) (por [@Angaisb_](https://x.com/Angaisb_))

**Compare formas e detalhes na mesma escala.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A comparação original mostra resultados de pixel art do GPT-6 Astra e do Fable 5.2.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [Reel de portfólio de motion design](https://x.com/Leviwoyun/status/2119955625820258308) (por [@Leviwoyun](https://x.com/Leviwoyun))

**Use um briefing aberto com duração fixa.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilha um reel com música e relata um tempo de produção de 24 minutos.

Prompt original

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [Renderização de uma piscina de vidro com dois modelos](https://x.com/MrTacticalX/status/2119955647542542439) (por [@MrTacticalX](https://x.com/MrTacticalX))

**Compare a iluminação, o tempo e o custo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor relata 90 minutos e US$ 57,87 para Fable contra 68 minutos e US$ 14,39 para Opus.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [Precisão de chamadas a ferramentas no TS-Bench](https://x.com/gosrum/status/2119956559031927079) (por [@gosrum](https://x.com/gosrum))

**Acompanhe separadamente os erros de chamada e o uso de tokens.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

O avaliador relata que o Fable 5.2 não errou chamadas a ferramentas e que as tarefas mais simples mal distinguem as variantes do Claude.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [Machu Picchu em miniatura](https://x.com/loktar00/status/2119958719362666708) (por [@loktar00](https://x.com/loktar00))

**Inspecione a atmosfera e os pequenos detalhes de uma cena em miniatura.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A demonstração de Machu Picchu inclui neblina volumétrica e pequenas alpacas.

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [GDPx por categoria de trabalho profissional](https://x.com/SemiAnalysis_/status/2119961447199289640) (por [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**Leia os resultados por subtarefa junto com a pontuação geral.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

O responsável pelo benchmark relata pontuação geral de 16,4% e detalha áreas como design de chips e engenharia de software.

[Material relacionado 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [Material relacionado 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [Material relacionado 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [Um retrato em um aplicativo de desenho](https://x.com/The_Alex/status/2119964472559489229) (por [@The_Alex](https://x.com/The_Alex))

**Use uma miniatura de referência para orientar o retrato.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O criador pediu ao Fable 5.2 que abrisse um aplicativo de desenho e fizesse seu retrato. O vídeo mostra o processo do contorno à versão final.

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [VulcanBench Frontier v4 com esforço Low](https://x.com/morganlinton/status/2119966067527467215) (por [@morganlinton](https://x.com/morganlinton))

**Compare gerações do modelo no mesmo nível de esforço.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

O autor do benchmark relata cerca de 5 contra 26 minutos por tarefa para Fable 5.2 e 5.1, respectivamente, com esforço Low.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [Inversão de papéis em um Backrooms jogável](https://x.com/LexnLin/status/2119966127149429093) (por [@LexnLin](https://x.com/LexnLin))

**Mude o objetivo do jogador para testar um conceito de jogo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O jogador controla o monstro e tenta capturar pessoas. O autor compartilha a partida e um link para jogar.

[Material relacionado 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [Bugatti Tourbillon no Blender](https://x.com/xikhar/status/2119966147328299284) (por [@xikhar](https://x.com/xikhar))

**Use imagens de referência para definir exterior e interior.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor relata que modelou um Bugatti Tourbillon, incluindo o interior, e renderizou uma sequência a partir de um prompt e referências.

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [Um vídeo sobre computadores feito com dois modelos](https://x.com/daradoescode/status/2119966154391183522) (por [@daradoescode](https://x.com/daradoescode))

**Registre as contribuições de cada modelo em um fluxo misto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilhou um vídeo estilizado criado com Fable 5.2 e contribuição substancial do Opus 5.5.

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [Um clipe musical sobre megakernels](https://x.com/elliotarledge/status/2119968762069934415) (por [@elliotarledge](https://x.com/elliotarledge))

**Use um conceito técnico como tema de um vídeo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor pediu um clipe sobre megakernels ao Fable 5.2 com esforço High e compartilhou o resultado.

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [Visita ao estúdio a partir de fotos de referência](https://x.com/rpnickson/status/2119969928304357507) (por [@rpnickson](https://x.com/rpnickson))

**Use fotos reais para orientar a reconstrução de uma cena.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor forneceu fotos do estúdio, adaptou um briefing de vídeo parecido e relata que a execução levou cerca de duas horas.

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [Um comercial de brinquedos dos anos 1990 feito em código](https://x.com/kevin_t_ngo/status/2119972124211454139) (por [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Separe a programação da animação da renderização.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor relata que animou um comercial retrô de brinquedos em Python e o renderizou no Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Cena de jogo em terceira pessoa com Three.js](https://x.com/bijanbowen/status/2119972220739187182) (por [@bijanbowen](https://x.com/bijanbowen))

**Use uma partida para observar o movimento e o cenário.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

O autor mostra em uma transmissão um resultado em Three.js com um personagem em terceira pessoa percorrendo um cenário externo.

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [Bryceball a partir de um renderizador existente](https://x.com/pleometric/status/2119973274402668852) (por [@pleometric](https://x.com/pleometric))

**Reutilize um motor de renderização como base de um jogo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor adaptou o renderizador da publicação vinculada para criar o jogo Bryceball.

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [Edição recursiva de vídeo com Fable](https://x.com/rileybrown/status/2119973951027724385) (por [@rileybrown](https://x.com/rileybrown))

**Reaproveite uma edição anterior em uma nova peça.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor compartilhou um vídeo editado com Fable 5.2 sobre outro vídeo que também havia editado com o modelo.

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [Uma história cinematográfica da ciência](https://x.com/DeryaTR_/status/2119974354260013293) (por [@DeryaTR_](https://x.com/DeryaTR_))

**Use uma linha do tempo para organizar uma sequência em 3D.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor pediu uma jornada cinematográfica dos primórdios da ciência a um futuro especulativo e compartilhou o vídeo.

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [Máquina voadora de Da Vinci em 3D](https://x.com/higgsfield_ai/status/2119975721909301684) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Modele um projeto histórico antes de testar alterações.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A Higgsfield mostrou uma interpretação 3D da máquina voadora de Leonardo e descreveu um teste físico e um novo desenho.

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [Roteamento de PCB a partir de um projeto](https://x.com/cmonkey/status/2119975852977029365) (por [@cmonkey](https://x.com/cmonkey))

**Inspecione o roteamento da placa antes da fabricação.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

O autor compartilhou um resultado de roteamento do Fable 5.2 em resposta a uma discussão sobre layout.

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [Um mesmo prompt em ambientes diferentes](https://x.com/loktar00/status/2119980613369319706) (por [@loktar00](https://x.com/loktar00))

**Registre as diferenças de ambiente ao comparar os resultados.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor enviou o mesmo prompt ao DeepSeek e ao Fable 5.2 em ambientes distintos e mostrou os resultados juntos.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [Ilustração do Godzilla desenhada com código](https://x.com/chetaslua/status/2119981510199808368) (por [@chetaslua](https://x.com/chetaslua))

**Reinterprete uma imagem com formas vetoriais e movimento.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor mostrou uma ilustração feita com código e uma animação curta inspirada em uma publicação sobre Godzilla.

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [Ventilador de mão para impressão 3D](https://x.com/davelee/status/2119981787325579398) (por [@davelee](https://x.com/davelee))

**Use um protótipo físico para verificar a montagem.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor e seus filhos projetaram um ventilador de mão imprimível e compartilharam o modelo antes da impressão.

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [Busca de bugs em um plugin contra o Opus](https://x.com/oaranda/status/2119982729747919096) (por [@oaranda](https://x.com/oaranda))

**Compare as correções com testes de regressão cruzados.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

Trecho do anúncio anotado pelo autor.

Os dois modelos encontraram os mesmos seis bugs. O Opus passou nos testes cruzados; o Fable falhou em um e achou outro problema no painel.

Prompt original

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [Istambul recriada em uma cena 3D](https://x.com/petergostev/status/2119877733488394520) (por [@petergostev](https://x.com/petergostev))

**Examine a cidade em vistas amplas e aproximadas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ Reproduzir vídeo</a>

Peter Gostev compartilha uma cena 3D de Istambul com Fable 5.2 Max e vincula a avaliação mais extensa.

[Material relacionado 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [Um filme no Blender com uma tela funcional](https://x.com/rileybrown/status/2119902109709537708) (por [@rileybrown](https://x.com/rileybrown))

**Anime a tela, a iluminação e a câmera na mesma cena 3D.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor relata 13 tomadas, uma página personalizada rodando no notebook e áudio da ElevenLabs. O render usou GPUs da RunPod.

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [Uma transição de buracos negros em acoplamento fraco](https://hexagonmath.org/2611.00175v1) (por [@Anthropic](https://www.anthropic.com/))

**Confira um cálculo pendente usando a formulação teórica original.**

A Anthropic relata que Fable 5.2 concluiu um cálculo antigo e encontrou uma transição abrupta no regime de acoplamento fraco. O preprint traz a derivação.

[Material relacionado 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [O limite de uma cota do bootstrap modular](https://hexagonmath.org/2611.00174v1) (por [@Anthropic](https://www.anthropic.com/))

**Publique a derivação junto à cota analítica proposta.**

A Anthropic relata que Fable 5.2 determinou o limite exato de uma técnica de bootstrap modular sem spin em um modelo simplificado de gravidade quântica.

[Material relacionado 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Vercel AI Gateway com modelos alternativos em ordem](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (por [Vercel](https://vercel.com/))

**Configure no gateway a ordem de fallback para solicitações recusadas pelo classificador.**

O exemplo do AI SDK da Vercel chama anthropic/claude-fable-5.2 e configura Opus 5.5 e depois Sonnet 5.5 como alternativas. O guia documenta o requisito de retenção de dados.

[Material relacionado 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [Subagentes aninhados e orçamento de revisão](https://news.ycombinator.com/item?id=50430925) (por [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**Monitore a delegação aninhada e imponha limites fora do prompt.**

O autor pediu no máximo quatro subagentes para revisar 80 mil linhas. Relata seis ou mais agentes aninhados e o esgotamento da cota de cinco horas em menos de 20 minutos.

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [Comparação de um design LCARS convertido em HTML](https://news.ycombinator.com/item?id=50430962) (por [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**Verifique curvas, ícones, animação e navegação separadamente.**

O autor compara Fable 5.2 e Opus 5.5 com o mesmo design inspirado em Star Trek. Preferiu as curvas e alguns ícones do Fable e o movimento do Opus. O SVG do Fable piscava de forma incômoda. Ele só pediu a primeira página.

[Material relacionado 1](https://html.non.io/lcars-fable-5.2/) · [Material relacionado 2](https://html.non.io/lcars-opus-5.5/) · [Material relacionado 3](https://news.ycombinator.com/item?id=50431231) · [Material relacionado 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [Otimização para GPU no Quantum ESPRESSO](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (por [Discovered Materials](https://discoveredmaterials.com/))

**Exija resultados de referência e testes ocultos representativos ao otimizar código científico.**

A Discovered Materials relata aceleração média geométrica de 36× em 13 testes de fônons na mesma GPU e de cerca de 9× em cálculos com funcionais híbridos. O patch publicado se apoia em testes de correção e desempenho.

[Material relacionado 1](https://github.com/discovered-materials/dm_qe) · [Material relacionado 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [Índice de inteligência da Artificial Analysis por esforço](https://artificialanalysis.ai/models/claude-fable-5-2) (por [Artificial Analysis](https://artificialanalysis.ai/))

**Leia juntos pontuação, custo e tempo por tarefa no nível escolhido.**

O recorte citado de Max com fallback padrão mostra índice 65, US$ 26,54 e 46,4 minutos por tarefa. Os números se referem à carga do benchmark.

[Material relacionado 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [Falsos positivos na revisão de mudanças com esforço High](https://news.ycombinator.com/item?id=50431810) (por [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**Valide no código os problemas apontados pelo modelo antes de agir.**

Um desenvolvedor relata que Fable 5.2 High apontou dois problemas inexistentes, que ele percebeu por conhecer o código.

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [Trinta tarefas rotineiras de programação](https://news.ycombinator.com/item?id=50432483) (por [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**Meça duração e tarefas concluídas na mesma carga de trabalho.**

O autor relata 26 de 30 tarefas resolvidas por Fable 5.2 e Opus 5.5, contra 25 pelo Fable 5.1. Fable 5.2 levou 0,62 vez o tempo do 5.1, sem bloqueios de segurança relatados.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [Protetor de tela de um náufrago em uma ilha](https://news.ycombinator.com/item?id=50432836) (por [@nzach](https://news.ycombinator.com/user?id=nzach))

**Abra a página interativa para examinar o protetor de tela.**

O autor do Show HN vincula Stranded with Claude, uma cena de ilha para navegador. O artefato publicado é um canvas interativo.

[Material relacionado 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [Três jogos de navegador com esforço High](https://senko.net/vibecode-bench/) (por [Senko Rašić](https://senko.net/))

**Compare separadamente a jogabilidade e a fidelidade visual.**

Senko Rašić executou briefings de estratégia em tempo real, voxels e simulador de voo com Fable 5.2 no Claude Code. Ele relata mecânicas mais profundas, como um dirigível para explorar todo o mapa, e avaliou partes dos gráficos como piores.

[Material relacionado 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [Roteiros de podcast de livros por capítulo](https://news.ycombinator.com/item?id=50434156) (por [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**Compare o tamanho dos roteiros na mesma tarefa recorrente.**

O autor gerou diálogos entre dois resenhistas, um capítulo de cada vez. Relata cerca de 2,5 páginas nas versões Fable contra 4,5 no Opus 5.5 e vincula ambas.

[Material relacionado 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [Material relacionado 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [Um serviço de produção migrado para Rust](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (por [@Anthropic](https://www.anthropic.com/))

**Meça o tempo de inicialização antes e depois da migração.**

A Anthropic relata que agentes com uma versão preliminar de Fable 5.2 reescreveram em Rust um serviço de produção em Python, reduzindo o tempo de inicialização em cerca de 26 vezes.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [Selecionar o Fable 5.2 no GitHub Copilot](https://x.com/github/status/2119926269982961833) (por [@github](https://x.com/github))

**Ative a política da organização antes de selecionar o modelo.**

O GitHub documenta o seletor de modelos do Copilot e a configuração administrativa exigida nas contas Business e Enterprise.

[Material relacionado 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [Desafio de design de cem páginas HTML](https://x.com/MiaAI_lab/status/2119930229661503893) (por [@MiaAI_lab](https://x.com/MiaAI_lab))

**Conte os arquivos concluídos e executáveis, além de avaliar o visual.**

O autor pediu 100 designs variados e publicou 76 arquivos com prompts. Segundo seu relato, atingiu o limite de uso do Fable.

[Material relacionado 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [Material relacionado 2](https://mia-ai.net/lab/experiments/100-htmls) · [Material relacionado 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [Material relacionado 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [Material relacionado 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [Material relacionado 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [Material relacionado 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [Material relacionado 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [Material relacionado 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [Material relacionado 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [Material relacionado 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [Material relacionado 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [Material relacionado 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [Material relacionado 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [Desvio de requisitos em um compilador](https://x.com/sameQCU/status/2119939304864800971) (por [@sameQCU](https://x.com/sameQCU))

**Compare os requisitos declarados pelo agente com a entrada original.**

O desenvolvedor descreve uma tarefa de compilação em que Fable 5.2 e versões anteriores do Opus relataram incorretamente os requisitos recebidos.

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [Acompanhar uma tarefa longa do Fable com Opus](https://x.com/marouane53/status/2119950129767858262) (por [@marouane53](https://x.com/marouane53))

**Use uma sessão separada para acompanhar tarefas demoradas.**

O autor relata que algumas tarefas do Fable passaram de duas horas com poucas atualizações. Usou o Opus 5.5 em outra conversa para explicar o andamento e as decisões.

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [Revisão de código com um olhar novo](https://x.com/doodlestein/status/2119958895158292786) (por [@doodlestein](https://x.com/doodlestein))

**Faça uma revisão separada dos arquivos novos e modificados.**

O autor compartilha dois prompts exatos de acompanhamento para localizar e corrigir erros após a implementação.

Prompt original

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

Prompt original

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [Perda de contexto na revisão de um recurso](https://news.ycombinator.com/item?id=50434214) (por [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**Use o projeto atual como lista de verificação ao revisar sugestões posteriores.**

O autor preferiu Opus 5.5 após comparar os modelos em uma revisão de projeto. Em um diagnóstico posterior, Fable 5.2 recomendou algo que já existia.

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [Comparação de Breakout no estilo DX Ball](https://news.ycombinator.com/item?id=50434424) (por [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**Compare as mecânicas e a sensação de jogo sob o mesmo briefing.**

O autor vincula versões feitas separadamente com Fable 5.2 e Opus 5.5. Fable alterou algumas mecânicas originais, e o autor preferiu jogar a versão do Opus.

[Material relacionado 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [Material relacionado 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [Teste de melhoria em um aplicativo 3D](https://news.ycombinator.com/item?id=50434433) (por [@user43928](https://news.ycombinator.com/user?id=user43928))

**Compare as mudanças visíveis com o orçamento gasto na mesma tarefa.**

O autor relata ter pedido melhorias em um aplicativo 3D que não era um jogo. Viu pouca diferença em relação ao Opus 5.5 e usou 25% da cota do plano Fable naquela noite.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [Jogo do rato e do gato em três modelos](https://news.ycombinator.com/item?id=50434508) (por [@simonw](https://news.ycombinator.com/user?id=simonw))

**Mantenha o prompt e examine cada implementação jogável.**

Simon Willison compartilha tentativas de um jogo Three.js para celulares com Fable 5.2 Extra, Opus 5.5 Extra e GPT-6 Extra High. Ele relata cerca de 40 minutos para o Fable.

[Material relacionado 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [Material relacionado 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [Material relacionado 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

Prompt original

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [Custo e pontuação no AIBenchy com esforço High](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (por [AIBenchy](https://aibenchy.com/))

**Compare pontuação, custo total e latência em níveis de esforço equivalentes.**

O AIBenchy publicou 8,7 contra 9,4, custo total de US$ 5,083 contra US$ 2,133 e média de 14,73 s contra 27,55 s para Fable 5.2 High e Opus 5.5 High, respectivamente.

[Material relacionado 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [Ajustar o ambiente de agentes do Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (por [@Anthropic](https://www.anthropic.com/))

**Teste novamente os níveis de esforço e defina avisos de progresso.**

O guia da Anthropic traz exemplos de instruções sobre esforço, critérios de conclusão, aprovações, atualizações e limites de subagentes.

[Material relacionado 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="case-469"></a>
### Case 469: [Um aplicativo para visualizar personagens animados](https://x.com/seiiiiiiiiiiru/status/2121390458572333253) (por [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Peça ao Fable que transforme verificações repetitivas de recursos em uma interface.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/ce514e99465c257220ee9bf7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/776670eda35fbabbf1c63663.jpg" alt="Case 469 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A pessoa que publicou o exemplo diz que passou a usar o Fable 5.2 como consultor e que o modelo transformou um fluxo pouco eficiente em um aplicativo. A gravação mostra movimentos predefinidos, controles de fundo e opções para exportar um personagem 3D em GLB e PNG transparente.

Type: Demo | Date: 2026-11-13

---

<a id="case-470"></a>
### Case 470: [Teste de um código QR criado sem ferramentas](https://x.com/AdamHoltererer/status/2121376853474578625) (por [@AdamHoltererer](https://x.com/AdamHoltererer))

**Escaneie a imagem do código QR para conferir se a tentativa funcionou.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d3833f006038158569c9816d.png" alt="Case 470 · 1" width="760">

Adam Holter atribui a demonstração do código QR ao Fable 5.2, ao Astra e ao Sol e afirma que nenhuma ferramenta foi usada. A leitura local da imagem anexada confirmou que o código contém o texto exato “MADE WITHOUT TOOLS”.

Type: Evaluation | Date: 2026-11-13

---

<a id="case-471"></a>
### Case 471: [Um jogo de zumbis no Unity com o Tripo](https://x.com/fe_yukichi/status/2121375714192814554) (por [@fe_yukichi](https://x.com/fe_yukichi))

**Use um fluxo comum de criação de recursos para montar um elenco de personagens jogáveis.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/055f505803b769bb8b24a54e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0fa0715e64f91ab69725599e.jpg" alt="Case 471 · 1" width="760"><br>▶ Reproduzir vídeo</a>

Em uma parceria declarada com o Tripo, o criador afirma ter usado o Tripo Agentic Canvas para produzir oito personagens jogáveis e dezesseis variantes de zumbis para um jogo feito no Unity com o Fable 5.2. O vídeo mostra a seleção de personagens e uma partida. O criador publicou uma versão para navegadores de desktop.

[Material relacionado 1](https://tsukiyo-zombie.pages.dev/)

Type: Demo | Date: 2026-11-13

---

<a id="case-472"></a>
### Case 472: [Uma rua nevada pintada no MS Paint](https://www.reddit.com/r/ClaudeAI/comments/1xvghd1/fable_52_painting_in_ms_paint/) (por [u/wollymonjac](https://www.reddit.com/user/wollymonjac/))

**Use uma gravação de tela para avaliar o controle direto do mouse durante uma tarefa longa.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/10ad84001f4c682c5343846c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e7af823e10ef2135adec2154.jpg" alt="Case 472 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor da publicação original no Reddit diz que o Fable 5.2 pintou uma rua nevada no MS Paint com o mouse em cerca de duas horas e meia. A republicação no X traz uma gravação da mesma cena.

[Material relacionado 1](https://x.com/i/status/2121373793599869213)

Type: Demo | Date: 2026-11-13

---

<a id="case-473"></a>
### Case 473: [Um cabo fora da tomada no Wojak-Bench](https://x.com/lukaspet/status/2121371593943466167) (por [@lukaspet](https://x.com/lukaspet))

**Confira se cada conexão da montagem 3D gerada corresponde à referência.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e509db79b2e79fcc2d6beda1.jpg" alt="Case 473 · 1" width="760">

O autor relata que o Fable 5.2 não conectou o cabo à tomada nessa tarefa do Wojak-Bench. A imagem original coloca uma foto do resultado 3D ao lado do desenho de referência.

Type: Limit | Date: 2026-11-13

---

<a id="case-474"></a>
### Case 474: [Um arranjo de piano para um jogo de ritmo](https://x.com/DJ_HYSNS/status/2121367353237942287) (por [@DJ_HYSNS](https://x.com/DJ_HYSNS))

**Verifique se a peça é tocável e quais controles de produção funcionam ao pedir que o modelo componha.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d016f48687e0c8e6cf810812.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/9faa77e2e9ba2ec99be995a7.jpg" alt="Case 474 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor pediu música para um jogo de ritmo e passou para piano solo depois de relatar dificuldade para fazer o modelo escolher timbres VST e mixar a peça. O vídeo mostra as notas na grade do piano roll. Segundo o autor, a peça ultrapassou o limite de dificuldade definido para que uma pessoa pudesse tocá-la.

Type: Evaluation | Date: 2026-11-13

---

<a id="case-475"></a>
### Case 475: [Redesenho da recuperação de tokens no Picnic](https://x.com/joaoavf/status/2121366491321057717) (por [@joaoavf](https://x.com/joaoavf))

**Compare os estados da interface ao recuperar tokens que a plataforma não aceita.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/551612796f4150a43b190ee3.jpg" alt="Case 475 · 1" width="760">

O autor diz que, com um ou dois prompts, o Fable 5.2 redesenhou o fluxo para recuperar tokens incompatíveis com o Picnic. A imagem anexada mostra várias telas da proposta.

Type: Demo | Date: 2026-11-13

---

<a id="case-476"></a>
### Case 476: [Edição de uma abertura de anime com clipes gerados](https://x.com/aimikoda/status/2121362621274177726) (por [@aimikoda](https://x.com/aimikoda))

**Entregue ao Fable os clipes, a trilha sonora e instruções claras para cortar no ritmo da música.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e3ab28061669d84818042ee0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/cb65344e413d2bd340406d59.jpg" alt="Case 476 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A pessoa que publicou o exemplo combinou cenas do MiniMax H3 e uma faixa do Suno v6 e usou o Fable 5.2 Medium para editar o vídeo. O resultado mostra personagens animados em pixel art e transições. O exemplo inclui o prompt original de edição para o Fable.

Prompt original

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
### Case 477: [Animação de personagem com três ferramentas](https://x.com/ingi_erlingsson/status/2121361947446677797) (por [@ingi_erlingsson](https://x.com/ingi_erlingsson))

**Compare o GIF inicial com a animação após as etapas no Fable e no ComfyUI.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/69a3410b7b2dcdb14ee6c5d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/391924750cd0641254cb114f.jpg" alt="Case 477 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O autor indica um GIF do GPT Image 2.6 como ponto de partida, seguido pelo Fable 5.2 e pelo ComfyUI. O vídeo anexado mostra a cabeça de um personagem mudando enquanto o ponto de vista gira.

Type: Demo | Date: 2026-11-13

---

<a id="case-478"></a>
### Case 478: [Renderização de um trailer urbano com scripts do Blender](https://x.com/hanghuang_/status/2121361932456427644) (por [@hanghuang_](https://x.com/hanghuang_))

**Divida a produção do trailer em cenário, personagem, veículo e renderização.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0e5170c057eecd328b178fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d10c5d322edba010282a60d0.jpg" alt="Case 478 · 1" width="760"><br>▶ Reproduzir vídeo</a>

O criador relata que o Fable 5.2 planejou um trailer com estética de jogo e escreveu código no Blender para a cidade, o personagem e o carro. Segundo o criador, sete GPUs alugadas renderizaram o resultado em 4K. O vídeo publicado mostra as tomadas finalizadas.

Type: Demo | Date: 2026-11-13

---

<a id="case-479"></a>
### Case 479: [Cenas noturnas desenhadas com JavaScript](https://x.com/kloss_xyz/status/2121356668311384487) (por [@kloss_xyz](https://x.com/kloss_xyz))

**Examine várias imagens concluídas ao avaliar ilustrações feitas com código.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/6e9d554b17822715f07d3be8.jpg" alt="Case 479 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/f57db49bb8213cc6ca4bcafe.jpg" alt="Case 479 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/2933b30de09501dbbb7e1505.jpg" alt="Case 479 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/490e5952694322b7963be8e2.jpg" alt="Case 479 · 4" width="450"></td></tr></table>

O autor atribui ao Fable 5.2 o desenho em JavaScript das quatro ilustrações publicadas. Os anexos mostram cenas noturnas estilizadas que permitem comparar os resultados.

Type: Demo | Date: 2026-11-13

---

<a id="case-480"></a>
### Case 480: [De modelos CAD a desenhos técnicos](https://x.com/MecAgent/status/2121352868490100787) (por [@MecAgent](https://x.com/MecAgent))

**Compare as vistas, cotas e anotações com o modelo CAD original.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/5ce59334e405a279e1008bf0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/780dc65cb1b04f7a75e27ace.jpg" alt="Case 480 · 1" width="760"><br>▶ Reproduzir vídeo</a>

A demonstração da MecAgent mostra desenhos técnicos com múltiplas vistas e anotações e atribui a conversão ao Fable 5.2. O vídeo apresenta as pranchas resultantes. A precisão das cotas teria de ser conferida nos arquivos CAD.

Type: Demo | Date: 2026-11-13

---

<a id="case-481"></a>
### Case 481: [As 43 tarefas do teste de análise do Plotly](https://plotly.com/blog/gemini-4-hydrogen-plotly-data-analytics-bench/) (por [Plotly](https://plotly.com/))

**Compare a precisão e o custo por execução no mesmo ambiente de teste.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/50882a17db12bede9165a92d.webp" alt="Case 481 · 1" width="760">

O relatório do Plotly coloca o Fable 5.2 entre os quatro modelos que acertaram as 43 questões, incluindo as cinco sobre padrões ocultos. O Plotly ressalta que uma execução por modelo fornece uma única observação. O gráfico apresenta o custo e a precisão do teste.

[Material relacionado 1](https://news.ycombinator.com/item?id=50485733)

Type: Benchmark | Date: 2026-11-12

---

<a id="case-482"></a>
### Case 482: [Uma estação SGI Indy recriada como site](https://news.ycombinator.com/item?id=50476597) (por [@gdubs](https://news.ycombinator.com/user?id=gdubs))

**Explore como uma estação de trabalho física pode virar um site por meio de uma recriação interativa.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/74b80686867b920881164246.jpg" alt="Case 482 · 1" width="760">

Gregory Wieber atribui ao Fable 5.2 a transformação de seu site em uma Silicon Graphics Indy dos anos 1990. A demonstração apresenta uma estação de trabalho 3D com login, um sistema de arquivos em 3D e o jogo Soft Break.

[Material relacionado 1](https://gregorywieber.com/indy/)

Type: Demo | Date: 2026-11-13

---

<a id="case-483"></a>
### Case 483: [Coordenação de agentes com issues e worktrees](https://news.ycombinator.com/item?id=50493545) (por [@nickalaso](https://news.ycombinator.com/user?id=nickalaso))

**Use issues para atribuir tarefas e worktrees e pull requests para isolar mudanças.**

O autor relata que usa o Fable 5.2 como coordenador principal, instâncias do Opus como coordenadores secundários e um servidor MCP próprio para iniciar agentes de vários fornecedores. Usa issues do GitHub para acompanhar o trabalho e worktrees e pull requests para evitar conflitos.

Type: Integration | Date: 2026-11-14

---

<a id="case-484"></a>
### Case 484: [Verificação de citações com agentes em segundo plano](https://x.com/tukiyomiiori/status/2121368478364192930) (por [@tukiyomiiori](https://x.com/tukiyomiiori))

**Delegue a conferência de citações e observe quando a sessão principal volta a rodar.**

O autor relata que pediu ao Fable 5.2 para conferir os artigos citados usando subagentes e scripts em segundo plano. Observou que a sessão do Claude Code pausava durante a execução e retomava quando os agentes ou scripts paravam.

Type: Integration | Date: 2026-11-13

---

<a id="case-485"></a>
### Case 485: [Depuração de um modelo de frete de ida e volta](https://x.com/allTheYud/status/2121360145921998877) (por [@allTheYud](https://x.com/allTheYud))

**Verifique se o modelo atribui corretamente os custos marginais ao trecho de volta.**

Em uma simulação de frete em dois sentidos, o autor afirma que o Fable 5.2 atribuiu a um trecho o combustível de ida e volta e tratou o outro como marginal, embora o navio tivesse de voltar. O autor precisou de várias rodadas de depuração para corrigir falhas desse tipo.

Type: Limit | Date: 2026-11-13

---

<a id="case-486"></a>
### Case 486: [Adaptação da inferência do Edge0 para Mac](https://news.ycombinator.com/item?id=50482710) (por [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen))

**Peça as mudanças de plataforma e teste a inferência no equipamento de destino.**

Em uma discussão sobre o Edge0-145B, um comentarista diz que pediu ao Fable 5.2 uma versão compatível com Mac e fez alguns ajustes. Em sua configuração com M5 Max e NVFP4, relata cerca de 50 tokens por segundo.

[Material relacionado 1](https://news.ycombinator.com/item?id=50475713)

Type: Integration | Date: 2026-11-13

---

<a id="case-487"></a>
### Case 487: [Revisão de placas de circuito de alta densidade](https://news.ycombinator.com/item?id=50478759) (por [@0_____0](https://news.ycombinator.com/user?id=0_____0))

**Confira o posicionamento e a escolha dos componentes à luz dos requisitos de desempenho da placa.**

Um comentarista do Hacker News testou o Fable 5.2 no posicionamento de componentes e no roteamento de trilhas de várias placas. Segundo ele, um layout denso parecia promissor no começo. Para atender aos requisitos, precisou fazer mudanças importantes no posicionamento e redesenhar manualmente a maior parte do esquema.

Type: Limit | Date: 2026-11-13

---

<a id="case-488"></a>
### Case 488: [Rastreamento de uma citação em um jornal pago](https://news.ycombinator.com/item?id=50478191) (por [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff))

**Trate a atribuição como provisória até conferir o texto original.**

Um comentarista do Hacker News rastreou uma atribuição a uma matéria de 1985 do The Dallas Morning News citada em uma lista de e-mails de linguística. Segundo ele, o Fable 5.2 não conseguiu abrir a matéria completa e sugeriu um possível repórter e contexto. A confirmação depende de acesso ao texto original.

[Material relacionado 1](https://listserv.linguistlist.org/pipermail/ads-l/2003-September/033575.html)

Type: Limit | Date: 2026-11-13

---

<a id="case-489"></a>
### Case 489: [Planejamento com o Fable e revisão das mudanças do Opus](https://news.ycombinator.com/item?id=50477200) (por [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology))

**Aprove um plano por escrito, divida a implementação em frentes de trabalho e confira as mudanças na CI e na homologação.**

O autor compartilha um fluxo que diz ter usado em bases grandes de código. O Fable 5.2 planeja, subagentes do Opus 5.5 implementam e revisam, a integração contínua protege a cobertura de testes e uma lista de homologação orienta a verificação manual.

Type: Tutorial | Date: 2026-11-13

---

<a id="acknowledge"></a>
## Créditos

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/), [@fe_yukichi](https://x.com/fe_yukichi), [u/wollymonjac](https://www.reddit.com/user/wollymonjac/), [@lukaspet](https://x.com/lukaspet), [@DJ_HYSNS](https://x.com/DJ_HYSNS), [@joaoavf](https://x.com/joaoavf), [@aimikoda](https://x.com/aimikoda), [@ingi_erlingsson](https://x.com/ingi_erlingsson), [@hanghuang_](https://x.com/hanghuang_), [@MecAgent](https://x.com/MecAgent), [Plotly](https://plotly.com/), [@gdubs](https://news.ycombinator.com/user?id=gdubs), [@nickalaso](https://news.ycombinator.com/user?id=nickalaso), [@tukiyomiiori](https://x.com/tukiyomiiori), [@allTheYud](https://x.com/allTheYud), [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen), [@0_____0](https://news.ycombinator.com/user?id=0_____0), [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff), [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology)
