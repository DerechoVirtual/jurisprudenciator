---
name: demanda-comprador-vivienda-construccion-contra-banco-469
description: "Redacta el escrito «Demanda del comprador de vivienda en construcción contra el banco avalista por cantidades entregadas» (formulario 469 de contratos, consumo y responsabilidad civil, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Demanda del comprador de vivienda en construcción contra el banco avalista por cantidades entregadas

> Formulario 0469 del plugin **Contratos, consumo y responsabilidad civil** · revisado el 17-11-2026. Uso interno.

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

- REQUISITO DE PROCEDIBILIDAD (MASC). Desde el 3-4-2025, en los procesos declarativos (libro II LEC) y en los especiales (libro IV, incluido el monitorio según la letra del art. 5.2) la demanda solo se admite si antes se intentó un medio adecuado de solución de controversias con el mismo objeto: mediación, conciliación, persona experta independiente, oferta vinculante confidencial, negociación directa o entre abogados, Derecho colaborativo (art. 5.1 LO 1/2025). Excepciones: materias del art. 5.2 (derechos fundamentales, art. 158 CC, medidas judiciales de apoyo, filiación, tutela sumaria de la posesión, obra en ruina, ingreso, entrada en domicilio y sustracción de menores, juicio cambiario); art. 5.3 (demanda ejecutiva, cautelares previas, diligencias preliminares, jurisdicción voluntaria salvo desacuerdo conyugal, gananciales y patria potestad, monitorio europeo y escasa cuantía europeo); art. 3.2 (concursal o parte del sector público); violencia sobre la mujer, donde está vedado (art. 89.9 LOPJ). La demanda describe la negociación o su imposibilidad (art. 399.3 LEC) y acompaña el documento del art. 10 LO 1/2025 o la declaración responsable del art. 264.4.º LEC; si falta, se inadmite (art. 403.2 LEC). Plazo: un año desde la recepción de la solicitud no atendida o desde el fin sin acuerdo (art. 7.3). Consumo: basta la reclamación previa a la empresa (DA 7.ª). Texto sugerido: «CUMPLIMIENTO DEL REQUISITO DE PROCEDIBILIDAD. Con carácter previo, esta parte acudió a [medio] el [fecha], con el mismo objeto que esta demanda, sin alcanzar acuerdo, según acredita el documento n.º [ ] (arts. 5 y 10 LO 1/2025; arts. 264.4.º y 399.3 LEC)».

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (5 veces)
- [ ] Nº DE DOCUMENTO
- [ ] COLEGIO
- [ ] CALLE (2 veces)
- [ ] Nº
- [ ] FECHA (4 veces)
- [ ] NÚMERO (11 veces)
- [ ] IMPORTE (10 veces)
- [ ] ACTO O RESOLUCIÓN
- [ ] LUGAR
- [ ] Otros 12 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…na a pago de cantidad, contra la entidad»; «…, para ser citada en su sede»; «…ECHOS PRIMERO.- Mi mandante y la entidad»; «…la vivienda, la segunda mitad del mes de»; «…de»; «… SEGUNDO.- La entidad bancaria demandada»; «…nte 18 meses, en el periodo que va desde»; «…hasta»; «…ón y liquidación concursal de la entidad»; «… general corriente, frente a la avalista»; «…Se dirige acción contra la entidad BANCO»; «…a demanda, condene a la entidad bancaria»

## Correcciones de la revisión (3)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- arts. 21 LOPJ
- arts. 85.1 LOPJ
- art. 51 LEC
- arts. 7.1 y 4 LEC
- art. 10 LEC
- arts. 23.1 y 31.1 LEC
- art. 253.1 LEC
- art. 5 de la Ley Orgánica 1/2025
- art. 394.1 LEC
- Ley 38/1999
- Ley 20/2015
- Ley 57/1968

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
