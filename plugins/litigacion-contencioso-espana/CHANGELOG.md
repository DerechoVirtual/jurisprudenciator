# Changelog

## 0.3.0 — 2026-09-27

### Cambiado — Jurisprudenciator en todas las skills

- Las 39 skills llevan, justo después del título, una sección «Jurisprudenciator en esta skill» que
  dice qué dato de esa tarea sale de qué herramienta del conector (jurisprudencia con párrafo literal
  y ECLI, artículos vigentes, verificación de citas, BOE, ordenanzas, Catastro, doctrina del TEAC y de
  Hacienda, Registro Mercantil) y qué hacer si una consulta falla: marcar el dato como
  `[pendiente de verificar]`, nunca completarlo de memoria.
- Se retiran los avisos antiguos sobre el conector de `briefing-asunto`, `cold-start-interview`,
  `customize`, `redactor-escrito-seccion` y `subsuncion-juridica`: su contenido queda en la sección
  nueva.
- `CLAUDE.md` describe todo lo que ofrece Jurisprudenciator e incluye una tabla «necesidad →
  herramienta» para el orden contencioso.

### Cambiado — gestor documental

- El `.mcp.json` configura solo Jurisprudenciator. Dropbox deja de instalarse con el plugin: el
  despacho guarda sus documentos donde prefiera (carpeta local, OneDrive, Google Drive o Dropbox si
  el abogado lo tiene conectado).
- `cold-start-interview` y `customize` comprueban las integraciones llamando a `estado` de
  Jurisprudenciator y, opcionalmente, al gestor documental que el abogado tenga conectado.
- `README.md`: instalación desde el marketplace de Jurisprudenciator.

## 0.2.0 — 2026-07-17

Revisión mayor. El plugin era un fork del plugin de litigación **civil** con once skills
contencioso-administrativas añadidas encima. Esta versión lo convierte en un plugin
contencioso-administrativo real: descontamina las skills heredadas, robustece el núcleo y cubre
los huecos. Todos los plazos y umbrales se han verificado artículo por artículo contra el BOE
consolidado.

### Corregido — errores que podían costar un asunto

- **Colisión del directorio de configuración.** Todas las skills escribían el perfil y los asuntos
  en `~/.claude/plugins/config/derecho-virtual/**litigacion-civil-espana-pro**/`, el directorio del
  plugin civil. Además de mezclar dos carteras de clientes en un mismo repositorio de datos
  personales, hacía que el perfil contencioso pisara al civil. Ahora:
  `.../litigacion-contencioso-espana/`.
- **MASC exigido en una jurisdicción donde no existe.** El intento de MASC de la LO 1/2025 es
  requisito de procedibilidad del orden **civil**. El plugin lo pedía, lo rastreaba
  (`masc_acreditado`) y **bloqueaba la redacción de demandas** por su ausencia. Eliminado de raíz.
  Su equivalente funcional —el **agotamiento de la vía administrativa** (art. 25.1 LJCA)— pasa a
  rastrearse en su lugar.
- **Recurso de alzada: «3 meses si el acto es presunto».** Era el art. 115.1 de la **Ley 30/1992,
  derogada en 2016**. Desde la Ley 39/2015 el recurso contra acto presunto se interpone **«en
  cualquier momento»** (arts. 122.1 y 124.1 LPAC).
- **Procedimiento abreviado: «cuestiones de tráfico».** El art. 78.1 LJCA no menciona el tráfico.
  Las materias son personal, extranjería, inadmisión de asilo y **disciplina deportiva en materia
  de dopaje**; el tráfico entra **por cuantía** (≤ 30.000 €).
- **Preparación de casación: faltaba un requisito obligatorio.** La skill listaba cinco apartados
  del art. 89.2 LJCA y omitía la **letra c)** (acreditar que se pidió la subsanación en la
  instancia cuando la infracción es de garantías procesales que produjeron indefensión). Son
  **seis**. Omitir uno → auto teniendo el recurso **por no preparado** (art. 89.4), recurrible solo
  en queja. El art. 93.2.b) lo recoge además como causa expresa de inadmisión.
- **Art. 78.6 LJCA presentado como «conclusiones orales».** Es la **apertura de la vista** por el
  demandante. Las conclusiones del abreviado están en otros apartados, y existe además un trámite
  de **conclusiones escritas de 5 días** (art. 78.3 in fine) que solo se abre si se rechazó la vista
  y el actor lo pidió en la demanda.
- **Tachas de testigos en el abreviado.** La skill de interrogatorio mandaba plantear tachas del
  art. 377 LEC. El **art. 78.15 LJCA** dispone que los testigos **no podrán ser tachados** y que las
  observaciones se hacen **únicamente en conclusiones**.
- **Prescripción civil aplicada al contencioso.** El intake calculaba prescripción por los
  arts. 1964/1968/1969 CC. Los plazos de interposición del contencioso son de **caducidad**
  (art. 46 LJCA) y **no se interrumpen** por burofax ni reclamación extrajudicial.
- **Cómputo de plazos por LEC 133 y postulación por art. 23 LEC.** Sustituidos por el
  **art. 128.2 LJCA** (agosto) y el **art. 23 LJCA** (procurador potestativo ante Juzgados,
  preceptivo ante Salas).
- **Cuota litis: cita desfasada.** La hoja de encargo invocaba una prohibición basada en la STS de
  4-11-2008. El **art. 26 EGA (RD 135/2021)** establece hoy la libre fijación de honorarios.

### Añadido — reformas que el plugin no conocía

| Norma | En vigor | Impacto |
|---|---|---|
| **RD-ley 5/2023** | 29-07-2023 | Emplazamiento ante el TS: de 30 a **15 días** (art. 89.5) |
| **RD-ley 6/2023** | 20-03-2024 | Art. 23 (representación); art. 81.2.e (apelación en extensión de efectos); **art. 139.4: tope de costas de 1/3 de la cuantía por favorecido, 18.000 € si es indeterminada**; art. 48 (expediente electrónico, multas coercitivas); art. 55 (régimen de reinicio del plazo) |
| **LO 1/2025** | 03-04-2025 | Art. 45.2.e (legitimación sindical); art. 78 (vista rogada y motivada, expediente electrónico, sentencia oral) |

### Añadido — nueve skills

Control de riesgo: `computo-plazos-ca` · `admisibilidad-ca` · `expediente-administrativo-ca`
Materias: `procedimiento-sancionador-ca` · `impugnacion-disposiciones-generales-ca` ·
`autorizacion-entrada-domicilio-ca`
Proceso: `contestacion-demanda-ca` (posición pasiva, que no existía)
Recursos: `costas-ca` · `extension-efectos-ca`

### Añadido — documentación

- **`references/anclas-normativas-ca.md`** — fuente única de verdad. Plazos, umbrales y requisitos
  verificados contra el BOE artículo por artículo, con fecha de verificación y regla de caducidad
  a los 6 meses. Ninguna skill puede afirmar una cifra que no esté aquí o que no verifique en el
  momento.
- **`PROTECCION-DATOS.md`** — política de datos, resultado de la auditoría y checklist previa a
  compartir el plugin.
- **`CHANGELOG.md`** — este archivo.

### Protección de datos

- Auditoría de los 34 archivos: **cero hallazgos** de DNI, IBAN, correos, teléfonos, direcciones o
  nombres de clientes reales. El `CLAUDE.md` ya era una plantilla con marcadores.
- Eliminados los ejemplos **con apariencia de cliente real** heredados del plugin civil (nombre de
  persona física, razón social de contraparte y procurador nominado en el `_log.yaml`).
  Sustituidos por ejemplos descritos **por materia**, sin nombres.
- Retirada de `plugin.json` y `README.md` la frase «basadas en plantillas reales del despacho,
  anonimizadas»: aunque el contenido esté despersonalizado, documenta por escrito un tratamiento
  de datos de clientes y no aporta nada al usuario.
- Añadida a las skills que tocan el expediente la advertencia sobre **datos de terceros** y sobre
  los **datos de salud** como categoría especial del **art. 9 RGPD**.
- Regla nueva: los **slugs de asunto se construyen por materia**, no por apellido — un listado de
  carpetas no debe revelar la cartera de clientes.

### Hallazgos incorporados durante la verificación

Reglas verificadas contra el BOE que ninguna skill recogía y que cambian la práctica:

- **Silencio positivo de segundo grado** (art. 24.1 párr. 3.º LPAC): recurrida en alzada una
  desestimación presunta, si la Administración vuelve a callar los 3 meses, **la alzada se entiende
  estimada** — salvo en las materias del párrafo anterior, entre ellas **responsabilidad
  patrimonial**.
- **Contra un reglamento no cabe recurso administrativo** (art. 112.3 LPAC). Quien interpone
  reposición contra una ordenanza consume los 2 meses del recurso directo y llega tarde.
- **Prueba obligatoria en sancionador** (art. 60.3 LJCA): si el objeto es una sanción, el proceso
  **se recibirá siempre a prueba** cuando haya disconformidad en los hechos, sin margen de
  apreciación judicial.
- **Recibimiento a prueba solo por otrosí** (art. 60.1 LJCA) en demanda, contestación o alegaciones
  complementarias. Olvidarlo deja el asunto sin prueba.
- **Expediente incompleto** (art. 55.3 LJCA): pedir la ampliación **dentro de los 10 primeros días**
  reinicia el plazo; pedirla el día 11 solo lo reanuda. Nunca reinicia si la pide la Administración.
- **Agosto no suspende la vía administrativa:** el art. 128.2 LJCA suspende los plazos «de esta
  Ley». El mes de alzada es un plazo de la Ley 39/2015 y **corre en agosto**.
- **Costas en casación** (art. 93.4): **no** rige el vencimiento objetivo — cada parte paga las
  suyas y las comunes por mitad, salvo mala fe o temeridad motivada.
- **Extensión de efectos** (art. 110 LJCA): son **tres** materias —tributaria, personal y **unidad
  de mercado** (Ley 20/2013)—, plazo único de **1 año** desde la última notificación a quienes
  fueron parte, y solicitud **directa al órgano judicial**.
- **Ejecución dineraria** (art. 106.3): **3 meses** para instar la ejecución forzosa, frente a los
  2 meses del régimen general del art. 104.2.
- **Art. 53.2 LPAC no recoge el derecho a no declarar contra uno mismo** — se invoca por el
  art. 24.2 CE.
- **Tráfico desplaza el régimen sancionador general** (RDL 6/2015): prescripción, caducidad y
  reducción propias; tras el pago con reducción el acto sigue siendo recurrible **en vía
  contenciosa** (art. 94.d).

---

## 0.1.0

Versión inicial. Once skills contencioso-administrativas sobre la base de un fork del plugin de
litigación civil.
