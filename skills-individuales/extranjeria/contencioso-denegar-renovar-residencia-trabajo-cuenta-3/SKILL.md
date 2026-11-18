---
name: contencioso-denegar-renovar-residencia-trabajo-cuenta-3
description: "Redacta el escrito «Contencioso por denegar renovar residencia y trabajo por cuenta ajena (antecedentes policiales)» (formulario 3 de extranjería, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Contencioso por denegar renovar residencia y trabajo por cuenta ajena (antecedentes policiales)

> Formulario 0003 del plugin **Extranjería** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Antes de usarlo: avisos de la revisión

El planteamiento del formulario está desfasado en algo. Corrígelo antes de redactar:

- Renovación por cuenta ajena: hoy art. 80 RD 1155/2024 (plazos en meses; solo «nueve meses en doce», desaparece «dieciocho en veinticuatro»; la denegación por orden público exige informe policial motivado, art. 78.1.e).

## Nota explicativa: puntualizaciones de la revisión

La nota explicativa de este formulario se ha revisado en el BOE. Tenlo en cuenta al redactar:

- El art. 8.4 LJCA vigente atribuye a estos órganos todas las resoluciones de extranjería dictadas por la Administración periférica del Estado «o por los órganos competentes de las Comunidades Autónomas»; no hace falta acudir al art. 8.2 LJCA (que solo cubre personal, sanciones y responsabilidad patrimonial) cuando la autorización la resuelva la Comunidad Autónoma.
- Desde el 31-12-2025 los Juzgados de lo Contencioso-Administrativo son Secciones de lo Contencioso-Administrativo del Tribunal de Instancia (LO 1/2025, DT 1.ª y DA 1.ª; arts. 84.2.h y 93 LOPJ); la plaza conserva el número del antiguo Juzgado. El procedimiento abreviado en extranjería sigue en el art. 78.1 LJCA (redacción de la LO 1/2025, vigente desde el 3-4-2025).
- En el RD 1155/2024 (vigente desde el 20-5-2025), el art. 78 regula la denegación de las autorizaciones iniciales de residencia temporal y trabajo por cuenta ajena y el art. 80 su renovación; el art. 80.8 extiende a la renovación las causas del art. 78 (entre ellas, la amenaza para el orden público acreditada y motivada en informe policial, art. 78.1.e), y el art. 80.5.a), como el art. 31.7.a) LO 4/2000, ordena valorar los antecedentes penales y la condena cumplida, indultada, remitida o suspendida.
- El INEM ya no existe: el Servicio Público de Empleo Estatal está pendiente de transformarse en la Agencia Española de Empleo (Ley 3/2023, de Empleo, art. 18).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión. Empieza con una nota explicativa (para qué sirve el escrito y cuándo se usa) y acaba con sus notas al pie, revisadas en el BOE: léela antes de redactar, pero no la copies en el escrito.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (3 veces)
- [ ] FECHA (5 veces)
- [ ] LUGAR (2 veces)
- [ ] Otros 7 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…de»; «…ro de Tarjeta de Identidad de Extranjero»; «…y cuya duración concluía el»; «…mporal y trabajo. SEGUNDO.- Por ello, en»; «…esidencia y trabajo. En el presente caso»; «…mposible o difícil reparación a causa de»; «…probatorios de los que pretendo valerme:»

## Elecciones que hay que hacer

- Procurador/a de los Tribunales / Letrado/a dotado/a de representación conforme al art. 23.1 de la LJCA
- Delegado del Gobierno / Subdelegado del Gobierno o autoridad autonómica
- Delegado del Gobierno / Subdelegado del Gobierno / autoridad autonómica de la Comunidad Autónoma

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Si NO solicita la apertura del procedimiento a prueba / Si solicita la apertura del procedimiento a prueba — el texto de cada opción no venía en el formulario original

## Párrafos opcionales (2)

Inclúyelos solo si encajan en los hechos:

- PRIMER OTROSÍ: Que solicito la adopción de la medida cautelar de suspensión de la ejecutividad de la resolució…
- SEGUNDO OTROSÍ: Conforme a los arts. 40 y 42 de la Ley 29/1998, de 13 de julio, reguladora de la Jurisdicción …

## Correcciones de la revisión (2)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- art. 23.1 de la LJCA
- art. 78 de la Ley 29/1998
- art. 78.1 del Real Decreto 1155/2024
- art. 19.1 de la Ley 29/1998
- art. 8 de la Ley 29/1998
- art. 14 de la Ley 29/1998
- art. 31.5 de la Ley Orgánica 4/2000
- art. 31.7 de la Ley Orgánica 4/2000
- art. 139 de la Ley 29/1998
- arts. 45.2 y 78.2 de la Ley 29/1998
- art. 78.2 de la LJCA
- art. 129 de la Ley 29/1998
- arts. 40 y 42 de la Ley 29/1998

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
