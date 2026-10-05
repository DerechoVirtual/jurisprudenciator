---
name: residencia-no-lucrativa
description: >-
  Prepara la solicitud de visado de residencia temporal no lucrativa (que lleva consigo la
  autorización inicial y se presenta en el consulado) y la renovación de esa autorización en la
  oficina de extranjería, conforme al Reglamento de extranjería de 2024 (arts. 61 a 64; visado,
  arts. 37 a 39): medios económicos sobre el IPREM para el titular y cada familiar, seguro de
  enfermedad, antecedentes, residencia efectiva para renovar y prohibición de trabajar. Si el visado
  o la renovación se deniegan, prepara el recurso. Úsala con «visado no lucrativo», «residencia no
  lucrativa», «jubilado que quiere vivir en España», «renovar la no lucrativa», «me han denegado el
  visado por medios económicos». Si el cliente va a teletrabajar para empresas extranjeras, usa
  `movilidad-internacional-ley-14-2013`; si va a trabajar en España, `trabajo-cuenta-ajena` o
  `trabajo-cuenta-propia`.
---

# Residencia temporal no lucrativa: visado inicial, renovación y recurso

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Requisitos del visado y de la autorización inicial** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 26, 37, 38, 39, 61, 62 y 63).
- **Renovación, prórroga de la vigencia y extinción** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 64, 197, 199 y 200; `ley="LOEX"`, artículo 52 si la renovación se pide fuera de plazo).
- **Norma aplicable a solicitudes anteriores al 20/05/2025** → `leer_boe` (`identificador="BOE-A-2024-24099"`, disposición transitoria segunda del Real Decreto, al principio del texto) y, si rige el reglamento anterior, `buscar_articulo` (`ley="Real Decreto 557/2011"`).
- **Denegación del visado, motivación y recursos** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 27 y 28; `ley="LOEX"`, artículo 27; `ley="LPAC"`, artículos 30, 68, 112, 118, 123 y 124; `ley="LJCA"`, artículos 8, 10 y 46).
- **Doctrina sobre medios económicos, su origen y su fiabilidad** → `buscar_sentencias` (`consulta="visado residencia no lucrativa medios económicos origen fondos"`, `jurisdiccion="CONTENCIOSO"`, `base="AN"`, `anios=3`) + `leer_sentencias` (`parrafos=3`, `terminos` con el motivo).
- **Doctrina sobre seguro de enfermedad, intención de no trabajar y motivación** → `buscar_sentencias` (`consulta="residencia no lucrativa seguro de enfermedad carencias copago"` o `consulta="visado residencia no lucrativa intención de trabajar"`, `jurisdiccion="CONTENCIOSO"`, `base="AN"`) y, para la suficiencia de medios, `base="TS"` con `consulta="suficiencia de medios económicos extranjería"`.
- **Revisión del documento** → cada redactor del equipo pasa `verificar_escrito` solo sobre sus frases con normas, y el ensamblado rechaza cualquier ECLI o ROJ que ningún redactor leyera; `buscar_por_cita` se usa solo con un ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Si citas una letra, escribe «la letra b) del artículo 61.2 del Real Decreto 1155/2024», no «artículo 61.2.b) del…»: con la letra pegada, `verificar_escrito` atribuye el artículo a otra norma del mismo párrafo. Por la misma razón, cuando un párrafo cite más de una norma, nombra la norma en cada cita («el artículo 76.1 del Real Decreto 1155/2024», no «el mismo artículo» ni «el artículo 76.1» a secas).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

## Cuándo usarla

- Extranjero de un tercer país que vive fuera de España y quiere residir aquí sin trabajar, con
  pensión, rentas o patrimonio: visado de residencia no lucrativa. Su solicitud conlleva la de la
  autorización inicial (art. 63.1), así que el trámite empieza siempre en el consulado.
- Titular de una autorización no lucrativa que tiene que renovarla (art. 64).
- Visado o renovación denegados: esta skill analiza el motivo y redacta el recurso.

No la uses, y dilo al abogado, cuando:

- El cliente está en España en situación irregular: el visado exige no encontrarse irregularmente
  en territorio español (art. 38.b). Valora `arraigo-social`, `arraigo-sociolaboral` o las demás
  skills de arraigo.
- Quiere teletrabajar para empresas extranjeras o realizar cualquier actividad profesional: la no
  lucrativa no habilita para trabajar (art. 61.1). Usa `movilidad-internacional-ley-14-2013`
  (teletrabajo) o `trabajo-cuenta-ajena` / `trabajo-cuenta-propia`.
- Es familiar de una persona con nacionalidad española (arts. 93 a 99) o de un ciudadano de otro
  Estado de la Unión (Real Decreto 240/2007): usa `familiares-de-espanoles` o
  `ciudadanos-ue-y-familiares`.
- Ha dejado de ser familiar de un ciudadano de la Unión o de un español: puede pasar a la no
  lucrativa sin visado por el art. 191.8; léelo y adapta el escrito a la oficina de extranjería.
- Aún no está claro qué autorización le conviene: usa antes `informe-viabilidad-extranjeria`.

## Datos que hay que reunir antes de redactar

Saca estos datos de la documentación aportada, por este orden (paso 2 de `redaccion-rapida`). Si falta un dato imprescindible (★) que bloquee el escrito, pídelos todos a la vez en una única ronda de no más de cuatro preguntas; lo demás queda como `[PENDIENTE: dato]`.

1. ★ Trámite: visado inicial, renovación o recurso. Si es recurso: resolución íntegra, órgano que
   la dictó, fecha de notificación y pie de recursos; si durante la tramitación hubo requerimientos
   de subsanación, citaciones o entrevista (art. 27.3 a 27.5) y sobre qué; qué documentos se
   aportaron con la solicitud y cuáles se pueden aportar ahora.
2. ★ Fecha de presentación de la solicitud (o de la solicitud denegada). Si es anterior al
   20/05/2025, se aplica el apartado «Norma aplicable».
3. ★ Nacionalidad, país y ciudad de residencia actual (fija la oficina consular: art. 26.1) y si
   está o ha estado en España y en qué situación.
4. ★ Familiares que le acompañan: vínculo, edad, discapacidad o dependencia (art. 61.3).
5. ★ Medios económicos: clase (pensión, rentas, depósitos, dividendos, inmuebles), importe, moneda,
   titular, desde cuándo los percibe, origen de los saldos y documentos que los prueban. Si
   proceden de participaciones en empresas radicadas en España, quién administra esas empresas.
6. ★ Seguro de enfermedad: aseguradora, si está autorizada para operar en España, coberturas,
   carencias, copagos y periodo cubierto.
7. ★ Antecedentes penales en los países de residencia de los últimos cinco años y en España;
   certificado médico; pasaporte y su caducidad; si firmó un compromiso de no retorno.
8. Solo renovación ★: fecha de caducidad de la autorización, días de residencia efectiva en España
   en el año natural, mantenimiento del seguro, menores en edad de escolarización obligatoria,
   condenas y su cumplimiento, deudas tributarias o de Seguridad Social. Opcional: informe
   autonómico de esfuerzo de integración (art. 64.6).
9. Cifra mensual del IPREM vigente y norma del BOE que la fija (ver «Requisitos», apartado C).

## Requisitos y comprobaciones

### A. Norma aplicable

- Lee con `buscar_articulo` cada artículo antes de afirmarlo. Anota su fecha «vigente desde» y
  cualquier nota «Téngase en cuenta que se declara la nulidad…»: aplícala. A 27/09/2026 el
  conector devuelve anulado el art. 197.2 (obligación de presentar por medios electrónicos, entre
  otras, la renovación de la no lucrativa); comprueba la nota antes de indicar cómo presentar.
- Si la solicitud es anterior al 20/05/2025, lee la disposición transitoria segunda con
  `leer_boe`: se tramita con la norma vigente al presentarla salvo que el interesado pida el
  reglamento nuevo. Si rige el anterior, pide cada artículo con `ley="Real Decreto 557/2011"`.
  Si `leer_boe` no devuelve completa esa disposición, aplica la puerta: sin ella no se sabe qué
  norma rige.

### B. Visado inicial: quién valora qué

| Requisito | Precepto | Valora |
|---|---|---|
| Impreso, no estar irregular en España, no ser rechazable, pasaporte con un año de vigencia, antecedentes de cinco años, certificado médico, tasa | art. 38 | Oficina consular (art. 39.2) |
| Medios económicos suficientes y seguro de enfermedad | art. 61.2.a y b | Oficina consular (art. 39.2) |
| Compromiso de no retorno, amenaza para el orden público (antecedentes en España e informe policial), tasa | art. 61.2.c, d y e | Oficina de extranjería (arts. 39.3.a y 63.2) |

- La autorización inicial dura un año (art. 61.4). Comprueba el concepto de familiar en el
  art. 61.3 (pareja estable: vínculo duradero y, salvo descendencia común, un año de convivencia).
- Antecedentes policiales: no deniegan de forma automática; la oficina debe valorar el caso de
  forma circunstanciada (art. 63.3). Si hay antecedentes, prepara la argumentación desde ese
  precepto.

### C. Medios económicos (art. 62)

- Cuantía: el porcentaje del IPREM que fija el art. 62.1 para el titular más el de cada familiar a
  cargo, calculado mensualmente y multiplicado por los meses de vigencia de la autorización que se
  pide (art. 62.2): un año en la inicial (art. 61.4) y dos en la renovación (art. 64.7). Copia los
  porcentajes del texto que devuelva `buscar_articulo`.
- El importe del IPREM lo fijan normas presupuestarias que Jurisprudenciator no devuelve (ni
  `buscar_boe` las localiza). Pide al abogado la cifra mensual vigente y la norma que la fija;
  no la pongas de memoria. Si no la facilita, usa el marcador `[IPREM MENSUAL VIGENTE Y NORMA]`,
  no afirmes en el escrito que el requisito se cumple y dilo en el resumen. Si facilita la cifra
  pero no la norma, calcula con la cifra, escribe la norma con el marcador `[NORMA QUE FIJA EL
  IPREM]` y avísalo en el resumen.
- Prueba (art. 62.3): cualquier medio admitido en Derecho. Para cuentas en el extranjero exige
  los cuatro datos del art. 62.3 (entidad y domicilio, identificación de las cuentas, fechas,
  saldo a 31 de diciembre del año anterior y saldo medio del último año). Si los medios vienen de
  acciones o participaciones en empresas radicadas en España, añade la certificación de que no
  ejerce actividad laboral en ellas y la declaración responsable.
- Presenta una tabla: fuente, importe mensual, documento, periodo; y otra con el cálculo exigido.

### D. Seguro de enfermedad (art. 61.2.b; renovación, art. 64.2.c)

- El Reglamento exige «un seguro de enfermedad» sin detallar coberturas. Las exigencias prácticas
  del consulado (carencias, copagos, límites) no están en el Reglamento: dile al abogado que las
  compruebe en la hoja informativa de la oficina consular y busca la doctrina sobre esa exigencia.
- Compara las fechas de la póliza con la entrada prevista y con el año de la autorización
  (art. 61.4): si la póliza empieza después de la entrada o vence antes de que acabe ese año,
  adviértelo en el resumen para que se ajuste antes de presentar.

### E. Prohibición de trabajar

- La autorización no habilita para trabajar (art. 61.1). Para trabajar hace falta modificarla
  (art. 191: léelo para ver qué requisitos se exigen según el tiempo de residencia). Las
  actividades exceptuadas de autorización de trabajo tienen su propia figura (arts. 88 y 89).
- Si hay indicios de actividad laboral en España (socio que gestiona una empresa, teletrabajo,
  contrato), advierte al abogado del riesgo de denegación y de extinción (art. 200.2.c).

### F. Plazos del visado inicial

- La oficina de extranjería resuelve en un mes desde que recibe la comunicación consular; el
  silencio es desestimatorio (art. 63.4). El visado se expide en un mes desde la resolución
  favorable (art. 39.5); se recoge en el plazo del art. 28.4. La tarjeta de identidad de extranjero
  se pide personalmente en un mes desde la entrada (arts. 37.3 y 63.5).

### G. Renovación (art. 64)

- Plazo: los dos meses previos a la caducidad; también dentro de los tres meses posteriores, con
  prórroga de la autorización pero con posible sanción (art. 64.1; LOEX art. 52). Calcula las
  fechas exactas y escríbelas.
- Requisitos del art. 64.2, letras a) a f): autorización en vigor o dentro de esos tres meses,
  medios del art. 62 para dos años, seguro mantenido, menores escolarizados, tasa y **residencia
  real y efectiva de más de 183 días en el año natural** (letra f). Pide prueba de ese periodo.
- Se valoran condenas cumplidas o suspendidas e incumplimientos tributarios o de Seguridad Social
  (art. 64.5) y el esfuerzo de integración (art. 64.6), que puede suplir un requisito no cumplido.
- Resolución en tres meses; el silencio es estimatorio (art. 64.8). Vigencia de dos años salvo que
  proceda la larga duración (art. 64.7). Tarjeta: un mes desde la notificación (art. 64.9).

### H. Denegación y recursos

- Causas de denegación del visado: art. 28.5. La denegación debe motivarse (art. 28.6) y expresar
  recurso, órgano y plazo (art. 28.7). Si la autorización se deniega, el consulado deniega el
  visado (art. 28.10).
- Toma el recurso del pie de la resolución y compruébalo: reposición potestativa en un mes si el
  acto pone fin a la vía administrativa (LPAC arts. 123 y 124), o contencioso en dos meses (LJCA
  art. 46). Qué actos agotan la vía lo dice una disposición adicional del Reglamento que el
  conector no devuelve: si el pie de recursos falta o es contradictorio, aplica la puerta.
- Órgano judicial: determínalo con `buscar_articulo` (LJCA arts. 8 y 10) y jurisprudencia reciente
  de competencia antes de encabezar. En denegaciones consulares no des por supuesta la sala:
  mira qué órgano dictó las sentencias de visados que devuelva Jurisprudenciator y confirma su
  competencia con la LJCA.
- Si la oficina consular denegó por un defecto documental (certificado bancario incompleto, póliza
  con carencias o copagos) sin requerir antes su subsanación, alega el art. 27.4 en relación con la
  LPAC art. 68. En reposición, los documentos nuevos se valoran si no hubo trámite de alegaciones
  en el que pudieran aportarse (LPAC art. 118.1): acompáñalos con un otrosí que lo razone. Calcula
  el plazo del recurso con la LPAC art. 30.4 (de fecha a fecha) y escribe la fecha final.
- Causas de denegación que aparecen en la jurisprudencia: saldos puntuales o sin origen
  acreditado, ingresos incoherentes con el perfil del solicitante, seguro con carencias o copagos,
  indicios de que va a trabajar, antecedentes y desistimiento por no atender requerimientos
  (art. 27.5).

## Estrategia y jurisprudencia

1. Construye la prueba de medios pensando en la fiabilidad: ingresos periódicos y documentados
   pesan más que un saldo reciente; si hay un ingreso extraordinario, acredita su origen (venta,
   herencia, liquidación) con documentos.
2. Busca la doctrina con las consultas de la lista y añade, según el caso:
   - `consulta="visado residencia no lucrativa medios económicos insuficientes"`;
   - `consulta="renovación residencia no lucrativa medios económicos"`;
   - `consulta="denegación visado motivación indefensión"` si la resolución es estereotipada.
   Filtra con `jurisdiccion="CONTENCIOSO"` y `base="AN"`; usa `base="TS"` para doctrina casacional.
   Lee con `leer_sentencias` (`parrafos=3`) solo las que vayas a citar.
3. Muchas sentencias recientes aplican aún el Real Decreto 557/2011 por la fecha de la solicitud.
   Comprueba qué reglamento aplicó cada una. Usa su doctrina solo si el requisito es equivalente
   en el texto vigente, y cita siempre el artículo vigente leído con `buscar_articulo`.
4. En la solicitud inicial la jurisprudencia es innecesaria salvo para anticipar un punto dudoso.
   En el recurso, cada motivo de denegación recibe su propio fundamento con el párrafo literal
   que lo desmonta y el documento que lo prueba.

## Documento que se entrega

Formato, destinatario, citas y datos según `references/formato-y-organos.md`. El impreso oficial
de solicitud y la tasa se obtienen en la sede oficial: no indiques modelos, códigos ni importes.

1. **Visado inicial** — `solicitud-visado-no-lucrativa-<apellido>-<AAAAMMDD>.docx`. Escrito de
   presentación y memoria que acompaña al impreso oficial, dirigido a la OFICINA CONSULAR DE
   ESPAÑA EN [CIUDAD]:
   - comparecencia del solicitante (y del representante solo si el art. 26.1 lo permite);
   - EXPONE, en hechos numerados: residencia actual y propósito de residir sin actividad laboral;
     familiares que le acompañan; medios económicos con tabla de fuentes y tabla de cálculo;
     seguro; antecedentes, certificado médico y pasaporte; ausencia de compromiso de no retorno;
   - FUNDAMENTOS DE DERECHO: arts. 38, 39, 61, 62 y 63 con su texto vigente;
   - SOLICITA la concesión del visado y de la autorización inicial;
   - declaración responsable de no ejercer actividad laboral o profesional en España y, si procede,
     la del art. 62.3 sobre participaciones en empresas;
   - relación numerada de documentos.
2. **Renovación** — `renovacion-no-lucrativa-<apellido>-<AAAAMMDD>.docx`, dirigido a la OFICINA DE
   EXTRANJERÍA DE [PROVINCIA] (art. 64.1; competencia territorial: art. 193.2). Hechos sobre cada
   letra del art. 64.2, con el cálculo de medios para dos años y la prueba de los días de residencia.
3. **Recurso** — `recurso-reposicion-no-lucrativa-<apellido>-<AAAAMMDD>.docx` (o el recurso que
   proceda), dirigido al órgano que dictó la resolución: identificación del acto y fecha de
   notificación; hechos; un fundamento por motivo de denegación con doctrina y prueba; SOLICITA la
   revocación y la concesión; otrosí con los documentos nuevos.

**Reparto para la redacción rápida:** visado inicial: 01 comparecencia y hechos (residencia, propósito y familiares); 02 medios económicos con las tablas de fuentes y de cálculo (que el director deja calculadas en `caso.md`); 03 seguro, antecedentes y certificado médico, fundamentos (arts. 38, 39, 61, 62 y 63), solicita, declaraciones responsables y documentos. Renovación: 01 hechos por cada letra del art. 64.2; 02 medios para dos años, solicita y documentos. Recurso: una sección por motivo de denegación.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación, con su fecha de
      vigencia y sus notas de nulidad; la norma aplicable por fecha está justificada.
- [ ] El cálculo de medios usa los porcentajes leídos y un IPREM facilitado por el abogado con su
      norma, o lleva el marcador y el aviso.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; se citan
      fundamentos, no hechos ni datos de aquellas partes.
- [ ] `verificar_escrito` pasado por cada redactor sobre sus frases con normas y sus avisos corregidos.
- [ ] Marcadores en todos los datos no facilitados; ningún dato inventado.
- [ ] Plazo con fecha inicial, precepto y fecha final (renovación o recurso).
- [ ] Resumen para el abogado según el apartado 7 del formato: documento y órgano, plazo, riesgos
      (fiabilidad de medios, seguro, indicios de trabajo), tabla de jurisprudencia y próximo paso.
