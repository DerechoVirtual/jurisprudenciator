---
name: accion-regreso-socio-contra-sociedad-art-331-lsc-demanda-p90
description: "Redacta el escrito «Acción de regreso del socio contra la sociedad (art. 331 LSC): demanda» (formulario 90 (Procesal) de contratos, consumo y responsabilidad civil, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Acción de regreso del socio contra la sociedad (art. 331 LSC): demanda

> Formulario 0090 de la colección de Procesal del plugin **Contratos, consumo y responsabilidad civil** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Sociedades que intervienen** (existencia, administradores, actos inscritos) → `buscar_empresa_mercantil`; para fechar un acto, `sumario_borme` → `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Antes de usarlo: avisos de la revisión

El planteamiento del formulario está desfasado en algo. Corrígelo antes de redactar:

- MASC obligatorio (art. 5 LO 1/2025). El requerimiento por correo certificado del hecho cuarto solo sirve si acredita la recepción y el contenido íntegro (art. 10.2) y si han pasado treinta días naturales sin respuesta (art. 10.4.a), con identidad de objeto (art. 5.1). Debe aportarse ese documento.
- El art. 1145.2 CC limita el regreso a «la parte que a cada uno corresponda». Reclamar el 100 % exige justificar que, en la relación interna, la cuota del socio es nula (responde como garante legal del art. 331 TRLSC). Si no, hay riesgo de estimación parcial.
- Intereses: el art. 1145.2 CC concede «los intereses del anticipo», es decir, desde el pago. El modelo los pide desde la reclamación extrajudicial; valorar pedirlos desde la fecha del pago.
- Competencia objetiva: Sección de lo Mercantil por la materia «sociedades mercantiles» (art. 87.6.a LOPJ). Como la acción se funda en el art. 1145 CC, cabe discutir que corresponda a la Sección Civil; prever una posible declinatoria.
- Cuantía: juicio ordinario si supera 15.000 euros (art. 249.2 LEC, umbral vigente desde el 20-3-2024); si no, juicio verbal.
- Costas: el art. 394.1, párrafo 3, y el art. 394.4 LEC tienen en cuenta la conducta de las partes en el MASC.
- El encabezamiento dice «Procurador/a ... de la entidad [COMPLETAR]», pero el actor es el socio, persona física, y la entidad es la demandada. Hay que corregirlo al usarlo.
- Responsabilidad del socio: solidaria, limitada a lo restituido, con prescripción de cinco años desde que la reducción es oponible a terceros (art. 331.2 y 331.3 TRLSC).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (4 veces)
- [ ] NÚMERO (4 veces)
- [ ] COLEGIO
- [ ] LOCALIDAD (5 veces)
- [ ] FECHA (11 veces)
- [ ] NIF
- [ ] IMPORTE (7 veces)
- [ ] Nº (6 veces)
- [ ] LUGAR
- [ ] Otros 30 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…ador/a de los Tribunales y de la entidad»; «…regreso o repetición frente a la entidad»; «…s socio, desde un inicio de la mercantil»; «…, constituida el»; «…, Notario de»; «…de»; «…de [COMPLETAR] en el»; «…de [COMPLETAR] en el [COMPLETAR], Tomo»; «… el [COMPLETAR], Tomo [COMPLETAR], Folio»; «…omo [COMPLETAR], Folio [COMPLETAR], Hoja»; «… de participaciones sociales con números»; «…da por unanimidad, reducir el capital de»; …

## Correcciones de la revisión (7)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- arts. 51.1 LEC
- art. 87.1 LOPJ
- art. 7.4 LEC
- art. 253.1 LEC
- art. 249.2 LEC
- arts. 23 y 31 LEC
- art. 399 LEC
- art. 399.3 LEC
- art. 5 LO 1/2025
- art. 1.145 CC
- art. 222 LEC
- art. 1.145.2 CC
- artículo 394 de la LEC

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
