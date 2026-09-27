# Perfil de despacho — [NOMBRE DEL DESPACHO]
# Plugin: litigacion-laboral-espana
# Origen: plantilla genérica (completar con `/cold-start-interview`)

> Plantilla viva del despacho. Ajustar cualquier campo con `/customize` o rehacer con `/cold-start-interview`. Mientras tenga `[PLACEHOLDER]`/`[PENDIENTE]`, las skills que dependen del perfil pedirán configurarlo primero.

---

## Identidad del despacho

| Campo | Valor |
|---|---|
| Abogado / Despacho | [NOMBRE DEL LETRADO / DESPACHO] |
| Forma jurídica | [Abogado ejerciente individual / SLP / SCP / multiprofesional] |
| Colegio profesional | [ILUSTRE COLEGIO DE ABOGADOS DE ...] |
| Nº de colegiado | [PENDIENTE] |
| Provincia de actuación | [PARTIDO JUDICIAL] |
| Años ejerciendo | [PENDIENTE] |
| Correo | [PENDIENTE] |
| Teléfono | [PENDIENTE] |

---

## Áreas de práctica

- **Laboral** (despidos, reclamaciones de cantidad, extinciones art. 50 ET, TRADE, modificaciones sustanciales)
- **Seguridad Social** (incapacidad permanente, determinación de contingencia, prestaciones)
- **[otras áreas del despacho]**

> El plugin está orientado a **litigación laboral y de Seguridad Social** conforme a la LRJS (Ley 36/2011). Ajustar el listado de áreas con `/customize`.

### Asuntos más frecuentes
[Listar los tipos de asunto más habituales del despacho — p. ej. despidos disciplinarios y objetivos, reclamaciones de cantidad, incapacidades permanentes, determinación de contingencia, extinción art. 50 ET, acoso laboral, TRADE.]

---

## Clientes

| Campo | Valor |
|---|---|
| Perfil típico | [Trabajadores / empresas / mixto — indicar proporción] |

---

## Rol y posición procesal

| Campo | Valor |
|---|---|
| Posición por defecto | [Variable — preguntar por asunto / lado trabajador (demandante habitual) / lado empresa (demandada habitual)] |
| Actuación ante | [Sección de lo Social del Tribunal de Instancia de .. / Sala de lo Social del TSJ de ...] |

---

## Herramientas y tecnología

| Herramienta | Uso |
|---|---|
| Gestor documental | [Carpeta local / OneDrive / Google Drive / Dropbox, si el abogado lo tiene conectado] |
| [Correo] | Correo |
| LexNET | Notificaciones / presentación |
| Word | Redacción / entregables `.docx` |
| Jurisprudenciator | Jurisprudencia, legislación vigente, convenios colectivos y Registro Mercantil — conector incluido en el plugin (ver `## Integraciones disponibles`) |
| CRM / gestor de expedientes | [No tiene / indicar] |

### Organización documental
[Describir dónde se guardan los documentos (carpeta local, OneDrive, Google Drive o Dropbox si está conectado) y el patrón: carpetas por cliente, expediente, etc.] Patrón de slug de expediente: `apellidos-tipo-año` (DEFAULT — ajustar con `/customize`).

---

## Integraciones disponibles

| Integración | Qué aporta | Estado |
|---|---|---|
| **Jurisprudenciator** (conector incluido en el plugin; la primera vez pide iniciar sesión con la cuenta de Jurisprudenciator) | Fuentes oficiales: jurisprudencia, legislación vigente, convenios, Registro Mercantil, BOE y BORME (detalle abajo) | [PENDIENTE — comprobar con `estado`] |
| Gestor documental (opcional) | Carpeta local, OneDrive, Google Drive o Dropbox, si el abogado lo tiene conectado | [PENDIENTE] |
| Tareas programadas (opcional) | Recordatorios de plazos y rutinas semanales | [PENDIENTE] |

### Qué ofrece Jurisprudenciator

- **Jurisprudencia oficial**: Tribunal Supremo, Audiencia Nacional, Tribunales Superiores de Justicia, Audiencias Provinciales y juzgados, Tribunal Constitucional y TJUE, con el párrafo literal y el ECLI o ROJ de cada resolución (`buscar_sentencias`, `opciones_busqueda`, `buscar_por_cita`, `leer_sentencias`, `continuar_lectura`).
- **Legislación vigente**: texto consolidado de cualquier artículo de leyes españolas y normas de la UE, con la norma que le dio la redacción actual (`buscar_articulo`).
- **Verificación de citas** de un borrador: artículos inexistentes o derogados, reformas mal atribuidas y contenidos que no casan (`verificar_escrito`).
- **BOE y BORME**: normas por materia o fecha, sumarios diarios, edictos, notificaciones y subastas por texto o NIF (`buscar_boe`, `leer_boe`, `sumario_boe`, `novedades_boe`, `sumario_borme`).
- **Registro Mercantil**: estado, domicilio, administradores, apoderados y últimos actos inscritos de una sociedad (`buscar_empresa_mercantil`).
- **Hacienda y TEAC**: consultas de la DGT y doctrina de los tribunales económico-administrativos (`buscar_consultas_hacienda`, `leer_consulta_hacienda`, `buscar_doctrina_teac`, `leer_resolucion_teac`).
- **Ordenanzas municipales** (`buscar_ordenanzas`, `leer_ordenanza`) y **Catastro** (`consultar_catastro`, `callejero_catastro`; no da titular ni valor catastral).
- **Convenios colectivos**: el convenio aplicable por sector y territorio, su texto por artículo o materia y su vigencia (`buscar_convenio`, `leer_convenio`, `vigencia_convenio`).
- **Guías de redacción** para escritos que no cubre ninguna skill del plugin (`escritos_disponibles`, `guia_escrito`) y **diagnóstico** del conector (`estado`).

### Orden social: necesidad → herramienta

| Necesidad | Herramienta |
|---|---|
| Doctrina de la Sala Cuarta del Tribunal Supremo | `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`) → `leer_sentencias` (`parrafos=3`) |
| Salas de lo Social de la AN y de los TSJ, juzgados de lo social | `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="AN"`, `tipo_organo`, `provincia`) |
| Tutela de derechos fundamentales, garantía de indemnidad, discriminación | `buscar_sentencias` (`base="TC"`) |
| Directivas de tiempo de trabajo, despidos colectivos, igualdad, temporalidad | `buscar_sentencias` (`base="TJUE"`) y `buscar_articulo` (p. ej. `ley="Directiva 1999/70/CE"`) |
| Verificar un ECLI o ROJ, o una sentencia de contraste | `buscar_por_cita` |
| Artículo vigente del ET, LRJS, LGSS, LISOS, LPRL, LOLS, Ley 15/2022 | `buscar_articulo` |
| Salario, categoría, jornada, pluses, antigüedad, vacaciones, mejoras de IT, ultraactividad | `buscar_convenio` → `leer_convenio` (`articulo` o `buscar_en`) + `vigencia_convenio` |
| Empresa demandada: denominación, CIF, domicilio social, administradores, grupo, sucesión, concurso | `buscar_empresa_mercantil` |
| Concurso o disolución de la empresa (FOGASA), edictos del juzgado de lo social | `sumario_borme`, `novedades_boe` → `leer_boe` |
| Normativa de Seguridad Social, bases y topes publicados | `buscar_boe` → `leer_boe` |
| Revisar las citas de un borrador antes de presentarlo | `verificar_escrito` |

---

## Estilo de la casa

| Campo | Valor |
|---|---|
| Voz redaccional | Estilo de la casa (`estilo-escritos-judiciales`) — calibrar con escritos reales del despacho cuando se aporten muestras |
| Entregable | Word `.docx` maquetado para LexNET |
| Vía de procedibilidad por defecto | Papeleta de conciliación ante el SMAC (arts. 63-68 LRJS); reclamación previa solo en prestaciones de Seguridad Social (art. 71 LRJS) — DEFAULT, ajustar |

> Nota: el requisito MASC de la LO 1/2025 (art. 5) rige en el orden **civil**, no en el social. En lo social la evitación del proceso se canaliza por conciliación/mediación previa (SMAC) o reclamación previa/vía administrativa, según el demandado.

---

## Honorarios / encargo

| Campo | Valor |
|---|---|
| IBAN del despacho | [PENDIENTE] |
| Hoja de encargo | `/hoja-encargo` |

---

## Qué quiere implementar con Claude (prioridades)

1. Redactar demandas laborales, papeletas de conciliación y recursos (suplicación, RCUD).
2. Búsqueda de jurisprudencia social (vía conector Jurisprudenciator).
3. Redacción de escritos jurídicos fundamentados.
4. Análisis de estrategia procesal de cada asunto, con visión crítica y opiniones fundamentadas en Derecho.
5. Informes jurídicos de los asuntos.

---

## Apetito al riesgo y RC profesional

> Todo PENDIENTE — definir con `/customize` (cobertura RC, franquicia, bandas de severidad, escalera de autoridad para transigir).

---

## Colaboradores clave

> PENDIENTE — graduado social colaborador, procurador (opcional en lo social), peritos médicos (incapacidades) y económicos, colaboradores. Completar con `/customize`.

---

## Historial de cambios

| Fecha | Acción |
|---|---|
| — | Plantilla genérica inicial |
