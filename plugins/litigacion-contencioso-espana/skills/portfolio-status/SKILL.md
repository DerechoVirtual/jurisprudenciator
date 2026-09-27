---
name: portfolio-status
description: Rollup de la cartera de asuntos contencioso-administrativos. Distribución por riesgo y materia, plazos de caducidad próximos, vía previa sin agotar, expedientes no recibidos, demandas en plazo del art. 52.1 LJCA y cautelares pendientes. Usar con dónde estoy, estado cartera o cuántos asuntos abiertos.
---

# Estado de cartera

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Recalcular vencimientos (sobre todo a la vuelta de agosto)** → `buscar_articulo` (`ley="LJCA"`, artículos 46, 48, 52, 55 y 128).
- **Vía previa pendiente sin movimiento** → `novedades_boe` (órgano y referencia del expediente; periodo de hasta 31 días) para detectar una resolución notificada por edicto que haya abierto un plazo sin que nadie lo sepa.
- **Asuntos estancados con una cuestión pendiente en el TS** → `buscar_sentencias` (`base="TS"`, `fecha_desde="dd/mm/aaaa"` = última actualización del asunto) para ver si ya hay sentencia.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- "¿Dónde estoy?", "estado cartera", "qué tengo encima"
- "Cuántos asuntos abiertos", "rollup", "panorama"
- "Plazos esta semana", "qué tengo que hacer urgente", "qué se me caduca"
- Antes de reunión de planificación
- **A la vuelta de agosto** — el art. 128.2 LJCA reactiva de golpe todos los plazos suspendidos

## Flujo

### 1. Leer fuente de verdad

- `matters/_log.yaml` — todos los asuntos
- Por defecto filtrar `status: open` (incluir closed con `--all`)

### 2. Calcular agregados

- **Distribución por riesgo:** count por `risk` ({critico, alto, medio, bajo})
- **Distribución por materia:** count por `type` (sancionador, urbanismo, responsabilidad-patrimonial, personal-función-pública, tributario-local, extranjería, contratación-pública, subvenciones, expropiación, seguridad-social, otros)
- **Distribución por procedimiento:** count por `procedimiento` (ordinario / abreviado / DDFF / otro)
- **Distribución por Administración:** count por `administracion_demandada` (estatal / autonómica / local / institucional)
- **Distribución por órgano:** count por `organo` (Juzgados CA / Salas TSJ / AN / TS)
- **Distribución por posición:** count por `side` (recurrente / demandada / codemandado)
- **Próximos plazos (14 días):** ordenar por `next_deadline`
- **Caducidades vivas:** asuntos con `fecha_caducidad_interposicion` en el futuro y recurso aún no interpuesto — ordenar por proximidad. **Es la lista que manda.**
- **Asuntos estancados:** `last_updated` >30 días
- **Cuantía total cartera:** suma de `cuantia` (informativa; excluir los `cuantia_determinada: "no"` del sumatorio y contarlos aparte)

### 3. Detectar anomalías

Marcadores automáticos:

- 🔴 **Caducidad vencida** — `fecha_caducidad_interposicion` ya pasada y recurso no interpuesto. Acto firme y consentido (art. 69.e LJCA). Máxima severidad: es irreversible.
- 🔴 **Caducidad a <7 días** sin escrito de interposición preparado (art. 46 LJCA)
- 🔴 **Vía previa sin agotar** con `fecha_caducidad_interposicion` fijada — contradicción: si la vía no está agotada, el contencioso no cabe todavía (art. 25.1 LJCA). Revisar el asunto.
- 🔴 **Demanda fuera de plazo del art. 52.1** — `expediente_administrativo: recibido` hace más de 20 días y no consta demanda presentada (procedimiento ordinario)
- 🟠 **`fecha_notificacion` vacía** en asunto con acto impugnado identificado — sin ella no hay cómputo de caducidad posible. Bloqueante.
- 🟠 **Vía previa pendiente** (`pendiente-alzada` / `pendiente-reposición`) con >1 mes sin movimiento — comprobar si ya se ha producido el silencio y ha nacido el acto presunto
- 🟠 **Expediente no recibido** — `reclamado` hace más de 20 días (art. 48.3: plazo improrrogable). Procede reiteración y, en su caso, multa coercitiva de 300 a 1.200 € (art. 48.7)
- 🟠 **Expediente incompleto sin reaccionar** — `recibido` y con huecos anotados, dentro aún de los 10 primeros días del plazo de demanda: la solicitud del art. 55 LJCA **reinicia** el plazo si se pide en esa ventana; después solo lo reanuda
- 🟠 **Medida cautelar pendiente** — `medida_cautelar: pedida` sin resolución, en asunto cuyo acto es ejecutivo
- 🟠 Asunto con `next_deadline` <7 días sin actualización
- 🟡 **Cautelar no pedida** en asunto con acto de ejecución inminente (sanción firme en vía administrativa, orden de demolición, clausura, reintegro) — valorar art. 130.1 LJCA
- 🟡 Asunto `last_updated` >60 días sin movimiento
- 🟡 **Sin procurador ante órgano colegiado** — `organo` es Sala (TSJ/AN/TS) y `procurador: no-designado`: es **preceptivo** (art. 23.2 LJCA)
- 🟡 **Acuerdo corporativo pendiente** — cliente persona jurídica sin el documento del art. 45.2.d): causa de inadmisión evitable
- 🟡 Asunto sin `cuantia` cuando la materia permite cuantificación — sin ella no se puede fijar procedimiento (art. 78.1) ni apelabilidad (art. 81.1.a)
- 🟡 **DDFF en agosto** — asunto con `procedimiento: DDFF` y plazo corriendo en agosto: **agosto es hábil** aquí (art. 128.2 LJCA). No se relaja.

### 4. Output

```
⚠️ Nota del revisor: lectura completa de _log.yaml · N asuntos abiertos · M anomalías marcadas

## Cartera (al [FECHA])

**Asuntos abiertos:** N
**Distribución por riesgo:** 🔴 Crítico: A · 🟠 Alto: B · 🟡 Medio: C · 🟢 Bajo: D
**Por materia:** sancionador: X · urbanismo: Y · responsabilidad-patrimonial: Z · ..
**Por procedimiento:** ordinario: X · abreviado: Y · DDFF: Z
**Por Administración:** estatal: X · autonómica: Y · local: Z
**Cuantía total estimada:** XX.XXX € (+ N asuntos de cuantía indeterminada)

### ⏳ Caducidades vivas (recurso aún no interpuesto)

| Vence | Slug | Acto impugnado | Cómputo | Días | Riesgo |
|---|---|---|---|---|---|
| .. | .. | .. | 2 meses art. 46.1 | .. | .. |

### Próximos plazos (próximos 14 días)

| Fecha | Slug | Acción | Norma | Riesgo |
|---|---|---|---|---|
| .. | .. | Demanda | art. 52.1 LJCA | .. |

### Anomalías (N)

🔴 [slug] — Caducidad vencida el [fecha]: acto firme y consentido (art. 69.e LJCA)
🔴 [slug] — Demanda no presentada: expediente recibido el [fecha], 20 días del art. 52.1 vencidos
🟠 [slug] — Vía previa sin agotar: pendiente de alzada desde [fecha]
🟠 [slug] — Expediente reclamado el [fecha]: superados los 20 días del art. 48.3 → reiterar
🟠 [slug] — Cautelar pedida el [fecha], sin resolver
🟡 [slug] — Sin movimiento desde [fecha]

### Asuntos críticos (más cercanos)

[3-5 entradas con: slug, materia, riesgo, próximo plazo, última actualización]
```

### 5. Decision tree

> **¿Qué hago ahora?**
> 1. **Atacar las caducidades** — empezar por la tabla ⏳, no por las anomalías
> 2. **Deep dive en uno** — `/briefing-asunto <slug>`
> 3. **Resolver anomalías** — seguir por las 🔴
> 4. **Agotar vías previas pendientes** — `/recurso-alzada-reposicion-ca`
> 5. **Generar emails a colaboradores** — `/colaboradores-status` para la semana
> 6. **Cerrar asuntos terminados** — si la lista incluye candidatos a cerrar
> 7. **Dashboard interactivo** — montar `create_artifact` con la cartera (recomendable si N>10)

📊 **¿Verlo como dashboard?** Si N > 10, ofrecer artifact con: summary stats arriba, tabla color-coded sortable por caducidad/riesgo/plazo, gráfico de distribución por materia y Administración, nota del revisor. En Cowork renderiza inline. **Sin datos personales:** usar `[CLIENTE]` y descriptores de materia.

## Variantes

- `--all`: incluir cerrados
- `--risk-high`: solo alto/crítico
- `--caducidad`: solo la tabla de caducidades vivas, ordenada por proximidad
- `--sin-agotar`: solo asuntos con `via_previa` distinta de `agotada`/`no-procede`
- `--expedientes`: estado de todos los expedientes administrativos
- `--cautelares`: asuntos con `medida_cautelar` en `pedida`
- `--by-administracion`: agrupar por Administración demandada
- `--by-organo`: agrupar por órgano judicial
- `--by-procurador`: agrupar por procurador asignado

## Reglas

1. **La caducidad manda.** El rollup se ordena por riesgo de perder un plazo del art. 46 LJCA, no por cuantía ni por riesgo comercial. Un asunto de 300 € con la caducidad a 3 días va por delante de uno de 300.000 € sin plazo próximo.
2. **Severity floor.** Un asunto marcado `critico` en el log no puede mostrarse como rutinario en el rollup.
3. **No inventar plazos.** Si `next_deadline` o `fecha_caducidad_interposicion` están vacíos, mostrar "—" y marcarlo como anomalía. **Nunca** derivar una caducidad de una `fecha_notificacion` estimada sin decir que es estimada.
4. **Agosto — art. 128.2 LJCA.** Al recalcular vencimientos, agosto **no corre** para ningún plazo de la LJCA, **salvo en DDFF, donde es hábil**. No citar el art. 133 LEC. Los plazos de la **vía administrativa** (LPAC) se rigen por sus propias normas: no aplicarles la regla de agosto de la LJCA.
5. **Nunca alertar por MASC.** No existe en contencioso. La alerta equivalente es **vía previa sin agotar** (art. 25.1 LJCA).
6. **Asuntos cerrados fuera del rollup activo** salvo `--all`.
7. **Sin datos personales en el rollup.** Slugs y descriptores de materia; terceros con marcadores.
