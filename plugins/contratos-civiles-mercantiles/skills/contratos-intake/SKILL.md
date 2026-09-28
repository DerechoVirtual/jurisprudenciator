---
name: contratos-intake
description: >-
  Puerta de entrada del plugin de contratos civiles y mercantiles para el primer encargo de un cliente.
  Clasifica qué necesita (redactar, revisar, negociar, reclamar por incumplimiento o interpretar),
  identifica las partes y la posición del cliente, el tipo de contrato, la cuantía, la ley aplicable
  (común, foral o extranjera) y las urgencias (caducidad del saneamiento, prescripción, preavisos,
  vencimientos, fecha de firma), calcula cada plazo con su precepto y deriva a la skill del catálogo.
  Entrega una ficha del encargo en Word, no un contrato. Úsala con «cliente nuevo», «me han pasado un
  contrato», «firma la semana que viene», «no le pagan», «qué hago con este contrato». Si ya se sabe
  qué hay que hacer, ve directamente a la skill de ese contrato; para comprobar quién firma, usa
  verificacion-partes-contrato.
---

# Primer encargo de contratos: ficha, urgencias y derivación

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazos que pueden estar corriendo** → `buscar_articulo` (`ley="CC"`, artículos `"5"` para el cómputo, `"1964"`, `"1966"`, `"1967"`, `"1968"`, `"1969"` y `"1973"`; `"1490"` si hay defectos en una compraventa; `"1301"` si se discute el consentimiento) y, según el contrato, (`ley="CCom"`, `"325"` y `"326"` para calificar la venta, `"336"` y `"342"`), (`ley="TRLGDCU"`, `"120"` y `"124"`), (`ley="BOE-A-1999-21567"`, `"17"` y `"18"`) o (`ley="Ley 12/1992"`, `"25"` y `"31"`).
- **Reclamación: negociación previa, mora y resolución** → `buscar_articulo` (`ley="LO 1/2025"`, artículos `"5"` y `"7"`; `ley="CC"`, `"1100"` y `"1124"`).
- **Ley aplicable** → `buscar_articulo` (`ley="CC"`, `articulo="10"`); con un elemento extranjero, (`ley="32008R0593"`, artículos `"3"`, `"4"` y `"6"`); con Derecho civil propio, `buscar_boe` (título de la norma) y `leer_boe` (su identificador).
- **Consumidor o empresario** → `buscar_articulo` (`ley="TRLGDCU"`, `articulo="3"`).
- **¿Contrato civil o mercantil, o relación laboral encubierta?** (agente, comercial, colaborador o «autónomo» que trabaja con instrucciones de la empresa) → `buscar_articulo` (`ley="Ley 12/1992"`, artículos `"1"` y `"2"`; `ley="ET"`, artículos `"2"` y `"59"`; representantes de comercio, `ley="BOE-A-1985-17410"`, artículos `"1"` y `"11"`; orden social, `ley="LRJS"`, `articulo="2"`).
- **Criterio vigente sobre el plazo que marca la urgencia** → `buscar_sentencias` (p. ej. `consulta="saneamiento vicios ocultos caducidad de la acción seis meses"` o, para saber si una compra entre empresas es civil o mercantil, `consulta="maquinaria compraventa civil no mercantil reventa artículo 325"`; `base="TS"`, `jurisdiccion="CIVIL"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión). Las consultas cortas, de cinco a ocho palabras, encuentran más que las frases largas.
- **Partes que son sociedades** → `buscar_empresa_mercantil` (denominación exacta o CIF); **inmuebles** → `consultar_catastro` (referencia catastral, o dirección y municipio).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Primera consulta sobre un contrato, antes de saber si hay que redactar, revisar, negociar, reclamar o interpretar.
- El cliente trae un contrato, un borrador, un burofax o una factura impagada y hay que saber qué es, qué plazo corre y quién lo lleva.
- El despacho recibe un asunto de otro compañero y hay que ordenarlo.
- No la uses cuando el encargo ya está claro: ve a la skill de ese contrato o tarea (tabla de derivación). Si lo único pendiente es comprobar quién firma, usa `verificacion-partes-contrato`.
- Si en las preguntas de urgencia aparece una firma en días, un requerimiento con plazo o mercaderías recibidas con defectos, aplica el semáforo en ese momento y completa la ficha después.

## Datos que hay que reunir antes de redactar

No redactes la ficha al primer mensaje. Pregunta en este orden; si falta un dato imprescindible (★), pídelo antes de seguir.

**Paso 1. Tres preguntas de urgencia (siempre primero).**

1. ★ ¿Hay fecha de firma, de entrega, de vencimiento o de prórroga del contrato? ¿Cuál?
2. ★ ¿Ha recibido el cliente un requerimiento, burofax, propuesta de negociación, reclamación o demanda? Pide copia y la **fecha de recepción**.
3. ★ ¿Ha descubierto un defecto en algo que compró o recibió, o ha dejado de cumplir la otra parte? Pide la **fecha de entrega o recepción** y la fecha en que lo descubrió.

**Paso 2. Qué quiere el cliente.** ★ Redactar, revisar, negociar, reclamar, interpretar, modificar o terminar (tabla de clasificación). Anota su objetivo con sus palabras y el plazo en que lo necesita.

**Paso 3. Partes y posición.** ★ Quién es el cliente y qué posición ocupa (vendedor o comprador, arrendador o arrendatario, prestador o cliente, franquiciador o franquiciado, prestamista o prestatario). ★ Quién es la otra parte. Para cada sociedad, denominación y CIF; para cada persona física, marcadores (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`) si no los facilita. Quién firmará por cada parte y con qué cargo o poder.

**Paso 4. Contrato.** ★ Tipo (por su contenido, no por su título), objeto, precio o cuantía, duración, fechas (firma, entrega, inicio, vencimiento). ¿Hay borrador o contrato firmado? Pide el texto íntegro con anexos.

**Paso 5. Consumo o empresa.** ★ ¿Alguna parte actúa con un propósito ajeno a su actividad empresarial o profesional? ¿El texto es un modelo impuesto por una parte (condiciones generales)?

**Paso 6. Ley aplicable.** ★ Dónde está el inmueble, si lo hay; residencia y nacionalidad de las partes; vecindad civil si puede aplicar un Derecho civil propio (Cataluña, Aragón, Navarra, País Vasco, Galicia, Baleares); cláusula de ley aplicable, fuero o arbitraje del contrato.

**Paso 7. Documentos y antecedentes.** Correos y ofertas previas, facturas, albaranes, actas de entrega, requerimientos enviados o recibidos (con fecha), pagos realizados.

Si el cliente no sabe una fecha, anótala como `[FECHA PENDIENTE]` y no calcules el plazo que depende de ella.

## Régimen jurídico y comprobaciones

### Clasificación del encargo

| Lo que pide el cliente | Tipo | Skill |
|---|---|---|
| Necesita un contrato nuevo | Redactar | La del contrato (tabla de derivación), precedida de `verificacion-partes-contrato` si hay sociedades, apoderados, inmuebles o personas con apoyos |
| Le han pasado un contrato para firmar | Revisar | `revision-contrato-semaforo`; si es un clausulado de adhesión con consumidores, `condiciones-generales-consumidores` |
| Ha recibido un borrador y quiere cambiarlo | Negociar | `negociacion-contrapropuesta` (si no hay informe de riesgos, antes `revision-contrato-semaforo`) |
| La otra parte no paga o no cumple | Reclamar | `requerimiento-cumplimiento`; después `masc-propuesta-acuerdo` y, según el caso, `reclamacion-deuda-monitorio` o `resolucion-por-incumplimiento`; defectos en lo recibido, `vicios-ocultos-saneamiento` |
| Discrepan sobre qué dice el contrato o han cambiado las circunstancias | Interpretar | `dictamen-interpretacion-contrato` |
| El «agente», comercial, colaborador o prestador persona física trabaja con ruta, horario, instrucciones, exclusividad o medios de la empresa | Posible relación laboral (fuera de este plugin) | Anótalo en la ficha con sus indicios y deriva **también** al plugin de Derecho laboral; mantén la vía civil que proceda. Los plazos laborales corren aparte y la acción de despido caduca en veinte días hábiles (ET 59): calcúlalos en la ficha |
| Quiere prorrogar, cambiar, ceder o terminar de mutuo acuerdo | Modificar | `modificacion-novacion-cesion` |

### Semáforo de urgencias

Lee con `buscar_articulo` el precepto de cada fila antes de escribir el plazo en la ficha. Si el texto trae una nota «Téngase en cuenta que esta actualización… entra en vigor el…» seguida de un texto entre comillas (ocurre en los arts. 120, 123 y 124 del TRLGDCU), el texto vigente es el que va **antes** de la nota cuando esa fecha ya ha pasado; el entrecomillado es la redacción anterior.

| Nivel | Situación | Precepto que se lee | Qué hacer y a qué skill |
|---|---|---|---|
| Rojo (días) | Firma prevista en siete días o menos | Los del tipo de contrato | Revisión limitada a partes y cláusulas en ROJO: `verificacion-partes-contrato` y `revision-contrato-semaforo`; si hay que redactar, la skill del contrato |
| Rojo (días) | Mercaderías recibidas con defectos en una compraventa mercantil (compra para revender, CCom 325; si hay duda sobre la calificación, trata el caso como mercantil a efectos del plazo) | CCom 336 (cuatro días desde el recibo, si venían embaladas) y 342 (treinta días desde la entrega, vicios internos) | Denuncia escrita dentro del plazo; `vicios-ocultos-saneamiento` |
| Rojo (días) | Requerimiento, reclamación o solicitud de negociación recibida | LO 1/2025, art. 7 (sin respuesta escrita ni primera reunión en treinta días naturales desde la recepción, el cómputo de los plazos del solicitante se reinicia o se reanuda; la colaboración de cada parte se valora después en costas) | Responder por escrito dentro de esos treinta días: `requerimiento-cumplimiento` (contestación) o `masc-propuesta-acuerdo` |
| Naranja (semanas) | Defecto oculto en una compraventa civil | CC 1484, 1486 y 1490 (seis meses desde la entrega) | `vicios-ocultos-saneamiento`; comprueba si cabe la vía del art. 1124 CC (búsqueda de «Criterio vigente») |
| Naranja (semanas) | Falta de conformidad en una compra de consumo | TRLGDCU 120 (tres años desde la entrega en bienes) y 124 (cinco años desde la manifestación) | `vicios-ocultos-saneamiento` o `condiciones-generales-consumidores` |
| Naranja (semanas) | Contrato que vence, se prorroga o hay que denunciar con preaviso | Cláusula del contrato; en agencia de duración indefinida, Ley 12/1992, art. 25 | `modificacion-novacion-cesion` o la skill del contrato |
| Naranja (semanas) | Agencia extinguida: indemnización por clientela o daños | Ley 12/1992, arts. 28 y 31 (un año desde la extinción) | `agencia-distribucion-franquicia` y `requerimiento-cumplimiento` |
| Amarillo (meses) | Impago o incumplimiento contractual | CC 1964, 1966, 1967, 1969 y 1973 | `requerimiento-cumplimiento`, `reclamacion-deuda-monitorio` o `resolucion-por-incumplimiento` |
| Amarillo (meses) | Daños en un edificio | LOE 17 (plazos de garantía desde la recepción) y 18 (dos años desde que se producen los daños) | `vicios-ocultos-saneamiento` o `contrato-obra` |
| Amarillo (meses) | Error, dolo, intimidación o falta de un consentimiento necesario | CC 1301 (cuatro años, con dies a quo según el vicio) | `dictamen-interpretacion-contrato` |

### Cálculo de plazos

- **Antes de aplicar los plazos del Código de Comercio, califica la venta.** Que las dos partes sean empresas no la hace mercantil: el art. 325 CCom exige comprar cosas muebles para revenderlas con ánimo de lucro, y el art. 326 CCom excluye las compras destinadas al consumo del comprador. La compra de maquinaria, equipos o bienes para el uso propio del comprador es, en principio, civil (saneamiento del CC 1484-1490 y resolución del CC 1124), y así lo ha declarado la Sala Primera cuando el comprador no revende lo adquirido: busca y lee esa doctrina con la consulta de calificación de la lista. Mientras la calificación no sea segura, anota los dos regímenes y usa como fecha límite la más corta.
- Si lo recibido es inservible para su fin (inhabilidad total, *aliud pro alio*), la vía es el incumplimiento (CC 1124 y 1964), no los plazos del saneamiento ni el art. 342 CCom: compruébalo con la búsqueda de «Criterio vigente» y lee el fundamento de la Sala antes de anotarlo.
- Para cada plazo escribe: hecho, fecha inicial, precepto leído, naturaleza (prescripción o caducidad), fecha final calculada y quién lo vigila.
- Fecha inicial: la que fije el precepto (entrega en CC 1490 y CCom 342; recibo en CCom 336; «desde que pueda exigirse el cumplimiento» en CC 1964; «desde el día en que pudieron ejercitarse» en CC 1969; extinción del contrato en Ley 12/1992, art. 31). En las obligaciones continuadas de hacer o no hacer, el plazo del art. 1964 corre cada vez que se incumplen.
- Prescripción: se interrumpe por reclamación judicial, extrajudicial o reconocimiento del deudor (CC 1973). En obligaciones mercantiles, el art. 944 CCom solo menciona la interpelación judicial: antes de afirmar que un burofax interrumpe, lee la doctrina de la Sala Primera sobre la interpretación unitaria (`consulta="reclamación extrajudicial interrupción prescripción artículo 944 Código de Comercio"`). La reclamación interrumpe solo la acción que se ejercita: si hay dos calificaciones posibles (agencia o relación laboral, saneamiento o incumplimiento), la reclamación debe nombrar cada acción y cada concepto. Caducidad: no se interrumpe por reclamación extrajudicial. Antes de calificar el plazo del art. 1490 CC o los del CCom, lee la doctrina con la búsqueda de «Criterio vigente» y anota lo que diga.
- La solicitud de negociación previa que defina el objeto interrumpe la prescripción y suspende la caducidad desde el intento de comunicación (LO 1/2025, art. 7); los plazos se reanudan si no hay primera reunión o respuesta escrita en treinta días naturales. Anótalo como herramienta para salvar un plazo a punto de vencer y deriva a `masc-propuesta-acuerdo`.
- Obligaciones nacidas antes del 07/10/2015 (fecha de vigencia de la redacción actual del art. 1964 CC que devuelve el conector): su régimen transitorio remite al art. 1939 CC a través de la disposición transitoria quinta de la Ley 42/2015, que `buscar_articulo` no devuelve. Lee el art. 1939 CC con `buscar_articulo`, lee esa disposición transitoria en internet, en el texto del BOE (https://www.boe.es/buscar/act.php?id=BOE-A-2015-10727), y cítala con el enlace y la fecha de consulta (punto 3 de la puerta). Busca además la doctrina con `consulta="disposición transitoria quinta Ley 42/2015 artículo 1939 prescripción acciones personales"`, `base="TS"`, `jurisdiccion="CIVIL"`. Si tampoco en internet aparece el texto, aplica la puerta en ese punto.

### Ley aplicable

- Contrato interno sin Derecho civil propio en juego: Código Civil y, si es mercantil, Código de Comercio y leyes especiales.
- Elemento extranjero (parte, lugar de entrega, inmueble fuera de España): lee los arts. 3 y 4 del Reglamento Roma I (`ley="32008R0593"`) y, con consumidores, el 6. `verificar_escrito` no identifica reglamentos de la Unión: comprueba sus artículos con `buscar_articulo` e ignora su veredicto sobre ellos. La Convención de Viena sobre compraventa internacional no está en el conector: búscala en internet, en su publicación en el BOE, y cita sus artículos con el enlace y la fecha de consulta; nunca de memoria.
- Derecho civil propio: localiza la norma con `buscar_boe` por su título (Cataluña, libro primero del Código civil, Ley 29/2002, `BOE-A-2003-2410`, y libro sexto, Ley 3/2017, `BOE-A-2017-2466`; Navarra, Compilación, `BOE-A-1973-330`; Aragón, Código del Derecho Foral; País Vasco, Ley 5/2015). Tres trampas comprobadas: `buscar_articulo` no devuelve artículos con numeración de guion (pide «621-1» y responde que no encuentra el «621»); con `ley="Código civil de Cataluña"` devuelve el artículo del **Código Civil estatal** del mismo número; y `leer_boe` devuelve el texto **publicado originalmente**, no el consolidado, y cortado. Usa `leer_boe` para localizar la regla y lee su redacción vigente en internet, en el texto consolidado oficial (BOE o boletín de la comunidad autónoma), citándola con el enlace y la fecha de consulta (punto 3 de la puerta). Si tampoco así obtienes el texto vigente y el caso depende de él, aplica la puerta.

### Comprobaciones rápidas en la primera consulta

- **Sociedades**: `buscar_empresa_mercantil`. Anota estado, cargos vigentes, fecha del último acto inscrito y cualquier acto de disolución, liquidación, revocación o concurso. La etiqueta «Activa» y la lista de actos salen de un índice del BORME sin fe pública que puede no recoger los actos más recientes: en las pruebas, una sociedad declarada en concurso seguía figurando «Activa» y sin ningún acto posterior a la declaración. Si el último acto es antiguo o hay indicios de crisis, anota que el abogado debe consultar el Registro Público Concursal y pedir nota simple del Registro Mercantil. La verificación completa, en `verificacion-partes-contrato`.
- **Inmuebles**: `consultar_catastro` para referencia, uso y superficie. No da titular ni cargas: anota que falta la nota simple del Registro de la Propiedad.
- **Consumo**: si una parte es consumidora según el art. 3 del TRLGDCU, anótalo: cambia la norma imperativa, el fuero (LEC 54.2) y la skill a la que se deriva.
- **Tributación y formalidades**: anota qué hay que comprobar (IVA o ITP y AJD, plusvalía municipal, escritura, inscripción, depósito de fianza), sin tipos ni importes que no se hayan leído con una herramienta. La doctrina tributaria se busca con `buscar_consultas_hacienda` o `buscar_doctrina_teac` en la skill que tramite el encargo.

### Tabla de derivación

Lee el precepto ancla antes de anotar la derivación y antes de descartar una vía en la ficha.

| Skill | Deriva cuando | Precepto ancla |
|---|---|---|
| `verificacion-partes-contrato` | Firma una sociedad, un apoderado, una persona con apoyos, alguien casado que dispone de la vivienda, o hay un inmueble | LSC 233 y 234; CC 1320 |
| `revision-contrato-semaforo` | Hay que revisar un contrato recibido | CC 1255 |
| `negociacion-contrapropuesta` | Hay que devolver un borrador con cambios | CC 1262 |
| `condiciones-generales-consumidores` | Clausulado de adhesión o contrato con consumidores | TRLGDCU 3 y 82; `ley="BOE-A-1998-8789"`, art. 5 |
| `dictamen-interpretacion-contrato` | Discrepancia sobre el sentido del contrato o cambio de circunstancias | CC 1281 |
| `modificacion-novacion-cesion` | Adenda, novación, cesión, subrogación, prórroga o mutuo disenso | CC 1203 y 1205 |
| `contrato-arras` | Señal o arras previas a una compraventa | CC 1454 |
| `compraventa-inmueble` | Compraventa de inmueble | CC 1445 |
| `arrendamiento-vivienda` | Alquiler para necesidad permanente de vivienda | LAU 2 |
| `arrendamiento-local-negocio` | Alquiler de local, oficina, nave o por temporada | LAU 3 |
| `compraventa-mercantil` | Compraventa de mercaderías o suministro entre empresas; esa skill califica la venta y, si el comprador no compra para revender (CCom 325 y 326), aplica el régimen del Código Civil | CCom 325 y 326; `ley="BOE-A-2004-21830"`, art. 4 |
| `prestacion-servicios` | Servicios profesionales o empresariales | CC 1544 |
| `contrato-obra` | Obra o reforma | CC 1588; LOE 17 |
| `agencia-distribucion-franquicia` | Agencia, distribución o franquicia | Ley 12/1992, art. 1; RD 201/2010, art. 3 |
| `prestamo-reconocimiento-deuda` | Préstamo o reconocimiento de deuda | CC 1740; Ley de 23 de julio de 1908, art. 1 |
| `pacto-de-socios` | Pacto parasocial | LSC 29 |
| `compraventa-participaciones` | Compraventa de participaciones o acciones | LSC 107 |
| `confidencialidad-nda` | Acuerdo de confidencialidad | `ley="BOE-A-2019-2364"`, art. 1 |
| `licencia-cesion-propiedad-intelectual` | Cesión o licencia de obras, software o marcas | TRLPI 43; Ley 17/2001, art. 48 |
| `encargo-tratamiento-datos` | Un proveedor trata datos personales por cuenta del cliente | RGPD 28 |
| `requerimiento-cumplimiento` | Hay que requerir el pago o el cumplimiento, o constituir en mora | CC 1100 |
| `resolucion-por-incumplimiento` | El cliente quiere resolver por incumplimiento | CC 1124 |
| `vicios-ocultos-saneamiento` | Defectos en lo comprado o construido | CC 1484 y 1490; CCom 336 y 342 |
| `reclamacion-deuda-monitorio` | Deuda dineraria documentada impagada | LEC 812 |
| `masc-propuesta-acuerdo` | Negociación previa obligatoria antes de demandar | LO 1/2025, arts. 5 y 7 |

Si el caso encaja en varias filas, anótalas por orden de urgencia y deriva primero a la que tenga un plazo corriendo.

## Documento que se entrega

**Ficha del encargo en Word** (maquetación de `references/formato-y-entrega-contratos.md`, apartado 2, adaptada a documento interno: sin REUNIDOS ni firmas). Nombre: `ficha-encargo-<tipo>-<parte-principal>-<AAAAMMDD>.docx`. Es interna del despacho y no es un contrato. Orden:

1. **Cabecera**: «FICHA DEL ENCARGO — CONTRATOS», fecha, abogado responsable, referencia interna.
2. **Alerta de urgencia** (solo si hay rojo o naranja): una línea por urgencia con nivel, hecho, precepto y fecha límite.
3. **Encargo**: tipo (tabla de clasificación) y objetivo del cliente con sus palabras.
4. **Partes**: tabla parte · posición · sociedad o persona física · quién firma y con qué título · resultado de `buscar_empresa_mercantil` (estado, cargos, último acto) · pendiente. Marcadores para lo no facilitado.
5. **Contrato**: tipo, objeto, cuantía, duración, fechas clave y documentos recibidos.
6. **Consumo y condiciones generales**: calificación y precepto leído.
7. **Ley aplicable**: norma y precepto; si hay Derecho civil propio, identificador BOE y advertencia de vigencia.
8. **Plazos**: tabla hecho · fecha inicial · precepto · naturaleza · fecha final · responsable; debajo, el criterio jurisprudencial leído sobre la calificación y la naturaleza de esos plazos (párrafo literal de la Sala, órgano, fecha, número y ECLI tal como los devolvió `leer_sentencias`).
9. **Derivación**: tabla skill · por qué · dato que falta · precepto ancla leído.
10. **Preceptos no disponibles**: los que el conector no devolvió y de los que depende el caso.
11. **Datos y documentos pendientes**: contrato íntegro, poderes, nota simple, facturas, correos.
12. **Tributación y formalidades a comprobar**: sin importes.
13. **Normativa consultada**: artículo, norma y «vigente desde» tal como los devolvió `buscar_articulo`.
14. **Próximo paso**: primera actuación y su fecha.

Cita en la ficha como indica el apartado 6 del formato: «artículo 1490 del Código Civil», «artículo 342 del Código de Comercio», «artículo 124 del Real Decreto Legislativo 1/2007», «artículo 18 de la Ley 38/1999, de 5 de noviembre, de Ordenación de la Edificación», «artículo 31 de la Ley 12/1992, de 27 de mayo, sobre Contrato de Agencia», «artículo 7 de la Ley Orgánica 1/2025», «artículo 59 del Estatuto de los Trabajadores», «artículo 1 del Real Decreto 1438/1985, de 1 de agosto». Todas estas formas las reconoce `verificar_escrito`; «del texto refundido de la Ley del Estatuto de los Trabajadores» no la reconoce. Cada artículo lleva su norma aunque se repita.

Si en el entorno no se pueden crear archivos, entrega el texto completo con esos títulos y avisa de que hay que pasarlo a Word.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió antes de empezar y ninguna consulta imprescindible quedó sin resultado.
- [ ] Las tres preguntas de urgencia se hicieron primero y el semáforo está aplicado.
- [ ] Cada precepto de la ficha se leyó con `buscar_articulo` en esta conversación, con su «vigente desde»; en los artículos con nota «Téngase en cuenta», se tomó el texto vigente y no el entrecomillado anterior.
- [ ] Cada plazo tiene fecha inicial, precepto, naturaleza y fecha final; ninguno se calculó sin fecha inicial.
- [ ] Cada sociedad se consultó con `buscar_empresa_mercantil`; la etiqueta «Activa» se contrastó con la fecha del último acto y se anotó el Registro Público Concursal si hay dudas.
- [ ] Ley aplicable anotada con su precepto; si hay Derecho civil propio o un reglamento de la Unión, con las advertencias de esta skill.
- [ ] Ningún ECLI en la ficha que no se haya leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] Marcadores en todos los datos no facilitados; ningún dato inventado ni búsqueda por el nombre de un particular.
- [ ] `verificar_escrito` pasado sobre el texto de la ficha; cada aviso revisado uno a uno.
- [ ] Resumen en el chat según el apartado 10 del formato: qué se ha preparado, urgencias y fechas límite con su precepto, datos y documentos que faltan, tabla de jurisprudencia (si se citó) y la skill a la que se deriva como próximo paso.
