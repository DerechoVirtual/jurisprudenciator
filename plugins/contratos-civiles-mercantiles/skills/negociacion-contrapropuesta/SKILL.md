---
name: negociacion-contrapropuesta
description: >-
  Prepara la respuesta a un borrador de contrato que envía la otra parte: tabla Cláusula | Texto
  actual | Texto propuesto | Motivo, versión limpia de las cláusulas cambiadas, prioridades de
  negociación (imprescindible, deseable, cedible) con posiciones de repliegue en una nota interna, y
  carta o correo de remisión. Pregunta primero a quién defiende el abogado y qué margen tiene, y ajusta
  cada cambio a la posición del cliente. Úsala con «contrapropuesta», «contraoferta», «devuélveles el
  contrato con nuestros cambios», «qué les pedimos», «marca los cambios», «redline», «segunda
  vuelta del borrador». Si antes hay que diagnosticar los riesgos del borrador, empieza por
  revision-contrato-semaforo; para redactar desde cero, la skill de ese contrato; si se negocia para
  resolver un conflicto antes de demandar, masc-propuesta-acuerdo.
---

# Contrapropuesta a un borrador de la otra parte

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Perfección del contrato y valor de la contrapropuesta** → `buscar_articulo` (`ley="CC"`, artículos `"1254"`, `"1258"`, `"1261"`, `"1262"`, `"1278"` y `"1279"`; `ley="CCom"`, `articulo="54"`; si se firma por medios electrónicos, `ley="Ley 34/2002"`, `articulo="23"`).
- **Base legal de cada cambio** → `buscar_articulo` sobre la norma de la cláusula (la del informe de revisión si existe): p. ej. (`ley="CC"`, `"1102"`, `"1105"`, `"1107"`, `"1152"`, `"1153"`, `"1154"`, `"1256"` y `"1288"`), (`ley="BOE-A-2004-21830"`, `"4"`, `"7"`, `"8"` y `"9"`), (`ley="LEC"`, `"54"`), (`ley="TRLC"`, `"156"`), (`ley="Ley 12/1992"`, `"3"`, `"20"`, `"25"` y `"28"`).
- **Condiciones generales y prueba de la negociación** → `buscar_articulo` (`ley="BOE-A-1998-8789"`, artículos `"1"`, `"5"` y `"7"`; `ley="TRLGDCU"`, `articulo="82"` si alguna parte es consumidora).
- **Confidencialidad de lo que se entrega al negociar** → `buscar_articulo` (`ley="BOE-A-2019-2364"`, `articulo="1"`); negociación de un conflicto ya surgido → (`ley="LO 1/2025"`, artículos `"2"` y `"9"`).
- **Doctrina que sostiene cada cambio imprescindible** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`; consultas de la tabla de cláusulas) + `leer_sentencias` (`parrafos=3`, `terminos` con la cláusula).
- **Responsabilidad por romper la negociación** → `buscar_sentencias` (`consulta="ruptura injustificada de las negociaciones responsabilidad precontractual confianza"`, `base="TS"`, `jurisdiccion="CIVIL"`).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (denominación o CIF); **inmuebles** → `consultar_catastro`.
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

- La otra parte ha enviado un borrador y el cliente quiere devolverlo con cambios.
- Llega una segunda o tercera versión y hay que responder a sus cambios y a los que no aceptaron.
- El cliente quiere saber qué pedir, qué ceder y en qué orden.

| Situación | Skill que procede |
|---|---|
| No se ha analizado aún el borrador | `revision-contrato-semaforo` primero; esta skill parte de su tabla |
| El contrato lo redacta el cliente desde cero | La skill del tipo de contrato |
| El borrador es un clausulado de adhesión con consumidores | `condiciones-generales-consumidores` |
| Ya hay incumplimiento y se negocia para evitar el pleito | `masc-propuesta-acuerdo` |
| Se cambia un contrato ya firmado (adenda, prórroga, cesión) | `modificacion-novacion-cesion` |
| Antes de enseñar información sensible hace falta un acuerdo de confidencialidad | `confidencialidad-nda` |

## Datos que hay que reunir antes de redactar

No redactes la contrapropuesta al primer mensaje. Si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende el abogado y qué posición ocupa el cliente en el contrato.
2. ★ Borrador íntegro de la otra parte, con versión o fecha y anexos; si es una vuelta posterior, también la versión anterior y los cambios ya aceptados o rechazados.
3. ★ Objetivos del cliente y líneas rojas: lo que no firmará en ningún caso.
4. ★ Margen: qué puede ceder, a cambio de qué, y hasta dónde (importes, plazos, topes).
5. ★ Fuerza negociadora: quién necesita más el contrato, alternativas del cliente, fecha objetivo de firma y consecuencias de no firmar.
6. ★ Destinatario de la remisión (la otra parte o su abogado), canal (correo o carta) y tono (colaborativo o firme).
7. Informe de revisión, si existe; si no, pídelo o haz primero el paso 1 del método.
8. Si alguna parte es consumidora, si el borrador es un modelo que la otra parte usa con todos sus clientes y si hay información confidencial en juego.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de usarlo como motivo.

- **La contrapropuesta no es aceptación.** El consentimiento es el concurso de la oferta y la aceptación sobre la cosa y la causa (CC 1262): responder con cambios es una nueva oferta. Hasta que haya acuerdo sobre todo, el cliente no está obligado; pero los contratos obligan cualquiera que sea su forma si concurren sus requisitos (CC 1278) y, si falta solo la forma, las partes pueden compelerse a otorgarla (CC 1279). Por eso la remisión dice que no habrá contrato hasta la firma del documento definitivo, y la nota advierte al cliente de que no empiece a ejecutar prestaciones antes de firmar: la ejecución puede discutirse como aceptación.
- **Buena fe en los tratos.** La ruptura injustificada de negociaciones que han generado una confianza razonable en la conclusión del contrato puede dar lugar a responsabilidad precontractual. Busca la doctrina con la consulta de la lista, lee el fundamento que enumera sus requisitos y úsala en la nota: si el cliente no va a firmar en ningún caso, que lo diga pronto y por escrito; si es la otra parte quien alarga la negociación sin intención de cerrar, que el cliente documente sus gastos.
- **Condiciones generales.** Una cláusula negociada deja de ser condición general (Ley 7/1998, art. 1: cláusulas predispuestas e impuestas para una pluralidad de contratos). Conservar las versiones cruzadas, los cambios aceptados y la contrapartida obtenida sirve de prueba de la negociación individual; con consumidores, quien afirma que una cláusula se negoció lo prueba (TRLGDCU 82.2). Si el cliente es el adherente, que el modelo general de la otra parte quede incorporado solo si se le ha entregado (Ley 7/1998, arts. 5 y 7).
- **Confidencialidad.** La información que el cliente entrega al negociar solo es secreto empresarial si ha sido objeto de medidas razonables para mantenerla en secreto (Ley 1/2019, art. 1): marca los documentos como confidenciales y, si hay información sensible, propone antes un acuerdo de confidencialidad. La confidencialidad del art. 9 de la LO 1/2025 es la del proceso de negociación de un **conflicto** (art. 2 de esa ley): no cubre la negociación de un contrato nuevo.
- **Cláusulas imperativas.** Ningún texto propuesto puede contradecir una norma imperativa (CC 6.3): si la otra parte pide algo nulo, el motivo lo dice y ofrece la alternativa válida.
- **Interpretación.** Toda redacción ambigua se vuelve contra quien la redactó (CC 1288): cuando el cliente proponga el texto, que sea inequívoco.

## Método

### Paso 1. Diagnóstico y prioridades

Parte del informe de revisión o, si no lo hay, clasifica cada cláusula con los criterios de `revision-contrato-semaforo` (ROJO, ÁMBAR, VERDE desde la posición del cliente). Después asigna prioridad:

| Prioridad | Qué entra | Cómo se trata |
|---|---|---|
| **Imprescindible** | Cláusulas en ROJO y líneas rojas del cliente | Se pide el cambio con motivo jurídico; si no se acepta, el cliente no firma o sube el asunto |
| **Deseable** | Cláusulas en ÁMBAR que mejoran la posición del cliente | Se pide el cambio; se prepara una posición de repliegue |
| **Cedible** | Cambios de poco coste para el cliente o que la otra parte valora | Se pide para tener moneda de cambio o no se pide; en la nota, a cambio de qué se cede |

Limita los cambios a los que el cliente defenderá: una lista larga de peticiones menores debilita las imprescindibles.

### Paso 2. Texto propuesto

- Conserva la numeración, los títulos y los términos definidos del borrador; no renumeres ni cambies «el Cliente» por «el Contratante». Si una definición cambia, revisa todas las cláusulas que la usan.
- Un cambio por fila; texto completo del apartado propuesto, no solo la palabra que cambia.
- Actualiza remisiones internas y anexos afectados.
- No cites jurisprudencia en el texto contractual; solo cita un artículo cuando el efecto dependa de nombrarlo (apartado 2 del formato).

### Paso 3. Opciones según la posición del cliente

| Cláusula | Si el cliente asume la obligación o el riesgo | Si el cliente es el beneficiario | Doctrina (`base="TS"`, `jurisdiccion="CIVIL"`) |
|---|---|---|---|
| Responsabilidad | Tope cuantitativo fijo (no dependiente de lo que decida la otra parte), exclusión de daños indirectos definidos, plazo de reclamación; siempre con la excepción del dolo (CC 1102) | Excepción de dolo y culpa grave al tope, tope ligado al valor del contrato, sin exclusión de la obligación principal | `consulta="cláusula limitativa de responsabilidad dolo culpa grave autonomía de la voluntad"` |
| Cláusula penal | Solo función liquidatoria (CC 1152), sin acumulación con el cumplimiento (CC 1153), proporcional y con moderación en cumplimiento parcial (CC 1154) | Pena clara para el incumplimiento concreto, acumulable si se quiere y así se dice | `consulta="cláusula penal moderación artículo 1154 incumplimiento previsto"` |
| Pago | Plazo largo dentro del máximo legal entre empresas y aceptación previa (Ley 3/2004, art. 4) | Plazo corto, interés de demora legal y costes de cobro (Ley 3/2004, arts. 7 y 8) | Solo si se discute: `consulta="Ley 3/2004 plazo de pago superior a sesenta días nulidad"` |
| Duración y salida | Desistimiento con preaviso razonable y sin penalización | Duración mínima, preaviso largo, compensación por salida anticipada | `consulta="desistimiento unilateral contrato de duración indefinida preaviso razonable buena fe"` |
| Resolución por incumplimiento | Requerimiento previo con plazo de subsanación; solo incumplimientos esenciales | Lista de incumplimientos que facultan a resolver sin esperar (CC 1124 como base) | La de `resolucion-por-incumplimiento` |
| Fuerza mayor | Definición amplia y suspensión de obligaciones (CC 1105) | Definición cerrada, aviso inmediato y derecho a resolver si se prolonga | — |
| Exclusividad y no competencia | Ámbito, territorio y plazo acotados, con compensación | Ámbito suficiente para proteger la inversión; en agencia, dentro del máximo del art. 20 de la Ley 12/1992 | `consulta="pacto de no competencia postcontractual duración ámbito compensación validez"`; si el Supremo no devuelve nada aplicable fuera del ámbito laboral o societario, `consulta="pacto de no competencia postcontractual contrato de prestación de servicios validez limitación temporal territorial"`, `base="AN"`, `tipo_organo="AP"` |
| Fuero y ley | Tribunales del domicilio del cliente o arbitraje con institución y sede; no vale la sumisión en contratos de adhesión o con consumidores (LEC 54.2) | Lo mismo desde su domicilio | — |
| Cesión | Cesión libre a sociedades del grupo | Cesión solo con consentimiento escrito (CC 1205) | — |
| Concurso | No aceptar cláusulas de resolución por concurso: se tienen por no puestas (TRLC 156) | Proponer garantías o pagos anticipados en lugar de esa cláusula | — |

Para las cláusulas de un tipo concreto (renta y fianza, indemnización por clientela, precio y ajustes de participaciones, derechos de propiedad intelectual), aplica los criterios de la skill de ese contrato.

### Paso 4. Motivo: externo e interno

- **Motivo externo** (va en la tabla que recibe la otra parte): una o dos frases comerciales o jurídicas, con el artículo cuando el cambio lo exige la ley. Nunca revela prioridades, margen, posiciones de repliegue ni la estrategia del cliente.
- **Motivo interno** (va en la nota): por qué se pide, artículo leído, jurisprudencia literal cuando la validez de la cláusula la discuten los tribunales (apartado 8 del formato), prioridad, posición de repliegue y qué se cede a cambio.

### Paso 5. Segunda vuelta y siguientes

Si la otra parte responde, compara su nueva versión con la anterior cláusula por cláusula (no te fíes de su marca de cambios), clasifica cada respuesta en aceptada, rechazada, contrapropuesta o cambio nuevo no anunciado, y actualiza la tabla. Los cambios no anunciados se señalan en la remisión.

## Documentos que se entregan

1. **Contrapropuesta** (para enviar): `contrapropuesta-<tipo>-<parte-principal>-<AAAAMMDD>.docx`. Encabezado con el borrador al que responde (versión o fecha), tabla `Cláusula | Texto actual | Texto propuesto | Motivo` en el orden del contrato y, al final, el texto íntegro de las cláusulas modificadas en limpio (apartado 4 del formato). Pie: «Documento de negociación sujeto a contrato. No constituye aceptación ni oferta vinculante hasta la firma del documento definitivo.»
2. **Nota interna para el abogado** (no se envía): `nota-<tipo>-<parte-principal>-<AAAAMMDD>.docx`, 2-5 páginas: prioridades (imprescindible, deseable, cedible) con la posición inicial y la de repliegue de cada cambio; motivo interno con artículos y jurisprudencia literal (órgano, fecha, número y ECLI tal como los devolvió `leer_sentencias`); riesgos de cada concesión; advertencias sobre perfección, ejecución anticipada, confidencialidad y ruptura de negociaciones; datos pendientes; tributación y formalidades a comprobar sin importes.
3. **Carta o correo de remisión**: en el formato que pida el abogado (texto para correo o Word `remision-<tipo>-<destinatario>-<AAAAMMDD>.docx`). Contenido: referencia al borrador recibido; que se adjunta la contrapropuesta; que el resto del texto se acepta en principio sujeto al acuerdo global; que la propuesta no constituye aceptación y que no habrá contrato hasta la firma del documento definitivo; confidencialidad de la documentación intercambiada; anexos o datos pendientes; plazo deseado de respuesta. Sin prioridades ni margen del cliente.
4. **Versión íntegra del contrato con los cambios incorporados**, solo si el abogado la pide.

Cita como indica el apartado 6 del formato; formas comprobadas con `verificar_escrito`: «artículo 1262 del Código Civil», «artículo 54 del Código de Comercio», «artículo 1 de la Ley 1/2019, de 20 de febrero, de Secretos Empresariales», «artículo 9 de la Ley Orgánica 1/2025», «artículo 4 de la Ley 3/2004, de 29 de diciembre», «artículo 20 de la Ley 12/1992, de 27 de mayo, sobre Contrato de Agencia».

Si en el entorno no se pueden crear archivos, entrega los textos completos con esos títulos y avisa de que hay que pasarlos a Word.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Posición del cliente, líneas rojas y margen confirmados con el abogado antes de redactar.
- [ ] Cada cambio tiene prioridad, texto completo, motivo externo y motivo interno; cada imprescindible sobre una cláusula de validez discutida tiene jurisprudencia leída con `leer_sentencias` (decisión de la Sala, no motivos ni hechos del pleito).
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación.
- [ ] Ningún texto propuesto contradice una norma imperativa; definiciones, numeración y remisiones coherentes con el resto del borrador.
- [ ] La contrapropuesta y la remisión no revelan prioridades, repliegues ni margen; llevan la reserva de «sujeto a contrato».
- [ ] En segundas vueltas, comparado el texto nuevo con el anterior y señalados los cambios no anunciados.
- [ ] Cada ECLI citado leído o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre la contrapropuesta, la nota y la remisión; avisos revisados uno a uno.
- [ ] Sin datos personales inventados: marcadores donde falten.
- [ ] Resumen en el chat según el apartado 10 del formato: qué se ha preparado y para quién, cambios imprescindibles y cómo se han resuelto, datos que faltan y riesgos (ejecución antes de firmar, ruptura, confidencialidad), tabla de jurisprudencia citada y próximo paso (envío y fecha prevista de respuesta).
