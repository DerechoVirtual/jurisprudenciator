---
name: recurso-administrativo-extranjeria
description: >-
  Escritos en vía administrativa de extranjería conforme a la LPAC y al Reglamento aprobado por el
  Real Decreto 1155/2024. Recurso potestativo de reposición y recurso de alzada contra denegaciones,
  archivos por desistimiento, inadmisiones y extinciones; recurso frente al silencio; contestación a
  requerimientos de subsanación, y alegaciones en trámite de audiencia. Calcula el plazo (arts. 122 y
  124 LPAC), elige el recurso según el pie de la resolución, decide si conviene reponer o ir directo
  al contencioso y pide la suspensión cuando procede. Entrega el escrito en Word. Úsala con «recurso
  de reposición extranjería», «me han denegado el arraigo», «recurso de alzada», «me han pedido
  documentación», «alegaciones a la extinción». Para demandar o suspender judicialmente una expulsión
  usa recurso-contencioso-extranjeria; en un expediente de expulsión,
  expulsion-procedimiento-sancionador.
---

# Recursos y escritos en vía administrativa de extranjería

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Clase de recurso, órgano y plazo** → `buscar_articulo` (`ley="LPAC"`, artículos `"30"`, `"40"`, `"43"`, `"112"`, `"115"` y `"121"` a `"124"`; `ley="BOE-A-2024-24099"`, `articulo="202"` para extinciones y `articulo="15"` para denegaciones de entrada; `ley="BOE-A-2013-10074"`, `articulo="76"` para la Unidad de Grandes Empresas).
- **Silencio y obligación de resolver** → `buscar_articulo` (`ley="LPAC"`, artículos `"21"`, `"24"` y `"25"`; `ley="BOE-A-2024-24099"`, el artículo del procedimiento de la vía, por ejemplo `"63"`, `"71"`, `"80"`, `"97"` o `"192"`).
- **Requerimientos y audiencia** → `buscar_articulo` (`ley="LPAC"`, artículos `"28"`, `"32"`, `"68"`, `"73"`, `"76"`, `"82"` y `"118"`; `ley="BOE-A-2024-24099"`, artículos `"130"`, `"97"` y `"202"`).
- **Motivos de impugnación** → `buscar_articulo` (`ley="LPAC"`, artículos `"35"`, `"47"`, `"48"` y `"119"`; `ley="LOEX"`, `articulo="20"`; y los artículos sustantivos de la autorización denegada, por ejemplo `ley="BOE-A-2024-24099"`, `"126"`, `"127"` y `"130"`).
- **Suspensión en vía administrativa** → `buscar_articulo` (`ley="LPAC"`, `articulo="117"`; `ley="LOEX"`, `articulo="21"`; `ley="BOE-A-2024-24099"`, artículos `"24"` (salidas obligatorias) y `"235"`).
- **Doctrina sobre el motivo del recurso** → `buscar_sentencias` (`base="AN"`, `jurisdiccion="CONTENCIOSO"`, `tipo_organo="TSJ"`, `provincia` del órgano) + `leer_sentencias` (`parrafos=3`, `terminos` del motivo); `base="TS"` para doctrina casacional.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Resolución de la oficina de extranjería (denegación, inadmisión, archivo por desistimiento, extinción) cuyo pie indica recurso potestativo de reposición.
- Resolución que no pone fin a la vía administrativa y cuyo pie indica alzada (por ejemplo, las de la Unidad de Grandes Empresas y Colectivos Estratégicos o las denegaciones de entrada).
- La Administración no ha resuelto en plazo y hay que recurrir la desestimación presunta o hacer valer un silencio estimatorio.
- Requerimiento de subsanación notificado: escrito que aporta y explica.
- Trámite de audiencia en una extinción o en otro procedimiento no sancionador.
- No la uses para alegaciones en expedientes de expulsión (`expulsion-procedimiento-sancionador`), para visados denegados por el consulado (`visados-denegacion`), para protección internacional (`proteccion-internacional-apatridia`), para nacionalidad (`nacionalidad-residencia` o `nacionalidad-otras-vias`) ni cuando conviene ir directo al juez o pedir una cautelar (`recurso-contencioso-extranjeria`).

## Datos que hay que reunir antes de redactar

Los datos con ★ son imprescindibles; si falta uno, pregúntalo antes de redactar.

1. ★ **Resolución o requerimiento íntegro**, con el pie de recursos, número de expediente y órgano que lo dicta.
2. ★ **Fecha de notificación** y forma (papel o electrónica, con la fecha de puesta a disposición y de acceso).
3. ★ **Solicitud original** con la relación de documentos presentados y su fecha de presentación.
4. ★ **Requerimientos anteriores** y lo que se contestó, con fechas.
5. ★ **Motivo de la denegación** tal como lo expresa la resolución.
6. Hechos o documentos nuevos y **por qué no se aportaron antes** (importa para el art. 118.1 LPAC).
7. Situación actual del cliente: si está en situación irregular o tiene un expediente de expulsión abierto, revisa primero el semáforo de `extranjeria-intake`.
8. Si se recurre un silencio: fecha de entrada de la solicitud en el registro del órgano competente.
9. Representación: poder notarial, apoderamiento apud acta o habilitación del art. 197.4 del Reglamento.

## Requisitos y comprobaciones

### 1. Reposición, alzada o contencioso directo

- Lee el pie de recursos. La notificación debe decir si el acto pone fin a la vía administrativa, qué recurso procede, ante qué órgano y en qué plazo (art. 40.2 LPAC); si le falta algo, lee el art. 40.3 LPAC sobre desde cuándo surte efecto.
- **Pone fin a la vía administrativa** → reposición potestativa ante el mismo órgano o contencioso directo (art. 123.1 LPAC). Mientras la reposición no se resuelva o se desestime por silencio no se puede ir al contencioso (art. 123.2).
- **No pone fin** → alzada ante el superior jerárquico, que puede presentarse ante el órgano que dictó el acto o ante el que debe resolver (art. 121 LPAC).
- Normas especiales que se leen siempre que encajen: extinción de autorizaciones (Reglamento 202.4: pone fin a la vía y admite reposición potestativa); autorizaciones de la Ley 14/2013 (`ley="BOE-A-2013-10074"`, art. 76: alzada conforme a los arts. 121 y 122 LPAC); denegación de entrada (Reglamento 15.2: no agota la vía administrativa).
- La regla general sobre qué resoluciones de extranjería ponen fin a la vía está en una disposición adicional del Reglamento que el conector no devuelve. Trabaja con el pie de recursos y con el artículo especial que hayas leído. Si el pie falta o es contradictorio y no hay artículo especial, aplica la puerta: detén la elección del recurso y explica al abogado qué precepto falta. No cites esa disposición en el escrito.
- El error en la calificación del recurso no impide tramitarlo si se deduce su carácter (art. 115.2 LPAC).

**Cuándo conviene reponer y cuándo ir al juez.** Repón cuando la denegación se deba a un error de hecho o a no haber valorado un documento que ya estaba en el expediente, cuando se recurra un silencio o cuando haya un hecho posterior que la oficina pueda valorar. Ve directo al contencioso cuando haga falta una medida cautelar (riesgo de expulsión o de pérdida del empleo), cuando la oficina haya fijado un criterio que no va a cambiar o cuando el recurso administrativo solo retrasaría el acceso al juez. La reposición no suspende por sí sola (art. 117.1 LPAC) y su plazo de resolución es el del art. 124.2 LPAC. Deja la decisión razonada en el resumen para el abogado.

### 2. Plazo

- Reposición: art. 124.1 LPAC (acto expreso, un mes; acto presunto, en cualquier momento desde que se produce). Alzada: art. 122.1 LPAC con la misma distinción.
- Cómputo: art. 30 LPAC (meses de fecha a fecha, apartado 4; último día inhábil, apartado 5). Notificación electrónica: art. 43 LPAC (acceso o rechazo por el transcurso de los días naturales que fija).
- Fuera de plazo: la resolución queda firme (art. 122.1) o solo cabe el contencioso (art. 124.1); si concurre alguna causa del art. 125 LPAC, valora el recurso extraordinario de revisión.
- Escribe en el escrito y en el resumen la fecha de notificación, el precepto y la fecha final calculada. Sin fecha de notificación no se da plazo.

### 3. Silencio

- Obligación de resolver y plazo supletorio: art. 21 LPAC. Regla general del silencio en procedimientos a instancia de parte: art. 24.1 LPAC, que admite excepciones fijadas por ley.
- En extranjería, busca primero el sentido del silencio en el artículo del procedimiento de la vía: algunos lo fijan (lee, según el caso, Reglamento 63.4, 71, 80.9, 97.6, 159, 160 o 192). Si el artículo lo fija, aplícalo y cítalo.
- Si el artículo no lo fija, el régimen depende de la disposición adicional primera de la LOEX y de disposiciones adicionales del Reglamento, que el conector no devuelve: aplica la puerta para ese punto, no afirmes el sentido del silencio y dile al abogado qué precepto falta.
- Desestimación presunta: permite recurrir (art. 24.2 LPAC) sin plazo de caducidad (arts. 122.1 y 124.1). Estimación presunta: es un acto que se puede hacer valer y acreditar con el certificado del art. 24.4; la resolución expresa posterior solo puede confirmarla (art. 24.3.a). Busca la doctrina de tu TSJ sobre la resolución denegatoria dictada tras un silencio estimatorio.
- Procedimientos de oficio: el vencimiento del plazo produce caducidad en los de gravamen (art. 25.1.b LPAC); en la extinción de autorizaciones, lee el plazo del art. 202.2 del Reglamento.

### 4. Contestación a un requerimiento de subsanación

- Plazo: el del artículo de la vía (por ejemplo, Reglamento 130.3 o 97.6) y, en su defecto, art. 68.1 LPAC; ampliación prudencial del art. 68.2 si aportar presenta dificultades especiales. La ampliación general es la del art. 32 LPAC: hasta la mitad del plazo; por el máximo cuando haya que cumplimentar un trámite en el extranjero (apartado 2, típico de los certificados de antecedentes de otro país), y siempre pedida y decidida antes del vencimiento (apartado 3).
- Contesta punto por punto: cada documento requerido, el que se aporta y su precepto. Si un documento no puede obtenerse a tiempo, aporta el justificante de haberlo pedido y pide la ampliación.
- Si se requiere un documento que la norma no exige o que ya obra en la Administración, apórtalo si puedes y deja constancia de la objeción con el art. 28 LPAC (apartado 2: documentos en poder de la Administración o elaborados por otra; apartado 3: documentos no exigidos por la norma). En el arraigo, antes de buscar un certificado de antecedentes de otro país, comprueba las excepciones del art. 130.2 del Reglamento (permanencia continuada de cinco años o acreditación en una solicitud anterior).
- Si ya se ha declarado el desistimiento: la actuación se admite si llegó antes o dentro del día en que se notificó la resolución que tuvo por transcurrido el plazo (art. 73.3 LPAC). Recurre el archivo con la prueba de la presentación en plazo o de la improcedencia del requerimiento.

### 5. Alegaciones en trámite de audiencia (procedimientos no sancionadores)

- Plazo del art. 82.2 LPAC salvo norma especial; en la extinción de autorizaciones, lee el art. 202.1 del Reglamento (audiencia no inferior a diez días), la caducidad del art. 202.2, el principio de proporcionalidad y las circunstancias del art. 202.3 y la causa concreta del art. 200.2.
- Aporta en este trámite todo lo que se quiera hacer valer después: en recurso no se tienen en cuenta los documentos que se pudieron aportar antes (art. 118.1 LPAC).

### 6. Motivos de fondo que se revisan

- Motivación insuficiente o estereotipada (art. 35 LPAC; LOEX 20.2).
- Requisito mal aplicado: compara la resolución con el texto vigente del artículo leído.
- Precepto anulado: si `buscar_articulo` devuelve junto al artículo en que se funda la denegación una nota «Téngase en cuenta que se declara la nulidad…» (el Supremo anuló en 2026 incisos o apartados de, entre otros, los arts. 94, 97, 98, 101, 159, 160, 166, 196 y 197), lo anulado no se aplica: alégalo citando la nota tal como la devuelve el conector. Cuando la nota habla del «inciso destacado», el texto que devuelve el conector no marca cuál es: no afirmes qué parte se anuló; razona si el caso cumple el precepto en cualquiera de sus lecturas o dile al abogado que lo compruebe en la sentencia.
- Informe policial o antecedentes valorados de forma automática: lee Reglamento 130.2 (último párrafo), 63.3 o 98.1 según la vía; calcula la cancelación de antecedentes con el art. 136 CP.
- Prueba aportada y no valorada; requerimiento improcedente; reglamento aplicado que no correspondía (lee con `leer_boe`, `identificador="BOE-A-2024-24099"`, la disposición transitoria segunda del Real Decreto si la solicitud es anterior al 20/05/2025).
- Nulidad (art. 47 LPAC) o anulabilidad (art. 48); retroacción si hay vicio de forma (art. 119.2); prohibición de agravar la situación del recurrente (art. 119.3).

### 7. Suspensión

- La interposición no suspende salvo disposición en contrario; el órgano puede suspender con ponderación si hay perjuicio de imposible o difícil reparación o causa de nulidad de pleno derecho, y la suspensión se entiende acordada si no se resuelve en el plazo del art. 117.3 LPAC. Pídela en otrosí cuando la ejecución cause un perjuicio concreto (salida obligatoria, pérdida del empleo).
- Régimen general de ejecutividad en extranjería: LOEX 21.2. En la expulsión preferente la suspensión administrativa no procede (Reglamento 235.3): esa urgencia se lleva al juez con `recurso-contencioso-extranjeria`.
- Denegación con advertencia de salida obligatoria: lee el art. 24 del Reglamento (plazo de salida fijado en la resolución o, en su defecto, quince días desde la notificación; al vencer, régimen de la estancia irregular). La suspensión presunta del art. 117.3 LPAC llega al mes de pedirla, normalmente después de vencer el plazo de salida: presenta el recurso cuanto antes, explica al abogado ese intervalo sin protección y qué hacer si se incoa una expulsión, y valora ir directo al contencioso con cautelar si el riesgo es inmediato. En el arraigo sociolaboral, la denegación pone fin además a la habilitación provisional para trabajar (Reglamento 130.5).

## Estrategia y jurisprudencia

- Un fundamento por motivo, cada uno con su forma: premisa normativa (texto leído), doctrina (párrafo literal), hecho del cliente con su documento y conclusión.
- Consultas de partida (`base="AN"`, `jurisdiccion="CONTENCIOSO"`, `tipo_organo="TSJ"`, provincia del órgano; si no hay resultados útiles, sin provincia):
  - `consulta="recurso de reposición extranjería documentos nuevos aportados en vía de recurso"`.
  - `consulta="requerimiento subsanación extranjería desistimiento archivo documentación aportada fuera de plazo"`.
  - `consulta="silencio administrativo positivo renovación autorización residencia resolución expresa posterior"`.
  - `consulta="motivación denegación autorización residencia informe policial desfavorable valoración"`.
  - `consulta="extinción autorización residencia proporcionalidad audiencia caducidad"`.
  - Antecedentes: `consulta="antecedentes policiales antecedentes penales cancelados denegación autorización residencia"` con `base="TS"`.
- Comprueba qué reglamento aplica cada resolución antes de citarla: muchas de 2025 y 2026 resuelven solicitudes del reglamento anterior.
- Lee solo lo que vas a citar (`leer_sentencias`, `parrafos=3`). Cita doctrina, nunca el relato de hechos ni datos personales de aquel pleito.

### Errores que hay que evitar

- Interponer reposición y demanda a la vez: la demanda espera a que la reposición se resuelva o se desestime por silencio (art. 123.2 LPAC).
- Contar el plazo desde la fecha de la resolución y no desde su notificación.
- Aportar en reposición documentos que se pudieron presentar antes sin explicar por qué no se hizo (art. 118.1 LPAC).
- Afirmar un silencio positivo o negativo sin un artículo leído que lo fije.
- Pedir en vía administrativa la suspensión de una expulsión preferente (Reglamento 235.3) en lugar de acudir al juez.
- Dejar vencer un requerimiento esperando un documento: aporta el justificante y pide la ampliación antes del vencimiento.
- Citar la disposición adicional del Reglamento sobre recursos, o la primera de la LOEX, sin haberla obtenido del conector.
- Fundar el recurso en sentencias que aplican el reglamento anterior sin advertirlo.

## Documento que se entrega

Escrito en Word según `references/formato-y-organos.md`. Nombres: `recurso-reposicion-<apellido-cliente>-<AAAAMMDD>.docx`, `recurso-alzada-…`, `subsanacion-…` o `alegaciones-…`.

Cita las normas en el documento como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca: «artículo N del Real Decreto 1155/2024» (nunca «del Reglamento de extranjería» ni «del Reglamento aprobado por…»), «artículo N de la Ley Orgánica 4/2000» y «Ley 14/2013, de 27 de septiembre». En esta skill, «Reglamento» es solo una abreviatura de trabajo del Real Decreto 1155/2024. Pon la letra o el ordinal delante del artículo y la norma justo detrás del número: «la letra b) del artículo 21.3 de la Ley 39/2015», «el ordinal 1.º de la letra b) del artículo 80.2 del Real Decreto 1155/2024». Con «artículo 21.3.b de la Ley 39/2015» o «artículo 197.4, letra a), del Real Decreto…», `verificar_escrito` no identifica la norma o atribuye el artículo a la última que se mencionó antes. `verificar_escrito` tampoco reconoce los artículos de las directivas de la UE: los da por no identificados o, dentro de un escrito, los atribuye a la última norma española citada y les pone «✔ existe». Compruébalos siempre con `buscar_articulo` (`ley="Directiva 2003/86/CE"`, por ejemplo) y no te fíes de lo que diga el verificador sobre ellos.

**Recurso de reposición o de alzada**

1. Encabezamiento en mayúsculas: reposición, al órgano que dictó el acto (por ejemplo, «A LA OFICINA DE EXTRANJERÍA DE LA SUBDELEGACIÓN DEL GOBIERNO EN [PROVINCIA]»); alzada, al órgano superior que indique el pie de recursos, con presentación ante el que dictó el acto o ante el que resuelve.
2. Comparecencia: datos del interesado con marcadores y representación acreditada (art. 5 LPAC; Reglamento 197.4).
3. Acto recurrido: órgano, fecha, número de expediente y fecha de notificación.
4. HECHOS numerados en ordinales, cada uno con su documento.
5. FUNDAMENTOS DE DERECHO: primero los procedimentales (acto recurrible, clase de recurso y órgano, plazo con fechas, legitimación, representación); después uno por cada motivo de fondo.
6. SOLICITA: que se tenga por interpuesto, se estime, se anule la resolución y se conceda lo pedido o, subsidiariamente, se retrotraiga el procedimiento.
7. OTROSÍ: suspensión (art. 117 LPAC) si procede; documentos nuevos con la razón de no haberlos aportado antes.
8. Lugar, fecha y firma; relación numerada de documentos.

**Contestación a requerimiento**: encabezamiento a la oficina que requirió, con el número de expediente; «EXPONE» la fecha del requerimiento y que se contesta en plazo; tabla punto requerido · documento aportado · precepto; en su caso, justificantes y petición de ampliación; «SOLICITA» que se tengan por aportados y continúe la tramitación.

**Alegaciones en audiencia**: encabezamiento al órgano instructor; alegaciones numeradas; «SOLICITA» el archivo o la resolución favorable; documentos.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió antes de empezar.
- [ ] Clase de recurso y órgano justificados con el pie de recursos y los artículos leídos; si dependían de una disposición no disponible, la tarea se detuvo en ese punto.
- [ ] Plazo con fecha de notificación, precepto (arts. 122 o 124 y 30 LPAC) y fecha final.
- [ ] Sentido del silencio afirmado solo si lo fija un artículo leído.
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación; cada ECLI se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`, y aplica el reglamento que corresponde.
- [ ] Marcadores en los datos no facilitados; ningún dato del cliente en las consultas.
- [ ] `verificar_escrito` pasado sobre el escrito completo.
- [ ] Resumen en el chat según el apartado 7 del formato: escrito y órgano, plazo y fecha límite con su precepto, documentos que faltan y riesgos (incluida la conveniencia de ir al contencioso), tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene) y próximo paso.
