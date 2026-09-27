---
name: menores-extranjeros
description: >-
  Menores extranjeros en España (art. 35 LOEX; arts. 159 a 174 del Real Decreto 1155/2024): residencia del
  hijo nacido en España o no nacido de residente, desplazamientos temporales humanitarios, y menores
  extranjeros no acompañados: determinación de la edad, repatriación, residencia del tutelado y acceso a
  la mayoría de edad con y sin autorización. Redacta en Word la solicitud de autorización, las alegaciones
  en el procedimiento de repatriación o la oposición al decreto de determinación de edad por la vía del
  art. 780 LEC. Aplica la sentencia del Supremo de 8 de julio de 2026 que anuló incisos de los arts. 159,
  160 y 166. Úsala con «menor no acompañado», «extutelado», «cumple 18», «pruebas de edad», «decreto de la
  Fiscalía», «repatriación», «hijo nacido aquí». Si es víctima de trata, usa también victimas-trata; si
  pide asilo, proteccion-internacional-apatridia.
---

# Menores extranjeros

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen legal del menor no acompañado y contingencias migratorias** → `buscar_articulo` (`ley="LOEX"`, artículos `"35"`, `"35 bis"`, `"35 ter"`, `"35 quáter"` y `"35 quinquies"`).
- **Menores acompañados y desplazamientos temporales** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"159"` a `"164"`, uno por llamada, y `"67"` para los medios y la vivienda que exige el art. 160).
- **Menores no acompañados: edad, repatriación, residencia y mayoría de edad** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"165"` a `"174"`, `"210"` y `"214"`).
- **Anulaciones del Tribunal Supremo** → cuando un artículo traiga la nota «Téngase en cuenta que se declara la nulidad del inciso destacado», el conector no marca el inciso: léelo en el fallo publicado con `leer_boe` (`identificador="BOE-A-2026-19632"`).
- **Determinación de la edad y oposición civil** → `buscar_articulo` (`ley="LO 1/1996"`, `articulo="12"`) y (`ley="LEC"`, artículos `"779"`, `"780"`, `"750"` para abogado y procurador, y `"133"` para el cómputo); órgano judicial → (`ley="LOPJ"`, artículos `"84"` y `"86"`: la sección la fija el art. 86.5.h); medida cautelar de reingreso → (`ley="CC"`, `articulo="158"`) y (`ley="LEC"`, `articulo="726"`).
- **Procedimiento de las autorizaciones por circunstancias excepcionales** (la del art. 174 lo es) → `buscar_articulo` (`ley="BOE-A-2024-24099"`, `articulo="130"`); órgano → `articulo="193"`.
- **Recurso y cautelares frente a la repatriación** → `buscar_articulo` (`ley="LJCA"`, artículos `"8"`, `"46"` y `"135"`).
- **Doctrina** → `buscar_sentencias` (edad: `base="TS"` con `jurisdiccion="CIVIL"`, porque la fija la Sala de lo Civil, y `base="TC"`; residencia y repatriación: `jurisdiccion="CONTENCIOSO"`, `base="AN"`; fechas en formato `dd/mm/aaaa`) + `leer_sentencias` (`parrafos=3`).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

## Cuándo usarla

Elige primero el bloque; cada uno tiene sus requisitos y su documento.

| Bloque | Situación | Preceptos |
|---|---|---|
| 1. Hijo nacido en España | Hijo de progenitores extranjeros con residencia | art. 159 |
| 2. Hijo no nacido en España o tutelado | Menor, o hijo con discapacidad, que vive con su progenitor o tutor residente | art. 160 |
| 3. Desplazamiento temporal | Programa humanitario de tratamiento médico, vacaciones o escolarización | arts. 161 a 164 |
| 4. Determinación de la edad | Indocumentado de edad incierta o documento cuya fiabilidad se discute | LOEX art. 35.3-4; art. 166; LO 1/1996 art. 12.4; LEC arts. 779-780 |
| 5. Repatriación | Procedimiento de repatriación de un menor no acompañado | LOEX art. 35.5-6; arts. 167 a 171 |
| 6. Residencia del menor tutelado | Autorización del menor no acompañado bajo protección | LOEX art. 35.7; art. 172 |
| 7. Mayoría de edad | Extutelado que cumple dieciocho con o sin autorización | LOEX art. 35.9; arts. 173 y 174 |

Detector: menor víctima de trata → también `victimas-trata` (arts. 154 y 165); menor víctima de violencia sexual → `victimas-violencia-genero-sexual` (art. 141); menor que pide asilo → `proteccion-internacional-apatridia` (art. 166.5 obliga a informarle); hijo de ciudadano de otro Estado de la UE o de español → `ciudadanos-ue-y-familiares` o `familiares-de-espanoles`; reagrupación desde el extranjero → `reagrupacion-familiar`; traslado entre comunidades autónomas por contingencia migratoria → ver «Huecos normativos».

## Sentencia del Supremo de 8 de julio de 2026 (publicada el 22/09/2026)

Anuló, entre otros, estos incisos del Reglamento. Léelos siempre en el fallo con `leer_boe` (`identificador="BOE-A-2026-19632"`) antes de citar los artículos afectados, porque `buscar_articulo` devuelve el texto con la nota pero sin marcar el inciso:

- Art. 159.1: el inciso «solteras» y el inciso que exigía que el menor no se hubiera ausentado de España desde su nacimiento; por auto de rectificación, esa condición se interpreta como **residencia efectiva habitual en España**, sin que las ausencias temporales y justificadas excluyan el precepto. El plazo de seis meses **no** se anuló.
- Art. 160.1: el inciso «solteros»; art. 160.2: el inciso que exigía que la tutela se hubiera constituido conforme al ordenamiento español.
- Art. 166.1: el inciso «en su caso»; la **atención inmediata** del art. 35.3 LOEX es imperativa e incondicionada desde que la policía comunica la localización de quien tiene minoría de edad incierta.

## Datos que hay que reunir antes de redactar

No redactes al primer disparo. Si falta un dato imprescindible (★), pídelo.

**Todos los bloques**
1. ★ Fecha de nacimiento que consta y documento que la acredita (pasaporte, acta, cédula de inscripción), nacionalidad y provincia de domicilio.
2. ★ Quién representa al menor y con qué título: progenitor, tutor, entidad pública de protección (resolución de tutela, guarda o protección provisional). Si actúa el abogado, su apoderamiento (art. 197.4). Si el menor tiene dieciséis años o más, puede actuar por sí en la repatriación y en el contencioso (LOEX art. 35.6). En la residencia del tutelado interviene quien acredite actuar en representación del servicio de protección (art. 172.1.b): una solicitud presentada por un abogado sin ese título se expone a la inadmisión, como muestra la doctrina de los TSJ (búscala antes de presentar).

**Bloques 1 y 2**
3. ★ Autorización de residencia de cada progenitor o del tutor (tipo y vigencia) y fecha en que accedieron a ella; en el bloque 1, fecha de nacimiento para el plazo de seis meses y periodos fuera de España con su causa.
4. ★ Escolarización si está en edad obligatoria; en el bloque 2, prueba de dos años de permanencia continuada, medios y vivienda de reagrupación y, si es hijo de uno solo de los cónyuges, patria potestad o custodia y consentimiento del otro progenitor o autorización judicial.

**Bloque 3**
5. ★ Promotor (administración, asociación o fundación inscrita), tipo de programa, fechas previstas, familia de acogida e informes del órgano autonómico de protección.

**Bloques 4 a 7 (menor no acompañado)**
6. ★ Fecha de localización, puesta a disposición de protección de menores y decreto de la Fiscalía (fecha, edad fijada, horquilla, pruebas realizadas, si se tuvo en cuenta el pasaporte), y resolución de la entidad pública derivada (cese de la protección, no declaración de desamparo) con su **fecha de notificación**.
7. ★ En repatriación: acuerdo de incoación y su notificación, informe consular sobre la familia, informes de la entidad de protección, voluntad del menor.
8. ★ En residencia y mayoría de edad: fechas de tutela y de la autorización, si se ha pedido la renovación, medios (empleo, programa de una entidad), acciones formativas, informes de integración, antecedentes penales.

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo, y aplica lo anulado según el apartado anterior.

**Bloque 1. Nacido en España (art. 159).** Hijo, biológico o adoptado, de progenitores extranjeros titulares de una autorización de residencia; sin visado; cinco años. El padre o la madre la solicita personalmente en los seis meses siguientes al nacimiento o a que uno de ellos acceda a la residencia, siempre que el menor esté en España y haya mantenido su residencia efectiva habitual aquí. Si el menor está en edad de escolarización obligatoria, matrícula en centro oficial. Documentos: pasaportes, certificado de nacimiento y escolarización. Subsanación en diez días; resolución en un mes y silencio desestimatorio; tarjeta en un mes con el progenitor; habilita a trabajar al llegar a la edad mínima; luego, larga duración.

**Bloque 2. No nacido en España o tutelado (art. 160).** Menor de dieciocho al solicitar, o hijo con discapacidad que no pueda proveer a sus necesidades, sin unidad familiar propia, acompañado del progenitor residente; **dos años** de permanencia continuada; los padres o tutores deben cumplir los medios y el alojamiento de la reagrupación (lee el art. 67). Hijo de uno solo de los cónyuges: patria potestad en solitario, custodia exclusiva con traslado autorizado, o custodia compartida con consentimiento del otro. Tutelado: menor acompañado por el residente que ejerce legalmente su tutela. Puede solicitarse mientras se tramita la residencia del progenitor. Subsanación en diez días; resolución en un mes y desestimación presunta; cinco años.

**Bloque 3. Desplazamientos temporales (arts. 161 a 164).** Informe previo favorable del Delegado o Subdelegado del lugar de estancia, con autorización de quien ejerce la patria potestad, informe favorable del órgano autonómico de protección (con certificados de antecedentes y de delitos sexuales de los convivientes mayores de catorce años), compromiso de regreso y, si hay familia de acogida, declaración de que no persigue la adopción (art. 161.3). Solicitud con tres a cuatro meses de antelación; silencio desestimatorio al mes (art. 161.4). Tratamiento médico: hasta noventa días, prórroga y, si es imprescindible seguir, residencia excepcional de hasta un año renovable con informe sanitario (art. 162). Vacaciones: desde ocho años, noventa días improrrogables (art. 163). Escolarización: desde doce años, naturaleza de estancia por estudios (art. 164).

**Bloque 4. Determinación de la edad.**
- Minoría indubitada por documento o apariencia: puesta a disposición de protección de menores e inscripción en el registro (art. 166.1; art. 214).
- Edad incierta: atención inmediata por los servicios autonómicos, imperativa desde la comunicación (fallo del Supremo); el Ministerio Fiscal dispone la determinación de la edad con pruebas prioritarias y urgentes (LOEX art. 35.3; art. 166.1).
- Mientras no se determina, es menor a efectos de protección; el fiscal debe hacer un juicio de proporcionalidad sobre por qué no es fiable el pasaporte o documento; las pruebas médicas exigen consentimiento informado, respeto a la dignidad y no pueden aplicarse indiscriminadamente (LO 1/1996 art. 12.4).
- Horquilla: es menor si la edad más baja es inferior a dieciocho (art. 166.4).
- Impugnación: el decreto de la Fiscalía no tiene recurso directo; se impugna indirectamente mediante la **oposición a la resolución administrativa de protección** que se base en él (cese o denegación de la tutela), ante los tribunales civiles, sin reclamación previa y en el plazo de **dos meses desde su notificación** (LEC art. 780.1), de fecha a fecha (LEC art. 133.3). Procedimiento preferente; competencia del Tribunal de Instancia del domicilio de la entidad pública (LEC art. 779) y, dentro de él, de la **Sección de Familia, Infancia y Capacidad**, que tiene jurisdicción exclusiva en la protección del menor, incluidos los procedimientos de los arts. 779 y 780 LEC (LOPJ art. 86.5.h); donde no exista, la Sección Civil o la Sección Única que asuma esos asuntos (LOPJ art. 86.3 y 86.4). Escrito inicial sucinto con la pretensión, la resolución impugnada, la fecha de notificación y otros procedimientos del menor; después, demanda en diez días desde el emplazamiento (LEC art. 780.2 y 780.4).
- Representación: abogado **y procurador** (LEC art. 750.1); si el joven no tiene asistencia jurídica gratuita reconocida, avísalo al abogado para que la tramite. Sin representantes legales en España, el menor actúa por el defensor que él mismo designe (LEC art. 780.1, párrafo tercero).
- Si la resolución lo ha dejado fuera de todo recurso de protección, pide en otrosí su **reingreso como medida cautelar** mientras dura el proceso: el art. 158.6.º CC permite adoptar, en cualquier proceso judicial, las disposiciones oportunas para apartar al menor de un peligro, y el art. 726.2 LEC admite órdenes de contenido similar a lo que se pretende.
- Contingencia migratoria extraordinaria declarada: la determinación de la edad se practica en la comunidad de destino (LOEX art. 35 quáter.5).

**Bloque 5. Repatriación (LOEX art. 35.5-6; arts. 167 a 171).** Competencia de la Delegación o Subdelegación del domicilio del menor; informe previo de la representación diplomática sobre la familia, o compromiso escrito de los servicios de protección del país (art. 167). Incoación solo si el interés superior se satisface con la reagrupación familiar o la puesta a disposición de esos servicios; notificación inmediata al menor, al fiscal y a la entidad, con información escrita en lengua comprensible (art. 168). **Diez días** de alegaciones y prueba desde la notificación; el menor de dieciséis o más actúa por sí o por representante; si un menor de dieciséis con juicio suficiente (se presume desde los doce años) discrepa de su tutor, se suspende hasta nombrar defensor judicial; informe de protección de menores en diez días; prueba de diez a treinta días (art. 169). Audiencia con presencia del menor con juicio suficiente; resolución según el interés superior, que **pone fin a la vía administrativa**; plazo máximo de seis meses desde el acuerdo de inicio (art. 170). Si el menor está incurso en un proceso judicial, la ejecución exige autorización judicial (art. 171.2). En el contencioso, legitimación propia desde los dieciséis (LOEX art. 35.6) y, si se piden cautelarísimas, audiencia previa al fiscal (LJCA art. 135.2).

**Bloque 6. Residencia del tutelado (LOEX art. 35.7; art. 172).** Su residencia es regular a todos los efectos mientras está tutelado. La oficina de la provincia del domicilio inicia el procedimiento de oficio, por orden superior o a instancia de parte, acreditada la imposibilidad de repatriación y, en todo caso, a los **noventa días** de la puesta a disposición de protección de menores. Documentos: pasaporte o cédula de inscripción (art. 210.5 exime del acta notarial con informe de la entidad), competencia de quien actúa por la entidad y título de tutela o guarda. Resolución en un mes (la redacción vigente, del Real Decreto 316/2026, suprimió el silencio desestimatorio). Efectos retroactivos a la puesta a disposición; habilita a trabajar desde los dieciséis en actividades que favorezcan su integración, sin situación nacional de empleo; dos años; renovación de oficio o a instancia en los dos meses previos, por tres años. La concesión no impide una repatriación posterior en interés del menor (art. 172.3).

**Bloque 7. Mayoría de edad.**
- **Con autorización (art. 173):** renovación en los dos meses previos al vencimiento o en los tres posteriores. Requisitos: medios superiores a la renta garantizada individual del ingreso mínimo vital, o sostenimiento asegurado en un programa de una institución (computan empleo, sistema social y otras cuantías; vale un contrato del art. 127.b); valoración de antecedentes con indultos, suspensiones y cumplimiento (LOEX art. 31.7); informes de la entidad de protección y de otras entidades. Dos años renovables. Jurisprudenciator no devuelve la cuantía de la renta garantizada: pide al abogado la cifra oficial vigente.
- **Sin autorización (art. 174):** extutelado que cumplía los requisitos del art. 172 (salvo tutela por medida cautelar), con participación en acciones formativas certificada o integración acreditada. Solicitud en los **dos meses previos o en los tres posteriores** a cumplir dieciocho; excepcionalmente, hasta el día siguiente a cumplir veinte, por causas ajenas acreditadas y con informe autonómico o municipal. Medios como en el art. 173; **carecer** de antecedentes penales en España o en países anteriores y no ser rechazable; permanencia en España hasta la solicitud con informe de integración. Dos años renovables.
- **Procedimiento del art. 174:** es una autorización por circunstancias excepcionales, así que se rige por el art. 130: solicitud personal del joven, **copia completa** del pasaporte en vigor o cédula de inscripción (hay sentencias que deniegan por aportar una copia incompleta) y subsanación en el plazo que se señale, nunca superior a quince días (art. 130.3). El certificado de antecedentes del país de origen del art. 130.2 se refiere al arraigo y a los arts. 128.3 y 129.2; para el art. 174 rige su propio apartado 3.b: si el certificado extranjero está pendiente, dilo y pide el requerimiento del art. 130.3. El informe de integración debe cubrir la permanencia «hasta el momento de la solicitud» (art. 174.3.c): si es anterior al cese de la tutela, pide uno actualizado.
- **Último día en sábado, domingo o festivo:** recomienda presentar el día hábil anterior; no des por hecho que la ventana del reglamento se prorroga.

**Causas típicas de denegación o inadmisión**

| Causa | Respuesta |
|---|---|
| Solicitud del menor tutelado presentada por un abogado sin título de la entidad | Hacerla presentar a la entidad o pedir el inicio de oficio (art. 172.1) |
| Pasaporte descartado sin motivación y pruebas médicas | Juicio de proporcionalidad del art. 12.4 LO 1/1996 y doctrina civil del Supremo |
| Ausencias del nacido en España | Residencia efectiva habitual y ausencias justificadas (fallo del Supremo y auto de rectificación) |
| Hijo casado, o tutela constituida en el extranjero | Incisos anulados de los arts. 159.1 y 160 |
| Solicitud fuera del plazo del art. 174 | Causa ajena acreditada e informe hasta los veinte años |
| Medios insuficientes al cumplir dieciocho | Programa de una institución, contrato o suma de ingresos (arts. 173.2.a y 174.3.a) |

## Huecos normativos

- El art. 35 bis LOEX remite a su disposición adicional undécima para la capacidad ordinaria que determina la contingencia migratoria; el conector no devuelve disposiciones adicionales. Si el caso depende de ella (traslado entre comunidades autónomas), detén la tarea y explica qué precepto falta.
- Plazos generales de resolución, silencio y recursos del Reglamento están en disposiciones adicionales no devueltas; usa los que traen los propios artículos (159.4, 160.5, 161.4, 170.3, 172.2) y, para recurrir, el pie de recursos de la resolución (LPAC art. 40.2, léelo).
- El Protocolo Marco de menores no acompañados (art. 166.2) no está en el conector: no cites su contenido.

## Estrategia y jurisprudencia

1. Edad: ataca primero el juicio de proporcionalidad sobre el documento y la falta de consentimiento o de garantías de las pruebas; presenta el escrito inicial del art. 780 LEC dentro de los dos meses aunque falten documentos.
2. Repatriación: exige el informe consular sobre la familia y la prueba de que el retorno satisface el interés superior; pide prueba y audiencia; valora protección internacional y trata.
3. Mayoría de edad: calcula las ventanas de solicitud desde la fecha de nacimiento que figure en el decreto o en el pasaporte y avisa de la fecha límite.
4. Consultas (dos a cuatro palabras clave; reformula como máximo dos veces):
   - Edad y documentación: `buscar_sentencias` (`consulta="determinación edad menor pasaporte"`, `base="TS"`, `jurisdiccion="CIVIL"`, `anios=8`); tutela judicial frente al decreto: `consulta="determinación de la edad menor extranjero no acompañado"`, `base="TC"`.
   - Repatriación: `consulta="repatriación menor no acompañado interés superior"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`.
   - Residencia del tutelado: `consulta="menor no acompañado autorización residencia tutela"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="20/05/2025"`.
   - Mayoría de edad: `consulta="mayoría de edad extutelado autorización residencia"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`; antecedentes: añade «antecedentes ponderación».
   - Hijos de residentes: `consulta="residencia menor nacido en España progenitor residente"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`.
5. Antes de citar una sentencia, comprueba en su texto qué reglamento aplicó: muchas, también de 2026, aplican el Real Decreto 557/2011 (menor no acompañado en torno a sus arts. 196 a 198, con nueve meses en lugar de noventa días para la residencia). Cítala solo donde el requisito se mantiene y di el precepto vigente equivalente.
6. Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y transcribe fundamentos, nunca los hechos ni la identidad de otros menores.

## Documento que se entrega

Un Word maquetado según `references/formato-y-organos.md`. Nunca incluyas en el texto datos del menor que no sean necesarios.

- **A. Solicitud de autorización de residencia** (bloques 1, 2, 6 o 7) ante la Oficina de Extranjería de la Delegación o Subdelegación del Gobierno en `[PROVINCIA]` (art. 193.2). Nombre: `solicitud-residencia-menor-<apellido-cliente>-<AAAAMMDD>.docx`. Estructura: comparecencia de quien representa al menor con su título; HECHOS (identidad, filiación o tutela, fechas clave del bloque, requisitos con su documento); FUNDAMENTOS (precepto del bloque, incisos anulados si influyen, doctrina con párrafo literal y ECLI cuando haya una aplicable al requisito que pueda discutirse); SOLICITA; OTROSÍ solo si procede (tramitación simultánea cuando el progenitor tenga su autorización en trámite, arts. 130.7 y 160.1; aportación posterior de un documento pendiente); relación de documentos. En la solicitud la jurisprudencia **no es imprescindible**: si las consultas (con sus dos reformulaciones) solo devuelven sentencias desfavorables o dictadas con el Real Decreto 557/2011 en un punto que ha cambiado, no detengas la tarea: redacta sin citarlas y explica en el resumen qué se buscó y qué riesgos revelan. En los documentos B y C sí es imprescindible.
- **B. Escrito de alegaciones en el procedimiento de repatriación** (art. 169) ante la Delegación o Subdelegación instructora, dentro de los diez días. Nombre: `alegaciones-repatriacion-<apellido-cliente>-<AAAAMMDD>.docx`. Estructura: comparecencia (el menor de dieciséis o más por sí o por representante; si hay conflicto con el tutor, petición de defensor judicial); ALEGACIONES numeradas (interés superior, informe consular insuficiente, situación familiar real, arraigo en España, riesgos de retorno, protección internacional o trata); PROPOSICIÓN DE PRUEBA (art. 169.3); SOLICITA que se acuerde la permanencia en España y se inicie la autorización del art. 172; OTROSÍ de intérprete y de audiencia del menor (art. 170.1).
- **C. Oposición a la resolución de protección basada en el decreto de determinación de edad** (LEC art. 780), ante el Tribunal de Instancia del domicilio de la entidad pública, **Sección de Familia, Infancia y Capacidad** (LOPJ art. 86.5.h; si no existe, la sección que asuma esos asuntos según el art. 86.3 y 86.4). Nombre: `oposicion-determinacion-edad-<apellido-cliente>-<AAAAMMDD>.docx`. Comparecencia por procurador con dirección de abogado (LEC art. 750.1) y, si el menor no tiene representantes legales, con el defensor que él designe (LEC art. 780.1). Escrito inicial: pretensión (que se declare la minoría de edad y se restablezca la protección), resolución a la que se opone y **fecha de notificación**, decreto de la Fiscalía en que se basa (con la doctrina que abre la impugnación indirecta), procedimientos relativos al menor, competencia y legitimación; SUPLICO que se tenga por formulada la oposición y que el letrado o letrada de la Administración de Justicia reclame el expediente (LEC art. 780.3); OTROSÍES: medida cautelar de reingreso si está fuera de la protección (CC art. 158; LEC art. 726.2), intérprete y audiencia del menor (LEC art. 780.1). Añade, como anexo para el abogado, el guion de la futura demanda: documentación oficial no invalidada, falta de juicio de proporcionalidad, garantías de las pruebas médicas, doctrina civil del Supremo y del Constitucional con párrafo literal y ECLI, prueba propuesta. SUPLICO («SUPLICO» ante el órgano judicial).

Cita el Reglamento siempre como «artículo N del Real Decreto 1155/2024» y la LOEX como «artículo N de la Ley Orgánica 4/2000» (formato, apartado 4); nunca «del Reglamento de Extranjería» ni «del Reglamento aprobado por el Real Decreto…», que `verificar_escrito` no identifica. En el documento C, además: la LOPJ como «letra h) del artículo 86.5 de la Ley Orgánica del Poder Judicial» (con «Ley Orgánica 6/1985» o con «86.5.h)» el verificador no identifica la ley o se la atribuye a la LEC), y cada artículo de la LEC con su nombre completo, nunca «de la misma ley» ni «párrafos … del artículo 780.1» entre el número y la ley.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos del bloque (LOEX 35 y los del Reglamento), LO 1/1996 art. 12, LEC 779, 780 y 750 y LOPJ 86 en el bloque 4 (y CC 158 y LEC 726 si se pide el reingreso), LJCA en el 5, art. 130 en el bloque 7 sin autorización; y leído el fallo `BOE-A-2026-19632` si el artículo trae nota de nulidad.
- [ ] Representación comprobada: quién presenta y con qué título.
- [ ] Plazos con fecha y precepto: seis meses (art. 159.1), diez días (art. 169.1), dos meses (LEC art. 780.1), noventa días (art. 172.1), ventanas de los arts. 173.1 y 174.2; si falta la fecha de notificación o de nacimiento, pedida y sin plazo inventado.
- [ ] Ningún contenido tomado de disposiciones adicionales ni del Protocolo Marco.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el texto completo. Si marca un artículo del Reglamento como no localizado o lo atribuye a la LOEX, compruébalo con `buscar_articulo` (`ley="BOE-A-2024-24099"`) y reescribe la cita como «artículo N del Real Decreto 1155/2024».
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[DOMICILIO]`, `[NÚMERO DE EXPEDIENTE]`, fecha de nacimiento) en lugar de datos inventados; cuantía de la renta garantizada confirmada por el abogado.
- [ ] Sin importes de tasa ni códigos de modelo.
- [ ] Resumen para el abogado según el apartado 7 del formato: órgano; plazo y fecha límite con su precepto; riesgos (mayoría de edad inminente, ejecución de la repatriación, representación); tabla de jurisprudencia; próximo paso.
