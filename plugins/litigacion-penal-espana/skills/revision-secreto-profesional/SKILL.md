---
name: revision-secreto-profesional
description: >-
  Primera pasada de clasificacion de comunicaciones y documentos bajo el secreto profesional del abogado (art. 542.3 LOPJ), con las especialidades del penal: confidencialidad abogado-cliente de los arts. 118.4 y 520.7 LECrim, entrevista reservada con el detenido del art. 520.6.d, datos de terceros y antecedentes penales (art. 10 RGPD). Usar con revisar secreto profesional o clasificar comunicaciones.
---

# Revisión de secreto profesional — penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Núcleo del secreto** (art. 542.3 LOPJ; arts. 118.4, 416 y 520.7 LECrim; art. 466 CP) → `buscar_articulo`.
- **Comunicación abogado-cliente intervenida** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`; y `base="TC"`) + `leer_sentencias` con `parrafos=3`.
- **Secreto profesional del abogado en el Derecho de la UE** → `buscar_sentencias` (`base="TJUE"`).
- **Intervención de comunicaciones (arts. 588 ter a – 588 ter i LECrim)** → `buscar_articulo` (`ley="LECrim"`, `articulo="588 ter a"`… hasta `"588 ter i"`), uno por uno.
- **Datos penales de terceros (art. 10 RGPD)** → `buscar_articulo` (`ley="RGPD"`, `articulo="10"`).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

> 📐 **Cifras: `references/anclas-normativas-penal.md`**; lo que no esté ahí se verifica con `buscar_articulo` **antes** de afirmarlo.

## Cuándo activar

- "Revisar secreto profesional", "clasificar comunicaciones"
- Ante un **oficio o requerimiento** que pida al despacho aportar documentación
- Antes de aportar documentación a las actuaciones (filtrar lo que NO debe salir)
- Tras un intercambio masivo de correos en un asunto
- Antes de compartir material con un perito de parte o con un colaborador
- **Si se ha intervenido una comunicación abogado-cliente** → ver § "Comunicación intervenida"

## Marco — el núcleo

**⭐ Art. 542.3 LOPJ** *(literal verificado 2026-07-17)*:

> «Los abogados deberán guardar secreto de todos los hechos o noticias de que conozcan por razón de cualquiera de las modalidades de su actuación profesional, **no pudiendo ser obligados a declarar sobre los mismos**.»

Complementado por:

- **Art. 24.2 CE** *(verificado)* — «La ley regulará los casos en que, por razón de parentesco o de **secreto profesional**, no se estará obligado a declarar sobre hechos presuntamente delictivos.» El secreto tiene anclaje constitucional.
- **Art. 199 CP** *(verificado)* — revelación de secretos: el **profesional** que, incumpliendo su obligación de sigilo, divulgue los secretos de otra persona → **prisión de 1 a 4 años, multa de 12 a 24 meses e inhabilitación especial de 2 a 6 años** (art. 199.2).
- **EGA (RD 135/2021)** y Código Deontológico — secreto profesional como deber y derecho.

## Lo específico del PENAL

### 1. ⭐ Confidencialidad de las comunicaciones abogado-cliente

**Art. 118.4 LECrim** *(literal verificado 2026-07-17)*:

> «**Todas las comunicaciones entre el investigado o encausado y su abogado tendrán carácter confidencial.**
> Si estas conversaciones o comunicaciones hubieran sido captadas o intervenidas durante la ejecución de alguna de las diligencias reguladas en esta ley, **el juez ordenará la eliminación de la grabación o la entrega al destinatario de la correspondencia detenida**, dejando constancia de estas circunstancias en las actuaciones.
> Lo dispuesto en el párrafo primero **no será de aplicación cuando se constate la existencia de indicios objetivos de la participación del abogado en el hecho delictivo investigado** o de su implicación junto con el investigado o encausado en la comisión de otra infracción penal, sin perjuicio de lo dispuesto en la Ley General Penitenciaria.»

**Art. 520.7 LECrim** — las comunicaciones entre el **detenido** y su abogado son confidenciales, en los términos y con las excepciones del art. 118.4.

> **Regla operativa:** la confidencialidad es la norma; la excepción exige **indicios objetivos de participación del propio abogado** en el hecho delictivo. No basta la sospecha, ni la conveniencia investigadora, ni que el contenido sea incriminatorio para el cliente.

### 2. ⭐ Entrevista reservada con el detenido — incluso ANTES de declarar

**Art. 520.6.d) LECrim** *(verificado)* — la asistencia letrada comprende «**entrevistarse reservadamente con el detenido, incluso antes de que se le reciba declaración** por la policía, el fiscal o la autoridad judicial», salvo lo dispuesto en el art. 527.

**Art. 118.2 LECrim** *(verificado)* — el derecho de defensa comprende la asistencia de abogado «con el que podrá **comunicarse y entrevistarse reservadamente, incluso antes de que se le reciba declaración** por la policía, el fiscal o la autoridad judicial», sin perjuicio del art. 527.

> **Consecuencias para esta skill:**
> - El contenido de esa entrevista está **cubierto por el secreto en su integridad**. Nunca se documenta en un soporte que pueda salir del despacho, ni se comparte, ni se resume a terceros.
> - **Ejercer siempre el derecho.** Renunciar a la entrevista previa por prisa es un error de defensa.
> - Si se **impide o restringe** la entrevista reservada fuera de los supuestos del art. 527, **hacerlo constar en acta** (art. 520.6.b permite pedir la consignación en acta de cualquier incidencia) — es materia de nulidad.

### 3. ⭐ Dispensa del abogado como testigo

**Art. 416.2 LECrim** *(verificado)* — está dispensado de la obligación de declarar:

> «El Abogado del procesado respecto a los **hechos que éste le hubiese confiado en su calidad de defensor**.»

Y el art. 416.3 extiende la dispensa a los **traductores e intérpretes** de las comunicaciones entre el investigado y su abogado, respecto de los hechos a que se refiera su traducción.

> Si citan al letrado como testigo sobre lo que le confió su defendido: **dispensa del art. 416.2 LECrim + art. 542.3 LOPJ** (no puede ser obligado a declarar). Invocarlo expresamente y hacerlo constar.

### 4. ⭐ Revelación de actuaciones secretas — tipo penal PROPIO del abogado

**Art. 466.1 CP** *(literal verificado 2026-07-17)*:

> «**El abogado o procurador que revelare actuaciones procesales declaradas secretas por la autoridad judicial**, será castigado con las penas de **multa de doce a veinticuatro meses e inhabilitación especial** para empleo, cargo público, profesión u oficio **de uno a cuatro años**.»

> ⚠️ **Si la causa está declarada secreta (art. 302 LECrim — *verificar antes de citar*), el letrado no puede revelar las actuaciones a NADIE**, incluido, en los términos del secreto decretado, al propio cliente. Comprobar **siempre** si hay secreto de sumario acordado antes de compartir cualquier cosa.

### 5. ⭐ Las actuaciones contienen datos de TERCEROS y ANTECEDENTES PENALES → art. 10 RGPD

**Este es el punto que más se descuida.** El expediente penal no contiene solo datos del cliente:

| Categoría | Ejemplos |
|---|---|
| **Víctimas** | Identidad, domicilio, informes médicos y psicológicos, declaraciones, datos de salud |
| **Testigos** | Identidad, domicilio, teléfono, declaraciones — incluidos **testigos protegidos** (LO 19/1994 — *verificar antes de citar*) |
| **Otros investigados** | Identidad, declaraciones, antecedentes, situación personal |
| **⭐ Antecedentes penales** | Del cliente **y de terceros**, incorporados a la causa |
| **Menores** | Datos de especial protección |
| **Datos derivados de intervenciones** | Comunicaciones de terceros captadas incidentalmente en una intervención telefónica |

**Art. 10 RGPD** — el tratamiento de datos personales relativos a **condenas e infracciones penales** o medidas de seguridad conexas está sometido a un régimen reforzado, y solo puede llevarse a cabo bajo supervisión de la autoridad o cuando lo autorice el Derecho de la Unión o de los Estados miembros. Concordante: **art. 10 LO 3/2018**.

> **Regla operativa — NUNCA difundir:**
> - No compartir el expediente ni fragmentos con quien no sea parte necesaria de la defensa
> - No usar el material del asunto en formación, redes, ejemplos o consultas sin **anonimizar completamente**
> - No incorporar datos de víctimas ni testigos a documentos que salgan del despacho
> - **No nombrar el asunto con el nombre del cliente** en carpetas ni archivos (patrón `descriptor-delito-año`)
> - Si se comparte con un **perito de parte**, hacerlo con el mínimo material necesario y con encargo de confidencialidad por escrito
> - La difusión de datos de terceros del expediente **no está cubierta por ningún interés legítimo de la defensa** más allá de lo que exija el propio proceso

## Categorización por defecto

### ✅ Claramente cubierto (NO aportar):

- **Comunicaciones abogado ↔ cliente** durante la relación profesional — **art. 118.4 LECrim** (confidencialidad **legal**, no solo deontológica)
- **Comunicaciones con el detenido**, incluida la **entrevista reservada previa a la declaración** (arts. 520.6.d y 520.7)
- **Hechos que el defendido confió al letrado en su calidad de defensor** (art. 416.2 LECrim)
- **Notas internas** del abogado sobre la estrategia de defensa, valoración de prueba y de riesgo
- **Borradores** no presentados de escritos
- **Comunicaciones con peritos de parte** contratados para asesoramiento, **antes** de su intervención en el proceso
- **Comunicaciones con colaboradores externos** del despacho en el contexto del asunto
- **Comunicaciones con el procurador** sobre estrategia

### 🟡 Dudoso (marcar para revisión letrada):

- Comunicaciones con el **perito de parte tras su intervención en el proceso** — su informe y sus bases pasan a las actuaciones; la correspondencia estratégica previa, no
- Comunicaciones abogado-cliente de contenido **mixto** (jurídico + empresarial u operativo)
- Comunicaciones que **involucran a terceros** (familiares del cliente, otros profesionales, empleados) — ¿hubo confidencialidad?
- Comunicaciones en las que el cliente anuncia la **intención de cometer un ilícito futuro** — el secreto protege lo confiado sobre hechos pasados o actuaciones legítimas; el anuncio de un delito futuro se sitúa en el límite. **Escalar siempre al letrado y, si procede, al Colegio.**
- **Documentos del cliente entregados al abogado pero no creados por él** — no se vuelven secretos por depositarse en el despacho
- Material en el que aparecen **datos de víctimas o testigos** → aunque no esté cubierto por el secreto, su difusión está limitada por el **art. 10 RGPD**
- Comunicaciones con **coinvestigados o sus letrados** (defensas coordinadas) — valorar si hay acuerdo de confidencialidad
- Todo lo relativo a una causa **declarada secreta** → art. 466 CP: no revelar

### ❌ Claramente NO cubierto (puede aportarse si se requiere):

- Documentos del cliente **preexistentes** a la relación profesional (contratos, facturas — son del cliente, y no se blindan por entregarlos al abogado)
- Comunicaciones del **cliente con terceros** que no son su abogado
- **Hechos públicos**
- **Documentos del proceso** (autos, sentencias, escritos ya presentados)
- Comunicaciones cuando concurran **indicios objetivos de participación del propio abogado** en el hecho delictivo investigado o de su implicación en otra infracción junto al investigado (**excepción del art. 118.4 párr. 3**)

> ⚠️ La excepción del art. 118.4 párr. 3 **no la aprecia esta skill ni el letrado afectado**: la constata el órgano judicial. Si se invoca frente al despacho, **asistencia letrada propia y comunicación al Colegio**.

## Comunicación intervenida — qué hacer

Si se detecta que una comunicación abogado-cliente **ha sido captada o intervenida**:

1. **Art. 118.4 párr. 2**: el juez **ordenará la eliminación de la grabación** o la entrega al destinatario de la correspondencia detenida, **dejando constancia en las actuaciones**.
2. **Solicitarlo expresamente y por escrito**, sin demora.
3. Valorar **nulidad** de la diligencia y de la prueba derivada — **art. 11.1 LOPJ** (prueba obtenida con vulneración de derechos fundamentales) y **art. 238 LOPJ** *(verificar antes de citar)*.
4. **Comunicar al Colegio de Abogados** — la intervención de comunicaciones con el letrado activa el amparo colegial.
5. Si la intervención se produjo en **sede penitenciaria**, atender a la salvedad del art. 118.4 in fine sobre la Ley General Penitenciaria *(verificar)*.

## Flujo

### 1. Cargar input

- Lista de comunicaciones / documentos a clasificar
- Asunto y **relación temporal** entre cada documento y el inicio del encargo profesional
- ⭐ **Comprobar si la causa está declarada secreta**

### 2. Clasificar cada documento

Para cada uno:
- Categoría (✅ cubierto / 🟡 dudoso / ❌ no cubierto)
- Razón breve, en una frase, **con el artículo**
- ⭐ **Flag adicional `[TERCEROS]`** si contiene datos de víctimas, testigos, otros investigados o antecedentes penales → art. 10 RGPD, restricción de difusión **aunque no esté cubierto por el secreto**

### 3. Output

`matters/<slug>/secreto-profesional-review.md`:

```markdown
# Revisión de secreto profesional — [slug]
Total documentos: [N]
Causa declarada secreta: [sí / no]

## Cubiertos (N) — NO aportar
- [Doc 1] Comunicación cliente-letrado [fecha] — razón: confidencialidad legal, art. 118.4 LECrim
- [Doc 2] Nota de la entrevista reservada previa a declaración [fecha] — razón: art. 520.6.d LECrim
- ..

## Dudosos (N) — REVISIÓN LETRADA OBLIGATORIA
- [Doc 5] Correspondencia con perito de parte [fecha] — razón: posterior a su intervención en el proceso
- ..

## No cubiertos (N) — pueden aportarse si se requiere
- [Doc 12] Factura preexistente al encargo [fecha] — razón: documento del cliente anterior a la relación profesional
- ..

## ⚠️ [TERCEROS] — datos de terceros / antecedentes penales (art. 10 RGPD)
- [Doc 8] Declaración de testigo — contiene identidad y domicilio → NO difundir
- [Doc 9] Informe médico de la víctima → datos de salud, NO difundir
- [Doc 14] Certificado de antecedentes penales → art. 10 RGPD
- ..

## Recomendaciones
- Decidir caso por caso los 🟡 antes de aportar
- Si hay requerimiento: oposición motivada respecto de los ✅ (art. 542.3 LOPJ; art. 416.2 LECrim)
- Los [TERCEROS] no se difunden aunque no estén cubiertos por el secreto
- [Si causa secreta: no revelar actuaciones — art. 466 CP]
```

### 4. Decision tree

> 1. **Revisar los 🟡 uno a uno** con el letrado
> 2. **Preparar oposición fundada** al requerimiento si afecta a documentos ✅
> 3. **Aportar los ❌**, si así se decide, purgando previamente los `[TERCEROS]`
> 4. **Si hay comunicación intervenida** — solicitar eliminación (art. 118.4) y comunicar al Colegio

## Reglas

1. **El secreto pertenece al cliente**, no al abogado: es él quien puede relevar de él. Pero ⚠️ **el consentimiento del cliente NO habilita a difundir datos de terceros** (víctimas, testigos, otros investigados) que consten en las actuaciones — esos datos no son suyos y siguen protegidos por el **art. 10 RGPD**.
2. **Excepciones tasadas y de interpretación estricta**: art. 118.4 párr. 3 (indicios objetivos de participación del abogado), Ley 10/2010 PBC/FT en los supuestos sujetos, autorización judicial específica. **Nada más.**
3. **NUNCA hacer un juicio definitivo automatizado.** Esto es una primera pasada; el letrado revisa los 🟡 antes de aportar.
4. **Comprobar el secreto de sumario antes de compartir nada** — art. 466 CP.
5. **Conservar los documentos**, aunque no se aporten, con cabecera de secreto profesional. ⛔ **Nunca destruirlos** — arts. 451 y 465 CP; ver `/conservacion-documental`.
6. **Ejercer siempre la entrevista reservada previa a la declaración** (art. 520.6.d) y hacer constar en acta cualquier restricción.
7. **Verificar cada artículo con `buscar_articulo`** antes de invocarlo en un escrito.
8. ⛔ **Prohibido citar jurisprudencia concreta** (ECLI/ROJ/fecha) sin verificarla con `jurisprudenciator`.
9. **Cero datos reales** en outputs de ejemplo: `[CLIENTE]`, `[LETRADO]`, `[Doc N]`.

## Handoffs

- Si llega el requerimiento y hay que triarlo: `/requerimiento-judicial-triage`
- Si hay que aconsejar al cliente sobre conservación: `/conservacion-documental` — **el abogado no puede aconsejar destruir nada**
