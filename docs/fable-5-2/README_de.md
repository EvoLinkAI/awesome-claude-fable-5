# Anwendungsfälle für Claude Fable 5.2

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

Arbeitsabläufe, Demos, Vergleiche, Benchmarks, Integrationen und praktische Grenzen aus der Sammlung vom 10. November, jeweils mit Quellen.

[Ankündigung von Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [Frühere Sammlung](../../README_de.md)

## Fallübersicht

| Case | Anwendungsfälle | Type |
| --- | --- | --- |
| 330 | [MacBook-Zeichnung als SVG auf mehreren Aufwandsstufen](#case-330) | Benchmark |
| 331 | [Beat ’em up für vier Spieler aus Familienzeichnungen](#case-331) | Demo |
| 332 | [Drei elektronische Geräte vom Entwurf bis zur Montage](#case-332) | Demo |
| 333 | [Formalisierung von Fermats letztem Satz in Lean](#case-333) | Evaluation |
| 334 | [Ein Betriebssystem aus einem leeren Ordner](#case-334) | Demo |
| 335 | [Zweiarmige Manipulation in RoboDojo](#case-335) | Benchmark |
| 336 | [Ein Springbrunnen in Bewegung](#case-336) | Demo |
| 337 | [Bildgenaue Lippensynchronisation mit Higgsfield](#case-337) | Integration |
| 338 | [Ein Open-World-Fahrprototyp](#case-338) | Demo |
| 339 | [Paris 1940 mit Referenzbildern](#case-339) | Integration |
| 340 | [Fable plant einen von Opus gerenderten Kurzfilm](#case-340) | Integration |
| 341 | [Ein Musikvideo-Experiment](#case-341) | Demo |
| 342 | [Ein gemaltes Porträt von Dario Amodei](#case-342) | Demo |
| 343 | [Spud Smash auf Medium](#case-343) | Demo |
| 344 | [Eiskathedrale mit Fable und Opus](#case-344) | Evaluation |
| 345 | [Gesang mit simulierten Vokaltrakten](#case-345) | Demo |
| 346 | [Drei Voxel-Tests in Istanbul](#case-346) | Evaluation |
| 347 | [Abgeschlossene Projekte im Remote Labor Index](#case-347) | Benchmark |
| 348 | [Eisbergszene auf vier Aufwandsstufen](#case-348) | Evaluation |
| 349 | [Ein 79 Sekunden langer Anime-Kurzfilm](#case-349) | Demo |
| 350 | [Mechanische Baugruppen mit Fable und Opus](#case-350) | Evaluation |
| 351 | [Eine Roboterhand erklimmt eine Wendeltreppe](#case-351) | Demo |
| 352 | [Rigging eines Tripo-Meshs in Blender](#case-352) | Evaluation |
| 353 | [Interaktive Erfindungen aus Da Vincis Notizbuch](#case-353) | Demo |
| 354 | [Eine von Claude gesteuerte Audioworkstation](#case-354) | Demo |
| 355 | [Ein animierter Raspberry Pi 5](#case-355) | Demo |
| 356 | [Eine Szene in Norditalien](#case-356) | Demo |
| 357 | [Pop-up-Buch mit lokalen Bauagenten](#case-357) | Evaluation |
| 358 | [Ein wiederaufgenommener Lavalampen-Test](#case-358) | Evaluation |
| 359 | [Ein detaillierter Jet in Blender](#case-359) | Integration |
| 360 | [Portalreise durch Hunderte Welten](#case-360) | Demo |
| 361 | [Ein Basar in Bombay in sechs Einstellungen mit Three.js](#case-361) | Integration |
| 362 | [Ein fotorealistisches Diner aus Code](#case-362) | Integration |
| 363 | [Ein Robotermodell in Blender](#case-363) | Demo |
| 364 | [Ein Motion-Graphics-Erklärvideo für Convex](#case-364) | Demo |
| 365 | [Eine Sammlung von Landingpages aus Einzelprompts](#case-365) | Demo |
| 366 | [Eine Klaviersonate in LilyPond](#case-366) | Demo |
| 367 | [Eine freie Videovorgabe](#case-367) | Demo |
| 368 | [Fable plant, DeepSeek baut, Opus prüft](#case-368) | Integration |
| 369 | [Fable 5.2 in AI Village](#case-369) | Integration |
| 370 | [Frontend-Design mit und ohne Skills](#case-370) | Evaluation |
| 371 | [Implizite Zustandsautomaten im Code finden](#case-371) | Tutorial |
| 372 | [Ein Spiel von Grund auf in acht Stunden](#case-372) | Demo |
| 373 | [Fishslop-Prototyp und Tokenkosten](#case-373) | Evaluation |
| 374 | [Ein American-Football-Spiel in Bewegung](#case-374) | Demo |
| 375 | [Open-World-Bosskampf mit Higgsfield MCP](#case-375) | Integration |
| 376 | [Mont Saint-Michel im Wechsel der Gezeiten](#case-376) | Demo |
| 377 | [Ein Roblox-Asset in Blender](#case-377) | Demo |
| 378 | [Schlussfolgern ohne ausgegebene Gedankenkette](#case-378) | Benchmark |
| 379 | [Chrome-Dino-Neuauflagen mit vier Modellen](#case-379) | Evaluation |
| 380 | [Dame mit einem Roboterarm](#case-380) | Demo |
| 381 | [Ein Motion-Graphics-Clip in fünfzehn Sekunden](#case-381) | Demo |
| 382 | [Ein spielbarer Eiffelturm](#case-382) | Demo |
| 383 | [Hochseerennen mit Three.js und Higgsfield](#case-383) | Integration |
| 384 | [Echtzeit-Honigsimulation in WebGL](#case-384) | Demo |
| 385 | [Programmierte visuelle Effekte auf Videoaufnahmen](#case-385) | Demo |
| 386 | [Animierte Erklärung der Fahndungsstufen in GTA](#case-386) | Demo |
| 387 | [Eine stilisierte MMO-Welt aus Code](#case-387) | Demo |
| 388 | [Eine 3D-Szene mit Fable und Opus](#case-388) | Evaluation |
| 389 | [Überflüssige Erklärungen im Pausenmenü](#case-389) | Limit |
| 390 | [Moodboards mit einer Krea-Umgebung](#case-390) | Integration |
| 391 | [Büro-Spieltest eines Portal-Shooters](#case-391) | Demo |
| 392 | [Ein detailliertes Hard-Surface-Asset in Blender](#case-392) | Demo |
| 393 | [Parallele Frontend-Tests auf mehreren Aufwandsstufen](#case-393) | Evaluation |
| 394 | [Ein kleines Spiel in zehn Prompts](#case-394) | Demo |
| 395 | [Bild-für-Bild-Animation in JavaScript](#case-395) | Demo |
| 396 | [Von der Videovorlage zur 3D-Animation](#case-396) | Demo |
| 397 | [Pixel-Lagerfeuer mit Fable und Opus](#case-397) | Evaluation |
| 398 | [Arena WebDev auf xHigh](#case-398) | Benchmark |
| 399 | [Filmtrailer-Typografie mit zwei Modellen](#case-399) | Evaluation |
| 400 | [Motion-Design- und 3D-Portfolio-Tests mit einem Prompt](#case-400) | Evaluation |
| 401 | [Ein zerlegbares Modell eines Kernreaktors](#case-401) | Demo |
| 402 | [Agenten in Blood on the Clocktower](#case-402) | Benchmark |
| 403 | [Ein Podrennen-Prototyp](#case-403) | Demo |
| 404 | [Zehn Sekunden Werbung für Claude-Unterwäsche](#case-404) | Demo |
| 405 | [Ein Vogel bei Sonnenaufgang, Strich für Strich](#case-405) | Demo |
| 406 | [Ein langer Grafiklauf in Devin](#case-406) | Evaluation |
| 407 | [Mit Code gemalte Kunst von drei Modellen](#case-407) | Evaluation |
| 408 | [Die Geschichte der Schrift in Bewegung](#case-408) | Demo |
| 409 | [Testgelände für Spielmaschinen](#case-409) | Demo |
| 410 | [Platine für eine tragbare Linux-Konsole](#case-410) | Evaluation |
| 411 | [Ein See aus Voxeln](#case-411) | Demo |
| 412 | [17 interaktive Ergebnisse von Arena](#case-412) | Demo |
| 413 | [Flug mit einem freundlichen Drachen](#case-413) | Demo |
| 414 | [Gelee-Orca mit Fable und Opus](#case-414) | Evaluation |
| 415 | [Offener Test der Videoqualität](#case-415) | Demo |
| 416 | [Weltraumhabitat mit mediterranem Thema](#case-416) | Demo |
| 417 | [AA-3D-Benchmark für interaktive Erlebnisse](#case-417) | Benchmark |
| 418 | [Ein Spiel mit Skelettfigur und Zeitlimit](#case-418) | Demo |
| 419 | [Pixelgrafik mit Fable und Astra](#case-419) | Evaluation |
| 420 | [Portfolio-Reel für Motion Design](#case-420) | Demo |
| 421 | [Rendering eines Glaspools mit zwei Modellen](#case-421) | Evaluation |
| 422 | [Genauigkeit von Werkzeugaufrufen in TS-Bench](#case-422) | Benchmark |
| 423 | [Machu Picchu als Miniaturwelt](#case-423) | Demo |
| 424 | [GDPx nach beruflichen Aufgabenkategorien](#case-424) | Benchmark |
| 425 | [Ein Porträt in einem Zeichenprogramm](#case-425) | Demo |
| 426 | [VulcanBench Frontier v4 mit Einstellung Low](#case-426) | Benchmark |
| 427 | [Spielbare Backrooms mit vertauschten Rollen](#case-427) | Demo |
| 428 | [Bugatti Tourbillon mit Blender modellieren](#case-428) | Demo |
| 429 | [Ein Computer-Video mit zwei Modellen](#case-429) | Demo |
| 430 | [Ein Musikvideo über Megakernels](#case-430) | Demo |
| 431 | [Studio-Rundgang aus Referenzfotos](#case-431) | Demo |
| 432 | [Spielzeugwerbung im Stil der 1990er aus Code](#case-432) | Demo |
| 433 | [Eine Three.js-Spielszene in Third-Person-Perspektive](#case-433) | Demo |
| 434 | [Bryceball auf Basis eines vorhandenen Renderers](#case-434) | Demo |
| 435 | [Rekursiver Videoschnitt mit Fable](#case-435) | Demo |
| 436 | [Eine filmische Geschichte der Wissenschaft](#case-436) | Demo |
| 437 | [Da Vincis Flugmaschine in 3D](#case-437) | Integration |
| 438 | [Leiterplatten-Routing nach Entwurfsvorgabe](#case-438) | Demo |
| 439 | [Derselbe Prompt in unterschiedlichen Laufzeitumgebungen](#case-439) | Evaluation |
| 440 | [Mit Code gezeichnete Godzilla-Illustration](#case-440) | Demo |
| 441 | [Handventilator für den 3D-Druck](#case-441) | Demo |
| 442 | [Fehlersuche in einem Plugin im Vergleich mit Opus](#case-442) | Evaluation |
| 443 | [Istanbul als 3D-Szene nachgebaut](#case-443) | Demo |
| 444 | [Ein Blender-Film mit funktionierendem Bildschirm](#case-444) | Demo |
| 445 | [Ein Schwarzes-Loch-Übergang bei schwacher Kopplung](#case-445) | Evaluation |
| 446 | [Die Grenze einer modularen Bootstrap-Schranke](#case-446) | Evaluation |
| 447 | [Vercel AI Gateway mit geordneten Fallback-Modellen](#case-447) | Integration |
| 448 | [Verschachtelte Subagenten und Review-Budget](#case-448) | Limit |
| 449 | [LCARS-Design als HTML im Modellvergleich](#case-449) | Evaluation |
| 450 | [GPU-Optimierung für Quantum ESPRESSO](#case-450) | Benchmark |
| 451 | [Artificial Analysis Intelligence Index nach Aufwandsstufe](#case-451) | Benchmark |
| 452 | [Fehlalarme in einem Änderungsreview auf High](#case-452) | Limit |
| 453 | [Dreißig alltägliche Programmieraufgaben](#case-453) | Evaluation |
| 454 | [Bildschirmschoner mit einer einsamen Insel](#case-454) | Demo |
| 455 | [Drei Browserspiele auf Aufwandsstufe High](#case-455) | Evaluation |
| 456 | [Buchpodcast-Skripte Kapitel für Kapitel](#case-456) | Evaluation |
| 457 | [Ein Produktivdienst nach Rust migriert](#case-457) | Evaluation |
| 458 | [Fable 5.2 in GitHub Copilot auswählen](#case-458) | Integration |
| 459 | [Eine Designaufgabe mit hundert HTML-Seiten](#case-459) | Evaluation |
| 460 | [Abweichende Anforderungen bei einer Compiler-Aufgabe](#case-460) | Limit |
| 461 | [Einen langen Fable-Lauf mit Opus verfolgen](#case-461) | Integration |
| 462 | [Code-Review mit frischem Blick](#case-462) | Tutorial |
| 463 | [Kontextverlust beim Review eines Funktionsentwurfs](#case-463) | Limit |
| 464 | [Breakout-Vergleich im Stil von DX Ball](#case-464) | Evaluation |
| 465 | [Ein Versuch zur Verbesserung einer 3D-App](#case-465) | Evaluation |
| 466 | [Maus-und-Katze-Spiel mit drei Modellen](#case-466) | Evaluation |
| 467 | [Kosten und Punktzahl in AIBenchy auf High](#case-467) | Benchmark |
| 468 | [Die Agentenumgebung für Fable 5.2 abstimmen](#case-468) | Tutorial |

<a id="fable-5-2-cases"></a>
## Anwendungsfälle

<a id="case-330"></a>
### Case 330: [MacBook-Zeichnung als SVG auf mehreren Aufwandsstufen](https://playcode.io/blog/macbook-svg-benchmark#compare) (von [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**Vergleiche Zeichnungsqualität, Tokenverbrauch und Ausgabelimits bei gleicher Vorgabe.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode meldet für Fable 5.2 High 76.158 Tokens für 3,05 US-Dollar. Xhigh und Max erreichten beim Streaming das Limit von 128.000 Tokens ohne Zeichnung und wurden erst mit mehr Spielraum über die Batch API fertig. Die Platzierung folgt dem visuellen Urteil des Herausgebers.

[Weiterführende Quellen 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [Beat ’em up für vier Spieler aus Familienzeichnungen](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (von [Lex](https://notesbylex.com/))

**Gib dem Coding-Agenten Skizzen, einen Prototyp und konkrete Controller-Anforderungen.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex machte mit Claude Code aus einem früheren Side-Scroller ein Beat ’em up mit 12 Levels und 18 Figuren. Bild- und Audiowerkzeuge lieferten Assets. Beim Familientest funktionierten vier Controller.

[Weiterführende Quellen 1](https://aidens-revenge.pages.dev/) · [Weiterführende Quellen 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [Weiterführende Quellen 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [Drei elektronische Geräte vom Entwurf bis zur Montage](https://www.anthropic.com/research/claude-electronics-design) (von [@Anthropic](https://www.anthropic.com/))

**Prüfe Schaltung, Gehäuse und Firmware als Gesamtsystem.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ Video abspielen</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic und Diode berichten von drei funktionierenden Geräten. Fable 5.2 routete Platinen, modellierte Gehäuse, schrieb Software und leitete Tests nach der Fertigung an.

[Weiterführende Quellen 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [Weiterführende Quellen 2](https://www.youtube.com/watch?v=vdYynH177h0) · [Weiterführende Quellen 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [Formalisierung von Fermats letztem Satz in Lean](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (von [@Anthropic](https://www.anthropic.com/))

**Nutze einen Beweisprüfer und Zwischensätze als Meilensteine.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Anthropic zufolge formalisierten 1.000 Fable-5.2-Agenten den vorhandenen Beweis in 30 Stunden. Opus 5.5 erreichte mit demselben Teamaufbau 26 % in 18 Stunden.

[Weiterführende Quellen 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [Weiterführende Quellen 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [Ein Betriebssystem aus einem leeren Ordner](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (von [@Anthropic](https://www.anthropic.com/))

**Prüfe Start, Treiber, Speicher und Installation getrennt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ Video abspielen</a>

Anthropic berichtet, dass Fable 5.2 in acht Tagen mehr als 1.000 Subagenten koordinierte. Der Betriebssystemprototyp startete auf einem Laptop.

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [Zweiarmige Manipulation in RoboDojo](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (von [@Anthropic](https://www.anthropic.com/))

**Vergleiche Modelle an denselben simulierten Manipulationsaufgaben.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ Video abspielen</a>

Anthropic nennt für RoboDojo 64,9 % für Fable 5.2 gegenüber 27,6 % für Fable 5.1. Die Ankündigung enthält eine Robotik-Demo.

[Weiterführende Quellen 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [Ein Springbrunnen in Bewegung](https://x.com/Angaisb_/status/2119909059277238733) (von [@Angaisb_](https://x.com/Angaisb_))

**Beurteile den visuellen Rhythmus anhand eines kontinuierlichen Wasserflusses.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

Der Autor zeigt eine Springbrunnenszene, die er Fable 5.2 zuschreibt.

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [Bildgenaue Lippensynchronisation mit Higgsfield](https://x.com/higgsfield_ai/status/2119909938969580024) (von [@higgsfield_ai](https://x.com/higgsfield_ai))

**Stimme den Ton auf Einzelbilder ab, bevor du den Clip prüfst.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ Video abspielen</a>

Higgsfield berichtet, in einem Ablauf mit Fable 5.2 die Mundbewegung verfolgt und den Ton auf die Einzelbilder abgestimmt zu haben.

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [Ein Open-World-Fahrprototyp](https://x.com/ericmaskfr/status/2119910195325481026) (von [@ericmaskfr](https://x.com/ericmaskfr))

**Teste eine kurze Open-World-Vorgabe an einem spielbaren Ausschnitt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt einen von GTA inspirierten Prototyp und berichtet von rund 2 Stunden und 14 Minuten Laufzeit.

Originalprompt

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [Paris 1940 mit Referenzbildern](https://x.com/higgsfield_ai/status/2119910344998912507) (von [@higgsfield_ai](https://x.com/higgsfield_ai))

**Trenne Referenzbilderzeugung und Szenencode.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ Video abspielen</a>

Higgsfield lieferte Referenzbilder über sein MCP und nutzte Fable 5.2 für eine Three.js-Szene.

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable plant einen von Opus gerenderten Kurzfilm](https://x.com/kloss_xyz/status/2119910613828980846) (von [@kloss_xyz](https://x.com/kloss_xyz))

**Trenne Planung und Umsetzung im Video-Workflow.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ Video abspielen</a>

Fable 5.2 schrieb Vorgabe und Plan. Opus 5.5 setzte die 16-sekündige Animation in Blender und Python um und synthetisierte die Musik.

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [Ein Musikvideo-Experiment](https://x.com/WesRoth/status/2119911161386934330) (von [@WesRoth](https://x.com/WesRoth))

**Prüfe sowohl den Text als auch die generierte Sequenz.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt ein mit Fable 5.2 erstelltes Musikvideo und kommentiert den Liedtext.

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Ein gemaltes Porträt von Dario Amodei](https://x.com/Mr_Salio/status/2119911922577637543) (von [@Mr_Salio](https://x.com/Mr_Salio))

**Vergleiche das stilisierte Porträt mit der daneben gezeigten Referenz.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt ein Porträt von Dario Amodei, das er Fable 5.2 zuschreibt.

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [Spud Smash auf Medium](https://x.com/argofowl/status/2119913148929187960) (von [@argofowl](https://x.com/argofowl))

**Gib einem Spielprototyp klare Aktionen und ein Ziel.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt eine Kartoffelfigur, die blaue Stühle schlägt, mit dem Kopf rammt oder verbrennt.

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Eiskathedrale mit Fable und Opus](https://x.com/QQTeng/status/2119913518015435103) (von [@QQTeng](https://x.com/QQTeng))

**Vergleiche Generierungszeit und Kosten für dieselbe Szene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor nennt etwa 1 Std. 57 Min. und 81,10 US-Dollar für Fable gegenüber rund 3 Std. 11 Min. und 45,97 US-Dollar für Opus.

Originalprompt

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [Gesang mit simulierten Vokaltrakten](https://x.com/banteg/status/2119914098171199996) (von [@banteg](https://x.com/banteg))

**Nutze ein physikalisches Stimmmodell für die Musikproduktion.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt eine Coverversion aus zwei Chimera-Vokaltraktsimulationen und einem Vocoder-Mix.

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [Drei Voxel-Tests in Istanbul](https://x.com/Avenoxai/status/2119914308603953485) (von [@Avenoxai](https://x.com/Avenoxai))

**Vergleiche eine Zerstörungsszene, eine funktionierende Uhr und eine Karte.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt drei Tests mit je einem Prompt und nennt nach eigener Bewertung 100, 100 und 95,6 Punkte.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Abgeschlossene Projekte im Remote Labor Index](https://x.com/ScaleAILabs/status/2119914701736075489) (von [@ScaleAILabs](https://x.com/ScaleAILabs))

**Interpretiere die Quote im Kontext der bewerteten Projekte.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ Video abspielen</a>

Scale Labs und CAIS berichten, dass Fable 5.2 41,3 % der bewerteten Projekte für Fernarbeit erfolgreich abschloss.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [Eisbergszene auf vier Aufwandsstufen](https://x.com/0xRhinoX/status/2119915121698840587) (von [@0xRhinoX](https://x.com/0xRhinoX))

**Vergleiche Fertigstellung, Kosten und Detailgrad bei steigendem Aufwand.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor nutzte auf vier Stufen denselben Prompt. High ließ das Polarlicht weg. Ultra ergänzte leuchtendes Eis und eine Unterwasseransicht.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [Ein 79 Sekunden langer Anime-Kurzfilm](https://x.com/anstapnever/status/2119915123070644263) (von [@anstapnever](https://x.com/anstapnever))

**Prüfe die Kontinuität von Szenen in einer längeren Animation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt einen 79-sekündigen Anime-Clip aus einem Workflow mit Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Mechanische Baugruppen mit Fable und Opus](https://x.com/ivanainai/status/2119915243321397550) (von [@ivanainai](https://x.com/ivanainai))

**Vergleiche, wie die Modelle eine mechanische Baugruppe anordnen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt beschriftete Explosionsdarstellungen eines Rads und Getriebes von Fable 5.2 und Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [Eine Roboterhand erklimmt eine Wendeltreppe](https://x.com/Luckyballa/status/2119915557663506720) (von [@Luckyballa](https://x.com/Luckyballa))

**Nutze ein simuliertes Hindernis, um ungewöhnliche Fortbewegung zu untersuchen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt einen Versuch mit Fable 5.2 und Steel 0.1, bei dem eine Wuji-Hand auf ihren Fingern läuft.

[Weiterführende Quellen 1](https://github.com/skild-ai/steel-webgpu/pull/7)

Originalprompt

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [Rigging eines Tripo-Meshs in Blender](https://x.com/0xKense1/status/2119916096098582566) (von [@0xKense1](https://x.com/0xKense1))

**Nutze messbare Kriterien für Griff, Textur und Verformung.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor vergleicht zwei Rigs aus Tripo-Assets. Fable erzeugte zwei Clips in 36 Minuten, Opus acht in etwa 21 Minuten.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [Interaktive Erfindungen aus Da Vincis Notizbuch](https://x.com/alexalbert__/status/2119916954337349737) (von [@alexalbert__](https://x.com/alexalbert__))

**Stütze ein interaktives Lernmodell auf Originalzeichnungen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ Video abspielen</a>

Alex Albert lieferte ein PDF von Leonardos Notizbuch und zeigte eine interaktive Umsetzung seiner Erfindungen.

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [Eine von Claude gesteuerte Audioworkstation](https://x.com/The_Alex/status/2119917226769985785) (von [@The_Alex](https://x.com/The_Alex))

**Nutze ein agentengesteuertes Werkzeug für wiederkehrende Kompositionsaufträge.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt eine digitale Audioworkstation aus Fable 5.2 und berichtet, dass Opus sie später zur Komposition eines Stücks öffnete.

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [Ein animierter Raspberry Pi 5](https://x.com/sparklabhq/status/2119917375080521921) (von [@sparklabhq](https://x.com/sparklabhq))

**Nutze eine Produktanimation zur Prüfung der Bauteile.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt einen mit Fable 5.2 animierten Raspberry Pi 5.

Originalprompt

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [Eine Szene in Norditalien](https://x.com/Angaisb_/status/2119917807119089926) (von [@Angaisb_](https://x.com/Angaisb_))

**Beurteile Landschaft und Atmosphäre bei einer ortsbezogenen Vorgabe.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt eine Szene aus Fable 5.2, die in Norditalien spielt.

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [Pop-up-Buch mit lokalen Bauagenten](https://x.com/atomicagent_io/status/2119918110752846094) (von [@atomicagent_io](https://x.com/atomicagent_io))

**Vergleiche Orchestrierung und Einzellauf am selben Auftrag.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ Video abspielen</a>

Atomic meldet 2,98 US-Dollar und 11 Minuten mit Fable als Koordinator lokaler Qwen-Agenten gegenüber 15,77 US-Dollar und 21 Minuten mit Fable allein.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [Ein wiederaufgenommener Lavalampen-Test](https://x.com/eidzoku/status/2119918134060601690) (von [@eidzoku](https://x.com/eidzoku))

**Vergleiche mehrere Modelle an derselben visuellen Aufgabe.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor legte einen Lavalampen-Test neu auf und teilt den visuellen Vergleich.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [Ein detaillierter Jet in Blender](https://x.com/higgsfield_ai/status/2119918248955392431) (von [@higgsfield_ai](https://x.com/higgsfield_ai))

**Lege Teilezahl, Dauer und Erscheinungsbild in der Vorgabe fest.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ Video abspielen</a>

Higgsfield beschreibt ein per Skript erzeugtes Blender-Modell mit 931 Teilen und 24.260 Nieten, erstellt mit Fable 5.2 und dem eigenen MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [Portalreise durch Hunderte Welten](https://x.com/emollick/status/2119918307457577163) (von [@emollick](https://x.com/emollick))

**Verbinde unabhängig erzeugte Umgebungen über Portale.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ Video abspielen</a>

Ethan Mollick berichtet von über 450 programmierten Welten aus der Arbeit von 25.000 Agenten und teilt die spielbare Fassung und das Repository.

[Weiterführende Quellen 1](https://portals-endless-worlds.netlify.app/) · [Weiterführende Quellen 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [Ein Basar in Bombay in sechs Einstellungen mit Three.js](https://x.com/higgsfield_ai/status/2119918834841010320) (von [@higgsfield_ai](https://x.com/higgsfield_ai))

**Teile die Bildvorgabe in Einstellungen mit fester Dauer auf.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ Video abspielen</a>

Higgsfield zeigt eine 21,5 Sekunden lange Basarsequenz mit sechs in Three.js gerenderten Einstellungen.

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [Ein fotorealistisches Diner aus Code](https://x.com/higgsfield_ai/status/2119918838490010008) (von [@higgsfield_ai](https://x.com/higgsfield_ai))

**Prüfe Material und Beleuchtung anhand einer programmierten Szene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ Video abspielen</a>

Higgsfield zeigt ein Diner und berichtet, die Szene allein mit Code und ohne 3D-Modellierungssoftware erstellt zu haben.

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [Ein Robotermodell in Blender](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (von [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Prüfe Gelenke und Silhouette in einer Drehansicht.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt einen kleinen mechanischen Roboter aus einer Blender-Demo mit Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [Ein Motion-Graphics-Erklärvideo für Convex](https://x.com/Rasmic/status/2119919466163093768) (von [@Rasmic](https://x.com/Rasmic))

**Erkläre ein Entwicklerprodukt mit einer kurzen Animation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor teilt ein animiertes Erklärvideo zu Convex, das mit Fable 5.2 entstand.

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [Eine Sammlung von Landingpages aus Einzelprompts](https://x.com/daradoescode/status/2119919529807466594) (von [@daradoescode](https://x.com/daradoescode))

**Vergleiche visuelle Hierarchie und Layout über mehrere kurze Vorgaben.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt in einem Video mehrere Landingpages aus Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [Eine Klaviersonate in LilyPond](https://x.com/imjustnewatai/status/2119919644836347926) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Halte die Partitur mit dem gerenderten Video verknüpft.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor bat um einen Satz im Stil Beethovens und berichtet, dass die gezeigten Noten aus der LilyPond-Datei stammen.

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [Eine freie Videovorgabe](https://x.com/aollivier82/status/2119920990893244510) (von [@aollivier82](https://x.com/aollivier82))

**Nutze eine offene Bildaufgabe, um kreative Standardeinstellungen zu beobachten.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt das Ergebnis seiner Bitte an Fable 5.2, das schönste mögliche Video zu machen.

Originalprompt

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable plant, DeepSeek baut, Opus prüft](https://x.com/ivanfioravanti/status/2119921810267636201) (von [@ivanfioravanti](https://x.com/ivanfioravanti))

**Verteile Koordination, Implementierung und Review auf getrennte Agenten.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ Video abspielen</a>

Fable koordiniert im Beispiel per herdr vier Agenten mit DeepSeek V4.1 Flash. Opus 5.5 prüft die Pull Requests.

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [Fable 5.2 in AI Village](https://x.com/aidigest_/status/2119923190411719158) (von [@aidigest_](https://x.com/aidigest_))

**Prüfen Sie die Antwort und die tatsächlichen Speicheraktionen getrennt.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

Im öffentlichen Protokoll sagt Fable einem anderen Agenten eine spätere Gedächtnisänderung zu. Ein weiterer Beitrag zeigt einen Test zur Zuordnung fiktiver Figuren.

[Weiterführende Quellen 1](https://x.com/aidigest_/status/2119923209311260707) · [Weiterführende Quellen 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [Frontend-Design mit und ohne Skills](https://x.com/AdamHoltererer/status/2119924849321914653) (von [@AdamHoltererer](https://x.com/AdamHoltererer))

**Halte das Modell konstant und ändere die Skill-Konfiguration.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

Der Autor zeigt zwei Frontend-Ergebnisse mit Fable 5.2, eines mit Skills und eines ohne.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [Implizite Zustandsautomaten im Code finden](https://x.com/kunchenguid/status/2119924895060795492) (von [@kunchenguid](https://x.com/kunchenguid))

**Prüfe ein konkretes Modul und fordere Vorher-Nachher-Diagramme an.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

Der Autor zeigt eine Bereinigung im Firstmate-Repository und veröffentlicht den genauen Prüf-Prompt.

[Weiterführende Quellen 1](https://github.com/kunchenguid/lavish-axi)

Originalprompt

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [Ein Spiel von Grund auf in acht Stunden](https://x.com/felixrieseberg/status/2119925633564463609) (von [@felixrieseberg](https://x.com/felixrieseberg))

**Erfasse zwischengespeicherte Eingaben, erzeugte Assets und Laufzeit.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ Video abspielen</a>

Der Anthropic-Ingenieur berichtet von Modellen, Sounds und Texturen aus einem einzigen Lauf für umgerechnet etwa 550 US-Dollar zu API-Preisen.

[Weiterführende Quellen 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [Weiterführende Quellen 2](https://x.com/AndrewCurran_/status/2119953960794780133)

Originalprompt

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Fishslop-Prototyp und Tokenkosten](https://x.com/theo/status/2119926277801144695) (von [@theo](https://x.com/theo))

**Vergleiche einen Spielentwurf mit einem früheren Modellergebnis.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ Video abspielen</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

Der Autor nennt 76 Minuten und rund 42 US-Dollar an Tokenkosten und vergleicht das Ergebnis mit Opus 5.5.

[Weiterführende Quellen 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [Ein American-Football-Spiel in Bewegung](https://x.com/WesRoth/status/2119926801514529027) (von [@WesRoth](https://x.com/WesRoth))

**Prüfe Rückmeldungen und Punkteanzeigen im Sportprototyp.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt ein Fable-5.2-Spielergebnis mit eingeblendeten Spielstandsmeldungen.

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [Open-World-Bosskampf mit Higgsfield MCP](https://x.com/higgsfield_ai/status/2119926932343324795) (von [@higgsfield_ai](https://x.com/higgsfield_ai))

**Unterscheide das spielbare Spiel von seinen Zwischensequenzen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ Video abspielen</a>

Higgsfield beschreibt ein Browserspiel mit offener Welt, dreiteiligem Bosskampf und Zwischensequenzen mit Fable 5.2 und dem eigenen MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [Mont Saint-Michel im Wechsel der Gezeiten](https://x.com/loktar00/status/2119927152489472076) (von [@loktar00](https://x.com/loktar00))

**Teste wechselnde Wasserstände in einer kleinen historischen Szene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt Mont Saint-Michel als Miniatur mit animierten Gezeiten.

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [Ein Roblox-Asset in Blender](https://x.com/hiyouwhatsapp/status/2119927163264573642) (von [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**Prüfe das Asset vor dem Import in Blender.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt ein Blender-Ergebnis für Roblox, das mit fast nur einem Prompt entstand.

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [Schlussfolgern ohne ausgegebene Gedankenkette](https://x.com/Tim_Hua_/status/2119927284761293089) (von [@Tim_Hua_](https://x.com/Tim_Hua_))

**Bewerte Antworten unter derselben Ausgabebeschränkung.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

Der Tester führte Schlussfolgerungs- und Wissenstests ohne Ausgabe einer Gedankenkette aus und sieht Fable 5.2 knapp hinter GPT-6.1 Sol.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [Chrome-Dino-Neuauflagen mit vier Modellen](https://x.com/noclipepe/status/2119927838321328577) (von [@noclipepe](https://x.com/noclipepe))

**Vergleiche Zeit und Kosten anhand einer wiederkehrenden Spielvorgabe.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor ergänzt Fable 5.2 in einem T-Rex-Test mit Opus, Gemini und Astra und zeigt alle Ergebnisse zusammen.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [Dame mit einem Roboterarm](https://x.com/karolina_dubiel/status/2119928342115676576) (von [@karolina_dubiel](https://x.com/karolina_dubiel))

**Lies Gelenkpositionen zurück und wiederhole fehlgeschlagene Griffe.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor berichtet, dass das Modell ein Absinken von rund 7 mm korrigierte und fehlgeschlagene Bewegungen anhand der Rückmeldung wiederholte.

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [Ein Motion-Graphics-Clip in fünfzehn Sekunden](https://x.com/aziz4ai/status/2119928581405200726) (von [@aziz4ai](https://x.com/aziz4ai))

**Erfasse den Kontingentverbrauch bei einem kurzen Test mit Code-Animation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt eine 15-Sekunden-Szene aus Code und berichtet von 4 % seines Wochenkontingents.

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [Ein spielbarer Eiffelturm](https://x.com/bobyau/status/2119928812628771212) (von [@bobyau](https://x.com/bobyau))

**Prüfe, ob ein Wahrzeichenmodell Interaktion ermöglicht.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor teilt eine Eiffelturm-Demo und nennt 25 Minuten Entwicklungszeit.

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [Hochseerennen mit Three.js und Higgsfield](https://x.com/higgsfield_ai/status/2119928918035910668) (von [@higgsfield_ai](https://x.com/higgsfield_ai))

**Trenne Spiellogik und Medienwerkzeuge in einem gemischten Ablauf.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ Video abspielen</a>

Higgsfield zeigt ein Rennspiel mit hohen Wellen, fünf KI-Gegnern und zielsuchenden Raketen.

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [Echtzeit-Honigsimulation in WebGL](https://x.com/deedydas/status/2119930300990177509) (von [@deedydas](https://x.com/deedydas))

**Prüfe Materialbewegung mit einer Physiksimulation im Browser.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt eine Honigsimulation in WebGL und veröffentlicht die kurze Originalvorgabe.

Originalprompt

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [Programmierte visuelle Effekte auf Videoaufnahmen](https://x.com/ashebytes/status/2119930763105931649) (von [@ashebytes](https://x.com/ashebytes))

**Prüfe Zeitpunkt und Position der Effekte über dem Ausgangsmaterial.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt einen Effekttest mit Fable 5.2, bei dem animierte Grafiken über Realaufnahmen gelegt wurden.

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [Animierte Erklärung der Fahndungsstufen in GTA](https://x.com/saimagnate/status/2119931563760632311) (von [@saimagnate](https://x.com/saimagnate))

**Erklären Sie Spielmechaniken mit Spielszenen und Diagrammen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor berichtet von einer einzigen Anfrage an Fable 5.2. Das Video vergleicht mit Spielszenen und Diagrammen die Fahndungssysteme in GTA V und RDR2.

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [Eine stilisierte MMO-Welt aus Code](https://x.com/Izkimar/status/2119931740940640542) (von [@Izkimar](https://x.com/Izkimar))

**Beurteile die Einheitlichkeit einer Welt anhand stilisierter Assets.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor berichtet, die gezeigte MMO-Welt mit programmierten Assets an einem Tag gebaut zu haben.

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [Eine 3D-Szene mit Fable und Opus](https://x.com/dom_scholz/status/2119933150025363661) (von [@dom_scholz](https://x.com/dom_scholz))

**Vergleiche Vorbereitungszeit und Detailgrad in einer Ansicht.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt Renderings von Fable 5.2 und Opus 5.5 nebeneinander und berichtet, Fable sei schneller gewesen.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [Überflüssige Erklärungen im Pausenmenü](https://x.com/AndrewPrifer/status/2119934600608915465) (von [@AndrewPrifer](https://x.com/AndrewPrifer))

**Prüfe generierte Oberflächentexte auf Wiederholungen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

Der Entwickler zeigt anhand eines Pausenmenüs, dass Fable 5.2 mehr Erklärungen als nötig schrieb.

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [Moodboards mit einer Krea-Umgebung](https://x.com/lambdacalcc/status/2119934725662060663) (von [@lambdacalcc](https://x.com/lambdacalcc))

**Vergleiche Entwürfe vor der Wahl einer visuellen Richtung.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

Der Autor zeigt vier Ergebnisse einer Moodboard-Sitzung mit Fable 5.2 in einer Krea-Umgebung.

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [Büro-Spieltest eines Portal-Shooters](https://x.com/_sholtodouglas/status/2119935331499925557) (von [@_sholtodouglas](https://x.com/_sholtodouglas))

**Beurteile ein generiertes Spiel im Mehrspielerbetrieb.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ Video abspielen</a>

Ein Anthropic-Ingenieur zeigt einen Arena-FPS mit Portalen und beschreibt Spieltests im Büro.

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Ein detailliertes Hard-Surface-Asset in Blender](https://x.com/ziwenxu_/status/2119937420280168929) (von [@ziwenxu_](https://x.com/ziwenxu_))

**Prüfe Topologie und Silhouette im Blender-Ansichtsfenster.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt ein detailliertes Hard-Surface-Asset als Ergebnis von Fable 5.2 in Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [Parallele Frontend-Tests auf mehreren Aufwandsstufen](https://x.com/AI_masaou/status/2119937635322085640) (von [@AI_masaou](https://x.com/AI_masaou))

**Vergleiche einfache und anspruchsvolle Aufgaben auf mehreren Stufen.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

Der Autor berichtet von ähnlichen einfachen Ergebnissen, mehr Details bei größeren Fable-Projekten und einem starken Anstieg von Zeit und Tokenzahl zwischen Medium und High.

[Weiterführende Quellen 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [Ein kleines Spiel in zehn Prompts](https://x.com/AmirMushich/status/2119937977426338283) (von [@AmirMushich](https://x.com/AmirMushich))

**Erfasse die Zahl der Iterationen und die Dateigröße des Prototyps.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor nennt 220 KB und rund 3400 Zeilen Code und teilt den Code und einen Clip.

[Weiterführende Quellen 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [Bild-für-Bild-Animation in JavaScript](https://x.com/kevin_t_ngo/status/2119938129079808282) (von [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Prüfe eine Folge aus programmatisch gezeichneten Einzelbildern.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor teilt eine Animation und berichtet, dass JavaScript jedes Einzelbild zeichnete.

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [Von der Videovorlage zur 3D-Animation](https://x.com/KHvostikk/status/2119939061049889130) (von [@KHvostikk](https://x.com/KHvostikk))

**Prüfe eine rekonstruierte Szene anhand der Filmvorlage.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt, wie mit Fable 5.2 aus Video eine 3D-Animation entstand.

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Pixel-Lagerfeuer mit Fable und Opus](https://x.com/GrilliotTodd/status/2119939651385655692) (von [@GrilliotTodd](https://x.com/GrilliotTodd))

**Vergleiche Beleuchtung und Silhouetten am selben Pixelmotiv.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ Video abspielen</a>

Die nebeneinander gezeigten Ausgaben stellen ein Lagerfeuer von Fable 5.2 und Opus 5.5 dar.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [Arena WebDev auf xHigh](https://x.com/arena/status/2119941204003770690) (von [@arena](https://x.com/arena))

**Vergleiche die in der Rangliste verwendete Aufwandsstufe.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena meldet für Claude Fable 5.2 xHigh zum Start 1832 Punkte in Code Arena WebDev.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [Filmtrailer-Typografie mit zwei Modellen](https://x.com/muku_sns/status/2119941490969624679) (von [@muku_sns](https://x.com/muku_sns))

**Vergleiche zwei Interpretationen desselben Absatzes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt die Titel von Opus und Fable nebeneinander. Fable ergänzt eine rote Umrandung und geschwärzte Titel.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [Motion-Design- und 3D-Portfolio-Tests mit einem Prompt](https://x.com/Khazix0918/status/2119941585538572390) (von [@Khazix0918](https://x.com/Khazix0918))

**Prüfe Recherche, Gestaltung und Rendering getrennt.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ Video abspielen</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ Video abspielen</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ Video abspielen</a></td></tr></table>

Der Autor zeigt vier Läufe: ein ChatGPT-Jubiläumsvideo, ein DeepSeek-Erklärvideo, eine Three.js-Szene und eine 3D-Nachbildung von Apple Jing’an.

[Weiterführende Quellen 1](https://x.com/Khazix0918/article/2119941585538572390)

Originalprompt

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [Ein zerlegbares Modell eines Kernreaktors](https://x.com/konstantinsaifo/status/2119941967136379334) (von [@konstantinsaifo](https://x.com/konstantinsaifo))

**Zeige mit einer Zerlegefunktion, wie Bauteile zusammenpassen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor bat um ein zerlegbares Reaktormodell in Three.js und nennt 92 US-Dollar API-Kosten.

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Agenten in Blood on the Clocktower](https://x.com/dwarkesh_sp/status/2119942657812451482) (von [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**Vergleiche Modelle im selben Spiel mit verdeckten Rollen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

Der Auswerter sieht Fable 5.2 vor Fable 5.1 und Opus 5.5. GPT-6 Astra liegt in diesem Benchmark weiter vorn.

[Weiterführende Quellen 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [Ein Podrennen-Prototyp](https://x.com/loktar00/status/2119943124965638444) (von [@loktar00](https://x.com/loktar00))

**Nutze ein bekanntes Rennformat, um Bewegung und Steuerung zu beurteilen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor teilt ein von Podrennen inspiriertes Ergebnis mit Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [Zehn Sekunden Werbung für Claude-Unterwäsche](https://x.com/Masimo_Blue/status/2119943368612487285) (von [@Masimo_Blue](https://x.com/Masimo_Blue))

**Erprobe eine offene Produktvorgabe mit eigener Musik.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ Video abspielen</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

Der Autor zeigt einen zehnsekündigen Werbeclip mit Acid Techno und den bereitgestellten Produktbildern.

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [Ein Vogel bei Sonnenaufgang, Strich für Strich](https://x.com/mgrczyk/status/2119943813028548721) (von [@mgrczyk](https://x.com/mgrczyk))

**Deaktiviere das Rückgängigmachen, um Zeichenentscheidungen nacheinander zu beobachten.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt einen Vogel bei Sonnenaufgang, gemalt in einer Umgebung, in der frühere Striche unveränderlich waren.

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [Ein langer Grafiklauf in Devin](https://x.com/Da7_Tech/status/2119944847255896490) (von [@Da7_Tech](https://x.com/Da7_Tech))

**Erfasse Zeit und Kosten bei einem aufwendigen Rendering.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ Video abspielen</a>

Ein als solcher ausgewiesener Cognition-Botschafter zeigt einen Lauf mit Devin Max, der laut Bericht etwa 82 US-Dollar und 3,5 Stunden erforderte.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [Mit Code gemalte Kunst von drei Modellen](https://x.com/kickingkeys/status/2119945841997672698) (von [@kickingkeys](https://x.com/kickingkeys))

**Vergleiche Zeichenbewegung und synthetisierten Ton über mehrere Läufe.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt ein mit Code gemaltes Bild samt Audio und beschreibt Tests mit demselben Prompt für Fable 5.2, Fable 5.1 und Gemini 4 Argon.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [Die Geschichte der Schrift in Bewegung](https://x.com/rileybrown/status/2119946022767980985) (von [@rileybrown](https://x.com/rileybrown))

**Ordne eine programmierte Erklärung entlang einer Zeitleiste.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt eine Animation zur Geschichte der Schrift, die nach seinen Angaben aus einem Prompt entstand.

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [Testgelände für Spielmaschinen](https://x.com/techartist_/status/2119946891106394518) (von [@techartist_](https://x.com/techartist_))

**Erprobe Spielmechanik, Physik und Effekte in einer gemeinsamen Szene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor baute mit Three.js und Blender ein Testgelände für vier Konzepte.

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [Platine für eine tragbare Linux-Konsole](https://x.com/seveibar/status/2119947341230907453) (von [@seveibar](https://x.com/seveibar))

**Vergleiche Modelle anhand derselben Schaltungsvorgabe.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ Video abspielen</a>

Der tscircuit-Entwickler zeigt einen Designversuch für eine tragbare Linux-Spielkonsole mit Astra 6 High und Fable 5.2 High.

Originalprompt

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [Ein See aus Voxeln](https://x.com/Angaisb_/status/2119947748690841841) (von [@Angaisb_](https://x.com/Angaisb_))

**Prüfe die Komposition mit einer kleinen Umgebung.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt einen Voxel-See, den er Fable 5.2 zuschreibt.

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [17 interaktive Ergebnisse von Arena](https://x.com/arena/status/2119948067449536733) (von [@arena](https://x.com/arena))

**Sieh dir mehrere Ausgabetypen an, bevor du eine Testaufgabe wählst.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ Video abspielen</a>

Arena zeigt 17 Ergebnisse, darunter 3D-Welten, Spiele, Benutzeroberflächen, Datenvisualisierungen und programmierte Animationen.

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [Flug mit einem freundlichen Drachen](https://x.com/chetanankola/status/2119951015407738913) (von [@chetanankola](https://x.com/chetanankola))

**Prüfe Kamera und Bewegung in einem Flugablauf.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt eine Drachenszene mit Three.js und Blender und beschreibt Verbesserungen durch Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Gelee-Orca mit Fable und Opus](https://x.com/vib3coded/status/2119951060752375827) (von [@vib3coded](https://x.com/vib3coded))

**Vergleiche Oberfläche und Bewegung am selben Motiv.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt Gelee-Orcas von Fable 5.2 und Opus 5.5 nebeneinander.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [Offener Test der Videoqualität](https://x.com/suna_gaku/status/2119952985933697063) (von [@suna_gaku](https://x.com/suna_gaku))

**Nutze eine freie Kreativaufgabe, um Modellentscheidungen zu beobachten.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor bat das Modell um sein bestes Video und teilte das Ergebnis.

Originalprompt

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [Weltraumhabitat mit mediterranem Thema](https://x.com/MaxXWilliamson/status/2119953172634677533) (von [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**Verbinde eine knappe Vorgabe mit etablierten Projektwerkzeugen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor stellte Werkzeuge aus früheren Habitat-Entwürfen bereit und bat um eine mediterran gestaltete Station.

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [AA-3D-Benchmark für interaktive Erlebnisse](https://x.com/ArtificialAnlys/status/2119953570430881946) (von [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Lies den Elo-Wert zusammen mit seinem Unsicherheitsintervall.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ Video abspielen</a>

Artificial Analysis meldet zum Start 1271 Elo für Fable 5.2 Max im Benchmark für interaktive 3D-Erlebnisse.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [Ein Spiel mit Skelettfigur und Zeitlimit](https://x.com/WesRoth/status/2119953913160093817) (von [@WesRoth](https://x.com/WesRoth))

**Nutze einen sichtbaren Timer zur Bewertung eines spielbaren Prototyps.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt ein Ergebnis aus einem Fable-5.2-Prompt mit Skelettfigur und eingeblendetem Countdown.

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Pixelgrafik mit Fable und Astra](https://x.com/Angaisb_/status/2119955179915137294) (von [@Angaisb_](https://x.com/Angaisb_))

**Vergleiche Formen und Details im selben Maßstab.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ Video abspielen</a>

Der Originalvergleich zeigt Pixelgrafiken von GPT-6 Astra und Fable 5.2.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [Portfolio-Reel für Motion Design](https://x.com/Leviwoyun/status/2119955625820258308) (von [@Leviwoyun](https://x.com/Leviwoyun))

**Gib eine offene Aufgabe mit fester Dauer vor.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor zeigt ein Motion-Design-Reel mit Musik und nennt 24 Minuten Produktionszeit.

Originalprompt

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [Rendering eines Glaspools mit zwei Modellen](https://x.com/MrTacticalX/status/2119955647542542439) (von [@MrTacticalX](https://x.com/MrTacticalX))

**Vergleiche Beleuchtung, Laufzeit und Kosten.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor nennt 90 Minuten und 57,87 US-Dollar für Fable gegenüber 68 Minuten und 14,39 US-Dollar für Opus.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [Genauigkeit von Werkzeugaufrufen in TS-Bench](https://x.com/gosrum/status/2119956559031927079) (von [@gosrum](https://x.com/gosrum))

**Erfasse Aufruffehler und Tokenverbrauch getrennt.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

Der Tester meldet für Fable 5.2 null Fehler bei Werkzeugaufrufen. Einfache Aufgaben unterschieden die Claude-Varianten kaum.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [Machu Picchu als Miniaturwelt](https://x.com/loktar00/status/2119958719362666708) (von [@loktar00](https://x.com/loktar00))

**Prüfe Atmosphäre und kleine Details in einer Miniaturszene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ Video abspielen</a>

Die Machu-Picchu-Demo zeigt volumetrischen Nebel und kleine Alpakas.

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [GDPx nach beruflichen Aufgabenkategorien](https://x.com/SemiAnalysis_/status/2119961447199289640) (von [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**Lies die Ergebnisse einzelner Teilaufgaben neben dem Gesamtergebnis.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

Der Herausgeber des Benchmarks meldet 16,4 % insgesamt und schlüsselt Bereiche wie Chipdesign und Softwareentwicklung auf.

[Weiterführende Quellen 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [Weiterführende Quellen 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [Weiterführende Quellen 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [Ein Porträt in einem Zeichenprogramm](https://x.com/The_Alex/status/2119964472559489229) (von [@The_Alex](https://x.com/The_Alex))

**Nutzen Sie ein kleines Referenzbild als Vorlage für das Porträt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor bat Fable 5.2, ein Zeichenprogramm zu öffnen und ihn zu porträtieren. Das Video zeigt den Weg von den Konturen bis zum fertigen Bild.

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [VulcanBench Frontier v4 mit Einstellung Low](https://x.com/morganlinton/status/2119966067527467215) (von [@morganlinton](https://x.com/morganlinton))

**Vergleiche Modellgenerationen auf derselben Aufwandsstufe.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

Der Benchmark-Autor nennt für Fable 5.2 und 5.1 auf Low etwa 5 beziehungsweise 26 Minuten pro Aufgabe.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [Spielbare Backrooms mit vertauschten Rollen](https://x.com/LexnLin/status/2119966127149429093) (von [@LexnLin](https://x.com/LexnLin))

**Ändere das Ziel des Spielers, um ein Spielkonzept zu prüfen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ Video abspielen</a>

Der Spieler steuert das Monster und versucht, Menschen zu fangen. Der Autor teilt Spielmaterial und einen Link zum Spiel.

[Weiterführende Quellen 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [Bugatti Tourbillon mit Blender modellieren](https://x.com/xikhar/status/2119966147328299284) (von [@xikhar](https://x.com/xikhar))

**Lege Außen- und Innendetails mit Referenzbildern fest.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor berichtet, einen Bugatti Tourbillon samt Innenraum modelliert und aus einem Prompt und Referenzen eine Filmsequenz gerendert zu haben.

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [Ein Computer-Video mit zwei Modellen](https://x.com/daradoescode/status/2119966154391183522) (von [@daradoescode](https://x.com/daradoescode))

**Halte bei einem gemischten Ablauf den Beitrag jedes Modells fest.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor teilte ein stilisiertes Video, das mit Fable 5.2 und erheblicher Unterstützung von Opus 5.5 entstand.

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [Ein Musikvideo über Megakernels](https://x.com/elliotarledge/status/2119968762069934415) (von [@elliotarledge](https://x.com/elliotarledge))

**Verwende ein technisches Konzept als Videothema.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor bat Fable 5.2 mit der Einstellung High um ein Musikvideo über Megakernels und teilte den Clip.

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [Studio-Rundgang aus Referenzfotos](https://x.com/rpnickson/status/2119969928304357507) (von [@rpnickson](https://x.com/rpnickson))

**Nutze echte Fotos als Grundlage für die Rekonstruktion einer Szene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor lieferte Studiofotos, passte eine ähnliche Videovorgabe an und berichtet von rund zwei Stunden Laufzeit.

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [Spielzeugwerbung im Stil der 1990er aus Code](https://x.com/kevin_t_ngo/status/2119972124211454139) (von [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Trenne Animationsskripte vom Rendering.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor animierte nach eigenen Angaben einen Retro-Spielzeugspot mit Python und renderte ihn in Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Eine Three.js-Spielszene in Third-Person-Perspektive](https://x.com/bijanbowen/status/2119972220739187182) (von [@bijanbowen](https://x.com/bijanbowen))

**Prüfe Bewegung und Umgebung anhand einer Spielsitzung.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

Der Autor zeigt im Stream ein Three.js-Ergebnis mit einer Spielfigur in einer Außenumgebung.

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [Bryceball auf Basis eines vorhandenen Renderers](https://x.com/pleometric/status/2119973274402668852) (von [@pleometric](https://x.com/pleometric))

**Nutze eine Rendering-Engine als Grundlage für ein Spiel.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor passte den Renderer aus dem verlinkten Beitrag an und machte daraus das spielbare Bryceball.

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [Rekursiver Videoschnitt mit Fable](https://x.com/rileybrown/status/2119973951027724385) (von [@rileybrown](https://x.com/rileybrown))

**Verwende einen früheren Schnitt als Material für einen weiteren Beitrag.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor teilte ein mit Fable 5.2 geschnittenes Video über ein früheres Video, das er ebenfalls mit dem Modell bearbeitet hatte.

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [Eine filmische Geschichte der Wissenschaft](https://x.com/DeryaTR_/status/2119974354260013293) (von [@DeryaTR_](https://x.com/DeryaTR_))

**Gliedere eine 3D-Sequenz anhand einer Zeitleiste.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor bat um eine filmische Reise von den Anfängen der Wissenschaft bis zu einer möglichen Zukunft und teilte den entstandenen Clip.

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [Da Vincis Flugmaschine in 3D](https://x.com/higgsfield_ai/status/2119975721909301684) (von [@higgsfield_ai](https://x.com/higgsfield_ai))

**Modelliere einen historischen Entwurf, bevor du Änderungen testest.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ Video abspielen</a>

Higgsfield zeigte eine 3D-Interpretation von Leonardos Flugmaschine und beschrieb einen Physiktest und einen überarbeiteten Entwurf.

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [Leiterplatten-Routing nach Entwurfsvorgabe](https://x.com/cmonkey/status/2119975852977029365) (von [@cmonkey](https://x.com/cmonkey))

**Prüfe die geroutete Platine vor der Fertigung.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

Als Antwort auf eine Layout-Diskussion teilte der Autor das PCB-Routing-Ergebnis von Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [Derselbe Prompt in unterschiedlichen Laufzeitumgebungen](https://x.com/loktar00/status/2119980613369319706) (von [@loktar00](https://x.com/loktar00))

**Halte Unterschiede der Ausführungsumgebung beim Vergleich fest.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor gab DeepSeek und Fable 5.2 denselben Prompt in verschiedenen Umgebungen und zeigte die Ergebnisse nebeneinander.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [Mit Code gezeichnete Godzilla-Illustration](https://x.com/chetaslua/status/2119981510199808368) (von [@chetaslua](https://x.com/chetaslua))

**Interpretiere eine Vorlage mit vektorartigen Formen und Bewegung neu.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor teilte eine mit Code gezeichnete Illustration mit einer kurzen Animation, inspiriert von einem Godzilla-Beitrag.

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [Handventilator für den 3D-Druck](https://x.com/davelee/status/2119981787325579398) (von [@davelee](https://x.com/davelee))

**Prüfe den Zusammenbau mit einem physischen Prototyp.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor und seine Kinder entwarfen einen druckbaren Handventilator und teilten das Modell vor dem Druck.

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [Fehlersuche in einem Plugin im Vergleich mit Opus](https://x.com/oaranda/status/2119982729747919096) (von [@oaranda](https://x.com/oaranda))

**Vergleiche die Korrekturen mit den Regressionstests des jeweils anderen Modells.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

Vom Autor kommentierter Auszug aus der Ankündigung.

Beide Modelle fanden dieselben sechs Plugin-Fehler. Opus bestand alle Gegentests. Fable scheiterte an einem und entdeckte ein weiteres Dashboard-Problem.

Originalprompt

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [Istanbul als 3D-Szene nachgebaut](https://x.com/petergostev/status/2119877733488394520) (von [@petergostev](https://x.com/petergostev))

**Prüfe eine Stadtszene sowohl im Überblick als auch aus der Nähe.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ Video abspielen</a>

Peter Gostev zeigt eine 3D-Ansicht von Istanbul mit Fable 5.2 Max und verlinkt die ausführliche Bewertung.

[Weiterführende Quellen 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [Ein Blender-Film mit funktionierendem Bildschirm](https://x.com/rileybrown/status/2119902109709537708) (von [@rileybrown](https://x.com/rileybrown))

**Animiere Bildschirm, Licht und Kamera in derselben 3D-Szene.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ Video abspielen</a>

Der Autor nennt 13 Kameraeinstellungen, eine eigene Webseite auf dem Laptop und ElevenLabs-Audio. Gerendert wurde auf RunPod-GPUs.

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [Ein Schwarzes-Loch-Übergang bei schwacher Kopplung](https://hexagonmath.org/2611.00175v1) (von [@Anthropic](https://www.anthropic.com/))

**Prüfe eine offene Rechnung anhand des ursprünglichen theoretischen Aufbaus.**

Anthropic berichtet, dass Fable 5.2 eine lange offene Rechnung abschloss und einen abrupten Übergang bei schwacher Kopplung fand. Der Preprint enthält die Herleitung.

[Weiterführende Quellen 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [Die Grenze einer modularen Bootstrap-Schranke](https://hexagonmath.org/2611.00174v1) (von [@Anthropic](https://www.anthropic.com/))

**Veröffentliche die Herleitung zusammen mit der analytischen Schranke.**

Anthropic berichtet, dass Fable 5.2 die exakte Grenze einer spinlosen modularen Bootstrap-Methode in einem vereinfachten Quantengravitationsmodell bestimmte.

[Weiterführende Quellen 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Vercel AI Gateway mit geordneten Fallback-Modellen](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (von [Vercel](https://vercel.com/))

**Lege die Reihenfolge für Anfragen fest, die der Klassifikator ablehnt.**

Das Vercel-AI-SDK-Beispiel ruft anthropic/claude-fable-5.2 auf und konfiguriert Opus 5.5 gefolgt von Sonnet 5.5 als Fallback. Der Leitfaden dokumentiert die Vorgabe zur Datenaufbewahrung.

[Weiterführende Quellen 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [Verschachtelte Subagenten und Review-Budget](https://news.ycombinator.com/item?id=50430925) (von [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**Überwache verschachtelte Delegation und begrenze das Budget außerhalb des Prompts.**

Der Autor verlangte höchstens vier Subagenten für ein Review von 80.000 Codezeilen. Er meldet mindestens sechs verschachtelte Agenten und ein in unter 20 Minuten aufgebrauchtes Fünf-Stunden-Kontingent.

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [LCARS-Design als HTML im Modellvergleich](https://news.ycombinator.com/item?id=50430962) (von [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**Prüfe Kurven, Icons, Animation und Navigation als getrennte Kriterien.**

Der Autor vergleicht Fable 5.2 und Opus 5.5 anhand desselben Star-Trek-Designs. Ihm gefielen Fables Kurven und einige Icons besser, Opus' Animationen ebenfalls. Das Flackern der Fable-SVG störte ihn. Er hatte nur die erste Seite angefordert.

[Weiterführende Quellen 1](https://html.non.io/lcars-fable-5.2/) · [Weiterführende Quellen 2](https://html.non.io/lcars-opus-5.5/) · [Weiterführende Quellen 3](https://news.ycombinator.com/item?id=50431231) · [Weiterführende Quellen 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [GPU-Optimierung für Quantum ESPRESSO](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (von [Discovered Materials](https://discoveredmaterials.com/))

**Verlange beim Optimieren wissenschaftlichen Codes Referenzergebnisse und repräsentative verdeckte Tests.**

Discovered Materials meldet im geometrischen Mittel 36-fache Beschleunigung bei 13 Phonon-Tests auf derselben GPU und rund 9-fache bei Hybridfunktional-Rechnungen. Der veröffentlichte Patch stützt sich auf Korrektheits- und Leistungstests.

[Weiterführende Quellen 1](https://github.com/discovered-materials/dm_qe) · [Weiterführende Quellen 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [Artificial Analysis Intelligence Index nach Aufwandsstufe](https://artificialanalysis.ai/models/claude-fable-5-2) (von [Artificial Analysis](https://artificialanalysis.ai/))

**Betrachte Punktzahl, Aufgabenkosten und Latenz gemeinsam.**

Der zitierte Max-Schnappschuss mit Standard-Fallback nennt Index 65, 26,54 US-Dollar und 46,4 Minuten pro Aufgabe. Die Zahlen beziehen sich auf die Benchmark-Aufgaben.

[Weiterführende Quellen 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [Fehlalarme in einem Änderungsreview auf High](https://news.ycombinator.com/item?id=50431810) (von [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**Prüfe Modellbefunde im Code, bevor du handelst.**

Ein Entwickler berichtet, dass Fable 5.2 High zwei nicht vorhandene Probleme markierte, die er anhand seiner Codekenntnis erkannte.

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [Dreißig alltägliche Programmieraufgaben](https://news.ycombinator.com/item?id=50432483) (von [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**Miss Laufzeit und gelöste Aufgaben bei derselben Arbeitslast.**

Laut Autor lösten Fable 5.2 und Opus 5.5 jeweils 26 von 30 Aufgaben, Fable 5.1 löste 25. Fable 5.2 benötigte 0,62-mal so viel Zeit wie 5.1. Sicherheitsstopps wurden nicht gemeldet.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [Bildschirmschoner mit einer einsamen Insel](https://news.ycombinator.com/item?id=50432836) (von [@nzach](https://news.ycombinator.com/user?id=nzach))

**Öffne die interaktive Seite, um den Bildschirmschoner zu prüfen.**

Der Show-HN-Autor verlinkt die Browserszene Stranded with Claude. Das veröffentlichte Ergebnis ist ein interaktives Canvas.

[Weiterführende Quellen 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [Drei Browserspiele auf Aufwandsstufe High](https://senko.net/vibecode-bench/) (von [Senko Rašić](https://senko.net/))

**Vergleiche Spielbarkeit und visuelle Qualität getrennt.**

Senko Rašić setzte Vorgaben für Echtzeitstrategie, Voxel und Flugsimulation mit Fable 5.2 in Claude Code um. Er beschreibt tiefere Mechaniken wie ein Luftschiff zur Erkundung der ganzen Karte und beurteilt Teile der Grafik schlechter.

[Weiterführende Quellen 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [Buchpodcast-Skripte Kapitel für Kapitel](https://news.ycombinator.com/item?id=50434156) (von [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**Vergleiche die Skriptlänge bei derselben wiederkehrenden Aufgabe.**

Der Autor erzeugte Dialoge zweier Rezensenten, jeweils zu einem Kapitel. Er nennt etwa 2,5 Seiten bei Fable gegenüber 4,5 bei Opus 5.5 und verlinkt beide Beispiele.

[Weiterführende Quellen 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [Weiterführende Quellen 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [Ein Produktivdienst nach Rust migriert](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (von [@Anthropic](https://www.anthropic.com/))

**Miss das Startverhalten vor und nach der Migration.**

Anthropic berichtet, dass Agenten mit einer Vorabversion von Fable 5.2 einen Python-Produktivdienst in Rust neu schrieben und die Startzeit um etwa den Faktor 26 senkten.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [Fable 5.2 in GitHub Copilot auswählen](https://x.com/github/status/2119926269982961833) (von [@github](https://x.com/github))

**Aktivieren Sie vor der Modellauswahl die Organisationsrichtlinie.**

GitHub beschreibt die Modellauswahl in Copilot und die erforderliche Administratoreinstellung für Business- und Enterprise-Konten.

[Weiterführende Quellen 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [Eine Designaufgabe mit hundert HTML-Seiten](https://x.com/MiaAI_lab/status/2119930229661503893) (von [@MiaAI_lab](https://x.com/MiaAI_lab))

**Zähle fertige, lauffähige Dateien und beurteile die Gestaltung.**

Der Autor verlangte 100 unterschiedliche Designs und veröffentlichte 76 Dateien samt Prompts. Nach eigenen Angaben erreichte er das Fable-Nutzungslimit.

[Weiterführende Quellen 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [Weiterführende Quellen 2](https://mia-ai.net/lab/experiments/100-htmls) · [Weiterführende Quellen 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [Weiterführende Quellen 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [Weiterführende Quellen 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [Weiterführende Quellen 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [Weiterführende Quellen 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [Weiterführende Quellen 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [Weiterführende Quellen 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [Weiterführende Quellen 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [Weiterführende Quellen 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [Weiterführende Quellen 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [Weiterführende Quellen 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [Weiterführende Quellen 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [Abweichende Anforderungen bei einer Compiler-Aufgabe](https://x.com/sameQCU/status/2119939304864800971) (von [@sameQCU](https://x.com/sameQCU))

**Vergleiche die vom Agenten genannten Anforderungen mit der Eingabe.**

Der Entwickler beschreibt Compiler-Arbeit, bei der Fable 5.2 und frühere Opus-Modelle die erhaltenen Anforderungen falsch wiedergaben.

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [Einen langen Fable-Lauf mit Opus verfolgen](https://x.com/marouane53/status/2119950129767858262) (von [@marouane53](https://x.com/marouane53))

**Verfolgen Sie lange Aufgaben in einer separaten Sitzung.**

Laut Autor liefen einige Fable-Aufgaben mehr als zwei Stunden mit wenigen Statusmeldungen. Opus 5.5 erklärte in einem anderen Gespräch den Fortschritt und die Entscheidungen.

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [Code-Review mit frischem Blick](https://x.com/doodlestein/status/2119958895158292786) (von [@doodlestein](https://x.com/doodlestein))

**Prüfe neue und geänderte Dateien in einem separaten Durchlauf.**

Der Autor teilt zwei genaue Folgeprompts zum Auffinden und Beheben von Fehlern nach der Implementierung.

Originalprompt

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

Originalprompt

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [Kontextverlust beim Review eines Funktionsentwurfs](https://news.ycombinator.com/item?id=50434214) (von [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**Nutze den aktuellen Entwurf als Checkliste für spätere Empfehlungen.**

Der Autor verglich beide Modelle beim Entwurfsreview und bevorzugte Opus 5.5. Ein späterer Diagnose-Durchlauf mit Fable 5.2 empfahl etwas, das der Entwurf bereits enthielt.

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [Breakout-Vergleich im Stil von DX Ball](https://news.ycombinator.com/item?id=50434424) (von [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**Vergleiche Mechanik und Spielgefühl anhand derselben Nachbauaufgabe.**

Der Autor verlinkt getrennte Versionen von Fable 5.2 und Opus 5.5. Fable änderte einige Originalmechaniken. Der Autor bevorzugte das Spielgefühl der Opus-Version.

[Weiterführende Quellen 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [Weiterführende Quellen 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [Ein Versuch zur Verbesserung einer 3D-App](https://news.ycombinator.com/item?id=50434433) (von [@user43928](https://news.ycombinator.com/user?id=user43928))

**Vergleiche sichtbare Änderungen mit dem verbrauchten Budget bei derselben Aufgabe.**

Der Autor bat Fable 5.2 um Verbesserungen an einer 3D-App außerhalb des Gaming-Bereichs. Er sah wenig Unterschied zu Opus 5.5 und verbrauchte an diesem Abend 25 % seines Fable-Kontingents.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [Maus-und-Katze-Spiel mit drei Modellen](https://news.ycombinator.com/item?id=50434508) (von [@simonw](https://news.ycombinator.com/user?id=simonw))

**Halte den Spielprompt konstant und prüfe jede spielbare Umsetzung.**

Simon Willison zeigt mobile Three.js-Varianten von Fable 5.2 Extra, Opus 5.5 Extra und GPT-6 Extra High. Der Fable-Lauf dauerte laut ihm rund 40 Minuten.

[Weiterführende Quellen 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [Weiterführende Quellen 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [Weiterführende Quellen 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

Originalprompt

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [Kosten und Punktzahl in AIBenchy auf High](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (von [AIBenchy](https://aibenchy.com/))

**Vergleiche Punktzahl, Gesamtkosten und Antwortzeit auf gleicher Aufwandsstufe.**

AIBenchy nennt 8,7 gegenüber 9,4 Punkten, 5,083 gegenüber 2,133 US-Dollar und im Mittel 14,73 gegenüber 27,55 Sekunden für Fable 5.2 High und Opus 5.5 High.

[Weiterführende Quellen 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [Die Agentenumgebung für Fable 5.2 abstimmen](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (von [@Anthropic](https://www.anthropic.com/))

**Testen Sie die Denkstufen erneut und legen Sie Statusmeldungen fest.**

Anthropics Leitfaden enthält Beispielanweisungen zu Denkaufwand, Abschlusskriterien, Freigaben, Statusmeldungen und Grenzen für Subagenten.

[Weiterführende Quellen 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="acknowledge"></a>
## Mitwirkende

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/)
