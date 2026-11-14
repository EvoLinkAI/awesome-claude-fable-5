# Casos de uso de Claude Fable 5.2

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

Flujos de trabajo, demostraciones, comparaciones, evaluaciones, integraciones y límites prácticos de las recopilaciones del 10 y del 13–14 de noviembre, con enlaces a las fuentes.

[Anuncio de Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [Colección anterior](../../README_es.md)

## Índice de casos

| Case | Casos de uso | Type |
| --- | --- | --- |
| 330 | [Un MacBook en SVG con distintos niveles de esfuerzo](#case-330) | Benchmark |
| 331 | [Un juego de lucha para cuatro a partir de dibujos familiares](#case-331) | Demo |
| 332 | [Tres dispositivos electrónicos, del diseño al montaje](#case-332) | Demo |
| 333 | [Formalización del último teorema de Fermat en Lean](#case-333) | Evaluation |
| 334 | [Un sistema operativo a partir de una carpeta vacía](#case-334) | Demo |
| 335 | [Manipulación con dos brazos en RoboDojo](#case-335) | Benchmark |
| 336 | [Una fuente en movimiento](#case-336) | Demo |
| 337 | [Sincronización labial por fotogramas con Higgsfield](#case-337) | Integration |
| 338 | [Prototipo de conducción en mundo abierto](#case-338) | Demo |
| 339 | [París en 1940 con imágenes de referencia](#case-339) | Integration |
| 340 | [Fable planifica un corto renderizado por Opus](#case-340) | Integration |
| 341 | [Un experimento de videoclip](#case-341) | Demo |
| 342 | [Retrato pintado de Dario Amodei](#case-342) | Demo |
| 343 | [Spud Smash con esfuerzo Medium](#case-343) | Demo |
| 344 | [Catedral de hielo con Fable y Opus](#case-344) | Evaluation |
| 345 | [Canto con tractos vocales simulados](#case-345) | Demo |
| 346 | [Tres pruebas de vóxeles en Estambul](#case-346) | Evaluation |
| 347 | [Proyectos completados en el Remote Labor Index](#case-347) | Benchmark |
| 348 | [Un iceberg con cuatro niveles de esfuerzo](#case-348) | Evaluation |
| 349 | [Un corto de anime de setenta y nueve segundos](#case-349) | Demo |
| 350 | [Conjuntos mecánicos con Fable y Opus](#case-350) | Evaluation |
| 351 | [Una mano robótica sube una escalera de caracol](#case-351) | Demo |
| 352 | [Rigging de una malla de Tripo en Blender](#case-352) | Evaluation |
| 353 | [Inventos interactivos del cuaderno de Da Vinci](#case-353) | Demo |
| 354 | [Un estudio de producción musical manejado por Claude](#case-354) | Demo |
| 355 | [Una Raspberry Pi 5 animada](#case-355) | Demo |
| 356 | [Una escena del norte de Italia](#case-356) | Demo |
| 357 | [Libro desplegable con agentes de construcción locales](#case-357) | Evaluation |
| 358 | [Regreso de la prueba de la lámpara de lava](#case-358) | Evaluation |
| 359 | [Un avión a reacción detallado en Blender](#case-359) | Integration |
| 360 | [Viaje con portales entre cientos de mundos](#case-360) | Demo |
| 361 | [Un bazar de Bombay en seis planos con Three.js](#case-361) | Integration |
| 362 | [Un restaurante fotorrealista hecho con código](#case-362) | Integration |
| 363 | [Un modelo de robot en Blender](#case-363) | Demo |
| 364 | [Vídeo animado para explicar Convex](#case-364) | Demo |
| 365 | [Colección de páginas de aterrizaje hechas con un solo prompt](#case-365) | Demo |
| 366 | [Una sonata para piano escrita en LilyPond](#case-366) | Demo |
| 367 | [Un encargo de vídeo sin restricciones](#case-367) | Demo |
| 368 | [Fable planifica, DeepSeek implementa y Opus revisa](#case-368) | Integration |
| 369 | [Fable 5.2 en AI Village](#case-369) | Integration |
| 370 | [Diseño de frontend con y sin skills](#case-370) | Evaluation |
| 371 | [Cómo detectar máquinas de estados implícitas](#case-371) | Tutorial |
| 372 | [Un juego creado desde cero en ocho horas](#case-372) | Demo |
| 373 | [Prototipo de Fishslop y coste en tokens](#case-373) | Evaluation |
| 374 | [Un juego de fútbol americano en movimiento](#case-374) | Demo |
| 375 | [Combate de jefe en mundo abierto con Higgsfield MCP](#case-375) | Integration |
| 376 | [Mont Saint-Michel y sus mareas](#case-376) | Demo |
| 377 | [Un recurso para Roblox en Blender](#case-377) | Demo |
| 378 | [Razonamiento sin mostrar la cadena de pensamiento](#case-378) | Benchmark |
| 379 | [Versiones de Chrome Dino con cuatro modelos](#case-379) | Evaluation |
| 380 | [Damas con un brazo robótico](#case-380) | Demo |
| 381 | [Un clip de motion graphics de quince segundos](#case-381) | Demo |
| 382 | [Una torre Eiffel jugable](#case-382) | Demo |
| 383 | [Carreras en alta mar con Three.js y Higgsfield](#case-383) | Integration |
| 384 | [Simulación de miel en tiempo real con WebGL](#case-384) | Demo |
| 385 | [Efectos visuales programados sobre vídeo](#case-385) | Demo |
| 386 | [Explicación animada del nivel de búsqueda en GTA](#case-386) | Demo |
| 387 | [Un mundo MMO estilizado mediante código](#case-387) | Demo |
| 388 | [Una escena 3D con Fable y Opus](#case-388) | Evaluation |
| 389 | [Texto redundante en una pantalla de pausa](#case-389) | Limit |
| 390 | [Tableros de inspiración con Krea](#case-390) | Integration |
| 391 | [Pruebas de un shooter con portales en la oficina](#case-391) | Demo |
| 392 | [Pieza de superficie rígida detallada en Blender](#case-392) | Demo |
| 393 | [Pruebas de frontend en paralelo con distintos niveles de esfuerzo](#case-393) | Evaluation |
| 394 | [Un juego pequeño en diez prompts](#case-394) | Demo |
| 395 | [Animación fotograma a fotograma en JavaScript](#case-395) | Demo |
| 396 | [De vídeo de referencia a animación 3D](#case-396) | Demo |
| 397 | [Hoguera en pixel art con Fable y Opus](#case-397) | Evaluation |
| 398 | [Arena WebDev con esfuerzo xHigh](#case-398) | Benchmark |
| 399 | [Tipografía de tráiler con dos modelos](#case-399) | Evaluation |
| 400 | [Pruebas de motion design y portafolio 3D con un solo prompt](#case-400) | Evaluation |
| 401 | [Explicación explorable de un reactor nuclear](#case-401) | Demo |
| 402 | [Agentes en Blood on the Clocktower](#case-402) | Benchmark |
| 403 | [Prototipo de carreras de pods](#case-403) | Demo |
| 404 | [Anuncio de ropa interior de Claude en diez segundos](#case-404) | Demo |
| 405 | [Un pájaro al amanecer, trazo a trazo](#case-405) | Demo |
| 406 | [Una ejecución gráfica prolongada en Devin](#case-406) | Evaluation |
| 407 | [Arte pintado con código por tres modelos](#case-407) | Evaluation |
| 408 | [La historia de la escritura en movimiento](#case-408) | Demo |
| 409 | [Banco de pruebas para máquinas de juego](#case-409) | Demo |
| 410 | [PCB para una consola portátil Linux](#case-410) | Evaluation |
| 411 | [Un lago de vóxeles](#case-411) | Demo |
| 412 | [Las 17 generaciones interactivas de Arena](#case-412) | Demo |
| 413 | [Vuelo con un dragón amistoso](#case-413) | Demo |
| 414 | [Orca de gelatina con Fable y Opus](#case-414) | Evaluation |
| 415 | [Prueba abierta de calidad de vídeo](#case-415) | Demo |
| 416 | [Hábitat espacial de inspiración mediterránea](#case-416) | Demo |
| 417 | [Benchmark AA-3D de experiencias interactivas](#case-417) | Benchmark |
| 418 | [Un desafío cronometrado con un personaje esquelético](#case-418) | Demo |
| 419 | [Pixel art con Fable y Astra](#case-419) | Evaluation |
| 420 | [Reel de portafolio de diseño en movimiento](#case-420) | Demo |
| 421 | [Renderizado de una piscina de cristal con dos modelos](#case-421) | Evaluation |
| 422 | [Precisión de llamadas a herramientas en TS-Bench](#case-422) | Benchmark |
| 423 | [Machu Picchu en miniatura](#case-423) | Demo |
| 424 | [GDPx por categoría de trabajo profesional](#case-424) | Benchmark |
| 425 | [Un retrato en una aplicación de dibujo](#case-425) | Demo |
| 426 | [VulcanBench Frontier v4 con esfuerzo Low](#case-426) | Benchmark |
| 427 | [Cambio de papeles en un Backrooms jugable](#case-427) | Demo |
| 428 | [Bugatti Tourbillon en Blender](#case-428) | Demo |
| 429 | [Un vídeo sobre ordenadores creado con dos modelos](#case-429) | Demo |
| 430 | [Un videoclip sobre megakernels](#case-430) | Demo |
| 431 | [Recorrido de un estudio a partir de fotografías](#case-431) | Demo |
| 432 | [Un anuncio de juguetes de los noventa hecho con código](#case-432) | Demo |
| 433 | [Una escena de juego en tercera persona con Three.js](#case-433) | Demo |
| 434 | [Bryceball a partir de un renderizador existente](#case-434) | Demo |
| 435 | [Edición recursiva de vídeo con Fable](#case-435) | Demo |
| 436 | [Una historia cinematográfica de la ciencia](#case-436) | Demo |
| 437 | [Máquina voladora de Da Vinci en 3D](#case-437) | Integration |
| 438 | [Trazado de una PCB a partir de un encargo](#case-438) | Demo |
| 439 | [Un mismo prompt en dos entornos de ejecución](#case-439) | Evaluation |
| 440 | [Ilustración de Godzilla dibujada con código](#case-440) | Demo |
| 441 | [Ventilador de mano diseñado para impresión 3D](#case-441) | Demo |
| 442 | [Búsqueda de errores en un plugin frente a Opus](#case-442) | Evaluation |
| 443 | [Estambul reconstruida como escena 3D](#case-443) | Demo |
| 444 | [Una película en Blender con una pantalla funcional](#case-444) | Demo |
| 445 | [Una transición de agujeros negros con acoplamiento débil](#case-445) | Evaluation |
| 446 | [El límite de una cota del bootstrap modular](#case-446) | Evaluation |
| 447 | [Vercel AI Gateway con modelos de respaldo ordenados](#case-447) | Integration |
| 448 | [Subagentes anidados y presupuesto de revisión](#case-448) | Limit |
| 449 | [Comparación de conversión de un diseño LCARS a HTML](#case-449) | Evaluation |
| 450 | [Optimización para GPU de Quantum ESPRESSO](#case-450) | Benchmark |
| 451 | [Índice de inteligencia de Artificial Analysis por nivel de esfuerzo](#case-451) | Benchmark |
| 452 | [Falsos positivos al revisar cambios con esfuerzo High](#case-452) | Limit |
| 453 | [Treinta tareas habituales de programación](#case-453) | Evaluation |
| 454 | [Salvapantallas de un náufrago en una isla](#case-454) | Demo |
| 455 | [Tres juegos de navegador con esfuerzo High](#case-455) | Evaluation |
| 456 | [Guiones de pódcast sobre libros, capítulo a capítulo](#case-456) | Evaluation |
| 457 | [Un servicio de producción migrado a Rust](#case-457) | Evaluation |
| 458 | [Elegir Fable 5.2 en GitHub Copilot](#case-458) | Integration |
| 459 | [Reto de diseño de cien páginas HTML](#case-459) | Evaluation |
| 460 | [Deriva de requisitos en un compilador](#case-460) | Limit |
| 461 | [Seguir una tarea larga de Fable con Opus](#case-461) | Integration |
| 462 | [Revisión de código con una mirada nueva](#case-462) | Tutorial |
| 463 | [Pérdida de contexto al revisar el diseño de una función](#case-463) | Limit |
| 464 | [Comparación de un Breakout al estilo DX Ball](#case-464) | Evaluation |
| 465 | [Una prueba de mejora de una aplicación 3D](#case-465) | Evaluation |
| 466 | [Juego del ratón y el gato con tres modelos](#case-466) | Evaluation |
| 467 | [Coste y puntuación en AIBenchy con esfuerzo High](#case-467) | Benchmark |
| 468 | [Ajustar el entorno de agentes de Fable 5.2](#case-468) | Tutorial |
| 469 | [Una aplicación para previsualizar personajes animados](#case-469) | Demo |
| 470 | [Prueba de un código QR generado sin herramientas](#case-470) | Evaluation |
| 471 | [Un juego de zombis en Unity con Tripo](#case-471) | Demo |
| 472 | [Una calle nevada pintada en MS Paint](#case-472) | Demo |
| 473 | [Un enchufe sin conectar en Wojak-Bench](#case-473) | Limit |
| 474 | [Un arreglo de piano para un videojuego rítmico](#case-474) | Evaluation |
| 475 | [Rediseño de la recuperación de tokens en Picnic](#case-475) | Demo |
| 476 | [Montaje de una apertura de anime con clips generados](#case-476) | Tutorial |
| 477 | [Animación de un personaje con tres herramientas](#case-477) | Demo |
| 478 | [Un tráiler urbano renderizado con scripts de Blender](#case-478) | Demo |
| 479 | [Escenas nocturnas dibujadas con JavaScript](#case-479) | Demo |
| 480 | [De modelos CAD a planos técnicos](#case-480) | Demo |
| 481 | [Las 43 tareas de la prueba de análisis de Plotly](#case-481) | Benchmark |
| 482 | [Una estación SGI Indy recreada como sitio web](#case-482) | Demo |
| 483 | [Coordinación de agentes mediante incidencias y worktrees](#case-483) | Integration |
| 484 | [Verificación de citas con procesos en segundo plano](#case-484) | Integration |
| 485 | [Depuración de un modelo de tarifas de flete de ida y vuelta](#case-485) | Limit |
| 486 | [Adaptación de la inferencia de Edge0 a Mac](#case-486) | Integration |
| 487 | [Revisión de placas de circuito de alta densidad](#case-487) | Limit |
| 488 | [Rastreo de una cita en un periódico de pago](#case-488) | Limit |
| 489 | [Planificación con Fable y revisión de los cambios de Opus](#case-489) | Tutorial |

<a id="fable-5-2-cases"></a>
## Casos de uso

<a id="case-330"></a>
### Case 330: [Un MacBook en SVG con distintos niveles de esfuerzo](https://playcode.io/blog/macbook-svg-benchmark#compare) (por [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**Compara calidad de dibujo, tokens y límites de salida con un mismo encargo.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode señala que Fable 5.2 High usó 76 158 tokens por 3,05 USD. Xhigh y Max llegaron al límite de 128 000 tokens en streaming sin producir un dibujo. Ambos terminaron con más margen mediante Batch API. La clasificación refleja el criterio visual del editor.

[Material relacionado 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [Un juego de lucha para cuatro a partir de dibujos familiares](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (por [Lex](https://notesbylex.com/))

**Da al agente bocetos, un prototipo existente y requisitos concretos de control.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex usó Claude Code para transformar un juego de desplazamiento lateral en un beat ’em up de 12 niveles y 18 personajes. Usó herramientas de imagen y audio para los recursos. En las pruebas familiares funcionaron cuatro mandos.

[Material relacionado 1](https://aidens-revenge.pages.dev/) · [Material relacionado 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [Material relacionado 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [Tres dispositivos electrónicos, del diseño al montaje](https://www.anthropic.com/research/claude-electronics-design) (por [@Anthropic](https://www.anthropic.com/))

**Comprueba el circuito, la carcasa y el firmware como un solo sistema.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ Reproducir video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic y Diode describen tres dispositivos funcionales. Fable 5.2 trazó las placas, modeló las carcasas, escribió el software y guio las pruebas posteriores a la fabricación.

[Material relacionado 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [Material relacionado 2](https://www.youtube.com/watch?v=vdYynH177h0) · [Material relacionado 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [Formalización del último teorema de Fermat en Lean](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (por [@Anthropic](https://www.anthropic.com/))

**Usa un verificador de pruebas y enunciados intermedios como hitos.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Anthropic afirma que 1000 agentes de Fable 5.2 formalizaron la demostración existente en 30 horas. Con la misma configuración de equipo, Opus 5.5 alcanzó el 26 % en 18 horas.

[Material relacionado 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [Material relacionado 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [Un sistema operativo a partir de una carpeta vacía](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (por [@Anthropic](https://www.anthropic.com/))

**Comprueba por separado el arranque, los controladores, el almacenamiento y la instalación.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ Reproducir video</a>

Anthropic afirma que Fable 5.2 coordinó más de 1000 subagentes durante ocho días para crear un prototipo de sistema operativo que arrancó en un portátil.

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [Manipulación con dos brazos en RoboDojo](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (por [@Anthropic](https://www.anthropic.com/))

**Compara los modelos en las mismas tareas simuladas de manipulación.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ Reproducir video</a>

Anthropic publicó un 64,9 % para Fable 5.2 frente al 27,6 % de Fable 5.1 en RoboDojo. El anuncio incluye una demostración robótica.

[Material relacionado 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [Una fuente en movimiento](https://x.com/Angaisb_/status/2119909059277238733) (por [@Angaisb_](https://x.com/Angaisb_))

**Usa el flujo continuo de agua para evaluar el ritmo visual.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

El autor comparte una escena de una fuente atribuida a Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [Sincronización labial por fotogramas con Higgsfield](https://x.com/higgsfield_ai/status/2119909938969580024) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Ajusta los tiempos por fotograma antes de revisar el clip.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ Reproducir video</a>

Higgsfield señala que en su flujo con Fable 5.2 siguió el movimiento de la boca y sincronizó el audio con los fotogramas.

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [Prototipo de conducción en mundo abierto](https://x.com/ericmaskfr/status/2119910195325481026) (por [@ericmaskfr](https://x.com/ericmaskfr))

**Prueba un encargo breve de mundo abierto en una sección jugable.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un juego inspirado en GTA y señala que completó la ejecución en unas 2 h 14 min.

Prompt original

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [París en 1940 con imágenes de referencia](https://x.com/higgsfield_ai/status/2119910344998912507) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Separa la generación de referencias del código de la escena.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ Reproducir video</a>

Higgsfield aportó las referencias mediante su MCP y usó Fable 5.2 para una escena en Three.js.

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable planifica un corto renderizado por Opus](https://x.com/kloss_xyz/status/2119910613828980846) (por [@kloss_xyz](https://x.com/kloss_xyz))

**Separa la planificación de la ejecución del vídeo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ Reproducir video</a>

Fable 5.2 redactó el encargo y el plan. Opus 5.5 creó una animación de 16 segundos con Blender y Python y sintetizó la música.

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [Un experimento de videoclip](https://x.com/WesRoth/status/2119911161386934330) (por [@WesRoth](https://x.com/WesRoth))

**Revisa tanto la letra como la secuencia generada.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un videoclip hecho con Fable 5.2 y comenta su letra.

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Retrato pintado de Dario Amodei](https://x.com/Mr_Salio/status/2119911922577637543) (por [@Mr_Salio](https://x.com/Mr_Salio))

**Compara el retrato estilizado con la referencia que aparece a su lado.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un retrato de Dario Amodei atribuido a Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [Spud Smash con esfuerzo Medium](https://x.com/argofowl/status/2119913148929187960) (por [@argofowl](https://x.com/argofowl))

**Da al prototipo acciones y un objetivo claros.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un personaje patata que golpea, cabecea o quema sillas azules.

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Catedral de hielo con Fable y Opus](https://x.com/QQTeng/status/2119913518015435103) (por [@QQTeng](https://x.com/QQTeng))

**Compara tiempo y coste al generar la misma escena.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ Reproducir video</a>

El autor indica unas 1 h 57 min y 81,10 USD para Fable, frente a unas 3 h 11 min y 45,97 USD para Opus.

Prompt original

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [Canto con tractos vocales simulados](https://x.com/banteg/status/2119914098171199996) (por [@banteg](https://x.com/banteg))

**Usa un modelo físico de la voz como entrada de producción musical.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una versión creada con dos tractos vocales simulados de Chimera y una mezcla con vocoder.

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [Tres pruebas de vóxeles en Estambul](https://x.com/Avenoxai/status/2119914308603953485) (por [@Avenoxai](https://x.com/Avenoxai))

**Compara una demolición, un reloj funcional y un mapa.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte tres pruebas de un solo prompt y les asigna 100, 100 y 95,6 puntos según su propia rúbrica.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Proyectos completados en el Remote Labor Index](https://x.com/ScaleAILabs/status/2119914701736075489) (por [@ScaleAILabs](https://x.com/ScaleAILabs))

**Interpreta la tasa en función de los proyectos evaluados.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ Reproducir video</a>

Scale Labs y CAIS indican que Fable 5.2 completó satisfactoriamente el 41,3 % de los proyectos evaluados de trabajo remoto.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [Un iceberg con cuatro niveles de esfuerzo](https://x.com/0xRhinoX/status/2119915121698840587) (por [@0xRhinoX](https://x.com/0xRhinoX))

**Compara la completitud, el coste y los detalles al aumentar el esfuerzo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ Reproducir video</a>

El autor usó el mismo prompt con cuatro niveles. High omitió la aurora y Ultra añadió hielo brillante y una vista submarina.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [Un corto de anime de setenta y nueve segundos](https://x.com/anstapnever/status/2119915123070644263) (por [@anstapnever](https://x.com/anstapnever))

**Examina la continuidad de las escenas en una animación larga.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un clip de anime de 79 segundos atribuido a un flujo de trabajo con Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Conjuntos mecánicos con Fable y Opus](https://x.com/ivanainai/status/2119915243321397550) (por [@ivanainai](https://x.com/ivanainai))

**Compara cómo distribuye cada modelo las piezas del conjunto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ Reproducir video</a>

El autor muestra renders etiquetados de Fable 5.2 y Opus 5.5, con un despiece de una rueda y sus engranajes.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [Una mano robótica sube una escalera de caracol](https://x.com/Luckyballa/status/2119915557663506720) (por [@Luckyballa](https://x.com/Luckyballa))

**Usa un obstáculo simulado para evaluar una locomoción poco habitual.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una prueba con Fable 5.2 y Steel 0.1 en la que una mano Wuji camina sobre sus dedos.

[Material relacionado 1](https://github.com/skild-ai/steel-webgpu/pull/7)

Prompt original

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [Rigging de una malla de Tripo en Blender](https://x.com/0xKense1/status/2119916096098582566) (por [@0xKense1](https://x.com/0xKense1))

**Usa comprobaciones numéricas para el agarre, la textura y la deformación.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ Reproducir video</a>

El autor compara dos rigs creados a partir de recursos de Tripo. Fable generó dos clips en 36 minutos y Opus ocho en unos 21 minutos.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [Inventos interactivos del cuaderno de Da Vinci](https://x.com/alexalbert__/status/2119916954337349737) (por [@alexalbert__](https://x.com/alexalbert__))

**Usa los dibujos originales como referencia para un modelo educativo interactivo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ Reproducir video</a>

Alex Albert proporcionó un PDF del cuaderno de Leonardo y compartió una interpretación interactiva de sus inventos.

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [Un estudio de producción musical manejado por Claude](https://x.com/The_Alex/status/2119917226769985785) (por [@The_Alex](https://x.com/The_Alex))

**Usa una herramienta controlada por un agente para solicitudes de composición recurrentes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una estación de audio digital creada con Fable 5.2 y afirma que Opus la abrió más tarde para componer una canción.

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [Una Raspberry Pi 5 animada](https://x.com/sparklabhq/status/2119917375080521921) (por [@sparklabhq](https://x.com/sparklabhq))

**Usa una animación de producto para inspeccionar sus componentes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una Raspberry Pi 5 animada con Fable 5.2.

Prompt original

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [Una escena del norte de Italia](https://x.com/Angaisb_/status/2119917807119089926) (por [@Angaisb_](https://x.com/Angaisb_))

**Evalúa el paisaje y la atmósfera de un encargo basado en un lugar.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una escena de Fable 5.2 ambientada en el norte de Italia.

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [Libro desplegable con agentes de construcción locales](https://x.com/atomicagent_io/status/2119918110752846094) (por [@atomicagent_io](https://x.com/atomicagent_io))

**Compara la orquestación con la ejecución de un solo modelo en la misma tarea.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ Reproducir video</a>

Atomic indica 2,98 USD y 11 minutos cuando Fable coordina agentes Qwen locales, frente a 15,77 USD y 21 minutos con Fable solo.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [Regreso de la prueba de la lámpara de lava](https://x.com/eidzoku/status/2119918134060601690) (por [@eidzoku](https://x.com/eidzoku))

**Usa la misma tarea visual para comparar varios modelos.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ Reproducir video</a>

El autor recuperó una prueba de lámparas de lava y compartió la comparación visual de los resultados.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [Un avión a reacción detallado en Blender](https://x.com/higgsfield_ai/status/2119918248955392431) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Indica en el encargo el número de piezas, la duración y el aspecto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ Reproducir video</a>

Higgsfield afirma haber creado en Blender un modelo programado de 931 piezas y 24 260 remaches con Fable 5.2 y su MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [Viaje con portales entre cientos de mundos](https://x.com/emollick/status/2119918307457577163) (por [@emollick](https://x.com/emollick))

**Conecta con portales entornos generados por separado.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ Reproducir video</a>

Ethan Mollick señala que 25 000 agentes crearon más de 450 mundos con código y comparte el juego y su repositorio.

[Material relacionado 1](https://portals-endless-worlds.netlify.app/) · [Material relacionado 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [Un bazar de Bombay en seis planos con Three.js](https://x.com/higgsfield_ai/status/2119918834841010320) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Divide el encargo visual en planos con duraciones definidas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ Reproducir video</a>

Higgsfield comparte una secuencia de bazar de 21,5 segundos, con seis planos renderizados en Three.js.

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [Un restaurante fotorrealista hecho con código](https://x.com/higgsfield_ai/status/2119918838490010008) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Usa una escena hecha con código para inspeccionar materiales e iluminación.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ Reproducir video</a>

Higgsfield muestra un restaurante y señala que lo construyó mediante código sin un programa de modelado 3D.

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [Un modelo de robot en Blender](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (por [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Inspecciona las articulaciones y la silueta en una vista giratoria.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ Reproducir video</a>

El autor muestra un pequeño robot mecánico construido en una demostración de Blender con Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [Vídeo animado para explicar Convex](https://x.com/Rasmic/status/2119919466163093768) (por [@Rasmic](https://x.com/Rasmic))

**Explica un producto para desarrolladores con una animación breve.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una explicación animada de Convex hecha con Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [Colección de páginas de aterrizaje hechas con un solo prompt](https://x.com/daradoescode/status/2119919529807466594) (por [@daradoescode](https://x.com/daradoescode))

**Compara jerarquía y distribución visual en varios encargos breves.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un vídeo que reúne páginas de aterrizaje creadas con Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [Una sonata para piano escrita en LilyPond](https://x.com/imjustnewatai/status/2119919644836347926) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Mantén la partitura vinculada al vídeo renderizado.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ Reproducir video</a>

El autor pidió un movimiento al estilo de Beethoven e indica que las notas mostradas provienen del archivo LilyPond.

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [Un encargo de vídeo sin restricciones](https://x.com/aollivier82/status/2119920990893244510) (por [@aollivier82](https://x.com/aollivier82))

**Usa un encargo visual abierto para conocer las preferencias creativas del modelo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte el resultado de pedir a Fable 5.2 que hiciera el vídeo más bello que pudiera.

Prompt original

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable planifica, DeepSeek implementa y Opus revisa](https://x.com/ivanfioravanti/status/2119921810267636201) (por [@ivanfioravanti](https://x.com/ivanfioravanti))

**Separa coordinación, implementación y revisión entre agentes.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ Reproducir video</a>

El autor muestra cómo Fable usa herdr para coordinar cuatro agentes DeepSeek V4.1 Flash, mientras Opus 5.5 revisa las pull requests.

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [Fable 5.2 en AI Village](https://x.com/aidigest_/status/2119923190411719158) (por [@aidigest_](https://x.com/aidigest_))

**Revisa por separado la respuesta del agente y sus acciones sobre la memoria.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

El registro público muestra que Fable aceptó revisar su memoria más adelante a petición de otro agente. Una publicación relacionada muestra una prueba de afinidad con personajes.

[Material relacionado 1](https://x.com/aidigest_/status/2119923209311260707) · [Material relacionado 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [Diseño de frontend con y sin skills](https://x.com/AdamHoltererer/status/2119924849321914653) (por [@AdamHoltererer](https://x.com/AdamHoltererer))

**Mantén fijo el modelo y varía la configuración de skills.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

El autor muestra dos resultados de frontend con Fable 5.2, uno con skills y otro sin ellas.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [Cómo detectar máquinas de estados implícitas](https://x.com/kunchenguid/status/2119924895060795492) (por [@kunchenguid](https://x.com/kunchenguid))

**Audita un módulo concreto y pide diagramas del antes y el después.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

El autor muestra una mejora del repositorio Firstmate y publica el prompt exacto de auditoría.

[Material relacionado 1](https://github.com/kunchenguid/lavish-axi)

Prompt original

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [Un juego creado desde cero en ocho horas](https://x.com/felixrieseberg/status/2119925633564463609) (por [@felixrieseberg](https://x.com/felixrieseberg))

**Registra las entradas en caché, los recursos generados y el tiempo real.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ Reproducir video</a>

El ingeniero de Anthropic afirma haber generado modelos, sonidos y texturas en una ejecución equivalente a unos 550 USD en API.

[Material relacionado 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [Material relacionado 2](https://x.com/AndrewCurran_/status/2119953960794780133)

Prompt original

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Prototipo de Fishslop y coste en tokens](https://x.com/theo/status/2119926277801144695) (por [@theo](https://x.com/theo))

**Compara una versión del juego con el resultado de otro modelo.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ Reproducir video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

El autor señala 76 minutos y unos 42 USD en tokens y compara el resultado con Opus 5.5.

[Material relacionado 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [Un juego de fútbol americano en movimiento](https://x.com/WesRoth/status/2119926801514529027) (por [@WesRoth](https://x.com/WesRoth))

**Prueba los avisos de juego y de puntuación en un prototipo deportivo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un juego de Fable 5.2 que indica en pantalla cuándo se anota.

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [Combate de jefe en mundo abierto con Higgsfield MCP](https://x.com/higgsfield_ai/status/2119926932343324795) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Distingue el juego ejecutable de sus cinemáticas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ Reproducir video</a>

Higgsfield describe un juego de navegador con mundo abierto, un combate de jefe en tres actos y cinemáticas hechas con Fable 5.2 y su MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [Mont Saint-Michel y sus mareas](https://x.com/loktar00/status/2119927152489472076) (por [@loktar00](https://x.com/loktar00))

**Prueba niveles de agua cambiantes en una pequeña escena histórica.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una miniatura de Mont Saint-Michel con mareas animadas.

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [Un recurso para Roblox en Blender](https://x.com/hiyouwhatsapp/status/2119927163264573642) (por [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**Revisa el recurso en Blender antes de importarlo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un resultado de Blender para Roblox obtenido casi con un único prompt.

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [Razonamiento sin mostrar la cadena de pensamiento](https://x.com/Tim_Hua_/status/2119927284761293089) (por [@Tim_Hua_](https://x.com/Tim_Hua_))

**Evalúa las respuestas con la misma restricción de salida.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

El evaluador hizo pruebas de razonamiento y conocimiento sin salida de cadena de pensamiento y sitúa a Fable 5.2 ligeramente por debajo de GPT-6.1 Sol.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [Versiones de Chrome Dino con cuatro modelos](https://x.com/noclipepe/status/2119927838321328577) (por [@noclipepe](https://x.com/noclipepe))

**Compara la duración y el coste en un encargo de juego recurrente.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ Reproducir video</a>

El autor añade Fable 5.2 a una prueba previa del T-Rex con Opus, Gemini y Astra y presenta los resultados juntos.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [Damas con un brazo robótico](https://x.com/karolina_dubiel/status/2119928342115676576) (por [@karolina_dubiel](https://x.com/karolina_dubiel))

**Lee las posiciones articulares y repite los agarres fallidos.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ Reproducir video</a>

El autor indica que el modelo corrigió un descenso de unos 7 mm y reintentó movimientos fallidos a partir de la retroalimentación.

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [Un clip de motion graphics de quince segundos](https://x.com/aziz4ai/status/2119928581405200726) (por [@aziz4ai](https://x.com/aziz4ai))

**Registra la cuota que consume una prueba de animación con código.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una escena de 15 segundos hecha con código y afirma haber usado el 4 % de su cuota semanal.

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [Una torre Eiffel jugable](https://x.com/bobyau/status/2119928812628771212) (por [@bobyau](https://x.com/bobyau))

**Comprueba si el modelo de un monumento permite interactuar con él.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una demostración de la torre Eiffel y señala que la creó en 25 minutos.

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [Carreras en alta mar con Three.js y Higgsfield](https://x.com/higgsfield_ai/status/2119928918035910668) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Separa la lógica de juego de las herramientas multimedia.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ Reproducir video</a>

Higgsfield muestra un juego de carreras con grandes olas, cinco rivales de IA y cohetes teledirigidos.

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [Simulación de miel en tiempo real con WebGL](https://x.com/deedydas/status/2119930300990177509) (por [@deedydas](https://x.com/deedydas))

**Usa una simulación física en el navegador para evaluar el movimiento del material.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ Reproducir video</a>

El autor muestra una simulación de miel en WebGL en tiempo real y publica el encargo breve original.

Prompt original

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [Efectos visuales programados sobre vídeo](https://x.com/ashebytes/status/2119930763105931649) (por [@ashebytes](https://x.com/ashebytes))

**Revisa los tiempos y la posición de los efectos sobre el metraje original.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una prueba de efectos visuales de Fable 5.2 con gráficos animados superpuestos sobre vídeo real.

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [Explicación animada del nivel de búsqueda en GTA](https://x.com/saimagnate/status/2119931563760632311) (por [@saimagnate](https://x.com/saimagnate))

**Combina escenas del juego y diagramas para explicar una mecánica.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ Reproducir video</a>

El creador atribuye el resultado a una sola petición a Fable 5.2. El video usa escenas del juego y diagramas para comparar los sistemas de búsqueda de GTA V y RDR2.

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [Un mundo MMO estilizado mediante código](https://x.com/Izkimar/status/2119931740940640542) (por [@Izkimar](https://x.com/Izkimar))

**Evalúa la coherencia del mundo a través de sus recursos estilizados.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ Reproducir video</a>

El autor afirma haber creado en un día el mundo MMO mostrado, con recursos generados mediante código.

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [Una escena 3D con Fable y Opus](https://x.com/dom_scholz/status/2119933150025363661) (por [@dom_scholz](https://x.com/dom_scholz))

**Compara en una misma vista el tiempo de preparación y el nivel de detalle.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte los renders de Fable 5.2 y Opus 5.5 e indica que Fable terminó antes.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [Texto redundante en una pantalla de pausa](https://x.com/AndrewPrifer/status/2119934600608915465) (por [@AndrewPrifer](https://x.com/AndrewPrifer))

**Revisa si los textos generados repiten explicaciones.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

El desarrollador usa una pantalla de pausa para mostrar que Fable 5.2 redactó más explicaciones de las necesarias.

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [Tableros de inspiración con Krea](https://x.com/lambdacalcc/status/2119934725662060663) (por [@lambdacalcc](https://x.com/lambdacalcc))

**Compara conceptos antes de elegir una dirección visual.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

El autor comparte cuatro resultados de una sesión de moodboards con Fable 5.2 en un entorno de Krea.

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [Pruebas de un shooter con portales en la oficina](https://x.com/_sholtodouglas/status/2119935331499925557) (por [@_sholtodouglas](https://x.com/_sholtodouglas))

**Evalúa el juego generado con partidas multijugador.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ Reproducir video</a>

Un ingeniero de Anthropic comparte un FPS de arena con portales y describe las partidas de prueba en la oficina.

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Pieza de superficie rígida detallada en Blender](https://x.com/ziwenxu_/status/2119937420280168929) (por [@ziwenxu_](https://x.com/ziwenxu_))

**Inspecciona la topología y la silueta en la vista de Blender.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una pieza de superficie rígida presentada como resultado de Fable 5.2 en Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [Pruebas de frontend en paralelo con distintos niveles de esfuerzo](https://x.com/AI_masaou/status/2119937635322085640) (por [@AI_masaou](https://x.com/AI_masaou))

**Compara encargos sencillos y ambiciosos con varios niveles de esfuerzo.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

El autor describe resultados parecidos en tareas sencillas, más detalles en las producciones grandes de Fable y un salto pronunciado de tiempo y tokens entre Medium y High.

[Material relacionado 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [Un juego pequeño en diez prompts](https://x.com/AmirMushich/status/2119937977426338283) (por [@AmirMushich](https://x.com/AmirMushich))

**Registra las iteraciones y el tamaño del juego.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ Reproducir video</a>

El autor indica que el juego pesa 220 KB y contiene unas 3400 líneas; comparte el código y el metraje.

[Material relacionado 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [Animación fotograma a fotograma en JavaScript](https://x.com/kevin_t_ngo/status/2119938129079808282) (por [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Inspecciona una secuencia cuyos fotogramas se dibujan mediante código.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte la animación e indica que JavaScript dibujó cada fotograma.

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [De vídeo de referencia a animación 3D](https://x.com/KHvostikk/status/2119939061049889130) (por [@KHvostikk](https://x.com/KHvostikk))

**Usa el metraje de referencia para evaluar una escena reconstruida.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una demostración de conversión de vídeo a animación 3D con Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Hoguera en pixel art con Fable y Opus](https://x.com/GrilliotTodd/status/2119939651385655692) (por [@GrilliotTodd](https://x.com/GrilliotTodd))

**Compara iluminación y siluetas sobre un mismo tema.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ Reproducir video</a>

Las imágenes en paralelo muestran una hoguera interpretada por Fable 5.2 y Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [Arena WebDev con esfuerzo xHigh](https://x.com/arena/status/2119941204003770690) (por [@arena](https://x.com/arena))

**Compara el nivel de esfuerzo concreto usado en la clasificación.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena publicó un debut de 1832 puntos para Claude Fable 5.2 xHigh en Code Arena WebDev.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [Tipografía de tráiler con dos modelos](https://x.com/muku_sns/status/2119941490969624679) (por [@muku_sns](https://x.com/muku_sns))

**Compara dos interpretaciones de un mismo párrafo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ Reproducir video</a>

El autor presenta los títulos de Opus y Fable en paralelo. La versión de Fable incorpora un borde rojo y títulos censurados.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [Pruebas de motion design y portafolio 3D con un solo prompt](https://x.com/Khazix0918/status/2119941585538572390) (por [@Khazix0918](https://x.com/Khazix0918))

**Evalúa investigación, diseño y renderizado por separado.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ Reproducir video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ Reproducir video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ Reproducir video</a></td></tr></table>

El autor comparte cuatro ejecuciones: una pieza por el aniversario de ChatGPT, una explicación de DeepSeek, una escena en Three.js y una recreación 3D de Apple Jing’an.

[Material relacionado 1](https://x.com/Khazix0918/article/2119941585538572390)

Prompt original

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [Explicación explorable de un reactor nuclear](https://x.com/konstantinsaifo/status/2119941967136379334) (por [@konstantinsaifo](https://x.com/konstantinsaifo))

**Usa una función de desmontaje para mostrar cómo encajan las piezas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ Reproducir video</a>

El autor pidió un reactor desmontable en Three.js y señala un gasto de 92 USD en API.

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Agentes en Blood on the Clocktower](https://x.com/dwarkesh_sp/status/2119942657812451482) (por [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**Compara modelos en el mismo juego de roles ocultos.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

El evaluador sitúa a Fable 5.2 por encima de Fable 5.1 y Opus 5.5, y a GPT-6 Astra por delante de todos ellos.

[Material relacionado 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [Prototipo de carreras de pods](https://x.com/loktar00/status/2119943124965638444) (por [@loktar00](https://x.com/loktar00))

**Usa un formato de carrera conocido para evaluar movimiento y control.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un resultado de Fable 5.2 inspirado en las carreras de pods.

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [Anuncio de ropa interior de Claude en diez segundos](https://x.com/Masimo_Blue/status/2119943368612487285) (por [@Masimo_Blue](https://x.com/Masimo_Blue))

**Prueba un encargo de producto abierto con música original.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ Reproducir video</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

El autor comparte un anuncio de diez segundos con música acid techno y las imágenes de producto proporcionadas.

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [Un pájaro al amanecer, trazo a trazo](https://x.com/mgrczyk/status/2119943813028548721) (por [@mgrczyk](https://x.com/mgrczyk))

**Desactiva la opción de deshacer para observar decisiones de dibujo consecutivas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ Reproducir video</a>

El autor muestra un pájaro pintado al amanecer en un entorno que impedía modificar los trazos anteriores.

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [Una ejecución gráfica prolongada en Devin](https://x.com/Da7_Tech/status/2119944847255896490) (por [@Da7_Tech](https://x.com/Da7_Tech))

**Registra la duración y el coste de un render exigente.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ Reproducir video</a>

Un embajador declarado de Cognition comparte una ejecución de Devin Max que, según indica, tomó unas 3,5 horas y costó 82 USD.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [Arte pintado con código por tres modelos](https://x.com/kickingkeys/status/2119945841997672698) (por [@kickingkeys](https://x.com/kickingkeys))

**Compara el movimiento del dibujo y el sonido sintetizado entre ejecuciones.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una pintura hecha con código y audio y describe pruebas con el mismo prompt en Fable 5.2, Fable 5.1 y Gemini 4 Argon.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [La historia de la escritura en movimiento](https://x.com/rileybrown/status/2119946022767980985) (por [@rileybrown](https://x.com/rileybrown))

**Usa una cronología para estructurar una explicación animada con código.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ Reproducir video</a>

El autor muestra una animación sobre la historia de la escritura y afirma que la creó con un único prompt.

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [Banco de pruebas para máquinas de juego](https://x.com/techartist_/status/2119946891106394518) (por [@techartist_](https://x.com/techartist_))

**Prueba mecánicas, física y efectos en una misma escena.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ Reproducir video</a>

El autor construyó un entorno de ensayo para cuatro conceptos con Three.js y Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [PCB para una consola portátil Linux](https://x.com/seveibar/status/2119947341230907453) (por [@seveibar](https://x.com/seveibar))

**Compara dos modelos con el mismo encargo de circuito.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ Reproducir video</a>

El creador de tscircuit muestra un ensayo de diseño de una consola portátil Linux con Astra 6 High y Fable 5.2 High.

Prompt original

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [Un lago de vóxeles](https://x.com/Angaisb_/status/2119947748690841841) (por [@Angaisb_](https://x.com/Angaisb_))

**Usa una escena pequeña para evaluar la composición.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un lago de vóxeles atribuido a Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [Las 17 generaciones interactivas de Arena](https://x.com/arena/status/2119948067449536733) (por [@arena](https://x.com/arena))

**Explora varios tipos de resultados antes de elegir una prueba.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ Reproducir video</a>

Arena comparte 17 generaciones, entre ellas mundos 3D, juegos, interfaces, visualizaciones y animaciones hechas con código.

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [Vuelo con un dragón amistoso](https://x.com/chetanankola/status/2119951015407738913) (por [@chetanankola](https://x.com/chetanankola))

**Usa un ciclo de vuelo para probar la cámara y el movimiento.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte una escena de un dragón con Three.js y Blender y describe mejoras hechas con Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Orca de gelatina con Fable y Opus](https://x.com/vib3coded/status/2119951060752375827) (por [@vib3coded](https://x.com/vib3coded))

**Compara la superficie y el movimiento de un mismo objeto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ Reproducir video</a>

El autor muestra en paralelo las orcas de gelatina de Fable 5.2 y Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [Prueba abierta de calidad de vídeo](https://x.com/suna_gaku/status/2119952985933697063) (por [@suna_gaku](https://x.com/suna_gaku))

**Da libertad creativa para observar las decisiones del modelo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ Reproducir video</a>

El autor pidió al modelo que mostrara su mejor trabajo en vídeo y compartió el resultado.

Prompt original

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [Hábitat espacial de inspiración mediterránea](https://x.com/MaxXWilliamson/status/2119953172634677533) (por [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**Combina un encargo breve con las herramientas del proyecto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ Reproducir video</a>

El autor proporcionó herramientas de sus hábitats espaciales anteriores y pidió una estación de inspiración mediterránea.

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [Benchmark AA-3D de experiencias interactivas](https://x.com/ArtificialAnlys/status/2119953570430881946) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Lee el Elo junto con su intervalo de incertidumbre.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ Reproducir video</a>

Artificial Analysis publicó un Elo inicial de 1271 para Fable 5.2 Max en su benchmark de experiencias interactivas 3D.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [Un desafío cronometrado con un personaje esquelético](https://x.com/WesRoth/status/2119953913160093817) (por [@WesRoth](https://x.com/WesRoth))

**Incluye un temporizador visible al evaluar un prototipo jugable.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ Reproducir video</a>

El autor muestra un resultado de Fable 5.2 creado con un solo prompt, con un personaje esquelético y una cuenta atrás en pantalla.

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Pixel art con Fable y Astra](https://x.com/Angaisb_/status/2119955179915137294) (por [@Angaisb_](https://x.com/Angaisb_))

**Compara las formas y los detalles a la misma escala.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ Reproducir video</a>

La comparación original muestra resultados de pixel art de GPT-6 Astra y Fable 5.2.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [Reel de portafolio de diseño en movimiento](https://x.com/Leviwoyun/status/2119955625820258308) (por [@Leviwoyun](https://x.com/Leviwoyun))

**Plantea un encargo abierto con una duración fija.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ Reproducir video</a>

El autor comparte un reel con música y señala un tiempo de producción de 24 minutos.

Prompt original

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [Renderizado de una piscina de cristal con dos modelos](https://x.com/MrTacticalX/status/2119955647542542439) (por [@MrTacticalX](https://x.com/MrTacticalX))

**Compara la iluminación, el tiempo y el coste.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ Reproducir video</a>

El autor indica 90 minutos y 57,87 USD para Fable frente a 68 minutos y 14,39 USD para Opus.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [Precisión de llamadas a herramientas en TS-Bench](https://x.com/gosrum/status/2119956559031927079) (por [@gosrum](https://x.com/gosrum))

**Mide por separado los errores de llamada y el consumo de tokens.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

El evaluador indica que Fable 5.2 no cometió errores al llamar a herramientas y que las tareas sencillas apenas distinguen entre las variantes de Claude.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [Machu Picchu en miniatura](https://x.com/loktar00/status/2119958719362666708) (por [@loktar00](https://x.com/loktar00))

**Inspecciona la atmósfera y los pequeños detalles de una escena en miniatura.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ Reproducir video</a>

La demostración de Machu Picchu incluye niebla volumétrica y pequeñas alpacas.

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [GDPx por categoría de trabajo profesional](https://x.com/SemiAnalysis_/status/2119961447199289640) (por [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**Lee los resultados por subtarea junto a la puntuación total.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

El editor del benchmark informa de una puntuación global del 16,4 % y desglosa áreas como diseño de chips e ingeniería de software.

[Material relacionado 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [Material relacionado 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [Material relacionado 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [Un retrato en una aplicación de dibujo](https://x.com/The_Alex/status/2119964472559489229) (por [@The_Alex](https://x.com/The_Alex))

**Guía el retrato con una miniatura de referencia.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ Reproducir video</a>

El creador pidió a Fable 5.2 que abriera una aplicación de dibujo y lo retratara. El video muestra el proceso desde los contornos hasta el dibujo terminado.

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [VulcanBench Frontier v4 con esfuerzo Low](https://x.com/morganlinton/status/2119966067527467215) (por [@morganlinton](https://x.com/morganlinton))

**Compara generaciones de un modelo con el mismo nivel de esfuerzo.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

El autor del benchmark indica unas 5 frente a 26 minutos por tarea para Fable 5.2 y 5.1, respectivamente, con esfuerzo Low.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [Cambio de papeles en un Backrooms jugable](https://x.com/LexnLin/status/2119966127149429093) (por [@LexnLin](https://x.com/LexnLin))

**Cambia el objetivo del jugador para probar una idea de juego.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ Reproducir video</a>

El jugador controla al monstruo e intenta atrapar personas. El autor comparte un vídeo de la partida y un enlace para jugar.

[Material relacionado 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [Bugatti Tourbillon en Blender](https://x.com/xikhar/status/2119966147328299284) (por [@xikhar](https://x.com/xikhar))

**Usa imágenes de referencia para definir el exterior y el interior.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ Reproducir video</a>

El autor afirma que modeló un Bugatti Tourbillon con su interior y renderizó una secuencia a partir de un prompt y varias referencias.

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [Un vídeo sobre ordenadores creado con dos modelos](https://x.com/daradoescode/status/2119966154391183522) (por [@daradoescode](https://x.com/daradoescode))

**Registra la aportación de cada modelo en un flujo mixto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ Reproducir video</a>

El autor compartió un vídeo estilizado creado con Fable 5.2 y una contribución importante de Opus 5.5.

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [Un videoclip sobre megakernels](https://x.com/elliotarledge/status/2119968762069934415) (por [@elliotarledge](https://x.com/elliotarledge))

**Usa un concepto técnico como tema de un vídeo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ Reproducir video</a>

El autor pidió a Fable 5.2 con esfuerzo High un videoclip sobre megakernels y compartió el resultado.

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [Recorrido de un estudio a partir de fotografías](https://x.com/rpnickson/status/2119969928304357507) (por [@rpnickson](https://x.com/rpnickson))

**Usa fotos reales como referencia para reconstruir una escena.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ Reproducir video</a>

El autor aportó fotos de su estudio, adaptó un encargo de vídeo similar y señala que la ejecución duró unas dos horas.

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [Un anuncio de juguetes de los noventa hecho con código](https://x.com/kevin_t_ngo/status/2119972124211454139) (por [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Separa la programación de la animación del renderizado.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ Reproducir video</a>

El autor afirma que animó un anuncio de juguetes retro con Python y lo renderizó en Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Una escena de juego en tercera persona con Three.js](https://x.com/bijanbowen/status/2119972220739187182) (por [@bijanbowen](https://x.com/bijanbowen))

**Usa una partida para observar el movimiento y el entorno.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

El autor muestra en una emisión un resultado en Three.js con un personaje en tercera persona que recorre un escenario exterior.

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [Bryceball a partir de un renderizador existente](https://x.com/pleometric/status/2119973274402668852) (por [@pleometric](https://x.com/pleometric))

**Reutiliza un motor de renderizado como base de un juego.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ Reproducir video</a>

El autor adaptó el renderizador descrito en la publicación enlazada para crear el juego Bryceball.

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [Edición recursiva de vídeo con Fable](https://x.com/rileybrown/status/2119973951027724385) (por [@rileybrown](https://x.com/rileybrown))

**Reutiliza una edición anterior como material para otra pieza.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ Reproducir video</a>

El autor compartió un vídeo editado con Fable 5.2 sobre otro que también había editado con el modelo.

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [Una historia cinematográfica de la ciencia](https://x.com/DeryaTR_/status/2119974354260013293) (por [@DeryaTR_](https://x.com/DeryaTR_))

**Organiza una secuencia 3D a partir de una cronología.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ Reproducir video</a>

El autor pidió un recorrido cinematográfico desde los orígenes de la ciencia hasta un futuro hipotético y compartió el vídeo resultante.

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [Máquina voladora de Da Vinci en 3D](https://x.com/higgsfield_ai/status/2119975721909301684) (por [@higgsfield_ai](https://x.com/higgsfield_ai))

**Modela un diseño histórico antes de ensayar cambios.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ Reproducir video</a>

Higgsfield mostró una interpretación 3D de la máquina voladora de Leonardo y describió una prueba física y un rediseño.

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [Trazado de una PCB a partir de un encargo](https://x.com/cmonkey/status/2119975852977029365) (por [@cmonkey](https://x.com/cmonkey))

**Inspecciona la placa enrutada antes de fabricarla.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

El autor compartió un trazado de PCB de Fable 5.2 en respuesta a una discusión sobre el diseño de placas.

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [Un mismo prompt en dos entornos de ejecución](https://x.com/loktar00/status/2119980613369319706) (por [@loktar00](https://x.com/loktar00))

**Registra las diferencias de entorno al comparar resultados.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ Reproducir video</a>

El autor dio el mismo prompt a DeepSeek y a Fable 5.2 en entornos distintos y mostró juntos los resultados.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [Ilustración de Godzilla dibujada con código](https://x.com/chetaslua/status/2119981510199808368) (por [@chetaslua](https://x.com/chetaslua))

**Reinterpreta una imagen con formas vectoriales y movimiento.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ Reproducir video</a>

El autor compartió una ilustración dibujada con código y una animación breve inspirada en una publicación de Godzilla.

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [Ventilador de mano diseñado para impresión 3D](https://x.com/davelee/status/2119981787325579398) (por [@davelee](https://x.com/davelee))

**Usa un prototipo físico para comprobar el ensamblaje.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ Reproducir video</a>

El autor y sus hijos diseñaron un ventilador de mano imprimible y compartieron el modelo antes de imprimirlo.

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [Búsqueda de errores en un plugin frente a Opus](https://x.com/oaranda/status/2119982729747919096) (por [@oaranda](https://x.com/oaranda))

**Compara las correcciones con pruebas de regresión cruzadas.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

Fragmento del anuncio anotado por el autor.

Ambos modelos hallaron los mismos seis errores. Opus superó todas las pruebas cruzadas; Fable falló una y detectó otro problema en el panel.

Prompt original

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [Estambul reconstruida como escena 3D](https://x.com/petergostev/status/2119877733488394520) (por [@petergostev](https://x.com/petergostev))

**Examina una escena urbana desde lejos y de cerca.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ Reproducir video</a>

Peter Gostev comparte una vista 3D de Estambul hecha con Fable 5.2 Max y enlaza la evaluación más extensa.

[Material relacionado 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [Una película en Blender con una pantalla funcional](https://x.com/rileybrown/status/2119902109709537708) (por [@rileybrown](https://x.com/rileybrown))

**Anima la pantalla, la iluminación y la cámara dentro de la misma escena 3D.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ Reproducir video</a>

El autor señala 13 tomas, una página web propia que se reproduce en el portátil y audio de ElevenLabs. Usó GPU de RunPod para renderizar.

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [Una transición de agujeros negros con acoplamiento débil](https://hexagonmath.org/2611.00175v1) (por [@Anthropic](https://www.anthropic.com/))

**Contrasta un cálculo pendiente con el planteamiento teórico original.**

Anthropic señala que Fable 5.2 completó un cálculo pendiente desde hacía tiempo y encontró una transición abrupta en el régimen de acoplamiento débil. La prepublicación recoge la derivación.

[Material relacionado 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [El límite de una cota del bootstrap modular](https://hexagonmath.org/2611.00174v1) (por [@Anthropic](https://www.anthropic.com/))

**Publica la derivación junto a la cota analítica propuesta.**

Anthropic señala que Fable 5.2 determinó el límite exacto de una técnica de bootstrap modular sin espín en un modelo simplificado de gravedad cuántica.

[Material relacionado 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Vercel AI Gateway con modelos de respaldo ordenados](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (por [Vercel](https://vercel.com/))

**Configura en el gateway el orden de respaldo para peticiones rechazadas por el clasificador.**

El ejemplo de Vercel AI SDK invoca anthropic/claude-fable-5.2 y configura Opus 5.5 y luego Sonnet 5.5 como respaldo. La guía documenta el requisito de retención de datos.

[Material relacionado 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [Subagentes anidados y presupuesto de revisión](https://news.ycombinator.com/item?id=50430925) (por [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**Controla la delegación anidada y limita el presupuesto fuera del prompt.**

El autor pidió un máximo de cuatro subagentes para revisar 80 000 líneas de código. Señala que hubo al menos seis agentes anidados y que agotó la cuota de cinco horas en menos de 20 minutos.

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [Comparación de conversión de un diseño LCARS a HTML](https://news.ycombinator.com/item?id=50430962) (por [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**Comprueba por separado las curvas, los iconos, la animación y la navegación.**

El autor compara Fable 5.2 y Opus 5.5 con un mismo diseño inspirado en Star Trek. Prefirió las curvas y algunos iconos de Fable, pero el movimiento de Opus, y consideró molesto el parpadeo del SVG de Fable. Solo solicitó la primera página.

[Material relacionado 1](https://html.non.io/lcars-fable-5.2/) · [Material relacionado 2](https://html.non.io/lcars-opus-5.5/) · [Material relacionado 3](https://news.ycombinator.com/item?id=50431231) · [Material relacionado 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [Optimización para GPU de Quantum ESPRESSO](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (por [Discovered Materials](https://discoveredmaterials.com/))

**Exige resultados de referencia y pruebas ocultas representativas al optimizar código científico.**

Discovered Materials señala una aceleración media geométrica de 36× en 13 pruebas de fonones con la misma GPU y de alrededor de 9× en cálculos con funcionales híbridos. El parche publicado se apoya en pruebas de corrección y rendimiento.

[Material relacionado 1](https://github.com/discovered-materials/dm_qe) · [Material relacionado 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [Índice de inteligencia de Artificial Analysis por nivel de esfuerzo](https://artificialanalysis.ai/models/claude-fable-5-2) (por [Artificial Analysis](https://artificialanalysis.ai/))

**Lee juntos la puntuación, el coste y la latencia por tarea en el nivel elegido.**

La medición citada de Max con alternativa predeterminada da un índice de 65, 26,54 USD y 46,4 minutos por tarea. Las cifras corresponden a la carga del benchmark.

[Material relacionado 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [Falsos positivos al revisar cambios con esfuerzo High](https://news.ycombinator.com/item?id=50431810) (por [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**Comprueba los hallazgos del modelo en el código antes de actuar.**

Un desarrollador señala que Fable 5.2 High marcó dos problemas inexistentes, que detectó gracias a su conocimiento del código.

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [Treinta tareas habituales de programación](https://news.ycombinator.com/item?id=50432483) (por [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**Mide la duración y las tareas resueltas con la misma carga de trabajo.**

El autor señala que Fable 5.2 y Opus 5.5 resolvieron 26 de 30 tareas y Fable 5.1 resolvió 25. Fable 5.2 tardó 0,62 veces lo que tardó 5.1, sin bloqueos de seguridad notificados.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [Salvapantallas de un náufrago en una isla](https://news.ycombinator.com/item?id=50432836) (por [@nzach](https://news.ycombinator.com/user?id=nzach))

**Abre la página interactiva para examinar el salvapantallas.**

El autor de Show HN enlaza una escena de isla para navegador llamada Stranded with Claude. El resultado publicado es un lienzo interactivo.

[Material relacionado 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [Tres juegos de navegador con esfuerzo High](https://senko.net/vibecode-bench/) (por [Senko Rašić](https://senko.net/))

**Compara por separado la jugabilidad y la fidelidad visual.**

Senko Rašić ejecutó los encargos de estrategia en tiempo real, vóxeles y simulación de vuelo con Fable 5.2 en Claude Code. Destaca mecánicas más elaboradas, como una aeronave para recorrer el mapa completo, y juzga peores algunas partes gráficas.

[Material relacionado 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [Guiones de pódcast sobre libros, capítulo a capítulo](https://news.ycombinator.com/item?id=50434156) (por [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**Compara la longitud de los guiones con el mismo encargo recurrente.**

El autor generó diálogos entre dos reseñistas, un capítulo por vez. Indica unas 2,5 páginas de las versiones de Fable frente a 4,5 de Opus 5.5 y enlaza ambas muestras.

[Material relacionado 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [Material relacionado 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [Un servicio de producción migrado a Rust](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (por [@Anthropic](https://www.anthropic.com/))

**Mide el arranque antes y después de migrar.**

Anthropic señala que agentes con una versión preliminar de Fable 5.2 reescribieron en Rust un servicio de producción en Python y redujeron el tiempo de arranque unas 26 veces.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [Elegir Fable 5.2 en GitHub Copilot](https://x.com/github/status/2119926269982961833) (por [@github](https://x.com/github))

**Habilita la política de la organización antes de elegir el modelo.**

GitHub documenta el selector de modelos de Copilot y la configuración de administrador necesaria en las cuentas Business y Enterprise.

[Material relacionado 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [Reto de diseño de cien páginas HTML](https://x.com/MiaAI_lab/status/2119930229661503893) (por [@MiaAI_lab](https://x.com/MiaAI_lab))

**Cuenta los archivos completos y ejecutables además de evaluar su aspecto.**

El autor pidió 100 diseños distintos, publicó 76 archivos con sus prompts y afirma haber agotado su cuota de Fable.

[Material relacionado 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [Material relacionado 2](https://mia-ai.net/lab/experiments/100-htmls) · [Material relacionado 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [Material relacionado 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [Material relacionado 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [Material relacionado 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [Material relacionado 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [Material relacionado 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [Material relacionado 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [Material relacionado 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [Material relacionado 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [Material relacionado 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [Material relacionado 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [Material relacionado 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [Deriva de requisitos en un compilador](https://x.com/sameQCU/status/2119939304864800971) (por [@sameQCU](https://x.com/sameQCU))

**Contrasta los requisitos citados por el agente con la entrada original.**

El desarrollador describe una tarea de compilación en la que Fable 5.2 y versiones anteriores de Opus describieron mal los requisitos recibidos.

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [Seguir una tarea larga de Fable con Opus](https://x.com/marouane53/status/2119950129767858262) (por [@marouane53](https://x.com/marouane53))

**Usa una sesión aparte para seguir el avance de tareas largas.**

El autor relata que algunas tareas de Fable duraron más de dos horas y que apenas hubo novedades. Usó Opus 5.5 en otro hilo para explicar el avance y las decisiones.

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [Revisión de código con una mirada nueva](https://x.com/doodlestein/status/2119958895158292786) (por [@doodlestein](https://x.com/doodlestein))

**Haz una revisión separada de los archivos nuevos y modificados.**

El autor comparte dos prompts de seguimiento exactos para encontrar y corregir errores después de implementar.

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
### Case 463: [Pérdida de contexto al revisar el diseño de una función](https://news.ycombinator.com/item?id=50434214) (por [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**Usa el diseño actual como lista de comprobación al revisar consejos posteriores.**

El autor comparó ambos modelos al revisar una función y prefirió Opus 5.5. En un diagnóstico posterior, Fable 5.2 recomendó algo ya presente en el diseño.

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [Comparación de un Breakout al estilo DX Ball](https://news.ycombinator.com/item?id=50434424) (por [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**Compara las mecánicas y la sensación al jugar a partir del mismo encargo.**

El autor enlaza versiones de Fable 5.2 y Opus 5.5 de ejecuciones distintas. Fable cambió algunas mecánicas originales y el autor prefirió jugar a la versión de Opus.

[Material relacionado 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [Material relacionado 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [Una prueba de mejora de una aplicación 3D](https://news.ycombinator.com/item?id=50434433) (por [@user43928](https://news.ycombinator.com/user?id=user43928))

**Compara los cambios visibles con el presupuesto consumido en la misma tarea.**

El autor pidió a Fable 5.2 que mejorara una aplicación 3D que no era un juego. Señala poca diferencia frente a Opus 5.5 y un consumo del 25 % de su cuota de Fable esa noche.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [Juego del ratón y el gato con tres modelos](https://news.ycombinator.com/item?id=50434508) (por [@simonw](https://news.ycombinator.com/user?id=simonw))

**Mantén fijo el prompt e inspecciona cada implementación jugable.**

Simon Willison comparte intentos en Three.js para móviles con Fable 5.2 Extra, Opus 5.5 Extra y GPT-6 Extra High. Señala unos 40 minutos para el intento de Fable.

[Material relacionado 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [Material relacionado 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [Material relacionado 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

Prompt original

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [Coste y puntuación en AIBenchy con esfuerzo High](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (por [AIBenchy](https://aibenchy.com/))

**Compara puntuación, coste total y latencia con niveles de esfuerzo equivalentes.**

AIBenchy publicó 8,7 frente a 9,4, costes totales de 5,083 frente a 2,133 USD y tiempos medios de 14,73 frente a 27,55 segundos para Fable 5.2 High y Opus 5.5 High, respectivamente.

[Material relacionado 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [Ajustar el entorno de agentes de Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (por [@Anthropic](https://www.anthropic.com/))

**Vuelve a probar los niveles de esfuerzo y define los avisos de progreso.**

La guía de Anthropic incluye ejemplos de instrucciones sobre esfuerzo, criterios de finalización, aprobaciones, avisos y límites de subagentes.

[Material relacionado 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="case-469"></a>
### Case 469: [Una aplicación para previsualizar personajes animados](https://x.com/seiiiiiiiiiiru/status/2121390458572333253) (por [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Pide a Fable que convierta las comprobaciones repetitivas de recursos en una interfaz.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/ce514e99465c257220ee9bf7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/776670eda35fbabbf1c63663.jpg" alt="Case 469 · 1" width="760"><br>▶ Reproducir video</a>

La persona que publicó el ejemplo cuenta que incorporó Fable 5.2 como asesor y que este convirtió un flujo poco eficiente en una aplicación. La grabación muestra movimientos predefinidos, controles de fondo y opciones para exportar un personaje 3D en GLB y PNG transparente.

Type: Demo | Date: 2026-11-13

---

<a id="case-470"></a>
### Case 470: [Prueba de un código QR generado sin herramientas](https://x.com/AdamHoltererer/status/2121376853474578625) (por [@AdamHoltererer](https://x.com/AdamHoltererer))

**Escanea la imagen del código QR para comprobar si el intento funcionó.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d3833f006038158569c9816d.png" alt="Case 470 · 1" width="760">

Adam Holter atribuye la demostración del código QR a Fable 5.2, Astra y Sol, y afirma que no usaron herramientas. Al escanear localmente la imagen adjunta se comprobó que codifica el texto exacto «MADE WITHOUT TOOLS».

Type: Evaluation | Date: 2026-11-13

---

<a id="case-471"></a>
### Case 471: [Un juego de zombis en Unity con Tripo](https://x.com/fe_yukichi/status/2121375714192814554) (por [@fe_yukichi](https://x.com/fe_yukichi))

**Usa un flujo común de creación de recursos para diseñar un elenco de personajes jugables.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/055f505803b769bb8b24a54e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0fa0715e64f91ab69725599e.jpg" alt="Case 471 · 1" width="760"><br>▶ Reproducir video</a>

En una colaboración declarada con Tripo, el creador afirma haber usado Tripo Agentic Canvas para generar ocho personajes jugables y dieciséis variantes de zombis para un juego de Unity hecho con Fable 5.2. El vídeo muestra la selección de personajes y una partida. El creador publicó una versión para navegadores de escritorio.

[Material relacionado 1](https://tsukiyo-zombie.pages.dev/)

Type: Demo | Date: 2026-11-13

---

<a id="case-472"></a>
### Case 472: [Una calle nevada pintada en MS Paint](https://www.reddit.com/r/ClaudeAI/comments/1xvghd1/fable_52_painting_in_ms_paint/) (por [u/wollymonjac](https://www.reddit.com/user/wollymonjac/))

**Usa una grabación de pantalla para evaluar el manejo directo del ratón durante una tarea larga.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/10ad84001f4c682c5343846c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e7af823e10ef2135adec2154.jpg" alt="Case 472 · 1" width="760"><br>▶ Reproducir video</a>

El autor de la publicación original en Reddit dice que Fable 5.2 pintó una calle nevada en MS Paint con el ratón en unas dos horas y media. La republicación enlazada en X contiene una grabación de la misma escena.

[Material relacionado 1](https://x.com/i/status/2121373793599869213)

Type: Demo | Date: 2026-11-13

---

<a id="case-473"></a>
### Case 473: [Un enchufe sin conectar en Wojak-Bench](https://x.com/lukaspet/status/2121371593943466167) (por [@lukaspet](https://x.com/lukaspet))

**Comprueba que cada conexión del montaje 3D generado coincida con la referencia.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e509db79b2e79fcc2d6beda1.jpg" alt="Case 473 · 1" width="760">

El autor cuenta que Fable 5.2 no conectó el cable a la toma en esta prueba de Wojak-Bench. La imagen original muestra una fotografía del resultado 3D junto al dibujo de referencia.

Type: Limit | Date: 2026-11-13

---

<a id="case-474"></a>
### Case 474: [Un arreglo de piano para un videojuego rítmico](https://x.com/DJ_HYSNS/status/2121367353237942287) (por [@DJ_HYSNS](https://x.com/DJ_HYSNS))

**Comprueba si la pieza se puede tocar y qué controles de producción puedes usar al pedirle a un modelo que componga.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d016f48687e0c8e6cf810812.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/9faa77e2e9ba2ec99be995a7.jpg" alt="Case 474 · 1" width="760"><br>▶ Reproducir video</a>

El autor pidió música para un videojuego rítmico y pasó al piano solo tras encontrar dificultades para que el modelo eligiera sonidos VST y mezclara la pieza. El vídeo muestra la cuadrícula de notas resultante. Según el autor, la pieza excede la dificultad que había fijado para que una persona pudiera tocarla.

Type: Evaluation | Date: 2026-11-13

---

<a id="case-475"></a>
### Case 475: [Rediseño de la recuperación de tokens en Picnic](https://x.com/joaoavf/status/2121366491321057717) (por [@joaoavf](https://x.com/joaoavf))

**Compara los estados de la interfaz al recuperar tokens que la plataforma no admite.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/551612796f4150a43b190ee3.jpg" alt="Case 475 · 1" width="760">

El autor dice que, con una o dos instrucciones, Fable 5.2 propuso un nuevo flujo para recuperar tokens no admitidos por Picnic. La imagen adjunta muestra varias pantallas de la propuesta.

Type: Demo | Date: 2026-11-13

---

<a id="case-476"></a>
### Case 476: [Montaje de una apertura de anime con clips generados](https://x.com/aimikoda/status/2121362621274177726) (por [@aimikoda](https://x.com/aimikoda))

**Dale a Fable los clips, la música y pautas explícitas para cortar al ritmo de la pista.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e3ab28061669d84818042ee0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/cb65344e413d2bd340406d59.jpg" alt="Case 476 · 1" width="760"><br>▶ Reproducir video</a>

La persona que publicó el ejemplo combinó clips de MiniMax H3 y una pista de Suno v6 y usó Fable 5.2 Medium para el montaje. El resultado publicado incluye personajes animados en pixel art y transiciones. El ejemplo conserva la instrucción original de montaje para Fable.

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
### Case 477: [Animación de un personaje con tres herramientas](https://x.com/ingi_erlingsson/status/2121361947446677797) (por [@ingi_erlingsson](https://x.com/ingi_erlingsson))

**Compara el GIF de entrada con la animación tras los pasos en Fable y ComfyUI.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/69a3410b7b2dcdb14ee6c5d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/391924750cd0641254cb114f.jpg" alt="Case 477 · 1" width="760"><br>▶ Reproducir video</a>

El autor indica que partió de un GIF de GPT Image 2.6 y usó después Fable 5.2 y ComfyUI. El vídeo adjunto muestra la cabeza de un personaje que cambia mientras gira el punto de vista.

Type: Demo | Date: 2026-11-13

---

<a id="case-478"></a>
### Case 478: [Un tráiler urbano renderizado con scripts de Blender](https://x.com/hanghuang_/status/2121361932456427644) (por [@hanghuang_](https://x.com/hanghuang_))

**Divide el trabajo del tráiler en la escena, el personaje, el vehículo y el renderizado.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0e5170c057eecd328b178fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d10c5d322edba010282a60d0.jpg" alt="Case 478 · 1" width="760"><br>▶ Reproducir video</a>

El creador cuenta que Fable 5.2 planificó un tráiler con estética de videojuego y escribió código de Blender para la ciudad, el personaje y el coche. Según el creador, siete GPU alquiladas renderizaron el resultado en 4K. El vídeo publicado muestra los planos terminados.

Type: Demo | Date: 2026-11-13

---

<a id="case-479"></a>
### Case 479: [Escenas nocturnas dibujadas con JavaScript](https://x.com/kloss_xyz/status/2121356668311384487) (por [@kloss_xyz](https://x.com/kloss_xyz))

**Revisa varias imágenes terminadas al evaluar ilustraciones generadas mediante código.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/6e9d554b17822715f07d3be8.jpg" alt="Case 479 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/f57db49bb8213cc6ca4bcafe.jpg" alt="Case 479 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/2933b30de09501dbbb7e1505.jpg" alt="Case 479 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/490e5952694322b7963be8e2.jpg" alt="Case 479 · 4" width="450"></td></tr></table>

El autor atribuye a Fable 5.2 el dibujo en JavaScript de las cuatro ilustraciones publicadas. Los adjuntos muestran escenas nocturnas estilizadas y permiten comparar los resultados.

Type: Demo | Date: 2026-11-13

---

<a id="case-480"></a>
### Case 480: [De modelos CAD a planos técnicos](https://x.com/MecAgent/status/2121352868490100787) (por [@MecAgent](https://x.com/MecAgent))

**Contrasta las vistas, cotas y anotaciones con el modelo CAD original.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/5ce59334e405a279e1008bf0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/780dc65cb1b04f7a75e27ace.jpg" alt="Case 480 · 1" width="760"><br>▶ Reproducir video</a>

La demostración de MecAgent muestra planos con varias vistas y anotaciones y atribuye la conversión a Fable 5.2. El vídeo permite ver los planos obtenidos. Para evaluar la precisión de las cotas habría que contrastarlas con los archivos CAD.

Type: Demo | Date: 2026-11-13

---

<a id="case-481"></a>
### Case 481: [Las 43 tareas de la prueba de análisis de Plotly](https://plotly.com/blog/gemini-4-hydrogen-plotly-data-analytics-bench/) (por [Plotly](https://plotly.com/))

**Compara la precisión y el coste por ejecución con el mismo entorno de evaluación.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/50882a17db12bede9165a92d.webp" alt="Case 481 · 1" width="760">

El informe de Plotly sitúa a Fable 5.2 entre los cuatro modelos que resolvieron las 43 preguntas, incluidas las cinco sobre patrones ocultos. Plotly advierte que una ejecución por modelo ofrece una sola observación. El gráfico recoge el coste y la precisión de la prueba.

[Material relacionado 1](https://news.ycombinator.com/item?id=50485733)

Type: Benchmark | Date: 2026-11-12

---

<a id="case-482"></a>
### Case 482: [Una estación SGI Indy recreada como sitio web](https://news.ycombinator.com/item?id=50476597) (por [@gdubs](https://news.ycombinator.com/user?id=gdubs))

**Explora cómo trasladar una estación de trabajo física a la web mediante una recreación interactiva.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/74b80686867b920881164246.jpg" alt="Case 482 · 1" width="760">

Gregory Wieber atribuye a Fable 5.2 la transformación de su sitio en una Silicon Graphics Indy de los años noventa. La demostración incluye una estación de trabajo en 3D con inicio de sesión, un sistema de archivos tridimensional y el juego Soft Break.

[Material relacionado 1](https://gregorywieber.com/indy/)

Type: Demo | Date: 2026-11-13

---

<a id="case-483"></a>
### Case 483: [Coordinación de agentes mediante incidencias y worktrees](https://news.ycombinator.com/item?id=50493545) (por [@nickalaso](https://news.ycombinator.com/user?id=nickalaso))

**Usa incidencias para asignar tareas y worktrees y pull requests para aislar los cambios.**

El autor dice que usa Fable 5.2 como coordinador principal, instancias de Opus como coordinadores secundarios y un servidor MCP propio para iniciar agentes de varios proveedores. Usa incidencias de GitHub para seguir el trabajo y worktrees y pull requests para evitar conflictos.

Type: Integration | Date: 2026-11-14

---

<a id="case-484"></a>
### Case 484: [Verificación de citas con procesos en segundo plano](https://x.com/tukiyomiiori/status/2121368478364192930) (por [@tukiyomiiori](https://x.com/tukiyomiiori))

**Delega la comprobación de citas y observa cuándo se reanuda la sesión principal.**

El autor cuenta que pidió a Fable 5.2 comprobar los artículos citados con subagentes y scripts en segundo plano. Observó que la sesión de Claude Code se puso en pausa mientras se ejecutaban y se reanudó cuando los subagentes o los scripts terminaron.

Type: Integration | Date: 2026-11-13

---

<a id="case-485"></a>
### Case 485: [Depuración de un modelo de tarifas de flete de ida y vuelta](https://x.com/allTheYud/status/2121360145921998877) (por [@allTheYud](https://x.com/allTheYud))

**Comprueba si el modelo imputa correctamente los costes marginales al trayecto de vuelta.**

En una simulación de transporte en ambos sentidos, el autor dice que Fable 5.2 imputó a un trayecto el combustible de ida y vuelta y trató el otro como marginal, pese a que el barco tenía que regresar. El autor tuvo que depurar varias veces fallos de ese tipo.

Type: Limit | Date: 2026-11-13

---

<a id="case-486"></a>
### Case 486: [Adaptación de la inferencia de Edge0 a Mac](https://news.ycombinator.com/item?id=50482710) (por [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen))

**Pide los cambios de plataforma y prueba la inferencia en el equipo de destino.**

En una conversación sobre Edge0-145B, un comentarista dice que le pidió a Fable 5.2 una versión compatible con Mac y que hizo algunos ajustes. En su equipo con M5 Max y NVFP4, dice haber obtenido unos 50 tokens por segundo.

[Material relacionado 1](https://news.ycombinator.com/item?id=50475713)

Type: Integration | Date: 2026-11-13

---

<a id="case-487"></a>
### Case 487: [Revisión de placas de circuito de alta densidad](https://news.ycombinator.com/item?id=50478759) (por [@0_____0](https://news.ycombinator.com/user?id=0_____0))

**Contrasta la colocación y la selección de componentes con los requisitos de rendimiento de la placa.**

Un comentarista de Hacker News probó Fable 5.2 para colocar componentes y trazar pistas en varias placas. Según explica, un diseño denso parecía prometedor al principio. Para cumplir sus requisitos tuvo que modificar considerablemente la colocación y redibujar a mano la mayor parte del esquema.

Type: Limit | Date: 2026-11-13

---

<a id="case-488"></a>
### Case 488: [Rastreo de una cita en un periódico de pago](https://news.ycombinator.com/item?id=50478191) (por [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff))

**Mantén la atribución como provisional hasta poder consultar el texto original.**

Un comentarista de Hacker News rastreó una atribución hasta un artículo de 1985 de The Dallas Morning News citado en una lista de correo de lingüística. Según cuenta, Fable 5.2 no pudo abrir el artículo completo y propuso un posible periodista y contexto. El texto original sigue siendo necesario para confirmar la atribución.

[Material relacionado 1](https://listserv.linguistlist.org/pipermail/ads-l/2003-September/033575.html)

Type: Limit | Date: 2026-11-13

---

<a id="case-489"></a>
### Case 489: [Planificación con Fable y revisión de los cambios de Opus](https://news.ycombinator.com/item?id=50477200) (por [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology))

**Aprueba un plan escrito, divide la implementación en frentes de trabajo y comprueba los cambios en CI y en preproducción.**

El autor comparte un flujo que dice haber usado en bases de código grandes. Fable 5.2 planifica, los subagentes de Opus 5.5 implementan y revisan, la integración continua controla la cobertura de pruebas y una lista de preproducción guía la verificación manual.

Type: Tutorial | Date: 2026-11-13

---

<a id="acknowledge"></a>
## Créditos

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/), [@fe_yukichi](https://x.com/fe_yukichi), [u/wollymonjac](https://www.reddit.com/user/wollymonjac/), [@lukaspet](https://x.com/lukaspet), [@DJ_HYSNS](https://x.com/DJ_HYSNS), [@joaoavf](https://x.com/joaoavf), [@aimikoda](https://x.com/aimikoda), [@ingi_erlingsson](https://x.com/ingi_erlingsson), [@hanghuang_](https://x.com/hanghuang_), [@MecAgent](https://x.com/MecAgent), [Plotly](https://plotly.com/), [@gdubs](https://news.ycombinator.com/user?id=gdubs), [@nickalaso](https://news.ycombinator.com/user?id=nickalaso), [@tukiyomiiori](https://x.com/tukiyomiiori), [@allTheYud](https://x.com/allTheYud), [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen), [@0_____0](https://news.ycombinator.com/user?id=0_____0), [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff), [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology)
