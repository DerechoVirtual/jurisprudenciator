---
name: redactar-demanda-despido
description: >-
  Redacta la demanda de despido disciplinario, objetivo o de fin de contrato temporal (LRJS arts. 103-113
  y 120-123; ET arts. 53-56) pidiendo la nulidad con su panorama de indicios (Ley 15/2022, LRJS arts.
  181-183) y, subsidiariamente, la improcedencia; alega la falta de audiencia previa al despido
  disciplinario, activa el trámite urgente si no se tramitó la baja (art. 103.4 LRJS), cita al FOGASA
  y al Fiscal cuando toca y cuantifica indemnización y salarios. Para el trabajador, la demanda; para la
  empresa demandada, la nota de defensa para el juicio (no hay contestación escrita). Úsala con «demanda
  de despido», «me han despedido», «despido nulo», «despido estando embarazada o de baja», «nos han
  demandado por despido». Si aún no hay papeleta, papeleta-conciliacion; si la empresa quiere redactar la
  carta, carta-despido-disciplinario o carta-despido-objetivo.
---

# Demanda de despido

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo, demanda, carga de la prueba, calificación y efectos** → `buscar_articulo` (`ley="LRJS"`, artículos `"10"`, `"43"`, `"80"`, `"103"`, `"104"`, `"105"`, `"108"`, `"110"` y `"113"`; en despido objetivo, además `"120"`, `"121"`, `"122"` y `"123"`).
- **Causa, forma y consecuencias del despido** → `buscar_articulo` (`ley="ET"`, artículos `"54"`, `"55"` y `"56"`; en objetivo, `"52"` y `"53"`; prescripción de faltas, `"60"`; garantías de representantes, `"68"`).
- **Nulidad y sus garantías** → `buscar_articulo` (`ley="LRJS"`, artículos `"96"`, `"178"`, `"179"`, `"181"`, `"183"` y `"184"`) y (`ley="BOE-A-2022-11589"`, artículos `"2"`, `"26"`, `"27"` y `"30"`); si es por razón de sexo, (`ley="BOE-A-2007-6115"`, artículos `"8"` y `"9"`).
- **Acumulación y FOGASA** → `buscar_articulo` (`ley="LRJS"`, artículos `"23"`, `"26"` y `"32"`; `ley="ET"`, `articulo="33"`).
- **Audiencia previa, suficiencia de la carta, nulidad y daño moral** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`; para la aplicación por los TSJ, `base="AN"`, `tipo_organo="TSJ"`, `provincia` = sede de la Sala) y (`base="TC"`) para indicios + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión).
- **Convenio aplicable y sus artículos** → `buscar_convenio` + `leer_convenio` (`buscar_en="faltas y sanciones"`, `buscar_en="despido"` para exigencias formales añadidas, categoría y complementos) + `vigencia_convenio` en la fecha del despido.
- **Empresa** → `buscar_empresa_mercantil` (denominación exacta, domicilio social, administradores, grupo, concurso o disolución).
- **Revisión del documento antes de entregarlo** → cada redactor pasa `verificar_escrito` sobre las frases de su sección que citan normas (no sobre el documento entero) y el ensamblado de `redaccion-rapida` comprueba que cada ECLI o ROJ citado figure entre las fuentes leídas; `buscar_por_cita` solo para una sentencia que aporte el abogado y no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). El Convenio 158 de la OIT y la disposición transitoria undécima del ET no los devuelve el conector: léelos en internet (instrumento de ratificación publicado en el BOE o base oficial de la OIT; texto consolidado del ET en el BOE) y cítalos con su enlace y la fecha de consulta, o a través del párrafo leído de la sentencia que los aplica (anclas, apartado 7).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Esta skill también está en el plugin de litigación laboral. En este plugin la usa el despacho que asesora a la empresa y además lleva sus despidos y reclamaciones, o que defiende al trabajador. **Pregunta primero a quién defiende el abogado**:

- **Trabajador**: demanda contra un despido disciplinario, un despido objetivo, la extinción de un contrato temporal que se considera fraudulento, un despido verbal o tácito, o la extinción por incapacidad permanente del art. 49.1.n ET (urgente, art. 120.2 LRJS). El objetivo es detectar por qué el despido no aguanta y pedir la calificación más favorable que se pueda sostener.
- **Empresa demandada**: no hay contestación escrita; el demandado contesta en el acto del juicio (art. 85.2 LRJS), expone primero y prueba los hechos de la carta (art. 105.1). Entrega una **nota de defensa** con los riesgos, la prueba que hay que llevar y la cifra para la conciliación judicial.

| Situación | Skill |
|---|---|
| No se ha presentado la papeleta o no se ha celebrado el acto | `papeleta-conciliacion` (despido no exento del art. 64 LRJS) |
| La empresa aún no ha despedido y quiere la carta | `carta-despido-disciplinario` o `carta-despido-objetivo` |
| Despido colectivo impugnado por los representantes o la empresa lo prepara | `despido-colectivo-empresa` |
| El trabajador sigue en la empresa y quiere irse por incumplimientos | `extincion-contrato-trabajador` (y el art. 32 LRJS si luego le despiden) |
| Vulneración de derechos fundamentales sin despido | `tutela-derechos-fundamentales` (con despido, siempre aquí: art. 184 LRJS) |
| Solo hay que cuantificar indemnización o salarios de tramitación | `calculo-indemnizacion-despido` |
| Sanción distinta del despido | `sanciones-disciplinarias` |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ A quién defiende el abogado.
2. ★ Fecha de efectos del despido, forma (carta, verbal, tácito) y, si hubo preaviso, su fecha; fecha de presentación de la papeleta, fecha y resultado del acto (o si pasaron quince días hábiles sin celebrarse).
3. ★ Carta de despido íntegra; en objetivo, además, si se puso a disposición la indemnización al entregarla, si hubo preaviso y si se dio copia a la representación legal.
4. ★ Antigüedad con todos los periodos (contratos anteriores encadenados, subrogaciones), categoría, salario real con sus conceptos (nóminas de los últimos doce meses), jornada, modalidad y duración del contrato, lugar de trabajo (art. 104.a LRJS).
5. ★ Si es o fue representante legal o sindical en el año anterior, y si está afiliado a un sindicato y la empresa lo sabía (art. 104.c y d LRJS; art. 55.1 ET).
6. ★ Si antes de despedir la empresa le dio ocasión de defenderse de los cargos (audiencia previa) y cómo.
7. ★ Indicios de nulidad, cada uno con fecha y documento: embarazo, permisos o adaptación de jornada solicitados o disfrutados, baja médica o enfermedad, reclamación o denuncia previa (también extrajudicial), afiliación o actividad sindical, violencia de género o sexual, comparativa con otros trabajadores.
8. ★ Si la empresa ha tramitado la baja en la Seguridad Social (art. 103.4 LRJS).
9. ★ Empresa exacta, grupo o contrata; convenio aplicable.
10. Cantidades vencidas y exigibles pendientes (finiquito, salarios) para acumular (art. 26.3 LRJS); solvencia de la empresa (FOGASA).
11. Si la readmisión es imposible (cierre, conflicto grave): permite pedir la extinción en sentencia (art. 110.1.b LRJS).
12. Si defiende a la empresa: expediente, pruebas de cada hecho de la carta, fecha en que conoció cada falta, régimen de faltas del convenio y margen para la conciliación judicial.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde».

**Plazo, órgano y calendario.**
- Veinte días hábiles de caducidad desde el despido, sin sábados, domingos ni festivos de la sede (art. 103.1 LRJS y art. 59.3 ET); en objetivo, desde el día siguiente a la extinción, pudiendo anticiparse desde el preaviso (art. 121.1). Agosto y del 24 de diciembre al 6 de enero cuentan (art. 43.4). Descuenta la suspensión de la papeleta (art. 65.1): calcula los días consumidos, la reanudación y la fecha límite, y ponlos en la nota.
- Error sobre quién es el empresario: nueva demanda o ampliación sin que corra la caducidad hasta que conste (art. 103.2).
- Órgano: Tribunal de Instancia, Sección de lo Social, del lugar de prestación de servicios o del domicilio del demandado, a elección del demandante (art. 10.1 LRJS; formato, apartado 3).
- Urgencia: si el trabajador manifiesta que no se ha tramitado su baja, el proceso es urgente y preferente, con vista en cinco días y sentencia en cinco (art. 103.4). Dilo en la demanda y en un otrosí.

**Contenido de la demanda.** Requisitos generales del art. 80 LRJS (modalidad procesal, hechos sin variación respecto de la papeleta, súplica) y los del art. 104 (antigüedad con periodos, categoría, salario, forma de pago, lugar, modalidad y duración, jornada; fecha y forma del despido y hechos alegados, con la carta; condición de representante; afiliación si se alega falta de audiencia a los delegados sindicales). Cada dato ausente, con marcador.

**Despido disciplinario.**
- Causas: incumplimiento grave y culpable del art. 54 ET. Forma: escrito con hechos y fecha de efectos; exigencias añadidas del convenio; expediente contradictorio si es representante; audiencia a los delegados sindicales si está afiliado y le consta a la empresa (art. 55.1 ET). Si falta la forma, improcedente (art. 55.4 ET y art. 108.1 LRJS).
- La empresa puede hacer un nuevo despido que cumpla lo omitido en los veinte días siguientes al primero (art. 55.2 ET): pregúntalo si defiende a la empresa, y compruébalo si defiende al trabajador.
- Prescripción de las faltas: plazos del art. 60.2 ET desde que la empresa las conoció y, en todo caso, desde su comisión; compara fechas de la carta con cada hecho.
- La empresa prueba los hechos de la carta y no puede alegar otros (art. 105 LRJS). Si los hechos probados no tienen gravedad suficiente pero son falta menor según el convenio, el juez puede autorizar una sanción adecuada (art. 108.1 LRJS, tercer párrafo): léelo y valóralo en la nota.
- **Audiencia previa (Convenio 158 OIT).** El Pleno de la Sala Cuarta (noviembre de 2024) la declaró exigible antes del despido disciplinario, salvo que no pueda pedirse razonablemente al empleador, y solo para despidos posteriores a la publicación de esa sentencia. Busca la del Pleno y la más reciente que la aplique (anclas, apartado 4), y en el TSJ de la sede cómo se está calificando su omisión. Cómo se alega: en HECHOS, que la empresa no comunicó los cargos ni dio ocasión de defenderse antes de decidir (fechas y documentos); en FUNDAMENTOS, el párrafo literal leído y la calificación que la doctrina anude a la omisión, como motivo autónomo o acumulado a los de fondo; y también en la papeleta. No afirmes la consecuencia sin haberla leído.

**Despido objetivo.** Causas del art. 52 ET; requisitos del art. 53.1 (comunicación escrita con la causa; puesta a disposición simultánea de la indemnización, salvo la excepción económica que debe constar en la carta; preaviso con copia a la representación en la letra c del art. 52). El incumplimiento determina la improcedencia, pero no la falta de preaviso ni el error excusable en la indemnización (art. 53.4 ET y art. 122.3 LRJS). Nulidad del art. 53.4 ET y del art. 122.2 LRJS (fraude eludiendo el despido colectivo). Percibir la indemnización no supone conformidad (art. 121.2).

**Nulidad.**
- Nulo el despido con móvil discriminatorio o con violación de derechos fundamentales, y en los supuestos objetivos del art. 55.5 ET, letras a) a c) (suspensiones por nacimiento y cuidado, riesgo durante el embarazo o la lactancia, embarazo, permisos y adaptaciones de jornada que enumera la letra b, víctimas de violencia de género o sexual, reincorporación tras el nacimiento), salvo que se declare procedente por motivos ajenos. Lee la lista vigente: la LO 1/2025 añadió supuestos.
- Ley 15/2022: la enfermedad o condición de salud es causa de discriminación (art. 2.1); son nulos los actos discriminatorios (art. 26); acreditada la discriminación se presume el daño moral (art. 27.1); con indicios fundados, la empresa debe dar una justificación objetiva, razonable y proporcionada (art. 30). Cita la ley con su fecha en cada mención.
- Carga: acreditados indicios de vulneración, corresponde al demandado justificar objetiva y razonablemente la medida (art. 96.1 y art. 181.2 LRJS). Construye el panorama indiciario: cada indicio con fecha, documento y conexión temporal con el despido.
- Con derechos fundamentales en juego se aplican las garantías de la tutela dentro de la modalidad de despido (arts. 178.2 y 184 LRJS): cita al Ministerio Fiscal y expresa la indemnización pretendida con sus bases (art. 179.3), compatible con la del despido (art. 183.3).
- Efectos: readmisión inmediata con abono de los salarios dejados de percibir (art. 55.6 ET y art. 113 LRJS).

**Improcedencia.** Opción de la empresa en cinco días entre readmisión con salarios de tramitación o indemnización de treinta y tres días por año, prorrateando por meses, con el tope del art. 56.1 ET; la opción es del trabajador si es representante (art. 56.4 ET y art. 110.2 LRJS). Puede anticiparse la opción en juicio y, si la readmisión no es realizable, pedirse que se tenga por hecha la opción por la indemnización en la sentencia (art. 110.1 LRJS). Si la sentencia llega pasados noventa días hábiles desde la demanda, la empresa puede reclamar al Estado los salarios de tramitación que excedan (art. 56.5 ET).

**Indemnización y antigüedad anterior al 12/02/2012.** Calcula con la tabla del apartado 7 del formato o con `calculo-indemnizacion-despido`. `buscar_articulo` **no devuelve la disposición transitoria undécima del ET** (probado con varias formas de pedirla): si la antigüedad es anterior a esa fecha, léela en internet en el texto consolidado del ET en el BOE (BOE-A-2015-11430) y cítala con su enlace y la fecha de consulta; como apoyo, el párrafo leído de una sentencia de la Sala Cuarta que aplique los dos tramos (`consulta="indemnización despido improcedente disposición transitoria antigüedad anterior 12 de febrero de 2012 tope 720 días"`, `base="TS"`).

**Acumulación y FOGASA.** Solo pueden acumularse al despido la extinción del contrato (dentro del plazo del despido), las cantidades vencidas, exigibles y de cuantía determinada y los daños derivados (art. 26.1 y 26.3 LRJS). Si antes hubo demanda de extinción del art. 50 ET, se acumulan y el juez decide el orden (art. 32.1). Cita al FOGASA si la empresa está en concurso, es insolvente o ha desaparecido (art. 23.2 LRJS).

## Estrategia y jurisprudencia

**Si defiende al trabajador**, ordena las causas de más a menos favorable y pide siempre la nulidad si hay indicios, con la improcedencia como subsidiaria (art. 108.3 LRJS: el juez se pronuncia sobre el móvil sea cual sea la forma):
1. Nulidad objetiva (art. 55.5 ET) y, además, nulidad por discriminación o vulneración de derechos fundamentales, con daño moral.
2. Improcedencia por forma: carta sin hechos concretos, falta de audiencia previa, de expediente o de audiencia sindical, requisitos del art. 53.1.
3. Improcedencia por fondo: hechos no probados, prescritos o sin gravedad según la graduación del convenio.

**Si defiende a la empresa**, la nota responde: ¿aguanta la carta?, ¿se dio audiencia previa (y si el despido es anterior al Pleno)?, ¿qué prueba acredita cada hecho y quién declara?, ¿hay indicios de nulidad que exijan justificación objetiva?, ¿cuánto cuesta cada escenario (procedente, improcedente con opción, nulo con salarios y daño moral)? Con ello propón la cifra para la conciliación judicial y, si procede, el reconocimiento de la improcedencia.

**Consultas** (reformula dos veces como máximo; lee solo lo que vayas a citar, `parrafos=3`, y transcribe fundamentos, nunca hechos ni datos de las partes):
- Audiencia previa: la consulta del apartado 4 de las anclas en `base="TS"`; después `consulta="omisión audiencia previa despido disciplinario Convenio 158 OIT improcedencia"`, `base="AN"`, `tipo_organo="TSJ"`, `fecha_desde="01/01/2025"`.
- Carta: `consulta="carta de despido disciplinario hechos genéricos indefensión suficiencia"`; en objetivo, `consulta="carta despido objetivo causas económicas concreción"`, `base="TS"`.
- Indicios: `consulta="prueba indiciaria vulneración derechos fundamentales inversión carga de la prueba despido"`, `base="TC"`; garantía de indemnidad: `consulta="garantía de indemnidad despido represalia reclamación extrajudicial"`, `base="TS"`.
- Enfermedad: `consulta="despido incapacidad temporal Ley 15/2022 enfermedad condición de salud nulidad"`, `base="AN"`, `tipo_organo="TSJ"` y después `base="TS"`.
- Daño moral: `consulta="indemnización daño moral despido nulo vulneración derechos fundamentales criterio orientativo LISOS"`, `base="TS"`. Si usas la LISOS como referencia, lee el tipo (`ley="BOE-A-2000-15060"`, `articulo="8"`) y la escala (`articulo="40"`) en el momento; no escribas importes de memoria.

## Documentos que se entregan

**1. Demanda** (`demanda-despido-<apellido-cliente>-<AAAAMMDD>.docx`), si defiende al trabajador, maquetada según el apartado 2 del formato:
1. Encabezamiento: «AL TRIBUNAL DE INSTANCIA DE [SEDE], SECCIÓN DE LO SOCIAL».
2. Comparecencia: `[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[DOMICILIO]`, representación; «formula DEMANDA DE DESPIDO» (modalidad, art. 80.1.a) contra `[DENOMINACIÓN SOCIAL]` (`[CIF]`, domicilio registral) y las demás demandadas; con citación del FOGASA y del Ministerio Fiscal cuando proceda.
3. HECHOS en ordinales: PRIMERO, relación laboral con todos los datos del art. 104.a; SEGUNDO, despido (fecha, forma, hechos imputados, con la carta como documento); TERCERO, por qué no se sostiene (forma, audiencia, prescripción, falsedad o falta de gravedad), un apartado por motivo; CUARTO, indicios de nulidad uno a uno con fecha y documento; QUINTO, condición de representante o afiliación, o su ausencia; SEXTO, baja en la Seguridad Social; SÉPTIMO, cantidades acumuladas en tabla; OCTAVO, conciliación previa (fechas y resultado).
4. FUNDAMENTOS DE DERECHO: jurisdicción y competencia (art. 2.a, art. 6 y art. 10.1 LRJS); conciliación previa y plazo (arts. 63, 65 y 103 LRJS); modalidad y carga de la prueba (arts. 103 a 105 LRJS, y 120 a 122 en objetivo); nulidad (art. 55.5 ET, art. 108.2 LRJS, Ley 15/2022, arts. 96.1 y 181.2 LRJS y doctrina leída); improcedencia (arts. 55.4 y 56 ET, arts. 108.1 y 110 LRJS, audiencia previa con el párrafo de la sentencia); indemnización por vulneración (arts. 179.3 y 183 LRJS, con las bases); convenio con su código. Cada fundamento con su propia secuencia (formato, apartado 2).
5. SUPLICO: sentencia que declare nulo el despido, con readmisión inmediata y abono de los salarios dejados de percibir, y condena a `[IMPORTE]` por daño moral; subsidiariamente, improcedente, con condena a readmitir con salarios de tramitación o a indemnizar con `[IMPORTE]` a opción de la empresa (del trabajador si es representante) y, si la readmisión no es realizable, con extinción en sentencia (art. 110.1.b LRJS); las cantidades acumuladas, con el interés del art. 29.3 ET en las de naturaleza salarial; la responsabilidad del FOGASA en su caso.
6. OTROSÍES: tramitación urgente (art. 103.4), si procede; prueba: interrogatorio con el apercibimiento del art. 91.2 LRJS, documental en poder de la empresa (expediente, registro de jornada, comunicaciones) pedida como diligencia de preparación (art. 90.3) con el apercibimiento del art. 94.2, testifical y pericial.
7. Lugar, fecha y firma; relación de documentos.

**Reparto para la redacción rápida:** encabezamiento, comparecencia y hechos (PRIMERO a OCTAVO; dos secciones si pasan de 1.200 palabras) / fundamentos procesales (jurisdicción, competencia, conciliación y plazo, modalidad y carga de la prueba) / nulidad (art. 55.5 ET, discriminación, indicios, derechos fundamentales y daño moral) / improcedencia (forma y audiencia previa, fondo e indemnización) / súplica, otrosíes, firma y documentos.

**2. Hoja de cálculo**, solo si el abogado la pide (si no, la tabla va en el resumen): `calculo-indemnizacion-<apellido-trabajador>-<AAAAMMDD>.docx`, con la tabla del apartado 7 del formato (salario anual, diario, antigüedad, días por año, tope, resultado, salarios de tramitación por día).

**3. Nota**, solo si el abogado la pide o si es el único entregable, porque se defiende a la parte para la que esta skill no redacta documento (si no se entrega aparte, lo que esta skill manda «a la nota» va en el resumen de la entrega), `nota-despido-<empresa>-<AAAAMMDD>.docx`: para el trabajador, plazo con fechas, riesgos y prueba que falta; para la empresa, la nota de defensa descrita arriba, con la exposición económica por escenario en tabla. En ambas, la jurisprudencia literal usada.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado (incluida la doctrina de audiencia previa en todo despido disciplinario).
- [ ] Leídos en esta conversación LRJS 10, 43, 80, 103, 104, 105, 108, 110 y 113; ET 54, 55, 56 y 60 (52 y 53 y LRJS 120 a 123 en objetivo; ET 49 si es la extinción de su letra n); y los de nulidad, acumulación y FOGASA que se citen.
- [ ] Convenio con su código y su vigencia en la fecha del despido; exigencias formales y graduación de faltas contrastadas.
- [ ] Empresa comprobada con `buscar_empresa_mercantil`.
- [ ] Plazo con fecha del despido, días consumidos, suspensión por la papeleta y fecha límite, con sus preceptos.
- [ ] Hechos de la demanda iguales a los de la papeleta (art. 80.1.c LRJS); lo nuevo, justificado como nuevo o desconocido.
- [ ] Cálculos en tabla con cada operación; antigüedad anterior al 12/02/2012 calculada con la disposición transitoria undécima leída en el BOE consolidado (enlace y fecha) o remitida a `calculo-indemnizacion-despido`.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; párrafos de fundamentos, sin datos de aquel pleito.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero); avisos de «posible disonancia» (por ejemplo, art. 181 LRJS, cuyo título es «Conciliación y juicio») contrastados con el apartado leído; su veredicto sobre el Convenio 158 de la OIT ignorado (anclas, apartado 7).
- [ ] Marcadores en lugar de datos no facilitados; ningún importe de sanción de la LISOS escrito de memoria.
- [ ] Los datos obtenidos en internet (Convenio 158 de la OIT, disposición transitoria undécima, denominación del órgano si hizo falta) figuran con su enlace en el documento y en el resumen.
- [ ] Resumen para el abogado según el apartado 9 del formato.
