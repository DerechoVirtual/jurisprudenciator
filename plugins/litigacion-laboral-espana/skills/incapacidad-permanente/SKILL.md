---
name: incapacidad-permanente
description: >-
  Redaccion de demanda en reclamacion del GRADO de incapacidad permanente (total, absoluta o gran invalidez), incluidas revisiones por mejoria y recalificaciones de grado, frente al INSS. Basada en plantilla real del despacho, anonimizada. Maneja datos de salud con extremo cuidado. Usar con "incapacidad permanente", "incapacidad absoluta", "incapacidad total", "revision de grado", "me han denegado la incapacidad". El objeto del pleito es el GRADO reconocido. Si lo que se discute es el ORIGEN de la dolencia (accidente de trabajo o enfermedad profesional frente a enfermedad comun), ese es un litigio distinto y previo → /seguridad-social-contingencia.
---

# Demanda de incapacidad permanente frente al INSS

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Arts. 193-194 LGSS (grados) y arts. 71, 72, 140-147 y 191.3.c) LRJS en su redacción vigente** → `buscar_articulo` (`ley="LGSS"`, `articulo="194"`; `ley="LRJS"`, `articulo="71"`).
- **Doctrina sobre criterios de calificación del grado y concepto de profesión habitual** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; para supuestos análogos de la Sala del territorio, `base="AN"` con `tipo_organo="TSJ"` y `provincia`) + `leer_sentencias` (`parrafos=3`, `terminos="profesión habitual"`). Busca por la cuestión jurídica y las limitaciones funcionales, nunca con datos de salud del cliente.
- **Funciones de la categoría profesional del actor, para acreditar las exigencias de su profesión habitual** → `buscar_convenio` + `leer_convenio` (`buscar_en="clasificación profesional"`).
- **Mejoras voluntarias del convenio por incapacidad permanente** (indemnización o seguro colectivo, reclamables aparte) → `leer_convenio` (`buscar_en="incapacidad permanente"`).
- **Comprobación de las citas** → cada redactor lee con `leer_sentencias` las sentencias que cita y pasa `verificar_escrito` solo sobre sus frases con normas; el ensamblado de `redaccion-rapida` rechaza cualquier ECLI o ROJ que nadie haya leído.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

> ⚠️ **Datos especialmente sensibles.** Esta skill maneja información de salud (categoría especial de datos personales, art. 9 RGPD). Nunca reproducir en ejemplos, plantillas de referencia o registros diagnósticos reales de casos anteriores, iniciales que permitan identificar a una persona, ni informes médicos completos de terceros. Trabajar siempre sobre los datos concretos que el usuario aporte para SU asunto actual, con marcadores genéricos en cualquier ejemplo o plantilla reutilizable.

## Marco normativo

- Grados de incapacidad permanente (arts. 193-194 LGSS — RDLeg 8/2015): parcial, total (para la profesión habitual), absoluta (para toda profesión u oficio), gran invalidez.
- Procedimiento: reclamación previa obligatoria (`/reclamacion-previa-seguridad-social`) y, tras su denegación expresa o por silencio (45 días), **demanda en el plazo de 30 días** (art. 71.6 LRJS) — este plazo es el que más demandas de IP mata: calcularlo y anotarlo SIEMPRE.
- Modalidad procesal de prestaciones de Seguridad Social: arts. 140-147 LRJS. El órgano judicial reclama de oficio el **expediente administrativo** (art. 143); en juicio no pueden aducirse hechos distintos a los alegados en el expediente (art. 72 LRJS) — la reclamación previa fija el perímetro del pleito.
- Competencia: Juzgado de lo Social / Sección de lo Social del Tribunal de Instancia, a elección del demandante, del domicilio del actor o de la sede del órgano que dictó la resolución (art. 10.2.a LRJS).
- La sentencia sobre grado de incapacidad tiene **siempre** acceso a suplicación (art. 191.3.c LRJS).
- Elementos clave a probar: cuadro clínico residual, limitaciones funcionales objetivas, profesión habitual concreta y sus exigencias, y por qué las limitaciones impiden (total o absolutamente) su desempeño.
- En supuestos de revisión por mejoría: la carga de acreditar la mejoría real corresponde a quien la alega (normalmente el INSS); el principio de seguridad jurídica y buena administración (Ley 39/2015) exige que la resolución sea coherente con resoluciones judiciales previas firmes o pendientes sobre el mismo cuadro clínico.

## Fase 1 — Documentación a pedir

- Resolución del INSS que se recurre (fecha, contenido, grado denegado/reconocido).
- Expedientes previos relacionados (si hay procedimientos anteriores sobre el mismo cuadro clínico).
- Informes médicos actualizados (especificar que se necesitan para fundamentar, pero sin incorporarlos literalmente a ninguna plantilla reutilizable del plugin).
- Profesión habitual exacta y sus tareas características.
- Certificado de reclamación previa.

## Fase 2 — Comprobaciones previas

Se responden con la documentación aportada (paso 2 de `redaccion-rapida`). Solo se pregunta al abogado lo que bloquee la estructura del escrito y no se deduzca de lo aportado, en una única ronda de como máximo cuatro preguntas; lo demás que falte se deja como `[PENDIENTE: dato]`.

- ¿Qué grado se reclama? total / absoluta / gran invalidez (y subsidiario si aplica).
- ¿Es una solicitud inicial o una revisión por mejoría/agravación?
- ¿Hay sentencia previa firme o pendiente de recurso sobre el mismo cuadro clínico? (relevante para el argumento de incoherencia si el INSS contradice una resolución judicial reciente).
- Profesión habitual y tareas concretas que resultan incompatibles con las limitaciones.
- Contingencia: común o profesional (afecta a la base reguladora y a la posible demanda conexa de determinación de contingencia, ver `/seguridad-social-contingencia`).

## Fase 3 — Estructura del escrito

1. Encabezamiento: Juzgado de lo Social, parte actora (marcador genérico), INSS como demandado (domicilio de la Dirección Provincial correspondiente).
2. **HECHOS**: antecedente administrativo (resolución recurrida, fecha) → si hay expediente/sentencia previa relacionada, mencionarla → motivo de disconformidad (persistencia o agravamiento del cuadro clínico, incoherencia con resolución judicial previa si aplica) → resumen de las limitaciones funcionales relevantes para el grado solicitado, sin reproducir el informe médico completo → tareas de la profesión habitual incompatibles con dichas limitaciones.
3. **FUNDAMENTOS DE DERECHO**: jurisdicción y competencia → arts. 193-194 LGSS sobre el grado solicitado → doctrina jurisprudencial sobre criterios de calificación (verificar cita exacta vía jurisprudenciator) → si aplica, art. 20 Ley 39/2015 (principios de eficacia y buena administración) cuando la resolución contradice sin motivación suficiente una situación previamente reconocida.
4. **SUPLICO**: revocar la resolución del INSS y reconocer el grado de incapacidad permanente solicitado (con subsidiario a grado inferior si procede).

**Reparto para la redacción rápida:** 01 encabezamiento, comparecencia y hechos (antecedente administrativo, limitaciones funcionales y profesión habitual, sin reproducir el informe médico); 02 fundamentos procesales (jurisdicción, competencia, reclamación previa y plazo); 03 grado reclamado (arts. 193-194 LGSS y doctrina, con el grado subsidiario) y, si procede, la incoherencia con la resolución previa; 04 cierre (suplico y firma).

## Fase 4 — Verificación y entrega

El estilo de la casa (`estilo-escritos-judiciales`) lo aplican los redactores al escribir; la jurisprudencia la lee y verifica cada redactor en su sección (`buscar_por_cita` si no salió de las búsquedas), el ensamblado rechaza las citas que nadie leyó y cada redactor pasa `verificar_escrito` sobre sus frases con normas. Entrega en Word (.docx) con el ensamblado de `redaccion-rapida`.
