---
name: arrendamiento-local-negocio
description: >-
  Redacta el arrendamiento para uso distinto de vivienda (local, oficina, nave, despacho y también el de
  temporada) y su nota para el abogado, en Word, defendiendo al arrendador o al arrendatario. Úsala
  cuando el abogado diga «alquiler de local», «arrendamiento de nave u oficina», «traspaso», «carencia
  por obras», «licencia de actividad», «indemnización del artículo 34», «repercutir el IBI» o
  «alquiler de temporada». Aplica la libertad de pactos del artículo 4.3 LAU con sus límites:
  duración, renta, obras y carencia, licencia, cesión y subarriendo, clientela, fianza y garantías,
  IBI y comunidad, adquisición preferente y desistimiento. Si es vivienda habitual, usa
  arrendamiento-vivienda; si se cede un negocio en marcha, valora antes el arrendamiento de industria.
---

# Arrendamiento de local y otros usos distintos de vivienda

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Calificación, régimen imperativo y libertad de pactos** → `buscar_articulo` (`ley="LAU"`, artículos `"1"`, `"3"`, `"4"`, `"36"` y `"37"`).
- **Régimen del título III y preceptos a los que remite** → `buscar_articulo` (`ley="LAU"`, artículos `"29"` a `"35"`, uno por uno, y `"19"`, `"21"`, `"22"`, `"23"`, `"25"`, `"26"` y `"27"`).
- **Código Civil supletorio: entrega apta, conservación, devolución, tácita reconducción, pena, resolución y fianza personal** → `buscar_articulo` (`ley="CC"`, artículos `"1554"`, `"1555"`, `"1561"`, `"1563"`, `"1566"`, `"1581"`, `"1152"`, `"1154"`, `"1124"`, `"1101"`, `"1255"`, `"1822"`, `"1831"` y `"1837"`).
- **IBI, comunidad, Registro y usos** → `buscar_articulo` (`ley="BOE-A-2004-4214"`, `articulo="63"`), (`ley="Ley 49/1960"`, `articulo="7"`) y (`ley="BOE-A-1946-2453"`, artículos `"2"` y `"34"`); usos y licencias municipales → `buscar_ordenanzas` + `leer_ordenanza` (municipio y `consulta` con la actividad o «licencia de actividad»).
- **Inmueble, certificado energético y temporada en plataformas** → `consultar_catastro` y `buscar_articulo` (`ley="Real Decreto Legislativo 1/2004"`, artículos `"38"` y `"40"`), (`ley="BOE-A-2021-9176"`, artículos `"3"` y `"17"`) y, si es temporada ofertada en plataformas, (`ley="BOE-A-2024-26931"`, artículos `"1"`, `"2"` y `"3"`).
- **Doctrina sobre indemnización del art. 34, renuncias, desistimiento y moderación, licencia, cesión e IBI** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; `base="AN"` + `tipo_organo="AP"` si no hay doctrina del Supremo o el asunto se litigará en esa plaza) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (existencia, administradores, apoderados, concurso); **IVA y retenciones de la renta** → `buscar_consultas_hacienda`; **depósito autonómico de la fianza** → `buscar_boe` (`consulta="depósito de fianzas"`).
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Cita la ley como «artículo N de la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos» y el IBI como «artículo 63 del Real Decreto Legislativo 2/2004, de 5 de marzo, por el que se aprueba el texto refundido de la Ley Reguladora de las Haciendas Locales»: así los reconoce `verificar_escrito`.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Arrendamiento de una edificación cuyo destino primordial no es la vivienda permanente del arrendatario (art. 3 LAU): local comercial o de hostelería, oficina, despacho profesional, nave, almacén, garaje independiente, local para actividad docente, asistencial o cultural.
- Arrendamiento de temporada de una vivienda (verano, curso académico, desplazamiento laboral o sanitario, obras en la vivienda propia), que la LAU trata como uso distinto (art. 3.2).

Pasa este detector antes de redactar. Si encaja otra figura, díselo al abogado con el artículo leído y deriva:

| Situación | Qué procede |
|---|---|
| El arrendatario va a vivir de forma permanente y no tiene otra vivienda, aunque se hable de «temporada» | `arrendamiento-vivienda` (art. 2 LAU): el título de temporada no evita el régimen imperativo |
| Vivienda amueblada comercializada en canales turísticos bajo normativa turística | Excluida de la LAU (art. 5.e): no la redactes. Rige la normativa turística autonómica (`buscar_boe`), las ordenanzas (`buscar_ordenanzas`) y la aprobación previa de la comunidad (arts. 7.3 y 17.12 LPH) |
| Se cede un negocio ya instalado y en funcionamiento (local más instalaciones, licencia y clientela como unidad) | Arrendamiento de industria, excluido de la LAU y regido por el Código Civil. Busca la doctrina (`consulta="arrendamiento de industria diferencia arrendamiento de local de negocio"`, `base="TS"`) y avisa al abogado antes de seguir con esta skill |
| Finca rústica con aprovechamiento agrario | Excluida (art. 5.c LAU): no la redactes con esta skill |
| Adenda de renta, prórroga, cesión o subrogación en un contrato vigente | `modificacion-novacion-cesion` |
| Contrato de la otra parte para revisar o contestar | `revision-contrato-semaforo` o `negociacion-contrapropuesta` |
| Circunstancias sobrevenidas que alteran la renta (cierre por autoridad, crisis) en un contrato vigente | `dictamen-interpretacion-contrato` |
| Impago, desistimiento ya producido o reclamación de rentas | `requerimiento-cumplimiento`, `resolucion-por-incumplimiento` o `reclamacion-deuda-monitorio` |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ A quién defiende el abogado: arrendador o arrendatario.
2. ★ Partes: si son sociedades, denominación y CIF para `buscar_empresa_mercantil`, y quién firma con qué cargo o poder; avalistas o garantes.
3. ★ Inmueble: dirección o referencia catastral (`consultar_catastro`), nota simple (titularidad, hipotecas, usufructo), superficie, estado, instalaciones, cédula o licencia de primera ocupación del local, estatutos de la comunidad si es un local en propiedad horizontal.
4. ★ Actividad concreta que se va a ejercer y si requiere licencia o declaración responsable; si la actividad es de venta al público (para el art. 34 LAU).
5. ★ Duración: plazo inicial, plazo de obligado cumplimiento, prórrogas y preavisos.
6. ★ Renta, IVA, forma y día de pago, actualización (índice y fecha), escalonados o bonificaciones, carencia.
7. ★ Obras: de adecuación que hará el arrendatario (proyecto, plazo, coste, quién las paga, propiedad al final) y obras del arrendador antes de la entrega.
8. Gastos: IBI, comunidad, tasas, seguros, suministros, con su importe o criterio de reparto.
9. Fianza (dos mensualidades) y garantías adicionales (aval a primer requerimiento, depósito, fianza personal, seguro de caución), importe y duración; comunidad autónoma para el depósito.
10. Si el arrendatario quiere poder ceder o subarrendar (traspasar el negocio), desistir anticipadamente o comprar el local.
11. Si el arrendamiento debe inscribirse en el Registro (duración larga, hipoteca previa).
12. En temporada: causa temporal concreta, fechas y si se ofertará en plataformas.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota su vigencia.

**Qué es imperativo y qué es pactable.**

- Rigen de forma imperativa los títulos I y IV de la LAU (art. 4.1): entre ellos, la fianza (art. 36) y la formalización (art. 37). Lo demás se rige por la voluntad de las partes, en su defecto por el título III y, supletoriamente, por el Código Civil (art. 4.3).
- Para excluir un precepto del título III hay que hacerlo de forma expresa y precepto por precepto (art. 4.4 LAU): una exclusión genérica («se excluye el título III») no basta. Nombra cada artículo que se excluye.
- Pueden pactarse mediación o arbitraje (art. 4.5 LAU; convenio por escrito, art. 9 de la Ley 60/2003) y una dirección electrónica para notificaciones fehacientes (art. 4.6 LAU).

**Régimen supletorio del título III.**

- Enajenación de la finca (art. 29 LAU): el adquirente se subroga salvo que sea tercero hipotecario (art. 34 de la Ley Hipotecaria). La Sala Primera ha precisado qué ocurre con el arrendamiento no inscrito cuando el local se ejecuta por una hipoteca anterior: búscalo (apartado siguiente) y lee qué dice también del arrendamiento inscrito **después** de esa hipoteca. Si defiendes al arrendatario que invierte en obras, exige la nota simple y recomienda inscribir el arrendamiento (art. 2 de la Ley Hipotecaria), pero no le digas que la inscripción le protege frente a una hipoteca anterior: frente a ella, valora pedir la posposición de la hipoteca o el consentimiento del acreedor, el compromiso del arrendador de pagar el préstamo y avisar de cualquier requerimiento, y el reembolso de la inversión no amortizada si el arrendamiento se extingue por la ejecución.
- Obras (art. 30 LAU): aplica los arts. 21, 22, 23 y 26 y, desde el inicio, la elevación de renta por mejoras del art. 19. Todo es pactable.
- Adquisición preferente (art. 31 LAU, que remite al 25): tanteo y retracto del arrendatario, renunciables por pacto.
- Cesión y subarriendo (art. 32 LAU): si se ejerce una actividad empresarial o profesional, el arrendatario puede ceder o subarrendar sin consentimiento, con elevación de renta del diez por ciento (subarriendo parcial) o del veinte (cesión o subarriendo total) y notificación fehaciente en un mes; la fusión, transformación o escisión de la sociedad arrendataria no es cesión, pero da derecho a la elevación.
- Muerte del arrendatario (art. 33 LAU): subrogación del heredero o legatario que continúe la actividad, notificada por escrito en dos meses.
- Indemnización al arrendatario (art. 34 LAU): al extinguirse por el transcurso del plazo, si en los últimos cinco años se ha ejercido una actividad comercial de venta al público y el arrendatario ofreció con cuatro meses de antelación renovar por cinco años más a renta de mercado. Su cuantía depende de si reinicia la actividad en el mismo municipio o si el arrendador o un tercero ejercen la misma o afín (hasta dieciocho mensualidades). La Sala Primera ha incluido la hostelería en la venta al público: busca la doctrina actual.
- Resolución de pleno derecho (art. 35 LAU): impago de renta o cantidades asimiladas, de la fianza, daños dolosos u obras no consentidas, actividades molestas o ilícitas, y cesión o subarriendo sin cumplir el art. 32.

**Código Civil y otras normas.**

- El arrendador debe entregar la cosa y mantenerla apta para el uso pactado y en goce pacífico (art. 1554 CC); el arrendatario paga, usa con diligencia y devuelve la finca como la recibió (arts. 1555, 1561 y 1563 CC).
- Si al vencer el arrendatario sigue quince días con aquiescencia del arrendador, hay tácita reconducción por los plazos de los arts. 1577 y 1581 CC, salvo requerimiento previo (art. 1566 CC). Regula el fin del plazo y el preaviso para evitarla o para prever prórrogas ordenadas.
- La LAU no da al arrendatario de local un derecho legal a desistir: solo existe si se pacta. Sin pacto, el desistimiento es un incumplimiento (arts. 1124 y 1101 CC) y la jurisprudencia modera la reclamación de las rentas pendientes según el daño real; con una cláusula penal pactada para ese desistimiento, no se modera (arts. 1152 y 1154 CC).
- IBI (art. 63 del Real Decreto Legislativo 2/2004): el sujeto pasivo es el propietario, que puede repercutir la carga conforme al Derecho común; sin pacto expreso no se traslada. El art. 20 LAU (gastos en vivienda) no rige para el local salvo remisión pactada.
- Estatutos de la comunidad (art. 7.2 LPH): el propietario y el ocupante no pueden ejercer actividades prohibidas por los estatutos ni molestas, insalubres, nocivas, peligrosas o ilícitas; pide los estatutos y comprueba que no prohíben la actividad. Si la actividad exige obras en elementos comunes (salida de humos, rótulos, climatización en fachada o cubierta), el contrato debe decir quién obtiene el acuerdo de la junta y en qué plazo, y qué ocurre si no se obtiene.
- Usos y licencias: consulta las ordenanzas del municipio con `buscar_ordenanzas` (consulta con la actividad y con «licencia de actividad») y lee el artículo aplicable con `leer_ordenanza`. Si el municipio no está cubierto, busca la ordenanza en internet en la sede electrónica del ayuntamiento o en el boletín oficial de la provincia y cítala con enlace y fecha de consulta. Si la compatibilidad depende del planeamiento urbanístico (no de una ordenanza), dilo y recomienda informe de compatibilidad urbanística o consulta previa al ayuntamiento; no afirmes que el uso está permitido.
- Certificado energético: el local que se alquila está dentro del ámbito salvo las exclusiones del art. 3.2 del Real Decreto 390/2021 (lee la nota «Téngase en cuenta» del art. 3: su redacción cambió en 2026); la etiqueta se anexa al contrato (art. 17.2).
- Referencia catastral en el contrato, aportada por el arrendador (arts. 38 y 40.1.d del Real Decreto Legislativo 1/2004); contrasta con `consultar_catastro` uso y superficie. País Vasco y Navarra, fuera del conector: consulta en internet la sede del catastro foral (o usa la certificación del abogado) y cita enlace y fecha.
- Fianza (art. 36 LAU): dos mensualidades en metálico, obligatoria; actualización según los apartados 2 y 3; garantías adicionales libres en uso distinto (el límite de dos mensualidades del art. 36.5 es solo para vivienda). Depósito según la comunidad autónoma: búscalo con `buscar_boe` y, si no aparece, en internet en el boletín o la sede electrónica de la comunidad, citando enlace y fecha; nunca des plazos ni importes de memoria.
- Tributación: avisa de que la renta de un local suele llevar IVA y, según el arrendatario, retención a cuenta; compruébalo con `buscar_consultas_hacienda` sin dar tipos que no leas en una norma. Si la herramienta no responde, busca la consulta en internet en la base oficial de la Dirección General de Tributos y cítala con enlace.
- Reclamación futura: antes de demandar habrá que intentar un medio adecuado de solución de controversias (art. 5 de la Ley Orgánica 1/2025; léelo). Deriva a `masc-propuesta-acuerdo` si el abogado quiere una cláusula de negociación previa.

**Arrendamiento de temporada.** Uso distinto de vivienda (art. 3.2 LAU): se rige por lo pactado y el título III. Deja en EXPONEN la causa temporal concreta y acreditable, fija la duración ligada a esa causa y la fecha de desalojo, y adviértele al arrendador en la nota de que, si el arrendatario vive allí de forma permanente, un juez puede aplicar el régimen de vivienda (busca `consulta="arrendamiento de temporada vivienda habitual calificación fraude de ley"`, `base="AN"`, `tipo_organo="AP"`, `anios=3`). Si se oferta en plataformas, lee los arts. 1, 2 y 3 del Real Decreto 1312/2024 con sus notas: el Tribunal Supremo anuló en 2026 parte del procedimiento de registro único; cita solo lo vigente.

## Cláusulas clave y jurisprudencia

Busca con `buscar_sentencias` (`jurisdiccion="CIVIL"`), lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y comprueba que es razonamiento de la Sala. La moderación de la cláusula penal y las renuncias a derechos del arrendatario exigen jurisprudencia (apartado 8 del formato): si tras dos reformulaciones no hay resolución aplicable, sigue el punto 3 de la puerta.

1. **Duración y plazo de obligado cumplimiento.** Pro arrendador: plazo largo con periodo de obligado cumplimiento y exclusión expresa de la tácita reconducción. Pro arrendatario: plazo inicial corto con prórrogas a su favor y preaviso breve.
2. **Desistimiento con indemnización.** `consulta="desistimiento anticipado arrendamiento local rentas pendientes moderación cláusula penal"` y `consulta="cláusula penal moderación incumplimiento previsto desistimiento arrendamiento uso distinto"` (`base="TS"`). Pro arrendador: cláusula penal que nombre el desistimiento anticipado como supuesto concreto y fije su importe (rentas pendientes del periodo de obligado cumplimiento o un número de mensualidades), excluyendo la moderación. Pro arrendatario: facultad de desistir tras un plazo, con preaviso y una indemnización cerrada y decreciente; sin ella, recoge en la nota que la reclamación de rentas es moderable.
3. **Indemnización del art. 34 y su renuncia.** `consulta="indemnización artículo 34 LAU requisitos actividad comercial venta al público"` (`base="TS"`) y `consulta="renuncia a la indemnización del artículo 34 LAU validez pacto artículo 4.3"` (`base="AN"`, `tipo_organo="AP"`). Pro arrendador: renuncia expresa nombrando el art. 34 (art. 4.4). Pro arrendatario: mantenerla, o pactar una cantidad fija o un derecho de renovación.
4. **Cesión, subarriendo y traspaso.** `consulta="cesión arrendamiento local de negocio artículo 32 LAU notificación elevación de renta"` (`base="TS"`). Pro arrendador: excluir expresamente el art. 32 y exigir consentimiento escrito; si se admite, elevación de renta, solvencia del cesionario, responsabilidad solidaria del cedente y tratamiento de los cambios de control de la sociedad arrendataria. Pro arrendatario: conservar la cesión con la venta del negocio, sin elevación o con la legal.
5. **Licencia de actividad.** `consulta="licencia de actividad arrendamiento local imputable arrendador resolución"` (`base="AN"`, `tipo_organo="AP"`, `anios=5`). Pro arrendatario: el arrendador declara que el local admite el uso pactado y hace a su costa las obras estructurales que exija la licencia; si la licencia se deniega por causas del local, resolución con devolución de fianza y de la renta pagada y reembolso de las obras. Pro arrendador: el arrendatario ha comprobado la viabilidad y tramita la licencia a su costa; la denegación no le exime de pagar, o solo le permite resolver con aviso dentro de un plazo y sin indemnización.
6. **Obras de adecuación y carencia.** `consulta="arrendamiento local carencia de renta obras de adecuación desistimiento"` (`base="AN"`, `tipo_organo="AP"`, `anios=5`). Fija proyecto, plazo, permisos, seguro, propiedad de las obras al final (con o sin reposición, art. 23.2 LAU) y qué pasa con la carencia si el arrendatario sale antes de amortizarla (devolución proporcional si defiendes al arrendador).
7. **IBI, comunidad y gastos.** `consulta="repercusión IBI arrendatario local pacto"` (`base="AN"`, `tipo_organo="AP"`, `anios=5`). Pro arrendador: repercusión expresa del IBI, tasas y cuotas de comunidad (ordinarias; derramas, si las acepta el arrendatario), pagaderos con la renta. Pro arrendatario: gastos cerrados con importe anual y tope de incremento; derramas extraordinarias y obras estructurales a cargo del arrendador.
8. **Enajenación y ejecución hipotecaria.** `consulta="ejecución hipotecaria arrendamiento local no inscrito extinción"` (`base="TS"`). Pro arrendatario: inscripción del arrendamiento y deber del arrendador de informar de hipotecas; pro arrendador: nada que limite su facultad de vender, con renuncia del arrendatario a la adquisición preferente (arts. 31 y 25.8 LAU).
9. **Renta, actualización y cierre por autoridad.** Pacta índice expreso (el art. 18 LAU es del título II y no se aplica al local sin remisión), fecha y notificación. Si el cliente lo pide, cláusula de reducción o suspensión de la renta por cierre ordenado por la autoridad; para su interpretación en un contrato vigente, `dictamen-interpretacion-contrato`.
10. **Garantías.** Aval bancario a primer requerimiento con duración que cubra el contrato y unos meses más; fiador solidario con renuncia expresa a los beneficios de excusión y división (arts. 1831 y 1837 CC). Pro arrendatario: devolución de la fianza y cancelación del aval en plazo tras la entrega de llaves.

## Documentos que se entregan

Dos documentos en Word, según `references/formato-y-entrega-contratos.md`:

1. `contrato-arrendamiento-local-<apellido-o-denominación-del-cliente>-<AAAAMMDD>.docx` (temporada: `contrato-arrendamiento-temporada-...`).
2. `nota-arrendamiento-local-<apellido-o-denominación-del-cliente>-<AAAAMMDD>.docx`

**Estructura del contrato** (una definición por término: «el Local», «la Actividad», «la Renta»):

- «CONTRATO DE ARRENDAMIENTO PARA USO DISTINTO DEL DE VIVIENDA», lugar y fecha. **REUNIDOS**, **INTERVIENEN** y **EXPONEN** (titularidad, datos registrales, referencia catastral `[REFERENCIA CATASTRAL]`, cargas, estado, actividad prevista, estatutos de la comunidad; en temporada, la causa temporal).
- **ESTIPULACIONES**: PRIMERA.- Objeto y destino (Actividad concreta; prohibición de otras). SEGUNDA.- Régimen jurídico (art. 4.3 LAU y exclusión expresa, artículo por artículo, de los preceptos del título III que no se quieran aplicar). TERCERA.- Duración, obligado cumplimiento, prórrogas y exclusión de la tácita reconducción. CUARTA.- Renta, IVA y pago. QUINTA.- Actualización. SEXTA.- Carencia y obras de adecuación. SÉPTIMA.- Licencias. OCTAVA.- Gastos, tributos, suministros y seguros. NOVENA.- Conservación y obras. DÉCIMA.- Cesión, subarriendo y cambio de control. UNDÉCIMA.- Adquisición preferente. DUODÉCIMA.- Desistimiento e indemnización. DECIMOTERCERA.- Indemnización del art. 34 LAU (mantenida, cuantificada o renunciada). DECIMOCUARTA.- Fianza y garantías adicionales. DECIMOQUINTA.- Incumplimiento y resolución. DECIMOSEXTA.- Devolución del Local. DECIMOSÉPTIMA.- Notificaciones y dirección electrónica. DECIMOCTAVA.- Datos, ley aplicable, negociación previa y fuero o arbitraje.
- Firmas en dos columnas y **ANEXOS**: plano, inventario de instalaciones, etiqueta energética, proyecto de obras, modelo de aval, consulta catastral.

**Reparto para la redacción rápida:** una sección por bloque de estipulaciones (`### [ESTIPULACION]`): comparecencia, expositivos, objeto y régimen jurídico (con las exclusiones del título III, artículo por artículo) / duración, renta, actualización, carencia, obras y licencias / gastos, conservación, cesión y subarriendo, adquisición preferente / desistimiento, indemnización del art. 34, fianza y garantías, resolución y devolución / notificaciones, datos, ley, fuero, firmas y anexos. La nota: apartado 11 del formato.

**Nota para el abogado** (2-5 páginas): régimen aplicable (imperativo frente a pactado) con los artículos leídos; preceptos del título III excluidos y por qué; cláusulas críticas con su fundamento y, cuando lo exija el apartado 8, párrafo literal con órgano, fecha y ECLI; compatibilidad de la actividad (ordenanza leída o informe pendiente); pendientes (nota simple, estatutos, licencia, depósito de la fianza); riesgos para la posición del cliente; tributos que hay que comprobar.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los arts. 1, 3, 4, 29 a 37 LAU y los preceptos a los que remiten, los del Código Civil usados, el art. 63 del texto refundido de Haciendas Locales, el art. 7 LPH y los de catastro y certificado energético.
- [ ] Detector pasado: uso distinto real (o temporada con causa acreditada), no vivienda permanente, no alquiler turístico ni arrendamiento de industria.
- [ ] Cada precepto del título III excluido se nombra de forma expresa (art. 4.4 LAU); ninguna exclusión de los títulos I y IV.
- [ ] Fianza de dos mensualidades en metálico; garantías adicionales con importe, duración y forma de ejecución.
- [ ] Actividad contrastada con estatutos y ordenanzas (`buscar_ordenanzas` o, si el municipio no está cubierto, ordenanza oficial en internet con enlace) o marcada como pendiente de informe urbanístico.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; ninguno en el contrato.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); cada «posible disonancia» contrastada con el artículo leído.
- [ ] Marcadores en lugar de datos inventados; renta, carencia, plazos, preavisos y definiciones coherentes.
- [ ] Resumen para el abogado según el apartado 10 del formato, con fecha de inicio, fin del obligado cumplimiento, fechas de preaviso (incluido el de cuatro meses del art. 34 si se mantiene) y primera actualización, cada una con su precepto o cláusula.
