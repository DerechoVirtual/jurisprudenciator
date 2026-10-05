---
name: reclamacion-previa-seguridad-social
description: >-
  Redaccion de la reclamacion previa administrativa frente al INSS/TGSS, requisito de procedibilidad ESPECIFICO de las materias de Seguridad Social, que sustituye a la papeleta de conciliacion (art. 71 LRJS). Basada en plantilla real del despacho, anonimizada. Maneja datos de salud con cuidado. Usar con "reclamacion previa INSS", "reclamacion previa incapacidad", "recurrir resolucion INSS via administrativa", "tramite previo frente al INSS o la TGSS". Solo cuando el demandado es una entidad gestora de la Seguridad Social: si el demandado es la EMPRESA, el tramite previo es la conciliacion ante el SMAC → /papeleta-conciliacion.
---

# Reclamación previa frente al INSS/TGSS

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazos del art. 71 LRJS (interposición, silencio, demanda y especialidades de las altas médicas)** → `buscar_articulo` (`ley="LRJS"`, `articulo="71"`).
- **Preceptos de la LGSS sobre la prestación denegada** (grados de incapacidad, contingencias, incapacidad temporal) → `buscar_articulo` (`ley="LGSS"`, `articulo="194"` o el que corresponda).
- **Normas reglamentarias aplicables** (cuadro de enfermedades profesionales, órdenes de bases y topes de cotización) → `buscar_boe` → `leer_boe`.
- **Criterios para fundar la disconformidad** (coherencia con resoluciones firmes previas, criterios de calificación) → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; `base="AN"` con `tipo_organo="TSJ"` para la Sala del territorio) + `leer_sentencias` (`parrafos=3`). Busca por la cuestión jurídica, nunca con el diagnóstico del cliente.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

> ⚠️ Cuando el asunto es de incapacidad o contingencia, aplican los mismos avisos de datos de salud que `/incapacidad-permanente` y `/seguridad-social-contingencia`: no reproducir diagnósticos reales de terceros en ejemplos.

## Marco normativo

- Art. 71 LRJS: requisito de procedibilidad **específico de las prestaciones de Seguridad Social** antes de demandar al INSS/TGSS/mutua. (Plazos verificados en la redacción vigente del art. 71.)
- **Plazo de interposición**: 30 días desde la notificación de la resolución expresa o desde que deba entenderse producido el silencio (art. 71.2). **Excepción — impugnación de altas médicas**: 11 días; y las altas emitidas al agotarse los 365 días de IT están **exentas** de reclamación previa (art. 71.1).
- **Plazo de contestación de la entidad**: 45 días; transcurridos, silencio negativo (art. 71.5). En altas médicas: 7 días.
- **Plazo para demandar**: 30 días desde la denegación expresa o presunta (art. 71.6). En impugnación de altas médicas: 20 días.
- El recibo de presentación o copia sellada de la reclamación se acompaña **inexcusablemente** con la demanda (art. 71.7).
- Si la entidad debió proceder de oficio y no resolvió, la solicitud del interesado vale como reclamación previa; puede reiterarse si caducó la anterior mientras el derecho no prescriba (art. 71.4).
- Principios de la Ley 39/2015 aplicables supletoriamente: eficacia, celeridad, buena administración — relevante cuando la resolución contradice sin motivación una situación previamente reconocida por sentencia u otra resolución firme.

## Fase 1 — Documentación a pedir

- Resolución que se recurre (fecha de emisión y notificación, número de expediente).
- Antecedentes relevantes (expedientes previos, sentencias relacionadas).
- Informes o documentos que sustenten la disconformidad (sin incorporar diagnósticos completos a la plantilla reutilizable).

## Fase 2 — Estructura del escrito

1. Encabezamiento: Dirección Provincial del INSS/TGSS competente, identificación del reclamante (marcador genérico) y número de expediente.
2. **FUNDAMENTOS**: numerados, exponiendo por qué la resolución no se ajusta a derecho (error en la valoración, incoherencia con resolución previa firme, incumplimiento de plazos por la Administración, etc.).
3. **SOLICITA**: que se tenga por presentada la reclamación previa y se revoque la resolución en el sentido pedido.

**Reparto para la redacción rápida:** documento breve: no necesita equipo; lo redacta el director en un único archivo de `secciones/`, con las consultas lanzadas en paralelo.

## Fase 3 — Entrega

Documento breve, Word (.docx). Recordar con FECHAS CONCRETAS: si no hay respuesta en 45 días o la respuesta es desfavorable, quedan **30 días para demandar** (art. 71.6 LRJS) mediante `/incapacidad-permanente` o `/seguridad-social-contingencia` según la materia — anotar el vencimiento en `_log.yaml` (`next_deadline`).

---

**Nota de anonimización**: cualquier nombre, NIE/DNI, domicilio o número de expediente real de terceros presente en la plantilla de origen se sustituye por marcador genérico y nunca se reproduce.
