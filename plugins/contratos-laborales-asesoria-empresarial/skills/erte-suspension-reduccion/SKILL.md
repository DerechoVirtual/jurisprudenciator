---
name: erte-suspension-reduccion
description: >-
  Prepara para la empresa un expediente de regulación temporal de empleo (ERTE) de suspensión de contratos o
  reducción de jornada: por causas económicas, técnicas, organizativas o de producción (art. 47 ET), por fuerza
  mayor temporal, incluido el impedimento o la limitación de la actividad por decisiones de la autoridad, o dentro
  del Mecanismo RED (art. 47 bis ET). Entrega la comunicación de inicio (o la solicitud de fuerza mayor), la
  documentación y una nota con calendario, obligaciones durante el ERTE (horas extra, externalizaciones,
  contrataciones, formación, mantenimiento del empleo), desempleo e impugnación. Úsala con «ERTE», «suspender
  contratos», «reducir jornada por falta de trabajo», «fuerza mayor», «Mecanismo RED». Si la medida es definitiva,
  despido-colectivo-empresa o carta-despido-objetivo; para cambiar condiciones, modificacion-sustancial-condiciones.
---

# ERTE: suspensión de contratos y reducción de jornada

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen legal del ERTE y del Mecanismo RED** → `buscar_articulo` (`ley="ET"`, artículos `"47"`, `"47 bis"`, `"45"`, `"41"` —apartado 4, interlocutores— y `"64"` —apartado 5, informe del comité—); si la fuerza mayor deriva de la imposibilidad de acceder al centro, también `"37"` (letra g del apartado 3).
- **Procedimiento reglamentario** → `buscar_articulo` (`ley="BOE-A-2012-13419"`, artículos `"16"` a `"24"` para causas económicas, técnicas, organizativas o de producción; `"25"` a `"28"` para autoridad competente, interlocución, comisión y acuerdos; `"31"` a `"33"` para fuerza mayor; y `"4"` y `"5"`, a los que remite el art. 18 para la documentación económica y los informes técnicos).
- **¿Está activado el Mecanismo RED para el sector y en qué fechas?** → `buscar_boe` (`consulta="Mecanismo RED activación"`) y `novedades_boe` (`contiene="Mecanismo RED"`, `desde` = un año antes de hoy); lee la orden que publique el acuerdo con `leer_boe`.
- **Desempleo y cotización de los afectados** → `buscar_articulo` (`ley="LGSS"`, artículos `"262"`, `"267"`, `"269"`, `"273"` y `"153 bis"`).
- **Impugnación** → `buscar_articulo` (`ley="LRJS"`, artículos `"138"`, `"153"`, `"148"`, `"64"` y `"43"`).
- **Doctrina** (buena fe y documentación, comunicación de la decisión final, carácter coyuntural, fuerza mayor, prohibiciones) → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`; los TSJ con `base="AN"`, `tipo_organo="TSJ"`) con las consultas del apartado de estrategia + `leer_sentencias` (`parrafos=3`).
- **Convenio aplicable y sus artículos** (complementos durante el ERTE, procedimientos propios, calendario) → `buscar_convenio` + `leer_convenio` (`buscar_en="regulación temporal"` o `buscar_en="suspensión"`; después `articulo="N"`) + `vigencia_convenio`. Si `vigencia_convenio` registra un texto posterior al que devuelve `leer_convenio`, localiza su publicación con `novedades_boe` y léela con `leer_boe`; si llega truncada, en el boletín oficial, con su enlace.
- **Disposiciones adicionales que el conector no devuelve** (beneficios en la cotización y compromiso de empleo, protección en el Mecanismo RED, acciones formativas) y **órgano concreto de la autoridad laboral** → internet, en la fuente oficial: ver «Huecos».
- **Empresa** → `buscar_empresa_mercantil` (denominación, CIF y grupo, si la causa económica exige documentación de otras sociedades).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). En los documentos, «artículo N del Real Decreto 1483/2012, de 29 de octubre» y «apartado 1 del artículo 47 bis del Estatuto de los Trabajadores».

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Para la **empresa** que necesita suspender contratos o reducir jornadas de forma temporal, sea cual sea el número de afectados (el procedimiento se aplica a cualquier plantilla, art. 47.3 ET). Primero decide la vía:

| Situación | Vía |
|---|---|
| Caída de actividad, pérdidas, cambios técnicos u organizativos de carácter temporal | ERTE por causas económicas, técnicas, organizativas o de producción (art. 47.1 a 47.4 ET) |
| Hecho externo, imprevisible o inevitable que impide trabajar temporalmente | fuerza mayor temporal (art. 47.5 ET) |
| Cierre o limitación de actividad ordenados por la autoridad (incluidas razones de salud pública) | fuerza mayor por impedimento o limitación (art. 47.6 ET) |
| Imposibilidad de acceder al centro más allá de los cuatro días del permiso del art. 37.3.g ET, sin trabajo a distancia posible | fuerza mayor del art. 47.6, párrafo segundo |
| El Consejo de Ministros ha activado el Mecanismo RED para el sector o con carácter cíclico | Mecanismo RED (art. 47 bis ET) |

| Situación | Skill que procede |
|---|---|
| La causa es estructural y la medida definitiva | `despido-colectivo-empresa` o `carta-despido-objetivo` |
| Se quiere cambiar horario, turnos o salario de forma estable | `modificacion-sustancial-condiciones` |
| Se defiende a un trabajador afectado o a los representantes | no es esta skill: nota de vicios con los apartados de abajo; la demanda individual por la modalidad del art. 138 LRJS y la colectiva con `guia_escrito` (`escrito="conflicto colectivo"`, `jurisdiccion="laboral"`) |
| No se sabe qué convenio se aplica | primero `convenio-aplicable` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ Vía (tabla anterior) y hecho causante con fechas.
2. ★ Plantilla total (menos de 50 o 50 o más: cambia la duración de las consultas), centros afectados, provincias y comunidades autónomas.
3. ★ Representación en cada centro afectado (comité, delegados, secciones sindicales y su peso) y centros sin representación.
4. ★ Causa y prueba de su **carácter temporal**:
   - económica: último ejercicio completo, cuentas provisionales del vigente e ingresos o ventas de los dos últimos trimestres frente a los mismos del año anterior;
   - técnica, organizativa o productiva: memoria del cambio y datos (pedidos, cartera, producción, suministros);
   - fuerza mayor: hecho, fecha, pruebas y, si viene de una decisión de la autoridad, la resolución o norma y las limitaciones concretas que produce.
5. ★ Afectados: número y clasificación profesional, y plantilla habitual del último año por clasificación; para cada persona, suspensión (número máximo de días) o reducción (porcentaje y base de cómputo), y el periodo de aplicación.
6. ★ Criterios de designación de los afectados.
7. ★ Si la empresa prevé durante el ERTE horas extraordinarias, nuevas contratas o subcontratas, o nuevas contrataciones; y si alguna de esas funciones no puede cubrirla el personal afectado y por qué.
8. ★ Si se van a aplicar beneficios en la cotización (condicionan el mantenimiento del empleo) y si hay acciones formativas previstas.
9. Complementos de la prestación u otras mejoras previstas en el convenio o que la empresa ofrece; ERTE anteriores o prórroga.
10. Afectados de 50 o más años a los que después se pudiera despedir (aportación al Tesoro: ver apartado 8).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**1. Causas y temporalidad (art. 47.1 y 47.2 ET).** Las definiciones son las del despido colectivo con una diferencia: la disminución de ingresos o ventas es persistente si dura **dos** trimestres consecutivos frente a los mismos del año anterior. La documentación debe acreditar la causa y que la situación es coyuntural (art. 18.1 del Real Decreto 1483/2012); el alcance y la duración de las medidas se adecúan a la situación que se quiere superar (art. 16.4). Si la causa parece estructural, dilo: el ERTE sería impugnable y la vía es otra.

**2. Medidas (art. 47.7.a ET; art. 16 del Real Decreto 1483/2012).** Suspensión por días completos, continuados o alternos, de al menos una jornada; o reducción de entre el 10 y el 70 % de la jornada, computada sobre base diaria, semanal, mensual o anual. Se prioriza la reducción cuando sea viable. Cada persona, o reducción o suspensión, no ambas a la vez. No genera indemnización.

**3. Procedimiento por causas económicas, técnicas, organizativas o de producción (art. 47.3 ET; arts. 17 a 23 y 26 a 28 del Real Decreto 1483/2012).**
- Comunicación fehaciente de la intención de iniciar el procedimiento. Comisión representativa constituida antes de la apertura: plazo máximo de **cinco** días, o **diez** si algún centro afectado no tiene representantes (art. 47.3 ET, que en esto se aparta de los plazos del art. 41.4). Interlocutores y reglas de composición, las del art. 41.4 ET; comisión única de hasta trece miembros por parte, constituida como órgano colegiado (art. 27).
- Autoridad laboral: se decide por dónde están los **trabajadores afectados** (art. 25 del reglamento): la de la comunidad autónoma si todos están en ella; la estatal si hay afectados en varias comunidades, salvo la regla del 85 % de la plantilla. El reglamento aún nombra la «Dirección General de Empleo»: hoy tramita estos procedimientos la Dirección General de Trabajo del Ministerio de Trabajo y Economía Social. Cada comunidad reparte su competencia entre órganos provinciales y centrales: compruébalo en su sede oficial y cita el enlace.
- Inicio: comunicación a la autoridad laboral y apertura **simultánea** del periodo de consultas. La comunicación de apertura contiene los extremos del art. 17.2 (causas; número y clasificación de afectados y de empleados habituales, desglosados por centro, provincia y comunidad; concreción y detalle de las medidas; criterios de designación; copia de la comunicación de intención; composición de la comisión) con la memoria explicativa. Documentación del art. 18. Solicitud del informe del art. 64.5 ET (art. 17.3). A la autoridad laboral, además, la composición de las representaciones y los centros sin representación (art. 19).
- Consultas de duración no superior a **quince** días, o **siete** en empresas de menos de 50 (art. 47.3 ET). El art. 20 del reglamento fija, salvo pacto, primera reunión no antes de un día desde la entrega de la comunicación y al menos dos reuniones separadas entre tres y siete días; con el tope de siete días de las empresas pequeñas, pacta el calendario en la primera reunión y déjalo en acta. Acta firmada de cada reunión. Negociación de buena fe; la empresa responde por escrito a las advertencias de la autoridad laboral (art. 21).
- Acuerdo: mayoría de los representantes o de la comisión que represente a la mayoría de los trabajadores de los centros afectados. Con acuerdo se presumen las causas y solo cabe impugnarlo por fraude, dolo, coacción o abuso de derecho (art. 47.3 ET).
- Decisión final: en los **quince días** siguientes a la última reunión, la empresa comunica a los representantes y a la autoridad laboral su decisión, con el periodo de aplicación y, conforme al art. 20.6 del reglamento, el calendario con los días concretos de suspensión o el porcentaje, periodos y horario de reducción de cada afectado, y las actas; si no, el procedimiento caduca. La Sala Cuarta ha anulado ERTE cuya decisión final no llegó a los representantes con ese contenido: lee esa doctrina. La decisión surte efectos desde su comunicación a la autoridad laboral, salvo que fije una fecha posterior; después, notificación individual con los días u horario de cada persona (art. 23).
- Informe preceptivo de la Inspección en quince días desde la notificación del fin de las consultas (art. 47.3 ET; art. 22).
- Prórroga: nueva consulta de hasta cinco días con la misma representación y comunicación a la autoridad laboral en siete días (art. 47.4 ET).

**4. Fuerza mayor temporal (art. 47.5 y 47.6 ET; arts. 31 a 33 del Real Decreto 1483/2012).** Solicitud a la autoridad laboral con los medios de prueba y comunicación simultánea a la representación. Informe preceptivo de la Inspección, salvo en el impedimento o limitación por decisión de la autoridad (47.6.a). Resolución en cinco días desde la entrada en el registro; sin resolución expresa se entiende autorizado. La resolución constata la fuerza mayor y fija hasta qué fecha surte efectos, desde el hecho causante; la decisión y su aplicación son de la empresa, que la traslada a la representación y a la autoridad. Si persiste, nueva solicitud. Si aparecen hechos distintos de los aportados, audiencia de un día (art. 33.3). En el impedimento o limitación, la empresa debe justificar las limitaciones concretas a su actividad (47.6.b). Si no se constata la fuerza mayor, cabe iniciar un ERTE por las otras causas (art. 33.6).

**5. Mecanismo RED (art. 47 bis ET).** Solo si está activado (compruébalo en el BOE con la consulta de la lista y comprueba sector y fechas). Solicitud voluntaria a la autoridad laboral con comunicación a la representación, consultas como en el art. 47.3, informe de la Inspección en siete días y resolución en siete días naturales desde la comunicación del fin de consultas (silencio positivo). En la modalidad sectorial, plan de recualificación. Se aplican las normas comunes del art. 47.4 y 47.7. La protección de los afectados está en la disposición adicional cuadragésima primera de la LGSS, que el conector no devuelve: léela en el BOE consolidado y cítala con su enlace (ver «Huecos»).

**6. Obligaciones durante el ERTE (art. 47.7 ET).** Afectar y desafectar según varíen las circunstancias, informando antes a la representación y comunicándolo a la entidad gestora y a la Tesorería por los procedimientos automatizados (no des códigos: remite a la fuente oficial). **Prohibidas** las horas extraordinarias, las nuevas externalizaciones de actividad y las nuevas contrataciones laborales, salvo que las personas afectadas del centro no puedan desempeñar esas funciones por formación, capacitación u otras razones objetivas y justificadas, informando antes a la representación. Las acciones formativas dan derecho a crédito adicional de formación programada (art. 47.7.d). Los beneficios en la cotización son voluntarios y quedan condicionados al mantenimiento en el empleo (art. 47.7.e). Los regula la disposición adicional cuadragésima cuarta de la LGSS (porcentajes según el tipo de ERTE, acciones formativas obligatorias en los ERTE por causas económicas, técnicas, organizativas o de producción y en el Mecanismo RED, declaraciones responsables, compromiso de mantenimiento del empleo y reintegro), y las acciones formativas, la disposición adicional vigesimoquinta del ET. El conector no devuelve ninguna de las dos: léelas en el BOE consolidado y cita con su enlace cada porcentaje, plazo y requisito que escribas.

**7. Desempleo y cotización (art. 47.7.f ET; arts. 262, 267, 269, 273 y 153 bis LGSS).** Los afectados están en situación legal de desempleo total o parcial; se acredita con la comunicación escrita y el certificado de empresa, con fecha de efectos igual o posterior a la comunicación de la decisión a la autoridad laboral (art. 267.3.a). En la reducción, el consumo de prestación es por horas (art. 269.5). La empresa sigue cotizando su aportación con las bases del art. 153 bis. Esta skill no calcula prestaciones.

**8. Relación con un despido posterior.** Si después se despide a afectados de 50 o más años, los periodos del ERTE pueden computar en la aportación al Tesoro (art. 2.3 del Real Decreto 1484/2012; léelo con `ley="BOE-A-2012-13420"`). Si la empresa aplica beneficios en la cotización, cualquier despido de afectados choca con el compromiso de mantenimiento del empleo del art. 47.7.e ET: explica el riesgo con la disposición adicional cuadragésima cuarta de la LGSS leída en el BOE consolidado (duración del compromiso, extinciones que no lo incumplen, reintegro con recargo e intereses), citada con su enlace.

**9. Impugnación (art. 47.3 ET; arts. 138, 153 y 148.b LRJS).** Trabajador afectado: modalidad del art. 138 LRJS, veinte días hábiles desde la notificación de la decisión, sin conciliación previa (art. 64 LRJS), proceso urgente; la sentencia declara la medida justificada o injustificada (reanudación, salarios o diferencias con la prestación, reintegro a la entidad gestora y diferencias de cotización) y nula si se eludió el periodo de consultas o hay móvil lesivo. Representantes: conflicto colectivo si la medida afecta a un número igual o superior a los umbrales del art. 51.1 ET, que paraliza las acciones individuales. Autoridad laboral: de oficio, por fraude o si la entidad gestora advierte obtención indebida de prestaciones. Agosto y Navidad son hábiles (art. 43.4 LRJS).

## Estrategia y jurisprudencia

Lo que tumba un ERTE: documentación que no acredita la causa ni su temporalidad, falta de negociación real, decisión final no comunicada a los representantes con el calendario individual, criterios de selección ausentes, y prohibiciones incumplidas durante la aplicación. Diseña cada documento para cerrar uno de esos riesgos.

**Consultas en Jurisprudenciator** (`base="TS"`, `jurisdiccion="SOCIAL"`; reformula como máximo dos veces):

- `consulta="suspensión de contratos causas productivas periodo de consultas buena fe nulidad ERTE"` y `consulta="ERTE documentación periodo de consultas información suficiente"`.
- `consulta="ERTE comunicación decisión final representantes calendario días concretos nulidad"`.
- `consulta="ERTE causas coyunturales frente a estructurales justificación medida temporal"`.
- `consulta="ERTE fuerza mayor temporal impedimento limitación actividad autoridad"`.
- `consulta="ERTE prohibición horas extraordinarias externalizaciones nuevas contrataciones"`, `base="AN"`, `tipo_organo="TSJ"`.
- `consulta="ERTE criterios de selección afectados discriminación"`.

Buena parte de la doctrina se dictó sobre los ERTE de la pandemia, con normas de emergencia hoy no vigentes: comprueba en cada sentencia qué régimen aplicó y cítala solo para lo que el art. 47 vigente (redacción del RDL 32/2021 y posteriores, que devuelve `buscar_articulo`) mantiene. Lee con `leer_sentencias` (`parrafos=3`) solo lo que cites; transcribe fundamentos, nunca hechos ni datos de aquel pleito. La jurisprudencia va en la nota, no en las comunicaciones.

## Documentos que se entregan

Todo en Word según `references/formato-y-organos-laboral.md`.

1. **Comunicación de intención de iniciar el procedimiento** — `carta-intencion-erte-<empresa>-<AAAAMMDD>.docx`, fehaciente, con el plazo de constitución de la comisión (cinco o diez días).
2. **Comunicación de inicio y apertura del periodo de consultas** — `carta-inicio-erte-<empresa>-<AAAAMMDD>.docx`: a la comisión o representantes, con copia simultánea a la autoridad laboral competente (art. 25 del reglamento; nombre del órgano comprobado en la sede oficial); extremos del art. 17.2; medidas por colectivo o puesto; periodo; criterios; calendario propuesto de reuniones; relación de documentación; solicitud del informe del art. 64.5 ET. En fuerza mayor, en su lugar, **solicitud a la autoridad laboral** — `solicitud-erte-fuerza-mayor-<empresa>-<AAAAMMDD>.docx`: hecho causante, prueba, limitaciones concretas si viene de una decisión de la autoridad, medidas y periodo, con la comunicación simultánea a la representación.
3. **Documentación** — `memoria-erte-<empresa>-<AAAAMMDD>.docx`: índice numerado y guion de la **memoria explicativa** (causa, datos, carácter temporal, proporcionalidad de cada medida, criterios), con la tabla de ingresos o ventas por trimestre si la causa es económica y la lista de documentos del art. 18 (o de las pruebas de la fuerza mayor).
4. **Nota para el abogado** — `nota-erte-<empresa>-<AAAAMMDD>.docx`: vía elegida y por qué; calendario con fecha y precepto de cada hito (intención, comisión, apertura, reuniones, fin de consultas, decisión final en quince días, informe de la Inspección, efectos, notificaciones individuales, prórroga); obligaciones durante la aplicación (prohibiciones y su excepción, afectación y desafectación, formación, compromiso de empleo si hay beneficios); desempleo y cotización por remisión a la LGSS; riesgos e impugnaciones con plazos; jurisprudencia literal; huecos normativos.
5. Si el abogado lo pide: **decisión final** y **notificación individual** con el calendario de días o el porcentaje, periodos y horario de cada persona (art. 20.6 y art. 23 del reglamento).

## Huecos que el conector no cubre

Lo que `buscar_articulo` no devuelve se busca en internet, en la fuente oficial, y se cita con su enlace y la fecha de consulta (punto 3 de la puerta); el resumen dice qué datos salen de internet.

- Disposición adicional cuadragésima cuarta de la LGSS (beneficios en la cotización, formación y compromiso de mantenimiento del empleo): https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-22.
- Disposición adicional cuadragésima primera de la LGSS (protección en el Mecanismo RED): https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-19.
- Disposición adicional vigesimoquinta del ET (acciones formativas en los ERTE): https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#da-4.
- Órgano concreto de la autoridad laboral, procedimientos automatizados ante la entidad gestora y la Tesorería, modelos: sede electrónica oficial. No des códigos ni formularios de memoria.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: ET 41, 45, 47, 64 (y 47 bis y 37 si proceden); Real Decreto 1483/2012 arts. 4, 5, 16-28 (y 31-33 si hay fuerza mayor); LGSS 153 bis, 262, 267, 269 y 273; LRJS 43, 64, 138, 148 y 153.
- [ ] Disposiciones adicionales y órgano de la autoridad laboral leídos en la fuente oficial, con enlace y fecha de consulta.
- [ ] Vía justificada; si es el Mecanismo RED, activación comprobada en el BOE con sector y fechas.
- [ ] Causa y carácter temporal documentados; medidas proporcionadas y definidas por persona.
- [ ] Plazos de comisión (cinco o diez días) y de consultas (quince o siete días) según la plantilla; calendario de reuniones pactado o conforme al art. 20.
- [ ] Decisión final prevista en quince días con el calendario individual, y notificaciones individuales.
- [ ] Prohibiciones durante el ERTE explicadas al cliente con su excepción; compromiso de empleo advertido sin cifras no leídas.
- [ ] Convenio consultado (complementos y procedimientos propios) con su vigencia.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`, con el régimen que aplicó; las comunicaciones no llevan jurisprudencia.
- [ ] `verificar_escrito` pasado sobre cada documento.
- [ ] Marcadores en vez de datos inventados; huecos normativos avisados.
- [ ] Resumen para el abogado según el apartado 9 del formato.
