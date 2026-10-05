---
name: contrato-obra
description: >-
  Redacta el contrato de ejecución de obra o de reforma (obra nueva, rehabilitación, reforma de
  vivienda, local o nave, instalaciones) entre el dueño o promotor y el contratista, o entre
  contratista y subcontratista, con su nota para el abogado en Word. Úsala cuando el abogado diga
  «contrato de obra», «contrato con la constructora», «reforma del local», «precio cerrado»,
  «certificaciones», «retención en garantía», «penalización por retraso», «acta de recepción» o
  «subcontrata». Ajusta precio alzado o por unidades, modificaciones, plazos, certificaciones,
  retenciones, recepción, responsabilidad de la LOE, garantías y subcontratación según defienda al
  dueño o al contratista. Para servicios sin resultado material, usa prestacion-servicios; para
  comprar una vivienda en construcción, compraventa-inmueble; para reclamar defectos ya aparecidos,
  vicios-ocultos-saneamiento.
---

# Contrato de obra y reforma

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Contrato de obra en el Código Civil** → `buscar_articulo` (`ley="CC"`, artículos `"1544"` y `"1588"` a `"1600"`, uno por uno; y `"1101"` a `"1107"`, `"1124"`, `"1152"`, `"1154"` y `"1256"`).
- **Edificación: ámbito, licencias, recepción, responsabilidad, prescripción y garantías** → `buscar_articulo` (`ley="BOE-A-1999-21567"`, artículos `"2"`, `"3"`, `"5"`, `"6"`, `"9"`, `"11"`, `"17"`, `"18"` y `"19"`).
- **Subcontratación en construcción y responsabilidad por contratas** → `buscar_articulo` (`ley="BOE-A-2006-18205"`, artículos `"4"`, `"5"`, `"7"` y `"8"`) y (`ley="ET"`, `articulo="42"`).
- **Pago de certificaciones, intereses y pactos abusivos; dueño consumidor** → `buscar_articulo` (`ley="BOE-A-2004-21830"`, artículos `"3"`, `"4"`, `"5"`, `"7"`, `"8"` y `"9"`) y, si el dueño es consumidor, (`ley="TRLGDCU"`, artículos `"3"`, `"82"`, `"83"`, `"85"`, `"86"`, `"87"`, `"88"` y `"90"`; si el contrato se celebra fuera del establecimiento del contratista o a distancia, además `"92"`, `"93"`, `"97"`, `"99"`, `"102"`, `"103"`, `"104"`, `"105"`, `"106"` y `"108"`; `ley="LEC"`, artículos `"52"` y `"54"`).
- **Doctrina sobre precio, modificaciones, penalizaciones, desistimiento, retenciones, recepción y acción directa** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; `base="AN"` + `tipo_organo="AP"` si no hay doctrina del Supremo o el asunto se litigará en esa plaza) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (existencia, estado, administradores, concurso); **inmueble de la obra** → `consultar_catastro` (referencia catastral, uso, superficie, año; no da titular: pide al abogado nota simple o título del dueño); usos y licencias municipales, si el municipio está cubierto → `buscar_ordenanzas` / `leer_ordenanza`.
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral o catastral...). Cita la LOE como «artículo N de la Ley 38/1999, de 5 de noviembre, de Ordenación de la Edificación» (con «LOE» a secas el conector encuentra la Ley Orgánica de Educación), la subcontratación como «artículo N de la Ley 32/2006, de 18 de octubre, reguladora de la subcontratación en el Sector de la Construcción» y la morosidad como «artículo N de la Ley 3/2004, de 29 de diciembre».

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Contrato principal entre dueño o promotor y contratista: obra nueva, ampliación, rehabilitación, reforma de vivienda, local, oficina o nave, instalaciones.
- Subcontrato entre contratista y subcontratista (con la Ley 32/2006 si es obra de construcción).
- Presupuesto aceptado que hay que convertir en contrato, o condiciones generales de un constructor.

| Situación | Skill que procede |
|---|---|
| Servicio sin resultado material (mantenimiento, consultoría, proyecto o dirección facultativa del arquitecto) | `prestacion-servicios` |
| Fabricación a medida de un bien mueble que se entrega, sin instalación relevante | `compraventa-mercantil` (valora con el abogado si prevalece la obra) |
| Compra de vivienda en construcción o sobre plano | `compraventa-inmueble` |
| El arrendatario de un local hace obras de adecuación | `arrendamiento-local-negocio` (y esta skill para el contrato con el constructor) |
| Revisar o contestar el borrador del constructor o del promotor | `revision-contrato-semaforo` o `negociacion-contrapropuesta` |
| Defectos ya aparecidos, certificaciones impagadas, abandono de la obra | `vicios-ocultos-saneamiento`, `reclamacion-deuda-monitorio`, `requerimiento-cumplimiento` o `resolucion-por-incumplimiento` |
| Cambios en un contrato de obra ya firmado | `modificacion-novacion-cesion` |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ A quién defiende el abogado: dueño o promotor, contratista o subcontratista.
2. ★ Partes: datos de identificación y poder; si el dueño es una persona física que reforma su vivienda (consumidor, art. 3 TRLGDCU) o actúa en su actividad empresarial. Si es consumidor, pregunta también **dónde se negocia y se firma** (en el establecimiento del contratista, en la vivienda del dueño o por medios a distancia) y si la visita la pidió el dueño.
3. ★ Inmueble: dirección y municipio o referencia catastral (comprueba con `consultar_catastro`), título del dueño (propietario, arrendatario con autorización del arrendador, comunidad) y si es edificio catalogado o protegido.
4. ★ Obra: descripción, proyecto (y si la obra lo exige, art. 2.2 LOE), memoria de calidades, planos, mediciones y presupuesto; dirección facultativa y coordinación de seguridad y salud; quién aporta los materiales.
5. ★ Licencia, declaración responsable o comunicación previa: quién la tramita y paga, y si la obra puede empezar antes de obtenerla.
6. ★ Sistema de precio: alzado o cerrado, por unidades de obra (precio unitario por medición real), por administración (coste más porcentaje) o mixto; IVA; revisión de precios.
7. ★ Plazos: fecha de inicio o acta de replanteo, hitos, fecha de terminación y causas que amplían el plazo.
8. ★ Pagos: anticipo (y aval que lo garantiza), certificaciones (periodicidad, quién las aprueba, plazo de pago), retención en garantía (porcentaje, forma de sustitución por aval, fecha de devolución) y liquidación final.
9. Penalizaciones por retraso y su tope; bonificaciones por adelanto.
10. Seguros y garantías: todo riesgo construcción, responsabilidad civil, y las garantías del art. 19 LOE si la obra está en su ámbito.
11. Subcontratación: libre, limitada o sujeta a aprobación; subcontratistas previstos.
12. Recepción: provisional y definitiva, plazo de garantía contractual, documentación final de la obra.
13. Si el contrato puede regirse por un Derecho civil propio: pregunta y, si aplica, busca la norma con `buscar_boe`; si no aparece, aplica la puerta.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota su línea de vigencia.

**Código Civil (arts. 1588 a 1600).**

- El contratista puede poner solo su trabajo o también el material (art. 1588); si pone el material, soporta la pérdida de la obra destruida antes de la entrega salvo mora del dueño en recibirla (art. 1589); si solo pone su trabajo, no cobra en ese caso salvo mora o mala calidad de los materiales advertida al dueño (art. 1590). Pacta quién asegura la obra y cuándo pasa el riesgo.
- Obra por piezas o por medida: el contratista puede exigir recepción y pago por partes, y la parte pagada se presume aprobada y recibida (art. 1592). Si defiendes al dueño, declara que los pagos de certificaciones son a cuenta y no suponen aprobación de la obra.
- Precio alzado sobre plano convenido: no hay aumento de precio por subida de jornales o materiales; sí por cambios en el plano que aumenten la obra, si el propietario los autorizó (art. 1593). Si defiendes al dueño, exige orden escrita con precio aceptado antes de ejecutar; si defiendes al contratista, prevé el precio de las partidas nuevas (precios contradictorios) y la ampliación de plazo.
- Desistimiento del dueño aunque la obra haya empezado, indemnizando gastos, trabajo y utilidad (art. 1594); muerte o imposibilidad del contratista elegido por sus cualidades (art. 1595).
- El contratista responde del trabajo de sus empleados (art. 1596). Quienes ponen trabajo y materiales en una obra ajustada alzadamente tienen acción contra el dueño hasta lo que este adeude al contratista cuando se reclama (art. 1597): es la acción directa del subcontratista, que el contrato principal no puede suprimir frente a terceros.
- Obra a satisfacción del propietario: a falta de conformidad, juicio pericial (art. 1598). Precio a la entrega salvo pacto o costumbre (art. 1599). Retención de la obra en cosa mueble (art. 1600).
- Ruina por vicios de la construcción en diez años, y quince si la causa es la falta a las condiciones del contrato (art. 1591): es el régimen de las obras a las que no se aplica la LOE; busca doctrina antes de afirmar su alcance en una reforma menor.

**Ley 38/1999, de 5 de noviembre, de Ordenación de la Edificación.**

- Ámbito: edificios del art. 2.1; requieren proyecto las obras del art. 2.2 (obra nueva salvo construcciones de escasa entidad; intervenciones que alteren la configuración arquitectónica; intervenciones en edificios protegidos). Una reforma que no encaje en el art. 2.2 queda fuera de los plazos del art. 17: dilo en la nota.
- Licencias y autorizaciones preceptivas (art. 5); el promotor debe obtenerlas y suscribir el acta de recepción (art. 9.2.c); el constructor designa jefe de obra, formaliza subcontrataciones dentro de los límites del contrato y firma el acta (art. 11.2).
- Recepción (art. 6): acta firmada por promotor y constructor con su contenido mínimo (partes, fecha del certificado final, coste final, reservas y plazo para subsanarlas, garantías); rechazo motivado por escrito; salvo pacto, dentro de los treinta días siguientes a la terminación notificada, con recepción tácita si el promotor no formula reservas o rechazo; los plazos de responsabilidad y garantía corren desde la recepción.
- Responsabilidad frente a propietarios y terceros adquirentes desde la recepción sin reservas o la subsanación (art. 17.1): diez años por defectos estructurales, tres por los de habitabilidad del art. 3.1.c) y un año del constructor por defectos de terminación o acabado. Individualizada o solidaria (art. 17.2 y 17.3); el constructor responde directamente por sus subcontratistas y por los productos que adquiera o acepte (art. 17.6); sin perjuicio de las acciones contractuales (art. 17.1) y de las del comprador (art. 17.9). Prescripción de dos años desde que se producen los daños y de dos años para la repetición (art. 18).
- Garantías (art. 19): seguro de daños materiales o de caución a uno, tres y diez años con capitales mínimos; la de un año puede sustituirse por la retención por el promotor del 5 % del importe de la ejecución material (art. 19.1.a). Qué garantías son obligatorias depende de la disposición adicional segunda, que `buscar_articulo` no devuelve (y `leer_boe` da el texto original, no el consolidado): léela en internet en el texto consolidado del BOE (https://www.boe.es/buscar/act.php?id=BOE-A-1999-21567) y cítala con enlace y fecha de consulta; nunca afirmes su obligatoriedad de memoria ni con el texto original.

**Subcontratación en construcción (Ley 32/2006).** Requisitos de contratistas y subcontratistas, incluida la inscripción en el Registro de Empresas Acreditadas (art. 4); niveles máximos de subcontratación y prohibiciones para autónomos y para quien solo aporta mano de obra (art. 5); deber de vigilancia y responsabilidad solidaria por obligaciones laborales y de Seguridad Social si se incumplen los arts. 4.2 o 5 (art. 7); Libro de Subcontratación (art. 8). Si la obra corresponde a la propia actividad del comitente, el art. 42 ET añade responsabilidad solidaria por cotizaciones y salarios (no la hay cuando una persona contrata la construcción o reparación de su vivienda, art. 42.2).

**Pagos (Ley 3/2004, de 29 de diciembre).** Se aplica entre empresas y expresamente entre contratistas principales y sus proveedores y subcontratistas (art. 3.1): plazo máximo pactado de sesenta días naturales y aceptación no superior a treinta días (art. 4); intereses y costes de cobro (arts. 5, 7 y 8); es criterio de abusividad que el contratista principal imponga a sus subcontratistas condiciones de pago no justificadas por las que él mismo obtiene (art. 9.1). Si defiendes al subcontratista, analiza con ese artículo el pago condicionado al cobro del contratista y las retenciones desproporcionadas.

**Dueño consumidor.** Si el dueño reforma su vivienda fuera de su actividad, el contratista es empresario y rigen las normas de consumidores (las cláusulas abusivas son nulas y se tienen por no puestas, arts. 82 y 83 TRLGDCU). Son abusivas, entre otras, la subida del precio sin razones objetivas ni derecho a resolver, salvo adaptación a un índice legal con el modo de variación explícito (art. 85.10); la indemnización desproporcionadamente alta a cargo del consumidor, incluidas las penas punitivas por desistimiento o los intereses de demora elevados (art. 85.6); las fechas de entrega meramente indicativas (art. 85.8); la exclusión o limitación de la responsabilidad del empresario o de los derechos del consumidor por cumplimiento defectuoso (art. 86.1 y 86.2); la retención de cantidades por renuncia sin reciprocidad y la pérdida de anticipos o el cobro de servicios no prestados (art. 87.2 y 87.6), y la sumisión a un fuero distinto del domicilio del consumidor o del lugar del inmueble (art. 90.2; y art. 54.2 LEC). **Si el contratista pide alguna de esas cláusulas, no la redactes**: la nota abre con una tabla «Lo que se pidió | Lo que dice la ley | Cómo queda» con cada artículo leído, y el contrato recoge la alternativa lícita (precio cerrado, pagos por hitos de obra ejecutada, liquidación del desistimiento conforme al art. 1594 CC con el beneficio industrial del presupuesto, interés legal del art. 1108 CC). Si el texto se usará con más clientes, es un modelo de condiciones generales: aplica además `condiciones-generales-consumidores`.

**Contrato con consumidor celebrado fuera del establecimiento o a distancia.** Si el contrato se negocia o se firma en la vivienda del dueño o en otro lugar distinto del establecimiento del contratista, o a distancia, se aplica el régimen de los arts. 92 y siguientes TRLGDCU (el art. 92.4 presume que los celebrados fuera del establecimiento están sometidos a él). Solo quedan fuera la construcción de edificios nuevos y la «transformación sustancial de edificios existentes» (art. 93.f): la reforma de una vivienda no suele serlo; si dudas, aplícalo. Consecuencias que el contrato y la nota deben recoger:

- Información precontractual del art. 97.1, incluidas las condiciones, el plazo y el procedimiento del desistimiento y el modelo de formulario (art. 97.1, letra j), y copia del contrato firmado en soporte duradero (art. 99).
- Derecho de desistimiento de catorce días naturales desde la celebración del contrato de servicios, o treinta si el contrato nace de una visita no solicitada por el consumidor (arts. 102 y 104), sin penalización ni renuncia válida (art. 102.2). Si no se informa, el plazo se alarga doce meses (art. 105).
- Si el dueño quiere que la obra empiece dentro de ese plazo, necesita una solicitud expresa y, si luego desiste, paga solo la parte proporcional ejecutada (arts. 99 y 108); si la obra se termina con su consentimiento expreso y su reconocimiento de que perderá el derecho, este se extingue (art. 103.a). Si no, fija el inicio después del plazo.
- Anexo con el documento de información y el formulario de desistimiento; el desistimiento se ejerce por el formulario o por cualquier declaración inequívoca (art. 106). Los modelos oficiales están en el anexo I del texto refundido, letra A (documento de información sobre el desistimiento) y letra B (formulario); el art. 106 aún los llama «anexo B». El conector no devuelve los anexos (`leer_boe` corta la ley): cópialos de internet, del texto consolidado del BOE (https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555), y cítalos con enlace y fecha de consulta.

**Tributación y costes públicos.** Avisa de que el abogado debe comprobar el IVA de la obra y quién asume las tasas e impuestos municipales de la licencia; no des tipos ni importes.

## Cláusulas clave y jurisprudencia

Consultas con `jurisdiccion="CIVIL"` y `base="TS"` salvo indicación; lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar.

| Cláusula | Si defiendes al dueño o promotor | Si defiendes al contratista | Qué buscar |
|---|---|---|---|
| Sistema de precio | Precio alzado cerrado sobre proyecto y mediciones; riesgo de errores de medición para el contratista | Precio por unidades con medición real, o alzado solo sobre lo definido y exclusiones listadas | `consulta="contrato de obra precio alzado artículo 1593 obras adicionales autorización del propietario"`; `consulta="contrato de obra por unidades de obra medición precio unitario exceso de mediciones"` |
| Modificaciones y obras adicionales | Solo por orden escrita del dueño con precio y plazo aceptados; lo no ordenado no se paga | Toda orden de la dirección facultativa obliga a pagar; precios contradictorios por baremo pactado; ampliación de plazo automática | `consulta="contrato de obra modificaciones obras no previstas orden escrita precio contradictorio"`, `base="AN"`, `tipo_organo="AP"` |
| Plazo y penalizaciones | Pena por día o semana acumulable a los daños, descontable de certificaciones; resolución tras un umbral | Tope global de la pena, pena sustitutiva de los daños, prórroga por causas no imputables (lluvias, licencias, cambios) | `consulta="penalización por retraso contrato de obra cláusula penal moderación"` |
| Certificaciones y pago | Certificaciones a cuenta, aprobadas por la dirección facultativa, sin aprobación de la obra; liquidación final | Pago en el plazo de la Ley 3/2004 desde la certificación; aprobación tácita si no hay reparos en plazo; suspensión de obra por impago | `consulta="certificaciones de obra carácter provisional pagos a cuenta liquidación final"`, `base="AN"`, `tipo_organo="AP"` |
| Retención en garantía y avales | Retención porcentual de cada certificación hasta la recepción definitiva; aval de fiel cumplimiento a primer requerimiento | Retención sustituible por aval; devolución en fecha cierta; intereses si se retrasa | `consulta="retención en garantía contrato de obra devolución del cinco por ciento"`, `base="AN"`, `tipo_organo="AP"` |
| Recepción | Recepción solo con certificado final, documentación y pruebas; reservas con plazo de subsanación | Recepción tácita del art. 6.4 LOE y recepción por fases; ocupación equivale a recepción | `consulta="recepción de la obra sin reservas defectos aparentes contratista"` |
| Desistimiento del dueño | Indemnización limitada a obra ejecutada, acopios y un porcentaje tasado del beneficio | Indemnización íntegra del art. 1594, incluido el beneficio de la obra pendiente; con dueño consumidor, nunca una pena alzada (art. 85.6 TRLGDCU): el beneficio industrial desglosado en el presupuesto | `consulta="desistimiento unilateral del comitente artículo 1594 indemnización beneficio industrial"`; con consumidor, `consulta="cláusula penal moderación artículo 1154 incumplimiento previsto por las partes"` (la doctrina del pleno sobre penas punitivas exceptúa las condiciones generales con consumidores) |
| Subcontratación y acción directa | Autorización previa, documentación de la Ley 32/2006 y del art. 42 ET, justificante de pago a subcontratistas antes de pagar cada certificación, facultad de pago directo | Libertad de subcontratar partidas; sin pago directo salvo acuerdo | `consulta="acción directa artículo 1597 subcontratista dueño de la obra cantidad adeudada"`, `anios=15`; subcontratista: `consulta="pago al subcontratista condicionado al cobro del contratista principal"`, `base="AN"`, `tipo_organo="AP"` |
| Responsabilidad por defectos | Garantía contractual adicional a los plazos legales; obligación de reparar en plazo o ejecución a costa del contratista | Limitación a los plazos y supuestos legales; exclusión de daños por uso o falta de mantenimiento | Solo arts. 17 y 18 LOE; obra fuera de la LOE: `consulta="responsabilidad del contratista artículo 1591 ruina obra no sujeta a la Ley de Ordenación de la Edificación"` |

Reglas para la nota:

- Las penalizaciones, el desistimiento, las retenciones y la calificación del precio son cuestiones de validez o alcance discutidas en la jurisprudencia (apartado 8 del formato): cita en la nota el párrafo literal de la resolución leída, con órgano, fecha y ECLI; si tras dos reformulaciones no hay resolución aplicable, aplica la puerta.
- Para retenciones, modificaciones y pagos condicionados la doctrina suele ser de Audiencias Provinciales: preferible la de la plaza donde se litigaría, y dilo.
- Los plazos de responsabilidad de la LOE frente a propietarios y adquirentes no se reducen por contrato: la cláusula de responsabilidad del contrato regula la relación entre las partes y debe decirlo.

## Documentos que se entregan

Dos documentos Word maquetados según `references/formato-y-entrega-contratos.md`:

1. `contrato-obra-<parte-principal>-<AAAAMMDD>.docx` (o `contrato-subcontrata-obra-…` en un subcontrato).
2. `nota-obra-<parte-principal>-<AAAAMMDD>.docx`.

Estructura del contrato:

1. REUNIDOS e INTERVIENEN; EXPONEN: título del dueño sobre el inmueble (con referencia catastral), proyecto y dirección facultativa, licencia o su tramitación, capacidad y acreditación del contratista.
2. PRIMERA.- Objeto y documentos contractuales con su prelación: contrato, proyecto, memoria de calidades, mediciones y presupuesto, plan de obra.
3. SEGUNDA.- Precio, sistema (alzado, por unidades o administración), IVA y revisión.
4. TERCERA.- Modificaciones y obras adicionales: orden escrita, precios contradictorios, efectos sobre el plazo.
5. CUARTA.- Plazos: inicio, hitos, terminación, prórrogas.
6. QUINTA.- Certificaciones, pagos, anticipo y aval; intereses por remisión a la Ley 3/2004, de 29 de diciembre.
7. SEXTA.- Retenciones y garantías de cumplimiento.
8. SÉPTIMA.- Obligaciones del contratista: ejecución conforme a proyecto e instrucciones, jefe de obra, medios, seguridad y salud, residuos, limpieza.
9. OCTAVA.- Obligaciones del dueño: acceso, licencias (si le corresponden), pagos, aprobaciones en plazo.
10. NOVENA.- Subcontratación, Libro de Subcontratación y justificación de pagos a subcontratistas.
11. DÉCIMA.- Materiales, riesgo y seguros (todo riesgo construcción, responsabilidad civil, garantías del art. 19 LOE si proceden).
12. UNDÉCIMA.- Penalizaciones.
13. DUODÉCIMA.- Recepción (acta con el contenido del art. 6 LOE), plazo de garantía contractual y liquidación.
14. DECIMOTERCERA.- Responsabilidad por defectos.
15. DECIMOCUARTA.- Suspensión, desistimiento del dueño y resolución por incumplimiento.
16. DECIMOQUINTA.- Cesión, notificaciones, negociación previa, ley aplicable y fuero.
17. Cierre, firmas y ANEXOS: proyecto o memoria, presupuesto y mediciones, plan de obra, modelo de certificación, modelo de acta de recepción, avales, pólizas.

**Reparto para la redacción rápida:** una sección por bloque de estipulaciones (`### [ESTIPULACION]`): comparecencia, expositivos, objeto y documentos contractuales / precio, modificaciones, plazos, certificaciones y pagos / retenciones y garantías, obligaciones de las partes y subcontratación / materiales, riesgo y seguros, penalizaciones, recepción y responsabilidad por defectos / suspensión, desistimiento y resolución, cesión, notificaciones, ley, fuero, firmas y anexos. La nota: apartado 11 del formato.

La nota sigue el apartado 3 del formato: si la obra está en el ámbito de la LOE (y consecuencias), sistema de precio elegido y riesgo, cláusulas críticas con su artículo y jurisprudencia literal, garantías obligatorias según la disposición adicional segunda consolidada (con su enlace), datos pendientes (licencia, nota simple, pólizas), fiscalidad a comprobar.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Detector pasado: es obra y no servicio, compraventa o arrendamiento; si el dueño es consumidor, aplicados los arts. 82 a 90 TRLGDCU, sin cláusulas abusivas aunque el cliente las pidiera (tabla en la nota).
- [ ] Dueño consumidor y contrato celebrado fuera del establecimiento o a distancia: información del desistimiento, formulario, plazo de catorce (o treinta) días y fecha de inicio de la obra coherente con él, o solicitud expresa de inicio anticipado.
- [ ] Inmueble identificado con `consultar_catastro` y título del dueño pedido al abogado (nota simple o autorización del arrendador).
- [ ] Leídos con `buscar_articulo` en esta conversación los arts. 1588 a 1600 CC que se usan, los de la LOE (`ley="BOE-A-1999-21567"`), la Ley 32/2006, el art. 42 ET y la Ley 3/2004 (título de cada respuesta comprobado).
- [ ] Ámbito LOE decidido (art. 2) y dicho en la nota; obligatoriedad de las garantías tomada de la disposición adicional segunda consolidada (internet, con enlace y fecha) y no de memoria.
- [ ] Lo que no dio Jurisprudenciator y se obtuvo en internet, citado con enlace y fecha de consulta desde fuente oficial y señalado en el resumen; ninguna sentencia citada sin `buscar_por_cita` y `leer_sentencias`.
- [ ] Sistema de precio, modificaciones y ampliaciones de plazo coherentes entre sí; pagos a cuenta sin aprobación implícita de la obra si se defiende al dueño.
- [ ] Plazo de pago de certificaciones no superior al máximo legal; retenciones y pena con tope y regla de devolución.
- [ ] Acta de recepción con el contenido del art. 6.2 LOE; plazos de responsabilidad computados desde la recepción.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); la LOE citada con número y fecha; cada «posible disonancia» contrastada con el apartado leído.
- [ ] Sociedades comprobadas con `buscar_empresa_mercantil`; firmantes con cargo o poder vigentes.
- [ ] Marcadores (`[REFERENCIA CATASTRAL]`, `[IMPORTE]`, `[FECHA DE INICIO]`…) en lugar de datos inventados; importes, porcentajes, plazos y anexos coherentes.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas, datos y documentos que faltan, tabla de jurisprudencia, plazos con su precepto (recepción, garantías, prescripción del art. 18 LOE, pago) y próximo paso.
