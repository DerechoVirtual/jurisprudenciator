---
name: revision-contrato-semaforo
description: >-
  Revisa un contrato civil o mercantil recibido y entrega un informe en Word con semáforo: resumen
  ejecutivo, tabla Cláusula | Riesgo (ROJO, ÁMBAR, VERDE) | Motivo y base legal | Propuesta, cláusulas
  que faltan y conclusión. Lee el contrato entero, identifica su tipo y la norma imperativa aplicable,
  comprueba cada artículo con Jurisprudenciator y busca jurisprudencia de cada cláusula en ROJO.
  Distingue contratos entre empresas (autonomía de la voluntad y control de incorporación) de los
  celebrados con consumidores. Úsala con «revísame este contrato», «qué riesgos tiene», «me lo han
  pasado para firmar», «puedo firmarlo», «semáforo». Si es un clausulado de adhesión con consumidores,
  usa condiciones-generales-consumidores; para devolver los cambios a la otra parte,
  negociacion-contrapropuesta; para un conflicto sobre qué significa una cláusula,
  dictamen-interpretacion-contrato.
---

# Revisión de un contrato con semáforo de riesgos

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Límites generales de lo pactado** → `buscar_articulo` (`ley="CC"`, artículos `"6"`, `"1102"`, `"1103"`, `"1105"`, `"1107"`, `"1115"`, `"1152"`, `"1153"`, `"1154"`, `"1255"`, `"1256"`, `"1258"` y `"1288"`).
- **Norma imperativa del tipo de contrato** → `buscar_articulo` sobre el ancla del tipo (anclas del plugin, apartado 1): p. ej. (`ley="LAU"`, `"4"` y `"6"`), (`ley="Ley 12/1992"`, `"3"`, `"20"`, `"25"` y `"28"`), (`ley="BOE-A-2004-21830"`, `"3"`, `"4"`, `"7"` y `"9"`), (`ley="CC"`, `"1476"` y `"1485"`) y, para las cláusulas ligadas al concurso, (`ley="TRLC"`, `"156"`).
- **Condiciones generales y consumidores** → `buscar_articulo` (`ley="BOE-A-1998-8789"`, artículos `"1"`, `"2"`, `"5"`, `"7"` y `"8"`; `ley="TRLGDCU"`, artículos `"3"`, `"82"`, `"83"` y, según la cláusula, `"85"` a `"90"`).
- **Fuero, arbitraje y ley aplicable** → `buscar_articulo` (`ley="LEC"`, `articulo="54"`; `ley="Ley 60/2003"`, `articulo="9"`; `ley="CC"`, `articulo="10"`; con elemento extranjero, `ley="32008R0593"`, artículos `"3"` y `"4"`).
- **Jurisprudencia de cada cláusula en ROJO (imprescindible) y de las ÁMBAR cuya validez discute la doctrina** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`; si el Supremo no tiene doctrina sobre el punto o el asunto se litigará en una plaza, `base="AN"`, `jurisdiccion="CIVIL"`, `tipo_organo="AP"`, `provincia`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cláusula).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (denominación o CIF); **inmuebles** → `consultar_catastro`.
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- El cliente ha recibido un contrato o borrador de la otra parte y pregunta si puede firmarlo o qué riesgos tiene.
- Hay que auditar un contrato ya firmado para saber qué cláusulas se sostienen antes de reclamar o renegociar.
- Otra skill (por ejemplo `negociacion-contrapropuesta`) necesita el diagnóstico de riesgos antes de proponer cambios.

| Situación | Skill que procede |
|---|---|
| Clausulado de adhesión o modelo impuesto a un **consumidor** (el cliente es la empresa que lo usa o el consumidor que lo recibe) | `condiciones-generales-consumidores` |
| Hay que devolver el borrador con texto alternativo | `negociacion-contrapropuesta` (después de esta) |
| Ya hay conflicto sobre qué significa una cláusula o han cambiado las circunstancias | `dictamen-interpretacion-contrato` |
| Hay que comprobar a fondo quién firma, sus poderes o el inmueble | `verificacion-partes-contrato` |
| La otra parte ya ha incumplido | `requerimiento-cumplimiento` o `resolucion-por-incumplimiento` |
| Hay que redactar el contrato desde cero | La skill del tipo de contrato |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de emitir el informe. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ Texto íntegro del contrato con todos sus anexos y las condiciones generales o documentos a los que remita. Si falta alguno, dilo y marca en el informe las cláusulas que dependen de él; no revises «por encima».
2. ★ A quién defiende el abogado y qué posición ocupa el cliente (vendedor o comprador, prestador o cliente, arrendador o arrendatario, franquiciador o franquiciado).
3. ★ Si alguna parte actúa como consumidor y si el texto es un modelo predispuesto por la otra parte o se ha negociado.
4. ★ Estado: borrador por firmar (y fecha prevista) o contrato ya firmado (y en ejecución o incumplido).
5. ★ Objetivo y líneas rojas del cliente: qué no puede aceptar (plazo de pago, responsabilidad, exclusividad, penalizaciones) y qué le importa más.
6. Importe, duración y peso económico de la operación para el cliente.
7. Ley aplicable y, si el cliente tiene vecindad civil foral o el inmueble está en un territorio con Derecho civil propio, cuál.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de usarlo como motivo. Si el texto devuelto trae una nota «Téngase en cuenta que esta actualización… entra en vigor el…» seguida de un entrecomillado, el vigente es el texto anterior a la nota cuando esa fecha ha pasado; el entrecomillado es la redacción derogada.

### Paso 1. Lectura completa e índice

Lee el contrato entero antes de valorar ninguna cláusula. Haz un índice con la numeración original (no la renumeres), las definiciones y las remisiones internas. Anota contradicciones entre cláusulas, definiciones usadas con dos sentidos y remisiones a cláusulas o anexos inexistentes: son riesgo ÁMBAR por sí mismas (la cláusula oscura no favorece a quien la redactó, CC 1288).

### Paso 2. Calificación y régimen

- **Tipo de contrato**: por su contenido, no por su título. Si combina prestaciones de varios tipos, identifica la prestación principal y la norma imperativa de cada parte.
- **Norma imperativa**: localiza el ancla del tipo y lee qué es imperativo y qué pactable (por ejemplo, LAU 4 y 6 en arrendamientos; Ley 12/1992 en agencia; Ley 3/2004 en pagos entre empresas). Lo contrario a norma imperativa es nulo salvo que la norma prevea otro efecto (CC 6.3).
- **Entre empresas con cláusulas negociadas**: autonomía de la voluntad dentro de la ley, la moral y el orden público (CC 1255); el cumplimiento no puede dejarse al arbitrio de una parte (CC 1256); la condición que depende de la exclusiva voluntad del deudor anula la obligación (CC 1115).
- **Entre empresas con condiciones generales**: la Ley 7/1998 se aplica también a un adherente profesional (arts. 1 y 2): hay control de incorporación (arts. 5 y 7) y nulidad por contravenir norma imperativa (art. 8.1). Los controles de transparencia material y de abusividad no se aplican entre profesionales según la doctrina del Supremo: confírmalo con `consulta="condiciones generales entre profesionales controles de transparencia y abusividad improcedentes buena fe"`, `base="TS"`, `jurisdiccion="CIVIL"`, y valora las cláusulas sorprendentes por la vía de la buena fe (CC 1258). No califiques de «abusiva» una cláusula entre empresas.
- **Con consumidores**: el consumidor es la persona física que actúa con un propósito ajeno a su actividad empresarial o profesional, y también la persona jurídica sin ánimo de lucro en ese ámbito (TRLGDCU 3). Si el contrato es un clausulado de adhesión, deriva a `condiciones-generales-consumidores`. Si continúas porque es un contrato negociado, recuerda que el control de abusividad se aplica a las cláusulas no negociadas individualmente y que quien afirma la negociación la prueba (TRLGDCU 82.2).

### Paso 3. Clasificación de cada cláusula

- **ROJO**: nula, abusiva, ineficaz o gravemente perjudicial para el cliente; hay que cambiarla o no firmar. Exige artículo leído y jurisprudencia leída (apartado 8 del formato).
- **ÁMBAR**: desequilibrada, ambigua, incompleta o con un riesgo económico relevante; conviene negociarla. Artículo leído; jurisprudencia cuando la validez de ese tipo de cláusula la discuten los tribunales.
- **VERDE**: correcta y equilibrada para la posición del cliente. Basta la base legal si la hay.

El color se asigna **desde la posición del cliente**: una cláusula penal alta es ROJO para quien la paga y puede ser VERDE para quien la cobra. Si la cláusula es válida pero perjudica al cliente, es ÁMBAR, no ROJO; di en el motivo que es válida.

### Paso 4. Criterios por cláusula

| Cláusula | ROJO cuando | ÁMBAR cuando | Consulta en Jurisprudenciator (`base="TS"`, `jurisdiccion="CIVIL"`) |
|---|---|---|---|
| Limitación o exclusión de responsabilidad | Alcanza la responsabilidad por dolo (CC 1102), el tope lo fija de hecho una de las partes (CC 1256) o vacía la obligación principal | No distingue culpa grave, el tope es bajo frente al riesgo o excluye daños indirectos sin definirlos (CC 1107) | `consulta="cláusula limitativa de responsabilidad dolo culpa grave autonomía de la voluntad"` |
| Cláusula penal | Con consumidor, indemnización desproporcionadamente alta (TRLGDCU 85, apartado 6); entre empresas, pena extraordinariamente excesiva desde la perspectiva de la firma | Acumula pena y cumplimiento o pena e indemnización sin decirlo con claridad (CC 1152 y 1153); no prevé el cumplimiento parcial (CC 1154) | `consulta="cláusula penal moderación artículo 1154 incumplimiento previsto pena extraordinariamente excesiva"` |
| Resolución o desistimiento unilateral | El cumplimiento queda al arbitrio de una parte (CC 1256); en agencia indefinida, preaviso inferior al legal o menor para el agente que para el empresario (Ley 12/1992, arts. 3 y 25) | Preaviso breve o sin compensación en un contrato de duración indefinida (distribución, suministro, servicios continuados) | `consulta="desistimiento unilateral contrato de duración indefinida preaviso razonable buena fe"` |
| Resolución o suspensión por concurso de la otra parte | Siempre: se tienen por no puestas (TRLC 156) | — | No hace falta: basta el artículo; dilo en el motivo |
| Condiciones suspensivas o resolutorias | Dependen de la exclusiva voluntad del deudor (CC 1115) | Sin plazo para cumplirse ni consecuencia si no se cumplen | `consulta="condición potestativa exclusiva voluntad del deudor nulidad obligación"` |
| Plazo de pago e intereses entre empresas | Plazo pactado superior a sesenta días naturales, exclusión del interés de demora o de la compensación por costes de cobro (Ley 3/2004, arts. 4 y 9) | Procedimientos de aceptación que alargan el cómputo o interés de demora inferior al legal | `consulta="Ley 3/2004 plazo de pago superior a sesenta días nulidad cláusula abusiva"` |
| Fuero y arbitraje | Sumisión expresa en un contrato de adhesión, con condiciones generales o con consumidores (LEC 54.2), o en asuntos de juicio verbal (LEC 54.1) | Fuero lejano para el cliente; arbitraje sin institución, sede ni número de árbitros (Ley 60/2003, art. 9) | Solo si se discute su validez: `consulta="sumisión expresa contrato de adhesión nulidad competencia territorial"` |
| No competencia y exclusividad | En agencia, más de dos años desde la extinción, o más de uno si el contrato duró menos (Ley 12/1992, art. 20); restricción que puede infringir la Ley 15/2007, art. 1 | Sin límite territorial, material o temporal definido, o sin compensación | `consulta="pacto de no competencia postcontractual duración ámbito compensación validez"` |
| Indemnización por clientela en agencia o distribución | En agencia, renuncia, cuantificación anticipada o límite que impida llegar a la indemnización legal (Ley 12/1992, arts. 3 y 28: normas imperativas salvo que dispongan otra cosa) | En distribución, silencio sobre la extinción y la clientela | `consulta="agencia carácter imperativo indemnización por clientela nulidad cláusulas que limiten el derecho del agente"`; en distribución, `consulta="distribución aplicación analógica indemnización por clientela Ley de Agencia"` |
| Saneamiento | Exoneración de la evicción con mala fe del vendedor (CC 1476) o de vicios que el vendedor conocía (CC 1485) | Plazos de denuncia más breves que los legales o exclusión genérica de garantías | `consulta="pacto de exoneración del saneamiento vicios ocultos conocidos por el vendedor"` |
| Modificación unilateral del precio o del contrato | Queda al arbitrio de una parte (CC 1256); con consumidores, TRLGDCU 85, apartados 3 y 10 | Revisión de precio sin índice objetivo ni tope | Solo si hay discusión: `consulta="modificación unilateral del precio arbitrio de una de las partes 1256"` |
| Renuncia de derechos del arrendatario de vivienda | Modifica en su perjuicio las normas del título II de la LAU (LAU 6) | — | Deriva a `arrendamiento-vivienda` para el detalle |
| Cesión del contrato y subcontratación | — | Una parte puede ceder sin consentimiento de la otra (la sustitución del deudor exige consentimiento del acreedor, CC 1205) | — |
| Confidencialidad, datos y propiedad intelectual | — | Sin plazo, sin definición de información confidencial, sin encargo de tratamiento cuando un proveedor trata datos personales (RGPD 28) o cesión de derechos sin modalidades, tiempo ni territorio (TRLPI 43) | Deriva a `confidencialidad-nda`, `encargo-tratamiento-datos` o `licencia-cesion-propiedad-intelectual` |
| Integridad del acuerdo y notificaciones | — | Deja fuera ofertas o anexos que el cliente considera parte del pacto; direcciones o medios de notificación no fehacientes | — |

Para los intereses moratorios entre profesionales, la doctrina los trata como cláusula penal: aplica esa fila. En préstamos, remite el análisis de usura a `prestamo-reconocimiento-deuda`.

### Paso 5. Jurisprudencia

- Busca con las consultas de la tabla y reformula como máximo dos veces cambiando términos, no filtros. Si tras dos reformulaciones no hay ninguna resolución aplicable a una cláusula en ROJO, aplica la puerta: detén el informe y dile al abogado qué consulta falló.
- Prefiere la Sala Primera y lo reciente (`anios=5` si hay mucha doctrina antigua). Usa una Audiencia Provincial solo si el Supremo no tiene doctrina sobre el punto o el pleito irá a esa plaza, y dilo: «doctrina de Audiencia Provincial».
- Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar. Transcribe el párrafo de la **decisión de la Sala**, no el resumen de los motivos del recurrente ni un voto particular; si los `terminos` devuelven el motivo, repite con los términos del fallo.
- No traslades doctrina de consumidores a un contrato entre empresas ni al revés: di en el motivo qué régimen aplicó la sentencia.

### Paso 6. Cláusulas que faltan

Compara el contrato con el contenido mínimo de su tipo (la skill de ese contrato lo detalla) y, como mínimo, con: objeto preciso; precio, revisión y forma y plazo de pago; duración, prórroga y preaviso; entrega o recepción y aceptación; garantías y su plazo; responsabilidad y su tope con la excepción del dolo; fuerza mayor (CC 1105); causas de resolución y consecuencias; cláusula penal, si interesa al cliente; confidencialidad; datos personales; propiedad intelectual; cesión; notificaciones con medio fehaciente; ley aplicable y fuero o arbitraje; integridad del acuerdo; identificación de firmantes y su título. Anota solo las que el cliente necesite en su posición.

### Tributación y formalidades

Señala si el contrato puede exigir escritura, inscripción, depósito de fianza o liquidación de impuestos (IVA o ITP y AJD) y quién los asume según el texto. No des tipos ni importes que no hayas leído en una norma con `buscar_articulo`; para doctrina tributaria, `buscar_consultas_hacienda` o `buscar_doctrina_teac`.

## Documento que se entrega

**Informe de revisión en Word** (apartados 4 y 6 del formato). Nombre: `revision-<tipo>-<parte-principal>-<AAAAMMDD>.docx`. Orden:

1. **Encabezado**: cliente y posición, contrato revisado (título, versión o fecha, número de páginas, anexos recibidos y anexos que faltan), fecha del informe.
2. **Resumen ejecutivo** (5-10 líneas): número de cláusulas en ROJO, ÁMBAR y VERDE; los dos o tres riesgos principales; recomendación: firmar, firmar con los cambios indicados o no firmar.
3. **Régimen jurídico**: tipo de contrato, contrato entre empresas o con consumidor, negociado o de adhesión, norma imperativa leída.
4. **Tabla de semáforo** en el orden del contrato: `Cláusula | Riesgo | Motivo y base legal | Propuesta`. Una fila por cláusula (las VERDE que no aporten nada pueden agruparse en una fila «Resto de cláusulas»). En «Motivo y base legal», el artículo con su norma y, en ROJO y en las ÁMBAR cuya validez discute la doctrina, el párrafo literal entre comillas con órgano, fecha, número y ECLI. En «Propuesta», el texto alternativo o qué hay que negociar.
5. **Cláusulas que faltan**: tabla `Cláusula | Por qué la necesita el cliente | Propuesta`.
6. **Verificación de las partes**: resultado de `buscar_empresa_mercantil` de cada sociedad (estado, cargo del firmante) o remisión a `verificacion-partes-contrato` si hay que profundizar.
7. **Tributación y formalidades a comprobar**.
8. **Conclusión y próximos pasos**: qué cambiar antes de firmar y si procede `negociacion-contrapropuesta`.
9. **Normativa y jurisprudencia consultadas**: artículo, norma y «vigente desde»; resoluciones con órgano, fecha, número y ECLI.

**Reparto para la redacción rápida:** cierras tú en el plan la lectura completa, la calificación y el color de cada cláusula (pasos 1 a 3). Secciones: encabezado, resumen ejecutivo y régimen jurídico / un bloque de cláusulas del contrato por redactor (objeto y precio / responsabilidad y penas / duración y resolución / cláusulas finales), cada uno con su tabla `Cláusula | Riesgo | Motivo y base legal | Propuesta` y la jurisprudencia de sus cláusulas en ROJO / cláusulas que faltan, verificación de partes, tributación y formalidades / conclusión y normativa y jurisprudencia consultadas.

Cita como indica el apartado 6 del formato. Formas comprobadas con `verificar_escrito`: «artículo 1102 del Código Civil», «artículo 7 de la Ley 7/1998, de 13 de abril, sobre condiciones generales de la contratación», «artículo 9 de la Ley 3/2004, de 29 de diciembre», «artículo 54 de la Ley de Enjuiciamiento Civil», «apartado 6 del artículo 85 del Real Decreto Legislativo 1/2007», «artículo 6 de la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos», «artículo 20 de la Ley 12/1992, de 27 de mayo, sobre Contrato de Agencia», «artículo 156 del Real Decreto Legislativo 1/2020». Nunca «85.6)» pegado ni «de la misma ley».

Si en el entorno no se pueden crear archivos, entrega el texto completo con esos títulos y avisa de que hay que pasarlo a Word.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] El contrato se leyó entero, con anexos; los que faltan constan en el informe.
- [ ] Posición del cliente, carácter empresarial o de consumo y tipo de contrato fijados antes de colorear.
- [ ] Cada artículo del informe se leyó con `buscar_articulo` en esta conversación, con su texto vigente (no el entrecomillado anterior de una nota «Téngase en cuenta»).
- [ ] Cada cláusula en ROJO tiene artículo y párrafo literal de una resolución leída con `leer_sentencias` (decisión de la Sala, no motivos ni hechos del pleito); las ÁMBAR discutidas por la doctrina también.
- [ ] Ninguna cláusula entre empresas calificada de «abusiva»; ninguna doctrina de consumo aplicada a un contrato entre empresas sin decirlo.
- [ ] Cada ECLI citado leído o comprobado con `buscar_por_cita`.
- [ ] Las propuestas mantienen las definiciones del contrato y no crean contradicciones con otras cláusulas.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); los avisos de «posible disonancia» contrastados con el artículo leído.
- [ ] Sin tipos ni importes tributarios no comprobados; sin datos personales inventados.
- [ ] Resumen en el chat según el apartado 10 del formato: qué se revisó y para quién, cláusulas en ROJO y cómo se proponen resolver, datos y anexos que faltan, tabla de jurisprudencia citada (ECLI · órgano · fecha · qué sostiene) y próximo paso.
