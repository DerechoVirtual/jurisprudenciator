---
name: seguridad-social-contingencia
description: >-
  Redaccion de demanda en materia de Seguridad Social sobre determinacion de CONTINGENCIA (accidente de trabajo/enfermedad profesional frente a enfermedad comun), incluidos supuestos de burnout y otras patologias derivadas del trabajo, frente al INSS, TGSS, empresa y mutua. Basada en plantilla real del despacho, anonimizada. Maneja datos de salud con extremo cuidado. Usar con "determinacion de contingencia", "que se declare accidente de trabajo", "enfermedad profesional", "burnout laboral", "demanda mutua". El objeto del pleito es el ORIGEN de la dolencia, no el grado: si lo que se reclama es la declaracion de incapacidad permanente total, absoluta o gran invalidez, usar /incapacidad-permanente.
---

# Demanda de determinación de contingencia (accidente de trabajo / enfermedad profesional)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Arts. 156-157 LGSS (presunción del art. 156.3) y arts. 71, 72 y 140-147 LRJS en su redacción vigente** → `buscar_articulo` (`ley="LGSS"`, `articulo="156"`).
- **Cuadro de enfermedades profesionales (RD 1299/2006) y sus modificaciones** → `buscar_boe` → `leer_boe`.
- **Doctrina sobre patologías psicosociales como accidente de trabajo, que varía por Sala y año** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"` y `base="AN"` con `tipo_organo="TSJ"`, `fecha_desde` reciente) + `leer_sentencias` (`parrafos=3`, `terminos="presunción de laboralidad"`).
- **Empresa codemandada** (denominación exacta, CIF, domicilio social) → `buscar_empresa_mercantil`.
- **Mejoras voluntarias del convenio ligadas a la contingencia profesional** (complemento de incapacidad temporal, indemnización por accidente) → `buscar_convenio` + `leer_convenio` (`buscar_en="accidente de trabajo"`).
- **Comprobación de las citas** → cada redactor lee con `leer_sentencias` las sentencias que cita y pasa `verificar_escrito` solo sobre sus frases con normas; el ensamblado de `redaccion-rapida` rechaza cualquier ECLI o ROJ que nadie haya leído.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

> ⚠️ Mismo aviso que `/incapacidad-permanente`: datos de salud, tratar con extremo cuidado, nunca reproducir diagnósticos reales de casos anteriores en plantillas de ejemplo.

## Marco normativo

- Distinción de contingencias: **accidente de trabajo** (art. 156 LGSS, incluye la presunción de laboralidad del art. 156.3 para lesiones sufridas durante tiempo y lugar de trabajo), **enfermedad profesional** (art. 157 LGSS, listado del RD 1299/2006) y **enfermedad común**. La calificación determina la base reguladora, el régimen de recargos y responsabilidades, y el acceso a determinadas prestaciones.
- **Patologías psicosociales (burnout, ansiedad, depresión de origen laboral)**: no están en el listado cerrado de enfermedades profesionales del RD 1299/2006, por lo que la vía habitual es reclamar su calificación como **accidente de trabajo** (no enfermedad profesional) invocando la presunción de laboralidad del art. 156.3 LGSS cuando la patología se manifiesta en tiempo y lugar de trabajo, y acreditando el nexo causal entre las condiciones/organización del trabajo y el cuadro clínico.
- Legitimados pasivos habituales: INSS, TGSS, la empresa y la mutua colaboradora con la Seguridad Social (ésta última asume la gestión de la contingencia profesional si se reconoce como tal) — el litisconsorcio incompleto es causa clásica de suspensión del juicio: identificarlos TODOS desde el principio.
- Requiere reclamación previa (`/reclamacion-previa-seguridad-social`); tras su denegación expresa o silencio (45 días), demanda en 30 días (art. 71.6 LRJS). Modalidad procesal: arts. 140-147 LRJS (expediente administrativo reclamado de oficio, art. 143; vinculación a los hechos del expediente, art. 72).

## Fase 1 — Documentación a pedir

- Resolución que califica la contingencia como común (la que se recurre).
- Informes médicos y, si existen, informes de servicios de prevención/mutua sobre la relación entre el puesto de trabajo y la patología.
- Descripción de las condiciones de trabajo relevantes (carga, organización, exposición a factores de riesgo psicosocial) — a aportar por el usuario, sin que la skill invente hechos.
- Certificado de reclamación previa.

## Fase 2 — Comprobaciones previas

Se responden con la documentación aportada (paso 2 de `redaccion-rapida`). Solo se pregunta al abogado lo que bloquee la estructura del escrito y no se deduzca de lo aportado, en una única ronda de como máximo cuatro preguntas; lo demás que falte se deja como `[PENDIENTE: dato]`.

- ¿Qué contingencia se reclama? accidente de trabajo (vía presunción de laboralidad) / enfermedad profesional (si encaja en listado RD 1299/2006).
- ¿La patología se manifestó en tiempo y lugar de trabajo, o existe nexo causal razonado aunque no fuera en el momento exacto?
- ¿Hay parte de accidente de trabajo previo, informe de servicio de prevención, o denuncia ante inspección de trabajo?
- Legitimados pasivos exactos: INSS, TGSS, empresa, mutua (identificar cuál).

## Fase 3 — Estructura del escrito

1. Encabezamiento: Juzgado de lo Social, parte actora (marcador genérico), codemandados (INSS, TGSS, empresa, mutua — todos con marcador genérico salvo que el usuario aporte los datos reales de su asunto).
2. **HECHOS**: relación laboral y puesto de trabajo → circunstancias en que se manifestó la patología → resolución que calificó la contingencia como común y por qué se discrepa → elementos que acreditan el nexo causal con el trabajo.
3. **FUNDAMENTOS DE DERECHO**: jurisdicción y competencia → arts. 156-157 LGSS → presunción de laboralidad del art. 156.3 LGSS si aplica → doctrina jurisprudencial sobre patologías psicosociales y su calificación como accidente de trabajo (verificar cita vía jurisprudenciator, este es un terreno donde la jurisprudencia varía por Sala/año — no asumir un criterio fijo sin comprobarlo).
4. **SUPLICO**: revocar la resolución y declarar que la contingencia es accidente de trabajo (o enfermedad profesional, según el caso), con los efectos prestacionales correspondientes.

**Reparto para la redacción rápida:** 01 encabezamiento, comparecencia y hechos (puesto de trabajo, circunstancias de la patología, resolución recurrida y nexo causal); 02 fundamentos procesales (jurisdicción, competencia, reclamación previa y legitimados pasivos); 03 contingencia: arts. 156-157 LGSS, presunción de laboralidad y doctrina sobre patologías psicosociales; 04 cierre (suplico y firma).

## Fase 4 — Verificación y entrega

Verificación jurisprudencial obligatoria antes de citar ningún criterio sobre burnout/patologías psicosociales — es una materia con doctrina evolutiva: la hace el redactor de esa sección leyendo las sentencias (el ensamblado rechaza las citas que nadie leyó). El estilo de la casa (`estilo-escritos-judiciales`) lo aplican los redactores al escribir, sin pasada posterior. Entrega en Word (.docx) con el ensamblado de `redaccion-rapida`.
