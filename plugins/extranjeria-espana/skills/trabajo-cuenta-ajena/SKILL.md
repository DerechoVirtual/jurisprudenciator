---
name: trabajo-cuenta-ajena
description: >-
  Prepara la solicitud de autorización inicial de residencia y trabajo por cuenta ajena que presenta
  el empleador para contratar a un trabajador que está en su país (LOEX arts. 36 a 40; Reglamento de
  2024, arts. 72 a 81): situación nacional de empleo con el catálogo de difícil cobertura o el
  certificado de insuficiencia de demandantes, contrato ajustado al convenio, medios del empleador,
  causas de denegación, visado y alta, cambio de empleador, modificación y renovación. Úsala con
  «contratar a un extranjero que está en su país», «oferta de empleo para un trabajador de fuera»,
  «catálogo de difícil cobertura», «renovar el permiso de trabajo», «cambio de empleador». Si el
  trabajador está en España sin autorización, usa `arraigo-sociolaboral`; para alta cualificación,
  traslados o teletrabajo, `movilidad-internacional-ley-14-2013`; para autónomos,
  `trabajo-cuenta-propia`.
---

# Residencia temporal y trabajo por cuenta ajena: autorización inicial, cambios y renovación

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen legal y exenciones de la situación nacional de empleo** → `buscar_articulo` (`ley="LOEX"`, artículos 36, 38 y 40).
- **Requisitos, situación nacional de empleo, medios, procedimiento y denegación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 72 a 78, 38 y 40; 193 a 195 si la comunidad autónoma tiene traspasadas las autorizaciones iniciales de trabajo).
- **Cambio de empleador, modificación y renovación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 79, 80, 81, 190, 191 y 192).
- **Salario y condiciones del convenio aplicable (art. 74.1.c) y salario mínimo** → `buscar_convenio` + `leer_convenio` (`buscar_en="salario"` o el artículo de tablas) y `vigencia_convenio`; para el salario mínimo, `buscar_boe` (`consulta="salario mínimo interprofesional"`) y `buscar_articulo` del real decreto que devuelva.
- **Existencia y administración de la empresa empleadora** → `buscar_empresa_mercantil` (nombre o CIF de la sociedad).
- **Norma aplicable a solicitudes anteriores al 20/05/2025** → `leer_boe` (`identificador="BOE-A-2024-24099"`, disposición transitoria segunda del Real Decreto) y, si rige el reglamento anterior, `buscar_articulo` (`ley="Real Decreto 557/2011"`).
- **Doctrina sobre los motivos de denegación** → `buscar_sentencias` (`consulta="autorización residencia trabajo cuenta ajena medios económicos empleador denegación"`, `consulta="autorización residencia trabajo cuenta ajena situación nacional de empleo"` o `consulta="renovación autorización residencia trabajo antecedentes valoración"`, `jurisdiccion="CONTENCIOSO"`, `base="AN"`; `base="TS"` para doctrina casacional) + `leer_sentencias` (`parrafos=3`).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Si citas una letra, escribe «la letra b) del artículo 61.2 del Real Decreto 1155/2024», no «artículo 61.2.b) del…»: con la letra pegada, `verificar_escrito` atribuye el artículo a otra norma del mismo párrafo. Por la misma razón, cuando un párrafo cite más de una norma, nombra la norma en cada cita («el artículo 76.1 del Real Decreto 1155/2024», no «el mismo artículo» ni «el artículo 76.1» a secas).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar o el requisito que hay que comprobar), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Empresa o empleador persona física que quiere contratar a un trabajador que reside fuera de
  España: autorización inicial (arts. 73 a 78) y, después, visado del trabajador (art. 40).
- Titular de una autorización inicial que cambia de empleador (art. 79) o de ocupación, sector o
  ámbito territorial (art. 192).
- Residente temporal o estudiante que pasa a residencia y trabajo sin visado (arts. 190 y 191).
- Renovación de la autorización (arts. 80 y 81).

Usa otra skill cuando: el trabajador está en España sin autorización (`arraigo-sociolaboral` y
demás skills de arraigo); la actividad es de temporada (arts. 100 y siguientes) o se contrata por
gestión colectiva en origen; el puesto es de alta cualificación, directivo de grupo, traslado
intraempresarial o teletrabajo para empresa extranjera (`movilidad-internacional-ley-14-2013`); el
trabajador será autónomo (`trabajo-cuenta-propia`); la actividad está exceptuada de autorización de
trabajo (arts. 88 y 89).

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes mientras falte un dato imprescindible (★).

1. ★ Trámite: autorización inicial, cambio de empleador, modificación, paso desde otra situación
   o renovación. Si hay resolución denegatoria o requerimiento, el texto íntegro y su fecha de
   notificación.
2. ★ Empleador: persona física o jurídica, denominación y CIF o NIF, representante y su poder,
   actividad, provincia y comunidad autónoma del centro de trabajo.
3. ★ Situación del empleador en los doce meses anteriores (y tres años para la infracción del
   art. 53.2.a LOEX): despidos improcedentes o nulos o extinciones de los arts. 50, 51 y 52.c) ET
   en los puestos que quiere cubrir; sanciones firmes; condenas; extinciones anticipadas de otros
   contratos con autorización; ERTE vigentes; deudas tributarias o con la Seguridad Social (art. 78).
4. ★ Medios del empleador: para empresas, inscripciones y cuentas; para personas físicas,
   declaración del IRPF del año anterior y número de personas a su cargo (arts. 76 y 77.2.c).
5. ★ Puesto: ocupación según la Clasificación Nacional de Ocupaciones, si figura en el catálogo de
   ocupaciones de difícil cobertura vigente de la provincia o comunidad (el abogado debe
   comprobar el catálogo trimestral en la sede del Servicio Público de Empleo Estatal) o si se
   gestionará oferta; o qué exención de la situación nacional de empleo se alega (LOEX art. 40,
   art. 74.2, convenio internacional). Si hay oferta: texto íntegro tal como se presentó, fecha,
   candidatos enviados, resultado comunicado con la causa de rechazo de cada uno y certificado de
   insuficiencia con su fecha; y la urgencia de la contratación y cómo se prueba (art. 75.2).
6. ★ Contrato: duración, jornada, salario bruto, categoría y convenio colectivo aplicable.
7. ★ Trabajador: nacionalidad y país de residencia, pasaporte, titulación o cualificación exigida
   para la profesión, antecedentes penales, compromiso de no retorno.
8. Solo renovación ★: fechas de la autorización, relación laboral actual, periodos de alta, causa
   de la extinción del contrato, inscripción como demandante, prestaciones, menores a cargo,
   condenas, deudas; informe de esfuerzo de integración (opcional).

## Requisitos y comprobaciones

### A. Norma aplicable

- Lee cada artículo con `buscar_articulo` y aplica sus notas de nulidad. A 27/09/2026 el conector
  devuelve anulado el art. 197.2, que imponía la presentación electrónica de la solicitud
  inicial por cuenta ajena: compruébalo antes de indicar cómo presentar.
- Solicitudes anteriores al 20/05/2025: disposición transitoria segunda (`leer_boe`); si rige el
  reglamento anterior, `ley="Real Decreto 557/2011"`. Si `leer_boe` no la devuelve completa,
  aplica la puerta.

### B. Requisitos del art. 74.1 (autorización inicial)

| Letra | Requisito | Cómo se comprueba o prueba |
|---|---|---|
| a) | Situación nacional de empleo que permita contratar | Art. 75 (apartado C) o exención |
| b) | Contrato firmado por ambos, actividad continuada durante la vigencia, inicio condicionado a la eficacia | Contrato en el modelo oficial |
| c) | Condiciones del convenio y de la normativa; a tiempo parcial, retribución anual no inferior al SMI de jornada completa | `leer_convenio` y `buscar_articulo` del real decreto del SMI |
| d) | Empleador al corriente con Hacienda y Seguridad Social | La oficina lo comprueba de oficio (art. 77.5) |
| e) | Medios del empleador | Art. 76 (apartado D) |
| f) | Capacitación y cualificación legalmente exigida | Título y, si es profesión regulada, homologación y colegiación (LOEX art. 36.3) |
| g) | Sin compromiso de no retorno vigente | Declaración del trabajador |
| h) | Sin amenaza para el orden público | Antecedentes en España e informe policial; sin automatismo (art. 77.5) |
| i) | Tasa abonada | Sede oficial |

### C. Situación nacional de empleo (art. 75; LOEX art. 38)

- Vía 1: la ocupación figura en el catálogo de ocupaciones de difícil cobertura vigente para el
  territorio (art. 75.1). El catálogo no está en Jurisprudenciator: el abogado lo comprueba en la
  sede del Servicio Público de Empleo Estatal y aporta la referencia del trimestre.
- Vía 2: oferta de empleo ante el servicio público de empleo del territorio del puesto, sin
  requisitos ajenos al puesto; gestión durante el plazo del art. 75.2, comunicación del resultado
  de la selección con las causas de rechazo y certificado de insuficiencia de demandantes en el
  plazo de ese mismo apartado. La oficina valora también la urgencia acreditada.
  Lee el texto de la oferta antes de redactar: si incluye requisitos sin relación directa con el
  puesto (nacionalidad o preferencia por ella, sexo, edad, un idioma que el puesto no necesita,
  experiencia desproporcionada) o si los rechazos tienen causas genéricas o ligadas a esos
  requisitos, el certificado no garantiza que la oficina dé por acreditada la insuficiencia.
  Díselo al abogado antes de redactar y recomienda repetir la oferta; si decide repetirla, redacta
  con marcadores para las fechas, los candidatos y el resultado de la nueva.
- Vía 3: exenciones de la LOEX art. 40 (familiares, hijos o nietos de español de origen,
  extranjeros nacidos y residentes en España, puestos de confianza y directivos…) o convenio
  internacional (art. 74.2). Identifica la letra concreta y la prueba (art. 77.2.f).

### D. Medios del empleador (art. 76)

- Suficientes para el proyecto empresarial y para las obligaciones del contrato, incluido el
  salario bruto. Si es persona física, además los porcentajes del SMI del art. 76.2 según los
  miembros de la unidad familiar, descontado el salario del contrato. Copia los porcentajes del
  texto leído y la cuantía del SMI del real decreto vigente obtenido con `buscar_boe`.
- No valen subvenciones ni ayudas asistenciales, salvo en dependencia y cuidado de menores
  (art. 77.2.c). Para sociedades, comprueba con `buscar_empresa_mercantil` que la empresa existe,
  está activa y quién la administra; sus cuentas anuales no las devuelve el conector: pídelas.

### E. Procedimiento y plazos

- Presenta el empleador ante la oficina de extranjería de la provincia del centro de trabajo
  (art. 77.1) o ante el órgano autonómico si hay traspaso (art. 194.2). Documentos: art. 77.2.
- Inadmisión a trámite: art. 77.3 remite a las causas de la LOEX, que están en una disposición
  adicional que el conector no devuelve. Si el caso depende de una causa de inadmisión, aplica la
  puerta y explícale al abogado qué precepto falta.
- Subsanación en diez días con advertencia de desistimiento (art. 77.4). Resolución en tres meses;
  silencio desestimatorio (art. 77.6).
- Concedida, el trabajador pide el visado en un mes desde la notificación al empleador
  (art. 40.1.b); el consulado resuelve en un mes (art. 40.3). Alta en la Seguridad Social en tres
  meses desde la entrada legal, que da eficacia a la autorización (arts. 73.1 y 77.8), y tarjeta en
  un mes desde el alta (art. 77.9).
- La autorización inicial dura lo que la actividad, con el máximo de un año, limitada a una
  ocupación y a un ámbito autonómico salvo que no se aplique la situación nacional de empleo
  (art. 73.1 y 73.4). Permite actividad por cuenta propia accesoria (art. 73.5).

### F. Denegación (art. 78)

Repasa con el cliente cada letra del art. 78.1 antes de presentar: falta de un requisito del
art. 74; amortización de los puestos en los doce meses anteriores; sanciones firmes; documentos
falsos, alegaciones inexactas o mala fe; amenaza para el orden público acreditada en informe
policial; condenas del empleador; extinciones anticipadas de contratos con autorización; ERTE en
esos puestos; causa de inadmisión no apreciada. La denegación debe motivarse y expresar los
recursos (art. 78.2). En la jurisprudencia aparecen sobre todo la insuficiencia de medios del
empleador, contratos que no se ajustan al convenio y la falta de acreditación de la cualificación.

### G. Cambio de empleador, modificación y paso desde otra situación

- Cambio de empleador (art. 79): libre en la misma ocupación desde los tres meses y durante el
  primer año; en cualquier momento por incumplimiento grave del empleador o por circunstancias
  sobrevenidas, con los plazos de comunicación de los apartados 2 y 3; la oficina verifica en un
  mes las letras b) a e) del art. 74 y el silencio es desestimatorio (art. 79.4).
- Modificación de ocupación, sector o territorio durante el primer año (art. 192.1): se tiene en
  cuenta la situación nacional de empleo; silencio estimatorio en un mes.
- Desde residencia temporal sin visado (art. 191) o desde estancia por estudios (art. 190): lee el
  apartado que corresponda al tiempo de residencia; en varios supuestos no se exige la letra a)
  del art. 74. Las autorizaciones del art. 191.7 no pueden modificarse.

### H. Renovación (arts. 80 y 81)

- Plazo: dos meses antes de la caducidad o tres meses después, con posible sanción (art. 80.1).
- Supuestos del art. 80.2, letras a) a d): continuidad del contrato; tres meses de actividad por
  año más nuevo contrato, alta o búsqueda activa tras extinción ajena a su voluntad; prestaciones
  de la LOEX art. 38.6.b) y c); nueve meses de alta en doce, familiar que reúne los medios para
  reagruparle o violencia de género o sexual.
- Se valoran condenas y deudas (art. 80.5) y el esfuerzo de integración (art. 80.6); los
  descubiertos de cotización no impiden renovar si hay actividad habitual (art. 80.7). También
  deniegan las causas del art. 78 atribuibles al trabajador (art. 80.8).
- Silencio estimatorio a los tres meses (art. 80.9); duración de cuatro años con cualquier
  actividad y territorio y efectos retroactivos (art. 81). Si la autorización inicial duró menos de
  un año, la renovación dura lo que la actividad, con el máximo de un año (art. 81.1).

## Estrategia y jurisprudencia

1. Antes de redactar, descarta las causas del art. 78 con el empleador: son las que más deniegan
   y no se corrigen después.
2. Contrato: comprueba con `leer_convenio` la categoría y la tabla salarial del año; si el
   contrato queda por debajo, corrígelo antes de presentar. Mira con `vigencia_convenio` si el
   convenio está vencido, denunciado o con revisiones salariales registradas después del texto:
   `leer_convenio` lee el texto publicado, y a menudo no devuelve las tablas de los anexos ni las
   revisiones salariales publicadas aparte. Si tras dos intentos (`articulo` con el de
   retribuciones, `buscar_en` con la categoría) no obtienes la cuantía de la categoría, aplica la
   puerta: detén esa comprobación y pide al abogado la tabla vigente publicada. Si no la tiene,
   escribe la cuantía con un marcador, no afirmes que el salario se ajusta al convenio y dile en el
   resumen qué tabla y qué categoría debe comprobar. Contrasta también la jornada con el artículo de
   jornada del convenio y el salario con el real decreto del SMI.
3. Busca la doctrina con las consultas de la lista y, según el motivo, `consulta="denegación
   autorización residencia trabajo contrato convenio colectivo salario"` o `consulta="renovación
   autorización residencia trabajo extinción contrato causas ajenas demandante de empleo"`.
   Para antecedentes en la renovación, busca en `base="TS"` la doctrina sobre la valoración global
   de las circunstancias sin automatismo.
4. Muchas sentencias aplican aún el Real Decreto 557/2011 (sus artículos sobre cuenta ajena tienen
   otra numeración). Comprueba qué norma aplicó cada una y cita siempre el artículo vigente.
5. Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y cita fundamentos.

## Documento que se entrega

Formato, destinatario, citas y datos según `references/formato-y-organos.md`. El impreso oficial,
el modelo de contrato y la tasa se obtienen en la sede oficial: no indiques modelos, códigos ni
importes.

1. **Autorización inicial** —
   `solicitud-residencia-trabajo-cuenta-ajena-<apellido-trabajador>-<AAAAMMDD>.docx`, escrito del
   empleador dirigido a la OFICINA DE EXTRANJERÍA DE [PROVINCIA DEL CENTRO DE TRABAJO] o al órgano
   autonómico competente:
   - comparecencia del empleador y su representante, con los datos del trabajador;
   - EXPONE: empleador y actividad; puesto y ocupación; situación nacional de empleo (vía y
     prueba); contrato y ajuste al convenio (con el salario comparado); medios del empleador con
     el cálculo; cualificación del trabajador; ausencia de las causas del art. 78;
   - FUNDAMENTOS DE DERECHO: LOEX arts. 36 y 38 (y 40 si hay exención) y Reglamento arts. 73 a 77;
   - SOLICITA la concesión;
   - relación numerada de documentos.
2. **Cambio de empleador o modificación** —
   `comunicacion-cambio-empleador-<apellido-trabajador>-<AAAAMMDD>.docx` o
   `modificacion-autorizacion-<apellido-trabajador>-<AAAAMMDD>.docx`, con el supuesto del art. 79,
   190, 191 o 192 y sus requisitos como hechos numerados.
3. **Renovación** — `renovacion-residencia-trabajo-<apellido>-<AAAAMMDD>.docx`, escrito del
   trabajador a la oficina de extranjería con el supuesto del art. 80.2 que se invoca.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación, con su vigencia y
      sus notas de nulidad; norma aplicable por fecha justificada.
- [ ] Situación nacional de empleo acreditada por una vía concreta; el catálogo lo aportó el
      abogado con su referencia; si hay oferta, su texto se revisó (sin requisitos ajenos al puesto)
      y cada rechazo tiene causa concreta.
- [ ] Salario contrastado con la tabla del convenio leída (o, si el conector no la devuelve, con
      marcador y aviso) y SMI tomado del real decreto obtenido en esta conversación.
- [ ] Causas del art. 78 descartadas una a una con el empleador.
- [ ] Cada ECLI se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el texto completo y sus avisos corregidos.
- [ ] Marcadores en los datos no facilitados; nada inventado.
- [ ] Plazos con fecha y precepto: visado (art. 40.1.b), alta (art. 73.1), renovación (art. 80.1).
- [ ] Resumen para el abogado según el apartado 7 del formato, con los riesgos y el próximo paso.
