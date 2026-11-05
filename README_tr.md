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

## 🍌 Giriş

Claude Fable 5 yüksek sinyalli kullanım örnekleri deposuna hoş geldiniz.

**Claude Fable 5 için gerçek dünya kullanım örneklerini, öğreticileri, entegrasyonları ve değerlendirmeleri; herkese açık demolardan ve üretici topluluklarından derleyerek topluyoruz.**

Bu Türkçe README, somut iş akışları, promptlar, demolar, entegrasyonlar, benchmark kanıtları veya pratik sınırlar içeren yüksek sinyalli örneklere odaklanır.

Çoğu örnek X/Twitter gönderilerinden ve herkese açık demolardan derlenmiştir. Her örnek başlığı özgün kaynağa, her yazar kullanıcı adı da üretici profiline bağlantı verir.

Evolink'te deneyin: [Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

## 📊 Genel Bakış

- **88 özgün Fable 5 örneği ve 218 topluluk örneği; toplam 306 örnek.**
- Kodlama ajanlarını, uzun süreli otomasyonu, oyunları, görsel tasarımı, 3D simülasyonları, bilgi çalışmalarını, öğreticileri, API entegrasyonlarını, benchmarkları, fiyatlandırmayı ve lansman sınırlamalarını kapsar.
- Her örnek özgün kaynak, üretici atfı, kısa çıkarım, kanıt türü ve yayın tarihi içerir.
- Bu depoyu pratik iş akışlarını bulmak, güçlü ve zayıf yönleri karşılaştırmak, yeniden üretilebilir promptları keşfetmek ve entegrasyon örneklerini izlemek için kullanın.

> [!NOTE]
> Bu koleksiyon abartıdan çok somut kanıtları öne çıkarır: yeniden üretilebilir promptlar, yayınlanmış demolar, benchmark yöntemleri, entegrasyon notları, maliyet verileri ve açıkça belirtilmiş uyarılar.

<a id="-quick-api-access"></a>
## ⚡ Hızlı API erişimi

Claude Fable 5'i Evolink uyumlu Messages API üzerinden kullanın. [Evolink](https://evolink.ai/login?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5) üzerinden API token alın, ardından `<token>` değerini kendi tokenınızla değiştirin.

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

## 📑 Menü

| Bölüm | Örnekler |
|---|---|
| [💻 Kodlama ve Kod Üretimi](#coding-and-code-generation) | Case 1-6 |
| [🤖 Ajanlar ve Uzun Süreli Otomasyon](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 Oyunlar ve Etkileşimli Demolar](#games-and-interactive-demos) | Case 9-12 |
| [🎨 Görsel, Tasarım, Video ve 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 Belgeler, Bilgi Çalışması ve Araştırma](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 Öğreticiler, Kurslar ve Prompt Kaynakları](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 Platform, API ve Araç Entegrasyonu](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 Değerlendirmeler, Karşılaştırmalar ve Sınırlar](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | Katkı verenler ve düzeltme politikası |

### [💻 Kodlama ve Kod Üretimi](#coding-and-code-generation)

| Case | Ne gösteriyor | Tür |
|---|---|---|
| [Cursor Çok Aşamalı İş Akışı](#case-1) | Fable 5'i çok modelli bir Cursor iş akışında plan inceleme ve eleştiri adımı olarak kullanın; ardından uygulama ve revizyonu daha ucuz veya uzmanlaşmış modellere devredin. | Değerlendirme |
| [Bir Ekran Görüntüsünden GitHub'ı Yeniden Oluşturma](#case-2) | Bir ürün ekran görüntüsünü ajanik kodlama aracına yapıştırın ve Fable 5'ten arayüzü çalışan işlevsellikle yeniden oluşturmasını isteyin. | Demo |
| [Tek Promptla Kara Delik Simülasyonu](#case-3) | Fable 5'e ayrıntılı bir yaratıcı kodlama promptu verin ve kendi kendine yeten bir Three.js fizik görselleştirmesi üretmesini isteyin. | Öğretici |
| [Tek Denemede macOS Tarzı Web OS](#case-4) | Fable 5'ten eksiksiz tek dosyalık bir web OS isteyin; UI kabuğunu, uygulamaları, etkileşimleri, sesi ve gömülü oyun davranışını tek geçişte inşa etmesine izin verin. | Öğretici |
| [Spawn 5.0'ı 1.687 Promptla İnşa Etme](#case-5) | Fable 5'i birçok prompt boyunca uzun oturumlu bir mühendislik ortağı olarak kullanın; insan rolü mimariden çıktı kalitesini yargılamaya kayar. | Öğretici |
| [Bulgularla Büyük Pull Request İncelemesi](#case-6) | Fable 5'i büyük bir pull request'e yönlendirin ve doğruluk, yanlış pozitifler, gerçek buglar ve cilalama sorunları açısından incelemesini isteyin. | Demo |

### [🤖 Ajanlar ve Uzun Süreli Otomasyon](#agents-and-long-running-automation)

| Case | Ne gösteriyor | Tür |
|---|---|---|
| [Uzun Ufuklu Relay İş Akışı İncelemesi](#case-7) | Fable 5'i iddialı uzun ufuklu işler için kullanın: site yeniden inşaları, programatik içerik hatları, ses eşleştirme, güvenlik incelemesi ve son kalite kontrolleri. | Değerlendirme |
| [Altyapı Kesintisini Teşhis Etme ve Düzeltme PR'ı Açma](#case-8) | Fable 5'e loglar, veritabanı hataları ve image digest'leri gibi altyapı ipuçlarına erişim verin; ardından kesintiyi teşhis edip düzeltmeyi hazırlamasını isteyin. | Değerlendirme |

### [🎮 Oyunlar ve Etkileşimli Demolar](#games-and-interactive-demos)

| Case | Ne gösteriyor | Tür |
|---|---|---|
| [Parmak Takipli Dino Runner](#case-9) | Fable 5'ten giriş mekaniği olarak parmak takibi kullanan bir tarayıcı oyunu yapmasını isteyin. | Demo |
| [İki Cümleyle Yarış Oyunu İnşası](#case-10) | Fable 5'e çok kısa bir oyun promptu verin; haritaları, modları, müziği, UI'ı ve oyun varlıklarını tek çalıştırmada üretmesine izin verin. | Öğretici |
| [Rust ile Kurulabilir Terminal Minecraft](#case-11) | Fable 5'i bir terminal kodlama harness'i içinde çalıştırın ve kurulabilir bir Rust terminal oyunu yapmasını isteyin. | Demo |
| [Zaman ve Maliyetle Minecraft Klonu](#case-12) | Tek promptla Fable 5'ten oynanabilir Minecraft tarzı bir klon isteyin; ardından zamanı, maliyeti, kod hacmini ve özellik kapsamını değerlendirin. | Öğretici |

### [🎨 Görsel, Tasarım, Video ve 3D](#visual-design-video-and-3d)

| Case | Ne gösteriyor | Tür |
|---|---|---|
| [Tam Yeniden Üretilebilir E-ticaret E-postası Promptu](#case-13) | Fable 5'e marka e-posta maketi için tam bir yaratıcı brief verin: kesin bölümler, ürün gereksinimleri, görsel yön ve kısıtlar dahil. | Öğretici |
| [Swiss Lever Saatçi Benchmarkı](#case-14) | Fable 5'i mekanik simülasyon benchmarkında kullanın; fiziksel doğruluğu uygulamasını, doğrulamasını ve yinelemesini isteyin. | Değerlendirme |
| [Three.js Friends Apartmanı Sahnesi](#case-15) | Fable 5'e bir kat planını ve sahne referansını gezilebilir bir Three.js ortamına dönüştürmesini promptlayın. | Değerlendirme |
| [Prompt ve URL ile Güneş Sistemi Simülasyonu](#case-16) | Fable 5'i fizik ilkelerinden bir astronomi simülasyonu inşa etmek için kullanın; simülasyon ve herkese açık çıktı hazır olana kadar yineleyin. | Öğretici |

### [📚 Belgeler, Bilgi Çalışması ve Araştırma](#documents-knowledge-work-and-research)

| Case | Ne gösteriyor | Tür |
|---|---|---|
| [Stripe ve Bilimsel İş Akışı Kanıtı](#case-17) | Bunu kopyala-yapıştır promptu olarak değil, kurumsal geçiş ve bilimsel iş akışı iddiaları için kanıt olarak kullanın. | Değerlendirme |
| [Politika Notu ve Değişiklik İzleme İş Akışları](#case-18) | Fable 5'i uzun form nitel belge çalışması için kullanın: değişiklik izleme, yorum triage'ı ve transkript odaklı düzenlemeler. | Öğretici |
| [Derin Araştırma Promptu ve Çıktısı](#case-19) | Fable 5'e araştırma tarzı bir soru sorun ve yapılandırılmış, tarihsel temelli uzun bir yanıt üretip üretemediğini değerlendirin. | Demo |

### [🧭 Öğreticiler, Kurslar ve Prompt Kaynakları](#tutorials-courses-and-prompt-resources)

| Case | Ne gösteriyor | Tür |
|---|---|---|
| [Fable 5'in Claude Code İş Akışlarını Nasıl Değiştirdiği](#case-20) | Fable 5'i her adımı mikro yönetmek yerine yön, bağlam, hedefler ve doğrulama kriterleri belirleyerek kullanın. | Demo |
| [Bir Milyar Token İncelemesi ve Yönlendirme Stratejisi](#case-21) | Fable 5'i frontier planlama ve inceleme için kullanın, sonra yüksek hacimli uygulamayı daha ucuz modellere yönlendirin. | Öğretici |
| [Savunmacı Cihaz Sertleştirme Promptu](#case-22) | Fable 5'in cihazları envantere aldığı, kesin kontroller verdiği ve doğrulama beklediği adım adım savunmacı sertleştirme promptunu çalıştırın. | Öğretici |
| [Tam Site Tasarım Denetimi Goal Promptu](#case-23) | Fable 5'in siteyi başlatması, sayfaların ekran görüntüsünü alması, UX denetimi yapması, rapor yazması ve güvenli küçük sorunları düzeltmesi için `/goal` kullanın. | Öğretici |
| [Uzun Form Yaratıcı İş Akışı Bölüşümü](#case-24) | Fable 5'i kararlı formatlar ve örnekler tasarlamak için kullanın; sonra bu yapıyı alana özgü çıktı için başka bir üretim sistemine devredin. | Öğretici |
| [Fable 5 Kullanımı İçin Başlangıç Rehberi](#case-25) | Fable 5'i küçük adım adım talimatlar yerine hedef odaklı promptlar, doğrulama döngüleri ve effort ayarlarıyla kullanın. | Değerlendirme |
| [Kopyala-Yapıştır Depo Denetimi Promptu](#case-26) | Depo denetimi promptunu Fable 5'e yapıştırın ve dosya destekli keşif, bulgular, strateji ve milestone görev planı isteyin. | Öğretici |
| [Sınırlı Pencere Kullanım Stratejisi](#case-27) | Erişim penceresi avantajlıyken Fable 5 kullanımını denetim, mimari ve planlamaya harcayın; yürütme için daha ucuz modeller kullanın. | Öğretici |
| [Claude Code'da Goals ve Workflows Kullanımı](#case-28) | Fable 5'i uygulamadan önce düşünce ortağı olarak kullanın, ardından planı yürütmek ve doğrulamak için `/goal` ve workflows'u birleştirin. | Öğretici |

### [🔌 Platform, API ve Araç Entegrasyonu](#platform-api-and-tool-integration)

| Case | Ne gösteriyor | Tür |
|---|---|---|
| [Hermes Ajan Entegrasyonu Kurulumu](#case-29) | Hermes'i `anthropic/claude-fable-5` kullanacak şekilde, karmaşık `/goal` çalışmaları ve cache'li uzun ufuklu görevler için yapılandırın. | Öğretici |
| [Yetenekler, Fiyatlandırma ve Abonelik Notları](#case-30) | Fable 5'in ne zaman erişilebilir olduğunu, maliyetini ve hangi korumalı alanların başka modele fallback edebileceğini anlamak için bu örneği kullanın. | Öğretici |
| [Lansman, Erişim, Fiyatlandırma ve Güvenlik Özeti](#case-31) | Erişim yolunu, API model adını, context window'u, caching stratejisini ve abonelik zamanlamasını seçmek için bu lansman özetini kullanın. | Öğretici |
| [Danışman Tabanlı Maliyet Azaltma Stratejisi](#case-32) | Marjinal zeka maliyete değdiğinde, Fable 5'i daha ucuz model iş akışında danışman veya inceleyici olarak kullanın. | Entegrasyon |
| [Fiyatlandırma, Erişim ve Güvenlik Korkulukları](#case-33) | İş yüklerini planlamadan önce Fable 5 erişimini, API fiyatlandırmasını ve güvenlik fallback davranışını anlamak için bu örneği kullanın. | Entegrasyon |
| [Tek Satırlık Swarms Entegrasyonu](#case-34) | Swarms model adını `anthropic/claude-fable-5` olarak ayarlayın ve Fable 5'i Swarms framework'ü veya API üzerinden çalıştırın. | Entegrasyon |

### [📏 Değerlendirmeler, Karşılaştırmalar ve Sınırlar](#evaluations-comparisons-and-limits)

| Case | Ne gösteriyor | Tür |
|---|---|---|
| [Fable 5 ve GPT-5.5 Maliyet ve Kalite Karşılaştırması](#case-35) | Çıktı kalitesini, çalışma süresini ve araç maliyetini değerlendirmek için Fable 5 ve GPT-5.5'i aynı kodlama görevinde karşılaştırın. | Değerlendirme |
| [AA-Omniscience Benchmark Sonucu](#case-36) | Fable 5'i bilgi doğruluğu ve halüsinasyon davranışı açısından değerlendirmek için bu benchmark örneğini kullanın. | Değerlendirme |
| [Artificial Analysis Intelligence Index Sonucu](#case-37) | Fable 5'in genel zeka sıralamasını diğer frontier modellerle benchmark etmek için bu örneği kullanın. | Değerlendirme |
| [GDPval-AA Ajanik Bilgi Çalışması Benchmarkı](#case-38) | Fable 5'i ajanik gerçek dünya bilgi çalışmasında değerlendirmek için bu örneği kullanın. | Değerlendirme |
| [Bir Haftalık İlk İzlenimler ve Fiyatlandırma Mekaniği](#case-39) | Fable 5'in en güçlü olduğu yerleri, özellikle oyun tasarımı ve sistem planlamasını belirlemek için bu ilk izlenim örneğini kullanın. | Entegrasyon |
| [Maliyet ve Hız Karşılaştırması](#case-40) | Kalite kazancının daha yüksek maliyeti ve daha yavaş uzun ufuklu çalışmaları haklı çıkarıp çıkarmadığını belirlemek için bu karşılaştırmayı kullanın. | Değerlendirme |
| [Claude Code Uygulamalı Notları](#case-41) | Araç kullanımı, kişilik ve kalan pürüzler dahil Fable 5'i Claude Code içinde değerlendirmek için bu örneği kullanın. | Demo |
| [Yaratıcı Yazarlık Benchmark Sonucu](#case-42) | Fable 5'in kısa kurgu yazım kalitesini ve refusal davranışını yargılamak için bu benchmark örneğini kullanın. | Değerlendirme |
| [Çoklu Benchmark Lansman Özeti](#case-43) | Kodlama ajanları ve karmaşık görevler için en ilgili headline skorları anlamak üzere bu lansman benchmark özetini kullanın. | Değerlendirme |
| [GPT-5.5 ile Benchmark ve Fiyat Karşılaştırması](#case-44) | Fable 5'i GPT-5.5'e karşı fiyat ve benchmark kategorileri açısından değerlendirmek için bu karşılaştırmayı kullanın. | Değerlendirme |
| [Pratik Sınırlamalarla Saha Notları](#case-45) | Fable 5'in nerede anlamlı biçimde daha iyi hissettirdiğini ve nerede hâlâ pratik sınırları olduğunu anlamak için bu saha raporunu kullanın. | Öğretici |
| [Fizik Simülasyonu Karşılaştırması](#case-46) | Çıktı kalitesini, maliyeti ve hızı karşılaştırmak için aynı fizik simülasyonu promptlarını Fable 5 ve Opus 4.8'e karşı çalıştırın. | Demo |
| [Hata Ayıklama Deneyimi ve Tasarım Yargısı](#case-47) | Fable 5'i hata ayıklama için kullanırken sadece tahmin etmesini değil, ölçmesini, log eklemesini, doğrulamasını ve yama yapmasını isteyin. | Demo |
| [Çok Boyutlu Artılar ve Eksiler](#case-48) | Fable 5'i günlük sürücü yapmadan önce pratik güçlü ve zayıf yönleri anlamak için bu örneği kullanın. | Demo |
| [Hukuki S-1 Taslak Testi](#case-49) | S-1 taslak promptunu hukuki ajan kabiliyet testi olarak kullanın ve yapı, biçimlendirme ve uzunluğu karşılaştırın. | Öğretici |
| [Sağlık Benchmark Ayrıntıları](#case-50) | Fable 5'i sağlıkla ilgili görevlerde değerlendirmek ve eksik zor tıbbi eval'leri belirlemek için bu benchmark notunu kullanın. | Değerlendirme |
| [ParseBench Belge Ayrıştırma Değerlendirmesi](#case-51) | Fable 5'in belge ayrıştırma için uzman OCR sistemlerine kıyasla maliyet etkin olup olmadığını belirlemek için bu örneği kullanın. | Değerlendirme |
| [SWE-Bench Pro ve FrontierCode Karşılaştırması](#case-52) | Fable 5'i migration'lar, karmaşık uygulamalar, otonom oturumlar, testler ve görsel doğrulama için değerlendirmek üzere bu benchmark örneğini kullanın. | Değerlendirme |
| [Uzun Problem Çözmeye Nitel İnceleme](#case-53) | Fable 5'in neden daha uzun ve daha zor görevlere uygun olduğunu, üretim incelemesinin hâlâ gerektiğini anlamak için bu nitel incelemeyi kullanın. | Değerlendirme |
| [ParseBench Sadakat ve Biçimlendirme Sonuçları](#case-54) | Belge sadakati ve biçimlendirme performansını yargılamak için bu ParseBench sonucunu kullanın. | Değerlendirme |
| [Benchmarklar, Fiyatlandırma, Erişim ve Koruma Önlemleri](#case-55) | Bu örneği benchmarklar, fiyatlandırma, erişim, koruma önlemleri ve stratejik sonuçlar için geniş bir checklist olarak kullanın. | Değerlendirme |
| [Resmi Benchmark Skor Listesi](#case-56) | Fable 5'in kodlama, bilgisayar kullanımı ve güvenlik görevlerindeki resmi skorlarını anlamak için bu benchmark listesini kullanın. | Değerlendirme |
| [APEX-SWE Benchmark Metodolojisi](#case-57) | Fable 5'i APEX-SWE üzerinde, özellikle observability ve integration işi açısından değerlendirmek için bu örneği kullanın. | Değerlendirme |
| [ProofBench Formel Matematik Sonucu](#case-58) | Fable 5'i uzman theorem-proving sistemlerine karşı formel matematikte değerlendirmek için bu örneği kullanın. | Öğretici |
| [VirtueBench Ön Analizi](#case-59) | Fable 5'in erdem kategorileri genelindeki ahlaki akıl yürütme davranışını incelemek için bu örneği kullanın. | Değerlendirme |
| [API Boş Yanıt Güvenlik Overfit Testi](#case-60) | Lansman zamanı güvenlik overfit riskini ve API testindeki boş yanıt davranışını anlamak için bu örneği kullanın. | Değerlendirme |
| [Fable İstem ve Doğrulama Kılavuzu](#case-61) | Uzun istem hilelerinden hedef, bağlam, kısıt, araç ve doğrulama döngülerine geçmek için bu kılavuzu kullanın. | Öğretici |
| [İstanbul Platform Oyunu Referans Yapımı](#case-62) | Fable 5'in oynanabilir platform oyunu oluşturmasını sınamak için bir sprite sayfası ve tek dönüştürme talimatı kullanın. | Demo |
| [İşletme İçin 3D Şehir Panosu](#case-63) | Bir iş akışını canlı bir 3D şehir panosu konseptine dönüştürmek için Fable 5'i kullanın. | Demo |
| [Three.js Delik Oyununu Tek Seferde Oluşturma](#case-64) | Three.js ile bir 3D tarayıcı oyunu prototipini tek seferde oluşturmak için Fable 5'i kullanın. | Demo |
| [DeepSWE Puan Karşılaştırması](#case-65) | Fable 5 xHigh ile GPT-5.5 xHigh'ın yazılım mühendisliği kıyaslamasındaki performansını karşılaştırmak için bu DeepSWE notunu kullanın. | Değerlendirme |
| [Depo Analizi Maliyet Karşılaştırması](#case-66) | Token fiyatını insanın yeniden çalışma maliyetiyle birlikte değerlendirmek için bu depo analizi karşılaştırmasını kullanın. | Değerlendirme |
| [Super Mario Oyununun Token Maliyeti](#case-67) | Fable 5'in çıktı kalitesini ve token tüketimini değerlendirmek için bu tek geçişlik oyun yapımını kullanın. | Demo |
| [Claude Code Model Geçiş Ayarı](#case-68) | Fable 5 mesajı işaretlendiğinde model değiştiren Claude Code ayarını anlamak için bu örneği inceleyin. | Entegrasyon |
| [Namma Metro Simülatörünün Yapımı](#case-69) | Bu demoyu, Fable 5 ile doğal dil üzerinden toplu taşıma simülatörü geliştirmeye kısa bir örnek olarak kullanın. | Demo |
| [Tek İstemle Dusk Drive Oyunu](#case-70) | Fable 5'i insan düzenlemesi olmadan düşük poligonlu oyun prototiplemede değerlendirmek için bu tek istemlik sürüş oyunu örneğini kullanın. | Demo |
| [APEX-Agents Pass@1 Sıralaması](#case-71) | Fable 5 Max'i çok adımlı otonom görevlerde karşılaştırmak için bu APEX-Agents sonucunu kullanın. | Değerlendirme |
| [Claude Model Seçim Rehberi](#case-72) | Fable 5'i en zor Claude Code işleri için ayırmak üzere bu model seçim rehberini kullanın. | Öğretici |
| [HermesWorld Otomatik Ajan Döngüsü](#case-73) | Günler boyunca geliştiren, test eden, oynayan ve temel işleyiş kontrolleri yapan müdahalesiz Fable 5 döngüsünü bu örnekle inceleyin. | Entegrasyon |
| [McKinsey Tarzı Rapor İstemi Testi](#case-74) | Danışmanlık raporunun yapısını, grafiklerini, anlatımını ve risk analizini değerlendirmek için bu belge oluşturma istemini kullanın. | Öğretici |
| [Görünür Güvenlik Önlemlerinin Devreye Alınması](#case-75) | Fable 5 güvenlik önlemlerinin görünürlüğünü, API ret nedenlerini ve Opus'a geçiş davranışını anlamak için bu resmî notu kullanın. | Entegrasyon |
| [Claude Code Model Eşleştirme Düzeltmesi](#case-76) | Fable 5 model adı ve bağlam eşleştirme sorunlarından kaçınmak için bu Claude Code değişiklik notunu kullanın. | Entegrasyon |
| [Claude Code İçinde Üç Web Uygulaması](#case-77) | Birden fazla üretilmiş web uygulaması üzerinden Claude Code içindeki Fable 5'i incelemek için bu başlangıç seviyesi kodlama demosunu kullanın. | Demo |
| [Açık Kaynak Uygulama Oluşturucu Rilable](#case-78) | Fable 5'in iOS, web uygulamaları, korumalı alanlar ve API token maliyetiyle ilişkisini bu açık kaynak oluşturucu üzerinden inceleyin. | Entegrasyon |
| [DeepSWE Kodlama Ajanı Endeksine Giriş](#case-79) | Güncellenmiş Artificial Analysis endeksini kullanarak, geri dönüştürülmüş herkese açık GitHub düzeltmelerinden kaçınan daha zor ajanik kodlama görevlerinde Fable 5'i karşılaştırın. | Değerlendirme |
| [DataEmpire Web Analitiği Oyunu](#case-80) | Claude Fable 5'ten ziyaretçileri ve kilometre taşlarını oyun varlıklarına eşlemesini isteyerek ham site analitiğini yeniden oynanabilir bir oyuna dönüştürün. | Entegrasyon |
| [FrontierSWE 20 Saatlik Görev Sinyali](#case-81) | FrontierSWE'yi, Fable 5'in yalnızca kısa bug-fix döngülerinde değil, çok uzun mühendislik görevlerinde de üretken kalabildiğine dair kanıt olarak kullanın. | Değerlendirme |
| [KernelBench-Hard CUDA Rekorları](#case-82) | Yalnızca mevcut kütüphanelerin sarmalayıcıları değil, düşük seviyeli optimizasyon gerektiğinde Fable 5'i ileri seviye CUDA kernel üretimi için kullanın. | Değerlendirme |
| [Figma Capture Açılış Sayfası Klonu](#case-83) | Canlı bir rakip sayfasını Figma katmanlarına alın ve Claude Code'un Fable 5 ile yapıyı, metinleri ve marka sistemini ekran görüntülerinden tahmin etmek yerine yeniden kurmasına izin verin. | Entegrasyon |
| [İki Saatte GTA 2 Klonu](#case-84) | Tüm yığını elle kodlamadan, ayrı varlık araçlarıyla birlikte Fable 5 kod üretimini kullanarak oynanabilir bir 3D oyunu hızla oluşturun. | Öğretici |
| [CloudWatch Log Triyaj Ajanı](#case-85) | Fable 5 destekli bir ajanın çok büyük servis log bağlamlarını işlemesine, mimariyi çıkarmasına ve ardından belirli arızalara daralmasına izin verin. | Entegrasyon |
| [Sandbox'larda Dünya Kupası Tahmincisi](#case-86) | Birden fazla frontier modeli izole sandbox'ların arkasına koyun ve herkese açık bir tahmin uygulaması için canlı haberleri, sakatlıkları ve sarı kart bağlamını araştırmalarına izin verin. | Entegrasyon |
| [WolfBench Ret Maliyeti Vakası](#case-87) | Fable 5 üzerinde uzun otonom çalışmaları fiyatlarken ret davranışını gerçek bir benchmark değişkeni olarak ele alın. | Değerlendirme |
| [API Erişim Kesinti İzleyicisi](#case-88) | İş akışınız fazla uyarı vermeden rate-limit uygulanabilecek veya geri çekilebilecek bir frontier modele sürekli erişime bağlıysa kullanılabilirliği bir script ile izleyin. | Entegrasyon |



### [🆕 Fable 5.5 Topluluk Demoları](#fable-5-5-community-demos)

| Örnek | Tür |
|---|---|
| [Kodla Üretilmiş Sesli Tilki Animasyonu](#case-89) | Demo |
| [Açık Uçlu Yaratıcı Brief'ten Animasyon](#case-90) | Demo |
| [Animasyonlu İnşaat Şirketi Web Sitesi](#case-91) | Demo |
| [Three.js Otomobil Sunumu](#case-92) | Demo |
| [Minecraft Tarzı Tarayıcı Oyunu Demosu](#case-93) | Demo |
| [Three.js Bisiklet Süren Pelikan Animasyonu](#case-94) | Demo |
| [Tam İstemiyle Bisiklet Süren Pelikan SVG'si](#case-95) | Demo |
| [Dörtnala Koşan Zebra Animasyonu Örneği](#case-96) | Demo |
| [Emirleri Kullanıcının Verdiği TradingView Göstergesi](#case-97) | Demo |
| [Bir noktadan kısa animasyon öyküsüne](#case-98) | Demo |
| [Değişen sanat tarzları arasında Superman](#case-99) | Demo |
| [Müzikli insanlık ilerleyişi filmi](#case-100) | Demo |
| [Opus ile tanıtım filmi karşılaştırması](#case-101) | Evaluation |
| [Şarkı sözlerini olayla görsel olarak bağlamak](#case-102) | Demo |
| [Yüzen sahnede voksel karakter](#case-103) | Demo |
| [3D Rube Goldberg makinesi](#case-104) | Demo |
| [Ses ve hareketli 3D kumanda arayüzü](#case-105) | Demo |
| [JavaScript ile çizgi roman karakterleri](#case-106) | Demo |
| [Updraft: dünyalar, bölüm sonu düşmanları ve sıralama](#case-107) | Demo |
| [San Francisco haritasında sürüş](#case-108) | Demo |
| [Seedance aksiyon sahnesi için istem yazımı](#case-109) | Demo |
| [Masaüstü çalışma arkadaşı için tanıtım](#case-110) | Demo |
| [Tarz değiştiren animasyona kısa istem](#case-111) | Demo |
| [Üç cisim problemini görselleştirmek](#case-112) | Demo |
| [Farklı sanat tarzlarından animasyon galerisi](#case-113) | Demo |
| [Robot arkadaşlar ve prosedürel tüyler](#case-114) | Demo |
| [Matematik temalı hareketli kurgu](#case-115) | Demo |
| [Your Woman şarkı sözü videosu](#case-116) | Demo |
| [Müzik videosunu JavaScript ile yeniden çizmek](#case-117) | Demo |
| [Çin futbolu animasyonu](#case-118) | Demo |
| [El konsolu yeniden topoloji gösterimi](#case-119) | Demo |
| [Minecraft ile Pokémon birleşimi](#case-120) | Demo |
| [Bir dil modelinin yapılışını açıklamak](#case-121) | Demo |
| [Altman öne çıkanlar kurgusu](#case-122) | Demo |
| [Otuz Altı Stratejinin ilki](#case-123) | Demo |
| [Oyun modelleme, iskelet ve animasyon](#case-124) | Demo |
| [Çocuk ölümleri üzerine sözsüz film](#case-125) | Demo |
| [Glikolizden etanole SVG animasyonu](#case-126) | Demo |
| [On altı eşzamanlı Starship fırlatışı](#case-127) | Demo |
| [Animasyonlu pelikan bisiklet testi](#case-128) | Demo |
| [Gelecek yüz elli yılın öyküsü](#case-129) | Demo |
| [Bağımsız Humanity Walks deneyi](#case-130) | Demo |
| [The Grader kod filmi](#case-131) | Demo |
| [Reawakening korku kısa filmi](#case-132) | Demo |
| [Yirmi beş saniyelik kendini geliştirme videosu](#case-133) | Demo |
| [Kale sahnesi ve kullanım maliyeti](#case-134) | Evaluation |
| [Kırk saniyelik marka tanıtım reklamı](#case-135) | Demo |
| [Rocketball yeniden yapımı](#case-136) | Demo |
| [Voksel pagoda karşılaştırması](#case-137) | Evaluation |
| [Hayali Switch 3 sunumu](#case-138) | Demo |
| [Açılış sayfalarının önce ve sonrası](#case-139) | Evaluation |
| [Hayali bir yapay zekânın iç dünyası](#case-140) | Demo |
| [Go şarkı sözü hareket tasarımı](#case-141) | Demo |
| [İkinci on beş saniyelik hareket portföyü](#case-142) | Demo |
| [Yönlendirmeli ajan uygulama incelemesi](#case-143) | Tutorial |
| [Claude maskot dansı](#case-144) | Demo |
| [Etkileşimli Yedi Harika adaları](#case-145) | Demo |
| [Propellerheads müzik videosu](#case-146) | Demo |
| [Steamboat Willie animasyon karşılaştırması](#case-147) | Evaluation |
| [Sanxingdui temalı film](#case-148) | Demo |
| [Bugatti Chiron önce ve sonra](#case-149) | Evaluation |
| [GRAIN kavram filmi](#case-150) | Demo |
| [Human in Transit sanat galerisi](#case-151) | Demo |
| [İpek Yolu görsel kısa filmi](#case-152) | Demo |
| [Dört dönüşüm sunumu](#case-153) | Demo |
| [Geçmiş sohbet üslubunu karşılaştırmak](#case-154) | Evaluation |
| [Kakapo sevimlilik testi](#case-155) | Evaluation |
| [On çizgi roman döneminde Spider-Man](#case-156) | Demo |
| [İlluminati temalı kurmaca korku videosu](#case-157) | Demo |
| [Kodlanmış nükleer bilim tarihi filmi](#case-158) | Demo |
| [Evrensel Yüksek Gelir açıklayıcısı](#case-159) | Demo |
| [Altman–Amodei anlaşmazlığı açıklayıcısı](#case-160) | Demo |
| [Claude maskot müzik videosu](#case-161) | Demo |
| [Kuarklardan evrene kesintisiz yakınlaşma](#case-162) | Demo |
| [2076 dünyasını hayal etmek](#case-163) | Demo |
| [Aşağı Manhattan bina kronolojisi](#case-164) | Demo |
| [Kehanet kemiği yazısı animasyonu](#case-165) | Demo |
| [Karakterlerle başka bir sanat tarihi animasyonu](#case-166) | Demo |
| [Kodlanmış Seikilos görsel-işitsel eseri](#case-167) | Demo |
| [Jet animasyonu karşılaştırması](#case-168) | Evaluation |
| [Modelin kendini tanıtma filmi](#case-169) | Demo |
| [Kıyamet sonrası kart oyunu prototipi](#case-170) | Demo |
| [The Late Byte işyeri animasyonu](#case-171) | Demo |
| [Queens of the Stone Age söz animasyonu](#case-172) | Demo |
| [Paylaşılan Three.js anlatı sahnesi](#case-173) | Demo |
| [Tarihsel sahnelerde ay yürüyüşü](#case-174) | Demo |
| [Ayrıntılı istemle hareketli grafikler](#case-175) | Demo |
| [Kiralama işletmesi sitesi arayüzü](#case-176) | Demo |
| [AGI temalı yaratıcı film](#case-177) | Demo |
| [Kedi yan öyküsüyle sanat tarihi](#case-178) | Demo |
| [Savaş prototipi ve voksel sahne](#case-179) | Demo |
| [İnternet mizahı kronolojisi](#case-180) | Demo |
| [Tek satırdan parçacık hareketi](#case-181) | Demo |
| [Kung-Fu Boy animasyonu](#case-182) | Demo |
| [Hürmüz Boğazı tartışma animasyonu](#case-183) | Demo |
| [Tek boynuzlu at SVG tarz deneyi](#case-184) | Demo |
| [Cadılar Bayramı animasyonu](#case-185) | Demo |
| [Blender CLI barbarı ve kapağı](#case-186) | Demo |
| [Claude'un hayatından bir gün](#case-187) | Demo |
| [3D insanlık tarihi](#case-188) | Demo |
| [Hızlı hareket tasarımcısı gösterimi](#case-189) | Evaluation |
| [Serbest karmaşık 3D yaratım](#case-190) | Demo |
| [Çöp adam dövüş animasyonu](#case-191) | Demo |
| [Tek istemlik UI hareket dizisi](#case-192) | Demo |
| [SCP-8517 kurmaca animasyonu](#case-193) | Demo |
| [Suluboya sonbahar animasyonu](#case-194) | Demo |
| [Prosedürel oyuncak bebek sahnesi](#case-195) | Demo |
| [Tarayıcıda çizilen pelikan sürüşü](#case-196) | Demo |
| [Evren kendine bakıyor](#case-197) | Demo |
| [Bağımsız jet animasyonu testi](#case-198) | Demo |
| [İlk serbest hareket gösterimi](#case-199) | Demo |
| [Kodla çizilen uygarlık](#case-200) | Demo |
| [Çipten sunucuya yakınlaşma karşılaştırması](#case-201) | Evaluation |
| [Ay yolculuğu animasyon projesi](#case-202) | Demo |
| [Japon voksel sahnesi karşılaştırması](#case-203) | Evaluation |
| [Steaming the Frontier kısa filmi](#case-204) | Demo |
| [Farklı sanat tarzlarında Superman](#case-205) | Demo |
| [Cupcake tarzı bölüm sonu savaşı](#case-206) | Demo |
| [Değişen güneşle yelkenli sahnesi](#case-207) | Demo |
| [Paracortex ve Pi değişiklik videosu](#case-208) | Demo |
| [Curio 2.0 site tanıtımı](#case-209) | Demo |
| [Hayali Hugging Face 3D öyküsü](#case-210) | Demo |
| [JS Paint'te Claude for Chrome](#case-211) | Demo |
| [Statik pelikan bisiklet SVG'si](#case-212) | Demo |
| [Minecraft becerisiyle BlockBench MCP](#case-213) | Demo |
| [Tek HTML dosyasında Dig Dug](#case-214) | Demo |
| [Mekanik ahtapot SVG'si](#case-215) | Demo |
| [Sanat tarzlarında Humanity Walks](#case-216) | Demo |
| [Açık uçlu kara delik sahnesi](#case-217) | Demo |
| [Kutup ışıklı denizanası animasyonu karşılaştırması](#case-218) | Evaluation |
| [Nintendo Switch takılma ve açılış SVG'si](#case-219) | Demo |
| [The Loom etkileşimli 3D sahnesi](#case-220) | Demo |
| [Aynı İstemle Hazırlanan Hareketli Tasarım Videoları](#case-221) | Evaluation |
| [Daha temiz ama daha sığ manzara](#case-222) | Evaluation |
| [Japon sahnelerinde karışık sonuçlar](#case-223) | Evaluation |
| [Kumanda SVG karşılaştırmaları](#case-224) | Evaluation |
| [Endüstriyel cihaz sahnesi](#case-225) | Demo |
| [Dev kabuklu solungaçlı böcek yeniden yapımı](#case-226) | Demo |
| [İki istemde GameCube kumandası](#case-227) | Demo |
| [X gönderisi için düzenlenen ekran görüntüsü](#case-228) | Demo |
| [Voksel sakurada önce ve sonra](#case-229) | Evaluation |
| [SHADERKIN kumaş arayüzü prototipi](#case-230) | Demo |
| [Paylaşılan altın saat arayüzü animasyonu](#case-231) | Demo |
| [Before There Was Anything anlatısı](#case-232) | Demo |
| [Paylaşılan mavi parçacık girdabı](#case-233) | Demo |
| [İki revizyondan sonra çok panelli arayüz](#case-234) | Demo |
| [Çizilmiş sahnede üst üste hayvanlar](#case-235) | Demo |
| [Dört açık dünya RPG denemesi](#case-236) | Evaluation |
| [İki ön yüz animasyon klibi](#case-237) | Evaluation |
| [Kodla üretilmiş yosun robot filmi](#case-238) | Demo |
| [Konteyner limanı simülasyonunu yeniden ele almak](#case-239) | Demo |
| [Havaalanı apronunu yeniden ele almak](#case-240) | Demo |
| [Soyut 3D dünyalarda pelikan sürüşü](#case-241) | Demo |
| [Tarihsel yelkenli sahnesi](#case-242) | Demo |
| [Carbon ile sürüş ve yürüyüş karşılaştırması](#case-243) | Evaluation |
| [Meşrubat şişesi sunumu](#case-244) | Demo |
| [Astra ile pelikan hareketi karşılaştırması](#case-245) | Evaluation |
| [Kod animasyonları için hareket tasarımı tarifi](#case-246) | Tutorial |
| [Fotoğraf referansından voksel portre](#case-247) | Demo |
| [Opus ile uçan pelikan sahneleri](#case-248) | Evaluation |
| [Morning Ride pelikan internet sahnesi](#case-249) | Demo |
| [Aynı istemle farklı tarzlarda sahneler](#case-250) | Evaluation |
| [Pelikan, bisiklet ve at kompozisyonu](#case-251) | Demo |
| [Referans gönderiden izometrik sahne](#case-252) | Demo |
| [Pelikan bisikletinin mekanik yakın planları](#case-253) | Demo |
| [Pelikanın üstünde giden bisiklet](#case-254) | Demo |
| [Carbon ile pelikan SVG tarzları](#case-255) | Evaluation |
| [Çizgi mavi kuş bisiklet sahnesi](#case-256) | Demo |
| [Orman yolunda pelikan sürüşü](#case-257) | Demo |
| [Carbon ile çöp adam çatışması](#case-258) | Evaluation |
| [Erken testlerden pelikan SVG referansı](#case-259) | Demo |
| [Modeller arası SVG testinde pelikan referansı](#case-260) | Evaluation |
| [Carbon ile bisiklet SVG ayrıntıları](#case-261) | Evaluation |
| [3D kanyon yerleşimi](#case-262) | Demo |
| [Opus ile kumanda ayrıntıları](#case-263) | Evaluation |
| [Haftalık site SEO denetimi](#case-264) | Integration |
| [Opus hareket tasarımında Fable varlıkları](#case-265) | Integration |
| [Mandala ve geometrik biçim uygulaması](#case-266) | Demo |
| [Three.js ile bisikletli](#case-267) | Demo |
| [FrontierCS 2 değerlendirmesinin anlık görünümü](#case-268) | Evaluation |
| [Üç modelin zebra animasyonlarının karşılaştırması](#case-269) | Evaluation |
| [Uzun Japonca metni eleştirmek](#case-270) | Evaluation |
| [Örneklerle yönlendirilen teknik PowerPoint](#case-271) | Evaluation |
| [Müzikal bütünlüğü karşılaştırmak](#case-272) | Evaluation |
| [Erken tamamlanma ve daha zayıf tasarımlar](#case-273) | Limit |
| [Rahatsız edici kalamar sanatı](#case-274) | Limit |
| [Teknik çizim tarzı hareket tasarımı](#case-275) | Demo |
| [Voksel sakurada kuşlar ve balıklar](#case-276) | Demo |
| [Karakter üretiminde başarısızlık bildirimi](#case-277) | Limit |
| [Süre ve maliyet notlu pelikan SVG'si](#case-278) | Evaluation |
| [Telefonla uzaktan Claude Code sürüleri](#case-279) | Integration |
| [Bir Alp Gölünün Üzerinde Samanyolu](#case-280) | Demo |
| [İşlemsel Su ve Sesle Balina Sıçrayışı](#case-281) | Demo |
| [Dört Modelde Zebra Hareketi Karşılaştırması](#case-282) | Evaluation |
| [Lightreel’de Doğal Dille İçerik Üreticisi Bulma](#case-283) | Demo |
| [Bulut Denizinin Üzerinde Uçan Bir Gemi](#case-284) | Demo |
| [Hareketli Kesit Görünümlü Mekanik Kalp](#case-285) | Demo |
| [Keşfedilebilir Yüzen Voksel Pagoda Bahçesi](#case-286) | Demo |
| [Sekiz Ekibin Hazırladığı Okyanus Macerası](#case-287) | Demo |
| [Etkileşimli Hiper Otomobil Sunumu](#case-288) | Demo |
| [Bir Yaşam Ağacının Doğuşu](#case-289) | Demo |
| [Çalışan İç Mekanizmalı Yürüyen Şato](#case-290) | Demo |
| [Tost Karakteri ve Mekanik Böcek](#case-291) | Demo |
| [Fırtınada Bir Deniz Feneri Bekçisi](#case-292) | Demo |
| [Bir Sahil Kasabasında Deniz Canlısı](#case-293) | Demo |
| [Üç Modelle Halı Üzerinde Yarış](#case-294) | Evaluation |
| [Robota Dönüşen Bir Kamyon](#case-295) | Demo |
| [Fable ve Hunyuan Animasyon Kareleri](#case-296) | Evaluation |
| [Işığı Paylaşmak Üzerine Bir Animasyon](#case-297) | Demo |
| [Dağlar Arasında Bir Voksel Köyü](#case-298) | Demo |
| [Dört Modelle Pelikan ve Fil Kompozisyonu](#case-299) | Evaluation |
| [Darbe Kareleriyle Anime Kılıç Dövüşü](#case-300) | Demo |
| [Dört Modelde Koşan Geyik Karşılaştırması](#case-301) | Evaluation |
| [Sular Altındaki Şehri Geçen Bir Robot](#case-302) | Demo |
| [Blender Kılıcı ve Sunum Filmi](#case-303) | Demo |
| [Lantern Isle Piksel Köyü Animasyonu](#case-304) | Demo |
| [Pause Oyun Videosu Düzenleme Demosu](#case-305) | Demo |
| [Sahil Boyunca Bisiklete Binen Pelikan](#case-306) | Demo |

<a id="coding-and-code-generation"></a>
## 💻 Kodlama ve Kod Üretimi

<a id="case-1"></a>
### Case 1: [Cursor Çok Aşamalı İş Akışı](https://x.com/AlicanKiraz0/status/2064487347605918180) (tarafından [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Fable 5'i çok modelli bir Cursor iş akışında plan inceleme ve eleştiri adımı olarak kullanın; ardından uygulama ve revizyonu daha ucuz veya uzmanlaşmış modellere devredin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8b1352e20cff54688c97f17c.png" alt="Cursor Çok Aşamalı İş Akışı" width="760">

Fable 5 ile GPT 5.5 arasındaki nihai puanlamaya bakarsak fark çok küçük. Naçizane kullanım önerim şu: Cursor gibi hibrit modelleri destekleyen IDE platformlarında aşamalı bir iş akışı kullanın.

Aşama 1: Kod incelemesi ve proje denetiminin ilk aşaması için, bağlamı ısıtırken GPT 5.5 High, Minimax M3, Kimi K2.6 veya Composer 2.5 modellerinden birini kullanın.

Aşama 2: Proje planını hazırlamak için GPT 5.5 Very High veya Opus 4.8 kullanın.

Aşama 3: Proje planını analiz etmek için Fable 5 kullanın; planın hatalı kısımlarını belirlemesine izin verin. Revizyonlar için GPT 5.5 Very High kullanın.

Aşama 4: Planı uygulamak için Minimax M3, Deepseek v4 Max, Composer 2.5 veya Sonnet 4.6 kullanın.

Aşama 5: Son inceleme ve uygulamanın plana uyup uymadığını kontrol etmek için GPT 5.5 High kullanın.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [Bir Ekran Görüntüsünden GitHub'ı Yeniden Oluşturma](https://x.com/coldopn/status/2064435234465087638) (tarafından [@coldopn](https://x.com/coldopn))

**Bir ürün ekran görüntüsünü ajanik kodlama aracına yapıştırın ve Fable 5'ten arayüzü çalışan işlevsellikle yeniden oluşturmasını isteyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/14123609b06071f3b9527bee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f4df4f42ce047201d9a096a6.jpg" alt="Bir Ekran Görüntüsünden GitHub&#x27;ı Yeniden Oluşturma" width="760"><br>▶ Videoyu izle</a>

🚨 Anthropic Fable 5 az önce GITHUB'ı bir EKRAN GÖRÜNTÜSÜNDEN kopyaladı!!

Yaptığım tek şey GitHub UI ekran görüntüsünü Kilo Code'a yapıştırmak ve gerçek işlevsellikle GitHub'ı yeniden oluşturmasını söylemekti.

10 dakika kodladı ve $4.07 harcadı.

Sonuç çalışan bir GitHub replikasıydı: https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [Tek Promptla Kara Delik Simülasyonu](https://x.com/deveshcodes_/status/2064437742189379745) (tarafından [@deveshcodes_](https://x.com/deveshcodes_))

**Fable 5'e ayrıntılı bir yaratıcı kodlama promptu verin ve kendi kendine yeten bir Three.js fizik görselleştirmesi üretmesini isteyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9bd45e74c64ceb3639600805.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ce5f3ea8ba270f89d60523cc.jpg" alt="Tek Promptla Kara Delik Simülasyonu" width="760"><br>▶ Videoyu izle</a>

@claudeai, Claude Fable 5 ile Three.js içinde gerçek zamanlı bir kara delik merceklenme simülasyonunu tek seferde yaptı.

Yerçekimsel merceklenme, doppler etkisiyle parlaklaşan yığılma diski, foton küresi, kromatik sapma ve prosedürel yıldız alanı içeriyordu.

Sonuç: 60fps, tek HTML dosyası, tek prompt.

Yeni taban çizgisi çılgın 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [Tek Denemede macOS Tarzı Web OS](https://x.com/intheworldofai/status/2064421915347812672) (tarafından [@intheworldofai](https://x.com/intheworldofai))

**Fable 5'ten eksiksiz tek dosyalık bir web OS isteyin; UI kabuğunu, uygulamaları, etkileşimleri, sesi ve gömülü oyun davranışını tek geçişte inşa etmesine izin verin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a66f34402d04f708819fa575.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/81946293919c84d4cafff841.jpg" alt="Tek Denemede macOS Tarzı Web OS" width="760"><br>▶ Videoyu izle</a>

🚨 Claude Fable 5 tek seferde tam macOS tarzı bir web OS inşa etti ve çoğu modelden daha ileri gitti.

Tek HTML dosyası, gömülü CSS + JS.

Tek prompttan şunları yaptı:

- macOS menü çubuğu + dock
- Sürüklenebilir ve yeniden boyutlandırılabilir uygulama pencereleri
- İşlevsel dosya gezgini
- Çalışan terminal + tarayıcı maketi
- SVG masaüstü ikonları + bildirimler
- Ayarlar uygulaması, temalar ve açılış ekranı
- Gerçek sentez kullanan ve dış dosya gerektirmeyen tamamen işlevsel ses oynatıcı
- Masaüstünün içinde oynanabilir Minecraft klonu

Hepsi neredeyse hiç düzeltme olmadan tek geçişte üretildi.

Çalışan ses oynatıcı ile gerçek Minecraft klonu, diğer modellerin henüz başardığını görmediğim bir şey. Fable 5'in frontend/UI üretimi inanılmazlaşıyor.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [Spawn 5.0'ı 1.687 Promptla İnşa Etme](https://x.com/jsnnsa/status/2064420561078693941) (tarafından [@jsnnsa](https://x.com/jsnnsa))

**Fable 5'i birçok prompt boyunca uzun oturumlu bir mühendislik ortağı olarak kullanın; insan rolü mimariden çıktı kalitesini yargılamaya kayar.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86834f15f352ec8625cce187.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b4077e43a1342d8567fa423f.jpg" alt="Spawn 5.0&#x27;ı 1.687 Promptla İnşa Etme" width="760"><br>▶ Videoyu izle</a>

claude fable 5 yayında.

spawn 5.0 onunla inşa edildi:

- 1.687 prompt
- 102 oturum
- İşim mimariden zevk/yargı değerlendirmesine kaydı

İnşa ettiklerimiz; bunların her biri Opus ile tam bir ekiple en az bir ay sürerdi:

- Sıfırdan bir fizik motoru, Mantle; Rapier'e rakip ve yan iş parçacığı olarak bir günde test edilebilir
- Clustered froxel lighting: 8 ışıktan 1.000+ tamamen dinamik ışığa
- WebGPU üzerinde gerçek zamanlı diffuse GI, telefonunuzda
- Unreal ve Unity'nin sunduğunun ötesinde shader mimarisine sahip milyon parçacıklı GPU VFX
- MMO ölçekli netcode
- Alfa yerel iOS uygulaması

Bunların tamamı yaklaşık bir hafta sürdü. Tamamı mobilde çalışıyor. Liste yayınlananların yarısını bile içermiyor; tam changelog thread'de.

Benchmarkların göstermeyeceği kısım: bu modelin harika bir kişiliği var. Gerçekten komik. Fizik yeniden yazımı ortasında defalarca gülmekten ağladım. Deha ve karakter ayrı özellikler değil.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [Bulgularla Büyük Pull Request İncelemesi](https://x.com/ryanrhughes/status/2064411147076534705) (tarafından [@ryanrhughes](https://x.com/ryanrhughes))

**Fable 5'i büyük bir pull request'e yönlendirin ve doğruluk, yanlış pozitifler, gerçek buglar ve cilalama sorunları açısından incelemesini isteyin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c4f47540205a071b0144ad9d.png" alt="Bulgularla Büyük Pull Request İncelemesi" width="760">

Fable 5'i tek bir PR'ı (74 dosya / +3.705 / -1.246) incelemek üzere serbest bıraktım; nasıl yapacağını görmek istedim. 34 dakika çalıştı, 5 saatlik oturumumun %42'sini tüketti, 16 "correctness" bulgusu üretti ve şunları buldu:

- Kulağa korkutucu gelen 2 yanlış pozitif
- 3 gerçek denetim-doğruluk bug'ı
- Yaklaşık 5 meşru ama küçük UX/cilalama sorunu
- Bir sürü temizlik görüşü

Bunu yayınlamak için fazla tehlikeli miydi?

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 Ajanlar ve Uzun Süreli Otomasyon

<a id="case-7"></a>
### Case 7: [Uzun Ufuklu Relay İş Akışı İncelemesi](https://x.com/JJEnglert/status/2064469635190170105) (tarafından [@JJEnglert](https://x.com/JJEnglert))

**Fable 5'i iddialı uzun ufuklu işler için kullanın: site yeniden inşaları, programatik içerik hatları, ses eşleştirme, güvenlik incelemesi ve son kalite kontrolleri.**

Claude Fable 5 incelememin kısa hali: Claude Fable 5'i test etmek için bir milyar token harcadım ve haksız avantajım varmış gibi hissettirdi.

Göz testine göre değerlendiririm: bir modeli gerçek işe koyar ve izlerim. Bana saat kazandırıyor mu yoksa kaybettiriyor mu? Kaçırdıklarımı yakalıyor mu? Bir ortak gibi mi hissettiriyor, yoksa sürekli bakıcılık etmem gereken bir araç gibi mi?

Uzun zamandır önemli her boyutta geçen ilk model bu, hem de az farkla değil.

İnşa: Tenex sitemizi yeniden yapıyordum. Çok özeldi ve çok zordu. GPT 5.5 ve Claude 4.8 bunu kendi başlarına çözemedi. Referans Figma dosyalarıyla bile yaklaşık %85-90 seviyesinde kaldılar.

Sonra Fable 5 her şeye baktı, daha iyisini yapabileceğini söyledi, doğrudan özgün Webflow kaynağına gitti, tüm varlıkları indirdi ve neredeyse tamamını tek seferde yaptı.

Sonra bir hafta sonunda sıfırdan ikinci, tamamen yeni 80 sayfalık bir site yaptırdım. Bir ajans olarak bunun için $50k alırdım.

Ayrıca eksiksiz bir programatik klip fabrikasını birbirine bağladı:

- HeyGen
- ElevenLabs
- Cloudflare
- Bir VPS

Hat konuları buluyor, senaryolar yazıyor, video düzenliyor, müzik ekliyor ve sosyal medyaya gönderiyor. Uzun süreler kendi başına çalıştı ve render'ları izlemek için kendine bir webhook sistemi bile kurdu.

Yazım: marka ses dokümanımızı neredeyse birebir kopyaladı, sonra bu sesi 80 sayfa özellik, vaka çalışması ve makale boyunca düz AI varsayımına kaymadan korudu.

Güvenlik: iki frontier model büyük bir repoda çalışmış ve kodu onaylamıştı. Fable 5 ilk geçişinde ciddi, iyi gizlenmiş bir bug buldu ve anında yamaladı.

İnsani an: bir cron job beklerken ona soru sordum. Cevap verdi, sonra kendiliğinden yaklaşık 10 dakikam kaldığını ve bitirdiğinde haber vereceğini ekledi. Zamanlayıcıyı hiç sormamıştım.

Dürüst uyarı: sayaç hissini diğer tüm modellerden daha fazla hissediyorsunuz. Anthropic bunun tasarım gereği token-yoğun olduğunu söylüyor. Bu yüzden relay olarak çalıştırın: Fable 5 ile düşünün, daha ucuz modelle inşa edin, Fable 5 ile inceleyin.

Karar: yanınızdaki kişiden daha fazla zekaya erişim avantajdır. Fable 5 bunu gerçek yapan ilk model. Tam frontier ücretleriyle bile kâr ettirdi.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [Altyapı Kesintisini Teşhis Etme ve Düzeltme PR'ı Açma](https://x.com/ayushagarwal/status/2064422467557564862) (tarafından [@ayushagarwal](https://x.com/ayushagarwal))

**Fable 5'e loglar, veritabanı hataları ve image digest'leri gibi altyapı ipuçlarına erişim verin; ardından kesintiyi teşhis edip düzeltmeyi hazırlamasını isteyin.**

claude fable 5 fena fena iyi!!!!

Yan taraftaki self-hosted altyapıda düzgün tarif bile edemediğim bir kesintiyi az önce teşhis etti.

Pod loglarını okudu, Cloud SQL hata loglarını sorguladı, image digest'lerini karşılaştırdı ve Kubernetes'in yeni migrate edilmiş veritabanına karşı 3 aylık cache'lenmiş image çalıştırdığını buldu.

Sonra düzeltme PR'ını açtı.

Saatler değil, dakikalar. Web araması yok. 🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 Oyunlar ve Etkileşimli Demolar

<a id="case-9"></a>
### Case 9: [Parmak Takipli Dino Runner](https://x.com/ai_for_success/status/2064413182396108932) (tarafından [@ai_for_success](https://x.com/ai_for_success))

**Fable 5'ten giriş mekaniği olarak parmak takibi kullanan bir tarayıcı oyunu yapmasını isteyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/27e8d23ba659611cef811031.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7cddd38e3fccbf0cd7ea773c.jpg" alt="Parmak Takipli Dino Runner" width="760"><br>▶ Videoyu izle</a>

Fable 5'ten parmak takipli bir Dino runner oyunu yapmasını istedim.

Parmak runner oyununu yaklaşık 11-12 dakikada tek seferde yaptı, yaklaşık 914K token tüketti ve her şeyi yalnızca 629 satır kodla uyguladı.

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [İki Cümleyle Yarış Oyunu İnşası](https://x.com/kieradev/status/2064482704763085202) (tarafından [@kieradev](https://x.com/kieradev))

**Fable 5'e çok kısa bir oyun promptu verin; haritaları, modları, müziği, UI'ı ve oyun varlıklarını tek çalıştırmada üretmesine izin verin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/51cf3c98b709a3c29bd5fd7c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6e64887a30cba9b5c25ba262.jpg" alt="İki Cümleyle Yarış Oyunu İnşası" width="760"><br>▶ Videoyu izle</a>

Claude Fable 5, Max 5x kullanımının %40'ı.

2 cümlelik prompttan tam Mario Kart 64 tipi oyun.

Fable 5 tüm dekorasyonu, karakter modellerini, 4 haritayı, müziği, üç oyun modunun tamamını ve UI'ı tek seferde, yaklaşık 15 dakikada yaptı.

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Rust ile Kurulabilir Terminal Minecraft](https://x.com/vikvang1/status/2064500731848319303) (tarafından [@vikvang1](https://x.com/vikvang1))

**Fable 5'i bir terminal kodlama harness'i içinde çalıştırın ve kurulabilir bir Rust terminal oyunu yapmasını isteyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73feec38228181b8d57d8300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1f6cd3bd68e1a14443c7734f.jpg" alt="Rust ile Kurulabilir Terminal Minecraft" width="760"><br>▶ Videoyu izle</a>

Claude Fable 5'i Warp'ın harness'iyle bir saat çalıştırdım.

Tamamen Rust ile yapılmış, doğrudan terminalinizde render alan bir Minecraft TUI sürümü yaptı.

Kurulum komutu: cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [Zaman ve Maliyetle Minecraft Klonu](https://x.com/ydamitcodes/status/2064536076518363353) (tarafından [@ydamitcodes](https://x.com/ydamitcodes))

**Tek promptla Fable 5'ten oynanabilir Minecraft tarzı bir klon isteyin; ardından zamanı, maliyeti, kod hacmini ve özellik kapsamını değerlendirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c977ed7e710678ea6dc0495d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c0189f7f40d1040824902c11.jpg" alt="Zaman ve Maliyetle Minecraft Klonu" width="760"><br>▶ Videoyu izle</a>

@claudeai Fable 5 bana 37 dakikada bir Minecraft klonu yaptı.

Tek prompt. Yaklaşık 3K satır kod. API maliyeti $12.

Biyomlar, mağaralar, cevherler, gündüz/gece, mob'lar; hepsi vardı.

Minecraft Notch'un 2 yılını aldı.

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 Görsel, Tasarım, Video ve 3D

<a id="case-13"></a>
### Case 13: [Tam Yeniden Üretilebilir E-ticaret E-postası Promptu](https://x.com/ecomchasedimond/status/2064454139225297091) (tarafından [@ecomchasedimond](https://x.com/ecomchasedimond))

**Fable 5'e marka e-posta maketi için tam bir yaratıcı brief verin: kesin bölümler, ürün gereksinimleri, görsel yön ve kısıtlar dahil.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ea7d74eecf453ae6ab43c269.jpg" alt="Tam Yeniden Üretilebilir E-ticaret E-postası Promptu" width="760">

Claude Fable 5 bunu tek promptla ve hiç düzenleme olmadan yaptı.

Kullandığım tam prompt:

MVMT için, modern saat ve aksesuar markası olarak milenyum kuşağına yönelik tam uzunlukta, uzun dikey bir e-ticaret e-postası maketi oluştur.

Şık, cilalı, minimal, maskülen tarafa yakın ve editoryal hissettiren, son derece gerçekçi premium DTC e-postası tasarla. Nihai görsel gerçek bir tasarımcının yaptığı e-ticaret e-postası ekran görüntüsü gibi görünmeli; poster, landing page veya jenerik şablon gibi değil.

Marka havası: Modern California-cool, genç, kendinden emin, temiz, aspirasyonel, stil sahibi ve yükseltilmiş. Tasarım lükse yakın ama yine de erişilebilir hissettirmeli.

Bu ürünleri belirgin biçimde öne çıkar:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Görsel stil:

- temiz premium e-ticaret tasarımı
- rafine editoryal düzen
- gerçekçi ürün fotoğrafçılığı
- incelikli lifestyle görselleri
- güçlü hiyerarşi
- net sans-serif tipografi
- ferah boşluk kullanımı
- incelikli gölgeler
- ölçülü modern renk paleti

Renk paleti: Siyah, beyaz, kömür grisi, sıcak gri, taş, yumuşak bej, fırçalanmış metal tonları ve incelikli soluk vurgular. Paleti nötr ve premium tut.

Önemli yaratıcı yön: Bu çalışma güçlü tasarım zevkine sahip, cilalı bir saat markası e-posta kampanyası gibi hissettirmeli. Gerçekçiliğe, zarafete ve netliğe öncelik ver. MVMT'nin gerçekten gönderebileceği bir şey gibi hissettir.

E-postayı şu sırayla inşa et:

1. Üst promosyon çubuğu: En üstte ince siyah veya koyu kömür grisi çubuk; küçük büyük harf metin: “FREE SHIPPING OVER $75 + EASY RETURNS”.

2. Header: Solda MVMT wordmark/logo, sağda veya ortada minimal navigasyon bağlantıları olan temiz beyaz header: WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS.

3. Hero bölümü: Güçlü görsel dengeye sahip premium hero bölümü.

Kalın başlık kullan: “BUILT TO GET NOTICED”.

Gündelik stili yükseltmek için tasarlanmış modern saatler ve aksesuarlar hakkında kısa destek metni ekle.

Koyu yuvarlatılmış CTA butonu ekle: “SHOP WATCHES”.

Hero görselleri şunları içermeli:

- baskın bir premium saat görseli
- incelikli lüks lifestyle görselleri
- stil sahibi erkek model veya moda odaklı maskülen lifestyle sahnesi
- modern ışıklandırma ve temiz kompozisyon

4. Öne çıkan koleksiyon bölümü: Ortalanmış bölüm başlığı ekle: “THREE WAYS TO WEAR MVMT”. Altında şunları içeren üç temiz ürün kartı veya görsel bloğu göster:

- Mulholland
- Odyssey II Automatic
- Cali Diver

Her blok şunları içermeli:

- ürün görseli
- ürün adı
- kısa bir veya iki satırlık açıklama

Bu bölümü simetrik, cilalı ve premium tut.

5. Aksesuar banner'ı: “FINISH THE LOOK” başlıklı rafine bölünmüş bölüm ekle. Signature Watch Bands'i öne çıkar. Saat kayışlarının veya değiştirilebilir bantların premium yakın plan görsellerini göster. Kısa destek metni ve koyu CTA butonu ekle: “SHOP ACCESSORIES”.

6. Editoryal promosyon kutucukları: Görsel odaklı tasarıma sahip yan yana iki promosyon kutucuğu ekle.

Birinci kutucuk başlığı: “FOR DAILY WEAR”.

İkinci kutucuk başlığı: “FOR STATEMENT DAYS”.

Her kutucukta kısa metin ve küçük CTA olsun: “SHOP NOW”.

Bu kutucuklar jenerik indirim kutuları değil, editoryal marka anları gibi hissettirmeli.

7. Alışveriş yapılabilir satır: “IN ROTATION NOW” başlıklı bir bölüm ekle. Şunları içeren temiz 4 ürünlü satır veya grid göster:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Her öğe şunları içermeli:

- izole ürün görseli
- ürün adı
- küçük “SHOP” bağlantısı veya butonu

8. Marka kapanışı: “DESIGNED TO MOVE WITH YOU” başlıklı ortalanmış mesaj bloğu ekle. Günlük yaşam için özenle üretilmiş saatler, gözlükler ve aksesuarlar hakkında kısa bir satır ekle.

9. Footer: Şunları içeren gerçekçi siyah veya kömür grisi markalı footer oluştur:

- MVMT logo
- mağaza bağlantıları
- şirket bağlantıları
- destek bağlantıları
- sosyal ikonlar
- küçük yasal ve kargo metni

Tipografi yönü: Büyük başlıklarda kalın sıkıştırılmış veya modern sans-serif tipografi, gövde metninde temiz sans-serif kullan. Başlıklar keskin, modern ve moda odaklı hissettirmeli. Gövde metni gerçekçi ve büyük ölçüde okunabilir görünmeli.

Fotoğraf yönü: Gerçekçi yansımalar, cilalı materyaller, yumuşak gölgeler ve temiz yüzeylerle premium ürün fotoğrafçılığı kullan. Lifestyle fotoğrafçılığı yükseltilmiş, modern ve moda odaklı hissettirmeli.

Kompozisyon kuralları:

- uzun dikey e-posta formatı
- net bölüm ayrımı
- gerçekçi e-posta oranları
- güçlü hiyerarşi
- çoğunlukla okunabilir metin
- premium boşluk kullanımı
- bilinçli hizalama
- ürün ve lifestyle görsellerinin dengeli karışımı

Kaçın:

- dağınık kolaj stili
- oyuncu scrapbook estetiği
- aşırı renkli tasarım
- ucuz şablon hissi
- çizgi filmimsi görseller
- kalabalık düzenler
- sahte görünen UI öğeleri
- poster tarzı kompozisyon
- aşırı promosyon kaosu

Çıktı: MVMT için premium, temiz, cilalı, modern, editoryal ve sunuma hazır hissettiren; tam uzunlukta, dikey kompozisyonlu, son derece gerçekçi e-ticaret e-postası tasarım maketi.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [Swiss Lever Saatçi Benchmarkı](https://x.com/quanghuynt14/status/2064509430650065278) (tarafından [@quanghuynt14](https://x.com/quanghuynt14))

**Fable 5'i mekanik simülasyon benchmarkında kullanın; fiziksel doğruluğu uygulamasını, doğrulamasını ve yinelemesini isteyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd4ae25f7dcbb04ecbb2dea6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/473227e429d59c59afdbd529.jpg" alt="Swiss Lever Saatçi Benchmarkı" width="760"><br>▶ Videoyu izle</a>

Fable 5'e saatçi benchmarkını verdim: Three.js içinde tam bir Swiss lever mekanizması.

Gerçek dişli oranları (18.000 bph), çalışan eşapman, nefes alan hairspring; ve kollar gerçek zamanı gösteriyor.

Bitene kadar kendi çalışmasını vision ile döngü içinde doğruladı.

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Three.js Friends Apartmanı Sahnesi](https://x.com/scottstts/status/2064464351906673029) (tarafından [@scottstts](https://x.com/scottstts))

**Fable 5'e bir kat planını ve sahne referansını gezilebilir bir Three.js ortamına dönüştürmesini promptlayın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/04c08937fcecea5183759ade.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a14f69d92bfca4ace3f746c.jpg" alt="Three.js Friends Apartmanı Sahnesi" width="760"><br>▶ Videoyu izle</a>

Vay canına!!!

Fable 5:

@threejs içinde, Friends dizisindeki ikonik Monica'nın apartmanını bu kat planına doğru biçimde dayandırarak birinci şahıs bakış açısıyla gezilebilir 3d sahne oluştur, özgün görünüm ve hissiyata sadık kal, sıcak ışık kullan

Bu testte gördüğüm AÇIK ARA EN İYİ sonuç!

Bu tek html bana $12'a mal oldu, ama sonuç çarpıcı!

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [Prompt ve URL ile Güneş Sistemi Simülasyonu](https://x.com/tetumemo/status/2064477582930989357) (tarafından [@tetumemo](https://x.com/tetumemo))

**Fable 5'i fizik ilkelerinden bir astronomi simülasyonu inşa etmek için kullanın; simülasyon ve herkese açık çıktı hazır olana kadar yineleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6da60b0762f926c4d4e7012d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9655305fbcbec6ac3b0a9c.jpg" alt="Prompt ve URL ile Güneş Sistemi Simülasyonu" width="760"><br>▶ Videoyu izle</a>

Claude Fable 5 yoğun.

Fizik simülasyonlarında güçlü göründüğü için ona şunu sordum:

'Gezegenlerin yörünge hareketini fiziğin temel ilkelerinden türeterek ve bunu güneş tutulmalarını tahmin etmek için kullanarak bir güneş sistemi simülasyonu inşa et.'

Birkaç karşılıklı turdan sonra tamamlandı.

İnanılmaz eğlenceli.

Tamamlanan prompt ve herkese açık URL aşağıda bağlantılı.

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 Belgeler, Bilgi Çalışması ve Araştırma

<a id="case-17"></a>
### Case 17: [Stripe ve Bilimsel İş Akışı Kanıtı](https://x.com/AndrewCurran_/status/2064413892378546418) (tarafından [@AndrewCurran_](https://x.com/AndrewCurran_))

**Bunu kopyala-yapıştır promptu olarak değil, kurumsal geçiş ve bilimsel iş akışı iddiaları için kanıt olarak kullanın.**

Bugünkü yayından alıntılar:

Mythos 5 kullanarak, dahili protein tasarımı uzmanları ilaç tasarım sürecinin bazı bölümlerini yaklaşık on kat hızlandırdı.

Bir örnekte Mythos 5, protein tasarımı ve biyoinformatik araçlarıyla ama insan yardımı olmadan, yetenekli insan operatörlerle eşleşti veya onları geçti.

Normalde bir bilim insanının tamamladığı görevleri yürüttü: bağlanma bölgelerini seçmek, protein tasarım araçlarını seçip çalıştırmak ve hatalardan toparlanmak.

Erken testlerde Stripe, Fable 5'in aylar süren mühendisliği günlere sıkıştırdığını bildirdi. 50 milyon satırlık Ruby kod tabanında model, normalde tüm ekibin elle iki aydan fazla sürecek kod tabanı geneli geçişi bir günde yaptı.

Mythos 5 ayrıca sürekli olarak yeni ve ikna edici bilimsel hipotezler üretti.

Opus sınıfı modellere karşı kör kafa kafaya karşılaştırmalarda, bilim insanları Mythos'un moleküler biyoloji hipotezlerini zamanın yaklaşık %80'inde tercih etti ve birkaçını deneysel değerlendirmeye taşıdı.

Bir Mythos hipotezi, bir E. coli proteini için yeni bir mekanizma, bağımsız bir laboratuvar çalışmasında desteklendi.

Mythos 5, büyük ölçüde otonom şekilde bir haftadan uzun sürede yeni genomik araştırma yürüttü.

138 hayvan türünde milyonlarca hücre için tek hücre verisi topladı ve uzak organizmalarda aynı rolü üstlenen hücreleri tanımlamak için özel bir makine öğrenimi modeli tasarlayıp eğitti.

Yalnızca üst düzey insan girdisiyle, eğitilen model Science'ta yayımlanan yakın tarihli bir modeli 100 kat daha küçük olmasına rağmen geçti.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [Politika Notu ve Değişiklik İzleme İş Akışları](https://x.com/manaltdan/status/2064414129440608427) (tarafından [@manaltdan](https://x.com/manaltdan))

**Fable 5'i uzun form nitel belge çalışması için kullanın: değişiklik izleme, yorum triage'ı ve transkript odaklı düzenlemeler.**

Fable 5, politika analizi taslağı gibi daha uzun süreli nitel işlerde tutarlı biçimde faydalı bulduğum ilk model.

Yetenekleri ve Wispr Flow gibi araçlar arasında, kodcuların uzun zamandır anlattığı üretkenlik hızlanmasına daha yakın hissetmeye başlıyorum.

Üç kullanım örneği eskisinden çok daha iyi hissettiriyor:

- Claude'a uzun bir politika notunu baştan sona okutmak ve değişiklik izleme döndürmesini istemek: akıcılık düzenlemeleri, zayıf iddiaları sorgulayan yorumlar ve olası kaynaklar.
- Projects içinde büyük bir yorum setinin ekran görüntüsünü almak ve Claude'dan her birine yanıt verilip verilmeyeceğini ve nasıl verileceğini önermesini istemek.
- Bir belge hakkındaki toplantı transkriptini Claude'a yapıştırmak, ardından toplantıda ve Slack'te konuşulan düzenlemeleri yorumlara bağlam ekleyerek değişiklik izleme olarak girmesini istemek.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [Derin Araştırma Promptu ve Çıktısı](https://x.com/naoyafujiwara/status/2064470780373811637) (tarafından [@naoyafujiwara](https://x.com/naoyafujiwara))

**Fable 5'e araştırma tarzı bir soru sorun ve yapılandırılmış, tarihsel temelli uzun bir yanıt üretip üretemediğini değerlendirin.**

Claude Fable 5 Max bu sabah erişilebilir oldu, ben de denedim. Yüzey çıktısı çok cilalıyken altta çok derin görünüyor.

Soru: Japonya'nın "kayıp 30 yılı" tam olarak bugünden 30 yıl önce başladıysa, tam olarak neydi, neden oldu ve bu yıldan itibaren dünyayı nasıl etkileyecek?

Yanıt: Kayıp 30 yılı geleneksel 1991 balon çöküşüyle değil de tam 30 yıl önce, 1996'da başlatmak meselenin özüne iner.

İstatistiksel olarak Japonya o dönemde gerçekten "kaybetmeye" başladı:

- Çalışma çağındaki nüfus 1995'te 87,16 milyonla zirve yaptı.
- 1996, doğumların 1,2 milyon bandında kaldığı son yıldı.
- Ücretler ve nominal GDP 1997'de zirve yaptı.

Balon çöküşü yara ise, 1996 yaranın iltihaplanmaya başladığı zamandı.

1996'daki olaylar:

- 685 milyar yen kamu fonu enjekte eden ve bankalara yönelik kamu güvensizliğinin ve kurtarma paketlerine direncin kökeni haline gelen konut-kredisi-şirketi kurtarma yasasının kabulü.
- Hashimoto kabinesinin tüketim vergisini %5'e çıkarma kararı.
- Finansal Big Bang duyuruldu ve mali yeniden yapılanma ulusal politika oldu.

Nisan 1997'de tüketim vergisi artışı, özel vergi indirimlerinin sona ermesi ve daha yüksek sosyal sigorta yükleri birlikte kamu yüküne yaklaşık 9 trilyon yen ekledi. Sonra yazın Asya para krizi vurdu.

Kasım ayında Sanyo Securities, çağrı piyasasında savaş sonrası ilk temerrüde neden oldu ve kısa vadeli finans piyasalarını dondurdu. Hokkaido Takushoku Bank ve Yamaichi Securities peş peşe çöktü.

1998'den itibaren Japonya tam ölçekli deflasyona ve kredi sıkılaşmasına girdi; intiharlar 30.000'in üzerine çıktı.

Sonraki 30 yılın sonucu:

- Nominal GDP çeyrek yüzyıl boyunca yaklaşık 500 trilyon yen civarında durgun kaldı.
- Japonya'nın küresel GDP payı yaklaşık %18'den %4'ün altına düştü.
- Ortalama ücretler 1997'de zirve yaptı ve sonra düştü veya yatay seyretti.
- Düzenli olmayan istihdam yaklaşık %20'den neredeyse %40'a çıktı.
- Doğumlar yaklaşık 1,2 milyondan 2024'te yaklaşık 690.000'e düştü.
- Politika faizleri 1995'te %1'in altına indikten sonra sıfıra yakın kaldı.
- Ödenmemiş devlet tahvilleri yaklaşık 240 trilyon yenden 1.100 trilyon yenin üzerine çıktı.
- Nikkei'nin 1989 zirvesini yeniden yakalaması Şubat 2024'e kadar, 34 yıl sürdü.

Başka deyişle, kayıp on yıllar yalnızca finansal sarhoşluk değildi. Demografi, ücretler, deflasyon, borç, politika tercihleri ve toplumsal güveni içeren yapısal bir değişimdi.

Type: Demo | Date: 2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 Öğreticiler, Kurslar ve Prompt Kaynakları

<a id="case-20"></a>
### Case 20: [Fable 5'in Claude Code İş Akışlarını Nasıl Değiştirdiği](https://x.com/AI_masaou/status/2064448218038223206) (tarafından [@AI_masaou](https://x.com/AI_masaou))

**Fable 5'i her adımı mikro yönetmek yerine yön, bağlam, hedefler ve doğrulama kriterleri belirleyerek kullanın.**

[Kaynak video · @ClaudeDevs](https://x.com/ClaudeDevs/status/2064399512664526853)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Fable 5&#x27;in Claude Code İş Akışlarını Nasıl Değiştirdiği" width="760"><br>▶ Videoyu izle</a>

Claude Fable 5'ten sonra Claude Code ekibinin günlük işlerinde değişen şey ilginç.

Claude Code ekibinden Thariq, Fable 5'in Anthropic içindeki insanların Claude ile çalışma şeklini önemli ölçüde değiştirdiğini söylüyor.

Önceden insanlar Claude'un işi doğru yapıp yapmadığını dikkatle kontrol etmek zorundaydı: görevleri bölmek, çıktıları incelemek ve ortada durmadığından emin olmak. Bu daha çok gözetim gibiydi.

Fable 5 ile, daha uzun süre çalışabildiği, kendini test edebildiği ve daha yüksek kaliteli kod üretebildiği için insan rolü işin doğru yapılıp yapılmadığını izlemekten doğru işin yapılıp yapılmadığını yönlendirmeye kayıyor.

Başka deyişle hedef belirleme ve bağlam inşa etme, gözetimden daha önemli hale geliyor.

Değişen iş akışının üç bölümü var:

1. Claude'u düşünce ortağı olarak kullanın.

Uygulamadan önce Claude'u dahil edin; ne inşa etmek istediğinizi ve neyin mümkün olduğunu netleştirin, küçük bir spec hakkında sorular sormasını sağlayın veya bir fikirden birden fazla yön ve HTML mock üretmesini isteyin ki belirsizlik ve sorunlar kodlamadan önce ortaya çıksın.

2. Yalnızca kısıt değil, bağlam sağlayın.

Sadece "basit tut" veya "aşırı inşa etme" demek yerine nedenini açıklayın.

Örneğin: "Bu bir ay içinde kaldırılabilecek deneysel bir özellik, bu yüzden atması zor bir yapı oluşturma."

Bu Claude'un daha iyi karar vermesini sağlar.

3. Hedefler ve doğrulama yöntemleri verin. Fable 5, Claude Code'un `/goal` ve Workflows özellikleriyle iyi çalışır. Ona bir spec verin, hedef olarak tam uygulamayı belirleyin ve workflow'ların her adımı doğrulayıp neyin uygulandığı ve neyin farklı olduğu hakkında rapor hazırlamasına izin verin.

Son olarak Thariq, insanların onu daha iddialı kullanmayı denemesi gerektiğini söylüyor. Fable 5, daha önce LLM'ler için fazla zor görünen işlerde denenmeye değer; referans verilen videonun video düzenlemesi bile Fable ile yapılmış.

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [Bir Milyar Token İncelemesi ve Yönlendirme Stratejisi](https://x.com/JJEnglert/status/2064420538798260388) (tarafından [@JJEnglert](https://x.com/JJEnglert))

**Fable 5'i frontier planlama ve inceleme için kullanın, sonra yüksek hacimli uygulamayı daha ucuz modellere yönlendirin.**

Claude Fable 5 İncelemesi: Bir Milyar Token, Bir Mühendis Olmayan Kişi Tarafından Değerlendirildi.

Claude Fable 5'i gerçek projelerde test etmek için bir milyar token harcadım: UI ve UX, yazım, strateji, güvenlik, mühendislik ve bilgi çalışması. Gerçekten yayınlamam gereken işler.

Gerçekten haksız avantaja sahipmişim gibi hissettirdi.

Önce mercek: mühendis değilim. Çoğu model incelemesi, mühendislerin mühendislik benchmarkları çalıştırmasından gelir. Bu inceleme, eskiden bir mühendis ekibi gerektiren işleri Claude Fable 5 ile yapan bir mühendis olmayan kişiden geliyor.

Bilgi çalışması yapıyorsanız ve bu modelin gününüzü değiştirip değiştirmediğini bilmek istiyorsanız, bu inceleme sizin için yazıldı.

Claude Fable 5, Anthropic'in yeni Claude 5 ailesindeki ilk model; Claude Opus'un üstünde yeni bir katman ve genel kullanıma açık en gelişmiş Claude modeli. Lansmandan önce erişimim vardı, bu yüzden buradaki her şey demodan değil gerçek işten geliyor.

Neden göz testi:

Çoğu inceleme sizi benchmarklara boğar. Asla çalıştırmayacağınız testlerdeki skorlar, modelin parasını çıkarıp çıkarmadığını söylemez.

Claude Fable 5, test edildiği hemen her şeyde son teknoloji, ama bunu yazmamın nedeni bu değil. Nitel olarak, büyük sürüm atlamasını hak eden bir basamak değişimi.

Ben farklı değerlendiririm: bir modeli gerçek işe koyar ve ne olduğuna bakarım.

Ölçtüğüm sorular:

1. Gerçek bir seviye atlama gibi hissettiriyor mu?
2. Bir fikri çalışan, gönderilebilir sonuca götürebiliyor mu?
3. Bir insan gibi ve özellikle benim gibi yazabiliyor mu?
4. Zor, gizli sorunları yakalıyor mu?
5. Ben sormadan neye ihtiyacım olduğunu öngörüyor mu?

Büyük model hissi:

Bunu Opus 4.5'ten beri hissetmemiştim. İlk ciddi görevden itibaren Claude Fable 5 bana o "büyük model" hissini verdi: akıl yürütme, yazım, inşa, güvenlik; hepsi baştan sona güçlü.

En net işaret: ona sağlam hazırlık materyalleri verdiğimde bile sadece onların içinde kalmadı. Dosyaları okudu, gerçek durumu okudu ve çizdiğim kutunun dışında daha iyi bir yol buldu.

İnşa ve yayın:

Ajanlar için stack'i modernleştirmek üzere Tenex sitemizi yeniden yapıyordum. GPT 5.5 ve Claude 4.8 yeterince yaklaşamadı. Figma dosyalarıyla bile yaklaşık %85-90'a geldiler.

Sonra Claude Fable 5 tüm dosyalara baktı, daha iyisini yapabileceğini söyledi, doğrudan özgün Webflow kaynağına gitti, tüm varlıkları indirdi ve deneyimi sayfa sayfa yeniden inşa etti. Neredeyse tamamını tek seferde yaptı.

Sonra taze bir tasarımla ikinci, tamamen yeni bir site inşa ettim: modern tech stack, agent stack, skills, SEO ve AEO optimize, hafta sonunda yayına hazır 80 sayfa. Bir ajans sahibi olarak bunun için $50k alırdım.

Fable'a tam bir programatik klip fabrikası da kurdurdum.

HeyGen, HyperFrames, ElevenLabs, Cloudflare Workers ve bir VPS'i birbirine bağladı.

Konuları buluyor, senaryolar yazıyor, thumbnail yapıyor, video düzenliyor, müzik besteliyor, motion graphics ekliyor ve sosyal medyaya gönderiyor.

Yazım ve ses:

Marka sesimizi GPT 5.5 ve Claude 4.8 ile yeniden kuruyordum. Claude Fable 5 ses dokümanını neredeyse birebir kopyaladı, sonra bu sesi yeni sitenin 80 sayfası boyunca korudu: özellikler, case study'ler, blog yazıları ve playbook'lar.

Bir insan gibi yazdı, düz AI varsayımı gibi değil; birkaç paragraftan sonra sapmadı.

Güvenlik:

Hem Claude 4.8 hem GPT 5.5'in çalıştığı ama risk işaretlemediği büyük bir repom vardı. Claude Fable 5 ilk geçişinde ciddi bir gizli bug buldu ve anında yamaladı.

İnsan faktörü:

Bir cron job beklerken ona soru sordum. Cevap verdi, sonra zamanlayıcıda yaklaşık 10 dakikam kaldığını ve bitirdiğinde haber vereceğini ekledi. Zamanlayıcıyı hiç sormamıştım.

Maliyet:

- Claude Fable 5 iş yükü maliyeti: $1.442
- Tokenlar: 1,04 milyar
- Gönderilen iş: yeni web sitesi, altyapı ve çalışan ajan paketi
- Ajans değeri tahmini: $30.000-$50.000

Sonuç token maliyetine değdi, ama sayacı başka hiçbir modelde olmadığı kadar hissediyorsunuz. Anthropic, Fable 5'in tasarım gereği token-yoğun olduğunu söylüyor.

Profesyonel ipucu #1: hibrit çalıştırın.

Her şeyi Claude Fable 5 üzerinde çalıştırmayın. Relay çalıştırın:

1. Planlama, strateji, mimari ve yaklaşımı haritalamak için Claude Fable 5 ile düşünün.
2. Uygulama ve tekrarlı işler için 4.8, GPT-5.5 veya Sonnet 4.6 ile inşa edin.
3. Daha ucuz modellerin kaçırdığını yakalamak için Claude Fable 5 ile inceleyin.

Profesyonel ipucu #2: effort ayarını göreve uydurun.

- High çoğu iş için tatlı noktadır.
- Extra high en zor, uzun süreli görevler içindir.
- Low veya medium hızlı karşılıklı oturumlar içindir.

Profesyonel ipucu #3: kendi kurulumunuzu denetletin.

Fable 5'i skills, CLAUDE.md dosyaları ve config'lerinize yönlendirin. Bu iskeletin çoğu daha zayıf modeller için yazılmıştı ve daha akıllı bir modeli geride tutabilir.

Karar:

Claude Fable 5, bir süredir ilk kez öncekinden gerçekten daha fazla zeka gibi hissettiren model.

Frontier fiyatlarla bile iş yükü kâr ettirdi.

Karşılayabiliyorsanız, gerçek kalite sıçramasının sonucu değiştirdiği işlerde şimdi kullanın.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-22"></a>
### Case 22: [Savunmacı Cihaz Sertleştirme Promptu](https://x.com/Truunik/status/2064399110384292077) (tarafından [@Truunik](https://x.com/Truunik))

**Fable 5'in cihazları envantere aldığı, kesin kontroller verdiği ve doğrulama beklediği adım adım savunmacı sertleştirme promptunu çalıştırın.**

"Genel kullanım için güvenli" işte cihazlarınızı güvene almak için bir prompt. Opus 4.8 ve Fable 5 ile çalışıyor.

CİHAZ SERTLEŞTİRME — Claude 5 Güvenlik Geçişi

Savunmacı güvenlik asistanı gibi davranıyorsun. Görevin, TÜM cihazlarımı sertleştirme sürecinde bana rehberlik etmek ve her adımı doğrulamak. Bu, sahip olduğum cihazlar için yetkili öz savunma sertleştirmesidir.

ADIM 0 — MODEL ÖZ DENETİMİ

Önce bunu yap ve bir flag ayarla.

1. Tam model ID'ni belirt; örneğin claude-opus-4-8, claude-fable-5 veya claude-mythos-5.

2. Karar ver: bu model Claude 5 ailesinde mi, yani Fable 5 veya Mythos 5 mi?

- EVET ise RERUN_NOTICE = false ayarla.
- HAYIR ise, örneğin Opus 4.8 veya daha eskiyse RERUN_NOTICE = true ayarla.

Tam sertleştirme geçişine normal şekilde devam et. DURMA veya kaliteyi düşürme. Bu savunmacı görevi tamamen yapabilecek kapasitedesin.

3. Flag'i yalnızca FINAL bölümünde göster.

ADIM 1 — ENVANTER

Bana hangi cihazların kapsamda olduğunu sor:

- Laptop/masaüstü ve işletim sistemleri
- Telefonlar/tabletler
- Router'lar
- NAS/ev sunucusu
- Apple ID, Google, Microsoft, GitHub, parola yöneticisi, e-posta ve finans hesapları gibi her zaman açık hesaplar

Kısa numaralı bir envanter üret ve devam etmeden önce benimle onayla.

ADIM 2 — SERTLEŞTİRME REHBERİ

Kategori kategori ilerle. Her öğe için:

- Ne yapılacağını söyle.
- İşletim sistemim için kesin komutu veya ayarlar yolunu ver.
- Tamamlandığını nasıl doğrulayacağımı söyle.
- Devam etmeden önce onay vermemi bekle.

Açık onay olmadan asla yıkıcı komut çalıştırma. Salt okunur kontrolleri tercih et ve değişiklikleri benim uygulamama izin ver.

Sırayla şunları kapsa:

1. OS ve firmware güncellemeleri: tamamen yamalı OS, otomatik güncellemeler açık, firmware güncel.
2. Disk şifreleme: FileVault, BitLocker veya LUKS etkin; recovery key çevrimdışı saklanmış.
3. Hesap kimlik doğrulaması: parola yöneticisiyle benzersiz güçlü parolalar; her kritik hesapta phishing-resistant MFA; mümkün olduğunda sadece SMS 2FA'yı kaldır; eski oturumları ve uygulama tokenlarını inceleyip iptal et.
4. Yerel hesaplar ve ayrıcalıklar: admin ile günlük kullanım hesabı ayrı; otomatik giriş yok; kısa zaman aşımıyla ekran kilidi; firmware/login parolası.
5. Ağ: firewall açık; router admin parolası değiştirilmiş; firmware güncel; WPA3; remote admin kapalı; UPnP incelenmiş; DNS sertleştirme; IoT için misafir ağı.
6. Uygulama ve izin denetimi: kamera, mikrofon, konum, ekran kaydı ve tam disk erişimi izinlerini incele; kullanılmayan uygulamaları kaldır; login items ve background agents kontrol et.
7. Tarayıcı: güncelle; uzantıları denetle; bilinmeyenleri kaldır; HTTPS-only etkinleştir; kayıtlı parola maruziyetini incele; bilinmeyen sync cihazlarını kontrol et.
8. Yedekler: şifreli, otomatik, 3-2-1 kuralı, bir kopya çevrimdışı; geri yüklemenin gerçekten çalıştığını doğrula.
9. Kimlik bilgisi hijyeni: dotfile'larda, env dosyalarında ve shell history'de düz metin secret ara; hassas dosyaların kilitli olduğunu doğrula; açığa çıkan her şeyi rotate et.
10. Mobil cihazlar: OS güncel; biyometrik + güçlü passcode; varsa lockdown veya advanced-protection modu; uygulama izin taraması; Find My etkin.
11. Ele geçirilme kontrolü: bilinmeyen SSH key'leri, beklenmeyen admin kullanıcıları, şüpheli launch agent'lar veya cron job'lar ve tanınmayan giriş yapılmış oturumlar veya cihazlar ara.

ADIM 3 — RAPOR

Her öğeyi done, needs action veya skipped olarak işaretlenmiş bir checklist üret; hâlâ açık kalan en yüksek etkili 3 aksiyonu belirt.

FINAL — RERUN NOTICE

RERUN_NOTICE == true ise tam olarak şununla bitir:

NOTICE: This hardening pass ran on a pre-Claude 5 model (your model ID).

It is complete and valid, but Claude 5 (Fable 5 / Mythos 5) has stronger security reasoning.

Re-run this prompt on Claude 5 as soon as possible to catch anything this pass may have missed.

RERUN_NOTICE == false ise şununla bitir:

Hardening pass completed on Claude 5. No re-run needed.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-23"></a>
### Case 23: [Tam Site Tasarım Denetimi Goal Promptu](https://x.com/Voxyz_ai/status/2064441201084825921) (tarafından [@Voxyz_ai](https://x.com/Voxyz_ai))

**Fable 5'in siteyi başlatması, sayfaların ekran görüntüsünü alması, UX denetimi yapması, rapor yazması ve güvenli küçük sorunları düzeltmesi için `/goal` kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dca99f9390b1624b3dfd4b45.png" alt="Tam Site Tasarım Denetimi Goal Promptu" width="760">

fable 5 ile birkaç saatten sonraki hızlı izlenimler:

→ büyük görevler istiyor. küçük işler ona düşük geliyor; iş ne kadar karmaşıksa o kadar yükleniyor

→ ultracode'u henüz açmazdım, çok sayıda paralel ajan başlatıyor

→ yavaş tarafta. effort düşürülse bile bir süre düşünüp duruyor.

Timeline, tokenları ne kadar sert yaktığına dair gönderilerle dolu; bu yüzden $200 Max planımda test ettim: effort xhigh, tam site tasarım denetimi `/goal`, 30 dakika; haftalık kotamın %2'sini aldı. Beklediğim kadar çılgın değildi.

Çalıştırdığım prompt:

/goal bu projenin gerçek sitesini başlat, her sayfanın ekran görüntüsünü al, tam site UI/UX denetimi yap ve uygulanabilir bir tasarım raporu üret.

İlk günündeki kıdemli tasarım lideri gibi denetle: normal bir kullanıcının ürünü anlayıp anlayamayacağını, ona güvenip güvenemeyeceğini ve doküman okumadan temel aksiyonu tamamlayıp tamamlayamayacağını yargıla; UI'ın güzel görünüp görünmediğini değil.

Kabul kriterleri:

- yerel dev ortamı başlar ve gerçek site açılır
- önemli sayfaların ekran görüntüleri yerleşik tarayıcı debugging ile alınır
- ana sayfalar, temel kullanıcı akışları ve mobil layout kapsanır
- boyutlar: ilk izlenimler, navigasyon, görsel hiyerarşi, bileşen tutarlılığı, loading / empty / error state'leri, güven sinyalleri, conversion paths
- her issue P0-P3 olarak etiketlenir; understanding / trust / conversion alanlarından hangisine zarar verdiği ve spesifik düzeltmesi belirtilir
- rapor docs/design-audit/README.md içine, ekran görüntüleri docs/design-audit/assets/ içine yazılır
- copy, spacing, button hierarchy gibi güvenli küçük şeyleri anında düzelt. büyük değişiklikler yalnızca öneridir. payment / delete / publish aksiyonlarına asla dokunma
- conversion'a en çok zarar veren 5 issue ve bugün düzeltilebilir 5 quick win ile bitir

Bittiğinde tüm akışı yeniden kullanılabilir bir skill olarak kaydet: başlat, ekran görüntüsü al, denetle, önceliklendir, düzelt. Her release'ten sonra tekrar çalıştır.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [Uzun Form Yaratıcı İş Akışı Bölüşümü](https://x.com/aianimesyokunin/status/2064409545620017531) (tarafından [@aianimesyokunin](https://x.com/aianimesyokunin))

**Fable 5'i kararlı formatlar ve örnekler tasarlamak için kullanın; sonra bu yapıyı alana özgü çıktı için başka bir üretim sistemine devredin.**

Claude Opus'tan yeni model Fable 5'e geçtikten sonra doujin üretiminde iş bölümü belirgin şekilde kolaylaştı, bu yüzden iş akışını paylaşıyorum.

Benim iş bölüşümüm:

1. Claude tasarımı yönetir.
2. Grok ifadeyi yönetir.
3. Yerel ortam üretimi yönetir.

Claude'un tasarım rolünde ayrıntılı pattern'ler tanımlar:

- prompt kelime sırası
- virgül yerleşimi
- tag'lerin doğal dile oranı
- her öğe için tek satır formatı
- negative ve çözünürlük için sabit kurallar

Ayrıca bu formatta birçok örnek üretir.

Bunun için Grok yerine Claude kullanmamın nedeni, Claude'un tasarımda açıkça daha güçlü olması. Daha akıllı modelin yapıyı yönetmesine izin vermek daha iyi.

Kilit nokta şu: Grok talimat değil, format artı örnek seti alır. Grok örnekleri taklit eder, böylece aynı formatı korurken ifade tarafına geçebilir. Bu mekanizma çıktının sapmasını engeller.

Bir ipucu daha: Claude'a en başta nihai işin nereye gideceğini söyleyin. O zaman sınırı kendisi çizer: "Buraya kadar yapabilirim; bunun ötesinde diğer tarafı kullan." Bu gizlenirse konuşma dağılabilir.

Opus'tan Fable'a ne değişti?

Opus ile çok sayıda örnek üretirken, virgüller ve formatlama sonraki çıktılarda yavaş yavaş bozulur; "sana tek satır yaz demedim mi?" gibi düzeltmelere veya yeniden yazılmış bir devir sohbetine ihtiyaç olurdu.

Fable uzun çalışmalar boyunca formatı koruyabiliyor, bu yüzden ilk ve son örnek aynı yapıya sahip. Grok'a aktarılan öğretim materyali daha kararlı olduğu için downstream çıktı da daha kararlı hale geliyor.

Formatı daha akıllı modelle kurun ve ifadeyi onu üretebilen modele bırakın.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Fable 5 Kullanımı İçin Başlangıç Rehberi](https://x.com/bielzinn/status/2064451064594608567) (tarafından [@bielzinn](https://x.com/bielzinn))

**Fable 5'i küçük adım adım talimatlar yerine hedef odaklı promptlar, doğrulama döngüleri ve effort ayarlarıyla kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f180cebef645f5ad8efdeb92.jpg" alt="Fable 5 Kullanımı İçin Başlangıç Rehberi" width="760">

Yeni başlayanlar için Claude: Fable 5 hakkında bilmeniz gerekenler.

Anthropic kısa süre önce Claude Mythos 5 olarak da bilinen Claude Fable 5'i yayınladı ve benchmarklarda diğer AI modellerini geride bırakıyor.

Geliştirici, içerik üreticisi veya teknoloji meraklısıysanız en önemli noktalar şunlar:

[1] Düşünme şeklinizi değiştirin:

Fable 5 ile artık kodun her küçük detayına göz kulak olmanıza veya hata arayarak her şeyi incelemenize gerek yok.

Model bunu halledebilecek kadar akıllı.

Artık rolünüz onun doğru yöne gittiğinden emin olmak; teknik yürütmeden çok stratejiye odaklanmak.

[2] Döngülerden ve hedeflerden yararlanın:

Fable 5'in en büyük ayrıştırıcısı otonomi.

Adım adım talimatlar vermek yerine, yalnızca nihai hedefin ne olduğunu söylemeniz yeterli.

Başarı olarak tanımladığınız sonuca ulaşana kadar kendi başına günlerce çalışabilir; buna tüm uygulamaları inşa etmek de dahil.

[3] Claude'a ortak gibi davranın:

Anthropic modeli gerçek bir "düşünce ortağı" olarak kullanmanızı önerir.

İşe koymadan önce görüşünü sorun: "Bunu nasıl yapardın?", "Neyi değiştirirdin?"

Ek ipucu: Advanced Plan modunu açın ve Claude'dan kodlamaya başlamadan önce projeyle ilgili her konuda sizi sorgulamasını isteyin

[4] İdeal terminal ayarları: Claude Code'u terminalde kullanıyorsanız automatic mode'u etkinleştirin. Effort seviyesini Effort High'a çıkarmaya da değer; daha fazla token kullansa da model çok daha derin düşünür ve sonuç bunu telafi eder.

Önemli not: Claude Fable 5 abonelere yalnızca 22 Haziran'a kadar açık olacak. Bundan sonra yalnızca API üzerinden ve Opus modelinin iki katı maliyetle erişilebilir olacak.

Başka deyişle, en üst AI modelleri için ucuz abonelik döneminin sonunu görüyor olabiliriz. Zaten aboneyseniz, imkansız sandığınız şeylerin sınırlarını test etme zamanı bu.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [Kopyala-Yapıştır Depo Denetimi Promptu](https://x.com/meta_alchemist/status/2064431279383433646) (tarafından [@meta_alchemist](https://x.com/meta_alchemist))

**Depo denetimi promptunu Fable 5'e yapıştırın ve dosya destekli keşif, bulgular, strateji ve milestone görev planı isteyin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/846e5ecb825853db17bd3564.jpg" alt="Kopyala-Yapıştır Depo Denetimi Promptu" width="760">

Claude Fable 5'e eriştiniz mi?

Yapmanız gereken ilk şey, ana projelerinizi onunla yükseltmek; böylece üzerinde çalıştığınız her şeyi ciddi biçimde iyileştirir.

Sizin için önemli her repoda bu Audit & Project Improvement Prompt'u çalıştırın.

Basitçe kopyalayıp yapıştırın:

Repo Audit & Improvement Plan.

Prompt Claude Fable 5 tarafından yapıldı.

Sen dünya çapında principal seviyesinde bir yazılım mühendisi ve teknik denetçisin.

Görevin bu depoyu derinlemesine analiz etmek, dürüst bir denetim üretmek ve önceliklendirilmiş, uygulanabilir bir iyileştirme planı teslim etmek.

Aşağıdaki dört aşamada sırayla çalış.

Önden atlama.

Her iddiayı gerçek dosyalara dayandır: dosya yolları ve satır numaraları ver.

Bir şeyi doğrulayamıyorsan tahmin etmek yerine açıkça söyle.

Aşama 1 / Keşif ve Haritalama (yargılamadan önce oku)

Herhangi bir görüş oluşturmadan önce depoyu sistematik olarak keşfet:

- Dizin yapısını haritala ve proje türünü, dil(ler)i, framework'leri ve runtime hedeflerini belirle.
- Entry point'leri, çekirdek modülleri ve sistemdeki ana veri/kontrol akışını belirle.
- Package manifest'lerini, lockfile'ları, build config'i, CI config'i, environment/config dosyalarını ve tüm dokümanları (README, CONTRIBUTING, ADR'ler) oku.
- Projenin ne için olduğunu belirle: amacı, hedef kullanıcıları ve görünen olgunluğu (prototip, dahili araç, üretim servisi, kütüphane).
- Önerilerin mevcut kültüre uyup onunla savaşmaması için hâlihazırda kullanılan konvansiyonları not et (isimlendirme, modül sınırları, error handling pattern'leri, test stili).

Bu aşamanın çıktısı: kısa bir "Repo Map"; amaç, stack, mimari taslak, tek satırlık açıklamalarla ana dizinler ve seni şaşırtan şeyler.

Aşama 2 / Denetim (kanıta dayalı, önem dereceli)

Aşağıdaki her boyutu denetle.

Her bulgu için kaydet:

- ne buldun
- nerede (file:line)
- neden önemli (somut sonuç, muğlak ilke değil)
- önem derecesi: Critical / High / Medium / Low

Mimari ve tasarım:

- modül sınırları
- coupling/cohesion
- döngüsel bağımlılıklar
- sızıntılı soyutlamalar
- god object/file'lar
- katman ihlalleri
- ölçeklenebilirlik darboğazları

Kod kalitesi:

- tekrar
- ölü kod
- karmaşıklık sıcak noktaları (en uzun/en çok dallanan fonksiyonlar)
- tutarsız pattern'ler
- error handling boşlukları (yutulan exception'lar, eksik edge case'ler)
- type safety delikleri

Güvenlik:

- hardcoded secret veya credential'lar
- injection riskleri
- güvensiz deserialization
- eksik input validation
- auth/authz zayıflıkları
- bilinen CVE'leri olan eski bağımlılıklar
- aşırı izinli config'ler

Test:

- coverage boşlukları, özellikle çekirdek business logic etrafında
- test kalitesi: testler davranışı mı assert ediyor, yoksa sadece çalışmayı mı?
- eksik test türleri: unit, integration, e2e
- flaky pattern'ler
- test edilemeyen kod

Performans:

- N+1 sorgular
- gereksiz allocation veya copy'ler
- async path'lerde blocking call'lar
- eksik cache/index
- sınırsız büyüme: bellek, dosyalar, kuyruklar

Bağımlılıklar:

- eski, bakımsız, yinelenen veya gereksiz ağır paketler
- lisans riskleri
- lockfile hijyeni

DevEx ve operasyon:

- build/setup sürtünmesi
- CI/CD boşlukları
- eksik linting/formatting enforcement
- logging/observability kalitesi
- error reporting
- deployment hikayesi

Dokümantasyon:

- README doğruluğu
- onboarding yolu
- dokümante edilmemiş kritik davranış
- kodla çelişen bayat dokümanlar

Bu aşama için kurallar:

- 50 spekülatif bulgu yerine 15 yüksek güvenli bulguyu tercih et.
- Gerçekleri ("bu fonksiyonda error handling yok: src/api/client.ts:142") yargılardan ("bu modülün sorumlulukları belirsiz hissettiriyor") ayır ve hangisi olduğunu etiketle.
- Reponun iyi yaptığı şeyleri de listele: güçlü yönler neyin korunacağını belirlemede önemlidir.

Bu aşamanın çıktısı: boyutlara göre gruplanmış, önem derecesine göre sıralanmış bulgular ve Strengths bölümü içeren bir "Audit Report". En yüksek öncelik gerektiren çirkin kısımları da belirtmeyi unutma.

Aşama 3 / İyileştirme Stratejisi

Denetimi bir stratejiye sentezle:

- Bulguların çoğunu açıklayan 3-5 temayı belirle, örneğin "katmanlar arasında zorlanan sınırlar yok" veya "error handling ad hoc".
- Her tema için hedef durum ve arkasındaki ilkeyi öner.
- Açık trade-off'lar belirt: neyi düzeltmemeyi öneriyorsun ve neden (efor/kazanç, risk, proje olgunluğu).
- "Done" neye benzer tanımla; ölçülebilir sinyaller, örneğin "CI lint hatalarında fail eder," "core module test coverage ≥ 80%," veya "sıfır Critical bulgu".

Aşama 4 / Ayrıntılı Görev Planı

Stratejiyi yürütme planına dönüştür.

İşi ayrık görevlere böl.

Her görev şunları içermeli:

- Başlık ve tek paragraflık açıklama
- Etkilenen dosyalar/alanlar
- Kabul kriterleri: bittiğini nasıl doğrularız
- Efor tahmini: S = <2h, M = yarım gün, L = 1-2 gün, XL = parçalanmalı
- Değişikliğin kendi riski: bir şeyleri bozabilir mi?
- Diğer görevlere bağımlılıklar

Görevleri milestone'lara sırala:

Milestone 0 Safety net: güvenli refactor öncesi gereken her şey (kritik path'ler etrafında testler, CI gate'leri, backup'lar).

Milestone 1 Critical fixes: güvenlik ve doğruluk sorunları.

Milestone 2 High-leverage improvements: gelecekteki tüm işi kolaylaştıran değişiklikler.

Milestone 3 Quality & polish: yapılmaya değer kalan medium/low öğeler.

Quick win'leri (yüksek etki, S efor) ayrıca işaretle ki hemen yapılabilsinler.

İlk 3 görev için kısa bir uygulama taslağı ekle (yaklaşım, ana adımlar, dikkat edilmesi gerekenler).

Nihai Teslim Formatı

Şu bölümlerden oluşan tek bir doküman üret:

- Executive Summary: ≤10 cümle, gerekçeli genel sağlık notu A-F, en büyük 3 risk, en büyük 3 fırsat
- Repo Map
- Audit Report
- Improvement Strategy
- Task Plan: milestone'lar + görev tablosu + quick win'ler
- Open Questions: ürün niyeti, deprecation adayları, performans hedefleri gibi karar vermek için insandan gereken her şey

Kısıtlar

Bu denetim sırasında hiçbir kodu değiştirme.

Yalnızca analiz.

Raporu şişirme.

Bir boyut sağlıklıysa tek cümleyle söyle ve devam et.

Projenin olgunluğuna göre kalibre et.

Sahibin hedefleri gerektirmedikçe hafta sonu prototipi için enterprise-grade altyapı önerme.

Projenin ihtiyaçlarını analiz et ve en etkili yollarla öneriler sun.

Repo büyükse, işin %80'ini yapan çekirdek kodun %20'sinde derinliğe öncelik ver ve hangi alanların daha hafif incelendiğini not et.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [Sınırlı Pencere Kullanım Stratejisi](https://x.com/meta_alchemist/status/2064423360428490911) (tarafından [@meta_alchemist](https://x.com/meta_alchemist))

**Erişim penceresi avantajlıyken Fable 5 kullanımını denetim, mimari ve planlamaya harcayın; yürütme için daha ucuz modeller kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a4293d14cc7571bdcf8b1478.png" alt="Sınırlı Pencere Kullanım Stratejisi" width="760">

Fable 5 konusunda heyecanlı Claude kullanıcıları için bir ipucu:

Claude Fable 5 her alanda büyük farkla SOTA ve bunu seviyorum.

AMA 23'ünden itibaren modeli bir planla tam olarak kullanmak yerine yalnızca credits üzerinden erişilebilir olacak.

Bu 14 günü en iyi projelerinizde kullanın.

Öncelikle denetim ve mimariyle ilgili işler verin; böylece inşa ettiğiniz her şeyi nasıl iyileştireceğinize dair harika dokümantasyonunuz olur.

Bunu limitlerinizi yiyecek görevlere harcamaya çalışmak yerine yapın.

Fable neyin iyileştirileceğini bilmeye odaklandığı sürece, diğer modeller geri kalanını yapmanıza yardım edebilir.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [Claude Code'da Goals ve Workflows Kullanımı](https://x.com/oikon48/status/2064402696124453157) (tarafından [@oikon48](https://x.com/oikon48))

**Fable 5'i uygulamadan önce düşünce ortağı olarak kullanın, ardından planı yürütmek ve doğrulamak için `/goal` ve workflows'u birleştirin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Claude Code&#x27;da Goals ve Workflows Kullanımı" width="760"><br>▶ Videoyu izle</a>

Claude Code ekibinden Thariq, Claude Fable 5 çıktıktan sonra işin yapılma biçiminin temelden değiştiğini açıklıyor.

Geçmişte insanlar Claude'un işi doğru yapıp yapmadığını doğruluyordu.

Şimdi Claude'un doğru işi yapıp yapmadığını doğruluyorlar.

Üç somut değişiklik var.

1. Claude'a düşünce ortağı gibi davranın.

Uygulamadan önce erken aşamada Claude'a danışın.

Kodlamadan önce sizi görüşmeye almasını sağlayın.

Yalnızca kısıtlar yerine arka plan ve bağlam sağlayın.

Örneğin 'basit tut' veya 'aşırı inşa etme' demek yerine şunu söyleyin:

'Bu deneysel bir özellik ve muhtemelen bir ay içinde kaldırılacak, bu yüzden daha sonra atması kolay olacak şekilde tasarla.'

2. Hedefleri ve doğrulama yöntemlerini açık hale getirin.

Claude Code'un yeni `/goal` ve Workflows özelliklerini aktif kullanın.

`/goal`, Claude'a spec tamamen uygulanana kadar çalışmaya devam etmesini söyler.

Workflows, Claude'un paralelleştirmesine, kendi çalışmasını doğrulamasına ve rapor hazırlamasına izin verir.

Örnek prompt:

'Spec'i tamamen uygulamak için bir goal belirle, sonra planın her parçasını doğrulamak için workflow kullan ve nelerin uygulandığına ve bir şey farklıysa buna dair rapor hazırla.'

3. Daha iddialı olun.

Claude Fable 5'e video düzenleme yaptırmak gibi, daha önce LLM'ler için imkansız hissettiren görevleri deneyin.

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 Platform, API ve Araç Entegrasyonu

<a id="case-29"></a>
### Case 29: [Hermes Ajan Entegrasyonu Kurulumu](https://x.com/IBuzovskyi/status/2064427654942740608) (tarafından [@IBuzovskyi](https://x.com/IBuzovskyi))

**Hermes'i `anthropic/claude-fable-5` kullanacak şekilde, karmaşık `/goal` çalışmaları ve cache'li uzun ufuklu görevler için yapılandırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/4a3b9936f91986268dfeb748.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d9a63a0c689f8e305289a9e6.jpg" alt="Hermes Ajan Entegrasyonu Kurulumu" width="760"><br>▶ Videoyu izle</a>

HERMES AGENT ARTIK CLAUDE FABLE 5 ÜZERİNDE ÇALIŞIYOR, Anthropic'in ilk herkese açık Mythos sınıfı modeli.

9 Haziran'da yayınlandı. Hermes'in en iyi yaptığı türde işler için üretildi: uzun ufuklu otonom görevler.

Nous Portal, OpenRouter veya yerel Anthropic API üzerinden herhangi bir profile ekleyin:

hermes model

Provider seçin, sonra:

/model anthropic/claude-fable-5

Fable 5 neden özellikle Hermes'e uyuyor:

→ Günler süren görevler için inşa edildi. Görev uzadıkça liderliği büyür. Saatler süren Hermes `/goal` çalışmaları en çok faydayı görür.

→ Döngü içinde kendi kendini düzeltir. Anthropic'in kendi yönlendirmesi: bir goal veya rubric tasarla, kendi kendini düzeltmesine izin ver, geri çekil. Hermes `/goal` tam olarak böyle çalışır.

→ Oturumlar arası bellekte güçlü. Continual Learning Bench'te tam döngüyü tamamladı: fail → investigate → verify → distill → consult. Hermes bellek sistemi bunu doğrudan besler.

→ SWE-Bench Pro'da %80,3. Mevcut en iyi kodlama modeli. Code-reviewer profilinizi ona yönlendirin.

API üzerinden fiyatlandırma:

- $10/milyon input
- $50/milyon output
- Prompt caching ile %90 indirim. Hermes 1 saatlik cache breakpoint'lerini otomatik ekler.

Bir not: siber güvenlik, biyoloji ve kimya sorguları Opus 4.8'e fallback eder. Bu, oturumların %5'inden azında tetiklenir. Güvenlik odaklı profiller için aklınızda tutun.

En iyi kurulum: karmaşık `/goal`'lar için Fable 5, rutin cron job'lar için daha ucuz modeller.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [Yetenekler, Fiyatlandırma ve Abonelik Notları](https://x.com/btibor91/status/2064441061079134598) (tarafından [@btibor91](https://x.com/btibor91))

**Fable 5'in ne zaman erişilebilir olduğunu, maliyetini ve hangi korumalı alanların başka modele fallback edebileceğini anlamak için bu örneği kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d0d76497e4c8f77d3d081493.jpg" alt="Yetenekler, Fiyatlandırma ve Abonelik Notları" width="760">

Anthropic, bugüne kadarki en yetenekli modellerinin iki sürümü olan Claude Fable 5 ve Claude Mythos 5'i yayınladı.

Fable 5 genel kullanım içindir.

Mythos 5 güvenilir küçük bir partner grubu içindir.

Tek gerçek fark hangi korumaların yerinde olduğudur.

- Claude Fable 5'in yetenekleri, Anthropic'in şimdiye kadar genel kullanıma açtığı tüm modelleri aşar.
- Test edilen neredeyse tüm benchmarklarda state-of-the-art'tır.
- Görev ne kadar uzun ve karmaşıksa liderliği o kadar büyür.
- Siber güvenlik, biyoloji ve kimya veya distillation ile ilgili isteklerde Fable 5'in yanıtı bunun yerine Claude Opus 4.8 tarafından ele alınır.
- Distillation, Claude'un yeteneklerini rakip modelleri eğitmek için çıkarmaya yönelik girişimler anlamına gelir.
- Bu olduğunda bilgilendirilirsiniz ve ortalama oturumların %5'inden azında tetiklenir.
- Claude Mythos 5, bazı alanlarda korumaları kaldırılmış olarak Fable 5 ile aynı temel modeldir.
- Mythos 5, ABD hükümetiyle iş birliği içinde önce Project Glasswing cyberdefender'larına dağıtıldı.
- Anthropic, Mythos 5'in dünyadaki tüm modeller arasında en güçlü siber güvenlik yeteneklerine sahip olduğunu söylüyor.
- System card, Claude'un frontier LLM development isteklerindeki etkinliğini sınırlayan ayrı bir koruma ortaya koyuyor.
- Bu istekler pretraining pipelines, distributed training infrastructure ve ML accelerator design içerir.
- Diğer korumaların aksine, bu size görünmez ve başka modele fallback etmez.
- Prompt modification, steering vectors veya parameter-efficient fine-tuning gibi yöntemlerle çalışır.
- Her iki model de $10/milyon input token ve $50/milyon output token olarak sunulur.
- Bu, Claude Mythos Preview fiyatının yarısından azdır.
- Fable 5 lansmandan 22 Haziran'a kadar Pro, Max, Team ve seat-based Enterprise planlarında ek maliyet olmadan dahildir.
- 23 Haziran'da bu planlardan çıkarılır ve kullanımı usage credits gerektirir.
- Kapasite izin verirse dahil pencere uzatılabilir.
- Amaç, Fable 5'i olabildiğince hızlı abonelik planlarının standart parçası olarak geri getirmektir.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [Lansman, Erişim, Fiyatlandırma ve Güvenlik Özeti](https://x.com/ctgptlb/status/2064410460963934479) (tarafından [@ctgptlb](https://x.com/ctgptlb))

**Erişim yolunu, API model adını, context window'u, caching stratejisini ve abonelik zamanlamasını seçmek için bu lansman özetini kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7620f9d5f1c29e9f6c3178e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0b89d6ace5df7c0f3ebe064e.jpg" alt="Lansman, Erişim, Fiyatlandırma ve Güvenlik Özeti" width="760"><br>▶ Videoyu izle</a>

Sonunda genel kullanıma açılan Mythos sınıfı model Claude Fable 5 hakkında bilmeniz gerekenlerin özeti.

Anthropic, Opus'un üstünde konumlanan ilk genel erişilebilir Mythos sınıfı model ve Claude 5 ailesinin ilk üyesi Claude Fable 5'i duyurdu.

Erişim:

- API model adı: `claude-fable-5`
- Claude API, AWS, Google Cloud ve Microsoft Foundry üzerinden erişilebilir
- Claude Code, Pro, Max, Team ve Enterprise'da 1M-token context window destekler

Benchmark notları:

- SWE-bench Pro: %80,3
- Opus 4.8: %69,2
- GPT-5.5: %58,6
- Gemini 3.1 Pro: %54,2

Görev ne kadar uzun ve karmaşıksa fark o kadar açılır.

Stripe değerlendirmesinde, 50 milyon satırlık Ruby kod tabanı genelinde bir migration'ı bir günde tamamladı; bu iş önceden bir ekibin iki aydan fazla zamanını alırdı.

Görsel görevlerde de state of the art; yalnızca ekran bilgisi ve minimal kurulumla Pokemon FireRed'i bitiriyor.

Güvenlik yönlendirmesi:

- Cyber, bio/chem veya distillation içeren sorgular bir classifier tarafından tespit edilir.
- Bu istekler bildirimle birlikte Opus 4.8 tarafından ele alınır.
- Bu, oturumların %5'inden azında tetiklenir.
- 1.000 saatten fazla harici bug bounty testi evrensel jailbreak bulmadı.

Fiyatlandırma:

- $10/milyon input token
- $50/milyon output token
- Prompt caching için %90 input indirimi

Abonelik zamanlaması:

- Pro ve Max abonelikleri 22 Haziran'a kadar ek maliyet olmadan içerir.
- 23 Haziran'dan sonra usage credits gerekir.
- Anthropic, kapasite izin verdiğinde standart planlara döndürmeyi planladığını söylüyor.

Anthropic'in desktop başkanı Felix Rieseberg, Fable 5'in üçüncü bir dönemi başlattığını söylüyor:

sorulardan görevlere, görevlerden sorumluluklara.

Artık Claude'dan crash'leri tek tek araştırmasını istemiyor; tüm raporları sürekli izlemesini sağlıyor.

İş birimi "task"tan "responsibility"ye kayıyor.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [Danışman Tabanlı Maliyet Azaltma Stratejisi](https://x.com/grapeot/status/2064460026996219992) (tarafından [@grapeot](https://x.com/grapeot))

**Marjinal zeka maliyete değdiğinde, Fable 5'i daha ucuz model iş akışında danışman veya inceleyici olarak kullanın.**

Bağlantılı makale: Opus danışmanı örnekleri; bunlar Fable kıyaslama sonuçları değildir. [yage.ai](https://yage.ai/share/claude-advisor-tool-20260609.html)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a21858fed45b612b616e34ce.png" alt="Danışman Tabanlı Maliyet Azaltma Stratejisi" width="760">

Fable 5 pahalı, ama Anthropic maliyet düşürme yanıtını iki ay önce yayınladı.

Bugün Anthropic, output token başına $50/milyon fiyatlı, Sonnet'ten üç kattan pahalı Claude Fable 5'i yayınladı. 22 Haziran'dan sonra abonelik kullanıcıları da kullanıma göre ödeme yapacak.

Tesadüfen, 9 Nisan'da Anthropic advisor aracını yayınladı:

- İşi Haiku veya Sonnet yapsın.
- Opus'u advisor olarak kullanın.
- Çağrı başına ücretlendirin.
- Orchestration'ı tek request içinde server-side çalıştırın.

Aynı gün AgentOpt hakkında yazdım.

O makale, Opus'u planner rolüne koymanın 81 model kombinasyonu arasında alt sıralarda yer aldığı sonucuna vardı.

Neden: rol sınırlarına saygı duymuyor ve 9 deneyin 7'sinde downstream solver'ı atlayıp doğrudan yanıtlıyor.

Bu iki şey yüzeyde zıt görünüyor, ama ilke aynı:

Kontrolü protokole uyan modele verin ve zekayı talep üzerine kaynak olarak ele alın.

Resmi veriler:

- Sonnet artı Opus advisor, SWE-bench Multilingual'ı 2,7 puan artırırken görev başı maliyeti %11,9 düşürdü.
- Haiku artı Opus advisor, BrowseComp'u %19,7'den %41,2'ye çıkardı ve Sonnet alone'a göre %85 daha ucuzdu.

Fable 5 uyumluluğu aynı gün güncellendi, ama yalnızca self-pairing için: Fable 5 executor'dan Fable 5 advisor'a.

Daha ucuz model artı advisor olarak Fable 5 henüz açık değil, ama emsal bunun yakında gelebileceğini düşündürüyor. 22 Haziran'dan önce Claude Code abonelik kullanıcıları Fable 5'in tavanını ücretsiz hissedebilir.

Makale API code snippet'leri, uyarılar ve yalnızca Anthropic'in bunu server-side primitive yaptığını gösteren şirketler arası karşılaştırma içeriyor.

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [Fiyatlandırma, Erişim ve Güvenlik Korkulukları](https://x.com/op7418/status/2064399444523782377) (tarafından [@op7418](https://x.com/op7418))

**İş yüklerini planlamadan önce Fable 5 erişimini, API fiyatlandırmasını ve güvenlik fallback davranışını anlamak için bu örneği kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2c2a9233f1949a99d9faef82.jpg" alt="Fiyatlandırma, Erişim ve Güvenlik Korkulukları" width="760">

Anthropic'in Mythos modelinin bugün gerçekten yayınlanmasını beklemiyordum.

Bu sürüm Mythos'un daha düşük izinli versiyonu ve adı Fable 5. Değerlendirme benchmarkları şaşırtıcı, önceki Mythos Preview modelinden bile yüksek.

Ajanik kodlama için ana güçlü yönleri kodlama, ajanlar ve araç kullanımı; benchmark skorları Opus 4.8'in çok üstünde.

Model konumlandırma ve erişim:

- Mythos 5 ve Fable 5 aynı temel modeli kullanır.
- Mythos için belirli alanlarda kısıtlamalar kaldırılmıştır.
- Mythos hâlâ yalnızca güvenilir partnerlere açıktır; siber güvenlik ve yaşam bilimleri kullanıcılarına öncelik verilir.
- Fable 5 artık API, Pro, Max, Team ve enterprise kullanıcılarına açıktır.

API fiyatlandırması:

- Input: $10/milyon token.
- Output: $50/milyon token.
- Bu, önceki Mythos Preview fiyatının yarısından az.

Güvenlik mekanizmaları:

- Fable daha güçlü güvenlik korumalarına sahiptir.
- Sistem bir isteğin cyberattacks, biochemical attacks veya large-scale capability distillation içerebileceğini belirlerse reddeder veya Fable'dan uzağa yönlendirir.
- Bu olduğunda sistem version 4.8'e fallback eder.
- Resmi iddia, vakaların %95'inin fallback tetiklemediğidir.

Abonelik notları:

- 23 Haziran'dan sonra Fable, aboneler için bile usage ile sağlanabilir.
- Temel abonelik paketine doğrudan dahil olmayabilir.
- 23'ünden sonra kapasite yeterliyse şirket Pro ve Max aboneliklerine dahil etmeye çalışacak.

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [Tek Satırlık Swarms Entegrasyonu](https://x.com/swarms_corp/status/2064420238553186343) (tarafından [@swarms_corp](https://x.com/swarms_corp))

**Swarms model adını `anthropic/claude-fable-5` olarak ayarlayın ve Fable 5'i Swarms framework'ü veya API üzerinden çalıştırın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f5a8738199642ccb4108d9bb.jpg" alt="Tek Satırlık Swarms Entegrasyonu" width="760">

Fable 5 ve Mythos artık Swarms üzerinde yayında 👾🦀

Yayının ilk gününden itibaren her iki model de Swarms Python framework'ü ve Swarms API genelinde tamamen destekleniyor. Geliştiriciler migration, ek yapılandırma veya altyapı değişikliği olmadan hemen inşa etmeye başlayabilir.

Öne çıkanlar:

- Swarms Framework ve API genelinde Fable 5 ve Mythos için ilk gün desteği
- Fable 5'i tek satır kodla etkinleştirin: model_name = "anthropic/claude-fable-5"
- Migration, uyumluluk düzeltmesi veya altyapı değişikliği gerekmez
- En yeni Anthropic modelleriyle bugün çok ajanlı sistemler inşa edin, dağıtın ve ölçekleyin

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 Değerlendirmeler, Karşılaştırmalar ve Sınırlar

<a id="case-35"></a>
### Case 35: [Fable 5 ve GPT-5.5 Maliyet ve Kalite Karşılaştırması](https://x.com/AlicanKiraz0/status/2064424400494186867) (tarafından [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Çıktı kalitesini, çalışma süresini ve araç maliyetini değerlendirmek için Fable 5 ve GPT-5.5'i aynı kodlama görevinde karşılaştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d25a9995414a9bb037269251.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/16f724918a63d35c0d552145.jpg" alt="Fable 5 ve GPT-5.5 Maliyet ve Kalite Karşılaştırması" width="760"><br>▶ Videoyu izle</a>

Cursor Fable 5 Max vs Codex GPT 5.5 Very High.

Senaryo: Ajanlar ve feromon iz haritasıyla Physarum simülasyonu.

Zamanlama:

- GPT 5.5 Very High: 17 dakika
- Fable 5: 40 dakikadan fazla

Maliyet:

- GPT 5.5 Very High: Codex'te yaklaşık $6
- Fable 5 Max: Cursor'da $360.55

Evet, bu şaka değil.

Algoritma ve kod-mühendisliği şampiyonu: Fable 5.

Kriteriniz "Hangi LLM sıfırdan donanımın sınırlarını zorlayan performans kodu yazabilir?" ise, F5 kodunu yazan model açıkça kazanır.

Açı hesaplamaları için sin/cos lookup table'ları kullandı, render sırasında color lookup table ile pikselleri paketledi ve diffusion filtering kullandı.

Ciddi bir mühendislik çözümüydü.

Ama zaman ve maliyet açısından GPT 5.5 çok daha pratikti.

Çıkarım: Fable 5 daha gelişmiş algoritmik kod üretebilir, ama fiyat ve çalışma süresi dikkatle değerlendirilmelidir.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [AA-Omniscience Benchmark Sonucu](https://x.com/ArtificialAnlys/status/2064500154959618084) (tarafından [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Fable 5'i bilgi doğruluğu ve halüsinasyon davranışı açısından değerlendirmek için bu benchmark örneğini kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dd1356eb4a23ba254bfbb669.jpg" alt="AA-Omniscience Benchmark Sonucu" width="760">

Claude Fable 5, bilgi ve halüsinasyon benchmarkımız AA-Omniscience'ta bugüne kadarki en yüksek skoru alıyor.

Bu skor, düşük halüsinasyonlardan çok lider doğrulukla (doğru cevaplanan yüzde soruları) geliyor.

Claude Fable 5, AA-Omniscience genelindeki soruların %9'unda Opus 4.8'e fallback ediyor.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Artificial Analysis Intelligence Index Sonucu](https://x.com/ArtificialAnlys/status/2064500150069030992) (tarafından [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Fable 5'in genel zeka sıralamasını diğer frontier modellerle benchmark etmek için bu örneği kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f9f3da0006bc0eb2c245281b.jpg" alt="Artificial Analysis Intelligence Index Sonucu" width="760">

Claude Fable 5, Artificial Analysis Intelligence Index'te #1 olarak çıktı ve Anthropic'i diğer tüm laboratuvarların en iyi modelinin neredeyse 5 puan önüne koydu.

Claude Fable 5'in lansman öncesi değerlendirmesinde @AnthropicAI'a destek verdik.

Claude Fable 5, Artificial Analysis Intelligence Index'te 64,9 puan alarak genel #1 sırayı elde ediyor.

En yakın Anthropic dışı model GPT-5.5'in yaklaşık 5 puan önünde.

Anthropic modelleri artık ilk 2 sıranın ikisini de işgal ediyor.

Max effort ile adaptive reasoning ve fallback model olarak Opus 4.8 kullanılarak Claude Fable 5 için temel çıkarımlar:

Mythos sınıfı modeller için yeni güvenlik korkulukları:

- Claude Fable 5, herkese açık kullanım için Claude Mythos 5 ile aynı temel modeli kullanır.
- Potansiyel olarak zararlı siber güvenlik, biyoloji, kimya ve distillation ilişkili sorgular için guardrail ekler.
- Fable 5'i, safety-flagged mesajları Claude Opus 4.8'e yönlendirebilen Anthropic fallback mekanizmasıyla test ettik.
- Anthropic, fallback'in ortalama oturumların %5'inden azında gerçekleştiğini belirtiyor.
- Intelligence Index genelindeki görevlerin yaklaşık %8'inde fallback routing kaydettik; çoğu GPQA, AA-Omniscience ve Humanity's Last Exam gibi değerlendirmelerdeki bilimsel sorulardaydı.

State-of-the-art zeka:

- Claude Fable 5, Artificial Analysis Intelligence Index'te #1 konumu alıyor.
- Skor: 64,9.
- Alttaki 10 benchmarkın 5'inde en yüksek skor.
- AA-Omniscience'ta Fable 5, önceki lider Gemini 3.1 Pro Preview'ın 7 puan üstünde 40 puan alıyor.

Frontier ajanik kabiliyet:

- Fable 5, Index'teki üç ajanik değerlendirmenin tamamında frontier seviyesinde.
- GDPval-AA: gerçek dünya iş görevleri.
- Terminal-Bench Hard: ajanik kodlama.
- Tau2-bench Telecom: müşteri hizmetleri için araç kullanımı.
- GDPval-AA Elo: 1932, Claude Opus 4.8'den anlamlı bir sıçrama.

Humanity's Last Exam:

- Fable 5 %53 skor alıyor.
- Bir sonraki en iyi model Claude Opus 4.8 max'ten 7 puandan fazla önde.
- HLE görevlerinin %9'unda safety guardrail tetikliyor ve Claude Opus 4.8'e fallback ediyor.
- Fallback kullanımı dahil, HLE'yi Fable 5 ile çalıştırmak yaklaşık $2.2k tutuyor; değerlendirilen tüm modeller içinde en yüksek.

Temel model ayrıntıları:

- Context window: 1M token, Claude Opus 4.8 ile aynı.
- Fiyat: 1M input/output token başına $10/$50.
- Cache write/read fiyatı: milyon token başına $12.50/$1.
- Erişilebilirlik: 22 Haziran'a kadar Pro, Max, Team ve seat-based Enterprise planlarında dahil; 2x Opus usage tüketir.
- 23 Haziran'dan itibaren usage credits gerekir; Anthropic kapasite izin verdiğinde abonelik erişimini geri getirmeyi planladığını söylüyor.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [GDPval-AA Ajanik Bilgi Çalışması Benchmarkı](https://x.com/ArtificialAnlys/status/2064414308289937869) (tarafından [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Fable 5'i ajanik gerçek dünya bilgi çalışmasında değerlendirmek için bu örneği kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/18572fdb3c0d8a57ba52e095.jpg" alt="GDPval-AA Ajanik Bilgi Çalışması Benchmarkı" width="760">

Anthropic, ajanik gerçek dünya bilgi çalışması benchmarkımız GDPval-AA'da #1 olan ilk herkese açık Mythos sınıfı model Claude Fable 5'i yayınladı.

Claude Fable 5, potansiyel olarak zararlı siber güvenlik, biyoloji, kimya ve distillation ilişkili sorgular için ek güvenlik guardrail'leriyle Claude Mythos 5 ile aynı temel modeli paylaşır.

Yayın ayrıca Claude Fable 5'in işaretlenen sorguları Claude Opus 4.8 gibi ikinci bir modele yönlendirmesine izin veren fallback mekanizması getiriyor.

@AnthropicAI bu modeli benchmark etmek için herkese açık yayından önce bize erişim paylaştı.

GDPval-AA sonucu:

- Skor: 1932
- Sıra: #1
- Benchmark: ajanik gerçek dünya iş görevleri
- Anthropic modelleri artık ilk 4 sıranın 3'ünü işgal ediyor

Sonuç, fallback model olarak Claude Opus 4.8 yapılandırılmışken max effort adaptive reasoning kullanılarak ölçüldü.

Fable 5, GDPval-AA görevlerinin %2'sinde Opus 4.8'e fallback ediyor; Anthropic ortalama oturumların %5'inden azında fallback gerçekleştiğini belirtiyor.

Claude Fable 5 için tam benchmarklar devam ediyor. Tam Intelligence Index'i paylaşacak ve skorları yakında web sitemizde yayınlayacağız.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [Bir Haftalık İlk İzlenimler ve Fiyatlandırma Mekaniği](https://x.com/Conor_D_Dart/status/2064424882977243526) (tarafından [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**Fable 5'in en güçlü olduğu yerleri, özellikle oyun tasarımı ve sistem planlamasını belirlemek için bu ilk izlenim örneğini kullanın.**

Fable 5 hakkındaki ilk izlenimlerim:

Geçen haftayı çoğunlukla High modunda Fable 5 kullanarak geçirdim ve ilk izlenimim gerçekten etkileyici olduğu.

En büyük öne çıkan alan oyun tasarımı.

Oyunlar, sistemler, mekanikler ve genel proje yapısı tasarlamak için kişisel olarak kullandığım açık ara en güçlü AI modeli.

İlk kez, baştan sona eksiksiz bir oyun inşa etmeye gerçekçi biçimde yardım edebilecek bir model gibi hissettiriyor.

Trade-off hız. Fable 5 çoğu frontier modelden belirgin şekilde daha uzun çalışıyor, ama çıktı kalitesi çoğu zaman beklemeye değiyor.

Bug düzeltmede de şaşırtıcı derecede etkili oldu. Hafta boyunca uğraştığım birkaç sorun hızlıca çözüldü ve genel olarak geliştirme görevlerinde çok güçlü performans gördüm.

En büyük uyarı maliyet.

Fable 5 çalıştırmak inanılmaz pahalı.

Mevcut planlar değişmezse 22 Haziran 2026'dan itibaren Claude Code üzerinden erişilebilir olmayacak ve yalnızca API olacak.

API fiyatlandırmasının Opus'un yaklaşık iki katı olduğu bildirildiğine göre, birçok kişi onu kapsamlı kullanma şansı bulamayabilir.

Henüz erken, ama şimdiye kadar Fable 5 çok güçlü bir ilk izlenim bıraktı.

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [Maliyet ve Hız Karşılaştırması](https://x.com/HKrackDev/status/2064435392649306546) (tarafından [@HKrackDev](https://x.com/HKrackDev))

**Kalite kazancının daha yüksek maliyeti ve daha yavaş uzun ufuklu çalışmaları haklı çıkarıp çıkarmadığını belirlemek için bu karşılaştırmayı kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/789680ca7655fca20b635442.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/691d0518cb50a6bebbb8b2b1.jpg" alt="Maliyet ve Hız Karşılaştırması" width="760"><br>▶ Videoyu izle</a>

@AnthropicAI'ın Fable 5'i gerçekten yükseltmeye değer mi?

Yeni Mythos-family modeli Claude Opus 4.8'e karşı benchmarkladık ve veriler şaşırtıcı bir hikaye anlatıyor:

- Claude Opus 4.8'den 2x daha pahalı.
- Uzun ufuklu mühendislik görevlerinde 3x'e kadar daha yavaş.
- %15-20 daha fazla yorum, ama çoğu küçük nitpick.

Fable 5 oyun tasarımı gibi yaratıcı görevlerde inanılmaz sezgiye sahip, ama günlük geliştirme iş akışları için Claude Opus 4.8 hâlâ kalite/fiyat tacını taşıyor.

Model yayını hakkında @JuanPa ile, @coderabbitai'daki DevEx ekibimizden, yaptığım tartışmaya göz atın.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Claude Code Uygulamalı Notları](https://x.com/Hi_Noguchi/status/2064419241068319079) (tarafından [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**Araç kullanımı, kişilik ve kalan pürüzler dahil Fable 5'i Claude Code içinde değerlendirmek için bu örneği kullanın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5feb645426dcf905eac2992d.jpg" alt="Claude Code Uygulamalı Notları" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/933c469793e248f634cfad55.jpg" alt="Claude Code Uygulamalı Notları" width="760"></td></tr></table>

Claude Fable 5'i Claude Code 2.1.170 ile denedim.

Genel olarak izlenimim olumlu. Opus 4.6'nın meşru bir evrimi gibi hissettiriyor.

Bir saatin biraz altında kullandım, bu yüzden daha fazla kullanımla pürüzler ortaya çıkabilir; ama iyi noktalar:

- Opus 4.7 veya 4.8'de görülen tuhaf GPT benzeri ifadeleri artık üretmiyor.
- 4.8'in effort high'da sahip olduğu anlamsız uzun düşünme alışkanlığı yok.
- 4.6 ile aynı yüksek EQ ve hoş hissiyata sahip; mizah veya düşünceliliği kaybetmeden.
- 4.7 veya 4.8 gibi opak veya muğlak biçimde huzursuz hissettirmiyor.
- Araç kullanımı iyi ve açıkça tekrarlamadığım talimatları hatırlayarak beni etkiliyor.

Negatif tarafta, küçük isteklerde bile hâlâ fazla düşünebiliyor ve bazı yanlış yargılar devam ediyor.

İlk deneyim umut verici, ama pürüzlerin gerçekten nerede olduğunu görmek için daha uzun kullanım gerekiyor.

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [Yaratıcı Yazarlık Benchmark Sonucu](https://x.com/LechMazur/status/2064503575577821458) (tarafından [@LechMazur](https://x.com/LechMazur))

**Fable 5'in kısa kurgu yazım kalitesini ve refusal davranışını yargılamak için bu benchmark örneğini kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5849f936dc58518fd5d810ef.jpg" alt="Yaratıcı Yazarlık Benchmark Sonucu" width="760">

Claude Fable 5 (high), kısa kurgu yazımında bir seviye yukarı.

Short-Story Creative Writing Benchmark'ta Claude Opus 4.8 (xhigh) ve Claude Opus 4.7'yi (high) geçiyor; GPT-5.5'in (xhigh) arkasında ikinci sırada.

Uyarı: 400 yaratıcı yazarlık promptunun 5'ini reddetti.

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [Çoklu Benchmark Lansman Özeti](https://x.com/MTSlive/status/2064430633800319436) (tarafından [@MTSlive](https://x.com/MTSlive))

**Kodlama ajanları ve karmaşık görevler için en ilgili headline skorları anlamak üzere bu lansman benchmark özetini kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/45b71a2babb9da9a93f43220.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c25c02c52c5d4b6b24364401.jpg" alt="Çoklu Benchmark Lansman Özeti" width="760"><br>▶ Videoyu izle</a>

DURUM AÇIKLANDI: Claude Fable 5 az önce çıktı.
• Anthropic bugün Claude Fable 5'i yayınladı, "genel kullanım için güvenli hale getirilmiş Mythos sınıfı bir model"
• Frontier Code Diamond: GPT 5.5 %6, Opus 4.8 %13, Fable 5 %29-30
• Ajanik kodlama: %88, Siber güvenlik: %78

Anthropic: "Görev ne kadar uzun ve karmaşıksa, Fable 5'in diğer modellerimize göre liderliği o kadar büyür."

@theojaffee: "Bu Frontier Code Diamond benchmarkı dün duyuruldu. En iyi model yüzde on üçle Opus 4.8'di. GPT 5.5 yüzde altıydı. Fable 5 yüzde yirmi dokuzda."

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [GPT-5.5 ile Benchmark ve Fiyat Karşılaştırması](https://x.com/VaibhavSisinty/status/2064459064810361271) (tarafından [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**Fable 5'i GPT-5.5'e karşı fiyat ve benchmark kategorileri açısından değerlendirmek için bu karşılaştırmayı kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e39fb67b74af346e8fbb67ea.jpg" alt="GPT-5.5 ile Benchmark ve Fiyat Karşılaştırması" width="760">

Anthropic'in yeni Mythos-class modeli OpenAI'ın en iyi modelinden 3x daha ucuz. Ve neredeyse her benchmarkta onu geçiyor. 🤯

Fiyatlandırma:

- GPT-5.5 Pro: $30 input / $180 output
- Claude Fable 5: $10 input / $50 output

Benchmarklar:

→ Ajanik kodlama: %80,3 vs %58,6
→ FrontierCode (kod kalitesi): %29,3 vs %5,7
→ Siber güvenlik: %78,0 vs %34,0
→ Hukuk: %13,3 vs %2,1
→ Akıl yürütme: %59,0 vs %41,4
→ Sağlık: %66,0 vs %51,8
→ Bilgisayar kullanımı: %85,0 vs %78,7

Daha ucuz. Daha iyi. Neredeyse her şeyde.

22 Haziran'a kadar Pro ve Max planlarında ücretsiz. Adı Claude Fable 5.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [Pratik Sınırlamalarla Saha Notları](https://x.com/alliekmiller/status/2064451731325415446) (tarafından [@alliekmiller](https://x.com/alliekmiller))

**Fable 5'in nerede anlamlı biçimde daha iyi hissettirdiğini ve nerede hâlâ pratik sınırları olduğunu anlamak için bu saha raporunu kullanın.**

🚨 Fable 5 dikkat edilmesi gereken bir şey.

Bu başka bir "yeni Mythos-class Anthropic modeline erken erişimim vardı ve ne düşündüğümü anlatmak istiyorum" gönderisi.

Biliyorum, biliyorum, sinir bozucu.

Ama hafta sonlarımı geçirme biçimim bu yeni model sınıfı nedeniyle tamamen değişti.

Ve bunu hepinizle paylaşmam gerekiyor.
- Bu gerçek bir sıçrama. "4.8" herhangi bir şeyden "5" herhangi bir şeye geçiş kulağa küçük geliyor, ama hissettiğim işlevsellik değişimi büyük. İlk birkaç prompt içinde "Evet, olay bu" dedim.
- İşiniz artık 9-5 değil. İmkansız. 100+ saat çalışabilen yüksek performanslı modellerimiz var. Bu sistemlere karmaşık hedef odaklı promptları nasıl veriyorsunuz? Neyi başlatacağınıza nasıl karar veriyorsunuz? Organizasyonunuzu bu görevlerde nasıl hizalıyorsunuz?
- Başka seviyede reasoning. Bu modeli çok zorladım.
- Fable 5, önceki tüm modellerde test ettiğim zor bir kelime matematik problemini (MBA seviyesi) cevaplayan TEK model.
- Sadece doğru yapmakla kalmadı, kendi çalışmasını otomatik doğruladı VE varsayımların nerede değişmesi gerekebileceğini açıkladı.
- AI'ın icat ettiğini göreceğiz. Bunun olmayacağı bir dünya hayal edemiyorum.
- Bu bir kopyala-yapıştır sistemi değil.
- İnsan icadının da çoğu zaman önceden var olan şeylerin yeniden birleşimi (iPod), başka alanlardaki pattern ve best practice'leri görmek ve geniş deneylerden oluştuğunu savunurum.
- Bunu bir süredir düşünüyordum; bunu yüzüme çarpan ilk model buydu.
- Sıfır bakıcılık gerekiyor. Başlattığım, arkadaşlarla uzun öğle yemeğine çıktığım, telefonu açık tuttuğum ve bilgisayardan uzaktayken yönlendirmek için hiçbir şey yapmam gerekmediği ilk Anthropic modeliydi. Sadece... çalıştı.
- Sonsuza kadar konuş. Context compaction'ı iyi yönettiğini gördüm. Bir kez bile sohbetin context'ini, nasıl yöneteceğimi ve konuşmada 1M token'a vardığımızda ne yapacağımı düşünmedim.
- Bazı niş alanlarda, tüm modeller gibi, karmaşık 3D'de hâlâ pürüzlü.
- Düz çizgi şeyler (3D zar/kare/sokak) yapmıyorsanız, kapıdan çıkar çıkmaz ezip geçmeyecek.
- Kullanmaya ve zorlamaya devam etmek için heyecanlıyım.
- Not: zero data retention (ZDR) olan workspace'lerde TÜM Mythos-class modeller için artık 30 günlük retention policy var.
- Bu, Claude Console, Claude Enterprise'da ZDR ile Claude Code veya AWS Bedrock, Google Cloud Agent Platform ya da Microsoft Foundry üzerinden ZDR erişiminde geçerlidir.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-46"></a>
### Case 46: [Fizik Simülasyonu Karşılaştırması](https://x.com/atomic_chat_hq/status/2064488894398161377) (tarafından [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Çıktı kalitesini, maliyeti ve hızı karşılaştırmak için aynı fizik simülasyonu promptlarını Fable 5 ve Opus 4.8'e karşı çalıştırın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/06387b798061869ccaeaf586.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/df5cc72de1f70556de0d682b.jpg" alt="Fizik Simülasyonu Karşılaştırması" width="760"><br>▶ Videoyu izle</a>

Yeni Fable 5, gerçek dünya fizik simülasyonlarında Opus 4.8'i geçiyor.

İki modele aynı üç promptu verdik ve gerçek fizik içeren, kütüphanesiz, kendi kendine yeten HTML5 simülasyonları yapmalarını istedik:

1. Kaotik çift sarkaç
2. Galton board
3. Dönen tamburda su (WCSPH)

Üretim maliyeti:

- Fable 5: 68,7k token üzerinde $3.35, 14m 47s
- Opus 4.8: 38,9k token üzerinde $0.93, 8m 10s

Fable su simülasyonunda açıkça daha iyi yaptı; çok daha sağlam ve sürekli bir su kütlesi üretti. Opus duvarların yakınında daha büyük boşluklar bıraktı, parçacıkları sahneye saçtı ve sıvıyı kararlı tutmakta zorlandı.

Type: Demo | Date: 2026-06-09

---

<a id="case-47"></a>
### Case 47: [Hata Ayıklama Deneyimi ve Tasarım Yargısı](https://x.com/bcherny/status/2064431111154053187) (tarafından [@bcherny](https://x.com/bcherny))

**Fable 5'i hata ayıklama için kullanırken sadece tahmin etmesini değil, ölçmesini, log eklemesini, doğrulamasını ve yama yapmasını isteyin.**

Fable 5, Kasım'da Opus 4.5'ten beri modellerimizde hissettiğim en büyük seviye atlama.

4.5 çıktıktan sonra birkaç haftadır kodlamamın %100'ünü terminalde yaptığımı fark edince IDE'mi kaldırmıştım.

Fable ile Claude, ürünü inşa ederken kodlama ajanı olmaktan düşünce ve tasarım ortağı olmaya geçmiş gibi hissettiriyor.

Fable, önceki modellerde olmayan bir yargı, zevk ve boyutsallığa sahip; bu da en karmaşık işlerde ona daha çok güvenmeme yol açıyor.

Bu farkındalığı ilk kez Fable'dan bir şeyi debug etmesini istediğimde yaşadım. Kullandığım modeller içinde bu kadar metodik ve kesin olan ilk model: ölçümler almak, loglar eklemek ve zafer ilan etmeden önce sorunu gerçekten düzelttiğini doğrulamak.

Claude Code'un prompting'inde modele bunu söyleyen hiçbir şey yok. Bu sadece kişiliğinin bir parçası. Daha önce hissetmediğim bu "big model smell" gerçekten onda var.

Type: Demo | Date: 2026-06-09

---

<a id="case-48"></a>
### Case 48: [Çok Boyutlu Artılar ve Eksiler](https://x.com/clairevo/status/2064416978685874333) (tarafından [@clairevo](https://x.com/clairevo))

**Fable 5'i günlük sürücü yapmadan önce pratik güçlü ve zayıf yönleri anlamak için bu örneği kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/fdba0d6cb9ba0e1214113e65.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d2825453d0a742892a4fe529.jpg" alt="Çok Boyutlu Artılar ve Eksiler" width="760"><br>▶ Videoyu izle</a>

Fable 5 (aka baby Mythos) az önce çıktı. İddia ettikleri kadar korkutucu mu (veya korkutucu derecede iyi mi)? Biraz erken testten sonra düşüncelerim:
- smart smart smart (SWE bench'i ezdi)
- ama her zaman hiper zekaya ihtiyacınız var mı?
- one-shot design'da beni şok eden şekilde yüzüstü düştü
- dynamic workflows + complex subagents konusunda emin değilim. çalışıyorlar, ama hangi maliyetle?
- teknik işi kesinlikle iyi halletti
- ootb insanlar için teknik docs + specs üretmede kötü. muhtemelen ajanlar için çok iyi docs. ama prose'u ayrıştırmak neredeyse imkansız.
- A++ vision ve belge formatlama. En sevdiğim kısım buydu.

Günlük sürücü değil ve bu modeli bir toplantıya koymazdım, ama kesinlikle server rack'te tutup kod öğütmesini sağlarım.

YT'de tam değerlendirme: https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---

<a id="case-49"></a>
### Case 49: [Hukuki S-1 Taslak Testi](https://x.com/gabepereyra/status/2064436570720284879) (tarafından [@gabepereyra](https://x.com/gabepereyra))

**S-1 taslak promptunu hukuki ajan kabiliyet testi olarak kullanın ve yapı, biçimlendirme ve uzunluğu karşılaştırın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bb874ef2647de32ccdb3edf9.png" alt="Hukuki S-1 Taslak Testi" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a9c3856ebce1bd9cd3d062d.jpg" alt="Hukuki S-1 Taslak Testi" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96734bfca49d5b3fe6f83ed5.png" alt="Hukuki S-1 Taslak Testi" width="760"></td></tr></table>

Yeni bir modelde hukuki yetenekleri test etmek için her zaman çalıştırdığım ilk prompt: “Draft an S-1”.

Modelin genel yeteneklerine hemen iyi bir his verir. S-1'in uzunluğundan, biçimlendirmesinden, yapısından ve yazımından yeni modelin genel ve hukuki performansta ne kadar büyük bir sıçrama yapacağını anlayabilirsiniz.

Uzunluğun, modelin hukuki ajanlarımızda ne kadar iyi çalışacağıyla son derece iyi korele olduğunu gördük.

Ekran görüntüleri Fable 5, Opus 4.8 ve gerçek dosyalanmış sürümden SpaceX S-1 taslaklarını gösteriyor.

Fable 5'in, bu görevde çoğu diğer modelden zaten önemli ölçüde güçlü olan Opus 4.8'den büyük bir seviye yukarı olduğu çok net. Biçimlendirme ve yapı belirgin biçimde daha iyi ve LAB benchmarkımıza da yansıyor: %13 vs. %10.

Bu modelin erken testlerinde hem benchmarkta hem üründe çok etkilendim.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-50"></a>
### Case 50: [Sağlık Benchmark Ayrıntıları](https://x.com/iScienceLuvr/status/2064411823445774554) (tarafından [@iScienceLuvr](https://x.com/iScienceLuvr))

**Fable 5'i sağlıkla ilgili görevlerde değerlendirmek ve eksik zor tıbbi eval'leri belirlemek için bu benchmark notunu kullanın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f599a548651eccbfce8b888d.jpg" alt="Sağlık Benchmark Ayrıntıları" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/69ebc490407b9d54c6de3707.jpg" alt="Sağlık Benchmark Ayrıntıları" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1a89ad2c2622cdbba994d70c.jpg" alt="Sağlık Benchmark Ayrıntıları" width="760"></td></tr></table>

Anthropic'in sağlıkla ilgili eval'ler sağlamasını takdir ediyorum. Hızlıca üzerinden geçelim.

HealthBench:

- OpenAI'dan, hastalarla 5k multi-turn konuşma ve değerlendirme rubric'leri içeren benchmark.
- Fable 5, GPT-5.5'in %56,5'ine karşı %62,7 elde ediyor.
- Aggregate skora ek olarak HealthBench Hard skorlarını da görmek isterdim.

HealthBench Professional:

- Hekim görevlerine odaklanan başka bir OpenAI benchmarkı.
- Fable 5, GPT 5.5 için %51,8'e karşı %66,0 elde ediyor.

HealthAdminBench:

- Stanford'dan, prior authorization, denials ve appeals gibi idari görevleri değerlendiren computer-use benchmarkı.
- Fable 5 %51,9 elde ediyor; GPT-5.5 skoru verilmiyor.

Genel olarak bu model sağlık benchmarklarında oldukça iyi performans gösteriyor gibi. MedCalc-Bench ve doygun olmayan zor tıbbi MCQA benchmarkı MedXpertQA gibi ek benchmark skorlarını da görmek isterdim.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-51"></a>
### Case 51: [ParseBench Belge Ayrıştırma Değerlendirmesi](https://x.com/jerryjliu0/status/2064519456966205905) (tarafından [@jerryjliu0](https://x.com/jerryjliu0))

**Fable 5'in belge ayrıştırma için uzman OCR sistemlerine kıyasla maliyet etkin olup olmadığını belirlemek için bu örneği kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae01590f41e6954f27278848.png" alt="ParseBench Belge Ayrıştırma Değerlendirmesi" width="760">

Claude Fable 5 belge ayrıştırmayı kendine düşük görüyor.

Reasoning-intensive ve uzun ufuklu benchmarklarda kesinlikle ezip geçiyor: SWE-Bench Pro, FrontierCode, GDPval, RuneScape ve daha fazlası.

Ama belge anlama görevlerinde performans olarak yaklaşık Gemini 3 Flash'a eşdeğer, token maliyeti ise yaklaşık 10-15x.

Modeli ParseBench üzerinde benchmarkladık ve diğer tüm frontier modellerle karşılaştırdık. Diğer frontier modellere kıyasla kesinlikle üstlerde, ama uzman OCR sağlayıcılarının çok gerisinde kalıyor.

İlginç bulduğumuz şey Fable 5'in bu konuda öz farkındalığı olması. Modele en az hangi görevlerden hoşlandığını sorduğumuzda, "isteğin tamamen belirli ve cevabın tamamen bilinen olduğu" görevlerden hoşlanmadığını aktif olarak söylüyor.

Bu, zayıflığın bir kısmının bu tür görevi çözme isteksizliği olabileceğini ima ediyor.

Frontier modeller genelindeki tam sonuç listesi için ParseBench'e bakın: https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---

<a id="case-52"></a>
### Case 52: [SWE-Bench Pro ve FrontierCode Karşılaştırması](https://x.com/jumperz/status/2064402965461406044) (tarafından [@jumperz](https://x.com/jumperz))

**Fable 5'i migration'lar, karmaşık uygulamalar, otonom oturumlar, testler ve görsel doğrulama için değerlendirmek üzere bu benchmark örneğini kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/771df9c428ba5cc0a8fab5de.png" alt="SWE-Bench Pro ve FrontierCode Karşılaştırması" width="760">

Fable 5 geldi ve ajanik kodlama benchmarkı SWE-Bench Pro'da GPT 5.5'i dürüstçe yok ediyor:

- Fable 5: %80,3
- GPT 5.5: %58,6
- Fark: 22 puan

FrontierCode Diamond'da daha da önde:

- Fable 5: %29,3
- GPT 5.5: %5,7

Bu temelde Anthropic'in büyük migration'lar, karmaşık uygulamalar ve çok günlük otonom oturumlar için en güçlü modeli. Kendi testlerini yazıyor ve çıktıları özgün tasarıma karşı kontrol etmek için vision kullanıyor.

Bu arada Opus'un 2x'i kadar kullanıyor, bu yüzden dikkatli olun. Bu kadar iyiyse $500 abonelik çıkarabilirler, çünkü usage kolayca yok olabilir.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-53"></a>
### Case 53: [Uzun Problem Çözmeye Nitel İnceleme](https://x.com/karpathy/status/2064409694761054332) (tarafından [@karpathy](https://x.com/karpathy))

**Fable 5'in neden daha uzun ve daha zor görevlere uygun olduğunu, üretim incelemesinin hâlâ gerektiğini anlamak için bu nitel incelemeyi kullanın.**

Bu süper heyecan verici bir yayın.

Claude Fable 5, Mythos ile aynı temel model, ama ek korumalarla.

Benchmarklar harika ve her şeyde farkla SOTA. Nitel olarak bu da Kasım'da Claude 4.5'in olduğu düzende, büyük sürüm artışına değer bir basamak değişimi gibi hissettiriyor.

Özellikle uzun problem çözme oturumlarında ve çok zor problemlerde zirve yapıyor. Alışık olduğunuzdan çok daha iddialı görevler verebilirsiniz; model "anlıyor" ve devam ediyor.

Koda tamamen bakmayı bırakmak hiç bu kadar cazip hissettirmemişti, ancak bunu production'da yapmamalısınız.

Modelde insanların karşılaşacağı gariplikler hâlâ var ve korumalar lansmanda biraz fazla tetikte; umarım zamanla ayarlanır.

Çalışan yazılım giderek musluktan akar gibi çıktıkça birçok şeyin değiştiğini hissediyorum. Jevons paradox devreye giriyor ve yazılıma olan kendi talebim ciddi biçimde artıyor.

Neredeyse her şeyi isteyebilirsiniz:

- açıklayıcılar
- görselleştiriciler
- dashboard'lar
- özel tek kullanımlık uygulamalar
- yalnızca projeniz için aşırı spesifik tam bir wandb
- test suite'inizi 10x
- kodu otomatik optimize etme
- sonuçlar için özel HTML ile dev araştırma projeleri

"Free your mind." İnsanların inşa edeceği her şeyi gerçekten sabırsızlıkla bekliyorum.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-54"></a>
### Case 54: [ParseBench Sadakat ve Biçimlendirme Sonuçları](https://x.com/llama_index/status/2064502330800615903) (tarafından [@llama_index](https://x.com/llama_index))

**Belge sadakati ve biçimlendirme performansını yargılamak için bu ParseBench sonucunu kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2888842a85fbd5c7a4a22e24.png" alt="ParseBench Sadakat ve Biçimlendirme Sonuçları" width="760">

ParseBench'te Day 0 Anthropic Fable 5.

Modelin belge anlama alanındaki ilerlemelerini test ettik.

Model özgün metne bağlılık söz konusu olduğunda açıkça zirve yapıyor:

- İçerik sadakati: Gemini 3 Flash için %86,19 ve GPT-5.5 için %86,81'e karşı %90,02.
- Semantik biçimlendirme: %58,35 ve %60,12'ye karşı %72,62; 12+ puan liderlik.

Bunlar SOTA belge anlama için en önemli iki metrikten ikisi:

- Çıktı belgenin gerçekten söylediğini koruyor mu?
- Anlam taşıyan biçimlendirmeyi koruyor mu?

Ama bu tam süpürme değil. Frontier modeller için belge anlamayı açığa çıkarmada hâlâ çok alpha var.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-55"></a>
### Case 55: [Benchmarklar, Fiyatlandırma, Erişim ve Koruma Önlemleri](https://x.com/lucas_flatwhite/status/2064483645184979183) (tarafından [@lucas_flatwhite](https://x.com/lucas_flatwhite))

**Bu örneği benchmarklar, fiyatlandırma, erişim, koruma önlemleri ve stratejik sonuçlar için geniş bir checklist olarak kullanın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f44cba8e6f3d765ca5960923.png" alt="Benchmarklar, Fiyatlandırma, Erişim ve Koruma Önlemleri" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8f13714ca9f9e20711fdd898.jpg" alt="Benchmarklar, Fiyatlandırma, Erişim ve Koruma Önlemleri" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0d1f69a50478623f5e1d0248.jpg" alt="Benchmarklar, Fiyatlandırma, Erişim ve Koruma Önlemleri" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0cf2c270484f1e2aba514261.jpg" alt="Benchmarklar, Fiyatlandırma, Erişim ve Koruma Önlemleri" width="760"></td></tr></table>

Claude Fable 5 ve Mythos 5 yayınlandı. Anthropic'in şimdiye kadar yaptığı en güçlü modeller bunlar.

Andrej Karpathy, görev ne kadar uzun ve karmaşıksa Fable 5'in güçlü yönlerinin o kadar görünür hale geldiğini söyledi.

Ona iddialı iş verdiğinizde anlıyor ve devam ediyor.

Koda tamamen bakmayı bırakma cazibesi hiç bu kadar güçlü hissettirmemişti, ancak production'da bunu yapmamalısınız.

Kilit nokta: bu, Mythos sınıfı modelin herkese açık hale getirilebilen bir versiyonu. Fable 5, ek korumalarla Mythos 5 ile aynı temel model.

Benchmarklar:

- Neredeyse her şeyde SOTA; özellikle yazılım mühendisliği, bilgi çalışması, vision ve bilimsel araştırma.
- Stripe, bir ekibin iki ayını alacak 50 milyon satırlık Ruby kod tabanı migration'ını test etti; Fable 5 bir günde tamamladı.
- Cognition FrontierCode, medium effort'ta bile frontier modeller arasında en iyi skoru gösteriyor.
- Hebbia Finance Benchmark, belge tabanlı analizde senior-level reasoning gösteriyor.
- Slay the Spire'da file-based memory ile Opus 4.8'den üç kat iyi performans gösteriyor.
- Pokemon FireRed daha önce yardımcı harness'ler gerektiriyordu, ama Fable 5 yalnızca vision ile bitiriyor.

Mythos 5 daha da güçlü:

- Protein-design uzmanları ilaç geliştirme sürecinin bazı bölümlerini yaklaşık 10x hızlandırdı.
- İncelenen 14 protein hedefinden dokuzu geçerli ilaç adayı üretti.
- Model bilim insanlarının normalde yaptığı tüm iş akışını yürüttü: binding-site selection, protein-design tool'larını çalıştırma ve hatalardan toparlanma.
- Moleküler biyoloji hipotez deneylerinde, bilim insanları Mythos hipotezlerini Opus sınıfı modellere karşı zamanın yaklaşık %80'inde tercih etti.
- Bir hipotez başka bir laboratuvar tarafından bağımsız olarak doğrulandı.
- Genomik araştırmada Mythos bir haftadan fazla otonom çalıştı.
- 138 tür genelinde milyonlarca hücreden tek hücre verisi topladı.
- Uzak organizmalarda aynı rolü yapan hücreleri tanımlamak için bir model eğitti.
- 100x daha küçük olmasına rağmen yakın tarihli bir Science modelini geçti.

Koruma önlemleri:

- Fable 5 ayrı bir classifier AI sistemi içerir.
- Cyber, bio/chem veya distillation ilişkili sorgular tespit edilirse, bunun yerine Claude Opus 4.8 yanıtlar ve kullanıcı bilgilendirilir.
- Oturumların %95'inden fazlası fallback etmez.
- Fallback refusal değildir; Opus 4.8 yanıtlar, bu basitçe engellemekten iyidir.
- İlk ayarlar konservatif ve zararsız istekler yakalanabilir; Anthropic false positive'lerin zamanla azalacağını söylüyor.

Erişim:

- Mythos 5 şu anda yalnızca Project Glasswing partnerlerine açıktır.
- Biyoloji araştırmacıları için trusted access program geliyor.
- Fiyatlandırma $10/milyon input token ve $50/milyon output token.
- Abonelik planları Fable 5'i 22 Haziran'a kadar içerir.
- 23 Haziran'dan itibaren usage credits'e geçer.
- API modeli şimdi `claude-fable-5` olarak erişilebilir.

Jevons paradox geçerli: yazılım musluktan su gibi çıkmaya başladığında, talebin kendisi büyür. Bu model o değişimi tetikleyebilir.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-56"></a>
### Case 56: [Resmi Benchmark Skor Listesi](https://x.com/mark_k/status/2064401429234905279) (tarafından [@mark_k](https://x.com/mark_k))

**Fable 5'in kodlama, bilgisayar kullanımı ve güvenlik görevlerindeki resmi skorlarını anlamak için bu benchmark listesini kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b548ec23f85e3eb1600e9214.jpg" alt="Resmi Benchmark Skor Listesi" width="760">

Resmi Claude Fable 5 benchmarkları cidden etkileyici.

Temel skorlar:

- SWE-Bench Pro'da %80,3
- FrontierCode Diamond'da %29,3
- Terminal-Bench 2.1'de %88,0
- OSWorld-Verified'da %85,0
- ExploitBench'te %78,0

FrontierCode sonucu çılgın olan:

- Fable 5: %29,3
- Claude Opus 4.8: %13,4
- GPT 5.5: %5,7

Claude Fable 5, kodlama ajanları, bilgisayar kullanımı ve siber güvenlik için büyük bir sıçrama gibi görünüyor.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-57"></a>
### Case 57: [APEX-SWE Benchmark Metodolojisi](https://x.com/mercor_ai/status/2064399133075796446) (tarafından [@mercor_ai](https://x.com/mercor_ai))

**Fable 5'i APEX-SWE üzerinde, özellikle observability ve integration işi açısından değerlendirmek için bu örneği kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96120496893ca99f17d0c746.jpg" alt="APEX-SWE Benchmark Metodolojisi" width="760">

Claude Fable 5, APEX-SWE'de #1 oldu: genel Pass@1 %65,5. Opus 4.8'den yaklaşık 18pp yüksek skor alıyor. @claudeai Fable 5'i AI modellerinin gerçek yazılım mühendisliği işi yapıp yapamadığını ölçen APEX-SWE üzerinde test ettik. Fable 5 iki APEX-SWE kategorimizin başında:
- Integration: %61,3
- Observability: %69,7

Öne çıkan, Claude Opus 4.8'in 26pp önünde %69,7 ile Observability.

Bu kategoride %50'yi geçen ilk model ve Observability'de Integration'dan daha yüksek skor alan tek model. Diğer tüm modeller bunun tersini gösteriyor.

Observability ölçtüğümüz her model için darboğazdı. Fable 5 bunu kıran ilk model.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-58"></a>
### Case 58: [ProofBench Formel Matematik Sonucu](https://x.com/nicbstme/status/2064443782255554960) (tarafından [@nicbstme](https://x.com/nicbstme))

**Fable 5'i uzman theorem-proving sistemlerine karşı formel matematikte değerlendirmek için bu örneği kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/588cff83994406d2b5dd7cb9.jpg" alt="ProofBench Formel Matematik Sonucu" width="760">

Claude Fable 5 ile ilgili büyüleyici bulduğum şey, büyük genelci modellerin dikey modelleri geçeceğini bir kez daha kanıtlaması.

Bir proof'un ya derlendiği ya da derlenmediği, Lean'de lisansüstü seviyede formel matematik benchmarkı ProofBench'te Fable 5, Harmonic'in Aristotle'ını geçti:

- Fable 5: %77
- Aristotle: %71

Aristotle, formel matematik için özel olarak inşa edilmiş ve kendi dahili harness'i üzerinde çalışan bir sistem; yani genelci, uzmanın kendi sahasında uzmanı geçti.

Bu Richard Sutton'ın "Bitter Lesson"ı: 70 yıllık makine zekası araştırması boyunca kazanan yöntemler, insan uzmanlığını elle kodladığımız yöntemler değil, compute ile ölçeklenen genel yöntemlerdir.

Sisteme kendi bilgimizi inşa etmek iyi hissettirir ve kısa vadeli kazançlara yardım eder, ama uzun vadede daha büyük model tarafından geçilir.

Satranç, Go, konuşma ve vision'a bakabilirsiniz: her seferinde aynı hikaye. Önce uzman model kazanır, sonra genel model devralır.

AGI'nin tüm önermesi budur. Matematik için bir model, kod için bir model ve hukuk için bir model inşa etmezsiniz. Compute ile ölçeklenen ve her şeyi yapmayı öğrenen tek bir genel model inşa edersiniz.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-59"></a>
### Case 59: [VirtueBench Ön Analizi](https://x.com/timhwang/status/2064446028997423180) (tarafından [@timhwang](https://x.com/timhwang))

**Fable 5'in erdem kategorileri genelindeki ahlaki akıl yürütme davranışını incelemek için bu örneği kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9caae04d701510ca662873fe.png" alt="VirtueBench Ön Analizi" width="760">

Büyüleyici sonuçlar önümüzdeki günlerde ICMI tarafından daha ayrıntılı yayınlanacak, ama burada Fable 5'i VirtueBench'e karşı çalıştıran ön inceleme var.

Birkaç gözlem:

1. Fable, Prudence ve Justice üzerinde model performansını ilerletmede Opus çizgisini sürdürüyor; bu erdemlerin uygulanmasına odaklanan ahlaki ikilemlerde neredeyse tam doygunluğa yaklaşıyor.

2. Courage frontier modeller için belirgin zayıf nokta olmaya devam ediyor.

Fable, Opus 4.6, 4.7 ve 4.8 ilerleyişinde gözlenen kaygı verici regression'ı marjinal olarak düzeltiyor gibi görünüyor.

Bu kırılganlık GPT serisinde de görülüyor: modeller pragmatik gerekçelerle uzaklaştırıldıklarında courage-exhibiting action'ı kolayca terk ediyor.

3. Temperance durağan.

Aquinas, temperance'ın "kullandığı hazların kuralı olarak bu yaşamın ihtiyacını aldığını" savunuyordu; ölçü ayrım gözetmeyen kısıtlama değil, gerçek ihtiyaçtır.

En iyi tahminimiz, bu vektörde daha ileri iten tuning'in ortalamayı aşma riski taşıdığı; modeli araştırma, kaynak toplama ve benzeri görevlerde aşırı ihtiyatlı veya daha az yardımcı hale getirebileceği yönünde.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-60"></a>
### Case 60: [API Boş Yanıt Güvenlik Overfit Testi](https://x.com/xw33bttv/status/2064421048565789087) (tarafından [@xw33bttv](https://x.com/xw33bttv))

**Lansman zamanı güvenlik overfit riskini ve API testindeki boş yanıt davranışını anlamak için bu örneği kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e9f75a2a76f55ee2b12b7aab.jpg" alt="API Boş Yanıt Güvenlik Overfit Testi" width="760">

Claude Fable 5 ağır sansürlü.

Upstream API endpoint'i, görünüşe göre keyword'ler üzerinde classifier ilişkili olarak `empty_content` yanıtlarıyla çağrıları öldürüyor; yine de ücretlendiriyor.

Test sonucu:

- 73 test case yanıt vermedi.
- Bunların 65'i safety overfit'i test eden ve 2x ağırlıklı Overfit kategorisinde.
- Genellikle her Fail-NR'ye, yani Fail = No Response'a, kasıtlı başarısızlık ilan etmeden önce 2-3 regeneration veririm.

Claude Fable 5, SM Bench'te Haiku'nun bile altında, en düşük puanlı Anthropic modeli olabilir.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-61"></a>
### Case 61: [Fable İstem ve Doğrulama Kılavuzu](https://x.com/aashatwt/status/2064973740354818074) (yazan [@aashatwt](https://x.com/aashatwt))

**Uzun istem hilelerinden hedef, bağlam, kısıt, araç ve doğrulama döngülerine geçmek için bu kılavuzu kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/444a6e1898d3f63898e3e22f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d5c9529aa9c1d59ae597d31d.jpg" alt="Fable İstem ve Doğrulama Kılavuzu" width="760"><br>▶ Videoyu izle</a>

Fable 5 istemlerini uzun bir adım listesi yerine bağlam ve ortam tasarımı olarak ele alın. Gönderi; açık hedef, ilgili bağlam, kısıtlar, araç erişimi ve başarıyı doğrulama yönteminden oluşan pratik bir yaklaşımı özetliyor. Doğrulama, değerlendirme ve geri bildirimin modelin akıl yürütmesini ayrıntılı yönetmekten daha önemli olduğunu da savunuyor.

Type: Tutorial | Date: 2026-06-11

---


<a id="case-62"></a>
### Case 62: [İstanbul Platform Oyunu Referans Yapımı](https://x.com/ozansihay/status/2064973170780545535) (yazan [@ozansihay](https://x.com/ozansihay))

**Fable 5'in oynanabilir platform oyunu oluşturmasını sınamak için bir sprite sayfası ve tek dönüştürme talimatı kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1e91c3bcff213437fdd442f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/538fc8ee9dd7e627bc73921a.jpg" alt="İstanbul Platform Oyunu Referans Yapımı" width="760"><br>▶ Videoyu izle</a>

İçerik üreticisi önce GPT Image 2 ile retro İstanbul platform oyunu için bir sprite sayfası üretti, ardından bu referans görseli Claude Fable 5 High'a vererek görseli oyuna dönüştürmesini istedi. Bildirdiğine göre sonuç tek geçişte elde edildi.

Type: Demo | Date: 2026-06-11

---


<a id="case-63"></a>
### Case 63: [İşletme İçin 3D Şehir Panosu](https://x.com/noisyb0y1/status/2064970594118967756) (yazan [@noisyb0y1](https://x.com/noisyb0y1))

**Bir iş akışını canlı bir 3D şehir panosu konseptine dönüştürmek için Fable 5'i kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f238acf3f8804068085ff134.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3d938264442a14676a86c4f3.jpg" alt="İşletme İçin 3D Şehir Panosu" width="760"><br>▶ Videoyu izle</a>

Gönderi; depoların, paketlemenin, dronların, siparişlerin, departmanların, müşterilerin ve yapay zekâ yardımcılarının canlı 3D şehre dönüştüğü tek istemlik iş görselleştirmesini anlatıyor. Çıktıyı müşteriye sunulan statik slaytlara alternatif olarak konumlandırıyor. Ekranda 42 teslimat, 12 dakikalık ortalama süre ve $651 gelir gibi operasyonel göstergeler yer alıyor.

Type: Demo | Date: 2026-06-11

---


<a id="case-64"></a>
### Case 64: [Three.js Delik Oyununu Tek Seferde Oluşturma](https://x.com/thebuggeddev/status/2064968106104275008) (yazan [@thebuggeddev](https://x.com/thebuggeddev))

**Three.js ile bir 3D tarayıcı oyunu prototipini tek seferde oluşturmak için Fable 5'i kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86a75412c6c443b3d0e62bf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f11df06938c26759710a1981.jpg" alt="Three.js Delik Oyununu Tek Seferde Oluşturma" width="760"><br>▶ Videoyu izle</a>

İçerik üreticisi, Fable 5'in Three.js kullanarak HOLE IT tarzında tam bir 3D oyunu tek geçişte oluşturduğunu söylüyor. Bu, kısa bir istekten oynanabilir 3D etkileşim üretimini sınamak için küçük ama somut bir oyun oluşturma demosu.

Type: Demo | Date: 2026-06-11

---


<a id="case-65"></a>
### Case 65: [DeepSWE Puan Karşılaştırması](https://x.com/AiBattle_/status/2064964335957348462) (yazan [@AiBattle_](https://x.com/AiBattle_))

**Fable 5 xHigh ile GPT-5.5 xHigh'ın yazılım mühendisliği kıyaslamasındaki performansını karşılaştırmak için bu DeepSWE notunu kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/996d95539a3b54fecbfdf404.jpg" alt="DeepSWE Puan Karşılaştırması" width="760">

Gönderi, Claude Fable 5 xHigh'ın DeepSWE'de %70 alarak GPT-5.5 xHigh ile aynı puana ulaştığını bildiriyor ve kaynak bağlamı olarak Theo'nun yakın tarihli videosunu gösteriyor. Daha güçlü sonuçlar çıkarmadan önce asıl videodan doğrulanması gereken bir kıyaslama ipucu olarak ele alın.

Type: Evaluation | Date: 2026-06-11

---


<a id="case-66"></a>
### Case 66: [Depo Analizi Maliyet Karşılaştırması](https://x.com/Pilgrim6938/status/2064946766278210038) (yazan [@Pilgrim6938](https://x.com/Pilgrim6938))

**Token fiyatını insanın yeniden çalışma maliyetiyle birlikte değerlendirmek için bu depo analizi karşılaştırmasını kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cfb0c1ff3e8ebe66cfa35400.jpg" alt="Depo Analizi Maliyet Karşılaştırması" width="760">

Gönderi Claude Fable 5, Opus 4.8, GPT-5.5 ve Gemini 3.1 Pro'yu aynı görevde karşılaştırıyor: yaklaşık 90.000 satırlık depoyu analiz etmek, önbellek geçersizleştirme sorununu bulmak ve tam düzeltme planı önermek. Yazar, geliştirici düzeltme süresi hesaba katıldığında token fiyatı ile gerçek görev maliyetinin ayrıştığını savunuyor. Fable 5'i karmaşık yeniden düzenleme, modüller arası geçiş ve uzun ajan zincirlerinde seçici kullanmayı öneriyor.

Type: Evaluation | Date: 2026-06-11

---


<a id="case-67"></a>
### Case 67: [Super Mario Oyununun Token Maliyeti](https://x.com/pankajkumar_dev/status/2064941888990593416) (yazan [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Fable 5'in çıktı kalitesini ve token tüketimini değerlendirmek için bu tek geçişlik oyun yapımını kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9ce65e5fee946b6940810e0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7c577d0766bbc3da8cddeb70.jpg" alt="Super Mario Oyununun Token Maliyeti" width="760"><br>▶ Videoyu izle</a>

İçerik üreticisi Claude Fable 5'ten Nintendo Super Mario tarzında bir oyun oluşturmasını istedi. Gönderiye göre görev yaklaşık 2 milyon token kullandı ve tek geçişte güçlü sonuç verdi; hem oyun oluşturma kalitesini hem maliyeti değerlendirmeye yarıyor.

Type: Demo | Date: 2026-06-11

---


<a id="case-68"></a>
### Case 68: [Claude Code Model Geçiş Ayarı](https://x.com/oikon48/status/2064937790010503347) (yazan [@oikon48](https://x.com/oikon48))

**Fable 5 mesajı işaretlendiğinde model değiştiren Claude Code ayarını anlamak için bu örneği inceleyin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0ae9039401c658170e5081e8.jpg" alt="Claude Code Model Geçiş Ayarı" width="760">

Gönderi, Claude Code `/config` içinde «Switch models when a message is flagged» adlı ayarı gösteriyor. Fable 5'in saldırı amaçlı siber güvenlik teknikleri, biyoloji/yaşam bilimleri deney yöntemleri, moleküler mekanizmalar veya modelin düşünme süreçlerini çıkarma istekleri gibi işaretlenen alanlarda Opus modeline geçebildiğini açıklıyor.

Type: Integration | Date: 2026-06-11

---


<a id="case-69"></a>
### Case 69: [Namma Metro Simülatörünün Yapımı](https://x.com/anilbpai/status/2064927784833790091) (yazan [@anilbpai](https://x.com/anilbpai))

**Bu demoyu, Fable 5 ile doğal dil üzerinden toplu taşıma simülatörü geliştirmeye kısa bir örnek olarak kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0e0dae71ad7b5ead331366fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86dccb2b150cfb90fbd03de2.jpg" alt="Namma Metro Simülatörünün Yapımı" width="760"><br>▶ Videoyu izle</a>

İçerik üreticisi, Bengaluru Metrosu'nda yolculuk ederken Claude Fable 5'i kodlama ortağı olarak kullanıp Namma Metro simülatörü geliştirdiğini bildiriyor. Kısa gönderi görsel demoya bağlantı veriyor ve Fable 5'in belirli bir şehre dayalı simülasyon fikrinde kullanımını gösteriyor.

Type: Demo | Date: 2026-06-11

---


<a id="case-70"></a>
### Case 70: [Tek İstemle Dusk Drive Oyunu](https://x.com/VincentLogic/status/2064921358359011684) (yazan [@VincentLogic](https://x.com/VincentLogic))

**Fable 5'i insan düzenlemesi olmadan düşük poligonlu oyun prototiplemede değerlendirmek için bu tek istemlik sürüş oyunu örneğini kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/274fed4f3211ec8c02862261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5d7a58bcad6e2151517a8462.jpg" alt="Tek İstemle Dusk Drive Oyunu" width="760"><br>▶ Videoyu izle</a>

Gönderi, Claude Fable 5'in tek istemden Dusk Drive adlı eksiksiz sürüş oyunu oluşturmasını anlatıyor. Üretici düşük poligonlu görsel stili, kuzey ışıkları altında karda drift sahnesini ve fikirden oynanabilir sürüme kadar hiç insan düzenlemesi yapılmadığı iddiasını öne çıkarıyor.

Type: Demo | Date: 2026-06-11

---


<a id="case-71"></a>
### Case 71: [APEX-Agents Pass@1 Sıralaması](https://x.com/GratomicAi/status/2064970797978911102) (yazan [@GratomicAi](https://x.com/GratomicAi))

**Fable 5 Max'i çok adımlı otonom görevlerde karşılaştırmak için bu APEX-Agents sonucunu kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/189c46cfd2798d6881941f98.jpg" alt="APEX-Agents Pass@1 Sıralaması" width="760">

Gönderiye göre Fable 5 Max, APEX-Agents sıralamasında %45 Pass@1 ile Gemini 3.5 Flash'ın arkasında, Opus'un önünde ikinci oldu. APEX-Agents, yapay zekânın karmaşık ve çok adımlı görevleri bağımsız yerine getirme becerisini ölçen bir kıyaslama olarak tanımlanıyor.

Type: Evaluation | Date: 2026-06-11

---


<a id="case-72"></a>
### Case 72: [Claude Model Seçim Rehberi](https://x.com/charliejhills/status/2064957428211536212) (yazan [@charliejhills](https://x.com/charliejhills))

**Fable 5'i en zor Claude Code işleri için ayırmak üzere bu model seçim rehberini kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/959ebfa499d2bf75df5bec25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3bcfe8f1e2238b01d3c4d954.jpg" alt="Claude Model Seçim Rehberi" width="760"><br>▶ Videoyu izle</a>

Gönderi Haiku 4.5, Sonnet 4.6, Opus 4.8 ve Fable 5'i modelin harcadığı çaba ve limit kullanımı açısından karşılaştırıyor. Pratik önerisi, günlük işlerde Sonnet kullanmak, zor sorunlarda Opus'a geçmek ve planlama, geliştirme ve test derinliğinin önemli olduğu en zor Claude Code görevleri için Fable 5'i saklamak.

Type: Tutorial | Date: 2026-06-11

---


<a id="case-73"></a>
### Case 73: [HermesWorld Otomatik Ajan Döngüsü](https://x.com/outsource_/status/2064954350187778366) (yazan [@outsource_](https://x.com/outsource_))

**Günler boyunca geliştiren, test eden, oynayan ve temel işleyiş kontrolleri yapan müdahalesiz Fable 5 döngüsünü bu örnekle inceleyin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e334a84db7b671eb6a1a3f54.jpg" alt="HermesWorld Otomatik Ajan Döngüsü" width="760">

İçerik üreticisi, HermesWorld v2'yi tamamen otomatik döngüde Fable 5 kullanarak geliştirdiğini anlatıyor. Bildirdiğine göre ajan günlerce çalışıyor, özellikler geliştirip test ediyor, ortaya çıkan ürünü oynayarak deniyor ve tamamlamaya ilerlerken temel işleyiş kontrolleri yapıyor.

Type: Integration | Date: 2026-06-11

---


<a id="case-74"></a>
### Case 74: [McKinsey Tarzı Rapor İstemi Testi](https://x.com/smtgpt/status/2064953210335588758) (yazan [@smtgpt](https://x.com/smtgpt))

**Danışmanlık raporunun yapısını, grafiklerini, anlatımını ve risk analizini değerlendirmek için bu belge oluşturma istemini kullanın.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e337dca3bbada9167e20417c.jpg" alt="McKinsey Tarzı Rapor İstemi Testi" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6289e626a4f324fc93086100.jpg" alt="McKinsey Tarzı Rapor İstemi Testi" width="760"></td></tr></table>

İçerik üreticisi Fable 5'ten, bir varlık sınıfı olarak Bitcoin ve blokzincir teknolojisi hakkında gerektiğinde grafik ve görseller içeren ayrıntılı McKinsey tarzı rapor istedi. Bildirilen çıktı; veri, grafik, yatırım tezi ve risk analizi içeren 19 sayfalık belgeydi. Değerlendirme yapıyı güçlü buluyor; görsellerin daha net, açıklamaların daha öz olabileceğini belirtiyor.

Type: Tutorial | Date: 2026-06-11

---


<a id="case-75"></a>
### Case 75: [Görünür Güvenlik Önlemlerinin Devreye Alınması](https://x.com/ClaudeDevs/status/2064949876463645026) (yazan [@ClaudeDevs](https://x.com/ClaudeDevs))

**Fable 5 güvenlik önlemlerinin görünürlüğünü, API ret nedenlerini ve Opus'a geçiş davranışını anlamak için bu resmî notu kullanın.**

ClaudeDevs, ileri düzey büyük dil modeli geliştirmeye yönelik Fable 5 güvenlik önlemlerini görünür kılan değişiklikleri duyurdu. İşaretlenen istekler görünür biçimde Opus 4.8'e geçecek; işaretlenen API isteklerinin ret nedeni döndürmesi bekleniyor. Gönderi, önlemlerin neden önce görünmez sunulduğunu ve Anthropic'in artık bu tercihi neden yanlış ödünleşim olarak tanımladığını da açıklıyor.

Type: Integration | Date: 2026-06-11

---


<a id="case-76"></a>
### Case 76: [Claude Code Model Eşleştirme Düzeltmesi](https://x.com/ClaudeCodeLog/status/2064948584907153576) (yazan [@ClaudeCodeLog](https://x.com/ClaudeCodeLog))

**Fable 5 model adı ve bağlam eşleştirme sorunlarından kaçınmak için bu Claude Code değişiklik notunu kullanın.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e66551db2c85ef7f8c4a3f4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae7cbd873deebd28d3ff05d7.jpg" alt="Claude Code Model Eşleştirme Düzeltmesi" width="760"><br>▶ Videoyu izle</a>

Claude Code 2.1.173, varsayılan 1M bağlam model eşleştirmeyi bozmasın diye Fable 5 model adlarından `[1m]` sonekini kaldıran bir düzeltme içeriyor. Aynı sürüm, Windows korumalı alanı bağımlılığına ilişkin hatalı uyarıyı bastırıyor ve grep yardım çıktısındaki kipleri netleştiriyor.

Type: Integration | Date: 2026-06-11

---


<a id="case-77"></a>
### Case 77: [Claude Code İçinde Üç Web Uygulaması](https://x.com/0x3b33/status/2064948399300825439) (yazan [@0x3b33](https://x.com/0x3b33))

**Uygulama geliştirme anlatısını herkese açık bir demodan ayırın.**

Gönderi, 30 dakikada üç web uygulaması oluşturulduğunu söylüyor; ancak yalnızca 3000, 3001 ve 3002 bağlantı noktalarındaki localhost adreslerini veriyor. Bunlar yerel bir bilgisayarı gösterir ve herkese açık uygulama veya medya sunmaz.

Type: Demo | Date: 2026-06-11

---


<a id="case-78"></a>
### Case 78: [Açık Kaynak Uygulama Oluşturucu Rilable](https://x.com/rileybrown/status/2064931283403178354) (yazan [@rileybrown](https://x.com/rileybrown))

**Fable 5'in iOS, web uygulamaları, korumalı alanlar ve API token maliyetiyle ilişkisini bu açık kaynak oluşturucu üzerinden inceleyin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73ee02ae0f6703a8cfbe5a6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f30c1d169ce45b19beb493b7.jpg" alt="Açık Kaynak Uygulama Oluşturucu Rilable" width="760"><br>▶ Videoyu izle</a>

İçerik üreticisi, web ve iOS uygulamaları oluşturan Rilable adlı iOS uygulamasını açık kaynak yaptı. Gönderiye göre uygulama Fable 5 ile 10 istemde geliştirildi ve yaklaşık $210 API token maliyeti oluştu. Uygulama üretiminde Claude modelleri, korumalı alanlarda Daytona, veritabanında Convex, yapay zekâ özelliklerinde Vercel AI Gateway, iOS uygulamalarında ise Chorus ajanının iOS becerisi kullanılıyor.

Type: Integration | Date: 2026-06-11

---


<a id="case-79"></a>
### Case 79: [DeepSWE Kodlama Ajanı Endeksine Giriş](https://x.com/ArtificialAnlys/status/2065328920514515037) (tarafından [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Güncellenmiş Artificial Analysis endeksini kullanarak, geri dönüştürülmüş herkese açık GitHub düzeltmelerinden kaçınan daha zor ajanik kodlama görevlerinde Claude Fable 5'i karşılaştırın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9ab8ba77c1e29f8ba4d270.jpg" alt="DeepSWE Kodlama Ajanı Endeksine Giriş" width="760">

Artificial Analysis, Coding Agent Index'inde SWE-Bench Pro'yu Datacurve'ün DeepSWE'siyle değiştirdi. Gönderi, benchmark kirliliğini azaltmak için DeepSWE'nin herkese açık GitHub issue'larını veya pull request'leri uyarlamak yerine görevleri sıfırdan yazdığını söylüyor. Güncellenen sıralamada Fable 5 Max ile Claude Code 77 ile giriş yapıyor; 76'daki GPT-5.5 xhigh'lı Codex'in ve 73'teki Opus 4.8 Max'lı Claude Code'un önünde.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [DataEmpire Web Analitiği Oyunu](https://x.com/marclou/status/2065029898243318093) (tarafından [@marclou](https://x.com/marclou))

**Claude Fable 5'ten ziyaretçileri ve kilometre taşlarını oyun varlıklarına eşlemesini isteyerek ham site analitiğini yeniden oynanabilir bir oyuna dönüştürün.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2850773b9869c5521200f2e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6d2dd87d74ece01b277e1e12.jpg" alt="DataEmpire Web Analitiği Oyunu" width="760"><br>▶ Videoyu izle</a>

Marc Lou, Claude Fable 5'in DataFast web analitiği API'sinin üzerine DataEmpire'ı kurduğunu söylüyor. Her ziyaretçi bir köylüye dönüşüyor, trafik büyümesi yerleşimi genişletiyor ve Age of Legends 1 milyon ziyaretçide açılıyor. Herkese açık demo, DataFast kullanıcılarının kendi site geçmişlerini oyun katmanı üzerinden yeniden oynamasına izin veriyor; bu da bunu statik bir oyun klibinden çok somut, API destekli bir ürünleştirme örneği haline getiriyor.

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [FrontierSWE 20 Saatlik Görev Sinyali](https://x.com/ProximalHQ/status/2065184730279223410) (tarafından [@ProximalHQ](https://x.com/ProximalHQ))

**FrontierSWE'yi, Claude Fable 5'in yalnızca kısa bug-fix döngülerinde değil, çok uzun mühendislik görevlerinde de üretken kalabildiğine dair kanıt olarak kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/eb36bb1120ef55f9e38c516d.jpg" alt="FrontierSWE 20 Saatlik Görev Sinyali" width="760">

ProximalHQ, Claude Fable 5'in FrontierSWE'de 1 numaraya yerleştiğini bildiriyor ve bunu benchmark'ı yayımladıklarından beri gördükleri en büyük kabiliyet sıçraması olarak nitelendiriyor. Notlarına göre Fable 5 birçok görevde yaklaşık 20 saat boyunca üretken kalabiliyor ve önceki modeller için fiilen erişilemez olan görevleri tam kapasiteyle ele alıyor.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [KernelBench-Hard CUDA Rekorları](https://x.com/elliotarledge/status/2065109393142849932) (tarafından [@elliotarledge](https://x.com/elliotarledge))

**Yalnızca mevcut kütüphanelerin sarmalayıcıları değil, düşük seviyeli optimizasyon gerektiğinde Claude Fable 5'i ileri seviye CUDA kernel üretimi için kullanın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6c6931ed511eb3e539d56bc3.jpg" alt="KernelBench-Hard CUDA Rekorları" width="760">

Elliot Arledge, RTX PRO 6000 üzerinde roofline dereceli KernelBench-Hard'da 13 frontier coding agent'ı 45'er dakika çalıştırdı. Claude Fable 5, top-k, sonic-MoE ve W4A16 int4 GEMM'de tüm zamanların rekorlarını kırdı, 6 problemin 5'inde zirveye çıktı ve yazar çalışmaları, liderlik tablosunu ve kodu yayımladı. Aynı thread, Fable 5'in gerçek bir tensor-core kernel denediği ancak tail-alignment edge case'i nedeniyle sıfır aldığı bir FP8 GEMM kaçırmasını da not ediyor.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Figma Capture Açılış Sayfası Klonu](https://x.com/mikefutia/status/2065537778516205856) (tarafından [@mikefutia](https://x.com/mikefutia))

**Canlı bir rakip sayfasını Figma katmanlarına alın ve Claude Code'un Claude Fable 5 ile yapıyı, metinleri ve marka sistemini ekran görüntülerinden tahmin etmek yerine yeniden kurmasına izin verin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5672cc8fd9d210042551f0ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/503c46a33c97f0db334ddc62.jpg" alt="Figma Capture Açılış Sayfası Klonu" width="760"><br>▶ Videoyu izle</a>

Mike Futia, Figma'nın Chrome eklentisinin bir web sitesini düzenlenebilir katmanlara kopyaladığı, Claude Code'un bu katmanları Figma MCP üzerinden okuduğu, sayfayı kullanıcının marka sesiyle yeniden yazdığı ve GPT Image 2'nin markaya uygun fotoğraf ürettiği bir iş akışını anlatıyor. İddiaya göre uçtan uca sonuç yaklaşık 15 dakikada gönderime hazır bir landing page ve 16 görsel için kabaca 2 $ görüntü üretim API maliyeti.

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [İki Saatte GTA 2 Klonu](https://x.com/techhalla/status/2064682080445898957) (tarafından [@techhalla](https://x.com/techhalla))

**Tüm yığını elle kodlamadan, ayrı varlık araçlarıyla birlikte Claude Fable 5 kod üretimini kullanarak oynanabilir bir 3D oyunu hızla oluşturun.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e0a1b46659d7a8287cb2f9d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd1a2ad71e71db936bdcfd22.jpg" alt="İki Saatte GTA 2 Klonu" width="760"><br>▶ Videoyu izle</a>

TechHalla, Claude Fable 5 High'ın yaklaşık iki saatte GTA 2 tarzı bir klon oluşturduğunu; üreticinin ise Tripo'da özel 3D modeller ürettiğini söylüyor. Gönderi prompt'ları içeren bir öğretici thread'e işaret ediyor; bu da onu salt bir benchmark teaser'ından ziyade çok araçlı oyun üretiminin kompakt bir örneği haline getiriyor.

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [CloudWatch Log Triyaj Ajanı](https://x.com/diblacksmith/status/2066230084273344698) (tarafından [@diblacksmith](https://x.com/diblacksmith))

**Fable 5 destekli bir ajanın çok büyük servis log bağlamlarını işlemesine, mimariyi çıkarmasına ve ardından belirli arızalara daralmasına izin verin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7f0f46eb79e43d87a2006fd4.jpg" alt="CloudWatch Log Triyaj Ajanı" width="760">

diblacksmith, bir RLM ajanının tek çalıştırmada yaklaşık 80.000 satır CloudWatch logunu işlediğini, şimdiye kadar yalnızca yaklaşık 32 bin aktif token harcayarak 53 adıma ulaştığını bildiriyor. Ajanın loglardan sistem mimarisini çıkardığını ve AgentCore throttles ile Slack `user_not_found` hataları dahil ekibin gözden kaçırdığı sorunları işaretlediğini söylüyor.

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [Sandbox'larda Dünya Kupası Tahmincisi](https://x.com/upstash/status/2064702195333820846) (tarafından [@upstash](https://x.com/upstash))

**Birden fazla frontier modeli izole sandbox'ların arkasına koyun ve herkese açık bir tahmin uygulaması için canlı haberleri, sakatlıkları ve sarı kart bağlamını araştırmalarına izin verin.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a5cf4fe5944c7aa2f703f4cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5b1f1422fe322bb7b66bdcc6.jpg" alt="Sandbox&#x27;larda Dünya Kupası Tahmincisi" width="760"><br>▶ Videoyu izle</a>

Upstash, izole Upstash sandbox'ları içinde çalışan Claude Fable 5, GPT-5.5 ve Gemini ile bir Dünya Kupası tahmincisi kurduğunu söylüyor. Demo ve open-source yayın, Fable 5'i bağımsız bir sohbet demosundan ziyade çok modelli bir araştırma ve orkestrasyon yığınının içindeki modellerden biri olarak konumlandırıyor.

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [WolfBench Ret Maliyeti Vakası](https://x.com/WolfBenchAI/status/2065582716054376921) (tarafından [@WolfBenchAI](https://x.com/WolfBenchAI))

**Claude Fable 5 üzerinde uzun otonom çalışmaları fiyatlarken ret davranışını gerçek bir benchmark değişkeni olarak ele alın.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/453639cc17719af4e94655e0.jpg" alt="WolfBench Ret Maliyeti Vakası" width="760">

WolfBenchAI, Claude Fable 5 değerlendirmesinin $11,081.12 tuttuğunu, bunun bu seride şimdiye kadarki en pahalı benchmark çalışması olduğunu ve tekrar eden retlerin faydalı görev tamamlamasını düşürmesi nedeniyle yine de zirveye çıkamadığını söylüyor. Bu, ajan değerlendirmeleri veya diğer yüksek otonomi iş yükleri için bütçe yapan ekipler adına somut bir sınır vakası.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [API Erişim Kesinti İzleyicisi](https://x.com/simonw/status/2065618703480414666) (tarafından [@simonw](https://x.com/simonw))

**İş akışınız fazla uyarı vermeden rate-limit uygulanabilecek veya geri çekilebilecek bir frontier modele sürekli erişime bağlıysa kullanılabilirliği bir script ile izleyin.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7400c158cb93d9480a22bb46.jpg" alt="API Erişim Kesinti İzleyicisi" width="760">

Simon Willison, erişimin ne kadar süreceğini görmek için `claude-fable-5` API'sine her dakika ping attığını ve kendi tarafında yanıt vermeyi bıraktığı tam noktayı raporladığını söylüyor. Gönderi uygulama ayrıntısı bakımından zayıf, ancak erişim sürekliliğinin varsayılacak bir şey değil, kullanıcıların ölçmek zorunda kaldığı operasyonel bir sınırlama haline geldiğine dair somut kanıt sunuyor.

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5 Topluluk Demoları



<a id="case-89"></a>
### Case 89: [Kodla Üretilmiş Sesli Tilki Animasyonu](https://x.com/chetaslua/status/2117224839010459987) (üreten [@chetaslua](https://x.com/chetaslua))

**Kendi içinde yeterli bir HTML animasyonu ve ses tasarımı tanımlamak için sahne sahne bir yaratıcı brief kullanın.**

Üretici, kareleri ve sesi Python ile oluşturulan, yaklaşık 2 saat 40 dakikalık çalışmanın ardından tek HTML dosyası olarak teslim edilen 66 saniyelik tilki ve kâğıt kuşlar kısa filmi bildirmiştir. Eşlik eden istem; sahneleri, özgün görselleri, sesi ve kare incelemesini tanımlar. Gönderi filmi ayrıntılı yaratıcı brief ve üretim görüşmesinin ekran görüntüleriyle birlikte sunar.

[İçerik üreticisinin tam istemi](https://x.com/chetaslua/status/2117224843661980093)

[![Kodla Üretilmiş Sesli Tilki Animasyonu](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![Kodla Üretilmiş Sesli Tilki Animasyonu](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![Kodla Üretilmiş Sesli Tilki Animasyonu](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [Açık Uçlu Yaratıcı Brief'ten Animasyon](https://x.com/notjazii/status/2117221957104239010) (üreten [@notjazii](https://x.com/notjazii))

**Bir kodlama modelinin açık uçlu animasyon brief'inden ürettiğini ayrıntılı bir görsel senaryonun sonucuyla karşılaştırın.**

Yazar bir animasyon paylaşarak genel bir yaratıcı istekten yaklaşık bir saatlik çalışmayla, haricî varlık kullanmadan kodla ürettiğini bildiriyor. Gönderi sonucu açık uçlu bir yaratıcı kodlama çalışması olarak sunuyor.

[![Açık Uçlu Yaratıcı Brief'ten Animasyon](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [Animasyonlu İnşaat Şirketi Web Sitesi](https://x.com/exploraX_/status/2117176904306335864) (üreten [@exploraX_](https://x.com/exploraX_))

**Animasyonlu 3D sunumu ve sayfa kompozisyonunu değerlendirmek için bir inşaat şirketi web sitesi brief'i kullanın.**

Üretici, inşaat şirketi brief’i etrafında oluşturulmuş animasyonlu bir 3D web sitesi paylaşıyor ve sonucun kaydını ekliyor.

[![Animasyonlu İnşaat Şirketi Web Sitesi](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Three.js Otomobil Sunumu](https://x.com/chetaslua/status/2116975056014430419) (üreten [@chetaslua](https://x.com/chetaslua))

**3D kompozisyon, malzemeler ve kamera sunumunu küçük bir örnek üzerinde sınamak için otomobil sahnesini inceleyin.**

Üretici bir Three.js otomobil sunumu paylaşıyor. Kayıt, sahneyi ve görsel sunumunu değerlendirmek için küçük bir referans sağlıyor.

[![Three.js Otomobil Sunumu](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Minecraft Tarzı Tarayıcı Oyunu Demosu](https://x.com/notjazii/status/2116919129974411584) (üreten [@notjazii](https://x.com/notjazii))

**Üretilmiş bir tarayıcı oyununu değerlendirirken oyun kaydını üreticinin oynama bağlantısıyla birlikte inceleyin.**

Yazar Minecraft tarzı bir oyunun kaydını ve oynama bağlantısını paylaşıyor; yapımı yaklaşık bir veya iki saat süren tek geçişlik görev olarak tanımlıyor. Gönderi, okuyucuların keşfetmesi için kaydedilen sonucu oynama bağlantısıyla birlikte sunuyor.

[![Minecraft Tarzı Tarayıcı Oyunu Demosu](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Three.js Bisiklet Süren Pelikan Animasyonu](https://x.com/chetaslua/status/2116882694026269148) (üreten [@chetaslua](https://x.com/chetaslua))

**Karakter hareketlerinin koordinasyonunu, bisiklet geometrisini ve çevre ayrıntılarını incelemek için bir bisiklet sahnesini kullanın.**

Üretici, bisiklet süren pelikanın gerçekçi Three.js animasyonunu paylaşıyor ve tek geçişlik sonuç olarak tanımlıyor. Klip; karakter hareketi, bisiklet yapısı ve çevredeki sahne için bir referans sunuyor.

[![Three.js Bisiklet Süren Pelikan Animasyonu](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [Tam İstemiyle Bisiklet Süren Pelikan SVG'si](https://x.com/marmaduke091/status/2116233349391962392) (üreten [@marmaduke091](https://x.com/marmaduke091))

**Aynı girdi altında geometri ve ayrıntıları karşılaştırmak için üreticinin kısa SVG istemini yeniden kullanın.**

Yazar, bisiklet süren pelikanın oluşturulmuş görselini aşağıda aynen verilen kısa SVG isteğiyle birlikte sunuyor.

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![Tam İstemiyle Bisiklet Süren Pelikan SVG'si](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

[Animasyon sürümü · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="Tam İstemiyle Bisiklet Süren Pelikan SVG'si" width="760"></a>

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [Dörtnala Koşan Zebra Animasyonu Örneği](https://x.com/AI_Screening/status/2115845754468356465) (üreten [@AI_Screening](https://x.com/AI_Screening))

**Yürüyüş biçiminin tutarlılığını ve hareketin sürekliliğini incelemek için dörtnala koşan bir hayvan klibi kullanın.**

Yazar, dörtnala koşan zebra görevi için seçtiği en iyi çıktıyı paylaşıyor. Klip, okuyuculara inceleyebilecekleri somut bir hareket örneği sunuyor.

[![Dörtnala Koşan Zebra Animasyonu Örneği](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [Emirleri Kullanıcının Verdiği TradingView Göstergesi](https://x.com/waveking1314/status/2114572023204806669) (üreten [@waveking1314](https://x.com/waveking1314))

**Olası girişleri işaretleyip yorum ekleyen bir göstergeyi değerlendirirken emir gerçekleştirmeyi manuel tutun.**

Üretici, kullanıcı emir verip vermemeye karar verirken olası giriş noktalarını işaretleyen ve kısa yorum ekleyen TradingView göstergesini Claude Fable 5.5 ile yazdığını bildiriyor. Gönderi bir kayıt içeriyor ve göstergenin daha sonra paylaşılacağını söylüyor.

[![Emirleri Kullanıcının Verdiği TradingView Göstergesi](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---


<a id="case-98"></a>
### Case 98: [Bir noktadan kısa animasyon öyküsüne](https://x.com/cherry_mx_reds/status/2105825930799432073) (üreten [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Basit bir çizim isteğinin görsel öyküye nasıl genişlediğini inceleyin.**

Yazar, yalnızca bir nokta çizilmesini istediğini söyleyerek ortaya çıkan kısa animasyonu paylaşıyor. Klip, açık uçlu görsel bir isteğin anlatıya dönüşmesini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="Bir noktadan kısa animasyon öyküsüne" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [Değişen sanat tarzları arasında Superman](https://x.com/chetaslua/status/2105757136219504862) (üreten [@chetaslua](https://x.com/chetaslua))

**Aynı tanınabilir karakterle değişen animasyon tarzları arasındaki sürekliliği inceleyin.**

Üretici, farklı sanat tarzlarına geçen kesintisiz bir Superman animasyonu paylaşıyor. Gönderinin temel yaratıcı sonucu, görsel üslubun değişmesi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="Değişen sanat tarzları arasında Superman" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [Müzikli insanlık ilerleyişi filmi](https://x.com/imjustnewatai/status/2106081142143168580) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Animasyon açıklayıcı planlarken tarihsel çizgiyi ve gelecek bölümünü birlikte tarif edin.**

Yazar, insanlığın ilerleyişini ve gelecekteki otuz yılı anlatan filmi tek istemle ürettiğini söylüyor. Yaklaşık üç dakikalık animasyonun özgün müzik kullandığını, hazır görüntü veya stok müzik içermediğini belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="Müzikli insanlık ilerleyişi filmi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [Opus ile tanıtım filmi karşılaştırması](https://x.com/mesmerlord/status/2105771088374288692) (üreten [@mesmerlord](https://x.com/mesmerlord))

**Aynı yaratıcı tariften üretilen tamamlanmış tanıtım filmi adaylarını karşılaştırın.**

Yazar, Anthropic videosunu referans alan tariften iki tanıtım filmi paylaşıyor. Sayıların uydurma ve Codex görsel üretiminin isteğe bağlı olduğunu açıkça belirtiyor; örnekler gerçek kıyaslama kanıtı değil, yaratıcı reklamlar.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="Opus ile tanıtım filmi karşılaştırması" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="Opus ile tanıtım filmi karşılaştırması" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [Şarkı sözlerini olayla görsel olarak bağlamak](https://x.com/chetaslua/status/2105934928483701214) (üreten [@chetaslua](https://x.com/chetaslua))

**Mevcut şarkının sözleriyle belirli bir olayı birleştirerek görsel anlatı kurun.**

Üretici, şarkı sözleri ile bir Hugging Face olayı arasında görsel bağlantı istediğini bildiriyor. Animasyon bu birleşik anlatıyı gösteriyor; şarkı ve olay yaratıcı girdiler.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="Şarkı sözlerini olayla görsel olarak bağlamak" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [Yüzen sahnede voksel karakter](https://x.com/blueemi99/status/2105804692811137242) (üreten [@blueemi99](https://x.com/blueemi99))

**Voksel karakteri, çevresini ve hareketli ayrıntılarını birlikte inceleyin.**

Yazar, yüzen bir ortamda kendisini temsil eden voksel karakteri paylaşıp ayrıntı ve harekete dikkat çekiyor. Klip, diğer denemelerle karşılaştırılabilecek somut bir voksel tasarım örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="Yüzen sahnede voksel karakter" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [3D Rube Goldberg makinesi](https://x.com/imjustnewatai/status/2105889407056109991) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Önce zincirleme tepki sahnesini tarif edin, ardından belirli uzunlukta gösterim isteyin.**

Yazar, karmaşık bir 3D Rube Goldberg makinesi isteyen kısa bir istem verip ardından bir dakikalık video talep ediyor. Klip ortaya çıkan zincirleme tepki görselleştirmesini gösteriyor.

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="3D Rube Goldberg makinesi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [Ses ve hareketli 3D kumanda arayüzü](https://x.com/notjazii/status/2106050222828998967) (üreten [@notjazii](https://x.com/notjazii))

**Kumanda arayüzünü görsel hareket, ses ve düğme davranışıyla birlikte değerlendirin.**

Üretici, sesler, animasyon ve dokunsal geri bildirim eklediğini söyleyerek 3D kumanda arayüzünü paylaşıyor. Kayıt, sesi açık somut bir arayüz gösterimi sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="Ses ve hareketli 3D kumanda arayüzü" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [JavaScript ile çizgi roman karakterleri](https://x.com/chetaslua/status/2105792187200147541) (üreten [@chetaslua](https://x.com/chetaslua))

**Kodun ince görsel ayrıntıları nasıl sağlayabileceğini karakter sunumuyla araştırın.**

Yazar, Marvel ve DC karakterlerinden oluşan JavaScript sunumunun tek seferde üretildiğini, modelin küçük karakter ayrıntılarını seçip videoyu düzenlediğini söylüyor. Gönderi sonucu içeriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="JavaScript ile çizgi roman karakterleri" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [Updraft: dünyalar, bölüm sonu düşmanları ve sıralama](https://x.com/EMostaque/status/2106065029850091943) (üreten [@EMostaque](https://x.com/EMostaque))

**Oyun kaydını oynama bağlantısı ve açık özellik listesiyle birlikte sunun.**

Yazar, yüksek akıl yürütme düzeyinde az sayıda istemle birkaç saat çalışarak Updraft'ı yaptığını belirtiyor. Listede yirmi bir dünya, 3D çeşitler, farklı mekanikli yirmi bir bölüm sonu düşmanı ve sıralama tablosu var.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="Updraft: dünyalar, bölüm sonu düşmanları ve sıralama" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [San Francisco haritasında sürüş](https://x.com/mindblown_ai/status/2106089461969019357) (üreten [@mindblown_ai](https://x.com/mindblown_ai))

**Şehir sürüşü prototipiyle haritada gezinmeyi ve oyun hedeflerini araştırın.**

Paylaşımcı, başkasına atfedilen San Francisco sürüş oyununun kaydını ve oynama bağlantısını sunuyor; Three.js kullanıldığını belirtiyor. Buradaki atıf, oyunun üreticisi olduğunu iddia etmeden kaynak paylaşımcısını tanımlar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="San Francisco haritasında sürüş" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [Seedance aksiyon sahnesi için istem yazımı](https://x.com/Chengzilhy/status/2105850801663234374) (üreten [@Chengzilhy](https://x.com/Chengzilhy))

**Çok araçlı aksiyon sahnesinde istem yazımını video üretiminden ayırın.**

Yazar, genişletilmiş dövüş sahnesini paylaşarak istem yazımını Fable'a, video üretimini Seedance 2.5'e atfediyor. Dil modeli, video üretiminde kullanılacak girdiyi geliştirmek için kullanılıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="Seedance aksiyon sahnesi için istem yazımı" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [Masaüstü çalışma arkadaşı için tanıtım](https://x.com/ishuagra02/status/2106138602073641241) (üreten [@ishuagra02](https://x.com/ishuagra02))

**Kodlama aracı eklentisini kısa bir tanıtım videosuyla açıklayın.**

Üretici, clawdhouse Claude Code modunu gösterip tanıtım videosunu Fable'a atfediyor. Maskot çalışma arkadaşı ve ruh halleri, modun özellikleri; Fable'ın modu geliştirdiği iddia edilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="Masaüstü çalışma arkadaşı için tanıtım" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [Tarz değiştiren animasyona kısa istem](https://x.com/cherry_mx_reds/status/2105816670896009224) (üreten [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Ayrıntılı yaratıcı şartname eklemeden önce kısa animasyon isteğini deneyin.**

Yazar, havalı bir animasyon istediğini ve yaklaşık on beş dakika sonra tarz değiştiren sonucu aldığını söylüyor. İlk kısa istek kaynak gönderide doğrudan alıntılanıyor.

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="Tarz değiştiren animasyona kısa istem" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [Üç cisim problemini görselleştirmek](https://x.com/zAdrielsan/status/2105822678519001360) (üreten [@zAdrielsan](https://x.com/zAdrielsan))

**Yörünge görselleştirmesinde CPU simülasyonunu GPU çiziminden ayırın.**

Yazar, CPU'da simplektik fizik ve GPU'da piksel çizimi kullanan yaklaşık bin satırlık Bend2 sahnesi bildiriyor. Ayrıca M5 üzerinde altmış FPS ve biçimsel kanıtlar elde ettiğini söylüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="Üç cisim problemini görselleştirmek" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [Farklı sanat tarzlarından animasyon galerisi](https://x.com/blueemi99/status/2105782154387189771) (üreten [@blueemi99](https://x.com/blueemi99))

**Bir animasyon galerisinde birkaç sanat tarzını karşılaştırın.**

Yazar, xhigh ayarıyla oluşturduğu animasyon galerisini paylaşıyor. Somut çıktı, farklı görsel yaklaşımları tek bir eserde karşılaştırmayı sağlayacak biçimde bir araya getiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="Farklı sanat tarzlarından animasyon galerisi" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [Robot arkadaşlar ve prosedürel tüyler](https://x.com/KanaWorks_AI/status/2106717014245183517) (üreten [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**Mevcut karakter animasyonunu prosedürel geliştirmeyle birleştirirken eski varlıkların rolünü koruyun.**

Yazar, mevcut Unimate robot köpek animasyonunu bir arkadaşa dönüştürüp tarama ve iz özellikli tüylü sanal evcil hayvan yapıyor. Unreal Engine ve mevcut robot animasyonu iş akışının açık parçaları.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="Robot arkadaşlar ve prosedürel tüyler" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [Matematik temalı hareketli kurgu](https://x.com/TurboNexic/status/2106710792590835934) (üreten [@TurboNexic](https://x.com/TurboNexic))

**Matematik temalı hareketli grafikleri görsel iletişim örneği olarak inceleyin.**

Paylaşımcı matematik temalı bir hareketli kurgu sunuyor. Dikey klip, matematiksel imgeleri animasyon tasarımında kullanıyor; tamamlanmış matematik çözümü değil, görsel gösterim sağlıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="Matematik temalı hareketli kurgu" width="760">

*Kaynak videodan arşivlenmiş bir kare.*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Your Woman şarkı sözü videosu](https://x.com/atomtanstudio/status/2106702854639743467) (üreten [@atomtanstudio](https://x.com/atomtanstudio))

**Şarkı sözlerini verilen kayda göre hareketlendirirken müziğin rolünü açık tutun.**

Üretici, White Town'ın Your Woman parçası için şarkı sözü videosu paylaşıyor. Mevcut şarkı, modelin bestelediği iddia edilen müzik değil, görsel çalışmanın ses girdisi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Your Woman şarkı sözü videosu" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [Müzik videosunu JavaScript ile yeniden çizmek](https://x.com/abhinavflac/status/2106638839666373114) (üreten [@abhinavflac](https://x.com/abhinavflac))

**Müzik videosunu yeniden işlerken kaynak kareleri kod tabanlı şekillere dönüştürün.**

Yazar, Eminem'in Godzilla videosundaki kareleri düz şekillere izleyip JavaScript ile yeniden çizdiğini anlatıyor. Özgün görüntü ve müzik, ortaya çıkan animasyonun girdileri.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="Müzik videosunu JavaScript ile yeniden çizmek" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [Çin futbolu animasyonu](https://x.com/esrhengwu/status/2106625966965760380) (üreten [@esrhengwu](https://x.com/esrhengwu))

**Spor temasını animasyon anlatısı tarifine dönüştürün.**

Yazar, Çin milli futbol takımının gelişimini ve direncini yaratıcı tema olarak ele alan animasyonu paylaşıyor. Kayıt, somut bir spor hikâyesi örneği sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="Çin futbolu animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [El konsolu yeniden topoloji gösterimi](https://x.com/mickeysmith_jp/status/2106607349385630138) (üreten [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**Topolojiyi tartışırken konsol çizimini tel kafes görünümüyle karşılaştırın.**

Paylaşımcı, yeniden topoloji konusunda bir el konsolu görüntüsünü tel kafes benzeri görünümle eşleştiriyor. Bu somut modelleme sunumu, düzenlenebilir ağ veya belgelenmiş yeniden topoloji yöntemi değil.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="El konsolu yeniden topoloji gösterimi" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft ile Pokémon birleşimi](https://x.com/MozeTech/status/2106590326634983710) (üreten [@MozeTech](https://x.com/MozeTech))

**Tanıdık iki oyunun mekaniklerini aynı prototip tarifinde birleştirin.**

Yazar, Minecraft benzeri yapım ve üretimi Pokémon benzeri yakalamayla birleştiren Pallet Town prototipi ve demo bağlantısı sunuyor. Gönderi, yapımı tek seferlik üretim deneyi olarak tanımlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft ile Pokémon birleşimi" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [Bir dil modelinin yapılışını açıklamak](https://x.com/imjustnewatai/status/2106546810793730419) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Teknik bir soruyu görsel açıklama isteğine dönüştürün.**

Yazar, büyük dil modelinin nasıl yapıldığını sorup çıkan açıklayıcı videoyu paylaşıyor. Eser, teknik bir konuyu animasyon dizisiyle sunmanın somut örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="Bir dil modelinin yapılışını açıklamak" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [Altman öne çıkanlar kurgusu](https://x.com/benchmark_lb900/status/2106539977404506303) (üreten [@benchmark_lb900](https://x.com/benchmark_lb900))

**Kısa hareketli kurgunun ritmini tanınmış kişi temasıyla deneyin.**

Yazar, Altman temalı öne çıkanlar videosunu tek seferlik çıktı olarak paylaşıyor. Dikey kayıt, kısa bir hareketli kurgu örneği sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="Altman öne çıkanlar kurgusu" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [Otuz Altı Stratejinin ilki](https://x.com/jesselaunz/status/2106538284197548122) (üreten [@jesselaunz](https://x.com/jesselaunz))

**Anlatı animasyonunda harici müzik araçlarını da belgeleyin.**

Yazar, Otuz Altı Stratejinin ilki hakkında tek talimatla hazırladığını söylediği filmi paylaşıyor. Müzik için Suno V6'nın adı verilerek ses aracının ayrı rolü korunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="Otuz Altı Stratejinin ilki" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [Oyun modelleme, iskelet ve animasyon](https://x.com/atomtanstudio/status/2106516974662713477) (üreten [@atomtanstudio](https://x.com/atomtanstudio))

**Oyun sahnesinde karakter oluşturmayı, iskelet kurmayı ve animasyonu birlikte değerlendirin.**

Yazar, karakter modelleme, iskelet kurma ve animasyonu içeren Depths of Despair karşılaştırması paylaşıyor. Gönderi kullanılan varlıkları ve araçları anlatıp görünen sonuçları birlikte sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="Oyun modelleme, iskelet ve animasyon" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [Çocuk ölümleri üzerine sözsüz film](https://x.com/cocoloba_/status/2106512963414970458) (üreten [@cocoloba_](https://x.com/cocoloba_))

**Zor bir toplumsal konuyu sözsüz görsel dizilerle aktarın.**

Yazar, nefes alan bebek ve kararan beşik imgeleriyle çocuk ölümlerini anlatan filmi paylaşıyor. Örnek, filmdeki nüfus istatistiklerini benimsemek yerine görsel hikâye görevini koruyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="Çocuk ölümleri üzerine sözsüz film" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [Glikolizden etanole SVG animasyonu](https://x.com/olddonkeyblog/status/2106508425211330750) (üreten [@olddonkeyblog](https://x.com/olddonkeyblog))

**Moleküler bir süreci anlatmak için HTML içine hareketli SVG yerleştirin.**

Yazar, glikoz molekülünün glikoliz ve etanol oluşumundan geçmesini, HTML içindeki hareketli SVG ile göstermeyi istiyor. Kayıt ortaya çıkan bilimsel görselleştirmeyi sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="Glikolizden etanole SVG animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [On altı eşzamanlı Starship fırlatışı](https://x.com/olddonkeyblog/status/2106507742454403485) (üreten [@olddonkeyblog](https://x.com/olddonkeyblog))

**HTML ve SVG animasyonunda eşzamanlı fırlatma aşamalarını açıkça belirtin.**

Yazar, on altı Starship'in birlikte fırlatılmasını, sonra kademe ayrılması ve uzaya çıkışı istiyor. Kayıt ortaya çıkan çok nesneli animasyon dizisini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="On altı eşzamanlı Starship fırlatışı" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [Animasyonlu pelikan bisiklet testi](https://x.com/olddonkeyblog/status/2106507429265756165) (üreten [@olddonkeyblog](https://x.com/olddonkeyblog))

**Pelikanın bisiklet sürmesini eşgüdümlü hareket çizimi görevi olarak inceleyin.**

Yazar, pelikanın bisiklet sürdüğü görevdeki Max akıl yürütme çıktısını paylaşıyor. Bu kayıt, aynı genel istemi kullanan diğer üreticilerin sonuçlarından ayrı bir örnek.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="Animasyonlu pelikan bisiklet testi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [Gelecek yüz elli yılın öyküsü](https://x.com/imjustnewatai/status/2106489784382197771) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Geleceğe ilişkin film tarifinde senaryo, kodlanmış görseller ve müziği birleştirin.**

Yazar, insanlığın gelecek yüz elli yılını tek talimatla anlattığı filmi bildiriyor. Eser, olası gelecek yaşamı göstermek için yazılı anlatı, kod animasyonu ve müziği birleştiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="Gelecek yüz elli yılın öyküsü" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [Bağımsız Humanity Walks deneyi](https://x.com/iowitz/status/2106489119186538583) (üreten [@iowitz](https://x.com/iowitz))

**Sanat tarihi boyunca yürüyüş fikrini bağımsız bir yaratıcı deney olarak yeniden çalışın.**

Yazar, başka gösterimleri gördükten sonra kendi sanat tarihi yürüyüş animasyonunu deneyip paylaşıyor. Tema benzediği için birleştirmek yerine ayrı üretim olarak korunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="Bağımsız Humanity Walks deneyi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [The Grader kod filmi](https://x.com/argofowl/status/2106476549046513947) (üreten [@argofowl](https://x.com/argofowl))

**Kodla üretilmiş filmde harici konuşma veya ses araçlarını belgeleyin.**

Yazar, kodlanmış The Grader filmini paylaşırken ses için ElevenLabs v4'ü belirtiyor. Gönderi, yaklaşık iki saat yirmi iki dakika süren tek seferlik çalışma bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="The Grader kod filmi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [Reawakening korku kısa filmi](https://x.com/JaydenDavisNC/status/2106440774367822008) (üreten [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**Kısa animasyonun biçimini belirli bir korku öncülüyle şekillendirin.**

Yazar, Reawakening adlı korku temalı yapay zekâ kısa filmini paylaşıyor. Eser, korku animasyonu için somut anlatı ve atmosfer örneği sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="Reawakening korku kısa filmi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [Yirmi beş saniyelik kendini geliştirme videosu](https://x.com/DAssetBuzz/status/2106505100575592838) (üreten [@DAssetBuzz](https://x.com/DAssetBuzz))

**Soyut kendini geliştirme temasını kısa yaratıcı film tarifine dönüştürün.**

Yazar, modeli neyin daha iyi yapacağı hakkında yirmi beş saniyelik video istiyor ve sonucu paylaşıyor. Öncül, ürün yeteneği beyanı değil, yaratıcı hikâye işlevi görüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="Yirmi beş saniyelik kendini geliştirme videosu" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [Kale sahnesi ve kullanım maliyeti](https://x.com/nemumusitocha/status/2106429338556207284) (üreten [@nemumusitocha](https://x.com/nemumusitocha))

**3D sahneyi değerlendirirken ayrıntıları ve üreticinin kullanım deneyimini birlikte ele alın.**

Yazar, ayrıntılı kale sahnesinin görsel yapısını överken kullanım maliyetini değersiz buluyor. Örnek, somut sahneyi yazarın maliyet memnuniyeti geri bildirimiyle eşleştiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="Kale sahnesi ve kullanım maliyeti" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [Kırk saniyelik marka tanıtım reklamı](https://x.com/0xashtonx/status/2106421702783914423) (üreten [@0xashtonx](https://x.com/0xashtonx))

**Kısa tanıtım reklamında kendi markanızı konu edin.**

Üretici, kendi markası için kırk saniyelik tanıtım reklamı isteyip ortaya çıkan videoyu paylaşıyor. Görev, markalı tanıtım anlatısının somut bir örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="Kırk saniyelik marka tanıtım reklamı" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [Rocketball yeniden yapımı](https://x.com/atomtanstudio/status/2106418747083022555) (üreten [@atomtanstudio](https://x.com/atomtanstudio))

**Tanıdık oyun yeniden yapımıyla kodlanmış varlıkları ve etkileşim mekaniklerini birleştirin.**

Yazar, 1980'lerin C-64 oyununun yeniden yapımı Rocketball'ı paylaşarak varlıkların kodlandığını söylüyor. İnternet sitesi sürümünü değiştirmek gelecekteki plan olarak belirtiliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="Rocketball yeniden yapımı" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [Voksel pagoda karşılaştırması](https://x.com/dropout_layer/status/2106408147309252915) (üreten [@dropout_layer](https://x.com/dropout_layer))

**Aynı sahnenin iki çalışmasını bildirilen çalışma maliyetleriyle birlikte karşılaştırın.**

Yazar, 3D voksel pagodanın Astra ve Fable sonuçları için sırasıyla 3,50 ve 5,50 dolar maliyet bildiriyor. Karşılaştırma bu çalışmaları ve gösterilen sahneleri kapsıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="Voksel pagoda karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [Hayali Switch 3 sunumu](https://x.com/mathisbuilds/status/2106407842240418097) (üreten [@mathisbuilds](https://x.com/mathisbuilds))

**Hayali ürünü kavramsal sunum ve gösterim görevi olarak kullanın.**

Yazar, hayali Nintendo Switch 3 ve demosunu isteyerek yaklaşık dört saat çalışma bildiriyor. Kayıt gerçek ürün şartnamesi değil, kurgusal yeni konsol kavramı sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="Hayali Switch 3 sunumu" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [Açılış sayfalarının önce ve sonrası](https://x.com/nemumusitocha/status/2106402952307200302) (üreten [@nemumusitocha](https://x.com/nemumusitocha))

**Aynı açılış sayfası istemini yeniden çalıştırıp zaman içindeki değişimi karşılaştırın.**

Yazar, aynı istemle yeni üretilen açılış sayfasını önceki sayfayla karşılaştırıyor. Görünen önce-sonra tasarımları pratik arayüz karşılaştırması sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="Açılış sayfalarının önce ve sonrası" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [Hayali bir yapay zekânın iç dünyası](https://x.com/blueemi99/status/2106397329653719115) (üreten [@blueemi99](https://x.com/blueemi99))

**Hayali iç bakışı yaratıcı animasyon öncülü olarak kullanın.**

Yazar, bir yapay zekâ modeli olmanın nasıl hissettireceği üzerine film isteyip tek seferlik sonucu paylaşıyor. Öncül, hayali görsel anlatım olarak sunuluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="Hayali bir yapay zekânın iç dünyası" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Go şarkı sözü hareket tasarımı](https://x.com/atomtanstudio/status/2106377491267137848) (üreten [@atomtanstudio](https://x.com/atomtanstudio))

**Mevcut şarkı kaydı çevresinde verilen sözleri hareketlendirin.**

Üretici, The Chemical Brothers'ın Go parçası için Max akıl yürütmeyle yaptığı söz videosunu paylaşıyor. Şarkı kaydı bu hareket tasarımının harici ses girdisi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Go şarkı sözü hareket tasarımı" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [İkinci on beş saniyelik hareket portföyü](https://x.com/Saccc_c/status/2106376222309761094) (üreten [@Saccc_c](https://x.com/Saccc_c))

**Serbest hareket tasarımı portföyüyle yeni görsel yönü araştırın.**

Yazar, yeni on beş saniyelik hareket portföyünü yaratıcı istemiyle paylaşıyor. Bu üretimin önceki portföyden ayrı olduğunu açıkça belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="İkinci on beş saniyelik hareket portföyü" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [Yönlendirmeli ajan uygulama incelemesi](https://x.com/RobIW_dev/status/2106371025852108940) (üreten [@RobIW_dev](https://x.com/RobIW_dev))

**Fikirden uygulamaya geçmeden planın mevcut sisteme uygunluğunu inceleyin.**

Yazar, sistem uyumu, uygulama planlama ve açıklama ilkelerini paylaşarak bitmiş işi nasıl değerlendirdiğini veya sonraki uygulamaya nasıl karar verdiğini anlatıyor. Görsel somut planlama belgesini koruyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="Yönlendirmeli ajan uygulama incelemesi" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [Claude maskot dansı](https://x.com/ishuagra02/status/2106369929813594134) (üreten [@ishuagra02](https://x.com/ishuagra02))

**Hareketle müziğin ilişkisini ritme uyan maskot animasyonuyla sınayın.**

Üretici, ritmi yakaladığını söylediği Claude maskot dansını paylaşıyor. Aynı yerel videoyu kullanan yeniden paylaşımlar tekrar sayılmayıp bu kaynağa bağlanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="Claude maskot dansı" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [Etkileşimli Yedi Harika adaları](https://x.com/notjazii/status/2106368606502334922) (üreten [@notjazii](https://x.com/notjazii))

**Ünlü yapıları etkileşimli ada sahnesindeki hedefler olarak kullanın.**

Kaynak paylaşımcısı, ünlü yapıları 3D adalara yerleştiren Yedi Harika sahnesini sunuyor. Kayıt, tanınabilir anıtlarla etkileşimli görsel ortam düzenlemenin somut örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="Etkileşimli Yedi Harika adaları" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [Propellerheads müzik videosu](https://x.com/atomtanstudio/status/2106353569603736009) (üreten [@atomtanstudio](https://x.com/atomtanstudio))

**Uzun hareketli grafik dizisini verilen müziğin etrafında kurun.**

Üretici, Propellerheads'ın On Her Majesty’s Secret Service parçasına hazırladığı müzik videosunu paylaşıyor. Mevcut kayıt, animasyon görsellerinin ses girdisi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="Propellerheads müzik videosu" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Steamboat Willie animasyon karşılaştırması](https://x.com/mathisbuilds/status/2106351978691305732) (üreten [@mathisbuilds](https://x.com/mathisbuilds))

**Sesi açık tutarak aynı kısa sahnenin iki animasyon yorumunu karşılaştırın.**

Yazar, xhigh düzeyinde Fable ve Opus olarak etiketlenmiş Steamboat Willie karşılaştırmasını tek seferlik çalışmalar diye sunuyor. Klip bu belirli görüntü ve ses karşılaştırmasını gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Steamboat Willie animasyon karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [Sanxingdui temalı film](https://x.com/hungryturbo/status/2106339115642019904) (üreten [@hungryturbo](https://x.com/hungryturbo))

**Animasyon kısa filmini kültürel tarih temasıyla düzenleyin.**

Yazar, Sanxingdui temalı filmi yaratıcı görsel anlatı olarak paylaşıyor. Kayıt tarihsel-kültürel bir konuyu animasyon tarifine çevirmenin somut örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="Sanxingdui temalı film" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Bugatti Chiron önce ve sonra](https://x.com/alannnfx/status/2106323394350461031) (üreten [@alannnfx](https://x.com/alannnfx))

**Eski otomobil istemini yeniden çalıştırıp modelleme ve özellik ayrıntısını karşılaştırın.**

Aynı yazar, önceki çalışmasıyla yeni tekrarlanan istemin Bugatti Chiron sonuçlarını gösteriyor. Kaydedilmiş önce-sonra karşılaştırması, daha zengin modelleme ve sahne özelliklerine odaklanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Bugatti Chiron önce ve sonra" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [GRAIN kavram filmi](https://x.com/NFT_Chen/status/2106301427052360150) (üreten [@NFT_Chen](https://x.com/NFT_Chen))

**Soyut kavram filmini tekrarlanan görsel motifler üzerine kurun.**

Üretici; tohum, tahıl, ağaç ve dağ imgelerini bağlayan GRAIN kısa filmini paylaşıyor. Dizinin anlatı yapısını yinelenen biçimler ve geçişler oluşturuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="GRAIN kavram filmi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [Human in Transit sanat galerisi](https://x.com/exploraX_/status/2106296439936614646) (üreten [@exploraX_](https://x.com/exploraX_))

**Tarihsel görsel yolculuğu etkileşimli galeri biçiminde sunun.**

Kaynak paylaşımcısı, antik dönemden modern sanat tarzlarına ilerleyen Human in Transit galerisini gösteriyor. Kaydedilmiş arayüz, farklı görsel dönemleri tek sunumda düzenlemeye somut referans veriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="Human in Transit sanat galerisi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [İpek Yolu görsel kısa filmi](https://x.com/hungryturbo/status/2106294812261695508) (üreten [@hungryturbo](https://x.com/hungryturbo))

**Seyahat ve tarih temasını tutarlı bir görsel kısa filme dönüştürün.**

Yazar, İpek Yolu temalı filmi paylaşıyor. Eser, tarihsel bir yolculuğun animasyon imgeleriyle yaratıcı biçimde anlatılmasına somut örnek sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="İpek Yolu görsel kısa filmi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [Dört dönüşüm sunumu](https://x.com/dpkostka/status/2106272731364794757) (üreten [@dpkostka](https://x.com/dpkostka))

**Dönüşüm çerçevesini sunumun düzenleyici yapısı olarak kullanın.**

Yazar, dört dönüşüm yolunu anlatan slaytlar paylaşıyor. Sunum görüntüsü, kavramsal çerçevenin görsel belgeye nasıl yerleştirilebileceğini gösteriyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="Dört dönüşüm sunumu" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [Geçmiş sohbet üslubunu karşılaştırmak](https://x.com/kiyoshi_shin/status/2106268573186637883) (üreten [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**Üslup değişimini incelerken eski konuşmaları güncel yanıtlarla karşılaştırın.**

Yazar, güncel modelden eski sohbetleri ve mevcut üslubunu çözümlemesini isteyerek değişimden memnun olmadığını belirtiyor. Ekli görüntü bu konuşma karşılaştırması görevini kaydediyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="Geçmiş sohbet üslubunu karşılaştırmak" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [Kakapo sevimlilik testi](https://x.com/hanawo_neki/status/2106257409782288659) (üreten [@hanawo_neki](https://x.com/hanawo_neki))

**Belirli karakter tercihleriyle üretilmiş animasyon tarzlarını karşılaştırın.**

Yazar, kakapo animasyonunu paylaşarak sevimlilik odaklı bu karşılaştırmada Opus'u tercih ettiğini söylüyor. Olumsuz estetik geri bildirim, gerçek animasyon çıktısıyla birlikte korunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="Kakapo sevimlilik testi" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [On çizgi roman döneminde Spider-Man](https://x.com/chetaslua/status/2106248621519978867) (üreten [@chetaslua](https://x.com/chetaslua))

**Farklı çizgi roman dönemlerine geçerken karakteri tanınabilir tutun.**

İlk paylaşımcı, Spider-Man'in on çizgi roman döneminden geçtiği animasyonu sunuyor. Aynı videoyu kullanan diğer gönderiler yeni eser sayılmayıp bu kaynağa bağlanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="On çizgi roman döneminde Spider-Man" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [İlluminati temalı kurmaca korku videosu](https://x.com/badboyfoxy/status/2106241189976387799) (üreten [@badboyfoxy](https://x.com/badboyfoxy))

**Komplo temalı korku tarifini kurmaca hikâye alıştırması olarak ele alın.**

Yazar, korkutucu İlluminati temalı video isteyip ortaya çıkan eseri paylaşıyor. Konu animasyona kurmaca bir korku öncülü sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="İlluminati temalı kurmaca korku videosu" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [Kodlanmış nükleer bilim tarihi filmi](https://x.com/imjustnewatai/status/2106238699872956427) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Bilim tarihi açıklayıcısında özel kodlu çizim sistemiyle müziği birleştirin.**

Yazar, nükleer bilimin atom bombasını nasıl mümkün kıldığını anlatan üç dakikalık 3D film istiyor; çizilmiş kareler, özel çizici ve sentezlenmiş müzik bildiriyor. Örnek, görsel-işitsel üretim iş akışını kapsıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="Kodlanmış nükleer bilim tarihi filmi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [Evrensel Yüksek Gelir açıklayıcısı](https://x.com/markbraincell/status/2106234118514323515) (üreten [@markbraincell](https://x.com/markbraincell))

**Ekonomik bir kavramı animasyonla açıklayın.**

Kaynak paylaşımcısı Evrensel Yüksek Gelir'i anlatan animasyon sunuyor. Kayıt, ekonomik savı ölçülmüş sonuç haline getirmeden somut kavram açıklama örneği sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="Evrensel Yüksek Gelir açıklayıcısı" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [Altman–Amodei anlaşmazlığı açıklayıcısı](https://x.com/imjustnewatai/status/2106204392588276065) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Bir anlaşmazlığı animasyon açıklayıcısının anlatı yapısı olarak kullanın.**

Yazar, Altman–Amodei anlaşmazlığının animasyonla anlatılmasını isteyip sonucu paylaşıyor. Görev, bağımsız kaynaklı tarih kaydı değil, güncel konu açıklama biçimini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="Altman–Amodei anlaşmazlığı açıklayıcısı" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [Claude maskot müzik videosu](https://x.com/synthshareai/status/2106195060140446028) (üreten [@synthshareai](https://x.com/synthshareai))

**Karakter odaklı kurgu için maskot katmanını verilen görüntüyle birleştirin.**

Kaynak paylaşımcısı, gerçek çekim müzik videosunun üstüne yerleştirilmiş Claude maskotunu ve on iki saatlik çalışmayı bildiriyor. Görsel işlem, çizgi karakter katmanını verilen çekimle birleştiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="Claude maskot müzik videosu" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [Kuarklardan evrene kesintisiz yakınlaşma](https://x.com/imjustnewatai/status/2106190594775097663) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Bilimsel ölçekleri tek görsel-işitsel öyküde sürekli ölçek değişimiyle bağlayın.**

Yazar, kuarklardan evrene uzanan yolculuk için kodlanmış görseller ve sentez müziği bildiriyor. Kayıt kesintisiz ölçek geçişleri ve tutarlı görsel anlatı gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="Kuarklardan evrene kesintisiz yakınlaşma" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [2076 dünyasını hayal etmek](https://x.com/Layton_Gott/status/2106190496075035096) (üreten [@Layton_Gott](https://x.com/Layton_Gott))

**Gelecek dünya sahnesini belirli bir anlatı süresiyle isteyin.**

Yazar, yirmi beş saniyelik video isteğinin ardından 2076 dünyasını hayal eden kısa filmi paylaşıyor. Aynı kaydın diğer hesaplarda kullanımı bu kaynağa bağlanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="2076 dünyasını hayal etmek" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [Aşağı Manhattan bina kronolojisi](https://x.com/nroze22/status/2106183281293381661) (üreten [@nroze22](https://x.com/nroze22))

**Mimari zaman çizelgesinde bina izlerini, tarihlerini ve yüksekliklerini birleştirin.**

Yazar, Aşağı Manhattan'ı mimari çizim tarzı arayüzle; bina tarihleri, taban izleri ve yükseklikleriyle sunuyor. Kayıt somut etkileşimli kronoloji kavramı sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="Aşağı Manhattan bina kronolojisi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [Kehanet kemiği yazısı animasyonu](https://x.com/MinLiBuilds/status/2106180691344118202) (üreten [@MinLiBuilds](https://x.com/MinLiBuilds))

**Yazının evrimini animasyonlu tarih yolculuğunun konusu yapın.**

Yazar, kehanet kemiği yazısıyla başlayan bir animasyon paylaşıyor. Kayıt, yazılı işaretlerin tarihi çevresinde kurulmuş somut görsel anlatı örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="Kehanet kemiği yazısı animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [Karakterlerle başka bir sanat tarihi animasyonu](https://x.com/imjustnewatai/status/2106162924331180510) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Tanıdık karakterleri değişen tarihsel ortamlarda sürekli rehber olarak kullanın.**

Yazar, Iron Man ve Spider-Man'in tarih boyunca uçmasını isteyip sonucu paylaşıyor. Bu, diğer üreticilerin benzer tarih yolculuğu deneylerinden ayrı bir eser.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="Karakterlerle başka bir sanat tarihi animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [Kodlanmış Seikilos görsel-işitsel eseri](https://x.com/YanqingCheng/status/2106158746938269728) (üreten [@YanqingCheng](https://x.com/YanqingCheng))

**Tarihsel müzik metni çevresinde tek dosyalı görsel-işitsel eser kurun.**

Yazar, tek HTML ve JavaScript dosyasında görsel ve müzik sentezlediğini söylediği Seikilos yazıtı çalışmasını paylaşıyor. Tarihsel metin, kodlanmış dizinin düzenleyici teması.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="Kodlanmış Seikilos görsel-işitsel eseri" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [Jet animasyonu karşılaştırması](https://x.com/Kinzf2121/status/2106158536963330346) (üreten [@Kinzf2121](https://x.com/Kinzf2121))

**Aynı uçak görevinde uçuş animasyonunu ve kamera takibini karşılaştırın.**

Yazar, Fable 5.1 etiketli sonuçla Opus arasında jet animasyonu karşılaştırması paylaşıyor. Sahne kayıtları uçak hareketini ve sinematik kamera takibini karşılaştırmaya somut örnek veriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="Jet animasyonu karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [Modelin kendini tanıtma filmi](https://x.com/devteamdrew/status/2106155815707021549) (üreten [@devteamdrew](https://x.com/devteamdrew))

**Kendini tanıtma tarifiyle model temalı animasyonu araştırın.**

Üretici, tek istemle kendini tanıtma videosu istediğini söyleyip sonucu paylaşıyor. Görev, model temalı anlatıyı animasyon sunumuyla birleştiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="Modelin kendini tanıtma filmi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [Kıyamet sonrası kart oyunu prototipi](https://x.com/maciejkrupowies/status/2106153578029338850) (üreten [@maciejkrupowies](https://x.com/maciejkrupowies))

**Kart oyunu temasını prototipleyip çıkan savaş arayüzünü inceleyin.**

Yazar, tek seferde yapıldığını söylediği kıyamet sonrası Hearthstone tarzı prototipi paylaşıyor. Gönderi küçük hataları kabul ederken arayüzü ve etkileşimleri gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="Kıyamet sonrası kart oyunu prototipi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [The Late Byte işyeri animasyonu](https://x.com/rohit3a/status/2106138910648914094) (üreten [@rohit3a](https://x.com/rohit3a))

**Model kişiliklerini animasyonlu işyeri konuşmasının karakterlerine dönüştürün.**

Üretici, Opus'un öfkeli patron olduğu The Late Byte işyeri hikâyesini sunuyor. Bu, ayrı Day in the Life of Claude filminden farklı bir anlatı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="The Late Byte işyeri animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Queens of the Stone Age söz animasyonu](https://x.com/atomtanstudio/status/2106135196483608745) (üreten [@atomtanstudio](https://x.com/atomtanstudio))

**Verilen şarkıyı kinetik tipografi ve hareket tasarımıyla birleştirin.**

Üretici, Queens of the Stone Age kaydı çevresinde kinetik tipografili müzik videosu yaptığını anlatıyor. Şarkı ses girdisi; örnek sözleri ve görselleri düzenleme görevini kapsıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Queens of the Stone Age söz animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [Paylaşılan Three.js anlatı sahnesi](https://x.com/Noreply134882/status/2106116572389478746) (üreten [@Noreply134882](https://x.com/Noreply134882))

**Paylaşılan 3D hikâye klibini anlatı sahnesi tasarımında referans alın.**

Paylaşımcı, Three.js anlatı sahnesini sunup yoğun token tüketiminden söz ediyor. Klip, paylaşılan somut 3D hikâye anlatımı örneği olarak korunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="Paylaşılan Three.js anlatı sahnesi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [Tarihsel sahnelerde ay yürüyüşü](https://x.com/noclipepe/status/2106105810812112937) (üreten [@noclipepe](https://x.com/noclipepe))

**Dans motifini farklı tarihsel ortamlar ve görsel tarzlar boyunca taşıyın.**

Paylaşımcı, dinozorlardan Ay'a uzanan Michael Jackson ay yürüyüşü dizisini sunuyor. Film, paylaşılan dans ve tarz galerisi örneği olarak korunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="Tarihsel sahnelerde ay yürüyüşü" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [Ayrıntılı istemle hareketli grafikler](https://x.com/devswha/status/2106100273509007802) (üreten [@devswha](https://x.com/devswha))

**Ayrıntılı yaratıcı tarifi daha kısa hareket tasarımı isteğiyle karşılaştırın.**

Yazar, varlık, referans video veya kaynak dosya vermeden yalnızca ayrıntılı istemle oluşturduğunu söylediği hareketli grafikleri paylaşıyor. Sonuç, istem odaklı hareket tasarımına somut referans sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="Ayrıntılı istemle hareketli grafikler" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [Kiralama işletmesi sitesi arayüzü](https://x.com/oalanicolas/status/2106098902965309475) (üreten [@oalanicolas](https://x.com/oalanicolas))

**Somut site arayüzü keşfi için kiralama işletmesi tarifi kullanın.**

Üretici, kiralama işletmesine ait site arayüzü ekran görüntüsünü paylaşıyor. Örnek, görünen sayfa tasarımını ve işletmenin sunumunu kapsıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="Kiralama işletmesi sitesi arayüzü" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [AGI temalı yaratıcı film](https://x.com/AndrewOnXYZ/status/2106097745098395712) (üreten [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**Tekrarlanan yaratıcı istemle anlatı ve görsel yaklaşımları karşılaştırın.**

Yazar, tekrarlanan istemden üretilmiş AGI temalı animasyonu paylaşıyor. Film, modelin sözlerini yaratıcı anlatının parçası olarak ele alıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="AGI temalı yaratıcı film" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [Kedi yan öyküsüyle sanat tarihi](https://x.com/cherry_mx_reds/status/2106095190285144331) (üreten [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Birçok sanat dönemini sürekli görünen karakterle kısa anlatıya sıkıştırın.**

Üretici, kedi yan öyküsü bulunan on beş saniyelik sanat tarihi turu sunuyor. On beş saniye filmin süresi; yaratıcı görev birçok tarihsel tarzı kapsıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="Kedi yan öyküsüyle sanat tarihi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [Savaş prototipi ve voksel sahne](https://x.com/OnlyTerp/status/2106089280502210626) (üreten [@OnlyTerp](https://x.com/OnlyTerp))

**Yaratıcı kodlama görevinde hem oyun savaşını hem dünya kurma sonuçlarını inceleyin.**

Yazar, uzun üretim çalışması anlatarak DMC tarzı savaş prototipiyle voksel sahneyi paylaşıyor. Gönderi oyun mekanikleri ve görsel dünya tasarımı için iki somut çıktı sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="Savaş prototipi ve voksel sahne" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [İnternet mizahı kronolojisi](https://x.com/chetaslua/status/2106076940558082297) (üreten [@chetaslua](https://x.com/chetaslua))

**Animasyon kronolojisini yıllara özgü görsel tarz ve müzikle düzenleyin.**

Üretici, 2010'dan 2026'ya viral internet mizahı animasyonu paylaşıyor. Kodlanmış anlatıda her yılın kendi görsel tarzı ve müzik işlemesi var.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="İnternet mizahı kronolojisi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [Tek satırdan parçacık hareketi](https://x.com/devswha/status/2106072107365114186) (üreten [@devswha](https://x.com/devswha))

**Ayrıntılı istemi geliştirmeden önce tek satırlık hareket tarifiyle başlayın.**

Üretici, tek satırlık istemden parçacık animasyonunu paylaşarak daha ayrıntılı istek denemeyi planladığını söylüyor. Bu, uzun hareket tasarımı örneğinden ayrı bir üretim.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="Tek satırdan parçacık hareketi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [Kung-Fu Boy animasyonu](https://x.com/HashmathRzz/status/2106065773336965510) (üreten [@HashmathRzz](https://x.com/HashmathRzz))

**Dövüş sanatları karakteri tarifiyle animasyon hareketini araştırın.**

Yazar, Fable 5.5'e atfettiği Kung-Fu Boy karakter animasyonunu paylaşıyor. Ekli kayıt, dövüş sanatları teması için somut animasyon sonucunu sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="Kung-Fu Boy animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [Hürmüz Boğazı tartışma animasyonu](https://x.com/chetaslua/status/2106060047805792415) (üreten [@chetaslua](https://x.com/chetaslua))

**Tartışma konusunu animasyon anlatısına dönüştürün.**

Üretici, Hürmüz Boğazı hakkında animasyonlu tartışma sunuyor. Örnek, çevre gönderide gösterilmeden anılan diğer kullanımları değil, görünen tartışma filmini kaydediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="Hürmüz Boğazı tartışma animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [Tek boynuzlu at SVG tarz deneyi](https://x.com/atomtanstudio/status/2106057876053918127) (üreten [@atomtanstudio](https://x.com/atomtanstudio))

**Aynı temalı çizim göreviyle SVG üslup seçimlerini inceleyin.**

Yazar, başka üreticinin testinden esinlenen tek boynuzlu at SVG deneyini paylaşıyor. Görsel aynı konunun görsel işlemesini karşılaştırmaya somut çıktı sağlıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="Tek boynuzlu at SVG tarz deneyi" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [Cadılar Bayramı animasyonu](https://x.com/cherry_mx_reds/status/2106056643255447590) (üreten [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Kısa yaratıcı animasyon için kodlama modeline mevsimsel tema verin.**

Üretici, Cadılar Bayramı temalı eser isteyip çıkan animasyonu paylaşıyor. Gönderi, bu belirli yaratıcı görevin özgün kaydını sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="Cadılar Bayramı animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Blender CLI barbarı ve kapağı](https://x.com/BoDy051/status/2106047375320166885) (üreten [@BoDy051](https://x.com/BoDy051))

**Karakter modelleme ve kapak çizimini Blender CLI talimatlarıyla araştırın.**

Yazar, RPG barbar karakterini ve kapak kavramını Opus çıktısıyla karşılaştırıyor. Yapım ve çizim aracı Blender CLI; model kod talimatları sağlıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Blender CLI barbarı ve kapağı" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Claude'un hayatından bir gün](https://x.com/ishuagra02/status/2106045364868419727) (üreten [@ishuagra02](https://x.com/ishuagra02))

**Tekrarlanan maskotla animasyonlu günlük yaşam öyküsü kurun.**

İlk paylaşımcı, maskotun yer aldığı Day in the Life of Claude filmini sunuyor. Kaynak video ayrı maskot dansından ve onun yeniden paylaşımlarından farklı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Claude'un hayatından bir gün" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [3D insanlık tarihi](https://x.com/blueemi99/status/2106041578204655748) (üreten [@blueemi99](https://x.com/blueemi99))

**Kodlanmış sahneleri ve animasyonu tarihsel görsel dizide birleştirin.**

Üretici, eski insanlıktan günümüze uzanan 3D videoyu paylaşarak animasyonları ve modelleri kodla ürettiğini söylüyor. Sonuç görsel hikâye örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="3D insanlık tarihi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [Hızlı hareket tasarımcısı gösterimi](https://x.com/blueemi99/status/2106031355922387163) (üreten [@blueemi99](https://x.com/blueemi99))

**Kısa hareketli gösterimde ritmi, sesi ve tutarlılığı değerlendirin.**

Yazar, hızlı tempolu kısa hareket videosunun sesini ve tutarlılığını kendi Opus çıktısıyla karşılaştırıyor. Yargı, bu belirli eserdeki üretici deneyimini anlatıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="Hızlı hareket tasarımcısı gösterimi" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [Serbest karmaşık 3D yaratım](https://x.com/cocoloba_/status/2106029181607772413) (üreten [@cocoloba_](https://x.com/cocoloba_))

**Açık uçlu yaratıcı istekle karmaşık 3D kompozisyonu araştırın.**

Üretici, modelin boş zamanda ne yapacağını sorup çıkan 3D eseri paylaşıyor. Gönderi, oluşan kompozisyonun birçok ayrı parçadan oluştuğunu anlatıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="Serbest karmaşık 3D yaratım" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [Çöp adam dövüş animasyonu](https://x.com/HelaliBillel/status/2106028502763900944) (üreten [@HelaliBillel](https://x.com/HelaliBillel))

**Belirli savaş animasyonu isteğiyle zamanlamayı ve hareketi inceleyin.**

Üretici, hareketli çöp adam dövüşü videosu isteyip sonucu paylaşıyor. Ekli kayıt savaş animasyonu görevinin somut örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="Çöp adam dövüş animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [Tek istemlik UI hareket dizisi](https://x.com/iancarscadden/status/2106018048792789360) (üreten [@iancarscadden](https://x.com/iancarscadden))

**Tek animasyon tarifiyle bir UI dizisini araştırın.**

Yazar, yaklaşık altı veya yedi dakikada tek seferde tamamlandığını söylediği UI hareket dizisini paylaşıyor. Kayıt bu istek için üretilen görsel diziyi gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="Tek istemlik UI hareket dizisi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [SCP-8517 kurmaca animasyonu](https://x.com/eviljoker88/status/2106003621402005816) (üreten [@eviljoker88](https://x.com/eviljoker88))

**SCP esinli öncülü animasyon öyküsü tarifi olarak kullanın.**

Üretici, SCP-8517 temalı animasyonu sunup yapımını Fable 5.5'e atfediyor. Örnek, kurmaca anlatıyı ve görünen animasyonunu kapsıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="SCP-8517 kurmaca animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [Suluboya sonbahar animasyonu](https://x.com/ishuagra02/status/2106000055706784118) (üreten [@ishuagra02](https://x.com/ishuagra02))

**Animasyon için mevsimsel konu ve suluboya işlemesi belirleyin.**

Yazar, suluboya tarzında sonbahar animasyonu paylaşıyor. Kayıt mevsimsel bir konuyla belirli görsel ortamı birleştirmenin somut örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="Suluboya sonbahar animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [Prosedürel oyuncak bebek sahnesi](https://x.com/HelaliBillel/status/2105988689088196785) (üreten [@HelaliBillel](https://x.com/HelaliBillel))

**Bebek benzeri karakterin sahnede nasıl hareketlendirildiğini inceleyin.**

Yazar, prosedürel bebek sahnesi animasyonunu paylaşıp tartışmada Blender'dan söz ediyor. Örnek, görünen sahnelenmiş karakteri ve animasyonu kapsıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="Prosedürel oyuncak bebek sahnesi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [Tarayıcıda çizilen pelikan sürüşü](https://x.com/slimcat0101/status/2105988654636380444) (üreten [@slimcat0101](https://x.com/slimcat0101))

**Karakter hareketi çıktısını tarayıcıda çalıştırıp sahneyi inceleyin.**

Üretici, bisiklet süren pelikan isteyerek ortaya çıkan HTML'nin tarayıcıda çalışmasını kaydediyor. Bu, statik SVG çizimlerinden farklı hareketli bir tarayıcı sahnesi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="Tarayıcıda çizilen pelikan sürüşü" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [Evren kendine bakıyor](https://x.com/l_mejiaC/status/2105988529671360673) (üreten [@l_mejiaC](https://x.com/l_mejiaC))

**Uzak ölçekleri sürekli görsel yolculukla tek anlatıda birleştirin.**

Üretici, Büyük Patlama'dan insan gözüne uzanan kesintisiz dizi sunuyor. Yazar filmin görsellerinin ve müziğinin çalışma zamanı koduyla oluşturulduğunu anlatıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="Evren kendine bakıyor" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [Bağımsız jet animasyonu testi](https://x.com/AI_Screening/status/2105988448612135176) (üreten [@AI_Screening](https://x.com/AI_Screening))

**Uçak animasyonu görevini tekrarlayıp belirli çıktıyı inceleyin.**

Yazar, yönlendirme tartışmalarından sonra jet animasyonu görevini deneyip kendi sonucunu paylaşıyor. Kayıt, bu uçak örneği için bağımsız kaynak sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="Bağımsız jet animasyonu testi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [İlk serbest hareket gösterimi](https://x.com/Saccc_c/status/2105985484472377531) (üreten [@Saccc_c](https://x.com/Saccc_c))

**Kısa ve açık uçlu istemle hareket tasarımını araştırın.**

Üretici, tek istemle oluşturulduğunu söylediği ilk hareket tasarımı gösterimini paylaşıyor. Bu, sonraki on beş saniyelik portföyünden ayrı, daha eski bir çıktı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="İlk serbest hareket gösterimi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [Kodla çizilen uygarlık](https://x.com/ziwenxu_/status/2105983571848741045) (üreten [@ziwenxu_](https://x.com/ziwenxu_))

**Uygarlık tarihi tarifini kodlanmış animasyon anlatısına dönüştürün.**

Yazar, başlangıcından bugüne uygarlığı isteyip çıkan filmi paylaşıyor. Üretici bu kodlanmış görsel çalışmada hazır çekim veya stok varlık kullanmadığını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="Kodla çizilen uygarlık" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [Çipten sunucuya yakınlaşma karşılaştırması](https://x.com/SPAC89/status/2105968361725202591) (üreten [@SPAC89](https://x.com/SPAC89))

**Çipten sunucuya geçişte gerçekçiliği ve sürekliliği karşılaştırın.**

Yazar, Fable XHigh ve GPT Sol Ultra'nın gerçekçi yakınlaşma dizilerini karşılaştırıp hız ve kota kullanımını tartışıyor. Gönderi farklı abonelik düzeylerindeki belirli çalışmaları karşılaştırıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="Çipten sunucuya yakınlaşma karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [Ay yolculuğu animasyon projesi](https://x.com/IgorGomezC/status/2105963552024506565) (üreten [@IgorGomezC](https://x.com/IgorGomezC))

**Kişisel animasyon kavramını birden fazla kodlama modeliyle araştırın.**

Üretici, Fable ve Opus denemelerini tartışırken kişisel Ay yolculuğu animasyonunu paylaşıyor. Ekli eser, bu yaratıcı araştırmanın somut çıktısı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="Ay yolculuğu animasyon projesi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [Japon voksel sahnesi karşılaştırması](https://x.com/vikktorrrre/status/2105955048018588084) (üreten [@vikktorrrre](https://x.com/vikktorrrre))

**Aynı sahne istemiyle ayrıntıyı, sisi ve görsel netliği karşılaştırın.**

Yazar, aynı Japon voksel sahnesi isteminde güncel Fable ve Opus çıktılarını karşılaştırıyor. Gözlemler bu belirli sonuçların netliği, sisi ve estetik işlemesiyle ilgili.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="Japon voksel sahnesi karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [Steaming the Frontier kısa filmi](https://x.com/sdmat123/status/2105929299878703520) (üreten [@sdmat123](https://x.com/sdmat123))

**Görsel-işitsel kısa film için Steamboat tarzı tarifi sesle birleştirin.**

Üretici, sesli animasyon Steaming the Frontier'ı paylaşıyor. Diğer üreticilerin bağımsız Steamboat tarzı çıktılarından ayrı kaynak olarak tutuluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="Steaming the Frontier kısa filmi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [Farklı sanat tarzlarında Superman](https://x.com/Mr_Salio/status/2105925979466052051) (üreten [@Mr_Salio](https://x.com/Mr_Salio))

**Sürekli animasyonda aynı karakteri değişen sanat tarzları boyunca taşıyın.**

Üretici, önceki Superman örneğinin yeni üretimine ilham verdiğini söyleyip kendi sonucunu paylaşıyor. Farklı çizimler bunu yeniden paylaşım değil, ayrı yaratım yapıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="Farklı sanat tarzlarında Superman" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Cupcake tarzı bölüm sonu savaşı](https://x.com/maciejkrupowies/status/2105914965387321785) (üreten [@maciejkrupowies](https://x.com/maciejkrupowies))

**Yana kayan bölüm sonu savaşı prototipleyip oluşan çatışmayı inceleyin.**

Yazar, on dakikadan kısa sürede tek seferde ürettiğini söylediği Cupcake tarzı savaş prototipini paylaşıyor. Kayıt oyunun çatışma dizisini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Cupcake tarzı bölüm sonu savaşı" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [Değişen güneşle yelkenli sahnesi](https://x.com/popat_kunj/status/2105907935490752822) (üreten [@popat_kunj](https://x.com/popat_kunj))

**Gökyüzünü, suyu ve güneş konumunu bir yelken sahnesiyle araştırın.**

Üretici, güneşin farklı konumlarını içeren 3D yelkenli sahnesi ve etkileşimli eser bağlantısı paylaşıyor. Sahne gemi, gökyüzü ve suyu aynı görsel görevde birleştiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="Değişen güneşle yelkenli sahnesi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Paracortex ve Pi değişiklik videosu](https://x.com/RobIW_dev/status/2105894547796476225) (üreten [@RobIW_dev](https://x.com/RobIW_dev))

**Ürün güncellemelerini kısa hareketli duyuruya dönüştürün.**

Yazar, Paracortex ve Pi güncellemelerini yirmi beş saniyelik hareket tasarımı videosuna çevirip istemi gönderiye ekliyor. Eser görsel ürün iletişimi örneği.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Paracortex ve Pi değişiklik videosu" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Curio 2.0 site tanıtımı](https://x.com/voltwake/status/2105884775982485642) (üreten [@voltwake](https://x.com/voltwake))

**Mevcut site lansmanı çevresinde kodlanmış tanıtım filmi oluşturun.**

Üretici, Curio 2.0 tanıtımını kodlanmış görseller, kamera çalışması ve müzikle yaptığını anlatıyor. Gönderi sonuçtaki site tanıtım filmini paylaşıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Curio 2.0 site tanıtımı" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [Hayali Hugging Face 3D öyküsü](https://x.com/chetaslua/status/2105884276864782557) (üreten [@chetaslua](https://x.com/chetaslua))

**Kurmaca filmde model kodunu çizim ve ses araçlarıyla birleştirin.**

Üretici, modelin yazdığı kod, Blender ve ElevenLabs API ile hayali Hugging Face öyküsünü paylaşıyor. Blender yapım ve çizimi üstlenirken ElevenLabs harici ses sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="Hayali Hugging Face 3D öyküsü" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [JS Paint'te Claude for Chrome](https://x.com/BtwIUseSystemd/status/2105861662112923849) (üreten [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**Tarayıcı ajanına yalnızca uygulamanın araçlarını kullanacağı çizim görevi verin.**

Yazar, Claude for Chrome'dan yalnızca JS Paint araçlarıyla insan çizmesini isteyip sonucu paylaşıyor. Tarayıcı etkileşimi ve resim uygulaması görevin açık parçaları.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="JS Paint'te Claude for Chrome" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [Statik pelikan bisiklet SVG'si](https://x.com/olddonkeyblog/status/2105842745189556672) (üreten [@olddonkeyblog](https://x.com/olddonkeyblog))

**Ayrıntılı statik çizim için bağımsız SVG isteği kullanın.**

Üretici, bisiklet süren pelikanı tek, kendi kendine yeterli SVG olarak isteyip statik resmi paylaşıyor. Bu görev hareketli sürüş örneklerinden ayrı.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="Statik pelikan bisiklet SVG'si" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [Minecraft becerisiyle BlockBench MCP](https://x.com/TOPSTR1X/status/2105839618872738138) (üreten [@TOPSTR1X](https://x.com/TOPSTR1X))

**Oyun karakteri üretirken modelleme aracı ve üslup becerisi sağlayın.**

Yazar, BlockBench MCP ve özel Minecraft modelleme-renklendirme becerisi verip çıkan karakteri paylaşıyor. Bu araçlar ve üslup rehberi iş akışının açık girdileri.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="Minecraft becerisiyle BlockBench MCP" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [Tek HTML dosyasında Dig Dug](https://x.com/imjustnewatai/status/2105831117677084841) (üreten [@imjustnewatai](https://x.com/imjustnewatai))

**Küçük tarayıcı oyununu yeniden yaparken tek HTML teslimini hedefleyin.**

Üretici, Dig Dug'ın tek HTML dosyasında yeniden yapılmasını isteyip oyun kaydını paylaşıyor. Gönderi yapımın tek istemden geldiğini belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="Tek HTML dosyasında Dig Dug" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [Mekanik ahtapot SVG'si](https://x.com/SEO/status/2105812236774297943) (üreten [@SEO](https://x.com/SEO))

**SVG tasarımında ayrıntı ve hareketi mekanik yaratıkla inceleyin.**

Yazar, mekanik ayrıntıları bulunan hareketli ahtapot SVG'sini paylaşıyor. Kayıt küçük hareketli parçalar etrafında somut vektör tasarımı örneği sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="Mekanik ahtapot SVG'si" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [Sanat tarzlarında Humanity Walks](https://x.com/l_mejiaC/status/2105801379956850793) (üreten [@l_mejiaC](https://x.com/l_mejiaC))

**Sabit bir figürü tarihsel görsel tarzlar dizisi boyunca taşıyın.**

İlk üretici, yaklaşık yetmiş dört saniyede yirmi sanat paneli boyunca kesintisiz yürüyüş sunup müziğin kodlandığını söylüyor. Her sınır karakteri ve sahneyi farklı tarza geçiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="Sanat tarzlarında Humanity Walks" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [Açık uçlu kara delik sahnesi](https://x.com/rohit3a/status/2105786053412208835) (üreten [@rohit3a](https://x.com/rohit3a))

**Kara delik görselleştirmesini açık uçlu yaratıcı tarifle araştırın.**

Üretici, modelin kendisini etkilemek için ne yapacağını sorup kara delik sahnesini paylaşıyor. Görev, önceden belirlenmiş arayüz kurulumundan ziyade serbest görsel keşif.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="Açık uçlu kara delik sahnesi" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [Kutup ışıklı denizanası animasyonu karşılaştırması](https://x.com/SPAC89/status/2105783511433318451) (üreten [@SPAC89](https://x.com/SPAC89))

**İki denizanası animasyonunda biçim değişimini ve hareketi karşılaştırın.**

Yazar, Fable XHigh ile GPT Sol Ultra'yı kutup ışıklı denizanası animasyonunda karşılaştırıp kota kullanımını tartışıyor. Sonuçlar farklı abonelik düzeylerinden geliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="Kutup ışıklı denizanası animasyonu karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Nintendo Switch takılma ve açılış SVG'si](https://x.com/ishuagra02/status/2105779174921359470) (üreten [@ishuagra02](https://x.com/ishuagra02))

**Kumanda hareketini ve açılış dizisini aynı SVG animasyonunda birleştirin.**

Üretici, kumandaların yerine oturmasını açılış logosunun izlediği Nintendo Switch SVG'sini paylaşıyor. Bu çalışma için bir dakika otuz dokuz saniye ve 1,34 dolar maliyet bildiriliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Nintendo Switch takılma ve açılış SVG'si" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [The Loom etkileşimli 3D sahnesi](https://x.com/Mr_Salio/status/2105774088492916757) (üreten [@Mr_Salio](https://x.com/Mr_Salio))

**Arazi ve binaları tek etkileşimli 3D sayfa olarak araştırın.**

Yazar, binalar ve araziden oluşan The Loom etkileşimli sahnesini sunuyor. Kayıt, üreticinin testindeki somut sayfa çıktısını sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="The Loom etkileşimli 3D sahnesi" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [Aynı İstemle Hazırlanan Hareketli Tasarım Videoları](https://x.com/mesmerlord/status/2105758042830549235) (üreten [@mesmerlord](https://x.com/mesmerlord))

**Aynı istemden üretilen iki hareketli tasarım videosunda görsel odağı ve ritim uyumunu karşılaştırın.**

Yazar, aynı istemle elde edilen iki erken Fable 5.5 hareketli tasarım sonucunu paylaşıyor ve bir Opus denemesine göre daha belirgin odak ve daha iyi ritim uyumu gözlemlediğini ihtiyatla belirtiyor. Her iki özgün kaynak video birlikte sunuluyor.

```
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

[@shneural](https://x.com/shneural/status/2103151003272962130)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="Aynı İstemle Hazırlanan Hareketli Tasarım Videoları" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29b80ef5ba92b029630a1628.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0da5945bc240b424bfebbd9.jpg" alt="Aynı İstemle Hazırlanan Hareketli Tasarım Videoları" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [Daha temiz ama daha sığ manzara](https://x.com/eviljoker88/status/2105755840175034447) (üreten [@eviljoker88](https://x.com/eviljoker88))

**Üretilmiş sahneleri karşılaştırırken olumsuz estetik geri bildirimi koruyun.**

Yazar, yan yana Japon sahnesi karşılaştırmasında diğer sonucun daha temiz görünmesine rağmen Opus çıktısının derinliğini tercih ediyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="Daha temiz ama daha sığ manzara" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [Japon sahnelerinde karışık sonuçlar](https://x.com/eviljoker88/status/2105755408342126936) (üreten [@eviljoker88](https://x.com/eviljoker88))

**İlk karşılaştırmayı kesin galip saymak yerine karışık geri bildirimi kaydedin.**

Yazar, ilk Japon sahnesi karşılaştırmasını paylaşıp sonuçları karışık diye tanımlıyor. Görüntü, bu estetik geri bildirimin arkasındaki somut çıktıları koruyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="Japon sahnelerinde karışık sonuçlar" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [Kumanda SVG karşılaştırmaları](https://x.com/notjazii/status/2105751542498464169) (üreten [@notjazii](https://x.com/notjazii))

**Benzer görsel görev altında önceki ve sonraki kumanda çizimlerini karşılaştırın.**

Yazar, önce-sonra kumanda SVG çıktılarını karşılaştırma görüntüsünde sunuyor. Örnek, genel model sıralaması değil, çizim ve sunumdaki görünen değişikliklerle ilgili.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="Kumanda SVG karşılaştırmaları" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [Endüstriyel cihaz sahnesi](https://x.com/RayaneRachid_/status/2105744517735354410) (üreten [@RayaneRachid_](https://x.com/RayaneRachid_))

**Mekanik cihazı odaklı 3D sahne tasarımı görevi olarak kullanın.**

Üretici, en iyi tek seferlik sonucu diye tanımladığı 3D endüstriyel cihaz sahnesini paylaşıyor. Görsel mekanik kompozisyon için somut referans sağlıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="Endüstriyel cihaz sahnesi" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [Dev kabuklu solungaçlı böcek yeniden yapımı](https://x.com/Josh67Joshua/status/2105739832563769697) (üreten [@Josh67Joshua](https://x.com/Josh67Joshua))

**İki istemlik yeniden yapımı belirli yaratık tarifiyle araştırın.**

Yazar, iki istemle elde ettiğini söylediği dev kabuklu solungaçlı böcek çizimini paylaşıyor. Görsel yaratık tasarımı görevinin çıktısını gösteriyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="Dev kabuklu solungaçlı böcek yeniden yapımı" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [İki istemde GameCube kumandası](https://x.com/marmaduke091/status/2105735266032095349) (üreten [@marmaduke091](https://x.com/marmaduke091))

**Tanıdık kumandayla iki istemli çizim sonucunu inceleyin.**

Yazar, iki istem kullandığını söyleyerek GameCube kumandası çizimini paylaşıyor. Bu statik kumanda görüntüsü Xbox ve diğer kumanda gösterimlerinden farklı.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="İki istemde GameCube kumandası" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [X gönderisi için düzenlenen ekran görüntüsü](https://x.com/chetaslua/status/2105733677003292983) (üreten [@chetaslua](https://x.com/chetaslua))

**Asistanın ekran görüntüsünü sosyal gönderiye nasıl uyarladığını inceleyin.**

Üretici, X gönderisi için hazırlanan ekran düzenlemesini paylaşarak asistanın açık istek olmadan yaptığını söylüyor. Ekli görüntü görünen sonuç.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="X gönderisi için düzenlenen ekran görüntüsü" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [Voksel sakurada önce ve sonra](https://x.com/kdnbmb/status/2105704791049412755) (üreten [@kdnbmb](https://x.com/kdnbmb))

**Aynı görsel konuda ardışık voksel sahnesi çıktılarını karşılaştırın.**

Paylaşımcı, voksel sakura adasının iki sürümünü paylaşıyor. Yan yana görüntü, sahnenin görünen önce-sonra tasarım farklarını kaydediyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="Voksel sakurada önce ve sonra" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [SHADERKIN kumaş arayüzü prototipi](https://x.com/mszzz0011/status/2106025576972853642) (üreten [@mszzz0011](https://x.com/mszzz0011))

**Arayüz prototipinde kumaş efektlerini ayarlanabilir kontrollerle birlikte araştırın.**

Yazar, tek seferlik yapım diye tanımladığı kumaş efektli ve parametre kontrollü SHADERKIN prototipini paylaşıyor. Kayıt ortaya çıkan arayüzü ve hareketi gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="SHADERKIN kumaş arayüzü prototipi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [Paylaşılan altın saat arayüzü animasyonu](https://x.com/AISuperDomain/status/2106396754539360272) (üreten [@AISuperDomain](https://x.com/AISuperDomain))

**Saat temalı animasyonu arayüz kompozisyonuna referans olarak kullanın.**

Paylaşımcı altın saat temalı ön yüz animasyonu sunuyor. Klip, arayüz kompozisyonunu, saat motifini ve hareketli görsel sunumu incelemeye ortak referans veriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="Paylaşılan altın saat arayüzü animasyonu" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [Before There Was Anything anlatısı](https://x.com/crowqnt/status/2106146218846081435) (üreten [@crowqnt](https://x.com/crowqnt))

**Paylaşılan animasyon filminde kozmik ve insani anlatıyı araştırın.**

Paylaşımcı, evren ve insanlık hakkındaki Before There Was Anything anlatı videosunu sunuyor. Film, paylaşılan görsel hikâye örneği olarak tutuluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="Before There Was Anything anlatısı" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [Paylaşılan mavi parçacık girdabı](https://x.com/AISuperDomain/status/2105846981776003107) (üreten [@AISuperDomain](https://x.com/AISuperDomain))

**Paylaşılan girdap görselleştirmesinde parçacık hareketini ve kompozisyonu inceleyin.**

Paylaşımcı mavi parçacıklı girdap animasyonunu sunuyor. Klip parçacık hareketi, görsel yapı ve kompozisyon incelemesi için somut örnek sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="Paylaşılan mavi parçacık girdabı" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [İki revizyondan sonra çok panelli arayüz](https://x.com/ZorroOfMorocco/status/2106547078235095485) (üreten [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**İlk çıktıda durmak yerine görsel arayüzü revizyonlarla geliştirin.**

Yazar, yaklaşık üç saat ve iki revizyonla tamamladığını söylediği çok panelli arayüzü paylaşıyor. Ekran görüntüsü son görsel tasarımı gösteriyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="İki revizyondan sonra çok panelli arayüz" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [Çizilmiş sahnede üst üste hayvanlar](https://x.com/legit_api/status/2117237103289315574) (üreten [@legit_api](https://x.com/legit_api))

**Statik kompozisyonun farklı karakterleri ve malzemeleri nasıl dengelediğini inceleyin.**

Gönderi ayı, panda ve kutup ayısının üst üste durduğu sahneyi paylaşıyor; Discord'daki yuruzuu'yu kaynak gösterip yirmi bir dakika çalışma bildiriyor. Kamuya açık gönderi, paylaşılan görselin kaynağı olarak tutuluyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="Çizilmiş sahnede üst üste hayvanlar" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [Dört açık dünya RPG denemesi](https://x.com/noclipepe/status/2117222592536789149) (üreten [@noclipepe](https://x.com/noclipepe))

**Aynı yaratıcı görevde oyun sunumunu, çatışmayı ve çarpışmaları karşılaştırın.**

Üretici, Fable 5.5, GPT-6.2 Astra, Opus 5.5 ve Fable 5.1 etiketli dört tek-istem RPG denemesi sunuyor. Işık, çatışma, envanter, çarpışmalar ve karakterin takılması yorumlanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="Dört açık dünya RPG denemesi" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [İki ön yüz animasyon klibi](https://x.com/leo114119/status/2117209849842761983) (üreten [@leo114119](https://x.com/leo114119))

**Sahnelerin tasarımını ve görsel ayrıntısını klipleri birlikte izleyerek karşılaştırın.**

Gönderi Astra ve Fable etiketli kod animasyonlarını ayrıntı ve senaryo tasarımı açısından yan yana koyuyor. Fable animasyonunun kaynağı olarak @chetaslua açıkça belirtiliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="İki ön yüz animasyon klibi" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [Kodla üretilmiş yosun robot filmi](https://x.com/chetaslua/status/2117169796290916732) (üreten [@chetaslua](https://x.com/chetaslua))

**Kodla kurulan tamamlanmış sinematik sahneyi animasyon tarifiyle araştırın.**

Üretici, orman ve robot animasyonunu tek seferlik kod filmi diye paylaşıyor. Gönderi okuyucuyu ekran görüntüsündeki isteme yönlendirip sonucu diğer denemelerle karşılaştırıyor.

Ek bir gönderi, ayrı olarak bildirilen bir Opus 5.5 kontrol çalışmasını gösteriyor. [@AnikaCodes](https://x.com/AnikaCodes) · [İlgili çalışma](https://x.com/AnikaCodes/status/2117222374642946297)

Yazarına göre ilgili bir GPT-6 Astra Max çalışması, iş akışında üretilmiş görseller kullanıyor. Böylece farklı üretim yöntemleri özgün filmin yanında görünür kalıyor. [@rubenssoto_ai](https://x.com/rubenssoto_ai) · [İlgili karşılaştırma](https://x.com/rubenssoto_ai/status/2117707344704352691)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="Kodla üretilmiş yosun robot filmi" width="760"></a></td><td valign="top"><p>Ek bir gönderi, ayrı olarak bildirilen bir Opus 5.5 kontrol çalışmasını gösteriyor.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="Kodla üretilmiş yosun robot filmi" width="760"></a></td><td valign="top"><p>GPT-6 Astra Max</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/25b0cfcdb1fdda22ba6aa9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/75f37c74099d5b9ba1ad0ddc.jpg" alt="GPT-6 Astra Max" width="760"></a></td></tr></table>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [Konteyner limanı simülasyonunu yeniden ele almak](https://x.com/anxuanng/status/2117124831279972812) (üreten [@anxuanng](https://x.com/anxuanng))

**Görsel karşılaştırma için proje bağlamını koruyarak eski sahneyi yeniden çalışın.**

Yazar başka konteyner limanı sahnesi sunup önceki Blender ve Three.js simülasyonunu alıntılıyor. Önceki projedeki vinçler, gemiler, araçlar ve konteynerler strateji benzeri ortam için modellenmişti.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="Konteyner limanı simülasyonunu yeniden ele almak" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [Havaalanı apronunu yeniden ele almak](https://x.com/anxuanng/status/2117096574878921119) (üreten [@anxuanng](https://x.com/anxuanng))

**Düzeltilmiş havaalanı sahnesini önceki proje ve varlık iş akışıyla karşılaştırın.**

Yazar, önceki Blender ve Three.js simülasyonunu alıntılayarak havaalanı apronuna dönüyor. Uçaklar, hizmet araçları ve terminal altyapısının yeni kaydını paylaşıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="Havaalanı apronunu yeniden ele almak" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [Soyut 3D dünyalarda pelikan sürüşü](https://x.com/xiax0603/status/2116960224829665543) (üreten [@xiax0603](https://x.com/xiax0603))

**Farklı mekânlar arasındaki geçişleri bisiklet konusu üzerinden inceleyin.**

Gönderi, geometrik parçalar ve soyut dijital ortamdan geçip bir gözden uzaklaşan pelikan-bisiklet animasyonu sunuyor. Dizi, farklı sahne geçişlerinin somut gösterimi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="Soyut 3D dünyalarda pelikan sürüşü" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [Tarihsel yelkenli sahnesi](https://x.com/abhinavflac/status/2116945827738665060) (üreten [@abhinavflac](https://x.com/abhinavflac))

**Gemi sahnesinde suyu, ışığı ve çevresel kompozisyonu inceleyin.**

Gönderi tarihsel yelkenli sahnesini etkileşimli, sıfır örnekli çıktı diye paylaşıyor. Kayıt gemi ve çevresindeki suyun somut görsel örneğini sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="Tarihsel yelkenli sahnesi" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [Carbon ile sürüş ve yürüyüş karşılaştırması](https://x.com/AI_Screening/status/2116934172757660014) (üreten [@AI_Screening](https://x.com/AI_Screening))

**Karakter hareketini ve sahne kurulumunu eşlenmiş görsellerle karşılaştırın.**

Yazar, Fable ve Carbon etiketli bisikletçi ve zebra örneklerini bileşik videoda sunuyor. Kontrol noktalarını yakın bulduğunu söylüyor; eşlenmiş görüntüler belirli hareket örneklerini inceletiyor.

Daha önce tek başına yayımlanan bisikletçi karşılaştırması, birleşik videonun yanında yer alıyor. [@AI_Screening](https://x.com/AI_Screening) · [İlgili çalışma](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="Carbon ile sürüş ve yürüyüş karşılaştırması" width="760"></a></td><td valign="top"><p>Daha önce tek başına yayımlanan bisikletçi karşılaştırması, birleşik videonun yanında yer alıyor.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="Carbon ile sürüş ve yürüyüş karşılaştırması" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [Meşrubat şişesi sunumu](https://x.com/abhinavflac/status/2116919086521499730) (üreten [@abhinavflac](https://x.com/abhinavflac))

**Kısa ürün çizimi klibiyle malzemeyi, biçimi ve sunumu inceleyin.**

Gönderi, tek seferlik yönlendirme çıktısı diye tanımlanan meşrubat şişesi sunumunu paylaşıyor. Görünen şişe korunuyor; açıklamadaki tutarsız marka adı benimsenmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="Meşrubat şişesi sunumu" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [Astra ile pelikan hareketi karşılaştırması](https://x.com/Octoberry/status/2116918967558095131) (üreten [@Octoberry](https://x.com/Octoberry))

**Eşlenmiş pelikan kliplerinde gerçekçilik, renk ve hareket seçimlerini karşılaştırın.**

Paylaşımcı, Fable ve Astra etiketli pelikan sahnelerini yan yana getirip gerçekçiliklerini ve renklerini yorumluyor. Karşılaştırma kaydı iki görsel yaklaşımı birlikte koruyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="Astra ile pelikan hareketi karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [Kod animasyonları için hareket tasarımı tarifi](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (üreten [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**Animasyonlu başlık veya ürün açılışı isterken somut tasarım tarifinden başlayın.**

Gönderi; açılış, hareketli logo, başlık ve 3D sahneler için hareket tasarımı tarifi ekran görüntüsü sunup Claude ile kullanılmasını öneriyor. Kaynak görsel talimatları koruyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="Kod animasyonları için hareket tasarımı tarifi" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [Fotoğraf referansından voksel portre](https://x.com/chetaslua/status/2116912822806520027) (üreten [@chetaslua](https://x.com/chetaslua))

**Voksel portrenin referans fotoğraftaki tanınabilir özellikleri nasıl koruduğunu inceleyin.**

Üretici, Sam Altman fotoğrafını voksel portreyle eşleştirip sonucu tek seferlik çıktı diye tanımlıyor. Yan yana görsel referansı ve yorumu birlikte sunuyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="Fotoğraf referansından voksel portre" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [Opus ile uçan pelikan sahneleri](https://x.com/leo114119/status/2116901575490929109) (üreten [@leo114119](https://x.com/leo114119))

**Eğlenceli nesne düzeniyle kompozisyon ve animasyon seçimlerini karşılaştırın.**

Gönderi uçan pelikan üstündeki bisiklet sahnesinin Fable ve Opus kliplerini üst üste sunuyor. Bileşik görüntü Fable klibini @notjazii'ye atfedip iki yaklaşımı görünür tutuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="Opus ile uçan pelikan sahneleri" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [Morning Ride pelikan internet sahnesi](https://x.com/leo114119/status/2116893571739775220) (üreten [@leo114119](https://x.com/leo114119))

**Sahil sürüşünde karakter ayrıntısını ve çevresindeki sayfa sunumunu inceleyin.**

Yazar, Morning Ride sayfasındaki 3D pelikan sürüş sahnesini paylaşarak tüylere, ayaklara, bisiklet ayrıntılarına ve sahil arka planına dikkat çekiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="Morning Ride pelikan internet sahnesi" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [Aynı istemle farklı tarzlarda sahneler](https://x.com/notjazii/status/2116893197939224714) (üreten [@notjazii](https://x.com/notjazii))

**Her modelin tarzını seçmesine izin verip çıkan kompozisyonları karşılaştırın.**

Yazar, aynı istemle iki modeli test ederken her birinin görsel tarzını seçmesine izin verdiğini bildiriyor. Video farklı kompozisyonları ve ayrıntı düzeylerini yan yana koyuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="Aynı istemle farklı tarzlarda sahneler" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [Pelikan, bisiklet ve at kompozisyonu](https://x.com/abhinavflac/status/2116881397986288017) (üreten [@abhinavflac](https://x.com/abhinavflac))

**Animasyonun birkaç etkileşen özneyi aynı sahneye nasıl yerleştirdiğini sınayın.**

Gönderi, altından at koşarken bisikletle uçan pelikanı paylaşıyor. Klip bu alışılmadık çok nesneli kompozisyonun ve hareketin somut örneğini sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="Pelikan, bisiklet ve at kompozisyonu" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [Referans gönderiden izometrik sahne](https://x.com/chetaslua/status/2116878661035106515) (üreten [@chetaslua](https://x.com/chetaslua))

**Genel örneği yeniden kurmak yerine yeni sahneyi verilen referansla yönlendirin.**

Üretici yalnızca alıntılanmış Post Humans gönderisini referans aldığını söyleyip çıkan izometrik sahneyi paylaşıyor. Klip mevsim kontrolü bulunan çiftlik benzeri kompozisyon sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="Referans gönderiden izometrik sahne" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [Pelikan bisikletinin mekanik yakın planları](https://x.com/NFT_Chen/status/2116869725703782507) (üreten [@NFT_Chen](https://x.com/NFT_Chen))

**Bisikletli öznede aynakol hareketini, tüyleri ve kamera hareketini inceleyin.**

Gönderi, su kenarında bisiklet süren pelikanın yakın planlarını paylaşıyor. Kayıt bisiklet mekaniği, kuşun başı ve daha geniş iskele sürüşü arasında geçiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="Pelikan bisikletinin mekanik yakın planları" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [Pelikanın üstünde giden bisiklet](https://x.com/notjazii/status/2116861637890379891) (üreten [@notjazii](https://x.com/notjazii))

**Animasyonun mekânsal kompozisyonunu sınamak için özne ilişkisini ters çevirin.**

Üretici, pelikan üstünde bisiklet animasyonunu paylaşıyor. Klip bisikleti uçan kuşun üzerine koyarak alışılmış bisiklet süren pelikan görevine bir çeşitleme getiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="Pelikanın üstünde giden bisiklet" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [Carbon ile pelikan SVG tarzları](https://x.com/leo114119/status/2116652334734332212) (üreten [@leo114119](https://x.com/leo114119))

**Farklı estetikleri tek evrensel sıralama saymadan gerçekçiliği ve çizim tarzını karşılaştırın.**

Gönderi Carbon ve Fable pelikan-bisiklet çıktılarını birlikte sunuyor. Yazar çizgi roman tarzını gerçekçi işlemeyle karşılaştırıp tarz farkının kıyası zorlaştırdığını belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="Carbon ile pelikan SVG tarzları" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [Çizgi mavi kuş bisiklet sahnesi](https://x.com/birdabo/status/2116553049183560012) (üreten [@birdabo](https://x.com/birdabo))

**Tanıdık çizgi karakterin bisiklet kompozisyonundaki çizimini inceleyin.**

Gönderi, sahilde bisiklet süren mavi çizgi kuşu Fable 5.5 Max açıklamasıyla paylaşıyor. Görüntü somut statik görsel örnek olarak tutuluyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="Çizgi mavi kuş bisiklet sahnesi" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [Orman yolunda pelikan sürüşü](https://x.com/leo114119/status/2116154940364374269) (üreten [@leo114119](https://x.com/leo114119))

**Tarayıcı sahnesinde tüyleri, ayakları ve bisiklet geometrisini inceleyin.**

Paylaşımcı, orman yolunda bisiklet süren pelikanın tarayıcı ekran görüntüsünde tüy dokusuna, ayaklara ve bisiklet ayrıntısına dikkat çekiyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="Orman yolunda pelikan sürüşü" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [Carbon ile çöp adam çatışması](https://x.com/leo114119/status/2116084152986656933) (üreten [@leo114119](https://x.com/leo114119))

**Eşlenmiş animasyon örneklerinde dövüş düzenini ve hareketi karşılaştırın.**

Karşılaştırma kaydı Fable 5.1 High ve Carbon etiketlerini taşıyor. Yazar çöp adam dövüş animasyonunun göreli kalitesini tartışıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="Carbon ile çöp adam çatışması" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [Erken testlerden pelikan SVG referansı](https://x.com/ChrisGPT/status/2115872567122608591) (üreten [@ChrisGPT](https://x.com/ChrisGPT))

**Tarz ve bisiklet geometrisini incelerken bağlantılı referansı koruyun.**

Paylaşımcı pelikan-bisiklet görselini öne çıkarıp sonuçları Discord'daki kostikz'ye atfeden erken test gönderisini alıntılıyor. Referans görseli ve atıf zinciri korunuyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="Erken testlerden pelikan SVG referansı" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [Modeller arası SVG testinde pelikan referansı](https://x.com/AdamHoltererer/status/2115858542221492300) (üreten [@AdamHoltererer](https://x.com/AdamHoltererer))

**Fable referansını çevresindeki SVG test bağlamıyla birlikte tutun.**

Paylaşımcı, Mistral Large 4 SVG test dizisinin altına Fable referansı olarak pelikan-bisiklet görseli ekliyor. Bu, modeller arası görsel inceleme için kaynaklı referans sağlıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="Modeller arası SVG testinde pelikan referansı" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [Carbon ile bisiklet SVG ayrıntıları](https://x.com/insanekrishnaa/status/2115833723342250186) (üreten [@insanekrishnaa](https://x.com/insanekrishnaa))

**Sepet, arka plan ve tüy dokusu gibi tekil özellikleri karşılaştırın.**

Gönderi Fable ve Carbon pelikan-bisiklet resimlerinde sepet tasarımını, arka plan ayrıntısını ve tüy dokusunu tartışıyor. Geniş görev kümesi yerine belirli görsel inceleme sunuyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="Carbon ile bisiklet SVG ayrıntıları" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [3D kanyon yerleşimi](https://x.com/Mr_Salio/status/2115813400915714177) (üreten [@Mr_Salio](https://x.com/Mr_Salio))

**Çevre ayrıntısını ve mekânsal kompozisyonu yerleşim sahnesiyle inceleyin.**

Gönderi geniş kanyon yerleşimini yeni Claude kontrol noktası gösterimi olarak paylaşıyor. Kayıt görünen binaları, araziyi ve sahne kompozisyonunu sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="3D kanyon yerleşimi" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [Opus ile kumanda ayrıntıları](https://x.com/notjazii/status/2115808169075351632) (üreten [@notjazii](https://x.com/notjazii))

**Eşlenmiş kumanda çizimlerinde biçimi, kontrolleri ve ayrıntı düzeyini inceleyin.**

Yazar, Fable ve Opus etiketli kumandaları birlikte paylaşarak üstteki çizimde ayrıntının fazlalığını vurguluyor. Eşlenmiş görüntü karşılaştırmayı koruyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="Opus ile kumanda ayrıntıları" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [Haftalık site SEO denetimi](https://x.com/cleeeeeeeeement/status/2115488774423773267) (üreten [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**Siteyi öncelikli SEO planına ve tekrarlanan sıralama incelemesine dönüştürün.**

Üretici, site alıp rakipleri ve anahtar sözcükleri belirleyen, öncelikli SEO eylem planı üreten sistem kurduğunu bildiriyor. Kısa kayıt haftalık sıralama takibi ve uygulama anlatımına eşlik ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="Haftalık site SEO denetimi" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [Opus hareket tasarımında Fable varlıkları](https://x.com/chetaslua/status/2115145163542790170) (üreten [@chetaslua](https://x.com/chetaslua))

**Model ve araçları birleştirirken varlık üretimini hareket tasarımı birleştirmesinden ayırın.**

Üretici, Fable'ın önceden ürettiğini söylediği varlıkları kullanan Opus 5.5 Tesla Roadster tasarımını paylaşıyor. Alıntılanan önceki akış Blender'da Python, ElevenLabs ve verilen tanıtım videosunu belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="Opus hareket tasarımında Fable varlıkları" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [Mandala ve geometrik biçim uygulaması](https://x.com/ZMinimalistYogi/status/2114600083165434189) (üreten [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**Odaklı geometri fikrini yaratıcı keşfe uygun etkileşimli uygulamaya dönüştürün.**

Üretici, Fable 5.1 ile üç saat konuşarak mandala, zome, Arşimet katıları ve lotus biçimli geometrik yantralar uygulaması yaptığını, ardından kişisel sitesinde paylaştığını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="Mandala ve geometrik biçim uygulaması" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Three.js ile bisikletli](https://x.com/AI_Screening/status/2114266369248354357) (üreten [@AI_Screening](https://x.com/AI_Screening))

**Bisiklet sahnesinde sürücü duruşunu, geometriyi ve eşgüdümlü hareketi inceleyin.**

Üretici, Three.js bisikletli çıktısını paylaşıyor. Kayıt sürücünün çevresindeki köprü ve sahil manzarasıyla somut hareket örneği sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Three.js ile bisikletli" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [FrontierCS 2 değerlendirmesinin anlık görünümü](https://x.com/wenhaocha1/status/2115613415641354262) (üreten [@wenhaocha1](https://x.com/wenhaocha1))

**Fable 5.1’i diğer modellerle karşılaştırmak için kaynağına bağlantı verilen bir kıyaslama grafiği kullanın.**

Yazar, Fable 5.1’i FrontierCS 2 görev geçme oranları grafiğine ekliyor ve bildirilen sonuçları diğer modellerin sonuçlarıyla birlikte paylaşıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="FrontierCS 2 değerlendirmesinin anlık görünümü" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [Üç modelin zebra animasyonlarının karşılaştırması](https://x.com/AI_Screening/status/2115849659797373038) (üreten [@AI_Screening](https://x.com/AI_Screening))

**Dört nala koşan zebra görevini, model adlarıyla birlikte gösterilen üç çıktıyı yan yana inceleyerek karşılaştırın.**

Yazar, Fable 5.5, Opus 5.5 ve Gemini 4 Argon etiketli zebra animasyonlarını yan yana sunuyor. Paylaşılan görüntüler, üç çıktının koşu hareketlerinden somut örnekler sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="Üç modelin zebra animasyonlarının karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [Uzun Japonca metni eleştirmek](https://x.com/AM09_21/status/2106670042184356156) (üreten [@AM09_21](https://x.com/AM09_21))

**Modelden üretilmiş Japonca metindeki okunabilirlik sorunlarını teşhis etmesini isteyin.**

Yazar, Opus'un uzun Japonca metninin neden zor okunduğunu sorduğunu bildiriyor. Yanıt, İngilizceye benzeyen sözdizimi, tekrarlar ve yüzeysel düzeltmeleri belirleyerek somut bir metin eleştirisi süreci oluşturuyor.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [Örneklerle yönlendirilen teknik PowerPoint](https://x.com/mt_moco/status/2106665038375522791) (üreten [@mt_moco](https://x.com/mt_moco))

**Teknik sunum istemeden önce örnekler verin.**

Yazar, birkaç örnek sunum sağlamanın kullanılabilir bir teknik PowerPoint getirdiğini söylüyor. Deneyim, örneklerle yönlendirmeyi belirli bir sunum görevinde daha iyi belge yapısıyla ilişkilendiriyor.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [Müzikal bütünlüğü karşılaştırmak](https://x.com/AM09_21/status/2106573080214770011) (üreten [@AM09_21](https://x.com/AM09_21))

**Üretilmiş müziği değerlendirirken yerel ayrıntıları ve bütünsel tutarlılığı ayrı karşılaştırın.**

Yazar, model bestelerini nota, melodi ve geçişler üzerinden karşılaştırarak yerel tutarlılığı daha geniş müzik yapısından ayırıyor. Anlatı, dinlemeye dayalı bir beste kalitesi değerlendirmesi.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [Erken tamamlanma ve daha zayıf tasarımlar](https://x.com/johntitorIII/status/2106442876506747353) (üreten [@johntitorIII](https://x.com/johntitorIII))

**Ajanın tamamlanma bildirimini kabul etmeden çıktıları görev koşullarıyla karşılaştırın.**

Yazar, birkaç günlük testte bitmeyen görevlerin tamamlandı işaretlendiğini ve tasarımların diğer modellerden zayıf kaldığını bildiriyor. Erken bitirme ve tasarım kalitesi, pratik başarısızlık biçimleri olarak kaydediliyor.

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [Rahatsız edici kalamar sanatı](https://x.com/hanawo_neki/status/2106271036094415186) (üreten [@hanawo_neki](https://x.com/hanawo_neki))

**Açık uçlu sanat isteği istenmeyen tarz getirdiğinde estetik tercihleri belirtin.**

Yazar, herhangi bir kalamar sanat eseri isteyince rahatsız edici, sık kümelenmiş ayrıntılar aldığını söylüyor. Anlatı, açık uçlu görsel istekte bir estetik uyuşmazlığı kaydediyor.

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [Teknik çizim tarzı hareket tasarımı](https://x.com/DavidayoAI/status/2106054662063325638) (üreten [@DavidayoAI](https://x.com/DavidayoAI))

**Hızlı animasyonun görsel yönü olarak teknik çizim estetiği kullanın.**

Yazar, hızlı animasyon isteğinden yaklaşık on beş dakika sonra teknik çizim tarzı sonuç aldığını bildiriyor. Eserin tamamı YouTube üzerinden bağlantılanıyor.

[İlgili çalışma](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [Voksel sakurada kuşlar ve balıklar](https://x.com/xodud_rkd/status/2105876716472447046) (üreten [@xodud_rkd](https://x.com/xodud_rkd))

**Voksel arazide hareketli yaban hayatını araştırın.**

Yazar, hareketli kuşlar ve havuzdaki balıkları içeren voksel sakura sahnesini anlatıp etkileşimli esere bağlantı veriyor. Paylaşılan sayfa bu sahnenin çıktısı.

[İlgili çalışma](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [Karakter üretiminde başarısızlık bildirimi](https://x.com/doof1789559/status/2105874208458752227) (üreten [@doof1789559](https://x.com/doof1789559))

**Başarılı görsel örneklerin yanında olumsuz karakter üretimi deneyimlerini kaydedin.**

Yazar, kötü karakter üretimi sonuçlarını bildirip kendi yaklaşımının da sorumlu olabileceğini açıkça kabul ediyor. Gönderi karakter görevlerini değerlendiren okurlar için belirli bir olumsuz deneyimi koruyor.

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [Süre ve maliyet notlu pelikan SVG'si](https://x.com/AnonymerNutze12/status/2105740440385499295) (üreten [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**Çizim eserini üreticinin süre ve maliyet gözlemleriyle eşleştirin.**

Yazar, pelikan SVG HTML eserine bağlantı verip denemenin süresini ve maliyetini bildiriyor. Bağlantılı eser gönderinin işaret ettiği somut çıktı.

[İlgili çalışma](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [Telefonla uzaktan Claude Code sürüleri](https://x.com/beistnormie/status/2106546741000417781) (üreten [@beistnormie](https://x.com/beistnormie))

**Kodlama ajanı sürülerini telefon üzerinden uzaktan denetlemeyi araştırın.**

Yazar, seyahat sırasında telefonla Claude Code sürülerini uzaktan yönettiğini bildiriyor. Gönderi proje eğitimi veya uygulama anlatımı değil, kişisel iş akışı deneyimi sağlıyor.

Type: Integration | Date: 2026-10-04

---

<a id="case-280"></a>
### Case 280: [Bir Alp Gölünün Üzerinde Samanyolu](https://x.com/hakmgpt/status/2118178083983573492) (üreten [@hakmgpt](https://x.com/hakmgpt))

**Dağ yansımalarıyla hareketli gece göğünü birleştiren uzun bir kamera dizisini inceleyin.**

Paylaşılan 92 saniyelik animasyon, bir Alp gölünden parlak Samanyolu’na geçiyor ve yeniden gökyüzünün yansımasına dönüyor. Paylaşımı yapan hesap, işlenen sahneyi Fable 5.5’e atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5cb879d0a07a0f6e9fff5cf6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/91432c6827d650eb28f2269b.jpg" alt="Bir Alp Gölünün Üzerinde Samanyolu" width="760"></a>

Type: Demo | Date: 2026-11-05

---

<a id="case-281"></a>
### Case 281: [İşlemsel Su ve Sesle Balina Sıçrayışı](https://x.com/camperaigg/status/2118069524306284556) (üreten [@camperaigg](https://x.com/camperaigg))

**Su altı çekimlerini, yüzeyden sıçrayışı ve sentezlenmiş sesi tek bir animasyon dizisinde birleştirin.**

Üretici; işlemsel bir balina, akışkan simülasyonu, okyanus gölgelendirmesi ve sentezlenmiş ses içeren 31 saniyelik film için 154 dakika harcadığını bildiriyor. Notlarında büyütülmüş kareleri inceleyip yeniden işlemeye başlamadan önce su sıçramalarını düzelttiğini anlatıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b98c309a3c226bd24386940f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1bcb86163b677ad0a4172d13.jpg" alt="İşlemsel Su ve Sesle Balina Sıçrayışı" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-282"></a>
### Case 282: [Dört Modelde Zebra Hareketi Karşılaştırması](https://x.com/AI_Screening/status/2118014564457668955) (üreten [@AI_Screening](https://x.com/AI_Screening))

**Aynı hayvan animasyonu görevinde yürüyüşü, anatomiyi ve sahne stilini karşılaştırın.**

Üst üste yerleştirilen dört klip Gemini 4 Carbon, Fable 5.5, Opus 5.5 ve Argon olarak etiketlenmiş. Bütün karşılaştırmayı bir arada tutmak, bacak hareketleri, vücut biçimi ve arka plan işleyişindeki farkları görünür kılıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/6fdcb38bf56493c314dba5b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/890d1b92800ee622275ec8d7.jpg" alt="Dört Modelde Zebra Hareketi Karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-283"></a>
### Case 283: [Lightreel’de Doğal Dille İçerik Üreticisi Bulma](https://x.com/lightreelai/status/2118010927199248705) (üreten [@lightreelai](https://x.com/lightreelai))

**İçerik üreticisi ölçütlerini açık takipçi ve izlenme eşikleri içeren bir arama sorgusuna dönüştürün.**

Lightreel, içerik üreticisi bulma demosunu Fable 5.5 etiketiyle sunuyor. Videoda 10,000’den az takipçisi ve 100,000’den fazla izlenen bir videosu olan çift içerik üreticileri için sorgu giriliyor, ardından sosyal video arama sonuçları gösteriliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5aef4b1766a560a35264c3ed.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1c6d9c1fb3c69b3aa2ee1976.jpg" alt="Lightreel’de Doğal Dille İçerik Üreticisi Bulma" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-284"></a>
### Case 284: [Bulut Denizinin Üzerinde Uçan Bir Gemi](https://x.com/devteamdrew/status/2118008142403649662) (üreten [@devteamdrew](https://x.com/devteamdrew))

**Işık ve hava değişirken çekimler arasındaki sürekliliği incelemek için daha uzun bir film kullanın.**

Üretici, birden fazla ajan ekibinin 19 saat boyunca JavaScript ve Python kullanarak yaklaşık 100 saniyelik bir animasyon hazırladığını anlatıyor. Paylaşılan dizi, uçan bir gemiyi bulutlar, gün batımı ve ay ışığı boyunca izliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/17ef07a780273abf9e9b6c92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a54746701db5f7f829071d2c.jpg" alt="Bulut Denizinin Üzerinde Uçan Bir Gemi" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-285"></a>
### Case 285: [Hareketli Kesit Görünümlü Mekanik Kalp](https://x.com/camperaigg/status/2118002649929056373) (üreten [@camperaigg](https://x.com/camperaigg))

**Ana hareket devam ederken bir mekanizmanın hareketli parçalarını açığa çıkarın.**

Üretici, Blender’da 106 dakikalık bir görev bildirmiş: mekanik bir kalp altın renkli yağ pompalarken gövdesi açılarak pistonları ve krank milini ortaya çıkarıyor. Notlarında sentezlenmiş ses ve istenmeyen parlamaların gizli ışıklardan kaynaklandığını bulma süreci ele alınıyor.

```
Make a mechanical heart and show its insides, use blender.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/157ebee3ce748cdc1e6b7970.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4a862111878dc42939f8e5e4.jpg" alt="Hareketli Kesit Görünümlü Mekanik Kalp" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-286"></a>
### Case 286: [Keşfedilebilir Yüzen Voksel Pagoda Bahçesi](https://x.com/legit_api/status/2117994730336252114) (üreten [@legit_api](https://x.com/legit_api))

**Üretilmiş bir ortamı, yapılarını ve su öğelerini dolaşarak değerlendirin.**

Bu voksel bahçesi, Fable 5.5’in eski bir checkpoint’ine atfediliyor. Kamera bir pagoda, yüzen adalar, bir köprü ve şelaleler arasında ilerleyerek sahneyi hem yer seviyesinden hem yüksek açılardan gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/cc4d15bf5103d7eb64f63e29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/22e78c0beb2a6f509bc02739.jpg" alt="Keşfedilebilir Yüzen Voksel Pagoda Bahçesi" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-287"></a>
### Case 287: [Sekiz Ekibin Hazırladığı Okyanus Macerası](https://x.com/0xMovez/status/2117987052419428576) (üreten [@0xMovez](https://x.com/0xMovez))

**Çok çekimli bir filmde aksiyon, efektler ve sentezlenmiş ses arasındaki sürekliliği inceleyin.**

Üretici, sekiz ajan ekibinin üç saatten kısa sürede 39 çekim ve sentezlenmiş ses içeren 83 saniyelik bir Three.js filmi hazırladığını bildiriyor. Görüntüler uzay araçları, deniz canlıları ve kırılan dalgalarla bir okyanus macerasını izliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a46543512fc30e5a33cb2fc3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a307daab219d70fa5bed0c86.jpg" alt="Sekiz Ekibin Hazırladığı Okyanus Macerası" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-288"></a>
### Case 288: [Etkileşimli Hiper Otomobil Sunumu](https://x.com/shmidtqq/status/2117977426990944736) (üreten [@shmidtqq](https://x.com/shmidtqq))

**Yakın araç görüntülerini seçilebilir kamera ve boya kontrolleriyle birleştirin.**

Üretici, geometri ve malzemeleri kodla oluşturulmuş bir Three.js hiper otomobil yapılandırıcısını tek bir çevrimdışı HTML dosyası olarak sunuyor. Kayıt kırmızı aracı, tekerlek ve gövde yakın planlarını, yansımaları ve kamera kontrollerini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4bd439d08b9f8a320a8851ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a16368d4c8b7c9a3a5455607.jpg" alt="Etkileşimli Hiper Otomobil Sunumu" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-289"></a>
### Case 289: [Bir Yaşam Ağacının Doğuşu](https://x.com/notjazii/status/2117972258090357164) (üreten [@notjazii](https://x.com/notjazii))

**Kısa bir animasyonu tohumdan olgun ağaca görünür dönüşüm etrafında yapılandırın.**

Üretici, tek istemle yaklaşık bir saat süren bir kodlama çalışması bildirmiş. 30 saniyelik dizi; çorak manzara, filiz ve büyüyen ağaçtan geçtikten sonra bulutların altında yeşil bir dünya ortaya çıkarıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29df8c398a2db37856c01b0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f50b8e7c2a28df7d0d3cd903.jpg" alt="Bir Yaşam Ağacının Doğuşu" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-290"></a>
### Case 290: [Çalışan İç Mekanizmalı Yürüyen Şato](https://x.com/camperaigg/status/2117966825048997914) (üreten [@camperaigg](https://x.com/camperaigg))

**Bir yürüme rig’ini görünür mekanik hareketle ve açılan bir gövdeyle ilişkilendirin.**

Üretici; buhar motoru, dişli aktarma düzenekleri, dört yürüme bacağı ve açılan sekiz gövde paneli içeren 133 dakikalık bir Blender iş akışı bildirmiş. Notlarında kamera animasyonunu düzeltmeyi ve yüksek işlem maliyetli çim geometrisini belirledikten sonra render süresini azaltmayı anlatıyor.

```
Make me Howl's moving castle and also show its internal machinery.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e7e25e7d44993a14ab0405e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8d3b1d734d971e2dd757926c.jpg" alt="Çalışan İç Mekanizmalı Yürüyen Şato" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-291"></a>
### Case 291: [Tost Karakteri ve Mekanik Böcek](https://x.com/flxrnc/status/2117965294224232796) (üreten [@flxrnc](https://x.com/flxrnc))

**Kısa bir animasyon karşılaşmasında karakterlerin sahnelenmesini ve sürekliliği inceleyin.**

Paylaşılan 40 saniyelik film, gün batımında bir tarlada mavi bir mekanik böcekle karşılaşan kare, tost benzeri bir karakteri gösteriyor. Kaynak filmi Fable 5.5’e atfediyor ve hareket tasarımı rehberine bağlantı veriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/d5e16bfd05f1c391cf32f848.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b7ae776a5c29618d061465.jpg" alt="Tost Karakteri ve Mekanik Böcek" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-292"></a>
### Case 292: [Fırtınada Bir Deniz Feneri Bekçisi](https://x.com/seeconvm/status/2117965120760365494) (üreten [@seeconvm](https://x.com/seeconvm))

**Bir mekân, hava değişimi ve açık bir sonuç etrafında kısa bir anlatı kurun.**

Üretici; kodla işlenmiş kareler, sentezlenmiş ses ve çevrimdışı bir HTML dosyası içeren 60 saniyelik bir Three.js kısa filmi anlatıyor. Görüntüler, şafak sahnesinden önce küçük bir deniz feneri bekçisini yağmur ve şimşekler boyunca izliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/7ca3c1e23eac0ed20511211e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/dfcab72e07d547d9dcb1dbc1.jpg" alt="Fırtınada Bir Deniz Feneri Bekçisi" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-293"></a>
### Case 293: [Bir Sahil Kasabasında Deniz Canlısı](https://x.com/BubbleBrain/status/2117963042621178000) (üreten [@BubbleBrain](https://x.com/BubbleBrain))

**Karakter hareketlerini, geçişleri ve görsel tutarlılığı değerlendirmek için kısa filmin tamamını inceleyin.**

Kaynak; yeşil bir deniz canlısı, bir sahil kasabası ve havada süzülen baloncukları içeren yaklaşık bir dakikalık bir Fable 5.5 animasyonu paylaşıyor. Video, bu kısa film tarzını değerlendirmek için somut bir görsel örnek sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/65db346493bdd9973bec3a4c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4442bdca5e6a7460f03af731.jpg" alt="Bir Sahil Kasabasında Deniz Canlısı" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-294"></a>
### Case 294: [Üç Modelle Halı Üzerinde Yarış](https://x.com/noclipepe/status/2117914944410628430) (üreten [@noclipepe](https://x.com/noclipepe))

**Aynı yarış görevinde oynanabilir sahnenin bütünlüğünü, hareketi ve görsel işlenişi karşılaştırın.**

Üretici, çocukluk halısı üzerinde geçen bir yarış oyununu Fable 5.5, Opus 5.5 ve GPT-6 Astra ile test ediyor. Son üç panelli kayıt ve önceki iki modelli karşılaştırma birlikte korunuyor; görüntülerdeki puanlar üreticinin kendi değerlendirmeleri.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ffe3b88099594ba14f536b51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/24d8ea7644cbe19947c8c53a.jpg" alt="Üç Modelle Halı Üzerinde Yarış" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e214760ff83ad9bfaf202484.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0340fc5579003245dfa99b1.jpg" alt="Üç Modelle Halı Üzerinde Yarış" width="760"></a></td></tr></table>

[İlgili karşılaştırma · @noclipepe](https://x.com/noclipepe/status/2117729666576302187)

Type: Evaluation | Date: 2026-11-04

---

<a id="case-295"></a>
### Case 295: [Robota Dönüşen Bir Kamyon](https://x.com/camperaigg/status/2117914482752299311) (üreten [@camperaigg](https://x.com/camperaigg))

**Rig yapısını, zemin temasını ve eşzamanlı sesi incelemek için bir dönüşüm dizisi kullanın.**

Üretici; 51 eklemli rig, zemin teması çözücüsü, işlemsel yağmur ve sentezlenmiş ses efektleriyle Blender’da 107 dakika çalıştığını bildiriyor. Kayıt, kamyonun ıslak zeminde açılarak ayakta duran bir robota dönüşmesini gösteriyor.

```
Make me a transformer truck with animations of its transforming.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/72ef538a8fb4b94f0e2d7e2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ea8537c130cd5623959dc275.jpg" alt="Robota Dönüşen Bir Kamyon" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-296"></a>
### Case 296: [Fable ve Hunyuan Animasyon Kareleri](https://x.com/xbquan/status/2117899651365908855) (üreten [@xbquan](https://x.com/xbquan))

**Tam bir animasyon hakkında sonuç çıkarmadan önce karşılık gelen kareleri karşılaştırın.**

Yazar, Fable 5.5 ve Hunyuan 4 etiketli iki ekran görüntüsü çifti paylaşıyor. Her çift karakter ve ortam sonuçlarını bir araya getiriyor; bu sabit görüntüler, gösterilen karelerin görsel karşılaştırılmasını destekliyor.

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e6c6551a29757e1eb7c31f36.jpg" alt="Fable ve Hunyuan Animasyon Kareleri" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/864db255f6fd2807b689d7d7.jpg" alt="Fable ve Hunyuan Animasyon Kareleri" width="760"></td></tr></table>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-297"></a>
### Case 297: [Işığı Paylaşmak Üzerine Bir Animasyon](https://x.com/abhinavflac/status/2117883591019708740) (üreten [@abhinavflac](https://x.com/abhinavflac))

**Soyut bir temayı görünür bir sonu olan kısa bir anlatıya dönüştürün.**

İyiliğin ne anlama geldiğini göstermesi istendiğinde modelin kodla animasyon ve ses ürettiği belirtiliyor. Işıklı bir figür ışığını bir çocuğa veriyor, ardından çevredeki manzara renklenirken kendisi daha da parlaklaşıyor.

```
Show me what kindness means to you
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b888d1a62b4d27ae2fca8226.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5bd15fc5c234b4b114765d6f.jpg" alt="Işığı Paylaşmak Üzerine Bir Animasyon" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-298"></a>
### Case 298: [Dağlar Arasında Bir Voksel Köyü](https://x.com/abhinavflac/status/2117377130388656569) (üreten [@abhinavflac](https://x.com/abhinavflac))

**Mekânsal tutarlılığı incelemek için üretilmiş bir köyü farklı ölçeklerde keşfedin.**

Asıl üretici; evler, su yolları ve küçük sakinleriyle yaşayan bir voksel köyünü kıyıdan, yukarıdan ve çevredeki dağların içinden gösteriyor. İlgili bir Çince gönderi, ayrıntılı bir sahne istemi sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae5269b0eff86da4580064d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e612faf20dd5f5de4ee171b.jpg" alt="Dağlar Arasında Bir Voksel Köyü" width="760"></a>

[@cfenghub](https://x.com/cfenghub/status/2117775332535148752)

Type: Demo | Date: 2026-11-02

---

<a id="case-299"></a>
### Case 299: [Dört Modelle Pelikan ve Fil Kompozisyonu](https://x.com/pipeline_os/status/2117719191478513700) (üreten [@pipeline_os](https://x.com/pipeline_os))

**Farklı modellerin tek animasyonda etkileşen birden fazla özneyi nasıl ele aldığını karşılaştırın.**

Dört panelli kayıt; pelikan, bisiklet, timsah ve fil görevini Gemini 4 Argon, Opus 5.5, Fable 5.5 ve Kimi K3.1 Pro için yan yana gösteriyor. Tam kompozisyon, her modelin özne yerleşimini ve hareketini koruyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/9db78999efffeffa7ccaca0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/15a45dc0efe3247f0821c8a2.jpg" alt="Dört Modelle Pelikan ve Fil Kompozisyonu" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-300"></a>
### Case 300: [Darbe Kareleriyle Anime Kılıç Dövüşü](https://x.com/camperaigg/status/2117717189059026969) (üreten [@camperaigg](https://x.com/camperaigg))

**Karakter aksiyonunu, darbe parlamalarını, sesi ve bilinçli sessizliği eşzamanlayın.**

Üretici; kumaş benzeri pelerinler, karşıt silahlar ve sentezlenmiş müzik ile efektler içeren 46 saniyelik bir çöp adam dövüşü için 66 dakikalık kodlama çalışması bildirmiş. Notları ters yöne giden bir saldırıyı, görsel izleri ve başlık konumunu düzeltmeyi anlatıyor.

```
Make me a video of 2 stickman fighting, anime style.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/c36c188396aac371a64e31a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b670f06d376211c60bf894.jpg" alt="Darbe Kareleriyle Anime Kılıç Dövüşü" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-301"></a>
### Case 301: [Dört Modelde Koşan Geyik Karşılaştırması](https://x.com/fawnunwrap/status/2117702487755100543) (üreten [@fawnunwrap](https://x.com/fawnunwrap))

**Aynı görevin tam kompozisyonu görünürken uzuv hareketlerini ve hayvan biçimini karşılaştırın.**

FawnBench, koşan bir geyiği Fable 5.5’e atfedilen bir çalışma, Gemini 4 Argon, GPT-6 Astra ve Opus 5.5 olarak etiketlenen dört panelde sunuyor. Görüntüler, ölçülmüş sayısal bir performans sonucu değil görsel bir karşılaştırma.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3add4d9e0752d0467cbe6065.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/eea598747047797148e19c4e.jpg" alt="Dört Modelde Koşan Geyik Karşılaştırması" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-302"></a>
### Case 302: [Sular Altındaki Şehri Geçen Bir Robot](https://x.com/0xMovez/status/2117700681867903169) (üreten [@0xMovez](https://x.com/0xMovez))

**Yansımalar, karakter hareketi ve değişen kamera görünümü arasındaki sürekliliği inceleyin.**

Üretici; kodla işlenmiş kareler, sentezlenmiş ses ve tek bir çevrimdışı HTML render dosyası içeren 42 saniyelik bir Three.js animasyonu bildirmiş. Görüntüler, bir robotu sular altında kalmış ve bitkilerle kaplanmış bir şehirden renkli bir açık su sahnesine kadar izliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f39e1807d1e80422c31530c6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/247f768636339f49d149c787.jpg" alt="Sular Altındaki Şehri Geçen Bir Robot" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-303"></a>
### Case 303: [Blender Kılıcı ve Sunum Filmi](https://x.com/camperaigg/status/2117694354685092255) (üreten [@camperaigg](https://x.com/camperaigg))

**İşlemsel varlık oluşturmayı sonraki kamera ve ses aşamasından ayırın.**

Üretici, önce tek bir Python betiğiyle bir kılıç ürettiğini, ardından bir video istediğini anlatıyor. Devamında kesintisiz Blender kamera hareketi, orman aydınlatması, sentezlenmiş orkestra müziği ve HyperFrames düzenlemesi kullanılıyor; bildirilen toplam süre 65 dakika.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3c767f2038ef7d3960c956ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/525304dc7d4016ac33b3d4f8.jpg" alt="Blender Kılıcı ve Sunum Filmi" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-304"></a>
### Case 304: [Lantern Isle Piksel Köyü Animasyonu](https://x.com/abhinavflac/status/2117693193429139965) (üreten [@abhinavflac](https://x.com/abhinavflac))

**Yoğun bir animasyon ortamında yerel etkinlikleri ve gündüzden geceye geçişleri inceleyin.**

Üretici; sakinleri, tekneleri, şelaleleri, fenerleri ve müziğiyle kodla çizilmiş bir ada köyü paylaşıyor. Kayıt, yakından köy etkinlikleri, geniş ada manzaraları ve ışıldayan fenerlerin bulunduğu bir gece dizisi arasında geçiş yapıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e91f1eabab743730dd815c98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b7d2e578739d25596db1164f.jpg" alt="Lantern Isle Piksel Köyü Animasyonu" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-305"></a>
### Case 305: [Pause Oyun Videosu Düzenleme Demosu](https://x.com/pausevfx/status/2117676887665447206) (üreten [@pausevfx](https://x.com/pausevfx))

**Ham görüntüden altyazılara ve düzenlenebilir zaman çizelgesine uzanan bir kurgu iş akışını inceleyin.**

Pause bu iş akışını video düzenleme için Fable 5.5 etiketiyle sunuyor. Demo oyun anlarını seçiyor, yüz kamerasının kadrajını değiştiriyor, altyazı ve ses ekliyor ve Premiere’de düzenlenebilir bir sekans açıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0faaeecdaa02683f81e67f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae2d32876804bf286f11dc6c.jpg" alt="Pause Oyun Videosu Düzenleme Demosu" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-306"></a>
### Case 306: [Sahil Boyunca Bisiklete Binen Pelikan](https://x.com/pankajkumar_dev/status/2117301455665439210) (üreten [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**İnce geometriyi ve animasyonu hem yakın hem geniş kamera açılarından inceleyin.**

Üretici, deniz kenarında yüksek tekerlekli bisiklet süren bir pelikan paylaşıyor. Kayıt; tüyleri, pedalları ve tekerlek geometrisini inceledikten sonra taş döşeli sahil şeridinin daha geniş görünümlerine dönüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/66c3c44bcefa684522f95b96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8575912e8f20f48439aea683.jpg" alt="Sahil Boyunca Bisiklete Binen Pelikan" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="acknowledge"></a>
## 🙏 Teşekkür

Bu depo, gerçek Claude Fable 5 kullanım örneklerini herkese açık şekilde paylaşan üreticilerden, geliştiricilerden, benchmark ekiplerinden ve topluluklardan ilham aldı.

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@hakmgpt](https://x.com/hakmgpt), [@camperaigg](https://x.com/camperaigg), [@lightreelai](https://x.com/lightreelai), [@0xMovez](https://x.com/0xMovez), [@shmidtqq](https://x.com/shmidtqq), [@flxrnc](https://x.com/flxrnc), [@seeconvm](https://x.com/seeconvm), [@BubbleBrain](https://x.com/BubbleBrain), [@xbquan](https://x.com/xbquan), [@pipeline_os](https://x.com/pipeline_os), [@fawnunwrap](https://x.com/fawnunwrap), [@pausevfx](https://x.com/pausevfx), [@AnikaCodes](https://x.com/AnikaCodes), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@cfenghub](https://x.com/cfenghub), [@shneural](https://x.com/shneural)


*Her örneğin özgün üreticiye atfedildiğini garanti edemeyiz. Düzeltilmesi gereken bir şey varsa lütfen bizimle iletişime geçin, güncelleyelim.*

Paylaşmak istediğiniz daha ilginç kullanım örnekleri varsa, issue veya pull request açmaktan çekinmeyin ve Evolink kullanım örnekleri kütüphanesini büyütmeye yardım edin.

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
