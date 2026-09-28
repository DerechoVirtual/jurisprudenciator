---
name: canal-denuncias-informantes
description: >-
  Diseña o revisa el Sistema interno de información de la Ley 2/2023: quién está obligado (50 o más
  trabajadores y sectores del anexo de la Directiva), política, procedimiento de gestión, Responsable del
  Sistema y su notificación a la Autoridad Independiente, canal escrito, verbal y anónimo, plazos, libro-registro,
  protección de datos y protección frente a represalias. Úsala cuando digan «canal de denuncias», «canal
  ético», «whistleblowing», «Ley 2/2023», «responsable del sistema», «nos piden el canal» o «me han
  represaliado por denunciar». Sirve a la empresa y al informante o al denunciado. Entrega procedimiento y
  política en Word y nota. Para instruir un acoso usa protocolo-acoso-laboral; para demandar un despido por
  represalia, redactar-demanda-despido; para la tutela sin despido, tutela-derechos-fundamentales.
---

# Canal de denuncias: Sistema interno de información (Ley 2/2023)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Ámbito material y personal, y entidades obligadas** → `buscar_articulo` (`ley="BOE-A-2023-4513"`, artículos `"2"`, `"3"`, `"10"`, `"11"` y `"12"`).
- **Sistema interno, gestión por tercero, canal, Responsable del Sistema y procedimiento** → `buscar_articulo` (`ley="BOE-A-2023-4513"`, artículos `"4"` a `"9"`).
- **Información pública del canal y libro-registro** → `buscar_articulo` (`ley="BOE-A-2023-4513"`, artículos `"25"` y `"26"`).
- **Protección de datos y confidencialidad** → `buscar_articulo` (`ley="BOE-A-2023-4513"`, artículos `"29"` a `"33"`) y (`ley="LOPDGDD"`, `articulo="24"`); los artículos del RGPD que se citen, con `ley="RGPD"`.
- **Protección del informante y del afectado** → `buscar_articulo` (`ley="BOE-A-2023-4513"`, artículos `"35"` a `"40"`); nulidad del despido lesivo de derechos fundamentales → (`ley="ET"`, `articulo="55"`).
- **Régimen sancionador** → `buscar_articulo` (`ley="BOE-A-2023-4513"`, artículos `"61"` a `"66"`); las multas, del artículo `"65"` en el momento, sin escribirlas de memoria.
- **Doctrina sobre represalias, garantía de indemnidad y uso de denuncias internas como prueba** → `buscar_sentencias` (`base="AN"`, `jurisdiccion="SOCIAL"`, `tipo_organo="TSJ"`; y `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`).
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

Pregunta primero a quién asesora el abogado:

- **Empresa o entidad privada**: saber si está obligada, implantar o revisar el Sistema (política, procedimiento, Responsable, canal, registro), externalizar la recepción, compartir medios o adaptar el sistema de un grupo.
- **Informante**: valorar si su comunicación está protegida y si una medida posterior es represalia.
- **Persona afectada por una comunicación**: comprobar si se respetaron su presunción de inocencia, su derecho a ser informada y oída y la confidencialidad.

Esta skill no cubre el sector público ni el canal externo de la Autoridad Independiente más allá de informar sobre él.

| Si lo que se necesita es… | Usa |
|---|---|
| Instruir una denuncia de acoso o redactar el protocolo | `protocolo-acoso-laboral` |
| Despido de un informante (demanda de nulidad) | `papeleta-conciliacion` y `redactar-demanda-despido` |
| Otra represalia sin despido (sanción, traslado, degradación) | `tutela-derechos-fundamentales` o `sanciones-disciplinarias` |
| Sancionar a un trabajador tras una investigación | `sanciones-disciplinarias` o `carta-despido-disciplinario` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ Forma jurídica, actividad y plantilla (número de trabajadores contratados), si opera en servicios financieros, prevención del blanqueo, seguridad del transporte o medio ambiente, y si recibe o gestiona fondos públicos.
2. ★ Si forma parte de un grupo (art. 42 del Código de Comercio) y qué quiere hacer la dominante; si quiere compartir el sistema con otras empresas.
3. ★ Órgano de administración (consejo, administrador único, solidarios o mancomunados): es quien implanta el sistema, aprueba el procedimiento y nombra al Responsable.
4. ★ Representación legal de los trabajadores (hay que consultarla antes de implantar) y fecha de la consulta.
5. ★ Quién será el Responsable del Sistema (persona u órgano colegiado), su cargo, independencia y posibles conflictos de interés; si existe una función de cumplimiento normativo.
6. Gestión interna o por tercero externo (contrato de encargo de tratamiento), herramienta de recepción, canal verbal, página web.
7. Canales o protocolos que ya existan (acoso, cumplimiento penal, calidad) que haya que integrar.
8. Comunidad autónoma donde opera: puede tener autoridad propia para notificaciones y sanciones.
9. Para el informante o el afectado: fecha y canal de la comunicación, contenido, medida adoptada después y su fecha (corre la caducidad del despido o de la sanción).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la fecha de vigencia. Cita la ley como «Ley 2/2023, de 20 de febrero».

**A. Obligados y ámbito**

- Obligados del sector privado: personas físicas o jurídicas con cincuenta o más trabajadores; las del ámbito de los actos de la Unión sobre servicios, productos y mercados financieros, blanqueo, seguridad del transporte y medio ambiente, sea cual sea su plantilla y con su normativa específica; partidos, sindicatos, organizaciones empresariales y sus fundaciones si reciben o gestionan fondos públicos (art. 10.1). Las demás pueden implantarlo, pero con todos los requisitos de la ley (art. 10.2).
- **Plazo de implantación**: lo fija la disposición transitoria segunda de la ley (tres meses desde su entrada en vigor, con un plazo más largo para las entidades privadas pequeñas). `buscar_articulo` no devuelve las disposiciones transitorias: léela en internet en el texto consolidado del BOE (https://www.boe.es/buscar/act.php?id=BOE-A-2023-4513), cítala con enlace y fecha de consulta y, si la entidad obligada aún no tiene sistema, di en la nota desde cuándo incumple.
- Grupos: la dominante aprueba una política general; el Responsable y el sistema pueden ser únicos para el grupo (art. 11). Entre cincuenta y doscientos cuarenta y nueve trabajadores, las empresas pueden compartir sistema y recursos (art. 12). Aunque el sistema sea común, la obligación es de cada sociedad: su órgano de administración lo implanta previa consulta a su propia representación, aprueba el procedimiento y designa al Responsable (arts. 5.1, 8.1 y 9.1); cada sociedad es responsable del tratamiento, de modo que al compartir el sistema son corresponsables y necesitan el acuerdo del art. 26 del RGPD (art. 6.2); y cada sociedad obligada lleva su libro-registro (art. 26). Distingue en la nota las sociedades obligadas de las que se integran voluntariamente (art. 10.2) y la autoridad de cada una según dónde tenga sus establecimientos.
- Qué protege: infracciones del Derecho de la Unión en las condiciones del art. 2.1.a) y acciones u omisiones que puedan ser infracción penal o administrativa grave o muy grave (art. 2.1.b). Las infracciones laborales en seguridad y salud se rigen también por su normativa (art. 2.3). Quién: trabajadores, autónomos, socios, administradores, personal de contratistas, relaciones terminadas o no iniciadas, becarios y voluntarios (art. 3.1 y 3.2); también quienes asisten al informante, sus compañeros y familiares y los representantes legales que le asesoran (art. 3.3 y 3.4).
- El canal puede recibir otras comunicaciones, pero quedan fuera de la protección (art. 7.4). No están protegidos los conflictos interpersonales o que solo afectan al informante y a la persona señalada, los rumores y lo ya público (art. 35.2).

**B. Requisitos del Sistema (arts. 4 a 9)**

- El órgano de administración implanta el sistema **previa consulta con la representación legal** y es responsable del tratamiento de datos (art. 5.1). Requisitos del art. 5.2, letra a) a j): acceso a todos los del art. 3, diseño seguro y confidencial, comunicaciones escritas o verbales, integración de todos los canales, tratamiento efectivo, independencia respecto de otras entidades, Responsable, **política** publicitada, **procedimiento** de gestión y garantías para el informante.
- Gestión por tercero externo: con garantías de independencia, confidencialidad, datos y secreto; es encargado del tratamiento con contrato del art. 28.3 RGPD; la responsabilidad sigue en el Responsable del Sistema (art. 6).
- Canal (art. 7): por escrito (correo postal o medio electrónico) o verbal (teléfono o mensajería de voz) y, si se pide, reunión presencial en siete días; grabación o transcripción con consentimiento y derecho a revisar y firmar la transcripción; información sobre los canales externos; domicilio o lugar seguro para notificaciones; **comunicaciones anónimas admitidas** (art. 7.3).
- Responsable del Sistema (art. 8): lo nombra y cesa el órgano de administración; si es colegiado, delega en uno de sus miembros; nombramiento y cese se notifican a la Autoridad Independiente de Protección del Informante o al órgano autonómico competente **en diez días hábiles**, con las razones del cese; actúa con independencia, sin instrucciones y con medios; en el sector privado es un directivo, salvo que la dimensión no lo permita, evitando conflictos de interés; puede serlo quien ya lleve el cumplimiento normativo. La vía y el formulario de notificación, así como la autoridad competente en la comunidad autónoma, búscalos en internet en la sede oficial de la Autoridad Independiente de Protección del Informante o del órgano autonómico y cítalos con enlace y fecha de consulta. Que una comunidad haya designado autoridad propia no basta: comprueba en su ley si esa autoridad tiene competencias sancionadoras sobre el **sector privado**, y aplica el criterio que publique la Autoridad Independiente sobre quién notifica ante ella (establecimientos en más de una comunidad; comunidad sin autoridad competente para el sector privado). En grupos y en sistemas voluntarios, consulta también sus preguntas frecuentes sobre el Responsable (si notifica cada sociedad obligada, si notifican las no obligadas). Calcula los diez días hábiles con el calendario oficial de días inhábiles del año.
- Procedimiento (art. 9.2, contenido mínimo de la letra a) a la j)): canales asociados; información sobre canales externos; **acuse de recibo en siete días naturales**; **respuesta en un máximo de tres meses** desde la recepción (o desde el vencimiento de los siete días si no hubo acuse), ampliable otros tres en casos de especial complejidad; comunicación con el informante; derecho del afectado a conocer lo que se le atribuye y a ser oído; confidencialidad cuando la comunicación llega por otra vía o a otra persona, con obligación de remitirla al Responsable; presunción de inocencia y honor; protección de datos; **remisión inmediata al Ministerio Fiscal** si los hechos pueden ser delito (a la Fiscalía Europea si afectan a intereses financieros de la Unión). Lo aprueba el órgano de administración y el Responsable responde de su tramitación diligente (art. 9.1). La ley no fija plazo ni causas de admisión para el canal interno: si el procedimiento los regula, puede tomar como referencia los del canal externo (art. 18.2) y advertir que la comunicación inadmitida queda fuera de la protección (art. 35.2, letra a); dilo como decisión de diseño, no como exigencia legal.
- Publicidad: información clara y accesible sobre el canal y los principios del procedimiento; si hay web, en la página de inicio, en sección separada (art. 25).
- Libro-registro de informaciones e investigaciones, no público, accesible solo por auto judicial; conservación de datos no superior a diez años (art. 26).

**C. Datos personales**

- Licitud por obligación legal cuando el sistema es obligatorio (art. 30.2; art. 24 LOPDGDD). Información a informantes y afectados; la identidad del informante nunca se comunica al afectado (art. 31.2); presunción de motivos legítimos frente a la oposición del afectado (art. 31.4).
- Acceso limitado a Responsable, RR. HH. solo si procede una medida disciplinaria, servicios jurídicos, encargados y delegado de protección de datos (art. 32.1); supresión de lo innecesario y de las categorías especiales; supresión a los tres meses sin investigación, salvo evidencia anonimizada del funcionamiento (art. 32.2 a 32.4).
- La identidad del informante solo se comunica a la autoridad judicial, al Ministerio Fiscal o a la administrativa competente, avisándole antes salvo que comprometa la investigación (art. 33.3).

**D. Protección**

- Condiciones: motivos razonables para creer que la información es veraz y entra en el ámbito de la ley, y comunicación conforme a la ley (art. 35.1); la protección alcanza al anónimo que luego es identificado (art. 35.3).
- Represalias prohibidas, incluidas amenazas y tentativas, con la lista del art. 36.3 (despido, no renovación, sanciones, degradación, modificaciones sustanciales, evaluaciones negativas, listas negras…), salvo ejercicio regular del poder de dirección por hechos acreditados y ajenos a la comunicación (art. 36.3.a); protección durante dos años, ampliable (art. 36.4).
- Presunción de represalia: acreditado razonablemente que comunicó y que sufrió un perjuicio, quien adoptó la medida debe probar motivos ajenos a la comunicación (art. 38.4); exención de responsabilidad por la comunicación (art. 38.1, 38.2 y 38.5). En lo laboral, el despido que vulnera derechos fundamentales es nulo (art. 55.5 ET): combínalo con la doctrina sobre la garantía de indemnidad.
- El afectado conserva la presunción de inocencia, el derecho de defensa y de acceso al expediente en los términos de la ley, y la misma confidencialidad (art. 39).
- Medidas de apoyo de las autoridades (art. 37).

**E. Sanciones**

- Potestad: la Autoridad Independiente en el sector privado, salvo que una comunidad autónoma la haya atribuido a su órgano para su territorio (art. 61). Comprueba la normativa autonómica del lugar de actividad: si Jurisprudenciator no la devuelve (`buscar_boe` con el nombre de la comunidad y «protección del informante»), búscala en internet en el boletín oficial de la comunidad y cítala con enlace.
- Muy graves (acciones u omisiones **dolosas**), entre otras: obstaculizar comunicaciones, represalias, vulnerar la confidencialidad o el anonimato, revelar a sabiendas información falsa y **no disponer del Sistema interno** (art. 63.1, letra g). Graves y leves en el art. 63.2 y 63.3. Prescripción en el art. 64; multas y sanciones accesorias en el art. 65 (léelas del artículo; distinguen personas físicas y jurídicas); graduación en el art. 66.

**F. Revisión de un sistema ya implantado**

Cuando la empresa ya tenga canal, comprueba cada punto con el documento que lo acredita y anota el artículo incumplido:

| Punto | Qué pedir | Artículo |
|---|---|---|
| Consulta previa a la representación | Comunicación y fecha | 5.1 |
| Aprobación de política y procedimiento por el órgano de administración | Acta o acuerdo | 5.2.h, 5.2.i y 9.1 |
| Responsable nombrado y notificado en plazo | Acuerdo y justificante de la notificación | 8.1 y 8.3 |
| Admisión de comunicaciones anónimas y de la reunión presencial a petición (el canal puede ser escrito, verbal o ambos) | Configuración real de la herramienta | 5.2.c, 7.2 y 7.3 |
| Contrato de encargo con el gestor externo | Contrato | 6.2 y 6.4 |
| Información en la web, en la página de inicio | Captura de la web | 25 |
| Libro-registro y plazos de conservación y supresión | Registro y política de conservación | 26 y 32 |
| Canales paralelos no integrados (correo de RR. HH., buzón de acoso) | Relación de canales | 5.2.d y 7.1 |

## Estrategia y jurisprudencia

1. **Empresa:** un canal sin procedimiento aprobado por el órgano de administración, sin Responsable notificado o que no admite anónimas incumple la ley aunque reciba denuncias. Documenta la consulta a la representación, el acuerdo del órgano, la notificación del Responsable y la publicación en la web. Integra los canales existentes (acoso, cumplimiento) en el sistema y coordina el protocolo de acoso con el Responsable.
2. **Informante:** acredita la comunicación (fecha, canal, contenido) y la cronología de la medida posterior; encuadra los hechos en el art. 2 (si son un conflicto personal no hay protección de la ley, pero puede haber garantía de indemnidad); ejercita la acción laboral en plazo (veinte días hábiles para el despido, arts. 59.3 ET y 103.1 LRJS).
3. **Afectado:** revisa si se le informó y oyó (art. 9.2.f), si se respetó la confidencialidad y si la medida disciplinaria se apoyó en hechos acreditados.
4. Consultas en Jurisprudenciator (reformula como máximo dos veces; la doctrina del Supremo sobre esta ley aún es escasa):
   - `consulta="Ley 2/2023 informante represalia despido nulidad canal de denuncias"`, `base="AN"`, `jurisdiccion="SOCIAL"`, `tipo_organo="TSJ"`.
   - `consulta="investigación interna canal de denuncias prueba despido disciplinario confidencialidad identidad denunciante"`, mismos filtros.
   - `consulta="garantía de indemnidad denuncia interna represalia"`, `base="TS"`, `jurisdiccion="SOCIAL"`; y en `base="TC"` para la doctrina constitucional sobre indicios.
5. Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y transcribe fundamentos. La política y el procedimiento se sostienen en el texto de la ley: cita doctrina solo si existe y aporta (apartado 8 del formato); en un caso de represalia es imprescindible.

## Documentos que se entregan

Word maquetado según `references/formato-y-organos-laboral.md`. Cita cada artículo como «artículo N de la Ley 2/2023, de 20 de febrero», y los que tienen letra como «letra a) del artículo 10.1 de la Ley 2/2023, de 20 de febrero» (con «artículo 10.1, letra a), de la Ley…» el verificador no enlaza la norma). Si el documento se apoya en un dato de internet (disposición transitoria, ley autonómica, criterio de la autoridad), cítalo con su enlace y fecha de consulta.

**1. Política del Sistema interno de información y defensa del informante** — `politica-sistema-interno-informacion-<empresa>-<AAAAMMDD>.docx`: finalidad y compromiso del órgano de administración; ámbito material (art. 2) y personal (art. 3); canales disponibles, incluido el anónimo, y canales externos; principios (confidencialidad, prohibición de represalias, presunción de inocencia, protección de datos); Responsable del Sistema y su independencia; derechos de informantes y afectados; consecuencias de las represalias y de la información falsa a sabiendas; aprobación (órgano y fecha), consulta a la representación (fecha) y publicación (web, sección separada).

**2. Procedimiento de gestión de informaciones** — `procedimiento-gestion-informaciones-<empresa>-<AAAAMMDD>.docx`: canales asociados; recepción y registro con código; comunicaciones verbales y reunión presencial; acuse de recibo en siete días naturales; admisión o inadmisión motivada; investigación (instructor, diligencias, audiencia del afectado, comunicación con el informante); plazo máximo de tres meses y su ampliación; conclusión y medidas; remisión al Ministerio Fiscal; comunicaciones recibidas por vías no previstas; conflicto de interés; libro-registro y conservación; protección de datos; coordinación con el protocolo de acoso y con RR. HH.; anexos (formulario, cláusula informativa de datos, modelo de acuse, acta de comunicación verbal).

**3. Si el abogado lo pide:** acuerdo del órgano de administración de implantación y nombramiento del Responsable, y texto de la comunicación del nombramiento a la autoridad competente dentro de los diez días hábiles, ajustado al formulario oficial que encuentres en su sede (cita el enlace); si no hay formulario, redacta la comunicación con los datos del art. 8.3.

**4. Nota para el abogado** — `nota-abogado-canal-denuncias-<empresa>-<AAAAMMDD>.docx`: si la entidad está obligada y por qué letra del art. 10.1; decisiones de diseño; artículos leídos con su vigencia; autoridad competente según la comunidad; plazos (notificación del Responsable, acuse, respuesta) con fechas si hay calendario; doctrina leída; riesgos y sanciones aplicables con remisión al art. 65.

**Si la entidad no está obligada** (por ejemplo, menos de cincuenta trabajadores y fuera de las letras b) y c) del art. 10.1), dilo con claridad y descarta cada letra con el dato que la excluye. No prepares política ni procedimiento salvo que el abogado quiera un sistema voluntario: basta la nota, que explica lo que la ley le aplica igualmente (sus trabajadores pueden acudir al canal externo, art. 16; las represalias están prohibidas y son sancionables para cualquier persona, arts. 36, 62 y 63; nulidad del despido lesivo, art. 55.5 ET), que un sistema voluntario debe cumplir todos los requisitos (art. 10.2) con su propia base de licitud (art. 30.2, segundo párrafo), que no puede usar como propio el canal de otra entidad fuera de los casos del art. 12 (art. 5.2, letra f) y que la ley no fija cómo se computan los cincuenta trabajadores.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos de la Ley 2/2023 que se citan (al menos 2, 3, 5, 7, 8, 9, 10, 25, 26, 32, 33, 35, 36, 38 y 63) y el art. 24 LOPDGDD.
- [ ] Obligación determinada con la letra concreta del art. 10.1 y el número de trabajadores facilitado; si la entidad no está obligada, dicho expresamente y con las alternativas del art. 10.2. Plazo de implantación de la disposición transitoria segunda leído en el BOE (con enlace).
- [ ] Plazos del procedimiento (siete días naturales, tres meses más tres, diez días hábiles para notificar al Responsable) tomados del texto leído.
- [ ] Ninguna cuantía de multa escrita sin leer el art. 65 en esta conversación.
- [ ] Autoridad competente, vía de notificación del Responsable y normativa autonómica comprobadas; lo obtenido en internet, citado con enlace y fecha de consulta y señalado en el resumen.
- [ ] Cada ECLI citado leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre cada documento y corregido lo que señale.
- [ ] Marcadores (`[DENOMINACIÓN SOCIAL]`, `[ÓRGANO DE ADMINISTRACIÓN]`, `[RESPONSABLE DEL SISTEMA]`, `[DIRECCIÓN DEL CANAL]`) en lugar de datos inventados.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y para quién, plazos con su precepto, documentos que faltan y riesgos, tabla de jurisprudencia y próximo paso.
