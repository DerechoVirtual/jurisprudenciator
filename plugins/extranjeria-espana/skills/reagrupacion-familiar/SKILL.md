---
name: reagrupacion-familiar
description: >-
  Prepara la solicitud de reagrupación familiar que presenta el extranjero residente en la oficina
  de extranjería (LOEX arts. 16 a 19; Reglamento de 2024, arts. 65 a 71): familiares reagrupables,
  ascendientes a cargo, medios sobre el IPREM, vivienda adecuada con su informe, seguro, visado del
  familiar, reagrupación en cadena, residencia independiente y renovación. Si se deniega la
  autorización o el visado, redacta el recurso. Úsala con «reagrupar a mi mujer», «traer a mis
  padres», «reagrupación de mis hijos», «informe de vivienda», «me han denegado la reagrupación»,
  «residencia independiente tras el divorcio». Si el reagrupante es español o ciudadano de otro
  Estado de la Unión, usa `familiares-de-espanoles` o `ciudadanos-ue-y-familiares`; si es titular de
  una autorización de la Ley 14/2013, `movilidad-internacional-ley-14-2013`.
---

# Reagrupación familiar del extranjero residente

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Derecho a reagrupar, familiares y requisitos legales** → `buscar_articulo` (`ley="LOEX"`, artículos 16, 17, 18 y 19) y, si se pide minoración o se discute la regularidad de los recursos, `ley="Directiva 2003/86/CE"`, artículos 5 (interés del menor) y 7 (recursos fijos y regulares); `verificar_escrito` no identifica las directivas y atribuye su artículo a otra norma: si lo marca, es un falso positivo que se explica en el resumen.
- **Familiares, requisitos, procedimiento y visado** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 38, 40, 65, 66, 67, 68 y 196; el 176 si el reagrupante es residente de larga duración-UE).
- **Residencia independiente, reagrupación en cadena y renovación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 69, 70 y 71).
- **Vivienda adecuada** → `buscar_articulo` (`ley="Ley 12/2023"`, artículo 3) y, si el abogado aporta la referencia catastral o la dirección de la vivienda, `consultar_catastro` para superficie y uso.
- **Norma aplicable a solicitudes anteriores al 20/05/2025** → `leer_boe` (`identificador="BOE-A-2024-24099"`, disposición transitoria segunda del Real Decreto) y, si rige el reglamento anterior, `buscar_articulo` (`ley="Real Decreto 557/2011"`); también, para rebatir doctrina dictada con el reglamento anterior (por ejemplo, el pronóstico de mantenimiento de los medios), su artículo 54.
- **Recursos contra la denegación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículo 28; `ley="LOEX"`, artículo 27; `ley="LPAC"`, artículos 112, 121 a 124; `ley="LJCA"`, artículos 8, 10 y 46).
- **Doctrina sobre los motivos de denegación** → `buscar_sentencias` (`consulta="reagrupación familiar ascendientes a cargo necesidad"`, `consulta="reagrupación familiar medios económicos minoración interés superior del menor"` o `consulta="visado reagrupación familiar denegación matrimonio fraude"`, `jurisdiccion="CONTENCIOSO"`, `base="AN"`; y `base="TS"` con `consulta="reagrupación familiar ascendientes a cargo"`) + `leer_sentencias` (`parrafos=3`).
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

- Extranjero con residencia temporal o de larga duración en España que quiere traer a su cónyuge
  o pareja, hijos, representados legales, ascendientes o al hijo mayor cuidador (art. 66).
- Reagrupado que quiere reagrupar a su vez (art. 70).
- Titular de una autorización de familiar de persona con nacionalidad española que reagrupa a sus
  propios familiares: el art. 95.2 remite a los arts. 68 y 69 (léelo con `buscar_articulo`).
- Reagrupado que necesita una autorización independiente: medios propios, ruptura del vínculo,
  violencia, fallecimiento del reagrupante o mayoría de edad (art. 69).
- Renovación de la autorización del reagrupado (art. 71).
- Denegación de la autorización (oficina de extranjería) o del visado (oficina consular).

Usa otra skill cuando el reagrupante sea español (arts. 93 a 99 del Reglamento:
`familiares-de-espanoles`), ciudadano de otro Estado de la Unión (Real Decreto 240/2007:
`ciudadanos-ue-y-familiares`), titular de una autorización de la Ley 14/2013 (sus familiares siguen
el art. 62.4 de esa ley: `movilidad-internacional-ley-14-2013`) o beneficiario de protección
internacional (Ley 12/2009: `proteccion-internacional-apatridia`). Los familiares de un estudiante
siguen el art. 56 del Reglamento, que esta skill no cubre. La autorización por circunstancias
excepcionales de la víctima de violencia de género o sexual es otra figura
(`victimas-violencia-genero-sexual`); la residencia independiente del reagrupado víctima (art.
69.2.b) sí se prepara aquí.

## Datos que hay que reunir antes de redactar

Saca estos datos de la documentación aportada, por este orden (paso 2 de `redaccion-rapida`). Si falta un dato imprescindible (★) que bloquee el escrito, pídelos todos a la vez en una única ronda de no más de cuatro preguntas; lo demás queda como `[PENDIENTE: dato]`.

1. ★ Trámite: solicitud inicial, residencia independiente, renovación o recurso. Si es recurso:
   resolución íntegra, órgano (oficina de extranjería o consulado) y fecha de notificación.
2. ★ Reagrupante: clase de autorización, fecha de la primera concesión, si ha pedido u obtenido la
   renovación y cuándo, larga duración (nacional o UE, en España o en otro Estado miembro) y
   provincia de residencia. Si su residencia deriva de una reagrupación, cómo obtuvo la
   autorización independiente (art. 70).
3. ★ Familiar: parentesco exacto, edad en la fecha de la solicitud, estado civil y, según el caso:
   - cónyuge: matrimonios anteriores y cómo se disolvieron (art. 66.1.a);
   - pareja: inscripción en un registro de la Unión o prueba de doce meses de convivencia, o
     descendencia común (art. 66.1.b);
   - hijo de uno solo de los progenitores: patria potestad, custodia, consentimiento del otro
     progenitor o autorización judicial (art. 66.1.c);
   - ascendiente: edad, dependencia económica o física, envíos de dinero del último año y desde
     cuándo, ingresos y gastos propios, otros hijos en el país y qué aportan, enfermedades y quién le
     cuida (arts. 66.1.e y 196); para la presunción del art. 196.3.c), el producto interior bruto per
     cápita del país de procedencia publicado por el Banco Mundial, con el año del dato;
   - hijo mayor cuidador: grado de dependencia reconocido del reagrupante (art. 66.1.f).
4. ★ Recursos económicos de la unidad: ingresos del reagrupante, de su cónyuge o pareja y de los
   familiares en primer grado residentes que conviven con él, con su naturaleza y documentos;
   patrimonio de los últimos seis meses; cuántos miembros tendrá la unidad familiar (art. 67.1).
5. ★ Vivienda: título de ocupación, número de habitaciones y de ocupantes, si se ha pedido el
   informe autonómico o municipal, en qué fecha y si se ha emitido (art. 67.2).
6. ★ Seguro de enfermedad del reagrupante y de los familiares; hijos ya en España escolarizados;
   antecedentes penales del familiar; compromiso de no retorno (art. 67.3 a 67.6).
7. Para la residencia independiente: fecha de notificación de la admisión de la demanda de nulidad,
   divorcio o separación o de la cancelación de la pareja (art. 69.2.a), de notificación de la orden
   de protección o del informe (art. 69.2.b) o del fallecimiento (art. 69.2.c): los plazos de seis
   meses cuentan desde ellas.
8. Cifras vigentes del IPREM y, si se pide la minoración por menores, de la renta garantizada del
   ingreso mínimo vital, con la norma que las fija (ver apartado C). Con ascendientes, además, la
   cuantía anual de las pensiones no contributivas y si la unidad percibe el ingreso mínimo vital
   (art. 196.3.d).

## Requisitos y comprobaciones

### A. Norma aplicable y notas de nulidad

- Lee cada artículo con `buscar_articulo` y aplica sus notas de nulidad. A 27/09/2026 el conector
  devuelve anulado el inciso del art. 196.2.b) que exigía que la dependencia económica se
  produjera en el país de origen: la dependencia puede probarse aunque el ascendiente esté en
  España. Comprueba la nota al leer el artículo.
- Solicitudes anteriores al 20/05/2025: disposición transitoria segunda (`leer_boe`); si rige el
  reglamento anterior, pide sus artículos con `ley="Real Decreto 557/2011"`. Si `leer_boe` no la
  devuelve completa, aplica la puerta.

### B. Cuándo se puede pedir (art. 68.1; LOEX art. 18.1)

- Regla: el reagrupante ha residido al menos un año y ha solicitado la autorización para residir
  al menos otro año; la autorización del familiar no se concede hasta que se renueve la del
  reagrupante. Calcula las fechas con los datos del paso 2.
- Ascendientes: el reagrupante debe ser residente de larga duración o de larga duración-UE en
  España (LOEX art. 18.1; art. 68.1.a). La solicitud puede presentarse desde que pidió esa
  autorización, pero no se concede hasta obtenerla (último párrafo del art. 68.1). Si es larga
  duración-UE, lee además el art. 176, letras b) y c).
- Reagrupados que reagrupan: autorización de residencia y trabajo independiente; los ascendientes
  reagrupados, además, larga duración y solvencia salvo la excepción del art. 70.3.

### C. Medios económicos (art. 67.1; LOEX art. 18.2)

- Cuantía: el porcentaje del IPREM que fija el art. 67.1 para una unidad de dos miembros más el
  porcentaje por cada miembro adicional. Para hijos y representados (art. 66.1.c y d) cabe la
  minoración que regula el mismo artículo, con referencia a la renta garantizada del ingreso
  mínimo vital y atendiendo al interés superior del menor. Copia porcentajes y reglas del texto leído.
- Las cifras del IPREM y del ingreso mínimo vital las fijan normas presupuestarias que
  Jurisprudenciator no devuelve. Pide al abogado las cifras vigentes con su norma; no las pongas
  de memoria. Si no las facilita, usa marcadores, no afirmes que el requisito se cumple y dilo en
  el resumen.
- Aplica las reglas de cómputo de las letras a) a e): ingresos íntegros con pagas
  extraordinarias, rendimientos netos de actividades económicas, patrimonio estable como media de
  seis meses; se excluyen ayudas de estudio y vivienda, pensiones compensatorias y de alimentos
  (salvo a favor del reagrupado) y la asistencia social.
- Suman los ingresos del cónyuge o pareja y de los familiares en primer grado residentes que
  formen parte de la unidad de convivencia (último párrafo del art. 67.1).

### D. Vivienda adecuada (art. 67.2)

- Concepto: el del art. 3.c) de la Ley 12/2023, salvo que choque con la normativa de vivienda
  competente. Léelo con `buscar_articulo`.
- Prueba: informe de los servicios competentes de la comunidad autónoma o del ayuntamiento, que
  debe emitirse y notificarse en un mes. Si no se emite en plazo y se acredita, vale cualquier
  prueba admitida en Derecho. Antigüedad máxima de seis meses y contenido mínimo: título, número
  de habitaciones, uso de cada dependencia, número de ocupantes y condiciones de habitabilidad y
  equipamiento. El informe no vincula, pero apartarse de él exige motivación expresa.
- El título puede estar a nombre de cualquier miembro de la unidad familiar de convivencia.

### E. Resto de requisitos

- Seguro de enfermedad del reagrupante y de los familiares (art. 67.3). Si el familiar tiene un
  seguro privado, comprueba en el condicionado que no excluya enfermedades preexistentes: si la
  solicitud se apoya en esas enfermedades (ascendientes), una póliza que las excluye contradice el
  propio expediente; adviértelo en el resumen para que se cambie antes de presentar.
- Escolarización de los hijos ya residentes (art. 67.4); ausencia de compromiso de no retorno
  (art. 67.5); orden público: antecedentes en España e informe policial, sin denegación automática
  por antecedentes policiales (arts. 67.6 y 68.4); tasa (art. 67.7).
- Documentación de la solicitud: la del art. 68.3, incluida la declaración responsable de que no
  reside en España otro cónyuge o pareja.

### F. Procedimiento, visado y plazos

- Presenta el reagrupante, personalmente, ante la oficina de extranjería de su provincia
  (arts. 68.2 y 197). Resolución en dos meses; el silencio es desestimatorio (art. 68.6).
  Tramitación preferente (art. 68.7).
- Concedida la autorización, el familiar pide el visado en dos meses desde la notificación al
  reagrupante, con los documentos originales del vínculo (art. 40.1.a); el consulado resuelve en
  un mes (art. 40.3). La autorización no surte efectos hasta la entrada, en el plazo del
  art. 68.5.a). Vigencia: art. 68.9.
- El consulado puede denegar el visado aunque la autorización esté concedida por las causas del
  art. 28.5 (falta de requisitos, documentos falsos, fraude de ley, identidad o veracidad no
  acreditadas); la denegación del visado de reagrupación debe motivarse (art. 28.6; LOEX art. 27.6).

### G. Residencia independiente, cadena y renovación

- Art. 69: supuestos, plazos de seis meses para pedirla y duración de cada autorización
  independiente. Léelo entero y encaja el caso en un apartado concreto.
- Renovación (art. 71): dos meses antes o tres meses después de la caducidad; mantenimiento del
  vínculo; se valoran condenas; escolarización; esfuerzo de integración. Silencio estimatorio a
  los tres meses (art. 71.5); duración de cuatro años condicionada a la del reagrupante (art. 71.6).

### H. Recursos

- Toma el recurso del pie de la resolución y compruébalo con la LPAC (reposición en un mes,
  arts. 123 y 124; alzada, arts. 121 y 122) o con la LJCA (dos meses, art. 46). Qué actos agotan la
  vía administrativa lo dice una disposición adicional del Reglamento que el conector no
  devuelve: si el pie falta o es contradictorio, aplica la puerta.
- Órgano judicial: contra la oficina de extranjería, LJCA art. 8.4 y la organización judicial del
  apartado 3 del formato; contra el consulado, determínalo con la LJCA y jurisprudencia de
  competencia antes de encabezar.

## Estrategia y jurisprudencia

1. Diagnostica primero el momento (art. 68.1) y el parentesco (art. 66): son causas de denegación
   que no se subsanan con prueba. Si no se cumplen, dilo antes de redactar.
2. Medios: si la unidad está cerca del umbral, documenta la regularidad (contratos, nóminas de seis
   meses, rendimientos netos) y, con menores, pide expresamente la minoración razonando el
   interés superior del menor con los factores del art. 67.1.
3. Ascendientes: prueba los tres elementos por separado (edad o razón humanitaria del art. 196.6;
   dependencia real, estable y previa del art. 196.1 a 196.4 o presunción del art. 196.3.c o del
   art. 196.5; y necesidad de residir en España). La jurisprudencia deniega cuando falta uno solo:
   no bastan las remesas; acredita los ingresos y gastos del ascendiente y qué aportan los demás
   hijos. El art. 196.3.d) exige además que la unidad de quien se hace cargo no perciba el ingreso
   mínimo vital y supere el porcentaje de las pensiones no contributivas que fija; sin esa cifra ni
   la del Banco Mundial, usa marcadores y no afirmes que se cumplen.
4. Visado denegado tras concederse la autorización: el debate suele ser el fraude (matrimonio sin
   convivencia, entrevista) o la veracidad del vínculo. Busca `consulta="denegación visado
   reagrupación familiar potestad oficina consular"` con `base="TS"` y `base="AN"`, y exige en el
   recurso los hechos concretos en que se apoyó el consulado (art. 28.6).
5. Muchas sentencias aplican todavía el Real Decreto 557/2011. Antes de usar su doctrina,
   comprueba que el requisito que interpretan existe igual en el texto vigente; si una sentencia
   exige algo que no aparece en el art. 67 leído (por ejemplo, un pronóstico de mantenimiento de
   los ingresos), no lo presentes como requisito vigente; si la oficina o la jurisprudencia lo
   aplican, contrasta con el art. 54 del Real Decreto 557/2011 leído y argumenta que el art. 67.1
   vigente solo manda valorar la naturaleza y regularidad de los recursos.
6. Lee con `leer_sentencias` (`parrafos=3`, `terminos` con el motivo) solo lo que vayas a citar y
   cita fundamentos, nunca los hechos ni los datos de aquellas familias.

## Documento que se entrega

Formato, destinatario, citas y datos según `references/formato-y-organos.md`. El impreso oficial
y la tasa se obtienen en la sede oficial: no indiques modelos, códigos ni importes.

1. **Solicitud inicial** — `solicitud-reagrupacion-familiar-<apellido-reagrupante>-<AAAAMMDD>.docx`,
   dirigida a la OFICINA DE EXTRANJERÍA DE [PROVINCIA]:
   - comparecencia del reagrupante y datos del familiar;
   - EXPONE: situación de residencia del reagrupante y fechas (art. 68.1); vínculo y encaje en la
     letra del art. 66.1; unidad familiar y tabla de recursos con el cálculo; vivienda (informe o
     prueba sustitutiva y, si se consultó, datos catastrales); seguro; escolarización; ausencia de
     antecedentes y de compromiso de no retorno;
   - FUNDAMENTOS DE DERECHO: LOEX arts. 16 a 18 y Reglamento arts. 66 a 68 (y 196 si hay
     ascendientes), con su texto vigente;
   - SOLICITA la concesión y, si procede, la minoración de medios;
   - declaración responsable del art. 68.3.a).4.º y relación numerada de documentos.
2. **Recurso** — `recurso-reposicion-reagrupacion-<apellido>-<AAAAMMDD>.docx`, o
   `recurso-visado-reagrupacion-<apellido>-<AAAAMMDD>.docx` si se deniega el visado, dirigido al
   órgano que indique el pie de recursos: acto recurrido y fecha de notificación; hechos; un
   fundamento por cada motivo de denegación, con el requisito leído, la doctrina literal y el
   documento que lo prueba; SOLICITA; otrosí con la prueba nueva.
3. **Residencia independiente o renovación** — `residencia-independiente-<apellido>-<AAAAMMDD>.docx`
   o `renovacion-reagrupacion-<apellido>-<AAAAMMDD>.docx`, con el supuesto del art. 69 o los
   requisitos del art. 71 como hechos numerados.

**Reparto para la redacción rápida:** solicitud inicial: 01 comparecencia y hechos (con la tabla de recursos y el cálculo, que el director deja cerrados en `caso.md`); 02 fundamentos: familiar reagrupable, unidad familiar y recursos; 03 vivienda, seguro, escolarización, declaración responsable, solicita y documentos. Recurso: una sección por motivo de denegación, más encabezamiento y cierre. Residencia independiente o renovación (dos o tres páginas): tres secciones o, si son más breves, el director sin equipo.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación, con su vigencia y
      sus notas de nulidad; la norma aplicable por fecha está justificada.
- [ ] Momento de la solicitud (art. 68.1) y parentesco (art. 66) comprobados antes de redactar.
- [ ] Cálculo de medios con porcentajes leídos y cifras facilitadas por el abogado con su norma, o
      con marcadores y aviso.
- [ ] Cada ECLI se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; ningún hecho ni
      dato personal de otros pleitos.
- [ ] `verificar_escrito` pasado por cada redactor sobre sus frases con normas y sus avisos corregidos.
- [ ] Marcadores en los datos no facilitados; nada inventado.
- [ ] Plazos con fecha inicial, precepto y fecha final: visado (art. 40.1.a), recurso o
      residencia independiente (art. 69).
- [ ] Resumen para el abogado según el apartado 7 del formato, con los riesgos (medios, vivienda,
      dependencia, fraude) y el próximo paso (informe de vivienda, visado).
