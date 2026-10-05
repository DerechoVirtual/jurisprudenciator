---
name: despido-colectivo-empresa
description: >-
  Organiza para la empresa un despido colectivo por causas económicas, técnicas, organizativas o de producción
  (art. 51 ET y Real Decreto 1483/2012): comprueba umbrales en 90 días y fraude por goteo, prepara el plan de
  trabajo con calendario, la comunicación de intención, la de apertura del periodo de consultas con su contenido y
  documentación, y, si la pides, una nota de riesgos (nulidad, convenio especial para mayores de 55 años, plan de recolocación,
  aportación al Tesoro, prioridades de permanencia, impugnación del art. 124 LRJS). Úsala con «ERE», «despido
  colectivo», «cerrar un centro», «despedir a 12 personas», «periodo de consultas». Sirve a la empresa. Por debajo
  de los umbrales, carta-despido-objetivo; si la medida es temporal, erte-suspension-reduccion.
---

# Despido colectivo desde la empresa

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Umbrales, causas, procedimiento, prioridades y obligaciones accesorias** → `buscar_articulo` (`ley="ET"`, artículos `"51"`, `"41"` —apartado 4, interlocutores—, `"53"`, `"64"` y `"68"`) y (`ley="LOLS"`, `articulo="10"`).
- **Procedimiento reglamentario** → `buscar_articulo` (`ley="BOE-A-2012-13419"`, artículos `"1"` a `"14"` —el 5 es la documentación de las causas técnicas, organizativas y productivas y el 6 la comunicación a la autoridad laboral—, `"25"`, `"26"`, `"27"` y `"28"`; fuerza mayor, `"31"` a `"33"`).
- **Convenio especial de mayores de 55 años** → `buscar_articulo` (`ley="BOE-A-2003-19281"`, `articulo="20"`, Orden TAS/2865/2003).
- **Aportación al Tesoro por trabajadores de 50 o más años** → `buscar_articulo` (`ley="BOE-A-2012-13420"`, artículos `"1"`, `"2"` y `"3"`, Real Decreto 1484/2012).
- **Impugnación y órgano** → `buscar_articulo` (`ley="LRJS"`, artículos `"124"`, `"122"`, `"148"`, `"7"`, `"8"` y `"43"`); **desempleo** → (`ley="LGSS"`, `articulo="267"`).
- **Disposiciones adicionales que el conector no devuelve** (convenio especial y aportación al Tesoro) y **órgano concreto de la autoridad laboral** → internet, en la fuente oficial: ver «Huecos».
- **Doctrina imprescindible** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`) con las consultas del apartado de estrategia (umbrales y cómputo, buena fe y documentación, criterios de selección, comunicación de la decisión final) + `leer_sentencias` (`parrafos=3`); Directiva 98/59 → `base="TJUE"`.
- **Convenio aplicable y sus artículos** (prioridades de permanencia pactadas, procedimientos propios) → `buscar_convenio` + `leer_convenio` (`buscar_en="permanencia"` o `buscar_en="despido colectivo"`; después `articulo="N"`) + `vigencia_convenio`. Si `vigencia_convenio` registra un texto posterior al que devuelve `leer_convenio`, localiza su publicación con `novedades_boe` (`contiene` = denominación, `desde` y `hasta`) y léela con `leer_boe`; si llega truncada, lee el texto completo en el boletín oficial y cítalo con su enlace.
- **Empresa y grupo** → `buscar_empresa_mercantil` (denominación, administradores, vínculos de grupo que obliguen a aportar documentación de otras sociedades, concurso).
- **Revisión del documento antes de entregarlo** → cada redactor pasa `verificar_escrito` sobre las frases de su sección que citan normas (no sobre el documento entero) y el ensamblado de `redaccion-rapida` comprueba que cada ECLI o ROJ citado figure entre las fuentes leídas; `buscar_por_cita` solo para una sentencia que aporte el abogado y no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). En los documentos, cita el reglamento como «artículo N del Real Decreto 1483/2012, de 29 de octubre», la orden como «artículo 20 de la Orden TAS/2865/2003, de 13 de octubre» y el de aportaciones como «artículo N del Real Decreto 1484/2012, de 29 de octubre»: así los reconoce `verificar_escrito`.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Para la **empresa** que va a extinguir contratos por causas económicas, técnicas, organizativas o de producción y alcanza (o puede alcanzar) los umbrales, o que cierra totalmente con más de cinco trabajadores.

| Situación | Skill que procede |
|---|---|
| Las extinciones en 90 días no alcanzan los umbrales | esta skill entrega solo la nota de umbrales (apartado «Si no se alcanza el umbral») y las cartas se hacen con `carta-despido-objetivo` |
| La causa es coyuntural: basta suspender o reducir jornada | `erte-suspension-reduccion` |
| Se defiende a los representantes o a un trabajador afectado frente al despido colectivo | no es esta skill: impugnación colectiva con `guia_escrito` (`escrito="impugnación del despido colectivo"`, `jurisdiccion="laboral"`); la individual, con `redactar-demanda-despido` |
| Cálculo de indemnizaciones individuales | `calculo-indemnizacion-despido` |
| Hay transmisión de la unidad productiva o subrogación | `sucesion-empresa-contratas` antes de decidir |
| La empresa está declarada en concurso | el procedimiento corresponde al juez del concurso: esta skill no lo cubre; díselo al abogado |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ Empresa y grupo: denominación, CIF, actividad, sociedad dominante y su domicilio, obligación de consolidar cuentas, saldos deudores o acreedores con otras sociedades del grupo.
2. ★ Plantilla total en la fecha prevista de inicio (todas las modalidades contractuales), por centro de trabajo, provincia y comunidad autónoma, y plantilla habitual del último año por clasificación profesional.
3. ★ Extinciones por iniciativa de la empresa en los 90 días anteriores y previstas en los 90 siguientes, con su causa (despidos objetivos, mutuos acuerdos, bajas incentivadas, no superaciones del periodo de prueba…), y procedimientos anteriores de despido colectivo o de ERTE.
4. ★ Número y clasificación profesional de afectados por centro, periodo previsto para los despidos y criterios de selección.
5. ★ Causa y documentación: cuentas anuales de los dos últimos ejercicios completos (auditadas si hay obligación), cuentas provisionales firmadas, ingresos o ventas trimestrales, previsiones y su informe técnico, o memoria técnica del cambio organizativo, técnico o productivo.
6. ★ Representación en cada centro afectado: comité o delegados de personal, secciones sindicales y su peso en los órganos unitarios, centros sin representación.
7. ★ Afectados de 55 o más años (y si alguno era mutualista el 1 de enero de 1967) y de 50 o más; beneficios de la empresa o del grupo en los dos ejercicios anteriores y previsión de los cuatro siguientes.
8. ★ Si afecta a más del 50 % de la plantilla, bienes que se venderán fuera del tráfico normal.
9. Trabajadores con prioridad de permanencia (representantes, delegados sindicales, colectivos pactados en convenio) y personas en situaciones de protección del art. 53.4 ET.
10. Medidas sociales que la empresa puede ofrecer (recolocación interna, movilidad, formación, indemnización superior a la legal, bajas voluntarias).
11. Convenio colectivo aplicable (o actividad real y provincias).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**1. ¿Hay despido colectivo? (art. 51.1 ET; art. 1 del Real Decreto 1483/2012).** En 90 días, al menos 10 trabajadores en empresas de menos de 100; el 10 % en las de 100 a 300; 30 en las de más de 300; o el cierre total con más de cinco. La plantilla se cuenta el día de inicio, con todas las modalidades contractuales. Suman las demás extinciones por iniciativa empresarial y motivos no inherentes a la persona (salvo las del art. 49.1.c ET) si son al menos cinco. Haz la tabla de ventanas de 90 días hacia atrás y hacia delante; lee la doctrina sobre extinciones computables (mutuos acuerdos a iniciativa de la empresa) y sobre el encadenamiento de periodos, y la del TJUE sobre el concepto de despido colectivo y la unidad de referencia. Las extinciones objetivas en periodos sucesivos para eludir los umbrales sin causas nuevas son nulas (art. 51.1, último párrafo, ET).

**Si no se alcanza el umbral.** No hay despido colectivo: no redactes comunicación de intención ni de apertura de consultas. Entrega solo la **nota de umbrales** — `nota-umbrales-despido-colectivo-<empresa>-<AAAAMMDD>.docx` — con:
- la tabla de ventanas de 90 días hacia atrás y hacia delante de cada extinción prevista, con las extinciones computables, las excluidas y el motivo de cada exclusión;
- la conclusión y el margen que queda hasta el umbral en cada ventana, con la fecha en que se cierra;
- el riesgo de superar el umbral con una sola extinción más dentro de la ventana (bajas incentivadas y mutuos acuerdos propuestos por la empresa incluidos): las extinciones objetivas hechas sin el procedimiento colectivo serían nulas;
- si el cliente prevé nuevas extinciones por la misma causa en periodos sucesivos, la advertencia expresa de fraude por goteo (art. 51.1, último párrafo, ET y art. 122.2 LRJS: las nuevas extinciones son nulas) y qué exige que haya «causas nuevas»;
- las alternativas: tramitar ahora un despido colectivo por el total previsible, medidas temporales (`erte-suspension-reduccion`) o esperar a que existan y se documenten causas nuevas;
- la jurisprudencia leída sobre cómputo, extinciones computables y goteo (consultas de umbrales del apartado de estrategia).
Después, las cartas individuales se redactan con `carta-despido-objetivo`.

**2. Causas (art. 51.1 ET).** Económicas (pérdidas actuales o previstas, o disminución persistente de ingresos o ventas durante tres trimestres consecutivos frente a los mismos del año anterior), técnicas, organizativas o productivas. Prepara la tabla trimestral o de resultados y el argumento de razonabilidad y proporcionalidad entre causa y número de extinciones.

**3. Antes de abrir consultas: comisión representativa (art. 51.2 y art. 41.4 ET; arts. 26 y 27 del Real Decreto 1483/2012).**
- Comunica de forma fehaciente a los trabajadores o a sus representantes la intención de iniciar el procedimiento.
- Interlocutores: las secciones sindicales si lo acuerdan y tienen la mayoría en los órganos unitarios de los centros afectados; si no, las reglas del art. 41.4 según haya uno o varios centros y tengan o no representación (comisión de hasta tres miembros elegida por los trabajadores o designada por los sindicatos en los centros sin representación).
- Plazo máximo para constituirla: siete días desde la comunicación, o quince si algún centro afectado no tiene representantes. Transcurrido, la empresa puede abrir consultas aunque no se haya constituido. El art. 51.2 no dice si esos días son naturales o hábiles: si la comisión no está constituida, fija la apertura cuando el plazo haya vencido también contado en días hábiles, y dilo en el calendario.
- Comisión única de máximo trece miembros por parte; en el acta de constitución, que actúa como órgano colegiado (art. 27.2 del Real Decreto 1483/2012).

**4. Comunicación de apertura (art. 51.2 ET; arts. 2, 3 y 4 del Real Decreto 1483/2012).** Escrito a los representantes con copia a la autoridad laboral, con: causas; número y clasificación de afectados y de empleados habituales en el último año, desglosados por centro, provincia y comunidad; periodo de los despidos; criterios de designación; copia de la comunicación de intención; composición de la comisión o constancia de que no se constituyó. Acompaña la memoria explicativa, la documentación de la causa, el plan de recolocación si afecta a más de 50 y la solicitud del informe del comité del art. 64.5 ET. Documentación económica: cuentas de los dos últimos ejercicios completos, auditadas si procede, y provisionales firmadas; si hay previsión de pérdidas, criterios e informe técnico; si hay disminución de ingresos, documentación de los tres trimestres consecutivos **inmediatamente anteriores a la comunicación de apertura** y de los mismos del año anterior (comprueba que el último trimestre cerrado antes de la apertura está incluido; si el cliente da trimestres más antiguos, pide el que falta con un marcador); si hay grupo, las cuentas consolidadas o las de las demás sociedades en los términos del art. 4.5. La documentación debe estar en manos de los representantes desde el inicio (art. 7.1). Por causas técnicas, organizativas o productivas: memoria e informes técnicos que acrediten los cambios (art. 5). A la autoridad laboral se remite, simultáneamente, copia de la comunicación, la documentación, la copia de la solicitud del informe del comité y la composición de las representaciones y los centros sin representación (art. 6).

**5. Periodo de consultas (art. 51.2 ET; arts. 7, 8 y 10 del Real Decreto 1483/2012).** Duración no superior a 30 días naturales, o 15 en empresas de menos de 50 trabajadores. Calendario de reuniones al abrir; primera reunión no antes de tres días desde la entrega de la comunicación; salvo pacto, al menos dos reuniones separadas entre tres y seis días (menos de 50) o tres reuniones separadas entre cuatro y nueve días (50 o más). Acta firmada de cada reunión. Contenido mínimo: evitar o reducir despidos y atenuar consecuencias con medidas sociales (art. 8). Negociación de buena fe, con propuestas y respuestas documentadas. Acuerdo: mayoría de los representantes o de la comisión que represente a la mayoría de los trabajadores de los centros afectados (art. 28). La empresa responde por escrito, antes de terminar, a las advertencias de la autoridad laboral (art. 10.1).

**6. Decisión final (art. 51.2 ET; arts. 12 y 13 del Real Decreto 1483/2012).** En los quince días siguientes a la última reunión, comunica a la autoridad laboral el resultado (con copia íntegra del acuerdo, si lo hay) y a los representantes y a la autoridad laboral la decisión final, con las medidas sociales, el plan de recolocación y las actas firmadas; si no, el procedimiento caduca. Justifica la afectación de quienes tienen prioridad de permanencia. La Sala Cuarta ha calificado esa comunicación como presupuesto constitutivo del despido: léelo.

**7. Notificaciones individuales (art. 51.4 ET; art. 14 del Real Decreto 1483/2012).** Tras la decisión final, cada despido se notifica con los requisitos del art. 53.1 ET (carta con la causa, indemnización mínima de veinte días por año con máximo de doce mensualidades puesta a disposición, preaviso de quince días). Entre la comunicación de apertura a la autoridad laboral y la fecha de efectos deben mediar al menos treinta días. Las cartas se hacen con `carta-despido-objetivo`.

**8. Prioridades y criterios (art. 51.5 y art. 68.b ET; art. 10.3 LOLS; art. 13 del Real Decreto 1483/2012).** Los representantes tienen prioridad de permanencia; el convenio o el acuerdo pueden añadir colectivos. Los criterios de designación deben constar y no ser discriminatorios (lo verifica el informe de la Inspección, art. 11.5). La doctrina distingue criterios genéricos de criterios ausentes: léela antes de redactarlos. No respetar las prioridades hace nulas esas extinciones individuales (art. 124.13 LRJS).

**9. Obligaciones accesorias:**
- **Venta de bienes** si se extingue más del 50 % de la plantilla (art. 51.3 ET).
- **Convenio especial** para afectados de 55 o más años no mutualistas a 1 de enero de 1967, en empresas no concursadas (art. 51.9 ET y art. 20 de la Orden TAS/2865/2003): la empresa lo solicita durante el procedimiento y hasta la notificación individual; cuotas a su cargo hasta la edad que fija ese artículo, con pago único o fraccionado con aval. El artículo remite a la disposición adicional decimotercera de la LGSS, que el conector no devuelve: léela en el BOE consolidado y cítala con su enlace (ver «Huecos»). Si la causa es a la vez económica y de otro tipo, advierte de la duda sobre la edad aplicable.
- **Plan de recolocación externa** si afecta a más de 50 trabajadores, con empresa de recolocación autorizada, mínimo seis meses y el contenido del art. 9 del Real Decreto 1483/2012; no en concurso (art. 51.10 ET).
- **Aportación al Tesoro** si hay afectados de 50 o más años y concurren los requisitos del art. 2 del Real Decreto 1484/2012 (tamaño de empresa o grupo, sobrerrepresentación de mayores de 50 entre los despedidos, beneficios en los ejercicios que indica); conceptos del art. 3. Léelos, junto con la disposición adicional decimosexta de la Ley 27/2011 en el BOE consolidado (define el grupo por el art. 42.1 del Código de Comercio y solo cuenta los resultados obtenidos en España), y aplícalos a los datos del punto 7 en una tabla; no calcules el importe (lo liquida la Administración).

**10. Autoridad laboral competente (art. 25 del Real Decreto 1483/2012).** Se decide por dónde están los **trabajadores afectados** (sus centros), no por dónde tiene centros la empresa: la de la comunidad autónoma si todos los afectados están en ella; la estatal si hay afectados en centros de varias comunidades, salvo que el 85 % de la plantilla de la empresa radique en una comunidad con afectados en ella, cuya autoridad instruye todo el procedimiento y notifica el final al Ministerio (art. 25.3). El reglamento todavía nombra la «Dirección General de Empleo del Ministerio de Empleo y Seguridad Social»: hoy tramita estos procedimientos la Dirección General de Trabajo del Ministerio de Trabajo y Economía Social (compruébalo en su norma de estructura orgánica, en el BOE, y cita el enlace). Cada comunidad reparte su competencia entre órganos provinciales y centrales: nombra el órgano concreto comprobándolo en la sede oficial y cita el enlace.

**11. Impugnación y efectos que hay que prever (art. 51.6 ET; arts. 124 y 148.b LRJS).** Los representantes tienen 20 días de caducidad desde el acuerdo o la notificación de la decisión, sin conciliación previa, ante la Sala del TSJ o de la Audiencia Nacional según el ámbito (arts. 7 y 8 LRJS). Nulidad si no hubo periodo de consultas, no se entregó la documentación, se vulneraron derechos fundamentales o no se respetó el procedimiento de fuerza mayor; no ajustado a Derecho si no se acredita la causa. Si nadie impugna, la empresa puede pedir que se declare ajustado a Derecho (art. 124.3). La autoridad laboral puede impugnar el acuerdo por fraude, dolo, coacción o abuso de derecho. Los trabajadores, individualmente, por la vía de los arts. 120 a 123 LRJS con las reglas del art. 124.13. Agosto y Navidad son hábiles (art. 43.4 LRJS).

**12. Fuerza mayor (art. 51.7 ET; arts. 31 a 33 del Real Decreto 1483/2012).** Si la causa es fuerza mayor, no hay periodo de consultas: la autoridad laboral la constata en cinco días a solicitud de la empresa con comunicación simultánea a los representantes. Adapta el plan de trabajo a ese procedimiento.

## Estrategia y jurisprudencia

La nulidad se juega en el procedimiento: documentación completa desde el primer día, negociación real y documentada, comunicación de la decisión en plazo y criterios objetivos. La causa se juega en la razonabilidad y proporcionalidad. Construye el plan para que cada riesgo tenga un documento que lo neutralice.

**Consultas en Jurisprudenciator** (`base="TS"`, `jurisdiccion="SOCIAL"`; reformula como máximo dos veces; `anios=5` primero):

- Umbrales: `consulta="despido colectivo umbrales cómputo noventa días extinciones computables"` y `consulta="fraude de ley despidos objetivos periodos sucesivos noventa días umbrales despido colectivo"`.
- Buena fe y documentación: `consulta="despido colectivo buena fe periodo de consultas documentación nulidad"` y, si hay grupo, `consulta="despido colectivo grupo de empresas documentación cuentas consolidadas nulidad"`.
- Criterios: `consulta="criterios de selección trabajadores afectados despido colectivo concreción"`.
- Decisión final: `consulta="despido colectivo comunicación decisión final representantes presupuesto constitutivo"`.
- Comisión representativa: `consulta="despido colectivo comisión ad hoc constitución interlocutores legitimación"`.
- Causa: `consulta="despido colectivo causas económicas razonabilidad proporcionalidad"` (o productivas, organizativas).
- TJUE: `consulta="despido colectivo Directiva 98/59 concepto centro de trabajo umbrales"`, `base="TJUE"`.
- Protección reforzada: `consulta="despido colectivo trabajadora embarazada motivación"`, `base="TS"` y `base="TJUE"`.

Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que cites en la nota; transcribe fundamentos, nunca hechos ni datos de aquel pleito.

## Documentos que se entregan

Todo en Word según `references/formato-y-organos-laboral.md`. Si no se alcanza el umbral, solo la nota de umbrales descrita en el apartado 1 del régimen jurídico.

1. **Plan de trabajo** — `nota-plan-despido-colectivo-<empresa>-<AAAAMMDD>.docx`:
   - Tabla de umbrales en ventanas de 90 días y conclusión.
   - Calendario con fecha y precepto de cada hito: comunicación de intención → constitución de la comisión (7 o 15 días) → apertura y envío a la autoridad laboral → reuniones → fin de consultas (máx. 30 o 15 días) → decisión final (máx. 15 días desde la última reunión) → informe de la Inspección → notificaciones individuales → fecha de efectos (mín. 30 días desde la apertura comunicada a la autoridad laboral) → solicitud del convenio especial (hasta la notificación individual).
   - Lista de documentos (memoria, cuentas, informes técnicos, plan de recolocación, actas, decisión final) con responsable y fecha.
   - Guion de la memoria explicativa: causa, datos, conexión con el número y perfil de afectados, criterios, medidas sociales.
2. **Comunicación de intención** — `carta-intencion-despido-colectivo-<empresa>-<AAAAMMDD>.docx`, fehaciente, a los representantes o a los trabajadores de centros sin representación, con el plazo para constituir la comisión.
3. **Comunicación de apertura del periodo de consultas** — `carta-apertura-consultas-despido-colectivo-<empresa>-<AAAAMMDD>.docx`: destinatarios (comisión o representantes), copia a la autoridad laboral competente; extremos a) a g) del art. 51.2 ET con los desgloses del art. 3.1 del Real Decreto 1483/2012; relación de la documentación que se entrega; calendario de reuniones; solicitud del informe del art. 64.5 ET; firma. Datos no facilitados como marcadores (`[NÚMERO DE AFECTADOS POR CENTRO]`, `[CRITERIOS DE DESIGNACIÓN]`).
4. **Nota de riesgos**, solo si el abogado la pide (si no, lo que esta skill manda «a la nota» —calendario, riesgos, cálculos y jurisprudencia con su ECLI— va en el resumen de la entrega) — `nota-riesgos-despido-colectivo-<empresa>-<AAAAMMDD>.docx`: causas de nulidad y cómo se previenen; riesgo sobre la causa; prioridades y personas protegidas; convenio especial, recolocación y aportación al Tesoro (si proceden, con el artículo leído); impugnaciones posibles con plazos y órganos; jurisprudencia literal; huecos normativos que el abogado debe comprobar en la fuente oficial.

**Reparto para la redacción rápida:** cada documento es un Word, repartido por apartados. Plan de trabajo: umbrales y calendario / documentos, responsables y guion de la memoria. Carta de apertura: destinatarios, causas, afectados y criterios / documentación, calendario de reuniones, informe del art. 64.5 ET y firma. La comunicación de intención (1 página), sin equipo.

## Huecos que el conector no cubre

Lo que `buscar_articulo` no devuelve se busca en internet, en la fuente oficial, y se cita con su enlace y la fecha de consulta (punto 3 de la puerta); el resumen dice qué datos salen de internet.

- Disposición adicional decimotercera de la LGSS (convenio especial de mayores de 55 años): https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#dadecimotercera.
- Disposición adicional decimosexta de la Ley 27/2011 (aportación al Tesoro): https://www.boe.es/buscar/act.php?id=BOE-A-2011-13242#dadecimosexta. Úsala con la Orden TAS/2865/2003 y el Real Decreto 1484/2012, que sí devuelve el conector; no calcules importes.
- Órgano concreto de la autoridad laboral, forma de presentación y modelos: sede electrónica de la comunidad autónoma o del Ministerio de Trabajo y Economía Social. No des códigos ni formularios de memoria.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: ET 41, 51, 53, 64 y 68; LOLS 10; Real Decreto 1483/2012 (arts. 1-14 y 25-28, y 31-33 si hay fuerza mayor); Orden TAS/2865/2003 art. 20; Real Decreto 1484/2012 arts. 1-3; LRJS 7, 8, 43, 122, 124 y 148; LGSS 267.
- [ ] Disposiciones adicionales y órgano de la autoridad laboral leídos en la fuente oficial, con enlace y fecha de consulta.
- [ ] Tabla de umbrales con extinciones computables y doctrina leída.
- [ ] Calendario con cada plazo, su precepto y su fecha.
- [ ] Documentación exigida por la causa listada y en poder de los representantes desde el inicio.
- [ ] Convenio consultado para prioridades o procedimientos propios, con su vigencia.
- [ ] Criterios de selección objetivos y prioridades justificadas.
- [ ] Obligaciones accesorias (bienes, convenio especial, recolocación, aportación) comprobadas con los datos de edad y beneficios.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; las comunicaciones no llevan jurisprudencia.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero), con las normas nombradas como indica esta skill.
- [ ] Marcadores en vez de datos inventados; huecos normativos avisados.
- [ ] Resumen para el abogado según el apartado 9 del formato.
