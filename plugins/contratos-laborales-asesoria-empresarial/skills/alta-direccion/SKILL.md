---
name: alta-direccion
description: >-
  Califica y redacta el contrato de alta dirección del Real Decreto 1382/1985 en Word (con nota para el
  abogado si la pides) y prepara su extinción: desistimiento con preaviso e indemnización, despido y dimisión del
  directivo. Úsala cuando la empresa diga «vamos a fichar a un director general», «contrato de alta
  dirección con blindaje» o «queremos prescindir del director», y cuando el directivo pregunte «¿soy alto
  directivo o trabajador común?», «me cesan con siete días por año» o «soy consejero y además director».
  Distingue alto directivo, directivo común y consejero o administrador (teoría del vínculo). Sirve a
  empresa y directivo. Si resulta directivo común, usa contrato-trabajo-modalidad; los pactos de no
  competencia o permanencia, con pactos-contrato-trabajo; la impugnación del cese, con
  redactar-demanda-despido.
---

# Alta dirección: calificación, contrato y extinción

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Concepto, fuentes, forma y contenido del contrato** → `buscar_articulo` (`ley="BOE-A-1985-17006"`, artículos `"1"`, `"2"`, `"3"`, `"4"`, `"5"`, `"6"` y `"7"`).
- **Pactos, promoción interna y extinción** → `buscar_articulo` (`ley="BOE-A-1985-17006"`, artículos `"8"`, `"9"`, `"10"`, `"11"`, `"12"`, `"13"`, `"14"` y `"15"`).
- **Frontera con el consejero y con la relación común** → `buscar_articulo` (`ley="ET"`, artículos `"1"` —letra c) del apartado 3— y `"2"` —letra a) del apartado 1—) y, si el directivo es consejero delegado o con funciones ejecutivas, (`ley="LSC"`, artículos `"249"` y `"217"`).
- **Forma del despido, plazos y notificación a la representación** → `buscar_articulo` (`ley="ET"`, artículos `"55"`, `"59"` y `"8"` —apartado 4—) y (`ley="LRJS"`, artículos `"103"` y `"65"`).
- **Empresa y cargos inscritos** → `buscar_empresa_mercantil` (administradores, consejeros delegados y apoderados inscritos: decide si el directivo forma parte del órgano de administración).
- **Doctrina sobre calificación, teoría del vínculo, desistimiento, blindajes e indemnizaciones** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; o `base="AN"` + `tipo_organo="TSJ"` + `provincia` sede de la Sala) + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión).
- **Revisión del documento antes de entregarlo** → cada redactor pasa `verificar_escrito` sobre las frases de su sección que citan normas (no sobre el documento entero) y el ensamblado de `redaccion-rapida` comprueba que cada ECLI o ROJ citado figure entre las fuentes leídas; `buscar_por_cita` solo para una sentencia que aporte el abogado y no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). En los documentos, cita «artículo 11 del Real Decreto 1382/1985» y las letras como «letra c) del apartado 3 del artículo 1 del Estatuto de los Trabajadores»: con «1.3.c)» pegado, `verificar_escrito` no detecta la cita. El verificador no lee el título de los artículos de ese real decreto (van como «Art. 11.») y puede marcar «posible disonancia» en cualquiera de ellos: compara la frase con el texto leído con `buscar_articulo` y, si coincide, mantén la cita y dilo en el resumen.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

La calificación de la relación y la frontera con el consejero las discute la jurisprudencia: antes de entregar un contrato o una valoración del cese, lee al menos una resolución aplicable sobre la calificación (formato, apartado 8).

## Cuándo usarla

Pregunta primero **a quién defiende el abogado** y **qué necesita**:

- **Empresa**: contratar a un directivo con un contrato que se califique de verdad como alta dirección; promover a un empleado; preparar su salida (desistimiento o despido) y calcular el coste.
- **Directivo**: saber si su relación es especial, común o mercantil, qué indemnización le corresponde y cómo impugnar el cese.

| Resultado de la calificación | Qué hacer |
|---|---|
| Alto directivo (art. 1.2 del Real Decreto 1382/1985) | Esta skill |
| Directivo con poderes limitados a un área y sometido a otro directivo | Relación laboral común: `contrato-trabajo-modalidad`; el cese, `carta-despido-disciplinario` o `carta-despido-objetivo` |
| Consejero o administrador que dirige la sociedad (vínculo orgánico) | Relación mercantil, fuera del orden social: el contrato del consejero ejecutivo del art. 249 de la Ley de Sociedades de Capital no es objeto de este plugin; dilo al abogado |
| Pacto de no competencia o de permanencia del directivo | Se redacta aquí con el art. 8; análisis de doctrina en `pactos-contrato-trabajo` |
| Impugnación del cese | `papeleta-conciliacion` y `redactar-demanda-despido`, con el análisis y el cálculo de esta skill |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ A quién defiende el abogado y qué necesita (contrato, promoción, salida, impugnación).
2. ★ Empresa: denominación, CIF, forma social, órgano de administración y grupo (consúltalo con `buscar_empresa_mercantil`).
3. ★ **Poderes reales del directivo**: escritura de apoderamiento (alcance, límites, mancomunado o solidario), a quién reporta, qué decide sin autorización (inversiones, contratación, estrategia, representación), ámbito (toda la empresa o un área). La calificación depende de lo que hace, no del nombre del puesto.
4. ★ Si es o ha sido **consejero o administrador** de la sociedad o del grupo, con fechas, cargo (consejero delegado, presidente, administrador solidario) y participación en el capital.
5. ★ Si tenía antes una **relación laboral común** con la empresa o el grupo (fechas, categoría) y qué se pactó al promocionar (sustitución o suspensión).
6. ★ Retribución desglosada: fija, variable, en especie (vehículo, vivienda, seguros), planes de incentivos; forma de pago.
7. ★ Duración pactada, periodo de prueba, preaviso, indemnizaciones pactadas (desistimiento, despido improcedente, cambio de control), pactos de exclusividad, permanencia y no competencia.
8. Si hay salida: fecha y forma de la comunicación, causa invocada, preaviso concedido, cantidades ofrecidas, fecha de efectos. Si es sector público, la entidad y su normativa retributiva.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde».

**1. Calificación (art. 1.2 del Real Decreto 1382/1985)**. Es alto directivo quien ejercita **poderes inherentes a la titularidad jurídica de la empresa**, **relativos a sus objetivos generales**, con **autonomía y plena responsabilidad**, limitadas solo por los criterios e instrucciones de la persona o de los órganos superiores de gobierno y administración que ostentan la titularidad. Comprueba los tres elementos con los datos 3 y 4; si falta uno, es relación común.

- Directivo común: dirige un área o departamento, depende de un director general o de otro directivo, o sus poderes son de gestión ordinaria.
- La doctrina interpreta el concepto de forma restrictiva: el nombre del cargo, un poder amplio no usado o el salario elevado no bastan.
- Consejero o administrador (letra c) del apartado 3 del artículo 1 del Estatuto de los Trabajadores y art. 1.3 del Real Decreto 1382/1985): si desempeña a la vez el cargo en el órgano de administración y la dirección o gerencia, la doctrina califica la relación por la **naturaleza del vínculo**, no por las funciones (teoría del vínculo): con integración orgánica en la administración social, la relación es mercantil; solo una relación laboral **común** puede coexistir con el cargo de consejero.
- Sector público: el art. 1.4 remite al Real Decreto 451/2012 y a su normativa retributiva específica; léela con `buscar_articulo` (`ley="Real Decreto 451/2012"`; comprueba el título de la respuesta) y, si el conector no devuelve el precepto que limita retribuciones o indemnizaciones, búscalo en internet en el BOE y cítalo con enlace y fecha de consulta antes de pactar indemnizaciones.

**2. Fuentes (arts. 2 y 3)**: la relación se basa en la recíproca confianza y la buena fe; se rige por la voluntad de las partes con sujeción al real decreto; el Estatuto de los Trabajadores solo se aplica cuando el real decreto remite o el contrato lo dice; en lo no regulado, legislación civil o mercantil. Decide con el abogado qué artículos del Estatuto se incorporan por contrato y escríbelo.

**3. Contrato (arts. 4 a 7)**:

- Por escrito, en duplicado; contenido mínimo: identificación de las partes, objeto, retribución con sus partidas en metálico y en especie, duración y las demás cláusulas que exige el real decreto (art. 4). Sin contrato escrito se presume alta dirección solo si la prestación encaja en el art. 1.2.
- Periodo de prueba de hasta nueve meses si es indefinido (art. 5).
- Duración pactada; sin pacto escrito, indefinido (art. 6).
- Tiempo de trabajo, fiestas, permisos y vacaciones según contrato, sin prestaciones que excedan notoriamente lo usual en el ámbito profesional (art. 7).
- La empresa notifica el contrato a la representación legal de los trabajadores; no entrega copia básica (art. 8.4 ET).

**4. Pactos (art. 8)**: exclusividad durante el contrato salvo autorización o pacto (la autorización se presume si la otra vinculación es pública y no se excluyó); permanencia por especialización a cargo de la empresa durante un periodo determinado, con indemnización si abandona antes; no competencia postcontractual de hasta dos años con interés industrial o comercial efectivo y compensación económica adecuada. La doctrina de la no competencia de los trabajadores comunes (compensación separada, sin renuncia unilateral de la empresa) está en `pactos-contrato-trabajo`: aplícala.

**5. Promoción interna (art. 9)**: contrato escrito especificando si la relación especial **sustituye** a la común o la **suspende**. Sin especificación, queda suspendida. La sustitución solo produce efectos a los dos años del acuerdo novatorio. Extinguida la especial, el directivo con relación común suspendida puede reanudarla, salvo despido disciplinario declarado procedente, sin perjuicio de las indemnizaciones.

**6. Extinción por el directivo (art. 10)**:

- Dimisión con preaviso mínimo de tres meses, ampliable por escrito hasta seis en contratos indefinidos o de más de cinco años; si no lo respeta, la empresa tiene derecho a los salarios del periodo incumplido. Sin preaviso si hay incumplimiento grave de la empresa.
- Extinción con derecho a la indemnización pactada (o, en su defecto, la del desistimiento) por modificaciones sustanciales que perjudiquen notoriamente su formación, menoscaben su dignidad o se decidan con grave transgresión de la buena fe; falta de pago o retraso continuado del salario; otro incumplimiento grave (salvo fuerza mayor); o sucesión de empresa o cambio importante de titularidad que renueve los órganos rectores o el contenido de la actividad principal, si se ejercita en los tres meses siguientes.

**7. Extinción por la empresa (arts. 11 y 12)**:

- **Desistimiento**: por escrito y con el preaviso del art. 10.1. Indemnización pactada o, en su defecto, siete días de salario **en metálico** por año de servicio con el límite de seis mensualidades. Si falta preaviso, salarios del periodo incumplido.
- **Despido disciplinario**: incumplimiento grave y culpable, con la forma y efectos del art. 55 ET. Si se declara improcedente, indemnización pactada o, en su defecto, veinte días de salario en metálico por año con el máximo de doce mensualidades. Improcedente o nulo: las partes acuerdan readmisión o indemnización; sin acuerdo, indemnización (art. 11.3).
- Otras causas y procedimientos del Estatuto de los Trabajadores (art. 12).
- Busca si la exigencia de audiencia previa al despido disciplinario se ha aplicado al alto directivo (consulta abajo). Sin doctrina aplicable, recomienda a la empresa darla. El conector no devuelve el Convenio 158 de la OIT: léelo en internet (BOE o base oficial de la OIT) y cítalo con enlace, o a través del párrafo literal de la sentencia que lo aplica.

**8. Faltas, suspensión, jurisdicción y plazos (arts. 13 a 15)**: sanciones en los términos del contrato, revisables en el orden social; las faltas prescriben a los doce meses desde su comisión o conocimiento. El contrato se suspende por las causas del art. 45 ET. Competencia del orden social (art. 14). Caducidad del despido y prescripción: art. 59 ET (art. 15.3). Impugna el cese, sea desistimiento o despido, dentro de los 20 días hábiles de caducidad (art. 59.3 ET y art. 103 LRJS): es la lectura prudente; da la fecha final.

**9. Consejero ejecutivo (art. 249 de la Ley de Sociedades de Capital)**: si el directivo es consejero delegado o tiene funciones ejecutivas, su contrato con la sociedad requiere aprobación previa del consejo por dos tercios, con abstención del afectado, se incorpora al acta y detalla toda retribución, incluida la indemnización por cese. Advierte al abogado de que ese contrato no es laboral.

## Estrategia y jurisprudencia

**Si defiende a la empresa**:

- Antes de redactar, confirma la calificación. Si el puesto no reúne el art. 1.2, un contrato de alta dirección no lo convierte en tal: el cese se juzgará como despido común, con su indemnización y sin el desistimiento libre.
- Si el directivo va a ser consejero, decide con el abogado entre relación mercantil (sin contrato laboral) o laboral común compatible con el cargo.
- Pacta preaviso, indemnización de desistimiento y de despido improcedente de forma expresa y calculable; los blindajes son válidos, pero en el sector público comprueba los límites propios y, en empresas en crisis, valora su riesgo.
- En la salida, elige entre desistimiento (sin causa, coste pactado o legal, preaviso) y despido disciplinario (causa probada, indemnización mayor si es improcedente). Calcula ambos escenarios.

**Si defiende al directivo**:

- Discute la calificación si no tenía autonomía y plena responsabilidad sobre los objetivos generales: si prospera, se aplica el régimen común (indemnización del despido improcedente y salarios de tramitación si hay readmisión).
- Si era consejero, valora primero la jurisdicción: con vínculo orgánico, la demanda social puede terminar en incompetencia; decide con el abogado el orden jurisdiccional antes de que caduque la acción.
- Si hubo promoción interna sin cláusula de sustitución o con menos de dos años, reclama la opción de reanudar la relación común (art. 9.3) además de la indemnización.
- Las indemnizaciones legales del art. 11 se calculan con el salario **en metálico**, que deja fuera la retribución en especie; busca doctrina antes de incluir o excluir variables, bonus o planes de acciones en el módulo, y si hay indemnización pactada, aplica el módulo que diga el contrato.

Consultas (reformula como máximo dos veces):

- Teoría del vínculo: `consulta="alta dirección teoría del vínculo consejero delegado relación mercantil"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Calificación: `consulta="alta dirección facultades inherentes a la titularidad de la empresa autonomía plena responsabilidad"`, `base="TS"`; y con `base="AN"`, `tipo_organo="TSJ"`, `provincia` sede de la Sala, `consulta="alta dirección relación laboral común notas distintivas"`.
- Desistimiento: `consulta="desistimiento alta dirección siete días por año seis mensualidades preaviso tres meses"`, `base="AN"`, `tipo_organo="TSJ"`.
- Blindaje: `consulta="alta dirección cláusula de blindaje indemnización pactada"`, `base="TS"`.
- Audiencia previa: `consulta="alta dirección despido disciplinario audiencia previa"`, `base="AN"`, `tipo_organo="TSJ"`, `fecha_desde="01/11/2024"`.
- Salario en metálico: `consulta="alto directivo desistimiento indemnización salario en metálico retribución en especie"`, `base="AN"`, `tipo_organo="TSJ"`.

En esta materia muchas resoluciones del Supremo son autos de inadmisión por falta de contradicción: no las cites como doctrina. Buena parte de la doctrina sobre calificación se dictó para entes públicos y centros sanitarios: úsala para el concepto y dilo si el caso es privado. Transcribe el razonamiento de la Sala, no los datos del directivo de aquel pleito. En el contrato no va jurisprudencia; va a la nota.

## Documentos que se entregan

1. **Contrato de alta dirección** (formato, apartado 2): `contrato-alta-direccion-<apellido-directivo>-<AAAAMMDD>.docx`.
   - REUNIDOS e INTERVIENEN (sociedad con `[CIF]` y el órgano o persona que la representa, con su nombramiento); EXPONEN (poderes que se confieren y por qué el puesto encaja en el art. 1.2; si hay relación común previa, su estado).
   - CLÁUSULAS en ordinales con título:
     - objeto y funciones, poderes conferidos y órgano del que dependen las instrucciones;
     - naturaleza especial de la relación y normas del Estatuto de los Trabajadores que se incorporan por contrato (art. 3.2);
     - promoción interna: sustitución o suspensión de la relación común (art. 9), si procede;
     - duración y periodo de prueba (arts. 5 y 6);
     - retribución fija, variable (criterios y devengo) y en especie, con su valoración;
     - tiempo de trabajo, vacaciones y permisos (art. 7);
     - exclusividad, permanencia y no competencia (art. 8);
     - preaviso (art. 10.1) e indemnizaciones pactadas por desistimiento, despido improcedente y extinción por el directivo del art. 10.3;
     - faltas y sanciones (art. 13); confidencialidad; protección de datos; jurisdicción social (art. 14);
   - firmas en dos columnas; anexo con la escritura de poderes.
   - **Reparto para la redacción rápida:** tres secciones por bloques de cláusulas: comparecencia, EXPONEN, objeto y funciones, poderes, naturaleza especial y promoción interna / duración, prueba, retribución, tiempo de trabajo, exclusividad, permanencia y no competencia / preaviso e indemnizaciones, faltas, confidencialidad, datos, jurisdicción, firmas y anexo.
2. **Nota para el abogado**, solo si el abogado la pide o si es el único entregable, porque se defiende a la parte para la que esta skill no redacta documento (si no se entrega aparte, lo que esta skill manda «a la nota» va en el resumen de la entrega): `nota-alta-direccion-<empresa>-<AAAAMMDD>.docx`. Calificación razonada elemento por elemento del art. 1.2 y frente al consejero; riesgos si se recalifica; jurisprudencia literal.
3. **Si hay salida**: tabla de cálculo en la nota (o en `calculo-extincion-alta-direccion-<apellido>-<AAAAMMDD>.docx`) con los escenarios: desistimiento (preaviso, indemnización pactada o legal), despido improcedente (pactada o legal), y régimen común si se recalifica (remite a `calculo-indemnizacion-despido`). Columnas: salario anual en metálico, salario diario (anual / 365), antigüedad en años y fracción, días por año, tope, resultado; cada operación visible. Si el abogado lo pide, la comunicación de desistimiento: `carta-desistimiento-alta-direccion-<apellido>-<AAAAMMDD>.docx` (por escrito, preaviso con su fecha o su sustitución por los salarios, indemnización y fecha de efectos).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado; al menos una resolución aplicable sobre calificación leída.
- [ ] Leídos en esta conversación los artículos del Real Decreto 1382/1985 que se citan, los arts. 1, 2, 8, 55 y 59 ET, 103 y 65 LRJS y, si es consejero, los arts. 249 y 217 de la Ley de Sociedades de Capital.
- [ ] Cargos inscritos comprobados con `buscar_empresa_mercantil`; la calificación distingue alto directivo, directivo común y consejero.
- [ ] Promoción interna: sustitución o suspensión escrita y cómputo de los dos años.
- [ ] Cálculos en tabla con salario en metálico, antigüedad, días, tope y resultado; plazo de 20 días hábiles con fecha final si hay cese.
- [ ] Cada ECLI de la nota leído con `leer_sentencias` o comprobado con `buscar_por_cita`; ninguno en el contrato; ningún auto de inadmisión citado como doctrina.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero); letras citadas con la forma que reconoce el verificador.
- [ ] Marcadores en lugar de datos no facilitados; lo que no sale de Jurisprudenciator (Convenio 158 de la OIT, normativa retributiva del sector público) procede de una fuente oficial con enlace y fecha de consulta, y el resumen lo identifica.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado, plazos con su precepto, cálculos, riesgos, documentos que faltan, tabla de jurisprudencia y próximo paso.
