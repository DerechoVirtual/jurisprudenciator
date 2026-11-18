---
name: conciliacion-laboral-personal-familiar-demanda-generica-124
description: "Redacta el escrito «Conciliación laboral, personal y familiar: demanda genérica de derechos» (formulario 124 de jornada, permisos y conciliación, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Conciliación laboral, personal y familiar: demanda genérica de derechos

> Formulario 0124 del plugin **Jornada, permisos y conciliación** · revisado el 17-11-2026. Uso interno.

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

- El art. 37.6 ET (reducción por cuidado de menor con cáncer o enfermedad grave) fue modificado por el RDL 31/2026 (BOE-A-2026-21872, vigente desde el 23-10-2026): extensión más allá de los 23 y 26 años con discapacidad del 65 % o grado III de dependencia, tratamiento continuado sin hospitalización y disfrute por ambos progenitores de forma alternativa o simultánea.
- Adaptación del art. 34.8 ET: hasta que los hijos cumplan doce años, negociación de 15 días con presunción de concesión si no hay oposición motivada, y nulidad objetiva del despido o extinción por solicitarla o disfrutarla (arts. 53.4.b y 55.5.b, redacción LO 1/2025).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (3 veces)
- [ ] LOCALIDAD (3 veces)
- [ ] ACTO O RESOLUCIÓN
- [ ] NIF
- [ ] FECHA (5 veces)
- [ ] IMPORTE (3 veces)
- [ ] TELÉFONO
- [ ] CORREO ELECTRÓNICO
- [ ] LUGAR
- [ ] Otros 16 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…, provisto/a de DNI (NIE)»; «…con domicilio en [LOCALIDAD] de»; «…, y domicilio en [LOCALIDAD], de»; «…halla encuadrado/a profesionalmente como»; «…tes se rige por el Convenio colectivo de»; «…egal vigente iba a ejercer el derecho de»; «…o derecho en las siguientes condiciones:»; «…ho, en base a los siguientes argumentos:»; «… actora que se le reconozca el derecho a»; «…e su derecho por aplicación del artículo»; «…anda se declare el derecho del actor/a a»; «…en las siguientes condiciones»; …

## Párrafos opcionales (5)

Inclúyelos solo si encajan en los hechos:

- PRIMER OTROSÍ DIGO: Que a efectos de práctica de prueba de interrogatorio de parte interesa que se cite al leg…
- SEGUNDO OTROSÍ DIGO: Que a efectos de práctica de prueba interesa esta parte que en el acto del juicio se apor…
- TERCER OTROSÍ DIGO: Que compareceré al acto del juicio asistido/a de letrado/a que me dirija y defienda, desig…
- CUARTO OTROSÍ DIGO: Que, de conformidad con lo previsto en el artículo 64.1 LRJS esta modalidad procesal está …
- QUINTO OTROSÍ DIGO: Que esta parte aportará a los actos de conciliación y juicio su propuesta y alternativa de…

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículo 139 de la LRJS
- artículo 139 de la Ley 36/2011
- artículos 2.1, 3.1, 4, 9.1 y 9.5 de la Ley Orgánica 6/1985
- artículos 2, 6 y 10 LRJS
- artículo 17.1 LRJS
- artículo 139 LRJS
- artículo 91.2 LRJS
- artículo 64.1 LRJS

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
