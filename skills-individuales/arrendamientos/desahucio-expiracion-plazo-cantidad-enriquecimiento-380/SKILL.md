---
name: desahucio-expiracion-plazo-cantidad-enriquecimiento-380
description: "Redacta el escrito «Desahucio por expiración del plazo y cantidad por enriquecimiento injusto (juicio verbal)» (formulario 380 de arrendamientos y desahucio, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Desahucio por expiración del plazo y cantidad por enriquecimiento injusto (juicio verbal)

> Formulario 0380 del plugin **Arrendamientos y desahucio** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Inmuebles** (referencia catastral, superficie, uso) → `consultar_catastro` (y `callejero_catastro` para localizar la dirección).

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Antes de usarlo: avisos de la revisión

El planteamiento del formulario está desfasado en algo. Corrígelo antes de redactar:

- Antes de demandar por expiración del plazo, comprobar si el inquilino puede pedir la prórroga extraordinaria de la DF 5.ª RDL 29/2026 (hasta dos años, obligatoria salvo excepciones) o las de los arts. 10.2-10.3 LAU.
- Desahucio de vivienda desde el 8-10-2026: comprobar la suspensión del art. 2 RDL 29/2026 (hasta 31-12-2030; aplicable a ejecuciones en curso, DT 2.ª) y, si es por impago y el inquilino es vulnerable, la enervación extraordinaria a cargo de la Administración del art. 22.6 LEC (dos meses de suspensión; independiente de la del 22.4).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (8 veces)
- [ ] LOCALIDAD (4 veces)
- [ ] Nº DE COLEGIADO/A
- [ ] IMPORTE (3 veces)
- [ ] CORREO ELECTRÓNICO
- [ ] Nº (2 veces)
- [ ] NÚMERO (4 veces)
- [ ] FECHA (9 veces)
- [ ] Nº DE DOCUMENTO (3 veces)
- [ ] ACTO O RESOLUCIÓN
- [ ] LUGAR (2 veces)
- [ ] Otros 8 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…del Ilustre Colegio de la Abogacía de»; «…, con domicilio (2), primero en»; «…; y segundo, el domicilio laboral en»; «…; y con número de teléfono móvil»; «…e arrendamiento con el ahora demandando,»; «…. TERCERO.- En la cláusula»; «…a anual de pagadera por mensualidades de»; «…iante correspondencia escrita, en fechas»

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Si el poder se otorga a través de la sede judicial electrónica / Si el poder se otorga mediante comparecencia apud acta / Si el poder se otorga ante Notario — el texto de cada opción no venía en el formulario original

## Párrafos opcionales (3)

Inclúyelos solo si encajan en los hechos:

- PRIMER OTROSI DIGO, que siendo el poder que acompaño, general para pleitos y necesitándolo para otros usos pro…
- SEGUNDO OTROSI DIGO, que esta parte manifiesta su voluntad, a los efectos del art. 231 de la LEC, de cumplir, …
- TERCER OTROSÍ DIGO, que de conformidad a lo establecido en el art. 437.3 "in fine" en relación al art. 549.3 L…

## Correcciones de la revisión (1)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- art. 24.1 LEC
- art. 439 LEC
- art. 3.k) de la Ley 12/2023
- artículo 10 LEC
- artículo 7.1 LEC
- artículo 23 LEC
- artículo 31 LEC
- art. 253 LEC
- art. 5 de la Ley Orgánica 1/2025
- artículo 1565 CC
- artículos 1577 y 1581 CC
- artículo 1569 CC
- artículo 549 LEC
- artículo 548 LEC
- artículo 394 LEC
- art. 231 de la LEC
- art. 549.3 LEC
- art. 24.2 LEC
- art. 155.3 LEC

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
