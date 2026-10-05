---
name: arraigo-familiar
description: >-
  Prepara la solicitud de autorización de residencia temporal por arraigo familiar (arts. 125.1.e y 127.e del
  Reglamento aprobado por el Real Decreto 1155/2024), de cinco años y sin permanencia mínima, con memoria
  justificativa en Word y relación de documentos para la Oficina de Extranjería. Úsala cuando el abogado diga
  «arraigo familiar», «es padre o madre de un menor comunitario», «el niño es de otro país de la UE» o «cuida
  de un familiar comunitario con discapacidad». Comprueba la nacionalidad del menor o de la persona con
  discapacidad, la tenencia a cargo, la convivencia o las obligaciones paternofiliales, y los antecedentes. Si
  el menor o el familiar es español, no es arraigo, sino familiares-de-espanoles. Sin ese vínculo, usa
  arraigo-social, arraigo-sociolaboral, arraigo-socioformativo o arraigo-segunda-oportunidad.
---

# Arraigo familiar

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Base legal y requisitos vigentes** → `buscar_articulo` (`ley="LOEX"`, `articulo="31"`) y `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"124"`, `"125"`, `"126"` y `"127"`).
- **Procedimiento, trabajo y duración** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"130"`, `"131"`, `"132"`, `"193"` y `"197"`).
- **Frontera con las figuras vecinas** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, `articulo="94"`) para familiares de españoles, y `buscar_articulo` (`ley="Real Decreto 240/2007"`, artículos `"2"` y `"7"`) para familiares de ciudadanos de la Unión. Si el menor puede tener también la nacionalidad española: `buscar_articulo` (`ley="CC"`, `articulo="17"`) y (`ley="LOEX"`, `articulo="1"`).
- **Medidas de apoyo a la persona con discapacidad** → `buscar_articulo` (`ley="CC"`, `articulo="250"`); **cancelación de antecedentes** → `buscar_articulo` (`ley="CP"`, `articulo="136"`).
- **Doctrina sobre progenitores de menores ciudadanos de la Unión, «a cargo» y antecedentes** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"`; `base="TS"` para el Supremo) y `buscar_sentencias` (`base="TJUE"`) + `leer_sentencias` (`parrafos=3`).
- **Reformas del Reglamento** → en cada artículo que devuelva `buscar_articulo`, la línea «redacción vigente dada por…» y las notas «Téngase en cuenta…» (`buscar_boe` no localiza las reformas); si hay que leer la norma que reformó, `leer_boe` con su identificador.
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

Si aún no está claro qué vía conviene al cliente, empieza por `extranjeria-intake` o `informe-viabilidad-extranjeria`; para revisar un expediente documental ya reunido, `documentacion-expediente`. Si la solicitud ya se presentó y hay requerimiento, denegación o archivo, esta skill no es la herramienta: `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria`.

Desde el Reglamento de 2025 el arraigo familiar **solo** cubre dos supuestos (art. 127.e):

1. **Padre, madre o tutor de un menor nacional de otro Estado miembro de la Unión Europea, del Espacio Económico Europeo o de Suiza**, que al solicitar acredita residir en España, tiene a cargo al menor y convive con él, o está al corriente de sus obligaciones paternofiliales.
2. **Familiar que presta apoyo a una persona con discapacidad** nacional de esos Estados para el ejercicio de su capacidad jurídica, que la tiene a cargo y convive con ella.

No exige permanencia mínima (art. 126.b, último párrafo) y dura **cinco años** (art. 125.2).

**Detector** (si encaja otra figura, dilo al abogado con el artículo leído y no redactes este arraigo; entrégale una nota breve —en el chat o, si la pide, en Word como nota interna y no como escrito para presentar— con el motivo, el artículo leído de la figura que procede, sus rasgos básicos leídos con `buscar_articulo` y la skill con la que seguir):

| Situación del cliente | Figura que procede |
|---|---|
| El menor, el cónyuge, la pareja, el hijo o el ascendiente es **español** | `familiares-de-espanoles` (arts. 93-99; progenitor de menor español en el art. 94.1.f) |
| El menor tiene **doble nacionalidad y una es la española** (típico: nació de padre o madre que ya era español, letra a) del art. 17.1 del Código Civil, aunque el abogado solo hable del pasaporte comunitario) | `familiares-de-espanoles`: para la Ley Orgánica 4/2000 no es extranjero quien tiene la nacionalidad española (art. 1.1 LOEX, léelo). No redactes el arraigo por la lectura literal de «nacional de otro Estado miembro»; explica al abogado que la vía del art. 94.1.f es la aplicable y además más favorable (arts. 97.5 y 97.8) |
| Cónyuge, pareja registrada, descendiente menor de 21 o a cargo, o ascendiente a cargo de un ciudadano de otro Estado de la UE que ejerce la libre circulación | `ciudadanos-ue-y-familiares`: tarjeta de familiar de ciudadano de la Unión (Real Decreto 240/2007, arts. 2 y 7) |
| El menor tiene nacionalidad de un tercer país (aunque haya nacido en España) | no hay arraigo familiar; valora el régimen de menores (arts. 159-164) y, para el progenitor, arraigo-social u otra figura |
| El menor es de otro Estado de la UE y la familia tiene recursos y seguro de enfermedad (art. 7.1.b del Real Decreto 240/2007) | compara con el abogado el derecho derivado del Derecho de la Unión (`ciudadanos-ue-y-familiares`) y el arraigo familiar, que da cinco años y trabajo (arts. 125.2 y 131) |
| Dos años en España con contrato, familia residente o formación | arraigo-sociolaboral, arraigo-social o arraigo-socioformativo |
| Fue titular de residencia no excepcional y no la renovó | arraigo-segunda-oportunidad (art. 127.a) |
| Ya tiene un arraigo familiar concedido con el Real Decreto 557/2011 por su vínculo con un español (progenitor de menor español, cónyuge…) y pregunta qué hacer al vencer | no es una solicitud nueva de arraigo: la disposición transitoria tercera del Real Decreto 1155/2024 (léela con `leer_boe`, `identificador="BOE-A-2024-24099"`; el conector la corta al final, así que no afirmes lo que no se lea) le permite conservar la residencia mientras cumpla las condiciones de los familiares de españoles; sigue con `familiares-de-espanoles` o `renovacion-modificacion-extincion` |
| Solicitante de protección internacional sin resolución firme, o con otro procedimiento de autorización en trámite | no puede pedir arraigo (art. 126.a y h), aunque no se exija permanencia |
| Orden de expulsión vigente o prohibición de entrada | `expulsion-procedimiento-sancionador` (la expulsión archiva cualquier procedimiento de residencia, art. 244.3) |

## Datos que hay que reunir antes de redactar

Saca estos datos de la documentación aportada (paso 2 de `redaccion-rapida`). Si falta algún imprescindible (★) que bloquee el escrito, pídelos todos a la vez en una única ronda de no más de cuatro preguntas; lo demás queda como `[PENDIENTE: dato]`:

1. ★ Nacionalidad, pasaporte en vigor y provincia de residencia efectiva del solicitante (art. 193.2); prueba de que reside en España.
2. ★ Supuesto: menor o persona con discapacidad.
3. ★ **Menor**: nacionalidad exacta y documento que la prueba (pasaporte o documento de identidad del Estado miembro, certificado consular de nacionalidad); **si tiene además la nacionalidad española** y la nacionalidad de cada progenitor en la fecha del nacimiento (si nació en España, pide la certificación literal del Registro Civil español: si un progenitor ya era español, el menor lo es de origen); certificado de nacimiento con la filiación, residencia en España (padrón, certificado de registro de ciudadano de la Unión si lo tiene), convivencia; si no convive: resolución de guarda y custodia, régimen de visitas y pensión de alimentos, y prueba de pago al corriente. Si es tutor: resolución de tutela.
4. ★ **Persona con discapacidad**: nacionalidad, grado de discapacidad reconocido, medida de apoyo que presta el solicitante (voluntaria, guarda de hecho, curatela o defensor judicial, art. 250 CC) y su documento, parentesco, convivencia y dependencia.
5. ★ Protección internacional (fechas y firmeza), autorizaciones previas y procedimientos de autorización en trámite.
6. ★ Antecedentes penales en España y en los países de residencia de los cinco años previos a la entrada, antecedentes policiales, expulsiones, prohibiciones de entrada, compromiso de no retorno.
7. Medios de vida de la unidad familiar y papel del solicitante en el cuidado del menor (útil para acreditar «a cargo» y para la ponderación si hay antecedentes).
8. Representación del abogado (art. 197.4).

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo; aplica las notas «Téngase en cuenta» sobre nulidad si aparecen.

**Generales (art. 126)**: estar en España sin ser solicitante de protección internacional (a); **sin permanencia mínima** (b, último párrafo); no ser amenaza para el orden público (c); carecer de antecedentes penales en España y en los países de residencia de los cinco años anteriores a la entrada (d, y art. 31.5 LOEX), comprobando con el art. 136 CP si están cancelados o deberían estarlo; no ser rechazable en Schengen (e); no estar en plazo de no retorno (f); tasa abonada, sin dar importe ni modelo: remite a la sede oficial (g); no ser titular de autorización de estancia o residencia ni interesado en otro procedimiento de concesión, prórroga, renovación o modificación de autorizaciones en trámite (h); si lo hay, adviértelo y valora con el abogado el desistimiento antes de presentar.

**Específicos (art. 127.e)**:

- **Supuesto 1.º (menor)**: vínculo de padre, madre o tutor; nacionalidad del menor de otro Estado de la UE, del EEE o de Suiza (no española); residencia del solicitante en España al solicitar; y **tener a cargo al menor y convivir con él, o estar al corriente de las obligaciones paternofiliales**. El segundo inciso permite el arraigo al progenitor no custodio que cumple: pruébalo con la resolución de medidas y los justificantes de pago y de relación.
- **Supuesto 2.º (discapacidad)**: nacionalidad de la persona apoyada de esos Estados; condición de familiar; medida de apoyo para el ejercicio de la capacidad jurídica (art. 250 CC); tenerla a cargo; convivencia.
- **«A cargo»**: el art. 196 define cuándo una persona extranjera está a cargo de otra a efectos del Reglamento. Léelo y valora si la oficina lo aplicará al menor o a la persona apoyada; busca doctrina sobre el concepto en el arraigo familiar antes de sostener tu lectura. Si quien solicita no tiene ingresos propios, avisa al abogado de que la oficina podría exigirle los umbrales de medios del apartado 3.d del art. 196 (pensados para reagrupaciones) y pide la prueba de los fondos con los que sostiene al menor. Revisa la nota de nulidad parcial del apartado 2.b (Tribunal Supremo, julio de 2026) antes de apoyarte en él.
- **Antecedentes y Derecho de la Unión**: cuando el derecho deriva de un menor ciudadano de la Unión, la doctrina europea y la de los tribunales españoles rechazan la **denegación automática** por antecedentes penales del progenitor y exigen valorar si su conducta es una amenaza real, actual y suficientemente grave, ponderando el interés superior del menor. Localiza y lee esa doctrina antes de alegarla (ver «Estrategia»). No la uses si el menor es español: ese supuesto va por los arts. 93-99.

**Prueba de cada elemento** (pide el documento principal; si no existe, la alternativa):

| Elemento | Documento principal | Alternativas |
|---|---|---|
| Filiación o tutela | Certificado de nacimiento del menor; resolución de tutela | Libro de familia o inscripción consular |
| Nacionalidad del menor o de la persona apoyada | Pasaporte o documento de identidad del Estado miembro | Certificado consular de nacionalidad |
| Residencia en España del solicitante | Padrón | Contrato de alquiler, asistencia sanitaria, escolarización del menor |
| Convivencia | Padrón colectivo o certificado de convivencia | Informes escolares o sanitarios con el mismo domicilio |
| Al corriente de las obligaciones paternofiliales | Resolución de medidas y justificantes de pago de la pensión | Transferencias periódicas, pago de gastos escolares, cumplimiento de visitas |
| Medida de apoyo | Escritura de apoyo voluntario o resolución judicial de curatela o defensor | Prueba de la guarda de hecho (art. 250 CC) |
| Discapacidad | Resolución de reconocimiento del grado | Informes médicos oficiales |

**Normas que el conector no devuelve por `buscar_articulo`:**

- Notas de nulidad que hablan del «inciso destacado» (por ejemplo, en el art. 94.1.f): el texto que devuelve `buscar_articulo` no marca cuál es. Léelo en el fallo con `leer_boe` (`identificador="BOE-A-2026-19632"`, sentencia del Tribunal Supremo de 8 de julio de 2026), que transcribe cada inciso anulado.
- `buscar_articulo` con `ley="CC"` y `articulo="9"` devuelve el art. 94 bis del Código Civil (fallo del conector): no apoyes la doble nacionalidad en el art. 9.9 CC; basta el art. 1.1 LOEX y el art. 17 CC.

- Disposiciones adicionales vigésima y vigesimoprimera del Reglamento (arraigo de solicitantes de protección internacional y arraigo extraordinario, que solo podían pedirse hasta el 30/06/2026): léelas con `leer_boe` (`identificador="BOE-A-2026-8284"`, Real Decreto 316/2026). Si el cliente tiene una de esas solicitudes sin resolver, choca con el art. 126.h.
- Solicitudes de arraigo presentadas desde el 20/05/2025 hasta la entrada en vigor del Real Decreto 316/2026 (sus redacciones rigen desde el 16/04/2026) y aún en trámite: su régimen está en la disposición transitoria segunda de ese real decreto, que `leer_boe` no llega a devolver. Si el caso depende de ella, aplica la puerta y di al abogado qué precepto falta.

**Procedimiento y efectos**:

- Solicitud personal (o por representante acreditado, art. 197.4) ante la oficina de la provincia de residencia, sin visado, con pasaporte en vigor y documentación del supuesto (art. 130.1).
- Certificados de antecedentes de los países de residencia de los cinco años previos a la entrada, con las excepciones del art. 130.2; la oficina pide de oficio penados e informe policial, que no deniega de forma automática (art. 130.2). Subsanación en el plazo que fije la oficina, máximo quince días (art. 130.3).
- Concedida: **cinco años** (arts. 125.2 y 132.1), con autorización de trabajo por cuenta ajena o propia sin límites (art. 131). TIE en un mes desde la notificación (art. 130.6).
- El art. 132.2 no fija requisitos específicos de prórroga para el arraigo familiar. Antes de aconsejar qué hacer al final de los cinco años, lee con `buscar_articulo` los artículos de residencia de larga duración (175 y siguientes, 182 y siguientes) y remite a `larga-duracion`.
- Plazo máximo de resolución y silencio: en disposiciones adicionales que el conector no devuelve. No los afirmes; remite al BOE consolidado.

**Causas típicas de denegación y cómo rebatirlas:**

| Causa | Respuesta |
|---|---|
| El menor no es nacional de otro Estado de la UE, el EEE o Suiza | Documento de nacionalidad del menor; si es español o de tercer país, cambiar de figura |
| No se acredita la filiación o la tutela | Certificado de nacimiento o resolución de tutela, con la legalización o apostilla y traducción que pida la oficina |
| No convive ni está a cargo | Segundo inciso: al corriente de obligaciones paternofiliales (pensión, visitas, gastos) |
| Antecedentes penales | Cancelación (art. 136 CP) y, además, doctrina que proscribe la denegación automática en supuestos de menores ciudadanos de la Unión |
| El solicitante no reside en España | Padrón y prueba de residencia efectiva al solicitar |
| Protección internacional pendiente o procedimiento en trámite | Art. 126.a y h: esperar firmeza o desistir antes de presentar |

## Estrategia y jurisprudencia

1. Confirma primero la nacionalidad del menor o de la persona apoyada: decide la figura entera (arraigo familiar, familiar de español o régimen de ciudadanos de la Unión).
2. Si hay antecedentes, construye la ponderación: tiempo transcurrido, pena cumplida, conducta posterior, vínculo real con el menor, consecuencias de la denegación para el menor.
   Ordena la ponderación en este orden, y cada punto con su documento: (a) naturaleza y gravedad del delito y pena impuesta; (b) fecha de los hechos y de extinción de la pena; (c) ausencia de reiteración y conducta posterior; (d) intensidad del vínculo con el menor (convivencia, cuidado diario, sostenimiento); (e) consecuencias de la denegación para el menor, que tendría que elegir entre separarse del progenitor o salir de España.
3. Consultas en Jurisprudenciator (máximo dos reformulaciones):
   - `buscar_sentencias` (`consulta="arraigo familiar progenitor menor ciudadano de la Unión antecedentes penales denegación automática"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`).
   - La misma con `base="TS"` para el criterio casacional.
   - `buscar_sentencias` (`consulta="progenitor nacional de tercer país menor ciudadano de la Unión derecho de residencia antecedentes penales"`, `base="TJUE"`).
   - `consulta="arraigo familiar progenitor no custodio al corriente obligaciones paternofiliales"`, `base="AN"`.
   - `consulta="arraigo familiar a cargo convivencia menor"`, `base="AN"`, `fecha_desde="20/05/2025"`.
   - Concepto «a cargo» fijado en casación: `consulta="concepto a cargo arraigo familiar circunstancias familiares económicas y sociales"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"` (sin la jurisdicción salen sentencias de la Sala de lo Penal). Lee el fundamento que responde a la cuestión de interés casacional con términos que alcancen toda la respuesta (`terminos="respuesta cuestión casacional circunstancias específicas subvenir necesidades básicas"`), no los párrafos que resumen las alegaciones de las partes, y comprueba que el párrafo que vas a transcribir está completo en la salida.
   - Supuesto de discapacidad: `consulta="residencia familiar apoyo persona con discapacidad ciudadano de la Unión a cargo convivencia"`, `base="AN"`.
4. Mucha doctrina se dictó sobre el antiguo art. 124.3 del Real Decreto 557/2011, que incluía a los progenitores de menores españoles. Cítala para los conceptos que se mantienen («a cargo», convivencia, obligaciones paternofiliales, ponderación de antecedentes) y dilo en el escrito; no la uses para el ámbito subjetivo, que ahora se limita a nacionales de otros Estados.
5. Transcribe solo párrafos de fundamentos leídos con `leer_sentencias`, nunca hechos ni datos de las partes de aquel pleito ni de los menores.

**Al citar una sentencia**, comprueba qué reglamento aplicó (Real Decreto 557/2011 o Real Decreto 1155/2024: fecha de la solicitud de aquel caso y artículos que cita) y dilo en el escrito. Si aplicó el anterior, cítala solo para requisitos que los arts. 126 y 127 vigentes mantienen iguales. Si la resolución anula o interpreta un precepto del Reglamento vigente, contrasta que la nota «Téngase en cuenta» de `buscar_articulo` lo refleja.

## Documento que se entrega

Un Word maquetado según `references/formato-y-organos.md`: **solicitud de autorización de residencia temporal por circunstancias excepcionales por arraigo familiar con memoria justificativa**. Acompaña al impreso oficial vigente, que el abogado descarga de la sede.

Nombre: `solicitud-arraigo-familiar-<apellido-cliente>-<AAAAMMDD>.docx`.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» (la primera vez, «, de 19 de noviembre, por el que se aprueba el Reglamento de la Ley Orgánica 4/2000») y la ley como «artículo 31.3 de la Ley Orgánica 4/2000», según el apartado 4 del formato: así `verificar_escrito` reconoce cada cita. Nunca «del Reglamento de Extranjería».

**Letras y ordinales, siempre delante del artículo**: «la letra e) del artículo 127 del Real Decreto 1155/2024», «el supuesto 1.º de la letra e) del artículo 127 del Real Decreto 1155/2024», «la letra b) del artículo 7.1 del Real Decreto 240/2007». Nunca «artículo 127.e) del…» ni «artículo 127, letra e), del…»: con esas formas `verificar_escrito` no identifica la norma y atribuye la cita a la última norma mencionada en el texto (aparece, por ejemplo, «artículo 127 de la Ley Orgánica 4/2000: no localizado»). Tampoco numeres artículos de los Tratados de la Unión («artículos 20 y 21 TFUE»): el verificador los atribuye al Reglamento; nómbralos sin número o remite a la sentencia que los interpreta.

Estructura:

1. **Encabezamiento**: «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA] — [DELEGACIÓN / SUBDELEGACIÓN] DEL GOBIERNO» (art. 193.2).
2. **Comparecencia** con marcadores (`[NOMBRE Y APELLIDOS]`, `[PASAPORTE]`, `[NIE]`, `[DOMICILIO]`) y representación (art. 197.4). Del menor o de la persona apoyada, solo iniciales y los datos imprescindibles (`[INICIALES DEL MENOR]`, `[NACIONALIDAD DEL MENOR]`).
3. **EXPONE — HECHOS**: PRIMERO.- Identidad y residencia en España del solicitante. SEGUNDO.- Vínculo (filiación, tutela o medida de apoyo). TERCERO.- Nacionalidad y residencia del menor o de la persona apoyada. CUARTO.- Convivencia y tenencia a cargo, o cumplimiento de las obligaciones paternofiliales. QUINTO.- Situación administrativa y ausencia de procedimientos en trámite. SEXTO.- Antecedentes y, si los hay, circunstancias para la ponderación.
4. **FUNDAMENTOS DE DERECHO**: I. Marco legal (art. 31.3 LOEX; arts. 124 y 125.1.e). II. Procedimiento y competencia (arts. 130, 193.2 y 197). III. Requisitos generales (art. 126), con la exención de permanencia. IV. Requisito específico (art. 127.e, supuesto aplicable). V. Interés superior del menor y, si procede, doctrina europea sobre antecedentes, con párrafo literal y ECLI. VI. Efectos: cinco años y trabajo (arts. 125.2 y 131).
5. **SOLICITA**: admisión a trámite y concesión por cinco años con habilitación para trabajar.
6. **OTROSÍ**: si hay antecedentes, que se practique la valoración individual y motivada del art. 130.2 y de la doctrina citada; que se recaben de oficio los informes del art. 130.2.
7. Lugar, fecha y firma.
8. **RELACIÓN DE DOCUMENTOS** numerada: impreso oficial; justificante de la tasa; pasaporte completo; prueba de residencia del solicitante; certificado de nacimiento o resolución de tutela o de la medida de apoyo; documento de nacionalidad del menor o de la persona apoyada y su residencia en España; certificado de discapacidad si procede; convivencia (padrón colectivo) o resolución de medidas y justificantes de pago; certificados de antecedentes (con legalización o apostilla y traducción según la hoja informativa); representación en una de las formas del art. 197.4 (apoderamiento notarial o apud acta en el registro electrónico de apoderamientos, convenio de habilitación o Registro Electrónico de Colaboradores de Extranjería; una autorización firmada en papel no basta).

**Reparto para la redacción rápida:** 01 encabezamiento, comparecencia y hechos; 02 fundamentos procesales (marco legal, procedimiento, competencia y requisitos generales del art. 126, con la exención de permanencia); 03 requisito específico del art. 127.e (supuesto aplicable, vínculo y nacionalidad del menor o de la persona apoyada); 04 interés superior del menor y doctrina sobre antecedentes, si los hay; 05 efectos, solicita, otrosí, firma y relación de documentos.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: LOEX 31; Reglamento 124, 125, 126, 127, 130, 131, 132, 193 y 197 (y 94, 196, Real Decreto 240/2007 arts. 2 y 7, CC 250 y CP 136 si se usan); fechas de vigencia y notas de nulidad revisadas.
- [ ] Nacionalidad del menor o de la persona apoyada acreditada; no es española (tampoco como segunda nacionalidad) ni de un tercer país.
- [ ] Letras y ordinales citados delante del artículo («la letra e) del artículo 127 del Real Decreto 1155/2024»), sin «artículo 127.e)».
- [ ] Supuesto del art. 127.e identificado y cada elemento con su documento.
- [ ] Si hay antecedentes: cancelación calculada y doctrina sobre la denegación no automática leída y citada con párrafo literal.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; `verificar_escrito` pasado por cada redactor sobre sus frases con normas.
- [ ] Cada aviso de «posible disonancia de contenido» de `verificar_escrito` contrastado con el apartado exacto leído con `buscar_articulo` (el verificador compara con el título del artículo, p. ej. «Requisitos específicos» o «Procedimiento»): si el apartado dice lo que afirma el escrito, se mantiene la cita y se explica en el resumen; si no, se corrige.
- [ ] Datos del menor reducidos a lo imprescindible; marcadores para lo que falta; sin importes de tasa, códigos de modelo ni plazos de resolución no obtenidos del conector.
- [ ] Resumen para el abogado según el apartado 7 del formato: oficina de destino; fechas con su precepto (subsanación, art. 130.3; TIE en un mes, art. 130.6; vencimiento a los cinco años, art. 125.2); documentos que faltan y riesgos; tabla de jurisprudencia; próximo paso.
