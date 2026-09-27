---
name: briefing-asunto
description: Briefing profundo de un asunto. Posicion actual, cambios, proximo plazo, cuestiones abiertas y re-evaluacion de riesgo. Usar con briefing o donde estamos con el asunto.
---

# Briefing de asunto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Verificar las resoluciones archivadas en el asunto antes de listarlas en «Jurisprudencia clave»** → `buscar_por_cita` (ECLI o ROJ exacto).
- **Jurisprudencia nueva sobre la tesis del asunto (opción 6 del árbol de decisión)** → `buscar_sentencias` (`jurisdiccion="CIVIL"`; `base="TS"` o `base="AN"` con `tipo_organo="AP"` y la `provincia` del asunto; `fecha_desde="dd/mm/aaaa"` del último briefing) + `leer_sentencias` (`parrafos=3`).
- **Cómputo del próximo plazo crítico con el precepto vigente** → `buscar_articulo` (`ley="LEC"`).
- **Situación actual de la contraparte si es sociedad (administradores, disolución, concurso)** → `buscar_empresa_mercantil`.
- **Comprobación previa del conector antes de citar jurisprudencia nueva (regla 3)** → `estado`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Briefing de [slug]", "ponme al día con [asunto]"
- "Dónde estamos con [asunto]"
- Antes de reunión con cliente, llamada con procurador, vista, audiencia previa
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
Contraparte: [nombre + abogado contraparte]
Tribunal: [Tribunal de Instancia + sección]
Cuantía: [€]
Estado: [open / stayed]
Riesgo: [icono + nivel]
Materialidad: [alta/media/baja]

---

## Tesis del asunto
[2-3 frases — la "historia" que vamos a contar]

## Posición procesal actual
[En qué fase está: pre-demanda / contestación pendiente / audiencia previa fijada / esperando sentencia / apelación / ejecución]

## Hitos desde la última actualización
[Eventos de history.md desde el último briefing — fechas + qué ocurrió]

## Próximo plazo crítico
[Fecha + qué hay que hacer + cómputo: "20 días hábiles desde notificación del XX-XX, vence el YY-YY"]

## Cuestiones abiertas
- [pregunta 1 que necesita decisión]
- [pregunta 2 que necesita información del cliente]

## Re-evaluación de riesgo
[Sigue siendo X o ha cambiado? Si cambia, propuesta de nuevo nivel y razón]

## Jurisprudencia clave en el asunto
- [STS o SAP con ECLI/ROJ — punto que sostiene]
- ..

## MASC
[Acreditado sí/no — si no, qué falta]

## Conservación documental
[Acreditada al cliente / pendiente / liberada]
```

### 4. Decision tree

> **¿Qué hago ahora?**
> 1. **Redactar el siguiente escrito** — `/redactar-demanda` / `/redactar-contestacion` / `/recurso-apelacion`
> 2. **Actualizar history con nuevos hitos** — `/actualizar-asunto <slug>`
> 3. **Cronología defensiva u ofensiva** — `/cronologia <slug>`
> 4. **Cuadro de elementos** — `/cuadro-elementos <slug>`
> 5. **Preparar interrogatorio** — `/preparacion-interrogatorio <slug> <nombre>`
> 6. **Tirar de jurisprudencia** — el conector MCP `jurisprudenciator` (`buscar_sentencias`)

## Reglas

1. **No reinventar la tesis.** Si `matter.md` tiene tesis, usarla. Si en `history.md` se cambió, marcarlo.
2. **Cómputo de plazos siempre hábiles** (LEC 133). Sábados no hábiles. Agosto inhábil salvo medidas urgentes.
3. **Pre-flight check** del conector `jurisprudenciator` antes de citar nueva jurisprudencia en el briefing.
4. **No narrar acciones del plugin** ("estoy leyendo history.md..."). Solo el briefing limpio.
