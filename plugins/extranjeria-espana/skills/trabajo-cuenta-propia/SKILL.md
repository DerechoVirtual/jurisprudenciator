---
name: trabajo-cuenta-propia
description: >-
  Prepara la solicitud de visado y autorización inicial de residencia temporal y trabajo por cuenta
  propia para el extranjero que quiere abrir un negocio o ejercer como autónomo en España (LOEX
  arts. 36.3 y 37; Reglamento de 2024, arts. 82 a 87; visado, arts. 38 y 39), el paso a cuenta
  propia desde otra situación y la renovación: requisitos de apertura y licencias, cualificación y
  colegiación, suficiencia de la inversión y creación de empleo con plan de negocio, orden público,
  alta en la Seguridad Social. Úsala con «quiero montar un negocio en España», «permiso de
  autónomo», «visado de trabajo por cuenta propia», «plan de negocio para extranjería», «renovar la
  cuenta propia». Si el proyecto es innovador y busca el informe de ENISA, usa
  `movilidad-internacional-ley-14-2013`; si va a ser asalariado, `trabajo-cuenta-ajena`; si está en
  España sin autorización, las skills de arraigo.
---

# Residencia temporal y trabajo por cuenta propia

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen legal** → `buscar_articulo` (`ley="LOEX"`, artículos 36 y 37).
- **Requisitos, procedimiento, visado, presentación y renovación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 26, 38, 39, 82 a 87 y 197; 193 a 195 para el órgano competente). Para saber si la comunidad autónoma resuelve la autorización inicial de trabajo, lee su Estatuto de Autonomía con `buscar_articulo` (Cataluña: `ley="Estatuto de Autonomía de Cataluña"`, artículo 138): `buscar_boe` no localiza los reales decretos de traspaso.
- **Paso a cuenta propia desde otra situación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 190, 191 y 192).
- **Requisitos de apertura, licencias y colegiación (art. 84.a y b)** → `buscar_boe` + `buscar_articulo` para la normativa sectorial o colegial de la actividad, y `buscar_ordenanzas` + `leer_ordenanza` para la licencia municipal cuando el municipio esté cubierto.
- **Sociedad a través de la que se ejercerá la actividad** → `buscar_empresa_mercantil` (nombre o CIF), si ya está constituida.
- **Norma aplicable a solicitudes anteriores al 20/05/2025** → `leer_boe` (`identificador="BOE-A-2024-24099"`, disposición transitoria segunda del Real Decreto) y, si rige el reglamento anterior, `buscar_articulo` (`ley="Real Decreto 557/2011"`).
- **Doctrina sobre los motivos de denegación** → `buscar_sentencias` (`consulta="autorización residencia trabajo cuenta propia suficiencia inversión"` o `consulta="autorización residencia trabajo cuenta propia licencia de apertura extranjero"`, `jurisdiccion="CONTENCIOSO"`, `base="AN"`, con `fecha_desde` en formato dd/mm/aaaa (por ejemplo `fecha_desde="01/01/2023"`; en formato aaaa-mm-dd se ignora) para no recibir pleitos urbanísticos antiguos; `base="TS"` para doctrina casacional) + `leer_sentencias` (`parrafos=3`).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Si citas una letra, escríbela detrás de la norma («artículo 84 del Real Decreto 1155/2024, letra a)»): con «artículo 84.a) del Real Decreto 1155/2024» `verificar_escrito` atribuye el artículo a la norma citada antes y puede darlo por inexistente. Tampoco reconoce las ordenanzas municipales: nómbralas completas y comprueba que no atribuya su artículo a otra norma.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Extranjero mayor de dieciocho años que reside fuera de España y quiere ejercer una actividad por
  cuenta propia aquí: visado de residencia y trabajo por cuenta propia, que conlleva la solicitud
  de la autorización inicial (arts. 39.1 y 85.1).
- Residente temporal o estudiante en España que quiere pasar a cuenta propia sin visado
  (arts. 190.3 y 191) o titular de cuenta ajena que quiere pasar a cuenta propia (art. 192.2).
- Renovación de la autorización por cuenta propia (arts. 86 y 87).

Usa otra skill cuando: el proyecto es una empresa innovadora o de especial interés económico que
necesita el informe de ENISA (`movilidad-internacional-ley-14-2013`, residencia para
emprendedores); el cliente será asalariado (`trabajo-cuenta-ajena`); está en España sin
autorización y el trabajo por cuenta propia sirve para un arraigo (`arraigo-social`,
`arraigo-sociolaboral`); es familiar de una persona con nacionalidad española (su autorización ya
habilita para trabajar por cuenta propia: art. 95.1, léelo; `familiares-de-espanoles`) o de un
ciudadano de otro Estado de la Unión (`ciudadanos-ue-y-familiares`). Si aún no está claro qué vía
conviene, usa antes `informe-viabilidad-extranjeria`.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes mientras falte un dato imprescindible (★).

1. ★ Trámite: visado inicial, paso desde otra situación en España o renovación. Si hay resolución
   denegatoria o requerimiento, el texto íntegro y su fecha de notificación.
2. ★ Solicitante: edad, nacionalidad, país de residencia (oficina consular: art. 26.1), situación
   en España si la tiene, antecedentes penales de los últimos cinco años, compromiso de no retorno.
3. ★ Actividad: qué hará, dónde (municipio, provincia y comunidad autónoma), forma jurídica
   (autónomo persona física o sociedad), si necesita local.
4. ★ Requisitos de apertura: licencias, autorizaciones sectoriales y colegiación que exige la
   actividad a un nacional; cuáles tiene ya y cuáles están en trámite.
5. ★ Cualificación o experiencia exigidas, títulos y su homologación si la profesión está regulada.
6. ★ Inversión: importe, origen de los fondos, destino (local, equipos, existencias, circulante) y
   financiación; empleo que se creará además del propio; plan de negocio con previsiones.
7. Solo renovación ★: continuidad de la actividad, altas y cotizaciones, obligaciones
   tributarias, cese de actividad reconocido, trabajador autónomo económicamente dependiente,
   menores a cargo, condenas; informe de esfuerzo de integración (opcional).

## Requisitos y comprobaciones

### A. Norma aplicable

- Lee cada artículo con `buscar_articulo` y aplica sus notas de nulidad.
- Solicitudes anteriores al 20/05/2025: disposición transitoria segunda (`leer_boe`); si rige el
  reglamento anterior, `ley="Real Decreto 557/2011"`. Si `leer_boe` no la devuelve completa,
  aplica la puerta.

### B. Requisitos específicos (art. 84; LOEX arts. 36.3 y 37.1)

| Letra | Requisito | Cómo se prueba |
|---|---|---|
| a) | Los requisitos que la legislación exige a los nacionales para abrir y hacer funcionar la actividad | Licencias, autorizaciones sectoriales o su solicitud; normativa leída con `buscar_boe`, `buscar_articulo` u ordenanza |
| b) | Cualificación profesional exigida o experiencia suficiente y, en su caso, colegiación | Títulos, homologación, certificados de experiencia, colegiación o su trámite |
| c) | Suficiencia de la inversión prevista e incidencia en el empleo, incluido el autoempleo | Plan de negocio, prueba y origen de los fondos, presupuestos, contratos de local |
| d) | Sin compromiso de no retorno vigente | Declaración |
| e) | Sin amenaza para el orden público | Antecedentes en España e informe policial; sin automatismo (art. 85.2) |
| f) | Tasa | Sede oficial |

- El art. 84 vigente no enumera los documentos ni exige un informe de viabilidad de una entidad
  concreta. El plan de negocio y, si el cliente lo obtiene, un informe de viabilidad de una
  organización profesional son los medios de prueba de la letra c). Dile al abogado que compruebe
  en la hoja informativa de la oficina consular o de extranjería qué documentos exige hoy.
- Para la letra a), identifica la norma sectorial con `buscar_boe` y lee sus artículos; para la
  licencia municipal, `buscar_ordenanzas` con el municipio. Lee también los planes especiales de
  usos que devuelva (densidades y distancias por tipo de establecimiento) y comprueba en la
  ordenanza en qué momento se presenta la comunicación o se pide la licencia (a menudo, al
  terminar las obras). Si el municipio no está cubierto, dilo y pide al abogado la ordenanza o el
  certificado municipal. No afirmes que una actividad no necesita licencia sin haberlo leído.
- Profesión colegiada (abogacía, arquitectura, profesiones sanitarias...): lee la norma de acceso y
  el estatuto general de la profesión (`buscar_boe` + `buscar_articulo`). La colegiación suele
  exigir la propia autorización de extranjería y el alta en la Seguridad Social: acredita todo lo
  que no depende de ellas (título, homologación, certificado del colegio de que solo falta eso) y
  explica ese círculo en el escrito. Si la profesión admite mutualidad alternativa al régimen de
  autónomos, avisa al abogado de que el art. 85.7 exige el alta «en el régimen correspondiente de
  la Seguridad Social» y de que la mutualidad puede discutirse.

### C. Procedimiento del visado inicial (arts. 39 y 85)

- La solicitud del visado conlleva la de la autorización (art. 39.1). El consulado valora el
  art. 38; la oficina de extranjería, o el órgano autonómico con competencias, los requisitos del
  art. 84 (arts. 39.3.b y 85.5). Si la comunidad autónoma tiene traspasada la autorización
  inicial por cuenta propia (compruébalo en su Estatuto: Cataluña, art. 138.2), la resolución es
  conjunta (art. 194.3): léelo y di al abogado qué órgano verifica cada aspecto. Si no consta
  competencia autonómica, resuelve la Delegación o Subdelegación del Gobierno de la provincia
  (art. 193.2). El conector no da la denominación vigente de los órganos autonómicos: déjala con
  marcador.
- Denegación: por incumplir el art. 84 o por documentos falsos, alegaciones inexactas o mala fe
  (art. 85.3). Resolución en tres meses desde la comunicación consular; silencio desestimatorio
  (art. 85.4).
- Concedida, el consulado expide el visado en el plazo del art. 39.5. Alta en la Seguridad Social
  en tres meses desde la entrada legal, que da eficacia a la autorización (art. 85.7); sin alta en
  ese plazo, obligación de salir (art. 85.9). Tarjeta en un mes desde el alta (art. 85.8).
- La autorización inicial dura un año y se limita a un sector de actividad y a un ámbito
  autonómico (art. 83). Varias comunidades a la vez exigen varias autorizaciones (art. 85.6).

### D. Paso a cuenta propia desde España

- Desde estancia por estudios con título obtenido: requisitos del art. 84 (art. 190.3), con los
  plazos y la autorización provisional del art. 190.6 y 190.7.
- Desde residencia temporal: lee el art. 191 y encaja el caso según el tiempo de residencia y si
  la autorización previa habilitaba para trabajar (art. 191.3 remite al art. 86; art. 191.4, al
  art. 84). Las autorizaciones del art. 191.7 no pueden modificarse.
- Desde cuenta ajena: art. 192.2 (la nueva autorización no amplía la vigencia).
- Plazo desde estudios (art. 190.6): cuenta desde la obtención del título y desde la extinción de
  la estancia; da las dos fechas y recomienda presentar antes de la primera.
- Presentación estando en España: personal, electrónica o por representante con apoderamiento
  notarial o apud acta (art. 197.1 y 197.4; su apartado 2 está anulado: lee la nota). En una
  comunidad con competencias, la solicitud de modificación la recibe el órgano autonómico
  (art. 195.2.b) y la resolución es conjunta (art. 194.3).
- Los arts. 190, 191 y 192.2 no fijan plazo de resolución ni sentido del silencio (el mes con
  silencio estimatorio del art. 192.1 es solo para modificar el alcance de la autorización inicial:
  ocupación, sector o territorio); el régimen general está en una disposición adicional de la Ley
  Orgánica 4/2000 que el conector no devuelve: no indiques plazo ni silencio y díselo al abogado.

### E. Renovación (arts. 86 y 87)

- Plazo: dos meses antes de la caducidad o tres meses después, con posible sanción (art. 86.1).
- Supuestos del art. 86.2: continuidad de la actividad con obligaciones tributarias y de
  Seguridad Social al día (los descubiertos no impiden renovar si la actividad es habitual);
  familiar que reúne los medios para reagruparle; protección por cese de actividad; autónomo
  económicamente dependiente cuyo contrato se extingue por causa ajena, incluida la víctima de
  violencia de género o sexual; situaciones de la LOEX art. 38.6.b) y c).
- Escolarización de menores (art. 86.3 y 86.4); valoración de condenas (art. 86.5); esfuerzo de
  integración, que puede alegarse si falta un requisito (art. 86.6).
- Silencio estimatorio a los tres meses (art. 87.2); duración de cuatro años para cualquier
  actividad y territorio, con efectos retroactivos (art. 87.1).
- Forma de presentación: el art. 197.2.d) obligaba a presentar la renovación por medios
  electrónicos, pero el Tribunal Supremo anuló el apartado 2 entero (nota del art. 197): no
  afirmes que la presentación electrónica es obligatoria.

### F. Causas de denegación en la jurisprudencia

Inversión insuficiente o sin origen acreditado; plan de negocio genérico o sin previsiones
verificables; falta de licencia o de la autorización sectorial; cualificación o colegiación no
acreditadas. Parte de la jurisprudencia sobre «cuenta propia» resuelve arraigos o circunstancias
excepcionales, no esta autorización: comprueba en cada sentencia qué figura se discutía.

## Estrategia y jurisprudencia

1. Traduce cada letra del art. 84 a una prueba concreta antes de redactar; si falta la licencia,
   acredita al menos su solicitud o lo que el orden de trámites permita y explica ese orden con la
   ordenanza leída: a menudo el título municipal solo se obtiene con las obras terminadas o con el
   alta, que presupone la autorización.
2. El plan de negocio debe cuadrar con la inversión probada: importes, calendario, ingresos
   previstos y empleo. Incluye un resumen de una página en la memoria y el plan como anexo.
3. Busca la doctrina con las consultas de la lista y, según el motivo,
   `consulta="visado residencia trabajo cuenta propia plan de negocio denegación"` o
   `consulta="renovación autorización cuenta propia continuidad actividad"`, con
   `jurisdiccion="CONTENCIOSO"` y `base="AN"`. Lee con `leer_sentencias` (`parrafos=3`) solo lo
   que vayas a citar.
4. Muchas sentencias aplican el Real Decreto 557/2011, con otra numeración. Comprueba qué norma
   aplicó cada una y cita siempre el artículo vigente leído.

## Documento que se entrega

Formato, destinatario, citas y datos según `references/formato-y-organos.md`. El impreso oficial y
la tasa se obtienen en la sede oficial: no indiques modelos, códigos ni importes.

1. **Visado inicial** —
   `solicitud-visado-cuenta-propia-<apellido>-<AAAAMMDD>.docx`, escrito de presentación y memoria
   que acompaña al impreso oficial, dirigido a la OFICINA CONSULAR DE ESPAÑA EN [CIUDAD]:
   - comparecencia del solicitante;
   - EXPONE: residencia actual; descripción de la actividad y su localización; un hecho por cada
     letra del art. 84 con su prueba; resumen del plan de negocio con tabla de inversión y origen
     de los fondos; empleo previsto;
   - FUNDAMENTOS DE DERECHO: LOEX arts. 36.3 y 37 y Reglamento arts. 38, 39, 83, 84 y 85, con su
     texto vigente;
   - SOLICITA el visado y la autorización inicial;
   - relación numerada de documentos, con el plan de negocio como anexo.
2. **Paso desde otra situación** — `modificacion-cuenta-propia-<apellido>-<AAAAMMDD>.docx`,
   dirigido a la OFICINA DE EXTRANJERÍA DE [PROVINCIA] o al órgano autonómico competente, con el
   supuesto de los arts. 190, 191 o 192 y los requisitos exigidos.
3. **Renovación** — `renovacion-cuenta-propia-<apellido>-<AAAAMMDD>.docx`, con el supuesto del
   art. 86.2 que se invoca y su prueba.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación, con su vigencia y
      sus notas de nulidad; norma aplicable por fecha justificada.
- [ ] Cada letra del art. 84 tiene su prueba o un marcador que dice qué falta.
- [ ] Órgano competente comprobado (Estatuto de Autonomía, arts. 193 a 195) y forma de
      presentación leída (art. 26 o art. 197 con su nota de nulidad).
- [ ] La normativa sectorial y la licencia se leyeron con el conector, o se avisa de que el
      municipio no está cubierto.
- [ ] Cada ECLI se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el texto completo y sus avisos corregidos.
- [ ] Marcadores en los datos no facilitados; ningún importe ni dato inventado.
- [ ] Plazos con fecha y precepto: presentación desde estudios (art. 190.6, con sus dos fechas),
      alta en la Seguridad Social (art. 85.7), renovación (art. 86.1).
- [ ] Resumen para el abogado según el apartado 7 del formato, con los riesgos (inversión,
      licencias, cualificación) y el próximo paso.
