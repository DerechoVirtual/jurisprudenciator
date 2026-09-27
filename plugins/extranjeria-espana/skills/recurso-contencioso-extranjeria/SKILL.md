---
name: recurso-contencioso-extranjeria
description: >-
  Recurso contencioso-administrativo contra resoluciones de extranjería (denegaciones, extinciones,
  expulsiones, multas, devoluciones). Fija la competencia (art. 8.4 LJCA; desde la LO 1/2025,
  Tribunal de Instancia, Sección de lo Contencioso-Administrativo, arts. 84 y 93 LOPJ) y la
  territorial (art. 14 LJCA), calcula el plazo (art. 46 LJCA) y, si ha vencido, lo dice y propone
  alternativas, redacta la demanda del procedimiento abreviado (art. 78 LJCA) y pide medidas
  cautelares y cautelarísimas (arts. 129 y ss. LJCA) para suspender una expulsión o una salida
  obligatoria, con jurisprudencia del TSJ y del Supremo. Entrega la demanda y, en su caso, la
  solicitud cautelar en Word. Úsala con «recurso contencioso extranjería», «demanda contra la
  denegación», «suspender la expulsión», «cautelarísima», «le van a expulsar mañana». Para
  reposición o alzada usa recurso-administrativo-extranjeria; para el internamiento en CIE,
  internamiento-cie.
---

# Recurso contencioso-administrativo en extranjería

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Competencia objetiva y territorial** → `buscar_articulo` (`ley="LJCA"`, artículos `"8"`, `"9"`, `"10"`, `"11"` y `"14"`; `ley="LOPJ"`, artículos `"84"` y `"93"`).
- **Plazo, cómputo y agosto** → `buscar_articulo` (`ley="LJCA"`, artículos `"46"` y `"128"`; `ley="LOPJ"`, artículos `"182"` y `"185"`; `ley="LPAC"`, `articulo="123"` si hubo reposición).
- **Plazo vencido** → `buscar_articulo` (`ley="LJCA"`, artículos `"28"` y `"69"`; `ley="LPAC"`, artículos `"40"`, `"41"`, `"43"`, `"106"`, `"124"` y `"125"`; `ley="LOEX"`, artículos `"22"` y `"63"`; `ley="Ley 1/1996"`, `articulo="16"`).
- **Procedimiento abreviado, legitimación, postulación, documentos y cuantía** → `buscar_articulo` (`ley="LJCA"`, artículos `"19"`, `"23"`, `"25"`, `"31"`, `"42"`, `"45"`, `"56"`, `"60"`, `"78"` y `"81"`; `ley="LEC"`, `articulo="253"` para la cuantía indeterminada).
- **Medidas cautelares y cautelarísimas** → `buscar_articulo` (`ley="LJCA"`, artículos `"80"` y `"129"` a `"135"`; `ley="LOEX"`, artículos `"21"`, `"57"`, `"63"`, `"63 bis"` y `"64"`; `ley="BOE-A-2024-24099"`, artículos `"235"` y `"245"`; `ley="Ley 12/2009"`, `articulo="29"` si hay protección internacional).
- **Familia y menores en expulsiones y denegaciones** → `buscar_articulo` (`ley="CE"`, `articulo="39"`; `ley="Ley Orgánica 1/1996"`, `articulo="2"`; `ley="BOE-A-2024-24099"`, artículos `"94"` (familiares de persona española) y `"244"` (prohibición de entrada); `ley="LOEX"`, `articulo="58"`).
- **Asistencia jurídica gratuita y voluntad de recurrir** → `buscar_articulo` (`ley="LOEX"`, `articulo="22"`; `ley="BOE-A-2024-24099"`, `articulo="222"`; `ley="Ley 1/1996"`, `articulo="16"`).
- **Doctrina sobre el fondo y sobre la cautelar** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`; `base="TS"` para doctrina casacional; `base="AN"` con `tipo_organo="TSJ"` y `provincia` para el criterio de apelación; `tipo_resolucion="AUTO"` para cautelares) + `leer_sentencias` (`parrafos=3`, `terminos`).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar o el requisito que hay que comprobar), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Resolución de extranjería que pone fin a la vía administrativa (denegación, archivo, inadmisión, extinción, expulsión, multa, devolución) y se quiere impugnar ante el juez, directamente o tras la reposición.
- Expulsión, devolución o salida obligatoria cuya ejecución hay que suspender ya: cautelar o cautelarísima.
- Desestimación presunta de una solicitud o de un recurso administrativo.
- No la uses para reposición o alzada (`recurso-administrativo-extranjeria`), para el control del internamiento en CIE, que corresponde al juez de instrucción (`internamiento-cie`), para las alegaciones dentro del expediente de expulsión (`expulsion-procedimiento-sancionador`) ni para el fondo de una vía concreta sin recurso (la skill de esa vía). Para visados, protección internacional y nacionalidad, usa esta skill para el escrito solo después de fijar la competencia con el paso 2.

## Datos que hay que reunir antes de redactar

Los datos con ★ son imprescindibles; si falta uno, pregúntalo antes de redactar.

1. ★ **Resolución impugnada íntegra**: órgano que la dicta, fecha, número de expediente y pie de recursos.
2. ★ **Fecha de notificación** (y, si hubo reposición, fecha de su interposición y de su resolución o del vencimiento para entenderla desestimada).
3. ★ **Urgencia**: si está detenido, en CIE, con fecha de vuelo o conducción, o con plazo de cumplimiento voluntario corriendo; fecha y hora.
4. ★ **Domicilio del cliente** (provincia y municipio): puede cambiar la competencia territorial en sanciones.
5. ★ **Arraigo acreditable** para la cautelar: familia (con nacionalidad y situación de cada miembro), menores a cargo escolarizados, empleo u oferta, tiempo de residencia, padrón, enfermedad, embarazo, solicitud de protección internacional o de residencia en trámite.
6. ★ **Representación**: poder a procurador o al abogado, o apoderamiento electrónico; si pide asistencia jurídica gratuita, fecha de la solicitud.
7. ★ **Expediente administrativo** o, al menos, la solicitud, los documentos presentados y los requerimientos.
8. Antecedentes penales o policiales y su estado de cancelación.
9. Si el cliente está fuera de España o privado de libertad (voluntad de recurrir y asistencia jurídica gratuita).

## Requisitos y comprobaciones

### 1. Actividad impugnable y agotamiento de la vía

- La resolución debe poner fin a la vía administrativa (art. 25 LJCA). Si se interpuso reposición, no se puede demandar hasta que se resuelva o se entienda desestimada (art. 123.2 LPAC).
- Pretensión: anulación y, cuando proceda, reconocimiento de la situación jurídica individualizada (art. 31 LJCA), por ejemplo, la concesión de la autorización.

### 2. Competencia objetiva

- Resoluciones de extranjería de la Administración periférica del Estado (Delegaciones y Subdelegaciones del Gobierno, oficinas de extranjería) o de los órganos competentes de las comunidades autónomas: art. 8.4 LJCA.
- El conector devuelve el art. 8.4 LJCA con la denominación «Juzgados de lo Contencioso-administrativo»; los arts. 84.2.h y 93 LOPJ, en la redacción de la LO 1/2025, integran la Sección de lo Contencioso-Administrativo en el Tribunal de Instancia con sede en la capital de provincia. La norma de la LO 1/2025 que hace equivaler una denominación a la otra está en su parte final, que el conector no devuelve: cita los arts. 8.4 LJCA y 84 y 93 LOPJ tal como salen y comprueba la denominación exacta del órgano con `buscar_sentencias` (`consulta="Tribunal de Instancia Sección de lo Contencioso-Administrativo extranjería"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `provincia` de la sede, `fecha_desde` del año en curso) y lee en el encabezamiento de una resolución reciente de esa sede cómo se denomina el órgano (los autos de esas Secciones salen con ROJ que empieza por «ATICA»). Si no aparecen autos de la sede, sirve el campo «Órgano origen» de las sentencias recientes del TSJ que resuelven apelaciones contra ella (por ejemplo, «Sección de lo Contencioso-Administrativo del Tribunal de Instancia de Valencia, Plaza n.º…»), que devuelve la misma búsqueda. Si tras la consulta y dos reformulaciones no aparece ninguna resolución de la sede, no detengas la tarea por eso: la denominación resulta de los arts. 84.1 (el Tribunal de Instancia toma el nombre de la capital del partido), 84.2.h y 93.1 LOPJ leídos; encabeza con ella y di en el resumen que no se pudo confirmar con resoluciones de la sede.
- Actos de órganos centrales o ministeriales, consulares, de protección internacional o de nacionalidad: no presumas el art. 8.4. Lee los arts. 9, 10 y 11 LJCA (por ejemplo, el art. 9.1.e para la inadmisión de peticiones de asilo) y busca jurisprudencia reciente de competencia antes de encabezar. Si no puedes fijar el órgano con lo que devuelve el conector, detén la tarea en ese punto y explica qué falta.

### 3. Competencia territorial

- Regla general: sede del órgano que dictó el acto originario (art. 14.1, regla primera, LJCA).
- Sanciones (la expulsión y la multa lo son): a elección del demandante, su domicilio o la sede del órgano (art. 14.1, regla segunda). Acredita el domicilio con el padrón si eliges esa opción; si el domicilio no consta, el tribunal puede declararse incompetente.

### 4. Plazo

- Dos meses desde el día siguiente a la notificación del acto expreso; seis meses para el acto presunto, desde que se produce según su normativa (art. 46.1 LJCA). Tras reposición, desde la notificación de su resolución expresa o desde que se entienda desestimada (art. 46.4).
- Cómputo según el Código Civil (art. 185 LOPJ); agosto no corre salvo en derechos fundamentales (art. 128.2 LJCA); los plazos son improrrogables (art. 128.1).
- Contra desestimaciones presuntas, busca antes de escribir el plazo la doctrina del Supremo sobre su aplicación (`consulta="plazo recurso contencioso-administrativo desestimación presunta silencio administrativo"`, `base="TS"`) y cita solo lo que leas.
- Asistencia jurídica gratuita: lee el art. 22.3 LOEX (solicitud y voluntad expresa de recurrir) y el art. 16 de la Ley 1/1996 (la solicitud no suspende por sí sola; suspensión que puede acordarse para evitar la preclusión). Si el cliente está privado de libertad, la voluntad de recurrir se manifiesta ante el funcionario del art. 222 del Reglamento: pide copia del acta.
- Escribe la fecha de notificación, el precepto y la fecha final. Sin fecha de notificación no se da plazo.

**Si el plazo ha vencido, no redactes la demanda.** Antes de darlo por perdido, comprueba por este orden y con el precepto leído:

1. Que la notificación fue válida: texto íntegro, indicación de si pone fin a la vía, recursos, órgano y plazo (art. 40.2 LPAC; si falta algo, surte efecto desde la actuación del interesado del art. 40.3); forma de práctica (arts. 41 y 43 LPAC; en la electrónica, el rechazo a los diez días naturales solo opera si era obligatoria o elegida por el interesado).
2. Que ninguna actuación interrumpió o suspendió el plazo: reposición presentada (art. 46.4 LJCA), solicitud de asistencia jurídica gratuita con voluntad de recurrir (art. 22.3 LOEX; art. 16 de la Ley 1/1996, que no suspende por sí sola).
3. Si todo es correcto, el acto es firme y consentido: la demanda sería inadmisible (arts. 28 y 69 LJCA). Dilo así al abogado.
4. Alternativas, cada una con su precepto: recurso extraordinario de revisión solo por las causas tasadas del art. 125 LPAC y en sus plazos; solicitud de revisión de oficio si hay causa de nulidad del art. 47.1 (art. 106 LPAC); nueva solicitud de la autorización con los requisitos actuales (suele ser la vía útil; comprueba los requisitos de la vía y que no haya otro procedimiento abierto); y el riesgo actual si la resolución incluía salida obligatoria u orden de expulsión, con la protección que da una nueva solicitud (en el procedimiento preferente, art. 63.6 LOEX).
5. Entrega la nota del apartado «Documento que se entrega» en lugar de la demanda.

### 5. Procedimiento, postulación y documentos

- Extranjería se tramita por el procedimiento abreviado (art. 78.1 LJCA): el recurso se inicia por **demanda**, con los documentos del art. 45.2 (art. 78.2). Si el órgano competente no tramita por abreviado, se empieza por el escrito de interposición del art. 45.1 y la demanda llega con el expediente (art. 52).
- Ante órgano unipersonal: abogado obligatorio y procurador potestativo; si la representación se confiere al abogado, a él se notifica (art. 23.1 LJCA); apoderamiento electrónico (art. 23.4).
- Legitimación: art. 19.1.a LJCA.
- Cuantía: fíjala con el art. 42 LJCA y la norma procesal civil a la que remite, leída con `buscar_articulo` (`ley="LEC"`); en pretensiones sin contenido económico, justifícala como indeterminada. Lee el art. 81 LJCA para anticipar si la sentencia será apelable.
- Vista o fallo sin vista: el art. 78.3 permite pedir por otrosí que se resuelva sin prueba ni vista; si hay hechos que probar (arraigo, convivencia, trabajo), pide vista y propón la prueba.
- Motivos: pueden alegarse todos los que procedan, se plantearan o no ante la Administración (art. 56.1 LJCA); documentos con la demanda (art. 56.3).

### 6. Medidas cautelares y cautelarísimas

- Momento: en cualquier estado del proceso (art. 129.1 LJCA). En extranjería, las medidas anteriores a la interposición del art. 136.2 no sirven (solo para inactividad o vía de hecho): la cautelar va con la demanda o después.
- Criterio: la medida procede cuando la ejecución pueda hacer perder su finalidad legítima al recurso, tras valorar todos los intereses en conflicto; puede denegarse por perturbación grave de intereses generales o de tercero (art. 130). No se reduce a la suspensión: caben cuantas medidas aseguren la efectividad de la sentencia (art. 129.1).
- Tramitación ordinaria: pieza separada, audiencia de la Administración y auto (art. 131). Especial urgencia: auto sin oír a la otra parte en el plazo del art. 135.1; si afecta a un menor en actuaciones que impliquen retorno, el juez oye antes al Fiscal (art. 135.2). Pide la habilitación de días inhábiles del art. 128.3 si la ejecución es inminente en festivo o en agosto.
- Por qué la cautelarísima es la vía en la expulsión preferente: la ejecución es inmediata (LOEX 63.7; Reglamento 235.2) y la Administración no puede declarar efecto suspensivo (Reglamento 235.3). En la expulsión ordinaria, cuenta el plazo de cumplimiento voluntario (LOEX 63 bis.2; Reglamento 245.2) y pide la cautelar antes de que venza. Si la resolución no aclara si los días son naturales o hábiles, trabaja con la fecha más temprana y dila en el resumen; recomienda además pedir a la Administración, antes de que venza, la prórroga del plazo por vínculos familiares o menores escolarizados (LOEX 63 bis.2; Reglamento 245.2).
- Hechos que se prueban con documento en la solicitud: fecha y hora de la ejecución; arraigo familiar, laboral y social; menores escolarizados (Reglamento 245.2); embarazo o enfermedad (LOEX 57.6; Reglamento 245.7); protección internacional solicitada (LOEX 64.5; Reglamento 245.7; Ley 12/2009, art. 29.2, que califica de especial urgencia la suspensión); supuestos del art. 57.5 LOEX; solicitud previa de residencia por circunstancias excepcionales (LOEX 63.6).
- Actos denegatorios: la denegación de una autorización es un acto de contenido negativo; lo que se suspende es la salida obligatoria o la expulsión que deriva de ella. Pedir la concesión provisional de la autorización es una medida positiva: fundaméntala en circunstancias excepcionales y pídela como subsidiaria.
- Caución y efectos: art. 133 LJCA (puede exigirse; en extranjería, argumenta su improcedencia si no hay perjuicio económico que garantizar); vigencia y modificación, art. 132; el auto que pone fin a la pieza cautelar es apelable en un solo efecto (art. 80.1.a).

### 7. Fondo: qué se comprueba según el acto

- **Expulsión por estancia irregular**: tipo (LOEX 53.1.a), proporcionalidad (LOEX 57.1), prohibición de entrada y su duración (LOEX 58; Reglamento 244.2), límites del art. 57.5 LOEX, motivación de las circunstancias agravantes en la propia resolución, y procedimiento seguido (preferente u ordinario, LOEX 63 y 63 bis; Reglamento 233 y 234). Si hay familia con nacionalidad española o menores, comprueba si el cliente tiene título para residir como familiar de persona española (Reglamento 94) y pondera el interés superior del menor (CE 39; art. 2 de la LO 1/1996).
- **Expulsión por condena** (LOEX 57.2): pena superior a un año por delito doloso y antecedentes no cancelados (art. 136 CP).
- **Denegación de autorización**: cada requisito con el texto vigente del artículo de la vía, la valoración de antecedentes (Reglamento 126.d y 130.2) y la prueba que la Administración no valoró.
- **Extinción**: causa del art. 200.2, audiencia, caducidad y proporcionalidad del art. 202 del Reglamento.
- **Precepto anulado**: lee las notas «Téngase en cuenta que se declara la nulidad…» que devuelva `buscar_articulo` (el Supremo anuló en 2026 incisos o apartados de, entre otros, los arts. 94, 97, 98, 101, 159, 160, 166, 196 y 197 del Reglamento). Si la resolución se funda en lo anulado, ese es un motivo autónomo: lo anulado no se aplica. Cuando la nota habla del «inciso destacado», el texto que devuelve el conector no marca cuál es: no afirmes qué parte se anuló; razona si el caso cumple el precepto en cualquiera de sus lecturas o dile al abogado que lo compruebe en la sentencia.
- Si la resolución depende de una disposición adicional o transitoria (por ejemplo, las adicionales vigésima y vigesimoprimera del Reglamento o la transitoria quinta del Real Decreto 1155/2024), el conector no devuelve su texto: aplica la puerta y explica qué precepto falta antes de construir ese motivo.

## Estrategia y jurisprudencia

- Estructura cada fundamento de fondo con premisa normativa, doctrina (párrafo literal), hecho probado y conclusión; varía el orden si el argumento lo pide.
- Consultas de partida:
  - Expulsión y multa: `consulta="expulsión estancia irregular multa circunstancias agravantes proporcionalidad"`, `base="TS"`; después la misma con `base="AN"`, `tipo_organo="TSJ"` y la provincia. Busca qué circunstancias concretas se han considerado agravantes y si basta la incoación por procedimiento preferente.
  - Cautelar frente a expulsión o salida obligatoria: `consulta="medida cautelar suspensión orden de expulsión arraigo perjuicio irreparable"`, `tipo_resolucion="AUTO"`, `base="AN"`, con la provincia del órgano.
  - Carga de acreditar el arraigo en la cautelar: `consulta="suspensión cautelar expulsión extranjero arraigo familiar carga de la prueba"`, `base="TS"`.
  - Antecedentes: `consulta="antecedentes policiales antecedentes penales cancelados denegación autorización residencia"`, `base="TS"`.
  - Competencia territorial en sanciones: `consulta="competencia territorial expulsión domicilio del recurrente sanción extranjería"`, `base="AN"`.
- Comprueba qué reglamento aplica cada sentencia que cites: muchas de 2025 y 2026 resuelven solicitudes del Reglamento anterior (Real Decreto 557/2011).
- Lee solo las resoluciones que vas a citar (`leer_sentencias`, `parrafos=3`, `terminos`). Cita doctrina, nunca el relato de hechos ni datos personales de aquel pleito. Si el auto o la sentencia recoge la doctrina del Supremo, busca y lee la sentencia del Supremo y cita esa.

### Errores que hay que evitar

- Encabezar ante un «Juzgado de lo Contencioso-Administrativo número…» sin comprobar la denominación actual del órgano en esa sede.
- Presentar un escrito de interposición en un asunto de abreviado: en extranjería el recurso empieza por demanda (art. 78.2 LJCA).
- Ignorar la opción del domicilio en sanciones o elegirla sin acreditar el domicilio (art. 14.1, regla segunda).
- Pedir la cautelar sin prueba documental del arraigo ni de la inminencia de la ejecución.
- Pedir la suspensión de una denegación sin identificar qué efecto se ejecuta (salida obligatoria, expulsión).
- Dejar vencer el plazo de cumplimiento voluntario sin haber pedido la cautelar.
- Descontar mal agosto: no corre para interponer (art. 128.2), pero la cautelar urgente puede pedir habilitación (art. 128.3).
- No acompañar la representación ni la resolución impugnada (art. 45.2 LJCA).
- Citar doctrina del Supremo a través de una sentencia de TSJ que la reproduce, sin leer la del Supremo.

## Documento que se entrega

Escritos en Word según `references/formato-y-organos.md`. Nombres: `demanda-contencioso-<apellido-cliente>-<AAAAMMDD>.docx` y, si se pide por separado, `cautelarisima-<apellido-cliente>-<AAAAMMDD>.docx`. Si el plazo ha vencido: `nota-plazo-vencido-<apellido-cliente>-<AAAAMMDD>.docx`.

Cita las normas en el documento como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca: «artículo N del Real Decreto 1155/2024» (nunca «del Reglamento de extranjería» ni «del Reglamento aprobado por…»), «artículo N de la Ley Orgánica 4/2000» y «Ley 14/2013, de 27 de septiembre». En esta skill, «Reglamento» es solo una abreviatura de trabajo del Real Decreto 1155/2024. Pon la letra o el ordinal delante del artículo y la norma justo detrás del número: «la letra b) del artículo 21.3 de la Ley 39/2015», «el ordinal 1.º de la letra b) del artículo 80.2 del Real Decreto 1155/2024». Con «artículo 21.3.b de la Ley 39/2015» o «artículo 197.4, letra a), del Real Decreto…», `verificar_escrito` no identifica la norma o atribuye el artículo a la última que se mencionó antes. `verificar_escrito` tampoco reconoce los artículos de las directivas de la UE: los da por no identificados o, dentro de un escrito, los atribuye a la última norma española citada y les pone «✔ existe». Compruébalos siempre con `buscar_articulo` (`ley="Directiva 2003/86/CE"`, por ejemplo) y no te fíes de lo que diga el verificador sobre ellos.

**Demanda de procedimiento abreviado**

1. Encabezamiento: «AL TRIBUNAL DE INSTANCIA DE [SEDE], SECCIÓN DE LO CONTENCIOSO-ADMINISTRATIVO (REPARTO)», con la denominación comprobada en el paso 2.
2. Comparecencia: abogado (y procurador, si lo hay) en nombre de `[NOMBRE Y APELLIDOS]`, `[NIE]`, `[DOMICILIO]`, con la representación que se acompaña; resolución impugnada (órgano, fecha, expediente, fecha de notificación); declaración de que se interpone recurso por el procedimiento abreviado del art. 78 LJCA.
3. HECHOS en ordinales, cada uno con su documento o folio del expediente.
4. FUNDAMENTOS DE DERECHO. I. Jurídico-procesales: jurisdicción, competencia objetiva y territorial, legitimación, postulación, actividad impugnable, plazo con fechas, procedimiento y cuantía. II. De fondo: un fundamento por motivo. III. Costas (art. 139 LJCA leído).
5. SUPLICO: anulación de la resolución y reconocimiento de la situación jurídica que proceda (concesión de la autorización, sustitución de la expulsión por multa o su anulación), con costas.
6. OTROSÍES: medida cautelar (si no va en escrito aparte); vista y prueba con puntos de hecho y medios (arts. 60 y 78 LJCA) o fallo sin vista; reclamación del expediente administrativo; habilitación de días si procede.
7. Lugar, fecha, firmas y relación numerada de documentos (representación, resolución impugnada, justificante de notificación, pruebas de arraigo).

**Nota de plazo vencido** (para el abogado, no para presentar): encabezamiento con el asunto y la resolución; conclusión en la primera línea (plazo vencido, fecha y consecuencia); cómputo con fechas y preceptos; resultado de las comprobaciones de notificación y suspensión; alternativas con su precepto, plazo y viabilidad; riesgo actual (salida obligatoria o expulsión) y próximo paso.

**Solicitud de medida cautelarísima** (escrito separado o primer otrosí): encabezamiento igual; «SOLICITUD DE MEDIDA CAUTELAR INAUDITA PARTE (ART. 135 LJCA)»; hechos de especial urgencia con fecha y hora; periculum (qué se pierde si se ejecuta); ponderación de intereses (art. 130); apariencia de buen derecho solo si es patente; menores (art. 135.2); habilitación de días (art. 128.3); SUPLICO: suspensión de la ejecución de la expulsión o de la salida obligatoria, comunicación urgente a la autoridad que deba ejecutarla y, subsidiariamente, tramitación por el art. 131.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió antes de empezar.
- [ ] Competencia objetiva y territorial fijadas con los artículos leídos y la denominación del órgano comprobada; si no se pudo, la tarea se detuvo.
- [ ] Plazo con fecha de notificación, art. 46 LJCA, agosto y fecha final; asistencia jurídica gratuita valorada. Si ha vencido: notificación y suspensión comprobadas, ninguna demanda redactada y nota de plazo vencido entregada.
- [ ] Cautelar: urgencia documentada, arts. 129 a 135 LJCA leídos, supuestos de suspensión de la LOEX y del Reglamento comprobados.
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación; ninguna disposición adicional o transitoria no disponible se ha suplido con memoria.
- [ ] Cada ECLI se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`, y aplica el reglamento correcto.
- [ ] Marcadores en los datos no facilitados; ningún dato del cliente en las consultas.
- [ ] `verificar_escrito` pasado sobre la demanda y sobre la solicitud cautelar.
- [ ] Resumen en el chat según el apartado 7 del formato: escritos y órgano, plazo y fecha límite con su precepto, urgencia de la cautelar, documentos que faltan y riesgos, tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene) y próximo paso (presentación y seguimiento de la pieza cautelar).
