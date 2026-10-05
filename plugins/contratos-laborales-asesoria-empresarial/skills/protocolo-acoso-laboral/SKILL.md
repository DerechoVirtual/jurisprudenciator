---
name: protocolo-acoso-laboral
description: >-
  Redacta el protocolo de prevención y actuación frente al acoso sexual, por razón de sexo, discriminatorio,
  contra las personas LGTBI y laboral o moral, y guía la instrucción de una denuncia interna: recepción,
  medidas cautelares, entrevistas, confidencialidad, informe y propuesta de sanción. Úsala cuando digan
  «protocolo de acoso», «nos han denunciado un acoso», «investigación interna», «comisión instructora»,
  «informe de conclusiones» o «protocolo LGTBI». Sirve a la empresa y al trabajador denunciante o denunciado
  que quiere saber si el protocolo se ha cumplido. Entrega el protocolo en Word y, si se piden, el informe de instrucción
  modelo y una nota. Para el canal de la Ley 2/2023 usa canal-denuncias-informantes; para despedir al
  acosador, carta-despido-disciplinario; para demandar, tutela-derechos-fundamentales o
  extincion-contrato-trabajador.
---

# Protocolo frente al acoso e instrucción de denuncias internas

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Deber de prevenir y de dar cauce a las denuncias; definiciones de acoso sexual y por razón de sexo** → `buscar_articulo` (`ley="LO 10/2022"`, `articulo="12"`), (`ley="BOE-A-2007-6115"`, artículos `"7"`, `"46"` y `"48"`) y (`ley="BOE-A-2020-12214"`, artículos `"2"` y `"12"`).
- **Acoso discriminatorio y protocolo LGTBI** → `buscar_articulo` (`ley="BOE-A-2022-11589"`, `articulo="6"`), (`ley="BOE-A-2023-5366"`, artículos `"3"` y `"15"`) y (`ley="Real Decreto 1026/2024"`, artículos `"2"` y `"8"`); contenido mínimo del protocolo LGTBI (anexo II) → `leer_boe` (`identificador="BOE-A-2024-20402"`).
- **Acoso laboral como riesgo psicosocial** → `buscar_articulo` (`ley="LPRL"`, artículos `"14"`, `"15"`, `"16"`, `"18"` y `"24"`) y (`ley="Real Decreto 39/1997"`, artículos `"4"` y `"5"`).
- **Derechos del trabajador, despido, sanciones, garantías de representantes y prescripción** → `buscar_articulo` (`ley="ET"`, artículos `"4"`, `"54"`, `"55"`, `"56"`, `"58"`, `"60"` y `"68"`) y (`ley="LRJS"`, `articulo="105"`); tipificación administrativa → (`ley="BOE-A-2000-15060"`, `articulo="8"`); delitos y su perseguibilidad → (`ley="CP"`, artículos `"173"`, `"184"` y `"191"`).
- **Relación con el canal de denuncias** → `buscar_articulo` (`ley="BOE-A-2023-4513"`, artículos `"2"`, `"7"`, `"9"`, `"35"`, `"36"` y `"39"`).
- **Faltas, sanciones y procedimiento disciplinario del convenio** → `buscar_convenio` + `leer_convenio` (`buscar_en="acoso"` y `buscar_en="faltas muy graves"`) + `vigencia_convenio`. Si el convenio aplicable no regula faltas y sanciones, busca su artículo de prelación o remisión y lee el régimen disciplinario del acuerdo o convenio estatal del sector (con `leer_convenio` sobre su código). Si `vigencia_convenio` registra una modificación posterior al texto que devuelve `leer_convenio`, localízala con `novedades_boe` o `buscar_boe` (o en el boletín autonómico o provincial) y léela con `leer_boe`: los acuerdos sectoriales están añadiendo una audiencia previa al despido con forma y plazo propios y capítulos LGTBI que remiten al anexo II del Real Decreto 1026/2024.
- **Doctrina sobre garantías de la investigación, audiencia previa, prescripción y responsabilidad de la empresa** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`; para aplicación de protocolos, `base="AN"`, `jurisdiccion="SOCIAL"`, `tipo_organo="TSJ"`) + `leer_sentencias` (`parrafos=3`).
- **Convenio 190 de la OIT** (violencia y acoso, también de terceros): no lo devuelve el conector; léelo en internet en el instrumento publicado en el BOE (punto 3 de la puerta).
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

## Cuándo usarla

Pregunta primero qué necesita y para quién:

1. **Empresa sin protocolo o con uno desfasado** → redacta el protocolo (sección «Documentos», 1).
2. **Empresa con una denuncia recibida** → guía la instrucción con el protocolo vigente de la empresa (léelo antes) y, si lo pide, prepara el informe de instrucción modelo (sección «Documentos», 2). **Si la empresa aún no tiene protocolo**, no esperes a aprobarlo: la instrucción empieza ya, con las garantías del anexo II del Real Decreto 1026/2024 y medidas cautelares; si la denuncia llegó fuera del Sistema interno de información (un correo a Recursos Humanos, un mando), remítela de inmediato al Responsable del Sistema y comprueba si ha vencido el acuse de recibo; y calcula la prescripción desde la recepción de la denuncia. Las dos cosas (protocolo e instrucción) pueden ir a la vez: el protocolo nuevo se aplica a la denuncia en curso en lo que sea más garantista.
3. **Trabajador denunciante** → comprueba si la empresa activó el protocolo, adoptó medidas cautelares, respetó plazos y le protegió frente a represalias: eso alimenta la tutela o la extinción del contrato.
4. **Trabajador denunciado** → comprueba si se le informó de los hechos, se le oyó, se respetaron los plazos y garantías del propio protocolo y si la sanción respetó la audiencia previa y la prescripción: eso alimenta la impugnación de la sanción o del despido.

| Si lo que se necesita es… | Usa |
|---|---|
| Diseñar el Sistema interno de información de la Ley 2/2023 | `canal-denuncias-informantes` |
| Negociar el plan de igualdad o las medidas planificadas LGTBI | `plan-igualdad-registro-retributivo` |
| Carta de despido del acosador | `carta-despido-disciplinario` |
| Sanción distinta del despido | `sanciones-disciplinarias` |
| Demanda de la víctima sin extinguir el contrato | `tutela-derechos-fundamentales` |
| La víctima quiere extinguir el contrato | `extincion-contrato-trabajador` |
| Requerimiento o acta de la Inspección por acoso | `inspeccion-trabajo-alegaciones` |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

**Para el protocolo:**

1. ★ Plantilla (y si supera cincuenta personas, a efectos del protocolo LGTBI del Real Decreto 1026/2024), centros, turnos, trabajo a distancia, presencia de personal de ETT, contratas en el mismo centro, trato con clientes o público (y si ha habido incidentes de acoso por clientes o por personal de contratas).
2. ★ Representación legal y si el protocolo se va a negociar con ella; plan de igualdad o medidas LGTBI en vigor.
3. ★ Convenio aplicable y su régimen de faltas y sanciones.
4. Evaluación de riesgos vigente y si incluye riesgos psicosociales y, en puestos ocupados por trabajadoras, la violencia sexual.
5. Sistema interno de información de la Ley 2/2023, si existe, y quién es su responsable.
6. Quién puede formar la comisión o persona instructora con imparcialidad (RR. HH., prevención, representantes, asesor externo) y medios para formarla.

**Para una denuncia concreta:**

7. ★ Fecha de recepción, canal (y si entró por el Sistema interno de información o por otra vía) y quién denuncia (la víctima o un tercero con su consentimiento), hechos, fechas, lugares, testigos y pruebas; si la víctima es fija discontinua, cuándo toca su llamamiento.
8. ★ Relación jerárquica entre las personas implicadas, si el denunciado es representante legal, delegado sindical o afiliado conocido por la empresa.
9. ★ Fecha en que la empresa tuvo conocimiento de los hechos (corre la prescripción de las faltas).
10. Medidas cautelares adoptadas, bajas médicas, denuncia penal o ante la Inspección.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la fecha de vigencia.

**A. Obligación de prevenir y de tener procedimiento**

- Todas las empresas, sin umbral, deben promover condiciones que eviten los delitos y conductas contra la libertad sexual y la integridad moral en el trabajo, con especial atención al acoso sexual y por razón de sexo, incluido el digital, y **arbitrar procedimientos específicos** de prevención y de cauce a las denuncias (art. 12.1 de la Ley Orgánica 10/2022; art. 48.1 LO 3/2007; art. 2.1 del Real Decreto 901/2020). Las medidas se negocian con la representación (art. 12.2 LO 10/2022; art. 48.1 LO 3/2007); la representación contribuye a prevenir e informa de lo que conozca (art. 48.2).
- Las medidas alcanzan a toda la plantilla, cualquiera que sea el contrato, y pueden beneficiar a becarias, voluntariado y personal puesto a disposición (art. 12.2 LO 10/2022). El protocolo LGTBI alcanza además a candidatos, proveedores, clientes y visitas (art. 2.4 del Real Decreto 1026/2024): aplica ese ámbito a todo el protocolo.
- La evaluación de riesgos debe incluir la violencia sexual en los puestos ocupados por trabajadoras (art. 12.2 LO 10/2022) y, en general, los riesgos psicosociales que no se hayan podido evitar (art. 16 LPRL; art. 4 del Real Decreto 39/1997). Consulta a los trabajadores (art. 18.2 LPRL) y coordina con las contratas que compartan centro (art. 24 LPRL).
- En empresas de más de cincuenta personas, las medidas planificadas LGTBI deben incluir un protocolo con el contenido mínimo del anexo II, que puede cumplirse con el protocolo general si incluye a las personas LGTBI (art. 8.4 del Real Decreto 1026/2024). Lee el anexo II con `leer_boe` y comprueba que el protocolo recoge: declaración de principios, ámbito, principios y garantías, procedimiento con plazo máximo, informe y resolución.
- El protocolo puede depositarse voluntariamente en el registro de convenios (art. 12 del Real Decreto 901/2020).
- Lo que Jurisprudenciator no devuelve se busca en internet en la fuente oficial y se cita con enlace y fecha de consulta: el Convenio 190 de la OIT sobre violencia y acoso (instrumento de ratificación en el BOE o base oficial de la OIT), el Convenio 158 de la OIT si no se cita a través de la sentencia que lo aplica, y las guías y protocolos modelo del Ministerio de Igualdad, del Instituto de las Mujeres o del Instituto Nacional de Seguridad y Salud en el Trabajo. Las guías orientan la redacción; no son norma y no se citan como tal.

**B. Conductas que cubre**

- Acoso sexual y acoso por razón de sexo: definiciones del art. 7.1 y 7.2 LO 3/2007; siempre son discriminatorios (art. 7.3) y lo es condicionar un derecho a su aceptación (art. 7.4).
- Acoso discriminatorio por cualquiera de las causas de la Ley 15/2022 (art. 6.4 de la Ley 15/2022, de 12 de julio) y por orientación, identidad, expresión de género o características sexuales (letra d) del art. 3 de la Ley 4/2023, de 28 de febrero).
- Acoso laboral o moral: sin definición en el Estatuto; describe la conducta con los elementos que exija la doctrina que leas (reiteración, hostigamiento, finalidad o efecto de degradar) y distínguela del conflicto interpersonal y del ejercicio regular del poder de dirección. El tipo penal del art. 173.1 CP (tercer párrafo) y el acoso sexual del art. 184 CP marcan cuándo los hechos pueden ser delito: el protocolo debe informar a la víctima de la vía penal y, si la denuncia entró por el Sistema interno de la Ley 2/2023, prever su remisión inmediata al Ministerio Fiscal (letra j) del art. 9.2 de esa ley).
- Consecuencias para la empresa: derecho del trabajador a la dignidad y a la protección frente al acoso (letra e) del art. 4.2 ET); el acoso es causa de despido disciplinario (letra g) del art. 54.2 ET); infracciones muy graves de los apartados 11, 13 y 13 bis del artículo 8 del Real Decreto Legislativo 5/2000 (el 13 bis exige que la empresa conociera el acoso y no adoptara medidas).

**C. Procedimiento y garantías que debe tener el protocolo**

- Principios del anexo II del Real Decreto 1026/2024 (aplícalos a todo el protocolo): agilidad con plazos fijados para cada fase, intimidad y dignidad, confidencialidad, protección frente a represalias, contradicción, restitución de la víctima y nulidad de las represalias contra quien denuncia, testifica o colabora. Entre las represalias, pon ejemplos del caso (no llamar en su orden a una persona fija discontinua, no renovar un contrato, cambiar el turno): el art. 36 de la Ley 2/2023 incluye la no renovación.
- Legitimación: la persona afectada o quien ella autorice; si denuncia un tercero, consentimiento expreso e informado de la afectada para iniciar las actuaciones (anexo II).
- Medidas cautelares tras la recepción que separen a la víctima del presunto acosador (anexo II). Criterio de la skill: que el cambio recaiga en el denunciado y no perjudique a la víctima salvo que ella lo pida.
- Instrucción: persona o comisión instructora imparcial y formada, con suplentes por conflicto de interés; entrevistas separadas con acta firmada; el denunciado debe conocer los hechos que se le atribuyen y ser oído (en el Sistema interno de la Ley 2/2023, art. 9.2 letras f) y h) y art. 39); pruebas documentales y testificales; sin mediación ni careo en acoso sexual o por razón de sexo (criterio de la skill).
- Informe con, al menos, descripción de los hechos, metodología, valoración, resultados y medidas cautelares, que concluya si hay o no indicios y, si los hay, proponga el expediente disciplinario (anexo II). El anexo II lo califica de **vinculante** y manda emitirlo en el plazo de días hábiles acordado **desde que se convoca la comisión**: fija ese plazo en días hábiles y di en el protocolo qué vincula (la existencia de indicios) y qué se decide después en el expediente disciplinario (calificación y sanción). Resolución de la empresa: medidas correctoras, protección de la víctima y sanción, o archivo.
- Autor que no trabaja para la empresa (clientes, huéspedes, pacientes, alumnos, proveedores, personal de contratas o de ETT): la empresa no puede sancionarlo, pero el protocolo debe prever el relevo inmediato de la víctima, las medidas frente al cliente (dejar de prestarle el servicio, colaborar con las autoridades), la comunicación de los hechos a la empleadora del autor para que ejerza su poder disciplinario, dentro de la coordinación de actividades (art. 24 LPRL), y el registro de incidentes para la evaluación de riesgos. Si la víctima es de la contrata o de la ETT y el autor de la empresa, se aplica el protocolo completo.
- Sanción: por el régimen del convenio (art. 58.1 ET) y su procedimiento; expediente contradictorio si el denunciado es representante legal o delegado sindical (art. 55.1 y letra a) del art. 68 ET), que en el despido deja al representante la opción si es improcedente (art. 56.4 ET); audiencia a los delegados sindicales si es afiliado conocido (art. 55.1); audiencia previa del trabajador antes del despido disciplinario (doctrina del Pleno de la Sala Cuarta: búscala, ver «Estrategia»). Si el convenio regula esa audiencia (forma, plazo), cúmplela además del expediente contradictorio: la doctrina del Supremo declara improcedente el despido que omite la audiencia exigida por el convenio, sin la excepción temporal de la sentencia del Pleno.
- Prescripción de las faltas: diez, veinte o sesenta días desde que la empresa tuvo conocimiento y, en todo caso, seis meses desde la comisión (art. 60.2 ET). Fija en el protocolo plazos de instrucción compatibles con esos plazos (que el procedimiento completo deje margen al expediente disciplinario) y busca la doctrina sobre cuándo se entiende que la empresa conoce los hechos cuando hay investigación. Esa doctrina retrasa el inicio del cómputo hasta que termina la investigación **prevista en el protocolo**: si la empresa no tenía protocolo o dejó pasar el tiempo sin investigar, no cuentes con ella y calcula desde la recepción de la denuncia. Si el denunciado es fijo discontinuo, comprueba qué dice el convenio de sus periodos de inactividad: el art. 60.2 ET no prevé que suspendan la prescripción, y algunos convenios solo interrumpen por ellos los plazos de reincidencia.
- Relación con la Ley 2/2023: si los hechos pueden ser infracción penal o administrativa grave o muy grave (art. 2.1.b), la denuncia entra en su ámbito y rigen sus garantías (plazos del art. 9, confidencialidad, prohibición de represalias del art. 36, remisión al Ministerio Fiscal de la letra j) del art. 9.2); los conflictos interpersonales quedan fuera de su protección (art. 35.2.b). El acoso sexual es infracción muy grave de la empresa (apartado 13 del art. 8 del Real Decreto Legislativo 5/2000), así que casi toda denuncia de acoso sexual entra. Todo canal interno para esas infracciones se integra en el Sistema interno de información (art. 7.1): el buzón o correo del protocolo es parte del Sistema. La denuncia recibida por otra vía o por personal no responsable se remite de inmediato al Responsable del Sistema (letra g) del art. 9.2), con acuse de recibo en siete días naturales (letra c)). El protocolo debe decir cómo se coordina con el Responsable del Sistema. Sobre la remisión al Fiscal, informa antes a la víctima: el acoso sexual se persigue por su denuncia o por querella del Fiscal (art. 191 CP).
- Confidencialidad frente a derecho de defensa: el denunciado puede reclamar conocer las conclusiones; la identidad de denunciante y testigos se protege. Decide en el protocolo qué se le traslada y cuándo, y comprueba la doctrina de los TSJ sobre esa tensión.

## Estrategia y jurisprudencia

1. **Empresa:** un protocolo sin plazos, sin instructor imparcial o que no se aplica agrava la responsabilidad: redacta solo compromisos que la empresa pueda cumplir y fija plazos concretos. En una denuncia recibida, activa el protocolo de inmediato, documenta cada paso, adopta cautelares y respeta la audiencia del denunciado; no dejes que la instrucción agote los plazos del art. 60.2 ET.
2. **Denunciante:** reúne la prueba de que la empresa conoció los hechos (fecha y canal) y de su respuesta; la falta de activación o de medidas es el núcleo de la reclamación por incumplimiento del deber de protección.
3. **Denunciado:** compara, fase por fase, lo que hizo la empresa con lo que dice su propio protocolo (plazos, traslado de hechos, audiencia, informe) y con la carta de despido: en el juicio la empresa solo puede oponer los motivos de la comunicación escrita (art. 105.2 LRJS).
4. Consultas en Jurisprudenciator (reformula como máximo dos veces; las consultas cortas funcionan mejor):
   - Audiencia previa: `consulta="audiencia previa despido disciplinario artículo 7 Convenio 158 OIT"`, `base="TS"`, `jurisdiccion="SOCIAL"`; lee la del Pleno y la más reciente que la aplique.
     Si el convenio regula la audiencia previa, busca en esos mismos resultados la sentencia que resuelve la audiencia exigida por convenio (su resumen lo dice) y léela: una consulta propia con «convenio colectivo» devuelve resultados ajenos.
   - Garantías del protocolo: `consulta="protocolo acoso garantías denunciado"`, `base="AN"`, `jurisdiccion="SOCIAL"`, `tipo_organo="TSJ"`, `provincia` con la sede de la Sala, `anios=4` (con más palabras el buscador no devuelve nada).
   - Incumplimiento del protocolo: `consulta="incumplimiento protocolo de acoso despido improcedente"`, mismos filtros.
   - Prescripción cuando hay investigación: `consulta="prescripción faltas protocolo acoso investigación"`, mismos filtros; en el Supremo, `consulta="prescripción falta muy grave investigación conocimiento cabal"`, `base="TS"`, `jurisdiccion="SOCIAL"`, `tipo_resolucion="SENTENCIA"` (la consulta genérica sobre «conocimiento empresa» trae resultados ajenos).
   - Carta de despido por acoso (concreción de víctimas y fechas frente a la confidencialidad): `consulta="carta de despido acoso hechos concretos"`, filtros de TSJ.
   - Represalias contra quien denuncia: `consulta="indemnidad denuncia acoso protocolo represalia"`, filtros de TSJ.
   - Acoso sexual y despido: `consulta="acoso sexual despido disciplinario"`, `base="TS"`, `jurisdiccion="SOCIAL"`, `anios=6`.
   - Riesgos psicosociales: `consulta="evaluación riesgos psicosociales acoso laboral obligación empresarial"`, `base="TS"`, `jurisdiccion="SOCIAL"` (casi todo son autos de inadmisión: no los cites como doctrina).
5. Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y transcribe fundamentos, nunca los hechos del acoso ajeno ni nombres de víctimas o testigos (los párrafos que empiezan por el relato de hechos probados o por lo que alega el recurrente no se citan). El protocolo no lleva jurisprudencia; la nota la cita si existe. Si el informe propone un despido, la doctrina sobre audiencia previa es imprescindible (apartado 8 del formato); en una denuncia concreta lo son también la de prescripción y la de represalias.

## Documentos que se entregan

Word maquetado según `references/formato-y-organos-laboral.md`.

**1. Protocolo** — `protocolo-acoso-<empresa>-<AAAAMMDD>.docx`:

1. Declaración de principios y tolerancia cero, firmada por la dirección.
2. Ámbito personal (plantilla, ETT, becarios, voluntariado, contratas, candidatos, clientes, proveedores y visitas), material (conductas del apartado B, también en entornos digitales y fuera del centro con ocasión del trabajo) y temporal.
3. Definiciones con su norma y ejemplos de conductas por tipo.
4. Medidas preventivas: evaluación de riesgos, formación, sensibilización, código de conducta, información a la plantilla y a las contratas.
5. Órganos: persona o comisión instructora, composición, suplencias, formación, incompatibilidades.
6. Principios y garantías del anexo II.
7. Procedimiento: canales de denuncia (integrados en el Sistema interno de información si existe, y remisión inmediata de las denuncias recibidas por otra vía), contenido de la denuncia, acuse de recibo, fase de admisión, medidas cautelares, instrucción, informe (con su plazo en días hábiles desde la convocatoria de la comisión y el alcance de su carácter vinculante), resolución, seguimiento, con un plazo en días para cada fase y uno máximo total; y la actuación cuando el autor no trabaja para la empresa (clientes, proveedores, contratas, ETT).
8. Consecuencias: régimen disciplinario del convenio (artículos leídos y citados con su código), medidas de restitución y apoyo a la víctima, prohibición de represalias, denuncias falsas hechas a sabiendas.
9. Protección de datos: acceso restringido, conservación y deber de sigilo de quienes intervienen.
10. Relación con la Inspección, la jurisdicción social y la penal, sin que el protocolo impida a nadie acudir a ellas.
11. Difusión, vigencia, revisión y seguimiento; negociación o consulta con la representación y fecha.
12. Anexos: formulario de denuncia, modelo de consentimiento del tercero, acta de entrevista, compromiso de confidencialidad.

**Reparto para la redacción rápida:** tres secciones por bloques de apartados: 1-4 (principios, ámbito, definiciones y medidas preventivas) / 5-7 (órganos, garantías y procedimiento con sus plazos, incluido el autor ajeno a la empresa) / 8-12 (consecuencias, datos, relación con otras vías, difusión y anexos). El informe de instrucción modelo, una sola sección.

**2. Informe de instrucción modelo**, si se pide — `informe-instruccion-acoso-<empresa>-<AAAAMMDD>.docx`: referencia del expediente, instructores y declaración de ausencia de conflicto; denuncia y fecha de conocimiento; medidas cautelares; diligencias con fecha (entrevistas, documentos); hechos que se consideran acreditados y no acreditados, cada uno con su prueba; valoración según las definiciones del protocolo; conclusión (indicios o no); propuesta (expediente disciplinario, medidas correctoras, archivo); fecha límite de prescripción calculada con el art. 60.2 ET. Con marcadores (`[PERSONA DENUNCIANTE]`, `[PERSONA DENUNCIADA]`, `[TESTIGO 1]`) y sin datos de salud innecesarios.

**3. Nota para el abogado**, solo si el abogado la pide o si es el único entregable, porque se defiende a la parte para la que esta skill no redacta documento (si no se entrega aparte, lo que esta skill manda «a la nota» va en el resumen de la entrega) — `nota-abogado-protocolo-acoso-<empresa>-<AAAAMMDD>.docx`: artículos leídos, convenio y artículos citados (y de dónde sale el régimen disciplinario si el convenio remite a otro), decisiones de diseño (instructor, cautelares, traslado de conclusiones, carácter vinculante del informe, terceros), doctrina con párrafo literal, riesgos y, en una denuncia concreta, calendario día a día hasta la fecha de prescripción (remisión al Responsable del Sistema, acuse, cautelares, informe, expediente contradictorio, audiencia previa, último día útil para notificar la sanción).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación el art. 12 de la Ley Orgánica 10/2022, los arts. 7 y 48 LO 3/2007, los del ET, la LPRL, la LISOS y la Ley 2/2023 que se citan; el anexo II del Real Decreto 1026/2024 leído con `leer_boe` si la empresa supera cincuenta personas o el protocolo cubre acoso LGTBI.
- [ ] Convenio identificado con su código, faltas y procedimiento sancionador leídos con `leer_convenio` y vigencia comprobada; si remite a un acuerdo estatal del sector, leído el régimen disciplinario de este; modificaciones posteriores registradas en `vigencia_convenio` localizadas y leídas en el boletín (audiencia previa, capítulo LGTBI).
- [ ] Cada fase del procedimiento con plazo concreto y compatible con el art. 60.2 ET; en una denuncia concreta, fecha límite de prescripción calculada con fecha inicial y precepto (desde la recepción si no había protocolo), y comprobado si la denuncia llegó fuera del Sistema interno y si venció el acuse de recibo.
- [ ] El protocolo prevé cómo actuar cuando el autor es un cliente, un proveedor o personal de una contrata o de una ETT.
- [ ] Cada ECLI citado leído con `leer_sentencias` (fundamentos, sin hechos ajenos) o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero) y corregido lo que señale.
- [ ] Marcadores en lugar de nombres, sin datos personales de víctimas ni testigos.
- [ ] Lo obtenido en internet (convenios de la OIT, guías oficiales) citado con enlace y fecha de consulta y señalado en el resumen.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y para quién, plazos con precepto, documentos que faltan y riesgos, tabla de jurisprudencia y próximo paso.
