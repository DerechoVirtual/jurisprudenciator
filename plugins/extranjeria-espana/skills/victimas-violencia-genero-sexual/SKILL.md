---
name: victimas-violencia-genero-sexual
description: >-
  Prepara la solicitud de autorización de residencia temporal y trabajo por circunstancias excepcionales
  de la mujer extranjera víctima de violencia de género o de la víctima de violencia sexual (art. 31 bis
  LOEX; arts. 133 a 141 del Real Decreto 1155/2024), con enfoque de protección y confidencialidad:
  autorización provisional desde la orden de protección, el informe fiscal o el título acreditativo,
  autorizaciones de hijos y ascendientes, suspensión del expediente sancionador o de la expulsión y
  autorización definitiva tras el proceso penal. Úsala con «orden de protección», «ha denunciado a su
  pareja y no tiene papeles», «agresión sexual», «informe del fiscal», «le abren expediente de expulsión
  tras denunciar». Si fue reagrupada por su agresor, valora la residencia independiente
  (reagrupacion-familiar); si hay trata, victimas-trata; otras violencias familiares,
  razones-humanitarias.
---

# Víctimas de violencia de género y de violencia sexual

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Derecho a la autorización, suspensión del sancionador y efectos del proceso penal** → `buscar_articulo` (`ley="LOEX"`, artículos `"31 bis"` y `"31"`).
- **Violencia de género: supuesto, familiares, procedimiento y resolución final** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"133"`, `"134"`, `"135"` y `"136"`).
- **Violencia sexual y víctimas menores** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"137"` a `"141"`, uno por llamada).
- **Títulos que acreditan la condición de víctima** → `buscar_articulo` (`ley="LO 1/2004"`, `articulo="23"`) y `buscar_articulo` (`ley="LO 10/2022"`, `articulo="37"`).
- **Órgano, representación, modificación y residencia independiente de la reagrupada** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"193"`, `"197"`, `"191"` y `"69"`) y `buscar_articulo` (`ley="LOEX"`, `articulo="19"`).
- **Expediente sancionador abierto (escrito B)** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"218"` y `"226"`): quién ordena la incoación y qué debe decir el acuerdo de iniciación (instructor y órgano que resuelve, art. 226.1.c y d).
- **Doctrina (antecedentes penales, sobreseimiento, provisional, medidas cautelares)** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"` o `base="AN"`; fechas en formato `dd/mm/aaaa`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
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

- Mujer extranjera en situación irregular que denuncia o acredita una situación de **violencia de género** (LOEX art. 31 bis; arts. 133 a 136).
- Víctima extranjera de **violencia sexual**: mujeres, niñas y niños según la definición del art. 137.1 (delitos de los arts. 178 a 194 bis CP, mutilación genital femenina, matrimonio forzado, acoso con connotación sexual y violencias sexuales digitales, según el art. 137.1), incluidas las menores (art. 141).
- Tres momentos: al acreditarse la violencia (solicitud y autorización provisional), durante el proceso penal (incluir hijos o ascendientes, defender la suspensión del sancionador) y al terminar (autorización definitiva o su solicitud en plazo).

Detector (léelo con `buscar_articulo` antes de decirlo y no redactes esta solicitud si encaja otra figura):

| Situación | Figura y skill |
|---|---|
| Reagrupada por el agresor, con residencia vigente | residencia y trabajo independiente (LOEX art. 19.2; art. 69.2.b, plazo de seis meses) → `reagrupacion-familiar` |
| Ya residía legalmente cuando se produjo o se acreditó la violencia | el art. 31 bis se refiere a quien está en situación irregular; valora la renovación o la modificación de su autorización → `renovacion-modificacion-extincion` |
| Víctima de violencia familiar que no es violencia de género (otro agresor, víctima varón) con sentencia firme | art. 128.2 → `razones-humanitarias` |
| Indicios de trata o explotación sexual por una red | → `victimas-trata` |
| Temor de persecución en su país por motivos de género | → `proteccion-internacional-apatridia` (compatible con esta solicitud) |

## Protección y confidencialidad

- Pregunta antes de nada si la víctima tiene medidas de protección que impidan revelar su domicilio. Por defecto, designa el domicilio del despacho a efectos de notificaciones y escribe el domicilio real solo si el abogado lo confirma.
- El escrito acredita la condición de víctima con el título (orden de protección, informe fiscal, resolución judicial o título administrativo) y no necesita relatar la violencia. No transcribas el atestado, las lesiones ni detalles íntimos; no incluyas datos del agresor más allá de lo que identifica el procedimiento penal.
- La tarjeta que se expida no refleja la condición de víctima ni el carácter provisional (arts. 135.4 y 139.4): díselo a la clienta.
- Datos de hijos: los imprescindibles para su autorización (identidad, filiación, presencia en España al denunciar).
- En las consultas a Jurisprudenciator, busca por la cuestión jurídica, nunca por nombres, juzgado ni número de procedimiento.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. Si falta un dato imprescindible (★), pídelo y espera.

1. ★ Tipo de violencia (género o sexual) y **título que la acredita**: orden de protección (fecha y órgano), informe del Ministerio Fiscal, resolución judicial con indicios (violencia sexual), o título administrativo de los servicios sociales o especializados (LO 1/2004 art. 23; LO 10/2022 art. 37).
2. ★ Estado del proceso penal: órgano y número (solo para el expediente, no para las búsquedas), fase, y si hay sentencia o auto que lo termine: tipo (condena, absolución, archivo por paradero desconocido, sobreseimiento provisional por expulsión del denunciado, otro) y **fecha de notificación** a la víctima.
3. ★ Situación administrativa en la fecha de la denuncia o acreditación y ahora: si estaba en situación irregular; expediente sancionador, orden de expulsión o de devolución (número, fecha, estado).
4. ★ Pasaporte, documento de viaje o cédula de inscripción en vigor (arts. 135.1.a y 139.1.a); provincia en la que reside (arts. 135.1 y 139.1).
5. ★ Hijos menores, tutelados, mayores con discapacidad que requiera apoyo o que no puedan proveer a sus necesidades por su salud, y ascendientes en primer grado: si estaban en España **en el momento de la denuncia**, edades (los mayores de dieciséis reciben residencia y trabajo) y documentos de filiación.
6. ★ Antecedentes penales en España o en países de residencia anteriores (LOEX art. 31.5), con fechas.
7. Representación: apoderamiento notarial o apud acta, o colaborador inscrito (art. 197.4). Si la solicitud la presenta un tercero, documento de representación (arts. 135.1.b y 139.1.b).

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**Suspensión del sancionador y de la expulsión (LOEX art. 31 bis.2; arts. 133.2 y 137.3)**

- Si al denunciar o acreditar la violencia se pone de manifiesto la situación irregular, no se incoa el expediente por la infracción del art. 53.1.a) LOEX y se suspende el ya incoado o la ejecución de la expulsión o devolución acordadas. Si el expediente no se había iniciado, su incoación se pospone hasta el final del proceso penal.
- La autoridad ante la que se denuncia o que expide el título informa de estas posibilidades (arts. 133.3 y 137.4). Si no lo hizo y hay un expediente abierto, prepara el escrito de solicitud de suspensión al instructor (ver «Documento»).

**Autorización provisional (LOEX art. 31 bis.3; arts. 134, 135, 138 y 139)**

- Se puede pedir desde que hay orden de protección o, en su defecto, informe del Ministerio Fiscal con indicios; el Reglamento admite además el documento que acredite la condición de víctima según su normativa (art. 135.1.c; art. 139.1.c añade la resolución judicial con indicios de violencia sexual). Comprueba el título con LO 1/2004 art. 23 o LO 10/2022 art. 37.
- Se presenta ante la oficina de extranjería de la provincia de residencia, con pasaporte o cédula, representación y título; en su caso, prueba del vínculo familiar (arts. 135.1 y 139.1).
- Presentada la solicitud, la autoridad concede **de oficio** la autorización provisional de residencia y trabajo para la solicitante y, en su caso: en violencia de género, **solo para los hijos** (art. 135.2; el ascendiente no tiene provisional y su autorización por razones humanitarias llega con la definitiva, art. 136.1: avísalo como riesgo); en violencia sexual, para todos los familiares del art. 138.2, **ascendientes incluidos** (art. 139.2). Eficacia desde su concesión y vigencia hasta la resolución definitiva (arts. 135.3 y 139.3).
- Tarjeta de vigencia anual en el plazo de un mes, que no se cuenta igual: en violencia de género, **desde la concesión**, ante la oficina de extranjería o la comisaría (art. 135.4); en violencia sexual, **desde la notificación**, ante la comisaría (art. 139.4).
- Tramitación preferente (arts. 134.3 y 138.3). La definitiva no se resuelve hasta que concluya el proceso penal (LOEX art. 31 bis.3).
- Habilita a trabajar por cuenta ajena y propia en cualquier ocupación (arts. 134.1 y 138.1).
- Si la provisional se concedió con el título administrativo, en la primera renovación de la tarjeta hay que adjuntar copia de la denuncia (arts. 135.5 y 139.5): avísalo en el resumen.

**Familiares (LOEX art. 31 bis.3; arts. 134.2 y 138.2)**

- Hijos menores, hijos menores tutelados, mayores con discapacidad que requiera apoyo y mayores que no puedan proveer a sus necesidades por su salud: residencia por circunstancias excepcionales; los mayores de dieciséis, residencia y trabajo. Ascendientes en primer grado: residencia por razones humanitarias (los prevén los arts. 134.2 y 138.2; el art. 31 bis LOEX solo menciona a los hijos, así que cítalos con el Reglamento).
- Requisito común: estar en España en el momento de la denuncia. Se pueden pedir con la solicitud o en cualquier momento del proceso penal y después.

**Final del proceso penal (LOEX art. 31 bis.4; arts. 136 y 140)**

- Sentencia condenatoria o resolución judicial de la que se deduzca la condición de víctima: autorización de residencia y trabajo de **cinco años** para ella y sus familiares; si ya tenía la provisional, se concede y notifica en el plazo máximo de veinte días desde que conste a la oficina; archivo del sancionador; el tiempo de la provisional computa para la larga duración.
- La LOEX incluye expresamente el **archivo por paradero desconocido del investigado** y el **sobreseimiento provisional por expulsión del denunciado**. Si la oficina deniega en esos casos porque el Reglamento no los menciona, sostén la primacía de la ley orgánica.
- Si no había pedido la autorización: el Ministerio Fiscal le informa y dispone de **seis meses desde la notificación** para pedirla: de la sentencia o resolución judicial en violencia de género (art. 136.2.1.º.b) y de la sentencia en violencia sexual (art. 140.2.1.º.b; si lo que terminó el proceso es otra resolución, dilo como riesgo y presenta cuanto antes). Calcula la fecha límite con la fecha de notificación; sin ella, pídela y no des plazo.
- Si de la resolución no se deduce la violencia: se deniega la definitiva, la provisional pierde eficacia sin pronunciamiento expreso y no computa para larga duración ni nacionalidad, y se inicia o reanuda el sancionador (arts. 136.2.2.º y 140.2.2.º; LOEX art. 31 bis.4).
- Modificación: desde estas autorizaciones no se puede pedir la modificación del art. 191 (art. 191.7.b); durante su vigencia puede pedirse la larga duración, computando el tiempo de la provisional (arts. 136 y 140).

**Antecedentes penales.** La carencia de antecedentes del art. 31.5 LOEX se aplica también a esta autorización, pero la jurisprudencia del Supremo exige ponderación y no aplicación automática. Búscala antes de redactar si hay antecedentes (ver «Estrategia»).

**Víctimas de violencia sexual menores (art. 141).** Autorización extensiva a los adultos responsables que estén en España salvo indicios de su implicación, consentimiento o falta de diligencia; tramitación preferente; posible derivación a recursos específicos a propuesta de la entidad tutelar o del fiscal. Si la menor no está acompañada, usa también `menores-extranjeros`.

**Causas típicas de denegación**

| Causa | Respuesta |
|---|---|
| Solicitud presentada cuando ya residía legalmente o tras el archivo del proceso | Revisa la fecha de la irregularidad y del título; si no encaja, reconduce (detector) |
| Sobreseimiento o archivo | Distingue el tipo: los supuestos de paradero desconocido y expulsión del denunciado cuentan como víctima (LOEX art. 31 bis.4) |
| Antecedentes penales | Ponderación obligatoria del tipo de delito, gravedad, peligro actual y circunstancias de la víctima |
| Hijos que no estaban en España al denunciar | No entran por esta vía: valora reagrupación o arraigo familiar |
| Plazo de seis meses vencido | Calcula desde la notificación a la víctima; si no consta notificación válida, el plazo no ha empezado |

## Estrategia y jurisprudencia

1. Presenta la solicitud en cuanto exista título: la provisional se concede de oficio y protege frente a la expulsión.
2. Si hay expediente de expulsión abierto, presenta a la vez el escrito de suspensión ante el instructor con copia del título.
3. Si se deniega la autorización, en el recurso contencioso puede pedirse una medida cautelar que mantenga la situación anterior: prepárala con `recurso-contencioso-extranjeria` y busca antes la doctrina de cautelares (consulta de abajo).
4. Consultas (reformula como máximo dos veces; dos a cuatro palabras clave):
   - Antecedentes: `buscar_sentencias` (`consulta="violencia de género antecedentes ponderación"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`, `anios=3`).
   - Sobreseimiento y fin del proceso: `consulta="violencia de género sobreseimiento residencia"`, `base="AN"`.
   - Autorización y requisitos: `consulta="víctima violencia de género autorización"`, `base="AN"`.
   - Violencia sexual: `consulta="violencia sexual 31 bis"`, `base="AN"`, `fecha_desde="07/10/2022"` (devuelve mucho ruido: sanciones de publicidad, acoso laboral…; no leas una sentencia solo porque su extracto automático diga «violencia sexual»).
   - Cautelares: `consulta="cautelar víctima violencia de género"`, `base="AN"`.
   Para los escritos A, B y C la jurisprudencia **no es imprescindible**: si tras dos reformulaciones no aparece nada aplicable, redacta con los preceptos leídos, omite el fundamento de doctrina y díselo al abogado en el resumen. Sí lo es si hay antecedentes penales que ponderar o un recurso: entonces aplica la puerta.
5. Antes de citar una sentencia, comprueba en su texto qué reglamento aplicó. Doctrina dictada con el Real Decreto 557/2011: úsala para lo que no ha cambiado (LOEX art. 31 bis, antecedentes) e indica el precepto equivalente vigente.
6. Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y transcribe fundamentos, nunca hechos ni datos de aquel pleito.

## Documento que se entrega

Un Word maquetado según `references/formato-y-organos.md`, con la marca «CONFIDENCIAL» en el encabezamiento. Según el momento:

- **A. Solicitud de autorización de residencia temporal y trabajo por circunstancias excepcionales (víctima de violencia de género / de violencia sexual) y de las autorizaciones de los familiares**. Nombre: `solicitud-victima-violencia-<apellido-cliente>-<AAAAMMDD>.docx`.
- **B. Escrito de solicitud de suspensión del expediente sancionador o de la ejecución de la expulsión o devolución**, dirigido al órgano que lo tramita. Nombre: `suspension-sancionador-victima-<apellido-cliente>-<AAAAMMDD>.docx`.
- **C. Solicitud de la autorización tras la sentencia**, cuando no se pidió antes (plazo de seis meses). Mismo esquema que A.

Estructura de A y C:

1. **Encabezamiento**: «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA] — [DELEGACIÓN / SUBDELEGACIÓN] DEL GOBIERNO» (arts. 135.1 o 139.1 y 193.2).
2. **Comparecencia**: `[NOMBRE Y APELLIDOS]`, nacionalidad, `[PASAPORTE]`, `[NIE]` si lo tiene, domicilio a efectos de notificaciones (despacho, salvo indicación del abogado); representación (art. 197.4).
3. **EXPONE — HECHOS** (ordinales): identidad y situación administrativa; existencia del título que acredita la violencia (tipo, órgano y fecha, sin relato de los hechos violentos); estado del proceso penal; familiares que estaban en España al denunciar; ausencia de antecedentes o su ponderación.
4. **FUNDAMENTOS DE DERECHO**: I. Derecho a la autorización (LOEX art. 31 bis; arts. 133 o 137). II. Título habilitante (arts. 135.1.c o 139.1.c; LO 1/2004 art. 23 o LO 10/2022 art. 37). III. Autorización provisional de oficio y tramitación preferente (arts. 134, 135 o 138, 139). IV. Familiares (arts. 134.2 o 138.2). V. Suspensión del sancionador (LOEX art. 31 bis.2). VI. En C: resolución que pone fin al proceso y plazo de seis meses (arts. 136 o 140). VII. Doctrina con párrafo literal y ECLI, si la hay aplicable. Cada fundamento con su propia secuencia (formato, apartado 2).
5. **SOLICITA**: autorización provisional de residencia y trabajo de oficio y, en su momento, la definitiva de cinco años; autorizaciones de los familiares indicados.
6. **OTROSÍES**: suspensión del expediente sancionador o de la expulsión que conste; tramitación preferente; confidencialidad del domicilio.
7. Lugar, fecha y firma.
8. **RELACIÓN DE DOCUMENTOS**: impreso oficial vigente (que el abogado descarga de la sede oficial); pasaporte o cédula de la solicitante y de cada familiar; título que acredita la violencia; documentos de filiación; representación; en C, resolución que pone fin al proceso y justificante de su notificación.

Estructura de B: encabezamiento al instructor que designa el acuerdo de iniciación (`[NÚMERO DE EXPEDIENTE]`; art. 226.1.c), con copia al órgano competente para resolver que figure en ese acuerdo (art. 226.1.d); hechos (expediente y su fecha, fecha de la denuncia —de ella depende que proceda «suspender» el incoado antes o «no incoar»—, título y fecha de solicitud de la autorización); fundamentos (LOEX art. 31 bis.2; arts. 133.2 o 137.3; deber de información de los arts. 133.3 o 137.4 si no se cumplió); solicita la suspensión inmediata hasta el final del proceso penal; documentos. Si ya hay orden de expulsión, pide la suspensión de su ejecución (mismo art. 31 bis.2).

Cita el Reglamento siempre como «artículo N del Real Decreto 1155/2024» y la LOEX como «artículo N de la Ley Orgánica 4/2000» (formato, apartado 4); nunca «del Reglamento de Extranjería» ni «del Reglamento aprobado por el Real Decreto…», que `verificar_escrito` no identifica. `verificar_escrito` tampoco enlaza la norma cuando el artículo lleva «bis» con apartado o una letra («artículo 31 bis.3 de la Ley Orgánica 4/2000», «artículo 135.1.c) del Real Decreto 1155/2024»): los atribuye a la norma citada antes. Escríbelos así: «apartado 3 del artículo 31 bis de la Ley Orgánica 4/2000», «letra c) del artículo 135.1 del Real Decreto 1155/2024», «letra a) del artículo 53.1 de la Ley Orgánica 4/2000»; y nombra la norma en cada remisión, también en las breves.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: LOEX 31 bis y 31; Reglamento 133 a 136 (o 137 a 141), 191, 193 y 197; LO 1/2004 art. 23 o LO 10/2022 art. 37; LOEX 19 y art. 69 si se descartó la residencia independiente; Reglamento 218 y 226 si hay escrito B.
- [ ] Detector pasado; si encaja otra figura, se ha dicho al abogado.
- [ ] Plazo de seis meses (si aplica) calculado con fecha de notificación y precepto; si no consta la fecha, pedida y sin plazo inventado.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el texto completo. Si marca un artículo del Reglamento como no localizado o lo atribuye a la LOEX, compruébalo con `buscar_articulo` (`ley="BOE-A-2024-24099"`) y reescribe la cita como «artículo N del Real Decreto 1155/2024».
- [ ] Confidencialidad revisada: sin relato de la violencia, sin domicilio real si no está autorizado, sin datos del agresor innecesarios; marcadores (`[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[DOMICILIO]`, `[NÚMERO DE EXPEDIENTE]`) en lugar de datos inventados.
- [ ] Sin importes de tasa ni códigos de modelo.
- [ ] Resumen para el abogado según el apartado 7 del formato: órgano; fechas y plazos con su precepto (tarjeta en un mes desde la concesión o desde la notificación, según el tipo de violencia; seis meses tras la sentencia; veinte días para la concesión); documentos que faltan y riesgos (antecedentes, tipo de sobreseimiento, familiares fuera de España); tabla de jurisprudencia; próximo paso.
