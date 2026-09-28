---
name: permisos-conciliacion-adaptacion
description: >-
  Permisos retribuidos del art. 37 ET en su redacción vigente (tras el RDL 5/2023 y las reformas
  posteriores), lactancia, reducción de jornada por guarda legal o cuidado de familiares (art. 37.6),
  concreción horaria (art. 37.7), permiso parental (art. 48 bis), semanas de cuidado del menor hasta
  los ocho años (art. 48.4) y adaptación de jornada (art. 34.8: negociación de quince días y respuesta
  motivada), con el procedimiento urgente del art. 139 LRJS. Sirve a la empresa (respuesta motivada,
  propuesta alternativa o aplazamiento que aguanten) y al trabajador (solicitud bien hecha y demanda
  con daños y perjuicios). Úsala con «permiso por hospitalización», «reducción de jornada», «cambio
  de turno por los niños», «teletrabajo para cuidar», «me deniegan la adaptación», «permiso
  parental». Para teletrabajo general usa teletrabajo-acuerdo; para despidos, redactar-demanda-despido.
---

# Permisos, conciliación y adaptación de jornada

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Permisos, lactancia, reducción de jornada, concreción horaria, víctimas y fuerza mayor** → `buscar_articulo` (`ley="ET"`, `articulo="37"`): lee la línea «vigente desde… redacción vigente dada por…» y las notas «Téngase en cuenta» en cada consulta, porque el artículo se ha reformado varias veces desde 2023.
- **Adaptación de jornada** → `buscar_articulo` (`ley="ET"`, `articulo="34"`, apartado 8); **permiso parental y cuidado del menor** → (`ley="ET"`, artículos `"48 bis"` y `"48"`, apartado 4) y **excedencia por cuidado** → (`ley="ET"`, `articulo="46"`).
- **Si la adaptación incluye trabajo a distancia** → `buscar_articulo` (`ley="BOE-A-2021-11472"`, artículos `"5"`, `"7"` y `"8"`: voluntariedad «sin perjuicio del derecho al trabajo a distancia que pueda reconocer la legislación», contenido mínimo del acuerdo individual y prioridades) y `leer_convenio` (`buscar_en="trabajo a distancia"`) para el umbral de trabajo a distancia regular y el acuerdo que exige el convenio.
- **Permiso por imposibilidad de acceder al centro de trabajo (primera letra g del art. 37.3)** → además del art. 37, `buscar_articulo` (`ley="ET"`, `articulo="47"`, apartado 6: durante los cuatro días no hay fuerza mayor; después, posible ERTE) y, si se habla de alertas y protocolos, (`ley="ET"`, artículos `"64"` —letra e del apartado 4— y `"85"`).
- **Protección frente a represalias y discriminación** → `buscar_articulo` (`ley="ET"`, artículos `"4"`, `"17"`, `"53"` y `"55"`) y (`ley="BOE-A-2000-15060"`, artículos `"7"` —apartado 5—, `"8"` —apartado 12— y `"40"`).
- **Procedimiento** → `buscar_articulo` (`ley="LRJS"`, artículos `"43"`, `"64"`, `"96"`, `"139"`, `"177"`, `"180"`, `"184"` y `"191"`).
- **Convenio: permisos mejorados, días naturales o laborables, criterios de concreción horaria, términos de la adaptación y preavisos** → `buscar_convenio` + `leer_convenio` (`buscar_en="permisos"`, `"licencias"`, `"reducción de jornada"`, `"conciliación"`) + `vigencia_convenio`; y el plan de igualdad si la empresa lo tiene.
- **Doctrina sobre adaptación, concreción horaria, inicio de los permisos y discriminación** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; los TSJ con `base="AN"`, `tipo_organo="TSJ"` y `provincia` con la sede de la Sala; `base="TC"` para la dimensión constitucional) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Método para la demanda** → no hay guía propia del art. 139 LRJS en `guia_escrito` (una consulta por texto devuelve la de la papeleta de conciliación, que aquí no procede: el art. 64.1 LRJS exime de ella). Pide `guia_escrito` (`escrito="estilo-escritos-judiciales"`, `jurisdiccion="laboral"`) para el estilo y la estructura, y sigue el apartado «Documentos que se entregan» de esta skill; si se acumula la tutela, también `escrito="tutela-derechos-fundamentales"`. Las reglas comunes de las guías dicen que agosto es inhábil salvo en algunas modalidades sin nombrar la del art. 139: manda el art. 43.4 LRJS, que sí la incluye.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Pregunta primero **a quién defiende el abogado**. La empresa quiere responder en plazo, negociar de verdad y motivar con datos; el trabajador quiere una solicitud completa que active los plazos y, si se deniega, una demanda del art. 139 LRJS presentada a tiempo.

- Solicitud o denegación de un permiso retribuido, de su duración o de su día de inicio.
- Reducción de jornada por guarda legal o cuidado, y su concreción horaria o turno.
- Solicitud de adaptación (horario, turno fijo, jornada continua, trabajo a distancia) por conciliación.
- Permiso parental del art. 48 bis o semanas de cuidado del menor del art. 48.4, y su aplazamiento por la empresa.
- Revisión de una política interna de permisos o del capítulo de conciliación de un convenio.

| Situación | Skill que procede |
|---|---|
| Acuerdo general de teletrabajo, gastos y desconexión (no por conciliación) | `teletrabajo-acuerdo` |
| Despido o extinción tras pedir o disfrutar un permiso o adaptación | `redactar-demanda-despido` (nulidad de los arts. 53.4 y 55.5 ET) |
| Represalia o discriminación sin decisión sobre la medida de conciliación | `tutela-derechos-fundamentales` |
| La empresa cambia el horario de quien ya tiene reducción o adaptación | `modificacion-sustancial-condiciones` (y los riesgos de discriminación de esta skill) |
| Cantidades de permisos no retribuidos o descontados indebidamente | `reclamacion-cantidad` |
| Medidas del plan de igualdad | `plan-igualdad-registro-retributivo` |
| Determinar el convenio | `convenio-aplicable` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende y qué necesita (solicitud, respuesta, aplazamiento, demanda, política).
2. ★ Derecho que se ejerce y sujeto causante: parentesco o convivencia, edad del menor, hecho (hospitalización, intervención, enfermedad grave, fallecimiento, nacimiento), fecha en que ocurrió y si fue en día laborable.
3. ★ Jornada y horario actuales (cuadrante, turnos, fines de semana, jornada a tiempo parcial) y medida concreta pedida: horas de reducción, franja horaria, turno, días, trabajo a distancia, fechas de inicio y fin.
4. ★ Fechas: solicitud (y cómo se presentó), respuesta de la empresa o silencio, reuniones de negociación, comunicación de la negativa o de la propuesta alternativa. Sin la fecha de la comunicación empresarial no se da plazo para demandar.
5. ★ Razones organizativas o productivas de la empresa, con datos: cobertura del servicio, otras reducciones concedidas, plantilla del turno, coste.
6. ★ Convenio aplicable y plan de igualdad: permisos, criterios de concreción, términos de la adaptación.
7. ★ Si otra persona de la empresa ejerce el mismo derecho por el mismo sujeto causante.
8. Perjuicio sufrido por la negativa o la demora (económico, cuidado contratado, bajas) si se van a pedir daños.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo. Comprueba en la respuesta si hay reformas posteriores a las citadas aquí y aplica la redacción vigente en la fecha del hecho causante.

**Permisos retribuidos (art. 37.3 ET):** previo aviso y justificación. Lee las letras en el texto vigente: matrimonio o registro de pareja de hecho; accidente o enfermedad graves, hospitalización o intervención sin hospitalización con reposo domiciliario (círculo de parientes y convivientes de la letra b); fallecimiento (letra b bis), con ampliación por desplazamiento; traslado de domicilio; deber inexcusable; funciones de representación; exámenes prenatales y trámites de adopción; imposibilidad de acceder al centro por restricciones de la autoridad o riesgo grave, con la posibilidad de trabajo a distancia; actos preparatorios de la donación de órganos. **Trampa de cita**: el apartado 3 tiene dos letras g) (el texto consolidado lo marca «[sic]»); cítalas por su contenido («letra g) del apartado 3 del artículo 37 del Estatuto de los Trabajadores, relativa a…»).

- Fuerza mayor familiar (art. 37.9 ET): ausencia por motivos familiares urgentes; retribuidas las horas equivalentes a cuatro días al año, conforme al convenio o acuerdo.
- Inicio y cómputo del permiso de la letra b) (días naturales o laborables, si puede diferirse mientras dure la hospitalización): la Sala Cuarta ha desarrollado su doctrina en 2026; léela antes de responder y aplica primero lo que diga el convenio si mejora la ley.

**Lactancia, prematuros y reducción (art. 37.4 a 37.7 ET):**

- Lactancia hasta los nueve meses, divisible, sustituible por reducción o acumulable en jornadas completas; derecho individual; ampliable a doce meses con reducción salarial si ambos progenitores lo ejercen con igual duración y régimen.
- Reducción por guarda legal de menor de doce años o persona con discapacidad sin actividad retribuida, o por cuidado de familiar hasta el segundo grado (incluido el consanguíneo de la pareja de hecho): entre un octavo y la mitad, con reducción proporcional del salario. Reducción por cuidado de menor con cáncer o enfermedad grave: al menos la mitad, con los límites de edad del párrafo tercero y siguientes.
- Concreción horaria dentro de la **jornada ordinaria**, a elección de la persona trabajadora, con los criterios que fije el convenio; preaviso de quince días o el del convenio (art. 37.7 ET). Si dos personas de la empresa lo generan por el mismo sujeto causante, la empresa puede limitar el ejercicio simultáneo por razones fundadas, motivadas por escrito y con plan alternativo.
- Si lo pedido sale de la jornada ordinaria (otro turno, otros días), comprueba con la búsqueda sobre «concreción horaria turnos» cómo lo ha tratado la Sala Cuarta y, si no cabe en el art. 37.7, encáuzalo como adaptación del art. 34.8 (puede pedirse a la vez que la reducción).

**Adaptación de jornada (art. 34.8 ET):**

- Derecho a **solicitar** adaptaciones razonables y proporcionadas de duración, distribución, ordenación del tiempo o forma de prestación, incluido el trabajo a distancia, para hijos hasta doce años y, justificando la necesidad, para hijos mayores, cónyuge o pareja, familiares por consanguinidad hasta el segundo grado y dependientes que convivan.
- Sin regulación en el convenio (lee si el convenio fija un procedimiento propio o se limita a remitir al Estatuto): la empresa abre un proceso de negociación de hasta quince días; si no hay oposición motivada expresa en ese plazo, se presume concedida. Al final, por escrito: aceptación, propuesta alternativa o negativa con las razones objetivas. Cuenta los quince días como naturales desde la recepción de la solicitud (el precepto no los califica de hábiles y no es un plazo procesal): la empresa debe responder dentro de ellos, también en agosto.
- La presunción de concesión por silencio no está asentada en todos los tribunales: comprueba el criterio del TSJ del territorio (`consulta="adaptación de jornada presunción de concesión quince días falta de oposición motivada expresa"`, `base="AN"`, `tipo_organo="TSJ"`, `anios=3`). Hay Salas que exigen que la necesidad esté justificada para que opere y que la han negado cuando la primera comunicación de la empresa, aunque tardía, ya contenía la oposición. En la demanda del trabajador, plantéala junto a la falta de negociación y la razonabilidad, nunca como único argumento.
- La Sala Cuarta ha calificado la apertura de la negociación como trámite imperativo: si la empresa no negocia y se limita a rechazar, procede acoger judicialmente la medida en los términos pedidos, salvo que sea manifiestamente irrazonable o desproporcionada. Léelo antes de redactar y úsalo según la posición.
- Derecho de regreso a la situación anterior al terminar el periodo o cuando decaigan las causas.

**Permiso parental y cuidado del menor:**

- Permiso parental (art. 48 bis ET): hasta ocho semanas, continuas o discontinuas, a tiempo completo o parcial, hasta que el menor cumpla ocho años; individual e intransferible; la persona trabajadora fija las fechas con diez días de preaviso o el del convenio. La empresa solo puede **aplazarlo** por un periodo razonable si dos o más personas lo generan por el mismo sujeto causante o en los supuestos del convenio que alteren seriamente su funcionamiento, justificándolo por escrito y tras ofrecer una alternativa igual de flexible. Comprueba en la redacción vigente si tiene retribución (la que devuelve el conector no la establece) y, si se invoca una prestación pública para este permiso, búscala en internet en el BOE o en la sede de la Seguridad Social y cítala con su enlace; nunca de memoria.
- Suspensión por nacimiento (art. 48.4 ET): lee duración y distribución vigentes, en particular las semanas de la letra c) que pueden disfrutarse hasta que el menor cumpla ocho años, con quince días de preaviso y posible limitación del disfrute simultáneo si ambos progenitores trabajan en la empresa.
- Excedencia por cuidado (art. 46.3 ET) como alternativa cuando la reducción o la adaptación no bastan.

**Protección:**

- Despido nulo, salvo procedencia, de quien haya solicitado o disfrute los permisos de la letra b) del apartado 3 y de los apartados 4, 5 y 6 del artículo 37, las adaptaciones del art. 34.8, la excedencia del art. 46.3 o el permiso parental (letras a) y b) del apartado 5 del artículo 55 y del apartado 4 del artículo 53 del ET, en su redacción vigente).
- Discriminación por razón de sexo, incluido el trato desfavorable por ejercer derechos de conciliación (letra c) del apartado 2 del artículo 4 y artículo 17 del ET); inversión de la carga de la prueba con indicios (art. 96 LRJS).
- Infracción grave por transgredir las normas de permisos (apartado 5 del artículo 7 del Real Decreto Legislativo 5/2000) y muy grave por decisiones discriminatorias (apartado 12 del artículo 8); cuantías en su art. 40, leídas en el momento.

**Procedimiento del art. 139 LRJS:**

- Demanda en **veinte días** desde que la empresa comunica la negativa o su disconformidad con la propuesta (art. 139.1.a LRJS); cuéntalos como hábiles (apartado 6 del formato). Agosto es hábil (art. 43.4 LRJS). Sin conciliación previa (art. 64.1 LRJS).
- Se puede acumular la indemnización de daños y perjuicios derivados de la negativa o la demora; la empresa se exonera si cumplió al menos provisionalmente la medida propuesta.
- Cada parte lleva su propuesta y alternativas al acto de conciliación ante el Letrado o Letrada de la Administración de Justicia y al juicio, con el informe de los órganos del plan de igualdad si lo hay.
- Urgente: vista en cinco días desde la admisión; sentencia en tres; sin recurso salvo que los daños acumulados alcancen la cuantía de suplicación (arts. 139.1.b y 191.2.f LRJS).
- Aplica también a los derechos de las víctimas de violencia de género, a la reducción de jornada y a la reordenación del tiempo (art. 139.2 LRJS), con las medidas cautelares del art. 180.4 LRJS.
- Si se invoca discriminación, se acumula la tutela en esta modalidad (art. 184 LRJS) y el Ministerio Fiscal es parte (art. 177.3 LRJS).

## Estrategia y jurisprudencia

1. **Empresa**: contesta dentro de los quince días; documenta la negociación (convocatoria, reunión, propuestas escritas); si deniega o propone alternativa, motiva con datos verificables del puesto y del servicio (cuadrantes, coberturas, número de personas con medidas similares, imposibilidad técnica del teletrabajo) y ofrece alternativas reales; evita justificaciones genéricas («necesidades del servicio»); si hay concurrencia de solicitudes, aplica un criterio objetivo y escrito. Valora conceder provisionalmente para limitar los daños.
2. **Trabajador**: pide por escrito, con la medida exacta, las fechas, la necesidad y el preaviso, y guarda el acuse; si la empresa no negocia o calla, documéntalo; tras la negativa, calcula el plazo de veinte días el mismo día y prepara la prueba de la necesidad (horarios del otro progenitor, colegio, informes médicos) y de la viabilidad organizativa (compañeros con horarios similares).
3. Consultas en Jurisprudenciator (reformula como máximo dos veces si no hay resultados útiles):
   - Adaptación sin negociación: `buscar_sentencias` (`consulta="adaptación de jornada artículo 34.8 omisión proceso negociador consecuencias"`, `base="TS"`, `jurisdiccion="SOCIAL"`).
   - Adaptación en el territorio: `consulta="adaptación de jornada artículo 34.8 negociación propuesta alternativa denegación motivada"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia` de la sede, `anios=3`.
   - Concreción horaria y turnos: `consulta="reducción de jornada guarda legal concreción horaria turnos"`, `base="TS"`.
   - Inicio de los permisos: `consulta="permiso hospitalización familiar inicio día laborable"`, `base="TS"`, `jurisdiccion="SOCIAL"`, `fecha_desde="01/01/2025"` (la redacción con «37.3 b)» y `fecha_desde` de 2026 no devuelve nada); para requisitos que la empresa añade al permiso, `consulta="requisitos adicionales permiso cuidado de familiares artículo 37.3 b"`, `base="TS"`.
   - Permiso de la primera letra g) del art. 37.3 (imposibilidad de acceder al centro de trabajo): a 27-9-2026 no hay doctrina publicada. Haz dos consultas (TS y TSJ del territorio) y la búsqueda en internet del punto 3 de la puerta; si nada aparece, dilo en la nota y apóyate en el texto del art. 37.3, en el art. 47.6 ET y en la exposición de motivos del Real Decreto-ley 8/2024 (`buscar_boe` + `leer_boe`, BOE-A-2024-24840). No es causa de detener la tarea: la carta y la nota no exigen jurisprudencia (apartado 8 del formato).
   - Discriminación y dimensión constitucional: `consulta="conciliación de la vida familiar y laboral dimensión constitucional discriminación por razón de sexo"`, `base="TC"`, y `consulta="denegación adaptación de jornada discriminación indirecta causas organizativas"`, `base="TS"`.
   - Daños: `consulta="indemnización daños y perjuicios negativa adaptación de jornada"`, `base="AN"`, `tipo_organo="TSJ"`, `anios=3`.
4. Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar y transcribe fundamentos, nunca hechos ni datos de aquel pleito. Muchas sentencias de instancia y de TSJ resuelven casos concretos: contrasta que la ponderación que citas se parece a la del cliente. En la respuesta de la empresa y en la solicitud no va jurisprudencia: va en la nota o en la demanda.

## Documentos que se entregan

Todos en Word según `references/formato-y-organos-laboral.md`.

**Posición de la empresa:**

1. Convocatoria y acta de la negociación del art. 34.8 (`carta-negociacion-adaptacion-<apellido-trabajador>-<AAAAMMDD>.docx`).
2. Respuesta motivada (`carta-respuesta-conciliacion-<apellido-trabajador>-<AAAAMMDD>.docx`): solicitud recibida y fecha; negociación seguida; decisión (aceptación, propuesta alternativa concreta o negativa); razones objetivas con datos; duración y revisión; derecho de regreso; firma y recibí. Para el aplazamiento del permiso parental o la limitación del ejercicio simultáneo: justificación escrita y alternativa o plan alternativo.
3. Nota para el abogado (`nota-conciliacion-<empresa>-<AAAAMMDD>.docx`): encuadre (permiso, reducción, concreción, adaptación, parental), plazos cumplidos, riesgos (presunción de concesión, nulidad de un despido posterior, discriminación, daños), artículos del ET y del convenio leídos y doctrina literal si existe.

**Posición del trabajador:**

1. Solicitud (`carta-solicitud-conciliacion-<apellido-trabajador>-<AAAAMMDD>.docx`): derecho y precepto; sujeto causante y necesidad; medida exacta, fecha de inicio y de fin; preaviso cumplido; petición de apertura de la negociación si es del art. 34.8; documentos que se adjuntan.
2. Demanda del art. 139 LRJS (`demanda-conciliacion-<apellido-trabajador>-<AAAAMMDD>.docx`) al Tribunal de Instancia, Sección de lo Social: hechos (relación, jornada, necesidad, solicitud, negociación o su ausencia, respuesta y fecha); fundamentos (plazo; derecho y requisitos; razonabilidad y proporcionalidad; falta de negociación o de motivación; discriminación si procede, con citación del Ministerio Fiscal); súplica (reconocimiento del derecho en los términos pedidos o en la alternativa que se indique y daños y perjuicios cuantificados); otrosíes (prueba y, si procede, medidas cautelares).
3. Nota de estrategia (`nota-conciliacion-<apellido-trabajador>-<AAAAMMDD>.docx`) con plazos (fecha inicial, precepto, fecha final, con los festivos del lugar del órgano comprobados en internet), cálculo de los daños con su base y la decisión sobre la cuantía: por debajo de 3.000 € la sentencia no admite suplicación (arts. 139.1.b y 191.2.f y g LRJS); no infles la indemnización para abrir el recurso.
4. Si lo que se reclama es el **salario de un permiso descontado** (no la medida de conciliación), la carta a la empresa es la solicitud del punto 1 (con el precepto citado por su contenido) y la nota de estrategia deriva la papeleta y la demanda a `reclamacion-cantidad`; si la empresa sanciona la ausencia, a `sanciones-disciplinarias`.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado, ni en Jurisprudenciator ni en internet.
- [ ] Todo dato que no sale de Jurisprudenciator (orden de cotización, tabla salarial, criterio técnico, nombre de un órgano, sede electrónica) lleva su enlace oficial y la fecha de consulta, y el resumen lo identifica.
- [ ] Leídos con `buscar_articulo` en esta conversación: ET 4, 17, 34, 37, 46, 48, 48 bis, 53 y 55 (los usados), con la fecha de vigencia de cada uno y las notas de reforma; LRJS 43, 64, 96, 139, 177, 180, 184 y 191; Real Decreto Legislativo 5/2000 arts. 7, 8 y 40 si se mencionan infracciones; Ley 10/2021 arts. 5, 7 y 8 y el artículo de trabajo a distancia del convenio si la adaptación lo incluye; ET 47.6 si el permiso es el de la primera letra g) del art. 37.3.
- [ ] Encuadrada la petición (permiso, lactancia, reducción, concreción, adaptación, parental, cuidado del menor) y aplicada la redacción vigente en la fecha del hecho causante.
- [ ] Convenio y plan de igualdad leídos con `leer_convenio` y vigencia comprobada cuando mejoran o concretan la ley.
- [ ] Plazo con fecha de la comunicación empresarial, precepto y fecha final; en la empresa, los quince días de negociación contados.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`; ninguna jurisprudencia en solicitudes ni respuestas.
- [ ] `verificar_escrito` pasado sobre cada documento; las dos letras g) del art. 37.3 citadas por su contenido; los avisos de «posible disonancia» contrastados con el apartado exacto leído.
- [ ] Marcadores en lugar de datos no facilitados; ningún dato de salud del familiar más allá del necesario.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y ante qué órgano; plazo; daños y de dónde salen; riesgos y documentos que faltan; tabla de jurisprudencia; próximo paso.
