---
name: briefing-asunto
description: Briefing profundo de un asunto. Posicion actual, cambios, proximo plazo, cuestiones abiertas y re-evaluacion de riesgo. Usar con briefing o donde estamos con el asunto.
---

# Briefing de asunto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Comprobación previa antes de citar jurisprudencia nueva** → `estado`.
- **Jurisprudencia nueva sobre la cuestión central desde el último briefing** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`, `fecha_desde` = fecha del último briefing) + `leer_sentencias` (`parrafos=3`).
- **Comprobar que la jurisprudencia archivada en `jurisprudencia/` sigue bien identificada** → `buscar_por_cita` sobre cada ECLI o ROJ.
- **Reformas que afecten a los plazos o a la pretensión** → `buscar_articulo` (redacción vigente) y `novedades_boe` (materia, último mes).
- **Situación de la empresa contraparte para la re-evaluación de riesgo** (concurso, disolución) → `buscar_empresa_mercantil`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- "Briefing de [slug]", "ponme al día con [asunto]"
- "Dónde estamos con [asunto]"
- Antes de reunión con cliente, acto de conciliación (SMAC o judicial) o acto del juicio
- Cuando un colaborador externo pide estado

## Flujo

### 1. Identificar asunto

Si no se da slug, listar candidatos por:
- Asunto activo en CLAUDE.md
- Asuntos con `next_deadline` próximo
- Últimos actualizados

### 2. Leer fuentes

- `matters/<slug>/matter.md` — intake + tesis
- `matters/<slug>/history.md` — eventos
- Fila correspondiente de `_log.yaml`
- Escritos en `matters/<slug>/escritos/` (lista con fechas)
- Jurisprudencia archivada en `matters/<slug>/jurisprudencia/`
- Cronología si existe en `matters/<slug>/cronologia.md`

### 3. Sintetizar briefing

Estructura:

```
**[Slug] — [Nombre del asunto]**
Cliente: [nombre + posición procesal]
Contraparte: [empresa / trabajador / INSS / TGSS / mutua + abogado contraparte]
Órgano: [Sección de lo Social del Tribunal de Instancia / Sala de lo Social del TSJ]
Cuantía: [€]
Estado: [open / stayed]
Riesgo: [icono + nivel]
Materialidad: [alta/media/baja]

---

## Tesis del asunto
[2-3 frases — la "historia" que vamos a contar]

## Posición procesal actual
[En qué fase está: pre-papeleta / conciliación SMAC pendiente / reclamación previa en plazo / demanda presentada / juicio señalado / esperando sentencia / suplicación / RCUD / ejecución]

## Hitos desde la última actualización
[Eventos de history.md desde el último briefing — fechas + qué ocurrió]

## Próximo plazo crítico
[Fecha + qué hay que hacer + cómputo: "caducidad de 20 días hábiles desde el despido del XX-XX, suspendida por papeleta el XX-XX, vence el YY-YY" / "anuncio de suplicación: 5 días desde notificación de sentencia"]

## Cuestiones abiertas
- [pregunta 1 que necesita decisión]
- [pregunta 2 que necesita información del cliente]

## Re-evaluación de riesgo
[Sigue siendo X o ha cambiado? Si cambia, propuesta de nuevo nivel y razón]

## Jurisprudencia clave en el asunto
- [STS (Sala IV) o STSJ con ECLI/ROJ — punto que sostiene]
- ..

## Vía de procedibilidad
[Papeleta SMAC / reclamación previa — acreditada sí/no — si no, qué falta y cómo afecta al cómputo de caducidad]

## Conservación documental
[Acreditada al cliente / pendiente / liberada]
```

### 4. Decision tree

> **¿Qué hago ahora?**
> 1. **Redactar el siguiente escrito** — `/papeleta-conciliacion` / `/redactar-demanda-despido` / `/reclamacion-cantidad` / `/recurso-suplicacion`
> 2. **Actualizar history con nuevos hitos** — `/actualizar-asunto <slug>`
> 3. **Cronología defensiva u ofensiva** — `/cronologia <slug>`
> 4. **Cuadro de elementos** — `/cuadro-elementos <slug>`
> 5. **Preparar interrogatorio** — `/preparacion-interrogatorio <slug> <nombre>`
> 6. **Tirar de jurisprudencia** — el conector MCP `jurisprudenciator` (`buscar_sentencias`)

## Reglas

1. **No reinventar la tesis.** Si `matter.md` tiene tesis, usarla. Si en `history.md` se cambió, marcarlo.
2. **Cómputo de plazos siempre hábiles** (art. 43 LRJS). Sábados no hábiles. Agosto y 24-dic a 6-ene inhábiles SALVO despido, extinción arts. 50-52 ET, MSCT, movilidad, conciliación familiar, altas médicas, vacaciones, electoral, conflictos colectivos y tutela DDFF (art. 43.4 LRJS).
3. **Pre-flight check** del conector `jurisprudenciator` (`estado`) antes de citar nueva jurisprudencia en el briefing.
4. **No narrar acciones del plugin** ("estoy leyendo history.md..."). Solo el briefing limpio.
