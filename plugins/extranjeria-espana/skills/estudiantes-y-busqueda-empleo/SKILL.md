---
name: estudiantes-y-busqueda-empleo
description: >-
  Prepara en Word la solicitud de autorización de estancia de larga duración por estudios, movilidad de alumnos, voluntariado o actividades formativas (arts. 52-59 del Reglamento aprobado por el Real Decreto 1155/2024) y su visado (arts. 34-36), su prórroga, la de los familiares del estudiante, la autorización para trabajar y el paso a residencia y trabajo al terminar (art. 190), y orienta sobre los visados de búsqueda de empleo (arts. 43-45). Úsala cuando el abogado diga «visado de estudiante», «estancia por estudios», «prórroga de estudios», «máster en España», «puede trabajar el estudiante», «ha terminado el grado y tiene oferta» o «le denegaron el visado de estudios por medios». Si la persona está en situación irregular y quiere formarse, usa arraigo-socioformativo; si es ciudadano de la UE, ciudadanos-ue-y-familiares.
---

# Estudiantes, formación y búsqueda de empleo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Figura y requisitos** → `buscar_articulo` (`ley="LOEX"`, `articulo="33"`) y `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"52"`, `"53"` y `"35"`).
- **Visado o solicitud desde España, plazos y silencio** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"34"`, `"36"`, `"54"`, `"28"`, `"193"` y `"197"`) y, para calcular fechas, `buscar_articulo` (`ley="LPAC"`, artículos `"21"` y `"30"`).
- **Duración, prórroga y extinción** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"55"`, `"200"` y `"202"`).
- **Trabajo compatible, familiares, formación sanitaria y movilidad en la Unión** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"57"`, `"56"`, `"58"` y `"59"`).
- **Paso a residencia y trabajo** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"190"`, `"74"`, `"84"` y `"89"`).
- **Visados de búsqueda de empleo y búsqueda tras los estudios** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"43"`, `"44"` y `"45"`) y `buscar_articulo` (`ley="Directiva (UE) 2016/801"`, `articulo="25"`); la orden ministerial anual y la disposición adicional decimoséptima de la Ley 14/2013 se buscan con `buscar_boe` y `leer_boe` (ver «Requisitos»).
- **Doctrina sobre denegaciones de visado, medios, prórrogas y modificación** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"` para TSJ y juzgados, `base="TS"` para el Supremo) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Revisión del documento** → cada redactor del equipo pasa `verificar_escrito` solo sobre sus frases con normas, y el ensamblado rechaza cualquier ECLI o ROJ que ningún redactor leyera; `buscar_por_cita` se usa solo con un ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Dos precauciones más para que el verificador no se equivoque: la letra va después de la norma («la letra a) del artículo 52.1 del Real Decreto 1155/2024» o «artículo 52.1 del Real Decreto 1155/2024, letra a)»), nunca pegada al número («artículo 52.1.a)» o «52.1 a) del…» dejan la norma sin identificar o la atribuyen a otra ley); y cada mención de un artículo lleva su norma, también en títulos de fundamentos (si no, la atribuye a la última ley citada). En una cita literal que nombre un artículo sin su norma, añádela entre corchetes.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

## Cuándo usarla

- Primera autorización de estancia de larga duración para estudios superiores, secundaria postobligatoria, movilidad de alumnos, voluntariado o actividades formativas: por visado desde el extranjero o, en los casos permitidos, desde España.
- Prórroga anual, familiares del estudiante de estudios superiores, autorización para trabajar compatible.
- Paso a residencia y trabajo por cuenta ajena, por cuenta propia o con excepción de autorización de trabajo al terminar (art. 190).
- Orientación sobre visados de búsqueda de empleo (hijos o nietos de español de origen, ocupaciones y territorios).
- Nueva solicitud tras una denegación, o revisión de una preparada.

**Detector previo:**

| Situación | Figura o skill |
|---|---|
| Persona en situación irregular que estudia o va a matricularse | arraigo-socioformativo (art. 127.d) |
| Investigación o prácticas no laborales | movilidad-internacional-ley-14-2013 (el art. 52.3 las remite a la Ley 14/2013) |
| Ciudadano de la UE, del EEE o de Suiza que estudia | ciudadanos-ue-y-familiares (art. 7.1.c del Real Decreto 240/2007) |
| Quiere cambiar a otra autorización que no sea la del art. 190 o renovar una residencia | renovacion-modificacion-extincion |
| Cómputo del tiempo de estudios para la larga duración | larga-duracion (art. 176.a) |
| Ya hay denegación notificada y se quiere recurrir | visados-denegacion (visado) o recurso-administrativo-extranjeria y recurso-contencioso-extranjeria (autorización o prórroga) |

## Datos que hay que reunir antes de redactar

Los marcados con ★ son imprescindibles.

1. ★ Actividad exacta y su letra del art. 52.1: nivel de estudios, programa, centro y registro en el que figura (Registro de Universidades, Centros y Títulos, registro estatal de centros docentes no universitarios o Registro de Instituciones y Centros de Enseñanza Superior), matrícula abonada, modalidad (presencial, híbrida, semipresencial) y porcentaje de créditos matriculados.
2. ★ Fecha de inicio de la actividad y fecha prevista de presentación (antelación mínima de dos meses).
3. ★ Dónde está la persona: en su país (visado) o en España y con qué situación y hasta qué fecha (solo cabe desde España en los casos del art. 54.1).
4. ★ Edad (art. 35.f) y, si es menor, autorización de quienes ejercen la patria potestad o tutela (art. 35.g).
5. ★ Medios económicos (propios, beca, alojamiento pagado, toma a cargo) y familiares que le acompañarán; seguro de enfermedad; antecedentes penales de los cinco años anteriores; certificado médico.
6. Prórroga: fecha de caducidad, prórrogas ya concedidas, cursos superados y matrícula del siguiente; en idiomas, curso superado o diploma DELE; en formación sanitaria, presentación a las pruebas.
7. Trabajo: contrato u oferta, horas semanales, lugar (comunidad autónoma), prácticas curriculares.
8. Paso a residencia y trabajo: fecha de obtención del título o certificado, tipo de estudios, si fue becado por programas de cooperación o acción humanitaria (art. 190.1), oferta de empleo con sus condiciones, proyecto por cuenta propia o supuesto de excepción, familiares en estancia que conviven.
9. Representación del solicitante o, en su caso, del centro (art. 54.6).

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` antes de afirmarlo y respeta su redacción vigente. Si la respuesta trae una nota «Téngase en cuenta…» (nulidad declarada por el Tribunal Supremo o reforma), léela y aplícala: lo anulado no se aplica ni se cita como vigente. El art. 190 fue modificado por el Real Decreto 316/2026 (`leer_boe`, `identificador="BOE-A-2026-8284"`) y el art. 197.2 fue anulado: trabaja con la redacción que devuelva el conector, no con la de 2025.

**Actividades (art. 52).** Estudios superiores a tiempo completo en centro reconocido (mínimo el 90 % de los créditos, art. 52.2), con curso preparatorio y prácticas obligatorias incluidos; secundaria postobligatoria y FP de grado medio; movilidad de alumnos; voluntariado en entidad inscrita; y solo las actividades formativas enumeradas en el art. 52.1.e) (auxiliares de conversación, idiomas en centros acreditados, preparación de pruebas de formación sanitaria especializada, habilitación profesional, certificados profesionales de grado C niveles 2 y 3). En las modalidades no presenciales, comprueba el mínimo presencial que exige el art. 52.

**Requisitos (arts. 35 y 53).** Admisión y matrícula abonada según la actividad (art. 53.1); no ser amenaza para el orden público, con penados e informe policial (art. 53.2); tasa (art. 53.3). Para el visado, además, pasaporte con un año de vigencia, edad mínima, medios (100 % del IPREM al mes para el estudiante salvo alojamiento pagado, y los porcentajes para familiares del art. 35.h, sin computar el coste de los estudios), seguro con prestaciones similares a las del Sistema Nacional de Salud, antecedentes de cinco años si supera seis meses, no ser rechazable y certificado médico (art. 35). Jurisprudenciator no devuelve la cuantía del IPREM: pídesela al abogado de la fuente oficial.

**Procedimiento.**

| Vía | Dónde y cuándo | Plazos y silencio que debes leer |
|---|---|---|
| Visado (arts. 34-36) | Consulado, dos meses antes del inicio salvo causa justificada; la solicitud incluye la autorización | Oficina: siete días, silencio desfavorable; consulado: un mes (art. 36) |
| Desde España (arts. 54.1 y 54.3) | Titular de una autorización de residencia que esté en España (cualquier actividad); además, quien esté regularmente en España para estudios superiores o formación sanitaria especializada, o para habilitación profesional si su resolución lo prevé, siendo mayor de edad; dos meses antes del inicio y dos meses antes de que expire su situación | Dos meses, silencio desfavorable; la solicitud prorroga su situación legal |
| Por el centro (art. 54.6-54.7) | Centro inscrito en el Registro de Instituciones y Centros de Enseñanza Superior | Quince días, silencio desestimatorio |

- Denegación: requisitos no cumplidos, documentos falsos o mala fe, centro no reconocido (art. 54.8); el consulado puede denegar además por falta de convencimiento sobre identidad, documentos o motivos (art. 28.5.d), con motivación (art. 28.6).
- TIE en un mes si supera seis meses (arts. 34.3 y 54.9).

**Duración y prórroga (art. 55).** La autorización dura lo que la actividad, con el límite de un año, salvo estudios superiores (duración oficial); empieza un mes antes y se extiende quince días después. En estudios de varios cursos, acreditar cada año la matrícula. Prórroga: en los dos meses previos a la caducidad, o en los tres posteriores con posible sanción; mantiene la validez hasta resolver; **silencio desestimatorio al mes** (calcula la fecha desde la entrada en registro con los arts. 21.3.b y 30.4-30.5 LPAC); la prórroga dura el curso o la actividad, con el límite de un año; como máximo una prórroga en voluntariado y actividades formativas y dos en estudios superiores y secundaria; la movilidad de alumnos no figura entre los supuestos prorrogables del art. 55.3.

- **Requisitos de la prórroga (art. 55.3):** los del art. 53.1 **para el mismo supuesto** por el que se obtuvo la autorización (admisión y matrícula abonada), el del art. 53.2 (no ser amenaza: penados e informe policial) y las letras b), h) e i) del art. 35: **pasaporte con un año de vigencia**, medios y seguro. Solo en idiomas (art. 52.1.e 2.º: curso superado en la escuela oficial, o DELE obtenido o inscripción a su prueba, o diploma SIELE) y en la preparación de pruebas de formación sanitaria especializada (52.1.e 3.º: haberse presentado a ellas) exige el art. 55.5 un resultado del curso anterior.
- **Aprovechamiento y continuidad son doctrina del Reglamento anterior.** El art. 40 del Real Decreto 557/2011 exigía superar «las pruebas o requisitos pertinentes para la continuidad de sus estudios», y los TSJ siguen denegando con esa base prórrogas por falta de aprovechamiento o por **cambio a estudios sin relación** con los autorizados (los tratan como una autorización distinta). El art. 55.3 vigente no recoge esa exigencia, pero la Administración la sigue aplicando: si el cliente cambia de programa, alega el texto vigente y, además, la continuidad o complementariedad de la formación (mismo nivel, misma área) con documentos (planes de estudios, notas). Si los estudios nuevos no guardan relación con los anteriores, advierte del riesgo y valora la nueva autorización desde España (arts. 54.1 y 54.3, con sus dos meses de antelación).
- **Presentación:** el art. 55.4 exige presentarla por medios electrónicos, pero el Supremo anuló el art. 197.2, que incluía estas prórrogas en la obligación de relación electrónica: presenta por vía electrónica si el cliente puede y, si no, advierte al abogado de esa tensión y busca doctrina posterior antes de presentar en papel.

**Trabajo (art. 57).** Los estudios superiores habilitan automáticamente a trabajar por cuenta ajena o propia si es compatible; el resto necesita autorización (requisitos de los arts. 74 u 84 con las excepciones del art. 57.1). Límite general de treinta horas semanales, cuyo incumplimiento **extingue** la estancia; ámbito de la comunidad autónoma y localidades limítrofes; prácticas curriculares cubiertas. Con alta en la Seguridad Social se tiene por cumplido el seguro (art. 57.5).

**Familiares (art. 56).** Solo del estudiante de estudios superiores o de formación sanitaria especializada, con al menos noventa días de vigencia restante; cónyuge, pareja registrada o estable, hijos menores o mayores con necesidades de apoyo; medios, seguro, antecedentes; **no pueden trabajar**; los hijos nacidos en España obtienen estancia pidiéndola en seis meses.

**Extinción.** Causas comunes del art. 200.2 y específicas: pérdida del reconocimiento del centro (con derecho a terminar en otro, art. 55.6) y exceso de horas de trabajo (art. 57.2). Para alegaciones en un procedimiento de extinción, usa renovacion-modificacion-extincion.

**Paso a residencia y trabajo (art. 190).** Titulares por estudios superiores, secundaria postobligatoria o formaciones del art. 52.1.e) 4.º y 5.º (y formación sanitaria especializada) que han obtenido el título, sin beca de cooperación o acción humanitaria; sin visado. Por cuenta ajena, art. 74 salvo su apartado 1.a) (la presenta el empleador o el estudiante; la tasa la paga el empleador); por cuenta propia, art. 84; excepción de autorización de trabajo, art. 89.2. Plazo: dos meses antes o tres meses después de la extinción de la estancia o de la obtención del título (art. 190.6); **calcula las dos fechas** (art. 30.4 LPAC) y aconseja presentar antes de la primera que venza. Desde el Real Decreto 316/2026, la presentación en plazo prorroga la validez de la estancia anterior **hasta la notificación de la resolución**, aunque ya hubiera vencido: su preámbulo (`leer_boe`, `identificador="BOE-A-2026-8284"`) explica que la reforma quiso evitar el vacío entre el fin de la estancia y la admisión a trámite. Desde la admisión, autorización provisional de residencia y trabajo a jornada completa. Eficacia condicionada al alta en la Seguridad Social; un año de duración; TIE en un mes. Familiares en estancia que convivan: residencia por reagrupación si hay medios y vivienda adecuada.

- **Exclusión por beca:** solo excluye a quien fue becado en programas «de cooperación para el desarrollo sostenible o de acción humanitaria» (art. 190.1). El art. 199 del Real Decreto 557/2011 decía «programas de cooperación o de desarrollo» y exigía además aprovechamiento (y, en su redacción original, tres años de estancia): esa doctrina no se traslada sin advertirlo. Una beca de otro tipo (mérito, formación de posgrado de su país) no excluye; pide las bases del programa. Una cláusula de retorno de la beca no es el compromiso de no retorno del art. 74.1.g) (retorno voluntario desde España).
- **Titulación:** si solo hay certificado de finalización y resguardo del título, adviértelo como riesgo y pide requerimiento de subsanación para aportar el título.

**Búsqueda de empleo.**

- Visados de búsqueda de empleo (arts. 43-45): doce meses para buscar trabajo; al conseguir contrato, el empleador pide la autorización inicial (resolución en diez días) y la situación se prorroga. Número de visados, destinatarios y forma de solicitud dependen de la **orden ministerial anual de gestión colectiva de contrataciones en origen**. Búscala con `buscar_boe` (varía la consulta y el año); si no la localizas o no llega su texto con `leer_boe`, aplica la puerta: no des requisitos, cupos ni plazos de esos visados y explícale al abogado que falta esa orden.
- Búsqueda de empleo o emprendimiento tras estudios superiores de nivel 6 o superior (art. 190.10): el art. 190.10 remite a la **disposición adicional decimoséptima de la Ley 14/2013**, que `buscar_articulo` no devuelve. Si el cliente necesita esa autorización, detén la redacción de ese apartado y dile al abogado que falta ese precepto; puedes indicarle, como referencia leída, el art. 25 de la Directiva (UE) 2016/801.

**Documentos por trámite (compruébalos en el artículo leído).**

- Visado o autorización inicial: impreso, pasaporte con un año de vigencia, admisión y matrícula abonada, prueba de medios y de seguro, antecedentes de los países de residencia de cinco años, certificado médico y, si es menor, autorización de sus representantes (arts. 35 y 53).
- Prórroga: matrícula abonada del nuevo curso o continuidad de la actividad, pasaporte con un año de vigencia, medios y seguro actualizados (arts. 55.3, 53.1 y 35 b, h, i); superación del curso solo en idiomas y formación sanitaria especializada (art. 55.5); si cambia de programa, planes de estudios y notas que muestren la continuidad.
- Familiar: vínculo, medios de la unidad, seguro y antecedentes (art. 56.3).
- Modificación: título o certificado obtenido, y la documentación del art. 74, 84 u 89.2 según la autorización pedida (art. 190).

**Causas típicas de denegación y respuesta.**

| Causa | Respuesta |
|---|---|
| Medios no acreditados o de origen dudoso | Extractos con saldo estable, beca o toma a cargo por escrito, alojamiento pagado (art. 35.h); explica el origen de los fondos |
| Consulado no convencido de la finalidad (art. 28.5.d) | Coherencia entre trayectoria académica, estudios elegidos y plan posterior; motivación exigible (art. 28.6) |
| Centro no reconocido o programa no a tiempo completo | Certificado de inscripción del centro y matrícula de al menos el 90 % de los créditos (art. 52) |
| Presentación sin la antelación de dos meses | Causa justificada o calendario de matrícula que impedía antes (arts. 36.1 y 54.2) |
| Prórroga sin aprovechamiento o para estudios distintos (doctrina del art. 40 del Real Decreto 557/2011) | El art. 55.3 vigente no lo exige salvo idiomas y formación sanitaria (art. 55.5): alégalo, y aporta notas, matrícula y la continuidad o complementariedad con los estudios autorizados |
| Seguro con copagos o carencias | Póliza con prestaciones similares a las del Sistema Nacional de Salud; pide subsanación antes de resolver |

## Estrategia y jurisprudencia

1. Comprueba la antelación de dos meses antes que nada: fuera de plazo, justifica la causa o valora esperar al curso siguiente.
2. En denegaciones por medios, prepara prueba de disponibilidad efectiva y de origen de los fondos; el consulado deniega a menudo por falta de convencimiento, así que la memoria debe responder a esa duda con documentos.
3. Para trabajar durante los estudios, confirma que el contrato respeta las treinta horas y el ámbito territorial: su incumplimiento extingue la estancia.
4. Consultas (reformula como máximo dos veces):
   - Visado y medios: `buscar_sentencias` (`consulta="visado de estudios denegación medios económicos oficina consular convencimiento"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="20/05/2025"`).
   - Prórroga: `consulta="prórroga estancia por estudios denegación aprovechamiento superación del curso"` y `consulta="prórroga estancia por estudios seguro de enfermedad subsanación"`, `base="AN"`.
   - Antecedentes en estancia por estudios: `consulta="estancia por estudios antecedentes penales ponderación"`, `base="TS"`.
   - Paso a residencia y trabajo: `consulta="extranjería estancia por estudios modificación residencia y trabajo titulación artículo 190"`, `base="AN"`, `fecha_desde="20/05/2025"`; si da resultados de otras materias, añade «extranjería» y el nombre de la autorización.
5. Buena parte de la doctrina interpreta el Real Decreto 557/2011 (arts. 37 a 44 y 199). Úsala para requisitos que se mantienen (medios, seguro, antecedentes) y dilo en el escrito. El aprovechamiento y la continuidad del antiguo art. 40, y los tres años, el aprovechamiento y la beca «de desarrollo» del antiguo art. 199, no figuran igual en los arts. 55.3 y 190 vigentes: si citas esa doctrina, es para anticipar el criterio de la Administración o para distinguir el caso, advirtiendo del cambio normativo.
6. **Si no hay doctrina sobre el precepto vigente** (lo normal con el art. 190 reformado en 2026): haz la consulta de la lista y sus dos reformulaciones; si ninguna sentencia es aplicable, en una **solicitud** redacta sin el fundamento de doctrina y di en el resumen qué consultas hiciste y por qué no citas nada. No es causa de detención, porque la solicitud se apoya en el texto del artículo; sí lo sería en un escrito que dependa de esa doctrina. Nunca rellenes el hueco con sentencias del régimen anterior que exigían otros requisitos.

## Documento que se entrega

Word maquetado según `references/formato-y-organos.md`, que acompaña al impreso oficial vigente (no lo sustituye). Sin importes de tasas ni códigos de modelos.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» y el resto de normas como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca.

Nombre según el trámite: `solicitud-estancia-estudios-<apellido-cliente>-<AAAAMMDD>.docx`, `solicitud-prorroga-estudios-<apellido-cliente>-<AAAAMMDD>.docx`, `solicitud-familiar-estudiante-<apellido-cliente>-<AAAAMMDD>.docx` o `solicitud-modificacion-estudios-trabajo-<apellido-cliente>-<AAAAMMDD>.docx`.

1. Encabezamiento: «A LA OFICINA CONSULAR DE ESPAÑA EN [CIUDAD]» (visado) o «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA]» (desde España, prórroga y modificación; provincia de inicio de la actividad o la de la autorización inicial, según el artículo leído).
2. Comparecencia: `[NOMBRE Y APELLIDOS]`, `[PASAPORTE]`, `[NIE]`, `[DOMICILIO]`; representante o centro presentador y su título.
3. EXPONE — HECHOS: PRIMERO, identidad y situación actual; SEGUNDO, actividad, centro y su reconocimiento; TERCERO, admisión, matrícula y calendario; CUARTO, medios y seguro; QUINTO, antecedentes; SEXTO, según el trámite: cursos superados (prórroga), vínculo y medios (familiar), título obtenido y oferta o proyecto (modificación).
4. FUNDAMENTOS DE DERECHO: I, figura (LOEX, art. 33; Reglamento, art. 52); II, vía y plazo de presentación; III, requisitos (arts. 35 y 53, o 55, 56 o 190 según el trámite; en el art. 190, también los del art. 74, 84 u 89.2 a los que remite); IV, doctrina con párrafo literal y ECLI, si la hay aplicable (si no, omítelo según el punto 6 de «Estrategia»); V, efectos pedidos (duración, trabajo, autorización provisional del art. 190.7).
5. SOLICITA la concesión con el alcance que corresponda.
6. OTROSÍ: que se haga constar la autorización provisional para trabajar a jornada completa (art. 190.7) o, en la prórroga, que se tenga por prorrogada la validez hasta resolver.
7. Lugar, fecha, firma y RELACIÓN DE DOCUMENTOS numerada.

**Reparto para la redacción rápida:** 01 encabezamiento, comparecencia y hechos; 02 fundamentos: figura, vía y plazo de presentación; 03 fundamentos: requisitos del trámite con su doctrina, si la hay; 04 efectos pedidos, solicita, otrosí, firma y relación de documentos. Una prórroga sencilla (una o dos páginas) la redacta el director sin equipo.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado; si el caso dependía de la orden ministerial o de la disposición adicional de la Ley 14/2013 y no se obtuvieron, esa parte se detuvo y se explicó.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos citados (33 LOEX; 34-36, 52-59, 190 y 200 del Reglamento y los que se usen).
- [ ] Antelación de dos meses comprobada; fecha límite de prórroga o modificación calculada con su precepto (en el art. 190, las dos fechas: desde la extinción y desde la titulación); fecha del silencio de la prórroga calculada.
- [ ] Límite de horas y ámbito territorial del trabajo revisados.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre sus frases con normas y corregido lo que señale.
- [ ] Marcadores para lo que falta; cuantía del IPREM confirmada por el abogado.
- [ ] Resumen para el abogado según el apartado 7 del formato: trámite y órgano, plazos con fecha y precepto, documentos que faltan y riesgos, tabla de jurisprudencia y próximo paso.
