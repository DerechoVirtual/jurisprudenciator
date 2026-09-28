---
name: condiciones-generales-consumidores
description: >-
  Redacta o audita condiciones generales de la contratación y contratos con consumidores: términos y
  condiciones de tienda online, web de servicios, suscripciones o apps y condicionados de adhesión en
  papel. Aplica el control de incorporación (Ley 7/1998, arts. 5 y 7), la transparencia y la abusividad
  (TRLGDCU, arts. 80-91), la información previa y los contratos a distancia (arts. 60, 97 y 98), el
  desistimiento (arts. 102-108), la garantía (arts. 114 y ss.) y la Ley 34/2002. Úsala con «condiciones
  generales», «términos y condiciones de mi web», «¿es abusiva esta cláusula?». Contrato negociado entre
  empresas: revision-contrato-semaforo; borrador de la otra parte: negociacion-contrapropuesta.
---

# Condiciones generales y contratos con consumidores

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Ámbito, incorporación, interpretación y nulidad de las condiciones generales** → `buscar_articulo` (`ley="BOE-A-1998-8789"`, artículos `"1"`, `"2"`, `"4"`, `"5"`, `"6"`, `"7"`, `"8"` y `"10"`). Comprueba que el encabezado dice `BOE-A-1998-8789`: con «Ley 7/1998» sale otra ley.
- **Consumidor, cláusulas no negociadas y abusividad** → `buscar_articulo` (`ley="TRLGDCU"`, artículos `"3"`, `"10"`, `"59"`, `"62"`, `"65"`, `"67"`, `"80"` y del `"82"` al `"90"`); si hay adherentes empresarios, además (`ley="BOE-A-2004-21830"`, artículos `"4"`, `"7"`, `"8"` y `"9"`) y (`ley="CC"`, artículos `"1102"`, `"1255"` y `"1258"`).
- **Fuero y tribunal competente** → `buscar_articulo` (`ley="LEC"`, artículos `"52"` y `"54"`).
- **Entrega, retraso y riesgo** → `buscar_articulo` (`ley="TRLGDCU"`, artículos `"66 bis"` y `"66 ter"`).
- **Atención a la clientela y reclamaciones (todo empresario)** → `buscar_articulo` (`ley="TRLGDCU"`, `articulo="21"`) y (`ley="BOE-A-2017-12659"`, artículos `"40"` y `"41"`: información sobre entidades de resolución alternativa).
- **Información previa, contratación a distancia y electrónica, desistimiento** → `buscar_articulo` (`ley="TRLGDCU"`, artículos `"21"`, `"60"`, `"63"`, `"97"`, `"98"` y del `"101"` al `"108"`) y (`ley="Ley 34/2002"`, artículos `"10"`, `"23"`, `"24"`, `"27"`, `"28"` y `"29"`).
- **Garantía de conformidad de bienes y de contenidos o servicios digitales** → `buscar_articulo` (`ley="TRLGDCU"`, artículos `"114"`, `"115 bis"`, `"115 ter"`, del `"117"` al `"121"`, `"124"`, `"126"`, `"126 bis"` y `"127"`).
- **Doctrina sobre incorporación, transparencia y abusividad** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`; `base="TJUE"` para la Directiva 93/13; `base="AN"`, `jurisdiccion="CIVIL"`, `tipo_organo="AP"` si el Supremo no ha tratado el punto) + `leer_sentencias` (`parrafos=3`, `terminos` con la cláusula).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (el predisponente: denominación, domicilio y datos registrales que la web debe publicar).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). En los documentos, nombra las normas así (las reconoce `verificar_escrito`): «artículo 5 de la Ley 7/1998, de 13 de abril, sobre condiciones generales de la contratación», «artículo 80 del Real Decreto Legislativo 1/2007», «artículo 27 de la Ley 34/2002, de 11 de julio», «artículo 2 de la Ley 10/2025, de 26 de diciembre, por la que se regulan los servicios de atención a la clientela», «artículo 40 de la Ley 7/2017, de 2 de noviembre», «artículo 9 de la Ley 3/2004, de 29 de diciembre, por la que se establecen medidas de lucha contra la morosidad en las operaciones comerciales». Cada artículo con su norma: si enumeras artículos detrás de otra norma o escribes «apartado 2 del mismo artículo» después de nombrar otra ley, el verificador los atribuye a la última nombrada. El conector no devuelve el anexo I del Real Decreto Legislativo 1/2007 (modelos de información y de formulario de desistimiento): léelo en internet en el texto consolidado del BOE y cópialo literal con enlace y fecha de consulta, nunca de memoria (ver «Documentos que se entregan»).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

Tiene dos modos. Pregunta cuál y a quién defiende el abogado:

- **Redactar**: condiciones generales de una tienda online, de un servicio (formación, software, mantenimiento, gimnasio) o de una suscripción; formulario de pedido; condicionado de un contrato de adhesión en papel. El cliente es el predisponente.
- **Auditar**: condiciones ya publicadas o firmadas, del propio cliente (para corregirlas) o de un empresario frente al que el cliente es adherente (para saber qué cláusulas no le obligan).

Si encaja otra figura, dilo al abogado y deriva:

| Situación | Qué procede |
|---|---|
| Contrato negociado cláusula a cláusula entre empresas, sin adhesión | `revision-contrato-semaforo` o `negociacion-contrapropuesta` |
| Préstamo o crédito (consumo o hipotecario) | `prestamo-reconocimiento-deuda`: su norma sectorial prevalece en lo que regula (art. 59.2 TRLGDCU); aquí, solo el control general |
| Alquiler de vivienda con cláusulas predispuestas | `arrendamiento-vivienda` (LAU imperativa); esta skill, solo para la abusividad |
| Venta de vivienda por promotor a consumidor | `compraventa-inmueble`, con los gastos del art. 89.3 TRLGDCU |
| Política de privacidad o tratamiento de datos por cuenta del cliente | `encargo-tratamiento-datos` |
| Licencia de software o contenidos | `licencia-cesion-propiedad-intelectual` y, si el licenciatario es consumidor, también esta skill |
| Qué significa una cláusula ya firmada | `dictamen-interpretacion-contrato` |
| Reclamar por una cláusula ya aplicada | `requerimiento-cumplimiento`; la demanda de nulidad, plugin de litigación civil (`nulidad-clausulas-abusivas`) |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. Si falta un dato ★, pídelo antes de redactar o de auditar.

1. ★ Modo (redactar o auditar) y posición del cliente: predisponente o adherente.
2. ★ Predisponente: denominación, CIF, domicilio, inscripción registral, correo y teléfono de contacto; si ejerce una profesión regulada, colegio, número y título (art. 10 de la Ley 34/2002).
3. ★ Adherentes: consumidores, empresarios o ambos. Si hay ambos, separa el régimen o aplica a todos el de consumo. Pregunta si se dirige a personas consumidoras vulnerables (art. 3.2 TRLGDCU).
4. ★ Canal: web o app, teléfono, fuera del establecimiento o presencial. En línea, pide capturas del proceso de compra completo: dónde se muestran las condiciones, casilla o botón de aceptación, texto del botón de pago y correo de confirmación.
5. ★ Objeto: bienes nuevos o de segunda mano, a medida o perecederos, servicios, contenidos o servicios digitales, suscripción de tracto sucesivo; si el consumidor paga con datos personales (art. 59.4).
6. ★ Precio y pago: impuestos y gastos, precio personalizado por decisiones automatizadas, renovación automática, permanencia y penalizaciones, medios de pago, restricciones de entrega.
7. Plazo de entrega o de inicio del servicio, y si el servicio empieza durante el plazo de desistimiento.
8. Garantía comercial, servicio posventa, canal de reclamaciones, adhesión a arbitraje de consumo o a un código de conducta.
9. Tamaño de la empresa (plantilla, volumen de negocio, balance) y sector: decide si le alcanza la Ley 10/2025 de atención a la clientela.
10. Territorio: si vende a otros Estados o a consumidores de una comunidad con código de consumo propio, pregunta si hay que aplicarlo y búscalo con `buscar_boe`; si el conector no devuelve el precepto, léelo en internet en el boletín oficial de la comunidad y cítalo con enlace (punto 3 de la puerta).
11. Solo al auditar: texto íntegro y fecha de la versión, cómo se aceptó, si alguna cláusula se negoció (la prueba es del empresario, art. 82.2) y qué cláusula se discute.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su línea «vigente desde…». Los arts. 21, 62 y 97 TRLGDCU tienen redacción de la Ley 10/2025, vigente desde el 28/12/2025: no uses versiones anteriores.

**1. ¿Hay condiciones generales y quién es el adherente?**
- Condición general: cláusula predispuesta, impuesta por una parte y redactada para una pluralidad de contratos (art. 1 Ley 7/1998). La negociación de una cláusula aislada no excluye el resto si el contrato es de adhesión (art. 1.2). Quedan fuera los contratos administrativos, de trabajo, de constitución de sociedades, familiares y sucesorios (art. 4).
- Consumidor: persona física que actúa con un propósito ajeno a su actividad comercial, empresarial, oficio o profesión, y la persona jurídica sin ánimo de lucro que actúa fuera de una actividad comercial (art. 3.1 TRLGDCU). Con consumidor y condiciones generales se aplican las dos leyes (art. 59.3).
- **Adherente empresario**: solo control de incorporación (arts. 5 y 7 Ley 7/1998) y nulidad por contravenir una norma imperativa o prohibitiva (art. 8.1). Los controles de transparencia material y de abusividad son improcedentes; frente a una cláusula sorprendente cabe el control por buena fe del art. 1258 CC, de menor intensidad (busca la doctrina, consulta 6). Sí alcanzan a las condiciones entre empresas: la nulidad de la sumisión expresa a fuero en contratos de adhesión (art. 54.2 LEC); la nulidad de toda condición contraria a una norma imperativa (art. 8.1 Ley 7/1998), como la exclusión de la responsabilidad por dolo (art. 1102 CC); y, **solo cuando el adherente es el acreedor** (el proveedor que vende o presta servicios al predisponente y cobra de él), la nulidad de los pactos manifiestamente abusivos sobre fecha o plazo de pago, interés de demora o costes de cobro «en perjuicio del acreedor» y el plazo máximo de pago (arts. 9 y 4 de la Ley 3/2004, de 29 de diciembre). Si el adherente es quien paga, el art. 9 no le protege: rige el interés pactado (art. 7.1) con los límites generales (arts. 1255 y 1258 CC); no lo invoques a su favor.

**2. Incorporación (todo adherente).**
- Aceptación del adherente, referencia en el contrato, información expresa de su existencia y entrega de un ejemplar (art. 5.1); en contratos sin forma escrita con resguardo, anuncio visible o posibilidad efectiva de conocerlas al contratar (art. 5.3). Redacción transparente, clara, concreta y sencilla (art. 5.5).
- No se incorporan las que el adherente no tuvo oportunidad real de conocer de manera completa al contratar, las no firmadas cuando era necesario y las ilegibles, ambiguas, oscuras e incomprensibles (art. 7).
- En línea: condiciones disponibles antes de iniciar la contratación, de modo que puedan almacenarse y reproducirse (art. 27.4 Ley 34/2002); información sobre trámites, archivo del documento, corrección de errores y lenguas (art. 27.1); confirmación de la aceptación (art. 28). Con consumidores, copia con las condiciones aceptadas (art. 63.1 TRLGDCU).

**3. Transparencia (consumidores).** Concreción, claridad y sencillez con comprensión directa, sin reenvíos a documentos no facilitados; legibilidad, nunca con letra inferior a 2,5 mm, interlineado inferior a 1,15 mm o contraste insuficiente; buena fe y justo equilibrio (art. 80.1). Las condiciones incorporadas de modo no transparente en perjuicio del consumidor son nulas (art. 83, párrafo segundo). La transparencia material exige que el consumidor medio pueda conocer la carga económica y jurídica de la cláusula y alcanza al precio y al objeto principal: no te pronuncies sin la doctrina del TJUE y del Supremo (consulta 5).

**4. Abusividad (consumidores).**
- Estipulación no negociada que, contra la buena fe, causa un desequilibrio importante en perjuicio del consumidor (art. 82.1), valorada con las circunstancias del momento de contratar (art. 82.3). Son abusivas en todo caso las de los arts. 85 a 90 (art. 82.4): vinculación a la voluntad del empresario (prórroga automática con fecha límite que impide oponerse, modificación unilateral sin motivo válido especificado, resolución anticipada solo para el empresario, indemnización desproporcionadamente alta, fechas de entrega indicativas, subida de precio sin derecho a resolver), limitación de derechos (86), falta de reciprocidad (87), garantías y carga de la prueba (88), perfeccionamiento y ejecución (89) y competencia y ley aplicable (90).
- Tracto sucesivo: prohibidas la duración excesiva y las trabas a la baja; la baja se ejerce en la misma forma en que se contrató, sin cargas desproporcionadas; el contrato describe el procedimiento de baja; la penalización por incumplir la permanencia es proporcional a los días no cumplidos (art. 62.2 a 62.5).
- Efectos: nulidad de pleno derecho, se tiene por no puesta y el contrato subsiste si puede (art. 83); integración a favor del consumidor (art. 65); la renuncia previa a sus derechos es nula (art. 10). Los arts. 82 a 91 y 114 a 126 se aplican cualquiera que sea la ley elegida si hay vínculo estrecho con el Espacio Económico Europeo (art. 67).

**5. Interpretación.** Prevalecen las condiciones particulares salvo que las generales sean más beneficiosas; las dudas, a favor del adherente (art. 6 Ley 7/1998); con consumidores, en acciones individuales, la interpretación más favorable (art. 80.2 TRLGDCU).

**6. Información previa y contratos a distancia.**
- General: art. 60.2 (características, identidad, precio total, pago y entrega, garantía, duración y baja, permanencias y penalizaciones, desistimiento, reclamaciones); la prueba de haber informado es del empresario (art. 60.5).
- A distancia y fuera del establecimiento: lista entera del art. 97.1; entre otras, dirección, teléfono y correo electrónico —letra c)—, precio total por periodo de facturación en suscripciones —letra e)—, aviso de que el precio se ha personalizado y con qué parámetros —letra f)— y, en contratos que se renuevan, aviso quince días antes de que venza el plazo para oponerse a la renovación —letra p)—. Esa información forma parte del contrato (art. 97.5); si faltan los gastos adicionales o de devolución, el consumidor no los paga (art. 97.6).
- Suscripciones y tracto sucesivo: si el contrato es de duración determinada y se renueva, hay que avisar al consumidor quince días antes de que venza el plazo para no renovar (letra p), párrafo segundo); si es de duración indefinida con cargo periódico, basta informar de las condiciones de resolución. Configurar la suscripción como indefinida evita un aviso en cada renovación. La cuota de un contrato en curso solo puede subir con motivos válidos especificados, preaviso y derecho a resolver sin coste (arts. 85.3 y 85.10).
- Pedido en línea: información destacada justo antes del pedido y botón etiquetado solo «pedido con obligación de pago» o fórmula análoga no ambigua; si no, el consumidor no queda obligado (art. 98.2). Restricciones de entrega y medios de pago, al inicio del proceso (art. 98.3); confirmación en soporte duradero (art. 98.7); el silencio no es aceptación (art. 101).
- Atención al cliente, **para todo empresario**: medios de reclamación que incluyan, al menos, el medio por el que se contrató (en una tienda online, la propia web), la vía postal, la telefónica y un medio electrónico; respuesta en quince días como máximo (art. 21.3); clave identificativa y justificante, atención personal directa y teléfono sin coste superior a una llamada estándar (art. 21.2). Si no está adherido a una entidad de resolución alternativa, cuando no resuelva una reclamación debe informar de al menos una entidad competente y de si participará (art. 40.3 de la Ley 7/2017). El art. 40.5 de esa ley sigue remitiendo a la plataforma europea de resolución de litigios en línea del Reglamento (UE) 524/2013, derogado con efecto a partir del 20/07/2025: compruébalo en EUR-Lex (Reglamento (UE) 2024/3228, punto 3 de la puerta) y no incluyas ese enlace.
- Gran empresa o servicios básicos de interés general: comprueba además la Ley 10/2025 (`ley="BOE-A-2025-26698"`, artículos `"1"`, `"2"` y los de plazos y canales de atención); su art. 2.2 la aplica a las demás empresas solo si en el ejercicio anterior ocuparon al menos a 250 trabajadores o superaron 50 millones de volumen de negocios o 43 millones de balance.

**7. Desistimiento.** Catorce días naturales sin motivo, treinta en visitas no solicitadas o excursiones (art. 102); cómputo del art. 104; si no se informó, el plazo se alarga doce meses (art. 105); basta cualquier declaración inequívoca y cuenta la fecha de envío (art. 106); reembolso en catorce días naturales por el mismo medio de pago (art. 107); devolución en catorce días, costes a cargo del consumidor solo si se le informó (art. 108). Lee el art. 103 entero y recoge en las condiciones solo las excepciones que apliquen, con el consentimiento expreso que exijan; para servicios que empiezan dentro del plazo, arts. 98.8 y 108.4. En la entrega periódica de bienes (suscripciones), el plazo corre desde la recepción del primer envío (art. 104.b.3.º). La excepción de bienes precintados (art. 103.e) solo alcanza al bien que, desprecintado, ya no puede volver a venderse por razones de salud o higiene (consulta 7).

**8. Garantía.** Conformidad según arts. 115 bis y 115 ter; subsanación, rebaja o resolución, más indemnización (arts. 117 a 119); responsabilidad por faltas que se manifiesten en tres años (bienes) o dos (contenidos o servicios digitales de acto único), pactable hasta un mínimo de un año en segunda mano (art. 120); presunción de preexistencia de dos años y un año (art. 121); la acción prescribe a los cinco años de la manifestación (art. 124). Modificar contenidos o servicios digitales en curso exige los requisitos del art. 126 y da derecho a resolver (art. 126 bis). Garantía comercial: art. 127.

**9. Entrega y retraso.** Salvo pacto, entrega sin demora indebida y en treinta días naturales como máximo desde la celebración; si no se entrega, el consumidor emplaza un plazo adicional y, si tampoco se cumple, resuelve, o resuelve de inmediato si la fecha era esencial y se acordó antes de contratar (art. 66 bis). El riesgo pasa al consumidor cuando él o un tercero distinto del transportista recibe los bienes (art. 66 ter). Las fechas de entrega «meramente indicativas» son abusivas (art. 85.8).

**10. Fuero, arbitraje y ley.** Con consumidores son abusivos el arbitraje distinto del de consumo (salvo institucional sectorial), el fuero distinto del domicilio del consumidor, del lugar de cumplimiento o de situación del inmueble, y la ley extranjera en los casos del art. 90.3. En contratos de adhesión o con condiciones generales la sumisión expresa no es válida, tampoco entre empresas (art. 54.2 LEC): no pactes fuero. En las acciones individuales del consumidor, este elige el tribunal de su domicilio (art. 52.3 LEC), y la acción de no incorporación o de nulidad de condiciones generales se presenta en el domicilio del demandante (art. 52.1.14.º LEC). El contrato electrónico con consumidor se presume celebrado en su residencia habitual (art. 29 Ley 34/2002).

## Cláusulas clave y jurisprudencia

La jurisprudencia es imprescindible al auditar (el informe cita al menos una resolución) y en toda cláusula cuya validez depende de una ponderación (apartado 8 del formato): la cláusula general del art. 82.1 (desequilibrio importante contra la buena fe), la proporcionalidad o la duración (arts. 62.3, 85.6 y 87.6), la transparencia material y, frente a un adherente empresario, la buena fe del art. 1258 CC. Cuando la cláusula encaja literalmente en un supuesto que los arts. 85 a 90 declaran abusivo en todo caso (art. 82.4) o contradice una norma imperativa (art. 8.1 Ley 7/1998; por ejemplo, art. 1102 CC o art. 54.2 LEC), el artículo basta: busca doctrina y cítala si existe; si no la hay, dilo en el informe. Reformula cada consulta como máximo dos veces; lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar, y cita fundamentos de la Sala, nunca hechos ni partes de aquel pleito ni lo que dijeron la sentencia de instancia o una parte.

| Cláusula | Predisponente | Adherente o consumidor |
|---|---|---|
| Aceptación | Casilla no premarcada junto al enlace descargable; registro fechado de la versión aceptada; envío con la confirmación | Sin oportunidad real de conocerlas o sin ejemplar, no se incorporan (art. 7) |
| Renovación, permanencia y baja | Aviso previo a la renovación; baja por el mismo canal; penalización proporcional al tiempo restante | Penalización fija o por todo el periodo: desproporcionada (arts. 62.5, 85.6 y 87.6) |
| Modificación unilateral | Solo para contratos futuros o con motivos válidos especificados, preaviso y resolución sin coste | Sin motivo concreto ni derecho a resolver: abusiva (art. 85.3) |
| Responsabilidad y garantía | Limitar daños indirectos solo frente a empresarios; con consumidores, respetar arts. 86 y 114 y ss. | Exclusión de responsabilidad o recorte de la garantía: nulo |
| Precio y objeto principal | Precio total, desglose y ejemplo numérico si hay variables | Coste no comprensible al contratar: falta de transparencia material |
| Fuero y arbitraje | Sin pacto de sumisión; el consumidor puede demandar en su domicilio (art. 52.3 LEC); entre empresas, no pactes fuero en adhesión (art. 54.2 LEC) | Sumisión a otro fuero o arbitraje no de consumo: abusiva (art. 90); en adhesión, nula también entre empresas (art. 54.2 LEC) |
| Cierres, suspensiones o servicios no prestados | Rebaja proporcional de la cuota | Cobro por servicios no efectivamente prestados: abusivo (art. 87.5) |
| Resolución por el empresario | Solo por incumplimiento o, en contratos indefinidos, con preaviso razonable | Resolución discrecional sin la misma facultad para el consumidor: abusiva (arts. 85.4 y 87.3) |

Consultas (`jurisdiccion="CIVIL"` salvo en el TJUE):

1. Incorporación en línea: `consulta="condiciones generales no incorporación oportunidad real de conocer contratación electrónica"`, `base="AN"`, `tipo_organo="AP"`, `anios=3`.
2. Penalización por baja o desistimiento: `consulta="cláusula penal por denuncia unilateral del contrato consumidor abusividad indemnización desproporcionada"`, `base="TS"`.
3. Duración o prórrogas excesivas: `consulta="duración excesiva contrato de mantenimiento consumidor cláusula abusiva prórroga"`, `base="TS"`; para gimnasios, academias y suscripciones, `consulta="prórroga automática preaviso permanencia gimnasio cláusula abusiva"`, `base="AN"`, `tipo_organo="AP"`.
4. Modificación unilateral: `consulta="modificación unilateral de las condiciones motivos válidos consumidor cláusula abusiva"`, `base="TS"`.
5. Transparencia material del precio u objeto principal: `consulta="Directiva 93/13 redacción clara y comprensible artículo 4 apartado 2 objeto principal"`, `base="TJUE"`, y `consulta="control de transparencia material carga económica consumidor medio"`, `base="TS"`.
6. Adherente empresario: `consulta="condiciones generales entre profesionales buena fe cláusula sorprendente"`, `base="TS"`; incorporación entre empresas, `consulta="control de incorporación adherente no consumidor condiciones generales empresario"`, `base="TS"`; exclusión de responsabilidad, `consulta="cláusula de exoneración de responsabilidad dolo culpa grave nula artículo 1102"`, `base="TS"`.
7. Excepción de bienes precintados en el desistimiento: `consulta="derecho de desistimiento bienes precintados no aptos para ser devueltos por razones de protección de la salud o de higiene desprecintados"`, `base="TJUE"`.

Si para una cláusula de ponderación o de transparencia no aparece ninguna resolución aplicable tras dos reformulaciones, aplica el punto 3 de la puerta: búscala en internet, localízala con `buscar_por_cita`, léela con `leer_sentencias` y, si tampoco así aparece, detén la tarea. Para una cláusula de la lista de los arts. 85 a 90 o contraria a norma imperativa, la falta de doctrina no detiene la auditoría.

## Documentos que se entregan

**Al redactar** (dos documentos, según el formato):

1. `contrato-condiciones-generales-<predisponente>-<AAAAMMDD>.docx`. Título «CONDICIONES GENERALES DE CONTRATACIÓN», versión y fecha; sin REUNIDOS ni INTERVIENEN; cláusulas numeradas en este orden:
   1. Identificación del prestador y medios de contacto (art. 10 Ley 34/2002; art. 97.1.b a d TRLGDCU).
   2. Objeto, destinatarios (consumidores, empresarios) y definiciones: un término por concepto.
   3. Proceso de contratación: trámites, archivo, corrección de errores, lenguas y confirmación (arts. 27 y 28 Ley 34/2002).
   4. Productos o servicios, disponibilidad y restricciones de entrega.
   5. Precio, impuestos, gastos, personalización del precio si la hay, y medios de pago.
   6. Entrega o ejecución: plazos y consecuencias del retraso.
   7. Duración, renovación, permanencia y procedimiento de baja (tracto sucesivo).
   8. Desistimiento: plazo, cómputo, forma, reembolso, devolución, costes y excepciones aplicables.
   9. Garantía legal y, en su caso, garantía comercial.
   10. Atención al cliente, quejas y reclamaciones (canales y plazo del art. 21.3 TRLGDCU), resolución extrajudicial (art. 40 Ley 7/2017).
   11. Responsabilidad.
   12. Modificación de las condiciones (solo para contratos futuros, salvo arts. 85.3 y 126).
   13. Protección de datos: remisión a la política de privacidad (la redacta `encargo-tratamiento-datos` o el abogado).
   14. Ley aplicable y jurisdicción.
   - **Anexo**: modelo de formulario de desistimiento del anexo I, letra B, del Real Decreto Legislativo 1/2007, copiado literal del texto consolidado del BOE en internet (`https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555`), con la fecha de consulta en la nota; si no lo obtienes, deja el marcador `[MODELO DE FORMULARIO DE DESISTIMIENTO — ANEXO I, LETRA B]` y dilo en el resumen.
   - Legibilidad: advierte en la nota que los mínimos del art. 80.1.b) se miden en el soporte final (pantalla, papel) y que el diseñador debe comprobarlos.
2. `nota-condiciones-generales-<predisponente>-<AAAAMMDD>.docx` (apartado 3 del formato), con una lista de control del proceso de compra: condiciones accesibles y descargables antes de contratar, casilla no premarcada, información destacada y botón del art. 98.2, restricciones de entrega al inicio, confirmación en soporte duradero, formulario de desistimiento, y lo que la web debe publicar además (aviso legal del art. 10 Ley 34/2002 y política de privacidad).

**Al auditar**: `revision-condiciones-generales-<predisponente>-<AAAAMMDD>.docx` con el semáforo del apartado 4 del formato. En «Motivo y base legal», di qué control falla (incorporación, transparencia, abusividad o norma imperativa) con su artículo y, si la cláusula es de ponderación o de transparencia, el párrafo literal de la resolución; si es de la lista de los arts. 85 a 90 o contraria a norma imperativa, el artículo y, si existe, la resolución. Después: información obligatoria que falta (arts. 60 y 97 TRLGDCU; arts. 10 y 27 Ley 34/2002), defectos del proceso de compra y conclusión. Si el cliente es el predisponente, añade las cláusulas corregidas en limpio; si es el adherente, los efectos (no incorporada o nula, se tiene por no puesta, subsistencia del contrato), las cantidades que puede recuperar o que no debe, calculadas con sus fechas, y el paso siguiente: reclamación al empresario (respuesta en quince días, art. 21.3 TRLGDCU, si es consumidor), negociación previa a la demanda (art. 5 de la Ley Orgánica 1/2025, `ley="LO 1/2025"`), `requerimiento-cumplimiento` para el escrito y el plugin de litigación civil para la demanda, con el tribunal competente (art. 52 LEC).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos citados, con el encabezado `BOE-A-1998-8789` comprobado y la redacción de la Ley 10/2025 en los arts. 21, 62 y 97 TRLGDCU.
- [ ] Separado el régimen de empresarios y de consumidores: a un adherente empresario no se le aplica control de transparencia ni de abusividad, y el art. 9 de la Ley 3/2004 solo se invoca a favor del adherente que cobra.
- [ ] Entrega y retraso (arts. 66 bis y 66 ter), canales y plazo de reclamaciones (art. 21.3), resolución alternativa (art. 40 Ley 7/2017) y fuero (arts. 52 y 54 LEC) leídos y reflejados.
- [ ] Cada cláusula en ROJO o ÁMBAR dice qué control falla, con artículo y, si es de ponderación o de transparencia, jurisprudencia leída con `leer_sentencias` o comprobada con `buscar_por_cita`; el informe cita al menos una resolución.
- [ ] Información obligatoria completa, botón del art. 98.2 y formulario de desistimiento copiado del BOE con enlace y fecha (o su marcador), nunca de memoria; los datos sacados de internet, señalados en el resumen.
- [ ] Plazos con su precepto: 14 o 30 días (art. 102), 12 meses (art. 105), 14 días de reembolso y devolución (arts. 107 y 108), 3 o 2 años (art. 120), 2 o 1 año de presunción (art. 121), 5 años (art. 124).
- [ ] `verificar_escrito` pasado sobre cada documento; los avisos de «posible disonancia» contrastados con el apartado leído.
- [ ] Marcadores (`[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[DOMICILIO]`, `[IMPORTE]`) en vez de datos inventados; sin tipos de IVA ni importes no leídos en una norma.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado, cláusulas críticas, datos que faltan y riesgos, tabla de jurisprudencia y próximo paso.
