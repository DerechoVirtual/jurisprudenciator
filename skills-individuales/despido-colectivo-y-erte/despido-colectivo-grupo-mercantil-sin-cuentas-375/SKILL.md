---
name: despido-colectivo-grupo-mercantil-sin-cuentas-375
description: "Redacta el escrito «Despido colectivo en grupo mercantil sin cuentas consolidadas: nulidad por falta de documentación» (formulario 375 de despido colectivo y erte, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Despido colectivo en grupo mercantil sin cuentas consolidadas: nulidad por falta de documentación

> Formulario 0375 del plugin **Despido colectivo y ERTE** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Convenio colectivo aplicable** (salario, jornada, categorías, faltas y sanciones) → `buscar_convenio` → `leer_convenio`; si sigue vigente o está denunciado, `vigencia_convenio`.
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

- Despido colectivo: art. 51 ET (consultas de hasta 30 días, 15 si menos de 50 trabajadores; comisión constituida en 7 días o 15 sin representantes; plan de recolocación externa de al menos seis meses si afecta a más de 50) y RD 1483/2012.

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] NOMBRE Y APELLIDOS (5 veces)
- [ ] DNI/NIE (5 veces)
- [ ] CALLE (6 veces)
- [ ] NÚMERO (6 veces)
- [ ] FECHA
- [ ] LUGAR
- [ ] DÍA
- [ ] MES
- [ ] AÑO
- [ ] a las que nos remitimos
- [ ] mantienen la titularidad del patrimonio
- [ ] se estructuran por sus propios órganos
- [ ] política empresarial común
- [ ] grupos verticales o de subordinación
- [ ] grupos horizontales o de coordinación
- [ ] por la titularidad de las acciones o participaciones sociales; y por la identidad de los miembros de órganos de administración
- [ ] «dominada» o «filial»
- [ ] Ley 24/1988, de 24/Julio [COMPLETAR]; en su redacción anterior a la Ley 47/2007, de 19/Diciembre
- [ ] 6/Noviembre [COMPLETAR], de desarrollo de la Ley 13/1992, de 1/Junio, sobre entidades financieras
- [ ]  Ley 27/1999, de 16/Julio
- [ ] ya derogada por el RD Legislativo 1/2010
- [ ] redacción proporcionada por la aludida Ley 47/2007 
- [ ] a (2 veces)
- [ ] indicado RD Legislativo 1/2010, de 2/Julio
- [ ] 13/Junio/1983
- [ ] traspuesta a nuestro Derecho por referida Ley 10/1997, de 24/Abril
- [ ] porque se acepta la independencia jurídica y la responsabilidad separada de las sociedades del grupo
- [ ] a virtud del principio de la realidad en la atribución de la condición de empresario, la doctrina del empresario aparente y la del fraude de ley
- [ ] muy particularmente desde la STS 03/05/90 que sistematiza la doctrina
- [ ] Otros 19 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…nº [NÚMERO] de»; «…nº [NÚMERO] de»; «…nº [NÚMERO] de»; «…nº [NÚMERO] de»; «…nº [NÚMERO] de»; «…ntes del comité de empresa de la empresa»; «…n por despido nulo (3) contra la empresa»; «…nº [NÚMERO] de»; «… que inicia el procedimiento. La empresa»; «…- La empresa se dedica a la actividad de»; «…cupa»; «…fundido del Estatuto de los Trabajadores»; …

## Elecciones que hay que hacer

- del Tribunal Superior de Justicia de [COMUNIDAD AUTÓNOMA] / de la Audiencia Nacional

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículo 51.2 ET
- artículo 124.11 LRJS
- artículo 124.4 LRJS
- artículo 124.6 LRJS
- artículo 51.1 ET
- art. 2 RD 1343/1992
- art. 1137 CE
- artículo 4.5 del RD 1483/2012
- artículo 4 del RD 1483/2012
- artículo 64.1 LRJS
- artículo 123.2 y 3 LRJS
- Ley 36/2011
- Ley 3/2012
- Real Decreto Legislativo 2/2015
- Real Decreto 1483/2012
- Ley 24/1988
- Ley 47/2007
- Ley 13/1992
- Ley 27/1999
- Ley 10/1997
- Ley 11/2013

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
