# Sincronizar el maestro (ES ↔ EN)

## Qué es y qué no es

- Los maestros son **fijos**. Adaptar a una oferta **nunca** los toca.
- Este modo solo se usa **cuando la persona lo pide**: nuevo trabajo o fin del actual, logro o métrica nueva, certificación terminada, corrección, o igualar los dos idiomas.
- **Nunca** se ejecuta por iniciativa propia ni como efecto secundario de otra tarea. Si durante una auditoría o adaptación ves algo que convendría cambiar en el maestro, **propónlo** y que la persona decida si sincroniza.

## Archivos

En `~/.claude/cv/`:
- `Nombre-Apellido-Product-Manager-MAESTRO-EN.docx` + `.pdf`
- `Nombre-Apellido-Product-Manager-MAESTRO-ES.docx` + `.pdf`

El `.docx` es la fuente editable. El `.pdf` es lo que lee el agente Marty: si no se regenera, Marty trabaja con información vieja.

## Flujo

1. **Lee los dos maestros** (texto de los PDF, o `textutil -convert txt -stdout` sobre los `.docx`).
2. **Describe el cambio pedido** y cómo quedaría **en ambos idiomas**, lado a lado:

   ```
   Sección / puesto: …
   EN (antes → después): …
   ES (antes → después): …
   ```

   La traducción sigue `mercados-idiomas.md` (español neutro, anglicismos del oficio, falsos amigos). No es literal: cada versión debe sonar nativa en su idioma.
3. **Si el objetivo es igualar** (o detectas diferencias de contenido entre EN y ES): lista cada diferencia — bullets que están en uno y no en otro, secciones con distinta estructura, datos que no coinciden — y propone cómo resolver cada una. Cuando los dos dicen cosas distintas sobre el mismo hecho, **pregunta cuál es la cierta**; no elijas tú.
4. **Espera aprobación explícita.** Sin un "sí" no se toca ningún archivo.
5. **Aplica los cambios aprobados a los dos `.docx`.**
   - Si tienes forma de editar `.docx` (p. ej. la skill `docx`), aplícalos conservando el formato del documento. Antes, guarda una copia de seguridad: `…-MAESTRO-EN.backup-AAAA-MM-DD.docx`.
   - Si no, entrega el texto final exacto de cada cambio, listo para pegar en Word, y guía a la persona.
6. **Regenera los dos PDF** desde Word (Archivo → Exportar → PDF), o pide a la persona que lo haga, con los mismos nombres. Comprueba que el texto se pueda leer.
7. **Confirma** qué cambió en cada idioma y que Marty ya lee la versión nueva. Si el cambio afecta al resumen de experiencia de `~/.claude/headhunter-pm/contexto.md`, propón actualizarlo también.
