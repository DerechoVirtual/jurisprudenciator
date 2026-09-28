---
name: arrendamiento-vivienda
description: >-
  Redacta el contrato de arrendamiento de vivienda habitual (LAU tras el Real Decreto-ley 7/2019 y la
  Ley 12/2023) y su nota para el abogado, en Word, defendiendo al arrendador o al arrendatario. Úsala
  cuando el abogado diga «contrato de alquiler», «arrendamiento de piso», «alquilar mi vivienda»,
  «inquilino», «prórroga de cinco o siete años», «actualización de la renta», «zona tensionada»,
  «fianza y aval» o «gastos de la inmobiliaria». Cubre duración y prórrogas, arrendador persona
  jurídica y gran tenedor, renta y sus límites, fianza y garantías adicionales, gastos, obras, cesión,
  desistimiento, adquisición preferente, certificado energético y Catastro. Si el arrendamiento es de
  temporada, local u oficina, usa arrendamiento-local-negocio; si es alquiler turístico, está fuera de
  la LAU; para revisar el contrato de la otra parte, revision-contrato-semaforo.
---

# Arrendamiento de vivienda

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Ámbito, régimen imperativo, exclusiones y forma** → `buscar_articulo` (`ley="LAU"`, artículos `"1"`, `"2"`, `"3"`, `"4"`, `"5"`, `"6"`, `"7"` y `"37"`).
- **Duración, prórrogas, desistimiento, subrogaciones y extinción** → `buscar_articulo` (`ley="LAU"`, artículos `"9"`, `"10"`, `"11"`, `"12"`, `"13"`, `"14"`, `"15"`, `"16"`, `"27"` y `"28"`); supletorio (`ley="CC"`, artículos `"1554"`, `"1555"`, `"1561"` y `"1563"`).
- **Renta, actualización, mejoras, gastos, fianza y garantías** → `buscar_articulo` (`ley="LAU"`, artículos `"17"`, `"18"`, `"19"`, `"20"` y `"36"`), fiador (`ley="CC"`, artículos `"1822"`, `"1831"` y `"1837"`) y `leer_boe` (`identificador="BOE-A-2024-26685"`, índice que limita la actualización desde 2025).
- **Obras, cesión, subarriendo y adquisición preferente** → `buscar_articulo` (`ley="LAU"`, artículos `"8"`, `"21"`, `"22"`, `"23"`, `"24"`, `"25"` y `"26"`).
- **Gran tenedor, zonas tensionadas, información previa, certificado energético, Catastro y uso turístico** → `buscar_articulo` (`ley="Ley 12/2023"`, artículos `"3"`, `"18"` y `"31"`), (`ley="BOE-A-2021-9176"`, `articulo="17"`), (`ley="Real Decreto Legislativo 1/2004"`, artículos `"38"` y `"40"`), (`ley="Ley 49/1960"`, artículos `"7"` y `"17"`) y (`ley="BOE-A-2024-26931"`, artículos `"1"`, `"2"` y `"3"`); inmueble → `consultar_catastro`.
- **Doctrina sobre temporada encubierta, renuncias del arrendatario, garantías, gastos y desistimiento** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; `base="AN"` + `tipo_organo="AP"`, con `anios=3` en lo reformado por la Ley 12/2023) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Arrendador o arrendatario sociedad** → `buscar_empresa_mercantil`; **depósito autonómico de la fianza** → `buscar_boe` (`consulta="depósito de fianzas"` o `consulta="fianzas de arrendamientos"`); **tributación** → `buscar_articulo` (`ley="BOE-A-2006-20764"`, `articulo="23"`) y `buscar_consultas_hacienda`; **reclamación futura** → `buscar_articulo` (`ley="LEC"`, `articulo="439"`; `ley="LO 1/2025"`, `articulo="5"`).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Cita la ley como «artículo N de la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos» y la vivienda como «artículo N de la Ley 12/2023, de 24 de mayo, por el derecho a la vivienda»: así las reconoce `verificar_escrito`.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Arrendamiento de una edificación habitable cuyo destino primordial es la necesidad permanente de vivienda del arrendatario (art. 2 LAU), con o sin garaje, trastero y muebles del mismo arrendador.
- Contrato nuevo, renovación con contrato nuevo o sustitución del modelo de la inmobiliaria cuando el cliente aún no ha firmado.

Pasa este detector antes de redactar. Si encaja otra figura, díselo al abogado con el artículo leído y deriva:

| Situación | Qué procede |
|---|---|
| Alquiler por temporada (curso, desplazamiento laboral, verano, obras en su casa) o para oficina, despacho, comercio | Uso distinto de vivienda (art. 3 LAU): `arrendamiento-local-negocio`. Si el arrendatario no tiene otra vivienda y va a vivir allí de forma permanente, es vivienda aunque se titule «de temporada»: usa esta skill |
| Cesión de vivienda amueblada comercializada en canales turísticos y sometida a normativa turística | Excluida de la LAU (art. 5.e): no la redactes con esta skill. Explica al abogado que rige la normativa turística autonómica (búscala con `buscar_boe`), las ordenanzas municipales (`buscar_ordenanzas`) y la aprobación previa de la comunidad de propietarios (art. 7.3 y 17.12 LPH) |
| Vivienda de más de 300 m² o renta anual inicial superior a 5,5 veces el salario mínimo interprofesional anual, y se arrienda entera | Esta skill, pero con el régimen del art. 4.2 LAU (prima la voluntad de las partes). Jurisprudenciator no da la cuantía del salario mínimo: búscala en internet en el real decreto vigente publicado en el BOE y cítala con enlace y fecha |
| Portería, vivienda militar, universitaria o finca con aprovechamiento agrario primordial | Excluidas (art. 5 LAU): no la redactes; díselo al abogado |
| Adenda, prórroga pactada, subrogación o cambio de arrendatario en un contrato vigente | `modificacion-novacion-cesion` |
| Contrato de la otra parte para revisar o contestar | `revision-contrato-semaforo` o `negociacion-contrapropuesta` |
| Impago, daños, obras no consentidas o reclamación de la fianza | `requerimiento-cumplimiento`, `resolucion-por-incumplimiento` o `reclamacion-deuda-monitorio` |
| Arrendatario consumidor frente a arrendador empresario que usa un modelo para todos | Esta skill y `condiciones-generales-consumidores` para auditar el modelo |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende el abogado: arrendador o arrendatario.
2. ★ Arrendador: persona física o jurídica (cambia los plazos de cinco a siete años); número de inmuebles urbanos de uso residencial y superficie que posee, para saber si es gran tenedor (art. 3.k de la Ley 12/2023); si es usufructuario o la vivienda tiene hipoteca (art. 13 LAU). Sociedad: `buscar_empresa_mercantil` y poder de quien firma.
3. ★ Arrendatario o arrendatarios: identificación, quién va a vivir (cónyuge, hijos, art. 7 LAU), solvencia y avalistas.
4. ★ Vivienda: dirección o referencia catastral (`consultar_catastro`), nota simple o título de propiedad, superficie, anexos, muebles e inventario, certificado de eficiencia energética registrado y etiqueta, cédula de habitabilidad si la comunidad autónoma la exige.
5. ★ Destino real: vivienda habitual y permanente. Si hay una causa temporal, pídela concreta y pasa el detector.
6. ★ Municipio y si está en una zona de mercado residencial tensionado declarada (resolución y fecha de vigencia); en ese caso, renta del último contrato de vivienda habitual de los últimos cinco años y su actualización (arts. 17.6 y 17.7 LAU y 31.3 de la Ley 12/2023). `buscar_boe` no localiza las declaraciones de zona tensionada: si el abogado no aporta la resolución, búscala en internet (BOE y sede del ministerio competente en vivienda) y cítala con enlace y fecha de consulta; si tampoco aparece, marca `[ZONA TENSIONADA: CONFIRMAR]` y no fijes una renta que pueda superar el límite sin advertirlo en la nota.
7. ★ Renta mensual, día y forma de pago, cuenta, actualización querida y gastos que se repercuten (comunidad, IBI, tasas) con su importe anual.
8. ★ Duración pactada y, si el arrendador es persona física, si puede necesitar la vivienda antes de cinco años y para quién (art. 9.3 LAU).
9. Fianza, garantías adicionales (aval bancario, depósito, seguro de impago, fiador) y su importe; comunidad autónoma para el depósito de la fianza.
10. Estado de la vivienda, obras pactadas antes o durante el contrato, reparaciones pendientes.
11. Mascotas, subarriendo parcial, dirección electrónica para notificaciones (art. 4.6 LAU), intermediario y quién le paga.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo. Varios cambiaron en 2019 y en 2023: anota la línea «vigente desde» de cada uno.

**Qué es imperativo.** Los títulos I y IV rigen de forma imperativa; el arrendamiento de vivienda se rige por lo pactado dentro del título II y, supletoriamente, por el Código Civil (art. 4.1 y 4.2 LAU). Son nulas las estipulaciones que modifiquen el título II en perjuicio del arrendatario salvo que la norma lo autorice (art. 6 LAU). La exclusión de un precepto, cuando se permite, debe ser expresa y precepto por precepto (art. 4.4 LAU).

**Duración y prórrogas.**

- Duración libre; si es inferior a cinco años (siete si el arrendador es persona jurídica), prórroga obligatoria anual hasta alcanzarlos, salvo que el arrendatario avise con treinta días (art. 9.1 LAU). El plazo corre desde el contrato o desde la puesta a disposición si es posterior. Sin plazo, un año (art. 9.2).
- Necesidad del arrendador persona física (art. 9.3 LAU): solo si consta de forma expresa en el contrato al celebrarlo, tras el primer año, para vivienda permanente propia o de los familiares que enumera; comunicación con dos meses de antelación y consecuencias si no se ocupa en tres meses. El precepto lo que hace es excluir la **prórroga obligatoria**: si se pacta una duración inicial de cinco años (siete) o más, no hay prórroga que excluir y la cláusula puede no operar frente al plazo pactado. Si el cliente quiere reservarse la necesidad, pacta una duración inicial inferior (normalmente un año) con las prórrogas anuales del art. 9.1, concreta la necesidad (quién y por qué) y explícalo en la nota.
- Prórroga tácita (art. 10.1 LAU): cumplidos cinco o siete años, si nadie notifica (arrendador cuatro meses antes; arrendatario dos), prórroga anual hasta tres años más.
- Prórrogas extraordinarias: un año a petición del arrendatario vulnerable con informe de servicios sociales, obligatoria si el arrendador es gran tenedor (art. 10.2); hasta tres años en zona tensionada, obligatoria salvo las excepciones del art. 10.3.
- Desistimiento del arrendatario (art. 11 LAU): tras seis meses, con treinta días de preaviso; solo puede pactarse una indemnización de una mensualidad por año que reste, proporcional. Una penalización mayor es nula (art. 6).
- Venta o ejecución de la vivienda: el adquirente se subroga durante cinco o siete años aunque sea tercero hipotecario (art. 14); si el derecho del arrendador se resuelve por ejecución hipotecaria u otras causas, el arrendatario continúa hasta ese plazo (art. 13.1). Más allá, solo si el arrendamiento se inscribió antes que el derecho que lo resuelve: si defiendes a un arrendatario con contrato largo, recomienda inscribirlo.

**Renta y actualización.**

- Renta libre, salvo zonas tensionadas (art. 17.1, 17.6 y 17.7 LAU): en zona tensionada, la renta inicial no puede superar la del último contrato de vivienda habitual de los cinco años anteriores actualizada, con un incremento máximo del diez por ciento solo en los supuestos tasados del art. 17.6; con arrendador gran tenedor (y en viviendas sin contrato anterior si lo dice la declaración), el límite es el índice de referencia (art. 17.7). En zona tensionada el contrato debe expresar la última renta y el valor del índice (art. 31.3 de la Ley 12/2023), y el mismo art. 17.6 prohíbe **repercutir al nuevo arrendatario cuotas o gastos que no estuvieran en el contrato anterior** (por ejemplo, el IBI si antes no se repercutía): pide el contrato anterior y compara. Si el cliente quiere más renta, revisa con él los supuestos del diez por ciento (la letra d, contrato o derecho de prórroga potestativo de diez años, es la única que no exige obras acreditadas) y adviértele de si son compatibles con la necesidad del art. 9.3.
- Pago mensual en los siete primeros días salvo pacto; nunca más de una mensualidad anticipada (art. 17.2); por medios electrónicos, salvo la excepción del art. 17.3; recibo o medio que acredite el pago (art. 17.4). La renta puede sustituirse por obras de reforma pactadas (art. 17.5).
- Actualización (art. 18 LAU): solo en cada aniversario, según lo pactado; sin pacto expreso no hay actualización; si el pacto no fija índice, se aplica el Índice de Garantía de Competitividad; el incremento nunca supera la variación del IPC. Desde el 1 de enero de 2025 opera además como límite el índice de referencia definido por el INE (lee la resolución con `leer_boe`, `identificador="BOE-A-2024-26685"`: dice que la crea una disposición adicional de la LAU que `buscar_articulo` no devuelve; si necesitas su texto, léelo en internet en el texto consolidado de la LAU en el BOE). Jurisprudenciator no da el valor mensual del índice: búscalo en internet en la web del INE y cítalo con enlace, mes de referencia y fecha de consulta. Busca con `buscar_boe` (`consulta="actualización renta arrendamiento vivienda"`, `desde` el año anterior) si hay una limitación extraordinaria posterior y, si la hay, léela.
- Mejoras (art. 19 LAU): elevación legal tras cinco o siete años; en cualquier momento, por acuerdo, sin reiniciar los plazos (art. 19.4).

**Gastos, fianza y garantías.**

- Gastos generales e IBI a cargo del arrendatario solo si el pacto consta por escrito y fija su importe anual (en zona tensionada, solo los que ya repercutía el contrato anterior, art. 17.6); incrementos limitados durante los primeros cinco o siete años (art. 20.1 y 20.2 LAU). Los suministros con contador son del arrendatario (art. 20.3). **Los gastos de gestión inmobiliaria y de formalización del contrato son del arrendador** (art. 20.1, en vigor desde 2023): no los traslades al arrendatario por ninguna vía.
- Fianza obligatoria en metálico de una mensualidad (art. 36.1 LAU), sin actualizar durante cinco o siete años (art. 36.2); el saldo no devuelto devenga interés legal pasado un mes desde la entrega de llaves (art. 36.4).
- Garantías adicionales (art. 36.5 LAU): se puede pactar cualquier garantía, pero en contratos de hasta cinco años (siete con arrendador persona jurídica) su valor no puede exceder de dos mensualidades. Suma aval, depósito y cualquier otra garantía para comprobar el límite.
- Depósito de la fianza: lo regula cada comunidad autónoma. Pregunta la comunidad y busca su norma con `buscar_boe`; si no aparece o no puedes leer el precepto, búscala en internet en el boletín o la sede electrónica de la comunidad autónoma y cítala con enlace y fecha de consulta; nunca des plazos ni importes de memoria.

**Obras, cesión y adquisición preferente.**

- El arrendador conserva la habitabilidad sin subir la renta (art. 21.1); las pequeñas reparaciones por desgaste ordinario son del arrendatario (art. 21.4); obras de mejora con preaviso de tres meses y facultad de desistir (art. 22); obras del arrendatario solo con consentimiento escrito (art. 23); adaptaciones por discapacidad (art. 24).
- Cesión con consentimiento escrito; subarriendo solo parcial, con consentimiento escrito y precio no superior a la renta (art. 8 LAU).
- Adquisición preferente (art. 25 LAU): tanteo en treinta días naturales y retracto; puede pactarse la renuncia (art. 25.8), y entonces el arrendador debe comunicar su intención de vender con treinta días de antelación.

**Otras comprobaciones.**

- Información mínima (art. 31 de la Ley 12/2023) y copia de la etiqueta energética anexa al contrato, con el documento de recomendaciones de uso (art. 17.2 del Real Decreto 390/2021, de 1 de junio).
- Referencia catastral en el contrato: la aporta el arrendador (arts. 38 y 40.1.d del Real Decreto Legislativo 1/2004). Consulta el inmueble con `consultar_catastro` y compara superficie y uso con lo declarado; País Vasco y Navarra, fuera del conector: consulta en internet la sede del catastro foral (o usa la certificación que aporte el abogado) y cita enlace y fecha.
- Arrendador: adviértele de que una futura demanda de recuperación de la posesión debe decir si la vivienda es habitual del ocupante y si él es gran tenedor, con certificación registral de sus propiedades si niega serlo (art. 439.6 LEC), y de que antes de demandar habrá que intentar un medio adecuado de solución de controversias (art. 5 de la Ley Orgánica 1/2025). Pacta una dirección electrónica válida para notificaciones (art. 4.6 LAU).
- Alquiler de corta duración y temporada ofertado en plataformas: lee los arts. 1, 2 y 3 del Real Decreto 1312/2024 con sus notas «Téngase en cuenta» (el Tribunal Supremo anuló en 2026 parte del procedimiento de registro único) y cita solo lo que siga vigente.
- Tributación: no des tipos. Avisa de qué comprobar (reducciones del IRPF del arrendador, tributación del contrato para el arrendatario y, si el arrendador es empresario, el IVA). Las reducciones del rendimiento del arrendador están en el art. 23.2 de la Ley 35/2006 (`buscar_articulo`, `ley="BOE-A-2006-20764"`, `articulo="23"`), que premia rebajar la renta en zona tensionada: léelo y dile al abogado qué porcentaje resulta de la renta pactada. Para criterios administrativos, `buscar_consultas_hacienda`; si no responde, busca la consulta en internet en la base oficial de la Dirección General de Tributos y cítala con enlace.

## Cláusulas clave y jurisprudencia

Busca con `buscar_sentencias` (`jurisdiccion="CIVIL"`), lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y comprueba que es razonamiento de la Sala. Toda renuncia a derechos del arrendatario exige jurisprudencia (apartado 8 del formato): si tras dos reformulaciones no hay resolución aplicable, sigue el punto 3 de la puerta.

1. **Calificación: vivienda o temporada.** `consulta="arrendamiento de temporada vivienda habitual calificación fraude de ley"`, `base="AN"`, `tipo_organo="AP"`, `anios=3`. Pro arrendador: si la causa es realmente temporal, deriva y deja la causa acreditada en el contrato; si no lo es, no disfraces el contrato: explícale el riesgo de nulidad de las cláusulas contrarias al título II. Pro arrendatario: la nota identifica las cláusulas nulas si el contrato se presenta como de temporada.
2. **Duración, renuncia a la prórroga y necesidad del arrendador.** `consulta="necesidad del arrendador de ocupar la vivienda artículo 9.3 constar en el contrato"` (`base="TS"`) y `consulta="renuncia prórroga obligatoria arrendamiento vivienda nulidad cláusula"` (`base="AN"`, `tipo_organo="AP"`, `anios=3`). Pro arrendador: cláusula de necesidad concreta (quién y para qué), nunca renuncia genérica a la prórroga. Pro arrendatario: duración igual o superior a la mínima y prórroga extraordinaria mencionada si procede.
3. **Renta y actualización.** Pro arrendador: índice expreso, fecha de actualización y notificación por nota en el recibo (art. 18.2); en zona tensionada, fija la renta dentro del límite y documenta el supuesto del diez por ciento si se aplica. Pro arrendatario: sin actualización o con el índice más bajo; exige que conste la última renta en zona tensionada.
4. **Gastos repercutidos.** `consulta="gastos de gestión inmobiliaria y formalización del contrato a cargo del arrendador"` y `consulta="pacto gastos comunidad IBI arrendatario importe anual artículo 20"`, ambas `base="AN"`, `tipo_organo="AP"`, `anios=3`. Pro arrendador: pacto por escrito con importe anual de cada concepto. Pro arrendatario: sin importe anual pactado, el pacto no vale.
5. **Fianza y garantías adicionales.** `consulta="garantía adicional fianza arrendamiento vivienda límite dos mensualidades"`, `base="AN"`, `tipo_organo="AP"`. Pro arrendador: aval a primer requerimiento o seguro de impago dentro del límite, fiador solidario con renuncia expresa a los beneficios de excusión y división (arts. 1831 y 1837 CC) si lo acepta. Pro arrendatario: suma todas las garantías y exige plazo y forma de devolución de la fianza con inventario de salida.
6. **Desistimiento.** `consulta="desistimiento arrendatario vivienda indemnización artículo 11"` (`base="TS"` y después `base="AN"`, `tipo_organo="AP"`). Pro arrendador: pacta la indemnización del art. 11 y el preaviso por escrito. Pro arrendatario: sin indemnización o proporcional; cualquier pena superior es nula.
7. **Renuncia a la adquisición preferente.** `consulta="renuncia derecho de adquisición preferente arrendatario vivienda artículo 25"` (`base="TS"` y, si no hay doctrina aplicable, `base="AN"`, `tipo_organo="AP"`). Pro arrendador: renuncia expresa del art. 25.8 con el compromiso de comunicar la venta con treinta días. Pro arrendatario: conserva el derecho o exige a cambio el deber de ofrecerle la compra.
8. **Conservación y pequeñas reparaciones.** Delimita con ejemplos qué es desgaste ordinario (art. 21.4) y qué conservación (art. 21.1); pro arrendatario, plazo de respuesta del arrendador y facultad de reparar lo urgente del art. 21.3.

## Documentos que se entregan

Dos documentos en Word, según `references/formato-y-entrega-contratos.md`:

1. `contrato-arrendamiento-vivienda-<apellido-o-denominación-del-cliente>-<AAAAMMDD>.docx`
2. `nota-arrendamiento-vivienda-<apellido-o-denominación-del-cliente>-<AAAAMMDD>.docx`

**Estructura del contrato** (una definición por término: «la Vivienda», «la Renta», «la Fianza»):

- «CONTRATO DE ARRENDAMIENTO DE VIVIENDA», lugar y fecha. **REUNIDOS**, **INTERVIENEN** y **EXPONEN** (titularidad, descripción, referencia catastral `[REFERENCIA CATASTRAL]`, anexos, estado, certificado energético, información entregada, zona tensionada y última renta si procede).
- **ESTIPULACIONES**: PRIMERA.- Objeto y destino (vivienda habitual y permanente; personas que la habitarán). SEGUNDA.- Duración, prórrogas y, si procede, necesidad del arrendador del art. 9.3. TERCERA.- Renta, pago y medios. CUARTA.- Actualización. QUINTA.- Gastos generales, tributos y suministros (con importe anual). SEXTA.- Fianza y garantías adicionales. SÉPTIMA.- Entrega, estado e inventario. OCTAVA.- Conservación, reparaciones y obras. NOVENA.- Cesión y subarriendo. DÉCIMA.- Adquisición preferente. UNDÉCIMA.- Desistimiento. DUODÉCIMA.- Incumplimiento y resolución. DECIMOTERCERA.- Devolución de la Vivienda y de la Fianza. DECIMOCUARTA.- Notificaciones y dirección electrónica. DECIMOQUINTA.- Protección de datos, ley aplicable y fuero.
- En el contrato, cita artículos solo cuando el efecto dependa de ello (art. 9.3, 11, 25.8 y 36.5 LAU); el resto va a la nota.
- Firmas en dos columnas y **ANEXOS**: inventario con fotografías, etiqueta energética y recomendaciones de uso, información del art. 31 de la Ley 12/2023, consulta catastral, justificante de la fianza y de las garantías.

**Nota para el abogado** (2-5 páginas): régimen aplicable (general o del art. 4.2), plazos que resultan según sea persona física o jurídica, límites de renta y actualización aplicados, cláusulas críticas con artículo y, cuando lo exija el apartado 8, párrafo literal con órgano, fecha y ECLI; pendientes (zona tensionada, valor del índice, depósito autonómico de la fianza, certificado energético); riesgos para la posición del cliente; tributos y formalidades que hay que comprobar.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos de la LAU usados, los de la Ley 12/2023, el art. 17 del Real Decreto 390/2021 y los del catastro, con su vigencia; leída con `leer_boe` la resolución del índice si hay cláusula de actualización.
- [ ] Detector pasado: vivienda habitual, no temporada ni uso turístico; régimen del art. 4.2 identificado si procede.
- [ ] Plazos de cinco o siete años aplicados según la naturaleza del arrendador; necesidad del art. 9.3 solo con arrendador persona física y causa expresa.
- [ ] Ningún gasto de gestión o formalización a cargo del arrendatario; gastos repercutidos con importe anual.
- [ ] Fianza de una mensualidad y garantías adicionales dentro del límite del art. 36.5 cuando el contrato no supera cinco o siete años.
- [ ] Zona tensionada confirmada con la resolución (aportada por el abogado o hallada en internet, con enlace) o marcada como pendiente; renta y actualización dentro de los límites leídos.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; ninguno en el contrato.
- [ ] `verificar_escrito` pasado sobre contrato y nota; cada «posible disonancia» contrastada con el artículo leído.
- [ ] Marcadores en lugar de datos inventados; renta, fechas, plazos y definiciones coherentes.
- [ ] Resumen para el abogado según el apartado 10 del formato, con la fecha de inicio, el final del plazo mínimo, la primera actualización posible y los preavisos de cada parte calculados con su precepto.
