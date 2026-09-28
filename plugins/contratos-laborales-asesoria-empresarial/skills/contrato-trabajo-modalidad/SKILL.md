---
name: contrato-trabajo-modalidad
description: >-
  Elige la modalidad de contrato de trabajo que permite la ley tras la reforma de 2021 y la redacta en Word
  con nota para el abogado: indefinido ordinario, fijo-discontinuo (también en contratas), temporal por
  circunstancias de la producción (imprevisible o previsible), sustitución, formativo en alternancia o para la
  práctica profesional y tiempo parcial. Úsala cuando la empresa diga «necesito a alguien para la campaña»,
  «¿le hago un temporal?», «contrato para cubrir una baja», «contrato de prácticas» o «media jornada», y
  cuando el trabajador pregunte si su temporal está en fraude y es fijo. Sirve a empresa y trabajador. El
  periodo de prueba se pacta con periodo-prueba; no competencia y permanencia, con pactos-contrato-trabajo;
  el trabajo a distancia, con teletrabajo-acuerdo; el alto directivo, con alta-direccion.
---

# Contrato de trabajo: elección de modalidad y redacción

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Causa, límites y efectos de cada modalidad** → `buscar_articulo` (`ley="ET"`, artículos `"15"` —indefinido, circunstancias de la producción, sustitución, encadenamiento—, `"16"` —fijo-discontinuo—, `"11"` —formativos— y `"12"` —tiempo parcial—).
- **Forma, copia básica, clasificación profesional y fin del contrato** → `buscar_articulo` (`ley="ET"`, artículos `"8"`, `"22"`, `"49"` y `"17"`); información de los elementos esenciales → `buscar_articulo` (`ley="Real Decreto 1659/1998"`, artículos `"2"`, `"5"` y `"6"`).
- **Consecuencias del incumplimiento para la empresa** → `buscar_articulo` (`ley="BOE-A-2000-15060"`, `articulo="7"`; la cuantía, del `"40"` en el momento) y cotización adicional de contratos cortos (`ley="LGSS"`, `articulo="151"`); si el contrato formativo incluye trabajo a distancia → (`ley="BOE-A-2021-11472"`, `articulo="3"`).
- **Contratos anteriores a la reforma** → las disposiciones transitorias del Real Decreto-ley 32/2021 (`ley="BOE-A-2021-21788"`) **no salen** por `buscar_articulo` ni por `leer_boe`: léelas en internet en el BOE y complétalas con la doctrina que las aplica (ver «Contratos anteriores a la reforma»).
- **Convenio aplicable y sus artículos** → `buscar_convenio` + `leer_convenio` (`buscar_en` con una sola materia: `"contratación"`, `"fijos discontinuos"`, `"formativo"`, `"grupos profesionales"`, `"periodo de prueba"`) + `vigencia_convenio`. Si los pasajes de `buscar_en` no contienen el artículo que buscas o `articulo="N"` llega cortado en un salto de página, pide el texto completo (`leer_convenio` con `max_chars` alto, p. ej. `200000`), localiza el artículo por su título y cita el que hayas leído entero. Las tablas salariales que el propio convenio trae en sus anexos (a veces de varios años) salen de ahí; solo si no están, búscalas en internet. Si el convenio está denunciado, lee su cláusula de vigencia y, en su defecto, el apartado 3 del art. 86 ET (`buscar_articulo`).
- **Doctrina sobre causa, fraude, encadenamiento y fijos-discontinuos** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; o `base="AN"` + `tipo_organo="TSJ"` + `provincia` sede de la Sala) + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión).
- **Empresa** → `buscar_empresa_mercantil` (denominación exacta, CIF y domicilio para la comparecencia).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

**Trampa del conector en los arts. 12 y 16 ET**: tras la nota «Téngase en cuenta… entra en vigor…», la respuesta reproduce entre comillas el texto **anterior** del precepto. Usa solo el bloque que va antes de esa nota.

## Cuándo usarla

Pregunta primero **a quién defiende el abogado**:

- **Empresa**: quiere contratar y necesita saber qué modalidad le permite la ley para esa necesidad concreta y un contrato que aguante una inspección o una demanda.
- **Trabajador**: tiene uno o varios contratos temporales o fijos-discontinuos y quiere saber si está en fraude, si ya es fijo o qué antigüedad tiene. Si el contrato **ya se extinguió**, el plazo de caducidad de 20 días hábiles del art. 59.3 ET corre desde la fecha de efectos: calcúlalo lo primero y deriva la impugnación a `papeleta-conciliacion` y `redactar-demanda-despido`; esta skill aporta el análisis del fraude.

| Situación | Skill |
|---|---|
| Pactar o revisar el periodo de prueba | `periodo-prueba` |
| No competencia postcontractual, permanencia, plena dedicación, confidencialidad | `pactos-contrato-trabajo` |
| El trabajo se prestará a distancia de forma regular | `teletrabajo-acuerdo` (el acuerdo va anexo al contrato) |
| Directivo con poderes de la titularidad de la empresa | `alta-direccion` |
| Duda de si hay relación laboral o autónomo | `falso-autonomo-trade` |
| No está claro el convenio | `convenio-aplicable` antes de redactar |
| Indemnización o finiquito al terminar un temporal | `calculo-indemnizacion-despido`, `finiquito-liquidacion` |
| Subrogación de plantilla por cambio de contratista | `sucesion-empresa-contratas` |
| Empleadora del sector público | Esta skill no cubre el acceso al empleo público: el fraude no da fijeza sino la figura del indefinido no fijo y la doctrina propia sobre abuso de temporalidad; avísalo y busca esa doctrina aparte |

## Datos que hay que reunir antes de redactar

No redactes al primer disparo. Pregunta en este orden; si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende el abogado.
2. ★ Empresa: denominación, CIF, `[CÓDIGO DE CUENTA DE COTIZACIÓN]`, actividad real, centro de trabajo, plantilla del centro y de la empresa, si pertenece a un grupo y si hay representación legal de los trabajadores (RLT).
3. ★ Trabajador: nombre, DNI/NIE, fecha de nacimiento (límite de edad del contrato en alternancia, art. 11.2.b ET), titulación y **fecha de terminación de los estudios** (art. 11.3.b ET), y **todos los contratos previos con la empresa o su grupo**, también a través de ETT (arts. 11.2.j, 11.3.b, 14.1 y 15.5 ET). Pide la vida laboral.
4. ★ Puesto: funciones, grupo profesional, centro, fecha de inicio, jornada (completa o parcial, horas y distribución) y salario desglosado.
5. ★ **La necesidad que justifica la contratación**, con hechos comprobables:
   - circunstancias de la producción imprevisibles: qué pedido, cliente, pico u oscilación, desde y hasta cuándo, volumen normal frente al actual; si son vacaciones, qué personas y fechas;
   - previsibles de duración reducida: qué situaciones concretas y qué días; **días ya usados por la empresa en el año natural** con esta modalidad y si trasladó a la RLT la previsión anual;
   - sustitución: nombre de la persona sustituida, causa de la reserva o de la reducción de jornada, o proceso de selección en curso y su fecha;
   - fijo-discontinuo: temporada o intermitencia, o la contrata (cliente, objeto, duración prevista) y el criterio de llamamiento.
6. ★ Convenio aplicable (denominación y código) o encarga antes `convenio-aplicable`.
7. Si defiende al trabajador: copia de cada contrato, prórrogas, llamamientos, comunicaciones de fin, nóminas y fecha de efectos de la extinción si ya se produjo.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde». Primero, orienta la elección con esta tabla; después comprueba cada regla del orden de decisión.

| Necesidad real de la empresa | Modalidad | Precepto |
|---|---|---|
| Puesto permanente, todo el año | Indefinido ordinario (a jornada completa o parcial) | arts. 15.1 y 12 ET |
| Actividad que se repite por temporadas o de forma intermitente | Fijo-discontinuo | art. 16.1 ET |
| Servicio a un cliente mediante contrata que forma parte de la actividad ordinaria | Fijo-discontinuo o indefinido | arts. 15.2 (último párrafo) y 16.1 ET |
| Pico ocasional e imprevisible, u oscilación (incluidas vacaciones) | Circunstancias de la producción imprevisibles | art. 15.2 ET |
| Situación ocasional, previsible y de pocos días identificados | Circunstancias de la producción previsibles | art. 15.2 ET |
| Ausencia con reserva de puesto, reducción de jornada o selección en curso | Sustitución | art. 15.3 ET |
| Persona que se forma a la vez que trabaja | Formativo en alternancia | art. 11.2 ET |
| Titulado reciente que necesita práctica profesional | Formativo para la práctica profesional | art. 11.3 ET |

1. **Presunción de indefinido (art. 15.1 ET)**. El contrato de duración determinada solo cabe por circunstancias de la producción o por sustitución. Para que haya causa hay que especificar **con precisión** la causa habilitante, las circunstancias concretas que la justifican y su conexión con la duración prevista. Si la necesidad es permanente o se repite cada año, la respuesta es indefinido o fijo-discontinuo, no un temporal.
2. **Circunstancias de la producción imprevisibles (art. 15.2 ET)**: incremento ocasional e imprevisible u oscilaciones de la actividad normal (incluidas las vacaciones) que generan un desajuste temporal, siempre que no sean supuestos del art. 16.1. Duración máxima de seis meses, ampliable hasta un año por **convenio sectorial** (compruébalo con `leer_convenio`); si se pacta por menos, una única prórroga por acuerdo sin superar el máximo. El convenio puede ampliar la duración y concretar el supuesto, pero no crear causas nuevas: si todavía enumera tareas heredadas del antiguo contrato de obra o servicio («nueva línea de producción», «apertura de nuevos mercados», «lanzamiento de un nuevo producto»…), no fundes el contrato en esa lista; la causa es la del art. 15.2 y el hecho concreto tiene que encajar en ella. Que el pedido se conozca con antelación no lo convierte por sí solo en «previsible», pero es el punto débil del contrato: la ley no traza la frontera con las situaciones ocasionales previsibles (máximo de noventa días al año, no continuados), así que busca doctrina de la Sala del territorio y, si no la hay, explica el riesgo en la nota. Si la necesidad se repite cada año, es fijo-discontinuo.
3. **Circunstancias de la producción previsibles (art. 15.2 ET)**: situaciones ocasionales, previsibles, de duración reducida y delimitada, **identificadas en el contrato**.
   - Tope por empresa y año natural: 90 días (120 en el sector agrario y agroalimentario, redacción reformada en 2025: confirma el texto vigente), no continuados, con independencia del número de personas contratadas cada día.
   - En el último trimestre la empresa traslada a la RLT la previsión anual de uso.
   - Lleva el cómputo de días de toda la empresa, no por trabajador: el exceso convierte en fijos a los contratados.
4. **Contratas**: el art. 15.2 impide usar como causa la ejecución de contratas, subcontratas o concesiones que sean la actividad habitual de la empresa, salvo que concurran de verdad circunstancias de la producción. Su cauce es el fijo-discontinuo (art. 16.1, párrafo segundo) o el indefinido ordinario.
5. **Sustitución (art. 15.3 ET)**, tres supuestos:
   - persona con derecho a reserva de puesto: nombre y causa en el contrato; puede empezar antes de la ausencia, coincidiendo el tiempo imprescindible y como máximo quince días;
   - completar la jornada reducida de otra persona por causa legal o convencional (nombre y causa);
   - cobertura durante el proceso de selección o promoción para un puesto fijo: máximo tres meses o el plazo inferior del convenio, sin nuevo contrato con el mismo objeto.
6. **Fijo-discontinuo (art. 16 ET)**:
   - supuestos: trabajos estacionales o de temporada; intermitentes con periodos de ejecución ciertos, determinados o indeterminados; contratas previsibles de la actividad ordinaria; ETT;
   - forma escrita con la duración del periodo de actividad, la jornada y su distribución (pueden figurar estimadas y concretarse en el llamamiento);
   - llamamiento según los criterios objetivos del convenio o acuerdo de empresa, por escrito o medio que deje constancia y con antelación adecuada; calendario anual de llamamientos a la RLT;
   - en contratas, la inactividad solo como espera de recolocación entre subcontratas, con el plazo máximo del convenio sectorial o, en su defecto, tres meses (art. 16.4);
   - antigüedad por toda la duración de la relación (art. 16.6); comprueba en el convenio el tiempo parcial, la bolsa sectorial, el llamamiento mínimo y la cuantía por fin de llamamiento (art. 16.5).
7. **Encadenamiento (art. 15.5 ET)**: adquiere la fijeza quien, en 24 meses, ha estado contratado más de 18 meses con dos o más contratos por circunstancias de la producción, en el mismo o distinto puesto, con la misma empresa o grupo, directamente o por ETT (también tras sucesión o subrogación); y quien ocupe un puesto cubierto más de 18 meses en 24 con esos contratos. La empresa entrega el documento de fijeza en los diez días siguientes (art. 15.9). Haz la tabla de cómputo (contrato, modalidad, inicio, fin, días, ventana de 24 meses).
8. **Efectos del incumplimiento y del fin del contrato**:
   - quien se contrata incumpliendo el art. 15 es fijo; también el temporal no dado de alta pasado un plazo igual al del periodo de prueba (art. 15.4);
   - al terminar el temporal, indemnización proporcional del art. 49.1.c ET, salvo formativos y sustitución; prórroga automática hasta el máximo si no hay denuncia y sigue trabajando; indefinido si continúa tras la duración máxima; preaviso de quince días si el contrato dura más de un año;
   - para la empresa, una infracción grave por cada trabajador afectado (art. 7.2 del Real Decreto Legislativo 5/2000; la cuantía, del art. 40 en el momento) y cotización adicional en los contratos de menos de 30 días (art. 151 LGSS), salvo sustitución.
9. **Formativos (art. 11 ET)**.
   - En alternancia (apartado 2): sin la cualificación que permite la práctica profesional; hasta treinta años en certificados de nivel 1 y 2 y programas del Catálogo; plan formativo individual y dos tutores (centro y empresa); entre tres meses y dos años; tiempo de trabajo efectivo máximo del 65 % el primer año y del 85 % el segundo; prohibido si ya desempeñó el puesto más de seis meses; sin horas extra, complementarias, nocturnidad ni turnos salvo la excepción; **sin periodo de prueba**; retribución del convenio o, en su defecto, los porcentajes del apartado 2.m y nunca por debajo del SMI proporcional (su cuantía del año sale del real decreto del SMI: búscalo en internet en el BOE y cítalo con enlace; no la escribas de memoria).
   - Para la práctica profesional (apartado 3):
     - título universitario o de formación profesional que habilite o capacite para la actividad; dentro de los tres años siguientes a terminar los estudios (cinco con discapacidad);
     - no cabe si ya tuvo más de tres meses de experiencia o actividad formativa en esa actividad en la empresa, **sin contar las prácticas que formen parte del currículo** del título (letra b): pide el certificado de la universidad o del centro;
     - entre seis meses y un año; nadie puede estar contratado por más tiempo con la misma titulación, en esa u otra empresa (letra d): las becas no laborales no son contratos formativos, pero pide la información del apartado 7;
     - periodo de prueba de un mes como máximo salvo que el convenio lo regule **para este contrato**; una escala general de ingreso que no menciona los formativos no basta: pacta un mes y explícalo en la nota;
     - sin horas extraordinarias salvo el art. 35.3; plan formativo, tutor con formación o experiencia adecuadas y certificado final;
     - **retribución** (letra i): la que el convenio fije para este contrato; si no fija ninguna, la del grupo y nivel de las funciones, íntegra, sin los porcentajes del apartado 2.m; nunca inferior a la mínima del contrato en alternancia ni al SMI en proporción al tiempo de trabajo efectivo.
   - Comunes (apartado 4): el texto del plan formativo va **dentro** del contrato; el fraude o el incumplimiento formativo lo convierten en indefinido ordinario; no pueden sustituir funciones de personas afectadas por ERTE; si continúa en la empresa, no hay nuevo periodo de prueba.
   - Recomienda pedir al servicio público de empleo la información del apartado 7 (valor liberatorio). Si hay trabajo a distancia, mínimo presencial del art. 3 de la Ley 10/2021, de 9 de julio, de trabajo a distancia.
10. **Tiempo parcial (art. 12 ET)**:
    - escrito con horas ordinarias y su distribución; sin ello, presunción de jornada completa;
    - registro diario y resumen mensual entregado con la nómina, conservado cuatro años (art. 12.4.c); sin horas extraordinarias salvo el art. 35.3; una sola interrupción en jornada partida salvo convenio; conversión siempre voluntaria (art. 12.4.e);
    - horas complementarias: pacto escrito aparte con los requisitos del apartado 5 (jornada mínima, porcentaje máximo, preaviso, renuncia); horas voluntarias del apartado 5.g solo en indefinidos. Lee también lo que diga el convenio (porcentaje entre el 30 % y el 60 %, preaviso inferior, consolidación de horas, jornada mínima de los parciales) y calcula en horas anuales el límite pactado.
11. **Forma y contenido (art. 8 ET)**: escrito en los casos del art. 8.2 (lee su texto junto con los arts. 11, 12, 15 y 16 vigentes: el art. 8.2 conserva nombres de modalidades derogadas) y en todo temporal de más de cuatro semanas; sin escrito, presunción de indefinido y jornada completa. Comunicación del contenido a la oficina pública de empleo en diez días (art. 8.3) y copia básica a la RLT en diez días (art. 8.4). El cauce telemático de comunicación (Contrat@) y los códigos de modalidad no salen del conector: búscalos en internet en la sede oficial del SEPE o de la Seguridad Social y cítalos con enlace y fecha de consulta. Si algún elemento esencial no está en el contrato, información escrita en el plazo del art. 6 del Real Decreto 1659/1998 (contenido del art. 2).
12. **Clasificación y salario (art. 22 ET)**: grupo profesional del convenio y funciones pactadas; en polivalencia, equiparación por las funciones de mayor tiempo. El salario del grupo sale de la tabla salarial publicada del año: búscala en internet (revisión salarial en el BOE, el boletín autonómico o el BOP; `vigencia_convenio` dice qué publicaciones hay) y cítala con enlace, o pídela al abogado (anclas, apartado 3). Sin tabla, deja `[SALARIO SEGÚN TABLA DEL CONVENIO]` y dilo en la nota. En todas las modalidades, compara el salario de tabla (en el tiempo parcial, en proporción a la jornada) con el SMI del año, que se busca en internet en el real decreto publicado en el BOE y se cita con enlace: hay tablas de convenio por debajo del SMI vigente. Si queda por debajo, el contrato garantiza el SMI y la nota lo explica con la operación.
13. **Igualdad de trato (arts. 15.6, 12.4.d y 17 ET)**: temporales, parciales y fijos-discontinuos no pueden recibir peores condiciones por su modalidad; la antigüedad se computa con los mismos criterios.

### Contratos anteriores a la reforma

Si el caso incluye contratos celebrados antes del 30/03/2022 (obra o servicio, eventuales, interinidad, prácticas, formación y aprendizaje), su régimen depende de las disposiciones transitorias del Real Decreto-ley 32/2021 (según Jurisprudenciator, mantienen la normativa anterior para los contratos basados en ella, limitan la duración de los celebrados entre su entrada en vigor y la del nuevo art. 15 y fijan una regla transitoria para el cómputo del encadenamiento). El conector no devuelve su texto (ni `buscar_articulo` ni `leer_boe`, que se corta en el preámbulo):

1. **Texto**: léelo en internet en el BOE (texto consolidado del Real Decreto-ley 32/2021, identificador BOE-A-2021-21788) y cita cada disposición transitoria con su enlace y la fecha de consulta; en el resumen, di que ese texto no sale de Jurisprudenciator.
2. **Doctrina que las interpreta**, con Jurisprudenciator: Tribunal Constitucional, que resolvió sobre el real decreto-ley (`buscar_sentencias`, `consulta="Real Decreto-ley 32/2021 disposiciones transitorias convalidación"`, `base="TC"`, y `leer_sentencias` con `terminos="disposición transitoria"`); Salas de lo Social (`consulta="contrato para obra o servicio determinado celebrado antes del 31 de diciembre de 2021 disposición transitoria tercera"`, `jurisdiccion="SOCIAL"`, `base="AN"`, `tipo_organo="TSJ"`).

Si el texto tampoco aparece en internet, aplica la puerta: no afirmes el régimen de esos contratos y dile al abogado qué disposición falta.

## Estrategia y jurisprudencia

**Si defiende a la empresa**: elige la modalidad por la necesidad, no por la comodidad de la extinción. Redacta la cláusula de causa con hechos verificables (cliente, pedido, fechas, volúmenes, persona sustituida) y su conexión con la duración; nunca «acumulación de tareas» o «necesidades de la producción» sin más. Dile qué pruebas guardar (pedidos, cuadrantes, bajas, previsión anual) y el calendario de vencimientos: fecha máxima, fecha de preaviso y fecha en que se cumplirían 18 meses en 24. Si la necesidad se repite, recomienda el fijo-discontinuo.

**Si defiende al trabajador**: busca por qué no aguanta el temporal: causa genérica o no conectada con la duración, actividad habitual o contrata como causa, superación de plazos, encadenamiento, falta de alta, falta de forma, formativo sin formación real. La consecuencia es la fijeza; si ya se extinguió, el cese es un despido (improcedente o nulo) y la antigüedad puede remontarse al primer contrato si hay unidad esencial del vínculo.

Consultas (reformula como máximo dos veces; `fecha_desde="30/03/2022"` para contratos de la regulación vigente):

- Causa y fraude: `consulta="contrato por circunstancias de la producción causa genérica fraude condición de fijo"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia` sede de la Sala.
- Fijo-discontinuo: `consulta="contrato fijo discontinuo contratas llamamiento"`, `base="TS"`.
- Antigüedad: `consulta="unidad esencial del vínculo antigüedad sucesión contratos temporales"`, `base="TS"`.
- Sustitución: `consulta="contrato de sustitución persona sustituida causa reserva de puesto"`, `base="TS"`.

Mucha doctrina del Supremo resuelve contratos anteriores a 2022 (obra o servicio, eventuales) y del sector público (indefinido no fijo). Úsala solo para lo que la regulación vigente mantiene (fraude y fijeza, unidad del vínculo, igualdad de trato) y dilo en la nota. En un contrato no se cita jurisprudencia; va a la nota (formato, apartados 1 y 8).

## Documentos que se entregan

1. **Contrato** (formato, apartado 2): `contrato-<modalidad>-<apellido-trabajador>-<AAAAMMDD>.docx`.
   - Título en mayúsculas con la modalidad; lugar y fecha; REUNIDOS e INTERVIENEN (empresa con `[CIF]`, `[CÓDIGO DE CUENTA DE COTIZACIÓN]` y representante; trabajador con `[DNI/NIE]` y `[DOMICILIO]`); EXPONEN (necesidad de la empresa).
   - CLÁUSULAS en ordinales con título:
     - PRIMERA, objeto y modalidad, con su precepto;
     - SEGUNDA, **causa de la temporalidad** (solo temporales): causa habilitante, circunstancias concretas y conexión con la duración; en previsibles, las situaciones y días identificados; en sustitución, nombre de la persona sustituida y causa;
     - TERCERA, grupo profesional y funciones; CUARTA, centro de trabajo;
     - QUINTA, duración: inicio y fin o hecho que lo determina; en fijo-discontinuo, periodo de actividad estimado y forma de llamamiento;
     - SEXTA, jornada y distribución; en parcial, horas, distribución y registro;
     - SÉPTIMA, retribución con desglose; OCTAVA, vacaciones;
     - NOVENA, periodo de prueba (cláusula de `periodo-prueba`, o «sin periodo de prueba» en alternancia);
     - DÉCIMA, convenio aplicable (denominación, código y publicación);
     - UNDÉCIMA, extinción y preaviso; DUODÉCIMA, protección de datos;
     - firmas en dos columnas.
   - ANEXOS: plan formativo individual (formativos, obligatorio); pacto de horas complementarias (parcial, documento separado); acuerdo de trabajo a distancia si procede.
2. **Nota para el abogado**: `nota-contrato-<modalidad>-<empresa>-<AAAAMMDD>.docx`. Modalidad elegida y descartadas con su precepto; análisis de la causa y riesgos (fijeza, infracción por trabajador, indemnizaciones); tabla de fechas (máxima, preaviso, 18 en 24, días previsibles consumidos); convenio y artículos leídos con su vigencia; obligaciones de la empresa con plazo (oficina de empleo, copia básica, previsión anual, información de vacantes del art. 15.7, documento de fijeza); jurisprudencia literal si la hay.
3. **Si defiende al trabajador**: nota de análisis del fraude con la tabla de contratos, la conclusión (fijo desde qué fecha, antigüedad) y el plazo que corre, en lugar del contrato.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos en esta conversación los arts. 8, 15 y el de la modalidad (11, 12 o 16) del ET, más 22, 49 y 17, con su fecha de vigencia; en los arts. 12 y 16, usado el texto anterior a la nota «Téngase en cuenta».
- [ ] Convenio identificado con código y vigencia (`vigencia_convenio`), y leídos sus artículos de contratación, grupos y periodo de prueba; si está denunciado, dicho en la nota por qué sigue aplicándose.
- [ ] Salario de tabla comparado con el SMI del año (proporcional en el tiempo parcial); en formativos, retribución de la letra m) del apartado 2 o de la letra i) del apartado 3 del art. 11 ET según la modalidad.
- [ ] La causa temporal está escrita con hechos, fechas y conexión con la duración; en previsibles, cómputo de días de la empresa en el año natural.
- [ ] Tabla de encadenamiento hecha si hay contratos previos; régimen transitorio citado desde el texto del BOE leído en internet (enlace y fecha de consulta) y la doctrina leída.
- [ ] Todo dato que no sale de Jurisprudenciator (disposiciones transitorias, SMI, tabla salarial, Contrat@) procede de una fuente oficial con enlace y fecha de consulta, y el resumen lo identifica.
- [ ] Cada ECLI de la nota leído con `leer_sentencias` o comprobado con `buscar_por_cita`; ninguno en el contrato.
- [ ] `verificar_escrito` pasado sobre el contrato y la nota; letras citadas como «letra c) del apartado 1 del artículo 49 del Estatuto de los Trabajadores».
- [ ] Marcadores en lugar de datos no facilitados; ninguna cuantía de sanción, SMI ni salario de tabla escrita de memoria.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado, fechas clave con su precepto, riesgos, documentos que faltan, tabla de jurisprudencia y próximo paso.
