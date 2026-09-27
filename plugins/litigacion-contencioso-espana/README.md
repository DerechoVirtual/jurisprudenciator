# Litigación contencioso-administrativa — España

Plugin de Claude Code para despachos que litigan ante la **jurisdicción
contencioso-administrativa** española. Cubre el ciclo completo del asunto: vía administrativa
previa, control de plazos y admisibilidad, proceso contencioso, recursos y ejecución.

**Marco normativo:** LJCA (Ley 29/1998) · LPAC (Ley 39/2015) · LRJSP (Ley 40/2015) · LEC
supletoria (DF 1.ª LJCA).

> **Ámbito exclusivo.** Este plugin es **solo** contencioso-administrativo. No cubre civil,
> mercantil, familia, laboral ni penal.
>
> **El MASC de la LO 1/2025 no se aplica en esta jurisdicción** — es un requisito de
> procedibilidad del orden civil. El equivalente funcional aquí es el **agotamiento de la vía
> administrativa** (art. 25.1 LJCA).

---

## Primer uso: tu estilo

La primera vez que el plugin vaya a redactar, te pedirá entre 3 y 5 escritos tuyos de referencia y aprenderá tu forma de escribir: fórmulas, estructura, tono, forma de citar y maquetación. El perfil se guarda una sola vez y lo usan todos los plugins de Jurisprudenciator. Puedes actualizarlo cuando quieras con la skill `perfil-de-estilo`.

## Instalación y primer uso

1. Añade el marketplace de Jurisprudenciator: https://jurisprudenciator.lexiaipro.org/plugins
2. Instala desde él el plugin `litigacion-contencioso-espana`. El conector **Jurisprudenciator** viene
   incluido: la primera vez pide iniciar sesión con la cuenta de Jurisprudenciator.
3. Ejecuta **`/cold-start-interview`** para configurar el perfil del despacho y comprobar el conector.
4. Abre tu primer asunto con **`/asunto-intake`**.

El perfil y los asuntos se escriben **fuera** del plugin, en
`~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/`. El `CLAUDE.md` que
viaja con el plugin es una **plantilla vacía**: nunca escribas datos reales en él.
Ver [`PROTECCION-DATOS.md`](PROTECCION-DATOS.md).

---

## Conector

| Conector | Para qué | Endpoint |
|---|---|---|
| **Jurisprudenciator** (MCP, incluido en el plugin) | Jurisprudencia oficial (**TS Sala Tercera**, AN, TSJ, juzgados, TC y TJUE) con párrafo literal y ECLI; artículos vigentes y verificación de las citas de un escrito; BOE y BORME; Registro Mercantil; consultas de la DGT y doctrina del TEAC; ordenanzas municipales; Catastro; convenios colectivos | `https://mcp.jurisprudenciator.lexiaipro.org/mcp` |

**Es la única vía de jurisprudencia y legislación del plugin.** Cada skill indica, en su sección
«Jurisprudenciator en esta skill», qué dato de esa tarea sale de qué herramienta. Ninguna skill puede
inventar un ECLI, un ROJ, una fecha ni el texto de un artículo.

**Sin Jurisprudenciator no se trabaja.** Cada skill empieza comprobando el conector (`estado`) y saca de él todos los datos jurídicos. Si no está conectado, falla o no devuelve lo que la tarea necesita (sentencias, el artículo, el convenio...), la skill se detiene y pide conectarlo: nunca sigue de memoria ni con citas pendientes.

**¿Ya tienes Jurisprudenciator en Claude?** Lo normal es tenerlo conectado con tu URL personal (https://jurisprudenciator.lexiaipro.org/instalacion): las skills usan ese. Si no, conecta el que trae el plugin e inicia sesión con tu cuenta.

**Conectores del despacho (opcionales).** El plugin trae también Google Drive, Gmail, Google Calendar, Microsoft 365 (Outlook, OneDrive, SharePoint), Dropbox, Box y DocuSign. Conecta solo los que uses; en la app de Claude están en la pestaña Conectores del plugin. Sirven para los documentos, el correo, los señalamientos y la firma, nunca como fuente de jurisprudencia o legislación. Los documentos del despacho pueden estar en una carpeta local o en cualquiera de esos servicios; se indica en `/cold-start-interview`.

### Límite de cobertura que debes conocer

El conector cubre **Derecho estatal (BOE)** y de la UE, jurisprudencia, doctrina de la DGT y del
TEAC, Catastro y **ordenanzas municipales de los municipios cubiertos**. **No cubre la normativa autonómica** ni los boletines
provinciales no incluidos. Como buena parte del Derecho administrativo material es autonómico y
local (urbanismo, actividades, tributos locales), en esas materias el plugin **te pedirá la norma**
en lugar de citarla de memoria. Es deliberado.

---

## Catálogo de skills

### Control de riesgo — córrelas antes de redactar nada

| Skill | Qué hace |
|---|---|
| `/computo-plazos-ca` | Calcula el plazo de **caducidad** (2 meses / 6 meses / 10-20 días vía de hecho), aplica la regla de agosto y el silencio administrativo, y devuelve fecha de vencimiento y margen de presentación |
| `/admisibilidad-ca` | Checklist del art. 69 LJCA: jurisdicción, legitimación, acto impugnable, agotamiento de vía, documentos del art. 45.2 (incluido el acuerdo corporativo), plazo |
| `/expediente-administrativo-ca` | Reclamación, auditoría y foliado del expediente; detección de huecos y escrito de ampliación (art. 55 LJCA) |

### Vía administrativa

| Skill | Qué hace |
|---|---|
| `/recurso-alzada-reposicion-ca` | Recursos de alzada (arts. 121-122 LPAC) y reposición (arts. 123-124 LPAC) |
| `/procedimiento-sancionador-ca` | Defensa en sancionador: caducidad, prescripción, tipicidad, culpabilidad, proporcionalidad; y su impugnación contenciosa |
| `/responsabilidad-patrimonial-ca` | Reclamación de responsabilidad patrimonial (arts. 32-37 LRJSP) y su impugnación |

### Proceso contencioso

| Skill | Qué hace |
|---|---|
| `/interposicion-recurso-contencioso-ca` | Escrito de interposición (art. 45 LJCA) |
| `/demanda-contencioso-administrativa` | Demanda (arts. 52-56 LJCA) |
| `/contestacion-demanda-ca` | Contestación y alegaciones previas (arts. 54, 58 LJCA) — posición pasiva |
| `/procedimiento-abreviado-ca` | Abreviado (art. 78 LJCA), con la reforma de la LO 1/2025 |
| `/proteccion-derechos-fundamentales-ca` | Procedimiento preferente y sumario (arts. 114-122 LJCA) |
| `/medidas-cautelares-ca` | Suspensión del acto y cautelares (arts. 129-136 LJCA) |
| `/impugnacion-disposiciones-generales-ca` | Recurso directo e indirecto contra reglamentos y cuestión de ilegalidad (arts. 26-27, 123-126 LJCA) |
| `/autorizacion-entrada-domicilio-ca` | Autorizaciones de entrada del art. 8.6 LJCA (ejecución forzosa, sanitarias, CNMC, tributaria) |
| `/escrito-conclusiones-ca` | Conclusiones del art. 64 LJCA (ordinario) y del abreviado, con variantes de nulidad de pleno derecho, responsabilidad patrimonial sanitaria, urbanismo y Seguridad Social |

### Recursos, costas y ejecución

| Skill | Qué hace |
|---|---|
| `/recurso-apelacion-ca` | Apelación ante la Sala del TSJ (arts. 81-85 LJCA) |
| `/preparacion-recurso-casacion-ca` | Preparación de casación por interés casacional objetivo (arts. 86-89 LJCA) |
| `/costas-ca` | Riesgo de costas, tope del tercio (art. 139.4 LJCA), tasación e impugnación |
| `/ejecucion-sentencias-ca` | Ejecución contra la Administración (arts. 103-113 LJCA) |
| `/extension-efectos-ca` | Extensión de efectos de sentencias firmes (arts. 110-111 LJCA) — personal y tributaria |

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

[`references/anclas-normativas-ca.md`](references/anclas-normativas-ca.md) contiene los plazos,
umbrales y requisitos **verificados contra el BOE consolidado** artículo por artículo
(última verificación: **2026-07-17**). Es la fuente única de verdad del plugin para cifras.

Recoge, entre otras, las tres reformas recientes de la LJCA que cambian la práctica:

| Norma | En vigor | Qué cambió |
|---|---|---|
| **RD-ley 5/2023** | 29-07-2023 | Emplazamiento ante el TS: de 30 a **15 días** (art. 89.5) |
| **RD-ley 6/2023** | 20-03-2024 | Representación (art. 23), apelación en extensión de efectos (art. 81.2.e), **tope de costas del tercio** (art. 139.4) |
| **LO 1/2025** | 03-04-2025 | Legitimación sindical (art. 45.2.e), abreviado: vista rogada y motivada, expediente electrónico, sentencia oral (art. 78) |

> Si han pasado más de 6 meses desde la última verificación, re-verifica antes de confiar en el
> documento. La LJCA se ha modificado tres veces entre 2023 y 2025.

---

## Lo que este plugin no hace

- **No sustituye al abogado.** Redacta borradores y controla riesgos; la firma, la estrategia y la
  responsabilidad son del letrado.
- **No inventa jurisprudencia.** Si no puede verificar una cita, lo dice.
- **No conoce tu normativa autonómica ni tus ordenanzas** si no están cubiertas por el conector.
  Te las pedirá.
- **No calcula plazos que no puedas comprobar.** Ante la duda sobre una caducidad, avisa y
  recomienda verificación humana: el coste de equivocarse es la pérdida irreversible de la acción.
