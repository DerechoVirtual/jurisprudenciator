---
name: interposicion-recurso-contencioso-ca
description: >-
  Redacta el PRIMER escrito del proceso contencioso ordinario —el de interposición del recurso (art. 45 LJCA), que abre el pleito y reclama el expediente— y verifica la admisibilidad antes de presentarlo: plazo, acto impugnable, legitimación, agotamiento de la vía, competencia y documentos del art. 45.2. Activar con "interponer recurso contencioso", "escrito de interposición", "art. 45 LJCA", "llevar esto al juzgado de lo contencioso", "quiero demandar a la Administración", "¿estoy todavía en plazo para recurrir?". El proceso ordinario es de DOBLE ESCRITO: aquí se empieza siempre; la demanda propiamente dicha se redacta después, ya recibido el expediente, con /demanda-contencioso-administrativa.
---

# Escrito de interposición del recurso contencioso-administrativo (art. 45 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo, acto impugnable y documentos del art. 45.2** → `buscar_articulo` (`ley="LJCA"`, artículos 25, 29, 30, 45 y 46).
- **Competencia objetiva antes de encabezar** → `buscar_articulo` (`ley="LJCA"`, artículos 8 a 14).
- **Fecha de publicación de la disposición general impugnada** → `buscar_boe` + `leer_boe` o `sumario_boe` del día.
- **Recurrente persona jurídica o terceros interesados (art. 45.5)** → `buscar_empresa_mercantil` (órgano de administración inscrito; adjudicatario o titular de la licencia).
- **Acto confirmatorio o de trámite cualificado** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Antes de presentar** → `verificar_escrito` sobre el escrito completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

Instrucciones PARA Claude. Fuente única de plazos y umbrales: `references/anclas-normativas-ca.md`.
Lo que no esté allí, verifícalo con `buscar_articulo` o márcalo `[verificar]`. **No inventes nunca**
plazos, letras de artículo ni cifras.

El escrito del art. 45.1 es **sucinto**: cita la disposición, acto, inactividad o vía de hecho que
se impugna y pide que se tenga por interpuesto el recurso. **No es la demanda** — no argumentes el
fondo aquí. Su único riesgo, y es letal, es la **admisibilidad**.

## 1. BLOQUE DE ADMISIBILIDAD — ejecútalo ANTES de redactar una sola línea

No redactes hasta haber contestado las seis preguntas. Si falta un dato, **pídelo**; no lo supongas.

### 1.1 Plazo — art. 46 LJCA (plazos de CADUCIDAD)

Fija el **dies a quo** = **fecha de notificación** (o de publicación, o de producción del silencio).
Pídela expresamente y hazla constar. Sin ella no hay control de plazo posible.

| Supuesto | Plazo | Cómputo desde |
|---|---|---|
| Acto **expreso** que pone fin a la vía | **2 meses** | Día siguiente a la notificación/publicación |
| Acto **presunto** (silencio) | **6 meses** | Día siguiente a producirse el acto presunto |
| Disposición general | **2 meses** | Día siguiente a la publicación |
| Tras **reposición** potestativa (expresa o presunta) | **2 meses** | Día siguiente a la notificación o a la desestimación presunta (**art. 46.4**) |
| **Inactividad** (art. 29) | **2 meses** | Día siguiente al vencimiento de los plazos del art. 29 |
| **Vía de hecho CON requerimiento** del art. 30 | **10 días** | Día siguiente al fin del plazo del art. 30 |
| **Vía de hecho SIN requerimiento** | **20 días** | Día en que se inició la actuación material |
| **Lesividad** | **2 meses** | Día siguiente a la declaración de lesividad |
| Litigios entre Administraciones | **2 meses** | (art. 46.6) |

- ⚠️ **Son plazos de CADUCIDAD, no de prescripción.** **No se interrumpen** con burofax,
  reclamación extrajudicial ni requerimiento. Perdido el plazo, el acto es firme y consentido →
  inadmisibilidad (**art. 69.e LJCA**). Dilo al usuario con estas palabras si viene con un burofax.
- **Agosto — art. 128.2 LJCA:** **no corre ningún plazo de la LJCA**, **salvo en el procedimiento
  de derechos fundamentales, donde agosto SÍ es hábil** (plazo de 10 días, art. 115.1 LJCA). Es la
  trampa clásica. **No cites el art. 133 LEC**: no es la norma aplicable.
- **Inactividad (art. 29):** 29.1 exige **reclamación previa** y **3 meses** sin cumplimiento;
  29.2 (no ejecución de actos firmes) exige petición y **1 mes**, y se tramita por **abreviado**.
- **Vía de hecho (art. 30):** el requerimiento intima la cesación; si no se atiende en **10 días**
  desde su presentación, cabe recurso. Los 10 días del art. 46.3 corren **desde el fin de ese plazo**.

### 1.2 Acto impugnable — art. 25 LJCA

- Disposiciones de carácter general.
- Actos **expresos y presuntos** que **pongan fin a la vía administrativa**, definitivos **o de
  trámite CUALIFICADOS**: que decidan directa o indirectamente el fondo, determinen la imposibilidad
  de continuar el procedimiento, o produzcan **indefensión o perjuicio irreparable**.
- Inactividad (art. 29) y **vía de hecho** (art. 30).

Si es un **trámite no cualificado**, **no lo recurras**: dilo y explica que la oposición se hará
valer contra la resolución final.

### 1.3 Legitimación — art. 19 LJCA

- 19.1.a) **derecho o interés legítimo** — el título ordinario; identifica en qué consiste.
- 19.1.b) corporaciones, asociaciones, sindicatos y grupos del art. 18 para intereses colectivos.
- 19.1.h) **acción popular**, solo en los casos expresamente previstos por las Leyes.
- **19.1.k)** (añadido por **LO 1/2025**, vigente 3-4-2025): **sindicatos** que actúan en nombre e
  interés del **personal funcionario y estatutario** afiliado **que lo autorice**, en defensa de sus
  derechos individuales; los efectos recaen sobre el afiliado. → Activa el **art. 45.2.e)**.
- 19.2 **lesividad**; 19.4 recursos especiales en materia de contratación.

### 1.4 Agotamiento de la vía administrativa

Requisito equivalente funcional del MASC civil (**que aquí NO existe**). Verifica que se interpuso
la **alzada** si era obligatoria, o que el acto agotaba la vía. Si hay **reposición pendiente sin
resolver**, **no se puede interponer** el contencioso (art. 123.2 LPAC).

### 1.5 Competencia objetiva — arts. 8-14 LJCA

Determínala antes de encabezar. Extracto verificado (art. 8): **Juzgados CA** → entidades locales
(excluidas impugnaciones de **planeamiento urbanístico**); CCAA en personal (salvo nacimiento y
extinción de la relación de funcionarios de carrera); **sanciones ≤ 60.000 €** (art. 8.2.b);
**responsabilidad patrimonial de CCAA ≤ 30.050 €** (art. 8.2.c); Administración periférica del
Estado salvo **> 60.000 €** o dominio público, obras públicas, expropiación y propiedades
especiales (art. 8.3); **extranjería**; autorizaciones judiciales del **art. 8.6**. Si el asunto
no encaja con claridad, **verifica el artículo y dilo**; no adivines la Sala.

### 1.6 Documentos del art. 45.2 — la causa de inadmisión más evitable

a) Documento que acredite la **representación** (salvo que conste en otro recurso ante el mismo
   órgano, en cuyo caso pide certificación).
b) Documento que acredite la **legitimación** cuando derive de **transmisión** (herencia u otro título).
c) **Copia o traslado del acto/disposición** impugnado, o indicación del expediente o del diario
   oficial. En inactividad o vía de hecho: órgano o dependencia al que se atribuye y datos que
   identifiquen suficientemente el objeto.
d) ⚠️ **PERSONAS JURÍDICAS — el «acuerdo corporativo».** Documento que acredite el **cumplimiento
   de los requisitos exigidos para entablar acciones** con arreglo a sus normas o estatutos.
   **Es la causa de inadmisión más frecuente y más evitable del orden contencioso.**
   **NO basta el poder para pleitos.** Hace falta acreditar el **acuerdo del órgano competente
   según los estatutos** (consejo de administración, junta, asamblea, presidente si los estatutos
   se lo atribuyen). Salvo que se haya insertado en lo pertinente **dentro del cuerpo del poder**
   (art. 45.2.d in fine) — comprueba si la escritura lo recoge y, si lo recoge, **dilo y cítalo**.
   Ante una persona jurídica, **pregunta siempre por el acuerdo**. No lo des por supuesto.
e) **SINDICATOS ex art. 19.1.k)** — añadido por la **LO 1/2025** (vigente **3-4-2025**): documentos
   que acrediten **(i)** la **afiliación** del personal, **(ii)** la **comunicación del sindicato al
   afiliado** de la voluntad de iniciar el proceso, y **(iii)** la **autorización expresa** del
   afiliado. Los tres. Faltando uno, se requiere subsanación.

**Subsanación: 10 días** (**art. 45.3**); el LAJ examina de oficio la validez de la comparecencia y
requiere la subsanación; si no se subsana, el órgano se pronuncia sobre el **archivo**.

## 2. Vías de iniciación alternativas — no las pases por alto

- **Art. 45.5 — interposición mediante DEMANDA directa:** cuando se recurre una disposición general,
  acto, inactividad o vía de hecho **en que no existan terceros interesados**, el recurso **puede
  iniciarse directamente por demanda** razonando la disconformidad a Derecho, acompañando los
  documentos del art. 45.2. Valóralo: **ahorra una fase completa**. Requiere certeza de que **no
  hay terceros interesados** — si los hay, no lo uses.
- **Art. 45.4 — lesividad:** se inicia **por demanda** (art. 56.1), fijando las personas demandadas,
  acompañando la **declaración de lesividad**, el **expediente** y, en su caso, los documentos de
  las letras a) y d).
- **Abreviado (art. 78.2):** se inicia **por demanda**, no por este escrito. Si el asunto es de
  personal, extranjería, inadmisión de asilo, dopaje o **cuantía ≤ 30.000 €**, **NO uses esta
  skill**: usa `procedimiento-abreviado-ca`. Comprobar esto es lo **primero** que debes hacer.

## 3. Estructura del escrito

1. **Encabezamiento:** «AL JUZGADO DE LO CONTENCIOSO-ADMINISTRATIVO Nº [ÓRGANO] DE [ÓRGANO]» / «A
   LA SALA DE LO CONTENCIOSO-ADMINISTRATIVO DEL [ÓRGANO]».
2. **Comparecencia:** `[CLIENTE]`, representación y **postulación — art. 23 LJCA** (no art. 23 LEC):
   procurador **potestativo** ante **Juzgados** (si se confiere la representación al abogado, a él se
   notifica), **preceptivo** ante **Salas**; abogado siempre. Los **funcionarios públicos** en
   defensa de sus derechos estatutarios pueden comparecer **por sí mismos**.
3. **Acto impugnado:** identificación, `[EXPEDIENTE]`, **fecha de notificación** y mención expresa
   de que se interpone **dentro del plazo del art. 46 LJCA**.
4. **Documentos** que se acompañan, **enumerados por la letra del art. 45.2** que cada uno cubre.
   Hazlo explícito: es la mejor defensa frente al requerimiento de subsanación.
5. **SUPLICO:** que se tenga por interpuesto el recurso, por personada a la parte, y que se
   **reclame el expediente administrativo** al órgano correspondiente (**art. 48 LJCA**).
6. **OTROSÍES:**
   - **Cuantía** (arts. 40-42) — anticípala; determina abreviado y apelabilidad.
   - **Medidas cautelares** (art. 129) — solicitables **en cualquier estado del proceso**, en pieza
     separada (art. 131). Si la ejecución puede **hacer perder al recurso su finalidad legítima**
     (art. 130.1), pídelas **ya**. Cautelarísima del art. 135 si hay especial urgencia. → skill
     `medidas-cautelares-ca`.
   - **Anuncio** de la vía del art. 78 si procede, o solicitud de **acumulación**.

## 4. Errores que pierden el asunto

- **Dejar caducar el plazo creyendo que el burofax lo interrumpe.** No lo interrumpe.
- **Olvidar el acuerdo corporativo del art. 45.2.d).** El error nº 1. El poder no basta.
- **Ignorar el art. 45.2.e)** en recursos sindicales ex art. 19.1.k) — norma nueva (LO 1/2025).
- **Recurrir un acto de trámite no cualificado** (art. 25.1).
- **Impugnar el acto confirmatorio en lugar del originario:** el confirmatorio de un acto firme y
  consentido no es impugnable (**art. 69.c**). Comprueba **cuál** fue el acto originario.
- **Interponer con la reposición pendiente** (art. 123.2 LPAC).
- **Aplicar la regla de agosto al procedimiento de derechos fundamentales** — allí agosto **es hábil**.
- **Errar la competencia objetiva** y perder meses en una Sala que declina.
- **Usar este escrito cuando procede el abreviado** (art. 78.2: se inicia por demanda).

## 5. Cierre

- **Jurisprudencia:** verifica **antes de citar** con `buscar_sentencias` / `buscar_por_cita`.
  Prohibido inventar ECLI, ROJ, fechas o fundamentos.
- **Normativa autonómica y local:** no la cubre el conector. **Pídesela al usuario**; no la cites
  de memoria.
- **Protección de datos:** `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`, `[EXPEDIENTE]`. Nunca
  reproduzcas datos de terceros ni datos de salud (art. 9 RGPD).
- **Nada de MASC:** es del orden civil.
- **Entregable:** Word `.docx` maquetado (skill `docx`). Aplica `estilo-escritos-judiciales`.
- **Avisa del siguiente hito:** recibido y entregado el expediente, la demanda se deduce en
  **20 días** (art. 52.1) → skill `demanda-contencioso-administrativa`. **Es un plazo de caducidad
  del recurso** (art. 52.2). Anótalo en la agenda del asunto **al presentar**, no después.
