---
name: prueba-ilicita-nulidad
description: Analiza y ataca la prueba obtenida con vulneración de derechos fundamentales (art. 11.1 LOPJ) y la nulidad de actuaciones (arts. 238 y 240 LOPJ), y prepara la alegación para la AUDIENCIA PRELIMINAR del art. 785 LECrim. Actívala ante "prueba ilícita", "nulidad de la prueba", "nulidad de actuaciones", "el registro fue ilegal", "entraron sin orden", "entrada y registro nula", "pinchazo telefónico", "intervención de comunicaciones sin motivación", "me miraron el móvil", "registro del móvil", "geolocalización", "agente encubierto", "cadena de custodia rota", "declaró sin abogado", "sin información de derechos", "efecto reflejo", "conexión de antijuridicidad", "frutos del árbol envenenado", "diligencias fuera de plazo del 324", "cuestiones previas".
---

# Prueba ilícita y nulidad — art. 11.1 LOPJ

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Texto vigente de los arts. 11, 238 y 240 LOPJ y de los arts. 18 y 24 CE** → `buscar_articulo` (`ley="LOPJ"` / `ley="CE"`).
- **Medidas de investigación tecnológica (arts. 588 bis a – 588 septies c LECrim)** → `buscar_articulo` (`ley="LECrim"`, `articulo="588 bis a"`… hasta `"588 septies c"`), uno por uno.
- **Conexión de antijuridicidad y efecto reflejo** → `buscar_sentencias` (`base="TC"` y, para la Sala Segunda, `jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3` y `terminos` («conexión de antijuridicidad»).
- **Conservación y acceso a datos de comunicaciones** → `buscar_sentencias` (`base="TJUE"`, consulta sobre la Directiva 2002/58/CE).
- **Diligencias acordadas fuera del plazo de instrucción** → `buscar_articulo` (`ley="LECrim"`, `articulo="324"`).
- **Resoluciones que invoque la acusación para salvar la prueba** → `buscar_por_cita`.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

El eje de la defensa penal. Objetivo: identificar el **derecho fundamental afectado**, decidir si estamos ante **prueba ilícita** o ante **prueba irregular**, mapear las **pruebas derivadas** y alegarlo **en la audiencia preliminar del art. 785 LECrim** con **protesta** expresa.

> **⚠️ Sede de la alegación — actualizado LO 1/2025 (vigente 3-4-2025).** La nulidad de actuaciones y la nulidad de la prueba **ya no se plantean al inicio del juicio oral**: su sede es la **audiencia preliminar del art. 785.1**. Todo material anterior a abril de 2025 que hable de "cuestiones previas del art. 786.2" **está desactualizado**. Ver § 4 y la skill `audiencia-preliminar-abreviado`.

---

## 1. La norma sobre la que gira todo — art. 11.1 LOPJ

Texto **literal vigente** (verificado con `buscar_articulo`, BOE-A-1985-12666, redacción LO 1/2025, vigente desde 23-1-2025):

> **Artículo 11.**
> **1. En todo tipo de procedimiento se respetarán las reglas de la buena fe. No surtirán efecto las pruebas obtenidas, directa o indirectamente, violentando los derechos o libertades fundamentales.**

Tres palabras hacen todo el trabajo:

- **«No surtirán efecto»** — no es una nulidad que haya que pedir y que el tribunal *pueda* conceder: es una **ineficacia radical**. Apreciable de oficio.
- **«directa o indirectamente»** — es el **anclaje legal del efecto reflejo**. La prueba derivada también cae. El debate no es *si* existe efecto reflejo (lo dice la ley), sino **hasta dónde** llega (§ 3).
- **«derechos o libertades fundamentales»** — no cualquier ilegalidad. **Solo** la vulneración de un derecho fundamental. Este es el filtro que separa el § 2.

---

## 2. Prueba ilícita vs. prueba irregular — **distinguirlas bien es la mitad del trabajo**

Es el primer error de los escritos de defensa: pedir la ineficacia del art. 11.1 LOPJ por una infracción que es de **legalidad ordinaria**. El tribunal desestima y se pierde el argumento bueno.

| | **Prueba ILÍCITA** | **Prueba IRREGULAR** |
|---|---|---|
| **Qué se infringe** | Un **derecho fundamental** (arts. 18, 24.2, 17 CE) | Solo la **legalidad ordinaria** procesal |
| **Régimen** | **Art. 11.1 LOPJ** — no surte efecto | **Arts. 238 y 240 LOPJ** — nulidad de actuaciones |
| **Alcance** | Se extiende a las derivadas («directa o indirectamente») | **No hay efecto reflejo**; en principio solo cae el acto |
| **Requiere indefensión** | **No** — la ineficacia es automática | **Sí**, por regla general (art. 238.3.º) |
| **Sanabilidad** | No subsanable | A menudo **subsanable**; puede bastar la repetición |
| **Ejemplo típico** | Registro domiciliario sin consentimiento válido ni auto motivado (art. 18.2 CE) | Defecto formal en el acta de una diligencia acordada válidamente |

### Arts. 238 y 240 LOPJ — el régimen de la irregular

Verificados con `buscar_articulo`:

- **Art. 238 LOPJ** (vigente desde 1-10-2015) — nulidad de pleno derecho de los actos procesales: **1.º** falta de jurisdicción o de competencia objetiva o funcional; **2.º** violencia o intimidación; **3.º** cuando se prescinda de **normas esenciales del procedimiento, siempre que por esa causa haya podido producirse indefensión**; **4.º** sin intervención de abogado cuando sea preceptiva; **5.º** vistas sin la preceptiva intervención del LAJ; **6.º** demás casos legales.
- **Art. 240 LOPJ** (vigente desde 15-1-2004) — **cómo se hace valer**: por medio de los **recursos** legalmente establecidos contra la resolución de que se trate, o por los demás medios de las leyes procesales (240.1). El tribunal puede declararla de oficio o a instancia de parte, **antes de que recaiga resolución que ponga fin al proceso** y siempre que no proceda subsanación, **previa audiencia de las partes** (240.2).

**Regla de trabajo:** identifica primero el **derecho fundamental**. Si no lo hay, no invoques el art. 11.1 LOPJ — reconduce a los arts. 238/240 y **acredita la indefensión material**, que es lo que el art. 238.3.º exige. Si hay derecho fundamental, invoca el art. 11.1 LOPJ **y**, subsidiariamente, la nulidad de actuaciones.

### Los derechos fundamentales en juego

- **Art. 18 CE** (verificado): 18.1 honor, **intimidad** personal y familiar, propia imagen; **18.2 inviolabilidad del domicilio** — «Ninguna entrada o registro podrá hacerse en él sin consentimiento del titular o resolución judicial, **salvo en caso de flagrante delito**»; **18.3 secreto de las comunicaciones** — «salvo resolución judicial»; 18.4 límites al uso de la informática.
- **Art. 24.2 CE** (verificado): Juez ordinario predeterminado por la ley, **defensa y asistencia de letrado**, ser informado de la acusación, proceso con todas las garantías, **utilizar los medios de prueba pertinentes**, **no declarar contra sí mismo**, **no confesarse culpable**, **presunción de inocencia**.
- **Art. 17 CE**: libertad personal — sede de los vicios de la detención.

---

## 3. ⚠️ Efecto reflejo y conexión de antijuridicidad — **NO CITAR DE MEMORIA**

El art. 11.1 LOPJ dice que la ineficacia alcanza a lo obtenido **«indirectamente»**. Pero el alcance real de esa proyección lo ha construido la **jurisprudencia del TC y de la Sala Segunda del TS** mediante la llamada **doctrina de la conexión de antijuridicidad**: se trata de decidir si la prueba derivada está de tal modo ligada a la originaria que deba compartir su suerte, o si es **jurídicamente independiente** y puede valorarse.

> **⛔ PROHIBIDO en esta skill citar sentencias de memoria.** Ni ECLI, ni ROJ, ni fecha, ni ponente, ni párrafos entrecomillados. Esta es la materia donde la tentación es máxima y donde una cita inventada destruye la credibilidad del escrito y expone al letrado.
>
> **Obligatorio antes de fundar el escrito:** verificar la **doctrina vigente** con `buscar_sentencias` (y `buscar_por_cita` / `leer_sentencias` para confirmar cada resolución que se vaya a citar) del **TC** y de la **Sala Segunda del TS**. La doctrina de la conexión de antijuridicidad ha sido **matizada y reformulada** en el tiempo: no basta con lo que uno recuerda. Búsquedas sugeridas: «conexión de antijuridicidad prueba refleja», «prueba ilícita derivada art. 11.1 LOPJ», «hallazgo inevitable», «fuente independiente».

### Límites que suelen invocarse — **todos son construcciones jurisprudenciales: verificar cada uno**

Ninguno de estos límites está en el texto del art. 11.1 LOPJ. Son creaciones de la jurisprudencia, de recepción y perfil variables. **Marcarlos siempre como `[verificar]`** y comprobar su vigencia y formulación exacta antes de invocarlos o de rebatirlos:

- **Fuente independiente** `[verificar]` — la prueba derivada se habría obtenido por un cauce autónomo, sin relación con la vulneración.
- **Hallazgo inevitable** `[verificar]` — la prueba se habría descubierto igualmente en el curso ordinario de la investigación.
- **Descubrimiento probablemente independiente** `[verificar]` — variante atenuada de la anterior; su recepción es discutida.
- **Buena fe** `[verificar]` — de origen anglosajón; su acogida en el Derecho español es **especialmente controvertida**. No darla por buena.
- **Confesión posterior del acusado** `[verificar]` — supuesto de altísima litigiosidad: si el acusado, ya con abogado e informado de la ilicitud, confiesa, se discute si esa confesión rompe la conexión. **Verificar imperativamente**: la doctrina ha evolucionado y el detalle importa.

**Como defensa**, la carga argumental es doble: (a) acreditar la vulneración originaria; (b) **trazar el nexo** causal y jurídico con cada prueba derivada, folio a folio. **Como acusación**, el trabajo es el inverso: sostener la independencia.

---

## 4. ⭐ CUÁNDO y DÓNDE se alega — **punto crítico, LO 1/2025**

Verificado literalmente en el **art. 785 LECrim** (`buscar_articulo`, redacción LO 1/2025, **vigente desde 3-4-2025**):

- **785.1** — el órgano de enjuiciamiento convoca al fiscal y a las partes a una **audiencia preliminar** en la que podrán exponer lo que estimen oportuno acerca de, entre otras cuestiones, **la vulneración de algún derecho fundamental**, la existencia de **artículos de previo pronunciamiento**, la **nulidad de actuaciones**, y **el contenido, finalidad o nulidad de las pruebas propuestas**.
- **785.2** — la celebración **requiere la asistencia del acusado y del abogado defensor**.
- **785.3** — el órgano resuelve **oralmente**, salvo que por la **complejidad** de las cuestiones haya de hacerlo por escrito, en cuyo caso el **auto** se dicta en **10 días**. **«Contra la resolución adoptada no cabrá recurso alguno, sin perjuicio de la pertinente protesta y de que la cuestión pueda ser reproducida, en su caso, en el recurso frente a la sentencia»**, salvo que ponga fin al procedimiento → **apelación** (arts. 790 y ss.).

### ⭐ Sin protesta no hay gravamen

Insistir hasta la pesadez: si el tribunal **rechaza** la nulidad en la audiencia preliminar, la resolución es **irrecurrible**. La **única** vía de acceso al recurso contra la sentencia es haber **formulado la protesta en el acto**. Omitirla equivale a consentir. **Hacerla constar expresamente y comprobar que queda registrada** (la comparecencia se registra conforme al art. 743 — art. 785.12).

### Reservar la cuestión para el juicio es llegar tarde

Verificado en el **art. 787.3 LECrim** (redacción LO 1/2025): al inicio de las sesiones del juicio **únicamente** podrá solicitarse la incorporación de informes, certificaciones y otros documentos, y proponerse la práctica de pruebas **de las que las partes no hubieran tenido conocimiento al momento de celebrar la comparecencia prevista en el artículo 785**.

**Consecuencia:** el juicio oral **ya no es sede** para plantear la nulidad. Quien se la guarde para el trámite de cuestiones previas del viejo esquema se la encuentra **precluida**.

---

## 5. Supuestos frecuentes en los que atacar

Para cada uno: derecho fundamental afectado → norma infringida → qué buscar en las actuaciones.

### 5.1 Entrada y registro
- **Art. 18.2 CE** + **arts. 545 y ss. LECrim**. Verificado: **art. 545 LECrim** — «Nadie podrá entrar en el domicilio de un español o extranjero residente en España sin su consentimiento, excepto en los casos y en la forma expresamente previstos en las leyes.»
- Solo tres títulos habilitantes (art. 18.2 CE): **consentimiento del titular**, **resolución judicial** o **flagrante delito**.
- **Qué atacar:** validez del **consentimiento** — si lo presta un **detenido**, comprobar que fue informado de sus derechos, que estaba **asistido de letrado** y que consintió libremente y por escrito; consentimiento de cotitular frente al ausente; **motivación** del auto (indicios objetivos, no meras sospechas); **presencia del LAJ** y su falta como vicio; extralimitación del registro respecto de lo autorizado; concepto constitucional de domicilio (vehículos, trasteros, habitaciones de hotel, sedes de personas jurídicas). Comprobar los requisitos concretos en **arts. 545 y ss. LECrim** con `buscar_articulo` antes de citar ordinales.

### 5.2 Intervención de comunicaciones y medidas de investigación tecnológica
- **Art. 18.3 CE** + **arts. 588 bis a y ss. LECrim** (medidas de investigación tecnológica, introducidas por la LO 13/2015).
- **Principios rectores — art. 588 bis a**: **especialidad, idoneidad, excepcionalidad, necesidad y proporcionalidad** `[verificar]`.
- **Autorización judicial y motivación — art. 588 bis c** `[verificar]`.
- **⛔ Prohibición de investigaciones PROSPECTIVAS**: la medida debe dirigirse a un **delito concreto** ya indiciariamente perfilado, no a *ver qué aparece*. El principio de **especialidad** excluye las medidas exploratorias. Es el ataque más rentable contra oficios policiales genéricos y autos que se limitan a asumirlos por remisión.
- **Qué atacar:** ausencia o insuficiencia de **motivación** del auto (motivación por remisión al oficio policial sin control judicial propio); falta de **indicios objetivos** previos frente a meras conjeturas; **desproporción** con la gravedad del delito; **prórrogas** sin control ni dación de cuenta; **falta de aportación de los soportes originales**; **hallazgos casuales** de delito distinto al investigado.

> **⚠️ `[verificar]` — limitación de herramienta.** El conector `buscar_articulo` **no ha podido recuperar** los arts. **588 bis a**, **588 bis c** ni **588 sexies** LECrim (la búsqueda trunca el sufijo alfabético y devuelve «no encontrado»). Su contenido **no está verificado contra el BOE** en esta skill. **Antes de citar cualquiera de estos preceptos —numeración, ordinales, requisitos o penas— hay que comprobar el texto vigente directamente en el BOE consolidado** (BOE-A-1882-6036) o por otra vía. **No dar por buena de memoria** la formulación de los principios rectores ni el régimen del registro de dispositivos.

### 5.3 Registro de dispositivos de almacenamiento masivo — **art. 588 sexies** `[verificar]`
- **Art. 18.1 y 18.4 CE** (intimidad; entorno digital).
- **La regla clave `[verificar]`**: la aprehensión lícita del dispositivo **no habilita** para acceder a su contenido. Se exige **autorización judicial específica y motivada** para el registro, **aunque el dispositivo se haya intervenido lícitamente** (p. ej., hallado en un registro domiciliario válido o incautado en la detención).
- **Qué atacar:** el auto de entrada y registro que **no menciona** los dispositivos; el volcado sin autorización; la extralimitación del acceso más allá de lo autorizado; el acceso policial al móvil del detenido «para comprobar un dato».
- **⛔ Verificar la numeración exacta y el contenido** (`588 sexies a`, `b`, `c`) en el BOE **antes de citarlos**. No verificado aquí.

### 5.4 Otros supuestos
- **Geolocalización** (balizas, datos de localización) — **art. 18.1 CE**; arts. 588 quinquies b y ss. `[verificar]`. Atacar motivación, duración y control de las prórrogas.
- **Agente encubierto** — art. 282 bis LECrim `[verificar]`. Frontera con el **delito provocado**: si la voluntad criminal la **crea** el agente, no hay delito, y la prueba es inhábil. Distinguir de la mera aportación de ocasión a quien ya había resuelto delinquir. Verificar la doctrina con `buscar_sentencias`.
- **Cadena de custodia** — ojo: **por regla general es un problema de *irregularidad* y de fiabilidad de la prueba, no de ilicitud del art. 11.1 LOPJ**, salvo que se conecte con una vulneración de derecho fundamental. Encajarla mal es el error clásico. Atacar la **mismidad** de lo analizado (identidad entre lo intervenido y lo periciado): precintos, etiquetas, actas, custodios, fechas y horas de cada eslabón, folio a folio. El efecto habitual no es la nulidad sino la **pérdida de fiabilidad probatoria** → presunción de inocencia (art. 24.2 CE).
- **Declaración del detenido sin información de derechos o sin abogado** — **arts. 17.3 y 24.2 CE** + **art. 520 LECrim**. Ver anclas § 8. Comprobar: información de derechos **por escrito**, en lenguaje **sencillo y accesible** y de forma **inmediata** (520.2); derecho a **guardar silencio** y a **no declarar contra sí mismo**; asistencia de letrado **sin demora injustificada** y plazo de **3 horas** del art. 520.5; **entrevista reservada previa** con el letrado **antes** de la declaración (520.6.d); renuncia a la asistencia letrada **solo** posible en delitos **exclusivamente** contra la seguridad del tráfico (520.8). Verificar el precepto con `buscar_articulo` antes de citar apartados.

### 5.5 ⭐ Diligencias fuera del plazo del art. 324 LECrim — **conéctalo**
Verificado (`buscar_articulo`, redacción Ley 2/2020, vigente desde 29-7-2020):

- **324.1** — la investigación judicial se desarrolla en un plazo máximo de **12 meses desde la incoación**; **prórrogas sucesivas** por periodos **iguales o inferiores a 6 meses**, de oficio o a instancia de parte, **oídas las partes**, mediante **auto** motivado que exponga las causas, las **concretas diligencias** pendientes y su relevancia.
- **324.2** — las diligencias acordadas **antes** del transcurso del plazo o de sus prórrogas **son válidas aunque se reciban después**.
- **⭐ 324.3** — «**Si, antes de la finalización del plazo o de alguna de sus prórrogas, el instructor no hubiere dictado la resolución a la que hace referencia el apartado 1, o bien esta fuera revocada por vía de recurso, no serán válidas las diligencias acordadas a partir de dicha fecha.**»

**Cómo se conecta con esta skill:** el art. 324.3 produce una **invalidez legal directa** —no requiere vulneración de derecho fundamental ni acreditar indefensión— de todas las diligencias acordadas a partir del vencimiento. Es el argumento de nulidad **más rentable y más desatendido**, y su sede natural de alegación es también la **audiencia preliminar del art. 785.1** (nulidad de actuaciones / nulidad de las pruebas).

**Operativo obligatorio:** construir la **línea temporal** — fecha de **incoación**; fecha de cada **auto de prórroga** y su fecha de **dictado** (no la de notificación); si cada uno se dictó **antes** del vencimiento anterior; si alguno fue **revocado en recurso**; y **fecha de acuerdo** de cada diligencia de cargo. Toda diligencia acordada tras un vencimiento no cubierto por auto previo → **inválida**. Cruzar con la skill `cronologia`.

---

## 6. Método de trabajo

1. **Mapa de la vulneración.** Para cada prueba de cargo: derecho fundamental afectado → norma infringida → **folio** exacto de las actuaciones. Sin folio no hay alegación.
2. **Clasificar**: ¿ilícita (art. 11.1 LOPJ) o irregular (arts. 238/240 LOPJ)? No mezclar. Alegar la principal y, **subsidiariamente**, la otra.
3. **Verificar el texto vigente** de cada precepto con `buscar_articulo` **antes** de citarlo. Los arts. 588 bis/sexies **no son recuperables** con la herramienta: comprobarlos en el BOE. Lo no verificable → `[verificar]` **y decirlo**.
4. **Verificar la doctrina** con `buscar_sentencias` / `buscar_por_cita` / `leer_sentencias`. **Cero citas de memoria.**
5. **Árbol de derivadas.** Prueba originaria → cada prueba derivada, con el **nexo** explicado. Anticipar los límites que opondrá la acusación (§ 3) y rebatirlos.
6. **Pronóstico honesto.** Probabilidad de éxito y, sobre todo, **qué queda en pie** si la nulidad prospera: si tras expulsar la prueba ilícita y sus derivadas subsiste prueba de cargo suficiente, la nulidad no absuelve. Decirlo al cliente.
7. **Preparar la audiencia preliminar** y la **protesta**. Coordinar con `audiencia-preliminar-abreviado`.

---

## 7. Salida

Dos entregables:

### 7.1 Informe de viabilidad de la nulidad
| Campo | Contenido |
|---|---|
| Prueba atacada | Identificación y **folio** |
| Derecho fundamental afectado | Art. 18.2 / 18.3 / 18.1 / 24.2 / 17 CE |
| Norma infringida | Precepto concreto **verificado** |
| Calificación | **Ilícita** (art. 11.1 LOPJ) / **irregular** (arts. 238-240 LOPJ) |
| Prueba originaria | Descripción y folio |
| Pruebas **derivadas** | Listado, con el **nexo** con la originaria, folio a folio |
| Límites que opondrá la acusación | Fuente independiente / hallazgo inevitable / confesión posterior — `[verificar]` cada uno |
| Doctrina verificada | Resultado de `buscar_sentencias` — **solo lo confirmado** |
| **Pronóstico** | Probabilidad y **prueba de cargo subsistente** si prospera |

### 7.2 Borrador del escrito / alegación para la audiencia preliminar
- Encabezamiento al órgano de enjuiciamiento, con nº de procedimiento abreviado.
- Invocación expresa del **art. 785.1 LECrim** como cauce.
- **Alegación primera** — vulneración del derecho fundamental: hecho, folio, norma, **art. 11.1 LOPJ** e ineficacia directa e indirecta.
- **Alegación segunda** — pruebas derivadas y nexo.
- **Subsidiariamente** — nulidad de actuaciones, arts. 238 y 240 LOPJ, con **acreditación de la indefensión material**.
- **SUPLICO**: se declare que la prueba **no surte efecto** ex art. 11.1 LOPJ y su exclusión, así como la de las derivadas; subsidiariamente, la nulidad.
- **⭐ OTROSÍ — PETICIÓN EXPRESA DE PROTESTA**: que, para el caso de desestimación, **se tenga por formulada la oportuna PROTESTA a los efectos del art. 785.3 LECrim**, y por reservada la reproducción de la cuestión en el recurso frente a la sentencia. **Nunca omitir este otrosí.**
- Lugar, fecha y firma.

**Entregable en Word `.docx`** maquetado para LexNET (skill `docx`). Estilo de la casa: `estilo-escritos-judiciales`.

---

## 8. Reglas de la casa

- **⛔ NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. La reforma que atribuiría la instrucción al Ministerio Fiscal está **en tramitación**, con entrada en vigor prevista para **1-1-2028**: no describirla como Derecho vigente ni citar un «art. 4 bis EOMF».
- **⛔ Nada de MASC.** Es del orden **civil**. Aquí no existe.
- **⛔ Prohibido inventar** penas, plazos, ordinales o artículos. Lo no verificable → `[verificar]` **y decirlo**.
- **⛔ Prohibido citar jurisprudencia concreta** (ECLI, ROJ, fecha, ponente, párrafos) sin haberla verificado con el conector `jurisprudenciator`. **Crítico en esta skill.**
- **Datos personales:** marcadores `[ACUSADO]`, `[INVESTIGADO]`, `[VÍCTIMA]`, `[FECHA]`. **Cero datos reales.** Los datos sobre infracciones y condenas son de **categoría especial** (**art. 10 RGPD**). Ver `PROTECCION-DATOS.md`.
- Perfil del despacho: `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.
- Anclas verificadas: `references/anclas-normativas-penal.md` (§ 1 reformas, § 2 LO 1/2025, § 3.1 art. 324, § 8 art. 520).

## 9. Skills relacionadas

`audiencia-preliminar-abreviado` (sede de la alegación) · `cronologia` (línea temporal del art. 324) · `escrito-defensa-calificacion` · `recurso-apelacion-sentencia-penal-catalogo` (reproducción de la cuestión) · `subsuncion-juridica`.
