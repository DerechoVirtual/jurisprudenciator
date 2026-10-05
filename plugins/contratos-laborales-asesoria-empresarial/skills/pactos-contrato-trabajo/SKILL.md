---
name: pactos-contrato-trabajo
description: >-
  Redacta y revisa los pactos del contrato de trabajo en Word con nota de validez: no competencia
  postcontractual (art. 21.2 ET), permanencia por especialización (art. 21.4), plena dedicación (art. 21.1)
  y confidencialidad. Úsala cuando la empresa diga «que no se vaya a la competencia», «le pagamos un máster
  y que se quede dos años» o «que no trabaje para nadie más», y cuando el trabajador pregunte «¿tengo que
  cumplir el pacto de no competencia?», «me piden devolver lo cobrado» o «la empresa renuncia al pacto al
  despedirme». Comprueba interés efectivo, compensación adecuada, duración máxima y la nulidad de la renuncia
  unilateral. Sirve a empresa y trabajador. El alto directivo tiene su propio régimen (art. 8 del Real
  Decreto 1382/1985): alta-direccion; el resto del contrato, contrato-trabajo-modalidad.
---

# Pactos del contrato de trabajo: no competencia, permanencia, plena dedicación y confidencialidad

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Requisitos de cada pacto** → `buscar_articulo` (`ley="ET"`, `articulo="21"`), deber de no concurrencia durante el contrato (`ley="ET"`, `articulo="5"`) y su sanción (`ley="ET"`, `articulo="54"`).
- **Alto directivo** → `buscar_articulo` (`ley="BOE-A-1985-17006"`, `articulo="8"`): límites propios; deriva a `alta-direccion` para el contrato.
- **Validez, arbitrio de una parte y cláusula penal** → `buscar_articulo` (`ley="CC"`, artículos `"1255"`, `"1256"`, `"1152"` y `"1154"`).
- **Confidencialidad y secretos empresariales** → `buscar_articulo` (`ley="BOE-A-2019-2364"`, artículos `"1"`, `"2"` y `"3"`; el apartado 3 del artículo 1 prohíbe usar la protección para limitar la experiencia y competencias adquiridas honestamente o para imponer restricciones no previstas legalmente). **Trampa del número**: con `ley="Ley 1/2019"` el conector devuelve una ley valenciana; pide siempre el identificador BOE y cita «Ley 1/2019, de 20 de febrero, de Secretos Empresariales».
- **Naturaleza de lo pagado y plazo para reclamar** → `buscar_articulo` (`ley="ET"`, artículos `"26"` y `"59"`).
- **Convenio aplicable y sus artículos** → `buscar_convenio` + `leer_convenio` (`buscar_en` con una sola materia: `"competencia"`, `"concurrencia"`, `"permanencia"`, `"dedicación"`, `"pluriempleo"`, `"confidencialidad"`; en muchos convenios «competencia» solo casa con las competencias de la comisión paritaria) + `vigencia_convenio`. `leer_convenio` devuelve el texto publicado originalmente: si `vigencia_convenio` registra un texto nuevo o una modificación posterior, localízala en internet en el boletín oficial y comprueba si toca estos pactos; di en la nota qué publicación rige y si el convenio los regula o no.
- **Doctrina sobre compensación, renuncia unilateral, devolución e indemnización** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; o `base="AN"` + `tipo_organo="TSJ"` + `provincia` sede de la Sala) + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión).
- **Revisión del documento antes de entregarlo** → cada redactor pasa `verificar_escrito` sobre las frases de su sección que citan normas (no sobre el documento entero) y el ensamblado de `redaccion-rapida` comprueba que cada ECLI o ROJ citado figure entre las fuentes leídas; `buscar_por_cita` solo para una sentencia que aporte el abogado y no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

La no competencia y su compensación están en el apartado 8 del formato entre las decisiones cuya validez discute la jurisprudencia: para ese pacto la doctrina es **imprescindible** (si tras dos reformulaciones no hay resolución aplicable, se aplica el punto 3 de la puerta: búsqueda en internet y localización de la sentencia con `buscar_por_cita`; si tampoco así aparece, la tarea se detiene). Para permanencia, plena dedicación y confidencialidad, se busca y se cita si existe.

## Cuándo usarla

Pregunta primero **qué pacto**, **en qué momento** (al contratar, durante la relación, al extinguirse o después) y **a quién defiende el abogado**:

- **Empresa**: quiere un pacto que se pueda exigir; o revisar uno antiguo antes de reclamar su incumplimiento o de extinguir el contrato.
- **Trabajador**: quiere saber si está obligado, si puede trabajar para la competencia, si debe devolver lo cobrado o si puede reclamar la compensación cuando la empresa dice renunciar al pacto.

| Situación | Skill |
|---|---|
| Alto directivo (poderes de la titularidad de la empresa) | `alta-direccion`; el pacto se redacta aquí con el art. 8 del Real Decreto 1382/1985 |
| Hay que redactar el contrato completo | `contrato-trabajo-modalidad` (el pacto va como anexo) |
| El trabajador compite deslealmente **durante** el contrato y la empresa quiere despedir | `carta-despido-disciplinario` (art. 54.2.d ET), con este análisis |
| Reclamar la compensación impagada o la indemnización por incumplimiento | `reclamacion-cantidad` (aporta el análisis de esta skill) |
| Deuda por permanencia que la empresa quiere descontar en el finiquito | `finiquito-liquidacion` |
| Autónomo o TRADE | `falso-autonomo-trade`: el art. 21 ET no se aplica a relaciones no laborales |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ A quién defiende el abogado, qué pacto y en qué momento.
2. ★ Empresa: actividad real, productos o servicios, mercado geográfico, clientes y competidores reales.
3. ★ Trabajador: puesto, funciones, acceso a información sensible (clientes, precios, tecnología, estrategia), titulación y si es **técnico** (determina la duración máxima del art. 21.2), salario bruto anual y fecha de antigüedad.
4. ★ No competencia: actividad que se prohíbe, ámbito geográfico, duración, compensación (importe, si se paga durante la relación o tras la extinción, y cómo figura en nómina) e indemnización por incumplimiento.
5. ★ Permanencia: especialización concreta (curso, máster, certificación), coste real pagado por la empresa y justificantes, relación con un proyecto o trabajo específico, fechas y duración de la permanencia.
6. ★ Plena dedicación: compensación económica expresa y actividades excluidas.
7. ★ Convenio aplicable (denominación y código).
8. Si el pacto ya existe: texto firmado, nóminas donde figure la compensación, fecha y causa de la extinción, nueva actividad del trabajador (empresa, puesto, fecha de inicio), comunicaciones de renuncia o requerimientos.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde».

**1. No competencia postcontractual (art. 21.2 ET)**. Solo es válido si concurren todos estos requisitos; si falta uno, el pacto es nulo:

- **Duración máxima**: dos años para técnicos y seis meses para los demás trabajadores. Si la condición de técnico es dudosa (puestos comerciales o mixtos), busca la doctrina antes de pactar más de seis meses (consulta de la lista de abajo) y deja el riesgo en la nota. Si no hay doctrina aplicable, justifica la condición de técnico en el EXPONEN con la titulación y las funciones técnicas reales, pide a la empresa que las documente y ofrece la alternativa de seis meses con la compensación ajustada.
- **Interés industrial o comercial efectivo** del empresario: redacta en el EXPONEN los hechos que lo prueban (información, clientes, conocimientos a los que accede) y limita la prohibición a la actividad y el territorio en que la empresa compite de verdad.
- **Compensación económica adecuada**: pondérala con la duración, la amplitud de la restricción, el salario y la indemnización pactada por incumplimiento. Una compensación simbólica, o desproporcionada frente a la penalidad, invalida el pacto.
- **Compensación pagada durante la relación**: tiene que ser una cantidad **adicional**, identificada y separada del salario pactado. Si solo se rebautiza una parte del salario convenido, es salario (art. 26.1 ET): el pacto carece de compensación y la empresa difícilmente podrá recuperarla, porque la doctrina que obliga a devolver lo cobrado tras la nulidad parte de que lo pagado era compensación y no salario. Si la empresa lo propone (por ejemplo, rebajar el fijo y crear un concepto «no competencia»), explícale por qué no sirve y ofrece la compensación adicional.
- **Sin renuncia unilateral**: la cláusula que permite a la empresa decidir, al extinguirse el contrato, si mantiene o deja sin efecto el pacto deja su eficacia al arbitrio de una parte (art. 1256 del Código Civil) y es nula; el trabajador conserva el derecho a la compensación. No la incluyas. Si la empresa quiere flexibilidad, que el pacto se extinga solo por acuerdo de ambas partes.
- **Incumplimiento del trabajador**: pacta la devolución de la compensación percibida y, si se quiere, una cláusula penal proporcionada (arts. 1152 y 1154 del Código Civil: el juez modera la pena si hubo cumplimiento parcial).
- **Nulidad del pacto**: según la doctrina, el trabajador puede tener que devolver lo percibido como compensación; valóralo antes de aconsejarle que alegue la nulidad.
- Cláusulas de no captación de clientes o de compañeros después del contrato restringen igualmente la actividad: trátalas con estos requisitos.

**2. Concurrencia durante el contrato (arts. 5 y 21.1 ET)**: el trabajador no puede concurrir deslealmente con la empresa aunque no haya pacto; fuera de ese caso, el pluriempleo es libre salvo pacto de plena dedicación. La concurrencia desleal puede fundar un despido por transgresión de la buena fe (art. 54.2.d ET).

**3. Plena dedicación (arts. 21.1 y 21.3 ET)**: exige compensación económica **expresa**. El trabajador puede rescindir el acuerdo comunicándolo por escrito con treinta días de preaviso y pierde la compensación y los derechos vinculados. Redacta qué actividades quedan excluidas (docencia, publicaciones, actividad familiar) para evitar discusiones.

**4. Permanencia (art. 21.4 ET)**:

- Solo si el trabajador recibe una **especialización profesional con cargo al empresario** para poner en marcha proyectos determinados o realizar un trabajo específico; la formación ordinaria del puesto o la obligatoria por ley no lo justifica.
- Duración máxima de dos años; siempre por escrito.
- Si el trabajador **abandona** antes del plazo, la empresa tiene derecho a una indemnización de daños y perjuicios: pacta una cantidad proporcional al coste acreditado y al tiempo que falte, no una cifra desconectada del gasto.
- El descuento en el finiquito exige una deuda líquida e indiscutida: si el trabajador discute el pacto o la cuantía, la empresa tiene que reclamarla.
- Si la extinción la causa la empresa (despido improcedente, extinción del art. 50 ET), busca doctrina antes de reclamar la indemnización. Si la permanencia se liga a un bonus o plan de acciones, busca la doctrina sobre ese requisito cuando el cese es un despido improcedente.

**5. Confidencialidad**:

- Deriva de la buena fe (arts. 5.a y 20.2 ET) y de la Ley 1/2019, de 20 de febrero, de Secretos Empresariales (art. 1.1: qué es secreto empresarial, incluidas las medidas razonables de protección que debe adoptar la empresa; art. 1.3: la protección no puede limitar el uso de la experiencia y competencias adquiridas honestamente ni imponer en los contratos de trabajo restricciones no previstas legalmente; art. 3: utilización o revelación ilícitas, incluido el incumplimiento de un acuerdo de confidencialidad). Cita cada artículo con el nombre completo de la ley: «su artículo 1» o «esa ley» hacen que `verificar_escrito` lo atribuya al Estatuto de los Trabajadores.
- Puede durar tras la extinción sin compensación, porque no impide trabajar sino usar o revelar información concreta. Define la información protegida (listas, precios, código, estrategias) y excluye la experiencia y conocimientos generales del trabajador. Si su redacción impide de hecho trabajar en el sector, se examinará como una no competencia encubierta (con las exigencias del art. 21.2): dilo en la nota.
- Respeta los usos lícitos del art. 2 de esa ley (información y consulta de los representantes, revelación de irregularidades).

**6. Alto directivo (art. 8 del Real Decreto 1382/1985)**: exclusividad durante el contrato salvo autorización o pacto (presunta si la vinculación es pública y no se excluyó); permanencia por especialización durante un periodo determinado; no competencia postcontractual de hasta dos años con interés efectivo y compensación adecuada.

**7. Plazos para reclamar**: la acción de cualquiera de las partes (compensación impagada, devolución, indemnización) prescribe al año (art. 59 ET); fija en la nota el día inicial con el apartado aplicable: para cada mensualidad de la compensación, su vencimiento (art. 59.2 ET); para la empresa que reclama la devolución, la Sala Cuarta cuenta el año desde que pudo ejercitar la acción por conocer el incumplimiento (búscalo con la consulta de adecuación de la compensación y cítalo si lo lees).

## Estrategia y jurisprudencia

**Si defiende a la empresa**: pacta solo lo que pueda probar que necesita. Un pacto amplio, largo y barato es un pacto nulo. Prefiere pagar la compensación tras la extinción (en mensualidades mientras dure la prohibición) o, si se paga durante la relación, como concepto separado y adicional en nómina, con la cláusula de devolución. Antes de extinguir el contrato de alguien con pacto, decide con el abogado si interesa mantenerlo (y pagarlo) o negociar su extinción por acuerdo en el documento de salida.

**Si defiende al trabajador**: revisa cada requisito y la cronología de los pagos. Si el pacto es nulo, calcula qué tendría que devolver y compáralo con el beneficio de la nueva actividad. Si la empresa «renuncia» al pacto al extinguir, reclama la compensación. Si la permanencia no responde a una especialización real o la indemnización no guarda relación con el coste, discútela.

Consultas (reformula como máximo dos veces; lee con `leer_sentencias`, `parrafos=3`, solo lo que vayas a citar):

- Compensación durante la relación: `consulta="pacto de no competencia postcontractual compensación abonada durante la relación laboral"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Adecuación de la compensación: `consulta="pacto de no competencia compensación económica adecuada nulidad"`, `base="TS"`.
- Renuncia unilateral: `consulta="pacto de no competencia renuncia empresa"`, `base="TS"` (las formulaciones largas con el art. 1256 no devuelven resultados).
- Devolución tras la nulidad: `consulta="pacto de no competencia reintegro compensación nulidad"`, `base="TS"`.
- Permanencia: `consulta="pacto de permanencia especialización profesional indemnización daños y perjuicios"`, `base="TS"`.
- Condición de técnico: `consulta="pacto de no competencia condición de técnico duración superior a seis meses"`, `base="AN"`, `tipo_organo="TSJ"` (con `base="TS"` no devuelve doctrina sobre el concepto).
- Plena dedicación: `consulta="pacto de plena dedicación compensación económica expresa"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia` sede de la Sala.

Mucha resolución del Supremo en esta materia es un auto de inadmisión por falta de contradicción: no lo cites como doctrina. Algunas sentencias también terminan por falta de contradicción (por ejemplo, sobre el reintegro de la compensación): si citas su párrafo, di que constatan el criterio de la Sala y no crean doctrina nueva. Transcribe el párrafo de fundamentos, no los importes ni los hechos de aquel pleito. En el pacto no va jurisprudencia; va a la nota.

## Documentos que se entregan

1. **Pacto** (formato, apartado 2), como anexo al contrato o documento propio: `contrato-pacto-<tipo>-<apellido-trabajador>-<AAAAMMDD>.docx`.
   - REUNIDOS e INTERVIENEN; EXPONEN con los hechos del interés efectivo (no competencia), de la especialización y su coste (permanencia) o de la información protegida (confidencialidad).
   - CLÁUSULAS en ordinales con título (apartado 2 del formato):
     - objeto y actividad prohibida o protegida, delimitada por actividad, territorio y, si procede, clientes;
     - duración y día inicial;
     - compensación: importe, forma y momento de pago, concepto separado en nómina si se paga durante la relación;
     - obligaciones de información del trabajador sobre su nueva actividad durante la vigencia;
     - consecuencias del incumplimiento: devolución y, en su caso, cláusula penal proporcionada;
     - extinción del pacto solo por acuerdo de ambas partes;
     - en permanencia: especialización, coste acreditado, plazo y cálculo de la indemnización a prorrata;
   - firmas en dos columnas.
   - **Reparto para la redacción rápida:** el pacto es corto (2-4 páginas): una sola sección, sin equipo; si reúne varios pactos (no competencia, permanencia, plena dedicación, confidencialidad), una sección por pacto y otra de comparecencia, EXPONEN, extinción y firmas.
2. **Nota para el abogado**, solo si el abogado la pide (si no, lo que esta skill manda «a la nota» —calendario, riesgos, cálculos y jurisprudencia con su ECLI— va en el resumen de la entrega): `nota-pacto-<tipo>-<empresa>-<AAAAMMDD>.docx`. Requisito a requisito con su precepto y prueba; tabla de la compensación (salario anual, compensación total, porcentaje, duración, penalidad) para valorar su adecuación; riesgos (nulidad, devolución, renuncia, compensación embebida en el salario); convenio leído; jurisprudencia con párrafo literal y ECLI.
3. **Si defiende al trabajador y el pacto ya existe**: nota de validez y de opciones (cumplir, negociar la extinción del pacto, alegar la nulidad y su coste, reclamar la compensación) con el plazo de prescripción calculado.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado; para la no competencia, al menos una resolución aplicable leída.
- [ ] Leídos en esta conversación el art. 21 ET y los que se citen (5, 26, 54 y 59 ET; 1152, 1154, 1255 y 1256 del Código Civil; arts. 1 a 3 de la Ley 1/2019 con su identificador BOE; art. 8 del Real Decreto 1382/1985).
- [ ] Convenio leído para esos pactos, con código y vigencia.
- [ ] Duración dentro del máximo según sea técnico o no; interés efectivo descrito con hechos; compensación separada del salario y ponderada en tabla.
- [ ] Ninguna cláusula de renuncia unilateral de la empresa.
- [ ] Permanencia ligada a una especialización real, con coste acreditado y plazo máximo de dos años.
- [ ] Cada ECLI de la nota leído con `leer_sentencias` o comprobado con `buscar_por_cita`; ninguno en el pacto; ningún auto de inadmisión citado como doctrina.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero) y corregido lo que señale.
- [ ] Marcadores en lugar de datos no facilitados; si algún dato no sale de Jurisprudenciator, procede de una fuente oficial con enlace y fecha de consulta, y el resumen lo identifica.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado, plazos con su precepto, cálculo de la compensación, riesgos, documentos que faltan, tabla de jurisprudencia y próximo paso.
