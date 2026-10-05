---
name: periodo-prueba
description: >-
  Pacta el periodo de prueba y resuelve su finalización: redacta en Word la cláusula del contrato o la
  comunicación de no superación (con nota de riesgos, si la pides). Úsala cuando la empresa pregunte «¿cuánto periodo de
  prueba le pongo?», «quiero cesarle en la prueba» o «no ha superado el periodo de prueba», y cuando el
  trabajador diga «me han echado en la prueba estando embarazada / de baja» o «ya había trabajado allí
  antes». Comprueba los límites del art. 14 ET y del convenio, la forma escrita, la nulidad del pacto si ya
  desempeñó las funciones y la nulidad del cese por embarazo o por discriminación (Ley 15/2022). Sirve a
  empresa y trabajador. Para elegir la modalidad del contrato, contrato-trabajo-modalidad; para impugnar un
  cese ya comunicado, papeleta-conciliacion y redactar-demanda-despido; en alta dirección, alta-direccion.
---

# Periodo de prueba: pacto y resolución

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Límites, forma, nulidad del pacto, embarazo e interrupciones** → `buscar_articulo` (`ley="ET"`, `articulo="14"`), y para la suspensión a la que remite → (`ley="ET"`, `articulo="48"`).
- **Reglas especiales por modalidad** → `buscar_articulo` (`ley="ET"`, `articulo="11"`: alternancia y práctica profesional) y, si es alto directivo, (`ley="BOE-A-1985-17006"`, `articulo="5"`).
- **Discriminación y carga de la prueba** → `buscar_articulo` (`ley="BOE-A-2022-11589"`, artículos `"2"`, `"4"`, `"9"`, `"26"`, `"27"` y `"30"`), (`ley="BOE-A-2007-6115"`, `articulo="8"`), (`ley="ET"`, artículos `"4"`, `"17"` y `"55"`) y (`ley="LRJS"`, artículos `"96"` y `"183"`).
- **Plazo para impugnar el cese** → `buscar_articulo` (`ley="ET"`, `articulo="59"`) y (`ley="LRJS"`, artículos `"103"`, `"65"` y `"43"`).
- **Duración, cómputo y forma según el convenio** → `buscar_convenio` + `leer_convenio` (`buscar_en="periodo de prueba"`) + `vigencia_convenio`.
- **Doctrina sobre nulidad del pacto, embarazo, enfermedad y sucesión de empresa** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; o `base="AN"` + `tipo_organo="TSJ"` + `provincia` sede de la Sala) + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión).
- **Empresa** → `buscar_empresa_mercantil` (denominación exacta y CIF para la comunicación).
- **Revisión del documento antes de entregarlo** → cada redactor pasa `verificar_escrito` sobre las frases de su sección que citan normas (no sobre el documento entero) y el ensamblado de `redaccion-rapida` comprueba que cada ECLI o ROJ citado figure entre las fuentes leídas; `buscar_por_cita` solo para una sentencia que aporte el abogado y no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). Cita la Ley 15/2022 con su fecha («artículo 30 de la Ley 15/2022, de 12 de julio, integral para la igualdad de trato y la no discriminación»): así la reconoce `verificar_escrito`.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Identifica primero **qué momento es** y **a quién defiende el abogado**:

| Momento | Empresa | Trabajador |
|---|---|---|
| A. Antes de firmar | Redactar la cláusula dentro de los límites | Revisar si el periodo pactado es válido |
| B. Durante la prueba | Decidir si cesar, comprobar riesgos y redactar la comunicación | Saber si el cese anunciado sería nulo |
| C. Cese ya comunicado | Valorar la defensa | Detectar por qué no aguanta y calcular el plazo de 20 días hábiles |

| Situación | Skill |
|---|---|
| Hay que elegir o redactar el contrato entero | `contrato-trabajo-modalidad` (esta skill le entrega la cláusula) |
| Alto directivo | `alta-direccion` (periodo de prueba del art. 5 del Real Decreto 1382/1985) |
| El cese ya se produjo y se va a impugnar | papeleta con `papeleta-conciliacion` y demanda con `redactar-demanda-despido`; esta skill aporta el análisis |
| Se quiere pedir además indemnización por vulneración de derechos fundamentales | `tutela-derechos-fundamentales` para su fundamentación |
| Liquidación de lo trabajado al cesar | `finiquito-liquidacion` |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ A quién defiende el abogado y en qué momento (A, B o C).
2. ★ Modalidad y duración del contrato (indefinido, temporal y su duración, formativo en alternancia o para la práctica profesional, alta dirección).
3. ★ Grupo profesional, funciones y si el trabajador es **técnico titulado** (titulación exigida por el puesto, no solo poseída).
4. ★ Plantilla total de la empresa (umbral de veinticinco trabajadores del art. 14.1 ET).
5. ★ Convenio aplicable (denominación y código) o encarga antes `convenio-aplicable`.
6. ★ **Servicios anteriores en la empresa** o en la empresa de la que procede por sucesión o subrogación, bajo cualquier modalidad (también becas, prácticas o puesta a disposición por ETT): fechas y funciones.
7. En B y C: ★ fecha de inicio, fecha de la decisión y fecha de efectos; si el pacto consta por escrito (pide el contrato firmado); suspensiones durante la prueba (incapacidad temporal, nacimiento, riesgo durante el embarazo…) y si se pactó que interrumpen el cómputo.
8. En B y C: ★ **factores de riesgo**: embarazo (si la empresa lo conocía, desde cuándo y cómo lo supo), nacimiento o cuidado de menor reciente, incapacidad temporal o enfermedad, reclamaciones previas del trabajador, afiliación o actividad sindical, discapacidad, solicitud de adaptación de jornada o de permisos, cualquier otra causa del art. 2.1 de la Ley 15/2022.
9. En B: motivos reales de la empresa y pruebas objetivas (evaluaciones, incidencias, objetivos, correos) anteriores al conocimiento del factor de riesgo.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde».

**Validez del pacto (art. 14.1 ET)**:

- Por escrito. Sin pacto escrito no hay periodo de prueba y el cese es un despido.
- Duración: la del convenio; en su defecto, seis meses para técnicos titulados y dos meses para los demás; en empresas de menos de veinticinco trabajadores, tres meses para los que no sean técnicos titulados. En temporales del art. 15 de hasta seis meses, un mes salvo convenio. Si el convenio fija límites, mandan los del convenio: léelos con `leer_convenio` y comprueba que el texto estaba vigente al firmar (`vigencia_convenio`).
- Nulo el pacto si el trabajador **ya desempeñó las mismas funciones en la empresa**, bajo cualquier modalidad de contratación. Compara funciones, no categorías.
- Formativos: en alternancia **no puede pactarse** (art. 11.2.l ET); en la práctica profesional, máximo de un mes salvo convenio (art. 11.3.e); si el trabajador sigue tras el formativo, no hay nuevo periodo (art. 11.4.g).
- Alta dirección: máximo de nueve meses si el contrato es indefinido (art. 5 del Real Decreto 1382/1985).
- Ambas partes están obligadas a realizar las experiencias que constituyen su objeto: una prueba en funciones distintas de las contratadas no sirve para valorar la aptitud.

Tabla de control (límites legales en defecto de convenio; el del convenio prevalece, léelo siempre):

| Supuesto | Límite | Precepto |
|---|---|---|
| Técnico titulado | seis meses | art. 14.1 ET |
| Resto de trabajadores | dos meses | art. 14.1 ET |
| Resto de trabajadores en empresa de menos de 25 | tres meses | art. 14.1 ET |
| Temporal del art. 15 de hasta seis meses | un mes, salvo convenio | art. 14.1 ET |
| Formativo en alternancia | no cabe | art. 11.2.l ET |
| Formativo para la práctica profesional | un mes, salvo convenio | art. 11.3.e ET |
| Alto directivo con contrato indefinido | nueve meses | art. 5 del Real Decreto 1382/1985 |

**Cómputo e interrupciones**:

- Los plazos por meses se computan de fecha a fecha (art. 5 del Código Civil), salvo que el convenio lo fije en días de trabajo efectivo u otra unidad: sigue su redacción literal.
- Incapacidad temporal, nacimiento, adopción, guarda, acogimiento, riesgo durante el embarazo o la lactancia y violencia de género **solo interrumpen** el cómputo si hay acuerdo de ambas partes (art. 14.3 ET); comprueba si el contrato o el convenio lo pactan.
- Superado el plazo sin desistimiento, el contrato despliega plenos efectos y el tiempo computa en la antigüedad (art. 14.3). La decisión comunicada después del último día de la prueba ya es un despido.

**Resolución durante la prueba (art. 14.2 ET)**:

- Cualquiera de las partes puede resolver sin causa ni preaviso legales; comprueba si el convenio exige forma o preaviso.
- **Embarazo**: la resolución a instancia de la empresa es nula desde el inicio del embarazo hasta el comienzo de la suspensión del art. 48.4, o por maternidad, salvo que concurran motivos no relacionados con el embarazo o la maternidad, que tiene que acreditar la empresa. El precepto no menciona el conocimiento del embarazo por la empresa: no afirmes si es necesario sin la doctrina de la Sala del territorio (consulta de «Estrategia»).
- **Otras causas de discriminación**: el art. 14.2 solo enumera el embarazo y la maternidad. Para el resto (enfermedad o condición de salud, discapacidad, conciliación, sindicación, represalia por reclamar…), el desistimiento es nulo si es discriminatorio: arts. 2.1, 4, 9.1 y 26 de la Ley 15/2022, art. 8 de la Ley Orgánica 3/2007 (embarazo como discriminación directa por sexo), arts. 4.2.c y 17.1 ET. Con indicios fundados, la empresa debe probar una justificación objetiva, razonable y proporcionada (art. 30 de la Ley 15/2022 y art. 96 LRJS).
- **Efectos**: pacto nulo o cese fuera de plazo → despido improcedente (o nulo si hay discriminación); nulidad → readmisión inmediata con abono de los salarios dejados de percibir (art. 55.6 ET) e indemnización por daño moral (art. 183 LRJS; el art. 27 de la Ley 15/2022 presume el daño moral acreditada la discriminación).
- **Plazo del trabajador**: caducidad de 20 días hábiles desde la fecha de efectos (art. 59.3 ET y art. 103 LRJS); la papeleta de conciliación suspende la caducidad en los términos del art. 65 LRJS (léelo: se reformó en 2025); en despido, agosto y del 24 de diciembre al 6 de enero son hábiles (art. 43.4 LRJS). Da la fecha final calculada.

## Estrategia y jurisprudencia

**Si defiende a la empresa (momento A)**: pacta la duración máxima que permita el convenio para ese grupo, por escrito y en el propio contrato; incluye la interrupción por las situaciones del art. 14.3 (necesita el acuerdo, y la firma del contrato lo documenta); describe las funciones que se probarán. No pactes prueba si hubo servicios anteriores con las mismas funciones ni en alternancia.

**Si defiende a la empresa (momento B)**: antes de redactar, pasa este filtro y ponlo en la nota:

1. ¿Hay pacto escrito válido y el plazo sigue abierto en la fecha de efectos?
2. ¿Hubo servicios previos con las mismas funciones, también con el empresario anterior en una sucesión?
3. ¿Concurre algún factor de riesgo del dato 8? Si concurre, la decisión solo aguanta con motivos objetivos anteriores y documentados. Recomienda no cesar hasta reunirlos y dilo con claridad al abogado.

La comunicación no necesita expresar la causa. Ofrece dos versiones cuando haya factor de riesgo: una neutra y otra que enuncie los motivos objetivos ya documentados; la elección es del abogado, y la nota explica que la neutra obliga a probar esos motivos en el juicio igualmente.

**Si defiende al trabajador (momentos B y C)**: busca por qué no aguanta: falta de pacto escrito, duración superior a la del convenio o la ley, funciones ya desempeñadas (también con el empresario anterior en una sucesión), formativo en alternancia, cese comunicado fuera de plazo, embarazo, o indicios de discriminación por enfermedad, conciliación o represalia (cronología: factor de riesgo → cese en pocos días). Pide nulidad y, subsidiariamente, improcedencia.

Consultas (reformula como máximo dos veces; `anios=5` para doctrina reciente):

- Pacto nulo por funciones previas: `consulta="nulidad periodo de prueba trabajador ya había desempeñado las mismas funciones"`, `base="TS"`; en sucesión, añade `"sucesión de empresa trabajador subrogado"`.
- Embarazo: `consulta="desistimiento periodo de prueba embarazo nulo motivos no relacionados"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia` sede de la Sala; y `base="TS"` con `consulta="periodo de prueba desistimiento trabajadora embarazada nulidad"`.
- Enfermedad o incapacidad temporal: `consulta="desistimiento periodo de prueba incapacidad temporal enfermedad discriminación Ley 15/2022 nulidad"`, `base="AN"`, `tipo_organo="TSJ"`, `fecha_desde="14/07/2022"` (entrada en vigor de la Ley 15/2022).
- Indicios y carga de la prueba: `consulta="periodo de prueba discriminación indicios carga de la prueba"`, `base="TC"`. La doctrina constitucional anterior a la regla del embarazo del art. 14.2 exigía indicios aportados por la trabajadora: úsala solo para la mecánica de indicios y dilo.

Lee con `leer_sentencias` (`parrafos=3`, `terminos="periodo de prueba"` más la cuestión) solo lo que vayas a citar. Mucha resolución del Supremo en esta materia es un auto de inadmisión por falta de contradicción: no lo cites como doctrina. En la cláusula y en la comunicación no va jurisprudencia; va a la nota (formato, apartado 1).

## Documentos que se entregan

1. **Cláusula de periodo de prueba** (momento A), lista para insertar en el contrato de `contrato-trabajo-modalidad`: duración y su fundamento (convenio con artículo y código, o art. 14.1 ET), funciones objeto de la prueba, interrupción pactada por las situaciones del art. 14.3, cómputo del tiempo en la antigüedad. Si se entrega suelta: `contrato-clausula-periodo-prueba-<apellido-trabajador>-<AAAAMMDD>.docx`.
2. **Comunicación de no superación del periodo de prueba** (momento B), con el formato de carta del apartado 2 del formato: `carta-no-superacion-periodo-prueba-<apellido-trabajador>-<AAAAMMDD>.docx`.
   - Membrete (`[DENOMINACIÓN SOCIAL]`, `[CIF]`), destinatario, lugar y fecha, asunto.
   - Cuerpo: referencia a la cláusula del contrato y a su fecha; decisión de resolver el contrato durante el periodo de prueba al amparo del art. 14.2 ET; **fecha de efectos**, que debe caer dentro del plazo; puesta a disposición de la liquidación; versión con motivos si el abogado la elige.
   - Firma de la empresa y recibí con fecha (o constancia de la negativa ante testigos).
   - **Reparto para la redacción rápida:** la cláusula (1 página) y la comunicación (1-2 páginas) son cortas: una sección cada una, sin equipo.
3. **Nota para el abogado**, solo si el abogado la pide o si es el único entregable, porque se defiende a la parte para la que esta skill no redacta documento (si no se entrega aparte, lo que esta skill manda «a la nota» va en el resumen de la entrega): `nota-periodo-prueba-<empresa>-<AAAAMMDD>.docx`. Validez del pacto (forma, duración frente a ley y convenio, funciones previas); cálculo del plazo con fecha inicial, interrupciones y último día; factores de riesgo y prueba disponible; valoración (bajo, medio, alto) del riesgo de nulidad; jurisprudencia con párrafo literal; si defiende al trabajador, calificación que se pedirá y fecha final de los 20 días hábiles.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos en esta conversación el art. 14 ET y los que se citen (11, 48, 4, 17, 55 y 59 ET; 96, 103, 65, 43 y 183 LRJS; arts. 2, 4, 9, 26, 27 y 30 de la Ley 15/2022; art. 8 de la Ley Orgánica 3/2007; art. 5 del Real Decreto 1382/1985).
- [ ] Convenio leído en su artículo de periodo de prueba, con código y vigencia en la fecha del pacto.
- [ ] Duración pactada comparada con la del convenio o la ley para el grupo y la plantilla; funciones previas descartadas o analizadas.
- [ ] Último día del periodo y fecha de efectos calculados; en el momento C, fecha final del plazo de 20 días hábiles con su precepto.
- [ ] Factores de riesgo listados y, si existen, advertencia expresa al abogado.
- [ ] Cada ECLI de la nota leído con `leer_sentencias` o comprobado con `buscar_por_cita`; ninguno en la cláusula ni en la carta; ningún auto de inadmisión citado como doctrina.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero) y corregido lo que señale.
- [ ] Marcadores en lugar de datos no facilitados; si algún dato no sale de Jurisprudenciator, procede de una fuente oficial con enlace y fecha de consulta, y el resumen lo identifica.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado, plazo y fecha límite con su precepto, riesgos, documentos que faltan, tabla de jurisprudencia y próximo paso.
