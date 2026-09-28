---
name: verificacion-partes-contrato
description: >-
  Comprueba quién firma un contrato antes de redactarlo, revisarlo o firmarlo y entrega un informe de
  verificación en Word con semáforo por parte. Sociedades: existencia y estado en el BORME, órgano de
  administración, cargos vigentes o caducados, apoderados, disolución, liquidación y concurso.
  Personas físicas: capacidad y medidas de apoyo tras la Ley 8/2021, régimen económico matrimonial y
  vivienda familiar (art. 1320 CC). Conflictos: autocontratación y transacciones del administrador
  (arts. 229-230 LSC) y activos esenciales (art. 160.f LSC). Inmuebles: Catastro y nota simple. Úsala
  con «comprueba la sociedad», «quién puede firmar», «tiene poderes», «está en concurso», «vende la
  vivienda familiar», «firma el administrador consigo mismo». Para analizar el clausulado, usa
  revision-contrato-semaforo; para redactar, la skill de ese contrato.
---

# Verificación de las partes y de quién firma

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Existencia, estado, cargos, apoderados y últimos actos de cada sociedad** → `buscar_empresa_mercantil` (denominación exacta o CIF; si devuelve varias sociedades, repite con el CIF).
- **Órgano de administración y poder de representación** → `buscar_articulo` (`ley="LSC"`, artículos `"210"`, `"214"`, `"221"`, `"222"`, `"233"`, `"234"` y `"249"`; `ley="CCom"`, `articulo="21"`); **apoderados** → (`ley="CC"`, artículos `"1259"`, `"1713"`, `"1727"`, `"1732"` y `"1738"`).
- **Conflicto de interés, autocontratación y activos esenciales** → `buscar_articulo` (`ley="LSC"`, artículos `"160"`, `"162"`, `"190"`, `"229"`, `"230"` y `"231"`).
- **Disolución, liquidación y concurso** → `buscar_articulo` (`ley="LSC"`, artículos `"363"`, `"371"` y `"379"`; `ley="TRLC"`, artículos `"106"`, `"109"`, `"156"`, `"226"` y `"227"`; si el concurso está en fase de liquidación, `"413"`, `"415"`, `"421"` y `"422"`).
- **Personas físicas: capacidad, apoyos y régimen matrimonial** → `buscar_articulo` (`ley="CC"`, artículos `"250"`, `"287"`, `"1263"`, `"1301"`, `"1302"`, `"1320"`, `"1322"`, `"1375"`, `"1377"` y `"1459"`; si hay separación o divorcio, `"96"` (uso atribuido), `"1392"` (conclusión de los gananciales) y `"397"` (cosa común)); extranjero que contrata en España → (`ley="32008R0593"`, `articulo="13"`).
- **Doctrina sobre activos esenciales, conflicto de interés, autocontratación, vivienda familiar y apoyos** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`, consultas de «Régimen jurídico y comprobaciones») + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Inmuebles** → `consultar_catastro` (referencia catastral, o dirección y municipio) y `buscar_articulo` (`ley="BOE-A-1946-2453"`, `articulo="34"`).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Antes de firmar o redactar cualquier contrato en el que intervenga una sociedad, un apoderado, un liquidador o administrador concursal, una persona con medidas de apoyo, un menor, o una persona casada que dispone de un inmueble.
- Al revisar un contrato ajeno, para comprobar a la contraparte y a quien firma por ella.
- Cuando la misma persona está en los dos lados (administrador de las dos sociedades, administrador que contrata con su sociedad, apoderado que se vende a sí mismo) o la operación es de gran tamaño para la sociedad.
- No es una auditoría legal completa de una empresa: para la compraventa de una sociedad, `compraventa-participaciones`. El clausulado se revisa en `revision-contrato-semaforo`; aquí solo se verifica quién contrata y con qué facultades.
- Busca siempre por la sociedad (denominación o CIF), nunca a un particular por su nombre o DNI.

## Datos que hay que reunir antes de redactar

Pregunta por cada parte, en este orden. Si falta un dato imprescindible (★), pídelo.

1. ★ Posición del cliente en el contrato y qué parte hay que verificar (la contraria, la propia o las dos).
2. ★ Sociedades: denominación exacta y CIF; quién firmará y en qué concepto (administrador único, solidario, mancomunado, consejero delegado, apoderado, liquidador).
3. ★ Si firma un apoderado: copia de la escritura de poder (notario, fecha y número de protocolo) y facultades concretas para este acto; si hay sospecha de revocación, fecha de la copia.
4. ★ Operación: objeto, precio y, si la sociedad adquiere, enajena o aporta un bien, su valor y el total de activos del último balance aprobado.
5. ★ Relación entre las partes: si alguien es administrador, socio o familiar de la otra parte, o administrador de las dos sociedades.
6. ★ Personas físicas: mayor o menor de edad; si tiene medidas de apoyo (escritura de medidas voluntarias, resolución judicial de curatela o defensor judicial) y su alcance; estado civil, régimen económico matrimonial (capitulaciones, vecindad civil) y si el inmueble es la vivienda habitual de la familia.
7. ★ Inmueble: referencia catastral o dirección y municipio; nota simple del Registro de la Propiedad de fecha próxima a la firma.
8. Nacionalidad y residencia de las personas físicas extranjeras.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo en el informe. La ley de sociedades se cita como «artículo N de la Ley de Sociedades de Capital» y la concursal como «artículo N del texto refundido de la Ley Concursal» o «del Real Decreto Legislativo 1/2020»: son formas que reconoce `verificar_escrito`. Las letras, delante: «letra f) del artículo 160 de la Ley de Sociedades de Capital».

### A. Sociedades

1. **Existencia y estado.** Lanza `buscar_empresa_mercantil` y anota: denominación, CIF, forma, estado, número de actos y fecha del último, cargos vigentes con su fecha «desde» y los últimos actos. Lee cada acto de «Disolución», «Liquidador», «Extinción», «Situación concursal», «Revocaciones» y «Ceses/Dimisiones».
   - La etiqueta «Activa» sale de un índice del BORME sin fe pública que puede no recoger los actos recientes: en las pruebas, una sociedad declarada en concurso figuraba «Activa» y sin ningún acto posterior. La herramienta muestra solo los doce últimos actos. Si el último acto es antiguo, si hay más actos de los mostrados o si hay indicios de crisis, pide nota simple del Registro Mercantil y la consulta del Registro Público Concursal. El conector no las sustituye.
   - «No encuentro ninguna sociedad» puede significar denominación distinta, sociedad reciente o que no es mercantil: pide el CIF y la escritura de constitución; nunca des la sociedad por inexistente solo por ese resultado. Si responde «Varias sociedades coinciden», repite con el CIF de la que interesa y no mezcles datos de dos sociedades.
   - **Cómo leer la respuesta** (formato comprobado en las pruebas):
     - «Cargos vigentes» mezcla cargos con poder de representación (Adm. Único, Adm. Solidario, Adm. Mancomunado, Consejero, Consejero Delegado o «Con.Delegado», Presidente, Liquidador) con cargos que no representan (Auditor, Secretario no consejero). Solo los primeros sirven para firmar.
     - Apoderados: «Apoderado» o «Apo.Sol.» actúa solo; «Apo.Manc.» actúa con otro apoderado mancomunado; «Apo.Man.Soli» combina ambos según el poder. El alcance real solo sale de la escritura.
     - La misma persona puede aparecer dos veces con distinta grafía («APELLIDOS NOMBRE» y «DON NOMBRE APELLIDOS»): no la cuentes dos veces ni la trates como dos apoderados.
     - Un consejero persona jurídica actúa por la persona física que la represente: pide quién es y su nombramiento.
     - La fecha «desde» es la de publicación del acto en el BORME, no la de la aceptación del cargo.
     - **La lista de «Cargos vigentes» no es fiable por sí sola: manda el acto inscrito.** En las pruebas, la lista seguía mostrando como presidenta a quien un acto de «Situación concursal» había cesado años antes, y omitía la reelección como consejero delegado que sí figuraba en un acto reciente. Contrasta cada cargo con los actos mostrados antes de dar por bueno a un firmante.
     - **Comprueba que la denominación y el CIF de la cabecera son los que pediste.** En las pruebas, una búsqueda por el CIF de una sociedad devolvió otra distinta (su auditora). Si no coinciden, repite por la denominación exacta y no mezcles datos.
2. **Quién representa (LSC 210 y 233).** Administrador único: él. Solidarios: cada uno. Conjuntos: en la SL con más de dos, al menos dos mancomunadamente; en la SA, mancomunadamente. Consejo: el consejo colegiadamente o el consejero delegado; la delegación permanente no produce efecto hasta su inscripción (LSC 249.2). Compara el cargo del firmante con los «Cargos vigentes»; si no figura, ROJO hasta que aporte título.
3. **Cargo caducado (LSC 214, 221 y 222).** El nombramiento surte efecto desde la aceptación. En la SA el plazo estatutario no excede de seis años; en la SL es indefinido salvo estatutos. Si un administrador de SA figura «desde» hace más de seis años sin reelección visible, ÁMBAR: pide certificado de vigencia del cargo.
4. **Límites del poder (LSC 234).** Las limitaciones estatutarias son ineficaces frente a terceros; la sociedad queda obligada con terceros de buena fe y sin culpa grave aunque el acto quede fuera del objeto social. Esa buena fe y la ausencia de culpa grave son las que se discuten cuando falta el acuerdo de junta sobre activos esenciales (punto 7).
5. **Apoderados.** El índice muestra apoderados (Apoderado, Apo.Sol., Apo.Manc.) pero no el contenido del poder: pide copia. Para enajenar, gravar, transigir o cualquier acto de riguroso dominio hace falta mandato expreso (CC 1713). Lo hecho sin poder es nulo salvo ratificación (CC 1259); el mandante responde dentro de los límites del mandato (CC 1727). El mandato se extingue por revocación, muerte, concurso o medidas de apoyo (CC 1732); lo hecho ignorando la extinción vale frente a terceros de buena fe (CC 1738). Los actos inscritos y publicados en el BORME son oponibles a terceros (CCom 21). Si el poder es de personas físicas y una ha fallecido, busca `consulta="subsistencia del poder tras el fallecimiento del poderdante compraventa buena fe del tercero"`.
6. **Conflicto de interés y autocontratación.**
   - El administrador debe abstenerse de transacciones con la sociedad salvo operaciones ordinarias, estándar y de escasa relevancia (LSC 229.1.a); también si el beneficiario es una persona vinculada (LSC 229.2 y 231).
   - Dispensa (LSC 230.2): de la junta cuando la transacción supera el diez por ciento de los activos sociales o se trata de ventajas de terceros; en la SL, también para asistencia financiera, garantías a favor del administrador o relaciones de servicios u obra con él. En los demás casos puede darla el órgano de administración con independencia de quien la concede e inocuidad o condiciones de mercado. En la SL, la junta acuerda caso por caso créditos y garantías a socios y administradores (LSC 162) y el socio en conflicto no vota esa dispensa ni esa asistencia (LSC 190.1).
   - Si falta la dispensa exigible: ROJO; pide el acuerdo con el orden del día. Busca `consulta="dispensa artículo 230 transacciones del administrador con la sociedad requisitos"` y `consulta="autocontratación administrador conflicto de intereses validez contrato"` (`base="TS"`, `jurisdiccion="CIVIL"`).
   - Apoderado que contrata consigo mismo o con quien también representa: necesita autorización expresa en el poder o ratificación. Busca `consulta="autocontrato validez autorización previa del representado ejercicio abusivo del poder"`.
7. **Activos esenciales (LSC 160.f).** Adquirir, enajenar o aportar activos esenciales es competencia de la junta; se presume esencial cuando la operación supera el veinticinco por ciento del valor de los activos del último balance aprobado. Busca `consulta="activos esenciales artículo 160 f eficacia frente a terceros buena fe culpa grave"`, `base="TS"`, `jurisdiccion="CIVIL"`, `fecha_desde="01/01/2026"`, y lee el fundamento de la «Decisión de la sala», no el resumen de los motivos: el criterio vigente aplica por analogía el art. 234.2 LSC, de modo que la falta de acuerdo de junta no es oponible al tercero que actúa de buena fe y sin culpa grave, y la presunción del veinticinco por ciento y las circunstancias del caso sirven para valorar esa buena fe. Consecuencias según la posición del cliente:
   - **Cliente que adquiere o recibe el activo**: si la operación supera el umbral o el activo sostiene la actividad, exige certificado del acuerdo de junta como anexo del contrato. Sin él su buena fe queda discutida; una simple manifestación de que el activo «no es esencial» no basta si el balance o la actividad dicen lo contrario.
   - **Cliente que es la sociedad que transmite o sus socios**: sin acuerdo, el administrador actúa fuera de su competencia y la eficacia del acto frente al adquirente dependerá de la buena fe y la culpa grave de este; recomienda convocar la junta antes de firmar.
8. **Disolución y liquidación (LSC 363, 371 y 379).** La sociedad disuelta conserva personalidad, añade «en liquidación» y la representan los liquidadores solo para operaciones necesarias para liquidar. Un administrador firmando por una sociedad disuelta: ROJO.
9. **Concurso (TRLC 106, 109, 156, 226 y 227).** En concurso voluntario, intervención de la administración concursal; en necesario, suspensión y sustitución. Los actos que infringen la intervención o la suspensión son anulables a instancia de la administración concursal y no se inscriben mientras no se confirmen. La declaración de concurso no resuelve el contrato y se tienen por no puestas las cláusulas de resolución por concurso. Son rescindibles los actos perjudiciales de los dos años anteriores a la solicitud; el perjuicio se presume sin prueba en contrario en los actos a título gratuito. Si la contraparte muestra indicios de insolvencia: ÁMBAR con esta advertencia; si está en concurso: ROJO salvo autorización de la administración concursal.
   - **Fase de liquidación** (acto «Auto de apertura de la fase de liquidación» o sociedad «Disuelta» con administración concursal): la resolución que la abre declara la disolución y el cese de los administradores o liquidadores, sustituidos a todos los efectos por la administración concursal (TRLC 413.2). Solo vende la administración concursal, del modo más conveniente para el concurso salvo reglas especiales del juez (TRLC 415 y 421); si el bien forma parte de una unidad productiva, su venta separada exige autorización judicial (TRLC 422). Pide la credencial vigente de la administración concursal, el auto de liquidación y las reglas especiales.
   - El Registro Público Concursal no está en el conector: consulta su portal oficial (https://www.publicidadconcursal.es) o, si la sociedad cotiza, las comunicaciones de la Comisión Nacional del Mercado de Valores, y cítalos con enlace y fecha (punto 3 de la puerta). Si la consulta no es posible, pide al abogado la certificación.

### B. Personas físicas

1. **Capacidad y apoyos (CC 250, 287, 1263, 1301 y 1302).** Tras la Ley 8/2021 no hay incapacitación: hay medidas de apoyo (voluntarias, guarda de hecho, curatela, defensor judicial). El contrato celebrado prescindiendo del apoyo previsto es anulable; el plazo de cuatro años corre desde la celebración; la persona que presta el apoyo solo puede anularlo si el otro contratante conocía las medidas o se aprovechó obteniendo una ventaja injusta. El curador con funciones de representación necesita autorización judicial, entre otros, para enajenar o gravar inmuebles, dar inmuebles en arrendamiento por más de seis años, tomar dinero a préstamo o prestar aval (CC 287). Pide la escritura o la resolución y su alcance; si falta la autorización exigible, ROJO o condición suspensiva de autorización judicial. Busca `consulta="contrato persona con discapacidad sin medidas de apoyo anulabilidad"` y `consulta="curador autorización judicial venta de inmueble nulidad anulabilidad"`.
2. **Menores (CC 1263).** Solo los contratos que la ley les permita o los de la vida corriente propios de su edad; el resto, con sus representantes y, si la ley lo exige, autorización judicial.
3. **Prohibiciones de adquirir (CC 1459).** El tutor o quien desempeña funciones de apoyo no compra los bienes de la persona a quien representa; el mandatario, los bienes cuya administración o enajenación tiene encargada. Si el comprador está en esa situación: ROJO.
4. **Régimen matrimonial y vivienda familiar (CC 1320, 1322, 1375 y 1377).** Para disponer de la vivienda habitual y de los muebles de uso ordinario hace falta el consentimiento de ambos cónyuges aunque pertenezca a uno solo; la manifestación errónea o falsa del disponente no perjudica al adquirente de buena fe. Los actos onerosos sobre gananciales exigen a los dos. Sin el consentimiento necesario, el acto es anulable a instancia del cónyuge omitido (plazo del CC 1301.5.º) y los actos gratuitos sobre bienes comunes son nulos. Exige la comparecencia del cónyuge o, si el disponente declara que no es vivienda familiar, esa manifestación en el contrato. Si el régimen puede ser foral (separación de bienes, consorcial, conquistas), localiza la norma con `buscar_boe` y lee su texto vigente en internet, en el texto consolidado oficial (BOE o boletín autonómico), con enlace y fecha de consulta (punto 3 de la puerta); si tampoco así lo obtienes, aplica la puerta. Busca `consulta="disposición de la vivienda habitual sin consentimiento del otro cónyuge 1320 1322 anulabilidad"`.
   - Pregunta también si hay un **derecho de uso de la vivienda atribuido en un proceso de familia** (sentencia o convenio regulador) y comprueba en la nota simple si consta. Para disponer de la vivienda cuyo uso se atribuyó hace falta el consentimiento de ambos cónyuges o autorización judicial, y esa restricción se hace constar en el Registro; la manifestación falsa del disponente no perjudica al adquirente de buena fe (CC 96.3). Si el comprador conoce el uso o consta inscrito, ROJO sin ese consentimiento. Doctrina: `consulta="derecho de uso sobre la vivienda familiar atribuido por sentencia oponible al adquirente"` (`base="TS"`, `jurisdiccion="CIVIL"`). Si no hay datos, ÁMBAR.
   - **Divorciados con gananciales sin liquidar**: la sociedad de gananciales concluye con la disolución del matrimonio (CC 1392) y el bien pertenece a la comunidad postganancial hasta la liquidación. La venta por uno solo no es nula, pero no transmite más que lo que puede disponer; el comprador solo queda a salvo como tercero hipotecario (LH 34) si el bien figura inscrito a nombre exclusivo del vendedor y compra de buena fe. Exige la comparecencia del excónyuge o la liquidación previa. Doctrina: `consulta="venta bien comunidad postganancial un solo cónyuge sin consentimiento"`.
5. **Extranjeros.** `buscar_articulo` con `ley="CC"` y `articulo="9"` devuelve por error el artículo 94 bis: la ley personal del CC no se obtiene por esa vía. Lee el art. 13 del Reglamento Roma I (quien tiene capacidad según la ley del país donde contratan solo invoca su incapacidad según otra ley si la otra parte la conocía o la ignoró por negligencia). Si la capacidad depende de la ley nacional, lee el artículo 9 del Código Civil en internet (texto consolidado del BOE, https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763) y, si hace falta, la ley extranjera en su fuente oficial, citándolos con enlace y fecha de consulta (punto 3 de la puerta); si no los obtienes, díselo al abogado y aplica la puerta en ese punto.

### C. Inmuebles

- `consultar_catastro`: referencia catastral, localización, uso, superficie construida, año, coeficiente y, en rústica, cultivos. Compara uso y superficie con la descripción del contrato y de la nota simple; toda discrepancia, ÁMBAR.
- El Catastro no da titular, valor catastral ni cargas, ni cubre País Vasco y Navarra. Titularidad, cargas, anotaciones y limitaciones salen de la nota simple del Registro de la Propiedad, que el conector no consulta: sin ella, el inmueble queda en ÁMBAR.
- La fe pública registral protege al tercero que adquiere de buena fe y a título oneroso de quien figura en el Registro con facultades, una vez inscrito (LH 34): el titular registral debe coincidir con quien vende.

### Semáforo por parte

| Color | Cuándo |
|---|---|
| **ROJO** | Sociedad disuelta, en liquidación o en concurso sin intervención válida; firmante sin cargo ni poder suficiente; autocontratación o transacción del administrador sin la dispensa exigible; activo que se presume esencial (LSC 160.f) sin acuerdo de junta; vivienda familiar o ganancial sin el consentimiento necesario; curatela representativa sin autorización judicial exigible; prohibición del CC 1459 |
| **ÁMBAR** | Falta un documento para confirmar lo que el índice sugiere (poder, certificado de vigencia, nota simple, balance, capitulaciones); cargo de SA con más de seis años sin reelección visible; último acto antiguo o indicios de crisis; discrepancia entre Catastro y contrato |
| **VERDE** | Existencia, cargo o poder, ausencia de conflicto y, si hay inmueble, titularidad y cargas comprobadas con documento |

Una parte está en VERDE solo cuando cada comprobación que le afecta lo está. El color de la parte es el peor de sus comprobaciones.

## Documento que se entrega

**Informe de verificación en Word** (maquetación del apartado 2 del formato adaptada a informe; sin REUNIDOS ni firmas). Nombre: `verificacion-partes-<tipo>-<parte-principal>-<AAAAMMDD>.docx`. Orden:

1. **Resumen**: una línea por parte con su color y la razón principal; recomendación (firmar, firmar con condiciones o no firmar hasta subsanar).
2. **Ficha de cada sociedad**: datos del BORME (con la fecha de consulta y la advertencia de que no tienen fe pública), órgano y forma de actuar, firmante y su título, conflictos, activos esenciales, disolución o concurso, color.
3. **Ficha de cada persona física**: capacidad y apoyos, régimen matrimonial y vivienda, prohibiciones, color. Marcadores (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`) para lo no facilitado.
4. **Inmuebles**: datos del Catastro, discrepancias y estado de la nota simple.
5. **Documentos que hay que pedir**: nota simple del Registro Mercantil, certificado de vigencia del cargo, copia del poder, certificado del acuerdo de junta o de la dispensa, último balance aprobado, capitulaciones o certificado de matrimonio, resolución o escritura de apoyos y autorización judicial, nota simple del Registro de la Propiedad, consulta del Registro Público Concursal.
6. **Cláusulas que hay que incorporar al contrato**, con texto base que la skill del contrato adapta a su numeración y definiciones:
   - Intervención de sociedad: «[NOMBRE Y APELLIDOS], en nombre y representación de [DENOMINACIÓN SOCIAL], con CIF [CIF], en su condición de [CARGO], cargo vigente según [certificado / escritura de nombramiento de fecha [FECHA], inscrita en el Registro Mercantil de [PROVINCIA]], o en virtud de poder otorgado ante el notario [NOTARIO] el [FECHA], número [PROTOCOLO], que asegura vigente y suficiente para este acto.»
   - Activos esenciales (cliente adquirente): «La Vendedora manifiesta que la enajenación ha sido autorizada por su junta general en acuerdo de fecha [FECHA], cuyo certificado se incorpora como Anexo [N].» Si el acuerdo no existe, la firma se condiciona a su aportación.
   - Transacción con administrador o persona vinculada: «La operación ha sido dispensada conforme al artículo 230 de la Ley de Sociedades de Capital por acuerdo de [junta general / órgano de administración] de fecha [FECHA] (Anexo [N]).»
   - Vivienda familiar: comparecencia del cónyuge prestando su consentimiento o, si no es vivienda habitual, manifestación expresa del disponente en ese sentido.
   - Apoyos o concurso: condición suspensiva de la autorización judicial o de la administración concursal, con plazo y consecuencia si no se obtiene.
7. **Doctrina aplicada**: solo si se ha usado para un ROJO o para sostener una exigencia (activos esenciales, dispensa, autocontrato, vivienda familiar): párrafo literal entre comillas, órgano, fecha, número y ECLI tal como los devolvió `leer_sentencias`, con una línea sobre qué sostiene.
8. **Normativa consultada**: artículo, norma y «vigente desde».

Si en el entorno no se pueden crear archivos, entrega el texto completo con esos títulos y avisa de que hay que pasarlo a Word.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Cada sociedad consultada con `buscar_empresa_mercantil` por su CIF o denominación exacta, con la cabecera de la respuesta coincidente con lo pedido; etiqueta «Activa» y lista de cargos contrastadas con los actos; Registro Público Concursal y nota mercantil pedidos si hay dudas.
- [ ] El firmante de cada sociedad coincide con un cargo vigente o con un poder aportado cuyo contenido cubre el acto.
- [ ] Transacciones con administradores o personas vinculadas y activos esenciales analizados con LSC 160, 229, 230 y 231 y la doctrina leída; si no hay acuerdo de junta o dispensa exigible, ROJO.
- [ ] Personas físicas: apoyos, menores, CC 1459 y régimen matrimonial comprobados; vivienda familiar con el consentimiento del cónyuge o la manifestación en el contrato; tras un divorcio, uso atribuido (CC 96.3) y gananciales sin liquidar resueltos con la comparecencia del excónyuge o la autorización judicial.
- [ ] Inmuebles: Catastro consultado y nota simple pedida; discrepancias señaladas.
- [ ] Cada artículo leído con `buscar_articulo` en esta conversación; la capacidad de un extranjero no se ha resuelto por su ley nacional sin haber obtenido el precepto (el art. 9 del Código Civil no sale por `buscar_articulo`).
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (fundamento, no hechos ni datos de aquel pleito) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el informe y corregido lo que señale.
- [ ] Ningún dato personal inventado ni búsqueda por el nombre de un particular.
- [ ] Resumen en el chat según el apartado 10 del formato: qué se verificó y para quién, color de cada parte y motivo, documentos que faltan, tabla de jurisprudencia citada y próximo paso (la skill del contrato con las cláusulas que hay que incorporar).
