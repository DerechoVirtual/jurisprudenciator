---
name: laboral-empresa-intake
description: >-
  Puerta de entrada de un asunto laboral, para la empresa o para el trabajador: quién es el cliente, qué
  ha pasado, fechas clave (efectos del despido, notificación de la sanción, de la modificación o del
  traslado), plazos de caducidad y prescripción que ya corren con su fecha final y su precepto,
  urgencias, plantilla, representación legal, convenio y datos registrales de la empresa. Entrega una
  ficha del asunto en Word con la skill que toca después. Úsala cuando digan «me ha entrado un asunto
  laboral», «me han despedido», «quiero despedir a un trabajador», «me han sancionado», «nos cambian el
  horario» o «¿estoy en plazo?». Si el documento que se quiere ya está claro y el plazo calculado, ve a
  la skill del catálogo; para estudiar el convenio a fondo, convenio-aplicable. Si el asunto es de
  Seguridad Social (alta médica, incapacidad, prestaciones) o de otro plugin, lo dice, anota los
  plazos que ya corren y deriva a la skill de ese plugin.
---

# Entrada de asuntos laborales (empresa y trabajador)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazos de caducidad y prescripción y su cómputo** → `buscar_articulo` (`ley="ET"`, artículos `"59"` y `"60"`), (`ley="LRJS"`, artículos `"43"`, `"65"`, `"103"`, `"114"`, `"125"`, `"138"`, `"139"`, `"179"` y `"279"`; `"124"` si hay despido colectivo) y (`ley="CC"`, `articulo="5"`) para los plazos por años. Lee siempre el 43 y el 65 LRJS y, de los demás, los de las acciones que el caso abre.
- **Asunto de Seguridad Social** (alta médica, incapacidad temporal o permanente, contingencia, desempleo, prestaciones) → `buscar_articulo` (`ley="LRJS"`, artículos `"64"`, `"71"` y `"140"`) y (`ley="LGSS"`, el artículo de la prestación: `"170"` en las altas médicas del INSS agotados los 365 días de incapacidad temporal, `"174"` extinción del subsidio, `"194"` grados de incapacidad permanente).
- **Requisito previo, órgano y competencia territorial** → `buscar_articulo` (`ley="LRJS"`, artículos `"63"`, `"64"`, `"69"` y `"10"`) y (`ley="LOPJ"`, `articulo="84"`).
- **Umbrales de plantilla, representación, garantías y nulidad** → `buscar_articulo` (`ley="ET"`, artículos `"51"`, `"41"`, `"40"`, `"62"`, `"63"`, `"68"`, `"55"`, `"53"` y `"56"`).
- **Convenio aplicable (primera identificación)** → `buscar_convenio` (`consulta` = actividad real de la empresa, `territorio` = provincia del centro de trabajo) + `vigencia_convenio` (`codigo`) + `leer_convenio` (`buscar_en="régimen disciplinario"` o `"preaviso"` si el asunto lo pide). Si hay más de un candidato o se discute, deriva a `convenio-aplicable`. Compara la fecha del boletín que encabeza el texto de `leer_convenio` con el último trámite «CONVENIO COLECTIVO (TEXTO NUEVO)» de `vigencia_convenio`: el conector puede devolver una publicación antigua o no poder descargarla. En ese caso lee el texto vigente en el boletín oficial (internet, punto 3 de la puerta) y cítalo con su enlace.
- **Empresa** → `buscar_empresa_mercantil` (denominación o CIF): denominación exacta, administradores, disolución o concurso (el buscador devuelve coincidencias aproximadas: comprueba por CIF y domicilio que la sociedad es la del asunto antes de usar sus datos); si hay insolvencia, `buscar_articulo` (`ley="LRJS"`, `articulo="23"`) y (`ley="ET"`, `articulo="33"`).
- **Doctrina que mueve una fecha o un riesgo** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión), con las consultas de «Estrategia y jurisprudencia».
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). Lo que Jurisprudenciator no tenga se cita de la fuente oficial de internet, con su enlace y la fecha de consulta, como dice el punto 3 de la puerta.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Al abrir cualquier asunto laboral, antes de redactar nada, y siempre que una fecha pueda estar corriendo. Sirve a las dos partes:

- **Empresa**: quiere despedir, sancionar, modificar condiciones, trasladar, dejar vencer un temporal o responder a una reclamación. La ficha le dice qué plazo propio tiene (prescripción de la falta, preavisos, opción tras la sentencia) y qué riesgo de nulidad o improcedencia corre.
- **Trabajador**: ha recibido una carta, una sanción, un cambio de condiciones, un finiquito, o no cobra. La ficha le dice qué acción tiene, hasta qué día y qué hay que presentar antes.

Primera pregunta, siempre: **¿a quién defiende el despacho, a la empresa o al trabajador?** No sigas sin la respuesta: el mismo hecho se analiza al revés según el cliente. Si la otra parte también es cliente del despacho, avísalo antes de continuar.

Después de la ficha, deriva:

| Situación | Skill siguiente |
|---|---|
| Despido ya comunicado; el trabajador quiere impugnarlo | `papeleta-conciliacion` y después `redactar-demanda-despido` |
| La empresa quiere despedir por incumplimiento | `carta-despido-disciplinario` |
| La empresa quiere despedir por causas objetivas | `carta-despido-objetivo`; si se alcanzan los umbrales del art. 51.1 ET, `despido-colectivo-empresa` |
| Hay que cuantificar indemnización o salarios de tramitación | `calculo-indemnizacion-despido` |
| Liquidación de haberes: hacer el finiquito o revisar uno recibido | `finiquito-liquidacion` |
| Salarios impagados, diferencias, horas extra, vacaciones | `reclamacion-cantidad` (prueba de jornada: `registro-jornada-horas-extra`) |
| Incumplimientos graves y el trabajador quiere irse indemnizado | `extincion-contrato-trabajador` |
| Imponer o impugnar una sanción | `sanciones-disciplinarias` |
| Cambio de jornada, horario, turnos, salario o funciones | `modificacion-sustancial-condiciones`; traslados o funciones distintas: `movilidad-geografica-funcional` |
| Permisos, adaptación o reducción de jornada | `permisos-conciliacion-adaptacion` |
| Acoso, discriminación o represalia sin despido | `tutela-derechos-fundamentales`; investigación interna: `protocolo-acoso-laboral` |
| ERTE o suspensión | `erte-suspension-reduccion` |
| Cambio de titular, contrata o subrogación | `sucesion-empresa-contratas` |
| Duda sobre el convenio | `convenio-aplicable` |
| Autónomo que puede ser trabajador; directivo | `falso-autonomo-trade`; `alta-direccion` |
| Requerimiento o acta de la Inspección | `inspeccion-trabajo-alegaciones` |
| Contratar, prueba, pactos, teletrabajo | `contrato-trabajo-modalidad`, `periodo-prueba`, `pactos-contrato-trabajo`, `teletrabajo-acuerdo` |
| Obligaciones por tamaño de plantilla | `plan-igualdad-registro-retributivo`, `canal-denuncias-informantes` |

**Asuntos que no son de este plugin.** Antes de seguir, comprueba si la consulta es en realidad de otra materia: la forma de la pregunta («¿me pueden despedir?») engaña a menudo. Dilo al abogado en la primera línea de la ficha y deriva:

| Situación | Dónde se trabaja |
|---|---|
| Seguridad Social frente a la entidad gestora: alta médica del INSS o de la mutua, incapacidad temporal o permanente, determinación de contingencia, desempleo, otras prestaciones | Plugin `litigacion-laboral-espana`: `asunto-intake` (abre el asunto y sus plazos), `reclamacion-previa-seguridad-social` (cuando la exige el art. 71 LRJS), `incapacidad-permanente`, `seguridad-social-contingencia` |
| Ya hay sentencia: recurso de suplicación o de casación para la unificación de doctrina, o su ejecución | Plugin `litigacion-laboral-espana`: `recurso-suplicacion`, `recurso-casacion-unificacion-doctrina`, `ejecucion-laboral` |
| Conflicto colectivo o impugnación del despido colectivo por los representantes | Plugin `litigacion-laboral-espana`: `conflicto-colectivo`, `impugnacion-despido-colectivo` |
| Relación mercantil sin indicios de laboralidad (agencia, distribución, franquicia, servicios entre empresas) | Plugin `contratos-civiles-mercantiles`: `contratos-intake`; si hay indicios de laboralidad, se queda aquí (`falso-autonomo-trade`) |
| Autorización de residencia y trabajo del trabajador extranjero | Plugin `extranjeria-espana`: `extranjeria-intake` |

En esos casos la ficha no se omite: recoge los plazos que ya corren, con su precepto leído (en un alta médica del INSS agotados los 365 días, la disconformidad del art. 170 LGSS, en días naturales, y la demanda de los arts. 71 y 140 LRJS), y la parte laboral del asunto (suspensión del contrato, obligación de reincorporarse, riesgo de despido por faltas de asistencia, efectos de una incapacidad permanente en el contrato según el art. 49 ET). Si no hay skill para un escrito urgente (por ejemplo, la disconformidad ante la inspección médica), la ficha dice qué contiene, ante quién se presenta y hasta cuándo. Si el despacho no tiene instalado el otro plugin, dilo. Las secciones de la ficha que no afecten al asunto (plantilla, convenio) se reducen a una línea.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No entregues la ficha al primer disparo: si falta un dato imprescindible (★), pídelo; si falta una fecha, no des plazo.

1. ★ Cliente (empresa o trabajador) y qué quiere conseguir.
2. ★ Qué ha pasado, en una frase: despido (disciplinario, objetivo, colectivo, fin de temporal, verbal o tácito), sanción, modificación, traslado, impago, petición de conciliación, requerimiento.
3. ★ Fechas, con el documento que prueba cada una:
   - entrega o recepción de la comunicación y fecha de efectos que figura en ella;
   - último día trabajado y fecha de baja en la Seguridad Social (el trabajador la ve en su vida laboral);
   - en sanciones y despidos disciplinarios: fecha de los hechos y fecha en que la empresa los conoció;
   - si ya se presentó papeleta: fecha de presentación y fecha del acto de conciliación, o si no se celebró.
4. ★ Relación: fecha de inicio y contratos anteriores (fechas y huecos entre ellos), subrogaciones, tipo de contrato, jornada, categoría, salario bruto real (nóminas de los últimos doce meses) y **localidad del centro de trabajo**.
5. ★ Empresa: denominación o CIF, actividad real, plantilla total y del centro, extinciones por causas no inherentes a la persona en los últimos noventa días, si forma grupo con otras.
6. ★ Representación: delegados, comité o secciones sindicales; si el trabajador es o ha sido representante en el último año, o está afiliado y la empresa lo sabe.
7. ★ Situaciones protegidas: embarazo, nacimiento o cuidado del menor, permisos o adaptaciones de jornada solicitados o en disfrute, excedencia, baja médica, víctima de violencia de género o sexual, reclamaciones o denuncias previas del trabajador.
8. Convenio que figura en las nóminas o en el contrato.
9. Si la empresa ha tramitado la baja en la Seguridad Social del trabajador despedido.
10. Si la empleadora es una Administración o una entidad de Derecho público.
11. **Festivos de la sede del órgano** (nacionales, autonómicos y locales del año): Jurisprudenciator no los devuelve. Búscalos en internet en las fuentes oficiales (resolución anual de fiestas laborales publicada en el BOE, boletín oficial de la comunidad autónoma para las autonómicas y locales) y cítalos con su enlace y la fecha de consulta; si no aparecen, pídelos al abogado y, hasta entonces, marca el plazo como provisional.
12. Documentos: carta o comunicación, contratos, nóminas, vida laboral, finiquito, correos o mensajes relevantes.

## Régimen jurídico y comprobaciones

Lee con `buscar_articulo`, en esta conversación, cada precepto que uses y anota su línea «vigente desde… redacción dada por…».

### Cómo se computa cada plazo

1. **Día inicial**: el que marque el precepto de la acción. Despido: los veinte días hábiles siguientes a aquel en que se produjo (art. 103.1 LRJS). Modificación sustancial y movilidad geográfica: desde el día siguiente a la notificación de la decisión, tras el periodo de consultas si lo hubo (art. 59.4 ET y art. 138.1 LRJS). Si la carta se entregó después de la fecha de efectos, si no hay carta (baja en la Seguridad Social, cierre, orden verbal) o si el trabajador estaba de baja médica, calcula con la fecha más temprana defendible y busca la doctrina (consultas abajo) antes de apurar la tardía.
2. **Días hábiles**: excluye sábados, domingos y festivos de la sede del órgano (art. 103.1 LRJS). Agosto y del 24 de diciembre al 6 de enero son hábiles solo en las modalidades del apartado 4 del art. 43 LRJS; léelo en cada caso: la impugnación de sanciones, por ejemplo, no figura en esa lista.
3. **Papeleta**: su presentación suspende la caducidad e interrumpe la prescripción; el cómputo se reanuda al día siguiente del intento de conciliación o transcurridos quince días hábiles desde la presentación sin celebrarse, y a los treinta días hábiles sin acto el trámite se tiene por cumplido (art. 65.1 y 65.2 LRJS). Suma los días ya consumidos antes de la papeleta: el plazo no vuelve a empezar. Para dar la fecha límite de la demanda, cuenta como consumido el día de presentación de la papeleta (criterio prudente) y dilo en la ficha.
4. **Plazos por años** (prescripción): de fecha a fecha y sin excluir inhábiles (art. 5 del Código Civil).
5. **Empresario equivocado**: si la papeleta o la demanda se dirigió a quien no era el empleador, el cómputo no empieza hasta que conste quién lo es (art. 103.2 LRJS).
6. **Administración empleadora**: agotamiento de la vía administrativa cuando proceda y demanda de despido en veinte días hábiles desde el acto o su notificación (art. 69 LRJS); una notificación sin pie de recursos mantiene suspendidos los plazos de caducidad (art. 69.1 LRJS).
7. En la ficha, cada plazo con: fecha inicial, precepto, días excluidos (con los festivos concretos), fecha final y **fecha recomendada de presentación** (día hábil anterior al vencimiento).

### Plazos que corren (acción del trabajador)

| Acción | Plazo | ¿Agosto y Navidad? | ¿Conciliación previa? | Preceptos |
|---|---|---|---|---|
| Despido (disciplinario, objetivo, fin de temporal que se impugna) | 20 días hábiles, caducidad | cuentan | sí | art. 59.3 ET; arts. 103, 63 y 65 LRJS |
| Sanción | 20 días hábiles (los del art. 103 LRJS), caducidad, desde su notificación | no cuentan | sí | art. 114.1 LRJS |
| Modificación sustancial o movilidad geográfica | 20 días hábiles, caducidad | cuentan | no | art. 59.4 ET; arts. 138.1 y 64.1 LRJS |
| Derechos de conciliación (adaptación, reducción, permisos) | 20 días desde la negativa o disconformidad | cuentan | no | arts. 139.1.a) y 64.1 LRJS |
| Fecha de vacaciones | 20 días desde que conoce la fecha, o dos meses antes de la fecha pretendida | cuentan | no | art. 125 LRJS |
| Tutela de derechos fundamentales | el de la acción frente a la conducta lesiva | cuentan | no | arts. 179.2 y 64.1 LRJS |
| Despido colectivo (representantes) | 20 días de caducidad desde el acuerdo o la notificación de la decisión | cuentan | no | art. 124.6 LRJS; la acción individual, con las reglas de ese artículo |
| Cantidad (salarios, diferencias, liquidación) | un año, prescripción, desde que la acción pudo ejercitarse | — | sí (interrumpe) | art. 59.1 y 59.2 ET; art. 65.1 LRJS |
| Ejecución de la readmisión no efectuada o irregular | 20 días, y tres meses desde la firmeza | — | — | art. 279 LRJS |
| Seguridad Social (prestaciones y altas médicas) | reclamación previa y demanda en los plazos del art. 71 LRJS; en el alta del INSS agotados los 365 días, disconformidad en cuatro días naturales (art. 170 LGSS) y demanda sin reclamación previa | cuentan en la impugnación de altas médicas | no (art. 64.1 LRJS) | arts. 71 y 140 LRJS; art. 170 LGSS. Deriva («Asuntos que no son de este plugin») |

La extinción a instancia del trabajador (art. 50 ET) no está en el art. 59.3 ET: no le asignes plazo en la ficha; deriva a `extincion-contrato-trabajador`, que estudia su régimen.

**Urgencias que cambian la tramitación**: si la empresa no ha tramitado la baja en la Seguridad Social del despedido, el procedimiento es urgente y preferente (art. 103.4 LRJS); lo mismo en la extinción por impago del art. 50.1.b) ET (art. 103.5 LRJS). Márcalo en la primera línea de la ficha.

### Plazos de la empresa

- **Prescripción de las faltas del trabajador**: leves, graves y muy graves, en los días que fija el art. 60.2 ET desde que la empresa tuvo conocimiento y, en todo caso, a los seis meses de haberse cometido. El precepto no los califica de hábiles y en el cómputo civil no se excluyen los inhábiles (art. 5.2 del Código Civil). Si los hechos son antiguos o continuados, busca la doctrina sobre el conocimiento de la empresa antes de afirmar que la falta está viva.
- **Nuevo despido que subsana la forma**: en veinte días desde el siguiente al primero, con los salarios intermedios y el alta (art. 55.2 ET). Tras una sentencia de improcedencia por forma con opción por la readmisión: siete días (art. 110.4 LRJS).
- **Opción tras la sentencia de improcedencia**: cinco días desde su notificación (art. 56.1 ET y art. 110.3 LRJS); sin opción, se entiende la readmisión (art. 56.3 ET); si el despedido es representante, opta él (art. 56.4 ET).
- **Preavisos**: despido objetivo (art. 53.1.c) ET), temporal de duración superior a un año (art. 49.1.c) ET), modificación sustancial individual (art. 41.3 ET) y traslado (art. 40.1 ET). Léelos y pon en la ficha la fecha mínima de efectos.
- **Modificación o traslado colectivos** (umbrales de los arts. 41.2 y 40.2 ET): periodo de consultas de hasta quince días con los representantes y efectos a los siete días de notificar la decisión (art. 41.4 y 41.5 ET; para el traslado, art. 40.2 ET). Pon en la ficha un calendario orientativo con la primera fecha en que la medida puede surtir efectos y avisa de que aplicarla antes, eludiendo las consultas, la hace nula (art. 138.7 LRJS). Si la condición que se quiere cambiar está fijada en el convenio estatutario (léelo), el cauce es la inaplicación del art. 82.3 ET, no el art. 41 (art. 41.6 ET).
- **Si no corre ningún plazo** (la empresa aún no ha actuado), la primera línea de la ficha lo dice y da la primera fecha en que la medida puede ser eficaz.

### Plantilla, representación y protección

Comprueba cada umbral con `buscar_articulo` antes de anotarlo. Los delegados y el comité se cuentan por centro de trabajo (salvo el comité conjunto del art. 63.2 ET): con varios centros, calcula cada uno.

| Plantilla | Consecuencia | Precepto |
|---|---|---|
| Entre seis y diez trabajadores | puede haber un delegado si lo decide la mayoría | art. 62.1 ET |
| Más de diez y menos de cincuenta | delegados de personal | art. 62.1 ET |
| Cincuenta o más en el centro | comité de empresa | art. 63.1 ET |
| Extinciones en noventa días que alcanzan los umbrales del art. 51.1 ET (y los del 41.2 y 40.2 para modificaciones y traslados) | despido colectivo, o modificación y traslado colectivos con periodo de consultas | arts. 51.1, 41.2 y 40.2 ET |
| Menos de veinticinco | límite del periodo de prueba en defecto de convenio | art. 14.1 ET |
| Cincuenta o más | plan de igualdad y sistema interno de información | art. 45.2 de la Ley Orgánica 3/2007 (`ley="BOE-A-2007-6115"`); art. 10 de la Ley 2/2023, de 20 de febrero (`ley="BOE-A-2023-4513"`) |

Para el umbral del despido colectivo, aplica las reglas de cómputo del propio art. 51.1 ET (extinciones por motivos no inherentes a la persona, excluidas las del art. 49.1.c) ET, si son al menos cinco; fraude por periodos sucesivos) y déjalas escritas en la ficha.

**Protección**: lee el apartado 5 del art. 55 ET y el apartado 4 del art. 53 ET y marca en la ficha cada situación que concurra (embarazo, suspensiones y permisos que enumeran, adaptación de jornada, excedencia, violencia de género o sexual, reincorporación tras el nacimiento). **Garantías**: representante legal o delegado sindical, expediente contradictorio (arts. 55.1 y 68.a) ET) y opción suya tras la improcedencia (art. 56.4 ET); afiliado cuya afiliación conste a la empresa, audiencia a los delegados sindicales (art. 55.1 ET). Lee además el régimen disciplinario del convenio (`leer_convenio`, `buscar_en="régimen disciplinario"`): puede exigir requisitos formales propios (art. 55.1 ET).

### Órgano y trámite previo

- Demanda: Tribunal de Instancia de [sede], Sección de lo Social (art. 84 LOPJ, leído); competencia territorial del art. 10.1 LRJS: lugar de prestación de servicios o domicilio del demandado, a elección del demandante.
- Conciliación previa obligatoria (art. 63 LRJS) salvo las excepciones del art. 64 LRJS; ante el servicio autonómico que indica el apartado 3 de `references/formato-y-organos-laboral.md`.
- Empresa en concurso o insolvente: FOGASA como interesado (art. 23 LRJS) y garantía del art. 33 ET.

## Estrategia y jurisprudencia

**Si defiendes a la empresa**, antes de actuar comprueba, por este orden: que la falta no ha prescrito; que no concurre ninguna situación de nulidad; las garantías de representación y afiliación; los requisitos del convenio; en el despido disciplinario, la audiencia previa exigida por la Sala Cuarta; y si las extinciones de los últimos noventa días empujan hacia el despido colectivo. Cada comprobación fallida es un riesgo con nombre en la ficha.

**Si defiendes al trabajador**, lo primero es la fecha: si al plazo le quedan cinco días hábiles o menos, la ficha lo dice en la primera línea y el siguiente paso es presentar la papeleta (`papeleta-conciliacion`) antes de profundizar. Después, identifica bien al empleador (grupo, contrata, cesión) con `buscar_empresa_mercantil`: demandar a quien no es acorta el margen.

Consultas (reformula como máximo dos veces si no hay nada útil):

- Reanudación del plazo tras la papeleta: `consulta="caducidad acción despido cómputo días hábiles papeleta conciliación reanudación"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Día inicial dudoso (baja en la Seguridad Social, despido tácito, baja médica): `consulta="despido tácito caducidad inicio cómputo baja en Seguridad Social conocimiento"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Faltas antiguas o continuadas: `consulta="prescripción faltas artículo 60.2 conocimiento cabal pleno y exacto empresa"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Despido disciplinario, siempre: `consulta="audiencia previa despido disciplinario artículo 7 Convenio 158 OIT"`, `base="TS"`, `jurisdiccion="SOCIAL"`; lee la del Pleno y la más reciente que la aplique, y comprueba desde qué fecha se exige.
- Antigüedad discutida por contratos anteriores: `consulta="unidad esencial del vínculo antigüedad contratos temporales interrupciones"`, `base="TS"`, `jurisdiccion="SOCIAL"`.

Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar, y comprueba que el párrafo es razonamiento de la Sala. En la ficha, la doctrina va en «Riesgos», con párrafo literal y ECLI; sin doctrina leída, la ficha dice «criterio no contrastado» y no concluye.

## Documento que se entrega

Nota en Word según `references/formato-y-organos-laboral.md`: `nota-ficha-asunto-<empresa>-<AAAAMMDD>.docx`.

1. **Primera línea: el vencimiento más próximo** («Despido: vence el [fecha] — art. 103.1 LRJS — presentar papeleta antes del [fecha]») y, si la hay, la tramitación urgente del art. 103.4 LRJS.
2. **Cliente y encargo**: a quién se defiende y qué quiere.
3. **Cronología** (tabla): fecha · hecho · documento que lo prueba · dato pendiente.
4. **Relación laboral** (tabla): inicio y contratos anteriores, categoría, jornada, salario bruto real y de dónde sale, centro de trabajo; marcadores (`[FECHA DE ANTIGÜEDAD]`, `[SALARIO BRUTO ANUAL]`…) para lo no facilitado.
5. **Empresa**: denominación exacta, CIF, administradores y estado registral según `buscar_empresa_mercantil`, con la advertencia de que es informativo; grupo o contrata si consta.
6. **Plantilla, representación y protección**: umbrales que se alcanzan, con su artículo; garantías y situaciones protegidas que concurren.
7. **Convenio**: denominación oficial, código de 14 dígitos, boletín, vigencia inscrita (`vigencia_convenio`) y si es provisional (entonces, `convenio-aplicable`).
8. **Plazos** (tabla): acción · día inicial · precepto · días excluidos · fecha final · fecha recomendada · trámite previo. Plazos de la empresa en tabla aparte.
9. **Riesgos**: nulidad, improcedencia, prescripción, garantías; doctrina literal si se ha leído.
10. **Documentos que faltan** y quién debe aportarlos.
11. **Skill siguiente** y por qué.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Cliente identificado (empresa o trabajador) antes de analizar.
- [ ] Comprobado si el asunto es de este plugin; si es de Seguridad Social o de otro plugin, dicho en la primera línea y derivado a la skill concreta, con los plazos que corren y la parte laboral en la ficha.
- [ ] Texto del convenio contrastado con `vigencia_convenio`: si `leer_convenio` devolvió una publicación anterior al último texto nuevo, o no pudo descargarla, leído el vigente en el boletín oficial y citado con enlace.
- [ ] Leídos en esta conversación con `buscar_articulo` los preceptos de cada plazo, el art. 43 LRJS y el art. 65 LRJS; anotada su vigencia.
- [ ] Cada plazo con fecha inicial, precepto, días excluidos, fecha final y fecha recomendada; sin fecha inicial, no hay plazo y se pide el dato.
- [ ] Festivos tomados de la fuente oficial (enlace y fecha de consulta) o confirmados por el abogado; si no, plazo marcado como provisional.
- [ ] Todo dato que no salga de Jurisprudenciator (festivos, nombre del servicio de conciliación) citado con su enlace y señalado en el resumen.
- [ ] Umbrales de plantilla, garantías y situaciones de nulidad comprobados con su artículo.
- [ ] Convenio identificado con código y vigencia, o derivado a `convenio-aplicable`.
- [ ] Empresa comprobada con `buscar_empresa_mercantil`; FOGASA valorado si hay insolvencia.
- [ ] Cada ECLI citado leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre la ficha; los avisos de «posible disonancia» contrastados con el apartado leído.
- [ ] Marcadores en lugar de datos no facilitados.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y para quién, vencimiento más próximo con su precepto, datos y documentos que faltan, riesgos, jurisprudencia citada y skill siguiente.
