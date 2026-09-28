---
name: registro-jornada-horas-extra
description: >-
  Registro diario de jornada (art. 34.9 ET), horas extraordinarias (art. 35 ET: límite, voluntariedad,
  pago o descanso y registro), descansos diario, semanal y entre jornadas, trabajo a tiempo parcial y
  jornadas especiales, y prueba del tiempo trabajado cuando no hay registro (doctrina del TJUE y de la
  Sala Cuarta). Sirve a la empresa (auditoría del sistema, política de registro e infracciones de la
  LISOS) y al trabajador (reconstrucción y cálculo de las horas y estrategia para reclamarlas). Úsala
  con «registro horario», «fichaje», «horas extra que no me pagan», «me hacen quedarme», «control
  horario», «inspección por jornada». La demanda de cantidad se redacta con reclamacion-cantidad; los
  cambios de horario, con modificacion-sustancial-condiciones.
---

# Registro de jornada, horas extraordinarias y descansos

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Jornada, descansos, registro, horas extraordinarias, nocturnidad y vacaciones** → `buscar_articulo` (`ley="ET"`, artículos `"34"`, `"35"`, `"36"`, `"37"` —apartado 1— y `"38"`); **tiempo parcial y horas complementarias** → (`ley="ET"`, `articulo="12"`, apartados 4 y 5).
- **Jornadas especiales, trabajo a distancia y hogar familiar** → `buscar_articulo` (`ley="BOE-A-1995-21346"`, Real Decreto 1561/1995, el artículo del sector: empieza por `"1"` y `"2"` y sigue con el que regule la actividad), (`ley="BOE-A-2021-11472"`, `articulo="14"`) y (`ley="BOE-A-2011-17975"`, `articulo="9"`).
- **Consulta e informe de la representación sobre el sistema de control** → `buscar_articulo` (`ley="ET"`, artículos `"64"` —letra f) del apartado 5 y apartado 6— y `"62"` —competencias de los delegados de personal—). **Información mensual de horas extraordinarias a los representantes**: disposición adicional tercera del Real Decreto 1561/1995, que `buscar_articulo` no devuelve: léela en internet en el texto consolidado del BOE (API de datos abiertos, bloque `datercera` de `BOE-A-1995-21346`) y cítala con su enlace.
- **Infracciones y sanciones** → `buscar_articulo` (`ley="BOE-A-2000-15060"`, artículos `"7"` —apartados 5 y 7—, `"39"` y `"40"`); **Directiva de tiempo de trabajo** → (`ley="Directiva 2003/88/CE"`, artículos `"2"` —definición de tiempo de trabajo—, `"3"`, `"5"` y `"6"`).
- **Prueba, prescripción y proceso** → `buscar_articulo` (`ley="LEC"`, `articulo="217"`), (`ley="LRJS"`, artículo `"94"`) y (`ley="ET"`, `articulo="59"`).
- **Sistemas de control y datos personales** → `buscar_articulo` (`ley="LOPDGDD"`, artículos `"87"`, `"88"`, `"89"` y `"90"`) y (`ley="RGPD"`, `articulo="9"` si el sistema usa datos biométricos).
- **Convenio: jornada anual, distribución irregular, precio o compensación de las horas extraordinarias, pausas y regulación del registro** → `buscar_convenio` + `leer_convenio` (`buscar_en="jornada"`, `"horas extraordinarias"`, `"registro de jornada"`, `"descanso"`) + `vigencia_convenio`.
- **Doctrina sobre registro, carga de la prueba, tiempo de trabajo y compensación** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; los TSJ con `base="AN"`, `tipo_organo="TSJ"` y `provincia` con la sede de la Sala; `base="TJUE"` para la Directiva 2003/88) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
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

Pregunta primero **a quién defiende el abogado**. La empresa necesita un registro que pruebe la jornada real y cumpla la ley, y saber qué riesgo tiene ante la Inspección o una reclamación; el trabajador necesita reconstruir las horas, calcularlas y saber qué parte de la prueba le corresponde.

- Auditoría del sistema de registro o de la política de horas extraordinarias; preparación ante una visita o requerimiento de la Inspección.
- Redacción o revisión de la política interna de registro, incluidas pausas, teletrabajo y trabajo fuera del centro.
- Reclamación de horas extraordinarias o de excesos de jornada, con o sin registro.
- Dudas sobre descansos, tiempo de trabajo efectivo (guardias, desplazamientos, tiempos de presencia) o jornadas especiales.

| Situación | Skill que procede |
|---|---|
| Redactar la demanda de cantidad por horas extraordinarias | `reclamacion-cantidad` (con el cálculo y la prueba de esta skill) |
| Acta o requerimiento de la Inspección ya recibido | `inspeccion-trabajo-alegaciones` |
| La empresa cambia jornada u horario | `modificacion-sustancial-condiciones` |
| Adaptación o reducción de jornada por conciliación | `permisos-conciliacion-adaptacion` |
| Acuerdo de trabajo a distancia y desconexión digital | `teletrabajo-acuerdo` |
| Contrato a tiempo parcial que se convierte en completo por falta de registro, o elección de modalidad | `contrato-trabajo-modalidad` |
| Sanción por no fichar o por incumplir el horario | `sanciones-disciplinarias` |
| Determinar el convenio | `convenio-aplicable` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende y qué necesita (auditoría, política, cálculo, estrategia).
2. ★ Convenio aplicable y jornada que fija (anual, semanal, distribución irregular, pausas computables); sector (para jornadas especiales).
3. ★ Plantilla, centros, modalidades de trabajo (presencial, a distancia, itinerante, a turnos, tiempo parcial) y representación legal.
4. ★ Empresa: sistema de registro actual (cómo se ficha, quién puede modificar un registro y si queda traza, qué se entrega al trabajador, desde cuándo, cómo se implantó y si se consultó a la representación), cuatro años de registros, nóminas con el resumen de horas, calendario laboral y política de horas extraordinarias (pago o descanso).
5. ★ Trabajador: periodo reclamado; horario pactado o prefijado (contrato, cuadrante, calendario) o patrón irregular (llamamientos, turnos cambiantes); pruebas de las horas reales (fichajes, correos o mensajes fuera de horario, accesos, conexiones, tacógrafo, geolocalización, albaranes, testigos); horas cobradas o compensadas; nóminas del periodo.
6. ★ Salario bruto anual y conceptos (para el valor de la hora) y precio o compensación de la hora extraordinaria en el convenio o el contrato.
7. Fecha de la última hora reclamada y de cualquier reclamación previa (prescripción).
8. Si hay actuación de la Inspección: fecha de la visita o del requerimiento, documentos pedidos y plazo concedido (entonces, además, `inspeccion-trabajo-alegaciones`).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y comprueba su «vigente desde» y «redacción vigente dada por»: aplica solo la redacción que devuelva el conector para cada periodo del caso.

**Registro diario (art. 34.9 ET):** la empresa garantiza el registro diario con la hora concreta de inicio y de finalización de la jornada de cada persona, sin perjuicio de la flexibilidad horaria. Se organiza por convenio o acuerdo de empresa o, en su defecto, por decisión del empresario **previa consulta** con la representación legal. Se conserva **cuatro años** y está a disposición de las personas trabajadoras, de sus representantes y de la Inspección.

- Implantar o revisar el sistema exige, además, el **informe previo** de la representación sobre «la implantación y revisión de sistemas de organización y control del trabajo» (letra f) del apartado 5 del artículo 64 ET), que se emite en quince días desde que se pide con la información necesaria (apartado 6 del artículo 64 ET); los delegados de personal tienen las mismas competencias (apartado 2 del artículo 62 ET). Los representantes tienen derecho a información **mensual** de las horas extraordinarias con copia de los resúmenes (disposición adicional tercera del Real Decreto 1561/1995, leída en internet) y el convenio puede añadir obligaciones propias. No consultar ni informar es infracción grave distinta de la del tiempo de trabajo (apartado 7 del artículo 7 del Real Decreto Legislativo 5/2000).
- Reglamento de desarrollo: el Gobierno puede fijar especialidades del registro (art. 34.7 ET) y en 2025-2026 se tramitó un proyecto de real decreto de registro de jornada digital. Comprueba en cada encargo si se ha aprobado: `buscar_boe` con `desde` (ojo: `novedades_boe` solo recorre 31 días desde la fecha inicial) y, si no aparece, internet en el BOE y en las referencias del Consejo de Ministros. Si sigue en proyecto, dilo así, con su enlace oficial, y no lo apliques como norma.

- El TJUE exige a los Estados que obliguen a los empleadores a establecer un sistema **objetivo, fiable y accesible** que permita computar la jornada diaria (Directiva 2003/88 y art. 31.2 de la Carta), y ha declarado contraria a esa exigencia la exención de los empleadores domésticos. Léelo antes de afirmarlo (ver «Estrategia») y úsalo para valorar si el sistema de la empresa cumple.
- Criterio técnico de la Inspección sobre el registro de jornada: no está en Jurisprudenciator; búscalo en internet en la web oficial de la Inspección de Trabajo y cítalo con su enlace y la fecha de consulta, como criterio de actuación (no es norma), y úsalo para la auditoría. El PDF oficial puede ser una imagen escaneada: léelo página a página y no le atribuyas nada que no hayas leído.
- Especialidades: el Gobierno puede establecer especialidades del registro por sectores (art. 34.7 ET); jornadas especiales y tiempos de presencia en el Real Decreto 1561/1995 (lee el artículo del sector); trabajo a distancia (artículo 14 de la Ley 10/2021, de 9 de julio, de trabajo a distancia: el registro refleja fielmente el tiempo, con inicio y fin); servicio del hogar (artículo 9 del Real Decreto 1620/2011, que excluye el registro de los arts. 35.5 y 12.5.h ET; contrasta con la doctrina del TJUE).
- Tiempo parcial (art. 12.4.c ET): registro día a día, totalizado mensualmente, con copia del resumen de horas ordinarias y complementarias junto al recibo de salarios, conservado cuatro años; si se incumple, el contrato se presume a jornada completa salvo prueba en contrario. No caben horas extraordinarias salvo las del art. 35.3; las complementarias, con los límites del art. 12.5.
- Sistema y datos personales: el control debe respetar la intimidad y la información previa a la plantilla (arts. 87 a 90 LOPDGDD); si el sistema usa huella o reconocimiento facial, son datos biométricos cuyo tratamiento está prohibido salvo que concurra alguna excepción del apartado 2 del art. 9 RGPD: compruébala antes de validarlo y valora un sistema alternativo; derecho a la desconexión digital (art. 88 LOPDGDD).

**Jornada y descansos:** jornada máxima de cuarenta horas semanales de promedio anual, distribución irregular con los límites y el preaviso del art. 34.2, nueve horas ordinarias diarias salvo convenio o acuerdo, doce horas entre jornadas y pausa de quince minutos si la jornada continuada supera seis horas (art. 34.1 a 34.4 ET; reglas propias para menores); descanso semanal de día y medio acumulable hasta catorce días (art. 37.1 ET); nocturnidad (art. 36 ET); vacaciones no sustituibles por dinero (art. 38 ET). El tiempo se computa estando en el puesto al inicio y al final (art. 34.5 ET). Guardias de presencia, disponibilidad y desplazamientos de trabajadores sin centro fijo: consulta la doctrina antes de calificarlos (ver «Estrategia»).

**Horas extraordinarias (art. 35 ET):**

- Las que superan la jornada máxima ordinaria fijada conforme al art. 34 (legal o pactada: mira el cómputo del convenio).
- Retribución no inferior a la hora ordinaria o compensación con descanso retribuido, según convenio o contrato; sin pacto, descanso dentro de los cuatro meses siguientes.
- Máximo de ochenta al año (reducción proporcional a tiempo parcial); no computan las compensadas con descanso en cuatro meses ni las de fuerza mayor del art. 35.3, que se retribuyen igualmente.
- Voluntarias, salvo pacto en convenio o contrato dentro de los límites.
- La negativa a hacer horas extraordinarias no pactadas, o complementarias fuera de las reglas del art. 12.5 ET (letras f y g), no es conducta sancionable: compruébalo antes de redactar o impugnar una sanción (`sanciones-disciplinarias`).
- Registro día a día, totalizado en el periodo de abono, con copia del resumen en el recibo (art. 35.5 ET).
- Superar límites o descansos, o no registrar, es infracción grave (apartado 5 del artículo 7 del Real Decreto Legislativo 5/2000); no consultar a la representación sobre el sistema o no informarle de las horas extraordinarias, también (apartado 7 del mismo artículo); graduación y cuantía en sus arts. 39 y 40, leídas en el momento. No escribas importes de memoria.

**Prueba de las horas:**

- Principio de disponibilidad y facilidad probatoria (apartado 7 del artículo 217 de la Ley de Enjuiciamiento Civil); si la empresa no aporta el registro requerido como prueba, pueden tenerse por probadas las alegaciones contrarias (art. 94.2 LRJS).
- La Sala Cuarta distingue: si existe un **horario prefijado**, conocido y habitualmente cumplido, la falta de registro no obliga a la empresa a probar la jornada: el trabajador debe aportar **indicios suficientes** de los excesos; si el trabajador sigue **patrones irregulares** (llamamientos, turnos imprevisibles), lo que se prueba es la jornada completa y la falta de registro pesa más contra la empresa. Lee la sentencia y aplica la regla que corresponda al caso.
- Prescripción de un año de cada cantidad desde que fue exigible (art. 59.1 y 59.2 ET): las horas prescriben mes a mes; la papeleta la interrumpe.

**Cómo se reconstruye y se calcula la jornada (para las dos posiciones):**

1. Fija el periodo de referencia del exceso con el convenio: si computa la jornada en cómputo anual o hay distribución irregular, las diferencias se compensan en el plazo del convenio o, en su defecto, en doce meses (art. 34.2 ET). No conviertas en horas extraordinarias los excesos de una semana que el propio sistema compensa después: compara con la jornada del periodo de referencia.
2. Determina qué tiempo es de trabajo efectivo antes de sumar (pausas no computables, guardias, tiempos de presencia de las jornadas especiales, desplazamientos), con el convenio y la doctrina de la consulta sobre tiempo de trabajo.
3. Ordena las fuentes por fuerza probatoria y dilo en la tabla: registro de la empresa; documentos generados por sistemas de la empresa (accesos, conexiones, tacógrafo, geolocalización, correos con hora); documentos del trabajador (anotaciones, mensajes); testigos. Un día sin ninguna fuente no se incluye como hora probada: se marca como estimación.
4. Resta lo ya pagado o compensado con descanso (según nóminas y cuadrantes) y la compensación pactada en el convenio (proporción de descanso por hora).
5. Separa los tramos que tengan precio distinto en el convenio (nocturnas, festivos, horas extraordinarias estructurales) y excluye lo prescrito a la fecha de la papeleta.
6. En tiempo parcial, las horas que superan la jornada pactada sin pacto de complementarias o por encima de sus límites se analizan con el art. 12 ET: pueden sostener la presunción de jornada completa si el registro no se llevó; plantéalo con `contrato-trabajo-modalidad` o en la demanda de cantidad.

**Errores que la empresa debe corregir y el trabajador debe aprovechar:** registro que solo recoge la entrada o que reproduce el horario teórico todos los días sin variación; correcciones sin traza; horas extraordinarias pagadas con conceptos opacos («plus de disponibilidad», «incentivo») sin totalizar en nómina; descanso compensatorio fuera de los cuatro meses sin pacto; personal a tiempo parcial o en teletrabajo sin registro; sistema implantado sin la consulta previa a la representación.

## Estrategia y jurisprudencia

1. **Empresa (auditoría)**: comprueba, punto por punto, que existe registro para toda la plantilla (tiempo parcial, teletrabajo, itinerantes, turnos), que recoge inicio y fin reales de cada día, que las pausas no computables quedan identificadas, que cada corrección deja traza con autor y motivo, que la implantación consta en convenio, acuerdo o decisión previa consulta e informe de la representación documentados, que se conserva cuatro años y se entrega a quien tiene derecho, que las horas extraordinarias se totalizan, figuran en nómina y se informan cada mes a la representación, que el pago o el descanso cumplen el convenio y los cuatro meses, que el precio pagado por hora (urgencias, fines de semana) no es inferior al de la hora ordinaria, y que los descansos se respetan. Si el convenio computa la jornada en cómputo anual, comprueba que el calendario laboral (art. 34.6 ET) cuadra el horario con la jornada anual y si los excesos de temporada se compensan con la bolsa de flexibilidad del convenio (con su preaviso) o son horas extraordinarias: no des por extraordinaria una estimación de excesos sin ese contraste, pero advierte que sin registro la compensación es difícil de probar. Cruza una muestra de registros con nóminas, cuadrantes y accesos: las discrepancias son el riesgo real ante la Inspección y en juicio.
2. **Trabajador**: clasifica el caso (horario prefijado o patrón irregular) antes de preparar la prueba; reconstruye las horas día a día con cada fuente y señala qué días tienen prueba directa y cuáles solo indicios; pide por escrito a la empresa copia del registro antes de demandar y, en la demanda, su aportación con el apercibimiento del art. 94.2 LRJS; descarta lo prescrito; valora la denuncia ante la Inspección.
3. Consultas en Jurisprudenciator (reformula como máximo dos veces si no hay resultados útiles):
   - Registro y carga de la prueba: `buscar_sentencias` (`consulta="horas extraordinarias registro diario de jornada carga de la prueba horario prefijado patrones irregulares"`, `base="TS"`, `jurisdiccion="SOCIAL"`, `fecha_desde="01/01/2026"`) y, en el territorio, `consulta="horas extraordinarias ausencia registro de jornada indicios"`, `base="AN"`, `tipo_organo="TSJ"`, `anios=3`.
   - TJUE: `buscar_sentencias` (`consulta="tiempo de trabajo registro diario sistema que permita computar la jornada"`, `base="TJUE"`) (la de la Gran Sala sobre el sistema objetivo, fiable y accesible); hogar familiar: `consulta="registro tiempo de trabajo empleados de hogar"`, `base="TJUE"`.
   - Validez de un sistema pactado: `consulta="registro de jornada acuerdo convenio colectivo sistema objetivo fiable accesible"`, `base="TS"`.
   - Tiempo de trabajo: `consulta="guardias de presencia física tiempo de trabajo efectivo"` y `consulta="tiempo de trabajo desplazamiento domicilio primer cliente trabajadores sin centro fijo"`, `base="TS"` (y `base="TJUE"`).
   - Compensación y valor: `consulta="descanso retribuido compensación horas extraordinarias equivalencia"` y `consulta="valor hora extraordinaria conceptos salariales computables"`, `base="TS"`.
4. Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar y transcribe fundamentos, nunca hechos ni datos de aquel pleito. En la política interna no va jurisprudencia: va en la nota o el informe.

## Documentos que se entregan

Todos en Word según `references/formato-y-organos-laboral.md`.

**Posición de la empresa:**

1. Informe de auditoría (`nota-auditoria-registro-jornada-<empresa>-<AAAAMMDD>.docx`): resumen de riesgo; hallazgos en tabla (requisito · precepto · situación · evidencia · riesgo · corrección); infracciones posibles con su artículo y la remisión a los arts. 39 y 40 del Real Decreto Legislativo 5/2000; riesgo de reclamaciones (periodo no prescrito, colectivos afectados); plan de corrección con plazos; artículos y convenio leídos; doctrina literal.
2. Política de registro de jornada (`politica-registro-jornada-<empresa>-<AAAAMMDD>.docx`): ámbito (toda la plantilla y modalidades); sistema y cómo se ficha; inicio, fin y pausas; trabajo a distancia y fuera del centro; correcciones con traza; horas extraordinarias (autorización previa, voluntariedad, pago o descanso en cuatro meses según convenio, totalización y copia en nómina); tiempo parcial (resumen mensual); descansos mínimos; desconexión digital; protección de datos e información a la plantilla; conservación cuatro años y acceso de trabajadores, representación e Inspección; régimen disciplinario remitido al convenio; información mensual de horas extraordinarias a la representación; constancia de la consulta y del informe previo de la representación (letra f) del apartado 5 del artículo 64 ET) o del acuerdo.

**Posición del trabajador:**

1. Cálculo de horas (`calculo-horas-extra-<apellido-trabajador>-<AAAAMMDD>.docx`), en tabla visible: por semana o mes según el cómputo del convenio, horas trabajadas, jornada ordinaria aplicable, exceso, horas ya pagadas o compensadas, horas pendientes, prueba de cada periodo y marca de lo prescrito; valor de la hora (precio del convenio o del contrato; si no lo hay, salario anual de los conceptos que retribuyen la jornada ordinaria dividido por la jornada anual del convenio, nunca inferior a la hora ordinaria) y total; si el precio o el salario salen de la tabla del convenio, búscala en internet en el boletín oficial del año y cítala con su enlace (apartado 3 de las anclas); sin tabla ni salario acreditado no se calcula.
2. Nota de estrategia (`nota-horas-extra-<apellido-trabajador>-<AAAAMMDD>.docx`): calificación del caso según la doctrina del registro, prueba disponible y su peso, plazo de prescripción con fechas, pasos (requerimiento del registro, papeleta, demanda con `reclamacion-cantidad`, denuncia a la Inspección) y riesgos.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado, ni en Jurisprudenciator ni en internet.
- [ ] Todo dato que no sale de Jurisprudenciator (orden de cotización, tabla salarial, criterio técnico, nombre de un órgano, sede electrónica) lleva su enlace oficial y la fecha de consulta, y el resumen lo identifica.
- [ ] Leídos con `buscar_articulo` en esta conversación: ET 12, 34, 35, 36, 37, 38 y 59 (los usados), con su fecha de vigencia; Real Decreto 1561/1995 (sector), Ley 10/2021 art. 14 y Real Decreto 1620/2011 art. 9 si aplican; Real Decreto Legislativo 5/2000 arts. 7 (apartados 5 y 7), 39 y 40; LEC 217; LRJS 94; LOPDGDD 87-90 y RGPD 9 si se analiza el sistema; ET 62 y 64 en la auditoría y en la política (consulta e informe previo). Disposición adicional tercera del Real Decreto 1561/1995 leída en internet con su enlace, y comprobado si se ha aprobado un reglamento de registro de jornada.
- [ ] Convenio leído con `leer_convenio` (jornada, horas extraordinarias, registro) y vigencia comprobada para cada año del periodo.
- [ ] Caso clasificado (horario prefijado o patrón irregular) con la doctrina leída; doctrina del TJUE leída si se invoca.
- [ ] Cálculo visible, semana a semana o mes a mes, con lo prescrito excluido y fuente de cada cifra; ninguna cuantía de sanción escrita de memoria.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`; ninguna jurisprudencia en la política.
- [ ] `verificar_escrito` pasado sobre cada documento; los avisos de «posible disonancia» contrastados con el apartado exacto leído.
- [ ] Marcadores en lugar de datos no facilitados.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y para quién; prescripción y fechas; cálculo y de dónde sale cada cifra; riesgos y documentos que faltan; tabla de jurisprudencia; próximo paso.
