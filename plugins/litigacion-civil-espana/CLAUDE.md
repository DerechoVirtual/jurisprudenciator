# Perfil de despacho — [NOMBRE DEL DESPACHO]
# Plugin: litigacion-civil-espana
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

- **Civil** (incl. reclamaciones económicas, responsabilidad civil)
- **Mercantil**
- **Familia**
- **[otras áreas del despacho]**

> El plugin está orientado a **litigación civil, mercantil y de familia** conforme a la LEC. Ajustar el listado de áreas con `/customize`.

### Asuntos más frecuentes
[Listar los tipos de asunto más habituales del despacho — p. ej. reclamaciones de cantidad, responsabilidad civil, nulidad de cláusulas abusivas, desahucios, familia.]

---

## Clientes

| Campo | Valor |
|---|---|
| Perfil típico | [Particulares / pymes / empresas] |

---

## Rol y posición procesal

| Campo | Valor |
|---|---|
| Posición por defecto | [Variable — preguntar por asunto / demandante / demandado] |
| Derecho civil foral | [N/A / indicar territorio] |

---

## Herramientas y tecnología

| Herramienta | Uso |
|---|---|
| Jurisprudenciator | Jurisprudencia, legislación vigente, verificación de citas y registros oficiales — conector incluido en el plugin (ver `## Integraciones disponibles`) |
| Gestor documental | [Carpeta local / OneDrive / Google Drive / Dropbox si el abogado lo tiene conectado] |
| [Correo] | Correo |
| LexNET | Notificaciones / presentación |
| Word | Redacción / entregables `.docx` |
| CRM / gestor de expedientes | [No tiene / indicar] |

### Organización documental
Ubicación: [carpeta local / OneDrive / Google Drive / Dropbox si está conectado]. [Describir el patrón: carpetas por cliente, expediente, etc.] Patrón de slug de expediente: `apellidos-tipo-año` (DEFAULT — ajustar con `/customize`).

---

## Integraciones disponibles

| Integración | Estado | Uso |
|---|---|---|
| Jurisprudenciator (conector incluido en el plugin) | [PENDIENTE — comprobar con `estado`] | Fuentes jurídicas oficiales: jurisprudencia, legislación y registros |
| Gestor documental (opcional) | [No conectado / OneDrive / Google Drive / Dropbox] | Documentación del despacho |

> Se actualiza con `/cold-start-interview --check-integrations` o con `/customize`.

### Jurisprudenciator — qué ofrece

Conector remoto (`https://mcp.jurisprudenciator.lexiaipro.org/mcp`) que viene con el plugin; la primera vez pide iniciar sesión con la cuenta de Jurisprudenciator. Todo dato jurídico que vaya a un escrito o a un consejo sale de sus herramientas:

- **Jurisprudencia oficial** del Tribunal Supremo, la Audiencia Nacional, los TSJ, las Audiencias Provinciales y los juzgados (civil, penal, contencioso, social y militar), además del Tribunal Constitucional y del TJUE, con el párrafo literal para citar y su ECLI o ROJ.
- **Artículos vigentes** de leyes españolas y normas de la UE (LEC, CC, LAU, LPH, LSC, TRLGDCU, LH, LO 1/2025, Directiva 93/13/CEE...), con la norma que dio la redacción vigente.
- **Verificación de citas** de un borrador: artículos inexistentes o derogados, reformas mal atribuidas y contenidos que no casan.
- **BOE y BORME**: normas por materia, sumarios diarios y vigilancia de edictos, notificaciones y subastas por texto o NIF.
- **Registro Mercantil**: estado, domicilio, administradores y apoderados, y últimos actos inscritos de una sociedad.
- **Hacienda y TEAC**: consultas de la Dirección General de Tributos y doctrina de los tribunales económico-administrativos.
- **Ordenanzas municipales**, **Catastro** (referencia catastral, superficie, uso y año de construcción; no da titular ni valor catastral y no cubre País Vasco ni Navarra) y **convenios colectivos** con su vigencia.

### Necesidad → herramienta (orden civil)

| Necesidad | Herramienta |
|---|---|
| Jurisprudencia de la Sala Primera del TS | `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`) |
| Audiencias Provinciales y juzgados | `buscar_sentencias` (`base="AN"`, `tipo_organo="AP"`, `provincia`) |
| Consumidores y cláusulas abusivas | `buscar_sentencias` (`base="TJUE"`) |
| Derechos fundamentales y agotamiento previo al amparo | `buscar_sentencias` (`base="TC"`) |
| Acotar una lista demasiado amplia | `opciones_busqueda` |
| Párrafo literal para citar | `leer_sentencias` (`parrafos=3` + `terminos`; `continuar_lectura` si lo pide) |
| Verificar un ECLI o ROJ aportado por el cliente o la contraria | `buscar_por_cita` |
| Artículo vigente (LEC, CC, LAU, LPH, LSC, TRLGDCU, LH, LO 1/2025...) | `buscar_articulo` |
| Revisar las citas de un borrador antes de presentarlo | `verificar_escrito` |
| Inmueble: referencia catastral, superficie y uso | `consultar_catastro` (+ `callejero_catastro` si la dirección no casa) |
| Sociedad: denominación, CIF, domicilio social, administradores, extinción o concurso | `buscar_empresa_mercantil` |
| Concursos, edictos y subastas publicados | `novedades_boe`, `sumario_borme` → `leer_boe` |
| Normas por materia (p. ej. Derecho civil foral) | `buscar_boe` → `leer_boe` |
| Diagnóstico del conector | `estado` |

**Regla:** se cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...). Si una consulta falla, se dice y el dato se marca como `[pendiente de verificar]`; nunca se completa de memoria. La jurisprudencia se atribuye a «Jurisprudenciator» o a «la base oficial de jurisprudencia».

---

## Estilo de la casa

| Campo | Valor |
|---|---|
| Voz redaccional | Estilo de la casa (`estilo-escritos-judiciales`) — calibrar con escritos reales del despacho cuando se aporten muestras |
| Entregable | Word `.docx` maquetado para LexNET |
| Postura MASC por defecto | Burofax = MASC (art. 5 LO 1/2025) — DEFAULT, ajustar |

---

## Honorarios / encargo

| Campo | Valor |
|---|---|
| IBAN del despacho | [PENDIENTE] |
| Hoja de encargo | `/hoja-encargo` |

---

## Qué quiere implementar con Claude (prioridades)

1. Redactar demandas, contestaciones y recursos.
2. Búsqueda de jurisprudencia (vía conector Jurisprudenciator).
3. Redacción de escritos jurídicos fundamentados.
4. Análisis de estrategia procesal de cada asunto, con visión crítica y opiniones fundamentadas en Derecho.
5. Informes jurídicos de los asuntos.

---

## Apetito al riesgo y RC profesional

> Todo PENDIENTE — definir con `/customize` (cobertura RC, franquicia, bandas de severidad, escalera de autoridad para transigir).

---

## Colaboradores clave

> PENDIENTE — procurador de cabecera, peritos, colaboradores, mediador MASC. Completar con `/customize`.

---

## Historial de cambios

| Fecha | Acción |
|---|---|
| — | Plantilla genérica inicial |
