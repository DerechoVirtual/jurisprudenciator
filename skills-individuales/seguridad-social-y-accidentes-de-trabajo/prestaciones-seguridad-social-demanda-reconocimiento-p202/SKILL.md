---
name: prestaciones-seguridad-social-demanda-reconocimiento-p202
description: "Redacta el escrito «Prestaciones de la Seguridad Social: demanda de reconocimiento» (formulario 202 (Procesal) de seguridad social y accidentes de trabajo, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Prestaciones de la Seguridad Social: demanda de reconocimiento

> Formulario 0202 de la colección de Procesal del plugin **Seguridad Social y accidentes de trabajo** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Antes de usarlo: avisos de la revisión

El planteamiento del formulario está desfasado en algo. Corrígelo antes de redactar:

- Reclamación previa ante la entidad gestora en el plazo de treinta días desde la notificación de la resolución o desde el silencio (art. 71.2 LRJS). Se entiende denegada a los cuarenta y cinco días (art. 71.5). La demanda se presenta en los treinta días siguientes a la notificación de la denegación o al silencio (art. 71.6).
- Altas médicas: la reclamación previa se presenta en once días, se resuelve en siete y la demanda va en veinte. No hay reclamación previa en las altas emitidas al agotarse los 365 días de incapacidad temporal (art. 71.1, 71.2, 71.5 y 71.6 LRJS).
- Con la demanda va inexcusablemente el recibo o la copia sellada de la reclamación previa (art. 71.7 LRJS). Si falta, se concede un plazo de subsanación de cuatro días (art. 140.2).
- En el juicio no pueden alegarse hechos distintos de los del expediente administrativo, salvo los nuevos o desconocidos (art. 143.4 LRJS).
- No hay conciliación previa en Seguridad Social (art. 64.1 LRJS), y los MASC de la LO 1/2025 no rigen en el orden social.
- Competencia territorial: la Sección de lo Social de la circunscripción donde se dictó la resolución originaria o la del domicilio del demandante, a su elección (art. 10.2.a LRJS; arts. 84.2.i y 94 LOPJ).
- Pensiones no contributivas: las gestiona el IMSERSO o la comunidad autónoma con servicios transferidos (art. 373 LGSS), así que hay que demandar al órgano autonómico competente. Desde el 23-10-2026 la de incapacidad exige discapacidad o enfermedad crónica de grado igual o superior al 65 % (art. 363 LGSS, Ley 4/2026).
- Recargo del art. 164 LGSS: entre el 30 % y el 50 %, a cargo directo del empresario infractor y no asegurable.
- Pago anticipado por la entidad gestora (art. 167.3 LGSS): solo en los supuestos que fija el reglamento y con el tope de 2,5 veces el IPREM o el capital coste. No es automático para la jubilación.
- En los huecos de fundamentos se mezclan «grado de discapacidad» y «grado de incapacidad»: son materias distintas (art. 2.o LRJS). Hay que elegir la coherente con la pretensión.
- Complemento para la reducción de la brecha de género: art. 60 LGSS (redacción del RDL 2/2023).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (3 veces)
- [ ] DNI/NIE
- [ ] LOCALIDAD (6 veces)
- [ ] TELÉFONO
- [ ] CORREO ELECTRÓNICO
- [ ] NIF
- [ ] COLEGIO
- [ ] TELÉFONO Y CORREO ELECTRÓNICO
- [ ] LUGAR
- [ ] FECHA
- [ ] Otros 12 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…mero de afiliación a la Seguridad Social»; «… del presente escrito formula DEMANDA DE»; «…RO DE LOS GASTOS MÉDICOS ocasionados por»; «…apacidad temporal y baja médica entre el»; «…y el»; «…La empresa»; «… efectos de ulteriores notificaciones en»; «…tativas de los salarios percibidos desde»; «…hasta»; «…andante por el período comprendido desde»; «…hasta»; «…- PERICIAL: en la persona de»

## Elecciones que hay que hacer

- ACCIDENTE DE TRABAJO / ENFERMEDAD PROFESIONAL
- INCAPACIDAD TEMPORAL / INCAPACIDAD PERMANENTE
- TOTAL / ABSOLUTA
- contingencias comunes / accidente laboral
- INCAPACIDAD TEMPORAL / INCAPACIDAD PERMANENTE PARCIAL PARA LA PROFESIÓN HABITUAL / INCAPACIDAD PERMANENTE TOTAL PARA LA PROFESIÓN HABITUAL / INCAPACIDAD PERMANENTE ABSOLUTA / GRAN INVALIDEZ
- accidente de trabajo / enfermedad común / enfermedad profesional
- INCAPACIDAD PERMANENTE / JUBILACIÓN

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS
- ELEGIR UNA OPCIÓN Y REDACTARLA: Reintegro de gastos médicos / Declaración de contingencia de accidente de trabajo o enfermedad profesional / Declaración de grado de incapacidad permanente / Incapacidad temporal derivada de accidente de trabajo o enfermedad común / Incapacidad permanente contributiva derivada de accidente de trabajo o enfermedad común / Incapacidad permanente contributiva derivada 
- ELEGIR UNA OPCIÓN Y REDACTARLA: Reintegro de gastos médicos / Declaración de accidente de trabajo o enfermedad profesional / Declaración de grado de discapacidad / Incapacidad temporal derivada de accidente de trabajo o enfermedad común / Incapacidad permanente contributiva derivada de accidente de trabajo o enfermedad común / Incapacidad permanente contributiva derivada de enfermedad profesional 
- ELEGIR UNA OPCIÓN Y REDACTARLA: Reintegro de gastos médicos / Declaración de accidente de trabajo o enfermedad profesional / Declaración de grado de incapacidad / Incapacidad temporal derivada de accidente de trabajo o enfermedad común / Incapacidad permanente contributiva derivada de accidente de trabajo o enfermedad común o enfermedad profesional / Incapacidad permanente no contributiva / Pensió

## Párrafos opcionales (20)

Inclúyelos solo si encajan en los hechos:

- el INSTITUTO NACIONAL DE LA SEGURIDAD SOCIAL, con domicilio en [LOCALIDAD];…
- la TESORERÍA GENERAL DE LA SEGURIDAD SOCIAL, con domicilio en [LOCALIDAD];…
- la MUTUA DE ACCIDENTES DE TRABAJO Y ENFERMEDADES PROFESIONALES, con domicilio en [LOCALIDAD];…
- el INSTITUTO DE MAYORES Y SERVICIOS SOCIALES (IMSERSO), con domicilio en [LOCALIDAD];…
- La empresa [COMPLETAR], con CIF nº [NIF], y domicilio social en [LOCALIDAD];…
- OTROSÍ DIGO que se solicita la reclamación de oficio al INSS del expediente y antecedentes que posea en relaci…
- OTROSÍ DIGO: Que interesa al derecho de esta parte, y sin perjuicio de ampliación en el momento procesal oport…
- - DOCUMENTAL consistente en el contrato de trabajo del demandante.…
- - Parte de alta y baja en la Seguridad Social.…
- - Nóminas acreditativas de los salarios percibidos desde [COMPLETAR] hasta [COMPLETAR].…
- - Recibo de liquidación de cotizaciones (RLC) y Relación Nominal de Trabajadores (RNT).…
- - DOCUMENTAL consistente en que se requiera a la empresa demandada para que aporte a juicio los siguientes doc…
- - DOCUMENTAL consistente en que se dirija atento Oficio a la Dirección Provincial de la Tesorería General de l…
- - Se dirija comunicación a la empresa demandada en estas actuaciones, para que aporte recibos de liquidación d…
- - INTERROGATORIO del representante legal de la empresa demandada, que deberá ser citado en el domicilio indica…
- - PERICIAL: la que esta parte aportará en el acto del juicio.…
- - PERICIAL: en la persona de [COMPLETAR].…
- - TESTIFICAL: la que esta parte aportará en el acto del juicio.…
- - TESTIFICAL: para que se cite en la debida forma a las siguientes personas:…
- OTROSÍ DIGO: Que importa al derecho de esta parte se declare la obligación del pago anticipado de la pensión d…

## Correcciones de la revisión (2)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículo 164 de la Ley General de la Seguridad Social
- artículos 1, 2, 6 y 10 de la Ley 36/2011

## Flujo

1. **Paso 0**: comprueba Jurisprudenciator (arriba).
2. Lee `formulario.md` entero, con su cabecera, y la parte de `marco.md` que afecte al caso (plazos, órgano, procedimiento, conciliación o mediación previa, reclamación previa o vía administrativa, según el caso).
3. Pide los datos de la lista. Lo que el usuario no sepa se queda como hueco visible.
4. Decide las elecciones y los párrafos opcionales según los hechos. Redacta las partes que el original no traía.
5. Aplica los avisos y las notas de revisión. Comprueba con `buscar_articulo` cada norma citada y, si citas jurisprudencia, localízala con `buscar_sentencias` o `buscar_por_cita` y léela con `leer_sentencias`.
6. Indica el plazo y el cauce: desde cuándo cuenta, cuándo vence y ante qué órgano se presenta.
7. Antes de entregarlo, pasa `verificar_escrito` con las frases del escrito que citan normas o sentencias y corrige lo que señale.
8. Entrega el escrito en **Word (.docx)** con formato de escrito (usa la skill de Word disponible) y, si es corto, también en el chat.
9. Cierra con: datos pendientes, partes redactadas por ti, normas y sentencias comprobadas con Jurisprudenciator y, si algún dato sale de internet, cuál es y su enlace.
