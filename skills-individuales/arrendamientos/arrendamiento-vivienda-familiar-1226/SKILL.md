---
name: arrendamiento-vivienda-familiar-1226
description: "Redacta el escrito «Arrendamiento de vivienda a un familiar» (formulario 1226 de arrendamientos y desahucio, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Arrendamiento de vivienda a un familiar

> Formulario 1226 del plugin **Arrendamientos y desahucio** · revisado el 17-11-2026. Uso interno.

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

- Contrato de 2013-2016: revisar contra la LAU vigente (RDL 29/2026, desde 8-10-2026): duración 5/7 años y prórroga tácita de 3 (arts. 9-10), actualización con tope IRAV y DF 6.ª (2 % hasta 31-12-2027), pago electrónico (17.3), gastos e IBI (20), sin indemnización por desistimiento (11.3), adquisición preferente irrenunciable (25.8) y garantía adicional ≤ 2 meses sin seguro de impago (36.5).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] LUGAR
- [ ] DÍA
- [ ] MES
- [ ] AÑO
- [ ] DNI/NIE
- [ ] CALLE (2 veces)
- [ ] NÚMERO (2 veces)
- [ ] NOMBRE Y APELLIDOS (5 veces)
- [ ] Nº
- [ ] FECHA
- [ ] IMPORTE (3 veces)
- [ ] Otros 23 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «… propio nombre y derecho y a favor de su»; «…y misma dirección que su»; «… misma dirección que su [COMPLETAR]. Que»; «…de»; «…de al Tomo»; «…de al Tomo [COMPLETAR], Folio»; «…, Folio [COMPLETAR], Finca»; «…que se describe de la forma siguiente»; «…para destinarla a domicilio de su»; «…de arrendamiento de vivienda a favor del»; «…de»; «…te contrato constituirá la residencia de»; …

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Comparecencia / En su nombre propio / En nombre y representación — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Desistimiento / Ausencia indemnización / Indemnización — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Forma de pago / Ingreso o transferencia / Domicilio arrendador [NOTA DE REVISIÓN: Art. 17.3 LAU vigente: el pago se efectúa por medios electrónicos; en metálico solo excepcionalmente, a solicitud de la parte que carezca de cuenta bancaria o de acceso a medios electrónicos de pago, y en la vivienda arrendada. Fuente: LAU (Ley 29/1994), BOE-A-1994-26003, art. 17.3 (te
- ELEGIR UNA OPCIÓN Y REDACTARLA: Cuotas comunidad de propietarios / Arrendatario liquida directamente / Arrendatario abona al arrendador — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: LAU / Renuncia — el texto de cada opción no venía en el formulario original

## Correcciones de la revisión (4)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículo 1124 del Código Civil
- Real Decreto 390/2021

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
