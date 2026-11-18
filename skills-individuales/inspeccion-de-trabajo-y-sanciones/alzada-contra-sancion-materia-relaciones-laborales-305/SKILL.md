---
name: alzada-contra-sancion-materia-relaciones-laborales-305
description: "Redacta el escrito «Alzada contra sanción en materia de relaciones laborales individuales y colectivas» (formulario 305 de inspección de trabajo y sanciones, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Alzada contra sanción en materia de relaciones laborales individuales y colectivas

> Formulario 0305 del plugin **Inspección de Trabajo y sanciones** · revisado el 17-11-2026. Uso interno.

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

- Alzada: un mes ante el órgano superior (art. 23.1 RD 928/1998, red. RD 688/2021; arts. 121-122 LPAC); no cabe si se pagó con la reducción del 40 % (art. 23.1, párr. 2.º); silencio desestimatorio a los tres meses (art. 23.2).
- Cuantías vigentes (art. 40.1 LISOS, red. RDL 32/2021): leves 70-750 €; graves 751-7.500 €; muy graves 7.501-225.018 €. Arts. 7.2 y 7.14: una infracción por cada persona trabajadora afectada o contratada, con multa de 1.000-10.000 € cada una (art. 40.1.c bis).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] ÓRGANO AL QUE SE DIRIGE
- [ ] NOMBRE Y APELLIDOS (2 veces)
- [ ] DNI/NIE
- [ ] DOMICILIO A EFECTOS DE NOTIFICACIONES
- [ ] FECHA (4 veces)
- [ ] ÓRGANO O PERSONA
- [ ] Nº DE EXPEDIENTE
- [ ] IMPORTE (2 veces)
- [ ] Otros 6 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…al y como sucedieron son los siguientes:»; «…n califica genéricamente los hechos como»; «…d a dictarse la resolución sancionadora:»; «…en el acta de infracción se hace constar»; «…en el acta de infracción se hace constar»; «… procedentes. Es de Justicia que pide en»

## Elecciones que hay que hacer

- en su propio nombre / en nombre de ..., cuya representación acredita conforme a la escritura de poder cuya copia acompaña

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Infracciones leves (art. 6 LISOS / Infracciones graves (art. 7 LISOS / Infracciones muy graves (art. 8 LISOS — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Infracciones leves (art. 6 LISOS / Infracciones graves (art. 7 LISOS / Infracciones muy graves (art. 8 LISOS — el texto de cada opción no venía en el formulario original
- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS
- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS
- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS
- ELEGIR UNA OPCIÓN Y REDACTARLA: Infracciones leves (art. 6 LISOS / Infracciones graves (art. 7 LISOS / Infracciones muy graves (art. 8 LISOS — el texto de cada opción no venía en el formulario original

## Párrafos opcionales (3)

Inclúyelos solo si encajan en los hechos:

- (Si no se refleja el nombre de los trabajadores en el acta)…
- (Si el acta se limita a calificar los hechos de forma genérica)…
- IV.- La sanción impuesta vulnera el principio de proporcionalidad establecido en el artículo 39 del Real Decre…

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículos 54 del Real Decreto Legislativo 5/2000
- artículos 6, 7 y 8 de la LISOS
- artículos 23 del Real Decreto 928/1998
- art. 6 LISOS
- art. 7 LISOS
- art. 8 LISOS
- artículo 25.2 de la Ley 40/2015
- artículos 25.1 de la Constitución
- artículo 24.1 de la Constitución
- artículo 53.2 del Real Decreto Legislativo 5/2000
- artículo 24.2 de la Constitución
- artículo 24 de la Constitución
- artículo 14.1 del Real Decreto 928/1998
- artículo 21.1 de la Ley 23/2015
- artículo 39 del Real Decreto Legislativo 5/2000
- Ley 39/2015
- Ley 27/2011

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
