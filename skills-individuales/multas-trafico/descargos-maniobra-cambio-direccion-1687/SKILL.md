---
name: descargos-maniobra-cambio-direccion-1687
description: "Redacta el escrito «Descargos por maniobra de cambio de dirección» (formulario 1687 de multas y expedientes de tráfico, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Descargos por maniobra de cambio de dirección

> Formulario 1687 del plugin **Multas y expedientes de tráfico** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Ordenanzas municipales** (tráfico, urbanismo, tributos locales, convivencia) → `buscar_ordenanzas` → `leer_ordenanza`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] NOMBRE Y APELLIDOS (2 veces)
- [ ] DNI/NIE
- [ ] DIRECCIÓN ELECTRÓNICA
- [ ] LOCALIDAD (2 veces)
- [ ] CALLE
- [ ] NÚMERO
- [ ] PROVINCIA
- [ ] C.P.
- [ ] ÓRGANO
- [ ] Nº DE EXPEDIENTE
- [ ] FECHA (4 veces)
- [ ] DESCRIBIR (3 veces)
- [ ] IMPORTE
- [ ] Nº
- [ ] ÓRGANO O PERSONA (2 veces)
- [ ] LUGAR
- [ ] Otros 10 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…de»; «…sta conducta se realizó ante el hecho de»; «…y la necesidad de»; «…n de la infracción, por el transcurso de»; «…consistente en que se tome declaración a»; «…, en su condición de»; «…, en el que se acredita»; «…, en el que se hace referencia a»; «…instructor para apreciar y acreditar que»; «…to la sanción, en lo que se refiere a la»

## Elecciones que hay que hacer

- Jefatura de Tráfico / ALCALDÍA

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Opción de infracción correspondiente al artículo 75.1.a) del Reglamento General de Circulación / Opción de infracción correspondiente al artículo 75.1.b) del Reglamento General de Circulación / Opción de infracción correspondiente al artículo 75.1.c) del Reglamento General de Circulación — el texto de cada opción no venía en el formulario original

## Párrafos opcionales (14)

Inclúyelos solo si encajan en los hechos:

- Prescripción de la infracción, por el transcurso de [COMPLETAR], contados desde la fecha en que los hechos sup…
- La caducidad del expediente, por el paso de un año desde el inicio del mismo sin que hasta la fecha presente s…
- La falta de notificación del expediente al autor de la infracción (D./Dña. [NOMBRE Y APELLIDOS], con domicilio…
- La ausencia en el boletín de denuncia de los datos esenciales para identificar al instructor y al titular del …
- La ausencia del empleo de la lengua oficial en esta Comunidad Autónoma, lo que resulta obligatorio y produce i…
- Falta de competencia del órgano instructor y sancionador por tratarse de una infracción cuyo conocimiento no l…
- La Concurrencia del siguiente hecho que extingue la responsabilidad en este expediente sancionador:…
- Pago anticipado.…
- Haber sido ya sancionado por los mismos hechos.…
- Testifical, consistente en que se tome declaración a [COMPLETAR], en cuanto testigos presenciales de los hecho…
- Pericial, consistente en informe de fecha [FECHA], emitido por [ÓRGANO O PERSONA], en su condición de [COMPLET…
- Documental, consistente en escrito de fecha [FECHA], suscrito por [ÓRGANO O PERSONA], en el que se hace refere…
- Reconocimiento sobre el terreno por el órgano instructor para apreciar y acreditar que [COMPLETAR] y los demás…
- Informe de ratificación, por parte del mismo agente denunciante de los hechos contenidos en la denuncia, y en …

## Correcciones de la revisión (2)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículo 75 del Real Decreto 1428/2003
- artículo 30 del Real Decreto Legislativo 6/2015
- artículo 75.1.a) del Reglamento General de Circulación
- artículo 75.1.b) del Reglamento General de Circulación
- artículo 75.1.c) del Reglamento General de Circulación
- artículos 93.1 y 95.1 del Real Decreto Legislativo 6/2015
- artículos 25 a 31 de la Ley 40/2015
- art. 112 TR LTCVMSV
- artículos 80 y 81 TR LTCVMSV

## Flujo

1. **Paso 0**: comprueba Jurisprudenciator (arriba).
2. Lee `formulario.md` entero, con su cabecera, y la parte de `marco.md` que afecte al caso (plazos, órgano, procedimiento, MASC si es una demanda civil).
3. Pide los datos de la lista. Lo que el usuario no sepa se queda como hueco visible.
4. Decide las elecciones y los párrafos opcionales según los hechos. Redacta las partes que el original no traía.
5. Aplica los avisos y las notas de revisión. Comprueba con `buscar_articulo` cada norma citada y, si citas jurisprudencia, localízala con `buscar_sentencias` o `buscar_por_cita` y léela con `leer_sentencias`.
6. Indica el plazo y el cauce: desde cuándo cuenta, cuándo vence y ante qué órgano se presenta.
7. Antes de entregarlo, pasa `verificar_escrito` con las frases del escrito que citan normas o sentencias y corrige lo que señale.
8. Entrega el escrito en **Word (.docx)** con formato de escrito (usa la skill de Word disponible) y, si es corto, también en el chat.
9. Cierra con: datos pendientes, partes redactadas por ti, normas y sentencias comprobadas con Jurisprudenciator y, si algún dato sale de internet, cuál es y su enlace.
