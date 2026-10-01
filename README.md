# Marty + cv-product-manager

Un agente y una skill para **Claude Code** que ayudan a buscar trabajo como **Product Manager / Product Owner** en remoto para empresas de **Latinoamérica, Estados Unidos y Canadá**.

- **Marty** (`agents/marty.md`) — headhunter que hace barridos de ofertas recién publicadas (últimos 7 días), las verifica, las filtra y valora el encaje con tu CV.
- **cv-product-manager** (`skills/cv-product-manager/`) — skill que audita, evalúa contra ofertas, adapta y sincroniza tu CV de PM/PO en español o inglés, y genera el PDF.

## Qué hace Marty

- Busca **Product Manager, Senior / Sr PM, Technical PM, AI PM, Product Owner y Technical PO**, niveles **mid y Senior**.
- Solo ofertas **remotas** publicadas en los **últimos 7 días**: abre cada oferta para verificar la fecha real y descarta lo que no puede comprobar.
- Busca en **Latin America** y en tu país/ciudad de residencia, además de EE. UU. y Canadá.
- Consulta al menos 3 portales (2 que no sean LinkedIn: Wellfound, Get on Board, We Work Remotely, Working Nomads, 4 Day Week) y hace una búsqueda directa en los ATS de las empresas.
- Presupuesto: 4-5 minutos, 8-10 búsquedas, 8-20 ofertas abiertas.
- Descarta: lo que no es PM/PO, lo no remoto, lo que no tiene vínculo con LATAM/EE. UU./Canadá y todo lo que esté por encima de Senior.
- Valora el encaje (alto / medio / bajo) contra tu CV maestro, marca restricciones de residencia o permiso de trabajo, y dice si orientar el CV a mid o Senior.
- Entrega un máximo de **10 fichas**, más una lectura del mercado, el recuento por portal y cuáles están listas para aplicar.
- Aprende de cada barrido en `aprendizajes.md`.
- **Nunca aplica por ti.**

Se activa con: *"Buenos días Marty"*, *"Ofertas de PM de hoy"* o *"Dame las ofertas de PM y PO"*.

## Qué hace la skill cv-product-manager

| Modo | Para qué |
|---|---|
| **Auditar** | Revisar un CV con veredicto, antes/después de cada bullet y checklist |
| **Evaluar encaje** | Decidir si aplicar a una oferta (mismos eliminatorios que Marty) |
| **Adaptar** | Informe de palabras clave en 3 grupos + CV orientado a mid/Senior y al enfoque de la oferta (PM, PO, Technical PM, AI PM, Technical PO) |
| **Sincronizar** | Mantener iguales tus CV maestros en inglés y español, solo cuando lo pides |
| **Crear** | Entrevista guiada para escribir un CV de PM desde cero |

Principios: impacto en negocio y producto, resultados y no entregables, nunca inventar métricas, ATS-safe (una columna, texto seleccionable), sin datos personales innecesarios.

## Instalación

1. Copia los archivos a tu carpeta de Claude Code:

   ```bash
   mkdir -p ~/.claude/agents ~/.claude/skills ~/.claude/headhunter-pm ~/.claude/cv
   cp agents/marty.md ~/.claude/agents/
   cp -R skills/cv-product-manager ~/.claude/skills/
   cp headhunter-pm/*.md ~/.claude/headhunter-pm/
   ```

2. Rellena `~/.claude/headhunter-pm/contexto.md` con tus datos (residencia, permiso de trabajo, zona horaria, idiomas).
3. En `~/.claude/agents/marty.md`, sustituye `[Tu país]` / `[Tu ciudad]` por tu ubicación.
4. Guarda tu CV maestro en `~/.claude/cv/` como `Nombre-Apellido-Product-Manager-MAESTRO-EN.pdf` (y `-ES.pdf` si tienes versión en español), con su `.docx` editable al lado.
5. Abre una conversación nueva en Claude Code y escribe *"Buenos días Marty"*.

Para generar PDFs, la skill usa **Google Chrome** en modo headless (`scripts/html_to_pdf.py`).

