---
name: responsabilidad-penal-personas-juridicas
description: Defensa de personas juridicas investigadas o acusadas penalmente (art. 31 bis CP). Conflicto de interes con la persona fisica, modelo de compliance como eje de defensa, atenuantes del 31 quater, penas del 33.7, representante especialmente designado e investigaciones internas. Usar con "responsabilidad penal de la empresa", "compliance", "modelo de prevencion", "han imputado a la sociedad", "31 bis", "canal de denuncias", "compliance officer", "defender a la empresa y al administrador", "penas para la persona juridica", "representante especialmente designado".
---

# Responsabilidad penal de las personas jurídicas

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen penal de la persona jurídica** (arts. 31 bis a 31 quinquies, 33.7, 66 bis y 129 CP) → `buscar_articulo` (`ley="CP"`).
- **Estatuto procesal** (arts. 119, 409 bis, 785.11 y 786 bis LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Sociedad, administradores de hecho y de derecho y apoderados** → `buscar_empresa_mercantil` (estado, domicilio, cargos vigentes, últimos actos inscritos).
- **Transformación, fusión o escisión en fechas clave (art. 130.2 CP)** → `sumario_borme` del día → `leer_boe`.
- **Doctrina de la Sala Segunda sobre el modelo de cumplimiento y su prueba** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Conflicto de interés penalmente tipificado** → `buscar_articulo` (`ley="CP"`, `articulo="467"`).
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

> **Anclas:** `references/anclas-normativas-penal.md` (BOE, 2026-07-17). Verificar todo artículo con
> `buscar_articulo` antes de citarlo; jurisprudencia **solo** con `buscar_sentencias`. **Prohibido
> inventar** ECLI, ROJ, fechas o ponentes. Lo no verificable → **`[verificar]`**, y se dice.
>
> ⛔ **NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción** (arts. 119 y 775
> LECrim). ⛔ **Nada de MASC**: es del orden civil.
>
> **Nomenclatura (LO 1/2025, DF 38.3, desde 3-10-2025):** el **órgano** es la **Sección de Instrucción
> del Tribunal de Instancia** (art. 14 LECrim), no el «Juzgado de Instrucción». Usarla en los
> encabezamientos; «Juez de Instrucción» se conserva solo al citar el texto legal literal.

---

## ⚠️ 1. CONFLICTO DE INTERÉS — RESOLVER ANTES DE ACEPTAR EL ENCARGO

**Se ejecuta primero. Si hay conflicto, no hay encargo que redactar.**

Defender a la vez a la persona jurídica y a la persona física investigada por los mismos hechos es un
conflicto **estructural**, no de oportunidad:

- El **31 bis.2.3.º** exige que los autores individuales **eludieran fraudulentamente** el modelo:
  **la defensa óptima de la sociedad incrimina al individuo**.
- La tesis óptima del individuo (práctica tolerada, sin controles reales, siguiendo instrucciones)
  **destruye la exención** de la sociedad.

**El consentimiento informado no sana un conflicto en que la defensa de un cliente exige sostener la
culpabilidad del otro.**

### ⭐ No es solo deontológico: es TIPO PENAL — art. 467.1 CP

> Verificado literalmente (anclas § 11.2 y `buscar_articulo`; vigente desde 24-5-1996): el abogado
> que, «habiendo asesorado o tomado la defensa o representación de alguna persona, **sin el
> consentimiento de ésta** defienda o represente **en el mismo asunto a quien tenga intereses
> contrarios**» → **multa de 6 a 12 meses** e **inhabilitación especial para su profesión de 2 a
> 4 años**.

El supuesto del art. 31 bis es el caso de manual: intereses **estructuralmente contrarios** en el
**mismo asunto**. Ojo también al **467.2**: perjudicar de forma manifiesta los intereses encomendados
—**incluso por imprudencia grave**— es delito (anclas § 11.2).

### Protocolo

1. **Antes de aceptar:** identificar a todos los investigados y su relación con `[ENTIDAD]`.
2. ¿La estrategia de la PJ pasa —hoy o previsiblemente— por el 31 bis.2.3.º? **Si es «sí» o «puede
   que sí», hay conflicto.**
3. **Advertir por escrito** a ambos, recomendar **defensas separadas**, documentarlo.
4. Si el despacho asesoraba a `[ENTIDAD]` en compliance antes de los hechos, valorar si el letrado
   puede acabar siendo **testigo** sobre la implantación del modelo — causa autónoma de abstención.

### El representante designado (art. 119.1.a LECrim)

Si el representante es la **propia persona física investigada**, el conflicto se reproduce dentro del
proceso: quien declara «en nombre de la sociedad» (409 bis) tiene interés directo en que no se
acredite su propia elusión fraudulenta.

- **Verificado — art. 786 bis.1** (redacción Ley 37/2011, vigente 31-10-2011; **la LO 1/2025 NO lo
  renumeró ni modificó**): la **única incompatibilidad expresa** es que **no puede designarse a quien
  haya de declarar como TESTIGO**.
- La incompatibilidad por **coinvestigado** **no** está en la ley: es construcción jurisprudencial →
  **`[verificar]` con `buscar_sentencias`** antes de fundar en ella una estrategia.
- **Recomendación:** persona **ajena a los hechos**, no investigada y que no vaya a ser testigo.
- La **falta de designación NO impide** la sustanciación con Abogado y Procurador (119.1.a): no es
  táctica dilatoria útil.

---

## 2. Art. 31 bis CP (vigente 1-7-2015, LO 1/2015)

### 2.1 Los dos títulos de imputación (31 bis.1)

| | **a) — «los de arriba»** | **b) — «los de abajo»** |
|---|---|---|
| **Autores** | Representantes legales; quienes, individualmente o como integrantes de un órgano, **están autorizados para tomar decisiones** en nombre de la PJ **u ostentan facultades de organización y control** | Quienes están **sometidos a la autoridad** de las personas físicas de a) |
| **Conexión** | **En nombre o por cuenta** de la PJ **y en su beneficio directo o indirecto** | **En el ejercicio de actividades sociales** y **por cuenta y en beneficio directo o indirecto** |
| **Plus** | — | Que hayan podido realizar los hechos por **haberse incumplido GRAVEMENTE** los **deberes de supervisión, vigilancia y control**, atendidas las concretas circunstancias del caso |

> ⚠️ **ERRATA FRECUENTE:** la ley **no** dice «en nombre y **provecho**» — redacción **anterior a
> 2015**. Hoy: «**en nombre o por cuenta**… **y en su beneficio directo o indirecto**». Citar
> «provecho» delata material desactualizado.

**Atacar el título antes que el modelo:** falta de **beneficio** directo o indirecto (delito en
beneficio exclusivo del individuo, o **contra** la sociedad); el autor **no encaja** en a) ni en b);
en b), que el incumplimiento **no fue grave** — con premio penológico: **66 bis regla 2.ª**, si no es
grave, las penas c) a g) tienen **máximo de 2 años en todo caso**.

### 2.2 ⭐ Exención — art. 31 bis.2 — CUATRO REQUISITOS ACUMULATIVOS (literal)

Solo para delitos de la **letra a)**:

1. **1.ª** el **órgano de administración** ha **adoptado y ejecutado con eficacia**, **antes de la
   comisión del delito**, modelos de organización y gestión que incluyen las medidas de vigilancia y
   control **idóneas para prevenir delitos de la misma naturaleza** o para **reducir de forma
   significativa el riesgo** de su comisión;
2. **2.ª** la **supervisión** del funcionamiento y del cumplimiento del modelo ha sido confiada a un
   **órgano de la persona jurídica con poderes autónomos de iniciativa y de control** o que tenga
   **encomendada legalmente** la función de supervisar la eficacia de los controles internos;
3. **3.ª** los **autores individuales** han cometido el delito **eludiendo fraudulentamente** los
   modelos de organización y de prevención; **y**
4. **4.ª** **no se ha producido una omisión o un ejercicio insuficiente** de sus funciones de
   supervisión, vigilancia y control por parte del órgano de la condición 2.ª

> ⭐ **La regla más rentable y la más olvidada — párrafo final del 31 bis.2:** la **acreditación
> PARCIAL** «será valorada a los efectos de **atenuación de la pena**». **Nunca se abandona la prueba
> del modelo aunque la exención se vea inalcanzable:** escrito requisito por requisito y **petición
> subsidiaria** de atenuación.

### 2.3 Apartados 3, 4 y 5

- **31 bis.3 — pequeñas dimensiones:** la supervisión de la 2.ª **puede asumirla el propio órgano de
  administración**. Definición legal cerrada: autorizadas a presentar **cuenta de PyG abreviada** →
  hecho **documentalmente acreditable** que neutraliza el reproche «no tenían compliance officer».
  **Comprobarlo siempre en las cuentas.**
- **31 bis.4 — exención en el título b):** basta haber **adoptado y ejecutado eficazmente, antes del
  delito**, un modelo **adecuado**. **Requisito único** — no exige elusión fraudulenta ni órgano
  autónomo: **es mucho más fácil que la del 31 bis.2**. Si el título es el b), es prioritaria.
  Atenuación por acreditación parcial igualmente aplicable.
- **31 bis.5 — requisitos del modelo (SEIS):** 1.º **identificar** actividades de riesgo; 2.º
  **protocolos** de formación de la voluntad, adopción y ejecución de decisiones; 3.º **gestión de
  recursos financieros**; 4.º **obligación de informar** de riesgos e incumplimientos al órgano de
  vigilancia (**sede legal del canal de denuncias**); 5.º **sistema disciplinario**; 6.º
  **verificación periódica** ante infracciones relevantes o cambios organizativos.
  > El 4.º **no dice «canal de denuncias»**: impone la obligación de informar. No atribuirle
  > exigencias (anonimato, plazos) que son de la **Ley 2/2023** — § 6.3.

### 2.4 Arts. 31 ter, quater y quinquies

**31 ter — autonomía.** **.1** Exigible **aunque la persona física no haya sido individualizada o no
haya sido posible dirigir el procedimiento contra ella**; multa a ambas → el tribunal **modula las
cuantías** para que la suma no sea desproporcionada (**invocarlo siempre** si el administrador también
es multado). **.2** Las circunstancias que afecten a la culpabilidad de la persona física, su
**fallecimiento** o **sustraerse a la acción de la justicia** **no excluyen ni modifican** la
responsabilidad de la PJ → cierra la defensa ingenua «absuelto el administrador, absuelta la empresa».

**⭐ 31 quater — CUATRO atenuantes** (numerus clausus: «**sólo** podrán considerarse»; posteriores al
delito y **a través de sus representantes legales**). **Lo decisivo es la ventana:**

| | Actividad | Ventana |
|---|---|---|
| **a)** | **Confesar** la infracción a las autoridades | **Antes de conocer que el procedimiento se dirige contra ella** |
| **b)** | **Colaborar** aportando pruebas **nuevas y decisivas** | **Cualquier momento del proceso** |
| **c)** | **Reparar o disminuir el daño** | Cualquier momento, **antes del juicio oral** |
| **d)** | **Medidas eficaces** para prevenir y descubrir delitos futuros cometidos con los medios o bajo la cobertura de la PJ | **Antes del comienzo del juicio oral** |

**31 quinquies — sector público.** **.1 Excluidos:** Estado, AAPP territoriales e institucionales,
Organismos Reguladores, Agencias y Entidades públicas Empresariales, organizaciones internacionales de
Derecho público, y las que ejerzan **potestades públicas de soberanía o administrativas**.
⚠️ **NO excluidos —sí responden— PARTIDOS POLÍTICOS y SINDICATOS** (su exclusión desapareció con la
LO 7/2012; error habitual de material antiguo). **.2** Sociedades mercantiles públicas que ejecuten
políticas públicas o presten **SIEG**: solo penas **a) (multa)** y **g) (intervención judicial)** —
**salvo** forma jurídica creada para **eludir** responsabilidad penal.

---

## 3. Penas y consecuencias accesorias

### 3.1 Catálogo del art. 33.7 — **todas GRAVES** (síntesis; literal con `buscar_articulo`)

| | Pena | Límite |
|---|---|---|
| **a)** | **Multa** por cuotas o proporcional | — |
| **b)** | **Disolución** — pérdida **definitiva** de personalidad y de capacidad de actuar en el tráfico o de cualquier actividad **aunque sea lícita** | definitiva |
| **c)** | **Suspensión de actividades** | ≤ **5 años** |
| **d)** | **Clausura de locales y establecimientos** | ≤ **5 años** |
| **e)** | **Prohibición de actividades** en cuyo ejercicio se cometió, favoreció o encubrió el delito | temporal (≤ **15 años**) o **definitiva** |
| **f)** | **Inhabilitación** para subvenciones y ayudas públicas, **contratar con el sector público** y beneficios fiscales o de Seguridad Social | ≤ **15 años** |
| **g)** | **Intervención judicial** para salvaguardar derechos de **trabajadores o acreedores** | ≤ **5 años** |

- **(g)** puede **limitarse a una instalación, sección o unidad de negocio**; el juez fija contenido e
  interventor en sentencia **o por auto posterior**; **modificable o suspendible en todo momento** →
  **pedir siempre la limitación a la unidad afectada** antes que la total.
- ⭐ **CAUTELARES (33.7 último párrafo):** **clausura temporal**, **suspensión de actividades sociales**
  e **intervención judicial** pueden acordarse por el **Juez Instructor durante la instrucción**. **Es
  la amenaza real y temprana: puede matar a la empresa antes de la sentencia.** Vigilarla desde el
  día 1 y oponerse con datos de impacto (empleo, contratos, SIEG).

### 3.2 Art. 66 bis — determinación (síntesis)

Reglas **1.ª a 4.ª y 6.ª a 8.ª del art. 66.1**, más:
- **Regla 1.ª** — para imponer y graduar **b) a g)**: **necesidad de prevenir la continuidad**
  delictiva; **consecuencias económicas y sociales, especialmente los efectos para los TRABAJADORES**;
  **puesto** de quien incumplió el deber de control.
  > La mención a los trabajadores es el mejor argumento contra las penas interdictivas. **Probarlo, no
  > alegarlo:** plantilla, contratos en ejecución, informe de impacto económico.
- **Regla 2.ª — techos:** c) a g) **no pueden exceder** la duración máxima de la **pena privativa de
  libertad prevista para la persona física**; **> 2 años** exige **reincidencia** **o**
  **instrumentalidad** (actividad legal **menos relevante** que la ilegal); ⭐ si la responsabilidad
  viene del **31 bis.1.b)** y el incumplimiento **no es grave** → **máximo 2 años en todo caso**;
  **permanente** de b) y e) y **> 5 años** de e) y f) exigen **66.1.5.ª** o instrumentalidad.

### 3.3 Art. 129 — entes SIN personalidad jurídica

Consecuencias accesorias con el contenido de las **letras c) a g) del 33.7**, más **prohibición
definitiva de cualquier actividad aunque sea lícita**. **Límite (129.2):** solo cuando el CP lo
**prevea expresamente** o se trate de delitos que permiten exigir responsabilidad a las PJ. Cautelares
por el **Juez Instructor** (129.3).

---

## 4. Estrategia de defensa

### 4.1 El modelo — cuatro objetos de prueba autónomos

| Requisito | Qué probar | Prueba típica |
|---|---|---|
| **1.ª — previo y eficaz** | Adoptado **y ejecutado antes** del delito, **idóneo** para delitos **de esa naturaleza** | Acuerdo del **órgano de administración** con fecha fehaciente; mapa de riesgos que **cubra el riesgo materializado**; evidencia de ejecución |
| **2.ª — órgano supervisor** | **Poderes autónomos de iniciativa y control** | Estatuto; **presupuesto y medios**; reporte directo al consejo; actas |
| **3.ª — elusión fraudulenta** | Que el autor **burló** el modelo | Logs, aprobaciones falseadas, controles saltados, dobles registros |
| **4.ª — no omisión** | Que el órgano **sí ejerció** sus funciones | Informes, auditorías, alertas atendidas, expedientes disciplinarios |

> **Lo decisivo es la EJECUCIÓN REAL, no el papel.** Un modelo **cosmético** —sin formación, sin
> auditorías, sin un solo expediente disciplinario, con órgano sin presupuesto ni acceso al consejo—
> **no exime y prueba en contra**: acredita el «ejercicio insuficiente» del requisito 4.ª.
> **Auditarlo con honestidad antes de construir la defensa sobre él.** Si es cosmético, cambiar de
> eje: negar el título (§ 2.1), negar el beneficio, y volcarse en el **31 quater**.

**Anticipar de la acusación:** riesgo materializado **no contemplado** en el mapa (modelo no idóneo);
modelo aprobado **después** del inicio de una conducta continuada (**fijar con precisión la fecha de
comisión**); compliance officer que es el propio administrador en entidad **no** de pequeñas
dimensiones (falla la 2.ª — comprobar antes el 31 bis.3).

### 4.2 ⭐ Atenuantes del 31 quater — la palanca práctica

1. **Letra d) — medidas eficaces ANTES DEL COMIENZO DEL JUICIO ORAL.** Única atenuante que **se
   construye legítimamente durante el proceso** y no depende del pasado. **Si `[ENTIDAD]` llega al
   juicio sin modelo, es un fallo de la defensa.** Implantar **cuanto antes** (un modelo aprobado dos
   semanas antes de la vista se lee como cosmético); documentar los **seis requisitos del 31 bis.5**;
   proponerlo como **prueba documental y pericial**.
2. **Letra c) — reparar antes del juicio oral.** Consignación, acuerdo con `[VÍCTIMA]`, devolución del
   beneficio. Barata y muy valorada; coordinar con el decomiso.
3. **Letra b) — colaborar con pruebas decisivas.** ⚠️ **Evaluar antes el conflicto (§ 1):**
   «decisivas» suele significar **contra la persona física**.
4. **Letra a) — confesar** antes de conocer que el procedimiento se dirige contra ella. Ventana muy
   estrecha; viva solo si la investigación interna detecta el delito **antes** de la citación.

### 4.3 Conformidad — art. 785.11 LECrim (anclas § 2.2)

La presta el **representante especialmente designado** con **poder especial**; es **independiente** de
los demás acusados y **no vinculante** para el juicio de estos. **La sociedad puede conformarse aunque
el administrador vaya a juicio** — suele ser lo racional para `[ENTIDAD]` (cierra el riesgo de penas
interdictivas y de inhabilitación para contratar con el sector público). **Y es el conflicto del § 1
en estado puro:** la conformidad de la sociedad es un dato demoledor contra la persona física.

- **785.7 in fine:** el letrado **facilitará por escrito** a su defendido la información sobre el
  acuerdo. Documentarlo.
- ⚠️ **Defecto de coordinación** (anclas § 2.2): los arts. 784.3 y 801 siguen remitiendo al **787**,
  pero la sede de la conformidad es hoy el **785**.

---

## 5. Estatuto procesal — arts. 119, 409 bis y 786 bis LECrim

> Los tres con redacción **Ley 37/2011** (vigente 31-10-2011). **La LO 1/2025 no los tocó.**

- **Art. 119 — imputación:** comparecencia del **art. 775** con particularidades: citación **en el
  domicilio social** requiriendo **representante, Abogado y Procurador**, con advertencia de
  designación **de oficio de estos dos últimos**; se practica con representante y Abogado
  (**inasistencia del representante → se practica con el Abogado**); el **Juez informa de los hechos
  por escrito o entregando copia de la denuncia o querella**; la designación de Procurador **sustituye
  al domicilio** a efectos de notificaciones, **incluidas las personales**.
- **Art. 409 bis — declaración:** del **representante especialmente designado**, asistido de su
  Abogado, con derechos a **guardar silencio, no declarar contra sí misma y no confesarse culpable**.
  Dirigida a averiguar los hechos **y la participación en ellos de la entidad y de las demás
  personas** — *léase con el § 1 en la mano: la ley diseña esta declaración para que apunte a las
  personas físicas*. ⭐ **La incomparecencia hace que se tenga por celebrado el acto**, entendiéndose
  que **se acoge al derecho a no declarar**: opción táctica legítima y **sin coste procesal**.
- **Art. 786 bis — juicio oral:** el representante **ocupa el lugar de los acusados**; **declara solo
  si se propuso y admitió esa prueba**; conserva la **última palabra**. **No puede designarse a quien
  haya de declarar como TESTIGO.** Su **incomparecencia no impide** la vista (Abogado y Procurador).

**Checklist al recibir la citación:**
- [ ] **Incoación** y control del **art. 324 LECrim** (12 meses + prórrogas; sin auto previo al
      vencimiento las diligencias posteriores **no son válidas** — anclas § 3.1).
- [ ] ¿Información de hechos **por escrito** (119.1.c)? Si no, **protesta**.
- [ ] **Representante sin conflicto** (§ 1); **poder especial** si se prevé conformidad.
- [ ] ¿**Cautelares del 33.7** pedidas o acordadas?
- [ ] ¿`[ENTIDAD]` de **pequeñas dimensiones** (31 bis.3)? ¿PyG abreviada?
- [ ] ⭐ ¿El **tipo concreto prevé** responsabilidad de la PJ? Es **numerus clausus** («en los supuestos
      previstos en este Código») → **`buscar_articulo`**. Si no la prevé: **sobreseimiento**, no
      defensa de fondo.

---

## 6. Investigaciones internas — advertencia seria

Mal hecha, no solo no sirve de descargo: **destruye la defensa** y puede generar responsabilidad del
despacho.

**6.1 Secreto profesional.** El asesoramiento legal está cubierto (**542.3 LOPJ**; skill
`revision-secreto-profesional`). ⚠️ **Tensión estructural:** usarla **como prueba de descargo** implica
aportarla, y aportarla implica **renunciar al secreto sobre ella**. **No se puede aportar lo favorable
y retener lo desfavorable del mismo trabajo.** Decidir **antes de empezar** si nace para asesorar o
para aportarse, y construirla en consecuencia.

**6.2 Derechos fundamentales de los trabajadores.** Un empleado entrevistado por los abogados de la
empresa, en horario laboral y bajo deber contractual de colaboración, **no está en una conversación
libre**.
- **Informarle de sus derechos** y de que **no está obligado a autoincriminarse**; **ausencia de
  coacción** (no condicionar el empleo, no amenazar con despido).
- ⭐ **Aviso *Upjohn***: constancia **expresa, previa y firmada** de que el abogado representa a
  **`[ENTIDAD]`, NO al trabajador**; que el secreto **pertenece a la empresa**, que **puede renunciar a
  él y aportar lo declarado**; y que el trabajador **puede procurarse su propio abogado**.
- **Dispositivos y correo corporativo:** expectativa de privacidad, política previa conocida,
  proporcionalidad (**art. 18 CE** y normativa de protección de datos). Terreno minado.

> ⚠️ **PRUEBA ILÍCITA — art. 11.1 LOPJ** (verificado, redacción LO 1/2025, vigente 23-1-2025): «No
> surtirán efecto las pruebas obtenidas, **directa o indirectamente**, violentando los derechos o
> libertades fundamentales.» Una investigación que vulnere derechos del trabajador puede arrastrar,
> **por conexión de antijuridicidad**, todo lo que derive de ella — **incluido el material con el que
> `[ENTIDAD]` pretendía probar la elusión fraudulenta del 31 bis.2.3.º**. El tiro sale por la culata.
>
> **La doctrina sobre investigaciones internas, valor de las entrevistas y alcance del secreto está
> viva y NO es pacífica: `[verificar]` SIEMPRE con `buscar_sentencias`.** Nada de memoria.

**6.3 Canal de denuncias — Ley 2/2023.** Conecta con el **31 bis.5.4.º**. **Verificado — art. 10
(vigente 13-3-2023), obligados del sector privado:** **a)** **50 o más trabajadores**; **b)** entidades
del ámbito de los actos de la UE en **servicios, productos y mercados financieros, blanqueo o
financiación del terrorismo, seguridad del transporte y protección del medio ambiente** (Directiva
(UE) 2019/1937), **con independencia del número de trabajadores** —incluidas las que, sin domicilio en
España, operen aquí por sucursales, agentes o sin establecimiento permanente—; **c)** **partidos,
sindicatos, organizaciones empresariales y sus fundaciones**, **si reciben o gestionan fondos
públicos**. **10.2:** las no obligadas **pueden** implantarlo, pero **debe cumplir en todo caso los
requisitos de la ley** — un canal «voluntario» descuidado **no es neutro**.

> ⚠️ **Solo está verificado el art. 10.** Cualquier otra obligación, plazo, régimen sancionador o
> requisito (anonimato, acuse de recibo, responsable del sistema) → **`buscar_articulo` o
> `[verificar]`**. **Siglas ambiguas:** confirmar que es **BOE-A-2023-4513**.

---

## 7. Datos, entregable y reglas de la casa

- **Cero datos reales.** Marcadores: **`[ACUSADO]`**, **`[ENTIDAD]`**, **`[CIF]`**,
  **`[REPRESENTANTE]`**, **`[VÍCTIMA]`**. **Art. 10 RGPD** (infracciones y condenas): el nombre de
  `[ENTIDAD]` asociado a una investigación penal es riesgo **reputacional y de mercado** (contratación
  pública, financiación, cotización). **Nunca** el slug con el nombre de la entidad o del investigado
  → `descriptor-delito-año` (`PROTECCION-DATOS.md`). Config:
  `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.
- **Entregable: Word `.docx`** (skill **`docx`**) para LexNET; estilo `estilo-escritos-judiciales`;
  toda afirmación de hecho **anclada al folio**.
- Análisis → `matters/<slug>/pj-31bis-analisis.md`: 1) **conflicto de interés** (conclusión y fecha de
  la advertencia escrita); 2) **título de imputación** y beneficio; 3) **¿el tipo prevé la
  responsabilidad de la PJ?**; 4) **los cuatro requisitos del 31 bis.2** con prueba y valoración de
  acreditación **total o parcial**; 5) **penas en riesgo** (33.7) y **techos del 66 bis**; 6) **plan de
  atenuantes del 31 quater con calendario** anclado al comienzo del juicio oral; 7) **cautelares**;
  8) **puntos `[verificar]`**.

**Reglas:** **(1)** el **conflicto se resuelve antes que nada**: si la defensa de `[ENTIDAD]` pasa por
el 31 bis.2.3.º, no se puede defender también a `[ACUSADO]` — **art. 467.1 CP: es delito**; advertir
por escrito. **(2)** Verificar el **tipo concreto**: la responsabilidad de la PJ es **numerus
clausus**; si el tipo no la prevé → **sobreseimiento**. **(3)** **Ley penal en el tiempo** (art. 2 CP):
redacción a la fecha de los hechos y comparación si la posterior es más favorable (2.2); **LO 1/2026**
desde **10-4-2026** (anclas § 7.3). **(4)** **Auditar el modelo con honestidad** antes de construir la
defensa sobre él: uno cosmético prueba en contra (requisito 4.ª). **(5)** **Nunca renunciar a la
acreditación parcial** del 31 bis.2: es atenuación por mandato legal expreso. **(6)** Nada de
jurisprudencia de memoria → `buscar_sentencias` o `[verificar]`, y decirlo. **(7)** **Caducidad:** más
de 6 meses desde la última verificación de las anclas → re-verificar.
