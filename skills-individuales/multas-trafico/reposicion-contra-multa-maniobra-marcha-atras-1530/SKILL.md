---
name: reposicion-contra-multa-maniobra-marcha-atras-1530
description: "Redacta el escrito «Reposición contra multa por maniobra de marcha atrás» (formulario 1530 de multas y expedientes de tráfico, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Reposición contra multa por maniobra de marcha atrás

> Formulario 1530 del plugin **Multas y expedientes de tráfico** · revisado el 17-11-2026. Uso interno.

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

- [ ] ÓRGANO AL QUE SE DIRIGE
- [ ] NOMBRE Y APELLIDOS
- [ ] DNI/NIE
- [ ] DIRECCIÓN ELECTRÓNICA
- [ ] LOCALIDAD
- [ ] CALLE
- [ ] NÚMERO
- [ ] PROVINCIA
- [ ] C.P.
- [ ] FECHA (5 veces)
- [ ] ÓRGANO O PERSONA (3 veces)
- [ ] Nº DE EXPEDIENTE
- [ ] IMPORTE
- [ ] Nº
- [ ] DESCRIBIR (3 veces)
- [ ] LUGAR
- [ ] art. 35.1.a) LPACAP
- [ ] Otros 8 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…para la imposición de esta sanción es de»; «…conducta se realizó ante la necesidad de»; «… para los demás usuarios de la vía y que»; «…consistente en que se tome declaración a»; «…, en su condición de»; «…, en el que se acredita»; «…, en el que se hace referencia a»; «…instructor para apreciar y acreditar que»

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Opciones correspondientes al artículo 81.1 del Reglamento General de Circulación / Opción correspondiente al artículo 81.2 del Reglamento General de Circulación / Opción correspondiente al artículo 81.3 del Reglamento General de Circulación — el texto de cada opción no venía en el formulario original

## Párrafos opcionales (16)

Inclúyelos solo si encajan en los hechos:

- Que se vulnera el principio de TIPICIDAD por cuanto que los hechos realizados por el supuesto infractor no est…
- Que la sanción impuesta es contraria al principio de PROPORCIONALIDAD ya que no guarda una proporción adecuada…
- Que en el expediente no se ha tenido en cuenta el principio de RESPONSABILIDAD o autoría, al no dirigirse las …
- Que el órgano sancionador ha vulnerado el derecho a la PRESUNCIÓN DE INOCENCIA que asiste a los ciudadanos en …
- Que no se ha respetado en todos sus términos y consecuencias del DERECHO DE DEFENSA del imputado en este exped…
- Que la resolución impugnada es nula de pleno derecho por cuanto la COMPETENCIA para la imposición de esta sanc…
- Que la sanción es improcedente en este momento por cuanto se habría producido la PRESCRIPCION de la infracción…
- Que, aunque debiera apreciarse de oficio por su carácter de norma de orden público, alegamos la CADUCIDAD del …
- Que no es correcta la sanción impuesta por el órgano de tráfico actuante ya que se produce con esta actuación …
- Que en el expediente instruido al efecto para adoptar la resolución sancionadora no se han respetado las norma…
- Que en la tramitación de este expediente sancionador en materia de tráfico, circulación de vehículos a motor y…
- Testifical, consistente en que se tome declaración a [COMPLETAR], en cuanto testigos presenciales de los hecho…
- Pericial, consistente en informe de fecha [FECHA], emitido por [ÓRGANO O PERSONA], en su condición de [COMPLET…
- Documental, consistente en escrito de fecha [FECHA], suscrito por [ÓRGANO O PERSONA], en el que se hace refere…
- Reconocimiento sobre el terreno por el órgano instructor para apreciar y acreditar que [COMPLETAR] y los demás…
- Informe de ratificación, por parte del mismo agente denunciante de los hechos contenidos en la denuncia, y en …

## Correcciones de la revisión (8)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículo 81 del Real Decreto 1428/2003
- artículo 32 del Real Decreto Legislativo 6/2015
- artículo 81.1 del Reglamento General de Circulación
- artículo 81.2 del Reglamento General de Circulación
- artículo 81.3 del Reglamento General de Circulación
- artículo 25.1 CE
- artículo 27 de la Ley 40/2015
- artículo 81 TR LTCVMSV
- art. 29.3 LRJSP
- artículo 82 TR LTCVMSV
- artículo 28 LRJSP
- artículo 130.1 de la Ley 30/1992
- art. 28 LRJSP
- artículo 53.2.b) de la Ley 39/2015
- artículo 77 LPACAP
- art. 95.2 TR LTCVMSV
- artículo 13 del Real Decreto 320/1994
- artículo 84 TR LTCVMSV
- artículo 112.1 TR LTCVMSV
- artículo 112.2 TR LTCVMSV
- art. 112.3 TR LTCVMSV
- artículo 31 LRJSP
- artículo 96 del Real Decreto Legislativo 6/2015
- artículos 112 a 126 LPACAP
- art. 96.2 TR LTCVMSV
- art. 88 TR LTCVMSV
- art. 35.1.a) LPACAP
- artículo 36.2 LPACAP
- artículo 112 TR LTCVMSV
- arts. 112 a 120 LPACAP
- art. 118 LPACAP
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
