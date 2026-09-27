# Perfil de despacho — [NOMBRE DEL DESPACHO]
# Plugin: litigacion-penal-espana
# Origen: plantilla genérica (completar con `/cold-start-interview`)

> Plantilla viva del despacho. Ajustar cualquier campo con `/customize` o rehacer con
> `/cold-start-interview`. Mientras tenga `[PLACEHOLDER]`/`[PENDIENTE]`, las skills que dependen del
> perfil pedirán configurarlo primero.
>
> ⚠️ **Este archivo viaja con el plugin y es una PLANTILLA VACÍA. Nunca escribir aquí datos reales.**
> El perfil cumplimentado se escribe en
> `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md`.
> Ver `PROTECCION-DATOS.md`.

---

## Ámbito del plugin

**Exclusivamente jurisdicción penal.** Marco normativo:

- **LECrim** — Real Decreto de 14 de septiembre de 1882.
- **CP** — LO 10/1995, de 23 de noviembre, del Código Penal.
- **LOPJ** — LO 6/1985 (art. 11.1: prueba ilícita; art. 238: nulidad).
- **CE** — arts. 17 (libertad), 18 (intimidad, domicilio, comunicaciones), 24 (tutela judicial,
  presunción de inocencia, defensa).
- Leyes especiales: **LO 5/1995** (Tribunal del Jurado), **LO 5/2000** (responsabilidad penal del
  menor), **Ley 4/2015, de 27 de abril** (Estatuto de la víctima del delito), **LO 6/1984** (habeas
  corpus), **LO 10/2022** (garantía integral de la libertad sexual), **LO 1/2004** (violencia de
  género).

> ⚠️ **Trampa verificada:** al consultar el **Estatuto de la víctima** con el conector, usar el ID
> **`BOE-A-2015-4606`**. Buscar «Ley 4/2015» a secas devuelve la **ley agraria de Galicia** (Ley
> 4/2015, **de 17 de junio**) — un texto plausible de una ley equivocada, sin dar error. Regla
> general: fuera de las grandes siglas (LECrim, CP, LOPJ, CE, LEC), localizar la norma con
> `buscar_boe` y usar su **ID BOE**. Ver `references/anclas-normativas-penal.md` § 12.1.

> ⛔ **Fuera de ámbito:** civil, mercantil, familia, laboral y contencioso-administrativo. La acción
> civil derivada del delito (arts. 100, 108-117 LECrim y 109-126 CP) **sí** entra: se ejercita en el
> proceso penal.
>
> ⛔ **El MASC de la LO 1/2025 NO se aplica en el orden penal.** Es requisito de procedibilidad del
> orden **civil**. Aquí no hay intento previo de MASC ni burofax como requisito. Lo más próximo, y
> solo en supuestos tasados, son la **querella** o **denuncia del ofendido** en delitos privados y
> semipúblicos, y el **acto de conciliación** del art. 804 LECrim en injurias y calumnias.
>
> ⛔ **NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. La reforma que
> atribuiría la instrucción al Ministerio Fiscal está **en tramitación**, con entrada en vigor
> prevista para **1-1-2028**. No describirla nunca como Derecho vigente.

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
| **Turno de oficio / guardia** | [No / Sí — indicar turno: penal, violencia de género, menores] |

---

## Áreas de práctica penal

Marcar las que trabaja el despacho (`/customize`):

- [ ] **Patrimoniales y socioeconómicos** (hurto, robo, estafa, apropiación indebida, daños)
- [ ] **Económico y societario** (administración desleal, insolvencias punibles, blanqueo)
- [ ] **Seguridad vial** (arts. 379-385 CP)
- [ ] **Lesiones y contra la vida**
- [ ] **Violencia de género y doméstica** (LO 1/2004 — competencia de las **Secciones de Violencia
      sobre la Mujer**, art. 89 LOPJ y art. 14.5 LECrim)
- [ ] **Libertad sexual** (LO 10/2022)
- [ ] **Salud pública / drogas** (arts. 368 y ss.)
- [ ] **Siniestralidad laboral** (arts. 316-318 CP)
- [ ] **Delitos contra la Administración pública**
- [ ] **Responsabilidad penal de personas jurídicas** (art. 31 bis CP) y compliance
- [ ] **Menores** (LO 5/2000)
- [ ] **Extranjería penal** (art. 89 CP)
- [ ] **Otros:** [indicar]

### Asuntos más frecuentes
[Listar los tipos de asunto más habituales — p. ej. juicios rápidos de seguridad vial, estafas,
lesiones, violencia de género.]

---

## Clientes

| Campo | Valor |
|---|---|
| Perfil típico | [Particulares / pymes / empresas / aseguradoras] |

---

## Rol y posición procesal

| Campo | Valor |
|---|---|
| Posición por defecto | [Defensa (habitual) / acusación particular / acusación popular / actor civil / responsable civil] |
| ¿Ejerce acusación popular? | [No / Sí — ojo a la fianza del art. 280 LECrim] |
| ¿Defiende a personas jurídicas? | [No / Sí — art. 31 bis CP; representante con poder especial] |

> ⚠️ **Conflicto estructural.** Defender a la persona jurídica y a la persona física investigada por
> los mismos hechos genera **conflicto de interés**. Comprobarlo siempre antes de aceptar.

### Órganos judiciales habituales

> ⚠️ **Nomenclatura vigente desde el 3-10-2025 (LO 1/2025, DF 38.3).** Ya **no** son «Juzgados de
> Instrucción», «de lo Penal» ni «de Violencia sobre la Mujer»: son **Secciones de los Tribunales de
> Instancia** (art. 14 LECrim). Usar la denominación correcta en todos los encabezamientos.

| Órgano | Detalle | Competencia |
|---|---|---|
| **Sección de Instrucción** del Tribunal de Instancia | [de (PARTIDO)] | Instrucción; juicios rápidos; **delitos leves** (art. 14.1 y 14.2) |
| **Sección de lo Penal** del Tribunal de Instancia | [de (CIRCUNSCRIPCIÓN)] | Enjuiciamiento: pena privativa ≤ 5 años, multa cualquiera, u otras ≤ 10 años (art. 14.3) |
| **Sección con competencia en Violencia sobre la Mujer** | [de (LUGAR)] | Art. 14.5 — instrucción, órdenes de protección y ⭐ **delitos contra la libertad sexual cuando la víctima sea mujer** (14.5.h) |
| ⭐ **Sección de Violencia contra la Infancia y la Adolescencia** | [de (LUGAR)] | **Órgano NUEVO** (art. 14.6) — víctimas niños, niñas y adolescentes |
| **Sección de Menores** del Tribunal de Instancia | [de (LUGAR)] | LO 5/2000 (art. 84.2.f LOPJ) |
| **Sección de Vigilancia Penitenciaria** del Tribunal de Instancia | [de (LUGAR)] | Ejecución penitenciaria (art. 84.2.g LOPJ) |
| Tribunal Central de Instancia | [si procede] | Antes «Juzgados Centrales» — art. 65 LOPJ. **[verificar la fórmula de encabezamiento]** |
| Audiencia Provincial | [de (PROVINCIA), Sección (X)] | Enjuiciamiento en los demás casos; apelación; jurado (art. 14.4) |
| Tribunal Superior de Justicia | [de (CCAA)] | Apelación del jurado y del art. 846 ter; aforados |
| Audiencia Nacional, Sala de lo Penal | [si procede] | Art. 65 LOPJ |
| Tribunal Supremo, Sala Segunda | [casación] | Casación |

> **Art. 84.2 LOPJ** (vigente 23-1-2025) — el Tribunal de Instancia se integra por una **Sección
> Única de Civil y de Instrucción** (o Sección Civil + Sección de Instrucción separadas) y, además,
> por alguna o varias de: **Familia, Infancia y Capacidad · Mercantil · Violencia sobre la Mujer ·
> Violencia contra la Infancia y la Adolescencia · Penal · Menores · Vigilancia Penitenciaria ·
> Contencioso-Administrativo · Social**. **También el JVP y el de Menores son hoy Secciones.**
>
> **Se mantienen con su nombre:** Audiencia Provincial, TSJ, Audiencia Nacional y Tribunal Supremo.

> ⚠️ **Regla práctica que nunca falla:** **copiar la denominación exacta que figure en la resolución
> que se contesta o en la carátula del procedimiento.** El régimen transitorio de implantación
> (DT 1.ª LO 1/2025) venció el **31-12-2025**, así que «Juzgado de Instrucción» ya no es la
> denominación correcta; pero la **DA 1.ª** ordena entender las referencias legales a los Juzgados
> **hechas a las Secciones**, de modo que un error de denominación **no invalida** el escrito.

> **Art. 14.7:** si los hechos pudieran ser conocidos por la Sección de Violencia contra la Infancia
> y la Adolescencia **y** por la de Violencia sobre la Mujer, la competencia es **en todo caso** de
> esta última.

---

## Herramientas y tecnología

| Herramienta | Uso |
|---|---|
| Gestor documental | [Carpeta local / OneDrive / Google Drive / Dropbox, si el abogado lo tiene conectado] |
| [Correo] | Correo |
| LexNET | Notificaciones / presentación |
| Word | Redacción / entregables `.docx` |
| Jurisprudenciator (conector incluido en el plugin) | Jurisprudencia, legislación vigente y verificación de citas |
| [Otras bases jurídicas] | [Opcional] |
| CRM / gestor de expedientes | [No tiene / indicar] |

### Organización documental
[Describir el patrón.] Patrón de slug de expediente: `descriptor-delito-año` (DEFAULT — ajustar con
`/customize`).

> ⚠️ **Nunca** construir el slug con el nombre del cliente. En penal, un listado de carpetas que
> revele quién está investigado es un riesgo reputacional grave para el cliente y una brecha de
> datos de **categoría especial** (art. 10 RGPD: infracciones y condenas). Ver `PROTECCION-DATOS.md`.

---

## Jurisprudencia y legislación — conector Jurisprudenciator (ÚNICA vía)

El plugin trae un único conector: **Jurisprudenciator** (`https://mcp.jurisprudenciator.lexiaipro.org/mcp`).
La primera vez que se usa pide iniciar sesión con la cuenta de Jurisprudenciator. Qué ofrece:

- **Jurisprudencia oficial** del Tribunal Supremo (**Sala Segunda**), la Audiencia Nacional, los TSJ,
  las Audiencias Provinciales y los juzgados, además del **Tribunal Constitucional** y del **TJUE**,
  con el **párrafo literal** y el **ECLI o ROJ** de cada resolución.
- **Artículos vigentes** de las leyes españolas y de las normas de la UE, con la norma que dio la
  redacción actual (clave para la ley penal en el tiempo).
- **Verificación de citas** de un borrador: artículos inexistentes o derogados, reformas mal
  atribuidas y contenidos que no casan.
- **BOE y BORME**: normas por materia, sumarios diarios y vigilancia de edictos, requisitorias,
  notificaciones e indultos.
- **Registro Mercantil**: estado, domicilio, administradores, apoderados y últimos actos inscritos de
  una sociedad.
- **Hacienda y TEAC**: consultas de la Dirección General de Tributos y doctrina
  económico-administrativa (útil en los delitos contra la Hacienda Pública).
- **Ordenanzas municipales**, **Catastro** (datos físicos de inmuebles; no da titular ni valor) y
  **convenios colectivos**.
- **Método de redacción** para los escritos que ninguna skill del plugin cubre.

Reglas:

- El texto vigente de cualquier artículo se comprueba con `buscar_articulo` **antes** de citarlo.
- **Prohibido inventar** ECLI, ROJ, fechas, ponentes o fundamentos. Si no se puede verificar, se
  marca `[verificar]` y se dice.
- Las consultas describen el **problema jurídico**, nunca los datos del cliente (`PROTECCION-DATOS.md`).
- Anclas de penas, plazos y requisitos ya verificadas: `references/anclas-normativas-penal.md`.

### Necesidad → herramienta en el orden penal

| Necesidad | Herramienta |
|---|---|
| Doctrina de la Sala Segunda | `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) → `leer_sentencias` (`parrafos=3`) |
| Criterio de la Audiencia Provincial, el TSJ o los juzgados | `buscar_sentencias` (`base="AN"`, `tipo_organo`, `provincia`) |
| Presunción de inocencia, prueba ilícita, tutela judicial, habeas corpus, amparo | `buscar_sentencias` (`base="TC"`) |
| Orden europea de detención, directivas de derechos procesales y de víctimas | `buscar_sentencias` (`base="TJUE"`); texto de la directiva con `buscar_articulo` |
| Verificar un ECLI o ROJ que aporta la otra parte | `buscar_por_cita` |
| Tipo, pena y redacción aplicable (ley penal en el tiempo) | `buscar_articulo` (`ley="CP"`, `"LECrim"`, `"LOPJ"`...) |
| Norma fuera de las grandes siglas (Estatuto de la víctima, LO 1/2004, LORPM) | `buscar_boe` → ID BOE → `buscar_articulo` |
| Revisar un escrito antes de presentarlo | `verificar_escrito` |
| Persona jurídica (art. 31 bis CP), administradores de hecho y de derecho, delitos societarios | `buscar_empresa_mercantil`; actos en fechas clave con `sumario_borme` → `leer_boe` |
| Inmuebles: usurpación, alzamiento, frustración de la ejecución, delitos urbanísticos | `consultar_catastro` (+ `callejero_catastro`) |
| Delitos urbanísticos y contra la ordenación del territorio | `buscar_ordenanzas` → `leer_ordenanza` (si el municipio está cubierto) |
| Delitos contra los derechos de los trabajadores | `buscar_convenio` → `leer_convenio`, `vigencia_convenio` |
| Delito fiscal: criterio administrativo | `buscar_consultas_hacienda` → `leer_consulta_hacienda`; `buscar_doctrina_teac` → `leer_resolucion_teac` |
| Requisitorias, edictos e indultos | `novedades_boe` → `leer_boe` |
| El conector no responde | `estado` |

---

## Estilo de la casa

| Campo | Valor |
|---|---|
| Voz redaccional | Estilo de la casa (`estilo-escritos-judiciales`) — calibrar con escritos reales del despacho cuando se aporten muestras |
| Entregable | Word `.docx` maquetado para LexNET |
| Anclaje probatorio | Toda afirmación de hecho se ancla al **folio de las actuaciones** |

---

## Reglas de la casa — plazos y ley aplicable

| Campo | Valor |
|---|---|
| **Ley penal en el tiempo** | Identificar **siempre** la redacción del CP vigente **a la fecha de los hechos** (art. 2 CP) y comprobar si la posterior es **más favorable** (art. 2.2 CP) |
| **Plazo de instrucción** | 12 meses desde la incoación, prorrogables (art. 324 LECrim). **Vigilar cada prórroga**: sin auto previo al vencimiento, las diligencias posteriores son inválidas (art. 324.3) |
| **Días inhábiles** | **Agosto** y **del 24 de diciembre al 6 de enero** (art. 183 LOPJ, redacción LO 14/2022), salvo actuaciones **declaradas urgentes** por las leyes procesales. **Pero la instrucción tiene régimen propio** (art. 201 LECrim): no se paraliza |
| **Prescripción** | La denuncia o querella **NO interrumpe** por sí sola: solo **suspende 6 meses** (art. 132.2.2.ª CP). Interrumpe la **resolución judicial motivada**. Si en 6 meses no la hay, el reloj sigue corriendo |
| Margen de seguridad interno | [DEFAULT: presentar con **2 días hábiles** de antelación al vencimiento] |
| Guardia | [Disponibilidad y protocolo de asistencia al detenido — plazo de **3 horas** del art. 520.5 LECrim] |

---

## Honorarios / encargo

| Campo | Valor |
|---|---|
| IBAN del despacho | [PENDIENTE] |
| Hoja de encargo | `/hoja-encargo` |

---

## Qué quiere implementar con Claude (prioridades)

1. Redactar denuncias, querellas, escritos de defensa y de acusación, y recursos.
2. Búsqueda de jurisprudencia (vía conector Jurisprudenciator).
3. Control de plazos de instrucción, prescripción y recursos.
4. Análisis de estrategia procesal de cada asunto, con visión crítica y opiniones fundamentadas en
   Derecho.
5. Informes jurídicos de los asuntos.

---

## Apetito al riesgo y RC profesional

> Todo PENDIENTE — definir con `/customize` (cobertura RC, franquicia, bandas de severidad, criterio
> de la casa sobre conformidades).

---

## Colaboradores clave

> PENDIENTE — procurador de cabecera, peritos (médico forense de parte, calígrafo, informático
> forense, tasador), criminólogo, detective. Completar con `/customize`.

---

## Integraciones disponibles

| Integración | Estado |
|---|---|
| Jurisprudenciator (conector incluido: jurisprudencia, legislación, BOE/BORME, Registro Mercantil, Hacienda/TEAC, ordenanzas, Catastro, convenios) | [PENDIENTE — comprobar con `estado` vía `/cold-start-interview --check-integrations`] |
| Gestor documental (carpeta local, OneDrive, Google Drive o Dropbox) | [PENDIENTE — opcional; solo si el abogado lo tiene conectado] |

---

## Historial de cambios

| Fecha | Acción |
|---|---|
| — | Plantilla genérica inicial |
