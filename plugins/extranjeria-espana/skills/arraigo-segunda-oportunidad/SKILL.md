---
name: arraigo-segunda-oportunidad
description: >-
  Prepara la solicitud de autorización de residencia temporal por arraigo de segunda oportunidad (arts.
  125.1.a y 127.a del Reglamento aprobado por el Real Decreto 1155/2024) con memoria justificativa en Word y
  relación de documentos para la Oficina de Extranjería. Úsala cuando el abogado diga «segunda oportunidad»,
  «tenía papeles y los perdió», «no pudo renovar la tarjeta», «le denegaron la renovación» o «se le caducó la
  residencia». Comprueba que la residencia anterior no fuera por circunstancias excepcionales, que se tuviera
  en los dos años anteriores, el motivo de la no renovación, la permanencia y los antecedentes. Si aún está a
  tiempo de renovar, renueva; si la residencia anterior era un arraigo, pide su prórroga; si nunca tuvo
  residencia, usa arraigo-social, arraigo-sociolaboral o arraigo-socioformativo; si es progenitor de un menor
  de otro Estado de la UE, arraigo-familiar.
---

# Arraigo de segunda oportunidad

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Base legal y requisitos vigentes** → `buscar_articulo` (`ley="LOEX"`, `articulo="31"`) y `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"124"`, `"125"`, `"126"` y `"127"`).
- **Vigencia y renovación de la autorización anterior** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, `articulo="200"`) y el artículo de renovación de ese tipo de autorización (por ejemplo `"80"` para cuenta ajena; localiza el de los demás tipos en `references/anclas-normativas-extranjeria.md` y léelo). **Si la renovación se pidió antes del 20/05/2025**, se tramitó con el reglamento anterior (disposición transitoria segunda del Real Decreto 1155/2024, que devuelve `leer_boe` con `identificador="BOE-A-2024-24099"`): lee también el artículo de renovación de entonces con `ley="Real Decreto 557/2011"` (por ejemplo `"71"` para cuenta ajena) y cítalo como fuente de la prórroga de vigencia.
- **Fecha en que terminó la prórroga de vigencia** (solo si el cálculo depende de ella) → `buscar_articulo` (`ley="LPAC"`, artículos `"39"` y `"40"`).
- **Procedimiento, trabajo, prórroga y paso posterior** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"130"`, `"131"`, `"132"`, `"191"`, `"193"` y `"197"`).
- **Cancelación de antecedentes** (si hay antecedentes) → `buscar_articulo` (`ley="CP"`, `articulo="136"`).
- **Doctrina sobre la nueva figura, la denegación de renovaciones y los antecedentes** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"`; `base="TS"` para el Supremo) + `leer_sentencias` (`parrafos=3`).
- **Reformas del Reglamento** → en cada artículo que devuelva `buscar_articulo`, la línea «redacción vigente dada por…» y las notas «Téngase en cuenta…» (`buscar_boe` no localiza las reformas); si hay que leer la norma que reformó, `leer_boe` con su identificador.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

## Cuándo usarla

Si aún no está claro qué vía conviene al cliente, empieza por `extranjeria-intake` o `informe-viabilidad-extranjeria`; para revisar un expediente documental ya reunido, `documentacion-expediente`. Si la solicitud ya se presentó y hay requerimiento, denegación o archivo, esta skill no es la herramienta: `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria`.

- Persona extranjera que **fue titular de una autorización de residencia** que no se otorgó por circunstancias excepcionales, dentro de los **dos años inmediatamente anteriores** a la solicitud, y que **no la renovó** por motivos distintos del orden público, la seguridad o la salud pública (art. 127.a): falta de contrato o de cotización, falta de medios, renovación presentada fuera de plazo, requisito del empleador, etc.
- Si la no renovación se debió a orden público, solo cabe cuando hubo **sentencia denegatoria, sobreseimiento o absolución** (art. 127.a, último inciso).
- Además, los requisitos generales del art. 126, **incluidos los dos años de permanencia continuada**: esta figura no los exime.

**Detector** (antes de redactar; si encaja otra vía, dilo al abogado con el artículo leído):

| Situación del cliente | Vía que procede |
|---|---|
| La autorización venció hace menos de tres meses | renovación fuera de plazo por el artículo de renovación de su tipo (por ejemplo, art. 80.1), que prorroga la validez hasta la resolución, sin perjuicio del expediente sancionador que ese mismo artículo prevé |
| La denegación de la renovación se notificó **después** del plazo máximo para resolverla (en cuenta ajena, tres meses con silencio estimatorio, art. 80.9; compruébalo en el artículo de su tipo y, si se pidió antes del 20/05/2025, en el del Real Decreto 557/2011) | no redactes todavía: la renovación pudo quedar concedida por silencio y el cliente sería titular de una autorización (art. 126.h). Explica el problema al abogado y valora con él `recurso-administrativo-extranjeria` o `renovacion-modificacion-extincion` |
| La autorización anterior era un arraigo u otra por circunstancias excepcionales | no cabe esta figura; prórroga del art. 132.3 si está en plazo, o el arraigo que corresponda |
| La renovación se denegó y aún está en plazo de recurso | valora primero `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria`, y ten en cuenta el art. 126.h |
| La no renovación fue por antecedentes u orden público, sin absolución ni sobreseimiento | no cabe esta figura; revisa si la denegación de la renovación respetó el art. 31.7 LOEX (valoración, no automatismo) y, si está en plazo, recurre con `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria` |
| Tuvo una estancia por estudios (no residencia) | el art. 127.a habla de residencia: valora `estudiantes-y-busqueda-empleo` (art. 190) si aún está en plazo, o arraigo-social, sociolaboral o socioformativo |
| Tuvo autorización de familiar de español o tarjeta de familiar de ciudadano de la Unión y cesó el vínculo | lee el art. 191.8 y consulta `familiares-de-espanoles` (residencia independiente) o `ciudadanos-ue-y-familiares` (conservación del derecho) |
| Perdió una residencia de larga duración | `larga-duracion` (recuperación, arts. 186-189) |
| Nunca tuvo residencia, o la perdió hace más de dos años | arraigo-social, arraigo-sociolaboral o arraigo-socioformativo |
| Progenitor o tutor de menor de otro Estado de la UE, el EEE o Suiza | arraigo-familiar (art. 127.e), sin permanencia mínima |
| Familiar de español | `familiares-de-espanoles` (arts. 93-99) |
| Orden de expulsión vigente o prohibición de entrada | `expulsion-procedimiento-sancionador` (la expulsión archiva cualquier procedimiento de residencia, art. 244.3) |

## Datos que hay que reunir antes de redactar

No redactes al primer disparo. Pide los imprescindibles (★) que falten:

1. ★ Nacionalidad, pasaporte en vigor y provincia de residencia efectiva (art. 193.2).
2. ★ **Autorización anterior**: tipo exacto, fechas de concesión y de fin de vigencia, número de expediente (`[NÚMERO DE EXPEDIENTE]`) y copia de la TIE o de la resolución.
3. ★ **Qué pasó con la renovación**: si se pidió y cuándo (en plazo o fuera de él), resolución denegatoria con **su fecha y la de su notificación** (y el acuse de notificación) y motivo literal, recursos presentados y su estado; o si no se pidió, por qué. Comprueba que la denegación se notificó dentro del plazo máximo para resolver la renovación (ver el detector).
4. ★ Si el motivo fue orden público, seguridad o salud pública: procedimiento penal y su final (sentencia absolutoria, auto de sobreseimiento, sentencia condenatoria), con firmeza.
5. ★ Permanencia continuada en España los dos años anteriores a la fecha prevista de presentación, incluidas salidas.
6. ★ Antecedentes penales en España y en los países de residencia de los cinco años previos a la entrada; antecedentes policiales; expulsiones o prohibiciones de entrada.
7. ★ Procedimientos de autorización en trámite (recursos incluidos) y solicitudes de protección internacional.
8. Situación laboral actual y prevista (útil para la prórroga y para la modificación posterior).
9. Representación del abogado (art. 197.4).

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo; aplica las notas «Téngase en cuenta» sobre nulidad si aparecen.

**Específico (art. 127.a)**:

- **Titularidad previa de una autorización de residencia no excepcional**: comprueba el tipo en la resolución de concesión. Quedan fuera las del título VII (arraigos, razones humanitarias, colaboración, víctimas).
- **Dentro de los dos años inmediatamente anteriores a la solicitud**: calcula la **fecha límite de presentación** (fin de la titularidad + dos años) y dásela al abogado. Si la renovación se pidió en plazo, la validez de la autorización se prorrogó «hasta la resolución del procedimiento» (art. 200.1 y el artículo de renovación de su tipo). Calcula **tres** fechas: desde el fin de vigencia original (prudente), desde la fecha de la resolución denegatoria y desde su notificación. Contar desde la notificación es sostenible (arts. 39.2 y 40.1 de la Ley 39/2015), pero choca con el art. 39.1 (los actos producen efectos desde que se dictan) y no hay doctrina que lo resuelva: si solo la fecha de la notificación deja la solicitud en plazo, aplica la puerta (paso 5 de la estrategia) y advierte del riesgo alto. El recurso de reposición o el contencioso contra la denegación no prorrogan la vigencia: no cuentes desde su resolución. Presenta antes de la más temprana si es posible; si no, advierte del riesgo. Si el plazo vence en un día inhábil o de inmediato, recuerda que el registro electrónico admite presentaciones todos los días a cualquier hora (art. 31.2 de la Ley 39/2015, léelo).
- **Motivo de la no renovación distinto del orden público, la seguridad o la salud pública**: cita el motivo literal de la resolución. Si el motivo fue de orden público, exige la sentencia absolutoria, el sobreseimiento o la «sentencia denegatoria» del art. 127.a. Ese último término no está definido: léelo en su contexto, dilo al abogado y no le des un contenido que el texto no tenga.

**Generales (art. 126, acumulativos)**: estar en España sin ser solicitante de protección internacional (a); **dos años de permanencia continuada** (b); no ser amenaza para el orden público (c); carecer de antecedentes penales en España y en los países de residencia de los cinco años anteriores a la entrada (d, y art. 31.5 LOEX), con el cálculo de cancelación del art. 136 CP; no ser rechazable en Schengen (e); no estar en plazo de no retorno (f); tasa abonada, sin dar importe ni modelo: remite a la sede oficial (g); **no ser titular de autorización de estancia o residencia ni interesado en procedimientos de concesión, prórroga, renovación o modificación en trámite** (h). Si hay un recurso pendiente contra la denegación de la renovación, advierte al abogado de que la oficina puede considerarlo procedimiento en trámite de renovación y decide con él entre mantener el recurso o desistir antes de presentar.

**Normas que el conector no devuelve por `buscar_articulo`:**

- Disposiciones adicionales vigésima y vigesimoprimera del Reglamento (arraigo de solicitantes de protección internacional y arraigo extraordinario, que solo podían pedirse hasta el 30/06/2026): léelas con `leer_boe` (`identificador="BOE-A-2026-8284"`, Real Decreto 316/2026). Si el cliente tiene una de esas solicitudes sin resolver, choca con el art. 126.h.
- Solicitudes de arraigo presentadas desde el 20/05/2025 hasta la entrada en vigor del Real Decreto 316/2026 (sus redacciones rigen desde el 16/04/2026) y aún en trámite: su régimen está en la disposición transitoria segunda de ese real decreto, que `leer_boe` no llega a devolver. Si el caso depende de ella, aplica la puerta y di al abogado qué precepto falta.

**Procedimiento y efectos**:

- Solicitud personal (o por representante acreditado, art. 197.4) ante la oficina de la provincia de residencia, sin visado, con pasaporte en vigor y documentación del supuesto (art. 130.1).
- Certificados de antecedentes de los países de residencia de los cinco años previos a la entrada: normalmente no hacen falta si lleva cinco años continuados en España o los acreditó en otra solicitud de los últimos cinco años sin salir (art. 130.2), algo frecuente en quien ya tuvo residencia. La oficina pide de oficio penados e informe policial; los antecedentes policiales exigen valoración individual (art. 130.2). Subsanación en el plazo que fije la oficina, máximo quince días (art. 130.3).
- Concedida: un año (art. 125.2) con autorización de trabajo por cuenta ajena o propia sin límites (art. 131). TIE en un mes desde la notificación (art. 130.6).
- Prórroga: búsqueda activa de empleo e inscripción en el servicio público de empleo, salvo impedimentos justificados (art. 132.2.a), en los dos meses anteriores o tres posteriores al vencimiento (art. 132.3). Tras un año de residencia, modificación del art. 191.3 a una autorización de residencia y trabajo de cuatro años, acreditando los requisitos de renovación del art. 80 (cuenta ajena) o del art. 86 (cuenta propia): explica al cliente desde el principio qué necesitará para no repetir la pérdida de la residencia.
- Plazo máximo de resolución y silencio: en disposiciones adicionales que el conector no devuelve. No los afirmes; remite al BOE consolidado.

**Causas típicas de denegación y cómo rebatirlas:**

| Causa | Respuesta |
|---|---|
| La autorización anterior era excepcional | No hay réplica: cambiar de figura |
| Han pasado más de dos años desde la titularidad | Prórroga legal de la vigencia mientras se tramitaba la renovación (art. 200.1); si no la hubo, cambiar de figura |
| La no renovación fue por orden público | Sentencia absolutoria, sobreseimiento firme o resolución del art. 127.a; si no existe, no cabe |
| Falta de permanencia continuada de dos años | Prueba por tramos (TIE, vida laboral, padrón, contratos de alquiler); doctrina sobre ausencias |
| Antecedentes penales | Cancelación o deber de cancelación (art. 136 CP) y doctrina del Supremo |
| Recurso o renovación pendiente | Art. 126.h: resolver antes la situación del procedimiento anterior |

## Estrategia y jurisprudencia

1. Descarta primero la renovación: si aún se puede renovar, esa vía conserva la antigüedad de la residencia y es mejor que empezar de nuevo con un arraigo.
2. Obtén la resolución denegatoria completa: el motivo literal decide si la figura cabe.
3. Entrega al abogado esta tabla con fechas concretas (sin las fechas de la autorización anterior y de la notificación de la denegación no hay cálculo: pídelas):

   | Hito | Precepto | Cálculo |
   |---|---|---|
   | Fin de vigencia original de la autorización | resolución de concesión o TIE | fecha que conste en el documento |
   | Fin de la validez prorrogada, si pidió la renovación en plazo | art. 200.1 y artículo de renovación de su tipo | fecha de la resolución de la renovación y, aparte, fecha de su notificación |
   | Fecha límite prudente de presentación | art. 127.a | fin de vigencia original + dos años |
   | Fecha límite defendible | arts. 127.a y 200.1 | fecha de la resolución + dos años |
   | Fecha límite máxima (riesgo alto, sin doctrina) | arts. 127.a y 200.1; arts. 39.2 y 40.1 de la Ley 39/2015 | fecha de la notificación + dos años |
   | Se cumplen los dos años de permanencia | art. 126.b | fecha desde la que hay prueba continuada + dos años |

   Si la permanencia de dos años se cumple después de la fecha límite prudente, dilo: la figura puede quedar fuera de alcance y habrá que ir al arraigo que corresponda. Si la fecha prudente ya pasó y el cliente tiene dos años de permanencia, ofrece además la alternativa del arraigo sociolaboral o social (letras b y c del art. 127) y advierte de que no pueden pedirse a la vez: la letra h) del art. 126 impide solicitar un arraigo con otro procedimiento de autorización en trámite.
4. Es una figura nueva desde el 20/05/2025 y la doctrina es escasa. Consultas (máximo dos reformulaciones):
   - `buscar_sentencias` (`consulta="\"segunda oportunidad\" arraigo"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="20/05/2025"`); si no hay resultados, sin comillas.
   - `consulta="denegación renovación autorización de residencia motivo"`, `base="AN"`, `fecha_desde="20/05/2025"`, para conocer los motivos habituales y cómo se revisan.
   - `consulta="solicitud de renovación en plazo prórroga de la vigencia hasta la resolución"`, `base="AN"`.
   - `consulta="renovación autorización residencia antecedentes penales valoración artículo 31.7"`, `base="TS"`.
   - Antecedentes: `consulta="arraigo antecedentes penales cancelados o cancelables artículo 136 Código Penal"`, `base="TS"`.
5. Si tras dos reformulaciones no hay doctrina sobre el art. 127.a, aplica la puerta: detente **antes de redactar**, dile al abogado qué consultas han fallado (cada una con su texto), la tabla de fechas del paso 3 y que la memoria solo podría apoyarse en el texto literal del artículo; espera su respuesta, porque es él quien decide si se presenta así. Si decide presentar, redacta y deja constancia en el fundamento de doctrina de que no la hay publicada sobre el requisito (sin nombrar la herramienta), y repite el aviso en el resumen. Nunca rellenes ese hueco con doctrina de otra figura presentada como si fuera de esta: comprueba de qué arraigo trata cada resultado antes de citarlo (los buscadores devuelven sentencias de arraigo socioformativo o social que transcriben el art. 125 completo).
6. Transcribe solo párrafos de fundamentos leídos con `leer_sentencias`, nunca hechos ni datos de las partes de aquel pleito.

**Al citar una sentencia**, comprueba qué reglamento aplicó (Real Decreto 557/2011 o Real Decreto 1155/2024: fecha de la solicitud de aquel caso y artículos que cita) y dilo en el escrito. Si aplicó el anterior, cítala solo para requisitos que los arts. 126 y 127 vigentes mantienen iguales. Si la resolución anula o interpreta un precepto del Reglamento vigente, contrasta que la nota «Téngase en cuenta» de `buscar_articulo` lo refleja.

## Documento que se entrega

Un Word maquetado según `references/formato-y-organos.md`: **solicitud de autorización de residencia temporal por circunstancias excepcionales por arraigo de segunda oportunidad con memoria justificativa**. Acompaña al impreso oficial vigente, que el abogado descarga de la sede.

Nombre: `solicitud-arraigo-segunda-oportunidad-<apellido-cliente>-<AAAAMMDD>.docx`.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» (la primera vez, «, de 19 de noviembre, por el que se aprueba el Reglamento de la Ley Orgánica 4/2000») y la ley como «artículo 31.3 de la Ley Orgánica 4/2000», según el apartado 4 del formato: así `verificar_escrito` reconoce cada cita. Nunca «del Reglamento de Extranjería». El reglamento anterior, como «artículo 71.1 del Real Decreto 557/2011»; la Ley 39/2015, como «artículo 39.2 de la Ley 39/2015».

**Letras, siempre delante del artículo**: «la letra a) del artículo 127 del Real Decreto 1155/2024», «la letra a) del artículo 125.1 del Real Decreto 1155/2024». Con «artículo 127.a) del…» o «artículo 127, letra a), del…» `verificar_escrito` no identifica la norma y atribuye la cita a la última norma mencionada en el texto. Dentro de un artículo ya nombrado, «(letra b)» sí funciona.

Estructura:

1. **Encabezamiento**: «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA] — [DELEGACIÓN / SUBDELEGACIÓN] DEL GOBIERNO» (art. 193.2).
2. **Comparecencia** con marcadores (`[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[DOMICILIO]`) y representación (art. 197.4).
3. **EXPONE — HECHOS**: PRIMERO.- Identidad y entrada. SEGUNDO.- Autorización anterior: tipo, fechas y `[NÚMERO DE EXPEDIENTE]`. TERCERO.- Renovación: solicitud, resolución, motivo literal y firmeza; o por qué no se pidió. CUARTO.- Si hubo motivo de orden público, final del procedimiento penal. QUINTO.- Permanencia continuada de los dos últimos años. SEXTO.- Antecedentes y situación administrativa actual.
4. **FUNDAMENTOS DE DERECHO**: I. Marco legal (art. 31.3 LOEX; arts. 124 y 125.1.a). II. Procedimiento y competencia (arts. 130, 193.2 y 197). III. Requisito específico (art. 127.a): naturaleza de la autorización anterior, cómputo de los dos años (con el art. 200.1 si procede) y motivo de la no renovación. IV. Requisitos generales (art. 126). V. Doctrina con párrafo literal y ECLI, o constancia de que no la hay sobre el art. 127.a. VI. Efectos (arts. 125.2 y 131).
5. **SOLICITA**: admisión a trámite y concesión por un año con habilitación para trabajar.
6. **OTROSÍ**: que se incorpore el expediente anterior que obra en la propia oficina; que se recaben de oficio los informes del art. 130.2.
7. Lugar, fecha y firma.
8. **RELACIÓN DE DOCUMENTOS** numerada: impreso oficial; justificante de la tasa; pasaporte completo; TIE o resolución de la autorización anterior; solicitud de renovación y resolución denegatoria con su notificación; resolución penal absolutoria o de sobreseimiento, si procede; prueba de permanencia por tramos; certificados de antecedentes si no concurren las excepciones del art. 130.2; representación.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: LOEX 31; Reglamento 124, 125, 126, 127, 130, 131, 132, 193, 197 y 200, y el artículo de renovación del tipo de autorización anterior; fechas de vigencia y notas de nulidad revisadas.
- [ ] Descartada la renovación en plazo o fuera de plazo y la prórroga del art. 132.3.
- [ ] Autorización anterior no excepcional y motivo de la no renovación comprobados con la resolución.
- [ ] Fechas límite calculadas desde el fin de vigencia original, desde la resolución de la renovación y desde su notificación, con su precepto; comprobado que la denegación se notificó dentro del plazo para resolver (sin silencio estimatorio).
- [ ] Si la renovación se pidió antes del 20/05/2025: leídos la disposición transitoria segunda del Real Decreto 1155/2024 (`leer_boe`) y el artículo de renovación del Real Decreto 557/2011.
- [ ] Letras citadas delante del artículo («la letra a) del artículo 127 del Real Decreto 1155/2024»).
- [ ] Dos años de permanencia continuada acreditados por tramos.
- [ ] Recursos o procedimientos pendientes resueltos con el abogado (art. 126.h).
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; `verificar_escrito` pasado.
- [ ] Cada aviso de «posible disonancia de contenido» de `verificar_escrito` contrastado con el apartado exacto leído con `buscar_articulo` (el verificador compara con el título del artículo, p. ej. «Requisitos específicos» o «Procedimiento»): si el apartado dice lo que afirma el escrito, se mantiene la cita y se explica en el resumen; si no, se corrige.
- [ ] Marcadores para lo que falta; sin importes de tasa, códigos de modelo ni plazos de resolución no obtenidos del conector.
- [ ] Resumen para el abogado según el apartado 7 del formato, con la fecha límite del art. 127.a, la subsanación (art. 130.3) y la TIE (art. 130.6).
