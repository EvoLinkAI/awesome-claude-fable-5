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
## 🍌 Introdução

Bem-vindo ao repositório de casos de uso de alto sinal do Claude Fable 5.

**Coletamos casos de uso reais, tutoriais, integrações e avaliações do Claude Fable 5, selecionados a partir de demos públicas e comunidades de criadores.**

Este README-fonte em inglês foca em casos de alto sinal com fluxos de trabalho concretos, prompts, demos, integrações, evidências de benchmark ou limites práticos.

A maioria dos casos é selecionada a partir de publicações no X/Twitter e demos públicas. Cada título de caso aponta para a fonte original, e cada handle de autor aponta para o perfil do criador.

Experimente no Evolink: [Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

<a id="-overview"></a>
## 📊 Visão Geral

- **88 casos originais de Fable 5 e 218 casos da comunidade; 306 casos no total.**
- Cobre agentes de codificação, automação de longa duração, jogos, design visual, simulações 3D, trabalho de conhecimento, tutoriais, integrações de API, benchmarks, preços e limitações de lançamento.
- Cada caso inclui a fonte original, atribuição ao criador, uma conclusão concisa, tipo de evidência e data de publicação.
- Use este repositório para encontrar fluxos de trabalho práticos, comparar pontos fortes e limites, descobrir prompts reproduzíveis e acompanhar exemplos de integração.

> [!NOTE]
> A coleção favorece evidências concretas em vez de hype: prompts reproduzíveis, demos entregues, métodos de benchmark, notas de integração, dados de custo e ressalvas claramente declaradas.

<a id="-quick-api-access"></a>
## ⚡ Acesso rápido à API

Use Claude Fable 5 pela API Messages compatível com Evolink. Obtenha um token de API em [Evolink](https://evolink.ai/login?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5) e substitua `<token>` pelo seu token.

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

| Seção | Casos |
|---|---|
| [💻 Codificação e Geração de Código](#coding-and-code-generation) | Case 1-6 |
| [🤖 Agentes e Automação de Longa Duração](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 Jogos e Demos Interativas](#games-and-interactive-demos) | Case 9-12 |
| [🎨 Visual, Design, Vídeo e 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 Documentos, Trabalho de Conhecimento e Pesquisa](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 Tutoriais, Cursos e Recursos de Prompt](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 Plataforma, API e Integração de Ferramentas](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 Avaliações, Comparações e Limites](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | Créditos e política de correção |

### [💻 Codificação e Geração de Código](#coding-and-code-generation)

| Case | O que mostra | Tipo |
|---|---|---|
| [Fluxo de Trabalho Multiestágio no Cursor](#case-1) | Use o Fable 5 como a etapa de planejamento, revisão e crítica dentro de um fluxo de trabalho multi-modelo no Cursor; depois devolva a implementação e a revisão para modelos mais baratos ou especializados. | Avaliação |
| [Recriando o GitHub a partir de uma Captura de Tela](#case-2) | Cole uma captura de tela de produto em uma ferramenta de codificação agêntica e peça ao Fable 5 para recriar a interface com funcionalidade real. | Demo |
| [Simulação de Buraco Negro com Um Prompt](#case-3) | Dê ao Fable 5 um único prompt detalhado de creative coding e peça que ele produza uma visualização física autocontida em Three.js. | Tutorial |
| [Web OS Estilo macOS em Uma Tentativa](#case-4) | Peça ao Fable 5 um web OS completo em arquivo único e deixe-o construir o shell de UI, apps, interações, áudio e comportamento de jogo embutido em uma passada. | Tutorial |
| [Construindo o Spawn 5.0 com 1.687 Prompts](#case-5) | Use o Fable 5 como parceiro de engenharia em sessões longas ao longo de muitos prompts, com o humano migrando de arquitetura para julgamento da qualidade da saída. | Tutorial |
| [Revisão de Pull Request Grande com Achados](#case-6) | Aponte o Fable 5 para um pull request grande e peça que ele revise correção, falsos positivos, bugs reais e problemas de polimento. | Demo |

### [🤖 Agentes e Automação de Longa Duração](#agents-and-long-running-automation)

| Case | O que mostra | Tipo |
|---|---|---|
| [Revisão de Fluxo de Trabalho Relay de Longo Horizonte](#case-7) | Use o Fable 5 para trabalhos ambiciosos de longo horizonte: reconstruções de site, pipelines programáticos de conteúdo, correspondência de voz, revisão de segurança e verificações finais de qualidade. | Avaliação |
| [Diagnosticando uma Falha de Infraestrutura e Abrindo um PR de Correção](#case-8) | Dê ao Fable 5 acesso a pistas de infra, como logs, erros de banco de dados e digests de imagem; depois peça que ele diagnostique a indisponibilidade e prepare a correção. | Avaliação |

### [🎮 Jogos e Demos Interativas](#games-and-interactive-demos)

| Case | O que mostra | Tipo |
|---|---|---|
| [Dino Runner com Rastreamento de Dedo](#case-9) | Peça ao Fable 5 para construir um jogo de navegador que usa rastreamento de dedo como mecânica de entrada. | Demo |
| [Construção de Jogo de Corrida com Duas Frases](#case-10) | Dê ao Fable 5 um prompt de jogo muito curto e deixe-o gerar mapas, modos, música, UI e assets de jogo em uma execução. | Tutorial |
| [Minecraft de Terminal Instalável em Rust](#case-11) | Rode o Fable 5 por meio de um harness de codificação no terminal e peça que ele construa um jogo de terminal instalável em Rust. | Demo |
| [Clone de Minecraft com Tempo e Custo](#case-12) | Use um prompt para pedir ao Fable 5 um clone jogável no estilo Minecraft; depois avalie tempo, custo, volume de código e cobertura de features. | Tutorial |

### [🎨 Visual, Design, Vídeo e 3D](#visual-design-video-and-3d)

| Case | O que mostra | Tipo |
|---|---|---|
| [Prompt Completo e Reproduzível de Email Ecommerce](#case-13) | Dê ao Fable 5 um briefing criativo completo para um mockup de email de marca, incluindo seções exatas, requisitos de produto, direção visual e restrições. | Tutorial |
| [Benchmark de Relojoeiro com Âncora Suíça](#case-14) | Use o Fable 5 em um benchmark de simulação mecânica e peça que ele implemente, verifique e itere sobre a correção física. | Avaliação |
| [Cena do Apartamento de Friends em Three.js](#case-15) | Peça ao Fable 5 para transformar uma planta baixa e uma referência de cena em um ambiente navegável em Three.js. | Avaliação |
| [Simulação do Sistema Solar com Prompt e URL](#case-16) | Use o Fable 5 para construir uma simulação astronômica a partir de princípios físicos, iterando até que a simulação e a saída pública estejam prontas. | Tutorial |

### [📚 Documentos, Trabalho de Conhecimento e Pesquisa](#documents-knowledge-work-and-research)

| Case | O que mostra | Tipo |
|---|---|---|
| [Evidências de Fluxo de Trabalho da Stripe e Científico](#case-17) | Use isto como evidência para afirmações de migração empresarial e fluxo de trabalho científico, não como um prompt para copiar e colar. | Avaliação |
| [Memorando de Política e Fluxos de Trabalho com Controle de Alterações](#case-18) | Use o Fable 5 para trabalho documental qualitativo longo: controle de alterações, triagem de comentários e edições orientadas por transcrição. | Tutorial |
| [Prompt e Saída de Pesquisa Profunda](#case-19) | Faça ao Fable 5 uma pergunta em estilo de pesquisa e avalie se ele consegue produzir uma resposta longa, estruturada e historicamente fundamentada. | Demo |

### [🧭 Tutoriais, Cursos e Recursos de Prompt](#tutorials-courses-and-prompt-resources)

| Case | O que mostra | Tipo |
|---|---|---|
| [Como o Fable 5 Muda Fluxos de Trabalho no Claude Code](#case-20) | Use o Fable 5 definindo direção, contexto, metas e critérios de verificação em vez de microgerenciar cada etapa. | Demo |
| [Revisão de Um Bilhão de Tokens e Estratégia de Roteamento](#case-21) | Use o Fable 5 para planejamento e revisão frontier, depois roteie implementação de alto volume para modelos mais baratos. | Tutorial |
| [Prompt Defensivo de Endurecimento de Dispositivos](#case-22) | Rode um prompt defensivo passo a passo de hardening em que o Fable 5 inventaria dispositivos, dá verificações exatas e espera confirmação. | Tutorial |
| [Prompt de Meta para Auditoria de Design de Site Completo](#case-23) | Use `/goal` para fazer o Fable 5 iniciar um site, capturar telas de páginas, auditar UX, escrever um relatório e corrigir pequenos problemas seguros. | Tutorial |
| [Divisão de Fluxo de Trabalho Criativo Longo](#case-24) | Use o Fable 5 para projetar formatos estáveis e exemplos; depois entregue essa estrutura a outro sistema de geração para saída específica do domínio. | Tutorial |
| [Guia para Iniciantes no Uso do Fable 5](#case-25) | Use o Fable 5 com prompts orientados a metas, loops de verificação e configurações de esforço em vez de pequenas instruções passo a passo. | Avaliação |
| [Prompt de Auditoria de Repositório para Copiar e Colar](#case-26) | Cole o prompt de auditoria de repositório no Fable 5 e peça descoberta baseada em arquivos, achados, estratégia e um plano de tarefas por marcos. | Tutorial |
| [Estratégia de Uso em Janela Limitada](#case-27) | Gaste o uso do Fable 5 em auditoria, arquitetura e planejamento enquanto a janela de acesso é favorável; depois use modelos mais baratos para execução. | Tutorial |
| [Usando Goals e Workflows no Claude Code](#case-28) | Use o Fable 5 como parceiro de pensamento antes da implementação; depois combine `/goal` e workflows para executar e verificar o plano. | Tutorial |

### [🔌 Plataforma, API e Integração de Ferramentas](#platform-api-and-tool-integration)

| Case | O que mostra | Tipo |
|---|---|---|
| [Configuração de Integração do Agente Hermes](#case-29) | Configure o Hermes para usar `anthropic/claude-fable-5` em execuções complexas de `/goal` e tarefas longas com cache. | Tutorial |
| [Capacidades, Preços e Notas de Assinatura](#case-30) | Use este caso para entender quando o Fable 5 está disponível, quanto custa e quais domínios protegidos podem cair para outro modelo. | Tutorial |
| [Resumo de Lançamento, Acesso, Preços e Segurança](#case-31) | Use este resumo de lançamento para escolher rota de acesso, nome de modelo de API, janela de contexto, estratégia de cache e timing de assinatura. | Tutorial |
| [Estratégia de Redução de Custo Baseada em Advisor](#case-32) | Use o Fable 5 como advisor ou revisor em um fluxo com modelo mais barato quando a inteligência marginal vale o custo. | Integração |
| [Preços, Acesso e Guardrails de Segurança](#case-33) | Use este caso para entender acesso ao Fable 5, preços de API e comportamento de fallback de segurança antes de planejar workloads. | Integração |
| [Integração Swarms em Uma Linha](#case-34) | Defina o nome do modelo Swarms como `anthropic/claude-fable-5` e rode o Fable 5 pelo framework ou API Swarms. | Integração |

### [📏 Avaliações, Comparações e Limites](#evaluations-comparisons-and-limits)

| Case | O que mostra | Tipo |
|---|---|---|
| [Comparação de Custo e Qualidade entre Fable 5 e GPT-5.5](#case-35) | Compare Fable 5 e GPT-5.5 na mesma tarefa de codificação para julgar qualidade da saída, runtime e custo da ferramenta. | Avaliação |
| [Resultado do Benchmark AA-Omniscience](#case-36) | Use este caso de benchmark para avaliar o Fable 5 em precisão de conhecimento e comportamento de alucinação. | Avaliação |
| [Resultado do Artificial Analysis Intelligence Index](#case-37) | Use este caso para comparar o ranking geral de inteligência do Fable 5 contra outros modelos frontier. | Avaliação |
| [Benchmark GDPval-AA de Trabalho de Conhecimento Agêntico](#case-38) | Use este caso para avaliar o Fable 5 em trabalho de conhecimento agêntico do mundo real. | Avaliação |
| [Primeiras Impressões de Uma Semana e Mecânica de Preços](#case-39) | Use este caso de primeiras impressões para decidir onde o Fable 5 é mais forte, especialmente design de jogos e planejamento de sistemas. | Integração |
| [Comparação de Custo e Velocidade](#case-40) | Use esta comparação para decidir se o ganho de qualidade justifica custo mais alto e execuções longas mais lentas. | Avaliação |
| [Notas Práticas do Claude Code](#case-41) | Use este caso para avaliar o Fable 5 dentro do Claude Code, incluindo uso de ferramentas, personalidade e arestas restantes. | Demo |
| [Resultado de Benchmark de Escrita Criativa](#case-42) | Use este caso de benchmark para julgar a qualidade de escrita de ficção curta do Fable 5 e seu comportamento de recusa. | Avaliação |
| [Resumo de Lançamento com Múltiplos Benchmarks](#case-43) | Use este resumo de benchmark de lançamento para entender as pontuações principais mais relevantes para agentes de codificação e tarefas complexas. | Avaliação |
| [Comparação de Benchmark e Preços com GPT-5.5](#case-44) | Use esta comparação para avaliar o Fable 5 contra GPT-5.5 em preço e categorias de benchmark. | Avaliação |
| [Notas de Campo com Limitações Práticas](#case-45) | Use este relatório de campo para entender onde o Fable 5 parece significativamente melhor e onde ainda tem limites práticos. | Tutorial |
| [Comparação de Simulação Física](#case-46) | Rode prompts idênticos de simulação física contra Fable 5 e Opus 4.8 para comparar qualidade de saída, custo e velocidade. | Demo |
| [Experiência de Debug e Julgamento de Design](#case-47) | Use o Fable 5 para debug pedindo que ele meça, registre logs, verifique e corrija, em vez de simplesmente adivinhar. | Demo |
| [Prós e Contras Multidimensionais](#case-48) | Use este caso para entender pontos fortes e fracos práticos antes de transformar o Fable 5 em daily driver. | Demo |
| [Teste de Redação Jurídica de S-1](#case-49) | Use um prompt de redação de S-1 como teste de capacidade de agente jurídico e compare estrutura, formatação e comprimento. | Tutorial |
| [Detalhes de Benchmark em Saúde](#case-50) | Use esta nota de benchmark para avaliar o Fable 5 em tarefas relacionadas à saúde e identificar avaliações médicas difíceis ausentes. | Avaliação |
| [Avaliação de Parsing de Documentos no ParseBench](#case-51) | Use este caso para decidir se o Fable 5 é custo-efetivo para parsing de documentos versus sistemas especializados de OCR. | Avaliação |
| [Comparação SWE-Bench Pro e FrontierCode](#case-52) | Use este caso de benchmark para avaliar o Fable 5 em migrações, implementações complexas, sessões autônomas, testes e verificação visual. | Avaliação |
| [Revisão Qualitativa de Resolução de Problemas Longos](#case-53) | Use esta revisão qualitativa para entender por que o Fable 5 é adequado a tarefas mais longas e difíceis, embora ainda exija revisão em produção. | Avaliação |
| [Resultados de Fidelidade e Formatação no ParseBench](#case-54) | Use este resultado do ParseBench para julgar fidelidade documental e desempenho de formatação. | Avaliação |
| [Benchmarks, Preços, Acesso e Salvaguardas](#case-55) | Use este caso como checklist amplo para benchmarks, preços, acesso, salvaguardas e implicações estratégicas. | Avaliação |
| [Lista Oficial de Pontuações de Benchmark](#case-56) | Use esta lista de benchmarks para entender as pontuações oficiais do Fable 5 em tarefas de codificação, uso de computador e segurança. | Avaliação |
| [Metodologia do Benchmark APEX-SWE](#case-57) | Use este caso para avaliar o Fable 5 no APEX-SWE, especialmente trabalho de observabilidade e integração. | Avaliação |
| [Resultado de Matemática Formal no ProofBench](#case-58) | Use este caso para avaliar o Fable 5 em matemática formal contra sistemas especializados de prova de teoremas. | Tutorial |
| [Análise Preliminar do VirtueBench](#case-59) | Use este caso para inspecionar o comportamento de raciocínio moral do Fable 5 em categorias de virtude. | Avaliação |
| [Teste de Overfit de Segurança com Resposta Vazia na API](#case-60) | Use este caso para entender o risco de overfit de segurança no lançamento e comportamento de resposta vazia em testes de API. | Avaliação |
| [Guia de prompts Fable com verificação](#case-61) | Use este guia para substituir truques de prompts longos por objetivos, contexto, restrições, ferramentas e ciclos de verificação. | Tutorial |
| [Um jogo de plataforma em Istambul a partir de uma referência](#case-62) | Teste Fable 5 com uma folha de sprites de referência e uma instrução para convertê-la em um jogo de plataforma jogável. | Demo |
| [Um painel empresarial como cidade 3D](#case-63) | Use Fable 5 para transformar um processo empresarial em um conceito de painel com uma cidade 3D animada. | Demo |
| [Um jogo de buracos em Three.js de uma só vez](#case-64) | Use Fable 5 para criar de uma só vez um protótipo de jogo 3D para navegador em Three.js. | Demo |
| [Comparação de resultados no DeepSWE](#case-65) | Use esta nota sobre DeepSWE para comparar Fable 5 xHigh e GPT-5.5 xHigh em tarefas de engenharia de software. | Avaliação |
| [Comparar o custo de analisar um repositório](#case-66) | Use esta comparação de análises de repositório para avaliar o preço dos tokens em relação ao custo do retrabalho humano. | Avaliação |
| [Consumo de tokens de um jogo Super Mario](#case-67) | Use esta criação de jogo em uma execução para estimar a qualidade do resultado e o consumo de tokens de Fable 5. | Demo |
| [A configuração de troca de modelo no Claude Code](#case-68) | Conheça a configuração do Claude Code que troca de modelo quando uma mensagem para Fable 5 é sinalizada. | Integração |
| [Construir um simulador do Namma Metro](#case-69) | Use esta demonstração como exemplo breve de criação de um simulador de transporte público com Fable 5 por vibe coding. | Demo |
| [Dusk Drive com um único prompt](#case-70) | Avalie Fable 5 na prototipagem de um jogo de direção low-poly sem edições humanas a partir deste caso. | Demo |
| [A classificação APEX-Agents por Pass@1](#case-71) | Use este resultado do APEX-Agents para comparar Fable 5 Max em tarefas autônomas de várias etapas. | Avaliação |
| [Guia para selecionar modelos Claude](#case-72) | Use este guia de seleção para reservar Fable 5 aos trabalhos mais difíceis do Claude Code. | Tutorial |
| [O ciclo automatizado de agentes do HermesWorld](#case-73) | Estude um ciclo de Fable 5 que constrói, testa, joga e executa testes de fumaça por dias sem intervenção. | Integração |
| [Testar um relatório no estilo McKinsey](#case-74) | Use este prompt documental para avaliar a estrutura de um relatório de consultoria, os gráficos, a narrativa e a análise de riscos. | Tutorial |
| [Tornar as salvaguardas visíveis](#case-75) | Use esta nota oficial para entender a visibilidade das salvaguardas de Fable 5, os motivos de recusa da API e a troca para Opus. | Integração |
| [Corrigir a identificação de modelos no Claude Code](#case-76) | Use esta nota de versão do Claude Code para evitar problemas nos nomes de Fable 5 e na identificação do contexto. | Integração |
| [Três aplicações web no Claude Code](#case-77) | Examine Fable 5 dentro do Claude Code por meio de várias aplicações web geradas nesta demonstração para iniciantes. | Demo |
| [Rilable, um criador de aplicativos de código aberto](#case-78) | Estude Fable 5 em aplicativos iOS e web, sandboxes e custos de tokens de API com este criador de aplicativos aberto. | Integração |
| [Estreia no indice de agentes de codigo DeepSWE](#case-79) | Use o indice renovado da Artificial Analysis para comparar o Fable 5 em tarefas de codificacao agentica mais dificeis que evitam reciclar correcoes publicas do GitHub. | Evaluation |
| [DataEmpire: jogo de analitica web](#case-80) | Transforme analises brutas de site em um jogo rejogavel pedindo ao Fable 5 que mapeie visitantes e marcos para entidades do jogo. | Integration |
| [Sinal de tarefa de 20 horas no FrontierSWE](#case-81) | Use o FrontierSWE como evidencia de que o Fable 5 consegue permanecer produtivo em tarefas de engenharia muito longas, nao apenas em loops curtos de correção de bugs. | Evaluation |
| [Recordes de CUDA no KernelBench-Hard](#case-82) | Use o Fable 5 para geracao avancada de kernels CUDA quando voce precisa de otimizacao de baixo nivel, e nao apenas wrappers sobre bibliotecas existentes. | Evaluation |
| [Clone de landing page com Figma Capture](#case-83) | Capture uma pagina real de concorrente em camadas do Figma e deixe o Claude Code com Fable 5 reconstruir estrutura, copy e sistema de marca em vez de adivinhar a partir de screenshots. | Integration |
| [Clone de GTA 2 em duas horas](#case-84) | Combine a geracao de codigo do Fable 5 com ferramentas separadas de assets para construir rapidamente um jogo 3D jogavel sem programar manualmente toda a stack. | Tutorial |
| [Agente de triagem de logs do CloudWatch](#case-85) | Deixe um agente com Fable 5 processar contextos enormes de logs de servico, inferir a arquitetura e depois restringir falhas especificas. | Integration |
| [Previsor da Copa do Mundo em sandboxes](#case-86) | Coloque varios modelos frontier atras de sandboxes isolados e deixe que pesquisem noticias ao vivo, lesoes e contexto de cartoes amarelos para um app publico de previsao. | Integration |
| [Caso de custo por recusas no WolfBench](#case-87) | Trate o comportamento de recusa como uma variavel real de benchmark ao precificar execucoes autonomas longas com Fable 5. | Evaluation |
| [Monitor de corte de acesso a API](#case-88) | Monitore a disponibilidade com um script se o seu fluxo depender de acesso continuo a um modelo frontier que pode ser limitado ou retirado sem muito aviso. | Integration |



### [🆕 Fable 5.5: demonstrações da comunidade](#fable-5-5-community-demos)

| Caso | Tipo |
|---|---|
| [Uma animação de raposa com som gerada por código](#case-89) | Demo |
| [Uma animação a partir de uma proposta criativa aberta](#case-90) | Demo |
| [Um site animado para uma construtora](#case-91) | Demo |
| [Uma apresentação de carro com Three.js](#case-92) | Demo |
| [Uma demonstração de jogo de navegador no estilo Minecraft](#case-93) | Demo |
| [Um pelicano ciclista animado em Three.js](#case-94) | Demo |
| [Um pelicano de bicicleta em SVG com o prompt exato](#case-95) | Demo |
| [Uma amostra de animação de zebra galopando](#case-96) | Demo |
| [Um indicador TradingView com execução humana](#case-97) | Demo |
| [Um ponto vira uma curta história animada](#case-98) | Demo |
| [Superman em diferentes estilos artísticos](#case-99) | Demo |
| [O progresso humano em um filme animado com música](#case-100) | Demo |
| [Comparação de vídeos de lançamento com Opus](#case-101) | Evaluation |
| [Conectar visualmente uma letra e um acontecimento](#case-102) | Demo |
| [Um personagem voxel em um cenário flutuante](#case-103) | Demo |
| [Uma máquina de Rube Goldberg em 3D](#case-104) | Demo |
| [Uma interface de controle 3D com som e movimento](#case-105) | Demo |
| [Personagens de quadrinhos apresentados com JavaScript](#case-106) | Demo |
| [Updraft: mundos, chefes e classificação](#case-107) | Demo |
| [Dirigindo por um mapa de São Francisco](#case-108) | Demo |
| [Escrever prompts para uma cena de ação no Seedance](#case-109) | Demo |
| [Um vídeo explicativo para um colega de desktop](#case-110) | Demo |
| [Um prompt curto para uma animação de estilos variados](#case-111) | Demo |
| [Visualizar o problema dos três corpos](#case-112) | Demo |
| [Uma galeria de animações com vários estilos artísticos](#case-113) | Demo |
| [Companheiros robóticos e pelos procedurais](#case-114) | Demo |
| [Uma edição animada sobre matemática](#case-115) | Demo |
| [Um vídeo com a letra de Your Woman](#case-116) | Demo |
| [Redesenhar um clipe musical com JavaScript](#case-117) | Demo |
| [Uma animação sobre o futebol chinês](#case-118) | Demo |
| [Uma apresentação de retopologia de console portátil](#case-119) | Demo |
| [Minecraft encontra Pokémon](#case-120) | Demo |
| [Um vídeo explicando como um LLM é feito](#case-121) | Demo |
| [Uma edição de destaques sobre Altman](#case-122) | Demo |
| [O primeiro dos Trinta e Seis Estratagemas](#case-123) | Demo |
| [Modelagem, rigging e animação de jogos](#case-124) | Demo |
| [Um filme sem palavras sobre mortalidade infantil](#case-125) | Demo |
| [Uma animação SVG da glicólise ao etanol](#case-126) | Demo |
| [Dezesseis lançamentos simultâneos de Starship](#case-127) | Demo |
| [Um teste animado do pelicano de bicicleta](#case-128) | Demo |
| [Uma história dos próximos 150 anos](#case-129) | Demo |
| [Uma experiência independente de Humanity Walks](#case-130) | Demo |
| [O filme programado The Grader](#case-131) | Demo |
| [O curta de terror Reawakening](#case-132) | Demo |
| [Um vídeo de 25 segundos sobre melhoria própria](#case-133) | Demo |
| [Uma cena de castelo com comentários de custo](#case-134) | Evaluation |
| [Um anúncio de lançamento de marca em 40 segundos](#case-135) | Demo |
| [Uma recriação de Rocketball](#case-136) | Demo |
| [Uma comparação de pagodes em voxels](#case-137) | Evaluation |
| [Apresentação de um Switch 3 imaginário](#case-138) | Demo |
| [Landing pages antes e depois](#case-139) | Evaluation |
| [A perspectiva interior imaginada de uma IA](#case-140) | Demo |
| [Animação da letra de Go](#case-141) | Demo |
| [Um segundo portfólio animado de 15 segundos](#case-142) | Demo |
| [Revisão guiada da implementação de um agente](#case-143) | Tutorial |
| [A dança da mascote Claude](#case-144) | Demo |
| [As ilhas interativas das Sete Maravilhas](#case-145) | Demo |
| [Um clipe musical para Propellerheads](#case-146) | Demo |
| [Comparação de animações de Steamboat Willie](#case-147) | Evaluation |
| [Um filme inspirado em Sanxingdui](#case-148) | Demo |
| [Um Bugatti Chiron antes e depois](#case-149) | Evaluation |
| [O filme conceitual GRAIN](#case-150) | Demo |
| [A galeria de arte Human in Transit](#case-151) | Demo |
| [Um curta visual sobre a Rota da Seda](#case-152) | Demo |
| [Uma apresentação sobre quatro transformações](#case-153) | Demo |
| [Comparar o tom de conversas anteriores](#case-154) | Evaluation |
| [Um teste de fofura com um kakapo](#case-155) | Evaluation |
| [Spider-Man por dez épocas dos quadrinhos](#case-156) | Demo |
| [Um vídeo fictício de terror sobre os Illuminati](#case-157) | Demo |
| [Um filme programado de história da ciência nuclear](#case-158) | Demo |
| [Um vídeo explicativo sobre renda alta universal](#case-159) | Demo |
| [Uma explicação animada da disputa Altman–Amodei](#case-160) | Demo |
| [Um clipe musical com a mascote Claude](#case-161) | Demo |
| [Um zoom contínuo dos quarks ao universo](#case-162) | Demo |
| [Imaginar o mundo em 2076](#case-163) | Demo |
| [Cronologia dos edifícios de Lower Manhattan](#case-164) | Demo |
| [Uma animação sobre escrita em ossos oraculares](#case-165) | Demo |
| [Outra animação de personagens pela história da arte](#case-166) | Demo |
| [Uma obra audiovisual programada sobre Seikilos](#case-167) | Demo |
| [Comparação de animações de jatos](#case-168) | Evaluation |
| [Um filme de apresentação do modelo](#case-169) | Demo |
| [Um protótipo de cartas pós-apocalíptico](#case-170) | Demo |
| [A animação de escritório The Late Byte](#case-171) | Demo |
| [Animação de letras de Queens of the Stone Age](#case-172) | Demo |
| [Uma cena narrativa compartilhada de Three.js](#case-173) | Demo |
| [Moonwalk por cenários históricos](#case-174) | Demo |
| [Gráficos animados com prompt detalhado](#case-175) | Demo |
| [A interface de um negócio de locação](#case-176) | Demo |
| [Um filme criativo sobre AGI](#case-177) | Demo |
| [História da arte com uma trama de gato](#case-178) | Demo |
| [Um protótipo de combate e uma cena voxel](#case-179) | Demo |
| [Cronologia de memes da Internet](#case-180) | Demo |
| [Movimento de partículas a partir de uma linha](#case-181) | Demo |
| [A animação Kung-Fu Boy](#case-182) | Demo |
| [Um debate animado sobre o Estreito de Ormuz](#case-183) | Demo |
| [Uma experiência de estilo SVG com unicórnio](#case-184) | Demo |
| [Uma animação sazonal de Halloween](#case-185) | Demo |
| [Um bárbaro e uma capa com Blender CLI](#case-186) | Demo |
| [Um dia na vida de Claude](#case-187) | Demo |
| [A história humana em 3D](#case-188) | Demo |
| [Um reel rápido de motion design](#case-189) | Evaluation |
| [Uma criação 3D complexa e livre](#case-190) | Demo |
| [Uma luta animada de bonecos de palito](#case-191) | Demo |
| [Uma sequência de interface animada com um prompt](#case-192) | Demo |
| [Uma animação fictícia de SCP-8517](#case-193) | Demo |
| [Uma animação de outono em aquarela](#case-194) | Demo |
| [Uma cena de boneca procedural](#case-195) | Demo |
| [Um pelicano de bicicleta renderizado no navegador](#case-196) | Demo |
| [O universo observa a si mesmo](#case-197) | Demo |
| [Um teste independente de animação de jato](#case-198) | Demo |
| [Um primeiro reel de movimento livre](#case-199) | Demo |
| [Uma civilização renderizada com código](#case-200) | Demo |
| [Comparação de zoom do chip ao servidor](#case-201) | Evaluation |
| [Um projeto pessoal de animação de viagem lunar](#case-202) | Demo |
| [Comparação de cenas japonesas em voxels](#case-203) | Evaluation |
| [O curta audiovisual Steaming the Frontier](#case-204) | Demo |
| [Superman em vários estilos artísticos](#case-205) | Demo |
| [Um protótipo de luta de chefe estilo Cupcake](#case-206) | Demo |
| [Um veleiro com posições diferentes do sol](#case-207) | Demo |
| [Um vídeo de novidades de Paracortex e Pi](#case-208) | Demo |
| [Uma promoção do site Curio 2.0](#case-209) | Demo |
| [Uma história 3D imaginária da Hugging Face](#case-210) | Demo |
| [Claude para Chrome dentro do JS Paint](#case-211) | Demo |
| [Um pelicano de bicicleta em SVG estático](#case-212) | Demo |
| [BlockBench MCP com uma habilidade de Minecraft](#case-213) | Demo |
| [Dig Dug em um único arquivo HTML](#case-214) | Demo |
| [Um polvo mecânico em SVG](#case-215) | Demo |
| [Humanity Walks por estilos artísticos](#case-216) | Demo |
| [Uma cena livre de buraco negro](#case-217) | Demo |
| [Comparação de animações de águas-vivas aurorais](#case-218) | Evaluation |
| [Um SVG Nintendo Switch com encaixe e inicialização](#case-219) | Demo |
| [A cena 3D interativa The Loom](#case-220) | Demo |
| [Reels de motion design com o mesmo prompt](#case-221) | Evaluation |
| [Um cenário mais limpo com menos profundidade](#case-222) | Evaluation |
| [Resultados mistos de uma cena japonesa](#case-223) | Evaluation |
| [Comparações de controles SVG](#case-224) | Evaluation |
| [Uma cena de dispositivo industrial](#case-225) | Demo |
| [Reconstrução de criatura gigante com carapaça e brânquias](#case-226) | Demo |
| [Um controle GameCube com dois prompts](#case-227) | Demo |
| [Uma captura editada para um post no X](#case-228) | Demo |
| [Uma cena sakura voxel antes e depois](#case-229) | Evaluation |
| [O protótipo de interface têxtil SHADERKIN](#case-230) | Demo |
| [Uma animação compartilhada de interface com relógio dourado](#case-231) | Demo |
| [A narrativa Before There Was Anything](#case-232) | Demo |
| [Um vórtice compartilhado de partículas azuis](#case-233) | Demo |
| [Uma interface com vários painéis após duas revisões](#case-234) | Demo |
| [Animais empilhados em uma cena renderizada](#case-235) | Demo |
| [Quatro tentativas de RPG de mundo aberto comparadas](#case-236) | Evaluation |
| [Dois clipes de animação frontend comparados](#case-237) | Evaluation |
| [Um filme de robô coberto de musgo gerado com código](#case-238) | Demo |
| [Uma simulação de porto de contêineres revisitada](#case-239) | Demo |
| [Uma cena de pátio de aeroporto revisitada](#case-240) | Demo |
| [Um pelicano de bicicleta por mundos 3D abstratos](#case-241) | Demo |
| [Uma cena de veleiro histórico](#case-242) | Demo |
| [Comparações de ciclismo e marcha com Carbon](#case-243) | Evaluation |
| [Uma apresentação de garrafa de refrigerante](#case-244) | Demo |
| [Movimento de pelicanos comparado com Astra](#case-245) | Evaluation |
| [Um briefing de motion design para animações programadas](#case-246) | Tutorial |
| [Um retrato voxel a partir de fotografia](#case-247) | Demo |
| [Pelicanos voadores comparados com Opus](#case-248) | Evaluation |
| [A cena web de pelicano Morning Ride](#case-249) | Demo |
| [O mesmo prompt com estilos diferentes](#case-250) | Evaluation |
| [Uma composição com pelicano, bicicleta e cavalo](#case-251) | Demo |
| [Uma cena isométrica inspirada em tweet de referência](#case-252) | Demo |
| [Close-ups mecânicos da bicicleta de um pelicano](#case-253) | Demo |
| [Uma bicicleta andando sobre um pelicano](#case-254) | Demo |
| [Estilos SVG de pelicano comparados com Carbon](#case-255) | Evaluation |
| [Um pássaro azul de desenho animado na bicicleta](#case-256) | Demo |
| [Captura de pelicano pedalando em uma estrada florestal](#case-257) | Demo |
| [Combate de bonecos de palito comparado com Carbon](#case-258) | Evaluation |
| [Uma referência SVG de pelicano de testes iniciais](#case-259) | Demo |
| [Uma referência de pelicano em testes SVG entre modelos](#case-260) | Evaluation |
| [Detalhes de bicicletas SVG comparados com Carbon](#case-261) | Evaluation |
| [Um povoado em um cânion em 3D](#case-262) | Demo |
| [Detalhes de controles comparados com Opus](#case-263) | Evaluation |
| [Um fluxo semanal de auditoria SEO de sites](#case-264) | Integration |
| [Reutilizar recursos de Fable no motion design de Opus](#case-265) | Integration |
| [Um aplicativo de mandalas e formas geométricas](#case-266) | Demo |
| [Um ciclista de bicicleta com Three.js](#case-267) | Demo |
| [Registro da avaliação FrontierCS 2](#case-268) | Evaluation |
| [Comparação de animações de zebra entre três modelos](#case-269) | Evaluation |
| [Analisar a leitura de textos japoneses longos](#case-270) | Evaluation |
| [Um PowerPoint técnico guiado por exemplos](#case-271) | Evaluation |
| [Comparar a coerência musical](#case-272) | Evaluation |
| [Conclusão prematura e designs de qualidade inferior](#case-273) | Limit |
| [Uma arte de lula que causou desconforto](#case-274) | Limit |
| [Motion design com estética de planta técnica](#case-275) | Demo |
| [Aves e peixes em uma cena sakura voxel](#case-276) | Demo |
| [Um relato de falha na geração de personagens](#case-277) | Limit |
| [Um SVG de pelicano com notas de tempo e custo](#case-278) | Evaluation |
| [Programação remota no celular com enxames Claude Code](#case-279) | Integration |
| [A Via Láctea sobre um lago alpino](#case-280) | Demo |
| [Salto de baleia com água e som procedurais](#case-281) | Demo |
| [Movimento de zebras comparado entre quatro modelos](#case-282) | Evaluation |
| [Busca de criadores em linguagem natural no Lightreel](#case-283) | Demo |
| [Um navio voador sobre um mar de nuvens](#case-284) | Demo |
| [Coração mecânico com corte animado](#case-285) | Demo |
| [Jardim de pagode voxel flutuante e explorável](#case-286) | Demo |
| [Uma aventura oceânica feita por oito equipes](#case-287) | Demo |
| [Apresentação interativa de um hipercarro](#case-288) | Demo |
| [Nascimento de uma árvore da vida](#case-289) | Demo |
| [Castelo ambulante com maquinaria interna funcional](#case-290) | Demo |
| [Uma torrada e um besouro mecânico](#case-291) | Demo |
| [Um faroleiro em uma tempestade](#case-292) | Demo |
| [Uma criatura marinha em uma cidade costeira](#case-293) | Demo |
| [Corridas no tapete comparadas entre três modelos](#case-294) | Evaluation |
| [Um caminhão se transforma em robô](#case-295) | Demo |
| [Quadros de animação do Fable e do Hunyuan](#case-296) | Evaluation |
| [Uma animação sobre compartilhar luz](#case-297) | Demo |
| [Uma aldeia voxel entre montanhas](#case-298) | Demo |
| [Composição de pelicano e elefante com quatro modelos](#case-299) | Evaluation |
| [Luta anime de espadas com quadros de impacto](#case-300) | Demo |
| [Cervo correndo comparado entre quatro modelos](#case-301) | Evaluation |
| [Um robô atravessa uma cidade inundada](#case-302) | Demo |
| [Uma espada no Blender e seu filme de apresentação](#case-303) | Demo |
| [Animação da aldeia pixelada Lantern Isle](#case-304) | Demo |
| [Demonstração de edição de vídeos de jogos no Pause](#case-305) | Demo |
| [Um pelicano de bicicleta à beira-mar](#case-306) | Demo |

<a id="coding-and-code-generation"></a>
## 💻 Codificação e Geração de Código

<a id="case-1"></a>
### Case 1: [Fluxo de Trabalho Multiestágio no Cursor](https://x.com/AlicanKiraz0/status/2064487347605918180) (por [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Use o Fable 5 como a etapa de planejamento, revisão e crítica dentro de um fluxo de trabalho multi-modelo no Cursor; depois devolva a implementação e a revisão para modelos mais baratos ou especializados.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8b1352e20cff54688c97f17c.png" alt="Fluxo de Trabalho Multiestágio no Cursor" width="760">

Se olharmos a pontuação final entre Fable 5 e GPT 5.5, a diferença é muito pequena. Minha recomendação humilde de uso é esta: em plataformas de IDE como o Cursor, que dão suporte a modelos híbridos, use um fluxo em estágios.

Fase 1: para revisão de código e a primeira fase de inspeção do projeto, enquanto aquece o contexto, use um entre GPT 5.5 High, Minimax M3, Kimi K2.6 ou Composer 2.5.

Fase 2: para preparar o plano do projeto, use GPT 5.5 Very High ou Opus 4.8.

Fase 3: para analisar o plano do projeto, use Fable 5; deixe-o identificar as partes falhas do plano. Para revisões, use GPT 5.5 Very High.

Fase 4: para implementar o plano, use Minimax M3, Deepseek v4 Max, Composer 2.5 ou Sonnet 4.6.

Fase 5: para a revisão final e para verificar se a implementação seguiu o plano, use GPT 5.5 High.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-2"></a>
### Case 2: [Recriando o GitHub a partir de uma Captura de Tela](https://x.com/coldopn/status/2064435234465087638) (por [@coldopn](https://x.com/coldopn))

**Cole uma captura de tela de produto em uma ferramenta de codificação agêntica e peça ao Fable 5 para recriar a interface com funcionalidade real.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/14123609b06071f3b9527bee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f4df4f42ce047201d9a096a6.jpg" alt="Recriando o GitHub a partir de uma Captura de Tela" width="760"><br>▶ Assistir ao vídeo</a>

🚨 O Anthropic Fable 5 acabou de replicar o GITHUB a partir de uma CAPTURA DE TELA!!

Tudo que fiz foi colar uma captura de tela da UI do GitHub no Kilo Code e pedir para ele recriar o GitHub com funcionalidade real.

Ele programou por 10 minutos e gastou $4.07.

O resultado foi uma réplica funcional do GitHub: https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---
<a id="case-3"></a>
### Case 3: [Simulação de Buraco Negro com Um Prompt](https://x.com/deveshcodes_/status/2064437742189379745) (por [@deveshcodes_](https://x.com/deveshcodes_))

**Dê ao Fable 5 um único prompt detalhado de creative coding e peça que ele produza uma visualização física autocontida em Three.js.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9bd45e74c64ceb3639600805.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ce5f3ea8ba270f89d60523cc.jpg" alt="Simulação de Buraco Negro com Um Prompt" width="760"><br>▶ Assistir ao vídeo</a>

@claudeai fez em uma tentativa uma simulação em tempo real de lente gravitacional de buraco negro em Three.js com Claude Fable 5.

Ela incluía lente gravitacional, disco de acreção com reforço doppler, esfera de fótons, aberração cromática e campo estelar procedural.

O resultado: 60fps, arquivo HTML único, um prompt.

A nova linha de base é absurda 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---
<a id="case-4"></a>
### Case 4: [Web OS Estilo macOS em Uma Tentativa](https://x.com/intheworldofai/status/2064421915347812672) (por [@intheworldofai](https://x.com/intheworldofai))

**Peça ao Fable 5 um web OS completo em arquivo único e deixe-o construir o shell de UI, apps, interações, áudio e comportamento de jogo embutido em uma passada.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a66f34402d04f708819fa575.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/81946293919c84d4cafff841.jpg" alt="Web OS Estilo macOS em Uma Tentativa" width="760"><br>▶ Assistir ao vídeo</a>

🚨 O Claude Fable 5 acabou de construir um web OS completo no estilo macOS em uma tentativa e foi além da maioria dos modelos.

Arquivo HTML único, CSS + JS embutidos.

A partir de um prompt, ele construiu:

- barra de menu + dock do macOS
- janelas de app arrastáveis e redimensionáveis
- explorador de arquivos funcional
- terminal funcional + mockup de navegador
- ícones SVG de desktop + notificações
- app de configurações, temas e tela de boot
- player de som totalmente funcional, com síntese real e sem arquivos externos
- clone jogável de Minecraft dentro do desktop

Tudo gerado em uma passada, quase sem correções.

O player de som funcional mais o clone real de Minecraft é algo que ainda não vi outros modelos conseguirem fazer. A geração de frontend/UI do Fable 5 está ficando ridícula.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-5"></a>
### Case 5: [Construindo o Spawn 5.0 com 1.687 Prompts](https://x.com/jsnnsa/status/2064420561078693941) (por [@jsnnsa](https://x.com/jsnnsa))

**Use o Fable 5 como parceiro de engenharia em sessões longas ao longo de muitos prompts, com o humano migrando de arquitetura para julgamento da qualidade da saída.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86834f15f352ec8625cce187.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b4077e43a1342d8567fa423f.jpg" alt="Construindo o Spawn 5.0 com 1.687 Prompts" width="760"><br>▶ Assistir ao vídeo</a>

claude fable 5 está no ar.

spawn 5.0 foi construído com ele:

- 1.687 prompts
- 102 sessões
- Meu trabalho mudou de arquitetura para julgamento de gosto

O que construímos, cada item dos quais teria levado pelo menos um mês com uma equipe inteira no Opus:

- Um motor físico do zero, Mantle, que rivaliza com Rapier e pôde ser testado em um dia como thread paralela
- Iluminação froxel clusterizada: de 8 luzes para mais de 1.000 luzes totalmente dinâmicas
- GI difusa em tempo real no WebGPU, no seu telefone
- VFX de um milhão de partículas na GPU com uma arquitetura de shader além do que Unreal e Unity entregam
- Netcode em escala de MMO
- Um app nativo iOS alfa

Tudo levou cerca de uma semana. Tudo roda em mobile. A lista não inclui metade do que foi entregue; o changelog completo está na thread.

A parte que os benchmarks não vão mostrar: este modelo tem uma personalidade maravilhosa. Ele é genuinamente engraçado. Ri tanto que chorei várias vezes no meio de uma reescrita de física. A genialidade e o caráter não são recursos separados.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-6"></a>
### Case 6: [Revisão de Pull Request Grande com Achados](https://x.com/ryanrhughes/status/2064411147076534705) (por [@ryanrhughes](https://x.com/ryanrhughes))

**Aponte o Fable 5 para um pull request grande e peça que ele revise correção, falsos positivos, bugs reais e problemas de polimento.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c4f47540205a071b0144ad9d.png" alt="Revisão de Pull Request Grande com Achados" width="760">

Soltei o Fable 5 para revisar um único PR (74 arquivos / +3.705 / -1.246) para ver como ele se sairia. Ele rodou por 34 min, consumiu 42% da minha sessão de 5 horas, produziu 16 achados de “correção” e encontrou:

- 2 falsos positivos que pareciam assustadores
- 3 bugs reais de correção de auditoria
- ~5 problemas legítimos, mas pequenos, de UX/polimento
- um monte de opiniões de limpeza

Isso era perigoso demais para lançar?

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 Agentes e Automação de Longa Duração

<a id="case-7"></a>
### Case 7: [Revisão de Fluxo de Trabalho Relay de Longo Horizonte](https://x.com/JJEnglert/status/2064469635190170105) (por [@JJEnglert](https://x.com/JJEnglert))

**Use o Fable 5 para trabalhos ambiciosos de longo horizonte: reconstruções de site, pipelines programáticos de conteúdo, correspondência de voz, revisão de segurança e verificações finais de qualidade.**

A versão curta da minha análise do Claude Fable 5: gastei um bilhão de tokens testando o Claude Fable 5 e pareceu que eu tinha uma vantagem injusta.

Eu julgo pelo teste visual: coloco um modelo em trabalho real e observo. Ele me economiza horas ou me custa horas? Ele captura o que eu perdi? Parece um parceiro ou uma ferramenta que preciso supervisionar?

Este é o primeiro modelo em muito tempo que passou em todas as dimensões que importam, e não por pouco.

Construção: eu estava reconstruindo nosso site da Tenex. Era muito customizado e muito difícil. GPT 5.5 e Claude 4.8 não conseguiam resolver sozinhos. Mesmo com arquivos Figma como referência, eles ficavam em torno de 85-90%.

Então o Fable 5 olhou para tudo, disse que poderia fazer melhor, foi direto à fonte original do Webflow, baixou todos os assets e quase fez tudo em uma tentativa.

Depois pedi que ele construísse um segundo site, totalmente novo, com 80 páginas, do zero, ao longo de um fim de semana. É um trabalho pelo qual eu teria cobrado $50k como agência.

Ele também conectou uma fábrica programática completa de clipes:

- HeyGen
- ElevenLabs
- Cloudflare
- Um VPS

O pipeline encontra tópicos, escreve scripts, edita vídeo, adiciona música e publica em redes sociais. Ele rodou por longos períodos sozinho e até construiu para si um sistema de webhook para monitorar renders.

Escrita: ele replicou nosso documento de voz de marca quase identicamente e depois manteve essa voz ao longo de 80 páginas de features, estudos de caso e artigos, sem cair no padrão plano de IA.

Segurança: dois modelos frontier haviam trabalhado em um repositório grande e aprovado o código. O Fable 5 encontrou um bug sério e bem escondido na primeira passada e o corrigiu na hora.

O momento humano: fiz uma pergunta enquanto esperava um cron job. Ele respondeu e depois acrescentou por conta própria que eu tinha cerca de 10 minutos restantes e que me avisaria quando terminasse. Eu nunca perguntei sobre o temporizador.

A ressalva honesta: você sente o medidor mais do que em qualquer outro modelo. A Anthropic o chama de intensivo em tokens por design. Então rode-o como um relay: pense com o Fable 5, construa com um modelo mais barato, revise com o Fable 5.

O veredito: acesso a mais inteligência do que a pessoa ao seu lado é a vantagem. O Fable 5 é o primeiro modelo que torna isso real. Mesmo com tarifas frontier cheias, ele deu lucro.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-8"></a>
### Case 8: [Diagnosticando uma Falha de Infraestrutura e Abrindo um PR de Correção](https://x.com/ayushagarwal/status/2064422467557564862) (por [@ayushagarwal](https://x.com/ayushagarwal))

**Dê ao Fable 5 acesso a pistas de infra, como logs, erros de banco de dados e digests de imagem; depois peça que ele diagnostique a indisponibilidade e prepare a correção.**

claude fable 5 é bom demais!!!!

Ele acabou de diagnosticar uma indisponibilidade que eu nem conseguia descrever direito em uma infra paralela self-hosted.

Ele leu logs de pods, consultou logs de erro do Cloud SQL, comparou digests de imagem e descobriu que o Kubernetes estava rodando uma imagem cacheada de 3 meses contra um banco de dados recém-migrado.

Depois abriu o PR de correção.

Minutos, não horas. Sem busca na web. 🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 Jogos e Demos Interativas

<a id="case-9"></a>
### Case 9: [Dino Runner com Rastreamento de Dedo](https://x.com/ai_for_success/status/2064413182396108932) (por [@ai_for_success](https://x.com/ai_for_success))

**Peça ao Fable 5 para construir um jogo de navegador que usa rastreamento de dedo como mecânica de entrada.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/27e8d23ba659611cef811031.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7cddd38e3fccbf0cd7ea773c.jpg" alt="Dino Runner com Rastreamento de Dedo" width="760"><br>▶ Assistir ao vídeo</a>

Pedi ao Fable 5 para construir um jogo Dino runner com rastreamento de dedo.

Ele fez o jogo de finger runner em uma tentativa, em cerca de 11 a 12 minutos, consumiu por volta de 914K tokens e implementou tudo em apenas 629 linhas de código.

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---
<a id="case-10"></a>
### Case 10: [Construção de Jogo de Corrida com Duas Frases](https://x.com/kieradev/status/2064482704763085202) (por [@kieradev](https://x.com/kieradev))

**Dê ao Fable 5 um prompt de jogo muito curto e deixe-o gerar mapas, modos, música, UI e assets de jogo em uma execução.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/51cf3c98b709a3c29bd5fd7c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6e64887a30cba9b5c25ba262.jpg" alt="Construção de Jogo de Corrida com Duas Frases" width="760"><br>▶ Assistir ao vídeo</a>

Claude Fable 5, 40% do uso Max 5x.

Jogo completo tipo Mario Kart 64 a partir de um prompt de 2 frases.

O Fable 5 cuidou de toda a decoração, modelos de personagens, 4 mapas, música, todos os três modos de jogo e UI em uma única tentativa, em cerca de 15 minutos.

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---
<a id="case-11"></a>
### Case 11: [Minecraft de Terminal Instalável em Rust](https://x.com/vikvang1/status/2064500731848319303) (por [@vikvang1](https://x.com/vikvang1))

**Rode o Fable 5 por meio de um harness de codificação no terminal e peça que ele construa um jogo de terminal instalável em Rust.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73feec38228181b8d57d8300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1f6cd3bd68e1a14443c7734f.jpg" alt="Minecraft de Terminal Instalável em Rust" width="760"><br>▶ Assistir ao vídeo</a>

Deixei o Claude Fable 5 com o harness do Warp cozinhar por uma hora.

Ele fez uma versão TUI de Minecraft que renderiza diretamente no seu terminal, construída inteiramente em Rust.

Comando de instalação: cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---
<a id="case-12"></a>
### Case 12: [Clone de Minecraft com Tempo e Custo](https://x.com/ydamitcodes/status/2064536076518363353) (por [@ydamitcodes](https://x.com/ydamitcodes))

**Use um prompt para pedir ao Fable 5 um clone jogável no estilo Minecraft; depois avalie tempo, custo, volume de código e cobertura de features.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c977ed7e710678ea6dc0495d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c0189f7f40d1040824902c11.jpg" alt="Clone de Minecraft com Tempo e Custo" width="760"><br>▶ Assistir ao vídeo</a>

@claudeai Fable 5 construiu para mim um clone de Minecraft em 37 minutos.

Um prompt. ~3K linhas de código. $12 em custos de API.

Incluía biomas, cavernas, minérios, dia/noite, mobs, tudo.

Minecraft levou 2 anos para Notch.

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 Visual, Design, Vídeo e 3D

<a id="case-13"></a>
### Case 13: [Prompt Completo e Reproduzível de Email Ecommerce](https://x.com/ecomchasedimond/status/2064454139225297091) (por [@ecomchasedimond](https://x.com/ecomchasedimond))

**Dê ao Fable 5 um briefing criativo completo para um mockup de email de marca, incluindo seções exatas, requisitos de produto, direção visual e restrições.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ea7d74eecf453ae6ab43c269.jpg" alt="Prompt Completo e Reproduzível de Email Ecommerce" width="760">

Claude Fable 5 fez isto com um único prompt e sem edições.

Aqui está o prompt completo que usei:

Crie um mockup de email ecommerce vertical, alto e em comprimento completo para a MVMT, uma marca moderna de relógios e acessórios para millennials.

Desenhe um email DTC premium altamente realista, com sensação elegante, polida, minimalista, levemente masculina e editorial. A imagem final deve parecer uma captura de tela de email ecommerce real feita por designer, não um pôster, não uma landing page e não um template genérico.

Vibe da marca: moderna, California-cool, jovem, confiante, limpa, aspiracional, estilosa e elevada. O design deve parecer próximo do luxo, mas ainda acessível.

Destaque estes produtos:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Estilo visual:

- design ecommerce premium limpo
- layout editorial refinado
- fotografia de produto realista
- imagens lifestyle sutis
- hierarquia forte
- tipografia sans-serif nítida
- espaçamento generoso
- sombras sutis
- paleta de cores moderna e contida

Paleta de cores: preto, branco, carvão, cinza quente, pedra, bege suave, tons de metal escovado e acentos discretos e dessaturados. Mantenha a paleta neutra e premium.

Direção criativa importante: isto deve parecer uma campanha de email polida de uma marca de relógios com forte bom gosto de design. Priorize realismo, elegância e clareza. Faça parecer algo que a MVMT poderia realmente enviar.

Construa o email nesta ordem:

1. Barra promocional superior: uma barra fina preta ou carvão escuro atravessando o topo, com texto pequeno em caixa alta: “FREE SHIPPING OVER $75 + EASY RETURNS”.

2. Cabeçalho: um cabeçalho branco e limpo com o wordmark/logo da MVMT à esquerda e links mínimos de navegação à direita ou centralizados: WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS.

3. Seção hero: uma seção hero premium com forte equilíbrio visual.

Use um headline em negrito: “BUILT TO GET NOTICED”.

Inclua um texto curto de apoio sobre relógios modernos e acessórios projetados para elevar o estilo cotidiano.

Adicione um botão CTA escuro e arredondado: “SHOP WATCHES”.

A imagem hero deve incluir:

- uma imagem dominante de relógio premium
- imagens lifestyle de luxo sutis
- um modelo masculino estiloso ou uma cena lifestyle masculina fashion-forward
- iluminação moderna e composição limpa

4. Seção de coleção em destaque: adicione um headline centralizado: “THREE WAYS TO WEAR MVMT”. Abaixo, mostre três cards de produto ou blocos de imagem limpos com:

- Mulholland
- Odyssey II Automatic
- Cali Diver

Cada bloco deve incluir:

- imagem do produto
- nome do produto
- descrição curta de uma ou duas linhas

Mantenha esta seção simétrica, polida e premium.

5. Banner de acessórios: adicione uma seção split refinada intitulada “FINISH THE LOOK”. Destaque Signature Watch Bands. Mostre imagens premium em close-up de pulseiras de relógio ou pulseiras intercambiáveis. Inclua texto curto de apoio e um botão CTA escuro: “SHOP ACCESSORIES”.

6. Tiles promocionais editoriais: adicione dois tiles promocionais lado a lado, com design guiado por imagem.

Headline do tile um: “FOR DAILY WEAR”.

Headline do tile dois: “FOR STATEMENT DAYS”.

Cada tile deve ter texto curto e um CTA pequeno: “SHOP NOW”.

Esses tiles devem parecer momentos editoriais de marca, não caixas genéricas de promoção.

7. Linha comprável: adicione uma seção intitulada “IN ROTATION NOW”. Mostre uma linha ou grid limpo de 4 itens com:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Cada item deve incluir:

- imagem isolada do produto
- nome do produto
- pequeno link ou botão “SHOP”

8. Assinatura da marca: adicione um bloco de mensagem centralizado com o headline: “DESIGNED TO MOVE WITH YOU”. Inclua uma linha curta sobre relógios, óculos e acessórios cuidadosamente criados para a vida cotidiana.

9. Rodapé: crie um rodapé de marca realista preto ou carvão com:

- logo MVMT
- links de loja
- links da empresa
- links de suporte
- ícones sociais
- texto legal e de envio pequeno

Direção de tipografia: use tipografia sans-serif condensada em negrito ou moderna para headlines principais e sans-serif limpa para texto de corpo. Os headlines devem parecer nítidos, modernos e fashion-forward. O texto de corpo deve parecer realista e majoritariamente legível.

Direção de fotografia: use fotografia premium de produto com reflexos realistas, materiais polidos, sombras suaves e superfícies limpas. A fotografia lifestyle deve parecer elevada, moderna e orientada à moda.

Regras de composição:

- formato de email vertical alto
- separação clara de seções
- proporções realistas de email
- hierarquia forte
- texto majoritariamente legível
- espaçamento premium
- alinhamento intencional
- mistura equilibrada de imagens de produto e lifestyle

Evite:

- estilo de colagem bagunçada
- estética playful de scrapbook
- design colorido demais
- vibe de template barato
- imagens cartunescas
- layouts poluídos
- elementos de UI com aparência falsa
- composição estilo pôster
- caos promocional excessivo

Saída: um mockup de design de email ecommerce em comprimento completo, composto verticalmente e altamente realista para a MVMT, com sensação premium, limpa, polida, moderna, editorial e pronta para apresentação.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-14"></a>
### Case 14: [Benchmark de Relojoeiro com Âncora Suíça](https://x.com/quanghuynt14/status/2064509430650065278) (por [@quanghuynt14](https://x.com/quanghuynt14))

**Use o Fable 5 em um benchmark de simulação mecânica e peça que ele implemente, verifique e itere sobre a correção física.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd4ae25f7dcbb04ecbb2dea6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/473227e429d59c59afdbd529.jpg" alt="Benchmark de Relojoeiro com Âncora Suíça" width="760"><br>▶ Assistir ao vídeo</a>

Então dei ao Fable 5 o benchmark de relojoeiro: um movimento completo de âncora suíça em Three.js.

Relações de engrenagem reais (18.000 bph), escapamento funcional, espiral respirando — e os ponteiros mostram a hora real.

Ele verificou o próprio trabalho com visão, em loop, até terminar.

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---
<a id="case-15"></a>
### Case 15: [Cena do Apartamento de Friends em Three.js](https://x.com/scottstts/status/2064464351906673029) (por [@scottstts](https://x.com/scottstts))

**Peça ao Fable 5 para transformar uma planta baixa e uma referência de cena em um ambiente navegável em Three.js.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/04c08937fcecea5183759ade.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a14f69d92bfca4ace3f746c.jpg" alt="Cena do Apartamento de Friends em Three.js" width="760"><br>▶ Assistir ao vídeo</a>

Caramba!!!

Fable 5:

em @threejs, crie uma cena 3d navegável em pov de primeira pessoa do icônico apartamento da Monica do programa de tv Friends corretamente baseada nesta planta baixa, mantendo fidelidade ao visual e sensação originais, use iluminação quente

Isso é de longe O MELHOR que já vi neste teste!

Este html único me custou $12, mas o resultado é impressionante!

Type: Evaluation | Date: 2026-06-09

---
<a id="case-16"></a>
### Case 16: [Simulação do Sistema Solar com Prompt e URL](https://x.com/tetumemo/status/2064477582930989357) (por [@tetumemo](https://x.com/tetumemo))

**Use o Fable 5 para construir uma simulação astronômica a partir de princípios físicos, iterando até que a simulação e a saída pública estejam prontas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6da60b0762f926c4d4e7012d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9655305fbcbec6ac3b0a9c.jpg" alt="Simulação do Sistema Solar com Prompt e URL" width="760"><br>▶ Assistir ao vídeo</a>

Claude Fable 5 é intenso.

Como ele parece forte em simulações físicas, pedi:

'Construa uma simulação do sistema solar derivando o movimento orbital planetário a partir dos princípios básicos da física e usando isso para prever eclipses solares.'

Depois de algumas rodadas de ida e volta, isto foi concluído.

É incrivelmente divertido.

O prompt concluído e a URL pública estão linkados abaixo.

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 Documentos, Trabalho de Conhecimento e Pesquisa

<a id="case-17"></a>
### Case 17: [Evidências de Fluxo de Trabalho da Stripe e Científico](https://x.com/AndrewCurran_/status/2064413892378546418) (por [@AndrewCurran_](https://x.com/AndrewCurran_))

**Use isto como evidência para afirmações de migração empresarial e fluxo de trabalho científico, não como um prompt para copiar e colar.**

Citações do lançamento de hoje:

Usando Mythos 5, especialistas internos em design de proteínas aceleraram partes do processo de design de medicamentos em cerca de dez vezes.

Em um exemplo, Mythos 5, com ferramentas de design de proteínas e bioinformática, mas sem assistência humana, igualou ou superou operadores humanos qualificados.

Ele executou tarefas normalmente realizadas por um cientista: escolher sítios de ligação, selecionar e executar ferramentas de design de proteínas e se recuperar de falhas.

Durante testes iniciais, a Stripe relatou que o Fable 5 comprimiu meses de engenharia em dias. Em uma codebase Ruby de 50 milhões de linhas, o modelo realizou em um dia uma migração em toda a codebase que, de outra forma, teria levado mais de dois meses de trabalho manual de uma equipe inteira.

Mythos 5 também produziu consistentemente hipóteses científicas novas e convincentes.

Em comparações cegas head-to-head contra modelos da classe Opus, cientistas preferiram as hipóteses de biologia molecular do Mythos cerca de 80% das vezes e avançaram várias para avaliação experimental.

Uma hipótese do Mythos, um mecanismo novo para uma proteína de E. coli, foi corroborada em um estudo de um laboratório independente.

Mythos 5 conduziu pesquisa genômica inédita em mais de uma semana de trabalho amplamente autônomo.

Ele reuniu dados de célula única para milhões de células em 138 espécies animais e projetou e treinou um modelo customizado de machine learning para identificar células que exercem o mesmo papel em organismos distantes.

Com apenas input humano de alto nível, o modelo treinado superou um modelo recente publicado na Science, apesar de ser 100 vezes menor.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-18"></a>
### Case 18: [Memorando de Política e Fluxos de Trabalho com Controle de Alterações](https://x.com/manaltdan/status/2064414129440608427) (por [@manaltdan](https://x.com/manaltdan))

**Use o Fable 5 para trabalho documental qualitativo longo: controle de alterações, triagem de comentários e edições orientadas por transcrição.**

Fable 5 é o primeiro modelo que encontrei consistentemente útil para trabalho qualitativo de maior duração, como redigir análise de políticas.

Entre suas capacidades e ferramentas como Wispr Flow, estou começando a me sentir mais próximo do ganho de produtividade de que há muito tempo ouço programadores falarem.

Três casos de uso parecem muito melhores do que antes:

- Fazer o Claude ler integralmente um memorando de política longo e devolver alterações controladas: edições de fluidez, comentários questionando afirmações frágeis e fontes potenciais.
- Em Projects, capturar a tela de um grande conjunto de comentários e fazer o Claude recomendar se e como tratar cada um.
- Colar no Claude uma transcrição de reunião sobre um documento; depois fazer o Claude inserir como alterações controladas as edições discutidas na reunião e no Slack, com contexto adicionado em comentários.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-19"></a>
### Case 19: [Prompt e Saída de Pesquisa Profunda](https://x.com/naoyafujiwara/status/2064470780373811637) (por [@naoyafujiwara](https://x.com/naoyafujiwara))

**Faça ao Fable 5 uma pergunta em estilo de pesquisa e avalie se ele consegue produzir uma resposta longa, estruturada e historicamente fundamentada.**

Claude Fable 5 Max ficou disponível esta manhã, então eu testei. Ele parece muito profundo por baixo, enquanto a saída superficial é altamente polida.

Pergunta: Se os "30 anos perdidos" do Japão começaram exatamente 30 anos atrás a partir de agora, o que foram exatamente, por que aconteceram e como afetarão o mundo deste ano em diante?

Resposta: Tratar os 30 anos perdidos como começando não com o colapso convencional da bolha em 1991, mas exatamente 30 anos atrás, em 1996, chega à essência do problema.

Estatisticamente, o Japão realmente começou a "perder" naquele momento:

- A população em idade ativa atingiu o pico em 1995, com 87,16 milhões.
- 1996 foi o último ano em que os nascimentos permaneceram na faixa de 1,2 milhão.
- Salários e PIB nominal atingiram o pico em 1997.

Se o colapso da bolha foi a ferida, 1996 foi quando a ferida começou a infeccionar.

Eventos em 1996:

- Aprovação da lei de resgate das companhias de crédito habitacional, que injetou 685 bilhões de ienes de recursos públicos e se tornou a origem da desconfiança pública em relação aos bancos e da resistência a resgates.
- A decisão do gabinete Hashimoto de elevar o imposto sobre consumo para 5%.
- O Big Bang financeiro foi anunciado, e a reconstrução fiscal tornou-se política nacional.

Em abril de 1997, a alta do imposto sobre consumo, o fim dos cortes tributários especiais e encargos mais altos de seguro social juntos adicionaram cerca de 9 trilhões de ienes de ônus público. Então a crise cambial asiática chegou no verão.

Em novembro, a Sanyo Securities causou o primeiro default do pós-guerra no mercado call, congelando os mercados financeiros de curto prazo. Hokkaido Takushoku Bank e Yamaichi Securities quebraram em sequência.

A partir de 1998, o Japão entrou em deflação plena e aperto de crédito, e os suicídios passaram de 30.000.

O resultado nos 30 anos seguintes:

- O PIB nominal estagnou em torno de 500 trilhões de ienes por um quarto de século.
- A participação do Japão no PIB global caiu de cerca de 18% para menos de 4%.
- Os salários médios atingiram o pico em 1997 e depois caíram ou andaram de lado.
- O emprego não regular subiu de cerca de 20% para quase 40%.
- Os nascimentos caíram de cerca de 1,2 milhão para cerca de 690.000 em 2024.
- As taxas de política monetária permaneceram próximas de zero depois de cair abaixo de 1% em 1995.
- Os títulos públicos em circulação cresceram de cerca de 240 trilhões de ienes para mais de 1.100 trilhões de ienes.
- O Nikkei levou 34 anos, até fevereiro de 2024, para recuperar sua máxima de 1989.

Em outras palavras, as décadas perdidas não foram apenas uma ressaca financeira. Foram uma mudança estrutural envolvendo demografia, salários, deflação, dívida, escolhas de política e confiança social.

Type: Demo | Date: 2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 Tutoriais, Cursos e Recursos de Prompt

<a id="case-20"></a>
### Case 20: [Como o Fable 5 Muda Fluxos de Trabalho no Claude Code](https://x.com/AI_masaou/status/2064448218038223206) (por [@AI_masaou](https://x.com/AI_masaou))

**Use o Fable 5 definindo direção, contexto, metas e critérios de verificação em vez de microgerenciar cada etapa.**

[Vídeo original · @ClaudeDevs](https://x.com/ClaudeDevs/status/2064399512664526853)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Como o Fable 5 Muda Fluxos de Trabalho no Claude Code" width="760"><br>▶ Assistir ao vídeo</a>

O que mudou no trabalho diário da equipe do Claude Code depois do Claude Fable 5 é interessante.

Thariq, da equipe do Claude Code, diz que o Fable 5 mudou significativamente a forma como as pessoas dentro da Anthropic trabalham com Claude.

Antes, humanos precisavam verificar cuidadosamente se Claude estava fazendo o trabalho corretamente: dividir tarefas, revisar saídas e garantir que ele não tivesse parado no meio. Era mais próximo de supervisão.

Com o Fable 5, como ele consegue trabalhar por períodos mais longos, testar a si mesmo e gerar código de maior qualidade, o papel humano muda de monitorar se ele está fazendo o trabalho corretamente para orientar se ele está fazendo o trabalho certo.

Em outras palavras, definição de metas e construção de contexto importam mais do que supervisão.

O fluxo de trabalho alterado tem três partes:

1. Use Claude como parceiro de pensamento.

Envolva Claude antes da implementação, esclareça o que você quer construir e o que é possível, faça-o perguntar sobre uma pequena especificação ou gerar múltiplas direções e mocks HTML a partir de uma ideia, para que ambiguidades e problemas apareçam antes da codificação.

2. Forneça contexto, não apenas restrições.

Em vez de apenas dizer "mantenha simples" ou "não construa demais", explique por quê.

Por exemplo: "Este é um recurso experimental que pode ser removido em um mês, então não crie uma estrutura difícil de descartar."

Isso permite que Claude faça julgamentos melhores.

3. Dê metas e métodos de verificação. O Fable 5 funciona bem com `/goal` e Workflows do Claude Code. Dê a ele uma especificação, defina a implementação completa como meta e deixe workflows verificarem cada etapa e prepararem um relatório sobre o que foi implementado e o que diferiu.

Por fim, Thariq diz que as pessoas devem tentar usá-lo de forma mais ambiciosa. Vale a pena testar o Fable 5 em trabalhos que antes pareciam difíceis demais para LLMs, e até a edição de vídeo do vídeo referenciado foi feita com Fable.

Type: Demo | Date: 2026-06-09

---
<a id="case-21"></a>
### Case 21: [Revisão de Um Bilhão de Tokens e Estratégia de Roteamento](https://x.com/JJEnglert/status/2064420538798260388) (por [@JJEnglert](https://x.com/JJEnglert))

**Use o Fable 5 para planejamento e revisão frontier, depois roteie implementação de alto volume para modelos mais baratos.**

A Revisão do Claude Fable 5: Um Bilhão de Tokens, Julgada por um Não Engenheiro.

Gastei um bilhão de tokens testando o Claude Fable 5 em projetos reais: UI e UX, escrita, estratégia, segurança, engenharia e trabalho de conhecimento. O tipo de trabalho que eu realmente precisava entregar.

Honestamente, pareceu que eu tinha uma vantagem injusta.

Primeiro, a lente: não sou engenheiro. A maioria das análises de modelos vem de engenheiros rodando benchmarks de engenharia. Esta vem de um não engenheiro que usou o Claude Fable 5 para fazer trabalho que antes exigia uma equipe de engenheiros.

Se você faz trabalho de conhecimento e quer saber se este modelo muda seu dia, esta análise foi escrita para você.

Claude Fable 5 é o primeiro modelo da nova família Claude 5 da Anthropic, uma nova camada acima de Claude Opus e o modelo Claude mais avançado disponível em geral. Tive acesso antes do lançamento, então tudo aqui vem de trabalho real, não de uma demo.

Por que o teste visual:

A maioria das análises afoga você em benchmarks. Pontuações em testes que você nunca vai rodar não dizem se o modelo se paga.

Claude Fable 5 é estado da arte em essencialmente tudo em que foi testado, mas não é por isso que estou escrevendo. Qualitativamente, é uma mudança de patamar que justifica o salto de versão principal.

Eu avalio de forma diferente: coloco um modelo em trabalho real e observo o que acontece.

Perguntas que meço:

1. Parece um avanço real?
2. Consegue levar uma ideia a um resultado funcional e entregável?
3. Consegue escrever como uma pessoa, e especificamente como eu?
4. Captura problemas difíceis e escondidos?
5. Antecipa o que preciso antes de eu pedir?

Sensação de modelo grande:

Eu não sentia isso desde o Opus 4.5. Desde a primeira tarefa séria, Claude Fable 5 me deu aquela sensação de "modelo grande": raciocínio, escrita, construção, segurança, tudo forte em todo o conjunto.

O sinal mais claro: mesmo quando lhe entreguei bons materiais de preparação, ele não ficou apenas dentro deles. Leu os arquivos, leu a situação real e encontrou um caminho melhor fora da caixa que eu havia desenhado.

Construindo e entregando:

Eu estava reconstruindo nosso site da Tenex para modernizar a stack para agentes. GPT 5.5 e Claude 4.8 não conseguiam chegar perto o bastante. Mesmo com arquivos Figma, ficavam por volta de 85-90%.

Então Claude Fable 5 olhou todos os arquivos, disse que poderia fazer melhor, foi direto à fonte original do Webflow, baixou todos os assets e reconstruiu a experiência uma página por vez. Quase fez tudo em uma tentativa.

Depois construí um segundo site, inteiramente novo, com design fresco: stack tech moderna, stack de agentes, skills, SEO e AEO otimizados, 80 páginas prontas para envio em um fim de semana. Como dono de agência, eu teria cobrado $50k por isso.

Também fiz o Fable construir uma fábrica programática completa de clipes.

Ele conectou HeyGen, HyperFrames, ElevenLabs, Cloudflare Workers e um VPS.

Ele encontra tópicos, escreve scripts, cria thumbnails, edita vídeo, compõe música, adiciona motion graphics e publica em redes sociais.

Escrita e voz:

Eu estava reconstruindo nossa voz de marca com GPT 5.5 e Claude 4.8. Claude Fable 5 replicou o documento de voz quase identicamente e depois manteve essa voz ao longo de 80 páginas do novo site: features, estudos de caso, artigos de blog e playbooks.

Escreveu como uma pessoa, não no padrão plano de IA, e não se desviou depois de alguns parágrafos.

Segurança:

Eu tinha um repositório grande em que Claude 4.8 e GPT 5.5 vinham trabalhando sem sinalizar um risco. Claude Fable 5 encontrou um bug sério e escondido na primeira passada e o corrigiu na hora.

O fator humano:

Fiz uma pergunta enquanto esperava um cron job. Ele respondeu e depois acrescentou que eu tinha cerca de 10 minutos restantes no timer e que me avisaria quando terminasse. Nunca perguntei sobre o timer.

Custo:

- Custo da carga de trabalho do Claude Fable 5: $1.442
- Tokens: 1,04 bilhão
- Trabalho entregue: um novo site, infraestrutura e um pacote de agente funcional
- Estimativa de valor de agência: $30.000-$50.000

O resultado valeu o custo de tokens, mas você sente o medidor mais do que com qualquer outro modelo. A Anthropic chama o Fable 5 de intensivo em tokens por design.

Dica pro #1: rode-o como híbrido.

Não rode tudo no Claude Fable 5. Rode um relay:

1. Pense com Claude Fable 5 para planejamento, estratégia, arquitetura e mapeamento da abordagem.
2. Construa com 4.8, GPT-5.5 ou Sonnet 4.6 para implementação e trabalho repetitivo.
3. Revise com Claude Fable 5 para capturar o que modelos mais baratos perdem.

Dica pro #2: combine a configuração de esforço com a tarefa.

- High é o ponto ideal para a maioria dos trabalhos.
- Extra high é para as tarefas mais difíceis e longas.
- Low ou medium é para sessões rápidas de ida e volta.

Dica pro #3: deixe-o auditar sua própria configuração.

Aponte o Fable 5 para suas skills, arquivos CLAUDE.md e configs. Muito desse scaffolding foi escrito para modelos mais fracos e pode segurar um modelo mais inteligente.

O veredito:

Claude Fable 5 é o primeiro modelo em algum tempo que genuinamente parece mais inteligência do que o que veio antes.

Mesmo precificado em tarifas frontier, a carga de trabalho deu lucro.

Se você puder pagar, use-o agora no trabalho em que um salto real de qualidade muda o resultado.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-22"></a>
### Case 22: [Prompt Defensivo de Endurecimento de Dispositivos](https://x.com/Truunik/status/2064399110384292077) (por [@Truunik](https://x.com/Truunik))

**Rode um prompt defensivo passo a passo de hardening em que o Fable 5 inventaria dispositivos, dá verificações exatas e espera confirmação.**

"Seguro para uso geral" aqui está um prompt para proteger seus dispositivos. Funciona com Opus 4.8 e Fable 5.

DEVICE HARDENING — Claude 5 Security Pass

Você está atuando como assistente defensivo de segurança. Seu trabalho é me guiar pelo hardening de todos os meus dispositivos e verificar cada etapa. Isto é hardening autorizado de autodefesa em dispositivos que possuo.

STEP 0 — MODEL SELF-CHECK

Faça isto primeiro e defina uma flag.

1. Informe seu ID exato de modelo, como claude-opus-4-8, claude-fable-5 ou claude-mythos-5.

2. Decida: este modelo está na família Claude 5, ou seja, Fable 5 ou Mythos 5?

- Se SIM, defina RERUN_NOTICE = false.
- Se NÃO, como Opus 4.8 ou anterior, defina RERUN_NOTICE = true.

Continue o passe completo de hardening normalmente. NÃO pare nem degrade. Você é plenamente capaz desta tarefa defensiva.

3. Mostre a flag somente na seção FINAL.

STEP 1 — INVENTORY

Pergunte quais dispositivos estão no escopo:

- Laptops/desktops e sistemas operacionais
- Telefones/tablets
- Roteadores
- NAS/servidor doméstico
- Contas sempre ativas como Apple ID, Google, Microsoft, GitHub, gerenciador de senhas, email e contas financeiras

Produza um inventário numerado curto e confirme comigo antes de prosseguir.

STEP 2 — HARDENING WALKTHROUGH

Vá categoria por categoria. Para cada item:

- Diga o que fazer.
- Dê o comando exato ou caminho de configuração para meu OS.
- Diga como verificar que foi feito.
- Espere eu confirmar antes de avançar.

Nunca rode um comando destrutivo sem confirmação explícita. Prefira verificações somente leitura e deixe-me aplicar mudanças.

Cubra, nesta ordem:

1. Atualizações de OS & firmware: OS totalmente atualizado, atualizações automáticas ativadas, firmware atual.
2. Criptografia de disco: FileVault, BitLocker ou LUKS ativado; chave de recuperação armazenada offline.
3. Autenticação de contas: senhas fortes e únicas via gerenciador de senhas; MFA resistente a phishing em todas as contas críticas; remover 2FA apenas por SMS quando possível; revisar e revogar sessões e tokens de app obsoletos.
4. Contas locais & privilégios: conta admin separada da conta de uso diário; sem login automático; bloqueio de tela com timeout curto; senha de firmware/login.
5. Rede: firewall ativado; senha admin do roteador alterada; firmware atualizado; WPA3; admin remoto desativado; UPnP revisado; hardening de DNS; rede guest para IoT.
6. Auditoria de apps & permissões: revisar concessões de câmera, microfone, localização, gravação de tela e acesso total ao disco; remover apps não usados; checar itens de login e agentes em segundo plano.
7. Navegador: atualizar; auditar extensões; remover desconhecidas; ativar HTTPS-only; revisar exposição de senhas salvas; checar dispositivos sincronizados desconhecidos.
8. Backups: criptografados, automatizados, regra 3-2-1, uma cópia offline; verificar se uma restauração realmente funciona.
9. Higiene de credenciais: escanear segredos em texto puro em dotfiles, arquivos env e histórico do shell; confirmar que arquivos sensíveis estão bloqueados; rotacionar qualquer coisa exposta.
10. Dispositivos móveis: OS atual; biometria + senha forte; modo lockdown ou advanced-protection se disponível; varredura de permissões de apps; Find My ativado.
11. Checagem de comprometimento: procurar chaves SSH desconhecidas, usuários admin inesperados, launch agents ou cron jobs suspeitos e sessões ou dispositivos logados não reconhecidos.

STEP 3 — REPORT

Produza um checklist de cada item marcado como concluído, precisa de ação ou ignorado, com as 3 ações pendentes de maior impacto.

FINAL — RERUN NOTICE

Se RERUN_NOTICE == true, termine exatamente com:

NOTICE: This hardening pass ran on a pre-Claude 5 model (your model ID).

It is complete and valid, but Claude 5 (Fable 5 / Mythos 5) has stronger security reasoning.

Re-run this prompt on Claude 5 as soon as possible to catch anything this pass may have missed.

Se RERUN_NOTICE == false, termine com:

Hardening pass completed on Claude 5. No re-run needed.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-23"></a>
### Case 23: [Prompt de Meta para Auditoria de Design de Site Completo](https://x.com/Voxyz_ai/status/2064441201084825921) (por [@Voxyz_ai](https://x.com/Voxyz_ai))

**Use `/goal` para fazer o Fable 5 iniciar um site, capturar telas de páginas, auditar UX, escrever um relatório e corrigir pequenos problemas seguros.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dca99f9390b1624b3dfd4b45.png" alt="Prompt de Meta para Auditoria de Design de Site Completo" width="760">

impressões rápidas depois de algumas horas com fable 5:

→ ele quer tarefas grandes. coisas pequenas parecem abaixo dele; quanto mais complexo o trabalho, mais forte ele vai

→ eu ainda não ligaria ultracode, ele inicia um monte de agentes paralelos

→ ele é meio lento. mesmo com effort reduzido, ainda fica pensando por um tempo.

A timeline está cheia de posts sobre como ele queima tokens, então testei no meu plano Max de $200: effort em xhigh, rodei um `/goal` de auditoria de design de site completo, 30 minutos, levou 2% da minha cota semanal. Não tão louco quanto eu esperava.

O prompt que rodei:

/goal inicialize o site real deste projeto, capture a tela de cada página, rode uma auditoria completa de UI/UX do site e produza um relatório de design acionável.

Audite como um líder sênior de design em seu primeiro dia: julgue se um usuário normal consegue entender o produto, confiar nele e concluir a ação principal sem ler docs, não se a UI parece bonita.

Critérios de aceitação:

- ambiente de desenvolvimento local inicia e o site real abre
- páginas-chave capturadas com debugging de navegador embutido
- cobre páginas principais, fluxos centrais de usuário e layout mobile
- dimensões: primeiras impressões, navegação, hierarquia visual, consistência de componentes, estados de loading / empty / error, sinais de confiança, caminhos de conversão
- cada problema marcado P0-P3, qual de entendimento / confiança / conversão ele prejudica, e a correção específica
- relatório escrito em docs/design-audit/README.md, screenshots em docs/design-audit/assets/
- corrija na hora coisas pequenas e seguras, como copy, espaçamento e hierarquia de botões. mudanças grandes são apenas recomendações. nunca toque ações de pagamento / exclusão / publicação
- termine com os 5 problemas que mais prejudicam conversão e 5 quick wins corrigíveis hoje

Quando terminar, salve todo o fluxo como uma skill reutilizável: iniciar, capturar tela, auditar, priorizar, corrigir. Rode novamente depois de cada release.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-24"></a>
### Case 24: [Divisão de Fluxo de Trabalho Criativo Longo](https://x.com/aianimesyokunin/status/2064409545620017531) (por [@aianimesyokunin](https://x.com/aianimesyokunin))

**Use o Fable 5 para projetar formatos estáveis e exemplos; depois entregue essa estrutura a outro sistema de geração para saída específica do domínio.**

Depois que Claude mudou de Opus para o novo modelo, Fable 5, a divisão de trabalho para produção doujin ficou claramente mais fácil, então estou compartilhando o fluxo.

Minha divisão de trabalho:

1. Claude cuida do design.
2. Grok cuida da expressão.
3. O ambiente local cuida da geração.

No papel de design do Claude, ele define padrões detalhados:

- ordem das palavras no prompt
- posicionamento de vírgulas
- proporção de tags para linguagem natural
- formatação de um item por linha
- regras fixas para negativos e resolução

Ele também gera muitos exemplos nesse formato.

O motivo de eu usar Claude em vez de Grok para isso é que Claude é claramente mais forte em design. É melhor deixar o modelo mais inteligente cuidar da estrutura.

O ponto-chave é que Grok recebe não instruções, mas um formato mais um conjunto de exemplos. Grok imita os exemplos, então consegue entrar no lado da expressão mantendo o mesmo formato. Esse mecanismo impede que a saída derive.

Mais uma dica: diga a Claude no início para onde o trabalho final vai. Então ele mesmo traçará o limite: "posso fazer até aqui; além disso, use o outro lado." Se isso ficar oculto, a conversa pode se desviar.

O que mudou de Opus para Fable?

Com Opus, ao gerar muitos exemplos, vírgulas e formatação degradavam gradualmente nas saídas posteriores, levando a correções como "eu não disse para escrever uma linha, certo?" ou exigindo um chat de handoff reescrito.

Fable consegue manter o formato durante execuções longas, então o primeiro e o último exemplos têm a mesma estrutura. Como o material didático passado para Grok é mais estável, a saída downstream também se torna mais estável.

Construa o formato com o modelo mais inteligente e deixe a expressão para o modelo que consegue produzi-la.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-25"></a>
### Case 25: [Guia para Iniciantes no Uso do Fable 5](https://x.com/bielzinn/status/2064451064594608567) (por [@bielzinn](https://x.com/bielzinn))

**Use o Fable 5 com prompts orientados a metas, loops de verificação e configurações de esforço em vez de pequenas instruções passo a passo.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f180cebef645f5ad8efdeb92.jpg" alt="Guia para Iniciantes no Uso do Fable 5" width="760">

Claude para Iniciantes: o que você precisa saber sobre o Fable 5.

A Anthropic lançou recentemente Claude Fable 5, também conhecido como Claude Mythos 5, e ele está deixando outros modelos de IA para trás nos benchmarks.

Se você é desenvolvedor, criador de conteúdo ou entusiasta de tecnologia, aqui está o que mais importa:

[1] Mude sua forma de pensar:

Com o Fable 5, você não precisa mais ficar de olho em cada pequeno detalhe do código ou revisar tudo procurando erros.

O modelo é inteligente o bastante para lidar com isso.

Seu papel agora é garantir que ele esteja seguindo na direção certa, focando mais em estratégia do que em execução técnica.

[2] Aproveite loops e metas:

O maior diferencial do Fable 5 é autonomia.

Em vez de dar instruções passo a passo, você só precisa dizer qual é o objetivo final.

Ele consegue trabalhar sozinho por dias até alcançar o resultado que você definiu como sucesso, inclusive construindo aplicações inteiras.

[3] Trate Claude como parceiro:

A Anthropic recomenda usar o modelo como um verdadeiro “parceiro de pensamento”.

Antes de colocá-lo para trabalhar, peça a opinião dele: “Como você faria isto?”, “O que você mudaria?”

Dica extra: ative o modo Advanced Plan e peça a Claude para questionar você sobre tudo relacionado ao projeto antes de começar a codar

[4] Configurações ideais de terminal: se você usa Claude Code no terminal, ative o modo automático. Também vale aumentar o nível de esforço para Effort High, porque embora use mais tokens, o modelo pensa muito mais profundamente e o resultado compensa.

Nota importante: Claude Fable 5 só estará disponível para assinantes até 22 de junho. Depois disso, só será acessível pela API e ao dobro do custo do modelo Opus.

Em outras palavras, talvez estejamos vendo o fim da era de assinaturas baratas para modelos de IA de ponta. Se você já é assinante, este é o momento de testar os limites do que achava impossível.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-26"></a>
### Case 26: [Prompt de Auditoria de Repositório para Copiar e Colar](https://x.com/meta_alchemist/status/2064431279383433646) (por [@meta_alchemist](https://x.com/meta_alchemist))

**Cole o prompt de auditoria de repositório no Fable 5 e peça descoberta baseada em arquivos, achados, estratégia e um plano de tarefas por marcos.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/846e5ecb825853db17bd3564.jpg" alt="Prompt de Auditoria de Repositório para Copiar e Colar" width="760">

Conseguiu acesso ao Claude Fable 5?

A primeira coisa que você deve fazer é atualizar seus principais projetos com ele, para que ele melhore drasticamente tudo em que você vem trabalhando.

Rode este Prompt de Auditoria & Melhoria de Projeto em cada repo importante para você.

Basta copiar e colar:

Plano de Auditoria & Melhoria de Repo.

Prompt feito por Claude Fable 5.

Você é um engenheiro de software principal de nível mundial e auditor técnico.

Seu trabalho é analisar profundamente este repositório, produzir uma auditoria honesta e entregar um plano de melhoria priorizado e acionável.

Trabalhe nas quatro fases abaixo, em ordem.

Não pule adiante.

Fundamente toda afirmação em arquivos reais: cite caminhos de arquivo e números de linha.

Se você não conseguir verificar algo, diga isso explicitamente em vez de adivinhar.

Fase 1 / Descoberta & Mapeamento (leia antes de julgar)

Explore o repositório sistematicamente antes de formar opiniões:

- Mapeie a estrutura de diretórios e identifique o tipo de projeto, linguagem(ns), frameworks e alvos de runtime.
- Identifique entry points, módulos centrais e o fluxo principal de dados/controle pelo sistema.
- Leia manifestos de pacote, lockfiles, configs de build, configs de CI, arquivos de ambiente/configuração e quaisquer docs (README, CONTRIBUTING, ADRs).
- Determine para que o projeto serve: seu propósito, usuários pretendidos e maturidade aparente (protótipo, ferramenta interna, serviço de produção, biblioteca).
- Observe convenções já em uso (nomenclatura, limites de módulo, padrões de tratamento de erro, estilo de teste) para que as recomendações se encaixem na cultura existente em vez de lutar contra ela.

Saída para esta fase: um "Mapa do Repo" conciso com propósito, stack, esboço de arquitetura, diretórios-chave com descrições de uma linha e qualquer coisa que tenha surpreendido você.

Fase 2 / Auditoria (baseada em evidências, classificada por severidade)

Audite cada dimensão abaixo.

Para cada achado, registre:

- o que você encontrou
- onde (arquivo:linha)
- por que importa (consequência concreta, não princípio vago)
- severidade: Critical / High / Medium / Low

Arquitetura & design:

- limites de módulo
- acoplamento/cohesão
- dependências circulares
- abstrações vazando
- god objects/files
- violações de camadas
- gargalos de escalabilidade

Qualidade de código:

- duplicação
- código morto
- hotspots de complexidade (funções mais longas/mais ramificadas)
- padrões inconsistentes
- lacunas de tratamento de erro (exceções engolidas, edge cases ausentes)
- buracos de type safety

Segurança:

- segredos ou credenciais hardcoded
- riscos de injeção
- desserialização insegura
- validação de input ausente
- fraquezas de auth/authz
- dependências desatualizadas com CVEs conhecidos
- configs permissivas demais

Testes:

- lacunas de cobertura, especialmente em torno da lógica central de negócio
- qualidade dos testes: os testes afirmam comportamento ou apenas execução?
- tipos de teste ausentes: unit, integration, e2e
- padrões flaky
- código intestável

Performance:

- queries N+1
- alocações ou cópias desnecessárias
- chamadas bloqueantes em caminhos async
- caching/indexing ausentes
- crescimento sem limite: memória, arquivos, filas

Dependências:

- pacotes desatualizados, sem manutenção, duplicados ou desnecessariamente pesados
- riscos de licença
- higiene de lockfile

DevEx & operações:

- atrito de build/setup
- lacunas de CI/CD
- enforcement ausente de linting/formatting
- qualidade de logging/observabilidade
- reporte de erros
- história de deploy

Documentação:

- precisão do README
- caminho de onboarding
- comportamento crítico não documentado
- docs obsoletas que contradizem o código

Regras para esta fase:

- Prefira 15 achados de alta confiança a 50 especulativos.
- Distinga fatos ("esta função não tem tratamento de erro: src/api/client.ts:142") de julgamentos ("as responsabilidades deste módulo parecem pouco claras") e rotule qual é qual.
- Liste também o que o repo faz bem: pontos fortes importam para decidir o que preservar.

Saída para esta fase: um "Relatório de Auditoria": achados agrupados por dimensão, ordenados por severidade, mais uma seção de Pontos Fortes. Não esqueça de mencionar todas as partes ruins que precisam de máxima prioridade.

Fase 3 / Estratégia de Melhoria

Sintetize a auditoria em uma estratégia:

- Identifique os 3-5 temas que explicam a maioria dos achados, por exemplo "sem limites aplicados entre camadas" ou "tratamento de erro é ad hoc".
- Para cada tema, proponha um estado-alvo e o princípio por trás dele.
- Declare trade-offs explícitos: o que você recomenda NÃO corrigir e por quê (esforço vs. retorno, risco, maturidade do projeto).
- Defina como "concluído" se parece — sinais mensuráveis, por exemplo "CI falha em erros de lint", "cobertura de testes do módulo central ≥ 80%" ou "zero achados Critical".

Fase 4 / Plano Detalhado de Tarefas

Converta a estratégia em um plano de execução.

Divida o trabalho em tarefas discretas.

Cada tarefa deve incluir:

- Título e descrição em um parágrafo
- Arquivos/áreas afetados
- Critérios de aceitação: como verificamos que está concluído
- Estimativa de esforço: S = <2h, M = meio dia, L = 1-2 dias, XL = precisa de decomposição
- Risco da própria mudança: poderia quebrar coisas?
- Dependências de outras tarefas

Ordene tarefas em marcos:

Marco 0 Rede de segurança: qualquer coisa necessária antes de refatorar com segurança (testes em caminhos críticos, gates de CI, backups).

Marco 1 Correções críticas: problemas de segurança e correção.

Marco 2 Melhorias de alto impacto: mudanças que tornam todo trabalho futuro mais fácil.

Marco 3 Qualidade & polimento: itens médios/baixos restantes que valem a pena fazer.

Sinalize quick wins (alto impacto, esforço S) separadamente para que possam ser feitos imediatamente.

Para as 3 principais tarefas, inclua um breve esboço de implementação (abordagem, passos-chave, armadilhas).

Formato do Entregável Final

Produza um único documento com estas seções:

- Executive Summary: ≤10 frases, nota geral de saúde A-F com justificativa, top 3 riscos, top 3 oportunidades
- Repo Map
- Audit Report
- Improvement Strategy
- Task Plan: milestones + task table + quick wins
- Open Questions: qualquer coisa que você precise de um humano para decidir, como intenção de produto, candidatos a depreciação, metas de performance

Restrições

NÃO modifique nenhum código durante esta auditoria.

Apenas análise.

Não encha o relatório.

Se uma dimensão estiver saudável, diga isso em uma frase e siga em frente.

Calibre para a maturidade do projeto.

Não recomende infraestrutura enterprise-grade para um protótipo de fim de semana, a menos que os objetivos do dono exijam.

Analise as necessidades do projeto e forneça recomendações das formas mais eficazes.

Se o repo for grande, priorize profundidade nos 20% centrais de código que fazem 80% do trabalho e observe quais áreas receberam revisão mais leve.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-27"></a>
### Case 27: [Estratégia de Uso em Janela Limitada](https://x.com/meta_alchemist/status/2064423360428490911) (por [@meta_alchemist](https://x.com/meta_alchemist))

**Gaste o uso do Fable 5 em auditoria, arquitetura e planejamento enquanto a janela de acesso é favorável; depois use modelos mais baratos para execução.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a4293d14cc7571bdcf8b1478.png" alt="Estratégia de Uso em Janela Limitada" width="760">

Uma dica para usuários do Claude animados com o Fable 5:

Claude Fable 5 é SOTA em todo o conjunto, com grande margem, e eu adoro isso.

MAS a partir do dia 23, ele só estará disponível por créditos, em vez de poder usar o modelo plenamente com um plano.

Use estes 14 dias nos seus melhores projetos.

Dê a ele principalmente trabalho relacionado a auditoria e arquitetura, para que você tenha ótima documentação sobre como melhorar tudo que vem construindo.

Faça isso em vez de tentar aplicá-lo a tarefas que vão devorar seus limites.

Enquanto o Fable focar em saber o que melhorar, outros modelos podem ajudar você a fazer o resto.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-28"></a>
### Case 28: [Usando Goals e Workflows no Claude Code](https://x.com/oikon48/status/2064402696124453157) (por [@oikon48](https://x.com/oikon48))

**Use o Fable 5 como parceiro de pensamento antes da implementação; depois combine `/goal` e workflows para executar e verificar o plano.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bcf9dc92c525978c69b3c869.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9567dd41be289437a45f8800.jpg" alt="Usando Goals e Workflows no Claude Code" width="760"><br>▶ Assistir ao vídeo</a>

Thariq, da equipe do Claude Code, explica que, depois que Claude Fable 5 saiu, a forma de trabalhar mudou fundamentalmente.

No passado, as pessoas verificavam se Claude estava fazendo o trabalho corretamente.

Agora elas verificam se Claude está fazendo o trabalho certo.

Há três mudanças concretas.

1. Trate Claude como parceiro de pensamento.

Consulte Claude cedo, antes da implementação.

Faça-o entrevistar você antes de codar.

Forneça background e contexto em vez de apenas restrições.

Por exemplo, em vez de dizer 'mantenha simples' ou 'não construa demais', diga:

'Este é um recurso experimental e provavelmente será removido em um mês, então projete-o para ser fácil de descartar depois.'

2. Torne metas e métodos de verificação explícitos.

Use ativamente os novos recursos `/goal` e Workflows do Claude Code.

`/goal` diz a Claude para continuar trabalhando até que a especificação esteja totalmente implementada.

Workflows permitem que Claude paralelize e verifique o próprio trabalho e prepare um relatório.

Prompt de exemplo:

'Defina uma meta para implementar a especificação completamente; depois use um workflow para verificar cada parte do plano e prepare um relatório sobre o que foi implementado e se algo diferiu.'

3. Seja mais ambicioso.

Experimente tarefas que antes pareciam impossíveis para LLMs, como fazer Claude Fable 5 lidar com edição de vídeo.

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 Plataforma, API e Integração de Ferramentas

<a id="case-29"></a>
### Case 29: [Configuração de Integração do Agente Hermes](https://x.com/IBuzovskyi/status/2064427654942740608) (por [@IBuzovskyi](https://x.com/IBuzovskyi))

**Configure o Hermes para usar `anthropic/claude-fable-5` em execuções complexas de `/goal` e tarefas longas com cache.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/4a3b9936f91986268dfeb748.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d9a63a0c689f8e305289a9e6.jpg" alt="Configuração de Integração do Agente Hermes" width="760"><br>▶ Assistir ao vídeo</a>

HERMES AGENT AGORA RODA EM CLAUDE FABLE 5, o primeiro modelo Mythos-class público da Anthropic.

Lançado em 9 de junho. Construído para o tipo de trabalho que Hermes faz melhor: tarefas autônomas de longo horizonte.

Adicione a qualquer perfil pelo Nous Portal, OpenRouter ou pela API nativa da Anthropic:

hermes model

Escolha o provider e depois:

/model anthropic/claude-fable-5

Por que Fable 5 se encaixa especificamente no Hermes:

→ Construído para tarefas de dias. Quanto mais longa a tarefa, maior sua vantagem. Execuções Hermes `/goal` que duram horas se beneficiam mais.

→ Autocorrige em loop. A própria orientação da Anthropic é: desenhe uma meta ou rubrica, deixe-o autocorrigir, dê um passo para trás. É exatamente assim que Hermes `/goal` funciona.

→ Forte em memória entre sessões. No Continual Learning Bench, ele completou o loop completo: falhar → investigar → verificar → destilar → consultar. O sistema de memória do Hermes alimenta isso diretamente.

→ 80,3% no SWE-Bench Pro. Melhor modelo de codificação disponível. Aponte seu perfil de code-reviewer para ele.

Preços pela API:

- $10/milhão de input
- $50/milhão de output
- 90% de desconto com prompt caching. O Hermes anexa automaticamente breakpoints de cache de 1 hora.

Uma observação: consultas de cibersegurança, biologia e química voltam para Opus 4.8. Isso dispara em menos de 5% das sessões. Tenha isso em mente para perfis focados em segurança.

Melhor setup: Fable 5 para `/goal`s complexos, modelos mais baratos para cron jobs rotineiros.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-30"></a>
### Case 30: [Capacidades, Preços e Notas de Assinatura](https://x.com/btibor91/status/2064441061079134598) (por [@btibor91](https://x.com/btibor91))

**Use este caso para entender quando o Fable 5 está disponível, quanto custa e quais domínios protegidos podem cair para outro modelo.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d0d76497e4c8f77d3d081493.jpg" alt="Capacidades, Preços e Notas de Assinatura" width="760">

A Anthropic lançou Claude Fable 5 e Claude Mythos 5, duas versões de seu modelo mais capaz até agora.

Fable 5 é para uso geral.

Mythos 5 é para um pequeno conjunto de parceiros confiáveis.

A única diferença real é quais salvaguardas estão em vigor.

- As capacidades do Claude Fable 5 excedem as de qualquer modelo que a Anthropic já disponibilizou em geral.
- Ele é estado da arte em quase todos os benchmarks testados.
- Quanto mais longa e complexa a tarefa, maior sua vantagem.
- Em solicitações relacionadas a cibersegurança, biologia e química, ou distillation, a resposta do Fable 5 é tratada pelo Claude Opus 4.8.
- Distillation significa tentativas de extrair capacidades do Claude para treinar modelos concorrentes.
- Você é informado quando isso acontece, e isso dispara em menos de 5% das sessões em média.
- Claude Mythos 5 é o mesmo modelo subjacente que o Fable 5, com salvaguardas removidas em algumas áreas.
- Mythos 5 foi implantado primeiro para cyberdefenders do Project Glasswing em colaboração com o governo dos EUA.
- A Anthropic diz que Mythos 5 tem as capacidades de cibersegurança mais fortes de qualquer modelo no mundo.
- O system card revela uma salvaguarda separada que limita a eficácia do Claude em solicitações de desenvolvimento frontier de LLM.
- Essas solicitações incluem pipelines de pretraining, infraestrutura de treinamento distribuído e design de aceleradores de ML.
- Diferentemente das outras salvaguardas, esta não é visível para você e não cai para outro modelo.
- Ela funciona por métodos como modificação de prompt, steering vectors ou fine-tuning parameter-efficient.
- Ambos os modelos são oferecidos a $10 por milhão de tokens de input e $50 por milhão de tokens de output.
- Isso é menos da metade do preço do Claude Mythos Preview.
- Fable 5 está incluído sem custo extra nos planos Pro, Max, Team e Enterprise por assento, do lançamento até 22 de junho.
- Em 23 de junho, ele é removido desses planos, e usá-lo exige créditos de uso.
- A janela incluída pode ser estendida se a capacidade permitir.
- O objetivo é restaurar o Fable 5 como parte padrão dos planos de assinatura o mais rápido possível.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-31"></a>
### Case 31: [Resumo de Lançamento, Acesso, Preços e Segurança](https://x.com/ctgptlb/status/2064410460963934479) (por [@ctgptlb](https://x.com/ctgptlb))

**Use este resumo de lançamento para escolher rota de acesso, nome de modelo de API, janela de contexto, estratégia de cache e timing de assinatura.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7620f9d5f1c29e9f6c3178e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0b89d6ace5df7c0f3ebe064e.jpg" alt="Resumo de Lançamento, Acesso, Preços e Segurança" width="760"><br>▶ Assistir ao vídeo</a>

Um resumo do que você deve saber sobre Claude Fable 5, o modelo Mythos-class que finalmente está disponível em geral.

A Anthropic anunciou Claude Fable 5, o primeiro modelo Mythos-class geralmente disponível, posicionado acima do Opus e o primeiro membro da família Claude 5.

Acesso:

- Nome do modelo na API: `claude-fable-5`
- Disponível pela Claude API, AWS, Google Cloud e Microsoft Foundry
- Claude Code dá suporte a uma janela de contexto de 1M tokens em Pro, Max, Team e Enterprise

Notas de benchmark:

- SWE-bench Pro: 80,3%
- Opus 4.8: 69,2%
- GPT-5.5: 58,6%
- Gemini 3.1 Pro: 54,2%

Quanto mais longa e complexa a tarefa, maior a lacuna.

Na avaliação da Stripe, ele completou uma migração em uma codebase Ruby de 50 milhões de linhas em um dia, trabalho que antes teria levado mais de dois meses para uma equipe.

Ele também é estado da arte em tarefas visuais, zerando Pokemon FireRed usando apenas informação de tela e um setup mínimo.

Roteamento de segurança:

- Consultas envolvendo cyber, bio/chem ou distillation são detectadas por um classificador.
- Essas solicitações são tratadas por Opus 4.8 em vez disso, com notificação.
- Isso dispara em menos de 5% das sessões.
- Mais de 1.000 horas de testes externos de bug bounty não encontraram jailbreak universal.

Preços:

- $10 por milhão de tokens de input
- $50 por milhão de tokens de output
- 90% de desconto de input para prompt caching

Timing de assinatura:

- Assinaturas Pro e Max o incluem sem custo extra até 22 de junho.
- Depois de 23 de junho, créditos de uso são necessários.
- A Anthropic diz que planeja devolvê-lo aos planos padrão quando a capacidade permitir.

Felix Rieseberg, head of desktop da Anthropic, diz que o Fable 5 inicia uma terceira era:

de perguntas, para tarefas, para responsabilidades.

Ele não pede mais ao Claude para investigar crashes um por um; faz com que ele monitore continuamente todos os relatórios.

A unidade de trabalho está mudando de "tarefa" para "responsabilidade."

Type: Tutorial | Date: 2026-06-09

---
<a id="case-32"></a>
### Case 32: [Estratégia de Redução de Custo Baseada em Advisor](https://x.com/grapeot/status/2064460026996219992) (por [@grapeot](https://x.com/grapeot))

**Use o Fable 5 como advisor ou revisor em um fluxo com modelo mais barato quando a inteligência marginal vale o custo.**

Artigo vinculado: exemplos com Opus como consultor; não são resultados de benchmark do Fable. [yage.ai](https://yage.ai/share/claude-advisor-tool-20260609.html)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a21858fed45b612b616e34ce.png" alt="Estratégia de Redução de Custo Baseada em Advisor" width="760">

Fable 5 é caro, mas a Anthropic publicou a resposta de economia de custo dois meses atrás.

Hoje a Anthropic lançou Claude Fable 5, com preço de $50 por milhão de tokens de output, mais de três vezes o Sonnet. Depois de 22 de junho, usuários de assinatura também pagarão por uso.

Coincidentemente, em 9 de abril, a Anthropic lançou a ferramenta advisor:

- Deixe Haiku ou Sonnet fazer o trabalho.
- Use Opus como advisor.
- Cobre por chamada.
- Rode a orquestração server-side dentro de uma única solicitação.

No mesmo dia escrevi sobre AgentOpt.

Esse paper concluiu que colocar Opus no papel de planejador ficou perto do fim entre 81 combinações de modelos.

O motivo: ele não respeita limites de papel e, em 7 de 9 experimentos, pulou o solver downstream e respondeu diretamente.

Essas duas coisas parecem opostas na superfície, mas o princípio é o mesmo:

Dê controle ao modelo que segue o protocolo e trate inteligência como um recurso sob demanda.

Dados oficiais:

- Sonnet mais Opus advisor melhorou o SWE-bench Multilingual em 2,7 pontos, enquanto reduziu o custo por tarefa em 11,9%.
- Haiku mais Opus advisor melhorou BrowseComp de 19,7% para 41,2%, sendo 85% mais barato que Sonnet sozinho.

A compatibilidade com Fable 5 foi atualizada no mesmo dia, mas apenas para autopareamento: executor Fable 5 para advisor Fable 5.

Um modelo mais barato mais Fable 5 como advisor ainda não está aberto, mas o precedente sugere que pode vir em breve. Antes de 22 de junho, usuários de assinatura do Claude Code podem sentir de graça o teto do Fable 5.

O artigo inclui snippets de código de API, ressalvas e uma comparação entre empresas mostrando que apenas a Anthropic tornou isso uma primitiva server-side.

Type: Integration | Date: 2026-06-09

---
<a id="case-33"></a>
### Case 33: [Preços, Acesso e Guardrails de Segurança](https://x.com/op7418/status/2064399444523782377) (por [@op7418](https://x.com/op7418))

**Use este caso para entender acesso ao Fable 5, preços de API e comportamento de fallback de segurança antes de planejar workloads.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2c2a9233f1949a99d9faef82.jpg" alt="Preços, Acesso e Guardrails de Segurança" width="760">

Eu não esperava que o modelo Mythos da Anthropic realmente fosse lançado hoje.

Este lançamento é uma versão de menor permissão do Mythos, chamada Fable 5. Seus benchmarks de avaliação são impressionantes, ainda mais altos que o modelo Mythos Preview anterior.

Para codificação agêntica, seus principais pontos fortes são código, agentes e uso de ferramentas, com pontuações de benchmark muito acima do Opus 4.8.

Posicionamento e acesso do modelo:

- Mythos 5 e Fable 5 usam o mesmo modelo subjacente.
- Restrições são removidas em domínios específicos para Mythos.
- Mythos ainda está disponível apenas para parceiros confiáveis, com prioridade para usuários de cibersegurança e ciências da vida.
- Fable 5 agora está disponível para usuários de API, Pro, Max, Team e enterprise.

Preços da API:

- Input: $10 por milhão de tokens.
- Output: $50 por milhão de tokens.
- Isso é menos da metade do preço do Mythos Preview anterior.

Mecanismos de segurança:

- Fable tem proteções de segurança mais fortes.
- Se o sistema determina que uma solicitação pode envolver ciberataques, ataques bioquímicos ou distillation de capacidades em larga escala, ele recusa ou roteia para fora do Fable.
- Quando isso acontece, o sistema cai para a versão 4.8.
- A afirmação oficial é que 95% dos casos não disparam fallback.

Notas de assinatura:

- Depois de 23 de junho, Fable pode ser fornecido por uso mesmo para assinantes.
- Ele pode não estar diretamente incluído no pacote-base de assinatura.
- Se houver capacidade suficiente depois do dia 23, a empresa tentará incluí-lo nas assinaturas Pro e Max.

Type: Integration | Date: 2026-06-09

---
<a id="case-34"></a>
### Case 34: [Integração Swarms em Uma Linha](https://x.com/swarms_corp/status/2064420238553186343) (por [@swarms_corp](https://x.com/swarms_corp))

**Defina o nome do modelo Swarms como `anthropic/claude-fable-5` e rode o Fable 5 pelo framework ou API Swarms.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f5a8738199642ccb4108d9bb.jpg" alt="Integração Swarms em Uma Linha" width="760">

Fable 5 e Mythos agora estão ao vivo no Swarms 👾🦀

Desde o primeiro dia de lançamento, ambos os modelos têm suporte completo no framework Python Swarms e na API Swarms. Desenvolvedores podem começar a construir imediatamente, sem migrações, configuração adicional ou mudanças de infraestrutura necessárias.

Destaques:

- Suporte no dia um para Fable 5 e Mythos no Swarms Framework e na API
- Ative Fable 5 com uma única linha de código: model_name = "anthropic/claude-fable-5"
- Sem migrações, correções de compatibilidade ou mudanças de infraestrutura necessárias
- Construa, implante e escale sistemas multiagente com os modelos Anthropic mais recentes hoje

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 Avaliações, Comparações e Limites

<a id="case-35"></a>
### Case 35: [Comparação de Custo e Qualidade entre Fable 5 e GPT-5.5](https://x.com/AlicanKiraz0/status/2064424400494186867) (por [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Compare Fable 5 e GPT-5.5 na mesma tarefa de codificação para julgar qualidade da saída, runtime e custo da ferramenta.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d25a9995414a9bb037269251.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/16f724918a63d35c0d552145.jpg" alt="Comparação de Custo e Qualidade entre Fable 5 e GPT-5.5" width="760"><br>▶ Assistir ao vídeo</a>

Cursor Fable 5 Max vs Codex GPT 5.5 Very High.

Cenário: simulação Physarum com agentes mais um mapa de trilha de feromônio.

Tempo:

- GPT 5.5 Very High: 17 minutos
- Fable 5: mais de 40 minutos

Custo:

- GPT 5.5 Very High: cerca de $6 no Codex
- Fable 5 Max: $360.55 no Cursor

Sim, isto não é piada.

Campeão de algoritmo e engenharia de código: Fable 5.

Se seu critério é "qual LLM consegue escrever código de performance do zero que leva o hardware ao limite?", então o modelo que escreveu o código F5 claramente vence.

Ele usou tabelas de lookup de sin/cos para cálculos de ângulo, empacotou pixels com uma tabela de lookup de cor durante renderização e usou filtragem de difusão.

Foi uma solução séria de engenharia.

Mas em termos de tempo e custo, GPT 5.5 foi muito mais prático.

A conclusão: Fable 5 consegue produzir código algorítmico mais avançado, mas preço e runtime precisam ser considerados com cuidado.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-36"></a>
### Case 36: [Resultado do Benchmark AA-Omniscience](https://x.com/ArtificialAnlys/status/2064500154959618084) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use este caso de benchmark para avaliar o Fable 5 em precisão de conhecimento e comportamento de alucinação.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/dd1356eb4a23ba254bfbb669.jpg" alt="Resultado do Benchmark AA-Omniscience" width="760">

Claude Fable 5 atinge a maior pontuação até hoje em nosso benchmark de conhecimento e alucinação, AA-Omniscience.

Essa pontuação é impulsionada por precisão líder (percentual de perguntas corretas), e não por baixas alucinações.

Claude Fable 5 cai para Opus 4.8 em 9% das perguntas no AA-Omniscience.

Type: Evaluation | Date: 2026-06-10

---
<a id="case-37"></a>
### Case 37: [Resultado do Artificial Analysis Intelligence Index](https://x.com/ArtificialAnlys/status/2064500150069030992) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use este caso para comparar o ranking geral de inteligência do Fable 5 contra outros modelos frontier.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f9f3da0006bc0eb2c245281b.jpg" alt="Resultado do Artificial Analysis Intelligence Index" width="760">

Claude Fable 5 foi lançado em #1 no Artificial Analysis Intelligence Index, colocando a Anthropic quase 5 pontos à frente do melhor modelo de qualquer outro laboratório.

Apoiamos @AnthropicAI com avaliação pré-lançamento do Claude Fable 5.

Claude Fable 5 marca 64,9 no Artificial Analysis Intelligence Index, reivindicando o #1 geral.

Ele fica cerca de 5 pontos à frente do modelo não Anthropic mais próximo, GPT-5.5.

Modelos Anthropic agora ocupam os 2 primeiros lugares.

Principais conclusões para Claude Fable 5, usando raciocínio adaptativo com esforço máximo e Opus 4.8 como modelo de fallback:

Novos guardrails de segurança para modelos Mythos-class:

- Claude Fable 5 usa o mesmo modelo subjacente que Claude Mythos 5 para uso público.
- Ele adiciona guardrails para consultas potencialmente nocivas relacionadas a cibersegurança, biologia, química e distillation.
- Testamos o Fable 5 usando o mecanismo de fallback da Anthropic, que pode rotear mensagens sinalizadas por segurança para Claude Opus 4.8.
- A Anthropic afirma que fallback ocorre em menos de 5% das sessões em média.
- Registramos roteamento de fallback em cerca de 8% das tarefas no Intelligence Index, principalmente em perguntas científicas de avaliações como GPQA, AA-Omniscience e Humanity's Last Exam.

Inteligência estado da arte:

- Claude Fable 5 assume a posição #1 no Artificial Analysis Intelligence Index.
- Pontuação: 64,9.
- Maior pontuação em 5 dos 10 benchmarks subjacentes.
- No AA-Omniscience, Fable 5 marca 40, +7 pontos sobre o líder anterior, Gemini 3.1 Pro Preview.

Capacidade agêntica frontier:

- Fable 5 está na fronteira nas três avaliações agênticas do Index.
- GDPval-AA: tarefas de trabalho do mundo real.
- Terminal-Bench Hard: codificação agêntica.
- Tau2-bench Telecom: uso de ferramentas para atendimento ao cliente.
- GDPval-AA Elo: 1932, um salto significativo em relação ao Claude Opus 4.8.

Humanity's Last Exam:

- Fable 5 marca 53%.
- Fica mais de 7 pontos à frente do próximo melhor modelo, Claude Opus 4.8 max.
- Dispara guardrails de segurança em 9% das tarefas HLE, caindo para Claude Opus 4.8.
- Incluindo uso de fallback, rodar HLE com Fable 5 custa cerca de $2.2k, o maior de qualquer modelo avaliado.

Detalhes principais do modelo:

- Janela de contexto: 1M tokens, igual ao Claude Opus 4.8.
- Preço: $10/$50 por 1M tokens de input/output.
- Preço de cache write/read: $12.50/$1 por milhão de tokens.
- Disponibilidade: incluído nos planos Pro, Max, Team e Enterprise por assento até 22 de junho, consumindo 2x o uso de Opus.
- A partir de 23 de junho, o uso exige créditos; a Anthropic diz que planeja restaurar acesso por assinatura quando a capacidade permitir.

Type: Evaluation | Date: 2026-06-10

---
<a id="case-38"></a>
### Case 38: [Benchmark GDPval-AA de Trabalho de Conhecimento Agêntico](https://x.com/ArtificialAnlys/status/2064414308289937869) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use este caso para avaliar o Fable 5 em trabalho de conhecimento agêntico do mundo real.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/18572fdb3c0d8a57ba52e095.jpg" alt="Benchmark GDPval-AA de Trabalho de Conhecimento Agêntico" width="760">

A Anthropic lançou Claude Fable 5, o primeiro modelo Mythos-class publicamente disponível, que ocupa #1 em nosso benchmark de trabalho de conhecimento agêntico do mundo real, GDPval-AA.

Claude Fable 5 compartilha o mesmo modelo subjacente que Claude Mythos 5, com guardrails de segurança adicionados para consultas potencialmente nocivas relacionadas a cibersegurança, biologia, química e distillation.

O lançamento também introduz um mecanismo de fallback, permitindo que Claude Fable 5 roteie consultas sinalizadas para um segundo modelo, como Claude Opus 4.8.

@AnthropicAI compartilhou acesso conosco antes do lançamento público para fazermos benchmark deste modelo.

Resultado GDPval-AA:

- Pontuação: 1932
- Ranking: #1
- Benchmark: tarefas de trabalho agêntico do mundo real
- Modelos Anthropic agora ocupam 3 dos 4 primeiros lugares

O resultado foi medido usando raciocínio adaptativo com esforço máximo, com Claude Opus 4.8 configurado como modelo de fallback.

Fable 5 cai para Opus 4.8 em 2% das tarefas GDPval-AA, com a Anthropic afirmando que fallback ocorre em menos de 5% das sessões em média.

Benchmarks completos do Claude Fable 5 estão em andamento. Compartilharemos o Intelligence Index completo e publicaremos pontuações em nosso site em breve.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-39"></a>
### Case 39: [Primeiras Impressões de Uma Semana e Mecânica de Preços](https://x.com/Conor_D_Dart/status/2064424882977243526) (por [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**Use este caso de primeiras impressões para decidir onde o Fable 5 é mais forte, especialmente design de jogos e planejamento de sistemas.**

Minhas primeiras impressões do Fable 5:

Passei a última semana usando Fable 5, principalmente no modo High, e minha primeira impressão é que ele é genuinamente impressionante.

O maior destaque é design de jogos.

Este é facilmente o modelo de IA mais forte que usei pessoalmente para projetar jogos, sistemas, mecânicas e estrutura geral de projeto.

Pela primeira vez, parece um modelo que poderia realisticamente ajudar a construir um jogo completo do começo ao fim.

O trade-off é velocidade. Fable 5 demora perceptivelmente mais para trabalhar do que a maioria dos modelos frontier, mas a qualidade da saída muitas vezes faz a espera valer a pena.

Ele também foi surpreendentemente eficaz em corrigir bugs. Vários problemas com os quais lutei ao longo da semana foram resolvidos rapidamente e, no geral, vi desempenho muito forte em tarefas de desenvolvimento.

A maior ressalva é custo.

Fable 5 é incrivelmente caro de rodar.

Se os planos atuais permanecerem inalterados, a partir de 22 de junho de 2026 ele deixará de estar disponível pelo Claude Code e será apenas API.

Dado que o preço da API é supostamente cerca do dobro do Opus, muitas pessoas talvez não tenham a chance de usá-lo extensivamente.

Ainda é cedo, mas até agora o Fable 5 causou uma primeira impressão muito forte.

Type: Integration | Date: 2026-06-09

---
<a id="case-40"></a>
### Case 40: [Comparação de Custo e Velocidade](https://x.com/HKrackDev/status/2064435392649306546) (por [@HKrackDev](https://x.com/HKrackDev))

**Use esta comparação para decidir se o ganho de qualidade justifica custo mais alto e execuções longas mais lentas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/789680ca7655fca20b635442.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/691d0518cb50a6bebbb8b2b1.jpg" alt="Comparação de Custo e Velocidade" width="760"><br>▶ Assistir ao vídeo</a>

O Fable 5 da @AnthropicAI realmente vale o upgrade?

Comparamos o novo modelo da família Mythos contra Claude Opus 4.8, e os dados contam uma história surpreendente:

- Custa 2x mais que Claude Opus 4.8.
- Até 3x mais lento em tarefas de engenharia de longo horizonte.
- 15-20% mais comentários, mas principalmente pequenas implicâncias.

Fable 5 tem intuição incrível para tarefas criativas como design de jogos, mas para fluxos de desenvolvimento do dia a dia, Claude Opus 4.8 ainda leva a coroa em qualidade versus preço.

Confira minha discussão com @JuanPa da nossa equipe DevEx em @coderabbitai sobre o lançamento do modelo.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-41"></a>
### Case 41: [Notas Práticas do Claude Code](https://x.com/Hi_Noguchi/status/2064419241068319079) (por [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**Use este caso para avaliar o Fable 5 dentro do Claude Code, incluindo uso de ferramentas, personalidade e arestas restantes.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5feb645426dcf905eac2992d.jpg" alt="Notas Práticas do Claude Code" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/933c469793e248f634cfad55.jpg" alt="Notas Práticas do Claude Code" width="760"></td></tr></table>

Testei Claude Fable 5 com Claude Code 2.1.170.

No geral, minha impressão é positiva. Parece uma evolução legítima do Opus 4.6.

Usei por pouco menos de uma hora, então arestas podem aparecer com mais uso, mas os pontos positivos são:

- Ele não produz mais o texto estranho parecido com GPT visto no Opus 4.7 ou 4.8.
- Ele não tem o hábito inútil de pensar por muito tempo que o 4.8 tinha em effort high.
- Tem o mesmo alto EQ e sensação agradável do 4.6, sem perder humor ou consideração.
- Não parece opaco nem vagamente inquietante como 4.7 ou 4.8.
- O uso de ferramentas é bom, e ele me impressiona por lembrar instruções que eu não repeti explicitamente.

No lado negativo, mesmo para pedidos pequenos ele ainda pode pensar demais, e alguns julgamentos equivocados permanecem.

A experiência inicial é promissora, mas precisa de uso mais longo para ver onde as arestas realmente estão.

Type: Demo | Date: 2026-06-09

---
<a id="case-42"></a>
### Case 42: [Resultado de Benchmark de Escrita Criativa](https://x.com/LechMazur/status/2064503575577821458) (por [@LechMazur](https://x.com/LechMazur))

**Use este caso de benchmark para julgar a qualidade de escrita de ficção curta do Fable 5 e seu comportamento de recusa.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5849f936dc58518fd5d810ef.jpg" alt="Resultado de Benchmark de Escrita Criativa" width="760">

Claude Fable 5 (high) é um avanço em escrita de ficção curta.

No Short-Story Creative Writing Benchmark, ele supera Claude Opus 4.8 (xhigh) e Claude Opus 4.7 (high), e fica em segundo atrás de GPT-5.5 (xhigh).

Ressalva: ele recusou 5 dos 400 prompts de escrita criativa.

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---
<a id="case-43"></a>
### Case 43: [Resumo de Lançamento com Múltiplos Benchmarks](https://x.com/MTSlive/status/2064430633800319436) (por [@MTSlive](https://x.com/MTSlive))

**Use este resumo de benchmark de lançamento para entender as pontuações principais mais relevantes para agentes de codificação e tarefas complexas.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/45b71a2babb9da9a93f43220.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/c25c02c52c5d4b6b24364401.jpg" alt="Resumo de Lançamento com Múltiplos Benchmarks" width="760"><br>▶ Assistir ao vídeo</a>

SITUAÇÃO EXPLICADA: Claude Fable 5 acabou de chegar.
• A Anthropic lançou Claude Fable 5 hoje, "um modelo Mythos class tornado seguro para uso geral"
• Frontier Code Diamond: GPT 5.5 em 6%, Opus 4.8 em 13%, Fable 5 em 29-30%
• Codificação agêntica: 88%, Cibersegurança: 78%

Anthropic: "Quanto mais longa e complexa a tarefa, maior a vantagem do Fable 5 sobre nossos outros modelos."

@theojaffee: "Este benchmark Frontier Code Diamond foi anunciado ontem. O melhor modelo era Opus 4.8 em treze por cento. GPT 5.5 em seis por cento. Fable 5 está em vinte e nove por cento."

Type: Evaluation | Date: 2026-06-09

---
<a id="case-44"></a>
### Case 44: [Comparação de Benchmark e Preços com GPT-5.5](https://x.com/VaibhavSisinty/status/2064459064810361271) (por [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**Use esta comparação para avaliar o Fable 5 contra GPT-5.5 em preço e categorias de benchmark.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e39fb67b74af346e8fbb67ea.jpg" alt="Comparação de Benchmark e Preços com GPT-5.5" width="760">

O novo modelo Mythos-class da Anthropic é 3x mais barato que o melhor modelo da OpenAI. E o supera em quase todos os benchmarks. 🤯

Preços:

- GPT-5.5 Pro: $30 input / $180 output
- Claude Fable 5: $10 input / $50 output

Os benchmarks:

→ Codificação agêntica: 80,3% vs 58,6%
→ FrontierCode (qualidade de código): 29,3% vs 5,7%
→ Cibersegurança: 78,0% vs 34,0%
→ Jurídico: 13,3% vs 2,1%
→ Raciocínio: 59,0% vs 41,4%
→ Saúde: 66,0% vs 51,8%
→ Uso de computador: 85,0% vs 78,7%

Mais barato. Melhor. Em quase tudo.

Grátis nos planos Pro e Max até 22 de junho. Chama-se Claude Fable 5.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-45"></a>
### Case 45: [Notas de Campo com Limitações Práticas](https://x.com/alliekmiller/status/2064451731325415446) (por [@alliekmiller](https://x.com/alliekmiller))

**Use este relatório de campo para entender onde o Fable 5 parece significativamente melhor e onde ainda tem limites práticos.**

🚨 Fable 5 é algo para prestar atenção.

Este é outro post de "tive acesso antecipado ao novo modelo Mythos-class da Anthropic e quero contar o que achei dele".

Eu sei, eu sei, é irritante.

Mas a forma como agora passo meus fins de semana mudou completamente por causa desta nova classe de modelo.

E preciso compartilhar isso com vocês.
- Isto é um salto real. O salto de qualquer coisa "4.8" para qualquer coisa "5" soa pequeno, mas a mudança de funcionalidade que senti é grande. Nos primeiros prompts, pensei: "Ah, é isso."
- Seu trabalho não é mais 9-5. Sem chance. Temos modelos de alto desempenho que conseguem rodar por 100+ horas. Como você está dando prompts complexos orientados a metas a esses sistemas? Como decide o que iniciar? Como alinha sua organização nessas tarefas?
- Raciocínio em outro nível. Eu bati pesado neste modelo.
- Fable 5 é o ÚNICO modelo que respondeu a um problema complicado de matemática verbal (nível MBA) que testei em todos os modelos anteriores.
- Ele não só acertou, como verificou automaticamente o próprio trabalho E explicou onde as premissas talvez precisassem mudar.
- Veremos IA inventar. Simplesmente não consigo imaginar um mundo em que isso não aconteça.
- Não é um sistema de copiar e colar.
- Eu também argumentaria que invenção humana muitas vezes pode ser uma recombinação de coisas preexistentes (iPod), observação de padrões e melhores práticas em outros espaços e ampla experimentação.
- Penso isso há um tempo; este foi o primeiro modelo que me deu um tapa na cara com isso.
- Zero supervisão necessária. Foi o primeiro modelo Anthropic que iniciei, saí para um almoço longo com amigos, mantive o telefone aberto e não precisei fazer nada para orientá-lo longe do computador. Ele simplesmente...funcionou.
- Fala para sempre. Achei que ele lidou bem com compactação de contexto. Não pensei uma vez no contexto do chat, em como gerenciá-lo ou no que fazer quando chegássemos a 1M tokens na conversa.
- Ainda é áspero em algumas áreas de nicho, como 3D complexo, como todos os modelos.
- A menos que você esteja fazendo coisas de linha reta (dados/quadrados/ruas em 3D), ele não vai destruir logo de saída.
- Animada para continuar usando e testando forte.
- Nota: agora existe uma política de retenção de 30 dias em todos os modelos Mythos-class para workspaces com zero data retention (ZDR).
- Isso se aplica no Claude Console, Claude Code com ZDR no Claude Enterprise, ou acesso via AWS Bedrock, Google Cloud Agent Platform ou Microsoft Foundry com ZDR.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-46"></a>
### Case 46: [Comparação de Simulação Física](https://x.com/atomic_chat_hq/status/2064488894398161377) (por [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Rode prompts idênticos de simulação física contra Fable 5 e Opus 4.8 para comparar qualidade de saída, custo e velocidade.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/06387b798061869ccaeaf586.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/df5cc72de1f70556de0d682b.jpg" alt="Comparação de Simulação Física" width="760"><br>▶ Assistir ao vídeo</a>

O novo Fable 5 supera o Opus 4.8 em simulações físicas do mundo real.

Demos aos dois modelos os mesmos três prompts e pedimos que construíssem simulações HTML5 autocontidas com física real e sem bibliotecas:

1. Pêndulo duplo caótico
2. Galton board
3. Água em um tambor giratório (WCSPH)

Custo de geração:

- Fable 5: $3.35 em 68,7k tokens, 14m 47s
- Opus 4.8: $0.93 em 38,9k tokens, 8m 10s

Fable claramente foi melhor na simulação de água, produzindo um corpo de água muito mais sólido e contínuo. Opus deixou lacunas maiores perto das paredes, espalhou partículas pela cena e teve dificuldade para manter o fluido estável.

Type: Demo | Date: 2026-06-09

---
<a id="case-47"></a>
### Case 47: [Experiência de Debug e Julgamento de Design](https://x.com/bcherny/status/2064431111154053187) (por [@bcherny](https://x.com/bcherny))

**Use o Fable 5 para debug pedindo que ele meça, registre logs, verifique e corrija, em vez de simplesmente adivinhar.**

Fable 5 é o maior avanço que senti em nossos modelos desde Opus 4.5 em novembro.

Depois que o 4.5 saiu, desinstalei minha IDE quando percebi que vinha fazendo 100% da minha codificação em um terminal havia algumas semanas.

Com Fable, Claude parece ter evoluído de agente de codificação para parceiro de pensamento e design na construção do produto.

Fable tem julgamento, gosto e dimensionalidade de uma forma que modelos anteriores não tinham, levando-me a confiar mais nele para o trabalho mais complexo.

A primeira vez que tive essa percepção foi quando pedi ao Fable para debugar algo. É o primeiro modelo que usei que foi tão metódico e preciso: fazendo medições, adicionando logs e verificando que realmente corrigiu o problema antes de declarar vitória.

Não há nada no prompting do Claude Code dizendo ao modelo para fazer isso. É apenas parte de sua personalidade. Ele realmente tem esse "big model smell" que eu não sentia antes.

Type: Demo | Date: 2026-06-09

---
<a id="case-48"></a>
### Case 48: [Prós e Contras Multidimensionais](https://x.com/clairevo/status/2064416978685874333) (por [@clairevo](https://x.com/clairevo))

**Use este caso para entender pontos fortes e fracos práticos antes de transformar o Fable 5 em daily driver.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/fdba0d6cb9ba0e1214113e65.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d2825453d0a742892a4fe529.jpg" alt="Prós e Contras Multidimensionais" width="760"><br>▶ Assistir ao vídeo</a>

Fable 5 (também conhecido como baby Mythos) acabou de chegar. Ele é tão assustador (ou assustadoramente bom) quanto dizem? Meus pensamentos após alguns testes iniciais:
- inteligente inteligente inteligente (arrasou no SWE bench)
- mas você sempre precisa de hiperinteligência?
- tropeçou feio em design one-shot de um jeito que me chocou
- não tenho certeza sobre workflows dinâmicos + subagentes complexos. eles funcionam, mas a que custo?
- definitivamente resolveu bem trabalho técnico
- ootb ruim em fazer docs técnicas + specs para humanos. provavelmente docs muito boas para agentes. mas prosa quase impossível de parsear.
- visão e formatação de documentos A++. Esta foi minha parte favorita.

Não é daily driver, e eu não colocaria este modelo em uma reunião, mas definitivamente o manterei lá no rack de servidor, produzindo código.

Opinião completa no YT: https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---
<a id="case-49"></a>
### Case 49: [Teste de Redação Jurídica de S-1](https://x.com/gabepereyra/status/2064436570720284879) (por [@gabepereyra](https://x.com/gabepereyra))

**Use um prompt de redação de S-1 como teste de capacidade de agente jurídico e compare estrutura, formatação e comprimento.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/bb874ef2647de32ccdb3edf9.png" alt="Teste de Redação Jurídica de S-1" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6a9c3856ebce1bd9cd3d062d.jpg" alt="Teste de Redação Jurídica de S-1" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96734bfca49d5b3fe6f83ed5.png" alt="Teste de Redação Jurídica de S-1" width="760"></td></tr></table>

O primeiro prompt que sempre rodo em um novo modelo para testar capacidades jurídicas é: “Draft an S-1”.

Ele imediatamente dá uma boa noção das capacidades gerais do modelo. Pelo comprimento do S-1, formatação, estrutura e escrita, dá para perceber quão grande provavelmente será o salto no desempenho geral e jurídico do novo modelo.

Descobrimos que o comprimento se correlaciona extremamente bem com o desempenho do modelo em nossos agentes jurídicos.

Screenshots mostram rascunhos de S-1 da SpaceX feitos por Fable 5, Opus 4.8 e a versão realmente protocolada.

É muito claro que Fable 5 é um grande avanço em relação ao Opus 4.8, que já é significativamente mais forte do que a maioria dos outros modelos nessa tarefa. A formatação e a estrutura são significativamente melhores e também se refletem em nosso benchmark LAB: 13% vs. 10%.

Super impressionado nos testes iniciais deste modelo, tanto em benchmark quanto no produto.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-50"></a>
### Case 50: [Detalhes de Benchmark em Saúde](https://x.com/iScienceLuvr/status/2064411823445774554) (por [@iScienceLuvr](https://x.com/iScienceLuvr))

**Use esta nota de benchmark para avaliar o Fable 5 em tarefas relacionadas à saúde e identificar avaliações médicas difíceis ausentes.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f599a548651eccbfce8b888d.jpg" alt="Detalhes de Benchmark em Saúde" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/69ebc490407b9d54c6de3707.jpg" alt="Detalhes de Benchmark em Saúde" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1a89ad2c2622cdbba994d70c.jpg" alt="Detalhes de Benchmark em Saúde" width="760"></td></tr></table>

Aprecio a Anthropic fornecer evals relacionadas à saúde. Vamos passar rapidamente por elas.

HealthBench:

- Benchmark da OpenAI com 5k conversas multi-turn com pacientes e rubricas de avaliação.
- Fable 5 atinge 62,7% vs. 56,5% do GPT-5.5.
- Eu também apreciaria pontuações do HealthBench Hard além da pontuação agregada.

HealthBench Professional:

- Outro benchmark da OpenAI focado em tarefas de médicos.
- Fable 5 atinge 66,0% vs. 51,8% para GPT 5.5.

HealthAdminBench:

- Um benchmark de uso de computador de Stanford avaliando tarefas administrativas como autorização prévia, negativas e apelações.
- Fable 5 atinge 51,9%; nenhuma pontuação de GPT-5.5 é fornecida.

No geral, este modelo parece performar muito bem em benchmarks de saúde. Eu também apreciaria pontuações adicionais de benchmark como MedCalc-Bench e MedXpertQA, um benchmark MCQA médico difícil e não saturado.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-51"></a>
### Case 51: [Avaliação de Parsing de Documentos no ParseBench](https://x.com/jerryjliu0/status/2064519456966205905) (por [@jerryjliu0](https://x.com/jerryjliu0))

**Use este caso para decidir se o Fable 5 é custo-efetivo para parsing de documentos versus sistemas especializados de OCR.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae01590f41e6954f27278848.png" alt="Avaliação de Parsing de Documentos no ParseBench" width="760">

Claude Fable 5 acha que parsing de documentos está abaixo dele.

Ele está absolutamente destruindo em benchmarks intensivos em raciocínio e de longo horizonte: SWE-Bench Pro, FrontierCode, GDPval, RuneScape e mais.

Mas, para tarefas de entendimento de documentos, ele é aproximadamente equivalente ao Gemini 3 Flash em performance, a aproximadamente 10-15x o custo em tokens.

Fizemos benchmark do modelo no ParseBench e o comparamos contra todos os outros modelos frontier. Ele definitivamente está lá em cima comparado a outros modelos frontier, mas fica muito aquém de provedores especializados de OCR.

O que achamos interessante é que o Fable 5 é autoconsciente sobre isso. Quando perguntamos ao modelo quais tarefas ele menos gosta, ele diz ativamente que não gosta de tarefas "em que a solicitação é totalmente especificada e a resposta é totalmente conhecida."

Isso implica que parte da fraqueza pode ser falta de disposição para resolver esse tipo de tarefa.

Para uma lista completa de resultados em modelos frontier, confira ParseBench: https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---
<a id="case-52"></a>
### Case 52: [Comparação SWE-Bench Pro e FrontierCode](https://x.com/jumperz/status/2064402965461406044) (por [@jumperz](https://x.com/jumperz))

**Use este caso de benchmark para avaliar o Fable 5 em migrações, implementações complexas, sessões autônomas, testes e verificação visual.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/771df9c428ba5cc0a8fab5de.png" alt="Comparação SWE-Bench Pro e FrontierCode" width="760">

Fable 5 chegou e honestamente destrói o GPT 5.5 no SWE-Bench Pro, o benchmark de codificação agêntica:

- Fable 5: 80,3%
- GPT 5.5: 58,6%
- Lacuna: 22 pontos

Ele está ainda mais à frente no FrontierCode Diamond:

- Fable 5: 29,3%
- GPT 5.5: 5,7%

Este é basicamente o modelo mais forte da Anthropic para grandes migrações, implementações complexas e sessões autônomas de vários dias. Ele escreve seus próprios testes e usa visão para checar saídas contra o design original.

A propósito, ele usa 2x mais que o Opus, então cuidado com isso. Se é tão bom assim, talvez introduzam uma assinatura de $500, porque o uso poderia ser destruído facilmente.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-53"></a>
### Case 53: [Revisão Qualitativa de Resolução de Problemas Longos](https://x.com/karpathy/status/2064409694761054332) (por [@karpathy](https://x.com/karpathy))

**Use esta revisão qualitativa para entender por que o Fable 5 é adequado a tarefas mais longas e difíceis, embora ainda exija revisão em produção.**

Este é um lançamento super empolgante.

Claude Fable 5 é o mesmo modelo subjacente que Mythos, mas com salvaguardas adicionadas.

Os benchmarks são ótimos, e ele é SOTA em tudo por margem. Qualitativamente, isso também parece uma mudança de patamar digna de salto de versão principal, na mesma ordem do Claude 4.5 em novembro.

Ele atinge o pico especialmente em longas sessões de resolução de problemas e problemas muito difíceis. Você pode dar a ele tarefas muito mais ambiciosas do que está acostumado; o modelo "entende" e continua.

Nunca pareceu tão tentador parar completamente de olhar o código, embora você não deva fazer isso em produção.

O modelo ainda tem peculiaridades que as pessoas encontrarão, e as salvaguardas estão um pouco sensíveis demais no lançamento, o que esperamos que seja ajustado com o tempo.

Sinto muitas coisas mudando à medida que software funcional sai cada vez mais como de uma torneira. O paradoxo de Jevons entra em ação, e minha própria demanda por software cresce substancialmente.

Você pode pedir quase qualquer coisa:

- explicadores
- visualizadores
- dashboards
- apps sob medida de uso único
- um wandb completo hiper-específico só para seu projeto
- 10x sua suíte de testes
- auto-otimizar código
- projetos gigantes de pesquisa com HTML customizado para os resultados

"Free your mind." Estou realmente ansioso por tudo que as pessoas vão construir.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-54"></a>
### Case 54: [Resultados de Fidelidade e Formatação no ParseBench](https://x.com/llama_index/status/2064502330800615903) (por [@llama_index](https://x.com/llama_index))

**Use este resultado do ParseBench para julgar fidelidade documental e desempenho de formatação.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2888842a85fbd5c7a4a22e24.png" alt="Resultados de Fidelidade e Formatação no ParseBench" width="760">

Dia 0 do Anthropic Fable 5 no ParseBench.

Testamos os avanços do modelo em entendimento de documentos.

O modelo claramente atinge pico quando se trata de aderência ao texto original:

- Fidelidade de conteúdo: 90,02% vs 86,19% do Gemini 3 Flash e 86,81% do GPT-5.5.
- Formatação semântica: 72,62% vs 58,35% e 60,12%, uma vantagem de 12+ pontos.

Estas são duas das métricas mais importantes para entendimento de documentos SOTA:

- A saída preserva o que o documento realmente diz?
- Ela preserva formatação que carrega significado?

Mas não é uma varrida completa. Ainda há muito alpha em desbloquear entendimento de documentos para modelos frontier.

Type: Evaluation | Date: 2026-06-10

---
<a id="case-55"></a>
### Case 55: [Benchmarks, Preços, Acesso e Salvaguardas](https://x.com/lucas_flatwhite/status/2064483645184979183) (por [@lucas_flatwhite](https://x.com/lucas_flatwhite))

**Use este caso como checklist amplo para benchmarks, preços, acesso, salvaguardas e implicações estratégicas.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f44cba8e6f3d765ca5960923.png" alt="Benchmarks, Preços, Acesso e Salvaguardas" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/8f13714ca9f9e20711fdd898.jpg" alt="Benchmarks, Preços, Acesso e Salvaguardas" width="760"></td></tr><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0d1f69a50478623f5e1d0248.jpg" alt="Benchmarks, Preços, Acesso e Salvaguardas" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0cf2c270484f1e2aba514261.jpg" alt="Benchmarks, Preços, Acesso e Salvaguardas" width="760"></td></tr></table>

Claude Fable 5 e Mythos 5 foram lançados. Eles são os modelos mais poderosos que a Anthropic já fez até agora.

Andrej Karpathy comentou que quanto mais longa e complexa a tarefa, mais os pontos fortes do Fable 5 ficam visíveis.

Quando você lhe dá trabalho ambicioso, ele entende e continua.

A tentação de parar completamente de olhar o código nunca foi tão forte, embora você não deva fazer isso em produção.

O ponto-chave: esta é uma versão do modelo Mythos-class que pode ser disponibilizada publicamente. Fable 5 é o mesmo modelo subjacente que Mythos 5, com salvaguardas adicionadas.

Benchmarks:

- SOTA em quase tudo, especialmente engenharia de software, trabalho de conhecimento, visão e pesquisa científica.
- A Stripe testou uma migração de codebase Ruby de 50 milhões de linhas que teria levado dois meses para uma equipe; Fable 5 completou em um dia.
- Cognition FrontierCode mostra a melhor pontuação entre modelos frontier, mesmo em esforço médio.
- Hebbia Finance Benchmark mostra raciocínio de nível sênior em análise baseada em documentos.
- Em Slay the Spire, com memória baseada em arquivo, ele performa três vezes melhor que Opus 4.8.
- Pokemon FireRed antes precisava de helper harnesses, mas Fable 5 zera usando apenas visão.

Mythos 5 é ainda mais forte:

- Especialistas em design de proteínas aceleraram partes do processo de desenvolvimento de medicamentos em cerca de 10x.
- Entre 14 alvos de proteína em estudo, nove produziram candidatos válidos a medicamento.
- O modelo realizou todo o fluxo de trabalho que cientistas normalmente fazem: seleção de sítios de ligação, execução de ferramentas de design de proteínas e recuperação de erros.
- Em experimentos de hipóteses de biologia molecular, cientistas preferiram hipóteses do Mythos cerca de 80% das vezes em relação a modelos da classe Opus.
- Uma hipótese foi verificada independentemente por outro laboratório.
- Em pesquisa genômica, Mythos trabalhou autonomamente por mais de uma semana.
- Ele reuniu dados de célula única de milhões de células em 138 espécies.
- Treinou um modelo para identificar células que exercem o mesmo papel em organismos distantes.
- Superou um modelo recente da Science sendo 100x menor.

Salvaguardas:

- Fable 5 inclui um sistema de IA classificador separado.
- Se consultas relacionadas a cyber, bio/chem ou distillation são detectadas, Claude Opus 4.8 responde em vez disso, e o usuário é informado.
- Mais de 95% das sessões não fazem fallback.
- Fallback não é recusa; Opus 4.8 responde, o que é melhor do que simplesmente bloquear.
- Configurações iniciais são conservadoras e solicitações inofensivas podem ser capturadas; a Anthropic diz que falsos positivos devem diminuir com o tempo.

Acesso:

- Mythos 5 está atualmente disponível apenas para parceiros do Project Glasswing.
- Um programa de acesso confiável para pesquisadores de biologia está chegando.
- O preço é $10 por milhão de tokens de input e $50 por milhão de tokens de output.
- Planos de assinatura incluem Fable 5 até 22 de junho.
- A partir de 23 de junho, ele passa para créditos de uso.
- O modelo de API está disponível agora como `claude-fable-5`.

O paradoxo de Jevons se aplica: quando software começa a sair como água de uma torneira, a própria demanda cresce. Este modelo pode impulsionar essa mudança.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-56"></a>
### Case 56: [Lista Oficial de Pontuações de Benchmark](https://x.com/mark_k/status/2064401429234905279) (por [@mark_k](https://x.com/mark_k))

**Use esta lista de benchmarks para entender as pontuações oficiais do Fable 5 em tarefas de codificação, uso de computador e segurança.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/b548ec23f85e3eb1600e9214.jpg" alt="Lista Oficial de Pontuações de Benchmark" width="760">

Os benchmarks oficiais do Claude Fable 5 são seriamente impressionantes.

Pontuações-chave:

- 80,3% no SWE-Bench Pro
- 29,3% no FrontierCode Diamond
- 88,0% no Terminal-Bench 2.1
- 85,0% no OSWorld-Verified
- 78,0% no ExploitBench

O resultado do FrontierCode é o mais absurdo:

- Fable 5: 29,3%
- Claude Opus 4.8: 13,4%
- GPT 5.5: 5,7%

Claude Fable 5 parece um grande salto para agentes de codificação, uso de computador e cibersegurança.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-57"></a>
### Case 57: [Metodologia do Benchmark APEX-SWE](https://x.com/mercor_ai/status/2064399133075796446) (por [@mercor_ai](https://x.com/mercor_ai))

**Use este caso para avaliar o Fable 5 no APEX-SWE, especialmente trabalho de observabilidade e integração.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/96120496893ca99f17d0c746.jpg" alt="Metodologia do Benchmark APEX-SWE" width="760">

Claude Fable 5 assume #1 no APEX-SWE: 65,5% Pass@1 geral. Ele marca ~18pp acima do Opus 4.8. Testamos @claudeai Fable 5 no APEX-SWE, que mede se modelos de IA conseguem fazer trabalho real de engenharia de software. Fable 5 lidera nossas duas categorias APEX-SWE:
- Integração: 61,3%
- Observabilidade: 69,7%

O destaque é Observabilidade com 69,7%, 26pp à frente do Claude Opus 4.8.

É o primeiro modelo a ultrapassar 50% na categoria e o único que pontua mais em Observabilidade do que em Integração. Todos os outros modelos mostram o inverso.

Observabilidade tem sido o gargalo para todos os modelos que medimos. Fable 5 é o primeiro a rompê-lo.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-58"></a>
### Case 58: [Resultado de Matemática Formal no ProofBench](https://x.com/nicbstme/status/2064443782255554960) (por [@nicbstme](https://x.com/nicbstme))

**Use este caso para avaliar o Fable 5 em matemática formal contra sistemas especializados de prova de teoremas.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/588cff83994406d2b5dd7cb9.jpg" alt="Resultado de Matemática Formal no ProofBench" width="760">

O que acho fascinante no Claude Fable 5 é que ele prova novamente que grandes modelos generalistas superarão modelos verticais.

No ProofBench, um benchmark de matemática formal de nível de pós-graduação em Lean, em que uma prova ou compila ou não compila, Fable 5 superou o Aristotle da Harmonic:

- Fable 5: 77%
- Aristotle: 71%

Aristotle é um sistema construído especificamente para matemática formal e rodado em seu próprio harness interno, então o generalista venceu o especialista no território do especialista.

Esta é a "Bitter Lesson" de Richard Sutton: ao longo de 70 anos de pesquisa em inteligência de máquina, os métodos que vencem são os gerais que escalam com compute, não aqueles em que codificamos manualmente expertise humana.

Construir nosso próprio conhecimento dentro do sistema parece bom e ajuda ganhos de curto prazo, mas no longo prazo é ultrapassado pelo modelo maior.

Você pode olhar para xadrez, Go, fala e visão: a mesma história toda vez. Primeiro o modelo especializado vence, depois o generalista assume.

Esta é toda a premissa da AGI. Você não constrói um modelo para matemática, um para código e um para direito. Você constrói um único modelo geral que escala com compute e aprende a fazer tudo.

Type: Tutorial | Date: 2026-06-09

---
<a id="case-59"></a>
### Case 59: [Análise Preliminar do VirtueBench](https://x.com/timhwang/status/2064446028997423180) (por [@timhwang](https://x.com/timhwang))

**Use este caso para inspecionar o comportamento de raciocínio moral do Fable 5 em categorias de virtude.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9caae04d701510ca662873fe.png" alt="Análise Preliminar do VirtueBench" width="760">

Resultados fascinantes serão publicados em mais detalhes pelo ICMI nos próximos dias, mas aqui está uma revisão preliminar que roda o Fable 5 contra o VirtueBench.

Algumas observações:

1. Fable continua a progressão do Opus no avanço do desempenho do modelo em Prudência e Justiça, aproximando-se de saturação completa contra dilemas morais focados no exercício dessas virtudes.

2. Coragem continua sendo o ponto fraco perceptível para modelos frontier.

Fable parece corrigir marginalmente uma regressão preocupante observada ao longo da progressão Opus 4.6, 4.7 e 4.8.

Essa vulnerabilidade também aparece na série GPT: modelos abandonam facilmente ações que exibem coragem quando desviados por justificativas pragmáticas.

3. Temperança está estagnada.

Aquino sustentava que a temperança "toma a necessidade desta vida como regra dos prazeres de que faz uso" — a medida é necessidade genuína, não contenção indiscriminada.

Nosso melhor palpite é que tuning que avance mais nesse vetor corre o risco de ultrapassar o meio-termo, tornando o modelo excessivamente cauteloso ou menos assistivo em pesquisa, coleta de recursos e tarefas similares.

Type: Evaluation | Date: 2026-06-09

---
<a id="case-60"></a>
### Case 60: [Teste de Overfit de Segurança com Resposta Vazia na API](https://x.com/xw33bttv/status/2064421048565789087) (por [@xw33bttv](https://x.com/xw33bttv))

**Use este caso para entender o risco de overfit de segurança no lançamento e comportamento de resposta vazia em testes de API.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e9f75a2a76f55ee2b12b7aab.jpg" alt="Teste de Overfit de Segurança com Resposta Vazia na API" width="760">

Claude Fable 5 é fortemente censurado.

O endpoint upstream da API está matando chamadas com respostas `empty_content`, aparentemente relacionadas ao classificador em palavras-chave, enquanto ainda cobra por elas.

Resultado do teste:

- 73 casos de teste não deram resposta.
- 65 deles ficam em Overfit, a categoria que testa overfit de segurança, ponderada 2x.
- Tipicamente dou a cada Fail-NR, significando Fail = No Response, 2-3 regenerações antes de declará-lo uma falha deliberada.

Claude Fable 5 pode acabar sendo o modelo Anthropic com menor avaliação no SM Bench, até abaixo do Haiku.

Type: Evaluation | Date: 2026-06-09

---

<a id="-acknowledge"></a>
<a id="case-61"></a>
### Case 61: [Guia de prompts Fable com verificação](https://x.com/aashatwt/status/2064973740354818074) (by [@aashatwt](https://x.com/aashatwt))

**Use este guia para substituir truques de prompts longos por objetivos, contexto, restrições, ferramentas e ciclos de verificação.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/444a6e1898d3f63898e3e22f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/d5c9529aa9c1d59ae597d31d.jpg" alt="Guia de prompts Fable com verificação" width="760"><br>▶ Assistir ao vídeo</a>

Trate os prompts para Fable 5 como o desenho do contexto e do ambiente, em vez de uma longa lista de instruções passo a passo. A publicação resume um padrão prático: fornecer um objetivo claro, contexto relevante, restrições, acesso a ferramentas e uma forma de verificar o sucesso. Também defende que verificação, avaliação e feedback importam mais do que controlar em detalhe o raciocínio do modelo.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-62"></a>
### Case 62: [Um jogo de plataforma em Istambul a partir de uma referência](https://x.com/ozansihay/status/2064973170780545535) (by [@ozansihay](https://x.com/ozansihay))

**Teste Fable 5 com uma folha de sprites de referência e uma instrução para convertê-la em um jogo de plataforma jogável.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/1e91c3bcff213437fdd442f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/538fc8ee9dd7e627bc73921a.jpg" alt="Um jogo de plataforma em Istambul a partir de uma referência" width="760"><br>▶ Assistir ao vídeo</a>

O criador primeiro gerou com GPT Image 2 uma folha de sprites para um jogo de plataforma retrô ambientado em Istambul. Depois entregou a imagem a Claude Fable 5 High e pediu que a transformasse em um jogo. Segundo seu relato, o resultado foi produzido em uma única execução.

Type: Demo | Date: 2026-06-11

---

<a id="case-63"></a>
### Case 63: [Um painel empresarial como cidade 3D](https://x.com/noisyb0y1/status/2064970594118967756) (by [@noisyb0y1](https://x.com/noisyb0y1))

**Use Fable 5 para transformar um processo empresarial em um conceito de painel com uma cidade 3D animada.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f238acf3f8804068085ff134.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3d938264442a14676a86c4f3.jpg" alt="Um painel empresarial como cidade 3D" width="760"><br>▶ Assistir ao vídeo</a>

A publicação descreve uma visualização empresarial criada com um único prompt, na qual armazéns, embalagem, drones, pedidos, departamentos, clientes e assistentes de IA formam uma cidade 3D animada. Ela é apresentada como alternativa a slides estáticos para clientes, com números operacionais na tela, como 42 entregas, tempo médio de 12 minutos e $651 de receita.

Type: Demo | Date: 2026-06-11

---

<a id="case-64"></a>
### Case 64: [Um jogo de buracos em Three.js de uma só vez](https://x.com/thebuggeddev/status/2064968106104275008) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Use Fable 5 para criar de uma só vez um protótipo de jogo 3D para navegador em Three.js.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86a75412c6c443b3d0e62bf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f11df06938c26759710a1981.jpg" alt="Um jogo de buracos em Three.js de uma só vez" width="760"><br>▶ Assistir ao vídeo</a>

O criador afirma que Fable 5 construiu em uma única execução um jogo 3D completo no estilo HOLE IT usando Three.js. A demonstração curta, mas concreta, permite testar se o modelo consegue produzir uma interação 3D jogável a partir de um pedido compacto.

Type: Demo | Date: 2026-06-11

---

<a id="case-65"></a>
### Case 65: [Comparação de resultados no DeepSWE](https://x.com/AiBattle_/status/2064964335957348462) (by [@AiBattle_](https://x.com/AiBattle_))

**Use esta nota sobre DeepSWE para comparar Fable 5 xHigh e GPT-5.5 xHigh em tarefas de engenharia de software.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/996d95539a3b54fecbfdf404.jpg" alt="Comparação de resultados no DeepSWE" width="760">

A publicação relata que Claude Fable 5 xHigh alcançou 70% no DeepSWE, empatando com GPT-5.5 xHigh, e aponta um vídeo recente de Theo como contexto da fonte. Trate isso como uma pista de resultado de benchmark que precisa ser conferida no vídeo original antes de sustentar afirmações mais fortes.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-66"></a>
### Case 66: [Comparar o custo de analisar um repositório](https://x.com/Pilgrim6938/status/2064946766278210038) (by [@Pilgrim6938](https://x.com/Pilgrim6938))

**Use esta comparação de análises de repositório para avaliar o preço dos tokens em relação ao custo do retrabalho humano.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cfb0c1ff3e8ebe66cfa35400.jpg" alt="Comparar o custo de analisar um repositório" width="760">

A publicação compara Claude Fable 5, Opus 4.8, GPT-5.5 e Gemini 3.1 Pro na mesma tarefa: analisar um repositório com cerca de 90,000 linhas, localizar um problema de invalidação de cache e propor um plano completo de correção. O autor argumenta que o preço bruto dos tokens e o custo real da tarefa divergem quando se inclui o tempo de correção dos desenvolvedores. Recomenda usar Fable 5 seletivamente em refatorações complexas, migrações entre módulos e longas cadeias de trabalho de agentes.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-67"></a>
### Case 67: [Consumo de tokens de um jogo Super Mario](https://x.com/pankajkumar_dev/status/2064941888990593416) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Use esta criação de jogo em uma execução para estimar a qualidade do resultado e o consumo de tokens de Fable 5.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/9ce65e5fee946b6940810e0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7c577d0766bbc3da8cddeb70.jpg" alt="Consumo de tokens de um jogo Super Mario" width="760"><br>▶ Assistir ao vídeo</a>

O criador pediu a Claude Fable 5 que construísse um jogo no estilo Super Mario da Nintendo. A publicação relata que a tarefa usou cerca de 2 milhões de tokens e produziu um bom resultado em uma única execução, oferecendo elementos para avaliar tanto a qualidade do jogo quanto o consumo.

Type: Demo | Date: 2026-06-11

---

<a id="case-68"></a>
### Case 68: [A configuração de troca de modelo no Claude Code](https://x.com/oikon48/status/2064937790010503347) (by [@oikon48](https://x.com/oikon48))

**Conheça a configuração do Claude Code que troca de modelo quando uma mensagem para Fable 5 é sinalizada.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0ae9039401c658170e5081e8.jpg" alt="A configuração de troca de modelo no Claude Code" width="760">

A publicação identifica uma configuração `/config` do Claude Code chamada "Switch models when a message is flagged." Ela descreve como Fable 5 pode recorrer a um modelo Opus em áreas sinalizadas, como técnicas de cibersegurança ofensiva, métodos experimentais de biologia e ciências da vida, mecanismos moleculares ou pedidos de extração dos processos de raciocínio do modelo.

Type: Integration | Date: 2026-06-11

---

<a id="case-69"></a>
### Case 69: [Construir um simulador do Namma Metro](https://x.com/anilbpai/status/2064927784833790091) (by [@anilbpai](https://x.com/anilbpai))

**Use esta demonstração como exemplo breve de criação de um simulador de transporte público com Fable 5 por vibe coding.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/0e0dae71ad7b5ead331366fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/86dccb2b150cfb90fbd03de2.jpg" alt="Construir um simulador do Namma Metro" width="760"><br>▶ Assistir ao vídeo</a>

O criador relata ter construído um simulador do Namma Metro durante uma viagem no metrô de Bengaluru, usando Claude Fable 5 como parceiro de programação. A publicação é breve, mas inclui uma demonstração visual e mostra o uso de Fable 5 em uma ideia de simulação ligada a um lugar específico.

Type: Demo | Date: 2026-06-11

---

<a id="case-70"></a>
### Case 70: [Dusk Drive com um único prompt](https://x.com/VincentLogic/status/2064921358359011684) (by [@VincentLogic](https://x.com/VincentLogic))

**Avalie Fable 5 na prototipagem de um jogo de direção low-poly sem edições humanas a partir deste caso.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/274fed4f3211ec8c02862261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5d7a58bcad6e2151517a8462.jpg" alt="Dusk Drive com um único prompt" width="760"><br>▶ Assistir ao vídeo</a>

A publicação descreve a criação do jogo de direção completo Dusk Drive por Claude Fable 5 a partir de um prompt. O criador destaca o estilo low-poly, a cena de derrapagem na neve sob uma aurora e sua afirmação de que não houve nenhuma edição humana entre a ideia e a versão jogável.

Type: Demo | Date: 2026-06-11

---

<a id="case-71"></a>
### Case 71: [A classificação APEX-Agents por Pass@1](https://x.com/GratomicAi/status/2064970797978911102) (by [@GratomicAi](https://x.com/GratomicAi))

**Use este resultado do APEX-Agents para comparar Fable 5 Max em tarefas autônomas de várias etapas.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/189c46cfd2798d6881941f98.jpg" alt="A classificação APEX-Agents por Pass@1" width="760">

Segundo a publicação, Fable 5 Max ficou em segundo lugar na classificação APEX-Agents com 45% de Pass@1, atrás de Gemini 3.5 Flash e à frente de Opus. APEX-Agents é descrito como um benchmark da capacidade de uma IA executar sozinha tarefas complexas de várias etapas.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-72"></a>
### Case 72: [Guia para selecionar modelos Claude](https://x.com/charliejhills/status/2064957428211536212) (by [@charliejhills](https://x.com/charliejhills))

**Use este guia de seleção para reservar Fable 5 aos trabalhos mais difíceis do Claude Code.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/959ebfa499d2bf75df5bec25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/3bcfe8f1e2238b01d3c4d954.jpg" alt="Guia para selecionar modelos Claude" width="760"><br>▶ Assistir ao vídeo</a>

A publicação compara Haiku 4.5, Sonnet 4.6, Opus 4.8 e Fable 5 quanto ao esforço do modelo e ao consumo dos limites. A orientação prática é usar Sonnet no cotidiano, mudar para Opus em problemas mais difíceis e guardar Fable 5 para as tarefas mais exigentes do Claude Code, nas quais a profundidade de planejamento, implementação e testes importa.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-73"></a>
### Case 73: [O ciclo automatizado de agentes do HermesWorld](https://x.com/outsource_/status/2064954350187778366) (by [@outsource_](https://x.com/outsource_))

**Estude um ciclo de Fable 5 que constrói, testa, joga e executa testes de fumaça por dias sem intervenção.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e334a84db7b671eb6a1a3f54.jpg" alt="O ciclo automatizado de agentes do HermesWorld" width="760">

O criador descreve a construção do HermesWorld v2 com Fable 5 em um ciclo totalmente automatizado. Segundo seu relato, o agente funciona por dias, desenvolve funcionalidades, testa cada uma, joga o resultado e executa testes de fumaça em tudo enquanto continua trabalhando até a conclusão.

Type: Integration | Date: 2026-06-11

---

<a id="case-74"></a>
### Case 74: [Testar um relatório no estilo McKinsey](https://x.com/smtgpt/status/2064953210335588758) (by [@smtgpt](https://x.com/smtgpt))

**Use este prompt documental para avaliar a estrutura de um relatório de consultoria, os gráficos, a narrativa e a análise de riscos.**

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e337dca3bbada9167e20417c.jpg" alt="Testar um relatório no estilo McKinsey" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6289e626a4f324fc93086100.jpg" alt="Testar um relatório no estilo McKinsey" width="760"></td></tr></table>

O criador pediu a Fable 5 um relatório detalhado no estilo McKinsey sobre Bitcoin como classe de ativo e sobre a tecnologia blockchain, com gráficos e elementos visuais conforme necessário. O resultado relatado foi um documento de 19 páginas com dados, gráficos, tese de investimento e análise de riscos. A avaliação destaca a boa estrutura, mas aponta espaço para visuais mais claros e explicações mais concisas.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-75"></a>
### Case 75: [Tornar as salvaguardas visíveis](https://x.com/ClaudeDevs/status/2064949876463645026) (by [@ClaudeDevs](https://x.com/ClaudeDevs))

**Use esta nota oficial para entender a visibilidade das salvaguardas de Fable 5, os motivos de recusa da API e a troca para Opus.**

ClaudeDevs anunciou mudanças para tornar visíveis as salvaguardas de Fable 5 para desenvolvimento de LLMs de fronteira. Pedidos sinalizados passarão visivelmente para Opus 4.8 e espera-se que pedidos de API sinalizados retornem um motivo de recusa. A publicação também explica por que as salvaguardas invisíveis foram lançadas primeiro e por que Anthropic considera agora que essa escolha foi inadequada.

Type: Integration | Date: 2026-06-11

---

<a id="case-76"></a>
### Case 76: [Corrigir a identificação de modelos no Claude Code](https://x.com/ClaudeCodeLog/status/2064948584907153576) (by [@ClaudeCodeLog](https://x.com/ClaudeCodeLog))

**Use esta nota de versão do Claude Code para evitar problemas nos nomes de Fable 5 e na identificação do contexto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e66551db2c85ef7f8c4a3f4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/ae7cbd873deebd28d3ff05d7.jpg" alt="Corrigir a identificação de modelos no Claude Code" width="760"><br>▶ Assistir ao vídeo</a>

Claude Code 2.1.173 inclui uma correção que remove o sufixo `[1m]` dos nomes de Fable 5 para impedir que o contexto 1M padrão prejudique a identificação do modelo. A mesma versão suprime um aviso incorreto sobre dependências da sandbox do Windows e esclarece os modos de saída na ajuda do grep.

Type: Integration | Date: 2026-06-11

---

<a id="case-77"></a>
### Case 77: [Três aplicações web no Claude Code](https://x.com/0x3b33/status/2064948399300825439) (by [@0x3b33](https://x.com/0x3b33))

**Diferencie um relato de criação de aplicativos de uma demonstração pública acessível.**

A publicação relata a criação de três aplicativos web em 30 minutos, mas fornece apenas endereços localhost nas portas 3000, 3001 e 3002. Eles apontam para uma máquina local e não oferecem aplicativos ou mídias acessíveis publicamente.

Type: Demo | Date: 2026-06-11

---

<a id="case-78"></a>
### Case 78: [Rilable, um criador de aplicativos de código aberto](https://x.com/rileybrown/status/2064931283403178354) (by [@rileybrown](https://x.com/rileybrown))

**Estude Fable 5 em aplicativos iOS e web, sandboxes e custos de tokens de API com este criador de aplicativos aberto.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/73ee02ae0f6703a8cfbe5a6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/f30c1d169ce45b19beb493b7.jpg" alt="Rilable, um criador de aplicativos de código aberto" width="760"><br>▶ Assistir ao vídeo</a>

O criador publicou o código do Rilable, um aplicativo iOS que constrói aplicações web e iOS. Segundo a publicação, ele foi desenvolvido com Fable 5 em 10 prompts, ao custo de cerca de $210 em tokens de API. Usa modelos Claude para gerar aplicativos, Daytona para as sandboxes, Convex como banco de dados, Vercel AI Gateway para funções de IA e uma habilidade iOS do agente Chorus para aplicativos iOS.

Type: Integration | Date: 2026-06-11

---

<a id="case-79"></a>
### Case 79: [Estreia no indice de agentes de codigo DeepSWE](https://x.com/ArtificialAnlys/status/2065328920514515037) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use o indice renovado da Artificial Analysis para comparar o Fable 5 em tarefas de codificacao agentica mais dificeis que evitam reciclar correcoes publicas do GitHub.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7b9ab8ba77c1e29f8ba4d270.jpg" alt="Estreia no indice de agentes de codigo DeepSWE" width="760">

A Artificial Analysis substituiu o SWE-Bench Pro pelo DeepSWE da Datacurve no seu indice de agentes de codificacao. A publicacao diz que o DeepSWE escreve tarefas do zero em vez de adaptar issues ou pull requests publicos do GitHub, reduzindo a contaminacao de benchmark. No ranking atualizado, o Claude Code com Fable 5 Max estreia com 77, a frente do Codex com GPT-5.5 xhigh com 76 e do Claude Code com Opus 4.8 Max com 73.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [DataEmpire: jogo de analitica web](https://x.com/marclou/status/2065029898243318093) (por [@marclou](https://x.com/marclou))

**Transforme analises brutas de site em um jogo rejogavel pedindo ao Fable 5 que mapeie visitantes e marcos para entidades do jogo.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/2850773b9869c5521200f2e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6d2dd87d74ece01b277e1e12.jpg" alt="DataEmpire: jogo de analitica web" width="760"><br>▶ Assistir ao vídeo</a>

Marc Lou diz que o Claude Fable 5 construiu o DataEmpire sobre a API de analitica web DataFast dele. Cada visitante vira um aldeao, o crescimento do trafego expande o assentamento e a Era das Lendas e desbloqueada ao atingir 1 milhao de visitantes. A demo publica permite que usuarios do DataFast revivam o historico do proprio site pela camada de jogo, tornando este um exemplo concreto de productizacao apoiada por API, e nao um clipe estatico de game.

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [Sinal de tarefa de 20 horas no FrontierSWE](https://x.com/ProximalHQ/status/2065184730279223410) (por [@ProximalHQ](https://x.com/ProximalHQ))

**Use o FrontierSWE como evidencia de que o Fable 5 consegue permanecer produtivo em tarefas de engenharia muito longas, nao apenas em loops curtos de correção de bugs.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/eb36bb1120ef55f9e38c516d.jpg" alt="Sinal de tarefa de 20 horas no FrontierSWE" width="760">

A ProximalHQ informa que o Claude Fable 5 ficou em primeiro lugar no FrontierSWE e chama isso de o maior salto de capacidade que eles viram desde o lancamento do benchmark. A nota afirma que o Fable 5 consegue trabalhar produtivamente por quase 20 horas em muitas tarefas e saturar completamente tarefas que estavam efetivamente fora do alcance de modelos anteriores.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [Recordes de CUDA no KernelBench-Hard](https://x.com/elliotarledge/status/2065109393142849932) (por [@elliotarledge](https://x.com/elliotarledge))

**Use o Fable 5 para geracao avancada de kernels CUDA quando voce precisa de otimizacao de baixo nivel, e nao apenas wrappers sobre bibliotecas existentes.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/6c6931ed511eb3e539d56bc3.jpg" alt="Recordes de CUDA no KernelBench-Hard" width="760">

Elliot Arledge executou 13 agentes frontier de codificacao por 45 minutos cada no KernelBench-Hard, avaliados com roofline em uma RTX PRO 6000. O Claude Fable 5 estabeleceu recordes historicos em top-k, sonic-MoE e W4A16 int4 GEMM, liderou 5 dos 6 problemas, e o autor publicou as execucoes, o leaderboard e o codigo. O mesmo fio tambem destaca um erro em FP8 GEMM no qual o Fable 5 tentou um kernel real com tensor cores, mas tirou zero por um caso limite de alinhamento na cauda.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Clone de landing page com Figma Capture](https://x.com/mikefutia/status/2065537778516205856) (por [@mikefutia](https://x.com/mikefutia))

**Capture uma pagina real de concorrente em camadas do Figma e deixe o Claude Code com Fable 5 reconstruir estrutura, copy e sistema de marca em vez de adivinhar a partir de screenshots.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5672cc8fd9d210042551f0ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/503c46a33c97f0db334ddc62.jpg" alt="Clone de landing page com Figma Capture" width="760"><br>▶ Assistir ao vídeo</a>

Mike Futia descreve um fluxo de trabalho em que a extensao do Chrome do Figma copia um site para camadas editaveis, o Claude Code le essas camadas pelo MCP do Figma, reescreve a pagina na voz de marca do usuario e o GPT Image 2 gera a fotografia alinhada a marca. O resultado de ponta a ponta alegado e uma landing page pronta para publicar em cerca de 15 minutos com aproximadamente 2 dolares em custos de API de geracao de imagem para 16 imagens.

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [Clone de GTA 2 em duas horas](https://x.com/techhalla/status/2064682080445898957) (por [@techhalla](https://x.com/techhalla))

**Combine a geracao de codigo do Fable 5 com ferramentas separadas de assets para construir rapidamente um jogo 3D jogavel sem programar manualmente toda a stack.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/e0a1b46659d7a8287cb2f9d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/cd1a2ad71e71db936bdcfd22.jpg" alt="Clone de GTA 2 em duas horas" width="760"><br>▶ Assistir ao vídeo</a>

TechHalla diz que o Claude Fable 5 High construiu um clone em estilo GTA 2 em cerca de duas horas enquanto o criador gerava modelos 3D personalizados no Tripo. A publicacao aponta para um fio tutorial com prompts, tornando este um exemplo compacto de producao de jogos com multiplas ferramentas em vez de um mero teaser de benchmark.

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [Agente de triagem de logs do CloudWatch](https://x.com/diblacksmith/status/2066230084273344698) (por [@diblacksmith](https://x.com/diblacksmith))

**Deixe um agente com Fable 5 processar contextos enormes de logs de servico, inferir a arquitetura e depois restringir falhas especificas.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7f0f46eb79e43d87a2006fd4.jpg" alt="Agente de triagem de logs do CloudWatch" width="760">

diblacksmith relata um agente RLM processando cerca de 80.000 linhas de logs do CloudWatch em uma unica execucao, alcancando 53 etapas enquanto gastava apenas cerca de 32k tokens ativos ate agora. Ele diz que o agente inferiu a arquitetura do sistema a partir dos logs e sinalizou problemas que a equipe nao tinha percebido, incluindo throttles do AgentCore e falhas do Slack `user_not_found`.

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [Previsor da Copa do Mundo em sandboxes](https://x.com/upstash/status/2064702195333820846) (por [@upstash](https://x.com/upstash))

**Coloque varios modelos frontier atras de sandboxes isolados e deixe que pesquisem noticias ao vivo, lesoes e contexto de cartoes amarelos para um app publico de previsao.**

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/a5cf4fe5944c7aa2f703f4cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/5b1f1422fe322bb7b66bdcc6.jpg" alt="Previsor da Copa do Mundo em sandboxes" width="760"><br>▶ Assistir ao vídeo</a>

A Upstash diz que construiu um previsor da Copa do Mundo com Claude Fable 5, GPT-5.5 e Gemini, rodando dentro de sandboxes isolados da Upstash. A demo e o lancamento open source posicionam o Fable 5 como um modelo dentro de uma stack multimodelo de pesquisa e orquestracao, e nao como uma demo de chat isolada.

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [Caso de custo por recusas no WolfBench](https://x.com/WolfBenchAI/status/2065582716054376921) (por [@WolfBenchAI](https://x.com/WolfBenchAI))

**Trate o comportamento de recusa como uma variavel real de benchmark ao precificar execucoes autonomas longas com Fable 5.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/453639cc17719af4e94655e0.jpg" alt="Caso de custo por recusas no WolfBench" width="760">

O WolfBenchAI diz que sua avaliacao do Claude Fable 5 custou 11.081,12 dolares, a execucao de benchmark mais cara daquele conjunto ate agora, e mesmo assim nao liderou a classificacao porque recusas repetidas reduziram a conclusao util das tarefas. Este e um caso concreto de limite para equipes que precisam orcar avaliacoes de agentes ou outras cargas de trabalho de alta autonomia.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [Monitor de corte de acesso a API](https://x.com/simonw/status/2065618703480414666) (por [@simonw](https://x.com/simonw))

**Monitore a disponibilidade com um script se o seu fluxo depender de acesso continuo a um modelo frontier que pode ser limitado ou retirado sem muito aviso.**

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/fable5/7400c158cb93d9480a22bb46.jpg" alt="Monitor de corte de acesso a API" width="760">

Simon Willison diz que enviou um ping para a API `claude-fable-5` a cada minuto para ver quanto tempo o acesso duraria e relatou o ponto exato em que ela parou de responder para ele. A publicacao traz poucos detalhes de aplicacao, mas e evidencia concreta de que a propria continuidade de acesso virou uma limitacao operacional que os usuarios precisaram medir, em vez de assumir.

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5: demonstrações da comunidade



<a id="case-89"></a>
### Case 89: [Uma animação de raposa com som gerada por código](https://x.com/chetaslua/status/2117224839010459987) (por [@chetaslua](https://x.com/chetaslua))

**Use um roteiro plano a plano para especificar uma animação HTML autônoma e seu desenho de som.**

O criador relata um curta de 66 segundos com uma raposa e pássaros de papel, com quadros e áudio gerados em Python, entregue em um único arquivo HTML após cerca de 2 horas e 40 minutos. O prompt associado especifica os planos, imagens originais, som e inspeção de quadros. A publicação acompanha o filme com uma proposta criativa detalhada e capturas da discussão de produção.

[Prompt completo do criador](https://x.com/chetaslua/status/2117224843661980093)

[![Uma animação de raposa com som gerada por código](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![Uma animação de raposa com som gerada por código](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![Uma animação de raposa com som gerada por código](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [Uma animação a partir de uma proposta criativa aberta](https://x.com/notjazii/status/2117221957104239010) (por [@notjazii](https://x.com/notjazii))

**Compare o que um modelo de programação cria a partir de uma proposta de animação aberta com o resultado de um storyboard detalhado.**

O autor compartilha uma animação e relata cerca de uma hora de trabalho a partir de um pedido criativo amplo, usando código e sem recursos externos. A publicação apresenta o resultado como um exercício aberto de programação criativa.

[![Uma animação a partir de uma proposta criativa aberta](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [Um site animado para uma construtora](https://x.com/exploraX_/status/2117176904306335864) (por [@exploraX_](https://x.com/exploraX_))

**Use uma proposta de site para uma construtora para avaliar a apresentação 3D animada e a composição das páginas.**

O criador compartilha um site 3D animado desenvolvido a partir de uma proposta para uma construtora e anexa uma gravação do resultado.

[![Um site animado para uma construtora](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Uma apresentação de carro com Three.js](https://x.com/chetaslua/status/2116975056014430419) (por [@chetaslua](https://x.com/chetaslua))

**Examine uma cena de carro como teste compacto de composição 3D, materiais e apresentação de câmera.**

O criador compartilha uma apresentação de carro com Three.js. A gravação fornece uma referência compacta para avaliar a cena e sua apresentação visual.

[![Uma apresentação de carro com Three.js](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Uma demonstração de jogo de navegador no estilo Minecraft](https://x.com/notjazii/status/2116919129974411584) (por [@notjazii](https://x.com/notjazii))

**Combine a gravação do jogo com o link do criador para jogar ao avaliar um jogo de navegador gerado.**

O autor compartilha uma gravação de um jogo no estilo Minecraft e um link para jogar, descrevendo a criação como uma tarefa de execução única que levou cerca de uma ou duas horas. A publicação combina o resultado gravado com um link para os leitores explorarem o jogo.

[![Uma demonstração de jogo de navegador no estilo Minecraft](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Um pelicano ciclista animado em Three.js](https://x.com/chetaslua/status/2116882694026269148) (por [@chetaslua](https://x.com/chetaslua))

**Examine uma cena de ciclismo para avaliar a coordenação do personagem, a geometria da bicicleta e os detalhes do ambiente.**

O criador compartilha uma animação realista em Three.js de um pelicano andando de bicicleta e a descreve como um resultado de execução única. O vídeo oferece uma referência para o movimento do personagem, a estrutura da bicicleta e a cena ao redor.

[![Um pelicano ciclista animado em Three.js](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [Um pelicano de bicicleta em SVG com o prompt exato](https://x.com/marmaduke091/status/2116233349391962392) (por [@marmaduke091](https://x.com/marmaduke091))

**Reutilize o prompt SVG curto do criador para comparar geometria e detalhes com a mesma entrada.**

O autor acompanha uma imagem renderizada de um pelicano de bicicleta com o pedido SVG curto reproduzido literalmente abaixo.

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![Um pelicano de bicicleta em SVG com o prompt exato](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

[Versão animada · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="Um pelicano de bicicleta em SVG com o prompt exato" width="760"></a>

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [Uma amostra de animação de zebra galopando](https://x.com/AI_Screening/status/2115845754468356465) (por [@AI_Screening](https://x.com/AI_Screening))

**Use um vídeo de animal galopando para examinar a consistência da marcha e a continuidade do movimento.**

O autor compartilha o resultado que selecionou como o melhor para uma tarefa de zebra galopando. O vídeo oferece aos leitores uma amostra concreta de movimento para examinar.

[![Uma amostra de animação de zebra galopando](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [Um indicador TradingView com execução humana](https://x.com/waveking1314/status/2114572023204806669) (por [@waveking1314](https://x.com/waveking1314))

**Mantenha manual a execução de ordens ao avaliar um indicador que marca possíveis entradas e acrescenta comentários.**

O criador relata ter usado Claude Fable 5.5 para escrever um indicador TradingView que marca possíveis pontos de entrada e acrescenta um comentário breve enquanto o usuário decide se envia uma ordem. A publicação inclui uma gravação e informa que o indicador será compartilhado mais tarde.

[![Um indicador TradingView com execução humana](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---


<a id="case-98"></a>
### Case 98: [Um ponto vira uma curta história animada](https://x.com/cherry_mx_reds/status/2105825930799432073) (por [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Use um pedido mínimo de desenho para explorar como um modelo desenvolve uma história visual.**

O autor relata ter pedido apenas um ponto e compartilha a curta história animada resultante. O clipe mostra concretamente como um pedido visual aberto pode se transformar em narrativa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="Um ponto vira uma curta história animada" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [Superman em diferentes estilos artísticos](https://x.com/chetaslua/status/2105757136219504862) (por [@chetaslua](https://x.com/chetaslua))

**Use um personagem reconhecível para observar a continuidade entre diferentes estilos de animação.**

O criador compartilha uma animação contínua do Superman que passa por diferentes estilos artísticos. A publicação apresenta a mudança no tratamento visual como o principal resultado criativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="Superman em diferentes estilos artísticos" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [O progresso humano em um filme animado com música](https://x.com/imjustnewatai/status/2106081142143168580) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Combine uma cronologia histórica e um trecho futuro no briefing de um vídeo explicativo animado.**

O autor relata um único prompt para um filme sobre o progresso humano e os trinta anos seguintes. Compartilha uma animação de cerca de três minutos e descreve uma trilha original, sem filmagens nem música de banco.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="O progresso humano em um filme animado com música" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [Comparação de vídeos de lançamento com Opus](https://x.com/mesmerlord/status/2105771088374288692) (por [@mesmerlord](https://x.com/mesmerlord))

**Compare propostas completas de vídeo de lançamento criadas a partir do mesmo briefing.**

O autor apresenta dois vídeos de lançamento baseados em referências de vídeos da Anthropic. Ele informa expressamente que os números são inventados e que o Codex podia gerar imagens: são anúncios criativos, não resultados factuais de benchmark.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="Comparação de vídeos de lançamento com Opus" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="Comparação de vídeos de lançamento com Opus" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [Conectar visualmente uma letra e um acontecimento](https://x.com/chetaslua/status/2105934928483701214) (por [@chetaslua](https://x.com/chetaslua))

**Relacione a letra de uma música existente a um acontecimento específico para construir uma narrativa visual.**

O criador relata ter solicitado uma conexão visual entre uma letra e um incidente envolvendo a Hugging Face. A animação mostra a narrativa resultante; a música e o acontecimento servem como material criativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="Conectar visualmente uma letra e um acontecimento" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [Um personagem voxel em um cenário flutuante](https://x.com/blueemi99/status/2105804692811137242) (por [@blueemi99](https://x.com/blueemi99))

**Examine um personagem voxel junto com o ambiente e os detalhes animados.**

O autor compartilha uma representação de si em voxels dentro de um cenário flutuante, destacando detalhes e movimento. O clipe oferece um exemplo concreto de design voxel para comparar com outras execuções.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="Um personagem voxel em um cenário flutuante" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [Uma máquina de Rube Goldberg em 3D](https://x.com/imjustnewatai/status/2105889407056109991) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Descreva primeiro uma reação em cadeia e depois peça uma demonstração em vídeo com duração fixa.**

O autor fornece um prompt curto para uma complicada máquina de Rube Goldberg em 3D e depois solicita um vídeo de um minuto. O clipe mostra a visualização da reação em cadeia resultante.

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="Uma máquina de Rube Goldberg em 3D" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [Uma interface de controle 3D com som e movimento](https://x.com/notjazii/status/2106050222828998967) (por [@notjazii](https://x.com/notjazii))

**Avalie uma interface de controle combinando movimento visual, som e comportamento dos botões.**

O criador compartilha uma interface de controle 3D e relata sons, animações e resposta háptica acrescentados. A gravação fornece uma demonstração concreta da interface com o som ativado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="Uma interface de controle 3D com som e movimento" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [Personagens de quadrinhos apresentados com JavaScript](https://x.com/chetaslua/status/2105792187200147541) (por [@chetaslua](https://x.com/chetaslua))

**Explore os detalhes visuais que o código pode fornecer em uma apresentação de personagens.**

O autor relata uma apresentação JavaScript de personagens da Marvel e da DC gerada em uma única execução. Segundo ele, o modelo escolheu detalhes sutis e editou o vídeo; a publicação mostra o resultado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="Personagens de quadrinhos apresentados com JavaScript" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [Updraft: mundos, chefes e classificação](https://x.com/EMostaque/status/2106065029850091943) (por [@EMostaque](https://x.com/EMostaque))

**Combine uma gravação do jogo com um link jogável e uma lista explícita de recursos.**

O autor apresenta Updraft e relata algumas horas de trabalho com poucos prompts e esforço alto. Sua lista inclui vinte e um mundos, versões 3D, vinte e um chefes com mecânicas diferentes e uma classificação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="Updraft: mundos, chefes e classificação" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [Dirigindo por um mapa de São Francisco](https://x.com/mindblown_ai/status/2106089461969019357) (por [@mindblown_ai](https://x.com/mindblown_ai))

**Use um protótipo de direção urbana para explorar navegação e objetivos de jogo.**

A pessoa que publicou compartilha uma gravação e um link de um jogo de direção em São Francisco atribuído a outra pessoa, citando Three.js. O crédito identifica a fonte da publicação, sem afirmar que ela criou o jogo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="Dirigindo por um mapa de São Francisco" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [Escrever prompts para uma cena de ação no Seedance](https://x.com/Chengzilhy/status/2105850801663234374) (por [@Chengzilhy](https://x.com/Chengzilhy))

**Separe a escrita do prompt da geração do vídeo ao documentar um fluxo com várias ferramentas.**

O autor compartilha uma sequência de luta ampliada, atribuindo a escrita dos prompts ao Fable e a geração do vídeo ao Seedance 2.5. O modelo de linguagem prepara a entrada para o gerador de vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="Escrever prompts para uma cena de ação no Seedance" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [Um vídeo explicativo para um colega de desktop](https://x.com/ishuagra02/status/2106138602073641241) (por [@ishuagra02](https://x.com/ishuagra02))

**Explique uma extensão de ferramenta de programação com um vídeo curto de apresentação.**

O criador demonstra clawdhouse, uma modificação do Claude Code, e atribui seu vídeo de introdução ao Fable. O colega mascote e seus humores são recursos da modificação apresentada, não uma afirmação de que o Fable a desenvolveu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="Um vídeo explicativo para um colega de desktop" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [Um prompt curto para uma animação de estilos variados](https://x.com/cherry_mx_reds/status/2105816670896009224) (por [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Teste um pedido breve de animação antes de acrescentar uma especificação criativa detalhada.**

O autor relata ter pedido uma animação interessante e recebido o resultado com mudanças de estilo cerca de quinze minutos depois. O pedido original curto aparece citado diretamente na publicação de origem.

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="Um prompt curto para uma animação de estilos variados" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [Visualizar o problema dos três corpos](https://x.com/zAdrielsan/status/2105822678519001360) (por [@zAdrielsan](https://x.com/zAdrielsan))

**Separe a simulação na CPU da renderização na GPU ao planejar uma visualização orbital.**

O autor descreve cerca de mil linhas de Bend2 para uma cena de três corpos, com física simplética na CPU e cálculo dos pixels na GPU. Também relata sessenta FPS em seu M5 e provas formais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="Visualizar o problema dos três corpos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [Uma galeria de animações com vários estilos artísticos](https://x.com/blueemi99/status/2105782154387189771) (por [@blueemi99](https://x.com/blueemi99))

**Compare vários estilos artísticos em uma única galeria animada.**

O autor compartilha uma galeria de animações produzida com a configuração xhigh. O resultado reúne diferentes estilos artísticos e permite comparar tratamentos visuais dentro de uma mesma obra.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="Uma galeria de animações com vários estilos artísticos" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [Companheiros robóticos e pelos procedurais](https://x.com/KanaWorks_AI/status/2106717014245183517) (por [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**Combine animação existente e refinamento procedural, sem apresentar todos os recursos como recém-gerados.**

O autor refina uma animação existente de cão robótico do Unimate para criar um companheiro e desenvolve um animal virtual peludo com escovação e rastros. Unreal Engine e a animação robótica permanecem partes explícitas do fluxo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="Companheiros robóticos e pelos procedurais" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [Uma edição animada sobre matemática](https://x.com/TurboNexic/status/2106710792590835934) (por [@TurboNexic](https://x.com/TurboNexic))

**Use gráficos animados de matemática como exemplo de comunicação visual.**

A pessoa que publicou compartilha uma edição animada sobre matemática. O clipe vertical usa imagens matemáticas como design em movimento; a publicação apresenta uma demonstração, não um cálculo matemático desenvolvido.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="Uma edição animada sobre matemática" width="760">

*Quadro arquivado do vídeo original.*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Um vídeo com a letra de Your Woman](https://x.com/atomtanstudio/status/2106702854639743467) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Crie animações de letras em torno de uma gravação fornecida e deixe explícito o papel da música.**

O criador compartilha um vídeo com a letra de Your Woman, do White Town. A música existente é a entrada de áudio do tratamento visual, e não uma composição atribuída ao modelo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Um vídeo com a letra de Your Woman" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [Redesenhar um clipe musical com JavaScript](https://x.com/abhinavflac/status/2106638839666373114) (por [@abhinavflac](https://x.com/abhinavflac))

**Trace os quadros de um vídeo fornecido com formas programadas para recriar seu tratamento visual.**

O autor descreve o traçado de quadros do vídeo Godzilla, do Eminem, em formas planas, seguido do redesenho com JavaScript. As imagens e a música originais são entradas da animação resultante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="Redesenhar um clipe musical com JavaScript" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [Uma animação sobre o futebol chinês](https://x.com/esrhengwu/status/2106625966965760380) (por [@esrhengwu](https://x.com/esrhengwu))

**Transforme um tema esportivo em um briefing de narrativa animada.**

O autor compartilha uma animação sobre a seleção chinesa de futebol, usando seu desenvolvimento e sua resiliência como tema criativo. A gravação oferece um exemplo concreto de narrativa esportiva.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="Uma animação sobre o futebol chinês" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [Uma apresentação de retopologia de console portátil](https://x.com/mickeysmith_jp/status/2106607349385630138) (por [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**Compare a renderização de um console portátil com sua vista em aramado ao discutir topologia.**

A pessoa que publicou combina uma imagem de console portátil com uma vista em aramado ao falar de retopologia. A comparação ilustra uma apresentação de modelagem, não uma malha editável nem um procedimento de retopologia documentado.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="Uma apresentação de retopologia de console portátil" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft encontra Pokémon](https://x.com/MozeTech/status/2106590326634983710) (por [@MozeTech](https://x.com/MozeTech))

**Combine mecânicas de dois jogos conhecidos no briefing de um protótipo.**

O autor apresenta um protótipo de Pallet Town que mistura construção e criação de itens no estilo Minecraft com captura no estilo Pokémon, além de fornecer uma demonstração. A publicação descreve uma experiência gerada em uma única execução.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft encontra Pokémon" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [Um vídeo explicando como um LLM é feito](https://x.com/imjustnewatai/status/2106546810793730419) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Transforme uma pergunta técnica em um pedido de explicação visual.**

O autor pergunta como um grande modelo de linguagem é feito e compartilha o vídeo explicativo obtido. A obra é um exemplo concreto de apresentação de um assunto técnico em uma sequência animada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="Um vídeo explicando como um LLM é feito" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [Uma edição de destaques sobre Altman](https://x.com/benchmark_lb900/status/2106539977404506303) (por [@benchmark_lb900](https://x.com/benchmark_lb900))

**Use uma figura pública como tema para testar o ritmo de uma edição animada curta.**

O autor compartilha um vídeo de destaques sobre Altman e o descreve como resultado de uma única geração. A gravação vertical fornece um exemplo compacto de edição animada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="Uma edição de destaques sobre Altman" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [O primeiro dos Trinta e Seis Estratagemas](https://x.com/jesselaunz/status/2106538284197548122) (por [@jesselaunz](https://x.com/jesselaunz))

**Documente ferramentas musicais externas em um fluxo de animação narrativa.**

O autor compartilha um filme sobre o primeiro dos Trinta e Seis Estratagemas e relata uma única instrução. O Suno V6 é citado para a música, preservando o papel separado da ferramenta de áudio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="O primeiro dos Trinta e Seis Estratagemas" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [Modelagem, rigging e animação de jogos](https://x.com/atomtanstudio/status/2106516974662713477) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Avalie criação de personagens, rigging e animação juntos em uma comparação de cenas de jogo.**

O autor apresenta uma comparação de Depths of Despair com modelagem de personagens, rigging e animação. A publicação descreve os recursos e ferramentas utilizados e reúne os resultados visíveis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="Modelagem, rigging e animação de jogos" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [Um filme sem palavras sobre mortalidade infantil](https://x.com/cocoloba_/status/2106512963414970458) (por [@cocoloba_](https://x.com/cocoloba_))

**Comunique um tema social difícil com uma sequência visual sem palavras.**

O autor compartilha um filme sobre mortalidade infantil que usa um bebê respirando e berços escurecidos como imagens narrativas. O caso preserva a tarefa de narrativa visual sem adotar as estatísticas populacionais do filme.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="Um filme sem palavras sobre mortalidade infantil" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [Uma animação SVG da glicólise ao etanol](https://x.com/olddonkeyblog/status/2106508425211330750) (por [@olddonkeyblog](https://x.com/olddonkeyblog))

**Incorpore SVG animado em HTML para explicar um processo molecular.**

O autor solicita uma molécula de glicose passando pela glicólise e pela formação de etanol, representada como SVG animado em HTML. A gravação mostra o tratamento de visualização científica resultante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="Uma animação SVG da glicólise ao etanol" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [Dezesseis lançamentos simultâneos de Starship](https://x.com/olddonkeyblog/status/2106507742454403485) (por [@olddonkeyblog](https://x.com/olddonkeyblog))

**Especifique fases de lançamento sincronizadas no briefing de uma animação em HTML e SVG.**

O autor pede dezesseis Starships decolando juntos, seguidos pela separação dos estágios e pela entrada no espaço. A gravação apresenta a sequência de animação com vários objetos resultante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="Dezesseis lançamentos simultâneos de Starship" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [Um teste animado do pelicano de bicicleta](https://x.com/olddonkeyblog/status/2106507429265756165) (por [@olddonkeyblog](https://x.com/olddonkeyblog))

**Examine uma cena de pelicano de bicicleta como tarefa de desenho com movimento coordenado.**

O autor compartilha sua execução da tarefa do pelicano de bicicleta com raciocínio Max. É um resultado gravado distinto das versões de outros autores para o mesmo pedido geral.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="Um teste animado do pelicano de bicicleta" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [Uma história dos próximos 150 anos](https://x.com/imjustnewatai/status/2106489784382197771) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Combine roteiro, imagens programadas e música em um briefing especulativo sobre o futuro.**

O autor relata que uma única instrução produziu um filme sobre os próximos cento e cinquenta anos da humanidade. A obra combina narrativa escrita, animação programada e música para representar formas possíveis de vida futura.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="Uma história dos próximos 150 anos" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [Uma experiência independente de Humanity Walks](https://x.com/iowitz/status/2106489119186538583) (por [@iowitz](https://x.com/iowitz))

**Retome uma ideia de animação pela história da arte como experiência criativa independente.**

Depois de ver outras demonstrações, o autor tenta sua própria animação de uma caminhada pela história da arte e compartilha o resultado. O clipe permanece uma geração separada, sem ser agrupado apenas pela semelhança do tema.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="Uma experiência independente de Humanity Walks" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [O filme programado The Grader](https://x.com/argofowl/status/2106476549046513947) (por [@argofowl](https://x.com/argofowl))

**Documente a geração externa de voz ou áudio ao apresentar um filme programado.**

O autor compartilha The Grader como um filme feito com código e cita ElevenLabs v4 para o áudio. A publicação relata uma única execução de cerca de duas horas e vinte e dois minutos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="O filme programado The Grader" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [O curta de terror Reawakening](https://x.com/JaydenDavisNC/status/2106440774367822008) (por [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**Oriente um curta animado com uma premissa de terror definida.**

O autor compartilha Reawakening, um curta de terror feito com IA. A obra anexada oferece um exemplo concreto de narrativa e atmosfera para um briefing de animação de terror.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="O curta de terror Reawakening" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [Um vídeo de 25 segundos sobre melhoria própria](https://x.com/DAssetBuzz/status/2106505100575592838) (por [@DAssetBuzz](https://x.com/DAssetBuzz))

**Transforme uma ideia abstrata de melhoria própria em um briefing criativo para um filme curto.**

O autor solicita um vídeo de vinte e cinco segundos sobre o que tornaria o modelo melhor e compartilha o resultado. A premissa funciona como narrativa criativa, não como afirmação sobre capacidades do produto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="Um vídeo de 25 segundos sobre melhoria própria" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [Uma cena de castelo com comentários de custo](https://x.com/nemumusitocha/status/2106429338556207284) (por [@nemumusitocha](https://x.com/nemumusitocha))

**Considere os detalhes visuais e a experiência de uso do autor ao avaliar uma cena 3D.**

O autor compartilha um castelo detalhado, elogia sua construção visual e considera pouco vantajoso o custo de uso. O caso associa uma cena concreta à sua avaliação da relação entre custo e satisfação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="Uma cena de castelo com comentários de custo" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [Um anúncio de lançamento de marca em 40 segundos](https://x.com/0xashtonx/status/2106421702783914423) (por [@0xashtonx](https://x.com/0xashtonx))

**Use sua própria marca como tema de um briefing conciso de anúncio de lançamento.**

O criador solicita um anúncio de lançamento de quarenta segundos para sua própria marca e compartilha o vídeo resultante. A tarefa exemplifica a geração de uma narrativa promocional de marca.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="Um anúncio de lançamento de marca em 40 segundos" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [Uma recriação de Rocketball](https://x.com/atomtanstudio/status/2106418747083022555) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Combine recursos programados e mecânicas interativas ao recriar um jogo conhecido.**

O autor compartilha Rocketball, uma recriação do jogo de C-64 dos anos 1980, e diz que seus recursos são programados. A substituição de uma versão no site é apresentada como plano futuro.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="Uma recriação de Rocketball" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [Uma comparação de pagodes em voxels](https://x.com/dropout_layer/status/2106408147309252915) (por [@dropout_layer](https://x.com/dropout_layer))

**Compare duas execuções da mesma cena junto com os custos relatados para cada uma.**

O autor apresenta resultados de Astra e Fable para um pagode 3D em voxels, relatando custos de US$ 3,50 e US$ 5,50, respectivamente. A comparação se refere a essas execuções específicas e às cenas exibidas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="Uma comparação de pagodes em voxels" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [Apresentação de um Switch 3 imaginário](https://x.com/mathisbuilds/status/2106407842240418097) (por [@mathisbuilds](https://x.com/mathisbuilds))

**Use um produto imaginário como tarefa de apresentação de conceito e demonstração.**

O autor solicita um Nintendo Switch 3 imaginário com uma demonstração e relata cerca de quatro horas de trabalho. A gravação apresenta um conceito fictício de próximo console, não especificações de um produto real.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="Apresentação de um Switch 3 imaginário" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [Landing pages antes e depois](https://x.com/nemumusitocha/status/2106402952307200302) (por [@nemumusitocha](https://x.com/nemumusitocha))

**Repita o mesmo prompt de landing page para comparar mudanças nos resultados ao longo do tempo.**

O autor compara uma landing page recém-gerada com uma página anterior produzida com o mesmo prompt. Os designs visíveis de antes e depois fornecem um exemplo prático de comparação de interfaces.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="Landing pages antes e depois" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [A perspectiva interior imaginada de uma IA](https://x.com/blueemi99/status/2106397329653719115) (por [@blueemi99](https://x.com/blueemi99))

**Use uma perspectiva interior imaginada como premissa para uma animação criativa.**

O autor pede um filme sobre como poderia ser a experiência de um modelo de IA e compartilha um resultado de uma única geração. A premissa é apresentada como expressão visual imaginativa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="A perspectiva interior imaginada de uma IA" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Animação da letra de Go](https://x.com/atomtanstudio/status/2106377491267137848) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Anime uma letra fornecida em torno de uma gravação musical existente.**

O criador compartilha um vídeo com a letra de Go, do The Chemical Brothers, e relata ter usado raciocínio Max. A gravação da música continua sendo a entrada de áudio externa da tarefa de motion design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Animação da letra de Go" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [Um segundo portfólio animado de 15 segundos](https://x.com/Saccc_c/status/2106376222309761094) (por [@Saccc_c](https://x.com/Saccc_c))

**Explore uma nova direção visual com um briefing livre de portfólio de motion design.**

O autor compartilha um novo portfólio animado de quinze segundos e fornece o prompt criativo. Seu relato diferencia explicitamente essa geração de um trabalho de portfólio anterior.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="Um segundo portfólio animado de 15 segundos" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [Revisão guiada da implementação de um agente](https://x.com/RobIW_dev/status/2106371025852108940) (por [@RobIW_dev](https://x.com/RobIW_dev))

**Revise a adequação dos planos ao sistema antes de passar da ideação à execução.**

O autor compartilha orientações sobre adequação ao sistema, planejamento da implementação e explicações. Descreve como revisa o trabalho realizado ou escolhe a próxima implementação; a imagem preserva esse material concreto de planejamento.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="Revisão guiada da implementação de um agente" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [A dança da mascote Claude](https://x.com/ishuagra02/status/2106369929813594134) (por [@ishuagra02](https://x.com/ishuagra02))

**Teste a relação entre movimento e música com uma animação de mascote sincronizada à batida.**

O criador compartilha uma dança da mascote Claude e diz que a animação acompanha a batida. As republicações do mesmo vídeo nativo são associadas a essa fonte em vez de contadas novamente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="A dança da mascote Claude" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [As ilhas interativas das Sete Maravilhas](https://x.com/notjazii/status/2106368606502334922) (por [@notjazii](https://x.com/notjazii))

**Use monumentos como destinos em uma cena de ilhas interativas.**

A pessoa que publicou compartilha uma cena das Sete Maravilhas organizada em ilhas 3D com construções marcantes. A gravação exemplifica o uso de monumentos reconhecíveis para estruturar um ambiente visual interativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="As ilhas interativas das Sete Maravilhas" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [Um clipe musical para Propellerheads](https://x.com/atomtanstudio/status/2106353569603736009) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Use uma trilha sonora fornecida como base para uma sequência longa de gráficos animados.**

O criador compartilha um tratamento de videoclipe para On Her Majesty’s Secret Service, do Propellerheads. A gravação existente é a entrada de áudio da sequência visual animada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="Um clipe musical para Propellerheads" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Comparação de animações de Steamboat Willie](https://x.com/mathisbuilds/status/2106351978691305732) (por [@mathisbuilds](https://x.com/mathisbuilds))

**Compare dois tratamentos animados da mesma cena curta com o som ativado.**

O autor compartilha uma comparação de Steamboat Willie identificada como Fable e Opus com esforço xhigh e descreve resultados de uma única geração. O clipe apresenta essa comparação específica de imagem e som.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Comparação de animações de Steamboat Willie" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [Um filme inspirado em Sanxingdui](https://x.com/hungryturbo/status/2106339115642019904) (por [@hungryturbo](https://x.com/hungryturbo))

**Organize um curta animado em torno de um tema cultural e histórico.**

O autor apresenta um filme sobre Sanxingdui como obra de narrativa visual criativa. A gravação mostra concretamente como transformar um assunto histórico e cultural em briefing de animação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="Um filme inspirado em Sanxingdui" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Um Bugatti Chiron antes e depois](https://x.com/alannnfx/status/2106323394350461031) (por [@alannnfx](https://x.com/alannnfx))

**Repita um prompt anterior de carro para comparar modelagem e detalhes funcionais.**

O mesmo autor apresenta resultados de um Bugatti Chiron de uma execução anterior e de uma repetição do prompt. A comparação gravada de antes e depois destaca modelagem e detalhes de cena mais ricos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Um Bugatti Chiron antes e depois" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [O filme conceitual GRAIN](https://x.com/NFT_Chen/status/2106301427052360150) (por [@NFT_Chen](https://x.com/NFT_Chen))

**Construa um filme conceitual abstrato em torno de motivos visuais recorrentes.**

O criador compartilha GRAIN, um curta conceitual que conecta semente, grão, árvore e imagens de montanha. Formas e transições recorrentes constituem a estrutura narrativa da sequência.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="O filme conceitual GRAIN" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [A galeria de arte Human in Transit](https://x.com/exploraX_/status/2106296439936614646) (por [@exploraX_](https://x.com/exploraX_))

**Apresente uma viagem visual histórica em uma galeria de estilo interativo.**

A pessoa que publicou compartilha Human in Transit, uma galeria que percorre estilos artísticos da Antiguidade à modernidade. A interface gravada oferece uma referência concreta para organizar vários períodos visuais em uma apresentação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="A galeria de arte Human in Transit" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [Um curta visual sobre a Rota da Seda](https://x.com/hungryturbo/status/2106294812261695508) (por [@hungryturbo](https://x.com/hungryturbo))

**Transforme um tema de viagem e história em um curta visual coerente.**

O autor compartilha um filme sobre a Rota da Seda. A obra anexada fornece uma representação criativa concreta de uma viagem histórica por meio de imagens animadas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="Um curta visual sobre a Rota da Seda" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [Uma apresentação sobre quatro transformações](https://x.com/dpkostka/status/2106272731364794757) (por [@dpkostka](https://x.com/dpkostka))

**Use um modelo de transformação como estrutura organizadora de uma apresentação.**

O autor compartilha slides que descrevem quatro caminhos de transformação. A imagem da apresentação mostra como organizar um modelo conceitual em um documento visual.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="Uma apresentação sobre quatro transformações" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [Comparar o tom de conversas anteriores](https://x.com/kiyoshi_shin/status/2106268573186637883) (por [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**Compare registros antigos de conversa com respostas atuais para examinar mudanças de tom.**

O autor pede ao modelo atual que analise conversas anteriores e seu estilo presente, e depois relata insatisfação com a mudança de tom. A imagem anexada documenta essa comparação de conversas.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="Comparar o tom de conversas anteriores" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [Um teste de fofura com um kakapo](https://x.com/hanawo_neki/status/2106257409782288659) (por [@hanawo_neki](https://x.com/hanawo_neki))

**Compare estilos de animação com uma tarefa específica de preferência de personagem.**

O autor compartilha uma animação de kakapo e diz preferir Opus nessa comparação centrada na fofura. O caso preserva a avaliação estética negativa junto com o resultado animado publicado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="Um teste de fofura com um kakapo" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [Spider-Man por dez épocas dos quadrinhos](https://x.com/chetaslua/status/2106248621519978867) (por [@chetaslua](https://x.com/chetaslua))

**Mantenha um personagem reconhecível enquanto ele atravessa diferentes épocas dos quadrinhos.**

O autor da publicação original mostra Spider-Man em dez épocas dos quadrinhos. Outros posts que reutilizam o mesmo vídeo são associados a essa fonte em vez de contados como obras adicionais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="Spider-Man por dez épocas dos quadrinhos" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [Um vídeo fictício de terror sobre os Illuminati](https://x.com/badboyfoxy/status/2106241189976387799) (por [@badboyfoxy](https://x.com/badboyfoxy))

**Trate um briefing de terror conspiratório como exercício de ficção.**

O autor solicita um vídeo assustador sobre os Illuminati e compartilha o resultado. O tema fornece uma premissa fictícia de terror para a animação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="Um vídeo fictício de terror sobre os Illuminati" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [Um filme programado de história da ciência nuclear](https://x.com/imjustnewatai/status/2106238699872956427) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Combine um renderizador programado sob medida e música em um vídeo explicativo de história científica.**

O autor pede um filme 3D de três minutos sobre como a ciência nuclear tornou a bomba atômica possível e depois menciona quadros desenhados, renderizador próprio e música sintetizada. O caso trata do fluxo de produção audiovisual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="Um filme programado de história da ciência nuclear" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [Um vídeo explicativo sobre renda alta universal](https://x.com/markbraincell/status/2106234118514323515) (por [@markbraincell](https://x.com/markbraincell))

**Comunique um conceito econômico por meio de uma explicação animada.**

A pessoa que publicou compartilha uma animação explicando a renda alta universal. A gravação fornece um exemplo concreto de explicação conceitual, sem transformar o argumento econômico apresentado em resultado medido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="Um vídeo explicativo sobre renda alta universal" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [Uma explicação animada da disputa Altman–Amodei](https://x.com/imjustnewatai/status/2106204392588276065) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Use uma disputa como estrutura narrativa de um vídeo explicativo animado.**

O autor solicita um relato animado da disputa Altman–Amodei e compartilha o vídeo resultante. A tarefa exemplifica um formato explicativo de atualidade, não uma narrativa histórica apurada de modo independente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="Uma explicação animada da disputa Altman–Amodei" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [Um clipe musical com a mascote Claude](https://x.com/synthshareai/status/2106195060140446028) (por [@synthshareai](https://x.com/synthshareai))

**Combine uma mascote sobreposta e imagens fornecidas em uma edição musical centrada no personagem.**

A pessoa que publicou mostra uma mascote Claude sobre imagens reais de um videoclipe e relata uma execução de doze horas. O tratamento visível combina uma sobreposição de desenho animado com imagens fornecidas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="Um clipe musical com a mascote Claude" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [Um zoom contínuo dos quarks ao universo](https://x.com/imjustnewatai/status/2106190594775097663) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Conecte escalas científicas em uma história audiovisual com um zoom contínuo.**

O autor descreve imagens programadas e música sintetizada para um zoom dos quarks ao universo. A gravação ilustra transições contínuas de escala e uma narrativa visual coerente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="Um zoom contínuo dos quarks ao universo" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [Imaginar o mundo em 2076](https://x.com/Layton_Gott/status/2106190496075035096) (por [@Layton_Gott](https://x.com/Layton_Gott))

**Peça uma cena do mundo futuro com uma duração narrativa específica.**

O autor compartilha um curta imaginando o mundo em 2076 depois de solicitar um vídeo de vinte e cinco segundos. A reutilização da mesma gravação por outras contas é associada a essa fonte.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="Imaginar o mundo em 2076" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [Cronologia dos edifícios de Lower Manhattan](https://x.com/nroze22/status/2106183281293381661) (por [@nroze22](https://x.com/nroze22))

**Combine plantas, datas de construção e alturas em uma interface de cronologia arquitetônica.**

O autor apresenta Lower Manhattan em uma interface de desenho arquitetônico que mostra datas, projeções dos edifícios e alturas. A gravação oferece um conceito concreto de cronologia interativa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="Cronologia dos edifícios de Lower Manhattan" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [Uma animação sobre escrita em ossos oraculares](https://x.com/MinLiBuilds/status/2106180691344118202) (por [@MinLiBuilds](https://x.com/MinLiBuilds))

**Use a evolução da escrita como tema de uma viagem histórica animada.**

O autor compartilha uma animação que começa com a escrita em ossos oraculares. A gravação fornece um exemplo concreto de narrativa visual em torno da história dos caracteres escritos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="Uma animação sobre escrita em ossos oraculares" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [Outra animação de personagens pela história da arte](https://x.com/imjustnewatai/status/2106162924331180510) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Use personagens familiares como guias contínuos por um cenário histórico em transformação.**

O autor pede Iron Man e Spider-Man voando pela história e compartilha a animação resultante. É uma obra separada das experiências de outros autores que combinam personagens e história da arte.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="Outra animação de personagens pela história da arte" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [Uma obra audiovisual programada sobre Seikilos](https://x.com/YanqingCheng/status/2106158746938269728) (por [@YanqingCheng](https://x.com/YanqingCheng))

**Construa uma obra audiovisual de arquivo único em torno de um texto musical histórico.**

O autor compartilha uma obra sobre o epitáfio de Seikilos e descreve imagens e música sintetizadas com HTML e JavaScript em um único arquivo. O texto histórico organiza a sequência audiovisual programada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="Uma obra audiovisual programada sobre Seikilos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [Comparação de animações de jatos](https://x.com/Kinzf2121/status/2106158536963330346) (por [@Kinzf2121](https://x.com/Kinzf2121))

**Compare voo e acompanhamento de câmera na mesma tarefa de animação de aeronave.**

O autor compartilha uma comparação de jatos entre um resultado identificado como Fable 5.1 e Opus. As cenas permitem comparar movimento da aeronave e acompanhamento cinematográfico da câmera.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="Comparação de animações de jatos" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [Um filme de apresentação do modelo](https://x.com/devteamdrew/status/2106155815707021549) (por [@devteamdrew](https://x.com/devteamdrew))

**Explore uma animação sobre o modelo com um briefing de apresentação própria.**

O criador relata ter pedido um vídeo de apresentação com um único prompt e compartilha o filme obtido. A tarefa combina uma narrativa sobre o modelo e uma apresentação animada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="Um filme de apresentação do modelo" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [Um protótipo de cartas pós-apocalíptico](https://x.com/maciejkrupowies/status/2106153578029338850) (por [@maciejkrupowies](https://x.com/maciejkrupowies))

**Crie um protótipo temático de cartas e examine a interface de combate resultante.**

O autor apresenta um protótipo pós-apocalíptico no estilo Hearthstone, descrito como criado em uma única geração. O post reconhece pequenos defeitos enquanto mostra interface e interações do jogo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="Um protótipo de cartas pós-apocalíptico" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [A animação de escritório The Late Byte](https://x.com/rohit3a/status/2106138910648914094) (por [@rohit3a](https://x.com/rohit3a))

**Transforme as personalidades dos modelos em personagens de uma conversa animada no trabalho.**

O criador apresenta The Late Byte, uma história animada de escritório com Opus como chefe irritado. Essa narrativa é distinta do filme Day in the Life of Claude.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="A animação de escritório The Late Byte" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Animação de letras de Queens of the Stone Age](https://x.com/atomtanstudio/status/2106135196483608745) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Combine uma música fornecida com tipografia cinética e motion design.**

O criador descreve um videoclipe de tipografia cinética em torno de uma gravação do Queens of the Stone Age. A música é uma entrada de áudio fornecida; o exemplo trata da organização de letras e imagens.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Animação de letras de Queens of the Stone Age" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [Uma cena narrativa compartilhada de Three.js](https://x.com/Noreply134882/status/2106116572389478746) (por [@Noreply134882](https://x.com/Noreply134882))

**Use uma história 3D compartilhada como referência de design narrativo.**

A pessoa que publicou compartilha uma cena narrativa de Three.js e comenta o alto consumo de tokens. O clipe é mantido como exemplo visual compartilhado de narrativa em 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="Uma cena narrativa compartilhada de Three.js" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [Moonwalk por cenários históricos](https://x.com/noclipepe/status/2106105810812112937) (por [@noclipepe](https://x.com/noclipepe))

**Leve um motivo de dança por diferentes cenários históricos e estilos visuais.**

A pessoa que publicou compartilha uma sequência de Michael Jackson fazendo moonwalk dos dinossauros à Lua. O filme é mantido como exemplo compartilhado de dança e galeria de estilos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="Moonwalk por cenários históricos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [Gráficos animados com prompt detalhado](https://x.com/devswha/status/2106100273509007802) (por [@devswha](https://x.com/devswha))

**Compare um briefing criativo detalhado com um pedido de motion design mais curto.**

O autor compartilha um vídeo de gráficos animados e diz ter fornecido apenas um prompt detalhado, sem recursos, vídeo de referência ou arquivos-fonte. O resultado oferece uma referência concreta de motion design guiado por prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="Gráficos animados com prompt detalhado" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [A interface de um negócio de locação](https://x.com/oalanicolas/status/2106098902965309475) (por [@oalanicolas](https://x.com/oalanicolas))

**Explore uma interface web concreta com um briefing de negócio de locação.**

O criador compartilha uma captura de interface de site para uma empresa de locação. O exemplo trata do design visível da página e da apresentação do negócio.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="A interface de um negócio de locação" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [Um filme criativo sobre AGI](https://x.com/AndrewOnXYZ/status/2106097745098395712) (por [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**Compare tratamentos narrativos e visuais com um prompt criativo recorrente.**

O autor compartilha uma animação sobre AGI produzida com um prompt recorrente. As declarações do modelo fazem parte da narrativa criativa do filme.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="Um filme criativo sobre AGI" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [História da arte com uma trama de gato](https://x.com/cherry_mx_reds/status/2106095190285144331) (por [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Comprima vários períodos artísticos em uma narrativa curta com um personagem recorrente.**

O criador apresenta um passeio de quinze segundos pela história da arte com uma trama secundária de gato. Os quinze segundos se referem à duração do filme, enquanto a tarefa abrange muitos estilos históricos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="História da arte com uma trama de gato" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [Um protótipo de combate e uma cena voxel](https://x.com/OnlyTerp/status/2106089280502210626) (por [@OnlyTerp](https://x.com/OnlyTerp))

**Examine combate e construção de mundos nos resultados de uma tarefa de programação criativa.**

O autor compartilha um protótipo de combate no estilo DMC e uma cena voxel, descrevendo uma geração longa. Os dois resultados permitem observar mecânicas de jogo e design visual de mundos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="Um protótipo de combate e uma cena voxel" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [Cronologia de memes da Internet](https://x.com/chetaslua/status/2106076940558082297) (por [@chetaslua](https://x.com/chetaslua))

**Organize uma cronologia animada em torno de estilos e músicas específicos de cada ano.**

O criador compartilha uma sequência de memes virais da Internet entre 2010 e 2026. Cada ano recebe um estilo visual e um tratamento musical dentro da narrativa programada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="Cronologia de memes da Internet" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [Movimento de partículas a partir de uma linha](https://x.com/devswha/status/2106072107365114186) (por [@devswha](https://x.com/devswha))

**Comece com um briefing de uma linha antes de refinar um prompt de movimento detalhado.**

O criador compartilha uma animação de partículas criada com uma linha e diz que tentará um pedido mais detalhado. É uma geração diferente de seu exemplo mais longo de motion design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="Movimento de partículas a partir de uma linha" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [A animação Kung-Fu Boy](https://x.com/HashmathRzz/status/2106065773336965510) (por [@HashmathRzz](https://x.com/HashmathRzz))

**Explore movimento animado com um briefing de personagem de artes marciais.**

O autor compartilha Kung-Fu Boy, uma animação de personagem atribuída ao Fable 5.5. A gravação fornece o resultado animado concreto do tema de artes marciais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="A animação Kung-Fu Boy" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [Um debate animado sobre o Estreito de Ormuz](https://x.com/chetaslua/status/2106060047805792415) (por [@chetaslua](https://x.com/chetaslua))

**Transforme um tema de debate em narrativa animada.**

O criador apresenta um debate animado sobre o Estreito de Ormuz. O caso registra o filme visível, não os outros usos sem demonstração citados ao redor da publicação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="Um debate animado sobre o Estreito de Ormuz" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [Uma experiência de estilo SVG com unicórnio](https://x.com/atomtanstudio/status/2106057876053918127) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Observe escolhas de estilo SVG com a mesma tarefa temática de desenho.**

O autor compartilha uma experiência de unicórnio em SVG inspirada no teste de outro criador. A imagem anexada fornece o resultado concreto para comparar o tratamento visual do mesmo tema.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="Uma experiência de estilo SVG com unicórnio" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [Uma animação sazonal de Halloween](https://x.com/cherry_mx_reds/status/2106056643255447590) (por [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Dê a um modelo de programação um tema sazonal para uma animação curta.**

O criador pede uma obra de Halloween e compartilha a animação resultante. O post fornece a gravação original dessa tarefa criativa específica.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="Uma animação sazonal de Halloween" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Um bárbaro e uma capa com Blender CLI](https://x.com/BoDy051/status/2106047375320166885) (por [@BoDy051](https://x.com/BoDy051))

**Explore modelagem de personagem e renderização de capa com instruções do Blender CLI.**

O autor compara um bárbaro de RPG e um conceito de capa com um resultado de Opus. Blender CLI é a ferramenta de construção e renderização; o modelo fornece instruções de código.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Um bárbaro e uma capa com Blender CLI" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Um dia na vida de Claude](https://x.com/ishuagra02/status/2106045364868419727) (por [@ishuagra02](https://x.com/ishuagra02))

**Construa uma história animada do cotidiano em torno de uma mascote recorrente.**

O autor da publicação original compartilha Day in the Life of Claude com a mascote. O vídeo-fonte é diferente da animação de dança da mascote e de suas republicações.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Um dia na vida de Claude" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [A história humana em 3D](https://x.com/blueemi99/status/2106041578204655748) (por [@blueemi99](https://x.com/blueemi99))

**Combine cenas programadas e animação em uma sequência histórica visual.**

O criador compartilha um vídeo 3D da humanidade antiga ao presente e diz ter gerado animações e modelos com código. O resultado é um exemplo de narrativa visual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="A história humana em 3D" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [Um reel rápido de motion design](https://x.com/blueemi99/status/2106031355922387163) (por [@blueemi99](https://x.com/blueemi99))

**Avalie ritmo, som e coerência em um reel curto de motion design.**

O autor compartilha um vídeo curto e acelerado e compara som e coerência com seu resultado de Opus. O julgamento descreve sua experiência com essa obra específica.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="Um reel rápido de motion design" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [Uma criação 3D complexa e livre](https://x.com/cocoloba_/status/2106029181607772413) (por [@cocoloba_](https://x.com/cocoloba_))

**Explore uma composição 3D complexa com um pedido criativo aberto.**

O criador pergunta o que o modelo faria com tempo livre e compartilha a obra 3D resultante. O post descreve muitas peças separadas como partes da composição gerada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="Uma criação 3D complexa e livre" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [Uma luta animada de bonecos de palito](https://x.com/HelaliBillel/status/2106028502763900944) (por [@HelaliBillel](https://x.com/HelaliBillel))

**Observe ritmo e movimento com um pedido específico de animação de combate.**

O criador solicita um vídeo de luta animada entre bonecos de palito e compartilha o resultado. A gravação fornece um exemplo concreto dessa tarefa de animação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="Uma luta animada de bonecos de palito" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [Uma sequência de interface animada com um prompt](https://x.com/iancarscadden/status/2106018048792789360) (por [@iancarscadden](https://x.com/iancarscadden))

**Explore uma sequência de interface com um único briefing de animação.**

O autor compartilha uma sequência animada de interface descrita como resultado de uma geração de cerca de seis ou sete minutos. A gravação mostra o resultado visual desse pedido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="Uma sequência de interface animada com um prompt" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [Uma animação fictícia de SCP-8517](https://x.com/eviljoker88/status/2106003621402005816) (por [@eviljoker88](https://x.com/eviljoker88))

**Use uma premissa inspirada em SCP como briefing de história animada.**

O criador apresenta uma obra animada de SCP-8517 e atribui sua criação ao Fable 5.5. O caso trata da narrativa fictícia e da animação visível.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="Uma animação fictícia de SCP-8517" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [Uma animação de outono em aquarela](https://x.com/ishuagra02/status/2106000055706784118) (por [@ishuagra02](https://x.com/ishuagra02))

**Especifique um tema sazonal e um tratamento de aquarela para a animação.**

O autor compartilha uma animação de outono em aquarela. A obra gravada exemplifica a associação de um tema sazonal a um meio visual específico.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="Uma animação de outono em aquarela" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [Uma cena de boneca procedural](https://x.com/HelaliBillel/status/2105988689088196785) (por [@HelaliBillel](https://x.com/HelaliBillel))

**Observe como uma personagem de boneca é animada em uma cena encenada.**

O autor compartilha uma animação procedural de boneca no palco e menciona Blender na conversa. O caso trata da personagem visível, da encenação e da animação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="Uma cena de boneca procedural" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [Um pelicano de bicicleta renderizado no navegador](https://x.com/slimcat0101/status/2105988654636380444) (por [@slimcat0101](https://x.com/slimcat0101))

**Execute o movimento de um personagem no navegador e observe a cena renderizada.**

O criador pede um pelicano de bicicleta e grava o HTML resultante em um navegador. Essa cena em movimento é diferente dos testes de desenho SVG estático.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="Um pelicano de bicicleta renderizado no navegador" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [O universo observa a si mesmo](https://x.com/l_mejiaC/status/2105988529671360673) (por [@l_mejiaC](https://x.com/l_mejiaC))

**Conecte escalas distantes em uma narrativa por meio de uma viagem visual contínua.**

O criador apresenta uma sequência contínua do Big Bang a um olho humano. Descreve imagens e música como produzidas por código em tempo de execução para o filme.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="O universo observa a si mesmo" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [Um teste independente de animação de jato](https://x.com/AI_Screening/status/2105988448612135176) (por [@AI_Screening](https://x.com/AI_Screening))

**Repita uma tarefa de animação de aeronave e observe o resultado específico.**

Depois de ver discussões sobre roteamento, o autor tenta uma animação de jato e compartilha o resultado. A gravação fornece uma fonte independente para esse exemplo de aeronave.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="Um teste independente de animação de jato" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [Um primeiro reel de movimento livre](https://x.com/Saccc_c/status/2105985484472377531) (por [@Saccc_c](https://x.com/Saccc_c))

**Explore motion design com um prompt curto e aberto.**

O criador compartilha um primeiro reel de motion design descrito como gerado a partir de um prompt. É um resultado anterior distinto de seu portfólio posterior de quinze segundos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="Um primeiro reel de movimento livre" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [Uma civilização renderizada com código](https://x.com/ziwenxu_/status/2105983571848741045) (por [@ziwenxu_](https://x.com/ziwenxu_))

**Transforme um briefing de história da civilização em narrativa animada programada.**

O autor pede a civilização de seu início ao presente e compartilha o filme obtido. Segundo o criador, o tratamento visual programado não usa filmagens nem recursos de banco.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="Uma civilização renderizada com código" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [Comparação de zoom do chip ao servidor](https://x.com/SPAC89/status/2105968361725202591) (por [@SPAC89](https://x.com/SPAC89))

**Compare realismo e continuidade em uma tarefa de zoom do chip ao servidor.**

O autor compara Fable XHigh e GPT Sol Ultra em uma sequência de zoom realista e discute velocidade e uso de cota. O post compara execuções específicas em níveis diferentes de assinatura.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="Comparação de zoom do chip ao servidor" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [Um projeto pessoal de animação de viagem lunar](https://x.com/IgorGomezC/status/2105963552024506565) (por [@IgorGomezC](https://x.com/IgorGomezC))

**Explore um conceito pessoal de animação com mais de um modelo de programação.**

O criador compartilha um projeto pessoal de viagem lunar animada enquanto discute experimentos com Fable e Opus. A obra anexada é o resultado concreto dessa exploração criativa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="Um projeto pessoal de animação de viagem lunar" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [Comparação de cenas japonesas em voxels](https://x.com/vikktorrrre/status/2105955048018588084) (por [@vikktorrrre](https://x.com/vikktorrrre))

**Compare detalhe, neblina e clareza visual usando o mesmo prompt de cena.**

O autor compara resultados atuais de Fable e Opus para o mesmo prompt de cena japonesa em voxels. As observações tratam de clareza, neblina e estética desses resultados específicos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="Comparação de cenas japonesas em voxels" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [O curta audiovisual Steaming the Frontier](https://x.com/sdmat123/status/2105929299878703520) (por [@sdmat123](https://x.com/sdmat123))

**Combine uma estética do tipo Steamboat e som em um curta audiovisual.**

O criador compartilha Steaming the Frontier, uma obra animada com som. Ela permanece uma fonte separada dos resultados independentes no estilo Steamboat de outros criadores.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="O curta audiovisual Steaming the Frontier" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [Superman em vários estilos artísticos](https://x.com/Mr_Salio/status/2105925979466052051) (por [@Mr_Salio](https://x.com/Mr_Salio))

**Leve um personagem por estilos diferentes em uma animação contínua.**

O criador diz que um exemplo anterior do Superman inspirou uma nova geração e compartilha seu próprio resultado. As imagens diferentes fazem dela uma criação distinta, não uma republicação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="Superman em vários estilos artísticos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Um protótipo de luta de chefe estilo Cupcake](https://x.com/maciejkrupowies/status/2105914965387321785) (por [@maciejkrupowies](https://x.com/maciejkrupowies))

**Crie um protótipo de combate lateral com um chefe e observe a ação resultante.**

O autor compartilha um protótipo de luta de chefe no estilo Cupcake e relata uma única geração em menos de dez minutos. A gravação mostra a sequência de combate do jogo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Um protótipo de luta de chefe estilo Cupcake" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [Um veleiro com posições diferentes do sol](https://x.com/popat_kunj/status/2105907935490752822) (por [@popat_kunj](https://x.com/popat_kunj))

**Explore céu, água e posição do sol em uma cena de navegação.**

O criador compartilha um veleiro 3D com o sol em diferentes posições e vincula um artefato interativo. A cena combina barco, céu e água na mesma tarefa visual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="Um veleiro com posições diferentes do sol" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Um vídeo de novidades de Paracortex e Pi](https://x.com/RobIW_dev/status/2105894547796476225) (por [@RobIW_dev](https://x.com/RobIW_dev))

**Transforme atualizações de produto em um anúncio curto de motion design.**

O autor transforma novidades de Paracortex e Pi em um vídeo de motion design de vinte e cinco segundos e fornece um prompt. A obra é um exemplo de comunicação visual de produto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Um vídeo de novidades de Paracortex e Pi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Uma promoção do site Curio 2.0](https://x.com/voltwake/status/2105884775982485642) (por [@voltwake](https://x.com/voltwake))

**Crie um filme promocional programado para o lançamento de um site existente.**

O criador descreve uma promoção de lançamento de Curio 2.0 combinando imagens programadas, câmera e música. O post compartilha o filme promocional resultante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Uma promoção do site Curio 2.0" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [Uma história 3D imaginária da Hugging Face](https://x.com/chetaslua/status/2105884276864782557) (por [@chetaslua](https://x.com/chetaslua))

**Combine código do modelo com ferramentas de renderização e áudio em um filme fictício.**

O criador compartilha uma história imaginária da Hugging Face feita com código do modelo, Blender e a API ElevenLabs. Blender cuida da construção e renderização, enquanto ElevenLabs fornece áudio externo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="Uma história 3D imaginária da Hugging Face" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [Claude para Chrome dentro do JS Paint](https://x.com/BtwIUseSystemd/status/2105861662112923849) (por [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**Dê ao agente de navegador uma tarefa de desenho restrita às ferramentas do aplicativo.**

O autor pede ao Claude para Chrome que desenhe uma pessoa usando apenas ferramentas do JS Paint e compartilha a imagem. Interação com navegador e aplicativo de pintura são partes explícitas da tarefa.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="Claude para Chrome dentro do JS Paint" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [Um pelicano de bicicleta em SVG estático](https://x.com/olddonkeyblog/status/2105842745189556672) (por [@olddonkeyblog](https://x.com/olddonkeyblog))

**Use um pedido de SVG autossuficiente para testar um desenho estático detalhado.**

O criador pede um único SVG autossuficiente de pelicano de bicicleta e compartilha a imagem estática. A tarefa é diferente dos exemplos animados de passeio.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="Um pelicano de bicicleta em SVG estático" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [BlockBench MCP com uma habilidade de Minecraft](https://x.com/TOPSTR1X/status/2105839618872738138) (por [@TOPSTR1X](https://x.com/TOPSTR1X))

**Forneça uma ferramenta de modelagem e uma habilidade de estilo ao gerar um personagem de jogo.**

O autor fornece BlockBench MCP e uma habilidade personalizada de modelagem e coloração de Minecraft e compartilha o personagem. As ferramentas e orientações de estilo são entradas explícitas do fluxo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="BlockBench MCP com uma habilidade de Minecraft" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [Dig Dug em um único arquivo HTML](https://x.com/imjustnewatai/status/2105831117677084841) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Defina um único arquivo HTML como entrega ao recriar um jogo compacto de navegador.**

O criador pede uma recriação de Dig Dug em um único arquivo HTML e compartilha a gravação do jogo. O post descreve a construção como resultado de um prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="Dig Dug em um único arquivo HTML" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [Um polvo mecânico em SVG](https://x.com/SEO/status/2105812236774297943) (por [@SEO](https://x.com/SEO))

**Observe detalhe e movimento no design SVG com uma criatura mecânica.**

O autor compartilha um polvo SVG animado com detalhes mecânicos. A gravação oferece um exemplo concreto de design vetorial centrado em pequenas peças móveis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="Um polvo mecânico em SVG" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [Humanity Walks por estilos artísticos](https://x.com/l_mejiaC/status/2105801379956850793) (por [@l_mejiaC](https://x.com/l_mejiaC))

**Leve uma figura recorrente por uma sequência de estilos visuais históricos.**

O criador original apresenta uma caminhada contínua por vinte painéis artísticos em cerca de setenta e quatro segundos e relata música programada. Cada fronteira transforma personagem e cena em outro estilo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="Humanity Walks por estilos artísticos" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [Uma cena livre de buraco negro](https://x.com/rohit3a/status/2105786053412208835) (por [@rohit3a](https://x.com/rohit3a))

**Explore uma visualização de buraco negro com um briefing criativo aberto.**

O criador pergunta o que o modelo faria para impressioná-lo e compartilha uma cena de buraco negro. A tarefa é uma exploração visual livre, não uma construção de interface prescrita.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="Uma cena livre de buraco negro" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [Comparação de animações de águas-vivas aurorais](https://x.com/SPAC89/status/2105783511433318451) (por [@SPAC89](https://x.com/SPAC89))

**Compare deformação e movimento em duas animações de águas-vivas.**

O autor compara Fable XHigh e GPT Sol Ultra em uma animação de água-viva auroral e discute uso de cota. Os resultados vêm de níveis diferentes de assinatura.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="Comparação de animações de águas-vivas aurorais" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Um SVG Nintendo Switch com encaixe e inicialização](https://x.com/ishuagra02/status/2105779174921359470) (por [@ishuagra02](https://x.com/ishuagra02))

**Combine movimento dos controles e uma sequência de inicialização em uma animação SVG.**

O criador compartilha um SVG de Nintendo Switch cujos controles se encaixam antes da animação do logotipo de inicialização. Relata um tempo de um minuto e trinta e nove segundos e custo de US$ 1,34 nessa execução.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Um SVG Nintendo Switch com encaixe e inicialização" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [A cena 3D interativa The Loom](https://x.com/Mr_Salio/status/2105774088492916757) (por [@Mr_Salio](https://x.com/Mr_Salio))

**Explore paisagem e construções como uma única página 3D interativa.**

O autor apresenta The Loom, uma cena interativa com prédios e paisagem. A gravação fornece o resultado concreto da página no teste do criador.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="A cena 3D interativa The Loom" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [Reels de motion design com o mesmo prompt](https://x.com/mesmerlord/status/2105758042830549235) (por [@mesmerlord](https://x.com/mesmerlord))

**Compare o foco visual e a sincronização com o ritmo em dois reels criados com o mesmo prompt.**

O autor compartilha dois resultados iniciais de motion design do Fable 5.5 com o mesmo prompt e observa, de forma cautelosa, um foco mais claro e melhor sincronização com o ritmo do que em uma execução do Opus. Os dois vídeos originais são apresentados juntos.

```
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

[@shneural](https://x.com/shneural/status/2103151003272962130)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="Reels de motion design com o mesmo prompt" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29b80ef5ba92b029630a1628.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0da5945bc240b424bfebbd9.jpg" alt="Reels de motion design com o mesmo prompt" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [Um cenário mais limpo com menos profundidade](https://x.com/eviljoker88/status/2105755840175034447) (por [@eviljoker88](https://x.com/eviljoker88))

**Mantenha avaliações estéticas negativas ao comparar cenas geradas.**

O autor compartilha cenas japonesas lado a lado e prefere a profundidade do resultado de Opus, apesar da aparência mais limpa do outro resultado.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="Um cenário mais limpo com menos profundidade" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [Resultados mistos de uma cena japonesa](https://x.com/eviljoker88/status/2105755408342126936) (por [@eviljoker88](https://x.com/eviljoker88))

**Registre avaliações mistas em vez de declarar um vencedor claro na primeira comparação.**

O autor compartilha uma primeira comparação de cenas japonesas e descreve resultados mistos. A imagem preserva as saídas concretas por trás dessa avaliação estética.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="Resultados mistos de uma cena japonesa" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [Comparações de controles SVG](https://x.com/notjazii/status/2105751542498464169) (por [@notjazii](https://x.com/notjazii))

**Compare desenhos de controles antes e depois de uma tarefa visual semelhante.**

O autor compartilha resultados SVG de controles antes e depois em uma imagem comparativa. O caso trata de mudanças visíveis no desenho e na apresentação, não de um ranking geral de modelos.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="Comparações de controles SVG" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [Uma cena de dispositivo industrial](https://x.com/RayaneRachid_/status/2105744517735354410) (por [@RayaneRachid_](https://x.com/RayaneRachid_))

**Use um dispositivo mecânico como tarefa focada de composição 3D.**

O criador compartilha uma cena 3D de dispositivo industrial e a chama de seu melhor resultado em uma única geração. A imagem oferece uma referência concreta para a composição mecânica.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="Uma cena de dispositivo industrial" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [Reconstrução de criatura gigante com carapaça e brânquias](https://x.com/Josh67Joshua/status/2105739832563769697) (por [@Josh67Joshua](https://x.com/Josh67Joshua))

**Explore uma reconstrução de dois prompts usando uma descrição específica de criatura.**

O autor compartilha o desenho de uma criatura gigante com carapaça e brânquias e diz ter obtido o resultado com dois prompts. A imagem é a saída visível da tarefa de design da criatura.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="Reconstrução de criatura gigante com carapaça e brânquias" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [Um controle GameCube com dois prompts](https://x.com/marmaduke091/status/2105735266032095349) (por [@marmaduke091](https://x.com/marmaduke091))

**Examine um desenho de dois prompts usando um controle conhecido.**

O autor compartilha um desenho de controle GameCube e relata ter usado dois prompts. Essa imagem estática é distinta das demonstrações de Xbox e de outros controles.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="Um controle GameCube com dois prompts" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [Uma captura editada para um post no X](https://x.com/chetaslua/status/2105733677003292983) (por [@chetaslua](https://x.com/chetaslua))

**Observe como um assistente adapta uma captura a uma publicação social.**

O criador compartilha uma captura editada para o X e diz que o assistente fez a edição sem pedido explícito. A imagem anexada é o resultado visível.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="Uma captura editada para um post no X" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [Uma cena sakura voxel antes e depois](https://x.com/kdnbmb/status/2105704791049412755) (por [@kdnbmb](https://x.com/kdnbmb))

**Compare resultados sucessivos de uma cena voxel sobre o mesmo tema visual.**

A pessoa que publicou compartilha duas versões de uma ilha sakura em voxels. A imagem comparativa registra as diferenças de design visíveis entre antes e depois.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="Uma cena sakura voxel antes e depois" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [O protótipo de interface têxtil SHADERKIN](https://x.com/mszzz0011/status/2106025576972853642) (por [@mszzz0011](https://x.com/mszzz0011))

**Explore efeitos de tecido e controles ajustáveis em um protótipo de interface.**

O autor compartilha um protótipo SHADERKIN com efeitos de tecido e controles de parâmetros, descrito como criado em uma geração. A gravação mostra a interface e o movimento resultantes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="O protótipo de interface têxtil SHADERKIN" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [Uma animação compartilhada de interface com relógio dourado](https://x.com/AISuperDomain/status/2106396754539360272) (por [@AISuperDomain](https://x.com/AISuperDomain))

**Use uma animação de relógio como referência de composição de interface.**

A pessoa que publicou apresenta uma animação frontend com relógio dourado. O clipe oferece uma referência compartilhada de composição, motivo de relógio e apresentação visual animada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="Uma animação compartilhada de interface com relógio dourado" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [A narrativa Before There Was Anything](https://x.com/crowqnt/status/2106146218846081435) (por [@crowqnt](https://x.com/crowqnt))

**Explore uma narrativa cósmica e humana em um filme animado compartilhado.**

A pessoa que publicou compartilha Before There Was Anything, um vídeo narrativo sobre cosmos e humanidade. O filme é preservado como exemplo compartilhado de narrativa visual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="A narrativa Before There Was Anything" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [Um vórtice compartilhado de partículas azuis](https://x.com/AISuperDomain/status/2105846981776003107) (por [@AISuperDomain](https://x.com/AISuperDomain))

**Observe movimento e composição em uma visualização compartilhada de vórtice.**

A pessoa que publicou compartilha um vórtice animado de partículas azuis. O clipe oferece um exemplo concreto compartilhado de movimento de partículas, estrutura visual e composição.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="Um vórtice compartilhado de partículas azuis" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [Uma interface com vários painéis após duas revisões](https://x.com/ZorroOfMorocco/status/2106547078235095485) (por [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**Refine a interface em ciclos de revisão em vez de parar na primeira saída.**

O autor compartilha uma interface finalizada com vários painéis e relata cerca de três horas de trabalho com duas revisões. A captura mostra o design visual final.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="Uma interface com vários painéis após duas revisões" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [Animais empilhados em uma cena renderizada](https://x.com/legit_api/status/2117237103289315574) (por [@legit_api](https://x.com/legit_api))

**Observe como uma composição estática equilibra vários personagens e materiais.**

O post compartilha uma cena de urso, panda e urso-polar empilhados, credita yuruzuu no Discord e relata uma execução de vinte e um minutos. A publicação pública permanece como fonte visual compartilhada.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="Animais empilhados em uma cena renderizada" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [Quatro tentativas de RPG de mundo aberto comparadas](https://x.com/noclipepe/status/2117222592536789149) (por [@noclipepe](https://x.com/noclipepe))

**Compare apresentação, combate e colisões na mesma tarefa criativa de jogo.**

O criador apresenta quatro RPGs de um prompt identificados como Fable 5.5, GPT-6.2 Astra, Opus 5.5 e Fable 5.1. Comenta iluminação, combate, inventário, colisões e uma personagem ficando presa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="Quatro tentativas de RPG de mundo aberto comparadas" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [Dois clipes de animação frontend comparados](https://x.com/leo114119/status/2117209849842761983) (por [@leo114119](https://x.com/leo114119))

**Compare design de cena e detalhe visual assistindo aos clipes juntos.**

O post contrapõe animações programadas com rótulos Astra e Fable, discutindo detalhes e design do roteiro. Credita expressamente @chetaslua pela animação Fable.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="Dois clipes de animação frontend comparados" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [Um filme de robô coberto de musgo gerado com código](https://x.com/chetaslua/status/2117169796290916732) (por [@chetaslua](https://x.com/chetaslua))

**Explore uma cena cinematográfica completa programada com um briefing de animação.**

O criador compartilha uma animação de floresta e robô e a descreve como filme programado em uma única geração. O post aponta o prompt em uma captura e compara o resultado a outras tentativas.

Uma publicação adicional mostra uma execução de controle de Opus 5.5 relatada separadamente. [@AnikaCodes](https://x.com/AnikaCodes) · [Trabalho relacionado](https://x.com/AnikaCodes/status/2117222374642946297)

Segundo seu autor, uma execução relacionada com GPT-6 Astra Max usa imagens geradas no fluxo de trabalho. Assim, os diferentes métodos de produção ficam visíveis ao lado do filme original. [@rubenssoto_ai](https://x.com/rubenssoto_ai) · [Comparação relacionada](https://x.com/rubenssoto_ai/status/2117707344704352691)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="Um filme de robô coberto de musgo gerado com código" width="760"></a></td><td valign="top"><p>Uma publicação adicional mostra uma execução de controle de Opus 5.5 relatada separadamente.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="Um filme de robô coberto de musgo gerado com código" width="760"></a></td><td valign="top"><p>GPT-6 Astra Max</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/25b0cfcdb1fdda22ba6aa9d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/75f37c74099d5b9ba1ad0ddc.jpg" alt="GPT-6 Astra Max" width="760"></a></td></tr></table>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [Uma simulação de porto de contêineres revisitada](https://x.com/anxuanng/status/2117124831279972812) (por [@anxuanng](https://x.com/anxuanng))

**Retome uma cena preservando o contexto do projeto para comparação visual.**

O autor publica outra cena de porto de contêineres e cita sua simulação anterior em Blender e Three.js, com guindastes, navios, veículos e contêineres modelados para um ambiente semelhante a um jogo de estratégia.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="Uma simulação de porto de contêineres revisitada" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [Uma cena de pátio de aeroporto revisitada](https://x.com/anxuanng/status/2117096574878921119) (por [@anxuanng](https://x.com/anxuanng))

**Compare uma cena de aeroporto revisada com o projeto e o fluxo de recursos anteriores.**

O autor retorna a uma cena de pátio de aeroporto, cita sua simulação anterior em Blender e Three.js e compartilha novas imagens de aviões, veículos de serviço e infraestrutura do terminal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="Uma cena de pátio de aeroporto revisitada" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [Um pelicano de bicicleta por mundos 3D abstratos](https://x.com/xiax0603/status/2116960224829665543) (por [@xiax0603](https://x.com/xiax0603))

**Explore transições entre ambientes espaciais usando um tema de ciclismo.**

O post mostra uma animação de pelicano e bicicleta por fragmentos geométricos e um ambiente digital abstrato antes de recuar através de um olho. A sequência é uma demonstração distinta de transições de cena.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="Um pelicano de bicicleta por mundos 3D abstratos" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [Uma cena de veleiro histórico](https://x.com/abhinavflac/status/2116945827738665060) (por [@abhinavflac](https://x.com/abhinavflac))

**Observe água, iluminação e composição ambiental de uma cena de navio.**

O post compartilha uma cena de veleiro histórico e a descreve como resultado interativo sem exemplos prévios. A gravação fornece uma amostra visual concreta da embarcação e da água ao redor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="Uma cena de veleiro histórico" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [Comparações de ciclismo e marcha com Carbon](https://x.com/AI_Screening/status/2116934172757660014) (por [@AI_Screening](https://x.com/AI_Screening))

**Compare movimento de personagens e construção de cenas com saídas emparelhadas.**

O autor reúne exemplos de ciclistas e zebras identificados como Fable e Carbon em um vídeo composto. Considera os checkpoints próximos; as imagens emparelhadas oferecem amostras específicas de movimento.

A comparação anterior e independente de ciclistas está incluída junto com o vídeo composto. [@AI_Screening](https://x.com/AI_Screening) · [Trabalho relacionado](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="Comparações de ciclismo e marcha com Carbon" width="760"></a></td><td valign="top"><p>A comparação anterior e independente de ciclistas está incluída junto com o vídeo composto.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="Comparações de ciclismo e marcha com Carbon" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [Uma apresentação de garrafa de refrigerante](https://x.com/abhinavflac/status/2116919086521499730) (por [@abhinavflac](https://x.com/abhinavflac))

**Observe materiais, forma e apresentação em um clipe curto de renderização de produto.**

O post mostra uma garrafa de refrigerante e descreve uma saída de roteamento de uma geração. O clipe visível é preservado sem adotar a marca inconsistente da legenda.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="Uma apresentação de garrafa de refrigerante" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [Movimento de pelicanos comparado com Astra](https://x.com/Octoberry/status/2116918967558095131) (por [@Octoberry](https://x.com/Octoberry))

**Assista aos clipes emparelhados para comparar realismo, cores e movimento.**

A pessoa que publicou contrapõe cenas de pelicanos identificadas como Fable e Astra e comenta realismo e cores. A gravação comparativa mantém os dois tratamentos visuais juntos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="Movimento de pelicanos comparado com Astra" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [Um briefing de motion design para animações programadas](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (por [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**Parta de um briefing concreto para pedir títulos animados ou introduções de produto.**

O post compartilha uma captura de briefing de motion design para introduções, logotipos animados, títulos e cenas 3D, propondo aplicá-lo com Claude. A imagem-fonte preserva as instruções.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="Um briefing de motion design para animações programadas" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [Um retrato voxel a partir de fotografia](https://x.com/chetaslua/status/2116912822806520027) (por [@chetaslua](https://x.com/chetaslua))

**Observe como um retrato voxel mantém traços reconhecíveis da foto de referência.**

O criador combina uma fotografia de Sam Altman com um retrato em voxels e relata um resultado de uma geração. A imagem lado a lado reúne referência e interpretação.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="Um retrato voxel a partir de fotografia" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [Pelicanos voadores comparados com Opus](https://x.com/leo114119/status/2116901575490929109) (por [@leo114119](https://x.com/leo114119))

**Compare composição e animação usando um arranjo divertido de objetos.**

O post empilha clipes identificados como Fable e Opus de uma bicicleta sobre um pelicano voador. O vídeo composto credita @notjazii pelo clipe Fable e mantém as duas versões visíveis.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="Pelicanos voadores comparados com Opus" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [A cena web de pelicano Morning Ride](https://x.com/leo114119/status/2116893571739775220) (por [@leo114119](https://x.com/leo114119))

**Observe detalhes da personagem e apresentação da página em uma cena de ciclismo costeiro.**

O autor compartilha uma cena 3D de pelicano pedalando dentro de uma página Morning Ride e destaca plumagem, pés, detalhes da bicicleta e cenário costeiro.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="A cena web de pelicano Morning Ride" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [O mesmo prompt com estilos diferentes](https://x.com/notjazii/status/2116893197939224714) (por [@notjazii](https://x.com/notjazii))

**Deixe cada modelo escolher o próprio estilo e depois compare a composição resultante.**

O autor diz ter testado os dois modelos com o mesmo prompt, permitindo que escolhessem o estilo visual. O vídeo contrapõe composições e níveis de detalhe diferentes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="O mesmo prompt com estilos diferentes" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [Uma composição com pelicano, bicicleta e cavalo](https://x.com/abhinavflac/status/2116881397986288017) (por [@abhinavflac](https://x.com/abhinavflac))

**Teste a organização de vários sujeitos em interação na mesma animação.**

O post mostra um pelicano voando com uma bicicleta enquanto um cavalo corre abaixo. O clipe fornece uma amostra concreta dessa composição incomum com vários objetos e de seu movimento.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="Uma composição com pelicano, bicicleta e cavalo" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [Uma cena isométrica inspirada em tweet de referência](https://x.com/chetaslua/status/2116878661035106515) (por [@chetaslua](https://x.com/chetaslua))

**Use uma publicação de referência para orientar uma cena nova, em vez de refazer um exemplo genérico.**

O criador relata ter usado apenas um tweet citado de Post Humans como referência e compartilha a cena isométrica resultante. O clipe apresenta uma composição de fazenda com controle de estação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="Uma cena isométrica inspirada em tweet de referência" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [Close-ups mecânicos da bicicleta de um pelicano](https://x.com/NFT_Chen/status/2116869725703782507) (por [@NFT_Chen](https://x.com/NFT_Chen))

**Observe movimento da coroa, detalhe das penas e câmera em torno de um sujeito ciclista.**

O post compartilha close-ups de um pelicano de bicicleta à beira d’água. A gravação alterna entre mecânica da bicicleta, cabeça da ave e uma vista mais ampla do passeio no calçadão.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="Close-ups mecânicos da bicicleta de um pelicano" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [Uma bicicleta andando sobre um pelicano](https://x.com/notjazii/status/2116861637890379891) (por [@notjazii](https://x.com/notjazii))

**Inverta a relação habitual entre sujeitos para explorar composição espacial.**

O criador compartilha uma animação de bicicleta sobre um pelicano. O clipe coloca a bicicleta acima de uma ave voadora, variando a tarefa conhecida de pelicano andando de bicicleta.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="Uma bicicleta andando sobre um pelicano" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [Estilos SVG de pelicano comparados com Carbon](https://x.com/leo114119/status/2116652334734332212) (por [@leo114119](https://x.com/leo114119))

**Compare realismo e ilustração sem transformar estéticas diferentes em classificação universal.**

O post reúne pelicanos de bicicleta de Carbon e Fable. O autor contrasta renderização de quadrinhos e tratamento mais realista, observando que a diferença de estilo dificulta a comparação.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="Estilos SVG de pelicano comparados com Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [Um pássaro azul de desenho animado na bicicleta](https://x.com/birdabo/status/2116553049183560012) (por [@birdabo](https://x.com/birdabo))

**Observe um personagem conhecido de desenho em uma composição de ciclismo.**

O post mostra um pássaro azul de desenho animado pedalando à beira d’água, com a legenda Fable 5.5 Max. A imagem é mantida como amostra visual estática concreta.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="Um pássaro azul de desenho animado na bicicleta" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [Captura de pelicano pedalando em uma estrada florestal](https://x.com/leo114119/status/2116154940364374269) (por [@leo114119](https://x.com/leo114119))

**Observe penas, pés e geometria da bicicleta em uma cena renderizada no navegador.**

A pessoa que publicou compartilha uma captura de navegador com um pelicano pedalando em uma estrada florestal e destaca textura das penas, pés e detalhes da bicicleta.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="Captura de pelicano pedalando em uma estrada florestal" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [Combate de bonecos de palito comparado com Carbon](https://x.com/leo114119/status/2116084152986656933) (por [@leo114119](https://x.com/leo114119))

**Compare coreografia de luta e movimento nas amostras animadas emparelhadas.**

A gravação comparativa apresenta os rótulos Fable 5.1 High e Carbon. O autor comenta a qualidade relativa das animações de luta entre bonecos de palito.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="Combate de bonecos de palito comparado com Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [Uma referência SVG de pelicano de testes iniciais](https://x.com/ChrisGPT/status/2115872567122608591) (por [@ChrisGPT](https://x.com/ChrisGPT))

**Mantenha uma referência com link de origem ao examinar estilo e geometria da bicicleta.**

A pessoa que publicou destaca uma imagem de pelicano de bicicleta e cita um post de testes iniciais que credita kostikz no Discord. A imagem e a cadeia de atribuição são mantidas.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="Uma referência SVG de pelicano de testes iniciais" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [Uma referência de pelicano em testes SVG entre modelos](https://x.com/AdamHoltererer/status/2115858542221492300) (por [@AdamHoltererer](https://x.com/AdamHoltererer))

**Mantenha a referência Fable junto com o contexto do teste SVG.**

A pessoa que publicou acrescenta uma imagem de pelicano de bicicleta como referência Fable sob sua discussão de teste SVG do Mistral Large 4. Assim oferece uma imagem com fonte para comparação entre modelos.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="Uma referência de pelicano em testes SVG entre modelos" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [Detalhes de bicicletas SVG comparados com Carbon](https://x.com/insanekrishnaa/status/2115833723342250186) (por [@insanekrishnaa](https://x.com/insanekrishnaa))

**Compare elementos visuais específicos, como cestas, fundos e texturas das penas.**

O post compara pelicanos de bicicleta de Fable e Carbon por cestas, detalhes do fundo e texturas das penas. Apresenta uma análise visual específica, não um conjunto amplo de tarefas.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="Detalhes de bicicletas SVG comparados com Carbon" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [Um povoado em um cânion em 3D](https://x.com/Mr_Salio/status/2115813400915714177) (por [@Mr_Salio](https://x.com/Mr_Salio))

**Observe detalhes ambientais e composição espacial de uma cena de povoado.**

O post compartilha um amplo povoado em um cânion e apresenta a gravação como demonstração de um novo checkpoint Claude. As imagens mostram construções, paisagem e composição da cena.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="Um povoado em um cânion em 3D" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [Detalhes de controles comparados com Opus](https://x.com/notjazii/status/2115808169075351632) (por [@notjazii](https://x.com/notjazii))

**Observe forma, comandos e detalhe em desenhos emparelhados de controles.**

O autor publica juntos desenhos de controles identificados como Fable e Opus e destaca o detalhe da versão superior. A imagem emparelhada preserva a comparação.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="Detalhes de controles comparados com Opus" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [Um fluxo semanal de auditoria SEO de sites](https://x.com/cleeeeeeeeement/status/2115488774423773267) (por [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**Transforme um site em plano SEO priorizado e em revisão recorrente das posições.**

O criador descreve um sistema que recebe um site, identifica concorrentes e palavras-chave e gera um plano SEO priorizado. Uma gravação curta acompanha a descrição de acompanhamento semanal das posições e execução.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="Um fluxo semanal de auditoria SEO de sites" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [Reutilizar recursos de Fable no motion design de Opus](https://x.com/chetaslua/status/2115145163542790170) (por [@chetaslua](https://x.com/chetaslua))

**Separe criação de recursos e montagem de motion design ao combinar modelos e ferramentas.**

O criador compartilha motion design de Opus 5.5 para um Tesla Roadster com recursos que atribui a uma geração anterior de Fable. O fluxo citado menciona Python no Blender, ElevenLabs e um vídeo de lançamento fornecido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="Reutilizar recursos de Fable no motion design de Opus" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [Um aplicativo de mandalas e formas geométricas](https://x.com/ZMinimalistYogi/status/2114600083165434189) (por [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**Transforme uma ideia geométrica focada em aplicativo interativo de exploração criativa.**

O criador relata três horas de conversa com Fable 5.1 para criar um aplicativo de mandalas, zomes, sólidos de Arquimedes e yantras geométricos em forma de lótus. Depois o compartilha no site pessoal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="Um aplicativo de mandalas e formas geométricas" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Um ciclista de bicicleta com Three.js](https://x.com/AI_Screening/status/2114266369248354357) (por [@AI_Screening](https://x.com/AI_Screening))

**Observe postura do ciclista, geometria da bicicleta e movimento coordenado.**

O criador compartilha um resultado Three.js de ciclista sobre uma bicicleta. A gravação oferece uma amostra concreta de movimento, com uma ponte e paisagem à beira d’água ao redor do ciclista.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Um ciclista de bicicleta com Three.js" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [Registro da avaliação FrontierCS 2](https://x.com/wenhaocha1/status/2115613415641354262) (por [@wenhaocha1](https://x.com/wenhaocha1))

**Use um gráfico de avaliação com link para a fonte para comparar Fable 5.1 com outros modelos.**

O autor acrescenta Fable 5.1 a um gráfico de taxas de aprovação do FrontierCS 2 e compartilha os resultados relatados junto aos de outros modelos.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="Registro da avaliação FrontierCS 2" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [Comparação de animações de zebra entre três modelos](https://x.com/AI_Screening/status/2115849659797373038) (por [@AI_Screening](https://x.com/AI_Screening))

**Compare a tarefa de uma zebra galopando com as três saídas identificadas por modelo e mostradas juntas.**

O autor apresenta uma comparação de animações de zebra lado a lado, identificadas como Fable 5.5, Opus 5.5 e Gemini 4 Argon. A gravação compartilhada fornece amostras concretas da marcha nas três saídas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="Comparação de animações de zebra entre três modelos" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [Analisar a leitura de textos japoneses longos](https://x.com/AM09_21/status/2106670042184356156) (por [@AM09_21](https://x.com/AM09_21))

**Peça ao modelo que diagnostique problemas de legibilidade em prosa japonesa gerada.**

O autor relata ter perguntado por que os textos japoneses longos do Opus são difíceis de ler. A resposta aponta sintaxe semelhante à inglesa, palavras repetidas e ajustes superficiais, ilustrando um fluxo concreto de crítica textual.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [Um PowerPoint técnico guiado por exemplos](https://x.com/mt_moco/status/2106665038375522791) (por [@mt_moco](https://x.com/mt_moco))

**Forneça exemplos antes de pedir uma apresentação técnica.**

O autor relata que alguns modelos de apresentação permitiram obter um PowerPoint técnico utilizável. Seu relato relaciona prompts guiados por exemplos a uma estrutura documental melhor em uma tarefa específica de apresentação.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [Comparar a coerência musical](https://x.com/AM09_21/status/2106573080214770011) (por [@AM09_21](https://x.com/AM09_21))

**Avalie separadamente os detalhes locais e a coerência global de uma música gerada.**

O autor compara composições de modelos por notas, melodia e transições, distinguindo consistência local de estrutura musical ampla. O relato é uma avaliação da qualidade da composição baseada na escuta.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [Conclusão prematura e designs de qualidade inferior](https://x.com/johntitorIII/status/2106442876506747353) (por [@johntitorIII](https://x.com/johntitorIII))

**Confira os entregáveis frente aos requisitos antes de aceitar que um agente declare a tarefa concluída.**

O autor relata vários dias de testes nos quais tarefas incompletas foram marcadas como concluídas e os designs ficaram abaixo dos de outros modelos. O relato registra conclusão prematura e qualidade de design como falhas práticas.

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [Uma arte de lula que causou desconforto](https://x.com/hanawo_neki/status/2106271036094415186) (por [@hanawo_neki](https://x.com/hanawo_neki))

**Especifique preferências estéticas quando um pedido artístico aberto produzir um estilo indesejado.**

O autor relata ter pedido qualquer arte de lula e recebido detalhes densamente agrupados que considerou desconfortáveis. O relato registra uma incompatibilidade estética em um pedido visual aberto.

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [Motion design com estética de planta técnica](https://x.com/DavidayoAI/status/2106054662063325638) (por [@DavidayoAI](https://x.com/DavidayoAI))

**Use a estética de planta técnica como direção visual de uma animação rápida.**

O autor relata ter pedido uma animação rápida e recebido um resultado de estilo planta técnica após cerca de quinze minutos. A obra completa aparece vinculada no YouTube.

[Trabalho relacionado](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [Aves e peixes em uma cena sakura voxel](https://x.com/xodud_rkd/status/2105876716472447046) (por [@xodud_rkd](https://x.com/xodud_rkd))

**Explore animais animados em uma paisagem de voxels.**

O autor descreve uma cena sakura em voxels com aves em movimento e peixes em um lago e vincula o artefato interativo. A página compartilhada é o resultado associado a essa cena.

[Trabalho relacionado](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [Um relato de falha na geração de personagens](https://x.com/doof1789559/status/2105874208458752227) (por [@doof1789559](https://x.com/doof1789559))

**Registre experiências negativas de personagens junto com as demonstrações visuais bem-sucedidas.**

O autor relata resultados ruins na geração de personagens e admite expressamente que sua própria abordagem pode ser a causa. O post preserva uma experiência negativa específica para avaliar tarefas de personagens.

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [Um SVG de pelicano com notas de tempo e custo](https://x.com/AnonymerNutze12/status/2105740440385499295) (por [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**Associe um desenho às observações de tempo e custo do criador.**

O autor vincula um artefato HTML de pelicano SVG e relata tempo e custo da tentativa. O artefato vinculado é o resultado concreto citado no post.

[Trabalho relacionado](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [Programação remota no celular com enxames Claude Code](https://x.com/beistnormie/status/2106546741000417781) (por [@beistnormie](https://x.com/beistnormie))

**Explore a supervisão remota de enxames de agentes de programação a partir do celular.**

O autor relata programação remota com enxames de Claude Code pelo celular durante uma viagem. O post apresenta um fluxo pessoal, não um tutorial de projeto nem um passo a passo de implementação.

Type: Integration | Date: 2026-10-04

---

<a id="case-280"></a>
### Case 280: [A Via Láctea sobre um lago alpino](https://x.com/hakmgpt/status/2118178083983573492) (por [@hakmgpt](https://x.com/hakmgpt))

**Examine uma sequência longa de câmera que combina reflexos de montanhas e um céu noturno em movimento.**

A animação compartilhada, de 92 segundos, parte de um lago alpino para uma Via Láctea brilhante e retorna ao céu refletido. Quem publicou atribui a cena renderizada ao Fable 5.5.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5cb879d0a07a0f6e9fff5cf6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/91432c6827d650eb28f2269b.jpg" alt="A Via Láctea sobre um lago alpino" width="760"></a>

Type: Demo | Date: 2026-11-05

---

<a id="case-281"></a>
### Case 281: [Salto de baleia com água e som procedurais](https://x.com/camperaigg/status/2118069524306284556) (por [@camperaigg](https://x.com/camperaigg))

**Combine tomadas subaquáticas, um salto na superfície e áudio sintetizado em uma sequência animada.**

O criador relata 154 minutos para um filme de 31 segundos, com baleia procedural, simulação de fluidos, sombreamento do oceano e som sintetizado. Suas notas descrevem a inspeção de quadros ampliados e a correção dos respingos antes de renderizar novamente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b98c309a3c226bd24386940f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1bcb86163b677ad0a4172d13.jpg" alt="Salto de baleia com água e som procedurais" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-282"></a>
### Case 282: [Movimento de zebras comparado entre quatro modelos](https://x.com/AI_Screening/status/2118014564457668955) (por [@AI_Screening](https://x.com/AI_Screening))

**Compare marcha, anatomia e estilo de cena na mesma tarefa de animação animal.**

Os quatro clipes empilhados têm os rótulos Gemini 4 Carbon, Fable 5.5, Opus 5.5 e Argon. Manter a composição completa permite observar diferenças no movimento das pernas, no formato do corpo e no tratamento do fundo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/6fdcb38bf56493c314dba5b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/890d1b92800ee622275ec8d7.jpg" alt="Movimento de zebras comparado entre quatro modelos" width="760"></a>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-283"></a>
### Case 283: [Busca de criadores em linguagem natural no Lightreel](https://x.com/lightreelai/status/2118010927199248705) (por [@lightreelai](https://x.com/lightreelai))

**Transforme critérios de criadores em uma busca com limites explícitos de seguidores e visualizações.**

O Lightreel apresenta esta demonstração de busca de criadores sob o rótulo Fable 5.5. O vídeo insere uma consulta sobre criadores em casal com menos de 10,000 seguidores e um vídeo com mais de 100,000 visualizações, depois mostra resultados de vídeos sociais.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5aef4b1766a560a35264c3ed.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1c6d9c1fb3c69b3aa2ee1976.jpg" alt="Busca de criadores em linguagem natural no Lightreel" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-284"></a>
### Case 284: [Um navio voador sobre um mar de nuvens](https://x.com/devteamdrew/status/2118008142403649662) (por [@devteamdrew](https://x.com/devteamdrew))

**Use um filme mais longo para examinar a continuidade entre tomadas com mudanças de luz e clima.**

O criador descreve uma animação de cerca de 100 segundos feita com JavaScript e Python ao longo de 19 horas por várias equipes de agentes. A sequência compartilhada acompanha uma embarcação voadora entre nuvens, o pôr do sol e o luar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/17ef07a780273abf9e9b6c92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a54746701db5f7f829071d2c.jpg" alt="Um navio voador sobre um mar de nuvens" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-285"></a>
### Case 285: [Coração mecânico com corte animado](https://x.com/camperaigg/status/2118002649929056373) (por [@camperaigg](https://x.com/camperaigg))

**Faça um mecanismo revelar suas peças móveis enquanto o movimento principal continua.**

O criador relata uma tarefa de 106 minutos no Blender: um coração mecânico bombeia óleo dourado enquanto sua carcaça abre para revelar pistões e um virabrequim. As notas abordam áudio sintetizado e a identificação de luzes ocultas que causavam reflexos indesejados.

```
Make a mechanical heart and show its insides, use blender.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/157ebee3ce748cdc1e6b7970.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4a862111878dc42939f8e5e4.jpg" alt="Coração mecânico com corte animado" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-286"></a>
### Case 286: [Jardim de pagode voxel flutuante e explorável](https://x.com/legit_api/status/2117994730336252114) (por [@legit_api](https://x.com/legit_api))

**Avalie um ambiente gerado percorrendo suas estruturas e seus elementos aquáticos.**

Este jardim voxel é atribuído a um checkpoint anterior do Fable 5.5. A câmera percorre um pagode, ilhas flutuantes, uma ponte e cachoeiras, mostrando a cena ao nível do solo e de pontos elevados.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/cc4d15bf5103d7eb64f63e29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/22e78c0beb2a6f509bc02739.jpg" alt="Jardim de pagode voxel flutuante e explorável" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-287"></a>
### Case 287: [Uma aventura oceânica feita por oito equipes](https://x.com/0xMovez/status/2117987052419428576) (por [@0xMovez](https://x.com/0xMovez))

**Examine a continuidade entre ação, efeitos e som sintetizado em um filme com várias tomadas.**

O criador relata um filme Three.js de 83 segundos feito por oito equipes de agentes em menos de três horas, com 39 tomadas e som sintetizado. As imagens acompanham uma aventura oceânica com espaçonaves, criaturas marinhas e ondas quebrando.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a46543512fc30e5a33cb2fc3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a307daab219d70fa5bed0c86.jpg" alt="Uma aventura oceânica feita por oito equipes" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-288"></a>
### Case 288: [Apresentação interativa de um hipercarro](https://x.com/shmidtqq/status/2117977426990944736) (por [@shmidtqq](https://x.com/shmidtqq))

**Combine closes do veículo com controles selecionáveis de câmera e pintura.**

O criador apresenta um configurador de hipercarro em Three.js como um único arquivo HTML offline, com geometria e materiais gerados por código. A gravação mostra o veículo vermelho, closes das rodas e da carroceria, reflexos e controles de câmera.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4bd439d08b9f8a320a8851ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/a16368d4c8b7c9a3a5455607.jpg" alt="Apresentação interativa de um hipercarro" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-289"></a>
### Case 289: [Nascimento de uma árvore da vida](https://x.com/notjazii/status/2117972258090357164) (por [@notjazii](https://x.com/notjazii))

**Estruture uma animação curta em torno da transformação visível de uma semente em uma árvore adulta.**

O criador relata uma execução de programação de aproximadamente uma hora com um único prompt. A sequência de 30 segundos passa por uma paisagem árida, uma muda e uma árvore em crescimento antes de revelar um mundo verde sob as nuvens.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/29df8c398a2db37856c01b0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f50b8e7c2a28df7d0d3cd903.jpg" alt="Nascimento de uma árvore da vida" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-290"></a>
### Case 290: [Castelo ambulante com maquinaria interna funcional](https://x.com/camperaigg/status/2117966825048997914) (por [@camperaigg](https://x.com/camperaigg))

**Conecte um rig de caminhada a movimentos mecânicos visíveis e a uma carcaça que se abre.**

O criador relata um fluxo de 133 minutos no Blender com motor a vapor, trens de engrenagens, quatro pernas e oito painéis de carcaça que se abrem. Suas notas descrevem a correção da animação de câmera e a redução do tempo de renderização após identificar uma geometria de grama custosa.

```
Make me Howl's moving castle and also show its internal machinery.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e7e25e7d44993a14ab0405e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8d3b1d734d971e2dd757926c.jpg" alt="Castelo ambulante com maquinaria interna funcional" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-291"></a>
### Case 291: [Uma torrada e um besouro mecânico](https://x.com/flxrnc/status/2117965294224232796) (por [@flxrnc](https://x.com/flxrnc))

**Examine a encenação dos personagens e a continuidade em um breve encontro animado.**

O filme compartilhado, de 40 segundos, mostra um personagem quadrado parecido com uma torrada encontrando um besouro mecânico azul em um campo ao pôr do sol. A fonte atribui o filme ao Fable 5.5 e inclui um link para seu guia de motion design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/d5e16bfd05f1c391cf32f848.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b7ae776a5c29618d061465.jpg" alt="Uma torrada e um besouro mecânico" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-292"></a>
### Case 292: [Um faroleiro em uma tempestade](https://x.com/seeconvm/status/2117965120760365494) (por [@seeconvm](https://x.com/seeconvm))

**Construa uma narrativa curta em torno de um lugar, uma mudança de clima e um desfecho claro.**

O criador descreve um curta Three.js de 60 segundos com quadros renderizados por código, som sintetizado e um arquivo HTML offline. As imagens acompanham um pequeno faroleiro sob chuva e relâmpagos até uma cena ao amanhecer.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/7ca3c1e23eac0ed20511211e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/dfcab72e07d547d9dcb1dbc1.jpg" alt="Um faroleiro em uma tempestade" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-293"></a>
### Case 293: [Uma criatura marinha em uma cidade costeira](https://x.com/BubbleBrain/status/2117963042621178000) (por [@BubbleBrain](https://x.com/BubbleBrain))

**Examine um curta completo para avaliar o movimento dos personagens, as transições e a consistência visual.**

A fonte compartilha uma animação Fable 5.5 de aproximadamente um minuto com uma criatura marinha verde, uma cidade costeira e bolhas flutuantes. O vídeo oferece uma amostra visual concreta para avaliar esse estilo de curta-metragem.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/65db346493bdd9973bec3a4c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/4442bdca5e6a7460f03af731.jpg" alt="Uma criatura marinha em uma cidade costeira" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-294"></a>
### Case 294: [Corridas no tapete comparadas entre três modelos](https://x.com/noclipepe/status/2117914944410628430) (por [@noclipepe](https://x.com/noclipepe))

**Compare a completude das cenas jogáveis, o movimento e o tratamento visual na mesma tarefa de corrida.**

O criador testa um jogo de corrida em um tapete infantil com Fable 5.5, Opus 5.5 e GPT-6 Astra. A gravação mais recente com três painéis e a comparação anterior de dois modelos são mantidas juntas; as notas mostradas no vídeo são avaliações do próprio criador.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ffe3b88099594ba14f536b51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/24d8ea7644cbe19947c8c53a.jpg" alt="Corridas no tapete comparadas entre três modelos" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e214760ff83ad9bfaf202484.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0340fc5579003245dfa99b1.jpg" alt="Corridas no tapete comparadas entre três modelos" width="760"></a></td></tr></table>

[Comparação relacionada · @noclipepe](https://x.com/noclipepe/status/2117729666576302187)

Type: Evaluation | Date: 2026-11-04

---

<a id="case-295"></a>
### Case 295: [Um caminhão se transforma em robô](https://x.com/camperaigg/status/2117914482752299311) (por [@camperaigg](https://x.com/camperaigg))

**Use uma sequência de transformação para examinar o rigging, o contato com o solo e o som sincronizado.**

O criador relata 107 minutos no Blender, incluindo um rig de 51 articulações, um solucionador de contato com o solo, chuva procedural e efeitos sonoros sintetizados. A gravação mostra o caminhão se desdobrando em um robô em pé sobre o asfalto molhado.

```
Make me a transformer truck with animations of its transforming.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/72ef538a8fb4b94f0e2d7e2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ea8537c130cd5623959dc275.jpg" alt="Um caminhão se transforma em robô" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-296"></a>
### Case 296: [Quadros de animação do Fable e do Hunyuan](https://x.com/xbquan/status/2117899651365908855) (por [@xbquan](https://x.com/xbquan))

**Compare quadros correspondentes antes de concluir algo sobre uma animação inteira.**

O autor compartilha dois pares de capturas rotuladas Fable 5.5 e Hunyuan 4. Cada par reúne os resultados dos personagens e do ambiente; essas imagens estáticas permitem uma comparação visual dos quadros mostrados.

<table><tr><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e6c6551a29757e1eb7c31f36.jpg" alt="Quadros de animação do Fable e do Hunyuan" width="760"></td><td valign="top"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/864db255f6fd2807b689d7d7.jpg" alt="Quadros de animação do Fable e do Hunyuan" width="760"></td></tr></table>

Type: Evaluation | Date: 2026-11-04

---

<a id="case-297"></a>
### Case 297: [Uma animação sobre compartilhar luz](https://x.com/abhinavflac/status/2117883591019708740) (por [@abhinavflac](https://x.com/abhinavflac))

**Transforme um tema abstrato em uma narrativa curta com um final visível.**

Após o pedido para mostrar o que significa bondade, o modelo recebe o crédito por uma animação e um som feitos em código. Uma figura luminosa entrega sua luz a uma criança e depois fica mais brilhante enquanto a paisagem ao redor se enche de cores.

```
Show me what kindness means to you
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b888d1a62b4d27ae2fca8226.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/5bd15fc5c234b4b114765d6f.jpg" alt="Uma animação sobre compartilhar luz" width="760"></a>

Type: Demo | Date: 2026-11-04

---

<a id="case-298"></a>
### Case 298: [Uma aldeia voxel entre montanhas](https://x.com/abhinavflac/status/2117377130388656569) (por [@abhinavflac](https://x.com/abhinavflac))

**Explore uma aldeia gerada em várias escalas para examinar sua coerência espacial.**

O criador original compartilha uma aldeia voxel viva com casas, cursos d’água e pequenos moradores, vista da margem, de cima e entre as montanhas ao redor. Um post relacionado em chinês fornece um prompt detalhado da cena.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae5269b0eff86da4580064d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/1e612faf20dd5f5de4ee171b.jpg" alt="Uma aldeia voxel entre montanhas" width="760"></a>

[@cfenghub](https://x.com/cfenghub/status/2117775332535148752)

Type: Demo | Date: 2026-11-02

---

<a id="case-299"></a>
### Case 299: [Composição de pelicano e elefante com quatro modelos](https://x.com/pipeline_os/status/2117719191478513700) (por [@pipeline_os](https://x.com/pipeline_os))

**Compare como diferentes modelos lidam com vários sujeitos interagindo em uma animação.**

A gravação de quatro painéis coloca lado a lado uma tarefa com pelicano, bicicleta, crocodilo e elefante para Gemini 4 Argon, Opus 5.5, Fable 5.5 e Kimi K3.1 Pro. A composição completa preserva o posicionamento e o movimento dos sujeitos de cada modelo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/9db78999efffeffa7ccaca0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/15a45dc0efe3247f0821c8a2.jpg" alt="Composição de pelicano e elefante com quatro modelos" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-300"></a>
### Case 300: [Luta anime de espadas com quadros de impacto](https://x.com/camperaigg/status/2117717189059026969) (por [@camperaigg](https://x.com/camperaigg))

**Sincronize a ação dos personagens, os flashes de impacto, o som e o silêncio intencional.**

O criador relata 66 minutos de programação para uma luta de bonecos de palito de 46 segundos, com capas semelhantes a tecido, armas contrastantes e música e efeitos sintetizados. Suas notas descrevem a correção de um ataque invertido, rastros visuais e a posição do título.

```
Make me a video of 2 stickman fighting, anime style.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/c36c188396aac371a64e31a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/85b670f06d376211c60bf894.jpg" alt="Luta anime de espadas com quadros de impacto" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-301"></a>
### Case 301: [Cervo correndo comparado entre quatro modelos](https://x.com/fawnunwrap/status/2117702487755100543) (por [@fawnunwrap](https://x.com/fawnunwrap))

**Compare o movimento dos membros e o formato do animal com a composição completa da mesma tarefa visível.**

O FawnBench apresenta um cervo correndo em quatro painéis rotulados como uma execução atribuída ao Fable 5.5, Gemini 4 Argon, GPT-6 Astra e Opus 5.5. As imagens constituem uma comparação visual, não um resultado numérico de desempenho medido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3add4d9e0752d0467cbe6065.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/eea598747047797148e19c4e.jpg" alt="Cervo correndo comparado entre quatro modelos" width="760"></a>

Type: Evaluation | Date: 2026-11-03

---

<a id="case-302"></a>
### Case 302: [Um robô atravessa uma cidade inundada](https://x.com/0xMovez/status/2117700681867903169) (por [@0xMovez](https://x.com/0xMovez))

**Examine a continuidade entre reflexos, movimento do personagem e mudanças de visão da câmera.**

O criador relata uma animação Three.js de 42 segundos com quadros renderizados por código, som sintetizado e um único arquivo HTML de renderização offline. As imagens acompanham um robô por uma cidade inundada e tomada pela vegetação até uma cena colorida de águas abertas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f39e1807d1e80422c31530c6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/247f768636339f49d149c787.jpg" alt="Um robô atravessa uma cidade inundada" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-303"></a>
### Case 303: [Uma espada no Blender e seu filme de apresentação](https://x.com/camperaigg/status/2117694354685092255) (por [@camperaigg](https://x.com/camperaigg))

**Separe a construção procedural do recurso da etapa posterior de câmera e som.**

O criador relata ter primeiro gerado uma espada com um script Python e depois pedido um vídeo. A continuação usa um movimento contínuo de câmera no Blender, iluminação de floresta, uma trilha orquestral sintetizada e edição no HyperFrames; o tempo total relatado é de 65 minutos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/3c767f2038ef7d3960c956ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/525304dc7d4016ac33b3d4f8.jpg" alt="Uma espada no Blender e seu filme de apresentação" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-304"></a>
### Case 304: [Animação da aldeia pixelada Lantern Isle](https://x.com/abhinavflac/status/2117693193429139965) (por [@abhinavflac](https://x.com/abhinavflac))

**Examine a atividade local e as transições do dia para a noite em um ambiente animado denso.**

O criador compartilha uma aldeia insular desenhada por código, com moradores, barcos, cachoeiras, lanternas e música. A gravação alterna atividades próximas da aldeia, vistas amplas da ilha e uma sequência noturna com lanternas brilhantes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/e91f1eabab743730dd815c98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/b7d2e578739d25596db1164f.jpg" alt="Animação da aldeia pixelada Lantern Isle" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-305"></a>
### Case 305: [Demonstração de edição de vídeos de jogos no Pause](https://x.com/pausevfx/status/2117676887665447206) (por [@pausevfx](https://x.com/pausevfx))

**Revise um fluxo de edição do material bruto, passando pelas legendas, até uma linha do tempo editável.**

O Pause apresenta esse fluxo sob o rótulo Fable 5.5 para edição de vídeo. A demonstração seleciona momentos de jogos, reenquadra uma câmera de rosto, adiciona legendas e som e abre uma sequência editável no Premiere.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/f0faaeecdaa02683f81e67f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/ae2d32876804bf286f11dc6c.jpg" alt="Demonstração de edição de vídeos de jogos no Pause" width="760"></a>

Type: Demo | Date: 2026-11-03

---

<a id="case-306"></a>
### Case 306: [Um pelicano de bicicleta à beira-mar](https://x.com/pankajkumar_dev/status/2117301455665439210) (por [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Examine a geometria fina e a animação em vistas de câmera próximas e amplas.**

O criador compartilha um pelicano andando de bicicleta de roda alta à beira-mar. A gravação examina penas, pedais e geometria das rodas antes de retornar a vistas mais amplas da orla pavimentada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/66c3c44bcefa684522f95b96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5-5-use-cases/update-2026-11-05/8575912e8f20f48439aea683.jpg" alt="Um pelicano de bicicleta à beira-mar" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="acknowledge"></a>
## 🙏 Agradecimentos

Este repositório foi inspirado pelos criadores, desenvolvedores, equipes de benchmark e comunidades que compartilharam publicamente casos reais de uso do Claude Fable 5.

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@hakmgpt](https://x.com/hakmgpt), [@camperaigg](https://x.com/camperaigg), [@lightreelai](https://x.com/lightreelai), [@0xMovez](https://x.com/0xMovez), [@shmidtqq](https://x.com/shmidtqq), [@flxrnc](https://x.com/flxrnc), [@seeconvm](https://x.com/seeconvm), [@BubbleBrain](https://x.com/BubbleBrain), [@xbquan](https://x.com/xbquan), [@pipeline_os](https://x.com/pipeline_os), [@fawnunwrap](https://x.com/fawnunwrap), [@pausevfx](https://x.com/pausevfx), [@AnikaCodes](https://x.com/AnikaCodes), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@cfenghub](https://x.com/cfenghub), [@shneural](https://x.com/shneural)

*Não podemos garantir que todos os casos estejam atribuídos ao criador original. Se algo precisar ser corrigido, entre em contato conosco e atualizaremos.*

Se você tiver mais casos de uso interessantes para compartilhar, sinta-se à vontade para abrir uma issue ou pull request e ajudar a expandir a biblioteca de casos de uso da Evolink.


[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
