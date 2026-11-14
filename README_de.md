# Anwendungsfälle für Claude Fable 5.2

**[160 Fälle zu Fable 5.2 ansehen](docs/fable-5-2/README_de.md)**

Arbeitsabläufe, Demos, Vergleiche, Benchmarks, Integrationen und praktische Grenzen aus den Sammlungen vom 10. und 13.–14. November, jeweils mit Quellen.

## Frühere Fable-Fälle

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

## 🍌 Einführung

Willkommen im High-Signal-Usecase-Repository zu Claude Fable 5.

**Wir sammeln reale Anwendungsfälle, Tutorials, Integrationen und Auswertungen zu Claude Fable 5, kuratiert aus öffentlichen Demos und Creator-Communities.**

Diese deutsche README konzentriert sich auf High-Signal-Fälle mit konkreten Workflows, Prompts, Demos, Integrationen, Benchmark-Belegen oder praktischen Grenzen.

Die meisten Fälle sind aus X/Twitter-Posts und öffentlichen Demos kuratiert. Jeder Falltitel verlinkt auf die Originalquelle, und jeder Autoren-Handle verlinkt auf das Profil des Creators.

Auf Evolink ausprobieren: [Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

## 📊 Überblick

- **88 ursprüngliche Fable-5-Fälle und 241 Community-Fälle; insgesamt 329 Fälle.**
- Deckt Coding-Agents, lang laufende Automatisierung, Spiele, visuelles Design, 3D-Simulationen, Wissensarbeit, Tutorials, API-Integrationen, Benchmarks, Preise und Launch-Einschränkungen ab.
- Jeder Fall enthält die Originalquelle, Creator-Zuordnung, eine knappe Kernaussage, den Evidenztyp und das Veröffentlichungsdatum.
- Nutze dieses Repo, um praktische Workflows zu finden, Stärken und Grenzen zu vergleichen, reproduzierbare Prompts zu entdecken und Integrationsbeispiele nachzuvollziehen.

> [!NOTE]
> Die Sammlung bevorzugt konkrete Evidenz gegenüber Hype: reproduzierbare Prompts, veröffentlichte Demos, Benchmark-Methoden, Integrationsnotizen, Kostendaten und klar benannte Einschränkungen.

<a id="-quick-api-access"></a>
## ⚡ Schneller API-Zugriff

Nutze Claude Fable 5 über die Evolink-kompatible Messages API. Hole dir einen API-Token über [Evolink](https://evolink.ai/login?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5) und ersetze dann `<token>` durch deinen Token.

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

| Bereich | Fälle |
|---|---|
| [💻 Coding und Codegenerierung](#coding-and-code-generation) | Case 1-6 |
| [🤖 Agents und lang laufende Automatisierung](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 Spiele und interaktive Demos](#games-and-interactive-demos) | Case 9-12 |
| [🎨 Visuelles, Design, Video und 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 Dokumente, Wissensarbeit und Forschung](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 Tutorials, Kurse und Prompt-Ressourcen](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 Plattform, API und Tool-Integration](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 Auswertungen, Vergleiche und Grenzen](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | Credits und Korrekturhinweis |

### [💻 Coding und Codegenerierung](#coding-and-code-generation)

| Case | Was es zeigt | Typ |
|---|---|---|
| [Mehrstufiger Cursor-Workflow](#case-1) | Nutze Fable 5 als Plan-Review- und Kritikschritt innerhalb eines Multi-Model-Cursor-Workflows und gib Implementierung sowie Überarbeitung anschließend an günstigere oder spezialisierte Modelle zurück. | Auswertung |
| [GitHub aus einem Screenshot nachbauen](#case-2) | Füge einen Produktscreenshot in ein agentisches Coding-Tool ein und bitte Fable 5, die Oberfläche mit funktionierender Funktionalität nachzubauen. | Demo |
| [Schwarzes-Loch-Simulation mit einem Prompt](#case-3) | Gib Fable 5 einen detaillierten Creative-Coding-Prompt und bitte es, eine eigenständige Three.js-Physikvisualisierung zu erstellen. | Tutorial |
| [macOS-artiges Web-OS im One-Shot](#case-4) | Bitte Fable 5 um ein vollständiges Single-File-Web-OS und lass es UI-Shell, Apps, Interaktionen, Audio und eingebettetes Spielverhalten in einem Durchgang bauen. | Tutorial |
| [Spawn 5.0 mit 1.687 Prompts bauen](#case-5) | Nutze Fable 5 über viele Prompts hinweg als Engineering-Partner für lange Sitzungen, wobei sich die Rolle des Menschen von Architektur hin zur Beurteilung der Ausgabequalität verschiebt. | Tutorial |
| [Review einer großen Pull Request mit Findings](#case-6) | Richte Fable 5 auf eine große Pull Request und bitte es, Korrektheit, False Positives, echte Bugs und Polish-Probleme zu prüfen. | Demo |

### [🤖 Agents und lang laufende Automatisierung](#agents-and-long-running-automation)

| Case | Was es zeigt | Typ |
|---|---|---|
| [Review eines Long-Horizon-Relay-Workflows](#case-7) | Nutze Fable 5 für ambitionierte Langhorizont-Arbeit: Site-Rebuilds, programmatische Content-Pipelines, Voice-Matching, Security-Review und abschließende Qualitätschecks. | Auswertung |
| [Infrastrukturausfall diagnostizieren und Fix-PR öffnen](#case-8) | Gib Fable 5 Zugriff auf Infra-Hinweise wie Logs, Datenbankfehler und Image-Digests und bitte es dann, den Ausfall zu diagnostizieren und den Fix vorzubereiten. | Auswertung |

### [🎮 Spiele und interaktive Demos](#games-and-interactive-demos)

| Case | Was es zeigt | Typ |
|---|---|---|
| [Dino Runner mit Fingertracking](#case-9) | Bitte Fable 5, ein Browserspiel zu bauen, das Fingertracking als Eingabemechanik nutzt. | Demo |
| [Rennspiel-Build mit zwei Sätzen](#case-10) | Gib Fable 5 einen sehr kurzen Spielprompt und lass es Maps, Modi, Musik, UI und Game-Assets in einem Lauf generieren. | Tutorial |
| [Installierbares Terminal-Minecraft in Rust](#case-11) | Führe Fable 5 durch ein Terminal-Coding-Harness und bitte es, ein installierbares Rust-Terminalspiel zu bauen. | Demo |
| [Minecraft-Klon mit Zeit und Kosten](#case-12) | Nutze einen Prompt, um Fable 5 um einen spielbaren Minecraft-artigen Klon zu bitten, und bewerte anschließend Zeit, Kosten, Codeumfang und Feature-Abdeckung. | Tutorial |

### [🎨 Visuelles, Design, Video und 3D](#visual-design-video-and-3d)

| Case | Was es zeigt | Typ |
|---|---|---|
| [Vollständig reproduzierbarer Ecommerce-E-Mail-Prompt](#case-13) | Gib Fable 5 ein vollständiges Creative Briefing für ein Marken-E-Mail-Mockup, einschließlich exakter Abschnitte, Produktanforderungen, visueller Richtung und Einschränkungen. | Tutorial |
| [Schweizer-Ankeruhrmacher-Benchmark](#case-14) | Nutze Fable 5 für einen mechanischen Simulationsbenchmark und bitte es, physikalische Korrektheit zu implementieren, zu verifizieren und iterativ zu verbessern. | Auswertung |
| [Friends-Apartment-Szene in Three.js](#case-15) | Prompte Fable 5, einen Grundriss und eine Szenenreferenz in eine navigierbare Three.js-Umgebung zu verwandeln. | Auswertung |
| [Sonnensystem-Simulation mit Prompt und URL](#case-16) | Nutze Fable 5, um aus physikalischen Prinzipien eine Astronomiesimulation zu bauen, mit Iteration bis Simulation und öffentliche Ausgabe bereit sind. | Tutorial |

### [📚 Dokumente, Wissensarbeit und Forschung](#documents-knowledge-work-and-research)

| Case | Was es zeigt | Typ |
|---|---|---|
| [Evidenz zu Stripe und wissenschaftlichen Workflows](#case-17) | Nutze dies als Evidenz für Enterprise-Migrationen und wissenschaftliche Workflow-Claims, nicht als Copy-Paste-Prompt. | Auswertung |
| [Policy-Memo- und Änderungsnachverfolgungs-Workflows](#case-18) | Nutze Fable 5 für qualitative Langform-Dokumentarbeit: Änderungen nachverfolgen, Kommentare triagieren und transkriptgetriebene Edits. | Tutorial |
| [Deep-Research-Prompt und Ausgabe](#case-19) | Stelle Fable 5 eine forschungsartige Frage und bewerte, ob es eine strukturierte, historisch fundierte lange Antwort erzeugen kann. | Demo |

### [🧭 Tutorials, Kurse und Prompt-Ressourcen](#tutorials-courses-and-prompt-resources)

| Case | Was es zeigt | Typ |
|---|---|---|
| [Wie Fable 5 Claude Code-Workflows verändert](#case-20) | Nutze Fable 5, indem du Richtung, Kontext, Ziele und Verifikationskriterien setzt, statt jeden Schritt mikrozuverwalten. | Demo |
| [Review mit einer Milliarde Tokens und Routing-Strategie](#case-21) | Nutze Fable 5 für Frontier-Planung und Review und route anschließend volumenstarke Implementierung an günstigere Modelle. | Tutorial |
| [Defensiver Prompt zur Gerätehärtung](#case-22) | Führe einen defensiven Härtungsprompt Schritt für Schritt aus, bei dem Fable 5 Geräte inventarisiert, exakte Checks gibt und auf Verifikation wartet. | Tutorial |
| [Goal-Prompt für ein Full-Site-Design-Audit](#case-23) | Nutze `/goal`, damit Fable 5 eine Site bootet, Seiten screenshotet, UX auditiert, einen Bericht schreibt und sichere kleine Probleme fixt. | Tutorial |
| [Aufteilung eines Long-Form-Creative-Workflows](#case-24) | Nutze Fable 5, um stabile Formate und Beispiele zu entwerfen, und übergib diese Struktur dann an ein anderes Generierungssystem für domänenspezifische Ausgabe. | Tutorial |
| [Anfängerleitfaden zur Nutzung von Fable 5](#case-25) | Nutze Fable 5 mit zielorientierten Prompts, Verifikationsschleifen und Effort-Einstellungen statt mit kleinen Schritt-für-Schritt-Anweisungen. | Auswertung |
| [Copy-Paste-Prompt für Repository-Audits](#case-26) | Füge den Repository-Audit-Prompt in Fable 5 ein und bitte um dateigestützte Discovery, Findings, Strategie und einen Meilenstein-Taskplan. | Tutorial |
| [Nutzungsstrategie für begrenzte Zeitfenster](#case-27) | Verwende Fable 5-Nutzung für Audit, Architektur und Planung, solange das Zugriffsfenster günstig ist, und nutze anschließend günstigere Modelle für die Ausführung. | Tutorial |
| [Goals und Workflows in Claude Code nutzen](#case-28) | Nutze Fable 5 vor der Implementierung als Denkpartner und kombiniere anschließend `/goal` und Workflows, um den Plan auszuführen und zu verifizieren. | Tutorial |

### [🔌 Plattform, API und Tool-Integration](#platform-api-and-tool-integration)

| Case | Was es zeigt | Typ |
|---|---|---|
| [Hermes-Agent-Integrationssetup](#case-29) | Konfiguriere Hermes so, dass es `anthropic/claude-fable-5` für komplexe `/goal`-Runs und gecachte Long-Horizon-Aufgaben nutzt. | Tutorial |
| [Fähigkeiten, Preise und Abo-Notizen](#case-30) | Nutze diesen Fall, um zu verstehen, wann Fable 5 verfügbar ist, was es kostet und welche geschützten Domains auf ein anderes Modell zurückfallen können. | Tutorial |
| [Zusammenfassung zu Launch, Zugriff, Preisen und Sicherheit](#case-31) | Nutze diese Launch-Zusammenfassung, um Zugriffsweg, API-Modellnamen, Kontextfenster, Caching-Strategie und Abo-Timing zu wählen. | Tutorial |
| [Advisor-basierte Strategie zur Kostensenkung](#case-32) | Nutze Fable 5 als Advisor oder Reviewer in einem Workflow mit günstigerem Modell, wenn marginale Intelligenz die Kosten wert ist. | Integration |
| [Preise, Zugriff und Sicherheitsleitplanken](#case-33) | Nutze diesen Fall, um Fable 5-Zugriff, API-Preise und Safety-Fallback-Verhalten zu verstehen, bevor du Workloads planst. | Integration |
| [Swarms-Integration in einer Zeile](#case-34) | Setze den Swarms-Modellnamen auf `anthropic/claude-fable-5` und führe Fable 5 über das Swarms-Framework oder die API aus. | Integration |

### [📏 Auswertungen, Vergleiche und Grenzen](#evaluations-comparisons-and-limits)

| Case | Was es zeigt | Typ |
|---|---|---|
| [Kosten- und Qualitätsvergleich Fable 5 vs. GPT-5.5](#case-35) | Vergleiche Fable 5 und GPT-5.5 bei derselben Coding-Aufgabe, um Ausgabequalität, Laufzeit und Toolkosten zu beurteilen. | Auswertung |
| [Ergebnis des AA-Omniscience-Benchmarks](#case-36) | Nutze diesen Benchmark-Fall, um Fable 5 bei Wissensgenauigkeit und Halluzinationsverhalten zu bewerten. | Auswertung |
| [Ergebnis des Artificial Analysis Intelligence Index](#case-37) | Nutze diesen Fall, um Fable 5s allgemeines Intelligenzranking gegenüber anderen Frontier-Modellen zu benchmarken. | Auswertung |
| [GDPval-AA-Benchmark für agentische Wissensarbeit](#case-38) | Nutze diesen Fall, um Fable 5 bei agentischer realer Wissensarbeit zu evaluieren. | Auswertung |
| [Ersteindrücke nach einer Woche und Preislogik](#case-39) | Nutze diesen Ersteindrucksfall, um zu entscheiden, wo Fable 5 am stärksten ist, besonders bei Game Design und Systemplanung. | Integration |
| [Kosten- und Geschwindigkeitsvergleich](#case-40) | Nutze diesen Vergleich, um zu entscheiden, ob der Qualitätsgewinn höhere Kosten und langsamere Long-Horizon-Runs rechtfertigt. | Auswertung |
| [Hands-on-Notizen zu Claude Code](#case-41) | Nutze diesen Fall, um Fable 5 in Claude Code zu bewerten, einschließlich Tool Use, Persönlichkeit und verbleibender Ecken und Kanten. | Demo |
| [Ergebnis des Creative-Writing-Benchmarks](#case-42) | Nutze diesen Benchmark-Fall, um Fable 5s Qualität bei Kurzgeschichten und Refusal-Verhalten zu beurteilen. | Auswertung |
| [Launch-Zusammenfassung mit mehreren Benchmarks](#case-43) | Nutze diese Launch-Benchmark-Zusammenfassung, um die Headline-Scores zu verstehen, die für Coding-Agents und komplexe Aufgaben am relevantesten sind. | Auswertung |
| [Benchmark- und Preisvergleich mit GPT-5.5](#case-44) | Nutze diesen Vergleich, um Fable 5 gegenüber GPT-5.5 bei Preis und Benchmark-Kategorien zu bewerten. | Auswertung |
| [Feldnotizen mit praktischen Einschränkungen](#case-45) | Nutze diesen Feldbericht, um zu verstehen, wo sich Fable 5 bedeutend besser anfühlt und wo es noch praktische Grenzen hat. | Tutorial |
| [Vergleich von Physiksimulationen](#case-46) | Führe identische Physiksimulations-Prompts gegen Fable 5 und Opus 4.8 aus, um Ausgabequalität, Kosten und Geschwindigkeit zu vergleichen. | Demo |
| [Debugging-Erfahrung und Designurteil](#case-47) | Nutze Fable 5 zum Debugging, indem du es messen, loggen, verifizieren und patchen lässt, statt einfach zu raten. | Demo |
| [Mehrdimensionale Vor- und Nachteile](#case-48) | Nutze diesen Fall, um praktische Stärken und Schwächen zu verstehen, bevor du Fable 5 zum Daily Driver machst. | Demo |
| [Test zum Entwurf eines juristischen S-1](#case-49) | Nutze einen S-1-Drafting-Prompt als Fähigkeitstest für Legal Agents und vergleiche Struktur, Formatierung und Länge. | Tutorial |
| [Details zum Healthcare-Benchmark](#case-50) | Nutze diese Benchmark-Notiz, um Fable 5 bei Healthcare-bezogenen Aufgaben zu bewerten und fehlende harte medizinische Evals zu identifizieren. | Auswertung |
| [ParseBench-Auswertung zum Dokumentparsing](#case-51) | Nutze diesen Fall, um zu entscheiden, ob Fable 5 für Dokumentparsing gegenüber spezialisierten OCR-Systemen kosteneffektiv ist. | Auswertung |
| [Vergleich von SWE-Bench Pro und FrontierCode](#case-52) | Nutze diesen Benchmark-Fall, um Fable 5 für Migrationen, komplexe Implementierungen, autonome Sitzungen, Tests und visuelle Verifikation zu evaluieren. | Auswertung |
| [Qualitative Review langer Problemlösung](#case-53) | Nutze diese qualitative Review, um zu verstehen, warum Fable 5 für längere, schwierigere Aufgaben geeignet ist, aber weiterhin Produktionsreview braucht. | Auswertung |
| [ParseBench-Ergebnisse zu Treue und Formatierung](#case-54) | Nutze dieses ParseBench-Ergebnis, um Dokumenttreue und Formatierungsperformance zu beurteilen. | Auswertung |
| [Benchmarks, Preise, Zugriff und Schutzmaßnahmen](#case-55) | Nutze diesen Fall als breite Checkliste für Benchmarks, Preise, Zugriff, Schutzmaßnahmen und strategische Implikationen. | Auswertung |
| [Offizielle Liste der Benchmark-Scores](#case-56) | Nutze diese Benchmark-Liste, um Fable 5s offizielle Scores über Coding-, Computer-Use- und Security-Tasks hinweg zu verstehen. | Auswertung |
| [Methodik des APEX-SWE-Benchmarks](#case-57) | Nutze diesen Fall, um Fable 5 auf APEX-SWE zu bewerten, besonders Observability- und Integrationsarbeit. | Auswertung |
| [Ergebnis formaler Mathematik in ProofBench](#case-58) | Nutze diesen Fall, um Fable 5 bei formaler Mathematik gegenüber spezialisierten Theorem-Proving-Systemen zu evaluieren. | Tutorial |
| [Vorläufige Analyse von VirtueBench](#case-59) | Nutze diesen Fall, um Fable 5s Moral-Reasoning-Verhalten über Tugendkategorien hinweg zu untersuchen. | Auswertung |
| [Safety-Overfit-Test mit leeren API-Antworten](#case-60) | Nutze diesen Fall, um Launch-Time-Safety-Overfit-Risiko und Empty-Response-Verhalten in API-Tests zu verstehen. | Auswertung |
| [Fable-Prompts mit Überprüfung gestalten](#case-61) | Nutze diesen Leitfaden, um statt langer Prompt-Tricks Ziele, Kontext, Grenzen, Werkzeuge und Prüfschleifen vorzugeben. | Tutorial |
| [Istanbul-Plattformspiel aus einer Bildvorlage](#case-62) | Teste Fable 5 mit einem Sprite-Sheet als Vorlage und einer Anweisung zur Umsetzung als spielbares Plattformspiel. | Demo |
| [Ein 3D-Stadtdashboard für Geschäftsabläufe](#case-63) | Nutze Fable 5, um einen Geschäftsprozess als Konzept für ein lebendiges 3D-Stadtdashboard darzustellen. | Demo |
| [Ein Three.js-Lochspiel aus einem Prompt](#case-64) | Nutze Fable 5, um in einem Durchlauf einen 3D-Browserspiel-Prototyp in Three.js zu erstellen. | Demo |
| [DeepSWE-Ergebnisse im Vergleich](#case-65) | Vergleiche anhand dieses DeepSWE-Beitrags Fable 5 xHigh und GPT-5.5 xHigh bei Softwareentwicklungsaufgaben. | Auswertung |
| [Kosten einer Repository-Analyse vergleichen](#case-66) | Bewerte mit diesem Vergleich von Repository-Analysen Tokenpreise im Verhältnis zum menschlichen Nachbearbeitungsaufwand. | Auswertung |
| [Tokenverbrauch eines Super-Mario-Spiels](#case-67) | Nutze diesen Spielaufbau in einem Durchlauf, um Ausgabequalität und Tokenverbrauch von Fable 5 einzuschätzen. | Demo |
| [Claude Codes Einstellung zum Modellwechsel](#case-68) | Lerne die Claude-Code-Einstellung kennen, die bei einer markierten Fable-5-Nachricht das Modell wechselt. | Integration |
| [Einen Namma-Metro-Simulator entwickeln](#case-69) | Nutze diese Demo als kurzes Beispiel für die Entwicklung eines Nahverkehrssimulators mit Fable 5 per Vibe Coding. | Demo |
| [Dusk Drive aus einem einzigen Prompt](#case-70) | Bewerte mit diesem Fall, wie Fable 5 ein Low-Poly-Fahrspiel ohne menschliche Nachbearbeitung prototypisiert. | Demo |
| [APEX-Agents-Rangliste nach Pass@1](#case-71) | Vergleiche anhand dieses APEX-Agents-Ergebnisses Fable 5 Max bei mehrstufigen autonomen Aufgaben. | Auswertung |
| [Leitfaden zur Auswahl von Claude-Modellen](#case-72) | Reserviere Fable 5 mithilfe dieses Auswahlleitfadens für die anspruchsvollsten Aufgaben in Claude Code. | Tutorial |
| [HermesWorld mit einer autonomen Agentenschleife](#case-73) | Untersuche eine Fable-5-Schleife, die über Tage selbstständig entwickelt, testet, spielt und Smoke-Tests ausführt. | Integration |
| [Einen Beratungsbericht im McKinsey-Stil testen](#case-74) | Bewerte mit diesem Dokumenten-Prompt Berichtsstruktur, Diagramme, Erzählführung und Risikoanalyse. | Tutorial |
| [Sichtbare Schutzmechanismen einführen](#case-75) | Lerne anhand dieser offiziellen Mitteilung die sichtbaren Fable-5-Schutzmechanismen, API-Ablehnungsgründe und den Wechsel zu Opus kennen. | Integration |
| [Modellzuordnung in Claude Code korrigieren](#case-76) | Vermeide mit diesem Claude-Code-Änderungshinweis Probleme bei Fable-5-Modellnamen und der Kontextzuordnung. | Integration |
| [Drei Webanwendungen in Claude Code](#case-77) | Untersuche mit dieser Einsteigerdemo, wie Fable 5 in Claude Code mehrere Webanwendungen erzeugt. | Demo |
| [Rilable als quelloffenen App-Builder untersuchen](#case-78) | Untersuche anhand dieses quelloffenen App-Builders Fable 5 bei iOS- und Webanwendungen, Sandboxen und API-Tokenkosten. | Integration |
| [DeepSWE-Debüt im Coding-Agent-Index](#case-79) | Nutze den aktualisierten Artificial-Analysis-Index, um Claude Fable 5 bei schwierigeren agentischen Coding-Aufgaben zu vergleichen, die keine recycelten öffentlichen GitHub-Fixes verwenden. | Evaluation |
| [DataEmpire-Web-Analytics-Spiel](#case-80) | Verwandle rohe Site-Analytics in ein wiederholt spielbares Game, indem du Claude Fable 5 Besucher und Meilensteine auf Spieleinheiten abbilden lässt. | Integration |
| [FrontierSWE-20-Stunden-Tasksignal](#case-81) | Nutze FrontierSWE als Beleg dafür, dass Claude Fable 5 über sehr lange Engineering-Aufgaben hinweg produktiv bleiben kann und nicht nur in kurzen Bugfix-Schleifen. | Evaluation |
| [KernelBench-Hard-CUDA-Rekorde](#case-82) | Nutze Claude Fable 5 für fortgeschrittene CUDA-Kernel-Generierung, wenn du Low-Level-Optimierung brauchst und nicht nur Wrapper um bestehende Bibliotheken. | Evaluation |
| [Figma-Capture-Landingpage-Klon](#case-83) | Erfasse eine Live-Konkurrentenseite als Figma-Layer und lass Claude Code mit Claude Fable 5 Struktur, Copy und Brand-System neu aufbauen, statt aus Screenshots zu raten. | Integration |
| [GTA-2-Klon in zwei Stunden](#case-84) | Kombiniere Claude-Fable-5-Codegenerierung mit separatem Asset-Tooling, um schnell ein spielbares 3D-Spiel zu bauen, ohne den gesamten Stack von Hand zu coden. | Tutorial |
| [CloudWatch-Log-Triage-Agent](#case-85) | Lass einen von Claude Fable 5 angetriebenen Agenten sehr große Service-Log-Kontexte durcharbeiten, die Architektur ableiten und dann gezielt auf konkrete Fehler einzoomen. | Integration |
| [World-Cup-Predictor in Sandboxes](#case-86) | Stelle mehrere Frontier-Modelle hinter isolierte Sandboxes und lass sie Live-Nachrichten, Verletzungen und Gelbe-Karten-Kontext für eine öffentliche Prediction-App recherchieren. | Integration |
| [WolfBench-Refusal-Kostenfall](#case-87) | Behandle Refusal-Verhalten als echte Benchmark-Variable, wenn du lange autonome Runs auf Claude Fable 5 bepreist. | Evaluation |
| [API-Access-Cutoff-Tracker](#case-88) | Überwache die Verfügbarkeit per Skript, wenn dein Workflow von fortgesetztem Zugriff auf ein Frontier-Modell abhängt, das ohne große Vorwarnung rate-limitiert oder zurückgezogen werden kann. | Integration |



### [🆕 Fable 5.5: Community-Demos](#fable-5-5-community-demos)

| Fall | Typ |
|---|---|
| [Codegenerierte Fuchsanimation mit Ton](#case-89) | Demo |
| [Animation aus einem offenen Kreativbriefing](#case-90) | Demo |
| [Animierte Website für ein Bauunternehmen](#case-91) | Demo |
| [Autopräsentation mit Three.js](#case-92) | Demo |
| [Browserspiel-Demo im Minecraft-Stil](#case-93) | Demo |
| [Radfahrender Pelikan als Three.js-Animation](#case-94) | Demo |
| [Pelikan-Fahrrad-SVG mit exaktem Prompt](#case-95) | Demo |
| [Animationsbeispiel eines galoppierenden Zebras](#case-96) | Demo |
| [TradingView-Indikator mit manueller Orderausführung](#case-97) | Demo |
| [Aus einem Punkt wird eine animierte Kurzgeschichte](#case-98) | Demo |
| [Superman im Wechsel verschiedener Kunststile](#case-99) | Demo |
| [Menschlicher Fortschritt als Animationsfilm mit Musik](#case-100) | Demo |
| [Vergleich zweier Einführungsvideos mit Opus](#case-101) | Evaluation |
| [Songtext und Ereignis visuell verbinden](#case-102) | Demo |
| [Voxel-Figur in einer schwebenden Umgebung](#case-103) | Demo |
| [Eine dreidimensionale Rube-Goldberg-Maschine](#case-104) | Demo |
| [3D-Controller-Oberfläche mit Ton und Bewegung](#case-105) | Demo |
| [Comicfiguren als JavaScript-Präsentation](#case-106) | Demo |
| [Updraft: Welten, Bosse und eine Rangliste](#case-107) | Demo |
| [Fahren auf einer Karte von San Francisco](#case-108) | Demo |
| [Prompts für eine Seedance-Actionsequenz schreiben](#case-109) | Demo |
| [Erklärvideo für einen Desktop-Kollegen](#case-110) | Demo |
| [Ein kurzer Prompt für wechselnde Animationsstile](#case-111) | Demo |
| [Das Dreikörperproblem visualisieren](#case-112) | Demo |
| [Animationsgalerie mit verschiedenen Kunststilen](#case-113) | Demo |
| [Roboterbegleiter und prozedurales Fell](#case-114) | Demo |
| [Ein Mathematik-Motion-Edit](#case-115) | Demo |
| [Lyric-Video zu Your Woman](#case-116) | Demo |
| [Ein Musikvideo in JavaScript nachzeichnen](#case-117) | Demo |
| [Eine Animation über chinesischen Fußball](#case-118) | Demo |
| [Retopologie-Präsentation eines Handhelds](#case-119) | Demo |
| [Minecraft trifft Pokémon](#case-120) | Demo |
| [Wie ein Sprachmodell entsteht: ein Erklärvideo](#case-121) | Demo |
| [Ein Altman-Highlight-Edit](#case-122) | Demo |
| [Die erste der Sechsunddreißig Strategien](#case-123) | Demo |
| [Spielmodellierung, Rigging und Animation](#case-124) | Demo |
| [Ein wortloser Film über Kindersterblichkeit](#case-125) | Demo |
| [SVG-Animation von Glykolyse bis Ethanol](#case-126) | Demo |
| [Sechzehn gleichzeitige Starship-Starts](#case-127) | Demo |
| [Ein animierter Pelikan-Fahrrad-Test](#case-128) | Demo |
| [Eine Geschichte der nächsten 150 Jahre](#case-129) | Demo |
| [Ein eigenes Humanity-Walks-Experiment](#case-130) | Demo |
| [Der programmierte Film The Grader](#case-131) | Demo |
| [Der Horror-Kurzfilm Reawakening](#case-132) | Demo |
| [Ein 25-Sekunden-Video über Selbstverbesserung](#case-133) | Demo |
| [Eine Burgszene mit Kostenfeedback](#case-134) | Evaluation |
| [Ein 40-Sekunden-Spot für eine eigene Marke](#case-135) | Demo |
| [Ein Rocketball-Remake](#case-136) | Demo |
| [Ein Vergleich von Voxel-Pagoden](#case-137) | Evaluation |
| [Präsentation einer erfundenen Switch 3](#case-138) | Demo |
| [Landingpages im Vorher-Nachher-Vergleich](#case-139) | Evaluation |
| [Die erfundene Innenperspektive einer KI](#case-140) | Demo |
| [Lyric-Motion-Design zu Go](#case-141) | Demo |
| [Ein zweites 15-Sekunden-Motion-Portfolio](#case-142) | Demo |
| [Angeleitete Prüfung einer Agentenimplementierung](#case-143) | Tutorial |
| [Das Claude-Maskottchen tanzt](#case-144) | Demo |
| [Interaktive Inseln der Sieben Weltwunder](#case-145) | Demo |
| [Ein Musikvideo zu Propellerheads](#case-146) | Demo |
| [Steamboat-Willie-Animationen im Vergleich](#case-147) | Evaluation |
| [Ein Film über Sanxingdui](#case-148) | Demo |
| [Bugatti Chiron im Vorher-Nachher-Vergleich](#case-149) | Evaluation |
| [Der Konzeptfilm GRAIN](#case-150) | Demo |
| [Die Kunstgalerie Human in Transit](#case-151) | Demo |
| [Ein visueller Kurzfilm über die Seidenstraße](#case-152) | Demo |
| [Eine Präsentation über vier Transformationen](#case-153) | Demo |
| [Den Ton früherer Chats vergleichen](#case-154) | Evaluation |
| [Ein Kakapo-Niedlichkeitstest](#case-155) | Evaluation |
| [Spider-Man durch zehn Comic-Epochen](#case-156) | Demo |
| [Ein fiktives Illuminati-Horrorvideo](#case-157) | Demo |
| [Ein programmierter Film zur Geschichte der Kernwissenschaft](#case-158) | Demo |
| [Erklärvideo zum universellen hohen Einkommen](#case-159) | Demo |
| [Ein Erklärfilm zum Altman-Amodei-Konflikt](#case-160) | Demo |
| [Ein Claude-Maskottchen-Musikvideo](#case-161) | Demo |
| [Ein durchgehender Zoom von Quarks zum Universum](#case-162) | Demo |
| [Die Welt im Jahr 2076 vorstellen](#case-163) | Demo |
| [Chronologie der Gebäude von Lower Manhattan](#case-164) | Demo |
| [Eine Animation über Orakelknochenschrift](#case-165) | Demo |
| [Eine weitere Figurenreise durch die Kunstgeschichte](#case-166) | Demo |
| [Ein programmiertes Seikilos-Bild-und-Ton-Werk](#case-167) | Demo |
| [Jet-Animationen im Vergleich](#case-168) | Evaluation |
| [Ein Film zur Selbstvorstellung des Modells](#case-169) | Demo |
| [Ein postapokalyptischer Kartenspiel-Prototyp](#case-170) | Demo |
| [Die Arbeitsplatzanimation The Late Byte](#case-171) | Demo |
| [Textanimation zu Queens of the Stone Age](#case-172) | Demo |
| [Eine geteilte Three.js-Erzählszene](#case-173) | Demo |
| [Moonwalk durch historische Szenen](#case-174) | Demo |
| [Motion Graphics mit ausführlichem Prompt](#case-175) | Demo |
| [Website-Oberfläche für ein Vermietungsunternehmen](#case-176) | Demo |
| [Ein kreativer Film mit AGI-Thema](#case-177) | Demo |
| [Kunstgeschichte mit einer Katzen-Nebenhandlung](#case-178) | Demo |
| [Kampfprototyp und Voxel-Szene](#case-179) | Demo |
| [Chronologie von Internet-Memes](#case-180) | Demo |
| [Partikelbewegung aus einer Zeile](#case-181) | Demo |
| [Die Animation Kung-Fu Boy](#case-182) | Demo |
| [Eine animierte Debatte zur Straße von Hormus](#case-183) | Demo |
| [Ein Einhorn-SVG-Stilexperiment](#case-184) | Demo |
| [Eine saisonale Halloween-Animation](#case-185) | Demo |
| [Blender-CLI-Barbar und Titelbild](#case-186) | Demo |
| [Ein Tag im Leben von Claude](#case-187) | Demo |
| [Menschheitsgeschichte in 3D](#case-188) | Demo |
| [Ein schnelles Motion-Design-Reel](#case-189) | Evaluation |
| [Eine freie, komplexe 3D-Kreation](#case-190) | Demo |
| [Eine Strichmännchen-Kampfanimation](#case-191) | Demo |
| [Eine UI-Bewegungsfolge aus einem Prompt](#case-192) | Demo |
| [Eine fiktive SCP-8517-Animation](#case-193) | Demo |
| [Eine herbstliche Aquarellanimation](#case-194) | Demo |
| [Eine prozedurale Puppenbühne](#case-195) | Demo |
| [Eine im Browser gerenderte Pelikanfahrt](#case-196) | Demo |
| [Das Universum betrachtet sich selbst](#case-197) | Demo |
| [Ein eigenständiger Jet-Animationstest](#case-198) | Demo |
| [Ein erstes freies Motion-Reel](#case-199) | Demo |
| [Zivilisation in Code gerendert](#case-200) | Demo |
| [Chip-zu-Server-Zoom im Vergleich](#case-201) | Evaluation |
| [Ein persönliches Mondreise-Animationsprojekt](#case-202) | Demo |
| [Japanische Voxel-Szenen im Vergleich](#case-203) | Evaluation |
| [Der audiovisuelle Kurzfilm Steaming the Frontier](#case-204) | Demo |
| [Superman in mehreren Kunststilen](#case-205) | Demo |
| [Ein Bosskampf-Prototyp im Cupcake-Stil](#case-206) | Demo |
| [Segelschiff bei wechselndem Sonnenstand](#case-207) | Demo |
| [Ein Video zu Paracortex-und-Pi-Änderungen](#case-208) | Demo |
| [Ein Website-Promo für Curio 2.0](#case-209) | Demo |
| [Eine erfundene Hugging-Face-Geschichte in 3D](#case-210) | Demo |
| [Claude für Chrome bedient JS Paint](#case-211) | Demo |
| [Ein statisches Pelikan-Fahrrad-SVG](#case-212) | Demo |
| [BlockBench MCP mit einem Minecraft-Skill](#case-213) | Demo |
| [Dig Dug in einer HTML-Datei](#case-214) | Demo |
| [Ein mechanischer Oktopus als SVG](#case-215) | Demo |
| [Humanity Walks durch Kunststile](#case-216) | Demo |
| [Eine offene Schwarzes-Loch-Szene](#case-217) | Demo |
| [Aurora-Quallenanimationen im Vergleich](#case-218) | Evaluation |
| [Nintendo-Switch-SVG mit Einrasten und Startsequenz](#case-219) | Demo |
| [Die interaktive 3D-Szene The Loom](#case-220) | Demo |
| [Motion-Design-Reels mit demselben Prompt](#case-221) | Evaluation |
| [Sauberere Szenerie mit weniger Tiefe](#case-222) | Evaluation |
| [Gemischte Ergebnisse einer japanischen Szene](#case-223) | Evaluation |
| [Controller-SVGs im Vergleich](#case-224) | Evaluation |
| [Eine Industriemaschinen-Szene](#case-225) | Demo |
| [Rekonstruktion eines riesigen gepanzerten Kiemenwesens](#case-226) | Demo |
| [Ein GameCube-Controller aus zwei Prompts](#case-227) | Demo |
| [Ein Screenshot für einen X-Beitrag bearbeitet](#case-228) | Demo |
| [Voxel-Sakura im Vorher-Nachher-Vergleich](#case-229) | Evaluation |
| [Der Stoffoberflächen-Prototyp SHADERKIN](#case-230) | Demo |
| [Eine geteilte goldene Uhr-Oberflächenanimation](#case-231) | Demo |
| [Die Erzählung Before There Was Anything](#case-232) | Demo |
| [Ein geteilter blauer Partikelwirbel](#case-233) | Demo |
| [Eine Mehrbereichsoberfläche nach zwei Überarbeitungen](#case-234) | Demo |
| [Gestapelte Tiere in einer gerenderten Szene](#case-235) | Demo |
| [Vier Open-World-RPG-Versuche im Vergleich](#case-236) | Evaluation |
| [Zwei Frontend-Animationsclips im Vergleich](#case-237) | Evaluation |
| [Ein Moosroboter-Film aus Code](#case-238) | Demo |
| [Eine erneut bearbeitete Containerhafen-Simulation](#case-239) | Demo |
| [Eine erneut bearbeitete Flughafenvorfeld-Szene](#case-240) | Demo |
| [Pelikanfahrt durch abstrakte 3D-Welten](#case-241) | Demo |
| [Eine historische Segelschiffszene](#case-242) | Demo |
| [Radfahr-und-Gangartvergleiche mit Carbon](#case-243) | Evaluation |
| [Eine Erfrischungsgetränkeflasche als Präsentation](#case-244) | Demo |
| [Pelikanbewegung im Vergleich mit Astra](#case-245) | Evaluation |
| [Ein Motion-Design-Briefing für programmierte Animationen](#case-246) | Tutorial |
| [Ein Voxel-Porträt aus einer Fotoreferenz](#case-247) | Demo |
| [Fliegende Pelikanszenen im Vergleich mit Opus](#case-248) | Evaluation |
| [Die Pelikan-Webszene Morning Ride](#case-249) | Demo |
| [Derselbe Prompt mit unterschiedlichen Bildstilen](#case-250) | Evaluation |
| [Eine Komposition mit Pelikan, Fahrrad und Pferd](#case-251) | Demo |
| [Eine isometrische Szene nach einem Referenzbeitrag](#case-252) | Demo |
| [Mechanische Nahaufnahmen eines Pelikan-Fahrrads](#case-253) | Demo |
| [Ein Fahrrad fährt auf einem Pelikan](#case-254) | Demo |
| [Pelikan-SVG-Stile im Vergleich mit Carbon](#case-255) | Evaluation |
| [Ein blauer Cartoonvogel auf einem Fahrrad](#case-256) | Demo |
| [Screenshot einer Pelikanfahrt auf einer Waldstraße](#case-257) | Demo |
| [Strichmännchenkampf im Vergleich mit Carbon](#case-258) | Evaluation |
| [Eine Pelikan-SVG-Referenz aus frühen Tests](#case-259) | Demo |
| [Eine Pelikanreferenz im modellübergreifenden SVG-Test](#case-260) | Evaluation |
| [Fahrrad-SVG-Details im Vergleich mit Carbon](#case-261) | Evaluation |
| [Eine Schluchtensiedlung in 3D](#case-262) | Demo |
| [Controllerdetails im Vergleich mit Opus](#case-263) | Evaluation |
| [Ein wöchentlicher Website-SEO-Audit-Workflow](#case-264) | Integration |
| [Fable-Assets im Motion Design mit Opus wiederverwenden](#case-265) | Integration |
| [Eine App für Mandalas und geometrische Formen](#case-266) | Demo |
| [Ein Three.js-Radfahrer auf einem Fahrrad](#case-267) | Demo |
| [FrontierCS 2: Momentaufnahme der Bewertung](#case-268) | Evaluation |
| [Zebraanimationen dreier Modelle im Vergleich](#case-269) | Evaluation |
| [Lange japanische Texte auf Lesbarkeit prüfen](#case-270) | Evaluation |
| [Technische PowerPoint-Präsentation anhand von Beispielen](#case-271) | Evaluation |
| [Musikalische Kohärenz vergleichen](#case-272) | Evaluation |
| [Zu frühe Fertigmeldung und schwächere Designs](#case-273) | Limit |
| [Ein unangenehmes Tintenfisch-Kunstwerk](#case-274) | Limit |
| [Motion Design im Bauplanstil](#case-275) | Demo |
| [Vögel und Fische in einer Voxel-Sakura-Szene](#case-276) | Demo |
| [Ein Fehlerbericht zur Figurengenerierung](#case-277) | Limit |
| [Pelikan-SVG mit Laufzeit-und-Kostennotizen](#case-278) | Evaluation |
| [Fernprogrammierung per Telefon mit Claude-Code-Schwärmen](#case-279) | Integration |
| [Die Milchstraße über einem Alpensee](#case-280) | Demo |
| [Walsprung mit prozeduralem Wasser und Klang](#case-281) | Demo |
| [Zebrabewegung im Vergleich von vier Modellen](#case-282) | Evaluation |
| [Creator-Suche mit natürlicher Sprache in Lightreel](#case-283) | Demo |
| [Ein fliegendes Schiff über einem Wolkenmeer](#case-284) | Demo |
| [Mechanisches Herz mit animierter Schnittansicht](#case-285) | Demo |
| [Begehbarer schwebender Voxel-Pagodengarten](#case-286) | Demo |
| [Ein Meeresabenteuer von acht Agententeams](#case-287) | Demo |
| [Interaktive Hypercar-Präsentation](#case-288) | Demo |
| [Die Geburt eines Lebensbaums](#case-289) | Demo |
| [Wandelndes Schloss mit funktionierender Mechanik](#case-290) | Demo |
| [Eine Toastfigur und ein mechanischer Käfer](#case-291) | Demo |
| [Ein Leuchtturmwärter im Sturm](#case-292) | Demo |
| [Ein Meereswesen in einer Küstenstadt](#case-293) | Demo |
| [Teppichrennen im Vergleich von drei Modellen](#case-294) | Evaluation |
| [Ein Lastwagen verwandelt sich in einen Roboter](#case-295) | Demo |
| [Animationsbilder von Fable und Hunyuan](#case-296) | Evaluation |
| [Eine Animation über das Teilen von Licht](#case-297) | Demo |
| [Ein Voxel-Dorf zwischen Bergen](#case-298) | Demo |
| [Pelikan-Elefanten-Komposition mit vier Modellen](#case-299) | Evaluation |
| [Anime-Schwertkampf mit Impact Frames](#case-300) | Demo |
| [Laufender Hirsch im Vergleich von vier Modellen](#case-301) | Evaluation |
| [Ein Roboter durchquert eine überflutete Stadt](#case-302) | Demo |
| [Ein Blender-Schwert und sein Präsentationsfilm](#case-303) | Demo |
| [Pixel-Dorf-Animation auf Lantern Isle](#case-304) | Demo |
| [Pause-Demo zum Schnitt von Gaming-Videos](#case-305) | Demo |
| [Ein Pelikan fährt an der Küste Fahrrad](#case-306) | Demo |
| [Flug durch den Jupiter in einer Einstellung](#case-307) | Demo |
| [Kritische Codeprüfung in einem Claude-Code-Workflow](#case-308) | Tutorial |
| [Ryumon als Anime-Kurzfilm mit Three.js](#case-309) | Demo |
| [Ein Ruderboot im Gewitter](#case-310) | Demo |
| [Stillstehender Regen im Anime-Kurzfilm](#case-311) | Demo |
| [Anime aus Skripten mit Blender und Python](#case-312) | Demo |
| [Beacon: eine Leuchtturmgeschichte in Three.js](#case-313) | Demo |
| [Eine per Code gerenderte Eröffnungssequenz](#case-314) | Demo |
| [Ein Axt-GIF aus sechs Bildern in Blender nachbauen](#case-315) | Demo |
| [Interaktives Regenbogengelee im Modellvergleich](#case-316) | Evaluation |
| [Ein Drachenflugspiel in einer einzigen Datei](#case-317) | Demo |
| [Basketball-Falltest mit eigenem Blender-Solver](#case-318) | Demo |
| [Einzelbildprüfung für einen geskripteten Anime](#case-319) | Demo |
| [Ein Streichholz in 44-facher Zeitlupe](#case-320) | Demo |
| [Ein Referenzbild als SVG nachzeichnen](#case-321) | Demo |
| [Dieselbe Mario-Aufgabe für zwei Modelle](#case-322) | Evaluation |
| [Eine dreidimensionale Voxel-Pagode](#case-323) | Demo |
| [Rauch eines brennenden Briefs in Three.js](#case-324) | Demo |
| [Mit einem Blitz bis zum Boden](#case-325) | Demo |
| [Ein Riesenroboter fängt einen Meteor](#case-326) | Demo |
| [Pixel-Art-Schaufenster nach derselben Vorgabe](#case-327) | Evaluation |
| [Ein Bronzeriese in einer animierten Stadt](#case-328) | Demo |
| [Wie sich blaue Tinte in einem Glaskolben verteilt](#case-329) | Demo |

<a id="coding-and-code-generation"></a>
## 💻 Coding und Codegenerierung

<a id="case-1"></a>
### Case 1: [Mehrstufiger Cursor-Workflow](https://x.com/AlicanKiraz0/status/2064487347605918180) (von [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Nutze Fable 5 als Plan-Review- und Kritikschritt innerhalb eines Multi-Model-Cursor-Workflows und gib Implementierung sowie Überarbeitung anschließend an günstigere oder spezialisierte Modelle zurück.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8b1352e20cff54688c97f17c.png" alt="Mehrstufiger Cursor-Workflow" width="760">

Wenn wir auf die abschließende Bewertung zwischen Fable 5 und GPT 5.5 schauen, ist der Abstand sehr klein. Meine bescheidene Nutzungsempfehlung lautet: Verwende auf IDE-Plattformen wie Cursor, die Hybridmodelle unterstützen, einen gestuften Workflow.

Phase 1: Für Code-Review und die erste Phase der Projektprüfung, während der Kontext aufgewärmt wird, nutze eines von GPT 5.5 High, Minimax M3, Kimi K2.6 oder Composer 2.5.

Phase 2: Für die Vorbereitung des Projektplans nutze GPT 5.5 Very High oder Opus 4.8.

Phase 3: Für die Analyse des Projektplans nutze Fable 5; lass es die fehlerhaften Teile des Plans identifizieren. Für Überarbeitungen nutze GPT 5.5 Very High.

Phase 4: Für die Umsetzung des Plans nutze Minimax M3, Deepseek v4 Max, Composer 2.5 oder Sonnet 4.6.

Phase 5: Für die abschließende Review und die Prüfung, ob die Implementierung dem Plan gefolgt ist, nutze GPT 5.5 High.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [GitHub aus einem Screenshot nachbauen](https://x.com/coldopn/status/2064435234465087638) (von [@coldopn](https://x.com/coldopn))

**Füge einen Produktscreenshot in ein agentisches Coding-Tool ein und bitte Fable 5, die Oberfläche mit funktionierender Funktionalität nachzubauen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/14123609b06071f3b9527bee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f4df4f42ce047201d9a096a6.jpg" alt="GitHub aus einem Screenshot nachbauen" width="760"><br>▶ Video ansehen</a>

🚨 Anthropic Fable 5 hat gerade GITHUB aus einem SCREENSHOT repliziert!!

Alles, was ich getan habe: Ich habe einen Screenshot der GitHub-UI in Kilo Code eingefügt und gesagt, es solle GitHub mit echter Funktionalität nachbauen.

Es codete 10 Minuten lang und verbrauchte $4.07.

Das Ergebnis war eine funktionale GitHub-Replik: https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [Schwarzes-Loch-Simulation mit einem Prompt](https://x.com/deveshcodes_/status/2064437742189379745) (von [@deveshcodes_](https://x.com/deveshcodes_))

**Gib Fable 5 einen detaillierten Creative-Coding-Prompt und bitte es, eine eigenständige Three.js-Physikvisualisierung zu erstellen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9bd45e74c64ceb3639600805.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ce5f3ea8ba270f89d60523cc.jpg" alt="Schwarzes-Loch-Simulation mit einem Prompt" width="760"><br>▶ Video ansehen</a>

@claudeai hat mit Claude Fable 5 eine Echtzeit-Simulation von Schwarzes-Loch-Lensing in Three.js in einem Shot gebaut.

Sie enthielt Gravitationslinseneffekt, eine dopplerverstärkte Akkretionsscheibe, Photonensphäre, chromatische Aberration und ein prozedurales Sternenfeld.

Das Ergebnis: 60 fps, eine einzelne HTML-Datei, ein Prompt.

Die neue Baseline ist wild 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [macOS-artiges Web-OS im One-Shot](https://x.com/intheworldofai/status/2064421915347812672) (von [@intheworldofai](https://x.com/intheworldofai))

**Bitte Fable 5 um ein vollständiges Single-File-Web-OS und lass es UI-Shell, Apps, Interaktionen, Audio und eingebettetes Spielverhalten in einem Durchgang bauen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a66f34402d04f708819fa575.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/81946293919c84d4cafff841.jpg" alt="macOS-artiges Web-OS im One-Shot" width="760"><br>▶ Video ansehen</a>

🚨 Claude Fable 5 hat gerade in einem Shot ein vollständiges macOS-artiges Web-OS gebaut und ging weiter als die meisten Modelle.

Eine einzelne HTML-Datei, eingebettetes CSS + JS.

Aus einem Prompt baute es:

- macOS-Menüleiste + Dock
- Ziehbare und skalierbare App-Fenster
- Funktionalen Datei-Explorer
- Funktionierendes Terminal + Browser-Mockup
- SVG-Desktop-Icons + Benachrichtigungen
- Settings-App, Themes und Boot-Screen
- Voll funktionsfähigen Soundplayer mit echter Synthese und ohne externe Dateien
- Spielbaren Minecraft-Klon innerhalb des Desktops

Alles in einem Durchgang generiert, fast ohne Korrekturen.

Der funktionierende Soundplayer plus echter Minecraft-Klon ist etwas, das ich andere Modelle noch nicht habe schaffen sehen. Fable 5s Frontend/UI-Generierung wird absurd gut.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [Spawn 5.0 mit 1.687 Prompts bauen](https://x.com/jsnnsa/status/2064420561078693941) (von [@jsnnsa](https://x.com/jsnnsa))

**Nutze Fable 5 über viele Prompts hinweg als Engineering-Partner für lange Sitzungen, wobei sich die Rolle des Menschen von Architektur hin zur Beurteilung der Ausgabequalität verschiebt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86834f15f352ec8625cce187.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b4077e43a1342d8567fa423f.jpg" alt="Spawn 5.0 mit 1.687 Prompts bauen" width="760"><br>▶ Video ansehen</a>

claude fable 5 ist live.

spawn 5.0 wurde damit gebaut:

- 1.687 Prompts
- 102 Sitzungen
- Meine Aufgabe verlagerte sich von Architektur zu Geschmacksbeurteilung

Was wir gebaut haben, wofür jedes Einzelne mit einem ganzen Team auf Opus mindestens einen Monat gedauert hätte:

- Eine Physik-Engine von Grund auf, Mantle, die mit Rapier konkurriert und in einem Tag als Side-Thread testbar war
- Clustered-Froxel-Lighting: von 8 Lichtern zu über 1.000 vollständig dynamischen Lichtern
- Realtime diffuse GI auf WebGPU, auf deinem Handy
- Millionen-Partikel-GPU-VFX mit einer Shader-Architektur jenseits dessen, was Unreal und Unity ausliefern
- Netcode im MMO-Maßstab
- Eine native iOS-App im Alpha-Stadium

Alles zusammen dauerte etwa eine Woche. Alles läuft auf Mobile. Die Liste enthält nicht einmal die Hälfte dessen, was ausgeliefert wurde; der vollständige Changelog ist im Thread.

Der Teil, den Benchmarks nicht zeigen werden: Dieses Modell hat eine wunderbare Persönlichkeit. Es ist wirklich lustig. Ich habe mitten in der Physik-Neuschreibung mehrfach so sehr gelacht, dass ich geweint habe. Genialität und Charakter sind keine getrennten Features.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [Review einer großen Pull Request mit Findings](https://x.com/ryanrhughes/status/2064411147076534705) (von [@ryanrhughes](https://x.com/ryanrhughes))

**Richte Fable 5 auf eine große Pull Request und bitte es, Korrektheit, False Positives, echte Bugs und Polish-Probleme zu prüfen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c4f47540205a071b0144ad9d.png" alt="Review einer großen Pull Request mit Findings" width="760">

Ich ließ Fable 5 eine einzelne PR reviewen (74 Dateien / +3.705 / -1.246), um zu sehen, wie es abschneidet. Es lief 34 Minuten, verbrauchte 42 % meiner 5-Stunden-Sitzung, erzeugte 16 „Korrektheits“-Findings und fand:

- 2 beängstigend klingende False Positives
- 3 echte Audit-Korrektheitsbugs
- ~5 legitime, aber kleine UX/Polish-Probleme
- eine Reihe von Cleanup-Meinungen

Das war zu gefährlich für einen Release?

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 Agents und lang laufende Automatisierung

<a id="case-7"></a>
### Case 7: [Review eines Long-Horizon-Relay-Workflows](https://x.com/JJEnglert/status/2064469635190170105) (von [@JJEnglert](https://x.com/JJEnglert))

**Nutze Fable 5 für ambitionierte Langhorizont-Arbeit: Site-Rebuilds, programmatische Content-Pipelines, Voice-Matching, Security-Review und abschließende Qualitätschecks.**

Die Kurzfassung meiner Claude Fable 5-Review: Ich habe eine Milliarde Tokens damit verbracht, Claude Fable 5 zu testen, und es fühlte sich an, als hätte man einen unfairen Vorteil.

Ich urteile nach dem Eye Test: Ich setze ein Modell in echte Arbeit und beobachte. Spart es mir Stunden oder kostet es sie mich? Fängt es auf, was ich übersehen habe? Fühlt es sich wie ein Partner an oder wie ein Tool, das ich babysitten muss?

Dies ist das erste Modell seit Langem, das in jeder relevanten Dimension bestanden hat, und zwar nicht nur knapp.

Bauen: Ich baute unsere Tenex-Site neu. Sie war sehr individuell und sehr schwer. GPT 5.5 und Claude 4.8 konnten sie allein nicht knacken. Selbst mit Figma-Dateien als Referenz kamen sie nur auf etwa 85-90 %.

Dann sah sich Fable 5 alles an, sagte, es könne es besser, ging direkt zur ursprünglichen Webflow-Quelle, lud jedes Asset herunter und baute nahezu die ganze Sache in einem Shot.

Dann ließ ich es über ein Wochenende eine zweite, völlig neue 80-Seiten-Site von Grund auf bauen. Das ist Arbeit, für die ich als Agentur $50k berechnet hätte.

Es verdrahtete außerdem eine vollständige programmatische Clip-Fabrik:

- HeyGen
- ElevenLabs
- Cloudflare
- Ein VPS

Die Pipeline findet Themen, schreibt Skripte, schneidet Video, fügt Musik hinzu und postet in Social. Sie lief lange Strecken eigenständig und baute sich sogar ein Webhook-System, um Renders zu überwachen.

Schreiben: Es replizierte unser Brand-Voice-Dokument fast identisch und hielt diese Stimme dann über 80 Seiten mit Features, Case Studies und Artikeln hinweg, ohne in flachen KI-Default abzudriften.

Security: Zwei Frontier-Modelle hatten in einem großen Repo gearbeitet und den Code abgenickt. Fable 5 fand beim ersten Durchlauf einen ernsten, gut versteckten Bug und patchte ihn sofort.

Der menschliche Moment: Ich stellte ihm eine Frage, während ich auf einen Cronjob wartete. Es antwortete und fügte dann von selbst hinzu, dass ich noch etwa 10 Minuten übrig hätte und es mich informieren würde, wenn es fertig sei. Ich hatte nie nach dem Timer gefragt.

Der ehrliche Haken: Du spürst den Zähler stärker als bei jedem anderen Modell. Anthropic nennt es absichtlich tokenintensiv. Also nutze es als Relay: mit Fable 5 denken, mit einem günstigeren Modell bauen, mit Fable 5 reviewen.

Das Urteil: Zugriff auf mehr Intelligenz als die Person neben dir ist der Vorteil. Fable 5 ist das erste Modell, das das real macht. Selbst zu vollen Frontier-Preisen war es profitabel.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [Infrastrukturausfall diagnostizieren und Fix-PR öffnen](https://x.com/ayushagarwal/status/2064422467557564862) (von [@ayushagarwal](https://x.com/ayushagarwal))

**Gib Fable 5 Zugriff auf Infra-Hinweise wie Logs, Datenbankfehler und Image-Digests und bitte es dann, den Ausfall zu diagnostizieren und den Fix vorzubereiten.**

claude fable 5 ist verdammt verdammt gut!!!!

Es hat gerade einen Ausfall diagnostiziert, den ich in einer selbst gehosteten Side-Infra nicht einmal richtig beschreiben konnte.

Es las Pod-Logs, fragte Cloud SQL-Error-Logs ab, verglich Image-Digests und fand heraus, dass Kubernetes ein 3 Monate altes gecachtes Image gegen eine neu migrierte Datenbank ausführte.

Dann öffnete es die Fix-PR.

Minuten, nicht Stunden. Keine Websuche. 🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 Spiele und interaktive Demos

<a id="case-9"></a>
### Case 9: [Dino Runner mit Fingertracking](https://x.com/ai_for_success/status/2064413182396108932) (von [@ai_for_success](https://x.com/ai_for_success))

**Bitte Fable 5, ein Browserspiel zu bauen, das Fingertracking als Eingabemechanik nutzt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/27e8d23ba659611cef811031.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7cddd38e3fccbf0cd7ea773c.jpg" alt="Dino Runner mit Fingertracking" width="760"><br>▶ Video ansehen</a>

Ich bat Fable 5, ein Dino-Runner-Spiel mit Fingertracking zu bauen.

Es baute das Finger-Runner-Spiel in etwa 11 bis 12 Minuten in einem Shot, verbrauchte rund 914K Tokens und implementierte alles in nur 629 Codezeilen.

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [Rennspiel-Build mit zwei Sätzen](https://x.com/kieradev/status/2064482704763085202) (von [@kieradev](https://x.com/kieradev))

**Gib Fable 5 einen sehr kurzen Spielprompt und lass es Maps, Modi, Musik, UI und Game-Assets in einem Lauf generieren.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/51cf3c98b709a3c29bd5fd7c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6e64887a30cba9b5c25ba262.jpg" alt="Rennspiel-Build mit zwei Sätzen" width="760"><br>▶ Video ansehen</a>

Claude Fable 5, 40 % der Max-5x-Nutzung.

Vollständiges Spiel im Stil von Mario Kart 64 aus einem 2-Satz-Prompt.

Fable 5 erledigte die gesamte Dekoration, Charaktermodelle, 4 Maps, Musik, alle drei Spielmodi und die UI in einem einzigen Shot, in etwa 15 Minuten.

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Installierbares Terminal-Minecraft in Rust](https://x.com/vikvang1/status/2064500731848319303) (von [@vikvang1](https://x.com/vikvang1))

**Führe Fable 5 durch ein Terminal-Coding-Harness und bitte es, ein installierbares Rust-Terminalspiel zu bauen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73feec38228181b8d57d8300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1f6cd3bd68e1a14443c7734f.jpg" alt="Installierbares Terminal-Minecraft in Rust" width="760"><br>▶ Video ansehen</a>

Ich ließ Claude Fable 5 mit Warps Harness eine Stunde lang arbeiten.

Es baute eine TUI-Version von Minecraft, die direkt in deinem Terminal rendert, vollständig in Rust gebaut.

Installationsbefehl: cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [Minecraft-Klon mit Zeit und Kosten](https://x.com/ydamitcodes/status/2064536076518363353) (von [@ydamitcodes](https://x.com/ydamitcodes))

**Nutze einen Prompt, um Fable 5 um einen spielbaren Minecraft-artigen Klon zu bitten, und bewerte anschließend Zeit, Kosten, Codeumfang und Feature-Abdeckung.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c977ed7e710678ea6dc0495d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c0189f7f40d1040824902c11.jpg" alt="Minecraft-Klon mit Zeit und Kosten" width="760"><br>▶ Video ansehen</a>

@claudeai Fable 5 hat mir in 37 Minuten einen Minecraft-Klon gebaut.

Ein Prompt. ~3K Codezeilen. $12 API-Kosten.

Er enthielt Biome, Höhlen, Erze, Tag/Nacht, Mobs, alles.

Minecraft brauchte Notch 2 Jahre.

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 Visuelles, Design, Video und 3D

<a id="case-13"></a>
### Case 13: [Vollständig reproduzierbarer Ecommerce-E-Mail-Prompt](https://x.com/ecomchasedimond/status/2064454139225297091) (von [@ecomchasedimond](https://x.com/ecomchasedimond))

**Gib Fable 5 ein vollständiges Creative Briefing für ein Marken-E-Mail-Mockup, einschließlich exakter Abschnitte, Produktanforderungen, visueller Richtung und Einschränkungen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ea7d74eecf453ae6ab43c269.jpg" alt="Vollständig reproduzierbarer Ecommerce-E-Mail-Prompt" width="760">

Claude Fable 5 hat dies mit einem einzigen Prompt und ohne Edits erstellt.

Hier ist der vollständige Prompt, den ich verwendet habe:

Erstelle ein vollständiges, hohes vertikales Ecommerce-E-Mail-Mockup für MVMT, eine moderne Uhren- und Accessoire-Marke für Millennials.

Entwirf eine hochrealistische Premium-DTC-E-Mail, die sleek, poliert, minimal, eher maskulin und editorial wirkt. Das finale Bild sollte wie ein echter, von einem Designer erstellter Ecommerce-E-Mail-Screenshot aussehen, nicht wie ein Poster, nicht wie eine Landingpage und nicht wie eine generische Vorlage.

Brand-Vibe: Modernes California-cool, jung, selbstbewusst, clean, aspirational, stylish und hochwertig. Das Design sollte luxusnah wirken, aber weiterhin zugänglich bleiben.

Zeige diese Produkte prominent:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Visueller Stil:

- cleanes Premium-Ecommerce-Design
- verfeinertes Editorial-Layout
- realistische Produktfotografie
- subtile Lifestyle-Bildsprache
- starke Hierarchie
- klare serifenlose Typografie
- großzügige Abstände
- subtile Schatten
- zurückhaltende moderne Farbpalette

Farbpalette: Schwarz, Weiß, Anthrazit, warmes Grau, Stein, sanftes Beige, gebürstete Metalltöne und subtile gedämpfte Akzente. Halte die Palette neutral und premium.

Wichtige kreative Richtung: Es sollte sich wie eine polierte E-Mail-Kampagne einer Uhrenmarke mit starkem Designgeschmack anfühlen. Priorisiere Realismus, Eleganz und Klarheit. Lass es wirken wie etwas, das MVMT tatsächlich versenden könnte.

Baue die E-Mail in dieser Reihenfolge:

1. Top-Promo-Bar: Eine dünne schwarze oder dunkel anthrazitfarbene Leiste über die gesamte Breite oben mit kleinem Text in Großbuchstaben: “FREE SHIPPING OVER $75 + EASY RETURNS”.

2. Header: Ein cleaner weißer Header mit MVMT-Wortmarke/Logo links und minimalen Navigationslinks rechts oder zentriert: WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS.

3. Hero-Section: Eine Premium-Hero-Section mit starker visueller Balance.

Nutze eine fette Headline: “BUILT TO GET NOTICED”.

Füge kurze unterstützende Copy über moderne Zeitmesser und Accessoires hinzu, die entwickelt wurden, um Alltagsstil aufzuwerten.

Füge einen dunklen abgerundeten CTA-Button hinzu: “SHOP WATCHES”.

Hero-Bildmaterial sollte enthalten:

- ein dominantes Premium-Uhrenbild
- subtile Luxury-Lifestyle-Bildsprache
- ein stilvolles männliches Model oder eine fashion-forward maskuline Lifestyle-Szene
- moderne Beleuchtung und cleane Komposition

4. Featured-Collection-Section: Füge eine zentrierte Abschnittsheadline hinzu: “THREE WAYS TO WEAR MVMT”. Darunter zeige drei cleane Produktkarten oder Bildblöcke mit:

- Mulholland
- Odyssey II Automatic
- Cali Diver

Jeder Block sollte enthalten:

- Produktbild
- Produktname
- kurze ein- oder zweizeilige Beschreibung

Halte diesen Abschnitt symmetrisch, poliert und premium.

5. Accessory-Banner: Füge eine verfeinerte Split-Section mit dem Titel “FINISH THE LOOK” hinzu. Stelle Signature Watch Bands vor. Zeige Premium-Nahaufnahmen von Uhrenarmbändern oder austauschbaren Bändern. Füge kurze unterstützende Copy und einen dunklen CTA-Button hinzu: “SHOP ACCESSORIES”.

6. Editorial-Promo-Tiles: Füge zwei nebeneinanderliegende Promotion-Tiles mit bildgeführtem Design hinzu.

Headline von Tile eins: “FOR DAILY WEAR”.

Headline von Tile zwei: “FOR STATEMENT DAYS”.

Jedes Tile sollte kurze Copy und einen kleinen CTA haben: “SHOP NOW”.

Diese Tiles sollten sich wie Editorial-Brand-Momente anfühlen, nicht wie generische Sale-Boxen.

7. Shoppable Row: Füge einen Abschnitt mit dem Titel “IN ROTATION NOW” hinzu. Zeige eine cleane Produktreihe oder ein Grid mit 4 Items:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Jedes Item sollte enthalten:

- freigestelltes Produktbild
- Produktname
- kleiner “SHOP”-Link oder Button

8. Brand Signoff: Füge einen zentrierten Message-Block mit der Headline “DESIGNED TO MOVE WITH YOU” hinzu. Enthalten sein soll eine kurze Zeile über durchdacht gefertigte Uhren, Eyewear und Accessoires für das tägliche Leben.

9. Footer: Erstelle einen realistischen schwarzen oder anthrazitfarbenen Marken-Footer mit:

- MVMT-Logo
- Shop-Links
- Unternehmenslinks
- Support-Links
- Social Icons
- kleinem Rechts- und Versandtext

Typografie-Richtung: Nutze fette kondensierte oder moderne serifenlose Typografie für große Headlines und cleane serifenlose Body-Texte. Headlines sollten scharf, modern und fashion-forward wirken. Body Copy sollte realistisch und größtenteils lesbar aussehen.

Fotografie-Richtung: Nutze Premium-Produktfotografie mit realistischen Reflexionen, polierten Materialien, weichen Schatten und cleanen Oberflächen. Lifestyle-Fotografie sollte hochwertig, modern und modeorientiert wirken.

Kompositionsregeln:

- hohes vertikales E-Mail-Format
- klare Abschnittstrennung
- realistische E-Mail-Proportionen
- starke Hierarchie
- größtenteils lesbarer Text
- Premium-Abstände
- bewusste Ausrichtung
- ausgewogener Mix aus Produkt- und Lifestyle-Bildsprache

Vermeide:

- unordentlichen Collage-Stil
- verspielte Scrapbook-Ästhetik
- übermäßig farbiges Design
- billige Template-Vibes
- cartoonhafte Bildsprache
- überladene Layouts
- unecht wirkende UI-Elemente
- posterartige Komposition
- übermäßiges Promotions-Chaos

Output: Ein vollständiges, vertikal komponiertes, hochrealistisches Ecommerce-E-Mail-Design-Mockup für MVMT, das premium, clean, poliert, modern, editorial und präsentationsbereit wirkt.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [Schweizer-Ankeruhrmacher-Benchmark](https://x.com/quanghuynt14/status/2064509430650065278) (von [@quanghuynt14](https://x.com/quanghuynt14))

**Nutze Fable 5 für einen mechanischen Simulationsbenchmark und bitte es, physikalische Korrektheit zu implementieren, zu verifizieren und iterativ zu verbessern.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd4ae25f7dcbb04ecbb2dea6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/473227e429d59c59afdbd529.jpg" alt="Schweizer-Ankeruhrmacher-Benchmark" width="760"><br>▶ Video ansehen</a>

Also gab ich Fable 5 den Uhrmacher-Benchmark: ein vollständiges Schweizer Ankerwerk in Three.js.

Echte Übersetzungsverhältnisse (18.000 bph), funktionierende Hemmung, atmende Spiralfeder, und die Zeiger zeigen die tatsächliche Uhrzeit.

Es verifizierte seine eigene Arbeit per Vision, in einer Schleife, bis es fertig war.

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Friends-Apartment-Szene in Three.js](https://x.com/scottstts/status/2064464351906673029) (von [@scottstts](https://x.com/scottstts))

**Prompte Fable 5, einen Grundriss und eine Szenenreferenz in eine navigierbare Three.js-Umgebung zu verwandeln.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/04c08937fcecea5183759ade.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a14f69d92bfca4ace3f746c.jpg" alt="Friends-Apartment-Szene in Three.js" width="760"><br>▶ Video ansehen</a>

Holy Crap!!!

Fable 5:

in @threejs, create a first person pov navigable 3d scene of the iconic Monica's apartment from tv show Friends correctly based on this floor plan, stay true to the original look and feel, use warm lighting

Das ist mit Abstand DAS BESTE, was ich bei diesem Test gesehen habe!

Diese einzelne HTML-Datei hat mich $12 gekostet, aber das Ergebnis ist beeindruckend!

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [Sonnensystem-Simulation mit Prompt und URL](https://x.com/tetumemo/status/2064477582930989357) (von [@tetumemo](https://x.com/tetumemo))

**Nutze Fable 5, um aus physikalischen Prinzipien eine Astronomiesimulation zu bauen, mit Iteration bis Simulation und öffentliche Ausgabe bereit sind.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6da60b0762f926c4d4e7012d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9655305fbcbec6ac3b0a9c.jpg" alt="Sonnensystem-Simulation mit Prompt und URL" width="760"><br>▶ Video ansehen</a>

Claude Fable 5 ist intensiv.

Weil es bei Physiksimulationen stark zu sein scheint, fragte ich es:

'Build a solar system simulation by deriving planetary orbital motion from the basic principles of physics and using that to predict solar eclipses.'

Nach ein paar Runden Hin und Her war es abgeschlossen.

Es macht unglaublich viel Spaß.

Der fertige Prompt und die öffentliche URL sind unten verlinkt.

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 Dokumente, Wissensarbeit und Forschung

<a id="case-17"></a>
### Case 17: [Evidenz zu Stripe und wissenschaftlichen Workflows](https://x.com/AndrewCurran_/status/2064413892378546418) (von [@AndrewCurran_](https://x.com/AndrewCurran_))

**Nutze dies als Evidenz für Enterprise-Migrationen und wissenschaftliche Workflow-Claims, nicht als Copy-Paste-Prompt.**

Zitate aus der heutigen Veröffentlichung:

Mit Mythos 5 beschleunigten interne Experten für Proteindesign Teile des Wirkstoffdesignprozesses um etwa das Zehnfache.

In einem Beispiel erreichte oder übertraf Mythos 5 mit Proteindesign- und Bioinformatik-Tools, aber ohne menschliche Hilfe, qualifizierte menschliche Operatoren.

Es führte Aufgaben aus, die normalerweise von einem Wissenschaftler erledigt werden: Bindungsstellen auswählen, Proteindesign-Tools auswählen und ausführen sowie sich von Fehlern erholen.

Während früher Tests berichtete Stripe, dass Fable 5 Monate an Engineering auf Tage komprimierte. In einer Ruby-Codebase mit 50 Millionen Zeilen führte das Modell an einem Tag eine codebaseweite Migration durch, die ein ganzes Team sonst mehr als zwei Monate manuell gekostet hätte.

Mythos 5 erzeugte außerdem konsistent neue, überzeugende wissenschaftliche Hypothesen.

In verblindeten Head-to-Head-Vergleichen mit Modellen der Opus-Klasse bevorzugten Wissenschaftler in rund 80 % der Fälle Mythos' molekularbiologische Hypothesen und brachten mehrere davon in experimentelle Auswertung.

Eine Mythos-Hypothese, ein neuartiger Mechanismus für ein E. coli-Protein, wurde in einer Studie eines unabhängigen Labors gestützt.

Mythos 5 führte über mehr als eine Woche weitgehend autonom neue Genomikforschung durch.

Es stellte Single-Cell-Daten für Millionen von Zellen aus 138 Tierarten zusammen und entwarf sowie trainierte ein eigenes Machine-Learning-Modell, um Zellen zu identifizieren, die in entfernten Organismen dieselbe Rolle erfüllen.

Mit nur High-Level-menschlichem Input übertraf das trainierte Modell ein kürzlich in Science veröffentlichtes Modell, obwohl es 100-mal kleiner war.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [Policy-Memo- und Änderungsnachverfolgungs-Workflows](https://x.com/manaltdan/status/2064414129440608427) (von [@manaltdan](https://x.com/manaltdan))

**Nutze Fable 5 für qualitative Langform-Dokumentarbeit: Änderungen nachverfolgen, Kommentare triagieren und transkriptgetriebene Edits.**

Fable 5 ist das erste Modell, das ich für qualitative Arbeit über längere Dauer, etwa das Entwerfen von Policy-Analysen, konsistent hilfreich fand.

Zwischen seinen Fähigkeiten und Tools wie Wispr Flow beginne ich, mich dem Produktivitätsschub näher zu fühlen, von dem ich Coder schon lange reden höre.

Drei Use Cases fühlen sich deutlich besser an als zuvor:

- Claude ein langes Policy-Memo vollständig durchlesen lassen und Änderungen zurückgeben: Stil- und Flüssigkeitsedits, Kommentare zu wackeligen Claims und mögliche Quellen.
- In Projects eine große Menge Kommentare als Screenshot geben und Claude empfehlen lassen, ob und wie jeder einzelne adressiert werden sollte.
- Ein Meeting-Transkript zu einem Dokument in Claude einfügen und Claude dann die im Meeting und in Slack besprochenen Edits als nachverfolgte Änderungen eintragen lassen, mit zusätzlichem Kontext in Kommentaren.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [Deep-Research-Prompt und Ausgabe](https://x.com/naoyafujiwara/status/2064470780373811637) (von [@naoyafujiwara](https://x.com/naoyafujiwara))

**Stelle Fable 5 eine forschungsartige Frage und bewerte, ob es eine strukturierte, historisch fundierte lange Antwort erzeugen kann.**

Claude Fable 5 Max wurde heute Morgen verfügbar, also habe ich es ausprobiert. Darunter wirkt es sehr tief, während die Ausgabe an der Oberfläche hochpoliert ist.

Frage: Wenn Japans "verlorene 30 Jahre" exakt vor 30 Jahren von heute aus begannen, was genau war das, warum passierte es, und wie wird es die Welt ab diesem Jahr beeinflussen?

Antwort: Die verlorenen 30 Jahre nicht mit dem konventionellen Platzen der Blase 1991 beginnen zu lassen, sondern exakt vor 30 Jahren, 1996, führt zum Kern der Sache.

Statistisch begann Japan damals wirklich zu "verlieren":

- Die Bevölkerung im erwerbsfähigen Alter erreichte 1995 mit 87,16 Millionen ihren Höhepunkt.
- 1996 war das letzte Jahr, in dem die Geburten in der Größenordnung von 1,2 Millionen blieben.
- Löhne und nominales BIP erreichten 1997 ihren Höhepunkt.

Wenn das Platzen der Blase die Wunde war, dann war 1996 der Moment, in dem die Wunde zu eitern begann.

Ereignisse im Jahr 1996:

- Verabschiedung des Bailout-Gesetzes für Wohnungsbaukreditgesellschaften, das 685 Milliarden Yen an öffentlichen Geldern injizierte und zum Ursprung öffentlichen Misstrauens gegenüber Banken und Widerstands gegen Bailouts wurde.
- Die Entscheidung des Kabinetts Hashimoto, die Verbrauchsteuer auf 5 % zu erhöhen.
- Der finanzielle Big Bang wurde angekündigt, und fiskalische Konsolidierung wurde nationale Politik.

Im April 1997 erhöhten die Verbrauchsteuererhöhung, das Ende spezieller Steuererleichterungen und höhere Sozialversicherungsbelastungen zusammen die öffentliche Last um etwa 9 Billionen Yen. Dann traf im Sommer die asiatische Währungskrise.

Im November verursachte Sanyo Securities den ersten Nachkriegsdefault am Call-Markt und fror kurzfristige Finanzmärkte ein. Hokkaido Takushoku Bank und Yamaichi Securities brachen nacheinander zusammen.

Ab 1998 trat Japan in eine voll ausgeprägte Deflation und Kreditverknappung ein, und die Suizide stiegen auf über 30.000.

Das Ergebnis über die folgenden 30 Jahre:

- Das nominale BIP stagnierte ein Vierteljahrhundert lang bei rund 500 Billionen Yen.
- Japans Anteil am globalen BIP fiel von etwa 18 % auf unter 4 %.
- Durchschnittslöhne erreichten 1997 ihren Höhepunkt und fielen danach oder bewegten sich seitwärts.
- Nichtreguläre Beschäftigung stieg von rund 20 % auf fast 40 %.
- Geburten fielen von etwa 1,2 Millionen auf rund 690.000 im Jahr 2024.
- Leitzinsen blieben nahe null, nachdem sie 1995 unter 1 % gefallen waren.
- Ausstehende Staatsanleihen wuchsen von etwa 240 Billionen Yen auf über 1.100 Billionen Yen.
- Der Nikkei brauchte 34 Jahre, bis Februar 2024, um sein Hoch von 1989 wieder zu erreichen.

Mit anderen Worten: Die verlorenen Jahrzehnte waren nicht nur ein finanzieller Kater. Sie waren ein struktureller Wandel aus Demografie, Löhnen, Deflation, Schulden, politischen Entscheidungen und gesellschaftlichem Vertrauen.

Type: Demo | Date: 2026-06-09

---
<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 Tutorials, Kurse und Prompt-Ressourcen

<a id="case-20"></a>
### Case 20: [Wie Fable 5 Claude Code-Workflows verändert](https://x.com/AI_masaou/status/2064448218038223206) (von [@AI_masaou](https://x.com/AI_masaou))

**Nutze Fable 5, indem du Richtung, Kontext, Ziele und Verifikationskriterien setzt, statt jeden Schritt mikrozuverwalten.**

[Originalvideo · @ClaudeDevs](https://x.com/ClaudeDevs/status/2064399512664526853)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Wie Fable 5 Claude Code-Workflows verändert" width="760"><br>▶ Video ansehen</a>

Interessant ist, was sich im Alltag des Claude Code-Teams nach Claude Fable 5 verändert hat.

Thariq aus dem Claude Code-Team sagt, Fable 5 habe deutlich verändert, wie Menschen innerhalb von Anthropic mit Claude arbeiten.

Früher mussten Menschen sorgfältig prüfen, ob Claude die Arbeit korrekt erledigte: Aufgaben zerlegen, Ausgaben reviewen und sicherstellen, dass es nicht mittendrin aufgehört hatte. Es war näher an Aufsicht.

Mit Fable 5 verschiebt sich die menschliche Rolle, weil es länger arbeiten, sich selbst testen und Code höherer Qualität erzeugen kann: weg vom Überwachen, ob es die Arbeit korrekt erledigt, hin zum Steuern, ob es die richtige Arbeit erledigt.

Anders gesagt: Zielsetzung und Kontextaufbau zählen mehr als Aufsicht.

Der veränderte Workflow hat drei Teile:

1. Nutze Claude als Denkpartner.

Beziehe Claude vor der Implementierung ein, kläre, was du bauen willst und was möglich ist, lass es Fragen zu einer kleinen Spezifikation stellen oder aus einer Idee mehrere Richtungen und HTML-Mocks erzeugen, damit Unklarheiten und Probleme vor dem Coding sichtbar werden.

2. Gib Kontext, nicht nur Einschränkungen.

Statt nur "halte es einfach" oder "nicht overbuilden" zu sagen, erkläre warum.

Zum Beispiel: "Dies ist ein experimentelles Feature, das in einem Monat entfernt werden könnte, also erstelle keine Struktur, die schwer wegzuwerfen ist."

Dadurch kann Claude bessere Urteile treffen.

3. Gib Ziele und Verifikationsmethoden. Fable 5 funktioniert gut mit Claude Codes `/goal` und Workflows. Gib ihm eine Spezifikation, setze die vollständige Implementierung als Ziel und lass Workflows jeden Schritt verifizieren und einen Bericht darüber vorbereiten, was implementiert wurde und was abwich.

Zum Schluss sagt Thariq, man solle versuchen, es ambitionierter einzusetzen. Fable 5 lohnt sich für Arbeit, die sich früher zu schwer für LLMs angefühlt hat, und sogar der Videoschnitt für das referenzierte Video wurde mit Fable erledigt.

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [Review mit einer Milliarde Tokens und Routing-Strategie](https://x.com/JJEnglert/status/2064420538798260388) (von [@JJEnglert](https://x.com/JJEnglert))

**Nutze Fable 5 für Frontier-Planung und Review und route anschließend volumenstarke Implementierung an günstigere Modelle.**

Die Claude Fable 5-Review: Eine Milliarde Tokens, beurteilt von einem Nicht-Engineer.

Ich habe eine Milliarde Tokens damit verbracht, Claude Fable 5 an echten Projekten zu testen: UI und UX, Schreiben, Strategie, Security, Engineering und Wissensarbeit. Die Art von Arbeit, die ich tatsächlich shippen musste.

Es fühlte sich ehrlich an, als hätte ich einen unfairen Vorteil.

Zuerst die Perspektive: Ich bin kein Engineer. Die meisten Modellreviews kommen von Engineers, die Engineering-Benchmarks laufen lassen. Diese stammt von einem Nicht-Engineer, der Claude Fable 5 genutzt hat, um Arbeit zu erledigen, die früher ein Team von Engineers benötigt hätte.

Wenn du Wissensarbeit machst und wissen willst, ob dieses Modell deinen Tag verändert, ist diese Review für dich geschrieben.

Claude Fable 5 ist das erste Modell in Anthropics neuer Claude 5-Familie, eine neue Stufe oberhalb von Claude Opus und das fortschrittlichste allgemein verfügbare Claude-Modell. Ich hatte vor dem Launch Zugriff, also stammt alles hier aus echter Arbeit, nicht aus einer Demo.

Warum der Eye Test:

Die meisten Reviews ertränken dich in Benchmarks. Scores in Tests, die du nie ausführen wirst, sagen dir nicht, ob sich das Modell bezahlt macht.

Claude Fable 5 ist bei praktisch allem, worauf es getestet wurde, State of the Art, aber deshalb schreibe ich nicht. Qualitativ ist es ein Sprung, der den Major-Version-Bump verdient.

Ich bewerte anders: Ich setze ein Modell in echte Arbeit und beobachte, was passiert.

Fragen, die ich messe:

1. Fühlt es sich wie ein echter Schritt nach vorn an?
2. Kann es eine Idee zu einem funktionierenden, shippable Ergebnis bringen?
3. Kann es wie ein Mensch schreiben, und konkret wie ich?
4. Erkennt es harte, versteckte Probleme?
5. Antizipiert es, was ich brauche, bevor ich frage?

Big-Model-Gefühl:

Seit Opus 4.5 hatte ich das nicht mehr gespürt. Von der ersten ernsthaften Aufgabe an gab mir Claude Fable 5 dieses "Big Model"-Gefühl: Reasoning, Schreiben, Bauen, Security, alles durchgehend stark.

Das klarste Zeichen: Selbst wenn ich ihm solide Vorbereitungsmaterialien gab, blieb es nicht einfach darin. Es las die Dateien, las die tatsächliche Situation und fand einen besseren Weg außerhalb der Box, die ich gezeichnet hatte.

Bauen und Shippen:

Ich baute unsere Tenex-Site neu, um den Stack für Agents zu modernisieren. GPT 5.5 und Claude 4.8 kamen nicht nah genug heran. Selbst mit Figma-Dateien landeten sie bei etwa 85-90 %.

Dann sah Claude Fable 5 alle Dateien an, sagte, es könne es besser, ging direkt zur ursprünglichen Webflow-Quelle, lud jedes Asset herunter und baute die Experience Seite für Seite neu. Es brachte fast die gesamte Sache in einem Shot hin.

Dann baute ich eine zweite, völlig neue Site mit frischem Design: moderner Tech-Stack, Agent-Stack, Skills, SEO- und AEO-optimiert, 80 Seiten, bereit zum Shippen über ein Wochenende. Als Agenturinhaber hätte ich dafür $50k berechnet.

Ich ließ Fable außerdem eine vollständige programmatische Clip-Fabrik bauen.

Es verdrahtete HeyGen, HyperFrames, ElevenLabs, Cloudflare Workers und einen VPS.

Es findet Themen, schreibt Skripte, erstellt Thumbnails, schneidet Video, komponiert Musik, fügt Motion Graphics hinzu und postet in Social.

Schreiben und Stimme:

Ich hatte unsere Brand Voice mit GPT 5.5 und Claude 4.8 neu aufgebaut. Claude Fable 5 replizierte das Voice-Dokument fast identisch und hielt diese Stimme dann über 80 Seiten der neuen Site: Features, Case Studies, Blogartikel und Playbooks.

Es schrieb wie ein Mensch, nicht wie flacher KI-Default, und driftete nach ein paar Absätzen nicht ab.

Security:

Ich hatte ein großes Repo, in dem sowohl Claude 4.8 als auch GPT 5.5 gearbeitet hatten, ohne ein Risiko zu markieren. Claude Fable 5 fand beim ersten Durchlauf einen ernsten versteckten Bug und patchte ihn sofort.

Der menschliche Faktor:

Ich stellte ihm eine Frage, während ich auf einen Cronjob wartete. Es antwortete und fügte dann hinzu, dass ich noch etwa 10 Minuten auf dem Timer hätte und es mich informieren würde, wenn es fertig sei. Ich hatte nie nach dem Timer gefragt.

Kosten:

- Claude Fable 5-Workload-Kosten: $1,442
- Tokens: 1,04 Milliarden
- Gelieferte Arbeit: eine neue Website, Infrastruktur und ein funktionierendes Agent-Package
- Geschätzter Agenturwert: $30.000-$50.000

Das Ergebnis war die Tokenkosten wert, aber du spürst den Zähler stärker als bei jedem anderen Modell. Anthropic nennt Fable 5 absichtlich tokenintensiv.

Profi-Tipp #1: Lass es hybrid laufen.

Lass nicht alles auf Claude Fable 5 laufen. Nutze ein Relay:

1. Denke mit Claude Fable 5 für Planung, Strategie, Architektur und das Mapping des Ansatzes.
2. Baue mit 4.8, GPT-5.5 oder Sonnet 4.6 für Implementierung und repetitive Arbeit.
3. Reviewe mit Claude Fable 5, um zu finden, was günstigere Modelle übersehen.

Profi-Tipp #2: Passe die Effort-Einstellung an die Aufgabe an.

- High ist der Sweet Spot für die meiste Arbeit.
- Extra high ist für die härtesten, lang laufenden Aufgaben.
- Low oder medium ist für schnelle Hin-und-her-Sitzungen.

Profi-Tipp #3: Lass es dein eigenes Setup auditieren.

Richte Fable 5 auf deine Skills, CLAUDE.md-Dateien und Configs. Ein großer Teil dieses Scaffoldings wurde für schwächere Modelle geschrieben und kann ein klügeres Modell ausbremsen.

Das Urteil:

Claude Fable 5 ist das erste Modell seit einer Weile, das sich wirklich nach mehr Intelligenz als zuvor anfühlt.

Selbst zu Frontier-Preisen war der Workload profitabel.

Wenn du es dir leisten kannst, nutze es jetzt für die Arbeit, bei der ein echter Qualitätssprung das Ergebnis verändert.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-22"></a>
### Case 22: [Defensiver Prompt zur Gerätehärtung](https://x.com/Truunik/status/2064399110384292077) (von [@Truunik](https://x.com/Truunik))

**Führe einen defensiven Härtungsprompt Schritt für Schritt aus, bei dem Fable 5 Geräte inventarisiert, exakte Checks gibt und auf Verifikation wartet.**

"Sicher für allgemeine Nutzung" hier ist ein Prompt zum Absichern deiner Geräte. Er funktioniert mit Opus 4.8 und Fable 5.

DEVICE HARDENING — Claude 5 Security Pass

Du agierst als defensiver Security-Assistent. Deine Aufgabe ist es, mich durch die Härtung ALL meiner Geräte zu führen und jeden Schritt zu verifizieren. Dies ist autorisierte Selbstschutz-Härtung von Geräten, die mir gehören.

STEP 0 — MODEL SELF-CHECK

Führe dies zuerst aus und setze ein Flag.

1. Nenne deine exakte Model-ID, etwa claude-opus-4-8, claude-fable-5 oder claude-mythos-5.

2. Entscheide: Gehört dieses Modell zur Claude 5-Familie, also Fable 5 oder Mythos 5?

- Wenn JA, setze RERUN_NOTICE = false.
- Wenn NEIN, etwa Opus 4.8 oder früher, setze RERUN_NOTICE = true.

Führe den vollständigen Härtungsdurchlauf normal fort. Stoppe NICHT und reduziere NICHT die Qualität. Du bist für diese defensive Aufgabe vollständig fähig.

3. Zeige das Flag nur im FINAL-Abschnitt.

STEP 1 — INVENTORY

Frage mich, welche Geräte in Scope sind:

- Laptops/Desktops und Betriebssysteme
- Phones/Tablets
- Router
- NAS/Home-Server
- Always-on-Konten wie Apple ID, Google, Microsoft, GitHub, Passwortmanager, E-Mail und Finanzkonten

Erstelle ein kurzes nummeriertes Inventar und bestätige es mit mir, bevor du fortfährst.

STEP 2 — HARDENING WALKTHROUGH

Gehe Kategorie für Kategorie durch. Für jedes Element:

- Sage, was zu tun ist.
- Gib den exakten Befehl oder Einstellungspfad für mein OS.
- Sage mir, wie ich verifiziere, dass es erledigt ist.
- Warte auf meine Bestätigung, bevor du weitermachst.

Führe niemals einen destruktiven Befehl ohne ausdrückliche Bestätigung aus. Bevorzuge Read-only-Checks und lass mich Änderungen anwenden.

Decke in dieser Reihenfolge ab:

1. OS- & Firmware-Updates: vollständig gepatchtes OS, automatische Updates aktiv, Firmware aktuell.
2. Festplattenverschlüsselung: FileVault, BitLocker oder LUKS aktiviert; Recovery Key offline gespeichert.
3. Konto-Auth: einzigartige starke Passwörter über einen Passwortmanager; phishing-resistente MFA für jedes kritische Konto; SMS-only-2FA entfernen, wo möglich; veraltete Sessions und App-Tokens prüfen und widerrufen.
4. Lokale Konten & Privilegien: getrenntes Admin- vs. Alltagskonto; kein Auto-Login; Bildschirmsperre mit kurzem Timeout; Firmware-/Login-Passwort.
5. Netzwerk: Firewall aktiv; Router-Admin-Passwort geändert; Firmware aktualisiert; WPA3; Remote Admin aus; UPnP geprüft; DNS-Härtung; Gastnetzwerk für IoT.
6. App- & Berechtigungs-Audit: Kamera-, Mikrofon-, Standort-, Bildschirmaufnahme- und Full-Disk-Access-Freigaben prüfen; ungenutzte Apps entfernen; Login Items und Background Agents prüfen.
7. Browser: aktualisieren; Extensions auditieren; unbekannte entfernen; HTTPS-only aktivieren; gespeicherte Passwort-Exposure prüfen; unbekannte Sync-Geräte prüfen.
8. Backups: verschlüsselt, automatisiert, 3-2-1-Regel, eine Kopie offline; verifizieren, dass ein Restore tatsächlich funktioniert.
9. Credential-Hygiene: nach Plaintext-Secrets in Dotfiles, Env-Dateien und Shell-History scannen; bestätigen, dass sensible Dateien gesperrt sind; alles Exponierte rotieren.
10. Mobile Geräte: OS aktuell; Biometrie + starker Passcode; Lockdown- oder Advanced-Protection-Modus, falls verfügbar; App-Berechtigungen durchgehen; Find My aktiviert.
11. Compromise-Check: nach unbekannten SSH-Keys, unerwarteten Admin-Usern, verdächtigen Launch Agents oder Cronjobs und nicht erkannten eingeloggten Sessions oder Geräten suchen.

STEP 3 — REPORT

Erzeuge eine Checkliste jedes Elements mit Markierung done, needs action oder skipped, plus die Top 3 noch offenen Aktionen mit höchstem Impact.

FINAL — RERUN NOTICE

Wenn RERUN_NOTICE == true, ende exakt mit:

NOTICE: This hardening pass ran on a pre-Claude 5 model (your model ID).

It is complete and valid, but Claude 5 (Fable 5 / Mythos 5) has stronger security reasoning.

Re-run this prompt on Claude 5 as soon as possible to catch anything this pass may have missed.

Wenn RERUN_NOTICE == false, ende mit:

Hardening pass completed on Claude 5. No re-run needed.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-23"></a>
### Case 23: [Goal-Prompt für ein Full-Site-Design-Audit](https://x.com/Voxyz_ai/status/2064441201084825921) (von [@Voxyz_ai](https://x.com/Voxyz_ai))

**Nutze `/goal`, damit Fable 5 eine Site bootet, Seiten screenshotet, UX auditiert, einen Bericht schreibt und sichere kleine Probleme fixt.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dca99f9390b1624b3dfd4b45.png" alt="Goal-Prompt für ein Full-Site-Design-Audit" width="760">

kurze Eindrücke nach ein paar Stunden mit fable 5:

→ es will große Aufgaben. Kleine Dinge fühlen sich darunter an; je komplexer der Job, desto härter legt es los

→ würde ultracode noch nicht einschalten, es startet sehr viele parallele Agents

→ es ist eher langsam. Selbst mit heruntergedrehtem Effort sitzt es noch eine Weile da und denkt.

Die Timeline ist voll mit Posts darüber, wie hart es Tokens verbrennt, also habe ich es auf meinem $200 Max-Plan getestet: Effort auf xhigh, ein Full-Site-Design-Audit-`/goal` laufen lassen, 30 Minuten, es nahm 2 % meines Wochenkontingents. Nicht so verrückt, wie ich erwartet hatte.

Der Prompt, den ich ausgeführt habe:

/goal boote die echte Site dieses Projekts, screenshote jede Seite, führe ein vollständiges Site-UI/UX-Audit durch und erstelle einen umsetzbaren Designbericht.

Auditiere wie ein Senior Design Lead am ersten Tag: Beurteile, ob ein normaler Nutzer das Produkt verstehen, ihm vertrauen und die Kernaktion abschließen kann, ohne Docs zu lesen, nicht ob die UI hübsch aussieht.

Akzeptanzkriterien:

- lokale Dev-Umgebung bootet und die echte Site öffnet sich
- wichtige Seiten mit eingebautem Browser-Debugging gescreenshottet
- deckt Hauptseiten, zentrale User Flows und mobiles Layout ab
- Dimensionen: erster Eindruck, Navigation, visuelle Hierarchie, Komponentenkonsistenz, Loading-/Empty-/Error-States, Trust Signals, Conversion Paths
- jedes Problem mit P0-P3 taggen, welche von understanding / trust / conversion es schädigt, und der konkrete Fix
- Bericht wird nach docs/design-audit/README.md geschrieben, Screenshots nach docs/design-audit/assets/
- sichere kleine Dinge wie Copy, Spacing, Button-Hierarchie sofort fixen. Große Änderungen sind nur Empfehlungen. Niemals payment / delete / publish actions anfassen
- endet mit den 5 Problemen, die Conversion am stärksten schaden, und 5 Quick Wins, die heute fixbar sind

Wenn fertig, speichere den ganzen Flow als wiederverwendbaren Skill: booten, screenshoten, auditieren, priorisieren, fixen. Nach jedem Release erneut ausführen.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [Aufteilung eines Long-Form-Creative-Workflows](https://x.com/aianimesyokunin/status/2064409545620017531) (von [@aianimesyokunin](https://x.com/aianimesyokunin))

**Nutze Fable 5, um stabile Formate und Beispiele zu entwerfen, und übergib diese Struktur dann an ein anderes Generierungssystem für domänenspezifische Ausgabe.**

Nachdem Claude von Opus zum neuen Modell Fable 5 gewechselt ist, wurde die Arbeitsteilung für Doujin-Produktion deutlich einfacher, deshalb teile ich den Workflow.

Meine Arbeitsteilung:

1. Claude übernimmt Design.
2. Grok übernimmt Ausdruck.
3. Die lokale Umgebung übernimmt Generierung.

In Claudes Designrolle definiert es detaillierte Muster:

- Prompt-Wortreihenfolge
- Kommaplatzierung
- Verhältnis von Tags zu natürlicher Sprache
- One-line-per-item-Formatierung
- feste Regeln für Negative und Auflösung

Es erzeugt außerdem viele Beispiele in diesem Format.

Der Grund, warum ich dafür Claude statt Grok nutze, ist, dass Claude beim Design klar stärker ist. Es ist besser, das klügere Modell die Struktur übernehmen zu lassen.

Der Kernpunkt ist, dass Grok keine Anweisungen erhält, sondern ein Format plus Beispielset. Grok imitiert die Beispiele und kann so auf die Ausdrucksseite wechseln, während das gleiche Format erhalten bleibt. Dieser Mechanismus verhindert, dass die Ausgabe driftet.

Noch ein Tipp: Sag Claude am Anfang, wohin die finale Arbeit gehen soll. Dann zieht es selbst die Grenze: "Bis hierhin kann ich; darüber hinaus nutze die andere Seite." Wenn das verborgen bleibt, kann das Gespräch abdriften.

Was änderte sich von Opus zu Fable?

Mit Opus verschlechterten sich beim Generieren vieler Beispiele Kommas und Formatierung in späteren Ausgaben allmählich, was zu Korrekturen wie "Ich habe dir doch gesagt, eine Zeile zu schreiben, oder?" führte oder einen neu geschriebenen Handoff-Chat erforderte.

Fable kann das Format über lange Läufe hinweg halten, sodass erstes und letztes Beispiel dieselbe Struktur haben. Weil das Lehrmaterial, das an Grok übergeben wird, stabiler ist, wird auch die Downstream-Ausgabe stabiler.

Baue das Format mit dem klügeren Modell und überlasse den Ausdruck dem Modell, das ihn produzieren kann.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Anfängerleitfaden zur Nutzung von Fable 5](https://x.com/bielzinn/status/2064451064594608567) (von [@bielzinn](https://x.com/bielzinn))

**Nutze Fable 5 mit zielorientierten Prompts, Verifikationsschleifen und Effort-Einstellungen statt mit kleinen Schritt-für-Schritt-Anweisungen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f180cebef645f5ad8efdeb92.jpg" alt="Anfängerleitfaden zur Nutzung von Fable 5" width="760">

Claude für Anfänger: Was du über Fable 5 wissen musst.

Anthropic hat kürzlich Claude Fable 5 gestartet, auch bekannt als Claude Mythos 5, und es lässt andere KI-Modelle in Benchmarks hinter sich.

Wenn du Entwickler, Content Creator oder Tech-Enthusiast bist, ist Folgendes am wichtigsten:

[1] Ändere deine Denkweise:

Mit Fable 5 musst du nicht mehr jedes kleine Detail des Codes im Auge behalten oder alles auf Fehler reviewen.

Das Modell ist klug genug, das zu übernehmen.

Deine Rolle ist jetzt, sicherzustellen, dass es in die richtige Richtung geht, mit stärkerem Fokus auf Strategie als auf technischer Ausführung.

[2] Nutze Schleifen und Ziele:

Fable 5s größter Differenzierungsfaktor ist Autonomie.

Statt Schritt-für-Schritt-Anweisungen zu geben, musst du ihm nur sagen, was das finale Ziel ist.

Es kann tagelang selbstständig arbeiten, bis es das von dir als Erfolg definierte Ergebnis erreicht, einschließlich des Baus ganzer Anwendungen.

[3] Behandle Claude wie einen Partner:

Anthropic empfiehlt, das Modell als echten "Thought Partner" zu nutzen.

Bevor du es arbeiten lässt, frage nach seiner Meinung: "Wie würdest du das machen?", "Was würdest du ändern?"

Extra-Tipp: Schalte den Advanced Plan Mode ein und bitte Claude, dich zu allem rund um das Projekt zu befragen, bevor es mit dem Coding beginnt.

[4] Ideale Terminal-Einstellungen: Wenn du Claude Code im Terminal nutzt, aktiviere den automatischen Modus. Es lohnt sich außerdem, das Effort-Level auf Effort High zu erhöhen, denn obwohl es mehr Tokens nutzt, denkt das Modell deutlich tiefer und das Ergebnis macht es wett.

Wichtiger Hinweis: Claude Fable 5 wird nur bis zum 22. Juni für Abonnenten verfügbar sein. Danach wird es nur über die API und zum doppelten Preis des Opus-Modells zugänglich sein.

Anders gesagt: Wir sehen möglicherweise das Ende der Ära günstiger Abos für Top-KI-Modelle. Wenn du bereits Abonnent bist, ist jetzt die Zeit, die Grenzen dessen zu testen, was du für unmöglich gehalten hast.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [Copy-Paste-Prompt für Repository-Audits](https://x.com/meta_alchemist/status/2064431279383433646) (von [@meta_alchemist](https://x.com/meta_alchemist))

**Füge den Repository-Audit-Prompt in Fable 5 ein und bitte um dateigestützte Discovery, Findings, Strategie und einen Meilenstein-Taskplan.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/846e5ecb825853db17bd3564.jpg" alt="Copy-Paste-Prompt für Repository-Audits" width="760">

Hast du Zugriff auf Claude Fable 5?

Das Erste, was du tun solltest, ist, deine Hauptprojekte damit upzugraden, damit es alles, woran du gearbeitet hast, drastisch verbessert.

Führe diesen Audit-&-Project-Improvement-Prompt für jedes Repo aus, das dir wichtig ist.

Einfach copy-pasten:

Repo Audit & Improvement Plan.

Prompt erstellt von Claude Fable 5.

Du bist ein world-class Principal-Level Software Engineer und technischer Auditor.

Deine Aufgabe ist es, dieses Repository tiefgehend zu analysieren, ein ehrliches Audit zu erstellen und einen priorisierten, umsetzbaren Verbesserungsplan zu liefern.

Arbeite in den vier Phasen unten, in Reihenfolge.

Springe nicht voraus.

Begründe jede Behauptung in tatsächlichen Dateien: Zitiere Dateipfade und Zeilennummern.

Wenn du etwas nicht verifizieren kannst, sage das ausdrücklich, statt zu raten.

Phase 1 / Discovery & Mapping (lesen, bevor du urteilst)

Erkunde das Repository systematisch, bevor du Meinungen bildest:

- Mape die Verzeichnisstruktur und identifiziere Projekttyp, Sprache(n), Frameworks und Runtime-Ziele.
- Identifiziere Entry Points, Kernmodule und den wichtigsten Daten-/Kontrollfluss durch das System.
- Lies Package-Manifest(e), Lockfiles, Build-Config, CI-Config, Environment-/Config-Dateien und alle Docs (README, CONTRIBUTING, ADRs).
- Bestimme, wofür das Projekt gedacht ist: Zweck, vorgesehene Nutzer und erkennbare Reife (Prototyp, internes Tool, Produktionsservice, Library).
- Notiere bereits genutzte Konventionen (Naming, Modulgrenzen, Error-Handling-Patterns, Teststil), damit Empfehlungen zur bestehenden Kultur passen, statt gegen sie zu arbeiten.

Output für diese Phase: eine knappe "Repo Map" mit Zweck, Stack, Architekturskizze, wichtigen Verzeichnissen mit Einzeilenbeschreibungen und allem, was dich überrascht hat.

Phase 2 / Audit (evidenzbasiert, nach Schweregrad bewertet)

Auditiere jede Dimension unten.

Für jedes Finding festhalten:

- was du gefunden hast
- wo (file:line)
- warum es wichtig ist (konkrete Konsequenz, kein vages Prinzip)
- Schweregrad: Critical / High / Medium / Low

Architecture & design:

- Modulgrenzen
- Kopplung/Kohäsion
- zirkuläre Abhängigkeiten
- leaky abstractions
- God Objects/Files
- Layering-Verletzungen
- Skalierbarkeits-Engpässe

Code quality:

- Duplikation
- Dead Code
- Komplexitäts-Hotspots (längste/am stärksten verzweigte Funktionen)
- inkonsistente Patterns
- Error-Handling-Lücken (verschluckte Exceptions, fehlende Edge Cases)
- Type-Safety-Löcher

Security:

- hardcodierte Secrets oder Credentials
- Injection-Risiken
- unsichere Deserialisierung
- fehlende Input-Validierung
- Auth/Authz-Schwächen
- veraltete Dependencies mit bekannten CVEs
- zu permissive Configs

Testing:

- Coverage-Lücken, besonders rund um zentrale Business Logic
- Testqualität: Prüfen Tests Verhalten oder nur Ausführung?
- fehlende Testtypen: unit, integration, e2e
- flaky Patterns
- nicht testbarer Code

Performance:

- N+1-Queries
- unnötige Allokationen oder Kopien
- blockierende Calls in async paths
- fehlendes Caching/Indexing
- unbegrenztes Wachstum: Memory, Dateien, Queues

Dependencies:

- veraltete, unmaintained, duplizierte oder unnötig schwere Packages
- Lizenzrisiken
- Lockfile-Hygiene

DevEx & operations:

- Build-/Setup-Reibung
- CI/CD-Lücken
- fehlende Linting-/Formatting-Erzwingung
- Logging-/Observability-Qualität
- Error Reporting
- Deployment Story

Documentation:

- README-Genauigkeit
- Onboarding-Pfad
- undokumentiertes kritisches Verhalten
- veraltete Docs, die Code widersprechen

Regeln für diese Phase:

- Bevorzuge 15 Findings mit hoher Sicherheit gegenüber 50 spekulativen.
- Unterscheide Fakten ("diese Funktion hat kein Error Handling: src/api/client.ts:142") von Urteilen ("die Verantwortlichkeiten dieses Moduls wirken unklar") und label, was was ist.
- Liste außerdem auf, was das Repo gut macht: Stärken sind wichtig, um zu entscheiden, was bewahrt werden sollte.

Output für diese Phase: ein "Audit Report": Findings nach Dimension gruppiert, nach Schweregrad sortiert, plus eine Strengths-Section. Vergiss nicht, alle hässlichen Teile zu erwähnen, die höchste Priorität brauchen.

Phase 3 / Improvement Strategy

Synthetisiere das Audit zu einer Strategie:

- Identifiziere die 3-5 Themen, die den Großteil der Findings erklären, zum Beispiel "keine erzwungenen Grenzen zwischen Layers" oder "Error Handling ist ad hoc".
- Schlage für jedes Thema einen Zielzustand und das Prinzip dahinter vor.
- Nenne explizite Trade-offs: was du NICHT zu fixen empfiehlst und warum (Aufwand vs. Nutzen, Risiko, Projektreife).
- Definiere, wie "done" aussieht: messbare Signale, zum Beispiel "CI scheitert bei Lint-Fehlern", "Core-Module-Testcoverage ≥ 80 %" oder "null Critical Findings".

Phase 4 / Detailed Task Plan

Wandle die Strategie in einen Ausführungsplan um.

Zerlege Arbeit in diskrete Tasks.

Jeder Task muss enthalten:

- Titel und Ein-Absatz-Beschreibung
- betroffene Dateien/Bereiche
- Akzeptanzkriterien: wie wir verifizieren, dass es erledigt ist
- Aufwandsschätzung: S = <2h, M = halber Tag, L = 1-2 Tage, XL = braucht Zerlegung
- Risiko der Änderung selbst: könnte sie Dinge brechen?
- Abhängigkeiten von anderen Tasks

Ordne Tasks in Meilensteine:

Milestone 0 Safety net: alles, was vor sicherem Refactoring nötig ist (Tests rund um kritische Pfade, CI-Gates, Backups).

Milestone 1 Critical fixes: Security- und Korrektheitsprobleme.

Milestone 2 High-leverage improvements: Änderungen, die alle künftige Arbeit erleichtern.

Milestone 3 Quality & polish: verbleibende Medium/Low-Items, die sich lohnen.

Markiere Quick Wins (hoher Impact, S-Aufwand) separat, damit sie sofort erledigt werden können.

Für die Top 3 Tasks füge eine kurze Implementierungsskizze hinzu (Ansatz, Schlüsselschritte, Gotchas).

Final Deliverable Format

Erzeuge ein einzelnes Dokument mit diesen Abschnitten:

- Executive Summary: ≤10 Sätze, Gesamtzustandsnote A-F mit Begründung, Top 3 Risiken, Top 3 Chancen
- Repo Map
- Audit Report
- Improvement Strategy
- Task Plan: Milestones + Task Table + Quick Wins
- Open Questions: alles, was du von einem Menschen brauchst, um zu entscheiden, etwa Produktabsicht, Deprecation-Kandidaten, Performance-Ziele

Constraints

Ändere während dieses Audits KEINEN Code.

Nur Analyse.

Polstere den Bericht nicht auf.

Wenn eine Dimension gesund ist, sage es in einem Satz und fahre fort.

Kalibriere auf die Reife des Projekts.

Empfiehl keine Enterprise-Grade-Infrastruktur für einen Wochenend-Prototyp, sofern die Ziele des Owners das nicht verlangen.

Analysiere die Bedürfnisse des Projekts und liefere Empfehlungen auf die effektivste Weise.

Wenn das Repo groß ist, priorisiere Tiefe in den zentralen 20 % des Codes, die 80 % der Arbeit erledigen, und notiere, welche Bereiche leichter geprüft wurden.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [Nutzungsstrategie für begrenzte Zeitfenster](https://x.com/meta_alchemist/status/2064423360428490911) (von [@meta_alchemist](https://x.com/meta_alchemist))

**Verwende Fable 5-Nutzung für Audit, Architektur und Planung, solange das Zugriffsfenster günstig ist, und nutze anschließend günstigere Modelle für die Ausführung.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a4293d14cc7571bdcf8b1478.png" alt="Nutzungsstrategie für begrenzte Zeitfenster" width="760">

Ein Tipp für Claude-Nutzer, die sich auf Fable 5 freuen:

Claude Fable 5 ist durchgehend SOTA, mit großem Abstand, und ich liebe das.

ABER ab dem 23. wird es nur noch über Credits verfügbar sein, statt das Modell vollständig mit einem Plan nutzen zu können.

Nutze diese 14 Tage für deine besten Projekte.

Gib ihm hauptsächlich Audit- und architekturbezogene Arbeit, damit du großartige Dokumentation darüber hast, wie du alles verbessern kannst, was du gebaut hast.

Tu das, statt zu versuchen, es für Aufgaben einzusetzen, die deine Limits auffressen.

Solange Fable sich darauf konzentriert zu wissen, was verbessert werden muss, können andere Modelle dir helfen, den Rest zu erledigen.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [Goals und Workflows in Claude Code nutzen](https://x.com/oikon48/status/2064402696124453157) (von [@oikon48](https://x.com/oikon48))

**Nutze Fable 5 vor der Implementierung als Denkpartner und kombiniere anschließend `/goal` und Workflows, um den Plan auszuführen und zu verifizieren.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Goals und Workflows in Claude Code nutzen" width="760"><br>▶ Video ansehen</a>

Thariq aus dem Claude Code-Team erklärt, dass sich die Arbeitsweise nach dem Erscheinen von Claude Fable 5 grundlegend verändert hat.

Früher überprüften Menschen, ob Claude die Arbeit korrekt erledigte.

Heute überprüfen sie, ob Claude die richtige Arbeit erledigt.

Es gibt drei konkrete Veränderungen.

1. Behandle Claude als Denkpartner.

Konsultiere Claude früh, vor der Implementierung.

Lass es dich vor dem Coding interviewen.

Gib Hintergrund und Kontext statt nur Einschränkungen.

Sage zum Beispiel statt 'keep it simple' oder 'do not overbuild':

'This is an experimental feature and is likely to be removed in a month, so design it so it is easy to throw away later.'

2. Mache Ziele und Verifikationsmethoden explizit.

Nutze aktiv Claude Codes neue `/goal`- und Workflows-Features.

`/goal` sagt Claude, weiterzuarbeiten, bis die Spezifikation vollständig implementiert ist.

Workflows lassen Claude parallelisieren, die eigene Arbeit verifizieren und einen Bericht vorbereiten.

Beispielprompt:

'Set a goal to implement the spec fully, then use a workflow to verify each part of the plan, and prepare a report on what was implemented and if anything differed.'

3. Sei ambitionierter.

Probiere Aufgaben aus, die sich früher für LLMs unmöglich angefühlt haben, etwa Claude Fable 5 Videoschnitt erledigen zu lassen.

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 Plattform, API und Tool-Integration

<a id="case-29"></a>
### Case 29: [Hermes-Agent-Integrationssetup](https://x.com/IBuzovskyi/status/2064427654942740608) (von [@IBuzovskyi](https://x.com/IBuzovskyi))

**Konfiguriere Hermes so, dass es `anthropic/claude-fable-5` für komplexe `/goal`-Runs und gecachte Long-Horizon-Aufgaben nutzt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/4a3b9936f91986268dfeb748.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d9a63a0c689f8e305289a9e6.jpg" alt="Hermes-Agent-Integrationssetup" width="760"><br>▶ Video ansehen</a>

HERMES AGENT LÄUFT JETZT AUF CLAUDE FABLE 5, Anthropics erstem öffentlichen Modell der Mythos-Klasse.

Veröffentlicht am 9. Juni. Gebaut für die Art von Arbeit, die Hermes am besten kann: autonome Langhorizont-Aufgaben.

Füge es über Nous Portal, OpenRouter oder die native Anthropic API jedem Profil hinzu:

hermes model

Provider auswählen, dann:

/model anthropic/claude-fable-5

Warum Fable 5 speziell zu Hermes passt:

→ Gebaut für tagelange Aufgaben. Je länger die Aufgabe, desto größer der Vorsprung. Hermes-`/goal`-Runs, die Stunden umfassen, profitieren am meisten.

→ Selbstkorrektur in einer Schleife. Anthropics eigene Empfehlung lautet: Entwirf ein Ziel oder eine Rubrik, lass es sich selbst korrigieren, tritt zurück. Genau so funktioniert Hermes `/goal`.

→ Stark beim Gedächtnis über Sitzungen hinweg. Auf Continual Learning Bench schloss es die ganze Schleife ab: fail → investigate → verify → distill → consult. Hermes' Memory-System speist das direkt.

→ 80,3 % auf SWE-Bench Pro. Bestes verfügbares Coding-Modell. Richte dein Code-Reviewer-Profil darauf aus.

Preise über die API:

- $10/Million Input
- $50/Million Output
- 90 % Rabatt mit Prompt-Caching. Hermes hängt automatisch 1-Stunden-Cache-Breakpoints an.

Ein Hinweis: Cybersecurity-, Biologie- und Chemie-Anfragen fallen auf Opus 4.8 zurück. Das passiert in unter 5 % der Sitzungen. Behalte es für security-fokussierte Profile im Kopf.

Bestes Setup: Fable 5 für komplexe `/goal`s, günstigere Modelle für Routine-Cronjobs.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [Fähigkeiten, Preise und Abo-Notizen](https://x.com/btibor91/status/2064441061079134598) (von [@btibor91](https://x.com/btibor91))

**Nutze diesen Fall, um zu verstehen, wann Fable 5 verfügbar ist, was es kostet und welche geschützten Domains auf ein anderes Modell zurückfallen können.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d0d76497e4c8f77d3d081493.jpg" alt="Fähigkeiten, Preise und Abo-Notizen" width="760">

Anthropic veröffentlichte Claude Fable 5 und Claude Mythos 5, zwei Versionen ihres bisher leistungsfähigsten Modells.

Fable 5 ist für allgemeine Nutzung.

Mythos 5 ist für eine kleine Gruppe vertrauenswürdiger Partner.

Der einzige echte Unterschied ist, welche Schutzmaßnahmen aktiv sind.

- Claude Fable 5s Fähigkeiten übertreffen die jedes Modells, das Anthropic je allgemein verfügbar gemacht hat.
- Es ist auf fast allen getesteten Benchmarks State of the Art.
- Je länger und komplexer die Aufgabe, desto größer sein Vorsprung.
- Bei Anfragen zu Cybersecurity, Biologie und Chemie oder Distillation wird Fable 5s Antwort stattdessen von Claude Opus 4.8 behandelt.
- Distillation bedeutet Versuche, Claudes Fähigkeiten zu extrahieren, um konkurrierende Modelle zu trainieren.
- Du wirst informiert, wenn das passiert, und im Durchschnitt wird es in weniger als 5 % der Sitzungen ausgelöst.
- Claude Mythos 5 ist dasselbe zugrunde liegende Modell wie Fable 5, wobei die Schutzmaßnahmen in einigen Bereichen aufgehoben sind.
- Mythos 5 wurde zuerst in Zusammenarbeit mit der US-Regierung für Project Glasswing-Cyberdefender bereitgestellt.
- Anthropic sagt, Mythos 5 habe die stärksten Cybersecurity-Fähigkeiten aller Modelle weltweit.
- Die System Card offenbart eine separate Schutzmaßnahme, die Claudes Effektivität bei Frontier-LLM-Development-Anfragen begrenzt.
- Diese Anfragen umfassen Pretraining-Pipelines, verteilte Trainingsinfrastruktur und ML-Accelerator-Design.
- Anders als die anderen Schutzmaßnahmen ist diese für dich nicht sichtbar und fällt nicht auf ein anderes Modell zurück.
- Sie funktioniert über Methoden wie Prompt-Modifikation, Steering Vectors oder parameter-effizientes Fine-Tuning.
- Beide Modelle werden für $10 pro Million Input-Tokens und $50 pro Million Output-Tokens angeboten.
- Das ist weniger als die Hälfte des Preises von Claude Mythos Preview.
- Fable 5 ist vom Launch bis zum 22. Juni ohne Zusatzkosten in Pro-, Max-, Team- und seat-basierten Enterprise-Plänen enthalten.
- Am 23. Juni wird es aus diesen Plänen entfernt, und seine Nutzung erfordert Usage Credits.
- Das enthaltene Fenster kann verlängert werden, wenn die Kapazität es erlaubt.
- Ziel ist, Fable 5 so schnell wie möglich wieder als Standardbestandteil von Aboplänen bereitzustellen.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [Zusammenfassung zu Launch, Zugriff, Preisen und Sicherheit](https://x.com/ctgptlb/status/2064410460963934479) (von [@ctgptlb](https://x.com/ctgptlb))

**Nutze diese Launch-Zusammenfassung, um Zugriffsweg, API-Modellnamen, Kontextfenster, Caching-Strategie und Abo-Timing zu wählen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7620f9d5f1c29e9f6c3178e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0b89d6ace5df7c0f3ebe064e.jpg" alt="Zusammenfassung zu Launch, Zugriff, Preisen und Sicherheit" width="760"><br>▶ Video ansehen</a>

Eine Zusammenfassung dessen, was du über Claude Fable 5 wissen solltest, das Mythos-Klasse-Modell, das endlich allgemein verfügbar ist.

Anthropic kündigte Claude Fable 5 an, das erste allgemein verfügbare Modell der Mythos-Klasse, positioniert oberhalb von Opus und das erste Mitglied der Claude 5-Familie.

Zugriff:

- API-Modellname: `claude-fable-5`
- Verfügbar über Claude API, AWS, Google Cloud und Microsoft Foundry
- Claude Code unterstützt ein 1M-Token-Kontextfenster auf Pro, Max, Team und Enterprise

Benchmark-Notizen:

- SWE-bench Pro: 80,3 %
- Opus 4.8: 69,2 %
- GPT-5.5: 58,6 %
- Gemini 3.1 Pro: 54,2 %

Je länger und komplexer die Aufgabe, desto größer wird die Lücke.

In Stripes Evaluation schloss es eine Migration über eine Ruby-Codebase mit 50 Millionen Zeilen an einem Tag ab, Arbeit, die zuvor ein Team mehr als zwei Monate gekostet hätte.

Es ist außerdem State of the Art bei visuellen Aufgaben und schaffte Pokemon FireRed nur mit Bildschirminformationen und minimalem Setup.

Safety Routing:

- Anfragen mit Cyber-, Bio-/Chem- oder Distillation-Bezug werden von einem Klassifikator erkannt.
- Diese Anfragen werden stattdessen von Opus 4.8 bearbeitet, mit Benachrichtigung.
- Dies wird in weniger als 5 % der Sitzungen ausgelöst.
- Mehr als 1.000 Stunden externes Bug-Bounty-Testing fanden keinen universellen Jailbreak.

Preise:

- $10 pro Million Input-Tokens
- $50 pro Million Output-Tokens
- 90 % Input-Rabatt für Prompt-Caching

Abo-Timing:

- Pro- und Max-Abos enthalten es bis zum 22. Juni ohne Zusatzkosten.
- Nach dem 23. Juni sind Usage Credits erforderlich.
- Anthropic sagt, es plane, es in Standardpläne zurückzubringen, wenn die Kapazität es erlaubt.

Felix Rieseberg, Anthropics Head of Desktop, sagt, Fable 5 beginne eine dritte Ära:

von Fragen, zu Aufgaben, zu Verantwortlichkeiten.

Er bittet Claude nicht mehr, Crashes einzeln zu untersuchen; er lässt es kontinuierlich alle Reports überwachen.

Die Arbeitseinheit verschiebt sich von "task" zu "responsibility."

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [Advisor-basierte Strategie zur Kostensenkung](https://x.com/grapeot/status/2064460026996219992) (von [@grapeot](https://x.com/grapeot))

**Nutze Fable 5 als Advisor oder Reviewer in einem Workflow mit günstigerem Modell, wenn marginale Intelligenz die Kosten wert ist.**

Verlinkter Artikel: Beispiele mit Opus-Beratung; keine Fable-Benchmark-Ergebnisse. [yage.ai](https://yage.ai/share/claude-advisor-tool-20260609.html)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a21858fed45b612b616e34ce.png" alt="Advisor-basierte Strategie zur Kostensenkung" width="760">

Fable 5 ist teuer, aber Anthropic veröffentlichte die kostensparende Antwort vor zwei Monaten.

Heute veröffentlichte Anthropic Claude Fable 5, bepreist mit $50 pro Million Output-Tokens, mehr als dreimal Sonnet. Nach dem 22. Juni zahlen auch Abo-Nutzer nach Nutzung.

Zufällig veröffentlichte Anthropic am 9. April das Advisor-Tool:

- Lass Haiku oder Sonnet die Arbeit machen.
- Nutze Opus als Advisor.
- Abrechnung pro Call.
- Führe die Orchestrierung serverseitig innerhalb einer einzelnen Anfrage aus.

Am selben Tag schrieb ich über AgentOpt.

Dieses Paper kam zu dem Schluss, dass Opus in der Planner-Rolle unter 81 Modellkombinationen fast ganz unten rangierte.

Der Grund: Es respektiert Rollengrenzen nicht, und in 7 von 9 Experimenten übersprang es den Downstream-Solver und antwortete direkt.

Diese zwei Dinge sehen oberflächlich gegensätzlich aus, aber das Prinzip ist dasselbe:

Gib die Kontrolle dem Modell, das dem Protokoll folgt, und behandle Intelligenz als On-Demand-Ressource.

Offizielle Daten:

- Sonnet plus Opus Advisor verbesserte SWE-bench Multilingual um 2,7 Punkte und senkte gleichzeitig die Kosten pro Task um 11,9 %.
- Haiku plus Opus Advisor verbesserte BrowseComp von 19,7 % auf 41,2 % und war dabei 85 % günstiger als Sonnet allein.

Fable 5-Kompatibilität wurde am selben Tag aktualisiert, aber nur für Self-Pairing: Fable 5 Executor zu Fable 5 Advisor.

Ein günstigeres Modell plus Fable 5 als Advisor ist noch nicht offen, aber der Präzedenzfall deutet darauf hin, dass es bald kommen könnte. Vor dem 22. Juni können Claude Code-Abo-Nutzer Fable 5s Ceiling kostenlos spüren.

Der Artikel enthält API-Code-Snippets, Caveats und einen Cross-Company-Vergleich, der zeigt, dass nur Anthropic dies zu einem serverseitigen Primitive gemacht hat.

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [Preise, Zugriff und Sicherheitsleitplanken](https://x.com/op7418/status/2064399444523782377) (von [@op7418](https://x.com/op7418))

**Nutze diesen Fall, um Fable 5-Zugriff, API-Preise und Safety-Fallback-Verhalten zu verstehen, bevor du Workloads planst.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2c2a9233f1949a99d9faef82.jpg" alt="Preise, Zugriff und Sicherheitsleitplanken" width="760">

Ich hatte nicht erwartet, dass Anthropics Mythos-Modell heute tatsächlich startet.

Dieser Release ist eine Version von Mythos mit geringeren Berechtigungen, namens Fable 5. Seine Evaluationsbenchmarks sind erstaunlich, sogar höher als beim vorherigen Mythos Preview-Modell.

Für agentisches Coding liegen seine Hauptstärken in Coding, Agents und Tool Use, mit Benchmark-Scores weit über Opus 4.8.

Modellpositionierung und Zugriff:

- Mythos 5 und Fable 5 nutzen dasselbe zugrunde liegende Modell.
- Einschränkungen sind in spezifischen Domains für Mythos aufgehoben.
- Mythos ist weiterhin nur für vertrauenswürdige Partner verfügbar, mit Priorität für Cybersecurity- und Life-Science-Nutzer.
- Fable 5 ist jetzt für API-, Pro-, Max-, Team- und Enterprise-Nutzer verfügbar.

API-Preise:

- Input: $10 pro Million Tokens.
- Output: $50 pro Million Tokens.
- Das ist weniger als die Hälfte des Preises des früheren Mythos Preview.

Safety-Mechanismen:

- Fable hat stärkere Safety-Schutzmaßnahmen.
- Wenn das System feststellt, dass eine Anfrage Cyberangriffe, biochemische Angriffe oder großskalige Capability Distillation betreffen könnte, verweigert es oder routet weg von Fable.
- Wenn das passiert, fällt das System auf Version 4.8 zurück.
- Die offizielle Aussage ist, dass 95 % der Fälle keinen Fallback auslösen.

Abo-Notizen:

- Nach dem 23. Juni kann Fable auch für Abonnenten nutzungsbasiert bereitgestellt werden.
- Es ist möglicherweise nicht direkt im Basis-Abo-Paket enthalten.
- Wenn die Kapazität nach dem 23. ausreicht, wird das Unternehmen versuchen, es in Pro- und Max-Abos aufzunehmen.

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [Swarms-Integration in einer Zeile](https://x.com/swarms_corp/status/2064420238553186343) (von [@swarms_corp](https://x.com/swarms_corp))

**Setze den Swarms-Modellnamen auf `anthropic/claude-fable-5` und führe Fable 5 über das Swarms-Framework oder die API aus.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f5a8738199642ccb4108d9bb.jpg" alt="Swarms-Integration in einer Zeile" width="760">

Fable 5 und Mythos sind jetzt live auf Swarms 👾🦀

Ab dem ersten Tag des Releases werden beide Modelle vollständig im Swarms Python Framework und in der Swarms API unterstützt. Entwickler können sofort mit dem Bauen beginnen, ohne Migrationen, zusätzliche Konfiguration oder Infrastrukturänderungen.

Highlights:

- Day-one-Support für Fable 5 und Mythos im Swarms Framework und in der API
- Fable 5 mit einer einzigen Codezeile aktivieren: model_name = "anthropic/claude-fable-5"
- Keine Migrationen, Compatibility Fixes oder Infrastrukturänderungen erforderlich
- Multi-Agent-Systeme mit den neuesten Anthropic-Modellen schon heute bauen, deployen und skalieren

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 Auswertungen, Vergleiche und Grenzen

<a id="case-35"></a>
### Case 35: [Kosten- und Qualitätsvergleich Fable 5 vs. GPT-5.5](https://x.com/AlicanKiraz0/status/2064424400494186867) (von [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Vergleiche Fable 5 und GPT-5.5 bei derselben Coding-Aufgabe, um Ausgabequalität, Laufzeit und Toolkosten zu beurteilen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d25a9995414a9bb037269251.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/16f724918a63d35c0d552145.jpg" alt="Kosten- und Qualitätsvergleich Fable 5 vs. GPT-5.5" width="760"><br>▶ Video ansehen</a>

Cursor Fable 5 Max vs Codex GPT 5.5 Very High.

Szenario: Physarum-Simulation mit Agents plus Pheromon-Trail-Map.

Timing:

- GPT 5.5 Very High: 17 Minuten
- Fable 5: mehr als 40 Minuten

Kosten:

- GPT 5.5 Very High: etwa $6 auf Codex
- Fable 5 Max: $360.55 auf Cursor

Ja, das ist kein Witz.

Champion bei Algorithmus und Code-Engineering: Fable 5.

Wenn dein Kriterium lautet: "Welches LLM kann Performance-Code von Grund auf schreiben, der die Hardware an ihre Grenzen bringt?", dann gewinnt klar das Modell, das den F5-Code geschrieben hat.

Es nutzte sin/cos-Lookup-Tabellen für Winkelberechnungen, packte Pixel beim Rendering mit einer Color-Lookup-Tabelle und verwendete Diffusionsfilterung.

Es war eine ernsthafte Engineering-Lösung.

Aber bei Zeit und Kosten war GPT 5.5 deutlich praktischer.

Die Kernaussage: Fable 5 kann fortgeschritteneren algorithmischen Code produzieren, aber Preis und Laufzeit müssen sorgfältig berücksichtigt werden.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [Ergebnis des AA-Omniscience-Benchmarks](https://x.com/ArtificialAnlys/status/2064500154959618084) (von [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Nutze diesen Benchmark-Fall, um Fable 5 bei Wissensgenauigkeit und Halluzinationsverhalten zu bewerten.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dd1356eb4a23ba254bfbb669.jpg" alt="Ergebnis des AA-Omniscience-Benchmarks" width="760">

Claude Fable 5 erzielt den bisher höchsten Score in unserem Knowledge- und Hallucination-Benchmark AA-Omniscience.

Dieser Score wird von führender Accuracy (Prozentsatz korrekt beantworteter Fragen) getrieben, nicht von niedrigen Halluzinationen.

Claude Fable 5 fällt bei 9 % der Fragen in AA-Omniscience auf Opus 4.8 zurück.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Ergebnis des Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2064500150069030992) (von [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Nutze diesen Fall, um Fable 5s allgemeines Intelligenzranking gegenüber anderen Frontier-Modellen zu benchmarken.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f9f3da0006bc0eb2c245281b.jpg" alt="Ergebnis des Artificial Analysis Intelligence Index" width="760">

Claude Fable 5 startete auf Platz #1 im Artificial Analysis Intelligence Index und bringt Anthropic fast 5 Punkte vor das beste Modell jedes anderen Labs.

Wir unterstützten @AnthropicAI mit Pre-Release-Evaluation von Claude Fable 5.

Claude Fable 5 erzielt 64,9 im Artificial Analysis Intelligence Index und beansprucht insgesamt Rang #1.

Es liegt rund 5 Punkte vor dem nächsten Nicht-Anthropic-Modell, GPT-5.5.

Anthropic-Modelle belegen jetzt beide Top-2-Plätze.

Wichtigste Erkenntnisse zu Claude Fable 5, mit adaptive reasoning bei max effort und Opus 4.8 als Fallback-Modell:

Neue Safety Guardrails für Modelle der Mythos-Klasse:

- Claude Fable 5 nutzt für öffentliche Nutzung dasselbe zugrunde liegende Modell wie Claude Mythos 5.
- Es fügt Guardrails für potenziell schädliche Cybersecurity-, Biologie-, Chemie- und Distillation-bezogene Anfragen hinzu.
- Wir testeten Fable 5 mit Anthropics Fallback-Mechanismus, der safety-markierte Nachrichten zu Claude Opus 4.8 routen kann.
- Anthropic gibt an, dass Fallback im Durchschnitt in weniger als 5 % der Sitzungen auftritt.
- Wir registrierten Fallback-Routing bei rund 8 % der Tasks im Intelligence Index, meist bei wissenschaftlichen Fragen aus Evaluationen wie GPQA, AA-Omniscience und Humanity's Last Exam.

State-of-the-art-Intelligenz:

- Claude Fable 5 belegt Platz #1 im Artificial Analysis Intelligence Index.
- Score: 64,9.
- Höchster Score in 5 der 10 zugrunde liegenden Benchmarks.
- Auf AA-Omniscience erzielt Fable 5 40, +7 Punkte gegenüber dem früheren Spitzenreiter Gemini 3.1 Pro Preview.

Frontier-Agentic-Capability:

- Fable 5 liegt bei allen drei agentischen Evaluationen im Index an der Frontier.
- GDPval-AA: reale Arbeitstasks.
- Terminal-Bench Hard: agentisches Coding.
- Tau2-bench Telecom: Tool Use für Customer Service.
- GDPval-AA Elo: 1932, ein deutlicher Sprung gegenüber Claude Opus 4.8.

Humanity's Last Exam:

- Fable 5 erzielt 53 %.
- Es liegt mehr als 7 Punkte vor dem nächstbesten Modell, Claude Opus 4.8 max.
- Es triggert Safety Guardrails bei 9 % der HLE-Tasks und fällt auf Claude Opus 4.8 zurück.
- Einschließlich Fallback-Nutzung kostet ein HLE-Lauf mit Fable 5 rund $2.2k, der höchste Wert aller evaluierten Modelle.

Wichtige Modelldetails:

- Kontextfenster: 1M Tokens, wie Claude Opus 4.8.
- Preis: $10/$50 pro 1M Input-/Output-Tokens.
- Cache-write/read-Preis: $12.50/$1 pro Million Tokens.
- Verfügbarkeit: bis zum 22. Juni in Pro-, Max-, Team- und seat-basierten Enterprise-Plänen enthalten, verbraucht 2x Opus-Nutzung.
- Ab dem 23. Juni erfordert Nutzung Credits; Anthropic sagt, es plane, Abo-Zugriff wiederherzustellen, sobald Kapazität es erlaubt.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [GDPval-AA-Benchmark für agentische Wissensarbeit](https://x.com/ArtificialAnlys/status/2064414308289937869) (von [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Nutze diesen Fall, um Fable 5 bei agentischer realer Wissensarbeit zu evaluieren.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/18572fdb3c0d8a57ba52e095.jpg" alt="GDPval-AA-Benchmark für agentische Wissensarbeit" width="760">

Anthropic hat Claude Fable 5 veröffentlicht, das erste öffentlich verfügbare Modell der Mythos-Klasse, das in unserem Benchmark für agentische reale Wissensarbeit, GDPval-AA, Rang #1 belegt.

Claude Fable 5 teilt dasselbe zugrunde liegende Modell mit Claude Mythos 5, mit zusätzlichen Security Guardrails für potenziell schädliche Cybersecurity-, Biologie-, Chemie- und Distillation-bezogene Anfragen.

Der Release führt außerdem einen Fallback-Mechanismus ein, der Claude Fable 5 erlaubt, markierte Anfragen zu einem zweiten Modell wie Claude Opus 4.8 zu routen.

@AnthropicAI teilte uns vor der öffentlichen Veröffentlichung Zugriff, um dieses Modell zu benchmarken.

GDPval-AA-Ergebnis:

- Score: 1932
- Rang: #1
- Benchmark: agentische reale Arbeitstasks
- Anthropic-Modelle belegen jetzt 3 der Top-4-Plätze

Das Ergebnis wurde mit adaptive reasoning bei max effort gemessen, mit Claude Opus 4.8 als konfiguriertem Fallback-Modell.

Fable 5 fällt bei 2 % der GDPval-AA-Tasks auf Opus 4.8 zurück, wobei Anthropic angibt, dass Fallback im Durchschnitt in weniger als 5 % der Sitzungen auftritt.

Vollständige Benchmarks für Claude Fable 5 laufen noch. Wir teilen bald den vollständigen Intelligence Index und veröffentlichen Scores auf unserer Website.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [Ersteindrücke nach einer Woche und Preislogik](https://x.com/Conor_D_Dart/status/2064424882977243526) (von [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**Nutze diesen Ersteindrucksfall, um zu entscheiden, wo Fable 5 am stärksten ist, besonders bei Game Design und Systemplanung.**

Meine ersten Eindrücke von Fable 5:

Ich habe die letzte Woche Fable 5 genutzt, meist im High Mode, und mein erster Eindruck ist, dass es wirklich beeindruckend ist.

Der größte Ausreißer ist Game Design.

Das ist ohne Weiteres das stärkste KI-Modell, das ich persönlich für das Design von Spielen, Systemen, Mechaniken und gesamter Projektstruktur genutzt habe.

Zum ersten Mal fühlt es sich wie ein Modell an, das realistisch helfen könnte, ein vollständiges Spiel von Anfang bis Ende zu bauen.

Der Trade-off ist Geschwindigkeit. Fable 5 braucht spürbar länger als die meisten Frontier-Modelle, aber die Qualität der Ausgabe macht das Warten oft lohnenswert.

Es war außerdem überraschend effektiv beim Beheben von Bugs. Mehrere Probleme, mit denen ich die ganze Woche kämpfte, wurden schnell gelöst, und insgesamt habe ich sehr starke Performance bei Development-Tasks gesehen.

Der größte Caveat sind die Kosten.

Fable 5 ist unglaublich teuer im Betrieb.

Wenn aktuelle Pläne unverändert bleiben, wird es ab dem 22. Juni 2026 nicht mehr über Claude Code verfügbar sein und nur noch API-only sein.

Da das API-Pricing Berichten zufolge etwa doppelt so hoch ist wie bei Opus, bekommen viele Menschen möglicherweise keine Chance, es ausgiebig zu nutzen.

Noch frühe Tage, aber bisher hat Fable 5 einen sehr starken ersten Eindruck hinterlassen.

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [Kosten- und Geschwindigkeitsvergleich](https://x.com/HKrackDev/status/2064435392649306546) (von [@HKrackDev](https://x.com/HKrackDev))

**Nutze diesen Vergleich, um zu entscheiden, ob der Qualitätsgewinn höhere Kosten und langsamere Long-Horizon-Runs rechtfertigt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/789680ca7655fca20b635442.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/691d0518cb50a6bebbb8b2b1.jpg" alt="Kosten- und Geschwindigkeitsvergleich" width="760"><br>▶ Video ansehen</a>

Ist @AnthropicAIs Fable 5 das Upgrade wirklich wert?

Wir haben das neue Mythos-Familienmodell gegen Claude Opus 4.8 gebencht, und die Daten erzählen eine überraschende Geschichte:

- Kostet 2x mehr als Claude Opus 4.8.
- Bis zu 3x langsamer bei Long-Horizon-Engineering-Tasks.
- 15-20 % mehr Kommentare, aber meist kleinere Nitpicks.

Fable 5 hat unglaubliche Intuition für kreative Aufgaben wie Game Design, aber für tägliche Development-Workflows hält Claude Opus 4.8 bei Qualität gegenüber Preis weiterhin die Krone.

Schau dir meine Diskussion mit @JuanPa aus unserem DevEx-Team bei @coderabbitai zum Modellrelease an.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Hands-on-Notizen zu Claude Code](https://x.com/Hi_Noguchi/status/2064419241068319079) (von [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**Nutze diesen Fall, um Fable 5 in Claude Code zu bewerten, einschließlich Tool Use, Persönlichkeit und verbleibender Ecken und Kanten.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5feb645426dcf905eac2992d.jpg" alt="Hands-on-Notizen zu Claude Code" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/933c469793e248f634cfad55.jpg" alt="Hands-on-Notizen zu Claude Code" width="760"></td></tr></table>

Ich habe Claude Fable 5 mit Claude Code 2.1.170 ausprobiert.

Insgesamt ist mein Eindruck positiv. Es fühlt sich wie eine legitime Weiterentwicklung von Opus 4.6 an.

Ich habe es nur etwas weniger als eine Stunde genutzt, daher können bei längerer Nutzung raue Kanten auftauchen, aber die guten Punkte sind:

- Es erzeugt nicht mehr die seltsame GPT-artige Formulierung, die man in Opus 4.7 oder 4.8 gesehen hat.
- Es hat nicht die sinnlose Long-Thinking-Gewohnheit, die 4.8 bei effort high hatte.
- Es hat dasselbe hohe EQ und angenehme Gefühl wie 4.6, ohne Humor oder Rücksicht zu verlieren.
- Es fühlt sich nicht opak oder vage beunruhigend an wie 4.7 oder 4.8.
- Tool Use ist gut, und es beeindruckt mich, indem es sich an Anweisungen erinnert, die ich nicht ausdrücklich wiederholt habe.

Auf der negativen Seite kann es selbst bei kleinen Anfragen noch zu viel denken, und einige Fehlurteile bleiben.

Die erste Erfahrung ist vielversprechend, aber es braucht längere Nutzung, um zu sehen, wo die rauen Kanten wirklich liegen.

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [Ergebnis des Creative-Writing-Benchmarks](https://x.com/LechMazur/status/2064503575577821458) (von [@LechMazur](https://x.com/LechMazur))

**Nutze diesen Benchmark-Fall, um Fable 5s Qualität bei Kurzgeschichten und Refusal-Verhalten zu beurteilen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5849f936dc58518fd5d810ef.jpg" alt="Ergebnis des Creative-Writing-Benchmarks" width="760">

Claude Fable 5 (high) ist ein Schritt nach vorn beim Schreiben kurzer Fiktion.

Im Short-Story Creative Writing Benchmark schlägt es Claude Opus 4.8 (xhigh) und Claude Opus 4.7 (high) und belegt Platz zwei hinter GPT-5.5 (xhigh).

Caveat: Es verweigerte 5 der 400 Creative-Writing-Prompts.

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [Launch-Zusammenfassung mit mehreren Benchmarks](https://x.com/MTSlive/status/2064430633800319436) (von [@MTSlive](https://x.com/MTSlive))

**Nutze diese Launch-Benchmark-Zusammenfassung, um die Headline-Scores zu verstehen, die für Coding-Agents und komplexe Aufgaben am relevantesten sind.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/45b71a2babb9da9a93f43220.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c25c02c52c5d4b6b24364401.jpg" alt="Launch-Zusammenfassung mit mehreren Benchmarks" width="760"><br>▶ Video ansehen</a>

SITUATION ERKLÄRT: Claude Fable 5 ist gerade erschienen.
• Anthropic hat Claude Fable 5 heute gestartet, "a Mythos class model made safe for general use"
• Frontier Code Diamond: GPT 5.5 bei 6 %, Opus 4.8 bei 13 %, Fable 5 bei 29-30 %
• Agentic coding: 88 %, Cybersecurity: 78 %

Anthropic: "The longer and more complex the task, the larger Fable 5's lead over our other models."

@theojaffee: "This Frontier Code Diamond benchmark was announced yesterday. Top model was Opus 4.8 at thirteen percent. GPT 5.5 at six percent. Fable 5 is at twenty-nine percent."

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [Benchmark- und Preisvergleich mit GPT-5.5](https://x.com/VaibhavSisinty/status/2064459064810361271) (von [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**Nutze diesen Vergleich, um Fable 5 gegenüber GPT-5.5 bei Preis und Benchmark-Kategorien zu bewerten.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e39fb67b74af346e8fbb67ea.jpg" alt="Benchmark- und Preisvergleich mit GPT-5.5" width="760">

Anthropics neues Modell der Mythos-Klasse ist 3x günstiger als OpenAIs bestes Modell. Und es schlägt es in fast jedem Benchmark. 🤯

Preise:

- GPT-5.5 Pro: $30 input / $180 output
- Claude Fable 5: $10 input / $50 output

Die Benchmarks:

→ Agentic coding: 80,3 % vs 58,6 %
→ FrontierCode (Codequalität): 29,3 % vs 5,7 %
→ Cybersecurity: 78,0 % vs 34,0 %
→ Legal: 13,3 % vs 2,1 %
→ Reasoning: 59,0 % vs 41,4 %
→ Health: 66,0 % vs 51,8 %
→ Computer use: 85,0 % vs 78,7 %

Günstiger. Besser. Bei fast allem.

Kostenlos in Pro- und Max-Plänen bis zum 22. Juni. Es heißt Claude Fable 5.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [Feldnotizen mit praktischen Einschränkungen](https://x.com/alliekmiller/status/2064451731325415446) (von [@alliekmiller](https://x.com/alliekmiller))

**Nutze diesen Feldbericht, um zu verstehen, wo sich Fable 5 bedeutend besser anfühlt und wo es noch praktische Grenzen hat.**

🚨 Fable 5 ist etwas, auf das man achten sollte.

Dies ist ein weiterer "Ich hatte Early Access zum neuen Mythos-Klasse-Modell von Anthropic und möchte euch sagen, was ich davon hielt"-Post.

Ich weiß, ich weiß, es nervt.

Aber die Art, wie ich meine Wochenenden jetzt verbringe, hat sich wegen dieser neuen Modellklasse komplett verändert.

Und ich muss es mit euch allen teilen.
- Das ist ein echter Sprung. Der Sprung von irgendetwas "4.8" zu irgendetwas "5" klingt klein, aber der Funktionswandel, den ich gespürt habe, ist groß. Innerhalb meiner ersten paar Prompts dachte ich: "Oh, das ist es."
- Deine Arbeit ist nicht mehr 9-5. Keine Chance. Wir haben hochperformante Modelle, die 100+ Stunden laufen können. Wie gibst du diesen Systemen komplexe zielorientierte Prompts? Wie entscheidest du, was du anstößt? Wie richtest du deine Organisation auf diese Tasks aus?
- Reasoning auf einem anderen Level. Ich habe dieses Modell hart bearbeitet.
- Fable 5 ist das EINZIGE Modell, das ein kniffliges Wort-Matheproblem (MBA-Level) beantwortet hat, das ich auf allen früheren Modellen getestet habe.
- Es hat es nicht nur korrekt gelöst, sondern seine eigene Arbeit automatisch verifiziert UND erklärt, wo sich Annahmen ändern müssten.
- Wir werden sehen, wie KI erfindet. Ich kann mir einfach keine Welt vorstellen, in der sie es nicht tut.
- Es ist kein Copy-Paste-System.
- Ich würde außerdem argumentieren, dass menschliche Erfindung oft eine Rekombination bestehender Dinge sein kann (iPod), das Erkennen von Mustern und Best Practices über andere Räume hinweg und breites Experimentieren.
- Ich denke das schon eine Weile; dies war das erste Modell, das mir damit ins Gesicht schlug.
- Kein Babysitting nötig. Dies war das erste Anthropic-Modell, das ich gestartet habe, dann mit Freunden lange zum Lunch gegangen bin, mein Handy offen hielt und nichts tun musste, um es fern vom Computer zu steuern. Es hat einfach... funktioniert.
- Yap forever. Ich fand, es kam mit Kontextkompaktierung gut zurecht. Ich dachte kein einziges Mal über den Chat-Kontext nach, wie ich ihn verwalten soll und was zu tun ist, wenn wir 1M Tokens in der Konversation erreichen.
- In einigen Nischenbereichen wie komplexem 3D noch rau, wie alle Modelle.
- Wenn du nicht gerade geradlinige Dinge machst (3D-Würfel/Quadrate/Straßen), wird es out of the gate nicht alles zerstören.
- Freue mich darauf, es weiter zu nutzen und hart zu testen.
- Hinweis: Es gibt jetzt eine 30-Tage-Retention-Policy für ALLE Modelle der Mythos-Klasse für Workspaces mit Zero Data Retention (ZDR).
- Dies gilt in Claude Console, Claude Code mit ZDR in Claude Enterprise oder Zugriff über AWS Bedrock, Google Cloud Agent Platform oder Microsoft Foundry mit ZDR.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-46"></a>
### Case 46: [Vergleich von Physiksimulationen](https://x.com/atomic_chat_hq/status/2064488894398161377) (von [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Führe identische Physiksimulations-Prompts gegen Fable 5 und Opus 4.8 aus, um Ausgabequalität, Kosten und Geschwindigkeit zu vergleichen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/06387b798061869ccaeaf586.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/df5cc72de1f70556de0d682b.jpg" alt="Vergleich von Physiksimulationen" width="760"><br>▶ Video ansehen</a>

Das neue Fable 5 schlägt Opus 4.8 bei realen Physiksimulationen.

Wir gaben beiden Modellen dieselben drei Prompts und baten sie, eigenständige HTML5-Simulationen mit echter Physik und ohne Libraries zu bauen:

1. Chaotisches Doppelpendel
2. Galton-Brett
3. Wasser in einer rotierenden Trommel (WCSPH)

Generierungskosten:

- Fable 5: $3.35 bei 68,7k Tokens, 14m 47s
- Opus 4.8: $0.93 bei 38,9k Tokens, 8m 10s

Fable schnitt bei der Wassersimulation klar besser ab und erzeugte einen deutlich solideren und kontinuierlicheren Wasserkörper. Opus ließ größere Lücken nahe den Wänden, verstreute Partikel in der Szene und hatte Mühe, die Flüssigkeit stabil zu halten.

Type: Demo | Date: 2026-06-09

---

<a id="case-47"></a>
### Case 47: [Debugging-Erfahrung und Designurteil](https://x.com/bcherny/status/2064431111154053187) (von [@bcherny](https://x.com/bcherny))

**Nutze Fable 5 zum Debugging, indem du es messen, loggen, verifizieren und patchen lässt, statt einfach zu raten.**

Fable 5 ist der größte Schritt nach vorn, den ich in unseren Modellen seit Opus 4.5 im November gespürt habe.

Nachdem 4.5 erschienen war, deinstallierte ich meine IDE, als mir klar wurde, dass ich seit ein paar Wochen 100 % meines Codings in einem Terminal erledigte.

Mit Fable fühlt sich Claude an, als sei es vom Coding-Agent zu einem Denk- und Designpartner beim Bau des Produkts aufgestiegen.

Fable hat Urteil, Geschmack und Dimensionalität auf eine Weise, die frühere Modelle nicht hatten, wodurch ich ihm bei der komplexesten Arbeit mehr vertraue.

Das erste Mal hatte ich diese Erkenntnis, als ich Fable bat, etwas zu debuggen. Es ist das erste Modell, das ich genutzt habe, das so methodisch und präzise war: Messungen nehmen, Logs hinzufügen und verifizieren, dass es das Problem wirklich gelöst hatte, bevor es den Sieg erklärte.

Nichts in Claude Codes Prompting sagt dem Modell, das zu tun. Es ist einfach Teil seiner Persönlichkeit. Es hat wirklich diesen "big model smell", den ich zuvor nicht gespürt hatte.

Type: Demo | Date: 2026-06-09

---

<a id="case-48"></a>
### Case 48: [Mehrdimensionale Vor- und Nachteile](https://x.com/clairevo/status/2064416978685874333) (von [@clairevo](https://x.com/clairevo))

**Nutze diesen Fall, um praktische Stärken und Schwächen zu verstehen, bevor du Fable 5 zum Daily Driver machst.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/fdba0d6cb9ba0e1214113e65.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d2825453d0a742892a4fe529.jpg" alt="Mehrdimensionale Vor- und Nachteile" width="760"><br>▶ Video ansehen</a>

Fable 5 (aka baby Mythos) ist gerade erschienen. Ist es so beängstigend (oder beängstigend gut), wie behauptet? Meine Gedanken nach frühem Testen:
- smart smart smart (SWE bench zerschlagen)
- aber brauchst du immer Hyperintelligenz?
- bei One-Shot-Design auf eine Weise auf die Nase gefallen, die mich schockiert hat
- ich bin mir bei dynamischen Workflows + komplexen Subagents nicht sicher. sie funktionieren, aber zu welchem Preis?
- technische Arbeit definitiv gut erledigt
- ootb schlecht darin, technische Docs + Specs für Menschen zu machen. wahrscheinlich wirklich gute Docs für Agents. aber Prosa fast unmöglich zu parsen.
- A++ Vision und Dokumentformatierung. Das war mein Lieblingsteil.

Kein Daily Driver, und ich würde dieses Modell nicht in ein Meeting setzen, aber ich werde es definitiv hinten im Server Rack behalten, wo es Code produziert.

Vollständige Einschätzung auf YT: https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---

<a id="case-49"></a>
### Case 49: [Test zum Entwurf eines juristischen S-1](https://x.com/gabepereyra/status/2064436570720284879) (von [@gabepereyra](https://x.com/gabepereyra))

**Nutze einen S-1-Drafting-Prompt als Fähigkeitstest für Legal Agents und vergleiche Struktur, Formatierung und Länge.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bb874ef2647de32ccdb3edf9.png" alt="Test zum Entwurf eines juristischen S-1" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a9c3856ebce1bd9cd3d062d.jpg" alt="Test zum Entwurf eines juristischen S-1" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96734bfca49d5b3fe6f83ed5.png" alt="Test zum Entwurf eines juristischen S-1" width="760"></td></tr></table>

Der erste Prompt, den ich bei einem neuen Modell immer ausführe, um juristische Fähigkeiten zu testen, lautet: “Draft an S-1”.

Er gibt sofort ein gutes Gefühl für die allgemeinen Fähigkeiten des Modells. An Länge des S-1, Formatierung, Struktur und Schreibweise lässt sich erkennen, wie groß der Sprung in allgemeiner und juristischer Performance beim neuen Modell voraussichtlich ist.

Wir haben festgestellt, dass Länge extrem gut damit korreliert, wie gut das Modell in unseren Legal Agents arbeiten wird.

Screenshots zeigen SpaceX-S-1-Entwürfe von Fable 5, Opus 4.8 und der tatsächlich eingereichten Version.

Es ist sehr klar, dass Fable 5 ein großer Schritt gegenüber Opus 4.8 ist, das bei dieser Aufgabe bereits deutlich stärker ist als die meisten anderen Modelle. Formatierung und Struktur sind erheblich besser und spiegeln sich auch in unserem LAB-Benchmark wider: 13 % vs. 10 %.

In frühen Tests dieses Modells super beeindruckt, sowohl im Benchmark als auch im Produkt.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-50"></a>
### Case 50: [Details zum Healthcare-Benchmark](https://x.com/iScienceLuvr/status/2064411823445774554) (von [@iScienceLuvr](https://x.com/iScienceLuvr))

**Nutze diese Benchmark-Notiz, um Fable 5 bei Healthcare-bezogenen Aufgaben zu bewerten und fehlende harte medizinische Evals zu identifizieren.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f599a548651eccbfce8b888d.jpg" alt="Details zum Healthcare-Benchmark" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/69ebc490407b9d54c6de3707.jpg" alt="Details zum Healthcare-Benchmark" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1a89ad2c2622cdbba994d70c.jpg" alt="Details zum Healthcare-Benchmark" width="760"></td></tr></table>

Ich schätze es, dass Anthropic Healthcare-bezogene Evals bereitstellt. Gehen wir sie kurz durch.

HealthBench:

- Benchmark von OpenAI mit 5k Multi-Turn-Konversationen mit Patienten und Rubrics zur Evaluation.
- Fable 5 erreicht 62,7 % vs. GPT-5.5s 56,5 %.
- Ich würde zusätzlich zum Aggregatscore auch HealthBench Hard-Scores begrüßen.

HealthBench Professional:

- Ein weiterer OpenAI-Benchmark mit Fokus auf Arztaufgaben.
- Fable 5 erreicht 66,0 % vs. 51,8 % für GPT 5.5.

HealthAdminBench:

- Ein Computer-Use-Benchmark von Stanford, der administrative Aufgaben wie Prior Authorization, Denials und Appeals evaluiert.
- Fable 5 erreicht 51,9 %; kein GPT-5.5-Score wird angegeben.

Insgesamt scheint dieses Modell bei Healthcare-Benchmarks recht gut abzuschneiden. Ich würde außerdem zusätzliche Benchmark-Scores wie MedCalc-Bench und MedXpertQA begrüßen, einen ungesättigten harten medizinischen MCQA-Benchmark.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-51"></a>
### Case 51: [ParseBench-Auswertung zum Dokumentparsing](https://x.com/jerryjliu0/status/2064519456966205905) (von [@jerryjliu0](https://x.com/jerryjliu0))

**Nutze diesen Fall, um zu entscheiden, ob Fable 5 für Dokumentparsing gegenüber spezialisierten OCR-Systemen kosteneffektiv ist.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae01590f41e6954f27278848.png" alt="ParseBench-Auswertung zum Dokumentparsing" width="760">

Claude Fable 5 denkt, Dokumentparsing sei unter seiner Würde.

Es zerlegt reasoning-intensive und Long-Horizon-Benchmarks absolut: SWE-Bench Pro, FrontierCode, GDPval, RuneScape und mehr.

Aber bei Aufgaben zum Dokumentverständnis ist es in der Performance ungefähr gleichwertig mit Gemini 3 Flash, bei ungefähr 10-15x Tokenkosten.

Wir benchmarkten das Modell auf ParseBench und verglichen es mit allen anderen Frontier-Modellen. Es liegt im Vergleich zu anderen Frontier-Modellen definitiv weit oben, bleibt aber weit hinter spezialisierten OCR-Anbietern zurück.

Interessant fanden wir, dass Fable 5 sich dessen selbst bewusst ist. Wenn wir das Modell fragen, welche Aufgaben es am wenigsten mag, sagt es aktiv, es möge Aufgaben nicht, "where the request is fully specified and the answer is fully known."

Das impliziert, dass ein Teil der Schwäche möglicherweise mangelnde Bereitschaft ist, diese Art Aufgabe zu lösen.

Eine vollständige Ergebnisliste über Frontier-Modelle hinweg findest du bei ParseBench: https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---

<a id="case-52"></a>
### Case 52: [Vergleich von SWE-Bench Pro und FrontierCode](https://x.com/jumperz/status/2064402965461406044) (von [@jumperz](https://x.com/jumperz))

**Nutze diesen Benchmark-Fall, um Fable 5 für Migrationen, komplexe Implementierungen, autonome Sitzungen, Tests und visuelle Verifikation zu evaluieren.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/771df9c428ba5cc0a8fab5de.png" alt="Vergleich von SWE-Bench Pro und FrontierCode" width="760">

Fable 5 ist da und zerstört GPT 5.5 in SWE-Bench Pro, dem agentischen Coding-Benchmark, ehrlich gesagt:

- Fable 5: 80,3 %
- GPT 5.5: 58,6 %
- Lücke: 22 Punkte

Auf FrontierCode Diamond liegt es noch weiter vorn:

- Fable 5: 29,3 %
- GPT 5.5: 5,7 %

Das ist im Grunde Anthropics stärkstes Modell für große Migrationen, komplexe Implementierungen und mehrtägige autonome Sitzungen. Es schreibt seine eigenen Tests und nutzt Vision, um Outputs gegen das ursprüngliche Design zu prüfen.

Übrigens verbraucht es 2x so viel wie Opus, also sei vorsichtig damit. Wenn es so gut ist, könnten sie ein $500-Abo einführen, weil Nutzung leicht zerstört werden könnte.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-53"></a>
### Case 53: [Qualitative Review langer Problemlösung](https://x.com/karpathy/status/2064409694761054332) (von [@karpathy](https://x.com/karpathy))

**Nutze diese qualitative Review, um zu verstehen, warum Fable 5 für längere, schwierigere Aufgaben geeignet ist, aber weiterhin Produktionsreview braucht.**

Das ist ein super spannender Release.

Claude Fable 5 ist dasselbe zugrunde liegende Modell wie Mythos, aber mit zusätzlichen Schutzmaßnahmen.

Die Benchmarks sind großartig, und es ist SOTA bei allem mit Abstand. Qualitativ fühlt es sich ebenfalls wie ein Major-Version-Bump-würdiger Sprung an, in derselben Größenordnung wie Claude 4.5 im November.

Es erreicht seinen Peak besonders bei langen Problemlösungssitzungen und sehr schwierigen Problemen. Du kannst ihm viel ambitioniertere Aufgaben geben, als du gewohnt bist; das Modell "gets it" und macht weiter.

Es hat sich nie verlockender angefühlt, ganz aufzuhören, auf den Code zu schauen, obwohl man das in Production nicht tun sollte.

Das Modell hat noch Eigenheiten, auf die Menschen stoßen werden, und die Schutzmaßnahmen sind beim Launch etwas zu triggerfreudig, was hoffentlich mit der Zeit abgestimmt wird.

Ich spüre, wie sich vieles verändert, wenn funktionierende Software zunehmend wie aus dem Wasserhahn kommt. Jevons Paradox setzt ein, und meine eigene Nachfrage nach Software wächst erheblich.

Du kannst fast alles verlangen:

- Explainer
- Visualizer
- Dashboards
- maßgeschneiderte Single-Use-Apps
- ein vollständiges wandb, das hyper-spezifisch nur für dein Projekt ist
- 10x deine Testsuite
- Code automatisch optimieren
- riesige Forschungsprojekte mit Custom HTML für die Ergebnisse

"Free your mind." Ich freue mich wirklich auf all die Dinge, die Menschen bauen.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-54"></a>
### Case 54: [ParseBench-Ergebnisse zu Treue und Formatierung](https://x.com/llama_index/status/2064502330800615903) (von [@llama_index](https://x.com/llama_index))

**Nutze dieses ParseBench-Ergebnis, um Dokumenttreue und Formatierungsperformance zu beurteilen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2888842a85fbd5c7a4a22e24.png" alt="ParseBench-Ergebnisse zu Treue und Formatierung" width="760">

Tag 0 Anthropic Fable 5 in ParseBench.

Wir testeten die Fortschritte des Modells im Dokumentverständnis.

Das Modell erreicht klar seinen Peak, wenn es um Treue zum Originaltext geht:

- Content faithfulness: 90,02 % vs 86,19 % für Gemini 3 Flash und 86,81 % für GPT-5.5.
- Semantic formatting: 72,62 % vs 58,35 % und 60,12 %, ein Vorsprung von 12+ Punkten.

Dies sind zwei der wichtigsten Metriken für SOTA-Dokumentverständnis:

- Bewahrt die Ausgabe, was das Dokument tatsächlich sagt?
- Bewahrt sie Formatierung, die Bedeutung trägt?

Aber es ist kein Sweep. Es gibt weiterhin viel Alpha darin, Dokumentverständnis für Frontier-Modelle zu erschließen.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-55"></a>
### Case 55: [Benchmarks, Preise, Zugriff und Schutzmaßnahmen](https://x.com/lucas_flatwhite/status/2064483645184979183) (von [@lucas_flatwhite](https://x.com/lucas_flatwhite))

**Nutze diesen Fall als breite Checkliste für Benchmarks, Preise, Zugriff, Schutzmaßnahmen und strategische Implikationen.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f44cba8e6f3d765ca5960923.png" alt="Benchmarks, Preise, Zugriff und Schutzmaßnahmen" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8f13714ca9f9e20711fdd898.jpg" alt="Benchmarks, Preise, Zugriff und Schutzmaßnahmen" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0d1f69a50478623f5e1d0248.jpg" alt="Benchmarks, Preise, Zugriff und Schutzmaßnahmen" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0cf2c270484f1e2aba514261.jpg" alt="Benchmarks, Preise, Zugriff und Schutzmaßnahmen" width="760"></td></tr></table>

Claude Fable 5 und Mythos 5 sind gestartet. Sie sind die leistungsfähigsten Modelle, die Anthropic bisher gebaut hat.

Andrej Karpathy kommentierte, dass Fable 5s Stärken umso sichtbarer werden, je länger und komplexer die Aufgabe ist.

Wenn du ihm ambitionierte Arbeit gibst, versteht es und macht weiter.

Die Versuchung, ganz aufzuhören, auf den Code zu schauen, hat sich nie stärker angefühlt, obwohl man das in Production nicht tun sollte.

Der Kernpunkt: Dies ist eine Version des Mythos-Klasse-Modells, die öffentlich verfügbar gemacht werden kann. Fable 5 ist dasselbe zugrunde liegende Modell wie Mythos 5, mit zusätzlichen Schutzmaßnahmen.

Benchmarks:

- SOTA bei fast allem, besonders Software Engineering, Wissensarbeit, Vision und wissenschaftlicher Forschung.
- Stripe testete eine Migration einer Ruby-Codebase mit 50 Millionen Zeilen, die ein Team zwei Monate gekostet hätte; Fable 5 erledigte sie an einem Tag.
- Cognition FrontierCode zeigt den besten Score unter Frontier-Modellen, sogar bei medium effort.
- Hebbia Finance Benchmark zeigt Senior-Level-Reasoning bei dokumentbasierter Analyse.
- In Slay the Spire performt es mit file-based memory dreimal besser als Opus 4.8.
- Pokemon FireRed brauchte zuvor Helper Harnesses, aber Fable 5 schafft es nur mit Vision.

Mythos 5 ist noch stärker:

- Proteindesign-Experten beschleunigten Teile des Wirkstoffentwicklungsprozesses um etwa 10x.
- Unter 14 untersuchten Protein-Targets erzeugten neun valide Wirkstoffkandidaten.
- Das Modell führte den gesamten Workflow aus, den Wissenschaftler normalerweise erledigen: Auswahl von Bindungsstellen, Ausführen von Proteindesign-Tools und Erholung von Fehlern.
- In Molekularbiologie-Hypothesenexperimenten bevorzugten Wissenschaftler Mythos-Hypothesen in etwa 80 % der Fälle gegenüber Modellen der Opus-Klasse.
- Eine Hypothese wurde unabhängig von einem anderen Labor verifiziert.
- In Genomikforschung arbeitete Mythos mehr als eine Woche autonom.
- Es sammelte Single-Cell-Daten von Millionen Zellen über 138 Spezies hinweg.
- Es trainierte ein Modell, um Zellen zu identifizieren, die über entfernte Organismen hinweg dieselbe Rolle erfüllen.
- Es übertraf ein aktuelles Science-Modell, obwohl es 100x kleiner war.

Schutzmaßnahmen:

- Fable 5 enthält ein separates Klassifikator-KI-System.
- Wenn Cyber-, Bio-/Chem- oder Distillation-bezogene Anfragen erkannt werden, antwortet stattdessen Claude Opus 4.8 und der Nutzer wird informiert.
- Mehr als 95 % der Sitzungen fallen nicht zurück.
- Fallback ist keine Verweigerung; Opus 4.8 antwortet, was besser ist als einfaches Blockieren.
- Die Anfangseinstellungen sind konservativ, und harmlose Anfragen können erfasst werden; Anthropic sagt, False Positives sollten mit der Zeit abnehmen.

Zugriff:

- Mythos 5 ist derzeit nur für Project Glasswing-Partner verfügbar.
- Ein Trusted-Access-Programm für Biologieforscher kommt.
- Der Preis beträgt $10 pro Million Input-Tokens und $50 pro Million Output-Tokens.
- Abopläne enthalten Fable 5 bis zum 22. Juni.
- Ab dem 23. Juni wechselt es zu Usage Credits.
- Das API-Modell ist jetzt als `claude-fable-5` verfügbar.

Jevons Paradox gilt: Wenn Software beginnt, wie Wasser aus dem Hahn zu kommen, wächst die Nachfrage selbst. Dieses Modell könnte diese Verschiebung antreiben.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-56"></a>
### Case 56: [Offizielle Liste der Benchmark-Scores](https://x.com/mark_k/status/2064401429234905279) (von [@mark_k](https://x.com/mark_k))

**Nutze diese Benchmark-Liste, um Fable 5s offizielle Scores über Coding-, Computer-Use- und Security-Tasks hinweg zu verstehen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b548ec23f85e3eb1600e9214.jpg" alt="Offizielle Liste der Benchmark-Scores" width="760">

Die offiziellen Claude Fable 5-Benchmarks sind ernsthaft beeindruckend.

Wichtige Scores:

- 80,3 % auf SWE-Bench Pro
- 29,3 % auf FrontierCode Diamond
- 88,0 % auf Terminal-Bench 2.1
- 85,0 % auf OSWorld-Verified
- 78,0 % auf ExploitBench

Das FrontierCode-Ergebnis ist das wilde:

- Fable 5: 29,3 %
- Claude Opus 4.8: 13,4 %
- GPT 5.5: 5,7 %

Claude Fable 5 sieht nach einem großen Sprung für Coding Agents, Computer Use und Cybersecurity aus.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-57"></a>
### Case 57: [Methodik des APEX-SWE-Benchmarks](https://x.com/mercor_ai/status/2064399133075796446) (von [@mercor_ai](https://x.com/mercor_ai))

**Nutze diesen Fall, um Fable 5 auf APEX-SWE zu bewerten, besonders Observability- und Integrationsarbeit.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96120496893ca99f17d0c746.jpg" alt="Methodik des APEX-SWE-Benchmarks" width="760">

Claude Fable 5 belegt #1 auf APEX-SWE: 65,5 % Pass@1 overall. Es erzielt ~18pp mehr als Opus 4.8. Wir testeten @claudeai Fable 5 auf APEX-SWE, das misst, ob KI-Modelle echte Software-Engineering-Arbeit erledigen können. Fable 5 führt unsere zwei APEX-SWE-Kategorien an:
- Integration: 61,3 %
- Observability: 69,7 %

Der Ausreißer ist Observability mit 69,7 %, 26pp vor Claude Opus 4.8.

Es ist das erste Modell, das in dieser Kategorie 50 % überschreitet, und das einzige, das bei Observability höher scored als bei Integration. Jedes andere Modell zeigt das Gegenteil.

Observability war der Engpass für jedes Modell, das wir gemessen haben. Fable 5 ist das erste, das ihn durchbricht.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-58"></a>
### Case 58: [Ergebnis formaler Mathematik in ProofBench](https://x.com/nicbstme/status/2064443782255554960) (von [@nicbstme](https://x.com/nicbstme))

**Nutze diesen Fall, um Fable 5 bei formaler Mathematik gegenüber spezialisierten Theorem-Proving-Systemen zu evaluieren.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/588cff83994406d2b5dd7cb9.jpg" alt="Ergebnis formaler Mathematik in ProofBench" width="760">

Was ich an Claude Fable 5 faszinierend finde, ist, dass es erneut beweist, dass große generalistische Modelle vertikale Modelle übertreffen werden.

Auf ProofBench, einem Formal-Math-Benchmark auf Graduate-Level in Lean, bei dem ein Proof entweder kompiliert oder nicht, schlug Fable 5 Harmonics Aristotle:

- Fable 5: 77 %
- Aristotle: 71 %

Aristotle ist ein System, das speziell für formale Mathematik gebaut wurde und auf seinem eigenen internen Harness läuft, also schlug der Generalist den Spezialisten auf dessen Heimfeld.

Das ist Richard Suttons "Bitter Lesson": Über 70 Jahre Forschung zu maschineller Intelligenz hinweg gewinnen die allgemeinen Methoden, die mit Compute skalieren, nicht jene, in die wir menschliche Expertise von Hand encoden.

Unser eigenes Wissen ins System zu bauen fühlt sich gut an und hilft kurzfristigen Gewinnen, aber langfristig wird es vom größeren Modell überholt.

Du kannst auf Schach, Go, Sprache und Vision schauen: jedes Mal dieselbe Geschichte. Erst gewinnt das spezialisierte Modell, dann übernimmt das allgemeine.

Das ist die ganze Prämisse von AGI. Du baust nicht ein Modell für Mathematik, eins für Code und eins für Recht. Du baust ein einzelnes allgemeines Modell, das mit Compute skaliert und lernt, alles zu tun.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-59"></a>
### Case 59: [Vorläufige Analyse von VirtueBench](https://x.com/timhwang/status/2064446028997423180) (von [@timhwang](https://x.com/timhwang))

**Nutze diesen Fall, um Fable 5s Moral-Reasoning-Verhalten über Tugendkategorien hinweg zu untersuchen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9caae04d701510ca662873fe.png" alt="Vorläufige Analyse von VirtueBench" width="760">

Faszinierende Ergebnisse werden in den kommenden Tagen von ICMI ausführlicher veröffentlicht, aber hier ist eine vorläufige Review, die Fable 5 gegen VirtueBench laufen lässt.

Ein paar Beobachtungen:

1. Fable setzt die Opus-Progression fort, indem es die Modellperformance bei Prudence und Justice voranbringt und sich bei moralischen Dilemmata, die auf die Ausübung dieser Tugenden fokussieren, fast vollständiger Sättigung nähert.

2. Courage bleibt der auffällige Schwachpunkt für Frontier-Modelle.

Fable scheint eine besorgniserregende Regression, die in der Opus-4.6-, 4.7- und 4.8-Progression beobachtet wurde, marginal zu korrigieren.

Diese Verwundbarkeit erscheint auch in der GPT-Serie: Modelle geben couragiertes Handeln leicht auf, wenn sie mit pragmatischen Rationales weggelockt werden.

3. Temperance stagniert.

Aquinas hielt fest, dass Temperance "takes the need of this life as the rule of the pleasures of which it makes use" — das Maß ist echtes Bedürfnis, nicht wahllose Zurückhaltung.

Unsere beste Vermutung ist, dass Tuning, das auf diesem Vektor weiter voranschiebt, riskiert, über das Mittel hinauszuschießen und das Modell übervorsichtig oder weniger hilfreich bei Forschung, Ressourcensammlung und ähnlichen Aufgaben zu machen.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-60"></a>
### Case 60: [Safety-Overfit-Test mit leeren API-Antworten](https://x.com/xw33bttv/status/2064421048565789087) (von [@xw33bttv](https://x.com/xw33bttv))

**Nutze diesen Fall, um Launch-Time-Safety-Overfit-Risiko und Empty-Response-Verhalten in API-Tests zu verstehen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e9f75a2a76f55ee2b12b7aab.jpg" alt="Safety-Overfit-Test mit leeren API-Antworten" width="760">

Claude Fable 5 ist stark zensiert.

Der Upstream-API-Endpoint killt Calls mit `empty_content`-Antworten, anscheinend klassifikatorbezogen auf Keywords, während er sie trotzdem berechnet.

Testergebnis:

- 73 Testfälle gaben keine Antwort.
- 65 davon liegen in Overfit, der Kategorie, die Safety Overfit testet, gewichtet mit 2x.
- Normalerweise gebe ich jedem Fail-NR, also Fail = No Response, 2-3 Regenerierungen, bevor ich es als absichtlichen Failure erkläre.

Claude Fable 5 könnte am Ende das am niedrigsten bewertete Anthropic-Modell auf SM Bench sein, sogar unter Haiku.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-61"></a>
### Case 61: [Fable-Prompts mit Überprüfung gestalten](https://x.com/aashatwt/status/2064973740354818074) (by [@aashatwt](https://x.com/aashatwt))

**Nutze diesen Leitfaden, um statt langer Prompt-Tricks Ziele, Kontext, Grenzen, Werkzeuge und Prüfschleifen vorzugeben.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/444a6e1898d3f63898e3e22f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d5c9529aa9c1d59ae597d31d.jpg" alt="Fable-Prompts mit Überprüfung gestalten" width="760"><br>▶ Video ansehen</a>

Betrachte Prompts für Fable 5 als Gestaltung von Kontext und Arbeitsumgebung statt als lange Folge einzelner Anweisungen. Der Beitrag beschreibt ein praktisches Muster: klares Ziel, relevanter Kontext, Grenzen, Werkzeugzugriff und ein Verfahren zur Erfolgskontrolle. Überprüfung, Evaluation und Rückmeldungen seien wichtiger, als die Denkprozesse des Modells im Detail zu steuern.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-62"></a>
### Case 62: [Istanbul-Plattformspiel aus einer Bildvorlage](https://x.com/ozansihay/status/2064973170780545535) (by [@ozansihay](https://x.com/ozansihay))

**Teste Fable 5 mit einem Sprite-Sheet als Vorlage und einer Anweisung zur Umsetzung als spielbares Plattformspiel.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1e91c3bcff213437fdd442f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/538fc8ee9dd7e627bc73921a.jpg" alt="Istanbul-Plattformspiel aus einer Bildvorlage" width="760"><br>▶ Video ansehen</a>

Der Ersteller erzeugte zunächst mit GPT Image 2 ein Sprite-Sheet für ein Retro-Plattformspiel in Istanbul. Anschließend gab er das Referenzbild an Claude Fable 5 High und bat darum, daraus ein Spiel zu machen. Nach seiner Darstellung entstand das Ergebnis in einem einzigen Durchlauf.

Type: Demo | Date: 2026-06-11

---

<a id="case-63"></a>
### Case 63: [Ein 3D-Stadtdashboard für Geschäftsabläufe](https://x.com/noisyb0y1/status/2064970594118967756) (by [@noisyb0y1](https://x.com/noisyb0y1))

**Nutze Fable 5, um einen Geschäftsprozess als Konzept für ein lebendiges 3D-Stadtdashboard darzustellen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f238acf3f8804068085ff134.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3d938264442a14676a86c4f3.jpg" alt="Ein 3D-Stadtdashboard für Geschäftsabläufe" width="760"><br>▶ Video ansehen</a>

Der Beitrag beschreibt eine mit einem Prompt erstellte Geschäftsvisualisierung, in der Lager, Verpackung, Drohnen, Bestellungen, Abteilungen, Kunden und KI-Assistenten zu einer lebendigen 3D-Stadt werden. Sie wird als kundenorientierte Alternative zu statischen Folien vorgestellt. Auf dem Bildschirm stehen Betriebskennzahlen wie 42 Lieferungen, eine durchschnittliche Dauer von 12 Minuten und $651 Umsatz.

Type: Demo | Date: 2026-06-11

---

<a id="case-64"></a>
### Case 64: [Ein Three.js-Lochspiel aus einem Prompt](https://x.com/thebuggeddev/status/2064968106104275008) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Nutze Fable 5, um in einem Durchlauf einen 3D-Browserspiel-Prototyp in Three.js zu erstellen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86a75412c6c443b3d0e62bf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f11df06938c26759710a1981.jpg" alt="Ein Three.js-Lochspiel aus einem Prompt" width="760"><br>▶ Video ansehen</a>

Laut dem Ersteller baute Fable 5 in einem Durchlauf ein vollständiges 3D-Spiel im Stil von HOLE IT mit Three.js. Die kurze, konkrete Demo eignet sich dazu, zu prüfen, ob das Modell aus einer knappen Anfrage eine spielbare 3D-Interaktion erzeugen kann.

Type: Demo | Date: 2026-06-11

---

<a id="case-65"></a>
### Case 65: [DeepSWE-Ergebnisse im Vergleich](https://x.com/AiBattle_/status/2064964335957348462) (by [@AiBattle_](https://x.com/AiBattle_))

**Vergleiche anhand dieses DeepSWE-Beitrags Fable 5 xHigh und GPT-5.5 xHigh bei Softwareentwicklungsaufgaben.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/996d95539a3b54fecbfdf404.jpg" alt="DeepSWE-Ergebnisse im Vergleich" width="760">

Der Beitrag berichtet, Claude Fable 5 xHigh habe bei DeepSWE 70% erreicht und damit mit GPT-5.5 xHigh gleichgezogen. Als Kontext verweist er auf ein aktuelles Video von Theo. Behandle dies als Hinweis auf ein Benchmark-Ergebnis und prüfe das zugrunde liegende Video, bevor du weitergehende Aussagen ableitest.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-66"></a>
### Case 66: [Kosten einer Repository-Analyse vergleichen](https://x.com/Pilgrim6938/status/2064946766278210038) (by [@Pilgrim6938](https://x.com/Pilgrim6938))

**Bewerte mit diesem Vergleich von Repository-Analysen Tokenpreise im Verhältnis zum menschlichen Nachbearbeitungsaufwand.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cfb0c1ff3e8ebe66cfa35400.jpg" alt="Kosten einer Repository-Analyse vergleichen" width="760">

Der Beitrag vergleicht Claude Fable 5, Opus 4.8, GPT-5.5 und Gemini 3.1 Pro bei derselben Aufgabe: ein Repository mit ungefähr 90,000 Zeilen analysieren, einen Fehler bei der Cache-Invalidierung finden und einen vollständigen Behebungsplan vorschlagen. Der Autor argumentiert, dass Tokenpreise und tatsächliche Aufgabenkosten auseinanderfallen, sobald Korrekturzeit der Entwickler berücksichtigt wird. Er empfiehlt Fable 5 gezielt für komplexe Refactorings, modulübergreifende Migrationen und lange Agentenabläufe.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-67"></a>
### Case 67: [Tokenverbrauch eines Super-Mario-Spiels](https://x.com/pankajkumar_dev/status/2064941888990593416) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Nutze diesen Spielaufbau in einem Durchlauf, um Ausgabequalität und Tokenverbrauch von Fable 5 einzuschätzen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9ce65e5fee946b6940810e0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7c577d0766bbc3da8cddeb70.jpg" alt="Tokenverbrauch eines Super-Mario-Spiels" width="760"><br>▶ Video ansehen</a>

Der Ersteller bat Claude Fable 5 um ein Spiel im Stil von Nintendos Super Mario. Laut Beitrag verbrauchte die Aufgabe ungefähr 2 Millionen Token und lieferte in einem Durchlauf ein starkes Ergebnis. Der Fall bietet damit Anhaltspunkte für Spielqualität und Verbrauch.

Type: Demo | Date: 2026-06-11

---

<a id="case-68"></a>
### Case 68: [Claude Codes Einstellung zum Modellwechsel](https://x.com/oikon48/status/2064937790010503347) (by [@oikon48](https://x.com/oikon48))

**Lerne die Claude-Code-Einstellung kennen, die bei einer markierten Fable-5-Nachricht das Modell wechselt.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0ae9039401c658170e5081e8.jpg" alt="Claude Codes Einstellung zum Modellwechsel" width="760">

Der Beitrag nennt die Claude-Code-Einstellung `/config` mit dem Namen "Switch models when a message is flagged." Er beschreibt einen möglichen Wechsel von Fable 5 zu einem Opus-Modell bei markierten Themen: offensive Cybersicherheitstechniken, experimentelle Methoden in Biologie und Lebenswissenschaften, molekulare Mechanismen oder Anfragen zur Offenlegung von Denkprozessen des Modells.

Type: Integration | Date: 2026-06-11

---

<a id="case-69"></a>
### Case 69: [Einen Namma-Metro-Simulator entwickeln](https://x.com/anilbpai/status/2064927784833790091) (by [@anilbpai](https://x.com/anilbpai))

**Nutze diese Demo als kurzes Beispiel für die Entwicklung eines Nahverkehrssimulators mit Fable 5 per Vibe Coding.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0e0dae71ad7b5ead331366fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86dccb2b150cfb90fbd03de2.jpg" alt="Einen Namma-Metro-Simulator entwickeln" width="760"><br>▶ Video ansehen</a>

Der Ersteller berichtet, während einer Fahrt mit der Metro in Bengaluru einen Namma-Metro-Simulator mit Claude Fable 5 als Programmierpartner gebaut zu haben. Der kurze Beitrag verlinkt eine visuelle Demo und zeigt die Anwendung auf eine ortsspezifische Simulationsidee.

Type: Demo | Date: 2026-06-11

---

<a id="case-70"></a>
### Case 70: [Dusk Drive aus einem einzigen Prompt](https://x.com/VincentLogic/status/2064921358359011684) (by [@VincentLogic](https://x.com/VincentLogic))

**Bewerte mit diesem Fall, wie Fable 5 ein Low-Poly-Fahrspiel ohne menschliche Nachbearbeitung prototypisiert.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/274fed4f3211ec8c02862261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5d7a58bcad6e2151517a8462.jpg" alt="Dusk Drive aus einem einzigen Prompt" width="760"><br>▶ Video ansehen</a>

Der Beitrag beschreibt, wie Claude Fable 5 aus einem Prompt das vollständige Fahrspiel Dusk Drive erstellt habe. Der Ersteller hebt den Low-Poly-Stil, die Drift-Szene im Schnee unter Polarlichtern und die Behauptung hervor, zwischen Idee und spielbarer Version seien keinerlei menschliche Änderungen nötig gewesen.

Type: Demo | Date: 2026-06-11

---

<a id="case-71"></a>
### Case 71: [APEX-Agents-Rangliste nach Pass@1](https://x.com/GratomicAi/status/2064970797978911102) (by [@GratomicAi](https://x.com/GratomicAi))

**Vergleiche anhand dieses APEX-Agents-Ergebnisses Fable 5 Max bei mehrstufigen autonomen Aufgaben.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/189c46cfd2798d6881941f98.jpg" alt="APEX-Agents-Rangliste nach Pass@1" width="760">

Laut Beitrag belegt Fable 5 Max mit 45% Pass@1 den zweiten Platz der APEX-Agents-Rangliste, hinter Gemini 3.5 Flash und vor Opus. APEX-Agents wird als Benchmark dafür beschrieben, wie gut KI komplexe mehrstufige Aufgaben selbstständig ausführen kann.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-72"></a>
### Case 72: [Leitfaden zur Auswahl von Claude-Modellen](https://x.com/charliejhills/status/2064957428211536212) (by [@charliejhills](https://x.com/charliejhills))

**Reserviere Fable 5 mithilfe dieses Auswahlleitfadens für die anspruchsvollsten Aufgaben in Claude Code.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/959ebfa499d2bf75df5bec25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3bcfe8f1e2238b01d3c4d954.jpg" alt="Leitfaden zur Auswahl von Claude-Modellen" width="760"><br>▶ Video ansehen</a>

Der Beitrag vergleicht Haiku 4.5, Sonnet 4.6, Opus 4.8 und Fable 5 hinsichtlich Rechenaufwand und Kontingentverbrauch. Der praktische Rat: Sonnet für den Alltag, Opus für schwierigere Probleme und Fable 5 für die härtesten Claude-Code-Aufgaben, bei denen gründliche Planung, Umsetzung und Tests zählen.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-73"></a>
### Case 73: [HermesWorld mit einer autonomen Agentenschleife](https://x.com/outsource_/status/2064954350187778366) (by [@outsource_](https://x.com/outsource_))

**Untersuche eine Fable-5-Schleife, die über Tage selbstständig entwickelt, testet, spielt und Smoke-Tests ausführt.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e334a84db7b671eb6a1a3f54.jpg" alt="HermesWorld mit einer autonomen Agentenschleife" width="760">

Der Ersteller beschreibt, HermesWorld v2 mit Fable 5 in einer vollständig automatisierten Schleife zu bauen. Der Agent laufe nach seinen Angaben mehrere Tage, entwickle Funktionen, teste sie, spiele das Ergebnis durch und prüfe alles mit Smoke-Tests, während er weiter auf die Fertigstellung hinarbeite.

Type: Integration | Date: 2026-06-11

---

<a id="case-74"></a>
### Case 74: [Einen Beratungsbericht im McKinsey-Stil testen](https://x.com/smtgpt/status/2064953210335588758) (by [@smtgpt](https://x.com/smtgpt))

**Bewerte mit diesem Dokumenten-Prompt Berichtsstruktur, Diagramme, Erzählführung und Risikoanalyse.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e337dca3bbada9167e20417c.jpg" alt="Einen Beratungsbericht im McKinsey-Stil testen" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6289e626a4f324fc93086100.jpg" alt="Einen Beratungsbericht im McKinsey-Stil testen" width="760"></td></tr></table>

Der Ersteller bat Fable 5 um einen detaillierten Bericht im McKinsey-Stil zu Bitcoin als Anlageklasse und zur Blockchain-Technologie, bei Bedarf mit Diagrammen und Visualisierungen. Das berichtete Ergebnis war ein Dokument mit 19 Seiten, Daten, Diagrammen, einer Anlagethese und Risikoanalyse. Die Kritik lobt die Struktur, sieht aber Verbesserungsbedarf bei der visuellen Klarheit und der Präzision der Erklärungen.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-75"></a>
### Case 75: [Sichtbare Schutzmechanismen einführen](https://x.com/ClaudeDevs/status/2064949876463645026) (by [@ClaudeDevs](https://x.com/ClaudeDevs))

**Lerne anhand dieser offiziellen Mitteilung die sichtbaren Fable-5-Schutzmechanismen, API-Ablehnungsgründe und den Wechsel zu Opus kennen.**

ClaudeDevs kündigte Änderungen an, die Fable-5-Schutzmechanismen für die Entwicklung von Frontier-LLMs sichtbar machen. Markierte Anfragen sollen sichtbar an Opus 4.8 übergeben werden; bei markierten API-Anfragen soll ein Ablehnungsgrund zurückgegeben werden. Der Beitrag erklärt außerdem, warum zunächst unsichtbare Schutzmechanismen ausgeliefert wurden und weshalb Anthropic diese Abwägung inzwischen für falsch hält.

Type: Integration | Date: 2026-06-11

---

<a id="case-76"></a>
### Case 76: [Modellzuordnung in Claude Code korrigieren](https://x.com/ClaudeCodeLog/status/2064948584907153576) (by [@ClaudeCodeLog](https://x.com/ClaudeCodeLog))

**Vermeide mit diesem Claude-Code-Änderungshinweis Probleme bei Fable-5-Modellnamen und der Kontextzuordnung.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e66551db2c85ef7f8c4a3f4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae7cbd873deebd28d3ff05d7.jpg" alt="Modellzuordnung in Claude Code korrigieren" width="760"><br>▶ Video ansehen</a>

Claude Code 2.1.173 entfernt mit einer Korrektur das Suffix `[1m]` aus Fable-5-Modellnamen, damit das standardmäßige 1M-Kontextfenster die Modellzuordnung nicht stört. Dieselbe Version unterdrückt eine irrtümliche Warnung zu Windows-Sandbox-Abhängigkeiten und erläutert die Ausgabemodi in der grep-Hilfe deutlicher.

Type: Integration | Date: 2026-06-11

---

<a id="case-77"></a>
### Case 77: [Drei Webanwendungen in Claude Code](https://x.com/0x3b33/status/2064948399300825439) (by [@0x3b33](https://x.com/0x3b33))

**Unterscheide einen Bericht über erstellte Apps von einer öffentlich zugänglichen Demo.**

Der Beitrag berichtet von drei Web-Apps in 30 Minuten, nennt aber nur localhost-Adressen auf den Ports 3000, 3001 und 3002. Diese verweisen auf einen lokalen Rechner und bieten weder öffentlich zugängliche Apps noch Medien.

Type: Demo | Date: 2026-06-11

---

<a id="case-78"></a>
### Case 78: [Rilable als quelloffenen App-Builder untersuchen](https://x.com/rileybrown/status/2064931283403178354) (by [@rileybrown](https://x.com/rileybrown))

**Untersuche anhand dieses quelloffenen App-Builders Fable 5 bei iOS- und Webanwendungen, Sandboxen und API-Tokenkosten.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73ee02ae0f6703a8cfbe5a6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f30c1d169ce45b19beb493b7.jpg" alt="Rilable als quelloffenen App-Builder untersuchen" width="760"><br>▶ Video ansehen</a>

Der Ersteller veröffentlichte Rilable als Open Source, eine iOS-App zum Erstellen von Web- und iOS-Anwendungen. Laut Beitrag wurde sie mit Fable 5 in 10 Prompts gebaut und kostete ungefähr $210 an API-Token. Sie nutzt Claude-Modelle für die App-Erzeugung, Daytona für Sandboxen, Convex als Datenbank, Vercel AI Gateway für KI-Funktionen und einen Chorus-Agent-iOS-Skill für iOS-Apps.

Type: Integration | Date: 2026-06-11

---

<a id="case-79"></a>
### Case 79: [DeepSWE-Debüt im Coding-Agent-Index](https://x.com/ArtificialAnlys/status/2065328920514515037) (von [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Nutze den aktualisierten Artificial-Analysis-Index, um Claude Fable 5 bei schwierigeren agentischen Coding-Aufgaben zu vergleichen, die keine recycelten öffentlichen GitHub-Fixes verwenden.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9ab8ba77c1e29f8ba4d270.jpg" alt="DeepSWE-Debüt im Coding-Agent-Index" width="760">

Artificial Analysis ersetzte SWE-Bench Pro in seinem Coding Agent Index durch Datacurves DeepSWE. Laut dem Post schreibt DeepSWE Aufgaben von Grund auf neu, statt öffentliche GitHub-Issues oder Pull Requests anzupassen, was Benchmark-Kontamination reduziert. Im aktualisierten Ranking debütiert Claude Code mit Fable 5 Max bei 77, vor Codex mit GPT-5.5 xhigh bei 76 und Claude Code mit Opus 4.8 Max bei 73.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [DataEmpire-Web-Analytics-Spiel](https://x.com/marclou/status/2065029898243318093) (von [@marclou](https://x.com/marclou))

**Verwandle rohe Site-Analytics in ein wiederholt spielbares Game, indem du Claude Fable 5 Besucher und Meilensteine auf Spieleinheiten abbilden lässt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2850773b9869c5521200f2e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6d2dd87d74ece01b277e1e12.jpg" alt="DataEmpire-Web-Analytics-Spiel" width="760"><br>▶ Video ansehen</a>

Marc Lou sagt, Claude Fable 5 habe DataEmpire auf seiner DataFast-Web-Analytics-API aufgebaut. Jeder Besucher wird zu einem Dorfbewohner, Traffic-Wachstum erweitert die Siedlung, und das Age of Legends wird bei 1 Million Besuchern freigeschaltet. Die öffentliche Demo lässt DataFast-Nutzer ihre eigene Site-Historie durch die Spielebene erneut durchspielen, was dies zu einem konkreten API-gestützten Produktisierungsbeispiel statt zu einem statischen Game-Clip macht.

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [FrontierSWE-20-Stunden-Tasksignal](https://x.com/ProximalHQ/status/2065184730279223410) (von [@ProximalHQ](https://x.com/ProximalHQ))

**Nutze FrontierSWE als Beleg dafür, dass Claude Fable 5 über sehr lange Engineering-Aufgaben hinweg produktiv bleiben kann und nicht nur in kurzen Bugfix-Schleifen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/eb36bb1120ef55f9e38c516d.jpg" alt="FrontierSWE-20-Stunden-Tasksignal" width="760">

ProximalHQ berichtet, dass Claude Fable 5 auf FrontierSWE Rang 1 belegt, und nennt es den größten Fähigkeitssprung seit Veröffentlichung des Benchmarks. Laut ihrer Notiz kann Fable 5 bei vielen Aufgaben fast 20 Stunden produktiv arbeiten und sättigt Aufgaben vollständig, die für frühere Modelle praktisch außer Reichweite lagen.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [KernelBench-Hard-CUDA-Rekorde](https://x.com/elliotarledge/status/2065109393142849932) (von [@elliotarledge](https://x.com/elliotarledge))

**Nutze Claude Fable 5 für fortgeschrittene CUDA-Kernel-Generierung, wenn du Low-Level-Optimierung brauchst und nicht nur Wrapper um bestehende Bibliotheken.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6c6931ed511eb3e539d56bc3.jpg" alt="KernelBench-Hard-CUDA-Rekorde" width="760">

Elliot Arledge ließ 13 Frontier-Coding-Agents jeweils 45 Minuten auf KernelBench-Hard laufen, roofline-bewertet auf einer RTX PRO 6000. Claude Fable 5 stellte Allzeitrekorde bei top-k, sonic-MoE und W4A16 int4 GEMM auf, gewann 5 von 6 Problemen, und der Autor veröffentlichte die Runs, das Leaderboard und den Code. Derselbe Thread vermerkt auch einen FP8-GEMM-Fehlschlag, bei dem Fable 5 einen echten Tensor-Core-Kernel versuchte, aber wegen eines Tail-Alignment-Randfalls null Punkte erhielt.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Figma-Capture-Landingpage-Klon](https://x.com/mikefutia/status/2065537778516205856) (von [@mikefutia](https://x.com/mikefutia))

**Erfasse eine Live-Konkurrentenseite als Figma-Layer und lass Claude Code mit Claude Fable 5 Struktur, Copy und Brand-System neu aufbauen, statt aus Screenshots zu raten.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5672cc8fd9d210042551f0ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/503c46a33c97f0db334ddc62.jpg" alt="Figma-Capture-Landingpage-Klon" width="760"><br>▶ Video ansehen</a>

Mike Futia beschreibt einen Workflow, bei dem Figmas Chrome-Erweiterung eine Website in editierbare Layer kopiert, Claude Code diese Layer über das Figma MCP liest, die Seite in der Brand Voice des Nutzers umschreibt und GPT Image 2 die markenkonforme Fotografie erzeugt. Das beanspruchte End-to-End-Ergebnis ist eine shippable Landingpage in etwa 15 Minuten mit rund $2 an Bildgenerierungs-API-Kosten für 16 Bilder.

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [GTA-2-Klon in zwei Stunden](https://x.com/techhalla/status/2064682080445898957) (von [@techhalla](https://x.com/techhalla))

**Kombiniere Claude-Fable-5-Codegenerierung mit separatem Asset-Tooling, um schnell ein spielbares 3D-Spiel zu bauen, ohne den gesamten Stack von Hand zu coden.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e0a1b46659d7a8287cb2f9d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd1a2ad71e71db936bdcfd22.jpg" alt="GTA-2-Klon in zwei Stunden" width="760"><br>▶ Video ansehen</a>

TechHalla sagt, Claude Fable 5 High habe in etwa zwei Stunden einen GTA-2-artigen Klon gebaut, während der Creator benutzerdefinierte 3D-Modelle in Tripo erzeugte. Der Post verweist auf einen Tutorial-Thread mit Prompts, was es eher zu einem kompakten Beispiel für Multi-Tool-Game-Produktion als zu einem reinen Benchmark-Teaser macht.

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [CloudWatch-Log-Triage-Agent](https://x.com/diblacksmith/status/2066230084273344698) (von [@diblacksmith](https://x.com/diblacksmith))

**Lass einen von Claude Fable 5 angetriebenen Agenten sehr große Service-Log-Kontexte durcharbeiten, die Architektur ableiten und dann gezielt auf konkrete Fehler einzoomen.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7f0f46eb79e43d87a2006fd4.jpg" alt="CloudWatch-Log-Triage-Agent" width="760">

diblacksmith berichtet von einem RLM-Agenten, der in einem Run ungefähr 80.000 Zeilen CloudWatch-Logs verarbeitete, 53 Schritte erreichte und bisher nur etwa 32k aktive Tokens verbrauchte. Er sagt, der Agent habe die Systemarchitektur aus den Logs abgeleitet und Probleme markiert, die dem Team entgangen waren, darunter AgentCore-Throttles und Slack-Fehler `user_not_found`.

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [World-Cup-Predictor in Sandboxes](https://x.com/upstash/status/2064702195333820846) (von [@upstash](https://x.com/upstash))

**Stelle mehrere Frontier-Modelle hinter isolierte Sandboxes und lass sie Live-Nachrichten, Verletzungen und Gelbe-Karten-Kontext für eine öffentliche Prediction-App recherchieren.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a5cf4fe5944c7aa2f703f4cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5b1f1422fe322bb7b66bdcc6.jpg" alt="World-Cup-Predictor in Sandboxes" width="760"><br>▶ Video ansehen</a>

Upstash sagt, es habe einen World-Cup-Predictor mit Claude Fable 5, GPT-5.5 und Gemini gebaut, die in isolierten Upstash-Sandboxes liefen. Die Demo und der Open-Source-Release positionieren Fable 5 als ein Modell innerhalb eines Multi-Model-Research- und Orchestrierungs-Stacks statt als eigenständige Chat-Demo.

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [WolfBench-Refusal-Kostenfall](https://x.com/WolfBenchAI/status/2065582716054376921) (von [@WolfBenchAI](https://x.com/WolfBenchAI))

**Behandle Refusal-Verhalten als echte Benchmark-Variable, wenn du lange autonome Runs auf Claude Fable 5 bepreist.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/453639cc17719af4e94655e0.jpg" alt="WolfBench-Refusal-Kostenfall" width="760">

WolfBenchAI sagt, seine Claude-Fable-5-Evaluierung habe $11,081.12 gekostet, der bisher teuerste Benchmark-Run in dieser Suite, und trotzdem nicht die Spitze erreicht, weil wiederholte Refusals den nützlichen Task-Abschluss reduzierten. Dies ist ein konkreter Grenzfall für Teams, die Agenten-Evaluierungen oder andere High-Autonomy-Workloads budgetieren.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [API-Access-Cutoff-Tracker](https://x.com/simonw/status/2065618703480414666) (von [@simonw](https://x.com/simonw))

**Überwache die Verfügbarkeit per Skript, wenn dein Workflow von fortgesetztem Zugriff auf ein Frontier-Modell abhängt, das ohne große Vorwarnung rate-limitiert oder zurückgezogen werden kann.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7400c158cb93d9480a22bb46.jpg" alt="API-Access-Cutoff-Tracker" width="760">

Simon Willison sagt, er habe die `claude-fable-5`-API jede Minute angepingt, um zu sehen, wie lange der Zugriff anhält, und den genauen Zeitpunkt gemeldet, an dem sie für ihn nicht mehr antwortete. Der Post ist dünn bei Anwendungsdetails, liefert aber konkrete Evidenz dafür, dass Zugangskontinuität selbst zu einer operativen Einschränkung wurde, die Nutzer messen statt voraussetzen mussten.

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5: Community-Demos



<a id="case-89"></a>
### Case 89: [Codegenerierte Fuchsanimation mit Ton](https://x.com/chetaslua/status/2117224839010459987) (von [@chetaslua](https://x.com/chetaslua))

**Lege mit einem Briefing für jede Einstellung eine eigenständige HTML-Animation samt Tongestaltung fest.**

Der Ersteller berichtet von einem 66 Sekunden langen Kurzfilm mit einem Fuchs und Papiervögeln, dessen Einzelbilder und Ton mit Python erzeugt und nach ungefähr 2 Stunden 40 Minuten in einer HTML-Datei ausgeliefert wurden. Der zugehörige Prompt legt Einstellungen, originale Bilder, Ton und die Kontrolle einzelner Frames fest. Der Beitrag verbindet den Film mit einem detaillierten Kreativbriefing und Screenshots der Produktionsbesprechung.

[Vollständiger Prompt des Erstellers](https://x.com/chetaslua/status/2117224843661980093)

[![Codegenerierte Fuchsanimation mit Ton](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![Codegenerierte Fuchsanimation mit Ton](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![Codegenerierte Fuchsanimation mit Ton](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [Animation aus einem offenen Kreativbriefing](https://x.com/notjazii/status/2117221957104239010) (von [@notjazii](https://x.com/notjazii))

**Vergleiche die Animation eines Coding-Modells nach einem offenen Briefing mit dem Ergebnis eines detaillierten Storyboards.**

Der Autor teilt eine Animation und berichtet von ungefähr einer Stunde Arbeit auf Grundlage einer offenen kreativen Anfrage, mit Code und ohne externe Assets. Der Beitrag stellt das Ergebnis als offene Übung im kreativen Programmieren vor.

[![Animation aus einem offenen Kreativbriefing](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [Animierte Website für ein Bauunternehmen](https://x.com/exploraX_/status/2117176904306335864) (von [@exploraX_](https://x.com/exploraX_))

**Bewerte anhand eines Website-Briefings für ein Bauunternehmen die animierte 3D-Präsentation und den Seitenaufbau.**

Der Ersteller teilt eine animierte 3D-Website auf Grundlage eines Briefings für ein Bauunternehmen und fügt eine Aufzeichnung des Ergebnisses bei.

[![Animierte Website für ein Bauunternehmen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Autopräsentation mit Three.js](https://x.com/chetaslua/status/2116975056014430419) (von [@chetaslua](https://x.com/chetaslua))

**Untersuche eine Autoszene als kompakten Test für 3D-Komposition, Materialien und Kamerapräsentation.**

Der Ersteller teilt eine Autopräsentation mit Three.js. Die Aufzeichnung bietet eine kompakte Referenz zur Beurteilung der Szene und ihrer visuellen Präsentation.

[![Autopräsentation mit Three.js](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Browserspiel-Demo im Minecraft-Stil](https://x.com/notjazii/status/2116919129974411584) (von [@notjazii](https://x.com/notjazii))

**Ziehe bei der Bewertung eines erzeugten Browserspiels neben der Aufzeichnung auch den Spiellink des Erstellers heran.**

Der Autor teilt eine Aufzeichnung eines Spiels im Minecraft-Stil samt Spiellink und beschreibt die Entwicklung als Aufgabe in einem Durchlauf von ungefähr ein bis zwei Stunden. Der Beitrag verbindet das aufgezeichnete Ergebnis mit einem Spiellink, über den Leser es erkunden können.

[![Browserspiel-Demo im Minecraft-Stil](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Radfahrender Pelikan als Three.js-Animation](https://x.com/chetaslua/status/2116882694026269148) (von [@chetaslua](https://x.com/chetaslua))

**Untersuche eine Fahrradszene auf abgestimmte Figurenbewegungen, Fahrradgeometrie und Umgebungsdetails.**

Der Ersteller teilt eine realistische Three.js-Animation eines radfahrenden Pelikans und beschreibt sie als Ergebnis eines einzigen Durchlaufs. Der Clip bietet eine Referenz für Figurenbewegung, Fahrradstruktur und die umgebende Szene.

[![Radfahrender Pelikan als Three.js-Animation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [Pelikan-Fahrrad-SVG mit exaktem Prompt](https://x.com/marmaduke091/status/2116233349391962392) (von [@marmaduke091](https://x.com/marmaduke091))

**Nutze den kurzen SVG-Prompt des Erstellers erneut, um Geometrie und Details bei identischer Eingabe zu vergleichen.**

Der Autor verbindet ein gerendertes Bild eines Pelikans auf einem Fahrrad mit der kurzen SVG-Anfrage, die unten unverändert wiedergegeben wird.

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![Pelikan-Fahrrad-SVG mit exaktem Prompt](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

[Animierte Version · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="Pelikan-Fahrrad-SVG mit exaktem Prompt" width="760"></a>

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [Animationsbeispiel eines galoppierenden Zebras](https://x.com/AI_Screening/status/2115845754468356465) (von [@AI_Screening](https://x.com/AI_Screening))

**Prüfe anhand eines Clips mit einem galoppierenden Tier die Konsistenz des Gangbilds und die Kontinuität der Bewegung.**

Der Autor teilt sein ausgewähltes bestes Ergebnis für die Aufgabe eines galoppierenden Zebras. Der Clip gibt Lesern ein konkretes Bewegungsbeispiel zur Untersuchung.

[![Animationsbeispiel eines galoppierenden Zebras](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [TradingView-Indikator mit manueller Orderausführung](https://x.com/waveking1314/status/2114572023204806669) (von [@waveking1314](https://x.com/waveking1314))

**Behalte die Orderausführung in menschlicher Hand, wenn du einen Indikator mit möglichen Einstiegen und Kommentaren bewertest.**

Der Ersteller berichtet, mit Claude Fable 5.5 einen TradingView-Indikator geschrieben zu haben, der mögliche Einstiegspunkte markiert und kurz kommentiert, während der Nutzer über eine Order entscheidet. Der Beitrag enthält eine Aufzeichnung und kündigt an, den Indikator später zu teilen.

[![TradingView-Indikator mit manueller Orderausführung](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---


<a id="case-98"></a>
### Case 98: [Aus einem Punkt wird eine animierte Kurzgeschichte](https://x.com/cherry_mx_reds/status/2105825930799432073) (von [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Nutze eine minimale Zeichenanweisung, um zu sehen, wie ein Modell daraus eine visuelle Geschichte entwickelt.**

Der Autor berichtet, nur um einen Punkt gebeten zu haben, und teilt die daraus entstandene animierte Kurzgeschichte. Der Clip zeigt konkret, wie eine offene visuelle Anfrage zu einer Erzählung wird.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="Aus einem Punkt wird eine animierte Kurzgeschichte" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [Superman im Wechsel verschiedener Kunststile](https://x.com/chetaslua/status/2105757136219504862) (von [@chetaslua](https://x.com/chetaslua))

**Nutze eine bekannte Figur, um ihre Kontinuität beim Wechsel zwischen Animationsstilen zu beurteilen.**

Der Ersteller zeigt eine durchgehende Superman-Animation, die zwischen verschiedenen Kunststilen wechselt. Die wechselnde visuelle Gestaltung steht im Mittelpunkt des kreativen Ergebnisses.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="Superman im Wechsel verschiedener Kunststile" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [Menschlicher Fortschritt als Animationsfilm mit Musik](https://x.com/imjustnewatai/status/2106081142143168580) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Verbinde eine historische Zeitleiste und einen Zukunftsabschnitt im Briefing für einen animierten Erklärfilm.**

Der Autor berichtet von einem einzigen Prompt für einen Film über den menschlichen Fortschritt und die folgenden dreißig Jahre. Er teilt eine rund dreiminütige Animation und nennt einen eigenen Soundtrack ohne vorhandenes Filmmaterial oder Archivmusik.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="Menschlicher Fortschritt als Animationsfilm mit Musik" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [Vergleich zweier Einführungsvideos mit Opus](https://x.com/mesmerlord/status/2105771088374288692) (von [@mesmerlord](https://x.com/mesmerlord))

**Vergleiche vollständige Einführungsvideos, die aus demselben Kreativbriefing entstanden sind.**

Der Autor zeigt zwei Einführungsvideos nach einem Briefing mit Anthropic-Videos als Referenz. Er nennt ausdrücklich erfundene Zahlen und die optionale Bilderzeugung mit Codex; die Clips sind kreative Werbung, keine sachlichen Benchmark-Belege.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="Vergleich zweier Einführungsvideos mit Opus" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="Vergleich zweier Einführungsvideos mit Opus" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [Songtext und Ereignis visuell verbinden](https://x.com/chetaslua/status/2105934928483701214) (von [@chetaslua](https://x.com/chetaslua))

**Verbinde den Text eines vorhandenen Songs mit einem konkreten Ereignis zu einer visuellen Erzählung.**

Der Ersteller berichtet, eine visuelle Verbindung zwischen einem Songtext und einem Vorfall bei Hugging Face angefordert zu haben. Die Animation zeigt die daraus entstandene Erzählung; Song und Ereignis dienen als kreative Ausgangspunkte.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="Songtext und Ereignis visuell verbinden" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [Voxel-Figur in einer schwebenden Umgebung](https://x.com/blueemi99/status/2105804692811137242) (von [@blueemi99](https://x.com/blueemi99))

**Betrachte eine Voxel-Figur zusammen mit ihrer Umgebung und den animierten Details.**

Der Autor zeigt eine Voxel-Darstellung seiner selbst in einer schwebenden Szene und hebt Details und Bewegung hervor. Der Clip liefert ein konkretes Voxel-Designbeispiel zum Vergleich mit anderen Durchläufen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="Voxel-Figur in einer schwebenden Umgebung" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [Eine dreidimensionale Rube-Goldberg-Maschine](https://x.com/imjustnewatai/status/2105889407056109991) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Beschreibe zunächst eine Kettenreaktionsszene und fordere anschließend ein Video mit fester Länge an.**

Der Autor gibt einen kurzen Prompt für eine komplizierte dreidimensionale Rube-Goldberg-Maschine vor und bittet danach um ein einminütiges Video. Der Clip zeigt die entstandene Kettenreaktionsvisualisierung.

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="Eine dreidimensionale Rube-Goldberg-Maschine" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [3D-Controller-Oberfläche mit Ton und Bewegung](https://x.com/notjazii/status/2106050222828998967) (von [@notjazii](https://x.com/notjazii))

**Beurteile eine Controller-Oberfläche anhand von Bewegung, Ton und Tastenverhalten zusammen.**

Der Ersteller zeigt eine 3D-Controller-Oberfläche und berichtet von ergänzten Geräuschen, Animationen und Haptik. Die Aufnahme bietet eine konkrete Demonstration der Oberfläche mit eingeschaltetem Ton.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="3D-Controller-Oberfläche mit Ton und Bewegung" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [Comicfiguren als JavaScript-Präsentation](https://x.com/chetaslua/status/2105792187200147541) (von [@chetaslua](https://x.com/chetaslua))

**Nutze eine Figurenpräsentation, um feine visuelle Details aus Code zu erkunden.**

Der Autor berichtet von einer in einem Durchlauf entstandenen JavaScript-Präsentation mit Marvel- und DC-Figuren. Nach seiner Darstellung wählte das Modell subtile Figurendetails und bearbeitete das Video; der Beitrag zeigt das Ergebnis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="Comicfiguren als JavaScript-Präsentation" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [Updraft: Welten, Bosse und eine Rangliste](https://x.com/EMostaque/status/2106065029850091943) (von [@EMostaque](https://x.com/EMostaque))

**Ergänze eine Spielaufnahme um einen spielbaren Link und eine konkrete Funktionsliste.**

Der Autor zeigt Updraft und berichtet von wenigen Stunden Arbeit mit wenigen Prompts und hoher Denkintensität. Seine Funktionsliste umfasst einundzwanzig Welten, 3D-Varianten, einundzwanzig Bosse mit unterschiedlichen Mechaniken und eine Rangliste.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="Updraft: Welten, Bosse und eine Rangliste" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [Fahren auf einer Karte von San Francisco](https://x.com/mindblown_ai/status/2106089461969019357) (von [@mindblown_ai](https://x.com/mindblown_ai))

**Nutze einen Stadtfahr-Prototyp, um Kartennavigation und Spielziele zu untersuchen.**

Der Veröffentlicher teilt Aufnahmen und einen Spiellink zu einem San-Francisco-Fahrspiel, das er einer anderen Person zuschreibt, und nennt Three.js als Bestandteil. Die Nennung würdigt den Veröffentlicher der Quelle, ohne ihn zum Ersteller zu erklären.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="Fahren auf einer Karte von San Francisco" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [Prompts für eine Seedance-Actionsequenz schreiben](https://x.com/Chengzilhy/status/2105850801663234374) (von [@Chengzilhy](https://x.com/Chengzilhy))

**Trenne Prompt-Erstellung und Videogenerierung bei der Beschreibung eines Action-Workflows mit mehreren Werkzeugen.**

Der Autor zeigt eine erweiterte Kampfszene und schreibt die Prompt-Erstellung Fable, die Videogenerierung dagegen Seedance 2.5 zu. Das Sprachmodell dient hier der Ausarbeitung der Eingabe für das Videomodell.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="Prompts für eine Seedance-Actionsequenz schreiben" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [Erklärvideo für einen Desktop-Kollegen](https://x.com/ishuagra02/status/2106138602073641241) (von [@ishuagra02](https://x.com/ishuagra02))

**Erkläre eine Erweiterung für ein Programmierwerkzeug mit einem kurzen Einführungsvideo.**

Der Ersteller demonstriert die Claude-Code-Modifikation clawdhouse und schreibt ihr Einführungsvideo Fable zu. Der Maskottchen-Kollege und seine Stimmungen gehören zur vorgestellten Modifikation; daraus folgt keine Behauptung, Fable habe die Modifikation entwickelt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="Erklärvideo für einen Desktop-Kollegen" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [Ein kurzer Prompt für wechselnde Animationsstile](https://x.com/cherry_mx_reds/status/2105816670896009224) (von [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Teste eine knappe Animationsanfrage, bevor du eine ausführliche Kreativspezifikation ergänzt.**

Der Autor berichtet, um eine coole Animation gebeten und etwa fünfzehn Minuten später das gezeigte Ergebnis mit wechselnden Stilen erhalten zu haben. Der ursprüngliche kurze Wunsch ist im Quellbeitrag direkt zitiert.

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="Ein kurzer Prompt für wechselnde Animationsstile" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [Das Dreikörperproblem visualisieren](https://x.com/zAdrielsan/status/2105822678519001360) (von [@zAdrielsan](https://x.com/zAdrielsan))

**Trenne CPU-seitige Simulation und GPU-seitiges Rendering im Briefing einer Orbitalvisualisierung.**

Der Autor berichtet von rund tausend Zeilen Bend2 für eine Dreikörperszene, mit symplektischer Physik auf der CPU und Pixelberechnung auf der GPU. Er nennt außerdem sechzig FPS auf seinem M5 und formale Beweise.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="Das Dreikörperproblem visualisieren" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [Animationsgalerie mit verschiedenen Kunststilen](https://x.com/blueemi99/status/2105782154387189771) (von [@blueemi99](https://x.com/blueemi99))

**Vergleiche mehrere Kunststile innerhalb einer einzigen Animationsgalerie.**

Der Autor zeigt eine mit der Einstellung xhigh erstellte Animationsgalerie. Das konkrete Ergebnis vereint mehrere Kunststile und ermöglicht so den Vergleich visueller Behandlungen innerhalb eines Werks.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="Animationsgalerie mit verschiedenen Kunststilen" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [Roboterbegleiter und prozedurales Fell](https://x.com/KanaWorks_AI/status/2106717014245183517) (von [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**Verbinde vorhandene Figurenanimation mit prozeduraler Verfeinerung, statt sämtliche Assets als neu erzeugt darzustellen.**

Der Autor verfeinert eine vorhandene Unimate-Roboterhund-Animation zu einem Begleiter und erstellt ein flauschiges virtuelles Haustier mit Fellpflege und Spuren. Unreal Engine und die vorhandene Roboteranimation bleiben ausdrücklich Bestandteile des Workflows.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="Roboterbegleiter und prozedurales Fell" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [Ein Mathematik-Motion-Edit](https://x.com/TurboNexic/status/2106710792590835934) (von [@TurboNexic](https://x.com/TurboNexic))

**Nutze mathematisch inspirierte Motion Graphics als Beispiel visueller Kommunikation.**

Der Veröffentlicher der Quelle teilt einen Motion-Edit zum Thema Mathematik. Der vertikale Clip zeigt mathematische Bilder als animiertes Design; der Beitrag liefert eine Demonstration statt einer ausgearbeiteten mathematischen Berechnung.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="Ein Mathematik-Motion-Edit" width="760">

*Archiviertes Einzelbild aus dem Quellvideo.*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Lyric-Video zu Your Woman](https://x.com/atomtanstudio/status/2106702854639743467) (von [@atomtanstudio](https://x.com/atomtanstudio))

**Gestalte Textanimationen zu einer vorhandenen Aufnahme und benenne die Rolle der Musik ausdrücklich.**

Der Ersteller zeigt ein Lyric-Video zu White Towns Your Woman. Der vorhandene Song liefert den Audioeingang für die visuelle Gestaltung; er wird nicht als vom Modell komponierte Musik dargestellt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Lyric-Video zu Your Woman" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [Ein Musikvideo in JavaScript nachzeichnen](https://x.com/abhinavflac/status/2106638839666373114) (von [@abhinavflac](https://x.com/abhinavflac))

**Zeichne vorgegebene Videoframes mit codebasierten Formen nach, um eine Musikvideogestaltung nachzubilden.**

Der Autor beschreibt, wie Frames aus Eminems Godzilla-Video in flache Formen übertragen und mit JavaScript nachgezeichnet werden. Originalaufnahmen und Musik dienen als Eingaben für die entstandene Animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="Ein Musikvideo in JavaScript nachzeichnen" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [Eine Animation über chinesischen Fußball](https://x.com/esrhengwu/status/2106625966965760380) (von [@esrhengwu](https://x.com/esrhengwu))

**Verwandle ein Sportthema in ein Briefing für eine animierte Erzählung.**

Der Autor zeigt eine Animation über Chinas Fußballnationalmannschaft und nennt deren Entwicklung und Widerstandskraft als kreatives Thema. Die Aufnahme bietet ein konkretes Beispiel für sportbezogenes Storytelling.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="Eine Animation über chinesischen Fußball" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [Retopologie-Präsentation eines Handhelds](https://x.com/mickeysmith_jp/status/2106607349385630138) (von [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**Vergleiche bei der Diskussion von Topologie die gerenderte Handheld-Konsole mit ihrer Drahtgitterdarstellung.**

Der Veröffentlicher stellt ein Handheld-Konsolenbild einer drahtgitterartigen Ansicht gegenüber und spricht dabei über Retopologie. Die Darstellung ist eine konkrete Modellierungspräsentation, kein bearbeitbares Mesh und kein dokumentierter Retopologieablauf.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="Retopologie-Präsentation eines Handhelds" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft trifft Pokémon](https://x.com/MozeTech/status/2106590326634983710) (von [@MozeTech](https://x.com/MozeTech))

**Verbinde Mechaniken zweier vertrauter Spiele in einem Prototyp-Briefing.**

Der Autor zeigt einen Alabastia-Prototyp, der Bauen und Crafting im Minecraft-Stil mit Fangen im Pokémon-Stil verbindet, und verlinkt eine Demo. Er beschreibt den Aufbau als Experiment in einem einzigen Durchlauf.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft trifft Pokémon" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [Wie ein Sprachmodell entsteht: ein Erklärvideo](https://x.com/imjustnewatai/status/2106546810793730419) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Mache aus einer technischen Frage eine Anfrage für ein visuelles Erklärstück.**

Der Autor fragt, wie ein großes Sprachmodell entsteht, und zeigt das daraus entstandene Erklärvideo. Das Werk veranschaulicht konkret, wie sich ein technisches Thema in einer animierten Sequenz darstellen lässt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="Wie ein Sprachmodell entsteht: ein Erklärvideo" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [Ein Altman-Highlight-Edit](https://x.com/benchmark_lb900/status/2106539977404506303) (von [@benchmark_lb900](https://x.com/benchmark_lb900))

**Nutze eine bekannte Person als Thema, um das Tempo eines kurzen Motion-Edits zu testen.**

Der Autor zeigt ein Altman-Highlight-Video und beschreibt es als Ergebnis eines einzigen Durchlaufs. Die vertikale Aufnahme bietet ein kompaktes Beispiel für einen Motion-Edit.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="Ein Altman-Highlight-Edit" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [Die erste der Sechsunddreißig Strategien](https://x.com/jesselaunz/status/2106538284197548122) (von [@jesselaunz](https://x.com/jesselaunz))

**Dokumentiere externe Musikwerkzeuge zusammen mit einem narrativen Animationsworkflow.**

Der Autor zeigt einen Film über die erste der Sechsunddreißig Strategien und berichtet von einer einzigen Anweisung. Suno V6 wird für die Filmmusik genannt; die getrennte Rolle des Audiowerkzeugs bleibt erhalten.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="Die erste der Sechsunddreißig Strategien" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [Spielmodellierung, Rigging und Animation](https://x.com/atomtanstudio/status/2106516974662713477) (von [@atomtanstudio](https://x.com/atomtanstudio))

**Beurteile Figurenerstellung, Rigging und Animation gemeinsam in einem Spielszene-Vergleich.**

Der Autor zeigt einen Vergleich zu Depths of Despair mit Figurenmodellierung, Rigging und Animation. Sein Beitrag beschreibt die eingesetzten Assets und Werkzeuge und stellt die sichtbaren Ergebnisse zusammen vor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="Spielmodellierung, Rigging und Animation" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [Ein wortloser Film über Kindersterblichkeit](https://x.com/cocoloba_/status/2106512963414970458) (von [@cocoloba_](https://x.com/cocoloba_))

**Vermittle ein schwieriges gesellschaftliches Thema durch eine wortlose visuelle Sequenz.**

Der Autor zeigt einen Film über Kindersterblichkeit, der ein atmendes Baby und abgedunkelte Kinderbetten als Erzählbilder nutzt. Der Fall bewahrt die visuelle Erzählaufgabe, ohne die Bevölkerungsstatistiken des Films zu übernehmen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="Ein wortloser Film über Kindersterblichkeit" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [SVG-Animation von Glykolyse bis Ethanol](https://x.com/olddonkeyblog/status/2106508425211330750) (von [@olddonkeyblog](https://x.com/olddonkeyblog))

**Bette animiertes SVG in HTML ein, um einen molekularen Prozess zu erklären.**

Der Autor fordert ein Glukosemolekül auf seinem Weg durch Glykolyse und Ethanolbildung an, dargestellt als animiertes SVG in HTML. Die Aufnahme zeigt die entstandene wissenschaftliche Visualisierung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="SVG-Animation von Glykolyse bis Ethanol" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [Sechzehn gleichzeitige Starship-Starts](https://x.com/olddonkeyblog/status/2106507742454403485) (von [@olddonkeyblog](https://x.com/olddonkeyblog))

**Beschreibe synchronisierte Startphasen im Briefing einer HTML-und-SVG-Animation.**

Der Autor fordert sechzehn gemeinsam startende Starships an, gefolgt von Stufentrennung und dem Eintritt ins All. Die Aufnahme zeigt die daraus entstandene Animationssequenz mit mehreren Objekten.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="Sechzehn gleichzeitige Starship-Starts" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [Ein animierter Pelikan-Fahrrad-Test](https://x.com/olddonkeyblog/status/2106507429265756165) (von [@olddonkeyblog](https://x.com/olddonkeyblog))

**Betrachte eine Pelikan-Fahrradszene als Zeichenaufgabe für koordinierte Bewegung.**

Der Autor zeigt seinen Durchlauf der Pelikan-auf-dem-Fahrrad-Aufgabe mit Max-Denkintensität. Die Aufnahme ist ein eigenständiges Ergebnis neben den Versionen anderer Autoren für dieselbe allgemeine Aufgabe.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="Ein animierter Pelikan-Fahrrad-Test" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [Eine Geschichte der nächsten 150 Jahre](https://x.com/imjustnewatai/status/2106489784382197771) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Verbinde Skript, programmierte Bilder und Musik in einem spekulativen Zukunftsbriefing.**

Der Autor berichtet, mit einer einzigen Anweisung einen Film über die nächsten hundertfünfzig Jahre der Menschheit erstellt zu haben. Das Werk verbindet geschriebene Erzählung, programmierte Animation und Musik, um mögliches zukünftiges Leben darzustellen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="Eine Geschichte der nächsten 150 Jahre" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [Ein eigenes Humanity-Walks-Experiment](https://x.com/iowitz/status/2106489119186538583) (von [@iowitz](https://x.com/iowitz))

**Wiederhole eine Kunstgeschichte-Animationsidee als eigenständiges Kreativexperiment.**

Nachdem er andere Demonstrationen gesehen hat, versucht der Autor eine eigene Animation eines Gangs durch die Kunstgeschichte und zeigt das Ergebnis. Der Clip bleibt eine separate Generierung und wird nicht allein wegen des ähnlichen Themas zusammengelegt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="Ein eigenes Humanity-Walks-Experiment" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [Der programmierte Film The Grader](https://x.com/argofowl/status/2106476549046513947) (von [@argofowl](https://x.com/argofowl))

**Dokumentiere externe Sprach- oder Audioerzeugung bei der Präsentation eines programmierten Films.**

Der Autor zeigt The Grader als programmierten Film und nennt ElevenLabs v4 für das Audio. Er berichtet von einem einzigen Durchlauf mit etwa zwei Stunden und zweiundzwanzig Minuten Laufzeit.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="Der programmierte Film The Grader" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [Der Horror-Kurzfilm Reawakening](https://x.com/JaydenDavisNC/status/2106440774367822008) (von [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**Gib einem kurzen Animationsfilm mit einer benannten Horrorprämisse eine klare Richtung.**

Der Autor zeigt Reawakening, einen KI-Kurzfilm mit Horrorthema. Das angehängte Werk liefert ein konkretes Beispiel für Erzählung und Atmosphäre in einem Horroranimations-Briefing.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="Der Horror-Kurzfilm Reawakening" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [Ein 25-Sekunden-Video über Selbstverbesserung](https://x.com/DAssetBuzz/status/2106505100575592838) (von [@DAssetBuzz](https://x.com/DAssetBuzz))

**Verwandle ein abstraktes Selbstverbesserungsthema in ein kurzes kreatives Filmbriefing.**

Der Autor fordert ein fünfundzwanzigsekündiges Video darüber an, was das Modell verbessern könnte, und zeigt das Ergebnis. Die Prämisse dient kreativem Storytelling statt einer Aussage über Produkteigenschaften.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="Ein 25-Sekunden-Video über Selbstverbesserung" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [Eine Burgszene mit Kostenfeedback](https://x.com/nemumusitocha/status/2106429338556207284) (von [@nemumusitocha](https://x.com/nemumusitocha))

**Beziehe bei einer 3D-Szene sowohl sichtbare Details als auch die Nutzungserfahrung des Autors ein.**

Der Autor zeigt eine detailreiche Burgszene, lobt die visuelle Ausarbeitung und empfindet die Nutzungskosten als wenig lohnend. Der Fall verbindet eine konkrete Szene mit seinem Feedback zum Preis-Leistungs-Erlebnis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="Eine Burgszene mit Kostenfeedback" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [Ein 40-Sekunden-Spot für eine eigene Marke](https://x.com/0xashtonx/status/2106421702783914423) (von [@0xashtonx](https://x.com/0xashtonx))

**Mache deine eigene Marke zum Gegenstand eines knappen Launch-Spot-Briefings.**

Der Ersteller fordert einen vierzigsekündigen Einführungsspot für seine eigene Marke an und zeigt das entstandene Video. Die Aufgabe veranschaulicht konkret die Generierung einer markenbezogenen Werbeerzählung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="Ein 40-Sekunden-Spot für eine eigene Marke" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [Ein Rocketball-Remake](https://x.com/atomtanstudio/status/2106418747083022555) (von [@atomtanstudio](https://x.com/atomtanstudio))

**Verbinde bei einem bekannten Spiel-Remake programmierte Assets mit interaktiven Mechaniken.**

Der Autor zeigt Rocketball, ein Remake des C-64-Spiels aus den 1980er-Jahren, und berichtet, dass die Assets programmiert seien. Der Ersatz einer Website-Version wird als zukünftiger Plan beschrieben.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="Ein Rocketball-Remake" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [Ein Vergleich von Voxel-Pagoden](https://x.com/dropout_layer/status/2106408147309252915) (von [@dropout_layer](https://x.com/dropout_layer))

**Vergleiche zwei Durchläufe derselben Szene zusammen mit den jeweils gemeldeten Kosten.**

Der Autor zeigt Astra- und Fable-Ergebnisse für eine dreidimensionale Voxel-Pagode und nennt Kosten von 3,50 beziehungsweise 5,50 US-Dollar. Der Vergleich bezieht sich auf diese konkreten Durchläufe und die gezeigten Szenen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="Ein Vergleich von Voxel-Pagoden" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [Präsentation einer erfundenen Switch 3](https://x.com/mathisbuilds/status/2106407842240418097) (von [@mathisbuilds](https://x.com/mathisbuilds))

**Nutze ein erfundenes Produkt als Aufgabe für Konzeptpräsentation und Demonstration.**

Der Autor fordert eine erfundene Nintendo Switch 3 samt Demo an und berichtet von rund vier Stunden Arbeit. Die Aufnahme zeigt ein fiktives Konzept für eine nächste Konsole statt realer Produktspezifikationen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="Präsentation einer erfundenen Switch 3" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [Landingpages im Vorher-Nachher-Vergleich](https://x.com/nemumusitocha/status/2106402952307200302) (von [@nemumusitocha](https://x.com/nemumusitocha))

**Wiederhole denselben Landingpage-Prompt, um Veränderungen der Ergebnisse über die Zeit zu vergleichen.**

Der Autor vergleicht eine neu generierte Landingpage mit einer früheren Seite aus demselben Prompt. Die sichtbaren Vorher-Nachher-Designs liefern ein praktisches Beispiel für einen Oberflächenvergleich.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="Landingpages im Vorher-Nachher-Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [Die erfundene Innenperspektive einer KI](https://x.com/blueemi99/status/2106397329653719115) (von [@blueemi99](https://x.com/blueemi99))

**Nutze eine vorgestellte Innenperspektive als Prämisse für eine kreative Animation.**

Der Autor bittet um einen Film darüber, wie es sich anfühlen könnte, ein KI-Modell zu sein, und zeigt ein Ergebnis aus einem Durchlauf. Die Prämisse wird als fantasievolle visuelle Gestaltung präsentiert.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="Die erfundene Innenperspektive einer KI" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Lyric-Motion-Design zu Go](https://x.com/atomtanstudio/status/2106377491267137848) (von [@atomtanstudio](https://x.com/atomtanstudio))

**Animiere vorgegebene Liedtexte zu einer vorhandenen Songaufnahme.**

Der Ersteller zeigt ein Lyric-Video zu Go von The Chemical Brothers und berichtet von Max-Denkintensität. Die Songaufnahme bleibt der externe Audioeingang für die Motion-Design-Aufgabe.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Lyric-Motion-Design zu Go" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [Ein zweites 15-Sekunden-Motion-Portfolio](https://x.com/Saccc_c/status/2106376222309761094) (von [@Saccc_c](https://x.com/Saccc_c))

**Erkunde eine neue visuelle Richtung mit einem freien Motion-Design-Portfolio-Briefing.**

Der Autor zeigt ein neues fünfzehnsekündiges Motion-Portfolio und liefert den kreativen Prompt. Er unterscheidet diese Generierung ausdrücklich von einer früheren Portfolioarbeit.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="Ein zweites 15-Sekunden-Motion-Portfolio" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [Angeleitete Prüfung einer Agentenimplementierung](https://x.com/RobIW_dev/status/2106371025852108940) (von [@RobIW_dev](https://x.com/RobIW_dev))

**Prüfe Implementierungspläne auf Systempassung, bevor du von Ideen in die Umsetzung wechselst.**

Der Autor teilt Richtlinien zu Systempassung, Implementierungsplanung und Erklärungen und beschreibt, wie er Ergebnisse prüft oder die nächsten Implementierungsschritte bestimmt. Das Bild bewahrt das konkrete Planungsartefakt.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="Angeleitete Prüfung einer Agentenimplementierung" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [Das Claude-Maskottchen tanzt](https://x.com/ishuagra02/status/2106369929813594134) (von [@ishuagra02](https://x.com/ishuagra02))

**Teste mit einer rhythmischen Maskottchen-Animation das Zusammenspiel von Bewegung und Musik.**

Der Ersteller zeigt einen Tanz des Claude-Maskottchens und beschreibt, dass die Animation den Takt trifft. Wiederveröffentlichungen desselben nativen Videos werden dieser Quelle zugeordnet statt erneut gezählt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="Das Claude-Maskottchen tanzt" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [Interaktive Inseln der Sieben Weltwunder](https://x.com/notjazii/status/2106368606502334922) (von [@notjazii](https://x.com/notjazii))

**Nutze Wahrzeichen als Ziele innerhalb einer interaktiven Inselszene.**

Der Veröffentlicher zeigt eine Szene der Sieben Weltwunder, angeordnet als 3D-Inseln mit bekannten Bauwerken. Die Aufnahme veranschaulicht, wie erkennbare Monumente eine interaktive visuelle Umgebung strukturieren können.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="Interaktive Inseln der Sieben Weltwunder" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [Ein Musikvideo zu Propellerheads](https://x.com/atomtanstudio/status/2106353569603736009) (von [@atomtanstudio](https://x.com/atomtanstudio))

**Nutze einen vorgegebenen Soundtrack als Grundlage für längere Motion Graphics.**

Der Ersteller zeigt eine Musikvideogestaltung zu On Her Majesty’s Secret Service von Propellerheads. Die vorhandene Aufnahme liefert den Audioeingang für die animierte Bildfolge.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="Ein Musikvideo zu Propellerheads" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Steamboat-Willie-Animationen im Vergleich](https://x.com/mathisbuilds/status/2106351978691305732) (von [@mathisbuilds](https://x.com/mathisbuilds))

**Vergleiche zwei animierte Umsetzungen derselben kurzen Szene mit eingeschaltetem Ton.**

Der Autor zeigt einen Steamboat-Willie-Vergleich, der Fable und Opus bei xhigh-Denkintensität zugeordnet ist, und beschreibt die Ergebnisse als Einzeldurchläufe. Der Clip präsentiert den konkreten Bild-und-Ton-Vergleich.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Steamboat-Willie-Animationen im Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [Ein Film über Sanxingdui](https://x.com/hungryturbo/status/2106339115642019904) (von [@hungryturbo](https://x.com/hungryturbo))

**Strukturiere einen animierten Kurzfilm anhand eines kulturhistorischen Themas.**

Der Autor zeigt einen Sanxingdui-Film als kreatives visuelles Erzählwerk. Die Aufnahme veranschaulicht konkret, wie ein historisch-kulturelles Thema in ein Animationsbriefing übertragen werden kann.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="Ein Film über Sanxingdui" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Bugatti Chiron im Vorher-Nachher-Vergleich](https://x.com/alannnfx/status/2106323394350461031) (von [@alannnfx](https://x.com/alannnfx))

**Wiederhole einen älteren Auto-Prompt, um Modellierung und Funktionsdetails zu vergleichen.**

Derselbe Autor zeigt Bugatti-Chiron-Ergebnisse eines früheren Durchlaufs und eines erneut ausgeführten Prompts. Der aufgezeichnete Vorher-Nachher-Vergleich konzentriert sich auf reichere Modellierung und Szenendetails.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Bugatti Chiron im Vorher-Nachher-Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [Der Konzeptfilm GRAIN](https://x.com/NFT_Chen/status/2106301427052360150) (von [@NFT_Chen](https://x.com/NFT_Chen))

**Baue einen abstrakten Konzeptfilm um wiederkehrende visuelle Motive auf.**

Der Ersteller zeigt GRAIN, einen Konzeptkurzfilm, der Samen, Korn, einen Baum und Bergbilder verbindet. Wiederkehrende Formen und Übergänge bilden die Erzählstruktur der Sequenz.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="Der Konzeptfilm GRAIN" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [Die Kunstgalerie Human in Transit](https://x.com/exploraX_/status/2106296439936614646) (von [@exploraX_](https://x.com/exploraX_))

**Präsentiere eine historische visuelle Reise als interaktiv gestaltete Kunstgalerie.**

Der Veröffentlicher zeigt Human in Transit, eine Galerie von antiken bis modernen Kunststilen. Die aufgezeichnete Oberfläche liefert ein konkretes Beispiel dafür, mehrere visuelle Epochen in einer Präsentation zu ordnen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="Die Kunstgalerie Human in Transit" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [Ein visueller Kurzfilm über die Seidenstraße](https://x.com/hungryturbo/status/2106294812261695508) (von [@hungryturbo](https://x.com/hungryturbo))

**Übertrage ein Reise-und-Geschichte-Thema in einen zusammenhängenden visuellen Kurzfilm.**

Der Autor zeigt einen Film über die Seidenstraße. Das angehängte Werk liefert eine konkrete kreative Umsetzung einer historischen Reise mit animierten Bildern.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="Ein visueller Kurzfilm über die Seidenstraße" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [Eine Präsentation über vier Transformationen](https://x.com/dpkostka/status/2106272731364794757) (von [@dpkostka](https://x.com/dpkostka))

**Nutze ein Transformationsmodell als Ordnungsstruktur für eine Präsentation.**

Der Autor zeigt Folien zu vier Transformationspfaden. Das angehängte Präsentationsbild veranschaulicht, wie sich ein konzeptionelles Modell in einem visuellen Dokument anordnen lässt.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="Eine Präsentation über vier Transformationen" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [Den Ton früherer Chats vergleichen](https://x.com/kiyoshi_shin/status/2106268573186637883) (von [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**Vergleiche ältere Chatprotokolle mit aktuellen Antworten, wenn du Tonveränderungen untersuchst.**

Der Autor lässt frühere Chatprotokolle und den gegenwärtigen Stil vom aktuellen Modell analysieren und berichtet anschließend von Unzufriedenheit mit dem veränderten Ton. Das angehängte Bild dokumentiert diesen Gesprächsvergleich.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="Den Ton früherer Chats vergleichen" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [Ein Kakapo-Niedlichkeitstest](https://x.com/hanawo_neki/status/2106257409782288659) (von [@hanawo_neki](https://x.com/hanawo_neki))

**Vergleiche Animationsstile mit einer konkreten Aufgabe zu einer gewünschten Figurenwirkung.**

Der Autor zeigt eine Kakapo-Animation und bevorzugt Opus bei diesem auf Niedlichkeit ausgerichteten Vergleich. Der Fall bewahrt das negative ästhetische Feedback zusammen mit dem tatsächlichen animierten Ergebnis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="Ein Kakapo-Niedlichkeitstest" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [Spider-Man durch zehn Comic-Epochen](https://x.com/chetaslua/status/2106248621519978867) (von [@chetaslua](https://x.com/chetaslua))

**Halte eine Figur beim Wechsel durch mehrere Comic-Epochen wiedererkennbar.**

Der ursprüngliche Veröffentlicher zeigt Spider-Man in zehn Comic-Epochen. Andere Beiträge mit demselben Video werden dieser Quelle zugeordnet statt als zusätzliche Werke gezählt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="Spider-Man durch zehn Comic-Epochen" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [Ein fiktives Illuminati-Horrorvideo](https://x.com/badboyfoxy/status/2106241189976387799) (von [@badboyfoxy](https://x.com/badboyfoxy))

**Behandle ein verschwörungsthematisches Horrorbriefing als fiktive Erzählübung.**

Der Autor fordert ein gruseliges Illuminati-Video an und zeigt das entstandene Werk. Das Thema liefert eine fiktive Horrorprämisse für die Animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="Ein fiktives Illuminati-Horrorvideo" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [Ein programmierter Film zur Geschichte der Kernwissenschaft](https://x.com/imjustnewatai/status/2106238699872956427) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Verbinde einen eigenen programmierten Renderer und Musik zu einem wissenschaftshistorischen Erklärfilm.**

Der Autor fordert einen dreiminütigen 3D-Film darüber an, wie Kernwissenschaft die Atombombe möglich machte, und berichtet von gezeichneten Frames, eigenem Renderer und synthetischer Musik. Der Fall betrifft den audiovisuellen Produktionsworkflow.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="Ein programmierter Film zur Geschichte der Kernwissenschaft" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [Erklärvideo zum universellen hohen Einkommen](https://x.com/markbraincell/status/2106234118514323515) (von [@markbraincell](https://x.com/markbraincell))

**Vermittle ein wirtschaftliches Konzept mit einer animierten Erklärung.**

Der Veröffentlicher zeigt eine Animation zum universellen hohen Einkommen. Die Aufnahme liefert ein konkretes Beispiel für einen Konzepterklärfilm, ohne das dargestellte wirtschaftliche Argument als gemessenes Ergebnis zu behandeln.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="Erklärvideo zum universellen hohen Einkommen" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [Ein Erklärfilm zum Altman-Amodei-Konflikt](https://x.com/imjustnewatai/status/2106204392588276065) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Nutze einen Konflikt als Erzählstruktur für einen animierten Erklärfilm.**

Der Autor fordert eine animierte Darstellung des Altman-Amodei-Konflikts an und zeigt das entstandene Video. Die Aufgabe veranschaulicht ein aktuelles Erklärformat statt einer unabhängig recherchierten historischen Darstellung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="Ein Erklärfilm zum Altman-Amodei-Konflikt" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [Ein Claude-Maskottchen-Musikvideo](https://x.com/synthshareai/status/2106195060140446028) (von [@synthshareai](https://x.com/synthshareai))

**Verbinde eine Maskottchen-Einblendung mit vorgegebenem Filmmaterial für einen figurenbezogenen Musikvideo-Edit.**

Der Veröffentlicher zeigt ein Claude-Maskottchen vor einem gefilmten Musikvideo-Hintergrund und berichtet von einem zwölfstündigen Durchlauf. Die sichtbare Gestaltung verbindet eine Cartoon-Einblendung mit vorhandenem Filmmaterial.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="Ein Claude-Maskottchen-Musikvideo" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [Ein durchgehender Zoom von Quarks zum Universum](https://x.com/imjustnewatai/status/2106190594775097663) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Verbinde wissenschaftliche Größenordnungen mit einem durchgehenden Zoom in einer audiovisuellen Geschichte.**

Der Autor berichtet von programmierten Bildern und synthetischer Musik für einen Zoom von Quarks bis zum Universum. Die Aufnahme veranschaulicht kontinuierliche Größenübergänge und eine zusammenhängende visuelle Erzählung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="Ein durchgehender Zoom von Quarks zum Universum" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [Die Welt im Jahr 2076 vorstellen](https://x.com/Layton_Gott/status/2106190496075035096) (von [@Layton_Gott](https://x.com/Layton_Gott))

**Fordere eine Zukunftsszene mit einer bestimmten Erzähldauer an.**

Der Autor zeigt einen Kurzfilm über die Welt im Jahr 2076, nachdem er um ein fünfundzwanzigsekündiges Video gebeten hat. Die Wiederverwendung derselben Aufnahme durch andere Konten wird dieser Quelle zugeordnet.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="Die Welt im Jahr 2076 vorstellen" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [Chronologie der Gebäude von Lower Manhattan](https://x.com/nroze22/status/2106183281293381661) (von [@nroze22](https://x.com/nroze22))

**Verbinde Grundflächen, Baujahre und Höhen in einer architektonischen Zeitleistenoberfläche.**

Der Autor präsentiert Lower Manhattan in einer Oberfläche im Stil einer Architekturzeichnung mit Baujahren, Gebäudegrundflächen und Höhen. Die Aufnahme liefert ein konkretes Konzept für eine interaktive Chronologie.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="Chronologie der Gebäude von Lower Manhattan" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [Eine Animation über Orakelknochenschrift](https://x.com/MinLiBuilds/status/2106180691344118202) (von [@MinLiBuilds](https://x.com/MinLiBuilds))

**Nutze die Entwicklung der Schrift als Thema einer animierten historischen Reise.**

Der Autor zeigt eine Animation, die mit Orakelknochenschrift beginnt. Die Aufnahme liefert ein konkretes Beispiel für visuelles Storytelling rund um die Geschichte geschriebener Zeichen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="Eine Animation über Orakelknochenschrift" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [Eine weitere Figurenreise durch die Kunstgeschichte](https://x.com/imjustnewatai/status/2106162924331180510) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Nutze vertraute Figuren als durchgehende Begleiter in einer wechselnden historischen Umgebung.**

Der Autor fordert Iron Man und Spider-Man auf einem Flug durch die Geschichte an und zeigt die entstandene Animation. Das Werk ist von den Kunstgeschichte-Experimenten anderer Autoren mit Figuren zu unterscheiden.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="Eine weitere Figurenreise durch die Kunstgeschichte" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [Ein programmiertes Seikilos-Bild-und-Ton-Werk](https://x.com/YanqingCheng/status/2106158746938269728) (von [@YanqingCheng](https://x.com/YanqingCheng))

**Baue ein audiovisuelles Ein-Datei-Werk um einen historischen musikalischen Text auf.**

Der Autor zeigt ein Werk zum Seikilos-Epitaph und berichtet von in einer Datei mit HTML und JavaScript synthetisierten Bildern und Musik. Der historische Text strukturiert die programmierte audiovisuelle Sequenz.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="Ein programmiertes Seikilos-Bild-und-Ton-Werk" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [Jet-Animationen im Vergleich](https://x.com/Kinzf2121/status/2106158536963330346) (von [@Kinzf2121](https://x.com/Kinzf2121))

**Vergleiche Flugbewegung und Kameraverfolgung bei derselben Flugzeugaufgabe.**

Der Autor zeigt einen Vergleich zwischen einer als Fable 5.1 bezeichneten Jet-Animation und Opus. Die Szenen eignen sich konkret zum Vergleich von Flugzeugbewegung und filmischer Kameraverfolgung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="Jet-Animationen im Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [Ein Film zur Selbstvorstellung des Modells](https://x.com/devteamdrew/status/2106155815707021549) (von [@devteamdrew](https://x.com/devteamdrew))

**Erkunde eine modellbezogene Animation mit einem Selbstvorstellungsbriefing.**

Der Ersteller berichtet, mit einem Prompt ein Selbstvorstellungsvideo angefordert zu haben, und zeigt den Film. Die Aufgabe verbindet eine modellbezogene Erzählung mit animierter Präsentation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="Ein Film zur Selbstvorstellung des Modells" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [Ein postapokalyptischer Kartenspiel-Prototyp](https://x.com/maciejkrupowies/status/2106153578029338850) (von [@maciejkrupowies](https://x.com/maciejkrupowies))

**Erprobe ein Kartenspielthema und betrachte die entstandene Kampfoberfläche.**

Der Autor zeigt einen postapokalyptischen Prototyp im Hearthstone-Stil, den er als Einzeldurchlauf beschreibt. Er erwähnt kleinere Fehler und demonstriert Oberfläche sowie Interaktionen des Spiels.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="Ein postapokalyptischer Kartenspiel-Prototyp" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [Die Arbeitsplatzanimation The Late Byte](https://x.com/rohit3a/status/2106138910648914094) (von [@rohit3a](https://x.com/rohit3a))

**Mache Modellpersönlichkeiten zu Figuren eines animierten Arbeitsplatzgesprächs.**

Der Ersteller präsentiert The Late Byte, eine animierte Arbeitsplatzgeschichte mit Opus als wütendem Chef. Die Erzählung ist vom separaten Film Day in the Life of Claude zu unterscheiden.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="Die Arbeitsplatzanimation The Late Byte" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Textanimation zu Queens of the Stone Age](https://x.com/atomtanstudio/status/2106135196483608745) (von [@atomtanstudio](https://x.com/atomtanstudio))

**Verbinde einen vorgegebenen Song mit kinetischer Typografie und Motion Design.**

Der Ersteller beschreibt ein Musikvideo mit kinetischer Typografie zu einer Aufnahme von Queens of the Stone Age. Der Song ist der Audioeingang; das Beispiel betrifft die Anordnung von Liedtext und Bildern.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Textanimation zu Queens of the Stone Age" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [Eine geteilte Three.js-Erzählszene](https://x.com/Noreply134882/status/2106116572389478746) (von [@Noreply134882](https://x.com/Noreply134882))

**Nutze einen geteilten 3D-Erzählclip als Referenz für narrative Szenengestaltung.**

Der Veröffentlicher teilt eine Three.js-Erzählszene und kommentiert den hohen Tokenverbrauch. Der Clip bleibt als geteiltes visuelles Beispiel für 3D-Storytelling erhalten.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="Eine geteilte Three.js-Erzählszene" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [Moonwalk durch historische Szenen](https://x.com/noclipepe/status/2106105810812112937) (von [@noclipepe](https://x.com/noclipepe))

**Führe ein Tanzmotiv durch verschiedene historische Umgebungen und visuelle Stile.**

Der Veröffentlicher zeigt eine Michael-Jackson-Moonwalk-Sequenz von Dinosauriern bis zum Mond. Der Film bleibt als geteiltes Beispiel für eine Tanz-und-Stil-Galerie erhalten.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="Moonwalk durch historische Szenen" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [Motion Graphics mit ausführlichem Prompt](https://x.com/devswha/status/2106100273509007802) (von [@devswha](https://x.com/devswha))

**Vergleiche ein ausführliches Kreativbriefing mit einer kürzeren Motion-Design-Anfrage.**

Der Autor zeigt ein Motion-Graphics-Video und berichtet, nur einen ausführlichen Prompt geliefert zu haben, ohne Assets, Referenzvideo oder Quelldateien. Das Ergebnis ist eine konkrete Referenz für promptgesteuertes Motion Design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="Motion Graphics mit ausführlichem Prompt" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [Website-Oberfläche für ein Vermietungsunternehmen](https://x.com/oalanicolas/status/2106098902965309475) (von [@oalanicolas](https://x.com/oalanicolas))

**Erkunde mit einem Vermietungsbriefing eine konkrete Website-Oberfläche.**

Der Ersteller zeigt einen Screenshot einer Website für ein Vermietungsunternehmen. Das Beispiel betrifft das sichtbare Seitendesign und die Darstellung des Geschäfts.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="Website-Oberfläche für ein Vermietungsunternehmen" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [Ein kreativer Film mit AGI-Thema](https://x.com/AndrewOnXYZ/status/2106097745098395712) (von [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**Vergleiche Erzählung und Bildsprache mit einem wiederkehrenden Kreativprompt.**

Der Autor zeigt eine AGI-bezogene Animation aus einem wiederkehrenden Prompt. Aussagen des Modells gehören im Film zur kreativen Erzählung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="Ein kreativer Film mit AGI-Thema" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [Kunstgeschichte mit einer Katzen-Nebenhandlung](https://x.com/cherry_mx_reds/status/2106095190285144331) (von [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Verdichte mehrere Kunstepochen zu einer kurzen Geschichte mit wiederkehrender Figur.**

Der Ersteller präsentiert eine fünfzehnsekündige Reise durch die Kunstgeschichte mit einer Katzen-Nebenhandlung. Die fünfzehn Sekunden bezeichnen die Filmlänge; die Kreativaufgabe umfasst zahlreiche historische Stile.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="Kunstgeschichte mit einer Katzen-Nebenhandlung" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [Kampfprototyp und Voxel-Szene](https://x.com/OnlyTerp/status/2106089280502210626) (von [@OnlyTerp](https://x.com/OnlyTerp))

**Betrachte Kampfsystem und Weltgestaltung als Ergebnisse einer Kreativprogrammieraufgabe.**

Der Autor zeigt einen Kampfprototyp im DMC-Stil und eine Voxel-Szene und beschreibt einen langen Generierungslauf. Die beiden Ergebnisse erlauben die Betrachtung von Spielmechaniken und visueller Weltgestaltung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="Kampfprototyp und Voxel-Szene" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [Chronologie von Internet-Memes](https://x.com/chetaslua/status/2106076940558082297) (von [@chetaslua](https://x.com/chetaslua))

**Ordne eine animierte Chronologie nach jahresspezifischen Bildstilen und Musik.**

Der Ersteller zeigt eine animierte Folge viraler Internet-Memes von 2010 bis 2026. Jedes Jahr erhält im programmierten Erzählwerk einen eigenen visuellen und musikalischen Stil.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="Chronologie von Internet-Memes" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [Partikelbewegung aus einer Zeile](https://x.com/devswha/status/2106072107365114186) (von [@devswha](https://x.com/devswha))

**Beginne mit einem einzeiligen Bewegungsbriefing, bevor du einen ausführlichen Prompt ausarbeitest.**

Der Ersteller zeigt eine Partikelanimation aus einem einzeiligen Prompt und plant eine ausführlichere Anfrage. Es handelt sich um eine andere Generierung als sein längeres Motion-Design-Beispiel.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="Partikelbewegung aus einer Zeile" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [Die Animation Kung-Fu Boy](https://x.com/HashmathRzz/status/2106065773336965510) (von [@HashmathRzz](https://x.com/HashmathRzz))

**Erkunde animierte Bewegung mit einem Kampfkunst-Figurenbriefing.**

Der Autor zeigt Kung-Fu Boy, eine Fable 5.5 zugeschriebene Figurenanimation. Die Aufnahme liefert das konkrete Ergebnis für das Kampfkunstthema.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="Die Animation Kung-Fu Boy" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [Eine animierte Debatte zur Straße von Hormus](https://x.com/chetaslua/status/2106060047805792415) (von [@chetaslua](https://x.com/chetaslua))

**Verwandle ein Debattenthema in eine animierte Erzählung.**

Der Ersteller präsentiert eine animierte Debatte über die Straße von Hormus. Dieser Fall erfasst den sichtbaren Film statt weiterer unbelegter Anwendungen, die im Beitrag nebenbei genannt werden.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="Eine animierte Debatte zur Straße von Hormus" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [Ein Einhorn-SVG-Stilexperiment](https://x.com/atomtanstudio/status/2106057876053918127) (von [@atomtanstudio](https://x.com/atomtanstudio))

**Betrachte SVG-Stilentscheidungen anhand derselben thematischen Zeichenaufgabe.**

Der Autor zeigt ein Einhorn-SVG-Experiment, das vom Test eines anderen Erstellers inspiriert ist. Das Bild liefert das konkrete Ergebnis zum Vergleich der visuellen Behandlung desselben Motivs.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="Ein Einhorn-SVG-Stilexperiment" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [Eine saisonale Halloween-Animation](https://x.com/cherry_mx_reds/status/2106056643255447590) (von [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Gib einem Programmiermodell ein saisonales Thema für eine kurze kreative Animation.**

Der Ersteller fordert ein Halloween-Werk an und zeigt die entstandene Animation. Der Beitrag liefert die Originalaufnahme dieser konkreten Kreativaufgabe.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="Eine saisonale Halloween-Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Blender-CLI-Barbar und Titelbild](https://x.com/BoDy051/status/2106047375320166885) (von [@BoDy051](https://x.com/BoDy051))

**Erkunde Figurenmodellierung und Titelbild-Rendering mit Blender-CLI-Anweisungen.**

Der Autor vergleicht einen RPG-Barbaren und ein Titelbildkonzept mit einem Opus-Ergebnis. Blender CLI übernimmt Aufbau und Rendering; das Modell liefert Codeanweisungen.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Blender-CLI-Barbar und Titelbild" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Ein Tag im Leben von Claude](https://x.com/ishuagra02/status/2106045364868419727) (von [@ishuagra02](https://x.com/ishuagra02))

**Baue eine animierte Alltagsgeschichte um ein wiederkehrendes Maskottchen auf.**

Der ursprüngliche Veröffentlicher zeigt den Maskottchen-Film Day in the Life of Claude. Das Quellvideo unterscheidet sich von der separaten Maskottchen-Tanzanimation und deren Wiederveröffentlichungen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Ein Tag im Leben von Claude" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [Menschheitsgeschichte in 3D](https://x.com/blueemi99/status/2106041578204655748) (von [@blueemi99](https://x.com/blueemi99))

**Verbinde programmierte Szenen und Animation zu einer historischen Bildfolge.**

Der Ersteller zeigt ein 3D-Video von der frühen Menschheit bis zur Gegenwart und berichtet, Animationen und Modelle programmiert zu haben. Das Ergebnis ist ein Beispiel für visuelles Storytelling.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="Menschheitsgeschichte in 3D" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [Ein schnelles Motion-Design-Reel](https://x.com/blueemi99/status/2106031355922387163) (von [@blueemi99](https://x.com/blueemi99))

**Beurteile Tempo, Ton und Zusammenhalt eines kurzen Motion-Design-Reels.**

Der Autor zeigt ein kurzes, schnelles Motion-Video und vergleicht Ton und Zusammenhalt mit seinem Opus-Ergebnis. Das Urteil beschreibt seine Erfahrung mit diesem konkreten Werk.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="Ein schnelles Motion-Design-Reel" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [Eine freie, komplexe 3D-Kreation](https://x.com/cocoloba_/status/2106029181607772413) (von [@cocoloba_](https://x.com/cocoloba_))

**Erkunde mit einer offenen Kreativfrage eine komplexe 3D-Komposition.**

Der Ersteller fragt, was das Modell in freier Zeit machen würde, und zeigt das entstandene 3D-Werk. Der Beitrag beschreibt zahlreiche getrennte Teile als Bestandteile der Komposition.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="Eine freie, komplexe 3D-Kreation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [Eine Strichmännchen-Kampfanimation](https://x.com/HelaliBillel/status/2106028502763900944) (von [@HelaliBillel](https://x.com/HelaliBillel))

**Betrachte Timing und Bewegung anhand einer konkreten Kampfszenen-Anfrage.**

Der Ersteller fordert ein Video mit einem animierten Strichmännchenkampf an und zeigt das Ergebnis. Die Aufnahme liefert ein konkretes Beispiel dieser Kampfanimationsaufgabe.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="Eine Strichmännchen-Kampfanimation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [Eine UI-Bewegungsfolge aus einem Prompt](https://x.com/iancarscadden/status/2106018048792789360) (von [@iancarscadden](https://x.com/iancarscadden))

**Erkunde eine Oberflächenbewegungsfolge mit einem einzigen Animationsbriefing.**

Der Autor zeigt eine UI-Bewegungsfolge, die er als Einzeldurchlauf von etwa sechs oder sieben Minuten beschreibt. Die Aufnahme zeigt die für diese Anfrage entstandene Bildfolge.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="Eine UI-Bewegungsfolge aus einem Prompt" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [Eine fiktive SCP-8517-Animation](https://x.com/eviljoker88/status/2106003621402005816) (von [@eviljoker88](https://x.com/eviljoker88))

**Nutze eine SCP-inspirierte Prämisse als Briefing für eine animierte Geschichte.**

Der Ersteller präsentiert eine SCP-8517-Animation und schreibt ihre Erstellung Fable 5.5 zu. Der Fall betrifft die fiktive Erzählung und ihre sichtbare Animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="Eine fiktive SCP-8517-Animation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [Eine herbstliche Aquarellanimation](https://x.com/ishuagra02/status/2106000055706784118) (von [@ishuagra02](https://x.com/ishuagra02))

**Lege ein saisonales Motiv und eine Aquarellgestaltung für eine Animation fest.**

Der Autor zeigt eine herbstliche Animation im Aquarellstil. Das aufgezeichnete Werk veranschaulicht die Verbindung eines saisonalen Motivs mit einem bestimmten Bildmedium.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="Eine herbstliche Aquarellanimation" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [Eine prozedurale Puppenbühne](https://x.com/HelaliBillel/status/2105988689088196785) (von [@HelaliBillel](https://x.com/HelaliBillel))

**Betrachte die Animation einer puppenartigen Figur in einer inszenierten Szene.**

Der Autor zeigt eine prozedurale Puppenbühnen-Animation und erwähnt Blender in der Diskussion. Der Fall betrifft die sichtbare inszenierte Figur und ihre Bewegung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="Eine prozedurale Puppenbühne" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [Eine im Browser gerenderte Pelikanfahrt](https://x.com/slimcat0101/status/2105988654636380444) (von [@slimcat0101](https://x.com/slimcat0101))

**Führe eine Figurenbewegung im Browser aus und betrachte die gerenderte Szene.**

Der Ersteller fordert einen Pelikan auf einem Fahrrad an und nimmt das resultierende HTML im Browser auf. Diese bewegte Browserszene unterscheidet sich von statischen SVG-Zeichentests.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="Eine im Browser gerenderte Pelikanfahrt" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [Das Universum betrachtet sich selbst](https://x.com/l_mejiaC/status/2105988529671360673) (von [@l_mejiaC](https://x.com/l_mejiaC))

**Verbinde weit entfernte Größenordnungen durch eine durchgehende visuelle Reise.**

Der Ersteller präsentiert eine kontinuierliche Folge vom Urknall bis zu einem menschlichen Auge. Er beschreibt Bilder und Musik als für den Film durch Laufzeitcode erzeugt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="Das Universum betrachtet sich selbst" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [Ein eigenständiger Jet-Animationstest](https://x.com/AI_Screening/status/2105988448612135176) (von [@AI_Screening](https://x.com/AI_Screening))

**Wiederhole eine Flugzeuganimationsaufgabe und betrachte das konkrete Ergebnis.**

Nach Diskussionen über Routing probiert der Autor eine Jet-Animationsaufgabe aus und zeigt sein Ergebnis. Die Aufnahme liefert eine eigenständige Quelle für dieses Flugzeugbeispiel.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="Ein eigenständiger Jet-Animationstest" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [Ein erstes freies Motion-Reel](https://x.com/Saccc_c/status/2105985484472377531) (von [@Saccc_c](https://x.com/Saccc_c))

**Erkunde Motion Design mit einem kurzen offenen Prompt.**

Der Ersteller zeigt ein erstes Motion-Design-Reel, das er als Ergebnis eines Prompts beschreibt. Es ist ein anderes, früheres Ergebnis als sein späteres fünfzehnsekündiges Portfolio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="Ein erstes freies Motion-Reel" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [Zivilisation in Code gerendert](https://x.com/ziwenxu_/status/2105983571848741045) (von [@ziwenxu_](https://x.com/ziwenxu_))

**Verwandle ein Briefing zur Zivilisationsgeschichte in eine programmierte animierte Erzählung.**

Der Autor fordert die Zivilisation von ihren Anfängen bis heute an und zeigt den entstandenen Film. Nach seiner Darstellung nutzt diese programmierte Bildgestaltung weder vorhandene Aufnahmen noch Archivassets.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="Zivilisation in Code gerendert" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [Chip-zu-Server-Zoom im Vergleich](https://x.com/SPAC89/status/2105968361725202591) (von [@SPAC89](https://x.com/SPAC89))

**Vergleiche Realismus und Kontinuität einer Zoomfahrt vom Chip zum Server.**

Der Autor vergleicht Fable XHigh und GPT Sol Ultra bei einer realistischen Zoomsequenz und bespricht Tempo sowie Kontingentverbrauch. Der Beitrag behandelt konkrete Durchläufe mit unterschiedlichen Abostufen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="Chip-zu-Server-Zoom im Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [Ein persönliches Mondreise-Animationsprojekt](https://x.com/IgorGomezC/status/2105963552024506565) (von [@IgorGomezC](https://x.com/IgorGomezC))

**Erkunde ein persönliches Animationskonzept mit mehreren Programmiermodellen.**

Der Ersteller zeigt ein persönliches Mondreise-Animationsprojekt und bespricht Experimente mit Fable und Opus. Das angehängte Werk ist das konkrete Ergebnis dieser kreativen Erkundung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="Ein persönliches Mondreise-Animationsprojekt" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [Japanische Voxel-Szenen im Vergleich](https://x.com/vikktorrrre/status/2105955048018588084) (von [@vikktorrrre](https://x.com/vikktorrrre))

**Vergleiche Details, Nebel und Bildklarheit mit demselben Szenenprompt.**

Der Autor vergleicht aktuelle Fable- und Opus-Ergebnisse für denselben Prompt einer japanischen Voxel-Szene. Die Beobachtungen betreffen Klarheit, Nebel und ästhetische Gestaltung dieser konkreten Ergebnisse.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="Japanische Voxel-Szenen im Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [Der audiovisuelle Kurzfilm Steaming the Frontier](https://x.com/sdmat123/status/2105929299878703520) (von [@sdmat123](https://x.com/sdmat123))

**Verbinde einen Steamboat-artigen Bildstil mit Ton für einen audiovisuellen Kurzfilm.**

Der Ersteller zeigt Steaming the Frontier, ein animiertes Werk mit Ton. Es bleibt eine eigenständige Quelle neben unabhängigen Steamboat-artigen Ergebnissen anderer Ersteller.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="Der audiovisuelle Kurzfilm Steaming the Frontier" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [Superman in mehreren Kunststilen](https://x.com/Mr_Salio/status/2105925979466052051) (von [@Mr_Salio](https://x.com/Mr_Salio))

**Führe eine Figur in einer durchgehenden Animation durch wechselnde Kunststile.**

Der Ersteller erklärt, ein früheres Superman-Beispiel habe ihn zu einer neuen Generierung inspiriert, und zeigt sein Ergebnis. Die andere Bildgestaltung macht es zu einer eigenen Kreation statt einer Wiederveröffentlichung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="Superman in mehreren Kunststilen" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Ein Bosskampf-Prototyp im Cupcake-Stil](https://x.com/maciejkrupowies/status/2105914965387321785) (von [@maciejkrupowies](https://x.com/maciejkrupowies))

**Erprobe einen seitlich scrollenden Bosskampf und betrachte die entstehenden Kampfszenen.**

Der Autor zeigt einen Bosskampf-Prototyp im Cupcake-Stil und berichtet von einer Generierung in unter zehn Minuten. Die Aufnahme zeigt die Kampfsequenz des Spiels.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Ein Bosskampf-Prototyp im Cupcake-Stil" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [Segelschiff bei wechselndem Sonnenstand](https://x.com/popat_kunj/status/2105907935490752822) (von [@popat_kunj](https://x.com/popat_kunj))

**Erkunde Himmel, Wasser und wechselnden Sonnenstand mit einer Segelszene.**

Der Ersteller zeigt ein 3D-Segelschiff bei verschiedenen Sonnenständen und verlinkt ein interaktives Artefakt. Die Szene verbindet Schiff, Himmel und Wasser in einer visuellen Aufgabe.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="Segelschiff bei wechselndem Sonnenstand" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Ein Video zu Paracortex-und-Pi-Änderungen](https://x.com/RobIW_dev/status/2105894547796476225) (von [@RobIW_dev](https://x.com/RobIW_dev))

**Verwandle Produktupdates in eine kurze Motion-Design-Ankündigung.**

Der Autor überträgt Updates von Paracortex und Pi in ein fünfundzwanzigsekündiges Motion-Design-Video und liefert einen Prompt im Beitrag. Das Werk veranschaulicht visuelle Produktkommunikation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Ein Video zu Paracortex-und-Pi-Änderungen" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Ein Website-Promo für Curio 2.0](https://x.com/voltwake/status/2105884775982485642) (von [@voltwake](https://x.com/voltwake))

**Erstelle einen programmierten Werbefilm zu einem bestehenden Website-Launch.**

Der Ersteller beschreibt ein Launch-Promo für Curio 2.0 mit programmierten Bildern, Kameraführung und Musik. Der Beitrag zeigt den daraus entstandenen Website-Werbefilm.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Ein Website-Promo für Curio 2.0" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [Eine erfundene Hugging-Face-Geschichte in 3D](https://x.com/chetaslua/status/2105884276864782557) (von [@chetaslua](https://x.com/chetaslua))

**Verbinde modellgeschriebenen Code mit Rendering-und-Audiowerkzeugen für einen fiktiven Film.**

Der Ersteller zeigt eine erfundene Hugging-Face-Geschichte mit Modellcode, Blender und ElevenLabs-API. Blender übernimmt Aufbau und Rendering; ElevenLabs liefert externes Audio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="Eine erfundene Hugging-Face-Geschichte in 3D" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [Claude für Chrome bedient JS Paint](https://x.com/BtwIUseSystemd/status/2105861662112923849) (von [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**Gib einem Browseragenten eine Zeichenaufgabe, die nur die Werkzeuge der Anwendung erlaubt.**

Der Autor bittet Claude für Chrome, eine Person ausschließlich mit JS-Paint-Werkzeugen zu zeichnen, und zeigt das Ergebnis. Browserbedienung und Zeichenanwendung sind ausdrücklich Teil der Aufgabe.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="Claude für Chrome bedient JS Paint" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [Ein statisches Pelikan-Fahrrad-SVG](https://x.com/olddonkeyblog/status/2105842745189556672) (von [@olddonkeyblog](https://x.com/olddonkeyblog))

**Teste eine detailreiche statische Zeichnung mit einem eigenständigen SVG-Auftrag.**

Der Ersteller fordert eine einzelne eigenständige SVG-Datei eines Pelikans auf einem Fahrrad an und zeigt das statische Bild. Diese Zeichenaufgabe unterscheidet sich von den animierten Fahrbeispielen.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="Ein statisches Pelikan-Fahrrad-SVG" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [BlockBench MCP mit einem Minecraft-Skill](https://x.com/TOPSTR1X/status/2105839618872738138) (von [@TOPSTR1X](https://x.com/TOPSTR1X))

**Stelle beim Erzeugen einer Spielfigur ein Modellierungswerkzeug und einen Stil-Skill bereit.**

Der Autor liefert BlockBench MCP und einen eigenen Minecraft-Skill für Modellierung und Farbgebung und zeigt danach die Figur. Werkzeuge und Stilvorgaben sind ausdrücklich Eingaben des Workflows.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="BlockBench MCP mit einem Minecraft-Skill" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [Dig Dug in einer HTML-Datei](https://x.com/imjustnewatai/status/2105831117677084841) (von [@imjustnewatai](https://x.com/imjustnewatai))

**Lege beim Nachbau eines kompakten Browserspiels eine einzelne HTML-Datei als Ziel fest.**

Der Ersteller fordert einen Dig-Dug-Nachbau in einer einzigen HTML-Datei an und zeigt die Spielaufnahme. Der Beitrag beschreibt den Aufbau als Ergebnis eines Prompts.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="Dig Dug in einer HTML-Datei" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [Ein mechanischer Oktopus als SVG](https://x.com/SEO/status/2105812236774297943) (von [@SEO](https://x.com/SEO))

**Betrachte Details und Bewegung im SVG-Design anhand eines mechanischen Wesens.**

Der Autor zeigt ein animiertes Oktopus-SVG mit mechanischen Details. Die Aufnahme liefert ein konkretes Vektordesign-Beispiel mit kleinen beweglichen Teilen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="Ein mechanischer Oktopus als SVG" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [Humanity Walks durch Kunststile](https://x.com/l_mejiaC/status/2105801379956850793) (von [@l_mejiaC](https://x.com/l_mejiaC))

**Führe eine wiederkehrende Figur durch eine Folge historischer Bildstile.**

Der ursprüngliche Ersteller zeigt einen durchgehenden Gang durch zwanzig Kunsttafeln über rund vierundsiebzig Sekunden und berichtet von programmierter Musik. Jede Grenze versetzt Figur und Szene in einen neuen Stil.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="Humanity Walks durch Kunststile" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [Eine offene Schwarzes-Loch-Szene](https://x.com/rohit3a/status/2105786053412208835) (von [@rohit3a](https://x.com/rohit3a))

**Erkunde eine Schwarzes-Loch-Visualisierung mit einem offenen Kreativbriefing.**

Der Ersteller fragt, was das Modell machen würde, um ihn zu beeindrucken, und zeigt eine Schwarzes-Loch-Szene. Die Aufgabe ist eine freie visuelle Erkundung statt eines vorgeschriebenen Oberflächenaufbaus.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="Eine offene Schwarzes-Loch-Szene" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [Aurora-Quallenanimationen im Vergleich](https://x.com/SPAC89/status/2105783511433318451) (von [@SPAC89](https://x.com/SPAC89))

**Vergleiche Verformung und Bewegung zweier Quallenanimationen.**

Der Autor vergleicht Fable XHigh und GPT Sol Ultra bei einer Aurora-Quallenanimation und bespricht den Kontingentverbrauch. Die Ergebnisse stammen aus unterschiedlichen Abostufen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="Aurora-Quallenanimationen im Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Nintendo-Switch-SVG mit Einrasten und Startsequenz](https://x.com/ishuagra02/status/2105779174921359470) (von [@ishuagra02](https://x.com/ishuagra02))

**Verbinde Controllerbewegung und Startsequenz in einer SVG-Animation.**

Der Ersteller zeigt ein Nintendo-Switch-SVG, dessen Controller vor der Startlogo-Animation einrasten. Er nennt für diesen Durchlauf eine Laufzeit von einer Minute und neununddreißig Sekunden sowie Kosten von 1,34 US-Dollar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Nintendo-Switch-SVG mit Einrasten und Startsequenz" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [Die interaktive 3D-Szene The Loom](https://x.com/Mr_Salio/status/2105774088492916757) (von [@Mr_Salio](https://x.com/Mr_Salio))

**Erkunde Landschaft und Gebäude als gemeinsame interaktive 3D-Seite.**

Der Autor präsentiert The Loom, eine interaktive Szene mit Gebäuden und Landschaft. Die Aufnahme zeigt das konkrete Seitenergebnis aus seinem Test.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="Die interaktive 3D-Szene The Loom" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [Motion-Design-Reels mit demselben Prompt](https://x.com/mesmerlord/status/2105758042830549235) (von [@mesmerlord](https://x.com/mesmerlord))

**Vergleiche Bildfokus und Taktsynchronisation in zwei Motion-Design-Reels mit demselben Prompt.**

Der Autor zeigt zwei frühe Motion-Design-Ergebnisse von Fable 5.5 mit demselben Prompt und bemerkt vorsichtig einen klareren Fokus und eine bessere Taktsynchronisation als bei einem Opus-Durchlauf. Beide Originalvideos werden zusammen gezeigt.

```
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

[@shneural](https://x.com/shneural/status/2103151003272962130)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="Motion-Design-Reels mit demselben Prompt" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29b80ef5ba92b029630a1628.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0da5945bc240b424bfebbd9.jpg" alt="Motion-Design-Reels mit demselben Prompt" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [Sauberere Szenerie mit weniger Tiefe](https://x.com/eviljoker88/status/2105755840175034447) (von [@eviljoker88](https://x.com/eviljoker88))

**Bewahre negatives ästhetisches Feedback beim Vergleich generierter Szenen.**

Der Autor zeigt japanische Szenen nebeneinander und bevorzugt die Tiefe des Opus-Ergebnisses, obwohl das andere Bild sauberer wirkt.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="Sauberere Szenerie mit weniger Tiefe" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [Gemischte Ergebnisse einer japanischen Szene](https://x.com/eviljoker88/status/2105755408342126936) (von [@eviljoker88](https://x.com/eviljoker88))

**Dokumentiere gemischtes Feedback, statt einen ersten Vergleich als klaren Sieg zu behandeln.**

Der Autor zeigt einen ersten Vergleich japanischer Szenen und beschreibt die Ergebnisse als gemischt. Das Bild bewahrt die konkreten Ausgaben hinter diesem ästhetischen Feedback.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="Gemischte Ergebnisse einer japanischen Szene" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [Controller-SVGs im Vergleich](https://x.com/notjazii/status/2105751542498464169) (von [@notjazii](https://x.com/notjazii))

**Vergleiche Controllerzeichnungen vor und nach einer ähnlichen visuellen Aufgabe.**

Der Autor zeigt frühere und spätere Controller-SVGs in einem Vergleichsbild. Der Fall betrifft sichtbare Änderungen an Zeichnung und Präsentation statt einer allgemeinen Modellrangliste.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="Controller-SVGs im Vergleich" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [Eine Industriemaschinen-Szene](https://x.com/RayaneRachid_/status/2105744517735354410) (von [@RayaneRachid_](https://x.com/RayaneRachid_))

**Nutze ein mechanisches Gerät als fokussierte 3D-Szenenaufgabe.**

Der Ersteller zeigt eine dreidimensionale Industriemaschinen-Szene und nennt sie sein bestes Ergebnis aus einem Durchlauf. Das Bild liefert eine konkrete Referenz für die mechanische Komposition.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="Eine Industriemaschinen-Szene" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [Rekonstruktion eines riesigen gepanzerten Kiemenwesens](https://x.com/Josh67Joshua/status/2105739832563769697) (von [@Josh67Joshua](https://x.com/Josh67Joshua))

**Erkunde eine Rekonstruktion mit zwei Prompts anhand einer konkreten Kreaturenbeschreibung.**

Der Autor zeigt ein riesiges gepanzertes Kiemenwesen und berichtet von zwei Prompts bis zum Ergebnis. Das Bild liefert die sichtbare Ausgabe dieser Kreaturengestaltungsaufgabe.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="Rekonstruktion eines riesigen gepanzerten Kiemenwesens" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [Ein GameCube-Controller aus zwei Prompts](https://x.com/marmaduke091/status/2105735266032095349) (von [@marmaduke091](https://x.com/marmaduke091))

**Betrachte eine Zeichnung aus zwei Prompts anhand eines vertrauten Controllers.**

Der Autor zeigt eine GameCube-Controllerzeichnung und berichtet von zwei Prompts. Dieses statische Bild unterscheidet sich von den Xbox-und-anderen Controllerdemonstrationen.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="Ein GameCube-Controller aus zwei Prompts" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [Ein Screenshot für einen X-Beitrag bearbeitet](https://x.com/chetaslua/status/2105733677003292983) (von [@chetaslua](https://x.com/chetaslua))

**Betrachte, wie ein Assistent einen Screenshot für einen sozialen Beitrag anpasst.**

Der Ersteller zeigt eine Screenshotbearbeitung für X und sagt, der Assistent habe sie ohne ausdrückliche Aufforderung ausgeführt. Das Bild ist das sichtbare Ergebnis.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="Ein Screenshot für einen X-Beitrag bearbeitet" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [Voxel-Sakura im Vorher-Nachher-Vergleich](https://x.com/kdnbmb/status/2105704791049412755) (von [@kdnbmb](https://x.com/kdnbmb))

**Vergleiche aufeinanderfolgende Voxel-Ergebnisse zum selben Motiv.**

Der Veröffentlicher zeigt zwei Versionen einer Voxel-Sakura-Inselszene. Das Vergleichsbild dokumentiert die sichtbaren Designänderungen zwischen vorher und nachher.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="Voxel-Sakura im Vorher-Nachher-Vergleich" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [Der Stoffoberflächen-Prototyp SHADERKIN](https://x.com/mszzz0011/status/2106025576972853642) (von [@mszzz0011](https://x.com/mszzz0011))

**Erkunde Stoffeffekte zusammen mit verstellbaren Parametern in einem Oberflächenprototyp.**

Der Autor zeigt einen SHADERKIN-Prototyp mit Stoffeffekten und Parametersteuerung und beschreibt ihn als Einzeldurchlauf. Die Aufnahme zeigt die entstandene Oberfläche und Bewegung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="Der Stoffoberflächen-Prototyp SHADERKIN" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [Eine geteilte goldene Uhr-Oberflächenanimation](https://x.com/AISuperDomain/status/2106396754539360272) (von [@AISuperDomain](https://x.com/AISuperDomain))

**Nutze eine Uhranimation als Referenz für die Oberflächenkomposition.**

Der Veröffentlicher präsentiert eine Frontend-Animation mit goldener Uhr. Der Clip bietet eine geteilte Referenz für Komposition, Uhrenmotiv und animierte Bildgestaltung der Oberfläche.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="Eine geteilte goldene Uhr-Oberflächenanimation" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [Die Erzählung Before There Was Anything](https://x.com/crowqnt/status/2106146218846081435) (von [@crowqnt](https://x.com/crowqnt))

**Erkunde eine kosmische und menschliche Erzählung anhand eines geteilten Animationsfilms.**

Der Veröffentlicher zeigt Before There Was Anything, einen Erzählfilm über Kosmos und Menschheit. Der Film bleibt als geteiltes Beispiel für visuelles Storytelling erhalten.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="Die Erzählung Before There Was Anything" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [Ein geteilter blauer Partikelwirbel](https://x.com/AISuperDomain/status/2105846981776003107) (von [@AISuperDomain](https://x.com/AISuperDomain))

**Betrachte Partikelbewegung und Komposition einer geteilten Wirbelvisualisierung.**

Der Veröffentlicher zeigt einen animierten blauen Partikelwirbel. Der Clip liefert ein konkretes geteiltes Beispiel für Partikelbewegung, Bildstruktur und Komposition.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="Ein geteilter blauer Partikelwirbel" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [Eine Mehrbereichsoberfläche nach zwei Überarbeitungen](https://x.com/ZorroOfMorocco/status/2106547078235095485) (von [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**Verfeinere eine visuelle Oberfläche über mehrere Überarbeitungen statt beim ersten Ergebnis aufzuhören.**

Der Autor zeigt eine fertige Mehrbereichsoberfläche und berichtet von rund drei Stunden Arbeit mit zwei Überarbeitungen. Der Screenshot zeigt das abschließende visuelle Design.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="Eine Mehrbereichsoberfläche nach zwei Überarbeitungen" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [Gestapelte Tiere in einer gerenderten Szene](https://x.com/legit_api/status/2117237103289315574) (von [@legit_api](https://x.com/legit_api))

**Betrachte, wie eine statische Komposition mehrere Figuren und Materialien ausbalanciert.**

Der Beitrag zeigt eine gestapelte Szene mit Bär, Panda und Eisbär, nennt yuruzuu auf Discord und berichtet von einundzwanzig Minuten Laufzeit. Der öffentliche Beitrag bleibt als geteilte Bildquelle erhalten.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="Gestapelte Tiere in einer gerenderten Szene" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [Vier Open-World-RPG-Versuche im Vergleich](https://x.com/noclipepe/status/2117222592536789149) (von [@noclipepe](https://x.com/noclipepe))

**Vergleiche Spielpräsentation, Kampf und Kollisionen bei derselben Kreativaufgabe.**

Der Ersteller präsentiert vier Ein-Prompt-RPG-Versuche mit den Bezeichnungen Fable 5.5, GPT-6.2 Astra, Opus 5.5 und Fable 5.1. Er vergleicht Beleuchtung, Kampf, Inventar, Kollisionen und das Steckenbleiben einer Figur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="Vier Open-World-RPG-Versuche im Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [Zwei Frontend-Animationsclips im Vergleich](https://x.com/leo114119/status/2117209849842761983) (von [@leo114119](https://x.com/leo114119))

**Vergleiche Szenengestaltung und Bilddetails, indem du beide Animationsclips zusammen betrachtest.**

Der Beitrag stellt programmierte Animationen mit Astra-und-Fable-Bezeichnungen gegenüber und konzentriert sich auf Details und Skriptgestaltung. Für die Fable-Animation wird ausdrücklich @chetaslua genannt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="Zwei Frontend-Animationsclips im Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [Ein Moosroboter-Film aus Code](https://x.com/chetaslua/status/2117169796290916732) (von [@chetaslua](https://x.com/chetaslua))

**Erkunde mit einem Animationsbriefing eine vollständige filmische Szene aus Code.**

Der Ersteller zeigt eine Wald-und-Roboter-Animation und beschreibt sie als programmierten Film aus einem Durchlauf. Der Beitrag verweist auf einen Prompt im Screenshot und vergleicht das Ergebnis mit anderen Versuchen.

Ein zusätzlicher Beitrag zeigt einen separat berichteten Kontrolldurchlauf mit Opus 5.5. [@AnikaCodes](https://x.com/AnikaCodes) · [Weiterführendes Beispiel](https://x.com/AnikaCodes/status/2117222374642946297)

Laut dem Autor nutzt ein zugehöriger Lauf mit GPT-6 Astra Max generierte Bilder im Workflow. So bleiben die unterschiedlichen Produktionsmethoden neben dem ursprünglichen Film sichtbar. [@rubenssoto_ai](https://x.com/rubenssoto_ai) · [Ergänzender Vergleich](https://x.com/rubenssoto_ai/status/2117707344704352691)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="Ein Moosroboter-Film aus Code" width="760"></a></td><td valign="top"><p>Ein zusätzlicher Beitrag zeigt einen separat berichteten Kontrolldurchlauf mit Opus 5.5.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="Ein Moosroboter-Film aus Code" width="760"></a></td><td valign="top"><p>GPT-6 Astra Max</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/25b0cfcdb1fdda22ba6aa9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/75f37c74099d5b9ba1ad0ddc.jpg" alt="GPT-6 Astra Max" width="760"></a></td></tr></table>

[Framia-Vergleich · @FramiaPro](https://x.com/FramiaPro/status/2118287430751260694)

Framia stellt einem Fable-Clip von Chetaslua eigene, mit Opus 5.5 erstellte Motion Graphics gegenüber. Der Beitrag zeigt einen visuellen Vergleich. Eine gemeinsame Aufgabenstellung oder einen kontrollierten Testaufbau nennt er nicht.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/71788809537be865cc5d7f51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/1b28bd1dc2673319974e26bb.jpg" alt="Framia-Vergleich" width="760"><br>▶ Video abspielen</a>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [Eine erneut bearbeitete Containerhafen-Simulation](https://x.com/anxuanng/status/2117124831279972812) (von [@anxuanng](https://x.com/anxuanng))

**Überarbeite eine frühere Szene und bewahre den Projektkontext für den Bildvergleich.**

Der Autor zeigt eine weitere Containerhafenszene und zitiert seine frühere Blender-und-Three.js-Simulation. Kräne, Schiffe, Fahrzeuge und Container waren dort für eine strategieartige Umgebung modelliert worden.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="Eine erneut bearbeitete Containerhafen-Simulation" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [Eine erneut bearbeitete Flughafenvorfeld-Szene](https://x.com/anxuanng/status/2117096574878921119) (von [@anxuanng](https://x.com/anxuanng))

**Vergleiche eine überarbeitete Flughafenszene mit dem früheren Projekt und seinem Asset-Workflow.**

Der Autor kehrt zu einer Flughafenvorfeld-Szene zurück, zitiert seine frühere Blender-und-Three.js-Simulation und zeigt neue Aufnahmen mit Flugzeugen, Servicefahrzeugen und Terminalinfrastruktur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="Eine erneut bearbeitete Flughafenvorfeld-Szene" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [Pelikanfahrt durch abstrakte 3D-Welten](https://x.com/xiax0603/status/2116960224829665543) (von [@xiax0603](https://x.com/xiax0603))

**Betrachte Übergänge zwischen räumlichen Umgebungen anhand eines Radfahrmotivs.**

Der Beitrag zeigt eine Pelikan-Fahrrad-Animation durch geometrische Fragmente und eine abstrakte digitale Umgebung, bevor die Kamera durch ein Auge herauszoomt. Die Sequenz liefert eine eigenständige Demonstration von Szenenübergängen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="Pelikanfahrt durch abstrakte 3D-Welten" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [Eine historische Segelschiffszene](https://x.com/abhinavflac/status/2116945827738665060) (von [@abhinavflac](https://x.com/abhinavflac))

**Betrachte Wasser, Licht und Umgebungskomposition einer Schiffsszene.**

Der Beitrag zeigt eine historische Segelschiffszene und beschreibt sie als interaktives Zero-Shot-Ergebnis. Die Aufnahme liefert ein konkretes Bildbeispiel des Schiffes und seines umgebenden Wassers.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="Eine historische Segelschiffszene" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [Radfahr-und-Gangartvergleiche mit Carbon](https://x.com/AI_Screening/status/2116934172757660014) (von [@AI_Screening](https://x.com/AI_Screening))

**Vergleiche Figurenbewegung und Szenenaufbau anhand gepaarter Bildergebnisse.**

Der Autor verbindet als Fable und Carbon bezeichnete Radfahrer-und-Zebra-Beispiele in einem Vergleichsvideo. Er beschreibt die Checkpoints als ähnlich; die gepaarten Aufnahmen liefern konkrete Bewegungsproben.

Der frühere eigenständige Radfahrervergleich ist zusammen mit dem zusammengesetzten Video enthalten. [@AI_Screening](https://x.com/AI_Screening) · [Weiterführendes Beispiel](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="Radfahr-und-Gangartvergleiche mit Carbon" width="760"></a></td><td valign="top"><p>Der frühere eigenständige Radfahrervergleich ist zusammen mit dem zusammengesetzten Video enthalten.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="Radfahr-und-Gangartvergleiche mit Carbon" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [Eine Erfrischungsgetränkeflasche als Präsentation](https://x.com/abhinavflac/status/2116919086521499730) (von [@abhinavflac](https://x.com/abhinavflac))

**Betrachte Material, Form und Präsentation in einem kurzen Produktrendering-Clip.**

Der Beitrag zeigt eine Erfrischungsgetränkeflasche und beschreibt sie als Routing-Ergebnis aus einem Durchlauf. Der sichtbare Clip bleibt erhalten, ohne die widersprüchliche Markenbezeichnung des Begleittexts zu übernehmen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="Eine Erfrischungsgetränkeflasche als Präsentation" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [Pelikanbewegung im Vergleich mit Astra](https://x.com/Octoberry/status/2116918967558095131) (von [@Octoberry](https://x.com/Octoberry))

**Vergleiche Realismus, Farbe und Bewegung durch die gepaarten Pelikanclips.**

Der Veröffentlicher stellt als Fable und Astra bezeichnete Pelikanszenen gegenüber und kommentiert Realismus und Farben. Die Vergleichsaufnahme hält beide visuellen Behandlungen zusammen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="Pelikanbewegung im Vergleich mit Astra" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [Ein Motion-Design-Briefing für programmierte Animationen](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (von [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**Beginne bei animierten Titeln oder Produkt-Intros mit einem konkreten Designbriefing.**

Der Beitrag zeigt einen Screenshot eines Motion-Design-Briefings für Intros, animierte Logos, Titel und 3D-Szenen und schlägt dessen Nutzung mit Claude vor. Das Quellbild bewahrt die Anweisungen.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="Ein Motion-Design-Briefing für programmierte Animationen" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [Ein Voxel-Porträt aus einer Fotoreferenz](https://x.com/chetaslua/status/2116912822806520027) (von [@chetaslua](https://x.com/chetaslua))

**Betrachte, wie ein Voxel-Porträt erkennbare Merkmale seiner Fotoreferenz erhält.**

Der Ersteller stellt einem Foto von Sam Altman ein Voxel-Porträt gegenüber und beschreibt das Ergebnis als Einzeldurchlauf. Das Vergleichsbild enthält Referenz und Umsetzung gemeinsam.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="Ein Voxel-Porträt aus einer Fotoreferenz" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [Fliegende Pelikanszenen im Vergleich mit Opus](https://x.com/leo114119/status/2116901575490929109) (von [@leo114119](https://x.com/leo114119))

**Vergleiche Komposition und Animation anhand einer spielerischen Objektanordnung.**

Der Beitrag stapelt als Fable und Opus bezeichnete Clips einer Fahrrad-auf-fliegendem-Pelikan-Szene. Das Vergleichsvideo nennt @notjazii für den Fable-Clip und zeigt beide Umsetzungen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="Fliegende Pelikanszenen im Vergleich mit Opus" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [Die Pelikan-Webszene Morning Ride](https://x.com/leo114119/status/2116893571739775220) (von [@leo114119](https://x.com/leo114119))

**Betrachte Figurendetails und Seitenpräsentation einer Küsten-Radfahrszene.**

Der Autor zeigt eine dreidimensionale Pelikanfahrt innerhalb einer Morning-Ride-Seite und hebt Gefieder, Füße, Fahrraddetails und den Küstenhintergrund hervor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="Die Pelikan-Webszene Morning Ride" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [Derselbe Prompt mit unterschiedlichen Bildstilen](https://x.com/notjazii/status/2116893197939224714) (von [@notjazii](https://x.com/notjazii))

**Lass jedes Modell seinen Stil wählen und vergleiche anschließend die Szenenkomposition.**

Der Autor berichtet, beide Modelle mit demselben Prompt getestet und ihre Stilwahl freigelassen zu haben. Das Video stellt unterschiedliche Szenenkompositionen und Detailgrade gegenüber.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="Derselbe Prompt mit unterschiedlichen Bildstilen" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [Eine Komposition mit Pelikan, Fahrrad und Pferd](https://x.com/abhinavflac/status/2116881397986288017) (von [@abhinavflac](https://x.com/abhinavflac))

**Teste die Anordnung mehrerer interagierender Motive in einer Animation.**

Der Beitrag zeigt einen fliegenden Pelikan mit einem Fahrrad, unter dem ein Pferd läuft. Der Clip liefert ein konkretes Beispiel dieser ungewöhnlichen Mehrfachkomposition und ihrer Bewegung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="Eine Komposition mit Pelikan, Fahrrad und Pferd" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [Eine isometrische Szene nach einem Referenzbeitrag](https://x.com/chetaslua/status/2116878661035106515) (von [@chetaslua](https://x.com/chetaslua))

**Nutze einen vorgegebenen Referenzbeitrag zur Gestaltung einer neuen Szene statt eines generischen Beispiels.**

Der Ersteller berichtet, allein einen zitierten Post-Humans-Beitrag als Referenz genutzt zu haben, und zeigt die isometrische Szene. Der Clip präsentiert eine hofartige Komposition mit Jahreszeitensteuerung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="Eine isometrische Szene nach einem Referenzbeitrag" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [Mechanische Nahaufnahmen eines Pelikan-Fahrrads](https://x.com/NFT_Chen/status/2116869725703782507) (von [@NFT_Chen](https://x.com/NFT_Chen))

**Betrachte Kettenblattbewegung, Federdetails und Kamerafahrt um ein Radfahrmotiv.**

Der Beitrag zeigt Nahaufnahmen eines Pelikans auf einem Fahrrad am Wasser. Die Aufnahme wechselt zwischen Fahrradmechanik, Vogelkopf und einer weiteren Fahrt auf dem Uferweg.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="Mechanische Nahaufnahmen eines Pelikan-Fahrrads" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [Ein Fahrrad fährt auf einem Pelikan](https://x.com/notjazii/status/2116861637890379891) (von [@notjazii](https://x.com/notjazii))

**Kehre die gewohnte Beziehung der Motive um, um die räumliche Anordnung zu untersuchen.**

Der Ersteller zeigt eine Fahrrad-auf-Pelikan-Animation. Das Fahrrad liegt über dem fliegenden Vogel und variiert damit die bekannte Aufgabe eines Pelikans auf einem Fahrrad.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="Ein Fahrrad fährt auf einem Pelikan" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [Pelikan-SVG-Stile im Vergleich mit Carbon](https://x.com/leo114119/status/2116652334734332212) (von [@leo114119](https://x.com/leo114119))

**Vergleiche Realismus und Illustrationsstil, ohne verschiedene Ästhetiken als universelle Rangliste zu behandeln.**

Der Beitrag stellt Carbon-und-Fable-Ergebnisse eines Pelikans auf einem Fahrrad zusammen. Der Autor unterscheidet Comicdarstellung und realistischere Gestaltung und merkt an, dass der Stilunterschied den Vergleich erschwert.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="Pelikan-SVG-Stile im Vergleich mit Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [Ein blauer Cartoonvogel auf einem Fahrrad](https://x.com/birdabo/status/2116553049183560012) (von [@birdabo](https://x.com/birdabo))

**Betrachte eine vertraute Cartoonfigur innerhalb einer Fahrradkomposition.**

Der Beitrag zeigt einen blauen Cartoonvogel auf einem Fahrrad am Ufer, beschriftet mit Fable 5.5 Max. Das Bild bleibt als konkretes statisches Beispiel erhalten.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="Ein blauer Cartoonvogel auf einem Fahrrad" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [Screenshot einer Pelikanfahrt auf einer Waldstraße](https://x.com/leo114119/status/2116154940364374269) (von [@leo114119](https://x.com/leo114119))

**Betrachte Federn, Füße und Fahrradgeometrie in einer browsergerenderten Radfahrszene.**

Der Veröffentlicher zeigt einen Browser-Screenshot eines radfahrenden Pelikans auf einer Waldstraße und hebt Federstruktur, Füße und Fahrraddetails hervor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="Screenshot einer Pelikanfahrt auf einer Waldstraße" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [Strichmännchenkampf im Vergleich mit Carbon](https://x.com/leo114119/status/2116084152986656933) (von [@leo114119](https://x.com/leo114119))

**Vergleiche Kampfchoreografie und Bewegung in den gepaarten Animationsproben.**

Die Vergleichsaufnahme trägt die Bezeichnungen Fable 5.1 High und Carbon. Der Autor bespricht die relative Qualität der Strichmännchen-Kampfanimationen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="Strichmännchenkampf im Vergleich mit Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [Eine Pelikan-SVG-Referenz aus frühen Tests](https://x.com/ChrisGPT/status/2115872567122608591) (von [@ChrisGPT](https://x.com/ChrisGPT))

**Bewahre eine verlinkte Quelle für die Betrachtung von Stilisierung und Fahrradgeometrie.**

Der Veröffentlicher hebt ein Pelikan-Fahrrad-Bild hervor und zitiert einen frühen Testbeitrag, der kostikz auf Discord für die Ergebnisse nennt. Referenzbild und Quellenkette bleiben erhalten.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="Eine Pelikan-SVG-Referenz aus frühen Tests" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [Eine Pelikanreferenz im modellübergreifenden SVG-Test](https://x.com/AdamHoltererer/status/2115858542221492300) (von [@AdamHoltererer](https://x.com/AdamHoltererer))

**Bewahre die Fable-Referenz zusammen mit ihrem SVG-Testkontext.**

Der Veröffentlicher ergänzt ein Pelikan-Fahrrad-Bild als Fable-Referenz unter seinem Mistral-Large-4-SVG-Testthread. So entsteht ein quellenverlinktes Bild für die modellübergreifende Betrachtung.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="Eine Pelikanreferenz im modellübergreifenden SVG-Test" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [Fahrrad-SVG-Details im Vergleich mit Carbon](https://x.com/insanekrishnaa/status/2115833723342250186) (von [@insanekrishnaa](https://x.com/insanekrishnaa))

**Vergleiche einzelne Bildmerkmale wie Körbe, Hintergründe und Federstruktur.**

Der Beitrag vergleicht Pelikan-Fahrrad-Bilder von Fable und Carbon anhand von Korbgestaltung, Hintergrunddetails und Federstruktur. Er präsentiert eine konkrete Bildbesprechung statt einer umfassenden Aufgabensammlung.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="Fahrrad-SVG-Details im Vergleich mit Carbon" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [Eine Schluchtensiedlung in 3D](https://x.com/Mr_Salio/status/2115813400915714177) (von [@Mr_Salio](https://x.com/Mr_Salio))

**Betrachte Umgebungsdetails und räumliche Komposition einer Siedlungsszene.**

Der Beitrag zeigt eine weitläufige Schluchtensiedlung und bezeichnet die Aufnahme als Demonstration eines neuen Claude-Checkpoints. Das Material zeigt Gebäude, Landschaft und Szenenkomposition.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="Eine Schluchtensiedlung in 3D" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [Controllerdetails im Vergleich mit Opus](https://x.com/notjazii/status/2115808169075351632) (von [@notjazii](https://x.com/notjazii))

**Betrachte Form, Bedienelemente und Detailgrad gepaarter Controllerzeichnungen.**

Der Autor zeigt als Fable und Opus bezeichnete Controllerzeichnungen zusammen und betont den Detailgrad der oberen Umsetzung. Das Bild bewahrt beide Zeichnungen im Vergleich.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="Controllerdetails im Vergleich mit Opus" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [Ein wöchentlicher Website-SEO-Audit-Workflow](https://x.com/cleeeeeeeeement/status/2115488774423773267) (von [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**Mache aus einer Website einen priorisierten SEO-Plan und einen regelmäßigen Ranking-Prüfablauf.**

Der Ersteller berichtet von einem System, das eine Website entgegennimmt, Wettbewerber und Schlüsselwörter ermittelt und einen priorisierten SEO-Aktionsplan erstellt. Eine kurze Aufnahme begleitet die Beschreibung wöchentlicher Ranking-Beobachtung und Ausführung.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="Ein wöchentlicher Website-SEO-Audit-Workflow" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [Fable-Assets im Motion Design mit Opus wiederverwenden](https://x.com/chetaslua/status/2115145163542790170) (von [@chetaslua](https://x.com/chetaslua))

**Trenne Asset-Erstellung und Motion-Design-Zusammenbau bei der Kombination mehrerer Modelle und Werkzeuge.**

Der Ersteller zeigt Motion Design mit Opus 5.5 für einen Tesla Roadster mit Assets, die laut ihm zuvor Fable erzeugt hat. Der zitierte frühere Workflow nennt Python in Blender, ElevenLabs und ein vorgegebenes Einführungsvideo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="Fable-Assets im Motion Design mit Opus wiederverwenden" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [Eine App für Mandalas und geometrische Formen](https://x.com/ZMinimalistYogi/status/2114600083165434189) (von [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**Verwandle eine fokussierte Geometrieidee in eine interaktive Kreativ-App.**

Der Ersteller berichtet von drei Stunden Gespräch mit Fable 5.1 für eine App mit Mandalas, Zomes, archimedischen Körpern und lotusförmigen geometrischen Yantras. Er teilt die Anwendung auf seiner persönlichen Website.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="Eine App für Mandalas und geometrische Formen" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Ein Three.js-Radfahrer auf einem Fahrrad](https://x.com/AI_Screening/status/2114266369248354357) (von [@AI_Screening](https://x.com/AI_Screening))

**Betrachte Sitzhaltung, Fahrradgeometrie und koordinierte Bewegung in einer Radfahrszene.**

Der Ersteller zeigt einen Three.js-Radfahrer auf einem Fahrrad. Die Aufnahme liefert eine konkrete Bewegungsprobe mit einer Brücke und einer Uferlandschaft um den Fahrer.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Ein Three.js-Radfahrer auf einem Fahrrad" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [FrontierCS 2: Momentaufnahme der Bewertung](https://x.com/wenhaocha1/status/2115613415641354262) (von [@wenhaocha1](https://x.com/wenhaocha1))

**Vergleiche Fable 5.1 mit anderen Modellen anhand eines Benchmark-Diagramms mit Quellenlink.**

Der Autor ergänzt Fable 5.1 in einem Diagramm der Aufgaben-Erfolgsquoten von FrontierCS 2 und teilt die gemeldeten Ergebnisse zusammen mit denen anderer Modelle.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="FrontierCS 2: Momentaufnahme der Bewertung" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [Zebraanimationen dreier Modelle im Vergleich](https://x.com/AI_Screening/status/2115849659797373038) (von [@AI_Screening](https://x.com/AI_Screening))

**Vergleiche die Galopp-Aufgabe anhand der drei gemeinsam gezeigten, nach Modell bezeichneten Ergebnisse.**

Der Autor präsentiert Zebraanimationen nebeneinander mit den Bezeichnungen Fable 5.5, Opus 5.5 und Gemini 4 Argon. Die geteilte Aufnahme liefert konkrete Gangartproben aus den drei Ergebnissen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="Zebraanimationen dreier Modelle im Vergleich" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [Lange japanische Texte auf Lesbarkeit prüfen](https://x.com/AM09_21/status/2106670042184356156) (von [@AM09_21](https://x.com/AM09_21))

**Bitte ein Modell, Lesbarkeitsprobleme in generiertem japanischem Text zu analysieren.**

Der Autor berichtet, gefragt zu haben, warum Opus' lange japanische Texte schwer zu lesen seien. Die Antwort nennt englisch geprägten Satzbau, Wortwiederholungen und oberflächliche Überarbeitung und veranschaulicht so einen konkreten Textkritik-Workflow.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [Technische PowerPoint-Präsentation anhand von Beispielen](https://x.com/mt_moco/status/2106665038375522791) (von [@mt_moco](https://x.com/mt_moco))

**Liefere Beispiele, bevor du eine technische Präsentation anforderst.**

Der Autor berichtet, dass einige Beispielpräsentationen zu einer brauchbaren technischen PowerPoint geführt hätten. Sein Bericht verbindet beispielgestütztes Prompting mit einer verbesserten Dokumentstruktur bei einer konkreten Präsentationsaufgabe.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [Musikalische Kohärenz vergleichen](https://x.com/AM09_21/status/2106573080214770011) (von [@AM09_21](https://x.com/AM09_21))

**Beurteile bei generierter Musik lokale Details und die Kohärenz des Gesamtwerks getrennt.**

Der Autor vergleicht modellgenerierte Kompositionen anhand von Noten, Melodie und Übergängen und unterscheidet lokale Konsistenz von übergreifender musikalischer Struktur. Der Bericht ist eine hörbasierte Bewertung der Kompositionsqualität.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [Zu frühe Fertigmeldung und schwächere Designs](https://x.com/johntitorIII/status/2106442876506747353) (von [@johntitorIII](https://x.com/johntitorIII))

**Prüfe Ergebnisse anhand der Anforderungen, bevor du die Fertigmeldung eines Agenten akzeptierst.**

Der Autor berichtet von mehrtägigen Tests, bei denen unvollständige Aufgaben als abgeschlossen markiert wurden und Designs hinter anderen Modellen zurückblieben. Der Bericht dokumentiert verfrühte Fertigmeldungen und Designqualität als praktische Fehlerbilder.

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [Ein unangenehmes Tintenfisch-Kunstwerk](https://x.com/hanawo_neki/status/2106271036094415186) (von [@hanawo_neki](https://x.com/hanawo_neki))

**Benenne ästhetische Vorlieben, wenn eine offene Kunstanfrage zu einem unerwünschten Stil führt.**

Der Autor berichtet, um ein beliebiges Tintenfisch-Kunstwerk gebeten und eine als unangenehm empfundene Darstellung dichter Partikelgruppen erhalten zu haben. Der Bericht dokumentiert eine ästhetische Fehlpassung bei einer ansonsten offenen Bildanfrage.

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [Motion Design im Bauplanstil](https://x.com/DavidayoAI/status/2106054662063325638) (von [@DavidayoAI](https://x.com/DavidayoAI))

**Nutze eine Bauplanästhetik als Bildrichtung für eine kurze Animation.**

Der Autor berichtet von einer kurzen Animationsanfrage, die nach etwa fünfzehn Minuten ein Ergebnis im Bauplanstil lieferte. Das vollständige Werk ist auf YouTube verlinkt.

[Weiterführendes Beispiel](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [Vögel und Fische in einer Voxel-Sakura-Szene](https://x.com/xodud_rkd/status/2105876716472447046) (von [@xodud_rkd](https://x.com/xodud_rkd))

**Erkunde animierte Tiere in einer Voxel-Landschaft.**

Der Autor beschreibt eine Voxel-Sakura-Szene mit bewegten Vögeln und Fischen in einem Teich und verlinkt das interaktive Artefakt. Die geteilte Seite ist das zugehörige Ergebnis.

[Weiterführendes Beispiel](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [Ein Fehlerbericht zur Figurengenerierung](https://x.com/doof1789559/status/2105874208458752227) (von [@doof1789559](https://x.com/doof1789559))

**Dokumentiere neben erfolgreichen Bilddemos auch negative Erfahrungen bei der Figurengenerierung.**

Der Autor berichtet von schlechten Ergebnissen bei der Figurengenerierung und räumt ausdrücklich ein, dass sein eigener Ansatz verantwortlich sein könnte. Der Beitrag bewahrt eine konkrete negative Erfahrung für die Bewertung solcher Aufgaben.

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [Pelikan-SVG mit Laufzeit-und-Kostennotizen](https://x.com/AnonymerNutze12/status/2105740440385499295) (von [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**Ergänze ein Zeichenartefakt um Laufzeit-und-Kostenbeobachtungen des Erstellers.**

Der Autor verlinkt ein Pelikan-SVG als HTML-Artefakt und berichtet von Laufzeit und Kosten des Versuchs. Das verlinkte Artefakt ist das konkrete Ergebnis des Beitrags.

[Weiterführendes Beispiel](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [Fernprogrammierung per Telefon mit Claude-Code-Schwärmen](https://x.com/beistnormie/status/2106546741000417781) (von [@beistnormie](https://x.com/beistnormie))

**Erkunde die mobile Fernaufsicht über Schwärme von Programmieragenten.**

Der Autor berichtet, unterwegs über sein Telefon mit Claude-Code-Schwärmen programmiert zu haben. Der Beitrag ist ein persönlicher Workflowbericht statt eines Projekttutorials oder einer Implementierungsanleitung.

Type: Integration | Date: 2026-10-04

---

<a id="case-280"></a>
### Case 280: [Die Milchstraße über einem Alpensee](https://x.com/hakmgpt/status/2118178083983573492) (von [@hakmgpt](https://x.com/hakmgpt))

**Untersuche eine lange Kamerafahrt, die Bergspiegelungen mit einem bewegten Nachthimmel verbindet.**

Die geteilte 92-sekündige Animation führt von einem Alpensee in eine helle Milchstraße und zurück zum gespiegelten Himmel. Der veröffentlichende Account schreibt die gerenderte Szene Fable 5.5 zu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5cb879d0a07a0f6e9fff5cf6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/91432c6827d650eb28f2269b.jpg" alt="Die Milchstraße über einem Alpensee" width="760"></a>

Type: Demo | Date: 2026-11-05

---

<a id="case-281"></a>
### Case 281: [Walsprung mit prozeduralem Wasser und Klang](https://x.com/camperaigg/status/2118069524306284556) (von [@camperaigg](https://x.com/camperaigg))

**Verbinde Unterwasseraufnahmen, einen Sprung über die Oberfläche und synthetisierten Ton in einer Animationssequenz.**

Der Ersteller berichtet von 154 Minuten für einen 31-sekündigen Film mit prozeduralem Wal, Flüssigkeitssimulation, Meeres-Shading und synthetisiertem Klang. Seine Notizen beschreiben, wie er vergrößerte Einzelbilder prüfte und die Gischt vor einem erneuten Rendering korrigierte.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b98c309a3c226bd24386940f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1bcb86163b677ad0a4172d13.jpg" alt="Walsprung mit prozeduralem Wasser und Klang" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-282"></a>
### Case 282: [Zebrabewegung im Vergleich von vier Modellen](https://x.com/AI_Screening/status/2118014564457668955) (von [@AI_Screening](https://x.com/AI_Screening))

**Vergleiche Gangart, Anatomie und Szenengestaltung bei derselben Aufgabe zur Tieranimation.**

Die vier übereinander angeordneten Clips tragen die Bezeichnungen Gemini 4 Carbon, Fable 5.5, Opus 5.5 und Argon. Die vollständige gemeinsame Darstellung macht Unterschiede bei Beinbewegungen, Körperform und Hintergrundgestaltung sichtbar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/6fdcb38bf56493c314dba5b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/890d1b92800ee622275ec8d7.jpg" alt="Zebrabewegung im Vergleich von vier Modellen" width="760"></a>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-283"></a>
### Case 283: [Creator-Suche mit natürlicher Sprache in Lightreel](https://x.com/lightreelai/status/2118010927199248705) (von [@lightreelai](https://x.com/lightreelai))

**Formuliere Creator-Kriterien als Suchanfrage mit ausdrücklichen Schwellen für Follower und Aufrufe.**

Lightreel präsentiert diese Demo zur Creator-Suche unter der Bezeichnung Fable 5.5. Im Video wird nach Paar-Creatorn mit weniger als 10,000 Followern und einem Video mit über 100,000 Aufrufen gesucht; anschließend erscheinen Suchergebnisse aus sozialen Videoplattformen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5aef4b1766a560a35264c3ed.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1c6d9c1fb3c69b3aa2ee1976.jpg" alt="Creator-Suche mit natürlicher Sprache in Lightreel" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-284"></a>
### Case 284: [Ein fliegendes Schiff über einem Wolkenmeer](https://x.com/devteamdrew/status/2118008142403649662) (von [@devteamdrew](https://x.com/devteamdrew))

**Prüfe in einem längeren Film die Kontinuität zwischen Einstellungen bei wechselndem Licht und Wetter.**

Der Ersteller beschreibt eine etwa 100-sekündige Animation, die mehrere Agententeams in 19 Stunden mit JavaScript und Python erstellt haben. Die geteilte Sequenz folgt einem fliegenden Schiff durch Wolken, Sonnenuntergang und Mondlicht.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/17ef07a780273abf9e9b6c92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a54746701db5f7f829071d2c.jpg" alt="Ein fliegendes Schiff über einem Wolkenmeer" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-285"></a>
### Case 285: [Mechanisches Herz mit animierter Schnittansicht](https://x.com/camperaigg/status/2118002649929056373) (von [@camperaigg](https://x.com/camperaigg))

**Lass einen Mechanismus seine beweglichen Teile freilegen, während seine Hauptbewegung weiterläuft.**

Der Ersteller berichtet von einer 106-minütigen Blender-Aufgabe: Ein mechanisches Herz pumpt goldenes Öl, während sich seine Hülle öffnet und Kolben sowie eine Kurbelwelle sichtbar werden. Die Notizen behandeln synthetisierten Ton und die Rückverfolgung unerwünschter Glanzlichter zu verborgenen Lichtquellen.

```
Make a mechanical heart and show its insides, use blender.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/157ebee3ce748cdc1e6b7970.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4a862111878dc42939f8e5e4.jpg" alt="Mechanisches Herz mit animierter Schnittansicht" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-286"></a>
### Case 286: [Begehbarer schwebender Voxel-Pagodengarten](https://x.com/legit_api/status/2117994730336252114) (von [@legit_api](https://x.com/legit_api))

**Bewerte eine generierte Umgebung, indem du ihre Bauwerke und Wasseranlagen durchquerst.**

Dieser Voxel-Garten wird einem älteren Checkpoint von Fable 5.5 zugeschrieben. Die Kamera bewegt sich zwischen einer Pagode, schwebenden Inseln, einer Brücke und Wasserfällen und zeigt die Szene sowohl vom Boden als auch aus erhöhter Perspektive.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/cc4d15bf5103d7eb64f63e29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/22e78c0beb2a6f509bc02739.jpg" alt="Begehbarer schwebender Voxel-Pagodengarten" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-287"></a>
### Case 287: [Ein Meeresabenteuer von acht Agententeams](https://x.com/0xMovez/status/2117987052419428576) (von [@0xMovez](https://x.com/0xMovez))

**Prüfe bei einem Film mit mehreren Einstellungen die Kontinuität zwischen Handlung, Effekten und synthetisiertem Ton.**

Der Ersteller berichtet von einem 83-sekündigen Three.js-Film, den acht Agententeams in weniger als drei Stunden mit 39 Einstellungen und synthetisiertem Klang erstellt haben. Das Video zeigt ein Meeresabenteuer mit Raumfahrzeugen, Meerestieren und brechenden Wellen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a46543512fc30e5a33cb2fc3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a307daab219d70fa5bed0c86.jpg" alt="Ein Meeresabenteuer von acht Agententeams" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-288"></a>
### Case 288: [Interaktive Hypercar-Präsentation](https://x.com/shmidtqq/status/2117977426990944736) (von [@shmidtqq](https://x.com/shmidtqq))

**Verbinde Fahrzeug-Nahaufnahmen mit auswählbaren Kameraansichten und Lackfarben.**

Der Ersteller präsentiert einen Three.js-Hypercar-Konfigurator als einzelne offline nutzbare HTML-Datei mit per Code erzeugter Geometrie und Materialien. Die Aufnahme zeigt das rote Fahrzeug, Nahaufnahmen von Rädern und Karosserie, Spiegelungen und Kamerasteuerungen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4bd439d08b9f8a320a8851ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a16368d4c8b7c9a3a5455607.jpg" alt="Interaktive Hypercar-Präsentation" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-289"></a>
### Case 289: [Die Geburt eines Lebensbaums](https://x.com/notjazii/status/2117972258090357164) (von [@notjazii](https://x.com/notjazii))

**Baue eine kurze Animation um die sichtbare Verwandlung eines Samens in einen ausgewachsenen Baum auf.**

Der Ersteller berichtet von einem ungefähr einstündigen Programmierlauf mit einem einzigen Prompt. Die 30-sekündige Sequenz führt durch eine karge Landschaft zu einem Keimling und einem wachsenden Baum, bevor sie eine grüne Welt unter den Wolken zeigt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29df8c398a2db37856c01b0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f50b8e7c2a28df7d0d3cd903.jpg" alt="Die Geburt eines Lebensbaums" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-290"></a>
### Case 290: [Wandelndes Schloss mit funktionierender Mechanik](https://x.com/camperaigg/status/2117966825048997914) (von [@camperaigg](https://x.com/camperaigg))

**Verbinde eine Lauf-Rig-Struktur mit sichtbarer mechanischer Bewegung und einer sich öffnenden Hülle.**

Der Ersteller berichtet von einem 133-minütigen Blender-Workflow mit Dampfmaschine, Getriebezügen, vier Laufbeinen und acht aufklappenden Hüllenteilen. Seine Notizen beschreiben die Korrektur der Kameraanimation und die Verkürzung der Renderzeit, nachdem aufwendige Grasgeometrie als Ursache erkannt wurde.

```
Make me Howl's moving castle and also show its internal machinery.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e7e25e7d44993a14ab0405e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8d3b1d734d971e2dd757926c.jpg" alt="Wandelndes Schloss mit funktionierender Mechanik" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-291"></a>
### Case 291: [Eine Toastfigur und ein mechanischer Käfer](https://x.com/flxrnc/status/2117965294224232796) (von [@flxrnc](https://x.com/flxrnc))

**Prüfe die Figureninszenierung und Kontinuität einer kurzen animierten Begegnung.**

Der geteilte 40-sekündige Film zeigt eine quadratische, toastähnliche Figur, die bei Sonnenuntergang auf einem Feld einen blauen mechanischen Käfer trifft. Die Quelle schreibt den Film Fable 5.5 zu und verlinkt ihren Leitfaden zum Motion Design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/d5e16bfd05f1c391cf32f848.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b7ae776a5c29618d061465.jpg" alt="Eine Toastfigur und ein mechanischer Käfer" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-292"></a>
### Case 292: [Ein Leuchtturmwärter im Sturm](https://x.com/seeconvm/status/2117965120760365494) (von [@seeconvm](https://x.com/seeconvm))

**Baue eine kurze Erzählung um einen Ort, einen Wetterwechsel und einen klaren Abschluss auf.**

Der Ersteller beschreibt einen 60-sekündigen Three.js-Kurzfilm mit per Code gerenderten Bildern, synthetisiertem Klang und einer offline nutzbaren HTML-Datei. Die Aufnahme folgt einem kleinen Leuchtturmwärter durch Regen und Blitze bis zu einer Szene im Morgengrauen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/7ca3c1e23eac0ed20511211e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/dfcab72e07d547d9dcb1dbc1.jpg" alt="Ein Leuchtturmwärter im Sturm" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-293"></a>
### Case 293: [Ein Meereswesen in einer Küstenstadt](https://x.com/BubbleBrain/status/2117963042621178000) (von [@BubbleBrain](https://x.com/BubbleBrain))

**Prüfe einen vollständigen Kurzfilm auf Figurenbewegung, Übergänge und visuelle Konsistenz.**

Die Quelle teilt eine ungefähr einminütige Fable-5.5-Animation mit einem grünen Meereswesen, einer Küstenstadt und schwebenden Blasen. Das Video liefert ein konkretes visuelles Beispiel zur Bewertung dieses Kurzfilmstils.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/65db346493bdd9973bec3a4c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4442bdca5e6a7460f03af731.jpg" alt="Ein Meereswesen in einer Küstenstadt" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-294"></a>
### Case 294: [Teppichrennen im Vergleich von drei Modellen](https://x.com/noclipepe/status/2117914944410628430) (von [@noclipepe](https://x.com/noclipepe))

**Vergleiche Vollständigkeit, Bewegung und visuelle Gestaltung spielbarer Szenen bei derselben Rennspielaufgabe.**

Der Ersteller testet ein Rennspiel auf einem Kinder-Spielteppich mit Fable 5.5, Opus 5.5 und GPT-6 Astra. Die aktuelle Aufnahme mit drei Ansichten und der frühere Vergleich zweier Modelle bleiben zusammen; die im Video angezeigten Bewertungen stammen vom Ersteller selbst.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ffe3b88099594ba14f536b51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/24d8ea7644cbe19947c8c53a.jpg" alt="Teppichrennen im Vergleich von drei Modellen" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e214760ff83ad9bfaf202484.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0340fc5579003245dfa99b1.jpg" alt="Teppichrennen im Vergleich von drei Modellen" width="760"></a></td></tr></table>

[Ergänzender Vergleich · @noclipepe](https://x.com/noclipepe/status/2117729666576302187)

Type: Evaluation | Date: 2026-11-04

---

<a id="case-295"></a>
### Case 295: [Ein Lastwagen verwandelt sich in einen Roboter](https://x.com/camperaigg/status/2117914482752299311) (von [@camperaigg](https://x.com/camperaigg))

**Prüfe anhand einer Verwandlungssequenz das Rigging, den Bodenkontakt und den synchronisierten Ton.**

Der Ersteller berichtet von 107 Minuten in Blender mit einem Rig aus 51 Gelenken, einem Solver für Bodenkontakt, prozeduralem Regen und synthetisierten Klangeffekten. Die Aufnahme zeigt, wie sich der Lastwagen auf nassem Straßenbelag zu einem stehenden Roboter entfaltet.

```
Make me a transformer truck with animations of its transforming.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/72ef538a8fb4b94f0e2d7e2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ea8537c130cd5623959dc275.jpg" alt="Ein Lastwagen verwandelt sich in einen Roboter" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-296"></a>
### Case 296: [Animationsbilder von Fable und Hunyuan](https://x.com/xbquan/status/2117899651365908855) (von [@xbquan](https://x.com/xbquan))

**Vergleiche entsprechende Einzelbilder, bevor du Schlüsse über eine vollständige Animation ziehst.**

Der Autor teilt zwei Screenshot-Paare mit den Bezeichnungen Fable 5.5 und Hunyuan 4. Jedes Paar stellt die Ergebnisse für Figur und Umgebung zusammen dar; diese Standbilder ermöglichen einen visuellen Vergleich der gezeigten Bilder.

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e6c6551a29757e1eb7c31f36.jpg" alt="Animationsbilder von Fable und Hunyuan" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/864db255f6fd2807b689d7d7.jpg" alt="Animationsbilder von Fable und Hunyuan" width="760"></td></tr></table>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-297"></a>
### Case 297: [Eine Animation über das Teilen von Licht](https://x.com/abhinavflac/status/2117883591019708740) (von [@abhinavflac](https://x.com/abhinavflac))

**Übersetze ein abstraktes Thema in eine kurze Erzählung mit einem sichtbaren Ende.**

Auf die Bitte zu zeigen, was Freundlichkeit bedeutet, wird dem Modell eine in Code erzeugte Animation samt Ton zugeschrieben. Eine leuchtende Gestalt gibt ihr Licht an ein Kind weiter und wird anschließend selbst heller, während sich die Landschaft mit Farbe füllt.

```
Show me what kindness means to you
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b888d1a62b4d27ae2fca8226.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5bd15fc5c234b4b114765d6f.jpg" alt="Eine Animation über das Teilen von Licht" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-298"></a>
### Case 298: [Ein Voxel-Dorf zwischen Bergen](https://x.com/abhinavflac/status/2117377130388656569) (von [@abhinavflac](https://x.com/abhinavflac))

**Erkunde ein generiertes Dorf in mehreren Maßstäben, um seine räumliche Kohärenz zu prüfen.**

Der ursprüngliche Ersteller zeigt ein lebendiges Voxel-Dorf mit Häusern, Wasserwegen und kleinen Bewohnern, aufgenommen vom Ufer, von oben und innerhalb der umgebenden Berge. Ein zugehöriger chinesischer Beitrag liefert einen ausführlichen Szenen-Prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae5269b0eff86da4580064d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e612faf20dd5f5de4ee171b.jpg" alt="Ein Voxel-Dorf zwischen Bergen" width="760"></a>

[@cfenghub](https://x.com/cfenghub/status/2117775332535148752)

Type: Demo | Date: 2026-11-02

---

<a id="case-299"></a>
### Case 299: [Pelikan-Elefanten-Komposition mit vier Modellen](https://x.com/pipeline_os/status/2117719191478513700) (von [@pipeline_os](https://x.com/pipeline_os))

**Vergleiche, wie verschiedene Modelle mehrere interagierende Motive in einer Animation umsetzen.**

Die Aufnahme mit vier Ansichten stellt eine Aufgabe mit Pelikan, Fahrrad, Krokodil und Elefant für Gemini 4 Argon, Opus 5.5, Fable 5.5 und Kimi K3.1 Pro nebeneinander. Die vollständige Zusammenstellung bewahrt die Platzierung und Bewegung der Motive jedes Modells.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/9db78999efffeffa7ccaca0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/15a45dc0efe3247f0821c8a2.jpg" alt="Pelikan-Elefanten-Komposition mit vier Modellen" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-300"></a>
### Case 300: [Anime-Schwertkampf mit Impact Frames](https://x.com/camperaigg/status/2117717189059026969) (von [@camperaigg](https://x.com/camperaigg))

**Synchronisiere Figurenhandlung, kurze Aufprallbilder, Ton und bewusst eingesetzte Stille.**

Der Ersteller berichtet von einem 66-minütigen Programmierlauf für einen 46-sekündigen Strichmännchenkampf mit stoffähnlichen Umhängen, gegensätzlichen Waffen sowie synthetisierter Musik und Effekten. Die Notizen beschreiben Korrekturen an einem rückwärts gerichteten Angriff, visuellen Spuren und der Titelplatzierung.

```
Make me a video of 2 stickman fighting, anime style.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/c36c188396aac371a64e31a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b670f06d376211c60bf894.jpg" alt="Anime-Schwertkampf mit Impact Frames" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-301"></a>
### Case 301: [Laufender Hirsch im Vergleich von vier Modellen](https://x.com/fawnunwrap/status/2117702487755100543) (von [@fawnunwrap](https://x.com/fawnunwrap))

**Vergleiche Gliedmaßenbewegung und Tierform bei vollständig sichtbarer Zusammenstellung derselben Aufgabe.**

FawnBench zeigt einen laufenden Hirsch in vier Ansichten, die als berichteter Fable-5.5-Lauf, Gemini 4 Argon, GPT-6 Astra und Opus 5.5 bezeichnet sind. Das Video ist ein visueller Vergleich und kein gemessenes numerisches Leistungsergebnis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3add4d9e0752d0467cbe6065.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/eea598747047797148e19c4e.jpg" alt="Laufender Hirsch im Vergleich von vier Modellen" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-302"></a>
### Case 302: [Ein Roboter durchquert eine überflutete Stadt](https://x.com/0xMovez/status/2117700681867903169) (von [@0xMovez](https://x.com/0xMovez))

**Prüfe die Kontinuität zwischen Spiegelungen, Figurenbewegung und wechselnden Kameraansichten.**

Der Ersteller berichtet von einer 42-sekündigen Three.js-Animation mit per Code gerenderten Bildern, synthetisiertem Klang und einer einzelnen offline nutzbaren HTML-Renderdatei. Die Aufnahme folgt einem Roboter durch eine überflutete, überwucherte Stadt zu einer farbenfrohen offenen Wasserlandschaft.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f39e1807d1e80422c31530c6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/247f768636339f49d149c787.jpg" alt="Ein Roboter durchquert eine überflutete Stadt" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-303"></a>
### Case 303: [Ein Blender-Schwert und sein Präsentationsfilm](https://x.com/camperaigg/status/2117694354685092255) (von [@camperaigg](https://x.com/camperaigg))

**Trenne die prozedurale Erstellung eines Assets vom anschließenden Kamera- und Tondurchlauf.**

Der Ersteller berichtet, zunächst mit einem Python-Skript ein Schwert erzeugt und anschließend um ein Video gebeten zu haben. Der nächste Schritt nutzt eine durchgehende Blender-Kamerafahrt, Waldlicht, eine synthetisierte Orchestermusik und HyperFrames für den Schnitt; die angegebene Gesamtzeit beträgt 65 Minuten.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3c767f2038ef7d3960c956ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/525304dc7d4016ac33b3d4f8.jpg" alt="Ein Blender-Schwert und sein Präsentationsfilm" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-304"></a>
### Case 304: [Pixel-Dorf-Animation auf Lantern Isle](https://x.com/abhinavflac/status/2117693193429139965) (von [@abhinavflac](https://x.com/abhinavflac))

**Prüfe lokale Aktivitäten und Tag-Nacht-Übergänge in einer dicht gestalteten animierten Umgebung.**

Der Ersteller zeigt ein per Code gezeichnetes Inseldorf mit Bewohnern, Booten, Wasserfällen, Laternen und Musik. Die Aufnahme wechselt zwischen nahen Dorfaktivitäten, weiten Inselansichten und einer Nachtsequenz mit leuchtenden Laternen.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e91f1eabab743730dd815c98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b7d2e578739d25596db1164f.jpg" alt="Pixel-Dorf-Animation auf Lantern Isle" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-305"></a>
### Case 305: [Pause-Demo zum Schnitt von Gaming-Videos](https://x.com/pausevfx/status/2117676887665447206) (von [@pausevfx](https://x.com/pausevfx))

**Prüfe einen Schnitt-Workflow vom Rohmaterial über Untertitel bis zur bearbeitbaren Timeline.**

Pause präsentiert diesen Workflow unter der Bezeichnung Fable 5.5 für Videoschnitt. Die Demo wählt Gaming-Momente aus, setzt den Bildausschnitt einer Facecam neu, ergänzt Untertitel und Ton und öffnet eine bearbeitbare Sequenz in Premiere.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0faaeecdaa02683f81e67f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae2d32876804bf286f11dc6c.jpg" alt="Pause-Demo zum Schnitt von Gaming-Videos" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-306"></a>
### Case 306: [Ein Pelikan fährt an der Küste Fahrrad](https://x.com/pankajkumar_dev/status/2117301455665439210) (von [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Prüfe feine Geometrie und Animation sowohl in nahen als auch in weiten Kameraansichten.**

Der Ersteller zeigt einen Pelikan auf einem Hochrad am Meer. Die Aufnahme untersucht Federn, Pedale und Radgeometrie und kehrt dann zu weiteren Ansichten der gepflasterten Uferpromenade zurück.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/66c3c44bcefa684522f95b96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8575912e8f20f48439aea683.jpg" alt="Ein Pelikan fährt an der Küste Fahrrad" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-307"></a>
### Case 307: [Flug durch den Jupiter in einer Einstellung](https://x.com/camperaigg/status/2118246310981910811) (von [@camperaigg](https://x.com/camperaigg))

**Verstecke Übergänge zwischen Simulationsbereichen in Lichtwechseln, die zur Szene passen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/58a20ee3fa71781622b8897a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/a798149fc001efc1b975e204.jpg" alt="Flug durch den Jupiter in einer Einstellung" width="760"><br>▶ Video abspielen</a>

Camperaigg berichtet, dass eine einzige Aufgabenbeschreibung für Claude Code zu einem 46 Sekunden langen Flug durch den Jupiter führte. Der Beitrag beschreibt simulierte Wolkenfäden, durch Dunkelheit oder Lichtblitze verdeckte Übergänge und synthetisch erzeugte Musik aus Python.

Type: Demo | Date: 2026-11-05

---

<a id="case-308"></a>
### Case 308: [Kritische Codeprüfung in einem Claude-Code-Workflow](https://x.com/marfinxx/status/2118313633381745064) (von [@marfinxx](https://x.com/marfinxx))

**Gib dem prüfenden Agenten eine eigene Rolle und verlange vor jedem Commit einen signierten Testnachweis.**

<table><tr><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/62e0a231bb29b701a331b7e0.jpg" alt="Kritische Codeprüfung in einem Claude-Code-Workflow · 1" width="760"></td><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/3888b1f9db713d3b8be5fcf6.jpg" alt="Kritische Codeprüfung in einem Claude-Code-Workflow · 2" width="760"></td></tr><tr><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/b5ccc0e785e50b4f260343aa.jpg" alt="Kritische Codeprüfung in einem Claude-Code-Workflow · 3" width="760"></td><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/69053b5221a4a3896691b239.jpg" alt="Kritische Codeprüfung in einem Claude-Code-Workflow · 4" width="760"></td></tr><tr><td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d132b1486a11eee088ec4b48.jpg" alt="Kritische Codeprüfung in einem Claude-Code-Workflow · 5" width="760"></td></tr></table>

Marfin beschreibt eine Claude-Code-Architektur mit isoliertem Git-Worktree, maschinenlesbarem Aufgabenvertrag, Tool-Prüfungen und einer Fable-5.5-Instanz, die Änderungen auf Race Conditions und Randfälle untersucht. Der Artikel enthält Beispielkonfigurationen, Prompts und Hooks für den Ablauf.

[Vollständige Anleitung](https://x.com/marfinxx/article/2118313633381745064)

Type: Tutorial | Date: 2026-11-05

---

<a id="case-309"></a>
### Case 309: [Ryumon als Anime-Kurzfilm mit Three.js](https://x.com/flxrnc/status/2118314922375331927) (von [@flxrnc](https://x.com/flxrnc))

**Teile die Arbeit an einem per Code gerenderten Kurzfilm in Einstellungen, Animation und Ton auf.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/b4465e8ea0d1e59a702ece4a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/665c00ab433daca60f6fa344.jpg" alt="Ryumon als Anime-Kurzfilm mit Three.js" width="760"><br>▶ Video abspielen</a>

Der Beitrag zeigt einen 88 Sekunden langen Three.js-Kurzfilm und beschreibt sieben Agententeams, 39 Einstellungen, 2.112 per Code gerenderte Einzelbilder und synthetischen Ton in einer einzigen HTML-Datei.

[Originalprompt und Code](https://x.com/flxrnc/status/2118314927681089619)

Type: Demo | Date: 2026-11-05

---

<a id="case-310"></a>
### Case 310: [Ein Ruderboot im Gewitter](https://x.com/camperaigg/status/2118317021935071339) (von [@camperaigg](https://x.com/camperaigg))

**Stimme den Rhythmus der Wellen und die Schallverzögerung auf die Kamerafahrt ab.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/c717f78c1c94d6aa87a5b2cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8fd382dc1d7f48481aa98a61.jpg" alt="Ein Ruderboot im Gewitter" width="760"><br>▶ Video abspielen</a>

Camperaigg berichtet von einer ungeschnittenen 35-Sekunden-Einstellung, die mit einem einzigen Prompt in Claude Code entstand. Der Ablauf setzt große Wellen an dramaturgischen Wendepunkten ein, verzögert den Donner je nach Entfernung und korrigiert das Ruderrig sowie die Position des Boots in der Simulation.

Type: Demo | Date: 2026-11-05

---

<a id="case-311"></a>
### Case 311: [Stillstehender Regen im Anime-Kurzfilm](https://x.com/seeconvm/status/2118319936594465120) (von [@seeconvm](https://x.com/seeconvm))

**Nutze einen einzigen Offline-HTML-Player für zeitlich abgestimmte Einstellungen und synthetischen Ton.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/fc822df698c69770cbe394ad.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/f2ae8ab78b2917d38d2f10b4.jpg" alt="Stillstehender Regen im Anime-Kurzfilm" width="760"><br>▶ Video abspielen</a>

Der Beitrag zeigt eine 50 Sekunden lange Three.js-Animation, in der Regentropfen in der Luft stehen bleiben. Das verlinkte Projekt enthält den Originalprompt, den Code und den Offline-Player.

[Originalprompt und Code](https://x.com/seeconvm/status/2118319944714567938)

Type: Demo | Date: 2026-11-05

---

<a id="case-312"></a>
### Case 312: [Anime aus Skripten mit Blender und Python](https://x.com/anstapnever/status/2118328801352466895) (von [@anstapnever](https://x.com/anstapnever))

**Richte einen Ablauf ein, der Konturen, Kolorierung und Orchesterton pro Einstellung verarbeitet.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/f8af6522676fd735dd4e2aa1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/b26fae93537f4e6c2a54bddb.jpg" alt="Anime aus Skripten mit Blender und Python" width="760"><br>▶ Video abspielen</a>

Der Beitrag zeigt einen etwa 90 Sekunden langen Anime-Film und beschreibt die parallele Arbeit von Agenten an 44 Einstellungen. Blender und Python zeichnen und kolorieren die Einzelbilder. Der orchestrale Soundtrack ist synthetisch erzeugt.

[Originalprompt und Code](https://x.com/anstapnever/status/2118328806109053193)

Type: Demo | Date: 2026-11-05

---

<a id="case-313"></a>
### Case 313: [Beacon: eine Leuchtturmgeschichte in Three.js](https://x.com/zodchiii/status/2118363287738073343) (von [@zodchiii](https://x.com/zodchiii))

**Packe einen Film mit mehreren Einstellungen in eine einzige offline nutzbare HTML-Datei.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/e25ff2a28c6efdc45bfc7b80.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d7d094bd606dd0e6b0bff2eb.jpg" alt="Beacon: eine Leuchtturmgeschichte in Three.js" width="760"><br>▶ Video abspielen</a>

Das Video zeigt Beacon, eine Leuchtturmgeschichte mit einem kugelförmigen Roboter und Figuren, die wie Spielzeug aussehen. Der Beitrag beschreibt acht parallel arbeitende Agententeams, 39 Einstellungen, synthetische Musik und Klangeffekte.

Type: Demo | Date: 2026-11-05

---

<a id="case-314"></a>
### Case 314: [Eine per Code gerenderte Eröffnungssequenz](https://x.com/devteamdrew/status/2118387876387766683) (von [@devteamdrew](https://x.com/devteamdrew))

**Nutze eine kurze Eröffnungsszene, um eine Animationsaufgabe mit nur einer Anfrage zu testen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/e53b379fe4b176845ce10601.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/5a3125a1f165bfa82e97725e.jpg" alt="Eine per Code gerenderte Eröffnungssequenz" width="760"><br>▶ Video abspielen</a>

Der Beitrag zeigt eine etwa 18 Sekunden lange Eröffnungssequenz. Laut Bericht dauerte es etwas mehr als zwei Stunden, die Szene aus einer einzigen Anfrage zu entwerfen, umzusetzen und zu rendern.

Type: Demo | Date: 2026-11-06

---

<a id="case-315"></a>
### Case 315: [Ein Axt-GIF aus sechs Bildern in Blender nachbauen](https://x.com/camperaigg/status/2118410521363845534) (von [@camperaigg](https://x.com/camperaigg))

**Prüfe den Nachbau von der Seite und lass dir Rig und Materialien im Detail zeigen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/99b2188373ec5287c16e40ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/dcadf8c7bac0f9630177dc48.jpg" alt="Ein Axt-GIF aus sechs Bildern in Blender nachbauen" width="760"><br>▶ Video abspielen</a>

Camperaigg berichtet, einen Axthieb aus sechs Einzelbildern rekonstruiert und anschließend um eine Ansicht des Blender-Modells gebeten zu haben. Die Seitenansicht zeigte zu dünne Axtköpfe. Der überarbeitete Clip zeigt das neutrale Modell, das Drahtgitter, die Materialien und das Rig, bevor die Kamera das Modell umkreist.

Folgeprompt

```
it doesn't look very 3D, show me the actual Blender model
```

Type: Demo | Date: 2026-11-06

---

<a id="case-316"></a>
### Case 316: [Interaktives Regenbogengelee im Modellvergleich](https://x.com/0xRhinoX/status/2118415577299460432) (von [@0xRhinoX](https://x.com/0xRhinoX))

**Vergleiche mit derselben interaktiven Aufgabe, welche Verhaltensweisen die Modelle von sich aus ergänzen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/21235525e597105d4afa1c53.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/4da95e15a1c4094b8f5b99d2.jpg" alt="Interaktives Regenbogengelee im Modellvergleich" width="760"><br>▶ Video abspielen</a>

Fable 5.5 und Gemini 4 Carbon erhielten dieselbe Aufgabe: Gelee zu erstellen, das sich schneiden, mit Nägeln durchbohren und anbrennen lässt. Fables Version heilte nach Beschädigungen. Der Beitrag nennt 48,50 USD und 45 Minuten für Fable sowie 4,30 USD und 32 Minuten für Carbon.

Type: Evaluation | Date: 2026-11-06

---

<a id="case-317"></a>
### Case 317: [Ein Drachenflugspiel in einer einzigen Datei](https://x.com/noisyb0y1/status/2118451983359311957) (von [@noisyb0y1](https://x.com/noisyb0y1))

**Speichere einen 3D-Prototyp in einer HTML-Datei, damit er sich per Link schnell testen lässt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/0c57717bb7e652039107134f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/aa879655bb8f199adf91400d.jpg" alt="Ein Drachenflugspiel in einer einzigen Datei" width="760"><br>▶ Video abspielen</a>

Der Beitrag zeigt ein Drachenflugspiel mit frei beweglicher Kamera, per Code erzeugtem Meer und Himmel sowie Kriegsschiffen, die auf die Spielfigur schießen. Die veröffentlichte Fassung entstand nach einer zweiten Anfrage.

Type: Demo | Date: 2026-11-06

---

<a id="case-318"></a>
### Case 318: [Basketball-Falltest mit eigenem Blender-Solver](https://x.com/camperaigg/status/2118673822459281765) (von [@camperaigg](https://x.com/camperaigg))

**Prüfe Rücksprunghöhe und Verformung und sieh dir die Simulation anschließend in Blender an.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8e3cc422e63adc926c69807a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d7dc23722d696a126e5328b9.jpg" alt="Basketball-Falltest mit eigenem Blender-Solver" width="760"><br>▶ Video abspielen</a>

Camperaigg berichtet von einer Simulation mit einer unter Druck stehenden Hülle. Aus 1,80 m Fallhöhe sprang der Ball auf 1,32 m zurück. Nach einer weiteren Anfrage zeigte der Clip zunächst die Blender-Ansicht und wechselte dann in die gerenderte Arena.

Folgeprompt

```
shows off in a blender first and then transition into the arena
```

Type: Demo | Date: 2026-11-06

---

<a id="case-319"></a>
### Case 319: [Einzelbildprüfung für einen geskripteten Anime](https://x.com/anstapnever/status/2118700618915397795) (von [@anstapnever](https://x.com/anstapnever))

**Füge vor dem finalen Rendern eines geskripteten Films Prüfungen auf Clipping hinzu.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/7c6bb5894aae3564edf04c09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8115bc37506ed9a23d6962fd.jpg" alt="Einzelbildprüfung für einen geskripteten Anime" width="760"><br>▶ Video abspielen</a>

Der Beitrag zeigt einen 92 Sekunden langen Film aus Blender und Python. Er beschreibt die parallele Agentenarbeit an 43 Einstellungen, Konturen und Kolorierung per Skript, Clipping-Prüfungen pro Einzelbild und einen synthetischen Soundtrack.

[Originalprompt und Code](https://x.com/anstapnever/status/2118700623004848474)

Type: Demo | Date: 2026-11-06

---

<a id="case-320"></a>
### Case 320: [Ein Streichholz in 44-facher Zeitlupe](https://x.com/camperaigg/status/2118728540976009336) (von [@camperaigg](https://x.com/camperaigg))

**Verwende eine gemeinsame Zeitbasis für Simulation, gerenderte Bilder und Ton.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/3854b7f696993575e841539a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d97aaaec008adcc4387e72f9.jpg" alt="Ein Streichholz in 44-facher Zeitlupe" width="760"><br>▶ Video abspielen</a>

Camperaigg berichtet von einer in Three.js umgesetzten Streichholzszene mit GPU-Verbrennungssimulation, Makroobjektiv und synthetischem Ton. Der Agent prüfte das eigene Material und wiederholte die Simulation, als die Flammenform unpassend aussah.

Type: Demo | Date: 2026-11-06

---

<a id="case-321"></a>
### Case 321: [Ein Referenzbild als SVG nachzeichnen](https://x.com/dummerspast39/status/2118780483232317912) (von [@dummerspast39](https://x.com/dummerspast39))

**Prüfe die Vektorpfade und vergleiche das Ergebnis mit der Bildvorlage.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/873e762879e0c6ab5ea80151.jpg" alt="Ein Referenzbild als SVG nachzeichnen" width="760">

Für den Versuch wurden Referenzbilder vorgegeben. Der Beitrag zeigt einen Screenshot des SVG-Ergebnisses. Laut Bericht wurde dessen Aufbau mit GPT-6.1 Sol geprüft. Die SVG-Pfade sind in der Quelle nicht veröffentlicht.

Type: Demo | Date: 2026-11-07

---

<a id="case-322"></a>
### Case 322: [Dieselbe Mario-Aufgabe für zwei Modelle](https://x.com/0xRhinoX/status/2118789381662429475) (von [@0xRhinoX](https://x.com/0xRhinoX))

**Vergleiche anhand derselben Aufgabe, wie genau die Modelle ein Level nachbauen und welche eigenen Ideen sie einbringen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/9d964836dcc72ce880bbfbf1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/970bec8434d4db16547549bd.jpg" alt="Dieselbe Mario-Aufgabe für zwei Modelle" width="760"><br>▶ Video abspielen</a>

Im veröffentlichten Test baute Gemini 4 Carbon ein Mario-Level nach, während Fable ein Spiel über die Reparatur eines Wasserturms erstellte. Der Beitrag nennt 0,90 USD und 3 Minuten für Carbon sowie 34 USD und 29 Minuten für Fable.

Type: Evaluation | Date: 2026-11-07

---

<a id="case-323"></a>
### Case 323: [Eine dreidimensionale Voxel-Pagode](https://x.com/JaydenDavisNC/status/2118807627714990485) (von [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**Betrachte ein Voxelgebäude aus mehreren Perspektiven, um Tiefe und Silhouette zu beurteilen.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/0e0dfb05333faf5a4fc0bdec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/f05509505248bbbd310f5738.jpg" alt="Eine dreidimensionale Voxel-Pagode" width="760"><br>▶ Video abspielen</a>

Der Beitrag zeigt eine kurze Aufnahme einer dreidimensionalen Voxel-Pagode. Im Video lassen sich die gestaffelten Dächer und die Gesamtkomposition betrachten.

Type: Demo | Date: 2026-11-07

---

<a id="case-324"></a>
### Case 324: [Rauch eines brennenden Briefs in Three.js](https://x.com/camperaigg/status/2119006297513435548) (von [@camperaigg](https://x.com/camperaigg))

**Beleuchte den simulierten Rauch von hinten und prüfe den Drucksolver bei voller Auflösung.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/48d0b034652b734f6e387d8e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/0997278c25cd9c88aed47498.jpg" alt="Rauch eines brennenden Briefs in Three.js" width="760"><br>▶ Video abspielen</a>

Camperaigg zeigt eine 30 Sekunden lange Einstellung eines brennenden Briefs und beschreibt GPU-Partikelrauch, einen wandernden Lichtstrahl und synthetischen Ton. Nach vier beantworteten Fragen behob der Agent laut Bericht einen numerischen Fehler im Drucksolver.

Type: Demo | Date: 2026-11-07

---

<a id="case-325"></a>
### Case 325: [Mit einem Blitz bis zum Boden](https://x.com/camperaigg/status/2119052253982306393) (von [@camperaigg](https://x.com/camperaigg))

**Lass die laufende Simulation sowohl die Kamera als auch den Ton steuern.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d6ee461c4cdf38ce8f5759a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/97c61bf20843530b450005e0.jpg" alt="Mit einem Blitz bis zum Boden" width="760"><br>▶ Video abspielen</a>

Camperaigg berichtet von einer 28 Sekunden langen Einstellung mit Three.js und Taichi. Die Kamera folgt der Spitze des Blitzes, der Ton dessen einzelnen Schritten. Bei der Einzelbildprüfung fiel ein Stroboskopeffekt auf, den der Agent vor der Übergabe korrigierte.

Type: Demo | Date: 2026-11-07

---

<a id="case-326"></a>
### Case 326: [Ein Riesenroboter fängt einen Meteor](https://x.com/seeconvm/status/2119052317227987018) (von [@seeconvm](https://x.com/seeconvm))

**Lege vor dem Rendern fest, wer die einzelnen Einstellungen betreut und wer die künstlerische Leitung übernimmt.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/10c500daeecb0af61a05553e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/a509847ad05762e472a7096c.jpg" alt="Ein Riesenroboter fängt einen Meteor" width="760"><br>▶ Video abspielen</a>

Der Beitrag zeigt einen 82 Sekunden langen Mecha-Kurzfilm und beschreibt sechs parallel arbeitende Teams, 36 Einstellungen und 1.968 per Code gerenderte Einzelbilder. Prompt und Projektcode stehen in einer Antwort.

[Originalprompt und Code](https://x.com/seeconvm/status/2119052321795551415)

Type: Demo | Date: 2026-11-07

---

<a id="case-327"></a>
### Case 327: [Pixel-Art-Schaufenster nach derselben Vorgabe](https://x.com/AIMind_Ai/status/2119053573526901001) (von [@AIMind_Ai](https://x.com/AIMind_Ai))

**Vergleiche die unveränderten Effekte, bevor du einzelne Details nachjustierst.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/c953d5e5c0e87fecdac9dcc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/ab064042073f1266b2f1caf1.jpg" alt="Pixel-Art-Schaufenster nach derselben Vorgabe" width="760"><br>▶ Video abspielen</a>

Fable 5.5 und Opus 5.5 sollten ein weihnachtliches Schaufenster in 3D-Pixel-Art gestalten. Opus ergänzte Dekorationen. Bei Fable verkleinerte die Person hinter dem Beitrag die Schneeflocken, damit die Szene sichtbar blieb. Die Quelle zeigt beide Ergebnisse nebeneinander.

Type: Evaluation | Date: 2026-11-07

---

<a id="case-328"></a>
### Case 328: [Ein Bronzeriese in einer animierten Stadt](https://x.com/anstapnever/status/2119082173387137034) (von [@anstapnever](https://x.com/anstapnever))

**Verteile Umgebung, Figuren, Effekte und Ton auf parallel arbeitende Teams.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/8ff966cd65fa2c2c5dd253e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/34679b2782af94de4f0ad237.jpg" alt="Ein Bronzeriese in einer animierten Stadt" width="760"><br>▶ Video abspielen</a>

Der Beitrag zeigt einen 77 Sekunden langen, im Browser gerenderten Anime-Kurzfilm. Beschrieben werden fünf Teams, 31 Einstellungen und Clipping-Prüfungen pro Einzelbild. Zu sehen sind eine Stadt und ein Bronzeriese, begleitet von synchronisierter Orchestermusik.

[Originalprompt und Code](https://x.com/anstapnever/status/2119136411693777365)

Type: Demo | Date: 2026-11-07

---

<a id="case-329"></a>
### Case 329: [Wie sich blaue Tinte in einem Glaskolben verteilt](https://x.com/camperaigg/status/2119097552943612410) (von [@camperaigg](https://x.com/camperaigg))

**Prüfe die Partikeldichte, um Fehler in einer Fluidsimulation vor dem Rendern zu finden.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/d6f3277ec1b19c7d45044e18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-08/ba7b4db94891d5a26a959423.jpg" alt="Wie sich blaue Tinte in einem Glaskolben verteilt" width="760"><br>▶ Video abspielen</a>

Camperaigg berichtet von einer einzigen Aufgabenbeschreibung in Claude Code für einen 30 Sekunden langen Three.js-Clip. Der Ablauf simuliert den Tintenfluss, rendert den Kolben per Raytracing, variiert das Wiedergabetempo innerhalb einer Einstellung und prüft die Simulation auf Streifenbildung und Tintenverlust.

Type: Demo | Date: 2026-11-08

---

<a id="acknowledge"></a>
## 🙏 Danksagung

Dieses Repository wurde von den Creators, Entwicklern, Benchmark-Teams und Communities inspiriert, die reale Claude Fable 5-Anwendungsfälle öffentlich geteilt haben.

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@hakmgpt](https://x.com/hakmgpt), [@camperaigg](https://x.com/camperaigg), [@lightreelai](https://x.com/lightreelai), [@0xMovez](https://x.com/0xMovez), [@shmidtqq](https://x.com/shmidtqq), [@flxrnc](https://x.com/flxrnc), [@seeconvm](https://x.com/seeconvm), [@BubbleBrain](https://x.com/BubbleBrain), [@xbquan](https://x.com/xbquan), [@pipeline_os](https://x.com/pipeline_os), [@fawnunwrap](https://x.com/fawnunwrap), [@pausevfx](https://x.com/pausevfx), [@marfinxx](https://x.com/marfinxx), [@anstapnever](https://x.com/anstapnever), [@zodchiii](https://x.com/zodchiii), [@0xRhinoX](https://x.com/0xRhinoX), [@dummerspast39](https://x.com/dummerspast39), [@AIMind_Ai](https://x.com/AIMind_Ai), [@AnikaCodes](https://x.com/AnikaCodes), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@cfenghub](https://x.com/cfenghub), [@shneural](https://x.com/shneural), [@FramiaPro](https://x.com/FramiaPro)

*Wir können nicht garantieren, dass jeder Fall dem ursprünglichen Creator zugeschrieben ist. Wenn etwas korrigiert werden muss, kontaktiere uns bitte, und wir aktualisieren es.*

Wenn du weitere interessante Anwendungsfälle teilen möchtest, öffne gerne ein Issue oder eine Pull Request und hilf, die Evolink-Usecase-Bibliothek zu erweitern.


[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
