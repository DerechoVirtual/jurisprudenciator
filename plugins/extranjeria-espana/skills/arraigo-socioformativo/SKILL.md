---
name: arraigo-socioformativo
description: >-
  Prepara la solicitud de autorización de residencia temporal por arraigo socioformativo (arts. 125.1.d y
  127.d del Reglamento aprobado por el Real Decreto 1155/2024) con memoria justificativa en Word y relación de
  documentos para la Oficina de Extranjería. Úsala cuando el abogado diga «arraigo socioformativo», «arraigo
  para la formación», «se va a matricular en FP», «está haciendo un certificado de profesionalidad»,
  «bachillerato» o «ESO de adultos». Comprueba permanencia, antecedentes, que la formación esté en la lista
  cerrada, la ventana de dos meses antes de la matrícula y el informe de integración. Si ya tiene contrato,
  usa arraigo-sociolaboral; si tiene familia residente con medios, arraigo-social; si tuvo residencia que no
  renovó, arraigo-segunda-oportunidad; si quiere cursar estudios superiores, estudiantes-y-busqueda-empleo.
---

# Arraigo socioformativo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Base legal y requisitos vigentes** → `buscar_articulo` (`ley="LOEX"`, `articulo="31"`) y `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"124"`, `"125"`, `"126"` y `"127"`).
- **Formaciones admitidas** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, `articulo="52"`, letras b) y e) 5.º) y, para la formación de los servicios públicos de empleo, `articulo="75"`.
- **Procedimiento, límite de trabajo, prórroga y paso posterior** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"130"`, `"131"`, `"132"`, `"191"`, `"193"` y `"197"`).
- **Cancelación de antecedentes** → `buscar_articulo` (`ley="CP"`, `articulo="136"`).
- **Antiguo solicitante de protección internacional (firmeza de la denegación)** → `buscar_articulo` (`ley="Ley 12/2009"`, `articulo="29"`), (`ley="LPAC"`, artículos `"30"` y `"124"`) y (`ley="LJCA"`, artículos `"46"` y `"128"`).
- **Doctrina sobre el arraigo socioformativo y el anterior arraigo para la formación** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"`; `base="TS"` para el Supremo) + `leer_sentencias` (`parrafos=3`).
- **¿Se ha reformado el artículo?** → no uses `buscar_boe` para esto (con «Real Decreto 1155/2024» y fecha desde no devuelve ninguna reforma): lee la línea «redacción vigente dada por…» y las notas «Téngase en cuenta…» que devuelve `buscar_articulo` en cada artículo.
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

Si aún no está claro qué vía conviene al cliente, empieza por `extranjeria-intake` o `informe-viabilidad-extranjeria`; para revisar un expediente documental ya reunido, `documentacion-expediente`. Si la solicitud ya se presentó y hay requerimiento, denegación o archivo, esta skill no es la herramienta: `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria`.

- Persona extranjera en España, sin autorización de estancia o residencia, con al menos dos años de permanencia continuada, que **está matriculada o cursando**, o se va a matricular, en una de estas formaciones (art. 127.d):
  - estudios de educación secundaria postobligatoria del art. 52.1.b en centro autorizado (el propio precepto incluye los ciclos formativos de grado medio y los títulos de Especialista de Formación Profesional; el resto se define por la normativa educativa);
  - formación completa conducente a certificados profesionales de grado C del art. 52.1.e) 5.º, **incluido el nivel 1** para este arraigo, en centro autorizado;
  - oferta **presencial** de enseñanzas obligatorias en la educación de personas adultas;
  - o que se **compromete** a una formación promovida por los servicios públicos de empleo orientada a ocupaciones del Catálogo del art. 75.1.
- Además se exige el **informe de integración social** del art. 127.c.

**Detector** (si encaja otra figura, dilo al abogado con el artículo leído y no redactes este arraigo). Si la formación no está en la lista cerrada, **no hay solicitud**: si el abogado pide algo para el cliente, entrega una nota breve en Word (`nota-viabilidad-arraigo-socioformativo-<apellido-cliente>-<AAAAMMDD>.docx`) con la conclusión, la letra del art. 127.d y del art. 52.1 contrastada con cada formación, y las alternativas (otra formación que sí encaje, arraigo social por vínculo familiar o por integración, sociolaboral si hay contrato).

| Situación del cliente | Figura que procede |
|---|---|
| Quiere cursar estudios superiores (universidad y demás estudios del art. 52.1.a) | no están en el art. 127.d: `estudiantes-y-busqueda-empleo` (arts. 52 y ss.) |
| Cursos de idiomas, voluntariado, formación modular o parcial | no están en el art. 127.d; valora arraigo-social con informe de integración |
| Tiene contrato de 20 h semanales o más con salario mínimo o de convenio | arraigo-sociolaboral (art. 127.b): habilita a trabajar sin el tope de 30 h |
| Cónyuge, pareja registrada, padres o hijos extranjeros residentes con medios | arraigo-social por vía familiar (art. 127.c) |
| Fue titular de residencia no excepcional en los dos últimos años y no la renovó | arraigo-segunda-oportunidad (art. 127.a) |
| Progenitor o tutor de menor de otro Estado de la UE, el EEE o Suiza | arraigo-familiar (art. 127.e) |
| Familiar de español | `familiares-de-espanoles` (arts. 93-99) |
| Menor de edad | valora antes el régimen de menores (arts. 159-174); si se opta por el arraigo, presenta la solicitud su representante legal (art. 130.1) |
| Titular de estancia por estudios | `estudiantes-y-busqueda-empleo`: modificación (art. 190), no arraigo (art. 126.h) |
| Solicitante de protección internacional sin resolución firme, o con otro procedimiento de autorización en trámite | no puede pedir arraigo (art. 126.a y h) |
| Orden de expulsión vigente o prohibición de entrada | `expulsion-procedimiento-sancionador` (la expulsión archiva cualquier procedimiento de residencia, art. 244.3) |

## Datos que hay que reunir antes de redactar

No redactes al primer disparo. Pide los imprescindibles (★) que falten:

1. ★ Nacionalidad, pasaporte en vigor y provincia de residencia efectiva (art. 193.2).
2. ★ Fecha de entrada y pruebas de permanencia de cada tramo de los dos años; salidas de España.
3. ★ Protección internacional: fecha de la solicitud, de la resolución y de su **notificación**, recursos interpuestos y, si hubo recurso judicial, diligencia de firmeza; autorizaciones previas y procedimientos en trámite.
4. ★ Antecedentes penales (España y países de residencia de los cinco años previos a la entrada): pena, firmeza, extinción y, si hubo suspensión, fechas del auto de suspensión y de la remisión definitiva; antecedentes policiales, expulsiones, prohibiciones de entrada, compromiso de no retorno.
5. ★ **Formación**: denominación exacta, nivel, centro, si el centro está autorizado e inscrito en el registro oficial, modalidad y porcentaje presencial, si es completa o modular, curso académico, fechas del **plazo oficial de matrícula** y si ya está matriculado o cursando. Pide el certificado del centro o la preinscripción.
6. ★ Si es formación de los servicios públicos de empleo: el documento del compromiso y la ocupación del Catálogo a la que se orienta (el conector no devuelve el Catálogo: pide al abogado el documento oficial).
7. ★ **Informe de integración social**: fecha de solicitud, órgano (autonómico o municipal habilitado) y si se ha emitido.
8. Representación del abogado (art. 197.4). Si el cliente trabaja o va a trabajar, horas previstas (límite del art. 131.b).

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo; aplica las notas «Téngase en cuenta» sobre nulidad si aparecen.

**Generales (art. 126, acumulativos)**: estar en España sin ser solicitante de protección internacional (a); dos años de permanencia continuada, sin computar el tiempo como solicitante de protección internacional hasta la resolución firme (b); no ser amenaza para el orden público (c); carecer de antecedentes penales en España y en los países de residencia de los cinco años anteriores a la entrada (d, y art. 31.5 LOEX), comprobando con el art. 136 CP si las condenas están canceladas o deberían estarlo (si la pena se extinguió por remisión tras una suspensión, el plazo se retrotrae según su apartado 2: la duración de la pena corre desde el día siguiente al otorgamiento de la suspensión); no ser rechazable en Schengen (e); no estar en plazo de no retorno (f); tasa abonada, sin dar importe ni modelo: remite a la sede oficial (g); no ser titular de autorización de estancia o residencia ni interesado en otro procedimiento de concesión, prórroga, renovación o modificación de autorizaciones en trámite (h); si lo hay, adviértelo y valora con el abogado el desistimiento antes de presentar.

**Antiguo solicitante de protección internacional (letra b)**: cuenta solo la permanencia posterior a la firmeza de la denegación. Sin recurso, la resolución pone fin a la vía administrativa (art. 29.1 de la Ley 12/2009) y es inatacable cuando vence el plazo del contencioso: dos meses desde el día siguiente a la notificación (art. 46.1 LJCA), sin contar agosto (art. 128.2 LJCA). Toma como firmeza el día siguiente a ese vencimiento (lectura prudente); con recurso judicial, la diligencia de firmeza de la sentencia. No sumes la permanencia anterior a la solicitud de asilo. Las vías de las disposiciones adicionales vigésima y vigesimoprimera se cerraron el 30/06/2026.

**Específicos (art. 127.d)**:

- **Formación incluida**: compara la formación del cliente con el texto literal del art. 52.1.b y del art. 52.1.e) 5.º leídos en esta conversación: centro autorizado e inscrito, programa a tiempo completo o formación completa (ni modular ni parcial), al menos el 50 % presencial. Si no coincide, dilo y vuelve al detector.
- **Ventana de presentación**: si la matrícula tiene plazo oficial de formalización, la solicitud se presenta **en los dos meses anteriores al inicio de ese plazo** (el de matrícula, no el de preinscripción o admisión). Calcula la ventana con las fechas oficiales del centro y dásela al abogado. Si el cliente **ya está matriculado o cursando**, el art. 127.d admite expresamente esa situación, pero el texto no le exime de la ventana: sostener que no se aplica es una interpretación. Explícala en la memoria, respáldala con doctrina si la hay y, si no la hay, avisa al abogado del riesgo y ofrécele la alternativa segura (presentar en la ventana del curso siguiente).
- **Prueba de la matrícula**: ante la oficina en **tres meses desde la notificación de la concesión**; su falta extingue la autorización. En casos justificados puede matricularse en otra formación que cumpla los requisitos.
- **Formación de los servicios públicos de empleo**: compromiso de realizarla, orientada a ocupaciones del Catálogo del art. 75.1; no realizarla extingue la autorización.
- **Informe de integración social** en los términos del art. 127.c: emitido en un mes desde la solicitud; si no se emite en plazo y se acredita, se justifica por cualquier medio de prueba.
- **Desajuste que debes señalar**: el art. 132.2.b condiciona la prórroga a la promoción al segundo curso «en el caso de los ciclos formativos de grado básico o grado medio», pero el art. 127.d no enumera expresamente el grado básico. Si el cliente cursa grado básico, comprueba si encaja en otra letra (enseñanzas obligatorias de adultos) y avisa al abogado del riesgo antes de presentar.

**Normas que el conector no devuelve por `buscar_articulo`:**

- Disposiciones adicionales vigésima y vigesimoprimera del Reglamento (arraigo de solicitantes de protección internacional y arraigo extraordinario, que solo podían pedirse hasta el 30/06/2026): léelas con `leer_boe` (`identificador="BOE-A-2026-8284"`, Real Decreto 316/2026). Si el cliente tiene una de esas solicitudes sin resolver, choca con el art. 126.h.
- Solicitudes de arraigo presentadas desde el 20/05/2025 hasta la entrada en vigor del Real Decreto 316/2026 (sus redacciones rigen desde el 16/04/2026) y aún en trámite: su régimen está en la disposición transitoria segunda de ese real decreto, que `leer_boe` no llega a devolver. Si el caso depende de ella, aplica la puerta y di al abogado qué precepto falta.

**Procedimiento y efectos**:

- Solicitud personal (o por representante acreditado, art. 197.4) ante la oficina de la provincia de residencia, sin visado, con pasaporte en vigor y documentación del supuesto (art. 130.1).
- Certificados de antecedentes de los países de residencia de los cinco años previos a la entrada, con las excepciones del art. 130.2; la oficina pide de oficio penados e informe policial; los antecedentes policiales exigen valoración individual (art. 130.2). Subsanación en el plazo que fije la oficina, máximo quince días (art. 130.3).
- Concedida: un año (art. 125.2); permite trabajar por cuenta ajena **un máximo de treinta horas semanales** en cómputo global, con salario mínimo o de convenio en proporción a la jornada (art. 131.b). TIE en un mes desde la notificación (art. 130.6).
- Prórroga (art. 132.2.b): informe del centro que certifique la **promoción al segundo curso** en ciclos de grado básico o medio; si terminó antes del año, título o certificado obtenido y búsqueda activa de empleo con inscripción en el servicio público de empleo. Plazo: dos meses antes o tres después del vencimiento (art. 132.3). Planifica con el cliente la matrícula del segundo curso desde el principio.
- Tras la formación, la salida natural es la modificación a residencia y trabajo del art. 191 (apartado 2 o 3 según el tiempo de residencia): léelo antes de aconsejarla.
- Plazo máximo de resolución y silencio: en disposiciones adicionales que el conector no devuelve. No los afirmes; remite al BOE consolidado.

**Causas típicas de denegación o extinción y cómo rebatirlas:**

| Causa | Respuesta |
|---|---|
| Formación no incluida (modular, parcial, en línea mayoritaria, estudios superiores) | Certificado del centro con plan, nivel, carácter completo y horas presenciales; si de verdad no encaja, cambiar de figura |
| Centro no autorizado o no inscrito | Resolución de autorización e inscripción del centro |
| Solicitud fuera de la ventana de dos meses | Si ya estaba matriculado o cursando, el art. 127.d lo admite; si no, esperar a la siguiente ventana |
| Falta del informe de integración | Justificante de solicitud y transcurso del mes; prueba por otros medios (art. 127.c) |
| Matrícula no acreditada en tres meses | Justificar la causa y la matrícula en otra formación admitida (art. 127.d) |
| Permanencia o antecedentes | Prueba por tramos; art. 136 CP y doctrina del Supremo sobre antecedentes cancelables |

## Estrategia y jurisprudencia

1. Empieza por la formación: si no está en la lista cerrada del art. 127.d, ningún argumento la salva. Pide al centro un certificado que diga expresamente nivel, carácter completo, porcentaje presencial e inscripción del centro.
2. Coordina tres calendarios: dos años de permanencia (art. 126.b), ventana de dos meses antes de la matrícula (art. 127.d) y mes de emisión del informe de integración (art. 127.c). Pide el informe antes de que se abra la ventana.
   Rellena y entrega esta tabla con fechas concretas (sin fecha de entrada o de matrícula no hay cálculo: pídelas):

   | Hito | Precepto | Cálculo |
   |---|---|---|
   | Se cumplen los dos años | art. 126.b | entrada + dos años; si fue solicitante de protección internacional, firmeza de la denegación + dos años (ver «Antiguo solicitante») |
   | Se abre la ventana de solicitud | art. 127.d | inicio del plazo oficial de matrícula menos dos meses |
   | Se cierra la ventana | art. 127.d | día anterior al inicio del plazo oficial de matrícula |
   | Vence la emisión del informe | art. 127.c | solicitud del informe + un mes |
   | Vence la prueba de la matrícula | art. 127.d | notificación de la concesión + tres meses |
   | Vence la TIE | art. 130.6 | notificación de la concesión + un mes |

   Si los dos años no se cumplen antes de que se cierre la ventana, dilo: habrá que esperar a la ventana siguiente o cambiar de figura.
3. Si el cliente necesita trabajar más de treinta horas, advierte del límite del art. 131.b y valora el arraigo sociolaboral.
4. Consultas en Jurisprudenciator (máximo dos reformulaciones):
   - `buscar_sentencias` (`consulta="arraigo socioformativo"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="20/05/2025"`).
   - `consulta="arraigo para la formación matrícula plazo tres meses"`, `base="AN"`.
   - `consulta="arraigo formación certificado de profesionalidad centro autorizado"`, `base="AN"`.
   - `consulta="arraigo informe de integración no emitido en plazo cualquier medio de prueba"`, `base="AN"`.
   - Antecedentes: `consulta="arraigo antecedentes penales cancelados o cancelables artículo 136 Código Penal"`, `base="TS"`.
5. El antiguo arraigo para la formación (art. 124.4 del Real Decreto 557/2011) tenía una estructura parecida (dos años, compromiso de formación, prueba de la matrícula). Su doctrina se puede citar para la finalidad de la figura y la prueba de la matrícula, diciéndolo en el escrito; no para la lista de formaciones, que ha cambiado.
6. Transcribe solo párrafos de fundamentos leídos con `leer_sentencias`, nunca hechos ni datos de las partes de aquel pleito. Comprueba que ese párrafo es razonamiento de la Sala y no alegaciones de parte ni la transcripción de un precepto (en estas pruebas salieron ambas cosas con `parrafos=3`); si no lo es, afina `terminos` o elige otra resolución.

**Al citar una sentencia**, comprueba qué reglamento aplicó (Real Decreto 557/2011 o Real Decreto 1155/2024: fecha de la solicitud de aquel caso y artículos que cita) y dilo en el escrito. Si aplicó el anterior, cítala solo para requisitos que los arts. 126 y 127 vigentes mantienen iguales. Si la resolución anula o interpreta un precepto del Reglamento vigente, contrasta que la nota «Téngase en cuenta» de `buscar_articulo` lo refleja.

## Documento que se entrega

Un Word maquetado según `references/formato-y-organos.md`: **solicitud de autorización de residencia temporal por circunstancias excepcionales por arraigo socioformativo con memoria justificativa**. Acompaña al impreso oficial vigente, que el abogado descarga de la sede.

Nombre: `solicitud-arraigo-socioformativo-<apellido-cliente>-<AAAAMMDD>.docx`.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» (la primera vez, «, de 19 de noviembre, por el que se aprueba el Reglamento de la Ley Orgánica 4/2000») y la ley como «artículo 31.3 de la Ley Orgánica 4/2000», según el apartado 4 del formato: así `verificar_escrito` reconoce cada cita. Nunca «del Reglamento de Extranjería». Dos precauciones más, comprobadas con el verificador: las letras se citan «letra d) del artículo 127 del Real Decreto 1155/2024» o «letra b) del artículo 52.1 del Real Decreto 1155/2024» (con «artículo 127.d) del Real Decreto…» no enlaza la norma y atribuye el artículo a la última norma citada), y cuando en el mismo párrafo aparecen artículos de varias normas, nombra la norma detrás de cada artículo.

Estructura:

1. **Encabezamiento**: «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA] — [DELEGACIÓN / SUBDELEGACIÓN] DEL GOBIERNO» (art. 193.2).
2. **Comparecencia** con marcadores (`[NOMBRE Y APELLIDOS]`, `[PASAPORTE]`, `[NIE]`, `[DOMICILIO]`) y representación (art. 197.4).
3. **EXPONE — HECHOS**: PRIMERO.- Identidad y entrada (`[FECHA DE ENTRADA EN ESPAÑA]`). SEGUNDO.- Permanencia continuada por tramos. TERCERO.- Situación administrativa. CUARTO.- Antecedentes. QUINTO.- Formación: denominación, nivel, centro, modalidad, calendario de matrícula y situación actual. SEXTO.- Informe de integración.
4. **FUNDAMENTOS DE DERECHO**: I. Marco legal (art. 31.3 LOEX; arts. 124 y 125.1.d). II. Procedimiento y competencia (arts. 130, 193.2 y 197). III. Requisitos generales (art. 126). IV. Formación incluida en el art. 127.d por remisión al art. 52 (cita la letra exacta). V. Momento de la solicitud y prueba de la matrícula. VI. Informe de integración (art. 127.c). VII. Doctrina con párrafo literal y ECLI. VIII. Efectos y límite de trabajo (arts. 125.2 y 131.b).
5. **SOLICITA**: admisión a trámite y concesión por un año, con la habilitación para trabajar del art. 131.b.
6. **OTROSÍ**: que se tenga por solicitado el informe de integración en la fecha indicada y, si no se emite en plazo, por acreditada la integración con los documentos aportados; compromiso de acreditar la matrícula en tres meses desde la notificación (art. 127.d).
7. Lugar, fecha y firma.
8. **RELACIÓN DE DOCUMENTOS** numerada: impreso oficial; justificante de la tasa; pasaporte completo; prueba de permanencia por tramos; certificados de antecedentes (con la legalización o apostilla y traducción que exija la hoja informativa de la oficina); certificado del centro, preinscripción o matrícula; autorización e inscripción del centro; documento del compromiso con los servicios públicos de empleo, si procede; informe de integración o justificante de haberlo pedido; representación.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: LOEX 31; Reglamento 52, 124, 125, 126, 127, 130, 131, 132, 193 y 197 (y 75 si hay formación de empleo); fechas de vigencia y notas de nulidad revisadas.
- [ ] La formación coincide con una letra concreta del art. 127.d y del art. 52; si no, se ha dicho al abogado.
- [ ] Calculadas y comunicadas: fecha de cumplimiento de los dos años (art. 126.b; desde la firmeza de la denegación si pidió asilo), ventana de dos meses antes de la matrícula (art. 127.d), fin del mes del informe (art. 127.c).
- [ ] Si hay condenas, cálculo de cancelación del art. 136 CP (apartado 2 si hubo suspensión y remisión).
- [ ] Advertidos los efectos: tres meses para acreditar la matrícula, treinta horas de trabajo y requisitos de la prórroga.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; `verificar_escrito` pasado.
- [ ] Cada aviso de «posible disonancia de contenido» de `verificar_escrito` contrastado con el apartado exacto leído con `buscar_articulo` (el verificador compara con el título del artículo, p. ej. «Requisitos específicos» o «Procedimiento»): si el apartado dice lo que afirma el escrito, se mantiene la cita y se explica en el resumen; si no, se corrige.
- [ ] Marcadores para lo que falta; sin importes de tasa, códigos de modelo ni plazos de resolución no obtenidos del conector.
- [ ] Resumen para el abogado según el apartado 7 del formato, con cada fecha y su precepto (también subsanación, art. 130.3, y TIE, art. 130.6).
