---
name: visados-denegacion
description: >-
  Analiza la denegación de un visado español (estancia de corta duración, estudios, residencia no
  lucrativa, reagrupación familiar, trabajo, familiares de españoles, búsqueda de empleo) y redacta en
  Word el recurso de reposición ante la oficina consular y el recurso contencioso-administrativo.
  Comprueba la causa de denegación, la motivación exigible (LOEX art. 27.6 y Reglamento art. 28.6), el
  «riesgo migratorio», la entrevista y su acta, los plazos y el órgano judicial competente. Úsala
  cuando el abogado diga «me han denegado el visado», «el consulado deniega», «visado Schengen
  denegado», «riesgo migratorio», «no acredita intención de regresar», «visado de reagrupación
  denegado», «visado de estudiante denegado» o «recurrir visado». Si lo denegado es la autorización
  previa de residencia, usa la skill de esa autorización.
---

# Denegación de visados: recurso de reposición y recurso contencioso

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Clase de visado, procedimiento, causas de denegación, motivación y notificación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"25"` a `"28"` y el del tipo de visado: `"29"` a `"33"` corta duración y tránsito, `"34"` a `"36"` estudios, `"37"` a `"41"` residencia, `"42"` extraordinario, `"43"` a `"45"` búsqueda de empleo, `"46"` retirada y anulación).
- **Base legal y alcance del deber de motivar** → `buscar_articulo` (`ley="LOEX"`, artículos `"20"`, `"25"`, `"25 bis"`, `"26"` y `"27"`; `ley="LPAC"`, artículos `"35"` y `"48"`).
- **Visado de corta duración (Código de visados y condiciones de entrada)** → `buscar_articulo` (`ley="Reglamento (CE) 810/2009"`, artículos `"14"`, `"21"`, `"32"` y `"35"`; `ley="Reglamento (UE) 2016/399"`, `articulo="6"`).
- **Recurso de reposición y contencioso: órgano, procedimiento y plazo** → `buscar_articulo` (`ley="LPAC"`, artículos `"30"`, `"123"` y `"124"`; `ley="LJCA"`, artículos `"8"`, `"10"`, `"11"`, `"14"`, `"23"`, `"45"`, `"46"`, `"48"`, `"52"`, `"78"` y `"128"`; `ley="LOPJ"`, `articulo="182"`).
- **Órgano judicial que conoce hoy de las denegaciones consulares** → `buscar_sentencias` (`consulta="denegación visado consulado competencia Tribunal Superior de Justicia de Madrid"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `tipo_resolucion="AUTO"`; con `fecha_desde` del último año puede no devolver nada: si es así, quita el filtro y elige el auto más reciente) y `leer_sentencias` (`parrafos=2`).
- **Doctrina sobre motivación y riesgo migratorio** → `buscar_sentencias` (`consulta="denegación visado motivación riesgo migratorio"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde` de los dos últimos años; con `base="AN"` el conector devuelve también sentencias del TSJ de Madrid (STSJ M), que es el tribunal que hoy resuelve estos recursos; y `base="TJUE"` con `consulta="Código de visados denegación artículo 32"`) y `leer_sentencias` (`parrafos=3`).
- **Visados de reagrupación o de familiares denegados por un requisito que ya valoró Extranjería** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"66"`, `"68"` y `"196"`, este último para «a cargo» y dependencia económica; `ley="LOEX"`, `articulo="17"`) y `buscar_sentencias` (`consulta="alcance potestad misión diplomática oficina consular denegación visado reagrupación familiar"`, `base="TS"`, `fecha_desde="01/07/2025"`), y lee la sentencia del Supremo de 2026 que devuelve.
- **Revisión del documento** → cada redactor del equipo pasa `verificar_escrito` solo sobre sus frases con normas, y el ensamblado rechaza cualquier ECLI o ROJ que ningún redactor leyera; `buscar_por_cita` se usa solo con un ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

## Cuándo usarla

- Estudiar una denegación de visado y decidir entre recurrir en reposición, ir directamente al contencioso o presentar una nueva solicitud mejor documentada.
- Redactar el recurso de reposición ante la oficina consular y el escrito de interposición del recurso contencioso-administrativo (y el esquema de la demanda).
- Pedir copia del expediente y del acta de la entrevista consular.
- Recurrir la retirada o anulación de un visado ya expedido.

Usa otra skill del plugin cuando lo denegado sea la **autorización** de la oficina de extranjería y no el visado, porque su recurso va a otro órgano administrativo y judicial:

- reagrupación → `reagrupacion-familiar`; familiares de españoles → `familiares-de-espanoles`;
- estudios y búsqueda de empleo → `estudiantes-y-busqueda-empleo`; residencia no lucrativa → `residencia-no-lucrativa`;
- trabajo → `trabajo-cuenta-ajena` o `trabajo-cuenta-propia`; Ley 14/2013 → `movilidad-internacional-ley-14-2013`;
- recurso administrativo contra la autorización → `recurso-administrativo-extranjeria`.

Si la oficina consular notifica a la vez la autorización desfavorable y la denegación del visado (`BOE-A-2024-24099`, art. 28.10), trata los dos actos por separado y dilo al abogado. La denegación de entrada en frontera o la devolución no son denegaciones de visado: usa `expulsion-procedimiento-sancionador` o `internamiento-cie`.

## Datos que hay que reunir antes de redactar

Saca estos datos de la documentación aportada, por este orden (paso 2 de `redaccion-rapida`). Si falta un dato imprescindible, pídelos todos a la vez en una única ronda de no más de cuatro preguntas y espera; lo demás queda como `[PENDIENTE: dato]`.

1. **Resolución** (imprescindible): texto íntegro o impreso normalizado, oficina consular que la dicta, fecha de notificación y medio (correo electrónico, teléfono, tablón), pie de recursos.
2. **Clase de visado y finalidad** (imprescindible): corta duración, tránsito, estudios, residencia (no lucrativa, reagrupación, trabajo por cuenta ajena o propia, temporada, familiar de español), búsqueda de empleo.
3. **Autorización previa**: si existía, órgano, fecha de concesión y de notificación, y fecha en que se presentó el visado (para comprobar los plazos de presentación).
4. **Entrevista**: si la hubo, fecha, quién estuvo presente, idioma, si se levantó acta y si se entregó copia.
5. **Documentos aportados** con la solicitud y en cada requerimiento, y los que el consulado dice que faltaban.
6. **Arraigo en el país de residencia** (en corta duración): trabajo, familia, bienes, viajes anteriores con regreso en plazo, visados anteriores.
7. **Situación de la persona en España** que invita o reagrupa: medios, vivienda, vínculo.
8. **Antecedentes**: inclusión en el SIS, prohibiciones de entrada, denegaciones anteriores.
9. **Urgencia**: fecha de inicio del curso, del contrato o del viaje, enfermedad grave de un familiar; condiciona si merece la pena pedir medidas cautelares o presentar una nueva solicitud.

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en el momento y cita el texto vigente del Reglamento aprobado por el Real Decreto 1155/2024 (vigente desde el 20/05/2025); no uses la numeración del Reglamento anterior.

El Tribunal Supremo anuló en julio de 2026 varios preceptos e incisos del Reglamento (fallo publicado en el BOE como `BOE-A-2026-19632`). Cuando `buscar_articulo` devuelva una nota «Téngase en cuenta que se declara la nulidad…», léela: lo anulado no se aplica ni se cita. Si dudas de si un precepto quedó afectado, lee el fallo con `leer_boe` (`identificador="BOE-A-2026-19632"`).

**Clases y régimen aplicable.**
- Clases de visado: tránsito aeroportuario, estancia de corta duración y larga duración (`BOE-A-2024-24099`, art. 25); tipos legales en `LOEX`, art. 25 bis.
- Tránsito y corta duración: régimen, requisitos y causas de denegación del Derecho de la Unión (arts. 29.2 y 30.1 del Reglamento): aplica el Código de visados. Anulación y retirada, también por Derecho de la Unión (art. 33).
- Larga duración: estudios (arts. 34 a 36), residencia (arts. 37 a 41), extraordinario (art. 42), búsqueda de empleo (arts. 43 a 45; sus cupos y requisitos específicos se remiten a una orden ministerial que el conector puede no devolver: si el caso depende de ella, aplica la puerta).
- Reparto de la valoración: la oficina consular valora los requisitos generales del visado de residencia (art. 38) y la oficina de extranjería los específicos de la autorización (arts. 39.2, 39.3, 40.2, 41); en reagrupación, el consulado valora la documentación original de vínculos, edad y dependencia legal (art. 40.2), mientras que la dependencia económica se acredita ante Extranjería (art. 68.3.b). Identifica qué órgano valoró el requisito que falló. **No sostengas que el consulado carece de competencia para revisarlo:** el Tribunal Supremo admitió en 2026 (aplicando el art. 57 del Reglamento anterior, de estructura igual al art. 40.2 actual) que, al resolver el visado, el consulado puede examinar la veracidad de las circunstancias valoradas en la autorización y denegar con la preceptiva motivación. Busca y lee esa sentencia (consulta de la lista) y argumenta dentro de sus límites, que son los que dice su texto: examinar la veracidad de esas circunstancias y motivar la denegación. Si el consulado no pone en duda ningún hecho y se limita a valorar de otra manera los mismos documentos que ya examinó Extranjería, sostén que eso excede lo que admite el Supremo y que, en todo caso, falta la motivación.

**Cuadro por clase de visado** (verificado; relee cada artículo antes de usar una cifra):

| Visado | Artículos | Plazo para presentarlo | Plazo para resolver | Qué valora el consulado |
|---|---|---|---|---|
| Tránsito y corta duración | Reglamento 29 a 33; Código de visados 9, 14, 21, 23 y 32 | Como regla, entre seis meses y quince días naturales antes del viaje (Código, art. 9.1) | Quince días naturales, ampliables a cuarenta y cinco (Código, art. 23) | Todas las condiciones y el riesgo de inmigración ilegal |
| Estudios, movilidad, voluntariado, formación | 34 a 36 | Dos meses antes del inicio, salvo causa justificada | Un mes desde la autorización favorable | Art. 35 salvo la autorización, que valora extranjería en siete días |
| No lucrativa, cuenta propia, excepción de autorización | 37 a 39 | Con la solicitud de autorización | Un mes desde la autorización favorable | Art. 38 y, en no lucrativa, art. 61.2 a) y b) |
| Reagrupación, cuenta ajena, temporada | 37, 38 y 40 | Dos meses (reagrupación) o un mes (trabajo) desde la notificación de la autorización | Un mes | Art. 38 y documentos originales del vínculo |
| Familiares de españoles | 37, 38 y 41 | Un mes en el supuesto del art. 97.1.a) | Quince días | Art. 38 salvo la letra h) y documentos del vínculo |
| Búsqueda de empleo | 43 a 45 | Orden ministerial | Orden ministerial | Art. 38 y requisitos de la orden |

**Procedimiento consular (`BOE-A-2024-24099`, art. 27).**
- Recibo con fecha y lugar; posibles informes; entrevista con al menos dos representantes de la Administración, intérprete si hace falta, acta firmada y copia al solicitante (art. 27.3).
- Incomparecencia en el plazo fijado (no más de quince días): desistimiento, salvo causa fundada (art. 27.3).
- Requerimientos: plazo máximo de diez días, ampliable hasta cinco; desatendidos, desistimiento (art. 27.5). Comprueba que el requerimiento se hizo por el medio convenido y quedó constancia.
- Plazos de presentación tras la autorización: dos meses en reagrupación y uno en trabajo por cuenta ajena y temporada (art. 40.1); uno en familiares de españoles del art. 97.1.a) (art. 41.2); antelación mínima de dos meses en estudios (art. 36.1).
- Plazos para resolver: un mes en estudios, residencia no lucrativa y por cuenta propia, reagrupación y trabajo (arts. 36.4, 39.5 y 40.3); quince días en familiares de españoles (art. 41.2 y 41.3). El silencio de la oficina de extranjería sobre la autorización es desfavorable a los siete días en estudios (art. 36.3) y desestimatorio a los dos meses en familiares de españoles (art. 41.3).
- El régimen general del silencio en el visado está en disposiciones adicionales de la LOEX y del Reglamento que Jurisprudenciator **no devuelve**. Si el recurso depende de él (recurso contra una falta de respuesta), aplica la puerta: detén esa parte y explica qué precepto falta.

**Causas de denegación y motivación.**
- Causas del art. 28.5 del Reglamento: no acreditar requisitos; documentos falsos, alegaciones inexactas, mala fe o fraude de ley; causa de inadmisión no apreciada al recibir la solicitud; falta de acreditación indubitada de identidad, validez de documentos o veracidad de los motivos. Encaja el motivo de la resolución en una de ellas; si no encaja en ninguna, dilo en el recurso.
- Motivación: el art. 28.6 del Reglamento exige que toda denegación sea motivada e informe de los hechos, circunstancias, testimonios, documentos e informes que la sustentan; el art. 28.7 exige indicar recurso, órgano y plazo. La `LOEX`, art. 27.6, solo impone la motivación en reagrupación, trabajo por cuenta ajena, estancia y tránsito, y el art. 20.2 salva lo dispuesto en el art. 27. Cita ambos y añade `LPAC`, art. 35.1, letras a) e i). La jurisprudencia reciente del Tribunal Superior de Justicia de Madrid solo anula por falta de motivación si causó indefensión (`LPAC`, art. 48.2): demuestra la indefensión concreta (qué documento no se identificó, qué contradicción no se explicó) en lugar de alegarla en abstracto.
- Corta duración: denegación con el impreso normalizado del anexo VI y derecho a recurrir conforme al Derecho nacional (`Reglamento (CE) 810/2009`, art. 32.2 y 32.3; `BOE-A-2024-24099`, art. 28.9). Motivos del art. 32.1 del Código (entre ellos, dudas razonables sobre la intención de abandonar el territorio) y verificación del «riesgo de inmigración ilegal» (art. 21.1); documentos justificativos (art. 14); condiciones de entrada (`Reglamento (UE) 2016/399`, art. 6). Una denegación anterior no implica la denegación automática de una nueva solicitud (Código, art. 21.9).
- «Riesgo migratorio» en visados de larga duración: no figura como causa autónoma en el art. 28.5 del Reglamento. Si la resolución lo invoca, sostén que solo cabe si se concreta en una causa del art. 28.5 (normalmente la letra d) con hechos, y comprueba antes cómo lo trata la jurisprudencia reciente.
- Lista de no admisibles del SIS: el interesado puede pedir acceso, rectificación o supresión a la Secretaría de Estado de Seguridad a través de la oficina consular (art. 28.8). Es un escrito distinto del recurso.

**Recursos y plazos.**
- Reposición potestativa ante la misma oficina consular: un mes desde la notificación (`LPAC`, arts. 123 y 124). Comprueba en el pie de recursos que la resolución pone fin a la vía administrativa; la disposición adicional del Reglamento que lo regula no la devuelve el conector.
- Recurso contencioso: los actos de las oficinas consulares no son de la Administración periférica del Estado, así que no entran en el art. 8.4 de la LJCA. La Audiencia Nacional declina su competencia y remite estos recursos al Tribunal Superior de Justicia de Madrid por la cláusula residual del art. 10.1.n) de la LJCA, en relación con su art. 14.1; confírmalo con la búsqueda de autos de la lista antes de encabezar y cita la regla del art. 14.1 solo si el auto leído la menciona (los autos no coinciden: unos citan el art. 14.1 sin más y otros su regla segunda). Ante la Sala actúan procurador y abogado (`LJCA`, art. 23.2) y el procedimiento es el ordinario (el abreviado del art. 78 es para órganos unipersonales).
- Plazo: dos meses desde el día siguiente a la notificación de la denegación o de la resolución expresa de la reposición (`LJCA`, art. 46.1); si la reposición no se resuelve en un mes, seis meses desde la desestimación presunta. **Durante agosto no corre el plazo** (`LJCA`, art. 128.2): si el plazo cruza agosto, descuéntalo y busca la doctrina del Supremo que lo aplica (`consulta="plazo de dos meses recurso contencioso-administrativo mes de agosto inhábil artículo 128.2"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`; sin el filtro de jurisdicción devuelve sentencias penales y civiles); da como fecha límite la más temprana de las interpretaciones posibles. Si el último día es sábado, domingo o festivo, pasa al siguiente hábil (`LOPJ`, art. 182.1). Fuera de plazo, inadmisión: antes de decir al abogado que el plazo ha vencido, comprueba agosto y los días inhábiles.
- Medidas cautelares: suspender una denegación no da el visado. Si hay urgencia real y documentada, valora con el abogado una medida cautelar positiva (`LJCA`, arts. 129 y 130) y avisa de que su concesión es excepcional; busca antes precedentes (`consulta="medida cautelar positiva visado concesión provisional"`, `base="AN"`).
- La LOEX solo prevé la solicitud de asistencia jurídica gratuita desde el extranjero para denegación de entrada, devolución o expulsión (`LOEX`, art. 22.3): no la afirmes para visados sin norma o jurisprudencia leída.

## Estrategia y jurisprudencia

1. **Recurrir o volver a solicitar.** Si la denegación se debe a un documento que faltaba y hoy existe, compara con el abogado el tiempo y coste de una nueva solicitud (Código de visados, art. 21.9, en corta duración) frente al recurso. Si la denegación es arbitraria o no identifica el motivo, recurre.
2. **Pide el expediente y el acta.** Si la denegación se apoya en la entrevista, solicita copia del acta (art. 27.3) y del expediente; la falta de acta o de copia refuerza la indefensión.
3. **Prueba del arraigo en origen (corta duración).** Ordena la documentación por los motivos del art. 32.1 del Código: finalidad y condiciones, medios, seguro, intención de regreso (trabajo, familia, bienes, viajes anteriores con regreso en plazo).
4. **Reagrupación y familiares.** Si el consulado duda del vínculo o aprecia fraude, aporta prueba de la relación y busca doctrina sobre la carga de la prueba del fraude y el valor del acta de entrevista (`consulta="denegación visado reagrupación familiar fraude matrimonio de conveniencia entrevista"`, `base="AN"`).
5. **Consultas útiles** (`jurisdiccion="CONTENCIOSO"`, `base="AN"`, `fecha_desde` de los dos últimos años): `"denegación visado motivación estereotipada indefensión"`, `"denegación visado estancia corta duración intención de abandonar arraigo"`, `"denegación visado estudios medios económicos"`, `"visado familiar de ciudadano español artículo 41"`. Con `base="TJUE"`: `"visado uniforme obligación de expedir margen de apreciación"` y `"Código de visados denegación recurso órgano jurisdiccional"`. Lee con `parrafos=3` y `terminos` del motivo.
6. **Cuadro de motivos habituales** (consultas con `jurisdiccion="CONTENCIOSO"` y `base="AN"` salvo que se indique otra):

| Motivo en la resolución | Encaje legal que debes comprobar | Consulta | Línea de defensa |
|---|---|---|---|
| «No acredita la intención de abandonar el territorio» | Código de visados, arts. 21.1 y 32.1.b) | `"visado corta duración intención de abandonar arraigo país de origen"` | Vínculos laborales, familiares y económicos documentados; viajes anteriores con regreso |
| «Riesgo migratorio» en un visado de larga duración | Reglamento, art. 28.5 (no lo recoge como causa autónoma) | `"denegación visado riesgo migratorio residencia"` | Exigir su concreción en una causa del art. 28.5 con hechos |
| «Documentos no fiables» o «falta de veracidad» | Reglamento, art. 28.5.b) y d) | `"denegación visado documentos falsos veracidad carga de la prueba"` | Identificar qué documento, aportar legalización o cotejo |
| «Fraude» en reagrupación o matrimonio | Reglamento, art. 28.5.b); acta del art. 27.3 | `"visado reagrupación matrimonio de conveniencia acta entrevista"` | Prueba de la relación; defectos del acta o falta de copia |
| Resolución genérica o estereotipada | Reglamento, art. 28.6; `LOEX`, art. 27.6; `LPAC`, arts. 35 y 48.2 | `"denegación visado motivación estereotipada indefensión"` | Indefensión concreta: qué no se pudo rebatir |
| Inclusión en el SIS | Reglamento, art. 28.8; Código, art. 32.1.a).v) | `"denegación visado Sistema de Información Schengen no admisible"` | Petición de acceso y rectificación, además del recurso |
| «No acredita la dependencia económica» o «la necesidad» en la reagrupación de un ascendiente ya autorizada por Extranjería | Reglamento, arts. 40.2, 66.1.e), 68.3.b) y 196; `LOEX`, art. 17.1.d) | `"alcance potestad misión diplomática oficina consular denegación visado reagrupación familiar"` con `base="TS"` | Doctrina del Supremo de 2026: la revisión consular se refiere a la veracidad de lo valorado y exige motivación; pide que el consulado identifique qué circunstancia no es veraz y por qué; presunción de estar a cargo del art. 196.3.c) (fondos de al menos el 51 % del PIB per cápita durante el año previo, dato del Banco Mundial que aporta el cliente) |

7. **Anticipa la réplica habitual:** la Abogacía del Estado y el Tribunal Superior de Justicia de Madrid subrayan la proximidad del consulado a la realidad del país y la falta de un derecho fundamental a entrar. Contesta con hechos concretos y documentos, no con principios.
8. **Cómo usar la doctrina:** premisa normativa con texto vigente, párrafo literal del fundamento con órgano, fecha y ECLI tal como los devolvió `leer_sentencias`, aplicación al caso y conclusión. Nunca el relato de hechos ni datos de las partes de aquel pleito.

## Documento que se entrega

Formato, citas y datos: `references/formato-y-organos.md`. Todo en Word. Dos reglas de cita en el texto del escrito:

- El Reglamento se cita como «artículo N del Real Decreto 1155/2024»; con otra fórmula, `verificar_escrito` no identifica la norma y da la cita por inexistente.
- `verificar_escrito` no reconoce los Reglamentos de la Unión (Código de visados, Código de fronteras Schengen): atribuye sus artículos a la ley española que tenga más cerca en el texto (LPAC, Real Decreto 1155/2024, LJCA) y los da por existentes con otro contenido, con «posible disonancia» o por no localizados. Comprueba esas citas una a una con `buscar_articulo`, no las retires por el aviso, no des por buena una cita por un «existe» que corresponde a otra norma y dilo en el resumen. Para reducir atribuciones erróneas, escribe siempre la norma junto al número del artículo («artículo 27.6 de la Ley Orgánica 4/2000», no «su artículo 27.6» ni «el artículo 28.6» a secas).

**A. Solicitud de copia del expediente y del acta** (`solicitud-expediente-visado-<apellido>-<AAAAMMDD>.docx`): a la oficina consular; identificación de la solicitud `[NÚMERO DE SOLICITUD DE VISADO]`; petición de copia del expediente, del acta de entrevista y de los informes; mención de que el plazo de recurso sigue corriendo.

**B. Recurso de reposición** (`recurso-reposicion-visado-<apellido>-<AAAAMMDD>.docx`).
1. Encabezamiento a la oficina consular que dictó la resolución (nombre exacto de la resolución).
2. Comparecencia: `[NOMBRE Y APELLIDOS]`, `[PASAPORTE]`, `[DOMICILIO EN LA DEMARCACIÓN CONSULAR]`, representación.
3. Hechos numerados: solicitud, autorización previa si la hubo, requerimientos, entrevista, resolución y motivo literal.
4. Fundamentos: procedencia y plazo; falta o insuficiencia de motivación con la indefensión concreta; cumplimiento del requisito que se dice incumplido; inexistencia de la causa del art. 28.5 invocada (o del art. 32.1 del Código); doctrina.
5. SOLICITA: estimación y concesión del visado; subsidiariamente, retroacción con nueva valoración o entrevista con acta.
6. Documentos nuevos numerados, con traducción cuando proceda.

**C. Escrito de interposición del recurso contencioso-administrativo** (`recurso-contencioso-visado-<apellido>-<AAAAMMDD>.docx`): a la Sala comprobada; comparecencia del procurador `[PROCURADOR]` con abogado; acto impugnado (denegación y, en su caso, desestimación de la reposición) y fecha de notificación; petición de que se tenga por interpuesto y se reclame el expediente (`LJCA`, art. 45); documentos. Si el abogado lo pide, añade el esquema de la demanda (plazo de veinte días desde la entrega del expediente, `LJCA`, art. 52): hechos, fundamentos, pretensión de anulación y reconocimiento del derecho al visado, prueba.

**Reparto para la redacción rápida:** A (solicitud de copia del expediente) y C (interposición), de una o dos páginas: el director sin equipo. B (reposición): 01 encabezamiento, comparecencia y hechos; 02 procedencia, plazo y motivación; una sección por cada requisito que se dice incumplido o causa invocada, con su doctrina; cierre con solicita, documentos nuevos y traducciones.

## Comprobación final

- [ ] `estado` respondió y la puerta se cumplió en todo el trabajo.
- [ ] Cada artículo citado del Reglamento (`BOE-A-2024-24099`), la LOEX, el Código de visados, la LPAC y la LJCA se leyó en esta conversación con `buscar_articulo`, con sus notas de nulidad; ningún inciso anulado se aplica ni se cita.
- [ ] El Reglamento se cita en el escrito como «artículo N del Real Decreto 1155/2024».
- [ ] Si el caso dependía de una disposición adicional (silencio, recursos) o de una orden ministerial que el conector no devuelve, la tarea se detuvo en ese punto y se explicó al abogado qué precepto falta.
- [ ] Separados la denegación del visado y, en su caso, la de la autorización previa, con su órgano y su recurso.
- [ ] Órgano judicial comprobado con la LJCA y con un auto o sentencia reciente leído.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; solo fundamentos jurídicos.
- [ ] `verificar_escrito` pasado por cada redactor sobre sus frases con normas y corregidos los avisos. No identifica las citas con letra («artículo 20.1.b)», «artículo 11.1.a)») y las marca como no localizadas: compruébalas con `buscar_articulo` y no las cambies por ese aviso.
- [ ] Marcadores entre corchetes para todo dato no facilitado; ningún dato inventado.
- [ ] Plazo con fecha de notificación, precepto y fecha final; sin fecha de notificación, no se da plazo. En el contencioso, agosto descontado (`LJCA`, art. 128.2) y último día inhábil trasladado al siguiente hábil.
- [ ] Para cada sentencia del TSJ de Madrid citada, comprobado si aplicó el Real Decreto 1155/2024 o el anterior Real Decreto 557/2011 (muchas de 2025 y 2026 aún resuelven denegaciones anteriores al 20/05/2025), y dicho en el escrito cuando sea el anterior.
- [ ] Resumen para el abogado según el apartado 7 del formato: documento y órgano, plazo, documentos que faltan y riesgos, tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene) y próximo paso (reposición, contencioso o nueva solicitud).
