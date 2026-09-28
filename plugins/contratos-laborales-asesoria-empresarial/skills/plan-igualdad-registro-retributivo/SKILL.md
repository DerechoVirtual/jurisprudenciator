---
name: plan-igualdad-registro-retributivo
description: >-
  Plan de igualdad (obligación desde 50 personas, cómputo, plazos, comisión negociadora con o sin
  representación, diagnóstico, contenido, vigencia y registro), registro y auditoría retributiva, y medidas
  planificadas LGTBI. Úsala con «plan de igualdad», «hemos pasado de 50 trabajadores», «registro salarial»,
  «brecha del 25 %», «auditoría retributiva», «medidas LGTBI» o «no tenemos comité, ¿con quién negociamos?».
  Sirve a la empresa y a la representación o al trabajador que exige el registro o impugna un plan. Entrega
  hoja de ruta, el documento pedido (acta de constitución, esquema del diagnóstico o registro retributivo) y
  nota. Para el protocolo de acoso usa protocolo-acoso-laboral; para un acta de la Inspección,
  inspeccion-trabajo-alegaciones; para la brecha de un trabajador concreto, tutela-derechos-fundamentales o
  reclamacion-cantidad.
---

# Plan de igualdad, registro retributivo y medidas LGTBI

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Obligación, contenido del plan, transparencia y registro de planes** → `buscar_articulo` (`ley="BOE-A-2007-6115"`, artículos `"45"`, `"46"` y `"47"`) y deber de negociar en convenio (`ley="ET"`, artículos `"85"` y, si es grupo, `"87"`).
- **Cómputo de plantilla, plazos, comisión negociadora, diagnóstico, contenido mínimo, vigencia y registro** → `buscar_articulo` (`ley="BOE-A-2020-12214"`, artículos `"2"` a `"11"`). El anexo con los criterios del diagnóstico no lo devuelve `buscar_articulo` y `leer_boe` (`identificador="BOE-A-2020-12214"`) lo corta: búscalo en internet (ver «Lo que el conector no devuelve»).
- **Registro retributivo, valoración de puestos y auditoría retributiva** → `buscar_articulo` (`ley="ET"`, `articulo="28"`) y (`ley="BOE-A-2020-12215"`, artículos `"3"` a `"10"`).
- **Medidas planificadas LGTBI** → `buscar_articulo` (`ley="BOE-A-2023-5366"`, `articulo="15"`; comprueba que la cabecera es la Ley 4/2023, de 28 de febrero) y (`ley="Real Decreto 1026/2024"`, artículos `"2"` a `"9"`); sus anexos I (medidas) y II (protocolo) → `leer_boe` (`identificador="BOE-A-2024-20402"`).
- **Consecuencias del incumplimiento** → `buscar_articulo` (`ley="BOE-A-2000-15060"`, artículos `"7"`, `"8"` y `"46 bis"`); cuantías, del artículo `"40"` en el momento.
- **Mejoras del convenio** (plazos, obligación por debajo del umbral, comisión de igualdad, clasificación profesional) → `buscar_convenio` + `leer_convenio` (`buscar_en="igualdad"` y `buscar_en="clasificación profesional"`) + `vigencia_convenio`.
- **Doctrina sobre legitimación negociadora, plan aprobado por la empresa y alcance del registro retributivo** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`); Audiencia Nacional con `base="AN"`, `jurisdiccion="SOCIAL"`.
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

- La empresa alcanza el umbral, quiere saber si está obligada y desde cuándo corre el plazo, o tiene un plan vencido o que hay que revisar.
- No hay comité ni delegados y hay que formar la comisión negociadora.
- Hay que elaborar o revisar el registro retributivo, justificar una diferencia retributiva o preparar la auditoría retributiva.
- Hay que negociar o implantar las medidas planificadas LGTBI y su protocolo.
- La representación legal, un sindicato o un trabajador quiere acceder al registro, impugnar un plan aprobado sin negociación o exigir su negociación.

Pregunta primero a quién asesora el abogado: la empresa quiere un calendario que cumpla y documentos defendibles ante la Inspección; la parte social quiere detectar el defecto de legitimación, de negociación o de información que invalida el plan o el registro.

| Si lo que se necesita es… | Usa |
|---|---|
| El protocolo frente al acoso sexual, por razón de sexo, laboral o LGTBI, o instruir una denuncia | `protocolo-acoso-laboral` |
| Contestar un requerimiento o un acta de la Inspección sobre el plan o el registro | `inspeccion-trabajo-alegaciones` |
| Reclamar la diferencia salarial de un trabajador concreto o la tutela por discriminación | `reclamacion-cantidad` o `tutela-derechos-fundamentales` |
| Saber qué convenio aplica a la empresa | `convenio-aplicable` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ Parte asesorada y documento que se pide (hoja de ruta, acta de constitución, esquema del diagnóstico, registro retributivo, revisión de un plan, medidas LGTBI).
2. ★ Plantilla total a 30 de junio y a 31 de diciembre de los últimos años: fijos, fijos discontinuos, temporales, tiempo parcial, puestos a disposición por ETT, y contratos temporales extinguidos en los seis meses anteriores con los días trabajados de cada uno. Fecha en que se alcanzó por primera vez el umbral.
3. ★ Representación legal: comité, delegados, secciones sindicales y su peso en el comité; comité intercentros y sus competencias; centros con y sin representación.
4. ★ Convenio o convenios aplicables (y si imponen plan por debajo del umbral o mejoran plazos), y si la empresa pertenece a un grupo que quiera un plan único.
5. Plan anterior: fecha de firma, vigencia, inscripción, evaluaciones hechas y hechos que obligan a revisarlo (fusión, modificaciones sustanciales, inaplicación del convenio, sentencia o actuación de la Inspección).
6. Para el registro retributivo: sistema de clasificación, conceptos salariales y extrasalariales, año de referencia, si hay auditoría retributiva y valoración de puestos, y fecha de la consulta a la representación.
7. Para las medidas LGTBI: plantilla computada, convenio que ya las recoja, representación y estado de la negociación.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la fecha de vigencia.

**A. Obligación y plazos**

- Todas las empresas deben negociar medidas contra la discriminación y arbitrar procedimientos frente al acoso sexual y por razón de sexo (art. 45.1 LO 3/2007; art. 2.1 del Real Decreto 901/2020). Desde cincuenta o más personas trabajadoras, esas medidas se articulan en un plan de igualdad (art. 45.2 LO 3/2007); también cuando lo imponga el convenio o lo acuerde la autoridad laboral en sustitución de sanciones accesorias (art. 45.3 y 45.4; art. 46 bis del Real Decreto Legislativo 5/2000). El art. 85.2 ET aún habla de «más de doscientos cincuenta» para el deber de negociarlo a través del convenio: la obligación del plan nace del art. 45.2 LO 3/2007, no de ese umbral.
- Cómputo (art. 3 del Real Decreto 901/2020): plantilla total de la empresa, todos los centros y todas las modalidades; cada contrato a tiempo parcial cuenta como una persona; se suman los temporales extinguidos en los seis meses anteriores a razón de una persona por cada cien días trabajados o fracción; se comprueba al menos el último día de junio y de diciembre. Alcanzado el umbral, la obligación subsiste aunque la plantilla baje, desde la constitución de la comisión hasta el fin de la vigencia del plan o durante cuatro años.
- Plazos (art. 4): constituir la comisión negociadora en los tres meses siguientes a alcanzar el umbral (o el plazo del convenio, o el del acuerdo sancionador); tener el plan negociado, aprobado y con la solicitud de registro presentada en un año desde el día siguiente al fin de ese plazo. Calcula las dos fechas y ponlas en la hoja de ruta con su precepto.

**B. Comisión negociadora (art. 5 del Real Decreto 901/2020)**

- Paritaria. Con representación legal: comité o delegados, o las secciones sindicales que sumen la mayoría del comité si así lo acuerdan; composición proporcional a la representatividad; comité intercentros si tiene competencias; en grupos, las reglas del art. 87 ET (art. 5.2).
- Sin representación legal: comisión sindical con los sindicatos más representativos y los representativos del sector legitimados para negociar el convenio aplicable, hasta seis miembros por parte; queda válidamente integrada por los que respondan a la convocatoria de la empresa en diez días (art. 5.3). Con centros con y sin representación, hasta trece miembros por parte.
- Una comisión formada por trabajadores elegidos ad hoc no está prevista. El plan elaborado por la empresa sin negociar solo se ha admitido de forma excepcional tras un bloqueo o una incomparecencia sindical prolongada y documentada: localiza la doctrina y comprueba qué convocatorias, reiteraciones y plazos exigió.
- Composición equilibrada y formación en igualdad (art. 5.4); acta de cada reunión (art. 5.5); buena fe y acuerdo con la conformidad de la empresa y de la mayoría de la parte social (art. 5.6); acceso a la información del art. 46.2 LO 3/2007 (art. 5.7); sigilo (art. 5.8); competencias y reglamento interno (art. 6).

**C. Diagnóstico y contenido del plan**

- Diagnóstico negociado en la comisión sobre, al menos, las nueve materias de la letra a) a la i) del art. 7.1 del Real Decreto 901/2020 (las mismas del art. 46.2 LO 3/2007), extendido a todos los puestos, centros y niveles, con datos desagregados por sexo, incluidas las personas cedidas por ETT (art. 7.2); si revela infrarrepresentación, el plan debe incluir medidas para corregirla (art. 7.4). Un resumen del diagnóstico forma parte del plan (art. 7.1).
- Contenido mínimo: las once letras del art. 8.2 (partes, ámbitos, informe de diagnóstico, resultados de la auditoría retributiva, objetivos, medidas con plazo, prioridad e indicadores, medios, calendario, seguimiento, comisión de seguimiento, procedimiento de modificación). Las medidas deben responder a la situación real de la empresa (art. 8.4): no copies planes tipo.
- Vigencia máxima de cuatro años (art. 9.1); revisión obligatoria en los supuestos del art. 9.2; evaluación intermedia y final (art. 9.6); comisión paritaria de seguimiento (art. 9.5). Alcanza a toda la plantilla y a las personas cedidas por ETT durante su servicio (art. 10).
- Inscripción obligatoria, se haya acordado o no, en el registro de convenios y acuerdos colectivos, con la hoja estadística del Real Decreto 713/2010 (art. 11; art. 46.4 y 46.5 LO 3/2007). La vía de presentación: búscala en internet en la sede electrónica de la autoridad laboral competente (estatal o autonómica) y cita el enlace con la fecha de consulta. Los protocolos de acoso pueden depositarse voluntariamente (art. 12).

**D. Registro retributivo y auditoría retributiva**

- Todas las empresas, sea cual sea su tamaño, llevan un registro de toda la plantilla, incluidos directivos y altos cargos (art. 28.2 ET; art. 5.1 del Real Decreto 902/2020), con media aritmética y mediana de lo realmente percibido, por sexo, por grupo, categoría, nivel o puesto, y desglosado por salario base, cada complemento y cada percepción extrasalarial (art. 5.2). Periodo de referencia: el año natural (art. 5.4). Consulta previa a la representación con diez días de antelación, también para modificarlo (art. 5.6).
- Acceso: con representación legal, a través de ella y con el contenido íntegro; sin representación, el trabajador solo recibe las diferencias porcentuales (art. 5.3; art. 28.2 ET). El registro contiene valores medios, no individuales: busca la doctrina sobre datos que permiten identificar la retribución de una persona.
- En empresas de al menos cincuenta trabajadores, si el promedio de un sexo supera al del otro en un veinticinco por ciento o más, el registro incluye la justificación de que la diferencia no responde al sexo (art. 28.3 ET); esa justificación no descarta por sí sola indicios de discriminación (art. 10.2 del Real Decreto 902/2020).
- Auditoría retributiva: obligatoria dentro del plan (art. 7 del Real Decreto 902/2020), con diagnóstico basado en la valoración de puestos según los criterios de adecuación, totalidad y objetividad (arts. 4 y 8) y plan de actuación; con auditoría, el registro añade las agrupaciones de trabajos de igual valor (art. 6).
- Directiva (UE) 2023/970 de transparencia retributiva: su plazo de transposición vencía el 7 de junio de 2026 (lee su art. 34 con `buscar_articulo`, `ley="Directiva (UE) 2023/970"`). Antes de redactar, comprueba en la línea «redacción vigente dada por…» del art. 28 ET y de los arts. 5 a 8 del Real Decreto 902/2020 si se ha transpuesto, busca con `buscar_boe` (`consulta="transparencia retributiva"`) y, si no aparece nada, confírmalo en internet en el BOE y en EUR-Lex (medidas nacionales de transposición), con enlace. Si no hay norma española que la transponga, aplica la vigente, no presentes la Directiva como obligación directa de la empresa y señala el riesgo en la nota.

**E. Medidas planificadas LGTBI**

- Obligación para las empresas de **más** de cincuenta personas trabajadoras (art. 15.1 de la Ley 4/2023, de 28 de febrero; art. 2.1 del Real Decreto 1026/2024): una empresa con cincuenta exactas tiene plan de igualdad pero no estas medidas. Cómputo como en el plan, fijado el día de constitución de la comisión (art. 3).
- Cauce: el convenio (de empresa o sectorial); con convenio anterior, la comisión negociadora se reúne solo para el anexo I; sin convenio y con representación, acuerdo de empresa; sin convenio ni representación, comisión sindical del art. 6.4 (art. 4). Si ningún sindicato responde en diez días hábiles, ampliables otros diez, la empresa puede fijarlas unilateralmente con el contenido del real decreto (art. 6.4).
- Plazos: constituir la comisión en tres meses (seis sin convenio ni representación) desde la entrada en vigor del real decreto o desde que se alcanza el umbral; a los tres meses de negociación sin acuerdo, se aplican las medidas del real decreto (art. 5).
- Contenido: al menos las medidas del anexo I y un protocolo frente al acoso y la violencia con el contenido mínimo del anexo II, que puede cumplirse ampliando el protocolo general (art. 8.3 y 8.4). Se respetan en la sucesión de empresa (art. 9.3). El protocolo se redacta con `protocolo-acoso-laboral`.

**F. Incumplimiento**

- No cumplir las obligaciones sobre planes y medidas de igualdad es infracción grave (apartado 13 del artículo 7 del Real Decreto Legislativo 5/2000); no elaborar o no aplicar el plan impuesto en sustitución de sanciones accesorias, muy grave (apartado 17 del artículo 8, en relación con el artículo 46 bis). La información retributiva o su ausencia sirve para las acciones administrativas y judiciales, incluido el procedimiento de oficio (art. 10.1 del Real Decreto 902/2020).

**Lo que el conector no devuelve: búscalo en internet en la fuente oficial y cítalo con enlace y fecha de consulta**

- El anexo del Real Decreto 901/2020 (criterios específicos del diagnóstico): `leer_boe` corta el texto antes de llegar a él. Léelo en el texto consolidado del BOE (www.boe.es, identificador BOE-A-2020-12214) e incorpora sus criterios al esquema del diagnóstico, citando el enlace; si no lo encuentras, construye el esquema solo sobre el art. 7 y el art. 46.2 LO 3/2007 y dilo en el resumen.
- El formato del registro retributivo y las guías y herramientas oficiales de igualdad retributiva y de planes de igualdad (art. 5.5 del Real Decreto 902/2020): búscalos en las webs oficiales del Ministerio de Trabajo y del Ministerio de Igualdad y cítalos con enlace.
- La Ley 4/2023, si `buscar_articulo` no devolviera su art. 15 con la cabecera correcta tras buscar su identificador con `buscar_boe`: léela en el BOE y cítala con enlace.

## Estrategia y jurisprudencia

1. **Empresa:** fija primero la fecha en que se alcanzó el umbral con el cómputo del art. 3 y documenta los cortes de junio y diciembre; sin esa fecha no hay calendario. Si no hay representación, convoca por escrito y de forma acreditable a todos los sindicatos legitimados, reitera las convocatorias y guarda las respuestas: es la única vía para que un plan sin acuerdo pueda sostenerse. Documenta cada reunión con acta y manifestaciones de parte.
2. **Parte social:** revisa la legitimación de quien negoció, si hubo diagnóstico negociado, si se entregó la información del art. 46.2 LO 3/2007 y si el registro incluye todos los conceptos y la justificación del art. 28.3 ET.
3. Consultas en Jurisprudenciator (reformula como máximo dos veces):
   - Plan elaborado por la empresa: `consulta="plan de igualdad elaborado unilateralmente por la empresa incomparecencia sindical"`, `base="TS"`, `jurisdiccion="SOCIAL"`; lee la más reciente y la que fija la excepcionalidad.
   - Legitimación: `consulta="plan de igualdad comisión ad hoc trabajadores sin representación legal comisión sindical"`, mismos filtros.
   - Registro: `consulta="registro retributivo valores medios identificación persona trabajadora"`, `base="TS"`, `jurisdiccion="SOCIAL"`; y `consulta="registro retributivo información a entregar"`, `base="AN"`, `jurisdiccion="SOCIAL"`.
   - Igual valor: `consulta="trabajo de igual valor discriminación retributiva indirecta por razón de sexo complemento salarial"`, `base="TS"`, `jurisdiccion="SOCIAL"`, `anios=5`.
   - Registro del plan: `consulta="denegación inscripción plan de igualdad"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
4. Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y transcribe fundamentos, nunca hechos ni datos de aquellas empresas. En la hoja de ruta y en los documentos internos, la doctrina se cita si existe y en la nota siempre que el caso discuta la legitimación o el alcance del registro.

## Documentos que se entregan

Word maquetado según `references/formato-y-organos-laboral.md`.

**1. Hoja de ruta** — `nota-hoja-ruta-igualdad-<empresa>-<AAAAMMDD>.docx`: obligaciones que tiene la empresa (plan, registro, auditoría, medidas LGTBI, protocolo) con su artículo; cálculo de la plantilla en tabla (modalidad · personas · regla del art. 3 · cómputo) y fecha de alcance del umbral; calendario en tabla (hito · fecha límite · precepto · responsable); composición de la comisión según el caso; riesgos y consecuencias del incumplimiento.

**2. El documento que pida el abogado:**

- **Acta de constitución de la comisión negociadora** — `acta-constitucion-comision-igualdad-<empresa>-<AAAAMMDD>.docx`: lugar, fecha y hora; parte empresarial y parte social con su legitimación (órgano de representación o sindicatos, convocatoria y respuesta si no hay representación); composición proporcional y equilibrada; asesores con voz y sin voto; objeto (diagnóstico y plan, auditoría retributiva); reglas de funcionamiento o remisión al reglamento; régimen de adopción de acuerdos (art. 5.6); información que la empresa se compromete a entregar y plazo; sigilo (art. 5.8); calendario de reuniones; firmas.
- **Esquema del diagnóstico** — `esquema-diagnostico-igualdad-<empresa>-<AAAAMMDD>.docx`: una sección por cada materia del art. 7.1 con los indicadores desagregados por sexo, la fuente de cada dato en la empresa y el responsable de facilitarlo; apartado de retribuciones enlazado con el registro y la auditoría; conclusiones y propuestas en blanco para la comisión. Incorpora los criterios del anexo del Real Decreto 901/2020 leídos en el BOE, con su enlace; si no se han podido leer, deja un aviso visible de que faltan.
- **Registro retributivo** — `registro-retributivo-<empresa>-<AAAA>.docx`: tabla por grupo, categoría o puesto × concepto (salario base, cada complemento, cada percepción extrasalarial) × media y mediana de mujeres y de hombres × diferencia porcentual; con auditoría, las agrupaciones de igual valor; la justificación del art. 28.3 ET si procede; y constancia de la consulta previa a la representación. Solo con datos que facilite la empresa: sin ellos, entrega la plantilla con marcadores (`[MEDIA MUJERES]`, `[MEDIANA HOMBRES]`) y no inventes cifras. Deja visible cada operación.

**3. Nota para el abogado** — `nota-abogado-igualdad-<empresa>-<AAAAMMDD>.docx`: artículos leídos con su vigencia, convenio y artículo leído, doctrina con párrafo literal, estado de transposición de la Directiva (UE) 2023/970, lagunas del conector y riesgos.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los arts. 45 a 47 LO 3/2007, los del Real Decreto 901/2020 y del Real Decreto 902/2020 que se usan, el art. 28 ET y, si hay medidas LGTBI, el art. 15 de la Ley 4/2023 (cabecera comprobada) y los del Real Decreto 1026/2024; anexos leídos con `leer_boe`.
- [ ] Cómputo de plantilla con la regla del art. 3 visible y fecha de umbral; plazos con fecha inicial, precepto y fecha final.
- [ ] Convenio identificado con su código, artículos sobre igualdad leídos y vigencia comprobada.
- [ ] Estado de transposición de la Directiva (UE) 2023/970 comprobado y explicado en la nota.
- [ ] Lo obtenido en internet (anexo del Real Decreto 901/2020, formatos o guías oficiales, vía de registro) citado con enlace y fecha de consulta y señalado en el resumen.
- [ ] Cada ECLI citado leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre cada documento; ignorado su veredicto sobre artículos de convenio o de la Directiva tras comprobarlos con `leer_convenio` o `buscar_articulo`.
- [ ] Ningún dato retributivo inventado; marcadores donde faltan.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado, fechas límite con su precepto, cálculos de plantilla y de diferencias con su origen, documentos que faltan, tabla de jurisprudencia y próximo paso.
