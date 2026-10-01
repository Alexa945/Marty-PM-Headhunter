# Aprendizajes — patrones de barridos (Marty)

Este archivo manda sobre la definición del agente en cuanto a qué portales priorizar o evitar. Marty lo va rellenando barrido a barrido.

## Punto de partida (observado en barridos reales, oct. 2026)

- **LinkedIn:** la página de búsqueda (`linkedin.com/jobs/search?keywords=Product%20Manager&f_TPR=r604800&f_WT=2&sortBy=DD&location=...`) se abre con WebFetch y trae "Posted X ago". Es la fuente con más volumen. Buscar por **país** además de `Latin America`: aparecen ofertas que la búsqueda regional no muestra.
- El filtro remoto de LinkedIn (`f_WT=2`) **cuela presenciales e híbridas**: abrir siempre la ficha y confirmar la modalidad. Si la ficha no declara remoto, descartar por duda.
- Muchas fichas muestran una ciudad en la cabecera aunque la oferta sea de otro país: leer la descripción.
- **Get on Board:** el listado por categoría trae fechas; los resultados de WebSearch suelen ser ofertas cerradas o antiguas.
- **4 Day Week, Wellfound, Himalayas:** cargan bien, pero casi todo es "US only".
- **We Work Remotely, startup.jobs:** devuelven 403 a WebFetch. **Working Nomads:** no muestra listados por WebFetch.
- **X-ray de ATS** (Greenhouse, Lever, Ashby…): WebSearch suele ignorar `site:` y las fichas casi nunca muestran fecha → rinde poco.
- Muchas ofertas "Senior PM" en LATAM piden 7+ años; algunas consultoras publican como "PM" puestos que en realidad son Project/Program Manager.

## Portales

| Portal | Rendimiento | Notas |
|---|---|---|
| _(se rellena con cada barrido)_ | | |

## Empresas

| Empresa | Notas |
|---|---|
| _(se rellena con cada barrido)_ | |

## Reglas aprendidas

- _(se rellena con cada barrido)_
