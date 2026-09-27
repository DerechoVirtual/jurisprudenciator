---
name: portfolio-status
description: Rollup de la cartera de asuntos. Distribucion por riesgo, plazos proximos, asuntos estancados y anomalias. Usar con donde estoy, estado cartera o cuantos asuntos abiertos.
---

# Estado de cartera

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Anomalías de plazo** (caducidad corriendo sin papeleta, 30 días del art. 71.6 LRJS) → `buscar_articulo` (`ley="LRJS"`, `articulo="65"`, `"71"` o `"103"`) para recalcular con la redacción vigente.
- **Empresas contrarias en concurso o disolución** (riesgo de cobro y FOGASA) → `buscar_empresa_mercantil` o `novedades_boe` (NIF de la empresa, último mes).
- **Asuntos con cuantía cercana a 3.000 €** (acceso a suplicación) → `buscar_articulo` (`ley="LRJS"`, `articulo="191"`).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "¿Dónde estoy?", "estado cartera", "qué tengo encima"
- "Cuántos asuntos abiertos", "rollup", "panorama"
- "Plazos esta semana", "qué tengo que hacer urgente"
- Antes de reunión de planificación

## Flujo

### 1. Leer fuente de verdad

- `matters/_log.yaml` — todos los asuntos
- Por defecto filtrar `status: open` (incluir closed con `--all`)

### 2. Calcular agregados

- **Distribución por riesgo:** count por `risk` ({critico, alto, medio, bajo})
- **Distribución por tipo:** count por `type`
- **Distribución por posición:** count por `side` (actor / demandado / mixto)
- **Próximos plazos (14 días):** ordenar por `next_deadline`, mostrar los que caen en los próximos 14 días
- **Asuntos estancados:** `last_updated` >30 días
- **Asuntos sin procedibilidad acreditada** (con tipo que la exige): cualquier `procedibilidad_acreditada: no` en asuntos donde el tipo requiera papeleta SMAC o reclamación previa (despido, cantidad, art. 50 ET, TRADE, prestaciones SS)
- **Cuantía total cartera:** suma de `cuantia` (informativa)

### 3. Detectar anomalías

Marcadores automáticos:
- 🔴 Asunto con `next_deadline` ya pasada (deadline incumplida)
- 🟠 Asunto con `next_deadline` <7 días sin actualización
- 🟡 Asunto `last_updated` >60 días sin movimiento
- 🟡 Asunto sin `representacion` definida (letrado / graduado social)
- 🟡 Asunto sin `cuantia` (cuando el tipo permite cuantificación)
- 🔴 Asunto de despido/sanción/MSCT con caducidad de 20 días corriendo y sin papeleta presentada
- 🟠 Reclamación previa SS resuelta o en silencio (45 días) con los 30 días de demanda corriendo (art. 71.6 LRJS)

### 4. Output

```
⚠️ Nota del revisor: lectura completa de _log.yaml · N asuntos abiertos · M anomalías marcadas

## Cartera (al [FECHA])

**Asuntos abiertos:** N
**Distribución por riesgo:** 🔴 Crítico: A · 🟠 Alto: B · 🟡 Medio: C · 🟢 Bajo: D
**Distribución por tipo:** despido: X · cantidad: Y · incapacidad: Z · contingencia: W · ..
**Cuantía total estimada:** XX.XXX €

### Próximos plazos (próximos 14 días)

| Fecha | Slug | Acción | Riesgo |
|---|---|---|---|
| .. | .. | .. | .. |

### Anomalías (N)

🔴 [slug] — Plazo incumplido: [fecha pasada] — [qué era]
🟠 [slug] — Caducidad de despido corriendo sin papeleta SMAC presentada
🟡 [slug] — Sin movimiento desde [fecha]

### Asuntos críticos (más cercanos)

[3-5 entradas con: slug, nombre, riesgo, próximo plazo, última actualización]
```

### 5. Decision tree

> **¿Qué hago ahora?**
> 1. **Deep dive en uno** — `/briefing-asunto <slug>` para ver detalle
> 2. **Resolver anomalías** — empezar por las 🔴
> 3. **Generar emails a colaboradores** — `/colaboradores-status` para semana
> 4. **Cerrar asuntos terminados** — si la lista incluye candidatos a cerrar
> 5. **Dashboard interactivo** — montar `create_artifact` con la cartera (recomendable si N>10)

📊 **Verlo como dashboard?** Si N > 10, ofrecer artifact con: summary stats arriba, tabla color-coded sortable por riesgo/plazo, gráfico de distribución, nota del revisor. En Cowork renderiza inline.

## Variantes

- `--all`: incluir cerrados
- `--risk-high`: solo alto/crítico
- `--by-colaborador`: agrupar por colaborador asignado (graduado social / procurador / perito)
- `--by-organo`: agrupar por órgano (Sección de lo Social del TI / Sala del TSJ)

## Reglas

1. **Severity floor.** Un asunto marcado `critico` en log no puede mostrarse como rutinario en rollup.
2. **No inventar plazos.** Si `next_deadline` está vacío, mostrar "—", no asumir.
3. **Asuntos cerrados fuera de rollup activo** salvo `--all`.
