---
name: recurso-apelacion-sentencia-penal-catalogo
description: Catálogo (sin plantilla). Redacta recurso de apelación penal contra sentencia de la Sección de lo Penal del Tribunal de Instancia (antes Juzgado de lo Penal) o de la Audiencia Provincial en primera instancia. Actívala ante "recurrir la sentencia penal", "recurso de apelación contra sentencia condenatoria/absolutoria", "sentencia del juzgado de lo penal", "error en la valoración de la prueba", "infracción de precepto penal", "apelar ante la Audiencia Provincial", "nulidad del juicio", o "adherirse a la apelación".
---

# Recurso de apelación penal contra sentencia (catálogo — sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo, motivos y límites de la apelación** (arts. 790-792 y 846 ter LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Criterio de la Sala que resolverá** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"` o `"TSJ"`, `provincia`) + `leer_sentencias` con `parrafos=3`.
- **Revisión de absoluciones y de la prueba personal en segunda instancia** → `buscar_sentencias` (`base="TC"`) y (`jurisdiccion="PENAL"`, `base="TS"`).
- **Resoluciones que cita la sentencia recurrida** → `buscar_por_cita`.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

Redacta la apelación penal contra sentencia. Consulta `references/anclas-normativas-penal.md` (§ 3.2)
antes de citar plazos. Perfil del despacho:
`~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.

---

## 1. Comprobaciones previas (bloque obligatorio antes de redactar)

1. **Recurribilidad y órgano** (verificado):
   - Sentencia del **Juez de lo Penal** → apelación ante la **Audiencia Provincial** (art. 790.1).
   - Sentencia del **Juez Central de lo Penal** → **Sala de lo Penal de la AN** (art. 790.1).
   - **Sentencias de las AP o de la Sala de lo Penal de la AN en primera instancia**, y los **autos
     que pongan fin al proceso por falta de jurisdicción o sobreseimiento libre** → apelación ante la
     **Sala de lo Civil y Penal del TSJ** o la **Sala de Apelación de la AN** (**art. 846 ter**,
     verificado), que se rige **por los arts. 790, 791 y 792** (art. 846 ter.3).
2. **Plazo: 10 días** desde la notificación de la sentencia (art. 790.1) — ver § 2, incluida la
   suspensión. **Días inhábiles (art. 183 LOPJ, redacción LO 14/2022, verificado): todo agosto y del
   24 de diciembre al 6 de enero, ambos inclusive**, salvo actuaciones declaradas urgentes por las
   leyes procesales. Margen de seguridad de la casa: presentar con **2 días hábiles** de antelación.
3. **Gravamen** — solo recurre quien resulta perjudicado por el fallo.
4. ⭐ **Protesta previa** — sin protesta no hay motivo:
   - Prueba **indebidamente denegada**: solo se puede reproponer en 2.ª instancia **«siempre que
     hubiere formulado en su momento la oportuna protesta»** (art. 790.3). **Localiza el folio y el
     minutaje de la grabación.**
   - Infracción procesal: hay que **acreditar haber pedido la subsanación en la primera instancia**
     (art. 790.2 párr. 2). Ver § 4.
   - Recuerda que, tras la **LO 1/2025**, la sede natural de las cuestiones previas es la **audiencia
     preliminar del art. 785**, no el inicio del juicio: la protesta que buscas suele estar ahí
     (art. 785.3: no cabe recurso, pero **sí protesta** y reproducción en el recurso contra la
     sentencia). Ver anclas § 2.
5. **Prescripción del delito** (arts. 131 y 133 CP — anclas §§ 3.3 y 3.4).
   > ⭐ **Regla de la casa, verificada (art. 132.2.2.ª CP):** la **querella o denuncia** ante órgano
   > judicial **NO interrumpe** por sí sola la prescripción: **suspende el cómputo un máximo de 6
   > MESES** desde su presentación. Solo interrumpe la **resolución judicial motivada** que atribuya a
   > persona determinada su presunta participación (regla 1.ª). Si dentro de los 6 meses recae esa
   > resolución, la interrupción se retrotrae a la fecha de la querella/denuncia; **si el juez no
   > adopta ninguna** —o recae inadmisión firme—, **el cómputo continúa desde la presentación**.
   > Reconstruye la cronología con folios: entre la denuncia y la primera resolución motivada suele
   > haber meses que nadie ha contado.
6. **Ley penal más favorable (art. 2.2 CP, verificado)**: efecto retroactivo **aunque hubiera recaído
   sentencia firme y el sujeto estuviese cumpliendo condena**; **en caso de duda será oído el reo**.
   Con **dos reformas recientes** (LO 1/2025 y **LO 1/2026**, vigente **10-4-2026**), en todo asunto
   con hechos anteriores al 10-4-2026 **compara penas** y alega la más favorable. Ver anclas §§ 1 y 7.
7. **Posición procesal** — condiciona radicalmente lo que puedes pedir. Ver § 5.

---

## 2. Plazo y ⭐ la suspensión que casi nadie usa (art. 790.1, verificado)

- **10 días** desde la notificación de la sentencia, por **cualquiera de las partes**. Durante ese
  período las actuaciones están en la **Oficina judicial** a disposición de las partes.
- ⭐ **Alargamiento legítimo del plazo:** dentro de los **3 días siguientes a la notificación** se
  puede **solicitar copia de los soportes en los que se hayan grabado las sesiones**, **con
  SUSPENSIÓN del plazo para la interposición del recurso**. El cómputo **se reanuda una vez hayan
  sido entregadas las copias**.
  > **Operativo:** en un asunto con prueba personal extensa, esto es tiempo real de trabajo, gratis y
  > legal. **Pídelo por sistema en los 3 primeros días** si vas a discutir la valoración de la prueba
  > —necesitas el visionado para citar minutajes—. Anota en el expediente: fecha de notificación,
  > fecha de solicitud, fecha de entrega, plazo reanudado.
- **Adhesión (art. 790.1 párr. 2):** la parte que **no** apeló puede **adherirse en el trámite de
  alegaciones del apartado 5** (10 días), ejercitando las pretensiones y motivos que convengan.
  ⚠️ **Queda supeditada a que el apelante mantenga el suyo**: si el apelante desiste, tu adhesión cae.
  Valora si te conviene apelar por derecho propio en vez de adherirte.
- **Impugnación de la adhesión: 2 días**, una vez conferido el traslado del apartado 6.

---

## 3. Motivos (art. 790.2 párr. 1, verificado)

El escrito de formalización se presenta **ante el órgano que dictó la resolución** (*a quo*) y en él
se exponen, **ordenadamente**, las alegaciones sobre:

1. **Quebrantamiento de las normas y garantías procesales.**
2. **Error en la apreciación de las pruebas.**
3. **Infracción de normas del ordenamiento jurídico.**

- ⚠️ **Requisito formal que se olvida:** el recurrente **habrá de fijar un domicilio para
  notificaciones en el lugar donde tenga su sede la Audiencia** (art. 790.2 in fine).
- La apelación penal es de **cognición amplia** — no tiene el corsé de la casación. Aquí **sí** se
  discute la prueba. Aprovéchalo: es la última oportunidad real (ver skill de casación, § 1).

---

## 4. Nulidad por infracción procesal (art. 790.2 párr. 2, verificado)

Si se pide la **declaración de nulidad del juicio** por infracción de normas o garantías procesales
que causaren **indefensión** al recurrente, **en términos tales que no pueda ser subsanada en la
segunda instancia**, hay que —**acumulativamente**—:

1. **Citar las normas legales o constitucionales** que se consideren infringidas;
2. **Expresar las razones de la indefensión** (material y efectiva, no formal);
3. ⭐ **Acreditar haberse pedido la subsanación de la falta o infracción en la primera instancia**,
   **salvo** que se hubieren cometido **en momento en el que fuere ya imposible la reclamación**.

> **El punto 3 es donde mueren estos motivos.** No basta con afirmar que se pidió: hay que
> **acreditarlo** — folio del escrito, acta, o minutaje de la grabación. Si la infracción se produjo
> cuando ya no cabía reclamar (p. ej., se descubre al leer la sentencia), **alega expresamente la
> excepción** y explica por qué la reclamación era imposible. No la des por sobreentendida.

---

## 5. ⭐⭐ El filtro del art. 790.2 párr. 3 — la clave de toda la apelación penal

**Texto verificado (párrafo añadido por la Ley 41/2015, vigente desde 6-12-2015):**

> «Cuando **la acusación** alegue error en la valoración de la prueba para pedir **la anulación de la
> sentencia absolutoria o el agravamiento de la condenatoria**, será preciso que se justifique **la
> insuficiencia o la falta de racionalidad en la motivación fáctica**, **el apartamiento manifiesto de
> las máximas de experiencia** o **la omisión de todo razonamiento sobre alguna o algunas de las
> pruebas practicadas que pudieran tener relevancia o cuya nulidad haya sido improcedentemente
> declarada.»

Y su cierre, el **art. 792.2 (verificado)**: la sentencia de apelación **NO podrá condenar al
encausado absuelto en primera instancia ni agravar la condena** por error en la apreciación de las
pruebas **en los términos del art. 790.2 párr. 3**. **Solo puede anular** y devolver las actuaciones.

**Explícalo en los dos sentidos — es asimétrico:**

### Si defiendes (frente a un recurso de la acusación)
Es tu mejor munición. El recurso de la acusación **no puede limitarse a proponer una valoración
alternativa de la prueba**, por razonable que sea. Debe acreditar un **defecto de racionalidad** de
la motivación. Alega en tu escrito de alegaciones del art. 790.5:
- Que el recurso **no identifica** ninguno de los tres supuestos tasados, sino que se limita a
  discrepar → **no supera el filtro legal**.
- Que la sentencia **sí motivó** los hechos: transcribe el pasaje y el folio.
- Que, **aun en el mejor de los casos para la acusación, el techo del art. 792.2 es la ANULACIÓN, no
  la condena**: el tribunal de apelación **no puede** condenar *ex novo*. Pídelo expresamente.
- Que el estándar no es «hay otra lectura posible», sino que la del juzgador sea **irracional**.

### Si acusas
Asúmelo antes de recurrir y **dilo al cliente**: revertir una absolución es **casi imposible**, y el
máximo alcanzable es que se **anule** el juicio y se repita, no una condena directa. Si aun así se
recurre, **estructura el motivo sobre uno de los tres supuestos tasados** y nómbralo expresamente:
1. **insuficiencia o falta de racionalidad de la motivación fáctica**; o
2. **apartamiento manifiesto de las máximas de experiencia**; o
3. **omisión de todo razonamiento** sobre pruebas relevantes, o **nulidad improcedentemente
   declarada** de una prueba.

Un recurso de acusación que argumenta «la prueba debió valorarse de otro modo» está **muerto al
nacer**. Y en el SUPLICO pide **anulación**, no condena: pedir lo que el art. 792.2 prohíbe delata
que no se ha leído la norma.

> **Límites constitucionales a la revisión de absolutorias por prueba personal (inmediación):**
> existe doctrina consolidada del **TC y del TEDH**, y de la Sala Segunda, sobre la imposibilidad de
> revisar prueba personal sin inmediación. ⛔ **NO la cites de memoria — ni ECLI, ni ROJ, ni fecha, ni
> ponente.** **Verifícala en el momento con `buscar_sentencias` / `buscar_por_cita`** y cita solo lo
> que devuelva el conector. Sin verificación → `[verificar]`.

---

## 6. Prueba en segunda instancia (art. 790.3, verificado)

En el **mismo escrito de formalización** puede pedirse la práctica de las diligencias de prueba:

| Supuesto | Requisito |
|---|---|
| Prueba que **no pudo proponer** en la primera instancia | Justificar la imposibilidad |
| Prueba **propuesta e indebidamente denegada** | ⭐ **Siempre que hubiere formulado en su momento la oportuna PROTESTA** |
| Prueba **admitida y no practicada** | Por **causas que no le sean imputables** |

- **Vista (art. 791, verificado):** si los escritos contienen **proposición de prueba o reproducción
  de la grabada**, el Tribunal resuelve **en 3 días** sobre la admisión y, en su caso, se señala vista.
  También **puede** celebrarse vista, de oficio o a petición de parte, cuando el Tribunal la estime
  **necesaria para la correcta formación de una convicción fundada**. La vista se señala **dentro de
  los 15 días siguientes**; empieza por la práctica de la prueba y la reproducción de las grabaciones,
  y luego las partes resumen oralmente. Grabación conforme al **art. 743**.
- Si la víctima lo ha solicitado, **será informada** aunque no se haya mostrado parte (art. 791.2).

---

## 7. Tramitación (arts. 790.4 a 790.6, verificado)

| Trámite | Plazo |
|---|---|
| Admisión por el Juez; si hay **defecto subsanable**, plazo de subsanación | **≤ 3 días** (790.4) |
| Traslado del escrito de formalización a las demás partes; escritos de alegaciones (y **adhesión**, y petición de prueba del 790.3) | **10 días comunes** (790.5) |
| Traslado de cada escrito a las demás partes y **elevación** de los autos a la Audiencia | **2 días** (790.6) |
| **Sentencia de apelación** | **5 días** tras la vista, o **10 días** desde la recepción de las actuaciones si no hubo vista (792.1) |

---

## 8. Sentencia de apelación (art. 792, verificado)

- **792.2 — *reformatio in peius* y revisión de absolutorias: SUBSISTE la prohibición**, y reforzada.
  No cabe condenar al absuelto ni agravar la condena **por error en la apreciación de las pruebas en
  los términos del art. 790.2 párr. 3**. Sí cabe **anular** (absolutoria o condenatoria) y devolver
  las actuaciones. La sentencia **concretará si la nulidad se extiende al juicio oral** y **si el
  principio de imparcialidad exige una nueva composición del órgano** de primera instancia.
- **792.3:** anulación por **quebrantamiento de forma esencial** → sin entrar en el fondo, se repone
  el procedimiento al momento de la falta, **conservando validez los actos cuyo contenido sería
  idéntico** pese a la falta.
- **792.4:** contra la sentencia de apelación **solo cabe casación en los supuestos del art. 847**
  → recuerda el filtro: contra sentencia de apelación de una **AP**, **solo el art. 849.1.º**. Avisa
  al cliente **ya en la apelación**: lo que no se gane aquí, **no se recupera en casación**.
- **792.5:** la sentencia **se notifica a los ofendidos y perjudicados** aunque no se hayan mostrado
  parte.

---

## 9. Estructura del escrito

1. Encabezamiento **al Juzgado/Tribunal que dictó la sentencia** (para ante la Audiencia Provincial /
   TSJ / Sala de Apelación de la AN, según § 1).
2. Comparecencia; interposición **en plazo** (deja constancia de la suspensión del § 2 si se usó) y
   **designación de domicilio en la sede de la Audiencia** (art. 790.2).
3. Breve relación de antecedentes: sentencia, fallo y **gravamen**.
4. **ALEGACIONES numeradas**, cada una encabezada por su motivo del art. 790.2:
   (i) **quebrantamiento de normas y garantías procesales** (si se pide nulidad → los 3 requisitos
   del § 4, con acreditación de la subsanación pedida);
   (ii) **error en la apreciación de las pruebas**, con designación de particulares, **folio** y
   **minutaje de la grabación** (si acusas → filtro del § 5);
   (iii) **infracción de normas del ordenamiento jurídico** (precepto sustantivo, subsunción,
   circunstancias modificativas, concurso);
   (iv) **individualización de la pena** (arts. 66 y ss. CP) y **responsabilidad civil**.
5. **Prueba en segunda instancia** (art. 790.3) y, en su caso, **solicitud de vista** (art. 791).
6. **SUPLICO**: revocación total o parcial; absolución o modificación de la pena. **Si eres
   acusación: anulación** (art. 792.2), no condena directa. Otrosíes: prueba, vista, costas.
7. Lugar, fecha y firma.

---

## 10. Errores típicos

- ❌ Dejar pasar los **3 días** para pedir las grabaciones y perder la suspensión del plazo (§ 2).
- ❌ Pedir prueba denegada **sin protesta** en su momento (art. 790.3).
- ❌ Pedir nulidad sin **acreditar** que se solicitó la subsanación en primera instancia (790.2 párr. 2).
- ❌ Como acusación, alegar error en la valoración **sin encajarlo en uno de los tres supuestos** del
  790.2 párr. 3 — y **pedir condena** cuando el art. 792.2 solo permite anulación.
- ❌ Confundir la apelación con la casación: aquí **sí** se discute la prueba. No te autolimites.
- ❌ Adherirse cuando interesaba apelar por derecho propio: la adhesión **cae si el apelante desiste**.
- ❌ **No fijar domicilio** en la sede de la Audiencia (art. 790.2).
- ❌ Citar de memoria la doctrina de inmediación sobre absolutorias. Ver § 11.
- ❌ Argumentar sobre folios que no se citan. Sin folio, no se afirma.

---

## 11. Reglas de trabajo

- **Jurisprudencia — verificación obligatoria y PREVIA** con el conector `jurisprudenciator`
  (`buscar_sentencias`, `buscar_por_cita`, `leer_sentencias`): doctrina sobre revisión de la prueba
  en apelación, inmediación y absolutorias. ⛔ **PROHIBIDO inventar o citar de memoria ECLI, ROJ,
  fechas o ponentes.** Sin verificación → `[verificar]`, y decírselo al usuario.
- **Prohibido inventar** artículos, plazos, ordinales o penas. Confirma el precepto sustantivo con
  `buscar_articulo` antes de citarlo.
- **Anclaje al folio.** Toda afirmación de hecho se ancla al **folio de las actuaciones** y, si es
  prueba personal, al **minutaje de la grabación**.
- **Marcadores de datos:** `[ACUSADO]`, `[PERJUDICADO]`, `[VÍCTIMA]`, `[DATO]`. **Nunca datos
  reales**: condenas e infracciones son datos de **categoría especial** (**art. 10 RGPD**). Ver
  `PROTECCION-DATOS.md`.
- **Terminología vigente (art. 14 LECrim, desde el 3-10-2025):** **Sección de lo Penal del Tribunal
  de Instancia** (ya **no** «Juzgado de lo Penal»), Audiencia Provincial, LAJ; nomenclatura de la
  **LO 1/2025** (recuerda: conformidad y cuestiones previas → **art. 785**).
  > ⭐ **En el encabezamiento, copia la denominación exacta de la sentencia que recurres.** Si la
  > sentencia se rotula «Juzgado de lo Penal nº X», ese es el órgano *a quo* que citas al
  > identificarla. Usar la denominación antigua no invalida el recurso (**DA 1.ª LO 1/2025**), pero
  > al describir el órgano por tu cuenta usa la vigente.
- ⛔ **NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. Reforma en tramitación
  (prevista 1-1-2028): **nunca** como Derecho vigente.
- ⛔ **Nada de MASC**: es del orden civil.

## Entrega

Escrito final en **Word `.docx`** (skill `docx`), maquetado para LexNET.
