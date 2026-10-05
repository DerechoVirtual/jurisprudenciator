---
name: escrito-acusacion-frustracion-ejecucion
description: Redacta el escrito de acusación (calificación provisional y solicitud de apertura de juicio oral) por delitos de frustración de la ejecución — alzamiento de bienes, ocultación patrimonial y presentación de relación de bienes mendaz (arts. 257 a 258 ter CP). Actívala ante "acusación por frustración de la ejecución", "alzamiento de bienes", "insolvencia punible", "el deudor ha ocultado bienes para no pagar", "vaciamiento patrimonial", "el ejecutado no declaró sus bienes", "denuncia penal tras ejecución civil infructuosa" o "me han embargado y no hay nada".
---

# Escrito de acusación por frustración de la ejecución (arts. 257-258 ter CP)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Tipos y penas** (arts. 257-258 ter CP) → `buscar_articulo` (`ley="CP"`).
- **Sociedad deudora y administradores de hecho y de derecho** → `buscar_empresa_mercantil` (estado, domicilio, administradores, últimos actos inscritos).
- **Actos societarios en las fechas clave** (ceses, cambios de domicilio, ampliaciones o transmisiones tras la deuda o el embargo) → `sumario_borme` del día → `leer_boe`.
- **Inmuebles transmitidos u ocultados** → `consultar_catastro` (referencia catastral, dirección o polígono y parcela; no da titular ni valor) y `callejero_catastro` si la dirección no casa.
- **Subastas, edictos y notificaciones de la ejecución civil previa** → `novedades_boe` (por el NIF de la sociedad deudora o el número de autos) → `leer_boe`.
- **Doctrina sobre insolvencia real y ficticia** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Comprobar las citas de normas** → `verificar_escrito`: cada redactor lo pasa solo con las frases de su sección que citan artículos o leyes; el ensamblado comprueba que cada ECLI o ROJ procede de una fuente leída.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Redacta el escrito de acusación por insolvencia punible. **Es un delito que se prueba con documentos:
la ejecución civil previa es tu instrucción hecha.**

---

## ⚠️ Rúbrica y ubicación — corregido

La **LO 1/2015** reordenó el Capítulo VII bis del Título XIII del Libro II CP. **La rúbrica vigente
del capítulo es «De la frustración de la ejecución»** — «alzamiento de bienes» dejó de ser el nombre
del conjunto y es hoy **solo una de las modalidades** (art. 257.1.1.º). Las «insolvencias punibles»
en sentido estricto (concurso punible) están en el **capítulo siguiente** (arts. 259 y ss.). No los
mezcles: son delitos distintos, con requisitos distintos.

Contenido del capítulo, verificado: **257** (alzamiento y actos de disposición frustratorios), **258**
(relación de bienes incompleta o mendaz en ejecución), **258 bis** (uso de bienes embargados
constituidos en depósito), **258 ter** (personas jurídicas).

---

## Comprobaciones previas

Se responden con la documentación aportada (paso 2 de `redaccion-rapida`); pregunta solo lo que
bloquee y en una única ronda.

1. **Prescripción (art. 131 CP).** Art. 257.1 y 257.2: pena máxima **4 años** de prisión → **5 años**.
   Art. 257.3 párr. 2 (deuda de Derecho público): pena máxima **6 años** → **10 años** (prisión
   superior a 5 y hasta 10). Art. 258: pena máxima **1 año** → **5 años**. **Art. 131.2:** pena
   compuesta → rige la que exija **mayor tiempo**. **Verifica el cómputo caso por caso**: el
   *dies a quo* se sitúa en el **acto de ocultación**, no en el impago ni en el auto de insolvencia.
2. **Plazo de instrucción (art. 324 LECrim).** 12 meses + prórrogas de ≤6 meses por auto motivado
   **previo**; sin él, **inválidas las diligencias posteriores (324.3)**. Aquí es crítico: la
   averiguación patrimonial (Registro, AEAT, TGSS, entidades bancarias) **consume meses**. Pide la
   prórroga tú y a tiempo.
3. **Ley penal más favorable (art. 2.2 CP).** LO 1/2025 y LO 1/2026. Los arts. 257-258 ter **no** han
   sido modificados por ellas (vigentes desde 1-7-2015, LO 1/2015). **Pero** el art. 257.4 remite al
   **art. 250.1.5.º y 6.º**, y la **LO 1/2026 reescribió el art. 250.1** — comprueba la redacción
   vigente a la fecha de los hechos y compara.
4. **Non bis in idem / prejudicialidad:** relación con el concurso de acreedores (ver art. 257.5).

---

## Los tipos — verificados literalmente

### Art. 257 CP (vigente desde 1-7-2015)

**257.1 — prisión de 1 a 4 años y multa de 12 a 24 meses:**

- **1.º** «El que **se alce con sus bienes en perjuicio de sus acreedores**.» — alzamiento clásico.
- **2.º** «Quien con el mismo fin realice **cualquier acto de disposición patrimonial o generador de
  obligaciones** que **dilate, dificulte o impida la eficacia de un embargo o de un procedimiento
  ejecutivo o de apremio, judicial, extrajudicial o administrativo, iniciado o de previsible
  iniciación**.»
  > ⭐ **La modalidad decisiva y la más desaprovechada.** Tres claves: (i) **basta dilatar o
  > dificultar** — no hace falta impedir; (ii) alcanza al procedimiento **administrativo de apremio**;
  > (iii) **«o de previsible iniciación»** → **el delito puede cometerse ANTES de que exista demanda
  > ejecutiva**. Si el deudor vació el patrimonio al recibir el burofax o al ser demandado en el
  > declarativo, **ya está en el tipo**. No esperes al auto de insolvencia para denunciar.

**257.2 — misma pena:** quien realice actos de disposición, contraiga obligaciones que **disminuyan su
patrimonio** u **oculte por cualquier medio** elementos patrimoniales sobre los que la ejecución podría
hacerse efectiva, con la finalidad de **eludir el pago de responsabilidades civiles derivadas de un
delito** que hubiere cometido o del que debiera responder.

**257.3 — alcance y subtipo agravado:**

- Párr. 1: se aplica «**cualquiera que sea la naturaleza u origen de la obligación o deuda**» cuya
  satisfacción se intente eludir, **incluidos los derechos económicos de los trabajadores**, y con
  independencia de que el acreedor sea particular o persona jurídica, **pública o privada**.
- Párr. 2 — **agravado: prisión de 1 a 6 años y multa de 12 a 24 meses** si la deuda u obligación es
  **de Derecho público y la acreedora una persona jurídico-pública**, o se trata de obligaciones
  pecuniarias derivadas de **delito contra la Hacienda Pública o la Seguridad Social**.

**257.4 — penas en su MITAD SUPERIOR** en los supuestos de los **numerales 5.º o 6.º del art. 250.1**
(valor de la defraudación > 50.000 € o afectación a elevado número de personas; abuso de relaciones
personales o de credibilidad empresarial/profesional). ⚠️ **La LO 1/2026 reescribió el art. 250.1**:
verifica la redacción aplicable a la fecha de los hechos (art. 2 CP) y la actual (art. 2.2 CP).

**257.5 — «Este delito será perseguido aun cuando tras su comisión se iniciara un procedimiento
concursal.»** El concurso posterior **no** blinda al deudor ni desplaza lo penal.

### Art. 258 CP — relación de bienes mendaz (prisión de 3 meses a 1 año o multa de 6 a 18 meses)

- **258.1:** quien, **en un procedimiento de ejecución judicial o administrativo**, presente al
  encargado de la ejecución una **relación de bienes o patrimonio incompleta o mendaz**, y **con ello
  dilate, dificulte o impida la satisfacción del acreedor**.
  - ⭐ **Definición legal de «incompleta»:** «cuando el deudor ejecutado **utilice o disfrute de bienes
    de titularidad de terceros y no aporte justificación suficiente del derecho que ampara dicho
    disfrute y de las condiciones a que está sujeto**.» — **La herramienta contra el insolvente que
    vive bien**: el que conduce el vehículo de la sociedad y habita la vivienda de su cónyuge o de una
    interpuesta.
- **258.2:** misma pena si el deudor, **requerido para ello**, **deja de facilitar** la relación de
  bienes.
- **⚠️ 258.3 — EXCUSA ABSOLUTORIA que debes anticipar:** no son perseguibles si el autor, **antes de
  que la autoridad o funcionario hubieran descubierto** el carácter mendaz o incompleto de la
  declaración, **comparece y presenta una declaración veraz y completa**. **Fija en el escrito la fecha
  exacta en que el carácter mendaz fue descubierto** y sitúa cualquier rectificación posterior a ella.
  Si no lo haces, te vacían la acusación.
- **Requisito procesal implícito:** el 258 exige un **requerimiento previo** de manifestación de bienes
  en la ejecución (art. 589 LEC). Acredítalo con testimonio.

### Art. 258 bis CP — prisión de 3 a 6 meses o multa de 6 a 24 meses

Quienes **hagan uso de bienes embargados** por autoridad pública **constituidos en depósito sin estar
autorizados** — «salvo que ya estuvieran castigados con una pena más grave en otro precepto». Tipo
subsidiario, útil contra el depositario que dispone del bien embargado.

### Art. 258 ter CP — personas jurídicas

Cuando conforme al **art. 31 bis** la persona jurídica sea responsable de los delitos **del capítulo**:

- **a)** multa de **2 a 5 años**, si el delito de la persona física tiene prevista pena de prisión de
  **más de 5 años**;
- **b)** multa de **1 a 3 años**, si tiene prevista pena de prisión de **más de 2 años** no incluida en
  a);
- **c)** multa de **6 meses a 2 años**, en el resto de los casos.
- Atendidas las reglas del **art. 66 bis**, cabe además imponer las penas de las **letras b) a g) del
  art. 33.7 CP**.

> **Aquí SÍ responde penalmente la persona jurídica** (a diferencia del art. 318 CP en siniestralidad
> laboral). Encaje típico: la sociedad instrumental a la que se transfieren los activos. **Acúsala**,
> y verifica el **programa de cumplimiento** (art. 31 bis 2 y 4). Determina la letra aplicable por la
> **pena en abstracto del delito de la persona física**: art. 257.1 (hasta 4 años) → **letra b)**;
> art. 257.3 párr. 2 (hasta 6 años) → **letra a)**; art. 258 → **letra c)**.

---

## Elementos que hay que acreditar — y cómo

| Elemento | Cómo se prueba |
|---|---|
| **Crédito preexistente**, vencido, líquido y exigible (o de **previsible** reclamación) | Contrato, facturas, albaranes, reconocimiento de deuda, burofax, sentencia del declarativo |
| **Acto de disposición u ocultación** | Escritura de compraventa o donación, nota simple con el asiento, extractos bancarios, cuentas anuales, BORME, contratos de cesión de activos |
| **Resultado: insolvencia total o parcial**, real o **ficticia** | Diligencia de embargo negativa, auto de insolvencia, averiguación patrimonial (**punto neutro judicial**), certificaciones AEAT/TGSS |
| **Nexo entre el acto y la frustración** | **Cronología**: el acto debe situarse tras el nacimiento del crédito y en proximidad al requerimiento, la demanda o el embargo |
| **Elemento subjetivo: ánimo de perjudicar** | Se infiere de **indicios objetivos** (ver abajo) |

### ⭐ Insolvencia real vs. ficticia — el punto que decide el juicio

- **Real:** el patrimonio **sale** efectivamente (venta a tercero, consumo, transferencia al
  extranjero).
- **Ficticia o aparente:** el patrimonio **permanece bajo el control** del deudor pero **cambia de
  titularidad formal** — transmisión a familiares, a sociedad interpuesta o instrumental, simulación.
  **Es la modalidad habitual y la más punible.**
- **No se exige insolvencia total.** Basta que la ocultación **dilate o dificulte** (257.1.2.º y
  258.1). El deudor que conserva bienes pero los hace inaccesibles está en el tipo. **Este es el error
  que más acusaciones hunde**: creer que hace falta un patrimonio a cero.
- **Indicios de ficción, a alegar acumulativamente y con folio:** precio **vil** o inexistente; falta
  de acreditación del **flujo real del dinero** (extractos); **proximidad temporal** con el
  requerimiento o la demanda; **vinculación personal o societaria** entre transmitente y adquirente;
  **el deudor sigue usando y disfrutando** del bien (enlaza con la definición legal del art. 258.1
  párr. 2); mantenimiento del **nivel de vida**; constitución de sociedad **coetánea** al conflicto;
  **cascada de transmisiones** encadenadas.

---

## Relación con el proceso civil de ejecución previo

**No es un requisito del tipo, pero es tu mejor prueba.** El art. 257.1.2.º admite el procedimiento
«**iniciado o de previsible iniciación**»: **no esperes al auto de insolvencia** — la prescripción
corre y los activos se alejan.

- **Testimonio íntegro de la ejecución civil**, por oficio: demanda ejecutiva, auto despachando
  ejecución, **diligencias de embargo negativas**, resultado de la **averiguación patrimonial**
  (art. 590 LEC), **requerimiento de manifestación de bienes (art. 589 LEC)** y la **relación
  presentada** — que es el **cuerpo del delito del art. 258**.
- La sentencia civil firme acredita el **crédito**, no el delito. El **ánimo de perjudicar** se prueba
  en lo penal.
- **Alternativa civil que debes valorar y explicar al cliente:** la **acción pauliana o rescisoria**
  (arts. 1111 y 1291.3.º CC) recupera el bien; lo penal castiga pero **no reintegra** salvo por la vía
  de la responsabilidad civil ex delicto (arts. 109 y ss. CP) o de la **nulidad de los actos** de
  disposición. Ambas vías son **compatibles**. Si el objetivo del cliente es **cobrar**, dilo.
- **Concurso posterior:** **art. 257.5** — el delito se persigue igualmente. No es óbice.

---

## Estructura del escrito

1. Encabezamiento a la **Sección de Instrucción del Tribunal de Instancia** con nº de diligencias
   previas / procedimiento abreviado.
   > ⭐ **Copia la denominación exacta que figure en la resolución que contestas o en la carátula del
   > procedimiento.** Es lo que nunca falla, diga «Sección de Instrucción del Tribunal de Instancia»
   > o siga diciendo «Juzgado de Instrucción». La nomenclatura vigente (art. 14 LECrim, desde el
   > 3-10-2025) es la de **Sección**; la antigua no invalida el escrito (DA 1.ª LO 1/2025).
2. Comparecencia de procurador y letrado de `[MERCANTIL ACUSADORA]` / `[PERJUDICADO]`.
3. Fórmula: evacuando el traslado del **art. 780.1 LECrim** (plazo **común de 10 días** — verificado),
   **solicita la APERTURA DEL JUICIO ORAL** ante la **Sección de lo Penal** contra `[ACUSADO 1]` (por sí y
   como administrador de `[MERCANTIL 1]`), `[ACUSADO 2]` y, en su caso, `[MERCANTIL 2]` como persona
   jurídica ex art. 258 ter, y formula **ESCRITO DE ACUSACIÓN**.
4. **CONCLUSIONES PROVISIONALES (art. 650):**
   - **PRIMERA — HECHOS PUNIBLES**, en orden **estrictamente cronológico**, anclados al folio:
     (i) **relación comercial** y suministro o servicio prestado; (ii) **facturas impagadas** y cuantía
     total; (iii) **reconocimiento de deuda** o requerimiento extrajudicial, **con su fecha** — marca
     el momento en que la ejecución era «**de previsible iniciación**»; (iv) **proceso civil previo**:
     juicio ordinario, sentencia, apelación confirmatoria, firmeza, demanda ejecutiva y auto de
     despacho; (v) **actos de ocultación y vaciamiento**, uno a uno, con fecha, instrumento, bien,
     valor y adquirente; (vi) **resultado**: embargo negativo, insolvencia; (vii) **indicios de
     simulación** y **continuidad en el uso** de los bienes.
   - **SEGUNDA — CALIFICACIÓN.** Art. 257.1.1.º y/o 257.1.2.º CP; agravado del 257.3 párr. 2 si la
     deuda es de Derecho público; **mitad superior** del 257.4 si concurre el 250.1.5.º o 6.º; art. 258
     por la relación mendaz; art. 258 bis si hubo uso de bien depositado; **art. 258 ter** para la
     persona jurídica. **Delito continuado (art. 74 CP)** si hay pluralidad de actos de ocultación en
     ejecución de un mismo plan — razónalo.
   - **TERCERA — PARTICIPACIÓN.** Autoría del deudor. **⭐ El adquirente (*extraneus*) responde como
     cooperador necesario** si conocía la finalidad frustratoria — **acúsalo**, con el indicio que lo
     soporta; es donde está el patrimonio. Administradores de hecho y de derecho (art. 31 CP).
   - **CUARTA — CIRCUNSTANCIAS MODIFICATIVAS.**
   - **QUINTA — PENAS**, individualizadas por acusado, con las reglas de los arts. 66 y ss. y, para la
     persona jurídica, del **art. 66 bis**.
   - **SEXTA — RESPONSABILIDAD CIVIL.** **⭐ Pide la NULIDAD de los actos de disposición** y la
     **reintegración del bien** al patrimonio del deudor, además de la indemnización (arts. 109-115 CP)
     y del **decomiso** (arts. 127 y ss. CP; considera el 127 bis/quater si procede) [verificar el
     apartado aplicable]. Sin nulidad, la sentencia condena pero no cobra.
5. **PRUEBA:** documental de la ejecución civil por **testimonio**; **certificaciones registrales**
   (propiedad y mercantil) con **nota histórica**; **cuentas anuales** depositadas y **BORME**;
   **oficio a la AEAT y a la TGSS**; **oficio a entidades bancarias** (movimientos del período crítico);
   **pericial contable** sobre el vaciamiento y el flujo del precio; **testifical** (fedatarios,
   adquirentes, empleados); **interrogatorio** de los acusados.
6. **SUPLICO** y **OTROSÍES:** **medidas cautelares reales** (art. 764 LECrim; **anotación preventiva
   de embargo** y **prohibición de disponer** sobre los bienes transmitidos) — **pídelas ya, no al
   final**; fianza al responsable civil (art. 783.2). Lugar, fecha y firma.

**Reparto para la redacción rápida:** las conclusiones llevan el rótulo `### [ALEGACION]`, que el ensamblador numera en femenino (PRIMERA.-, SEGUNDA.-…). 01 encabezamiento, comparecencia, fórmula y conclusión PRIMERA, hechos punibles en orden cronológico (dos secciones si pasan de 1.200 palabras) · 02 conclusión SEGUNDA, calificación (tipos del 257, 258, 258 bis y 258 ter, delito continuado, con sus búsquedas sobre insolvencia ficticia y deuda vencida) · 03 conclusiones TERCERA a QUINTA: participación del deudor y del adquirente, circunstancias y penas · 04 conclusión SEXTA, responsabilidad civil con nulidad de los actos de disposición, reintegración y decomiso · 05 prueba, suplico, otrosíes con cautelares reales, lugar, fecha y firma.

---

## Errores típicos

| Error | Corrección |
|---|---|
| «Alzamiento de bienes» como rúbrica del capítulo | Es **frustración de la ejecución** desde la LO 1/2015. El alzamiento es el **257.1.1.º** |
| Confundirlo con las **insolvencias punibles** del concurso | Son los **arts. 259 y ss.**, capítulo distinto |
| Esperar al auto de insolvencia para denunciar | El **257.1.2.º** cubre la ejecución «**de previsible iniciación**». Se pierde tiempo y prescripción |
| Exigir insolvencia **total** | Basta **dilatar o dificultar** (257.1.2.º y 258.1) |
| No acusar al **adquirente** | Cooperador necesario si conocía la finalidad. **Ahí está el patrimonio** |
| Olvidar el **art. 258** cuando hubo manifestación de bienes | La relación mendaz es un delito **autónomo** y muy probable en toda ejecución |
| Ignorar la **excusa absolutoria del 258.3** | Fija la **fecha del descubrimiento** y sitúa la rectificación después |
| No pedir la **nulidad** de los actos de disposición | Sin ella, condena sin cobro |
| Creer que el **concurso posterior** blinda al deudor | **Art. 257.5**: se persigue igualmente |
| Olvidar el **art. 258 ter** | Aquí la persona jurídica **sí** responde ex art. 31 bis |
| No pedir medidas cautelares reales al inicio | Los bienes siguen moviéndose durante la instrucción |
| Citar el 250.1.5.º/6.º sin verificar | La **LO 1/2026 reescribió el art. 250.1**. Arts. 2 y 2.2 CP |

## Reglas de trabajo

- **Verifica con `buscar_articulo` antes de citar.** Anclas: `references/anclas-normativas-penal.md`.
- **Jurisprudencia solo vía `jurisprudenciator`** (`buscar_sentencias`, `buscar_por_cita`,
  `leer_sentencias`) — especialmente sobre la insolvencia ficticia, la exigencia de deuda vencida y la
  posición del adquirente. **Prohibido inventar** ECLI, ROJ, fechas o ponentes. Sin verificar →
  `[verificar]`.
- **Prohibido inventar** penas, plazos, ordinales o artículos. Lo no verificable → `[verificar]`.
- **Ancla al folio**: «(f. …)». La cronología es la acusación: fecha, folio, acto.
- **Anonimización:** `[ACUSADO]`, `[PERJUDICADO]`, `[MERCANTIL]`, `[CIF]`, `[TESTIGO]`. Datos de
  infracciones y condenas = **categoría especial (art. 10 RGPD)**. Ver `PROTECCION-DATOS.md`.
- **Instruye el Juez de Instrucción.** No existe el «fiscal instructor» en Derecho vigente.
- Terminología LO 1/2025: Tribunales de Instancia, LAJ, audiencia preliminar (art. 785).

## Entrega

Word `.docx`, que genera el ensamblado de `redaccion-rapida`, con conclusiones provisionales, prueba,
suplico y otrosíes, maquetado para LexNET. Incluye en el propio escrito una **línea temporal** (fecha →
acto → folio → efecto patrimonial) y un **cuadro de bienes** (bien → titularidad originaria → acto de
transmisión → adquirente → precio → uso actual).
