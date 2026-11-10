# Cas d’utilisation de Claude Fable 5.2

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

Flux de travail, démonstrations, comparaisons, évaluations, intégrations et limites pratiques recensés le 10 novembre, avec leurs sources.

[Annonce d’Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [Collection précédente](../../README_fr.md)

## Index des cas

| Case | Cas d’utilisation | Type |
| --- | --- | --- |
| 330 | [MacBook en SVG à différents niveaux d’effort](#case-330) | Benchmark |
| 331 | [Un beat ’em up à quatre à partir de dessins familiaux](#case-331) | Demo |
| 332 | [Trois appareils électroniques, de la conception au montage](#case-332) | Demo |
| 333 | [Formalisation du dernier théorème de Fermat dans Lean](#case-333) | Evaluation |
| 334 | [Un système d’exploitation à partir d’un dossier vide](#case-334) | Demo |
| 335 | [Manipulation à deux bras dans RoboDojo](#case-335) | Benchmark |
| 336 | [Une fontaine en mouvement](#case-336) | Demo |
| 337 | [Synchronisation labiale image par image avec Higgsfield](#case-337) | Integration |
| 338 | [Prototype de conduite en monde ouvert](#case-338) | Demo |
| 339 | [Paris en 1940 à partir d’images de référence](#case-339) | Integration |
| 340 | [Fable planifie un court métrage rendu par Opus](#case-340) | Integration |
| 341 | [Un essai de clip musical](#case-341) | Demo |
| 342 | [Un portrait peint de Dario Amodei](#case-342) | Demo |
| 343 | [Spud Smash en mode Medium](#case-343) | Demo |
| 344 | [Cathédrale de glace avec Fable et Opus](#case-344) | Evaluation |
| 345 | [Chant avec des conduits vocaux simulés](#case-345) | Demo |
| 346 | [Trois tests de voxels à Istanbul](#case-346) | Evaluation |
| 347 | [Projets achevés dans le Remote Labor Index](#case-347) | Benchmark |
| 348 | [Scène d’iceberg à quatre niveaux d’effort](#case-348) | Evaluation |
| 349 | [Un court anime de soixante-dix-neuf secondes](#case-349) | Demo |
| 350 | [Assemblages mécaniques avec Fable et Opus](#case-350) | Evaluation |
| 351 | [Une main robotisée gravit un escalier en colimaçon](#case-351) | Demo |
| 352 | [Rigging d’un maillage Tripo dans Blender](#case-352) | Evaluation |
| 353 | [Inventions interactives d’après le carnet de Léonard de Vinci](#case-353) | Demo |
| 354 | [Une station audio pilotée par Claude](#case-354) | Demo |
| 355 | [Un Raspberry Pi 5 animé](#case-355) | Demo |
| 356 | [Une scène du nord de l’Italie](#case-356) | Demo |
| 357 | [Livre pop-up avec des agents d’exécution locaux](#case-357) | Evaluation |
| 358 | [Le retour du test de la lampe à lave](#case-358) | Evaluation |
| 359 | [Un avion à réaction détaillé dans Blender](#case-359) | Integration |
| 360 | [Un voyage par portails entre des centaines de mondes](#case-360) | Demo |
| 361 | [Un bazar de Bombay en six plans avec Three.js](#case-361) | Integration |
| 362 | [Un diner photoréaliste créé en code](#case-362) | Integration |
| 363 | [Un modèle de robot dans Blender](#case-363) | Demo |
| 364 | [Une vidéo animée pour expliquer Convex](#case-364) | Demo |
| 365 | [Une collection de pages d’accueil créées en une consigne](#case-365) | Demo |
| 366 | [Une sonate pour piano écrite en LilyPond](#case-366) | Demo |
| 367 | [Un brief vidéo en création libre](#case-367) | Demo |
| 368 | [Fable planifie, DeepSeek implémente et Opus relit](#case-368) | Integration |
| 369 | [Fable 5.2 dans AI Village](#case-369) | Integration |
| 370 | [Design de frontend avec et sans skills](#case-370) | Evaluation |
| 371 | [Détecter les machines à états implicites dans le code](#case-371) | Tutorial |
| 372 | [Un jeu créé de zéro en huit heures](#case-372) | Demo |
| 373 | [Prototype de Fishslop et coût en tokens](#case-373) | Evaluation |
| 374 | [Un jeu de football américain en mouvement](#case-374) | Demo |
| 375 | [Combat de boss en monde ouvert avec Higgsfield MCP](#case-375) | Integration |
| 376 | [Mont-Saint-Michel au rythme des marées](#case-376) | Demo |
| 377 | [Un élément de Roblox dans Blender](#case-377) | Demo |
| 378 | [Raisonnement sans chaîne de pensée en sortie](#case-378) | Benchmark |
| 379 | [Variations de Chrome Dino avec quatre modèles](#case-379) | Evaluation |
| 380 | [Jeu de dames avec un bras robotisé](#case-380) | Demo |
| 381 | [Une animation graphique de quinze secondes](#case-381) | Demo |
| 382 | [Une tour Eiffel jouable](#case-382) | Demo |
| 383 | [Course en haute mer avec Three.js et Higgsfield](#case-383) | Integration |
| 384 | [Simulation de miel en temps réel dans WebGL](#case-384) | Demo |
| 385 | [Effets visuels programmés sur de la vidéo](#case-385) | Demo |
| 386 | [Une animation sur les niveaux de recherche dans GTA](#case-386) | Demo |
| 387 | [Un monde de MMO stylisé créé en code](#case-387) | Demo |
| 388 | [Une scène 3D avec Fable et Opus](#case-388) | Evaluation |
| 389 | [Texte redondant dans un menu de pause](#case-389) | Limit |
| 390 | [Planches d’inspiration dans un environnement Krea](#case-390) | Integration |
| 391 | [Essais au bureau d’un jeu de tir avec portails](#case-391) | Demo |
| 392 | [Un objet à surfaces rigides détaillé dans Blender](#case-392) | Demo |
| 393 | [Essais parallèles de frontend à plusieurs niveaux d’effort](#case-393) | Evaluation |
| 394 | [Un petit jeu en dix consignes](#case-394) | Demo |
| 395 | [Animation image par image en JavaScript](#case-395) | Demo |
| 396 | [De la vidéo de référence à l’animation 3D](#case-396) | Demo |
| 397 | [Feu de camp en pixel art avec Fable et Opus](#case-397) | Evaluation |
| 398 | [Arena WebDev en mode xHigh](#case-398) | Benchmark |
| 399 | [Typographie de bande-annonce avec deux modèles](#case-399) | Evaluation |
| 400 | [Essais de motion design et de portfolio 3D en une consigne](#case-400) | Evaluation |
| 401 | [Un réacteur nucléaire à explorer](#case-401) | Demo |
| 402 | [Agents dans Blood on the Clocktower](#case-402) | Benchmark |
| 403 | [Prototype de course de pods](#case-403) | Demo |
| 404 | [Une publicité de dix secondes pour les sous-vêtements Claude](#case-404) | Demo |
| 405 | [Un oiseau au lever du soleil, trait après trait](#case-405) | Demo |
| 406 | [Un long essai graphique dans Devin](#case-406) | Evaluation |
| 407 | [Peinture programmée avec trois modèles](#case-407) | Evaluation |
| 408 | [L’histoire de l’écriture en mouvement](#case-408) | Demo |
| 409 | [Terrain d’essai pour des engins de jeu](#case-409) | Demo |
| 410 | [Circuit imprimé pour une console Linux portable](#case-410) | Evaluation |
| 411 | [Un lac en voxels](#case-411) | Demo |
| 412 | [Les 17 générations interactives d’Arena](#case-412) | Demo |
| 413 | [Vol avec un dragon amical](#case-413) | Demo |
| 414 | [Orque en gelée avec Fable et Opus](#case-414) | Evaluation |
| 415 | [Test vidéo en création libre](#case-415) | Demo |
| 416 | [Habitat spatial d’inspiration méditerranéenne](#case-416) | Demo |
| 417 | [Benchmark AA-3D d’expériences interactives](#case-417) | Benchmark |
| 418 | [Un défi chronométré avec un personnage squelettique](#case-418) | Demo |
| 419 | [Pixel art avec Fable et Astra](#case-419) | Evaluation |
| 420 | [Bande démo de motion design](#case-420) | Demo |
| 421 | [Rendu d’une piscine de verre avec deux modèles](#case-421) | Evaluation |
| 422 | [Précision des appels d’outils sur TS-Bench](#case-422) | Benchmark |
| 423 | [Machu Picchu en miniature](#case-423) | Demo |
| 424 | [GDPx par catégorie de tâches professionnelles](#case-424) | Benchmark |
| 425 | [Un portrait dans un logiciel de dessin](#case-425) | Demo |
| 426 | [VulcanBench Frontier v4 en mode Low](#case-426) | Benchmark |
| 427 | [Un jeu Backrooms aux rôles inversés](#case-427) | Demo |
| 428 | [Une Bugatti Tourbillon dans Blender](#case-428) | Demo |
| 429 | [Une vidéo sur l’informatique réalisée avec deux modèles](#case-429) | Demo |
| 430 | [Un clip musical sur les megakernels](#case-430) | Demo |
| 431 | [Visite d’un studio à partir de photos de référence](#case-431) | Demo |
| 432 | [Une publicité pour jouets des années 1990 réalisée en code](#case-432) | Demo |
| 433 | [Scène de jeu à la troisième personne avec Three.js](#case-433) | Demo |
| 434 | [Bryceball à partir d’un moteur de rendu existant](#case-434) | Demo |
| 435 | [Montage vidéo récursif avec Fable](#case-435) | Demo |
| 436 | [Une histoire cinématographique des sciences](#case-436) | Demo |
| 437 | [La machine volante de Léonard de Vinci en 3D](#case-437) | Integration |
| 438 | [Routage de circuit imprimé à partir d’un cahier des charges](#case-438) | Demo |
| 439 | [Une même consigne dans deux environnements](#case-439) | Evaluation |
| 440 | [Illustration de Godzilla dessinée en code](#case-440) | Demo |
| 441 | [Ventilateur à main conçu pour l’impression 3D](#case-441) | Demo |
| 442 | [Recherche de bugs dans un plugin face à Opus](#case-442) | Evaluation |
| 443 | [Istanbul reconstituée en 3D](#case-443) | Demo |
| 444 | [Un film Blender avec un écran fonctionnel](#case-444) | Demo |
| 445 | [Une transition de trou noir à couplage faible](#case-445) | Evaluation |
| 446 | [La limite d’une borne du bootstrap modulaire](#case-446) | Evaluation |
| 447 | [Vercel AI Gateway avec des modèles de repli ordonnés](#case-447) | Integration |
| 448 | [Sous-agents imbriqués et budget de revue](#case-448) | Limit |
| 449 | [Comparatif de conversion d’un design LCARS en HTML](#case-449) | Evaluation |
| 450 | [Optimisation GPU de Quantum ESPRESSO](#case-450) | Benchmark |
| 451 | [Indice d’intelligence d’Artificial Analysis par effort](#case-451) | Benchmark |
| 452 | [Faux positifs lors d’une revue en mode High](#case-452) | Limit |
| 453 | [Trente tâches courantes de programmation](#case-453) | Evaluation |
| 454 | [Écran de veille d’un naufragé sur une île](#case-454) | Demo |
| 455 | [Trois jeux pour navigateur en mode High](#case-455) | Evaluation |
| 456 | [Scripts de podcast littéraire chapitre par chapitre](#case-456) | Evaluation |
| 457 | [Un service de production migré vers Rust](#case-457) | Evaluation |
| 458 | [Choisir Fable 5.2 dans GitHub Copilot](#case-458) | Integration |
| 459 | [Un défi de conception de cent pages HTML](#case-459) | Evaluation |
| 460 | [Dérive des exigences dans un travail de compilation](#case-460) | Limit |
| 461 | [Suivre une longue tâche Fable avec Opus](#case-461) | Integration |
| 462 | [Relecture du code avec un regard neuf](#case-462) | Tutorial |
| 463 | [Perte de contexte lors d’une revue de conception](#case-463) | Limit |
| 464 | [Comparaison de casse-briques dans le style de DX Ball](#case-464) | Evaluation |
| 465 | [Essai d’amélioration d’une application 3D](#case-465) | Evaluation |
| 466 | [Un jeu de chat et de souris avec trois modèles](#case-466) | Evaluation |
| 467 | [Coût et score dans AIBenchy en mode High](#case-467) | Benchmark |
| 468 | [Régler l’environnement d’agents pour Fable 5.2](#case-468) | Tutorial |

<a id="fable-5-2-cases"></a>
## Cas d’utilisation

<a id="case-330"></a>
### Case 330: [MacBook en SVG à différents niveaux d’effort](https://playcode.io/blog/macbook-svg-benchmark#compare) (par [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**Comparez dessin, tokens et plafond de sortie à consigne fixe.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode indique 76 158 tokens et 3,05 USD pour Fable 5.2 High. Xhigh et Max ont atteint 128 000 tokens en streaming sans dessin, puis terminé avec davantage de marge via Batch API. Le classement reflète le jugement visuel de l’éditeur.

[Sources associées 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [Un beat ’em up à quatre à partir de dessins familiaux](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (par [Lex](https://notesbylex.com/))

**Donnez à l’agent des croquis, un prototype existant et des exigences précises pour les manettes.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex a utilisé Claude Code pour transformer un jeu à défilement horizontal en beat ’em up de 12 niveaux et 18 personnages. Des outils d’image et de son ont fourni les ressources. Quatre manettes ont fonctionné en famille.

[Sources associées 1](https://aidens-revenge.pages.dev/) · [Sources associées 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [Sources associées 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [Trois appareils électroniques, de la conception au montage](https://www.anthropic.com/research/claude-electronics-design) (par [@Anthropic](https://www.anthropic.com/))

**Vérifiez le circuit, le boîtier et le micrologiciel comme un ensemble.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ Lire la vidéo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic et Diode rapportent trois appareils fonctionnels. Fable 5.2 a routé les cartes, modélisé les boîtiers, écrit le logiciel et guidé les essais après fabrication.

[Sources associées 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [Sources associées 2](https://www.youtube.com/watch?v=vdYynH177h0) · [Sources associées 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [Formalisation du dernier théorème de Fermat dans Lean](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (par [@Anthropic](https://www.anthropic.com/))

**Prenez le vérificateur de preuves et les énoncés intermédiaires comme jalons.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Selon Anthropic, 1 000 agents Fable 5.2 ont formalisé la preuve existante en 30 heures. Opus 5.5 a atteint 26 % en 18 heures avec la même configuration d’équipe.

[Sources associées 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [Sources associées 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [Un système d’exploitation à partir d’un dossier vide](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (par [@Anthropic](https://www.anthropic.com/))

**Vérifiez séparément démarrage, pilotes, stockage et installation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ Lire la vidéo</a>

Anthropic rapporte que Fable 5.2 a coordonné plus de 1 000 sous-agents pendant huit jours pour produire un prototype de système qui a démarré sur un portable.

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [Manipulation à deux bras dans RoboDojo](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (par [@Anthropic](https://www.anthropic.com/))

**Comparez les modèles sur les mêmes tâches de manipulation simulées.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ Lire la vidéo</a>

Anthropic indique 64,9 % pour Fable 5.2 contre 27,6 % pour Fable 5.1 dans RoboDojo. L’annonce inclut une démonstration robotique.

[Sources associées 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [Une fontaine en mouvement](https://x.com/Angaisb_/status/2119909059277238733) (par [@Angaisb_](https://x.com/Angaisb_))

**Évaluez le rythme visuel à partir de l’écoulement continu de l’eau.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

L’auteur partage une scène de fontaine qu’il attribue à Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [Synchronisation labiale image par image avec Higgsfield](https://x.com/higgsfield_ai/status/2119909938969580024) (par [@higgsfield_ai](https://x.com/higgsfield_ai))

**Alignez le son sur les images avant de revoir la vidéo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ Lire la vidéo</a>

Higgsfield rapporte avoir suivi les mouvements de la bouche et calé le son sur les images dans son processus avec Fable 5.2.

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [Prototype de conduite en monde ouvert](https://x.com/ericmaskfr/status/2119910195325481026) (par [@ericmaskfr](https://x.com/ericmaskfr))

**Testez un brief de monde ouvert sur une section jouable.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un prototype inspiré de GTA et indique une durée d’environ 2 h 14 min.

Prompt d’origine

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [Paris en 1940 à partir d’images de référence](https://x.com/higgsfield_ai/status/2119910344998912507) (par [@higgsfield_ai](https://x.com/higgsfield_ai))

**Séparez la création des références du code de la scène.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ Lire la vidéo</a>

Higgsfield a fourni des images via son MCP et utilisé Fable 5.2 pour une scène Three.js.

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable planifie un court métrage rendu par Opus](https://x.com/kloss_xyz/status/2119910613828980846) (par [@kloss_xyz](https://x.com/kloss_xyz))

**Distinguez planification et réalisation dans un flux vidéo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ Lire la vidéo</a>

Fable 5.2 a rédigé le brief et le plan. Opus 5.5 a créé l’animation de 16 secondes dans Blender et Python et synthétisé la musique.

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [Un essai de clip musical](https://x.com/WesRoth/status/2119911161386934330) (par [@WesRoth](https://x.com/WesRoth))

**Vérifiez les paroles et la séquence générée.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage un clip fait avec Fable 5.2 et commente ses paroles.

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Un portrait peint de Dario Amodei](https://x.com/Mr_Salio/status/2119911922577637543) (par [@Mr_Salio](https://x.com/Mr_Salio))

**Comparez le portrait stylisé avec la référence affichée à côté.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage un portrait de Dario Amodei qu’il attribue à Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [Spud Smash en mode Medium](https://x.com/argofowl/status/2119913148929187960) (par [@argofowl](https://x.com/argofowl))

**Donnez au prototype des actions et un objectif clairs.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un personnage pomme de terre qui frappe, percute de la tête ou brûle des chaises bleues.

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Cathédrale de glace avec Fable et Opus](https://x.com/QQTeng/status/2119913518015435103) (par [@QQTeng](https://x.com/QQTeng))

**Comparez le coût et la durée de génération pour une même scène.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur indique environ 1 h 57 min et 81,10 USD pour Fable, contre environ 3 h 11 min et 45,97 USD pour Opus.

Prompt d’origine

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [Chant avec des conduits vocaux simulés](https://x.com/banteg/status/2119914098171199996) (par [@banteg](https://x.com/banteg))

**Utilisez un modèle physique de la voix comme entrée de production musicale.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une reprise réalisée avec deux simulations de conduits vocaux Chimera et un mixage au vocodeur.

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [Trois tests de voxels à Istanbul](https://x.com/Avenoxai/status/2119914308603953485) (par [@Avenoxai](https://x.com/Avenoxai))

**Comparez une démolition, une horloge fonctionnelle et une carte.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre trois tests à consigne unique et annonce des scores de 100, 100 et 95,6 selon sa propre grille.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Projets achevés dans le Remote Labor Index](https://x.com/ScaleAILabs/status/2119914701736075489) (par [@ScaleAILabs](https://x.com/ScaleAILabs))

**Interprétez le taux au regard des projets évalués.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ Lire la vidéo</a>

Scale Labs et CAIS indiquent que Fable 5.2 a mené à bien 41,3 % des projets de travail à distance évalués.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [Scène d’iceberg à quatre niveaux d’effort](https://x.com/0xRhinoX/status/2119915121698840587) (par [@0xRhinoX](https://x.com/0xRhinoX))

**Comparez le résultat, le coût et le détail quand l’effort augmente.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a employé la même consigne aux quatre niveaux. High a omis l’aurore. Ultra a ajouté de la glace lumineuse et une vue sous-marine.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [Un court anime de soixante-dix-neuf secondes](https://x.com/anstapnever/status/2119915123070644263) (par [@anstapnever](https://x.com/anstapnever))

**Examinez la continuité des scènes dans une animation plus longue.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage un clip d’anime de 79 secondes qu’il attribue à un processus avec Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Assemblages mécaniques avec Fable et Opus](https://x.com/ivanainai/status/2119915243321397550) (par [@ivanainai](https://x.com/ivanainai))

**Comparez la manière dont chaque modèle dispose les pièces.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre deux rendus annotés de Fable 5.2 et Opus 5.5, sous forme de vues éclatées d’une roue et d’engrenages.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [Une main robotisée gravit un escalier en colimaçon](https://x.com/Luckyballa/status/2119915557663506720) (par [@Luckyballa](https://x.com/Luckyballa))

**Utilisez un obstacle simulé pour observer un déplacement inhabituel.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un test de Fable 5.2 et Steel 0.1 où une main Wuji marche sur ses doigts.

[Sources associées 1](https://github.com/skild-ai/steel-webgpu/pull/7)

Prompt d’origine

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [Rigging d’un maillage Tripo dans Blender](https://x.com/0xKense1/status/2119916096098582566) (par [@0xKense1](https://x.com/0xKense1))

**Fixez des critères mesurables pour la prise, la texture et la déformation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur compare deux rigs issus de ressources Tripo. Fable a produit deux clips en 36 minutes et Opus huit en 21 minutes environ.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [Inventions interactives d’après le carnet de Léonard de Vinci](https://x.com/alexalbert__/status/2119916954337349737) (par [@alexalbert__](https://x.com/alexalbert__))

**Basez un modèle pédagogique interactif sur des dessins originaux.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ Lire la vidéo</a>

Alex Albert a fourni un PDF du carnet de Léonard et partagé une interprétation interactive de ses inventions.

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [Une station audio pilotée par Claude](https://x.com/The_Alex/status/2119917226769985785) (par [@The_Alex](https://x.com/The_Alex))

**Utilisez un outil piloté par agent pour des demandes de composition récurrentes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre une station de travail audio créée avec Fable 5.2 et indique qu’Opus l’a ouverte ensuite pour composer un morceau.

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [Un Raspberry Pi 5 animé](https://x.com/sparklabhq/status/2119917375080521921) (par [@sparklabhq](https://x.com/sparklabhq))

**Inspectez les composants à l’aide d’une animation de produit.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage un Raspberry Pi 5 animé avec Fable 5.2.

Prompt d’origine

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [Une scène du nord de l’Italie](https://x.com/Angaisb_/status/2119917807119089926) (par [@Angaisb_](https://x.com/Angaisb_))

**Observez le paysage et l’atmosphère dans un brief ancré dans un lieu.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une scène de Fable 5.2 située dans le nord de l’Italie.

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [Livre pop-up avec des agents d’exécution locaux](https://x.com/atomicagent_io/status/2119918110752846094) (par [@atomicagent_io](https://x.com/atomicagent_io))

**Comparez orchestration et modèle seul sur une même tâche.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ Lire la vidéo</a>

Atomic indique 2,98 USD en 11 minutes quand Fable coordonne des agents Qwen locaux, contre 15,77 USD en 21 minutes avec Fable seul.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [Le retour du test de la lampe à lave](https://x.com/eidzoku/status/2119918134060601690) (par [@eidzoku](https://x.com/eidzoku))

**Comparez plusieurs modèles sur la même tâche visuelle.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a relancé un test de lampe à lave et a partagé le comparatif visuel.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [Un avion à réaction détaillé dans Blender](https://x.com/higgsfield_ai/status/2119918248955392431) (par [@higgsfield_ai](https://x.com/higgsfield_ai))

**Précisez le nombre de pièces, la durée et l’apparence dans le brief.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ Lire la vidéo</a>

Higgsfield décrit un modèle Blender de 931 pièces et 24 260 rivets produit par script avec Fable 5.2 et son MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [Un voyage par portails entre des centaines de mondes](https://x.com/emollick/status/2119918307457577163) (par [@emollick](https://x.com/emollick))

**Reliez par des portails des environnements générés indépendamment.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ Lire la vidéo</a>

Ethan Mollick rapporte que 25 000 agents ont créé plus de 450 mondes en code et partage un jeu et son dépôt.

[Sources associées 1](https://portals-endless-worlds.netlify.app/) · [Sources associées 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [Un bazar de Bombay en six plans avec Three.js](https://x.com/higgsfield_ai/status/2119918834841010320) (par [@higgsfield_ai](https://x.com/higgsfield_ai))

**Découpez le brief visuel en plans de durée définie.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ Lire la vidéo</a>

Higgsfield montre une séquence de bazar de 21,5 secondes, rendue en six plans dans Three.js.

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [Un diner photoréaliste créé en code](https://x.com/higgsfield_ai/status/2119918838490010008) (par [@higgsfield_ai](https://x.com/higgsfield_ai))

**Examinez les matériaux et la lumière dans une scène programmée.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ Lire la vidéo</a>

Higgsfield montre un diner et indique l’avoir créé en code sans logiciel de modélisation 3D.

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [Un modèle de robot dans Blender](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (par [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Vérifiez les articulations et la silhouette dans une vue tournante.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un petit robot mécanique construit dans une démonstration Blender avec Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [Une vidéo animée pour expliquer Convex](https://x.com/Rasmic/status/2119919466163093768) (par [@Rasmic](https://x.com/Rasmic))

**Présentez un produit pour développeurs avec une courte animation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une animation explicative sur Convex faite avec Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [Une collection de pages d’accueil créées en une consigne](https://x.com/daradoescode/status/2119919529807466594) (par [@daradoescode](https://x.com/daradoescode))

**Comparez la hiérarchie et la mise en page sur plusieurs briefs courts.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une vidéo qui regroupe des pages d’accueil créées avec Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [Une sonate pour piano écrite en LilyPond](https://x.com/imjustnewatai/status/2119919644836347926) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Gardez un lien entre la partition source et la vidéo rendue.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a demandé un mouvement dans le style de Beethoven et indique que les notes affichées proviennent du fichier LilyPond.

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [Un brief vidéo en création libre](https://x.com/aollivier82/status/2119920990893244510) (par [@aollivier82](https://x.com/aollivier82))

**Utilisez un brief ouvert pour observer les choix créatifs spontanés.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre le résultat de sa demande à Fable 5.2 de créer la plus belle vidéo possible.

Prompt d’origine

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable planifie, DeepSeek implémente et Opus relit](https://x.com/ivanfioravanti/status/2119921810267636201) (par [@ivanfioravanti](https://x.com/ivanfioravanti))

**Confiez coordination, implémentation et revue à des agents différents.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre Fable coordonnant quatre agents DeepSeek V4.1 Flash via herdr, tandis qu’Opus 5.5 relit les pull requests.

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [Fable 5.2 dans AI Village](https://x.com/aidigest_/status/2119923190411719158) (par [@aidigest_](https://x.com/aidigest_))

**Examinez séparément la réponse de l’agent et ses actions sur la mémoire.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

Le journal public montre que Fable accepte de modifier sa mémoire plus tard à la demande d’un autre agent. Une publication associée montre un test de correspondance avec des personnages.

[Sources associées 1](https://x.com/aidigest_/status/2119923209311260707) · [Sources associées 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [Design de frontend avec et sans skills](https://x.com/AdamHoltererer/status/2119924849321914653) (par [@AdamHoltererer](https://x.com/AdamHoltererer))

**Gardez le modèle fixe et modifiez la configuration des skills.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

L’auteur présente deux interfaces faites avec Fable 5.2, l’une avec des skills et l’autre sans.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [Détecter les machines à états implicites dans le code](https://x.com/kunchenguid/status/2119924895060795492) (par [@kunchenguid](https://x.com/kunchenguid))

**Auditez un module précis et demandez des schémas avant-après.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

L’auteur montre une amélioration dans le dépôt Firstmate et publie la consigne d’audit exacte.

[Sources associées 1](https://github.com/kunchenguid/lavish-axi)

Prompt d’origine

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [Un jeu créé de zéro en huit heures](https://x.com/felixrieseberg/status/2119925633564463609) (par [@felixrieseberg](https://x.com/felixrieseberg))

**Consignez les entrées mises en cache, les ressources générées et le temps écoulé.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ Lire la vidéo</a>

L’ingénieur d’Anthropic indique avoir créé modèles, sons et textures en une seule exécution, pour un coût équivalent à environ 550 USD via l’API.

[Sources associées 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [Sources associées 2](https://x.com/AndrewCurran_/status/2119953960794780133)

Prompt d’origine

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Prototype de Fishslop et coût en tokens](https://x.com/theo/status/2119926277801144695) (par [@theo](https://x.com/theo))

**Comparez une version du jeu à un résultat d’un modèle précédent.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ Lire la vidéo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

L’auteur annonce 76 minutes et environ 42 USD en tokens, puis compare le résultat à celui d’Opus 5.5.

[Sources associées 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [Un jeu de football américain en mouvement](https://x.com/WesRoth/status/2119926801514529027) (par [@WesRoth](https://x.com/WesRoth))

**Testez les signaux visuels et les indications de score dans un prototype sportif.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un jeu fait avec Fable 5.2 qui signale les actions de score à l’écran.

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [Combat de boss en monde ouvert avec Higgsfield MCP](https://x.com/higgsfield_ai/status/2119926932343324795) (par [@higgsfield_ai](https://x.com/higgsfield_ai))

**Distinguez le jeu jouable de ses cinématiques.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ Lire la vidéo</a>

Higgsfield décrit un jeu de navigateur en monde ouvert, avec un combat de boss en trois actes et des cinématiques produits avec Fable 5.2 et son MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [Mont-Saint-Michel au rythme des marées](https://x.com/loktar00/status/2119927152489472076) (par [@loktar00](https://x.com/loktar00))

**Testez les variations de niveau d’eau dans une petite scène historique.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre une miniature du Mont-Saint-Michel aux marées animées.

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [Un élément de Roblox dans Blender](https://x.com/hiyouwhatsapp/status/2119927163264573642) (par [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**Examinez l’élément dans Blender avant de l’importer.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un résultat Blender pour Roblox obtenu presque en une seule consigne.

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [Raisonnement sans chaîne de pensée en sortie](https://x.com/Tim_Hua_/status/2119927284761293089) (par [@Tim_Hua_](https://x.com/Tim_Hua_))

**Évaluez les réponses avec la même contrainte de sortie.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

L’évaluateur a lancé des tests de raisonnement et de connaissances sans chaîne de pensée en sortie et place Fable 5.2 juste derrière GPT-6.1 Sol.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [Variations de Chrome Dino avec quatre modèles](https://x.com/noclipepe/status/2119927838321328577) (par [@noclipepe](https://x.com/noclipepe))

**Comparez durée et coût sur un brief de jeu récurrent.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur ajoute Fable 5.2 à un test précédent de T-Rex avec Opus, Gemini et Astra et montre les résultats ensemble.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [Jeu de dames avec un bras robotisé](https://x.com/karolina_dubiel/status/2119928342115676576) (par [@karolina_dubiel](https://x.com/karolina_dubiel))

**Relisez les positions articulaires et recommencez les prises ratées.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur indique que le modèle a corrigé un affaissement d’environ 7 mm et réessayé les mouvements ratés grâce au retour fourni.

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [Une animation graphique de quinze secondes](https://x.com/aziz4ai/status/2119928581405200726) (par [@aziz4ai](https://x.com/aziz4ai))

**Consignez la part du quota utilisée par une courte animation en code.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une scène de 15 secondes réalisée en code et indique avoir utilisé 4 % d’un quota hebdomadaire.

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [Une tour Eiffel jouable](https://x.com/bobyau/status/2119928812628771212) (par [@bobyau](https://x.com/bobyau))

**Vérifiez si la modélisation d’un monument permet d’interagir avec lui.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une démonstration de la tour Eiffel et indique 25 minutes de réalisation.

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [Course en haute mer avec Three.js et Higgsfield](https://x.com/higgsfield_ai/status/2119928918035910668) (par [@higgsfield_ai](https://x.com/higgsfield_ai))

**Séparez la logique du jeu des outils de production média.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ Lire la vidéo</a>

Higgsfield montre un jeu de course avec de grandes vagues, cinq adversaires IA et des roquettes à tête chercheuse.

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [Simulation de miel en temps réel dans WebGL](https://x.com/deedydas/status/2119930300990177509) (par [@deedydas](https://x.com/deedydas))

**Testez le mouvement d’un matériau avec une simulation physique dans le navigateur.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre une simulation de miel dans WebGL en temps réel et publie le brief original.

Prompt d’origine

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [Effets visuels programmés sur de la vidéo](https://x.com/ashebytes/status/2119930763105931649) (par [@ashebytes](https://x.com/ashebytes))

**Vérifiez le placement et le calage des effets sur le métrage d’origine.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un test d’effets visuels de Fable 5.2 avec des graphismes animés superposés à des prises de vue réelles.

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [Une animation sur les niveaux de recherche dans GTA](https://x.com/saimagnate/status/2119931563760632311) (par [@saimagnate](https://x.com/saimagnate))

**Associez images de jeu et schémas pour expliquer une mécanique.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur attribue le résultat à une seule demande à Fable 5.2. La vidéo compare les systèmes de recherche de GTA V et RDR2 avec des extraits et des schémas.

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [Un monde de MMO stylisé créé en code](https://x.com/Izkimar/status/2119931740940640542) (par [@Izkimar](https://x.com/Izkimar))

**Évaluez la cohérence du monde à travers ses éléments stylisés.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur rapporte avoir créé en un jour le monde de MMO montré, à partir d’éléments générés en code.

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [Une scène 3D avec Fable et Opus](https://x.com/dom_scholz/status/2119933150025363661) (par [@dom_scholz](https://x.com/dom_scholz))

**Comparez la durée de mise en place et le niveau de détail sur une même vue.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre les rendus de Fable 5.2 et Opus 5.5 et indique que Fable a terminé plus vite.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [Texte redondant dans un menu de pause](https://x.com/AndrewPrifer/status/2119934600608915465) (par [@AndrewPrifer](https://x.com/AndrewPrifer))

**Repérez les explications répétées dans le texte généré pour l’interface.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

Le développeur montre un menu de pause comme exemple de texte explicatif superflu produit par Fable 5.2.

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [Planches d’inspiration dans un environnement Krea](https://x.com/lambdacalcc/status/2119934725662060663) (par [@lambdacalcc](https://x.com/lambdacalcc))

**Comparez les concepts avant de choisir une direction visuelle.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

L’auteur partage quatre résultats d’une séance de moodboards avec Fable 5.2 dans un environnement Krea.

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [Essais au bureau d’un jeu de tir avec portails](https://x.com/_sholtodouglas/status/2119935331499925557) (par [@_sholtodouglas](https://x.com/_sholtodouglas))

**Évaluez un jeu généré lors de parties multijoueurs.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ Lire la vidéo</a>

Un ingénieur d’Anthropic montre un FPS d’arène avec portails et décrit les essais au bureau.

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Un objet à surfaces rigides détaillé dans Blender](https://x.com/ziwenxu_/status/2119937420280168929) (par [@ziwenxu_](https://x.com/ziwenxu_))

**Inspectez la topologie et la silhouette dans la vue 3D de Blender.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un objet à surfaces rigides présenté comme un résultat de Fable 5.2 dans Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [Essais parallèles de frontend à plusieurs niveaux d’effort](https://x.com/AI_masaou/status/2119937635322085640) (par [@AI_masaou](https://x.com/AI_masaou))

**Comparez des briefs simples et ambitieux à différents niveaux d’effort.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

L’auteur décrit des résultats simples similaires, davantage de détails dans les grandes productions de Fable et une hausse marquée du temps et des tokens entre Medium et High.

[Sources associées 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [Un petit jeu en dix consignes](https://x.com/AmirMushich/status/2119937977426338283) (par [@AmirMushich](https://x.com/AmirMushich))

**Suivez le nombre d’itérations et la taille du prototype.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur indique que le jeu fait 220 Ko et environ 3 400 lignes et fournit le code et la vidéo.

[Sources associées 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [Animation image par image en JavaScript](https://x.com/kevin_t_ngo/status/2119938129079808282) (par [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Examinez une séquence dont les images sont dessinées par programmation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une animation et indique que JavaScript a dessiné chaque image.

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [De la vidéo de référence à l’animation 3D](https://x.com/KHvostikk/status/2119939061049889130) (par [@KHvostikk](https://x.com/KHvostikk))

**Utilisez la vidéo source pour juger une scène reconstituée.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre une conversion vidéo vers animation 3D réalisée avec Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Feu de camp en pixel art avec Fable et Opus](https://x.com/GrilliotTodd/status/2119939651385655692) (par [@GrilliotTodd](https://x.com/GrilliotTodd))

**Comparez l’éclairage et les silhouettes sur le même sujet.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ Lire la vidéo</a>

Le comparatif montre des feux de camp réalisés avec Fable 5.2 et Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [Arena WebDev en mode xHigh](https://x.com/arena/status/2119941204003770690) (par [@arena](https://x.com/arena))

**Comparez les résultats au niveau d’effort employé pour le classement.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena indique un résultat initial de 1 832 points pour Claude Fable 5.2 xHigh dans Code Arena WebDev.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [Typographie de bande-annonce avec deux modèles](https://x.com/muku_sns/status/2119941490969624679) (par [@muku_sns](https://x.com/muku_sns))

**Comparez deux interprétations du même paragraphe.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre les titres d’Opus et de Fable côte à côte. Fable ajoute une bordure rouge et des titres caviardés.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [Essais de motion design et de portfolio 3D en une consigne](https://x.com/Khazix0918/status/2119941585538572390) (par [@Khazix0918](https://x.com/Khazix0918))

**Testez séparément recherche, conception et rendu.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ Lire la vidéo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ Lire la vidéo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ Lire la vidéo</a></td></tr></table>

L’auteur partage quatre essais, avec un clip anniversaire de ChatGPT, une explication de DeepSeek, une scène Three.js et une reconstitution 3D d’Apple Jing’an.

[Sources associées 1](https://x.com/Khazix0918/article/2119941585538572390)

Prompt d’origine

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [Un réacteur nucléaire à explorer](https://x.com/konstantinsaifo/status/2119941967136379334) (par [@konstantinsaifo](https://x.com/konstantinsaifo))

**Montrez l’assemblage des pièces avec une fonction de démontage.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a demandé un réacteur démontable dans Three.js et indique 92 USD de frais d’API.

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Agents dans Blood on the Clocktower](https://x.com/dwarkesh_sp/status/2119942657812451482) (par [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**Comparez les modèles sur un même jeu à rôles cachés.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

L’évaluateur classe Fable 5.2 devant Fable 5.1 et Opus 5.5, avec GPT-6 Astra en tête de ce test.

[Sources associées 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [Prototype de course de pods](https://x.com/loktar00/status/2119943124965638444) (par [@loktar00](https://x.com/loktar00))

**Utilisez un format de course connu pour juger les mouvements et les commandes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une production de Fable 5.2 inspirée des courses de pods.

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [Une publicité de dix secondes pour les sous-vêtements Claude](https://x.com/Masimo_Blue/status/2119943368612487285) (par [@Masimo_Blue](https://x.com/Masimo_Blue))

**Testez un brief produit ouvert avec une musique originale.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ Lire la vidéo</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

L’auteur partage une publicité de dix secondes avec de l’acid techno et les images produit fournies.

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [Un oiseau au lever du soleil, trait après trait](https://x.com/mgrczyk/status/2119943813028548721) (par [@mgrczyk](https://x.com/mgrczyk))

**Désactivez l’annulation pour observer les décisions de dessin successives.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un oiseau peint au lever du soleil dans un environnement qui interdisait de modifier les traits précédents.

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [Un long essai graphique dans Devin](https://x.com/Da7_Tech/status/2119944847255896490) (par [@Da7_Tech](https://x.com/Da7_Tech))

**Consignez la durée et le coût d’un rendu exigeant.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ Lire la vidéo</a>

Un ambassadeur déclaré de Cognition montre un essai avec Devin Max qui aurait duré environ 3,5 heures et coûté 82 USD.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [Peinture programmée avec trois modèles](https://x.com/kickingkeys/status/2119945841997672698) (par [@kickingkeys](https://x.com/kickingkeys))

**Comparez le tracé et le son synthétisé entre les essais.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une peinture réalisée en code avec du son et décrit des tests avec la même consigne sur Fable 5.2, Fable 5.1 et Gemini 4 Argon.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [L’histoire de l’écriture en mouvement](https://x.com/rileybrown/status/2119946022767980985) (par [@rileybrown](https://x.com/rileybrown))

**Suivez une chronologie pour organiser une explication animée en code.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre une animation sur l’histoire de l’écriture et indique l’avoir produite avec une seule consigne.

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [Terrain d’essai pour des engins de jeu](https://x.com/techartist_/status/2119946891106394518) (par [@techartist_](https://x.com/techartist_))

**Éprouvez les mécaniques, la physique et les effets dans une scène commune.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a créé avec Three.js et Blender un terrain d’essai pour quatre concepts.

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [Circuit imprimé pour une console Linux portable](https://x.com/seveibar/status/2119947341230907453) (par [@seveibar](https://x.com/seveibar))

**Comparez les modèles sur un même cahier des charges électronique.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ Lire la vidéo</a>

Le créateur de tscircuit montre un test de conception de console Linux portable avec Astra 6 High et Fable 5.2 High.

Prompt d’origine

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [Un lac en voxels](https://x.com/Angaisb_/status/2119947748690841841) (par [@Angaisb_](https://x.com/Angaisb_))

**Utilisez un petit environnement pour juger la composition.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage un lac en voxels qu’il attribue à Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [Les 17 générations interactives d’Arena](https://x.com/arena/status/2119948067449536733) (par [@arena](https://x.com/arena))

**Explorez différents types de production avant de choisir une tâche d’évaluation.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ Lire la vidéo</a>

Arena partage 17 productions, dont des mondes 3D, des jeux, des interfaces, des visualisations et des animations programmées.

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [Vol avec un dragon amical](https://x.com/chetanankola/status/2119951015407738913) (par [@chetanankola](https://x.com/chetanankola))

**Évaluez la caméra et les mouvements sur un parcours en vol.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur présente une scène de dragon réalisée avec Three.js et Blender et décrit les améliorations apportées avec Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Orque en gelée avec Fable et Opus](https://x.com/vib3coded/status/2119951060752375827) (par [@vib3coded](https://x.com/vib3coded))

**Comparez la surface et le mouvement sur un même sujet.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre côte à côte les versions de l’orque en gelée de Fable 5.2 et Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [Test vidéo en création libre](https://x.com/suna_gaku/status/2119952985933697063) (par [@suna_gaku](https://x.com/suna_gaku))

**Donnez une consigne ouverte pour observer les choix créatifs du modèle.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a demandé au modèle de montrer sa meilleure production vidéo, puis a partagé le résultat.

Prompt d’origine

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [Habitat spatial d’inspiration méditerranéenne](https://x.com/MaxXWilliamson/status/2119953172634677533) (par [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**Combinez une consigne courte et les outils déjà utilisés dans le projet.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a fourni les outils de précédents habitats spatiaux et demandé une station d’inspiration méditerranéenne.

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [Benchmark AA-3D d’expériences interactives](https://x.com/ArtificialAnlys/status/2119953570430881946) (par [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Lisez le classement Elo avec son intervalle d’incertitude.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ Lire la vidéo</a>

Artificial Analysis publie un résultat initial de 1 271 Elo pour Fable 5.2 Max dans son benchmark d’expériences 3D interactives.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [Un défi chronométré avec un personnage squelettique](https://x.com/WesRoth/status/2119953913160093817) (par [@WesRoth](https://x.com/WesRoth))

**Évaluez le prototype jouable à l’aide d’un minuteur visible.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur montre un résultat de Fable 5.2 en une seule consigne, avec un personnage squelettique et un compte à rebours à l’écran.

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Pixel art avec Fable et Astra](https://x.com/Angaisb_/status/2119955179915137294) (par [@Angaisb_](https://x.com/Angaisb_))

**Comparez les formes et les détails à une échelle identique.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ Lire la vidéo</a>

Le comparatif original montre des productions en pixel art de GPT-6 Astra et Fable 5.2.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [Bande démo de motion design](https://x.com/Leviwoyun/status/2119955625820258308) (par [@Leviwoyun](https://x.com/Leviwoyun))

**Proposez un brief ouvert assorti d’une durée fixe.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur partage une bande démo musicale et indique 24 minutes de production.

Prompt d’origine

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [Rendu d’une piscine de verre avec deux modèles](https://x.com/MrTacticalX/status/2119955647542542439) (par [@MrTacticalX](https://x.com/MrTacticalX))

**Comparez l’éclairage, la durée et le coût.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur indique 90 minutes et 57,87 USD pour Fable, contre 68 minutes et 14,39 USD pour Opus.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [Précision des appels d’outils sur TS-Bench](https://x.com/gosrum/status/2119956559031927079) (par [@gosrum](https://x.com/gosrum))

**Suivez séparément les erreurs d’appel et la consommation de tokens.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

L’évaluateur ne relève aucune erreur d’appel d’outil pour Fable 5.2 et précise que les tâches simples différencient peu les variantes de Claude.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [Machu Picchu en miniature](https://x.com/loktar00/status/2119958719362666708) (par [@loktar00](https://x.com/loktar00))

**Examinez l’atmosphère et les petits détails d’une scène miniature.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ Lire la vidéo</a>

La démonstration du Machu Picchu comporte de la brume volumétrique et de petits alpagas.

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [GDPx par catégorie de tâches professionnelles](https://x.com/SemiAnalysis_/status/2119961447199289640) (par [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**Examinez le détail des tâches avec le résultat global.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

L’éditeur du benchmark indique un score global de 16,4 % et présente des résultats par domaine, notamment la conception de puces et le génie logiciel.

[Sources associées 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [Sources associées 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [Sources associées 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [Un portrait dans un logiciel de dessin](https://x.com/The_Alex/status/2119964472559489229) (par [@The_Alex](https://x.com/The_Alex))

**Utilisez une vignette de référence pour guider le portrait.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a demandé à Fable 5.2 d’ouvrir un logiciel de dessin et de faire son portrait. La vidéo montre le passage des contours au dessin terminé.

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [VulcanBench Frontier v4 en mode Low](https://x.com/morganlinton/status/2119966067527467215) (par [@morganlinton](https://x.com/morganlinton))

**Comparez les générations à un niveau d’effort identique.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

L’auteur du benchmark indique environ 5 minutes par tâche pour Fable 5.2, contre 26 pour Fable 5.1, en mode Low.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [Un jeu Backrooms aux rôles inversés](https://x.com/LexnLin/status/2119966127149429093) (par [@LexnLin](https://x.com/LexnLin))

**Changez l’objectif du joueur pour mettre un concept à l’épreuve.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ Lire la vidéo</a>

Le joueur dirige le monstre et tente d’attraper des personnes. L’auteur partage une vidéo de jeu et un lien pour y jouer.

[Sources associées 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [Une Bugatti Tourbillon dans Blender](https://x.com/xikhar/status/2119966147328299284) (par [@xikhar](https://x.com/xikhar))

**Définissez l’extérieur et l’intérieur à l’aide de références visuelles.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur indique avoir modélisé une Bugatti Tourbillon, intérieur compris, puis produit un rendu cinématographique à partir d’une consigne et d’images de référence.

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [Une vidéo sur l’informatique réalisée avec deux modèles](https://x.com/daradoescode/status/2119966154391183522) (par [@daradoescode](https://x.com/daradoescode))

**Consignez la contribution de chaque modèle dans un processus mixte.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a partagé une vidéo stylisée réalisée avec Fable 5.2 et une contribution importante d’Opus 5.5.

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [Un clip musical sur les megakernels](https://x.com/elliotarledge/status/2119968762069934415) (par [@elliotarledge](https://x.com/elliotarledge))

**Prenez un concept technique pour sujet de vidéo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a demandé à Fable 5.2 en mode High un clip sur les megakernels, puis a partagé le résultat.

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [Visite d’un studio à partir de photos de référence](https://x.com/rpnickson/status/2119969928304357507) (par [@rpnickson](https://x.com/rpnickson))

**Appuyez la reconstitution d’une scène sur des photos réelles.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a fourni des photos de son studio, adapté un brief vidéo similaire et indiqué une durée d’exécution d’environ deux heures.

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [Une publicité pour jouets des années 1990 réalisée en code](https://x.com/kevin_t_ngo/status/2119972124211454139) (par [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Séparez les scripts d’animation du rendu.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur indique avoir animé une publicité rétro pour des jouets avec Python, puis effectué le rendu dans Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Scène de jeu à la troisième personne avec Three.js](https://x.com/bijanbowen/status/2119972220739187182) (par [@bijanbowen](https://x.com/bijanbowen))

**Observez le mouvement et le décor pendant une partie.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

L’auteur montre en direct une scène Three.js avec un personnage à la troisième personne dans un environnement extérieur.

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [Bryceball à partir d’un moteur de rendu existant](https://x.com/pleometric/status/2119973274402668852) (par [@pleometric](https://x.com/pleometric))

**Réutilisez un moteur de rendu pour créer un jeu.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a adapté le moteur de rendu décrit dans la publication liée pour créer le jeu Bryceball.

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [Montage vidéo récursif avec Fable](https://x.com/rileybrown/status/2119973951027724385) (par [@rileybrown](https://x.com/rileybrown))

**Réutilisez un montage antérieur dans une nouvelle production.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a partagé une vidéo montée avec Fable 5.2, consacrée à une vidéo qu’il avait déjà montée avec le modèle.

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [Une histoire cinématographique des sciences](https://x.com/DeryaTR_/status/2119974354260013293) (par [@DeryaTR_](https://x.com/DeryaTR_))

**Organisez une séquence 3D autour d’une chronologie.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a demandé un voyage des débuts de la science à un avenir spéculatif et a partagé la vidéo obtenue.

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [La machine volante de Léonard de Vinci en 3D](https://x.com/higgsfield_ai/status/2119975721909301684) (par [@higgsfield_ai](https://x.com/higgsfield_ai))

**Modélisez une invention historique avant de tester des modifications.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ Lire la vidéo</a>

Higgsfield a montré une interprétation 3D de la machine volante de Léonard et décrit un test physique et une refonte.

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [Routage de circuit imprimé à partir d’un cahier des charges](https://x.com/cmonkey/status/2119975852977029365) (par [@cmonkey](https://x.com/cmonkey))

**Inspectez la carte routée avant sa fabrication.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

L’auteur a partagé un routage de circuit imprimé réalisé par Fable 5.2, en réponse à un échange sur l’implantation des composants.

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [Une même consigne dans deux environnements](https://x.com/loktar00/status/2119980613369319706) (par [@loktar00](https://x.com/loktar00))

**Notez les différences d’environnement lorsque vous comparez les résultats.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a donné la même consigne à DeepSeek et Fable 5.2 dans des environnements distincts et a montré leurs résultats côte à côte.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [Illustration de Godzilla dessinée en code](https://x.com/chetaslua/status/2119981510199808368) (par [@chetaslua](https://x.com/chetaslua))

**Réinterprétez une image par des formes vectorielles et du mouvement.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur a partagé une illustration dessinée en code, accompagnée d’une courte animation inspirée d’une publication sur Godzilla.

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [Ventilateur à main conçu pour l’impression 3D](https://x.com/davelee/status/2119981787325579398) (par [@davelee](https://x.com/davelee))

**Vérifiez l’assemblage sur un prototype physique.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur et ses enfants ont conçu un ventilateur à main imprimable et partagé le modèle avant de l’imprimer.

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [Recherche de bugs dans un plugin face à Opus](https://x.com/oaranda/status/2119982729747919096) (par [@oaranda](https://x.com/oaranda))

**Comparez les correctifs avec des tests de régression croisés.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

Extrait de l’annonce annoté par l’auteur.

Les deux modèles ont trouvé les mêmes six bugs. Opus a réussi les tests croisés. Fable en a raté un et a détecté un autre problème dans le tableau de bord.

Prompt d’origine

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [Istanbul reconstituée en 3D](https://x.com/petergostev/status/2119877733488394520) (par [@petergostev](https://x.com/petergostev))

**Examinez une scène urbaine en plan large et de près.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ Lire la vidéo</a>

Peter Gostev montre une scène 3D d’Istanbul obtenue avec Fable 5.2 Max et fournit l’évaluation détaillée.

[Sources associées 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [Un film Blender avec un écran fonctionnel](https://x.com/rileybrown/status/2119902109709537708) (par [@rileybrown](https://x.com/rileybrown))

**Animez l’écran, la lumière et la caméra dans la même scène 3D.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ Lire la vidéo</a>

L’auteur indique 13 plans, une page web personnalisée lue sur le portable et du son ElevenLabs. Le rendu a utilisé des GPU de RunPod.

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [Une transition de trou noir à couplage faible](https://hexagonmath.org/2611.00175v1) (par [@Anthropic](https://www.anthropic.com/))

**Vérifiez un calcul resté ouvert à partir de son cadre théorique d’origine.**

Anthropic indique que Fable 5.2 a achevé un calcul ancien et trouvé une transition abrupte à faible couplage. La prépublication détaille la dérivation.

[Sources associées 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [La limite d’une borne du bootstrap modulaire](https://hexagonmath.org/2611.00174v1) (par [@Anthropic](https://www.anthropic.com/))

**Publiez la dérivation avec la borne analytique proposée.**

Anthropic indique que Fable 5.2 a déterminé la limite exacte d’une technique de bootstrap modulaire sans spin dans un cadre simplifié de gravité quantique.

[Sources associées 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Vercel AI Gateway avec des modèles de repli ordonnés](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (par [Vercel](https://vercel.com/))

**Configurez l’ordre de repli des requêtes refusées par le classificateur.**

L’exemple Vercel AI SDK appelle anthropic/claude-fable-5.2 et configure Opus 5.5 puis Sonnet 5.5 en repli. Le guide documente l’exigence de conservation des données.

[Sources associées 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [Sous-agents imbriqués et budget de revue](https://news.ycombinator.com/item?id=50430925) (par [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**Suivez la délégation imbriquée et imposez des limites hors du prompt.**

L’auteur avait demandé quatre sous-agents au maximum pour examiner 80 000 lignes. Il indique au moins six agents imbriqués et un quota de cinq heures épuisé en moins de 20 minutes.

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [Comparatif de conversion d’un design LCARS en HTML](https://news.ycombinator.com/item?id=50430962) (par [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**Vérifiez séparément courbes, icônes, animation et navigation.**

L’auteur compare Fable 5.2 et Opus 5.5 avec un même design inspiré de Star Trek. Il a préféré les courbes et certaines icônes de Fable, mais le mouvement d’Opus, et a trouvé le scintillement du SVG de Fable gênant. Seule la première page était demandée.

[Sources associées 1](https://html.non.io/lcars-fable-5.2/) · [Sources associées 2](https://html.non.io/lcars-opus-5.5/) · [Sources associées 3](https://news.ycombinator.com/item?id=50431231) · [Sources associées 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [Optimisation GPU de Quantum ESPRESSO](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (par [Discovered Materials](https://discoveredmaterials.com/))

**Exigez des résultats de référence et des tests cachés représentatifs pour optimiser du code scientifique.**

Discovered Materials annonce une accélération moyenne géométrique de 36× sur 13 tests de phonons avec le même GPU, et d’environ 9× pour les fonctionnelles hybrides. Le correctif publié s’appuie sur des tests d’exactitude et de performance.

[Sources associées 1](https://github.com/discovered-materials/dm_qe) · [Sources associées 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [Indice d’intelligence d’Artificial Analysis par effort](https://artificialanalysis.ai/models/claude-fable-5-2) (par [Artificial Analysis](https://artificialanalysis.ai/))

**Lisez ensemble score, coût et latence par tâche au niveau choisi.**

La mesure citée de Max avec repli par défaut indique un indice de 65, 26,54 USD et 46,4 minutes par tâche. Ces chiffres concernent la charge du benchmark.

[Sources associées 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [Faux positifs lors d’une revue en mode High](https://news.ycombinator.com/item?id=50431810) (par [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**Vérifiez les problèmes signalés dans le code avant d’agir.**

Un développeur rapporte que Fable 5.2 High a relevé deux problèmes inexistants, qu’il a décelés grâce à sa connaissance du code.

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [Trente tâches courantes de programmation](https://news.ycombinator.com/item?id=50432483) (par [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**Mesurez le temps et les tâches réussies sur une charge identique.**

L’auteur indique 26 réussites sur 30 pour Fable 5.2 et Opus 5.5, et 25 pour Fable 5.1. Fable 5.2 a pris 0,62 fois le temps de 5.1, sans blocage de sécurité signalé.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [Écran de veille d’un naufragé sur une île](https://news.ycombinator.com/item?id=50432836) (par [@nzach](https://news.ycombinator.com/user?id=nzach))

**Ouvrez la page interactive pour examiner directement l’écran de veille.**

L’auteur du Show HN renvoie à Stranded with Claude, une scène d’île pour navigateur. L’objet publié est un canvas interactif.

[Sources associées 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [Trois jeux pour navigateur en mode High](https://senko.net/vibecode-bench/) (par [Senko Rašić](https://senko.net/))

**Comparez séparément les mécaniques jouables et la fidélité visuelle.**

Senko Rašić a testé des briefs de stratégie, de voxels et de simulation de vol dans Claude Code avec Fable 5.2. Il relève des mécaniques plus riches, dont un dirigeable pour explorer toute la carte, et juge certains graphismes moins réussis.

[Sources associées 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [Scripts de podcast littéraire chapitre par chapitre](https://news.ycombinator.com/item?id=50434156) (par [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**Comparez la longueur des scripts pour une même tâche récurrente.**

L’auteur a généré des dialogues entre deux critiques, un chapitre à la fois. Il indique environ 2,5 pages pour Fable contre 4,5 pour Opus 5.5 et fournit les deux exemples.

[Sources associées 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [Sources associées 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [Un service de production migré vers Rust](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (par [@Anthropic](https://www.anthropic.com/))

**Mesurez le démarrage avant et après la migration.**

Anthropic indique que des agents utilisant une préversion de Fable 5.2 ont réécrit en Rust un service Python en production et divisé son temps de démarrage par environ 26.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [Choisir Fable 5.2 dans GitHub Copilot](https://x.com/github/status/2119926269982961833) (par [@github](https://x.com/github))

**Activez la politique de l’organisation avant de sélectionner le modèle.**

GitHub documente le sélecteur de modèles de Copilot et le réglage administrateur requis pour les comptes Business et Enterprise.

[Sources associées 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [Un défi de conception de cent pages HTML](https://x.com/MiaAI_lab/status/2119930229661503893) (par [@MiaAI_lab](https://x.com/MiaAI_lab))

**Comptez les fichiers finis et exécutables, puis évaluez leur apparence.**

L’auteur a demandé 100 designs variés et publié 76 fichiers avec leurs consignes. Il indique avoir atteint sa limite d’usage de Fable.

[Sources associées 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [Sources associées 2](https://mia-ai.net/lab/experiments/100-htmls) · [Sources associées 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [Sources associées 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [Sources associées 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [Sources associées 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [Sources associées 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [Sources associées 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [Sources associées 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [Sources associées 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [Sources associées 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [Sources associées 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [Sources associées 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [Sources associées 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [Dérive des exigences dans un travail de compilation](https://x.com/sameQCU/status/2119939304864800971) (par [@sameQCU](https://x.com/sameQCU))

**Comparez les exigences reformulées par l’agent avec le texte d’origine.**

Le développeur décrit une tâche de compilation dans laquelle Fable 5.2 et d’anciens modèles Opus ont mal retranscrit les exigences reçues.

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [Suivre une longue tâche Fable avec Opus](https://x.com/marouane53/status/2119950129767858262) (par [@marouane53](https://x.com/marouane53))

**Suivez la progression des longues tâches dans une session séparée.**

L’auteur indique que certaines tâches Fable ont dépassé deux heures avec peu de nouvelles. Dans un autre fil, Opus 5.5 lui a expliqué la progression et les décisions.

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [Relecture du code avec un regard neuf](https://x.com/doodlestein/status/2119958895158292786) (par [@doodlestein](https://x.com/doodlestein))

**Consacrez une passe distincte aux fichiers nouveaux et modifiés.**

L’auteur fournit deux consignes de suivi exactes pour repérer et corriger des erreurs après l’implémentation.

Prompt d’origine

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

Prompt d’origine

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [Perte de contexte lors d’une revue de conception](https://news.ycombinator.com/item?id=50434214) (par [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**Utilisez la conception actuelle comme liste de contrôle des conseils ultérieurs.**

L’auteur a comparé les deux modèles lors d’une revue de fonctionnalité et préféré Opus 5.5. Lors d’un diagnostic ultérieur, Fable 5.2 a recommandé une chose déjà prévue.

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [Comparaison de casse-briques dans le style de DX Ball](https://news.ycombinator.com/item?id=50434424) (par [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**Comparez les mécaniques et les sensations de jeu pour le même brief.**

L’auteur lie des versions issues d’essais distincts avec Fable 5.2 et Opus 5.5. Fable a changé certaines mécaniques originales. L’auteur a préféré jouer à la version d’Opus.

[Sources associées 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [Sources associées 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [Essai d’amélioration d’une application 3D](https://news.ycombinator.com/item?id=50434433) (par [@user43928](https://news.ycombinator.com/user?id=user43928))

**Comparez les changements visibles et le budget consommé sur la même tâche.**

L’auteur a demandé à Fable 5.2 d’améliorer une application 3D hors jeu. Il rapporte peu de différence avec Opus 5.5 et 25 % de son quota Fable consommé ce soir-là.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [Un jeu de chat et de souris avec trois modèles](https://news.ycombinator.com/item?id=50434508) (par [@simonw](https://news.ycombinator.com/user?id=simonw))

**Gardez la même consigne et examinez chaque version jouable.**

Simon Willison montre un jeu Three.js adapté au mobile avec Fable 5.2 Extra, Opus 5.5 Extra et GPT-6 Extra High. Il indique environ 40 minutes pour l’essai de Fable.

[Sources associées 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [Sources associées 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [Sources associées 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

Prompt d’origine

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [Coût et score dans AIBenchy en mode High](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (par [AIBenchy](https://aibenchy.com/))

**Comparez score, coût total et latence à niveau d’effort identique.**

AIBenchy publie 8,7 contre 9,4, 5,083 contre 2,133 USD au total et 14,73 contre 27,55 secondes en moyenne pour Fable 5.2 High et Opus 5.5 High.

[Sources associées 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [Régler l’environnement d’agents pour Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (par [@Anthropic](https://www.anthropic.com/))

**Retestez les niveaux d’effort et définissez les messages de progression.**

Le guide d’Anthropic fournit des exemples d’instructions sur l’effort, les critères d’achèvement, les approbations, le suivi et les limites des sous-agents.

[Sources associées 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="acknowledge"></a>
## Crédits

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/)
