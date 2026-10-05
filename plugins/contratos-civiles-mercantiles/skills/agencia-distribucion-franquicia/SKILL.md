---
name: agencia-distribucion-franquicia
description: >-
  Redacta contratos de agencia comercial, distribución (exclusiva, selectiva, concesión) y franquicia
  (individual o máster), con su nota para el abogado en Word. Úsala cuando el abogado diga «contrato
  de agente comercial», «comisionista», «distribuidor en exclusiva», «concesionario», «red de
  distribución», «franquicia», «dossier de información precontractual», «indemnización por clientela»,
  «pacto de no competencia» o «preaviso». Califica la relación, ajusta territorio y exclusiva,
  remuneración o cánones, objetivos, precios de reventa, no competencia, duración, preaviso e
  indemnizaciones según defienda al fabricante o franquiciador o al agente, distribuidor o
  franquiciado, y comprueba los límites del Derecho de la competencia. Para una venta sin red ni
  exclusiva, usa compraventa-mercantil; para una licencia de marca sin sistema de negocio,
  licencia-cesion-propiedad-intelectual.
---

# Agencia, distribución y franquicia

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Agencia** → `buscar_articulo` (`ley="Ley 12/1992"`, artículos `"1"` a `"31"` que se usen, uno por uno; como mínimo `"1"`, `"2"`, `"3"`, `"11"`, `"12"`, `"13"`, `"20"`, `"21"`, `"25"`, `"26"`, `"28"`, `"29"`, `"30"` y `"31"`).
- **Franquicia, marca, saber hacer y secretos** → `buscar_articulo` (`ley="Ley 7/1996"`, `articulo="62"`; `ley="RD 201/2010"`, artículos `"2"`, `"3"` y `"4"`; `ley="Ley 17/2001"`, `articulo="48"`; `ley="BOE-A-2019-2364"`, artículos `"1"` y `"3"`).
- **Derecho de la competencia** → `buscar_articulo` (`ley="Ley 15/2007"`, artículos `"1"` y `"5"`) y el Reglamento (UE) 2022/720 de exención de acuerdos verticales (`ley="32022R0720"`, artículos `"1"`, `"2"`, `"3"`, `"4"`, `"5"` y `"11"`; si no responde, localízalo con `buscar_boe`, `consulta="Reglamento (UE) 2022/720 acuerdos verticales"`, y usa el CELEX que devuelva).
- **Distribución (contrato atípico) y contrato internacional** → `buscar_articulo` (`ley="CC"`, artículos `"1101"`, `"1106"`, `"1124"`, `"1152"`, `"1154"`, `"1255"`, `"1256"` y `"1258"`; `ley="CCom"`, artículos `"50"` y `"57"`) y, si las partes están en Estados distintos, (`ley="32008R0593"`, artículos `"3"` y `"4"`; `ley="32012R1215"`, `articulo="25"`).
- **Doctrina** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; `base="AN"` + `tipo_organo="AP"` si no hay doctrina del Supremo o se litigará en esa plaza; `base="TJUE"` para la Directiva de agentes comerciales) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Concurso de una de las partes** → `buscar_articulo` (`ley="TRLC"`, `articulo="156"`).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (existencia, estado, administradores y apoderados vigentes, concurso; en franquicia, contrasta los datos del franquiciador con los del dossier).
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Cita con fecha: «artículo N de la Ley 12/1992, de 27 de mayo, sobre Contrato de Agencia», «artículo N del Real Decreto 201/2010, de 26 de febrero», «artículo 62 de la Ley 7/1996, de 15 de enero, de Ordenación del Comercio Minorista», «artículo N de la Ley 15/2007, de 3 de julio, de Defensa de la Competencia». `verificar_escrito` no identifica el Reglamento (UE) 2022/720 ni los demás reglamentos de la Unión (atribuye su artículo a la última ley española nombrada): comprueba cada artículo europeo con `buscar_articulo` e ignora ese veredicto. No cites el Reglamento de memoria: si el conector no lo devuelve, léelo en internet en EUR-Lex (CELEX 32022R0720) y cítalo con enlace y fecha de consulta.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Contrato con un agente comercial que promueve (y quizá concluye) ventas por cuenta de un fabricante o proveedor.
- Contrato de distribución: el distribuidor compra y revende en su nombre, con o sin exclusiva territorial, o como miembro de una red selectiva; concesión.
- Contrato de franquicia individual, máster franquicia o precontrato de franquicia, y el documento de información precontractual.

Antes de redactar, **califica la relación** (el nombre que le den las partes no decide):

| Hechos | Calificación y régimen |
|---|---|
| Promueve operaciones por cuenta ajena, de forma continuada, cobra por ello y no asume el riesgo salvo pacto (art. 1 de la Ley 12/1992) | Agencia: régimen imperativo de la Ley 12/1992 (art. 3.1) |
| No puede organizar su actividad ni su tiempo con sus propios criterios, o está vinculado por relación laboral común o especial (art. 2 de la Ley 12/1992) | No es agente: deriva al plugin laboral (skill `falso-autonomo-trade` de contratos laborales, si está instalado) y no redactes un contrato de agencia |
| Compra en firme y revende en su nombre y a su riesgo | Distribución: contrato atípico (arts. 1255 y 1258 CC; arts. 50 y 57 CCom), con aplicación analógica de la Ley 12/1992 solo si hay identidad de razón |
| Explota el sistema de negocio de otro con marca o rótulo común, saber hacer propio, sustancial y singular, y asistencia continuada (art. 62.1 de la Ley 7/1996; art. 2.1 del Real Decreto 201/2010) | Franquicia; si solo hay distribución exclusiva, licencia de fabricación o cesión de marca o rótulo, no es franquicia (art. 2.3 y 2.4 del Real Decreto 201/2010) |
| Encargo aislado de una operación | No es agencia (falta la relación continuada o estable): valora `prestacion-servicios` |

| Situación | Skill que procede |
|---|---|
| Venta o suministro sin exclusiva ni integración en red | `compraventa-mercantil` |
| Solo licencia de marca, patente o software | `licencia-cesion-propiedad-intelectual` |
| Intercambio de información antes de negociar | `confidencialidad-nda` |
| Revisar o contestar el borrador de la otra parte | `revision-contrato-semaforo` o `negociacion-contrapropuesta` |
| El contrato ya se ha extinguido o se quiere romper: calcular y reclamar indemnizaciones | `dictamen-interpretacion-contrato`, `resolucion-por-incumplimiento` o `requerimiento-cumplimiento` |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ Tipo de relación según los hechos (cuadro anterior) y a quién defiende el abogado: fabricante, proveedor o franquiciador, o agente, distribuidor o franquiciado.
2. ★ Partes y Estado de establecimiento de cada una (si difieren, contrato internacional).
3. ★ Productos o servicios, territorio, grupo de clientes y canales (tienda física, venta en línea, grandes cuentas reservadas).
4. ★ Exclusividad: a favor de quién, en qué territorio o clientela, y si hay obligación de no vender productos competidores durante el contrato.
5. ★ Retribución: comisión (base, porcentaje, devengo, pago) o fijo en agencia; precios de compra, márgenes, *rappels* y objetivos en distribución; canon de entrada, *royalties* y canon de publicidad en franquicia.
6. ★ Duración, prórroga y preaviso deseados; qué pasa al final (existencias, clientes, marca, local, datos).
7. ★ Pacto de no competencia posterior al contrato: si se quiere, alcance, duración y contraprestación.
8. ★ Cuota de mercado aproximada del proveedor y del comprador en su mercado de referencia (si no se conoce, dilo en la nota como riesgo de competencia).
9. Precios de reventa: si el proveedor quiere recomendar precios o fijar máximos.
10. Marca (titularidad y registro), manual de operaciones, formación, asistencia y controles de calidad.
11. En franquicia: fecha de entrega del documento de información precontractual y de cualquier pago previo; previsiones de ventas entregadas y su base.
12. Garantías (aval, depósito), seguros, objetivos mínimos y consecuencias de no alcanzarlos.
13. Si el contrato puede regirse por un Derecho civil propio: pregunta y, si aplica, busca la norma con `buscar_boe`; si no aparece, aplica la puerta.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota su línea de vigencia.

**Agencia (Ley 12/1992, de 27 de mayo).** Sus preceptos son imperativos salvo que dispongan otra cosa (art. 3.1).

- Actuación: subagentes solo con autorización expresa (art. 5); concluir operaciones en nombre del empresario solo si se le atribuye esa facultad (art. 6). Deberes del agente (art. 9) y del empresario, que debe aceptar o rechazar la operación comunicada en quince días (art. 10).
- Remuneración: fija, comisión o mixta (art. 11); comisión por operaciones concluidas durante el contrato, incluidas las de su zona o grupo exclusivo aunque no intervenga (art. 12); por operaciones posteriores a la extinción en los supuestos y plazos del art. 13; relación trimestral de comisiones y derecho a verificar la contabilidad (art. 15); pago no más tarde del último día del mes siguiente al trimestre (art. 16); pérdida de la comisión solo en el caso del art. 17; sin reembolso de gastos salvo pacto (art. 18); el pacto *del credere* exige forma escrita y comisión expresa (art. 19).
- No competencia posterior: máximo dos años desde la extinción y un año si el contrato se pactó por tiempo menor (art. 20.2); por escrito, limitada a la zona o grupo confiados y a los bienes o servicios del contrato (art. 21).
- Duración y extinción: indefinido si no se fija plazo (art. 23); el de plazo determinado que se sigue ejecutando se transforma en indefinido (art. 24); preaviso escrito de un mes por año de vigencia con máximo de seis, y de un mes el primer año; pueden pactarse plazos mayores, pero el del agente no puede ser inferior al del empresario (art. 25); extinción inmediata por incumplimiento o concurso de la otra parte (art. 26). Lee también el art. 156 del texto refundido de la Ley Concursal (la declaración de concurso no es causa de resolución y se tienen por no puestas las cláusulas que la prevean) y explica en la nota cómo se relaciona con el art. 26 si el contrato lo menciona.
- Indemnizaciones: por clientela si concurren los requisitos del art. 28.1, con el límite del art. 28.3; de daños por inversiones no amortizadas en la denuncia del contrato indefinido (art. 29); supuestos en que no se deben (art. 30); prescripción de un año desde la extinción (art. 31). La Sala Primera declara nulas las cláusulas que excluyen o limitan la indemnización por clientela y rechaza su moderación: no las redactes aunque defiendas al empresario; lee la doctrina y explícalo en la nota.

**Distribución.** Es atípica: rige lo pactado dentro de los arts. 1255, 1256 y 1258 CC. Doctrina que debes localizar y leer antes de redactar la terminación: la indemnización por clientela del art. 28 de la Ley 12/1992 no se aplica automáticamente; solo por analogía cuando se prueba que el distribuidor creó una clientela que aprovecha el proveedor (no la fidelidad a la marca); en el contrato indefinido cabe la denuncia con preaviso razonable, y la falta de preaviso se indemniza conforme a los arts. 1101 y 1106 CC, con la analogía del art. 29 para inversiones no amortizadas si se prueban. La indemnización pactada como precio de la desvinculación se ha aplicado sin moderar. Por eso, en distribución, pacta expresamente preaviso, recompra de existencias y compensación (o su exclusión, si defiendes al proveedor, dentro de lo que admita la doctrina leída).

**Franquicia.**

- Concepto (art. 62.1 de la Ley 7/1996; art. 2.1 y 2.2 del Real Decreto 201/2010) y exclusiones (art. 2.3 y 2.4).
- Información precontractual por escrito, veraz y no engañosa, con veinte días hábiles de antelación a la firma del contrato o precontrato o a cualquier pago (art. 3 del Real Decreto 201/2010; art. 62.2 de la Ley 7/1996), con el contenido de las letras a) a g), y previsiones de ventas basadas en experiencias o estudios suficientemente fundamentados (letra e). El franquiciador puede exigir confidencialidad sobre esa información (art. 4). Deja constancia firmada de la fecha de entrega y del contenido.
- Registro de franquiciadores: el art. 62 vigente de la Ley 7/1996 (léelo) no menciona el registro, pero el conector devuelve los arts. 5 y siguientes del Real Decreto 201/2010 como vigentes. La norma que dio al art. 62 su redacción vigente (la indica `buscar_articulo`) suprimió el registro y, en su disposición derogatoria, derogó el capítulo III del Real Decreto 201/2010: compruébalo en internet en el texto de esa norma en el BOE y en el consolidado del Real Decreto, cítalos con enlace y fecha de consulta, y no exijas ni menciones como vigente la comunicación al registro.
- Saber hacer: propio, sustancial y singular (art. 2.1.b del Real Decreto 201/2010); protégelo como secreto empresarial con medidas razonables (art. 1 de la Ley 1/2019) y con la cláusula de confidencialidad, cuya infracción hace ilícito su uso (art. 3.2).
- Marca: licencia exclusiva o no, sin sublicencia salvo pacto, con acciones del titular frente al licenciatario que infrinja límites del contrato (art. 48 de la Ley 17/2001).

**Derecho de la competencia.** Están prohibidos y son nulos los acuerdos que restrinjan la competencia, entre ellos la fijación de precios o el reparto de mercados (art. 1.1 y 1.2 de la Ley 15/2007), salvo exención (art. 1.3) o cumplimiento de un reglamento de exención de la Unión, aunque no afecte al comercio entre Estados (art. 1.4). Con el Reglamento (UE) 2022/720 leído:

- Exención de los acuerdos verticales (art. 2) si las cuotas del proveedor y del comprador no superan el 30 % (art. 3).
- Restricciones especialmente graves que hacen perder la exención (art. 4): fijar precios de reventa (se admiten recomendados o máximos), ciertas restricciones territoriales o de clientela, e impedir el uso efectivo de internet.
- Restricciones excluidas (art. 5): no competencia durante el contrato indefinida o superior a cinco años (salvo local del proveedor, art. 5.2) y no competencia posterior salvo que cumpla las condiciones del art. 5.3 (bienes competidores, limitada al local, indispensable para proteger el saber hacer, máximo un año).
- Comprueba su vigencia (art. 11) antes de citarlo. Si las cuotas se desconocen o se superan, o hay una restricción grave, dilo en la nota como riesgo de nulidad y recomienda análisis específico de competencia; no lo resuelvas con cláusulas de estilo.

**Contrato internacional.** A falta de elección, la franquicia se rige por la ley de la residencia habitual del franquiciado y la distribución por la del distribuidor (art. 4.1.e y 4.1.f del Reglamento Roma I, `32008R0593`); la agencia no tiene letra propia en el art. 4.1, así que pacta siempre la ley aplicable (art. 3) en lugar de discutir si encaja en la prestación de servicios (art. 4.1.b) o en la regla del art. 4.2. Si el agente actúa en otro Estado de la Unión, busca la doctrina del Tribunal de Justicia sobre la Directiva de agentes comerciales antes de elegir ley y fuero.

**Tributación.** Avisa de que el abogado debe comprobar el IVA y, en su caso, las retenciones de comisiones, cánones y *royalties* (y su tratamiento si hay pagador extranjero) con `buscar_consultas_hacienda`; no des tipos.

## Cláusulas clave y jurisprudencia

Consultas con `jurisdiccion="CIVIL"` y `base="TS"` salvo indicación; lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar.

| Cláusula | Si defiendes al fabricante, proveedor o franquiciador | Si defiendes al agente, distribuidor o franquiciado | Qué buscar |
|---|---|---|---|
| Calificación | Distribución o servicios si los hechos lo sostienen; asunción real del riesgo por la otra parte | Agencia si promueve por cuenta ajena sin riesgo (régimen imperativo favorable) | `consulta="contrato de agencia o distribución calificación asunción del riesgo reventa en nombre propio"` |
| Territorio y exclusiva | Exclusiva condicionada a objetivos; reserva de grandes cuentas y de ventas en línea dentro de lo que permite el art. 4 del Reglamento | Exclusiva plena; comisión por operaciones en su zona (art. 12.2 de la Ley 12/1992); protección frente a ventas activas de otros | Arts. 4 del Reglamento (UE) 2022/720 y 12 de la Ley 12/1992 |
| Precios de reventa y venta en línea | Precios recomendados o máximos; criterios de calidad para la venta en línea | Libertad de precio y de venta en línea | `consulta="franquicia fijación de precios de reventa nulidad derecho de la competencia"` |
| No competencia durante el contrato | Hasta cinco años o la duración del local del proveedor | Duración limitada y liberación si se pierde la exclusiva | Art. 5 del Reglamento (UE) 2022/720 |
| No competencia posterior | Agencia: hasta dos años (art. 20); franquicia y distribución: un año, local y saber hacer (art. 5.3 del Reglamento) | Limitarla al mínimo, con contraprestación; en agencia, tenerla en cuenta para la indemnización por clientela (art. 28.1) | `consulta="franquicia pacto de no competencia postcontractual"`; `consulta="contrato de agencia pacto de limitación de la competencia artículo 20"` |
| Duración y preaviso | Plazo determinado sin prórroga tácita (evita el art. 24); en distribución, preaviso pactado y tasado | Preaviso largo; en agencia, nunca inferior al del art. 25 | `consulta="contrato de distribución duración indefinida preaviso razonable indemnización inversiones no amortizadas"`; `consulta="contrato de agencia preaviso artículo 25 indemnización falta de preaviso"` |
| Indemnización por clientela | Agencia: no la excluyas (es nula); documenta clientela preexistente. Distribución: exclusión o compensación tasada, advirtiendo del riesgo | Agencia: cálculo con el límite del art. 28.3. Distribución: reconocimiento expreso o criterios de cálculo | `consulta="contrato de agencia renuncia anticipada a la indemnización por clientela carácter imperativo"`; `consulta="contrato de distribución indemnización por clientela aplicación analógica Ley de Agencia"`; TJUE: `consulta="agente comercial indemnización por clientela Directiva 86/653"`, `base="TJUE"` |
| Información precontractual (franquicia) | Acuse firmado de entrega con fecha y contenido; previsiones con su base documental | Revisión del dossier y de las previsiones; derecho a resolver o a indemnización si la información no fue veraz | `consulta="franquicia información precontractual previsiones de ventas error vicio del consentimiento"`, `base="AN"`, `tipo_organo="AP"`; `consulta="franquicia deber de información precontractual dolo error anulación"` |
| Terminación y efectos | Cese inmediato de marca y rótulo, recompra opcional de existencias, entrega de datos de clientes (con base de protección de datos) | Recompra obligatoria de existencias y amortización de inversiones exigidas | Arts. 29 de la Ley 12/1992 y 1101 y 1106 CC; doctrina de la fila «Duración y preaviso» |

Reglas para la nota:

- La indemnización por clientela, la aplicación analógica a la distribución, el preaviso y los pactos de no competencia están en el apartado 8 del formato: cita en la nota el párrafo literal de la resolución leída, con órgano, fecha y ECLI; si tras dos reformulaciones no hay resolución aplicable, aplica la puerta.
- Si la resolución interpreta el Reglamento (UE) 330/2010, anterior, dilo y contrasta su criterio con el texto vigente del Reglamento (UE) 2022/720 antes de trasladarlo.
- Cita la doctrina del Tribunal de Justicia solo para interpretar la Ley 12/1992 en lo que transpone la Directiva, indicando el asunto y el ECLI europeo que devuelva el conector.

## Documentos que se entregan

Dos documentos Word maquetados según `references/formato-y-entrega-contratos.md` (y un tercero en franquicia si se pide):

1. `contrato-agencia-…`, `contrato-distribucion-…` o `contrato-franquicia-<parte-principal>-<AAAAMMDD>.docx`.
2. `nota-<tipo>-<parte-principal>-<AAAAMMDD>.docx`.
3. En franquicia, si el abogado defiende al franquiciador y lo pide: `informacion-precontractual-franquicia-<franquiciador>-<AAAAMMDD>.docx`, con los apartados a) a g) del art. 3 del Real Decreto 201/2010 y el acuse de recibo con fecha.

Estructura del contrato:

1. REUNIDOS e INTERVIENEN; EXPONEN: actividad de cada parte, marca y sistema (franquicia), independencia de la otra parte y, en franquicia, fecha de entrega de la información precontractual.
2. PRIMERA.- Definiciones (Productos, Territorio, Clientes reservados, Marca, Saber hacer, Manual).
3. SEGUNDA.- Objeto y calificación: agencia, distribución o franquicia, con las obligaciones que la caracterizan.
4. TERCERA.- Territorio, exclusiva y canales (incluida la venta en línea).
5. CUARTA.- Obligaciones de cada parte (promoción, información, suministro, formación, asistencia, controles).
6. QUINTA.- Retribución: comisiones y su devengo y liquidación (agencia); precios, condiciones de compra y objetivos (distribución); cánones (franquicia).
7. SEXTA.- Precios de reventa: solo recomendados o máximos.
8. SÉPTIMA.- Marca, saber hacer, manual y confidencialidad.
9. OCTAVA.- No competencia durante el contrato.
10. NOVENA.- Duración, prórroga y preaviso.
11. DÉCIMA.- Resolución por incumplimiento (no pactes la resolución por la sola declaración de concurso: el art. 156 del texto refundido de la Ley Concursal la tiene por no puesta; en agencia, ver el art. 26 de la Ley 12/1992 y la regla anterior).
12. UNDÉCIMA.- Efectos de la extinción: existencias, clientes, marca, rótulo, datos, indemnizaciones (con el régimen que corresponda).
13. DUODÉCIMA.- No competencia posterior (si se pacta).
14. DECIMOTERCERA.- Protección de datos, cesión y subagentes o subfranquicias.
15. DECIMOCUARTA.- Notificaciones, negociación previa, ley aplicable y fuero o arbitraje.
16. DECIMOQUINTA.- Integridad y modificaciones por escrito.
17. Cierre, firmas y ANEXOS: productos y tarifas, territorio (mapa o lista), objetivos, manual (índice), acuse de la información precontractual.

**Reparto para la redacción rápida:** una sección por bloque de estipulaciones (`### [ESTIPULACION]`): comparecencia, expositivos y definiciones / objeto y calificación, territorio, exclusiva y obligaciones de las partes / retribución, precios de reventa, marca, saber hacer y no competencia durante el contrato / duración, preaviso, resolución, efectos de la extinción, indemnizaciones y no competencia posterior / datos, cesión, notificaciones, ley y fuero, integridad, firmas y anexos. La nota: apartado 11 del formato.

La nota sigue el apartado 3 del formato e incluye siempre: calificación con sus hechos, régimen imperativo aplicable, análisis de competencia (cuotas, restricciones graves, no competencia), indemnizaciones previsibles a la extinción y documentos pendientes (registro de la marca, dossier firmado, cuotas de mercado).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Relación calificada por los hechos; si hay dependencia laboral, derivada y no redactada como agencia.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos citados de la Ley 12/1992, la Ley 7/1996, el Real Decreto 201/2010, la Ley 17/2001, la Ley 1/2019, la Ley 15/2007, el CC y el CCom; el Reglamento (UE) 2022/720 leído con su CELEX (y su vigencia, art. 11) en el conector o, si no respondió, en EUR-Lex con enlace y fecha de consulta.
- [ ] Agencia: sin cláusulas que excluyan o limiten la indemnización por clientela; preaviso no inferior al del art. 25; no competencia dentro de los arts. 20 y 21.
- [ ] Distribución y franquicia: sin fijación de precios de reventa ni restricciones graves del art. 4; no competencia dentro del art. 5; cuotas de mercado conocidas o señaladas como riesgo.
- [ ] Franquicia: fecha de entrega de la información precontractual acreditada con al menos veinte días hábiles de antelación; registro de franquiciadores comprobado en el BOE consolidado (internet, con enlace) o discrepancia señalada, sin afirmar la obligación de memoria.
- [ ] Lo que no dio Jurisprudenciator y se obtuvo en internet, citado con enlace y fecha de consulta desde fuente oficial y señalado en el resumen; ninguna sentencia citada sin `buscar_por_cita` y `leer_sentencias`.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); los avisos sobre reglamentos de la Unión resueltos con `buscar_articulo`; cada «posible disonancia» contrastada con el apartado leído.
- [ ] Sociedades comprobadas con `buscar_empresa_mercantil`; firmantes con cargo o poder vigentes.
- [ ] Marcadores en lugar de datos inventados; territorio, porcentajes, objetivos, plazos y anexos coherentes.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, calificación, cláusulas críticas, riesgos de competencia, datos que faltan, tabla de jurisprudencia, plazos con su precepto (preaviso, no competencia, prescripción del art. 31) y próximo paso.
