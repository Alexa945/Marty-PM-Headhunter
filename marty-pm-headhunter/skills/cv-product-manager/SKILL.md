---
name: cv-product-manager
description: Audita, evalúa contra ofertas, adapta, sincroniza y (si no existe) crea CVs de Product Manager, Senior Product Manager, Technical Product Manager, AI Product Manager, Product Owner y Technical Product Owner para el mercado remoto de Latinoamérica, Estados Unidos y Canadá, en español o inglés, y genera el documento en HTML listo para exportar a PDF. Úsala siempre que aparezca un CV, currículum, resume o résumé en contexto de product management o product owner — tanto si piden revisarlo, "darle una vuelta", mejorar los bullets, ajustarlo o adaptarlo a una oferta concreta, traducirlo, como si pegan una oferta de PM/PO y preguntan si encaja, si cumplen los requisitos, si merece la pena aplicar o qué les falta. Actívala también cuando el agente Marty pida ajustar el CV para una oferta, cuando se quiera actualizar o igualar el CV maestro en inglés y en español, o cuando digan que no les llaman a entrevistas para puestos de producto. No usar para CVs de Product Designer / UX / UI (eso es cv-product-designer).
---

# CVs de Product Manager / Product Owner

## La idea que ordena todo lo demás

Un CV de PM tiene un solo trabajo: **demostrar impacto en negocio y producto** — métricas movidas, decisiones de priorización y trabajo con stakeholders. No es un resumen de vida laboral ni una lista de funciones.

Y ese trabajo se hace bajo dos filtros:

1. **Primero lo lee una máquina (el ATS)**, que lo convierte a texto plano y lo compara con el vocabulario de la oferta. Lo que no sobrevive a eso no llega a una persona.
2. **Después una persona lo escanea en unos 7 segundos.** En ese tiempo tiene que ver nivel, dominio y una prueba de impacto. Si no las ve, pasa al siguiente.

De ahí salen cinco consecuencias que gobiernan cada decisión de esta skill:

- **Resultados, no entregables.** "Lancé 12 features" o "gestioné el roadmap" describen actividad. Lo que cuenta es qué cambió gracias a eso: retención, conversión, tiempo, coste, adopción, riesgo evitado.
- **Alcance visible.** Usuarios, tamaño del equipo, número de squads, presupuesto, mercados. El alcance es lo que comunica el nivel (mid o Senior) en esos 7 segundos.
- **Vocabulario de la oferta para el ATS** — roadmap, discovery, OKRs, A/B testing, stakeholder management, Agile/Scrum, SQL… — pero **solo si hay experiencia real detrás**. Una keyword sin respaldo se cae en la primera entrevista.
- **Honestidad radical con las métricas.** Nunca inventar, estimar ni redondear hacia arriba (§ Métricas). En PM la tentación es mayor porque todo parece medible.
- **El perfil híbrido es un diferencial.** Una PM con base en otra disciplina (UX/Product Design, Psicología, ingeniería, un MBA…) es poco común: es un ángulo a destacar (en el resumen y en cómo se reencuadra la experiencia de diseño), no algo que esconder.

## Contexto de la persona usuaria

Antes de trabajar, lee `~/.claude/headhunter-pm/contexto.md`: ahí están residencia, permiso de trabajo, zona horaria, idiomas y dónde viven los CV maestros. Es la fuente de verdad; no la dupliques aquí ni la contradigas.

- **CV maestros** (en `~/.claude/cv/`): `…-MAESTRO-EN.docx` / `.pdf` y `…-MAESTRO-ES.docx` / `.pdf`. El `.docx` es la fuente editable; el `.pdf` es lo que lee el agente Marty. Para leer el contenido usa el PDF (Read sin el parámetro `pages`) o `textutil -convert txt -stdout <archivo.docx>`.
- **Nunca uses el CV de Product Designer** como base de un CV de PM.
- **Portfolio:** inclúyelo en la cabecera solo si `contexto.md` lo indica. Si no hay portfolio o se está rehaciendo, no lo añadas.

## Los maestros son fijos

Hay **un único CV maestro**, en dos idiomas con el mismo contenido. Es la versión larga: toda la experiencia, logros y métricas, aunque ocupe más de dos páginas.

- **Adaptar a una oferta nunca modifica el maestro.** Cada adaptación es un archivo nuevo.
- El maestro solo cambia en el **modo Sincronizar**, cuando la persona lo pide y con su aprobación.

Esto importa porque el maestro es la memoria de todo lo que es cierto. Si se recorta al adaptar, lo recortado se pierde para la siguiente oferta.

## Elige el modo antes de empezar

| Situación | Modo | Sigue |
|---|---|---|
| Hay CV y quieren mejorarlo (primer uso típico: auditar los maestros) | **Auditar** | `references/auditoria.md` |
| Hay CV + oferta, y la duda es si aplicar | **Evaluar encaje** | `references/evaluar-encaje.md` |
| Hay CV + oferta, y ya se decidió aplicar (o lo pide Marty) | **Adaptar** | `references/adaptar-oferta.md` |
| Cambió algo del maestro (trabajo nuevo, logro, certificación, corrección) o hay que igualar EN y ES | **Sincronizar** | `references/sincronizar.md` |
| No existe ningún CV de PM | **Crear** | `references/entrevista.md` → bullets → documento |

Si no está claro cuál piden, pregunta con una sola frase. Si te dan un CV existente, **audita antes de reescribir**: entender por qué falla evita cambiar lo que ya funcionaba.

**Crear no se usa** si ya existen los maestros: nunca generes un maestro nuevo a partir de otro CV (y menos del de diseño) sin que la persona lo pida.

---

## Niveles: solo mid y Senior

Esta skill trabaja con dos niveles. **No existe Lead** ni ningún nivel superior (Principal, Staff, Group PM, Head of Product, Director/VP, CPO): esas ofertas se descartan, no se adapta el CV hacia ellas.

La experiencia es siempre la misma y siempre real; lo que cambia es **qué se pone delante**:

| | Orientación **mid** | Orientación **Senior** |
|---|---|---|
| Qué destaca | Ejecución y entrega: backlog, sprints, lanzamientos, coordinación de equipos | Estrategia y propiedad: visión, roadmap, priorización con impacto en negocio, influencia sobre stakeholders |
| Resumen | "PM con X años entregando…" | "Senior PM que define y prioriza…" |
| Métricas | De funcionalidad o de equipo | De negocio: ingresos, retención, conversión, coste |
| Extensión | 1 página | 2 páginas como máximo |

**Los enfoques no son versiones.** Mismo maestro; lo que cambia según el título de la oferta es qué experiencia se pone delante y qué vocabulario se usa:

| Enfoque | Para ofertas de | Qué se pone delante | Vocabulario típico de la oferta |
|---|---|---|---|
| **PM** | Product Manager, Senior / Sr Product Manager | Estrategia, discovery, priorización, métricas de negocio | product strategy, discovery, roadmap, OKRs, growth |
| **PO** | Product Owner | Backlog, Scrum, refinamiento, delivery | backlog, user stories, sprint, acceptance criteria |
| **Technical PM** | Technical Product Manager | Trabajo directo con ingeniería y arquitectura: migraciones, re-platforming, integraciones, dependencias entre squads, decisiones técnicas con impacto en producto, construcción propia de producto | APIs, platform, integrations, architecture, system design, technical trade-offs |
| **AI PM** | AI Product Manager | Producto con IA: IA conversacional, iniciativas de IA, trabajo con AI Engineers y Data, métricas de efectividad del modelo o del bot, prototipado y construcción con herramientas de IA | LLMs, conversational AI, AI/ML, model evaluation, data, experimentation |
| **Technical PO** | Technical Product Owner | Backlog técnico: criterios de aceptación con ingeniería, dependencias, migraciones, deuda técnica | technical backlog, APIs, integrations, dependencies |

Los enfoques Technical y AI **solo reordenan y reformulan experiencia real**. Si la oferta pide profundidad técnica que no está en el maestro (programar en producción, diseñar APIs, entrenar modelos, SQL avanzado), eso va al grupo "no se tiene" del informe de palabras clave y se trata como posible hueco en Evaluar encaje — nunca se insinúa en el CV.

---

## Estructura del documento

Orden, de arriba abajo:

```
1. Cabecera        Nombre · Rol · Ciudad, País · Remote · zona horaria · Email · Teléfono · LinkedIn
2. Resumen         3 líneas como máximo.
3. Experiencia     Lo más reciente primero. 3-5 bullets en puestos recientes, 1-2 en los antiguos.
4. Habilidades     Agrupadas y honestas. Sin barras de nivel.
5. Formación       Casi al final.
6. Certificaciones Solo si las hay.
7. Idiomas         Con escala estándar.
```

**Cabecera orientada a remoto.** Quien selecciona tiene que ver en un segundo que la persona puede trabajar en su horario: *"Bogotá, Colombia · Remote · ET-aligned (UTC-5)"*. Teléfono en formato internacional (+57…) y LinkedIn como URL en texto visible, no como un "aquí" hipervinculado. Todo en el cuerpo del documento, nunca en el header/footer del PDF (muchos parsers los descartan).

**Nada de foto, edad, fecha de nacimiento, DNI, estado civil ni dirección postal** — tampoco en las versiones para Latinoamérica, aunque allí sea habitual. En EE. UU. y Canadá la foto puede descalificar por normativa antidiscriminación, y en remoto internacional esos datos no suman nada.

**Títulos de sección estándar**: *Summary / Experience / Skills / Education / Certifications / Languages* (en español: *Resumen / Experiencia / Habilidades / Formación / Certificaciones / Idiomas*). "Mi trayectoria" confunde al parser.

### El resumen

Tres líneas como máximo, y va sobre lo que aporta, no sobre lo que busca. Fórmula: **[rol y años] + [dominio] + [la evidencia más fuerte]**. Aquí vive también el ángulo híbrido si suma para la oferta.

> Senior Product Manager with [X]+ years across FinTech and SaaS. Owned the payments backlog of a digital bank across 3 squads; background in UX research that drives discovery-led prioritization.

(Ejemplo de forma, no de contenido: los años y cada dato salen del maestro, nunca de este ejemplo.)

Un "Objective" del tipo *"busco una posición que me permita crecer"* habla del candidato y no dice nada: se elimina siempre. Si el CV se adapta a una oferta, el resumen es lo primero que se reescribe.

### Bullets

Es el 80% del valor del CV. Lee `references/bullets.md` antes de redactar el primero. En corto: fórmula tipo Google — **"Logré X, medido por Y, haciendo Z"** — y si el bullet sobreviviría igual en el CV de cualquier otro PM de la empresa, no es un bullet, es una descripción del puesto.

### Experiencia de diseño

No se borra: se **reencuadra** hacia resultados de producto (decisiones, métricas, discovery, validación de hipótesis) y con menos bullets, para que el CV se lea como el de una PM con base en diseño y no como el de una diseñadora. Los procesos de diseño puros (wireframes, prototipos de alta fidelidad, design system) solo quedan si van unidos a un resultado de producto.

### Habilidades

Agrupadas, sin barras de nivel y solo con lo que se domina de verdad:
- **Product:** discovery, roadmapping, prioritization, MVP definition, product analytics…
- **Methods:** Scrum, Kanban, OKRs, Design Sprints…
- **Tools & Data:** Jira, Amplitude, GA4, SQL…

### Qué se elimina siempre

- Frases de "Objetivo" / "Objective".
- Bullets que describen el puesto en lugar de los resultados.
- Procesos genéricos sin resultado — de diseño (research, wireframes, Figma…) y de PM (gestión del backlog, reuniones con stakeholders, ceremonias Scrum, redacción de user stories, Jira/Confluence).
- "Responsible for…" / "Encargada de…" sin resultado.
- Soft skills sin evidencia ("proactiva", "líder", "results-oriented").
- Herramientas básicas (Office, Google Workspace).
- Experiencia de hace más de 10-15 años que no aporte al puesto.
- "References available upon request" / "Referencias disponibles a solicitud".

---

## Métricas: qué hacer cuando no las hay

**Nunca inventes, estimes ni redondees hacia arriba una métrica.** Un número inventado se cae en la primera entrevista y arrastra con él la credibilidad de todo lo demás. Si un número del maestro es aproximado ("~50%", "~100 profesionales"), se mantiene como aproximado.

Cuando no hay números de negocio, hay alternativas verificables, en orden de fuerza:

- **Escala** — el tamaño de lo que se tocó: *"…across 8 squads of 8–10 people"*.
- **Alcance y propiedad** — lo que solo esa persona sostenía: *"Owned the payments backlog for 9+ months during a PO vacancy"*.
- **Adopción** — la prueba de que el trabajo se usa: *"…achieving the 3% first-month usage target"*.
- **Decisión y consecuencia** — lo que dejó de pasar gracias a una decisión: *"Validated hypotheses with founders before development, avoiding build investment on unproven ideas"*.

Si la métrica existe pero es confidencial, exprésala en relativo sin romper el NDA: *"reduced onboarding time by half"* en vez del dato absoluto.

---

## ATS: lo que importa de verdad

- **PDF con texto seleccionable.** Un PDF que es una imagen es texto invisible para el ATS.
- **Una sola columna.** Dos columnas hacen que el parser mezcle líneas de ambas.
- **Cargo, empresa y fechas en la misma línea** (el mismo nodo de texto), para que no se desemparejen al extraer.
- **Sin tablas, cajas de texto, iconos ni barras de nivel** para contenido.
- **Contacto en el cuerpo**, no en header/footer.
- **Encabezados de sección estándar.**
- **Fechas coherentes** en todo el documento: *Jan 2022 – Present* en inglés, *ene. 2022 – actualidad* en español.
- **Nunca keywords ocultas** (texto blanco): los ATS las revelan y varios rechazan por ello.

**Prueba antes de entregar:** extrae el texto del PDF (Read del PDF, o copiar todo y pegar en texto plano). Lo que ves es lo que ve el ATS. Si sale desordenado o falta algo, el CV no está listo.

---

## Idioma y mercado

Lee `references/mercados-idiomas.md` cuando trabajes en un idioma o mercado concreto. En corto:

- **Español o inglés** según la oferta o la empresa. **Si es ambiguo, inglés.**
- Mercados: **Latinoamérica, Estados Unidos, Canadá y remoto internacional**. Se adaptan convenciones, no se traduce literal.
- **Español neutro latinoamericano**: sin giros de España ni localismos peruanos.
- En español, los **términos del oficio se mantienen en inglés** (stakeholders, roadmap, backlog, discovery…); los títulos de sección sí se traducen.
- Nivel de idioma con escala estándar (MCER o *Full professional proficiency*), nunca "avanzado" a secas.

---

## Generar el documento

1. Parte de `assets/cv-template.html` (una columna, ATS-safe, variables de tipografía y color arriba).
2. Tamaño de papel según mercado: **Letter** para EE. UU. y Canadá, **A4** para Latinoamérica (la plantilla trae ambos; cambia `@page size`).
3. Diseño contenido: **un color de acento y dos pesos tipográficos**. La contención comunica criterio; los adornos restan.
4. Genera el PDF:

```bash
python3 ~/.claude/skills/cv-product-manager/scripts/html_to_pdf.py cv.html cv.pdf
```

Usa Google Chrome en modo headless.

5. Pasa la prueba de copiar y pegar (§ ATS).

**Nombre del archivo** — rol, idioma y, en adaptaciones, empresa:

- Maestros: `Nombre-Apellido-Product-Manager-MAESTRO-EN.docx` / `…-ES.docx` (y sus `.pdf`).
- Adaptaciones: `Nombre-Apellido-Product-Manager-EN-Empresa.pdf`, `Nombre-Apellido-Product-Owner-ES-Empresa.pdf`, etc.

Guarda las adaptaciones en `~/.claude/cv/adaptaciones/` (créala si no existe) y **devuelve siempre el nombre exacto del archivo generado**, para anotarlo en la columna "CV usado" de `~/.claude/headhunter-pm/candidaturas.md`. La skill no añade filas a ese registro: eso se hace tras un envío real.

**Copia en Descargas, siempre.** Cada PDF generado (adaptación o CV nuevo) se copia también a `~/Downloads/` y se muestra en Finder (`open -R ~/Downloads/<archivo>.pdf`). `~/.claude` es una carpeta oculta y los enlaces a ella no se abren desde el chat: al entregar, di que el CV está en Descargas en vez de enlazar la ruta de `~/.claude`. El original se queda en `~/.claude/cv/adaptaciones/`. Si regeneras un PDF ya copiado, vuelve a copiarlo para que Descargas tenga la última versión.

---

## Fuera de alcance (v2)

Cartas de presentación y respuestas a preguntas de formulario ("Why this company?"). Si las piden, dilo en una línea y ofrece ayudar sin la skill.

---

## Ficheros de referencia

Cárgalos cuando los necesites, no todos de golpe:

- `references/bullets.md` — fórmula de bullets, verbos ES/EN, antes/después, qué borrar. **Léelo siempre antes de redactar.**
- `references/auditoria.md` — rúbrica de auditoría y checklist de salida.
- `references/evaluar-encaje.md` — veredicto, eliminatorios (alineados con Marty) y negociables.
- `references/adaptar-oferta.md` — informe de palabras clave y orientación mid/Senior y enfoque (PM, PO, Technical PM, AI PM, Technical PO).
- `references/sincronizar.md` — cómo actualizar e igualar los maestros EN/ES con aprobación.
- `references/mercados-idiomas.md` — convenciones LATAM/US/Canadá, anglicismos, falsos amigos, equivalencias.
- `references/entrevista.md` — guion de extracción para PM (solo modo Crear).

---

Basada en la skill `cv-product-designer` de **Gema Gutiérrez Medina** ([tribUX](https://escuelatribux.com), [Píldoras UX](https://pildorasux.com)), licencia MIT; adaptada a Product Management / Product Owner para el mercado remoto de LATAM, EE. UU. y Canadá.
