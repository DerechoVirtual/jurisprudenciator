---
name: querella-catalogo
description: >-
  Catálogo (sin plantilla). Redacta querellas conforme a los arts. 270-281 LECrim ante la Sección de Instrucción del Tribunal de Instancia. Actívala ante "presentar querella", "querella criminal", "interponer querella", "querellarse contra", "acusación popular", "ejercer la acción popular", "poder especial para querellarse", "fianza del querellante", "diferencia entre querella y denuncia", "me han admitido/inadmitido la querella", "recurso contra la inadmisión de la querella". Requisito previo: la causa penal NO está iniciada y hay que incoarla con este escrito. Si ya existe un procedimiento en marcha (denuncia, atestado o querella de otro) y la víctima solo quiere mostrarse parte en él, usar /personacion-acusacion-particular-catalogo.
---

# Querella (catálogo — sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Requisitos, fianza y admisión** (arts. 270-281 y 312-313 LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Tipo y pena del delito querellado** → `buscar_articulo` (`ley="CP"`), en la redacción vigente a la fecha de los hechos.
- **Límite jurisprudencial de la acusación popular** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Querellada persona jurídica o sus administradores** → `buscar_empresa_mercantil`; para fechar un acto societario, `sumario_borme` → `leer_boe`.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Construye la querella desde el marco legal: no hay plantilla del despacho. Orden de trabajo:
**comprobaciones previas → decisión querella/denuncia → escrito**.

---

## Lo primero: ¿querella o denuncia? — decide y explícalo

| | **Denuncia** | **Querella** |
|---|---|---|
| **Posición** | El denunciante **NO es parte**. Pone el hecho en conocimiento y queda fuera | El querellante **ES parte** desde la admisión |
| **Postulación** | **Sin** procurador ni abogado preceptivos | **Procurador con poder bastante + abogado** (art. 277 LECrim, verificado) |
| **Poder** | No | **Poder especial** para querellarse (ver § poder) |
| **Contenido** | Libre, sin requisitos tasados | **Requisitos tasados del art. 277** |
| **Fianza** | No | Sí para el **acusador popular** (art. 280), con las **excepciones del 281** |
| **Control de admisión** | Art. 269 LECrim | Arts. 312-313 LECrim |
| **Efecto** | No da derecho a intervenir ni a recurrir como parte | Permite proponer diligencias, intervenir y **recurrir** |

> **Regla de decisión.** Si el cliente quiere **controlar la instrucción** —proponer diligencias,
> intervenir, recurrir el archivo— necesita **ser parte**: querella, o denuncia + personación
> posterior. Si solo quiere que los hechos se investiguen, la denuncia basta y es más barata y rápida.
> **Explícale el coste real** de la querella (procurador, poder notarial especial, eventual fianza) y
> decide con él. Alternativa frecuente y más eficiente: **denunciar y personarse después** como
> acusación particular → `personacion-acusacion-particular-catalogo`.

---

## Bloque previo de comprobaciones (OBLIGATORIO)

1. **Fecha de los hechos → redacción del CP aplicable (art. 2 CP).** Irretroactividad (2.1); **ley más
   favorable con efecto retroactivo** (2.2). Con dos reformas penales en 2025-2026 (LO 1/2025 y **LO
   1/2026**, vigente **10-4-2026**), esto **no es teórico**: en hechos anteriores al 10-4-2026,
   **compara redacciones**. Ver `references/anclas-normativas-penal.md` § 1 y § 7.
2. **Prescripción del delito (art. 131 CP, verificado):** 20 años (prisión máx. ≥ 15) · 15 (inhab. > 10
   o prisión > 10 y < 15) · 10 (prisión o inhab. > 5 y ≤ 10) · **5 años los demás delitos** · **1 año
   los delitos leves y las injurias y calumnias**. Pena compuesta → la que exija **mayor** tiempo
   (131.2). Concurso o conexas → plazo del **delito más grave** (131.4). Imprescriptibles: 131.3.
   - **Cómputo (art. 132.1 CP, verificado):** desde la comisión; **delito continuado** → desde la
     **última infracción**; permanente → desde que cesó la situación ilícita. Reglas especiales de
     *dies a quo* diferido cuando la **víctima es menor de 18 años** (mayoría de edad; o **35 años** en
     tentativa de homicidio, lesiones de los arts. 149-150, maltrato habitual del 173.2, **delitos
     contra la libertad sexual** y **trata**). **Verifica el supuesto concreto en el art. 132.1 antes
     de aplicarlo.**
   - **🚨 Art. 132.2 CP (verificado) — LA QUERELLA NO INTERRUMPE POR SÍ SOLA:**
     - **Interrumpe** que el procedimiento **se dirija contra la persona indiciariamente responsable**,
       es decir (regla **1.ª**) que se dicte **resolución judicial motivada** atribuyéndole su presunta
       participación.
     - **«La presentación de querella o la denuncia formulada ante un órgano judicial… SUSPENDERÁ el
       cómputo de la prescripción por un plazo MÁXIMO DE SEIS MESES**, a contar desde la misma fecha de
       presentación» (regla **2.ª**, literal).
     - Si **dentro de los 6 meses** recae resolución de la regla 1.ª → interrupción **retroactiva** a la
       fecha de la querella.
     - **Si recae inadmisión firme, o el juez no adopta ninguna resolución en 6 meses → el cómputo
       CONTINÚA desde la fecha de presentación.**
     - **132.3:** la persona debe quedar **suficientemente determinada** en la resolución (identificación
       directa, o datos que permitan concretarla en el seno de la organización o grupo).
     > **Operativo:** presentar la querella **no para el reloj**. Con prescripción próxima, **vigila los
     > 6 meses**, pide expresamente resolución motivada dirigiendo el procedimiento contra
     > `[QUERELLADO]`, e **impulsa**. Y ojo: si la querella **se inadmite** (art. 313), la suspensión
     > **decae con efecto retroactivo** — puedes encontrarte con el delito prescrito.
3. **Competencia (art. 14 LECrim, verificado, vigente 3-10-2025):** instruye la **Sección de
   Instrucción del Tribunal de Instancia del partido en que el delito se hubiere cometido** (14.2);
   o las Secciones de **violencia sobre la mujer** / **violencia contra la infancia y la adolescencia**
   (14.5 y 14.6), o el **Juez Central de Instrucción**. **Art. 14.7: si los hechos pudieran ser
   conocidos por ambas Secciones de violencia, la competencia es en todo caso de la de violencia sobre
   la mujer.** Aforamientos → verifica el órgano (art. 57 LOPJ y ss.) antes de dirigir la querella.
   ⚠️ La querella **se inadmite** si el órgano no se considera competente (art. 313).
4. **Naturaleza del delito — determina si la querella es NECESARIA o solo conveniente:**
   - **Públicos** (la mayoría): de oficio. Basta denuncia; la querella es **opcional**, para ser parte.
   - **Semipúblicos**: exigen **denuncia del ofendido** como requisito de procedibilidad (p. ej. art.
     **152.2 in fine CP**, verificado: las lesiones por **imprudencia menos grave** «solo será[n]
     perseguible[s] mediante denuncia de la persona agraviada o de su representante legal»). Sin
     denuncia del ofendido → no cabe proceder. **Art. 105.2 LECrim (verificado):** en delitos
     perseguibles a instancia de la agraviada **también podrá denunciar el Ministerio Fiscal** si
     fuere **menor de edad, persona con discapacidad necesitada de especial protección o desvalida**;
     y **la ausencia de denuncia no impedirá la práctica de diligencias a prevención**.
   - **Privados** (injurias y calumnias contra particulares): **solo por QUERELLA del ofendido**, y con
     **acto de conciliación previo (art. 804 LECrim)**. Aquí la querella **no es opcional: es la única
     vía**. **Verifica los arts. 804 y 805 LECrim con `buscar_articulo`** antes de redactar.
   - **Art. 105.1 LECrim (verificado):** el Ministerio Fiscal debe ejercitar todas las acciones penales
     procedentes, haya o no acusador particular, **«menos aquellas que el Código Penal reserva
     exclusivamente a la querella privada»**.
   > **Comprueba siempre la naturaleza del tipo concreto con `buscar_articulo`.** Equivocarse aquí es
   > fatal: una querella por delito privado sin conciliación previa se inadmite; una denuncia en delito
   > privado no abre nada.
5. **Legitimación** (ver § siguiente) y **fianza** (§ correspondiente).
6. **Postulación:** procurador con poder bastante + abogado. **Poder especial** para querellarse.

---

## Legitimación — quién puede querellarse

**Art. 101 LECrim (verificado):** «La acción penal es pública. Todos los ciudadanos españoles podrán
ejercitarla con arreglo a las prescripciones de la Ley.»

**Art. 270 LECrim (verificado):** «Todos los ciudadanos españoles, hayan sido o no ofendidos por el
delito, pueden querellarse, ejercitando la **acción popular** establecida en el artículo 101.»
También pueden querellarse los **extranjeros** por los delitos cometidos contra sus personas o bienes
o los de sus representados, previo cumplimiento del **art. 280**, si no estuvieren comprendidos en el
**último párrafo del 281**.

**Art. 125 CE** — fundamento constitucional de la acción popular.

**⭐ Art. 105.3 LECrim — NOVEDAD LO 1/2026 (vigente 10-4-2026), verificado literalmente:**
> «Sin perjuicio de lo establecido en los apartados anteriores, **las entidades locales podrán ejercer
> la acción penal por los delitos de hurto** previstos en el capítulo I del título XIII del libro II
> de la Ley Orgánica 10/1995, de 23 de noviembre, del Código Penal.»
- Legitimación **nueva y específica**. Tiene rango de **ley ordinaria** (DF 3.ª LO 1/2026).
- **Solo hurto** (capítulo I del título XIII del libro II CP), no robo ni otros patrimoniales.
- Si el cliente es un **ayuntamiento** o entidad local y el asunto es hurto, esta es su vía directa:
  no necesita construir su legitimación por la acción popular general.

**Art. 109 bis.3 II LECrim (verificado):** cuando el delito tenga por finalidad **impedir u
obstaculizar a los miembros de las corporaciones locales el ejercicio de sus funciones públicas**,
puede personarse la **Administración local** en cuyo territorio se cometió el hecho.

**Art. 109 bis.3 I LECrim (verificado):** la acción penal puede ejercitarla también **asociaciones de
víctimas** y **personas jurídicas** a las que la ley reconoce legitimación para defender los derechos
de las víctimas, **siempre que lo autorice la víctima**.

### Acusación popular y su límite jurisprudencial

- El art. 101 LECrim reconoce la acción popular a **todos los ciudadanos españoles**, ofendidos o no.
- **⚠️ Existe una doctrina jurisprudencial restrictiva sobre el alcance de la acusación popular**
  —singularmente sobre si puede, **por sí sola y sin acusación del Fiscal ni del acusador particular**,
  sostener la apertura del juicio oral en el procedimiento abreviado (art. 782.1 LECrim)—, y sobre sus
  **excepciones**. Es doctrina **matizada y evolutiva**.
- ⛔ **NO la afirmes de memoria ni cites resolución alguna sin comprobarla.** **Instrucción:** antes de
  fundar cualquier estrategia en la acusación popular, **búscala con `buscar_sentencias`** (TS, Sala
  Segunda) y **verifica cada cita con `buscar_por_cita`**. Informa al usuario del **estado actual** de
  la doctrina y de su **incidencia concreta** en el asunto. Si no puedes verificarla, **márcalo
  `[verificar]` y dilo**.
- Consecuencia práctica que **sí** debes advertir: quien solo puede ejercer la **acción popular** está
  en posición **más débil** que el ofendido. Si el cliente **es** perjudicado, ejercítala como
  **acusación particular** (arts. 109-110), no como popular: se ahorra la fianza (art. 281.1.º) y evita
  el debate sobre el límite.

---

## Requisitos del art. 277 LECrim — VERIFICADO, transcritos

> «La querella se presentará **siempre por medio de Procurador con poder bastante y suscrita por
> Letrado**. Se extenderá en papel de oficio, y en ella se expresará:»

| Ord. | Contenido literal | Cómo cumplirlo |
|---|---|---|
| **1.º** | «El Juez o Tribunal ante quien se presente» | Órgano competente **determinado** (art. 14). Encabezamiento |
| **2.º** | «El nombre, apellidos y **vecindad** del querellante» | `[QUERELLANTE]` — **vecindad**, no solo domicilio |
| **3.º** | «El nombre, apellidos y **vecindad** del querellado» | `[QUERELLADO]`. **Si se ignoran**: el art. 277 permite «hacer la designación del querellado **por las señas que mejor pudieran darle a conocer**» — úsalo, no inventes identidad |
| **4.º** | «La **relación circunstanciada del hecho**, con expresión del **lugar, año, mes, día y hora** en que se ejecutó, **si se supieren**» | El requisito más incumplido. **Fecha y hora** cuando consten; si no, dilo («si se supieren» lo ampara) |
| **5.º** | «Expresión de las **diligencias** que se deberán practicar para la **comprobación del hecho**» | **No es opcional**: enumérala. Es requisito de forma |
| **6.º** | «La **petición de que se admita** la querella, se practiquen las diligencias indicadas, se proceda a la **detención y prisión** del presunto culpable o a exigirle **fianza de libertad provisional**, y se acuerde el **embargo de sus bienes** en la cantidad necesaria **en los casos en que así proceda**» | Contenido del SUPLICO. Pide detención/prisión/embargo **solo si procede**: pedirlo por inercia desacredita |
| **7.º** | «La **firma del querellante** o la de otra persona a su ruego si no supiere o no pudiere firmar **cuando el Procurador no tuviese poder especial para formular la querella**» | ⭐ Lee bien: la firma del querellante se exige **cuando el procurador NO tiene poder especial**. **Con poder especial, basta la firma del procurador y del letrado.** |

> **Consecuencia del 7.º — el punto del poder.** El art. 277 exige «poder **bastante**» y condiciona la
> firma personal del querellante a que el procurador **no tenga poder especial**. La práctica
> consolidada es otorgar **poder especial notarial para querellarse** (que además identifica los hechos
> o el querellado): evita el defecto y la exigencia de firma. **Recábalo siempre** y adviértelo al
> cliente como coste y trámite previo. Si no lo hay, **el querellante debe firmar la querella**.

---

## Fianza de la acción popular — arts. 280 y 281 LECrim (VERIFICADOS)

**Art. 280 (literal):** «El **particular querellante** prestará **fianza de la clase y en la cuantía
que fijare el Juez o Tribunal** para responder de las resultas del juicio.»
- La ley **no fija cuantía ni clase**: es **discrecional y motivada** del órgano.
- Fin: responder de las resultas del juicio.

**Art. 281 (literal, redacción Ley 4/2015, vigente 28-10-2015) — EXENTOS de fianza:**
1. **«El ofendido y sus herederos o representantes legales.»** ← **La excepción clave.** Si el cliente
   es el ofendido, **no presta fianza**. Alégalo expresamente en un OTROSÍ.
2. **«En los delitos de asesinato o de homicidio**, el **cónyuge** del difunto o persona vinculada por
   análoga relación de afectividad, los **ascendientes y descendientes** y sus **parientes colaterales
   hasta el segundo grado** inclusive, los **herederos de la víctima** y **los padres, madres e hijos
   del delincuente**.»
3. **«Las asociaciones de víctimas y las personas jurídicas a las que la ley reconoce legitimación
   para defender los derechos de las víctimas siempre que el ejercicio de la acción penal hubiera sido
   expresamente autorizado por la propia víctima.»**

**Párrafo final (literal):** «La exención de fianza **no es aplicable a los extranjeros** si no les
correspondiere en virtud de **tratados internacionales** o por el **principio de reciprocidad**.»

> **Operativo:** identifica en qué casilla está tu cliente **antes** de redactar.
> - **Ofendido** → exento (281.1.º). Alégalo.
> - **Acusador popular no ofendido** → **fianza** (280). Advierte del coste y de que la cuantía la fija
>   el órgano: no prometas importes.
> - **Extranjero** → art. 270 II + último párrafo del 281: comprueba **tratado o reciprocidad**.
> - **Asociación de víctimas / persona jurídica legitimada** → exenta **solo con autorización expresa
>   de la víctima** (281.3.º) — recábala y acompáñala como documento.

---

## Estructura del escrito

1. **Encabezamiento:** «A LA SECCIÓN DE INSTRUCCIÓN DEL TRIBUNAL DE INSTANCIA DE [PARTIDO] QUE POR
   REPARTO CORRESPONDA» (art. 14 LECrim, LO 1/2025). ← requisito **277.1.º**
2. **Comparecencia:** procurador `[PROCURADOR]` en nombre de `[QUERELLANTE]`, con **poder especial**
   para querellarse que se acompaña, y letrado/a director/a. Fórmula: «formula **QUERELLA** por delito
   de [tipo] del art. [X] CP contra `[QUERELLADO]`».
3. **I. ÓRGANO COMPETENTE** — art. 277.1.º. Razona la competencia (art. 14 LECrim) y el punto de
   conexión territorial. **No lo des por supuesto**: el art. 313 permite inadmitir por incompetencia.
4. **II. QUERELLANTE** — art. 277.2.º: nombre, apellidos y **vecindad**. Legitimación (ofendido /
   acción popular / art. 105.3 / art. 109 bis.3).
5. **III. QUERELLADO** — art. 277.3.º: nombre, apellidos y **vecindad**; o **designación por señas** si
   se ignoran. Si es persona jurídica: `[ENTIDAD]`, `[CIF]`, domicilio social, y razona el **art. 31
   bis CP** (**verifícalo con `buscar_articulo`**).
6. **IV. RELACIÓN CIRCUNSTANCIADA DE HECHOS** — art. 277.4.º: numerada y **cronológica**, con **lugar,
   año, mes, día y hora** («si se supieren»). Un hecho por ordinal. **Cada hecho anclado a su folio o
   documento.**
7. **V. CALIFICACIÓN JURÍDICA PROVISIONAL:** tipo penal **con artículo verificado**; subsunción
   elemento por elemento; grado de ejecución; autoría/participación **individualizada** (autor,
   cooperador necesario, cómplice) con actos concretos de cada querellado; concursos.
8. **VI. DILIGENCIAS QUE SE SOLICITAN** — art. 277.5.º: **requisito de forma, no adorno**. Enumeradas,
   con su **relevancia** para la comprobación del hecho. → `solicitud-diligencias-instruccion-catalogo`.
9. **VII. RESPONSABILIDAD CIVIL** y, en su caso, **MEDIDAS CAUTELARES** (personales y reales) — art.
   277.6.º.
10. **DOCUMENTOS:** poder especial, acreditación de la legitimación, prueba documental numerada.
11. **SUPLICO** — art. 277.6.º: admisión a trámite, **tenerle por parte querellante**, incoación,
    práctica de las diligencias y, **si procede**, medidas cautelares.
12. **OTROSÍES:** exención de fianza (art. 281.1.º) o su ofrecimiento (art. 280); designación de
    domicilio a efectos de notificaciones; copias.
13. **FIRMA:** procurador y letrado; **y del querellante si el procurador no tiene poder especial**
    (art. 277.7.º).

> **Anclaje al folio — regla innegociable.** Todo hecho afirmado se ancla al **folio de las
> actuaciones** o al **documento** que se acompaña. Sin actuaciones aún, ancla al documento nº X. Un
> hecho sin ancla no sostiene un indicio racional.

---

## Admisión, inadmisión y recursos

- **Art. 312 LECrim** — admisión y práctica de las diligencias. **Verifícalo con `buscar_articulo`
  antes de citar su tenor.**
- **Art. 313 LECrim (VERIFICADO, literal):** «**Desestimará** en la misma forma la querella **cuando los
  hechos en que se funde no constituyan delito, o cuando no se considere competente** para instruir el
  sumario objeto de la misma. **Contra el auto a que se refiere este artículo procederá el recurso de
  apelación, que será admisible en ambos efectos.**»
  > **Dos causas tasadas, y solo dos:** (a) atipicidad y (b) incompetencia. **No** cabe inadmitir por
  > falta de indicios suficientes o por «insuficiencia probatoria»: eso es materia de instrucción. Si
  > el auto inadmite por otro motivo, **es un argumento de recurso**: alégalo.
  > **Y ojo al régimen:** contra el auto del **313** la apelación es **en ambos efectos**, régimen
  > propio que **no** es el general del art. 766 LECrim. No los confundas.
- **Régimen general de recursos contra autos (art. 766 LECrim, verificado):** caben **reforma** y
  **apelación**; la apelación puede interponerse **subsidiariamente con la reforma o por separado**, y
  **«en ningún caso será necesario interponer previamente el de reforma para presentar la apelación»**
  (766.2). **Plazo de apelación: 5 días** desde la notificación del auto recurrido o del resolutorio de
  la reforma (766.3). Traslado a las demás partes: 5 días comunes.
- **Subsanación:** si la inadmisión se basa en un **defecto formal del art. 277** (p. ej. falta de
  poder especial o de firma), lo procedente suele ser **subsanar y volver a presentar**, no recurrir.
  Valóralo con el usuario.
- **Si se inadmite por atipicidad**, el recurso debe combatir **la subsunción**, no los hechos.

---

## Errores típicos que hunden la querella

1. **Presentarla sin poder especial** y **sin la firma del querellante** → defecto del art. 277.7.º.
2. **Omitir las diligencias** (277.5.º): es **requisito de forma**, no una sección optativa.
3. **Omitir la vecindad** del querellante o del querellado (277.2.º y 3.º).
4. **No expresar lugar, año, mes, día y hora** de los hechos, pudiendo hacerlo (277.4.º).
5. **Inventar la identidad del querellado** en vez de designarlo **por señas**, como permite el 277.3.º.
6. **Pedir detención, prisión o embargo por inercia**, sin que proceda (277.6.º: «en los casos en que
   así proceda»). Desacredita el escrito entero.
7. **Ejercer la acción popular siendo ofendido**: pierdes la exención de fianza del 281.1.º y te metes
   en el debate del límite jurisprudencial **sin necesidad**.
8. **No ofrecer ni discutir la fianza** cuando se actúa como popular (280).
9. **Querella por delito privado sin acto de conciliación previo** (art. 804 LECrim — **verifícalo**).
10. **Confundir el régimen de recursos**: la apelación del art. 313 es **en ambos efectos**.
11. **Dirigirla a un órgano incompetente** → inadmisión directa (313).
12. **Creer que la querella interrumpe la prescripción.** No: **suspende 6 meses** (art. 132.2.2.ª CP).
    Y si se inadmite, la suspensión **decae retroactivamente**.
13. **Afirmar de memoria la doctrina de la acusación popular.** ⛔ Verifícala.
14. **Citar jurisprudencia sin conector.** ⛔ Prohibido.

---

## Datos personales — categoría reforzada

- Marcadores obligatorios: `[QUERELLANTE]`, `[QUERELLADO]`, `[TESTIGO]`, `[ENTIDAD]`, `[CIF]`,
  `[DOMICILIO]`, `[IMPORTE]`, `[PROCURADOR]`. **Nunca datos reales de terceros en la salida.**
- ⚠️ Los datos de **infracciones y condenas penales** son **categoría especial del art. 10 RGPD**.
  Cuidado extremo con **menores** y **víctimas**. La querella **identifica nominalmente a un
  querellado**: es el escrito con mayor riesgo reputacional del plugin.
- Slug del expediente: `descriptor-delito-año`. **Nunca con el nombre del cliente**
  (`PROTECCION-DATOS.md`).

---

## Reglas de trabajo

- **Cifras y artículos:** fuente única `references/anclas-normativas-penal.md` (§ 9) o verificación en
  el momento con **`buscar_articulo`**. ⛔ **Prohibido inventar** artículos, ordinales, plazos o penas.
  Lo no verificable → **`[verificar]`** y **dilo**.
- **Jurisprudencia:** solo vía `buscar_sentencias` / `buscar_por_cita` / `leer_sentencias`. ⛔ Nunca de
  memoria.
- **Instruye el Juez de Instrucción** (Sección de Instrucción del Tribunal de Instancia). ⛔ **No existe
  el «fiscal instructor»**: reforma en tramitación (prevista 1-1-2028), **no es Derecho vigente**. No
  la menciones, ni cites un «art. 4 bis EOMF».
- ⛔ **Nada de MASC**: es del orden **civil**. En penal lo más próximo es el **acto de conciliación del
  art. 804 LECrim** en injurias y calumnias.
- ⚠️ **Sigla ambigua:** «Ley 4/2015» a secas resuelve en el conector a la *Ley de mejora de la
  estructura territorial agraria de Galicia*. El **Estatuto de la víctima** es la **Ley 4/2015, de 27
  de abril** (BOE-A-2015-4606): búscala por su **nombre completo**.

## Entrega

Escrito final en **Word `.docx`** con la skill **`docx`**, maquetado como querella (encabezamiento,
apartados I-VII, suplico, otrosíes, firmas), listo para **LexNET**.
