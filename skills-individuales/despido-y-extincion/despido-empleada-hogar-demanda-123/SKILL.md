---
name: despido-empleada-hogar-demanda-123
description: "Redacta el escrito «Despido de empleada del hogar: demanda» (formulario 123 de despido y extinción del contrato, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Despido de empleada del hogar: demanda

> Formulario 0123 del plugin **Despido y extinción del contrato** · revisado el 17-11-2026. Uso interno.

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

## Antes de usarlo: avisos de la revisión

El planteamiento del formulario está desfasado en algo. Corrígelo antes de redactar:

- Desistimiento en el hogar familiar: el art. 11 RD 1620/2011 (redacción RDL 16/2022) exige causa justificada (letras a-c del ap. 2), comunicación escrita, indemnización de 12 días por año con límite de seis mensualidades y preaviso de 20 días (7 si dura menos de un año); su incumplimiento formal hace presumir despido.

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (6 veces)
- [ ] LOCALIDAD (3 veces)
- [ ] TELÉFONO
- [ ] CORREO ELECTRÓNICO
- [ ] FECHA (6 veces)
- [ ] IMPORTE (2 veces)
- [ ] Nº
- [ ] Nº DE DOCUMENTO
- [ ] COLEGIO
- [ ] Otros 14 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…, de»; «…, con domicilio en [LOCALIDAD], de»; «…, en virtud de contrato de trabajo»; «…horas semanales entre los días»; «…, con horario»; «…(acompaño como documentos»; «…, enviándole finiquito fechado el»; «…ancaria. Acompaño como documento números»; «…ta de extinción son totalmente inciertos»; «…to que se hace una referencia genérica a»; «…, acompañando como documentos»; «…, a»; …

## Elecciones que hay que hacer

- externa/o / interna/o
- Disminución de los ingresos de la unidad familiar o incremento de sus gastos por circunstancia sobrevenida / Modificación sustancial de las necesidades de la unidad familiar que justifican que se prescinda de la persona trabajadora del hogar / El comportamiento de la persona trabajadora que fundamente de manera razonable y proporcionada la pérdida de confianza de la persona empleadora
- sin avenencia / sin efecto

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículos 1, 2 y 3 de la Ley 36/2011
- art. 13 del RD 1620/2011
- artículo 24.1 de la CE
- artículo 103.1 de la LJS
- artículos 53, 55 y 59 ET
- art. 11 del RD 1620/2011
- artículo 49.1 del Estatuto de los Trabajadores
- art. 11.2 del RD 1620/2011
- artículos 54, 55 y 56 ET
- Real Decreto 1620/2011

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
