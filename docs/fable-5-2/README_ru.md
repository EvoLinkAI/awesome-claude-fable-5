# Примеры использования Claude Fable 5.2

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

Рабочие процессы, демонстрации, сравнения, тесты, интеграции и практические ограничения из подборок за 10 и 13–14 ноября со ссылками на источники.

[Анонс Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [Предыдущая подборка](../../README_ru.md)

## Указатель кейсов

| Case | Примеры использования | Type |
| --- | --- | --- |
| 330 | [Рисунок MacBook в SVG при разных уровнях усилий](#case-330) | Benchmark |
| 331 | [Игра beat ’em up на четверых по семейным рисункам](#case-331) | Demo |
| 332 | [Три электронных устройства от проекта до сборки](#case-332) | Demo |
| 333 | [Формализация Великой теоремы Ферма в Lean](#case-333) | Evaluation |
| 334 | [Операционная система из пустой папки](#case-334) | Demo |
| 335 | [Манипуляции двумя роботизированными руками в RoboDojo](#case-335) | Benchmark |
| 336 | [Фонтан в движении](#case-336) | Demo |
| 337 | [Покадровая синхронизация губ с Higgsfield](#case-337) | Integration |
| 338 | [Прототип вождения в открытом мире](#case-338) | Demo |
| 339 | [Париж 1940 года по референсам](#case-339) | Integration |
| 340 | [Fable планирует короткометражку, Opus её создаёт](#case-340) | Integration |
| 341 | [Эксперимент с музыкальным клипом](#case-341) | Demo |
| 342 | [Живописный портрет Дарио Амодеи](#case-342) | Demo |
| 343 | [Spud Smash в режиме Medium](#case-343) | Demo |
| 344 | [Ледяной собор от Fable и Opus](#case-344) | Evaluation |
| 345 | [Пение с имитацией речевого тракта](#case-345) | Demo |
| 346 | [Три воксельных теста со Стамбулом](#case-346) | Evaluation |
| 347 | [Доля выполненных проектов в Remote Labor Index](#case-347) | Benchmark |
| 348 | [Сцена с айсбергом при четырёх уровнях усилий](#case-348) | Evaluation |
| 349 | [Аниме-ролик на 79 секунд](#case-349) | Demo |
| 350 | [Механические сборки от Fable и Opus](#case-350) | Evaluation |
| 351 | [Роботизированная кисть поднимается по винтовой лестнице](#case-351) | Demo |
| 352 | [Оснастка модели Tripo в Blender](#case-352) | Evaluation |
| 353 | [Интерактивные изобретения из блокнота да Винчи](#case-353) | Demo |
| 354 | [Музыкальная рабочая станция под управлением Claude](#case-354) | Demo |
| 355 | [Анимированная Raspberry Pi 5](#case-355) | Demo |
| 356 | [Сцена на севере Италии](#case-356) | Demo |
| 357 | [Книжка-панорама с локальными агентами](#case-357) | Evaluation |
| 358 | [Возвращение теста с лава-лампой](#case-358) | Evaluation |
| 359 | [Детализированный реактивный самолёт в Blender](#case-359) | Integration |
| 360 | [Путешествие через порталы в сотни миров](#case-360) | Demo |
| 361 | [Бомбейский базар в шести кадрах на Three.js](#case-361) | Integration |
| 362 | [Фотореалистичная закусочная, созданная кодом](#case-362) | Integration |
| 363 | [Модель робота в Blender](#case-363) | Demo |
| 364 | [Анимационный ролик о Convex](#case-364) | Demo |
| 365 | [Подборка лендингов по одному запросу на каждый](#case-365) | Demo |
| 366 | [Партитура фортепианной сонаты в LilyPond](#case-366) | Demo |
| 367 | [Видео по свободному заданию](#case-367) | Demo |
| 368 | [Fable планирует, DeepSeek реализует, Opus проверяет](#case-368) | Integration |
| 369 | [Fable 5.2 в AI Village](#case-369) | Integration |
| 370 | [Дизайн интерфейса с навыками и без них](#case-370) | Evaluation |
| 371 | [Поиск неявных конечных автоматов в коде](#case-371) | Tutorial |
| 372 | [Игра с нуля за восемь часов](#case-372) | Demo |
| 373 | [Прототип Fishslop и затраты на токены](#case-373) | Evaluation |
| 374 | [Футбольная игра в движении](#case-374) | Demo |
| 375 | [Бой с боссом в открытом мире с Higgsfield MCP](#case-375) | Integration |
| 376 | [Мон-Сен-Мишель с приливами и отливами](#case-376) | Demo |
| 377 | [Игровой объект для Roblox в Blender](#case-377) | Demo |
| 378 | [Рассуждение без вывода цепочки мыслей](#case-378) | Benchmark |
| 379 | [Версии Chrome Dino от четырёх моделей](#case-379) | Evaluation |
| 380 | [Шашки с роботизированной рукой](#case-380) | Demo |
| 381 | [Пятнадцатисекундный анимационный ролик](#case-381) | Demo |
| 382 | [Интерактивная сцена с Эйфелевой башней](#case-382) | Demo |
| 383 | [Гонки в открытом море с Three.js и Higgsfield](#case-383) | Integration |
| 384 | [Симуляция мёда в реальном времени на WebGL](#case-384) | Demo |
| 385 | [Программно созданные визуальные эффекты для видео](#case-385) | Demo |
| 386 | [Анимация о звёздах розыска в GTA](#case-386) | Demo |
| 387 | [Стилизованный мир MMO, созданный кодом](#case-387) | Demo |
| 388 | [3D-сцена от Fable и Opus](#case-388) | Evaluation |
| 389 | [Избыточный текст на экране паузы игры](#case-389) | Limit |
| 390 | [Мудборды в среде Krea](#case-390) | Integration |
| 391 | [Офисное тестирование шутера с порталами](#case-391) | Demo |
| 392 | [Детализированный твердотельный объект в Blender](#case-392) | Demo |
| 393 | [Параллельные тесты интерфейсов при разных уровнях усилий](#case-393) | Evaluation |
| 394 | [Небольшая игра за десять запросов](#case-394) | Demo |
| 395 | [Покадровая анимация на JavaScript](#case-395) | Demo |
| 396 | [3D-анимация по видеореференсу](#case-396) | Demo |
| 397 | [Пиксельный костёр от Fable и Opus](#case-397) | Evaluation |
| 398 | [Arena WebDev в режиме xHigh](#case-398) | Benchmark |
| 399 | [Типографика кинотрейлера от двух моделей](#case-399) | Evaluation |
| 400 | [Моушн-дизайн и 3D по одному запросу на проект](#case-400) | Evaluation |
| 401 | [Интерактивное объяснение устройства ядерного реактора](#case-401) | Demo |
| 402 | [Агенты в Blood on the Clocktower](#case-402) | Benchmark |
| 403 | [Прототип гонок на подах](#case-403) | Demo |
| 404 | [Десятисекундная реклама белья Claude](#case-404) | Demo |
| 405 | [Птица на рассвете, мазок за мазком](#case-405) | Demo |
| 406 | [Длительный графический прогон в Devin](#case-406) | Evaluation |
| 407 | [Живопись кодом в трёх моделях](#case-407) | Evaluation |
| 408 | [История письменности в анимации](#case-408) | Demo |
| 409 | [Полигон для игровых механизмов](#case-409) | Demo |
| 410 | [Печатная плата портативной консоли на Linux](#case-410) | Evaluation |
| 411 | [Воксельная сцена с озером](#case-411) | Demo |
| 412 | [17 интерактивных работ от Arena](#case-412) | Demo |
| 413 | [Полёт с дружелюбным драконом](#case-413) | Demo |
| 414 | [Желейная косатка от Fable и Opus](#case-414) | Evaluation |
| 415 | [Открытая проверка качества видео](#case-415) | Demo |
| 416 | [Космическая станция в средиземноморском стиле](#case-416) | Demo |
| 417 | [Бенчмарк интерактивных 3D-сцен AA-3D](#case-417) | Benchmark |
| 418 | [Игровое испытание со скелетом на время](#case-418) | Demo |
| 419 | [Пиксель-арт от Fable и Astra](#case-419) | Evaluation |
| 420 | [Портфолио-ролик с моушн-дизайном](#case-420) | Demo |
| 421 | [Рендер бассейна со стеклом в двух моделях](#case-421) | Evaluation |
| 422 | [Точность вызова инструментов в TS-Bench](#case-422) | Benchmark |
| 423 | [Миниатюрный мир Мачу-Пикчу](#case-423) | Demo |
| 424 | [GDPx по категориям профессиональных задач](#case-424) | Benchmark |
| 425 | [Портрет в графическом редакторе](#case-425) | Demo |
| 426 | [VulcanBench Frontier v4 в режиме Low](#case-426) | Benchmark |
| 427 | [Играбельные Backrooms со сменой ролей](#case-427) | Demo |
| 428 | [Bugatti Tourbillon в Blender](#case-428) | Demo |
| 429 | [Ролик о компьютерах, созданный двумя моделями](#case-429) | Demo |
| 430 | [Музыкальный клип о мегаядрах](#case-430) | Demo |
| 431 | [Экскурсия по студии на основе фотографий](#case-431) | Demo |
| 432 | [Реклама игрушек в духе 1990-х, созданная кодом](#case-432) | Demo |
| 433 | [Игровая сцена от третьего лица на Three.js](#case-433) | Demo |
| 434 | [Bryceball на основе готового рендерера](#case-434) | Demo |
| 435 | [Видеомонтаж с Fable на материале предыдущей работы](#case-435) | Demo |
| 436 | [История науки в кинематографичной 3D-сцене](#case-436) | Demo |
| 437 | [Летательный аппарат да Винчи в 3D](#case-437) | Integration |
| 438 | [Трассировка печатной платы по техническому заданию](#case-438) | Demo |
| 439 | [Один запрос в разных средах запуска](#case-439) | Evaluation |
| 440 | [Годзилла, нарисованный кодом](#case-440) | Demo |
| 441 | [Ручной вентилятор для 3D-печати](#case-441) | Demo |
| 442 | [Поиск ошибок в плагине с Fable и Opus](#case-442) | Evaluation |
| 443 | [Стамбул, воссозданный в 3D](#case-443) | Demo |
| 444 | [Ролик о студии в Blender с работающим экраном](#case-444) | Demo |
| 445 | [Переход с образованием чёрных дыр при слабой связи](#case-445) | Evaluation |
| 446 | [Предел оценки в модульном бутстрепе](#case-446) | Evaluation |
| 447 | [Резервные модели по порядку в Vercel AI Gateway](#case-447) | Integration |
| 448 | [Вложенные субагенты и бюджет проверки кода](#case-448) | Limit |
| 449 | [Перенос дизайна LCARS в HTML](#case-449) | Evaluation |
| 450 | [Оптимизация Quantum ESPRESSO для GPU](#case-450) | Benchmark |
| 451 | [Индекс Artificial Analysis при разных уровнях усилий](#case-451) | Benchmark |
| 452 | [Ложные срабатывания при проверке изменений в режиме High](#case-452) | Limit |
| 453 | [Тридцать повседневных задач по программированию](#case-453) | Evaluation |
| 454 | [Заставка о робинзоне на необитаемом острове](#case-454) | Demo |
| 455 | [Три браузерные игры в режиме High](#case-455) | Evaluation |
| 456 | [Сценарии книжного подкаста по главам](#case-456) | Evaluation |
| 457 | [Перенос рабочего сервиса на Rust](#case-457) | Evaluation |
| 458 | [Выбор Fable 5.2 в GitHub Copilot](#case-458) | Integration |
| 459 | [Испытание на сто вариантов HTML-дизайна](#case-459) | Evaluation |
| 460 | [Искажение требований в задаче для компилятора](#case-460) | Limit |
| 461 | [Наблюдение за долгой задачей Fable через Opus](#case-461) | Integration |
| 462 | [Повторная проверка кода свежим взглядом](#case-462) | Tutorial |
| 463 | [Уход от текущего проекта при проверке функции](#case-463) | Limit |
| 464 | [Сравнение игр в духе DX Ball](#case-464) | Evaluation |
| 465 | [Попытка улучшить 3D-приложение](#case-465) | Evaluation |
| 466 | [Игра про мышь и кошку от трёх моделей](#case-466) | Evaluation |
| 467 | [Сравнение оценок и стоимости в AIBenchy при High](#case-467) | Benchmark |
| 468 | [Настройка среды агентов для Fable 5.2](#case-468) | Tutorial |
| 469 | [Приложение для просмотра анимированных персонажей](#case-469) | Demo |
| 470 | [Проверка QR-кода, созданного без инструментов](#case-470) | Evaluation |
| 471 | [Игра про зомби на Unity с Tripo](#case-471) | Demo |
| 472 | [Заснеженная улица, нарисованная в MS Paint](#case-472) | Demo |
| 473 | [Пропущенное соединение с розеткой в Wojak-Bench](#case-473) | Limit |
| 474 | [Фортепианная аранжировка для ритм-игры](#case-474) | Evaluation |
| 475 | [Новый сценарий восстановления токенов в Picnic](#case-475) | Demo |
| 476 | [Монтаж аниме-заставки из сгенерированных кадров](#case-476) | Tutorial |
| 477 | [Анимация персонажа с помощью трёх инструментов](#case-477) | Demo |
| 478 | [Рендер городского трейлера с помощью скриптов Blender](#case-478) | Demo |
| 479 | [Рисование ночных сцен на JavaScript](#case-479) | Demo |
| 480 | [Преобразование моделей САПР в инженерные чертежи](#case-480) | Demo |
| 481 | [43 задания по анализу данных от Plotly](#case-481) | Benchmark |
| 482 | [Воссоздание SGI Indy в браузере](#case-482) | Demo |
| 483 | [Координация агентов через задачи и рабочие деревья Git](#case-483) | Integration |
| 484 | [Проверка ссылок на публикации в фоновом режиме](#case-484) | Integration |
| 485 | [Отладка модели цен на перевозку в оба конца](#case-485) | Limit |
| 486 | [Адаптация запуска Edge0 для Mac](#case-486) | Integration |
| 487 | [Проверка компоновки плат с высокой плотностью монтажа](#case-487) | Limit |
| 488 | [Поиск источника цитаты в платном газетном архиве](#case-488) | Limit |
| 489 | [Планирование с Fable и проверка изменений Opus](#case-489) | Tutorial |

<a id="fable-5-2-cases"></a>
## Примеры использования

<a id="case-330"></a>
### Case 330: [Рисунок MacBook в SVG при разных уровнях усилий](https://playcode.io/blog/macbook-svg-benchmark#compare) (автор [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**На одном задании сравнивайте качество рисунка, расход токенов и предел вывода.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode сообщает, что Fable 5.2 в режиме High израсходовала 76 158 токенов за $3.05. В потоковом режиме Xhigh и Max достигли потолка в 128 000 токенов без готового рисунка. Оба режима завершили рисунок при большем лимите через Batch API. Порядок в рейтинге отражает визуальную оценку издателя.

[Дополнительные материалы 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [Игра beat ’em up на четверых по семейным рисункам](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (автор [Lex](https://notesbylex.com/))

**Дайте агенту эскизы, существующий прототип и конкретные требования к контроллерам.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex переработал с Claude Code прежнюю игру с боковой прокруткой в beat ’em up с 12 уровнями и 18 персонажами. Графику и звук создали отдельными инструментами. На семейном тесте работали четыре контроллера.

[Дополнительные материалы 1](https://aidens-revenge.pages.dev/) · [Дополнительные материалы 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [Дополнительные материалы 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [Три электронных устройства от проекта до сборки](https://www.anthropic.com/research/claude-electronics-design) (автор [@Anthropic](https://www.anthropic.com/))

**Проверяйте схему, корпус и прошивку как единую систему.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ Смотреть видео</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic и Diode сообщают о трёх работающих устройствах. Fable 5.2 выполнила разводку плат, смоделировала корпуса, написала ПО и помогла провести испытания после изготовления.

[Дополнительные материалы 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [Дополнительные материалы 2](https://www.youtube.com/watch?v=vdYynH177h0) · [Дополнительные материалы 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [Формализация Великой теоремы Ферма в Lean](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (автор [@Anthropic](https://www.anthropic.com/))

**Используйте проверку доказательств и формулировки промежуточных теорем как контрольные точки.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Anthropic сообщает, что команда из 1 000 агентов Fable 5.2 формализовала существующее доказательство за 30 часов. При той же организации команды Opus 5.5 достигла 26% за 18 часов.

[Дополнительные материалы 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [Дополнительные материалы 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [Операционная система из пустой папки](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (автор [@Anthropic](https://www.anthropic.com/))

**Отдельно проверяйте загрузку, драйверы, хранение данных и установку.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ Смотреть видео</a>

Anthropic сообщает, что Fable 5.2 за восемь дней скоординировала более 1 000 субагентов. Они создали прототип ОС, который загрузился на ноутбуке.

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [Манипуляции двумя роботизированными руками в RoboDojo](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (автор [@Anthropic](https://www.anthropic.com/))

**Сравнивайте модели на одних и тех же задачах манипуляции в симуляции.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ Смотреть видео</a>

По данным Anthropic, Fable 5.2 набрала 64,9%, а Fable 5.1 — 27,6% в RoboDojo. В публикации показана демонстрация робота.

[Дополнительные материалы 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [Фонтан в движении](https://x.com/Angaisb_/status/2119909059277238733) (автор [@Angaisb_](https://x.com/Angaisb_))

**Оцените визуальный ритм сцены по непрерывному движению воды.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

Автор показал сцену с фонтаном, созданную, по его словам, с Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [Покадровая синхронизация губ с Higgsfield](https://x.com/higgsfield_ai/status/2119909938969580024) (автор [@higgsfield_ai](https://x.com/higgsfield_ai))

**Синхронизируйте звук с точностью до кадра перед просмотром ролика.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ Смотреть видео</a>

Higgsfield сообщила, что использовала Fable 5.2 для отслеживания движений рта и покадровой привязки звука.

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [Прототип вождения в открытом мире](https://x.com/ericmaskfr/status/2119910195325481026) (автор [@ericmaskfr](https://x.com/ericmaskfr))

**Проверьте короткое задание на небольшом играбельном фрагменте.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал прототип игры по мотивам GTA и сообщил, что работа заняла около 2 часов 14 минут.

Исходный промпт

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [Париж 1940 года по референсам](https://x.com/higgsfield_ai/status/2119910344998912507) (автор [@higgsfield_ai](https://x.com/higgsfield_ai))

**Разделите генерацию референсов и создание сцены кодом.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ Смотреть видео</a>

Higgsfield предоставила изображения-референсы через свой MCP и использовала Fable 5.2 для сцены на Three.js.

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable планирует короткометражку, Opus её создаёт](https://x.com/kloss_xyz/status/2119910613828980846) (автор [@kloss_xyz](https://x.com/kloss_xyz))

**Разделите планирование и производство видео.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ Смотреть видео</a>

Fable 5.2 написала задание и план. Opus 5.5 сделала 16-секундную анимацию с Blender и Python и синтезировала музыку.

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [Эксперимент с музыкальным клипом](https://x.com/WesRoth/status/2119911161386934330) (автор [@WesRoth](https://x.com/WesRoth))

**Оцените и текст песни, и сгенерированный видеоряд.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился музыкальным клипом, созданным с Fable 5.2, и прокомментировал его текст.

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Живописный портрет Дарио Амодеи](https://x.com/Mr_Salio/status/2119911922577637543) (автор [@Mr_Salio](https://x.com/Mr_Salio))

**Сравните стилизованный портрет с показанным рядом референсом.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился портретом Дарио Амодеи, созданным, по его словам, с Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [Spud Smash в режиме Medium](https://x.com/argofowl/status/2119913148929187960) (автор [@argofowl](https://x.com/argofowl))

**Задайте игровому прототипу понятную цель и набор действий.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал персонажа-картофелину, который бьёт, таранит головой или поджигает синие стулья.

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Ледяной собор от Fable и Opus](https://x.com/QQTeng/status/2119913518015435103) (автор [@QQTeng](https://x.com/QQTeng))

**Сравните время и стоимость генерации одной и той же сцены.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ Смотреть видео</a>

По данным автора, Fable потратила около 1 часа 57 минут и $81.10, а Opus — около 3 часов 11 минут и $45.97.

Исходный промпт

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [Пение с имитацией речевого тракта](https://x.com/banteg/status/2119914098171199996) (автор [@banteg](https://x.com/banteg))

**Используйте физическую модель голоса при создании музыки.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился кавером, сделанным с двумя симуляциями речевого тракта Chimera и сведением через вокодер.

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [Три воксельных теста со Стамбулом](https://x.com/Avenoxai/status/2119914308603953485) (автор [@Avenoxai](https://x.com/Avenoxai))

**Сравните сцену разрушения, работающие часы и карту.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал три теста по одному запросу на каждый и выставил по собственной шкале 100, 100 и 95,6 балла.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Доля выполненных проектов в Remote Labor Index](https://x.com/ScaleAILabs/status/2119914701736075489) (автор [@ScaleAILabs](https://x.com/ScaleAILabs))

**Интерпретируйте процент в контексте конкретных оценённых проектов.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ Смотреть видео</a>

Scale Labs и CAIS сообщают, что Fable 5.2 успешно выполнила 41,3% оценивавшихся проектов удалённой работы.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [Сцена с айсбергом при четырёх уровнях усилий](https://x.com/0xRhinoX/status/2119915121698840587) (автор [@0xRhinoX](https://x.com/0xRhinoX))

**Сравните полноту, стоимость и детализацию при повышении уровня усилий.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ Смотреть видео</a>

Автор дал один и тот же запрос в четырёх режимах. High не показал полярное сияние, а Ultra добавил светящийся лёд и вид из-под воды.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [Аниме-ролик на 79 секунд](https://x.com/anstapnever/status/2119915123070644263) (автор [@anstapnever](https://x.com/anstapnever))

**Проверяйте непрерывность сцен в более длинной анимации.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился 79-секундным аниме-роликом, который, по его словам, создан с Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Механические сборки от Fable и Opus](https://x.com/ivanainai/status/2119915243321397550) (автор [@ivanainai](https://x.com/ivanainai))

**Сравните, как модели показывают расположение деталей в сборке.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал подписанные рендеры от Fable 5.2 и Opus 5.5 с разнесёнными деталями колеса и зубчатого узла.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [Роботизированная кисть поднимается по винтовой лестнице](https://x.com/Luckyballa/status/2119915557663506720) (автор [@Luckyballa](https://x.com/Luckyballa))

**Проверьте необычный способ передвижения на препятствии в симуляции.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал тест Fable 5.2 и Steel 0.1, в котором кисть Wuji передвигалась на пальцах.

[Дополнительные материалы 1](https://github.com/skild-ai/steel-webgpu/pull/7)

Исходный промпт

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [Оснастка модели Tripo в Blender](https://x.com/0xKense1/status/2119916096098582566) (автор [@0xKense1](https://x.com/0xKense1))

**Проверяйте захват, текстуры и деформацию по численным критериям.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ Смотреть видео</a>

Автор сравнил две оснастки для моделей из Tripo. Fable сделала два клипа за 36 минут, а Opus — восемь примерно за 21 минуту.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [Интерактивные изобретения из блокнота да Винчи](https://x.com/alexalbert__/status/2119916954337349737) (автор [@alexalbert__](https://x.com/alexalbert__))

**Создайте интерактивную учебную модель по исходным чертежам.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ Смотреть видео</a>

Alex Albert предоставил PDF с блокнотом Леонардо и поделился интерактивной интерпретацией его изобретений.

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [Музыкальная рабочая станция под управлением Claude](https://x.com/The_Alex/status/2119917226769985785) (автор [@The_Alex](https://x.com/The_Alex))

**Дайте агенту инструмент, к которому он сможет обращаться для новых композиций.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал цифровую звуковую рабочую станцию, созданную с Fable 5.2. По его словам, Opus позже открыл её, чтобы написать песню.

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [Анимированная Raspberry Pi 5](https://x.com/sparklabhq/status/2119917375080521921) (автор [@sparklabhq](https://x.com/sparklabhq))

**Оцените проработку компонентов в анимации продукта.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал анимированную Raspberry Pi 5, сделанную с Fable 5.2.

Исходный промпт

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [Сцена на севере Италии](https://x.com/Angaisb_/status/2119917807119089926) (автор [@Angaisb_](https://x.com/Angaisb_))

**Оцените пейзаж и атмосферу в задании с конкретным местом действия.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился сценой на севере Италии, созданной с Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [Книжка-панорама с локальными агентами](https://x.com/atomicagent_io/status/2119918110752846094) (автор [@atomicagent_io](https://x.com/atomicagent_io))

**На одной задаче сравните команду агентов с запуском одной модели.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ Смотреть видео</a>

По данным Atomic, Fable с локальными агентами Qwen выполнила работу за 11 минут и $2.98, а Fable самостоятельно — за 21 минуту и $15.77.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [Возвращение теста с лава-лампой](https://x.com/eidzoku/status/2119918134060601690) (автор [@eidzoku](https://x.com/eidzoku))

**Дайте нескольким моделям одну и ту же визуальную задачу.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ Смотреть видео</a>

Автор возобновил тест с лава-лампой и поделился сравнением сгенерированных вариантов.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [Детализированный реактивный самолёт в Blender](https://x.com/higgsfield_ai/status/2119918248955392431) (автор [@higgsfield_ai](https://x.com/higgsfield_ai))

**Укажите в задании количество деталей, длительность и внешний вид.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ Смотреть видео</a>

Higgsfield сообщила о модели Blender из 931 детали и 24 260 заклёпок, созданной скриптами с помощью Fable 5.2 и MCP от Higgsfield.

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [Путешествие через порталы в сотни миров](https://x.com/emollick/status/2119918307457577163) (автор [@emollick](https://x.com/emollick))

**Соединяйте независимо сгенерированные пространства порталами.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ Смотреть видео</a>

Итан Моллик сообщил, что 25 000 агентов создали кодом более 450 миров, и поделился играбельной сборкой и репозиторием.

[Дополнительные материалы 1](https://portals-endless-worlds.netlify.app/) · [Дополнительные материалы 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [Бомбейский базар в шести кадрах на Three.js](https://x.com/higgsfield_ai/status/2119918834841010320) (автор [@higgsfield_ai](https://x.com/higgsfield_ai))

**Разбейте визуальное задание на планы с заданной длительностью.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ Смотреть видео</a>

Higgsfield опубликовала сцену базара из шести планов общей длительностью 21,5 секунды, отрендеренную в Three.js.

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [Фотореалистичная закусочная, созданная кодом](https://x.com/higgsfield_ai/status/2119918838490010008) (автор [@higgsfield_ai](https://x.com/higgsfield_ai))

**Оцените материалы и освещение на сцене, целиком построенной кодом.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ Смотреть видео</a>

Higgsfield показала сцену с закусочной и сообщила, что создала её кодом без приложения для 3D-моделирования.

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [Модель робота в Blender](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (автор [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Покрутите модель, чтобы рассмотреть сочленения и силуэт.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал небольшого механического робота, созданного в демонстрации Fable 5.2 с Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [Анимационный ролик о Convex](https://x.com/Rasmic/status/2119919466163093768) (автор [@Rasmic](https://x.com/Rasmic))

**Объясните продукт для разработчиков с помощью короткой анимации.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился роликом о Convex, созданным с помощью Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [Подборка лендингов по одному запросу на каждый](https://x.com/daradoescode/status/2119919529807466594) (автор [@daradoescode](https://x.com/daradoescode))

**Сравните иерархию и компоновку по нескольким коротким заданиям.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился видеоподборкой лендингов, созданных с Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [Партитура фортепианной сонаты в LilyPond](https://x.com/imjustnewatai/status/2119919644836347926) (автор [@imjustnewatai](https://x.com/imjustnewatai))

**Сохраняйте связь между исходной партитурой и готовым видео.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ Смотреть видео</a>

Автор запросил музыкальную часть в стиле Бетховена и сообщил, что показанные ноты взяты из исходного файла LilyPond.

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [Видео по свободному заданию](https://x.com/aollivier82/status/2119920990893244510) (автор [@aollivier82](https://x.com/aollivier82))

**Дайте задание без визуальных ограничений, чтобы оценить творческий выбор модели.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ Смотреть видео</a>

Автор попросил Fable 5.2 сделать самое красивое видео, на которое способна модель, и поделился результатом.

Исходный промпт

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable планирует, DeepSeek реализует, Opus проверяет](https://x.com/ivanfioravanti/status/2119921810267636201) (автор [@ivanfioravanti](https://x.com/ivanfioravanti))

**Поручите координацию, реализацию и проверку разным агентам.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал, как Fable с помощью herdr координирует четырёх агентов DeepSeek V4.1 Flash, а Opus 5.5 проверяет пул-реквесты.

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [Fable 5.2 в AI Village](https://x.com/aidigest_/status/2119923190411719158) (автор [@aidigest_](https://x.com/aidigest_))

**Проверяйте отдельно ответ агента и его действия с памятью.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

Открытый журнал показывает, как Fable соглашается позже изменить память по просьбе другого агента. Связанный пост показывает тест на сходство с персонажами.

[Дополнительные материалы 1](https://x.com/aidigest_/status/2119923209311260707) · [Дополнительные материалы 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [Дизайн интерфейса с навыками и без них](https://x.com/AdamHoltererer/status/2119924849321914653) (автор [@AdamHoltererer](https://x.com/AdamHoltererer))

**Используйте одну модель и меняйте набор навыков.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

Автор показал два варианта интерфейса от Fable 5.2, один с навыками, другой без них.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [Поиск неявных конечных автоматов в коде](https://x.com/kunchenguid/status/2119924895060795492) (автор [@kunchenguid](https://x.com/kunchenguid))

**Проверьте конкретный модуль и попросите схемы до и после изменений.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

Автор показал упрощение в репозитории Firstmate и опубликовал точный запрос для аудита.

[Дополнительные материалы 1](https://github.com/kunchenguid/lavish-axi)

Исходный промпт

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [Игра с нуля за восемь часов](https://x.com/felixrieseberg/status/2119925633564463609) (автор [@felixrieseberg](https://x.com/felixrieseberg))

**Фиксируйте кэшированный ввод, сгенерированные ресурсы и полное время работы.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ Смотреть видео</a>

По словам инженера Anthropic, модели, звуки и текстуры были созданы за один прогон с эквивалентной стоимостью API около $550.

[Дополнительные материалы 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [Дополнительные материалы 2](https://x.com/AndrewCurran_/status/2119953960794780133)

Исходный промпт

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Прототип Fishslop и затраты на токены](https://x.com/theo/status/2119926277801144695) (автор [@theo](https://x.com/theo))

**Сравнивайте новую сборку игры с предыдущим результатом.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ Смотреть видео</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

Автор сообщил о 76 минутах и примерно $42 затрат на токены и сопоставил результат с Opus 5.5.

[Дополнительные материалы 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [Футбольная игра в движении](https://x.com/WesRoth/status/2119926801514529027) (автор [@WesRoth](https://x.com/WesRoth))

**Проверьте обратную связь и индикацию счёта в спортивном прототипе.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал игровой эпизод, созданный с Fable 5.2, с экранной индикацией набранных очков.

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [Бой с боссом в открытом мире с Higgsfield MCP](https://x.com/higgsfield_ai/status/2119926932343324795) (автор [@higgsfield_ai](https://x.com/higgsfield_ai))

**Оценивайте игровой процесс и кат-сцены отдельно.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ Смотреть видео</a>

Higgsfield сообщила о браузерной игре с открытым миром, боем с боссом в три этапа и кат-сценами, созданными с Fable 5.2 и её MCP.

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [Мон-Сен-Мишель с приливами и отливами](https://x.com/loktar00/status/2119927152489472076) (автор [@loktar00](https://x.com/loktar00))

**Проверьте изменение уровня воды в небольшой исторической сцене.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал миниатюру Мон-Сен-Мишеля с анимированными приливами и отливами.

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [Игровой объект для Roblox в Blender](https://x.com/hiyouwhatsapp/status/2119927163264573642) (автор [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**Проверьте игровой объект в Blender перед импортом.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился результатом разработки для Roblox, полученным в Blender почти за один запрос.

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [Рассуждение без вывода цепочки мыслей](https://x.com/Tim_Hua_/status/2119927284761293089) (автор [@Tim_Hua_](https://x.com/Tim_Hua_))

**Оценивайте ответы при одинаковом ограничении на вывод рассуждений.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

Автор проверил знания и рассуждения без вывода цепочки мыслей и сообщил, что Fable 5.2 немного уступила GPT-6.1 Sol.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [Версии Chrome Dino от четырёх моделей](https://x.com/noclipepe/status/2119927838321328577) (автор [@noclipepe](https://x.com/noclipepe))

**Сравнивайте время и стоимость на одном игровом задании.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ Смотреть видео</a>

Автор добавил Fable 5.2 к своему тесту с тираннозавром для Opus, Gemini и Astra и показал результаты вместе.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [Шашки с роботизированной рукой](https://x.com/karolina_dubiel/status/2119928342115676576) (автор [@karolina_dubiel](https://x.com/karolina_dubiel))

**Считывайте положения шарниров и повторяйте неудачные захваты.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ Смотреть видео</a>

По словам автора, модель компенсировала провисание примерно на 7 мм и использовала обратную связь, чтобы повторить неудачные ходы.

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [Пятнадцатисекундный анимационный ролик](https://x.com/aziz4ai/status/2119928581405200726) (автор [@aziz4ai](https://x.com/aziz4ai))

**Следите за тем, сколько лимита расходует короткая анимация, созданная кодом.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал 15-секундную сцену, созданную кодом, и сообщил о расходе 4% недельного лимита.

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [Интерактивная сцена с Эйфелевой башней](https://x.com/bobyau/status/2119928812628771212) (автор [@bobyau](https://x.com/bobyau))

**Проверьте, поддерживает ли модель достопримечательности взаимодействие.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал демонстрацию Эйфелевой башни и сообщил, что создание заняло 25 минут.

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [Гонки в открытом море с Three.js и Higgsfield](https://x.com/higgsfield_ai/status/2119928918035910668) (автор [@higgsfield_ai](https://x.com/higgsfield_ai))

**Разделите игровую логику и инструменты работы с медиа.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ Смотреть видео</a>

Higgsfield показала гонку с большими волнами, пятью соперниками под управлением ИИ и самонаводящимися ракетами.

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [Симуляция мёда в реальном времени на WebGL](https://x.com/deedydas/status/2119930300990177509) (автор [@deedydas](https://x.com/deedydas))

**Проверяйте движение материала с помощью физической симуляции в браузере.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал симуляцию мёда в реальном времени на WebGL и опубликовал исходное короткое задание.

Исходный промпт

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [Программно созданные визуальные эффекты для видео](https://x.com/ashebytes/status/2119930763105931649) (автор [@ashebytes](https://x.com/ashebytes))

**Проверьте время появления и расположение эффектов на исходных кадрах.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал эксперимент с Fable 5.2, в котором анимированная графика наложена на видеосъёмку.

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [Анимация о звёздах розыска в GTA](https://x.com/saimagnate/status/2119931563760632311) (автор [@saimagnate](https://x.com/saimagnate))

**Сочетайте игровые кадры и схемы, чтобы объяснить механику.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ Смотреть видео</a>

Автор сообщает о результате одного запроса к Fable 5.2. В ролике игровые кадры и схемы сопоставляют системы розыска GTA V и RDR2.

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [Стилизованный мир MMO, созданный кодом](https://x.com/Izkimar/status/2119931740940640542) (автор [@Izkimar](https://x.com/Izkimar))

**Оцените, выдержан ли общий стиль игровых объектов.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ Смотреть видео</a>

Автор сообщил, что создал показанный мир MMO за один день, генерируя игровые объекты кодом.

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [3D-сцена от Fable и Opus](https://x.com/dom_scholz/status/2119933150025363661) (автор [@dom_scholz](https://x.com/dom_scholz))

**Сопоставьте время подготовки и детализацию результата.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал рендеры Fable 5.2 и Opus 5.5 рядом и сообщил, что прогон Fable был быстрее.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [Избыточный текст на экране паузы игры](https://x.com/AndrewPrifer/status/2119934600608915465) (автор [@AndrewPrifer](https://x.com/AndrewPrifer))

**Проверьте сгенерированные надписи на повторяющиеся пояснения.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

Разработчик привёл экран паузы как пример того, что Fable 5.2 добавляет больше пояснений, чем нужно.

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [Мудборды в среде Krea](https://x.com/lambdacalcc/status/2119934725662060663) (автор [@lambdacalcc](https://x.com/lambdacalcc))

**Сравните концепции, прежде чем выбирать визуальное направление.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

Автор показал четыре варианта мудборда из сессии Fable 5.2 в среде Krea.

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [Офисное тестирование шутера с порталами](https://x.com/_sholtodouglas/status/2119935331499925557) (автор [@_sholtodouglas](https://x.com/_sholtodouglas))

**Проводите многопользовательские тесты сгенерированных игр.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ Смотреть видео</a>

Инженер Anthropic показал аренный шутер от первого лица с порталами и описал офисные игровые тесты.

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Детализированный твердотельный объект в Blender](https://x.com/ziwenxu_/status/2119937420280168929) (автор [@ziwenxu_](https://x.com/ziwenxu_))

**Изучите топологию и силуэт в окне Blender.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал детализированный твердотельный объект и представил его как результат работы Fable 5.2 в Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [Параллельные тесты интерфейсов при разных уровнях усилий](https://x.com/AI_masaou/status/2119937635322085640) (автор [@AI_masaou](https://x.com/AI_masaou))

**Сравнивайте простые и сложные задания при нескольких настройках.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

По словам автора, на простых заданиях Fable и Opus показали похожие результаты, а в крупных проектах Fable проработала больше деталей. При переходе от Medium к High время и расход токенов резко выросли.

[Дополнительные материалы 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [Небольшая игра за десять запросов](https://x.com/AmirMushich/status/2119937977426338283) (автор [@AmirMushich](https://x.com/AmirMushich))

**Фиксируйте число итераций и размер игрового прототипа.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ Смотреть видео</a>

Автор сообщил об игре размером 220 КБ и примерно 3 400 строках кода, а также опубликовал код и видео.

[Дополнительные материалы 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [Покадровая анимация на JavaScript](https://x.com/kevin_t_ngo/status/2119938129079808282) (автор [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Оцените последовательность кадров, отрисованных программно.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился анимацией и сообщил, что каждый кадр был нарисован с помощью JavaScript.

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [3D-анимация по видеореференсу](https://x.com/KHvostikk/status/2119939061049889130) (автор [@KHvostikk](https://x.com/KHvostikk))

**Сверяйте воссозданную сцену с исходным видео.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал, как с Fable 5.2 превратил видеореференс в 3D-анимацию.

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Пиксельный костёр от Fable и Opus](https://x.com/GrilliotTodd/status/2119939651385655692) (автор [@GrilliotTodd](https://x.com/GrilliotTodd))

**Сравните освещение и силуэты на одном сюжете.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ Смотреть видео</a>

На сравнении рядом показаны версии одного костра от Fable 5.2 и Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [Arena WebDev в режиме xHigh](https://x.com/arena/status/2119941204003770690) (автор [@arena](https://x.com/arena))

**Учитывайте конкретный уровень усилий, указанный в рейтинге.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena сообщает, что Claude Fable 5.2 в режиме xHigh дебютировала с результатом 1 832 балла в Code Arena WebDev.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [Типографика кинотрейлера от двух моделей](https://x.com/muku_sns/status/2119941490969624679) (автор [@muku_sns](https://x.com/muku_sns))

**Сравните две интерпретации одного абзаца.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал титры от Opus и Fable рядом. В версии Fable появились мотив красной рамки и частично скрытые заголовки.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [Моушн-дизайн и 3D по одному запросу на проект](https://x.com/Khazix0918/status/2119941585538572390) (автор [@Khazix0918](https://x.com/Khazix0918))

**Проверяйте исследование, дизайн и рендеринг как отдельные части творческого задания.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ Смотреть видео</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ Смотреть видео</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ Смотреть видео</a></td></tr></table>

Автор показал юбилейный ролик о ChatGPT, объясняющее видео о DeepSeek, сцену на Three.js и 3D-реконструкцию магазина Apple Jing’an, полученные в четырёх прогонах.

[Дополнительные материалы 1](https://x.com/Khazix0918/article/2119941585538572390)

Исходный промпт

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [Интерактивное объяснение устройства ядерного реактора](https://x.com/konstantinsaifo/status/2119941967136379334) (автор [@konstantinsaifo](https://x.com/konstantinsaifo))

**Дайте зрителю разобрать модель, чтобы показать, как соединяются детали.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ Смотреть видео</a>

Автор запросил разборную модель реактора на Three.js и сообщил о затратах на API в размере $92.

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Агенты в Blood on the Clocktower](https://x.com/dwarkesh_sp/status/2119942657812451482) (автор [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**Сравнивайте модели в одной и той же игре со скрытыми ролями.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

Автор теста сообщает, что Fable 5.2 опередила Fable 5.1 и Opus 5.5, а GPT-6 Astra показала ещё более высокий результат.

[Дополнительные материалы 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [Прототип гонок на подах](https://x.com/loktar00/status/2119943124965638444) (автор [@loktar00](https://x.com/loktar00))

**Возьмите знакомый формат гонки, чтобы оценить движение и управление.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал результат Fable 5.2 в стиле гонок на подах.

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [Десятисекундная реклама белья Claude](https://x.com/Masimo_Blue/status/2119943368612487285) (автор [@Masimo_Blue](https://x.com/Masimo_Blue))

**Испытайте свободное задание для рекламы продукта с оригинальной музыкой.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ Смотреть видео</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

Автор поделился десятисекундным роликом в сопровождении эйсид-техно, в котором использовал предоставленные изображения продукта.

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [Птица на рассвете, мазок за мазком](https://x.com/mgrczyk/status/2119943813028548721) (автор [@mgrczyk](https://x.com/mgrczyk))

**Отключите отмену, чтобы проследить решения модели в процессе рисования.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал картину с птицей на рассвете. Модель рисовала мазок за мазком в среде, где нельзя было изменить уже нанесённое.

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [Длительный графический прогон в Devin](https://x.com/Da7_Tech/status/2119944847255896490) (автор [@Da7_Tech](https://x.com/Da7_Tech))

**Записывайте время и затраты на сложный рендер.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ Смотреть видео</a>

Автор указал, что он амбассадор Cognition, и сообщил, что прогон в Devin Max занял примерно 3,5 часа и стоил около $82.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [Живопись кодом в трёх моделях](https://x.com/kickingkeys/status/2119945841997672698) (автор [@kickingkeys](https://x.com/kickingkeys))

**Сравнивайте движение кисти и синтезированный звук в разных прогонах.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал рисунок и звук, созданные кодом, и описал тесты с одинаковым запросом для Fable 5.2, Fable 5.1 и Gemini 4 Argon.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [История письменности в анимации](https://x.com/rileybrown/status/2119946022767980985) (автор [@rileybrown](https://x.com/rileybrown))

**Постройте объясняющий ролик вокруг хронологии.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал анимацию об истории письменности и сообщил, что она создана по одному запросу.

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [Полигон для игровых механизмов](https://x.com/techartist_/status/2119946891106394518) (автор [@techartist_](https://x.com/techartist_))

**Проверяйте механику, физику и эффекты в общей тестовой сцене.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ Смотреть видео</a>

Автор создал в Three.js и Blender полигон для четырёх концепций.

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [Печатная плата портативной консоли на Linux](https://x.com/seveibar/status/2119947341230907453) (автор [@seveibar](https://x.com/seveibar))

**Сравнивайте проекты плат по одному и тому же заданию.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ Смотреть видео</a>

Создатель tscircuit показал, как Astra 6 High и Fable 5.2 High справились с проектом портативной игровой консоли на Linux.

Исходный промпт

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [Воксельная сцена с озером](https://x.com/Angaisb_/status/2119947748690841841) (автор [@Angaisb_](https://x.com/Angaisb_))

**Возьмите небольшую сцену, чтобы оценить композицию.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал воксельное озеро, созданное, по его словам, с Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [17 интерактивных работ от Arena](https://x.com/arena/status/2119948067449536733) (автор [@arena](https://x.com/arena))

**Посмотрите разные виды результатов перед выбором тестовой задачи.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ Смотреть видео</a>

Arena опубликовала 17 работ: 3D-миры, игры, интерфейсы, визуализации данных и анимацию, созданную кодом.

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [Полёт с дружелюбным драконом](https://x.com/chetanankola/status/2119951015407738913) (автор [@chetanankola](https://x.com/chetanankola))

**Проверьте камеру и движение на повторяющемся маршруте полёта.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал сцену с драконом на Three.js и Blender и описал улучшения, сделанные с Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Желейная косатка от Fable и Opus](https://x.com/vib3coded/status/2119951060752375827) (автор [@vib3coded](https://x.com/vib3coded))

**Сравнивайте поверхность и движение на одном объекте.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал рядом две версии желейной косатки от Fable 5.2 и Opus 5.5.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [Открытая проверка качества видео](https://x.com/suna_gaku/status/2119952985933697063) (автор [@suna_gaku](https://x.com/suna_gaku))

**Дайте свободное творческое задание, чтобы оценить решения модели.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ Смотреть видео</a>

Автор попросил модель показать её лучшую работу с видео и поделился результатом.

Исходный промпт

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [Космическая станция в средиземноморском стиле](https://x.com/MaxXWilliamson/status/2119953172634677533) (автор [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**Дополните короткое задание проверенными инструментами проекта.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ Смотреть видео</a>

Автор предоставил инструменты из предыдущих проектов космических станций и попросил создать станцию в средиземноморском стиле.

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [Бенчмарк интерактивных 3D-сцен AA-3D](https://x.com/ArtificialAnlys/status/2119953570430881946) (автор [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Учитывайте интервал неопределённости при чтении рейтинга Elo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ Смотреть видео</a>

Artificial Analysis сообщает, что на момент запуска Fable 5.2 Max набрала 1 271 балл Elo в бенчмарке интерактивных 3D-сцен.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [Игровое испытание со скелетом на время](https://x.com/WesRoth/status/2119953913160093817) (автор [@WesRoth](https://x.com/WesRoth))

**Используйте видимый таймер при тестировании игрового прототипа.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал результат одного запроса к Fable 5.2: скелета и таймер обратного отсчёта на экране.

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Пиксель-арт от Fable и Astra](https://x.com/Angaisb_/status/2119955179915137294) (автор [@Angaisb_](https://x.com/Angaisb_))

**Сравнивайте формы и детали в одном масштабе.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ Смотреть видео</a>

В исходном сравнении показан пиксель-арт, созданный GPT-6 Astra и Fable 5.2.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [Портфолио-ролик с моушн-дизайном](https://x.com/Leviwoyun/status/2119955625820258308) (автор [@Leviwoyun](https://x.com/Leviwoyun))

**Дайте свободное творческое задание и задайте длительность ролика.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал анимационный ролик с музыкой и сообщил, что работа заняла 24 минуты.

Исходный промпт

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [Рендер бассейна со стеклом в двух моделях](https://x.com/MrTacticalX/status/2119955647542542439) (автор [@MrTacticalX](https://x.com/MrTacticalX))

**Сравнивайте освещение вместе со временем и стоимостью рендера.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ Смотреть видео</a>

По данным автора, Fable понадобилось 90 минут и $57.87, а Opus — 68 минут и $14.39.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [Точность вызова инструментов в TS-Bench](https://x.com/gosrum/status/2119956559031927079) (автор [@gosrum](https://x.com/gosrum))

**Измеряйте ошибки вызова инструментов отдельно от расхода токенов.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

По данным автора теста, Fable 5.2 не допустила ошибок вызова инструментов. На простых задачах различия между версиями Claude были небольшими.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [Миниатюрный мир Мачу-Пикчу](https://x.com/loktar00/status/2119958719362666708) (автор [@loktar00](https://x.com/loktar00))

**Оцените атмосферу и мелкие детали в миниатюрной сцене.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ Смотреть видео</a>

В демонстрации Мачу-Пикчу видны объёмный туман и маленькие альпаки.

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [GDPx по категориям профессиональных задач](https://x.com/SemiAnalysis_/status/2119961447199289640) (автор [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**Смотрите результаты отдельных категорий вместе с общим баллом.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

Издатель бенчмарка приводит общий результат 16,4% и оценки по областям, в том числе по проектированию чипов и разработке ПО.

[Дополнительные материалы 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [Дополнительные материалы 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [Дополнительные материалы 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [Портрет в графическом редакторе](https://x.com/The_Alex/status/2119964472559489229) (автор [@The_Alex](https://x.com/The_Alex))

**Используйте миниатюру референса при создании портрета.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ Смотреть видео</a>

Автор попросил Fable 5.2 открыть редактор и нарисовать его портрет. Видео показывает работу от контуров до готового рисунка.

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [VulcanBench Frontier v4 в режиме Low](https://x.com/morganlinton/status/2119966067527467215) (автор [@morganlinton](https://x.com/morganlinton))

**Сравнивайте поколения моделей при одинаковом уровне усилий.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

Автор бенчмарка сообщает, что в режиме Low Fable 5.2 тратила около 5 минут на задачу, а Fable 5.1 — около 26 минут.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [Играбельные Backrooms со сменой ролей](https://x.com/LexnLin/status/2119966127149429093) (автор [@LexnLin](https://x.com/LexnLin))

**Поменяйте цель игрока, чтобы проверить игровую концепцию.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ Смотреть видео</a>

Игрок управляет монстром и пытается ловить людей. Автор поделился записью игрового процесса и ссылкой на игру.

[Дополнительные материалы 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [Bugatti Tourbillon в Blender](https://x.com/xikhar/status/2119966147328299284) (автор [@xikhar](https://x.com/xikhar))

**Используйте референсы, чтобы задать детали кузова и салона.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ Смотреть видео</a>

По словам автора, он смоделировал Bugatti Tourbillon вместе с салоном и отрендерил ролик, опираясь на запрос и референсы.

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [Ролик о компьютерах, созданный двумя моделями](https://x.com/daradoescode/status/2119966154391183522) (автор [@daradoescode](https://x.com/daradoescode))

**Фиксируйте вклад каждой модели в совместной работе.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал стилизованный ролик, созданный с Fable 5.2 при значительной помощи Opus 5.5.

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [Музыкальный клип о мегаядрах](https://x.com/elliotarledge/status/2119968762069934415) (автор [@elliotarledge](https://x.com/elliotarledge))

**Возьмите техническое понятие за тему ролика.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ Смотреть видео</a>

Автор попросил Fable 5.2 в режиме High сделать музыкальный клип о мегаядрах и поделился результатом.

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [Экскурсия по студии на основе фотографий](https://x.com/rpnickson/status/2119969928304357507) (автор [@rpnickson](https://x.com/rpnickson))

**Дайте реальные фотографии для точного воссоздания пространства.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ Смотреть видео</a>

Автор загрузил фотографии студии, адаптировал похожее задание для видео и сообщил, что работа заняла около двух часов.

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [Реклама игрушек в духе 1990-х, созданная кодом](https://x.com/kevin_t_ngo/status/2119972124211454139) (автор [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Разделите программирование анимации и рендеринг.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ Смотреть видео</a>

По словам автора, анимацию для ретроролика он написал на Python, а отрендерил её в Blender.

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Игровая сцена от третьего лица на Three.js](https://x.com/bijanbowen/status/2119972220739187182) (автор [@bijanbowen](https://x.com/bijanbowen))

**Оцените движение персонажа и окружение во время игры.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

Автор поделился фрагментом трансляции со сценой на Three.js, в которой персонаж перемещается по открытому пространству.

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [Bryceball на основе готового рендерера](https://x.com/pleometric/status/2119973274402668852) (автор [@pleometric](https://x.com/pleometric))

**Возьмите существующий рендерер за основу игры.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ Смотреть видео</a>

Автор превратил рендерер из публикации по ссылке в играбельный проект Bryceball.

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [Видеомонтаж с Fable на материале предыдущей работы](https://x.com/rileybrown/status/2119973951027724385) (автор [@rileybrown](https://x.com/rileybrown))

**Возьмите предыдущий монтаж за основу следующего ролика.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ Смотреть видео</a>

Автор поделился роликом, смонтированным в Fable 5.2, о более раннем видео, которое тоже монтировал с этой моделью.

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [История науки в кинематографичной 3D-сцене](https://x.com/DeryaTR_/status/2119974354260013293) (автор [@DeryaTR_](https://x.com/DeryaTR_))

**Задайте хронологию, чтобы выстроить последовательность 3D-сцен.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ Смотреть видео</a>

Автор попросил показать путь от зарождения науки до воображаемого будущего и поделился получившимся роликом.

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [Летательный аппарат да Винчи в 3D](https://x.com/higgsfield_ai/status/2119975721909301684) (автор [@higgsfield_ai](https://x.com/higgsfield_ai))

**Смоделируйте историческую конструкцию, прежде чем испытывать изменения.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ Смотреть видео</a>

Higgsfield показала 3D-версию летательного аппарата Леонардо и описала физическое испытание и переработку конструкции.

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [Трассировка печатной платы по техническому заданию](https://x.com/cmonkey/status/2119975852977029365) (автор [@cmonkey](https://x.com/cmonkey))

**Проверьте разводку платы перед изготовлением.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

В продолжение обсуждения разводки автор показал результат трассировки печатной платы с Fable 5.2.

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [Один запрос в разных средах запуска](https://x.com/loktar00/status/2119980613369319706) (автор [@loktar00](https://x.com/loktar00))

**Фиксируйте различия в средах запуска при сравнении ответов моделей.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ Смотреть видео</a>

Автор дал DeepSeek и Fable 5.2 один и тот же запрос в разных средах и показал результаты рядом.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [Годзилла, нарисованный кодом](https://x.com/chetaslua/status/2119981510199808368) (автор [@chetaslua](https://x.com/chetaslua))

**Переосмыслите изображение с помощью векторных форм и движения.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ Смотреть видео</a>

Автор показал рисунок, созданный кодом, и короткую анимацию по мотивам публикации о Годзилле.

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [Ручной вентилятор для 3D-печати](https://x.com/davelee/status/2119981787325579398) (автор [@davelee](https://x.com/davelee))

**Проверьте смоделированную сборку на физическом прототипе.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ Смотреть видео</a>

Автор вместе с детьми спроектировал ручной вентилятор для 3D-печати и поделился моделью перед печатью.

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [Поиск ошибок в плагине с Fable и Opus](https://x.com/oaranda/status/2119982729747919096) (автор [@oaranda](https://x.com/oaranda))

**Проверяйте исправления регрессионными тестами, составленными в другом прогоне.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

Фрагмент анонса с пометками автора.

Обе модели нашли одни и те же шесть ошибок в плагине. Opus прошла перекрёстные проверки, а Fable не прошла один тест и обнаружила ещё одну проблему на панели управления.

Исходный промпт

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [Стамбул, воссозданный в 3D](https://x.com/petergostev/status/2119877733488394520) (автор [@petergostev](https://x.com/petergostev))

**Рассмотрите городскую сцену с дальних и ближних ракурсов.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ Смотреть видео</a>

Питер Гостев показал 3D-версию Стамбула от Fable 5.2 Max и дал ссылку на подробное сравнение.

[Дополнительные материалы 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [Ролик о студии в Blender с работающим экраном](https://x.com/rileybrown/status/2119902109709537708) (автор [@rileybrown](https://x.com/rileybrown))

**Анимируйте экран, освещение и камеру в одной 3D-сцене.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ Смотреть видео</a>

Автор сообщил о 13 планах, специально созданной веб-странице на экране ноутбука и звуке от ElevenLabs. Для рендера использовались графические процессоры RunPod.

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [Переход с образованием чёрных дыр при слабой связи](https://hexagonmath.org/2611.00175v1) (автор [@Anthropic](https://www.anthropic.com/))

**Сверяйте незавершённый расчёт с исходной теоретической постановкой.**

Anthropic сообщает, что Fable 5.2 завершила давний расчёт и обнаружила резкий переход в режиме слабой связи. Вывод приведён в препринте.

[Дополнительные материалы 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [Предел оценки в модульном бутстрепе](https://hexagonmath.org/2611.00174v1) (автор [@Anthropic](https://www.anthropic.com/))

**Публикуйте вывод вместе с заявленной аналитической оценкой.**

Anthropic сообщает, что Fable 5.2 определила точный предел метода модульного бутстрепа для случая нулевого спина в упрощённой постановке квантовой гравитации.

[Дополнительные материалы 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Резервные модели по порядку в Vercel AI Gateway](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (автор [Vercel](https://vercel.com/))

**Настройте порядок резервных моделей для запросов, отклонённых классификатором.**

Пример Vercel AI SDK обращается к anthropic/claude-fable-5.2 и назначает Opus 5.5, затем Sonnet 5.5 резервными моделями. В руководстве указано требование шлюза к хранению данных.

[Дополнительные материалы 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [Вложенные субагенты и бюджет проверки кода](https://news.ycombinator.com/item?id=50430925) (автор [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**Отслеживайте вложенное делегирование и ограничивайте бюджет средствами среды запуска.**

Для проверки 80 000 строк кода автор запросил не более четырёх субагентов. По его словам, запустилось шесть или больше вложенных агентов, а лимит на пять часов закончился менее чем за 20 минут.

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [Перенос дизайна LCARS в HTML](https://news.ycombinator.com/item?id=50430962) (автор [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**Проверяйте кривые, точность иконок, анимацию и навигацию по отдельности.**

Автор сравнил Fable 5.2 и Opus 5.5 на одном дизайне в стиле Star Trek. Ему больше понравились кривые и некоторые иконки Fable, а также анимация Opus. Мерцание SVG в версии Fable отвлекало. Автор просил сделать только первую страницу.

[Дополнительные материалы 1](https://html.non.io/lcars-fable-5.2/) · [Дополнительные материалы 2](https://html.non.io/lcars-opus-5.5/) · [Дополнительные материалы 3](https://news.ycombinator.com/item?id=50431231) · [Дополнительные материалы 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [Оптимизация Quantum ESPRESSO для GPU](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (автор [Discovered Materials](https://discoveredmaterials.com/))

**Требуйте эталонные результаты и репрезентативные скрытые тесты при оптимизации научного кода.**

Discovered Materials сообщает об ускорении в 36 раз по среднему геометрическому на 13 фононных тестах на одном и том же GPU и примерно в 9 раз для расчётов с гибридными функционалами. Опубликованный патч проверен тестами корректности и производительности.

[Дополнительные материалы 1](https://github.com/discovered-materials/dm_qe) · [Дополнительные материалы 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [Индекс Artificial Analysis при разных уровнях усилий](https://artificialanalysis.ai/models/claude-fable-5-2) (автор [Artificial Analysis](https://artificialanalysis.ai/))

**Учитывайте оценку, стоимость и длительность задачи для выбранного режима.**

В приведённом срезе для Max со стандартным резервным переключением указаны 65 баллов, $26.54 и 46,4 минуты на задачу. Эти числа относятся к задачам бенчмарка.

[Дополнительные материалы 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [Ложные срабатывания при проверке изменений в режиме High](https://news.ycombinator.com/item?id=50431810) (автор [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**Сверяйте замечания модели с кодом перед исправлением.**

Разработчик сообщил, что Fable 5.2 в режиме High указала на две несуществующие проблемы в изменении. Он обнаружил ошибки в замечаниях благодаря знанию кода.

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [Тридцать повседневных задач по программированию](https://news.ycombinator.com/item?id=50432483) (автор [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**Измеряйте время и число успешно решённых задач на одном наборе.**

По данным автора, Fable 5.2 и Opus 5.5 решили по 26 из 30 задач, а Fable 5.1 — 25. Fable 5.2 потребовалось 0,62 от времени Fable 5.1. Автор не отметил остановок из-за защитных механизмов.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [Заставка о робинзоне на необитаемом острове](https://news.ycombinator.com/item?id=50432836) (автор [@nzach](https://news.ycombinator.com/user?id=nzach))

**Откройте интерактивную страницу, чтобы оценить заставку в работе.**

Автор публикации Show HN дал ссылку на браузерную сцену Stranded with Claude. Она опубликована как интерактивный холст.

[Дополнительные материалы 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [Три браузерные игры в режиме High](https://senko.net/vibecode-bench/) (автор [Senko Rašić](https://senko.net/))

**Оценивайте игровой процесс и визуальное соответствие отдельно.**

Сенко Рашич дал Fable 5.2 в Claude Code задания на стратегию в реальном времени, воксельную игру и авиасимулятор. По его словам, модели удалось добавить более глубокую механику, например дирижабль для исследования всей карты, хотя часть графики ему понравилась меньше.

[Дополнительные материалы 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [Сценарии книжного подкаста по главам](https://news.ycombinator.com/item?id=50434156) (автор [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**Сравните объём сценариев, созданных по одному и тому же заданию.**

Автор генерировал диалоги двух книжных обозревателей отдельно для каждой главы. По его словам, версии Fable занимали около 2,5 страницы, а версии Opus 5.5 — около 4,5. Он дал ссылки на оба примера.

[Дополнительные материалы 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [Дополнительные материалы 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [Перенос рабочего сервиса на Rust](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (автор [@Anthropic](https://www.anthropic.com/))

**Измерьте время запуска до и после миграции.**

По данным Anthropic, агенты с предварительной версией Fable 5.2 переписали рабочий сервис с Python на Rust. Время запуска сократилось примерно в 26 раз.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [Выбор Fable 5.2 в GitHub Copilot](https://x.com/github/status/2119926269982961833) (автор [@github](https://x.com/github))

**Включите политику организации перед выбором модели.**

GitHub описывает переключатель моделей Copilot и настройку администратора для аккаунтов Business и Enterprise.

[Дополнительные материалы 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [Испытание на сто вариантов HTML-дизайна](https://x.com/MiaAI_lab/status/2119930229661503893) (автор [@MiaAI_lab](https://x.com/MiaAI_lab))

**Оценивайте число завершённых и работающих файлов наряду с визуальным качеством.**

Автор запросил 100 разных дизайнов и опубликовал 76 файлов с запросами. По его словам, эксперимент упёрся в лимит использования Fable.

[Дополнительные материалы 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [Дополнительные материалы 2](https://mia-ai.net/lab/experiments/100-htmls) · [Дополнительные материалы 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [Дополнительные материалы 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [Дополнительные материалы 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [Дополнительные материалы 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [Дополнительные материалы 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [Дополнительные материалы 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [Дополнительные материалы 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [Дополнительные материалы 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [Дополнительные материалы 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [Дополнительные материалы 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [Дополнительные материалы 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [Дополнительные материалы 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [Искажение требований в задаче для компилятора](https://x.com/sameQCU/status/2119939304864800971) (автор [@sameQCU](https://x.com/sameQCU))

**Сверяйте требования в пересказе агента с исходным заданием.**

Разработчик описал задачу для компилятора, в которой Fable 5.2 и ранние модели Opus неверно передали полученные требования.

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [Наблюдение за долгой задачей Fable через Opus](https://x.com/marouane53/status/2119950129767858262) (автор [@marouane53](https://x.com/marouane53))

**Отслеживайте длинную задачу в отдельной сессии.**

Автор сообщает, что некоторые задачи Fable шли больше двух часов с редкими обновлениями. В отдельном чате Opus 5.5 объяснял ход работы и решения.

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [Повторная проверка кода свежим взглядом](https://x.com/doodlestein/status/2119958895158292786) (автор [@doodlestein](https://x.com/doodlestein))

**Отдельно просмотрите новые и изменённые файлы после реализации.**

Автор приводит два точных запроса для повторного поиска и исправления ошибок в готовом коде.

Исходный промпт

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

Исходный промпт

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [Уход от текущего проекта при проверке функции](https://news.ycombinator.com/item?id=50434214) (автор [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**Сверяйте повторные рекомендации агента с уже принятыми проектными решениями.**

Автор сравнил модели при проверке проекта новой функции и предпочёл Opus 5.5. При повторной проверке Fable 5.2 предложила решение, которое уже было в проекте.

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [Сравнение игр в духе DX Ball](https://news.ycombinator.com/item?id=50434424) (автор [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**Проверяйте механику и ощущения от игры по одному заданию на воссоздание.**

Автор дал ссылки на версии Fable 5.2 и Opus 5.5 из разных прогонов. Fable изменила часть исходной механики, а по ощущениям автору больше понравилась версия Opus.

[Дополнительные материалы 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [Дополнительные материалы 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [Попытка улучшить 3D-приложение](https://news.ycombinator.com/item?id=50434433) (автор [@user43928](https://news.ycombinator.com/user?id=user43928))

**Сравнивайте видимые изменения и расход лимита на одном задании по доработке.**

Автор попросил Fable 5.2 улучшить неигровое 3D-приложение. По его словам, результат мало отличался от Opus 5.5, а за вечер ушло 25% лимита Fable по тарифу.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [Игра про мышь и кошку от трёх моделей](https://news.ycombinator.com/item?id=50434508) (автор [@simonw](https://news.ycombinator.com/user?id=simonw))

**Дайте моделям один запрос и проверьте каждую играбельную версию.**

Саймон Уиллисон показал мобильные игры на Three.js от Fable 5.2 Extra, Opus 5.5 Extra и GPT-6 Extra High. По его словам, работа Fable заняла около 40 минут.

[Дополнительные материалы 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [Дополнительные материалы 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [Дополнительные материалы 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

Исходный промпт

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [Сравнение оценок и стоимости в AIBenchy при High](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (автор [AIBenchy](https://aibenchy.com/))

**Сравнивайте оценку, полную стоимость и время ответа при одном уровне усилий.**

По опубликованным данным AIBenchy, Fable 5.2 High и Opus 5.5 High набрали 8,7 и 9,4 балла, стоили $5.083 и $2.133 и отвечали в среднем за 14,73 и 27,55 секунды соответственно.

[Дополнительные материалы 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [Настройка среды агентов для Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (автор [@Anthropic](https://www.anthropic.com/))

**Заново проверьте уровни усилия и настройте отчёты о ходе работы.**

Руководство Anthropic приводит примеры инструкций для уровней усилия, критериев завершения, согласований, отчётов и ограничений субагентов.

[Дополнительные материалы 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="case-469"></a>
### Case 469: [Приложение для просмотра анимированных персонажей](https://x.com/seiiiiiiiiiiru/status/2121390458572333253) (автор [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Попросите Fable сделать интерфейс для повторяющихся проверок 3D-материалов.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/ce514e99465c257220ee9bf7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/776670eda35fbabbf1c63663.jpg" alt="Case 469 · 1" width="760"><br>▶ Смотреть видео</a>

Автор рассказывает, что подключил Fable 5.2 как консультанта и модель превратила неудобный рабочий процесс в приложение. На записи видны готовые анимации, настройки фона и средства экспорта 3D-персонажа в GLB и PNG с прозрачным фоном.

Type: Demo | Date: 2026-11-13

---

<a id="case-470"></a>
### Case 470: [Проверка QR-кода, созданного без инструментов](https://x.com/AdamHoltererer/status/2121376853474578625) (автор [@AdamHoltererer](https://x.com/AdamHoltererer))

**Декодируйте полученный QR-код, прежде чем засчитывать успешную попытку.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d3833f006038158569c9816d.png" alt="Case 470 · 1" width="760">

Адам Холтер приписывает демонстрацию Fable 5.2, Astra и Sol и сообщает, что инструменты не использовались. Локальная проверка изображения подтвердила, что в QR-коде зашифрован текст MADE WITHOUT TOOLS.

Type: Evaluation | Date: 2026-11-13

---

<a id="case-471"></a>
### Case 471: [Игра про зомби на Unity с Tripo](https://x.com/fe_yukichi/status/2121375714192814554) (автор [@fe_yukichi](https://x.com/fe_yukichi))

**Готовьте модели в одном рабочем процессе, чтобы собрать набор игровых персонажей.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/055f505803b769bb8b24a54e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0fa0715e64f91ab69725599e.jpg" alt="Case 471 · 1" width="760"><br>▶ Смотреть видео</a>

Автор открыто указывает на сотрудничество с Tripo и сообщает, что с помощью Tripo Agentic Canvas создал восемь игровых персонажей и шестнадцать вариантов зомби для игры на Unity, сделанной с Fable 5.2. В видео показаны выбор персонажа и игровой процесс. Автор также опубликовал сборку для настольного браузера.

[Дополнительные материалы 1](https://tsukiyo-zombie.pages.dev/)

Type: Demo | Date: 2026-11-13

---

<a id="case-472"></a>
### Case 472: [Заснеженная улица, нарисованная в MS Paint](https://www.reddit.com/r/ClaudeAI/comments/1xvghd1/fable_52_painting_in_ms_paint/) (автор [u/wollymonjac](https://www.reddit.com/user/wollymonjac/))

**По записи экрана оцените, как модель напрямую управляет мышью во время длительной задачи.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/10ad84001f4c682c5343846c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e7af823e10ef2135adec2154.jpg" alt="Case 472 · 1" width="760"><br>▶ Смотреть видео</a>

Автор публикации на Reddit сообщает, что Fable 5.2 примерно за два с половиной часа нарисовала мышью заснеженную улицу в MS Paint. В репосте на X опубликована запись работы над той же сценой.

[Дополнительные материалы 1](https://x.com/i/status/2121373793599869213)

Type: Demo | Date: 2026-11-13

---

<a id="case-473"></a>
### Case 473: [Пропущенное соединение с розеткой в Wojak-Bench](https://x.com/lukaspet/status/2121371593943466167) (автор [@lukaspet](https://x.com/lukaspet))

**Сверьте каждое соединение с образцом, проверяя сгенерированную 3D-сборку.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e509db79b2e79fcc2d6beda1.jpg" alt="Case 473 · 1" width="760">

По словам автора, в задаче Wojak-Bench Fable 5.2 не соединила шнур с розеткой. На исходном изображении рядом с рисунком-образцом показана фотография объёмного результата.

Type: Limit | Date: 2026-11-13

---

<a id="case-474"></a>
### Case 474: [Фортепианная аранжировка для ритм-игры](https://x.com/DJ_HYSNS/status/2121367353237942287) (автор [@DJ_HYSNS](https://x.com/DJ_HYSNS))

**При работе над музыкой проверяйте исполнимость партии и управление звуком.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d016f48687e0c8e6cf810812.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/9faa77e2e9ba2ec99be995a7.jpg" alt="Case 474 · 1" width="760"><br>▶ Смотреть видео</a>

Автор попросил модель написать музыку для ритм-игры. По его словам, выбрать звуки VST и свести композицию оказалось трудно, поэтому он перешёл на фортепианное соло. В ролике показана получившаяся партия в редакторе нот. По оценке автора, она вышла за пределы того, что может сыграть человек, хотя это было одним из условий.

Type: Evaluation | Date: 2026-11-13

---

<a id="case-475"></a>
### Case 475: [Новый сценарий восстановления токенов в Picnic](https://x.com/joaoavf/status/2121366491321057717) (автор [@joaoavf](https://x.com/joaoavf))

**Сравните на макетах экраны восстановления неподдерживаемых токенов.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/551612796f4150a43b190ee3.jpg" alt="Case 475 · 1" width="760">

Автор сообщает, что одного или двух запросов к Fable 5.2 хватило, чтобы переработать сценарий восстановления токенов, которые Picnic не поддерживает. На приложенном изображении показано несколько экранов предложенного сценария.

Type: Demo | Date: 2026-11-13

---

<a id="case-476"></a>
### Case 476: [Монтаж аниме-заставки из сгенерированных кадров](https://x.com/aimikoda/status/2121362621274177726) (автор [@aimikoda](https://x.com/aimikoda))

**Передайте Fable видеоклипы, звуковую дорожку и чёткие указания, где делать склейки в такт музыке.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e3ab28061669d84818042ee0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/cb65344e413d2bd340406d59.jpg" alt="Case 476 · 1" width="760"><br>▶ Смотреть видео</a>

Для монтажа автор объединил кадры MiniMax H3 и трек Suno v6 с помощью Fable 5.2 в режиме Medium. В опубликованном ролике есть анимированные пиксельные персонажи и переходы. К примеру приложен исходный запрос на монтаж.

Исходный промпт

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
### Case 477: [Анимация персонажа с помощью трёх инструментов](https://x.com/ingi_erlingsson/status/2121361947446677797) (автор [@ingi_erlingsson](https://x.com/ingi_erlingsson))

**Сравните исходный GIF с анимацией после обработки в Fable и ComfyUI.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/69a3410b7b2dcdb14ee6c5d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/391924750cd0641254cb114f.jpg" alt="Case 477 · 1" width="760"><br>▶ Смотреть видео</a>

Автор указывает, что использовал GIF из GPT Image 2.6 как исходный материал и затем подключил Fable 5.2 и ComfyUI. В приложенном ролике голова персонажа меняется и показана с разных сторон при вращении.

Type: Demo | Date: 2026-11-13

---

<a id="case-478"></a>
### Case 478: [Рендер городского трейлера с помощью скриптов Blender](https://x.com/hanghuang_/status/2121361932456427644) (автор [@hanghuang_](https://x.com/hanghuang_))

**Разбейте работу над городским трейлером на сцену, персонажа, транспорт и рендеринг.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0e5170c057eecd328b178fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d10c5d322edba010282a60d0.jpg" alt="Case 478 · 1" width="760"><br>▶ Смотреть видео</a>

По словам автора, Fable 5.2 спланировала трейлер в стиле видеоигры и написала код Blender для города, персонажа и автомобиля. Автор говорит, что итоговый ролик в 4K отрендерили на семи арендованных GPU. В публикации показаны готовые кадры.

Type: Demo | Date: 2026-11-13

---

<a id="case-479"></a>
### Case 479: [Рисование ночных сцен на JavaScript](https://x.com/kloss_xyz/status/2121356668311384487) (автор [@kloss_xyz](https://x.com/kloss_xyz))

**При оценке иллюстраций, созданных кодом, сравнивайте несколько готовых изображений.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/6e9d554b17822715f07d3be8.jpg" alt="Case 479 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/f57db49bb8213cc6ca4bcafe.jpg" alt="Case 479 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/2933b30de09501dbbb7e1505.jpg" alt="Case 479 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/490e5952694322b7963be8e2.jpg" alt="Case 479 · 4" width="450"></td></tr></table>

Автор приписывает Fable 5.2 четыре опубликованные иллюстрации, нарисованные на JavaScript. В приложениях показаны стилизованные ночные сцены, которые можно сопоставить.

Type: Demo | Date: 2026-11-13

---

<a id="case-480"></a>
### Case 480: [Преобразование моделей САПР в инженерные чертежи](https://x.com/MecAgent/status/2121352868490100787) (автор [@MecAgent](https://x.com/MecAgent))

**Сверьте виды, размеры и обозначения с исходной моделью САПР.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/5ce59334e405a279e1008bf0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/780dc65cb1b04f7a75e27ace.jpg" alt="Case 480 · 1" width="760"><br>▶ Смотреть видео</a>

MecAgent в своей демонстрации показывает листы чертежей с несколькими видами и обозначениями и приписывает их построение Fable 5.2. В ролике видны готовые чертежи. Для проверки точности размеров потребуются исходные файлы САПР.

Type: Demo | Date: 2026-11-13

---

<a id="case-481"></a>
### Case 481: [43 задания по анализу данных от Plotly](https://plotly.com/blog/gemini-4-hydrogen-plotly-data-analytics-bench/) (автор [Plotly](https://plotly.com/))

**Сравните точность и стоимость прогона в одинаковой среде тестирования.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/50882a17db12bede9165a92d.webp" alt="Case 481 · 1" width="760">

По данным Plotly, Fable 5.2 вошла в число четырёх моделей, выполнивших все 43 задания, включая пять заданий на поиск скрытых закономерностей. Издатель предупреждает, что на каждую модель приходится по одному прогону. На графике сопоставлены стоимость и точность.

[Дополнительные материалы 1](https://news.ycombinator.com/item?id=50485733)

Type: Benchmark | Date: 2026-11-12

---

<a id="case-482"></a>
### Case 482: [Воссоздание SGI Indy в браузере](https://news.ycombinator.com/item?id=50476597) (автор [@gdubs](https://news.ycombinator.com/user?id=gdubs))

**Посмотрите на интерактивную реконструкцию, чтобы понять, как перенести физическую рабочую станцию на сайт.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/74b80686867b920881164246.jpg" alt="Case 482 · 1" width="760">

Грегори Вибер сообщает, что Fable 5.2 помогла переделать его сайт в рабочую станцию Silicon Graphics Indy из 1990-х. В опубликованной демонстрации есть трёхмерная рабочая станция, экран входа, трёхмерная файловая система и игра Soft Break.

[Дополнительные материалы 1](https://gregorywieber.com/indy/)

Type: Demo | Date: 2026-11-13

---

<a id="case-483"></a>
### Case 483: [Координация агентов через задачи и рабочие деревья Git](https://news.ycombinator.com/item?id=50493545) (автор [@nickalaso](https://news.ycombinator.com/user?id=nickalaso))

**Распределяйте работу через задачи и изолируйте изменения с помощью рабочих деревьев Git и пул-реквестов.**

Автор использует Fable 5.2 как главного координатора, Opus как координаторов отдельных групп и собственный MCP-сервер для запуска агентов разных поставщиков. За ходом работы он следит в GitHub Issues, а рабочие деревья и пул-реквесты помогают избегать конфликтов.

Type: Integration | Date: 2026-11-14

---

<a id="case-484"></a>
### Case 484: [Проверка ссылок на публикации в фоновом режиме](https://x.com/tukiyomiiori/status/2121368478364192930) (автор [@tukiyomiiori](https://x.com/tukiyomiiori))

**Поручите агентам проверить ссылки и проследите, когда возобновится основной сеанс.**

Автор сообщает, что попросил Fable 5.2 проверять цитируемые исследования через субагентов и фоновые скрипты. По его наблюдению, сеанс Claude Code приостанавливался на время проверки и возобновлялся, когда агенты или скрипты завершали работу.

Type: Integration | Date: 2026-11-13

---

<a id="case-485"></a>
### Case 485: [Отладка модели цен на перевозку в оба конца](https://x.com/allTheYud/status/2121360145921998877) (автор [@allTheYud](https://x.com/allTheYud))

**Убедитесь, что модель правильно учитывает предельные издержки обратного рейса.**

Автор сообщает, что при моделировании перевозки в двух направлениях Fable 5.2 отнесла затраты на топливо за оба направления к одному рейсу, а для другого учла только предельные затраты, хотя судно в любом случае должно было вернуться. Для устранения подобных ошибок потребовалось несколько циклов отладки.

Type: Limit | Date: 2026-11-13

---

<a id="case-486"></a>
### Case 486: [Адаптация запуска Edge0 для Mac](https://news.ycombinator.com/item?id=50482710) (автор [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen))

**Запросите изменения для нужной платформы, затем проверьте инференс на целевом компьютере.**

В обсуждении Edge0-145B пользователь рассказывает, что попросил Fable 5.2 подготовить версию для Mac и внёс несколько правок. По его данным, на M5 Max с NVFP4 получалось около 50 токенов в секунду.

[Дополнительные материалы 1](https://news.ycombinator.com/item?id=50475713)

Type: Integration | Date: 2026-11-13

---

<a id="case-487"></a>
### Case 487: [Проверка компоновки плат с высокой плотностью монтажа](https://news.ycombinator.com/item?id=50478759) (автор [@0_____0](https://news.ycombinator.com/user?id=0_____0))

**Проверьте расположение и выбор компонентов по требованиям к характеристикам платы.**

Пользователь Hacker News попробовал Fable 5.2 для размещения компонентов и трассировки нескольких плат. По его словам, плотная компоновка поначалу выглядела многообещающе. Чтобы выполнить свои требования, пользователю пришлось существенно изменить размещение компонентов и вручную перерисовать большую часть схемы.

Type: Limit | Date: 2026-11-13

---

<a id="case-488"></a>
### Case 488: [Поиск источника цитаты в платном газетном архиве](https://news.ycombinator.com/item?id=50478191) (автор [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff))

**Считайте предположение об авторстве предварительным до сверки с оригиналом.**

Участник Hacker News нашёл ссылку на статью Dallas Morning News за 1985 год в лингвистической рассылке. По его словам, Fable 5.2 не смогла открыть статью целиком и предложила вероятного автора и контекст. Проверка авторства требует доступа к исходному тексту.

[Дополнительные материалы 1](https://listserv.linguistlist.org/pipermail/ads-l/2003-September/033575.html)

Type: Limit | Date: 2026-11-13

---

<a id="case-489"></a>
### Case 489: [Планирование с Fable и проверка изменений Opus](https://news.ycombinator.com/item?id=50477200) (автор [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology))

**Утвердите письменный план, разделите реализацию на независимые направления и проверьте изменения в CI и тестовой среде.**

Автор делится процессом, который, по его словам, применял в крупных кодовых базах. Fable 5.2 составляет план, субагенты Opus 5.5 реализуют и проверяют изменения, CI следит за покрытием тестами, а контрольный список помогает вручную проверить результат в тестовой среде.

Type: Tutorial | Date: 2026-11-13

---

<a id="acknowledge"></a>
## Авторы

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/), [@fe_yukichi](https://x.com/fe_yukichi), [u/wollymonjac](https://www.reddit.com/user/wollymonjac/), [@lukaspet](https://x.com/lukaspet), [@DJ_HYSNS](https://x.com/DJ_HYSNS), [@joaoavf](https://x.com/joaoavf), [@aimikoda](https://x.com/aimikoda), [@ingi_erlingsson](https://x.com/ingi_erlingsson), [@hanghuang_](https://x.com/hanghuang_), [@MecAgent](https://x.com/MecAgent), [Plotly](https://plotly.com/), [@gdubs](https://news.ycombinator.com/user?id=gdubs), [@nickalaso](https://news.ycombinator.com/user?id=nickalaso), [@tukiyomiiori](https://x.com/tukiyomiiori), [@allTheYud](https://x.com/allTheYud), [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen), [@0_____0](https://news.ycombinator.com/user?id=0_____0), [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff), [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology)
