---
name: arrendamiento-vivienda-adaptado-ley-12-2023-derecho-1447
description: "Redacta el escrito «Arrendamiento de vivienda adaptado a la Ley 12/2023 por el derecho a la vivienda» (formulario 1447 de arrendamientos y desahucio, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Arrendamiento de vivienda adaptado a la Ley 12/2023 por el derecho a la vivienda

> Formulario 1447 del plugin **Arrendamientos y desahucio** · revisado el 17-11-2026. Uso interno.

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

- Ya adaptado en parte (nota del RDL 29/2026); revisar además renta (IRAV y DF 6.ª), gastos e IBI (art. 20), adquisición preferente irrenunciable (25.8) y prórroga tácita (art. 10).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] NOMBRE Y APELLIDOS (5 veces)
- [ ] NACIONALIDAD (2 veces)
- [ ] LOCALIDAD (3 veces)
- [ ] DNI/NIE (4 veces)
- [ ] NÚMERO
- [ ] FECHA (2 veces)
- [ ] IMPORTE (3 veces)
- [ ] Nº
- [ ] LUGAR
- [ ] Otros 14 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…de que.... Adaptado a la Ley 12/2023. En»; «…, con una superficie de»; «…scrita en el Registro de la Propiedad de»; «…en el»; «…vigente en los últimos cinco años fue de»; «…e viviendas que resulta de aplicación es»; «…ivienda arrendada cuyo precio se fija en»; «… plaza de aparcamiento arrendados es del»; «…e resolverán a través de la Mediación de»; «…ecida en la Ley 5/2012, de 6 de julio, y»; «…suelta mediante Arbitraje de la Corte de»; «…s árbitros, de acuerdo con su reglamento»; …

## Elecciones que hay que hacer

- soltero / soltera / casado / casada / divorciado / divorciada / separado / separada / viudo / viuda
- gananciales / separación de bienes
- propietaria / usufructuaria
- metálico / lo que se pacte

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Seleccionar en caso de que todas las partes actúen en nombre y representación propia / Seleccionar si alguna de las partes actúa en su propio nombre y representación — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Si se trata de persona física / Si se trata de una persona jurídica — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: En caso de vivienda amueblada / En caso de vivienda no amueblada — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Con puesta a disposición y entrega de llaves / Puesta a disposición posterior — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: En caso de que la renta se revise conforme a lo pactado / (Si la renta se revisa conforme a índices/IPC) [NOTA DE REVISIÓN: Art. 18 LAU vigente: solo hay actualización si se pacta; el incremento anual no puede exceder de la variación del IRAV y la renta actualizada es exigible desde el mes siguiente a la notificación escrita (art. 18.2; vale la nota en el recibo). P
- ELEGIR UNA OPCIÓN Y REDACTARLA: En caso de pactar no elevar la renta si se realizan obras de mejora / Si se pacta elevar la renta si se realizan obras de mejora — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: En caso de no incluir los gastos generales en la renta / En caso de incluir los gastos generales en la renta — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: En caso de contrato inferior a 5 años / En caso de pactar una duración diferente del contrato / En caso de contrato superior a 5 años e inferior a 7 años / En caso de inmueble ubicado en una zona de mercado residencial tensionado — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Si se nombra avalista o fiador sin poder ante notario / Si se nombra avalista o fiador ante notario — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Si se permite subarrendar la vivienda / En caso de que no se permita subarrendar la vivienda — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: (En caso de que no se pacte el derecho de adquisición preferente) [NOTA DE REVISIÓN: Art. 25.8 LAU (RDL 29/2026): las partes no pueden pactar la renuncia del arrendatario de vivienda al derecho de adquisición preferente; esta opción solo sirve para contratos anteriores al 8-10-2026. Fuente: LAU (Ley 29/1994), BOE-A-1994-26003, art. 25.8 (redacción RDL 29/2026, BOE-A
- ELEGIR UNA OPCIÓN Y REDACTARLA: En caso de que se excluya el derecho de subrogación / En caso de que se pacte el derecho de subrogación — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Si se pacta la resolución del contrato por falta de pago de renta y la restitución inmediata del inmueble al arrendador / En caso de que no se pacte la resolución por falta de pago de renta — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: En caso de que se pacte indemnización al arrendador por desistimiento del arrendatario / En caso de que no se pacte indemnización al arrendador por desistimiento del arrendatario — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: (A cargo de la arrendataria) [NOTA DE REVISIÓN: Art. 20.1-2 LAU (RDL 29/2026): no pueden imponerse al arrendatario los tributos asociados a la vivienda (salvo que sea obligado tributario, p. ej. ITP del arrendamiento) ni los gastos de gestión inmobiliaria y de formalización del contrato. Fuente: LAU (Ley 29/1994), BOE-A-1994-26003, art. 20.1-2 (redacción RDL 29/2026

## Párrafos opcionales (7)

Inclúyelos solo si encajan en los hechos:

- Casado…
- (Seleccionar en caso de estado civil casado/a)…
- (Seleccionar si alguna de las partes actúa en nombre y representación de persona física o jurídica)…
- Cuando la vivienda que vaya a ser objeto de arrendamiento como vivienda habitual se encuentre ubicada en una z…
- (Si se pacta el derecho de opción de compra)…
- (Si se pacta el pago por el arrendatario de gastos de comunidad y otros)…
- (Si se pacta por las partes que, durante un plazo determinado, la obligación del pago de la renta sea reemplaz…

## Correcciones de la revisión (2)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- art. 31 de la Ley 12/2023
- artículo 4.6 LAU
- Ley 29/1994
- Ley 5/2012
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
