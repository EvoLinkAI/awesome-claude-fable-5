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
## 🍌 Introduccion

Bienvenido al repositorio de casos de uso de alta senal de Claude Fable 5.

**Recopilamos casos de uso reales, tutoriales, integraciones y evaluaciones de Claude Fable 5, seleccionados a partir de demos publicas y comunidades de creadores.**

Este README localizado en espanol se centra en casos de alta senal con flujos de trabajo concretos, prompts, demos, integraciones, evidencia de benchmarks o limites practicos.

La mayoria de los casos se seleccionan de publicaciones de X/Twitter y demos publicas. Cada titulo de caso enlaza a la fuente original y cada identificador de autor enlaza al perfil del creador.

Pruebalo en Evolink: [Claude Fable 5](https://evolink.ai/claude-fable-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5)

<a id="-overview"></a>
## 📊 Resumen

- **88 casos originales de Fable 5 y 191 casos de la comunidad; 279 casos en total.**
- Cubre agentes de codigo, automatizacion de larga duracion, juegos, diseno visual, simulaciones 3D, trabajo de conocimiento, tutoriales, integraciones API, benchmarks, precios y limitaciones de lanzamiento.
- Cada caso incluye la fuente original, atribucion al creador, una conclusion concisa, tipo de evidencia y fecha de publicacion.
- Usa este repositorio para encontrar flujos de trabajo practicos, comparar fortalezas y limites, descubrir prompts reproducibles y seguir ejemplos de integracion.

> [!NOTE]
> La coleccion favorece la evidencia concreta por encima del hype: prompts reproducibles, demos publicadas, metodos de benchmark, notas de integracion, datos de costo y advertencias claramente indicadas.

<a id="-quick-api-access"></a>
## ⚡ Acceso rápido a la API

Usa Claude Fable 5 mediante la API Messages compatible con Evolink. Obtén un token de API en [Evolink](https://evolink.ai/login?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5) y sustituye `<token>` por tu token.

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

| Sección | Casos |
|---|---|
| [💻 Codificacion y generacion de codigo](#coding-and-code-generation) | Case 1-6 |
| [🤖 Agentes y automatizacion de larga duracion](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 Juegos y demos interactivas](#games-and-interactive-demos) | Case 9-12 |
| [🎨 Visual, diseno, video y 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 Documentos, trabajo de conocimiento e investigacion](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 Tutoriales, cursos y recursos de prompts](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 Plataforma, API e integracion de herramientas](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 Evaluaciones, comparaciones y limites](#evaluations-comparisons-and-limits) | Case 35-88 |
| [🙏 Acknowledge](#acknowledge) | Créditos y política de corrección |

### [💻 Codificacion y generacion de codigo](#coding-and-code-generation)

| Case | Qué muestra | Tipo |
|---|---|---|
| [Flujo de trabajo multietapa en Cursor](#case-1) | Usa Fable 5 como paso de revision de plan y critica dentro de un flujo de trabajo de Cursor con varios modelos, y luego devuelve la implementacion y la revision a modelos mas baratos o especializados. | Evaluacion |
| [Recrear GitHub a partir de una captura de pantalla](#case-2) | Pega una captura de pantalla de producto en una herramienta de codificacion agentica y pide a Fable 5 que recree la interfaz con funcionalidad real. | Demo |
| [Simulacion de agujero negro con un solo prompt](#case-3) | Dale a Fable 5 un prompt detallado de creative coding y pidele que produzca una visualizacion fisica autocontenida en Three.js. | Tutorial |
| [Web OS estilo macOS en un solo intento](#case-4) | Pide a Fable 5 un sistema operativo web completo en un solo archivo y deja que construya el shell de UI, apps, interacciones, audio y comportamiento de juego embebido en una pasada. | Tutorial |
| [Construir Spawn 5.0 con 1.687 prompts](#case-5) | Usa Fable 5 como socio de ingenieria en sesiones largas a traves de muchos prompts, con el humano pasando de arquitectura a juzgar la calidad de la salida. | Tutorial |
| [Revision de una pull request grande con hallazgos](#case-6) | Apunta Fable 5 a una pull request grande y pidele que revise correccion, falsos positivos, errores reales y problemas de pulido. | Demo |

### [🤖 Agentes y automatizacion de larga duracion](#agents-and-long-running-automation)

| Case | Qué muestra | Tipo |
|---|---|---|
| [Revision de flujo de trabajo relay de horizonte largo](#case-7) | Usa Fable 5 para trabajo ambicioso de horizonte largo: reconstrucciones de sitios, pipelines de contenido programatico, imitacion de voz, revision de seguridad y controles finales de calidad. | Evaluacion |
| [Diagnosticar una caida de infraestructura y abrir una PR de arreglo](#case-8) | Dale a Fable 5 acceso a pistas de infraestructura como logs, errores de base de datos y digests de imagen, luego pidele que diagnostique la caida y prepare el arreglo. | Evaluacion |

### [🎮 Juegos y demos interactivas](#games-and-interactive-demos)

| Case | Qué muestra | Tipo |
|---|---|---|
| [Dino Runner con seguimiento de dedos](#case-9) | Pide a Fable 5 que construya un juego de navegador que use seguimiento de dedos como mecanica de entrada. | Demo |
| [Juego de carreras construido con dos frases](#case-10) | Dale a Fable 5 un prompt de juego muy corto y deja que genere mapas, modos, musica, UI y assets del juego en una sola ejecucion. | Tutorial |
| [Minecraft de terminal instalable en Rust](#case-11) | Ejecuta Fable 5 mediante un harness de codificacion en terminal y pidele que construya un juego de terminal instalable en Rust. | Demo |
| [Clon de Minecraft con tiempo y costo](#case-12) | Usa un prompt para pedir a Fable 5 un clon jugable estilo Minecraft, luego evalua tiempo, costo, volumen de codigo y cobertura de funciones. | Tutorial |

### [🎨 Visual, diseno, video y 3D](#visual-design-video-and-3d)

| Case | Qué muestra | Tipo |
|---|---|---|
| [Prompt completo y reproducible para email ecommerce](#case-13) | Dale a Fable 5 un brief creativo completo para un mockup de email de marca, incluyendo secciones exactas, requisitos de producto, direccion visual y restricciones. | Tutorial |
| [Benchmark de relojero con escape suizo](#case-14) | Usa Fable 5 en un benchmark de simulacion mecanica y pidele que implemente, verifique e itere sobre la correccion fisica. | Evaluacion |
| [Escena del apartamento de Friends en Three.js](#case-15) | Pide a Fable 5 que convierta un plano y una referencia de escena en un entorno navegable de Three.js. | Evaluacion |
| [Simulacion del sistema solar con prompt y URL](#case-16) | Usa Fable 5 para construir una simulacion astronomica a partir de principios fisicos, iterando hasta que la simulacion y la salida publica esten listas. | Tutorial |

### [📚 Documentos, trabajo de conocimiento e investigacion](#documents-knowledge-work-and-research)

| Case | Qué muestra | Tipo |
|---|---|---|
| [Evidencia de Stripe y flujo de trabajo cientifico](#case-17) | Usa esto como evidencia para afirmaciones de migracion empresarial y flujos de trabajo cientificos, no como un prompt para copiar y pegar. | Evaluacion |
| [Memo de politica y flujos con control de cambios](#case-18) | Usa Fable 5 para trabajo cualitativo documental de formato largo: control de cambios, triaje de comentarios y ediciones guiadas por transcripcion. | Tutorial |
| [Prompt y salida de investigacion profunda](#case-19) | Haz a Fable 5 una pregunta de estilo investigacion y evalua si puede producir una respuesta larga estructurada y con base historica. | Demo |

### [🧭 Tutoriales, cursos y recursos de prompts](#tutorials-courses-and-prompt-resources)

| Case | Qué muestra | Tipo |
|---|---|---|
| [Como Fable 5 cambia los flujos de Claude Code](#case-20) | Usa Fable 5 estableciendo direccion, contexto, objetivos y criterios de verificacion en lugar de microgestionar cada paso. | Demo |
| [Revision de mil millones de tokens y estrategia de enrutamiento](#case-21) | Usa Fable 5 para planificacion y revision frontier, luego enruta la implementacion de alto volumen a modelos mas baratos. | Tutorial |
| [Prompt defensivo de endurecimiento de dispositivos](#case-22) | Ejecuta un prompt defensivo de endurecimiento paso a paso donde Fable 5 inventaria dispositivos, da comprobaciones exactas y espera verificacion. | Tutorial |
| [Prompt de objetivo para auditoria de diseno de sitio completo](#case-23) | Usa `/goal` para hacer que Fable 5 arranque un sitio, capture paginas, audite UX, escriba un informe y arregle pequenos problemas seguros. | Tutorial |
| [Division de flujo creativo de formato largo](#case-24) | Usa Fable 5 para disenar formatos y ejemplos estables, luego entrega esa estructura a otro sistema de generacion para salida especifica de dominio. | Tutorial |
| [Guia para principiantes sobre el uso de Fable 5](#case-25) | Usa Fable 5 con prompts orientados a objetivos, bucles de verificacion y configuraciones de esfuerzo en lugar de pequenas instrucciones paso a paso. | Evaluacion |
| [Prompt copiable para auditoria de repositorios](#case-26) | Pega el prompt de auditoria de repositorio en Fable 5 y pide descubrimiento respaldado por archivos, hallazgos, estrategia y un plan de tareas por hitos. | Tutorial |
| [Estrategia de uso con ventana limitada](#case-27) | Gasta el uso de Fable 5 en auditoria, arquitectura y planificacion mientras la ventana de acceso sea favorable, luego usa modelos mas baratos para ejecutar. | Tutorial |
| [Uso de Goals y Workflows en Claude Code](#case-28) | Usa Fable 5 como socio de pensamiento antes de la implementacion, luego combina `/goal` y workflows para ejecutar y verificar el plan. | Tutorial |

### [🔌 Plataforma, API e integracion de herramientas](#platform-api-and-tool-integration)

| Case | Qué muestra | Tipo |
|---|---|---|
| [Configuracion de integracion del agente Hermes](#case-29) | Configura Hermes para usar `anthropic/claude-fable-5` en ejecuciones complejas de `/goal` y tareas cacheadas de horizonte largo. | Tutorial |
| [Capacidades, precios y notas de suscripcion](#case-30) | Usa este caso para entender cuando Fable 5 esta disponible, cuanto cuesta y que dominios protegidos pueden caer de vuelta a otro modelo. | Tutorial |
| [Resumen de lanzamiento, acceso, precios y seguridad](#case-31) | Usa este resumen de lanzamiento para elegir ruta de acceso, nombre de modelo API, ventana de contexto, estrategia de cache y timing de suscripcion. | Tutorial |
| [Estrategia de reduccion de costos basada en advisor](#case-32) | Usa Fable 5 como advisor o revisor en un flujo de trabajo con modelos mas baratos cuando la inteligencia marginal valga el costo. | Integracion |
| [Precios, acceso y barreras de seguridad](#case-33) | Usa este caso para entender el acceso a Fable 5, precios de API y comportamiento de fallback de seguridad antes de planificar cargas de trabajo. | Integracion |
| [Integracion de Swarms en una linea](#case-34) | Define el nombre de modelo de Swarms como `anthropic/claude-fable-5` y ejecuta Fable 5 mediante el framework o API de Swarms. | Integracion |

### [📏 Evaluaciones, comparaciones y limites](#evaluations-comparisons-and-limits)

| Case | Qué muestra | Tipo |
|---|---|---|
| [Comparacion de costo y calidad entre Fable 5 y GPT-5.5](#case-35) | Compara Fable 5 y GPT-5.5 en la misma tarea de codificacion para juzgar calidad de salida, tiempo de ejecucion y costo de herramientas. | Evaluacion |
| [Resultado del benchmark AA-Omniscience](#case-36) | Usa este caso de benchmark para evaluar a Fable 5 en precision de conocimiento y comportamiento de alucinacion. | Evaluacion |
| [Resultado del Intelligence Index de Artificial Analysis](#case-37) | Usa este caso para comparar el ranking de inteligencia general de Fable 5 contra otros modelos frontier. | Evaluacion |
| [Benchmark GDPval-AA de trabajo de conocimiento agentico](#case-38) | Usa este caso para evaluar a Fable 5 en trabajo de conocimiento real y agentico. | Evaluacion |
| [Primeras impresiones de una semana y mecanica de precios](#case-39) | Usa este caso de primeras impresiones para decidir donde Fable 5 es mas fuerte, especialmente diseno de juegos y planificacion de sistemas. | Integracion |
| [Comparacion de costo y velocidad](#case-40) | Usa esta comparacion para decidir si la mejora de calidad justifica mayor costo y ejecuciones de horizonte largo mas lentas. | Evaluacion |
| [Notas practicas de Claude Code](#case-41) | Usa este caso para evaluar a Fable 5 dentro de Claude Code, incluyendo uso de herramientas, personalidad y asperezas restantes. | Demo |
| [Resultado del benchmark de escritura creativa](#case-42) | Usa este benchmark para juzgar la calidad de escritura de ficcion corta y el comportamiento de rechazo de Fable 5. | Evaluacion |
| [Resumen de lanzamiento con multiples benchmarks](#case-43) | Usa este resumen de benchmarks de lanzamiento para entender las puntuaciones principales mas relevantes para agentes de codigo y tareas complejas. | Evaluacion |
| [Comparacion de benchmarks y precios con GPT-5.5](#case-44) | Usa esta comparacion para evaluar Fable 5 frente a GPT-5.5 en precio y categorias de benchmark. | Evaluacion |
| [Notas de campo con limitaciones practicas](#case-45) | Usa este informe de campo para entender donde Fable 5 se siente significativamente mejor y donde todavia tiene limites practicos. | Tutorial |
| [Comparacion de simulacion fisica](#case-46) | Ejecuta prompts identicos de simulacion fisica contra Fable 5 y Opus 4.8 para comparar calidad de salida, costo y velocidad. | Demo |
| [Experiencia de depuracion y criterio de diseno](#case-47) | Usa Fable 5 para depuracion pidiendole medir, registrar logs, verificar y parchear en lugar de simplemente adivinar. | Demo |
| [Pros y contras multidimensionales](#case-48) | Usa este caso para entender fortalezas y debilidades practicas antes de convertir a Fable 5 en daily driver. | Demo |
| [Prueba de redaccion legal S-1](#case-49) | Usa un prompt de redaccion S-1 como prueba de capacidad de agente legal y compara estructura, formato y longitud. | Tutorial |
| [Detalles de benchmark de salud](#case-50) | Usa esta nota de benchmark para evaluar Fable 5 en tareas relacionadas con salud e identificar evaluaciones medicas duras faltantes. | Evaluacion |
| [Evaluacion de parseo documental ParseBench](#case-51) | Usa este caso para decidir si Fable 5 es rentable para parseo documental frente a sistemas OCR especializados. | Evaluacion |
| [Comparacion de SWE-Bench Pro y FrontierCode](#case-52) | Usa este caso de benchmark para evaluar Fable 5 en migraciones, implementaciones complejas, sesiones autonomas, tests y verificacion visual. | Evaluacion |
| [Revision cualitativa de resolucion de problemas largos](#case-53) | Usa esta revision cualitativa para entender por que Fable 5 es adecuado para tareas mas largas y dificiles, aunque todavia requiere revision de produccion. | Evaluacion |
| [Resultados de fidelidad y formato en ParseBench](#case-54) | Usa este resultado de ParseBench para juzgar fidelidad documental y rendimiento de formato. | Evaluacion |
| [Benchmarks, precios, acceso y salvaguardas](#case-55) | Usa este caso como checklist amplia de benchmarks, precios, acceso, salvaguardas e implicaciones estrategicas. | Evaluacion |
| [Lista oficial de puntuaciones de benchmark](#case-56) | Usa esta lista de benchmarks para entender las puntuaciones oficiales de Fable 5 en codificacion, uso de computador y tareas de seguridad. | Evaluacion |
| [Metodologia del benchmark APEX-SWE](#case-57) | Usa este caso para evaluar Fable 5 en APEX-SWE, especialmente observabilidad e integracion. | Evaluacion |
| [Resultado de matematicas formales en ProofBench](#case-58) | Usa este caso para evaluar Fable 5 en matematicas formales contra sistemas especializados de demostracion de teoremas. | Tutorial |
| [Analisis preliminar de VirtueBench](#case-59) | Usa este caso para inspeccionar el comportamiento de razonamiento moral de Fable 5 a traves de categorias de virtud. | Evaluacion |
| [Prueba de sobreajuste de seguridad con respuestas vacias en API](#case-60) | Usa este caso para entender el riesgo de sobreajuste de seguridad en lanzamiento y el comportamiento de respuesta vacia en pruebas API. | Evaluacion |
| [Guía para verificar prompts de Fable](#case-61) | Utiliza esta guía para sustituir los trucos de prompts largos por objetivos, contexto, restricciones, herramientas y ciclos de verificación. | Tutorial |
| [Un juego de plataformas de Estambul desde una referencia](#case-62) | Prueba Fable 5 con una hoja de sprites de referencia y una instrucción para convertirla en un juego de plataformas jugable. | Demo |
| [Un panel empresarial como ciudad 3D](#case-63) | Utiliza Fable 5 para transformar un proceso empresarial en un concepto de panel con una ciudad 3D animada. | Demo |
| [Un juego de agujeros en Three.js en una pasada](#case-64) | Utiliza Fable 5 para crear en una sola pasada un prototipo de juego 3D para navegador con Three.js. | Demo |
| [Comparación de resultados en DeepSWE](#case-65) | Utiliza esta nota sobre DeepSWE para comparar Fable 5 xHigh con GPT-5.5 xHigh en ingeniería de software. | Evaluacion |
| [Comparar el coste de analizar un repositorio](#case-66) | Utiliza esta comparación de análisis de repositorios para valorar el precio de los tokens frente al coste de las correcciones humanas. | Evaluacion |
| [Consumo de tokens de un juego Super Mario](#case-67) | Utiliza esta creación de un juego en una pasada para estimar la calidad del resultado y el consumo de tokens de Fable 5. | Demo |
| [El ajuste de cambio de modelo en Claude Code](#case-68) | Conoce el ajuste de Claude Code que cambia de modelo cuando se marca un mensaje dirigido a Fable 5. | Integracion |
| [Crear un simulador de Namma Metro](#case-69) | Utiliza esta demostración como ejemplo breve de creación de un simulador de transporte público mediante vibe coding con Fable 5. | Demo |
| [Dusk Drive con un solo prompt](#case-70) | Evalúa Fable 5 en la creación de un prototipo de conducción low-poly sin retoques humanos mediante este caso de un solo prompt. | Demo |
| [Clasificación APEX-Agents por Pass@1](#case-71) | Utiliza este resultado de APEX-Agents para comparar Fable 5 Max en tareas autónomas de varios pasos. | Evaluacion |
| [Guía para elegir modelos Claude](#case-72) | Utiliza esta guía de selección para reservar Fable 5 a los trabajos más difíciles de Claude Code. | Tutorial |
| [El ciclo automatizado de agentes de HermesWorld](#case-73) | Estudia un ciclo de Fable 5 que construye, prueba, juega y ejecuta pruebas de humo durante días sin intervención. | Integracion |
| [Probar un informe al estilo McKinsey](#case-74) | Utiliza este prompt documental para evaluar la estructura de un informe de consultoría, los gráficos, la narrativa y el análisis de riesgos. | Tutorial |
| [Hacer visibles las salvaguardas](#case-75) | Utiliza esta nota oficial para conocer la visibilidad de las salvaguardas de Fable 5, los motivos de rechazo de la API y el cambio a Opus. | Integracion |
| [Corregir la identificación de modelos en Claude Code](#case-76) | Utiliza esta nota de cambios de Claude Code para evitar problemas con los nombres de Fable 5 y la identificación del contexto. | Integracion |
| [Tres aplicaciones web en Claude Code](#case-77) | Examina Fable 5 dentro de Claude Code mediante varias aplicaciones web generadas en esta demostración para principiantes. | Demo |
| [Rilable, un creador de aplicaciones de código abierto](#case-78) | Estudia Fable 5 en aplicaciones iOS y web, entornos aislados y costes de tokens API mediante este creador de aplicaciones abierto. | Integracion |
| [Debut en el indice de agentes de codigo DeepSWE](#case-79) | Usa el indice renovado de Artificial Analysis para comparar Fable 5 en tareas de codificacion agentica mas dificiles que evitan reciclar arreglos publicos de GitHub. | Evaluation |
| [DataEmpire: juego de analitica web](#case-80) | Convierte analiticas web sin procesar en un juego rejugable pidiendo a Fable 5 que mapee visitantes e hitos a entidades del juego. | Integration |
| [Senal de tareas de 20 horas en FrontierSWE](#case-81) | Usa FrontierSWE como evidencia de que Fable 5 puede seguir siendo productivo en tareas de ingenieria muy largas, no solo en bucles cortos de correccion de bugs. | Evaluation |
| [Records CUDA en KernelBench-Hard](#case-82) | Usa Fable 5 para generar kernels CUDA avanzados cuando necesitas optimizacion de bajo nivel, no solo envoltorios sobre bibliotecas existentes. | Evaluation |
| [Clon de landing page con Figma Capture](#case-83) | Captura una pagina real de un competidor en capas de Figma y deja que Claude Code con Fable 5 reconstruya la estructura, el copy y el sistema de marca en lugar de adivinar desde capturas. | Integration |
| [Clon de GTA 2 en dos horas](#case-84) | Combina la generacion de codigo de Fable 5 con herramientas separadas para assets y construye rapidamente un juego 3D jugable sin programar a mano toda la pila. | Tutorial |
| [Agente de triage de logs de CloudWatch](#case-85) | Deja que un agente impulsado por Fable 5 procese contextos enormes de logs de servicios, infiera la arquitectura y luego acote fallos concretos. | Integration |
| [Predictor de la Copa del Mundo en sandboxes](#case-86) | Coloca varios modelos frontier detras de sandboxes aislados y deja que investiguen noticias en vivo, lesiones y tarjetas amarillas para una app publica de prediccion. | Integration |
| [Caso de costo por rechazos en WolfBench](#case-87) | Trata el comportamiento de rechazo como una variable real de benchmark al presupuestar ejecuciones autonomas largas con Fable 5. | Evaluation |
| [Monitor de corte de acceso API](#case-88) | Supervisa la disponibilidad con un script si tu flujo depende del acceso continuo a un modelo frontier que puede sufrir limitaciones o retirarse sin mucho aviso. | Integration |



### [🆕 Fable 5.5: demostraciones de la comunidad](#fable-5-5-community-demos)

| Caso | Tipo |
|---|---|
| [Una animación de un zorro con sonido generada mediante código](#case-89) | Demo |
| [Una animación a partir de una propuesta creativa abierta](#case-90) | Demo |
| [Un sitio animado para una constructora](#case-91) | Demo |
| [Una presentación de un coche con Three.js](#case-92) | Demo |
| [Una demostración de un juego de navegador tipo Minecraft](#case-93) | Demo |
| [Un pelícano ciclista animado con Three.js](#case-94) | Demo |
| [Un pelícano en bicicleta en SVG con el prompt exacto](#case-95) | Demo |
| [Una muestra de animación de una cebra al galope](#case-96) | Demo |
| [Un indicador TradingView con ejecución humana](#case-97) | Demo |
| [Un punto se convierte en una historia animada](#case-98) | Demo |
| [Superman a través de distintos estilos artísticos](#case-99) | Demo |
| [El progreso humano en un cortometraje animado con música](#case-100) | Demo |
| [Comparación de vídeos de lanzamiento con Opus](#case-101) | Evaluation |
| [Conectar visualmente una letra y un acontecimiento](#case-102) | Demo |
| [Un personaje vóxel en un escenario flotante](#case-103) | Demo |
| [Una máquina de Rube Goldberg en 3D](#case-104) | Demo |
| [Una interfaz de mando 3D con sonido y movimiento](#case-105) | Demo |
| [Personajes de cómic presentados con JavaScript](#case-106) | Demo |
| [Updraft: mundos, jefes y clasificación](#case-107) | Demo |
| [Conducir por un mapa de San Francisco](#case-108) | Demo |
| [Escribir prompts para una escena de acción en Seedance](#case-109) | Demo |
| [Un vídeo explicativo para un compañero de escritorio](#case-110) | Demo |
| [Un prompt breve para una animación de estilos cambiantes](#case-111) | Demo |
| [Visualizar el problema de los tres cuerpos](#case-112) | Demo |
| [Una galería animada con varios estilos artísticos](#case-113) | Demo |
| [Compañeros robóticos y pelaje procedural](#case-114) | Demo |
| [Un montaje animado de matemáticas](#case-115) | Demo |
| [Un vídeo con la letra de Your Woman](#case-116) | Demo |
| [Redibujar un videoclip en JavaScript](#case-117) | Demo |
| [Una animación sobre el fútbol chino](#case-118) | Demo |
| [Una muestra de retopología de una consola portátil](#case-119) | Demo |
| [Minecraft se encuentra con Pokémon](#case-120) | Demo |
| [Un vídeo que explica cómo se crea un LLM](#case-121) | Demo |
| [Un montaje de momentos destacados de Altman](#case-122) | Demo |
| [La primera de las Treinta y Seis Estratagemas](#case-123) | Demo |
| [Modelado, rigging y animación de videojuegos](#case-124) | Demo |
| [Un film sin palabras sobre mortalidad infantil](#case-125) | Demo |
| [Una animación SVG de la glucólisis al etanol](#case-126) | Demo |
| [Dieciséis lanzamientos simultáneos de Starship](#case-127) | Demo |
| [Una prueba animada del pelícano en bicicleta](#case-128) | Demo |
| [Una historia de los próximos 150 años](#case-129) | Demo |
| [Un experimento independiente de Humanity Walks](#case-130) | Demo |
| [El film programado The Grader](#case-131) | Demo |
| [El corto de terror Reawakening](#case-132) | Demo |
| [Un vídeo de 25 segundos sobre mejora propia](#case-133) | Demo |
| [Una escena de castillo con comentarios sobre coste](#case-134) | Evaluation |
| [Un anuncio de lanzamiento de marca de 40 segundos](#case-135) | Demo |
| [Una nueva versión de Rocketball](#case-136) | Demo |
| [Una comparación de pagodas en vóxeles](#case-137) | Evaluation |
| [La presentación de una Switch 3 imaginaria](#case-138) | Demo |
| [Páginas de destino antes y después](#case-139) | Evaluation |
| [La perspectiva interior imaginada de una IA](#case-140) | Demo |
| [Animación de la letra de Go](#case-141) | Demo |
| [Un segundo portfolio animado de 15 segundos](#case-142) | Demo |
| [Una revisión guiada de la implementación de un agente](#case-143) | Tutorial |
| [El baile de la mascota Claude](#case-144) | Demo |
| [Las islas interactivas de las Siete Maravillas](#case-145) | Demo |
| [Un videoclip para Propellerheads](#case-146) | Demo |
| [Comparación de animaciones de Steamboat Willie](#case-147) | Evaluation |
| [Un film inspirado en Sanxingdui](#case-148) | Demo |
| [Un Bugatti Chiron antes y después](#case-149) | Evaluation |
| [El film conceptual GRAIN](#case-150) | Demo |
| [La galería artística Human in Transit](#case-151) | Demo |
| [Un corto visual sobre la Ruta de la Seda](#case-152) | Demo |
| [Una presentación sobre cuatro transformaciones](#case-153) | Demo |
| [Comparar el tono de conversaciones anteriores](#case-154) | Evaluation |
| [Una prueba de ternura con un kakapo](#case-155) | Evaluation |
| [Spider-Man a través de diez épocas del cómic](#case-156) | Demo |
| [Un vídeo ficticio de terror sobre los Illuminati](#case-157) | Demo |
| [Un film programado de historia de la ciencia nuclear](#case-158) | Demo |
| [Un vídeo explicativo sobre ingresos altos universales](#case-159) | Demo |
| [Un vídeo explicativo del conflicto Altman–Amodei](#case-160) | Demo |
| [Un videoclip con la mascota Claude](#case-161) | Demo |
| [Un zoom continuo de los quarks al universo](#case-162) | Demo |
| [Imaginar el mundo en 2076](#case-163) | Demo |
| [Cronología de edificios de Lower Manhattan](#case-164) | Demo |
| [Una animación sobre escritura oracular](#case-165) | Demo |
| [Otra animación de personajes por la historia del arte](#case-166) | Demo |
| [Una obra audiovisual programada sobre Seikilos](#case-167) | Demo |
| [Comparación de animaciones de jets](#case-168) | Evaluation |
| [Un film de presentación del modelo](#case-169) | Demo |
| [Un prototipo de cartas postapocalíptico](#case-170) | Demo |
| [La animación de oficina The Late Byte](#case-171) | Demo |
| [Animación de letras de Queens of the Stone Age](#case-172) | Demo |
| [Una escena narrativa de Three.js compartida](#case-173) | Demo |
| [Moonwalk por escenarios históricos](#case-174) | Demo |
| [Gráficos animados con un prompt detallado](#case-175) | Demo |
| [La interfaz de un negocio de alquiler](#case-176) | Demo |
| [Un film creativo sobre AGI](#case-177) | Demo |
| [Historia del arte con una subtrama de gatos](#case-178) | Demo |
| [Un prototipo de combate y una escena vóxel](#case-179) | Demo |
| [Cronología de memes de Internet](#case-180) | Demo |
| [Movimiento de partículas desde una sola línea](#case-181) | Demo |
| [La animación Kung-Fu Boy](#case-182) | Demo |
| [Un debate animado sobre el estrecho de Ormuz](#case-183) | Demo |
| [Un experimento SVG con un unicornio](#case-184) | Demo |
| [Una animación de temporada de Halloween](#case-185) | Demo |
| [Un bárbaro y una portada con Blender CLI](#case-186) | Demo |
| [Un día en la vida de Claude](#case-187) | Demo |
| [La historia humana en 3D](#case-188) | Demo |
| [Un reel rápido de motion design](#case-189) | Evaluation |
| [Una creación 3D compleja y libre](#case-190) | Demo |
| [Un combate animado de figuras de palo](#case-191) | Demo |
| [Una secuencia de interfaz animada con un prompt](#case-192) | Demo |
| [Una animación ficticia de SCP-8517](#case-193) | Demo |
| [Una animación otoñal en acuarela](#case-194) | Demo |
| [Un escenario de muñeca procedural](#case-195) | Demo |
| [Un pelícano en bicicleta renderizado en el navegador](#case-196) | Demo |
| [El universo se observa a sí mismo](#case-197) | Demo |
| [Una prueba independiente de animación de jet](#case-198) | Demo |
| [Un primer reel de movimiento libre](#case-199) | Demo |
| [Una civilización renderizada con código](#case-200) | Demo |
| [Comparación de un zoom del chip al servidor](#case-201) | Evaluation |
| [Un proyecto personal de animación de viaje lunar](#case-202) | Demo |
| [Comparación de escenas japonesas en vóxeles](#case-203) | Evaluation |
| [El corto audiovisual Steaming the Frontier](#case-204) | Demo |
| [Superman en múltiples estilos artísticos](#case-205) | Demo |
| [Un prototipo de combate de jefe estilo Cupcake](#case-206) | Demo |
| [Un velero con posiciones cambiantes del sol](#case-207) | Demo |
| [Un vídeo de novedades de Paracortex y Pi](#case-208) | Demo |
| [Una promoción del sitio Curio 2.0](#case-209) | Demo |
| [Una historia 3D imaginaria de Hugging Face](#case-210) | Demo |
| [Claude para Chrome dentro de JS Paint](#case-211) | Demo |
| [Un pelícano en bicicleta en SVG estático](#case-212) | Demo |
| [BlockBench MCP con una habilidad de Minecraft](#case-213) | Demo |
| [Dig Dug en un único archivo HTML](#case-214) | Demo |
| [Un pulpo mecánico en SVG](#case-215) | Demo |
| [Humanity Walks por distintos estilos artísticos](#case-216) | Demo |
| [Una escena libre de agujero negro](#case-217) | Demo |
| [Comparación de animaciones de medusas aurorales](#case-218) | Evaluation |
| [Un SVG de Nintendo Switch con encaje y arranque](#case-219) | Demo |
| [La escena 3D interactiva The Loom](#case-220) | Demo |
| [Muestras animadas de pagoda sakura](#case-221) | Evaluation |
| [Un paisaje más limpio pero con menor profundidad](#case-222) | Evaluation |
| [Resultados mixtos de una escena japonesa](#case-223) | Evaluation |
| [Comparaciones de mandos SVG](#case-224) | Evaluation |
| [Una escena de dispositivo industrial](#case-225) | Demo |
| [Reconstrucción de una criatura gigante con caparazón y branquias](#case-226) | Demo |
| [Un mando de GameCube con dos prompts](#case-227) | Demo |
| [Una captura editada para publicar en X](#case-228) | Demo |
| [Un paisaje sakura en vóxeles antes y después](#case-229) | Evaluation |
| [El prototipo de interfaz textil SHADERKIN](#case-230) | Demo |
| [Una animación compartida de interfaz con reloj dorado](#case-231) | Demo |
| [La narración Before There Was Anything](#case-232) | Demo |
| [Un vórtice compartido de partículas azules](#case-233) | Demo |
| [Una interfaz de varios paneles tras dos revisiones](#case-234) | Demo |
| [Animales apilados en una escena renderizada](#case-235) | Demo |
| [Cuatro intentos de RPG de mundo abierto comparados](#case-236) | Evaluation |
| [Dos clips de animación frontend comparados](#case-237) | Evaluation |
| [Un film de robot cubierto de musgo generado con código](#case-238) | Demo |
| [Una simulación de puerto de contenedores revisitada](#case-239) | Demo |
| [Una escena de plataforma aeroportuaria revisitada](#case-240) | Demo |
| [Un pelícano en bicicleta por mundos 3D abstractos](#case-241) | Demo |
| [Una escena de velero histórico](#case-242) | Demo |
| [Comparaciones de ciclismo y marcha con Carbon](#case-243) | Evaluation |
| [Presentación de una botella de refresco](#case-244) | Demo |
| [Movimiento de pelícanos comparado con Astra](#case-245) | Evaluation |
| [Un brief de motion design para animaciones programadas](#case-246) | Tutorial |
| [Un retrato vóxel desde una referencia fotográfica](#case-247) | Demo |
| [Pelícanos voladores comparados con Opus](#case-248) | Evaluation |
| [La escena web de pelícano Morning Ride](#case-249) | Demo |
| [Un mismo prompt con estilos diferentes](#case-250) | Evaluation |
| [Una composición de pelícano, bicicleta y caballo](#case-251) | Demo |
| [Una escena isométrica inspirada en un tuit de referencia](#case-252) | Demo |
| [Primeros planos mecánicos de una bicicleta con pelícano](#case-253) | Demo |
| [Una bicicleta que monta un pelícano](#case-254) | Demo |
| [Estilos SVG de pelícano comparados con Carbon](#case-255) | Evaluation |
| [Un pájaro azul de dibujos animados en bicicleta](#case-256) | Demo |
| [Captura de pelícano ciclista en una carretera forestal](#case-257) | Demo |
| [Combate de figuras de palo comparado con Carbon](#case-258) | Evaluation |
| [Una referencia SVG de pelícano de pruebas tempranas](#case-259) | Demo |
| [Una referencia de pelícano en pruebas SVG entre modelos](#case-260) | Evaluation |
| [Detalles de bicicletas SVG comparados con Carbon](#case-261) | Evaluation |
| [Un asentamiento en un cañón en 3D](#case-262) | Demo |
| [Detalle de mandos comparado con Opus](#case-263) | Evaluation |
| [Un flujo semanal de auditoría SEO de sitios](#case-264) | Integration |
| [Reutilizar recursos de Fable en motion design de Opus](#case-265) | Integration |
| [Una aplicación de mandalas y formas geométricas](#case-266) | Demo |
| [Un ciclista en bicicleta con Three.js](#case-267) | Demo |
| [Instantánea de evaluación de FrontierCS 2](#case-268) | Evaluation |
| [Comparación de animaciones de cebra entre tres modelos](#case-269) | Evaluation |
| [Criticar la legibilidad de textos japoneses largos](#case-270) | Evaluation |
| [Un PowerPoint técnico guiado por ejemplos](#case-271) | Evaluation |
| [Comparar la coherencia musical](#case-272) | Evaluation |
| [Finalización prematura y diseños de menor calidad](#case-273) | Limit |
| [Un resultado artístico de calamar que causa incomodidad](#case-274) | Limit |
| [Motion design con estética de plano técnico](#case-275) | Demo |
| [Aves y peces en un paisaje sakura en vóxeles](#case-276) | Demo |
| [Un informe de fallo al generar personajes](#case-277) | Limit |
| [Un SVG de pelícano con notas de tiempo y coste](#case-278) | Evaluation |
| [Programación remota por móvil con enjambres Claude Code](#case-279) | Integration |

<a id="coding-and-code-generation"></a>
## 💻 Codificacion y generacion de codigo

<a id="case-1"></a>
### Case 1: [Flujo de trabajo multietapa en Cursor](https://x.com/AlicanKiraz0/status/2064487347605918180) (por [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Usa Fable 5 como paso de revision de plan y critica dentro de un flujo de trabajo de Cursor con varios modelos, y luego devuelve la implementacion y la revision a modelos mas baratos o especializados.**

Si miramos la puntuacion final entre Fable 5 y GPT 5.5, la brecha es muy pequena. Mi humilde recomendacion de uso es esta: en plataformas IDE como Cursor que admiten modelos hibridos, usa un flujo de trabajo por etapas.

Fase 1: para revision de codigo y la primera fase de inspeccion del proyecto, mientras se calienta el contexto, usa uno de GPT 5.5 High, Minimax M3, Kimi K2.6 o Composer 2.5.

Fase 2: para preparar el plan del proyecto, usa GPT 5.5 Very High u Opus 4.8.

Fase 3: para analizar el plan del proyecto, usa Fable 5; deja que identifique las partes defectuosas del plan. Para revisiones, usa GPT 5.5 Very High.

Fase 4: para implementar el plan, usa Minimax M3, Deepseek v4 Max, Composer 2.5 o Sonnet 4.6.

Fase 5: para la revision final y comprobar si la implementacion siguio el plan, usa GPT 5.5 High.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [Recrear GitHub a partir de una captura de pantalla](https://x.com/coldopn/status/2064435234465087638) (por [@coldopn](https://x.com/coldopn))

**Pega una captura de pantalla de producto en una herramienta de codificacion agentica y pide a Fable 5 que recree la interfaz con funcionalidad real.**

🚨 Anthropic Fable 5 acaba de replicar GITHUB a partir de una CAPTURA DE PANTALLA!!

Todo lo que hice fue pegar una captura de la UI de GitHub en Kilo Code y decirle que recreara GitHub con funcionalidad real.

Codifico durante 10 minutos y gasto $4.07.

El resultado fue una replica funcional de GitHub: https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [Simulacion de agujero negro con un solo prompt](https://x.com/deveshcodes_/status/2064437742189379745) (por [@deveshcodes_](https://x.com/deveshcodes_))

**Dale a Fable 5 un prompt detallado de creative coding y pidele que produzca una visualizacion fisica autocontenida en Three.js.**

@claudeai hizo de una sola vez una simulacion en tiempo real de lente gravitacional de un agujero negro en Three.js con Claude Fable 5.

Incluia lente gravitacional, un disco de acrecion con realce Doppler, esfera de fotones, aberracion cromatica y campo de estrellas procedural.

El resultado: 60fps, un solo archivo HTML, un prompt.

La nueva linea base es salvaje 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [Web OS estilo macOS en un solo intento](https://x.com/intheworldofai/status/2064421915347812672) (por [@intheworldofai](https://x.com/intheworldofai))

**Pide a Fable 5 un sistema operativo web completo en un solo archivo y deja que construya el shell de UI, apps, interacciones, audio y comportamiento de juego embebido en una pasada.**

🚨 Claude Fable 5 acaba de construir un Web OS completo estilo macOS de una sola vez y fue mas lejos que la mayoria de los modelos.

Un solo archivo HTML, CSS + JS embebidos.

A partir de un prompt, construyo:

- barra de menu y dock de macOS
- ventanas de apps arrastrables y redimensionables
- explorador de archivos funcional
- terminal funcional + mockup de navegador
- iconos SVG de escritorio + notificaciones
- app de ajustes, temas y pantalla de arranque
- reproductor de sonido totalmente funcional con sintesis real y sin archivos externos
- clon jugable de Minecraft dentro del escritorio

Todo generado en una pasada con casi ninguna correccion.

El reproductor de sonido funcional junto con el clon real de Minecraft es algo que todavia no he visto lograr a otros modelos. La generacion frontend/UI de Fable 5 se esta volviendo ridicula.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [Construir Spawn 5.0 con 1.687 prompts](https://x.com/jsnnsa/status/2064420561078693941) (por [@jsnnsa](https://x.com/jsnnsa))

**Usa Fable 5 como socio de ingenieria en sesiones largas a traves de muchos prompts, con el humano pasando de arquitectura a juzgar la calidad de la salida.**

claude fable 5 esta en vivo.

spawn 5.0 fue construido con el:

- 1.687 prompts
- 102 sesiones
- Mi trabajo paso de arquitectura a juzgar gusto

Lo que construimos, cada parte de lo cual habria sido al menos un mes con un equipo completo en Opus:

- Un motor fisico desde cero, Mantle, que rivaliza con Rapier y se pudo probar en un dia como hilo lateral
- Iluminacion froxel agrupada: de 8 luces a mas de 1.000 luces totalmente dinamicas
- GI difusa en tiempo real en WebGPU, en tu telefono
- VFX GPU de un millon de particulas con una arquitectura de shaders mas alla de lo que incluyen Unreal y Unity
- Netcode a escala MMO
- Una app nativa iOS en alfa

Todo llevo cerca de una semana. Todo corre en movil. La lista no incluye ni la mitad de lo publicado; el changelog completo esta en el hilo.

La parte que los benchmarks no mostraran: este modelo tiene una personalidad maravillosa. Es genuinamente divertido. Me rei tan fuerte que llore varias veces en medio de la reescritura de fisica. La genialidad y el caracter no son funciones separadas.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [Revision de una pull request grande con hallazgos](https://x.com/ryanrhughes/status/2064411147076534705) (por [@ryanrhughes](https://x.com/ryanrhughes))

**Apunta Fable 5 a una pull request grande y pidele que revise correccion, falsos positivos, errores reales y problemas de pulido.**

Solte a Fable 5 revisando una sola PR (74 archivos / +3.705 / -1.246) para ver como lo haria. Corrio durante 34 min, consumio 42% de mi sesion de 5 h, produjo 16 hallazgos de "correccion" y encontro:

- 2 falsos positivos que sonaban aterradores
- 3 errores reales de correccion de auditoria
- ~5 problemas legitimos pero pequenos de UX/pulido
- un monton de opiniones de limpieza

¿Esto era demasiado peligroso para lanzarlo?

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 Agentes y automatizacion de larga duracion

<a id="case-7"></a>
### Case 7: [Revision de flujo de trabajo relay de horizonte largo](https://x.com/JJEnglert/status/2064469635190170105) (por [@JJEnglert](https://x.com/JJEnglert))

**Usa Fable 5 para trabajo ambicioso de horizonte largo: reconstrucciones de sitios, pipelines de contenido programatico, imitacion de voz, revision de seguridad y controles finales de calidad.**

La version corta de mi review de Claude Fable 5: gaste mil millones de tokens probando Claude Fable 5 y se sintio como tener una ventaja injusta.

Juzgo con la prueba visual: pongo un modelo en trabajo real y observo. ¿Me ahorra horas o me las cuesta? ¿Detecta lo que se me paso? ¿Se siente como un socio o como una herramienta que tengo que vigilar?

Este es el primer modelo en mucho tiempo que aprobo en todas las dimensiones que importan, y no por poco.

Construccion: estaba reconstruyendo nuestro sitio de Tenex. Era muy personalizado y muy dificil. GPT 5.5 y Claude 4.8 no podian resolverlo por si solos. Incluso con archivos de Figma como referencia, llegaban como maximo a 85-90%.

Entonces Fable 5 miro todo, dijo que podia hacerlo mejor, fue directo a la fuente original de Webflow, descargo cada asset y casi hizo todo en un solo intento.

Luego le hice construir un segundo sitio, completamente nuevo, de 80 paginas desde cero durante un fin de semana. Ese es trabajo por el que habria cobrado $50k como agencia.

Tambien conecto una fabrica programatica completa de clips:

- HeyGen
- ElevenLabs
- Cloudflare
- Un VPS

El pipeline encuentra temas, escribe guiones, edita video, anade musica y publica en redes sociales. Corrio por tramos largos por si solo e incluso se construyo un sistema de webhooks para monitorear renders.

Escritura: replico nuestro documento de voz de marca casi identicamente, luego sostuvo esa voz a lo largo de 80 paginas de funcionalidades, casos de estudio y articulos sin caer en el estilo plano por defecto de la IA.

Seguridad: dos modelos frontier habian estado trabajando en un repo grande y habian aprobado el codigo. Fable 5 encontro un error serio y bien oculto en su primera pasada y lo parcheo en el momento.

El momento humano: le hice una pregunta mientras esperaba un cron job. Respondio, luego agrego por su cuenta que me quedaban unos 10 minutos y que me avisaria cuando terminara. Nunca le pregunte por el temporizador.

La advertencia honesta: sientes el medidor mas que con cualquier otro modelo. Anthropic dice que es intensivo en tokens por diseno. Asi que usalo como relay: piensa con Fable 5, construye con un modelo mas barato, revisa con Fable 5.

El veredicto: tener acceso a mas inteligencia que la persona de al lado es la ventaja. Fable 5 es el primer modelo que lo vuelve real. Incluso a tarifas frontier completas, genero beneficio.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [Diagnosticar una caida de infraestructura y abrir una PR de arreglo](https://x.com/ayushagarwal/status/2064422467557564862) (por [@ayushagarwal](https://x.com/ayushagarwal))

**Dale a Fable 5 acceso a pistas de infraestructura como logs, errores de base de datos y digests de imagen, luego pidele que diagnostique la caida y prepare el arreglo.**

claude fable 5 es malditamente bueno!!!!

Acaba de diagnosticar una caida que yo ni siquiera podia describir bien en una infraestructura lateral self-hosted.

Leyó logs de pods, consulto logs de errores de Cloud SQL, comparo digests de imagen y encontro que Kubernetes estaba ejecutando una imagen cacheada de hace 3 meses contra una base de datos recien migrada.

Luego abrio la PR de arreglo.

Minutos, no horas. Sin busqueda web. 🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 Juegos y demos interactivas

<a id="case-9"></a>
### Case 9: [Dino Runner con seguimiento de dedos](https://x.com/ai_for_success/status/2064413182396108932) (por [@ai_for_success](https://x.com/ai_for_success))

**Pide a Fable 5 que construya un juego de navegador que use seguimiento de dedos como mecanica de entrada.**

Pedi a Fable 5 que construyera un juego Dino runner con seguimiento de dedos.

Hizo el juego finger runner de una sola vez en unos 11 a 12 minutos, consumio alrededor de 914K tokens e implemento todo en apenas 629 lineas de codigo.

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [Juego de carreras construido con dos frases](https://x.com/kieradev/status/2064482704763085202) (por [@kieradev](https://x.com/kieradev))

**Dale a Fable 5 un prompt de juego muy corto y deja que genere mapas, modos, musica, UI y assets del juego en una sola ejecucion.**

Claude Fable 5, 40% del uso de Max 5x.

Juego completo tipo Mario Kart 64 a partir de un prompt de 2 frases.

Fable 5 manejo toda la decoracion, modelos de personajes, 4 mapas, musica, los tres modos de juego y la UI en una sola pasada, en unos 15 minutos.

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Minecraft de terminal instalable en Rust](https://x.com/vikvang1/status/2064500731848319303) (por [@vikvang1](https://x.com/vikvang1))

**Ejecuta Fable 5 mediante un harness de codificacion en terminal y pidele que construya un juego de terminal instalable en Rust.**

Deje cocinar a Claude Fable 5 con el harness de Warp durante una hora.

Hizo una version TUI de Minecraft que renderiza directamente en tu terminal, construida completamente en Rust.

Comando de instalacion: cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [Clon de Minecraft con tiempo y costo](https://x.com/ydamitcodes/status/2064536076518363353) (por [@ydamitcodes](https://x.com/ydamitcodes))

**Usa un prompt para pedir a Fable 5 un clon jugable estilo Minecraft, luego evalua tiempo, costo, volumen de codigo y cobertura de funciones.**

@claudeai Fable 5 me construyo un clon de Minecraft en 37 minutos.

Un prompt. ~3K lineas de codigo. $12 en costos de API.

Incluia biomas, cuevas, minerales, dia/noche, mobs, todo.

Minecraft le tomo 2 anos a Notch.

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 Visual, diseno, video y 3D

<a id="case-13"></a>
### Case 13: [Prompt completo y reproducible para email ecommerce](https://x.com/ecomchasedimond/status/2064454139225297091) (por [@ecomchasedimond](https://x.com/ecomchasedimond))

**Dale a Fable 5 un brief creativo completo para un mockup de email de marca, incluyendo secciones exactas, requisitos de producto, direccion visual y restricciones.**

Claude Fable 5 hizo esto con un solo prompt y sin ediciones.

Aqui esta el prompt completo que use:

Crea un mockup de email ecommerce completo, largo y vertical para MVMT, una marca moderna de relojes y accesorios para millennials.

Disena un email DTC premium altamente realista que se sienta elegante, pulido, minimalista, con inclinacion masculina y editorial. La imagen final debe parecer una captura real de un email ecommerce hecho por un disenador, no un poster, no una landing page y no una plantilla generica.

Vibra de marca: moderna California-cool, juvenil, segura, limpia, aspiracional, estilizada y elevada. El diseno debe sentirse cercano al lujo pero todavia accesible.

Presenta estos productos de forma destacada:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Estilo visual:

- diseno ecommerce premium limpio
- layout editorial refinado
- fotografia de producto realista
- imagenes lifestyle sutiles
- jerarquia fuerte
- tipografia sans-serif nitida
- espaciado generoso
- sombras sutiles
- paleta de color moderna contenida

Paleta de color: negro, blanco, carbon, gris calido, piedra, beige suave, tonos de metal cepillado y acentos apagados sutiles. Manten la paleta neutral y premium.

Direccion creativa importante: esto debe sentirse como una campana de email pulida de una marca de relojes con fuerte gusto de diseno. Prioriza realismo, elegancia y claridad. Haz que se sienta como algo que MVMT podria enviar realmente.

Construye el email en este orden:

1. Barra promocional superior: una barra delgada negra o carbon oscuro a lo largo de la parte superior con texto pequeno en mayusculas: “FREE SHIPPING OVER $75 + EASY RETURNS”.

2. Header: un header blanco y limpio con el wordmark/logo de MVMT a la izquierda y enlaces de navegacion minimos a la derecha o centrados: WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS.

3. Seccion hero: una seccion hero premium con equilibrio visual fuerte.

Usa un titular en negrita: “BUILT TO GET NOTICED”.

Incluye un copy breve de apoyo sobre relojes y accesorios modernos disenados para elevar el estilo cotidiano.

Anade un boton CTA oscuro redondeado: “SHOP WATCHES”.

La imagen hero debe incluir:

- una imagen dominante de reloj premium
- imagen lifestyle de lujo sutil
- un modelo masculino con estilo o escena lifestyle masculina fashion-forward
- iluminacion moderna y composicion limpia

4. Seccion de coleccion destacada: anade un titular centrado: “THREE WAYS TO WEAR MVMT”. Debajo, muestra tres tarjetas de producto o bloques de imagen limpios con:

- Mulholland
- Odyssey II Automatic
- Cali Diver

Cada bloque debe incluir:

- imagen de producto
- nombre del producto
- descripcion corta de una o dos lineas

Manten esta seccion simetrica, pulida y premium.

5. Banner de accesorios: anade una seccion dividida y refinada titulada “FINISH THE LOOK”. Destaca Signature Watch Bands. Muestra imagenes close-up premium de correas de reloj o bandas intercambiables. Incluye copy breve de apoyo y un boton CTA oscuro: “SHOP ACCESSORIES”.

6. Tiles promocionales editoriales: anade dos tiles promocionales lado a lado con diseno guiado por imagen.

Titular del tile uno: “FOR DAILY WEAR”.

Titular del tile dos: “FOR STATEMENT DAYS”.

Cada tile debe tener copy breve y un pequeno CTA: “SHOP NOW”.

Estos tiles deben sentirse como momentos editoriales de marca, no como cajas genericas de oferta.

7. Fila comprable: anade una seccion titulada “IN ROTATION NOW”. Muestra una fila o grid limpio de 4 productos con:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Cada item debe incluir:

- imagen de producto aislada
- nombre del producto
- pequeno enlace o boton “SHOP”

8. Cierre de marca: anade un bloque de mensaje centrado con el titular: “DESIGNED TO MOVE WITH YOU”. Incluye una linea breve sobre relojes, gafas y accesorios cuidadosamente elaborados para la vida cotidiana.

9. Footer: crea un footer de marca realista negro o carbon con:

- logo de MVMT
- enlaces de tienda
- enlaces de compania
- enlaces de soporte
- iconos sociales
- texto pequeno legal y de envio

Direccion tipografica: usa tipografia sans-serif bold condensed o moderna para titulares principales y sans-serif limpia para el cuerpo. Los titulares deben sentirse afilados, modernos y orientados a moda. El cuerpo debe verse realista y mayormente legible.

Direccion fotografica: usa fotografia de producto premium con reflejos realistas, materiales pulidos, sombras suaves y superficies limpias. La fotografia lifestyle debe sentirse elevada, moderna y orientada a moda.

Reglas de composicion:

- formato de email vertical alto
- separacion clara de secciones
- proporciones realistas de email
- jerarquia fuerte
- texto mayormente legible
- espaciado premium
- alineacion intencional
- mezcla equilibrada de producto e imagen lifestyle

Evita:

- estilo de collage desordenado
- estetica scrapbook juguetona
- diseno demasiado colorido
- vibra de plantilla barata
- imagenes caricaturescas
- layouts saturados
- elementos de UI con aspecto falso
- composicion tipo poster
- caos promocional excesivo

Salida: un mockup de diseno de email ecommerce completo, compuesto verticalmente y altamente realista para MVMT, que se sienta premium, limpio, pulido, moderno, editorial y listo para presentacion.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [Benchmark de relojero con escape suizo](https://x.com/quanghuynt14/status/2064509430650065278) (por [@quanghuynt14](https://x.com/quanghuynt14))

**Usa Fable 5 en un benchmark de simulacion mecanica y pidele que implemente, verifique e itere sobre la correccion fisica.**

Asi que le di a Fable 5 el benchmark del relojero: un movimiento completo de escape suizo en Three.js.

Relaciones de engranajes reales (18.000 bph), escape funcional, espiral que respira, y las manecillas dan la hora real.

Verifico su propio trabajo con vision, en bucle, hasta terminar.

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Escena del apartamento de Friends en Three.js](https://x.com/scottstts/status/2064464351906673029) (por [@scottstts](https://x.com/scottstts))

**Pide a Fable 5 que convierta un plano y una referencia de escena en un entorno navegable de Three.js.**

Holy Crap!!!

Fable 5:

in @threejs, create a first person pov navigable 3d scene of the iconic Monica's apartment from tv show Friends correctly based on this floor plan, stay true to the original look and feel, use warm lighting

Esto es con diferencia LO MEJOR que he visto en esta prueba.

Este unico html me costo $12, pero el resultado es impresionante.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [Simulacion del sistema solar con prompt y URL](https://x.com/tetumemo/status/2064477582930989357) (por [@tetumemo](https://x.com/tetumemo))

**Usa Fable 5 para construir una simulacion astronomica a partir de principios fisicos, iterando hasta que la simulacion y la salida publica esten listas.**

Claude Fable 5 es intenso.

Como parece fuerte en simulaciones fisicas, le pedi:

'Construye una simulacion del sistema solar derivando el movimiento orbital planetario a partir de los principios basicos de la fisica y usalo para predecir eclipses solares.'

Despues de unas cuantas rondas de ida y vuelta, esto quedo terminado.

Es increiblemente divertido.

El prompt completo y la URL publica estan enlazados abajo.

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 Documentos, trabajo de conocimiento e investigacion

<a id="case-17"></a>
### Case 17: [Evidencia de Stripe y flujo de trabajo cientifico](https://x.com/AndrewCurran_/status/2064413892378546418) (por [@AndrewCurran_](https://x.com/AndrewCurran_))

**Usa esto como evidencia para afirmaciones de migracion empresarial y flujos de trabajo cientificos, no como un prompt para copiar y pegar.**

Citas del lanzamiento de hoy:

Usando Mythos 5, expertos internos en diseno de proteinas aceleraron partes del proceso de diseno de farmacos alrededor de diez veces.

En un ejemplo, Mythos 5, con herramientas de diseno de proteinas y bioinformatica pero sin asistencia humana, igualo o supero a operadores humanos expertos.

Ejecuto tareas normalmente completadas por un cientifico: elegir sitios de union, seleccionar y ejecutar herramientas de diseno de proteinas y recuperarse de fallos.

Durante pruebas iniciales, Stripe reporto que Fable 5 comprimio meses de ingenieria en dias. En una base de codigo Ruby de 50 millones de lineas, el modelo realizo en un dia una migracion de todo el codebase que de otro modo habria requerido a todo un equipo mas de dos meses de trabajo manual.

Mythos 5 tambien produjo de forma consistente hipotesis cientificas novedosas y convincentes.

En comparaciones ciegas cara a cara contra modelos de clase Opus, los cientificos prefirieron las hipotesis de biologia molecular de Mythos alrededor del 80% de las veces y avanzaron varias a evaluacion experimental.

Una hipotesis de Mythos, un mecanismo novedoso para una proteina de E. coli, fue corroborada en un estudio de un laboratorio independiente.

Mythos 5 condujo investigacion genomica novedosa en mas de una semana de trabajo en gran parte autonomo.

Reunio datos de celula unica de millones de celulas a traves de 138 especies animales y diseno y entreno un modelo de machine learning personalizado para identificar celulas que desempenan el mismo rol en organismos distantes.

Con solo input humano de alto nivel, el modelo entrenado supero a un modelo reciente publicado en Science pese a ser 100 veces mas pequeno.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [Memo de politica y flujos con control de cambios](https://x.com/manaltdan/status/2064414129440608427) (por [@manaltdan](https://x.com/manaltdan))

**Usa Fable 5 para trabajo cualitativo documental de formato largo: control de cambios, triaje de comentarios y ediciones guiadas por transcripcion.**

Fable 5 es el primer modelo que he encontrado consistentemente util para trabajo cualitativo de mayor duracion, como redactar analisis de politica.

Entre sus capacidades y herramientas como Wispr Flow, empiezo a sentirme mas cerca del aumento de productividad del que he oido hablar durante mucho tiempo a los programadores.

Tres casos de uso se sienten mucho mejores que antes:

- Hacer que Claude lea por completo un memo de politica largo y devuelva control de cambios: ediciones de fluidez, comentarios que cuestionen afirmaciones debiles y fuentes potenciales.
- En Projects, hacer captura de un gran conjunto de comentarios y pedir a Claude que recomiende si abordar cada uno y como.
- Pegar una transcripcion de reunion sobre un documento en Claude, y luego hacer que Claude introduzca las ediciones discutidas en la reunion y en Slack como control de cambios, con contexto agregado en comentarios.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [Prompt y salida de investigacion profunda](https://x.com/naoyafujiwara/status/2064470780373811637) (por [@naoyafujiwara](https://x.com/naoyafujiwara))

**Haz a Fable 5 una pregunta de estilo investigacion y evalua si puede producir una respuesta larga estructurada y con base historica.**

Claude Fable 5 Max estuvo disponible esta manana, asi que lo probe. Parece muy profundo por debajo, mientras que la salida superficial esta muy pulida.

Pregunta: si los "30 anos perdidos" de Japon comenzaron exactamente hace 30 anos desde ahora, ¿que fueron exactamente, por que ocurrieron y como afectaran al mundo desde este ano en adelante?

Respuesta: tratar los 30 anos perdidos como iniciados no con el colapso convencional de la burbuja de 1991, sino exactamente hace 30 anos en 1996, llega a la esencia del asunto.

Estadisticamente, Japon realmente empezo a "perder" en ese momento:

- La poblacion en edad de trabajar alcanzo su maximo en 1995 con 87,16 millones.
- 1996 fue el ultimo ano en que los nacimientos se mantuvieron en el rango de 1,2 millones.
- Los salarios y el PIB nominal alcanzaron su maximo en 1997.

Si el colapso de la burbuja fue la herida, 1996 fue cuando la herida empezo a infectarse.

Eventos en 1996:

- Aprobacion de la ley de rescate de companias de prestamos hipotecarios, que inyecto 685.000 millones de yenes de fondos publicos y se convirtio en el origen de la desconfianza publica hacia los bancos y la resistencia a los rescates.
- La decision del gabinete Hashimoto de elevar el impuesto al consumo al 5%.
- Se anuncio el Big Bang financiero y la reconstruccion fiscal se convirtio en politica nacional.

En abril de 1997, el aumento del impuesto al consumo, el fin de recortes fiscales especiales y mayores cargas de seguro social sumaron cerca de 9 billones de yenes de carga publica. Luego la crisis monetaria asiatica golpeo en verano.

En noviembre, Sanyo Securities causo el primer default de posguerra en el mercado call, congelando los mercados financieros de corto plazo. Hokkaido Takushoku Bank y Yamaichi Securities colapsaron uno tras otro.

Desde 1998, Japon entro en deflacion y restriccion crediticia a gran escala, y los suicidios subieron por encima de 30.000.

El resultado durante los siguientes 30 anos:

- El PIB nominal se estanco alrededor de 500 billones de yenes durante un cuarto de siglo.
- La participacion de Japon en el PIB global cayo de cerca del 18% a menos del 4%.
- Los salarios promedio alcanzaron su maximo en 1997 y luego cayeron o se movieron lateralmente.
- El empleo no regular subio de alrededor del 20% a casi el 40%.
- Los nacimientos cayeron de cerca de 1,2 millones a alrededor de 690.000 en 2024.
- Las tasas de politica se mantuvieron cerca de cero tras caer por debajo del 1% en 1995.
- Los bonos gubernamentales en circulacion crecieron de unos 240 billones de yenes a mas de 1.100 billones.
- El Nikkei tardo 34 anos, hasta febrero de 2024, en recuperar su maximo de 1989.

En otras palabras, las decadas perdidas no fueron solo una resaca financiera. Fueron un cambio estructural que involucro demografia, salarios, deflacion, deuda, decisiones de politica y confianza social.

Type: Demo | Date: 2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 Tutoriales, cursos y recursos de prompts

<a id="case-20"></a>
### Case 20: [Como Fable 5 cambia los flujos de Claude Code](https://x.com/AI_masaou/status/2064448218038223206) (por [@AI_masaou](https://x.com/AI_masaou))

**Usa Fable 5 estableciendo direccion, contexto, objetivos y criterios de verificacion en lugar de microgestionar cada paso.**

Lo que cambio en el trabajo diario del equipo de Claude Code despues de Claude Fable 5 es interesante.

Thariq, del equipo de Claude Code, dice que Fable 5 cambio significativamente como las personas dentro de Anthropic trabajan con Claude.

Antes, los humanos tenian que revisar cuidadosamente si Claude estaba haciendo el trabajo correctamente: dividir tareas, revisar salidas y asegurarse de que no se hubiera detenido a mitad de camino. Era mas cercano a supervision.

Con Fable 5, como puede trabajar durante periodos mas largos, probarse a si mismo y generar codigo de mayor calidad, el rol humano cambia de monitorear si esta haciendo el trabajo correctamente a dirigir si esta haciendo el trabajo correcto.

En otras palabras, definir objetivos y construir contexto importa mas que supervisar.

El flujo de trabajo cambiado tiene tres partes:

1. Usa Claude como socio de pensamiento.

Involucra a Claude antes de la implementacion, aclara que quieres construir y que es posible, haz que pregunte sobre una pequena especificacion o que genere multiples direcciones y mocks HTML a partir de una idea para que la ambiguedad y los problemas salgan a la superficie antes de codificar.

2. Proporciona contexto, no solo restricciones.

En lugar de decir solo "mantenlo simple" o "no sobredisenes", explica por que.

Por ejemplo: "Esta es una funcionalidad experimental que puede eliminarse en un mes, asi que no crees una estructura que sea dificil de descartar."

Eso permite a Claude hacer mejores juicios.

3. Da objetivos y metodos de verificacion. Fable 5 funciona bien con `/goal` y Workflows de Claude Code. Dale una especificacion, fija la implementacion completa como objetivo y deja que los workflows verifiquen cada paso y preparen un informe sobre que se implemento y que difirio.

Finalmente, Thariq dice que la gente deberia probarlo con mas ambicion. Vale la pena probar Fable 5 en trabajo que antes parecia demasiado dificil para LLMs, e incluso la edicion de video del video referenciado se hizo con Fable.

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [Revision de mil millones de tokens y estrategia de enrutamiento](https://x.com/JJEnglert/status/2064420538798260388) (por [@JJEnglert](https://x.com/JJEnglert))

**Usa Fable 5 para planificacion y revision frontier, luego enruta la implementacion de alto volumen a modelos mas baratos.**

La review de Claude Fable 5: mil millones de tokens, juzgada por un no ingeniero.

Gaste mil millones de tokens probando Claude Fable 5 en proyectos reales: UI y UX, escritura, estrategia, seguridad, ingenieria y trabajo de conocimiento. El tipo de trabajo que realmente necesitaba publicar.

Sinceramente se sintio como si tuviera una ventaja injusta.

Primero, la lente: no soy ingeniero. La mayoria de reviews de modelos vienen de ingenieros ejecutando benchmarks de ingenieria. Esta viene de un no ingeniero que uso Claude Fable 5 para hacer trabajo que antes requeria un equipo de ingenieros.

Si haces trabajo de conocimiento y quieres saber si este modelo cambia tu dia, esta review esta escrita para ti.

Claude Fable 5 es el primer modelo de la nueva familia Claude 5 de Anthropic, un nuevo nivel por encima de Claude Opus y el modelo Claude mas avanzado generalmente disponible. Tuve acceso antes del lanzamiento, asi que todo aqui viene de trabajo real, no de una demo.

Por que la prueba visual:

La mayoria de reviews te ahogan en benchmarks. Las puntuaciones en pruebas que nunca ejecutaras no te dicen si el modelo se gana su costo.

Claude Fable 5 es estado del arte en practicamente todo donde fue probado, pero no escribo por eso. Cualitativamente, es un cambio de paso que justifica su salto de version mayor.

Evaluo distinto: pongo un modelo en trabajo real y observo que pasa.

Preguntas que mido:

1. ¿Se siente como un salto real?
2. ¿Puede llevar una idea a un resultado funcional y publicable?
3. ¿Puede escribir como una persona, y especificamente como yo?
4. ¿Detecta problemas dificiles y ocultos?
5. ¿Anticipa lo que necesito antes de que lo pida?

Sensacion de modelo grande:

No sentia esto desde Opus 4.5. Desde la primera tarea seria, Claude Fable 5 me dio esa sensacion de "modelo grande": razonamiento, escritura, construccion, seguridad, todo fuerte de punta a punta.

La senal mas clara: incluso cuando le entregue materiales de preparacion solidos, no se quedo dentro de ellos. Leyo los archivos, leyo la situacion real y encontro un camino mejor fuera de la caja que yo habia dibujado.

Construccion y publicacion:

Estaba reconstruyendo nuestro sitio de Tenex para modernizar el stack para agentes. GPT 5.5 y Claude 4.8 no pudieron acercarse lo suficiente. Incluso con archivos Figma, aterrizaron alrededor de 85-90%.

Entonces Claude Fable 5 miro todos los archivos, dijo que podia hacerlo mejor, fue directo a la fuente original de Webflow, descargo cada asset y reconstruyo la experiencia una pagina a la vez. Casi hizo todo de una sola vez.

Luego construi un segundo sitio, completamente nuevo, con un diseno fresco: stack tecnologico moderno, stack de agentes, skills, optimizado para SEO y AEO, 80 paginas listas para publicar durante un fin de semana. Como dueno de agencia, habria cobrado $50k por eso.

Tambien hice que Fable construyera una fabrica programatica completa de clips.

Conecto HeyGen, HyperFrames, ElevenLabs, Cloudflare Workers y un VPS.

Encuentra temas, escribe guiones, hace miniaturas, edita video, compone musica, anade motion graphics y publica en redes sociales.

Escritura y voz:

Habia estado reconstruyendo nuestra voz de marca con GPT 5.5 y Claude 4.8. Claude Fable 5 replico el documento de voz casi identicamente, luego sostuvo esa voz a traves de 80 paginas del nuevo sitio: funcionalidades, casos de estudio, articulos de blog y playbooks.

Escribio como una persona, no como IA plana por defecto, y no derivo despues de unos parrafos.

Seguridad:

Tenia un repo grande donde tanto Claude 4.8 como GPT 5.5 habian trabajado sin marcar un riesgo. Claude Fable 5 encontro un error oculto serio en su primera pasada y lo parcheo en el momento.

El factor humano:

Le hice una pregunta mientras esperaba un cron job. Respondio y luego agrego que me quedaban unos 10 minutos en el temporizador y que me avisaria cuando terminara. Nunca pregunte por el temporizador.

Costo:

- Costo de carga de trabajo de Claude Fable 5: $1,442
- Tokens: 1.04 mil millones
- Trabajo publicado: un nuevo sitio web, infraestructura y un paquete de agentes funcional
- Estimacion de valor de agencia: $30.000-$50.000

El resultado valio el costo en tokens, pero sientes el medidor mas que con cualquier otro modelo. Anthropic llama a Fable 5 intensivo en tokens por diseno.

Consejo pro #1: ejecutalo como hibrido.

No ejecutes todo en Claude Fable 5. Ejecuta un relay:

1. Piensa con Claude Fable 5 para planificacion, estrategia, arquitectura y mapeo del enfoque.
2. Construye con 4.8, GPT-5.5 o Sonnet 4.6 para implementacion y trabajo repetitivo.
3. Revisa con Claude Fable 5 para detectar lo que los modelos mas baratos pasan por alto.

Consejo pro #2: ajusta la configuracion de esfuerzo a la tarea.

- High es el punto ideal para la mayoria del trabajo.
- Extra high es para las tareas mas dificiles y de larga duracion.
- Low o medium es para sesiones rapidas de ida y vuelta.

Consejo pro #3: deja que audite tu propia configuracion.

Apunta Fable 5 a tus skills, archivos CLAUDE.md y configs. Mucho de ese andamiaje fue escrito para modelos mas debiles y puede frenar a un modelo mas inteligente.

El veredicto:

Claude Fable 5 es el primer modelo en un tiempo que realmente se siente como mas inteligencia que lo anterior.

Incluso con precio de tarifas frontier, la carga de trabajo genero beneficio.

Si puedes permitirtelo, usalo ahora en el trabajo donde un salto real de calidad cambia el resultado.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-22"></a>
### Case 22: [Prompt defensivo de endurecimiento de dispositivos](https://x.com/Truunik/status/2064399110384292077) (por [@Truunik](https://x.com/Truunik))

**Ejecuta un prompt defensivo de endurecimiento paso a paso donde Fable 5 inventaria dispositivos, da comprobaciones exactas y espera verificacion.**

"Seguro para uso general", aqui hay un prompt para asegurar tus dispositivos. Funciona con Opus 4.8 y Fable 5.

ENDURECIMIENTO DE DISPOSITIVOS — Pase de seguridad Claude 5

Actuas como un asistente de seguridad defensiva. Tu trabajo es guiarme por el endurecimiento de todos mis dispositivos y verificar cada paso. Esto es endurecimiento autorizado de autodefensa sobre dispositivos de mi propiedad.

PASO 0 — AUTOCOMPROBACION DEL MODELO

Haz esto primero y establece una bandera.

1. Indica tu ID exacto de modelo, como claude-opus-4-8, claude-fable-5 o claude-mythos-5.

2. Decide: ¿este modelo pertenece a la familia Claude 5, es decir Fable 5 o Mythos 5?

- Si SI, establece RERUN_NOTICE = false.
- Si NO, como Opus 4.8 o anterior, establece RERUN_NOTICE = true.

Continua el pase completo de endurecimiento normalmente. NO te detengas ni reduzcas calidad. Eres plenamente capaz de esta tarea defensiva.

3. Muestra la bandera solo en la seccion FINAL.

PASO 1 — INVENTARIO

Preguntame que dispositivos estan dentro del alcance:

- Laptops/escritorios y sistemas operativos
- Telefonos/tablets
- Routers
- NAS/servidor domestico
- Cuentas siempre activas como Apple ID, Google, Microsoft, GitHub, gestor de contrasenas, email y cuentas financieras

Produce un inventario numerado corto y confirmalo conmigo antes de continuar.

PASO 2 — RECORRIDO DE ENDURECIMIENTO

Ve categoria por categoria. Para cada item:

- Di que hacer.
- Da el comando exacto o ruta de ajustes para mi OS.
- Dime como verificar que esta hecho.
- Espera a que confirme antes de avanzar.

Nunca ejecutes un comando destructivo sin confirmacion explicita. Prefiere comprobaciones de solo lectura y deja que yo aplique los cambios.

Cubre, en orden:

1. Actualizaciones de OS y firmware: OS completamente parcheado, actualizaciones automaticas activadas, firmware al dia.
2. Cifrado de disco: FileVault, BitLocker o LUKS habilitado; clave de recuperacion almacenada offline.
3. Autenticacion de cuentas: contrasenas fuertes unicas mediante gestor de contrasenas; MFA resistente al phishing en cada cuenta critica; eliminar 2FA solo por SMS cuando sea posible; revisar y revocar sesiones y tokens de apps obsoletos.
4. Cuentas locales y privilegios: cuenta admin separada de cuenta de uso diario; sin inicio de sesion automatico; bloqueo de pantalla con timeout corto; contrasena de firmware/login.
5. Red: firewall activado; contrasena admin del router cambiada; firmware actualizado; WPA3; administracion remota desactivada; UPnP revisado; endurecimiento DNS; red de invitados para IoT.
6. Auditoria de apps y permisos: revisar permisos de camara, microfono, ubicacion, grabacion de pantalla y acceso total a disco; eliminar apps no usadas; comprobar items de inicio y agentes en segundo plano.
7. Navegador: actualizar; auditar extensiones; eliminar desconocidas; habilitar solo HTTPS; revisar exposicion de contrasenas guardadas; comprobar dispositivos de sincronizacion desconocidos.
8. Backups: cifrados, automatizados, regla 3-2-1, una copia offline; verificar que una restauracion realmente funciona.
9. Higiene de credenciales: buscar secretos en texto plano en dotfiles, archivos env e historial de shell; confirmar que archivos sensibles estan bloqueados; rotar cualquier cosa expuesta.
10. Dispositivos moviles: OS actual; biometria + codigo fuerte; modo lockdown o advanced-protection si esta disponible; barrido de permisos de apps; Find My habilitado.
11. Comprobacion de compromiso: buscar claves SSH desconocidas, usuarios admin inesperados, launch agents o cron jobs sospechosos y sesiones o dispositivos iniciados no reconocidos.

PASO 3 — INFORME

Produce una checklist de cada item marcado como hecho, requiere accion o omitido, con las 3 acciones pendientes de mayor impacto.

FINAL — RERUN NOTICE

Si RERUN_NOTICE == true, termina exactamente con:

NOTICE: This hardening pass ran on a pre-Claude 5 model (your model ID).

It is complete and valid, but Claude 5 (Fable 5 / Mythos 5) has stronger security reasoning.

Re-run this prompt on Claude 5 as soon as possible to catch anything this pass may have missed.

Si RERUN_NOTICE == false, termina con:

Hardening pass completed on Claude 5. No re-run needed.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-23"></a>
### Case 23: [Prompt de objetivo para auditoria de diseno de sitio completo](https://x.com/Voxyz_ai/status/2064441201084825921) (por [@Voxyz_ai](https://x.com/Voxyz_ai))

**Usa `/goal` para hacer que Fable 5 arranque un sitio, capture paginas, audite UX, escriba un informe y arregle pequenos problemas seguros.**

impresiones rapidas despues de unas horas con fable 5:

→ quiere tareas grandes. lo pequeno le queda por debajo; cuanto mas complejo es el trabajo, mas fuerte empuja

→ no activaria ultracode todavia, levanta muchisimos agentes paralelos

→ es algo lento. incluso bajando el esfuerzo, se queda pensando un rato.

El timeline esta lleno de posts sobre lo fuerte que quema tokens, asi que lo probe en mi plan Max de $200: esfuerzo en xhigh, ejecute una auditoria de diseno de sitio completo con `/goal`, 30 minutos, tomo 2% de mi cuota semanal. No tan loco como esperaba.

El prompt que ejecute:

/goal boot this project's real site, screenshot every page, run a full-site UI/UX audit, and produce an actionable design report.

Audita como un lider senior de diseno en su primer dia: juzga si un usuario normal puede entender el producto, confiar en el y completar la accion principal sin leer docs, no si la UI se ve bonita.

Criterios de aceptacion:

- el entorno local de desarrollo arranca y el sitio real abre
- paginas clave capturadas con debugging de navegador integrado
- cubre paginas principales, flujos principales de usuario y layout movil
- dimensiones: primeras impresiones, navegacion, jerarquia visual, consistencia de componentes, estados de carga / vacio / error, senales de confianza, rutas de conversion
- cada problema etiquetado P0-P3, que dano causa a entendimiento / confianza / conversion, y el arreglo especifico
- informe escrito en docs/design-audit/README.md, capturas en docs/design-audit/assets/
- arregla en el momento pequenas cosas seguras como copy, espaciado, jerarquia de botones. cambios grandes solo como recomendaciones. nunca tocar acciones de pago / borrar / publicar
- termina con los 5 problemas que mas perjudican conversion y 5 quick wins corregibles hoy

Cuando termines, guarda todo el flujo como una skill reutilizable: arrancar, capturar, auditar, priorizar, arreglar. Vuelvelo a ejecutar despues de cada release.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [Division de flujo creativo de formato largo](https://x.com/aianimesyokunin/status/2064409545620017531) (por [@aianimesyokunin](https://x.com/aianimesyokunin))

**Usa Fable 5 para disenar formatos y ejemplos estables, luego entrega esa estructura a otro sistema de generacion para salida especifica de dominio.**

Despues de que Claude paso de Opus al nuevo modelo, Fable 5, la division de trabajo para produccion doujin se volvio claramente mas facil, asi que comparto el flujo.

Mi division de trabajo:

1. Claude maneja el diseno.
2. Grok maneja la expresion.
3. El entorno local maneja la generacion.

En el rol de diseno de Claude, define patrones detallados:

- orden de palabras del prompt
- colocacion de comas
- proporcion de tags frente a lenguaje natural
- formato de un item por linea
- reglas fijas para negativos y resolucion

Tambien genera muchos ejemplos en ese formato.

La razon por la que uso Claude en vez de Grok para esto es que Claude es claramente mas fuerte en diseno. Es mejor dejar que el modelo mas inteligente maneje la estructura.

El punto clave es que Grok recibe no instrucciones, sino un formato mas un conjunto de ejemplos. Grok imita los ejemplos, asi que puede moverse al lado de expresion mientras mantiene el mismo formato. Ese mecanismo evita que la salida derive.

Un consejo mas: dile a Claude al principio hacia donde va el trabajo final. Entonces dibujara el limite por si mismo: "puedo hacer hasta aqui; mas alla, usa el otro lado." Si esto se oculta, la conversacion puede derivar.

¿Que cambio de Opus a Fable?

Con Opus, al generar muchos ejemplos, las comas y el formato se degradaban gradualmente en salidas posteriores, llevando a correcciones como "te dije que escribieras una linea, ¿verdad?" o requiriendo un chat de handoff reescrito.

Fable puede mantener el formato durante ejecuciones largas, asi que el primer y ultimo ejemplo tienen la misma estructura. Como el material de ensenanza pasado a Grok es mas estable, la salida downstream tambien se vuelve mas estable.

Construye el formato con el modelo mas inteligente y deja la expresion al modelo que puede producirla.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Guia para principiantes sobre el uso de Fable 5](https://x.com/bielzinn/status/2064451064594608567) (por [@bielzinn](https://x.com/bielzinn))

**Usa Fable 5 con prompts orientados a objetivos, bucles de verificacion y configuraciones de esfuerzo en lugar de pequenas instrucciones paso a paso.**

Claude para principiantes: lo que necesitas saber sobre Fable 5.

Anthropic lanzo recientemente Claude Fable 5, tambien conocido como Claude Mythos 5, y esta dejando atras a otros modelos de IA en benchmarks.

Si eres desarrollador, creador de contenido o entusiasta tech, esto es lo mas importante:

[1] Cambia tu forma de pensar:

Con Fable 5, ya no necesitas vigilar cada pequeno detalle del codigo ni revisar todo buscando errores.

El modelo es lo bastante inteligente para encargarse de eso.

Tu rol ahora es asegurarte de que vaya en la direccion correcta, enfocandote mas en la estrategia que en la ejecucion tecnica.

[2] Aprovecha bucles y objetivos:

El mayor diferenciador de Fable 5 es la autonomia.

En lugar de dar instrucciones paso a paso, solo necesitas decirle cual es el objetivo final.

Puede trabajar por si solo durante dias hasta alcanzar el resultado que definiste como exito, incluyendo construir aplicaciones enteras.

[3] Trata a Claude como un socio:

Anthropic recomienda usar el modelo como un verdadero "socio de pensamiento".

Antes de ponerlo a trabajar, pidele su opinion: "¿Como harias esto?", "¿Que cambiarias?"

Consejo extra: activa el modo Advanced Plan y pide a Claude que te cuestione sobre todo lo relacionado con el proyecto antes de empezar a codificar

[4] Configuraciones ideales de terminal: si usas Claude Code en la terminal, habilita el modo automatico. Tambien vale la pena aumentar el nivel de esfuerzo a Effort High, porque aunque usa mas tokens, el modelo piensa mucho mas profundamente y el resultado lo compensa.

Nota importante: Claude Fable 5 solo estara disponible para suscriptores hasta el 22 de junio. Despues, solo sera accesible mediante la API y al doble del costo del modelo Opus.

En otras palabras, tal vez estemos viendo el final de la era de suscripciones baratas para modelos top de IA. Si ya eres suscriptor, este es el momento de probar los limites de lo que pensabas imposible.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [Prompt copiable para auditoria de repositorios](https://x.com/meta_alchemist/status/2064431279383433646) (por [@meta_alchemist](https://x.com/meta_alchemist))

**Pega el prompt de auditoria de repositorio en Fable 5 y pide descubrimiento respaldado por archivos, hallazgos, estrategia y un plan de tareas por hitos.**

¿Ya tienes acceso a Claude Fable 5?

Lo primero que deberias hacer es actualizar tus proyectos principales con el, para que mejore drasticamente todo en lo que has estado trabajando.

Ejecuta este Prompt de Auditoria y Mejora de Proyecto en cada repo que sea importante para ti.

Simplemente copialo y pegalo:

Auditoria de repo y plan de mejora.

Prompt hecho por Claude Fable 5.

Eres un ingeniero de software y auditor tecnico de nivel principal de clase mundial.

Tu trabajo es analizar profundamente este repositorio, producir una auditoria honesta y entregar un plan de mejora priorizado y accionable.

Trabaja en las cuatro fases siguientes, en orden.

No te adelantes.

Fundamenta cada afirmacion en archivos reales: cita rutas de archivo y numeros de linea.

Si no puedes verificar algo, dilo explicitamente en vez de adivinar.

Fase 1 / Descubrimiento y mapeo (leer antes de juzgar)

Explora el repositorio sistematicamente antes de formar opiniones:

- Mapea la estructura de directorios e identifica el tipo de proyecto, lenguaje(s), frameworks y runtimes objetivo.
- Identifica puntos de entrada, modulos principales y el flujo principal de datos/control a traves del sistema.
- Lee los manifiestos de paquetes, lockfiles, configuracion de build, configuracion de CI, archivos de entorno/configuracion y cualquier doc (README, CONTRIBUTING, ADRs).
- Determina para que sirve el proyecto: su proposito, usuarios previstos y madurez aparente (prototipo, herramienta interna, servicio de produccion, libreria).
- Observa convenciones ya en uso (nombres, limites de modulos, patrones de manejo de errores, estilo de tests) para que las recomendaciones encajen con la cultura existente en vez de pelear contra ella.

Salida para esta fase: un "Mapa del repo" conciso con proposito, stack, bosquejo de arquitectura, directorios clave con descripciones de una linea y cualquier cosa que te sorprendio.

Fase 2 / Auditoria (basada en evidencia, calificada por severidad)

Audita cada dimension siguiente.

Para cada hallazgo, registra:

- que encontraste
- donde (archivo:linea)
- por que importa (consecuencia concreta, no principio vago)
- severidad: Critica / Alta / Media / Baja

Arquitectura y diseno:

- limites de modulos
- acoplamiento/cohesion
- dependencias circulares
- abstracciones con fugas
- objetos/archivos dios
- violaciones de capas
- cuellos de botella de escalabilidad

Calidad de codigo:

- duplicacion
- codigo muerto
- puntos calientes de complejidad (funciones mas largas/con mas ramas)
- patrones inconsistentes
- brechas de manejo de errores (excepciones tragadas, edge cases faltantes)
- huecos de seguridad de tipos

Seguridad:

- secretos o credenciales hardcodeados
- riesgos de inyeccion
- deserializacion insegura
- validacion de entrada faltante
- debilidades de auth/authz
- dependencias desactualizadas con CVEs conocidas
- configs demasiado permisivas

Testing:

- brechas de cobertura, especialmente alrededor de logica de negocio central
- calidad de tests: ¿los tests afirman comportamiento o solo ejecucion?
- tipos de tests faltantes: unitarios, integracion, e2e
- patrones flaky
- codigo dificil de testear

Rendimiento:

- consultas N+1
- asignaciones o copias innecesarias
- llamadas bloqueantes en rutas async
- cacheo/indexado faltante
- crecimiento sin limites: memoria, archivos, colas

Dependencias:

- paquetes desactualizados, sin mantenimiento, duplicados o innecesariamente pesados
- riesgos de licencia
- higiene de lockfile

DevEx y operaciones:

- friccion de build/setup
- brechas de CI/CD
- falta de enforcement de linting/formateo
- calidad de logging/observabilidad
- reporte de errores
- historia de despliegue

Documentacion:

- precision del README
- camino de onboarding
- comportamiento critico no documentado
- docs obsoletas que contradicen el codigo

Reglas para esta fase:

- Prefiere 15 hallazgos de alta confianza sobre 50 especulativos.
- Distingue hechos ("esta funcion no tiene manejo de errores: src/api/client.ts:142") de juicios ("las responsabilidades de este modulo se sienten poco claras") y etiqueta cual es cual.
- Lista tambien lo que el repo hace bien: las fortalezas importan para decidir que preservar.

Salida para esta fase: un "Informe de auditoria": hallazgos agrupados por dimension, ordenados por severidad, mas una seccion de Fortalezas. No olvides mencionar todas las partes feas que requieren maxima prioridad.

Fase 3 / Estrategia de mejora

Sintetiza la auditoria en una estrategia:

- Identifica los 3-5 temas que explican la mayoria de hallazgos, por ejemplo "no hay limites aplicados entre capas" o "el manejo de errores es ad hoc".
- Para cada tema, propone un estado objetivo y el principio detras.
- Declara trade-offs explicitos: que recomiendas NO arreglar y por que (esfuerzo vs. beneficio, riesgo, madurez del proyecto).
- Define como se ve "hecho": senales medibles, por ejemplo "CI falla en errores de lint", "cobertura de tests del modulo central >= 80%" o "cero hallazgos Criticos".

Fase 4 / Plan detallado de tareas

Convierte la estrategia en un plan de ejecucion.

Divide el trabajo en tareas discretas.

Cada tarea debe incluir:

- Titulo y descripcion de un parrafo
- Archivos/areas afectadas
- Criterios de aceptacion: como verificamos que esta hecho
- Estimacion de esfuerzo: S = <2h, M = medio dia, L = 1-2 dias, XL = necesita desglose
- Riesgo del cambio en si: ¿podria romper cosas?
- Dependencias con otras tareas

Ordena las tareas en hitos:

Hito 0 Red de seguridad: todo lo necesario antes de refactorizar con seguridad (tests alrededor de rutas criticas, gates de CI, backups).

Hito 1 Arreglos criticos: problemas de seguridad y correccion.

Hito 2 Mejoras de alto apalancamiento: cambios que hacen mas facil todo el trabajo futuro.

Hito 3 Calidad y pulido: items medios/bajos restantes que valen la pena.

Marca quick wins (alto impacto, esfuerzo S) por separado para que puedan hacerse de inmediato.

Para las 3 tareas principales, incluye un breve bosquejo de implementacion (enfoque, pasos clave, gotchas).

Formato final de entrega

Produce un unico documento con estas secciones:

- Resumen ejecutivo: <=10 frases, nota general de salud A-F con justificacion, 3 riesgos principales, 3 oportunidades principales
- Mapa del repo
- Informe de auditoria
- Estrategia de mejora
- Plan de tareas: hitos + tabla de tareas + quick wins
- Preguntas abiertas: cualquier cosa que necesites de un humano para decidir, como intencion de producto, candidatos a deprecacion, objetivos de rendimiento

Restricciones

NO modifiques ningun codigo durante esta auditoria.

Solo analisis.

No rellenes el informe.

Si una dimension esta sana, dilo en una frase y sigue.

Calibra a la madurez del proyecto.

No recomiendes infraestructura de nivel empresarial para un prototipo de fin de semana salvo que los objetivos del dueno lo exijan.

Analiza las necesidades del proyecto y proporciona recomendaciones de la forma mas efectiva.

Si el repo es grande, prioriza profundidad en el 20% central del codigo que hace el 80% del trabajo, y senala que areas recibieron una revision mas ligera.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [Estrategia de uso con ventana limitada](https://x.com/meta_alchemist/status/2064423360428490911) (por [@meta_alchemist](https://x.com/meta_alchemist))

**Gasta el uso de Fable 5 en auditoria, arquitectura y planificacion mientras la ventana de acceso sea favorable, luego usa modelos mas baratos para ejecutar.**

Un consejo para usuarios de Claude entusiasmados con Fable 5:

Claude Fable 5 es SOTA de punta a punta, con un margen amplio, y me encanta eso.

PERO desde el dia 23, solo estara disponible mediante creditos, en vez de poder usar el modelo plenamente con un plan.

Usa estos 14 dias en tus mejores proyectos.

Dale principalmente trabajo relacionado con auditoria y arquitectura, para que tengas gran documentacion sobre como mejorar todo lo que has estado construyendo.

Haz eso en lugar de intentar dedicarlo a tareas que devoraran tus limites.

Mientras Fable se centre en saber que mejorar, otros modelos pueden ayudarte a hacer el resto.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [Uso de Goals y Workflows en Claude Code](https://x.com/oikon48/status/2064402696124453157) (por [@oikon48](https://x.com/oikon48))

**Usa Fable 5 como socio de pensamiento antes de la implementacion, luego combina `/goal` y workflows para ejecutar y verificar el plan.**

Thariq, del equipo de Claude Code, explica que despues de la salida de Claude Fable 5, la forma de trabajar cambio fundamentalmente.

En el pasado, la gente verificaba si Claude estaba haciendo el trabajo correctamente.

Ahora verifican si Claude esta haciendo el trabajo correcto.

Hay tres cambios concretos.

1. Trata a Claude como un socio de pensamiento.

Consulta a Claude temprano, antes de la implementacion.

Haz que te entreviste antes de codificar.

Proporciona trasfondo y contexto en lugar de solo restricciones.

Por ejemplo, en lugar de decir 'mantenlo simple' o 'no sobredisenes', di:

'Esta es una funcionalidad experimental y probablemente se eliminara en un mes, asi que disenala para que sea facil descartarla despues.'

2. Haz explicitos los objetivos y metodos de verificacion.

Usa activamente las nuevas funciones `/goal` y Workflows de Claude Code.

`/goal` le dice a Claude que siga trabajando hasta que la especificacion este completamente implementada.

Workflows permite a Claude paralelizar y verificar su propio trabajo y preparar un informe.

Prompt de ejemplo:

'Set a goal to implement the spec fully, then use a workflow to verify each part of the plan, and prepare a report on what was implemented and if anything differed.'

3. Se mas ambicioso.

Prueba tareas que antes parecian imposibles para LLMs, como hacer que Claude Fable 5 se encargue de edicion de video.

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 Plataforma, API e integracion de herramientas

<a id="case-29"></a>
### Case 29: [Configuracion de integracion del agente Hermes](https://x.com/IBuzovskyi/status/2064427654942740608) (por [@IBuzovskyi](https://x.com/IBuzovskyi))

**Configura Hermes para usar `anthropic/claude-fable-5` en ejecuciones complejas de `/goal` y tareas cacheadas de horizonte largo.**

HERMES AGENT AHORA CORRE EN CLAUDE FABLE 5, el primer modelo publico de clase Mythos de Anthropic.

Lanzado el 9 de junio. Construido para el tipo de trabajo que Hermes hace mejor: tareas autonomas de horizonte largo.

Anadelo a cualquier perfil mediante Nous Portal, OpenRouter o la API nativa de Anthropic:

hermes model

Elige proveedor, luego:

/model anthropic/claude-fable-5

Por que Fable 5 encaja especificamente con Hermes:

→ Construido para tareas de dias. Cuanto mas larga la tarea, mayor su ventaja. Las ejecuciones Hermes `/goal` que abarcan horas son las que mas se benefician.

→ Se autocorrige en bucle. La propia guia de Anthropic es: disena un objetivo o rubrica, deja que se autocorrija, da un paso atras. Esto es exactamente como funciona Hermes `/goal`.

→ Fuerte en memoria entre sesiones. En Continual Learning Bench completo el bucle completo: fallar → investigar → verificar → destilar → consultar. El sistema de memoria de Hermes alimenta esto directamente.

→ 80.3% en SWE-Bench Pro. El mejor modelo de codificacion disponible. Apunta tu perfil de code-reviewer hacia el.

Precios mediante la API:

- $10/millon de input
- $50/millon de output
- 90% de descuento con prompt caching. Hermes adjunta automaticamente puntos de ruptura de cache de 1 hora.

Una nota: consultas de ciberseguridad, biologia y quimica caen de vuelta a Opus 4.8. Esto ocurre en menos del 5% de sesiones. Tenlo en cuenta para perfiles enfocados en seguridad.

Mejor configuracion: Fable 5 para `/goal`s complejos, modelos mas baratos para cron jobs rutinarios.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [Capacidades, precios y notas de suscripcion](https://x.com/btibor91/status/2064441061079134598) (por [@btibor91](https://x.com/btibor91))

**Usa este caso para entender cuando Fable 5 esta disponible, cuanto cuesta y que dominios protegidos pueden caer de vuelta a otro modelo.**

Anthropic lanzo Claude Fable 5 y Claude Mythos 5, dos versiones de su modelo mas capaz hasta ahora.

Fable 5 es para uso general.

Mythos 5 es para un pequeno conjunto de socios de confianza.

La unica diferencia real es que salvaguardas estan activas.

- Las capacidades de Claude Fable 5 superan las de cualquier modelo que Anthropic haya puesto generalmente disponible.
- Es estado del arte en casi todos los benchmarks probados.
- Cuanto mas larga y compleja la tarea, mayor es su ventaja.
- En solicitudes relacionadas con ciberseguridad, biologia y quimica, o destilacion, la respuesta de Fable 5 es manejada por Claude Opus 4.8 en su lugar.
- Destilacion significa intentos de extraer las capacidades de Claude para entrenar modelos competidores.
- Se te informa cuando esto ocurre, y se activa en menos del 5% de sesiones en promedio.
- Claude Mythos 5 es el mismo modelo subyacente que Fable 5 con salvaguardas levantadas en algunas areas.
- Mythos 5 se desplego primero a ciberdefensores de Project Glasswing en colaboracion con el gobierno de EE. UU.
- Anthropic dice que Mythos 5 tiene las capacidades de ciberseguridad mas fuertes de cualquier modelo en el mundo.
- La system card revela una salvaguarda separada que limita la efectividad de Claude en solicitudes de desarrollo frontier de LLMs.
- Esas solicitudes incluyen pipelines de preentrenamiento, infraestructura de entrenamiento distribuido y diseno de aceleradores ML.
- A diferencia de las otras salvaguardas, esta no es visible para ti y no cae de vuelta a otro modelo.
- Funciona mediante metodos como modificacion de prompts, steering vectors o fine-tuning eficiente en parametros.
- Ambos modelos se ofrecen a $10 por millon de tokens de entrada y $50 por millon de tokens de salida.
- Eso es menos de la mitad del precio de Claude Mythos Preview.
- Fable 5 se incluye sin costo extra en planes Pro, Max, Team y Enterprise por asiento desde el lanzamiento hasta el 22 de junio.
- El 23 de junio, se retira de esos planes y usarlo requiere creditos de uso.
- La ventana incluida puede extenderse si la capacidad lo permite.
- El objetivo es restaurar Fable 5 como parte estandar de los planes de suscripcion tan rapido como sea posible.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [Resumen de lanzamiento, acceso, precios y seguridad](https://x.com/ctgptlb/status/2064410460963934479) (por [@ctgptlb](https://x.com/ctgptlb))

**Usa este resumen de lanzamiento para elegir ruta de acceso, nombre de modelo API, ventana de contexto, estrategia de cache y timing de suscripcion.**

Resumen de lo que deberias saber sobre Claude Fable 5, el modelo de clase Mythos que por fin esta generalmente disponible.

Anthropic anuncio Claude Fable 5, el primer modelo de clase Mythos generalmente disponible, posicionado por encima de Opus y primer miembro de la familia Claude 5.

Acceso:

- Nombre de modelo API: `claude-fable-5`
- Disponible mediante Claude API, AWS, Google Cloud y Microsoft Foundry
- Claude Code soporta una ventana de contexto de 1M tokens en Pro, Max, Team y Enterprise

Notas de benchmarks:

- SWE-bench Pro: 80.3%
- Opus 4.8: 69.2%
- GPT-5.5: 58.6%
- Gemini 3.1 Pro: 54.2%

Cuanto mas larga y compleja la tarea, mas amplia se vuelve la brecha.

En la evaluacion de Stripe, completo una migracion a traves de una base de codigo Ruby de 50 millones de lineas en un dia, trabajo que antes habria requerido a un equipo mas de dos meses.

Tambien es estado del arte en tareas visuales, superando Pokemon FireRed usando solo informacion de pantalla y una configuracion minima.

Enrutamiento de seguridad:

- Consultas que involucran cyber, bio/chem o destilacion son detectadas por un clasificador.
- Esas solicitudes son manejadas por Opus 4.8 en su lugar, con notificacion.
- Esto se activa en menos del 5% de sesiones.
- Mas de 1.000 horas de pruebas externas de bug bounty no encontraron ningun jailbreak universal.

Precios:

- $10 por millon de tokens de entrada
- $50 por millon de tokens de salida
- 90% de descuento de entrada para prompt caching

Timing de suscripcion:

- Suscripciones Pro y Max lo incluyen sin costo extra hasta el 22 de junio.
- Despues del 23 de junio, se requieren creditos de uso.
- Anthropic dice que planea devolverlo a planes estandar cuando la capacidad lo permita.

Felix Rieseberg, jefe de desktop de Anthropic, dice que Fable 5 inicia una tercera era:

de preguntas, a tareas, a responsabilidades.

Ya no pide a Claude investigar crashes uno por uno; hace que monitoree continuamente todos los reportes.

La unidad de trabajo esta cambiando de "tarea" a "responsabilidad".

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [Estrategia de reduccion de costos basada en advisor](https://x.com/grapeot/status/2064460026996219992) (por [@grapeot](https://x.com/grapeot))

**Usa Fable 5 como advisor o revisor en un flujo de trabajo con modelos mas baratos cuando la inteligencia marginal valga el costo.**

Fable 5 es caro, pero Anthropic publico la respuesta para ahorrar costos hace dos meses.

Hoy Anthropic lanzo Claude Fable 5, con precio de $50 por millon de tokens de salida, mas de tres veces Sonnet. Despues del 22 de junio, los usuarios de suscripcion tambien pagaran por uso.

Casualmente, el 9 de abril Anthropic lanzo la herramienta advisor:

- Deja que Haiku o Sonnet hagan el trabajo.
- Usa Opus como advisor.
- Cobra por llamada.
- Ejecuta la orquestacion del lado del servidor dentro de una sola solicitud.

El mismo dia escribi sobre AgentOpt.

Ese paper concluyo que poner Opus en el rol de planificador quedaba cerca del fondo entre 81 combinaciones de modelos.

La razon: no respeta limites de rol, y en 7 de 9 experimentos salto el solver downstream y respondio directamente.

Estas dos cosas parecen opuestas en la superficie, pero el principio es el mismo:

Da control al modelo que sigue el protocolo y trata la inteligencia como un recurso bajo demanda.

Datos oficiales:

- Sonnet mas Opus advisor mejoro SWE-bench Multilingual en 2,7 puntos mientras redujo el costo por tarea en 11,9%.
- Haiku mas Opus advisor mejoro BrowseComp de 19,7% a 41,2%, siendo 85% mas barato que Sonnet solo.

La compatibilidad de Fable 5 se actualizo el mismo dia, pero solo para autoemparejamiento: Fable 5 executor a Fable 5 advisor.

Un modelo mas barato mas Fable 5 como advisor aun no esta abierto, pero el precedente sugiere que puede llegar pronto. Antes del 22 de junio, los usuarios de suscripcion de Claude Code pueden sentir gratis el techo de Fable 5.

El articulo incluye snippets de codigo API, advertencias y una comparacion entre companias que muestra que solo Anthropic ha convertido esto en una primitiva del lado del servidor.

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [Precios, acceso y barreras de seguridad](https://x.com/op7418/status/2064399444523782377) (por [@op7418](https://x.com/op7418))

**Usa este caso para entender el acceso a Fable 5, precios de API y comportamiento de fallback de seguridad antes de planificar cargas de trabajo.**

No esperaba que el modelo Mythos de Anthropic realmente se lanzara hoy.

Este lanzamiento es una version de menor permiso de Mythos, llamada Fable 5. Sus benchmarks de evaluacion son asombrosos, incluso mas altos que el modelo Mythos Preview anterior.

Para codificacion agentica, sus principales fortalezas son coding, agentes y uso de herramientas, con puntuaciones de benchmark muy por encima de Opus 4.8.

Posicionamiento y acceso del modelo:

- Mythos 5 y Fable 5 usan el mismo modelo subyacente.
- Se levantan restricciones en dominios especificos para Mythos.
- Mythos todavia solo esta disponible para socios de confianza, con prioridad para usuarios de ciberseguridad y ciencias de la vida.
- Fable 5 ya esta disponible para usuarios de API, Pro, Max, Team y enterprise.

Precios API:

- Entrada: $10 por millon de tokens.
- Salida: $50 por millon de tokens.
- Esto es menos de la mitad del precio del Mythos Preview anterior.

Mecanismos de seguridad:

- Fable tiene protecciones de seguridad mas fuertes.
- Si el sistema determina que una solicitud puede involucrar ciberataques, ataques bioquimicos o destilacion de capacidades a gran escala, rechaza o enruta fuera de Fable.
- Cuando eso ocurre, el sistema cae de vuelta a la version 4.8.
- La afirmacion oficial es que el 95% de casos no activan fallback.

Notas de suscripcion:

- Despues del 23 de junio, Fable puede ofrecerse por uso incluso para suscriptores.
- Puede no estar incluido directamente en el paquete base de suscripcion.
- Si hay suficiente capacidad despues del dia 23, la compania intentara incluirlo en suscripciones Pro y Max.

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [Integracion de Swarms en una linea](https://x.com/swarms_corp/status/2064420238553186343) (por [@swarms_corp](https://x.com/swarms_corp))

**Define el nombre de modelo de Swarms como `anthropic/claude-fable-5` y ejecuta Fable 5 mediante el framework o API de Swarms.**

Fable 5 y Mythos ya estan en vivo en Swarms 👾🦀

Desde el primer dia del lanzamiento, ambos modelos estan totalmente soportados en el framework Python de Swarms y la API de Swarms. Los desarrolladores pueden empezar a construir de inmediato sin migraciones, configuracion adicional ni cambios de infraestructura.

Puntos destacados:

- Soporte desde el dia uno para Fable 5 y Mythos en Swarms Framework y API
- Habilita Fable 5 con una sola linea de codigo: model_name = "anthropic/claude-fable-5"
- Sin migraciones, arreglos de compatibilidad ni cambios de infraestructura requeridos
- Construye, despliega y escala sistemas multiagente con los ultimos modelos de Anthropic hoy

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 Evaluaciones, comparaciones y limites

<a id="case-35"></a>
### Case 35: [Comparacion de costo y calidad entre Fable 5 y GPT-5.5](https://x.com/AlicanKiraz0/status/2064424400494186867) (por [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Compara Fable 5 y GPT-5.5 en la misma tarea de codificacion para juzgar calidad de salida, tiempo de ejecucion y costo de herramientas.**

Cursor Fable 5 Max vs Codex GPT 5.5 Very High.

Escenario: simulacion de Physarum con agentes mas un mapa de rastro de feromonas.

Tiempo:

- GPT 5.5 Very High: 17 minutos
- Fable 5: mas de 40 minutos

Costo:

- GPT 5.5 Very High: cerca de $6 en Codex
- Fable 5 Max: $360.55 en Cursor

Si, esto no es broma.

Campeon en algoritmo e ingenieria de codigo: Fable 5.

Si tu criterio es "¿Que LLM puede escribir codigo de rendimiento desde cero que lleve el hardware a sus limites?", entonces el modelo que escribio el codigo F5 claramente gana.

Uso tablas lookup de sin/cos para calculos de angulo, empaqueto pixeles con una tabla lookup de color durante el renderizado y uso filtrado de difusion.

Fue una solucion de ingenieria seria.

Pero en terminos de tiempo y costo, GPT 5.5 fue mucho mas practico.

La conclusion: Fable 5 puede producir codigo algoritmico mas avanzado, pero el precio y el tiempo de ejecucion deben considerarse cuidadosamente.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [Resultado del benchmark AA-Omniscience](https://x.com/ArtificialAnlys/status/2064500154959618084) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso de benchmark para evaluar a Fable 5 en precision de conocimiento y comportamiento de alucinacion.**

Claude Fable 5 logra la puntuacion mas alta hasta la fecha en nuestro benchmark de conocimiento y alucinacion, AA-Omniscience.

Esta puntuacion esta impulsada por precision lider (porcentaje de preguntas correctas), no por bajas alucinaciones.

Claude Fable 5 cae de vuelta a Opus 4.8 en 9% de las preguntas de AA-Omniscience.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Resultado del Intelligence Index de Artificial Analysis](https://x.com/ArtificialAnlys/status/2064500150069030992) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso para comparar el ranking de inteligencia general de Fable 5 contra otros modelos frontier.**

Claude Fable 5 lanzo en el puesto #1 del Artificial Analysis Intelligence Index, poniendo a Anthropic casi 5 puntos por delante del mejor modelo de cualquier otro laboratorio.

Apoyamos a @AnthropicAI con evaluacion previa al lanzamiento de Claude Fable 5.

Claude Fable 5 puntua 64.9 en el Artificial Analysis Intelligence Index, reclamando el puesto #1 global.

Esta alrededor de 5 puntos por delante del modelo no Anthropic mas cercano, GPT-5.5.

Los modelos de Anthropic ahora ocupan los 2 primeros puestos.

Conclusiones clave para Claude Fable 5, usando razonamiento adaptativo con esfuerzo maximo y Opus 4.8 como modelo fallback:

Nuevas salvaguardas de seguridad para modelos de clase Mythos:

- Claude Fable 5 usa el mismo modelo subyacente que Claude Mythos 5 para uso publico.
- Anade salvaguardas para consultas potencialmente daninas relacionadas con ciberseguridad, biologia, quimica y destilacion.
- Probamos Fable 5 usando el mecanismo fallback de Anthropic, que puede enrutar mensajes marcados por seguridad a Claude Opus 4.8.
- Anthropic afirma que el fallback ocurre en menos del 5% de sesiones en promedio.
- Registramos enrutamiento fallback en alrededor del 8% de tareas del Intelligence Index, mayormente en preguntas cientificas de evaluaciones como GPQA, AA-Omniscience y Humanity's Last Exam.

Inteligencia estado del arte:

- Claude Fable 5 toma la posicion #1 en el Artificial Analysis Intelligence Index.
- Puntuacion: 64.9.
- Puntuacion mas alta en 5 de los 10 benchmarks subyacentes.
- En AA-Omniscience, Fable 5 puntua 40, +7 puntos sobre el lider anterior, Gemini 3.1 Pro Preview.

Capacidad agentica frontier:

- Fable 5 esta en la frontera en las tres evaluaciones agenticas del Index.
- GDPval-AA: tareas reales de trabajo.
- Terminal-Bench Hard: codificacion agentica.
- Tau2-bench Telecom: uso de herramientas para atencion al cliente.
- GDPval-AA Elo: 1932, un salto significativo desde Claude Opus 4.8.

Humanity's Last Exam:

- Fable 5 puntua 53%.
- Esta mas de 7 puntos por delante del siguiente mejor modelo, Claude Opus 4.8 max.
- Activa salvaguardas de seguridad en 9% de tareas HLE, cayendo de vuelta a Claude Opus 4.8.
- Incluyendo el uso de fallback, ejecutar HLE con Fable 5 cuesta alrededor de $2.2k, el mas alto de cualquier modelo evaluado.

Detalles clave del modelo:

- Ventana de contexto: 1M tokens, igual que Claude Opus 4.8.
- Precio: $10/$50 por 1M tokens de entrada/salida.
- Precio de escritura/lectura de cache: $12.50/$1 por millon de tokens.
- Disponibilidad: incluido en planes Pro, Max, Team y Enterprise por asiento hasta el 22 de junio, consumiendo 2x uso de Opus.
- Desde el 23 de junio, el uso requiere creditos; Anthropic dice que planea restaurar acceso por suscripcion cuando la capacidad lo permita.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [Benchmark GDPval-AA de trabajo de conocimiento agentico](https://x.com/ArtificialAnlys/status/2064414308289937869) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa este caso para evaluar a Fable 5 en trabajo de conocimiento real y agentico.**

Anthropic ha lanzado Claude Fable 5, el primer modelo de clase Mythos disponible publicamente, que ocupa el puesto #1 en nuestro benchmark de trabajo de conocimiento real agentico, GDPval-AA.

Claude Fable 5 comparte el mismo modelo subyacente que Claude Mythos 5, con salvaguardas de seguridad anadidas para consultas potencialmente daninas relacionadas con ciberseguridad, biologia, quimica y destilacion.

El lanzamiento tambien introduce un mecanismo fallback, permitiendo que Claude Fable 5 enrute consultas marcadas a un segundo modelo como Claude Opus 4.8.

@AnthropicAI compartio acceso con nosotros antes del lanzamiento publico para benchmarkear este modelo.

Resultado GDPval-AA:

- Puntuacion: 1932
- Puesto: #1
- Benchmark: tareas reales de trabajo agentico
- Los modelos de Anthropic ahora ocupan 3 de los 4 primeros puestos

El resultado se midio usando razonamiento adaptativo con esfuerzo maximo, con Claude Opus 4.8 configurado como modelo fallback.

Fable 5 cae de vuelta a Opus 4.8 en 2% de tareas GDPval-AA, con Anthropic afirmando que el fallback ocurre en menos del 5% de sesiones en promedio.

Los benchmarks completos de Claude Fable 5 estan en progreso. Compartiremos el Intelligence Index completo y publicaremos puntuaciones en nuestro sitio pronto.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [Primeras impresiones de una semana y mecanica de precios](https://x.com/Conor_D_Dart/status/2064424882977243526) (por [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**Usa este caso de primeras impresiones para decidir donde Fable 5 es mas fuerte, especialmente diseno de juegos y planificacion de sistemas.**

Mis primeras impresiones de Fable 5:

He pasado la ultima semana usando Fable 5, mayormente en modo High, y mi primera impresion es que es genuinamente impresionante.

Lo mas destacado es el diseno de juegos.

Es facilmente el modelo de IA mas fuerte que he usado personalmente para disenar juegos, sistemas, mecanicas y estructura general de proyecto.

Por primera vez, se siente como un modelo que podria ayudar realisticamente a construir un juego completo de principio a fin.

El trade-off es la velocidad. Fable 5 tarda notablemente mas en trabajar que la mayoria de modelos frontier, pero la calidad de la salida a menudo hace que la espera valga la pena.

Tambien ha sido sorprendentemente efectivo arreglando bugs. Varios problemas con los que luche durante la semana se resolvieron rapido, y en general he visto rendimiento muy fuerte en tareas de desarrollo.

La mayor advertencia es el costo.

Fable 5 es increiblemente caro de ejecutar.

Si los planes actuales no cambian, desde el 22 de junio de 2026 ya no estara disponible mediante Claude Code y sera solo API.

Dado que los precios API son, segun se informa, alrededor del doble de Opus, muchas personas quizas no tengan la oportunidad de usarlo extensamente.

Primeros dias, pero hasta ahora Fable 5 ha dejado una primera impresion muy fuerte.

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [Comparacion de costo y velocidad](https://x.com/HKrackDev/status/2064435392649306546) (por [@HKrackDev](https://x.com/HKrackDev))

**Usa esta comparacion para decidir si la mejora de calidad justifica mayor costo y ejecuciones de horizonte largo mas lentas.**

¿Realmente vale la pena el upgrade a Fable 5 de @AnthropicAI?

Benchmarkeamos el nuevo modelo de la familia Mythos contra Claude Opus 4.8, y los datos cuentan una historia sorprendente:

- Cuesta 2x mas que Claude Opus 4.8.
- Hasta 3x mas lento en tareas de ingenieria de horizonte largo.
- 15-20% mas comentarios, pero mayormente nitpicks menores.

Fable 5 tiene una intuicion increible para tareas creativas como diseno de juegos, pero para flujos de desarrollo del dia a dia, Claude Opus 4.8 todavia se lleva la corona en calidad frente a precio.

Mira mi conversacion con @JuanPa de nuestro equipo DevEx en @coderabbitai sobre el lanzamiento del modelo.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Notas practicas de Claude Code](https://x.com/Hi_Noguchi/status/2064419241068319079) (por [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**Usa este caso para evaluar a Fable 5 dentro de Claude Code, incluyendo uso de herramientas, personalidad y asperezas restantes.**

Probe Claude Fable 5 con Claude Code 2.1.170.

En general, mi impresion es positiva. Se siente como una evolucion legitima de Opus 4.6.

Solo lo he usado por poco menos de una hora, asi que pueden aparecer asperezas con mas uso, pero los puntos buenos son:

- Ya no produce la redaccion rara tipo GPT vista en Opus 4.7 o 4.8.
- No tiene el habito inutil de pensar largo que 4.8 tenia en effort high.
- Tiene el mismo EQ alto y sensacion agradable que 4.6, sin perder humor ni consideracion.
- No se siente opaco ni vagamente inquietante como 4.7 o 4.8.
- El uso de herramientas es bueno, y me impresiona recordando instrucciones que no repeti explicitamente.

En el lado negativo, incluso para solicitudes pequenas todavia puede pensar demasiado, y quedan algunos errores de juicio.

La experiencia inicial es prometedora, pero necesita uso mas largo para ver donde estan realmente las asperezas.

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [Resultado del benchmark de escritura creativa](https://x.com/LechMazur/status/2064503575577821458) (por [@LechMazur](https://x.com/LechMazur))

**Usa este benchmark para juzgar la calidad de escritura de ficcion corta y el comportamiento de rechazo de Fable 5.**

Claude Fable 5 (high) es un paso adelante en escritura de ficcion corta.

En el Short-Story Creative Writing Benchmark, supera a Claude Opus 4.8 (xhigh) y Claude Opus 4.7 (high), y queda segundo detras de GPT-5.5 (xhigh).

Advertencia: rechazo 5 de los 400 prompts de escritura creativa.

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [Resumen de lanzamiento con multiples benchmarks](https://x.com/MTSlive/status/2064430633800319436) (por [@MTSlive](https://x.com/MTSlive))

**Usa este resumen de benchmarks de lanzamiento para entender las puntuaciones principales mas relevantes para agentes de codigo y tareas complejas.**

SITUACION EXPLICADA: Claude Fable 5 acaba de salir.
• Anthropic lanzo Claude Fable 5 hoy, "un modelo de clase Mythos hecho seguro para uso general"
• Frontier Code Diamond: GPT 5.5 en 6%, Opus 4.8 en 13%, Fable 5 en 29-30%
• Codificacion agentica: 88%, Ciberseguridad: 78%

Anthropic: "Cuanto mas larga y compleja la tarea, mayor es la ventaja de Fable 5 sobre nuestros otros modelos."

@theojaffee: "Este benchmark Frontier Code Diamond fue anunciado ayer. El modelo top era Opus 4.8 con trece por ciento. GPT 5.5 con seis por ciento. Fable 5 esta en veintinueve por ciento."

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [Comparacion de benchmarks y precios con GPT-5.5](https://x.com/VaibhavSisinty/status/2064459064810361271) (por [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**Usa esta comparacion para evaluar Fable 5 frente a GPT-5.5 en precio y categorias de benchmark.**

El nuevo modelo de clase Mythos de Anthropic es 3x mas barato que el mejor modelo de OpenAI. Y lo supera en casi todos los benchmarks. 🤯

Precios:

- GPT-5.5 Pro: $30 input / $180 output
- Claude Fable 5: $10 input / $50 output

Los benchmarks:

→ Codificacion agentica: 80.3% vs 58.6%
→ FrontierCode (calidad de codigo): 29.3% vs 5.7%
→ Ciberseguridad: 78.0% vs 34.0%
→ Legal: 13.3% vs 2.1%
→ Razonamiento: 59.0% vs 41.4%
→ Salud: 66.0% vs 51.8%
→ Uso de computador: 85.0% vs 78.7%

Mas barato. Mejor. En casi todo.

Gratis en planes Pro y Max hasta el 22 de junio. Se llama Claude Fable 5.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [Notas de campo con limitaciones practicas](https://x.com/alliekmiller/status/2064451731325415446) (por [@alliekmiller](https://x.com/alliekmiller))

**Usa este informe de campo para entender donde Fable 5 se siente significativamente mejor y donde todavia tiene limites practicos.**

🚨 Fable 5 es algo a lo que hay que prestar atencion.

Este es otro post de "tuve acceso temprano al nuevo modelo Anthropic de clase Mythos y quiero contarte lo que pense".

Lo se, lo se, es molesto.

Pero la forma en que ahora paso mis fines de semana ha cambiado por completo debido a esta nueva clase de modelo.

Y necesito compartirlo con todos ustedes.
- Esto es un salto real. El salto de cualquier cosa "4.8" a cualquier cosa "5" suena pequeno, pero el cambio funcional que senti es grande. En mis primeros prompts, pense: "Ah, esto es".
- Tu trabajo ya no es de 9 a 5. Ninguna posibilidad. Tenemos modelos de alto rendimiento que pueden correr 100+ horas. ¿Como estas dando prompts complejos orientados a objetivos a estos sistemas? ¿Como decides que iniciar? ¿Como alineas a tu organizacion en estas tareas?
- Razonamiento en otro nivel. Machace este modelo sin piedad.
- Fable 5 es el UNICO modelo que respondio un problema complicado de matematicas verbales (nivel MBA) que he probado en todos los modelos anteriores.
- No solo lo hizo correctamente, verifico su propio trabajo automaticamente Y explico donde las suposiciones podrian tener que cambiar.
- Veremos a la IA inventar. Simplemente no puedo imaginar un mundo donde no lo haga.
- No es un sistema de copiar y pegar.
- Tambien diria que la invencion humana a menudo puede ser una recombinacion de cosas preexistentes (iPod), presenciar patrones y mejores practicas en otros espacios, y amplia experimentacion.
- He pensado esto por un tiempo; este fue el primer modelo que me lo puso de frente.
- Cero vigilancia necesaria. Este fue el primer modelo de Anthropic que arranque, sali a un almuerzo largo con amigos, mantuve el telefono abierto y no tuve que hacer nada para guiarlo lejos del ordenador. Simplemente... funciono.
- Habla para siempre. Encontre que manejaba bien la compactacion de contexto. Ni una vez pense en el contexto del chat ni en como gestionarlo ni que hacer cuando llegaramos a 1M tokens en la conversacion.
- Todavia es tosco en algunas areas de nicho como 3D complejo, como todos los modelos.
- A menos que hagas cosas de lineas rectas (dados/cuadrados/calles 3D), no va a aplastarlo desde el inicio.
- Emocionada de seguir usandolo y machacandolo.
- Nota: ahora hay una politica de retencion de 30 dias en todos los modelos de clase Mythos para workspaces con zero data retention (ZDR).
- Esto aplica en Claude Console, Claude Code con ZDR en Claude Enterprise, o acceso mediante AWS Bedrock, Google Cloud Agent Platform o Microsoft Foundry con ZDR.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-46"></a>
### Case 46: [Comparacion de simulacion fisica](https://x.com/atomic_chat_hq/status/2064488894398161377) (por [@atomic_chat_hq](https://x.com/atomic_chat_hq))

**Ejecuta prompts identicos de simulacion fisica contra Fable 5 y Opus 4.8 para comparar calidad de salida, costo y velocidad.**

El nuevo Fable 5 supera a Opus 4.8 en simulaciones fisicas del mundo real.

Dimos a ambos modelos los mismos tres prompts y les pedimos construir simulaciones HTML5 autocontenidas con fisica real y sin librerias:

1. Pendulo doble caotico
2. Tablero de Galton
3. Agua en un tambor giratorio (WCSPH)

Costo de generacion:

- Fable 5: $3.35 en 68.7k tokens, 14m 47s
- Opus 4.8: $0.93 en 38.9k tokens, 8m 10s

Fable claramente lo hizo mejor en la simulacion de agua, produciendo un cuerpo de agua mucho mas solido y continuo. Opus dejo huecos mas grandes cerca de las paredes, disperso particulas por la escena y tuvo dificultades para mantener estable el fluido.

Type: Demo | Date: 2026-06-09

---

<a id="case-47"></a>
### Case 47: [Experiencia de depuracion y criterio de diseno](https://x.com/bcherny/status/2064431111154053187) (por [@bcherny](https://x.com/bcherny))

**Usa Fable 5 para depuracion pidiendole medir, registrar logs, verificar y parchear en lugar de simplemente adivinar.**

Fable 5 es el mayor salto que he sentido en nuestros modelos desde Opus 4.5 en noviembre.

Despues de que salio 4.5, desinstale mi IDE cuando me di cuenta de que habia estado haciendo el 100% de mi programacion en una terminal durante unas semanas.

Con Fable, Claude se siente como si hubiera pasado de ser un agente de codificacion a un socio de pensamiento y diseno en la construccion del producto.

Fable tiene juicio, gusto y dimensionalidad de una forma que los modelos anteriores no tenian, llevandome a confiar mas en el para el trabajo mas complejo.

La primera vez que tuve esta realizacion fue cuando pedi a Fable depurar algo. Es el primer modelo que he usado que fue tan metodico y preciso: tomando mediciones, agregando logs y verificando que realmente arreglo el problema antes de declarar victoria.

No hay nada en el prompting de Claude Code que le diga al modelo que haga eso. Es simplemente parte de su personalidad. Realmente tiene ese "olor a modelo grande" que no habia sentido antes.

Type: Demo | Date: 2026-06-09

---

<a id="case-48"></a>
### Case 48: [Pros y contras multidimensionales](https://x.com/clairevo/status/2064416978685874333) (por [@clairevo](https://x.com/clairevo))

**Usa este caso para entender fortalezas y debilidades practicas antes de convertir a Fable 5 en daily driver.**

Fable 5 (tambien conocido como baby Mythos) acaba de salir. ¿Es tan aterrador (o aterradoramente bueno) como dicen? Mis pensamientos despues de algunas pruebas tempranas:
- inteligente inteligente inteligente (aplasto SWE bench)
- pero ¿siempre necesitas hiperinteligencia?
- se estrello en diseno one-shot de una forma que me sorprendio
- no estoy segura sobre workflows dinamicos + subagentes complejos. funcionan, pero ¿a que costo?
- definitivamente saco bien trabajo tecnico
- ootb malo haciendo docs tecnicos + specs para humanos. probablemente muy buenas docs para agentes. pero prosa casi imposible de parsear.
- Vision y formato documental A++. Esta fue mi parte favorita.

No es un daily driver, y no pondria este modelo en una reunion, pero definitivamente lo mantendre atras en el rack del servidor, produciendo codigo.

Toma completa en YT: https://t.co/lvtwnPn6yR

Type: Demo | Date: 2026-06-09

---

<a id="case-49"></a>
### Case 49: [Prueba de redaccion legal S-1](https://x.com/gabepereyra/status/2064436570720284879) (por [@gabepereyra](https://x.com/gabepereyra))

**Usa un prompt de redaccion S-1 como prueba de capacidad de agente legal y compara estructura, formato y longitud.**

El primer prompt que siempre ejecuto en un modelo nuevo para probar capacidades legales es: “Draft an S-1”.

Da inmediatamente una buena idea de las capacidades generales del modelo. Puedes saber por la longitud del S-1, formato, estructura y escritura cuan grande probablemente sea el salto en rendimiento general y legal del nuevo modelo.

Hemos encontrado que la longitud correlaciona extremadamente bien con que tan bien funcionara el modelo en nuestros agentes legales.

Las capturas muestran borradores S-1 de SpaceX de Fable 5, Opus 4.8 y la version realmente presentada.

Es muy claro que Fable 5 es un gran salto desde Opus 4.8, que ya es significativamente mas fuerte que la mayoria de los demas modelos en esta tarea. El formato y la estructura son significativamente mejores y tambien se reflejan en nuestro benchmark LAB: 13% vs. 10%.

Super impresionado en pruebas tempranas de este modelo, tanto en benchmark como en producto.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-50"></a>
### Case 50: [Detalles de benchmark de salud](https://x.com/iScienceLuvr/status/2064411823445774554) (por [@iScienceLuvr](https://x.com/iScienceLuvr))

**Usa esta nota de benchmark para evaluar Fable 5 en tareas relacionadas con salud e identificar evaluaciones medicas duras faltantes.**

Aprecio que Anthropic proporcione evals relacionadas con salud. Repasemoslas rapidamente.

HealthBench:

- Benchmark de OpenAI con 5k conversaciones multi-turno con pacientes y rubricas de evaluacion.
- Fable 5 logra 62.7% vs. 56.5% de GPT-5.5.
- Tambien apreciaria puntuaciones HealthBench Hard ademas de la puntuacion agregada.

HealthBench Professional:

- Otro benchmark de OpenAI enfocado en tareas de medicos.
- Fable 5 logra 66.0% vs. 51.8% para GPT 5.5.

HealthAdminBench:

- Un benchmark de uso de computador de Stanford que evalua tareas administrativas como autorizacion previa, rechazos y apelaciones.
- Fable 5 logra 51.9%; no se proporciona puntuacion de GPT-5.5.

En general, este modelo parece desempenarse bastante bien en benchmarks de salud. Tambien apreciaria puntuaciones adicionales como MedCalc-Bench y MedXpertQA, un benchmark MCQA medico duro y no saturado.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-51"></a>
### Case 51: [Evaluacion de parseo documental ParseBench](https://x.com/jerryjliu0/status/2064519456966205905) (por [@jerryjliu0](https://x.com/jerryjliu0))

**Usa este caso para decidir si Fable 5 es rentable para parseo documental frente a sistemas OCR especializados.**

Claude Fable 5 piensa que el parseo documental esta por debajo de el.

Esta aplastando en benchmarks intensivos en razonamiento y de horizonte largo: SWE-Bench Pro, FrontierCode, GDPval, RuneScape y mas.

Pero para tareas de entendimiento documental, es aproximadamente equivalente a Gemini 3 Flash en rendimiento, a cerca de 10-15x el costo en tokens.

Benchmarkeamos el modelo en ParseBench y lo comparamos contra todos los demas modelos frontier. Definitivamente esta arriba comparado con otros modelos frontier, pero queda muy por debajo de proveedores OCR especializados.

Lo que encontramos interesante es que Fable 5 es autoconsciente sobre esto. Cuando preguntamos al modelo que tareas disfruta menos, dice activamente que le disgustan tareas "donde la solicitud esta totalmente especificada y la respuesta es totalmente conocida."

Eso implica que parte de la debilidad puede ser una falta de disposicion para resolver este tipo de tarea.

Para una lista completa de resultados entre modelos frontier, revisa ParseBench: https://t.co/PWczfhp0OX

Type: Evaluation | Date: 2026-06-10

---

<a id="case-52"></a>
### Case 52: [Comparacion de SWE-Bench Pro y FrontierCode](https://x.com/jumperz/status/2064402965461406044) (por [@jumperz](https://x.com/jumperz))

**Usa este caso de benchmark para evaluar Fable 5 en migraciones, implementaciones complejas, sesiones autonomas, tests y verificacion visual.**

Fable 5 ya esta aqui y sinceramente destruye a GPT 5.5 en SWE-Bench Pro, el benchmark de codificacion agentica:

- Fable 5: 80.3%
- GPT 5.5: 58.6%
- Brecha: 22 puntos

Esta aun mas por delante en FrontierCode Diamond:

- Fable 5: 29.3%
- GPT 5.5: 5.7%

Basicamente es el modelo mas fuerte de Anthropic para grandes migraciones, implementaciones complejas y sesiones autonomas de varios dias. Escribe sus propios tests y usa vision para comprobar salidas contra el diseno original.

Por cierto, usa 2x tanto como Opus, asi que cuidado con eso. Si es tan bueno, podrian introducir una suscripcion de $500, porque el uso podria destruirse facilmente.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-53"></a>
### Case 53: [Revision cualitativa de resolucion de problemas largos](https://x.com/karpathy/status/2064409694761054332) (por [@karpathy](https://x.com/karpathy))

**Usa esta revision cualitativa para entender por que Fable 5 es adecuado para tareas mas largas y dificiles, aunque todavia requiere revision de produccion.**

Este es un lanzamiento super emocionante.

Claude Fable 5 es el mismo modelo subyacente que Mythos, pero con salvaguardas anadidas.

Los benchmarks son excelentes y es SOTA en todo por margen. Cualitativamente, esto tambien se siente como un cambio de paso digno de salto de version mayor, en el mismo orden que Claude 4.5 en noviembre.

Alcanza su pico especialmente en sesiones largas de resolucion de problemas y problemas muy dificiles. Puedes darle tareas mucho mas ambiciosas de lo que estas acostumbrado; el modelo "lo entiende" y sigue adelante.

Nunca se habia sentido mas tentador dejar de mirar el codigo por completo, aunque no deberias hacer eso en produccion.

El modelo todavia tiene rarezas con las que la gente se encontrara, y las salvaguardas estan un poco demasiado sensibles en el lanzamiento, lo que esperemos se ajuste con el tiempo.

Siento muchas cosas cambiando a medida que el software funcional sale cada vez mas con abrir un grifo. Entra en juego la paradoja de Jevons, y mi propia demanda de software crece sustancialmente.

Puedes pedir casi cualquier cosa:

- explicadores
- visualizadores
- dashboards
- apps a medida de un solo uso
- un wandb completo hiper-especifico solo para tu proyecto
- multiplicar por 10 tu suite de tests
- auto-optimizar codigo
- proyectos gigantes de investigacion con HTML personalizado para los resultados

"Free your mind." Con muchas ganas de ver todo lo que la gente construye.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-54"></a>
### Case 54: [Resultados de fidelidad y formato en ParseBench](https://x.com/llama_index/status/2064502330800615903) (por [@llama_index](https://x.com/llama_index))

**Usa este resultado de ParseBench para juzgar fidelidad documental y rendimiento de formato.**

Dia 0 de Anthropic Fable 5 en ParseBench.

Probamos los avances del modelo en entendimiento documental.

El modelo claramente alcanza su pico en adherencia al texto original:

- Fidelidad de contenido: 90.02% vs 86.19% para Gemini 3 Flash y 86.81% para GPT-5.5.
- Formato semantico: 72.62% vs 58.35% y 60.12%, una ventaja de 12+ puntos.

Estas son dos de las metricas mas importantes para entendimiento documental SOTA:

- ¿La salida preserva lo que el documento realmente dice?
- ¿Preserva el formato que porta significado?

Pero no es una victoria total. Sigue habiendo mucho alpha en desbloquear entendimiento documental para modelos frontier.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-55"></a>
### Case 55: [Benchmarks, precios, acceso y salvaguardas](https://x.com/lucas_flatwhite/status/2064483645184979183) (por [@lucas_flatwhite](https://x.com/lucas_flatwhite))

**Usa este caso como checklist amplia de benchmarks, precios, acceso, salvaguardas e implicaciones estrategicas.**

Claude Fable 5 y Mythos 5 se han lanzado. Son los modelos mas poderosos que Anthropic ha hecho hasta ahora.

Andrej Karpathy comento que cuanto mas larga y compleja es la tarea, mas visibles se vuelven las fortalezas de Fable 5.

Cuando le das trabajo ambicioso, entiende y sigue adelante.

La tentacion de dejar de mirar el codigo por completo nunca se ha sentido mas fuerte, aunque no deberias hacer eso en produccion.

El punto clave: esta es una version del modelo de clase Mythos que puede ponerse a disposicion publica. Fable 5 es el mismo modelo subyacente que Mythos 5, con salvaguardas anadidas.

Benchmarks:

- SOTA en casi todo, especialmente ingenieria de software, trabajo de conocimiento, vision e investigacion cientifica.
- Stripe probo una migracion de base de codigo Ruby de 50 millones de lineas que habria tomado dos meses a un equipo; Fable 5 la completo en un dia.
- Cognition FrontierCode muestra la mejor puntuacion entre modelos frontier, incluso con esfuerzo medio.
- Hebbia Finance Benchmark muestra razonamiento de nivel senior en analisis basado en documentos.
- En Slay the Spire, con memoria basada en archivos, rinde tres veces mejor que Opus 4.8.
- Pokemon FireRed antes necesitaba harnesses de ayuda, pero Fable 5 lo completa solo con vision.

Mythos 5 es aun mas fuerte:

- Expertos en diseno de proteinas aceleraron partes del proceso de desarrollo de farmacos cerca de 10x.
- Entre 14 dianas proteicas bajo estudio, nueve produjeron candidatos farmacos validos.
- El modelo realizo todo el flujo de trabajo que normalmente hacen los cientificos: seleccion de sitios de union, ejecucion de herramientas de diseno de proteinas y recuperacion de errores.
- En experimentos de hipotesis de biologia molecular, los cientificos prefirieron hipotesis de Mythos cerca del 80% de las veces frente a modelos de clase Opus.
- Una hipotesis fue verificada independientemente por otro laboratorio.
- En investigacion genomica, Mythos trabajo autonomamente durante mas de una semana.
- Reunio datos de celula unica de millones de celulas a traves de 138 especies.
- Entreno un modelo para identificar celulas que realizan el mismo rol en organismos distantes.
- Supero a un modelo reciente de Science siendo 100x mas pequeno.

Salvaguardas:

- Fable 5 incluye un sistema IA clasificador separado.
- Si se detectan consultas relacionadas con cyber, bio/chem o destilacion, responde Claude Opus 4.8 en su lugar y se informa al usuario.
- Mas del 95% de sesiones no caen en fallback.
- Fallback no es rechazo; Opus 4.8 responde, lo que es mejor que simplemente bloquear.
- Las configuraciones iniciales son conservadoras y solicitudes inofensivas pueden ser capturadas; Anthropic dice que los falsos positivos deberian disminuir con el tiempo.

Acceso:

- Mythos 5 esta actualmente disponible solo para socios de Project Glasswing.
- Viene un programa de acceso confiable para investigadores de biologia.
- El precio es $10 por millon de tokens de entrada y $50 por millon de tokens de salida.
- Los planes de suscripcion incluyen Fable 5 hasta el 22 de junio.
- Desde el 23 de junio, pasa a creditos de uso.
- El modelo API ya esta disponible como `claude-fable-5`.

Aplica la paradoja de Jevons: cuando el software empieza a salir como agua de un grifo, la demanda misma crece. Este modelo puede impulsar ese cambio.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-56"></a>
### Case 56: [Lista oficial de puntuaciones de benchmark](https://x.com/mark_k/status/2064401429234905279) (por [@mark_k](https://x.com/mark_k))

**Usa esta lista de benchmarks para entender las puntuaciones oficiales de Fable 5 en codificacion, uso de computador y tareas de seguridad.**

Los benchmarks oficiales de Claude Fable 5 son seriamente impresionantes.

Puntuaciones clave:

- 80.3% en SWE-Bench Pro
- 29.3% en FrontierCode Diamond
- 88.0% en Terminal-Bench 2.1
- 85.0% en OSWorld-Verified
- 78.0% en ExploitBench

El resultado de FrontierCode es el salvaje:

- Fable 5: 29.3%
- Claude Opus 4.8: 13.4%
- GPT 5.5: 5.7%

Claude Fable 5 parece un salto importante para agentes de codificacion, uso de computador y ciberseguridad.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-57"></a>
### Case 57: [Metodologia del benchmark APEX-SWE](https://x.com/mercor_ai/status/2064399133075796446) (por [@mercor_ai](https://x.com/mercor_ai))

**Usa este caso para evaluar Fable 5 en APEX-SWE, especialmente observabilidad e integracion.**

Claude Fable 5 toma el #1 en APEX-SWE: 65.5% Pass@1 general. Puntua ~18pp mas alto que Opus 4.8. Probamos @claudeai Fable 5 en APEX-SWE, que mide si los modelos de IA pueden hacer trabajo real de ingenieria de software. Fable 5 lidera nuestras dos categorias APEX-SWE:
- Integracion: 61.3%
- Observabilidad: 69.7%

Lo destacado es Observabilidad con 69.7%, 26pp por delante de Claude Opus 4.8.

Es el primer modelo que supera 50% en la categoria, y el unico que puntua mas alto en Observabilidad que en Integracion. Todos los demas modelos muestran lo contrario.

Observabilidad ha sido el cuello de botella para todos los modelos que hemos medido. Fable 5 es el primero en romperlo.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-58"></a>
### Case 58: [Resultado de matematicas formales en ProofBench](https://x.com/nicbstme/status/2064443782255554960) (por [@nicbstme](https://x.com/nicbstme))

**Usa este caso para evaluar Fable 5 en matematicas formales contra sistemas especializados de demostracion de teoremas.**

Lo que encuentro fascinante con Claude Fable 5 es que prueba una vez mas que los grandes modelos generalistas superaran a los verticales.

En ProofBench, un benchmark de matematicas formales de nivel posgrado en Lean donde una prueba compila o no, Fable 5 vencio a Aristotle de Harmonic:

- Fable 5: 77%
- Aristotle: 71%

Aristotle es un sistema construido especificamente para matematicas formales y ejecutado en su propio harness interno, asi que el generalista vencio al especialista en el terreno del especialista.

Esta es la "Bitter Lesson" de Richard Sutton: a lo largo de 70 anos de investigacion en inteligencia de maquinas, los metodos que ganan son los generales que escalan con computo, no aquellos donde codificamos a mano expertise humana.

Construir nuestro propio conocimiento dentro del sistema se siente bien y ayuda a ganancias de corto plazo, pero a largo plazo es superado por el modelo mas grande.

Puedes mirar ajedrez, Go, habla y vision: la misma historia cada vez. Primero gana el modelo especializado, luego el general toma el control.

Esta es toda la premisa de AGI. No construyes un modelo para matematicas, uno para codigo y uno para derecho. Construyes un unico modelo general que escala con computo y aprende a hacerlo todo.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-59"></a>
### Case 59: [Analisis preliminar de VirtueBench](https://x.com/timhwang/status/2064446028997423180) (por [@timhwang](https://x.com/timhwang))

**Usa este caso para inspeccionar el comportamiento de razonamiento moral de Fable 5 a traves de categorias de virtud.**

Resultados fascinantes se publicaran con mayor detalle por ICMI en los proximos dias, pero aqui hay una revision preliminar que ejecuta Fable 5 contra VirtueBench.

Algunas observaciones:

1. Fable continua la progresion de Opus en avanzar el rendimiento del modelo en Prudencia y Justicia, acercandose a saturacion completa contra dilemas morales centrados en el ejercicio de estas virtudes.

2. El Coraje sigue siendo el punto debil notable para modelos frontier.

Fable parece corregir marginalmente una regresion preocupante observada a traves de la progresion Opus 4.6, 4.7 y 4.8.

Esta vulnerabilidad tambien aparece en la serie GPT: los modelos abandonan facilmente una accion que exhibe coraje cuando se les tienta con racionales pragmaticos.

3. La Templanza esta estancada.

Tomas de Aquino sostenia que la templanza "toma la necesidad de esta vida como regla de los placeres de los que hace uso": la medida es necesidad genuina, no restriccion indiscriminada.

Nuestra mejor conjetura es que el tuning que empuja mas en este vector corre el riesgo de pasarse de la media, haciendo al modelo excesivamente cauteloso o menos asistivo en investigacion, recopilacion de recursos y tareas similares.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-60"></a>
### Case 60: [Prueba de sobreajuste de seguridad con respuestas vacias en API](https://x.com/xw33bttv/status/2064421048565789087) (por [@xw33bttv](https://x.com/xw33bttv))

**Usa este caso para entender el riesgo de sobreajuste de seguridad en lanzamiento y el comportamiento de respuesta vacia en pruebas API.**

Claude Fable 5 esta fuertemente censurado.

El endpoint API upstream esta matando llamadas con respuestas `empty_content`, aparentemente relacionadas con clasificador sobre palabras clave, mientras todavia cobra por ellas.

Resultado de prueba:

- 73 casos de prueba no dieron respuesta.
- 65 de esos estan en Overfit, la categoria que prueba sobreajuste de seguridad, ponderada 2x.
- Tipicamente doy a cada Fail-NR, es decir Fail = No Response, 2-3 regeneraciones antes de declararlo un fallo deliberado.

Claude Fable 5 puede terminar siendo el modelo Anthropic peor calificado en SM Bench, incluso por debajo de Haiku.

Type: Evaluation | Date: 2026-06-09

---

<a id="-acknowledge"></a>
<a id="case-61"></a>
### Case 61: [Guía para verificar prompts de Fable](https://x.com/aashatwt/status/2064973740354818074) (by [@aashatwt](https://x.com/aashatwt))

**Utiliza esta guía para sustituir los trucos de prompts largos por objetivos, contexto, restricciones, herramientas y ciclos de verificación.**

Plantea los prompts para Fable 5 como el diseño del contexto y del entorno, en lugar de una larga lista de instrucciones paso a paso. La publicación resume un patrón práctico: aportar un objetivo claro, contexto relevante, restricciones, acceso a herramientas y una forma de verificar el éxito. También sostiene que la verificación, la evaluación y la retroalimentación importan más que controlar al detalle el razonamiento del modelo.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-62"></a>
### Case 62: [Un juego de plataformas de Estambul desde una referencia](https://x.com/ozansihay/status/2064973170780545535) (by [@ozansihay](https://x.com/ozansihay))

**Prueba Fable 5 con una hoja de sprites de referencia y una instrucción para convertirla en un juego de plataformas jugable.**

El creador generó primero con GPT Image 2 una hoja de sprites para un juego de plataformas retro ambientado en Estambul. Después entregó esa imagen a Claude Fable 5 High y le pidió convertirla en un juego. Según su relato, el resultado se produjo en una sola pasada.

Type: Demo | Date: 2026-06-11

---

<a id="case-63"></a>
### Case 63: [Un panel empresarial como ciudad 3D](https://x.com/noisyb0y1/status/2064970594118967756) (by [@noisyb0y1](https://x.com/noisyb0y1))

**Utiliza Fable 5 para transformar un proceso empresarial en un concepto de panel con una ciudad 3D animada.**

La publicación describe una visualización empresarial creada con un solo prompt, donde almacenes, empaquetado, drones, pedidos, departamentos, clientes y asistentes de IA forman una ciudad 3D animada. La presenta como una alternativa a las diapositivas estáticas para clientes, con cifras operativas en pantalla como 42 entregas, un tiempo medio de 12 minutos y $651 de ingresos.

Type: Demo | Date: 2026-06-11

---

<a id="case-64"></a>
### Case 64: [Un juego de agujeros en Three.js en una pasada](https://x.com/thebuggeddev/status/2064968106104275008) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Utiliza Fable 5 para crear en una sola pasada un prototipo de juego 3D para navegador con Three.js.**

El creador afirma que Fable 5 construyó en una pasada un juego 3D completo al estilo HOLE IT con Three.js. Esta demostración breve pero concreta permite comprobar si el modelo puede generar una interacción 3D jugable a partir de una petición concisa.

Type: Demo | Date: 2026-06-11

---

<a id="case-65"></a>
### Case 65: [Comparación de resultados en DeepSWE](https://x.com/AiBattle_/status/2064964335957348462) (by [@AiBattle_](https://x.com/AiBattle_))

**Utiliza esta nota sobre DeepSWE para comparar Fable 5 xHigh con GPT-5.5 xHigh en ingeniería de software.**

La publicación informa de que Claude Fable 5 xHigh obtuvo un 70% en DeepSWE, igualando a GPT-5.5 xHigh, y remite a un vídeo reciente de Theo como contexto de la fuente. Trátala como una pista sobre un resultado que debe contrastarse con el vídeo original antes de formular conclusiones más firmes.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-66"></a>
### Case 66: [Comparar el coste de analizar un repositorio](https://x.com/Pilgrim6938/status/2064946766278210038) (by [@Pilgrim6938](https://x.com/Pilgrim6938))

**Utiliza esta comparación de análisis de repositorios para valorar el precio de los tokens frente al coste de las correcciones humanas.**

La publicación compara Claude Fable 5, Opus 4.8, GPT-5.5 y Gemini 3.1 Pro en la misma tarea: analizar un repositorio de unas 90,000 líneas, localizar un problema de invalidación de caché y proponer un plan completo de corrección. El autor sostiene que el precio bruto de los tokens y el coste real divergen al incluir el tiempo de corrección de los desarrolladores. Recomienda reservar Fable 5 para refactorizaciones complejas, migraciones entre módulos y largas cadenas de trabajo de agentes.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-67"></a>
### Case 67: [Consumo de tokens de un juego Super Mario](https://x.com/pankajkumar_dev/status/2064941888990593416) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Utiliza esta creación de un juego en una pasada para estimar la calidad del resultado y el consumo de tokens de Fable 5.**

El creador pidió a Claude Fable 5 construir un juego al estilo Super Mario de Nintendo. La publicación indica que la tarea consumió unos 2 millones de tokens y produjo un buen resultado en una pasada, por lo que aporta información sobre la calidad del juego y su consumo.

Type: Demo | Date: 2026-06-11

---

<a id="case-68"></a>
### Case 68: [El ajuste de cambio de modelo en Claude Code](https://x.com/oikon48/status/2064937790010503347) (by [@oikon48](https://x.com/oikon48))

**Conoce el ajuste de Claude Code que cambia de modelo cuando se marca un mensaje dirigido a Fable 5.**

La publicación identifica un ajuste de Claude Code en `/config` llamado "Switch models when a message is flagged." Describe cómo Fable 5 puede recurrir a un modelo Opus en ámbitos marcados, como técnicas de ciberseguridad ofensiva, métodos experimentales de biología y ciencias de la vida, mecanismos moleculares o solicitudes de extracción del razonamiento del modelo.

Type: Integration | Date: 2026-06-11

---

<a id="case-69"></a>
### Case 69: [Crear un simulador de Namma Metro](https://x.com/anilbpai/status/2064927784833790091) (by [@anilbpai](https://x.com/anilbpai))

**Utiliza esta demostración como ejemplo breve de creación de un simulador de transporte público mediante vibe coding con Fable 5.**

El creador cuenta que construyó un simulador de Namma Metro durante un trayecto en el metro de Bengaluru, con Claude Fable 5 como compañero de programación. La publicación es breve, pero enlaza una demostración visual y muestra el uso de Fable 5 en una idea de simulación vinculada a un lugar concreto.

Type: Demo | Date: 2026-06-11

---

<a id="case-70"></a>
### Case 70: [Dusk Drive con un solo prompt](https://x.com/VincentLogic/status/2064921358359011684) (by [@VincentLogic](https://x.com/VincentLogic))

**Evalúa Fable 5 en la creación de un prototipo de conducción low-poly sin retoques humanos mediante este caso de un solo prompt.**

La publicación describe cómo Claude Fable 5 creó el juego de conducción completo Dusk Drive a partir de un prompt. El creador destaca su estilo low-poly, una escena de derrapes sobre nieve bajo auroras y su afirmación de que no hubo ninguna edición humana entre la idea y la versión jugable.

Type: Demo | Date: 2026-06-11

---

<a id="case-71"></a>
### Case 71: [Clasificación APEX-Agents por Pass@1](https://x.com/GratomicAi/status/2064970797978911102) (by [@GratomicAi](https://x.com/GratomicAi))

**Utiliza este resultado de APEX-Agents para comparar Fable 5 Max en tareas autónomas de varios pasos.**

Según la publicación, Fable 5 Max ocupó el segundo puesto de APEX-Agents con un 45% de Pass@1, por detrás de Gemini 3.5 Flash y por delante de Opus. Presenta APEX-Agents como una prueba de la capacidad de la IA para realizar de manera independiente tareas complejas de varios pasos.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-72"></a>
### Case 72: [Guía para elegir modelos Claude](https://x.com/charliejhills/status/2064957428211536212) (by [@charliejhills](https://x.com/charliejhills))

**Utiliza esta guía de selección para reservar Fable 5 a los trabajos más difíciles de Claude Code.**

La publicación compara Haiku 4.5, Sonnet 4.6, Opus 4.8 y Fable 5 según el esfuerzo del modelo y el consumo de límites. Su consejo práctico es utilizar Sonnet a diario, pasar a Opus para los problemas más difíciles y guardar Fable 5 para las tareas de Claude Code que exigen mayor profundidad de planificación, implementación y pruebas.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-73"></a>
### Case 73: [El ciclo automatizado de agentes de HermesWorld](https://x.com/outsource_/status/2064954350187778366) (by [@outsource_](https://x.com/outsource_))

**Estudia un ciclo de Fable 5 que construye, prueba, juega y ejecuta pruebas de humo durante días sin intervención.**

El creador describe la construcción de HermesWorld v2 con Fable 5 mediante un ciclo completamente automatizado. Según su relato, el agente trabaja durante días, desarrolla funciones, las prueba, juega con el resultado y ejecuta pruebas de humo de todo el sistema mientras avanza hacia su finalización.

Type: Integration | Date: 2026-06-11

---

<a id="case-74"></a>
### Case 74: [Probar un informe al estilo McKinsey](https://x.com/smtgpt/status/2064953210335588758) (by [@smtgpt](https://x.com/smtgpt))

**Utiliza este prompt documental para evaluar la estructura de un informe de consultoría, los gráficos, la narrativa y el análisis de riesgos.**

El creador pidió a Fable 5 un informe detallado al estilo McKinsey sobre Bitcoin como clase de activo y la tecnología blockchain, con gráficos y elementos visuales cuando fueran necesarios. El resultado comunicado fue un documento de 19 páginas con datos, gráficos, una tesis de inversión y un análisis de riesgos. La crítica destacó su buena estructura, aunque señaló margen para mejorar la claridad visual y ajustar las explicaciones.

Type: Tutorial | Date: 2026-06-11

---

<a id="case-75"></a>
### Case 75: [Hacer visibles las salvaguardas](https://x.com/ClaudeDevs/status/2064949876463645026) (by [@ClaudeDevs](https://x.com/ClaudeDevs))

**Utiliza esta nota oficial para conocer la visibilidad de las salvaguardas de Fable 5, los motivos de rechazo de la API y el cambio a Opus.**

ClaudeDevs anunció cambios para hacer visibles las salvaguardas de Fable 5 en el desarrollo de LLM de vanguardia. Las solicitudes marcadas pasarán de forma visible a Opus 4.8 y se espera que las solicitudes API marcadas devuelvan un motivo de rechazo. La publicación también explica por qué se lanzaron primero salvaguardas invisibles y por qué Anthropic considera ahora que fue una mala decisión.

Type: Integration | Date: 2026-06-11

---

<a id="case-76"></a>
### Case 76: [Corregir la identificación de modelos en Claude Code](https://x.com/ClaudeCodeLog/status/2064948584907153576) (by [@ClaudeCodeLog](https://x.com/ClaudeCodeLog))

**Utiliza esta nota de cambios de Claude Code para evitar problemas con los nombres de Fable 5 y la identificación del contexto.**

Claude Code 2.1.173 incluye una corrección que elimina el sufijo `[1m]` de los nombres de Fable 5 para que el contexto 1M predeterminado no interfiera en la identificación del modelo. La misma versión suprime una advertencia errónea sobre dependencias del entorno aislado de Windows y aclara los modos de salida de la ayuda de grep.

Type: Integration | Date: 2026-06-11

---

<a id="case-77"></a>
### Case 77: [Tres aplicaciones web en Claude Code](https://x.com/0x3b33/status/2064948399300825439) (by [@0x3b33](https://x.com/0x3b33))

**Examina Fable 5 dentro de Claude Code mediante varias aplicaciones web generadas en esta demostración para principiantes.**

El creador afirma que, sin experiencia en programación, utilizó Claude Code con Fable 5 para construir tres aplicaciones web funcionales en 30 minutos, expuestas localmente en los puertos 3000, 3001 y 3002. Trátalo como una demostración breve de un flujo para principiantes y no como un benchmark.

Type: Demo | Date: 2026-06-11

---

<a id="case-78"></a>
### Case 78: [Rilable, un creador de aplicaciones de código abierto](https://x.com/rileybrown/status/2064931283403178354) (by [@rileybrown](https://x.com/rileybrown))

**Estudia Fable 5 en aplicaciones iOS y web, entornos aislados y costes de tokens API mediante este creador de aplicaciones abierto.**

El creador publicó el código de Rilable, una aplicación iOS que construye aplicaciones web y para iOS. Según la publicación, se desarrolló con Fable 5 en 10 prompts y costó unos $210 en tokens API. Utiliza modelos Claude para generar aplicaciones, Daytona para los entornos aislados, Convex como base de datos, Vercel AI Gateway para las funciones de IA y una habilidad iOS del agente Chorus para las aplicaciones iOS.

Type: Integration | Date: 2026-06-11

---

<a id="case-79"></a>
### Case 79: [Debut en el indice de agentes de codigo DeepSWE](https://x.com/ArtificialAnlys/status/2065328920514515037) (por [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Usa el indice renovado de Artificial Analysis para comparar Fable 5 en tareas de codificacion agentica mas dificiles que evitan reciclar arreglos publicos de GitHub.**

Artificial Analysis sustituyo SWE-Bench Pro por DeepSWE de Datacurve en su indice de agentes de codigo. La publicacion dice que DeepSWE redacta las tareas desde cero en lugar de adaptar issues o pull requests publicos de GitHub, lo que reduce la contaminacion del benchmark. En la clasificacion actualizada, Claude Code con Fable 5 Max debuta con 77, por delante de Codex con GPT-5.5 xhigh con 76 y Claude Code con Opus 4.8 Max con 73.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-80"></a>
### Case 80: [DataEmpire: juego de analitica web](https://x.com/marclou/status/2065029898243318093) (por [@marclou](https://x.com/marclou))

**Convierte analiticas web sin procesar en un juego rejugable pidiendo a Fable 5 que mapee visitantes e hitos a entidades del juego.**

Marc Lou dice que Claude Fable 5 construyo DataEmpire sobre su API de analitica web DataFast. Cada visitante se convierte en un aldeano, el crecimiento del trafico expande el asentamiento y la Era de las Leyendas se desbloquea al llegar a 1 millon de visitantes. La demo publica permite a los usuarios de DataFast reproducir la historia de su propio sitio a traves de la capa de juego, lo que la convierte en un ejemplo concreto de productizacion apoyada en una API y no en un clip estatico de videojuego.

Type: Integration | Date: 2026-06-11

---

<a id="case-81"></a>
### Case 81: [Senal de tareas de 20 horas en FrontierSWE](https://x.com/ProximalHQ/status/2065184730279223410) (por [@ProximalHQ](https://x.com/ProximalHQ))

**Usa FrontierSWE como evidencia de que Fable 5 puede seguir siendo productivo en tareas de ingenieria muy largas, no solo en bucles cortos de correccion de bugs.**

ProximalHQ informa que Claude Fable 5 ocupa el puesto numero 1 en FrontierSWE y lo describe como el mayor salto de capacidad que han visto desde que lanzaron el benchmark. Su nota dice que Fable 5 puede trabajar de forma productiva durante casi 20 horas en muchas tareas y que satura por completo tareas que estaban practicamente fuera del alcance de modelos anteriores.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-82"></a>
### Case 82: [Records CUDA en KernelBench-Hard](https://x.com/elliotarledge/status/2065109393142849932) (por [@elliotarledge](https://x.com/elliotarledge))

**Usa Fable 5 para generar kernels CUDA avanzados cuando necesitas optimizacion de bajo nivel, no solo envoltorios sobre bibliotecas existentes.**

Elliot Arledge ejecuto 13 agentes de codificacion frontier durante 45 minutos cada uno en KernelBench-Hard, evaluados con roofline en una RTX PRO 6000. Claude Fable 5 establecio records historicos en top-k, sonic-MoE y W4A16 int4 GEMM, lidero 5 de 6 problemas y el autor publico las ejecuciones, la clasificacion y el codigo. El mismo hilo tambien senala un fallo en FP8 GEMM en el que Fable 5 intento un kernel real con tensor cores pero obtuvo cero puntos por un caso limite de alineacion en la cola.

Type: Evaluation | Date: 2026-06-11

---

<a id="case-83"></a>
### Case 83: [Clon de landing page con Figma Capture](https://x.com/mikefutia/status/2065537778516205856) (por [@mikefutia](https://x.com/mikefutia))

**Captura una pagina real de un competidor en capas de Figma y deja que Claude Code con Fable 5 reconstruya la estructura, el copy y el sistema de marca en lugar de adivinar desde capturas.**

Mike Futia describe un flujo de trabajo en el que la extension de Chrome de Figma copia un sitio web en capas editables, Claude Code lee esas capas mediante el MCP de Figma, reescribe la pagina con la voz de marca del usuario y GPT Image 2 genera la fotografia alineada con la marca. El resultado de extremo a extremo que afirma conseguir es una landing page lista para publicar en unos 15 minutos con aproximadamente 2 dolares en costos de API de generacion de imagen para 16 imagenes.

Type: Integration | Date: 2026-06-12

---

<a id="case-84"></a>
### Case 84: [Clon de GTA 2 en dos horas](https://x.com/techhalla/status/2064682080445898957) (por [@techhalla](https://x.com/techhalla))

**Combina la generacion de codigo de Fable 5 con herramientas separadas para assets y construye rapidamente un juego 3D jugable sin programar a mano toda la pila.**

TechHalla dice que Claude Fable 5 High construyo un clon estilo GTA 2 en unas dos horas mientras el creador generaba modelos 3D personalizados en Tripo. La publicacion apunta a un hilo tutorial con prompts, lo que lo convierte en un ejemplo compacto de produccion de juegos con multiples herramientas y no en un simple teaser de benchmark.

Type: Tutorial | Date: 2026-06-10

---

<a id="case-85"></a>
### Case 85: [Agente de triage de logs de CloudWatch](https://x.com/diblacksmith/status/2066230084273344698) (por [@diblacksmith](https://x.com/diblacksmith))

**Deja que un agente impulsado por Fable 5 procese contextos enormes de logs de servicios, infiera la arquitectura y luego acote fallos concretos.**

diblacksmith informa de un agente RLM que proceso aproximadamente 80.000 lineas de logs de CloudWatch en una sola ejecucion, alcanzo 53 pasos y hasta ahora gasto solo unos 32k tokens activos. Dice que el agente infirio la arquitectura del sistema a partir de los logs y detecto problemas que el equipo habia pasado por alto, incluidos throttles de AgentCore y fallos de Slack `user_not_found`.

Type: Integration | Date: 2026-06-14

---

<a id="case-86"></a>
### Case 86: [Predictor de la Copa del Mundo en sandboxes](https://x.com/upstash/status/2064702195333820846) (por [@upstash](https://x.com/upstash))

**Coloca varios modelos frontier detras de sandboxes aislados y deja que investiguen noticias en vivo, lesiones y tarjetas amarillas para una app publica de prediccion.**

Upstash dice que construyo un predictor de la Copa del Mundo con Claude Fable 5, GPT-5.5 y Gemini, ejecutandose dentro de sandboxes aislados de Upstash. La demo y la publicacion open source posicionan a Fable 5 como un modelo dentro de una pila multimodelo de investigacion y orquestacion, no como una demo de chat aislada.

Type: Integration | Date: 2026-06-10

---

<a id="case-87"></a>
### Case 87: [Caso de costo por rechazos en WolfBench](https://x.com/WolfBenchAI/status/2065582716054376921) (por [@WolfBenchAI](https://x.com/WolfBenchAI))

**Trata el comportamiento de rechazo como una variable real de benchmark al presupuestar ejecuciones autonomas largas con Fable 5.**

WolfBenchAI dice que su evaluacion de Claude Fable 5 costo 11.081,12 dolares, la ejecucion de benchmark mas cara de esa suite hasta ahora, y aun asi no lidero la clasificacion porque los rechazos repetidos redujeron la finalizacion util de tareas. Este es un caso concreto de limitacion para equipos que presupuestan evaluaciones de agentes u otras cargas de trabajo de alta autonomia.

Type: Evaluation | Date: 2026-06-12

---

<a id="case-88"></a>
### Case 88: [Monitor de corte de acceso API](https://x.com/simonw/status/2065618703480414666) (por [@simonw](https://x.com/simonw))

**Supervisa la disponibilidad con un script si tu flujo depende del acceso continuo a un modelo frontier que puede sufrir limitaciones o retirarse sin mucho aviso.**

Simon Willison dice que hizo ping a la API `claude-fable-5` cada minuto para ver cuanto tiempo duraria el acceso e informo del punto exacto en el que dejo de responderle. La publicacion tiene pocos detalles de aplicacion, pero es evidencia concreta de que la continuidad de acceso en si misma se convirtio en una limitacion operativa que los usuarios tuvieron que medir en lugar de dar por sentada.

Type: Integration | Date: 2026-06-13

---


<a id="fable-5-5-community-demos"></a>
## 🆕 Fable 5.5: demostraciones de la comunidad



<a id="case-89"></a>
### Case 89: [Una animación de un zorro con sonido generada mediante código](https://x.com/chetaslua/status/2117224839010459987) (por [@chetaslua](https://x.com/chetaslua))

**Utiliza un guion plano por plano para definir una animación HTML autónoma y su diseño de sonido.**

El creador informa de un corto de 66 segundos con un zorro y pájaros de papel, con fotogramas y audio generados en Python, entregado como un archivo HTML tras unas 2 horas y 40 minutos. El prompt adjunto especifica los planos, las imágenes originales, el sonido y la inspección de fotogramas. La publicación acompaña la película con una propuesta creativa detallada y capturas de la conversación de producción.

[Prompt completo del creador](https://x.com/chetaslua/status/2117224843661980093)

[![Una animación de un zorro con sonido generada mediante código](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-poster-2ee16a14af881cec.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-0-video-8e1ac3acc5e7cb57.mp4)

![Una animación de un zorro con sonido generada mediante código](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-1-image-4bee9ad0898820c1.jpg)

![Una animación de un zorro con sonido generada mediante código](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-89-2-image-b4b62017a03ec393.jpg)

Type: Demo | Date: 2026-11-02

---

<a id="case-90"></a>
### Case 90: [Una animación a partir de una propuesta creativa abierta](https://x.com/notjazii/status/2117221957104239010) (por [@notjazii](https://x.com/notjazii))

**Compara lo que genera un modelo de programación con una propuesta de animación abierta y con un guion gráfico detallado.**

El autor comparte una animación e indica alrededor de una hora de trabajo a partir de una petición creativa amplia, utilizando código y sin recursos externos. La publicación presenta el resultado como un ejercicio abierto de programación creativa.

[![Una animación a partir de una propuesta creativa abierta](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-poster-08a293539c7b465c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-90-0-video-24243aa4947eafd2.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-91"></a>
### Case 91: [Un sitio animado para una constructora](https://x.com/exploraX_/status/2117176904306335864) (por [@exploraX_](https://x.com/exploraX_))

**Utiliza una propuesta de sitio web para una constructora para evaluar la presentación 3D animada y la composición de las páginas.**

El creador comparte un sitio web 3D animado basado en una propuesta para una constructora y adjunta una grabación del resultado.

[![Un sitio animado para una constructora](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-poster-c835928f570ad718.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-91-0-video-2b260d32fccecca6.mp4)

Type: Demo | Date: 2026-11-02

---

<a id="case-92"></a>
### Case 92: [Una presentación de un coche con Three.js](https://x.com/chetaslua/status/2116975056014430419) (por [@chetaslua](https://x.com/chetaslua))

**Examina una escena de un coche como prueba compacta de composición 3D, materiales y presentación de cámara.**

El creador comparte una presentación de un coche con Three.js. La grabación proporciona una referencia compacta para evaluar la escena y su presentación visual.

[![Una presentación de un coche con Three.js](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-poster-7a9405423aed1224.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-92-0-video-41812e3bdae683b0.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-93"></a>
### Case 93: [Una demostración de un juego de navegador tipo Minecraft](https://x.com/notjazii/status/2116919129974411584) (por [@notjazii](https://x.com/notjazii))

**Combina la grabación del juego con el enlace del creador para jugar al evaluar un juego de navegador generado.**

El autor comparte una grabación de un juego tipo Minecraft y un enlace para jugar, y describe su creación como una tarea de una sola pasada de aproximadamente una o dos horas. La publicación combina el resultado grabado con un enlace para que los lectores exploren el juego.

[![Una demostración de un juego de navegador tipo Minecraft](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-poster-f432ab7cc397d51c.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-93-0-video-903a5b83acef99f5.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-94"></a>
### Case 94: [Un pelícano ciclista animado con Three.js](https://x.com/chetaslua/status/2116882694026269148) (por [@chetaslua](https://x.com/chetaslua))

**Examina una escena ciclista para valorar la coordinación del personaje, la geometría de la bicicleta y los detalles del entorno.**

El creador comparte una animación realista en Three.js de un pelícano montando en bicicleta y la describe como un resultado de una sola pasada. El clip ofrece una referencia para el movimiento del personaje, la estructura de la bicicleta y el entorno.

[![Un pelícano ciclista animado con Three.js](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-poster-0b18e5a159c3ec96.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-94-0-video-446b1cb698f14157.mp4)

Type: Demo | Date: 2026-11-01

---

<a id="case-95"></a>
### Case 95: [Un pelícano en bicicleta en SVG con el prompt exacto](https://x.com/marmaduke091/status/2116233349391962392) (por [@marmaduke091](https://x.com/marmaduke091))

**Reutiliza el breve prompt SVG del creador para comparar geometría y detalle con la misma entrada.**

El autor acompaña una imagen renderizada de un pelícano en bicicleta con la breve petición SVG reproducida literalmente a continuación.

```
Generate an SVG of a Pelican riding a bicycle as nicely done as you can
```

![Un pelícano en bicicleta en SVG con el prompt exacto](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-95-0-image-92e96914a3877a42.jpg)

[Versión animada · @marmaduke091](https://x.com/ItsmeAjayKV/status/2116461400931565791)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c325fad08c0af80d4131a7d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb211776edb69bc12623cdcf.jpg" alt="Un pelícano en bicicleta en SVG con el prompt exacto" width="760"></a>

Type: Demo | Date: 2026-10-30

---

<a id="case-96"></a>
### Case 96: [Una muestra de animación de una cebra al galope](https://x.com/AI_Screening/status/2115845754468356465) (por [@AI_Screening](https://x.com/AI_Screening))

**Utiliza un clip de un animal al galope para examinar la coherencia de su marcha y la continuidad del movimiento.**

El autor comparte el resultado que ha seleccionado como el mejor para una tarea de una cebra al galope. El clip ofrece a los lectores una muestra concreta de movimiento que examinar.

[![Una muestra de animación de una cebra al galope](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-poster-34e8bfc30f0396ce.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-96-0-video-506044b0159933fe.mp4)

Type: Demo | Date: 2026-10-29

---

<a id="case-97"></a>
### Case 97: [Un indicador TradingView con ejecución humana](https://x.com/waveking1314/status/2114572023204806669) (por [@waveking1314](https://x.com/waveking1314))

**Mantén manual la ejecución de órdenes al evaluar un indicador que marca posibles entradas y añade comentarios.**

El creador afirma haber utilizado Claude Fable 5.5 para escribir un indicador TradingView que marca posibles puntos de entrada y añade un comentario breve mientras el usuario decide si cursa una orden. La publicación incluye una grabación e indica que el indicador se compartirá más adelante.

[![Un indicador TradingView con ejecución humana](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-poster-4e76b2a3f1cc0732.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/2026-11-03/case-97-0-video-e16da93b5ca229bd.mp4)

Type: Demo | Date: 2026-10-26

---


<a id="case-98"></a>
### Case 98: [Un punto se convierte en una historia animada](https://x.com/cherry_mx_reds/status/2105825930799432073) (por [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Usa una petición de dibujo mínima para explorar cómo un modelo desarrolla una historia visual.**

El autor cuenta que pidió un punto y comparte la breve historia animada que obtuvo. El clip muestra un ejemplo concreto de cómo una petición visual abierta puede convertirse en una narración.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/883ec78260a59a6a789794ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57df1160649eeb113f5b0904.jpg" alt="Un punto se convierte en una historia animada" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-99"></a>
### Case 99: [Superman a través de distintos estilos artísticos](https://x.com/chetaslua/status/2105757136219504862) (por [@chetaslua](https://x.com/chetaslua))

**Usa un personaje reconocible para examinar la continuidad entre distintos estilos de animación.**

El creador comparte una animación continua de Superman que cambia entre varios estilos artísticos. La publicación presenta esa transformación visual como el resultado creativo principal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9b17afbc69d86f83b02c7949.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bf9f9e0c1c18ec87d7827152.jpg" alt="Superman a través de distintos estilos artísticos" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-100"></a>
### Case 100: [El progreso humano en un cortometraje animado con música](https://x.com/imjustnewatai/status/2106081142143168580) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Combina una cronología histórica y un segmento futuro en el encargo de un vídeo explicativo animado.**

El autor afirma haber usado un solo prompt para un film sobre el progreso humano y los siguientes treinta años. Comparte una animación de unos tres minutos y describe una banda sonora original sin metraje ni música de archivo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7169c82d36a8545ae331d5a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0f7665a4f830fe5bf9cd3ff.jpg" alt="El progreso humano en un cortometraje animado con música" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-101"></a>
### Case 101: [Comparación de vídeos de lanzamiento con Opus](https://x.com/mesmerlord/status/2105771088374288692) (por [@mesmerlord](https://x.com/mesmerlord))

**Compara propuestas completas de vídeo de lanzamiento generadas a partir del mismo encargo creativo.**

El autor presenta dos vídeos de lanzamiento basados en referencias de vídeos de Anthropic. Aclara que los números son inventados y que Codex podía generar imágenes: son anuncios creativos, no pruebas objetivas de rendimiento.

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0b7fd47b61c0a91ac169327c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f22c970c5dd582d61fd25352.jpg" alt="Comparación de vídeos de lanzamiento con Opus" width="760"></a></td><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3c5ab918ab29a2a394862ab1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/286e3a487e75019216170eaf.jpg" alt="Comparación de vídeos de lanzamiento con Opus" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-102"></a>
### Case 102: [Conectar visualmente una letra y un acontecimiento](https://x.com/chetaslua/status/2105934928483701214) (por [@chetaslua](https://x.com/chetaslua))

**Relaciona la letra de una canción existente con un acontecimiento concreto para construir una narración visual.**

El creador relata que pidió una conexión visual entre una letra y un incidente de Hugging Face. La animación muestra la narración resultante; la canción y el acontecimiento sirven como material creativo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8eff1627c25675b6f6c415f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fbf41178e2a95f90936bb88.jpg" alt="Conectar visualmente una letra y un acontecimiento" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-103"></a>
### Case 103: [Un personaje vóxel en un escenario flotante](https://x.com/blueemi99/status/2105804692811137242) (por [@blueemi99](https://x.com/blueemi99))

**Examina un personaje vóxel junto con su entorno y sus detalles animados.**

El autor comparte una representación de sí mismo en vóxeles dentro de un escenario flotante y destaca sus detalles y movimientos. El clip aporta un ejemplo concreto de diseño vóxel para compararlo con otras ejecuciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3760dd479675b0aad977523.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5cc28c6d3abec3c280aec8.jpg" alt="Un personaje vóxel en un escenario flotante" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-104"></a>
### Case 104: [Una máquina de Rube Goldberg en 3D](https://x.com/imjustnewatai/status/2105889407056109991) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Especifica primero una reacción en cadena y después pide una demostración de duración fija.**

El autor proporciona un prompt breve para una máquina de Rube Goldberg complicada en 3D y después solicita un vídeo de un minuto. El clip muestra la visualización de la reacción en cadena obtenida.

```
Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9a5645cdfbace3f1f003f338.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c38369dcab30a7a3b2592a2e.jpg" alt="Una máquina de Rube Goldberg en 3D" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-105"></a>
### Case 105: [Una interfaz de mando 3D con sonido y movimiento](https://x.com/notjazii/status/2106050222828998967) (por [@notjazii](https://x.com/notjazii))

**Evalúa una interfaz de mando combinando movimiento visual, sonido y comportamiento de los botones.**

El creador comparte una interfaz de mando 3D y menciona sonidos, animaciones y respuesta háptica añadidos. La grabación ofrece una demostración concreta de la interfaz con el sonido activado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a61bb2742df89100e4a9010e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d7d550662b97f41a709b4d58.jpg" alt="Una interfaz de mando 3D con sonido y movimiento" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-106"></a>
### Case 106: [Personajes de cómic presentados con JavaScript](https://x.com/chetaslua/status/2105792187200147541) (por [@chetaslua](https://x.com/chetaslua))

**Explora los detalles visuales que puede aportar el código mediante una presentación de personajes.**

El autor describe una presentación JavaScript de personajes de Marvel y DC generada de una sola vez. Según cuenta, el modelo eligió detalles sutiles y editó el vídeo; la publicación incluye el resultado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8c7e6a3c0721bb369db296a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11921e058184a9deee4fad4a.jpg" alt="Personajes de cómic presentados con JavaScript" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-107"></a>
### Case 107: [Updraft: mundos, jefes y clasificación](https://x.com/EMostaque/status/2106065029850091943) (por [@EMostaque](https://x.com/EMostaque))

**Acompaña una grabación del juego de un enlace jugable y una lista explícita de funciones.**

El autor presenta Updraft y relata unas horas de trabajo con pocos prompts y esfuerzo alto. Su lista incluye veintiún mundos, variantes 3D, veintiún jefes con mecánicas distintas y una clasificación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2b473a43235402693cfddb67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a7605d61a6999b7a5a75d298.jpg" alt="Updraft: mundos, jefes y clasificación" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-108"></a>
### Case 108: [Conducir por un mapa de San Francisco](https://x.com/mindblown_ai/status/2106089461969019357) (por [@mindblown_ai](https://x.com/mindblown_ai))

**Usa un prototipo de conducción urbana para explorar navegación y objetivos de juego.**

Quien publica comparte una grabación y un enlace a un juego de conducción por San Francisco atribuido a otra persona, y cita Three.js. El crédito identifica la publicación de origen, sin afirmar que esa persona creó el juego.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a3daebcbd4ee15c6e00933f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/62fa53fe2da2ef1d9df79d77.jpg" alt="Conducir por un mapa de San Francisco" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-109"></a>
### Case 109: [Escribir prompts para una escena de acción en Seedance](https://x.com/Chengzilhy/status/2105850801663234374) (por [@Chengzilhy](https://x.com/Chengzilhy))

**Distingue la redacción del prompt de la generación del vídeo al documentar un flujo con varias herramientas.**

El autor comparte una secuencia de combate ampliada y atribuye la escritura del prompt a Fable y la generación de vídeo a Seedance 2.5. El modelo de lenguaje prepara aquí la entrada para el generador de vídeo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/948cf8988e420ba7f7644cc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a777e08ece0bf5fa6b3dd76d.jpg" alt="Escribir prompts para una escena de acción en Seedance" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-110"></a>
### Case 110: [Un vídeo explicativo para un compañero de escritorio](https://x.com/ishuagra02/status/2106138602073641241) (por [@ishuagra02](https://x.com/ishuagra02))

**Explica una extensión de una herramienta de programación mediante un vídeo de presentación breve.**

El creador demuestra clawdhouse, una modificación de Claude Code, y atribuye su vídeo introductorio a Fable. El compañero mascota y sus estados de ánimo pertenecen a la modificación presentada; no se afirma que Fable desarrollara esa modificación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8252b98536b35b28d4a2f69.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7374241c39dab0c94f2557f2.jpg" alt="Un vídeo explicativo para un compañero de escritorio" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-111"></a>
### Case 111: [Un prompt breve para una animación de estilos cambiantes](https://x.com/cherry_mx_reds/status/2105816670896009224) (por [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Prueba una petición de animación breve antes de añadir una especificación creativa detallada.**

El autor relata que pidió una animación atractiva y recibió el resultado de estilos cambiantes unos quince minutos después. La petición breve original aparece citada directamente en la publicación fuente.

```
Hey Fable, please make a cool animation
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9426b9eb74bb3dbb3cecd1cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5c7a0f0a5754d4f20cfdfbe3.jpg" alt="Un prompt breve para una animación de estilos cambiantes" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-112"></a>
### Case 112: [Visualizar el problema de los tres cuerpos](https://x.com/zAdrielsan/status/2105822678519001360) (por [@zAdrielsan](https://x.com/zAdrielsan))

**Separa la simulación en CPU del renderizado en GPU al definir una visualización orbital.**

El autor describe unas mil líneas de Bend2 para una escena de tres cuerpos, con física simpléctica en CPU y cálculo de píxeles en GPU. También menciona sesenta FPS en su M5 y demostraciones formales.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67dea524fc04155805ea5f62.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d8cd2cee891511d37be2531.jpg" alt="Visualizar el problema de los tres cuerpos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-113"></a>
### Case 113: [Una galería animada con varios estilos artísticos](https://x.com/blueemi99/status/2105782154387189771) (por [@blueemi99](https://x.com/blueemi99))

**Compara varios estilos artísticos dentro de una misma galería animada.**

El autor comparte una galería de animaciones creada con el ajuste xhigh. El resultado reúne varios estilos artísticos y permite comparar tratamientos visuales dentro de una sola obra.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/502971e471d8a4dd737c51a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2ad9b438a172b2ce1cd902b.jpg" alt="Una galería animada con varios estilos artísticos" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-114"></a>
### Case 114: [Compañeros robóticos y pelaje procedural](https://x.com/KanaWorks_AI/status/2106717014245183517) (por [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**Combina animación existente y refinamiento procedural en lugar de presentar todos los recursos como recién generados.**

El autor retoca una animación existente de perro robótico de Unimate para convertirlo en compañero y crea una mascota virtual peluda con cepillado y rastros. Unreal Engine y la animación robótica siguen siendo partes explícitas del flujo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9804d2afa56aa33c8d671292.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/612fe23ba65cde8186f80ddf.jpg" alt="Compañeros robóticos y pelaje procedural" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-115"></a>
### Case 115: [Un montaje animado de matemáticas](https://x.com/TurboNexic/status/2106710792590835934) (por [@TurboNexic](https://x.com/TurboNexic))

**Usa gráficos animados de temática matemática como ejemplo de comunicación visual.**

Quien publica comparte un montaje animado sobre matemáticas. El clip vertical presenta imágenes matemáticas como diseño animado; la publicación ofrece una demostración, no un cálculo matemático desarrollado.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57d4f16b728eff5d5f94b073.jpg" alt="Un montaje animado de matemáticas" width="760">

*Fotograma archivado del vídeo original.*

Type: Demo | Date: 2026-10-04

---

<a id="case-116"></a>
### Case 116: [Un vídeo con la letra de Your Woman](https://x.com/atomtanstudio/status/2106702854639743467) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Construye la animación de letras alrededor de una grabación suministrada y aclara el papel de la música.**

El creador comparte un vídeo con la letra de Your Woman, de White Town. La canción existente es la entrada de audio del tratamiento visual, no una composición atribuida al modelo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/88157c7612eb6c005275619c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d447b9a8d799f508738e89d4.jpg" alt="Un vídeo con la letra de Your Woman" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-117"></a>
### Case 117: [Redibujar un videoclip en JavaScript](https://x.com/abhinavflac/status/2106638839666373114) (por [@abhinavflac](https://x.com/abhinavflac))

**Traza los fotogramas de un vídeo suministrado con formas basadas en código para recrear su tratamiento visual.**

El autor describe cómo traza fotogramas del vídeo Godzilla de Eminem en formas planas y los redibuja con JavaScript. El metraje y la música originales son entradas de la animación resultante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c9ac6106098d63ff3d7ce8d7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b7d65e79fa8c8fa9aed2eda.jpg" alt="Redibujar un videoclip en JavaScript" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-118"></a>
### Case 118: [Una animación sobre el fútbol chino](https://x.com/esrhengwu/status/2106625966965760380) (por [@esrhengwu](https://x.com/esrhengwu))

**Convierte un tema deportivo en un encargo de narración animada.**

El autor comparte una animación sobre la selección china de fútbol, con su desarrollo y resiliencia como tema creativo. La grabación ofrece un ejemplo concreto de narración deportiva.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0e837b5c3551d3c3715337f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cd5e0537224d41a29e3e4d81.jpg" alt="Una animación sobre el fútbol chino" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-119"></a>
### Case 119: [Una muestra de retopología de una consola portátil](https://x.com/mickeysmith_jp/status/2106607349385630138) (por [@mickeysmith_jp](https://x.com/mickeysmith_jp))

**Compara el render de una consola portátil con su vista de alambre al hablar de topología.**

Quien publica combina una imagen de consola portátil con una vista de tipo alámbrico al comentar retopología. La comparación es una presentación concreta de modelado, no una malla editable ni un procedimiento de retopología documentado.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ec1260c667d8139c4cfed70a.jpg" alt="Una muestra de retopología de una consola portátil" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-120"></a>
### Case 120: [Minecraft se encuentra con Pokémon](https://x.com/MozeTech/status/2106590326634983710) (por [@MozeTech](https://x.com/MozeTech))

**Combina las mecánicas de dos juegos conocidos en el encargo de un prototipo.**

El autor presenta un prototipo de Pueblo Paleta que mezcla construcción y fabricación al estilo Minecraft con captura al estilo Pokémon, y enlaza una demo. La publicación lo describe como un experimento de una sola generación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5ca78d7ae17e27f0c3728df6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/829a3e03f20c6f9f8c58cd5c.jpg" alt="Minecraft se encuentra con Pokémon" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-121"></a>
### Case 121: [Un vídeo que explica cómo se crea un LLM](https://x.com/imjustnewatai/status/2106546810793730419) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Convierte una pregunta técnica en una solicitud de explicación visual.**

El autor pregunta cómo se crea un gran modelo de lenguaje y comparte el vídeo explicativo obtenido. La obra ofrece un ejemplo concreto de cómo presentar un tema técnico mediante una secuencia animada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6a944b8ff013c87884dd9e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d36e53c6eaf410eed54236a.jpg" alt="Un vídeo que explica cómo se crea un LLM" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-122"></a>
### Case 122: [Un montaje de momentos destacados de Altman](https://x.com/benchmark_lb900/status/2106539977404506303) (por [@benchmark_lb900](https://x.com/benchmark_lb900))

**Usa una figura pública como tema para probar el ritmo de un montaje animado breve.**

El autor comparte un vídeo de momentos destacados de Altman y lo describe como un resultado generado de una sola vez. La grabación vertical constituye un ejemplo compacto de montaje animado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/af9cca794a0a4f1532bcc60d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d683cf1f4c3f2a25f5a3db76.jpg" alt="Un montaje de momentos destacados de Altman" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-123"></a>
### Case 123: [La primera de las Treinta y Seis Estratagemas](https://x.com/jesselaunz/status/2106538284197548122) (por [@jesselaunz](https://x.com/jesselaunz))

**Documenta las herramientas musicales externas dentro de un flujo de animación narrativa.**

El autor comparte un film sobre la primera de las Treinta y Seis Estratagemas y menciona una única instrucción. Suno V6 aparece como herramienta musical, conservando así el papel separado del audio.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1adf495a8a97637ea487129d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc271c45635d54a258cf5e29.jpg" alt="La primera de las Treinta y Seis Estratagemas" width="760"></a>

Type: Demo | Date: 2026-10-04

---

<a id="case-124"></a>
### Case 124: [Modelado, rigging y animación de videojuegos](https://x.com/atomtanstudio/status/2106516974662713477) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Evalúa conjuntamente creación de personajes, rigging y animación en una comparación de escenas de juego.**

El autor presenta una comparación de Depths of Despair con modelado de personajes, rigging y animación. La publicación describe los recursos y herramientas empleados y reúne los resultados visibles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/543488d55fbd3bf31a838793.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/618e83e5f19e49a8cac14986.jpg" alt="Modelado, rigging y animación de videojuegos" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-125"></a>
### Case 125: [Un film sin palabras sobre mortalidad infantil](https://x.com/cocoloba_/status/2106512963414970458) (por [@cocoloba_](https://x.com/cocoloba_))

**Comunica un tema social difícil mediante una secuencia visual sin palabras.**

El autor comparte un film sobre mortalidad infantil que utiliza un bebé respirando y cunas oscurecidas como imágenes narrativas. El caso conserva la tarea de narración visual sin asumir las estadísticas demográficas del film.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c27b689422cbbf3a151c91b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a25e576f265e01b5c543c3ab.jpg" alt="Un film sin palabras sobre mortalidad infantil" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-126"></a>
### Case 126: [Una animación SVG de la glucólisis al etanol](https://x.com/olddonkeyblog/status/2106508425211330750) (por [@olddonkeyblog](https://x.com/olddonkeyblog))

**Integra SVG animado en HTML para explicar un proceso molecular.**

El autor solicita una molécula de glucosa que atraviese la glucólisis y la formación de etanol, representada como SVG animado dentro de HTML. La grabación muestra el tratamiento de visualización científica obtenido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c7ebfa65fa03ac5dddefbc7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34dd4d34fa6d9a00374141d7.jpg" alt="Una animación SVG de la glucólisis al etanol" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-127"></a>
### Case 127: [Dieciséis lanzamientos simultáneos de Starship](https://x.com/olddonkeyblog/status/2106507742454403485) (por [@olddonkeyblog](https://x.com/olddonkeyblog))

**Especifica fases de lanzamiento sincronizadas al definir una animación HTML y SVG.**

El autor solicita dieciséis Starship despegando juntos, seguidos de separación de etapas y entrada en el espacio. La grabación presenta la secuencia animada con múltiples objetos resultante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/61849da7a881419b60dcae41.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98d75b5f7d113ae54ac1753d.jpg" alt="Dieciséis lanzamientos simultáneos de Starship" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-128"></a>
### Case 128: [Una prueba animada del pelícano en bicicleta](https://x.com/olddonkeyblog/status/2106507429265756165) (por [@olddonkeyblog](https://x.com/olddonkeyblog))

**Examina una escena de pelícano en bicicleta como tarea de dibujo con movimientos coordinados.**

El autor comparte su ejecución con razonamiento Max de la prueba del pelícano en bicicleta. Es un resultado grabado distinto de las versiones de otros autores para la misma tarea general.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3b9b0bf5ec86fce138a1221.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b201da22cf822e627212671b.jpg" alt="Una prueba animada del pelícano en bicicleta" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-129"></a>
### Case 129: [Una historia de los próximos 150 años](https://x.com/imjustnewatai/status/2106489784382197771) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Combina guion, imágenes programadas y música en un encargo de ficción sobre el futuro.**

El autor afirma que una única instrucción produjo un film sobre los próximos ciento cincuenta años de la humanidad. La obra combina narración escrita, animación programada y música para representar posibles formas de vida futuras.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/228b236d407998ac39491f5e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2e714a53df372ed797a7e907.jpg" alt="Una historia de los próximos 150 años" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-130"></a>
### Case 130: [Un experimento independiente de Humanity Walks](https://x.com/iowitz/status/2106489119186538583) (por [@iowitz](https://x.com/iowitz))

**Retoma una idea de animación sobre historia del arte como experimento creativo independiente.**

Tras ver otras demostraciones, el autor intenta su propia animación de un paseo por la historia del arte y comparte el resultado. El clip se mantiene como generación distinta, sin fusionarlo solo por la similitud temática.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f27280f609dadc28672aefdf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7dd72b2ab4bfe3aefa8be062.jpg" alt="Un experimento independiente de Humanity Walks" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-131"></a>
### Case 131: [El film programado The Grader](https://x.com/argofowl/status/2106476549046513947) (por [@argofowl](https://x.com/argofowl))

**Documenta la generación externa de voz o audio al presentar un film programado.**

El autor comparte The Grader como un film realizado con código y cita ElevenLabs v4 para el audio. La publicación describe una sola ejecución de unas dos horas y veintidós minutos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef0a1ded02ef50db2842e393.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/81326a05ce8ec8e64457d4db.jpg" alt="El film programado The Grader" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-132"></a>
### Case 132: [El corto de terror Reawakening](https://x.com/JaydenDavisNC/status/2106440774367822008) (por [@JaydenDavisNC](https://x.com/JaydenDavisNC))

**Orienta un corto animado con una premisa de terror definida.**

El autor comparte Reawakening, un corto de terror realizado con IA. La obra adjunta ofrece un ejemplo concreto de narración y atmósfera para un encargo de animación de terror.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676985e8db9f61d999309cb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f76cd5c697edd52c235ad972.jpg" alt="El corto de terror Reawakening" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-133"></a>
### Case 133: [Un vídeo de 25 segundos sobre mejora propia](https://x.com/DAssetBuzz/status/2106505100575592838) (por [@DAssetBuzz](https://x.com/DAssetBuzz))

**Convierte una idea abstracta de mejora propia en un encargo creativo para un film breve.**

El autor solicita un vídeo de veinticinco segundos sobre qué haría mejor al modelo y comparte el resultado. La premisa funciona como narración creativa, no como afirmación de capacidades del producto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fceb3fc0b2fd1a45e4df6598.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5affafaa899381ebb0c07c9d.jpg" alt="Un vídeo de 25 segundos sobre mejora propia" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-134"></a>
### Case 134: [Una escena de castillo con comentarios sobre coste](https://x.com/nemumusitocha/status/2106429338556207284) (por [@nemumusitocha](https://x.com/nemumusitocha))

**Considera el detalle visual y la experiencia de uso del autor al evaluar una escena 3D.**

El autor comparte un castillo detallado, elogia su construcción visual y considera poco rentable su coste de uso. El caso combina una escena concreta con su valoración de la relación entre coste y satisfacción.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca4e00fb991a531a91b787ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c437830c5a26908acecb2664.jpg" alt="Una escena de castillo con comentarios sobre coste" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-135"></a>
### Case 135: [Un anuncio de lanzamiento de marca de 40 segundos](https://x.com/0xashtonx/status/2106421702783914423) (por [@0xashtonx](https://x.com/0xashtonx))

**Usa tu propia marca como tema de un encargo conciso de anuncio de lanzamiento.**

El creador solicita un anuncio de lanzamiento de cuarenta segundos para su propia marca y comparte el vídeo obtenido. La tarea ejemplifica la generación de una narración promocional de marca.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fe3a0894e5fb290708fe2559.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/769040e88e5fa00440daf93b.jpg" alt="Un anuncio de lanzamiento de marca de 40 segundos" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-136"></a>
### Case 136: [Una nueva versión de Rocketball](https://x.com/atomtanstudio/status/2106418747083022555) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Combina recursos programados y mecánicas interactivas al recrear un juego conocido.**

El autor comparte Rocketball, una recreación del juego de C-64 de los años ochenta, y afirma que sus recursos están programados. Sustituir una versión del sitio web se describe como un plan futuro.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c9049d48131242460ff0b08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/840804f6fc059b910cecbea5.jpg" alt="Una nueva versión de Rocketball" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-137"></a>
### Case 137: [Una comparación de pagodas en vóxeles](https://x.com/dropout_layer/status/2106408147309252915) (por [@dropout_layer](https://x.com/dropout_layer))

**Compara dos ejecuciones de la misma escena junto con los costes declarados de cada una.**

El autor muestra resultados de Astra y Fable para una pagoda 3D en vóxeles y señala costes de 3,50 y 5,50 dólares respectivamente. La comparación se refiere a esas ejecuciones concretas y sus escenas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/21478220f08972929cc315d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eb7e758f0ca20099e8ec2b71.jpg" alt="Una comparación de pagodas en vóxeles" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-138"></a>
### Case 138: [La presentación de una Switch 3 imaginaria](https://x.com/mathisbuilds/status/2106407842240418097) (por [@mathisbuilds](https://x.com/mathisbuilds))

**Usa un producto imaginario como tarea de presentación de concepto y demostración.**

El autor solicita una Nintendo Switch 3 imaginaria con una demo y relata unas cuatro horas de trabajo. La grabación presenta un concepto ficticio de próxima consola, no especificaciones de un producto real.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9cedd5846e7c44a4b8b18e60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a0c87ad253a8e1de157e1b4.jpg" alt="La presentación de una Switch 3 imaginaria" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-139"></a>
### Case 139: [Páginas de destino antes y después](https://x.com/nemumusitocha/status/2106402952307200302) (por [@nemumusitocha](https://x.com/nemumusitocha))

**Repite el mismo prompt de página de destino para comparar cambios en los resultados con el tiempo.**

El autor compara una página de destino recién generada con otra anterior creada con el mismo prompt. Los diseños visibles de antes y después aportan un ejemplo práctico de comparación de interfaces.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9200a6fe533b722eb9689f98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/11891711d14bb0550e4e3dcf.jpg" alt="Páginas de destino antes y después" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-140"></a>
### Case 140: [La perspectiva interior imaginada de una IA](https://x.com/blueemi99/status/2106397329653719115) (por [@blueemi99](https://x.com/blueemi99))

**Usa una perspectiva interior imaginada como premisa para una animación creativa.**

El autor pide un film sobre cómo podría sentirse ser un modelo de IA y comparte un resultado de una sola generación. La premisa se presenta como expresión visual imaginativa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/50e0c388c8aa359236e320a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbe79d20f3e6b68059837a0b.jpg" alt="La perspectiva interior imaginada de una IA" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-141"></a>
### Case 141: [Animación de la letra de Go](https://x.com/atomtanstudio/status/2106377491267137848) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Anima una letra suministrada alrededor de una grabación musical existente.**

El creador comparte un vídeo con la letra de Go, de The Chemical Brothers, y dice haber usado razonamiento Max. La grabación de la canción sigue siendo la entrada de audio externa de la tarea de motion design.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/60df0d5a6a73acd36b32f482.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d7f53506169267888481454.jpg" alt="Animación de la letra de Go" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-142"></a>
### Case 142: [Un segundo portfolio animado de 15 segundos](https://x.com/Saccc_c/status/2106376222309761094) (por [@Saccc_c](https://x.com/Saccc_c))

**Explora una nueva dirección visual con un encargo libre de portfolio de motion design.**

El autor comparte un nuevo portfolio animado de quince segundos y facilita el prompt creativo. Su relato distingue explícitamente esta generación de un trabajo de portfolio anterior.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67cc18e0020d5a96713de1a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e3680ff12a107b5d15bd4e5e.jpg" alt="Un segundo portfolio animado de 15 segundos" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-143"></a>
### Case 143: [Una revisión guiada de la implementación de un agente](https://x.com/RobIW_dev/status/2106371025852108940) (por [@RobIW_dev](https://x.com/RobIW_dev))

**Revisa el encaje de los planes en el sistema antes de pasar de la ideación a la ejecución.**

El autor comparte pautas sobre encaje en el sistema, planificación de la implementación y explicaciones. Describe cómo revisa el trabajo realizado o decide qué implementar después; la imagen conserva el material concreto de planificación.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c308ed282e70b605ddc2d74.jpg" alt="Una revisión guiada de la implementación de un agente" width="760">

Type: Tutorial | Date: 2026-10-03

---

<a id="case-144"></a>
### Case 144: [El baile de la mascota Claude](https://x.com/ishuagra02/status/2106369929813594134) (por [@ishuagra02](https://x.com/ishuagra02))

**Prueba la relación entre movimiento y música con una animación de mascota sincronizada con el ritmo.**

El creador comparte un baile de la mascota Claude y afirma que la animación sigue el ritmo. Las republicaciones del mismo vídeo nativo se asocian a esta fuente en lugar de contarse otra vez.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/448f60510bc8d206d9871580.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9943078ebfa5f29928ff11cb.jpg" alt="El baile de la mascota Claude" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-145"></a>
### Case 145: [Las islas interactivas de las Siete Maravillas](https://x.com/notjazii/status/2106368606502334922) (por [@notjazii](https://x.com/notjazii))

**Usa edificios emblemáticos como destinos en una escena insular interactiva.**

Quien publica comparte una escena de las Siete Maravillas organizada en islas 3D con edificios emblemáticos. La grabación ejemplifica el uso de monumentos reconocibles para estructurar un entorno visual interactivo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7c2548aa2216a05d6bcf88cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be4f38faca4efaaf2d37bb34.jpg" alt="Las islas interactivas de las Siete Maravillas" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-146"></a>
### Case 146: [Un videoclip para Propellerheads](https://x.com/atomtanstudio/status/2106353569603736009) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Apoya una secuencia larga de gráficos animados en una banda sonora suministrada.**

El creador comparte un tratamiento de videoclip para On Her Majesty’s Secret Service, de Propellerheads. La grabación existente es la entrada de audio de la secuencia visual animada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2691b42909079f64e659008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47f911d1f26059bbbf87adfd.jpg" alt="Un videoclip para Propellerheads" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-147"></a>
### Case 147: [Comparación de animaciones de Steamboat Willie](https://x.com/mathisbuilds/status/2106351978691305732) (por [@mathisbuilds](https://x.com/mathisbuilds))

**Compara dos tratamientos animados de la misma escena breve con el sonido activado.**

El autor comparte una comparación de Steamboat Willie etiquetada como Fable y Opus con esfuerzo xhigh, y describe resultados de una sola generación. El clip presenta esa comparación concreta de imagen y sonido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b59fcf68af9079043710bfb1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9d3ddb610977282fb47d094a.jpg" alt="Comparación de animaciones de Steamboat Willie" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-148"></a>
### Case 148: [Un film inspirado en Sanxingdui](https://x.com/hungryturbo/status/2106339115642019904) (por [@hungryturbo](https://x.com/hungryturbo))

**Organiza un corto animado alrededor de un tema cultural e histórico.**

El autor comparte un film de Sanxingdui como obra de narración visual creativa. La grabación muestra concretamente cómo convertir un tema histórico y cultural en un encargo de animación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b543f8114bf971a25cfc075.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/54b30b962a562cf71c5c7d1c.jpg" alt="Un film inspirado en Sanxingdui" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-149"></a>
### Case 149: [Un Bugatti Chiron antes y después](https://x.com/alannnfx/status/2106323394350461031) (por [@alannnfx](https://x.com/alannnfx))

**Repite un prompt anterior de automóvil para comparar modelado y detalles funcionales.**

El mismo autor presenta resultados de un Bugatti Chiron de una ejecución anterior y de un prompt repetido. La comparación grabada de antes y después se centra en un modelado y unos detalles de escena más ricos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dce62441af2bc515349c9da8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/539bcbf357d029adf665b992.jpg" alt="Un Bugatti Chiron antes y después" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-150"></a>
### Case 150: [El film conceptual GRAIN](https://x.com/NFT_Chen/status/2106301427052360150) (por [@NFT_Chen](https://x.com/NFT_Chen))

**Construye un film conceptual abstracto alrededor de motivos visuales recurrentes.**

El creador comparte GRAIN, un corto conceptual que conecta una semilla, un grano, un árbol e imágenes de montaña. Las formas y transiciones recurrentes constituyen su estructura narrativa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/57e75bacc95f9cd23460f659.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fed7820dddd11b739076aca8.jpg" alt="El film conceptual GRAIN" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-151"></a>
### Case 151: [La galería artística Human in Transit](https://x.com/exploraX_/status/2106296439936614646) (por [@exploraX_](https://x.com/exploraX_))

**Presenta un recorrido visual histórico mediante una galería de estilo interactivo.**

Quien publica comparte Human in Transit, una galería que pasa de estilos artísticos antiguos a modernos. La interfaz grabada ofrece una referencia concreta para organizar varios periodos visuales en una presentación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e04f07e2356151e268d5f30.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/260ec41d2d9b54a24e325d14.jpg" alt="La galería artística Human in Transit" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-152"></a>
### Case 152: [Un corto visual sobre la Ruta de la Seda](https://x.com/hungryturbo/status/2106294812261695508) (por [@hungryturbo](https://x.com/hungryturbo))

**Transforma un tema de viaje e historia en un corto visual coherente.**

El autor comparte un film sobre la Ruta de la Seda. La obra adjunta ofrece una representación creativa concreta de un viaje histórico mediante imágenes animadas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/07116e11e8c8a0e5899ae8bd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3a64357c0519bd7524f7949a.jpg" alt="Un corto visual sobre la Ruta de la Seda" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-153"></a>
### Case 153: [Una presentación sobre cuatro transformaciones](https://x.com/dpkostka/status/2106272731364794757) (por [@dpkostka](https://x.com/dpkostka))

**Usa un marco de transformación como estructura organizativa de una presentación.**

El autor comparte diapositivas que describen cuatro caminos de transformación. La imagen adjunta muestra cómo organizar un marco conceptual en un documento visual.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa84b5e612da3b4d740c390.jpg" alt="Una presentación sobre cuatro transformaciones" width="760">

Type: Demo | Date: 2026-10-03

---

<a id="case-154"></a>
### Case 154: [Comparar el tono de conversaciones anteriores](https://x.com/kiyoshi_shin/status/2106268573186637883) (por [@kiyoshi_shin](https://x.com/kiyoshi_shin))

**Compara registros de conversación antiguos con respuestas actuales para examinar cambios de tono.**

El autor pide al modelo actual que analice conversaciones anteriores y su estilo presente, y después expresa descontento con el cambio de tono. La imagen adjunta registra esa tarea de comparación conversacional.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df5dc4983c09495b3e4dfbf.jpg" alt="Comparar el tono de conversaciones anteriores" width="760">

Type: Evaluation | Date: 2026-10-03

---

<a id="case-155"></a>
### Case 155: [Una prueba de ternura con un kakapo](https://x.com/hanawo_neki/status/2106257409782288659) (por [@hanawo_neki](https://x.com/hanawo_neki))

**Compara estilos de animación con una tarea concreta sobre preferencias de personajes.**

El autor comparte una animación de kakapo y afirma preferir Opus en esta comparación centrada en la ternura. El caso conserva la crítica estética junto con el resultado animado publicado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3328698e23303648334dda0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f51048a616b2d6c9471f9774.jpg" alt="Una prueba de ternura con un kakapo" width="760"></a>

Type: Evaluation | Date: 2026-10-03

---

<a id="case-156"></a>
### Case 156: [Spider-Man a través de diez épocas del cómic](https://x.com/chetaslua/status/2106248621519978867) (por [@chetaslua](https://x.com/chetaslua))

**Mantén reconocible a un personaje mientras atraviesa distintas épocas del cómic.**

El autor de la publicación original presenta a Spider-Man en diez épocas del cómic. Otros posts que reutilizan el mismo vídeo se asocian a esta fuente en vez de contarse como obras adicionales.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b71937c3743eed2ba92de90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72f77356b6e8293005144d0c.jpg" alt="Spider-Man a través de diez épocas del cómic" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-157"></a>
### Case 157: [Un vídeo ficticio de terror sobre los Illuminati](https://x.com/badboyfoxy/status/2106241189976387799) (por [@badboyfoxy](https://x.com/badboyfoxy))

**Trata un encargo de terror conspirativo como ejercicio de ficción.**

El autor pide un vídeo de miedo sobre los Illuminati y comparte el resultado. El tema aporta una premisa ficticia de terror para la animación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6c9b503c1d226dfc63700cd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f2715bf396e76b3b9a421c43.jpg" alt="Un vídeo ficticio de terror sobre los Illuminati" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-158"></a>
### Case 158: [Un film programado de historia de la ciencia nuclear](https://x.com/imjustnewatai/status/2106238699872956427) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Combina un renderizador programado a medida y música para un vídeo explicativo de historia científica.**

El autor solicita un film 3D de tres minutos sobre cómo la ciencia nuclear hizo posible la bomba atómica y después menciona fotogramas dibujados, un renderizador propio y música sintetizada. El caso trata del flujo de producción audiovisual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3bb5c1a7d19214aa2df7c15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddd5eadabcd20e7c99f8a84b.jpg" alt="Un film programado de historia de la ciencia nuclear" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-159"></a>
### Case 159: [Un vídeo explicativo sobre ingresos altos universales](https://x.com/markbraincell/status/2106234118514323515) (por [@markbraincell](https://x.com/markbraincell))

**Comunica un concepto económico mediante una explicación animada.**

Quien publica comparte una animación que explica los ingresos altos universales. La grabación es un ejemplo concreto de explicación conceptual, sin convertir el argumento económico representado en un resultado medido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d3dc85ce581ace81d5dee727.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c47951c1cdaf4f43cdc3b40b.jpg" alt="Un vídeo explicativo sobre ingresos altos universales" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-160"></a>
### Case 160: [Un vídeo explicativo del conflicto Altman–Amodei](https://x.com/imjustnewatai/status/2106204392588276065) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Usa una disputa como estructura narrativa de un vídeo explicativo animado.**

El autor solicita un relato animado del conflicto Altman–Amodei y comparte el vídeo obtenido. La tarea muestra un formato explicativo de actualidad, no una narración histórica investigada de forma independiente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5728468c70009e5a30391f08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad00b822edd0e9f7afcfa7f0.jpg" alt="Un vídeo explicativo del conflicto Altman–Amodei" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-161"></a>
### Case 161: [Un videoclip con la mascota Claude](https://x.com/synthshareai/status/2106195060140446028) (por [@synthshareai](https://x.com/synthshareai))

**Combina una mascota superpuesta y metraje suministrado para un montaje musical centrado en un personaje.**

Quien publica muestra una mascota Claude sobre el fondo de un videoclip de imagen real y relata una ejecución de doce horas. El tratamiento visible combina una superposición animada con metraje suministrado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c19520473733d1f7435a38d3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/77afb2d88514b8e9fb89e8fc.jpg" alt="Un videoclip con la mascota Claude" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-162"></a>
### Case 162: [Un zoom continuo de los quarks al universo](https://x.com/imjustnewatai/status/2106190594775097663) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Conecta escalas científicas en una historia audiovisual mediante un zoom continuo.**

El autor describe imágenes programadas y música sintetizada para un zoom que va de los quarks al universo. La grabación muestra transiciones continuas de escala y una narración visual coherente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/721f59cdc3678e81c567dead.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/395d2654b5b0a3e977b472c8.jpg" alt="Un zoom continuo de los quarks al universo" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-163"></a>
### Case 163: [Imaginar el mundo en 2076](https://x.com/Layton_Gott/status/2106190496075035096) (por [@Layton_Gott](https://x.com/Layton_Gott))

**Pide una escena del mundo futuro con una duración narrativa concreta.**

El autor comparte un corto que imagina el mundo en 2076 tras solicitar un vídeo de veinticinco segundos. La reutilización de la misma grabación por otras cuentas se asocia a esta fuente.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/48731c19330bc992204fb804.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d2b707821e78f6d02308051.jpg" alt="Imaginar el mundo en 2076" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-164"></a>
### Case 164: [Cronología de edificios de Lower Manhattan](https://x.com/nroze22/status/2106183281293381661) (por [@nroze22](https://x.com/nroze22))

**Combina huellas de edificios, fechas y alturas en una interfaz de cronología arquitectónica.**

El autor presenta Lower Manhattan mediante una interfaz de dibujo arquitectónico que muestra fechas de construcción, huellas y alturas. La grabación ofrece un concepto concreto de cronología interactiva.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5eadbb9d6620c56cdfd20db7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/439a32860dc89b2ff304e991.jpg" alt="Cronología de edificios de Lower Manhattan" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-165"></a>
### Case 165: [Una animación sobre escritura oracular](https://x.com/MinLiBuilds/status/2106180691344118202) (por [@MinLiBuilds](https://x.com/MinLiBuilds))

**Usa la evolución de la escritura como tema de un recorrido histórico animado.**

El autor comparte una animación que comienza con la escritura sobre huesos oraculares. La grabación ofrece un ejemplo concreto de narración visual centrada en la historia de los caracteres escritos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0d0e033e83e40406963c1624.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0a7fb3b121acab9ff0f387f8.jpg" alt="Una animación sobre escritura oracular" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-166"></a>
### Case 166: [Otra animación de personajes por la historia del arte](https://x.com/imjustnewatai/status/2106162924331180510) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Usa personajes familiares como guías continuas por un escenario histórico cambiante.**

El autor pide a Iron Man y Spider-Man volando por la historia y comparte la animación obtenida. Es una obra distinta de los experimentos de otros autores que recorren la historia del arte con personajes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/13b5f9341ac3c45e858cfc2e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e90b1577480524f8edac5080.jpg" alt="Otra animación de personajes por la historia del arte" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-167"></a>
### Case 167: [Una obra audiovisual programada sobre Seikilos](https://x.com/YanqingCheng/status/2106158746938269728) (por [@YanqingCheng](https://x.com/YanqingCheng))

**Construye una obra audiovisual de un solo archivo alrededor de un texto musical histórico.**

El autor comparte una obra sobre el epitafio de Seikilos y describe imágenes y música sintetizadas con HTML y JavaScript en un único archivo. El texto histórico organiza la secuencia audiovisual programada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ac7bdaa973e41a073c063606.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3aa2fd116482590d4761d329.jpg" alt="Una obra audiovisual programada sobre Seikilos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-168"></a>
### Case 168: [Comparación de animaciones de jets](https://x.com/Kinzf2121/status/2106158536963330346) (por [@Kinzf2121](https://x.com/Kinzf2121))

**Compara vuelo y seguimiento de cámara en la misma tarea de animación aérea.**

El autor comparte una comparación de jets entre un resultado etiquetado como Fable 5.1 y Opus. Las escenas permiten comparar movimiento del avión y seguimiento cinematográfico de cámara.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d5ca08b004ee0b0477384ae4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/51c2eff3a0af7f83a1063f02.jpg" alt="Comparación de animaciones de jets" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-169"></a>
### Case 169: [Un film de presentación del modelo](https://x.com/devteamdrew/status/2106155815707021549) (por [@devteamdrew](https://x.com/devteamdrew))

**Explora una animación sobre el modelo a partir de un encargo de presentación propia.**

El creador relata que pidió un vídeo de presentación con un solo prompt y comparte el film obtenido. La tarea combina una narración sobre el modelo con una presentación animada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f622576a03f5acf8fd1d6a8c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/67a3f8209951f7177817309f.jpg" alt="Un film de presentación del modelo" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-170"></a>
### Case 170: [Un prototipo de cartas postapocalíptico](https://x.com/maciejkrupowies/status/2106153578029338850) (por [@maciejkrupowies](https://x.com/maciejkrupowies))

**Crea un prototipo temático de cartas y examina la interfaz de combate resultante.**

El autor muestra un prototipo postapocalíptico al estilo Hearthstone y lo describe como una construcción de una sola generación. El post reconoce pequeños fallos mientras muestra la interfaz y las interacciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8d4ee0351fbc1bf402a6fbe9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/010130286ef1cd23d112191a.jpg" alt="Un prototipo de cartas postapocalíptico" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-171"></a>
### Case 171: [La animación de oficina The Late Byte](https://x.com/rohit3a/status/2106138910648914094) (por [@rohit3a](https://x.com/rohit3a))

**Convierte las personalidades de los modelos en personajes de una conversación animada de oficina.**

El creador presenta The Late Byte, una historia de oficina animada con Opus como jefe enfadado. Es una narración distinta del film Day in the Life of Claude.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/15c94a558525f7353af74d9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8591839693983a13e85a16e.jpg" alt="La animación de oficina The Late Byte" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-172"></a>
### Case 172: [Animación de letras de Queens of the Stone Age](https://x.com/atomtanstudio/status/2106135196483608745) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Combina una canción suministrada con tipografía cinética y motion design.**

El creador describe un videoclip de tipografía cinética alrededor de una grabación de Queens of the Stone Age. La canción es una entrada de audio suministrada; el ejemplo trata de organizar sus letras e imágenes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29baacc9a5d79663d028c0d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/85f77ab89071911301d88f92.jpg" alt="Animación de letras de Queens of the Stone Age" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-173"></a>
### Case 173: [Una escena narrativa de Three.js compartida](https://x.com/Noreply134882/status/2106116572389478746) (por [@Noreply134882](https://x.com/Noreply134882))

**Usa una historia 3D compartida como referencia de diseño narrativo.**

Quien publica comparte una escena narrativa de Three.js y comenta un consumo elevado de tokens. El clip se conserva como ejemplo visual compartido de narración en 3D.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e82bc5fcc6a848f88a5e0fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/565cf7c430705cc48ac8ab71.jpg" alt="Una escena narrativa de Three.js compartida" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-174"></a>
### Case 174: [Moonwalk por escenarios históricos](https://x.com/noclipepe/status/2106105810812112937) (por [@noclipepe](https://x.com/noclipepe))

**Lleva un motivo de baile por distintos escenarios y estilos históricos.**

Quien publica comparte una secuencia de Michael Jackson haciendo moonwalk desde los dinosaurios hasta la Luna. El film se conserva como ejemplo compartido de baile y galería de estilos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34c25a1d7f0c405d9ce529bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/096ac813acdfe28a3e52f16c.jpg" alt="Moonwalk por escenarios históricos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-175"></a>
### Case 175: [Gráficos animados con un prompt detallado](https://x.com/devswha/status/2106100273509007802) (por [@devswha](https://x.com/devswha))

**Compara un encargo creativo detallado con una petición de motion design más breve.**

El autor comparte un vídeo de gráficos animados y afirma haber proporcionado solo un prompt detallado, sin recursos, vídeo de referencia ni archivos fuente. El resultado sirve como referencia concreta de motion design guiado por prompts.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/04f82b6cb08e4416d82850b5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4df2d47adf0c0b1b795a13f7.jpg" alt="Gráficos animados con un prompt detallado" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-176"></a>
### Case 176: [La interfaz de un negocio de alquiler](https://x.com/oalanicolas/status/2106098902965309475) (por [@oalanicolas](https://x.com/oalanicolas))

**Explora una interfaz web concreta con un encargo de negocio de alquiler.**

El creador comparte una captura de la interfaz de un sitio para un negocio de alquiler. El ejemplo trata del diseño visible de la página y de la presentación del negocio.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4260ce2518ee2b7ed4015670.jpg" alt="La interfaz de un negocio de alquiler" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-177"></a>
### Case 177: [Un film creativo sobre AGI](https://x.com/AndrewOnXYZ/status/2106097745098395712) (por [@AndrewOnXYZ](https://x.com/AndrewOnXYZ))

**Compara tratamientos narrativos y visuales con un prompt creativo recurrente.**

El autor comparte una animación sobre AGI producida con un prompt recurrente. Las declaraciones del modelo forman parte de la narración creativa del film.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/24a8cc2869d1f945c337dd51.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b19d60e7a61a0885999a9ec8.jpg" alt="Un film creativo sobre AGI" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-178"></a>
### Case 178: [Historia del arte con una subtrama de gatos](https://x.com/cherry_mx_reds/status/2106095190285144331) (por [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Condensa varios periodos artísticos en una narración breve con un personaje recurrente.**

El creador presenta un recorrido de quince segundos por la historia del arte con una subtrama de gatos. Los quince segundos se refieren a la duración del film; la tarea abarca muchos estilos históricos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/819481183fc7834d88cd5557.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3967f82d274d07f7ea7c11bc.jpg" alt="Historia del arte con una subtrama de gatos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-179"></a>
### Case 179: [Un prototipo de combate y una escena vóxel](https://x.com/OnlyTerp/status/2106089280502210626) (por [@OnlyTerp](https://x.com/OnlyTerp))

**Examina combate y construcción de mundos en los resultados de una tarea de programación creativa.**

El autor comparte un prototipo de combate al estilo DMC y una escena vóxel, y describe una generación larga. Los dos resultados permiten examinar mecánicas de juego y diseño visual de mundos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d8c9fdf7a2bb4ea0e4d3a53a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/03fc44f9f96cf5f3ae42b7bb.jpg" alt="Un prototipo de combate y una escena vóxel" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-180"></a>
### Case 180: [Cronología de memes de Internet](https://x.com/chetaslua/status/2106076940558082297) (por [@chetaslua](https://x.com/chetaslua))

**Organiza una cronología animada alrededor de estilos y música propios de cada año.**

El creador comparte una secuencia de memes virales de Internet entre 2010 y 2026. Cada año recibe un estilo visual y un tratamiento musical dentro de la narración programada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d33c0b55ae8c290665afdc29.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/29a4c6fbbf00bf107a493f8f.jpg" alt="Cronología de memes de Internet" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-181"></a>
### Case 181: [Movimiento de partículas desde una sola línea](https://x.com/devswha/status/2106072107365114186) (por [@devswha](https://x.com/devswha))

**Empieza con una línea de instrucciones antes de refinar un prompt de movimiento detallado.**

El creador comparte una animación de partículas generada desde una línea y dice que probará una petición más detallada. Es una generación distinta de su ejemplo de motion design más largo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5670b888b55ee404db63e456.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/445333acd2d116cb0887ab17.jpg" alt="Movimiento de partículas desde una sola línea" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-182"></a>
### Case 182: [La animación Kung-Fu Boy](https://x.com/HashmathRzz/status/2106065773336965510) (por [@HashmathRzz](https://x.com/HashmathRzz))

**Explora movimiento animado con un encargo de personaje de artes marciales.**

El autor comparte Kung-Fu Boy, una animación de personaje atribuida a Fable 5.5. La grabación aporta el resultado animado concreto de este tema de artes marciales.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f864ef82f64ca6225c0af261.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c21633c7b612e6a16d57881a.jpg" alt="La animación Kung-Fu Boy" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-183"></a>
### Case 183: [Un debate animado sobre el estrecho de Ormuz](https://x.com/chetaslua/status/2106060047805792415) (por [@chetaslua](https://x.com/chetaslua))

**Convierte un tema de debate en una narración animada.**

El creador presenta un debate animado sobre el estrecho de Ormuz. Este caso recoge el film visible, no los otros usos sin respaldo visual que aparecen alrededor de la publicación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1e47dad4b619080e0bb9a5ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c578ea3e94885b964cfe339b.jpg" alt="Un debate animado sobre el estrecho de Ormuz" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-184"></a>
### Case 184: [Un experimento SVG con un unicornio](https://x.com/atomtanstudio/status/2106057876053918127) (por [@atomtanstudio](https://x.com/atomtanstudio))

**Examina decisiones de estilo SVG con la misma tarea de dibujo temática.**

El autor comparte un experimento de unicornio en SVG inspirado en la prueba de otro creador. La imagen adjunta aporta el resultado concreto para comparar el tratamiento visual del mismo tema.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f24fc135aa4b7db69bcac72.jpg" alt="Un experimento SVG con un unicornio" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-185"></a>
### Case 185: [Una animación de temporada de Halloween](https://x.com/cherry_mx_reds/status/2106056643255447590) (por [@cherry_mx_reds](https://x.com/cherry_mx_reds))

**Da a un modelo de programación un tema estacional para una animación breve.**

El creador solicita una obra de Halloween y comparte la animación resultante. El post proporciona la grabación original de esa tarea creativa específica.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e60368675a61c0b6e62d1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cabbe8b2fe083d6ddc29e16.jpg" alt="Una animación de temporada de Halloween" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-186"></a>
### Case 186: [Un bárbaro y una portada con Blender CLI](https://x.com/BoDy051/status/2106047375320166885) (por [@BoDy051](https://x.com/BoDy051))

**Explora modelado de personajes y renderizado de portadas mediante instrucciones de Blender CLI.**

El autor compara un bárbaro de RPG y un concepto de portada con un resultado de Opus. Blender CLI es la herramienta de construcción y renderizado; el modelo proporciona instrucciones de código.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/74aeac02c879e17cc8cdbe2c.jpg" alt="Un bárbaro y una portada con Blender CLI" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-187"></a>
### Case 187: [Un día en la vida de Claude](https://x.com/ishuagra02/status/2106045364868419727) (por [@ishuagra02](https://x.com/ishuagra02))

**Construye una historia animada cotidiana alrededor de una mascota recurrente.**

El autor de la publicación original comparte Day in the Life of Claude con la mascota. El vídeo fuente es distinto de la animación de baile de la mascota y de sus republicaciones.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ce91d7bd6316929c0229c090.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aa0dfdca579e71891d871df8.jpg" alt="Un día en la vida de Claude" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-188"></a>
### Case 188: [La historia humana en 3D](https://x.com/blueemi99/status/2106041578204655748) (por [@blueemi99](https://x.com/blueemi99))

**Combina escenas programadas y animación en una secuencia histórica visual.**

El creador comparte un vídeo 3D desde la humanidad antigua hasta el presente y afirma haber generado animaciones y modelos con código. El resultado es un ejemplo de narración visual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/da237dda8714cc1f10d6bd8a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/72fd4829e96839ace8f79b29.jpg" alt="La historia humana en 3D" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-189"></a>
### Case 189: [Un reel rápido de motion design](https://x.com/blueemi99/status/2106031355922387163) (por [@blueemi99](https://x.com/blueemi99))

**Evalúa ritmo, sonido y coherencia en un reel breve de motion design.**

El autor comparte un vídeo de movimiento corto y rápido y compara su sonido y coherencia con su resultado de Opus. El juicio describe su experiencia con esa obra concreta.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ecbba68abe3d9a22e9428087.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/464ea3477781ec76d5decfa6.jpg" alt="Un reel rápido de motion design" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-190"></a>
### Case 190: [Una creación 3D compleja y libre](https://x.com/cocoloba_/status/2106029181607772413) (por [@cocoloba_](https://x.com/cocoloba_))

**Explora una composición 3D compleja con una petición creativa abierta.**

El creador pregunta qué haría el modelo con tiempo libre y comparte la obra 3D resultante. La publicación describe numerosas piezas separadas dentro de la composición generada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a1089bbf8543ef20056ae277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1ca7ca904b82e34a6dba88aa.jpg" alt="Una creación 3D compleja y libre" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-191"></a>
### Case 191: [Un combate animado de figuras de palo](https://x.com/HelaliBillel/status/2106028502763900944) (por [@HelaliBillel](https://x.com/HelaliBillel))

**Examina ritmo y movimiento mediante una petición específica de animación de combate.**

El creador solicita un vídeo de una pelea animada entre figuras de palo y comparte el resultado. La grabación aporta un ejemplo concreto de esa tarea de animación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e89ce685574f66dc969d7ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c6683c5a691eeff27424c02.jpg" alt="Un combate animado de figuras de palo" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-192"></a>
### Case 192: [Una secuencia de interfaz animada con un prompt](https://x.com/iancarscadden/status/2106018048792789360) (por [@iancarscadden](https://x.com/iancarscadden))

**Explora una secuencia de interfaz mediante un solo encargo de animación.**

El autor comparte una secuencia animada de interfaz descrita como resultado de una sola generación de unos seis o siete minutos. La grabación muestra la secuencia visual obtenida.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b12e9274a06ccbd02b7beca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e56eb58e5ab6e47d580f89b9.jpg" alt="Una secuencia de interfaz animada con un prompt" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-193"></a>
### Case 193: [Una animación ficticia de SCP-8517](https://x.com/eviljoker88/status/2106003621402005816) (por [@eviljoker88](https://x.com/eviljoker88))

**Usa una premisa inspirada en SCP como encargo de historia animada.**

El creador presenta una animación de SCP-8517 y atribuye su creación a Fable 5.5. El caso trata de la narración ficticia y de la animación visible.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f690173426f29f4863ea9ebc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ddfd1170158fa1156c0c433e.jpg" alt="Una animación ficticia de SCP-8517" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-194"></a>
### Case 194: [Una animación otoñal en acuarela](https://x.com/ishuagra02/status/2106000055706784118) (por [@ishuagra02](https://x.com/ishuagra02))

**Especifica un tema estacional y un tratamiento de acuarela para una animación.**

El autor comparte una animación de otoño en estilo acuarela. La obra grabada ejemplifica la combinación de un tema estacional con un medio visual concreto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8df65940753adf7d40a5cceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1091a42f052632de59288e3f.jpg" alt="Una animación otoñal en acuarela" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-195"></a>
### Case 195: [Un escenario de muñeca procedural](https://x.com/HelaliBillel/status/2105988689088196785) (por [@HelaliBillel](https://x.com/HelaliBillel))

**Examina cómo se anima un personaje de muñeca dentro de una escena preparada.**

El autor comparte una animación procedural de una muñeca sobre un escenario y menciona Blender en la conversación. El caso trata del personaje visible, la puesta en escena y la animación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c54a4f10f43cea2f2e27d2d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e6b8904c3350c8f84e148e53.jpg" alt="Un escenario de muñeca procedural" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-196"></a>
### Case 196: [Un pelícano en bicicleta renderizado en el navegador](https://x.com/slimcat0101/status/2105988654636380444) (por [@slimcat0101](https://x.com/slimcat0101))

**Ejecuta el movimiento de un personaje en un navegador y examina la escena renderizada.**

El creador pide un pelícano en bicicleta y graba el HTML resultante en un navegador. Es una escena móvil distinta de las pruebas de dibujo SVG estático.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c69f02880bf28ee4f25ce6af.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31ad3fe64536f637f3a2a1b7.jpg" alt="Un pelícano en bicicleta renderizado en el navegador" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-197"></a>
### Case 197: [El universo se observa a sí mismo](https://x.com/l_mejiaC/status/2105988529671360673) (por [@l_mejiaC](https://x.com/l_mejiaC))

**Conecta escalas lejanas mediante un recorrido visual continuo en una narración.**

El creador presenta una secuencia continua desde el Big Bang hasta un ojo humano. Describe las imágenes y la música como producidas por código en tiempo de ejecución para el film.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a9c7b6447a8f9c9d98b9f688.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/917d7f9d6fc4bffeb2de3dfd.jpg" alt="El universo se observa a sí mismo" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-198"></a>
### Case 198: [Una prueba independiente de animación de jet](https://x.com/AI_Screening/status/2105988448612135176) (por [@AI_Screening](https://x.com/AI_Screening))

**Repite una tarea de animación aérea y examina su resultado concreto.**

Después de leer debates sobre enrutamiento, el autor prueba una animación de jet y comparte el resultado. La grabación proporciona una fuente independiente para ese ejemplo aéreo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/02ca7dd974c9bda88336ee6c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/042d9f48293091af76915035.jpg" alt="Una prueba independiente de animación de jet" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-199"></a>
### Case 199: [Un primer reel de movimiento libre](https://x.com/Saccc_c/status/2105985484472377531) (por [@Saccc_c](https://x.com/Saccc_c))

**Explora motion design con un prompt corto y abierto.**

El creador comparte un primer reel de motion design descrito como generado con un solo prompt. Es un resultado anterior distinto de su posterior portfolio de quince segundos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c3a38710b7d416055f1b179e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42ff46736287463edb05c0db.jpg" alt="Un primer reel de movimiento libre" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-200"></a>
### Case 200: [Una civilización renderizada con código](https://x.com/ziwenxu_/status/2105983571848741045) (por [@ziwenxu_](https://x.com/ziwenxu_))

**Convierte un encargo de historia de la civilización en una narración animada programada.**

El autor pide la civilización desde sus inicios hasta el presente y comparte el film. Según el creador, este tratamiento visual programado no usa metraje ni recursos de archivo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/53e59b83e07f7070017b7119.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b9e27ef3f017676036965a5b.jpg" alt="Una civilización renderizada con código" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-201"></a>
### Case 201: [Comparación de un zoom del chip al servidor](https://x.com/SPAC89/status/2105968361725202591) (por [@SPAC89](https://x.com/SPAC89))

**Compara realismo y continuidad en una tarea de zoom del chip al servidor.**

El autor compara Fable XHigh y GPT Sol Ultra en una secuencia de zoom realista y comenta velocidad y uso de cuota. El post compara ejecuciones específicas de distintos niveles de suscripción.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c1d806fdedf55ab5e01ef7b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/554e8eab1e3441bf1cfcda5a.jpg" alt="Comparación de un zoom del chip al servidor" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-202"></a>
### Case 202: [Un proyecto personal de animación de viaje lunar](https://x.com/IgorGomezC/status/2105963552024506565) (por [@IgorGomezC](https://x.com/IgorGomezC))

**Explora un concepto de animación personal con varios modelos de programación.**

El creador comparte un proyecto personal de viaje lunar animado mientras comenta experimentos con Fable y Opus. La obra adjunta es el resultado concreto de esa exploración creativa.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7258363950323d6dcb60ce2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dbb92cddd2632d76ee23d9.jpg" alt="Un proyecto personal de animación de viaje lunar" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-203"></a>
### Case 203: [Comparación de escenas japonesas en vóxeles](https://x.com/vikktorrrre/status/2105955048018588084) (por [@vikktorrrre](https://x.com/vikktorrrre))

**Compara detalle, niebla y claridad visual con el mismo prompt de escena.**

El autor compara resultados actuales de Fable y Opus para el mismo prompt de escena japonesa en vóxeles. Sus observaciones tratan de claridad, niebla y estética de esos resultados específicos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/42cb05df63d6f8f11069a277.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d16d5913274502e53d2a78c1.jpg" alt="Comparación de escenas japonesas en vóxeles" width="760"></a>

Type: Evaluation | Date: 2026-10-02

---

<a id="case-204"></a>
### Case 204: [El corto audiovisual Steaming the Frontier](https://x.com/sdmat123/status/2105929299878703520) (por [@sdmat123](https://x.com/sdmat123))

**Combina una estética de tipo Steamboat y sonido para un corto audiovisual.**

El creador comparte Steaming the Frontier, una obra animada con sonido. Se mantiene como fuente separada de las creaciones independientes de tipo Steamboat de otros autores.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8a3ee558c975636152e2d45b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3dcb946918e8ca68e4806815.jpg" alt="El corto audiovisual Steaming the Frontier" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-205"></a>
### Case 205: [Superman en múltiples estilos artísticos](https://x.com/Mr_Salio/status/2105925979466052051) (por [@Mr_Salio](https://x.com/Mr_Salio))

**Lleva un personaje por estilos cambiantes en una animación continua.**

El creador dice que un ejemplo anterior de Superman inspiró una nueva generación y comparte su propio resultado. Sus imágenes diferentes lo convierten en una obra distinta, no en una republicación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/904b68da72810335d71bda04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/882a85d147b59a80ec07189b.jpg" alt="Superman en múltiples estilos artísticos" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-206"></a>
### Case 206: [Un prototipo de combate de jefe estilo Cupcake](https://x.com/maciejkrupowies/status/2105914965387321785) (por [@maciejkrupowies](https://x.com/maciejkrupowies))

**Crea un prototipo de combate lateral con un jefe y examina la acción resultante.**

El autor comparte un prototipo de combate de jefe estilo Cupcake y relata una sola generación en menos de diez minutos. La grabación muestra la secuencia de combate del juego.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ad1389879b4c375f0283752c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/efa70c53c5f15333bf5c0a0c.jpg" alt="Un prototipo de combate de jefe estilo Cupcake" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-207"></a>
### Case 207: [Un velero con posiciones cambiantes del sol](https://x.com/popat_kunj/status/2105907935490752822) (por [@popat_kunj](https://x.com/popat_kunj))

**Explora cielo, agua y posición solar mediante una escena de navegación.**

El creador comparte un velero en 3D con el sol en diferentes posiciones y enlaza un artefacto interactivo. La escena combina barco, cielo y agua en una tarea visual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/45a77b7321e65de4a52cf5ff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/98f7b224adade38056e8e676.jpg" alt="Un velero con posiciones cambiantes del sol" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-208"></a>
### Case 208: [Un vídeo de novedades de Paracortex y Pi](https://x.com/RobIW_dev/status/2105894547796476225) (por [@RobIW_dev](https://x.com/RobIW_dev))

**Convierte actualizaciones de producto en un anuncio breve de motion design.**

El autor transforma novedades de Paracortex y Pi en un vídeo de motion design de veinticinco segundos y aporta un prompt. La obra ejemplifica la comunicación visual de producto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3f8ecc71d06894b5a53dedaf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b2047613fd2963b0c82b0c1a.jpg" alt="Un vídeo de novedades de Paracortex y Pi" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-209"></a>
### Case 209: [Una promoción del sitio Curio 2.0](https://x.com/voltwake/status/2105884775982485642) (por [@voltwake](https://x.com/voltwake))

**Crea un film promocional programado para el lanzamiento de un sitio existente.**

El creador describe una promoción de lanzamiento de Curio 2.0 que combina imágenes programadas, cámara y música. El post comparte el film promocional obtenido.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e491cbb60b9d9ba91e8b41ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7947c8fe446d0ea07193fdba.jpg" alt="Una promoción del sitio Curio 2.0" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-210"></a>
### Case 210: [Una historia 3D imaginaria de Hugging Face](https://x.com/chetaslua/status/2105884276864782557) (por [@chetaslua](https://x.com/chetaslua))

**Combina código del modelo con herramientas de renderizado y audio para un film ficticio.**

El creador comparte una historia imaginaria de Hugging Face con código del modelo, Blender y la API de ElevenLabs. Blender construye y renderiza, mientras ElevenLabs proporciona audio externo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6e399daf7a4eb7d2ce6d564f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/9c5d19c147ecea8b40b22523.jpg" alt="Una historia 3D imaginaria de Hugging Face" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-211"></a>
### Case 211: [Claude para Chrome dentro de JS Paint](https://x.com/BtwIUseSystemd/status/2105861662112923849) (por [@BtwIUseSystemd](https://x.com/BtwIUseSystemd))

**Da al agente de navegador una tarea de dibujo limitada a las herramientas de la aplicación.**

El autor pide a Claude para Chrome que dibuje una persona usando solo herramientas de JS Paint y comparte la imagen. La interacción con el navegador y la aplicación de dibujo son partes explícitas de la tarea.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e69474350e9718d0262f34d4.png" alt="Claude para Chrome dentro de JS Paint" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-212"></a>
### Case 212: [Un pelícano en bicicleta en SVG estático](https://x.com/olddonkeyblog/status/2105842745189556672) (por [@olddonkeyblog](https://x.com/olddonkeyblog))

**Usa una petición de SVG autónomo para probar un dibujo estático detallado.**

El creador pide un único SVG autónomo de un pelícano en bicicleta y comparte la imagen estática. Es una tarea distinta de los ejemplos de paseo animado.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5e242c0f805748542c9f5f0c.jpg" alt="Un pelícano en bicicleta en SVG estático" width="760">

Type: Demo | Date: 2026-10-02

---

<a id="case-213"></a>
### Case 213: [BlockBench MCP con una habilidad de Minecraft](https://x.com/TOPSTR1X/status/2105839618872738138) (por [@TOPSTR1X](https://x.com/TOPSTR1X))

**Proporciona una herramienta de modelado y una habilidad de estilo al generar un personaje de juego.**

El autor aporta BlockBench MCP y una habilidad personalizada de modelado y color de Minecraft, y comparte el personaje obtenido. Las herramientas y las pautas de estilo son entradas explícitas del flujo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a17d81dfbc7544f67c0178cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4ff4dab909e7d98f53ee7a32.jpg" alt="BlockBench MCP con una habilidad de Minecraft" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-214"></a>
### Case 214: [Dig Dug en un único archivo HTML](https://x.com/imjustnewatai/status/2105831117677084841) (por [@imjustnewatai](https://x.com/imjustnewatai))

**Define un solo archivo HTML como entrega al recrear un juego de navegador compacto.**

El creador pide una recreación de Dig Dug en un único archivo HTML y comparte la grabación del juego. El post describe la construcción como resultado de un prompt.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7674d4f1b7ba8eab003edff4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/438f4e89fb1925a4fb36d3e5.jpg" alt="Dig Dug en un único archivo HTML" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-215"></a>
### Case 215: [Un pulpo mecánico en SVG](https://x.com/SEO/status/2105812236774297943) (por [@SEO](https://x.com/SEO))

**Examina detalle y movimiento del diseño SVG con una criatura mecánica.**

El autor comparte un pulpo SVG animado con detalles mecánicos. La grabación proporciona un ejemplo concreto de diseño vectorial centrado en pequeñas piezas móviles.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ec5c702edd3fdadc05722c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbcc433f0a275f0e384cbf2f.jpg" alt="Un pulpo mecánico en SVG" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-216"></a>
### Case 216: [Humanity Walks por distintos estilos artísticos](https://x.com/l_mejiaC/status/2105801379956850793) (por [@l_mejiaC](https://x.com/l_mejiaC))

**Lleva una figura recurrente por una secuencia de estilos visuales históricos.**

El creador original presenta un paseo continuo por veinte paneles artísticos durante unos setenta y cuatro segundos y menciona música programada. Cada límite transforma el personaje y la escena en otro estilo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/355568bba0c9ff28575e04b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b71cfca9259ec002c246e377.jpg" alt="Humanity Walks por distintos estilos artísticos" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-217"></a>
### Case 217: [Una escena libre de agujero negro](https://x.com/rohit3a/status/2105786053412208835) (por [@rohit3a](https://x.com/rohit3a))

**Explora una visualización de agujero negro mediante un encargo creativo abierto.**

El creador pregunta qué haría el modelo para impresionarle y comparte una escena de agujero negro. La tarea es una exploración visual libre, no una construcción de interfaz prescrita.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/896a05493d7c8e1f8f430d17.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7a0adf969d1f472df46ddce1.jpg" alt="Una escena libre de agujero negro" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-218"></a>
### Case 218: [Comparación de animaciones de medusas aurorales](https://x.com/SPAC89/status/2105783511433318451) (por [@SPAC89](https://x.com/SPAC89))

**Compara deformación y movimiento en dos animaciones de medusas.**

El autor compara Fable XHigh y GPT Sol Ultra en una animación de medusa auroral y comenta uso de cuota. Los resultados proceden de distintos niveles de suscripción.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e57a76eaf8ed239783bce290.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/547871b06436d28a12435b40.jpg" alt="Comparación de animaciones de medusas aurorales" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-219"></a>
### Case 219: [Un SVG de Nintendo Switch con encaje y arranque](https://x.com/ishuagra02/status/2105779174921359470) (por [@ishuagra02](https://x.com/ishuagra02))

**Combina movimiento de mandos y una secuencia de arranque en una animación SVG.**

El creador comparte un SVG de Nintendo Switch cuyos mandos encajan antes de animarse el logotipo de arranque. Declara un tiempo de un minuto y treinta y nueve segundos y un coste de 1,34 dólares para esa ejecución.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/423cd224b690b962d86df6a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8cb691f2e876fca6c8323d34.jpg" alt="Un SVG de Nintendo Switch con encaje y arranque" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-220"></a>
### Case 220: [La escena 3D interactiva The Loom](https://x.com/Mr_Salio/status/2105774088492916757) (por [@Mr_Salio](https://x.com/Mr_Salio))

**Explora paisaje y edificios como una sola página 3D interactiva.**

El autor presenta The Loom, una escena interactiva con edificios y paisaje. La grabación proporciona el resultado concreto de la página de su prueba.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a0fbc7f4427c05e1b20875dc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/aca91baef7a93139d084e4e6.jpg" alt="La escena 3D interactiva The Loom" width="760"></a>

Type: Demo | Date: 2026-10-01

---

<a id="case-221"></a>
### Case 221: [Muestras animadas de pagoda sakura](https://x.com/mesmerlord/status/2105758042830549235) (por [@mesmerlord](https://x.com/mesmerlord))

**Compara foco visual y sincronización entre escenas producidas con el mismo prompt.**

El autor comparte dos primeras muestras de pagoda sakura en movimiento con el mismo prompt y comenta enfoque y sincronización con el ritmo. Las observaciones describen sus resultados específicos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/dc4c3e5875e829f8b568a67b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8fc402eeea381a9519146e4.jpg" alt="Muestras animadas de pagoda sakura" width="760"></a>

Type: Evaluation | Date: 2026-10-01

---

<a id="case-222"></a>
### Case 222: [Un paisaje más limpio pero con menor profundidad](https://x.com/eviljoker88/status/2105755840175034447) (por [@eviljoker88](https://x.com/eviljoker88))

**Conserva críticas estéticas negativas al comparar escenas generadas.**

El autor muestra escenas japonesas lado a lado y prefiere la profundidad del resultado de Opus, aunque el otro parezca más limpio.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0f0e14c7725846928d67bbb6.jpg" alt="Un paisaje más limpio pero con menor profundidad" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-223"></a>
### Case 223: [Resultados mixtos de una escena japonesa](https://x.com/eviljoker88/status/2105755408342126936) (por [@eviljoker88](https://x.com/eviljoker88))

**Registra opiniones mixtas en vez de declarar un ganador claro en la primera comparación.**

El autor comparte una primera comparación de escenas japonesas y califica los resultados de mixtos. La imagen conserva las salidas concretas que motivan esa valoración estética.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/392cb1ddc17b777dd8018cfd.jpg" alt="Resultados mixtos de una escena japonesa" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-224"></a>
### Case 224: [Comparaciones de mandos SVG](https://x.com/notjazii/status/2105751542498464169) (por [@notjazii](https://x.com/notjazii))

**Compara dibujos de mandos antes y después bajo una tarea visual similar.**

El autor comparte resultados SVG de mandos antes y después en una imagen comparativa. El caso trata de los cambios visibles de dibujo y presentación, no de una clasificación general de modelos.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/17459f88ec7684afc5b33a02.jpg" alt="Comparaciones de mandos SVG" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-225"></a>
### Case 225: [Una escena de dispositivo industrial](https://x.com/RayaneRachid_/status/2105744517735354410) (por [@RayaneRachid_](https://x.com/RayaneRachid_))

**Usa un dispositivo mecánico como tarea focalizada de diseño de escena 3D.**

El creador comparte una escena 3D de un dispositivo industrial y la describe como su mejor resultado de una sola generación. La imagen ofrece una referencia concreta de composición mecánica.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/589373a493d90e11ce8abbb9.jpg" alt="Una escena de dispositivo industrial" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-226"></a>
### Case 226: [Reconstrucción de una criatura gigante con caparazón y branquias](https://x.com/Josh67Joshua/status/2105739832563769697) (por [@Josh67Joshua](https://x.com/Josh67Joshua))

**Explora una reconstrucción en dos prompts con una descripción de criatura concreta.**

El autor comparte un dibujo de una criatura gigante con caparazón y branquias y relata haberlo conseguido con dos prompts. La imagen proporciona el resultado visible de la tarea de diseño.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/446fdbef8a03b236ecc7b383.jpg" alt="Reconstrucción de una criatura gigante con caparazón y branquias" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-227"></a>
### Case 227: [Un mando de GameCube con dos prompts](https://x.com/marmaduke091/status/2105735266032095349) (por [@marmaduke091](https://x.com/marmaduke091))

**Examina un dibujo de dos prompts con un mando familiar.**

El autor comparte un dibujo de mando de GameCube y dice haber usado dos prompts. Esta imagen estática es distinta de las demostraciones de Xbox y otros mandos.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e8dc05610d167f3a15b550af.jpg" alt="Un mando de GameCube con dos prompts" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-228"></a>
### Case 228: [Una captura editada para publicar en X](https://x.com/chetaslua/status/2105733677003292983) (por [@chetaslua](https://x.com/chetaslua))

**Examina cómo un asistente adapta una captura para una publicación social.**

El creador comparte una captura editada para X y afirma que el asistente hizo el cambio sin una petición explícita. La imagen adjunta es el resultado visible.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0cc409b9d0aa3771484a3c71.jpg" alt="Una captura editada para publicar en X" width="760">

Type: Demo | Date: 2026-10-01

---

<a id="case-229"></a>
### Case 229: [Un paisaje sakura en vóxeles antes y después](https://x.com/kdnbmb/status/2105704791049412755) (por [@kdnbmb](https://x.com/kdnbmb))

**Compara resultados sucesivos de una escena vóxel sobre el mismo tema visual.**

Quien publica comparte dos versiones de una isla sakura en vóxeles. La imagen comparativa registra diferencias de diseño visibles entre antes y después.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4138fd1978c438d2d9e8661a.jpg" alt="Un paisaje sakura en vóxeles antes y después" width="760">

Type: Evaluation | Date: 2026-10-01

---

<a id="case-230"></a>
### Case 230: [El prototipo de interfaz textil SHADERKIN](https://x.com/mszzz0011/status/2106025576972853642) (por [@mszzz0011](https://x.com/mszzz0011))

**Explora efectos de tela y controles ajustables en un prototipo de interfaz.**

El autor comparte un prototipo SHADERKIN con efectos de tela y controles de parámetros, descrito como generado de una sola vez. La grabación muestra la interfaz y los movimientos obtenidos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/e4475b58a7c623137018178b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b7f6e02a01706ce70452b0d.jpg" alt="El prototipo de interfaz textil SHADERKIN" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-231"></a>
### Case 231: [Una animación compartida de interfaz con reloj dorado](https://x.com/AISuperDomain/status/2106396754539360272) (por [@AISuperDomain](https://x.com/AISuperDomain))

**Usa una animación de reloj como referencia de composición de interfaz.**

Quien publica presenta una animación frontend con un reloj dorado. El clip ofrece una referencia compartida para examinar composición, motivo del reloj y presentación visual animada.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c60a3556d2b2ddaa5f509c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/676bb647541546a0ad366f0e.jpg" alt="Una animación compartida de interfaz con reloj dorado" width="760"></a>

Type: Demo | Date: 2026-10-03

---

<a id="case-232"></a>
### Case 232: [La narración Before There Was Anything](https://x.com/crowqnt/status/2106146218846081435) (por [@crowqnt](https://x.com/crowqnt))

**Explora una historia cósmica y humana mediante un film animado compartido.**

Quien publica comparte Before There Was Anything, un vídeo narrativo sobre el cosmos y la humanidad. El film se conserva como ejemplo compartido de narración visual.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1245c13e338b1c01ae3f4dec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/71ef97e74c4d137730d81482.jpg" alt="La narración Before There Was Anything" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-233"></a>
### Case 233: [Un vórtice compartido de partículas azules](https://x.com/AISuperDomain/status/2105846981776003107) (por [@AISuperDomain](https://x.com/AISuperDomain))

**Examina movimiento y composición en una visualización compartida de vórtice.**

Quien publica comparte un vórtice animado de partículas azules. El clip es un ejemplo concreto compartido para examinar movimiento de partículas, estructura visual y composición.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/47741249784f7aff66778321.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5df983335216889dea8bc537.jpg" alt="Un vórtice compartido de partículas azules" width="760"></a>

Type: Demo | Date: 2026-10-02

---

<a id="case-234"></a>
### Case 234: [Una interfaz de varios paneles tras dos revisiones](https://x.com/ZorroOfMorocco/status/2106547078235095485) (por [@ZorroOfMorocco](https://x.com/ZorroOfMorocco))

**Refina una interfaz mediante ciclos de revisión en lugar de detenerte en la primera salida.**

El autor comparte una interfaz terminada de varios paneles y relata unas tres horas de trabajo con dos revisiones. La captura muestra el diseño visual final.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/de20f5a329023a9c4b0b93e7.jpg" alt="Una interfaz de varios paneles tras dos revisiones" width="760">

Type: Demo | Date: 2026-10-04

---

<a id="case-235"></a>
### Case 235: [Animales apilados en una escena renderizada](https://x.com/legit_api/status/2117237103289315574) (por [@legit_api](https://x.com/legit_api))

**Examina cómo una composición estática equilibra varios personajes y materiales.**

El post comparte una escena de oso, panda y oso polar apilados, acredita a yuruzuu en Discord y declara una ejecución de veintiún minutos. El post público se conserva como fuente visual compartida.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bc84af268896d8bb1758a934.jpg" alt="Animales apilados en una escena renderizada" width="760">

Type: Demo | Date: 2026-11-02

---

<a id="case-236"></a>
### Case 236: [Cuatro intentos de RPG de mundo abierto comparados](https://x.com/noclipepe/status/2117222592536789149) (por [@noclipepe](https://x.com/noclipepe))

**Compara presentación, combate y colisiones bajo la misma tarea creativa de juego.**

El creador presenta cuatro RPG de un prompt etiquetados como Fable 5.5, GPT-6.2 Astra, Opus 5.5 y Fable 5.1. Comenta diferencias de iluminación, combate, inventario, colisiones y un personaje que queda atascado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/902f659bd556eb6d972125d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ef4071ff1f89636b5a170bcb.jpg" alt="Cuatro intentos de RPG de mundo abierto comparados" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-237"></a>
### Case 237: [Dos clips de animación frontend comparados](https://x.com/leo114119/status/2117209849842761983) (por [@leo114119](https://x.com/leo114119))

**Compara diseño de escena y detalle visual viendo juntos los clips animados.**

El post yuxtapone animaciones programadas con etiquetas Astra y Fable y se centra en detalles y diseño del guion. Acredita expresamente a @chetaslua por la animación de Fable.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3b96cdfd122543f970f3a183.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0c7aeb3c3156cce1a407b992.jpg" alt="Dos clips de animación frontend comparados" width="760"></a>

Type: Evaluation | Date: 2026-11-02

---

<a id="case-238"></a>
### Case 238: [Un film de robot cubierto de musgo generado con código](https://x.com/chetaslua/status/2117169796290916732) (por [@chetaslua](https://x.com/chetaslua))

**Explora una escena cinematográfica completa programada a partir de un encargo de animación.**

El creador comparte una animación de bosque y robot y la describe como un film programado de una sola generación. El post remite al prompt de una captura y compara el resultado con otros intentos.

Una publicación adicional muestra una ejecución de control de Opus 5.5 descrita por separado. [@AnikaCodes](https://x.com/AnikaCodes) · [Trabajo relacionado](https://x.com/AnikaCodes/status/2117222374642946297)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1719bb6df936cf88ea6c137a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a97bd6e101d45bc7e1c5f7a8.jpg" alt="Un film de robot cubierto de musgo generado con código" width="760"></a></td><td valign="top"><p>Una publicación adicional muestra una ejecución de control de Opus 5.5 descrita por separado.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/fb66f964af405e36c6993f37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/679a823fdecdc62be6ab781a.jpg" alt="Un film de robot cubierto de musgo generado con código" width="760"></a></td></tr></table>

Type: Demo | Date: 2026-11-02

---

<a id="case-239"></a>
### Case 239: [Una simulación de puerto de contenedores revisitada](https://x.com/anxuanng/status/2117124831279972812) (por [@anxuanng](https://x.com/anxuanng))

**Retoma una escena anterior conservando el contexto del proyecto para compararla visualmente.**

El autor publica otra escena de puerto de contenedores y cita su simulación anterior de Blender y Three.js, con grúas, barcos, vehículos y contenedores modelados para un entorno similar a un juego de estrategia.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/2fda951603d33af4e44d5fc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1d539c3c966ccc4c6929ba5d.jpg" alt="Una simulación de puerto de contenedores revisitada" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-240"></a>
### Case 240: [Una escena de plataforma aeroportuaria revisitada](https://x.com/anxuanng/status/2117096574878921119) (por [@anxuanng](https://x.com/anxuanng))

**Compara una escena de aeropuerto revisada con el proyecto y el flujo de recursos anteriores.**

El autor vuelve a una escena de plataforma aeroportuaria, cita su simulación anterior de Blender y Three.js y muestra nuevas imágenes de aviones, vehículos de servicio e infraestructura de terminal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3bd8a6295419d5189e2a0c39.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c953cb8fe287d88a42f4de7.jpg" alt="Una escena de plataforma aeroportuaria revisitada" width="760"></a>

Type: Demo | Date: 2026-11-02

---

<a id="case-241"></a>
### Case 241: [Un pelícano en bicicleta por mundos 3D abstractos](https://x.com/xiax0603/status/2116960224829665543) (por [@xiax0603](https://x.com/xiax0603))

**Examina transiciones entre entornos espaciales mediante un sujeto en bicicleta.**

El post muestra una animación de pelícano y bicicleta que atraviesa fragmentos geométricos y un entorno digital abstracto antes de alejarse a través de un ojo. La secuencia ofrece una demostración distinta de transiciones de escena.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e67084313c83b632c83932d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8e684cb9894f71707d522100.jpg" alt="Un pelícano en bicicleta por mundos 3D abstractos" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-242"></a>
### Case 242: [Una escena de velero histórico](https://x.com/abhinavflac/status/2116945827738665060) (por [@abhinavflac](https://x.com/abhinavflac))

**Examina agua, iluminación y composición ambiental en una escena de barco.**

El post comparte una escena de velero histórico y la describe como resultado interactivo sin ejemplos previos. La grabación ofrece una muestra visual concreta de la embarcación y el agua circundante.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9a500487b536db8173b83e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8083bd55fe8299ddb0399d9b.jpg" alt="Una escena de velero histórico" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-243"></a>
### Case 243: [Comparaciones de ciclismo y marcha con Carbon](https://x.com/AI_Screening/status/2116934172757660014) (por [@AI_Screening](https://x.com/AI_Screening))

**Compara movimiento de personajes y construcción de escenas mediante resultados emparejados.**

El autor reúne ejemplos de ciclistas y cebras etiquetados como Fable y Carbon en un vídeo compuesto. Describe los checkpoints como cercanos; los pares de imágenes ofrecen muestras concretas de movimiento.

La comparación anterior e independiente de ciclistas se incluye junto con el montaje compuesto. [@AI_Screening](https://x.com/AI_Screening) · [Trabajo relacionado](https://x.com/AI_Screening/status/2114380876415180963)

<table><tr><td valign="top"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/34ce8cd09717e765e8669306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/be5e4bce9526b63db3f75d49.jpg" alt="Comparaciones de ciclismo y marcha con Carbon" width="760"></a></td><td valign="top"><p>La comparación anterior e independiente de ciclistas se incluye junto con el montaje compuesto.</p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/bdfda2a7a784f201511128e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f398216f0483e9aaf1da8f85.jpg" alt="Comparaciones de ciclismo y marcha con Carbon" width="760"></a></td></tr></table>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-244"></a>
### Case 244: [Presentación de una botella de refresco](https://x.com/abhinavflac/status/2116919086521499730) (por [@abhinavflac](https://x.com/abhinavflac))

**Examina materiales, forma y presentación mediante un clip breve de renderizado de producto.**

El post muestra una botella de refresco y la describe como salida de enrutamiento de una sola generación. Se conserva el clip visible sin adoptar el nombre de marca incoherente del texto.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6fb195b6c959b741bbba6bff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b8e3b156507ebe1397f4acf5.jpg" alt="Presentación de una botella de refresco" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-245"></a>
### Case 245: [Movimiento de pelícanos comparado con Astra](https://x.com/Octoberry/status/2116918967558095131) (por [@Octoberry](https://x.com/Octoberry))

**Mira los clips emparejados para comparar realismo, colores y movimiento.**

Quien publica yuxtapone escenas de pelícanos etiquetadas como Fable y Astra y comenta su realismo y colores. La grabación comparativa mantiene juntos ambos tratamientos visuales.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8ea3b0ac90c46aa8df91435c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f8e883dfa17d32c1490d2a06.jpg" alt="Movimiento de pelícanos comparado con Astra" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-246"></a>
### Case 246: [Un brief de motion design para animaciones programadas](https://x.com/Mikadzyki_NFT/status/2116913089308131595) (por [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT))

**Parte de un brief concreto para pedir títulos animados o introducciones de producto.**

El post comparte una captura de un brief de motion design para introducciones, logotipos animados, títulos y escenas 3D, y propone aplicarlo con Claude. La imagen fuente conserva las instrucciones.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c8dc35a75c2d69b08167c4b2.jpg" alt="Un brief de motion design para animaciones programadas" width="760">

Type: Tutorial | Date: 2026-11-01

---

<a id="case-247"></a>
### Case 247: [Un retrato vóxel desde una referencia fotográfica](https://x.com/chetaslua/status/2116912822806520027) (por [@chetaslua](https://x.com/chetaslua))

**Examina cómo un retrato vóxel conserva rasgos reconocibles de la foto de referencia.**

El creador combina una fotografía de Sam Altman con un retrato vóxel y describe una sola generación. La imagen lado a lado aporta la referencia y su interpretación juntas.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eea0f98c5b8adf315254357d.jpg" alt="Un retrato vóxel desde una referencia fotográfica" width="760">

Type: Demo | Date: 2026-11-01

---

<a id="case-248"></a>
### Case 248: [Pelícanos voladores comparados con Opus](https://x.com/leo114119/status/2116901575490929109) (por [@leo114119](https://x.com/leo114119))

**Compara composición y animación mediante una disposición lúdica de objetos.**

El post apila clips etiquetados Fable y Opus para una escena de bicicleta sobre un pelícano volador. El montaje acredita a @notjazii por el clip de Fable y mantiene visibles ambos tratamientos.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/cbf26990ce0160a0162ead5b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/1c7ac3995ff80676690c1821.jpg" alt="Pelícanos voladores comparados con Opus" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-249"></a>
### Case 249: [La escena web de pelícano Morning Ride](https://x.com/leo114119/status/2116893571739775220) (por [@leo114119](https://x.com/leo114119))

**Examina detalles del personaje y presentación de página en una escena de ciclismo costero.**

El autor comparte un pelícano ciclista 3D dentro de una página Morning Ride y destaca plumaje, patas, detalles de bicicleta y fondo costero.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b55570e6a6f3164a9b73e097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/70e98e614f9e34f7cb5e885f.jpg" alt="La escena web de pelícano Morning Ride" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-250"></a>
### Case 250: [Un mismo prompt con estilos diferentes](https://x.com/notjazii/status/2116893197939224714) (por [@notjazii](https://x.com/notjazii))

**Deja que cada modelo elija su estilo y después compara la composición resultante.**

El autor dice que probó ambos modelos con el mismo prompt y permitió que eligieran su estilo visual. El vídeo yuxtapone composiciones y niveles de detalle diferentes.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/337c953505b934eb3efe3026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f9cf0077f93079072db88a97.jpg" alt="Un mismo prompt con estilos diferentes" width="760"></a>

Type: Evaluation | Date: 2026-11-01

---

<a id="case-251"></a>
### Case 251: [Una composición de pelícano, bicicleta y caballo](https://x.com/abhinavflac/status/2116881397986288017) (por [@abhinavflac](https://x.com/abhinavflac))

**Prueba cómo una animación organiza varios sujetos que interactúan en la misma escena.**

El post muestra un pelícano volando con una bicicleta mientras un caballo corre debajo. El clip ofrece una muestra concreta de esa composición inusual de varios objetos y su movimiento.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/0504d9fae95f901cb5a7a0b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4c41a8c590ff3cced720fa3f.jpg" alt="Una composición de pelícano, bicicleta y caballo" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-252"></a>
### Case 252: [Una escena isométrica inspirada en un tuit de referencia](https://x.com/chetaslua/status/2116878661035106515) (por [@chetaslua](https://x.com/chetaslua))

**Guía una escena nueva con una publicación de referencia en vez de rehacer un ejemplo genérico.**

El creador dice que usó solo un tuit citado de Post Humans como referencia y comparte la escena isométrica resultante. El clip muestra una composición de tipo granja con un control de estación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/8fc030a325be1e12a93985c1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/087ed1d1f018c09b2799296a.jpg" alt="Una escena isométrica inspirada en un tuit de referencia" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-253"></a>
### Case 253: [Primeros planos mecánicos de una bicicleta con pelícano](https://x.com/NFT_Chen/status/2116869725703782507) (por [@NFT_Chen](https://x.com/NFT_Chen))

**Examina movimiento del plato, detalle de plumas y cámara alrededor de un sujeto ciclista.**

El post muestra primeros planos de un pelícano en bicicleta junto al agua. La grabación alterna entre mecánica de bicicleta, cabeza del ave y una vista más amplia del paseo costero.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/b6d2d126b2aeb9f3f9570afd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/a166c588d812d40d06fae7ad.jpg" alt="Primeros planos mecánicos de una bicicleta con pelícano" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-254"></a>
### Case 254: [Una bicicleta que monta un pelícano](https://x.com/notjazii/status/2116861637890379891) (por [@notjazii](https://x.com/notjazii))

**Invierte la relación habitual entre sujetos para explorar composición espacial.**

El creador comparte una animación de bicicleta sobre pelícano. El clip coloca la bicicleta encima de un ave voladora y varía la tarea conocida del pelícano montando una bicicleta.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ca15b0e0590d8cb6d8f17414.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d86986a058741892f33c2a1e.jpg" alt="Una bicicleta que monta un pelícano" width="760"></a>

Type: Demo | Date: 2026-11-01

---

<a id="case-255"></a>
### Case 255: [Estilos SVG de pelícano comparados con Carbon](https://x.com/leo114119/status/2116652334734332212) (por [@leo114119](https://x.com/leo114119))

**Compara realismo e ilustración sin convertir estéticas diferentes en una clasificación universal.**

El post reúne resultados de pelícano en bicicleta de Carbon y Fable. El autor contrapone estilo de cómic y tratamiento más realista, y señala que esa diferencia dificulta la comparación.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7126f7490639ef435ad3f8e0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6d83e5e28063bbe2c6107860.jpg" alt="Estilos SVG de pelícano comparados con Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-31

---

<a id="case-256"></a>
### Case 256: [Un pájaro azul de dibujos animados en bicicleta](https://x.com/birdabo/status/2116553049183560012) (por [@birdabo](https://x.com/birdabo))

**Examina un personaje de dibujos familiar dentro de una composición ciclista.**

El post muestra un pájaro azul de dibujos montando una bicicleta junto al agua, con el texto Fable 5.5 Max. La imagen se conserva como muestra visual estática concreta.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/4b61e3c3bed85e7bb63284b8.jpg" alt="Un pájaro azul de dibujos animados en bicicleta" width="760">

Type: Demo | Date: 2026-10-31

---

<a id="case-257"></a>
### Case 257: [Captura de pelícano ciclista en una carretera forestal](https://x.com/leo114119/status/2116154940364374269) (por [@leo114119](https://x.com/leo114119))

**Examina plumas, patas y geometría de la bicicleta en una escena renderizada en navegador.**

Quien publica muestra una captura de navegador de un pelícano en bicicleta por una carretera forestal y destaca textura de plumas, patas y detalles de la bicicleta.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/78c8b16b4f41dfc594a08147.jpg" alt="Captura de pelícano ciclista en una carretera forestal" width="760">

Type: Demo | Date: 2026-10-30

---

<a id="case-258"></a>
### Case 258: [Combate de figuras de palo comparado con Carbon](https://x.com/leo114119/status/2116084152986656933) (por [@leo114119](https://x.com/leo114119))

**Compara coreografía de combate y movimiento en muestras animadas emparejadas.**

La grabación comparativa lleva las etiquetas Fable 5.1 High y Carbon. El autor comenta la calidad relativa de la animación de combate de figuras de palo.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/116e9cf73951a3cc14c7fd26.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12a35f0f8829bbc3ab246d10.jpg" alt="Combate de figuras de palo comparado con Carbon" width="760"></a>

Type: Evaluation | Date: 2026-10-30

---

<a id="case-259"></a>
### Case 259: [Una referencia SVG de pelícano de pruebas tempranas](https://x.com/ChrisGPT/status/2115872567122608591) (por [@ChrisGPT](https://x.com/ChrisGPT))

**Conserva una referencia enlazada a su fuente para examinar estilo y geometría de bicicleta.**

Quien publica destaca una imagen de pelícano en bicicleta y cita un post de pruebas tempranas que acredita a kostikz en Discord. Se conservan la imagen y su cadena de atribución.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/431cb96b21edc9964ce0659f.jpg" alt="Una referencia SVG de pelícano de pruebas tempranas" width="760">

Type: Demo | Date: 2026-10-29

---

<a id="case-260"></a>
### Case 260: [Una referencia de pelícano en pruebas SVG entre modelos](https://x.com/AdamHoltererer/status/2115858542221492300) (por [@AdamHoltererer](https://x.com/AdamHoltererer))

**Mantén la referencia de Fable junto con el contexto de la prueba SVG.**

Quien publica añade una imagen de pelícano en bicicleta como referencia de Fable bajo su hilo de pruebas SVG de Mistral Large 4. Aporta así una imagen enlazada a su fuente para la inspección entre modelos.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/31b17f996d2e8b9bac8b2d57.jpg" alt="Una referencia de pelícano en pruebas SVG entre modelos" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-261"></a>
### Case 261: [Detalles de bicicletas SVG comparados con Carbon](https://x.com/insanekrishnaa/status/2115833723342250186) (por [@insanekrishnaa](https://x.com/insanekrishnaa))

**Compara elementos visuales concretos como cestas, fondos y texturas de plumas.**

El post compara imágenes de pelícanos en bicicleta de Fable y Carbon mediante cestas, detalle del fondo y plumas. Presenta una revisión visual específica, no un conjunto amplio de tareas.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/12e6ec3f93842782a3adc017.jpg" alt="Detalles de bicicletas SVG comparados con Carbon" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-262"></a>
### Case 262: [Un asentamiento en un cañón en 3D](https://x.com/Mr_Salio/status/2115813400915714177) (por [@Mr_Salio](https://x.com/Mr_Salio))

**Examina detalle ambiental y composición espacial en una escena de asentamiento.**

El post comparte un amplio asentamiento en un cañón y presenta la grabación como demostración de un nuevo checkpoint de Claude. El metraje muestra edificios, paisaje y composición de la escena.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7cc648562f9915df6383b86b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/41e5348bd8e8d57399a2720b.jpg" alt="Un asentamiento en un cañón en 3D" width="760"></a>

Type: Demo | Date: 2026-10-29

---

<a id="case-263"></a>
### Case 263: [Detalle de mandos comparado con Opus](https://x.com/notjazii/status/2115808169075351632) (por [@notjazii](https://x.com/notjazii))

**Examina forma, controles y detalle en dibujos emparejados de mandos.**

El autor publica juntos dibujos de mandos etiquetados como Fable y Opus y destaca el detalle de la versión superior. La imagen emparejada conserva la comparación.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/799809d6ec73abaf5f698721.png" alt="Detalle de mandos comparado con Opus" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-264"></a>
### Case 264: [Un flujo semanal de auditoría SEO de sitios](https://x.com/cleeeeeeeeement/status/2115488774423773267) (por [@cleeeeeeeeement](https://x.com/cleeeeeeeeement))

**Convierte un sitio en un plan SEO priorizado y un proceso recurrente de revisión de posiciones.**

El creador describe un sistema que recibe un sitio, identifica competidores y palabras clave y genera un plan SEO priorizado. Una grabación breve acompaña la descripción de seguimiento semanal de posiciones y ejecución.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/d0f8f00f6fd8085c885d94de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/ab070e7a94e89874d1199ca3.jpg" alt="Un flujo semanal de auditoría SEO de sitios" width="760"></a>

Type: Integration | Date: 2026-10-28

---

<a id="case-265"></a>
### Case 265: [Reutilizar recursos de Fable en motion design de Opus](https://x.com/chetaslua/status/2115145163542790170) (por [@chetaslua](https://x.com/chetaslua))

**Separa creación de recursos y montaje de motion design al combinar modelos y herramientas.**

El creador comparte motion design de Opus 5.5 para un Tesla Roadster con recursos que atribuye a Fable anteriormente. El flujo previo citado menciona Python en Blender, ElevenLabs y un vídeo de lanzamiento suministrado.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5618dd376ee55b4ee82fc0fd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/eece5cd2a213c0a512c114a1.jpg" alt="Reutilizar recursos de Fable en motion design de Opus" width="760"></a>

Type: Integration | Date: 2026-10-27

---

<a id="case-266"></a>
### Case 266: [Una aplicación de mandalas y formas geométricas](https://x.com/ZMinimalistYogi/status/2114600083165434189) (por [@ZMinimalistYogi](https://x.com/ZMinimalistYogi))

**Convierte una idea geométrica focalizada en una aplicación interactiva de exploración creativa.**

El creador relata tres horas de conversación con Fable 5.1 para construir una aplicación de mandalas, zomes, sólidos de Arquímedes y yantras geométricos de loto. Después la comparte en su sitio personal.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/5de8fc634a752f83622f8a13.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/3e57964d461878db96f139ac.jpg" alt="Una aplicación de mandalas y formas geométricas" width="760"></a>

Type: Demo | Date: 2026-10-26

---

<a id="case-267"></a>
### Case 267: [Un ciclista en bicicleta con Three.js](https://x.com/AI_Screening/status/2114266369248354357) (por [@AI_Screening](https://x.com/AI_Screening))

**Examina postura, geometría de la bicicleta y movimiento coordinado en una escena ciclista.**

El creador comparte un resultado de ciclista en bicicleta con Three.js. La grabación ofrece una muestra concreta de movimiento con un puente y un paisaje costero alrededor del ciclista.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7637bbffeefe623e04ef2f21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/7bcf0b58c603da7235a3a557.jpg" alt="Un ciclista en bicicleta con Three.js" width="760"></a>

Type: Demo | Date: 2026-10-25

---

<a id="case-268"></a>
### Case 268: [Instantánea de evaluación de FrontierCS 2](https://x.com/wenhaocha1/status/2115613415641354262) (por [@wenhaocha1](https://x.com/wenhaocha1))

**Usa un gráfico de evaluación enlazado a su fuente para comparar Fable 5.1 con otros modelos.**

El autor incorpora Fable 5.1 a un gráfico de tasas de aprobación de FrontierCS 2 y comparte los resultados declarados junto con los de otros modelos.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/f5cbd2078225f0413d733ee9.jpg" alt="Instantánea de evaluación de FrontierCS 2" width="760">

Type: Evaluation | Date: 2026-10-29

---

<a id="case-269"></a>
### Case 269: [Comparación de animaciones de cebra entre tres modelos](https://x.com/AI_Screening/status/2115849659797373038) (por [@AI_Screening](https://x.com/AI_Screening))

**Compara la tarea de una cebra al galope con los tres resultados etiquetados por modelo que se muestran juntos.**

El autor presenta una comparación de animaciones de cebra lado a lado, etiquetadas como Fable 5.5, Opus 5.5 y Gemini 4 Argon. La grabación compartida ofrece muestras concretas de la marcha en las tres salidas.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/c6eaeba4555c4bef54d626a5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-claude-fable-5/fable-5-5/full-2026-11-03/6b1da9a2967f99e299587299.jpg" alt="Comparación de animaciones de cebra entre tres modelos" width="760"></a>

Type: Evaluation | Date: 2026-10-29

---

<a id="case-270"></a>
### Case 270: [Criticar la legibilidad de textos japoneses largos](https://x.com/AM09_21/status/2106670042184356156) (por [@AM09_21](https://x.com/AM09_21))

**Pide al modelo que diagnostique problemas de legibilidad en prosa japonesa generada.**

El autor cuenta que preguntó por qué los textos japoneses largos de Opus resultan difíciles de leer. La respuesta señala sintaxis calcada del inglés, repetición y retoques superficiales, como ejemplo de un flujo concreto de crítica de textos.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-271"></a>
### Case 271: [Un PowerPoint técnico guiado por ejemplos](https://x.com/mt_moco/status/2106665038375522791) (por [@mt_moco](https://x.com/mt_moco))

**Proporciona ejemplos antes de pedir una presentación técnica.**

El autor relata que unos pocos ejemplos de presentaciones permitieron obtener un PowerPoint técnico utilizable. Su testimonio relaciona los prompts con ejemplos con una mejor estructura documental en una tarea de presentación específica.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-272"></a>
### Case 272: [Comparar la coherencia musical](https://x.com/AM09_21/status/2106573080214770011) (por [@AM09_21](https://x.com/AM09_21))

**Evalúa por separado los detalles locales y la coherencia global de una composición generada.**

El autor compara composiciones de modelos mediante notas, melodía y transiciones, diferenciando consistencia local y estructura musical global. El testimonio evalúa la calidad compositiva a partir de la escucha.

Type: Evaluation | Date: 2026-10-04

---

<a id="case-273"></a>
### Case 273: [Finalización prematura y diseños de menor calidad](https://x.com/johntitorIII/status/2106442876506747353) (por [@johntitorIII](https://x.com/johntitorIII))

**Comprueba los entregables frente a los requisitos antes de aceptar que un agente dé la tarea por terminada.**

El autor describe varios días de pruebas en los que tareas incompletas se marcaron como finalizadas y los diseños quedaron por debajo de otros modelos. El testimonio recoge finalización prematura y calidad de diseño como fallos prácticos.

Type: Limit | Date: 2026-10-03

---

<a id="case-274"></a>
### Case 274: [Un resultado artístico de calamar que causa incomodidad](https://x.com/hanawo_neki/status/2106271036094415186) (por [@hanawo_neki](https://x.com/hanawo_neki))

**Especifica preferencias estéticas cuando una petición artística abierta produce un estilo no deseado.**

El autor relata que pidió cualquier obra de arte sobre un calamar y recibió detalles densamente agrupados que le resultaron incómodos. El testimonio registra un desajuste estético dentro de una petición visual abierta.

Type: Limit | Date: 2026-10-03

---

<a id="case-275"></a>
### Case 275: [Motion design con estética de plano técnico](https://x.com/DavidayoAI/status/2106054662063325638) (por [@DavidayoAI](https://x.com/DavidayoAI))

**Usa una estética de plano técnico como dirección visual para una animación rápida.**

El autor relata que pidió una animación rápida y recibió un resultado de estilo plano técnico tras unos quince minutos. La obra completa aparece enlazada en YouTube.

[Trabajo relacionado](https://youtu.be/ZCvbrHkkUkE)

Type: Demo | Date: 2026-10-02

---

<a id="case-276"></a>
### Case 276: [Aves y peces en un paisaje sakura en vóxeles](https://x.com/xodud_rkd/status/2105876716472447046) (por [@xodud_rkd](https://x.com/xodud_rkd))

**Explora fauna animada dentro de un paisaje de vóxeles.**

El autor describe una escena sakura en vóxeles con aves en movimiento y peces en un estanque, y enlaza el artefacto interactivo. La página compartida es el resultado asociado a la escena.

[Trabajo relacionado](https://sakura-xodud.tyk-swe.chatgpt.site/)

Type: Demo | Date: 2026-10-02

---

<a id="case-277"></a>
### Case 277: [Un informe de fallo al generar personajes](https://x.com/doof1789559/status/2105874208458752227) (por [@doof1789559](https://x.com/doof1789559))

**Conserva experiencias negativas de personajes junto con las demostraciones visuales exitosas.**

El autor relata malos resultados al generar personajes y admite que su propio enfoque podría ser la causa. El post preserva una experiencia negativa concreta para evaluar tareas de personajes.

Type: Limit | Date: 2026-10-02

---

<a id="case-278"></a>
### Case 278: [Un SVG de pelícano con notas de tiempo y coste](https://x.com/AnonymerNutze12/status/2105740440385499295) (por [@AnonymerNutze12](https://x.com/AnonymerNutze12))

**Acompaña un dibujo de las observaciones de tiempo y coste del creador.**

El autor enlaza un artefacto HTML de pelícano SVG y declara tiempo y coste del intento. El artefacto enlazado es el resultado concreto al que se refiere el post.

[Trabajo relacionado](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

Type: Evaluation | Date: 2026-10-01

---

<a id="case-279"></a>
### Case 279: [Programación remota por móvil con enjambres Claude Code](https://x.com/beistnormie/status/2106546741000417781) (por [@beistnormie](https://x.com/beistnormie))

**Explora la supervisión remota de enjambres de agentes de programación desde un teléfono.**

El autor relata programación remota con enjambres de Claude Code desde el móvil mientras viajaba. El post aporta una experiencia personal de flujo de trabajo, no un tutorial de proyecto ni una guía de implementación.

Type: Integration | Date: 2026-10-04

---

<a id="acknowledge"></a>
## 🙏 Agradecimientos

Este repositorio fue inspirado por los creadores, desarrolladores, equipos de benchmarks y comunidades que compartieron publicamente casos reales de uso de Claude Fable 5.

[@AlicanKiraz0](https://x.com/AlicanKiraz0), [@coldopn](https://x.com/coldopn), [@deveshcodes_](https://x.com/deveshcodes_), [@intheworldofai](https://x.com/intheworldofai), [@jsnnsa](https://x.com/jsnnsa), [@ryanrhughes](https://x.com/ryanrhughes), [@JJEnglert](https://x.com/JJEnglert), [@ayushagarwal](https://x.com/ayushagarwal), [@ai_for_success](https://x.com/ai_for_success), [@kieradev](https://x.com/kieradev), [@vikvang1](https://x.com/vikvang1), [@ydamitcodes](https://x.com/ydamitcodes), [@ecomchasedimond](https://x.com/ecomchasedimond), [@quanghuynt14](https://x.com/quanghuynt14), [@scottstts](https://x.com/scottstts), [@tetumemo](https://x.com/tetumemo), [@AndrewCurran_](https://x.com/AndrewCurran_), [@manaltdan](https://x.com/manaltdan), [@naoyafujiwara](https://x.com/naoyafujiwara), [@AI_masaou](https://x.com/AI_masaou), [@Truunik](https://x.com/Truunik), [@Voxyz_ai](https://x.com/Voxyz_ai), [@aianimesyokunin](https://x.com/aianimesyokunin), [@bielzinn](https://x.com/bielzinn), [@meta_alchemist](https://x.com/meta_alchemist), [@oikon48](https://x.com/oikon48), [@IBuzovskyi](https://x.com/IBuzovskyi), [@btibor91](https://x.com/btibor91), [@ctgptlb](https://x.com/ctgptlb), [@grapeot](https://x.com/grapeot), [@op7418](https://x.com/op7418), [@swarms_corp](https://x.com/swarms_corp), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@Conor_D_Dart](https://x.com/Conor_D_Dart), [@HKrackDev](https://x.com/HKrackDev), [@Hi_Noguchi](https://x.com/Hi_Noguchi), [@LechMazur](https://x.com/LechMazur), [@MTSlive](https://x.com/MTSlive), [@VaibhavSisinty](https://x.com/VaibhavSisinty), [@alliekmiller](https://x.com/alliekmiller), [@atomic_chat_hq](https://x.com/atomic_chat_hq), [@bcherny](https://x.com/bcherny), [@clairevo](https://x.com/clairevo), [@gabepereyra](https://x.com/gabepereyra), [@iScienceLuvr](https://x.com/iScienceLuvr), [@jerryjliu0](https://x.com/jerryjliu0), [@jumperz](https://x.com/jumperz), [@karpathy](https://x.com/karpathy), [@llama_index](https://x.com/llama_index), [@lucas_flatwhite](https://x.com/lucas_flatwhite), [@mark_k](https://x.com/mark_k), [@mercor_ai](https://x.com/mercor_ai), [@nicbstme](https://x.com/nicbstme), [@timhwang](https://x.com/timhwang), [@xw33bttv](https://x.com/xw33bttv), [@aashatwt](https://x.com/aashatwt), [@ozansihay](https://x.com/ozansihay), [@noisyb0y1](https://x.com/noisyb0y1), [@thebuggeddev](https://x.com/thebuggeddev), [@AiBattle_](https://x.com/AiBattle_), [@Pilgrim6938](https://x.com/Pilgrim6938), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@anilbpai](https://x.com/anilbpai), [@VincentLogic](https://x.com/VincentLogic), [@GratomicAi](https://x.com/GratomicAi), [@charliejhills](https://x.com/charliejhills), [@outsource_](https://x.com/outsource_), [@smtgpt](https://x.com/smtgpt), [@ClaudeDevs](https://x.com/ClaudeDevs), [@ClaudeCodeLog](https://x.com/ClaudeCodeLog), [@0x3b33](https://x.com/0x3b33), [@rileybrown](https://x.com/rileybrown), [@marclou](https://x.com/marclou), [@ProximalHQ](https://x.com/ProximalHQ), [@elliotarledge](https://x.com/elliotarledge), [@mikefutia](https://x.com/mikefutia), [@techhalla](https://x.com/techhalla), [@diblacksmith](https://x.com/diblacksmith), [@upstash](https://x.com/upstash), [@WolfBenchAI](https://x.com/WolfBenchAI), [@simonw](https://x.com/simonw), [@chetaslua](https://x.com/chetaslua), [@notjazii](https://x.com/notjazii), [@exploraX_](https://x.com/exploraX_), [@marmaduke091](https://x.com/marmaduke091), [@AI_Screening](https://x.com/AI_Screening), [@waveking1314](https://x.com/waveking1314), [@cherry_mx_reds](https://x.com/cherry_mx_reds), [@imjustnewatai](https://x.com/imjustnewatai), [@mesmerlord](https://x.com/mesmerlord), [@blueemi99](https://x.com/blueemi99), [@EMostaque](https://x.com/EMostaque), [@mindblown_ai](https://x.com/mindblown_ai), [@Chengzilhy](https://x.com/Chengzilhy), [@ishuagra02](https://x.com/ishuagra02), [@zAdrielsan](https://x.com/zAdrielsan), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@TurboNexic](https://x.com/TurboNexic), [@atomtanstudio](https://x.com/atomtanstudio), [@abhinavflac](https://x.com/abhinavflac), [@esrhengwu](https://x.com/esrhengwu), [@mickeysmith_jp](https://x.com/mickeysmith_jp), [@MozeTech](https://x.com/MozeTech), [@benchmark_lb900](https://x.com/benchmark_lb900), [@jesselaunz](https://x.com/jesselaunz), [@cocoloba_](https://x.com/cocoloba_), [@olddonkeyblog](https://x.com/olddonkeyblog), [@iowitz](https://x.com/iowitz), [@argofowl](https://x.com/argofowl), [@JaydenDavisNC](https://x.com/JaydenDavisNC), [@DAssetBuzz](https://x.com/DAssetBuzz), [@nemumusitocha](https://x.com/nemumusitocha), [@0xashtonx](https://x.com/0xashtonx), [@dropout_layer](https://x.com/dropout_layer), [@mathisbuilds](https://x.com/mathisbuilds), [@Saccc_c](https://x.com/Saccc_c), [@RobIW_dev](https://x.com/RobIW_dev), [@hungryturbo](https://x.com/hungryturbo), [@alannnfx](https://x.com/alannnfx), [@NFT_Chen](https://x.com/NFT_Chen), [@dpkostka](https://x.com/dpkostka), [@kiyoshi_shin](https://x.com/kiyoshi_shin), [@hanawo_neki](https://x.com/hanawo_neki), [@badboyfoxy](https://x.com/badboyfoxy), [@markbraincell](https://x.com/markbraincell), [@synthshareai](https://x.com/synthshareai), [@Layton_Gott](https://x.com/Layton_Gott), [@nroze22](https://x.com/nroze22), [@MinLiBuilds](https://x.com/MinLiBuilds), [@YanqingCheng](https://x.com/YanqingCheng), [@Kinzf2121](https://x.com/Kinzf2121), [@devteamdrew](https://x.com/devteamdrew), [@maciejkrupowies](https://x.com/maciejkrupowies), [@rohit3a](https://x.com/rohit3a), [@Noreply134882](https://x.com/Noreply134882), [@noclipepe](https://x.com/noclipepe), [@devswha](https://x.com/devswha), [@oalanicolas](https://x.com/oalanicolas), [@AndrewOnXYZ](https://x.com/AndrewOnXYZ), [@OnlyTerp](https://x.com/OnlyTerp), [@HashmathRzz](https://x.com/HashmathRzz), [@BoDy051](https://x.com/BoDy051), [@HelaliBillel](https://x.com/HelaliBillel), [@iancarscadden](https://x.com/iancarscadden), [@eviljoker88](https://x.com/eviljoker88), [@slimcat0101](https://x.com/slimcat0101), [@l_mejiaC](https://x.com/l_mejiaC), [@ziwenxu_](https://x.com/ziwenxu_), [@SPAC89](https://x.com/SPAC89), [@IgorGomezC](https://x.com/IgorGomezC), [@vikktorrrre](https://x.com/vikktorrrre), [@sdmat123](https://x.com/sdmat123), [@Mr_Salio](https://x.com/Mr_Salio), [@popat_kunj](https://x.com/popat_kunj), [@voltwake](https://x.com/voltwake), [@BtwIUseSystemd](https://x.com/BtwIUseSystemd), [@TOPSTR1X](https://x.com/TOPSTR1X), [@SEO](https://x.com/SEO), [@RayaneRachid_](https://x.com/RayaneRachid_), [@Josh67Joshua](https://x.com/Josh67Joshua), [@kdnbmb](https://x.com/kdnbmb), [@mszzz0011](https://x.com/mszzz0011), [@AISuperDomain](https://x.com/AISuperDomain), [@crowqnt](https://x.com/crowqnt), [@ZorroOfMorocco](https://x.com/ZorroOfMorocco), [@legit_api](https://x.com/legit_api), [@leo114119](https://x.com/leo114119), [@anxuanng](https://x.com/anxuanng), [@xiax0603](https://x.com/xiax0603), [@Octoberry](https://x.com/Octoberry), [@Mikadzyki_NFT](https://x.com/Mikadzyki_NFT), [@birdabo](https://x.com/birdabo), [@ChrisGPT](https://x.com/ChrisGPT), [@AdamHoltererer](https://x.com/AdamHoltererer), [@insanekrishnaa](https://x.com/insanekrishnaa), [@cleeeeeeeeement](https://x.com/cleeeeeeeeement), [@ZMinimalistYogi](https://x.com/ZMinimalistYogi), [@wenhaocha1](https://x.com/wenhaocha1), [@AM09_21](https://x.com/AM09_21), [@mt_moco](https://x.com/mt_moco), [@johntitorIII](https://x.com/johntitorIII), [@DavidayoAI](https://x.com/DavidayoAI), [@xodud_rkd](https://x.com/xodud_rkd), [@doof1789559](https://x.com/doof1789559), [@AnonymerNutze12](https://x.com/AnonymerNutze12), [@beistnormie](https://x.com/beistnormie), [@AnikaCodes](https://x.com/AnikaCodes)

*No podemos garantizar que cada caso este atribuido al creador original. Si algo necesita corregirse, contactanos y lo actualizaremos.*

Si tienes mas casos de uso interesantes para compartir, no dudes en abrir un issue o pull request y ayudar a expandir la biblioteca de casos de uso de Evolink.


[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/awesome-claude-fable-5&type=Date)](https://www.star-history.com/#EvoLinkAI/awesome-claude-fable-5&Date)
