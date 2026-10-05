---
name: escrito-defensa-calificacion
description: >-
  Redacta el escrito de defensa (calificación de la defensa) en procedimiento abreviado tras el traslado del art. 784.1 LECrim, con conclusiones correlativas, proposición de prueba y otrosíes. Actívala ante "escrito de defensa", "conclusiones provisionales de la defensa", "contestar a la acusación", "disconformidad con el escrito de acusación", "proponer prueba para juicio", "me han dado traslado para defensa", "tengo diez días para el escrito de defensa" o "solicitar la libre absolución". Es también la VÍA ÚTIL para combatir una acusación tras la apertura del juicio oral: como el auto de apertura es irrecurrible salvo en cuanto a la situación personal, "quiero recurrir la apertura de juicio oral" se canaliza normalmente por aquí y no por /recurso-reforma-apelacion-auto-apertura-jo.
---

# Escrito de defensa (calificación de la defensa) — procedimiento abreviado

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo y contenido del escrito** (arts. 650, 784 y 785 LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Tipo, pena y conclusiones alternativas** (atenuantes, dilaciones indebidas del art. 21.6.ª) → `buscar_articulo` (`ley="CP"`), en la redacción aplicable a la fecha de los hechos.
- **Doctrina que sostiene cada conclusión de la defensa** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Presunción de inocencia y prueba ilícita** → `buscar_sentencias` (`base="TC"`).
- **ECLI que cite el escrito de acusación** → `buscar_por_cita`.
- **Comprobar las citas de normas** → `verificar_escrito`: cada redactor lo pasa solo con las frases de su sección que citan artículos o leyes; el ensamblado comprueba que cada ECLI o ROJ procede de una fuente leída.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Redacta el escrito de defensa del art. 784.1 LECrim. **Es el escrito que fija el perímetro del juicio
para la defensa: lo que no se pide aquí, en general, ya no se pide.**

---

## ⏱️ EL PLAZO — 10 días comunes, y es preclusivo para la prueba

Verificado literalmente contra el BOE (art. 784.1, redacción LO 13/2015, **no modificado** por la
LO 1/2025):

1. Abierto el juicio oral, el LAJ emplaza al encausado, con copia de los escritos de acusación, para
   que **en 3 días** comparezca con abogado y procurador.
2. Cumplido ese trámite, traslado de las actuaciones para que **en plazo común de 10 días** se
   presente escrito de defensa.

### Consecuencia de no presentarlo — matiz que se falla siempre

- «Si la defensa no presentare su escrito en el plazo señalado, **se entenderá que se opone a las
  acusaciones y seguirá su curso el procedimiento**», sin perjuicio de la responsabilidad
  disciplinaria (Título V del Libro V LOPJ). **No hay allanamiento ni condena automática.**
- **⚠️ PERO la prueba PRECLUYE.** Art. 784.1 párr. 3, verificado: «Una vez precluido el trámite para
  presentar su escrito, **la defensa sólo podrá proponer la prueba que aporte en el acto del juicio
  oral para su práctica en el mismo**», sin perjuicio de que pueda interesar previamente que se
  libren las comunicaciones necesarias **con antelación suficiente** respecto de la fecha señalada.
  > **Traducción:** sin escrito de defensa, te quedas sin testigos citados judicialmente, sin
  > peritos y sin oficios. Solo la prueba que **lleves físicamente** al juicio. Es la diferencia
  > entre defender y asistir.
- El precepto salva expresamente «lo previsto en el **párrafo segundo del apartado 1 del artículo
  785**» — que hoy, tras la LO 1/2025, permite en la **audiencia preliminar** proponer la
  incorporación de informes, certificaciones y documentos, y la prueba **de la que no se tuvo
  conocimiento** al formular los escritos. Es una vía de rescate **estrecha**, no un sustituto.
- **⚠️ Remisión descoordinada (verificada):** el 784.1 in fine añade que, si hay indefensión, podrá
  aducirse «de acuerdo con lo previsto en el **apartado 2 del artículo 786**». Cuando se escribió,
  el 786.2 era el **turno de cuestiones previas** al inicio del juicio. Tras la LO 1/2025, el **786.2
  son los criterios de señalamiento**: la remisión **ha quedado vacía de sentido**. Léela hoy
  reconducida a la **audiencia preliminar del art. 785**, y adviértelo si la invocas.

### Comprobaciones previas — antes de escribir una línea

Se responden con la documentación aportada (paso 2 de `redaccion-rapida`); pregunta solo lo que
bloquee y en una única ronda.

1. **Prescripción del delito (art. 131 CP)** a la fecha de los hechos: 5 años el común; 1 año delitos
   leves e injurias/calumnias; ver `references/anclas-normativas-penal.md` § 3.3. Si prescribió,
   **artículo de previo pronunciamiento**, no conclusión.
2. **Plazo de instrucción (art. 324 LECrim).** 12 meses desde la **incoación**, prórrogas de ≤6 meses
   por **auto motivado dictado ANTES del vencimiento**. **324.3:** sin ese auto previo, o si fue
   revocado en recurso, **no son válidas las diligencias acordadas a partir de esa fecha**. Reconstruye
   la cronología: fecha de incoación → cada auto de prórroga → fecha de cada diligencia de cargo. Es
   el argumento de nulidad más rentable y más desatendido. Las acordadas **antes** del vencimiento
   valen aunque se reciban después (324.2).
3. **Ley penal más favorable (art. 2.2 CP).** **LO 1/2025** y **LO 1/2026** (multirreincidencia,
   vigente 10-4-2026: reescribió el **art. 248 CP** y tocó 22.8.ª, 66.2, 80.2, 234.2, 235.1,
   250.1.8.º, 255.3, 568.2). Hechos anteriores → **compara y pide la más favorable**.
4. **Prueba ilícita:** art. 11.1 LOPJ y art. 238 LOPJ; arts. 18 y 24 CE.
5. **Suspensión (art. 80 CP, redacción LO 1/2026):** calcula desde ya si la pena pedida es
   suspendible. ⭐ Novedad: no computan los antecedentes de delitos que «carezcan de relevancia para
   valorar la probabilidad de comisión de delitos futuros» (80.2.1.ª).

---

## Marco normativo

- **Traslado y plazo:** art. 784.1 LECrim (3 días para comparecer; **10 días comunes** para el
  escrito). Correlación con los escritos de acusación del art. 780.1.
- **Contenido de las conclusiones:** por remisión al **art. 650 LECrim** — verificado: conclusiones
  **precisas y numeradas**: 1.º hechos punibles; 2.º calificación legal; 3.º participación; 4.º
  circunstancias modificativas o eximentes; 5.º penas. Y, para quien sostenga la acción civil:
  cuantía de daños y perjuicios o cosa a restituir, y personas responsables.
- **Prueba:** **art. 784.2** LECrim — en el escrito de defensa «se podrá solicitar del órgano judicial
  que **recabe la remisión de documentos o cite a peritos o testigos**», para el juicio oral o, en su
  caso, para **prueba anticipada**.
- **Presunción de inocencia y defensa:** art. 24.2 CE. **Ley penal en el tiempo:** art. 2 CP.
- **Conformidad en el escrito de defensa:** art. 784.3 (ver abajo).
- **Rebeldía:** art. 784.4 (ver abajo).

---

## ⚖️ Artículos de previo pronunciamiento — su sede CAMBIÓ

**La LO 1/2025 los trasladó a la audiencia preliminar del art. 785.1.** Ya **NO** se plantean al
inicio del juicio oral.

- En la **audiencia preliminar (art. 785.1)** se ventilan: **conformidad**, **competencia**,
  **vulneración de derechos fundamentales**, **artículos de previo pronunciamiento**, causas de
  suspensión, **nulidad de actuaciones**, y **contenido, finalidad o nulidad de las pruebas**
  propuestas. También la incorporación de documentos y la prueba desconocida al calificar.
- **785.2:** requiere asistencia del **acusado y del abogado defensor**; no se suspende por
  inasistencia injustificada del acusado citado en forma.
- **785.3:** resolución **oral** (o auto en **10 días** si hay complejidad). **No cabe recurso**,
  salvo **protesta** y reproducción en el recurso contra la sentencia — **salvo** que la resolución
  **ponga fin al procedimiento**, en cuyo caso cabe **apelación** (arts. 790 y ss.).
- **⚠️ Quien reserve las cuestiones previas para el juicio llega tarde.** El **art. 787.3** vigente
  solo admite ya, al inicio de las sesiones, la incorporación de **informes, certificaciones y
  documentos** y la prueba **de la que no se tuvo conocimiento al celebrar la audiencia preliminar**.
- **Operativo:** **anuncia en el escrito de defensa**, por otrosí, las cuestiones que sostendrás en la
  audiencia preliminar (nulidad ex 324.3, prueba ilícita ex 11.1 LOPJ, competencia, prescripción). No
  es exigencia legal expresa, pero evita la sorpresa y consolida tu posición. Y **no dejes de formular
  la protesta** del 785.3 si te las rechazan: sin protesta, no hay motivo en apelación.

---

## Conformidad en el escrito de defensa (art. 784.3)

- Cabe manifestarla **en el propio escrito, firmado también por el acusado**.
- También con el **nuevo escrito de calificación** que firmen conjuntamente acusaciones, acusado y
  letrado, **en cualquier momento anterior a las sesiones del juicio**.
- **⚠️ Descoordinación verificada:** el 784.3 remite a «los términos previstos en el **artículo 787**»
  y a «lo dispuesto en el **artículo 787.1**». Tras la LO 1/2025, el régimen de la conformidad está en
  el **art. 785.4-785.11**, y el 787.1 regula hoy la asistencia al juicio. **Cita el 785 como sede
  sustantiva** y advierte del desajuste. Detalle completo en la skill `conformidad-penal-catalogo`.
- Si te conformas, **cumple el art. 785.7 in fine**: «El letrado o la letrada facilitará por escrito a
  la persona a quien defiende la información sobre el acuerdo alcanzado.»

## Rebeldía (art. 784.4) — remisión rota, verificada

Texto vigente: si abierto el juicio oral los acusados están en **ignorado paradero** y no designaron
domicilio (art. 775), «y en cualquier caso, si **la pena solicitada excediera de los límites
establecidos en el párrafo segundo del apartado 1 del artículo 786**», el juez expedirá requisitoria y
los declarará **rebeldes**.

- **⚠️ La remisión está DESCOORDINADA.** Verificado: el **art. 786 vigente es el señalamiento**, y su
  apartado 1 párrafo segundo dice hoy «En los demás casos se fijará el día y hora por el letrado o la
  letrada de la Administración de Justicia…» — **no contiene límite de pena alguno**.
- **Los límites existen, pero se han mudado al art. 787.1**, párrafo 2, letras a) y b) — verificado:
  - **a)** que la **pena más grave solicitada** no exceda de **2 años** de privación de libertad; que
    no exceda de **6 años** si es de **distinta naturaleza**; o que sea **multa**, cualquiera que sea
    su cuantía o duración; **y**
  - **b)** ⭐ que, tratándose de penas privativas de libertad, **la suma total de las penas
    solicitadas no exceda de 5 años** — **requisito acumulativo nuevo** que antes no existía.
- **Operativo:** la remisión del 784.4 debe leerse hoy dirigida al **art. 787.1 párr. 2**. Dilo así,
  con la advertencia del desajuste, y **contrasta con `buscar_sentencias`** antes de fundar en ello una
  estrategia. Para la defensa, el requisito **b)** es una vía nueva: una suma de penas > 5 años impide
  el juicio en ausencia aunque ninguna pena individual llegue a 2 años.
- **784.5:** presentado el escrito o transcurrido el plazo, el LAJ remite lo actuado al órgano de
  enjuiciamiento.

---

## Estructura del escrito

1. Encabezamiento a la **Sección de lo Penal del Tribunal de Instancia** / Audiencia Provincial, con
   nº de procedimiento abreviado y de diligencias previas de origen.
   > ⭐ **Copia la denominación exacta que figure en la resolución que contestas o en la carátula del
   > procedimiento.** Es lo que nunca falla, diga «Sección de lo Penal del Tribunal de Instancia» o
   > siga diciendo «Juzgado de lo Penal». La nomenclatura vigente (art. 14 LECrim, desde el
   > 3-10-2025) es la de **Sección**; la antigua no invalida el escrito (DA 1.ª LO 1/2025).
2. Comparecencia de procurador y letrado de `[ACUSADO]`.
3. Fórmula: **evacuando el traslado conferido conforme al art. 784.1 LECrim**, en tiempo y forma, y
   mostrando **disconformidad** con los escritos de acusación del Ministerio Fiscal y de la acusación
   particular, formula **ESCRITO DE DEFENSA** con las siguientes conclusiones, **correlativas** a las
   de la acusación.
4. **CONCLUSIONES** (correlativas y numeradas, art. 650):
   - **PRIMERA — HECHOS.** Disconformidad con el relato de la acusación. Contrarrelato **anclado al
     folio** de las actuaciones. Fija el **marco temporal** (determina la redacción del CP aplicable,
     art. 2 CP). Niega expresamente los hechos base de cada elemento del tipo — no globalmente.
   - **SEGUNDA — CALIFICACIÓN.** Atipicidad, o subsunción alternativa más benigna. Cita el precepto
     **vigente a la fecha de los hechos** y, si la reforma posterior es más favorable, invoca el
     **art. 2.2 CP**.
   - **TERCERA — PARTICIPACIÓN.** No intervención de `[ACUSADO]`; subsidiariamente, complicidad
     (art. 29 CP) o tentativa (art. 16 CP) frente a autoría consumada.
   - **CUARTA — CIRCUNSTANCIAS MODIFICATIVAS.** Disconformidad con las agravantes. Atenuantes que se
     invocan (art. 21 CP: reparación, dilaciones indebidas, confesión, adicción), **con el hecho que
     las soporta y su folio**. Eximentes completas o incompletas (arts. 20 y 21.1.ª CP).
   - **QUINTA — PENAS.** Improcedencia. Subsidiariamente, pena mínima con el precepto correcto y las
     reglas de los arts. 66 y ss. CP.
   - **SEXTA — RESPONSABILIDAD CIVIL.** Inexistencia; subsidiariamente, impugnación del quantum y de
     los conceptos, y de la condición de responsable civil.
5. **SUPLICO:** que se tenga por evacuado el traslado y presentado en tiempo y forma el escrito de
   defensa, y por interesada la práctica de la prueba, dictándose en su día sentencia **absolutoria**
   de `[ACUSADO]`, con todos los pronunciamientos favorables y declaración de costas de oficio.
6. **OTROSÍES:**
   - **PRIMERO — PRUEBA (art. 784.2).** Por orden: **interrogatorio** de `[ACUSADO]`; **testifical**
     con nombre y domicilio a efectos de citación judicial, indicando si comparecerán a instancia de
     parte; **pericial**, con identificación del perito y del informe, e interesando su citación para
     ratificación y contradicción; **documental** por reproducción de folios **concretos** (nunca «la
     totalidad de las actuaciones»); **más documental** vía oficios, con la entidad, el documento y la
     **pertinencia** de cada uno; en su caso, **prueba anticipada** (art. 784.2) con su justificación.
   - **SEGUNDO — CUESTIONES PARA LA AUDIENCIA PRELIMINAR (art. 785.1).** Anuncia nulidad ex art. 324.3,
     prueba ilícita ex art. 11.1 LOPJ, competencia, prescripción o artículos de previo pronunciamiento.
   - **TERCERO — SITUACIÓN PERSONAL**, si procede.
   - **CUARTO —** en su caso, conformidad ex art. 784.3, **firmada también por el acusado**.
7. Lugar, fecha y firma de letrado y procurador.

**Reparto para la redacción rápida:** las conclusiones llevan el rótulo `### [ALEGACION]`, que el ensamblador numera en femenino (PRIMERA.-, SEGUNDA.-…), y cada una debe quedar correlativa a la de la acusación. 01 encabezamiento, comparecencia, fórmula y conclusión PRIMERA, contrarrelato de hechos con folios · 02 conclusiones SEGUNDA y TERCERA: calificación y participación (sus búsquedas) · 03 conclusiones CUARTA a SEXTA: circunstancias, penas y responsabilidad civil · 04 suplico y otrosíes (prueba por orden, cuestiones para la audiencia preliminar, situación personal), lugar, fecha y firma.

---

## Errores típicos

| Error | Corrección |
|---|---|
| Reservar las cuestiones previas «para el inicio del juicio» | Su sede es la **audiencia preliminar del 785.1**. El 787.3 ya no las admite |
| Dejar pasar los 10 días «porque igualmente se entiende que hay oposición» | Cierto en cuanto a la oposición, **pero la prueba precluye** (784.1 párr. 3) |
| Citar el art. 786.1 párr. 2 para los límites de la rebeldía | Hoy es el señalamiento. Los límites están en el **787.1 párr. 2 a) y b)** |
| Olvidar el requisito **b)** del 787.1 (suma ≤ 5 años) | Es **acumulativo y nuevo**: puede impedir el juicio en ausencia |
| «Conformidad del art. 787» | Es el **art. 785.4-11** desde el 3-4-2025 |
| Proponer «la totalidad de las actuaciones» como documental | Se inadmite o se convierte en nada. Cita **folios concretos** |
| Testigos sin domicilio | Sin domicilio no hay citación judicial: comparecencia a tu cargo |
| No formular la protesta del 785.3 | Sin protesta **no hay motivo** en el recurso contra la sentencia |
| Conclusiones no correlativas | Rompen el contraste con la acusación y debilitan el escrito |
| Alegar el CP vigente hoy para hechos de 2024 | **Art. 2 CP.** Identifica la redacción de la fecha de los hechos y compara (2.2 CP) |
| Atenuantes sin hecho ni folio que las soporte | Se desestiman sin más |

## Reglas de trabajo

- **Verifica con `buscar_articulo` antes de citar.** Anclas: `references/anclas-normativas-penal.md`.
- **Jurisprudencia solo vía `jurisprudenciator`** (`buscar_sentencias`, `buscar_por_cita`,
  `leer_sentencias`). **Prohibido inventar** ECLI, ROJ, fechas o ponentes. Sin verificar → `[verificar]`.
- **Prohibido inventar** penas, plazos, ordinales o artículos. Lo no verificable → `[verificar]`, y se
  advierte.
- **Ancla al folio** toda afirmación de hecho: «(f. 123)». Sin folio, no se escribe.
- **Anonimización:** `[ACUSADO]`, `[VÍCTIMA]`, `[TESTIGO]`, `[PERITO]`. Los datos de infracciones y
  condenas penales son de **categoría especial (art. 10 RGPD)**. Máxima cautela con víctimas menores.
  Ver `PROTECCION-DATOS.md`.
- **Instruye el Juez de Instrucción.** No existe el «fiscal instructor» en Derecho vigente.
- Terminología LO 1/2025: Tribunales de Instancia, LAJ, audiencia preliminar.

## Entrega

Word `.docx`, que genera el ensamblado de `redaccion-rapida`, con conclusiones correlativas, suplico y
otrosíes de prueba, maquetado para LexNET. Añade al resumen de la entrega (no al Word) un **cuadro de
control de plazos**: fecha de notificación del traslado, día de vencimiento de los 10 días y fecha de
presentación con el margen de seguridad de la casa.
