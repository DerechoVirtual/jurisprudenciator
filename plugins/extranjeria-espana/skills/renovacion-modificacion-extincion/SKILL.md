---
name: renovacion-modificacion-extincion
description: >-
  Prepara en Word la solicitud de renovación o prórroga de una autorización temporal (cada figura con su artículo: 64, 71, 80, 86, 95.4, 112, 132 del Reglamento aprobado por el Real Decreto 1155/2024), la de modificación de situación (arts. 190-192), el escrito que hace valer una renovación estimada por silencio y las alegaciones contra un procedimiento de extinción (arts. 199-203). Úsala cuando el abogado diga «le caduca la tarjeta», «renovar el permiso», «presentó la renovación tarde», «no le contestan la renovación», «pasar de residencia a residencia y trabajo», «cambiar de cuenta ajena a propia» o «le han abierto un expediente de extinción». Para la larga duración usa larga-duracion; para la prórroga o el paso a trabajo del estudiante, estudiantes-y-busqueda-empleo; para la tarjeta comunitaria, ciudadanos-ue-y-familiares.
---

# Renovación, modificación y extinción de autorizaciones

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Renovación o prórroga de la figura concreta** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, el artículo de la tabla de «Requisitos»: `"64"`, `"71"`, `"80"`, `"81"`, `"86"`, `"87"`, `"95"`, `"112"`, `"132"` o `"55"`) y `buscar_articulo` (`ley="LOEX"`, artículos `"31"` y `"52"`).
- **Modificaciones de situación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"190"`, `"191"` y `"192"`, y los de requisitos a los que remiten: `"74"`, `"84"` y `"89"`).
- **Extinción** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"199"`, `"200"`, `"201"`, `"202"` y `"203"`) y `buscar_articulo` (`ley="LOEX"`, `articulo="57"` si hay expulsión).
- **Procedimiento, silencio y cómputo** → `buscar_articulo` (`ley="LPAC"`, artículos `"21"`, `"22"` (suspensión del plazo para resolver), `"24"`, `"25"` (caducidad de los procedimientos de oficio), `"30"`, `"68"`, `"82"` y `"124"` (plazo de la reposición)) y `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"193"` y `"197"`).
- **Alternativa si la renovación ya no es posible** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"126"` y `"127"`: arraigo de segunda oportunidad).
- **Doctrina sobre silencio, plazo, antecedentes, requisitos de cada renovación y extinción** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"` o `base="AN"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Revisión del documento** → cada redactor del equipo pasa `verificar_escrito` solo sobre sus frases con normas, y el ensamblado rechaza cualquier ECLI o ROJ que ningún redactor leyera; `buscar_por_cita` se usa solo con un ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). La letra va detrás de la norma («la letra b) del artículo 52 de la Ley Orgánica 4/2000», «artículo 80.2 del Real Decreto 1155/2024, letra b)»), nunca pegada al número («52.b) de la…» se atribuye a otra norma), y cada mención de un artículo lleva su norma; en una cita literal que nombre un artículo sin norma (o con «la Ley Orgánica» o «el Reglamento» a secas), añádela entre corchetes.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

## Cuándo usarla

- Renovar o prorrogar una autorización temporal antes de que caduque o en los tres meses siguientes.
- Hacer valer una renovación estimada por silencio o reaccionar ante una denegación dictada después del silencio.
- Modificar la situación: de residencia a residencia y trabajo (art. 191), del familiar que deja de serlo (art. 191.8), cambio de ocupación, sector o territorio en el primer año o de cuenta ajena a cuenta propia (art. 192).
- Alegaciones en el trámite de audiencia de un procedimiento de extinción.

**Detector previo:**

| Situación | Skill |
|---|---|
| Larga duración: concesión, recuperación o tarjeta | larga-duracion |
| Prórroga de estancia por estudios o paso a trabajo al terminar | estudiantes-y-busqueda-empleo (aquí solo si el abogado lo pide junto con otro trámite) |
| Tarjeta de familiar de ciudadano de la Unión | ciudadanos-ue-y-familiares |
| Residencia independiente del familiar de español | familiares-de-espanoles |
| Han pasado más de tres meses desde la caducidad | Ya no hay renovación: valora arraigo-segunda-oportunidad (art. 127.a) u otra autorización inicial |
| Denegación o extinción ya resuelta | recurso-administrativo-extranjeria o recurso-contencioso-extranjeria (la extinción agota la vía administrativa, art. 202.4) |

## Datos que hay que reunir antes de redactar

Los marcados con ★ son imprescindibles.

1. ★ Tipo exacto de autorización (el que figura en la resolución y en la TIE), fecha de concesión, fecha de caducidad y renovaciones anteriores.
2. ★ Fecha de presentación (hecha o prevista) y, si ya se presentó, número de expediente y si hubo requerimiento.
3. ★ Datos de la figura: contratos, altas y periodos cotizados, inscripción como demandante de empleo, prestación por cese de actividad (trabajo); medios, seguro y días de residencia efectiva en el año (no lucrativa); situación del reagrupante y del vínculo (reagrupación); búsqueda activa de empleo o promoción de curso (circunstancias excepcionales); situación del familiar español (art. 95.4).
4. ★ Antecedentes penales (condena, pena, cumplimiento, suspensión, indulto, cancelación), obligaciones tributarias y de Seguridad Social, hijos en edad de escolarización obligatoria.
5. Informe de esfuerzo de integración de la comunidad autónoma: si se ha pedido, cuándo y su sentido.
6. Modificación: tiempo en residencia, si la autorización actual habilitaba a trabajar, oferta o contrato con sus condiciones o proyecto por cuenta propia, y por qué la actual no sirve.
7. ★ Extinción: fecha de notificación del acuerdo de incoación, causa invocada, plazo de audiencia concedido, si la autorización seguía vigente al incoarse y circunstancias personales (años en España, familia, trabajo, arraigo).
8. Representación.

## Requisitos y comprobaciones

Lee con `buscar_articulo` el artículo propio de la figura antes de afirmar un requisito, un plazo o el sentido del silencio. La tabla dice dónde mirar; su contenido se comprueba siempre en el texto leído. Si la respuesta trae una nota «Téngase en cuenta…» (nulidad declarada por el Tribunal Supremo o reforma), léela y aplícala: lo anulado no se aplica ni se cita como vigente. Los arts. 132, 190 y 191 fueron modificados por el Real Decreto 316/2026 (`leer_boe`, `identificador="BOE-A-2026-8284"`): usa la redacción vigente que devuelva el conector.

| Autorización | Artículos | Silencio que dice el propio artículo | Duración de la renovada |
|---|---|---|---|
| Residencia no lucrativa | 64 | Estimatorio a los tres meses (64.8) | Dos años (64.7) |
| Reagrupación familiar | 71 | Estimatorio a los tres meses (71.5) | Cuatro años (71.6) |
| Residencia y trabajo por cuenta ajena | 80 y 81 | Estimatorio a los tres meses (80.9) | Cuatro años, efectos desde el día siguiente a la caducidad (81.1) |
| Residencia y trabajo por cuenta propia | 86 y 87 | Favorable a los tres meses (87.2) | Cuatro años, efectos desde el día siguiente a la caducidad (87.1) |
| Familiar de persona española | 95.4 | No lo dice | Cinco años o el periodo de residencia del español |
| Actividades de temporada | 112 | Estimatorio al mes (112.2) | Cuatro años (112.1) |
| Circunstancias excepcionales (prórroga) | 132 | No lo dice | Un año; cinco en arraigo familiar (132.1) |
| Estancia por estudios (prórroga) | 55 | **Desestimatorio** al mes (55.4) | Hasta un año (55.5) |

**Plazo y prórroga de la vigencia.** En todas las renovaciones y prórrogas de la tabla (salvo temporada, que tiene su propio régimen en el art. 112): en los **dos meses anteriores** a la caducidad; también en los **tres meses posteriores**, sin perjuicio de la infracción leve del art. 52.b) LOEX. Presentada en plazo, la autorización anterior se prorroga hasta que se resuelva (art. 200.1 y el artículo de la figura). Calcula las fechas con el art. 30.4 LPAC (meses de fecha a fecha) y el 30.5 (último día inhábil). Si ya han pasado los tres meses, la autorización se extinguió por el transcurso del tiempo: no redactes una renovación y explícale al abogado las alternativas.

**Requisitos de cada renovación.** Resúmelos del artículo leído. Por ejemplo, cuenta ajena: continuidad del contrato; o tres meses de actividad por año más un nuevo contrato «acorde con las características de su autorización» (con alta al solicitar, o condicionado a la renovación) o la extinción del anterior por causa ajena a su voluntad con inscripción ininterrumpida como demandante de empleo **hasta la fecha de la solicitud** (si ya trabaja de nuevo, ese supuesto no encaja: usa el del nuevo contrato); o nueve meses de alta en doce, o reagrupación posible por un familiar, o violencia de género o sexual (art. 80.2); no lucrativa: medios del art. 62, seguro, escolarización y más de ciento ochenta y tres días de residencia efectiva en el año natural (art. 64.2); prórroga de arraigo: búsqueda activa de empleo e inscripción, salvo impedimento justificado (art. 132.2.a).

**Valoraciones comunes (LOEX, art. 31.7).** Los antecedentes penales, el cumplimiento de obligaciones tributarias y de Seguridad Social y el esfuerzo de integración **se valoran**, no deniegan automáticamente: condenas cumplidas, indultadas, suspendidas o en remisión condicional se ponderan (arts. 64.5, 71.3.c, 80.5 y 86.5). Los descubiertos de cotización no impiden renovar si hay actividad habitual (arts. 80.7 y 86.2.a). Si falta la escolarización de un menor, la oficina advierte y concede un mes (arts. 64.4, 71.4.c, 80.4 y 86.4). El informe de integración de la comunidad autónoma sirve precisamente cuando falta algún requisito; si no se emite en un mes, se prueba por otros medios.

**Silencio.**

- Donde el artículo lo fija, aplícalo y calcula la fecha desde la entrada de la solicitud en el registro del órgano competente (art. 21.3.b LPAC). Si la renovación quedó estimada, la resolución expresa posterior solo puede ser confirmatoria (art. 24.3.a LPAC) y el acto presunto se acredita por cualquier medio, incluido el certificado del art. 24.4 LPAC (quince días).
- **Requerimientos durante la tramitación:** el plazo para resolver «se podrá suspender» solo por el tiempo entre la notificación del requerimiento y su cumplimiento (art. 22.1.a LPAC); no se reinicia. Calcula la fecha del silencio sin suspensión y con la suspensión máxima, y di en el escrito que en ambos casos ha vencido (o cuándo vencerá).
- **Tasa:** hay doctrina que retrasa el inicio del cómputo hasta el pago de la tasa cuando se abonó después de la solicitud (por ejemplo, STSJ Andalucía 9781/2026, con el Reglamento anterior; léela con `leer_sentencias` antes de citarla). Comprueba la fecha del pago y acredítala.
- Si ya llegó una denegación expresa posterior al silencio, además del escrito C hay que recurrirla (reposición en un mes, art. 124 LPAC, o contencioso): usa recurso-administrativo-extranjeria.
- Donde el artículo no lo dice (arts. 95.4, 132 y 191), la regla está en la disposición adicional primera de la LOEX y en la octava del Reglamento, que `buscar_articulo` no devuelve. Obtén la doctrina con `buscar_sentencias` (`consulta="silencio positivo renovación autorización residencia disposición adicional primera Ley Orgánica 4/2000"`, `base="AN"` y después `base="TS"`) y cítala con su párrafo literal. Si no la obtienes, no afirmes el sentido del silencio y díselo al abogado.

**Modificaciones.**

- Art. 191: desde residencia temporal a residencia y trabajo sin visado. Menos de un año de residencia: todos los requisitos del art. 74 y autorización inicial de un año (191.2). Un año o más y la actual ya habilitaba a trabajar: requisitos de renovación (arts. 80 u 86) y cuatro años con efectos retroactivos (191.3). Un año o más y no habilitaba: art. 74 salvo su apartado 1.a) u 84, un año, eficacia condicionada al alta en un mes (191.4). La presenta el empleador o el extranjero (191.5). Exclusiones del art. 191.7 en su redacción vigente, que ha cambiado en 2026: léela siempre. Familiar de ciudadano de la Unión o de español que deja de serlo: 191.8.
- Art. 192: en el primer año, cambio de ocupación, sector o ámbito territorial (con situación nacional de empleo si es por cuenta ajena; un mes, silencio estimatorio) y paso de cuenta ajena a cuenta propia sin ampliar la vigencia.
- Presenta la modificación mientras la autorización esté vigente o en el plazo que prorroga su validez (art. 200.1).

**Extinción.**

- Por el transcurso del tiempo, sin resolución (art. 200.1), salvo que se haya pedido en plazo la prórroga, renovación o modificación.
- Por resolución, en los casos del art. 200.2 (prohibición de entrada, fraude, fines distintos, pérdida de requisitos salvo previsión en contrario, cambio de nacionalidad, falta de pasaporte, orden público, condena por los arts. 177 bis o 318 bis CP y causas propias de cada figura); la expulsión extingue siempre (art. 200.3). Larga duración: art. 201.
- Procedimiento (art. 202): **incoación de oficio durante la vigencia** de la autorización; audiencia no inferior a diez días; resolución y notificación en **seis meses** desde la notificación del acuerdo de incoación, con **caducidad** si no; decisión proporcionada, atendiendo a las circunstancias y a los intereses del trabajador; pone fin a la vía administrativa (reposición potestativa o contencioso). Efectos desde que se dicta (art. 203).

**Causas típicas de denegación de la renovación y respuesta.**

| Causa | Respuesta |
|---|---|
| Presentada fuera de plazo | Si está dentro de los tres meses posteriores, la renovación es admisible con la infracción leve del art. 52.b) LOEX; más allá, busca otra figura |
| Relación laboral extinguida | Supuestos alternativos del art. 80.2 (nuevo contrato, demandante de empleo ininterrumpido, nueve de doce meses, familiar que podría reagrupar) |
| Actividad por cuenta propia sin continuidad | Cese de actividad reconocido, reagrupación posible por un familiar, autónomo dependiente (art. 86.2) |
| Medios insuficientes o menos de ciento ochenta y tres días en España (no lucrativa) | Prueba de medios del art. 62 y de residencia efectiva; informe de integración (art. 64.6) |
| Antecedentes penales o incumplimientos tributarios | Valoración, no automatismo (LOEX, art. 31.7); cumplimiento, suspensión o cancelación de la pena |
| Resolución denegatoria dictada tras vencer el plazo con silencio estimatorio | Solo cabía confirmar (art. 24.3.a LPAC): escrito C y, en su caso, recurso |

**Causas típicas de extinción y alegación.**

| Causa invocada | Alegación |
|---|---|
| Pérdida de requisitos (art. 200.2.d) | Supuesto alternativo de la propia figura; la regulación de la figura puede disponer otra cosa |
| Fines distintos (art. 200.2.c) | Prueba de la actividad autorizada |
| Orden público (art. 200.2.g) | Gravedad, tipo de infracción, peligro actual, duración de la residencia y vínculos en España |
| Fraude o documentos falsos (art. 200.2.b) | Carga de la prueba de la Administración; autenticidad y buena fe |
| Incoación con la autorización ya caducada | El art. 202.1 exige incoar durante la vigencia |
| Orden público por una condena que la Administración ya valoró al renovar después | La renovación exigía ponderar esos antecedentes (LOEX, art. 31.7; art. 80.5): sin hechos nuevos, la extinción contradice esa ponderación |
| Más de seis meses desde la notificación de la incoación | Caducidad del procedimiento (art. 202.2) |

## Estrategia y jurisprudencia

1. Calcula primero las fechas (caducidad, dos meses antes, tres meses después, fecha del silencio, caducidad del procedimiento de extinción) y ponlas en el resumen: deciden la estrategia.
2. Si falta un requisito de la renovación, busca el supuesto alternativo del mismo artículo y refuérzalo con el informe de integración; si ninguno encaja, valora la modificación del art. 191 o la autorización inicial que corresponda.
3. En la extinción, articula las alegaciones por este orden: caducidad del procedimiento; incoación fuera de la vigencia; falta de prueba de la causa; proporcionalidad (art. 202.3) con los vínculos y la trayectoria; efectos solo hacia el futuro (art. 203).
4. Consultas (reformula como máximo dos veces):
   - Silencio: `buscar_sentencias` (`consulta="renovación autorización residencia silencio positivo resolución expresa posterior"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`).
   - Presentación en los tres meses posteriores: `consulta="renovación autorización residencia presentada tres meses posteriores caducidad prórroga de la vigencia"`, `base="AN"`.
   - Antecedentes en la renovación: `consulta="renovación autorización residencia antecedentes penales condena cumplida ponderación"`, `base="TS"`.
   - Requisitos de trabajo: `consulta="renovación autorización residencia trabajo cuenta ajena periodo de actividad demandante de empleo"`, `base="AN"`.
   - Extinción: `consulta="extinción autorización de residencia transcurso del plazo de vigencia incumplimiento de requisitos"`, `base="TS"`, y `consulta="extinción autorización de residencia audiencia caducidad proporcionalidad"`, `base="AN"`, `fecha_desde="20/05/2025"`; si la causa es el orden público, usa también la de antecedentes en la renovación (`base="TS"`), que da la doctrina de la ponderación.
   - Suspensión del plazo y silencio: `consulta="silencio positivo renovación autorización residencia suspensión plazo requerimiento documentación"`, `base="AN"`.
   - Modificación: `consulta="modificación autorización de residencia a residencia y trabajo artículo 191"`, `base="AN"`, `fecha_desde="20/05/2025"`.
5. Buena parte de la doctrina interpreta el Real Decreto 557/2011 (renovaciones de sus arts. 51, 61, 71 y 109, extinción del art. 162). El Supremo declaró con esa norma que la extinción por transcurso del plazo y la extinción por resolución se excluyen entre sí; el art. 202.1 vigente exige además incoar durante la vigencia. Cita esa doctrina indicando la norma que interpretaba.
6. **Comprueba que el párrafo citado es razonamiento de la Sala** y no alegaciones de parte, la resolución recurrida o la sentencia de instancia. Cuando la Sala transcribe doctrina del Supremo, atribúyela así («que recoge la doctrina del Tribunal Supremo…») y cita el ECLI de la sentencia leída. En una solicitud, si ninguna sentencia es aplicable, redacta sin ese fundamento y explícalo en el resumen.

## Documento que se entrega

Word maquetado según `references/formato-y-organos.md`. Las solicitudes acompañan al impreso oficial vigente (no lo sustituyen); sin importes de tasas ni códigos de modelos.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» y el resto de normas como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca.

**A) Solicitud de renovación o prórroga** — `solicitud-renovacion-<tipo>-<apellido-cliente>-<AAAAMMDD>.docx`. Encabezamiento a la oficina de extranjería de la provincia (arts. 193 y 197); comparecencia con `[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[DOMICILIO]` y representación; HECHOS: autorización y caducidad, presentación en plazo, requisito o supuesto que se cumple, valoraciones (antecedentes, obligaciones, integración, escolarización); FUNDAMENTOS: artículo de la figura, plazo y prórroga de la vigencia, supuesto alegado, doctrina; SOLICITA la renovación por el tiempo del artículo; OTROSÍ: prórroga de la vigencia hasta resolver y requerimiento previo si falta algún documento; RELACIÓN DE DOCUMENTOS.

**B) Solicitud de modificación** — `solicitud-modificacion-<apellido-cliente>-<AAAAMMDD>.docx`. Misma estructura, con un fundamento que encaje el caso en el apartado exacto del art. 191 o 192 y otro sobre la duración y los efectos pedidos.

**C) Escrito que hace valer el silencio** — `escrito-silencio-renovacion-<apellido-cliente>-<AAAAMMDD>.docx`. HECHOS: fecha de presentación, plazo del artículo y fecha en que venció sin notificación; FUNDAMENTOS: artículo de la figura y art. 24 LPAC; SOLICITA el certificado acreditativo del silencio y la expedición de la TIE, y que se deje sin efecto cualquier resolución expresa posterior no confirmatoria.

**D) Alegaciones en el procedimiento de extinción** — `alegaciones-extincion-<apellido-cliente>-<AAAAMMDD>.docx`. Encabezamiento al órgano que incoó, con el número de expediente `[NÚMERO DE EXPEDIENTE]`; HECHOS: autorización y vigencia, acuerdo de incoación y su notificación, circunstancias personales; ALEGACIONES numeradas con el orden del apartado de estrategia; SOLICITA el archivo o la no declaración de extinción y, en su caso, la declaración de caducidad; OTROSÍ: prueba propuesta; RELACIÓN DE DOCUMENTOS.

**Reparto para la redacción rápida:** A y B: 01 encabezamiento, comparecencia y hechos; 02 fundamentos y doctrina; 03 solicita, otrosí, firma y relación de documentos. C (silencio), de una o dos páginas: el director sin equipo. D: 01 encabezamiento y hechos; una sección por alegación, en el orden del apartado de estrategia; cierre con solicita, prueba y documentos.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leído con `buscar_articulo` en esta conversación el artículo de la figura concreta y los demás citados (LOEX 31 y 52; Reglamento 190-192 y 199-203; LPAC 24 y 30).
- [ ] Fechas calculadas y escritas con su precepto: caducidad, ventana de dos meses antes y tres después, vencimiento del silencio (con y sin la suspensión del art. 22.1.a LPAC si hubo requerimiento), audiencia (días hábiles) y caducidad de la extinción (art. 202.2; art. 25.1.b LPAC).
- [ ] Sentido del silencio afirmado solo si lo dice el artículo leído o la doctrina obtenida con Jurisprudenciator.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; doctrina del Reglamento anterior identificada como tal.
- [ ] `verificar_escrito` pasado por cada redactor sobre sus frases con normas y corregido lo que señale.
- [ ] Marcadores para lo que falta (`[NÚMERO DE EXPEDIENTE]`, `[NIE]`, fechas no facilitadas); sin importes.
- [ ] Resumen para el abogado según el apartado 7 del formato: qué se ha preparado y para qué órgano, plazos con fecha y precepto, documentos que faltan y riesgos, tabla de jurisprudencia y próximo paso.
