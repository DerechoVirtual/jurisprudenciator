---
name: portfolio-status
description: Rollup de la cartera de asuntos penales. Distribucion por fase, posicion y riesgo; alertas de plazo de instruccion del art. 324 LECrim, prescripcion, plazos de recurso, prision provisional, detenido en 72 h, escrito de defensa y juicios señalados. Usar con donde estoy, estado cartera o cuantos asuntos abiertos.
---

# Estado de cartera — penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Alertas de plazo** (arts. 324 y 504 LECrim; prescripción de los arts. 131 y 132 CP) → `buscar_articulo` cuando el asunto no trae la redacción verificada.
- **Tipos reformados después de los hechos** → `buscar_articulo` (`ley="CP"`), que indica la norma que dio la redacción vigente, para marcar los asuntos en los que toca comparar la ley más favorable.
- **Edictos o requisitorias publicados en causas de la cartera** → `novedades_boe` (por número de procedimiento u órgano, nunca por el nombre del cliente) → `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "¿Dónde estoy?", "estado cartera", "qué tengo encima"
- "Cuántos asuntos abiertos", "rollup", "panorama"
- "Plazos esta semana", "qué tengo que hacer urgente"
- Antes de reunión de planificación o de una semana de guardia

## Flujo

### 1. Leer fuente de verdad

- `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/matters/_log.yaml` — todos los
  asuntos
- Por defecto filtrar `status: open` (incluir cerrados con `--all`)

### 2. Calcular agregados

- **Distribución por riesgo:** count por `risk` ({critico, alto, medio, bajo})
- **Distribución por fase:** count por `fase` (diligencias-previas / instrucción / intermedia /
  juicio-oral / recurso / ejecución)
- **Distribución por posición:** count por `posicion` (defensa / acusación-particular /
  acusación-popular / actor-civil / responsable-civil-subsidiario)
- **Distribución por procedimiento:** count por `procedimiento` (abreviado / sumario / juicio-rápido /
  delito-leve / jurado / menores)
- **Clientes privados de libertad:** count de `situacion_personal: prision-provisional` ← **el número
  que se mira primero**
- **Instrucciones vivas:** count de asuntos con `fase: instruccion` o `diligencias-previas`, con sus
  días restantes hasta `fecha_vencimiento_instruccion`
- **Próximos plazos (14 días):** ordenar por `next_deadline`
- **Asuntos estancados:** `last_updated` > 30 días
- **Responsabilidad civil total reclamada:** suma de `responsabilidad_civil.cuantia_reclamada`
  (informativa)

### 3. Detectar anomalías — alertas propias del penal

Marcadores automáticos, **en este orden de precedencia**:

| Prioridad | Alerta | Regla |
|---|---|---|
| 🔴 | **Detenido dentro del plazo de 72 h** | `detenido.hubo: sí` y < 72 h desde `detenido.fecha` — art. 520.1 LECrim. Todo lo demás espera. |
| 🔴 | **⚠️ Instrucción vencida o a punto, sin prórroga acordada** | `fecha_vencimiento_instruccion` a **< 30 días** y `prorrogas` sin auto vigente — art. 324.1 |
| 🔴 | **Art. 324.3 activado** | `art_324_3_alerta: sí` — hubo diligencias acordadas tras vencer sin auto previo, o la prórroga fue revocada: **no son válidas**. Línea de nulidad viva. |
| 🔴 | **Plazo de recurso abierto y venciendo** | `next_deadline_concepto` de recurso a < 3 días |
| 🔴 | **Plazo incumplido** | `next_deadline` ya pasada |
| 🔴 | **Prisión provisional cerca del límite** | días desde el ingreso > **2/3** del máximo del art. 504 → art. 504.6: comunicación y tramitación preferente. Y si roza el máximo: **excarcelación** |
| 🟠 | **Prescripción próxima** | `prescripcion_delito.fecha_estimada` a < 6 meses (a < 2 meses si el plazo es de **1 año**: delitos leves, injurias y calumnias — art. 131 CP) |
| 🟠 | **Escrito de defensa pendiente** | traslado notificado y `next_deadline` de escrito de defensa a < 5 días — **10 días** comunes, art. 784.1 LECrim |
| 🟠 | **Juicio señalado** | señalamiento a < 30 días sin preparación registrada en `history.md` |
| 🟠 | **Prórroga de instrucción a solicitar** | `fecha_vencimiento_instruccion` a < 60 días en asuntos de **acusación** (a la defensa le interesa lo contrario: no es una tarea, es una oportunidad) |
| 🟠 | **Medida cautelar a revisar** | `544-bis` / `544-ter` / `fianza-embargo` sin revisión en > 90 días |
| 🟡 | **Sin movimiento** | `last_updated` > 60 días |
| 🟡 | **Sin control del art. 324** | `fecha_incoacion` vacía o `art_324_3_alerta: [verificar]` en asunto con instrucción viva |
| 🟡 | **Sin fecha de los hechos** | `fecha_hechos` vacía → no se puede fijar el CP aplicable (art. 2 CP) ni la prescripción |
| 🟡 | **Comparación de penas pendiente** | `fecha_hechos` anterior al **10-4-2026** (LO 1/2026) o al **3-4-2025** (LO 1/2025) sin constancia de comparación del art. 2.2 CP |
| 🟡 | **Sin procurador** cuando el procedimiento lo requiere |
| 🟡 | **Conformidad negociando** sin movimiento en > 30 días |

### 4. Output

```
⚠️ Nota del revisor: lectura completa de _log.yaml · N asuntos abiertos · M anomalías marcadas

## Cartera (al [FECHA])

**Asuntos abiertos:** N   |   **Clientes en prisión provisional:** P
**Distribución por riesgo:** 🔴 Crítico: A · 🟠 Alto: B · 🟡 Medio: C · 🟢 Bajo: D
**Por fase:** DP: X · instrucción: Y · intermedia: Z · juicio oral: W · recurso: V · ejecución: U
**Por posición:** defensa: X · acusación particular: Y · acusación popular: Z · actor civil: W
**Responsabilidad civil total reclamada:** XX.XXX € (informativa)

### ⚠️ Control del art. 324 LECrim — instrucciones vivas

| Slug | Incoación | Vence | Restan | Prórrogas | 324.3 |
|---|---|---|---|---|---|
| .. | .. | .. | N días | N (última: fecha auto) | ✅ / ⚠️ |

### Próximos plazos (próximos 14 días)

| Fecha | Slug | Concepto (con su norma) | Fase | Riesgo |
|---|---|---|---|---|
| .. | .. | Escrito de defensa — 10 días, art. 784.1 | intermedia | 🔴 |

### Anomalías (N)

🔴 [slug] — Detenido desde [fecha/hora]. Restan [N] h de las 72 (art. 520.1).
🔴 [slug] — Instrucción vence el [fecha] ([N] días) sin auto de prórroga (art. 324.1).
🔴 [slug] — ⚠️ Art. 324.3: diligencias acordadas tras el vencimiento. No son válidas: [cuáles].
🔴 [slug] — Prisión provisional: [N] días, superadas las 2/3 partes del máximo (art. 504.6).
🟠 [slug] — Prescripción del delito el [fecha] ([N] restantes) — art. 131 CP.
🟠 [slug] — Escrito de defensa vence el [fecha] (art. 784.1).
🟡 [slug] — Sin movimiento desde [fecha].

### Asuntos críticos (más cercanos)

[3-5 entradas con: slug, delitos, fase, posición, riesgo, próximo plazo, última actualización]
```

### 5. Decision tree

> **¿Qué hago ahora?**
> 1. **Empezar por las 🔴** — detenido, art. 324 y prisión provisional van antes que todo
> 2. **Deep dive en uno** — `/briefing-asunto <slug>`
> 3. **Pedir diligencias donde quede plazo** — `/solicitud-diligencias-instruccion-catalogo`
> 4. **Revisar medidas cautelares** — `/medidas-cautelares-penales-catalogo`
> 5. **Generar emails a colaboradores** — `/colaboradores-status`
> 6. **Cerrar asuntos terminados** — `/cerrar-asunto` (ojo: sentencia firme ≠ cerrado si hay
>    ejecutoria viva)
> 7. **Dashboard interactivo** — montar artifact con la cartera (recomendable si N > 10)

📊 **¿Verlo como dashboard?** Si N > 10, ofrecer artifact con: contador de días del art. 324 por
asunto arriba del todo, tabla color-coded sortable por riesgo/plazo/fase, gráfico de distribución por
fase, nota del revisor. En Cowork renderiza inline.

> ⚠️ **Si el dashboard sale del entorno del despacho, va despersonalizado**: solo slugs, delitos y
> fechas. Nunca nombres. Art. 10 RGPD.

## Variantes

- `--all`: incluir cerrados
- `--risk-high`: solo alto/crítico
- `--instruccion`: solo asuntos con instrucción viva, ordenados por días restantes del art. 324
- `--presos`: solo `situacion_personal: prision-provisional`, con días y límite del art. 504
- `--by-organo`: agrupar por órgano judicial
- `--by-posicion`: agrupar por posición procesal
- `--by-procurador`: agrupar por procurador asignado

## Reglas

1. **⚠️ El art. 324 va primero.** El cuadro de instrucciones vivas se muestra **siempre**, antes que
   los agregados. Es el único plazo que se pierde sin que nadie avise y que no se recupera.
2. **Severity floor.** Un asunto marcado `critico` en el log no puede mostrarse como rutinario en el
   rollup.
3. **No inventar plazos.** Si un campo está vacío, mostrar "—" y marcarlo como anomalía 🟡. Nunca
   estimar una fecha de vencimiento de instrucción o de prescripción sin `fecha_incoacion` o
   `fecha_hechos`.
4. **Toda cita de plazo lleva su norma** (art. 324 LECrim, art. 131 CP, art. 784.1 LECrim,
   art. 790.1 LECrim, art. 856 LECrim, art. 504 LECrim, art. 520.1 LECrim). Lo que no esté en
   `references/anclas-normativas-penal.md` se verifica con `buscar_articulo` o se marca `[verificar]`.
5. **Asuntos cerrados fuera del rollup activo** salvo `--all`. Los que están en **ejecutoria** no
   están cerrados: aparecen con `fase: ejecucion`.
6. **El rollup no imprime nombres.** Se construye desde `_log.yaml`, que no los tiene. Si se pide
   "la lista de mis clientes investigados", el output sigue siendo por slug.
