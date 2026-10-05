---
name: sucesion-empresa-contratas
description: >-
  Analiza sucesión de empresa (art. 44 ET), sucesión de plantilla, subrogación por convenio o pliego,
  contratas y subcontratas de propia actividad (art. 42 ET) y cesión ilegal de trabajadores (art. 43 ET), y
  entrega informe de riesgo en Word (y nota para el abogado, si la pides). Úsala cuando digan «cambio de adjudicataria», «nos
  quedamos la contrata», «subrogación del personal», «compramos el negocio», «reversión del servicio», «la
  principal responde de los salarios», «cesión ilegal» o «prestamismo laboral». Sirve a la empresa (entrante,
  saliente, principal, contratista, cedente o cesionaria) y al trabajador. Para fijar el convenio de la contrata
  usa convenio-aplicable; para cuantificar, calculo-indemnizacion-despido; para demandar, redactar-demanda-despido
  o reclamacion-cantidad; si la transmisión trae despidos masivos, despido-colectivo-empresa.
---

# Sucesión de empresa, subrogación, contratas y cesión ilegal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Sucesión, responsabilidad solidaria, convenio de origen, información y consultas** → `buscar_articulo` (`ley="ET"`, artículos `"44"` y `"64"`); responsabilidad frente a la Seguridad Social por sucesión → `buscar_articulo` (`ley="LGSS"`, artículos `"142"` y `"168"`).
- **Contratas y subcontratas** → `buscar_articulo` (`ley="ET"`, `articulo="42"`) y, si comparten centro, (`ley="LPRL"`, `articulo="24"`).
- **Cesión ilegal y su sanción** → `buscar_articulo` (`ley="ET"`, `articulo="43"`) y (`ley="BOE-A-2000-15060"`, artículos `"7"` y `"8"`).
- **Venta de unidad productiva en concurso y contratos públicos** → `buscar_articulo` (`ley="TRLC"`, artículos `"221"`, `"222"` y `"224"`) y (`ley="LCSP"`, `articulo="130"`). Comprueba que la cabecera de la respuesta dice «Ley Concursal (RDL 1/2020)» y «LCSP (Ley 9/2017)».
- **Subrogación impuesta por convenio y convenio de la contrata** → `buscar_convenio` + `leer_convenio` (`buscar_en="subrogación"` y después `articulo` con el número que salga) + `vigencia_convenio`. Compara la fecha de publicación del texto que devuelve `leer_convenio` con el último «CONVENIO COLECTIVO (TEXTO NUEVO)» que lista `vigencia_convenio`: si hay un texto posterior, el conector puede estar leyendo el anterior; busca el nuevo en internet en el boletín oficial (enlace y fecha de consulta) o avisa de que el artículo leído puede haber cambiado.
- **Doctrina sobre sucesión de plantilla, subrogación convencional, propia actividad y cesión ilegal** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`, `tipo_resolucion="SENTENCIA"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión); Directiva 2001/23/CE → `buscar_sentencias` (`base="TJUE"`).
- **Empresas implicadas** (denominación, administradores, disolución o concurso, vínculos de grupo) → `buscar_empresa_mercantil` con cada una.
- **Revisión del documento antes de entregarlo** → cada redactor pasa `verificar_escrito` sobre las frases de su sección que citan normas (no sobre el documento entero) y el ensamblado de `redaccion-rapida` comprueba que cada ECLI o ROJ citado figure entre las fuentes leídas; `buscar_por_cita` solo para una sentencia que aporte el abogado y no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Pregunta primero a quién defiende el abogado. La empresa quiere saber qué asume y cómo limitarlo; el trabajador, a quién puede reclamar y hasta cuándo; la representación legal, qué información y qué consultas le deben.

| Situación | Figura que se analiza |
|---|---|
| Compra, arrendamiento o aportación de un negocio, centro o unidad productiva con sus medios | Sucesión legal (art. 44.1 y 44.2 ET) |
| Cambio de contratista en una actividad que descansa en la mano de obra (limpieza, vigilancia, restauración colectiva, atención telefónica) y la entrante asume parte de la plantilla | Sucesión de plantilla: art. 44 ET según doctrina (ver «Estrategia») |
| Cambio de contratista con cláusula de subrogación en el convenio sectorial o en el pliego | Subrogación convencional o contractual, en sus términos; y comprobación de si además hay sucesión de plantilla |
| Cambio de contratista sin medios, sin plantilla asumida y sin cláusula | No hay subrogación: la saliente decide sobre sus contratos → `carta-despido-objetivo` o `despido-colectivo-empresa` |
| El servicio vuelve a la Administración o al titular (reversión, fin de arrendamiento) | Sucesión solo si se dan los requisitos del art. 44 o lo impone norma, convenio o acuerdo (art. 130.3 LCSP): busca doctrina específica |
| Fusión o escisión de sociedades | Art. 44 ET, con la información al tiempo de convocar las juntas (art. 44.8) |
| Venta de una unidad productiva dentro de un concurso | Arts. 221, 222 y 224 del texto refundido de la Ley Concursal: decide el juez del concurso |
| Encargo de obras o servicios de la propia actividad | Responsabilidad de la principal (art. 42 ET) |
| El contratista solo aporta personas y la principal organiza y dirige | Cesión ilegal (art. 43 ET) |

Derivaciones: convenio de los trabajadores de una contrata o tras la sucesión → `convenio-aplicable`; homogeneizar condiciones tras la sucesión → `modificacion-sustancial-condiciones`; traslados derivados → `movilidad-geografica-funcional`; importes → `calculo-indemnizacion-despido` o `finiquito-liquidacion`; conciliación y demanda → `papeleta-conciliacion`, `redactar-demanda-despido`, `reclamacion-cantidad`. Si la cesión la hace una empresa de trabajo temporal autorizada, la cesión es lícita (art. 43.1 ET) y su régimen excede de esta skill.

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ Parte a la que se asesora y qué pregunta concreta hay que contestar (asumir o no una plantilla, deudas heredadas, riesgo de cesión ilegal, reclamación del trabajador).
2. ★ Operación: tipo (compraventa, arrendamiento, cambio de adjudicatario, reversión, fusión, venta en concurso), fecha prevista o fecha de efectos, y documentos que la soportan (contrato, pliego, acta de adjudicación, auto del juez del concurso).
3. ★ Qué pasa de una empresa a otra: activos, locales, maquinaria, clientes, marca, sistemas informáticos, mandos intermedios. Si la actividad descansa esencialmente en la mano de obra o en medios materiales relevantes.
4. ★ Plantilla afectada: número total, cuántos asume la entrante y con qué funciones y categorías (mandos y personal cualificado), antigüedades y modalidades de contrato.
5. ★ Convenio aplicable en la saliente y en la entrante, y si alguno impone subrogación: requisitos (antigüedad mínima en el servicio, documentación que debe entregar la saliente, plazos, trabajadores excluidos).
6. ★ Representación legal de los trabajadores en cada empresa y si se ha informado o consultado (fechas).
7. Deudas pendientes con los trabajadores (salarios, finiquitos, indemnizaciones) y con la Seguridad Social; certificaciones de descubiertos pedidas y su fecha.
8. Para contratas: objeto del contrato mercantil, si forma parte de la propia actividad de la principal, si comparten centro, libro registro y comunicaciones hechas.
9. Para cesión ilegal: quién da las órdenes, fija horarios, vacaciones y sanciones; de quién son las herramientas, uniformes y sistemas; cómo se factura (por horas o personas o por resultado); si la contratista tiene estructura propia y la pone en juego; si la situación sigue vigente o ya terminó; si la cesionaria es una Administración.
10. ★ Si defiende al trabajador y ya hay extinción o negativa a subrogar: fecha de efectos y de la comunicación (corre la caducidad del despido).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la fecha de vigencia.

**A. Sucesión de empresa (art. 44 ET)**

- El cambio de titularidad de una empresa, centro o unidad productiva autónoma no extingue los contratos: el nuevo empresario se subroga en los derechos y obligaciones laborales y de Seguridad Social, incluidos compromisos de pensiones y protección social complementaria (art. 44.1). Hay sucesión cuando se transmite una entidad económica que mantiene su identidad: medios organizados para una actividad, esencial o accesoria (art. 44.2).
- Responsabilidad: cedente y cesionario responden solidariamente durante tres años de las obligaciones laborales anteriores no satisfechas en las transmisiones inter vivos, y también de las posteriores si la cesión se declara delito (art. 44.3). Frente a la Seguridad Social, la responsabilidad por sucesión alcanza la totalidad de las deudas de cotización anteriores (art. 142.1 LGSS) y las prestaciones causadas antes (art. 168.2 LGSS).
- Convenio: sigue el de origen hasta su expiración o hasta que entre en vigor otro aplicable a la entidad transmitida, salvo pacto con la representación legal una vez consumada la sucesión (art. 44.4). Si la unidad conserva su autonomía, los representantes mantienen el mandato (art. 44.5).
- Información: cedente y cesionario informan a sus representantes de fecha prevista, motivos, consecuencias jurídicas, económicas y sociales, y medidas previstas (art. 44.6); sin representantes, a los trabajadores afectados (art. 44.7); con suficiente antelación, y en fusiones y escisiones al convocar las juntas (art. 44.8). No se admite la excusa de que la decisión la tomó la matriz (art. 44.10). Incumplir la información a los trabajadores es infracción grave (apartado 11 del artículo 7 del Real Decreto Legislativo 5/2000); la de los representantes, también (apartado 7 del mismo artículo).
- Medidas laborales con motivo de la transmisión: periodo de consultas con la representación, de buena fe y antes de aplicarlas; si son traslados o modificaciones colectivas, con el procedimiento de los arts. 40.2 y 41.4 ET (art. 44.9).
- Concurso: la enajenación de una unidad productiva es sucesión a efectos laborales y de Seguridad Social, y solo el juez del concurso la declara y delimita (art. 221 del texto refundido de la Ley Concursal); el adquirente se subroga en los contratos afectos (art. 222); no asume deudas anteriores salvo, entre otros casos, las laborales y de Seguridad Social de los trabajadores en cuyos contratos se subroga, con la posible exclusión de la parte que asuma el FOGASA (art. 224.1.3.º), y la exoneración no alcanza a personas especialmente relacionadas con el concursado (art. 224.2).
- Contratos públicos: el pliego debe informar de las condiciones de los trabajadores a subrogar (art. 130.1 LCSP); si la Administración asume el servicio, solo se subroga si lo impone una norma legal, un convenio o un acuerdo de eficacia general (art. 130.3); el pliego obliga al contratista saliente a responder de salarios impagados y cotizaciones, sin que esa obligación pase al nuevo contratista y sin perjuicio del art. 44 ET, y la Administración retiene lo debido al saliente (art. 130.6); si los costes laborales resultan mayores que los informados, el nuevo contratista tiene acción directa contra el antiguo (art. 130.5).

**B. Sucesión de plantilla y subrogación por convenio o pliego**

- La mera sucesión de contratas no es, por sí sola, sucesión de empresa: la subrogación se rige entonces por el convenio o el pliego, con sus requisitos (lee el artículo concreto con `leer_convenio`, comprueba su vigencia en la fecha del cambio y cita su código).
- Cuando la actividad descansa esencialmente en la mano de obra y la entrante asume una parte esencial de la plantilla, en número y competencias, la doctrina aplica el art. 44 ET aunque la asunción venga impuesta por el convenio; con ello llegan la responsabilidad solidaria del art. 44.3 y el resto de efectos. Localiza y lee la doctrina vigente sobre: el concepto de parte esencial, la carga de la prueba de la asunción de plantilla y el alcance de las cláusulas del convenio que limitan la responsabilidad de la entrante. Ordena por fecha y lee la más reciente: la carga de la prueba se ha resuelto de forma distinta según la actividad descanse en la mano de obra o en medios materiales (transporte sanitario, por ejemplo), y la doctrina que la imponía al trabajador puede estar superada para las actividades de mano de obra con subrogación convencional obligatoria.
- Si la actividad descansa en medios materiales relevantes, la asunción de plantilla no basta: analiza qué medios se transmiten.

**C. Contratas y subcontratas (art. 42 ET)**

- Solo la contrata de obras o servicios de la **propia actividad** de la principal genera las responsabilidades del art. 42: busca la doctrina sobre el concepto de propia actividad y aplícala a la actividad real de la principal.
- La principal debe comprobar que la contratista está al corriente con la Seguridad Social pidiendo por escrito la certificación negativa de descubiertos; si la Tesorería no la libra en treinta días improrrogables, queda exonerada (art. 42.1). Cómo se pide la certificación: búscalo en internet en la sede electrónica de la Seguridad Social y cita el enlace con la fecha de consulta; no escribas códigos ni modelos de memoria.
- Responde solidariamente, durante los tres años siguientes a la terminación del encargo, de las obligaciones de Seguridad Social que contratistas y subcontratistas contrajeron durante la contrata (salvo la exoneración del art. 42.1), y de las salariales durante el año siguiente a la finalización del encargo; no responde el particular que contrata obras en su vivienda ni el propietario que no contrata por razón de actividad empresarial (art. 42.2). Además, el propietario de la obra o industria responde de prestaciones si el empresario es declarado insolvente (art. 168.1 LGSS).
- Información: a los trabajadores de la contratista, la identidad de la principal antes de empezar (art. 42.3); a la representación de la principal, los datos de la letra a) a la e) del art. 42.4, con libro registro si comparten centro de forma continuada; la contratista informa a su representación antes de empezar (art. 42.5). Incumplir la información del art. 42.3 o no tener el libro registro con falta de información a los representantes son infracciones graves (apartados 11 y 12 del artículo 7 del Real Decreto Legislativo 5/2000). Si comparten centro, coordinación preventiva (art. 24 LPRL).
- Convenio de la contratista: el del sector de la actividad desarrollada en la contrata, salvo otro convenio sectorial aplicable conforme al título III o convenio propio de la contratista en los términos del art. 84 (art. 42.6). Para determinarlo, deriva a `convenio-aplicable` y busca la doctrina reciente sobre el art. 42.6.

**D. Cesión ilegal (art. 43 ET)**

- Solo las empresas de trabajo temporal autorizadas pueden ceder trabajadores (art. 43.1). Hay cesión ilegal si el contrato entre empresas se limita a poner trabajadores a disposición, o la cedente carece de actividad u organización propia y estable, o de los medios necesarios, o no ejerce las funciones inherentes a su condición de empresario (art. 43.2).
- Efectos: responsabilidad solidaria de cedente y cesionaria frente a trabajadores y Seguridad Social (art. 43.3; también art. 168.2 LGSS para prestaciones); derecho del trabajador a ser fijo, a su elección, en cualquiera de ellas, con los derechos del puesto equivalente de la cesionaria y la antigüedad desde el inicio de la cesión (art. 43.4). Es infracción muy grave (apartado 2 del artículo 8 del Real Decreto Legislativo 5/2000).
- Busca la doctrina sobre los indicios (justificación técnica y autonomía de la contrata, medios propios, ejercicio real del poder de dirección, riesgo empresarial, organización que no se pone en juego), sobre la necesidad de ejercitar la acción mientras la cesión subsiste (comprueba qué momento cuenta: la doctrina lo ha vinculado al inicio de la conciliación o reclamación previa, no a la demanda), sobre la prescripción de las diferencias salariales mientras se discute la cesión (la acción declarativa no la interrumpe: reclámalas a la vez) y sobre el efecto cuando la cesionaria es una Administración pública.

**E. Plazos (léelos con `buscar_articulo` y da fecha inicial, precepto y fecha final)**

- Despido o negativa a subrogar: veinte días hábiles de caducidad (art. 59.3 ET y art. 103.1 LRJS), suspendidos por la papeleta (art. 65 LRJS). Demanda a saliente y entrante, y a la principal si procede. Si se demandó por error a quien no era el empresario, la caducidad frente al verdadero no empieza hasta que consta quién es (art. 103.2 LRJS): no confíes en ello y demanda desde el principio a todos los posibles empleadores.
- Cantidades: un año de prescripción (art. 59.1 y 59.2 ET), dentro de las ventanas de responsabilidad solidaria (tres años del art. 44.3; un año tras el encargo del art. 42.2).
- Plazos del convenio o del pliego (comunicación del cambio, entrega de la documentación por la saliente, liquidación de lo pendiente): léelos en el artículo de subrogación y ponlos en el calendario con su fecha.

## Estrategia y jurisprudencia

**Si defiende a la empresa entrante o adquirente:** calcula antes de asumir personal si lo que asume es una parte esencial en número y competencias; si lo es, presupone la responsabilidad del art. 44.3 y protégete: si hay contrato con la transmitente (compraventa, arrendamiento, aportación), con declaración de deudas, retenciones, garantías e indemnidad; en un cambio de contratista no suele haber contrato entre saliente y entrante, así que requiere de forma fehaciente la documentación y la liquidación que exija el convenio (con sus plazos), el certificado de estar al corriente y el informe de deuda, resérvate la acción de daños que prevea el convenio y la de regreso contra la saliente por lo que pagues como deudor solidario (art. 1145 CC), y pide la colaboración del cliente. En contratación pública exige la información del art. 130 LCSP y apóyate en la retención del art. 130.6. Si la subrogación es solo convencional, cumple sus requisitos y documenta que no se asume más de lo que impone el convenio.

**Si defiende a la saliente o cedente:** cumple la información (art. 44.6 a 44.8) y la entrega de documentación que exija el convenio; si nadie se subroga, trata las extinciones con su propia causa y umbrales (deriva a la skill que toque).

**Si defiende a la principal:** comprueba si la contrata es de propia actividad, pide la certificación del art. 42.1 antes de empezar y periódicamente, cumple la información del art. 42.4 y evita los indicios de cesión (que la contratista organice, dirija, controle y sancione a su personal, con medios propios y facturación por resultado).

**Si defiende al trabajador o a la representación:** identifica a todos los posibles responsables (saliente y entrante, cedente y cesionaria, contratista y principal), demanda a todos dentro de plazo, pide la documentación de la operación y la información del art. 44.6, y ejercita la cesión ilegal mientras subsista.

**Consultas en Jurisprudenciator** (reformula como máximo dos veces; con consultas largas el buscador devuelve autos de inadmisión, por eso usa `tipo_resolucion="SENTENCIA"`):

- Sucesión de plantilla: `consulta="sucesión de plantilla mano de obra parte esencial"`, `base="TS"`, `jurisdiccion="SOCIAL"`, `tipo_resolucion="SENTENCIA"`.
- Subrogación convencional y deudas: `consulta="subrogación convencional sucesión de plantilla responsabilidad solidaria deudas salariales artículo 44"`, mismos filtros; lee la más reciente sobre carga de la prueba.
- Directiva: `consulta="Directiva 2001/23 subrogación impuesta por convenio colectivo parte esencial de los efectivos"`, `base="TJUE"`.
- Reversión: `consulta="reversión servicio público Administración sucesión de empresa plantilla"`, `base="TS"`, `jurisdiccion="SOCIAL"`, `anios=5`.
- Propia actividad: `consulta="contrata propia actividad artículo 42 responsabilidad solidaria empresa principal"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Cesión ilegal: `consulta="cesión ilegal de trabajadores contrata aportación de medios propios poder de dirección"`, `base="TS"`, `jurisdiccion="SOCIAL"`, `anios=5`; y `consulta="cesión ilegal acción mientras subsiste la cesión"`.
- Convenio de la contrata: `consulta="artículo 42.6 convenio colectivo aplicable empresa contratista sector de la actividad"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Diferencias salariales durante la cesión: `consulta="prescripción diferencias salariales cesión ilegal"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Si el caso se discute en un TSJ concreto: `base="AN"`, `jurisdiccion="SOCIAL"`, `tipo_organo="TSJ"`, `provincia` con la sede de la Sala.

Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y transcribe el párrafo de fundamentos, nunca el relato de hechos ni los nombres de aquellas empresas o trabajadores. En el informe, cada conclusión discutida (sucesión de plantilla, propia actividad, cesión ilegal) lleva al menos una resolución leída: es jurisprudencia imprescindible (apartado 8 del formato).

## Documentos que se entregan

Word maquetado según `references/formato-y-organos-laboral.md`.

**1. Informe de riesgo** — `nota-informe-riesgo-sucesion-<empresa>-<AAAAMMDD>.docx` (para el cliente, sin jurisprudencia de relleno):

1. Encargo, parte asesorada y pregunta que se contesta.
2. Hechos relevantes y documentos examinados; lo que falta, en lista.
3. Calificación de la operación: sucesión legal, sucesión de plantilla, subrogación convencional, mera sucesión de contratas, contrata de propia actividad o cesión ilegal, con el artículo y la doctrina leída (párrafo literal y ECLI).
4. Matriz de riesgos en tabla: riesgo · fundamento (artículo o doctrina) · probabilidad (alta, media o baja, con el hecho que la justifica) · consecuencia · medida para reducirlo.
5. Responsabilidades en tabla: obligación · responsable · alcance temporal · precepto.
6. Obligaciones de información y consultas con calendario (quién, a quién, qué contenido, antes de qué fecha). Si se asesora al trabajador, calendario de actuaciones (conciliación mientras subsiste la cesión, demanda, despido con su caducidad) y los derechos de información que puede exigir (arts. 42.3 y 42.7 ET).
7. Recomendaciones y cláusulas que conviene incluir en el contrato entre empresas.
8. Convenio: denominación, código, artículo pertinente leído (el de subrogación en las sucesiones; en la cesión ilegal o la contrata, el convenio de la cesionaria o de la principal para el puesto equivalente, o el del art. 42.6) y vigencia comprobada, con la fecha del texto leído.

**Reparto para la redacción rápida (informe de riesgo):** encargo, hechos y documentos / una sección de calificación por cada figura que se discute (sucesión legal y de plantilla, contrata de propia actividad, cesión ilegal), cada una con su doctrina / matriz de riesgos y responsabilidades en tablas / obligaciones de información y calendario, recomendaciones, cláusulas y convenio.

**2. Nota para el abogado**, solo si el abogado la pide (si no, lo que esta skill manda «a la nota» —calendario, riesgos, cálculos y jurisprudencia con su ECLI— va en el resumen de la entrega) — `nota-abogado-sucesion-<empresa>-<AAAAMMDD>.docx`: artículos leídos con su fecha de vigencia, consultas hechas y resoluciones leídas, puntos discutibles y cómo los resolvería cada parte, plazos con fecha y datos que faltan.

**3. Si el abogado lo pide**, la comunicación informativa del art. 44.6 o 44.7 a la representación o a los trabajadores, o la del art. 42.4 sobre la contrata, como carta (`carta-informacion-sucesion-<empresa>-<AAAAMMDD>.docx`) con cada extremo exigido por el artículo y sin jurisprudencia.

Datos que no se hayan facilitado van con marcadores (`[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[FECHA DE TRANSMISIÓN]`, `[NÚMERO DE TRABAJADORES ASUMIDOS]`).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos 42, 43 y 44 del Estatuto de los Trabajadores que se usan, los de la LGSS, la LISOS, la Ley Concursal o la LCSP que se citan, con la cabecera de la norma comprobada.
- [ ] Convenio identificado con su código, artículo pertinente (subrogación, o puesto equivalente en la cesión) leído con `leer_convenio`, vigencia comprobada con `vigencia_convenio` en la fecha de la operación y texto leído cotejado con el último texto inscrito.
- [ ] Empresas comprobadas con `buscar_empresa_mercantil` (concurso, disolución, administradores comunes).
- [ ] Cada calificación discutida apoyada en una resolución leída con `leer_sentencias` (párrafo de fundamentos) o comprobada con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero); los avisos sobre artículos de convenio o de la Directiva, ignorados tras comprobarlos con `leer_convenio` o `buscar_articulo`.
- [ ] Plazos con fecha inicial, precepto y fecha final; marcadores en vez de datos inventados.
- [ ] Lo obtenido en internet (trámite de la certificación de la Tesorería, pliegos publicados) citado con enlace y fecha de consulta y señalado en el resumen.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y para quién, plazos, responsabilidades cuantificables y de dónde salen, documentos que faltan y riesgos, tabla de jurisprudencia y próximo paso.
