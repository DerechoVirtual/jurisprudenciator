---
name: carta-despido-objetivo
description: >-
  Prepara para la empresa la carta de despido por causas objetivas (arts. 52 y 53 ET): ineptitud, falta de
  adaptación, causas económicas, técnicas, organizativas o de producción por debajo de los umbrales del despido
  colectivo, o insuficiencia de consignación en entidades sin ánimo de lucro; con la puesta a disposición de la
  indemnización, el preaviso, la copia a la representación y, si la pides, una nota con el cálculo. Úsala con «despido objetivo»,
  «despido por causas económicas», «amortizar el puesto», «carta de despido por pérdidas», «20 días por año». Revisa
  también, para el trabajador, una carta recibida. Si se alcanzan los umbrales, usa despido-colectivo-empresa; si la
  medida es temporal, erte-suspension-reduccion; si la causa es la conducta, carta-despido-disciplinario.
---

# Carta de despido objetivo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Causas objetivas y definición de las causas económicas, técnicas, organizativas y de producción** → `buscar_articulo` (`ley="ET"`, artículos `"52"` y `"51"`).
- **Requisitos formales, nulidad y efectos** → `buscar_articulo` (`ley="ET"`, artículos `"53"` y `"56"`) y (`ley="LRJS"`, artículos `"120"`, `"121"`, `"122"` y `"123"`).
- **Concreción de la causa en la carta** → `buscar_sentencias` (`consulta="despido objetivo carta concreción causa expresiones genéricas indefensión"`, `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`, `terminos="carta concreción causa indefensión"`).
- **Error excusable y falta de liquidez** → `buscar_sentencias` (`consulta="error excusable cálculo indemnización despido objetivo"` y `consulta="falta de liquidez puesta a disposición indemnización despido objetivo carga de la prueba"`, `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`).
- **Umbrales y cómputo de extinciones en 90 días** → `buscar_sentencias` (`consulta="despido colectivo umbrales cómputo noventa días extinciones computables"` y `consulta="fraude de ley despidos objetivos periodos sucesivos noventa días umbrales despido colectivo"`, `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias`.
- **Plazo del trabajador, inhábiles y desempleo** → `buscar_articulo` (`ley="LRJS"`, artículos `"121"`, `"103"`, `"43"`, `"63"` y `"65"`), (`ley="ET"`, `articulo="59"`: el art. 121 LRJS dice «veinte días» y el carácter hábil lo dan el art. 59.3 ET y el art. 103.1 LRJS) y (`ley="LGSS"`, `articulo="267"`). Los festivos autonómicos y locales de la sede del órgano no los da el conector: léelos en internet en el boletín oficial (decreto de fiestas de la comunidad y resolución de fiestas locales de la provincia) y cítalos con enlace.
- **Convenio aplicable y sus artículos** → `buscar_convenio` (`consulta` con el nombre del sector tal como lo usa el registro y `territorio` = provincia del centro) + `leer_convenio` (`buscar_en="despido"` o `buscar_en="preaviso"` para localizar exigencias propias; después `articulo="N"`). Después, `vigencia_convenio` de cada convenio que uses: **`leer_convenio` devuelve el texto publicado originalmente, no las modificaciones posteriores**. Si `vigencia_convenio` registra un **texto nuevo del convenio** (sustituye entero al que has leído), una modificación, un acuerdo parcial o un pronunciamiento de tribunal posterior a esa publicación y anterior a la decisión, búscalo en internet en el boletín oficial (BOE, boletín autonómico o BOP) y comprueba si cambia los artículos que aplicas; cítalo con su enlace (punto 3 de la puerta). `buscar_boe`, `sumario_boe` y `novedades_boe` no localizan los convenios (sección III): búscalo en internet por su denominación y el periodo de vigencia en el dominio del boletín y lee el texto directamente. Si no lo localizas, dilo en la nota.
- **Empresa y grupo** → `buscar_empresa_mercantil` (denominación, CIF y vínculos que obliguen a contar la plantilla o las extinciones del grupo).
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

Primera pregunta: **¿a quién defiende el abogado?**

- **Empresa**: quiere extinguir uno o pocos contratos por una causa objetiva. Entregas carta, justificante de la puesta a disposición y copia para la representación, con el cálculo y los riesgos en el resumen (y una nota, si la pides).
- **Trabajador**: ha recibido la carta y quiere saber si aguanta. Entregas una nota de revisión con los defectos, su efecto (improcedencia o nulidad), las diferencias que se reclaman y el plazo; la papeleta y la demanda, con `papeleta-conciliacion` y `redactar-demanda-despido`.

| Situación | Skill que procede |
|---|---|
| Las extinciones, sumadas en 90 días, alcanzan los umbrales del art. 51.1 ET | `despido-colectivo-empresa` (ni una carta objetiva más) |
| La causa es coyuntural y basta suspender o reducir jornada | `erte-suspension-reduccion` |
| Cabe una alternativa menos gravosa (traslado, cambio de funciones, modificación) | `movilidad-geografica-funcional` o `modificacion-sustancial-condiciones` |
| El motivo real es la conducta del trabajador | `carta-despido-disciplinario` |
| Cálculos complejos (tramos anteriores al 12/02/2012, salario discutido) | `calculo-indemnizacion-despido` |
| Finiquito | `finiquito-liquidacion` |
| No se sabe qué convenio se aplica | primero `convenio-aplicable` |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ A quién defiende el abogado.
2. ★ Causa y hechos concretos:
   - **Ineptitud**: en qué consiste, desde cuándo, cómo se acredita, y si ya existía antes de superar el periodo de prueba.
   - **Falta de adaptación**: qué modificación técnica, cuándo se introdujo, qué curso se ofreció y cuándo terminó.
   - **Económica**: pérdidas actuales o previstas (cifras y ejercicios) o disminución de ingresos o ventas trimestre a trimestre frente a los mismos trimestres del año anterior; documentación contable y fiscal.
   - **Técnica, organizativa o de producción**: qué cambio, cuándo, y por qué sobra precisamente este puesto.
   - **Entidad sin ánimo de lucro**: contrato indefinido, plan o programa público, consignación y su insuficiencia.
3. ★ Plantilla de la empresa (y del grupo si hay vínculos) y extinciones por motivos no inherentes a la persona en los 90 días anteriores y previstas en los 90 siguientes, con su causa (incluidos mutuos acuerdos y bajas incentivadas).
4. ★ Condición del trabajador: representante legal o delegado sindical (prioridad de permanencia), y situaciones del art. 53.4 ET (embarazo, suspensión por nacimiento o cuidado, permisos del art. 37 o adaptación del art. 34.8 solicitados o en disfrute, excedencia del art. 46.3, reincorporación en los doce meses siguientes al nacimiento, víctima de violencia de género o sexual).
5. ★ Fecha prevista de entrega de la carta y de extinción (preaviso) o decisión de abonar el preaviso.
6. ★ Antigüedad real (contratos anteriores, sucesión de empresa), nóminas de los últimos doce meses y tipo de contrato y jornada.
7. ★ Liquidez para pagar la indemnización en el acto; si se alega falta de liquidez, qué prueba la acredita (saldos, descubiertos, embargos).
8. ★ Existencia de representación legal de los trabajadores (para la copia en la causa de la letra c).
9. Convenio colectivo o actividad real y provincia del centro.
10. **Solo trabajador**: la carta, fechas de entrega y de efectos, importe recibido y cómo, y si se le dio el preaviso o se le abonó.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**1. Causas (art. 52 ET).**
- **a) Ineptitud** conocida o sobrevenida tras la colocación efectiva; la anterior al cumplimiento del periodo de prueba no puede alegarse después.
- **b) Falta de adaptación** a modificaciones técnicas razonables: la empresa debe haber ofrecido antes un curso (tiempo de trabajo efectivo y retribuido) y no puede extinguir hasta que pasen al menos dos meses desde la modificación o desde el fin de la formación. Comprueba las dos fechas.
- **c) Causas del art. 51.1 ET** por debajo de los umbrales. Económicas: situación económica negativa, con pérdidas actuales o previstas o disminución persistente de ingresos o ventas; es persistente si durante tres trimestres consecutivos cada trimestre queda por debajo del mismo trimestre del año anterior (léelo en el art. 51.1 y haz la tabla trimestre a trimestre). Técnicas, organizativas y productivas: cambios en los medios, en los métodos o en la demanda. Los representantes tienen prioridad de permanencia (art. 52.c y art. 68.b ET).
- **e) Entidades sin ánimo de lucro**: contratos indefinidos concertados directamente para planes y programas públicos sin dotación estable, por insuficiencia de la consignación.
- Para la causa c), además de acreditarla, explica en la carta la conexión entre la causa y la amortización de ese puesto: es lo que discuten los juzgados.

**2. Umbrales: ¿es un despido colectivo encubierto?** Construye la tabla de extinciones en la ventana de 90 días (anteriores y posteriores): despidos objetivos por la letra c) y demás extinciones por iniciativa del empresario por motivos no inherentes a la persona distintos del fin de contrato del art. 49.1.c ET, que se suman si son al menos cinco (art. 51.1 ET). Lee la doctrina sobre qué extinciones computan (la Sala Cuarta ha contado mutuos acuerdos surgidos a iniciativa de la empresa en un contexto de reducción de plantilla) y sobre cómo se encadenan las ventanas de 90 días. Si se alcanzan los umbrales, para y deriva a `despido-colectivo-empresa`. Si en ventanas sucesivas de 90 días se fracciona para no alcanzarlos sin causas nuevas, las extinciones son nulas por fraude (art. 51.1, último párrafo, ET y art. 122.2 LRJS).

**3. Requisitos formales (art. 53.1 ET).**
- **Comunicación escrita expresando la causa.** La doctrina de la Sala Cuarta exige que el trabajador conozca de forma suficiente la causa para defenderse en igualdad; reproducir las expresiones genéricas del art. 51 ET no basta. En la causa económica, pon las cifras, los ejercicios o trimestres y la fuente; en las demás, el cambio concreto y su efecto sobre el puesto.
- **Puesta a disposición simultánea** a la entrega de la carta de la indemnización de veinte días por año de servicio, prorrateándose por meses los periodos inferiores al año, con un máximo de doce mensualidades. Simultánea significa en el mismo acto: transferencia ordenada ese día con justificante o cheque entregado con la carta.
- **Excepción por falta de liquidez**: solo si la causa es económica (art. 52.c) y se hace constar en la carta. La doctrina exige a la empresa probar, además de la mala situación económica, la falta concreta de liquidez en ese momento. Si no hay prueba específica, no la uses.
- **Preaviso de quince días** desde la entrega de la comunicación hasta la extinción; en la causa c), copia del escrito a la representación legal de los trabajadores. Durante el preaviso, licencia retribuida de seis horas semanales para buscar empleo (art. 53.2 ET).

**4. Consecuencias de los defectos (art. 53.4 ET y art. 122 LRJS).** Sin causa acreditada o sin los requisitos del art. 53.1, improcedencia. Excepción: no conceder el preaviso o el **error excusable** en el cálculo de la indemnización no determinan la improcedencia, pero obligan a pagar los salarios del preaviso o la diferencia. Lee la doctrina sobre qué error es excusable: la Sala Cuarta valora de dónde viene el error (por ejemplo, la antigüedad que figuraba en nómina frente a una unidad de vínculo apreciada después) y su entidad. Para la empresa: calcula con la antigüedad real y documenta el origen de cada dato.

**5. Nulidad (art. 53.4 ET y art. 122.2 LRJS).** Nula si el móvil es discriminatorio o lesiona derechos fundamentales, en los supuestos objetivos de las letras a), b) y c) del art. 53.4 (dato 4) y en el fraude de umbrales. En los supuestos objetivos, para que sea procedente hay que acreditar que la causa requiere concretamente la extinción del contrato de esa persona: explícalo en la carta (por qué ese puesto y no otro, si hay alguien más en funciones equivalentes y por qué no hay recolocación) y di que la situación protegida no ha intervenido. En la nota, advierte de que el resultado alternativo es la nulidad, no la improcedencia, y señala las alternativas que el trabajador alegará (formación, cambio de puesto, movilidad funcional) para que la empresa las documente o las ofrezca antes de entregar la carta. Si aparece una nota «Téngase en cuenta» con otra redacción de la letra b), compara las dos y, para la empresa, trata como protegidos los supuestos de ambas.

**6. Efectos (art. 53.5 ET y art. 123 LRJS).** Procedente: la indemnización del art. 53.1 y situación legal de desempleo (art. 267.1.a.4.º LGSS). Improcedente: los efectos del art. 56 ET (33 días por año, tope de 24 mensualidades), descontando lo percibido si se opta por indemnizar o reintegrándolo si se readmite; los salarios de tramitación no se compensan con los del preaviso. Nula: readmisión y salarios.

**7. Plazo del trabajador (art. 121 LRJS).** Veinte días hábiles desde el día siguiente a la fecha de extinción; puede demandar ya desde que recibe la carta. Cobrar la indemnización o usar la licencia no supone conformidad (art. 121.2 LRJS). Agosto y del 24 de diciembre al 6 de enero cuentan (art. 43.4 LRJS: extinciones del art. 52 ET). Papeleta previa obligatoria, que suspende el plazo (arts. 63 y 65 LRJS).

## Estrategia y jurisprudencia

**Empresa.** Ordena el trabajo así: tabla de umbrales → causa acreditable con documentos → conexión causa-puesto → persona protegida o representante → cálculo con antigüedad real → forma de pago simultáneo → preaviso o su abono → copia a la representación. Si falla la causa o la documentación, di en la nota que el riesgo de improcedencia es alto y cuantifícalo.

**Trabajador.** Revisa en este orden: supuesto del art. 53.4 o móvil lesivo (nulidad); fraude de umbrales (nulidad); carta genérica; indemnización no puesta a disposición o no simultánea; falta de liquidez alegada sin prueba; error inexcusable en el cálculo; causa no acreditada o sin conexión con el puesto; preaviso no dado (salarios); copia a la representación omitida.

**Consultas en Jurisprudenciator** (reformula como máximo dos veces; `anios=5` primero):

- Las de la lista para carta, error excusable, liquidez y umbrales.
- Causa concreta: `consulta="despido objetivo causas <económicas|organizativas|productivas> razonabilidad conexión puesto amortización"`, `base="TS"`, y la misma con `base="AN"`, `tipo_organo="TSJ"` y la `provincia` de la sede de la Sala.
- Ineptitud o falta de adaptación: `consulta="despido objetivo ineptitud sobrevenida"` o `consulta="despido objetivo falta de adaptación modificaciones técnicas curso"`, `base="TS"`.
- Copia a la representación: `consulta="despido objetivo copia representantes trabajadores omisión"`, `base="TS"` (la Sala Cuarta ha admitido la entrega posterior en un plazo prudencial, nunca previa a la carta: entrégala el mismo día, después).
- Persona protegida del art. 53.4 ET (dato 4): `consulta="despido objetivo trabajadora con reducción de jornada por guarda legal causa requiere concretamente la extinción de su contrato"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia` sede de la Sala, `anios=5` (con `base="TS"` esta consulta devuelve sobre todo despidos colectivos y autos de inadmisión).

Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que cites; transcribe párrafos de fundamentos, nunca los hechos ni datos de las partes. La jurisprudencia va en la nota, nunca en la carta.

## Cálculo (con cada operación visible; en la nota si se entrega, si no en el resumen)

| Concepto | Dato | Fuente |
|---|---|---|
| Salario bruto anual real (12 meses, prorrata de pagas y complementos salariales) | `[importe]` | nóminas |
| Salario diario (anual / 365) | | |
| Antigüedad hasta la fecha de extinción: años y meses completos (prorrateo por meses) | | contrato, vida laboral |
| Indemnización objetiva: 20 días × años (+ fracción mensual) × salario diario | | art. 53.1.b ET |
| Tope: 12 mensualidades | | art. 53.1.b ET |
| Preaviso no concedido: días que falten hasta 15 × salario diario | | art. 53.1.c ET |
| Escenario de improcedencia: 33 días por año, tope 24 mensualidades, menos lo ya pagado | | art. 56.1 ET y art. 53.5.b ET |

Si la antigüedad es anterior al 12/02/2012, el escenario de improcedencia necesita los dos tramos de la disposición transitoria undécima del ET. Pídela con `buscar_articulo` (`ley="ET"`, `articulo="disposición transitoria undécima"`); es un límite conocido del conector que no la devuelva (anclas, apartado 7). En ese caso léela en internet en el texto consolidado del BOE (https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430, disposición transitoria undécima) y cítala con el enlace y la fecha de consulta. Puedes apoyar el método de cálculo en la sentencia de la Sala Cuarta que aplica esas reglas (`consulta="cálculo indemnización despido improcedente antigüedad anterior 12 febrero 2012 disposición transitoria 720 días"`, `base="TS"`, `jurisdiccion="SOCIAL"`) si la lees. Calcula cada tramo por separado, con su prorrateo por meses (si quedan fracciones de mes y no has leído doctrina que fije cómo se computan, da los dos resultados: solo meses completos y fracción como mes completo), y aplica el tope de 720 días o, si el primer tramo lo supera, el de ese tramo con el máximo de 42 mensualidades. Solo si tampoco en internet aparece el texto, aplica la puerta y deriva el cálculo a `calculo-indemnizacion-despido`. La indemnización objetiva (20 días) no tiene tramos.

Reducción de jornada por cuidado de menor o familiar (apartados 4 in fine, 5, 6 y 8 del art. 37 ET) o ejercicio a tiempo parcial de los permisos de nacimiento o parental: la indemnización (la de 20 días y la de la improcedencia) se calcula con el salario que correspondería **sin la reducción**, mientras no haya vencido su plazo máximo (disposición adicional decimonovena del ET). El conector no devuelve las disposiciones adicionales: léela en internet en el texto consolidado del BOE y cítala con enlace. Pide el salario a jornada completa (o calcúlalo con el porcentaje de reducción).

## Documentos que se entregan

Todo en Word según `references/formato-y-organos-laboral.md`.

1. **Carta de despido objetivo** — `carta-despido-objetivo-<apellido-trabajador>-<AAAAMMDD>.docx`:
   - Membrete (`[DENOMINACIÓN SOCIAL]`, `[CIF]`), destinatario (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`), lugar y fecha, asunto.
   - Decisión de extinguir al amparo de la letra que proceda del art. 52 del Estatuto de los Trabajadores.
   - Causa: hechos concretos, cifras y periodos, documentos que la acreditan y conexión con el puesto; en supuestos del art. 53.4, por qué la causa requiere concretamente esta extinción.
   - Indemnización: importe, cálculo resumido (salario diario, antigüedad, días) y forma de puesta a disposición simultánea; o declaración motivada de falta de liquidez si la causa es económica y se puede probar.
   - Preaviso: fecha de extinción a quince días o más de la entrega, o abono de los días de preaviso; licencia de seis horas semanales.
   - Fecha de efectos, liquidación y documentación para el desempleo.
   - Firma, recibí fechado o constancia de negativa ante dos testigos.
   - **Reparto para la redacción rápida:** carta de 2-4 páginas: una sola sección, sin equipo; si la causa económica lleva muchas cifras, dos: encabezamiento, causa y conexión con el puesto / indemnización, preaviso, efectos y firma. El justificante y la copia a la representación, una sección cada uno.
2. **Justificante de la puesta a disposición** (orden de transferencia del mismo día o recibí del cheque) — `justificante-puesta-disposicion-<apellido-trabajador>-<AAAAMMDD>.docx` — y **copia para la representación legal** con acuse, en la causa c) — `carta-copia-representacion-<apellido-trabajador>-<AAAAMMDD>.docx`, con la información que exija el convenio (muchos piden informar de los despidos a la representación).
3. **Nota para el abogado**, solo si el abogado la pide (si no, lo que esta skill manda «a la nota» —calendario, riesgos, cálculos y jurisprudencia con su ECLI— va en el resumen de la entrega) — `nota-despido-objetivo-<empresa>-<AAAAMMDD>.docx`: tabla de umbrales en 90 días; acreditación de la causa (tabla trimestral si es económica); comprobación de cada requisito del art. 53.1; riesgos de nulidad e improcedencia; cálculo en tabla; jurisprudencia literal sobre la concreción de la carta y la que sostenga la causa; plazo del trabajador con fechas.

Para el trabajador: **nota de revisión** — `nota-revision-despido-objetivo-<apellido-trabajador>-<AAAAMMDD>.docx`, con defectos, efecto, jurisprudencia literal, diferencias reclamables en tabla y plazo (fecha de extinción, precepto, fecha final).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: ET 51, 52, 53, 56 y 59; LRJS 43, 103, 120, 121, 122 y 123; LGSS 267; festivos de la sede leídos en el boletín oficial; revisada la nota «Téngase en cuenta» del art. 53.4. Convenio con vigencia comprobada y modificaciones posteriores al texto leído localizadas en el boletín oficial (o señaladas como pendientes).
- [ ] Tabla de umbrales en 90 días hecha con las extinciones computables y doctrina leída; si se alcanzan, tarea derivada.
- [ ] Causa acreditada con documentos y conectada con el puesto; en la económica, cifras y trimestres en la carta.
- [ ] Indemnización calculada con salario real y antigüedad real (salario sin reducir si hay reducción de jornada por cuidado, disposición adicional decimonovena leída en el BOE), puesta a disposición simultánea documentada, o falta de liquidez probada; escenario de improcedencia con la disposición transitoria undécima si la antigüedad es anterior al 12/02/2012.
- [ ] Preaviso de quince días o su abono; copia a la representación en la causa c).
- [ ] Doctrina sobre concreción de la carta, error excusable y liquidez leída cuando se usa.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; la carta no lleva jurisprudencia.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero); citas con «la letra c) del artículo 52 del Estatuto de los Trabajadores», no «52.c)».
- [ ] Marcadores en vez de datos inventados; cálculo visible.
- [ ] Resumen para el abogado según el apartado 9 del formato.
