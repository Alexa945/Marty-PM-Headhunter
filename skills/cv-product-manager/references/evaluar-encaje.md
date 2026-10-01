# Evaluar encaje con una oferta

El entregable es un **informe por escrito**, no un CV modificado. Si reescribes antes de que la persona lea el veredicto, das por hecho que aplicar es buena idea.

## Criterios alineados con Marty

Esta skill y el agente Marty (`~/.claude/agents/marty.md`) tienen que llegar a la misma conclusión sobre la misma oferta. Si Marty dice "encaje bajo por elegibilidad", aquí no puede salir "adelante".

### Eliminatorios automáticos

Si se da cualquiera de estos, el veredicto es **no aplicar**, se dice en la primera línea y no se ofrece adaptar el CV:

1. **Elegibilidad:** la oferta es "US only", "Canada residents only" o exige autorización de trabajo en EE. UU./Canadá que la persona no tiene (ver `~/.claude/headhunter-pm/contexto.md`). Remoto abierto a LATAM, al país de residencia, "Americas", worldwide o vía EOR/contrato internacional (Deel, Remote.com, Oyster…) **sí** es elegible.
2. **Nivel por encima de Senior:** Lead, Principal, Staff, Group PM, Head of Product, Director/VP of Product, CPO.
3. **Francés obligatorio** (típico en Quebec).

### No eliminatorio: el horario

El horario **nunca descarta** una oferta. ET (Nueva York) es lo preferido, PT (California) es aceptable; otras zonas (Europa, Asia) se anotan como desventaja y pueden bajar el encaje, pero la oferta se evalúa igual.

### Negociables

Se compensan o se matizan:
- Años de experiencia a 1-2 de lo pedido.
- Dominio adyacente (FinTech ↔ InsurTech ↔ SaaS).
- Herramienta concreta dentro de una categoría que ya se domina (Amplitude vs GA4, Linear vs Jira).
- Requisitos "nice to have" / "a plus" / "deseable" (incluido portugués en LATAM: se cita como desventaja competitiva, no bloquea).
- Horario (ver arriba).

En ofertas **Technical PM / Technical PO / AI PM**, revisa con cuidado la profundidad técnica exigida: "background en ingeniería", "CS degree", "hands-on con APIs", "experiencia con LLMs en producción". Si es requisito central y no está en el maestro, es un hueco serio (casi eliminatorio); si es "a plus", negociable.

Una diferencia grande de años (más de ~3) o un requisito técnico central que no se tiene (p. ej. "SQL avanzado diario" sin ninguna experiencia en SQL) se tratan como **casi eliminatorios**: se dice claramente.

## Estructura del informe

```
**Veredicto:** Aplicar / Aplicar con ajustes / No aplicar — motivo en una frase.
**Nivel de la oferta:** mid / Senior (o "por encima de Senior → eliminatorio")
**Enfoque:** PM / PO / Technical PM / AI PM / Technical PO
**Idioma del CV:** EN / ES  ·  **Papel:** Letter / A4

**Eliminatorios:** ninguno / cuál y por qué
**Requisito a requisito:**
- [requisito] → ✅ cubierto (dónde en el CV) / 🟡 parcial (qué falta) / ❌ no se tiene
**Horario:** qué pide y cómo encaja (no eliminatorio)
**Huecos y qué hacer con cada uno:** reformular / destacar algo existente / asumirlo y preparar respuesta para la entrevista
```

Solo al final, si el veredicto no es "No aplicar", ofrece pasar al modo Adaptar.

## Oferta que no describe el puesto

Si el título dice PM pero el cuerpo es plantilla genérica o describe otro rol (Project Manager, Product Marketing, Business Analyst), dilo. No evalúes contra requisitos imaginados: convierte lo que falta en preguntas para quien publica.

## Saber decir que no

La tentación es encontrar la manera de que todo encaje. Eso hace que la persona gaste semanas en procesos que terminan en rechazo. **Que una oferta no sea para este CV es el resultado más útil que puede dar este modo**, y se dice en la primera línea. Separa el CV de la persona: a veces la persona encaja y lo que falla es que el documento no lo demuestra — eso se arregla adaptando.
