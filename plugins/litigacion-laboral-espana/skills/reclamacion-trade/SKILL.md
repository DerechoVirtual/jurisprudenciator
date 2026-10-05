---
name: reclamacion-trade
description: >-
  Redaccion de demanda de resolucion de contrato del Trabajador Autonomo Economicamente Dependiente (TRADE) por incumplimiento de la empresa y reclamacion de cantidad por facturas impagadas y danos y perjuicios. Basada en plantilla real del despacho, anonimizada. Usar con "TRADE", "trabajador autonomo dependiente", "resolucion contrato TRADE", "reclamacion facturas TRADE", "soy autonomo y facturo casi todo a un solo cliente". Requisito previo: el reclamante es TRADE (autonomo con contrato TRADE registrado y dependencia economica del art. 11 LETA), no trabajador por cuenta ajena. Si hay relacion laboral y nominas impagadas, usar /reclamacion-cantidad.
---

# Reclamación TRADE — resolución de contrato e indemnización

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen del TRADE (arts. 11-18 LETA, causas de extinción e indemnización del art. 15) y competencia del orden social (art. 2.d LRJS)** → `buscar_articulo` (`ley="Ley 20/2007"`, `articulo="15"`; `ley="LRJS"`, `articulo="2"`).
- **RD 197/2009 de desarrollo** (contrato TRADE y su registro) → `buscar_boe` → `leer_boe`.
- **Empresa cliente y cambios societarios que motivan la resolución** (denominación, CIF, domicilio, administradores, venta, fusión o cambio de socio) → `buscar_empresa_mercantil` y, para el acto inscrito concreto, `sumario_borme` → `leer_boe`.
- **Plazo de prescripción de las facturas impagadas** → `buscar_articulo` (`ley="CC"`, `articulo="1964"`).
- **Doctrina sobre la condición de TRADE y el incumplimiento del cliente** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; `base="AN"` con `tipo_organo="TSJ"`) + `leer_sentencias` (`parrafos=3`).
- **Comprobación de las citas** → cada redactor lee con `leer_sentencias` las sentencias que cita y pasa `verificar_escrito` solo sobre sus frases con normas; el ensamblado de `redaccion-rapida` rechaza cualquier ECLI o ROJ que nadie haya leído.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

## Marco normativo

- **Ley 20/2007, del Estatuto del Trabajo Autónomo (LETA)** — arts. 11-18 (régimen TRADE: al menos el 75% de los ingresos de un único cliente; contrato registrado) y **RD 197/2009** de desarrollo.
- Competencia: la jurisdicción social conoce de los litigios entre TRADE y su cliente principal derivados del contrato (art. 2.d LRJS; art. 17 LETA).
- Causas de extinción por voluntad del TRADE fundada en incumplimiento del cliente: art. 15.1.c LETA (con derecho a indemnización, art. 15.4). Supuestos típicos: impago reiterado de facturas, incumplimiento de condiciones del contrato registrado, modificación unilateral sustancial (p. ej. tras una venta/cambio de titularidad de la empresa cliente).
- Conciliación previa: exigible (arts. 63-65 LRJS) — vía papeleta ante el SMAC (`/papeleta-conciliacion`). Si hay acuerdo de interés profesional con procedimiento propio, comprobar el compromiso arbitral (art. 65.3-65.4 LRJS y art. 18 LETA).
- **Plazo de la reclamación de cantidad**: la acción por facturas impagadas no goza del régimen del art. 59 ET; aplicar la prescripción civil de las acciones (verificar plazo vigente aplicable al caso — regla general art. 1964 CC) y valorarlo asunto por asunto.

## Fase 1 — Documentación a pedir

- Contrato TRADE registrado (fecha, condiciones).
- Facturas emitidas y su estado de pago (fecha de emisión, fecha de cobro real, importes bruto/neto pendientes).
- Comunicaciones sobre cambios societarios o de condiciones (venta de la empresa, cambio de grupo).
- Certificado de conciliación.

## Fase 2 — Comprobaciones previas

Se responden con la documentación aportada (paso 2 de `redaccion-rapida`). Solo se pregunta al abogado lo que bloquee la estructura del escrito y no se deduzca de lo aportado, en una única ronda de como máximo cuatro preguntas; lo demás que falte se deja como `[PENDIENTE: dato]`.

- ¿Cuál es la causa de la resolución? impago reiterado / incumplimiento de condiciones / modificación unilateral.
- Relación exacta de facturas impagadas o pagadas con retraso (fecha emisión, fecha de pago real, importe bruto y neto).
- ¿Se reclama también indemnización por daños y perjuicios además de las cantidades adeudadas?
- Antigüedad de la relación TRADE y condiciones pactadas inicialmente.

## Fase 3 — Estructura del escrito

1. Encabezamiento: Juzgado de lo Social (o Tribunal de Instancia, Sección Social, según nomenclatura vigente) competente, parte actora, parte demandada (empresa cliente, con marcadores genéricos para datos reales).
2. **HECHOS**: naturaleza de la relación TRADE (fecha de inicio, normativa aplicable) → hechos que motivan la resolución (impagos con fechas e importes concretos, cambios societarios, incumplimientos) → cuantificación de lo adeudado → acreditación de conciliación previa.
3. **FUNDAMENTOS DE DERECHO**: jurisdicción y competencia → legitimación → aplicación de la Ley 20/2007 y RD 197/2009 → causa de resolución imputable a la empresa por analogía/remisión al régimen de incumplimientos contractuales graves → cuantificación de la reclamación de cantidad.
4. **SUPLICO**: declarar resuelto el contrato TRADE por incumplimiento de la empresa, condena al pago de las cantidades adeudadas por servicios prestados y, en su caso, indemnización por daños y perjuicios.
5. **OTROSÍES**: asistencia letrada, proposición de prueba documental (facturas, contrato) y testifical.

**Reparto para la redacción rápida:** 01 encabezamiento y hechos; 02 fundamentos procesales (jurisdicción, competencia, legitimación, conciliación previa); 03 resolución del contrato TRADE por incumplimiento (Ley 20/2007, RD 197/2009 y doctrina); 04 reclamación de cantidad, daños y perjuicios, suplico y otrosíes.

## Fase 4 — Verificación y entrega

El estilo de la casa (`estilo-escritos-judiciales`) lo aplican los redactores al escribir, sin pasada posterior. Entrega en Word (.docx) con el ensamblado de `redaccion-rapida`.

---

**Nota de anonimización**: cualquier dato real de empresa, grupo comprador, letrado/a o cliente se sustituye por marcador genérico.
