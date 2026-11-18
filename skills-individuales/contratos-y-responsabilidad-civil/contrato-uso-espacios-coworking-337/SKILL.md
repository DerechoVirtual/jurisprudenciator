---
name: contrato-uso-espacios-coworking-337
description: "Redacta el escrito «Contrato de uso de espacios de coworking» (formulario 337 de contratos, consumo y responsabilidad civil, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Contrato de uso de espacios de coworking

> Formulario 0337 del plugin **Contratos, consumo y responsabilidad civil** · revisado el 17-11-2026. Uso interno.

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

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] NOMBRE Y APELLIDOS (8 veces)
- [ ] NACIONALIDAD (2 veces)
- [ ] LOCALIDAD (3 veces)
- [ ] DNI/NIE (4 veces)
- [ ] PLAZO (6 veces)
- [ ] Nº (3 veces)
- [ ] IMPORTE
- [ ] Otros 38 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…tividad empresarial. Recuerde que.... En»; «…, con una superficie de»; «…metros cuadrados compuesto por»; «… "EL ESPACIO COWORKING"), que cuenta con»; «…locales/puestos de trabajo y»; «…e la COWORKER o ARRENDATARIA se dedica a»; «…arrendar el LOCAL/PUESTO DE TRABAJO para»; «…, con efecto a partir del»; «…ifieste a la COWORKING o ARRENDADORA con»; «…ARRENDADORA con una antelación mínima de»; «…RENDADORA con una cantidad equivalente a»; «…o ARRENDATARIA única y exclusivamente a:»; …

## Elecciones que hay que hacer

- soltero / soltera / casado / casada / divorciado / divorciada / separado / separada / viudo / viuda
- gananciales / separación de bienes
- proporcionar / facilitar
- todos los días / de lunes a viernes
- despacho / puesto de trabajo
- hora / mes / año

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Seleccionar en caso de que todas las partes actúen en nombre y representación propia / Seleccionar si alguna de las partes actúa en su propio nombre y representación — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Si se trata de persona física / Si se trata de una persona jurídica — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: En caso de puesto de trabajo o despacho fijo y de uso exclusivo / En caso de puesto de trabajo no fijo — el texto de cada opción no venía en el formulario original
- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS
- ELEGIR UNA OPCIÓN Y REDACTARLA: Reconocimiento / Renucia — el texto de cada opción no venía en el formulario original
- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS

## Párrafos opcionales (30)

Inclúyelos solo si encajan en los hechos:

- (Seleccionar en caso de estado civil casado/a)…
- (Seleccionar en caso de estado civil casado/a)…
- (Seleccionar si alguna de las partes actúa en nombre y representación de persona física o jurídica)…
- (Desistimiento.)…
- (En caso de Coworking en despacho o puesto de trabajo fijo y de uso exclusivo)…
- (En caso de Coworking en despacho o puesto de trabajo fijo y de uso exclusivo)…
- - Instalación eléctrica.…
- - Uso de la cocina, supeditado a disponibilidad, según lo dispuesto en el Anexo II.…
- - Uso de WC.…
- - Acceso a Internet a alta velocidad y seguro por cable e inalámbrico.…
- - Uso de la Sala de reuniones, supeditado a disponibilidad, según lo dispuesto en el Anexo II.…
- - Entrada gratuita a eventos y formaciones organizadas por otros coworkers.…
- - Climatización del módulo de oficina.…
- - Servicio recogida diaria de correspondencia.…
- - Servicio de recogida de mensajes telefónicos.…
- - Servicio de sala de espera, sujeto a disponibilidad, según lo dispuesto en el Anexo II.…
- - Servicio de atención a clientes.…
- Séptima.- Servicios optativos…
- El importe de los servicios y suministros individualizados de luz, agua, gas, teléfono, internet u otros simil…
- .- Rótulos y anuncios…
- .- No competencia…
- .- Fianza…
- (Fiador Solidario)…
- (Depósito si el despacho está amueblado)…
- La COWORKER o ARRENDATARIA se obliga a contratar una póliza de seguro que cubra [COMPLETAR]. Deberá ser notifi…
- Asimismo, serán de cuenta y cargo de la parte COWORKER o ARRENDATARIA cualquier obra que pudiera ser ordenada …
- (Exclusiones)…
- (Reducción de precio)…
- (En caso de posibilidad de subarriendo)…
- (En caso de previsión para fallecimiento de la COWORKER o ARRENDATARIA persona física)…

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- Real Decreto 390/2021
- Ley Orgánica 3/2018
- Ley 29/1994

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
