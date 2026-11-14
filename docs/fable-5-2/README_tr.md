# Claude Fable 5.2 Kullanım Örnekleri

[English](README.md) · [简体中文](README_zh-CN.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Português](README_pt.md) · [Deutsch](README_de.md) · [Français](README_fr.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md)

10 Kasım ve 13–14 Kasım derlemelerindeki iş akışları, demolar, karşılaştırmalar, kıyaslama testleri, entegrasyonlar ve kullanımda karşılaşılan sınırlar, kaynak bağlantılarıyla birlikte.

[Anthropic duyurusu](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [Önceki örnek koleksiyonu](../../README_tr.md)

## Örnek Dizini

| Case | Kullanım Örnekleri | Type |
| --- | --- | --- |
| 330 | [Çaba düzeylerine göre MacBook SVG çizimi](#case-330) | Benchmark |
| 331 | [Aile çizimlerinden dört kişilik dövüş oyunu](#case-331) | Demo |
| 332 | [Tasarımdan montaja üç elektronik cihaz](#case-332) | Demo |
| 333 | [Fermat’nın Son Teoremi’nin Lean’de biçimselleştirilmesi](#case-333) | Evaluation |
| 334 | [Boş klasörden işletim sistemi](#case-334) | Demo |
| 335 | [RoboDojo’da iki kollu manipülasyon](#case-335) | Benchmark |
| 336 | [Hareket hâlinde bir çeşme](#case-336) | Demo |
| 337 | [Higgsfield ile kare bazında dudak senkronu](#case-337) | Integration |
| 338 | [Açık dünya sürüş prototipi](#case-338) | Demo |
| 339 | [Referans görsellerle 1940 Paris’i](#case-339) | Integration |
| 340 | [Fable’ın planladığı, Opus’un ürettiği kısa film](#case-340) | Integration |
| 341 | [Bir müzik klibi denemesi](#case-341) | Demo |
| 342 | [Dario Amodei’nin boyanmış portresi](#case-342) | Demo |
| 343 | [Medium ayarında Spud Smash](#case-343) | Demo |
| 344 | [Fable ve Opus ile buz katedrali](#case-344) | Evaluation |
| 345 | [Simüle edilmiş ses yollarıyla şarkı](#case-345) | Demo |
| 346 | [İstanbul’da üç voksel testi](#case-346) | Evaluation |
| 347 | [Remote Labor Index’te proje tamamlama](#case-347) | Benchmark |
| 348 | [Dört çaba düzeyinde buzdağı](#case-348) | Evaluation |
| 349 | [Yetmiş dokuz saniyelik anime kısa filmi](#case-349) | Demo |
| 350 | [Fable ve Opus ile mekanik montaj](#case-350) | Evaluation |
| 351 | [Sarmal merdiven çıkan robot el](#case-351) | Demo |
| 352 | [Blender’da Tripo ağına iskelet eklemek](#case-352) | Evaluation |
| 353 | [Da Vinci’nin defterinden etkileşimli icatlar](#case-353) | Demo |
| 354 | [Claude’un yönettiği ses iş istasyonu](#case-354) | Demo |
| 355 | [Hareketli Raspberry Pi 5](#case-355) | Demo |
| 356 | [Kuzey İtalya’dan bir sahne](#case-356) | Demo |
| 357 | [Yerel uygulama ajanlarıyla açılır kitap](#case-357) | Evaluation |
| 358 | [Lav lambası testinin dönüşü](#case-358) | Evaluation |
| 359 | [Blender’da ayrıntılı jet modeli](#case-359) | Integration |
| 360 | [Portallarla yüzlerce dünya arasında yolculuk](#case-360) | Demo |
| 361 | [Three.js’de altı planlık Bombay pazarı](#case-361) | Integration |
| 362 | [Kodla oluşturulan fotogerçekçi lokanta](#case-362) | Integration |
| 363 | [Blender’da robot modeli](#case-363) | Demo |
| 364 | [Convex için hareketli açıklama videosu](#case-364) | Demo |
| 365 | [Tek istemle oluşturulan açılış sayfaları](#case-365) | Demo |
| 366 | [LilyPond ile yazılmış piyano sonatı](#case-366) | Demo |
| 367 | [Serbest bir video tarifi](#case-367) | Demo |
| 368 | [Fable planlıyor, DeepSeek yapıyor, Opus inceliyor](#case-368) | Integration |
| 369 | [AI Village'da Fable 5.2](#case-369) | Integration |
| 370 | [Skills ile ve skills olmadan arayüz tasarımı](#case-370) | Evaluation |
| 371 | [Kodda örtük durum makinelerini bulmak](#case-371) | Tutorial |
| 372 | [Sekiz saatte sıfırdan bir oyun](#case-372) | Demo |
| 373 | [Fishslop prototipi ve token maliyeti](#case-373) | Evaluation |
| 374 | [Hareketli Amerikan futbolu oyunu](#case-374) | Demo |
| 375 | [Higgsfield MCP ile açık dünya boss savaşı](#case-375) | Integration |
| 376 | [Mont Saint-Michel ve değişen gelgitler](#case-376) | Demo |
| 377 | [Blender’da bir Roblox öğesi](#case-377) | Demo |
| 378 | [Düşünce zinciri çıktısı olmadan akıl yürütme](#case-378) | Benchmark |
| 379 | [Dört modelle Chrome Dino uyarlaması](#case-379) | Evaluation |
| 380 | [Robot kolla dama oyunu](#case-380) | Demo |
| 381 | [On beş saniyelik hareketli grafik](#case-381) | Demo |
| 382 | [Oynanabilir Eyfel Kulesi](#case-382) | Demo |
| 383 | [Three.js ve Higgsfield ile açık deniz yarışı](#case-383) | Integration |
| 384 | [WebGL’de gerçek zamanlı bal simülasyonu](#case-384) | Demo |
| 385 | [Görüntüler üzerinde programlanmış görsel efektler](#case-385) | Demo |
| 386 | [GTA Aranma Seviyelerini Anlatan Animasyon](#case-386) | Demo |
| 387 | [Kodla oluşturulan stilize MMO dünyası](#case-387) | Demo |
| 388 | [Fable ve Opus ile 3B sahne](#case-388) | Evaluation |
| 389 | [Oyun duraklatma ekranında gereksiz metin](#case-389) | Limit |
| 390 | [Krea ortamıyla ilham panoları](#case-390) | Integration |
| 391 | [Portal temalı nişancı oyununun ofis testi](#case-391) | Demo |
| 392 | [Blender’da ayrıntılı sert yüzey modeli](#case-392) | Demo |
| 393 | [Farklı çaba düzeylerinde paralel arayüz testleri](#case-393) | Evaluation |
| 394 | [On istemle hazırlanan küçük oyun](#case-394) | Demo |
| 395 | [JavaScript ile kare kare animasyon](#case-395) | Demo |
| 396 | [Referans videodan 3B animasyona](#case-396) | Demo |
| 397 | [Fable ve Opus ile piksel kamp ateşi](#case-397) | Evaluation |
| 398 | [xHigh ayarında Arena WebDev](#case-398) | Benchmark |
| 399 | [İki modelle film fragmanı tipografisi](#case-399) | Evaluation |
| 400 | [Tek istemle hareketli tasarım ve 3B portföy testleri](#case-400) | Evaluation |
| 401 | [Keşfedilebilir nükleer reaktör anlatımı](#case-401) | Demo |
| 402 | [Blood on the Clocktower’da ajanlar](#case-402) | Benchmark |
| 403 | [Pod yarışı prototipi](#case-403) | Demo |
| 404 | [On saniyelik Claude iç çamaşırı reklamı](#case-404) | Demo |
| 405 | [Gün doğumunda bir kuş, çizgi çizgi](#case-405) | Demo |
| 406 | [Devin’de uzun bir grafik çalışması](#case-406) | Evaluation |
| 407 | [Üç modelle koddan resim](#case-407) | Evaluation |
| 408 | [Hareketli anlatımla yazının tarihi](#case-408) | Demo |
| 409 | [Oyun makineleri için test alanı](#case-409) | Demo |
| 410 | [Taşınabilir Linux konsolu için PCB tasarımı](#case-410) | Evaluation |
| 411 | [Voksel gölü](#case-411) | Demo |
| 412 | [Arena’dan 17 etkileşimli üretim](#case-412) | Demo |
| 413 | [Dost canlısı bir ejderhayla uçuş](#case-413) | Demo |
| 414 | [Fable ve Opus ile jelatin orka](#case-414) | Evaluation |
| 415 | [Açık uçlu video kalitesi testi](#case-415) | Demo |
| 416 | [Akdeniz temalı uzay habitatı](#case-416) | Demo |
| 417 | [Etkileşimli deneyimler için AA-3D benchmark’ı](#case-417) | Benchmark |
| 418 | [Süreli iskelet karakteri oyunu](#case-418) | Demo |
| 419 | [Fable ve Astra ile piksel sanatı](#case-419) | Evaluation |
| 420 | [Hareketli tasarım portföyü videosu](#case-420) | Demo |
| 421 | [İki modelle cam havuz görselleştirmesi](#case-421) | Evaluation |
| 422 | [TS-Bench’te araç çağrısı doğruluğu](#case-422) | Benchmark |
| 423 | [Minyatür Machu Picchu](#case-423) | Demo |
| 424 | [Mesleki görev kategorilerine göre GDPx](#case-424) | Benchmark |
| 425 | [Bir Çizim Uygulamasında Portre](#case-425) | Demo |
| 426 | [Low ayarında VulcanBench Frontier v4](#case-426) | Benchmark |
| 427 | [Oynanabilir Backrooms’da roller tersine dönüyor](#case-427) | Demo |
| 428 | [Blender’da Bugatti Tourbillon](#case-428) | Demo |
| 429 | [İki modelle hazırlanan bilgisayar temalı video](#case-429) | Demo |
| 430 | [Megakernel konulu müzik klibi](#case-430) | Demo |
| 431 | [Referans fotoğraflarından stüdyo turu](#case-431) | Demo |
| 432 | [Kodla hazırlanan 1990’lar oyuncak reklamı](#case-432) | Demo |
| 433 | [Three.js ile üçüncü şahıs oyun sahnesi](#case-433) | Demo |
| 434 | [Mevcut işleyiciden Bryceball](#case-434) | Demo |
| 435 | [Fable ile özyinelemeli video kurgusu](#case-435) | Demo |
| 436 | [Bilim tarihine sinematik bir yolculuk](#case-436) | Demo |
| 437 | [Da Vinci’nin uçan makinesi 3B ortamda](#case-437) | Integration |
| 438 | [Bir tasarım tarifinden PCB hat yönlendirmesi](#case-438) | Demo |
| 439 | [Farklı çalışma ortamlarında aynı istem](#case-439) | Evaluation |
| 440 | [Kodla çizilmiş Godzilla görseli](#case-440) | Demo |
| 441 | [3B baskı için el tipi vantilatör](#case-441) | Demo |
| 442 | [Opus ile eklenti hatası avı](#case-442) | Evaluation |
| 443 | [3B sahnede yeniden kurulan İstanbul](#case-443) | Demo |
| 444 | [Çalışan ekranlı bir Blender filmi](#case-444) | Demo |
| 445 | [Zayıf bağlaşımda kara delik geçişi](#case-445) | Evaluation |
| 446 | [Modüler bootstrap sınırının limiti](#case-446) | Evaluation |
| 447 | [Sıralı alternatif modellerle Vercel AI Gateway](#case-447) | Integration |
| 448 | [İç içe alt ajanlar ve inceleme bütçesi](#case-448) | Limit |
| 449 | [LCARS tasarımından HTML’e model karşılaştırması](#case-449) | Evaluation |
| 450 | [Quantum ESPRESSO için GPU optimizasyonu](#case-450) | Benchmark |
| 451 | [Çaba düzeyine göre Artificial Analysis Intelligence Index](#case-451) | Benchmark |
| 452 | [High düzeyinde değişiklik incelemesinde yanlış alarmlar](#case-452) | Limit |
| 453 | [Otuz günlük programlama görevi](#case-453) | Evaluation |
| 454 | [Issız ada ekran koruyucusu](#case-454) | Demo |
| 455 | [High düzeyinde üç tarayıcı oyunu](#case-455) | Evaluation |
| 456 | [Bölüm bölüm kitap podcast’i metinleri](#case-456) | Evaluation |
| 457 | [Üretimdeki bir hizmetin Rust’a taşınması](#case-457) | Evaluation |
| 458 | [GitHub Copilot'ta Fable 5.2 Seçmek](#case-458) | Integration |
| 459 | [Yüz HTML sayfası tasarlama denemesi](#case-459) | Evaluation |
| 460 | [Derleyici çalışmasında gereksinim sapması](#case-460) | Limit |
| 461 | [Uzun Fable Görevini Opus ile İzlemek](#case-461) | Integration |
| 462 | [Koda taze bir gözle bakmak](#case-462) | Tutorial |
| 463 | [Özellik tasarımı incelemesinde bağlam sapması](#case-463) | Limit |
| 464 | [DX Ball tarzı Breakout karşılaştırması](#case-464) | Evaluation |
| 465 | [3B uygulamayı iyileştirme denemesi](#case-465) | Evaluation |
| 466 | [Üç modelle fare ve kedi oyunu](#case-466) | Evaluation |
| 467 | [High düzeyinde AIBenchy maliyet ve puan karşılaştırması](#case-467) | Benchmark |
| 468 | [Fable 5.2 Ajan Ortamını Ayarlamak](#case-468) | Tutorial |
| 469 | [Animasyonlu Karakterleri Önizleme Uygulaması](#case-469) | Demo |
| 470 | [Araç Kullanmadan Üretilen QR Kodunu Test Etme](#case-470) | Evaluation |
| 471 | [Tripo ile Unity’de Zombi Oyunu](#case-471) | Demo |
| 472 | [MS Paint’te Karlı Bir Sokak Çizme](#case-472) | Demo |
| 473 | [Wojak-Bench’te Eksik Kalan Priz Bağlantısı](#case-473) | Limit |
| 474 | [Ritim Oyunu İçin Piyano Düzenlemesi](#case-474) | Evaluation |
| 475 | [Picnic’in Token Kurtarma Akışını Yeniden Tasarlama](#case-475) | Demo |
| 476 | [Üretilen Kliplerle Anime Açılışı Kurgulama](#case-476) | Tutorial |
| 477 | [Üç Araçla Karakter Animasyonu](#case-477) | Demo |
| 478 | [Blender Betikleriyle Şehir Fragmanı Oluşturma](#case-478) | Demo |
| 479 | [JavaScript ile Gece Manzaraları Çizme](#case-479) | Demo |
| 480 | [CAD Modellerini Teknik Resimlere Dönüştürme](#case-480) | Demo |
| 481 | [Plotly’nin Veri Analizi Sınavında 43 Görev](#case-481) | Benchmark |
| 482 | [SGI Indy’yi Web Sitesi Olarak Yeniden Canlandırma](#case-482) | Demo |
| 483 | [İş Kayıtları ve Git Çalışma Ağaçlarıyla Ajan Koordinasyonu](#case-483) | Integration |
| 484 | [Atıfları Arka Planda Çalışan Ajanlarla Kontrol Etme](#case-484) | Integration |
| 485 | [Gidiş Dönüş Navlun Fiyatı Modelinde Hata Ayıklama](#case-485) | Limit |
| 486 | [Edge0 Çıkarım Kurulumunu Mac’e Uyarlama](#case-486) | Integration |
| 487 | [Yüksek Bileşen Yoğunluklu Devre Kartı Yerleşimlerini İnceleme](#case-487) | Limit |
| 488 | [Ücretli Gazete Arşivinde Bir Atfın İzini Sürme](#case-488) | Limit |
| 489 | [Fable ile Planlama ve Opus Değişikliklerini İnceleme](#case-489) | Tutorial |

<a id="fable-5-2-cases"></a>
## Kullanım Örnekleri

<a id="case-330"></a>
### Case 330: [Çaba düzeylerine göre MacBook SVG çizimi](https://playcode.io/blog/macbook-svg-benchmark#compare) (üreten [Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin))

**Sabit tarifle çizim kalitesini, token’ları ve çıktı sınırını karşılaştırın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3a563fe19bbacbf0f20641c0.webp" alt="Case 330 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f589cd623d18ff3947543e39.webp" alt="Case 330 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0b238da7d1ec8608e4c08e7.webp" alt="Case 330 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b30fadede0a6be4e93158631.webp" alt="Case 330 · 4" width="450"></td></tr></table>

Playcode, Fable 5.2 High için 76.158 token ve 3,05 ABD doları bildiriyor. Xhigh ile Max, akışta çizim vermeden 128.000 token sınırına ulaştı ve Batch API’de daha geniş sınırla tamamladı. Sıralama yayıncının görsel değerlendirmesine dayanıyor.

[İlgili kaynaklar 1](https://news.ycombinator.com/item?id=50432975)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-331"></a>
### Case 331: [Aile çizimlerinden dört kişilik dövüş oyunu](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game) (üreten [Lex](https://notesbylex.com/))

**Ajanla eskizleri, mevcut prototipi ve kontrolcü gereksinimlerini paylaşın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/96e846247d4036b66aaae9e8.jpg" alt="Case 331 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1b9bab45940d075a19fe17a7.jpg" alt="Case 331 · 2" width="450"></td></tr></table>

Lex, Claude Code ile önceki yandan kaydırmalı oyunu 12 seviyeli, 18 karakterli bir dövüş oyununa dönüştürdü. Görüntü ve ses araçları öğeleri sağladı. Aile testinde dört kontrolcü çalıştı.

[İlgili kaynaklar 1](https://aidens-revenge.pages.dev/) · [İlgili kaynaklar 2](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game#enter-fable-52) · [İlgili kaynaklar 3](https://news.ycombinator.com/item?id=50433659)

Type: Demo | Date: 2026-11-09

---

<a id="case-332"></a>
### Case 332: [Tasarımdan montaja üç elektronik cihaz](https://www.anthropic.com/research/claude-electronics-design) (üreten [@Anthropic](https://www.anthropic.com/))

**Devreyi, muhafazayı ve gömülü yazılımı tek sistem olarak kontrol edin.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f565a48fdd8e980bc3d7ff87.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f4bd6327dd1a967343e3ad.webp" alt="Case 332 · 1" width="450"><br>▶ Videoyu oynat</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/62a9fe80e19b946a6cbbcb0f.png" alt="Case 332 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/406e5eae46b8c096de7dc9e6.png" alt="Case 332 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3481b7904ee4d849aa59462.png" alt="Case 332 · 4" width="450"></td></tr></table>

Anthropic ve Diode üç çalışan cihaz bildiriyor. Fable 5.2 kartların hatlarını çizdi, muhafazaları modelledi, yazılımı yazdı ve üretim sonrası testleri yönlendirdi.

[İlgili kaynaklar 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) · [İlgili kaynaklar 2](https://www.youtube.com/watch?v=vdYynH177h0) · [İlgili kaynaklar 3](https://news.ycombinator.com/item?id=50430687)

Type: Demo | Date: 2026-11-09

---

<a id="case-333"></a>
### Case 333: [Fermat’nın Son Teoremi’nin Lean’de biçimselleştirilmesi](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) (üreten [@Anthropic](https://www.anthropic.com/))

**İspat denetleyicisini ve ara teoremleri ilerleme ölçütü olarak kullanın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/13dca8328dafc6e21860d772.png" alt="Case 333 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ae9400390023085b8047fa4a.png" alt="Case 333 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f0caf7f3e1dd17ad5ca3c9c.png" alt="Case 333 · 3" width="450"></td></tr></table>

Anthropic, 1.000 Fable 5.2 ajanının mevcut ispatı 30 saatte biçimselleştirdiğini bildiriyor. Aynı ekip düzeninde Opus 5.5, 18 saatte %26’ya ulaştı.

[İlgili kaynaklar 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#mathematics) · [İlgili kaynaklar 2](https://news.ycombinator.com/item?id=50430379)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-334"></a>
### Case 334: [Boş klasörden işletim sistemi](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding) (üreten [@Anthropic](https://www.anthropic.com/))

**Açılış, sürücüler, depolama ve kurulumu ayrı ayrı kontrol edin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/362732c44b7c4ac0f59826d5.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b47999d8a41c742ce6ebed22.webp" alt="Case 334 · 1" width="760"><br>▶ Videoyu oynat</a>

Anthropic, Fable 5.2’nin sekiz günde 1.000’den fazla alt ajanı yönettiğini ve ortaya çıkan işletim sistemi prototipinin dizüstü bilgisayarda açıldığını bildiriyor.

Type: Demo | Date: 2026-11-09

---

<a id="case-335"></a>
### Case 335: [RoboDojo’da iki kollu manipülasyon](https://www.anthropic.com/claude-fable-and-mythos-5-2#hardware-and-robotics) (üreten [@Anthropic](https://www.anthropic.com/))

**Modelleri aynı simüle edilmiş manipülasyon görevleriyle karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39bb958360d8c38c6b75a72.webm"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4fdf401a464d0aa4e465a8eb.webp" alt="Case 335 · 1" width="760"><br>▶ Videoyu oynat</a>

Anthropic RoboDojo’da Fable 5.2 için %64,9, Fable 5.1 için %27,6 bildiriyor. Duyuruda bir robotik gösterimi de yer alıyor.

[İlgili kaynaklar 1](https://robodojo-benchmark.com/)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-336"></a>
### Case 336: [Hareket hâlinde bir çeşme](https://x.com/Angaisb_/status/2119909059277238733) (üreten [@Angaisb_](https://x.com/Angaisb_))

**Görsel ritmi kesintisiz su akışıyla değerlendirin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/aeda6ed069b1f8cd8a6ac969.jpg" alt="Case 336 · 1" width="760">

Yazar Fable 5.2’ye atfettiği bir çeşme sahnesi paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-337"></a>
### Case 337: [Higgsfield ile kare bazında dudak senkronu](https://x.com/higgsfield_ai/status/2119909938969580024) (üreten [@higgsfield_ai](https://x.com/higgsfield_ai))

**Klibi incelemeden önce sesi karelere hizalayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/67ad09565161509c52771dca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/76c141802313642b67984dc9.jpg" alt="Case 337 · 1" width="760"><br>▶ Videoyu oynat</a>

Higgsfield, Fable 5.2 kullanılan iş akışında ağız hareketini takip edip sesi karelere hizaladığını bildiriyor.

Type: Integration | Date: 2026-11-10

---

<a id="case-338"></a>
### Case 338: [Açık dünya sürüş prototipi](https://x.com/ericmaskfr/status/2119910195325481026) (üreten [@ericmaskfr](https://x.com/ericmaskfr))

**Kısa bir açık dünya tarifini oynanabilir bir bölümde sınayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30396ec07a6114476972b8cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c6969c03966c3dbf07da664e.jpg" alt="Case 338 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar GTA esintili bir prototip gösteriyor ve işlemin yaklaşık 2 saat 14 dakika sürdüğünü bildiriyor.

Orijinal istem

```
you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug
```

Type: Demo | Date: 2026-11-10

---

<a id="case-339"></a>
### Case 339: [Referans görsellerle 1940 Paris’i](https://x.com/higgsfield_ai/status/2119910344998912507) (üreten [@higgsfield_ai](https://x.com/higgsfield_ai))

**Referans görsel üretimini sahne kodundan ayırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d323c2a653c756fd011298cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63b2bd7bb96612c79f175db6.jpg" alt="Case 339 · 1" width="760"><br>▶ Videoyu oynat</a>

Higgsfield, MCP’sinden referans görseller sağladı ve Three.js sahnesinde Fable 5.2 kullandı.

Type: Integration | Date: 2026-11-10

---

<a id="case-340"></a>
### Case 340: [Fable’ın planladığı, Opus’un ürettiği kısa film](https://x.com/kloss_xyz/status/2119910613828980846) (üreten [@kloss_xyz](https://x.com/kloss_xyz))

**Video iş akışında planlamayı uygulamadan ayırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9e42129cf9859dcd0d0870b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/452a57a4d600164ef135df17.jpg" alt="Case 340 · 1" width="760"><br>▶ Videoyu oynat</a>

Fable 5.2 tarifi ve planı yazdı. Opus 5.5, Blender ve Python ile 16 saniyelik animasyonu yaptı ve müziği sentezledi.

Type: Integration | Date: 2026-11-10

---

<a id="case-341"></a>
### Case 341: [Bir müzik klibi denemesi](https://x.com/WesRoth/status/2119911161386934330) (üreten [@WesRoth](https://x.com/WesRoth))

**Şarkı sözlerini ve üretilen sekansı inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c5bed886d666e18d52a07f4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b4b4651998e8801edca48a0f.jpg" alt="Case 341 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ile hazırlanan müzik klibini paylaşıyor ve sözleri hakkında yorum yapıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-342"></a>
### Case 342: [Dario Amodei’nin boyanmış portresi](https://x.com/Mr_Salio/status/2119911922577637543) (üreten [@Mr_Salio](https://x.com/Mr_Salio))

**Stilize portreyi yanında gösterilen referansla karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4bfd3c4e2d4a239eed445854.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c0c6ebd30dd13f764da7e41e.jpg" alt="Case 342 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Dario Amodei’nin Fable 5.2’ye atfettiği portresini paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-343"></a>
### Case 343: [Medium ayarında Spud Smash](https://x.com/argofowl/status/2119913148929187960) (üreten [@argofowl](https://x.com/argofowl))

**Oyun prototipine belirgin eylemler ve bir hedef verin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/03cd8171abcd943e7bb5a436.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4f56dc5bb7990f3b5e28d2fb.jpg" alt="Case 343 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar mavi sandalyeleri yumruklayan, kafayla vuran veya yakan bir patates karakteri gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-344"></a>
### Case 344: [Fable ve Opus ile buz katedrali](https://x.com/QQTeng/status/2119913518015435103) (üreten [@QQTeng](https://x.com/QQTeng))

**Aynı sahnede üretim süresi ve maliyeti karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1a3e1adbf5da7852b4d25a26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/471d0d240c12e142b858e9c6.jpg" alt="Case 344 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable için yaklaşık 1 saat 57 dakika ve 81,10 ABD doları, Opus için yaklaşık 3 saat 11 dakika ve 45,97 ABD doları bildiriyor.

Orijinal istem

```
冰之大教堂
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-345"></a>
### Case 345: [Simüle edilmiş ses yollarıyla şarkı](https://x.com/banteg/status/2119914098171199996) (üreten [@banteg](https://x.com/banteg))

**Müzik üretiminde fiziksel bir ses modelini girdi olarak kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/940a2356280b5e07dcc44751.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6c227cf2dffdccef095e4799.jpg" alt="Case 345 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar iki Chimera ses yolu simülasyonu ve vocoder miksajıyla hazırlanmış bir yorum paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-346"></a>
### Case 346: [İstanbul’da üç voksel testi](https://x.com/Avenoxai/status/2119914308603953485) (üreten [@Avenoxai](https://x.com/Avenoxai))

**Bir yıkım sahnesini, çalışan saati ve haritayı karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8b1b5599e06c8eefcd9b0fb7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70fae6a141721a5192ac5b4a.jpg" alt="Case 346 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar tek istemli üç test paylaşıyor ve kendi ölçütlerine göre 100, 100 ve 95,6 puan bildiriyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-347"></a>
### Case 347: [Remote Labor Index’te proje tamamlama](https://x.com/ScaleAILabs/status/2119914701736075489) (üreten [@ScaleAILabs](https://x.com/ScaleAILabs))

**Oranı değerlendirilen projeler bağlamında okuyun.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b5bbfe56be8b79eeb49d98a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af07f32ff45a05194ba2a477.jpg" alt="Case 347 · 1" width="760"><br>▶ Videoyu oynat</a>

Scale Labs ve CAIS, Fable 5.2’nin değerlendirilen uzaktan çalışma projelerinin %41,3’ünü başarıyla tamamladığını bildiriyor.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-348"></a>
### Case 348: [Dört çaba düzeyinde buzdağı](https://x.com/0xRhinoX/status/2119915121698840587) (üreten [@0xRhinoX](https://x.com/0xRhinoX))

**Çaba arttıkça tamamlanma, maliyet ve ayrıntıyı karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f977ce3872745825d4cd40e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cb39469c95d647cb4a3d2b7e.jpg" alt="Case 348 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar dört düzeyde de aynı istemi kullandı. High kutup ışıklarını atladı. Ultra parlayan buz ve su altı görünümü ekledi.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-349"></a>
### Case 349: [Yetmiş dokuz saniyelik anime kısa filmi](https://x.com/anstapnever/status/2119915123070644263) (üreten [@anstapnever](https://x.com/anstapnever))

**Uzun animasyonda sahne sürekliliğini inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8847a7da2b15fea6ed61486.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ecffeee901866b75c766911.jpg" alt="Case 349 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 iş akışına atfettiği 79 saniyelik anime klibini paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-350"></a>
### Case 350: [Fable ve Opus ile mekanik montaj](https://x.com/ivanainai/status/2119915243321397550) (üreten [@ivanainai](https://x.com/ivanainai))

**Modellerin montaj parçalarını nasıl düzenlediğini karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3e4ce757f8b2546c1bfaee2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/138babe723c00db5b4322023.jpg" alt="Case 350 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ve Opus 5.5 ile yapılan, tekerlek ve dişlilerin etiketli patlatılmış görünümlerini gösteriyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-351"></a>
### Case 351: [Sarmal merdiven çıkan robot el](https://x.com/Luckyballa/status/2119915557663506720) (üreten [@Luckyballa](https://x.com/Luckyballa))

**Alışılmadık bir hareketi incelemek için simüle edilmiş bir engel kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f512d1a1fd80fb3375772a7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cede6335afe5fed468b4064d.jpg" alt="Case 351 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ve Steel 0.1 kullanarak Wuji elinin parmakları üzerinde yürümesini gösteriyor.

[İlgili kaynaklar 1](https://github.com/skild-ai/steel-webgpu/pull/7)

Orijinal istem

```
Make Wuji hand climb a spiral staircase by walking on its fingers as legs
```

Type: Demo | Date: 2026-11-10

---

<a id="case-352"></a>
### Case 352: [Blender’da Tripo ağına iskelet eklemek](https://x.com/0xKense1/status/2119916096098582566) (üreten [@0xKense1](https://x.com/0xKense1))

**Tutuş, doku ve deformasyon için sayısal ölçütler kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4ad640a0567811c818691e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e505d06a00bab567b94f40b4.jpg" alt="Case 352 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Tripo öğelerinden oluşturulan iki iskeleti karşılaştırıyor. Fable 36 dakikada iki, Opus yaklaşık 21 dakikada sekiz klip üretti.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-353"></a>
### Case 353: [Da Vinci’nin defterinden etkileşimli icatlar](https://x.com/alexalbert__/status/2119916954337349737) (üreten [@alexalbert__](https://x.com/alexalbert__))

**Eğitim modelini özgün çizimlere dayandırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09ecdd249f91a3487cce3a69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5aa9b617dbcfb527afb93327.jpg" alt="Case 353 · 1" width="760"><br>▶ Videoyu oynat</a>

Alex Albert, Leonardo'nun defterinin PDF dosyasını verdi ve icatların etkileşimli bir yorumunu paylaştı.

Type: Demo | Date: 2026-11-10

---

<a id="case-354"></a>
### Case 354: [Claude’un yönettiği ses iş istasyonu](https://x.com/The_Alex/status/2119917226769985785) (üreten [@The_Alex](https://x.com/The_Alex))

**Yinelenen beste istekleri için ajan kontrollü bir araç kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/05d8dafa9d71243ac431f4b3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/af7b840fccc26a3e6a5c977d.jpg" alt="Case 354 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ile yaptığı dijital ses iş istasyonunu gösteriyor ve Opus’un daha sonra şarkı yapmak için bu aracı açtığını belirtiyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-355"></a>
### Case 355: [Hareketli Raspberry Pi 5](https://x.com/sparklabhq/status/2119917375080521921) (üreten [@sparklabhq](https://x.com/sparklabhq))

**Parçaları incelemek için ürün animasyonu kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eda7686c7321d3b7ea97c7e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8ac13e688746a6cca47f3d59.jpg" alt="Case 355 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ile canlandırılmış Raspberry Pi 5 paylaşıyor.

Orijinal istem

```
animate a raspberry pi 5
```

Type: Demo | Date: 2026-11-10

---

<a id="case-356"></a>
### Case 356: [Kuzey İtalya’dan bir sahne](https://x.com/Angaisb_/status/2119917807119089926) (üreten [@Angaisb_](https://x.com/Angaisb_))

**Bir yere dayanan tarifte manzara ve atmosferi inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba91e63a0dbc7971eac55c46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/df913630f97a669a116887aa.jpg" alt="Case 356 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Kuzey İtalya’da geçen bir Fable 5.2 sahnesi paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-357"></a>
### Case 357: [Yerel uygulama ajanlarıyla açılır kitap](https://x.com/atomicagent_io/status/2119918110752846094) (üreten [@atomicagent_io](https://x.com/atomicagent_io))

**Aynı görevde ajan koordinasyonunu tek modelli çalışmayla karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f4266018c9fba1eeafd8f0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4b117f500fa02c3662d99749.jpg" alt="Case 357 · 1" width="760"><br>▶ Videoyu oynat</a>

Atomic, Fable yerel Qwen ajanlarını yönettiğinde 11 dakika ve 2,98 ABD doları, tek başına çalıştığında 21 dakika ve 15,77 ABD doları bildiriyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-358"></a>
### Case 358: [Lav lambası testinin dönüşü](https://x.com/eidzoku/status/2119918134060601690) (üreten [@eidzoku](https://x.com/eidzoku))

**Modelleri aynı görsel görevde karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1864d0790d0e9a1e27a29cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/06fc317c230156e876a5c9b9.jpg" alt="Case 358 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar lav lambası testini yeniden yapıp görsel karşılaştırmayı paylaştı.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-359"></a>
### Case 359: [Blender’da ayrıntılı jet modeli](https://x.com/higgsfield_ai/status/2119918248955392431) (üreten [@higgsfield_ai](https://x.com/higgsfield_ai))

**Tarifte parça sayısını, süreyi ve görünümü belirtin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0d9c17fb4f7560dec16b1915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/20403905ba10d5bc666a6e3f.jpg" alt="Case 359 · 1" width="760"><br>▶ Videoyu oynat</a>

Higgsfield, Fable 5.2 ve kendi MCP’siyle Blender’da betik kullanarak 931 parça ve 24.260 perçin içeren model ürettiğini belirtiyor.

Type: Integration | Date: 2026-11-10

---

<a id="case-360"></a>
### Case 360: [Portallarla yüzlerce dünya arasında yolculuk](https://x.com/emollick/status/2119918307457577163) (üreten [@emollick](https://x.com/emollick))

**Bağımsız üretilen ortamları portallarla bağlayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/671ee19ede1777190076393b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/953ef3fd0c7732a4686a921a.jpg" alt="Case 360 · 1" width="760"><br>▶ Videoyu oynat</a>

Ethan Mollick, 25.000 ajanın kodla 450’den fazla dünya ürettiğini bildiriyor ve oyunla deposunu paylaşıyor.

[İlgili kaynaklar 1](https://portals-endless-worlds.netlify.app/) · [İlgili kaynaklar 2](https://github.com/emollick/ai-portals)

Type: Demo | Date: 2026-11-10

---

<a id="case-361"></a>
### Case 361: [Three.js’de altı planlık Bombay pazarı](https://x.com/higgsfield_ai/status/2119918834841010320) (üreten [@higgsfield_ai](https://x.com/higgsfield_ai))

**Görsel tarifi süreleri belirli planlara ayırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7b8fe2acbb88ea8c65675f3e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0ee56bc16e9dbe0b757aa27.jpg" alt="Case 361 · 1" width="760"><br>▶ Videoyu oynat</a>

Higgsfield, Three.js’de işlenen 21,5 saniyelik altı planlı pazar sekansını gösteriyor.

Type: Integration | Date: 2026-11-10

---

<a id="case-362"></a>
### Case 362: [Kodla oluşturulan fotogerçekçi lokanta](https://x.com/higgsfield_ai/status/2119918838490010008) (üreten [@higgsfield_ai](https://x.com/higgsfield_ai))

**Malzeme ve aydınlatmayı kodla kurulmuş bir sahnede inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ceb25943484f81c5bc98cbec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f4ad3267a4a9afaf55a4143f.jpg" alt="Case 362 · 1" width="760"><br>▶ Videoyu oynat</a>

Higgsfield bir lokanta gösteriyor ve sahneyi 3B modelleme yazılımı kullanmadan kodla kurduğunu bildiriyor.

Type: Integration | Date: 2026-11-10

---

<a id="case-363"></a>
### Case 363: [Blender’da robot modeli](https://x.com/seiiiiiiiiiiru/status/2119919169768747313) (üreten [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Eklem ve silueti incelemek için döner görünüm kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8324c4a3ab6c13d6a7b07341.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/764a49ccb5f55b8cc7e1d6b2.jpg" alt="Case 363 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, Fable 5.2 ile Blender’da yapılan küçük bir mekanik robotu gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-364"></a>
### Case 364: [Convex için hareketli açıklama videosu](https://x.com/Rasmic/status/2119919466163093768) (üreten [@Rasmic](https://x.com/Rasmic))

**Geliştiricilere yönelik bir ürünü kısa animasyonla anlatın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/99fecfafe87450800e8b7819.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/78b2a07c5c1eb461e5f06c44.jpg" alt="Case 364 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ile yapılmış bir Convex animasyonu paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-365"></a>
### Case 365: [Tek istemle oluşturulan açılış sayfaları](https://x.com/daradoescode/status/2119919529807466594) (üreten [@daradoescode](https://x.com/daradoescode))

**Kısa tarifler arasında görsel hiyerarşi ve düzeni karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fae5081bcfb2859df1dcdfb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/116812f7cc009fd99e0464ef.jpg" alt="Case 365 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ile üretilen açılış sayfalarını bir videoda topluyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-366"></a>
### Case 366: [LilyPond ile yazılmış piyano sonatı](https://x.com/imjustnewatai/status/2119919644836347926) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Nota dosyasını işlenmiş videoyla ilişkilendirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/45d35e4b13927ed2a7c6b88a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40deb153659a4cc5c2f5bd94.jpg" alt="Case 366 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Beethoven tarzında bir bölüm istediğini ve gösterilen notaların LilyPond dosyasından geldiğini bildiriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-367"></a>
### Case 367: [Serbest bir video tarifi](https://x.com/aollivier82/status/2119920990893244510) (üreten [@aollivier82](https://x.com/aollivier82))

**Modelin varsayılan yaratıcı seçimlerini gözlemlemek için açık bir tarif kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3941c4573571c2e35b7013c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/872fea16ef18ad523bacfc9e.jpg" alt="Case 367 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2’den yapabileceği en güzel videoyu istedi ve sonucu paylaştı.

Orijinal istem

```
make me the most beautiful video you can
```

Type: Demo | Date: 2026-11-10

---

<a id="case-368"></a>
### Case 368: [Fable planlıyor, DeepSeek yapıyor, Opus inceliyor](https://x.com/ivanfioravanti/status/2119921810267636201) (üreten [@ivanfioravanti](https://x.com/ivanfioravanti))

**Koordinasyon, uygulama ve incelemeyi ayrı ajanlara verin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5c4d1f03ae039305d58d9153.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/eaa8c645d0ded887a7d12f4c.jpg" alt="Case 368 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable’ın herdr üzerinden dört DeepSeek V4.1 Flash ajanını yönettiğini ve Opus 5.5’in pull request’leri incelediğini gösteriyor.

Type: Integration | Date: 2026-11-10

---

<a id="case-369"></a>
### Case 369: [AI Village'da Fable 5.2](https://x.com/aidigest_/status/2119923190411719158) (üreten [@aidigest_](https://x.com/aidigest_))

**Ajanın yanıtını ve bellek işlemlerini ayrı ayrı inceleyin.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/daf94788cbc08ec41821de10.jpg" alt="Case 369 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7e814abcdd6f1f6c6bac2f05.jpg" alt="Case 369 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/50c97527b4dcec19201353f6.jpg" alt="Case 369 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f892b80e6f77b034a5a8f8b3.png" alt="Case 369 · 4" width="450"></td></tr></table>

Herkese açık günlükte Fable, başka bir ajanın isteği üzerine belleğini daha sonra güncellemeyi kabul ediyor. İlgili gönderi bir karakter eşleştirme testini gösteriyor.

[İlgili kaynaklar 1](https://x.com/aidigest_/status/2119923209311260707) · [İlgili kaynaklar 2](https://theaidigest.org/village/agent/claude-fable-5-2)

Type: Integration | Date: 2026-11-10

---

<a id="case-370"></a>
### Case 370: [Skills ile ve skills olmadan arayüz tasarımı](https://x.com/AdamHoltererer/status/2119924849321914653) (üreten [@AdamHoltererer](https://x.com/AdamHoltererer))

**Modeli sabit tutup skills yapılandırmasını değiştirin.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7ad18fd1bfd24cba134effd2.jpg" alt="Case 370 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3356427eeeaaae860c2f1fa.jpg" alt="Case 370 · 2" width="450"></td></tr></table>

Yazar Fable 5.2 ile biri skills kullanılarak, diğeri kullanılmadan hazırlanan iki arayüz gösteriyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-371"></a>
### Case 371: [Kodda örtük durum makinelerini bulmak](https://x.com/kunchenguid/status/2119924895060795492) (üreten [@kunchenguid](https://x.com/kunchenguid))

**Bir modülü inceleyip önce ve sonra diyagramları isteyin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/debfe905f84bc3f7ebf0c1c9.jpg" alt="Case 371 · 1" width="760">

Yazar Firstmate deposundaki bir iyileştirmeyi gösteriyor ve inceleme istemini aynen yayımlıyor.

[İlgili kaynaklar 1](https://github.com/kunchenguid/lavish-axi)

Orijinal istem

```
audit and find implicit state machines in this <codebase/directory/module> that would drive concrete improvements if made explicit. explain before/after of each one and discuss with me in lavish-axi. fewer words, big visuals
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-372"></a>
### Case 372: [Sekiz saatte sıfırdan bir oyun](https://x.com/felixrieseberg/status/2119925633564463609) (üreten [@felixrieseberg](https://x.com/felixrieseberg))

**Önbelleğe alınan girdileri, üretilen öğeleri ve geçen süreyi kaydedin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d317e1a4b4c6aaa6bbff3ba.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/98cec5260c61ad41b9142fbb.jpg" alt="Case 372 · 1" width="760"><br>▶ Videoyu oynat</a>

Anthropic mühendisi tek bir çalışmada model, ses ve dokular ürettiğini ve API fiyatlarıyla maliyetin yaklaşık 550 ABD doları olduğunu belirtiyor.

[İlgili kaynaklar 1](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp) · [İlgili kaynaklar 2](https://x.com/AndrewCurran_/status/2119953960794780133)

Orijinal istem

```
You know, you should also build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics.
```

Type: Demo | Date: 2026-11-10

---

<a id="case-373"></a>
### Case 373: [Fishslop prototipi ve token maliyeti](https://x.com/theo/status/2119926277801144695) (üreten [@theo](https://x.com/theo))

**Oyun yapımını önceki bir model sonucuyla karşılaştırın.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d2e16882e0b486907b1b4420.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9a79cdfcb7c314b21d4ebd.jpg" alt="Case 373 · 1" width="450"><br>▶ Videoyu oynat</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/775a6bf0c6d12a31188bdd49.jpg" alt="Case 373 · 2" width="450"></td></tr></table>

Yazar 76 dakika ve yaklaşık 42 ABD doları token maliyeti bildiriyor ve sonucu Opus 5.5 ile karşılaştırıyor.

[İlgili kaynaklar 1](https://x.com/theo/status/2119948914023653845)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-374"></a>
### Case 374: [Hareketli Amerikan futbolu oyunu](https://x.com/WesRoth/status/2119926801514529027) (üreten [@WesRoth](https://x.com/WesRoth))

**Spor prototipinde geri bildirim ve skor işaretlerini sınayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a25ad49f1039ed39d04876e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e121ccc7f3aa7c068c718ef8.jpg" alt="Case 374 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ile yapılan oyunda ekranda skor bildirimleri gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-375"></a>
### Case 375: [Higgsfield MCP ile açık dünya boss savaşı](https://x.com/higgsfield_ai/status/2119926932343324795) (üreten [@higgsfield_ai](https://x.com/higgsfield_ai))

**Oynanabilir bölümü ara sahnelerden ayırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/533377898eafb413d365af69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/207aa9b866615d3d84d05a71.jpg" alt="Case 375 · 1" width="760"><br>▶ Videoyu oynat</a>

Higgsfield, Fable 5.2 ve kendi MCP’siyle açık dünya, üç aşamalı boss savaşı ve ara sahneler içeren bir tarayıcı oyunu yapıldığını bildiriyor.

Type: Integration | Date: 2026-11-10

---

<a id="case-376"></a>
### Case 376: [Mont Saint-Michel ve değişen gelgitler](https://x.com/loktar00/status/2119927152489472076) (üreten [@loktar00](https://x.com/loktar00))

**Küçük bir tarihî sahnede değişen su seviyelerini sınayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/58323f1bb54f928947490281.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5e0ccde2b3185ab5c5ce9d5.jpg" alt="Case 376 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, gelgitleri canlandırılmış minyatür Mont Saint-Michel’i gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-377"></a>
### Case 377: [Blender’da bir Roblox öğesi](https://x.com/hiyouwhatsapp/status/2119927163264573642) (üreten [@hiyouwhatsapp](https://x.com/hiyouwhatsapp))

**Öğeyi içe aktarmadan önce Blender’da inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/79a90ae2311cebfb94b843bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/647cc34303356c4c4e8ebef2.jpg" alt="Case 377 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, Roblox için Blender’da neredeyse tek istemle üretilen bir sonuç gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-378"></a>
### Case 378: [Düşünce zinciri çıktısı olmadan akıl yürütme](https://x.com/Tim_Hua_/status/2119927284761293089) (üreten [@Tim_Hua_](https://x.com/Tim_Hua_))

**Yanıtları aynı çıktı kısıtı altında değerlendirin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/205aca5742ab3eda93dad5db.jpg" alt="Case 378 · 1" width="760">

Testi yapan kişi, akıl yürütme ve bilgi testlerini düşünce zinciri çıktısı olmadan yürüttü ve Fable 5.2’yi GPT-6.1 Sol’un biraz gerisinde konumlandırdı.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-379"></a>
### Case 379: [Dört modelle Chrome Dino uyarlaması](https://x.com/noclipepe/status/2119927838321328577) (üreten [@noclipepe](https://x.com/noclipepe))

**Tekrarlanan bir oyun tarifinde süre ve maliyeti karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c44effaf41686e33555f28dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/311664f9f75b453e779f1e36.jpg" alt="Case 379 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2’yi Opus, Gemini ve Astra’yla yürüttüğü T-Rex testine ekliyor ve sonuçları birlikte gösteriyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-380"></a>
### Case 380: [Robot kolla dama oyunu](https://x.com/karolina_dubiel/status/2119928342115676576) (üreten [@karolina_dubiel](https://x.com/karolina_dubiel))

**Eklem konumlarını okuyun ve başarısız tutuşları yeniden deneyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bac4f2cf9b9025cbbfb95bab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f02785be39d9a47e9b600a94.jpg" alt="Case 380 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, modelin yaklaşık 7 mm’lik sarkmayı düzelttiğini ve geri bildirimle başarısız hareketleri yeniden denediğini bildiriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-381"></a>
### Case 381: [On beş saniyelik hareketli grafik](https://x.com/aziz4ai/status/2119928581405200726) (üreten [@aziz4ai](https://x.com/aziz4ai))

**Kısa bir kod animasyonu testinin kota tüketimini kaydedin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fe389dc70f8d815a65c6620a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7756dc98b70619f6ad05099f.jpg" alt="Case 381 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar kodla yapılmış 15 saniyelik sahne paylaşıyor ve haftalık hakkının %4’ünü kullandığını söylüyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-382"></a>
### Case 382: [Oynanabilir Eyfel Kulesi](https://x.com/bobyau/status/2119928812628771212) (üreten [@bobyau](https://x.com/bobyau))

**Bir yapı modelinin etkileşim sunup sunmadığını sınayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5035b499b759d7537c21a9c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4eb65ee55920daaa638405b6.jpg" alt="Case 382 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar bir Eyfel Kulesi demosu paylaşıyor ve yapımın 25 dakika sürdüğünü belirtiyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-383"></a>
### Case 383: [Three.js ve Higgsfield ile açık deniz yarışı](https://x.com/higgsfield_ai/status/2119928918035910668) (üreten [@higgsfield_ai](https://x.com/higgsfield_ai))

**Oyun mantığını medya araçlarından ayırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2f4273f52da2fb9b9f429e54.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4792a0ff1feea8db949ee982.jpg" alt="Case 383 · 1" width="760"><br>▶ Videoyu oynat</a>

Higgsfield büyük dalgalar, beş yapay zekâ rakibi ve güdümlü roketlerle bir yarış oyunu gösteriyor.

Type: Integration | Date: 2026-11-10

---

<a id="case-384"></a>
### Case 384: [WebGL’de gerçek zamanlı bal simülasyonu](https://x.com/deedydas/status/2119930300990177509) (üreten [@deedydas](https://x.com/deedydas))

**Malzeme hareketini tarayıcıdaki fizik simülasyonuyla sınayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/07c711157eba0b6074af4974.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ffa13e754087a8b61cdc8ea0.jpg" alt="Case 384 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar WebGL’de gerçek zamanlı bal simülasyonunu gösteriyor ve özgün kısa tarifi yayımlıyor.

Orijinal istem

```
Can you write the most intricate photorealistic simulation of honey in WebGL in the browser
```

Type: Demo | Date: 2026-11-10

---

<a id="case-385"></a>
### Case 385: [Görüntüler üzerinde programlanmış görsel efektler](https://x.com/ashebytes/status/2119930763105931649) (üreten [@ashebytes](https://x.com/ashebytes))

**Efektlerin zamanlamasını ve yerini kaynak video üzerinde inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d9ccc08cd6aecfa457f0d87b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0da2938b5b8bbd8b25c401eb.jpg" alt="Case 385 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar gerçek görüntülerin üzerine hareketli grafiklerin eklendiği bir Fable 5.2 efekt testi paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-386"></a>
### Case 386: [GTA Aranma Seviyelerini Anlatan Animasyon](https://x.com/saimagnate/status/2119931563760632311) (üreten [@saimagnate](https://x.com/saimagnate))

**Oyun mekaniğini açıklarken oyun görüntüleriyle diyagramları birleştirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5adedb3da512c769262399da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31cc3c3f927d6e7a4f329bc5.jpg" alt="Case 386 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, Fable 5.2 ile tek istekte sonuç aldığını bildiriyor. Video, GTA V ile RDR2'nin aranma sistemlerini oyun görüntüleri ve diyagramlarla karşılaştırıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-387"></a>
### Case 387: [Kodla oluşturulan stilize MMO dünyası](https://x.com/Izkimar/status/2119931740940640542) (üreten [@Izkimar](https://x.com/Izkimar))

**Dünya tutarlılığını stilize öğeler üzerinden değerlendirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a55db5cfb9de540e7a7d692f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ef14e9adb025980557290e38.jpg" alt="Case 387 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, gösterilen MMO dünyasını bir günde kurduğunu ve öğeleri kodla ürettiğini belirtiyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-388"></a>
### Case 388: [Fable ve Opus ile 3B sahne](https://x.com/dom_scholz/status/2119933150025363661) (üreten [@dom_scholz](https://x.com/dom_scholz))

**Kurulum süresini ve ayrıntıları tek görünümde karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5b95a4cf1e5f0df9648ebd03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/86f182a05174d0d766495cd7.jpg" alt="Case 388 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ve Opus 5.5 görselleştirmelerini birlikte gösteriyor ve Fable’ın daha hızlı tamamladığını bildiriyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-389"></a>
### Case 389: [Oyun duraklatma ekranında gereksiz metin](https://x.com/AndrewPrifer/status/2119934600608915465) (üreten [@AndrewPrifer](https://x.com/AndrewPrifer))

**Üretilen arayüz metninde tekrarlanan açıklamaları arayın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a1f6aa1990f7c8580b9d6df.jpg" alt="Case 389 · 1" width="760">

Geliştirici, Fable 5.2’nin gerekenden fazla açıklama yazmasına örnek olarak bir duraklatma ekranı gösteriyor.

Type: Limit | Date: 2026-11-10

---

<a id="case-390"></a>
### Case 390: [Krea ortamıyla ilham panoları](https://x.com/lambdacalcc/status/2119934725662060663) (üreten [@lambdacalcc](https://x.com/lambdacalcc))

**Görsel yönü seçmeden önce fikirleri karşılaştırın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/55fd19628867c71d3fab0e87.jpg" alt="Case 390 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c82e767185af7003aee1f137.png" alt="Case 390 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/31a45c26f73a01003f94e395.png" alt="Case 390 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f468d8e4fbf862d50b00f685.jpg" alt="Case 390 · 4" width="450"></td></tr></table>

Yazar Krea ortamında Fable 5.2 ile hazırlanan dört ilham panosu sonucu paylaşıyor.

Type: Integration | Date: 2026-11-10

---

<a id="case-391"></a>
### Case 391: [Portal temalı nişancı oyununun ofis testi](https://x.com/_sholtodouglas/status/2119935331499925557) (üreten [@_sholtodouglas](https://x.com/_sholtodouglas))

**Üretilen oyunu çok oyunculu oturumlarda değerlendirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bcd1207a213dae8138ad294f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e4d546440c1a2e8fe81a63cb.jpg" alt="Case 391 · 1" width="760"><br>▶ Videoyu oynat</a>

Bir Anthropic mühendisi portallı bir arena FPS’i gösteriyor ve ofisteki deneme maçlarını anlatıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-392"></a>
### Case 392: [Blender’da ayrıntılı sert yüzey modeli](https://x.com/ziwenxu_/status/2119937420280168929) (üreten [@ziwenxu_](https://x.com/ziwenxu_))

**Topolojiyi ve silueti Blender görünümünde inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37270269488a3f35f882385d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/34ffedde747e32f211cd91f6.jpg" alt="Case 392 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, Fable 5.2 Blender çıktısı olarak sunduğu ayrıntılı bir sert yüzey modelini paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-393"></a>
### Case 393: [Farklı çaba düzeylerinde paralel arayüz testleri](https://x.com/AI_masaou/status/2119937635322085640) (üreten [@AI_masaou](https://x.com/AI_masaou))

**Basit ve iddialı tarifleri farklı çaba düzeylerinde karşılaştırın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c55726b163f0c43c2108d64d.jpg" alt="Case 393 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f25c0c20720327c56de45a15.jpg" alt="Case 393 · 2" width="450"></td></tr></table>

Yazar, basit çıktıları benzer bulduğunu, daha büyük Fable çalışmalarında daha zengin ayrıntılar gördüğünü ve Medium ile High arasında süre ve token tüketiminin belirgin arttığını bildiriyor.

[İlgili kaynaklar 1](https://x.com/AI_masaou/article/2119937635322085640)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-394"></a>
### Case 394: [On istemle hazırlanan küçük oyun](https://x.com/AmirMushich/status/2119937977426338283) (üreten [@AmirMushich](https://x.com/AmirMushich))

**İterasyon sayısını ve prototip boyutunu kaydedin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3a7790b768da97455f3d118.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c466b6b77bdc0fe3dbeffbc8.jpg" alt="Case 394 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar yaklaşık 3400 satırlık, 220 KB boyutunda bir oyun bildiriyor ve kod ile videoyu paylaşıyor.

[İlgili kaynaklar 1](https://github.com/amirmushichge/worm-rider)

Type: Demo | Date: 2026-11-10

---

<a id="case-395"></a>
### Case 395: [JavaScript ile kare kare animasyon](https://x.com/kevin_t_ngo/status/2119938129079808282) (üreten [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Kareleri programla çizilen bir sekansı inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c39a0369984d92a12e223e1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/70387b28ce12f432b24343a8.jpg" alt="Case 395 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar animasyonu paylaşıyor ve her kareyi JavaScript’in çizdiğini belirtiyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-396"></a>
### Case 396: [Referans videodan 3B animasyona](https://x.com/KHvostikk/status/2119939061049889130) (üreten [@KHvostikk](https://x.com/KHvostikk))

**Yeniden kurulan sahneyi değerlendirirken kaynak görüntüleri kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c141a7a9178bfe910966548e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/90814ab3239232dfb2299b1c.jpg" alt="Case 396 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ile videodan 3B animasyona dönüşüm gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-397"></a>
### Case 397: [Fable ve Opus ile piksel kamp ateşi](https://x.com/GrilliotTodd/status/2119939651385655692) (üreten [@GrilliotTodd](https://x.com/GrilliotTodd))

**Aynı piksel sanatı konusu üzerinde ışık ve siluetleri karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/35b1a7be25723d5e1bd13340.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/61568e70f257333e83e0cc14.jpg" alt="Case 397 · 1" width="760"><br>▶ Videoyu oynat</a>

Yan yana sonuçlarda Fable 5.2 ve Opus 5.5’in kamp ateşi çizimleri görülüyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-398"></a>
### Case 398: [xHigh ayarında Arena WebDev](https://x.com/arena/status/2119941204003770690) (üreten [@arena](https://x.com/arena))

**Sıralamada kullanılan çaba ayarını dikkate alın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3cbd6d793e779219f101b55.jpg" alt="Case 398 · 1" width="760">

Arena, Claude Fable 5.2 xHigh’ın Code Arena WebDev’e 1832 puanla giriş yaptığını bildiriyor.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-399"></a>
### Case 399: [İki modelle film fragmanı tipografisi](https://x.com/muku_sns/status/2119941490969624679) (üreten [@muku_sns](https://x.com/muku_sns))

**Aynı paragrafın iki yorumunu karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/bee4623c21a86cd5d4dc4d13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8e1468901c8f2a0a970a13b1.jpg" alt="Case 399 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Opus ve Fable’ın fragman başlıklarını yan yana gösteriyor. Fable sürümü kırmızı kenarlık ve karartılmış başlıklar ekliyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-400"></a>
### Case 400: [Tek istemle hareketli tasarım ve 3B portföy testleri](https://x.com/Khazix0918/status/2119941585538572390) (üreten [@Khazix0918](https://x.com/Khazix0918))

**Araştırma, tasarım ve görüntü işlemeyi ayrı ayrı sınayın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/09294ed8fc0f7be597f72dc0.png" alt="Case 400 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fb625dfe20ed5cfe3ef34ac9.jpg" alt="Case 400 · 2" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/52db3c1d40d900766444f8d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/387de7c8f500b3503bb18f18.jpg" alt="Case 400 · 3" width="450"><br>▶ Videoyu oynat</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7000a24c9cbe5f27e17d2465.png" alt="Case 400 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bcb9dd989af7fff138ed8fa.jpg" alt="Case 400 · 5" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/834d60f7ebd040f6c21aeb80.jpg" alt="Case 400 · 6" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/286cb83f293951f5acc981bf.png" alt="Case 400 · 7" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6ba9dbf16c076efe467ddd86.jpg" alt="Case 400 · 8" width="450"></td></tr><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/22091edfeabf27e0d244be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/40755737d0e315a653665d3d.jpg" alt="Case 400 · 9" width="450"><br>▶ Videoyu oynat</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/315fe812bfd8b0721e92f362.png" alt="Case 400 · 10" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/37752a7b49874dd54644c2de.jpg" alt="Case 400 · 11" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/517912ea3de4206e75472f13.jpg" alt="Case 400 · 12" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f5c1cfcb5ae5f7b1d6190ff1.jpg" alt="Case 400 · 13" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1f1ac47986ef7c5ae3806a6c.jpg" alt="Case 400 · 14" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7d470171b1d2ab82d064c220.jpg" alt="Case 400 · 15" width="450"></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e5a492a58cba090b6a9483a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ba7146a003f1c72b0ff53ef9.jpg" alt="Case 400 · 16" width="450"><br>▶ Videoyu oynat</a></td></tr></table>

Yazar, ChatGPT yıl dönümü klibi, DeepSeek anlatımı, Three.js sahnesi ve Apple Jing’an’ın 3B canlandırmasını içeren dört deneme paylaşıyor.

[İlgili kaynaklar 1](https://x.com/Khazix0918/article/2119941585538572390)

Orijinal istem

```
做一支 40 秒到 1 分钟的 ChatGPT 四周年致敬动效视频（2022.11.30–2026.11.30），16:9 横版，无旁白，配原创音乐。内容自己联网查证，讲这四年的关键版本、里程碑和数字，不得杜撰。动手前先去 OpenAI 官网、博客和近期发布视频里观察他们的视觉风格，提炼后作为这支片子的视觉基调。节奏要快，动效密、画面饱满，随音乐卡点。片子定位是第三方致敬，不要做成 OpenAI 官方出品的样子。
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-401"></a>
### Case 401: [Keşfedilebilir nükleer reaktör anlatımı](https://x.com/konstantinsaifo/status/2119941967136379334) (üreten [@konstantinsaifo](https://x.com/konstantinsaifo))

**Parçaların nasıl birleştiğini sökme etkileşimiyle gösterin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/11840e17106c0bdf60374010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f6963c836c5837eac19511a.jpg" alt="Case 401 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Three.js’de sökülebilir bir reaktör istedi ve 92 ABD doları API masrafı bildirdi.

Type: Demo | Date: 2026-11-10

---

<a id="case-402"></a>
### Case 402: [Blood on the Clocktower’da ajanlar](https://x.com/dwarkesh_sp/status/2119942657812451482) (üreten [@dwarkesh_sp](https://x.com/dwarkesh_sp))

**Modelleri aynı gizli rol oyununda karşılaştırın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c3562a2b864f07dfa8ba9dc.jpg" alt="Case 402 · 1" width="760">

Değerlendirmede Fable 5.2, Fable 5.1 ve Opus 5.5’in önünde yer alıyor. GPT-6 Astra bu testte daha ileride.

[İlgili kaynaklar 1](https://clocktowerbench.com/)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-403"></a>
### Case 403: [Pod yarışı prototipi](https://x.com/loktar00/status/2119943124965638444) (üreten [@loktar00](https://x.com/loktar00))

**Hareket ve kontrolleri değerlendirmek için tanıdık bir yarış biçimi kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd09ca633da910aa6e6d437a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7bd3dfe7b4e26a85dc40087a.jpg" alt="Case 403 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar pod yarışlarından esinlenen bir Fable 5.2 çıktısı paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-404"></a>
### Case 404: [On saniyelik Claude iç çamaşırı reklamı](https://x.com/Masimo_Blue/status/2119943368612487285) (üreten [@Masimo_Blue](https://x.com/Masimo_Blue))

**Özgün müzikle açık uçlu bir ürün tarifini sınayın.**

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/329b7fd8f8a84cc8724e06c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fd6181a6ff78f66fa995e4ab.jpg" alt="Case 404 · 1" width="450"><br>▶ Videoyu oynat</a></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f63f12faeb2f173c0eb17172.jpg" alt="Case 404 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01b08e8189af5d473733318c.jpg" alt="Case 404 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e1e83fbf08adc14580e1e560.jpg" alt="Case 404 · 4" width="450"></td></tr></table>

Yazar, verilen ürün görsellerini ve acid techno müziğini kullanan on saniyelik reklamı paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-405"></a>
### Case 405: [Gün doğumunda bir kuş, çizgi çizgi](https://x.com/mgrczyk/status/2119943813028548721) (üreten [@mgrczyk](https://x.com/mgrczyk))

**Ardışık çizim kararlarını gözlemlemek için geri almayı devre dışı bırakın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3511418d70567425e70497c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/073bc3917d82b10149bcee86.jpg" alt="Case 405 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, önceki çizgilerin değiştirilemediği bir ortamda gün doğumunda resmedilen kuşu gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-406"></a>
### Case 406: [Devin’de uzun bir grafik çalışması](https://x.com/Da7_Tech/status/2119944847255896490) (üreten [@Da7_Tech](https://x.com/Da7_Tech))

**Zorlu bir görselleştirmede süre ve masrafı kaydedin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/be08a176e815fa46453b51c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2fe8a92de2aa1a6ae809a964.jpg" alt="Case 406 · 1" width="760"><br>▶ Videoyu oynat</a>

Cognition elçisi olduğunu belirten yazar, yaklaşık 82 ABD doları ve 3,5 saatlik bir Devin Max çalışması paylaşıyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-407"></a>
### Case 407: [Üç modelle koddan resim](https://x.com/kickingkeys/status/2119945841997672698) (üreten [@kickingkeys](https://x.com/kickingkeys))

**Çizim hareketlerini ve sentezlenmiş sesi karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/fdfaf999bd215ba743e68a82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/178877a1e48defde7e90dc1a.jpg" alt="Case 407 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar kodla yapılmış sesli bir resim paylaşıyor ve Fable 5.2, Fable 5.1 ve Gemini 4 Argon ile aynı istemi kullandığı testleri anlatıyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-408"></a>
### Case 408: [Hareketli anlatımla yazının tarihi](https://x.com/rileybrown/status/2119946022767980985) (üreten [@rileybrown](https://x.com/rileybrown))

**Kodla hazırlanan bir anlatımı zaman çizelgesiyle düzenleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a79f598d47fa73f06527d56e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/97da3453a07c08e5ee982a3d.jpg" alt="Case 408 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar yazının tarihi animasyonunu gösteriyor ve tek istemle yaptığını belirtiyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-409"></a>
### Case 409: [Oyun makineleri için test alanı](https://x.com/techartist_/status/2119946891106394518) (üreten [@techartist_](https://x.com/techartist_))

**Mekanik, fizik ve efektleri aynı sahnede sınayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/156fe650e1324950d1b79302.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8abf053e72d1aa9b66553118.jpg" alt="Case 409 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Three.js ve Blender ile dört fikir için bir deneme alanı yaptı.

Type: Demo | Date: 2026-11-10

---

<a id="case-410"></a>
### Case 410: [Taşınabilir Linux konsolu için PCB tasarımı](https://x.com/seveibar/status/2119947341230907453) (üreten [@seveibar](https://x.com/seveibar))

**Modelleri aynı devre tarifiyle karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/48bc04eaedb2a9096e630447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4226f1f1305f93fb2f40ec48.jpg" alt="Case 410 · 1" width="760"><br>▶ Videoyu oynat</a>

tscircuit geliştiricisi, Astra 6 High ve Fable 5.2 High ile taşınabilir Linux oyun cihazı tasarım testini gösteriyor.

Orijinal istem

```
Design handheld linux gaming device using tscircuit
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-411"></a>
### Case 411: [Voksel gölü](https://x.com/Angaisb_/status/2119947748690841841) (üreten [@Angaisb_](https://x.com/Angaisb_))

**Kompozisyonu küçük bir ortamla değerlendirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f14b9d0930dda721f141f963.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/77b942ac4aa66eaadd58b609.jpg" alt="Case 411 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2’ye atfettiği bir voksel gölü paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-412"></a>
### Case 412: [Arena’dan 17 etkileşimli üretim](https://x.com/arena/status/2119948067449536733) (üreten [@arena](https://x.com/arena))

**Bir test görevi seçmeden önce farklı çıktı türlerine bakın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5f8bb8798f552bf82f9d7938.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/01fc53e51ef5352f6310e8a6.jpg" alt="Case 412 · 1" width="760"><br>▶ Videoyu oynat</a>

Arena; 3B dünyalar, oyunlar, arayüzler, veri görselleştirmeleri ve kodlanmış animasyonlar dahil 17 üretim paylaşıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-413"></a>
### Case 413: [Dost canlısı bir ejderhayla uçuş](https://x.com/chetanankola/status/2119951015407738913) (üreten [@chetanankola](https://x.com/chetanankola))

**Kamera ve hareketi bir uçuş döngüsüyle sınayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b8c29a140b65ad1c827f5db2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1cebba9f7f320aed8bf56eac.jpg" alt="Case 413 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Three.js ve Blender ile yapılmış bir ejderha sahnesi paylaşıyor ve Fable 5.2 ile yapılan iyileştirmeleri anlatıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-414"></a>
### Case 414: [Fable ve Opus ile jelatin orka](https://x.com/vib3coded/status/2119951060752375827) (üreten [@vib3coded](https://x.com/vib3coded))

**Aynı konuda yüzeyi ve hareketi karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3f4aa77103c3a580cf74e81b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/395e556b54fcb5d9e12f8ac2.jpg" alt="Case 414 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2 ve Opus 5.5’in jelatin orkalarını yan yana gösteriyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-415"></a>
### Case 415: [Açık uçlu video kalitesi testi](https://x.com/suna_gaku/status/2119952985933697063) (üreten [@suna_gaku](https://x.com/suna_gaku))

**Modelin yaratıcı kararlarını görmek için açık bir tarif verin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/d3be65becd13d9a0b831d4f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5ff67dcd378ba3ef35fe1ac2.jpg" alt="Case 415 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar modelden en iyi videosunu yapmasını istedi ve sonucu paylaştı.

Orijinal istem

```
今の実力を見せつける最強の動画を見せて
```

Type: Demo | Date: 2026-11-10

---

<a id="case-416"></a>
### Case 416: [Akdeniz temalı uzay habitatı](https://x.com/MaxXWilliamson/status/2119953172634677533) (üreten [@MaxXWilliamson](https://x.com/MaxXWilliamson))

**Kısa bir tarifi mevcut proje araçlarıyla birleştirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/3204db42b62faeec40c87290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/e0f0b919a659cba4de7ef7e1.jpg" alt="Case 416 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar daha önceki uzay habitatı çalışmalarında kullandığı araçları verip Akdeniz temalı bir istasyon istedi.

Type: Demo | Date: 2026-11-10

---

<a id="case-417"></a>
### Case 417: [Etkileşimli deneyimler için AA-3D benchmark’ı](https://x.com/ArtificialAnlys/status/2119953570430881946) (üreten [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Elo puanını belirsizlik aralığıyla okuyun.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730c30a7cd064b9496b28347.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cc3e2370eff4a3329232131c.jpg" alt="Case 417 · 1" width="760"><br>▶ Videoyu oynat</a>

Artificial Analysis, etkileşimli 3B benchmark’ında Fable 5.2 Max için ilk ölçümde 1271 Elo yayımladı.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-418"></a>
### Case 418: [Süreli iskelet karakteri oyunu](https://x.com/WesRoth/status/2119953913160093817) (üreten [@WesRoth](https://x.com/WesRoth))

**Oynanabilir prototipi görünür bir sayaçla değerlendirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b1c8eb524d8f0d51037a8c31.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7823fc3e0283317623f1b3c3.jpg" alt="Case 418 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable 5.2’nin tek istemle ürettiği, iskelet karakteri ve ekranda geri sayım olan bir sonuç gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-419"></a>
### Case 419: [Fable ve Astra ile piksel sanatı](https://x.com/Angaisb_/status/2119955179915137294) (üreten [@Angaisb_](https://x.com/Angaisb_))

**Şekil ve ayrıntıları aynı ölçekte karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0595d47673a4d164c5b0eebb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f6941e6fce47147e79a4ed5f.jpg" alt="Case 419 · 1" width="760"><br>▶ Videoyu oynat</a>

Özgün karşılaştırmada GPT-6 Astra ve Fable 5.2’nin piksel sanatı çıktıları yer alıyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-420"></a>
### Case 420: [Hareketli tasarım portföyü videosu](https://x.com/Leviwoyun/status/2119955625820258308) (üreten [@Leviwoyun](https://x.com/Leviwoyun))

**Süresi sabit, yaratıcı yönü açık bir tarif kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0f1f5c9ae6b0a3cd64d6b9cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8c7eed599c0c90f61eb12d92.jpg" alt="Case 420 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar müzikli portföy videosunu paylaşıyor ve yapımın 24 dakika sürdüğünü belirtiyor.

Orijinal istem

```
制作一段 30 秒动态图形短片，展现作为动态设计师出众的实力，就当做用于简历的个人作品集，请尽情发挥
```

Type: Demo | Date: 2026-11-10

---

<a id="case-421"></a>
### Case 421: [İki modelle cam havuz görselleştirmesi](https://x.com/MrTacticalX/status/2119955647542542439) (üreten [@MrTacticalX](https://x.com/MrTacticalX))

**Aydınlatmayı süre ve maliyetle birlikte karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/74cc630deb84e0066affb15d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2a9144e6e185b847b01b7b4c.jpg" alt="Case 421 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar Fable için 90 dakika ve 57,87 ABD doları, Opus için 68 dakika ve 14,39 ABD doları bildiriyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-422"></a>
### Case 422: [TS-Bench’te araç çağrısı doğruluğu](https://x.com/gosrum/status/2119956559031927079) (üreten [@gosrum](https://x.com/gosrum))

**Çağrı hatalarını ve token kullanımını ayrı takip edin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c9b5bc5d81051efe658cfba.jpg" alt="Case 422 · 1" width="760">

Testi yapan kişi, Fable 5.2’de araç çağrısı hatası görmediğini ve basit görevlerin Claude sürümlerini ayırt etmekte yetersiz kaldığını belirtiyor.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-423"></a>
### Case 423: [Minyatür Machu Picchu](https://x.com/loktar00/status/2119958719362666708) (üreten [@loktar00](https://x.com/loktar00))

**Minyatür sahnenin atmosferini ve küçük ayrıntılarını inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b98ba690496144704ebac2c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c1d0f95291b21092f925992b.jpg" alt="Case 423 · 1" width="760"><br>▶ Videoyu oynat</a>

Machu Picchu demosunda hacimsel sis ve küçük alpakalar yer alıyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-424"></a>
### Case 424: [Mesleki görev kategorilerine göre GDPx](https://x.com/SemiAnalysis_/status/2119961447199289640) (üreten [@SemiAnalysis_](https://x.com/SemiAnalysis_))

**Alt görev sonuçlarını toplam puanla birlikte okuyun.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/63c9f6198650d5778e1f1d04.jpg" alt="Case 424 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/5673e82da7c5ee3d0a53680b.jpg" alt="Case 424 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f0cb08440e517a003e7e0dc4.jpg" alt="Case 424 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f3ce6b38febadaadb789b8e7.jpg" alt="Case 424 · 4" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1ada0710dbff750e216a737d.jpg" alt="Case 424 · 5" width="450"></td></tr></table>

Benchmark yayıncısı %16,4 toplam puan bildiriyor ve çip tasarımı ile yazılım mühendisliği gibi alanları ayrı inceliyor.

[İlgili kaynaklar 1](https://x.com/SemiAnalysis_/status/2119961456716189764) · [İlgili kaynaklar 2](https://x.com/SemiAnalysis_/status/2119961452496756926) · [İlgili kaynaklar 3](https://x.com/SemiAnalysis_/status/2119961448465997846)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-425"></a>
### Case 425: [Bir Çizim Uygulamasında Portre](https://x.com/The_Alex/status/2119964472559489229) (üreten [@The_Alex](https://x.com/The_Alex))

**Portreyi küçük bir referans görselle yönlendirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/dbe6dc4a1520e2813282f632.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c570e267faea809c9560d196.jpg" alt="Case 425 · 1" width="760"><br>▶ Videoyu oynat</a>

İçerik üreticisi Fable 5.2'den bir çizim uygulaması açıp portresini çizmesini istedi. Video, ilk çizgilerden bitmiş portreye kadar süreci gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-426"></a>
### Case 426: [Low ayarında VulcanBench Frontier v4](https://x.com/morganlinton/status/2119966067527467215) (üreten [@morganlinton](https://x.com/morganlinton))

**Model nesillerini aynı çaba düzeyinde karşılaştırın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2ca6ab5c74d326ff18ca4dac.png" alt="Case 426 · 1" width="760">

Benchmark yazarı, Low ayarında Fable 5.2 için görev başına yaklaşık 5 dakika, Fable 5.1 için 26 dakika bildiriyor.

Type: Benchmark | Date: 2026-11-10

---

<a id="case-427"></a>
### Case 427: [Oynanabilir Backrooms’da roller tersine dönüyor](https://x.com/LexnLin/status/2119966127149429093) (üreten [@LexnLin](https://x.com/LexnLin))

**Bir oyun fikrini sınamak için oyuncunun hedefini değiştirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/9f538302d8c0ba95cb908bf4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/c54a5ee73eed3e46864ec9a9.jpg" alt="Case 427 · 1" width="760"><br>▶ Videoyu oynat</a>

Oyuncu canavarı yönetip insanları yakalamaya çalışıyor. Yazar oynanış videosu ve oyun bağlantısı paylaşıyor.

[İlgili kaynaklar 1](https://feed-backrooms.vercel.app)

Type: Demo | Date: 2026-11-10

---

<a id="case-428"></a>
### Case 428: [Blender’da Bugatti Tourbillon](https://x.com/xikhar/status/2119966147328299284) (üreten [@xikhar](https://x.com/xikhar))

**İç ve dış ayrıntıları belirlemek için referans görseller kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a183adc38399689cfd61d444.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a3ee9de66b42a6db86e005a1.jpg" alt="Case 428 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, bir istem ve referanslarla iç mekânı dahil Bugatti Tourbillon’u modelleyip sinematik bir sekans işlediğini belirtiyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-429"></a>
### Case 429: [İki modelle hazırlanan bilgisayar temalı video](https://x.com/daradoescode/status/2119966154391183522) (üreten [@daradoescode](https://x.com/daradoescode))

**Karma iş akışında her modelin katkısını kaydedin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cbb652cf30f17b9ace409879.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/de9b2035b7d63747fa569c1e.jpg" alt="Case 429 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, Fable 5.2 ve Opus 5.5’in önemli katkısıyla hazırlanan stilize bir video paylaştı.

Type: Demo | Date: 2026-11-10

---

<a id="case-430"></a>
### Case 430: [Megakernel konulu müzik klibi](https://x.com/elliotarledge/status/2119968762069934415) (üreten [@elliotarledge](https://x.com/elliotarledge))

**Teknik bir kavramı video konusu olarak kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0a42287bf088732191b41048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/8a072be29416df52b2b669c4.jpg" alt="Case 430 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, High ayarındaki Fable 5.2’den megakernel konulu bir müzik klibi istedi ve sonucu paylaştı.

Type: Demo | Date: 2026-11-10

---

<a id="case-431"></a>
### Case 431: [Referans fotoğraflarından stüdyo turu](https://x.com/rpnickson/status/2119969928304357507) (üreten [@rpnickson](https://x.com/rpnickson))

**Bir sahneyi yeniden kurarken gerçek fotoğrafları kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/cd6052e81d387ab468ab314e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/2aefe138d7ef7bd6219c31bc.jpg" alt="Case 431 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar stüdyosunun fotoğraflarını verdi, benzer bir video tarifini uyarladı ve işlemin yaklaşık iki saat sürdüğünü bildirdi.

Type: Demo | Date: 2026-11-10

---

<a id="case-432"></a>
### Case 432: [Kodla hazırlanan 1990’lar oyuncak reklamı](https://x.com/kevin_t_ngo/status/2119972124211454139) (üreten [@kevin_t_ngo](https://x.com/kevin_t_ngo))

**Animasyon betiklerini görüntü işlemeden ayırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/730a1f40be0003005200a1a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/094c01817aa5b71ac790aaaa.jpg" alt="Case 432 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, nostaljik oyuncak reklamını Python ile canlandırıp Blender’da işlediğini belirtiyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-433"></a>
### Case 433: [Three.js ile üçüncü şahıs oyun sahnesi](https://x.com/bijanbowen/status/2119972220739187182) (üreten [@bijanbowen](https://x.com/bijanbowen))

**Hareketi ve ortamı oynanış üzerinden inceleyin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/7c3bfda53634766fd3b7c0bb.jpg" alt="Case 433 · 1" width="760">

Yazar, açık bir alanda ilerleyen üçüncü şahıs karakterini içeren Three.js sonucunu yayında gösteriyor.

Type: Demo | Date: 2026-11-10

---

<a id="case-434"></a>
### Case 434: [Mevcut işleyiciden Bryceball](https://x.com/pleometric/status/2119973274402668852) (üreten [@pleometric](https://x.com/pleometric))

**Bir görüntü işleme motorunu oyunun temeli olarak kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ee3fb95d435e0bc021f0f4e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/461645af9276bdee5b31d9ca.jpg" alt="Case 434 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, bağlantıdaki işleyiciyi oynanabilir Bryceball oyununa uyarladı.

Type: Demo | Date: 2026-11-10

---

<a id="case-435"></a>
### Case 435: [Fable ile özyinelemeli video kurgusu](https://x.com/rileybrown/status/2119973951027724385) (üreten [@rileybrown](https://x.com/rileybrown))

**Önceki kurguyu yeni bir çalışma için malzeme olarak kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/0c9595d630dd1857ac874605.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4ffb7df28dbe2a6a1f48f862.jpg" alt="Case 435 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, daha önce modelle kurguladığı bir videoyu anlatan ve yine Fable 5.2 ile kurgulanan bir video paylaştı.

Type: Demo | Date: 2026-11-10

---

<a id="case-436"></a>
### Case 436: [Bilim tarihine sinematik bir yolculuk](https://x.com/DeryaTR_/status/2119974354260013293) (üreten [@DeryaTR_](https://x.com/DeryaTR_))

**3B sekansı bir zaman çizelgesiyle düzenleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/a82420b6f66285ae7b95ab74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/30d168caba043849aa02ccad.jpg" alt="Case 436 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, bilimin ilk dönemlerinden varsayımsal bir geleceğe uzanan sinematik bir yolculuk istedi ve ortaya çıkan videoyu paylaştı.

Type: Demo | Date: 2026-11-10

---

<a id="case-437"></a>
### Case 437: [Da Vinci’nin uçan makinesi 3B ortamda](https://x.com/higgsfield_ai/status/2119975721909301684) (üreten [@higgsfield_ai](https://x.com/higgsfield_ai))

**Değişiklikleri denemeden önce tarihî tasarımı modelleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/726310d892c26109879655b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/617432609a4731a7dbcb5806.jpg" alt="Case 437 · 1" width="760"><br>▶ Videoyu oynat</a>

Higgsfield, Leonardo’nun uçan makinesinin 3B yorumunu gösterdi ve fizik testiyle yeniden tasarım sürecini anlattı.

Type: Integration | Date: 2026-11-10

---

<a id="case-438"></a>
### Case 438: [Bir tasarım tarifinden PCB hat yönlendirmesi](https://x.com/cmonkey/status/2119975852977029365) (üreten [@cmonkey](https://x.com/cmonkey))

**Üretimden önce hatları çizilmiş kartı inceleyin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/4d8b14f9d0fc79b63afa77d3.jpg" alt="Case 438 · 1" width="760">

Yazar, kart yerleşimi tartışmasına yanıt olarak Fable 5.2’nin PCB hat yönlendirme sonucunu paylaştı.

Type: Demo | Date: 2026-11-10

---

<a id="case-439"></a>
### Case 439: [Farklı çalışma ortamlarında aynı istem](https://x.com/loktar00/status/2119980613369319706) (üreten [@loktar00](https://x.com/loktar00))

**Sonuçları karşılaştırırken ortam farklarını kaydedin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/81415e048aee983349383d93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/44a96173b2e880641cbbe2ff.jpg" alt="Case 439 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar DeepSeek ve Fable 5.2’ye farklı ortamlarda aynı istemi verdi ve sonuçları yan yana gösterdi.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-440"></a>
### Case 440: [Kodla çizilmiş Godzilla görseli](https://x.com/chetaslua/status/2119981510199808368) (üreten [@chetaslua](https://x.com/chetaslua))

**Bir görseli vektör benzeri şekiller ve hareketle yeniden yorumlayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/1fe62f775d3dcd7a180b3d68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ca40cead4c363d8348616185.jpg" alt="Case 440 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, bir Godzilla paylaşımından esinlenen kodla çizilmiş bir görsel ve kısa animasyon yayımladı.

Type: Demo | Date: 2026-11-10

---

<a id="case-441"></a>
### Case 441: [3B baskı için el tipi vantilatör](https://x.com/davelee/status/2119981787325579398) (üreten [@davelee](https://x.com/davelee))

**Montajı fiziksel bir prototiple kontrol edin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/b32230a3f0a69db0b2632288.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/856b34dd10dd4c118ad129e0.jpg" alt="Case 441 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar ve çocukları basılabilir bir el vantilatörü tasarlayıp modeli baskıdan önce paylaştı.

Type: Demo | Date: 2026-11-10

---

<a id="case-442"></a>
### Case 442: [Opus ile eklenti hatası avı](https://x.com/oaranda/status/2119982729747919096) (üreten [@oaranda](https://x.com/oaranda))

**Düzeltmeleri çapraz regresyon testleriyle karşılaştırın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/47881ab281850bba95544be6.png" alt="Case 442 · 1" width="760">

Yazarın not eklediği duyuru alıntısı.

İki model de aynı altı eklenti hatasını buldu. Opus çapraz testleri geçti. Fable bir testte başarısız oldu ve panelde başka bir sorun buldu.

Orijinal istem

```
Bugs CONFIRMADOS (no especulación): línea, qué falla, entrada concreta que lo dispara, y la reproducción que corriste
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-443"></a>
### Case 443: [3B sahnede yeniden kurulan İstanbul](https://x.com/petergostev/status/2119877733488394520) (üreten [@petergostev](https://x.com/petergostev))

**Kent sahnesini geniş ve yakın açılardan inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/10ffdee8a0f23e2844489ea8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/f043bbd9078ba36d8d3b05f6.jpg" alt="Case 443 · 1" width="760"><br>▶ Videoyu oynat</a>

Peter Gostev, Fable 5.2 Max ile elde edilen 3B İstanbul sahnesini ve daha kapsamlı değerlendirme bağlantısını paylaşıyor.

[İlgili kaynaklar 1](https://www.youtube.com/watch?v=QwaU4yU0PdQ)

Type: Demo | Date: 2026-11-10

---

<a id="case-444"></a>
### Case 444: [Çalışan ekranlı bir Blender filmi](https://x.com/rileybrown/status/2119902109709537708) (üreten [@rileybrown](https://x.com/rileybrown))

**Ekranı, ışığı ve kamerayı aynı 3B sahnede canlandırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/ad72b04f7c14dca3693131c9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-10/6d60e34d1ab5f831a06f5ff5.jpg" alt="Case 444 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar 13 kamera planı, dizüstü ekranda çalışan özel bir web sayfası ve ElevenLabs sesi bildiriyor. Görüntü işleme RunPod GPU’larında yapıldı.

Type: Demo | Date: 2026-11-10

---

<a id="case-445"></a>
### Case 445: [Zayıf bağlaşımda kara delik geçişi](https://hexagonmath.org/2611.00175v1) (üreten [@Anthropic](https://www.anthropic.com/))

**Yarım kalmış hesabı özgün kuramsal çerçeveye göre kontrol edin.**

Anthropic, Fable 5.2’nin uzun süredir açık olan bir hesabı tamamlayıp zayıf bağlaşımda ani geçiş bulduğunu bildiriyor. Ön baskı türetimi içeriyor.

[İlgili kaynaklar 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-446"></a>
### Case 446: [Modüler bootstrap sınırının limiti](https://hexagonmath.org/2611.00174v1) (üreten [@Anthropic](https://www.anthropic.com/))

**Öne sürülen analitik sınırla birlikte türetimi yayımlayın.**

Anthropic, Fable 5.2’nin basitleştirilmiş kuantum kütleçekimi çerçevesinde spinsiz modüler bootstrap tekniğinin kesin limitini belirlediğini bildiriyor.

[İlgili kaynaklar 1](https://www.anthropic.com/claude-fable-and-mythos-5-2#theoretical-physics)

Type: Evaluation | Date: 2026-11-07

---

<a id="case-447"></a>
### Case 447: [Sıralı alternatif modellerle Vercel AI Gateway](https://vercel.com/changelog/claude-fable-5-2-now-available-on-ai-gateway) (üreten [Vercel](https://vercel.com/))

**Sınıflandırıcının reddettiği istekler için gateway’de alternatif model sırasını belirleyin.**

Vercel AI SDK örneği anthropic/claude-fable-5.2 modelini çağırıyor ve alternatif olarak önce Opus 5.5’i, ardından Sonnet 5.5’i ayarlıyor. Rehber veri saklama gereksinimini açıklıyor.

[İlgili kaynaklar 1](https://news.ycombinator.com/item?id=50430691)

Type: Integration | Date: 2026-11-09

---

<a id="case-448"></a>
### Case 448: [İç içe alt ajanlar ve inceleme bütçesi](https://news.ycombinator.com/item?id=50430925) (üreten [@TuxSH](https://news.ycombinator.com/user?id=TuxSH))

**İç içe görev dağıtımını izleyip bütçeyi istem dışında sınırlandırın.**

Yazar 80.000 satırlık kod incelemesi için en fazla dört alt ajan istedi. Altı veya daha fazla iç içe ajan ve 20 dakikadan kısa sürede tükenen beş saatlik kullanım hakkı bildiriyor.

Type: Limit | Date: 2026-11-09

---

<a id="case-449"></a>
### Case 449: [LCARS tasarımından HTML’e model karşılaştırması](https://news.ycombinator.com/item?id=50430962) (üreten [@jjcm](https://news.ycombinator.com/user?id=jjcm))

**Eğrileri, simgeleri, animasyonu ve gezinmeyi ayrı ölçütlerle kontrol edin.**

Yazar iki modeli aynı Star Trek tarzı tasarımla karşılaştırdı. Fable’ın eğrilerini ve bazı simgelerini, Opus’un hareketini tercih etti. Fable’ın SVG titremesini dikkat dağıtıcı buldu ve yalnızca ilk sayfayı istemişti.

[İlgili kaynaklar 1](https://html.non.io/lcars-fable-5.2/) · [İlgili kaynaklar 2](https://html.non.io/lcars-opus-5.5/) · [İlgili kaynaklar 3](https://news.ycombinator.com/item?id=50431231) · [İlgili kaynaklar 4](https://news.ycombinator.com/item?id=50431418)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-450"></a>
### Case 450: [Quantum ESPRESSO için GPU optimizasyonu](https://discoveredmaterials.com/research/accelerating-quantum-espresso/) (üreten [Discovered Materials](https://discoveredmaterials.com/))

**Bilimsel kodda referans sonuçları ve temsili gizli testleri şart koşun.**

Discovered Materials, aynı GPU’daki 13 fonon testinde geometrik ortalama olarak 36 kat, hibrit fonksiyonel hesaplarda yaklaşık 9 kat hızlanma bildiriyor. Yayımlanan yama doğruluk ve performans testlerine dayanıyor.

[İlgili kaynaklar 1](https://github.com/discovered-materials/dm_qe) · [İlgili kaynaklar 2](https://news.ycombinator.com/item?id=50430969)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-451"></a>
### Case 451: [Çaba düzeyine göre Artificial Analysis Intelligence Index](https://artificialanalysis.ai/models/claude-fable-5-2) (üreten [Artificial Analysis](https://artificialanalysis.ai/))

**Seçilen düzeyde puanı, görev maliyetini ve süreyi birlikte okuyun.**

Atıf yapılan varsayılan alternatifli Max ölçümünde indeks 65, görev başına maliyet 26,54 ABD doları ve süre 46,4 dakika. Değerler benchmark iş yüküne ait.

[İlgili kaynaklar 1](https://news.ycombinator.com/item?id=50431144)

Type: Benchmark | Date: 2026-11-09

---

<a id="case-452"></a>
### Case 452: [High düzeyinde değişiklik incelemesinde yanlış alarmlar](https://news.ycombinator.com/item?id=50431810) (üreten [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd))

**Harekete geçmeden model bulgularını kodda doğrulayın.**

Bir geliştirici, Fable 5.2 High’ın bir değişiklikte gerçekte bulunmayan iki sorunu işaretlediğini ve bunları kod bilgisiyle fark ettiğini bildiriyor.

Type: Limit | Date: 2026-11-09

---

<a id="case-453"></a>
### Case 453: [Otuz günlük programlama görevi](https://news.ycombinator.com/item?id=50432483) (üreten [@ariwilson](https://news.ycombinator.com/user?id=ariwilson))

**Aynı iş yükünde süreyi ve tamamlanan görev sayısını ölçün.**

Yazar, 30 görevin 26’sını Fable 5.2 ve Opus 5.5’in, 25’ini Fable 5.1’in çözdüğünü bildiriyor. Fable 5.2, 5.1’in süresinin 0,62 katını kullandı. Bildirilen güvenlik engeli yoktu.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-454"></a>
### Case 454: [Issız ada ekran koruyucusu](https://news.ycombinator.com/item?id=50432836) (üreten [@nzach](https://news.ycombinator.com/user?id=nzach))

**Ekran koruyucusunu incelemek için etkileşimli sayfayı açın.**

Show HN yazarı, Stranded with Claude adlı tarayıcıda çalışan ada sahnesini paylaşıyor. Yayımlanan sonuç etkileşimli bir canvas.

[İlgili kaynaklar 1](https://claude-castaway.zachy.dev/)

Type: Demo | Date: 2026-11-09

---

<a id="case-455"></a>
### Case 455: [High düzeyinde üç tarayıcı oyunu](https://senko.net/vibecode-bench/) (üreten [Senko Rašić](https://senko.net/))

**Oynanabilirliği ve görsel doğruluğu ayrı değerlendirin.**

Senko Rašić, gerçek zamanlı strateji, voksel ve uçuş simülatörü tariflerini Claude Code’da Fable 5.2 ile denedi. Tüm haritayı gezmeye yarayan hava gemisi gibi daha derin mekanikler gördü ve bazı grafikleri daha zayıf buldu.

[İlgili kaynaklar 1](https://news.ycombinator.com/item?id=50433004)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-456"></a>
### Case 456: [Bölüm bölüm kitap podcast’i metinleri](https://news.ycombinator.com/item?id=50434156) (üreten [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato))

**Aynı podcast görevinde metin uzunluklarını karşılaştırın.**

Yazar iki kitap eleştirmeninin konuşmalarını bölüm bölüm üretti. Fable sürümlerinin yaklaşık 2,5, Opus 5.5’in 4,5 sayfa olduğunu bildiriyor ve iki örneğe bağlantı veriyor.

[İlgili kaynaklar 1](https://claude.ai/share/274a96a8-c8a5-4564-9ca1-e914edffc722) · [İlgili kaynaklar 2](https://claude.ai/share/da8ab6bd-0987-47dc-9c26-68ebbfb25781)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-457"></a>
### Case 457: [Üretimdeki bir hizmetin Rust’a taşınması](https://www.anthropic.com/claude-fable-and-mythos-5-2#coding:~:text=Python%20to%20Rust) (üreten [@Anthropic](https://www.anthropic.com/))

**Taşıma öncesinde ve sonrasında açılış süresini ölçün.**

Anthropic, ön sürüm Fable 5.2 kullanan ajanların Python üretim hizmetini Rust ile yeniden yazıp açılış süresini yaklaşık 26 kat azalttığını bildiriyor.

Type: Evaluation | Date: 2026-11-09

---

<a id="case-458"></a>
### Case 458: [GitHub Copilot'ta Fable 5.2 Seçmek](https://x.com/github/status/2119926269982961833) (üreten [@github](https://x.com/github))

**Modeli seçmeden önce kuruluş ilkesini etkinleştirin.**

GitHub, Copilot model seçicisini ve Business ile Enterprise hesapları için gereken yönetici ayarını açıklıyor.

[İlgili kaynaklar 1](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/)

Type: Integration | Date: 2026-11-10

---

<a id="case-459"></a>
### Case 459: [Yüz HTML sayfası tasarlama denemesi](https://x.com/MiaAI_lab/status/2119930229661503893) (üreten [@MiaAI_lab](https://x.com/MiaAI_lab))

**Görünümün yanında tamamlanan ve çalışan dosyaları sayın.**

Yazar 100 farklı tasarım istedi, istemleriyle birlikte 76 dosya yayımladı ve Fable kullanım sınırına ulaştığını belirtti.

[İlgili kaynaklar 1](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/) · [İlgili kaynaklar 2](https://mia-ai.net/lab/experiments/100-htmls) · [İlgili kaynaklar 3](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/006-volcan-chico-hot-sauce.html) · [İlgili kaynaklar 4](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/009-koi-pond-noon.html) · [İlgili kaynaklar 5](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/016-vector-lunar-descent.html) · [İlgili kaynaklar 6](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/018-pen-plotter-landscapes.html) · [İlgili kaynaklar 7](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/025-pottery-wheel.html) · [İlgili kaynaklar 8](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/031-tangram-menagerie.html) · [İlgili kaynaklar 9](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/032-the-night-typist.html) · [İlgili kaynaklar 10](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/033-lava-lamp-1971.html) · [İlgili kaynaklar 11](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/041-jelly-alphabet.html) · [İlgili kaynaklar 12](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/044-ariadnes-thread.html) · [İlgili kaynaklar 13](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/048-cross-stitch-studio.html) · [İlgili kaynaklar 14](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/051-pinscreen.html)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-460"></a>
### Case 460: [Derleyici çalışmasında gereksinim sapması](https://x.com/sameQCU/status/2119939304864800971) (üreten [@sameQCU](https://x.com/sameQCU))

**Ajanın ifade ettiği gereksinimleri özgün girdiye göre kontrol edin.**

Geliştirici, Fable 5.2 ve önceki Opus modellerinin kendilerine verilen gereksinimleri yanlış aktardığı bir derleyici görevini anlatıyor.

Type: Limit | Date: 2026-11-10

---

<a id="case-461"></a>
### Case 461: [Uzun Fable Görevini Opus ile İzlemek](https://x.com/marouane53/status/2119950129767858262) (üreten [@marouane53](https://x.com/marouane53))

**Uzun görevlerin ilerlemesini ayrı bir oturumdan izleyin.**

Yazar, bazı Fable görevlerinin seyrek durum güncellemeleriyle iki saati aştığını bildiriyor. İlerlemeyi ve kararları açıklamak için ayrı bir konuşmada Opus 5.5 kullandı.

Type: Integration | Date: 2026-11-10

---

<a id="case-462"></a>
### Case 462: [Koda taze bir gözle bakmak](https://x.com/doodlestein/status/2119958895158292786) (üreten [@doodlestein](https://x.com/doodlestein))

**Yeni ve değiştirilen dosyalar için ayrı bir inceleme yürütün.**

Yazar, uygulama sonrasında hataları bulup düzeltmek için kullandığı iki takip istemini aynen paylaşıyor.

Orijinal istem

```
Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with "fresh eyes" looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover.
```

Orijinal istem

```
Once again, check over everything again with fresh eyes looking for any blunders, mistakes, errors, oversights, omissions, problems, misconceptions, bugs, etc. Be SUPER thorough and meticulous!
```

Type: Tutorial | Date: 2026-11-10

---

<a id="case-463"></a>
### Case 463: [Özellik tasarımı incelemesinde bağlam sapması](https://news.ycombinator.com/item?id=50434214) (üreten [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin))

**Sonraki önerileri incelerken mevcut tasarımı kontrol listesi olarak kullanın.**

Yazar özellik tasarımı incelemesinde modelleri karşılaştırıp Opus 5.5’i tercih etti. Fable 5.2 sonraki bir tanılama turunda tasarımda zaten bulunan bir şeyi önerdi.

Type: Limit | Date: 2026-11-10

---

<a id="case-464"></a>
### Case 464: [DX Ball tarzı Breakout karşılaştırması](https://news.ycombinator.com/item?id=50434424) (üreten [@goyozi](https://news.ycombinator.com/user?id=goyozi))

**Aynı tarifle mekanikleri ve oyun hissini karşılaştırın.**

Yazar ayrı Fable 5.2 ve Opus 5.5 çalışmalarını bağlantıyla paylaşıyor. Fable özgün mekaniklerden bazılarını değiştirdi. Yazar Opus sürümünün oyun hissini tercih etti.

[İlgili kaynaklar 1](https://claude.ai/artifact/UszKFvuonWAT5psjMttAEg) · [İlgili kaynaklar 2](https://claude.ai/artifact/UuT7P936dU1XoPByYZ7xyD)

Type: Evaluation | Date: 2026-11-10

---

<a id="case-465"></a>
### Case 465: [3B uygulamayı iyileştirme denemesi](https://news.ycombinator.com/item?id=50434433) (üreten [@user43928](https://news.ycombinator.com/user?id=user43928))

**Aynı görevde görünür değişikliği harcanan bütçeyle karşılaştırın.**

Yazar Fable 5.2’den oyun dışı bir 3B uygulamayı iyileştirmesini istedi. Opus 5.5’e göre az fark gördüğünü ve o akşam Fable kullanım hakkının %25’ini tükettiğini bildiriyor.

Type: Evaluation | Date: 2026-11-10

---

<a id="case-466"></a>
### Case 466: [Üç modelle fare ve kedi oyunu](https://news.ycombinator.com/item?id=50434508) (üreten [@simonw](https://news.ycombinator.com/user?id=simonw))

**Oyun istemini sabit tutup her oynanabilir sürümü inceleyin.**

Simon Willison, Fable 5.2 Extra, Opus 5.5 Extra ve GPT-6 Extra High ile mobil uyumlu Three.js oyunu denemelerini paylaşıyor. Fable denemesi yaklaşık 40 dakika sürdü.

[İlgili kaynaklar 1](https://claude.ai/artifact/Agsqbng2MnkTPAU67it87o) · [İlgili kaynaklar 2](https://claude.ai/artifact/RRyEndXLSPQbcig3BgzgCZ) · [İlgili kaynaklar 3](https://squeak-and-seek-mouse-1027.simonw.chatgpt.site/)

Orijinal istem

```
Build a mobile-friendly three.js game where a mouse has to hide from a cat
```

Type: Evaluation | Date: 2026-11-10

---

<a id="case-467"></a>
### Case 467: [High düzeyinde AIBenchy maliyet ve puan karşılaştırması](https://aibenchy.com/compare/anthropic-claude-fable-5-2-high/anthropic-claude-opus-5-5-high/) (üreten [AIBenchy](https://aibenchy.com/))

**Aynı çaba etiketi altında puanı, toplam maliyeti ve yanıt süresini karşılaştırın.**

AIBenchy, Fable 5.2 High ve Opus 5.5 High için sırasıyla 8,7 ve 9,4 puan, 5,083 ve 2,133 ABD doları maliyet, 14,73 ve 27,55 saniye ortalama yanıt süresi yayımladı.

[İlgili kaynaklar 1](https://news.ycombinator.com/item?id=50435602)

Type: Benchmark | Date: 2026-11-10

---

<a id="case-468"></a>
### Case 468: [Fable 5.2 Ajan Ortamını Ayarlamak](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) (üreten [@Anthropic](https://www.anthropic.com/))

**Akıl yürütme düzeylerini yeniden test edin ve ilerleme bildirimlerini tanımlayın.**

Anthropic rehberi, akıl yürütme düzeyi, bitirme ölçütleri, onaylar, durum bildirimleri ve alt ajan sınırları için örnek talimatlar veriyor.

[İlgili kaynaklar 1](https://x.com/t_wada/status/2119925892000739340)

Type: Tutorial | Date: 2026-11-10

---

<a id="case-469"></a>
### Case 469: [Animasyonlu Karakterleri Önizleme Uygulaması](https://x.com/seiiiiiiiiiiru/status/2121390458572333253) (üreten [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru))

**Tekrarlanan 3B varlık kontrollerini bir arayüze dönüştürmesini Fable’dan isteyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/ce514e99465c257220ee9bf7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/776670eda35fbabbf1c63663.jpg" alt="Case 469 · 1" width="760"><br>▶ Videoyu oynat</a>

İçerik üreticisi, Fable 5.2’yi danışman olarak sürece kattığını ve modelin verimsiz bir iş akışını uygulamaya dönüştürdüğünü söylüyor. Kayıtta bir 3B karakter için hazır hareketler, arka plan ayarları ve GLB ile şeffaf arka planlı PNG dışa aktarma seçenekleri görülüyor.

Type: Demo | Date: 2026-11-13

---

<a id="case-470"></a>
### Case 470: [Araç Kullanmadan Üretilen QR Kodunu Test Etme](https://x.com/AdamHoltererer/status/2121376853474578625) (üreten [@AdamHoltererer](https://x.com/AdamHoltererer))

**Denemeyi başarılı saymadan önce üretilen QR kodunu okutun.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d3833f006038158569c9816d.png" alt="Case 470 · 1" width="760">

Adam Holter, QR kodu gösterimini Fable 5.2, Astra ve Sol’a atfediyor ve araç kullanılmadığını belirtiyor. Ekli görseli yerelde taradığımızda QR kodunun MADE WITHOUT TOOLS metnini içerdiği doğrulandı.

Type: Evaluation | Date: 2026-11-13

---

<a id="case-471"></a>
### Case 471: [Tripo ile Unity’de Zombi Oyunu](https://x.com/fe_yukichi/status/2121375714192814554) (üreten [@fe_yukichi](https://x.com/fe_yukichi))

**Oynanabilir karakterler hazırlamak için ortak bir varlık üretim süreci kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/055f505803b769bb8b24a54e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0fa0715e64f91ab69725599e.jpg" alt="Case 471 · 1" width="760"><br>▶ Videoyu oynat</a>

İçerik üreticisi, Tripo ile iş birliği yaptığını belirtiyor ve Fable 5.2 ile geliştirdiği Unity oyunu için Tripo Agentic Canvas kullanarak sekiz oynanabilir karakter ve on altı zombi çeşidi ürettiğini söylüyor. Videoda karakter seçimi ve oynanış görülüyor. Üretici, masaüstü tarayıcıda çalışan bir sürüm de paylaşmış.

[İlgili kaynaklar 1](https://tsukiyo-zombie.pages.dev/)

Type: Demo | Date: 2026-11-13

---

<a id="case-472"></a>
### Case 472: [MS Paint’te Karlı Bir Sokak Çizme](https://www.reddit.com/r/ClaudeAI/comments/1xvghd1/fable_52_painting_in_ms_paint/) (üreten [u/wollymonjac](https://www.reddit.com/user/wollymonjac/))

**Uzun bir görevde farenin doğrudan kontrolünü ekran kaydı üzerinden değerlendirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/10ad84001f4c682c5343846c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e7af823e10ef2135adec2154.jpg" alt="Case 472 · 1" width="760"><br>▶ Videoyu oynat</a>

Reddit’teki paylaşımın sahibi, Fable 5.2’nin fareyi kullanarak MS Paint’te yaklaşık iki buçuk saatte karlı bir sokak çizdiğini söylüyor. Bağlantısı verilen X paylaşımı aynı sahnenin çizim kaydını içeriyor.

[İlgili kaynaklar 1](https://x.com/i/status/2121373793599869213)

Type: Demo | Date: 2026-11-13

---

<a id="case-473"></a>
### Case 473: [Wojak-Bench’te Eksik Kalan Priz Bağlantısı](https://x.com/lukaspet/status/2121371593943466167) (üreten [@lukaspet](https://x.com/lukaspet))

**Üretilen 3B montajdaki her bağlantıyı referansla karşılaştırın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e509db79b2e79fcc2d6beda1.jpg" alt="Case 473 · 1" width="760">

Yazar, bu Wojak-Bench görevinde Fable 5.2’nin kabloyu prize bağlayamadığını bildiriyor. Kaynak görselde 3B sonucun fotoğrafı ve referans çizimi yan yana gösteriliyor.

Type: Limit | Date: 2026-11-13

---

<a id="case-474"></a>
### Case 474: [Ritim Oyunu İçin Piyano Düzenlemesi](https://x.com/DJ_HYSNS/status/2121367353237942287) (üreten [@DJ_HYSNS](https://x.com/DJ_HYSNS))

**Modelden beste isterken parçanın çalınabilirliğini ve ses prodüksiyonundaki kontrolleri inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d016f48687e0c8e6cf810812.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/9faa77e2e9ba2ec99be995a7.jpg" alt="Case 474 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar ritim oyunu için müzik istedi. Modele VST sesleri seçtirmekte ve miks yaptırmakta zorlandığını belirterek solo piyanoya geçti. Videoda ortaya çıkan piyano rulosu görülüyor. Yazara göre parça, bir insanın çalabileceği sınırlar içinde kalma şartını aştı.

Type: Evaluation | Date: 2026-11-13

---

<a id="case-475"></a>
### Case 475: [Picnic’in Token Kurtarma Akışını Yeniden Tasarlama](https://x.com/joaoavf/status/2121366491321057717) (üreten [@joaoavf](https://x.com/joaoavf))

**Desteklenmeyen token’ları kurtarma sürecinin farklı adımlarını arayüz taslaklarında karşılaştırın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/551612796f4150a43b190ee3.jpg" alt="Case 475 · 1" width="760">

Yazar, Picnic’in desteklemediği token’ları kurtarma sürecini Fable 5.2’ye verdiği bir ya da iki istemle yeniden tasarladığını söylüyor. Ekli görsel, önerilen akıştan birkaç ekran gösteriyor.

Type: Demo | Date: 2026-11-13

---

<a id="case-476"></a>
### Case 476: [Üretilen Kliplerle Anime Açılışı Kurgulama](https://x.com/aimikoda/status/2121362621274177726) (üreten [@aimikoda](https://x.com/aimikoda))

**Fable’a klipleri, müziği ve kesmeleri ritme oturtmak için açık talimatları verin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/e3ab28061669d84818042ee0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/cb65344e413d2bd340406d59.jpg" alt="Case 476 · 1" width="760"><br>▶ Videoyu oynat</a>

İçerik üreticisi, MiniMax H3 görüntülerini ve Suno v6 müziğini Fable 5.2 Medium ile kurguladı. Paylaşılan videoda hareketli piksel karakterler ve geçişler yer alıyor. Fable’a verilen özgün kurgu istemi de örneğe ekli.

Orijinal istem

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
### Case 477: [Üç Araçla Karakter Animasyonu](https://x.com/ingi_erlingsson/status/2121361947446677797) (üreten [@ingi_erlingsson](https://x.com/ingi_erlingsson))

**Kaynak GIF’i Fable ve ComfyUI adımlarından sonraki animasyonla karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/69a3410b7b2dcdb14ee6c5d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/391924750cd0641254cb114f.jpg" alt="Case 477 · 1" width="760"><br>▶ Videoyu oynat</a>

Yazar, girdi olarak GPT Image 2.6 ile hazırlanan bir GIF kullandığını, ardından Fable 5.2 ve ComfyUI’ye geçtiğini belirtiyor. Ekli klipte değişen karakter yüzü, dönen bir kamera açısıyla gösteriliyor.

Type: Demo | Date: 2026-11-13

---

<a id="case-478"></a>
### Case 478: [Blender Betikleriyle Şehir Fragmanı Oluşturma](https://x.com/hanghuang_/status/2121361932456427644) (üreten [@hanghuang_](https://x.com/hanghuang_))

**Şehir fragmanının yapımını sahne, karakter, araç ve işleme görevlerine ayırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/0e5170c057eecd328b178fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/d10c5d322edba010282a60d0.jpg" alt="Case 478 · 1" width="760"><br>▶ Videoyu oynat</a>

İçerik üreticisi, Fable 5.2’nin oyun tarzında bir fragman planladığını ve şehir, karakter ve otomobil için Blender kodu yazdığını söylüyor. Üreticiye göre 4K sonuç yedi kiralık GPU ile işlendi. Paylaşılan videoda tamamlanan sahneler görülüyor.

Type: Demo | Date: 2026-11-13

---

<a id="case-479"></a>
### Case 479: [JavaScript ile Gece Manzaraları Çizme](https://x.com/kloss_xyz/status/2121356668311384487) (üreten [@kloss_xyz](https://x.com/kloss_xyz))

**Kodla oluşturulan çizimleri değerlendirirken bitmiş birkaç örneği bir arada inceleyin.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/6e9d554b17822715f07d3be8.jpg" alt="Case 479 · 1" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/f57db49bb8213cc6ca4bcafe.jpg" alt="Case 479 · 2" width="450"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/2933b30de09501dbbb7e1505.jpg" alt="Case 479 · 3" width="450"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/490e5952694322b7963be8e2.jpg" alt="Case 479 · 4" width="450"></td></tr></table>

Yazar, paylaştığı dört çizimi Fable 5.2’nin JavaScript ile oluşturduğunu belirtiyor. Eklerde karşılaştırılabilecek stilize gece manzaraları görülüyor.

Type: Demo | Date: 2026-11-13

---

<a id="case-480"></a>
### Case 480: [CAD Modellerini Teknik Resimlere Dönüştürme](https://x.com/MecAgent/status/2121352868490100787) (üreten [@MecAgent](https://x.com/MecAgent))

**Görünüşleri, ölçüleri ve açıklamaları kaynak CAD modeliyle karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/5ce59334e405a279e1008bf0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/780dc65cb1b04f7a75e27ace.jpg" alt="Case 480 · 1" width="760"><br>▶ Videoyu oynat</a>

MecAgent, kendi gösteriminde birden fazla görünüş ve açıklama içeren teknik resim paftalarını yayımlıyor ve dönüşümü Fable 5.2’ye atfediyor. Klipte ortaya çıkan çizimler görülüyor. Ölçülerin doğruluğu için CAD dosyalarıyla karşılaştırma gerekir.

Type: Demo | Date: 2026-11-13

---

<a id="case-481"></a>
### Case 481: [Plotly’nin Veri Analizi Sınavında 43 Görev](https://plotly.com/blog/gemini-4-hydrogen-plotly-data-analytics-bench/) (üreten [Plotly](https://plotly.com/))

**Doğruluğu ve çalıştırma maliyetini aynı analiz testi ortamında karşılaştırın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/50882a17db12bede9165a92d.webp" alt="Case 481 · 1" width="760">

Plotly’nin raporuna göre Fable 5.2, gizli örüntüleri bulmaya yönelik beş soru dâhil 43 sorunun tamamını geçen dört modelden biri. Yayımlayan ekip, model başına tek çalıştırmanın yalnızca tek örnek sağladığını belirtiyor. Grafik, testteki doğruluğu ve maliyeti gösteriyor.

[İlgili kaynaklar 1](https://news.ycombinator.com/item?id=50485733)

Type: Benchmark | Date: 2026-11-12

---

<a id="case-482"></a>
### Case 482: [SGI Indy’yi Web Sitesi Olarak Yeniden Canlandırma](https://news.ycombinator.com/item?id=50476597) (üreten [@gdubs](https://news.ycombinator.com/user?id=gdubs))

**Fiziksel bir iş istasyonunun web sitesine nasıl taşınabileceğini etkileşimli bir örnekle inceleyin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable-5-2/2026-11-14/74b80686867b920881164246.jpg" alt="Case 482 · 1" width="760">

Gregory Wieber, sitesini 1990’lardan kalma bir Silicon Graphics Indy olarak yeniden tasarlamada Fable 5.2’nin rolünü belirtiyor. Yayımlanan demoda oturum açma ekranı, 3B dosya sistemi ve Soft Break oyunu bulunan üç boyutlu bir iş istasyonu var.

[İlgili kaynaklar 1](https://gregorywieber.com/indy/)

Type: Demo | Date: 2026-11-13

---

<a id="case-483"></a>
### Case 483: [İş Kayıtları ve Git Çalışma Ağaçlarıyla Ajan Koordinasyonu](https://news.ycombinator.com/item?id=50493545) (üreten [@nickalaso](https://news.ycombinator.com/user?id=nickalaso))

**Görevleri GitHub iş kayıtlarıyla dağıtın, değişiklikleri çalışma ağaçları ve çekme istekleriyle ayırın.**

Yazar, Fable 5.2’yi ana koordinatör, Opus’u alt koordinatör olarak kullandığını ve birden fazla sağlayıcının ajanlarını özel bir MCP sunucusu üzerinden başlattığını söylüyor. İşleri GitHub Issues ile takip ediyor ve değişikliklerin çakışmasını önlemek için Git çalışma ağaçları ile çekme isteklerinden yararlanıyor.

Type: Integration | Date: 2026-11-14

---

<a id="case-484"></a>
### Case 484: [Atıfları Arka Planda Çalışan Ajanlarla Kontrol Etme](https://x.com/tukiyomiiori/status/2121368478364192930) (üreten [@tukiyomiiori](https://x.com/tukiyomiiori))

**Atıf kontrollerini devredin ve ana oturumun ne zaman devam ettiğini gözlemleyin.**

Yazar, Fable 5.2’den atıf yapılan makaleleri alt ajanlar ve arka plan betikleriyle kontrol etmesini istediğini bildiriyor. Claude Code oturumunun bu işler sürerken beklemeye geçtiğini, ajanlar veya betikler durduğunda ise yeniden devreye girdiğini gözlemlemiş.

Type: Integration | Date: 2026-11-13

---

<a id="case-485"></a>
### Case 485: [Gidiş Dönüş Navlun Fiyatı Modelinde Hata Ayıklama](https://x.com/allTheYud/status/2121360145921998877) (üreten [@allTheYud](https://x.com/allTheYud))

**Modelin dönüş ayağına marjinal maliyetleri doğru yükleyip yüklemediğini kontrol edin.**

Yazar, iki yönlü taşıma simülasyonunda Fable 5.2’nin her iki yönün yakıt giderini tek ayağa, yalnızca marjinal giderleri ise diğer ayağa yüklediğini söylüyor. Simülasyonda geminin zaten geri dönmesi gerekiyordu. Yazar, bu tür hatalar için tekrar tekrar hata ayıklamak zorunda kalmış.

Type: Limit | Date: 2026-11-13

---

<a id="case-486"></a>
### Case 486: [Edge0 Çıkarım Kurulumunu Mac’e Uyarlama](https://news.ycombinator.com/item?id=50482710) (üreten [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen))

**Platforma uygun değişiklikleri isteyin ve çıkarımı hedef makinede test edin.**

Edge0-145B tartışmasındaki bir kullanıcı, Fable 5.2’den Mac uyumlu bir sürüm istediğini ve birkaç düzeltme yaptığını söylüyor. Kendi M5 Max ve NVFP4 kurulumunda saniyede yaklaşık 50 token elde ettiğini bildiriyor.

[İlgili kaynaklar 1](https://news.ycombinator.com/item?id=50475713)

Type: Integration | Date: 2026-11-13

---

<a id="case-487"></a>
### Case 487: [Yüksek Bileşen Yoğunluklu Devre Kartı Yerleşimlerini İnceleme](https://news.ycombinator.com/item?id=50478759) (üreten [@0_____0](https://news.ycombinator.com/user?id=0_____0))

**Yerleşimi ve bileşen seçimini kartın performans gereksinimleriyle karşılaştırın.**

Bir Hacker News kullanıcısı, birkaç kartın bileşen yerleşimi ve hat çizimi için Fable 5.2’yi denedi. Yoğun bir yerleşimin ilk bakışta iyi göründüğünü, kendi gereksinimlerini karşılamak için bileşenleri önemli ölçüde yeniden yerleştirmesi ve şemanın büyük kısmını elle çizmesi gerektiğini söylüyor.

Type: Limit | Date: 2026-11-13

---

<a id="case-488"></a>
### Case 488: [Ücretli Gazete Arşivinde Bir Atfın İzini Sürme](https://news.ycombinator.com/item?id=50478191) (üreten [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff))

**Özgün metne bakana kadar atıf önerisini geçici kabul edin.**

Bir Hacker News kullanıcısı, bir dilbilim e-posta listesinde atıf yapılan 1985 tarihli Dallas Morning News makalesine ulaştı. Kullanıcı, Fable 5.2’nin makalenin tamamını açamadığını ve olası bir muhabir ile bağlam önerdiğini belirtiyor. Atfı doğrulamak için özgün metin hâlâ gerekli.

[İlgili kaynaklar 1](https://listserv.linguistlist.org/pipermail/ads-l/2003-September/033575.html)

Type: Limit | Date: 2026-11-13

---

<a id="case-489"></a>
### Case 489: [Fable ile Planlama ve Opus Değişikliklerini İnceleme](https://news.ycombinator.com/item?id=50477200) (üreten [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology))

**Yazılı bir planı onaylayın, uygulamayı iş kollarına ayırın ve değişiklikleri CI ile ön üretim ortamında doğrulayın.**

Yazar, büyük kod tabanlarında uyguladığını söylediği bir iş akışını paylaşıyor. Planı Fable 5.2 hazırlıyor, değişiklikleri Opus 5.5 alt ajanları uygulayıp inceliyor, CI test kapsamını denetliyor ve ön üretim kontrol listesi elle doğrulamaya rehberlik ediyor.

Type: Tutorial | Date: 2026-11-13

---

<a id="acknowledge"></a>
## Katkıda bulunanlar

[Ruslan Ianberdin](https://news.ycombinator.com/user?id=ianberdin), [Lex](https://notesbylex.com/), [@Anthropic](https://www.anthropic.com/), [@Angaisb_](https://x.com/Angaisb_), [@higgsfield_ai](https://x.com/higgsfield_ai), [@ericmaskfr](https://x.com/ericmaskfr), [@kloss_xyz](https://x.com/kloss_xyz), [@WesRoth](https://x.com/WesRoth), [@Mr_Salio](https://x.com/Mr_Salio), [@argofowl](https://x.com/argofowl), [@QQTeng](https://x.com/QQTeng), [@banteg](https://x.com/banteg), [@Avenoxai](https://x.com/Avenoxai), [@ScaleAILabs](https://x.com/ScaleAILabs), [@0xRhinoX](https://x.com/0xRhinoX), [@anstapnever](https://x.com/anstapnever), [@ivanainai](https://x.com/ivanainai), [@Luckyballa](https://x.com/Luckyballa), [@0xKense1](https://x.com/0xKense1), [@alexalbert__](https://x.com/alexalbert__), [@The_Alex](https://x.com/The_Alex), [@sparklabhq](https://x.com/sparklabhq), [@atomicagent_io](https://x.com/atomicagent_io), [@eidzoku](https://x.com/eidzoku), [@emollick](https://x.com/emollick), [@seiiiiiiiiiiru](https://x.com/seiiiiiiiiiiru), [@Rasmic](https://x.com/Rasmic), [@daradoescode](https://x.com/daradoescode), [@imjustnewatai](https://x.com/imjustnewatai), [@aollivier82](https://x.com/aollivier82), [@ivanfioravanti](https://x.com/ivanfioravanti), [@aidigest_](https://x.com/aidigest_), [@AdamHoltererer](https://x.com/AdamHoltererer), [@kunchenguid](https://x.com/kunchenguid), [@felixrieseberg](https://x.com/felixrieseberg), [@theo](https://x.com/theo), [@loktar00](https://x.com/loktar00), [@hiyouwhatsapp](https://x.com/hiyouwhatsapp), [@Tim_Hua_](https://x.com/Tim_Hua_), [@noclipepe](https://x.com/noclipepe), [@karolina_dubiel](https://x.com/karolina_dubiel), [@aziz4ai](https://x.com/aziz4ai), [@bobyau](https://x.com/bobyau), [@deedydas](https://x.com/deedydas), [@ashebytes](https://x.com/ashebytes), [@saimagnate](https://x.com/saimagnate), [@Izkimar](https://x.com/Izkimar), [@dom_scholz](https://x.com/dom_scholz), [@AndrewPrifer](https://x.com/AndrewPrifer), [@lambdacalcc](https://x.com/lambdacalcc), [@_sholtodouglas](https://x.com/_sholtodouglas), [@ziwenxu_](https://x.com/ziwenxu_), [@AI_masaou](https://x.com/AI_masaou), [@AmirMushich](https://x.com/AmirMushich), [@kevin_t_ngo](https://x.com/kevin_t_ngo), [@KHvostikk](https://x.com/KHvostikk), [@GrilliotTodd](https://x.com/GrilliotTodd), [@arena](https://x.com/arena), [@muku_sns](https://x.com/muku_sns), [@Khazix0918](https://x.com/Khazix0918), [@konstantinsaifo](https://x.com/konstantinsaifo), [@dwarkesh_sp](https://x.com/dwarkesh_sp), [@Masimo_Blue](https://x.com/Masimo_Blue), [@mgrczyk](https://x.com/mgrczyk), [@Da7_Tech](https://x.com/Da7_Tech), [@kickingkeys](https://x.com/kickingkeys), [@rileybrown](https://x.com/rileybrown), [@techartist_](https://x.com/techartist_), [@seveibar](https://x.com/seveibar), [@chetanankola](https://x.com/chetanankola), [@vib3coded](https://x.com/vib3coded), [@suna_gaku](https://x.com/suna_gaku), [@MaxXWilliamson](https://x.com/MaxXWilliamson), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Leviwoyun](https://x.com/Leviwoyun), [@MrTacticalX](https://x.com/MrTacticalX), [@gosrum](https://x.com/gosrum), [@SemiAnalysis_](https://x.com/SemiAnalysis_), [@morganlinton](https://x.com/morganlinton), [@LexnLin](https://x.com/LexnLin), [@xikhar](https://x.com/xikhar), [@elliotarledge](https://x.com/elliotarledge), [@rpnickson](https://x.com/rpnickson), [@bijanbowen](https://x.com/bijanbowen), [@pleometric](https://x.com/pleometric), [@DeryaTR_](https://x.com/DeryaTR_), [@cmonkey](https://x.com/cmonkey), [@chetaslua](https://x.com/chetaslua), [@davelee](https://x.com/davelee), [@oaranda](https://x.com/oaranda), [@petergostev](https://x.com/petergostev), [Vercel](https://vercel.com/), [@TuxSH](https://news.ycombinator.com/user?id=TuxSH), [@jjcm](https://news.ycombinator.com/user?id=jjcm), [Discovered Materials](https://discoveredmaterials.com/), [Artificial Analysis](https://artificialanalysis.ai/), [@popkkksidhd](https://news.ycombinator.com/user?id=popkkksidhd), [@ariwilson](https://news.ycombinator.com/user?id=ariwilson), [@nzach](https://news.ycombinator.com/user?id=nzach), [Senko Rašić](https://senko.net/), [@GMoromisato](https://news.ycombinator.com/user?id=GMoromisato), [@github](https://x.com/github), [@MiaAI_lab](https://x.com/MiaAI_lab), [@sameQCU](https://x.com/sameQCU), [@marouane53](https://x.com/marouane53), [@doodlestein](https://x.com/doodlestein), [@nikitamalyavin](https://news.ycombinator.com/user?id=nikitamalyavin), [@goyozi](https://news.ycombinator.com/user?id=goyozi), [@user43928](https://news.ycombinator.com/user?id=user43928), [@simonw](https://news.ycombinator.com/user?id=simonw), [AIBenchy](https://aibenchy.com/), [@fe_yukichi](https://x.com/fe_yukichi), [u/wollymonjac](https://www.reddit.com/user/wollymonjac/), [@lukaspet](https://x.com/lukaspet), [@DJ_HYSNS](https://x.com/DJ_HYSNS), [@joaoavf](https://x.com/joaoavf), [@aimikoda](https://x.com/aimikoda), [@ingi_erlingsson](https://x.com/ingi_erlingsson), [@hanghuang_](https://x.com/hanghuang_), [@MecAgent](https://x.com/MecAgent), [Plotly](https://plotly.com/), [@gdubs](https://news.ycombinator.com/user?id=gdubs), [@nickalaso](https://news.ycombinator.com/user?id=nickalaso), [@tukiyomiiori](https://x.com/tukiyomiiori), [@allTheYud](https://x.com/allTheYud), [@kjjohnsen](https://news.ycombinator.com/user?id=kjjohnsen), [@0_____0](https://news.ycombinator.com/user?id=0_____0), [@mmahemoff](https://news.ycombinator.com/user?id=mmahemoff), [@DeepOntology](https://news.ycombinator.com/user?id=DeepOntology)
