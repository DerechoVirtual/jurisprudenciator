---
name: teletrabajo-acuerdo
description: >-
  Redacta en Word el acuerdo de trabajo a distancia de la Ley 10/2021 con su contenido mínimo, la
  compensación de gastos, el control empresarial y la reversibilidad, más la política de desconexión digital
  y, si la pides, una nota de riesgos. Úsala cuando la empresa diga «vamos a teletrabajar dos días a la semana», «¿tengo
  que pagar los gastos de teletrabajo?» o «quiero que vuelva a la oficina», y cuando el trabajador pregunte
  «¿me pueden obligar a volver?», «no me pagan internet ni la luz» o «me han puesto un programa de control».
  Comprueba el umbral de regularidad del art. 1, la voluntariedad, el convenio y la doctrina sobre cláusulas
  nulas. Sirve a empresa y trabajador. Si el teletrabajo se pide para conciliar (art. 34.8 ET), usa
  permisos-conciliacion-adaptacion; para el registro horario en general, registro-jornada-horas-extra.
---

# Acuerdo de trabajo a distancia (Ley 10/2021)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Ámbito, voluntariedad, forma, contenido mínimo y modificación** → `buscar_articulo` (`ley="BOE-A-2021-11472"`, artículos `"1"`, `"2"`, `"3"`, `"4"`, `"5"`, `"6"`, `"7"` y `"8"`). **Trampa del número**: con `ley="Ley 10/2021"` puede salir una ley autonómica; usa el identificador BOE y comprueba el título de la respuesta.
- **Derechos y obligaciones** → `buscar_articulo` (`ley="BOE-A-2021-11472"`, artículos `"9"` a `"22"`: medios `"11"`, gastos `"12"`, horario `"13"`, registro `"14"`, prevención `"15"` y `"16"`, intimidad `"17"`, desconexión `"18"`, control `"22"`).
- **Remisiones del Estatuto** → `buscar_articulo` (`ley="ET"`, artículos `"13"`, `"20"`, `"20 bis"` y `"34"` —apartados 8 y 9—).
- **Protección de datos y derechos digitales** → `buscar_articulo` (`ley="LOPDGDD"`, artículos `"87"`, `"88"`, `"89"`, `"90"` y `"91"`).
- **Reclamación judicial y sanción** → `buscar_articulo` (`ley="LRJS"`, artículos `"138 bis"` y `"139"`) y (`ley="BOE-A-2000-15060"`, `articulo="7"`; la cuantía, del `"40"` en el momento).
- **Convenio aplicable y sus artículos** → `buscar_convenio` + `leer_convenio` (`buscar_en="teletrabajo"` y, por separado, `"trabajo a distancia"` y `"desconexión"`) + `vigencia_convenio`: el convenio puede fijar la compensación de gastos, la reversibilidad y los criterios de acceso. Los pasajes de `buscar_en` salen cortados: en cuanto localices el artículo que regula el trabajo a distancia, léelo entero con `leer_convenio` (`articulo="N"`), porque los importes, el preaviso y los requisitos suelen estar al final. Elige el convenio por la actividad principal real de la empresa (su ámbito funcional), aunque el cliente crea que es otro. Si `vigencia_convenio` muestra revisiones salariales o actas de la comisión paritaria posteriores al texto, la compensación de gastos puede estar actualizada en ellas y `leer_convenio` no las devuelve: búscalas en el BOE o el boletín oficial (punto 3 de la puerta) y cita el importe vigente con su enlace.
- **Doctrina sobre cláusulas del acuerdo, gastos, presencialidad, averías y control** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; `base="AN"`, que incluye la Sala de lo Social de la Audiencia Nacional en conflictos colectivos; o `base="AN"` + `tipo_organo="TSJ"` + `provincia` sede de la Sala) + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión).
- **Revisión del documento antes de entregarlo** → cada redactor pasa `verificar_escrito` sobre las frases de su sección que citan normas (no sobre el documento entero) y el ensamblado de `redaccion-rapida` comprueba que cada ECLI o ROJ citado figure entre las fuentes leídas; `buscar_por_cita` solo para una sentencia que aporte el abogado y no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). En los documentos, cita «artículo 7 de la Ley 10/2021, de 9 de julio, de trabajo a distancia» y «artículo 88 de la Ley Orgánica 3/2018, de 5 de diciembre»: así los reconoce `verificar_escrito`.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Pregunta primero **a quién defiende el abogado**:

- **Empresa**: implantar o documentar el trabajo a distancia de una o varias personas, fijar la compensación de gastos, el control y la vuelta a la presencialidad, o revisar acuerdos ya firmados.
- **Trabajador**: saber si tiene derecho a acuerdo, reclamar los gastos, oponerse a una vuelta a la oficina impuesta, impugnar una cláusula o un sistema de control, o pedir el acceso al trabajo a distancia que reconozca el convenio.

| Situación | Skill |
|---|---|
| El trabajador pide teletrabajar para conciliar (adaptación del art. 34.8 ET) | `permisos-conciliacion-adaptacion` (procedimiento del art. 139 LRJS) |
| Registro de jornada, horas extra y descansos en general | `registro-jornada-horas-extra` |
| La empresa cambia unilateralmente condiciones distintas del acuerdo (por la vía del art. 41 ET) | `modificacion-sustancial-condiciones` (el acuerdo no puede imponerse ni modificarse por esa vía) |
| Traslado a otro centro o ciudad ligado a la vuelta a la presencialidad | `movilidad-geografica-funcional` |
| Contrato nuevo con teletrabajo desde el inicio | `contrato-trabajo-modalidad` (el acuerdo va como anexo) |
| Despido o sanción por negarse al teletrabajo o por pedir la reversión | `redactar-demanda-despido` o `sanciones-disciplinarias`, con este análisis |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ A quién defiende el abogado.
2. ★ **Porcentaje de jornada a distancia** en un periodo de tres meses y distribución (días fijos, flexibles, semanas alternas). Con él decides si la Ley 10/2021 es obligatoria.
3. ★ Tipo de contrato y edad: menores y contratos formativos tienen un mínimo presencial (art. 3).
4. ★ Convenio aplicable (denominación y código) y si hay acuerdo colectivo de teletrabajo en la empresa.
5. ★ Medios que aporta la empresa (ordenador, pantalla, silla, teléfono, conexión) y los que usaría el trabajador; gastos que soporta el trabajador (conexión, electricidad, climatización, espacio) y cómo se quieren compensar.
6. ★ Horario, franjas de disponibilidad y flexibilidad; sistema de registro de jornada.
7. ★ Centro de adscripción y lugar elegido por el trabajador (domicilio u otro), y si puede cambiarlo.
8. ★ Medios de control previstos (software, conexión a sistemas, cámaras, geolocalización) y si se usan dispositivos del trabajador.
9. Reversibilidad: quién puede pedirla, con qué preaviso y por qué causas.
10. Si existe representación legal de los trabajadores (copia del acuerdo, audiencia en la política de desconexión y en los criterios de uso de dispositivos).
11. Si el conflicto ya existe: acuerdo firmado, comunicación de la empresa (negativa, reversión, cambio) y su fecha, para el plazo de 20 días hábiles del art. 138 bis LRJS.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde».

**1. ¿Se aplica la Ley 10/2021? (arts. 1 y 2)**. Es trabajo a distancia **regular** el que se presta, en un periodo de referencia de tres meses, al menos el 30 % de la jornada, o el porcentaje proporcional según la duración del contrato. Teletrabajo es el trabajo a distancia prestado con medios telemáticos de forma exclusiva o prevalente.

- **Cómo se calcula**: la ley no dice si en días o en horas ni si el periodo es el trimestre natural. Si la jornada diaria no es igual todos los días, calcula en horas y en días y toma el resultado más alto; usa como denominador las horas de trabajo efectivo del periodo (sin vacaciones, festivos ni permisos) y comprueba cualquier periodo de tres meses consecutivos. Muestra en una tabla el trimestre tipo y el **trimestre desfavorable** (las vacaciones y los festivos que caen en días presenciales reducen el denominador y no los días a distancia): un esquema del 22-25 % puede superar el 30 % en ese trimestre.
- **Por debajo del umbral** no rige el régimen de la ley: ni el acuerdo obligatorio de los arts. 6 y 7 ni la compensación del art. 12 (tampoco la del convenio, si el convenio la liga al trabajo a distancia «regular»: compruébalo en su texto). Siguen aplicándose el registro de jornada (art. 34.9 ET), la intimidad digital y la desconexión (arts. 87 y 88 de la Ley Orgánica 3/2018 y art. 20 bis ET), el control del art. 20.3 ET y el deber general de prevención (art. 14 de la Ley 31/1995, `ley="LPRL"`). Entrega un pacto de trabajo a distancia ocasional (apartado «Documentos que se entregan») con un **tope de seguridad** por debajo del 30 % (por ejemplo, el 25 % de las horas efectivas de cualquier periodo de tres meses), controlado con el registro de jornada, y la regla de que superarlo exige firmar antes el acuerdo de la ley.
- **Riesgo de condición más beneficiosa**: un teletrabajo ocasional concedido sin documentar y disfrutado de forma continuada puede consolidarse y no poder retirarse después sin acuerdo o sin la vía del art. 41 ET. Documenta su carácter voluntario, ocasional y revocable (revocación recíproca, con preaviso y razón expresada) y busca la doctrina general de la condición más beneficiosa (consulta abajo).

**2. Límites (art. 3)**: con menores y en contratos formativos, solo cabe un acuerdo que garantice al menos el 50 % de prestación presencial.

**3. Voluntariedad y reversibilidad (art. 5)**:

- Voluntario para ambas partes; requiere acuerdo; no se puede imponer por la vía del art. 41 ET, sin perjuicio del derecho que reconozca la ley o el convenio.
- La negativa a teletrabajar, el ejercicio de la reversibilidad y las dificultades ligadas exclusivamente al cambio **no justifican** la extinción ni la modificación sustancial.
- La vuelta a la presencialidad de quien empezó en presencial es reversible para ambas partes en los términos del convenio o, en su defecto, del acuerdo: fija causas y preaviso en el acuerdo.
- **Quien fue contratado a distancia desde el inicio no está incluido en el art. 5.3**: la ley no da a la empresa un derecho a revertir, y hacerle trabajar en la oficina es modificar el porcentaje de presencialidad, que exige acuerdo escrito previo (art. 8.1). Lo que la ley le reconoce es prioridad para vacantes presenciales si trabaja a distancia a jornada completa (art. 8.2). Comprueba además el convenio: algunos solo declaran reversible el trabajo a distancia que no formaba parte de la descripción inicial del puesto. Una cláusula del acuerdo que deje a la empresa decidir sola la vuelta «por necesidades organizativas» choca con el art. 8.1 y con el art. 1256 del Código Civil.

**4. Forma y copia (art. 6)**: por escrito, en el contrato inicial o después, pero **antes** de empezar a distancia. Copia a la RLT en diez días (sin datos que afecten a la intimidad), que la firma, y remisión a la oficina de empleo; si no hay RLT, también se formaliza y remite. No formalizar el acuerdo es infracción grave (art. 7.1 del Real Decreto Legislativo 5/2000).

**5. Contenido mínimo (art. 7, letras a a l)**: inventario de medios y su vida útil; enumeración de gastos y forma de cuantificar la compensación, momento y forma de pago (la del convenio, si existe); horario y reglas de disponibilidad; porcentaje y distribución entre presencial y a distancia; centro de adscripción; lugar elegido por el trabajador; preaviso de la reversibilidad; medios de control; procedimiento ante dificultades técnicas; instrucciones de protección de datos (con participación de la RLT); instrucciones de seguridad de la información (previa información a la RLT); duración del acuerdo. Cada letra tiene su cláusula; ninguna queda en blanco.

**6. Modificación y prioridades (art. 8)**: cualquier cambio del acuerdo, incluido el porcentaje de presencialidad, por acuerdo escrito previo y comunicado a la RLT. Quien trabaja a distancia desde el inicio y a tiempo completo tiene prioridad para vacantes presenciales. El convenio puede fijar criterios de paso y preferencias.

**7. Derechos que el acuerdo tiene que respetar**:

- igualdad de trato y retribución, incluidos los complementos de los presenciales salvo los inherentes a la presencialidad (art. 4);
- formación y promoción (arts. 9 y 10);
- dotación y mantenimiento de medios, y atención ante dificultades técnicas (art. 11);
- **gastos**: el trabajo a distancia lo sufraga o compensa la empresa y no puede suponer gastos para el trabajador; el convenio puede fijar el mecanismo (art. 12);
- horario flexible en los términos del acuerdo y del convenio (art. 13); registro que refleje fielmente el tiempo, con inicio y fin de la jornada (art. 14 de la ley y art. 34.9 ET);
- prevención: evaluación limitada a la zona habilitada; visita al domicilio solo con permiso del trabajador y con informe escrito; sin permiso, evaluación con la información que él aporte (arts. 15 y 16);
- intimidad: la empresa no puede exigir instalar programas en dispositivos del trabajador ni que los use; criterios de uso de los dispositivos con participación de la RLT (art. 17 de la ley y art. 87 de la Ley Orgánica 3/2018);
- **desconexión digital** fuera del horario y política interna previa audiencia de la RLT (art. 18 de la ley y art. 88 de la Ley Orgánica 3/2018);
- derechos colectivos (art. 19).

**8. Control empresarial (art. 22 de la ley y arts. 20.3 y 20 bis ET)**: medidas de vigilancia con respeto a la dignidad; información previa, expresa y clara si hay videovigilancia o grabación de sonido (art. 89 de la Ley Orgánica 3/2018) o geolocalización (art. 90); acceso a los dispositivos de empresa solo para controlar obligaciones e integridad, con criterios de uso previos (art. 87). Todo medio de control figura en el acuerdo (art. 7.h) y responde a idoneidad, necesidad y proporcionalidad (art. 17.1).

**9. Reclamación judicial (art. 138 bis LRJS)**: acceso, reversión y modificación del trabajo a distancia, demanda en veinte días hábiles desde que la empresa comunica su negativa o disconformidad; procedimiento urgente; sin recurso salvo acumulación de daños con cuantía suficiente. Si la reclamación es de conciliación, procedimiento del art. 139 LRJS. Da la fecha final calculada.

- **Sin conciliación previa**: el art. 64.1 LRJS (lee el texto vigente, que el conector da antes de la nota «Téngase en cuenta») exceptúa las reclamaciones del art. 138 bis; una papeleta no suspende el plazo salvo que ambas partes acudan voluntariamente y de común acuerdo (art. 64.3).
- **Cómputo cuando la decisión es de la empresa** (reversión o cambio impuestos): el art. 138 bis está redactado para la negativa a una propuesta del trabajador; cuenta de forma prudente desde la comunicación de la empresa, no desde su respuesta a la disconformidad, y da las dos fechas. No figura entre las modalidades del art. 43.4 LRJS: agosto y del 24 de diciembre al 6 de enero son inhábiles para esta acción.
- **Órgano**: Tribunal de Instancia, Sección de lo Social (art. 84 LOPJ), del lugar de prestación de servicios o del domicilio de la empresa, a elección del trabajador (art. 10.1 LRJS). El art. 138 bis no remite a medidas cautelares como el art. 139: la orden de la empresa es ejecutiva mientras no haya sentencia. Explica al trabajador las opciones (cumplir con reserva de acciones y reclamar los gastos, o no cumplir con riesgo de sanción, impugnable en veinte días hábiles por los arts. 114 y 103 LRJS); el art. 5.2 de la Ley 10/2021 no protege la negativa a volver a la oficina.

## Estrategia y jurisprudencia

**Si defiende a la empresa**: un acuerdo que aguante es un acuerdo que no deja a la empresa decidir sola lo que la ley manda pactar.

- Fija un porcentaje y una distribución concretos; si se quiere flexibilidad, pacta una regla de cambio con preaviso y compensación de días, no la facultad del responsable de decidir cuándo se va a la oficina.
- Compensa los gastos con un método comprobable (importe periódico justificado por conceptos, o reembolso con justificantes) o remite al del convenio; nunca declares que el teletrabajo no genera gastos o que se compensan con ahorros.
- Documenta las averías como tiempo de trabajo si impiden trabajar sin culpa del trabajador (art. 4.2).
- Elabora o actualiza la política de desconexión y los criterios de uso de dispositivos con audiencia de la RLT antes de firmar los acuerdos.

**Si defiende al trabajador**: comprueba si supera el umbral del art. 1, si existe acuerdo escrito con las doce letras del art. 7, si la empresa compensa gastos y si las cláusulas de presencialidad, control o reversibilidad le dejan la decisión unilateral. Una vuelta impuesta sin causa pactada o convencional se impugna por el art. 138 bis LRJS en veinte días hábiles.

Doctrina que se ha localizado con Jurisprudenciator y que hay que buscar y leer en cada caso (no la cites sin el párrafo literal):

- son nulas la cláusula que niega los gastos o los da por compensados con ahorros y la que permite a la empresa exigir presencia en días de teletrabajo sin sustituirlos (arts. 7.b, 8.1 y 12 de la ley y art. 1256 del Código Civil);
- el art. 8.1 prohíbe a la empresa modificar unilateralmente el porcentaje de presencialidad pactado, por ejemplo ordenando trabajar en la oficina más días a la semana (útil para impugnar una vuelta impuesta);
- el riesgo ergonómico genérico, no evaluado en el puesto concreto, no obliga a entregar silla ergonómica a toda la plantilla: la dotación depende de la evaluación de riesgos, del acuerdo y del convenio;
- el porcentaje y la distribución forman parte del contenido mínimo y deben ser pactados, no fijados por el responsable jerárquico;
- el tiempo en que no se puede trabajar por averías o incidencias no imputables es tiempo de trabajo;
- el teletrabajo impuesto durante la pandemia tiene un régimen propio (disposición transitoria de la Ley 10/2021, que el conector no devuelve: léela en internet en el texto consolidado del BOE, identificador BOE-A-2021-11472, y cítala con enlace y fecha de consulta): no apliques esa doctrina a los acuerdos ordinarios sin decirlo. Lo mismo para las disposiciones adicionales y transitorias de la ley si el caso depende de ellas (acuerdos o convenios anteriores a su entrada en vigor).

Consultas (reformula como máximo dos veces):

- Cláusulas del acuerdo: `consulta="acuerdo individual de teletrabajo cláusulas presencialidad compensación de gastos"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Gastos: `consulta="trabajo a distancia compensación de gastos Ley 10/2021"`, `base="TS"`.
- Averías: `consulta="trabajo a distancia tiempo de trabajo averías incidencias técnicas tiempo efectivo"`, `base="TS"`.
- Reversibilidad: `consulta="teletrabajo reversibilidad vuelta al trabajo presencial"`, `base="AN"`, `fecha_desde="11/07/2021"`, y con `tipo_organo="TSJ"` + `provincia`.
- Control: `consulta="teletrabajo control empresarial software monitorización intimidad"`, `base="AN"`, `tipo_organo="TSJ"`.
- Medios y prevención: `consulta="teletrabajo silla ergonómica evaluación de riesgos dotación de medios"`, `base="TS"`.
- Teletrabajo ocasional por debajo del umbral: `consulta="condición más beneficiosa voluntad inequívoca de la empresa incorporar al nexo contractual mera tolerancia"`, `base="TS"`, `anios=5` (no se ha encontrado doctrina específica sobre el trabajo a distancia inferior al 30 %; si tampoco aparece, redacta sobre los arts. 1 y 2 y dilo en la nota).

Al leer, los primeros párrafos que devuelve `leer_sentencias` suelen ser hechos o alegaciones de las partes: cita solo el razonamiento de la Sala; si los tres párrafos no lo contienen, repite la lectura con `terminos` propios de la conclusión (por ejemplo, «desestimar el motivo» y el precepto) antes de descartar la sentencia.

Casi toda la doctrina del Supremo en esta materia sale de conflictos colectivos: sirve igual para el acuerdo individual, pero comprueba que la cláusula enjuiciada es equivalente a la del caso. En el acuerdo no va jurisprudencia; va a la nota.

## Documentos que se entregan

1. **Acuerdo de trabajo a distancia** (formato, apartado 2): `contrato-acuerdo-trabajo-distancia-<apellido-trabajador>-<AAAAMMDD>.docx`.
   - REUNIDOS, INTERVIENEN y EXPONEN (voluntariedad de ambas partes, art. 5; convenio aplicable con código).
   - CLÁUSULAS en ordinales, una por cada letra del art. 7 y en su orden: medios (remite al anexo I), gastos y compensación, horario y disponibilidad, porcentaje y distribución, centro de adscripción, lugar de trabajo, reversibilidad y preaviso, medios de control, dificultades técnicas, protección de datos, seguridad de la información, duración.
   - Cláusulas adicionales: registro de jornada; desconexión digital (remite a la política); prevención (evaluación y, en su caso, autorización de visita); modificación solo por acuerdo escrito (art. 8.1); copia a la RLT.
   - ANEXO I, **inventario** en tabla (elemento, modelo o descripción, número de serie, fecha de entrega, vida útil o plazo de renovación). ANEXO II, **cálculo de la compensación de gastos** en tabla (concepto, criterio, importe o método, periodicidad, fuente: convenio o acuerdo).
   - **Reparto para la redacción rápida:** tres secciones por bloques de cláusulas: comparecencia, EXPONEN, medios (anexo I), gastos y compensación (anexo II) / horario, porcentaje y distribución, centro de adscripción, lugar, reversibilidad y preaviso / control, dificultades técnicas, protección de datos, seguridad de la información, duración, cláusulas adicionales y firmas. La política de desconexión, una sola sección.
2. **Política de desconexión digital** si la empresa no la tiene: `politica-desconexion-digital-<empresa>-<AAAAMMDD>.docx`, con el contenido del art. 88.3 de la Ley Orgánica 3/2018 y constancia de la audiencia a la RLT.
3. **Nota para el abogado**, solo si el abogado la pide (si no, lo que esta skill manda «a la nota» —calendario, riesgos, cálculos y jurisprudencia con su ECLI— va en el resumen de la entrega): `nota-teletrabajo-<empresa>-<AAAAMMDD>.docx`. Si supera el umbral (cálculo del porcentaje en tabla); convenio y sus artículos; cláusulas de riesgo y alternativa válida; plazos (copia a la RLT en diez días desde la firma, con fecha; si hay conflicto, el del art. 138 bis LRJS con fecha); jurisprudencia literal.
4. **Si defiende al trabajador**: nota de análisis del acuerdo o de la decisión de la empresa, con la reclamación que procede, su plazo (las dos fechas si el inicio es dudoso), el órgano y la actuación recomendada mientras no haya sentencia.
5. **Si el trabajo a distancia no alcanza el umbral**: en lugar del acuerdo, `contrato-pacto-trabajo-distancia-ocasional-<apellido-trabajador>-<AAAAMMDD>.docx` (REUNIDOS, INTERVIENEN, EXPONEN con el cálculo que demuestra que no es regular, y CLÁUSULAS: objeto y carácter ocasional; días y tope de seguridad controlado con el registro; horario y registro de jornada; medios; compensación de gastos, voluntaria salvo que el convenio la imponga también al trabajo ocasional; control; protección de datos y seguridad; prevención; desconexión; revocación recíproca con preaviso y razón expresada, y declaración de que el disfrute no consolida un derecho; duración), más la tabla del cálculo y el trimestre desfavorable (en la nota del punto 3 si se entrega; si no, en el resumen).

En las tablas de preceptos de la nota escribe las fechas de vigencia con letra («11 de julio de 2021»): con el formato «11/07/2021» junto a los artículos, `verificar_escrito` toma la fecha por el número de una norma («Ley 12/2018», «Decreto-ley 12/2021») y marca falsos errores.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos en esta conversación los arts. 1 a 8, 11, 12, 14, 16, 17, 18 y 22 de la Ley 10/2021 (con su identificador BOE y título comprobado), los arts. 87, 88 y, si procede, 89 y 90 de la Ley Orgánica 3/2018, y los arts. 13, 20, 20 bis y 34 ET; 138 bis LRJS si hay conflicto.
- [ ] Convenio leído en teletrabajo, trabajo a distancia y desconexión, con código y vigencia.
- [ ] Umbral del 30 % calculado en horas y en días, con el trimestre desfavorable; por debajo, pacto ocasional con tope de seguridad; mínimo presencial del art. 3 respetado en menores y formativos.
- [ ] Artículo del convenio leído entero (`articulo="N"`) y, si hay revisiones posteriores, importe vigente de la compensación comprobado en el boletín oficial.
- [ ] Las doce letras del art. 7 tienen cláusula; ninguna deja a la empresa la decisión unilateral sobre porcentaje, presencialidad o gastos.
- [ ] Inventario y cálculo de gastos en tabla, con la fuente de cada importe; sin cuantías inventadas.
- [ ] Cada ECLI de la nota leído con `leer_sentencias` o comprobado con `buscar_por_cita`; ninguno en el acuerdo.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero) y corregido lo que señale.
- [ ] Marcadores en lugar de datos no facilitados; lo que no sale de Jurisprudenciator (disposiciones de la ley, criterios oficiales) procede de una fuente oficial con enlace y fecha de consulta.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado, plazos con su precepto, cálculos de gastos, datos obtenidos de internet, riesgos, documentos que faltan, tabla de jurisprudencia y próximo paso.
