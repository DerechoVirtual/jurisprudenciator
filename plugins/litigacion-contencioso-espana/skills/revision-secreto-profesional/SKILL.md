---
name: revision-secreto-profesional
description: Primera pasada de clasificacion de comunicaciones y documentos bajo el secreto profesional del abogado (art. 542.3 LOPJ y art. 5 del Codigo Deontologico) en asuntos contencioso-administrativos. Marca cubiertos, dudosos y no cubiertos, y detecta datos de terceros en el expediente administrativo. Usar con revisar secreto profesional.
---

# Revisión de secreto profesional — contencioso-administrativo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Marco del secreto y del acceso al expediente** → `buscar_articulo` (`ley="LOPJ"`, `articulo="542"`; `ley="LPAC"`, artículos 13 y 53; `ley="LJCA"`, `articulo="48"`; `ley="Ley 19/2013"`, `articulo="15"`).
- **Datos de salud y minimización** → `buscar_articulo` (`ley="RGPD"`, artículos 5 y 9).
- **Tipo penal de revelación** → `buscar_articulo` (`ley="CP"`, `articulo="199"`).
- **Deberes del Estatuto General de la Abogacía** → `buscar_boe` + `leer_boe` (RD 135/2021) antes de citar su art. 48.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Revisar secreto profesional", "clasificar comunicaciones"
- Ante requerimiento de aportar documentación que pueda incluir comunicaciones cubiertas
- **Antes de aportar documentos con la demanda o con el escrito de conclusiones** (filtrar lo que NO se debe aportar)
- **Al recibir el expediente administrativo** — pasada obligatoria: ver § "Datos de terceros"
- Antes de remitir documentación a un perito o al procurador
- Tras un intercambio masivo de correos en un asunto

## Marco

- **Art. 542.3 LOPJ** — Los abogados deberán guardar secreto de todos los hechos o noticias de que conozcan por razón de cualquiera de las modalidades de su actuación profesional, **no pudiendo ser obligados a declarar sobre los mismos**.
- **Art. 5 del Código Deontológico de la Abogacía Española** — secreto profesional: deber y derecho del abogado.
- **Art. 199 CP** — tipificación penal de la revelación.
- **Excepciones tasadas:** Ley 10/2010 PBC/FT (obligación de comunicación en los supuestos legalmente previstos), autorización judicial específica en los casos previstos, y **relevación por el propio cliente**.

### Dimensión propia del contencioso-administrativo

El eje del problema aquí **no es solo** proteger la comunicación abogado-cliente. Es que **el expediente administrativo llega al despacho lleno de datos de personas que no son nuestro cliente**.

- El expediente lo remite la Administración al órgano judicial (art. 48 LJCA) y las partes acceden a él. Puede contener: **otros interesados** en el procedimiento, **denunciantes**, terceros afectados, informes sobre **historiales clínicos de terceros**, datos de empleados públicos, alegaciones de vecinos, listados de opositores.
- **Nunca reproducir ni difundir esos datos.** No trasladarlos al cliente más allá de lo imprescindible para su defensa, no incorporarlos a escritos si no son necesarios para el fundamento, no compartirlos con peritos salvo lo estrictamente preciso, y no volcarlos en ficheros del despacho sin necesidad.
- **El acceso a esa información está limitado:**
  - **Art. 13.d) LPAC** — el derecho de acceso a la información pública, archivos y registros se ejerce **de acuerdo con lo previsto en la Ley 19/2013** de transparencia y el resto del ordenamiento. No es un acceso libre.
  - **Art. 15 Ley 19/2013** — protección de datos personales: si la información contiene datos que revelan **ideología, afiliación sindical, religión o creencias**, el acceso exige **consentimiento expreso y por escrito** del afectado; si contiene datos sobre **origen racial, salud o vida sexual, datos genéticos o biométricos, o infracciones penales o administrativas** sin amonestación pública, exige **consentimiento expreso** o amparo en **norma con rango de ley**. Fuera de esos casos, el órgano pondera el interés público y los derechos de los afectados. Si los datos se **disocian**, el régimen no aplica (art. 15.4). Y la normativa de protección de datos **rige el tratamiento posterior** de lo obtenido (art. 15.5).
  - **RGPD** — principio de **minimización** (art. 5.1.c). Los **datos de salud** son **categoría especial** del **art. 9 RGPD**: su tratamiento en el proceso se ampara en el **art. 9.2.f** (formulación, ejercicio o defensa de reclamaciones), lo que legitima usarlos **para el pleito**, no para nada más.
  - **Art. 53.1.a) LPAC** — el **interesado** sí tiene derecho a conocer el estado del procedimiento y a **acceder y obtener copia de los documentos** contenidos en los procedimientos en que lo sea. Es el título de acceso de nuestro cliente a su propio expediente — distinto del acceso general del art. 13.d).
  - **Art. 48.6 LJCA** — del expediente se excluyen, mediante resolución motivada, los documentos clasificados como **secreto oficial**, haciéndolo constar en el índice y en el lugar del expediente.

> ⚠️ **El expediente administrativo NO está cubierto por el secreto profesional.** Es la prueba del proceso y llega por vía judicial. Lo que exige es un **tratamiento cuidadoso de los datos de terceros** que contiene. Son dos problemas distintos: no confundirlos.

## Categorización por defecto

### ✅ Claramente cubierto (NO aportar)

- Correos abogado ↔ cliente durante la relación profesional
- Notas internas del abogado sobre la estrategia procesal (viabilidad del recurso, riesgo de inadmisión, valoración de la prueba)
- Borradores no presentados de escritos (interposición, demanda, conclusiones)
- Dictamen de viabilidad emitido al cliente (art. 48.6 EGA: el cliente es el destinatario exclusivo salvo autorización expresa)
- Comunicaciones del abogado con peritos **contratados para asesoramiento**, antes de que el informe se aporte al proceso
- Comunicaciones con colaboradores externos en el contexto del asunto
- Instrucciones del cliente sobre desistir, allanarse o aceptar la satisfacción extraprocesal

### 🟡 Dudoso (marcar para revisión letrada)

- Correos abogado-cliente de asunto mixto jurídico-empresarial (p. ej. "recurso contra la sanción + cómo reorganizamos la actividad")
- **Informe pericial y comunicaciones con el perito una vez el informe se aporta al proceso** — el informe pasa a ser prueba; los correos previos de trabajo, no necesariamente
- Comunicaciones que involucran a terceros (familia del cliente, otros profesionales, otros interesados del expediente)
- Comunicaciones en que el cliente manifiesta la intención de cometer un ilícito futuro
- Documentos del cliente entregados al abogado pero no creados por él
- Escritos presentados por el cliente **en vía administrativa antes de contratar al abogado** — son suyos y públicos en el expediente, pero pueden revelar estrategia
- Comunicaciones del cliente con la Administración por canales informales (llamadas al funcionario, correos al técnico municipal)

### ❌ Claramente NO cubierto (aportar si se requiere)

- **El expediente administrativo y todo su contenido** — es la prueba del proceso, no comunicación profesional (**pero ver § Datos de terceros**)
- La **resolución impugnada** y su notificación
- Las **alegaciones presentadas en vía administrativa** con su justificante de registro
- Documentos del cliente preexistentes a la relación profesional (contratos, facturas, licencias)
- Comunicaciones del cliente con terceros que no son su abogado
- Hechos públicos; disposiciones publicadas en boletines oficiales
- Documentos del proceso judicial (autos, providencias, sentencias, escritos presentados)

### 🔴 Datos de terceros — categoría propia (NO reproducir aunque no estén cubiertos por secreto)

Documentos que **sí** forman parte del expediente y **sí** podemos usar en el pleito, pero cuyos datos de terceros **no deben reproducirse ni difundirse**:

- Identidad y datos del **denunciante** en expedientes sancionadores
- Alegaciones, recursos y datos de **otros interesados** (vecinos en urbanismo, otros opositores en función pública, otros licitadores en contratación)
- **Historias clínicas o informes médicos de terceros** que aparezcan en un expediente sanitario — **art. 9 RGPD, categoría especial**
- Datos de empleados públicos más allá de los meramente identificativos de su función (art. 15.2 Ley 19/2013)
- Listados, baremos y puntuaciones de otros aspirantes

**Tratamiento:** usar solo lo necesario para el fundamento del escrito; **disociar o anonimizar** cuando el dato personal no sea necesario (art. 15.4 Ley 19/2013); no trasladar al cliente copia íntegra de lo que contenga datos de terceros si no lo necesita para su defensa; no remitir al perito más que lo imprescindible.

## Flujo

### 1. Cargar input

- Lista de comunicaciones / documentos a clasificar (carpeta, lote, intercambio de correos, **expediente administrativo recibido**)
- Asunto + relación temporal entre los documentos y la apertura del encargo profesional

### 2. Clasificar cada documento

Para cada uno:
- Asignar categoría (✅ cubierto / 🟡 dudoso / ❌ no cubierto / 🔴 contiene datos de terceros)
- Razón breve, en una frase
- Un documento puede ser **❌ y 🔴 a la vez**: aportable, pero con datos de terceros que exigen tratamiento. Es el caso más común del expediente.

### 3. Output

`matters/<slug>/secreto-profesional-review.md`:

```markdown
# Revisión de secreto profesional — [slug]
Total documentos: [N]

## Cubiertos (N) — NO aportar
- [Doc 1] Correo cliente-abogado [fecha] — razón: comunicación durante el encargo profesional
- [Doc 2] Nota interna de viabilidad [fecha] — razón: estrategia procesal
- ..

## Dudosos (N) — REVISIÓN LETRADA OBLIGATORIA
- [Doc 5] Correo abogado-perito [fecha] — razón: el informe se aportó después al proceso;
  cobertura dudosa de los correos de trabajo previos
- ..

## No cubiertos (N) — Pueden aportarse si se requiere
- [Doc 12] Alegaciones en vía administrativa + justificante de registro [fecha] —
  razón: documento del expediente
- ..

## 🔴 Con datos de terceros (N) — aportables, pero NO reproducir los datos
- [Doc 20] Folios [X-Y] del expediente — denuncia de tercero — razón: identidad del
  denunciante; usar el contenido, no los datos identificativos
- [Doc 21] Folios [X-Y] — informe médico de tercero — razón: art. 9 RGPD, categoría
  especial; disociar
- ..

## Recomendaciones
- Antes de aportar el lote, decidir caso por caso los 🟡
- Disociar o anonimizar los 🔴 antes de citarlos en el escrito
- Si hay requerimiento: posible motivo de oposición sobre los ✅
```

### 4. Decision tree

> 1. **Revisar los 🟡 uno a uno** con el letrado
> 2. **Disociar los 🔴** antes de incorporarlos a un escrito
> 3. **Preparar oposición fundada al requerimiento** si afecta a documentos ✅
> 4. **Aportar los ❌** si así se ha decidido

## Reglas

1. **El secreto pertenece al cliente** — es renunciable por él, no por el abogado. Si el cliente quiere aportar una comunicación abogado-cliente, puede hacerlo.
2. **Excepciones tasadas:** Ley 10/2010 PBC/FT y autorización judicial específica en los supuestos previstos. Nada más.
3. **NUNCA hacer un juicio definitivo automatizado.** Esto es una primera pasada. El letrado revisa los 🟡 antes de aportar.
4. **El expediente administrativo no es secreto profesional, pero sí es un campo minado de datos de terceros.** Pasada obligatoria al recibirlo. Nunca reproducir ni difundir datos de terceros ajenos al cliente: su acceso está limitado por el **art. 13.d) LPAC** (que remite a la Ley 19/2013, cuyo art. 15 restringe el acceso a datos personales) y por el **RGPD**.
5. **Datos de salud = categoría especial (art. 9 RGPD).** En responsabilidad patrimonial sanitaria, la historia clínica del cliente se trata al amparo del art. 9.2.f RGPD (defensa de reclamaciones) y **solo para el pleito**. La de **terceros**, nunca sin base jurídica: disociar.
6. **Minimización (art. 5.1.c RGPD).** Al perito y al procurador solo se les remite lo estrictamente necesario para su función.
7. **Conservar los originales.** Aunque no se aporten al proceso, conservarlos en el despacho con cabecera de secreto. Recordar que el abogado **no puede retener documentación del cliente**, sin perjuicio de conservar copia (art. 48.7 EGA).
8. **Cero datos reales en la ficha.** Identificar por **slug** y por **folio del expediente**, no por nombre. Ningún DNI, IBAN, dirección, teléfono ni correo real en el archivo de revisión: marcadores entre corchetes.
9. **No inventar.** Cualquier artículo o plazo que no esté en `references/anclas-normativas-ca.md` se verifica con `buscar_articulo` o se marca `[verificar]`.
