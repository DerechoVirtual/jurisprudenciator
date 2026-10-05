---
name: victimas-trata
description: >-
  Prepara en Word los escritos de protección de la persona extranjera víctima de trata de seres humanos
  (art. 59 bis LOEX; arts. 148 a 155 del Real Decreto 1155/2024): comunicación de indicios y petición de
  identificación, propuesta del periodo de restablecimiento y reflexión de al menos noventa días,
  suspensión del sancionador, de la expulsión o de la devolución y salida del CIE, exención de
  responsabilidad, autorización de residencia y trabajo provisional y definitiva, retorno asistido, hijos
  y víctimas menores. Úsala con «trata», «la obligaban a prostituirse», «tiene una deuda con la red»,
  «trabajo forzado», «la trajeron engañada», «está en el CIE y es víctima». Si colabora contra una red sin
  ser víctima de trata, usa razones-humanitarias; si pide asilo, proteccion-internacional-apatridia; si es
  menor no acompañada, también menores-extranjeros.
---

# Víctimas de trata de seres humanos

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen legal de la víctima** → `buscar_articulo` (`ley="LOEX"`, artículos `"59 bis"` y `"59"`).
- **Identificación, periodo de restablecimiento y reflexión, exención, autorización, retorno, menores y reagrupación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"148"` a `"155"`, uno por llamada).
- **Suspensión de la devolución y efectos sobre otros procedimientos** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"23"`, `"165"` y `"191"`).
- **Tipo penal y exención de pena por delitos cometidos bajo la explotación** → `buscar_articulo` (`ley="CP"`, `articulo="177 bis"`); **derecho de la Unión** → `buscar_articulo` (`ley="Directiva 2011/36/UE"`, `articulo="11"`).
- **Recursos contra la denegación o revocación del periodo** → `buscar_articulo` (`ley="LPAC"`, artículos `"40"`, `"112"`, `"121"`, `"122"`, `"123"` y `"124"`) y (`ley="LJCA"`, artículos `"8"`, `"11"` y `"46"`).
- **Doctrina** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"` para TSJ, juzgados y Audiencia Nacional, `base="TS"` para el Supremo, `base="TJUE"` para el Tribunal de Justicia; fechas en formato `dd/mm/aaaa`) + `leer_sentencias` (`parrafos=3`).
- **Revisión del documento** → cada redactor del equipo pasa `verificar_escrito` solo sobre sus frases con normas, y el ensamblado rechaza cualquier ECLI o ROJ que ningún redactor leyera; `buscar_por_cita` se usa solo con un ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

## Cuándo usarla

- Persona extranjera en situación irregular sobre la que hay **motivos razonables** para creer que es víctima de trata: captación, traslado o acogida mediante violencia, engaño, abuso de vulnerabilidad o pagos, con fines de explotación laboral, sexual, mendicidad, actividades delictivas, extracción de órganos o matrimonio forzado (CP art. 177 bis.1, léelo).
- En cualquier fase: antes de que la policía la identifique, durante el periodo de restablecimiento y reflexión, al pedir la exención y la autorización, o frente a una denegación.

**Urgencia.** Si está en un CIE, detenida para devolución o con expulsión a punto de ejecutarse, prepara primero el escrito A (ver «Documento»): durante la identificación quedan suspendidos el sancionador, la expulsión y la devolución (art. 149.2), la devolución no se ejecuta si se pone de manifiesto que es víctima de trata (art. 23.6.c), y con víctima en CIE el Delegado o Subdelegado resuelve la propuesta en veinticuatro horas (art. 150.3). Coordina con `internamiento-cie`.

Detector:

| Situación | Figura y skill |
|---|---|
| Colabora contra una red de tráfico, inmigración ilegal o explotación laboral sin indicios de trata | LOEX art. 59; arts. 142 a 147 → `razones-humanitarias` |
| Reagrupada, víctima de trata por el propio reagrupante | residencia independiente (art. 69.2.b) → `reagrupacion-familiar` |
| Teme persecución en su país (incluido el riesgo de volver a ser captada) | → `proteccion-internacional-apatridia`; es compatible (art. 152.8) |
| Violencia sexual sin red ni explotación | → `victimas-violencia-genero-sexual` |
| Menor no acompañada | esta skill y `menores-extranjeros` (arts. 154 y 165) |

## Protección de la víctima

- La información para la identificación tiene carácter reservado (art. 149.2). En los escritos, lo imprescindible: indicios, no relatos completos; nunca el domicilio de acogida ni datos que permitan localizarla. Notificaciones en el despacho o en la entidad especializada que la acompañe, si lo autoriza.
- La decisión de colaborar con la investigación es suya y no condiciona el periodo de reflexión ni la exención por situación personal (arts. 150.1 y 151.1). La asistencia no se supedita a su colaboración (Directiva 2011/36/UE, art. 11.3).
- Pide su conformidad expresa antes de solicitar la propuesta del periodo (art. 150.1) y antes de comunicar indicios a la policía.
- Documentos: se puede eximir de aportar los que supongan un riesgo obtener (LOEX art. 59 bis.4; art. 152.2). No le pidas contactar con su consulado sin valorar el riesgo.
- En las búsquedas, nunca uses nombres, alias, lugares de explotación ni números de procedimiento.

## Datos que hay que reunir antes de redactar

Saca estos datos de la documentación aportada (paso 2 de `redaccion-rapida`). Si falta un dato imprescindible (★), pídelos todos a la vez en una única ronda; en urgencia, redacta el escrito A con marcadores y pide el resto después.

1. ★ Dónde está ahora (CIE, comisaría, centro de acogida, libertad) y si hay expediente sancionador, orden de expulsión o de devolución: número, fecha, órgano y estado.
2. ★ Indicios de trata que el abogado pueda sostener (acción, medio y finalidad del art. 177 bis CP) y quién más los ha detectado (entidad especializada, Inspección de Trabajo, servicios sociales, sanitarios).
3. ★ Si ya hubo identificación por unidad policial especializada, propuesta o resolución sobre el periodo (fechas, duración, sentido).
4. ★ Si quiere colaborar con la investigación o el proceso penal, o si la exención se pedirá por su situación personal.
5. ★ Hijos menores, tutelados, mayores con discapacidad o que no puedan proveer a sus necesidades, y ascendientes en primer grado: si estaban en España al identificarla (art. 152.1) o están fuera (art. 155).
6. ★ Edad: si hay duda sobre si es menor, trátala como posible menor y aplica el art. 154 y `menores-extranjeros`.
7. Documentación de identidad disponible y riesgo de obtenerla.
8. Si desea retorno asistido (art. 153) o protección internacional.
9. Representación (art. 197.4) y conformidad de la víctima con cada paso.

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**Identificación (LOEX art. 59 bis.1-2; art. 149)**

- Cualquiera que tenga noticia de una posible víctima informa a la autoridad policial competente, a la Delegación o Subdelegación del Gobierno o a la Inspección de Trabajo, que activan el procedimiento sin dilación (art. 149.1). Se puede iniciar a instancia de parte.
- Con motivos razonables, la policía informa por escrito, en idioma comprensible y con intérprete, de sus derechos y de la posible derivación a servicios sociales y sanitarios; si hay explotación sexual, también de los derechos de la LO 10/2022 (art. 149.1).
- Identifican unidades policiales con formación específica, con entrevista en condiciones adecuadas, sin personas del entorno de los explotadores y, si es posible, con apoyo jurídico y psicológico; las entidades especializadas pueden aportar información (art. 149.2).
- Durante la identificación quedan suspendidos el sancionador y la expulsión o devolución (art. 149.2; LOEX art. 59 bis.2).

**Periodo de restablecimiento y reflexión (LOEX art. 59 bis.2-3; art. 150)**

- La unidad de extranjería eleva la propuesta en cuarenta y ocho horas, previa conformidad de la víctima, a la Delegación o Subdelegación de la provincia de identificación; si identificó otra unidad policial, esta remite informe motivado a la unidad de extranjería (art. 150.1-2).
- Duración de **al menos noventa días** y suficiente para restablecerse y decidir si coopera (LOEX art. 59 bis.2; art. 150.1).
- El Delegado o Subdelegado resuelve en **cinco días**; transcurridos sin resolución, **se entiende concedido** por la duración propuesta; si la víctima está en un CIE, **veinticuatro horas** (art. 150.3). Los plazos se cuentan desde la recepción de la propuesta.
- La resolución favorable suspende el sancionador o la expulsión o devolución por la infracción del art. 53.1.a), autoriza la estancia y supone la propuesta al juez de su puesta en libertad si está en un CIE (art. 150.5-6). Seguridad y subsistencia a cargo de las administraciones; al final, evaluación para una posible ampliación (LOEX art. 59 bis.2).
- Denegación o revocación solo por orden público o invocación indebida, motivada y recurrible (LOEX art. 59 bis.3). Ese precepto remite a la Ley 30/1992, derogada: aplica la LPAC y determina el recurso con el pie de recursos de la resolución (LPAC art. 40.2). El Reglamento regula los recursos en una disposición adicional que el conector no devuelve: si el pie de recursos falta o es contradictorio, detén la redacción del recurso y explícalo al abogado.

**Exención de responsabilidad (LOEX art. 59 bis.4; art. 151)**

- La propone la autoridad con la que colabora o la determina **de oficio** el Delegado o Subdelegado en atención a la situación personal de la víctima; se refiere a la infracción del art. 53.1.a) LOEX.
- Si no se declara, se levanta la suspensión; pero el sancionador queda condicionado si la víctima pide otra autorización por circunstancias excepcionales por un supuesto distinto (art. 151.2-3).

**Autorización de residencia y trabajo (LOEX art. 59 bis.4; art. 152)**

- Declarada la exención, se informa a la víctima de que puede pedirla: a la Secretaría de Estado de Seguridad si la base es la colaboración, o a la de Migraciones si es la situación personal; si concurren ambas, puede iniciar los dos procedimientos (art. 152.1).
- Se presenta ante la Delegación o Subdelegación que declaró la exención, personalmente o por representante, con pasaporte o título de viaje en vigor o cédula de inscripción, salvo exención de documentos de riesgo (art. 152.2).
- Con informe favorable, autorización **provisional** de residencia y trabajo sin nueva solicitud, eficaz desde la notificación de su concesión; tarjeta en un mes desde la concesión, renovable anualmente, sin mención de su condición (art. 152.4).
- Definitiva de **cinco años**, con cómputo de la provisional para larga duración (art. 152.5). La denegación extingue la provisional, que no computa (art. 152.6), sin impedir otra solicitud por supuesto distinto (art. 152.7).
- Extensión a hijos menores o tutelados, mayores con discapacidad o sin capacidad de proveer por su salud, y ascendientes en primer grado (estos, por razones humanitarias), si estaban en España al identificarla (art. 152.1).
- No afecta al derecho a pedir protección internacional (art. 152.8). Desde estas autorizaciones no cabe la modificación del art. 191 (art. 191.7.b).

**Retorno asistido (art. 153).** Puede pedirse desde que hay motivos razonables, dirigido a la Secretaría de Estado de Migraciones ante cualquiera de las autoridades del procedimiento; incluye evaluación previa de riesgos, transporte y asistencia en origen, tránsito y destino; se aplaza si su permanencia es necesaria para la investigación.

**Menores (LOEX art. 59 bis.5; art. 154).** Interés superior del menor, derivación a recursos específicos a propuesta de la entidad tutelar o del fiscal, separación entre menores y adultos.

**Reagrupación de hijos que no estén en España (art. 155)**, sin exigir medios, residencia previa ni vivienda. Solo hijos (menores, tutelados, o mayores con discapacidad o sin capacidad de proveer por su salud) que no estuvieran en España al declararse la exención; el cónyuge no está incluido y va por el régimen general (`reagrupacion-familiar`).

**Ámbito penal.** La víctima queda exenta de pena por las infracciones cometidas en la situación de explotación cuando sean consecuencia directa de ella y proporcionadas (CP art. 177 bis.11). Si tiene causa penal abierta, avisa al abogado para que lo haga valer en esa jurisdicción.

**Huecos normativos.** El Reglamento dedica una disposición adicional a la identificación y protección de la víctima de trata, y el art. 148 remite a un protocolo marco; ninguno de los dos lo devuelve el conector. No cites su contenido. Si el caso depende de ellos, detén la tarea y explica al abogado qué texto falta. La Directiva 2011/36/UE fue modificada en 2024: antes de invocar sus apartados nuevos, comprueba con `buscar_boe` (`consulta="trata de seres humanos"`) si España los ha transpuesto.

## Estrategia y jurisprudencia

1. El objetivo inmediato es la suspensión y la protección: comunica indicios por escrito y deja constancia de la fecha y hora de entrada, que abre la fase de identificación a instancia de parte (art. 149.1). Los plazos no corren desde tu escrito: las cuarenta y ocho horas de la propuesta cuentan desde la **identificación** por la unidad de extranjería (art. 150.1), y los cinco días (o veinticuatro horas en CIE) de la resolución, desde la **recepción de la propuesta** en la Delegación o Subdelegación (art. 150.3). Dile al abogado que pida esas dos fechas: sin ellas no sabrá cuándo opera el silencio positivo.
2. Apoya los indicios en informes de entidades especializadas (art. 149.2) y en indicadores objetivos (deuda, retención de documentos, control de movimientos, captación con engaño).
3. Pide la exención por situación personal cuando la víctima no quiera o no pueda colaborar; si colabora, pide a la autoridad que emita su informe y que formalice ante el Delegado la propuesta de exención (art. 151.1). Si el periodo ya terminó y nadie ha propuesto ni declarado la exención, el escrito B pide primero al Delegado o Subdelegado que recabe esa propuesta y declare la exención (y, si procede, también de oficio por la situación personal: con doble fundamento se abren los dos procedimientos, arts. 152.1 y 152.3). La exención es discrecional («podrá»): la doctrina localizada (TSJ de Canarias, 2016, con el Reglamento de 2011) la trata como una facultad y no como un derecho, así que refuerza el expediente con informes.
4. Consultas (dos a cuatro palabras clave; el buscador mezcla resultados ajenos con frases largas; reformula como máximo dos veces):
   - Periodo, exención y autorización: `buscar_sentencias` (`consulta="trata seres humanos 59 bis"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `anios=12`).
   - Suspensión de la expulsión: `consulta="víctima trata expulsión"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`.
   - Asilo e indicios de trata: `consulta="víctima de trata asilo"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`, `anios=12`.
   - Derecho de la Unión: `consulta="víctima de trata"`, `base="TJUE"`.
   La base tiene poca doctrina específica de trata en vía administrativa: para los escritos A y B la jurisprudencia no es imprescindible y, si no aparece nada aplicable tras dos reformulaciones, redacta con los preceptos leídos y díselo al abogado; para el recurso C sí lo es. No leas una sentencia solo porque su resumen diga «restablecimiento y reflexión»: las de 2014-2016 suelen limitarse a transcribir el art. 59 bis y el art. 142 del Reglamento de 2011 y a relatar hechos.
5. Descarta los resultados que no traten de trata (el buscador devuelve ruido); lee con `leer_sentencias` (`parrafos=3`, `terminos="trata"`) solo lo que vayas a citar y transcribe fundamentos, nunca hechos.
6. Antes de citar una sentencia, comprueba en su texto qué reglamento aplicó. Doctrina dictada con el Real Decreto 557/2011: su periodo mínimo era distinto; cita la doctrina solo en lo que no depende de la duración y usa siempre los noventa días vigentes.
7. Contencioso: las resoluciones de las Secretarías de Estado se impugnan ante la Sala de la Audiencia Nacional (LJCA art. 11.1.a) y las de la Delegación o Subdelegación ante la Sección de lo Contencioso-Administrativo del Tribunal de Instancia (LJCA art. 8.4; formato, apartado 3). Comprueba ambos artículos antes de encabezar; prepara el recurso con `recurso-contencioso-extranjeria`.

## Documento que se entrega

Uno o varios Word maquetados según `references/formato-y-organos.md`, con la marca «CONFIDENCIAL — INFORMACIÓN RESERVADA (art. 149.2)»:

- **A. Comunicación de indicios de trata y solicitud de identificación, de propuesta del periodo de restablecimiento y reflexión y de suspensión** — a la unidad policial de extranjería competente, con copia a la Delegación o Subdelegación del Gobierno (art. 149.1) y, si hay expediente, al instructor. Nombre: `comunicacion-trata-<apellido-cliente>-<AAAAMMDD>.docx`.
- **B. Solicitud de exención de responsabilidad y de autorización de residencia y trabajo por circunstancias excepcionales** — ante la Delegación o Subdelegación, dirigida a la Secretaría de Estado que corresponda (arts. 151 y 152). Nombre: `solicitud-autorizacion-trata-<apellido-cliente>-<AAAAMMDD>.docx`.
- **C. Recurso contra la denegación o revocación del periodo** — con el recurso que indique el pie de recursos (LPAC art. 40.2); si no lo indica, ver «Huecos normativos». Nombre: `recurso-periodo-reflexion-<apellido-cliente>-<AAAAMMDD>.docx`.

Estructura de A:

1. Encabezamiento al órgano policial y a la Delegación o Subdelegación de `[PROVINCIA]`.
2. Comparecencia del abogado en nombre de `[NOMBRE Y APELLIDOS]` (o identificación mínima si aún no la hay), con su conformidad expresa.
3. HECHOS: situación actual (CIE, detención, expediente `[NÚMERO DE EXPEDIENTE]`); indicios de trata ordenados por acción, medio y finalidad, sin detalles que la pongan en riesgo; informes de entidades que se acompañan.
4. FUNDAMENTOS: deber de identificación y motivos razonables (LOEX art. 59 bis.1-2; art. 149); suspensión durante la identificación (art. 149.2) y de la devolución (art. 23.6.c); plazos de la propuesta y de la resolución, silencio positivo y plazo de veinticuatro horas si está en CIE (art. 150); libertad del CIE (art. 150.5); asistencia no condicionada (Directiva 2011/36/UE, art. 11.3); doctrina con párrafo literal y ECLI, si se ha leído.
5. SOLICITA: identificación inmediata por unidad especializada; propuesta favorable de un periodo de al menos noventa días; suspensión del sancionador, de la expulsión o de la devolución; si está en CIE, propuesta al juez de su puesta en libertad; derivación a recursos de asistencia.
6. OTROSÍ: intérprete; entrevista sin presencia de personas del entorno de los explotadores; reserva de la información.
7. Lugar, fecha, firma y relación de documentos.

Estructura de B: encabezamiento a la Delegación o Subdelegación que declaró o debe declarar la exención y, por su conducto, a la Secretaría de Estado de Seguridad o de Migraciones (si la exención aún no está declarada, el primer pedimento es que la declare: ver «Estrategia», punto 3); hechos (periodo concedido, colaboración o situación personal, familiares en España); fundamentos (LOEX art. 59 bis.4; arts. 151 y 152; exención de documentos de riesgo; extensión a familiares; compatibilidad con el asilo); solicita exención, autorización provisional y definitiva de cinco años y las de los familiares; otrosí de reagrupación de hijos que estén fuera (art. 155) o de retorno asistido si lo elige (art. 153); documentos.

**Reparto para la redacción rápida:** los escritos A y B son breves y reservados: el director los redacta sin equipo, empezando por A por su urgencia; si B pasa de cuatro páginas, 01 encabezamiento y hechos, 02 fundamentos y solicitud con otrosíes. El recurso C: encabezamiento y hechos, una sección por motivo y cierre.

Cita el Reglamento siempre como «artículo N del Real Decreto 1155/2024» y la LOEX como «artículo N de la Ley Orgánica 4/2000» (formato, apartado 4); nunca «del Reglamento de Extranjería» ni «del Reglamento aprobado por el Real Decreto…», que `verificar_escrito` no identifica. `verificar_escrito` atribuye a la norma citada antes los artículos con «bis» y apartado («artículo 59 bis.2», «artículo 177 bis.1») o con letra («23.6.c)»): escribe «apartado 2 del artículo 59 bis de la Ley Orgánica 4/2000», «apartado 1 del artículo 177 bis del Código Penal», «artículo 23.6 del Real Decreto 1155/2024». Tampoco reconoce la Directiva 2011/36/UE: su artículo 11 sale como «posible disonancia» o como artículo de otra norma. Si `buscar_articulo` (`ley="Directiva 2011/36/UE"`) lo devolvió, la cita es correcta: dilo en el resumen como falso aviso.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: LOEX 59 bis (y 59); Reglamento 148 a 155, 23 y 191; CP 177 bis; Directiva 2011/36/UE art. 11; LPAC y LJCA si hay recurso.
- [ ] Conformidad de la víctima registrada para cada escrito; información reservada; sin domicilio de acogida ni datos que la expongan.
- [ ] Plazos con fecha y precepto: presentación del escrito A (hora), 48 horas desde la identificación (art. 150.1), cinco días o 24 horas desde la recepción de la propuesta (art. 150.3), noventa días (art. 150.1), tarjeta en un mes desde la concesión (art. 152.4); recurso con el plazo del pie de recursos y su artículo de la LPAC.
- [ ] Ningún contenido del protocolo marco ni de disposiciones adicionales no devueltas.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre sus frases con normas. Si marca un artículo del Reglamento como no localizado o lo atribuye a la LOEX, compruébalo con `buscar_articulo` (`ley="BOE-A-2024-24099"`) y reescribe la cita como «artículo N del Real Decreto 1155/2024».
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[NÚMERO DE EXPEDIENTE]`) en lugar de datos inventados.
- [ ] Resumen para el abogado según el apartado 7 del formato: órganos; plazos y fechas límite con su precepto; riesgos (CIE, devolución inminente, documentos); tabla de jurisprudencia; próximo paso (seguimiento del silencio positivo a los cinco días, solicitud de exención, asilo si procede).
