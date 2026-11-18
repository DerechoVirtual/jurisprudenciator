---
name: sancion-indisciplina-desobediencia-carta-314
description: "Redacta el escrito «Sanción por indisciplina o desobediencia: carta» (formulario 314 de régimen disciplinario laboral, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Sanción por indisciplina o desobediencia: carta

> Formulario 0314 del plugin **Régimen disciplinario laboral** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Convenio colectivo aplicable** (salario, jornada, categorías, faltas y sanciones) → `buscar_convenio` → `leer_convenio`; si sigue vigente o está denunciado, `vigencia_convenio`.

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

- [ ] FECHA (2 veces)
- [ ] NOMBRE Y APELLIDOS (4 veces)
- [ ] Otros 11 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…alizar un trabajo en un lugar concreto A»; «…. Muy Sr./a mío/a:»; «… establecido en el Convenio colectivo de»; «…Su conducta ha producido:»; «…para la empresa, en tanto»; «…as instalaciones de la empresa, en tanto»; «…de la empresa, en tanto»; «…n de riesgos para las personas, en tanto»; «…de»; «…ada en el art. del Convenio colectivo de»; «…, con la sanción de»

## Elecciones que hay que hacer

- no grave / grave / muy grave
- instrumentos / bienes / enseres / maquinarias / otros
- leve / grave / muy grave

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: No utilización o utilización de forma negligente elementos de protección en materia de seguridad o prevención de riesgos / Desobedecer las órdenes sobre uso de sistemas de seguridad o prevención de riesgos / No realizar determinado trabajo / No realizar un trabajo de un modo concreto / No realizar un trabajo en un tiempo concreto / No realizar un trabajo en un lugar
- ELEGIR UNA OPCIÓN Y REDACTARLA: Infracción grave o muy grave si el trabajador es representante legal o sindical / Infracción muy grave de persona trabajadora no afiliada a un sindicato / Infracción muy grave de persona trabajadora afiliada a un sindicato — el texto de cada opción no venía en el formulario original

## Párrafos opcionales (9)

Inclúyelos solo si encajan en los hechos:

- - Perjuicio [ELEGIR: no grave / grave / muy grave] para la empresa, en tanto [COMPLETAR].…
- - Causación de averías en las instalaciones de la empresa, en tanto [COMPLETAR].…
- - Causación de averías en los [ELEGIR: instrumentos / bienes / enseres / maquinarias / otros] de la empresa, e…
- - Causación de riesgos para las personas, en tanto [COMPLETAR].…
- (Si los productos o servicios de la empresa pueden acarrear problemas sanitarios)…
- (Si se trata de una suspensión de empleo y sueldo)…
- (Si en Infracción grave o muy grave la persona trabajadora renuncia a la presencia o asistencia de un represen…
- (Si en la persona trabajadora no quiere firmar la recepción de la carta de sanción)…
- D./Dña. [NOMBRE Y APELLIDOS]…

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículo 20 del Estatuto de los Trabajadores
- Real Decreto Legislativo 2/2015

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
