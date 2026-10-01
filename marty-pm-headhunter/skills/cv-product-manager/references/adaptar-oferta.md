# Adaptar el CV a una oferta

Si aún no se ha decidido aplicar, pasa antes por `evaluar-encaje.md`. Si hay un eliminatorio, no se adapta.

**Regla que no se cruza:** adaptar es **reordenar, reformular y elegir qué destacar de lo que es cierto**. No es añadir experiencia, herramientas ni métricas que no existen.

## Paso 0 — Base e idioma

- Parte siempre del **maestro** en el idioma de la oferta (`…-MAESTRO-EN` o `…-MAESTRO-ES`). Si el idioma es ambiguo, inglés.
- **No modifiques el maestro.** La adaptación es un archivo nuevo.

## Paso 1 — Informe de palabras clave (antes de tocar nada)

Extrae de la oferta las palabras clave que un ATS y quien selecciona van a buscar: rol, métodos, herramientas, dominio, tipo de producto, métricas, stakeholders. Preséntalas en tres grupos:

```
**Ya cubiertas por el CV** — están y con respaldo en bullets
- roadmap (Empresa A, Empresa B) · discovery (Empresa C) · …

**Se pueden añadir con experiencia real** — la persona lo ha hecho, pero el CV no lo dice o lo dice con otras palabras
- "stakeholder management" → el CV dice "coordiné negocio y tecnología" en Empresa B
- …

**No se tienen** — no se añaden; se decide qué hacer con el hueco
- SQL avanzado → preparar respuesta honesta para la entrevista
- …
```

Para el grupo del medio, cita el bullet del maestro que lo respalda. Si no hay bullet que lo respalde, va al tercer grupo. Si dudas, pregunta a la persona antes de moverlo.

Espera confirmación antes de seguir, o sigue directamente si la persona ya pidió la adaptación completa (p. ej. cuando la invoca Marty con la oferta).

## Paso 2 — Orientación

Decide y di en una línea:
- **Nivel:** mid o Senior (según la oferta; si lo indica Marty, respeta su criterio).
- **Enfoque:** PM, PO, Technical PM, AI PM o Technical PO, según el título y el cuerpo de la oferta (ver la tabla de enfoques en SKILL.md § Niveles). Si el título es genérico ("Product Manager") pero el cuerpo es claramente técnico o de IA, usa el enfoque del cuerpo y dilo.

Ver la tabla de SKILL.md § Niveles.

## Paso 3 — Ajustes, en este orden

1. **Resumen**: reescríbelo para esta oferta — rol y años + dominio de la oferta + la evidencia más fuerte para ella.
2. **Título de la cabecera**: igual al de la oferta si es cierto (*Product Owner* vs *Senior Product Manager*).
3. **Orden de bullets dentro de cada puesto**: lo que más conecta con la oferta, arriba.
4. **Reformulación con el vocabulario de la oferta** (grupo 2 del informe), sin cambiar el hecho.
5. **Recorte**: fuera los bullets que no conectan, hasta la extensión objetivo (1 página mid, máx. 2 Senior). El maestro los conserva.
6. **Habilidades**: reordena para que lo que pide la oferta aparezca primero; nunca añadas lo que no se domina.
7. **Experiencia de diseño**: más o menos presente según cuánto valore la oferta discovery/UX.

## Paso 4 — Generar y entregar

1. Maqueta con `assets/cv-template.html` (Letter para EE. UU./Canadá, A4 para LATAM).
2. Genera el PDF con `scripts/html_to_pdf.py` en `~/.claude/cv/adaptaciones/`.
3. Pasa la prueba de extracción de texto y la checklist de `auditoria.md`.
4. Copia el PDF final a `~/Downloads/` y muéstralo en Finder (`open -R ~/Downloads/<archivo>.pdf`). Ver SKILL.md § Generar el documento.
5. Entrega:
   - Resumen de lo que cambió respecto al maestro (3-6 líneas).
   - Huecos que quedan (grupo 3) y cómo afrontarlos en la entrevista.
   - **El nombre exacto del archivo**, p. ej. `Nombre-Apellido-Product-Owner-EN-Stripe.pdf`, para anotarlo en la columna "CV usado" de `~/.claude/headhunter-pm/candidaturas.md`.

## Nombre del archivo

`Nombre-Apellido-<Rol>-<EN|ES>-<Empresa>.pdf`

- El rol es el de la oferta, en Title-Case con guiones: `Product-Manager`, `Product-Owner`, `Technical-Product-Manager`, `AI-Product-Manager`, `Technical-Product-Owner`.
- La empresa sin espacios ni caracteres raros (`Mercado-Libre`, `Nubank`).
- Si ya existe un archivo con ese nombre (segunda adaptación para la misma empresa), añade el puesto o la fecha: `…-Nubank-2026-10.pdf`. Nunca sobrescribas sin preguntar.
