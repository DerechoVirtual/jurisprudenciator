---
name: recurso-casacion-penal-catalogo
description: Catálogo (sin plantilla). Prepara e interpone recurso de casación penal ante la Sala Segunda del Tribunal Supremo, determinando primero qué motivos son admisibles según la resolución recurrida (art. 847 LECrim). Actívala ante "recurso de casación penal", "casación por infracción de ley art. 849", "quebrantamiento de forma art. 850/851", "preparar casación", "casación contra sentencia de apelación de la Audiencia Provincial", "recurrir ante el Tribunal Supremo en lo penal", o "¿cabe casación contra esta sentencia?".
---

# Recurso de casación penal (catálogo — sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Motivos admisibles, preparación e interposición** (arts. 847, 849-852, 855, 856 y 874 LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Doctrina de la Sala Segunda sobre el motivo y sus causas de inadmisión** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`; `tipo_resolucion="AUTO"` para las inadmisiones) + `leer_sentencias` con `parrafos=3`.
- **Lista demasiado amplia** → `opciones_busqueda` para acotar por año o ponente.
- **Vulneración de derechos fundamentales por la vía del art. 852** → `buscar_sentencias` (`base="TC"`).
- **ECLI que cita la sentencia recurrida o la parte contraria** → `buscar_por_cita`.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Redacta la preparación y la interposición de la casación penal. **Antes de escribir una sola línea,
determina qué motivos son admisibles.** Es la decisión que decide el recurso.

Consulta `references/anclas-normativas-penal.md` (§ 4) antes de citar plazos o preceptos.
Perfil del despacho: `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.

---

## 1. ⚠️ PASO CERO — los motivos DEPENDEN de la resolución recurrida (art. 847 LECrim)

**Este es el error que más casaciones inadmite.** No existe un catálogo único de motivos: existe el
catálogo que corresponde a la resolución que recurres. Identifica **qué órgano dictó la sentencia y
en qué instancia** antes de nada.

| Resolución recurrida | Motivos admisibles | Cauce |
|---|---|---|
| Sentencias en **única instancia o en apelación** de la **Sala de lo Civil y Penal de los TSJ** | Infracción de ley **Y** quebrantamiento de forma | art. 847.1.a.1.º |
| Sentencias de la **Sala de Apelación de la Audiencia Nacional** | Infracción de ley **Y** quebrantamiento de forma | art. 847.1.a.2.º |
| Sentencias **en apelación de las Audiencias Provinciales** y de la **Sala de lo Penal de la AN** | ⚠️ **SOLO infracción de ley del art. 849.1.º** | art. 847.1.b |

- **art. 847.2:** quedan **exceptuadas** las sentencias que se limiten a declarar la **nulidad** de las
  recaídas en primera instancia. Contra ellas **no cabe casación**: comprueba el fallo antes de
  preparar.

### 🔴 La consecuencia que debes gritar al usuario

Contra una **sentencia de apelación de una Audiencia Provincial** —el supuesto más frecuente en la
práctica— **el único motivo posible es el art. 849.1.º**. **NO caben:**

- ❌ art. 849.2.º (error de hecho basado en documentos)
- ❌ arts. 850 y 851 (quebrantamiento de forma)
- ❌ art. 852 (infracción de precepto constitucional, vía art. 5.4 LOPJ)

Plantear cualquiera de ellos por esa vía → **inadmisión** (art. 884.1.º y 884.2.º). Y no solo del
motivo: arrastra la credibilidad del recurso entero. Si el cliente quiere discutir la prueba o la
presunción de inocencia contra una sentencia de apelación de AP, **dilo con claridad: esa puerta
está cerrada por ley**. La sede para eso era la apelación (art. 790.2), ya agotada.

> **Verifica siempre el encabezamiento de la sentencia recurrida**: órgano, instancia y si el fallo
> se limita a anular. Si la resolución no encaja en ninguna fila de la tabla, **no prepares**: informa
> de que no es recurrible en casación y estudia el incidente de nulidad (art. 241 LOPJ) o el amparo.

---

## 2. Preparación — 5 días (art. 856 LECrim), verificado

- **Plazo: 5 días** desde la **última notificación** de la sentencia, ante el **Tribunal que la
  dictó** (*a quo*), por escrito **autorizado por abogado y procurador**.
- **Contenido (art. 855, verificado — redacción del RD-ley 5/2023, vigente 29-7-2023):**
  1. Pedir **testimonio** de la resolución.
  2. **Manifestar la clase o clases de recurso** que se pretenden utilizar.
  3. ⭐ **Requisito reforzado (párr. 2, añadido en 2023) — casación contra sentencia dictada en
     apelación por AP o Sala de lo Penal de la AN por infracción de ley:** el recurrente **deberá
     presentar escrito consignando, en párrafos separados, con la mayor claridad y concisión, la
     concurrencia de los requisitos exigidos, identificando el precepto o preceptos sustantivos que
     se consideran infringidos y explicando de modo sucinto las razones que fundan tal infracción**.
     La preparación en la vía del 847.1.b **ya no es un trámite formulario**: es un escrito motivado.
     Despacharlo con una frase genérica es un defecto de preparación → inadmisión (art. 884.4.º).
  4. Si se funda en el **849.2.º**: designar, **sin razonamiento alguno**, los particulares del
     documento que muestren el error.
  5. Si se funda en **quebrantamiento de forma**: designar, **sin razonamiento alguno**, la falta o
     faltas cometidas y, en su caso, **la reclamación practicada para subsanarlas y su fecha**.

> Recuerda: los puntos 4 y 5 solo operan cuando el art. 847 permite esos motivos. En la vía 847.1.b
> son inaplicables.

---

## 3. El corsé del art. 849.1.º — respeto íntegro a los hechos probados

El art. 849.1.º (verificado) exige que, **«dados los hechos que se declaren probados»**, se haya
infringido **un precepto penal de carácter sustantivo u otra norma jurídica del mismo carácter que
deba ser observada en la aplicación de la Ley penal**.

**Traducción operativa — el error argumental clásico:**

- El 849.1.º es un debate **exclusivamente jurídico**: se acepta el relato de hechos probados **tal
  como está**, íntegro, sin añadir, quitar ni matizar, y se discute **si la calificación jurídica que
  el tribunal hizo de esos hechos es correcta**.
- **Prohibido**: discutir la prueba, decir «no quedó acreditado», introducir hechos del recurso,
  apoyarse en declaraciones, o pedir que se valore de nuevo un testimonio. Todo eso **es** el motivo
  que no tienes.
- **art. 884.3.º (verificado) — causa expresa de inadmisión:** cuando **no se respeten los hechos que
  la sentencia declare probados** o se hagan **alegaciones jurídicas en notoria contradicción o
  incongruencia con aquéllos** (salvo el 849.2.º, cuando quepa).

**Test antes de presentar:** lee tu motivo y pregúntate si seguiría en pie **aunque los hechos
probados fuesen literalmente ciertos**. Si la respuesta es no, el motivo está mal construido.
Reescríbelo o retíralo.

**Lo que SÍ cabe por el 849.1.º:** error de subsunción (el hecho probado no colma el tipo aplicado o
colma otro más leve), atipicidad, concurso mal resuelto, circunstancias modificativas no apreciadas
**cuyo sustrato fáctico ya conste en los hechos probados**, error en las reglas de determinación de
la pena (arts. 61 y ss. CP), prescripción sobre las fechas del relato, o infracción de norma
sustantiva de la responsabilidad civil.

---

## 4. Motivos — solo cuando el art. 847 los permite

- **849.1.º** — infracción de precepto penal sustantivo. Cita **el precepto concreto** y el **sentido**
  de la infracción (indebida aplicación / inaplicación).
- **849.2.º** — error de hecho **basado en documentos que obren en autos, que demuestren la
  equivocación del juzgador sin resultar contradichos por otros elementos probatorios** (verificado).
  Requisitos de admisión (**art. 884.6.º**, verificado): que el documento **haya figurado en el
  proceso** y que se **designen concretamente las declaraciones** del mismo que se opongan a las de
  la resolución. Documento **literosuficiente**; las declaraciones personales documentadas no son
  «documento» a estos efectos — **verifica el estado de la doctrina con `buscar_sentencias`**.
- **850 y 851** — quebrantamiento de forma. **art. 884.5.º (verificado):** en los casos del art. 850
  es **inadmisible** si la parte **no reclamó la subsanación mediante los recursos procedentes o la
  oportuna protesta**. Sin protesta no hay motivo.
- **852** — infracción de precepto constitucional (vía art. 5.4 LOPJ).

> Verifica el contenido literal de los ordinales del **850** y del **851** con `buscar_articulo`
> antes de invocar uno concreto. **No los cites de memoria.**

---

## 5. Interposición — art. 874 LECrim (verificado)

Escrito firmado por **abogado y procurador autorizado con poder bastante**; **no se admite la
protesta de presentarlo**. Se consignará **en párrafos numerados**, con la mayor concisión y claridad:

1. **1.º** El fundamento o fundamentos doctrinales y legales aducidos como motivo, **encabezados con
   un breve extracto de su contenido**. (El «extracto» no es adorno: es requisito legal.)
2. **2.º** **El artículo de esta Ley que autorice cada motivo** de casación.
3. **3.º** La **reclamación o reclamaciones** practicadas para subsanar el quebrantamiento de forma y
   **su fecha**, si la falta es de las que exigen ese requisito.

- Se acompaña el **testimonio del art. 859** (si fue entregado) y **copia literal** del testimonio y
  del recurso, autorizada por la representación, **para cada una de las demás partes emplazadas**.
- ⚠️ **La falta de presentación de copias produce la desestimación del escrito** y se considera
  comprendida en el **art. 884.4.º**. Comprobar el número de partes emplazadas y contarlas.
- La **adhesión** al recurso se interpone en la misma forma.

---

## 6. Causas de inadmisión — la lista contra la que debes contrastar el escrito

**Art. 884 (verificado) — el recurso SERÁ inadmisible:**

| Ordinal | Causa | Control previo |
|---|---|---|
| 1.º | Interponerse por **causas distintas** de las de los arts. 849 a 851 | ¿Mi motivo tiene cauce legal? |
| 2.º | Contra **resoluciones distintas** de las de los arts. 847 y 848 | ¿Pasa el filtro del § 1? |
| 3.º | **No respetar los hechos probados** o alegaciones en notoria contradicción con ellos | Test del § 3 |
| 4.º | No observar los **requisitos de preparación o interposición** | §§ 2 y 5 (¡copias!) |
| 5.º | En los casos del art. 850, **no haber reclamado la subsanación** o formulado protesta | ¿Consta en acta? |
| 6.º | En el 849.2.º, documento **no obrante en autos** o **sin designación concreta** | Folio exacto |

**Art. 885 (verificado) — PODRÁ inadmitirse:** 1.º cuando **carezca manifiestamente de fundamento**;
2.º cuando el TS **hubiese ya desestimado en el fondo otros recursos sustancialmente iguales**. La
inadmisión **puede afectar a todos los motivos o solo a algunos**.

> Consecuencia estratégica: un motivo inviable no es gratis. Mejor **un motivo sólido** que cuatro,
> tres de ellos inadmisibles.

---

## 7. Comprobaciones previas (bloque obligatorio antes de redactar)

1. **Recurribilidad** — tabla del § 1 + art. 847.2 (¿el fallo se limita a anular?).
2. **Plazo** — 5 días desde la **última** notificación (art. 856). Identifica la fecha de la última,
   no la de la tuya. **Días inhábiles (art. 183 LOPJ, redacción LO 14/2022, verificado): todo agosto y
   del 24 de diciembre al 6 de enero, ambos inclusive**, salvo actuaciones declaradas urgentes por las
   leyes procesales. Margen de seguridad de la casa: presentar con **2 días hábiles** de antelación.
3. **Gravamen** — solo recurre quien resulta perjudicado por el fallo. Sin gravamen no hay recurso.
4. **Protesta previa / reclamación de subsanación** — para 850 (y quebrantamientos): **sin protesta
   documentada en acta no hay motivo** (art. 884.5.º). Localiza el folio y la fecha.
5. **Prescripción del delito** (art. 131 CP) — si los hechos probados y sus fechas la revelan, es
   materia de **849.1.º** puro: no exige tocar el relato. Ver anclas § 3.3.
   > ⭐ **Regla de la casa, verificada (art. 132.2.2.ª CP):** la **querella o denuncia** ante órgano
   > judicial **NO interrumpe** por sí sola la prescripción: **suspende el cómputo un máximo de 6
   > MESES** desde su presentación. Solo interrumpe la **resolución judicial motivada** que atribuya a
   > una persona determinada su presunta participación (regla 1.ª). Si dentro de esos 6 meses recae tal
   > resolución, la interrupción se retrotrae a la fecha de la querella/denuncia; **pero si el juez de
   > instrucción no adopta ninguna** de esas resoluciones en el plazo —o recae inadmisión firme—, **el
   > cómputo CONTINÚA desde la fecha de presentación**, como si nada. Revisa siempre esa ventana de 6
   > meses sobre los hechos probados: es prescripción ganada que casi nadie mira, y por el 849.1.º
   > entra sin tocar el relato.
6. **Ley penal más favorable (art. 2.2 CP, verificado)** — tiene **efecto retroactivo aunque hubiera
   recaído sentencia firme y el sujeto estuviese cumpliendo condena**; **en caso de duda será oído el
   reo**. Con **dos reformas recientes** (LO 1/2025 y **LO 1/2026**, vigente 10-4-2026), en todo
   asunto con hechos anteriores al 10-4-2026 hay que **comparar penas**. Ver anclas §§ 1 y 7.
7. **Postulación** — procurador ante el TS y letrado.

---

## 8. Estructura del escrito de interposición

1. Encabezamiento **a la Sala Segunda del Tribunal Supremo** (previa preparación ante el *a quo*).
2. Comparecencia: procurador ante el TS y letrado; poder bastante.
3. Breve extracto de **antecedentes procesales** (órgano, instancia, fecha, fallo) — deja acreditado
   de un vistazo **por qué cabe casación y por qué vía del art. 847**.
4. **MOTIVOS numerados**, cada uno con: **breve extracto** (art. 874.1.º) → **cauce legal invocado**
   (art. 874.2.º) → precepto sustantivo infringido y sentido de la infracción → desarrollo,
   **partiendo literalmente del hecho probado** (transcríbelo) → petición.
5. En el 849.2.º (cuando quepa): designación literal del documento, **folio** y particulares.
6. **SUPLICO**: que se case y anule la sentencia y se dicte **segunda sentencia** conforme a Derecho,
   con el pronunciamiento concreto que se interesa (absolución, subsunción alternativa, pena que
   proceda). Otrosíes: costas; en su caso, vista.
7. Lugar, fecha y firma.

---

## 9. Errores típicos (revisa el borrador contra esta lista)

- ❌ Plantear 849.2.º, 850/851 o 852 contra sentencia de apelación de una **AP**. → **Inadmisión.**
- ❌ Preparar en la vía 847.1.b con escrito genérico, sin identificar el precepto sustantivo ni
  razonar la infracción (art. 855 párr. 2).
- ❌ Argumentar el 849.1.º peleando la prueba o negando los hechos probados (art. 884.3.º).
- ❌ Invocar el 850 sin protesta documentada (art. 884.5.º).
- ❌ 849.2.º con documento no obrante en autos, sin designación de particulares, o sobre
  declaraciones personales.
- ❌ No presentar copias para todas las partes emplazadas (art. 874 in fine + 884.4.º).
- ❌ Recurrir una sentencia que **solo anula** la de instancia (art. 847.2).
- ❌ Acumular motivos débiles: activa el art. 885.1.º y contamina el recurso.
- ❌ Citar jurisprudencia de memoria. Ver § 10.

---

## 10. Reglas de trabajo

- **Jurisprudencia — verificación obligatoria y PREVIA.** En casación la doctrina de la **Sala Segunda
  es todo**, y por eso aquí el riesgo de inventar es máximo. **PROHIBIDO citar ECLI, ROJ, fecha o
  ponente que no venga de una consulta viva** a `buscar_sentencias` / `buscar_por_cita` /
  `leer_sentencias` (conector `jurisprudenciator`). Nunca de memoria. Sin verificación → `[verificar]`
  y decírselo al usuario.
- **Prohibido inventar** artículos, ordinales, plazos o penas. Los ordinales del 849, 850 y 851 se
  confunden con facilidad: **compruébalos con `buscar_articulo`** antes de citarlos.
- **Anclaje al folio.** Toda afirmación sobre lo actuado (protesta, documento, notificación) se ancla
  al **folio de las actuaciones**. Sin folio, no se afirma.
- **Marcadores de datos:** `[ACUSADO]`, `[PENADO]`, `[VÍCTIMA]`, `[DATO]`. **Nunca datos reales**: los
  antecedentes penales y las condenas son datos de **categoría especial** (**art. 10 RGPD**). Ver
  `PROTECCION-DATOS.md`.
- **Terminología vigente:** Tribunal Supremo, Sala Segunda; Tribunal de Instancia; LAJ; nomenclatura
  de la LO 1/2025.
- ⛔ **NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. La reforma está en
  tramitación (prevista 1-1-2028): **nunca** como Derecho vigente.
- ⛔ **Nada de MASC**: es del orden civil, no del penal.

## Entrega

Escrito final en **Word `.docx`** (skill `docx`), maquetado para LexNET.
