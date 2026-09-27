---
name: expulsion-procedimiento-sancionador
description: >-
  Defensa en vía administrativa del procedimiento sancionador de extranjería y de expulsión (LOEX
  arts. 50-58, 63 y 63 bis; arts. 215-252 del Reglamento aprobado por el Real Decreto 1155/2024),
  ordinario, preferente o simplificado: alegaciones al acuerdo de iniciación o a la propuesta,
  prueba, caducidad y prescripción, multa en lugar de expulsión por estancia irregular, expulsión
  por condena (art. 57.2), residentes de larga duración y protegidos del art. 57.5. Entrega el
  escrito de alegaciones en Word. Úsala con «me han abierto expediente de expulsión», «acuerdo de
  iniciación», «tengo 48 horas», «propuesta de resolución», «multa o expulsión». Si hay detención o
  petición de internamiento, usa también internamiento-cie; si la expulsión ya se ejecutó y el
  cliente quiere volver, prohibicion-entrada-antecedentes.
---

# Expulsión y procedimiento sancionador de extranjería

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Infracción imputada, sanción posible, exclusiones y prescripción** → `buscar_articulo` (`ley="LOEX"`, artículos 53, 54, 55, 56, 57 y 59).
- **Modalidad de procedimiento, plazos de alegaciones, prueba y audiencia, caducidad** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 216, 221, 224 a 240; la ley en los artículos 63 y 63 bis con `ley="LOEX"`).
- **Contenido del acuerdo de expulsión, prohibición de entrada, cumplimiento voluntario y ejecución** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 24, 241 a 248; `ley="LOEX"`, artículos 58 y 64).
- **Cómputo de plazos, caducidad y ejecutividad** → `buscar_articulo` (`ley="LPAC"`, artículos 21, 25, 30, 31, 53, 90 y 95).
- **Expulsión por condena** → `buscar_articulo` (`ley="CP"`, el artículo del tipo penal de la sentencia y el 136 para la cancelación).
- **Derecho de la Unión** → `buscar_articulo` (`ley="Directiva 2008/115/CE"`, artículos 5, 6, 7 y 11; `ley="Directiva 2003/109/CE"`, artículo 12 si es residente de larga duración).
- **Doctrina sobre multa o expulsión y circunstancias agravantes** → `buscar_sentencias` (`consulta="estancia irregular expulsión multa circunstancias agravantes"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="01/01/2023"`) + `leer_sentencias` (`parrafos=3`, `terminos="multa expulsión agravantes proporcionalidad"`).
- **Doctrina sobre expulsión por condena y residentes de larga duración** → `buscar_sentencias` (`consulta="expulsión residente de larga duración 57.2 amenaza real ponderación"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`) y el TSJ del territorio con `base="AN"`, `jurisdiccion="CONTENCIOSO"` y `provincia`.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Cuando el precepto lleve letra o «bis», escribe «la letra a) del artículo 53.1 de la Ley Orgánica 4/2000» o «el apartado 2 del artículo 63 bis de la Ley Orgánica 4/2000», y pon la norma en cada cita: con «53.1.a)» o «63 bis.2», o sin norma detrás, el verificador no la identifica o la atribuye a la norma citada antes. El verificador no reconoce las Directivas: atribuye sus artículos a otra norma del escrito; si el artículo se leyó con `buscar_articulo` en su Directiva, la cita es correcta y no se cambia.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Se ha notificado un **acuerdo de iniciación** de expediente sancionador de extranjería (ordinario, preferente o simplificado) y hay que presentar alegaciones y proponer prueba.
- Se ha notificado la **propuesta de resolución** y corre el trámite de audiencia.
- El expediente lleva meses abierto sin resolución notificada: **escrito pidiendo la declaración de caducidad y el archivo**.
- Escritos accesorios en vía administrativa: suspensión del expediente porque el cliente pidió arraigo antes de la iniciación; prórroga del plazo de cumplimiento voluntario; sustitución de la expulsión por salida obligatoria.

No la uses para:

- Oponerse al internamiento, recurrir el auto o pedir el cese → `internamiento-cie` (puede ir en paralelo con esta).
- Levantar una prohibición de entrada ya impuesta, una alerta Schengen o cancelar antecedentes → `prohibicion-entrada-antecedentes`.
- Recurrir la resolución de expulsión ya dictada → `recurso-administrativo-extranjeria` (reposición) o `recurso-contencioso-extranjeria` (recurso judicial y medida cautelarísima). Esta skill solo deja anotados el pie de recursos y la manifestación de la voluntad de recurrir.
- La expulsión sustitutiva de la pena que acuerda el juez penal (art. 89 del Código Penal): se discute en el proceso penal, no aquí.
- Medidas de orden público contra ciudadanos de la Unión y sus familiares sujetos al Real Decreto 240/2007 → `ciudadanos-ue-y-familiares`.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. Los marcados como imprescindibles detienen la redacción si faltan.

1. **Documento notificado** (acuerdo de iniciación, propuesta o resolución), íntegro. Imprescindible.
2. **Fecha y hora de la notificación** y cómo se hizo (en mano, sede electrónica, a través del letrado). Imprescindible: sin ella no se calcula el plazo.
3. **Modalidad** que indica el acuerdo (ordinario, preferente, simplificado), **infracción imputada** con su letra del artículo de la LOEX, instructor, órgano que resuelve y número de expediente. Imprescindible.
4. **Fecha del acuerdo de iniciación** y cualquier actuación posterior (suspensiones, requerimientos, paralizaciones atribuidas al cliente). Imprescindible para la caducidad.
5. **Situación personal**: ¿está detenido?, ¿hay medidas cautelares (pasaporte retirado, presentaciones)?, ¿se ha pedido internamiento? Si hay detención, abre también `internamiento-cie`.
6. **Situación administrativa**: fecha y forma de entrada, pasaporte, autorizaciones anteriores y su extinción, residencia de larga duración, permiso de otro Estado de la Unión, solicitudes pendientes (sobre todo arraigo presentado antes de la iniciación: fecha y justificante de registro), protección internacional.
7. **Vínculos**: cónyuge o pareja y su situación, hijos (edad, nacionalidad, escolarización), convivencia y empadronamiento, trabajo, estudios, salud, embarazo, prestaciones públicas, condición de víctima de trata o de redes.
8. **Antecedentes**: condenas (delito, pena, fecha de firmeza, de extinción y de cancelación), detenciones, procesos penales pendientes (juzgado y número), expulsiones o prohibiciones de entrada previas, órdenes de salida incumplidas.
9. **Pruebas disponibles**: documentos que el cliente puede aportar y los que hay que pedir a otras Administraciones.
10. Opcional: capacidad económica (para graduar la multa), riesgos en el país de origen, preferencia del cliente si la expulsión es inevitable (salir voluntariamente o no).

No redactes al primer disparo: si falta un dato imprescindible, pregúntalo. Para lo que el abogado no tenga, usa marcadores (`[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[NÚMERO DE EXPEDIENTE]`).

## Requisitos y comprobaciones

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo. Si la respuesta trae una nota «Téngase en cuenta…» (nulidad declarada por el Tribunal Supremo, como la sentencia de julio de 2026 publicada en `BOE-A-2026-19632`, o una reforma), léela y aplícala: lo anulado no se aplica ni se cita como vigente. Los números que siguen son el mapa, no el texto.

### 1. Modalidad y plazo del trámite

- Identifica la modalidad con los artículos 216, 225, 233 y 237 del Reglamento (`ley="BOE-A-2024-24099"`) y el 63 y 63 bis de la LOEX. Comprueba que la infracción imputada encaja en la modalidad elegida: el preferente solo procede en los supuestos del art. 233 (y 63.1 LOEX); si se aplica a una estancia irregular, el acuerdo debe motivar una de las circunstancias de su párrafo segundo. Si no la motiva, alega la elección indebida: en el preferente no hay plazo de salida voluntaria (art. 63.1 LOEX, último párrafo).
- Plazos que debes comprobar y citar con su artículo: alegaciones del preferente (art. 234.1 del Reglamento y 63.4 LOEX), prueba y audiencia del preferente (art. 234.4); alegaciones del ordinario (art. 227.1), periodo de prueba (art. 228.1), audiencia (art. 231.1), actuaciones complementarias y agravación (art. 232.1 y 232.3); simplificado (arts. 237 y 238).
- **Plazos por horas**: lee el art. 30.1 LPAC. Da al abogado la hora límite calculada de la forma más estricta (horas seguidas desde el minuto de la notificación) y, aparte, la que resultaría del art. 30.1; recomienda presentar antes de la primera. Si la hora estricta cae en sábado, domingo o festivo, lee también el art. 31.2.b) LPAC (lo presentado por registro electrónico en día inhábil se entiende presentado a primera hora del siguiente hábil) y avisa de que, si esa primera hora es posterior al límite estricto, conviene además entregar copia ese mismo día al instructor con sello de entrada.
- **Contenido mínimo del acuerdo**: coteja el acuerdo con el art. 226.1 y, si puede terminar en expulsión, con el art. 242 (asistencia jurídica gratuita, intérprete, advertencia de la prohibición de entrada). Anota cada omisión y valora si causó indefensión real antes de alegarla.
- **Asistencia letrada e intérprete**: arts. 22.2 y 63.3 LOEX; arts. 226.3 y 234.2 del Reglamento.
- **Efecto de no alegar**: el acuerdo puede valer como propuesta de resolución (arts. 226.2 y 234.3). Adviértelo al abogado y no dejes pasar el plazo.

### 2. Caducidad y prescripción

- **Caducidad**: plazo máximo para dictar y notificar la resolución desde el acuerdo de iniciación (art. 224.1 del Reglamento; el del simplificado en el art. 237). Descuenta solo la paralización imputable al interesado o la suspensión acordada. Efectos con los arts. 25.1.b) y 95.3 LPAC: el procedimiento caducado no interrumpe la prescripción. Da la fecha de vencimiento y el precepto.
- **Prescripción de la infracción**: art. 56.1 LOEX y art. 224.2 del Reglamento (plazos, cómputo, interrupción y reanudación). Si la infracción es la estancia irregular, busca antes doctrina sobre su carácter continuado (`consulta="prescripción infracción estancia irregular 53.1.a"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `tipo_organo="TSJ"`); no afirmes la prescripción sin ella.
- **Prescripción de la sanción**: art. 56.2 y 56.3 LOEX y art. 224.3 del Reglamento (la de expulsión no empieza a correr hasta que vence la prohibición de entrada).

### 3. Tipicidad y prueba de los hechos

- Compara los hechos del acuerdo con el tipo exacto (arts. 53 y 54 LOEX). Ejemplo típico: el art. 53.1.a) no se comete si la autorización lleva caducada tres meses o menos o si se pidió la renovación en plazo; compruébalo con el texto que devuelva el conector.
- La resolución no puede usar hechos distintos de los instruidos (arts. 221.2 y 232.3 del Reglamento; art. 90.2 LPAC).
- Pide el expediente completo (art. 53.1.a) LPAC) y propón prueba útil: documental propia, informes de otras Administraciones (art. 229), estado de la solicitud de arraigo, testifical sobre convivencia.

### 4. Multa o expulsión

- La expulsión solo sustituye a la multa en las infracciones del art. 57.1 LOEX, en atención al principio de proporcionalidad y con resolución motivada; nunca se imponen juntas (art. 57.3). Graduación: art. 55.3 y 55.4 LOEX y art. 221.3 del Reglamento (circunstancias personales y familiares).
- **Estancia irregular (art. 53.1.a)**: busca y lee la doctrina actual del Tribunal Supremo sobre la sanción procedente y sobre qué circunstancias son o no agravantes. Copia la lista de agravantes del párrafo que leas; no la reconstruyas de memoria (si el párrafo llega cortado, menciona solo las que aparezcan y, para el riesgo de incomparecencia, las circunstancias del art. 233 del Reglamento). Contrasta después cada agravante que invoque la Administración con el expediente: si no consta motivada en la resolución, dilo.
- **Preferente mal elegido**: si el acuerdo invoca riesgo de incomparecencia, compara cada circunstancia del art. 233 con los documentos (domicilio, pasaporte —también si lo retiró la propia policía como medida cautelar del art. 61.1 LOEX—, prueba de la entrada). Busca además cómo trata el TSJ del territorio la motivación insuficiente del preferente: si la considera irregularidad no invalidante cuando la causa existe, apoya la alegación en que la causa no existe, no en el defecto de motivación.
- Advierte al abogado de que la multa no regulariza: va seguida de la salida obligatoria (art. 24 del Reglamento).
- **Excepciones a la decisión de retorno** (Directiva 2008/115/CE, art. 6.2 a 6.5): permiso de residencia de otro Estado miembro (art. 57.4 LOEX, párrafo segundo, y art. 241.2 del Reglamento), procedimiento de renovación pendiente.
- **Arraigo solicitado antes de la iniciación**: art. 63.6 LOEX y art. 240.1 del Reglamento (este regula el preferente: el instructor pide informe y, si continúa, lo hace por el ordinario). Pide la suspensión y aporta el justificante con fecha de registro anterior al acuerdo. Una solicitud presentada después de la iniciación no suspende el expediente: dilo al abogado y valora la revocación posterior del art. 240.2 y 240.3.
- **Personas protegidas**: art. 57.5 LOEX (nacidos en España con residencia legal, residentes de larga duración, antiguos españoles de origen, perceptores de las prestaciones que enumera, y su cónyuge, ascendientes e hijos a cargo en las condiciones del último párrafo), salvo las excepciones que el propio apartado fija en su primer párrafo; art. 57.6 (no devolución, embarazo). Directiva 2008/115/CE, art. 5 (interés del menor, vida familiar, salud).
- **Víctimas o testigos de redes y trata**: art. 59 LOEX; el instructor debe informar de esa vía (art. 59.2). Para la autorización de la víctima de trata usa `victimas-trata`.

### 5. Expulsión por condena penal (art. 57.2 LOEX)

- Comprueba los cuatro elementos con el texto vigente: condena por conducta dolosa, dentro o fuera de España, delito sancionado con pena privativa de libertad superior a un año, antecedentes no cancelados. Busca la doctrina del Supremo sobre si el umbral se refiere a la pena en abstracto o a la impuesta (`consulta="57.2 pena prevista en abstracto superior a un año"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`) y aplica la que leas. Lee también el tipo penal de la sentencia con `buscar_articulo` (`ley="CP"`) y compara su pena con el umbral que fije esa doctrina; si no lo supera, la falta de presupuesto del art. 57.2 es el motivo principal (archivo) y la protección del residente va como subsidiaria.
- Si ya se cumplen los plazos del art. 136 del Código Penal (`ley="CP"`), pide la cancelación (skill `prohibicion-entrada-antecedentes`) y alega el apartado 5 de ese artículo solo si encuentras doctrina que lo aplique a la expulsión.
- **Residente de larga duración**: art. 57.5.b) LOEX y Directiva 2003/109/CE, art. 12 (amenaza real y suficientemente grave; duración de la residencia, edad, consecuencias familiares, vínculos); el art. 241.1 del Reglamento enuncia las causas de expulsión, incluida la condena, sin perjuicio del art. 57.5 y 57.6 LOEX. Busca la doctrina del Supremo que excluye el automatismo y exige una amenaza actual. Comprueba en la tarjeta si la residencia es de larga duración-UE (arts. 175-181 del Reglamento) o nacional (arts. 182-185): la Directiva regula el estatuto de la Unión; si es nacional, dilo al abogado y apóyate sobre todo en el art. 57.5.b) LOEX.
- **Resto de residentes**: busca la doctrina sobre la motivación reforzada de las circunstancias personales y familiares en la expulsión por condena (`consulta="expulsión 57.2 motivación circunstancias personales familiares arraigo"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`).
- **Procesos penales pendientes**: art. 57.7 LOEX y art. 247 del Reglamento (autorización judicial en tres días). Decide con el abogado si conviene acreditarlos en el expediente.

### 6. Prohibición de entrada y ejecución

- Duración máxima, supuesto excepcional con informe de la Comisaría General y no imposición o revocación si el cliente sale durante el expediente o en el plazo voluntario: art. 58.1 y 58.2 LOEX y art. 244.2 del Reglamento. Pide la duración mínima con motivos concretos y explica al cliente cómo comunicar la salida (formas del art. 244.2).
- Ordinario: plazo de cumplimiento voluntario, su prórroga y la regla de los menores escolarizados (art. 63 bis.2 LOEX; art. 245.2 del Reglamento); sin internamiento durante ese plazo (arts. 63 bis.3 LOEX, 223.2 y 243.1 del Reglamento).
- Preferente: ejecución inmediata (art. 63.7 LOEX; art. 235 del Reglamento). Avisa de que solo la frena una medida cautelar judicial (`recurso-contencioso-extranjeria`; art. 135 LJCA).
- Sustitución por salida obligatoria: art. 245.5 del Reglamento (requisitos acumulativos). Suspensión por protección internacional, embarazo o enfermedad: art. 245.7.
- Privado de libertad: la voluntad de recurrir se hace constar como dice el art. 222 del Reglamento (art. 22.3 LOEX).

## Estrategia y jurisprudencia

Ordena el análisis así y no pases al siguiente escalón sin cerrar el anterior:

1. **Forma**: modalidad correcta, contenido del acuerdo, asistencia letrada e intérprete, caducidad, prescripción.
2. **Hechos**: ¿están probados?, ¿encajan en el tipo?
3. **Sanción**: multa o expulsión; agravantes motivadas o no; protección del art. 57.5; condena del art. 57.2.
4. **Consecuencias**: duración de la prohibición de entrada, plazo voluntario y su prórroga, salida obligatoria.

Consultas que debes lanzar según el caso (siempre `jurisdiccion="CONTENCIOSO"`; para el TSJ del territorio `base="AN"` y `provincia`):

| Cuestión | `consulta` | Filtros |
|---|---|---|
| Sanción preferente en la estancia irregular | «estancia irregular multa preferente circunstancias agravantes» | `base="TS"`, `fecha_desde="01/01/2023"` |
| Qué es y qué no es agravante | «circunstancias de agravación estancia irregular pasaporte entrada antecedentes» | `base="TS"` |
| Preferente mal elegido | «procedimiento preferente riesgo de incomparecencia motivación salida voluntaria» | `base="AN"`, `provincia` |
| Arraigo familiar frente a la expulsión | «expulsión proporcionalidad arraigo familiar convivencia hijos menores» | `base="AN"`, `provincia` |
| Residente de larga duración | «expulsión residente de larga duración 57.2 amenaza real ponderación» | `base="TS"` |
| Caducidad | «caducidad procedimiento sancionador expulsión seis meses» | `base="AN"`, `tipo_organo="TSJ"` o `provincia` |
| Duración de la prohibición | «expulsión prohibición de entrada cinco años reducción proporcionalidad» | `base="AN"`, `tipo_organo="TSJ"` o `provincia` |

- Lee con `leer_sentencias` (`parrafos=3` y `terminos` de la cuestión) solo las que vayas a citar. Prefiere las más recientes del Supremo y, para cuestiones de hecho, las del TSJ que resolverá la apelación.
- Antes de citar un párrafo, comprueba que es razonamiento de la Sala y no el resumen de lo que alegan las partes o de lo que decía la sentencia recurrida: los párrafos que devuelve el conector a menudo reproducen esas posiciones (por ejemplo, la tesis del «automatismo» de la expulsión del residente, que el Supremo rechaza). Si solo tienes esa clase de párrafos, no cites la sentencia. Cuando una sentencia transcriba otra del Supremo, dilo así («que transcribe la STS nº …»).
- **Comprueba qué reglamento aplicó cada sentencia**: las dictadas sobre hechos anteriores al 20/05/2025, y muchas posteriores, aplican el Reglamento anterior (Real Decreto 557/2011), con otra numeración. No traslades esa numeración: cita el artículo vigente tras leerlo y usa la sentencia solo por su doctrina.
- **Derecho de la Unión**: las sentencias del Supremo que leas citan las del TJUE que fijan la doctrina de multa o expulsión. Ábrelas con `buscar_por_cita` usando el número de asunto que aparezca en el párrafo leído; si `base="TJUE"` da resultados ajenos, no insistas por texto.
- Motivos típicos por los que se desestima la defensa y que debes prevenir con prueba: empadronamiento sin convivencia real acreditada, vínculos familiares sin dependencia, carencia de pasaporte o de constancia de la entrada, incumplimiento de una salida obligatoria anterior, antecedentes o detenciones relevantes.
- En el escrito, cada fundamento de doctrina lleva el párrafo literal entre comillas y después órgano, fecha, número y ECLI tal como los devolvió `leer_sentencias`.

## Documento que se entrega

**Escrito de alegaciones** (al acuerdo de iniciación o a la propuesta de resolución) o, si procede, **escrito de solicitud de caducidad y archivo**. Formato según `references/formato-y-organos.md` del plugin.

- Destinatario: el instructor que designa el acuerdo, en el expediente del Delegado o Subdelegado del Gobierno que resolverá (art. 221 del Reglamento). Toma el órgano, la unidad y el número del propio acuerdo; si no constan, marcador.
- Estructura:
  1. Encabezamiento: `AL INSTRUCTOR DEL EXPEDIENTE SANCIONADOR [NÚMERO DE EXPEDIENTE] — [DELEGACIÓN O SUBDELEGACIÓN DEL GOBIERNO EN ...]`.
  2. Comparecencia: datos del interesado, representación del letrado y domicilio a efectos de notificaciones.
  3. Objeto: trámite que se evacua, fecha de notificación y precepto del plazo.
  4. ALEGACIONES numeradas (PRIMERA.-, SEGUNDA.-…): primero las de forma (caducidad, prescripción, modalidad, defectos del acuerdo), después hechos y circunstancias personales, después la sanción (multa, ausencia de agravantes, protección) y por último la prohibición de entrada y la ejecución. Cada alegación con premisa normativa, doctrina, hecho y conclusión, sin repetir la misma secuencia de subtítulos.
  5. PROPOSICIÓN DE PRUEBA: cada medio con lo que acredita. En las alegaciones a la propuesta de resolución (audiencia de los arts. 231.1 y 234.4) ya no se propone prueba: sustituye este apartado por la relación de documentos que se aportan y lo que acredita cada uno.
  6. SOLICITA: principal (archivo por caducidad o prescripción, inexistencia de infracción o falta del presupuesto del art. 57.2; o, si la infracción no se discute, multa en lugar de expulsión) y subsidiarias en orden (multa en su cuantía mínima con arreglo a la capacidad económica; si hubiera expulsión, prohibición de entrada mínima, plazo de cumplimiento voluntario máximo y su prórroga; suspensión del art. 63.6 LOEX cuando proceda). Si el expediente es preferente sin causa, pide también que continúe por el ordinario.
  7. OTROSÍ: copia íntegra del expediente; en su caso, suspensión por solicitud previa de arraigo.
  8. Lugar, fecha y firma; relación numerada de documentos.
- En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» y el resto de normas como indica el apartado 4 de `references/formato-y-organos.md` (por ejemplo, «Ley Orgánica 4/2000», no «Reglamento de Extranjería»), para que `verificar_escrito` las reconozca.
- Nombre del archivo: `alegaciones-expulsion-<apellido-cliente>-<AAAAMMDD>.docx` (o `solicitud-caducidad-expulsion-…`).

## Comprobación final

Antes de entregar, comprueba y marca cada punto:

- [ ] Puerta cumplida: `estado` respondió al empezar.
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación y el escrito dice lo que dice su texto vigente (Reglamento siempre con `ley="BOE-A-2024-24099"`).
- [ ] Ninguna numeración del Reglamento anterior presentada como vigente.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; la cita es doctrina, no hechos ni datos de las partes de otro pleito.
- [ ] `verificar_escrito` pasado sobre el texto completo y sus avisos resueltos.
- [ ] Plazo del trámite con fecha y hora de notificación, precepto y fecha u hora final; fecha de caducidad calculada con el art. 224.
- [ ] Marcadores en todos los datos que faltan; ningún dato inventado.
- [ ] Súplica con principal y subsidiarias coherentes con las alegaciones.
- [ ] Resumen para el abogado según el apartado 7 del formato: qué se ha preparado y para qué órgano, plazo y hora o fecha límite con su precepto, documentos que faltan y riesgos (preferente, ejecución inmediata, internamiento), tabla de jurisprudencia citada (ECLI · órgano · fecha · qué sostiene) y próximo paso (presentación; recurso si se dicta expulsión).
