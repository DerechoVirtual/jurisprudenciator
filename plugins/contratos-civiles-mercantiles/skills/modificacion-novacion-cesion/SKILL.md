---
name: modificacion-novacion-cesion
description: >-
  Redacta en Word la adenda o novación de un contrato (modificativa o extintiva, arts. 1203-1213 CC), la
  cesión del contrato con consentimiento del cedido, el cambio de deudor, la subrogación, la cesión de
  créditos, la prórroga y la resolución de mutuo acuerdo con finiquito recíproco, con su nota para el
  abogado y las notificaciones necesarias. Úsala con «adenda», «modificar el contrato», «prorrogar»,
  «ceder el contrato», «que otra empresa se quede con el contrato», «subrogarse», «ceder la deuda»,
  «resolver de mutuo acuerdo» o «finiquito». Cuida que no caigan las garantías (fianzas y avales). Si
  hay que averiguar qué dice el contrato vigente, dictamen-interpretacion-contrato; si se resuelve por
  incumplimiento, resolucion-por-incumplimiento.
---

# Modificación, novación, cesión y resolución de mutuo acuerdo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Novación modificativa o extintiva y cambio de deudor** → `buscar_articulo` (`ley="CC"`, del `"1203"` al `"1208"`, uno por uno, y `"1156"`, `"1255"` y `"1257"`).
- **Subrogación y cesión de créditos** → `buscar_articulo` (`ley="CC"`, del `"1209"` al `"1213"`, `"1112"`, del `"1526"` al `"1529"`, `"1198"` y `"1535"`), (`ley="CCom"`, artículos `"347"` y `"348"`) y, si el crédito tiene hipoteca, (`ley="BOE-A-1946-2453"`, `articulo="149"`).
- **Garantías y forma** → `buscar_articulo` (`ley="CC"`, artículos `"1207"`, `"1847"`, `"1851"`, `"1278"`, `"1279"` y `"1280"`).
- **Resolución de mutuo acuerdo, finiquito y renuncias** → `buscar_articulo` (`ley="CC"`, artículos `"6"`, `"1187"`, `"1188"`, `"1809"`, `"1816"` y `"1817"`) y, si hay consumidor, (`ley="TRLGDCU"`, artículos `"10"` y `"86"`).
- **Régimen especial del contrato** → `buscar_articulo` con el valor de las anclas: arrendamientos (`ley="LAU"`, artículos `"4"`, `"8"` y `"32"`), agencia, préstamo, sociedades.
- **Doctrina** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`; `base="AN"`, `tipo_organo="AP"` si el Supremo no ha tratado el punto) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (cedente, cesionario, cedido y fiadores: existencia, estado, administradores y apoderados vigentes, disolución o concurso).
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Cita la LAU como «artículo 32 de la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos» y la Ley Hipotecaria por su nombre completo con fecha.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

Identifica primero qué operación es, porque cada una tiene requisitos distintos:

| Operación | Qué cambia | Quién tiene que consentir |
|---|---|---|
| Adenda o novación modificativa | Objeto, precio, plazo o condiciones; el contrato sigue | Las partes (y los fiadores, para que les alcance) |
| Novación extintiva | Nace una obligación nueva que sustituye a la anterior | Las partes, de forma terminante |
| Cambio de deudor (asunción de deuda) | Otro deudor ocupa el lugar del primitivo | El acreedor, siempre |
| Cesión del contrato | Una parte transmite toda su posición (derechos y obligaciones) | Cedente, cesionario y cedido |
| Cesión de crédito | Solo el derecho de cobro | Cedente y cesionario; al deudor basta notificarle |
| Subrogación | Un tercero que paga ocupa el lugar del acreedor | Según el caso (arts. 1209 a 1211 CC) |
| Prórroga | Solo el plazo | Las partes; el fiador, o la fianza se extingue |
| Resolución de mutuo acuerdo con finiquito | Termina el contrato y se liquidan las cuentas | Las partes |

Si encaja mejor otra skill, dilo y deriva:

| Situación | Skill |
|---|---|
| Qué dice o si ya se novó el contrato vigente | `dictamen-interpretacion-contrato` |
| Terminar por incumplimiento de la otra parte | `resolucion-por-incumplimiento` |
| Prórroga legal o tácita de un alquiler de vivienda | `arrendamiento-vivienda` |
| Traspaso o cesión de un local con obras, renta y fianza | `arrendamiento-local-negocio` (y esta skill para el documento de cesión) |
| Deuda reconocida con plan de pagos, o novación o subrogación de un préstamo hipotecario | `prestamo-reconocimiento-deuda` |
| Entrada de un socio o venta de la sociedad (no hay cesión de contratos) | `compraventa-participaciones` |
| Acuerdo para evitar un pleito ya planteado | `masc-propuesta-acuerdo` |
| Transmisión de empresa con trabajadores | plugin laboral (sucesión de empresa) |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ Contrato original con anexos y todas las adendas anteriores, en orden cronológico.
2. ★ A quién defiende el abogado: acreedor o deudor; cedente, cesionario o cedido; quien concede la prórroga o quien la pide.
3. ★ Qué cambia exactamente, desde qué fecha y qué sigue igual.
4. ★ Garantías vigentes: fianzas, avales a primer requerimiento, hipotecas, prendas, seguros; quién las prestó y si firmará.
5. ★ Si el contrato prohíbe la cesión, exige consentimiento o la autoriza de antemano (art. 1112 CC).
6. ★ Estado de cumplimiento a la fecha: deudas, entregas pendientes, reclamaciones abiertas; quién responde de lo anterior a la cesión.
7. Precio de la cesión o contraprestación de la novación, y forma de pago.
8. Si alguna parte es consumidor, o si el contrato original se otorgó en escritura pública o está inscrito.
9. Situación de cada parte: si hay disolución, liquidación o concurso (compruébalo con `buscar_empresa_mercantil`; en concurso, deriva la cuestión de los efectos del concurso sobre el contrato a la norma concursal con `ley="TRLC"`).
10. Derecho civil foral o autonómico aplicable: si aplica, busca su norma con `buscar_boe`; si el conector no devuelve el precepto, léelo en internet en el texto consolidado oficial y cítalo con enlace (punto 3 de la puerta).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de aplicarlo.

**1. Novación modificativa o extintiva.** Las obligaciones pueden modificarse variando su objeto o condiciones principales, sustituyendo al deudor o subrogando a un tercero en los derechos del acreedor (art. 1203 CC). Para que una obligación quede extinguida por otra hace falta que así se declare terminantemente o que la antigua y la nueva sean de todo punto incompatibles (art. 1204). Para la Sala Primera la novación extintiva no se presume, la voluntad de extinguir ha de ser inequívoca y la duda favorece a quien niega la novación (consulta 1). Consecuencias que deciden la redacción:
- Si la obligación principal se extingue por novación, las accesorias solo subsisten en cuanto aprovechen a terceros que no consintieron (art. 1207): en una novación extintiva caen las garantías salvo que se vuelvan a constituir.
- La novación es nula si lo es la obligación primitiva, salvo las excepciones del art. 1208.
- Por eso, en una adenda di expresamente que es modificativa, que subsiste todo lo no modificado y que se mantienen las garantías, y haz firmar a los garantes.

**2. Garantías y prórroga.** La obligación del fiador se extingue con la del deudor (art. 1847 CC), y la prórroga concedida al deudor sin consentimiento del fiador extingue la fianza (art. 1851). La modificación de la obligación garantizada no le es oponible al fiador que no la consintió: solo responde en los términos originales (consulta 2). Consecuencia: toda adenda que amplíe plazo, precio o penalidades lleva la firma de conformidad de cada fiador o avalista, o una nueva garantía.

**3. Cambio de deudor.** Puede hacerse sin conocimiento del deudor primitivo, pero nunca sin consentimiento del acreedor (art. 1205 CC). La insolvencia del nuevo deudor aceptado no hace revivir la acción contra el primitivo, salvo insolvencia anterior y pública o conocida por él (art. 1206). Si defiendes al acreedor, pacta que el deudor primitivo queda como garante solidario.

**4. Cesión del contrato.** No tiene regulación general en el Código Civil: es la transmisión de la posición contractual completa y exige el consentimiento del contratante cedido (conjunción de tres voluntades), que puede darse de antemano en el contrato (consulta 3). Distínguela de la cesión de crédito (consulta 4). Los contratos solo producen efecto entre las partes y sus herederos (art. 1257). Regímenes especiales que hay que leer:
- Vivienda: el arrendatario no puede ceder sin consentimiento escrito del arrendador (art. 8 LAU).
- Local de negocio: puede ceder sin consentimiento del arrendador, que tiene derecho a elevar la renta un 20 % (10 % en subarriendo parcial), con notificación fehaciente en el mes siguiente (art. 32 LAU); en uso distinto de vivienda manda primero lo pactado (art. 4.3 LAU), así que comprueba si el contrato lo excluyó o lo condicionó.
- Consumidores: es abusiva la liberación de responsabilidad del empresario por cesión del contrato a un tercero sin consentimiento del consumidor si puede mermar sus garantías (art. 86.3 TRLGDCU).

**5. Cesión de créditos.** Los derechos nacidos de una obligación son transmisibles salvo pacto en contrario (art. 1112 CC). La cesión surte efecto frente a terceros desde que su fecha es cierta y, si se refiere a un inmueble, desde su inscripción (art. 1526). El deudor que paga al cedente antes de conocer la cesión queda liberado (art. 1527), y la compensación que puede oponer depende de si consintió o conoció la cesión (art. 1198). La cesión comprende fianzas, hipotecas, prendas y privilegios (art. 1528). El cedente de buena fe responde de la existencia y legitimidad del crédito, no de la solvencia del deudor salvo pacto o insolvencia anterior y pública (art. 1529). En créditos mercantiles basta notificar al deudor, que desde entonces solo paga bien al cesionario (arts. 347 y 348 CCom). Si el crédito es litigioso, el deudor puede extinguirlo reembolsando lo que pagó el cesionario (art. 1535). Crédito hipotecario: escritura pública e inscripción de la cesión (art. 149 de la Ley Hipotecaria).

**6. Subrogación.** No se presume fuera de los casos legales; en los demás debe establecerse con claridad (art. 1209 CC). Presunciones del art. 1210, subrogación por el deudor con préstamo en escritura (art. 1211), efectos (art. 1212) y preferencia del acreedor pagado en parte (art. 1213).

**7. Resolución de mutuo acuerdo y finiquito.** Las partes pueden extinguir el contrato por su voluntad (arts. 1255 y 1156 CC). Si cada una cede algo para evitar o terminar un pleito, el acuerdo es transacción (art. 1809), con autoridad de cosa juzgada entre ellas (art. 1816) e impugnable por error, dolo, violencia o falsedad (art. 1817). La renuncia de derechos solo vale si no contraría el interés o el orden público ni perjudica a terceros (art. 6.2); la condonación expresa se ajusta a las formas de la donación (art. 1187). Con consumidores, la renuncia previa a sus derechos es nula (art. 10 TRLGDCU) y la renuncia de acciones en un acuerdo novatorio tiene que superar el control de transparencia y limitarse a la controversia (consulta 5). El alcance del finiquito se interpreta por lo que liquida: enumera los conceptos (consulta 6).

**8. Forma.** Los contratos obligan cualquiera que sea su forma (art. 1278 CC), pero las partes pueden compelerse a llenar la forma exigida (art. 1279). Van en documento público los actos sobre derechos reales en inmuebles, los arrendamientos de seis o más años que deban perjudicar a tercero y la cesión de derechos que proceden de un acto en escritura pública (art. 1280). Si el contrato original está en escritura pública o inscrito, advierte en la nota de que la modificación o la cesión necesitará escritura para perjudicar a terceros o inscribirse (art. 1280 CC y, en el crédito hipotecario, art. 149 de la Ley Hipotecaria).

**9. Tributación.** La cesión onerosa de un contrato o de un crédito, la novación de préstamos con garantía y su escritura pueden tributar (ITP, AJD o IVA). No des tipos ni importes: pide al abogado que lo compruebe y, si quiere doctrina, `buscar_consultas_hacienda` con la operación concreta.

## Cláusulas clave y jurisprudencia

En la cesión del contrato y el cambio de deudor hay tres intereses distintos; ajusta cada cláusula al cliente:

| Cláusula | Cedente o deudor que sale | Cesionario o nuevo deudor | Cedido o acreedor |
|---|---|---|---|
| Liberación de quien sale | Total desde la fecha de efectos | Indiferente | Queda como garante solidario de lo cedido |
| Obligaciones anteriores a la fecha de efectos | Las asume el cesionario | Las conserva el cedente | Responden los dos solidariamente |
| Manifestaciones sobre el estado del contrato | Mínimas | Cumplimiento al día, sin reclamaciones, garantías vigentes, con responsabilidad del cedente | Las mismas, dirigidas también a él |
| Excepciones oponibles | Indiferente | El cedido renuncia a las que tenía frente al cedente | Conserva frente al cesionario las que tenía |
| Garantías | Se liberan las que prestó | Solo las nuevas que acepte | Se mantienen o se sustituyen antes de la fecha de efectos |

En la adenda, la prórroga y el finiquito, las dos posiciones son estas:

| Cláusula | Quien pide el cambio o paga | Quien lo concede o cobra |
|---|---|---|
| Calificación | «Novación modificativa»; subsiste lo no modificado | Igual, más la firma de fiadores y avalistas |
| Prórroga | Nuevo plazo sin más cambios | Actualización del precio y firma del fiador o nueva garantía |
| Finiquito | Renuncia general a toda reclamación | Renuncia limitada a lo liquidado, con exclusión de vicios ocultos, responsabilidades legales imperativas y obligaciones que sobreviven (confidencialidad, no competencia) |

Consultas (`base="TS"`, `jurisdiccion="CIVIL"`; reformula como máximo dos veces):

1. `consulta="novación extintiva modificativa animus novandi declaración terminante incompatibilidad artículo 1204"`.
2. `consulta="prórroga concedida al deudor sin consentimiento del fiador extingue la fianza artículo 1851"` (incluye avales a primer requerimiento y novaciones no consentidas).
3. `consulta="cesión de la posición contractual requiere consentimiento del cedido derechos y obligaciones"`, con `base="AN"`, `tipo_organo="AP"`.
4. `consulta="cesión del crédito frente a cesión del contrato consentimiento del deudor cedido notificación"`.
5. `consulta="acuerdo novatorio renuncia de acciones consumidor control de transparencia"`.
6. `consulta="finiquito liquidación de relaciones comerciales alcance renuncia de acciones"`, con `base="AN"`, `tipo_organo="AP"`.

Úsalas en la nota: la calificación como modificativa (1), la firma de los garantes (2), el consentimiento del cedido (3 y 4) y la renuncia de un consumidor (5) son cláusulas cuya eficacia depende de la jurisprudencia (apartado 8 del formato): cítala literal. Si no hay resolución aplicable tras dos reformulaciones, aplica el punto 3 de la puerta (internet para localizarla, `buscar_por_cita` y `leer_sentencias` para citarla); si tampoco así aparece, detén la tarea.

## Documentos que se entregan

Siempre dos documentos y, si hacen falta, las notificaciones:

1. El documento de la operación, maquetado según el apartado 2 del formato:
   - `contrato-adenda-<parte-principal>-<AAAAMMDD>.docx`: REUNIDOS e INTERVIENEN; EXPONEN con el contrato original (fecha, objeto), las adendas anteriores y el motivo del cambio; ESTIPULACIONES: PRIMERA.- Naturaleza: novación modificativa. SEGUNDA.- Modificaciones, cláusula por cláusula, con el texto nuevo íntegro (no «donde dice… debe decir…» suelto). TERCERA.- Fecha de efectos. CUARTA.- Subsistencia de lo no modificado. QUINTA.- Garantías (ratificación de fiadores y avalistas, que intervienen y firman). SEXTA.- Ley y fuero, como el contrato original salvo cambio pactado.
   - `contrato-cesion-<parte-principal>-<AAAAMMDD>.docx`: intervienen cedente, cesionario y cedido; objeto (posición contractual completa); fecha de efectos; obligaciones anteriores y posteriores; liberación o garantía del cedente; manifestaciones del cedente; consentimiento del cedido; garantías (sustitución o mantenimiento); precio de la cesión; entrega de documentación; notificaciones.
   - `contrato-cesion-credito-<parte-principal>-<AAAAMMDD>.docx`: crédito identificado (origen, importe, vencimiento), accesorios, precio, responsabilidad del cedente (art. 1529 CC) y obligación de notificar al deudor.
   - `contrato-prorroga-<parte-principal>-<AAAAMMDD>.docx`: nuevo plazo, condiciones y garantías.
   - `contrato-resolucion-mutuo-acuerdo-<parte-principal>-<AAAAMMDD>.docx`: fecha de extinción; liquidación con cuadro de conceptos e importes (`[IMPORTE]`); pagos y devoluciones; entrega de bienes o documentación; obligaciones que sobreviven; renuncia recíproca limitada a lo liquidado; transacción si hay controversia.
   - **Reparto para la redacción rápida:** una sección de comparecencia y expositivos (contrato original, adendas anteriores y motivo); una por bloque de estipulaciones (`### [ESTIPULACION]`) propio de la operación (en la adenda, las modificaciones cláusula por cláusula con el texto nuevo íntegro; en la cesión, efectos, obligaciones anteriores y posteriores, liberación y consentimiento del cedido; en la resolución de mutuo acuerdo, la liquidación con su cuadro); y una de garantías, subsistencia, ley, fuero y firmas. Los documentos de una o dos páginas (prórroga, cesión de crédito, notificaciones) los redactas tú. La nota: apartado 11 del formato.
2. `nota-<tipo>-<parte-principal>-<AAAAMMDD>.docx` (apartado 3 del formato): calificación de la operación y por qué; consentimientos obtenidos y pendientes; efecto sobre cada garantía; forma e inscripción; tributación que comprobar; riesgos y alternativas.
3. Si hace falta, notificación fehaciente al cedido, al deudor cedido o al arrendador: `requerimiento-<destinatario>-<AAAAMMDD>.docx` (apartado 5 del formato), con el hecho de la cesión, su fecha de efectos y, en la cesión de crédito, a quién se paga desde ese momento. El medio de envío lo decide el abogado.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Operación calificada con la tabla de «Cuándo usarla»; consentimientos necesarios identificados y recogidos en el documento.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos citados (CC 1203 a 1213, 1207, 1847 y 1851, 1526 a 1529, y los de la LAU, el Código de Comercio o la Ley Hipotecaria si se usan).
- [ ] Cada garantía tratada: se mantiene con firma del garante, se sustituye o se extingue a sabiendas del cliente.
- [ ] Texto modificado íntegro y coherente con las definiciones del contrato original; fechas de efectos e importes cuadrados con la liquidación.
- [ ] Renuncias limitadas a lo liquidado y, con consumidores, revisadas con la doctrina de transparencia.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`.
- [ ] Lo que no dio Jurisprudenciator y se obtuvo en internet, citado con enlace y fecha de consulta desde fuente oficial y señalado en el resumen; ninguna sentencia citada sin `buscar_por_cita` y `leer_sentencias`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); los avisos de «posible disonancia» contrastados con el apartado leído.
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[IMPORTE]`, `[FECHA DE EFECTOS]`) en lugar de datos inventados; sin tipos ni cuotas tributarias.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas, consentimientos y documentos pendientes, tabla de jurisprudencia, plazos (notificación del art. 32 LAU, si aplica) y próximo paso.
