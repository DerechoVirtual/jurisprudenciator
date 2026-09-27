---
name: actualizar-asunto
description: Añade evento fechado al historial del asunto y refresca el log. Captura notificaciones, cambios de estado, re-evaluaciones de riesgo. Usar con anota en el asunto o actualiza el asunto.
---

# Actualizar asunto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Nuevo plazo que abre el evento (contestación, recurso, oposición): precepto vigente que lo fija y su cómputo en días hábiles** → `buscar_articulo` (`ley="LEC"`; `articulo="133"` para el cómputo).
- **Cambio de cuantía que obliga a revisar procedimiento y postulación (arts. 23, 249 y 250 LEC)** → `buscar_articulo` (`ley="LEC"`).
- **Evento que afecta a una contraparte sociedad (cambio de denominación, domicilio o administradores, disolución, concurso)** → `buscar_empresa_mercantil` (por nombre o CIF).
- **Edicto, notificación o anuncio de subasta del asunto publicado en el BOE** → `novedades_boe` (por texto o NIF, periodo de hasta 31 días) → `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- "Anota en [slug] que [evento]"
- "Hubo notificación en [asunto]"
- "Actualiza [asunto] con [hito]"
- Tras notificación de demanda, auto, sentencia, decreto del LAJ
- Tras burofax enviado o recibido
- Tras llamada relevante con cliente / contraparte / procurador
- Cuando cambia el riesgo o la cuantía

## Flujo

### 1. Identificar asunto

Si no se da slug, pedir.

### 2. Capturar evento

Vía `AskUserQuestion` o input directo:

- **Tipo de evento:**
  - Notificación recibida (demanda / auto / sentencia / decreto / providencia)
  - Notificación enviada (presentación de escrito)
  - Comunicación con cliente
  - Comunicación con contraparte / procurador / perito
  - Audiencia / vista celebrada
  - MASC celebrado
  - Cambio de tesis / estrategia
  - Re-evaluación de riesgo
  - Cambio de cuantía o pretensión
  - Otro
- **Fecha del evento** (default: hoy)
- **Resumen breve** (1-3 frases)
- **¿Cambia próximo plazo?** Si sí, capturar nueva fecha + qué corresponde
- **¿Cambia riesgo?** Si sí, capturar nuevo nivel + razón

### 3. Escribir entradas

#### A `matters/<slug>/history.md` — append-only

```
[AAAA-MM-DD] [TIPO] — [resumen]
  - Detalle adicional si procede
  - Próximo paso derivado
```

Ej:
```
[2026-05-13] NOTIFICACIÓN RECIBIDA — Auto admitiendo demanda y emplazando al demandado.
  - Plazo de contestación: 20 días hábiles desde notificación (hoy).
  - Vence el 2026-06-10 (excluido sábado y domingo, agosto no aplica).
  - Próximo paso: redactar contestación; pedir más documentación al cliente.
```

#### A `matters/_log.yaml` — actualizar fila

- `last_updated`: hoy
- `next_deadline`: nuevo si cambió
- `risk`: nuevo si re-evaluado (con `severity floor`: no se demota silenciosamente)
- `cuantia`: actualizado si cambió

### 4. Si la re-evaluación demota riesgo

Aplicar regla de severity floor:
- Si el nuevo riesgo es MENOR que el anterior, exigir razón explícita.
- Registrar en history.md la razón explícita: "Riesgo bajado de Alto a Medio porque [razón]."
- En `_log.yaml`, mantener el riesgo nuevo pero el history.md preserva la razón.

### 5. Output

```
✅ Anotado en [slug].

**Evento:** [tipo + fecha]
**History.md:** entrada añadida
**Log:** last_updated actualizado [, next_deadline a XX-XX] [, risk de X a Y]

**Siguiente plazo:** [fecha + acción]
```

### 6. Decision tree (opcional)

Si el evento implica acción inmediata:

> **¿Hago algo más?**
> 1. **Redactar la respuesta** — si llegó demanda/auto, redactar contestación/recurso
> 2. **Comunicar al cliente** — borrador de email con el evento y siguiente paso
> 3. **Pedir documentación adicional** — si el evento revela hueco probatorio
> 4. **Solo registrarlo** — ya hecho, sin acción inmediata

## Reglas

1. **History append-only.** Si una entrada anterior estuvo mal, añadir entrada de corrección. NO editar.
2. **Fechas absolutas.** "Mañana" → fecha absoluta calculada desde hoy.
3. **Cómputo de plazos hábiles** según LEC 133 (excluir sábados, domingos, festivos, agosto inhábil salvo materias urgentes).
4. **Cambios de cuantía** disparan re-evaluación de jurisdicción/procedimiento. Si pasa de >2000€ a <2000€ procurador deja de ser preceptivo; si pasa de <15000€ a >15000€, cambia de verbal a ordinario.
