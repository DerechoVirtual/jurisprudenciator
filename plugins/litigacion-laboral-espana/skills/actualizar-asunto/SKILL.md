---
name: actualizar-asunto
description: Añade evento fechado al historial del asunto y refresca el log. Captura notificaciones, cambios de estado, re-evaluaciones de riesgo. Usar con anota en el asunto o actualiza el asunto.
---

# Actualizar asunto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo que abre la notificación** (anuncio de suplicación, impugnación, preparación del RCUD, reclamación previa, reanudación de la caducidad tras el acto de conciliación) → `buscar_articulo` (`ley="LRJS"`, `articulo="194"`, `"197"`, `"220"`, `"71"` o `"65"`).
- **Recurribilidad cuando cambia la cuantía** → `buscar_articulo` (`ley="LRJS"`, `articulo="191"`).
- **Evento que revela concurso o cambio societario de la empresa** → `buscar_empresa_mercantil` y `novedades_boe` (nombre o NIF de la empresa).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- "Anota en [slug] que [evento]"
- "Hubo notificación en [asunto]"
- "Actualiza [asunto] con [hito]"
- Tras notificación de citación, auto, sentencia, decreto del LAJ
- Tras presentar papeleta SMAC o reclamación previa, o tras el acto de conciliación
- Tras llamada relevante con cliente / contraparte / colaborador
- Cuando cambia el riesgo o la cuantía

## Flujo

### 1. Identificar asunto

Si no se da slug, pedir.

### 2. Capturar evento

Vía `AskUserQuestion` o input directo:

- **Tipo de evento:**
  - Notificación recibida (citación a juicio / auto / sentencia / decreto / providencia / resolución INSS)
  - Notificación enviada (presentación de papeleta, demanda o escrito)
  - Comunicación con cliente
  - Comunicación con contraparte / colaborador / perito
  - Acto de conciliación (SMAC o judicial) / juicio celebrado
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
[2026-05-13] NOTIFICACIÓN RECIBIDA — Sentencia estimatoria parcial del despido (improcedencia, no nulidad).
  - Anuncio de suplicación: 5 días hábiles desde notificación (art. 194 LRJS).
  - Vence el 2026-05-20 (excluidos sábados, domingos y festivos).
  - Próximo paso: decidir con el cliente si se recurre; si anuncia la contraria, preparar impugnación (5 días, art. 197 LRJS).
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
3. **Cómputo de plazos hábiles** según art. 43 LRJS (excluir sábados, domingos y festivos; agosto y 24-dic a 6-ene inhábiles salvo las modalidades urgentes del art. 43.4: despido, extinción, MSCT, vacaciones, tutela DDFF, conflictos colectivos, etc.).
4. **Cambios de cuantía** disparan re-evaluación de recurribilidad: por debajo de 3.000 € la sentencia NO tendrá suplicación por razón de cuantía (art. 191.2.g LRJS), salvo que la materia la garantice (despido, prestaciones SS, etc. — art. 191.3).
