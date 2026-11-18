---
name: desahucio-impago-rentas-gran-tenedor-enervacion-finca-61
description: "Redacta el escrito «Desahucio por impago y rentas del gran tenedor, con enervación (finca urbana)» (formulario 61 de arrendamientos y desahucio, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Desahucio por impago y rentas del gran tenedor, con enervación (finca urbana)

> Formulario 0061 del plugin **Arrendamientos y desahucio** · revisado el 17-11-2026. Uso interno.

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

- Desahucio de vivienda desde el 8-10-2026: comprobar la suspensión del art. 2 RDL 29/2026 (hasta 31-12-2030; aplicable a ejecuciones en curso, DT 2.ª) y, si es por impago y el inquilino es vulnerable, la enervación extraordinaria a cargo de la Administración del art. 22.6 LEC (dos meses de suspensión; independiente de la del 22.4).
- La condición de gran tenedor se acredita ahora con certificación registral (art. 3.k Ley 12/2023, redacción RDL 29/2026).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (5 veces)
- [ ] LOCALIDAD (6 veces)
- [ ] Nº DE COLEGIADO/A
- [ ] CORREO ELECTRÓNICO
- [ ] Nº (2 veces)
- [ ] CALLE
- [ ] FECHA (7 veces)
- [ ] Nº DE DOCUMENTO (7 veces)
- [ ] NÚMERO
- [ ] IMPORTE (11 veces)
- [ ] LUGAR
- [ ] DÍA
- [ ] MES
- [ ] AÑO
- [ ] Otros 12 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…del Ilustre Colegio de la Abogacía de»; «…con domicilio (3), primero en»; «…; y segundo, el domicilio laboral en»; «…; y con número de teléfono móvil»; «…aria de la vivienda sita en la ciudad de»; «…renta mensual que asciende a la cifra de»; «…el quinto día anticipado de cada mes del»; «… las rentas correspondientes a los meses»; «…ntidad bancaria, como documentos números»; «…y»; «…iante correspondencia escrita, en fechas»; «…n de la presente demanda; el servicio de»

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Si el poder se otorga a través de la sede judicial electrónica / Si el poder se otorga mediante comparecencia apud acta / Si el poder se otorga ante Notario — el texto de cada opción no venía en el formulario original

## Correcciones de la revisión (3)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- art. 24.1 LEC
- art. 439.6 LEC
- art. 3 k) de la Ley 12/2023
- art. 3.k) de la Ley 12/2023
- art. 439.6 c) LEC
- art. 438.5 LEC
- art. 437.3 LEC
- art. 85.1 LOPJ
- art. 438.5 y 6 LEC
- arts. 23.1 y 31.1 LEC
- art. 253 LEC
- art. 251 LEC
- art. 439.7 LEC
- art. 437.1 LEC
- art. 5 de la Ley Orgánica 1/2025
- art. 17 LAU
- art. 1.556 CCiv
- art. 27.2 a) LAU
- art. 220 LEC
- art. 439.3 LEC
- art. 22.4 LEC
- art. 394.1 LEC
- art. 22.5 LEC
- art. 439 LEC
- art. 655 bis LEC
- art. 685.2 LEC
- art. 250 LEC
- art. 24.2 LEC
- art. 155.3 LEC
- artículo 250 LEC

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
