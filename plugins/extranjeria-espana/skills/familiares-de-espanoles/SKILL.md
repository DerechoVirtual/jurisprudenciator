---
name: familiares-de-espanoles
description: >-
  Prepara en Word la solicitud de autorización de residencia temporal de familiar de persona con nacionalidad española (arts. 93-99 del Reglamento aprobado por el Real Decreto 1155/2024) y de su visado (art. 41), o la de residencia independiente tras divorcio, fallecimiento o violencia. Úsala cuando el abogado diga «casada con un español», «pareja de hecho de una española», «hijo de español», «madre de un menor español», «ascendiente a cargo de un español» o «se ha divorciado de su marido español». Antes decide si el caso va por el Real Decreto 240/2007 (familiar de ciudadano de otro Estado de la Unión, español que regresa tras residir con su familiar en otro Estado miembro o solicitud anterior al 20/05/2025): entonces usa ciudadanos-ue-y-familiares.
---

# Familiares de personas con nacionalidad española

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Figura, familiares incluidos y requisitos** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"93"`, `"94"`, `"95"`, `"96"` y `"196"`).
- **Procedimiento, visado, plazos, silencio y TIE** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"97"`, `"41"`, `"38"`, `"28"`, `"193"`, `"197"` y `"209"`).
- **Orden público, mantenimiento, residencia independiente y cambio de autorización** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"98"`, `"99"`, `"191"` y `"200"`).
- **Nulidades declaradas por el Tribunal Supremo en los arts. 94.1.f), 97.4, 98.1 y 196.2.b) y reforma de los arts. 97.1.c) y 97.5** → las notas «Téngase en cuenta» que devuelve `buscar_articulo`, el fallo con `leer_boe` (`identificador="BOE-A-2026-19632"`) y la reforma con `leer_boe` (`identificador="BOE-A-2026-8284"`: Real Decreto 316/2026, vigente desde el 16/04/2026).
- **Régimen transitorio (solicitudes anteriores al 20/05/2025, tarjetas y arraigos familiares vigentes)** → `leer_boe` (`identificador="BOE-A-2024-24099"`, disposiciones transitorias del real decreto aprobatorio).
- **Frontera con el régimen de la Unión** → `buscar_articulo` (`ley="Real Decreto 240/2007"`, artículos `"2"` y `"7"`), `buscar_articulo` (`ley="Directiva 2004/38/CE"`, `articulo="3"`) y el fallo que anuló expresiones del Real Decreto 240/2007 con `leer_boe` (`identificador="BOE-A-2010-16822"`): el art. 2 que devuelve el conector conserva sin marcar las expresiones anuladas «otro Estado miembro» y «separación legal»; no las cites como vigentes.
- **Doctrina sobre el nuevo régimen, el «a cargo», la pareja estable y el art. 20 TFUE** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"` o `base="AN"`; `base="TJUE"` para la doctrina europea) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

## Cuándo usarla

- Familiar extranjero (no nacional de la UE, del EEE ni de Suiza) de una persona española que **no ha ejercido la libre circulación**, cuando quieren residir juntos en España: desde el consulado o desde España.
- Residencia independiente del familiar tras fallecimiento del español, fin de su residencia en España, nulidad, divorcio, cancelación de la pareja o violencia (art. 99).
- Revisión de una solicitud preparada o respuesta a un requerimiento de subsanación.

**Detector previo.** Resuelve primero qué régimen se aplica. Lee cada precepto que cites en la tabla y dile al abogado cuál procede antes de redactar:

| Situación | Régimen y skill |
|---|---|
| Español que nunca ha residido con su familiar en otro Estado miembro («español estático»); solicitud presentada desde el 20/05/2025 | Esta skill (arts. 93-99) |
| Español que residió de forma efectiva con su familiar en otro Estado miembro y regresa a España | Doctrina del TJUE sobre el ciudadano que regresa: régimen de la Directiva, aplicado a través del Real Decreto 240/2007 → ciudadanos-ue-y-familiares |
| Solicitud presentada antes del 20/05/2025 | Normativa vigente al presentarla, salvo que el interesado pida el nuevo Reglamento (disposición transitoria segunda del real decreto aprobatorio) → ciudadanos-ue-y-familiares |
| Titular, al 20/05/2025, de tarjeta de familiar de ciudadano de la Unión o de arraigo familiar por vínculo con un español | Disposición transitoria tercera: `leer_boe` la devuelve **cortada**. Si el asunto depende de la parte que no llega (renovación o conversión de esa tarjeta), aplica la puerta: detente y dile al abogado que falta el texto completo de esa transitoria |
| Familiar de ciudadano de otro Estado de la Unión | ciudadanos-ue-y-familiares |
| Progenitor de un menor de otro Estado de la Unión, el EEE o Suiza | arraigo-familiar (art. 127.e) |
| Familiar de extranjero residente | reagrupacion-familiar (arts. 65-71) |
| Cónyuge menor de dieciocho años | No cabe por el art. 94.1.a), que el Supremo declaró conforme a Derecho en la sentencia de 8 de julio de 2026 (fundamento jurídico séptimo: léelo con `leer_sentencias` antes de atribuirle nada). Valora reagrupación o circunstancias excepcionales y, si la denegación obligaría al español a abandonar la Unión, el art. 20 TFUE |
| Ya hay resolución denegatoria | recurso-administrativo-extranjeria o recurso-contencioso-extranjeria; si deniega el consulado, visados-denegacion. Esta skill solo sirve para una nueva solicitud |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. Los marcados con ★ son imprescindibles: sin ellos no se redacta.

1. ★ Persona española: cómo acredita la nacionalidad, si es **española de origen** (decide la letra h), dónde reside y si ha vivido con el familiar en otro Estado miembro (fechas y prueba de residencia efectiva allí).
2. ★ Familiar extranjero: nacionalidad, pasaporte (vigencia), dónde está hoy, fecha de entrada en España si está aquí y si su estancia es regular o no.
3. ★ Vínculo y letra del art. 94.1 en que encaja, con el documento que lo prueba: matrimonio (y matrimonios anteriores de cualquiera de los dos), inscripción de la pareja y su registro, prueba de doce meses de convivencia o descendencia común, filiación, adopción, tutela, custodia o consentimiento del otro progenitor, grado de dependencia reconocido.
4. ★ Convivencia actual o prevista (el art. 94.1 la exige) y domicilio en España.
5. ★ Si hay que acreditar que está **a cargo** (letras d mayores de 26 años, e y i): envíos o gastos del año anterior, situación económica en el país de procedencia, ingresos y patrimonio de la unidad del español, si alguien percibe el ingreso mínimo vital, edad y salud del ascendiente.
6. ★ Antecedentes penales del familiar en España y en los países de residencia de los cinco años anteriores; antecedentes policiales; prohibiciones de entrada.
7. ★ Procedimientos anteriores: solicitudes inadmitidas o denegadas (el art. 97.5 niega la autorización provisional si hay identidad sustancial de hechos) y procedimientos en trámite.
8. Para residencia independiente: hecho causante y fecha (fallecimiento, admisión de la demanda, cancelación, cese de convivencia, orden de protección o informe), duración del vínculo y del tiempo en España, custodia o régimen de visitas, fecha de la comunicación a extranjería.
9. Representación: apoderamiento notarial, apud acta en el registro electrónico de apoderamientos o colaborador inscrito (art. 197.4).

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo. Varios llevan una nota «Téngase en cuenta» de nulidad parcial: léela, lee el fallo con `leer_boe` (`identificador="BOE-A-2026-19632"`) y **no cites nunca un inciso anulado** como vigente.

**Ámbito (arts. 93 y 94).**

- El familiar no puede tener nacionalidad de la UE, del EEE ni de Suiza. El vínculo vale con independencia de dónde y cuándo se creó, siempre que se mantenga y el familiar acompañe o se reúna con el español en España; los hijos de español de origen (letra h) pueden hacerlo en cualquier circunstancia.
- Comprueba la letra aplicable y su requisito propio:
  - a) cónyuge mayor de dieciocho años, sin nulidad, divorcio ni fraude; un solo cónyuge; si hubo matrimonios anteriores, que su disolución fijara la situación del cónyuge previo y sus familiares;
  - b) pareja inscrita en un registro público de un Estado de la UE, del EEE o Suiza, mayor de dieciocho años;
  - c) pareja estable: doce meses continuados de convivencia análoga a la conyugal, dentro o fuera de España, salvo descendencia común; matrimonio, pareja registrada y pareja estable son incompatibles entre sí;
  - d) hijos del español o de su cónyuge o pareja, menores de veintiséis años, o mayores a cargo o con discapacidad que precise apoyo, no casados ni con unidad familiar propia; hijos menores del cónyuge o pareja: patria potestad o custodia exclusiva del progenitor, o consentimiento del otro ante autoridad o fedatario;
  - e) ascendientes en primer grado, a cargo y sin apoyo familiar en origen, o por razones humanitarias (art. 196.6);
  - f) padre, madre, tutor o tutora de un menor español que lo tenga a cargo y conviva o esté al corriente de sus obligaciones. El inciso que exigía que la relación se constituyera conforme al ordenamiento español **está anulado**: una tutela constituida en el extranjero no se rechaza por ese solo motivo;
  - g) un único familiar hasta segundo grado que cuide a un español con grado de dependencia reconocido;
  - h) hijos de padre o madre que sean o hayan sido españoles de origen;
  - i) otros familiares a cargo, acreditado de forma fehaciente al solicitar.
- Menores sin filiación: medidas de protección por desamparo (art. 94.4).

**Persona a cargo y razones humanitarias (art. 196).** Dependencia económica real, estable y previa a la solicitud, valorada caso por caso. El inciso que exigía que se produjera **en el país de origen o procedencia está anulado** en cuanto impedía acreditarla con el ascendiente ya en España. Comprueba en el texto leído la presunción por fondos recibidos el año anterior (art. 196.3.c), la solvencia exigida a la unidad del español (art. 196.3.d), la dependencia física (art. 196.4) y las presunciones del art. 196.5. Jurisprudenciator no devuelve el PIB per cápita del Banco Mundial ni la cuantía anual de las pensiones no contributivas: pide al abogado la cifra de la fuente oficial y no la escribas de memoria.

**Documentación (art. 96).** Pasaporte o DNI del español y, para cónyuge o pareja, declaración responsable de que no reside con él otro cónyuge o pareja; pasaporte del familiar, prueba del vínculo, de estar a cargo cuando se exija y, en la pareja estable, de la relación y del tiempo de convivencia. En la vía c) se añade lo que exige el art. 38 salvo sus letras b) y h) (art. 97.4): compruébalo en el texto leído del art. 38 (impreso oficial, no figurar como rechazable, pasaporte con vigencia mínima de un año, antecedentes penales de los países de residencia de los cinco últimos años y certificado médico) e inclúyelo en la relación de documentos.

**Procedimiento (arts. 97 y 41).** Elige la vía según dónde estén los dos:

| Vía | Quién y dónde presenta | Plazos que debes leer |
|---|---|---|
| 97.1.a) español en España, familiar fuera | El español, ante la oficina de extranjería de su provincia; concedida, el familiar pide visado en el consulado | Oficina: dos meses, silencio desestimatorio (art. 97.6); visado en un mes desde la notificación de la concesión y resolución consular en quince días (art. 41.2) |
| 97.1.b) ambos fuera | El familiar, visado en el consulado, que lleva implícita la autorización | Oficina: dos meses desde la comunicación consular, silencio desestimatorio; consulado: quince días (art. 41.3) |
| 97.1.c) ambos en España | Cualquiera de los dos, ante la oficina de la provincia de residencia; solo letras a) a h) | Resolución en dos meses, silencio desestimatorio (art. 97.6) |

- En la vía c) se exigen los requisitos del art. 38 **salvo** sus letras b) y h): la estancia irregular no impide solicitar. La redacción actual del art. 97.1.c), que incluye las letras d) y e), y la del art. 97.5 proceden del Real Decreto 316/2026, vigente desde el 16/04/2026: antes de esa fecha los hijos mayores de dieciocho años y los ascendientes no podían pedirla desde España. El Supremo declaró terminado el proceso sobre esos incisos (fallo, ordinal cuarto); no le atribuyas otra interpretación del art. 97.1.c) que no hayas leído con `leer_sentencias`.
- Autorización provisional de residencia y trabajo desde la admisión a trámite en la vía c), con efectos retroactivos si se concede, salvo solicitudes previas del mismo tipo inadmitidas o denegadas por hechos sustancialmente idénticos (art. 97.5).
- Subsanación en el plazo que fije la oficina, nunca superior a quince días, con apercibimiento de desistimiento (art. 97.6). Informes de oficio de policía, juzgados y penados.
- Tramitación preferente y gratuita (art. 97.8). TIE en un mes desde la notificación (vía c) o desde la entrada (resto) (art. 97.7).

**Efectos (art. 95).** Cinco años (o el tiempo previsto de residencia del español si es menor), desde la concesión o desde la entrada; habilita a trabajar por cuenta ajena y propia en todo el territorio, sin situación nacional de empleo; el familiar puede reagrupar (arts. 68 y 69). Renovación, si la duración fue inferior a cinco años, en los dos meses anteriores o los tres posteriores a la caducidad (art. 95.4).

**Orden público y antecedentes (art. 98.1).** La denegación por orden o seguridad pública exige conducta personal que sea amenaza real, actual y suficientemente grave, con proporcionalidad; las condenas no deniegan por sí solas, salvo para las letras c), g), h) e i), que deben acreditar carecer de antecedentes. Ese automatismo (y el del art. 97.4) **está anulado en los supuestos del art. 20 TFUE**: cuando la denegación obligaría al español (por ejemplo, un menor dependiente) a abandonar el territorio de la Unión, exige ponderación individual. Argumenta esa dependencia con hechos concretos.

**Mantenimiento (arts. 98.2-98.3 y 200).** Comunicar cambios de domicilio, nacionalidad, estado civil o pareja en dos meses. Dejar de hacer vida familiar efectiva es causa de retirada.

**Residencia independiente (art. 99).** No cabe para las letras c) e i). Supuestos: fallecimiento (si ya residía en España), cese de la residencia del español (hijos escolarizados y progenitor custodio), nulidad, divorcio o cancelación (tres años de vínculo hasta el inicio del procedimiento judicial, al menos uno de ellos en España; custodia; o régimen de visitas vigente de un hijo menor que reside en España) y violencia o trata. Comunicar el hecho en seis meses y **pedir la residencia independiente en los seis meses siguientes** al hecho causante (art. 99.6); en nulidad o divorcio el plazo corre desde la **notificación de la admisión de la demanda**, y en la pareja registrada desde la resolución de cancelación (art. 99.4.a). Si falta la fecha de esa notificación, pídela: sin ella no hay plazo. Si no es posible, modificación del título XI en los tres meses siguientes (arts. 99.7 y 191.8).

**Causas típicas de denegación y respuesta.**

| Causa | Respuesta |
|---|---|
| Pareja estable sin doce meses acreditados | Prueba de convivencia por tramos, dentro o fuera de España, o descendencia común |
| No acredita estar a cargo | Envíos y gastos del año anterior, situación en origen y solvencia de la unidad del español (art. 196.3); si el ascendiente ya está en España, invoca la nulidad del inciso de origen |
| Matrimonio en fraude de ley | Prueba de relación real; doctrina sobre la carga de la prueba del fraude |
| Antecedentes penales | Letras a), b), d), e), f): no automáticos, exige amenaza actual; art. 20 TFUE: ponderación obligatoria |
| Tutela constituida en el extranjero | Inciso anulado del art. 94.1.f) |

## Estrategia y jurisprudencia

1. Decide el régimen con el detector antes que nada; si hay duda entre este y el Real Decreto 240/2007, explica las dos vías al abogado y deja que elija.
2. Elige la vía del art. 97 que dé autorización provisional si el familiar está en España (vía c) y no hay denegaciones previas por los mismos hechos.
3. Consultas (reformula como máximo dos veces):
   - Nuevo régimen y su control por el Supremo: `buscar_sentencias` (`consulta="Real Decreto 1155/2024 familiares de personas con nacionalidad española"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="01/07/2026"`); lee con `leer_sentencias` (`parrafos=4`, `terminos="familiares nacionalidad española artículo 20 TFUE antecedentes régimen constitutivo"`).
   - Aplicación por los tribunales: `consulta="autorización de residencia familiar de persona con nacionalidad española artículo 94"`, `base="AN"`, `fecha_desde="20/05/2025"`.
   - A cargo: `consulta="familiar a cargo ciudadano español dependencia económica envíos de dinero"`, `base="AN"`.
   - Pareja estable: `consulta="pareja estable ciudadano español convivencia doce meses prueba"`, `base="AN"`.
   - Art. 20 TFUE: `consulta="artículo 20 TFUE derecho de residencia derivado relación de dependencia"`, `base="TJUE"`, y `consulta="artículo 20 TFUE ciudadano español menor dependencia progenitor denegación residencia"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`.
   - Ciudadano que regresa: `consulta="ciudadano de la Unión que regresa a su Estado miembro de origen familiar nacional de tercer país"`, `base="TJUE"`.
   - Residencia independiente tras nulidad o divorcio: `consulta="residencia independiente divorcio familiar de español duración tres años matrimonio inicio del procedimiento judicial"`, `base="AN"`, y, para la fórmula idéntica del art. 13.2.a) de la Directiva (que el art. 99.4.a reproduce), `consulta="mantenimiento del derecho de residencia en caso de divorcio duración del matrimonio tres años inicio del procedimiento judicial de divorcio nacional de un tercer país"`, `base="TJUE"`. La Directiva no rige al familiar de un español estático: cita al Tribunal de Justicia solo como criterio interpretativo de esa fórmula y dilo en el escrito. Si no hay doctrina española sobre el art. 99, dilo en el resumen.
4. La doctrina dictada con el Real Decreto 240/2007 aplicado por analogía a familiares de españoles solo se traslada a conceptos con igual contenido (persona a cargo, orden público, pareja estable); no a los requisitos que el nuevo régimen cambia (visado, sistema constitutivo, medios). Dilo expresamente en el escrito cuando la cites.
5. Transcribe el párrafo de fundamentos, nunca los hechos ni datos del pleito ajeno.

## Documento que se entrega

Word maquetado según `references/formato-y-organos.md`. Acompaña al impreso oficial vigente, que no sustituye: indica al abogado que lo descargue de la sede oficial. No des importes ni códigos de modelos.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» y el resto de normas como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca. La primera cita del Reglamento hazla sin letras («al amparo del artículo 97 del Real Decreto 1155/2024, por la vía de su apartado 1.c)»): `verificar_escrito` no enlaza con su norma una cita con letra («artículo 97.1.c)») si esa norma no ha aparecido antes en el texto, y en ese caso la atribuye a la última norma nombrada. Tampoco reconoce la Directiva 2004/38/CE (atribuye sus artículos al Real Decreto 1155/2024): comprueba los de la Directiva con `buscar_articulo`.

**A) Solicitud de autorización de residencia temporal de familiar de persona con nacionalidad española** — `solicitud-residencia-familiar-espanol-<apellido-cliente>-<AAAAMMDD>.docx`.

1. Encabezamiento: vías a) y c), «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA] — [DELEGACIÓN / SUBDELEGACIÓN] DEL GOBIERNO» (art. 193.2 leído); vía b), «A LA OFICINA CONSULAR DE ESPAÑA EN [CIUDAD]».
2. Comparecencia: solicitante según la vía (art. 97.1), con `[NOMBRE Y APELLIDOS]`, `[PASAPORTE]` o DNI, `[NIE]` si lo tiene, `[DOMICILIO]`; representación y su título.
3. EXPONE — HECHOS: PRIMERO, persona española y su nacionalidad; SEGUNDO, familiar y situación en que se encuentra; TERCERO, vínculo y letra del art. 94.1; CUARTO, convivencia; QUINTO, dependencia o razones humanitarias, si se exigen; SEXTO, antecedentes y procedimientos previos.
4. FUNDAMENTOS DE DERECHO: I, régimen aplicable y por qué no el Real Decreto 240/2007; II, competencia y vía de presentación (arts. 97, 193 y 197); III, encaje en el art. 94.1 con su prueba (art. 96); IV, persona a cargo (art. 196), si procede; V, orden público y, en su caso, art. 20 TFUE (art. 98.1 y fallo anulatorio); VI, doctrina aplicable con párrafo literal y ECLI; VII, efectos pedidos (art. 95 y, en la vía c, art. 97.5).
5. SOLICITA: la concesión por cinco años o por el periodo que corresponda y, en la vía c), que la comunicación de inicio haga constar la autorización provisional para trabajar.
6. OTROSÍ: que se recaben de oficio los informes del art. 97.6; en su caso, que se tenga por aportada la prueba de la dependencia del ascendiente ya residente en España.
7. Lugar, fecha, firma y RELACIÓN DE DOCUMENTOS numerada en el orden de los hechos.

**B) Solicitud de residencia independiente (art. 99)** — `solicitud-residencia-independiente-<apellido-cliente>-<AAAAMMDD>.docx`. Misma estructura; los hechos se centran en el hecho causante, su fecha y la comunicación a extranjería; el fundamento principal es el apartado del art. 99 aplicable y, en subsidio, la modificación del art. 191.8. Aprovecha el escrito para comunicar los cambios pendientes (domicilio y estado civil, art. 98.2; nulidad o divorcio, art. 99.4) y, si alguno está fuera de plazo, dilo al abogado. El art. 99 no fija plazo de resolución ni sentido del silencio: no afirmes ninguno que no hayas obtenido con Jurisprudenciator. Para el plan B del art. 191.8, lee con `buscar_articulo` los requisitos de la autorización a la que se pasaría antes de afirmar que se cumplen.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Detector resuelto y explicado al abogado; si dependía de una transitoria que no llega completa, la tarea se detuvo.
- [ ] Leídos con `buscar_articulo` en esta conversación los arts. 41, 93-99, 196 y los demás citados; revisadas las notas de nulidad y leído el fallo con `leer_boe`.
- [ ] Ningún inciso anulado citado como vigente (arts. 94.1.f, 97.4, 98.1 y 196.2.b del Reglamento; «otro Estado miembro» y «separación legal» del art. 2 del Real Decreto 240/2007).
- [ ] Vía del art. 97 y destinatario correctos; plazos de visado, subsanación, resolución y TIE con su precepto.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; solo fundamentos, sin datos del pleito ajeno.
- [ ] `verificar_escrito` pasado sobre el texto completo y corregido lo que señale.
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[DOMICILIO]`, `[FECHA DE ENTRADA EN ESPAÑA]`) en lugar de datos inventados; sin importes ni cifras del IPREM, PIB o pensiones no confirmadas por el abogado.
- [ ] Resumen para el abogado según el apartado 7 del formato: qué se ha preparado y ante quién; plazos (visado, residencia independiente, TIE) con su fecha y precepto; documentos que faltan y riesgos; tabla de jurisprudencia; próximo paso.
