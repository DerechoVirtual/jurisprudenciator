---
name: nacionalidad-otras-vias
description: >-
  Estudia y redacta en Word los escritos de nacionalidad española distintos de la residencia -
  nacionalidad de origen (art. 17 CC), adopción, opción (art. 20), carta de naturaleza (art. 21),
  consolidación y declaración con valor de simple presunción (art. 18), conservación, pérdida, nulidad
  y recuperación (arts. 24-26), y los recursos ante la Dirección General y la oposición judicial.
  Úsala cuando el abogado diga «optar a la nacionalidad», «hijo de español», «nieto de español», «Ley
  de Memoria Democrática», «ley de nietos», «carta de naturaleza», «recuperar la nacionalidad», «he
  perdido la nacionalidad», «consolidación por posesión de estado», «nacido en España de padres
  apátridas» o «el Registro Civil me deniega la inscripción». La Ley 20/2022 solo se trabaja con la
  puerta de su disposición adicional. Para residencia usa nacionalidad-residencia.
---

# Nacionalidad española: origen, opción, carta de naturaleza, consolidación, conservación y recuperación

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Vía de adquisición o conservación aplicable, requisitos y plazos de caducidad** → `buscar_articulo` (`ley="CC"`, artículos `"17"`, `"18"`, `"19"`, `"20"`, `"21"`, `"23"`, `"24"`, `"25"` y `"26"`).
- **Inscripción, declaraciones de voluntad, presunción de nacionalidad y expediente con valor de simple presunción** → `buscar_articulo` (`ley="Ley 20/2011"`, artículos `"10"`, `"68"`, `"69"`, `"92"`, `"93"` y `"98"`).
- **Recurso contra la decisión del Encargado del Registro Civil y vía judicial** → `buscar_articulo` (`ley="Ley 20/2011"`, artículos `"85"`, `"86"`, `"87"` y `"88"`; `ley="LEC"`, artículos `"781 bis"` y `"753"`; `ley="LOPJ"`, `articulo="84"`).
- **Ley 20/2022 de Memoria Democrática** → `leer_boe` (`identificador="BOE-A-2022-17099"`) solo para leer el preámbulo, `leer_boe` (`identificador="BOE-A-2022-17470"`) para el criterio administrativo de la instrucción de 2022, `buscar_boe` (`consulta="prórroga opción nacionalidad Memoria Democrática"`) para localizar cualquier acuerdo o norma que haya prorrogado o modificado el plazo, y `buscar_sentencias` (`consulta="disposición adicional octava Ley 20/2022 nacionalidad"`, `base="TS"`, `fecha_desde` del último año) para conocer litigios en curso.
- **Doctrina sobre la vía concreta** → `buscar_sentencias` (por ejemplo `consulta="consolidación nacionalidad artículo 18 posesión utilización continuada buena fe título inscrito"`, `base="TS"`, `jurisdiccion="CIVIL"`; o `consulta="nacionalidad española de origen artículo 17.1.c apatridia"`, `base="TS"`) y `leer_sentencias` (`parrafos=3`).
- **Carta de naturaleza y dispensas ministeriales: órgano judicial** → `buscar_articulo` (`ley="LJCA"`, artículos `"11"`, `"12"` y `"46"`) y `buscar_sentencias` (`consulta="carta de naturaleza denegación"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Decidir por qué vía puede ser español el cliente (origen, adopción, opción, carta de naturaleza, consolidación, recuperación) y preparar el escrito ante el Registro Civil.
- Preparar la declaración de conservación para evitar la pérdida, o la defensa frente a una pérdida o una acción de nulidad.
- Recurrir ante la Dirección General la decisión del Encargado del Registro Civil y preparar la oposición judicial posterior.
- Solicitar la carta de naturaleza o la dispensa ministerial de residencia en la recuperación.
- Detectar que el caso depende de la Ley 20/2022 y explicar al abogado qué se puede y qué no se puede hacer con esta skill.

Usa otra skill del plugin cuando:

- la vía sea la residencia, incluido el plazo de un año del nacido fuera de España de padre, madre, abuelo o abuela originariamente españoles (`CC`, art. 22.2.f) → `nacionalidad-residencia`;
- se pida el estatuto de apátrida, que es un procedimiento distinto de la nacionalidad de origen del art. 17.1.c), aunque a veces conviene plantear ambos → `proteccion-internacional-apatridia`;
- el cliente, mientras tanto, necesite residir en España como familiar de español → `familiares-de-espanoles`; o buscar empleo como hijo o nieto de español de origen → `estudiantes-y-busqueda-empleo`.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. Si falta un dato imprescindible, pregunta y espera.

1. **Objetivo** (imprescindible): adquirir, conservar, recuperar o defender la nacionalidad; o recurrir una decisión concreta.
2. **Árbol familiar documentado** (imprescindible en origen, opción y recuperación): lugar y fecha de nacimiento del interesado, de sus progenitores y, si importa, de sus abuelos; nacionalidad de cada uno en cada fecha; si alguno fue español de origen y nacido en España.
3. **Fechas clave** (imprescindible): fecha de nacimiento, mayoría de edad o emancipación del interesado y edad de la emancipación según su ley personal (de ella depende la prórroga del art. 20.2.c; el Derecho extranjero no se comprueba con Jurisprudenciator: pide al abogado que lo acredite), fecha en que el progenitor adquirió la nacionalidad (la de la inscripción, que es constitutiva: `Ley 20/2011`, art. 68.1), fecha de determinación de la filiación o de la adopción, fecha de adquisición de otra nacionalidad.
4. **Situación registral**: inscripción de nacimiento en el Registro Civil español (necesaria antes de inscribir la nacionalidad, `Ley 20/2011`, art. 68.1), título inscrito, documentos españoles usados (DNI, pasaporte, censo).
5. **Residencia**: residencia legal en España o condición de emigrante o hijo de emigrante (recuperación).
6. **Resolución impugnada** (imprescindible para recursos): texto, órgano (Encargado, Dirección General, Ministerio, Consejo de Ministros), fecha de notificación y pie de recursos.
7. **Ley 20/2022**: si el cliente pretende acogerse a ella, anota el supuesto que alega y la fecha en que presentó o pretende presentar la solicitud.

## Requisitos y comprobaciones

Lee cada artículo en el momento con `buscar_articulo` y cita el texto vigente.

**Mapa de vías** (verificado; confirma cada fila con el texto vigente antes de usarla):

| Vía | Precepto | Plazo o límite | Ante quién | Si se deniega |
|---|---|---|---|---|
| Origen (filiación o nacimiento) | `CC`, art. 17.1 | Ninguno | Registro Civil (inscripción o expediente de simple presunción) | Recurso a la Dirección General y oposición civil |
| Opción de origen por determinación tardía | `CC`, arts. 17.2 y 20.1.c) | Dos años desde la determinación | Encargado, notario o cónsul | Ídem |
| Adopción de mayor de edad | `CC`, arts. 19.2 y 20.1.c) | Dos años desde la adopción | Ídem | Ídem |
| Opción por patria potestad | `CC`, art. 20.1.a) | Caduca a los veinte años (art. 20.2.c) | Ídem | Ídem |
| Opción del hijo de español de origen nacido en España | `CC`, art. 20.1.b) | Sin límite de edad (art. 20.3) | Ídem | Ídem |
| Consolidación | `CC`, art. 18 | Diez años de posesión | Registro Civil o jurisdicción civil | Ídem |
| Conservación | `CC`, art. 24.1 y 24.3 | Tres años | Encargado, notario o cónsul (`Ley 20/2011`, art. 68.3) | Ídem |
| Recuperación | `CC`, art. 26 | Ninguno | Encargado; dispensa del Ministro | Ídem; la dispensa, contencioso |
| Carta de naturaleza | `CC`, art. 21.1 | Caduca a los 180 días de la notificación sin art. 23 | Ministerio; Real Decreto | Contencioso (órgano según quién firme) |

**Nacionalidad de origen (`CC`, art. 17).**
- Supuestos del art. 17.1: hijo de padre o madre españoles; nacido en España de padres extranjeros si uno nació en España (salvo hijos de diplomáticos acreditados); nacido en España de padres apátridas o cuya ley no le atribuye nacionalidad; nacido en España con filiación no determinada (y presunción de los menores cuyo primer lugar conocido de estancia es España).
- Determinación de la filiación o del nacimiento en España después de los dieciocho años: no da la nacionalidad por sí sola; abre la opción de origen en dos años desde la determinación (art. 17.2).
- Para el art. 17.1.c), prueba qué atribuye la ley nacional de cada progenitor; busca jurisprudencia del país concreto (`consulta="nacionalidad de origen artículo 17.1.c <país> ley no atribuye nacionalidad"`). Para personas nacidas en el Sáhara Occidental antes de la descolonización existe doctrina civil del Supremo contraria a su consideración como españoles de origen por el art. 17: búscala y léela antes de plantear esa vía.
- Presunción legal: se presumen españoles los nacidos en España de progenitores también nacidos en España, mientras no conste la extranjería de estos (`Ley 20/2011`, art. 69).

**Adopción (`CC`, art. 19).** El menor adoptado por español adquiere la nacionalidad de origen desde la adopción; el adoptado mayor de dieciocho años puede optar en dos años desde la constitución.

**Opción (`CC`, art. 20).**
- Supuestos: sujetos a la patria potestad de un español; hijos de padre o madre originariamente español y nacido en España; supuestos de los arts. 17.2 y 19.2.
- Forma según edad y capacidad (art. 20.2): representante legal del menor de catorce años, mayor de catorce asistido, interesado mayor de edad o emancipado, persona con discapacidad con apoyos.
- Caducidad: la opción caduca a los veinte años de edad, con la prórroga de dos años desde la emancipación si la ley personal la retrasa (art. 20.2.c) y el plazo especial tras extinguirse medidas de apoyo (art. 20.2.e). El supuesto del art. 20.1.b) no tiene límite de edad (art. 20.3). Calcula la fecha exacta de caducidad (el vigésimo cumpleaños, o dos años desde la emancipación) y ponla en el resumen con una fecha límite prudente: el día anterior. Si el plazo es corto, advierte de que la declaración puede hacerse ante notario (`Ley 20/2011`, art. 68.3) cuando el Registro no dé cita a tiempo.
- Causa típica de denegación: la patria potestad del español ya se había extinguido cuando el progenitor adquirió la nacionalidad, o se optó fuera del plazo. Si la opción caducó, valora la residencia de un año (`CC`, art. 22.2.b) y remite a `nacionalidad-residencia`.

**Carta de naturaleza (`CC`, art. 21.1).** Discrecional, mediante Real Decreto, cuando concurren circunstancias excepcionales. La solicitud debe describir y documentar esas circunstancias. Caduca a los ciento ochenta días de la notificación si no se cumple el art. 23 (art. 21.4). Para el recurso, identifica quién firma la denegación: si es el Consejo de Ministros, `LJCA`, art. 12.1.a); si es un Ministro, `LJCA`, art. 11.1.a); confírmalo con jurisprudencia y explica al abogado el control limitado de las decisiones discrecionales.

**Consolidación y simple presunción (`CC`, art. 18; `Ley 20/2011`, arts. 92 y 93).**
- Consolidación: posesión y utilización continuada de la nacionalidad durante diez años, con buena fe y basada en un título inscrito en el Registro Civil, aunque después se anule el título.
- Vía registral: expediente de declaración de la nacionalidad con valor de simple presunción (art. 92.1.b); es una presunción iuris tantum y se anota (art. 93).
- Vía judicial: acción declarativa ante la jurisdicción civil. Antes de elegirla, busca jurisprudencia civil sobre el procedimiento y la prueba de la posesión de estado (DNI, pasaporte, censo, servicio militar, actuaciones como español).

**Requisitos comunes (`CC`, art. 23).** Jura o promesa, renuncia a la nacionalidad anterior salvo naturales de los países del art. 24.1 y sefardíes originarios de España, e inscripción. La inscripción de la adquisición por opción, carta de naturaleza o residencia, y la recuperación, son constitutivas; la de la pérdida es declarativa (`Ley 20/2011`, art. 68.1). Las declaraciones pueden hacerse ante Encargado, notario o funcionario consular (art. 68.3).

**Conservación y pérdida (`CC`, arts. 24 y 25).**
- Pérdida del art. 24.1 (emancipados residentes en el extranjero que adquieren voluntariamente otra nacionalidad o usan exclusivamente la anterior): se produce a los tres años y se evita declarando la voluntad de conservar ante el Encargado. La adquisición de la nacionalidad de los países que enumera el propio apartado no basta para perder la de origen.
- Art. 24.3: nacidos y residentes en el extranjero, hijos de españoles también nacidos fuera, a quienes el país de residencia atribuye su nacionalidad: pierden la española si no declaran conservarla en tres años desde la mayoría de edad o emancipación. Calcula la fecha límite.
- Renuncia expresa (art. 24.2) y excepción en caso de guerra (art. 24.4).
- Españoles no de origen (art. 25.1): uso exclusivo durante tres años de la nacionalidad renunciada, o servicio de armas o cargo político extranjero contra prohibición expresa.
- Nulidad por falsedad, ocultación o fraude declarada por sentencia firme; la acción la ejerce el Ministerio Fiscal en quince años (art. 25.2).
- El Convenio de nacionalidad con Francia modifica el régimen para sus nacionales: `buscar_articulo` devuelve la nota; si el cliente es francés, léelo con `leer_boe` antes de concluir.

**Recuperación (`CC`, art. 26).** Residencia legal en España (no exigida a emigrantes ni a hijos de emigrantes; dispensable por el Ministro por circunstancias excepcionales), declaración ante el Encargado e inscripción. Quien está en un supuesto del art. 25 necesita habilitación previa del Gobierno (art. 26.2). El régimen del silencio en la dispensa está en una disposición adicional que el conector no devuelve: si el asunto depende de él, aplica la puerta.

**Recursos (`Ley 20/2011`; `LEC`).**
- Contra decisiones de los Encargados (Oficina Central, Generales y Consulares): recurso ante la Dirección General de Seguridad Jurídica y Fe Pública en un mes (art. 85.1), presentado conforme a la LPAC (art. 86.1). Si no resuelve en seis meses, se entiende desestimado y queda abierta la vía judicial (art. 86.2). En los procedimientos registrales el silencio es negativo (art. 88.2).
- Contra resoluciones de la Dirección General: oposición ante el órgano civil de la capital de provincia del domicilio del recurrente (art. 87.1), en dos meses desde la notificación y sin reclamación previa (`LEC`, art. 781 bis.1); escrito inicial sucinto, reclamación del expediente y demanda en veinte días, por los trámites del juicio verbal (arts. 781 bis y 753). La ley habla de «Juzgado de Primera Instancia»: comprueba con `LOPJ`, art. 84, la sección del Tribunal de Instancia que lo sustituye y encabeza con ella.
- Excepción: lo relativo a la nacionalidad por residencia va a la jurisdicción contencioso-administrativa (art. 87.2).

**Ley 20/2022 de Memoria Democrática: puerta específica.**
- La opción de los nacidos fuera de España de progenitores o abuelos exiliados, de hijos de españolas que perdieron la nacionalidad por matrimonio antes de 1978 y de hijos mayores de edad de quienes la obtuvieron por esa vía está en su **disposición adicional octava**, que Jurisprudenciator **no devuelve** (tampoco devuelve la disposición adicional séptima de la Ley 52/2007). El preámbulo, que sí se obtiene con `leer_boe`, solo describe su alcance. La Instrucción de 25 de octubre de 2022 de la Dirección General de Seguridad Jurídica y Fe Pública se lee con `leer_boe` (`identificador="BOE-A-2022-17470"`): es un criterio administrativo, no la ley, y su interpretación está discutida ante el Tribunal Supremo (comprueba el estado con la búsqueda de la lista y describe con exactitud el objeto del recurso y si la resolución es cautelar o definitiva); úsala solo para explicar al abogado cómo la aplica la Administración, nunca como sustituto del texto de la disposición adicional. Tampoco la uses para decir si el plazo sigue abierto: el plazo lo fija la disposición adicional y, en su caso, el acuerdo o la norma que lo haya modificado.
- Si el derecho del cliente depende de esa disposición (requisitos, plazo para optar, documentos, efectos), **detén la tarea en ese punto**: di al abogado que falta el texto de la disposición adicional octava de la Ley 20/2022 y cualquier norma o acuerdo que haya modificado su plazo, y que sin ellos no se redacta ni se calcula nada. No afirmes si el plazo está abierto o cerrado. Antes de detenerte, pide la disposición adicional con `buscar_articulo` (`ley="Ley 20/2022"`) y busca el acuerdo de prórroga con `buscar_boe`: si nada de ello aparece, la puerta se aplica. En ese caso no entregues Word: entrega solo el resumen para el abogado con qué precepto falta, qué sí se ha comprobado (preámbulo, criterio de la Instrucción, litigio) y el cuadro de vías alternativas.
- Sí puedes: identificar que el caso encaja en el ámbito descrito en el preámbulo, buscar y resumir jurisprudencia reciente (hay litigio en el Tribunal Supremo sobre la instrucción de aplicación de 2022; comprueba su estado con la consulta de la lista) y trabajar las vías alternativas que no dependen de ella (opción del art. 20.1.b, residencia de un año del art. 22.2.f).

## Estrategia y jurisprudencia

1. **Ordena las vías de más a menos fuerte.** Origen (declarativa, efectos desde el nacimiento) > opción de origen > opción simple > recuperación > residencia de un año > carta de naturaleza. Presenta al abogado un cuadro: vía, requisito que falta o se cumple, plazo de caducidad con fecha, prueba necesaria.
2. **Prueba documental.** Cada eslabón del árbol familiar necesita certificado (nacimiento, matrimonio, nacionalidad del progenitor en la fecha relevante). Señala los que faltan con marcadores.
3. **Jurisprudencia.** Busca por la vía y el hecho decisivo: `"opción nacionalidad patria potestad español extinguida"`, `"caducidad opción nacionalidad veinte años"`, `"consolidación nacionalidad posesión de estado DNI buena fe"`, `"recuperación nacionalidad emigrante hijo de emigrante"`, `"pérdida nacionalidad artículo 24 declaración de conservación"`. Usa `base="TS"` (Salas de lo Civil y de lo Contencioso, según la vía) y `base="AN"` para audiencias provinciales y tribunales superiores (en esta base, con `jurisdiccion="CIVIL"` para la vía registral). Lee con `parrafos=3`. En las vías registrales (opción, conservación, recuperación) apenas hay jurisprudencia: los asuntos se resuelven en el Registro y ante la Dirección General. Si el caso no depende de una cuestión controvertida (los requisitos son objetivos y constan en documentos: edad, fechas, filiación, patria potestad), la jurisprudencia no es imprescindible: tras la búsqueda y dos reformulaciones sin resultado, redacta con la ley y dilo en el resumen. Aplica la puerta solo si el caso depende de una cuestión discutida que la ley no resuelve (por ejemplo, la eficacia de un título, la posesión de estado o el alcance de una causa de pérdida).
4. **Resoluciones de la Dirección General.** Jurisprudenciator no las devuelve como jurisprudencia: no las cites si el abogado no aporta su texto; apóyate en sentencias.
5. **Cómo usar la doctrina:** premisa normativa con texto vigente, párrafo literal del fundamento con órgano, fecha y ECLI tal como los devolvió `leer_sentencias`, aplicación a los hechos del cliente y conclusión. Nunca el relato de hechos ni datos de las partes de aquel pleito.

## Documento que se entrega

Formato, citas y datos: `references/formato-y-organos.md`. Entrega en Word el escrito que el caso requiera:

**A. Escrito ante el Registro Civil** (`declaracion-opcion-<apellido>-<AAAAMMDD>.docx`; o `declaracion-conservacion-`, `solicitud-recuperacion-`, `expediente-simple-presuncion-` según el caso).
1. Encabezamiento: Encargado de la Oficina del Registro Civil competente (general del domicilio o consular), o notario si la declaración se hace ante él.
2. Comparecencia: `[NOMBRE Y APELLIDOS]`, `[PASAPORTE]`, `[DOMICILIO]`, representación legal o apoyos si procede.
3. Hechos numerados: árbol familiar con fechas y documentos.
4. Fundamentos: precepto de la vía, cumplimiento de cada requisito y del plazo con su fecha, inscripción previa del nacimiento si falta (`Ley 20/2011`, art. 68.1, con la certificación extranjera como título conforme al art. 98.1) y doctrina aplicable cuando la haya.
5. Declaraciones del art. 23 cuando procedan (jura o promesa, renuncia o su excepción) y petición de inscripción.
6. SOLICITA y relación numerada de documentos.

**B. Recurso ante la Dirección General** (`recurso-dgsjfp-nacionalidad-<apellido>-<AAAAMMDD>.docx`): encabezamiento a la Dirección General de Seguridad Jurídica y Fe Pública; decisión recurrida y fecha de notificación; hechos; fundamentos (procedencia y plazo del art. 85, fondo con doctrina); SOLICITA; documentos.

**C. Escrito inicial de oposición judicial** (`oposicion-781bis-<apellido>-<AAAAMMDD>.docx`): encabezamiento a la sección del Tribunal de Instancia comprobada; comparecencia con representación; resolución a la que se opone y pretensión sucinta (`LEC`, art. 781 bis.2); petición de que se reclame el expediente. Si el abogado lo pide, añade el esquema de la demanda de juicio verbal.

**D. Solicitud de carta de naturaleza** (`solicitud-carta-naturaleza-<apellido>-<AAAAMMDD>.docx`): memoria de las circunstancias excepcionales con prueba de cada una. Modelo, tasa y sede se comprueban en la sede oficial: no des importes ni códigos.

## Comprobación final

- [ ] `estado` respondió y la puerta se cumplió en todo el trabajo.
- [ ] Cada artículo citado se leyó en esta conversación con `buscar_articulo` (incluidas las notas de vigencia que devuelve).
- [ ] Si el caso dependía de la disposición adicional octava de la Ley 20/2022 u otra disposición que el conector no devuelve, la tarea se detuvo en ese punto y se explicó al abogado qué precepto falta.
- [ ] Fechas de caducidad de la opción y de la conservación calculadas con su precepto.
- [ ] Órgano de destino y vía (registral, civil o contencioso-administrativa) comprobados con la Ley 20/2011, la LEC, la LOPJ o la LJCA.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; solo fundamentos jurídicos.
- [ ] `verificar_escrito` pasado sobre el texto completo y corregidos los avisos. No identifica las citas con letra («artículo 20.1.b)», «artículo 11.1.a)») y las marca como no localizadas: compruébalas con `buscar_articulo` y no las cambies por ese aviso.
- [ ] Marcadores entre corchetes para todo dato no facilitado; ningún dato inventado.
- [ ] Plazo con fecha inicial, precepto y fecha final; sin fecha de notificación, no se da plazo.
- [ ] Resumen para el abogado según el apartado 7 del formato, con el cuadro de vías, la tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene) y el próximo paso.
