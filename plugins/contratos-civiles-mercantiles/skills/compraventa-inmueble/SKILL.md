---
name: compraventa-inmueble
description: >-
  Redacta la compraventa de un inmueble en documento privado o la minuta para la escritura, con su nota
  para el abogado, en Word. Úsala cuando el abogado diga «compraventa de piso», «contrato privado de
  compraventa», «minuta para el notario», «vender con la hipoteca pendiente», «vivienda con inquilino»,
  «compra sobre plano» o «venta de local o solar». Identifica la finca en Registro y Catastro, cargas y
  su cancelación, arrendatarios y adquisición preferente, situación urbanística, certificado energético,
  información de la Ley 12/2023, deudas de comunidad, pago sin efectivo, saneamiento por evicción y
  vicios, gastos y tributos que hay que comprobar, y garantías de las entregas a cuenta en obra nueva,
  según defienda al comprador o al vendedor. Si solo se entrega una señal previa, usa contrato-arras;
  para reclamar vicios ya aparecidos, vicios-ocultos-saneamiento.
---

# Compraventa de inmueble

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Compraventa, entrega, cabida, precio, forma y consentimiento del cónyuge** → `buscar_articulo` (`ley="CC"`, artículos `"1445"`, `"1450"`, `"1455"`, `"1461"`, `"1462"`, `"1466"`, `"1468"`, `"1469"`, `"1471"`, `"1473"`, `"1500"`, `"1501"`, `"1502"`, `"1504"`, `"1279"`, `"1280"`, `"1320"` y `"1377"`).
- **Saneamiento, resolución y prescripción** → `buscar_articulo` (`ley="CC"`, artículos `"1474"`, `"1475"`, `"1476"`, `"1477"`, `"1478"`, `"1483"`, `"1484"`, `"1485"`, `"1486"`, `"1490"`, `"1101"`, `"1124"` y `"1964"`).
- **Registro, comunidad, arrendatarios, urbanismo e información previa** → `buscar_articulo` (`ley="BOE-A-1946-2453"`, artículos `"32"`, `"34"` y `"254"`), (`ley="Ley 49/1960"`, `articulo="9"`), (`ley="LAU"`, artículos `"14"` y `"25"` para vivienda; `"29"` y `"31"` para local), (`ley="BOE-A-2015-11723"`, `articulo="27"`) y (`ley="Ley 12/2023"`, `articulo="31"`).
- **Catastro, certificado energético, IBI, plusvalía y pagos** → `consultar_catastro` y `buscar_articulo` (`ley="Real Decreto Legislativo 1/2004"`, artículos `"38"`, `"40"` y `"41"`), (`ley="BOE-A-2021-9176"`, artículos `"3"`, `"13"` y `"17"`), (`ley="BOE-A-2004-4214"`, artículos `"64"` y `"106"`), (`ley="BOE-A-2012-13416"`, `articulo="7"`) y (`ley="LGT"`, `articulo="17"`).
- **Obra nueva, sobre plano y consumidores** → `buscar_articulo` (`ley="BOE-A-1999-21567"`, artículos `"17"`, `"18"` y `"19"`), (`ley="Ley 57/1968"`, artículos `"1"` y `"2"`, con la advertencia del apartado «Compra sobre plano») y (`ley="TRLGDCU"`, artículos `"3"`, `"4"`, `"82"`, `"83"`, `"85"`, `"87"`, `"89"` y `"90"`).
- **Doctrina sobre cabida, cargas, aliud pro alio, información urbanística, cantidades anticipadas y abusividad** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; `base="AN"` + `tipo_organo="AP"` si no hay doctrina del Supremo o el asunto se litigará en esa plaza) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil`; **tributos de la operación (IVA, ITP, AJD, plusvalía, IRPF)** → `buscar_consultas_hacienda` y `buscar_doctrina_teac` para la doctrina, sin tipos ni importes no leídos en una norma.
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Formas que reconoce `verificar_escrito`: «artículo 34 de la Ley Hipotecaria», «artículo 27 del Real Decreto Legislativo 7/2015, de 30 de octubre», «artículo 64 del Real Decreto Legislativo 2/2004, de 5 de marzo», «artículo 38 del Real Decreto Legislativo 1/2004, de 5 de marzo», «artículo 17 del Real Decreto 390/2021, de 1 de junio», «artículo 7 de la Ley 7/2012, de 29 de octubre», «artículo 17 de la Ley 38/1999, de 5 de noviembre, de Ordenación de la Edificación» y «artículo 89 del Real Decreto Legislativo 1/2007». En los documentos no uses la sigla «LOE»: `verificar_escrito` la lee como Ley Orgánica de Educación; escribe siempre «Ley 38/1999, de 5 de noviembre, de Ordenación de la Edificación».

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Compraventa de vivienda, local, garaje, trastero, nave, solar o finca rústica en documento privado (con precio pagado, aplazado o pendiente de escritura).
- Minuta de compraventa para remitir al notario, con las estipulaciones que el cliente quiere ver en la escritura.
- Compra de vivienda en construcción o sobre plano con entregas a cuenta al promotor.

Pasa este detector antes de redactar. Si encaja otra skill, díselo al abogado y deriva:

| Situación | Skill que procede |
|---|---|
| Solo se entrega una señal y la compraventa se firmará más tarde | `contrato-arras` |
| Vende una sociedad y hay dudas sobre poderes, concurso o disolución; o vende un menor, un incapacitado o una herencia yacente | `verificacion-partes-contrato` antes de esta skill |
| Se transmiten las participaciones de la sociedad propietaria, no el inmueble | `compraventa-participaciones` |
| El promotor usa un modelo de contrato para todos los compradores consumidores | esta skill para la operación y `condiciones-generales-consumidores` para auditar el modelo |
| Borrador de la otra parte o del promotor | `revision-contrato-semaforo` o `negociacion-contrapropuesta` |
| Tras la entrega aparecen defectos, cargas ocultas o menor cabida | `vicios-ocultos-saneamiento` o `resolucion-por-incumplimiento` |
| El comprador no paga el precio aplazado | `requerimiento-cumplimiento`, `resolucion-por-incumplimiento` o `reclamacion-deuda-monitorio` |
| Compra con precio aplazado garantizado con préstamo del vendedor o reconocimiento de deuda | esta skill y `prestamo-reconocimiento-deuda` para el aplazamiento |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ A quién defiende el abogado (comprador o vendedor) y si el vendedor actúa como empresario (promotor, sociedad inmobiliaria) frente a un comprador consumidor.
2. ★ Documento: contrato privado, minuta para escritura o ambos.
3. ★ Partes: nombre, DNI/NIE, domicilio, estado civil y régimen económico; si el inmueble es vivienda habitual de la familia del vendedor; residencia fiscal (si el vendedor no reside en España, hay que comprobar retenciones y el sustituto de la plusvalía). Sociedades: denominación, CIF, firmante y cargo o poder.
4. ★ **Nota simple** reciente (titular, descripción, cargas, arrendamientos inscritos, afecciones fiscales, prohibiciones de disponer) y título de adquisición del vendedor. El conector no consulta el Registro: sin nota simple, redacta con `[DATOS REGISTRALES]` y advierte en la nota y en el resumen que no debe firmarse sin contrastarla.
5. ★ Dirección o referencia catastral para `consultar_catastro` (en obra nueva sin división horizontal, la de la parcela).
6. ★ Precio, forma de pago (arras previas a descontar, pago en la firma, aplazamiento), cuentas, financiación hipotecaria del comprador y cargas que se cancelan con el precio.
7. ★ Ocupación: libre, arrendada (tipo, fecha, renuncia al derecho de adquisición preferente, notificación hecha o pendiente) u ocupada sin título.
8. ★ Si es obra nueva o sobre plano: licencia, fecha prevista de entrega, cantidades a cuenta, entidad receptora y garantía (aval o seguro) de cada entrega.
9. Comunidad: cuotas, deudas, derramas aprobadas, obras acordadas; certificado del secretario.
10. Situación urbanística conocida: fuera de ordenación, expedientes de disciplina, obras sin licencia, vivienda protegida, protección arquitectónica.
11. Certificado de eficiencia energética registrado y su fecha, cédula o certificado de habitabilidad si la comunidad autónoma lo exige, último recibo del IBI.
12. Si aplica un Derecho civil propio (Cataluña, Navarra, Aragón, País Vasco, Galicia, Baleares) o derechos de adquisición preferente autonómicos sobre viviendas.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la línea «vigente desde» y las notas «Téngase en cuenta».

**Perfección, forma y entrega.**

- La venta se perfecciona con el acuerdo en cosa y precio (art. 1450 CC); el documento privado obliga, pero para inscribir hace falta escritura (art. 1280.1 CC) y las partes pueden compelerse a otorgarla (art. 1279 CC).
- La escritura equivale a la entrega salvo que resulte lo contrario (art. 1462 CC): si la posesión se entrega otro día, dilo. El vendedor no está obligado a entregar si no se le paga ni se fijó plazo (art. 1466 CC).
- Cabida: con precio por unidad de medida rige el art. 1469 CC; con precio alzado, «como cuerpo cierto», no hay ajuste de precio por mayor o menor cabida (art. 1471 CC). Si defiendes al vendedor, vende como cuerpo cierto; si al comprador y la superficie es determinante, fija precio por metro o garantía de superficie útil mínima con consecuencia pactada.
- Precio aplazado: en inmuebles, el comprador puede pagar mientras no se le requiera judicialmente o por acta notarial aunque se haya pactado resolución automática (art. 1504 CC). Pro vendedor: condición resolutoria explícita con requerimiento notarial y garantía (hipoteca, aval); pro comprador: plazo de gracia y consignación.
- Intereses: el comprador los debe entre la entrega y el pago en los casos del art. 1501 CC; puede suspender el pago si es perturbado o teme fundadamente serlo (art. 1502 CC).
- Doble venta (art. 1473 CC) y tercero hipotecario (art. 34 de la Ley Hipotecaria): el comprador protegido es el que inscribe primero de buena fe. Si defiendes al comprador en un contrato privado con pago relevante, pacta escritura en plazo corto y nota simple de última hora.
- Vivienda familiar: consentimiento de ambos cónyuges aunque la vivienda sea privativa (art. 1320 CC); en bienes gananciales, el de ambos (art. 1377 CC).

**Saneamiento.**

- Evicción (arts. 1474 a 1478 CC): responde el vendedor si el comprador es privado del bien por sentencia firme en virtud de un derecho anterior. Es nulo el pacto que exima al vendedor de mala fe (art. 1476 CC); la renuncia del comprador solo le priva de todo si la hizo conociendo el riesgo (art. 1477 CC).
- Cargas no aparentes no mencionadas (art. 1483 CC): rescisión o indemnización durante un año desde la escritura; después, indemnización en un año desde que se descubren. Declara en el contrato todas las servidumbres y cargas conocidas.
- Vicios ocultos (arts. 1484 a 1486 CC): desistir o rebajar el precio, más daños si el vendedor los conocía. Las acciones caducan a los seis meses desde la entrega (art. 1490 CC). La exoneración pactada no vale si el vendedor conocía el vicio (art. 1485 CC). Pro vendedor: venta en el estado actual, conocido y aceptado, con informe técnico anexo y exclusión del saneamiento por vicios desconocidos; pro comprador: declaraciones concretas del vendedor (humedades, estructura, instalaciones, licencias) cuya falsedad dé lugar a resolución o indemnización, y plazo contractual de reclamación más largo.
- Si el defecto frustra el fin del contrato (vivienda no legalizable, sin licencia de primera ocupación, orden de demolición), la jurisprudencia admite la resolución por incumplimiento (aliud pro alio, arts. 1124 y 1101 CC), sujeta a la prescripción del art. 1964 CC y no a los seis meses.
- Obra nueva: además del contrato, los agentes de la edificación responden durante diez, tres y un año según el daño (art. 17 LOE); la acción prescribe a los dos años desde que se produce el daño (art. 18 LOE); garantías del art. 19 LOE. La renuncia al saneamiento en la escritura no alcanza la responsabilidad del proceso constructivo: búscalo (apartado siguiente).

**Registro, urbanismo, comunidad y ocupación.**

- Situación urbanística (art. 27 del Real Decreto Legislativo 7/2015): en las enajenaciones debe constar en el título la situación de los terrenos que no admitan uso o edificación, las edificaciones fuera de ordenación, las viviendas con precio tasado y los deberes pendientes; su infracción permite al adquirente rescindir en cuatro años. La jurisprudencia añade la anulación por dolo omisivo cuando se calla la situación real. Incluye la declaración del vendedor y, si hay duda, cédula urbanística.
- Comunidad (art. 9.1.e LPH): el inmueble responde de las deudas de la anualidad en curso y de los tres años anteriores; en la escritura el vendedor declara estar al corriente y aporta la certificación, salvo exoneración expresa del comprador. Pro comprador: nunca exoneres; pacta retención del precio.
- IBI (art. 64 del Real Decreto Legislativo 2/2004): el inmueble queda afecto al pago de la cuota. Pacta quién paga el IBI del año de la venta y si se prorratea; si hay controversia, busca doctrina con `consulta="repercusión IBI prorrateo compraventa vendedor comprador"`.
- Arrendatario de vivienda: tanteo de 30 días naturales desde la notificación fehaciente de la decisión de vender, precio y condiciones; los efectos de esa notificación caducan a los 180 días naturales; retracto si falta la notificación, si se omite algún requisito o si el precio efectivo resulta inferior o las condiciones menos onerosas que las notificadas, y caduca a los 30 días naturales desde que el adquirente notifica la venta con copia de la escritura; para inscribir hay que justificar las notificaciones o declarar en la escritura que la vivienda no está arrendada (art. 25 LAU). Si se firma el contrato privado antes de que venza el tanteo, sujétalo a la condición suspensiva de que el arrendatario no lo ejercite, mantén el precio y las condiciones notificados (ninguna más favorable para el comprador sin nueva notificación) y obliga al comprador a notificar la escritura al arrendatario. No hay tanteo ni retracto en la venta conjunta del art. 25.7 LAU; la renuncia pactada (art. 25.8 LAU) exige comunicar la intención de vender con 30 días de antelación. El comprador se subroga en el arrendamiento con el alcance del art. 14 LAU (plazos mínimos de cinco o siete años aunque sea tercero hipotecario). Local: arts. 29 y 31 LAU.
- Información mínima (art. 31 de la Ley 12/2023): el comprador de vivienda puede pedirla antes de entregar cualquier cantidad (identificación registral y cargas, cuota, superficies, certificado energético, antigüedad, accesibilidad, ocupación, protección oficial o arquitectónica, amianto a petición). Anéxala o deja constancia de su entrega.
- Certificado de eficiencia energética (arts. 3 y 17 del Real Decreto 390/2021): en la venta de un edificio existente o parte de él se anexa copia del certificado registrado y la etiqueta; validez del art. 13. Comprueba la nota «Téngase en cuenta» del art. 3: la redacción cambió en 2026.
- Catastro (arts. 38, 40 y 41 del Real Decreto Legislativo 1/2004): la referencia catastral debe constar y se acredita con los documentos del art. 41. Consulta con `consultar_catastro` y compara superficie, uso y año de construcción con la nota simple: si no coinciden, dilo en la nota (posible falta de declaración de obra nueva o ampliación sin legalizar). País Vasco y Navarra: catastro foral fuera del conector; búscalo en internet en la sede electrónica foral (o toma la certificación que aporte el abogado) y cítalo con enlace y fecha de consulta.
- Registro (art. 254 de la Ley Hipotecaria): no se inscribe sin NIF de todos los comparecientes, sin identificar los medios de pago ni sin acreditar la presentación de la plusvalía. Recoge en la minuta los medios de pago con detalle.
- Pagos en efectivo (art. 7 de la Ley 7/2012): con una parte empresaria o profesional, no se paga en efectivo por encima del umbral que devuelva la consulta.

**Compra sobre plano.**

- `buscar_articulo` con `ley="Ley 57/1968"` devuelve esa ley como vigente, pero la jurisprudencia de Audiencias recoge que la Ley 20/2015 la derogó y trasladó el régimen a la disposición adicional primera de la LOE, y la nota del art. 19 LOE sitúa esa reforma el 1 de enero de 2016. `buscar_articulo` no devuelve la disposición adicional primera y `leer_boe` (`identificador="BOE-A-1999-21567"`) da su redacción de 1999.
- Para contratos anteriores a esa fecha aplica la Ley 57/1968 y su abundante jurisprudencia. Para los posteriores, busca `consulta="disposición adicional primera Ley de Ordenación de la Edificación cantidades anticipadas garantía"` y `consulta="Ley 20/2015 derogó Ley 57/1968 cantidades anticipadas"` (`base="AN"`, `tipo_organo="AP"`) y cita el régimen vigente mediante el párrafo literal que lo transcriba o, si no lo encuentras, léelo en internet en el texto consolidado de la Ley 38/1999 en el BOE y cítalo con enlace y fecha de consulta.
- En todo caso, el contrato identifica la garantía (aval o seguro) de cada entrega, la entidad y la cuenta especial, y el comprador no entrega nada sin el documento de garantía individual. En la redacción vigente de la disposición adicional primera, el seguro de caución es una póliza individual por adquirente que identifica el inmueble: una póliza colectiva con certificados no se ajusta a ella; dilo en la nota si la promotora solo tiene la colectiva. La Sala Primera extiende la responsabilidad del banco receptor de los anticipos: búscala (apartado siguiente) y comprueba si la sentencia aplica la Ley 57/1968 (contratos anteriores a 2016) antes de trasladarla a un contrato posterior.

**Consumidores y tributos.**

- Vendedor empresario y comprador consumidor: son abusivas las cláusulas del art. 89.3 TRLGDCU (gastos de preparación de la titulación del promotor, subrogación forzosa en su hipoteca, tributos cuyo sujeto pasivo es el empresario, acometidas de suministros) y las de falta de reciprocidad del art. 87; la cláusula abusiva es nula y se tiene por no puesta (art. 83).
- Plusvalía municipal: en la venta, el sujeto pasivo es el transmitente, con el comprador como sustituto si el vendedor persona física no reside en España (art. 106 del Real Decreto Legislativo 2/2004). Trasladarla al comprador consumidor desde un empresario es abusivo (art. 89.3.c TRLGDCU); entre particulares el pacto vale entre ellos, pero no altera la obligación frente a la Administración (art. 17.5 LGT).
- IVA o ITP y AJD, IRPF o Impuesto sobre Sociedades del vendedor, retenciones a no residentes: avisa de qué comprobar según vendedor, inmueble (primera o segunda entrega, terreno, vivienda) y comprador; usa `buscar_consultas_hacienda` y `buscar_doctrina_teac` para la doctrina y no des tipos ni importes que no leas en una norma con `buscar_articulo`. Los aranceles de notaría y Registro no se calculan: remite a la fuente oficial. Si una consulta tributaria no responde, búscala en internet en la base oficial de la Dirección General de Tributos y cítala con enlace.
- Derecho civil propio o derechos de adquisición preferente autonómicos sobre viviendas: busca la norma con `buscar_boe`; si no aparece o `buscar_articulo` no devuelve el precepto (numeración con guion), léelo en internet en el texto consolidado oficial y cítalo con enlace y fecha de consulta.

## Cláusulas clave y jurisprudencia

Busca con `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"` salvo indicación), lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y comprueba que es razonamiento de la Sala, no alegación de parte. Con comprador consumidor y cláusulas predispuestas, la abusividad es jurisprudencia imprescindible (apartado 8 del formato): si tras dos reformulaciones no hay resolución aplicable, sigue el punto 3 de la puerta.

1. **Cuerpo cierto y cabida.** `consulta="venta a cuerpo cierto precio alzado menor cabida artículo 1471"`. Pro vendedor: «se vende como cuerpo cierto, por precio alzado, con independencia de su cabida real». Pro comprador: superficie útil mínima garantizada y rebaja proporcional o resolución si falta más de un porcentaje pactado.
2. **Cargas y servidumbres.** `consulta="cargas no aparentes artículo 1483 compraventa inmueble"`. Declaración exhaustiva del vendedor; cancelación registral a su costa con retención del precio y plazo para aportar la carta de pago y la escritura de cancelación.
3. **Situación urbanística y licencias.** `consulta="deber de información situación urbanística dolo omisivo compraventa"` y `consulta="aliud pro alio vivienda licencia de primera ocupación resolución compraventa"`. Pro comprador: declaración de legalidad de las obras y de inexistencia de expedientes, con resolución y devolución si resultan falsas. Pro vendedor: describe las irregularidades conocidas y que el comprador las acepta.
4. **Vicios ocultos y renuncia al saneamiento.** `consulta="vicios ocultos compraventa vivienda plazo seis meses artículo 1490 caducidad"` y `consulta="renuncia saneamiento vicios ocultos escritura ruina alcance"`. Redacta la renuncia citando los artículos a que se extiende (la jurisprudencia la interpreta de forma estricta) y excluye expresamente el dolo.
5. **Plusvalía y gastos con consumidor.** `consulta="plusvalía municipal comprador consumidor promotor cláusula abusiva"`. Si defiendes al promotor, deja cada tributo y gasto en quien la ley designa aunque el cliente pida trasladarlos (explícale que la cláusula sería nula y restituible); si defiendes al consumidor, señala en la nota las cláusulas nulas.
6. **Cantidades anticipadas.** `consulta="cantidades anticipadas vivienda sobre plano responsabilidad entidad de crédito cuenta especial"`, con `anios=6`. Úsala para exigir cuenta especial, garantía individual y plazo de entrega con consecuencia resolutoria.
7. **Retracto y venta conjunta.** Si hay arrendatario y se venden varias viviendas: `consulta="retracto arrendatario artículo 25.7 venta conjunta excepciones"`. Documenta si la operación encaja o no en la excepción.
8. **Negociación previa y fuero.** Si el abogado quiere prever cómo se resolverán las disputas, lee `buscar_articulo` (`ley="LO 1/2025"`, `articulo="5"`) y (`ley="Ley 60/2003"`, `articulo="9"`) y remite a `masc-propuesta-acuerdo` para el procedimiento; con consumidor, no pactes arbitraje distinto del de consumo ni fuero distinto de los que permite el art. 90 TRLGDCU.
9. **Cláusula penal con consumidor (retención de lo pagado a cuenta).** `consulta="cláusula penal abusiva consumidor nulidad no moderación"` (`base="TS"`) y arts. 85.6 y 87 TRLGDCU. Es jurisprudencia imprescindible (apartado 8 del formato). La pena que permite al promotor quedarse con todo o con una parte desproporcionada de lo entregado es abusiva, nula y no se modera (art. 83 TRLGDCU). Pro promotor: pena cerrada y proporcionada a daños que pueda acreditar, devolución del resto en plazo y pena recíproca si incumple él.

## Documentos que se entregan

Dos documentos en Word, según `references/formato-y-entrega-contratos.md`:

1. `contrato-compraventa-inmueble-<apellido-o-denominación-del-cliente>-<AAAAMMDD>.docx` (si es minuta: `contrato-compraventa-inmueble-minuta-...`).
2. `nota-compraventa-inmueble-<apellido-o-denominación-del-cliente>-<AAAAMMDD>.docx`

**Estructura del contrato privado** (una definición por término: «el Inmueble», «el Precio», «la Escritura»):

- «CONTRATO PRIVADO DE COMPRAVENTA DE [VIVIENDA / LOCAL / FINCA]», lugar y fecha.
- **REUNIDOS** e **INTERVIENEN** (cónyuges si procede; sociedades con su cargo o poder).
- **EXPONEN**: I. Titularidad y título de adquisición. II. Descripción, datos registrales `[DATOS REGISTRALES]`, referencia catastral `[REFERENCIA CATASTRAL]` y resultado del Catastro. III. Cargas según nota simple de `[FECHA]`. IV. Ocupación y, si hay arrendatario, notificaciones del art. 25 LAU. V. Situación urbanística. VI. Comunidad y certificado de deudas. VII. Certificado energético e información del art. 31 de la Ley 12/2023 entregados. VIII. Arras previas, si las hubo.
- **ESTIPULACIONES**: PRIMERA.- Objeto (cuerpo cierto o precio por unidad). SEGUNDA.- Precio y pago (medios, cuentas, retenciones, aplazamiento y su garantía o condición resolutoria). TERCERA.- Cargas y su cancelación. CUARTA.- Escritura (plazo, notario, documentos). QUINTA.- Entrega de la posesión y estado. SEXTA.- Declaraciones y garantías del vendedor. SÉPTIMA.- Saneamiento (alcance, renuncias y plazos). OCTAVA.- Gastos y tributos. NOVENA.- Arrendatarios y ocupantes. DÉCIMA.- Incumplimiento y resolución (con cláusula penal si se pacta). UNDÉCIMA.- Notificaciones, datos, ley aplicable y fuero.
- Firmas en dos columnas y **ANEXOS**: nota simple, consulta al Catastro, certificado energético y etiqueta, información del art. 31, certificado de la comunidad, plano, inventario de muebles.

**Reparto para la redacción rápida:** una sección por bloque de estipulaciones (`### [ESTIPULACION]`): comparecencia y expositivos (titularidad, cargas, ocupación, situación urbanística, comunidad) / objeto, precio y pago, cargas y escritura / posesión, declaraciones del vendedor y saneamiento / gastos y tributos, arrendatarios, incumplimiento y resolución / notificaciones, ley, fuero, firmas y anexos. La minuta, si se pide, es otro Word con su propia mesa de trabajo y el mismo reparto en formato notarial. La nota: apartado 11 del formato.

**Minuta para la escritura**: mismo contenido en formato notarial (comparecencia, intervención, exposición con descripción registral y catastral, estipulaciones), con la identificación completa de los medios de pago y las advertencias que debe recoger el notario marcadas entre corchetes para su revisión. Sin jurisprudencia.

**Nota para el abogado** (2-5 páginas): régimen aplicable y artículos leídos; cláusulas críticas con su fundamento y, cuando dependan de la jurisprudencia, el párrafo literal con órgano, fecha y ECLI; contraste entre Registro, Catastro y realidad; pendientes (nota simple, certificados, notificación al arrendatario, garantías de las entregas a cuenta); riesgos y alternativas; tributos y formalidades que hay que comprobar.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos usados (CC, Ley Hipotecaria, LPH, LAU, Real Decreto Legislativo 7/2015, Ley 12/2023, Real Decreto Legislativo 1/2004, Real Decreto 390/2021, Real Decreto Legislativo 2/2004, Ley 7/2012, LOE y TRLGDCU si hay consumidor), con su vigencia y sus notas «Téngase en cuenta».
- [ ] Inmueble consultado con `consultar_catastro` (o catastro foral consultado en internet con enlace) y contrastado con la nota simple; discrepancias en la nota.
- [ ] Si hay arrendatario: notificación del tanteo o renuncia y su comunicación, con fechas y plazo de 30 días naturales calculado.
- [ ] Si es sobre plano: régimen de las cantidades anticipadas según la fecha del contrato, con la disposición adicional primera de la LOE leída en un párrafo de Jurisprudenciator o en el BOE consolidado (enlace y fecha).
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; ninguno en el contrato ni en la minuta.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); cada «posible disonancia» contrastada con el artículo leído.
- [ ] Marcadores en lugar de datos inventados; precio, cuentas, fechas y definiciones coherentes en todos los documentos.
- [ ] Ningún tipo impositivo, arancel ni umbral que no se haya leído en esta conversación.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas, pendientes y riesgos, tabla de jurisprudencia, plazos con su precepto (saneamiento, tanteo, escritura) y próximo paso.
