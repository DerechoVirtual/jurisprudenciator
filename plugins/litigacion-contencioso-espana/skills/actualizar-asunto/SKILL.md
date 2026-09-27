---
name: actualizar-asunto
description: Añade evento fechado al historial del asunto contencioso-administrativo y refresca el log. Captura notificaciones, entrega del expediente, resoluciones cautelares, cambios de estado y re-evaluaciones de riesgo. Usar con anota en el asunto o actualiza el asunto.
---

# Actualizar asunto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo que abre cada evento de la tabla del § 4** (arts. 46, 52.1, 54.1, 64.1, 85.1, 89.1 y 115.1 LJCA) → `buscar_articulo` (`ley="LJCA"` y el `articulo` del evento) antes de escribir `next_deadline`.
- **Ampliación del expediente incompleto y regla de agosto** → `buscar_articulo` (`ley="LJCA"`, artículos 55 y 128) cuando el evento sea `expediente_administrativo: recibido` o el cómputo cruce agosto.
- **Notificación que el cliente dice no haber recibido** → `novedades_boe` (texto con el órgano y la referencia del expediente, o el NIF si el interesado es una sociedad; periodo de hasta 31 días) + `leer_boe`, para saber si se notificó por edicto en el BOE y desde qué fecha corre el plazo.
- **Re-evaluación de riesgo por una resolución nueva** (cambio de criterio, casación admitida) → `buscar_por_cita` (ECLI o ROJ) + `leer_sentencias` (`parrafos=3`) para anotar en `history.md` el pasaje literal que justifica el cambio.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Anota en [slug] que [evento]"
- "Hubo notificación en [asunto]"
- "Actualiza [asunto] con [hito]"
- Tras notificación de resolución administrativa, decreto del LAJ, auto, providencia o sentencia
- **Tras la entrega del expediente administrativo** — dispara el plazo de demanda del art. 52.1 LJCA
- Tras resolución del incidente de medidas cautelares
- Tras resolución de la alzada o la reposición (agota la vía y abre el plazo del contencioso)
- Tras llamada relevante con cliente, procurador, perito o letrado de la Administración
- Cuando cambia el riesgo, la cuantía o el procedimiento

## Flujo

### 1. Identificar asunto

Si no se da slug, pedir.

### 2. Capturar evento

Vía `AskUserQuestion` o input directo:

- **Tipo de evento:**
  - **Notificación administrativa recibida** (resolución sancionadora, resolución de alzada/reposición, requerimiento, acuerdo de inicio)
  - **Silencio administrativo producido** (fecha en que se cumple el plazo → nace el acto presunto)
  - **Notificación judicial recibida** (decreto de admisión, auto, providencia, sentencia)
  - **Escrito presentado** (interposición, demanda, contestación, conclusiones, recurso)
  - **Expediente administrativo:** reclamado / recibido / incompleto → ampliación pedida (art. 55 LJCA)
  - **Medida cautelar:** solicitada / concedida / denegada
  - Vista celebrada (abreviado o DDFF)
  - Comunicación con cliente
  - Comunicación con procurador / perito / letrado de la Administración
  - Cambio de tesis / estrategia
  - Re-evaluación de riesgo
  - Cambio de cuantía, procedimiento u órgano
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
  - Cómputo del plazo derivado, escrito
  - Próximo paso derivado
```

Ej.:
```
[2026-05-13] NOTIFICACIÓN ADMINISTRATIVA — Resolución del recurso de reposición, desestimatoria.
  - Agota la vía administrativa. via_previa: agotada.
  - Plazo de interposición del contencioso: 2 meses desde el día siguiente (art. 46.4 LJCA).
  - fecha_caducidad_interposicion: 2026-07-13 (confirmada en doble control).
  - CADUCIDAD, no prescripción: ninguna gestión extrajudicial la interrumpe.
  - Próximo paso: escrito de interposición (art. 45 LJCA) + documentos del art. 45.2.
```

```
[2026-06-02] EXPEDIENTE RECIBIDO — Entregado el expediente administrativo (312 folios, índice autentificado).
  - Dispara el plazo de demanda: 20 días desde la entrega (art. 52.1 LJCA). Vence el 2026-06-30.
  - Faltan los informes técnicos previos → valorar art. 55 LJCA dentro de los 10 primeros días.
  - Próximo paso: /demanda-contencioso-administrativa.
```

#### A `matters/_log.yaml` — actualizar fila

- `last_updated`: hoy
- `next_deadline`: nuevo si cambió
- `risk`: nuevo si re-evaluado (con `severity floor`: no se demota silenciosamente)
- Campos propios del contencioso que este evento puede mover:
  - `via_previa` → agotada / pendiente-alzada / pendiente-reposición / no-procede
  - `fecha_notificacion` y `fecha_caducidad_interposicion` (si el acto notificado es uno nuevo)
  - `expediente_administrativo` → no-reclamado / reclamado / recibido / incompleto-ampliación-pedida
  - `medida_cautelar` → no-pedida / pedida / concedida / denegada
  - `procedimiento`, `organo`, `cuantia`, `cuantia_determinada`

### 4. Eventos que disparan cómputo — escribirlo siempre

| Evento | Plazo que abre | Norma |
|---|---|---|
| Notificación del acto expreso que agota la vía | **2 meses** para interponer | art. 46.1 LJCA |
| Acto presunto producido | **6 meses** para interponer | art. 46.1 LJCA |
| Resolución (o silencio) de la reposición | **2 meses** para interponer | art. 46.4 LJCA |
| Vía de hecho, con requerimiento previo | **10 días** | art. 46.3 LJCA |
| Vía de hecho, sin requerimiento | **20 días** | art. 46.3 LJCA |
| **Entrega del expediente** | **20 días** para la demanda | art. 52.1 LJCA |
| Traslado de la demanda | **20 días** para contestar | art. 54.1 LJCA |
| Requerimiento de subsanación art. 45.2 | **10 días** | art. 45.3 LJCA |
| Traslado para conclusiones | **10 días** | art. 64.1 LJCA |
| Notificación de sentencia apelable | **15 días** para apelar | art. 85.1 LJCA |
| Notificación de sentencia recurrible en casación | **30 días** para preparar | art. 89.1 LJCA |
| Tenido por preparado el recurso de casación | **15 días** para comparecer ante el TS | art. 89.5 LJCA |
| Acto lesivo de derechos fundamentales | **10 días** para interponer (agosto hábil) | art. 115.1 LJCA |

**Ampliación del expediente incompleto (art. 55 LJCA)** — regla que hay que anotar bien:
- La solicitud **suspende** el curso del plazo de demanda o contestación; el LAJ resuelve en **3 días**.
- Si se pide **dentro de los 10 primeros días** del plazo y se acepta → el plazo se **reinicia** desde que el expediente completo se pone a disposición.
- Si se pide después de esos 10 días, o se rechaza → el plazo simplemente se **reanuda**.
- Por eso: cuando se anota `expediente_administrativo: recibido`, revisar el índice **de inmediato**, no el día 15.

### 5. Si la re-evaluación demota riesgo

Aplicar regla de severity floor:
- Si el nuevo riesgo es MENOR que el anterior, exigir razón explícita.
- Registrar en `history.md`: "Riesgo bajado de Alto a Medio porque [razón]."
- En `_log.yaml` queda el riesgo nuevo; `history.md` preserva la razón.

### 6. Output

```
✅ Anotado en [slug].

**Evento:** [tipo + fecha]
**History.md:** entrada añadida
**Log:** last_updated actualizado [, next_deadline a XX-XX] [, via_previa a X] [, expediente_administrativo a Y] [, risk de X a Y]

**Siguiente plazo:** [fecha + acción + cómputo]
```

### 7. Decision tree (opcional)

Si el evento implica acción inmediata:

> **¿Hago algo más?**
> 1. **Redactar el escrito que toca** — `/interposicion-recurso-contencioso-ca`, `/demanda-contencioso-administrativa`, `/escrito-conclusiones-ca`, `/recurso-apelacion-ca`
> 2. **Pedir la ampliación del expediente** — si el índice revela huecos, y estamos en los 10 primeros días
> 3. **Pedir medida cautelar** — `/medidas-cautelares-ca` si el acto va a ejecutarse
> 4. **Comunicar al cliente** — borrador con el evento y el siguiente paso
> 5. **Solo registrarlo** — ya hecho, sin acción inmediata

## Reglas

1. **History append-only.** Si una entrada anterior estuvo mal, añadir entrada de corrección. NO editar.
2. **Fechas absolutas.** "Mañana" → fecha absoluta calculada desde hoy.
3. **Agosto: art. 128.2 LJCA.** Durante agosto **no corre** el plazo de interposición **ni ningún otro plazo de la LJCA**, **salvo en el procedimiento de derechos fundamentales, donde agosto SÍ es hábil** (el plazo de 10 días del art. 115.1 corre en agosto). No citar el art. 133 LEC: es la regla civil.
4. **Los plazos de interposición son de CADUCIDAD.** Ningún evento extrajudicial —burofax, reclamación, llamada, escrito a la Administración— los interrumpe. Si se anota una gestión de ese tipo, no tocar `fecha_caducidad_interposicion` y decirlo expresamente.
5. **La fecha de notificación no se estima.** Si el cliente "cree que fue por ahí", anotarlo como estimación explícita y pedir el justificante. De ese dato depende la admisibilidad del recurso.
6. **Cambios de cuantía disparan re-evaluación** de procedimiento y de vía de recurso: cruzar el umbral de **30.000 €** cambia el abreviado a ordinario (art. 78.1 LJCA) y abre la apelación (art. 81.1.a LJCA). Anotar ambas consecuencias.
7. **Cambios de órgano** (de Juzgado a Sala) hacen **preceptivo el procurador** (art. 23.2 LJCA). Anotarlo y actualizar `procurador`.
8. **Nunca registrar eventos MASC.** No existen en esta jurisdicción. Si un evento parece MASC, es agotamiento de la vía administrativa: registrarlo en `via_previa`.
