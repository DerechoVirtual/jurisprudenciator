---
name: denuncia-derechos-trabajadores
description: >-
  Redacta denuncias que INICIAN el proceso penal por delito contra los derechos de los trabajadores y siniestralidad laboral (arts. 311-318 CP), en su caso en concurso con lesiones u homicidio imprudentes. Actívala ante "denuncia por accidente laboral", "accidente de trabajo", "siniestro laboral", "falta de medidas de seguridad", "delito contra la seguridad de los trabajadores", "riesgo grave para la vida del trabajador", "caída de altura", "acta de la Inspección de Trabajo", "responsabilidad del contratista o subcontratista", "coordinador de seguridad", "recargo de prestaciones", "concurso con lesiones imprudentes", "art. 316", "art. 317", "explotación laboral", "trabajadores sin alta en la Seguridad Social", o cuando un trabajador resulte lesionado o fallecido por defectos de prevención. Es el escrito de ARRANQUE, antes de que haya instrucción: si la causa ya está incoada e instruida y toca calificar y pedir la apertura del juicio oral, usar /escrito-acusacion-accidente-laboral.
---

# Denuncia por delito contra los derechos de los trabajadores

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Tipos y penas** (arts. 311-318 CP) **y delito de resultado** (arts. 142 y 152 CP) → `buscar_articulo` (`ley="CP"`).
- **Norma de prevención infringida** (el tipo es norma penal en blanco) → `buscar_articulo` (`ley="LPRL"`); para reglamentos de seguridad, localízalos con `buscar_boe` y usa su ID BOE.
- **Convenio colectivo del sector** (formación, recursos preventivos, condiciones que protege el art. 311 CP) → `buscar_convenio` (sector y territorio) → `leer_convenio` (`buscar_en="formación"` o `articulo`) y `vigencia_convenio` a la fecha de los hechos.
- **Empresa empleadora, contratas y administradores** → `buscar_empresa_mercantil` por denominación o CIF (estado, administradores y apoderados), base para la imputación del art. 318 CP.
- **Deslinde 316/317 y responsabilidad de encargados y administradores** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`; `base="AN"` con `tipo_organo="AP"` para la Audiencia de la provincia) + `leer_sentencias` con `parrafos=3`.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Redacta la denuncia penal por delito contra los derechos de los trabajadores, típicamente por
**siniestro laboral**. Orden: **comprobaciones previas → deslinde 316/317 y sujetos responsables →
escrito**.

---

## Bloque previo de comprobaciones (OBLIGATORIO)

1. **¿Hay RESULTADO lesivo o solo RIESGO?** Es la primera bifurcación y condiciona todo:
   - **Solo riesgo grave** (sin lesión) → **art. 316** (o 317) **aislado**. Es delito de **peligro
     concreto**: se consuma **sin** resultado. Muchos abogados creen que sin lesión no hay delito.
     **Lo hay.**
   - **Con lesión o muerte** → **concurso** entre el delito de peligro y el de resultado (§ concursos).
2. **Fecha de los hechos → ley aplicable (art. 2 CP, verificado).** 2.1 irretroactividad; **2.2 ley más
   favorable retroactiva**. Los arts. 316-318 **no** fueron tocados por la LO 1/2026, pero **el art.
   152 CP sí tiene redacción de la LO 11/2022 (vigente 15-9-2022)**: en siniestros antiguos, **compara**.
3. **Prescripción (arts. 131 y 132 CP, verificados).**
   - **Art. 316** (prisión 6 meses – 3 años + multa 6-12 meses) → **5 años**.
   - **Art. 317** (pena inferior en grado) → **5 años** («los demás delitos»).
   - **Art. 152.1.1.º** (lesiones del 147.1 por imprudencia grave: prisión 3-6 meses **o** multa 6-18
     meses) → **verifica la calificación como leve o menos grave** antes de fijar el plazo: si la
     infracción fuera **leve**, prescribe **al AÑO** (art. 131.1 in fine). **Punto crítico y frecuente.**
   - **Art. 131.4:** concurso o infracciones conexas → plazo del **delito más grave**. En el concurso
     316 + 152 esto **juega a favor** de la acusación: aplica el plazo del más grave.
   - **🚨 Art. 132.2 CP (verificado):** la denuncia **NO interrumpe** la prescripción: solo la
     **suspende 6 meses**. Interrumpe la **resolución judicial motivada** que dirige el procedimiento
     contra persona determinada (regla 1.ª). Si en 6 meses no recae, **el cómputo continúa desde la
     fecha de la denuncia**. ⚠️ **Muy relevante aquí:** estos asuntos suelen llegar al despacho **tras
     meses de expediente ante la Inspección**. Comprueba el reloj antes de nada.
4. **Naturaleza perseguible — comprobación que se olvida:**
   - Los **arts. 316-318 CP** son delitos **públicos**: de oficio, basta denuncia.
   - **PERO art. 152.2 in fine CP (verificado, literal):** «El delito previsto en este apartado **solo
     será perseguible mediante denuncia de la persona agraviada o de su representante legal**.» →
     **las lesiones por imprudencia MENOS GRAVE son SEMIPÚBLICAS.** Si el resultado se califica así y
     no hay denuncia del agraviado, **no cabe proceder por ellas**. Asegúrate de que el trabajador
     `[PERJUDICADO]` denuncia expresamente.
5. **Competencia (art. 14.2 LECrim, verificado):** Sección de Instrucción del Tribunal de Instancia
   **del partido en que el delito se hubiere cometido** = donde radica el **centro de trabajo**.
6. **Estado del expediente administrativo:** ¿hay **acta de la Inspección de Trabajo**? ¿hay
   procedimiento sancionador **en curso**? → § *non bis in idem*: **cambia la estrategia**.
7. **Legitimación y posición:** trabajador accidentado, o —si falleció— los legitimados del **art. 109
   bis.1 II LECrim** (verificado: cónyuge no separado, pareja de hecho, hijos convivientes,
   progenitores, parientes hasta 3.er grado bajo su guarda…).
8. **Si quiere ser parte**, la denuncia no basta → `personacion-acusacion-particular-catalogo`.

---

## Marco normativo penal — VERIFICADO contra el BOE el 2026-07-17

### El tipo de peligro

**Art. 316 CP (verificado; redacción original LO 10/1995, vigente 24-5-1996) — literal:**
> «**Los que con infracción de las normas de prevención de riesgos laborales y estando legalmente
> obligados, no faciliten los medios necesarios para que los trabajadores desempeñen su actividad con
> las medidas de seguridad e higiene adecuadas, de forma que pongan así en peligro grave su vida, salud
> o integridad física**, serán castigados con las penas de **prisión de seis meses a tres años y multa
> de seis a doce meses**.»

**Elementos — subsúmelos uno a uno, con folio:**

| Elemento | Qué acreditar | Riesgo si falla |
|---|---|---|
| **Infracción de normas de prevención** | Precepto **concreto** de la LPRL o de su desarrollo reglamentario. **Norma penal en blanco**: sin norma extrapenal identificada, no hay tipo | Atipicidad |
| **«Estando legalmente obligados»** | Que el denunciado es **sujeto del deber** (§ sujetos). No basta ser directivo | Atipicidad para ese sujeto |
| **No facilitar los medios necesarios** | Omisión concreta: qué medio faltaba | Atipicidad |
| **Peligro GRAVE** para vida, salud o integridad | **Peligro concreto y grave**, no abstracto ni remoto | Atipicidad |
| **Dolo** (al menos eventual) | Conocimiento del riesgo y de la omisión | **Degrada al art. 317** |

- ⚠️ **«No facilitar los medios» se interpreta ampliamente** (no solo entregar el EPI: también formar,
  informar, evaluar el riesgo, vigilar el cumplimiento). **Pero es interpretación jurisprudencial:
  contrástala con `buscar_sentencias` antes de construir el escrito sobre ella.** ⛔ No la afirmes de
  memoria.
- **Delito de PELIGRO CONCRETO:** se consuma **sin resultado lesivo**. **El accidente no es elemento
  del tipo**: es la prueba de que el peligro existía.

**Art. 317 CP (verificado, literal):** «**Cuando el delito a que se refiere el artículo anterior se
cometa por imprudencia grave, será castigado con la pena inferior en grado.**»

### ⭐ El deslinde 316 / 317 — donde se gana o se pierde

**Es la cuestión central de estas denuncias. La única diferencia es el elemento subjetivo.**

| | **Art. 316 — DOLO** | **Art. 317 — IMPRUDENCIA GRAVE** |
|---|---|---|
| **Elemento subjetivo** | **Dolo**, bastando el **eventual**: conoce el riesgo grave y la omisión, y **acepta** el resultado de peligro | **Imprudencia grave**: infracción del deber de cuidado **sin** representación/aceptación del peligro |
| **Pena** | Prisión 6 m – 3 a + multa 6-12 m | **Inferior en grado** |
| **Imprudencia LEVE o MENOS GRAVE** | — | **ATÍPICA**: el 317 exige imprudencia **GRAVE**. Sin gravedad, no hay delito |

> **Cómo se acredita el DOLO EVENTUAL — con hechos, no adjetivos.** Alega, si constan:
> - **requerimientos previos** de la Inspección de Trabajo sobre el mismo riesgo, desatendidos;
> - **advertencias** de los trabajadores, del delegado de prevención o del servicio de prevención;
> - **accidentes anteriores** de mecánica idéntica en la misma empresa;
> - **evaluación de riesgos que YA identificaba el riesgo** y planificación **no ejecutada**;
> - **reiteración y permanencia** de la situación (no un descuido puntual);
> - **decisión consciente** de continuar la actividad pese al riesgo (p. ej. por plazo o coste).
> **Sin estos indicios, la calificación honesta suele ser el 317.** Forzar el 316 sin ellos invita a
> una degradación que arrastra la credibilidad del resto del escrito. **Y ojo:** si se degrada al 317 y
> además la imprudencia se reputa **no grave**, el resultado es **atipicidad total**.
> ⚠️ **Verifica la doctrina sobre el dolo eventual en el 316 con `buscar_sentencias`.** ⛔ No la
> afirmes de memoria.

### ⭐ Art. 318 CP — atribución de responsabilidad en personas jurídicas

**Art. 318 CP (verificado; redacción LO 11/2003, vigente 1-10-2003) — literal:**
> «**Cuando los hechos previstos en los artículos de este título se atribuyeran a personas jurídicas, se
> impondrá la pena señalada a los ADMINISTRADORES O ENCARGADOS DEL SERVICIO que hayan sido responsables
> de los mismos y a quienes, CONOCIÉNDOLOS Y PUDIENDO REMEDIARLO, NO HUBIERAN ADOPTADO MEDIDAS para
> ello. En estos supuestos la autoridad judicial podrá decretar, además, alguna o algunas de las
> medidas previstas en el artículo 129 de este Código.**»

**Léelo con cuidado — es un precepto peculiar y muy mal citado:**
- **NO es el art. 31 bis.** El art. 318 es una **regla de atribución** que traslada la pena **a personas
  FÍSICAS** cuando los hechos se atribuyen a una persona jurídica. **La persona jurídica NO es penada
  con las penas del art. 33.7 por esta vía**: solo caben las **medidas del art. 129**.
  > ⛔ **No pidas multa a la sociedad por el art. 318**: no la contempla. **Verifica el art. 129 con
  > `buscar_articulo`** antes de enumerar las medidas. → `[verificar]`
- **Dos círculos de responsables, y son distintos:**
  1. **«Administradores o encargados del servicio» que hayan sido RESPONSABLES** de los hechos →
     responsabilidad **activa**.
  2. **«Quienes, CONOCIÉNDOLOS y PUDIENDO REMEDIARLO, NO hubieran adoptado medidas»** → responsabilidad
     **omisiva**, con **dos requisitos acumulativos**: **conocimiento efectivo** + **capacidad real de
     remediar**. ⭐ Este segundo círculo es **la vía para alcanzar al administrador que "no estaba allí"**
     — pero **exige probar ambos requisitos**. No lo uses como atajo.
- **«Encargado del servicio»** no es un cargo formal: es quien **tiene atribuida la función**. Alcanza a
  jefes de obra, encargados y mandos intermedios con capacidad de decisión sobre la seguridad.
- ⚠️ **Individualiza SIEMPRE.** «Los administradores» en bloque **no** es una imputación: es una
  omisión de trabajo. Por **cada** denunciado: **qué deber tenía, qué sabía, qué podía hacer, qué no
  hizo, y en qué folio consta**.

### Los demás tipos del Título XV (arts. 311-318)

- **Art. 311 CP (verificado, LO 14/2022, vigente 12-1-2023)** — **prisión 6 meses – 6 años y multa 6-12
  meses**: **1.º** imposición de condiciones laborales o de Seguridad Social lesivas **mediante engaño o
  abuso de situación de necesidad**; **2.º** **condiciones ilegales** mediante contratación bajo
  **fórmulas ajenas al contrato de trabajo**, o su mantenimiento contra requerimiento o sanción
  administrativa; **3.º** **ocupación simultánea de una pluralidad de trabajadores sin alta** en la
  Seguridad Social o sin autorización de trabajo, con umbrales **25 %** (> 100 trabajadores), **50 %**
  (> 10 y ≤ 100), **la totalidad** (> 5 y ≤ 10); **4.º** mantenimiento de esas condiciones en
  **transmisión de empresas**; **5.º** **violencia o intimidación → penas superiores en grado**.
  > ⚠️ **Renumeración por la LO 14/2022:** en hechos **anteriores al 12-1-2023** los ordinales **son
  > distintos** (lo que hoy es 3.º antes era 2.º). **No cites el ordinal sin comprobar la redacción
  > aplicable**, y contrasta los umbrales con la plantilla real.
- **Art. 312 CP (verificado):** **prisión 2-5 años y multa 6-12 meses**. **312.1** **tráfico ilegal de
  mano de obra**; **312.2** reclutar o determinar al abandono del puesto **ofreciendo empleo o
  condiciones engañosas o falsas**, y **emplear a extranjeros sin permiso de trabajo** en condiciones
  que perjudiquen, supriman o restrinjan sus derechos.
- **Arts. 313, 314 y 315 CP** (migraciones fraudulentas, discriminación grave, libertad sindical y
  huelga): **verifícalos con `buscar_articulo` antes de citarlos** → `[verificar]`.
- **⚠️ Art. 318 bis ≠ art. 318.** El **318 bis** (verificado) es **ayuda a la entrada, tránsito o
  permanencia irregular** de extranjeros: **otro Título**, nada que ver con la regla de atribución del
  318. Confusión frecuente por proximidad numérica.

---

## Concurso con el delito de resultado

**Art. 152 CP — lesiones imprudentes (verificado, LO 11/2022, vigente 15-9-2022):**
- **152.1 — imprudencia GRAVE**, «en atención al riesgo creado y el resultado producido»:
  - **1.º** lesiones del **art. 147.1** → **prisión 3-6 meses O multa 6-18 meses**.
  - **2.º** lesiones del **art. 149** → **prisión 1-3 años**.
  - **3.º** lesiones del **art. 150** → **prisión 6 meses – 2 años**.
  - **Imprudencia PROFESIONAL** → además **inhabilitación especial** para profesión, oficio o cargo de
    **6 meses a 4 años**.
- **152.2 — imprudencia MENOS GRAVE:** lesiones del 147.1 → **multa 1-2 meses**; lesiones de los arts.
  149 y 150 → **multa 3-12 meses**. **Y: «solo será perseguible mediante denuncia de la persona
  agraviada o de su representante legal».**
> **Verifica con `buscar_articulo` los arts. 147, 149 y 150** para encajar la lesión concreta antes de
> fijar el apartado. ⛔ No adivines el ordinal: la calificación de la lesión **decide la pena y el
> plazo de prescripción**.
> Si el resultado es **muerte** → **homicidio imprudente, art. 142 CP**: **verifícalo con
> `buscar_articulo`** antes de citarlo → `[verificar]`.

**Art. 77 CP — concurso (verificado):**
- **77.1:** se aplica cuando **un solo hecho constituye dos o más delitos** (**ideal**), o cuando **uno
  es medio necesario para cometer el otro** (**medial**).
- **77.2 (ideal):** se aplica **en su mitad superior la pena prevista para la infracción más grave**,
  **sin que pueda exceder de la suma** de las que corresponderían por separado; si excede, **se
  sancionan por separado**.
- **77.3 (medial):** pena **superior** a la que habría correspondido por la infracción más grave, sin
  exceder de la suma de las penas concretas separadas; individualización conforme al **art. 66**.

> ⚠️ **La relación concursal entre el art. 316/317 y el delito de resultado (152/142) es cuestión
> JURISPRUDENCIAL DEBATIDA** — concurso **ideal** (art. 77), concurso de **normas** (art. 8), o
> absorción, y la solución varía según **el peligro alcance o no a trabajadores distintos del
> accidentado**. **⛔ NO la afirmes de memoria: contrástala con `buscar_sentencias` antes de calificar.**
> **Argumento que sí debes conocer y alegar cuando proceda:** si el peligro grave afectó a **varios
> trabajadores** y solo **uno** resultó lesionado, el delito de peligro **conserva sustantividad
> propia** respecto de los demás y no queda absorbido. **Verifícalo antes de sostenerlo.**

---

## Sujetos responsables — mapa completo

**No te quedes en «la empresa». Recorre este mapa e individualiza cada posición con hechos y folios:**

- **Empresario / persona física titular** — deudor de seguridad (**art. 14 LPRL**).
- **Administradores** — vía **art. 318**, primer o segundo círculo.
- **«Encargados del servicio»** — jefe de obra, encargado, mando intermedio con capacidad de decisión.
- **Empresa principal / contratista / subcontratista** — § siguiente.
- **Coordinador de seguridad y salud** y **recurso preventivo** en obras: régimen del **RD 1627/1997**
  y del art. 32 bis LPRL — **verifícalos con `buscar_articulo` antes de citarlos** → `[verificar]`.
- **Servicio de prevención** (propio o ajeno) y **técnico** que evaluó el riesgo.
- **Persona jurídica**: por el **art. 318**, solo **medidas del art. 129** (no penas del 33.7).

**Normativa de reenvío — la clave del tipo (norma penal en blanco):**
- **Art. 14 LPRL (verificado):** derecho de los trabajadores a **protección eficaz** y **correlativo
  DEBER DEL EMPRESARIO** de protección. **14.2:** el empresario **«deberá garantizar la seguridad y la
  salud de los trabajadores a su servicio en TODOS los aspectos relacionados con el trabajo»**,
  integrando la actividad preventiva y adoptando **cuantas medidas sean necesarias**; **acción
  permanente de seguimiento**. **⭐ 14.4:** el recurso a un **servicio de prevención ajeno** y la
  atribución de funciones a trabajadores **NO EXIMEN al empresario** de su deber. **⭐ 14.5:** «El coste
  de las medidas relativas a la seguridad y la salud en el trabajo **no deberá recaer en modo alguno
  sobre los trabajadores**.»
  > **14.4 es munición de primer orden:** desmonta la defensa habitual «lo teníamos externalizado con
  > un servicio de prevención». **Álegalo siempre que aparezca esa excusa.**
- **Art. 16 LPRL (verificado) — plan de prevención, evaluación y planificación:** **16.1** la prevención
  debe **integrarse en el sistema general de gestión** y **en todos los niveles jerárquicos**, mediante
  el **plan de prevención**. **16.2.a)** **evaluación inicial**, actualizada al cambiar las condiciones
  y **revisable «con ocasión de los daños para la salud que se hayan producido»**. **16.2.b)** si hay
  riesgo → **actividades preventivas planificadas** con plazo, responsables y recursos, y «el empresario
  deberá asegurarse de la **EFECTIVA EJECUCIÓN**». **⭐ 16.3:** producido un daño, «el empresario llevará
  a cabo una **INVESTIGACIÓN** al respecto, a fin de detectar las causas».
  > **Dos argumentos potentes:** (1) un plan **existente pero no ejecutado** (16.2.b) o una evaluación
  > **que ya identificaba el riesgo** acreditan **conocimiento** → refuerzan el **dolo eventual del 316**;
  > «tener papeles» no es prevenir. (2) **Pide la investigación del 16.3**: si no la hizo, infracción
  > autónoma; si la hizo, es una confesión documentada de las causas.
- **Art. 24 LPRL (verificado) — coordinación de actividades empresariales:** **24.1** varias empresas en
  un mismo centro → **deber de cooperar** y establecer **medios de coordinación**. **24.2** el
  **empresario titular del centro** debe procurar que los demás reciban **información e instrucciones**
  sobre riesgos y **medidas de emergencia**. **24.5** esos deberes alcanzan a los **autónomos** que
  operen en el centro.
  - **⭐ 24.3 — la llave para alcanzar a la empresa principal:** las empresas que **contraten o
    subcontraten** obras o servicios **correspondientes a su propia actividad** y que se desarrollen **en
    sus propios centros de trabajo** «deberán **VIGILAR el cumplimiento** por dichos contratistas y
    subcontratistas de la normativa de prevención».
- **⭐ Art. 42.3 LISOS** — **Real Decreto Legislativo 5/2000** (verificado): «**La empresa principal
  responderá SOLIDARIAMENTE con los contratistas y subcontratistas a que se refiere el apartado 3 del
  artículo 24 de la Ley de Prevención de Riesgos Laborales** del cumplimiento, durante el período de la
  contrata, de las obligaciones impuestas por dicha Ley en relación con los trabajadores que aquéllos
  ocupen en los centros de trabajo de la empresa principal, **siempre que la infracción se haya producido
  en el centro de trabajo de dicho empresario principal**.» **ETT:** la **empresa usuaria** es
  responsable de las condiciones de ejecución del trabajo en cuanto a seguridad y salud y del **recargo
  de prestaciones**. «**Los pactos que tengan por objeto la elusión, en fraude de ley, de las
  responsabilidades establecidas en este apartado son NULOS y no producirán efecto alguno.**»
  > ⚠️ **Precisión que debes respetar:** el **art. 42.3 LISOS es responsabilidad ADMINISTRATIVA
  > solidaria**, **no** una regla de autoría penal. **Cítalo para la responsabilidad civil y como
  > contexto del deber de vigilancia (24.3 LPRL), NO como fundamento de la imputación penal.** La
  > responsabilidad penal se construye por el **art. 318** e individualizando conductas. Confundirlo es
  > un error de bulto.
  > ⚠️ **Sigla trampa (constatada):** «**LISOS**» a secas resuelve en el conector a una *Orden de 1994
  > sobre alambres trefilados **lisos***. Búscala como «**Real Decreto Legislativo 5/2000**».

---

## ⚠️ Non bis in idem y relación con el orden social y administrativo

**Art. 3 del RDLeg 5/2000 (LISOS) — «Concurrencia con el orden jurisdiccional penal» (VERIFICADO):**
- **3.1:** «**No podrán sancionarse los hechos que hayan sido sancionados penal o administrativamente,
  en los casos en que se aprecie IDENTIDAD DE SUJETO, DE HECHO Y DE FUNDAMENTO.**» ← la **triple
  identidad**: sin las tres, **no** hay bis in idem.
- **⭐ 3.2 — PREFERENCIA DEL ORDEN PENAL:** «En los supuestos en que las infracciones pudieran ser
  constitutivas de **ilícito penal**, la Administración **pasará el tanto de culpa** al órgano judicial
  competente o al Ministerio Fiscal y **SE ABSTENDRÁ DE SEGUIR EL PROCEDIMIENTO SANCIONADOR** mientras
  la autoridad judicial no dicte **sentencia firme** o resolución que ponga fin al procedimiento, o
  mientras el Ministerio Fiscal no comunique la improcedencia de iniciar o proseguir actuaciones.»
  > **Consecuencia estratégica de primer orden — explícasela al cliente:** **la denuncia penal
  > PARALIZA el expediente sancionador de la Inspección.** Esto tiene dos caras:
  > - **A favor:** el orden penal tiene medios de investigación superiores y el proceso penal fija los
  >   hechos.
  > - **En contra:** si el expediente sancionador estaba **avanzado** y la sanción era **segura**,
  >   denunciar puede **retrasar años** un resultado que ya se tenía. **Valóralo antes de denunciar y
  >   déjalo por escrito.**
- **3.3:** de **no** estimarse ilícito penal, o dictada resolución que ponga fin al procedimiento penal,
  **la Administración continuará el expediente sancionador «en base a los hechos que los Tribunales
  hayan considerado PROBADOS»** ← **vinculación de los hechos probados**. El archivo penal **no** cierra
  la vía administrativa.
- **⭐ 3.4 — lo que NO se paraliza:** el tanto de culpa **no afecta** al **inmediato cumplimiento de las
  medidas de PARALIZACIÓN de trabajos** en riesgo grave e inminente, ni a la efectividad de los
  **requerimientos de subsanación**, ni a los expedientes **sin conexión directa** con las actuaciones
  penales. **Tranquiliza al cliente: denunciar no desprotege a la plantilla.**

**Compatibilidades — no son bis in idem (falta la triple identidad):**
- **Recargo de prestaciones** de la Seguridad Social — **verifica el precepto (art. 164 LGSS) con
  `buscar_articulo`** antes de citarlo → `[verificar]`.
- **Indemnización civil** de daños y perjuicios.
- **Art. 42.6 LISOS (verificado):** los hechos probados de una **sentencia firme contencioso-
  administrativa** sobre infracción de prevención **vinculan al orden social** en cuanto al **recargo**.

---

## Responsabilidad civil derivada del delito

Se ejercita **en el proceso penal** salvo reserva o renuncia expresa (arts. 100, 108-117 LECrim; arts.
109-126 CP). ⚠️ **Coordínala con lo ya percibido**: recargo, mejoras voluntarias, seguro de convenio y
prestaciones de Seguridad Social. **Advierte del riesgo de sobreindemnización y de la posible
compensación.**
- **Art. 116 CP (verificado):** con varios responsables el tribunal **señala la cuota** de cada uno;
  autores y cómplices responden **solidariamente entre sí por sus cuotas** y **subsidiariamente** por
  las de los demás.
- **Responsable civil subsidiario (art. 120 CP)** — vía natural para la **empresa**: **verifícalo con
  `buscar_articulo`** antes de invocarlo → `[verificar]`.
- **Aseguradora de RC** — **responsable civil directo (art. 117 CP)**: **verifícalo** → `[verificar]`.
  **Llámala al proceso desde el inicio**: es quien paga.
- **Valóralo, no lo dejes abierto:** lesiones, secuelas, perjuicio personal básico y particular, lucro
  cesante. **Verifica el baremo aplicable y su vigencia antes de citarlo** → `[verificar]`. **⛔ No
  inventes cuantías ni factores de corrección.**

---

## Prueba y diligencias — pídelas ya

⏰ **Art. 324 LECrim:** 12 meses prorrogables; **sin auto de prórroga previo al vencimiento, las
diligencias posteriores NO son válidas** (324.3). → `solicitud-diligencias-instruccion-catalogo`.

- **⭐ Acta e informe de la INSPECCIÓN DE TRABAJO** — la pieza central. Oficio a la ITSS interesando el
  **acta de infracción**, el **informe** del accidente y **todo el expediente**, incluidos
  **requerimientos anteriores** sobre el mismo riesgo (→ **dolo**).
- **Plan de prevención, evaluación de riesgos y planificación** (art. 16 LPRL), **con su fecha**; y el
  **informe de investigación del art. 16.3 LPRL**, que la empresa **está obligada** a realizar.
- **Formación e información** del trabajador (arts. 18 y 19 LPRL — **verifícalos**) y **entrega de
  EPIs** con acuse.
- **Contratos** de contrata/subcontrata, **libro de subcontratación**, **plan de seguridad y salud** y
  **actas de coordinación** (art. 24 LPRL; RD 1627/1997 — **verifícalo**).
- **Atestado**; **acta de levantamiento** si hay fallecido. **Parte de baja**, historia clínica,
  **informe de alta** y **pericial médico-forense** de sanidad y secuelas.
- **⭐ Pericial técnica de seguridad** sobre la mecánica del accidente y la medida omitida — **decisiva**:
  es la que enlaza la omisión con el resultado.
- **Testificales** `[TESTIGO]`: compañeros presentes, **delegado de prevención**, encargado, recurso
  preventivo.
- **Nota simple del Registro Mercantil** (`[ENTIDAD]`, `[CIF]`): administradores **y FECHA de su
  nombramiento** — decide **quién era administrador el día del accidente** (o
  `buscar_empresa_mercantil`). **TC2 / alta en Seguridad Social** (relación laboral; art. 311.3.º).
- **Preservación** de videovigilancia y del **lugar de los hechos**: se pierden en días. → **art. 777.2
  LECrim** (preconstituida) si algún testigo es de difícil localización posterior.

---

## Estructura del escrito

1. **Encabezamiento:** «A LA SECCIÓN DE INSTRUCCIÓN DEL TRIBUNAL DE INSTANCIA DE [PARTIDO] QUE POR
   REPARTO CORRESPONDA» (art. 14.2 LECrim: partido del **centro de trabajo**).
2. **Comparecencia:** letrado/a y `[PERJUDICADO]` (trabajador accidentado), o los legitimados del art.
   109 bis.1 II si falleció. **La denuncia no exige procurador ni poder especial.**
3. **Fórmula de interposición:** «formula **DENUNCIA** por delito contra los derechos de los
   trabajadores del **art. 316 CP** [o **317**] **en relación con el art. 318 CP**, en concurso [ideal
   / medial — **art. 77 CP**] con un delito de lesiones imprudentes del **art. 152.[apartado] CP**
   [u homicidio imprudente del art. 142 CP], contra `[DENUNCIADO]`».
4. **Apartados numerados:**
   - **PRIMERO — Órgano competente** (art. 14.2 LECrim).
   - **SEGUNDO — Denunciante:** nombre, apellidos y **vecindad**.
   - **TERCERO — Denunciados:** empresario, administrador/es, encargado del servicio, contratista
     principal, subcontratista, coordinador. **Cada uno con su posición y su deber.**
   - **CUARTO — Relación circunstanciada de los hechos:** relación laboral y antigüedad; **funciones**
     del trabajador; **tarea encomendada** el día del siniestro; **condiciones del centro**; **medida de
     seguridad OMITIDA** (concreta); **mecánica del accidente**; **lesiones** y **baja**; asistencia
     posterior. **Cada hecho con su folio o documento.**
5. **FUNDAMENTOS DE LA CALIFICACIÓN:**
   - **Norma de prevención infringida**: precepto **concreto** de la LPRL o reglamento (norma penal en
     blanco — **sin esto no hay tipo**).
   - **Condición de obligado** de cada denunciado (arts. 14 LPRL, 24.3 LPRL, 318 CP).
   - **Peligro grave** para la vida, salud o integridad.
   - **Elemento subjetivo**: **dolo (316)** con sus indicios, **o** imprudencia **grave (317)**.
   - **NEXO CAUSAL** entre la omisión y el resultado — y **valoración de la conducta del trabajador**
     (§ errores).
   - **Concurso** (art. 77) — **verificado con `buscar_sentencias`**.
6. **DILIGENCIAS interesadas** (§ anterior).
7. **RESPONSABILIDAD CIVIL** — incluida la **aseguradora** y la empresa como responsable civil
   subsidiario.
8. **DOCUMENTOS:** nota simple del Registro Mercantil, informe/acta ITSS, parte de baja, contrato.
9. **SUPLICO:** admisión, **incoación de diligencias previas**, práctica de diligencias.
10. **OTROSÍES** — lugar, fecha y firma.

> **Anclaje al folio — regla innegociable.** Especialmente en la **medida omitida** y en el **nexo
> causal**: son los dos puntos que la defensa atacará. Cada uno, con su folio o su documento.

---

## Errores típicos que hunden el escrito

1. **No identificar la NORMA DE PREVENCIÓN concreta infringida.** Es **norma penal en blanco**: sin
   precepto extrapenal identificado, **no hay tipo**. **El error más frecuente y más letal.**
2. **Calificar por el 316 (dolo) sin indicios de conocimiento** → degradación al 317, y arrastre de
   credibilidad. Y si la imprudencia no es **grave**, **atipicidad total**.
3. **Confundir el art. 318 con el art. 31 bis**: el 318 traslada la pena a **personas físicas**; a la
   persona jurídica solo le caben las **medidas del art. 129** (no las penas del 33.7).
4. **Confundir el art. 318 con el 318 bis** (ayuda a la inmigración irregular): nada que ver.
5. **Imputar en bloque «a los administradores»** sin individualizar deber, conocimiento, capacidad de
   remediar y omisión de cada uno (art. 318).
6. **Usar el art. 42.3 LISOS como fundamento de la imputación PENAL**: es responsabilidad
   **administrativa solidaria**. La penal se construye por el 318 y el 24.3 LPRL.
7. **Creer que sin lesión no hay delito**: el 316 es de **peligro concreto**, se consuma sin resultado.
8. **Olvidar que las lesiones por imprudencia MENOS GRAVE son semipúblicas** (art. 152.2 in fine) →
   sin denuncia del agraviado, no cabe proceder.
9. **No comprobar el apartado del art. 152** (147.1 / 149 / 150) → pena y **plazo de prescripción**
   erróneos; si la infracción es **leve**, prescribe **al año**.
10. **Denunciar sin valorar el art. 3.2 LISOS**: la denuncia **paraliza** el expediente sancionador. A
    veces **no interesa**.
11. **Creer que el archivo penal cierra la vía administrativa**: **no** (art. 3.3 LISOS), y además la
    Administración queda vinculada por los **hechos probados**.
12. **Aceptar la excusa del servicio de prevención ajeno**: **art. 14.4 LPRL** — **no exime**.
13. **Ignorar la conducta del trabajador.** La imprudencia **del propio trabajador** es la defensa
    estándar. **Anticípala**: el deber de protección del empresario alcanza también a los **descuidos
    previsibles** e incluso a las **imprudencias no temerarias** — **pero esto es doctrina
    jurisprudencial: verifícala con `buscar_sentencias` antes de sostenerla.** ⛔ No la afirmes de
    memoria.
14. **No pedir el informe de investigación del art. 16.3 LPRL** ni los **requerimientos previos** de la
    ITSS: son la munición del **dolo**.
15. **No llamar a la aseguradora** desde el inicio.
16. **Buscar «LISOS»** a secas → *alambres trefilados*. Usa **RDLeg 5/2000**.
17. **Citar los ordinales del art. 311 sin comprobar la redacción aplicable** (renumerados por la LO
    14/2022, vigente 12-1-2023).
18. **Citar jurisprudencia sin conector.** ⛔ Prohibido.

---

## Datos personales — categoría reforzada

- Marcadores: `[DENUNCIADO]`, `[PERJUDICADO]`, `[TESTIGO]`, `[ENTIDAD]`, `[CIF]`, `[DOMICILIO]`,
  `[IMPORTE]`. **Nunca datos reales de terceros en la salida.**
- ⚠️ **Doble sensibilidad en esta skill:** los datos de **infracciones y condenas penales** son
  **categoría especial del art. 10 RGPD**; y aquí se manejan además **datos de SALUD del trabajador**
  (partes de baja, historia clínica, secuelas), **categoría especial del art. 9 RGPD**. **Aporta solo
  lo pertinente al objeto del proceso**, no la historia clínica completa. Cuidado extremo con
  **menores** (trabajo de menores) y con el **compañero testigo**, que sigue empleado en la empresa
  denunciada y está expuesto a represalias.
- Slug del expediente: `descriptor-delito-año`, **nunca con el nombre del cliente**
  (`PROTECCION-DATOS.md`).

---

## Reglas de trabajo

- **Cifras y artículos:** fuente única `references/anclas-normativas-penal.md` o verificación en el
  momento con **`buscar_articulo`**. ⛔ **Prohibido inventar** penas, plazos, ordinales o artículos. Lo
  no verificable → **`[verificar]`** y **dilo**.
- **Jurisprudencia:** solo `buscar_sentencias` / `buscar_por_cita` / `leer_sentencias`. ⛔ Nunca de
  memoria — **en especial** la relación concursal 316/152, el dolo eventual y la incidencia de la
  imprudencia del trabajador: son las tres cuestiones **más debatidas** de esta materia.
- **⚠️ Ámbito:** el plugin es **exclusivamente penal**. La reclamación por despido, el recargo de
  prestaciones o la demanda de daños ante el **orden social** **quedan fuera**. La **acción civil
  derivada del delito sí entra** (se ejercita en el proceso penal). **No redactes escritos del orden
  social**; si el asunto lo requiere, **dilo y deriva**.
- **Instruye el Juez de Instrucción** (Sección de Instrucción del Tribunal de Instancia). ⛔ **No existe
  el «fiscal instructor»**: reforma en tramitación (prevista 1-1-2028), **no es Derecho vigente**. No la
  menciones, ni cites un «art. 4 bis EOMF». ⚠️ Que el art. 3.2 LISOS mencione que la Administración pasa
  el tanto de culpa **al órgano judicial o al Ministerio Fiscal** **no** significa que el Fiscal
  instruya.
- ⛔ **Nada de MASC**: es del orden **civil**. Y **no confundas con la conciliación previa del orden
  social (SMAC)**: aquí no existe requisito preprocesal alguno.
- **Días inhábiles: art. 183 LOPJ** (verificado, LO 14/2022): inhábiles **agosto** y **del 24 de
  diciembre al 6 de enero**, salvo actuaciones **declaradas urgentes**. **Pero art. 201 LECrim**
  (verificado): «**Todos los días y horas del año serán hábiles para la instrucción de las causas
  criminales, sin necesidad de habilitación especial**».

## Entrega

Documento final en **Word `.docx`** con la skill **`docx`**, maquetado como escrito judicial
(encabezamiento, apartados numerados, fundamentos, suplico, otrosíes), listo para **LexNET**.
