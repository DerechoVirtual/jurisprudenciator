---
name: arraigo-social
description: >-
  Prepara la solicitud de autorización de residencia temporal por arraigo social (arts. 125.1.c y 127.c del
  Reglamento aprobado por el Real Decreto 1155/2024) con memoria justificativa en Word y relación de
  documentos para la Oficina de Extranjería. Úsala cuando el abogado diga «arraigo social», «lleva dos años en
  España sin papeles», «tiene familia con residencia» o «informe de integración». Comprueba permanencia,
  antecedentes, vínculos con familiares extranjeros residentes y medios del 100 % del IPREM, o el informe de
  integración. Si hay contrato de trabajo, usa arraigo-sociolaboral; si estudia o va a matricularse,
  arraigo-socioformativo; si tuvo una residencia que no pudo renovar, arraigo-segunda-oportunidad; si es
  progenitor de un menor de otro Estado de la UE, arraigo-familiar; si su familiar es español,
  familiares-de-espanoles.
---

# Arraigo social

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Base legal y requisitos vigentes** → `buscar_articulo` (`ley="LOEX"`, `articulo="31"`) y `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"124"`, `"125"`, `"126"` y `"127"`).
- **Procedimiento, documentación, órgano y representación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"130"`, `"193"` y `"197"`).
- **Efectos: trabajo, duración y prórroga** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"131"`, `"132"` y `"191"`).
- **Medios por cuenta propia, si se alegan** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, `articulo="84"`); **cancelación de antecedentes** → `buscar_articulo` (`ley="CP"`, `articulo="136"`).
- **Antiguo solicitante de protección internacional (fecha de firmeza de la denegación)** → `buscar_articulo` (`ley="Ley 12/2009"`, `articulo="29"`), (`ley="LPAC"`, artículos `"30"` y `"124"`) y (`ley="LJCA"`, artículos `"46"` y `"128"`).
- **Doctrina sobre permanencia, antecedentes, vínculos, medios e informe de integración** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"` para TSJ y juzgados, `base="TS"` para el Supremo) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **¿Se ha reformado el artículo?** → no uses `buscar_boe` para esto (con «Real Decreto 1155/2024» y fecha desde no devuelve ninguna reforma): lee la línea «redacción vigente dada por…» y las notas «Téngase en cuenta…» que devuelve `buscar_articulo` en cada artículo.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar o el requisito que hay que comprobar), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` (dónde está cada figura) y `references/formato-y-organos.md` (Word, destinatario, citas, datos, plazos y resumen). Léelas antes de redactar.

## Cuándo usarla

Si aún no está claro qué vía conviene al cliente, empieza por `extranjeria-intake` o `informe-viabilidad-extranjeria`; para revisar un expediente documental ya reunido, `documentacion-expediente`. Si la solicitud ya se presentó y hay requerimiento, denegación o archivo, esta skill no es la herramienta: `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria`.

- Persona extranjera en España, sin autorización de estancia o residencia, con al menos dos años de permanencia continuada, que quiere regularizarse **sin contrato de trabajo** apoyándose en:
  - **vía familiar**: cónyuge o pareja registrada, padres o hijos que son extranjeros **titulares de una autorización de residencia**, más medios económicos disponibles en España de al menos el 100 % del IPREM (pueden venir de esos familiares o de una actividad por cuenta propia que cumpla el art. 84); o
  - **vía de integración**: informe favorable de integración social de la comunidad autónoma o del ayuntamiento habilitado.
- También para revisar una solicitud ya preparada antes de presentarla.

Antes de seguir, pasa este **detector**. Si encaja otra figura, dilo al abogado con el artículo que lo sustenta (léelo con `buscar_articulo`) y no redactes el arraigo social. Si el abogado pide algo para el cliente, entrega una nota breve en Word (`nota-viabilidad-arraigo-social-<apellido-cliente>-<AAAAMMDD>.docx`) con el motivo, los artículos leídos y las alternativas:

| Situación del cliente | Figura que procede |
|---|---|
| Tiene uno o varios contratos que suman ≥ 20 h semanales con salario mínimo o de convenio | arraigo-sociolaboral (art. 127.b), que además habilita a trabajar desde la admisión (art. 130.5) |
| Estudia o va a matricularse en FP, bachillerato, certificado profesional o ESO de adultos presencial | arraigo-socioformativo (art. 127.d) |
| Fue titular de una residencia no excepcional en los dos últimos años y no la renovó | arraigo-segunda-oportunidad (art. 127.a) |
| Es padre, madre o tutor de un menor de otro Estado de la UE, el EEE o Suiza, o presta apoyo a un familiar con discapacidad de esa nacionalidad | arraigo-familiar (art. 127.e), sin permanencia mínima |
| El familiar es **español** (cónyuge, pareja, hijo, progenitor de menor español…) | `familiares-de-espanoles` (arts. 93-99), no arraigo |
| Familiar de ciudadano de otro Estado de la UE que ejerce la libre circulación | `ciudadanos-ue-y-familiares` (Real Decreto 240/2007, arts. 2 y 7) |
| Ha trabajado en situación irregular al menos seis meses en los dos últimos años y lo acredita ante la autoridad laboral o judicial | `razones-humanitarias` (colaboración del art. 129.2), que no exige los dos años de permanencia |
| Enfermedad grave sobrevenida, víctima de los delitos del art. 128.2 o riesgo al volver | `razones-humanitarias` (art. 128) |
| Víctima de violencia de género, sexual o de trata | `victimas-violencia-genero-sexual` (arts. 133-141) o `victimas-trata` (arts. 148-155) |
| Solicitante de protección internacional sin resolución firme | no puede pedir arraigo (art. 126.a); el estado de su solicitud, en `proteccion-internacional-apatridia` |
| Antiguo solicitante con denegación firme | sí puede pedirlo, pero los dos años cuentan desde la firmeza (ver requisito b): calcula la primera fecha segura antes de fijar la presentación |
| Titular de estancia por estudios | `estudiantes-y-busqueda-empleo`: modificación (art. 190), no arraigo (art. 126.h) |
| Orden de expulsión vigente o prohibición de entrada | primero `expulsion-procedimiento-sancionador`: la resolución de expulsión archiva cualquier procedimiento de residencia (art. 244.3) |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ Nacionalidad, pasaporte en vigor (fecha de caducidad) y provincia donde reside de forma efectiva (determina la oficina competente, art. 193.2).
2. ★ Fecha de entrada en España y pruebas de permanencia de **cada tramo** de los dos años anteriores a la fecha prevista de presentación: padrón histórico, asistencia sanitaria, envíos de dinero, cursos, abonos de transporte, informes de servicios sociales, pasaporte con sellos. Pregunta por cualquier salida de España y su duración.
3. ★ Situación administrativa: si ha pedido protección internacional (fecha de la manifestación de voluntad y de la formalización; fecha de la resolución y de su **notificación**; recursos interpuestos —reposición, contencioso, casación— y, si hubo recurso judicial, la sentencia y su **diligencia de firmeza**), si tiene o ha tenido alguna autorización, y si tiene **algún procedimiento de autorización de estancia o residencia en trámite** (incluidas las solicitudes de arraigo extraordinario o de la disposición adicional vigésima presentadas hasta el 30/06/2026).
4. ★ Antecedentes penales en España y en los países donde residió los cinco años anteriores a la entrada: condenas, pena impuesta, fecha de firmeza y de extinción de la pena y, si hubo suspensión, fecha del auto que la concedió y de la remisión definitiva; detenciones o antecedentes policiales y cómo terminaron.
5. ★ Expulsiones, devoluciones, prohibiciones de entrada o compromiso de no retorno por retorno voluntario.
6. ★ Vía que se va a usar:
   - familiar: parentesco exacto, título de residencia del familiar (tipo y vigencia), documentos del vínculo; cuantía mensual de los medios, de quién proceden y cómo se acreditan en España;
   - integración: fecha en que se pidió el informe, órgano, si se ha emitido y su sentido.
7. Si alega medios por cuenta propia: actividad, inversión y licencias (art. 84).
8. Representación: si presenta el abogado, apoderamiento notarial, apud acta en el registro electrónico de apoderamientos o inscripción como colaborador (art. 197.4).
9. Opcional: arraigo reforzante (cursos de idioma, voluntariado, hijos escolarizados, vivienda), útil para la vía de integración y para rebatir la amenaza al orden público.

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo. Si la respuesta incluye una nota «Téngase en cuenta» sobre nulidad declarada por el Tribunal Supremo, aplícala y cítala.

**Generales (art. 126, acumulativos):**

- **a) Estar en España y no ser solicitante de protección internacional** al presentar ni durante la tramitación. Si hay solicitud sin resolución firme (administrativa y, en su caso, judicial), no se puede pedir: explica al abogado que el cliente tendría que esperar a la firmeza o desistir. Busca la doctrina del Supremo que ha validado este requisito: `buscar_sentencias` (`consulta="arraigo artículo 126 solicitante de protección internacional"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="01/01/2026"`).
- **b) Dos años de permanencia continuada** antes de la solicitud. El tiempo como solicitante de protección internacional **no computa** hasta la resolución firme en sede administrativa y, en su caso, judicial. El padrón es prueba indiciaria, no exclusiva: la permanencia se acredita por cualquier medio. Si hubo salidas, busca doctrina sobre continuidad y ausencias (ver «Estrategia»).
  - **Cómo se calcula si fue solicitante de asilo** (déjalo por escrito en la memoria, con cada precepto leído): cuenta solo la permanencia posterior a la firmeza de la denegación. Si no recurrió, la resolución pone fin a la vía administrativa (art. 29.1 de la Ley 12/2009) y solo es inatacable cuando vence el plazo del recurso contencioso: dos meses desde el día siguiente a la notificación (art. 46.1 LJCA), sin contar agosto (art. 128.2 LJCA); el de reposición, un mes (arts. 124.1 y 30.4 LPAC), vence antes. Toma como firmeza el día siguiente al vencimiento del plazo del contencioso (lectura prudente) y da al abogado la **primera fecha segura de presentación**. Si hubo recurso judicial, la firmeza es la de la sentencia: pide la diligencia de firmeza. No sumes la permanencia anterior a la solicitud de asilo (es discutible) ni el trabajo realizado como solicitante (no suma permanencia). El Tribunal Supremo declaró conforme a Derecho en julio de 2026 esta exclusión, incluido el periodo que llega hasta la firmeza judicial: la búsqueda de la letra a) la localiza; léela y cítala cuando el cómputo sea relevante.
  - Las vías de las disposiciones adicionales vigésima y vigesimoprimera (solicitantes de protección internacional y arraigo extraordinario) solo admitían solicitudes hasta el 30/06/2026: dilo al abogado si el cliente pudo usarlas y no lo hizo.
- **c) No ser amenaza para el orden público, la seguridad o la salud pública.**
- **d) Carecer de antecedentes penales** en España y en los países de residencia de los cinco años anteriores a la entrada, por delitos del ordenamiento español (también art. 31.5 LOEX). Con cada condena, calcula con el art. 136 CP si está cancelada o si debería estarlo: el plazo del apartado 1 según la pena corre desde el día siguiente a su extinción, pero si la pena se extinguió por remisión tras una suspensión, el apartado 2 lo retrotrae (la duración de la pena se cuenta desde el día siguiente al otorgamiento de la suspensión y el plazo de cancelación, desde el día siguiente a aquel en que la pena habría quedado cumplida). Deja el cálculo, fecha a fecha, en la memoria. Si es cancelable, recomienda pedir la cancelación antes de presentar y aporta el justificante.
- **e) No figurar como rechazable** en el espacio Schengen. **f)** No estar en plazo de compromiso de no retorno. **g)** Tasa abonada: no des importe ni modelo; remite a la sede electrónica oficial. **h)** No ser titular de autorización de estancia o residencia ni interesado en otro procedimiento de concesión, prórroga, renovación o modificación en trámite: si lo hay, advierte al abogado de que la nueva solicitud chocará con este requisito y valora el desistimiento del anterior.

**Específico (art. 127.c):**

- **Vía familiar**: vínculo con **otra persona extranjera titular de una autorización de residencia**, limitado al cónyuge o pareja registrada y a familiares en primer grado en línea directa (padres e hijos). Hermanos, tíos, parejas no registradas o familiares con solo una estancia no valen: pasa a la vía de integración. Si el familiar es español, no es arraigo social: `familiares-de-espanoles`. Si es ciudadano de otro Estado de la UE, compara antes con `ciudadanos-ue-y-familiares`.
- **Medios económicos**: al menos el 100 % del IPREM, disponibles en España; pueden proceder de esos familiares, o de actividad por cuenta propia si se cumple el art. 84. Jurisprudenciator no devuelve la cuantía del IPREM: pide al abogado la cifra vigente de la fuente oficial y no la escribas de memoria.
- **Vía de integración**: si no hay vínculos familiares de ese tipo, se valora el esfuerzo de integración mediante **informe favorable** del órgano autonómico (o de la corporación local si la comunidad lo ha habilitado). Debe emitirse en **un mes** desde que se pide; si no se emite en plazo y el interesado lo acredita, el requisito se justifica **por cualquier medio de prueba**. Pide el justificante de la solicitud del informe.
- **Duda de lectura que debes resolver con el abogado**: el art. 127.c) liga expresamente los medios del 100 % del IPREM a la vía familiar, y en la vía de integración solo dice que el informe «hará constar… los medios económicos con los que cuente». Si el cliente tiene medios, acredítalos en cualquier vía. Si no los tiene y va por integración, sostén la lectura literal y busca doctrina aplicada al Reglamento vigente antes de afirmarlo.

**Normas que el conector no devuelve por `buscar_articulo`:**

- Disposiciones adicionales vigésima y vigesimoprimera del Reglamento (arraigo de solicitantes de protección internacional y arraigo extraordinario, que solo podían pedirse hasta el 30/06/2026): léelas con `leer_boe` (`identificador="BOE-A-2026-8284"`, Real Decreto 316/2026). Si el cliente tiene una de esas solicitudes sin resolver, choca con el art. 126.h.
- Solicitudes de arraigo presentadas desde el 20/05/2025 hasta la entrada en vigor del Real Decreto 316/2026 (sus redacciones rigen desde el 16/04/2026) y aún en trámite: su régimen está en la disposición transitoria segunda de ese real decreto, que `leer_boe` no llega a devolver. Si el caso depende de ella, aplica la puerta y di al abogado qué precepto falta.

**Procedimiento (art. 130) y efectos:**

- Solicitud personal ante la oficina competente, sin visado, con copia completa del pasaporte en vigor y la documentación del supuesto (art. 130.1). La presentación por representante acreditado cuenta como comparecencia personal (art. 197.4).
- Certificado de antecedentes de los países de residencia de los cinco años previos a la entrada, salvo que lleve cinco años continuados en España o lo haya acreditado en otra solicitud de los últimos cinco años sin salir (art. 130.2). La oficina pide de oficio penados y el informe policial; los antecedentes policiales no deniegan de forma automática: exigen valoración individual (art. 130.2).
- Subsanación: plazo que fije la oficina, no superior a quince días, con apercibimiento de desistimiento (art. 130.3).
- Concedida: un año de duración (art. 125.2); habilita a trabajar por cuenta ajena o propia sin límite geográfico ni de ocupación (art. 131); TIE en el plazo de un mes desde la notificación (art. 130.6).
- Prórroga: condicionada a búsqueda activa de empleo e inscripción en el servicio público de empleo, salvo impedimentos justificados (art. 132.2.a); se pide en los dos meses anteriores al vencimiento o en los tres posteriores (art. 132.3). Tras un año, cabe modificar a residencia y trabajo (art. 191.3).
- Plazo máximo de resolución y sentido del silencio: están en disposiciones adicionales que el conector no devuelve (LOEX y Reglamento). No los afirmes; dile al abogado que los compruebe en el BOE consolidado.

**Causas típicas de denegación y cómo rebatirlas:**

| Causa | Respuesta |
|---|---|
| No acredita dos años continuados (solo padrón reciente) | Aportar prueba de cada tramo por cualquier medio; doctrina sobre el valor indiciario del padrón |
| Antecedentes penales | Si están cancelados o debieron estarlo por el art. 136 CP, no pueden fundar la denegación (doctrina del Supremo) |
| Antecedentes policiales | Art. 130.2: no deniegan por sí solos; exigir valoración casuística y motivada |
| Vínculo con familiar sin residencia o fuera del primer grado | Reconducir a la vía de integración o a otra figura |
| Medios insuficientes o no disponibles en España | Sumar ingresos de los familiares del art. 127.c; acreditar cuenta en España |
| Informe de integración no emitido | Acreditar la fecha de solicitud y el transcurso del mes; probar la integración por otros medios (art. 127.c) |
| Procedimiento previo en trámite o solicitud de protección internacional | Arts. 126.a y 126.h: esperar firmeza o desistir antes de presentar |

## Estrategia y jurisprudencia

1. Elige la vía más objetiva: la familiar con medios acreditados se resuelve con documentos; la de integración depende del informe. Si concurren las dos, alega ambas en fundamentos separados.
2. Pide el informe de integración cuanto antes: el mes de plazo corre desde su solicitud.
3. Consultas en Jurisprudenciator (reformula como máximo dos veces si no hay resultados útiles):
   - Antecedentes: `buscar_sentencias` (`consulta="arraigo antecedentes penales cancelados o cancelables artículo 136 Código Penal"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`) y la misma con `base="AN"`.
   - Antecedentes policiales: `consulta="arraigo antecedentes policiales denegación automática valoración"`, `base="AN"`.
   - Permanencia: `consulta="arraigo permanencia continuada empadronamiento prueba indiciaria"` y `consulta="arraigo permanencia continuada ausencias"`, `base="AN"`.
   - Vínculos y medios: `consulta="arraigo social vínculos familiares extranjeros residentes medios económicos IPREM"`, `base="AN"`, `fecha_desde="20/05/2025"`.
   - Informe: `consulta="arraigo social informe de integración no emitido en plazo cualquier medio de prueba"`, `base="AN"`.
4. Lee con `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión) solo las resoluciones que vayas a citar y transcribe el párrafo de **fundamentos**, nunca los hechos ni datos de aquel pleito. Comprueba que ese párrafo es razonamiento de la Sala y no alegaciones de parte ni la transcripción de un precepto (en estas pruebas salieron ambas cosas con `parrafos=3`); si no lo es, afina `terminos` o elige otra resolución.
5. Buena parte de la doctrina se dictó bajo el art. 124 del Real Decreto 557/2011 (tres años y contrato). Cítala solo para lo que el Reglamento vigente mantiene con el mismo texto (antecedentes, prueba de la permanencia y, de la letra c) del art. 127, el círculo de familiares —cónyuge o pareja registrada y primer grado en línea directa— o la prueba por cualquier medio si el informe no se emite en plazo) y dilo en el escrito: «doctrina dictada bajo el artículo 124 del Real Decreto 557/2011, trasladable porque el artículo 126 del Real Decreto 1155/2024 mantiene el mismo requisito». No la uses para lo que ha cambiado (tres años, contrato de trabajo, medios del 100 % del IPREM).
6. Prefiere lo reciente: usa `fecha_desde="20/05/2025"` para la regulación vigente y amplía solo si no hay nada.

**Al citar una sentencia**, comprueba qué reglamento aplicó (Real Decreto 557/2011 o Real Decreto 1155/2024: fecha de la solicitud de aquel caso y artículos que cita) y dilo en el escrito. Si aplicó el anterior, cítala solo para requisitos que los arts. 126 y 127 vigentes mantienen iguales. Si la resolución anula o interpreta un precepto del Reglamento vigente, contrasta que la nota «Téngase en cuenta» de `buscar_articulo` lo refleja.

## Documento que se entrega

Un Word maquetado según `references/formato-y-organos.md`: **solicitud de autorización de residencia temporal por circunstancias excepcionales por arraigo social con memoria justificativa**. Acompaña al impreso oficial de solicitud vigente, que no sustituye: indica al abogado que lo descargue de la sede oficial.

Nombre: `solicitud-arraigo-social-<apellido-cliente>-<AAAAMMDD>.docx`.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» (la primera vez, «, de 19 de noviembre, por el que se aprueba el Reglamento de la Ley Orgánica 4/2000») y la ley como «artículo 31.3 de la Ley Orgánica 4/2000», según el apartado 4 del formato: así `verificar_escrito` reconoce cada cita. Nunca «del Reglamento de Extranjería». Dos precauciones más, comprobadas con el verificador: las letras se citan «letra c) del artículo 127 del Real Decreto 1155/2024» (con «artículo 127.c) del Real Decreto 1155/2024» no enlaza la norma y atribuye el artículo a la última norma citada), y cuando en el mismo párrafo aparecen artículos de varias normas (Reglamento, Código Penal, LJCA, LPAC), nombra la norma detrás de cada artículo.

Estructura:

1. **Encabezamiento**: «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA] — [DELEGACIÓN / SUBDELEGACIÓN] DEL GOBIERNO» (competencia del art. 193.2, leído).
2. **Comparecencia**: `[NOMBRE Y APELLIDOS]`, nacionalidad, `[PASAPORTE]`, `[NIE]` si lo tiene, `[DOMICILIO]`; si actúa el abogado, representación y título (art. 197.4).
3. **EXPONE — HECHOS** (ordinales):
   - PRIMERO.- Identidad y entrada en España (`[FECHA DE ENTRADA EN ESPAÑA]`).
   - SEGUNDO.- Permanencia continuada, tramo a tramo, con el documento que prueba cada periodo.
   - TERCERO.- Situación administrativa: sin autorización ni procedimiento en trámite; protección internacional, si la hubo, con su firmeza.
   - CUARTO.- Ausencia de antecedentes penales (o su cancelación) y de prohibiciones de entrada.
   - QUINTO.- Vínculos familiares y medios, o integración y estado del informe.
   - SEXTO.- Otros elementos de arraigo, si los hay.
4. **FUNDAMENTOS DE DERECHO**: I. Marco legal (art. 31.3 LOEX; arts. 124 y 125.1.c). II. Competencia y procedimiento (arts. 130, 193.2 y 197). III. Requisitos generales del art. 126, uno por uno con su prueba. IV. Requisito específico del art. 127.c. V. Doctrina aplicable, con párrafo literal y ECLI. VI. Efectos de la concesión (arts. 125.2 y 131). Cada fundamento con su propia secuencia argumental (formato, apartado 2).
5. **SOLICITA**: que se admita a trámite y se conceda la autorización por arraigo social por un año con habilitación para trabajar.
6. **OTROSÍ**: que se tenga por solicitado el informe de integración en la fecha indicada y, si no se emite en plazo, por acreditada la integración con los documentos aportados (art. 127.c); que se recaben de oficio los informes del art. 130.2.
7. Lugar, fecha y firma.
8. **RELACIÓN DE DOCUMENTOS**, numerada y en el orden de los hechos: impreso oficial; justificante de la tasa; pasaporte completo; prueba de permanencia por tramos; certificados de antecedentes (con la legalización o apostilla y traducción que pida la oficina según su hoja informativa); documentos del vínculo y título de residencia del familiar; prueba de medios; informe de integración o justificante de haberlo pedido; representación.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: LOEX 31 y Reglamento 124, 125, 126, 127, 130, 131, 132, 193 y 197 (y 84, CP 136, o Ley 12/2009 art. 29, LPAC 30 y 124 y LJCA 46 y 128 si se usan); anotada la fecha de vigencia y revisadas las notas de nulidad.
- [ ] Detector pasado: ninguna otra figura encaja mejor; si encaja, se ha dicho al abogado.
- [ ] Fecha en que se cumplen los dos años calculada; si fue solicitante de protección internacional, desde la firmeza de la denegación (notificación, plazos de los arts. 124 LPAC y 46 y 128.2 LJCA, o diligencia de firmeza) y con la primera fecha segura de presentación en el resumen.
- [ ] Cada condena, con su cálculo de cancelación del art. 136 CP (apartado 2 si hubo suspensión y remisión).
- [ ] Cada requisito tiene su documento en la relación; lo que falta está marcado y listado en el resumen.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el texto completo y corregido lo que señale.
- [ ] Cada aviso de «posible disonancia de contenido» de `verificar_escrito` contrastado con el apartado exacto leído con `buscar_articulo` (el verificador compara con el título del artículo, p. ej. «Requisitos específicos» o «Procedimiento»): si el apartado dice lo que afirma el escrito, se mantiene la cita y se explica en el resumen; si no, se corrige.
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[DOMICILIO]`, `[FECHA DE ENTRADA EN ESPAÑA]`, cuantía del IPREM confirmada por el abogado) en lugar de datos inventados.
- [ ] Sin importes de tasa, códigos de modelo ni plazos de resolución no obtenidos del conector.
- [ ] Resumen para el abogado según el apartado 7 del formato: qué se ha preparado y para qué oficina; fechas clave con su precepto (dos años, art. 126.b; informe en un mes, art. 127.c; subsanación, art. 130.3; TIE, art. 130.6); documentos que faltan y riesgos; tabla de jurisprudencia; próximo paso.
