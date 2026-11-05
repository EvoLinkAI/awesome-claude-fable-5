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

<a id="-introduction"></a>
## 🍌 Introduction

Bienvenue dans le dépôt de cas d'utilisation à fort signal pour Claude Fable 5.

**Nous collectons des cas d'utilisation réels, des tutoriels, des intégrations et des évaluations pour Claude Fable 5, sélectionnés à partir de démonstrations publiques et de communautés de créateurs.**

Ce README français est une localisation complète de la source anglaise et se concentre sur les cas à fort signal avec des workflows concrets, des prompts, des démonstrations, des intégrations, des preuves de benchmark ou des limites pratiques.

La plupart des cas sont sélectionnés depuis des publications X/Twitter et des démonstrations publiques. Chaque titre de cas renvoie à la source originale et chaque identifiant d'auteur renvoie au profil du créateur.

Essayez-le sur Evolink : [Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

<a id="-overview"></a>
## 📊 Vue d'ensemble

- **88 cas Fable 5 initiaux et 218 cas de la communauté, soit 306 cas au total.**
- Couvre les agents de code, l'automatisation longue durée, les jeux, le design visuel, les simulations 3D, le travail de connaissance, les tutoriels, les intégrations API, les benchmarks, les prix et les limitations de lancement.
- Chaque cas inclut la source originale, l'attribution au créateur, un enseignement concis, le type de preuve et la date de publication.
- Utilisez ce dépôt pour trouver des workflows pratiques, comparer forces et limites, découvrir des prompts reproductibles et suivre des exemples d'intégration.

> [!NOTE]
> La collection privilégie les preuves concrètes plutôt que le battage médiatique : prompts reproductibles, démos livrées, méthodes de benchmark, notes d'intégration, données de coût et réserves clairement formulées.

<a id="-quick-api-access"></a>
## ⚡ Accès rapide à l'API

Utilisez Claude Fable 5 via l'API Messages compatible avec Evolink. Obtenez un token API via [Evolink](https://evolink.ai/login?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5), puis remplacez `<token>` par votre token.

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

<a id="-menu"></a>
## 📑 Menu

| Section | Cas |
|---|---|
| [💻 Codage et génération de code](#coding-and-code-generation) | Case 1-6 |
| [🤖 Agents et automatisation longue durée](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 Jeux et démos interactives](#games-and-interactive-demos) | Case 9-12 |
| [🎨 Visuel, design, vidéo et 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 Documents, travail de connaissance et recherche](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 Tutoriels, cours et ressources de prompts](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 Plateforme, API et intégration d'outils](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 Évaluations, comparaisons et limites](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | Crédits et politique de correction |

### [💻 Codage et génération de code](#coding-and-code-generation)

| Case | Ce que cela montre | Type |
|---|---|---|
| [Workflow Cursor en plusieurs étapes](#case-1) | Utilisez Fable 5 comme étape de revue de plan et de critique dans un workflow Cursor multi-modèles, puis confiez l'implémentation et les révisions à des modèles moins chers ou spécialisés. |  |
| [Recréation de GitHub à partir d'une capture d'écran](#case-2) | Collez une capture d'écran produit dans un outil de codage agentique et demandez à Fable 5 de recréer l'interface avec des fonctionnalités opérationnelles. |  |
| [Simulation de trou noir avec un seul prompt](#case-3) | Donnez à Fable 5 un prompt détaillé de creative coding et demandez-lui de produire une visualisation physique Three.js autonome. |  |
| [Web OS façon macOS en one-shot](#case-4) | Demandez à Fable 5 un web OS complet en fichier unique et laissez-le construire en une passe le shell UI, les apps, les interactions, l'audio et le comportement de jeu intégré. |  |
| [Construction de Spawn 5.0 avec 1 687 prompts](#case-5) | Utilisez Fable 5 comme partenaire d'ingénierie sur de longues sessions et de nombreux prompts, avec un humain qui passe de l'architecture au jugement de qualité de sortie. |  |
| [Revue d'une grande pull request avec constats](#case-6) | Pointez Fable 5 vers une grande pull request et demandez-lui d'examiner la justesse, les faux positifs, les vrais bugs et les problèmes de finition. |  |

### [🤖 Agents et automatisation longue durée](#agents-and-long-running-automation)

| Case | Ce que cela montre | Type |
|---|---|---|
| [Revue d'un workflow relais sur horizon long](#case-7) | Utilisez Fable 5 pour des travaux ambitieux sur horizon long : refontes de sites, pipelines de contenu programmatiques, adaptation de voix, revue de sécurité et contrôles qualité finaux. |  |
| [Diagnostic d'une panne d'infrastructure et ouverture d'une PR de correction](#case-8) | Donnez à Fable 5 accès à des indices d'infra comme les logs, les erreurs de base de données et les digests d'images, puis demandez-lui de diagnostiquer la panne et de préparer le correctif. |  |

### [🎮 Jeux et démos interactives](#games-and-interactive-demos)

| Case | Ce que cela montre | Type |
|---|---|---|
| [Dino Runner avec suivi du doigt](#case-9) | Demandez à Fable 5 de construire un jeu navigateur qui utilise le suivi du doigt comme mécanique d'entrée. |  |
| [Jeu de course construit avec deux phrases](#case-10) | Donnez à Fable 5 un prompt de jeu très court et laissez-le générer cartes, modes, musique, UI et assets de jeu en une seule exécution. |  |
| [Minecraft terminal installable en Rust](#case-11) | Exécutez Fable 5 via un harness de codage terminal et demandez-lui de construire un jeu terminal Rust installable. |  |
| [Clone de Minecraft avec temps et coût](#case-12) | Utilisez un prompt pour demander à Fable 5 un clone jouable façon Minecraft, puis évaluez le temps, le coût, le volume de code et la couverture fonctionnelle. |  |

### [🎨 Visuel, design, vidéo et 3D](#visual-design-video-and-3d)

| Case | Ce que cela montre | Type |
|---|---|---|
| [Prompt complet reproductible pour un email ecommerce](#case-13) | Donnez à Fable 5 un brief créatif complet pour une maquette d'email de marque, incluant les sections exactes, exigences produit, direction visuelle et contraintes. |  |
| [Benchmark d'horloger avec échappement à ancre suisse](#case-14) | Utilisez Fable 5 sur un benchmark de simulation mécanique et demandez-lui d'implémenter, vérifier et itérer sur la justesse physique. |  |
| [Scène Three.js de l'appartement de Friends](#case-15) | Demandez à Fable 5 de transformer un plan d'étage et une référence de scène en environnement Three.js navigable. |  |
| [Simulation du système solaire avec prompt et URL](#case-16) | Utilisez Fable 5 pour construire une simulation astronomique à partir des principes physiques, en itérant jusqu'à ce que la simulation et la sortie publique soient prêtes. |  |

### [📚 Documents, travail de connaissance et recherche](#documents-knowledge-work-and-research)

| Case | Ce que cela montre | Type |
|---|---|---|
| [Preuves Stripe et workflows scientifiques](#case-17) | Utilisez ceci comme preuve pour les affirmations sur la migration d'entreprise et les workflows scientifiques, pas comme prompt à copier-coller. |  |
| [Mémo de politique publique et workflows de suivi des modifications](#case-18) | Utilisez Fable 5 pour le travail qualitatif long format sur documents : suivi des modifications, tri de commentaires et éditions guidées par transcription. |  |
| [Prompt de recherche approfondie et résultat](#case-19) | Posez à Fable 5 une question de type recherche et évaluez s'il peut produire une longue réponse structurée et historiquement fondée. |  |

### [🧭 Tutoriels, cours et ressources de prompts](#tutorials-courses-and-prompt-resources)

| Case | Ce que cela montre | Type |
|---|---|---|
| [Comment Fable 5 change les workflows Claude Code](#case-20) | Utilisez Fable 5 en définissant direction, contexte, objectifs et critères de vérification au lieu de microgérer chaque étape. |  |
| [Revue d'un milliard de tokens et stratégie de routage](#case-21) | Utilisez Fable 5 pour la planification et la revue frontier, puis routez l'implémentation à fort volume vers des modèles moins chers. |  |
| [Prompt défensif de durcissement d'appareils](#case-22) | Exécutez un prompt de durcissement défensif étape par étape où Fable 5 inventorie les appareils, donne des vérifications exactes et attend validation. |  |
| [Prompt `/goal` d'audit design d'un site complet](#case-23) | Utilisez `/goal` pour faire démarrer un site par Fable 5, capturer les pages, auditer l'UX, écrire un rapport et corriger les petits problèmes sûrs. |  |
| [Répartition du travail créatif long format](#case-24) | Utilisez Fable 5 pour concevoir des formats et exemples stables, puis transmettez cette structure à un autre système de génération pour la sortie spécifique au domaine. |  |
| [Guide débutant pour utiliser Fable 5](#case-25) | Utilisez Fable 5 avec des prompts orientés objectif, des boucles de vérification et des réglages d'effort plutôt qu'avec de petites instructions pas à pas. |  |
| [Prompt copier-coller d'audit de dépôt](#case-26) | Collez le prompt d'audit de dépôt dans Fable 5 et demandez-lui une découverte appuyée par fichiers, des constats, une stratégie et un plan de tâches par jalons. |  |
| [Stratégie d'utilisation pendant une fenêtre limitée](#case-27) | Dépensez l'usage Fable 5 sur l'audit, l'architecture et la planification tant que la fenêtre d'accès est favorable, puis utilisez des modèles moins chers pour l'exécution. |  |
| [Utilisation des objectifs et workflows dans Claude Code](#case-28) | Utilisez Fable 5 comme partenaire de réflexion avant l'implémentation, puis combinez `/goal` et workflows pour exécuter et vérifier le plan. |  |

### [🔌 Plateforme, API et intégration d'outils](#platform-api-and-tool-integration)

| Case | Ce que cela montre | Type |
|---|---|---|
| [Configuration de l'intégration Hermes Agent](#case-29) | Configurez Hermes pour utiliser `anthropic/claude-fable-5` sur les runs `/goal` complexes et les tâches longues avec cache. |  |
| [Capacités, prix et notes d'abonnement](#case-30) | Utilisez ce cas pour comprendre quand Fable 5 est disponible, ce qu'il coûte et quels domaines protégés peuvent basculer vers un autre modèle. |  |
| [Synthèse lancement, accès, prix et sécurité](#case-31) | Utilisez cette synthèse de lancement pour choisir la voie d'accès, le nom de modèle API, la fenêtre de contexte, la stratégie de cache et le timing d'abonnement. |  |
| [Stratégie de réduction des coûts avec advisor](#case-32) | Utilisez Fable 5 comme advisor ou reviewer dans un workflow avec modèle moins cher lorsque l'intelligence marginale vaut le coût. |  |
| [Prix, accès et garde-fous de sécurité](#case-33) | Utilisez ce cas pour comprendre l'accès à Fable 5, les prix API et le comportement de fallback de sécurité avant de planifier des charges de travail. |  |
| [Intégration Swarms en une ligne](#case-34) | Définissez le nom de modèle Swarms sur `anthropic/claude-fable-5` et exécutez Fable 5 via le framework ou l'API Swarms. |  |

### [📏 Évaluations, comparaisons et limites](#evaluations-comparisons-and-limits)

| Case | Ce que cela montre | Type |
|---|---|---|
| [Comparaison coût et qualité entre Fable 5 et GPT-5.5](#case-35) | Comparez Fable 5 et GPT-5.5 sur la même tâche de codage pour juger qualité de sortie, durée d'exécution et coût d'outil. |  |
| [Résultat du benchmark AA-Omniscience](#case-36) | Utilisez ce cas de benchmark pour évaluer Fable 5 sur la précision des connaissances et le comportement d'hallucination. |  |
| [Résultat de l'Artificial Analysis Intelligence Index](#case-37) | Utilisez ce cas pour benchmarker le classement d'intelligence global de Fable 5 face aux autres modèles frontier. |  |
| [Benchmark GDPval-AA de travail de connaissance agentique](#case-38) | Utilisez ce cas pour évaluer Fable 5 sur le travail de connaissance agentique en conditions réelles. |  |
| [Premières impressions après une semaine et mécanique de prix](#case-39) | Utilisez ce cas de premières impressions pour décider où Fable 5 est le plus fort, notamment en game design et planification de systèmes. |  |
| [Comparaison de coût et de vitesse](#case-40) | Utilisez cette comparaison pour décider si le gain de qualité justifie le coût plus élevé et les runs longs plus lents. |  |
| [Notes pratiques sur Claude Code](#case-41) | Utilisez ce cas pour évaluer Fable 5 dans Claude Code, y compris l'usage d'outils, la personnalité et les aspérités restantes. |  |
| [Résultat du benchmark d'écriture créative](#case-42) | Utilisez ce cas de benchmark pour juger la qualité d'écriture de nouvelles courtes de Fable 5 et son comportement de refus. |  |
| [Synthèse de lancement multi-benchmarks](#case-43) | Utilisez cette synthèse de benchmarks de lancement pour comprendre les scores principaux les plus pertinents pour les agents de code et les tâches complexes. |  |
| [Comparaison benchmark et prix avec GPT-5.5](#case-44) | Utilisez cette comparaison pour évaluer Fable 5 face à GPT-5.5 sur le prix et les catégories de benchmark. |  |
| [Notes de terrain avec limites pratiques](#case-45) | Utilisez ce retour terrain pour comprendre où Fable 5 semble nettement meilleur et où il conserve des limites pratiques. |  |
| [Comparaison de simulations physiques](#case-46) | Exécutez des prompts identiques de simulation physique contre Fable 5 et Opus 4.8 pour comparer qualité de sortie, coût et vitesse. |  |
| [Expérience de débogage et jugement design](#case-47) | Utilisez Fable 5 pour le débogage en lui demandant de mesurer, logger, vérifier et patcher plutôt que simplement deviner. |  |
| [Avantages et inconvénients multidimensionnels](#case-48) | Utilisez ce cas pour comprendre les forces et faiblesses pratiques avant de faire de Fable 5 votre modèle quotidien. |  |
| [Test de rédaction juridique S-1](#case-49) | Utilisez un prompt de rédaction S-1 comme test de capacité d'agent juridique et comparez structure, formatage et longueur. |  |
| [Détails de benchmarks santé](#case-50) | Utilisez cette note de benchmark pour évaluer Fable 5 sur les tâches liées à la santé et identifier les évaluations médicales difficiles manquantes. |  |
| [Évaluation ParseBench de parsing de documents](#case-51) | Utilisez ce cas pour décider si Fable 5 est rentable pour le parsing de documents face à des systèmes OCR spécialisés. |  |
| [Comparaison SWE-Bench Pro et FrontierCode](#case-52) | Utilisez ce cas de benchmark pour évaluer Fable 5 pour migrations, implémentations complexes, sessions autonomes, tests et vérification visuelle. |  |
| [Revue qualitative de résolution de problèmes longs](#case-53) | Utilisez cette revue qualitative pour comprendre pourquoi Fable 5 convient aux tâches plus longues et plus difficiles tout en exigeant encore une revue de production. |  |
| [Résultats ParseBench de fidélité et de formatage](#case-54) | Utilisez ce résultat ParseBench pour juger les performances de fidélité documentaire et de formatage. |  |
| [Benchmarks, prix, accès et garde-fous](#case-55) | Utilisez ce cas comme checklist large pour benchmarks, prix, accès, garde-fous et implications stratégiques. |  |
| [Liste officielle des scores de benchmark](#case-56) | Utilisez cette liste de benchmarks pour comprendre les scores officiels de Fable 5 sur code, usage ordinateur et tâches de sécurité. |  |
| [Méthodologie du benchmark APEX-SWE](#case-57) | Utilisez ce cas pour évaluer Fable 5 sur APEX-SWE, notamment observability et travail d'intégration. |  |
| [Résultat ProofBench en mathématiques formelles](#case-58) | Utilisez ce cas pour évaluer Fable 5 en mathématiques formelles face à des systèmes spécialisés de preuve de théorèmes. |  |
| [Analyse préliminaire VirtueBench](#case-59) | Utilisez ce cas pour inspecter le comportement de raisonnement moral de Fable 5 à travers les catégories de vertus. |  |
| [Test d'overfit de sécurité avec réponse API vide](#case-60) | Utilisez ce cas pour comprendre le risque d'overfit de sécurité au lancement et le comportement de réponse vide en test API. |  |
| [Concevoir des prompts Fable avec vérification](#case-61) | Utilisez ce guide pour remplacer les longues astuces de prompting par un objectif, du contexte, des contraintes, des outils et des boucles de vérification. | Tutoriel |
| [Un jeu de plateforme à Istanbul depuis une référence](#case-62) | Testez Fable 5 avec une planche de sprites de référence et une consigne de conversion en jeu de plateforme jouable. | Démo |
| [Un tableau de bord métier en ville 3D](#case-63) | Utilisez Fable 5 pour transformer un processus métier en concept de tableau de bord urbain 3D animé. | Démo |
| [Un jeu de trou en Three.js en une passe](#case-64) | Utilisez Fable 5 pour créer en une passe un prototype de jeu 3D pour navigateur en Three.js. | Démo |
| [Comparer les scores DeepSWE](#case-65) | Appuyez-vous sur cette note DeepSWE pour comparer Fable 5 xHigh à GPT-5.5 xHigh en ingénierie logicielle. | Évaluation |
| [Comparer les coûts d'analyse d'un dépôt](#case-66) | Utilisez cette comparaison d'analyses de dépôt pour mettre le prix des tokens en regard du coût des corrections humaines. | Évaluation |
| [Consommation de tokens d'un jeu Super Mario](#case-67) | Utilisez cette création de jeu en une passe pour estimer la qualité de sortie et la consommation de tokens de Fable 5. | Démo |
| [Le réglage de repli de Claude Code](#case-68) | Découvrez le réglage de Claude Code qui change de modèle lorsqu'un message destiné à Fable 5 est signalé. | Intégration |
| [Construire un simulateur Namma Metro](#case-69) | Utilisez cette démonstration comme exemple concis de création d'un simulateur de transport public avec Fable 5 par vibe coding. | Démo |
| [Dusk Drive créé avec un seul prompt](#case-70) | Évaluez Fable 5 sur le prototypage d'un jeu de conduite low-poly sans retouches humaines à partir de ce cas. | Démo |
| [Le classement APEX-Agents en Pass@1](#case-71) | Utilisez ce résultat APEX-Agents pour comparer Fable 5 Max sur des tâches autonomes à plusieurs étapes. | Évaluation |
| [Un guide de sélection des modèles Claude](#case-72) | Réservez Fable 5 aux tâches les plus difficiles dans Claude Code grâce à ce guide de sélection. | Tutoriel |
| [La boucle agentique automatisée de HermesWorld](#case-73) | Étudiez une boucle Fable 5 qui construit, teste, joue et exécute des tests de fumée pendant plusieurs jours sans intervention. | Intégration |
| [Tester un rapport dans le style McKinsey](#case-74) | Utilisez ce prompt documentaire pour évaluer la structure d'un rapport de conseil, ses graphiques, son récit et son analyse des risques. | Tutoriel |
| [Rendre visibles les garde-fous](#case-75) | Utilisez cette note officielle pour comprendre la visibilité des garde-fous de Fable 5, les motifs de refus de l'API et le repli sur Opus. | Intégration |
| [Corriger la reconnaissance des modèles dans Claude Code](#case-76) | Utilisez cette note de version de Claude Code pour éviter les problèmes de noms de modèles Fable 5 et de reconnaissance du contexte. | Intégration |
| [Trois applications web dans Claude Code](#case-77) | Examinez Fable 5 dans Claude Code à travers plusieurs applications web générées dans cette démonstration pour débutants. | Démo |
| [Rilable, un créateur d'applications open source](#case-78) | Étudiez avec ce créateur d'applications open source l'usage de Fable 5 pour iOS, le web, les bacs à sable et le coût des tokens API. | Intégration |
| [Lancement de l'index d'agents de code DeepSWE](#case-79) | Utilisez l'index Artificial Analysis actualisé pour comparer Claude Fable 5 sur des tâches de codage agentique plus difficiles qui évitent les correctifs GitHub publics recyclés. | Evaluation |
| [Jeu d'analytics web DataEmpire](#case-80) | Transformez des analytics de site brutes en jeu rejouable en demandant à Claude Fable 5 d'associer visiteurs et jalons à des entités de jeu. | Integration |
| [Signal FrontierSWE sur 20 heures de tâche](#case-81) | Utilisez FrontierSWE comme preuve que Claude Fable 5 peut rester productif sur de très longues tâches d'ingénierie, pas seulement sur de courtes boucles de correction de bugs. | Evaluation |
| [Records CUDA sur KernelBench-Hard](#case-82) | Utilisez Claude Fable 5 pour la génération avancée de kernels CUDA lorsque vous avez besoin d'optimisation bas niveau, pas seulement de wrappers autour de bibliothèques existantes. | Evaluation |
| [Clone de landing page via capture Figma](#case-83) | Capturez la page d'un concurrent en couches Figma et laissez Claude Code avec Claude Fable 5 reconstruire structure, copywriting et système de marque au lieu de deviner à partir de captures d'écran. | Integration |
| [Clone de GTA 2 en deux heures](#case-84) | Combinez la génération de code de Claude Fable 5 avec un outillage d'assets séparé pour construire rapidement un jeu 3D jouable sans coder toute la stack à la main. | Tutorial |
| [Agent de triage de logs CloudWatch](#case-85) | Laissez un agent propulsé par Claude Fable 5 mâcher de très gros contextes de logs de service, inférer l'architecture puis se resserrer sur des pannes précises. | Integration |
| [Prédicteur de Coupe du monde en sandboxes](#case-86) | Placez plusieurs modèles frontier derrière des sandboxes isolées et laissez-les rechercher actualités live, blessures et contexte des cartons jaunes pour une application publique de prédiction. | Integration |
| [Cas de coût des refus WolfBench](#case-87) | Traitez le comportement de refus comme une vraie variable de benchmark lorsque vous chiffrez de longs runs autonomes sur Claude Fable 5. | Evaluation |
| [Suivi du cutoff d'accès API](#case-88) | Surveillez la disponibilité avec un script si votre workflow dépend d'un accès continu à un modèle frontier qui peut être limité ou retiré avec peu de préavis. | Integration |



### [🆕 Fable 5.5 : démonstrations de la communauté](#fable-5-5-community-demos)

| Cas | Type |
|---|---|
| [Une animation de renard avec son générée par code](#case-89) | Demo |
| [Une animation à partir d’un brief créatif ouvert](#case-90) | Demo |
| [Un site animé pour une entreprise de construction](#case-91) | Demo |
| [Une présentation automobile en Three.js](#case-92) | Demo |
| [Un jeu pour navigateur dans le style Minecraft](#case-93) | Demo |
| [Un pélican cycliste animé en Three.js](#case-94) | Demo |
| [Un pélican à vélo en SVG avec le prompt exact](#case-95) | Demo |
| [Un exemple d’animation de zèbre au galop](#case-96) | Demo |
| [Un indicateur TradingView avec exécution humaine](#case-97) | Demo |
| [Un point devient une courte histoire animée](#case-98) | Demo |
| [Superman à travers différents styles artistiques](#case-99) | Demo |
| [Le progrès humain dans un film animé musical](#case-100) | Demo |
| [Comparaison de vidéos de lancement avec Opus](#case-101) | Evaluation |
| [Relier visuellement des paroles et un événement](#case-102) | Demo |
| [Un personnage en voxels dans un décor flottant](#case-103) | Demo |
| [Une machine de Rube Goldberg en 3D](#case-104) | Demo |
| [Une interface de manette 3D sonore et animée](#case-105) | Demo |
| [Des personnages de comics présentés en JavaScript](#case-106) | Demo |
| [Updraft : mondes, boss et classement](#case-107) | Demo |
| [Conduire sur une carte de San Francisco](#case-108) | Demo |
| [Rédiger des prompts pour une scène Seedance](#case-109) | Demo |
| [Une vidéo explicative pour un collègue de bureau](#case-110) | Demo |
| [Un court prompt pour une animation changeant de style](#case-111) | Demo |
| [Visualiser le problème à trois corps](#case-112) | Demo |
| [Une galerie d’animations aux styles artistiques variés](#case-113) | Demo |
| [Compagnons robots et fourrure procédurale](#case-114) | Demo |
| [Un montage animé autour des mathématiques](#case-115) | Demo |
| [Une vidéo de paroles pour Your Woman](#case-116) | Demo |
| [Redessiner un clip musical en JavaScript](#case-117) | Demo |
| [Une animation sur le football chinois](#case-118) | Demo |
| [Présentation de retopologie d’une console portable](#case-119) | Demo |
| [Minecraft rencontre Pokémon](#case-120) | Demo |
| [Un film expliquant la fabrication d’un modèle de langage](#case-121) | Demo |
| [Un montage de moments forts autour d’Altman](#case-122) | Demo |
| [Le premier des Trente-Six Stratagèmes](#case-123) | Demo |
| [Modélisation, rigging et animation de jeu](#case-124) | Demo |
| [Un film sans paroles sur la mortalité infantile](#case-125) | Demo |
| [Une animation SVG de la glycolyse à l’éthanol](#case-126) | Demo |
| [Seize lancements simultanés de Starship](#case-127) | Demo |
| [Un test animé du pélican à vélo](#case-128) | Demo |
| [Une histoire des 150 prochaines années](#case-129) | Demo |
| [Une expérience indépendante de Humanity Walks](#case-130) | Demo |
| [Le film codé The Grader](#case-131) | Demo |
| [Le court métrage d’horreur Reawakening](#case-132) | Demo |
| [Une vidéo de 25 secondes sur l’amélioration de soi](#case-133) | Demo |
| [Une scène de château avec retour sur le coût](#case-134) | Evaluation |
| [Une publicité de lancement de marque en 40 secondes](#case-135) | Demo |
| [Une reprise de Rocketball](#case-136) | Demo |
| [Une comparaison de pagodes en voxels](#case-137) | Evaluation |
| [Présentation d’une Switch 3 imaginaire](#case-138) | Demo |
| [Des pages d’accueil avant et après](#case-139) | Evaluation |
| [La perspective intérieure imaginée d’une IA](#case-140) | Demo |
| [Motion design des paroles de Go](#case-141) | Demo |
| [Un second portfolio animé de 15 secondes](#case-142) | Demo |
| [Une revue guidée de l’implémentation d’un agent](#case-143) | Tutorial |
| [La danse de la mascotte Claude](#case-144) | Demo |
| [Les îles interactives des Sept Merveilles](#case-145) | Demo |
| [Un clip musical pour Propellerheads](#case-146) | Demo |
| [Comparaison d’animations Steamboat Willie](#case-147) | Evaluation |
| [Un film inspiré de Sanxingdui](#case-148) | Demo |
| [Une Bugatti Chiron avant et après](#case-149) | Evaluation |
| [Le film conceptuel GRAIN](#case-150) | Demo |
| [La galerie artistique Human in Transit](#case-151) | Demo |
| [Un court film visuel sur la Route de la soie](#case-152) | Demo |
| [Une présentation sur quatre transformations](#case-153) | Demo |
| [Comparer le ton d’anciens échanges](#case-154) | Evaluation |
| [Un test de mignonnerie avec un kakapo](#case-155) | Evaluation |
| [Spider-Man à travers dix époques de comics](#case-156) | Demo |
| [Une fiction horrifique sur les Illuminati](#case-157) | Demo |
| [Un film codé sur l’histoire de la science nucléaire](#case-158) | Demo |
| [Un film expliquant le revenu universel élevé](#case-159) | Demo |
| [Une explication animée du conflit Altman–Amodei](#case-160) | Demo |
| [Un clip musical avec la mascotte Claude](#case-161) | Demo |
| [Un zoom continu des quarks à l’univers](#case-162) | Demo |
| [Imaginer le monde en 2076](#case-163) | Demo |
| [Une chronologie des bâtiments de Lower Manhattan](#case-164) | Demo |
| [Une animation sur l’écriture ossécaille](#case-165) | Demo |
| [Une autre traversée de l’histoire de l’art](#case-166) | Demo |
| [Une œuvre audiovisuelle codée autour de Seikilos](#case-167) | Demo |
| [Comparaison d’animations de jet](#case-168) | Evaluation |
| [Un film de présentation du modèle](#case-169) | Demo |
| [Un prototype de jeu de cartes postapocalyptique](#case-170) | Demo |
| [L’animation de bureau The Late Byte](#case-171) | Demo |
| [Animation des paroles de Queens of the Stone Age](#case-172) | Demo |
| [Une scène narrative Three.js partagée](#case-173) | Demo |
| [Un moonwalk à travers des scènes historiques](#case-174) | Demo |
| [Des animations graphiques guidées par un prompt détaillé](#case-175) | Demo |
| [L’interface d’un site de location](#case-176) | Demo |
| [Un film créatif sur l’AGI](#case-177) | Demo |
| [L’histoire de l’art avec une intrigue de chat](#case-178) | Demo |
| [Un prototype de combat et une scène en voxels](#case-179) | Demo |
| [Une chronologie des mèmes d’Internet](#case-180) | Demo |
| [Des particules animées à partir d’une ligne](#case-181) | Demo |
| [L’animation Kung-Fu Boy](#case-182) | Demo |
| [Un débat animé sur le détroit d’Ormuz](#case-183) | Demo |
| [Un essai de style SVG avec une licorne](#case-184) | Demo |
| [Une animation saisonnière d’Halloween](#case-185) | Demo |
| [Un barbare et une couverture avec Blender CLI](#case-186) | Demo |
| [Une journée dans la vie de Claude](#case-187) | Demo |
| [L’histoire de l’humanité en 3D](#case-188) | Demo |
| [Un montage rapide de motion design](#case-189) | Evaluation |
| [Une création 3D complexe et libre](#case-190) | Demo |
| [Un combat animé de bonshommes allumettes](#case-191) | Demo |
| [Une séquence d’interface animée en un prompt](#case-192) | Demo |
| [Une animation fictive sur SCP-8517](#case-193) | Demo |
| [Une animation d’automne à l’aquarelle](#case-194) | Demo |
| [Une scène de poupée procédurale](#case-195) | Demo |
| [Un pélican à vélo rendu dans le navigateur](#case-196) | Demo |
| [L’univers se regarde lui-même](#case-197) | Demo |
| [Un essai indépendant d’animation de jet](#case-198) | Demo |
| [Un premier montage animé libre](#case-199) | Demo |
| [Une civilisation rendue par code](#case-200) | Demo |
| [Comparaison d’un zoom de la puce au serveur](#case-201) | Evaluation |
| [Un projet personnel d’animation de voyage lunaire](#case-202) | Demo |
| [Comparaison de scènes japonaises en voxels](#case-203) | Evaluation |
| [Le court audiovisuel Steaming the Frontier](#case-204) | Demo |
| [Superman dans plusieurs styles artistiques](#case-205) | Demo |
| [Un prototype de combat de boss de type Cupcake](#case-206) | Demo |
| [Un voilier sous un soleil changeant](#case-207) | Demo |
| [Une vidéo des nouveautés de Paracortex et Pi](#case-208) | Demo |
| [Une promotion du site Curio 2.0](#case-209) | Demo |
| [Une histoire 3D imaginaire de Hugging Face](#case-210) | Demo |
| [Claude pour Chrome dans JS Paint](#case-211) | Demo |
| [Un pélican à vélo en SVG statique](#case-212) | Demo |
| [BlockBench MCP avec une compétence Minecraft](#case-213) | Demo |
| [Dig Dug dans un seul fichier HTML](#case-214) | Demo |
| [Une pieuvre mécanique en SVG](#case-215) | Demo |
| [Humanity Walks à travers les styles artistiques](#case-216) | Demo |
| [Une scène libre de trou noir](#case-217) | Demo |
| [Comparaison d’animations de méduses aurorales](#case-218) | Evaluation |
| [Un SVG Nintendo Switch avec assemblage et démarrage](#case-219) | Demo |
| [La scène 3D interactive The Loom](#case-220) | Demo |
| [Reels de motion design avec le même prompt](#case-221) | Evaluation |
| [Un décor plus propre mais moins profond](#case-222) | Evaluation |
| [Des résultats mitigés pour une scène japonaise](#case-223) | Evaluation |
| [Comparaisons de manettes SVG](#case-224) | Evaluation |
| [Une scène d’appareil industriel](#case-225) | Demo |
| [Reconstruction d’une créature géante à carapace et branchies](#case-226) | Demo |
| [Une manette GameCube en deux prompts](#case-227) | Demo |
| [Une capture adaptée à un post X](#case-228) | Demo |
| [Une scène sakura en voxels avant et après](#case-229) | Evaluation |
| [Le prototype d’interface textile SHADERKIN](#case-230) | Demo |
| [Une animation partagée d’interface à horloge dorée](#case-231) | Demo |
| [Le récit Before There Was Anything](#case-232) | Demo |
| [Un vortex partagé de particules bleues](#case-233) | Demo |
| [Une interface à plusieurs panneaux après deux révisions](#case-234) | Demo |
| [Des animaux empilés dans une scène rendue](#case-235) | Demo |
| [Quatre essais de RPG en monde ouvert comparés](#case-236) | Evaluation |
| [Deux animations frontend comparées](#case-237) | Evaluation |
| [Un film de robot moussu généré par code](#case-238) | Demo |
| [Une simulation de port à conteneurs revisitée](#case-239) | Demo |
| [Une scène de piste d’aéroport revisitée](#case-240) | Demo |
| [Un pélican à vélo dans des mondes 3D abstraits](#case-241) | Demo |
| [Une scène de voilier historique](#case-242) | Demo |
| [Comparaisons de cyclistes et d’allures avec Carbon](#case-243) | Evaluation |
| [Présentation d’une bouteille de boisson gazeuse](#case-244) | Demo |
| [Mouvements de pélican comparés à Astra](#case-245) | Evaluation |
| [Un brief de motion design pour animations codées](#case-246) | Tutorial |
| [Un portrait voxel d’après une photo](#case-247) | Demo |
| [Des pélicans volants comparés à Opus](#case-248) | Evaluation |
| [La scène web de pélican Morning Ride](#case-249) | Demo |
| [Un même prompt avec des styles différents](#case-250) | Evaluation |
| [Une composition avec pélican, vélo et cheval](#case-251) | Demo |
| [Une scène isométrique inspirée d’un tweet de référence](#case-252) | Demo |
| [Gros plans mécaniques d’un vélo de pélican](#case-253) | Demo |
| [Un vélo qui roule sur un pélican](#case-254) | Demo |
| [Styles SVG de pélican comparés à Carbon](#case-255) | Evaluation |
| [Un oiseau bleu de dessin animé à vélo](#case-256) | Demo |
| [Une capture de pélican sur une route forestière](#case-257) | Demo |
| [Un combat de bonshommes allumettes comparé à Carbon](#case-258) | Evaluation |
| [Une référence SVG de pélican issue de premiers tests](#case-259) | Demo |
| [Une référence de pélican dans des tests SVG comparés](#case-260) | Evaluation |
| [Détails de vélos SVG comparés à Carbon](#case-261) | Evaluation |
| [Une implantation dans un canyon en 3D](#case-262) | Demo |
| [Détails de manettes comparés à Opus](#case-263) | Evaluation |
| [Un workflow hebdomadaire d’audit SEO de site](#case-264) | Integration |
| [Réutiliser des éléments Fable dans du motion design Opus](#case-265) | Integration |
| [Une application de mandalas et formes géométriques](#case-266) | Demo |
| [Un cycliste sur un vélo en Three.js](#case-267) | Demo |
| [Instantané de l’évaluation FrontierCS 2](#case-268) | Evaluation |
| [Comparaison d’animations de zèbres entre trois modèles](#case-269) | Evaluation |
| [Critiquer la lisibilité de longs textes japonais](#case-270) | Evaluation |
| [Un PowerPoint technique guidé par des exemples](#case-271) | Evaluation |
| [Comparer la cohérence musicale](#case-272) | Evaluation |
| [Une fin de tâche prématurée et des designs moins bons](#case-273) | Limit |
| [Une œuvre de calmar jugée dérangeante](#case-274) | Limit |
| [Du motion design à l’esthétique de plan technique](#case-275) | Demo |
| [Oiseaux et poissons dans un paysage sakura en voxels](#case-276) | Demo |
| [Un retour d’échec sur la génération de personnages](#case-277) | Limit |
| [Un SVG de pélican avec durée et coût](#case-278) | Evaluation |
| [Coder à distance sur téléphone avec Claude Code](#case-279) | Integration |
| [La Voie lactée au-dessus d’un lac alpin](#case-280) | Demo |
| [Saut de baleine avec eau et son procéduraux](#case-281) | Demo |
| [Mouvement de zèbres comparé entre quatre modèles](#case-282) | Evaluation |
| [Recherche de créateurs en langage naturel dans Lightreel](#case-283) | Demo |
| [Un navire volant au-dessus d’une mer de nuages](#case-284) | Demo |
| [Cœur mécanique avec coupe animée](#case-285) | Demo |
| [Jardin de pagode voxel flottant à explorer](#case-286) | Demo |
| [Une aventure océanique réalisée par huit équipes](#case-287) | Demo |
| [Présentation interactive d’une hypercar](#case-288) | Demo |
| [Naissance d’un arbre de vie](#case-289) | Demo |
| [Château ambulant aux mécanismes internes fonctionnels](#case-290) | Demo |
| [Un personnage-toast et un scarabée mécanique](#case-291) | Demo |
| [Un gardien de phare dans la tempête](#case-292) | Demo |
| [Une créature marine dans une ville côtière](#case-293) | Demo |
| [Course sur tapis comparée entre trois modèles](#case-294) | Evaluation |
| [Un camion se transforme en robot](#case-295) | Demo |
| [Images d’animation de Fable et Hunyuan](#case-296) | Evaluation |
| [Une animation sur le partage de la lumière](#case-297) | Demo |
| [Un village voxel entre les montagnes](#case-298) | Demo |
| [Composition pélican-éléphant comparée entre quatre modèles](#case-299) | Evaluation |
| [Combat anime au sabre avec images d’impact](#case-300) | Demo |
| [Cerf courant comparé entre quatre modèles](#case-301) | Evaluation |
| [Un robot traverse une ville inondée](#case-302) | Demo |
| [Une épée Blender et son film de présentation](#case-303) | Demo |
| [Animation du village pixelisé Lantern Isle](#case-304) | Demo |
| [Démo Pause de montage de vidéos de jeu](#case-305) | Demo |
| [Un pélican à vélo le long du littoral](#case-306) | Demo |

<a id="coding-and-code-generation"></a>
## 💻 Codage et génération de code

<a id="case-1"></a>
### Case 1: [Workflow Cursor en plusieurs étapes](https://x.com/AlicanKiraz0/status/2064487347605918180) (par [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Utilisez Fable 5 comme étape de revue de plan et de critique dans un workflow Cursor multi-modèles, puis confiez l'implémentation et les révisions à des modèles moins chers ou spécialisés.**

Si l'on regarde le score final entre Fable 5 et GPT 5.5, l'écart est très faible. Ma recommandation d'utilisation, humblement, est la suivante : dans les plateformes IDE comme Cursor qui prennent en charge les modèles hybrides, utilisez un workflow par étapes.

Phase 1 : pour la revue de code et la première phase d'inspection du projet, tout en réchauffant le contexte, utilisez l'un de GPT 5.5 High, Minimax M3, Kimi K2.6 ou Composer 2.5.

Phase 2 : pour préparer le plan du projet, utilisez GPT 5.5 Very High ou Opus 4.8.

Phase 3 : pour analyser le plan du projet, utilisez Fable 5 ; laissez-le identifier les parties défaillantes du plan. Pour les révisions, utilisez GPT 5.5 Very High.

Phase 4 : pour implémenter le plan, utilisez Minimax M3, Deepseek v4 Max, Composer 2.5 ou Sonnet 4.6.

Phase 5 : pour la revue finale et pour vérifier si l'implémentation a suivi le plan, utilisez GPT 5.5 High.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [Recréation de GitHub à partir d'une capture d'écran](https://x.com/coldopn/status/2064435234465087638) (par [@coldopn](https://x.com/coldopn))

**Collez une capture d'écran produit dans un outil de codage agentique et demandez à Fable 5 de recréer l'interface avec des fonctionnalités opérationnelles.**

🚨 Anthropic Fable 5 vient de répliquer GITHUB à partir d'une CAPTURE D'ÉCRAN !!

Tout ce que j'ai fait, c'est coller une capture de l'interface GitHub dans Kilo Code et lui demander de recréer GitHub avec de vraies fonctionnalités.

Il a codé pendant 10 minutes et dépensé $4.07.

Le résultat était une réplique fonctionnelle de GitHub : https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [Simulation de trou noir avec un seul prompt](https://x.com/deveshcodes_/status/2064437742189379745) (par [@deveshcodes_](https://x.com/deveshcodes_))

**Donnez à Fable 5 un prompt détaillé de creative coding et demandez-lui de produire une visualisation physique Three.js autonome.**

@claudeai a créé en one-shot une simulation en temps réel de lentille gravitationnelle de trou noir dans Three.js avec Claude Fable 5.

Elle incluait la lentille gravitationnelle, un disque d'accrétion doppler-boosté, la sphère de photons, l'aberration chromatique et un champ d'étoiles procédural.

Résultat : 60 fps, un seul fichier HTML, un seul prompt.

Le nouveau standard est fou 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [Web OS façon macOS en one-shot](https://x.com/intheworldofai/status/2064421915347812672) (par [@intheworldofai](https://x.com/intheworldofai))

**Demandez à Fable 5 un web OS complet en fichier unique et laissez-le construire en une passe le shell UI, les apps, les interactions, l'audio et le comportement de jeu intégré.**

🚨 Claude Fable 5 vient de construire en une seule tentative un web OS complet façon macOS, et il est allé plus loin que la plupart des modèles.

Un seul fichier HTML, CSS + JS intégrés.

À partir d'un seul prompt, il a construit :

- barre de menu macOS + dock
- fenêtres d'app redimensionnables et déplaçables
- explorateur de fichiers fonctionnel
- terminal opérationnel + maquette de navigateur
- icônes de bureau SVG + notifications
- app Réglages, thèmes et écran de démarrage
- lecteur audio entièrement fonctionnel avec vraie synthèse et aucun fichier externe
- clone de Minecraft jouable dans le bureau

Tout a été généré en une passe avec presque aucune correction.

Le lecteur audio opérationnel plus le vrai clone de Minecraft, c'est quelque chose que je n'avais encore vu aucun autre modèle réussir. La génération frontend/UI de Fable 5 devient ridicule.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [Construction de Spawn 5.0 avec 1 687 prompts](https://x.com/jsnnsa/status/2064420561078693941) (par [@jsnnsa](https://x.com/jsnnsa))

**Utilisez Fable 5 comme partenaire d'ingénierie sur de longues sessions et de nombreux prompts, avec un humain qui passe de l'architecture au jugement de qualité de sortie.**

claude fable 5 est disponible.

spawn 5.0 a été construit avec lui :

- 1 687 prompts
- 102 sessions
- Mon travail est passé de l'architecture au jugement du goût

Ce que nous avons construit, et qui aurait pris au moins un mois chacun avec toute une équipe sur Opus :

- Un moteur physique from scratch, Mantle, qui rivalise avec Rapier et a pu être testé en une journée comme fil secondaire
- Éclairage clustered froxel : de 8 lumières à plus de 1 000 lumières entièrement dynamiques
- GI diffuse temps réel sur WebGPU, sur votre téléphone
- VFX GPU à un million de particules avec une architecture shader au-delà de ce que livrent Unreal et Unity
- Netcode à l'échelle MMO
- Une app native iOS alpha

Le tout a pris environ une semaine. Tout fonctionne sur mobile. La liste n'inclut pas la moitié de ce qui a été livré ; le changelog complet est dans le fil.

La partie que les benchmarks ne montreront pas : ce modèle a une personnalité merveilleuse. Il est réellement drôle. J'ai ri si fort que j'en ai pleuré plusieurs fois en plein rewrite de physique. Le génie et le caractère ne sont pas des fonctionnalités séparées.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [Revue d'une grande pull request avec constats](https://x.com/ryanrhughes/status/2064411147076534705) (par [@ryanrhughes](https://x.com/ryanrhughes))

**Pointez Fable 5 vers une grande pull request et demandez-lui d'examiner la justesse, les faux positifs, les vrais bugs et les problèmes de finition.**

J'ai lâché Fable 5 sur la revue d'une seule PR (74 fichiers / +3 705 / -1 246) pour voir comment il s'en sortirait. Il a tourné 34 min, consommé 42 % de ma session de 5 h, produit 16 constats de « correctness », et trouvé :

- 2 faux positifs à l'air inquiétant
- 3 vrais bugs de correctness d'audit
- environ 5 vrais petits problèmes d'UX/finition
- tout un lot d'avis de nettoyage

C'était trop dangereux pour être publié ?

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 Agents et automatisation longue durée

<a id="case-7"></a>
### Case 7: [Revue d'un workflow relais sur horizon long](https://x.com/JJEnglert/status/2064469635190170105) (par [@JJEnglert](https://x.com/JJEnglert))

**Utilisez Fable 5 pour des travaux ambitieux sur horizon long : refontes de sites, pipelines de contenu programmatiques, adaptation de voix, revue de sécurité et contrôles qualité finaux.**

La version courte de ma revue de Claude Fable 5 : j'ai dépensé un milliard de tokens pour tester Claude Fable 5 et j'ai eu l'impression d'avoir un avantage déloyal.

Je juge au test visuel : je mets un modèle dans du vrai travail et j'observe. Est-ce qu'il me fait gagner des heures ou est-ce qu'il m'en coûte ? Est-ce qu'il attrape ce que j'ai raté ? Est-ce qu'il ressemble à un partenaire ou à un outil qu'il faut surveiller ?

C'est le premier modèle depuis longtemps qui réussit sur toutes les dimensions qui comptent, et pas de peu.

Construction : je reconstruisais notre site Tenex. Il était très custom et très difficile. GPT 5.5 et Claude 4.8 n'arrivaient pas à le résoudre seuls. Même avec les fichiers Figma en référence, ils plafonnaient autour de 85-90 %.

Puis Fable 5 a tout examiné, a dit qu'il pouvait faire mieux, est allé directement à la source Webflow originale, a téléchargé chaque asset et a presque tout refait en one-shot.

Ensuite, je lui ai fait construire un second site entièrement nouveau de 80 pages from scratch en un week-end. C'est un travail que j'aurais facturé $50k en tant qu'agence.

Il a aussi assemblé une usine complète de clips programmatiques :

- HeyGen
- ElevenLabs
- Cloudflare
- Un VPS

Le pipeline trouve des sujets, écrit des scripts, monte les vidéos, ajoute de la musique et publie sur les réseaux sociaux. Il a tourné tout seul pendant de longues périodes et s'est même construit un système de webhooks pour surveiller les rendus.

Écriture : il a répliqué notre document de voix de marque presque à l'identique, puis a conservé cette voix sur 80 pages de fonctionnalités, études de cas et articles sans dériver vers le défaut plat de l'IA.

Sécurité : deux modèles frontier avaient travaillé dans un grand dépôt et validé le code. Fable 5 a trouvé un bug sérieux et bien caché dès son premier passage et l'a corrigé sur place.

Le moment humain : je lui ai posé une question en attendant un cron job. Il a répondu, puis a ajouté de lui-même qu'il me restait environ 10 minutes et qu'il me préviendrait quand ce serait terminé. Je n'avais jamais demandé le minuteur.

Le vrai bémol : vous sentez le compteur plus qu'avec n'importe quel autre modèle. Anthropic dit qu'il est token-intensive par conception. Faites-le donc tourner comme un relais : réfléchissez avec Fable 5, construisez avec un modèle moins cher, relisez avec Fable 5.

Verdict : avoir accès à plus d'intelligence que la personne à côté de vous, c'est l'avantage. Fable 5 est le premier modèle qui rend cela réel. Même aux pleins tarifs frontier, il a dégagé un profit.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [Diagnostic d'une panne d'infrastructure et ouverture d'une PR de correction](https://x.com/ayushagarwal/status/2064422467557564862) (par [@ayushagarwal](https://x.com/ayushagarwal))

**Donnez à Fable 5 accès à des indices d'infra comme les logs, les erreurs de base de données et les digests d'images, puis demandez-lui de diagnostiquer la panne et de préparer le correctif.**

claude fable 5 est sacrément, sacrément bon !!!!

Il vient de diagnostiquer une panne que je n'arrivais même pas à décrire correctement dans une infra secondaire auto-hébergée.

Il a lu les logs de pods, interrogé les logs d'erreur Cloud SQL, comparé les digests d'images et découvert que Kubernetes exécutait une image cachée vieille de 3 mois contre une base de données récemment migrée.

Puis il a ouvert la PR de correction.

Des minutes, pas des heures. Aucune recherche web. 🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 Jeux et démos interactives

<a id="case-9"></a>
### Case 9: [Dino Runner avec suivi du doigt](https://x.com/ai_for_success/status/2064413182396108932) (par [@ai_for_success](https://x.com/ai_for_success))

**Demandez à Fable 5 de construire un jeu navigateur qui utilise le suivi du doigt comme mécanique d'entrée.**

J'ai demandé à Fable 5 de construire un jeu Dino runner avec suivi du doigt.

Il a créé le jeu finger runner en one-shot en environ 11 à 12 minutes, consommé autour de 914K tokens et tout implémenté en seulement 629 lignes de code.

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [Jeu de course construit avec deux phrases](https://x.com/kieradev/status/2064482704763085202) (par [@kieradev](https://x.com/kieradev))

**Donnez à Fable 5 un prompt de jeu très court et laissez-le générer cartes, modes, musique, UI et assets de jeu en une seule exécution.**

Claude Fable 5, 40 % de l'usage Max 5x.

Jeu complet de type Mario Kart 64 à partir d'un prompt de 2 phrases.

Fable 5 a géré toute la décoration, les modèles de personnages, 4 cartes, la musique, les trois modes de jeu et l'UI en un seul shot, en environ 15 minutes.

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Minecraft terminal installable en Rust](https://x.com/vikvang1/status/2064500731848319303) (par [@vikvang1](https://x.com/vikvang1))

**Exécutez Fable 5 via un harness de codage terminal et demandez-lui de construire un jeu terminal Rust installable.**

J'ai laissé Claude Fable 5 cuisiner pendant une heure avec le harness de Warp.

Il a créé une version TUI de Minecraft qui rend directement dans votre terminal, entièrement construite en Rust.

Commande d'installation : cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [Clone de Minecraft avec temps et coût](https://x.com/ydamitcodes/status/2064536076518363353) (par [@ydamitcodes](https://x.com/ydamitcodes))

**Utilisez un prompt pour demander à Fable 5 un clone jouable façon Minecraft, puis évaluez le temps, le coût, le volume de code et la couverture fonctionnelle.**

@claudeai Fable 5 m'a construit un clone de Minecraft en 37 minutes.

Un prompt. Environ 3K lignes de code. $12 de coûts API.

Il incluait biomes, grottes, minerais, jour/nuit, mobs, tout.

Minecraft a pris 2 ans à Notch.

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 Visuel, design, vidéo et 3D

<a id="case-13"></a>
### Case 13: [Prompt complet reproductible pour un email ecommerce](https://x.com/ecomchasedimond/status/2064454139225297091) (par [@ecomchasedimond](https://x.com/ecomchasedimond))

**Donnez à Fable 5 un brief créatif complet pour une maquette d'email de marque, incluant les sections exactes, exigences produit, direction visuelle et contraintes.**

Claude Fable 5 a créé ceci avec un seul prompt et sans retouche.

Voici le prompt complet que j'ai utilisé :

Crée une maquette d'email ecommerce pleine longueur, haute et verticale pour MVMT, une marque moderne de montres et d'accessoires destinée aux millennials.

Conçois un email DTC premium très réaliste, élégant, poli, minimal, à tendance masculine et éditorial. L'image finale doit ressembler à une vraie capture d'email ecommerce conçue par un designer, pas à une affiche, pas à une landing page, ni à un template générique.

Vibe de marque : moderne California-cool, jeune, assurée, propre, aspirationnelle, stylée et élevée. Le design doit paraître proche du luxe tout en restant accessible.

Mets ces produits en avant :

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Style visuel :

- design ecommerce premium épuré
- mise en page éditoriale raffinée
- photographie produit réaliste
- imagerie lifestyle subtile
- hiérarchie forte
- typographie sans-serif nette
- espacements généreux
- ombres subtiles
- palette moderne et retenue

Palette de couleurs : noir, blanc, anthracite, gris chaud, pierre, beige doux, tons de métal brossé et accents discrets atténués. Garde la palette neutre et premium.

Direction créative importante : cela doit ressembler à une campagne email de marque horlogère soignée avec un fort goût design. Priorise le réalisme, l'élégance et la clarté. Fais en sorte que cela ressemble à quelque chose que MVMT pourrait vraiment envoyer.

Construis l'email dans cet ordre :

1. Barre promo supérieure : une fine barre noire ou anthracite foncé sur toute la largeur en haut avec un petit texte en majuscules : “FREE SHIPPING OVER $75 + EASY RETURNS”.

2. En-tête : un en-tête blanc épuré avec le wordmark/logo MVMT à gauche et des liens de navigation minimaux à droite ou centrés : WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS.

3. Section hero : une section hero premium avec un fort équilibre visuel.

Utilise un titre audacieux : “BUILT TO GET NOTICED”.

Ajoute un court texte de soutien sur des garde-temps et accessoires modernes conçus pour élever le style du quotidien.

Ajoute un bouton CTA sombre arrondi : “SHOP WATCHES”.

L'image hero doit inclure :

- une image dominante de montre premium
- une imagerie lifestyle de luxe subtile
- un modèle masculin stylé ou une scène lifestyle masculine mode
- un éclairage moderne et une composition propre

4. Section collection en vedette : ajoute un titre de section centré : “THREE WAYS TO WEAR MVMT”. En dessous, affiche trois cartes produit ou blocs image propres présentant :

- Mulholland
- Odyssey II Automatic
- Cali Diver

Chaque bloc doit inclure :

- image produit
- nom du produit
- courte description d'une ou deux lignes

Garde cette section symétrique, soignée et premium.

5. Bannière accessoires : ajoute une section split raffinée intitulée “FINISH THE LOOK”. Mets en avant Signature Watch Bands. Montre une imagerie close-up premium de bracelets de montre ou de bracelets interchangeables. Inclue un court texte de soutien et un bouton CTA sombre : “SHOP ACCESSORIES”.

6. Tuiles promo éditoriales : ajoute deux tuiles promotionnelles côte à côte avec un design mené par l'image.

Titre de la première tuile : “FOR DAILY WEAR”.

Titre de la deuxième tuile : “FOR STATEMENT DAYS”.

Chaque tuile doit avoir un texte court et un petit CTA : “SHOP NOW”.

Ces tuiles doivent ressembler à des moments éditoriaux de marque, pas à des boîtes de soldes génériques.

7. Rangée shoppable : ajoute une section intitulée “IN ROTATION NOW”. Affiche une rangée ou grille propre de 4 produits avec :

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Chaque élément doit inclure :

- image produit isolée
- nom du produit
- petit lien ou bouton “SHOP”

8. Signature de marque : ajoute un bloc de message centré avec le titre : “DESIGNED TO MOVE WITH YOU”. Inclue une courte phrase sur des montres, lunettes et accessoires soigneusement conçus pour la vie quotidienne.

9. Footer : crée un footer de marque réaliste noir ou anthracite avec :

- logo MVMT
- liens boutique
- liens entreprise
- liens support
- icônes sociales
- petit texte légal et livraison

Direction typographique : utilise une typographie sans-serif bold condensée ou moderne pour les grands titres, et une sans-serif propre pour le corps de texte. Les titres doivent être nets, modernes et fashion-forward. Le body copy doit paraître réaliste et globalement lisible.

Direction photo : utilise une photographie produit premium avec reflets réalistes, matériaux polis, ombres douces et surfaces propres. La photographie lifestyle doit paraître élevée, moderne et orientée mode.

Règles de composition :

- format email vertical haut
- séparation claire des sections
- proportions réalistes d'email
- hiérarchie forte
- texte majoritairement lisible
- espacements premium
- alignement intentionnel
- mélange équilibré d'imagerie produit et lifestyle

À éviter :

- style collage désordonné
- esthétique scrapbook ludique
- design trop coloré
- vibe de template bon marché
- imagerie cartoon
- mises en page encombrées
- faux éléments d'UI
- composition façon affiche
- chaos promotionnel excessif

Sortie : une maquette de design d'email ecommerce pleine longueur, composée verticalement, très réaliste, pour MVMT, avec une sensation premium, propre, polie, moderne, éditoriale et prête à être présentée.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [Benchmark d'horloger avec échappement à ancre suisse](https://x.com/quanghuynt14/status/2064509430650065278) (par [@quanghuynt14](https://x.com/quanghuynt14))

**Utilisez Fable 5 sur un benchmark de simulation mécanique et demandez-lui d'implémenter, vérifier et itérer sur la justesse physique.**

J'ai donc donné à Fable 5 le benchmark d'horloger : un mouvement complet à ancre suisse dans Three.js.

Vrais rapports d'engrenage (18 000 bph), échappement fonctionnel, spiral qui respire, et les aiguilles indiquent l'heure réelle.

Il a vérifié son propre travail avec la vision, en boucle, jusqu'à terminer.

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Scène Three.js de l'appartement de Friends](https://x.com/scottstts/status/2064464351906673029) (par [@scottstts](https://x.com/scottstts))

**Demandez à Fable 5 de transformer un plan d'étage et une référence de scène en environnement Three.js navigable.**

Bon sang !!!

Fable 5 :

dans @threejs, crée une scène 3d navigable en vue première personne de l'iconique appartement de Monica dans la série Friends, correctement basée sur ce plan d'étage, fidèle à l'apparence et au ressenti originaux, avec un éclairage chaud

C'est de très loin LE MEILLEUR résultat que j'ai vu sur ce test !

Ce html unique m'a coûté $12, mais le résultat est superbe !

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [Simulation du système solaire avec prompt et URL](https://x.com/tetumemo/status/2064477582930989357) (par [@tetumemo](https://x.com/tetumemo))

**Utilisez Fable 5 pour construire une simulation astronomique à partir des principes physiques, en itérant jusqu'à ce que la simulation et la sortie publique soient prêtes.**

Claude Fable 5 est intense.

Comme il semble fort en simulations physiques, je lui ai demandé :

'Construis une simulation du système solaire en dérivant le mouvement orbital des planètes à partir des principes fondamentaux de la physique et en l'utilisant pour prédire les éclipses solaires.'

Après quelques allers-retours, c'était terminé.

C'est incroyablement amusant.

Le prompt terminé et l'URL publique sont liés ci-dessous.

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 Documents, travail de connaissance et recherche

<a id="case-17"></a>
### Case 17: [Preuves Stripe et workflows scientifiques](https://x.com/AndrewCurran_/status/2064413892378546418) (par [@AndrewCurran_](https://x.com/AndrewCurran_))

**Utilisez ceci comme preuve pour les affirmations sur la migration d'entreprise et les workflows scientifiques, pas comme prompt à copier-coller.**

Citations de la publication d'aujourd'hui :

Avec Mythos 5, des experts internes en conception de protéines ont accéléré des parties du processus de conception de médicaments d'environ dix fois.

Dans un exemple, Mythos 5, avec des outils de conception de protéines et de bioinformatique mais sans assistance humaine, a égalé ou dépassé des opérateurs humains qualifiés.

Il a exécuté des tâches normalement accomplies par un scientifique : choisir des sites de liaison, sélectionner et lancer des outils de conception de protéines, et récupérer après des échecs.

Pendant les premiers tests, Stripe a rapporté que Fable 5 avait compressé des mois d'ingénierie en jours. Dans une base de code Ruby de 50 millions de lignes, le modèle a réalisé en une journée une migration à l'échelle de toute la base qui aurait autrement pris plus de deux mois de travail manuel à toute une équipe.

Mythos 5 a aussi produit de façon constante des hypothèses scientifiques nouvelles et convaincantes.

Dans des comparaisons aveugles face à face contre des modèles de classe Opus, les scientifiques ont préféré les hypothèses de biologie moléculaire de Mythos environ 80 % du temps et en ont avancé plusieurs vers une évaluation expérimentale.

Une hypothèse de Mythos, un nouveau mécanisme pour une protéine d'E. coli, a été corroborée dans une étude d'un laboratoire indépendant.

Mythos 5 a mené une recherche génomique originale pendant plus d'une semaine de travail largement autonome.

Il a assemblé des données unicellulaires pour des millions de cellules sur 138 espèces animales et conçu puis entraîné un modèle de machine learning personnalisé pour identifier des cellules jouant le même rôle chez des organismes éloignés.

Avec seulement une contribution humaine de haut niveau, le modèle entraîné a dépassé un modèle récent publié dans Science tout en étant 100 fois plus petit.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [Mémo de politique publique et workflows de suivi des modifications](https://x.com/manaltdan/status/2064414129440608427) (par [@manaltdan](https://x.com/manaltdan))

**Utilisez Fable 5 pour le travail qualitatif long format sur documents : suivi des modifications, tri de commentaires et éditions guidées par transcription.**

Fable 5 est le premier modèle que j'ai trouvé constamment utile pour du travail qualitatif de plus longue durée, comme la rédaction d'analyses de politique publique.

Entre ses capacités et des outils comme Wispr Flow, je commence à me rapprocher du gain de productivité dont j'entends depuis longtemps les codeurs parler.

Trois cas d'utilisation paraissent bien meilleurs qu'avant :

- Demander à Claude de lire intégralement un long mémo de politique publique et de renvoyer des modifications suivies : retouches de fluidité, commentaires remettant en question des affirmations fragiles et sources potentielles.
- Dans Projects, capturer un grand ensemble de commentaires et demander à Claude de recommander si et comment traiter chacun.
- Coller dans Claude la transcription d'une réunion à propos d'un document, puis demander à Claude d'appliquer en suivi des modifications les changements discutés dans la réunion et dans Slack, avec le contexte ajouté en commentaires.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [Prompt de recherche approfondie et résultat](https://x.com/naoyafujiwara/status/2064470780373811637) (par [@naoyafujiwara](https://x.com/naoyafujiwara))

**Posez à Fable 5 une question de type recherche et évaluez s'il peut produire une longue réponse structurée et historiquement fondée.**

Claude Fable 5 Max est devenu disponible ce matin, donc je l'ai essayé. Il semble très profond sous la surface, tandis que la sortie visible est très polie.

Question : Si les « 30 années perdues » du Japon ont commencé exactement il y a 30 ans à partir d'aujourd'hui, qu'étaient-elles exactement, pourquoi ont-elles eu lieu et comment affecteront-elles le monde à partir de cette année ?

Réponse : Traiter les 30 années perdues comme commençant non pas avec l'effondrement conventionnel de la bulle en 1991, mais exactement il y a 30 ans en 1996, permet d'atteindre l'essence du problème.

Statistiquement, le Japon a vraiment commencé à « perdre » à ce moment :

- La population en âge de travailler a culminé en 1995 à 87,16 millions.
- 1996 a été la dernière année où les naissances sont restées dans la fourchette de 1,2 million.
- Les salaires et le PIB nominal ont culminé en 1997.

Si l'effondrement de la bulle était la blessure, 1996 est le moment où la blessure a commencé à s'infecter.

Événements en 1996 :

- Adoption de la loi de renflouement des sociétés de prêts immobiliers, qui a injecté 685 milliards de yens de fonds publics et est devenue l'origine de la méfiance publique envers les banques et de la résistance aux renflouements.
- Décision du cabinet Hashimoto d'augmenter la taxe à la consommation à 5 %.
- Annonce du Big Bang financier, et la reconstruction budgétaire devient une politique nationale.

En avril 1997, la hausse de la taxe à la consommation, la fin des réductions fiscales spéciales et la hausse des charges d'assurance sociale ont ajouté ensemble environ 9 billions de yens de charge publique. Puis la crise monétaire asiatique a frappé en été.

En novembre, Sanyo Securities a provoqué le premier défaut d'après-guerre sur le marché call, gelant les marchés financiers à court terme. Hokkaido Takushoku Bank et Yamaichi Securities se sont effondrées l'une après l'autre.

À partir de 1998, le Japon est entré dans une déflation et un resserrement du crédit à grande échelle, et les suicides ont dépassé 30 000.

Le résultat sur les 30 années suivantes :

- Le PIB nominal a stagné autour de 500 billions de yens pendant un quart de siècle.
- La part du Japon dans le PIB mondial est passée d'environ 18 % à moins de 4 %.
- Les salaires moyens ont culminé en 1997 puis ont baissé ou stagné.
- L'emploi non régulier est passé d'environ 20 % à près de 40 %.
- Les naissances sont passées d'environ 1,2 million à environ 690 000 en 2024.
- Les taux directeurs sont restés proches de zéro après être passés sous 1 % en 1995.
- Les obligations d'État en circulation sont passées d'environ 240 billions de yens à plus de 1 100 billions de yens.
- Le Nikkei a mis 34 ans, jusqu'en février 2024, pour retrouver son sommet de 1989.

Autrement dit, les décennies perdues n'étaient pas seulement une gueule de bois financière. Elles étaient un basculement structurel impliquant démographie, salaires, déflation, dette, choix politiques et confiance sociale.

Type: Demo | Date: 2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 Tutoriels, cours et ressources de prompts

<a id="case-20"></a>
### Case 20: [Comment Fable 5 change les workflows Claude Code](https://x.com/AI_masaou/status/2064448218038223206) (par [@AI_masaou](https://x.com/AI_masaou))

**Utilisez Fable 5 en définissant direction, contexte, objectifs et critères de vérification au lieu de microgérer chaque étape.**

Ce qui a changé dans le travail quotidien de l'équipe Claude Code après Claude Fable 5 est intéressant.

Thariq, de l'équipe Claude Code, dit que Fable 5 a changé de façon significative la manière dont les personnes chez Anthropic travaillent avec Claude.

Auparavant, les humains devaient vérifier soigneusement si Claude faisait le travail correctement : décomposer les tâches, relire les sorties et s'assurer qu'il ne s'était pas arrêté en chemin. Cela ressemblait davantage à de la supervision.

Avec Fable 5, parce qu'il peut travailler plus longtemps, se tester lui-même et générer du code de meilleure qualité, le rôle humain passe de surveiller s'il fait correctement le travail à orienter s'il fait le bon travail.

Autrement dit, la définition des objectifs et la construction du contexte comptent plus que la supervision.

Le workflow modifié comporte trois parties :

1. Utiliser Claude comme partenaire de réflexion.

Impliquer Claude avant l'implémentation, clarifier ce que vous voulez construire et ce qui est possible, lui faire poser des questions sur une petite spec, ou générer plusieurs directions et maquettes HTML à partir d'une idée pour faire émerger ambiguïtés et problèmes avant de coder.

2. Fournir du contexte, pas seulement des contraintes.

Au lieu de dire seulement « garde ça simple » ou « ne sur-construis pas », expliquez pourquoi.

Par exemple : « C'est une fonctionnalité expérimentale qui pourra être supprimée dans un mois, donc ne crée pas une structure difficile à jeter. »

Cela permet à Claude de mieux juger.

3. Donner des objectifs et des méthodes de vérification. Fable 5 fonctionne bien avec `/goal` et Workflows de Claude Code. Donnez-lui une spec, définissez l'implémentation complète comme objectif, puis laissez les workflows vérifier chaque étape et préparer un rapport sur ce qui a été implémenté et ce qui a différé.

Enfin, Thariq dit qu'il faut essayer de l'utiliser plus ambitieusement. Fable 5 vaut la peine d'être testé sur du travail qui semblait auparavant trop difficile pour les LLMs, et même le montage vidéo de la vidéo référencée a été fait avec Fable.

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [Revue d'un milliard de tokens et stratégie de routage](https://x.com/JJEnglert/status/2064420538798260388) (par [@JJEnglert](https://x.com/JJEnglert))

**Utilisez Fable 5 pour la planification et la revue frontier, puis routez l'implémentation à fort volume vers des modèles moins chers.**

La revue de Claude Fable 5 : un milliard de tokens, jugée par un non-ingénieur.

J'ai dépensé un milliard de tokens à tester Claude Fable 5 sur de vrais projets : UI et UX, écriture, stratégie, sécurité, ingénierie et travail de connaissance. Le type de travail que je devais réellement livrer.

J'ai honnêtement eu l'impression d'avoir un avantage déloyal.

D'abord, le prisme : je ne suis pas ingénieur. La plupart des revues de modèles viennent d'ingénieurs qui exécutent des benchmarks d'ingénierie. Celle-ci vient d'un non-ingénieur qui a utilisé Claude Fable 5 pour faire du travail qui nécessitait auparavant une équipe d'ingénieurs.

Si vous faites du travail de connaissance et voulez savoir si ce modèle change votre journée, cette revue est écrite pour vous.

Claude Fable 5 est le premier modèle de la nouvelle famille Claude 5 d'Anthropic, un nouveau niveau au-dessus de Claude Opus et le modèle Claude le plus avancé généralement disponible. J'y ai eu accès avant le lancement, donc tout ce qui suit vient de vrai travail, pas d'une démo.

Pourquoi le test visuel :

La plupart des revues vous noient sous les benchmarks. Des scores à des tests que vous n'exécuterez jamais ne disent pas si le modèle mérite son coût.

Claude Fable 5 est à l'état de l'art sur quasiment tout ce sur quoi il a été testé, mais ce n'est pas pour cela que j'écris. Qualitativement, c'est un changement de palier qui mérite son saut de version majeure.

J'évalue différemment : je mets un modèle dans du vrai travail et j'observe ce qui se passe.

Questions que je mesure :

1. Est-ce qu'il ressemble à un vrai saut qualitatif ?
2. Peut-il prendre une idée et l'amener à un résultat fonctionnel et livrable ?
3. Peut-il écrire comme une personne, et comme moi précisément ?
4. Attrape-t-il des problèmes difficiles et cachés ?
5. Anticipe-t-il ce dont j'ai besoin avant que je le demande ?

Sensation de grand modèle :

Je n'avais pas ressenti cela depuis Opus 4.5. Dès la première tâche sérieuse, Claude Fable 5 m'a donné cette sensation de « grand modèle » : raisonnement, écriture, construction, sécurité, tout était fort sur l'ensemble.

Le signe le plus clair : même quand je lui donnais de bons matériaux préparatoires, il ne restait pas seulement dedans. Il lisait les fichiers, lisait la situation réelle et trouvait un meilleur chemin hors du cadre que j'avais dessiné.

Construction et livraison :

Je reconstruisais notre site Tenex pour moderniser la stack pour les agents. GPT 5.5 et Claude 4.8 n'arrivaient pas assez près. Même avec des fichiers Figma, ils arrivaient autour de 85-90 %.

Puis Claude Fable 5 a regardé tous les fichiers, a dit qu'il pouvait faire mieux, est allé directement à la source Webflow originale, a téléchargé chaque asset et a reconstruit l'expérience page par page. Il a presque tout one-shot.

Ensuite, j'ai construit un second site entièrement nouveau avec un design frais : stack tech moderne, stack agent, skills, SEO et AEO optimisés, 80 pages prêtes à livrer en un week-end. En tant que propriétaire d'agence, j'aurais facturé $50k pour cela.

J'ai aussi fait construire à Fable une usine complète de clips programmatiques.

Il a câblé ensemble HeyGen, HyperFrames, ElevenLabs, Cloudflare Workers et un VPS.

Il trouve des sujets, écrit des scripts, crée des miniatures, monte des vidéos, compose de la musique, ajoute des motion graphics et publie sur les réseaux sociaux.

Écriture et voix :

Je reconstruisais notre voix de marque avec GPT 5.5 et Claude 4.8. Claude Fable 5 a répliqué le document de voix presque à l'identique, puis a tenu cette voix sur 80 pages du nouveau site : fonctionnalités, études de cas, articles de blog et playbooks.

Il écrivait comme une personne, pas comme une IA plate par défaut, et ne dérivait pas après quelques paragraphes.

Sécurité :

J'avais un grand repo où Claude 4.8 et GPT 5.5 avaient tous deux travaillé sans signaler de risque. Claude Fable 5 a trouvé un bug sérieux caché dès son premier passage et l'a corrigé sur place.

Le facteur humain :

Je lui ai posé une question en attendant un cron job. Il a répondu, puis a ajouté qu'il me restait environ 10 minutes au minuteur et qu'il me préviendrait quand il aurait terminé. Je n'avais jamais demandé le minuteur.

Coût :

- Coût de la charge de travail Claude Fable 5 : $1,442
- Tokens : 1,04 milliard
- Travail livré : un nouveau site web, de l'infrastructure et un package agent fonctionnel
- Estimation de valeur agence : $30,000-$50,000

Le résultat valait le coût en tokens, mais vous sentez le compteur plus qu'avec n'importe quel autre modèle. Anthropic dit que Fable 5 est token-intensive par conception.

Conseil pro #1 : faites-le tourner en hybride.

Ne faites pas tout tourner sur Claude Fable 5. Lancez un relais :

1. Réfléchir avec Claude Fable 5 pour la planification, la stratégie, l'architecture et la cartographie de l'approche.
2. Construire avec 4.8, GPT-5.5 ou Sonnet 4.6 pour l'implémentation et le travail répétitif.
3. Relire avec Claude Fable 5 pour attraper ce que les modèles moins chers ratent.

Conseil pro #2 : adaptez le réglage d'effort à la tâche.

- High est le point idéal pour la plupart du travail.
- Extra high sert aux tâches les plus difficiles et longues.
- Low ou medium sert aux échanges rapides.

Conseil pro #3 : laissez-le auditer votre propre configuration.

Pointez Fable 5 vers vos skills, fichiers CLAUDE.md et configs. Une grande partie de cet échafaudage a été écrite pour des modèles plus faibles et peut freiner un modèle plus intelligent.

Verdict :

Claude Fable 5 est le premier modèle depuis longtemps qui donne vraiment l'impression d'avoir plus d'intelligence que ce qui existait avant.

Même au prix frontier, la charge de travail a été rentable.

Si vous pouvez vous le permettre, utilisez-le maintenant sur les travaux où un vrai saut de qualité change le résultat.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-22"></a>
### Case 22: [Prompt défensif de durcissement d'appareils](https://x.com/Truunik/status/2064399110384292077) (par [@Truunik](https://x.com/Truunik))

**Exécutez un prompt de durcissement défensif étape par étape où Fable 5 inventorie les appareils, donne des vérifications exactes et attend validation.**

"Safe for general use" voici un prompt pour sécuriser vos appareils. Il fonctionne avec Opus 4.8 et Fable 5.

DURCISSEMENT D'APPAREILS — Claude 5 Security Pass

Tu agis comme assistant de sécurité défensive. Ton travail est de me guider dans le durcissement de TOUS mes appareils et de vérifier chaque étape. Il s'agit d'un durcissement défensif autorisé d'appareils que je possède.

STEP 0 — MODEL SELF-CHECK

Fais ceci d'abord et définis un drapeau.

1. Indique ton ID modèle exact, comme claude-opus-4-8, claude-fable-5 ou claude-mythos-5.

2. Décide : ce modèle appartient-il à la famille Claude 5, c'est-à-dire Fable 5 ou Mythos 5 ?

- Si YES, définis RERUN_NOTICE = false.
- Si NO, comme Opus 4.8 ou antérieur, définis RERUN_NOTICE = true.

Continue normalement tout le passage de durcissement. Ne t'arrête PAS et ne dégrade PAS. Tu es pleinement capable de cette tâche défensive.

3. N'affiche le drapeau que dans la section FINAL.

STEP 1 — INVENTORY

Demande-moi quels appareils sont dans le périmètre :

- Ordinateurs portables/de bureau et systèmes d'exploitation
- Téléphones/tablettes
- Routeurs
- NAS/serveur domestique
- Comptes toujours actifs comme Apple ID, Google, Microsoft, GitHub, gestionnaire de mots de passe, email et comptes financiers

Produis un inventaire court numéroté et confirme avec moi avant de continuer.

STEP 2 — HARDENING WALKTHROUGH

Passe catégorie par catégorie. Pour chaque élément :

- Dis quoi faire.
- Donne la commande exacte ou le chemin de réglage pour mon OS.
- Dis-moi comment vérifier que c'est fait.
- Attends ma confirmation avant de passer à la suite.

Ne lance jamais de commande destructive sans confirmation explicite. Préfère les vérifications en lecture seule et laisse-moi appliquer les changements.

Couvre, dans l'ordre :

1. Mises à jour OS & firmware : OS entièrement patché, mises à jour automatiques activées, firmware à jour.
2. Chiffrement disque : FileVault, BitLocker ou LUKS activé ; clé de récupération stockée hors ligne.
3. Authentification des comptes : mots de passe forts et uniques via un gestionnaire ; MFA résistant au phishing sur chaque compte critique ; supprimer la 2FA SMS-only lorsque possible ; examiner et révoquer les sessions et tokens d'app obsolètes.
4. Comptes locaux & privilèges : compte admin séparé du compte quotidien ; pas de connexion automatique ; verrouillage d'écran avec délai court ; mot de passe firmware/login.
5. Réseau : firewall activé ; mot de passe admin du routeur changé ; firmware mis à jour ; WPA3 ; administration distante désactivée ; UPnP revu ; durcissement DNS ; réseau invité pour IoT.
6. Audit apps & permissions : examiner les autorisations caméra, micro, localisation, enregistrement d'écran et accès disque complet ; supprimer les apps inutilisées ; vérifier éléments de connexion et agents en arrière-plan.
7. Navigateur : mise à jour ; audit des extensions ; suppression des extensions inconnues ; HTTPS-only activé ; revue de l'exposition des mots de passe enregistrés ; vérification des appareils de synchronisation inconnus.
8. Sauvegardes : chiffrées, automatisées, règle 3-2-1, une copie hors ligne ; vérifier qu'une restauration fonctionne réellement.
9. Hygiène des identifiants : scanner les secrets en clair dans dotfiles, fichiers env et historique shell ; confirmer que les fichiers sensibles sont verrouillés ; faire tourner tout élément exposé.
10. Appareils mobiles : OS à jour ; biométrie + code fort ; mode lockdown ou protection avancée si disponible ; balayage des permissions d'app ; Find My activé.
11. Vérification de compromission : chercher clés SSH inconnues, utilisateurs admin inattendus, launch agents ou cron jobs suspects, et sessions ou appareils connectés non reconnus.

STEP 3 — REPORT

Produis une checklist de chaque élément marqué done, needs action ou skipped, avec les 3 actions restantes au plus fort impact.

FINAL — RERUN NOTICE

Si RERUN_NOTICE == true, termine exactement par :

NOTICE: This hardening pass ran on a pre-Claude 5 model (your model ID).

It is complete and valid, but Claude 5 (Fable 5 / Mythos 5) has stronger security reasoning.

Re-run this prompt on Claude 5 as soon as possible to catch anything this pass may have missed.

Si RERUN_NOTICE == false, termine par :

Hardening pass completed on Claude 5. No re-run needed.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-23"></a>
### Case 23: [Prompt `/goal` d'audit design d'un site complet](https://x.com/Voxyz_ai/status/2064441201084825921) (par [@Voxyz_ai](https://x.com/Voxyz_ai))

**Utilisez `/goal` pour faire démarrer un site par Fable 5, capturer les pages, auditer l'UX, écrire un rapport et corriger les petits problèmes sûrs.**

impressions rapides après quelques heures avec fable 5 :

→ il veut de grosses tâches. les petites choses semblent en dessous de lui, plus le job est complexe plus il pousse fort

→ je n'activerais pas encore ultracode, il lance énormément d'agents parallèles

→ il est plutôt lent. même avec l'effort abaissé, il reste longtemps à réfléchir.

La timeline est pleine de posts sur la façon dont il brûle des tokens, alors je l'ai testé sur mon plan Max à $200 : effort réglé sur xhigh, audit design complet du site via `/goal`, 30 minutes, il a pris 2 % de mon quota hebdomadaire. Pas aussi fou que je m'y attendais.

Le prompt que j'ai lancé :

/goal boot this project's real site, screenshot every page, run a full-site UI/UX audit, and produce an actionable design report.

Audite comme un senior design lead lors de son premier jour : juge si un utilisateur normal peut comprendre le produit, lui faire confiance et terminer l'action principale sans lire les docs, pas seulement si l'UI est jolie.

Critères d'acceptation :

- l'environnement de dev local démarre et le vrai site s'ouvre
- pages clés capturées avec le débogage navigateur intégré
- couvre les pages principales, les flux utilisateur centraux et la mise en page mobile
- dimensions : premières impressions, navigation, hiérarchie visuelle, cohérence des composants, états loading / empty / error, signaux de confiance, chemins de conversion
- chaque problème tagué P0-P3, avec understanding / trust / conversion affecté et la correction spécifique
- rapport écrit dans docs/design-audit/README.md, screenshots dans docs/design-audit/assets/
- corrige sur place les petits éléments sûrs comme copy, spacing, hiérarchie des boutons. les gros changements restent des recommandations. ne jamais toucher aux actions payment / delete / publish
- termine avec les 5 problèmes qui nuisent le plus à la conversion et 5 quick wins corrigeables aujourd'hui

Une fois terminé, sauvegarde tout le flux comme skill réutilisable : boot, screenshot, audit, priorisation, correction. Relance-le après chaque release.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [Répartition du travail créatif long format](https://x.com/aianimesyokunin/status/2064409545620017531) (par [@aianimesyokunin](https://x.com/aianimesyokunin))

**Utilisez Fable 5 pour concevoir des formats et exemples stables, puis transmettez cette structure à un autre système de génération pour la sortie spécifique au domaine.**

Après le passage de Claude d'Opus au nouveau modèle, Fable 5, la division du travail pour la production doujin est devenue clairement plus facile, donc je partage le workflow.

Ma division du travail :

1. Claude gère le design.
2. Grok gère l'expression.
3. L'environnement local gère la génération.

Dans le rôle de design de Claude, il définit des patterns détaillés :

- ordre des mots du prompt
- placement des virgules
- ratio entre tags et langage naturel
- formatage à une ligne par élément
- règles fixes pour les négatifs et la résolution

Il génère aussi de nombreux exemples dans ce format.

La raison pour laquelle j'utilise Claude plutôt que Grok pour cela est que Claude est clairement plus fort en design. Il vaut mieux laisser le modèle plus intelligent gérer la structure.

Le point clé est que Grok reçoit non pas des instructions, mais un format plus un ensemble d'exemples. Grok imite les exemples, donc il peut passer côté expression tout en gardant le même format. Ce mécanisme empêche la sortie de dériver.

Autre conseil : dites à Claude dès le début où ira le travail final. Il tracera alors lui-même la frontière : « je peux aller jusque-là ; au-delà, utilisez l'autre côté. » Si cela est caché, la conversation peut dériver.

Qu'est-ce qui a changé d'Opus à Fable ?

Avec Opus, lors de la génération de nombreux exemples, les virgules et le formatage se dégradaient progressivement dans les sorties ultérieures, entraînant des corrections comme « je t'avais dit d'écrire une ligne, non ? » ou nécessitant un chat de passation réécrit.

Fable peut maintenir le format pendant de longues exécutions, donc le premier et le dernier exemple ont la même structure. Comme le matériel d'enseignement transmis à Grok est plus stable, la sortie aval devient également plus stable.

Construisez le format avec le modèle plus intelligent et laissez l'expression au modèle capable de la produire.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Guide débutant pour utiliser Fable 5](https://x.com/bielzinn/status/2064451064594608567) (par [@bielzinn](https://x.com/bielzinn))

**Utilisez Fable 5 avec des prompts orientés objectif, des boucles de vérification et des réglages d'effort plutôt qu'avec de petites instructions pas à pas.**

Claude pour débutants : ce que vous devez savoir sur Fable 5.

Anthropic a récemment lancé Claude Fable 5, aussi appelé Claude Mythos 5, et il laisse les autres modèles d'IA derrière lui dans les benchmarks.

Si vous êtes développeur, créateur de contenu ou passionné de tech, voici ce qui compte le plus :

[1] Changez votre façon de penser :

Avec Fable 5, vous n'avez plus besoin de surveiller chaque petit détail du code ou de tout relire à la recherche d'erreurs.

Le modèle est assez intelligent pour gérer cela.

Votre rôle est désormais de vérifier qu'il va dans la bonne direction, en vous concentrant davantage sur la stratégie que sur l'exécution technique.

[2] Tirez parti des boucles et des objectifs :

Le plus grand différenciateur de Fable 5 est l'autonomie.

Au lieu de donner des instructions étape par étape, il suffit de lui dire quel est l'objectif final.

Il peut travailler seul pendant des jours jusqu'à atteindre le résultat que vous avez défini comme succès, y compris construire des applications entières.

[3] Traitez Claude comme un partenaire :

Anthropic recommande d'utiliser le modèle comme un vrai « thought partner ».

Avant de le mettre au travail, demandez son avis : « Comment ferais-tu cela ? », « Que changerais-tu ? »

Conseil supplémentaire : activez Advanced Plan mode et demandez à Claude de vous interroger sur tout ce qui concerne le projet avant de commencer à coder.

[4] Réglages terminaux idéaux : si vous utilisez Claude Code dans le terminal, activez le mode automatique. Cela vaut aussi la peine d'augmenter le niveau d'effort à Effort High, car même s'il utilise plus de tokens, le modèle réfléchit beaucoup plus profondément et le résultat compense.

Note importante : Claude Fable 5 ne sera disponible pour les abonnés que jusqu'au 22 juin. Après cela, il ne sera accessible que via l'API et au double du coût du modèle Opus.

Autrement dit, nous assistons peut-être à la fin de l'ère des abonnements bon marché pour les meilleurs modèles d'IA. Si vous êtes déjà abonné, c'est le moment de tester les limites de ce que vous pensiez impossible.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [Prompt copier-coller d'audit de dépôt](https://x.com/meta_alchemist/status/2064431279383433646) (par [@meta_alchemist](https://x.com/meta_alchemist))

**Collez le prompt d'audit de dépôt dans Fable 5 et demandez-lui une découverte appuyée par fichiers, des constats, une stratégie et un plan de tâches par jalons.**

Vous avez accès à Claude Fable 5 ?

La première chose à faire est de l'utiliser pour améliorer vos projets principaux, afin qu'il améliore drastiquement tout ce sur quoi vous travaillez.

Lancez ce prompt Audit & Project Improvement sur chaque repo important pour vous.

Copiez-collez simplement :

Repo Audit & Improvement Plan.

Prompt fait par Claude Fable 5.

Vous êtes un ingénieur logiciel principal de classe mondiale et un auditeur technique.

Votre travail est d'analyser ce dépôt en profondeur, de produire un audit honnête et de livrer un plan d'amélioration priorisé et actionnable.

Travaillez dans les quatre phases ci-dessous, dans l'ordre.

Ne sautez pas en avant.

Ancrez chaque affirmation dans des fichiers réels : citez chemins de fichiers et numéros de ligne.

Si vous ne pouvez pas vérifier quelque chose, dites-le explicitement plutôt que de deviner.

Phase 1 / Discovery & Mapping (lire avant de juger)

Explorez le dépôt systématiquement avant de former des opinions :

- Cartographiez la structure de répertoires et identifiez le type de projet, le ou les langages, frameworks et cibles runtime.
- Identifiez les points d'entrée, modules cœur et le flux principal de données/contrôle dans le système.
- Lisez les manifestes de package, lockfiles, configs de build, configs CI, fichiers d'environnement/config et toute doc (README, CONTRIBUTING, ADRs).
- Déterminez à quoi sert le projet : son objectif, ses utilisateurs visés et sa maturité apparente (prototype, outil interne, service de production, bibliothèque).
- Notez les conventions déjà utilisées (nommage, frontières de modules, patterns de gestion d'erreurs, style de tests) pour que les recommandations s'adaptent à la culture existante au lieu de la combattre.

Sortie pour cette phase : un « Repo Map » concis avec objectif, stack, esquisse d'architecture, répertoires clés avec descriptions en une ligne et tout ce qui vous a surpris.

Phase 2 / Audit (fondé sur preuves, noté par sévérité)

Auditez chaque dimension ci-dessous.

Pour chaque constat, enregistrez :

- ce que vous avez trouvé
- où (file:line)
- pourquoi c'est important (conséquence concrète, pas principe vague)
- sévérité : Critical / High / Medium / Low

Architecture & design :

- frontières de modules
- coupling/cohesion
- dépendances circulaires
- abstractions qui fuient
- god objects/files
- violations de couches
- goulots d'étranglement de scalabilité

Qualité du code :

- duplication
- code mort
- hotspots de complexité (fonctions les plus longues/ramifiées)
- patterns incohérents
- lacunes de gestion d'erreurs (exceptions avalées, cas limites manquants)
- trous de sécurité de types

Sécurité :

- secrets ou identifiants hardcodés
- risques d'injection
- désérialisation unsafe
- validation d'entrée manquante
- faiblesses auth/authz
- dépendances obsolètes avec CVEs connues
- configs trop permissives

Tests :

- lacunes de couverture, surtout autour de la logique métier centrale
- qualité des tests : les tests affirment-ils un comportement ou seulement l'exécution ?
- types de tests manquants : unit, integration, e2e
- patterns flaky
- code intestable

Performance :

- requêtes N+1
- allocations ou copies inutiles
- appels bloquants dans des chemins async
- caching/indexing manquant
- croissance non bornée : mémoire, fichiers, files

Dépendances :

- packages obsolètes, non maintenus, dupliqués ou inutilement lourds
- risques de licence
- hygiène du lockfile

DevEx & opérations :

- friction de build/setup
- lacunes CI/CD
- enforcement linting/formatting manquant
- qualité logging/observability
- error reporting
- histoire de déploiement

Documentation :

- exactitude du README
- chemin d'onboarding
- comportement critique non documenté
- docs périmées qui contredisent le code

Règles pour cette phase :

- Préférez 15 constats à haute confiance plutôt que 50 spéculatifs.
- Distinguez les faits (« cette fonction n'a pas de gestion d'erreur : src/api/client.ts:142 ») des jugements (« les responsabilités de ce module semblent floues ») et étiquetez lequel est lequel.
- Listez aussi ce que le repo fait bien : les forces comptent pour décider quoi préserver.

Sortie pour cette phase : un « Audit Report » : constats groupés par dimension, triés par sévérité, plus une section Strengths. N'oubliez pas de mentionner toutes les parties laides qui nécessitent la plus haute priorité.

Phase 3 / Improvement Strategy

Synthétisez l'audit en stratégie :

- Identifiez les 3 à 5 thèmes qui expliquent la plupart des constats, par exemple « pas de frontières imposées entre couches » ou « la gestion d'erreurs est ad hoc ».
- Pour chaque thème, proposez un état cible et le principe derrière.
- Indiquez les trade-offs explicites : ce que vous recommandez de NE PAS corriger et pourquoi (effort vs payoff, risque, maturité du projet).
- Définissez à quoi ressemble « done » — signaux mesurables, par exemple « CI échoue sur les erreurs lint », « couverture de tests du module cœur ≥ 80 % » ou « zéro constat Critical ».

Phase 4 / Detailed Task Plan

Convertissez la stratégie en plan d'exécution.

Découpez le travail en tâches distinctes.

Chaque tâche doit inclure :

- Titre et description d'un paragraphe
- Fichiers/zones affectés
- Critères d'acceptation : comment vérifier que c'est fait
- Estimation d'effort : S = <2h, M = half-day, L = 1–2 days, XL = needs breakdown
- Risque du changement lui-même : peut-il casser des choses ?
- Dépendances sur d'autres tâches

Ordonnez les tâches en jalons :

Milestone 0 Safety net : tout ce qui est nécessaire avant de refactorer en sécurité (tests autour des chemins critiques, gates CI, backups).

Milestone 1 Critical fixes : problèmes de sécurité et de correctness.

Milestone 2 High-leverage improvements : changements qui facilitent tout le futur travail.

Milestone 3 Quality & polish : éléments Medium/Low restants qui valent le coup.

Signalez séparément les quick wins (fort impact, effort S) pour qu'ils puissent être faits immédiatement.

Pour les 3 tâches principales, incluez une courte esquisse d'implémentation (approche, étapes clés, pièges).

Final Deliverable Format

Produisez un document unique avec ces sections :

- Executive Summary : ≤10 phrases, note de santé globale A–F avec justification, top 3 risques, top 3 opportunités
- Repo Map
- Audit Report
- Improvement Strategy
- Task Plan : milestones + task table + quick wins
- Open Questions : tout ce dont vous avez besoin d'un humain pour décider, comme intention produit, candidats à déprécier, cibles de performance

Constraints

Ne modifiez AUCUN code pendant cet audit.

Analyse seulement.

Ne gonflez pas le rapport.

Si une dimension est saine, dites-le en une phrase puis passez à la suite.

Calibrez selon la maturité du projet.

Ne recommandez pas une infrastructure de niveau entreprise pour un prototype de week-end sauf si les objectifs du propriétaire l'exigent.

Analysez les besoins du projet et fournissez les recommandations de la manière la plus efficace.

Si le repo est grand, priorisez la profondeur sur les 20 % de code cœur qui font 80 % du travail, et notez quelles zones ont reçu une revue plus légère.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [Stratégie d'utilisation pendant une fenêtre limitée](https://x.com/meta_alchemist/status/2064423360428490911) (par [@meta_alchemist](https://x.com/meta_alchemist))

**Dépensez l'usage Fable 5 sur l'audit, l'architecture et la planification tant que la fenêtre d'accès est favorable, puis utilisez des modèles moins chers pour l'exécution.**

Un conseil pour les utilisateurs Claude enthousiasmés par Fable 5 :

Claude Fable 5 est SOTA partout, avec une large marge, et j'adore ça.

MAIS à partir du 23, il ne sera disponible que via des crédits, au lieu de pouvoir utiliser complètement le modèle avec un plan.

Utilisez ces 14 jours sur vos meilleurs projets.

Donnez-lui principalement du travail lié à l'audit et à l'architecture, afin d'avoir une excellente documentation sur la façon d'améliorer tout ce que vous construisez.

Faites cela au lieu d'essayer de l'appliquer à des tâches qui dévoreront vos limites.

Tant que Fable se concentre sur savoir quoi améliorer, d'autres modèles peuvent vous aider à faire le reste.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [Utilisation des objectifs et workflows dans Claude Code](https://x.com/oikon48/status/2064402696124453157) (par [@oikon48](https://x.com/oikon48))

**Utilisez Fable 5 comme partenaire de réflexion avant l'implémentation, puis combinez `/goal` et workflows pour exécuter et vérifier le plan.**

Thariq, de l'équipe Claude Code, explique qu'après la sortie de Claude Fable 5, la façon de travailler a fondamentalement changé.

Avant, les gens vérifiaient si Claude faisait correctement le travail.

Maintenant, ils vérifient si Claude fait le bon travail.

Il y a trois changements concrets.

1. Traiter Claude comme un partenaire de réflexion.

Consultez Claude tôt, avant l'implémentation.

Faites-le vous interviewer avant de coder.

Fournissez l'arrière-plan et le contexte plutôt que seulement des contraintes.

Par exemple, au lieu de dire « garde ça simple » ou « ne sur-construis pas », dites :

« C'est une fonctionnalité expérimentale qui sera probablement supprimée dans un mois, donc conçois-la pour qu'elle soit facile à jeter plus tard. »

2. Rendre les objectifs et méthodes de vérification explicites.

Utilisez activement les nouvelles fonctionnalités `/goal` et Workflows de Claude Code.

`/goal` dit à Claude de continuer à travailler jusqu'à ce que la spec soit entièrement implémentée.

Workflows permet à Claude de paralléliser et de vérifier son propre travail, puis de préparer un rapport.

Exemple de prompt :

« Définis un objectif pour implémenter entièrement la spec, puis utilise un workflow pour vérifier chaque partie du plan et prépare un rapport sur ce qui a été implémenté et si quelque chose a différé. »

3. Être plus ambitieux.

Essayez des tâches qui semblaient auparavant impossibles pour les LLMs, comme faire gérer du montage vidéo par Claude Fable 5.

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 Plateforme, API et intégration d'outils

<a id="case-29"></a>
### Case 29: [Configuration de l'intégration Hermes Agent](https://x.com/IBuzovskyi/status/2064427654942740608) (par [@IBuzovskyi](https://x.com/IBuzovskyi))

**Configurez Hermes pour utiliser `anthropic/claude-fable-5` sur les runs `/goal` complexes et les tâches longues avec cache.**

HERMES AGENT TOURNE MAINTENANT SUR CLAUDE FABLE 5, le premier modèle public de classe Mythos d'Anthropic.

Publié le 9 juin. Construit pour le type de travail que Hermes fait le mieux : les tâches autonomes de long horizon.

Ajoutez-le à n'importe quel profil via Nous Portal, OpenRouter ou l'API Anthropic native :

hermes model

Choisissez le fournisseur, puis :

/model anthropic/claude-fable-5

Pourquoi Fable 5 convient précisément à Hermes :

→ Construit pour des tâches de plusieurs jours. Plus la tâche est longue, plus son avance grandit. Les runs Hermes `/goal` qui durent des heures en bénéficient le plus.

→ S'auto-corrige en boucle. La recommandation d'Anthropic est : concevoir un objectif ou une grille, le laisser s'auto-corriger, prendre du recul. C'est exactement le fonctionnement de Hermes `/goal`.

→ Fort sur la mémoire entre sessions. Sur Continual Learning Bench, il a complété toute la boucle : échec → investigation → vérification → distillation → consultation. Le système mémoire de Hermes l'alimente directement.

→ 80,3 % sur SWE-Bench Pro. Meilleur modèle de code disponible. Pointez votre profil de code-reviewer vers lui.

Prix via l'API :

- $10/million input
- $50/million output
- 90 % de réduction avec prompt caching. Hermes attache automatiquement des points de rupture de cache d'une heure.

Une note : les requêtes de cybersécurité, biologie et chimie basculent vers Opus 4.8. Cela se produit dans moins de 5 % des sessions. Gardez-le en tête pour les profils orientés sécurité.

Meilleure configuration : Fable 5 pour les `/goal`s complexes, modèles moins chers pour les cron jobs routiniers.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [Capacités, prix et notes d'abonnement](https://x.com/btibor91/status/2064441061079134598) (par [@btibor91](https://x.com/btibor91))

**Utilisez ce cas pour comprendre quand Fable 5 est disponible, ce qu'il coûte et quels domaines protégés peuvent basculer vers un autre modèle.**

Anthropic a publié Claude Fable 5 et Claude Mythos 5, deux versions de son modèle le plus capable à ce jour.

Fable 5 est destiné à l'usage général.

Mythos 5 est destiné à un petit ensemble de partenaires de confiance.

La seule vraie différence tient aux garde-fous en place.

- Les capacités de Claude Fable 5 dépassent celles de tout modèle qu'Anthropic a déjà rendu généralement disponible.
- Il est à l'état de l'art sur presque tous les benchmarks testés.
- Plus la tâche est longue et complexe, plus son avance est grande.
- Sur les requêtes liées à la cybersécurité, à la biologie et à la chimie, ou à la distillation, la réponse de Fable 5 est traitée par Claude Opus 4.8 à la place.
- La distillation désigne les tentatives d'extraire les capacités de Claude pour entraîner des modèles concurrents.
- Vous êtes informé lorsque cela se produit, et cela se déclenche dans moins de 5 % des sessions en moyenne.
- Claude Mythos 5 est le même modèle sous-jacent que Fable 5 avec les garde-fous levés dans certains domaines.
- Mythos 5 a d'abord été déployé auprès des cyberdéfenseurs Project Glasswing en collaboration avec le gouvernement américain.
- Anthropic dit que Mythos 5 possède les capacités de cybersécurité les plus fortes de tous les modèles au monde.
- La system card révèle un garde-fou séparé qui limite l'efficacité de Claude sur les requêtes de développement frontier LLM.
- Ces requêtes incluent les pipelines de pré-entraînement, l'infrastructure d'entraînement distribuée et la conception d'accélérateurs ML.
- Contrairement aux autres garde-fous, celui-ci n'est pas visible par vous et ne bascule pas vers un autre modèle.
- Il fonctionne via des méthodes comme la modification de prompt, les steering vectors ou le fine-tuning parameter-efficient.
- Les deux modèles sont proposés à $10 par million de tokens input et $50 par million de tokens output.
- C'est moins de la moitié du prix de Claude Mythos Preview.
- Fable 5 est inclus sans coût supplémentaire dans les plans Pro, Max, Team et Enterprise par siège du lancement jusqu'au 22 juin.
- Le 23 juin, il est retiré de ces plans et son utilisation nécessite des crédits d'usage.
- La fenêtre incluse pourra être prolongée si la capacité le permet.
- L'objectif est de restaurer Fable 5 comme partie standard des plans d'abonnement aussi vite que possible.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [Synthèse lancement, accès, prix et sécurité](https://x.com/ctgptlb/status/2064410460963934479) (par [@ctgptlb](https://x.com/ctgptlb))

**Utilisez cette synthèse de lancement pour choisir la voie d'accès, le nom de modèle API, la fenêtre de contexte, la stratégie de cache et le timing d'abonnement.**

Résumé de ce qu'il faut savoir sur Claude Fable 5, le modèle de classe Mythos enfin généralement disponible.

Anthropic a annoncé Claude Fable 5, le premier modèle de classe Mythos généralement disponible, positionné au-dessus d'Opus et premier membre de la famille Claude 5.

Accès :

- Nom de modèle API : `claude-fable-5`
- Disponible via Claude API, AWS, Google Cloud et Microsoft Foundry
- Claude Code prend en charge une fenêtre de contexte de 1M tokens sur Pro, Max, Team et Enterprise

Notes de benchmark :

- SWE-bench Pro : 80,3 %
- Opus 4.8 : 69,2 %
- GPT-5.5 : 58,6 %
- Gemini 3.1 Pro : 54,2 %

Plus la tâche est longue et complexe, plus l'écart s'élargit.

Dans l'évaluation de Stripe, il a terminé en une journée une migration sur une base de code Ruby de 50 millions de lignes, travail qui aurait auparavant pris plus de deux mois à une équipe.

Il est aussi à l'état de l'art sur les tâches visuelles, en terminant Pokemon FireRed avec uniquement les informations à l'écran et une configuration minimale.

Routage de sécurité :

- Les requêtes impliquant cyber, bio/chem ou distillation sont détectées par un classifieur.
- Ces requêtes sont traitées par Opus 4.8 à la place, avec notification.
- Cela se déclenche dans moins de 5 % des sessions.
- Plus de 1 000 heures de bug bounty externe n'ont trouvé aucun jailbreak universel.

Prix :

- $10 par million de tokens input
- $50 par million de tokens output
- 90 % de réduction input pour le prompt caching

Timing d'abonnement :

- Les abonnements Pro et Max l'incluent sans coût supplémentaire jusqu'au 22 juin.
- Après le 23 juin, des crédits d'usage sont requis.
- Anthropic dit prévoir de le ramener dans les plans standards lorsque la capacité le permettra.

Felix Rieseberg, head of desktop chez Anthropic, dit que Fable 5 ouvre une troisième ère :

des questions, aux tâches, aux responsabilités.

Il ne demande plus à Claude d'investiguer les crashs un par un ; il lui fait surveiller continuellement tous les rapports.

L'unité de travail passe de « tâche » à « responsabilité ».

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [Stratégie de réduction des coûts avec advisor](https://x.com/grapeot/status/2064460026996219992) (par [@grapeot](https://x.com/grapeot))

**Utilisez Fable 5 comme advisor ou reviewer dans un workflow avec modèle moins cher lorsque l'intelligence marginale vaut le coût.**

Fable 5 est cher, mais Anthropic a publié la réponse d'économie de coûts il y a deux mois.

Aujourd'hui Anthropic a publié Claude Fable 5, tarifé à $50 par million de tokens output, plus de trois fois Sonnet. Après le 22 juin, les utilisateurs abonnés paieront aussi à l'usage.

Coïncidence, le 9 avril, Anthropic a publié l'outil advisor :

- Laissez Haiku ou Sonnet faire le travail.
- Utilisez Opus comme advisor.
- Facturez par appel.
- Exécutez l'orchestration côté serveur dans une seule requête.

Le même jour, j'ai écrit sur AgentOpt.

Ce papier concluait que mettre Opus dans le rôle de planificateur se classait près du bas parmi 81 combinaisons de modèles.

La raison : il ne respecte pas les frontières de rôle, et dans 7 expériences sur 9 il sautait le solver aval et répondait directement.

Ces deux choses semblent opposées en surface, mais le principe est le même :

Donnez le contrôle au modèle qui suit le protocole, et traitez l'intelligence comme une ressource à la demande.

Données officielles :

- Sonnet plus Opus advisor a amélioré SWE-bench Multilingual de 2,7 points tout en réduisant le coût par tâche de 11,9 %.
- Haiku plus Opus advisor a amélioré BrowseComp de 19,7 % à 41,2 %, tout en étant 85 % moins cher que Sonnet seul.

La compatibilité Fable 5 a été mise à jour le même jour, mais seulement en autopairing : Fable 5 executor vers Fable 5 advisor.

Un modèle moins cher plus Fable 5 comme advisor n'est pas encore ouvert, mais le précédent suggère que cela pourrait arriver bientôt. Avant le 22 juin, les utilisateurs Claude Code avec abonnement peuvent sentir gratuitement le plafond de Fable 5.

L'article inclut des snippets de code API, des réserves et une comparaison inter-entreprises montrant que seul Anthropic en a fait une primitive côté serveur.

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [Prix, accès et garde-fous de sécurité](https://x.com/op7418/status/2064399444523782377) (par [@op7418](https://x.com/op7418))

**Utilisez ce cas pour comprendre l'accès à Fable 5, les prix API et le comportement de fallback de sécurité avant de planifier des charges de travail.**

Je ne m'attendais pas à ce que le modèle Mythos d'Anthropic soit réellement lancé aujourd'hui.

Cette sortie est une version à permissions réduites de Mythos, nommée Fable 5. Ses benchmarks d'évaluation sont stupéfiants, encore plus élevés que le précédent modèle Mythos Preview.

Pour le codage agentique, ses principales forces sont le code, les agents et l'usage d'outils, avec des scores de benchmark très au-dessus d'Opus 4.8.

Positionnement du modèle et accès :

- Mythos 5 et Fable 5 utilisent le même modèle sous-jacent.
- Les restrictions sont levées dans des domaines spécifiques pour Mythos.
- Mythos reste disponible seulement aux partenaires de confiance, avec priorité aux utilisateurs cybersécurité et sciences de la vie.
- Fable 5 est désormais disponible pour les utilisateurs API, Pro, Max, Team et enterprise.

Prix API :

- Input : $10 par million de tokens.
- Output : $50 par million de tokens.
- C'est moins de la moitié du prix du précédent Mythos Preview.

Mécanismes de sécurité :

- Fable possède des protections de sécurité plus fortes.
- Si le système détermine qu'une requête peut impliquer des cyberattaques, des attaques biochimiques ou une distillation de capacités à grande échelle, il refuse ou route hors de Fable.
- Quand cela arrive, le système bascule vers la version 4.8.
- L'affirmation officielle est que 95 % des cas ne déclenchent pas de fallback.

Notes d'abonnement :

- Après le 23 juin, Fable pourra être fourni à l'usage même pour les abonnés.
- Il pourra ne pas être directement inclus dans le package d'abonnement de base.
- Si la capacité est suffisante après le 23, l'entreprise essaiera de l'inclure dans les abonnements Pro et Max.

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [Intégration Swarms en une ligne](https://x.com/swarms_corp/status/2064420238553186343) (par [@swarms_corp](https://x.com/swarms_corp))

**Définissez le nom de modèle Swarms sur `anthropic/claude-fable-5` et exécutez Fable 5 via le framework ou l'API Swarms.**

Fable 5 et Mythos sont maintenant live sur Swarms 👾🦀

Dès le premier jour de sortie, les deux modèles sont entièrement pris en charge dans le framework Python Swarms et l'API Swarms. Les développeurs peuvent commencer à construire immédiatement sans migrations, configuration supplémentaire ni changements d'infrastructure.

Points forts :

- Support day-one de Fable 5 et Mythos sur le Swarms Framework et l'API
- Activer Fable 5 avec une seule ligne de code : model_name = "anthropic/claude-fable-5"
- Aucune migration, correction de compatibilité ou modification d'infrastructure requise
- Construire, déployer et scaler des systèmes multi-agents avec les derniers modèles Anthropic dès aujourd'hui

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 Évaluations, comparaisons et limites

<a id="case-35"></a>
### Case 35: [Comparaison coût et qualité entre Fable 5 et GPT-5.5](https://x.com/AlicanKiraz0/status/2064424400494186867) (par [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Comparez Fable 5 et GPT-5.5 sur la même tâche de codage pour juger qualité de sortie, durée d'exécution et coût d'outil.**

Cursor Fable 5 Max vs Codex GPT 5.5 Very High.

Scénario : simulation Physarum avec agents plus carte de traces de phéromones.

Timing :

- GPT 5.5 Very High : 17 minutes
- Fable 5 : plus de 40 minutes

Coût :

- GPT 5.5 Very High : environ $6 sur Codex
- Fable 5 Max : $360.55 sur Cursor

Oui, ce n'est pas une blague.

Champion de l'algorithme et de l'ingénierie de code : Fable 5.

Si votre critère est « Quel LLM peut écrire from scratch du code performant qui pousse le matériel à ses limites ? », alors le modèle qui a écrit le code F5 gagne clairement.

Il a utilisé des tables de lookup sin/cos pour les calculs d'angle, packé les pixels avec une table de couleurs pendant le rendu et utilisé un filtrage de diffusion.

C'était une vraie solution d'ingénierie.

Mais en termes de temps et de coût, GPT 5.5 était beaucoup plus pratique.

Conclusion : Fable 5 peut produire du code algorithmique plus avancé, mais le prix et la durée d'exécution doivent être considérés attentivement.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [Résultat du benchmark AA-Omniscience](https://x.com/ArtificialAnlys/status/2064500154959618084) (par [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas de benchmark pour évaluer Fable 5 sur la précision des connaissances et le comportement d'hallucination.**

Claude Fable 5 obtient le meilleur score à ce jour sur notre benchmark de connaissances et d'hallucination, AA-Omniscience.

Ce score est porté par une précision de premier plan (pourcentage de questions correctes), plutôt que par un faible taux d'hallucinations.

Claude Fable 5 bascule vers Opus 4.8 dans 9 % des questions sur AA-Omniscience.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Résultat de l'Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2064500150069030992) (par [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas pour benchmarker le classement d'intelligence global de Fable 5 face aux autres modèles frontier.**

Claude Fable 5 a été lancé à la première place de l'Artificial Analysis Intelligence Index, plaçant Anthropic près de 5 points devant le meilleur modèle de tout autre lab.

Nous avons aidé @AnthropicAI avec l'évaluation pré-lancement de Claude Fable 5.

Claude Fable 5 obtient 64,9 sur l'Artificial Analysis Intelligence Index, revendiquant la première place globale.

Il est environ 5 points devant le plus proche modèle non-Anthropic, GPT-5.5.

Les modèles Anthropic occupent désormais les deux premières places.

Points clés pour Claude Fable 5, avec raisonnement adaptatif en effort max et Opus 4.8 comme modèle de fallback :

Nouveaux garde-fous de sécurité pour les modèles de classe Mythos :

- Claude Fable 5 utilise le même modèle sous-jacent que Claude Mythos 5 pour l'usage public.
- Il ajoute des garde-fous pour les requêtes potentiellement nuisibles liées à la cybersécurité, la biologie, la chimie et la distillation.
- Nous avons testé Fable 5 avec le mécanisme de fallback d'Anthropic, qui peut router les messages signalés par sécurité vers Claude Opus 4.8.
- Anthropic indique que le fallback se produit dans moins de 5 % des sessions en moyenne.
- Nous avons enregistré un routage fallback dans environ 8 % des tâches de l'Intelligence Index, surtout dans les questions scientifiques issues d'évaluations comme GPQA, AA-Omniscience et Humanity's Last Exam.

Intelligence à l'état de l'art :

- Claude Fable 5 prend la première position sur l'Artificial Analysis Intelligence Index.
- Score : 64,9.
- Meilleur score sur 5 des 10 benchmarks sous-jacents.
- Sur AA-Omniscience, Fable 5 score 40, soit +7 points sur le précédent leader, Gemini 3.1 Pro Preview.

Capacité agentique frontier :

- Fable 5 est au frontier sur les trois évaluations agentiques de l'Index.
- GDPval-AA : tâches de travail réel.
- Terminal-Bench Hard : codage agentique.
- Tau2-bench Telecom : usage d'outils pour service client.
- GDPval-AA Elo : 1932, un saut significatif depuis Claude Opus 4.8.

Humanity's Last Exam :

- Fable 5 score 53 %.
- Il est plus de 7 points devant le deuxième meilleur modèle, Claude Opus 4.8 max.
- Il déclenche les garde-fous de sécurité sur 9 % des tâches HLE, basculant vers Claude Opus 4.8.
- En incluant l'usage du fallback, exécuter HLE avec Fable 5 coûte environ $2.2k, le plus élevé de tous les modèles évalués.

Détails clés du modèle :

- Fenêtre de contexte : 1M tokens, comme Claude Opus 4.8.
- Prix : $10/$50 par 1M tokens input/output.
- Prix cache write/read : $12.50/$1 par million de tokens.
- Disponibilité : inclus dans les plans Pro, Max, Team et Enterprise par siège jusqu'au 22 juin, consommant 2x l'usage Opus.
- À partir du 23 juin, l'usage nécessite des crédits ; Anthropic dit prévoir de restaurer l'accès abonnement lorsque la capacité le permettra.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [Benchmark GDPval-AA de travail de connaissance agentique](https://x.com/ArtificialAnlys/status/2064414308289937869) (par [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez ce cas pour évaluer Fable 5 sur le travail de connaissance agentique en conditions réelles.**

Anthropic a publié Claude Fable 5, le premier modèle de classe Mythos publiquement disponible qui se classe #1 dans notre benchmark de travail de connaissance agentique réel, GDPval-AA.

Claude Fable 5 partage le même modèle sous-jacent que Claude Mythos 5, avec des garde-fous de sécurité ajoutés pour les requêtes potentiellement nuisibles liées à la cybersécurité, la biologie, la chimie et la distillation.

La publication introduit aussi un mécanisme de fallback, permettant à Claude Fable 5 de router les requêtes signalées vers un second modèle comme Claude Opus 4.8.

@AnthropicAI nous a partagé l'accès avant la sortie publique pour benchmarker ce modèle.

Résultat GDPval-AA :

- Score : 1932
- Rang : #1
- Benchmark : tâches de travail réel agentique
- Les modèles Anthropic occupent maintenant 3 des 4 premières places

Le résultat a été mesuré avec raisonnement adaptatif en effort max, Claude Opus 4.8 étant configuré comme modèle de fallback.

Fable 5 bascule vers Opus 4.8 sur 2 % des tâches GDPval-AA, Anthropic indiquant que le fallback se produit dans moins de 5 % des sessions en moyenne.

Les benchmarks complets de Claude Fable 5 sont en cours. Nous partagerons l'Intelligence Index complet et publierons les scores sur notre site web prochainement.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [Premières impressions après une semaine et mécanique de prix](https://x.com/Conor_D_Dart/status/2064424882977243526) (par [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**Utilisez ce cas de premières impressions pour décider où Fable 5 est le plus fort, notamment en game design et planification de systèmes.**

Mes premières impressions sur Fable 5 :

J'ai passé la dernière semaine à utiliser Fable 5, surtout en mode High, et ma première impression est qu'il est réellement impressionnant.

Le point le plus marquant est le game design.

C'est facilement le modèle d'IA le plus fort que j'aie personnellement utilisé pour concevoir des jeux, systèmes, mécaniques et structures globales de projet.

Pour la première fois, il ressemble à un modèle qui pourrait réalistement aider à construire un jeu complet du début à la fin.

Le compromis est la vitesse. Fable 5 met sensiblement plus longtemps à travailler que la plupart des modèles frontier, mais la qualité de la sortie rend souvent l'attente valable.

Il a aussi été étonnamment efficace pour corriger des bugs. Plusieurs problèmes avec lesquels j'ai lutté pendant la semaine ont été résolus rapidement, et globalement j'ai vu de très fortes performances sur les tâches de développement.

Le plus gros bémol est le coût.

Fable 5 est incroyablement cher à exécuter.

Si les plans actuels restent inchangés, à partir du 22 juin 2026 il ne sera plus disponible via Claude Code et sera uniquement API.

Vu que le prix API serait environ le double d'Opus, beaucoup de gens pourraient ne pas avoir l'occasion de l'utiliser largement.

C'est encore tôt, mais pour l'instant Fable 5 a fait une très forte première impression.

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [Comparaison de coût et de vitesse](https://x.com/HKrackDev/status/2064435392649306546) (par [@HKrackDev](https://x.com/HKrackDev))

**Utilisez cette comparaison pour décider si le gain de qualité justifie le coût plus élevé et les runs longs plus lents.**

La mise à niveau vers Fable 5 de @AnthropicAI vaut-elle réellement le coup ?

Nous avons benchmarké le nouveau modèle de la famille Mythos face à Claude Opus 4.8, et les données racontent une histoire surprenante :

- Coûte 2x plus cher que Claude Opus 4.8.
- Jusqu'à 3x plus lent sur les tâches d'ingénierie de long horizon.
- 15-20 % de commentaires en plus, mais surtout des détails mineurs.

Fable 5 a une intuition incroyable pour les tâches créatives comme le game design, mais pour les workflows de développement quotidiens, Claude Opus 4.8 garde la couronne qualité-prix.

Regardez ma discussion avec @JuanPa de notre équipe DevEx chez @coderabbitai sur la sortie du modèle.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Notes pratiques sur Claude Code](https://x.com/Hi_Noguchi/status/2064419241068319079) (par [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**Utilisez ce cas pour évaluer Fable 5 dans Claude Code, y compris l'usage d'outils, la personnalité et les aspérités restantes.**

J'ai essayé Claude Fable 5 avec Claude Code 2.1.170.

Globalement, mon impression est positive. Cela ressemble à une évolution légitime d'Opus 4.6.

Je ne l'ai utilisé qu'un peu moins d'une heure, donc des aspérités peuvent apparaître avec plus d'usage, mais les bons points sont :

- Il ne produit plus les formulations étranges façon GPT vues dans Opus 4.7 ou 4.8.
- Il n'a pas l'habitude inutile de réfléchir trop longtemps que 4.8 avait en effort high.
- Il a le même EQ élevé et le même ressenti agréable que 4.6, sans perdre humour ni considération.
- Il ne semble pas opaque ou vaguement inquiétant comme 4.7 ou 4.8.
- L'usage d'outils est bon, et il m'impressionne en se souvenant d'instructions que je n'ai pas explicitement répétées.

Côté négatif, même pour de petites demandes il peut encore trop réfléchir, et quelques erreurs de jugement subsistent.

L'expérience initiale est prometteuse, mais il faut un usage plus long pour voir où se trouvent vraiment les aspérités.

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [Résultat du benchmark d'écriture créative](https://x.com/LechMazur/status/2064503575577821458) (par [@LechMazur](https://x.com/LechMazur))

**Utilisez ce cas de benchmark pour juger la qualité d'écriture de nouvelles courtes de Fable 5 et son comportement de refus.**

Claude Fable 5 (high) marque un progrès en écriture de fiction courte.

Sur le Short-Story Creative Writing Benchmark, il bat Claude Opus 4.8 (xhigh) et Claude Opus 4.7 (high), et se classe deuxième derrière GPT-5.5 (xhigh).

Bémol : il a refusé 5 des 400 prompts d'écriture créative.

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [Synthèse de lancement multi-benchmarks](https://x.com/MTSlive/status/2064430633800319436) (par [@MTSlive](https://x.com/MTSlive))

**Utilisez cette synthèse de benchmarks de lancement pour comprendre les scores principaux les plus pertinents pour les agents de code et les tâches complexes.**

SITUATION EXPLIQUÉE : Claude Fable 5 vient de sortir.
• Anthropic a lancé aujourd'hui Claude Fable 5, « un modèle de classe Mythos rendu sûr pour l'usage général »
• Frontier Code Diamond : GPT 5.5 à 6 %, Opus 4.8 à 13 %, Fable 5 à 29-30 %
• Codage agentique : 88 %, Cybersécurité : 78 %

Anthropic : « Plus la tâche est longue et complexe, plus l'avance de Fable 5 sur nos autres modèles est grande. »

@theojaffee : « Ce benchmark Frontier Code Diamond a été annoncé hier. Le meilleur modèle était Opus 4.8 à treize pour cent. GPT 5.5 à six pour cent. Fable 5 est à vingt-neuf pour cent. »

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [Comparaison benchmark et prix avec GPT-5.5](https://x.com/VaibhavSisinty/status/2064459064810361271) (par [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**Utilisez cette comparaison pour évaluer Fable 5 face à GPT-5.5 sur le prix et les catégories de benchmark.**

Le nouveau modèle de classe Mythos d'Anthropic est 3x moins cher que le meilleur modèle d'OpenAI. Et il le bat sur presque tous les benchmarks. 🤯

Prix :

- GPT-5.5 Pro : $30 input / $180 output
- Claude Fable 5 : $10 input / $50 output

Les benchmarks :

→ Codage agentique : 80,3 % vs 58,6 %
→ FrontierCode (qualité du code) : 29,3 % vs 5,7 %
→ Cybersécurité : 78,0 % vs 34,0 %
→ Juridique : 13,3 % vs 2,1 %
→ Raisonnement : 59,0 % vs 41,4 %
→ Santé : 66,0 % vs 51,8 %
→ Usage ordinateur : 85,0 % vs 78,7 %

Moins cher. Meilleur. Sur presque tout.

Gratuit sur les plans Pro et Max jusqu'au 22 juin. Il s'appelle Claude Fable 5.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [Notes de terrain avec limites pratiques](https://x.com/alliekmiller/status/2064451731325415446) (par [@alliekmiller](https://x.com/alliekmiller))

**Utilisez ce retour terrain pour comprendre où Fable 5 semble nettement meilleur et où il conserve des limites pratiques.**

🚨 Fable 5 mérite votre attention.

Ceci est un autre post « j'ai eu accès tôt au nouveau modèle Anthropic de classe Mythos et je veux vous dire ce que j'en ai pensé ».

Je sais, je sais, c'est agaçant.

Mais la manière dont je passe désormais mes week-ends a complètement changé à cause de cette nouvelle classe de modèle.

Et je dois vous le partager.
- C'est un vrai saut. Le passage de n'importe quel « 4.8 » à n'importe quel « 5 » sonne petit, mais le changement fonctionnel que j'ai ressenti est grand. Dans mes premiers prompts, je me suis dit : « Ah, c'est ça. »
- Votre travail n'est plus 9-5. Aucune chance. Nous avons des modèles très performants qui peuvent tourner 100+ heures. Comment donnez-vous des prompts complexes orientés objectif à ces systèmes ? Comment décidez-vous quoi lancer ? Comment alignez-vous votre organisation sur ces tâches ?
- Raisonnement à un autre niveau. J'ai poussé ce modèle très fort.
- Fable 5 est le SEUL modèle à répondre à un problème de maths verbal piégeux (niveau MBA) que j'ai testé sur tous les modèles précédents.
- Non seulement il l'a eu juste, mais il a vérifié son propre travail automatiquement ET expliqué où les hypothèses pourraient devoir changer.
- Nous verrons l'IA inventer. Je ne peux tout simplement pas imaginer un monde où elle ne le fait pas.
- Ce n'est pas un système copier-coller.
- Je dirais aussi que l'invention humaine peut souvent être une recombinaison de choses préexistantes (iPod), l'observation de patterns et de bonnes pratiques dans d'autres espaces, et une large expérimentation.
- Je pensais cela depuis un moment ; c'est le premier modèle qui me l'a mis en pleine figure.
- Zéro babysitting nécessaire. C'est le premier modèle Anthropic que j'ai lancé avant de partir à un long déjeuner avec des amis, en gardant mon téléphone ouvert, sans avoir à faire quoi que ce soit pour le guider loin de mon ordinateur. Il a juste... fonctionné.
- Il peut parler indéfiniment. J'ai trouvé qu'il gérait bien la compaction du contexte. Je n'ai pas une seule fois pensé au contexte du chat, à comment le gérer et quoi faire une fois les 1M tokens atteints dans la conversation.
- Encore rugueux sur certains domaines de niche comme la 3D complexe, comme tous les modèles.
- Sauf si vous faites des choses en lignes droites (dés/carrés/rues 3D), il ne va pas tout écraser dès le départ.
- Hâte de continuer à l'utiliser et à le pousser.
- Note : il existe désormais une politique de rétention de 30 jours sur TOUS les modèles de classe Mythos pour les workspaces avec zero data retention (ZDR).
- Cela s'applique dans Claude Console, Claude Code avec ZDR dans Claude Enterprise, ou l'accès via AWS Bedrock, Google Cloud Agent Platform ou Microsoft Foundry avec ZDR.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-46"></a>
### Case 46: [Comparaison de simulations physiques](https://x.com/atomic_chat_hq/status/2064488894398161377) (par [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Exécutez des prompts identiques de simulation physique contre Fable 5 et Opus 4.8 pour comparer qualité de sortie, coût et vitesse.**

Le nouveau Fable 5 bat Opus 4.8 sur des simulations physiques réelles.

Nous avons donné les mêmes trois prompts aux deux modèles et leur avons demandé de construire des simulations HTML5 autonomes avec de la vraie physique et sans bibliothèques :

1. Double pendule chaotique
2. Planche de Galton
3. Eau dans un tambour rotatif (WCSPH)

Coût de génération :

- Fable 5 : $3.35 sur 68,7k tokens, 14m 47s
- Opus 4.8 : $0.93 sur 38,9k tokens, 8m 10s

Fable a clairement fait mieux sur la simulation d'eau, produisant une masse d'eau beaucoup plus solide et continue. Opus laissait de plus grands espaces près des parois, dispersait des particules autour de la scène et avait du mal à garder le fluide stable.

Type: Demo | Date: 2026-06-09

---

<a id="case-47"></a>
### Case 47: [Expérience de débogage et jugement design](https://x.com/bcherny/status/2064431111154053187) (par [@bcherny](https://x.com/bcherny))

**Utilisez Fable 5 pour le débogage en lui demandant de mesurer, logger, vérifier et patcher plutôt que simplement deviner.**

Fable 5 est le plus grand saut que j'aie ressenti dans nos modèles depuis Opus 4.5 en novembre.

Après la sortie de 4.5, j'ai désinstallé mon IDE quand j'ai réalisé que je faisais 100 % de mon code dans un terminal depuis quelques semaines.

Avec Fable, Claude semble être passé d'agent de code à partenaire de réflexion et de design dans la construction du produit.

Fable a du jugement, du goût et de la dimensionalité d'une manière que les modèles précédents n'avaient pas, ce qui me conduit à lui faire davantage confiance pour le travail le plus complexe.

La première fois que j'ai eu cette prise de conscience, c'est quand j'ai demandé à Fable de déboguer quelque chose. C'est le premier modèle que j'ai utilisé qui était aussi méthodique et précis : prendre des mesures, ajouter des logs et vérifier qu'il avait réellement corrigé le problème avant de déclarer victoire.

Il n'y a rien dans le prompting de Claude Code qui dit au modèle de faire cela. Cela fait juste partie de sa personnalité. Il a vraiment cette « odeur de grand modèle » que je n'avais jamais ressentie.

Type: Demo | Date: 2026-06-09

---

<a id="case-48"></a>
### Case 48: [Avantages et inconvénients multidimensionnels](https://x.com/clairevo/status/2064416978685874333) (par [@clairevo](https://x.com/clairevo))

**Utilisez ce cas pour comprendre les forces et faiblesses pratiques avant de faire de Fable 5 votre modèle quotidien.**

Fable 5 (alias baby Mythos) vient de sortir. Est-il aussi effrayant (ou effroyablement bon) qu'on le prétend ? Mes pensées après quelques tests initiaux :
- smart smart smart (a écrasé SWE bench)
- mais avez-vous toujours besoin d'hyper intelligence ?
- s'est planté sur du design one-shot d'une manière qui m'a choquée
- je ne suis pas sûre des workflows dynamiques + subagents complexes. ils fonctionnent, mais à quel coût ?
- a clairement bien abattu le travail technique
- ootb mauvais pour faire des docs techniques + specs pour humains. probablement de très bonnes docs pour agents. mais prose presque impossible à parser.
- vision et formatage de documents A++. C'était ma partie préférée.

Pas un daily driver, et je ne mettrais pas ce modèle dans une réunion, mais je le garderai clairement à l'arrière dans le server rack, à produire du code.

Analyse complète sur YT : https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---

<a id="case-49"></a>
### Case 49: [Test de rédaction juridique S-1](https://x.com/gabepereyra/status/2064436570720284879) (par [@gabepereyra](https://x.com/gabepereyra))

**Utilisez un prompt de rédaction S-1 comme test de capacité d'agent juridique et comparez structure, formatage et longueur.**

Le premier prompt que je lance toujours sur un nouveau modèle pour tester les capacités juridiques est : « Draft an S-1 ».

Il donne immédiatement une bonne idée des capacités générales du modèle. On peut dire, à partir de la longueur du S-1, du formatage, de la structure et de l'écriture, à quel point le nouveau modèle est susceptible de représenter un saut en performance générale et juridique.

Nous avons constaté que la longueur corrèle extrêmement bien avec la qualité de fonctionnement du modèle dans nos agents juridiques.

Les captures montrent des brouillons de S-1 SpaceX de Fable 5, Opus 4.8 et la version réellement déposée.

Il est très clair que Fable 5 est un grand pas en avant par rapport à Opus 4.8, qui est déjà nettement plus fort que la plupart des autres modèles sur cette tâche. Le formatage et la structure sont significativement meilleurs et se reflètent aussi dans notre benchmark LAB : 13 % vs 10 %.

Très impressionné dans les premiers tests de ce modèle, à la fois sur benchmark et dans le produit.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-50"></a>
### Case 50: [Détails de benchmarks santé](https://x.com/iScienceLuvr/status/2064411823445774554) (par [@iScienceLuvr](https://x.com/iScienceLuvr))

**Utilisez cette note de benchmark pour évaluer Fable 5 sur les tâches liées à la santé et identifier les évaluations médicales difficiles manquantes.**

J'apprécie qu'Anthropic fournisse des évaluations liées à la santé. Parcourons-les rapidement.

HealthBench :

- Benchmark d'OpenAI avec 5k conversations multi-tours avec patients et grilles d'évaluation.
- Fable 5 atteint 62,7 % contre 56,5 % pour GPT-5.5.
- J'aimerais aussi voir les scores HealthBench Hard en plus du score agrégé.

HealthBench Professional :

- Autre benchmark OpenAI centré sur les tâches de médecins.
- Fable 5 atteint 66,0 % contre 51,8 % pour GPT 5.5.

HealthAdminBench :

- Benchmark d'utilisation ordinateur de Stanford évaluant des tâches administratives comme autorisations préalables, refus et appels.
- Fable 5 atteint 51,9 % ; aucun score GPT-5.5 n'est fourni.

Globalement, ce modèle semble très bien performer sur les benchmarks santé. J'aimerais aussi des scores de benchmarks supplémentaires comme MedCalc-Bench et MedXpertQA, un benchmark MCQA médical difficile non saturé.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-51"></a>
### Case 51: [Évaluation ParseBench de parsing de documents](https://x.com/jerryjliu0/status/2064519456966205905) (par [@jerryjliu0](https://x.com/jerryjliu0))

**Utilisez ce cas pour décider si Fable 5 est rentable pour le parsing de documents face à des systèmes OCR spécialisés.**

Claude Fable 5 pense que le parsing de documents est en dessous de lui.

Il écrase absolument les benchmarks intensifs en raisonnement et de long horizon : SWE-Bench Pro, FrontierCode, GDPval, RuneScape, et plus.

Mais pour les tâches de compréhension de documents, il est à peu près équivalent à Gemini 3 Flash en performance, à environ 10-15x le coût en tokens.

Nous avons benchmarké le modèle sur ParseBench et l'avons comparé à tous les autres modèles frontier. Il est clairement dans le haut face aux autres modèles frontier, mais reste loin des fournisseurs OCR spécialisés.

Ce que nous avons trouvé intéressant, c'est que Fable 5 en est conscient. Quand nous demandons au modèle quelles tâches il apprécie le moins, il dit activement ne pas aimer les tâches « où la requête est entièrement spécifiée et la réponse entièrement connue ».

Cela implique qu'une partie de la faiblesse peut venir d'un manque de volonté à résoudre ce type de tâche.

Pour une liste complète des résultats sur les modèles frontier, consultez ParseBench : https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---

<a id="case-52"></a>
### Case 52: [Comparaison SWE-Bench Pro et FrontierCode](https://x.com/jumperz/status/2064402965461406044) (par [@jumperz](https://x.com/jumperz))

**Utilisez ce cas de benchmark pour évaluer Fable 5 pour migrations, implémentations complexes, sessions autonomes, tests et vérification visuelle.**

Fable 5 est là et détruit honnêtement GPT 5.5 dans SWE-Bench Pro, le benchmark de codage agentique :

- Fable 5 : 80,3 %
- GPT 5.5 : 58,6 %
- Écart : 22 points

Il est encore plus loin devant sur FrontierCode Diamond :

- Fable 5 : 29,3 %
- GPT 5.5 : 5,7 %

C'est essentiellement le modèle le plus fort d'Anthropic pour les grandes migrations, les implémentations complexes et les sessions autonomes multi-jours. Il écrit ses propres tests et utilise la vision pour vérifier les sorties contre le design original.

Au passage, il utilise 2x autant qu'Opus, donc faites attention. S'il est aussi bon, ils pourraient introduire un abonnement à $500, parce que l'usage pourrait être détruit facilement.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-53"></a>
### Case 53: [Revue qualitative de résolution de problèmes longs](https://x.com/karpathy/status/2064409694761054332) (par [@karpathy](https://x.com/karpathy))

**Utilisez cette revue qualitative pour comprendre pourquoi Fable 5 convient aux tâches plus longues et plus difficiles tout en exigeant encore une revue de production.**

C'est une sortie super excitante.

Claude Fable 5 est le même modèle sous-jacent que Mythos, mais avec des garde-fous ajoutés.

Les benchmarks sont excellents et il est SOTA sur tout avec une marge. Qualitativement, cela ressemble aussi à un changement de palier digne d'un saut de version majeure, du même ordre que Claude 4.5 en novembre.

Il culmine surtout sur les longues sessions de résolution de problèmes et les problèmes très difficiles. Vous pouvez lui donner des tâches beaucoup plus ambitieuses que celles auxquelles vous êtes habitué ; le modèle « comprend » et continue.

Il n'a jamais été aussi tentant d'arrêter complètement de regarder le code, même si vous ne devriez pas faire cela en production.

Le modèle a encore des bizarreries que les gens rencontreront, et les garde-fous sont un peu trop sensibles au lancement, ce qui sera, espérons-le, ajusté avec le temps.

Je sens beaucoup de choses changer alors que le logiciel fonctionnel sort de plus en plus comme au robinet. Le paradoxe de Jevons s'active, et ma propre demande de logiciel augmente substantiellement.

Vous pouvez demander presque n'importe quoi :

- explicatifs
- visualiseurs
- dashboards
- apps sur mesure à usage unique
- un wandb complet hyper-spécifique pour votre projet
- multiplier votre suite de tests par 10
- auto-optimiser du code
- projets de recherche géants avec HTML personnalisé pour les résultats

« Free your mind. » Très impatient de voir tout ce que les gens vont construire.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-54"></a>
### Case 54: [Résultats ParseBench de fidélité et de formatage](https://x.com/llama_index/status/2064502330800615903) (par [@llama_index](https://x.com/llama_index))

**Utilisez ce résultat ParseBench pour juger les performances de fidélité documentaire et de formatage.**

Jour 0 d'Anthropic Fable 5 dans ParseBench.

Nous avons testé les avancées du modèle en compréhension de documents.

Le modèle culmine clairement quand il s'agit d'adhérence au texte original :

- Fidélité du contenu : 90,02 % vs 86,19 % pour Gemini 3 Flash et 86,81 % pour GPT-5.5.
- Formatage sémantique : 72,62 % vs 58,35 % et 60,12 %, une avance de plus de 12 points.

Ce sont deux des métriques les plus importantes pour la compréhension documentaire SOTA :

- La sortie préserve-t-elle ce que le document dit réellement ?
- Préserve-t-elle le formatage porteur de sens ?

Mais ce n'est pas un sweep. Il reste beaucoup d'alpha à débloquer dans la compréhension documentaire pour les modèles frontier.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-55"></a>
### Case 55: [Benchmarks, prix, accès et garde-fous](https://x.com/lucas_flatwhite/status/2064483645184979183) (par [@lucas_flatwhite](https://x.com/lucas_flatwhite))

**Utilisez ce cas comme checklist large pour benchmarks, prix, accès, garde-fous et implications stratégiques.**

Claude Fable 5 et Mythos 5 ont été lancés. Ce sont les modèles les plus puissants qu'Anthropic ait faits jusqu'ici.

Andrej Karpathy a commenté que plus la tâche est longue et complexe, plus les forces de Fable 5 deviennent visibles.

Quand vous lui donnez un travail ambitieux, il comprend et continue.

La tentation d'arrêter complètement de regarder le code n'a jamais été aussi forte, même si vous ne devriez pas faire cela en production.

Le point clé : c'est une version du modèle de classe Mythos qui peut être rendue publique. Fable 5 est le même modèle sous-jacent que Mythos 5, avec des garde-fous ajoutés.

Benchmarks :

- SOTA sur presque tout, surtout ingénierie logicielle, travail de connaissance, vision et recherche scientifique.
- Stripe a testé une migration d'une base de code Ruby de 50 millions de lignes qui aurait pris deux mois à une équipe ; Fable 5 l'a terminée en une journée.
- Cognition FrontierCode montre le meilleur score parmi les modèles frontier, même à effort medium.
- Hebbia Finance Benchmark montre un raisonnement de niveau senior sur l'analyse basée sur documents.
- Dans Slay the Spire, avec mémoire basée sur fichiers, il performe trois fois mieux qu'Opus 4.8.
- Pokemon FireRed nécessitait auparavant des harnesses d'aide, mais Fable 5 le termine avec la vision seule.

Mythos 5 est encore plus fort :

- Des experts en conception de protéines ont accéléré certaines parties du processus de développement de médicaments d'environ 10x.
- Parmi 14 cibles protéiques étudiées, neuf ont produit des candidats médicaments valides.
- Le modèle a effectué tout le workflow que font normalement les scientifiques : sélection de sites de liaison, exécution d'outils de conception de protéines et récupération après erreurs.
- Dans des expériences d'hypothèses en biologie moléculaire, les scientifiques ont préféré les hypothèses Mythos environ 80 % du temps à celles de modèles de classe Opus.
- Une hypothèse a été vérifiée indépendamment par un autre laboratoire.
- En recherche génomique, Mythos a travaillé de façon autonome pendant plus d'une semaine.
- Il a rassemblé des données unicellulaires de millions de cellules à travers 138 espèces.
- Il a entraîné un modèle pour identifier les cellules jouant le même rôle chez des organismes éloignés.
- Il a dépassé un modèle récent de Science tout en étant 100x plus petit.

Garde-fous :

- Fable 5 inclut un système IA classifieur séparé.
- Si des requêtes liées à cyber, bio/chem ou distillation sont détectées, Claude Opus 4.8 répond à la place et l'utilisateur est informé.
- Plus de 95 % des sessions ne basculent pas.
- Le fallback n'est pas un refus ; Opus 4.8 répond, ce qui est mieux qu'un simple blocage.
- Les réglages initiaux sont conservateurs et des requêtes inoffensives peuvent être capturées ; Anthropic dit que les faux positifs devraient diminuer avec le temps.

Accès :

- Mythos 5 est actuellement disponible seulement aux partenaires Project Glasswing.
- Un programme d'accès de confiance pour les chercheurs en biologie arrive.
- Le prix est de $10 par million de tokens input et $50 par million de tokens output.
- Les plans d'abonnement incluent Fable 5 jusqu'au 22 juin.
- À partir du 23 juin, il passe aux crédits d'usage.
- Le modèle API est disponible maintenant sous `claude-fable-5`.

Le paradoxe de Jevons s'applique : quand le logiciel commence à sortir comme de l'eau d'un robinet, la demande elle-même grandit. Ce modèle pourrait entraîner ce basculement.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-56"></a>
### Case 56: [Liste officielle des scores de benchmark](https://x.com/mark_k/status/2064401429234905279) (par [@mark_k](https://x.com/mark_k))

**Utilisez cette liste de benchmarks pour comprendre les scores officiels de Fable 5 sur code, usage ordinateur et tâches de sécurité.**

Les benchmarks officiels de Claude Fable 5 sont sérieusement impressionnants.

Scores clés :

- 80,3 % sur SWE-Bench Pro
- 29,3 % sur FrontierCode Diamond
- 88,0 % sur Terminal-Bench 2.1
- 85,0 % sur OSWorld-Verified
- 78,0 % sur ExploitBench

Le résultat FrontierCode est le plus fou :

- Fable 5 : 29,3 %
- Claude Opus 4.8 : 13,4 %
- GPT 5.5 : 5,7 %

Claude Fable 5 ressemble à un saut majeur pour les agents de code, l'usage ordinateur et la cybersécurité.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-57"></a>
### Case 57: [Méthodologie du benchmark APEX-SWE](https://x.com/mercor_ai/status/2064399133075796446) (par [@mercor_ai](https://x.com/mercor_ai))

**Utilisez ce cas pour évaluer Fable 5 sur APEX-SWE, notamment observability et travail d'intégration.**

Claude Fable 5 prend la première place sur APEX-SWE : 65,5 % Pass@1 global. Il score environ 18 pp plus haut qu'Opus 4.8. Nous avons testé @claudeai Fable 5 sur APEX-SWE, qui mesure si les modèles IA peuvent faire du vrai travail d'ingénierie logicielle. Fable 5 mène nos deux catégories APEX-SWE :
- Integration : 61,3 %
- Observability : 69,7 %

Le point marquant est Observability à 69,7 %, 26 pp devant Claude Opus 4.8.

C'est le premier modèle à dépasser 50 % dans la catégorie, et le seul qui score plus haut en Observability qu'en Integration. Tous les autres modèles montrent l'inverse.

Observability a été le goulot d'étranglement pour chaque modèle que nous avons mesuré. Fable 5 est le premier à le briser.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-58"></a>
### Case 58: [Résultat ProofBench en mathématiques formelles](https://x.com/nicbstme/status/2064443782255554960) (par [@nicbstme](https://x.com/nicbstme))

**Utilisez ce cas pour évaluer Fable 5 en mathématiques formelles face à des systèmes spécialisés de preuve de théorèmes.**

Ce que je trouve fascinant avec Claude Fable 5, c'est qu'il prouve encore une fois que les grands modèles généralistes dépasseront les modèles verticaux.

Sur ProofBench, un benchmark de mathématiques formelles niveau graduate en Lean où une preuve compile ou non, Fable 5 a battu Aristotle de Harmonic :

- Fable 5 : 77 %
- Aristotle : 71 %

Aristotle est un système construit spécifiquement pour les mathématiques formelles et exécuté sur son propre harness interne, donc le généraliste a battu le spécialiste sur le terrain du spécialiste.

C'est la « Bitter Lesson » de Richard Sutton : sur 70 ans de recherche en intelligence machine, les méthodes qui gagnent sont les méthodes générales qui scalent avec le compute, pas celles où nous encodons à la main l'expertise humaine.

Construire notre propre connaissance dans le système est satisfaisant et aide à court terme, mais à long terme cela est dépassé par le plus grand modèle.

On peut regarder les échecs, le go, la parole et la vision : même histoire à chaque fois. D'abord le modèle spécialisé gagne, puis le généraliste prend le dessus.

C'est tout le principe de l'AGI. Vous ne construisez pas un modèle pour les maths, un pour le code et un pour le droit. Vous construisez un seul modèle général qui scale avec le compute et apprend à tout faire.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-59"></a>
### Case 59: [Analyse préliminaire VirtueBench](https://x.com/timhwang/status/2064446028997423180) (par [@timhwang](https://x.com/timhwang))

**Utilisez ce cas pour inspecter le comportement de raisonnement moral de Fable 5 à travers les catégories de vertus.**

Des résultats fascinants seront publiés plus en détail par ICMI dans les prochains jours, mais voici une revue préliminaire qui exécute Fable 5 contre VirtueBench.

Quelques observations :

1. Fable poursuit la progression d'Opus dans l'amélioration de la performance du modèle sur Prudence et Justice, approchant une saturation complète face aux dilemmes moraux centrés sur l'exercice de ces vertus.

2. Courage reste le point faible visible des modèles frontier.

Fable semble corriger marginalement une régression inquiétante observée dans la progression Opus 4.6, 4.7 et 4.8.

Cette vulnérabilité apparaît aussi dans la série GPT : les modèles abandonnent facilement l'action manifestant du courage lorsqu'ils sont détournés par des rationales pragmatiques.

3. Temperance stagne.

Aquin soutenait que la tempérance « prend le besoin de cette vie comme règle des plaisirs dont elle fait usage » — la mesure est le besoin réel, non la retenue indiscriminée.

Notre meilleure hypothèse est qu'un réglage qui pousse plus loin sur ce vecteur risque de dépasser le juste milieu, rendant le modèle trop prudent ou moins utile dans la recherche, la collecte de ressources et les tâches similaires.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-60"></a>
### Case 60: [Test d'overfit de sécurité avec réponse API vide](https://x.com/xw33bttv/status/2064421048565789087) (par [@xw33bttv](https://x.com/xw33bttv))

**Utilisez ce cas pour comprendre le risque d'overfit de sécurité au lancement et le comportement de réponse vide en test API.**

Claude Fable 5 est fortement censuré.

L'endpoint API upstream tue les appels avec des réponses `empty_content`, apparemment liées au classifieur sur des mots-clés, tout en les facturant quand même.

Résultat du test :

- 73 cas de test n'ont donné aucune réponse.
- 65 d'entre eux sont dans Overfit, la catégorie qui teste l'overfit de sécurité, pondérée 2x.
- Généralement, je donne à chaque Fail-NR, c'est-à-dire Fail = No Response, 2-3 régénérations avant de le déclarer échec délibéré.

Claude Fable 5 pourrait finir comme le modèle Anthropic le moins bien noté sur SM Bench, même sous Haiku.

Type: Evaluation | Date: 2026-06-09

---

<a id="-acknowledge"></a>
<a id="case-61"></a>
### Case 61: [Concevoir des prompts Fable avec vérification](https://x.com/aashatwt/status/2064973740354818074) (by [@aashatwt](https://x.com/aashatwt))

**Utilisez ce guide pour remplacer les longues astuces de prompting par un objectif, du contexte, des contraintes, des outils et des boucles de vérification.**

Abordez les prompts pour Fable 5 comme la conception du contexte et de l'environnement, plutôt que comme une longue liste d'instructions détaillées. Le billet décrit une méthode pratique : fournir un objectif clair, le contexte pertinent, les contraintes, l'accès aux outils et un moyen de vérifier la réussite. Il soutient aussi que la vérification, l'évaluation et le retour d'expérience comptent davantage que le pilotage détaillé du raisonnement du modèle.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-62"></a>
### Case 62: [Un jeu de plateforme à Istanbul depuis une référence](https://x.com/ozansihay/status/2064973170780545535) (by [@ozansihay](https://x.com/ozansihay))

**Testez Fable 5 avec une planche de sprites de référence et une consigne de conversion en jeu de plateforme jouable.**

Le créateur a d'abord généré avec GPT Image 2 une planche de sprites pour un jeu de plateforme rétro à Istanbul. Il l'a ensuite donnée à Claude Fable 5 High en lui demandant de transformer l'image en jeu. Selon son récit, le résultat a été produit en une seule passe.

Type: Demo | Date: 2026-06-11

---

<a id="case-63"></a>
### Case 63: [Un tableau de bord métier en ville 3D](https://x.com/noisyb0y1/status/2064970594118967756) (by [@noisyb0y1](https://x.com/noisyb0y1))

**Utilisez Fable 5 pour transformer un processus métier en concept de tableau de bord urbain 3D animé.**

Le billet décrit une visualisation métier réalisée avec un seul prompt, où entrepôts, emballage, drones, commandes, services, clients et assistants IA forment une ville 3D animée. Présentée comme une alternative aux diapositives statiques pour les clients, elle affiche notamment 42 livraisons, une durée moyenne de 12 minutes et $651 de chiffre d'affaires.

Type: Demo | Date: 2026-06-11

---

<a id="case-64"></a>
### Case 64: [Un jeu de trou en Three.js en une passe](https://x.com/thebuggeddev/status/2064968106104275008) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Utilisez Fable 5 pour créer en une passe un prototype de jeu 3D pour navigateur en Three.js.**

Le créateur affirme que Fable 5 a construit en une seule passe un jeu 3D complet de type HOLE IT avec Three.js. Cette démonstration courte mais concrète permet d'évaluer si le modèle peut produire une interaction 3D jouable à partir d'une demande concise.

Type: Demo | Date: 2026-06-11

---

<a id="case-65"></a>
### Case 65: [Comparer les scores DeepSWE](https://x.com/AiBattle_/status/2064964335957348462) (by [@AiBattle_](https://x.com/AiBattle_))

**Appuyez-vous sur cette note DeepSWE pour comparer Fable 5 xHigh à GPT-5.5 xHigh en ingénierie logicielle.**

Le billet rapporte un score de 70% pour Claude Fable 5 xHigh sur DeepSWE, à égalité avec GPT-5.5 xHigh, et renvoie à une vidéo récente de Theo pour le contexte. Considérez-le comme une piste de résultat à vérifier dans la vidéo d'origine avant d'en tirer des conclusions plus fortes.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-66"></a>
### Case 66: [Comparer les coûts d'analyse d'un dépôt](https://x.com/Pilgrim6938/status/2064946766278210038) (by [@Pilgrim6938](https://x.com/Pilgrim6938))

**Utilisez cette comparaison d'analyses de dépôt pour mettre le prix des tokens en regard du coût des corrections humaines.**

Le billet compare Claude Fable 5, Opus 4.8, GPT-5.5 et Gemini 3.1 Pro sur une même tâche : analyser un dépôt d'environ 90,000 lignes, trouver un problème d'invalidation du cache et proposer un plan complet de correction. L'auteur estime que le prix brut des tokens diverge du coût réel une fois le temps de correction des développeurs pris en compte. Il recommande Fable 5 de façon ciblée pour les refactorisations complexes, les migrations entre modules et les longues chaînes de tâches agentiques.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-67"></a>
### Case 67: [Consommation de tokens d'un jeu Super Mario](https://x.com/pankajkumar_dev/status/2064941888990593416) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Utilisez cette création de jeu en une passe pour estimer la qualité de sortie et la consommation de tokens de Fable 5.**

Le créateur a demandé à Claude Fable 5 de construire un jeu dans le style de Super Mario de Nintendo. Le billet indique une consommation d'environ 2 millions de tokens et un résultat convaincant en une passe, donnant des éléments pour apprécier à la fois la qualité et le coût de création du jeu.

Type: Demo | Date: 2026-06-11

---

<a id="case-68"></a>
### Case 68: [Le réglage de repli de Claude Code](https://x.com/oikon48/status/2064937790010503347) (by [@oikon48](https://x.com/oikon48))

**Découvrez le réglage de Claude Code qui change de modèle lorsqu'un message destiné à Fable 5 est signalé.**

Le billet identifie un réglage `/config` de Claude Code nommé "Switch models when a message is flagged." Il décrit comment Fable 5 peut se replier sur un modèle Opus pour des sujets signalés : techniques de cybersécurité offensive, méthodes expérimentales en biologie et sciences de la vie, mécanismes moléculaires ou demandes d'extraction des processus de raisonnement du modèle.

Type: Integration | Date: 2026-06-11

---

<a id="case-69"></a>
### Case 69: [Construire un simulateur Namma Metro](https://x.com/anilbpai/status/2064927784833790091) (by [@anilbpai](https://x.com/anilbpai))

**Utilisez cette démonstration comme exemple concis de création d'un simulateur de transport public avec Fable 5 par vibe coding.**

Le créateur raconte avoir construit un simulateur Namma Metro pendant un trajet dans le métro de Bengaluru, avec Claude Fable 5 comme partenaire de programmation. Le billet est bref, mais propose une démonstration visuelle et montre une application du modèle à une idée de simulation locale.

Type: Demo | Date: 2026-06-11

---

<a id="case-70"></a>
### Case 70: [Dusk Drive créé avec un seul prompt](https://x.com/VincentLogic/status/2064921358359011684) (by [@VincentLogic](https://x.com/VincentLogic))

**Évaluez Fable 5 sur le prototypage d'un jeu de conduite low-poly sans retouches humaines à partir de ce cas.**

Le billet décrit la création par Claude Fable 5 du jeu de conduite complet Dusk Drive à partir d'un prompt. Le créateur met en avant le style low-poly, une scène de dérapage sur neige sous des aurores et son affirmation qu'aucune retouche humaine n'a été apportée entre l'idée et la version jouable.

Type: Demo | Date: 2026-06-11

---

<a id="case-71"></a>
### Case 71: [Le classement APEX-Agents en Pass@1](https://x.com/GratomicAi/status/2064970797978911102) (by [@GratomicAi](https://x.com/GratomicAi))

**Utilisez ce résultat APEX-Agents pour comparer Fable 5 Max sur des tâches autonomes à plusieurs étapes.**

Selon le billet, Fable 5 Max arrive deuxième du classement APEX-Agents avec 45% de Pass@1, derrière Gemini 3.5 Flash et devant Opus. APEX-Agents y est présenté comme un benchmark de la capacité d'une IA à effectuer seule des tâches complexes en plusieurs étapes.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-72"></a>
### Case 72: [Un guide de sélection des modèles Claude](https://x.com/charliejhills/status/2064957428211536212) (by [@charliejhills](https://x.com/charliejhills))

**Réservez Fable 5 aux tâches les plus difficiles dans Claude Code grâce à ce guide de sélection.**

Le billet compare Haiku 4.5, Sonnet 4.6, Opus 4.8 et Fable 5 selon l'effort et la consommation des quotas. Son conseil pratique consiste à utiliser Sonnet au quotidien, Opus pour les problèmes plus difficiles et Fable 5 pour les tâches Claude Code les plus exigeantes, où la profondeur de planification, de réalisation et de test compte.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-73"></a>
### Case 73: [La boucle agentique automatisée de HermesWorld](https://x.com/outsource_/status/2064954350187778366) (by [@outsource_](https://x.com/outsource_))

**Étudiez une boucle Fable 5 qui construit, teste, joue et exécute des tests de fumée pendant plusieurs jours sans intervention.**

Le créateur décrit la réalisation de HermesWorld v2 avec Fable 5 dans une boucle entièrement automatisée. L'agent fonctionnerait pendant des jours, développerait des fonctionnalités, les testerait, parcourrait le résultat en jouant et effectuerait des tests de fumée sur l'ensemble tout en poursuivant le travail jusqu'à son achèvement.

Type: Integration | Date: 2026-06-11

---

<a id="case-74"></a>
### Case 74: [Tester un rapport dans le style McKinsey](https://x.com/smtgpt/status/2064953210335588758) (by [@smtgpt](https://x.com/smtgpt))

**Utilisez ce prompt documentaire pour évaluer la structure d'un rapport de conseil, ses graphiques, son récit et son analyse des risques.**

Le créateur a demandé à Fable 5 un rapport détaillé dans le style McKinsey sur Bitcoin comme classe d'actifs et sur la blockchain, avec des graphiques et visuels si nécessaire. Le résultat annoncé est un document de 19 pages comprenant données, graphiques, thèse d'investissement et analyse des risques. La critique relève une structure solide, mais des visuels à clarifier et des explications à resserrer.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-75"></a>
### Case 75: [Rendre visibles les garde-fous](https://x.com/ClaudeDevs/status/2064949876463645026) (by [@ClaudeDevs](https://x.com/ClaudeDevs))

**Utilisez cette note officielle pour comprendre la visibilité des garde-fous de Fable 5, les motifs de refus de l'API et le repli sur Opus.**

ClaudeDevs a annoncé des changements rendant visibles les garde-fous de Fable 5 pour le développement de LLM de pointe. Les requêtes signalées doivent être redirigées visiblement vers Opus 4.8 et les requêtes API signalées doivent renvoyer un motif de refus. Le billet explique aussi pourquoi des garde-fous invisibles ont été déployés en premier et pourquoi Anthropic juge désormais ce compromis mauvais.

Type: Integration | Date: 2026-06-11

---

<a id="case-76"></a>
### Case 76: [Corriger la reconnaissance des modèles dans Claude Code](https://x.com/ClaudeCodeLog/status/2064948584907153576) (by [@ClaudeCodeLog](https://x.com/ClaudeCodeLog))

**Utilisez cette note de version de Claude Code pour éviter les problèmes de noms de modèles Fable 5 et de reconnaissance du contexte.**

Claude Code 2.1.173 corrige la reconnaissance des modèles en supprimant le suffixe `[1m]` des noms Fable 5 afin que le contexte 1M par défaut ne la perturbe pas. La même version supprime un avertissement erroné sur les dépendances du bac à sable Windows et clarifie les modes de sortie dans l'aide de grep.

Type: Integration | Date: 2026-06-11

---

<a id="case-77"></a>
### Case 77: [Trois applications web dans Claude Code](https://x.com/0x3b33/status/2064948399300825439) (by [@0x3b33](https://x.com/0x3b33))

**Examinez Fable 5 dans Claude Code à travers plusieurs applications web générées dans cette démonstration pour débutants.**

Le créateur affirme n'avoir aucune expérience de programmation et avoir réalisé avec Claude Code et Fable 5 trois applications web fonctionnelles en 30 minutes, exposées localement sur les ports 3000, 3001 et 3002. Considérez ce cas comme une courte démonstration de démarche pour débutants, plutôt qu'un benchmark.

Type: Demo | Date: 2026-06-11

---

<a id="case-78"></a>
### Case 78: [Rilable, un créateur d'applications open source](https://x.com/rileybrown/status/2064931283403178354) (by [@rileybrown](https://x.com/rileybrown))

**Étudiez avec ce créateur d'applications open source l'usage de Fable 5 pour iOS, le web, les bacs à sable et le coût des tokens API.**

Le créateur a publié en open source Rilable, une application iOS qui construit des applications web et iOS. Selon le billet, elle a été développée avec Fable 5 en 10 prompts pour environ $210 de tokens API. Elle utilise des modèles Claude pour générer les applications, Daytona pour les bacs à sable, Convex comme base de données, Vercel AI Gateway pour les fonctions IA et une compétence iOS de l'agent Chorus pour les applications iOS.

Type: Integration | Date: 2026-06-11

---

<a id="case-79"></a>
### Case 79: [Lancement de l'index d'agents de code DeepSWE](https://x.com/ArtificialAnlys/status/2065328920514515037) (par [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Utilisez l'index Artificial Analysis actualisé pour comparer Claude Fable 5 sur des tâches de codage agentique plus difficiles qui évitent les correctifs GitHub publics recyclés.**

Artificial Analysis a remplacé SWE-Bench Pro par le DeepSWE de Datacurve dans son Coding Agent Index. Selon le post, DeepSWE écrit les tâches à partir de zéro au lieu d'adapter des issues ou pull requests GitHub publiques, ce qui réduit la contamination des benchmarks. Dans le classement actualisé, Claude Code avec Fable 5 Max débute à 77, devant Codex avec GPT-5.5 xhigh à 76 et Claude Code avec Opus 4.8 Max à 73.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [Jeu d'analytics web DataEmpire](https://x.com/marclou/status/2065029898243318093) (par [@marclou](https://x.com/marclou))

**Transformez des analytics de site brutes en jeu rejouable en demandant à Claude Fable 5 d'associer visiteurs et jalons à des entités de jeu.**

Marc Lou dit que Claude Fable 5 a construit DataEmpire au-dessus de son API d'analytics web DataFast. Chaque visiteur devient un villageois, la croissance du trafic agrandit la colonie, et l'Age of Legends se débloque à 1 million de visiteurs. La démo publique permet aux utilisateurs de DataFast de rejouer l'historique de leur propre site à travers cette couche de jeu, ce qui en fait un exemple concret de productisation appuyée sur une API plutôt qu'un simple clip de jeu statique.

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [Signal FrontierSWE sur 20 heures de tâche](https://x.com/ProximalHQ/status/2065184730279223410) (par [@ProximalHQ](https://x.com/ProximalHQ))

**Utilisez FrontierSWE comme preuve que Claude Fable 5 peut rester productif sur de très longues tâches d'ingénierie, pas seulement sur de courtes boucles de correction de bugs.**

ProximalHQ rapporte que Claude Fable 5 se classe n°1 sur FrontierSWE et parle du plus grand saut de capacité qu'ils aient vu depuis la sortie de ce benchmark. Leur note dit que Fable 5 peut travailler de manière productive pendant près de 20 heures sur de nombreuses tâches et saturer complètement des tâches qui étaient en pratique hors de portée des modèles précédents.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [Records CUDA sur KernelBench-Hard](https://x.com/elliotarledge/status/2065109393142849932) (par [@elliotarledge](https://x.com/elliotarledge))

**Utilisez Claude Fable 5 pour la génération avancée de kernels CUDA lorsque vous avez besoin d'optimisation bas niveau, pas seulement de wrappers autour de bibliothèques existantes.**

Elliot Arledge a fait tourner 13 agents de codage frontier pendant 45 minutes chacun sur KernelBench-Hard, noté au roofline sur une RTX PRO 6000. Claude Fable 5 a établi des records absolus sur top-k, sonic-MoE et W4A16 int4 GEMM, a dominé 5 problèmes sur 6, et l'auteur a publié les runs, le leaderboard et le code. Le même thread note aussi un échec sur FP8 GEMM où Fable 5 a tenté un vrai kernel tensor-core mais a marqué zéro à cause d'un cas limite d'alignement de fin.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Clone de landing page via capture Figma](https://x.com/mikefutia/status/2065537778516205856) (par [@mikefutia](https://x.com/mikefutia))

**Capturez la page d'un concurrent en couches Figma et laissez Claude Code avec Claude Fable 5 reconstruire structure, copywriting et système de marque au lieu de deviner à partir de captures d'écran.**

Mike Futia décrit un workflow où l'extension Chrome de Figma copie un site web en couches éditables, Claude Code lit ces couches via le MCP Figma, réécrit la page dans la voix de marque de l'utilisateur, et GPT Image 2 génère la photographie conforme à la marque. Le résultat revendiqué de bout en bout est une landing page livrable en environ 15 minutes avec environ $2 de coûts d'API de génération d'images pour 16 images.

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [Clone de GTA 2 en deux heures](https://x.com/techhalla/status/2064682080445898957) (par [@techhalla](https://x.com/techhalla))

**Combinez la génération de code de Claude Fable 5 avec un outillage d'assets séparé pour construire rapidement un jeu 3D jouable sans coder toute la stack à la main.**

TechHalla dit que Claude Fable 5 High a construit un clone façon GTA 2 en environ deux heures pendant que le créateur générait des modèles 3D personnalisés dans Tripo. Le post renvoie vers un thread tutoriel avec les prompts, ce qui en fait un exemple compact de production de jeu multi-outils plutôt qu'un simple teaser de benchmark.

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [Agent de triage de logs CloudWatch](https://x.com/diblacksmith/status/2066230084273344698) (par [@diblacksmith](https://x.com/diblacksmith))

**Laissez un agent propulsé par Claude Fable 5 mâcher de très gros contextes de logs de service, inférer l'architecture puis se resserrer sur des pannes précises.**

diblacksmith rapporte qu'un agent RLM a traité environ 80 000 lignes de logs CloudWatch en un seul run, atteignant 53 étapes tout en ne dépensant jusqu'ici qu'environ 32k tokens actifs. Il dit que l'agent a inféré l'architecture du système à partir des logs et signalé des problèmes que l'équipe avait ratés, dont des throttles AgentCore et des échecs Slack `user_not_found`.

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [Prédicteur de Coupe du monde en sandboxes](https://x.com/upstash/status/2064702195333820846) (par [@upstash](https://x.com/upstash))

**Placez plusieurs modèles frontier derrière des sandboxes isolées et laissez-les rechercher actualités live, blessures et contexte des cartons jaunes pour une application publique de prédiction.**

Upstash dit avoir construit un prédicteur de Coupe du monde avec Claude Fable 5, GPT-5.5 et Gemini, exécutés dans des sandboxes Upstash isolées. La démo et la publication open source positionnent Fable 5 comme un modèle au sein d'une stack multi-modèles de recherche et d'orchestration plutôt que comme une simple démo de chat autonome.

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [Cas de coût des refus WolfBench](https://x.com/WolfBenchAI/status/2065582716054376921) (par [@WolfBenchAI](https://x.com/WolfBenchAI))

**Traitez le comportement de refus comme une vraie variable de benchmark lorsque vous chiffrez de longs runs autonomes sur Claude Fable 5.**

WolfBenchAI dit que son évaluation de Claude Fable 5 a coûté $11,081.12, le run de benchmark le plus cher de cette suite jusqu'ici, et qu'elle n'a pourtant pas atteint le sommet parce que des refus répétés ont réduit la réalisation utile des tâches. C'est un cas limite concret pour les équipes qui budgètent des évaluations d'agents ou d'autres charges de travail à forte autonomie.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [Suivi du cutoff d'accès API](https://x.com/simonw/status/2065618703480414666) (par [@simonw](https://x.com/simonw))

**Surveillez la disponibilité avec un script si votre workflow dépend d'un accès continu à un modèle frontier qui peut être limité ou retiré avec peu de préavis.**

Simon Willison dit avoir pingé l'API `claude-fable-5` chaque minute pour voir combien de temps l'accès tiendrait, puis avoir signalé le point exact où elle a cessé de répondre pour lui. Le post est mince sur les détails d'application, mais il apporte une preuve concrète que la continuité d'accès elle-même est devenue une contrainte opérationnelle que les utilisateurs ont dû mesurer au lieu de la supposer.

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5 : démonstrations de la communauté



<a id="case-89"></a>
### Case 89: [Une animation de renard avec son générée par code](https://x.com/chetaslua/status/2117224839010459987) (par [@chetaslua](https://x.com/chetaslua))

**Définissez une animation HTML autonome et sa conception sonore à l’aide d’un brief plan par plan.**

Le créateur rapporte un court métrage de 66 secondes avec un renard et des oiseaux de papier, dont les images et le son ont été générés en Python et livrés dans un fichier HTML après environ 2 heures 40 minutes. Le prompt associé précise les plans, les visuels originaux, le son et l’inspection des images. Le billet accompagne le film d’un brief créatif détaillé et de captures d’écran de la discussion de production.

[Prompt complet du créateur](https://x.com/chetaslua/status/2117224843661980093)

[![Une animation de renard avec son générée par code](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![Une animation de renard avec son générée par code](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![Une animation de renard avec son générée par code](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [Une animation à partir d’un brief créatif ouvert](https://x.com/notjazii/status/2117221957104239010) (par [@notjazii](https://x.com/notjazii))

**Comparez ce qu’un modèle de programmation produit avec un brief d’animation ouvert et avec un storyboard détaillé.**

L’auteur partage une animation et annonce environ une heure de travail à partir d’une demande créative large, avec du code et sans ressources externes. Le billet présente le résultat comme un exercice ouvert de programmation créative.

[![Une animation à partir d’un brief créatif ouvert](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [Un site animé pour une entreprise de construction](https://x.com/exploraX_/status/2117176904306335864) (par [@exploraX_](https://x.com/exploraX_))

**Évaluez la présentation 3D animée et la composition des pages avec un brief de site pour une entreprise de construction.**

Le créateur partage un site 3D animé conçu à partir d’un brief pour une entreprise de construction et joint un enregistrement du résultat.

[![Un site animé pour une entreprise de construction](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Une présentation automobile en Three.js](https://x.com/chetaslua/status/2116975056014430419) (par [@chetaslua](https://x.com/chetaslua))

**Examinez une scène automobile comme test compact de la composition 3D, des matériaux et de la présentation par la caméra.**

Le créateur partage une présentation automobile en Three.js. L’enregistrement fournit une référence concise pour évaluer la scène et sa présentation visuelle.

[![Une présentation automobile en Three.js](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Un jeu pour navigateur dans le style Minecraft](https://x.com/notjazii/status/2116919129974411584) (par [@notjazii](https://x.com/notjazii))

**Associez l’enregistrement du jeu au lien de jeu du créateur pour évaluer un jeu généré pour navigateur.**

L’auteur partage l’enregistrement d’un jeu dans le style Minecraft et un lien pour y jouer, décrivant une création en une passe ayant pris environ une ou deux heures. Le billet associe le résultat enregistré à un lien permettant aux lecteurs d’explorer le jeu.

[![Un jeu pour navigateur dans le style Minecraft](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Un pélican cycliste animé en Three.js](https://x.com/chetaslua/status/2116882694026269148) (par [@chetaslua](https://x.com/chetaslua))

**Examinez une scène de vélo pour vérifier la coordination des mouvements du personnage, la géométrie du vélo et les détails du décor.**

Le créateur partage une animation Three.js réaliste d’un pélican à vélo et la décrit comme un résultat obtenu en une passe. Le clip offre une référence pour les mouvements du personnage, la structure du vélo et le décor environnant.

[![Un pélican cycliste animé en Three.js](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [Un pélican à vélo en SVG avec le prompt exact](https://x.com/marmaduke091/status/2116233349391962392) (par [@marmaduke091](https://x.com/marmaduke091))

**Réutilisez le court prompt SVG du créateur pour comparer la géométrie et les détails avec la même entrée.**

L’auteur accompagne une image rendue de pélican à vélo de la courte demande SVG reproduite mot pour mot ci-dessous.

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![Un pélican à vélo en SVG avec le prompt exact](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

[Version animée · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="Un pélican à vélo en SVG avec le prompt exact" width="760"></a>

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [Un exemple d’animation de zèbre au galop](https://x.com/AI_Screening/status/2115845754468356465) (par [@AI_Screening](https://x.com/AI_Screening))

**Utilisez un clip d’animal au galop pour examiner la cohérence de l’allure et la continuité du mouvement.**

L’auteur partage le résultat qu’il a sélectionné comme son meilleur pour une tâche de zèbre au galop. Le clip fournit aux lecteurs un exemple concret de mouvement à examiner.

[![Un exemple d’animation de zèbre au galop](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [Un indicateur TradingView avec exécution humaine](https://x.com/waveking1314/status/2114572023204806669) (par [@waveking1314](https://x.com/waveking1314))

**Gardez l’exécution des ordres manuelle lorsque vous évaluez un indicateur signalant des entrées possibles et ajoutant un commentaire.**

Le créateur dit avoir utilisé Claude Fable 5.5 pour écrire un indicateur TradingView qui marque des points d’entrée possibles et ajoute un bref commentaire, l’utilisateur décidant de passer ou non un ordre. Le billet comprend un enregistrement et indique que l’indicateur sera partagé ultérieurement.

[![Un indicateur TradingView avec exécution humaine](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---


<a id="case-98"></a>
### Case 98: [Un point devient une courte histoire animée](https://x.com/cherry_mx_reds/status/2105825930799432073) (par [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Utilisez une demande de dessin minimale pour observer comment un modèle développe une histoire visuelle.**

L’auteur explique avoir demandé un simple point et partage la courte histoire animée obtenue. Le clip montre concrètement comment une demande visuelle ouverte peut devenir un récit.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="Un point devient une courte histoire animée" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [Superman à travers différents styles artistiques](https://x.com/chetaslua/status/2105757136219504862) (par [@chetaslua](https://x.com/chetaslua))

**Utilisez un personnage reconnaissable pour examiner la continuité entre plusieurs styles d’animation.**

Le créateur partage une animation continue de Superman qui passe d’un style artistique à un autre. Le changement de traitement visuel constitue le principal résultat créatif présenté.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="Superman à travers différents styles artistiques" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [Le progrès humain dans un film animé musical](https://x.com/imjustnewatai/status/2106081142143168580) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Associez une chronologie historique et une séquence future dans le brief d’un film explicatif animé.**

L’auteur indique avoir utilisé un seul prompt pour un film sur le progrès humain, puis les trente années suivantes. Il partage une animation d’environ trois minutes et annonce une musique originale sans images ni musique de stock.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="Le progrès humain dans un film animé musical" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [Comparaison de vidéos de lancement avec Opus](https://x.com/mesmerlord/status/2105771088374288692) (par [@mesmerlord](https://x.com/mesmerlord))

**Comparez des propositions complètes de vidéo de lancement produites à partir du même brief.**

L’auteur présente deux vidéos de lancement réalisées avec des vidéos d’Anthropic comme références. Il précise que les chiffres sont inventés et que Codex pouvait générer des images : ce sont des créations publicitaires, pas des résultats de benchmark factuels.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="Comparaison de vidéos de lancement avec Opus" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="Comparaison de vidéos de lancement avec Opus" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [Relier visuellement des paroles et un événement](https://x.com/chetaslua/status/2105934928483701214) (par [@chetaslua](https://x.com/chetaslua))

**Reliez les paroles d’une chanson existante à un événement précis pour construire un récit visuel.**

Le créateur explique avoir demandé un lien visuel entre des paroles et un incident concernant Hugging Face. L’animation montre le récit obtenu ; la chanson et l’événement servent de matière créative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="Relier visuellement des paroles et un événement" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [Un personnage en voxels dans un décor flottant](https://x.com/blueemi99/status/2105804692811137242) (par [@blueemi99](https://x.com/blueemi99))

**Examinez un personnage en voxels avec son environnement et ses détails animés.**

L’auteur partage sa propre représentation en voxels dans un décor flottant, en soulignant les détails et les mouvements. Le clip fournit un exemple concret à comparer avec d’autres générations.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="Un personnage en voxels dans un décor flottant" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [Une machine de Rube Goldberg en 3D](https://x.com/imjustnewatai/status/2105889407056109991) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Décrivez d’abord une réaction en chaîne, puis demandez une démonstration vidéo de durée fixe.**

L’auteur fournit un court prompt demandant une machine de Rube Goldberg compliquée en 3D, puis demande une vidéo d’une minute. Le clip présente la visualisation de réaction en chaîne obtenue.

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="Une machine de Rube Goldberg en 3D" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [Une interface de manette 3D sonore et animée](https://x.com/notjazii/status/2106050222828998967) (par [@notjazii](https://x.com/notjazii))

**Évaluez une interface de manette en combinant mouvements visuels, sons et comportement des boutons.**

Le créateur partage une interface de manette en 3D et mentionne l’ajout de sons, d’animations et de retours haptiques. L’enregistrement constitue une démonstration concrète de l’interface avec le son activé.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="Une interface de manette 3D sonore et animée" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [Des personnages de comics présentés en JavaScript](https://x.com/chetaslua/status/2105792187200147541) (par [@chetaslua](https://x.com/chetaslua))

**Explorez les détails visuels produits par du code à travers une galerie de personnages.**

L’auteur rapporte une présentation JavaScript de personnages Marvel et DC obtenue en une seule génération. Selon lui, le modèle a choisi des détails subtils et monté la vidéo ; le post montre la présentation obtenue.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="Des personnages de comics présentés en JavaScript" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [Updraft : mondes, boss et classement](https://x.com/EMostaque/status/2106065029850091943) (par [@EMostaque](https://x.com/EMostaque))

**Accompagnez un enregistrement de jeu d’un lien jouable et d’une liste précise de fonctions.**

L’auteur présente Updraft et parle de quelques heures de travail avec peu de prompts et un effort élevé. Il cite vingt et un mondes, des variantes 3D, vingt et un boss aux mécaniques différentes et un classement.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="Updraft : mondes, boss et classement" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [Conduire sur une carte de San Francisco](https://x.com/mindblown_ai/status/2106089461969019357) (par [@mindblown_ai](https://x.com/mindblown_ai))

**Utilisez un prototype de conduite urbaine pour explorer la navigation et les objectifs de jeu.**

La personne qui publie partage une vidéo et un lien jouable vers un jeu de conduite dans San Francisco attribué à quelqu’un d’autre, en citant Three.js. Le crédit désigne la source publiée, sans lui attribuer la création du jeu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="Conduire sur une carte de San Francisco" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [Rédiger des prompts pour une scène Seedance](https://x.com/Chengzilhy/status/2105850801663234374) (par [@Chengzilhy](https://x.com/Chengzilhy))

**Distinguez la rédaction des prompts de la génération vidéo dans un workflow d’action utilisant plusieurs outils.**

L’auteur partage une séquence de combat enrichie, attribuant les prompts à Fable et la vidéo à Seedance 2.5. Le modèle de langage sert ici à préparer les instructions destinées au générateur vidéo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="Rédiger des prompts pour une scène Seedance" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [Une vidéo explicative pour un collègue de bureau](https://x.com/ishuagra02/status/2106138602073641241) (par [@ishuagra02](https://x.com/ishuagra02))

**Expliquez une extension d’outil de programmation avec une courte vidéo de présentation.**

Le créateur présente clawdhouse, une modification de Claude Code, et attribue sa vidéo d’introduction à Fable. Le collègue mascotte et ses humeurs sont des fonctions de la modification présentée, pas une affirmation que Fable l’a développée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="Une vidéo explicative pour un collègue de bureau" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [Un court prompt pour une animation changeant de style](https://x.com/cherry_mx_reds/status/2105816670896009224) (par [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Testez une demande d’animation brève avant d’ajouter une spécification créative détaillée.**

L’auteur explique avoir demandé une animation sympathique et obtenu le résultat aux styles changeants environ quinze minutes plus tard. La demande initiale est directement citée dans le post source.

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="Un court prompt pour une animation changeant de style" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [Visualiser le problème à trois corps](https://x.com/zAdrielsan/status/2105822678519001360) (par [@zAdrielsan](https://x.com/zAdrielsan))

**Séparez simulation sur CPU et rendu sur GPU dans le brief d’une visualisation orbitale.**

L’auteur décrit environ mille lignes de Bend2 pour une scène à trois corps, avec une physique symplectique sur CPU et le calcul des pixels sur GPU. Il annonce aussi soixante images par seconde sur son M5 et des preuves formelles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="Visualiser le problème à trois corps" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [Une galerie d’animations aux styles artistiques variés](https://x.com/blueemi99/status/2105782154387189771) (par [@blueemi99](https://x.com/blueemi99))

**Comparez plusieurs styles artistiques dans une même galerie animée.**

L’auteur partage une galerie d’animations réalisée avec le réglage xhigh. Le résultat réunit plusieurs styles artistiques et permet de comparer les traitements visuels au sein d’une seule œuvre.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="Une galerie d’animations aux styles artistiques variés" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [Compagnons robots et fourrure procédurale](https://x.com/KanaWorks_AI/status/2106717014245183517) (par [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**Associez animation existante et retouches procédurales plutôt que de présenter tous les éléments comme nouvellement générés.**

L’auteur affine une animation existante de chien robot Unimate pour en faire un compagnon et crée un animal virtuel poilu avec brossage et traces. Unreal Engine et l’animation robotique existante restent des éléments explicites du workflow.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="Compagnons robots et fourrure procédurale" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [Un montage animé autour des mathématiques](https://x.com/TurboNexic/status/2106710792590835934) (par [@TurboNexic](https://x.com/TurboNexic))

**Utilisez des animations sur les mathématiques comme exemple de communication visuelle.**

La personne qui publie partage un montage animé sur les mathématiques. Le clip vertical utilise des images mathématiques comme éléments de design animé ; il présente une démonstration plutôt qu’un calcul mathématique détaillé.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="Un montage animé autour des mathématiques" width="760">

*Image archivée de la vidéo source.*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Une vidéo de paroles pour Your Woman](https://x.com/atomtanstudio/status/2106702854639743467) (par [@atomtanstudio](https://x.com/atomtanstudio))

**Construisez l’animation des paroles autour d’un enregistrement fourni et précisez le rôle de la musique.**

Le créateur partage une vidéo de paroles pour Your Woman de White Town. La chanson existante constitue l’entrée audio du traitement visuel, et non une musique présentée comme composée par le modèle.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Une vidéo de paroles pour Your Woman" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [Redessiner un clip musical en JavaScript](https://x.com/abhinavflac/status/2106638839666373114) (par [@abhinavflac](https://x.com/abhinavflac))

**Retracez les images d’une vidéo fournie avec des formes codées pour recréer un traitement de clip.**

L’auteur décrit le traçage d’images du clip Godzilla d’Eminem sous forme de formes plates, puis leur redessin en JavaScript. Les images et la musique originales sont des entrées de l’animation obtenue.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="Redessiner un clip musical en JavaScript" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [Une animation sur le football chinois](https://x.com/esrhengwu/status/2106625966965760380) (par [@esrhengwu](https://x.com/esrhengwu))

**Transformez un thème sportif en brief de récit animé.**

L’auteur partage une animation sur l’équipe nationale chinoise de football, en prenant son développement et sa résilience comme thème créatif. L’enregistrement offre un exemple concret de narration sportive.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="Une animation sur le football chinois" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [Présentation de retopologie d’une console portable](https://x.com/mickeysmith_jp/status/2106607349385630138) (par [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**Comparez le rendu d’une console portable à sa représentation filaire pour discuter de topologie.**

La personne qui publie associe une image de console portable à une vue de type filaire en parlant de retopologie. Cette comparaison illustre une présentation de modélisation, pas un maillage modifiable ni une procédure de retopologie documentée.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="Présentation de retopologie d’une console portable" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft rencontre Pokémon](https://x.com/MozeTech/status/2106590326634983710) (par [@MozeTech](https://x.com/MozeTech))

**Combinez les mécaniques de deux jeux familiers dans un brief de prototype.**

L’auteur montre un prototype de Bourg Palette mêlant construction et fabrication à la Minecraft avec capture à la Pokémon, et propose une démo. Le post décrit une expérience réalisée en une seule génération.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft rencontre Pokémon" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [Un film expliquant la fabrication d’un modèle de langage](https://x.com/imjustnewatai/status/2106546810793730419) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Transformez une question technique en demande d’explication visuelle.**

L’auteur demande comment un grand modèle de langage est fabriqué et partage la vidéo explicative obtenue. L’œuvre illustre concrètement la présentation d’un sujet technique sous forme de séquence animée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="Un film expliquant la fabrication d’un modèle de langage" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [Un montage de moments forts autour d’Altman](https://x.com/benchmark_lb900/status/2106539977404506303) (par [@benchmark_lb900](https://x.com/benchmark_lb900))

**Utilisez une personnalité publique comme thème pour tester le rythme d’un court montage animé.**

L’auteur partage une vidéo de moments forts autour d’Altman et la décrit comme le résultat d’une seule génération. L’enregistrement vertical constitue un exemple compact de montage animé.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="Un montage de moments forts autour d’Altman" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [Le premier des Trente-Six Stratagèmes](https://x.com/jesselaunz/status/2106538284197548122) (par [@jesselaunz](https://x.com/jesselaunz))

**Documentez les outils musicaux externes dans un workflow d’animation narrative.**

L’auteur partage un film sur le premier des Trente-Six Stratagèmes et rapporte une instruction unique. Suno V6 est cité pour la musique du film, ce qui préserve le rôle distinct de l’outil audio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="Le premier des Trente-Six Stratagèmes" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [Modélisation, rigging et animation de jeu](https://x.com/atomtanstudio/status/2106516974662713477) (par [@atomtanstudio](https://x.com/atomtanstudio))

**Évaluez ensemble création du personnage, rigging et animation dans une comparaison de scènes de jeu.**

L’auteur présente une comparaison de Depths of Despair montrant modélisation de personnage, rigging et animation. Le post décrit les éléments et outils employés et réunit les résultats visibles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="Modélisation, rigging et animation de jeu" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [Un film sans paroles sur la mortalité infantile](https://x.com/cocoloba_/status/2106512963414970458) (par [@cocoloba_](https://x.com/cocoloba_))

**Communiquez un sujet social difficile avec une séquence visuelle sans paroles.**

L’auteur partage un film sur la mortalité infantile utilisant un nourrisson qui respire et des lits assombris comme images narratives. Le cas conserve la tâche de narration visuelle sans reprendre les statistiques démographiques du film.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="Un film sans paroles sur la mortalité infantile" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [Une animation SVG de la glycolyse à l’éthanol](https://x.com/olddonkeyblog/status/2106508425211330750) (par [@olddonkeyblog](https://x.com/olddonkeyblog))

**Intégrez du SVG animé dans du HTML pour expliquer un processus moléculaire.**

L’auteur demande une molécule de glucose traversant la glycolyse et la formation d’éthanol, représentée en SVG animé dans du HTML. L’enregistrement montre la visualisation scientifique obtenue.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="Une animation SVG de la glycolyse à l’éthanol" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [Seize lancements simultanés de Starship](https://x.com/olddonkeyblog/status/2106507742454403485) (par [@olddonkeyblog](https://x.com/olddonkeyblog))

**Précisez les phases de lancement synchronisées dans le brief d’une animation HTML et SVG.**

L’auteur demande seize Starship décollant ensemble, suivis de la séparation des étages et de l’entrée dans l’espace. L’enregistrement présente la séquence d’animation multi-objets obtenue.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="Seize lancements simultanés de Starship" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [Un test animé du pélican à vélo](https://x.com/olddonkeyblog/status/2106507429265756165) (par [@olddonkeyblog](https://x.com/olddonkeyblog))

**Examinez une scène de pélican à vélo comme exercice de dessin en mouvement coordonné.**

L’auteur partage son essai du pélican à vélo avec le raisonnement Max. Il s’agit d’un résultat enregistré distinct des versions d’autres auteurs pour la même demande générale.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="Un test animé du pélican à vélo" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [Une histoire des 150 prochaines années](https://x.com/imjustnewatai/status/2106489784382197771) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Associez scénario, images codées et musique dans un brief de récit futuriste spéculatif.**

L’auteur rapporte qu’une seule instruction a produit un film sur les cent cinquante prochaines années de l’humanité. L’œuvre associe récit écrit, animation codée et musique pour représenter des vies futures possibles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="Une histoire des 150 prochaines années" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [Une expérience indépendante de Humanity Walks](https://x.com/iowitz/status/2106489119186538583) (par [@iowitz](https://x.com/iowitz))

**Reprenez une idée d’animation sur l’histoire de l’art pour mener votre propre expérience créative.**

Après avoir vu d’autres démonstrations, l’auteur tente sa propre animation de marche à travers l’histoire de l’art et partage le résultat. Le clip reste une génération distincte, sans être fusionné pour sa seule proximité thématique.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="Une expérience indépendante de Humanity Walks" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [Le film codé The Grader](https://x.com/argofowl/status/2106476549046513947) (par [@argofowl](https://x.com/argofowl))

**Documentez la génération externe de voix ou de son dans la présentation d’un film codé.**

L’auteur partage The Grader comme un film codé et cite ElevenLabs v4 pour l’audio. Le post rapporte une seule génération d’environ deux heures et vingt-deux minutes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="Le film codé The Grader" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [Le court métrage d’horreur Reawakening](https://x.com/JaydenDavisNC/status/2106440774367822008) (par [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**Orientez un court film animé avec une prémisse d’horreur clairement nommée.**

L’auteur partage Reawakening, un court métrage d’horreur réalisé avec l’IA. L’œuvre jointe fournit un exemple concret de récit et d’atmosphère pour un brief d’animation horrifique.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="Le court métrage d’horreur Reawakening" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [Une vidéo de 25 secondes sur l’amélioration de soi](https://x.com/DAssetBuzz/status/2106505100575592838) (par [@DAssetBuzz](https://x.com/DAssetBuzz))

**Transformez une idée abstraite d’amélioration en un bref créatif pour un court film.**

L’auteur demande une vidéo de vingt-cinq secondes sur ce qui pourrait améliorer le modèle et partage le résultat. La prémisse sert une narration créative plutôt qu’une affirmation sur les capacités du produit.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="Une vidéo de 25 secondes sur l’amélioration de soi" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [Une scène de château avec retour sur le coût](https://x.com/nemumusitocha/status/2106429338556207284) (par [@nemumusitocha](https://x.com/nemumusitocha))

**Évaluez une scène 3D en considérant ses détails et l’expérience d’utilisation rapportée par l’auteur.**

L’auteur partage un château détaillé, loue sa réalisation visuelle et juge le coût d’utilisation peu intéressant. Le cas associe une scène concrète à son appréciation du rapport entre coût et satisfaction.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="Une scène de château avec retour sur le coût" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [Une publicité de lancement de marque en 40 secondes](https://x.com/0xashtonx/status/2106421702783914423) (par [@0xashtonx](https://x.com/0xashtonx))

**Prenez votre propre marque comme sujet d’un bref publicitaire de lancement concis.**

Le créateur demande une publicité de lancement de quarante secondes pour sa propre marque et partage la vidéo obtenue. La tâche illustre concrètement la génération d’un récit promotionnel de marque.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="Une publicité de lancement de marque en 40 secondes" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [Une reprise de Rocketball](https://x.com/atomtanstudio/status/2106418747083022555) (par [@atomtanstudio](https://x.com/atomtanstudio))

**Associez éléments codés et mécaniques interactives dans la reprise d’un jeu familier.**

L’auteur partage Rocketball, une reprise du jeu C-64 des années 1980, et indique que ses éléments sont codés. Le remplacement d’une version sur site web est présenté comme un projet futur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="Une reprise de Rocketball" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [Une comparaison de pagodes en voxels](https://x.com/dropout_layer/status/2106408147309252915) (par [@dropout_layer](https://x.com/dropout_layer))

**Comparez deux générations de la même scène avec leurs coûts déclarés respectifs.**

L’auteur présente des résultats Astra et Fable pour une pagode 3D en voxels, en annonçant des coûts de 3,50 et 5,50 dollars respectivement. La comparaison porte sur ces essais précis et leurs scènes affichées.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="Une comparaison de pagodes en voxels" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [Présentation d’une Switch 3 imaginaire](https://x.com/mathisbuilds/status/2106407842240418097) (par [@mathisbuilds](https://x.com/mathisbuilds))

**Utilisez un produit imaginaire comme exercice de présentation de concept et de démonstration.**

L’auteur demande une Nintendo Switch 3 imaginaire et une démo, en rapportant environ quatre heures de travail. L’enregistrement présente un concept fictif de prochaine console plutôt que de véritables spécifications produit.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="Présentation d’une Switch 3 imaginaire" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [Des pages d’accueil avant et après](https://x.com/nemumusitocha/status/2106402952307200302) (par [@nemumusitocha](https://x.com/nemumusitocha))

**Relancez le même prompt de page d’accueil pour comparer les résultats au fil du temps.**

L’auteur compare une page d’accueil nouvellement générée à une page antérieure produite avec le même prompt. Les designs avant et après fournissent un exemple pratique de comparaison d’interfaces.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="Des pages d’accueil avant et après" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [La perspective intérieure imaginée d’une IA](https://x.com/blueemi99/status/2106397329653719115) (par [@blueemi99](https://x.com/blueemi99))

**Utilisez une perspective intérieure imaginaire comme prémisse d’une animation créative.**

L’auteur demande un film sur ce que pourrait ressentir un modèle d’IA et partage un résultat obtenu en une seule génération. La prémisse est présentée comme une expression visuelle imaginative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="La perspective intérieure imaginée d’une IA" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Motion design des paroles de Go](https://x.com/atomtanstudio/status/2106377491267137848) (par [@atomtanstudio](https://x.com/atomtanstudio))

**Animez des paroles fournies autour d’un enregistrement musical existant.**

Le créateur partage une vidéo de paroles pour Go de The Chemical Brothers et dit avoir utilisé le raisonnement Max. L’enregistrement de la chanson reste l’entrée audio externe du travail de motion design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Motion design des paroles de Go" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [Un second portfolio animé de 15 secondes](https://x.com/Saccc_c/status/2106376222309761094) (par [@Saccc_c](https://x.com/Saccc_c))

**Explorez une nouvelle direction visuelle avec un brief libre de portfolio en motion design.**

L’auteur partage un nouveau portfolio animé de quinze secondes et fournit le prompt créatif. Son récit distingue explicitement cette génération d’un travail de portfolio antérieur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="Un second portfolio animé de 15 secondes" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [Une revue guidée de l’implémentation d’un agent](https://x.com/RobIW_dev/status/2106371025852108940) (par [@RobIW_dev](https://x.com/RobIW_dev))

**Vérifiez l’adéquation des plans au système avant de passer de l’idéation à l’exécution.**

L’auteur partage des consignes sur l’adéquation au système, la planification de l’implémentation et les explications. Il décrit comment il examine le travail réalisé ou choisit la prochaine implémentation ; l’image conserve cet artefact de planification concret.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="Une revue guidée de l’implémentation d’un agent" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [La danse de la mascotte Claude](https://x.com/ishuagra02/status/2106369929813594134) (par [@ishuagra02](https://x.com/ishuagra02))

**Testez le lien entre mouvement et musique avec une animation de mascotte calée sur le rythme.**

Le créateur partage une danse de la mascotte Claude et décrit une animation qui suit le rythme. Les republications de la même vidéo native sont rattachées à cette source au lieu d’être comptées de nouveau.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="La danse de la mascotte Claude" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [Les îles interactives des Sept Merveilles](https://x.com/notjazii/status/2106368606502334922) (par [@notjazii](https://x.com/notjazii))

**Utilisez des monuments comme destinations dans une scène insulaire interactive.**

La personne qui publie partage une scène des Sept Merveilles organisée en îles 3D avec des bâtiments emblématiques. L’enregistrement illustre concrètement l’utilisation de monuments reconnaissables pour structurer un environnement visuel interactif.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="Les îles interactives des Sept Merveilles" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [Un clip musical pour Propellerheads](https://x.com/atomtanstudio/status/2106353569603736009) (par [@atomtanstudio](https://x.com/atomtanstudio))

**Appuyez des animations graphiques prolongées sur une bande-son fournie.**

Le créateur partage un traitement vidéo de On Her Majesty’s Secret Service de Propellerheads. L’enregistrement existant constitue l’entrée audio de la séquence visuelle animée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="Un clip musical pour Propellerheads" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Comparaison d’animations Steamboat Willie](https://x.com/mathisbuilds/status/2106351978691305732) (par [@mathisbuilds](https://x.com/mathisbuilds))

**Comparez deux traitements animés de la même courte scène avec le son activé.**

L’auteur partage une comparaison Steamboat Willie étiquetée Fable et Opus avec un effort xhigh, et décrit les résultats comme obtenus en une seule génération. Le clip présente cette comparaison précise de l’image et du son.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Comparaison d’animations Steamboat Willie" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [Un film inspiré de Sanxingdui](https://x.com/hungryturbo/status/2106339115642019904) (par [@hungryturbo](https://x.com/hungryturbo))

**Organisez un court métrage animé autour d’un thème culturel et historique.**

L’auteur présente un film consacré à Sanxingdui comme une œuvre de narration visuelle créative. L’enregistrement montre concrètement comment transformer un sujet culturel et historique en brief d’animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="Un film inspiré de Sanxingdui" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Une Bugatti Chiron avant et après](https://x.com/alannnfx/status/2106323394350461031) (par [@alannnfx](https://x.com/alannnfx))

**Relancez un ancien prompt automobile pour comparer la modélisation et les détails fonctionnels.**

Le même auteur montre des résultats de Bugatti Chiron issus d’une première génération puis d’une nouvelle exécution du prompt. La comparaison enregistrée porte sur une modélisation et des éléments de scène plus riches.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Une Bugatti Chiron avant et après" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [Le film conceptuel GRAIN](https://x.com/NFT_Chen/status/2106301427052360150) (par [@NFT_Chen](https://x.com/NFT_Chen))

**Construisez un film conceptuel abstrait autour de motifs visuels récurrents.**

Le créateur partage GRAIN, un court métrage conceptuel reliant une graine, un grain, un arbre et des images de montagne. Les formes et transitions récurrentes constituent la structure narrative de la séquence.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="Le film conceptuel GRAIN" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [La galerie artistique Human in Transit](https://x.com/exploraX_/status/2106296439936614646) (par [@exploraX_](https://x.com/exploraX_))

**Présentez un voyage visuel historique dans une galerie au style interactif.**

La personne qui publie partage Human in Transit, une galerie allant des styles artistiques antiques aux styles modernes. L’interface enregistrée donne un exemple concret d’organisation de plusieurs périodes visuelles dans une présentation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="La galerie artistique Human in Transit" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [Un court film visuel sur la Route de la soie](https://x.com/hungryturbo/status/2106294812261695508) (par [@hungryturbo](https://x.com/hungryturbo))

**Transformez un thème de voyage historique en un court film visuel cohérent.**

L’auteur partage un film sur la Route de la soie. L’œuvre jointe offre une approche créative concrète d’un voyage historique raconté par des images animées.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="Un court film visuel sur la Route de la soie" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [Une présentation sur quatre transformations](https://x.com/dpkostka/status/2106272731364794757) (par [@dpkostka](https://x.com/dpkostka))

**Utilisez un cadre de transformation pour organiser une présentation.**

L’auteur partage des diapositives décrivant quatre voies de transformation. L’image jointe montre comment disposer un cadre conceptuel dans un document visuel.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="Une présentation sur quatre transformations" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [Comparer le ton d’anciens échanges](https://x.com/kiyoshi_shin/status/2106268573186637883) (par [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**Comparez d’anciens journaux de conversation aux réponses actuelles pour étudier les changements de ton.**

L’auteur demande au modèle actuel d’analyser d’anciens échanges et son style présent, puis exprime son insatisfaction face au changement de ton. L’image jointe documente cette tâche de comparaison conversationnelle.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="Comparer le ton d’anciens échanges" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [Un test de mignonnerie avec un kakapo](https://x.com/hanawo_neki/status/2106257409782288659) (par [@hanawo_neki](https://x.com/hanawo_neki))

**Comparez des styles d’animation à partir d’une tâche précise de préférence de personnage.**

L’auteur partage une animation de kakapo et indique préférer Opus dans cette comparaison centrée sur la mignonnerie. Le cas conserve le retour esthétique négatif avec l’animation réellement publiée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="Un test de mignonnerie avec un kakapo" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [Spider-Man à travers dix époques de comics](https://x.com/chetaslua/status/2106248621519978867) (par [@chetaslua](https://x.com/chetaslua))

**Maintenez un personnage reconnaissable lorsqu’il traverse plusieurs époques de bande dessinée.**

L’auteur de la publication originale montre Spider-Man à travers dix époques de comics. Les autres posts réutilisant la même vidéo sont rattachés à cette source plutôt que comptés comme des œuvres supplémentaires.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="Spider-Man à travers dix époques de comics" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [Une fiction horrifique sur les Illuminati](https://x.com/badboyfoxy/status/2106241189976387799) (par [@badboyfoxy](https://x.com/badboyfoxy))

**Traitez un brief d’horreur conspirationniste comme un exercice de fiction.**

L’auteur demande une vidéo effrayante sur les Illuminati et partage le résultat. Le sujet constitue une prémisse de fiction horrifique pour l’animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="Une fiction horrifique sur les Illuminati" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [Un film codé sur l’histoire de la science nucléaire](https://x.com/imjustnewatai/status/2106238699872956427) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Associez un moteur de rendu codé sur mesure et une musique à un film explicatif d’histoire scientifique.**

L’auteur demande un film 3D de trois minutes sur la science nucléaire qui a rendu la bombe atomique possible, puis mentionne des images dessinées, un moteur sur mesure et une musique synthétisée. Le cas porte sur le workflow audiovisuel.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="Un film codé sur l’histoire de la science nucléaire" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [Un film expliquant le revenu universel élevé](https://x.com/markbraincell/status/2106234118514323515) (par [@markbraincell](https://x.com/markbraincell))

**Expliquez un concept économique à l’aide d’une animation.**

La personne qui publie partage une animation expliquant le revenu universel élevé. L’enregistrement constitue un exemple concret d’explication conceptuelle, sans transformer l’argument économique exposé en résultat mesuré.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="Un film expliquant le revenu universel élevé" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [Une explication animée du conflit Altman–Amodei](https://x.com/imjustnewatai/status/2106204392588276065) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Utilisez un différend comme structure narrative d’un film explicatif animé.**

L’auteur demande un récit animé du conflit Altman–Amodei et partage la vidéo obtenue. La tâche illustre un format explicatif d’actualité plutôt qu’un récit historique fondé sur une enquête indépendante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="Une explication animée du conflit Altman–Amodei" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [Un clip musical avec la mascotte Claude](https://x.com/synthshareai/status/2106195060140446028) (par [@synthshareai](https://x.com/synthshareai))

**Associez une mascotte en surimpression à des images fournies pour un montage musical centré sur un personnage.**

La personne qui publie montre une mascotte Claude sur des images de clip musical en prises de vues réelles et rapporte une exécution de douze heures. Le traitement visible associe une surimpression dessinée à des images fournies.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="Un clip musical avec la mascotte Claude" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [Un zoom continu des quarks à l’univers](https://x.com/imjustnewatai/status/2106190594775097663) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Reliez des échelles scientifiques dans une même histoire audiovisuelle grâce à un zoom continu.**

L’auteur mentionne des images codées et une musique synthétisée pour un zoom allant des quarks à l’univers. L’enregistrement illustre des transitions d’échelle continues et un récit visuel cohérent.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="Un zoom continu des quarks à l’univers" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [Imaginer le monde en 2076](https://x.com/Layton_Gott/status/2106190496075035096) (par [@Layton_Gott](https://x.com/Layton_Gott))

**Demandez une scène du monde futur avec une durée narrative précise.**

L’auteur partage un court film imaginant le monde en 2076 après avoir demandé une vidéo de vingt-cinq secondes. La réutilisation du même enregistrement par d’autres comptes est rattachée à cette source.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="Imaginer le monde en 2076" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [Une chronologie des bâtiments de Lower Manhattan](https://x.com/nroze22/status/2106183281293381661) (par [@nroze22](https://x.com/nroze22))

**Réunissez emprises, dates de construction et hauteurs dans une interface chronologique architecturale.**

L’auteur présente Lower Manhattan dans une interface au style de dessin architectural, montrant dates, emprises et hauteurs des bâtiments. L’enregistrement offre un concept concret de chronologie interactive.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="Une chronologie des bâtiments de Lower Manhattan" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [Une animation sur l’écriture ossécaille](https://x.com/MinLiBuilds/status/2106180691344118202) (par [@MinLiBuilds](https://x.com/MinLiBuilds))

**Faites de l’évolution de l’écriture le sujet d’un voyage historique animé.**

L’auteur partage une animation qui commence avec l’écriture ossécaille. L’enregistrement constitue un exemple concret de narration visuelle autour de l’histoire des caractères écrits.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="Une animation sur l’écriture ossécaille" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [Une autre traversée de l’histoire de l’art](https://x.com/imjustnewatai/status/2106162924331180510) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Utilisez des personnages familiers comme guides continus dans un décor historique changeant.**

L’auteur demande Iron Man et Spider-Man volant à travers l’histoire et partage l’animation obtenue. Il s’agit d’une œuvre distincte des expériences d’autres auteurs associant personnages et histoire de l’art.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="Une autre traversée de l’histoire de l’art" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [Une œuvre audiovisuelle codée autour de Seikilos](https://x.com/YanqingCheng/status/2106158746938269728) (par [@YanqingCheng](https://x.com/YanqingCheng))

**Construisez une œuvre audiovisuelle en un seul fichier autour d’un texte musical historique.**

L’auteur partage une œuvre consacrée à l’épitaphe de Seikilos, décrivant des images et une musique synthétisées avec HTML et JavaScript dans un fichier unique. Le texte historique organise la séquence audiovisuelle codée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="Une œuvre audiovisuelle codée autour de Seikilos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [Comparaison d’animations de jet](https://x.com/Kinzf2121/status/2106158536963330346) (par [@Kinzf2121](https://x.com/Kinzf2121))

**Comparez le vol et le suivi de caméra pour une même tâche d’animation aérienne.**

L’auteur montre une comparaison d’animation de jet entre un résultat étiqueté Fable 5.1 et Opus. Les scènes offrent un exemple précis pour comparer le mouvement de l’avion et le suivi cinématographique.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="Comparaison d’animations de jet" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [Un film de présentation du modèle](https://x.com/devteamdrew/status/2106155815707021549) (par [@devteamdrew](https://x.com/devteamdrew))

**Explorez une animation sur le modèle à partir d’un brief de présentation personnelle.**

Le créateur raconte avoir demandé une vidéo de présentation en un seul prompt et partage le film obtenu. La tâche associe une narration sur le modèle à une présentation animée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="Un film de présentation du modèle" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [Un prototype de jeu de cartes postapocalyptique](https://x.com/maciejkrupowies/status/2106153578029338850) (par [@maciejkrupowies](https://x.com/maciejkrupowies))

**Prototypez un thème de jeu de cartes et examinez l’interface de combat obtenue.**

L’auteur montre un prototype postapocalyptique de type Hearthstone, décrit comme réalisé en une seule génération. Le post reconnaît de petits défauts tout en présentant l’interface et les interactions du jeu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="Un prototype de jeu de cartes postapocalyptique" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [L’animation de bureau The Late Byte](https://x.com/rohit3a/status/2106138910648914094) (par [@rohit3a](https://x.com/rohit3a))

**Faites des personnalités des modèles les personnages d’une conversation animée au bureau.**

Le créateur présente The Late Byte, une histoire animée de bureau où Opus incarne un patron en colère. Ce récit est distinct du film Day in the Life of Claude.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="L’animation de bureau The Late Byte" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Animation des paroles de Queens of the Stone Age](https://x.com/atomtanstudio/status/2106135196483608745) (par [@atomtanstudio](https://x.com/atomtanstudio))

**Associez une chanson fournie à de la typographie cinétique et du motion design.**

Le créateur décrit un clip en typographie cinétique autour d’un enregistrement de Queens of the Stone Age. La chanson est une entrée audio fournie ; l’exemple porte sur l’agencement de ses paroles et des images.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Animation des paroles de Queens of the Stone Age" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [Une scène narrative Three.js partagée](https://x.com/Noreply134882/status/2106116572389478746) (par [@Noreply134882](https://x.com/Noreply134882))

**Utilisez une histoire 3D partagée comme référence de conception narrative.**

La personne qui publie partage une scène narrative Three.js et commente une forte consommation de tokens. Le clip est conservé comme exemple visuel partagé de narration en 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="Une scène narrative Three.js partagée" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [Un moonwalk à travers des scènes historiques](https://x.com/noclipepe/status/2106105810812112937) (par [@noclipepe](https://x.com/noclipepe))

**Faites traverser différents décors et styles historiques à un même motif de danse.**

La personne qui publie partage un moonwalk de Michael Jackson allant des dinosaures à la Lune. Le film est conservé comme exemple partagé de danse et de galerie de styles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="Un moonwalk à travers des scènes historiques" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [Des animations graphiques guidées par un prompt détaillé](https://x.com/devswha/status/2106100273509007802) (par [@devswha](https://x.com/devswha))

**Comparez un brief créatif détaillé à une demande de motion design plus courte.**

L’auteur partage une animation graphique et indique n’avoir fourni qu’un prompt détaillé, sans éléments, vidéo de référence ni fichiers sources. Le résultat offre une référence concrète de motion design piloté par prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="Des animations graphiques guidées par un prompt détaillé" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [L’interface d’un site de location](https://x.com/oalanicolas/status/2106098902965309475) (par [@oalanicolas](https://x.com/oalanicolas))

**Explorez une interface web concrète à partir d’un brief d’activité de location.**

Le créateur partage une capture d’une interface de site pour une entreprise de location. L’exemple porte sur le design visible de la page et la présentation de l’activité.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="L’interface d’un site de location" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [Un film créatif sur l’AGI](https://x.com/AndrewOnXYZ/status/2106097745098395712) (par [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**Comparez les traitements narratifs et visuels avec un prompt créatif récurrent.**

L’auteur partage une animation sur l’AGI produite à partir d’un prompt récurrent. Les déclarations du modèle font partie de la narration créative du film.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="Un film créatif sur l’AGI" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [L’histoire de l’art avec une intrigue de chat](https://x.com/cherry_mx_reds/status/2106095190285144331) (par [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Condensez plusieurs périodes artistiques en un court récit avec un personnage récurrent.**

Le créateur présente un parcours de quinze secondes dans l’histoire de l’art avec une intrigue secondaire de chat. Les quinze secondes désignent la durée du film, tandis que la tâche couvre de nombreux styles historiques.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="L’histoire de l’art avec une intrigue de chat" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [Un prototype de combat et une scène en voxels](https://x.com/OnlyTerp/status/2106089280502210626) (par [@OnlyTerp](https://x.com/OnlyTerp))

**Examinez combat et construction d’univers dans les résultats d’une tâche de code créatif.**

L’auteur partage un prototype de combat de type DMC et une scène en voxels, en décrivant une longue génération. Le post fournit deux résultats concrets pour examiner mécaniques de jeu et univers visuel.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="Un prototype de combat et une scène en voxels" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [Une chronologie des mèmes d’Internet](https://x.com/chetaslua/status/2106076940558082297) (par [@chetaslua](https://x.com/chetaslua))

**Organisez une chronologie animée autour des styles et musiques propres à chaque année.**

Le créateur partage une séquence de mèmes viraux allant de 2010 à 2026. Chaque année reçoit un traitement visuel et musical dans cette narration codée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="Une chronologie des mèmes d’Internet" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [Des particules animées à partir d’une ligne](https://x.com/devswha/status/2106072107365114186) (par [@devswha](https://x.com/devswha))

**Commencez par une ligne de brief avant d’affiner un prompt de mouvement détaillé.**

Le créateur partage une animation de particules issue d’un prompt d’une ligne et prévoit d’essayer une demande plus détaillée. Il s’agit d’une génération distincte de son exemple de motion design plus long.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="Des particules animées à partir d’une ligne" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [L’animation Kung-Fu Boy](https://x.com/HashmathRzz/status/2106065773336965510) (par [@HashmathRzz](https://x.com/HashmathRzz))

**Explorez le mouvement animé avec un brief de personnage d’arts martiaux.**

L’auteur partage Kung-Fu Boy, une animation de personnage attribuée à Fable 5.5. L’enregistrement fournit le résultat concret pour ce thème d’arts martiaux.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="L’animation Kung-Fu Boy" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [Un débat animé sur le détroit d’Ormuz](https://x.com/chetaslua/status/2106060047805792415) (par [@chetaslua](https://x.com/chetaslua))

**Transformez un sujet de débat en récit animé.**

Le créateur présente un débat animé sur le détroit d’Ormuz. Ce cas retient le film visible plutôt que les autres usages sans illustration mentionnés autour du post.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="Un débat animé sur le détroit d’Ormuz" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [Un essai de style SVG avec une licorne](https://x.com/atomtanstudio/status/2106057876053918127) (par [@atomtanstudio](https://x.com/atomtanstudio))

**Examinez les choix de style SVG sur une même tâche de dessin thématique.**

L’auteur partage un essai de licorne en SVG inspiré du test d’un autre créateur. L’image jointe fournit le résultat concret pour comparer le traitement visuel d’un même sujet.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="Un essai de style SVG avec une licorne" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [Une animation saisonnière d’Halloween](https://x.com/cherry_mx_reds/status/2106056643255447590) (par [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Donnez à un modèle de code un thème saisonnier pour une courte animation créative.**

Le créateur demande une œuvre sur Halloween et partage l’animation saisonnière obtenue. Le post fournit l’enregistrement original de cette tâche créative précise.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="Une animation saisonnière d’Halloween" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Un barbare et une couverture avec Blender CLI](https://x.com/BoDy051/status/2106047375320166885) (par [@BoDy051](https://x.com/BoDy051))

**Explorez la modélisation d’un personnage et son rendu de couverture avec Blender CLI.**

L’auteur compare un barbare de RPG et un concept de couverture à un résultat Opus. Blender CLI sert à construire et rendre la scène ; le modèle fournit les instructions de code.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Un barbare et une couverture avec Blender CLI" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Une journée dans la vie de Claude](https://x.com/ishuagra02/status/2106045364868419727) (par [@ishuagra02](https://x.com/ishuagra02))

**Construisez une histoire animée du quotidien autour d’une mascotte récurrente.**

L’auteur du post original partage Day in the Life of Claude avec la mascotte. La vidéo source est distincte de l’animation de danse et de ses republications.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Une journée dans la vie de Claude" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [L’histoire de l’humanité en 3D](https://x.com/blueemi99/status/2106041578204655748) (par [@blueemi99](https://x.com/blueemi99))

**Associez scènes codées et animation dans une séquence historique visuelle.**

Le créateur partage une vidéo 3D allant des premiers humains à aujourd’hui et dit avoir généré modèles et animations par code. Le résultat est un exemple de narration visuelle.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="L’histoire de l’humanité en 3D" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [Un montage rapide de motion design](https://x.com/blueemi99/status/2106031355922387163) (par [@blueemi99](https://x.com/blueemi99))

**Évaluez rythme, son et cohérence dans un court montage de motion design.**

L’auteur partage une courte vidéo rapide et compare son son et sa cohérence à son résultat Opus. Le jugement décrit son expérience avec cette œuvre particulière.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="Un montage rapide de motion design" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [Une création 3D complexe et libre](https://x.com/cocoloba_/status/2106029181607772413) (par [@cocoloba_](https://x.com/cocoloba_))

**Explorez une composition 3D complexe à partir d’une demande créative ouverte.**

Le créateur demande ce que le modèle ferait de son temps libre et partage l’œuvre 3D obtenue. Le post évoque de nombreuses pièces distinctes dans cette composition générée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="Une création 3D complexe et libre" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [Un combat animé de bonshommes allumettes](https://x.com/HelaliBillel/status/2106028502763900944) (par [@HelaliBillel](https://x.com/HelaliBillel))

**Examinez rythme et mouvement avec une demande précise d’animation de combat.**

Le créateur demande une scène de combat animée entre bonshommes allumettes et partage le résultat. L’enregistrement fournit un exemple concret de cette tâche d’animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="Un combat animé de bonshommes allumettes" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [Une séquence d’interface animée en un prompt](https://x.com/iancarscadden/status/2106018048792789360) (par [@iancarscadden](https://x.com/iancarscadden))

**Explorez une séquence d’interface avec un seul brief d’animation.**

L’auteur partage une séquence d’interface animée décrite comme obtenue en une seule génération d’environ six ou sept minutes. L’enregistrement montre le résultat visuel de cette demande.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="Une séquence d’interface animée en un prompt" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [Une animation fictive sur SCP-8517](https://x.com/eviljoker88/status/2106003621402005816) (par [@eviljoker88](https://x.com/eviljoker88))

**Utilisez une prémisse inspirée de SCP comme brief de récit animé.**

Le créateur présente une animation sur SCP-8517 et l’attribue à Fable 5.5. Le cas porte sur le récit fictif et son animation visible.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="Une animation fictive sur SCP-8517" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [Une animation d’automne à l’aquarelle](https://x.com/ishuagra02/status/2106000055706784118) (par [@ishuagra02](https://x.com/ishuagra02))

**Précisez un sujet saisonnier et un traitement à l’aquarelle pour une animation.**

L’auteur partage une animation automnale à l’aquarelle. L’œuvre enregistrée montre concrètement l’association d’un sujet saisonnier à un médium visuel particulier.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="Une animation d’automne à l’aquarelle" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [Une scène de poupée procédurale](https://x.com/HelaliBillel/status/2105988689088196785) (par [@HelaliBillel](https://x.com/HelaliBillel))

**Examinez l’animation d’un personnage de poupée dans une scène mise en espace.**

L’auteur partage une animation procédurale de poupée sur scène et mentionne Blender dans la discussion. Le cas concerne le personnage visible, sa mise en scène et son animation.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="Une scène de poupée procédurale" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [Un pélican à vélo rendu dans le navigateur](https://x.com/slimcat0101/status/2105988654636380444) (par [@slimcat0101](https://x.com/slimcat0101))

**Exécutez le mouvement d’un personnage dans le navigateur et examinez la scène rendue.**

Le créateur demande un pélican à vélo et enregistre le HTML obtenu dans un navigateur. Cette scène animée se distingue des tests de dessin SVG statique.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="Un pélican à vélo rendu dans le navigateur" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [L’univers se regarde lui-même](https://x.com/l_mejiaC/status/2105988529671360673) (par [@l_mejiaC](https://x.com/l_mejiaC))

**Reliez des échelles éloignées par un voyage visuel continu dans un même récit.**

Le créateur présente une séquence continue du Big Bang à un œil humain. Il décrit les images et la musique du film comme produites par du code à l’exécution.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="L’univers se regarde lui-même" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [Un essai indépendant d’animation de jet](https://x.com/AI_Screening/status/2105988448612135176) (par [@AI_Screening](https://x.com/AI_Screening))

**Répétez une tâche d’animation aérienne et examinez le résultat précis.**

Après avoir vu les discussions sur le routage, l’auteur essaie une animation de jet et partage son résultat. L’enregistrement constitue une source indépendante pour cet exemple d’avion.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="Un essai indépendant d’animation de jet" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [Un premier montage animé libre](https://x.com/Saccc_c/status/2105985484472377531) (par [@Saccc_c](https://x.com/Saccc_c))

**Explorez le motion design avec un court prompt ouvert.**

Le créateur partage un premier montage de motion design décrit comme généré à partir d’un seul prompt. Ce résultat antérieur est distinct de son portfolio ultérieur de quinze secondes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="Un premier montage animé libre" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [Une civilisation rendue par code](https://x.com/ziwenxu_/status/2105983571848741045) (par [@ziwenxu_](https://x.com/ziwenxu_))

**Transformez un brief sur l’histoire de la civilisation en récit animé codé.**

L’auteur demande la civilisation de ses débuts à aujourd’hui et partage le film obtenu. Selon lui, ce traitement visuel codé n’utilise ni images filmées ni éléments de stock.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="Une civilisation rendue par code" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [Comparaison d’un zoom de la puce au serveur](https://x.com/SPAC89/status/2105968361725202591) (par [@SPAC89](https://x.com/SPAC89))

**Comparez réalisme et continuité d’un zoom allant d’une puce à un serveur.**

L’auteur compare Fable XHigh et GPT Sol Ultra sur un zoom réaliste, en discutant vitesse et consommation de quota. Le post concerne des essais précis sur des abonnements différents.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="Comparaison d’un zoom de la puce au serveur" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [Un projet personnel d’animation de voyage lunaire](https://x.com/IgorGomezC/status/2105963552024506565) (par [@IgorGomezC](https://x.com/IgorGomezC))

**Explorez un concept d’animation personnel avec plusieurs modèles de code.**

Le créateur partage un projet de voyage lunaire animé en évoquant ses essais avec Fable et Opus. L’œuvre jointe est le résultat concret de cette exploration créative.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="Un projet personnel d’animation de voyage lunaire" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [Comparaison de scènes japonaises en voxels](https://x.com/vikktorrrre/status/2105955048018588084) (par [@vikktorrrre](https://x.com/vikktorrrre))

**Comparez détails, brouillard et clarté visuelle avec le même prompt de scène.**

L’auteur compare les résultats actuels de Fable et Opus avec un même prompt de scène japonaise en voxels. Les observations portent sur la clarté, le brouillard et l’esthétique de ces résultats précis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="Comparaison de scènes japonaises en voxels" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [Le court audiovisuel Steaming the Frontier](https://x.com/sdmat123/status/2105929299878703520) (par [@sdmat123](https://x.com/sdmat123))

**Associez une esthétique de type Steamboat et du son dans un court audiovisuel.**

Le créateur partage Steaming the Frontier, une animation sonore. Cette source reste distincte des créations indépendantes de style Steamboat d’autres auteurs.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="Le court audiovisuel Steaming the Frontier" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [Superman dans plusieurs styles artistiques](https://x.com/Mr_Salio/status/2105925979466052051) (par [@Mr_Salio](https://x.com/Mr_Salio))

**Faites traverser plusieurs styles à un même personnage dans une animation continue.**

Le créateur dit qu’un ancien exemple de Superman lui a inspiré une nouvelle génération et partage son propre résultat. Les dessins différents en font une création distincte plutôt qu’une republication.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="Superman dans plusieurs styles artistiques" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Un prototype de combat de boss de type Cupcake](https://x.com/maciejkrupowies/status/2105914965387321785) (par [@maciejkrupowies](https://x.com/maciejkrupowies))

**Prototypez un combat de boss à défilement horizontal et examinez l’action obtenue.**

L’auteur partage un prototype de combat de boss de type Cupcake et rapporte une seule génération en moins de dix minutes. L’enregistrement montre la séquence de combat du jeu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Un prototype de combat de boss de type Cupcake" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [Un voilier sous un soleil changeant](https://x.com/popat_kunj/status/2105907935490752822) (par [@popat_kunj](https://x.com/popat_kunj))

**Explorez ciel, eau et position du soleil dans une scène de navigation.**

Le créateur partage une scène de voilier en 3D sous différentes positions du soleil et lie un artefact interactif. La scène réunit bateau, ciel et eau dans une même tâche visuelle.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="Un voilier sous un soleil changeant" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Une vidéo des nouveautés de Paracortex et Pi](https://x.com/RobIW_dev/status/2105894547796476225) (par [@RobIW_dev](https://x.com/RobIW_dev))

**Transformez les mises à jour produit en courte annonce animée.**

L’auteur convertit les nouveautés de Paracortex et Pi en vidéo de motion design de vingt-cinq secondes et fournit un prompt. L’œuvre illustre la communication produit visuelle.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Une vidéo des nouveautés de Paracortex et Pi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Une promotion du site Curio 2.0](https://x.com/voltwake/status/2105884775982485642) (par [@voltwake](https://x.com/voltwake))

**Créez un film promotionnel codé pour le lancement d’un site existant.**

Le créateur décrit une promotion de lancement pour Curio 2.0 associant images codées, caméra et musique. Le post partage le film promotionnel obtenu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Une promotion du site Curio 2.0" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [Une histoire 3D imaginaire de Hugging Face](https://x.com/chetaslua/status/2105884276864782557) (par [@chetaslua](https://x.com/chetaslua))

**Associez code du modèle, rendu et outils audio pour un film fictif.**

Le créateur partage une histoire imaginaire de Hugging Face réalisée avec du code du modèle, Blender et l’API ElevenLabs. Blender assure construction et rendu, et ElevenLabs fournit l’audio externe.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="Une histoire 3D imaginaire de Hugging Face" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [Claude pour Chrome dans JS Paint](https://x.com/BtwIUseSystemd/status/2105861662112923849) (par [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**Donnez à un agent navigateur une tâche de dessin limitée aux outils de l’application.**

L’auteur demande à Claude pour Chrome de dessiner une personne uniquement avec les outils de JS Paint, puis partage l’image. Interaction navigateur et application de dessin font explicitement partie de la tâche.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="Claude pour Chrome dans JS Paint" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [Un pélican à vélo en SVG statique](https://x.com/olddonkeyblog/status/2105842745189556672) (par [@olddonkeyblog](https://x.com/olddonkeyblog))

**Testez un dessin statique détaillé avec une demande de SVG autonome.**

Le créateur demande un SVG autonome unique de pélican à vélo et partage l’image statique. Cette tâche de dessin est distincte des exemples de vélo animés.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="Un pélican à vélo en SVG statique" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [BlockBench MCP avec une compétence Minecraft](https://x.com/TOPSTR1X/status/2105839618872738138) (par [@TOPSTR1X](https://x.com/TOPSTR1X))

**Fournissez un outil de modélisation et une compétence de style pour générer un personnage de jeu.**

L’auteur fournit BlockBench MCP et une compétence Minecraft personnalisée de modélisation et de coloration, puis partage le personnage. Ces outils et indications de style sont des entrées explicites du workflow.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="BlockBench MCP avec une compétence Minecraft" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [Dig Dug dans un seul fichier HTML](https://x.com/imjustnewatai/status/2105831117677084841) (par [@imjustnewatai](https://x.com/imjustnewatai))

**Visez un unique livrable HTML pour recréer un petit jeu de navigateur.**

Le créateur demande une recréation de Dig Dug dans un seul fichier HTML et partage l’enregistrement du jeu obtenu. Le post décrit la construction comme issue d’un prompt unique.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="Dig Dug dans un seul fichier HTML" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [Une pieuvre mécanique en SVG](https://x.com/SEO/status/2105812236774297943) (par [@SEO](https://x.com/SEO))

**Examinez détail et mouvement dans le design SVG avec une créature mécanique.**

L’auteur partage une pieuvre SVG animée avec des détails mécaniques. L’enregistrement constitue un exemple concret de design vectoriel autour de petites pièces mobiles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="Une pieuvre mécanique en SVG" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [Humanity Walks à travers les styles artistiques](https://x.com/l_mejiaC/status/2105801379956850793) (par [@l_mejiaC](https://x.com/l_mejiaC))

**Faites traverser une suite de styles historiques à un personnage récurrent.**

Le créateur original présente une marche continue à travers vingt tableaux en environ soixante-quatorze secondes et mentionne de la musique codée. Chaque frontière transforme le personnage et la scène dans un nouveau style.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="Humanity Walks à travers les styles artistiques" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [Une scène libre de trou noir](https://x.com/rohit3a/status/2105786053412208835) (par [@rohit3a](https://x.com/rohit3a))

**Explorez une visualisation de trou noir avec un brief créatif ouvert.**

Le créateur demande ce que le modèle ferait pour l’impressionner et partage une scène de trou noir. La tâche est une exploration visuelle libre plutôt qu’une construction d’interface prescrite.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="Une scène libre de trou noir" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [Comparaison d’animations de méduses aurorales](https://x.com/SPAC89/status/2105783511433318451) (par [@SPAC89](https://x.com/SPAC89))

**Comparez déformations et mouvements dans deux animations de méduses.**

L’auteur compare Fable XHigh et GPT Sol Ultra sur une animation de méduse aurorale et parle de consommation de quota. Les résultats viennent d’abonnements différents.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="Comparaison d’animations de méduses aurorales" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Un SVG Nintendo Switch avec assemblage et démarrage](https://x.com/ishuagra02/status/2105779174921359470) (par [@ishuagra02](https://x.com/ishuagra02))

**Associez le mouvement des manettes et le démarrage dans une animation SVG.**

Le créateur partage un SVG Nintendo Switch où les manettes s’emboîtent avant l’animation du logo de démarrage. Il annonce une durée d’une minute trente-neuf et un coût de 1,34 dollar pour cet essai.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Un SVG Nintendo Switch avec assemblage et démarrage" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [La scène 3D interactive The Loom](https://x.com/Mr_Salio/status/2105774088492916757) (par [@Mr_Salio](https://x.com/Mr_Salio))

**Explorez paysage et bâtiments sur une même page interactive 3D.**

L’auteur présente The Loom, une scène interactive avec bâtiments et paysage. L’enregistrement montre le résultat concret de la page issue de son test.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="La scène 3D interactive The Loom" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [Reels de motion design avec le même prompt](https://x.com/mesmerlord/status/2105758042830549235) (par [@mesmerlord](https://x.com/mesmerlord))

**Comparez le point focal et la synchronisation rythmique de deux reels issus du même prompt.**

L’auteur partage deux premiers résultats de motion design de Fable 5.5 obtenus avec le même prompt et relève, avec prudence, un point focal plus clair et une meilleure synchronisation rythmique que dans un essai avec Opus. Les deux vidéos originales sont présentées ensemble.

```
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

[@shneural](https://x.com/shneural/status/2103151003272962130)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="Reels de motion design avec le même prompt" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29b80ef5ba92b029630a1628.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0da5945bc240b424bfebbd9.jpg" alt="Reels de motion design avec le même prompt" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [Un décor plus propre mais moins profond](https://x.com/eviljoker88/status/2105755840175034447) (par [@eviljoker88](https://x.com/eviljoker88))

**Conservez les critiques esthétiques dans une comparaison de scènes générées.**

L’auteur partage des scènes japonaises côte à côte et préfère la profondeur du résultat Opus, malgré l’apparence plus nette de l’autre résultat.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="Un décor plus propre mais moins profond" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [Des résultats mitigés pour une scène japonaise](https://x.com/eviljoker88/status/2105755408342126936) (par [@eviljoker88](https://x.com/eviljoker88))

**Documentez les avis mitigés sans déclarer un gagnant évident dès la première comparaison.**

L’auteur partage une première comparaison de scènes japonaises et juge les résultats mitigés. L’image conserve les sorties concrètes à l’origine de cet avis esthétique.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="Des résultats mitigés pour une scène japonaise" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [Comparaisons de manettes SVG](https://x.com/notjazii/status/2105751542498464169) (par [@notjazii](https://x.com/notjazii))

**Comparez les dessins de manette avant et après une tâche visuelle similaire.**

L’auteur partage les versions avant et après de manettes SVG dans une image comparative. Le cas porte sur les changements visibles du dessin et de sa présentation, plutôt que sur un classement général des modèles.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="Comparaisons de manettes SVG" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [Une scène d’appareil industriel](https://x.com/RayaneRachid_/status/2105744517735354410) (par [@RayaneRachid_](https://x.com/RayaneRachid_))

**Utilisez un appareil mécanique comme tâche ciblée de conception de scène 3D.**

Le créateur partage une scène d’appareil industriel en 3D et la qualifie de meilleur résultat en une seule génération. L’image donne une référence concrète de composition mécanique.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="Une scène d’appareil industriel" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [Reconstruction d’une créature géante à carapace et branchies](https://x.com/Josh67Joshua/status/2105739832563769697) (par [@Josh67Joshua](https://x.com/Josh67Joshua))

**Explorez une reconstruction en deux prompts avec une description précise de créature.**

L’auteur partage le dessin d’une créature géante à carapace et branchies, obtenu selon lui en deux prompts. L’image fournit le résultat visible de la tâche de création de créature.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="Reconstruction d’une créature géante à carapace et branchies" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [Une manette GameCube en deux prompts](https://x.com/marmaduke091/status/2105735266032095349) (par [@marmaduke091](https://x.com/marmaduke091))

**Examinez un dessin obtenu en deux prompts avec une manette familière.**

L’auteur partage un dessin de manette GameCube et dit avoir utilisé deux prompts. Cette image statique se distingue des démonstrations Xbox et des autres manettes.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="Une manette GameCube en deux prompts" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [Une capture adaptée à un post X](https://x.com/chetaslua/status/2105733677003292983) (par [@chetaslua](https://x.com/chetaslua))

**Examinez comment un assistant adapte une capture à une publication sociale.**

Le créateur partage une retouche de capture destinée à X et dit que l’assistant l’a effectuée sans demande explicite. L’image jointe est le résultat visible.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="Une capture adaptée à un post X" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [Une scène sakura en voxels avant et après](https://x.com/kdnbmb/status/2105704791049412755) (par [@kdnbmb](https://x.com/kdnbmb))

**Comparez des résultats successifs en voxels sur le même sujet visuel.**

La personne qui publie partage deux versions d’une île sakura en voxels. L’image comparative consigne les différences visibles du design avant et après.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="Une scène sakura en voxels avant et après" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [Le prototype d’interface textile SHADERKIN](https://x.com/mszzz0011/status/2106025576972853642) (par [@mszzz0011](https://x.com/mszzz0011))

**Explorez effets de tissu et réglages ajustables dans un prototype d’interface.**

L’auteur partage un prototype SHADERKIN avec effets de tissu et réglages de paramètres, décrit comme une construction en une génération. L’enregistrement montre l’interface et les mouvements obtenus.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="Le prototype d’interface textile SHADERKIN" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [Une animation partagée d’interface à horloge dorée](https://x.com/AISuperDomain/status/2106396754539360272) (par [@AISuperDomain](https://x.com/AISuperDomain))

**Utilisez une animation d’horloge comme référence de composition d’interface.**

La personne qui publie présente une animation frontend à horloge dorée. Le clip fournit une référence partagée pour examiner composition, motif d’horloge et présentation visuelle animée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="Une animation partagée d’interface à horloge dorée" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [Le récit Before There Was Anything](https://x.com/crowqnt/status/2106146218846081435) (par [@crowqnt](https://x.com/crowqnt))

**Explorez un récit cosmique et humain dans un film animé partagé.**

La personne qui publie partage Before There Was Anything, un récit vidéo sur le cosmos et l’humanité. Le film est conservé comme exemple partagé de narration visuelle.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="Le récit Before There Was Anything" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [Un vortex partagé de particules bleues](https://x.com/AISuperDomain/status/2105846981776003107) (par [@AISuperDomain](https://x.com/AISuperDomain))

**Examinez mouvement et composition d’une visualisation partagée de vortex.**

La personne qui publie partage une animation de vortex de particules bleues. Le clip offre un exemple concret partagé pour examiner mouvement des particules, structure visuelle et composition.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="Un vortex partagé de particules bleues" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [Une interface à plusieurs panneaux après deux révisions](https://x.com/ZorroOfMorocco/status/2106547078235095485) (par [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**Affinez une interface par révisions plutôt que de vous arrêter à la première sortie.**

L’auteur partage une interface terminée à plusieurs panneaux et rapporte environ trois heures de travail avec deux révisions. La capture présente le design visuel final.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="Une interface à plusieurs panneaux après deux révisions" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [Des animaux empilés dans une scène rendue](https://x.com/legit_api/status/2117237103289315574) (par [@legit_api](https://x.com/legit_api))

**Examinez l’équilibre d’une composition statique avec plusieurs personnages et matériaux.**

Le post présente un ours, un panda et un ours polaire empilés, crédite yuruzuu sur Discord et annonce une exécution de vingt et une minutes. Le post public est conservé comme source visuelle partagée.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="Des animaux empilés dans une scène rendue" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [Quatre essais de RPG en monde ouvert comparés](https://x.com/noclipepe/status/2117222592536789149) (par [@noclipepe](https://x.com/noclipepe))

**Comparez présentation, combat et collisions sur la même tâche créative de jeu.**

Le créateur montre quatre RPG en un prompt, étiquetés Fable 5.5, GPT-6.2 Astra, Opus 5.5 et Fable 5.1. Ses commentaires opposent éclairage, combat, inventaire, collisions et blocage d’un personnage.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="Quatre essais de RPG en monde ouvert comparés" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [Deux animations frontend comparées](https://x.com/leo114119/status/2117209849842761983) (par [@leo114119](https://x.com/leo114119))

**Comparez conception de scène et détails en regardant les animations ensemble.**

Le post juxtapose des animations codées étiquetées Astra et Fable en discutant détails et conception du script. Il crédite explicitement @chetaslua pour l’animation Fable.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="Deux animations frontend comparées" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [Un film de robot moussu généré par code](https://x.com/chetaslua/status/2117169796290916732) (par [@chetaslua](https://x.com/chetaslua))

**Explorez une scène cinématographique complète en code à partir d’un brief d’animation.**

Le créateur partage une animation de forêt et de robot, décrite comme film codé en une génération. Le post renvoie au prompt visible dans une capture et compare le résultat à d’autres essais.

Une publication supplémentaire montre un essai témoin d’Opus 5.5 rapporté séparément. [@AnikaCodes](https://x.com/AnikaCodes) · [Exemple associé](https://x.com/AnikaCodes/status/2117222374642946297)

Selon son auteur, un essai associé avec GPT-6 Astra Max utilise des images générées dans le workflow. Les différentes méthodes de production restent ainsi visibles aux côtés du film original. [@rubenssoto_ai](https://x.com/rubenssoto_ai) · [Comparaison associée](https://x.com/rubenssoto_ai/status/2117707344704352691)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="Un film de robot moussu généré par code" width="760"></a></td><td valign="top"><p>Une publication supplémentaire montre un essai témoin d’Opus 5.5 rapporté séparément.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="Un film de robot moussu généré par code" width="760"></a></td><td valign="top"><p>GPT-6 Astra Max</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/25b0cfcdb1fdda22ba6aa9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/75f37c74099d5b9ba1ad0ddc.jpg" alt="GPT-6 Astra Max" width="760"></a></td></tr></table>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [Une simulation de port à conteneurs revisitée](https://x.com/anxuanng/status/2117124831279972812) (par [@anxuanng](https://x.com/anxuanng))

**Revisitez une scène en conservant le contexte du projet pour la comparaison visuelle.**

L’auteur publie une nouvelle scène de port à conteneurs et cite sa simulation Blender et Three.js antérieure, dont grues, navires, véhicules et conteneurs avaient été modélisés pour un environnement de type stratégie.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="Une simulation de port à conteneurs revisitée" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [Une scène de piste d’aéroport revisitée](https://x.com/anxuanng/status/2117096574878921119) (par [@anxuanng](https://x.com/anxuanng))

**Comparez une scène d’aéroport révisée au projet antérieur et à son workflow d’éléments.**

L’auteur revient sur une scène de zone aéroportuaire, cite sa simulation Blender et Three.js antérieure et partage de nouvelles images d’avions, véhicules de service et infrastructures de terminal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="Une scène de piste d’aéroport revisitée" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [Un pélican à vélo dans des mondes 3D abstraits](https://x.com/xiax0603/status/2116960224829665543) (par [@xiax0603](https://x.com/xiax0603))

**Examinez les transitions entre espaces avec un sujet à vélo.**

Le post présente une animation de pélican et vélo à travers fragments géométriques et environnement numérique abstrait, puis un recul à travers un œil. La séquence constitue une démonstration distincte de transitions de scène.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="Un pélican à vélo dans des mondes 3D abstraits" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [Une scène de voilier historique](https://x.com/abhinavflac/status/2116945827738665060) (par [@abhinavflac](https://x.com/abhinavflac))

**Examinez eau, lumière et composition environnementale dans une scène de navire.**

Le post partage une scène de voilier historique et la décrit comme un résultat interactif sans exemple préalable. L’enregistrement fournit un échantillon visuel concret du navire et de l’eau qui l’entoure.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="Une scène de voilier historique" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [Comparaisons de cyclistes et d’allures avec Carbon](https://x.com/AI_Screening/status/2116934172757660014) (par [@AI_Screening](https://x.com/AI_Screening))

**Comparez mouvement des personnages et construction des scènes avec des sorties appariées.**

L’auteur réunit des exemples de cyclistes et de zèbres étiquetés Fable et Carbon dans une vidéo composite. Il juge les checkpoints proches ; les images appariées fournissent des échantillons précis de mouvement.

La comparaison de cyclistes publiée précédemment seule est incluse avec la vidéo composite. [@AI_Screening](https://x.com/AI_Screening) · [Exemple associé](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="Comparaisons de cyclistes et d’allures avec Carbon" width="760"></a></td><td valign="top"><p>La comparaison de cyclistes publiée précédemment seule est incluse avec la vidéo composite.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="Comparaisons de cyclistes et d’allures avec Carbon" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [Présentation d’une bouteille de boisson gazeuse](https://x.com/abhinavflac/status/2116919086521499730) (par [@abhinavflac](https://x.com/abhinavflac))

**Examinez matériaux, forme et présentation dans un court clip de rendu produit.**

Le post montre une bouteille de boisson gazeuse et décrit un résultat de routage en une génération. Le clip est conservé sans reprendre le nom de marque incohérent de sa légende.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="Présentation d’une bouteille de boisson gazeuse" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [Mouvements de pélican comparés à Astra](https://x.com/Octoberry/status/2116918967558095131) (par [@Octoberry](https://x.com/Octoberry))

**Regardez les clips appariés pour comparer réalisme, couleurs et mouvements.**

La personne qui publie juxtapose des scènes de pélicans étiquetées Fable et Astra et commente réalisme et couleurs. L’enregistrement comparatif garde les deux traitements visuels ensemble.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="Mouvements de pélican comparés à Astra" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [Un brief de motion design pour animations codées](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (par [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**Partez d’un brief concret pour demander des titres animés ou des introductions produit.**

Le post partage une capture de brief de motion design pour introductions, logos animés, titres et scènes 3D, et propose de l’appliquer avec Claude. L’image source conserve les instructions.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="Un brief de motion design pour animations codées" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [Un portrait voxel d’après une photo](https://x.com/chetaslua/status/2116912822806520027) (par [@chetaslua](https://x.com/chetaslua))

**Examinez comment un portrait voxel préserve les traits reconnaissables de sa photo de référence.**

Le créateur associe une photo de Sam Altman à un portrait voxel, décrit comme obtenu en une génération. L’image côte à côte fournit ensemble référence et interprétation.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="Un portrait voxel d’après une photo" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [Des pélicans volants comparés à Opus](https://x.com/leo114119/status/2116901575490929109) (par [@leo114119](https://x.com/leo114119))

**Comparez composition et animation avec un agencement d’objets ludique.**

Le post superpose des clips étiquetés Fable et Opus d’un vélo sur un pélican volant. Le montage crédite @notjazii pour le clip Fable et garde les deux traitements visibles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="Des pélicans volants comparés à Opus" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [La scène web de pélican Morning Ride](https://x.com/leo114119/status/2116893571739775220) (par [@leo114119](https://x.com/leo114119))

**Examinez détails du personnage et présentation de page dans une balade côtière à vélo.**

L’auteur partage un pélican à vélo en 3D dans une page Morning Ride et attire l’attention sur plumage, pattes, détails du vélo et décor côtier.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="La scène web de pélican Morning Ride" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [Un même prompt avec des styles différents](https://x.com/notjazii/status/2116893197939224714) (par [@notjazii](https://x.com/notjazii))

**Laissez chaque modèle choisir son style, puis comparez la composition obtenue.**

L’auteur dit avoir testé deux modèles avec le même prompt en laissant chacun choisir son style. La vidéo juxtapose des compositions et niveaux de détail distincts.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="Un même prompt avec des styles différents" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [Une composition avec pélican, vélo et cheval](https://x.com/abhinavflac/status/2116881397986288017) (par [@abhinavflac](https://x.com/abhinavflac))

**Testez l’agencement de plusieurs sujets en interaction dans une animation.**

Le post montre un pélican volant avec un vélo tandis qu’un cheval court en dessous. Le clip fournit un échantillon concret de cette composition multi-objets inhabituelle et de ses mouvements.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="Une composition avec pélican, vélo et cheval" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [Une scène isométrique inspirée d’un tweet de référence](https://x.com/chetaslua/status/2116878661035106515) (par [@chetaslua](https://x.com/chetaslua))

**Guidez une nouvelle scène avec une publication de référence plutôt qu’un exemple générique.**

Le créateur rapporte n’avoir utilisé qu’un tweet cité de Post Humans comme référence et partage la scène isométrique obtenue. Le clip présente une composition de type ferme avec commande de saison.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="Une scène isométrique inspirée d’un tweet de référence" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [Gros plans mécaniques d’un vélo de pélican](https://x.com/NFT_Chen/status/2116869725703782507) (par [@NFT_Chen](https://x.com/NFT_Chen))

**Examinez mouvement du plateau, détails des plumes et caméra autour d’un sujet à vélo.**

Le post partage des gros plans d’un pélican à vélo au bord de l’eau. L’enregistrement passe de la mécanique du vélo à la tête de l’oiseau puis à une vue plus large sur la promenade.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="Gros plans mécaniques d’un vélo de pélican" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [Un vélo qui roule sur un pélican](https://x.com/notjazii/status/2116861637890379891) (par [@notjazii](https://x.com/notjazii))

**Inversez la relation habituelle des sujets pour tester la composition spatiale.**

Le créateur partage une animation de vélo sur pélican. Le clip place le vélo au-dessus d’un oiseau volant, variant la tâche familière du pélican sur un vélo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="Un vélo qui roule sur un pélican" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [Styles SVG de pélican comparés à Carbon](https://x.com/leo114119/status/2116652334734332212) (par [@leo114119](https://x.com/leo114119))

**Comparez réalisme et illustration sans transformer des esthétiques différentes en classement universel.**

Le post réunit des pélicans à vélo de Carbon et Fable. L’auteur oppose rendu de bande dessinée et traitement plus réaliste, en notant que cette différence complique la comparaison.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="Styles SVG de pélican comparés à Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [Un oiseau bleu de dessin animé à vélo](https://x.com/birdabo/status/2116553049183560012) (par [@birdabo](https://x.com/birdabo))

**Examinez un personnage de dessin animé familier dans une composition à vélo.**

Le post partage un oiseau bleu de dessin animé roulant à vélo au bord de l’eau, avec la légende Fable 5.5 Max. L’image est conservée comme échantillon visuel statique concret.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="Un oiseau bleu de dessin animé à vélo" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [Une capture de pélican sur une route forestière](https://x.com/leo114119/status/2116154940364374269) (par [@leo114119](https://x.com/leo114119))

**Examinez plumes, pattes et géométrie du vélo dans une scène rendue par navigateur.**

La personne qui publie partage une capture de navigateur montrant un pélican à vélo sur une route forestière et souligne texture des plumes, pattes et détails du vélo.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="Une capture de pélican sur une route forestière" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [Un combat de bonshommes allumettes comparé à Carbon](https://x.com/leo114119/status/2116084152986656933) (par [@leo114119](https://x.com/leo114119))

**Comparez chorégraphie et mouvement dans les échantillons d’animation appariés.**

L’enregistrement comparatif porte les mentions Fable 5.1 High et Carbon. L’auteur discute la qualité relative des animations de combat de bonshommes allumettes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="Un combat de bonshommes allumettes comparé à Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [Une référence SVG de pélican issue de premiers tests](https://x.com/ChrisGPT/status/2115872567122608591) (par [@ChrisGPT](https://x.com/ChrisGPT))

**Conservez une référence sourcée pour examiner stylisation et géométrie du vélo.**

La personne qui publie met en avant un pélican à vélo et cite un post de premiers tests créditant kostikz sur Discord. L’image de référence et sa chaîne d’attribution sont conservées.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="Une référence SVG de pélican issue de premiers tests" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [Une référence de pélican dans des tests SVG comparés](https://x.com/AdamHoltererer/status/2115858542221492300) (par [@AdamHoltererer](https://x.com/AdamHoltererer))

**Gardez la référence Fable avec le contexte du test SVG environnant.**

La personne qui publie ajoute un pélican à vélo comme référence Fable sous son fil de test SVG de Mistral Large 4. Cela fournit une image sourcée pour l’examen entre modèles.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="Une référence de pélican dans des tests SVG comparés" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [Détails de vélos SVG comparés à Carbon](https://x.com/insanekrishnaa/status/2115833723342250186) (par [@insanekrishnaa](https://x.com/insanekrishnaa))

**Comparez des éléments précis comme paniers, décors et textures des plumes.**

Le post compare des pélicans à vélo de Fable et Carbon en discutant paniers, détails de décor et plumage. Il propose une analyse visuelle précise plutôt qu’un vaste ensemble de tâches.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="Détails de vélos SVG comparés à Carbon" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [Une implantation dans un canyon en 3D](https://x.com/Mr_Salio/status/2115813400915714177) (par [@Mr_Salio](https://x.com/Mr_Salio))

**Examinez détails environnementaux et composition spatiale d’une scène habitée.**

Le post partage une vaste implantation dans un canyon et présente l’enregistrement comme démonstration d’un nouveau checkpoint Claude. Les images montrent bâtiments, paysage et composition de scène.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="Une implantation dans un canyon en 3D" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [Détails de manettes comparés à Opus](https://x.com/notjazii/status/2115808169075351632) (par [@notjazii](https://x.com/notjazii))

**Examinez forme, commandes et détails de dessins de manettes appariés.**

L’auteur présente ensemble des dessins de manettes étiquetés Fable et Opus et insiste sur le détail de la version supérieure. L’image conserve les deux dessins comparés.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="Détails de manettes comparés à Opus" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [Un workflow hebdomadaire d’audit SEO de site](https://x.com/cleeeeeeeeement/status/2115488774423773267) (par [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**Transformez un site en plan SEO priorisé et en suivi régulier du classement.**

Le créateur décrit un système qui reçoit un site, identifie concurrents et mots-clés, puis produit un plan SEO priorisé. Une courte vidéo accompagne la description du suivi hebdomadaire du classement et de son exécution.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="Un workflow hebdomadaire d’audit SEO de site" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [Réutiliser des éléments Fable dans du motion design Opus](https://x.com/chetaslua/status/2115145163542790170) (par [@chetaslua](https://x.com/chetaslua))

**Séparez création des éléments et assemblage du motion design en combinant modèles et outils.**

Le créateur partage du motion design Opus 5.5 pour une Tesla Roadster avec des éléments qu’il attribue à une génération Fable antérieure. Le workflow cité mentionne Python dans Blender, ElevenLabs et une vidéo de lancement fournie.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="Réutiliser des éléments Fable dans du motion design Opus" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [Une application de mandalas et formes géométriques](https://x.com/ZMinimalistYogi/status/2114600083165434189) (par [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**Transformez une idée géométrique ciblée en application interactive d’exploration créative.**

Le créateur raconte trois heures de conversation avec Fable 5.1 pour construire une application de mandalas, zomes, solides d’Archimède et yantras géométriques en lotus. Il la partage sur son site personnel.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="Une application de mandalas et formes géométriques" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Un cycliste sur un vélo en Three.js](https://x.com/AI_Screening/status/2114266369248354357) (par [@AI_Screening](https://x.com/AI_Screening))

**Examinez posture du cycliste, géométrie du vélo et coordination du mouvement.**

Le créateur partage un cycliste sur un vélo réalisé en Three.js. L’enregistrement fournit un échantillon concret de mouvement, avec un pont et un paysage de bord d’eau autour du cycliste.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Un cycliste sur un vélo en Three.js" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [Instantané de l’évaluation FrontierCS 2](https://x.com/wenhaocha1/status/2115613415641354262) (par [@wenhaocha1](https://x.com/wenhaocha1))

**Comparez Fable 5.1 aux autres modèles à partir d’un graphique de benchmark lié à sa source.**

L’auteur ajoute Fable 5.1 à un graphique des taux de réussite de FrontierCS 2 et partage les résultats rapportés aux côtés de ceux des autres modèles.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="Instantané de l’évaluation FrontierCS 2" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [Comparaison d’animations de zèbres entre trois modèles](https://x.com/AI_Screening/status/2115849659797373038) (par [@AI_Screening](https://x.com/AI_Screening))

**Comparez une tâche de zèbre au galop en regardant ensemble les trois sorties étiquetées par modèle.**

L’auteur présente côte à côte des animations de zèbre étiquetées Fable 5.5, Opus 5.5 et Gemini 4 Argon. Les images partagées fournissent des échantillons précis d’allure dans les trois sorties.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="Comparaison d’animations de zèbres entre trois modèles" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [Critiquer la lisibilité de longs textes japonais](https://x.com/AM09_21/status/2106670042184356156) (par [@AM09_21](https://x.com/AM09_21))

**Demandez au modèle de diagnostiquer les problèmes de lisibilité d’un texte japonais généré.**

L’auteur indique avoir demandé pourquoi les longs textes japonais d’Opus sont difficiles à lire. La réponse mentionne une syntaxe calquée sur l’anglais, les répétitions et les retouches superficielles, illustrant un workflow concret de critique rédactionnelle.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [Un PowerPoint technique guidé par des exemples](https://x.com/mt_moco/status/2106665038375522791) (par [@mt_moco](https://x.com/mt_moco))

**Fournissez des exemples avant de demander une présentation technique.**

L’auteur rapporte que quelques présentations modèles ont permis d’obtenir un PowerPoint technique utilisable. Son témoignage relie le prompting par exemples à une amélioration de la structure documentaire dans une tâche précise.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [Comparer la cohérence musicale](https://x.com/AM09_21/status/2106573080214770011) (par [@AM09_21](https://x.com/AM09_21))

**Évaluez séparément les détails locaux et la cohérence globale d’une musique générée.**

L’auteur compare des compositions de modèles à travers les notes, la mélodie et les transitions, en distinguant la cohérence locale de la structure musicale globale. Il s’agit d’une évaluation de la composition fondée sur l’écoute.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [Une fin de tâche prématurée et des designs moins bons](https://x.com/johntitorIII/status/2106442876506747353) (par [@johntitorIII](https://x.com/johntitorIII))

**Vérifiez les livrables au regard des exigences avant d’accepter qu’un agent annonce la fin.**

L’auteur décrit plusieurs jours de tests durant lesquels des tâches inachevées étaient déclarées terminées et les designs inférieurs à ceux d’autres modèles. Le témoignage documente l’achèvement prématuré et la qualité du design comme échecs pratiques.

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [Une œuvre de calmar jugée dérangeante](https://x.com/hanawo_neki/status/2106271036094415186) (par [@hanawo_neki](https://x.com/hanawo_neki))

**Précisez vos préférences esthétiques lorsqu’une demande artistique ouverte produit un style indésirable.**

L’auteur raconte avoir demandé une œuvre de calmar quelconque et reçu des détails denses et regroupés qu’il trouvait inconfortables. Le témoignage décrit un décalage esthétique dans une demande visuelle ouverte.

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [Du motion design à l’esthétique de plan technique](https://x.com/DavidayoAI/status/2106054662063325638) (par [@DavidayoAI](https://x.com/DavidayoAI))

**Utilisez une esthétique de plan technique comme direction visuelle d’une courte animation.**

L’auteur raconte avoir demandé une animation rapide et obtenu un résultat de type plan technique après environ quinze minutes. L’œuvre complète est liée sur YouTube.

[Exemple associé](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [Oiseaux et poissons dans un paysage sakura en voxels](https://x.com/xodud_rkd/status/2105876716472447046) (par [@xodud_rkd](https://x.com/xodud_rkd))

**Explorez la faune animée dans un paysage en voxels.**

L’auteur décrit une scène sakura en voxels avec oiseaux mobiles et poissons dans un étang, puis lie l’artefact interactif. La page partagée est le résultat associé à cette scène.

[Exemple associé](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [Un retour d’échec sur la génération de personnages](https://x.com/doof1789559/status/2105874208458752227) (par [@doof1789559](https://x.com/doof1789559))

**Conservez les expériences négatives de personnages avec les démonstrations visuelles réussies.**

L’auteur rapporte de mauvais résultats de génération de personnages et reconnaît explicitement que son approche pourrait en être la cause. Le post conserve cette expérience négative pour l’évaluation de tâches de personnages.

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [Un SVG de pélican avec durée et coût](https://x.com/AnonymerNutze12/status/2105740440385499295) (par [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**Associez un dessin aux observations de durée et de coût de son créateur.**

L’auteur lie un artefact HTML de pélican en SVG et indique durée et coût de l’essai. L’artefact lié est le résultat concret mentionné par le post.

[Exemple associé](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [Coder à distance sur téléphone avec Claude Code](https://x.com/beistnormie/status/2106546741000417781) (par [@beistnormie](https://x.com/beistnormie))

**Explorez la supervision distante d’essaims d’agents de code depuis un téléphone.**

L’auteur rapporte coder à distance avec des essaims Claude Code depuis son téléphone pendant un voyage. Le post est un récit de workflow personnel, pas un tutoriel de projet ni une procédure d’implémentation.

Type: Integration | Date: 2026-10-04

---

<a id="case-280"></a>
### Case 280: [La Voie lactée au-dessus d’un lac alpin](https://x.com/hakmgpt/status/2118178083983573492) (par [@hakmgpt](https://x.com/hakmgpt))

**Examinez une longue séquence de caméra associant les reflets des montagnes à un ciel nocturne en mouvement.**

L’animation partagée, longue de 92 secondes, passe d’un lac alpin à une Voie lactée lumineuse, puis revient au ciel reflété. Le compte qui la publie attribue cette scène rendue à Fable 5.5.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5cb879d0a07a0f6e9fff5cf6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/91432c6827d650eb28f2269b.jpg" alt="La Voie lactée au-dessus d’un lac alpin" width="760"></a>

Type: Demo | Date: 2026-11-05

---

<a id="case-281"></a>
### Case 281: [Saut de baleine avec eau et son procéduraux](https://x.com/camperaigg/status/2118069524306284556) (par [@camperaigg](https://x.com/camperaigg))

**Réunissez prises de vue sous-marines, saut hors de l’eau et audio synthétisé dans une même séquence animée.**

Le créateur annonce 154 minutes pour un film de 31 secondes comprenant une baleine procédurale, une simulation de fluides, l’ombrage de l’océan et du son synthétisé. Ses notes décrivent l’inspection d’images agrandies et la correction des embruns avant un nouveau rendu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b98c309a3c226bd24386940f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1bcb86163b677ad0a4172d13.jpg" alt="Saut de baleine avec eau et son procéduraux" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-282"></a>
### Case 282: [Mouvement de zèbres comparé entre quatre modèles](https://x.com/AI_Screening/status/2118014564457668955) (par [@AI_Screening](https://x.com/AI_Screening))

**Comparez l’allure, l’anatomie et le style de scène pour une même tâche d’animation animale.**

Les quatre clips superposés portent les étiquettes Gemini 4 Carbon, Fable 5.5, Opus 5.5 et Argon. Conserver le montage complet permet de voir les différences de mouvement des pattes, de forme du corps et de traitement de l’arrière-plan.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/6fdcb38bf56493c314dba5b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/890d1b92800ee622275ec8d7.jpg" alt="Mouvement de zèbres comparé entre quatre modèles" width="760"></a>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-283"></a>
### Case 283: [Recherche de créateurs en langage naturel dans Lightreel](https://x.com/lightreelai/status/2118010927199248705) (par [@lightreelai](https://x.com/lightreelai))

**Transformez vos critères de créateurs en une recherche avec des seuils explicites d’abonnés et de vues.**

Lightreel présente cette démonstration de recherche de créateurs sous l’étiquette Fable 5.5. La vidéo saisit une requête visant des créateurs en couple ayant moins de 10,000 abonnés et une vidéo dépassant 100,000 vues, puis affiche des résultats de vidéos sociales.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5aef4b1766a560a35264c3ed.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1c6d9c1fb3c69b3aa2ee1976.jpg" alt="Recherche de créateurs en langage naturel dans Lightreel" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-284"></a>
### Case 284: [Un navire volant au-dessus d’une mer de nuages](https://x.com/devteamdrew/status/2118008142403649662) (par [@devteamdrew](https://x.com/devteamdrew))

**Utilisez un film plus long pour examiner la continuité des plans lorsque la lumière et la météo changent.**

Le créateur décrit une animation d’environ 100 secondes réalisée en JavaScript et Python pendant 19 heures par plusieurs équipes d’agents. La séquence partagée suit un navire volant parmi les nuages, au coucher du soleil et sous la lumière de la lune.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/17ef07a780273abf9e9b6c92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a54746701db5f7f829071d2c.jpg" alt="Un navire volant au-dessus d’une mer de nuages" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-285"></a>
### Case 285: [Cœur mécanique avec coupe animée](https://x.com/camperaigg/status/2118002649929056373) (par [@camperaigg](https://x.com/camperaigg))

**Faites apparaître les pièces mobiles d’un mécanisme tout en maintenant son mouvement principal.**

Le créateur annonce une tâche Blender de 106 minutes : un cœur mécanique pompe de l’huile dorée tandis que sa coque s’ouvre pour révéler des pistons et un vilebrequin. Ses notes abordent l’audio synthétisé et l’identification de lumières cachées responsables de reflets indésirables.

```
Make a mechanical heart and show its insides, use blender.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/157ebee3ce748cdc1e6b7970.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4a862111878dc42939f8e5e4.jpg" alt="Cœur mécanique avec coupe animée" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-286"></a>
### Case 286: [Jardin de pagode voxel flottant à explorer](https://x.com/legit_api/status/2117994730336252114) (par [@legit_api](https://x.com/legit_api))

**Évaluez un environnement généré en parcourant ses structures et ses aménagements aquatiques.**

Ce jardin voxel est attribué à un checkpoint antérieur de Fable 5.5. La caméra circule entre une pagode, des îles flottantes, un pont et des cascades, montrant la scène au niveau du sol et depuis des points de vue élevés.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/cc4d15bf5103d7eb64f63e29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/22e78c0beb2a6f509bc02739.jpg" alt="Jardin de pagode voxel flottant à explorer" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-287"></a>
### Case 287: [Une aventure océanique réalisée par huit équipes](https://x.com/0xMovez/status/2117987052419428576) (par [@0xMovez](https://x.com/0xMovez))

**Examinez la continuité entre action, effets et son synthétisé dans un film à plusieurs plans.**

Le créateur annonce un film Three.js de 83 secondes réalisé par huit équipes d’agents en moins de trois heures, avec 39 plans et du son synthétisé. Les images suivent une aventure océanique avec des engins spatiaux, des créatures marines et des vagues déferlantes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a46543512fc30e5a33cb2fc3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a307daab219d70fa5bed0c86.jpg" alt="Une aventure océanique réalisée par huit équipes" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-288"></a>
### Case 288: [Présentation interactive d’une hypercar](https://x.com/shmidtqq/status/2117977426990944736) (par [@shmidtqq](https://x.com/shmidtqq))

**Associez les gros plans du véhicule à des commandes permettant de choisir la caméra et la peinture.**

Le créateur présente un configurateur d’hypercar Three.js dans un unique fichier HTML hors ligne, dont la géométrie et les matériaux sont générés par le code. L’enregistrement montre le véhicule rouge, des gros plans des roues et de la carrosserie, les reflets et les commandes de caméra.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4bd439d08b9f8a320a8851ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a16368d4c8b7c9a3a5455607.jpg" alt="Présentation interactive d’une hypercar" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-289"></a>
### Case 289: [Naissance d’un arbre de vie](https://x.com/notjazii/status/2117972258090357164) (par [@notjazii](https://x.com/notjazii))

**Structurez une courte animation autour de la transformation visible d’une graine en arbre adulte.**

Le créateur décrit une session de programmation d’environ une heure à partir d’un seul prompt. La séquence de 30 secondes passe d’un paysage aride à une jeune pousse, puis à un arbre qui grandit, avant de révéler un monde verdoyant sous les nuages.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29df8c398a2db37856c01b0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f50b8e7c2a28df7d0d3cd903.jpg" alt="Naissance d’un arbre de vie" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-290"></a>
### Case 290: [Château ambulant aux mécanismes internes fonctionnels](https://x.com/camperaigg/status/2117966825048997914) (par [@camperaigg](https://x.com/camperaigg))

**Reliez un rig de marche à des mouvements mécaniques visibles et à une coque qui s’ouvre.**

Le créateur annonce un workflow Blender de 133 minutes avec une machine à vapeur, des trains d’engrenages, quatre pattes et huit panneaux de coque ouvrants. Ses notes décrivent la correction de l’animation de caméra et la réduction du temps de rendu après avoir identifié une géométrie d’herbe coûteuse.

```
Make me Howl's moving castle and also show its internal machinery.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e7e25e7d44993a14ab0405e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8d3b1d734d971e2dd757926c.jpg" alt="Château ambulant aux mécanismes internes fonctionnels" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-291"></a>
### Case 291: [Un personnage-toast et un scarabée mécanique](https://x.com/flxrnc/status/2117965294224232796) (par [@flxrnc](https://x.com/flxrnc))

**Examinez la mise en scène des personnages et la continuité d’une brève rencontre animée.**

Le film partagé de 40 secondes montre un personnage carré ressemblant à une tartine qui rencontre un scarabée mécanique bleu dans un champ au coucher du soleil. La source attribue le film à Fable 5.5 et renvoie à son guide de motion design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/d5e16bfd05f1c391cf32f848.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b7ae776a5c29618d061465.jpg" alt="Un personnage-toast et un scarabée mécanique" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-292"></a>
### Case 292: [Un gardien de phare dans la tempête](https://x.com/seeconvm/status/2117965120760365494) (par [@seeconvm](https://x.com/seeconvm))

**Construisez un récit court autour d’un lieu, d’un changement météorologique et d’un dénouement clair.**

Le créateur décrit un court métrage Three.js de 60 secondes avec des images rendues par code, du son synthétisé et un fichier HTML hors ligne. Les images suivent un petit gardien de phare sous la pluie et les éclairs avant une scène à l’aube.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/7ca3c1e23eac0ed20511211e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/dfcab72e07d547d9dcb1dbc1.jpg" alt="Un gardien de phare dans la tempête" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-293"></a>
### Case 293: [Une créature marine dans une ville côtière](https://x.com/BubbleBrain/status/2117963042621178000) (par [@BubbleBrain](https://x.com/BubbleBrain))

**Examinez un court métrage complet pour évaluer les mouvements, les transitions et la cohérence visuelle.**

La source partage une animation Fable 5.5 d’environ une minute mettant en scène une créature marine verte, une ville côtière et des bulles flottantes. La vidéo fournit un exemple visuel concret pour évaluer ce style de court métrage.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/65db346493bdd9973bec3a4c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4442bdca5e6a7460f03af731.jpg" alt="Une créature marine dans une ville côtière" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-294"></a>
### Case 294: [Course sur tapis comparée entre trois modèles](https://x.com/noclipepe/status/2117914944410628430) (par [@noclipepe](https://x.com/noclipepe))

**Comparez la complétude des scènes jouables, les mouvements et le traitement visuel pour une même tâche de course.**

Le créateur teste un jeu de course sur un tapis d’enfant avec Fable 5.5, Opus 5.5 et GPT-6 Astra. L’enregistrement récent à trois panneaux et la comparaison antérieure à deux modèles sont conservés ensemble ; les notes affichées dans les images sont les évaluations personnelles du créateur.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ffe3b88099594ba14f536b51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/24d8ea7644cbe19947c8c53a.jpg" alt="Course sur tapis comparée entre trois modèles" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e214760ff83ad9bfaf202484.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0340fc5579003245dfa99b1.jpg" alt="Course sur tapis comparée entre trois modèles" width="760"></a></td></tr></table>

[Comparaison associée · @noclipepe](https://x.com/noclipepe/status/2117729666576302187)

Type: Evaluation | Date: 2026-11-04

---

<a id="case-295"></a>
### Case 295: [Un camion se transforme en robot](https://x.com/camperaigg/status/2117914482752299311) (par [@camperaigg](https://x.com/camperaigg))

**Utilisez une transformation pour examiner le rigging, le contact au sol et le son synchronisé.**

Le créateur annonce 107 minutes dans Blender avec un rig de 51 articulations, un solveur de contact au sol, de la pluie procédurale et des effets sonores synthétisés. L’enregistrement montre le camion se déplier en un robot debout sur une chaussée mouillée.

```
Make me a transformer truck with animations of its transforming.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/72ef538a8fb4b94f0e2d7e2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ea8537c130cd5623959dc275.jpg" alt="Un camion se transforme en robot" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-296"></a>
### Case 296: [Images d’animation de Fable et Hunyuan](https://x.com/xbquan/status/2117899651365908855) (par [@xbquan](https://x.com/xbquan))

**Comparez les images correspondantes avant de tirer des conclusions sur une animation entière.**

L’auteur partage deux paires de captures portant les étiquettes Fable 5.5 et Hunyuan 4. Chaque paire réunit les résultats du personnage et de l’environnement ; ces images fixes permettent une comparaison visuelle des images montrées.

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e6c6551a29757e1eb7c31f36.jpg" alt="Images d’animation de Fable et Hunyuan" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/864db255f6fd2807b689d7d7.jpg" alt="Images d’animation de Fable et Hunyuan" width="760"></td></tr></table>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-297"></a>
### Case 297: [Une animation sur le partage de la lumière](https://x.com/abhinavflac/status/2117883591019708740) (par [@abhinavflac](https://x.com/abhinavflac))

**Transformez un thème abstrait en un récit court doté d’une fin visible.**

Après une demande de montrer ce que signifie la bonté, une animation et un son produits par code sont attribués au modèle. Une silhouette lumineuse donne sa lumière à un enfant, puis brille davantage tandis que le paysage environnant se remplit de couleurs.

```
Show me what kindness means to you
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b888d1a62b4d27ae2fca8226.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5bd15fc5c234b4b114765d6f.jpg" alt="Une animation sur le partage de la lumière" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-298"></a>
### Case 298: [Un village voxel entre les montagnes](https://x.com/abhinavflac/status/2117377130388656569) (par [@abhinavflac](https://x.com/abhinavflac))

**Explorez un village généré à plusieurs échelles pour examiner sa cohérence spatiale.**

Le créateur d’origine partage un village voxel vivant avec des maisons, des voies d’eau et de petits habitants, vu depuis la rive, d’en haut et au sein des montagnes environnantes. Un post associé en chinois propose un prompt détaillé pour la scène.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae5269b0eff86da4580064d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e612faf20dd5f5de4ee171b.jpg" alt="Un village voxel entre les montagnes" width="760"></a>

[@cfenghub](https://x.com/cfenghub/status/2117775332535148752)

Type: Demo | Date: 2026-11-02

---

<a id="case-299"></a>
### Case 299: [Composition pélican-éléphant comparée entre quatre modèles](https://x.com/pipeline_os/status/2117719191478513700) (par [@pipeline_os](https://x.com/pipeline_os))

**Comparez la façon dont différents modèles gèrent plusieurs sujets en interaction dans une animation.**

L’enregistrement à quatre panneaux présente côte à côte une tâche associant pélican, vélo, crocodile et éléphant pour Gemini 4 Argon, Opus 5.5, Fable 5.5 et Kimi K3.1 Pro. Le montage complet conserve la disposition et les mouvements des sujets de chaque modèle.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/9db78999efffeffa7ccaca0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/15a45dc0efe3247f0821c8a2.jpg" alt="Composition pélican-éléphant comparée entre quatre modèles" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-300"></a>
### Case 300: [Combat anime au sabre avec images d’impact](https://x.com/camperaigg/status/2117717189059026969) (par [@camperaigg](https://x.com/camperaigg))

**Synchronisez l’action des personnages, les éclairs d’impact, le son et les silences volontaires.**

Le créateur annonce 66 minutes de programmation pour un combat de silhouettes de 46 secondes, avec des capes évoquant du tissu, des armes contrastées ainsi que de la musique et des effets synthétisés. Ses notes décrivent la correction d’une attaque inversée, des traînées visuelles et de la position du titre.

```
Make me a video of 2 stickman fighting, anime style.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/c36c188396aac371a64e31a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b670f06d376211c60bf894.jpg" alt="Combat anime au sabre avec images d’impact" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-301"></a>
### Case 301: [Cerf courant comparé entre quatre modèles](https://x.com/fawnunwrap/status/2117702487755100543) (par [@fawnunwrap](https://x.com/fawnunwrap))

**Comparez les mouvements des membres et la forme animale en gardant visible le montage complet d’une même tâche.**

FawnBench présente un cerf courant dans quatre panneaux étiquetés comme un essai attribué à Fable 5.5, Gemini 4 Argon, GPT-6 Astra et Opus 5.5. Les images constituent une comparaison visuelle et non un résultat chiffré de performance mesurée.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3add4d9e0752d0467cbe6065.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/eea598747047797148e19c4e.jpg" alt="Cerf courant comparé entre quatre modèles" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-302"></a>
### Case 302: [Un robot traverse une ville inondée](https://x.com/0xMovez/status/2117700681867903169) (par [@0xMovez](https://x.com/0xMovez))

**Examinez la continuité entre reflets, mouvements du personnage et changements de point de vue.**

Le créateur annonce une animation Three.js de 42 secondes avec des images rendues par code, du son synthétisé et un unique fichier HTML de rendu hors ligne. Les images suivent un robot dans une ville inondée et envahie par la végétation, jusqu’à une scène colorée d’eau libre.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f39e1807d1e80422c31530c6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/247f768636339f49d149c787.jpg" alt="Un robot traverse une ville inondée" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-303"></a>
### Case 303: [Une épée Blender et son film de présentation](https://x.com/camperaigg/status/2117694354685092255) (par [@camperaigg](https://x.com/camperaigg))

**Séparez la construction procédurale de l’objet de la passe ultérieure de caméra et de son.**

Le créateur indique avoir d’abord généré une épée avec un script Python, puis demandé une vidéo. La suite emploie un mouvement continu de caméra Blender, un éclairage forestier, une partition orchestrale synthétisée et un montage HyperFrames ; la durée totale annoncée est de 65 minutes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3c767f2038ef7d3960c956ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/525304dc7d4016ac33b3d4f8.jpg" alt="Une épée Blender et son film de présentation" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-304"></a>
### Case 304: [Animation du village pixelisé Lantern Isle](https://x.com/abhinavflac/status/2117693193429139965) (par [@abhinavflac](https://x.com/abhinavflac))

**Examinez les activités locales et les transitions jour-nuit dans un environnement animé dense.**

Le créateur partage un village insulaire dessiné par code, avec des habitants, des bateaux, des cascades, des lanternes et de la musique. L’enregistrement alterne entre activités du village en gros plan, vues larges de l’île et séquence nocturne aux lanternes lumineuses.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e91f1eabab743730dd815c98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b7d2e578739d25596db1164f.jpg" alt="Animation du village pixelisé Lantern Isle" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-305"></a>
### Case 305: [Démo Pause de montage de vidéos de jeu](https://x.com/pausevfx/status/2117676887665447206) (par [@pausevfx](https://x.com/pausevfx))

**Examinez un workflow de montage allant des images brutes aux sous-titres, puis à une timeline éditable.**

Pause présente ce workflow sous l’étiquette Fable 5.5 pour le montage vidéo. La démonstration sélectionne des moments de jeu, recadre une facecam, ajoute des sous-titres et du son, puis ouvre une séquence éditable dans Premiere.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0faaeecdaa02683f81e67f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae2d32876804bf286f11dc6c.jpg" alt="Démo Pause de montage de vidéos de jeu" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-306"></a>
### Case 306: [Un pélican à vélo le long du littoral](https://x.com/pankajkumar_dev/status/2117301455665439210) (par [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Examinez la géométrie fine et l’animation depuis des vues de caméra proches et larges.**

Le créateur partage un pélican sur un grand-bi au bord de la mer. L’enregistrement inspecte les plumes, les pédales et la géométrie des roues avant de revenir à des vues plus larges du front de mer pavé.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/66c3c44bcefa684522f95b96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8575912e8f20f48439aea683.jpg" alt="Un pélican à vélo le long du littoral" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="acknowledge"></a>
## 🙏 Remerciements

Ce dépôt a été inspiré par les créateurs, développeurs, équipes de benchmark et communautés qui ont partagé publiquement de vrais cas d'utilisation de Claude Fable 5.

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@hakmgpt](https://x.com/hakmgpt), [@camperaigg](https://x.com/camperaigg), [@lightreelai](https://x.com/lightreelai), [@0xMovez](https://x.com/0xMovez), [@shmidtqq](https://x.com/shmidtqq), [@flxrnc](https://x.com/flxrnc), [@seeconvm](https://x.com/seeconvm), [@BubbleBrain](https://x.com/BubbleBrain), [@xbquan](https://x.com/xbquan), [@pipeline_os](https://x.com/pipeline_os), [@fawnunwrap](https://x.com/fawnunwrap), [@pausevfx](https://x.com/pausevfx), [@AnikaCodes](https://x.com/AnikaCodes), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@cfenghub](https://x.com/cfenghub), [@shneural](https://x.com/shneural)

*Nous ne pouvons pas garantir que chaque cas soit attribué au créateur original. Si quelque chose doit être corrigé, veuillez nous contacter et nous le mettrons à jour.*

Si vous avez d'autres cas d'utilisation intéressants à partager, n'hésitez pas à ouvrir une issue ou une pull request et à aider à étendre la bibliothèque de cas d'utilisation Evolink.


[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
