---
name: reclamacion-cantidad
description: >-
  Prepara la reclamación de cantidad laboral por el procedimiento ordinario o el monitorio (LRJS arts.
  80-101): salarios impagados, diferencias de convenio o de categoría, horas extraordinarias y su prueba
  sin registro de jornada, pagas extra, vacaciones no disfrutadas al extinguirse el contrato y
  liquidación. Cuadro de desglose mes a mes, filtro de prescripción de un año (art. 59 ET), interés por
  mora del art. 29.3 ET, FOGASA y acceso a suplicación (arts. 191-192 LRJS). Para el trabajador, la
  demanda o la petición monitoria; para la empresa reclamada, la nota de riesgo con cálculo
  contradictorio y oferta. Úsala con «me deben nóminas», «diferencias salariales», «horas extra»,
  «finiquito mal pagado», «nos reclaman cantidad». Si el trabajador quiere además irse por los impagos,
  extincion-contrato-trabajador; si solo hay que revisar un finiquito, finiquito-liquidacion.
---

# Reclamación de cantidad

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Salario, pago puntual, mora, pagas extra, compensación y absorción y prescripción** → `buscar_articulo` (`ley="ET"`, artículos `"4"`, `"26"`, `"29"`, `"31"` y `"59"`); interrupción de la prescripción → (`ley="CC"`, `articulo="1973"`); interés de las deudas no salariales → (`ley="CC"`, `articulo="1108"`).
- **Jornada, registro, horas extraordinarias, vacaciones y funciones superiores** → `buscar_articulo` (`ley="ET"`, artículos `"34"`, `"35"`, `"38"` y `"39"`).
- **Salario mínimo del año reclamado, si el pactado o el de convenio queda por debajo** → `buscar_boe` (real decreto de salario mínimo de cada año) + `leer_boe`; si no lo devuelven, en internet en el BOE (punto 3 de la puerta); nunca la cuantía de memoria.
- **Procedimiento, prueba, sentencia, recurso y FOGASA** → `buscar_articulo` (`ley="LRJS"`, artículos `"23"`, `"25"`, `"26"`, `"64"`, `"80"`, `"90"`, `"91"`, `"94"`, `"99"`, `"101"`, `"191"` y `"192"`) y (`ley="ET"`, `articulo="33"`).
- **Doctrina sobre el interés del art. 29.3 ET y sobre la prueba de las horas extraordinarias sin registro** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`, consultas de «Estrategia») + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión).
- **Convenio aplicable y sus artículos** (estructura salarial, pluses, pagas, precio de la hora extra, jornada anual, vacaciones, clasificación) → `buscar_convenio` + `leer_convenio` + `vigencia_convenio` de cada periodo reclamado; la **tabla salarial del año** no la devuelve el conector, y muchos convenios fijan también en ella el **precio de la hora extraordinaria** o de los festivos: búscala en internet en el boletín oficial (texto del convenio o revisión salarial publicada), cítala con su enlace y, si no aparece, pídela al abogado (anclas, apartado 3). Si `leer_convenio` devuelve solo el título de un artículo, léelo en el mismo boletín. **Interés por mora del convenio**: busca si el convenio lo regula o lo mejora (`leer_convenio` con `buscar_en="interés por mora"` o `"reclamaciones de cantidad"`, o en el índice del texto oficial).
- **Empresa** → `buscar_empresa_mercantil` (estado, concurso, disolución); edictos concursales recientes → `novedades_boe` (`contiene` = denominación de la empresa).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Esta skill también está en el plugin de litigación laboral. En este plugin la usa el despacho que asesora a la empresa y además lleva sus despidos y reclamaciones, o que defiende al trabajador. **Pregunta primero a quién defiende el abogado**:

- **Trabajador**: demanda de cantidad por el procedimiento ordinario o petición monitoria, con la relación laboral viva o extinguida.
- **Empresa reclamada** (papeleta o demanda recibida, requerimiento monitorio): nota de riesgo con cálculo contradictorio concepto a concepto, excepciones (prescripción, compensación y absorción, naturaleza extrasalarial, pago), prueba que hay que llevar y oferta. Si recibe un requerimiento monitorio, tiene diez días para pagar u oponerse por escrito motivado (art. 101.a LRJS): calcula la fecha y dilo en la primera línea de la nota.

| Situación | Skill |
|---|---|
| Aún no se ha intentado la conciliación (salvo monitorio, exento: art. 64.1 LRJS) | `papeleta-conciliacion` |
| Despido en los últimos veinte días hábiles | `redactar-demanda-despido`, acumulando las cantidades vencidas y exigibles (art. 26.3 LRJS) |
| Impagos o retrasos graves y el trabajador quiere extinguir el contrato | `extincion-contrato-trabajador` (admite acumular la cantidad: art. 26.3) |
| Solo revisar o calcular un finiquito | `finiquito-liquidacion` |
| Auditoría del registro de jornada o preparación de la prueba de horas | `registro-jornada-horas-extra`, y vuelve aquí para la demanda |
| Dudas sobre qué convenio se aplica | `convenio-aplicable` |
| Diferencia retributiva por sexo u otra causa discriminatoria | `tutela-derechos-fundamentales` o `plan-igualdad-registro-retributivo` |
| Discrepancia sobre la fecha de disfrute de las vacaciones | modalidad propia de los arts. 125 y 126 LRJS (urgente y sin recurso), no esta skill |

## Datos que hay que reunir antes de redactar

No redactes al primer disparo: si falta un dato imprescindible (★), pregúntalo.

1. ★ A quién defiende el abogado; si la relación sigue viva o, si se extinguió, la fecha.
2. ★ Cada concepto reclamado con su periodo: salario, complementos, pagas extra, horas extraordinarias, vacaciones, diferencias de convenio o de categoría, otros devengos.
3. ★ Nóminas del periodo (devengado y percibido) y contrato; vida laboral si hay dudas de antigüedad.
4. ★ Convenio aplicable y, si se reclaman diferencias de convenio, **la tabla salarial publicada de cada año**: búscala en internet (revisión salarial en el BOE, el boletín autonómico o el BOP; `vigencia_convenio` dice qué publicaciones hay) y cítala con su enlace; si no aparece, pídela al abogado con boletín y fecha. Sin tabla no se calculan diferencias: la tarea se detiene en ese punto.
5. ★ Horas extraordinarias: registro de jornada o, si no lo hay, cuadrantes, correos, mensajes, geolocalización, fichajes, testigos; si el horario era fijo y prefijado o seguía patrones irregulares; si se compensaron con descanso.
6. ★ Fecha de presentación de la papeleta y del acto; reclamaciones extrajudiciales o reconocimientos de deuda previos (fecha y soporte).
7. ★ Empresa exacta; indicios de insolvencia o concurso.
8. Funciones superiores: periodo, funciones realizadas y grupo profesional del convenio (art. 39.3 ET; acumulación del art. 26.4 LRJS).
9. Si defiende a la empresa: pagos hechos, nóminas firmadas, registro de jornada, conceptos que considera absorbibles y cuánto está dispuesta a ofrecer.
10. Si reclaman varios trabajadores lo mismo: nexo de título o causa de pedir para acumular (art. 25.3 LRJS) y cuantía para el recurso según el art. 192.1 LRJS; si afecta a toda la plantilla, valora la afectación general (art. 191.3.b).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde».

**Qué es salario.**
- Salario es la totalidad de las percepciones por la prestación de servicios; no lo son las indemnizaciones o suplidos por gastos, las prestaciones de la Seguridad Social ni las indemnizaciones por traslados, suspensiones o despidos (art. 26.1 y 26.2 ET). La calificación decide el interés aplicable, la garantía del FOGASA y la cotización: califica cada concepto en el cuadro y, si es discutido, lee el artículo del convenio que lo crea.
- Compensación y absorción: operan cuando lo realmente abonado, en su conjunto y cómputo anual, es más favorable (art. 26.5 ET). Es la primera defensa de la empresa en diferencias de convenio; la doctrina exige homogeneidad de conceptos: búscala antes de aceptarla o rechazarla.
- Dos pagas extraordinarias al año, cuantía por convenio, prorrateables si el convenio lo permite (art. 31 ET). Salario mínimo del año como suelo (art. 27 ET), leyendo el real decreto de cada año.

**Pago, mora e intereses.**
- Pago puntual y documentado, periodos de hasta un mes (art. 29.1 ET y art. 4.2.f ET).
- Interés por mora del diez por ciento de lo adeudado en el pago del salario (art. 29.3 ET). Lee la doctrina vigente antes de fijar su régimen en la demanda: la Sala Cuarta lo aplica con carácter objetivo a las deudas estrictamente salariales y reserva para las no salariales el interés del art. 1108 del Código Civil; el día inicial es aquel en que la obligación debió cumplirse. Si el convenio mejora el tipo, pide el del convenio con cita literal de su artículo y, subsidiariamente, el del art. 29.3 ET. Liquida el interés en el cuadro solo con la base, el día inicial y el tipo que resulten de la doctrina y del convenio leídos; si alguno es dudoso (por ejemplo, un tipo del convenio de redacción ambigua), pídelo en el suplico sin liquidar y explica la duda en la nota.

**Prescripción (art. 59.1 y 59.2 ET).** Un año desde que cada cantidad pudo exigirse: las nóminas prescriben mes a mes. Filtra el cuadro antes de sumar y lista lo que queda fuera. Interrumpen: la papeleta (art. 65.1 LRJS), la reclamación extrajudicial y el reconocimiento de deuda (art. 1973 CC), con prueba de fecha. **Frente al FOGASA**, la reclamación extrajudicial y el reconocimiento de deuda no interrumpen, salvo el reconocimiento ante el servicio administrativo de conciliación (art. 23.5 LRJS): si hay riesgo de insolvencia, no dejes correr plazos confiando en burofaxes.

**Horas extraordinarias.** Son las que exceden la jornada máxima ordinaria; se pagan en la cuantía del convenio o contrato, nunca por debajo de la hora ordinaria, o se compensan con descanso (sin pacto, dentro de los cuatro meses siguientes); límite anual y registro con totalización y copia en el recibo (art. 35 ET). Registro diario de jornada con inicio y fin, conservado cuatro años (art. 34.9 ET). La doctrina más reciente de la Sala Cuarta distingue según hubiera un horario prefijado o patrones irregulares, y atribuye a la empresa que no lleva el registro la carga de probar la jornada real en determinados casos: léela y aplica lo que diga. En la demanda, detalla día a día o semana a semana las horas (cuadrante como documento), porque la precisión de lo alegado es presupuesto de esa regla. Comprueba el mínimo del art. 35.1 ET con cifras: valor de la hora ordinaria = salario anual (con las pagas extra) / jornada anual del convenio; si el precio del convenio es inferior, se reclama al valor de la hora ordinaria. Comprueba también si el convenio o el contrato pactan la compensación con descanso: sin pacto de compensación y con precio fijado en el convenio, corresponde el pago.

**Convenio vencido.** Si el convenio está denunciado o fuera de su vigencia inicial y no hay texto ni revisión salarial posterior en `vigencia_convenio`, lee su cláusula de denuncia y ultraactividad (y, en su defecto, el art. 86 ET) antes de aplicar la última tabla publicada a los meses posteriores, y advierte en la nota del riesgo de un convenio nuevo con tablas retroactivas.

**Vacaciones.** No sustituibles por compensación económica, mínimo de treinta días naturales; reglas de coincidencia con incapacidad temporal y límite de dieciocho meses (art. 38 ET). Su pago en dinero se reclama al extinguirse el contrato o en los supuestos que admita la doctrina: búscala antes de pedirlo con la relación viva.

**Funciones superiores.** Derecho a la retribución de las funciones efectivamente realizadas (art. 39.3 ET); la reclamación de clasificación profesional admite acumular las diferencias (art. 26.4 LRJS).

**Procedimiento.**
- Ordinario, con conciliación previa (arts. 63 y 80 LRJS). La sentencia debe fijar la cantidad sin reservarla para ejecución (art. 99): el suplico lleva el total líquido y el desglose.
- Monitorio para cantidades vencidas, exigibles y de cuantía determinada, frente a empresarios que no estén en concurso y hasta el límite del art. 101 LRJS, con desglose de conceptos, cuantías y periodos y documentos de principio de prueba; exento de conciliación (art. 64.1). Si hay oposición, sigue el ordinario.
- Acumulación: cuantas acciones tenga contra el mismo demandado (art. 25.1 LRJS); con varios trabajadores, si hay nexo de título o causa de pedir (art. 25.3).
- Prueba: diligencias de preparación al menos diez días antes del juicio (art. 90.3 LRJS); documentos en poder de la empresa (nóminas, registro de jornada, registro retributivo) con el apercibimiento de tener por probadas las alegaciones de la contraria (art. 94.2); interrogatorio con el apercibimiento del art. 91.2.

**Recurso.** Sin suplicación si la cuantía litigiosa no excede de la cifra del art. 191.2.g LRJS, salvo afectación general (art. 191.3.b). La cuantía se fija por la reclamación mayor si hay varios demandantes y sumando las pretensiones de un mismo actor, sin intereses ni recargos (art. 192.1 y 192.2). Dilo al cliente antes de presentar: puede ser un pleito a instancia única.

**FOGASA.** Abona salarios reconocidos en conciliación o resolución judicial, con los límites que fija el art. 33.1 ET (léelos: no escribas la cifra de memoria). Cítalo como parte si la empresa está en concurso, es insolvente o ha desaparecido (art. 23.2 LRJS).

## Estrategia y jurisprudencia

**Si defiende al trabajador.**
1. Construye primero el cuadro (mes · concepto · devengado según convenio o contrato · percibido · diferencia · naturaleza salarial o no · prescrito sí o no) y luego la demanda.
2. Reclama cada concepto con su fuente: artículo del convenio con su código, tabla del año facilitada, nómina concreta.
3. Elige vía: monitorio si la deuda es clara, documentada, dentro del límite y la empresa no está en concurso; ordinario si hay debate de fondo (categoría, horas, absorción).
4. Si los impagos son graves y continuados, advierte de la vía del art. 50.1.b ET (`extincion-contrato-trabajador`): léelo con `buscar_articulo`, porque fija cuándo se entiende que hay retraso y cuántas mensualidades adeudadas en un año o meses de retraso bastan, y di en la nota si el caso llega ya a esos umbrales.

**Si defiende a la empresa.**
1. Recalcula: prescripción mes a mes, tabla del año correcto, compensación y absorción, conceptos extrasalariales, horas compensadas con descanso, pagos acreditados.
2. Revisa si tiene registro de jornada conforme al art. 34.9 ET: sin él, la carga de la prueba de la jornada puede recaer sobre la empresa.
3. Cuantifica el riesgo con intereses y propón pagar lo no discutido cuanto antes, porque el interés corre desde el vencimiento.

**Consultas** (reformula dos veces como máximo; lee solo lo que vayas a citar, `parrafos=3`, y transcribe fundamentos, nunca hechos ni datos de las partes):
- Mora: `consulta="interés por mora diez por ciento artículo 29.3 conceptos salariales"`, `base="TS"`, `anios=3`; día inicial: `consulta="día inicial devengo interés por mora artículo 29.3"`.
- Horas: `consulta="horas extraordinarias carga de la prueba registro diario de jornada artículo 34.9"`, `base="TS"`, `anios=3`; aplicación en la sede: `base="AN"`, `tipo_organo="TSJ"`, `provincia` = sede de la Sala.
- Absorción: `consulta="compensación y absorción conceptos homogéneos diferencias salariales convenio"`, `base="TS"`.
- Vacaciones: `consulta="vacaciones no disfrutadas compensación económica extinción del contrato"`, `base="TS"`.

## Documentos que se entregan

**1. Demanda** (`demanda-cantidad-<apellido-cliente>-<AAAAMMDD>.docx`) o **petición monitoria** (`peticion-monitoria-<apellido-cliente>-<AAAAMMDD>.docx`), si defiende al trabajador, maquetada según el apartado 2 del formato:
1. Encabezamiento al Tribunal de Instancia de `[SEDE]`, Sección de lo Social; demandante con marcadores; `[DENOMINACIÓN SOCIAL]` y `[CIF]` comprobados; FOGASA si procede. Modalidad: procedimiento ordinario (o proceso monitorio del art. 101 LRJS).
2. HECHOS: relación laboral (antigüedad, categoría o grupo, convenio con su código, salario y estructura); conceptos adeudados con remisión al cuadro; prueba de las horas; reclamaciones extrajudiciales; conciliación previa (fechas y resultado), salvo monitorio.
3. FUNDAMENTOS: competencia (art. 2.a, art. 6 y art. 10.1 LRJS); conciliación previa (arts. 63 y 65 LRJS) o exención (art. 64.1); fondo (arts. 4.2.f, 26, 29 y el que toque del ET, y el artículo del convenio con su código); interés del art. 29.3 ET con la doctrina leída; horas y registro (arts. 34.9 y 35 ET, doctrina leída); FOGASA (art. 33 ET, art. 23 LRJS).
4. SUPLICO: condena a pagar `[TOTAL]` €, desglosado por conceptos, más el interés del art. 29.3 ET sobre los salariales (y el del art. 1108 CC sobre los que no lo sean), con la responsabilidad del FOGASA en su caso.
5. OTROSÍES: diligencias de preparación y documental en poder de la empresa (arts. 90.3 y 94.2 LRJS), interrogatorio (art. 91.2), testifical para las horas.

**2. Cuadro de desglose** como tabla en el mismo Word y como documento numerado (`calculo-cantidades-<apellido-cliente>-<AAAAMMDD>.docx`, con los datos de partida, cada operación y los días iniciales del interés): mes · concepto · fuente (artículo del convenio o nómina) · debido · percibido · diferencia · salarial sí/no · prescrito sí/no; totales por concepto y total general. Comprueba las sumas dos veces.

**3. Nota** (`nota-cantidad-<empresa>-<AAAAMMDD>.docx`): cantidades prescritas y por qué; acceso a suplicación con la cuantía calculada según el art. 192 LRJS; riesgos de prueba; para la empresa, el cálculo contradictorio, las excepciones con su soporte y la oferta.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos en esta conversación ET 26, 29 y 59 y los que se citen (4, 27, 31, 34, 35, 38, 39); CC 1973 y 1108 si se usan; LRJS 80, 99, 191 y 192 (y 101 en monitorio).
- [ ] Convenio con su código y vigencia en cada periodo reclamado (ultraactividad comprobada si está vencido); diferencias y precio de la hora extraordinaria calculados solo con la tabla salarial citada con su enlace o aportada por el abogado (boletín y fecha), y comparados con el valor de la hora ordinaria.
- [ ] Buscado en el convenio si regula o mejora el interés por mora; si lo mejora, pedido con carácter principal y el del art. 29.3 ET como subsidiario.
- [ ] Salario mínimo de cada año leído en su real decreto, si se usa.
- [ ] Empresa comprobada con `buscar_empresa_mercantil`; concurso descartado antes de elegir el monitorio.
- [ ] Prescripción filtrada mes a mes, con las interrupciones acreditadas y la advertencia del art. 23.5 LRJS si hay riesgo de insolvencia.
- [ ] Cuadro con cada operación visible y sumas comprobadas; interés liquidado solo con la doctrina leída.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre cada documento; el aviso de «posible disonancia» sobre el art. 29 ET (su título es «Liquidación y pago») contrastado con el apartado 3 leído; los artículos de convenio comprobados con `leer_convenio`, no con el verificador.
- [ ] Marcadores en lugar de datos no facilitados; ninguna cifra de salario mínimo, límite del FOGASA o umbral de recurso escrita sin haberla leído.
- [ ] Los datos obtenidos en internet (tabla salarial, salario mínimo si hizo falta) figuran con su enlace en el documento y en el resumen.
- [ ] Resumen para el abogado según el apartado 9 del formato.
