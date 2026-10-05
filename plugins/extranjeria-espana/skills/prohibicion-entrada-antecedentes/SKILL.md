---
name: prohibicion-entrada-antecedentes
description: >-
  Levantamiento, revocación, no imposición o reducción de la prohibición de entrada que acompaña a
  una expulsión o devolución (LOEX arts. 26, 57.4 y 58; arts. 11, 23, 240 y 244 del Reglamento
  aprobado por el Real Decreto 1155/2024), su reflejo en el Sistema de Información Schengen (SIS) y
  cancelación de antecedentes penales y policiales que bloquean un visado, una autorización o su
  renovación. Prepara en Word la solicitud de revocación y, si procede, las de cancelación de
  antecedentes penales (art. 136 del Código Penal), supresión de datos policiales (LO 7/2021) o
  acceso al SIS. Úsala con «tiene prohibida la entrada», «quiere volver tras la expulsión»,
  «rechazable Schengen», «alerta SIS», «le deniegan por antecedentes», «cancelar antecedentes». Si
  el expediente de expulsión sigue abierto, usa expulsion-procedimiento-sancionador.
---

# Prohibición de entrada, Schengen y antecedentes

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Prohibición de entrada: supuestos, duración, no imposición y revocación** → `buscar_articulo` (`ley="LOEX"`, artículos 26, 56, 57 y 58; `ley="BOE-A-2024-24099"`, artículos 11, 23, 24, 224, 240, 244 y 246).
- **Efectos sobre autorizaciones, renovaciones y arraigo** → `buscar_articulo` (`ley="LOEX"`, artículo 31; `ley="BOE-A-2024-24099"`, artículos 126, 130, 200, 201 y 202).
- **Derecho de la Unión y SIS** → `buscar_articulo` (`ley="Directiva 2008/115/CE"`, artículos 3 y 11; `ley="Reglamento (UE) 2018/1861"`, artículos 24, 28 a 30, 39, 53 y 54; `ley="Reglamento (UE) 2018/1860"`, artículos 3, 6 y 14).
- **Cancelación de antecedentes penales** → `buscar_articulo` (`ley="CP"`, artículos 89 y 136; `ley="Real Decreto 95/2009"`, artículos 19, 20 y 25).
- **Supresión de datos policiales** → `buscar_articulo` (`ley="Ley Orgánica 7/2021"`, artículos 6, 8, 11, 22, 23, 24 y 25; el art. 23.2 remite a los arts. 6 y 11) y, para el final judicial, `ley="LECrim"` (arts. 637 y 641) y `ley="CP"` (art. 131, prescripción del delito, que decide si el responsable puede conservar los datos de una causa sobreseída provisionalmente).
- **Revocación de actos desfavorables y revisión** → `buscar_articulo` (`ley="LPAC"`, artículos 21, 106, 109 y 125; `ley="LJCA"`, artículo 46).
- **Doctrina sobre antecedentes, rechazable Schengen y levantamiento** → `buscar_sentencias` (`consulta="antecedentes policiales denegación autorización residencia valoración"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`), (`consulta="rechazable Schengen descripción SIS denegación autorización residencia"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`) + `leer_sentencias` (`parrafos=3`).
- **Revisión del documento** → cada redactor del equipo pasa `verificar_escrito` solo sobre sus frases con normas, y el ensamblado rechaza cualquier ECLI o ROJ que ningún redactor leyera; `buscar_por_cita` se usa solo con un ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Cuando el precepto lleve letra, ordinal o «bis», escribe «la letra a) del artículo 53.1 de la Ley Orgánica 4/2000» o «el número 1.º del artículo 641 de la Ley de Enjuiciamiento Criminal», y pon la norma en cada cita: con «53.1.a)» o «641.1.º», o sin norma detrás, el verificador no la identifica o la atribuye a la norma citada antes. El verificador no reconoce las normas de la Unión (Directiva 2008/115/CE, Reglamentos (UE) 2018/1860 y 2018/1861): atribuye sus artículos a otra norma del escrito. Si se leyeron con `buscar_articulo` en su norma, la cita es correcta; explícalo en el resumen.

Comprueba siempre que el título de la norma que devuelve `buscar_articulo` es el que pediste: si la base de normativa de la Unión falla, el conector puede devolver un artículo con el mismo número de otra norma española (pasó con el art. 11 de la Directiva 2008/115/CE, que devolvió el art. 11 del Real Decreto 1837/2008). Repite la consulta y, si sigue sin salir la norma correcta, aplica la puerta.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

## Cuándo usarla

- El cliente fue expulsado o devuelto, está fuera y quiere volver: se le deniega o se le va a denegar el visado por la prohibición de entrada.
- Salió de España durante el expediente o dentro del plazo de cumplimiento voluntario y la prohibición no se ha dejado sin efecto.
- Está en España con una expulsión o devolución no ejecutada y pide una autorización por circunstancias excepcionales: hay que pedir que se revoque.
- Una autorización, renovación o visado se deniega o extingue por figurar como «rechazable» en el espacio Schengen o por antecedentes penales o policiales.
- Hay antecedentes penales cancelables o datos policiales que deben suprimirse.

No la uses para:

- Defenderse en un expediente de expulsión en trámite → `expulsion-procedimiento-sancionador`.
- Recurrir en plazo la resolución de expulsión o la denegación → `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria` (esta skill solo detecta si todavía hay plazo).
- La buena conducta cívica en la nacionalidad por residencia → `nacionalidad-residencia`.
- La denegación del visado en sí (motivos distintos de la prohibición) → `visados-denegacion`; la renovación o extinción de la autorización → `renovacion-modificacion-extincion`.
- La prohibición de regreso que impone el juez penal al sustituir la pena por expulsión (art. 89 del Código Penal): no se levanta en vía administrativa; explícalo al abogado y deriva al proceso penal.

## Datos que hay que reunir antes de redactar

1. **Origen de la prohibición** y copia de la resolución: expulsión administrativa (infracción, órgano, fecha, firmeza, duración fijada), devolución (letra del art. 58.3 LOEX), expulsión judicial del art. 89 del Código Penal, prohibición acordada por otro Estado Schengen, prohibición del Ministro del Interior. Imprescindible.
2. **Salida de España**: fecha, lugar y prueba (sello, certificado del paso fronterizo, billete, personación consular), y si fue durante el expediente, en el plazo voluntario o por ejecución forzosa. Imprescindible si el cliente está fuera.
3. **Situación actual**: dónde está, qué quiere pedir (visado, autorización, renovación, arraigo, larga duración) y resolución denegatoria si existe, con su fecha de notificación. Imprescindible.
4. **Motivo exacto del bloqueo** tal como lo dice la resolución: prohibición de entrada, rechazable Schengen (Estado que la introdujo, si consta), antecedentes penales, informe policial desfavorable.
5. **Antecedentes penales**: órgano, fecha y delito de cada condena, pena, fecha de extinción o cumplimiento, suspensión o remisión, certificado actual; antecedentes en el país de origen o de residencia anterior.
6. **Antecedentes policiales**: detenciones o diligencias y su final judicial (sobreseimiento, absolución) con testimonio.
7. **Vínculos y cambio de circunstancias**: familia en España y su situación, trabajo ofrecido, tiempo transcurrido, razones humanitarias.
8. **Régimen del cliente**: si es ciudadano de la Unión o familiar sujeto al Real Decreto 240/2007 (apóyate en `ciudadanos-ue-y-familiares`), o familiar de persona con nacionalidad española (arts. 93 a 99 del Reglamento; `familiares-de-espanoles`): cambia la norma aplicable.

Sin los datos 1 a 3 no se redacta: si faltan tras leer la documentación, pídelos todos a la vez en una única ronda (paso 2 de `redaccion-rapida`). Lo que falte va con marcador (`[FECHA DE SALIDA]`, `[NÚMERO DE EXPEDIENTE DE EXPULSIÓN]`, `[ESTADO QUE INTRODUJO LA DESCRIPCIÓN]`).

## Requisitos y comprobaciones

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo. Si la respuesta trae una nota «Téngase en cuenta…» (nulidad declarada por el Tribunal Supremo, como la sentencia de julio de 2026 publicada en `BOE-A-2026-19632`, o una reforma), léela y aplícala: lo anulado no se aplica ni se cita como vigente.

### 1. Identifica la prohibición y su régimen

- **Expulsión administrativa**: art. 58.1 y 58.2 LOEX y art. 244.2 del Reglamento (duración según las circunstancias, límite ordinario, supuesto excepcional con informe de la Comisaría General) y extensión a los Estados con acuerdo (arts. 242.c) y 244.2). La expulsión extingue las autorizaciones y archiva los procedimientos (art. 57.4 LOEX; art. 244.3).
- **Cómputo**: busca doctrina sobre desde cuándo corre la prohibición (`consulta='prohibición de entrada "abandonó efectivamente el territorio"'`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`; si no da nada, quita las comillas); las sentencias que la aplican citan la del TJUE: ábrela con `buscar_por_cita` con el número de asunto que aparezca y calcula la fecha de vencimiento.
- **Devolución**: art. 58.3 y 58.7 LOEX y art. 23 del Reglamento (la devolución por quebrantar la prohibición reinicia su cómputo, art. 23.5; prescripción de la devolución, art. 23.7). El inciso del art. 58.7 que ligaba una prohibición de tres años a toda devolución por entrada ilegal fue declarado inconstitucional: el conector lo señala en la nota del artículo; lee la sentencia con `buscar_sentencias` (`consulta="devolución prohibición de entrada tres años inconstitucional"`, `base="TC"`) antes de alegarlo. El art. 11.b) del Reglamento solo menciona la devolución del art. 58.3.a).
- **Expulsión judicial**: art. 89.5 y 89.7 del Código Penal (plazo de no regreso fijado por el juez). Fuera del alcance administrativo.
- **Prohibición de otro Estado**: solo puede levantarla el Estado que la dictó (Directiva 2008/115/CE, art. 11.4; Reglamento (UE) 2018/1861, arts. 24 y 39). Aquí se prepara el ejercicio de derechos sobre el dato (apartado 3) y se avisa de que la revocación se pide en ese Estado.
- **Régimen de la Unión**: si el cliente está sujeto al Real Decreto 240/2007, lee su art. 15 (`ley="Real Decreto 240/2007"`): regula la solicitud de levantamiento, el cambio material de circunstancias, el plazo mínimo y el de resolución. Úsalo en lugar de las vías del apartado 2.
- **Supuestos de prohibición de entrada y prescripción**: art. 26.1 LOEX y art. 11 del Reglamento (la letra a) excluye los casos de caducidad del procedimiento o prescripción de la infracción o de la sanción); prescripción de la sanción de expulsión: art. 56.3 LOEX y art. 224.3 del Reglamento.

### 2. Vías para dejarla sin efecto (con su fundamento)

Comprueba cuál encaja y en este orden:

1. **No imposición o revocación por salida** (art. 58.2 LOEX, párrafo segundo; art. 244.2 del Reglamento; Directiva 2008/115/CE, art. 11.3, párrafo primero): solo expedientes por las letras a) y b) del art. 53.1 LOEX; salida durante la tramitación o en el plazo de cumplimiento voluntario; comunicación de la salida en una de las formas del art. 244.2 (impreso en el control fronterizo o personación consular con prueba). Si la salida no se comunicó, comunícala ahora: en el propio escrito al órgano que sancionó, con la prueba de la fecha (sello de salida, tarjetas de embarque; el art. 245.6 admite el certificado del paso fronterizo), y aconseja además la personación consular de la letra b) del art. 244.2, cuyo justificante se aportará después. Comprueba que el expediente fue ordinario: en el preferente no hay plazo de cumplimiento voluntario y esta vía no existe.
2. **Revocación de la expulsión por concesión de una autorización por circunstancias excepcionales** (art. 240.2 del Reglamento, para las de los arts. 31 bis, 59, 59 bis y 68.3 LOEX; art. 240.3 para las demás cuando el análisis inicial muestra indicios claros de concesión). Para la devolución no ejecutada, art. 23.8. El art. 240.3 remite a la disposición adicional cuarta de la LOEX, que el conector no devuelve: si el caso depende de su texto (por ejemplo, una inadmisión fundada en ella), aplica la puerta y di al abogado qué precepto falta.
3. **Revocación por motivos humanitarios u otros** (Directiva 2008/115/CE, art. 11.3, párrafos tercero y cuarto) junto con la revocación de actos desfavorables del art. 109.1 LPAC (límites: prescripción, igualdad, interés público). El art. 57.4 LOEX remite los supuestos de revocación de la expulsión al Reglamento: no afirmes un derecho a la revocación fuera de los supuestos reglamentarios; plantéalo como solicitud motivada con cambio de circunstancias.
4. **Nulidad o revisión**: revisión de oficio de actos nulos (art. 106 LPAC) o recurso extraordinario de revisión (art. 125 LPAC: causas y plazos), por ejemplo cuando una sentencia penal absolutoria posterior deja sin base una expulsión por condena.
5. **Recurso ordinario** si aún hay plazo (art. 46 LJCA): pásalo a `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria`.
6. **Reducción de la duración** cuando no cabe levantarla: proporcionalidad y circunstancias personales.

### 3. Sistema de Información Schengen

- Descripción para denegar la entrada: Reglamento (UE) 2018/1861, art. 24 (condiciones; efecto desde la salida; derecho a recurrir) y art. 39 (revisión y supresión automática). Consultas entre Estados cuando hay permiso de residencia o visado: arts. 28 a 30. Comprueba que el título que devuelve el conector coincide con el que citas; si no coincide, aplica la puerta.
- Descripción sobre retorno: Reglamento (UE) 2018/1860, arts. 3, 6 (confirmación del retorno y supresión) y 14 (supresión si la decisión se revoca o anula, o si se acredita la salida).
- Derechos de acceso, rectificación y supresión y vías de recurso en cualquier Estado: arts. 53 y 54 del Reglamento (UE) 2018/1861.
- «Rechazable» como causa de denegación: art. 31.5 LOEX y art. 126.e) del Reglamento. Busca la doctrina del TSJ del territorio que exige consultar el SIS y al Estado emisor antes de denegar, sobre todo en renovaciones (`consulta="rechazable Schengen descripción SIS denegación autorización residencia"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`).

### 4. Antecedentes penales

- Dónde bloquean: residencia temporal inicial (art. 31.5 LOEX), renovación (art. 31.7.a) LOEX: se valoran, con indultos, remisión o suspensión), arraigo (art. 126.d) del Reglamento), certificados del país de origen y valoración no automática del informe policial (art. 130.2), expulsión por condena salvo antecedentes cancelados (art. 57.2 LOEX), extinción por las condenas del art. 200.2.h) y 201.1.f).
- Cancelación: art. 136 del Código Penal (plazos desde la extinción de la pena, cómputo con remisión condicional, efectos del apartado 5) y art. 19 del Real Decreto 95/2009 (de oficio o a instancia; plazo para resolver; sentido del silencio; recurso). El art. 20 de ese real decreto remite a un apartado del art. 136 con numeración anterior: cita el apartado que devuelva el conector para el Código Penal vigente.
- Calcula con el cliente la fecha en que se cumple el plazo de cada condena, con la fecha de extinción y el precepto. Sin fecha de extinción no des fecha de cancelación: pídela o pide que se solicite al órgano sentenciador.
- Los antecedentes en otros países se cancelan según su propia ley: no redactes esa solicitud; indica al abogado qué certificado necesita.

### 5. Antecedentes policiales

- No son antecedentes penales. Derechos: acceso (art. 22 de la Ley Orgánica 7/2021), rectificación y supresión (art. 23, plazo para suprimir), restricciones y deber de informar (art. 24), ejercicio a través de la autoridad de protección de datos y recurso (art. 25), revisión y plazo máximo de conservación (art. 8).
- Acredita el final judicial (sobreseimiento, absolución) con testimonio y pide la supresión al responsable del tratamiento que figure en el informe policial. No inventes el órgano ni la dirección: si no consta, marcador y aviso de que se compruebe en la sede oficial.
- Distingue el final de cada causa. Con absolución firme o sobreseimiento libre, pide la supresión (art. 23.2 en relación con el art. 6.1, letras d) y e), y el art. 11.1 de la Ley Orgánica 7/2021). Con sobreseimiento provisional, el responsable puede conservar los datos mientras el delito no haya prescrito (art. 8.3): pide la supresión como principal y, subsidiariamente, que se completen con el archivo (art. 23.1), se limite su tratamiento y se fije la fecha de supresión; calcula la prescripción con el art. 131 CP según la calificación que conste en el auto. Pide en todo caso la comunicación a los destinatarios, incluida la oficina de extranjería (art. 23.5), y el acceso del art. 22.1.
- La jurisprudencia no es imprescindible en la solicitud de supresión, que se funda en la Ley Orgánica 7/2021: si tras dos reformulaciones no aparece doctrina aplicable, redacta con los preceptos y dilo en el resumen. La doctrina del Supremo sobre antecedentes policiales en extranjería sí es imprescindible en el recurso contra la denegación.
- En el procedimiento de autorización, busca y cita la doctrina del Supremo que exige valorar los antecedentes en su contexto, sin automatismo, y que rechaza fundar la denegación en la mera mención de un delito sin su resultado judicial.

### 6. Plazos

- Solicitudes de revocación: no tienen plazo propio; el límite es la prescripción (art. 109.1 LPAC). Plazo para resolver: el de la norma aplicable (en el régimen de la Unión, el del art. 15 del Real Decreto 240/2007) o el del art. 21 LPAC. Los plazos de resolución y el sentido del silencio en extranjería están en las disposiciones adicionales séptima y octava del Reglamento, que el conector no devuelve: no afirmes ni plazo ni silencio con base en ellas; indícalo al abogado como dato que debe comprobar.
- Recurso extraordinario de revisión: plazos del art. 125.2 LPAC desde la notificación o desde el conocimiento del documento o la firmeza de la sentencia.
- Cancelación de antecedentes penales y supresión de datos policiales: plazos del art. 19.2 del Real Decreto 95/2009 y de los arts. 23.2 y 24.2 de la Ley Orgánica 7/2021.
- Si hay una denegación notificada, calcula el plazo del recurso con su precepto y avisa de inmediato.

## Estrategia y jurisprudencia

1. Clasifica el origen de la prohibición; si es judicial o de otro Estado, dilo al principio y ajusta el encargo.
2. Calcula la fecha de vencimiento de la prohibición y la de prescripción de la sanción: a veces basta esperar o pedir que se declare vencida.
3. Elige la vía del apartado 2 que tenga respaldo en un artículo leído; las vías generales (art. 109 LPAC, Directiva art. 11.3) van como subsidiarias.
4. Limpia a la vez los obstáculos accesorios: cancelación de antecedentes, supresión de datos policiales, descripción en el SIS.

Consultas (siempre `jurisdiccion="CONTENCIOSO"` salvo el TC):

| Cuestión | `consulta` | Filtros |
|---|---|---|
| Revocación de la expulsión al conceder circunstancias excepcionales | «revocación expulsión no ejecutada arraigo autorización circunstancias excepcionales» | `base="AN"`, `tipo_organo="TSJ"` |
| Cómputo de la prohibición | «prohibición de entrada "abandonó efectivamente el territorio"» | `base="AN"` |
| Salida en plazo y revocación | «prohibición de entrada abandonó territorio revocación comunicación salida» | `base="AN"`, `tipo_organo="TSJ"` |
| Levantamiento en el régimen de la Unión | «levantamiento prohibición de entrada cambio material de circunstancias» | `base="AN"` |
| Rechazable Schengen | «rechazable Schengen descripción SIS denegación autorización residencia» | `base="AN"` |
| Antecedentes policiales | «antecedentes policiales denegación autorización residencia valoración» | `base="TS"` |
| Renovación con antecedentes penales | «renovación autorización residencia antecedentes penales suspensión de la pena valoración» | `base="TS"` |
| Antecedentes cancelados | «cancelación antecedentes penales autorización residencia renovación» | `base="AN"`, `tipo_organo="TSJ"` |
| Devolución y prohibición | «devolución prohibición de entrada tres años inconstitucional» | `base="TC"` |

- Lee solo lo que vayas a citar (`leer_sentencias`, `parrafos=3`). Comprueba qué reglamento aplicó cada sentencia: muchas aplican aún el Reglamento anterior (Real Decreto 557/2011), con otra numeración; usa su doctrina, pero cita el artículo vigente leído.
- Para el TJUE, parte de las sentencias españolas que lo citan y abre la resolución con `buscar_por_cita`; la búsqueda por texto en `base="TJUE"` da resultados ajenos en esta materia.

## Documento que se entrega

Formato según `references/formato-y-organos.md` del plugin; ante la Administración, «SOLICITA».

1. **Solicitud de revocación (o de no imposición, o de reducción) de la prohibición de entrada** — a la Delegación o Subdelegación del Gobierno que dictó la expulsión o devolución (tómalo de la resolución; arts. 221 y 244.2 del Reglamento), con número de expediente. Estructura: comparecencia (si el cliente está fuera, con representación y domicilio en España a efectos de notificaciones); HECHOS (resolución, notificación, salida y su prueba, tiempo transcurrido, vínculos y cambio de circunstancias); FUNDAMENTOS (la vía elegida con su precepto y, subsidiariamente, las generales; efectos en el SIS); SOLICITA: revocación o no imposición, comunicación de la baja de la descripción en el SIS y certificación de la resolución; subsidiariamente, reducción de la duración; documentos numerados. Archivo: `solicitud-revocacion-prohibicion-entrada-<apellido>-<AAAAMMDD>.docx`.
2. Solo si procede, cada uno en archivo aparte (si no hay prohibición de entrada, el documento principal es el de cancelación o supresión que corresponda, y el resumen indica el plazo del recurso contra la denegación y remite a la skill de recursos):
   - **Solicitud de cancelación de antecedentes penales** al Ministerio de Justicia, Registro Central de Penados (art. 136.1 del Código Penal): condenas, fechas de extinción, plazos cumplidos. `solicitud-cancelacion-antecedentes-penales-<apellido>-<AAAAMMDD>.docx`.
   - **Solicitud de supresión de datos policiales** al responsable del tratamiento (art. 23 de la Ley Orgánica 7/2021), con el testimonio del final judicial. `solicitud-supresion-datos-policiales-<apellido>-<AAAAMMDD>.docx`.
   - **Solicitud de acceso y, en su caso, supresión de la descripción en el SIS** (arts. 53 y 54 del Reglamento (UE) 2018/1861). `solicitud-acceso-sis-<apellido>-<AAAAMMDD>.docx`.

**Reparto para la redacción rápida:** solicitud de revocación: 01 encabezamiento, comparecencia y hechos; 02 fundamentos (la vía elegida con su precepto y las subsidiarias, con doctrina); 03 efectos en el SIS, solicita y documentos. Los documentos del punto 2 (cancelación de antecedentes, supresión de datos policiales, acceso al SIS) son de una o dos páginas: el director los redacta sin equipo, cada uno en su archivo.

No indiques modelos oficiales, tasas, códigos ni direcciones de presentación: di que se comprueben en la sede electrónica oficial del órgano.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» y el resto de normas como indica el apartado 4 de `references/formato-y-organos.md` (por ejemplo, «Ley Orgánica 4/2000», no «Reglamento de Extranjería»), para que `verificar_escrito` las reconozca.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió al empezar.
- [ ] Origen de la prohibición identificado y, si es judicial o de otro Estado, advertido al abogado.
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación; ningún inciso declarado inconstitucional o anulado se cita como vigente; ninguna disposición adicional se cita sin texto devuelto por el conector.
- [ ] Fecha de vencimiento de la prohibición y de prescripción de la sanción calculadas con su precepto y la fecha de salida.
- [ ] Cada ECLI se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; solo doctrina, sin datos de las partes de otros pleitos.
- [ ] `verificar_escrito` pasado sobre las frases con normas de cada documento y avisos resueltos.
- [ ] Marcadores en los datos que faltan; ningún órgano, dirección, tasa ni modelo inventado.
- [ ] Resumen para el abogado según el apartado 7 del formato: documentos preparados y órgano de cada uno, plazos con su precepto (recurso pendiente, plazo para resolver), obstáculos que quedan (SIS de otro Estado, antecedentes en el extranjero, silencio no determinado), tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene) y próximo paso (presentar la revocación antes de pedir el visado o la autorización).
