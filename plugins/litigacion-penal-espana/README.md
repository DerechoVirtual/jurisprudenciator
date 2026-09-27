# Litigación penal — España

Plugin de Claude Code para despachos que litigan ante la **jurisdicción penal** española. Cubre el
ciclo completo del asunto: guardia y detención, instrucción, fase intermedia, juicio oral, recursos
y ejecutoria.

**Marco normativo:** LECrim (RD de 14 de septiembre de 1882) · CP (LO 10/1995) · LOPJ (LO 6/1985) ·
CE (arts. 17, 18 y 24) · leyes especiales (LO 5/1995 Jurado, LO 5/2000 Menores, Ley 4/2015 Estatuto
de la víctima, LO 6/1984 Habeas corpus, LO 10/2022, LO 1/2004).

> **Ámbito exclusivo.** Este plugin es **solo** penal. No cubre civil, mercantil, familia, laboral
> ni contencioso-administrativo. La **acción civil derivada del delito** sí entra: se ejercita en el
> proceso penal.
>
> **El MASC de la LO 1/2025 no se aplica en el orden penal** — es un requisito de procedibilidad del
> orden civil.
>
> **No existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. La reforma que
> atribuiría la instrucción al Ministerio Fiscal está **en tramitación**, con entrada en vigor
> prevista para **1-1-2028**. El plugin describe únicamente la ley vigente.

---

## Instalación y primer uso

1. Añade el marketplace de Jurisprudenciator: https://jurisprudenciator.lexiaipro.org/plugins
   (en Claude Code: `/plugin marketplace add https://jurisprudenciator.lexiaipro.org/plugins`).
2. Instala el plugin **`litigacion-penal-espana`** (en Claude Code:
   `/plugin install litigacion-penal-espana@jurisprudenciator`). La primera vez que una skill consulte
   Jurisprudenciator, Claude te pedirá iniciar sesión con tu cuenta de Jurisprudenciator.
3. Ejecuta **`/cold-start-interview`** para configurar el perfil del despacho.
4. Abre tu primer asunto con **`/asunto-intake`**.

El perfil y los asuntos se escriben **fuera** del plugin, en
`~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`. El `CLAUDE.md` que viaja con el
plugin es una **plantilla vacía**: nunca escribas datos reales en él.

> ⚠️ **Protección de datos.** En penal los datos de **infracciones y condenas** tienen régimen propio
> (**art. 10 RGPD**), más estricto que las categorías especiales del art. 9. Lee
> [`PROTECCION-DATOS.md`](PROTECCION-DATOS.md) antes de usar el plugin en asuntos reales.

---

## Conector: Jurisprudenciator

**¿Ya tienes Jurisprudenciator en Claude?** Lo normal es tenerlo conectado con tu URL personal (https://jurisprudenciator.lexiaipro.org/instalacion): las skills usan ese. Si no, conecta el que trae el plugin e inicia sesión con tu cuenta. Endpoint del plugin: `https://mcp.jurisprudenciator.lexiaipro.org/mcp`.
Cada skill indica, en su sección «Jurisprudenciator en esta skill», qué dato de la tarea sale de qué
herramienta.

| Qué ofrece | Para qué sirve en penal |
|---|---|
| Jurisprudencia oficial (TS Sala Segunda, AN, TSJ, AP, juzgados, TC y TJUE) con párrafo literal y ECLI | Fundar cada escrito con la doctrina exacta y verificar las citas de la otra parte |
| Artículos vigentes y norma que dio la redacción | Penas, plazos y ley penal en el tiempo |
| Verificación de citas de un borrador | Revisar el escrito antes de presentarlo |
| BOE y BORME | Normas, edictos, requisitorias, indultos y actos societarios |
| Registro Mercantil | Personas jurídicas, administradores de hecho y de derecho |
| Catastro, ordenanzas y convenios colectivos | Alzamiento y usurpación, delitos urbanísticos, delitos contra los trabajadores |
| Hacienda y TEAC | Delitos contra la Hacienda Pública |

**Es la única vía de jurisprudencia y legislación del plugin.** Ninguna skill puede inventar un
ECLI, un ROJ, una pena ni el texto de un artículo. En penal esto no es una formalidad — una pena mal citada es un error con consecuencias.

**Sin Jurisprudenciator no se trabaja.** Cada skill empieza comprobando el conector (`estado`) y saca de él todos los datos jurídicos. Si no está conectado, falla o no devuelve lo que la tarea necesita (sentencias, el artículo, el convenio...), la skill se detiene y pide conectarlo: nunca sigue de memoria ni con citas pendientes.

**Conectores del despacho (opcionales).** El plugin trae también Google Drive, Gmail, Google Calendar, Microsoft 365 (Outlook, OneDrive, SharePoint), Dropbox, Box y DocuSign. Conecta solo los que uses; en la app de Claude están en la pestaña Conectores del plugin. Sirven para los documentos, el correo, los señalamientos y la firma, nunca como fuente de jurisprudencia o legislación.

---

## Catálogo de skills

### Urgencia — guardia y detención

| Skill | Qué hace |
|---|---|
| `/asistencia-detenido` | Checklist operativo del art. 520 LECrim: los 10 derechos, el plazo de **3 horas** del letrado, las 72 horas de la detención, la entrevista reservada previa, y la decisión de declarar o no |
| `/habeas-corpus` | Procedimiento de la LO 6/1984 cuando la detención es ilegal |
| `/juicio-rapido` | Arts. 795-803 LECrim y la decisión de conformarse en la guardia con la **reducción de un tercio** (art. 801) |

### Control de riesgo — córrelas antes de redactar nada

| Skill | Qué hace |
|---|---|
| `/computo-plazos-penal` | **Art. 324 LECrim** (12 meses de instrucción y validez de las diligencias tras cada prórroga), prescripción del delito (art. 131 CP) y de la pena (art. 133 CP), plazos de recurso |
| `/ley-penal-en-el-tiempo` | Qué redacción del CP se aplica (art. 2 CP) y si la posterior es **más favorable**. Con dos reformas en 15 meses, ya no es teórico |
| `/prueba-ilicita-nulidad` | Art. 11.1 LOPJ: prueba ilícita frente a irregular, efecto reflejo, y **dónde se alega ahora** (audiencia preliminar del art. 785) |

### Instrucción

| Skill | Qué hace |
|---|---|
| `/denuncia-estafa` | Denuncia por estafa (art. 248 CP), con la frontera del negocio civil criminalizado |
| `/denuncia-derechos-trabajadores` | Delitos contra los derechos de los trabajadores (arts. 311-318 CP) |
| `/querella-catalogo` | Querella (arts. 277-281 LECrim), acción popular y su fianza |
| `/personacion-acusacion-particular-catalogo` | Personación de la víctima (arts. 109-110, 776 LECrim; Ley 4/2015) |
| `/solicitud-diligencias-instruccion-catalogo` | Diligencias de investigación, con el reloj del art. 324 |
| `/alegaciones-oposicion-sobreseimiento` | Oposición al sobreseimiento libre (art. 637) o provisional (art. 641) |
| `/recurso-reforma-apelacion-auto-archivo` | Recursos contra el auto de archivo |
| `/recurso-reforma-apelacion-auto-apertura-jo` | Recursos contra el auto de apertura de juicio oral |
| `/medidas-cautelares-penales-catalogo` | Prisión provisional (arts. 502-505), **art. 544 bis reformado**, orden de protección (544 ter), fianza y embargo |

### Fase intermedia y juicio oral

| Skill | Qué hace |
|---|---|
| `/escrito-defensa-calificacion` | Escrito de defensa (art. 784 LECrim), conclusiones del art. 650 |
| `/escrito-acusacion-accidente-laboral` | Acusación por siniestralidad laboral (arts. 316-318 CP) |
| `/escrito-acusacion-frustracion-ejecucion` | Acusación por frustración de la ejecución (arts. 257 y ss. CP) |
| `/audiencia-preliminar-abreviado` | **Trámite nuevo de la LO 1/2025** (art. 785): conformidad, nulidades, cuestiones previas y prueba. Es el momento decisivo del abreviado |
| `/conformidad-penal-catalogo` | Conformidad del art. 785 (abreviado) y del art. 801 (guardia) |
| `/violencia-genero-orden-proteccion` | Competencia de la **Sección de Violencia sobre la Mujer**, orden de protección (544 ter) y art. 544 bis |
| `/responsabilidad-penal-personas-juridicas` | Art. 31 bis CP, modelos de compliance y el conflicto de interés estructural |
| `/tribunal-jurado` | LO 5/1995: fases propias y el **objeto del veredicto** |
| `/delitos-leves` | Arts. 962-977 LECrim, prescripción de **1 año** y el efecto de la multirreincidencia |

### Recursos y ejecución

| Skill | Qué hace |
|---|---|
| `/recurso-apelacion-sentencia-penal-catalogo` | Apelación (art. 790), con la suspensión del plazo por petición de las grabaciones |
| `/recurso-casacion-penal-catalogo` | Casación ante la Sala Segunda — **los motivos dependen de la resolución recurrida** (art. 847) |
| `/ejecucion-penal-liquidacion-condena-suspension-catalogo` | Liquidación de condena, abono de la preventiva (art. 58 CP) y suspensión (**art. 80 CP reformado**) |

### Gestión del despacho y de la cartera

`/cold-start-interview` · `/customize` · `/asunto-intake` · `/actualizar-asunto` ·
`/briefing-asunto` · `/cerrar-asunto` · `/portfolio-status` · `/matter-workspace` ·
`/colaboradores-status` · `/hoja-encargo` · `/requerimiento-judicial-triage` ·
`/conservacion-documental` · `/revision-secreto-profesional`

### Trabajo jurídico transversal

`/cronologia` · `/cuadro-elementos` · `/subsuncion-juridica` · `/preparacion-interrogatorio` ·
`/redactor-escrito-seccion` · `/estilo-escritos-judiciales`

---

## Anclas normativas

[`references/anclas-normativas-penal.md`](references/anclas-normativas-penal.md) contiene las penas,
plazos y requisitos **verificados contra el BOE consolidado** artículo por artículo (última
verificación: **2026-07-17**). Es la fuente única de verdad del plugin para cifras.

Recoge las **dos reformas recientes** que cambian la práctica:

| Norma | En vigor | Qué cambió |
|---|---|---|
| **LO 1/2025**, de 2 de enero | **03-04-2025** | **Reestructura el juicio oral del abreviado**: nueva **audiencia preliminar** (art. 785), a la que se traslada la **conformidad**; el art. 786 pasa a ser el señalamiento y el **art. 787, la celebración del juicio oral**. Todo material anterior cita mal estos artículos. |
| **LO 1/2026**, de 8 de abril, **de multirreincidencia** | **10-04-2026** | **CP:** arts. 22.8ª, 66.2, **80** (suspensión), 234.2 (hurto leve), 235.1 (nuevo **10.º: teléfonos móviles**), **248** (estafa, reescrito), 250.1.8º, nuevo 255.3, nuevo 568.2 (*petaqueo*). **LECrim:** arts. 13, nuevo **105.3** (acción penal de las entidades locales por hurto) y **544 bis**. |

> Si han pasado más de 6 meses desde la última verificación, re-verifica antes de confiar en el
> documento.

---

## Lo que este plugin no hace

- **No sustituye al abogado.** Redacta borradores y controla riesgos; la firma, la estrategia y la
  responsabilidad son del letrado. En penal está en juego la libertad de una persona.
- **No inventa jurisprudencia ni penas.** Si no puede verificar una cita, lo dice.
- **No calcula plazos que no puedas comprobar.** Ante la duda sobre una prescripción o sobre el
  vencimiento del art. 324, avisa y recomienda verificación humana.
- **No anticipa la ley futura.** Describe el Derecho vigente. La reforma del fiscal instructor
  (prevista para 2028) no está en el plugin, y es deliberado.
