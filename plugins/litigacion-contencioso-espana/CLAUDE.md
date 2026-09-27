# Perfil de despacho — [NOMBRE DEL DESPACHO]
# Plugin: litigacion-contencioso-espana
# Origen: plantilla genérica (completar con `/cold-start-interview`)

> Plantilla viva del despacho. Ajustar cualquier campo con `/customize` o rehacer con
> `/cold-start-interview`. Mientras tenga `[PLACEHOLDER]`/`[PENDIENTE]`, las skills que dependen
> del perfil pedirán configurarlo primero.
>
> ⚠️ **Este archivo viaja con el plugin y es una PLANTILLA VACÍA. Nunca escribir aquí datos
> reales.** El perfil cumplimentado se escribe en
> `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md`.
> Ver `PROTECCION-DATOS.md`.

---

## Ámbito del plugin

**Exclusivamente jurisdicción contencioso-administrativa.** Marco normativo:

- **LJCA** — Ley 29/1998, de 13 de julio, reguladora de la Jurisdicción Contencioso-administrativa.
- **LPAC** — Ley 39/2015, del Procedimiento Administrativo Común (vía administrativa previa,
  responsabilidad patrimonial, sancionador).
- **LRJSP** — Ley 40/2015, de Régimen Jurídico del Sector Público (responsabilidad patrimonial,
  potestad sancionadora).
- Supletoriamente, la **LEC** (DF 1.ª LJCA) — solo en lo no previsto por la LJCA.

> ⛔ **Fuera de ámbito:** civil, mercantil, familia, laboral y penal. Si el asunto no es
> contencioso-administrativo, decirlo y no forzar el encaje.
>
> ⛔ **El MASC de la LO 1/2025 NO se aplica en esta jurisdicción.** Es un requisito de
> procedibilidad del orden **civil**. El equivalente funcional aquí es el **agotamiento de la vía
> administrativa** (art. 25.1 LJCA). Ninguna skill debe pedir MASC ni bloquear un escrito por su
> ausencia.

---

## Identidad del despacho

| Campo | Valor |
|---|---|
| Abogado / Despacho | [NOMBRE DEL LETRADO / DESPACHO] |
| Forma jurídica | [Abogado ejerciente individual / SLP / SCP / multiprofesional] |
| Colegio profesional | [ILUSTRE COLEGIO DE ABOGADOS DE ...] |
| Nº de colegiado | [PENDIENTE] |
| Provincia de actuación | [PROVINCIA] |
| Años ejerciendo | [PENDIENTE] |
| Correo | [PENDIENTE] |
| Teléfono | [PENDIENTE] |

---

## Áreas de práctica contencioso-administrativas

Marcar las que trabaja el despacho (`/customize`):

- [ ] **Sancionador** (tráfico, disciplina, actividad, consumo, extranjería sancionadora)
- [ ] **Urbanismo y ordenación del territorio** (licencias, disciplina, planeamiento, ruina)
- [ ] **Responsabilidad patrimonial** (sanitaria, viaria, funcionamiento de servicios)
- [ ] **Función pública y personal** (oposiciones, provisión, retribuciones, disciplina)
- [ ] **Tributario y recaudación** (local y autonómico, apremio, derivación de responsabilidad)
- [ ] **Extranjería**
- [ ] **Seguridad Social y actas de liquidación** (impugnación en vía contenciosa)
- [ ] **Contratación pública** (recurso especial, adjudicación, modificados)
- [ ] **Subvenciones y ayudas** (reintegro)
- [ ] **Expropiación forzosa y justiprecio**
- [ ] **Autorizaciones judiciales** (entrada en domicilio, art. 8.6 LJCA)
- [ ] **Otros:** [indicar]

### Asuntos más frecuentes
[Listar los tipos de asunto más habituales — p. ej. sanciones de tráfico, licencias de actividad,
responsabilidad patrimonial sanitaria, personal estatutario.]

---

## Clientes

| Campo | Valor |
|---|---|
| Perfil típico | [Particulares / pymes / empresas / entidades locales / asociaciones] |
| ¿Defiende también a la Administración? | [No / Sí — indicar cuáles] |

---

## Rol y posición procesal

| Campo | Valor |
|---|---|
| Posición por defecto | [Recurrente (habitual) / Administración demandada / codemandado-aseguradora / variable] |
| Administraciones habitualmente demandadas | [Estatal / autonómica: indicar CCAA / local: indicar / institucional] |
| Normativa autonómica y local aplicable | [CCAA + ordenanzas relevantes] |

### Órganos judiciales habituales

| Órgano | Detalle | Postulación (art. 23 LJCA) |
|---|---|---|
| Juzgados de lo Contencioso-Administrativo | [nº X de (LUGAR)] | Procurador **potestativo** |
| Juzgados Centrales de lo CA | [si procede] | Procurador **potestativo** |
| Sala de lo CA del TSJ | [de (CCAA), Sección (X)] | Procurador **preceptivo** |
| Audiencia Nacional, Sala de lo CA | [si procede] | Procurador **preceptivo** |
| Tribunal Supremo, Sala Tercera | [casación] | Procurador **preceptivo** |

> **Nota de ámbito territorial.** Buena parte del Derecho administrativo material es **autonómico
> y local** (urbanismo, actividades, tributos locales). El conector `jurisprudenciator` cubre
> **BOE (Derecho estatal)**, jurisprudencia, doctrina de la DGT y del TEAC, Catastro y
> **ordenanzas municipales** de los municipios cubiertos. La normativa **autonómica** (boletines autonómicos) y los **BOP** no
> cubiertos **no** son accesibles: en esos casos, pedir la norma al usuario y **no citarla de
> memoria**.

---

## Herramientas y tecnología

| Herramienta | Uso |
|---|---|
| Gestor documental | [Carpeta local / OneDrive / Google Drive / Dropbox, si el abogado lo tiene conectado] |
| [Correo] | Correo |
| LexNET | Notificaciones / presentación |
| Word | Redacción / entregables `.docx` |
| [Base de datos jurídica] | Doctrina y legislación |
| CRM / gestor de expedientes | [No tiene / indicar] |

### Organización documental
[Describir el patrón: carpetas por cliente, expediente, etc.] Patrón de slug de expediente:
`descriptor-materia-año` (DEFAULT — ajustar con `/customize`).

> **Recordatorio:** el slug y el nombre del asunto **no deben contener el nombre del cliente**
> si el repositorio se comparte o sincroniza. Ver `PROTECCION-DATOS.md`.

---

## Jurisprudencia y legislación — conector Jurisprudenciator (ÚNICA vía)

El plugin trae configurado un único conector, **Jurisprudenciator**
(`https://mcp.jurisprudenciator.lexiaipro.org/mcp`, en `.mcp.json`). La primera vez pide iniciar sesión
con la cuenta de Jurisprudenciator. Si sus herramientas no aparecen o fallan, llamar a `estado` y
decírselo al abogado: nunca sustituir la consulta por memoria. Cada skill tiene una sección
«Jurisprudenciator en esta skill» con las herramientas que usa.

**Qué ofrece:**

- **Jurisprudencia oficial** del TS (Sala Tercera y demás salas), la AN, los TSJ, las AP y los
  juzgados, además del **TC** y del **TJUE**: búsqueda con ROJ, ECLI, fecha, ponente y resumen, y lectura
  del **párrafo literal** que se va a citar.
- **Legislación vigente**: texto consolidado de un artículo (LJCA, LPAC, LRJSP, LGT, LEC, CE...) y de
  normas de la UE, con la norma que le dio su redacción.
- **Verificación de citas** de un borrador: artículos inexistentes o derogados, reformas mal atribuidas
  y contenidos que no casan.
- **BOE y BORME**: búsqueda y lectura de disposiciones, sumario de un día y seguimiento de
  publicaciones (edictos, notificaciones, anuncios) por texto o NIF en periodos de hasta 31 días.
- **Registro Mercantil**: estado, domicilio, administradores, apoderados y últimos actos inscritos de
  una sociedad.
- **Hacienda y tribunales económico-administrativos**: consultas de la DGT y doctrina del TEAC y los
  TEAR.
- **Ordenanzas y reglamentos municipales** de los municipios cubiertos (terrazas, ruido, ZBE,
  residuos, viviendas turísticas, IBI, ICIO, plusvalía...).
- **Catastro**: datos de un inmueble o finca por referencia catastral, dirección, polígono y parcela
  o coordenadas. No da titular ni valor catastral y no cubre País Vasco ni Navarra.
- **Convenios colectivos**: identificación, texto, artículo concreto y vigencia.

**Necesidad → herramienta en el orden contencioso:**

| Necesidad | Herramienta |
|---|---|
| Doctrina de la Sala Tercera | `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) → `leer_sentencias` (`parrafos=3`) |
| Criterio de un TSJ, de la AN o de los juzgados | `buscar_sentencias` (`base="AN"`, `tipo_organo="TSJ"`, `provincia`) |
| Derechos fundamentales / Derecho de la UE | `buscar_sentencias` con `base="TC"` / `base="TJUE"` |
| Autos de admisión de casación | `buscar_sentencias` (`base="TS"`, `tipo_resolucion="AUTO"`) + `opciones_busqueda` |
| ECLI o ROJ citado por la Administración o por el contrario | `buscar_por_cita` |
| Texto vigente de un precepto | `buscar_articulo` |
| Revisar las citas del borrador antes de presentar | `verificar_escrito` |
| Disposición general impugnada, fecha de publicación y cómputo | `buscar_boe` → `leer_boe`, `sumario_boe` |
| Notificación edictal en el BOE, anuncios de licitación | `novedades_boe` → `leer_boe` |
| Ordenanza aplicada (sanción municipal, licencia, tributo local) | `buscar_ordenanzas` → `leer_ordenanza` |
| Inmueble (expropiación, IBI, plusvalía, urbanismo, ruina, responsabilidad viaria) | `consultar_catastro` (+ `callejero_catastro`) |
| Vía económico-administrativa y criterio de Hacienda | `buscar_doctrina_teac` → `leer_resolucion_teac`; `buscar_consultas_hacienda` → `leer_consulta_hacienda` |
| Sociedad recurrente, adjudicataria o codemandada | `buscar_empresa_mercantil`, `sumario_borme` |
| Diagnóstico del conector | `estado` |

**Reglas:**

- El texto vigente de cualquier artículo se comprueba con `buscar_articulo` **antes** de citarlo.
- **Prohibido inventar** ECLI, ROJ, fechas, ponentes o fundamentos. Si no se puede verificar, se
  marca `[verificar]` y se dice.
- En las consultas se describe el problema jurídico, nunca los datos del cliente (ver
  `PROTECCION-DATOS.md`).
- Anclas de plazos y umbrales ya verificadas: `references/anclas-normativas-ca.md`.

---

## Estilo de la casa

| Campo | Valor |
|---|---|
| Voz redaccional | Estilo de la casa (`estilo-escritos-judiciales`) — calibrar con escritos reales del despacho cuando se aporten muestras |
| Entregable | Word `.docx` maquetado para LexNET |
| Tratamiento del expediente | Toda afirmación de hecho se ancla al **expediente administrativo** con folio |

---

## Calendario y plazos — reglas de la casa

| Campo | Valor |
|---|---|
| Naturaleza de los plazos de interposición | **Caducidad** — no se interrumpen por reclamación extrajudicial |
| Agosto | **No corre** ningún plazo de la LJCA, **salvo derechos fundamentales** (agosto hábil) — art. 128.2 LJCA |
| Margen de seguridad interno | [DEFAULT: presentar con **7 días naturales** de antelación al vencimiento] |
| Doble control de plazo | [DEFAULT: sí — el plazo lo confirma una segunda lectura antes de cerrar el asunto de agenda] |

---

## Honorarios / encargo

| Campo | Valor |
|---|---|
| IBAN del despacho | [PENDIENTE] |
| Hoja de encargo | `/hoja-encargo` |
| Advertencia de costas al cliente | Tope del **tercio de la cuantía** por cada favorecido (art. 139.4 LJCA) |

---

## Qué quiere implementar con Claude (prioridades)

1. Redactar recursos administrativos, interposiciones, demandas y recursos contenciosos.
2. Búsqueda de jurisprudencia (vía conector Jurisprudenciator).
3. Control de plazos de caducidad y de causas de inadmisibilidad.
4. Análisis de estrategia procesal de cada asunto, con visión crítica y opiniones fundamentadas
   en Derecho.
5. Informes jurídicos de los asuntos.

---

## Apetito al riesgo y RC profesional

> Todo PENDIENTE — definir con `/customize` (cobertura RC, franquicia, bandas de severidad,
> escalera de autoridad para desistir o allanarse).

---

## Colaboradores clave

> PENDIENTE — procurador de cabecera (preceptivo solo ante órganos colegiados, art. 23.2 LJCA),
> peritos (médico, arquitecto/urbanista, económico), colaboradores. Completar con `/customize`.

---

## Integraciones disponibles

| Integración | Estado |
|---|---|
| `jurisprudenciator` (MCP, incluido en el plugin) | [PENDIENTE — comprobar con `estado` (`/cold-start-interview --check-integrations`)] |
| Gestor documental (opcional: OneDrive, Google Drive o Dropbox, si el abogado lo tiene conectado; si no, carpeta local) | [PENDIENTE] |

---

## Historial de cambios

| Fecha | Acción |
|---|---|
| — | Plantilla genérica inicial |
