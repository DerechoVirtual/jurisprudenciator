---
name: recurso-suplicacion
description: >-
  Redaccion del recurso de suplicacion ANTE el TSJ contra sentencias del Juzgado de lo Social, y del escrito de impugnacion por la parte recurrida. Basada en plantilla real del despacho, anonimizada. Usar con "recurso de suplicacion", "recurrir la sentencia del Juzgado de lo Social", "impugnar suplicacion", "anuncio de suplicacion". Requisito previo: la sentencia recurrida es la de INSTANCIA (Juzgado de lo Social). Si la sentencia que se quiere recurrir es la ya dictada por el TSJ resolviendo una suplicacion, el cauce es el RCUD ante el Tribunal Supremo → /recurso-casacion-unificacion-doctrina.
---

# Recurso de suplicación — flujo maestro

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Recurribilidad, plazos, depósito y consignación** (arts. 191, 193-197 y 229-230 LRJS) → `buscar_articulo` (`ley="LRJS"`, `articulo="191"`).
- **Infracción de jurisprudencia del motivo del art. 193.c)** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`, `terminos` del punto infringido).
- **Criterio de la Sala de suplicación competente y posibles sentencias de contraste para un futuro RCUD** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia`).
- **Normas sustantivas infringidas** → `buscar_articulo` (ET, LGSS...) y, si la infracción es del convenio, `leer_convenio` (`articulo`).
- **Verificación antes de entregar** → `buscar_por_cita` sobre toda sentencia citada y `verificar_escrito` con el texto completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Marco normativo

- Regulado en los arts. 190-204 LRJS (disposiciones comunes a los recursos: arts. 229-235).
- **Recurribilidad** (art. 191 LRJS): siempre en despido y extinción de contrato, prestaciones de Seguridad Social y grado de incapacidad, conflictos colectivos, tutela DDFF y demás supuestos del art. 191.3; por razón de cuantía, solo si lo litigioso **excede de 3.000 €** (art. 191.2.g). Excluidos: sanciones no muy graves, fecha de vacaciones, clasificación profesional, MSCT no colectiva, impugnación de alta médica, entre otros (art. 191.2).
- **Trámite y plazos**: **anuncio en 5 días** desde la notificación de la sentencia ante el propio Juzgado (art. 194); **interposición en 10 días** desde que se notifica la puesta a disposición de los autos al letrado/graduado social (art. 195.1); traslado a las recurridas para **impugnación en 5 días** (art. 197.1). Contra el auto que tiene por no anunciado el recurso: queja ante la Sala del TSJ (art. 195.2).
- **Depósito y consignación si recurre la empresa** (arts. 229-230 LRJS): depósito de 300 € y consignación del importe de la condena (o aval solidario). El trabajador y los beneficiarios de Seguridad Social están exentos.
- **Motivos tasados** (art. 193 LRJS): a) reposición de autos por quebrantamiento de forma; b) revisión de hechos probados con base en prueba documental o pericial que obre en autos; c) infracción de normas sustantivas o de la jurisprudencia.
- **Costas** (art. 235 LRJS): la sentencia que desestime el recurso impondrá las costas al recurrente vencido (salvo que goce del beneficio de justicia gratuita), con honorarios del letrado impugnante hasta el límite legal.
- **Otrosíes habituales**: designación de domicilio a efectos de notificaciones del letrado/a firmante en la sede de la Sala, y constancia de firmeza de sentencias de contraste si el asunto puede acabar en RCUD (art. 221.3 LRJS).

## Fase 1 — Documentación a pedir

- Sentencia recurrida (fecha, Juzgado, número de autos).
- Escrito de anuncio del recurso y providencia/diligencia teniéndolo por preparado.
- Hechos probados de la sentencia que se quieren revisar, con la prueba documental/pericial concreta en que se basa la revisión pretendida.
- Normas o jurisprudencia que se consideran infringidas.

## Fase 2 — Batería de preguntas

- ¿Es recurrible la sentencia? Comprobar materia y cuantía (art. 191 LRJS) ANTES de redactar nada.
- ¿Quién recurre? Si es la empresa: advertir del depósito de 300 € y de la consignación de la condena (arts. 229-230 LRJS).
- ¿Qué motivo(s) del art. 193 LRJS se invocan? (puede ser más de uno, en orden: forma → hechos → derecho).
- Si se pide revisión de hechos probados (193.b): ¿qué documento/pericial concreta del expediente lo sustenta? (no cabe revisión basada en nueva valoración de prueba testifical) — proponer redacción alternativa LITERAL del hecho probado.
- ¿Qué infracción sustantiva o jurisprudencial se alega (193.c)? Localizar y verificar la jurisprudencia antes de citarla.
- Datos del procedimiento (Juzgado de origen, número de autos, Sala del TSJ competente).
- ¿Estamos recurriendo o impugnando el recurso de la contraria? (la impugnación tiene su propio plazo de 5 días y puede incluir rectificaciones de hechos y causas de oposición subsidiarias — art. 197.1).

## Fase 3 — Estructura del escrito

1. Encabezamiento: Sala de lo Social del TSJ competente, identificación de quien recurre (letrado/a y poderdante, con marcadores genéricos), identificación de la sentencia recurrida.
2. Cumplimiento de trámites procesales (recurribilidad, plazo, anuncio previo) — art. 191 y ss. LRJS.
3. **Motivos del recurso**, numerados y con encabezado claro de cada uno (ej. "MOTIVO PRIMERO, al amparo del art. 193.b) LRJS, por error en la apreciación de la prueba...").
4. **SUPLICO**: que se admita el recurso, se revoque/modifique la sentencia recurrida en el sentido pedido.
5. **OTROSÍES**: designación de domicilio profesional del letrado/a (marcador genérico), y cualquier manifestación adicional exigida por el art. 221 LRJS si hay conexión con un futuro recurso de casación.

## Fase 4 — Verificación y entrega

Verificación jurisprudencial obligatoria de toda sentencia de contraste con `buscar_por_cita`. Pulir con `/estilo-escritos-judiciales`. Entregar en Word (.docx).

---

**Nota de anonimización**: cualquier dato real de letrado/a, colegiado, domicilio o partes presente en la plantilla de origen se sustituye por marcador genérico.
