---
name: allanamiento-morada-ocupacion-inmueble-denuncia-408
description: "Redacta el escrito «Allanamiento de morada por ocupación de inmueble: denuncia» (formulario 408 de delitos contra el patrimonio, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Allanamiento de morada por ocupación de inmueble: denuncia

> Formulario 0408 del plugin **Delitos contra el patrimonio** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Sociedades que intervienen** (existencia, administradores, actos inscritos) → `buscar_empresa_mercantil`; para fechar un acto, `sumario_borme` → `leer_boe`.
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

- Desde el 3-4-2025 los delitos de allanamiento de morada (art. 202 CP) y de usurpación (art. 245 CP) pueden tramitarse por juicio rápido si hay atestado policial (art. 795.1.2.ª i) y j) LECrim, LO 1/2025, BOE-A-2025-76).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] NOMBRE Y APELLIDOS (6 veces)
- [ ] DNI/NIE
- [ ] CORREO ELECTRÓNICO
- [ ] TELÉFONO
- [ ] PROFESIÓN
- [ ] LOCALIDAD (2 veces)
- [ ] CALLE
- [ ] FECHA (2 veces)
- [ ] IMPORTE
- [ ] Nº DE DOCUMENTO
- [ ] LUGAR
- [ ] ÓRGANO
- [ ] Otros 11 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…e que ha sido ocupado son los siguientes»; «…abitual, ya que ocupa ese inmueble desde»; «…última vez que fuimos a nuestra casa fue»; «…, y es ahora cuando, en el transcurso de»; «…e la fecha de acceso está entre los días»; «…y»; «… La fecha de adquisición del inmueble es»; «…del contrato de arrendamiento firmado el»; «…e consta que los inquilinos actuales son»; «…en la siguiente dirección web»; «…y/o anunciada en»

## Elecciones que hay que hacer

- a la venta / en alquiler

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS
- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS

## Párrafos opcionales (12)

Inclúyelos solo si encajan en los hechos:

- 1.- Declaración del/de los denunciados.…
- .-Declaración del/de la denunciante.…
- .- Testifical:…
- D./Dña. [NOMBRE Y APELLIDOS] vecino/a del inmueble…
- D./Dña. [NOMBRE Y APELLIDOS] familiar del/de la denunciante acerca del uso habitual del inmueble y su consider…
- - La fecha de adquisición del inmueble es [COMPLETAR] según consta en el documento nº [Nº DE DOCUMENTO] adjunt…
- - Copia de los recibos de los suministros de luz, agua, gas, etc, que tiene dados de alta.…
- - Fotografías del acceso al inmueble con el cambio de cerradura.…
- - Prueba digital de video grabado del/de la denunciante intentando convencer a los ocupantes del inmueble y su…
- (Si el inmueble está alquilado)…
- (Si el inmueble está puesto a la venta o alquiler)…
- (Si se designa abogado y procurador ya en la denuncia)…

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- arts. 265 y 266 LECRIM
- art. 202.1 CP
- art. 13 LECRIM
- artículos 259 a 269 de la LECRIM
- art. 13 de la Ley de Enjuiciamiento Criminal
- art. 202 CP
- art. 245.2 CP
- artículo 10 de la Ley 39/2015

## Flujo

1. **Paso 0**: comprueba Jurisprudenciator (arriba).
2. Lee `formulario.md` entero, con su cabecera, y la parte de `marco.md` que afecte al caso (plazos, órgano, procedimiento, procedimiento aplicable, requisitos de perseguibilidad (denuncia de la persona agraviada, querella con poder especial) y prescripción).
3. Pide los datos de la lista. Lo que el usuario no sepa se queda como hueco visible.
4. Decide las elecciones y los párrafos opcionales según los hechos. Redacta las partes que el original no traía.
5. Aplica los avisos y las notas de revisión. Comprueba con `buscar_articulo` cada norma citada y, si citas jurisprudencia, localízala con `buscar_sentencias` o `buscar_por_cita` y léela con `leer_sentencias`.
6. Indica el plazo y el cauce: desde cuándo cuenta, cuándo vence y ante qué órgano se presenta.
7. Antes de entregarlo, pasa `verificar_escrito` con las frases del escrito que citan normas o sentencias y corrige lo que señale.
8. Entrega el escrito en **Word (.docx)** con formato de escrito (usa la skill de Word disponible) y, si es corto, también en el chat.
9. Cierra con: datos pendientes, partes redactadas por ti, normas y sentencias comprobadas con Jurisprudenciator y, si algún dato sale de internet, cuál es y su enlace.
