---
name: sanciones-disciplinarias
description: >-
  Prepara la carta de sanción disciplinaria (amonestación, suspensión de empleo y sueldo u otra prevista en el
  convenio) con su nota de riesgo para la empresa, o analiza una sanción ya impuesta para impugnarla en nombre del
  trabajador. Úsala cuando digan «quiero sancionar a un trabajador», «carta de sanción», «falta grave o muy grave»,
  «suspensión de empleo y sueldo», «me han sancionado», «impugnar la sanción» o «¿ha prescrito la falta?». Comprueba
  tipificación y graduación en el convenio, sanciones prohibidas, forma escrita, expediente contradictorio, audiencia
  a delegados sindicales, prescripción y plazo de impugnación (arts. 114-115 LRJS). Sirve a empresa y trabajador. Si
  la sanción es el despido, usa carta-despido-disciplinario; para la papeleta, papeleta-conciliacion.
---

# Sanciones disciplinarias: carta de sanción e impugnación

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Poder disciplinario, graduación, forma y sanciones prohibidas** → `buscar_articulo` (`ley="ET"`, `articulo="58"`); **incumplimientos contractuales tipificados en la ley** → `buscar_articulo` (`ley="ET"`, `articulo="54"`).
- **Prescripción de la falta** → `buscar_articulo` (`ley="ET"`, `articulo="60"`) + `buscar_sentencias` (`consulta="prescripción faltas laborales dies a quo conocimiento cabal faltas continuadas ocultación"`, `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`, `terminos="prescripción conocimiento cabal pleno y exacto"`). Si hay expediente contradictorio o audiencia a delegados sindicales: `buscar_sentencias` (`consulta="audiencia delegados sindicales sanción prescripción corta tiempo invertido"`, `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`terminos="expediente disciplinario preceptivo interrupción suspensión prescripción corta"`).
- **Garantías de representantes y afiliados** → `buscar_articulo` (`ley="ET"`, artículos `"68"`, `"55"` y `"64"`) y (`ley="LOLS"`, `articulo="10"`).
- **Impugnación, plazo, vía previa y contenido de la sentencia** → `buscar_articulo` (`ley="LRJS"`, artículos `"114"`, `"115"`, `"103"`, `"43"`, `"64"`, `"65"` y, si se invocan derechos fundamentales, `"184"`).
- **Convenio aplicable: faltas, sanciones, procedimiento y prescripción convencional** → `buscar_convenio` (`consulta` con el nombre del sector tal como lo usa el registro, por ejemplo «metal», «hostelería» o «contact center», y `territorio` = provincia del centro; si no sale nada, simplifica la consulta) + `leer_convenio` (`buscar_en="faltas"` para localizar el capítulo; después `articulo="N"` para leer cada artículo completo). Si el convenio provincial remite el régimen disciplinario a un acuerdo o convenio estatal, lee los artículos en el estatal y comprueba la remisión. Después, `vigencia_convenio` de cada convenio que uses: **`leer_convenio` devuelve el texto publicado originalmente, no las modificaciones posteriores**. Si `vigencia_convenio` registra una modificación, un acuerdo parcial o un pronunciamiento de tribunal posterior a esa publicación y anterior a la sanción, búscalo en internet en el boletín oficial (BOE, boletín autonómico o BOP) y comprueba si cambia los artículos que aplicas; cítalo con su enlace (punto 3 de la puerta). Si no lo localizas, dilo en la nota.
- **Doctrina sobre tipicidad, proporcionalidad y elección de una sanción inferior** → `buscar_sentencias` (`consulta="sanción disciplinaria calificación muy grave sanción inferior tipicidad proporcionalidad nulidad"`, `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`).
- **Tutela acumulada (defensa del trabajador)** → `buscar_articulo` (`ley="LRJS"`, artículos `"178"`, `"180"`, `"183"` y `"191"`).
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

Primera pregunta, siempre: **¿a quién defiende el abogado?**

- **Empresa**: quiere imponer una sanción que aguante la impugnación. Entregas carta de sanción, los escritos del procedimiento previo que procedan y nota de riesgo.
- **Trabajador**: ha recibido una sanción y quiere saber si la puede tumbar y en qué plazo. Entregas nota de impugnación con los motivos ordenados por fuerza y el plazo calculado.

| Situación | Skill que procede |
|---|---|
| La sanción que se quiere imponer es el despido | `carta-despido-disciplinario` |
| No se sabe qué convenio se aplica o hay concurrencia de convenios | primero `convenio-aplicable` |
| El trabajador impugna: hay que presentar la papeleta | `papeleta-conciliacion` (esta skill le pasa los motivos y el plazo) |
| La sanción encubre un traslado o un cambio de funciones o de condiciones | `movilidad-geografica-funcional` o `modificacion-sustancial-condiciones` |
| La conducta sancionada nace de una denuncia de acoso | `protocolo-acoso-laboral` además de esta |
| Se reclama una tutela de derechos fundamentales sin sanción ni despido | `tutela-derechos-fundamentales` |
| Lo que se discute es una infracción del empresario ante la Inspección | `inspeccion-trabajo-alegaciones` |

Si la sanción impuesta invoca o lesiona un derecho fundamental (represalia por reclamar, libertad sindical, discriminación), sigue en esta skill: el art. 184 LRJS obliga a tramitarla por la modalidad de impugnación de sanciones, acumulando la tutela.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende el abogado.
2. ★ Hechos: qué hizo el trabajador, día (y hora si importa), lugar, quién lo presenció y qué pruebas hay (partes, correos, registros, testigos). Si son varios hechos o una conducta repetida, la fecha de cada uno.
3. ★ Fecha y forma en que **la empresa conoció** los hechos, y quién (qué cargo) los conoció; si hubo investigación interna, fecha de inicio y de cierre, y si el trabajador ocupaba un puesto de confianza que le permitiera ocultarlos.
4. ★ Convenio colectivo (denominación o código, si lo sabe), actividad real de la empresa y provincia del centro de trabajo.
5. ★ Condición del trabajador: representante legal (miembro del comité o delegado de personal) o lo fue en el último año; delegado sindical; afiliado a un sindicato y si la empresa lo sabe; si existen delegados sindicales de su sección en la empresa o el centro.
6. ★ Sanciones anteriores (fecha, falta, si se impugnaron) cuando la calificación dependa de la reincidencia; y si el convenio cancela las anteriores al cabo de un tiempo.
7. ★ Procedimiento previo que exija el convenio, un reglamento interno o el contrato (pliego de cargos, plazo de alegaciones, comunicación a la representación).
8. Circunstancias que abren la nulidad: embarazo, permisos o adaptaciones del art. 37 o 34.8 ET solicitados o en curso, reclamaciones o denuncias previas del trabajador, baja médica, actividad sindical.
9. **Solo trabajador**: ★ carta de sanción, ★ fecha de notificación y forma (entrega en mano, burofax, correo), fecha en que se cumplió o se cumplirá, si firmó el recibí o puso «no conforme», y ★ salario diario si la sanción es de suspensión (para reclamar lo descontado).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**1. Tipicidad y graduación (art. 58.1 ET).** Solo se sanciona lo que la ley o el convenio tipifican, con la graduación que fijen. Lee el capítulo de faltas y sanciones del convenio artículo por artículo y construye la tabla: hecho → tipo del convenio (artículo y letra) → grado (leve, grave, muy grave) → sanciones previstas para ese grado. Una sanción no tipificada en la ley o el convenio es nula (art. 115.1.d LRJS).
- Sobre elegir una sanción de grado inferior al de la falta calificada, la Sala Cuarta la ha admitido como ejercicio de la potestad disciplinaria: localízala con la consulta de doctrina de la lista y léela antes de aconsejar o de atacar esa elección.
- Si el hecho encaja a la vez en el art. 54.2 ET y en el convenio, cita los dos; para la graduación manda el convenio.

**2. Sanciones prohibidas (art. 58.3 ET).** No cabe reducir la duración de las vacaciones ni minorar otros descansos, ni imponer multa de haber. Si la sanción propuesta o impuesta lo hace, es nula (art. 115.1.d LRJS): propón otra sanción del catálogo del convenio.

**3. Forma (art. 58.2 ET).** Las faltas graves y muy graves exigen comunicación escrita con la fecha y los hechos que la motivan. Comprueba si el convenio exige además forma escrita para las leves. La empresa no podrá alegar después otros motivos distintos de los comunicados (art. 114.3 LRJS): todo hecho que quiera usar va en la carta.

**4. Expediente contradictorio (art. 68.a ET y art. 10.3 LOLS).** Para sancionar por falta grave o muy grave a un representante legal o a un delegado sindical hay que abrir expediente contradictorio y oír al interesado y al comité o a los restantes delegados. Sin él, la sanción es nula (art. 115.2 LRJS) y en juicio la empresa debe aportar el expediente (art. 114.2 LRJS). Si el trabajador dejó de ser representante hace menos de un año, abre el expediente igualmente: no cuesta nada y cierra la discusión sobre la garantía del art. 68.c ET. El expediente se dirige al interesado y a los restantes miembros de la representación, con el mismo plazo para alegar. Si la falta es una ausencia, un retraso o una salida del puesto de un representante o delegado, comprueba antes si pudo ser uso del crédito horario (art. 68.e ET y lo que el convenio exija de preaviso y justificación) y pídele en el pliego que lo acredite: sancionar una actuación representativa vulnera la garantía del art. 68.c ET y la libertad sindical.

**5. Audiencia a los delegados sindicales (art. 10.3.3.º LOLS; art. 115.2 LRJS).** Si el trabajador está afiliado y a la empresa le consta, hay que oír antes a los delegados sindicales de su sección. Comprueba en el art. 10.1 LOLS y en el convenio si en esa empresa o centro existen delegados sindicales; si no existen, dilo en la nota.

**6. Requisitos del convenio.** Cualquier requisito formal convencional (pliego de cargos, plazo de alegaciones, informe de la representación, plazo para imponer la sanción) se cumple al pie de la letra: su omisión o un defecto que frustre su finalidad hace nula la sanción (art. 115.1.d LRJS).

**7. Información al comité (art. 64.4.c ET).** El comité debe ser informado de todas las sanciones por faltas muy graves. Comprueba si el convenio convierte esa información en requisito previo; si no, documéntala igualmente.

**8. Nulidad por la persona o el móvil (art. 115.1.d LRJS en relación con el art. 108.2 LRJS y el art. 55.5 ET).** Si concurre alguna de las situaciones del dato 8, la sanción corre el riesgo de nulidad: la empresa necesita hechos acreditados y ajenos a esa circunstancia; el trabajador, aportar indicios (el art. 55.5 ET, leído, lista los supuestos objetivos). Si en el art. 55.5 aparece una nota «Téngase en cuenta» con otra redacción de la letra b), compara las dos y dile al abogado qué supuestos cambian.

**9. Prescripción (art. 60.2 ET).** Faltas leves, diez días; graves, veinte; muy graves, sesenta, desde que la empresa tuvo conocimiento, y en todo caso seis meses desde la comisión. Calcula las dos fechas (corta y larga) y compáralas con la fecha de notificación de la sanción:
- Dies a quo según la doctrina que localiza la consulta de la lista: el conocimiento que cuenta es el cabal, pleno y exacto, cuando los hechos exigen investigarlos, y el que llega a un órgano con facultades sancionadoras; si el trabajador ocultó los hechos aprovechando su cargo, el plazo no corre mientras dura la ocultación. Lee la sentencia y cita su párrafo.
- **Faltas continuadas o repetidas**: busca la doctrina (`consulta="falta continuada prescripción último acto cómputo dies a quo"`, `base="TS"`, `jurisdiccion="SOCIAL"`) y fija de qué acto parte cada plazo.
- **Expediente previo**: si se abrió un expediente o una investigación, busca si interrumpió el plazo (`consulta="expediente disciplinario interrupción prescripción faltas artículo 60.2"`) y en qué condiciones; no lo afirmes sin leerlo. Para el expediente preceptivo por ley o convenio y para la audiencia a los delegados sindicales, usa además la consulta específica de la lista: la Sala Cuarta ha tratado el tiempo de esos trámites como suspensión del plazo corto. Aun así, **calendariza sin contar con ese descuento**: la carta debe salir antes del límite más estricto (el conocimiento más temprano que un juez podría imputar a la empresa, por ejemplo el del mando que presenció los hechos).
- **Días naturales o hábiles**: el art. 60.2 ET no lo dice. Busca la doctrina (`consulta="prescripción faltas artículo 60.2 días naturales cómputo"`); si no la encuentras, computa en días naturales, que es la lectura más estricta para la empresa, y dilo en la nota.
- Comprueba si el convenio regula la prescripción: si fija plazos más largos que la ley, adviértelo; el art. 60.2 ET es el que se aplica en caso de duda.

**10. Impugnación (arts. 114 y 103 LRJS).** El trabajador tiene **20 días hábiles** desde la notificación de la sanción, con papeleta previa obligatoria (la impugnación de sanciones no está entre las excepciones del art. 64 LRJS) que suspende el plazo (art. 65 LRJS). Las sanciones no figuran entre las modalidades del art. 43.4 LRJS: agosto y del 24 de diciembre al 6 de enero son inhábiles, salvo que se tramite con tutela de derechos fundamentales; en ese caso lee el art. 43.4 y el 184 LRJS y, si hay duda, computa esos días como hábiles (lectura prudente). Da siempre fecha inicial, precepto y fecha final. Si se acumula la tutela, la excepción del art. 64 para la tutela y la regla de la modalidad de sanciones chocan: cuando quede poco plazo, aconseja presentar la papeleta y también la demanda dentro del plazo original, sin contar con la suspensión. Con tutela acumulada se aplican las garantías del capítulo de tutela (art. 178.2 LRJS): pide la indemnización del art. 183 y valora la suspensión cautelar del art. 180. El nombre del servicio de conciliación es el de la comunidad autónoma, buscado en su sede oficial (apartado 3 del formato).

**11. Qué puede decidir el juez (art. 115 LRJS).** Confirmar; revocar totalmente, con condena a los salarios descontados; revocar en parte si la falta es de menor grado y no había prescrito, autorizando a la empresa a imponer la sanción adecuada en diez días desde la firmeza; o declarar la sanción nula. Contra la sentencia solo cabe recurso en sanciones por faltas muy graves apreciadas judicialmente (art. 115.3 LRJS y art. 191.2.a LRJS): dilo en la nota, porque la instancia suele ser la única oportunidad. Si se acumula la tutela, el art. 191.3.f LRJS admite siempre la suplicación en tutela: si no localizas doctrina que resuelva la tensión, no garantices ni excluyas el recurso.

## Estrategia y jurisprudencia

**Si defiendes a la empresa:**

1. Calcula la prescripción antes que nada: si la falta muy grave ya no se puede sancionar, dilo y para.
2. Encaja cada hecho en un tipo concreto del convenio y elige la sanción dentro del abanico de ese grado; justifica en la nota la elección (reincidencia, perjuicio, puesto).
3. Si hay representante, delegado o afiliado conocido, planifica el expediente o la audiencia con fechas y deja el rastro documental antes de firmar la carta.
4. Redacta los hechos con día, lugar y conducta: la carta es el único material que la empresa podrá defender en juicio.
5. Fija las fechas de cumplimiento de la suspensión en la carta y comprueba si el convenio pone plazo para ejecutarla. Si el convenio no dice si los días de suspensión son naturales o laborables, fija días naturales consecutivos o, si fijas días laborables, comprueba que, contados en días naturales, cada sanción sigue dentro de la escala de su grado.

**Si defiendes al trabajador**, ataca en este orden y detente en el primero que prospere, pero alega todos:

1. Prescripción (corta y larga, con el dies a quo discutido).
2. Forma: sin escrito, sin fecha o sin hechos concretos.
3. Expediente contradictorio o audiencia a delegados sindicales omitidos, o requisito del convenio incumplido (nulidad del art. 115.1.d y 115.2 LRJS).
4. Falta de tipicidad o sanción prohibida.
5. Hechos no probados o de menor entidad (revocación total o parcial).
6. Móvil lesivo de derechos fundamentales o supuesto del art. 55.5 ET (nulidad, con tutela acumulada del art. 184 LRJS).

**Consultas en Jurisprudenciator** (reformula como máximo dos veces; prioriza lo reciente con `anios=5` y amplía si no hay nada):

- Prescripción: las tres consultas del apartado 9, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Tipicidad y graduación: la consulta de doctrina de la lista y, si el convenio es sectorial provincial, la misma con `base="AN"`, `tipo_organo="TSJ"` y la `provincia` de la sede de la Sala.
- Expediente o audiencia omitidos: `consulta="sanción representante legal expediente contradictorio omisión nulidad"` y `consulta="sanción afiliado audiencia delegados sindicales nulidad"`, `base="TS"`.
- Represalia: `consulta="sanción disciplinaria garantía de indemnidad indicios reclamación previa"`, `base="TS"`; en `base="TC"` la búsqueda es literal sobre el texto: usa pocas palabras (`consulta="garantía de indemnidad"`; `consulta="reducción de jornada discriminación por razón de sexo"` si la sanción castiga un derecho de conciliación).

Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar, transcribe el párrafo de fundamentos y comprueba que es razonamiento de la Sala. La jurisprudencia va en la nota, nunca en la carta.

## Documentos que se entregan

Todo en Word según `references/formato-y-organos-laboral.md`.

**Empresa:**

1. **Carta de sanción** — `carta-sancion-<apellido-trabajador>-<AAAAMMDD>.docx`:
   - Membrete (`[DENOMINACIÓN SOCIAL]`, `[CIF]`), destinatario (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`), lugar y fecha, asunto «Comunicación de sanción por falta [grado]».
   - Hechos, uno por párrafo: fecha, lugar, conducta concreta y consecuencia; sin valoraciones genéricas.
   - Calificación: artículo y letra del convenio (con su denominación y código) y, si procede, letra del art. 54.2 ET; grado de la falta.
   - Sanción: la del catálogo del convenio para ese grado; si es suspensión, número de días y fechas exactas de cumplimiento.
   - Mención del expediente contradictorio o de la audiencia a delegados sindicales realizados, con sus fechas, cuando procedan.
   - Firma de la empresa y recibí del trabajador con fecha, o constancia de la negativa a firmar ante dos testigos; copia a la representación si el convenio o el art. 64.4.c ET lo piden.
2. **Si hay representante o delegado**: comunicación de apertura del expediente contradictorio con el pliego de cargos, al interesado y al comité o restantes delegados, con plazo para alegaciones (el del convenio; si no fija ninguno, uno que permita defenderse y que no ponga en riesgo la prescripción, que sigue corriendo) — `carta-expediente-contradictorio-<apellido-trabajador>-<AAAAMMDD>.docx`.
3. **Si hay afiliado conocido**: comunicación a los delegados sindicales para su audiencia previa, con los hechos y plazo — `carta-audiencia-delegados-sindicales-<apellido-trabajador>-<AAAAMMDD>.docx`.
4. **Nota para el abogado** — `nota-sancion-<empresa>-<AAAAMMDD>.docx`: tabla hecho → tipo → grado → sanción; cálculo de la prescripción (fecha de comisión, fecha de conocimiento, fechas límite corta y larga); garantías aplicables y cómo se cumplen; artículos del ET, la LRJS, la LOLS y el convenio leídos; riesgos de nulidad o revocación; jurisprudencia con párrafo literal.

**Trabajador:**

1. **Nota de impugnación** — `nota-impugnacion-sancion-<apellido-trabajador>-<AAAAMMDD>.docx`: plazo (fecha de notificación, precepto, fecha final, efecto de la papeleta); motivos en el orden de la estrategia, cada uno con su artículo y, cuando exista, su doctrina literal; pronunciamiento que se pedirá (nulidad, revocación total o parcial); salarios a reclamar si la suspensión se cumplió (días × salario diario, en tabla); prueba que hay que pedir a la empresa; posibilidad de recurso según el art. 115.3 LRJS.
2. Papeleta: pásale a `papeleta-conciliacion` los motivos y el plazo.
3. Si el abogado pide también la demanda, redáctala como escrito procesal (apartado 2 del formato) dirigida a la Sección de lo Social del Tribunal de Instancia, con los requisitos del art. 80 LRJS (léelo) y el suplico ajustado al art. 115 LRJS; acompaña la certificación del acto de conciliación.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Preguntado a quién defiende el abogado y bifurcado el trabajo.
- [ ] Leídos con `buscar_articulo` en esta conversación: ET 54, 55, 58, 60, 64 y 68; LOLS 10; LRJS 43, 64, 65, 103, 114 y 115 (y 184 y 80 si se usan).
- [ ] Convenio identificado, capítulo de faltas y sanciones leído artículo por artículo con `leer_convenio`, y vigencia en la fecha de los hechos comprobada con `vigencia_convenio`; las modificaciones o sentencias posteriores al texto leído, localizadas en el boletín oficial y revisadas (o señaladas como pendientes en la nota).
- [ ] Prescripción calculada con fechas (corta y larga), con la doctrina del dies a quo leída y, si hay conducta continuada o expediente previo, con su doctrina.
- [ ] Garantías revisadas: expediente contradictorio, audiencia a delegados sindicales, requisitos del convenio, información al comité.
- [ ] Sanción del catálogo del convenio y no prohibida por el art. 58.3 ET.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; la carta no lleva jurisprudencia.
- [ ] `verificar_escrito` pasado sobre cada documento; los artículos del convenio, contrastados con `leer_convenio` (el verificador no los reconoce).
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[DENOMINACIÓN SOCIAL]`, `[CIF]`, fechas no facilitadas) en vez de datos inventados.
- [ ] Plazo de impugnación con fecha inicial, precepto y fecha final, y tratamiento de agosto y Navidad justificado.
- [ ] Resumen para el abogado según el apartado 9 del formato.
