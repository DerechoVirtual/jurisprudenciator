---
name: denegacion-entrada-devolucion
description: >-
  Actuación urgente en frontera con escritos en Word: denegación de entrada en puesto fronterizo (arts.
  26.2 y 60 LOEX; art. 15 del Real Decreto 1155/2024; art. 14 del Código de fronteras Schengen) y
  devolución de quien pretende entrar irregularmente o contraviene una prohibición de entrada (art. 58.3
  LOEX; art. 23 del Real Decreto 1155/2024). Asistencia letrada y alegaciones de suspensión (asilo, trata,
  minoría de edad, embarazo o enfermedad), petición de entrada por razones humanitarias, solicitud de
  protección internacional, habeas corpus y recurso de alzada. Úsala con «denegación de entrada en el
  aeropuerto», «sala de inadmitidos», «interceptado en patera», «orden de devolución», «rechazo en
  frontera», «72 horas». Para expulsión usa expulsion-procedimiento-sancionador; para internamiento en
  CIE, internamiento-cie; para tramitar el asilo, proteccion-internacional-apatridia.
---

# Denegación de entrada y devolución

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Denegación de entrada, requisitos de entrada y regreso** → `buscar_articulo` (`ley="LOEX"`, artículos `"26"`, `"60"` y `"22"`); (`ley="BOE-A-2024-24099"`, artículos `"4"` y `"15"`, y el `"6"` a `"11"` que corresponda a la causa de denegación); (`ley="Reglamento (UE) 2016/399"`, artículos `"6"` y `"14"`).
- **Medios económicos de entrada (cuantía y forma de acreditarlos)** → el art. 9 del Reglamento remite a una orden ministerial: la vigente es la Orden PRE/1282/2007 (`buscar_boe` la localiza; léela con `leer_boe`, `identificador="BOE-A-2007-9608"`, porque se divide en apartados y `buscar_articulo` no la encuentra). Fija la cuantía en porcentajes del salario mínimo interprofesional, que el conector no devuelve: pide al abogado la cifra vigente.
- **Reexamen de la denegación y acceso al expediente** → `buscar_articulo` (`ley="LPAC"`, artículos `"109"` y `"53"`).
- **Devolución y sus suspensiones** → `buscar_articulo` (`ley="LOEX"`, `articulo="58"`) y (`ley="BOE-A-2024-24099"`, `articulo="23"`).
- **Protección internacional en frontera** → `buscar_articulo` (`ley="Ley 12/2009"`, artículos `"16"`, `"19"`, `"21"` y `"22"`); (`ley="Reglamento (UE) 2024/1348"`, artículos `"4"` y `"26"` (quién recibe la solicitud y cuándo se entiende formulada), `"27"` (registro en cinco días; su apartado 7 lo aplaza al final del triaje), `"10"` (derecho a permanecer), `"43"`, `"51"`, `"53"` y `"79"`); (`ley="Reglamento (UE) 2024/1356"`, artículos `"5"`, `"8"`, `"18"` y `"25"`).
- **Privación de libertad y habeas corpus** → `buscar_articulo` (`ley="CE"`, `articulo="17"`) y (`ley="LO 6/1984"`, artículos `"1"` a `"4"`).
- **Recursos y plazos** → `buscar_articulo` (`ley="LPAC"`, artículos `"40"`, `"112"`, `"121"`, `"122"`, `"123"` y `"124"`) y (`ley="LJCA"`, artículos `"8"`, `"46"` y `"135"`).
- **Doctrina** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"` para TSJ y juzgados, `base="TS"` para el Supremo; `base="TC"` para habeas corpus y libertad; fechas en formato `dd/mm/aaaa`) + `leer_sentencias` (`parrafos=3`). La búsqueda se hace siempre, porque tarda segundos; leer y citar puede omitirse en los escritos urgentes A y C (ver «Estrategia», punto 5).
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

Primero identifica la figura: cada una tiene órgano, garantías y recursos distintos.

| Figura | Cuándo | Base |
|---|---|---|
| Denegación de entrada | Llega a un puesto fronterizo habilitado (aeropuerto, puerto, frontera terrestre) y no cumple los requisitos de entrada | LOEX arts. 26.2 y 60; arts. 4 y 15; Código de fronteras Schengen art. 14 |
| Devolución por prohibición de entrada | Expulsado que vuelve mientras dura la prohibición | LOEX art. 58.3.a; art. 23.1.a |
| Devolución por entrada irregular | Pretende entrar irregularmente, incluidos los interceptados en la frontera o sus inmediaciones (patera, salto de valla, a nado) | LOEX art. 58.3.b; art. 23.1.b |
| Rechazo en frontera de Ceuta y Melilla | Detectado en la línea fronteriza intentando superar los elementos de contención | disposición adicional décima LOEX: ver «Huecos normativos» |
| Expulsión | Ya está en España en situación irregular o con condena | → `expulsion-procedimiento-sancionador` |

El Supremo ha distinguido en 2026 el rechazo en frontera de la devolución y ha declarado que a quien se intercepta en el mar intentando entrar a nado en Ceuta o Melilla se le aplica la devolución, no el rechazo: localiza esa doctrina (ver «Estrategia») antes de calificar el caso.

Deriva además: internamiento o CIE → `internamiento-cie`; tramitación de la solicitud de asilo (reexamen, entrevista, recurso) → `proteccion-internacional-apatridia`; indicios de trata → `victimas-trata`; posible menor no acompañado → `menores-extranjeros`; prohibición de entrada ya impuesta → `prohibicion-entrada-antecedentes`.

## El reloj de las 72 horas

- Denegación de entrada: el regreso se ejecuta de inmediato y en todo caso en setenta y dos horas; si no es posible, la autoridad se dirige al juez de instrucción para que fije el lugar de permanencia (LOEX art. 60.1; art. 15.3). En las instalaciones del puesto se permanece como máximo setenta y dos horas, con la libertad ambulatoria limitada a asegurar el regreso (art. 15.4).
- Devolución: si no se ejecuta en setenta y dos horas, se pide al juez el internamiento (LOEX art. 58.6; art. 23.4).
- Detención preventiva: máximo setenta y dos horas (CE art. 17.2).
- Anota **hora** de llegada, de la resolución y de cualquier traslado: sin ellas no puede valorarse el habeas corpus ni el plazo del juez.

## Datos que hay que reunir antes de redactar

En urgencia, redacta con marcadores y pide el resto después; nunca inventes una fecha u hora.

1. ★ Figura (tabla anterior), lugar exacto y horas: llegada o interceptación, resolución, ingreso en instalaciones o dependencias policiales.
2. ★ Resolución notificada: copia, causa de denegación o de devolución, pie de recursos (recurso, órgano y plazo), si se entregó en impreso normalizado y en qué idioma.
3. ★ Garantías: si se le informó de su derecho a asistencia letrada (de oficio si no tiene recursos) y a intérprete desde el control, y si se le prestaron (LOEX arts. 22.2 y 26.2; arts. 15.1 y 23.3).
4. ★ Nacionalidad, documento de viaje, visado, motivo del viaje, reservas, medios económicos, carta de invitación u otros documentos (art. 4 y siguientes).
5. ★ Si ha manifestado o quiere manifestar que pide protección internacional, y fecha y hora de esa manifestación, del registro y de la formalización.
6. ★ Vulnerabilidad: posible minoría de edad, embarazo, enfermedad, indicios de trata, víctima de violencia.
7. En devolución por la letra a): resolución de expulsión anterior, fecha, duración de la prohibición y Estado que la impuso.
8. Familiares o vínculos en España, y contacto consular (art. 15.6).

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**A. Denegación de entrada**

- Causas: incumplimiento de alguno de los requisitos del art. 4 (documento de viaje, visado, justificación del objeto, medios, requisitos sanitarios, prohibición de entrada, amenaza para el orden público) y de las condiciones del art. 6 del Código de fronteras Schengen. Lee el artículo de desarrollo de la causa invocada (arts. 6 a 11) y contrástalo con los documentos del cliente.
- Forma: resolución **motivada** con la causa concreta, notificada directamente, con información de recursos, plazo y órgano, del derecho a asistencia letrada y a intérprete desde el control, y de que el efecto es el regreso al punto de origen (LOEX art. 26.2; art. 15.1; Código de fronteras Schengen art. 14.2).
- Autorización excepcional de entrada: la Comisaría General de Extranjería y Fronteras puede autorizar la entrada a quien no cumple los requisitos por razones excepcionales humanitarias, de interés público o de compromisos de España (art. 4.3). Pídela por escrito cuando haya enfermedad, menores, familia en España u otra causa humanitaria acreditable.
- Recurso: la resolución **no agota la vía administrativa** y su interposición **no suspende** el regreso (art. 15.2; Código de fronteras Schengen art. 14.3). Procede recurso de alzada ante el superior jerárquico que indique el pie de recursos, en el plazo de un mes (LPAC arts. 121 y 122); desde el extranjero, a través del consulado (art. 15.2). Contra la resolución del recurso, contencioso (prepáralo con `recurso-contencioso-extranjeria`). Para litigar con asistencia gratuita hay que pedirla, y quien esté privado de libertad puede manifestar su voluntad de recurrir ante el Delegado o Subdelegado, el director del CIE o el responsable del puesto, que la hacen constar en acta (LOEX art. 22.3; art. 15.2).
- Para impedir el regreso inmediato, lo eficaz es la solicitud de protección internacional (apartado C) y, si la privación de libertad excede lo legal, el habeas corpus (apartado D).
- Si no hay petición de asilo ni otra causa de suspensión, **no pidas una «suspensión del regreso»** que la ley niega: pide el reexamen y la revocación de la denegación a la vista de los documentos (LPAC art. 109.1), la autorización excepcional del art. 4.3 y, si el problema son los medios, subsidiariamente la entrada con estancia reducida en proporción a los recursos acreditados (Orden PRE/1282/2007, apartado segundo.4); y que el regreso no se ejecute antes de resolver esas peticiones, dentro siempre de las setenta y dos horas. Con los medios, recuerda que valen el efectivo y las tarjetas de crédito con extracto (Orden, apartado segundo.2; Código de fronteras Schengen art. 6.4) y que la carta de invitación con alojamiento en casa de quien invita puede constituir prueba de medios (art. 6.4), aunque por sí sola no suple los demás requisitos (art. 8.2.c).

**B. Devolución**

- Sin expediente de expulsión, por resolución del Subdelegado del Gobierno o del Delegado en comunidades uniprovinciales (LOEX art. 58.3 y 58.5; art. 23.1). Los interceptados son conducidos a la comisaría del Cuerpo Nacional de Policía para su identificación (art. 23.2).
- Derecho a asistencia jurídica e intérprete, gratuitos si carece de recursos (art. 23.3; LOEX art. 22.2).
- **Suspensión obligatoria** de la ejecución (art. 23.6; LOEX art. 58.4): mujeres embarazadas o personas enfermas cuando la medida suponga riesgo; solicitud de protección internacional hasta que se resuelva o se inadmita (la admisión a trámite autoriza la entrada y la permanencia provisional); víctima de trata; indicios de que es menor no acompañado.
- Efectos: la devolución por la letra a) reinicia el cómputo de la prohibición de entrada; la de la letra b) lleva prohibición de entrada de hasta tres años (LOEX art. 58.7; art. 23.5). El art. 58.7 trae una nota del Tribunal Constitucional sobre un inciso declarado inconstitucional: léela en la respuesta del conector y no apliques ese inciso.
- Prescripción de la resolución: cinco años (letra a, contados tras la prohibición reiniciada) o dos años (letra b), de oficio (art. 23.7).
- Revocación si después procede una autorización por circunstancias excepcionales (art. 23.8).
- Recurso: el Reglamento regula los recursos en una disposición adicional que el conector no devuelve. Toma el recurso, el órgano y el plazo del pie de recursos de la resolución (LPAC art. 40.2) y compruébalos con la LPAC y la LJCA (reposición potestativa en un mes, LPAC art. 124; contencioso en dos meses, LJCA art. 46; cautelarísima, LJCA art. 135). Si el pie falta o es contradictorio, dilo al abogado: la notificación incompleta solo surte efecto desde que el interesado actúa o recurre (LPAC art. 40.3); no calcules un plazo que no puedas fundar.

**Motivos frecuentes de impugnación**

| Motivo | Dónde se apoya |
|---|---|
| Resolución genérica, sin la causa concreta ni valoración de los documentos aportados | LOEX art. 26.2; art. 15.1.a; Código de fronteras Schengen art. 14.2 |
| Sin asistencia letrada o sin intérprete desde el control o durante la devolución | LOEX art. 22.2; arts. 15.1 y 23.3 |
| Devolución ejecutada pese a una causa de suspensión alegada (asilo, trata, minoría, embarazo o enfermedad) | LOEX art. 58.4; art. 23.6; Ley 12/2009 art. 19.1 |
| Calificación errónea: ya estaba en España (procede, en su caso, expediente de expulsión) o no hubo intento de entrada irregular | LOEX arts. 57 y 58.3; art. 23.1 |
| Más de setenta y dos horas sin decisión judicial sobre el lugar de permanencia o el internamiento | LOEX arts. 58.6 y 60.1; arts. 15.3 y 23.4; LO 6/1984 art. 1 |

**C. Protección internacional en frontera o tras la interceptación**

- Solicitada la protección, no cabe devolución ni expulsión hasta que se resuelva o se inadmita (Ley 12/2009 art. 19.1; LOEX art. 58.4; art. 23.6.b). Derecho a entrevistarse con abogado en el puesto fronterizo (Ley 12/2009 art. 19.4); en el procedimiento en frontera, la asistencia jurídica es preceptiva (art. 16.2).
- Régimen según la fecha de **formalización** de la solicitud: antes del 12/06/2026, procedimiento en frontera de la Ley 12/2009 (arts. 21 y 22); desde esa fecha, Reglamento (UE) 2024/1348 (art. 79; procedimiento fronterizo de los arts. 43 a 54, con su duración máxima del art. 51 y las excepciones del art. 53, entre ellas los menores no acompañados) y triaje previo del Reglamento (UE) 2024/1356 (arts. 5, 8 y 18; aplicable desde la misma fecha según su art. 25). Comprueba con `buscar_boe` si España ha adaptado la Ley 12/2009; si un plazo concreto depende de una norma española que el conector no devuelve, dilo al abogado y actúa dentro del plazo más corto de los posibles.
- Desde el 12/06/2026, distingue **formular** (expresar en persona el deseo de protección ante una autoridad competente, que incluye como mínimo a la policía y la guardia de fronteras: Reglamento 2024/1348, arts. 26.1 y 4.2), **registrar** (sin demora y como máximo en cinco días; para quien está sometido a triaje, una vez concluido este: art. 27.1 y 27.7) y **formalizar**. El derecho a permanecer está en su art. 10.1, con las excepciones tasadas del art. 10.4. Si la persona ya expresó el deseo ante la policía, fecha y hora de esa manifestación son la primera prueba: pide el acta.
- Triaje (Reglamento 2024/1356): se aplica también a los desembarcados tras una operación de búsqueda y salvamento (art. 5.1.b), dura como máximo siete días desde el desembarco (art. 8.3) y termina derivando al registro a quien formuló la solicitud y al retorno solo a quien no lo hizo (art. 18.1 y 18.2). Una devolución acordada antes de concluir el triaje y sin valorar una petición ya expresada es un argumento del escrito.
- **Confidencialidad:** toda la información del procedimiento, incluido el hecho de haber pedido protección, es confidencial (Ley 12/2009 art. 16.4). Nunca pidas comunicación consular para quien pide asilo; pide lo contrario.
- Tu escrito se limita a dejar constancia de la voluntad de pedir protección y a exigir su registro y la suspensión; la solicitud, el reexamen y los recursos se preparan con `proteccion-internacional-apatridia`.

**D. Habeas corpus (LO 6/1984; CE art. 17.4)**

- Procede si la persona está detenida ilegalmente: sin supuesto legal o sin las formalidades exigidas, internada ilícitamente, retenida más allá del plazo legal sin libertad ni puesta a disposición judicial, o sin respeto de sus derechos de detenido (art. 1). Por ejemplo, más de setenta y dos horas en las instalaciones del puesto sin que el juez haya fijado el lugar de permanencia (LOEX art. 60.1; art. 15.3-4).
- Competencia: juez de instrucción del lugar donde se encuentre (art. 2). Legitimación, también del abogado defensor (art. 3). Escrito o comparecencia sin abogado ni procurador preceptivos, con identidad del solicitante y del privado de libertad, lugar y autoridad de custodia y motivo concreto (art. 4).
- Si ya está en un CIE con auto de internamiento, usa `internamiento-cie`.

**Huecos normativos.** El conector no devuelve la disposición adicional décima de la LOEX (rechazo en frontera en Ceuta y Melilla) ni la disposición adicional del Reglamento sobre recursos. Si el caso depende de su texto, detén la redacción y explica al abogado qué precepto falta; puedes informarle de la doctrina que lo interpreta, leída con `leer_sentencias`, pero no redactes el escrito sobre una disposición que no has podido leer.

## Estrategia y jurisprudencia

1. Orden de actuación: (1) garantías (abogado, intérprete, copia de la resolución); (2) causas de suspensión (asilo, trata, minoría, salud) por escrito y con hora; (3) autorización excepcional de entrada si hay causa humanitaria; (4) habeas corpus si el plazo se ha superado; (5) recurso.
2. En la denegación, ataca la motivación y la valoración individual de los documentos aportados en el control; en la devolución, la calificación de los hechos (¿intentaba entrar o ya estaba en España?) y la omisión de garantías.
3. Consultas (dos a cuatro palabras clave; reformula como máximo dos veces):
   - Denegación de entrada: `buscar_sentencias` (`consulta="denegación de entrada"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="20/05/2025"`) y `consulta="denegación entrada motivación documentos"`.
   - Devolución: `consulta="devolución entrada irregular asistencia letrada"`, `base="AN"`; y `consulta="devolución interceptados frontera"`, `base="TS"`.
   - Rechazo en frontera y Ceuta y Melilla: `consulta="rechazo en frontera Ceuta Melilla"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`, `anios=2`.
   - Centros de atención temporal tras la interceptación: `consulta="CATE devolución"`, `base="TS"`.
   - Habeas corpus en frontera: `consulta="habeas corpus extranjero puesto fronterizo"` y `consulta="habeas corpus aeropuerto asilo"`, `base="TC"`.
4. Antes de citar una sentencia, comprueba en su texto qué reglamento aplicó: muchas aplican el Real Decreto 557/2011; cítala solo donde el precepto vigente sea equivalente y dilo.
5. En los escritos urgentes A y C la jurisprudencia no es imprescindible, así que su falta no activa el punto 3 de la puerta: si el reloj no permite leerla o las consultas, con sus dos reformulaciones, no devuelven doctrina favorable aplicable, presenta con los preceptos leídos antes que con citas sin verificar y díselo al abogado en el resumen (qué se buscó y qué riesgo revela lo leído). En el recurso B sí es imprescindible.
6. Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y transcribe fundamentos, nunca hechos ni datos de aquel pleito.

## Documento que se entrega

Word maquetado según `references/formato-y-organos.md`. Si no hay tiempo para el Word, entrega el texto maquetado en el chat y avisa de que hay que pasarlo a Word.

- **A. Escrito urgente de alegaciones y solicitud de suspensión** (denegación de entrada o devolución), dirigido al responsable del puesto fronterizo o a la Subdelegación o Delegación del Gobierno que tramita la devolución. Nombre: `alegaciones-frontera-<apellido-cliente>-<AAAAMMDD>.docx`.
  Estructura: encabezamiento; comparecencia (letrado designado o de oficio, `[NOMBRE Y APELLIDOS]`, `[PASAPORTE]`, lugar de custodia); HECHOS con horas; FUNDAMENTOS: garantías (LOEX arts. 22.2 y 26.2; arts. 15.1 o 23.3), causa de suspensión que concurra (art. 23.6; LOEX art. 58.4; Ley 12/2009 art. 19.1), falta de motivación o error en la causa de denegación (art. 4 y el de la causa invocada; en medios, la Orden PRE/1282/2007), doctrina con párrafo literal y ECLI si la hay (punto 5 de «Estrategia»); SOLICITA: si concurre una causa de suspensión (asilo, trata, minoría, embarazo o enfermedad), suspensión del regreso o de la devolución y registro de la solicitud de protección internacional si se manifiesta; si no concurre, reexamen y revocación (LPAC art. 109.1), entrada con estancia reducida como subsidiaria (Orden, apartado segundo.4) y que el regreso no se ejecute antes de resolver, dentro de las setenta y dos horas; en ambos casos, entrevista reservada con el abogado, intérprete y copia íntegra del expediente (LPAC art. 53.1.a); OTROSÍ: autorización excepcional de entrada por razones humanitarias (art. 4.3), dirigida a la Comisaría General de Extranjería y Fronteras; comunicación consular (art. 15.6) **solo** en la denegación de entrada y si el cliente la quiere, nunca si pide protección internacional (pide entonces confidencialidad, Ley 12/2009 art. 16.4); en la devolución, constancia en acta de la voluntad de recurrir (art. 23.4); relación de documentos.
- **B. Recurso de alzada contra la denegación de entrada**, ante el órgano que indique el pie de recursos, en un mes (LPAC arts. 121 y 122). Nombre: `recurso-alzada-denegacion-entrada-<apellido-cliente>-<AAAAMMDD>.docx`. Estructura: encabezamiento; comparecencia y representación; resolución recurrida y fecha de notificación; HECHOS; FUNDAMENTOS (motivación del art. 15.1 y del art. 14.2 del Código de fronteras Schengen, cumplimiento real de los requisitos del art. 4, garantías, proporcionalidad); SOLICITA la anulación y el reconocimiento del derecho a no haber sido objeto de denegación; relación de documentos. Si el cliente ya está fuera de España, indica la presentación por el consulado (art. 15.2).
- **C. Solicitud de habeas corpus**, al juez de instrucción del lugar de custodia (LO 6/1984 arts. 2 y 4). Nombre: `habeas-corpus-<apellido-cliente>-<AAAAMMDD>.docx`. Estructura breve: solicitante y privado de libertad; lugar, autoridad de custodia y hora de inicio de la privación; motivo concreto con la letra del art. 1 que concurre; SUPLICO: incoación, comparecencia inmediata del privado de libertad y puesta en libertad o a disposición judicial.
- Recurso contra la devolución: prepáralo con `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria`, con la causa de suspensión y la cautelarísima (LJCA art. 135) si la ejecución es inminente.

Cita el Reglamento siempre como «artículo N del Real Decreto 1155/2024» y la LOEX como «artículo N de la Ley Orgánica 4/2000» (formato, apartado 4); nunca «del Reglamento de Extranjería» ni «del Reglamento aprobado por el Real Decreto…», que `verificar_escrito` no identifica. Con letra, escribe «la letra b) del artículo 23.6 del Real Decreto 1155/2024»: con «23.6.b)» el verificador atribuye el artículo a otra ley. `verificar_escrito` **no identifica los Reglamentos (UE)** (2016/399, 2024/1348, 2024/1356): marca sus artículos como «ley no identificada» o, si antes se ha citado una norma española (aunque sea en un fundamento anterior), se los atribuye a esa norma y a veces avisa de «disonancia». Citar la norma de la Unión antes que la española dentro de cada fundamento reduce esas atribuciones, pero no las elimina: compruébalos todos con `buscar_articulo` y explica en el resumen que esos avisos no son errores.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Figura identificada (denegación, devolución a o b, rechazo en frontera, expulsión) y derivaciones hechas.
- [ ] Leídos con `buscar_articulo` en esta conversación: LOEX 22, 26, 58 y 60; Reglamento 4, 15 y 23 (y el de la causa invocada); Código de fronteras Schengen 6 y 14; Orden PRE/1282/2007 (con `leer_boe`) si la causa son los medios; Ley 12/2009 (16, 19, 21 y 22) y Reglamentos (UE) 2024/1348 (4, 10, 26, 27, 43, 51, 53 y 79) y 2024/1356 (5, 8, 18 y 25) si hay asilo; LO 6/1984 si hay habeas corpus; LPAC y LJCA para el recurso.
- [ ] Horas anotadas y cómputo de las setenta y dos horas con su precepto; plazo del recurso con fecha de notificación, precepto y fecha final, o explicación de por qué no puede darse.
- [ ] Ningún contenido tomado de la disposición adicional décima de la LOEX ni de disposiciones adicionales del Reglamento.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el texto completo. Si marca un artículo del Reglamento como no localizado o lo atribuye a la LOEX, compruébalo con `buscar_articulo` (`ley="BOE-A-2024-24099"`) y reescribe la cita como «artículo N del Real Decreto 1155/2024».
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[PASAPORTE]`, `[NIE]`, `[NÚMERO DE EXPEDIENTE]`, horas) en lugar de datos inventados.
- [ ] Resumen para el abogado según el apartado 7 del formato: órgano; hora límite de las setenta y dos horas y plazo del recurso con su precepto; riesgos (regreso inmediato, recurso sin efecto suspensivo, vulnerabilidad detectada); tabla de jurisprudencia; próximo paso (asilo, habeas corpus, internamiento o recurso).
