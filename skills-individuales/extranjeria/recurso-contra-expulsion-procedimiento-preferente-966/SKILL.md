---
name: recurso-contra-expulsion-procedimiento-preferente-966
description: "Redacta el escrito «Recurso contra la expulsión del procedimiento preferente» (formulario 966 de extranjería, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Recurso contra la expulsión del procedimiento preferente

> Formulario 0966 del plugin **Extranjería** · revisado el 17-11-2026. Uso interno.

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

- Las letras del art. 57.1 citadas no cuadran: las infracciones a que se refiere son las de las letras a), b), c), d) y f) del art. 53.1 LO 4/2000. Procedimiento preferente: arts. 233-236 RD 1155/2024.
- Expedientes presentados antes del 20-5-2025: se tramitan con la norma vigente al presentarse (RD 557/2011) salvo que el interesado pida la nueva (DT 2.ª RD 1155/2024); en esos casos la cita al RD 557/2011 puede ser la correcta.

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (3 veces)
- [ ] NOMBRE DEL REPRESENTADO/A (3 veces)
- [ ] COLEGIO
- [ ] DOMICILIO A EFECTOS DE NOTIFICACIONES
- [ ] LOCALIDAD
- [ ] LUGAR
- [ ] FECHA
- [ ] Otros 18 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…eción a los siguientes: HECHOS PRIMERO.-»; «…SEGUNDO.-»; «…ición potestativo suprímase este ordinal»; «…da en sus legítimos intereses formuló en»; «… el cual ha sido desestimado por otra de»; «…por haber sido dictada la resolución por»; «…crito de demanda, rechazó la práctica de»; «…eben ser reducidas al máximo. Pues bien,»; «…. 2º.-»; «…ORGANO PARA LA RESOLUCIÓN DEL EXPEDIENTE»; «…- CONCURRENCIA DE SANCIONES»; «…de expulsión al amparo de una motivación»; …

## Elecciones que hay que hacer

- PÚBLICA / PRIVADA

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA OPCIÓN Y REDACTARLA: Si no se ha formulado recurso de reposición / Si ya se había formulado recurso de reposición y este ha sido desestimado — el texto de cada opción no venía en el formulario original
- ELEGIR UNA OPCIÓN Y REDACTARLA: Si se solicita celebración de la vista / Si NO se solicita celebración de la vista — el texto de cada opción no venía en el formulario original
- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS

## Párrafos opcionales (16)

Inclúyelos solo si encajan en los hechos:

- D./Dª [NOMBRE Y APELLIDOS] Procurador/a de los Tribunales, actuando en nombre y representación de [NOMBRE DEL …
- D/Dª [NOMBRE Y APELLIDOS], Procurador/a de los Tribunales, actuando en nombre y representación de [NOMBRE DEL …
- D/Dª [NOMBRE Y APELLIDOS], Letrado del Ilustre Colegio de [COLEGIO] con domicilio a efectos de notificaciones …
- TERCERO.- (Si no se dedujo recurso de reposición potestativo suprímase este ordinal [COMPLETAR])…
- - FALTA DE COMPETENCIA DEL ORGANO PARA LA RESOLUCIÓN DEL EXPEDIENTE [COMPLETAR]…
- - FALTA DE TIPICIDAD DE LOS HECHOS.…
- - CONCURRENCIA DE SANCIONES [COMPLETAR]…
- - PRESCRIPCIÓN DE LA INFRACCIÓN.…
- - CADUCIDAD DEL PROCEDIMIENTO.…
- - ILEGALIDAD DE LA INTERVENCIÓN DE LOS BIENES EMPLEADOS PARA LA SUPUESTA COMISICIÓN DE LA INFRACCIÓN.…
- I.- DOCUMENTAL.- Que se reproduzcan en dicho ramo probatorio los documentos obrantes en el expediente administ…
- II.- MAS DOCUMENTAL [ELEGIR: PÚBLICA / PRIVADA].…
- III.- INTERROGATORIO DE TESTIGOS.-…
- IV.- DICTAMEN DE PERITOS.-…
- V.- INTERROGATORIO DE LAS PARTES.-…
- VI.- RECONOCIMIENTO JUDICIAL.-.…

## Correcciones de la revisión (3)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- art. 78 de la Ley 29/1998
- art. 78 de la LJCA
- art. 19.1 de la LJCA
- art. 8 de la LJCA
- art. 14 de la LJCA
- art. 53 Ley 39/2015
- art. 24.2 de la Constitución
- artículos 55.3 y 4 de la Ley Orgánica 4/2000
- art. 57.1 de la Ley Orgánica 4/2000
- art. 29 de la Ley 40/2015
- art. 55.3 de la Ley Orgánica 4/2000
- art. 139.1 de la LJCA
- art. 78.2 LJCA
- art. 45.2 de la LJCA
- art. 78.2 de la LJCA
- artículo 129.1 de la LJCA
- art. 130.1 LJCA
- art. 133 LJCA
- arts. 40 y 42 de la LJCA
- art. 60 de la LJCA
- art. 60.1 de la LJCA
- art. 4 de la Ley 1/2000
- art. 78.1 de la LJCA
- Ley Orgánica 2/2009
- Real Decreto 1155/2024

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
