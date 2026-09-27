# Changelog

## 0.3.0 — 2026-09-27

### Jurisprudenciator en todas las skills

- Las **46 skills** incluyen, justo después del título, la sección **«Jurisprudenciator en esta
  skill»**: qué dato de cada tarea sale de qué herramienta del conector (jurisprudencia de la Sala
  Segunda, de las Audiencias, del TC y del TJUE con párrafo literal y ECLI; artículos vigentes;
  verificación de citas; BOE y BORME; Registro Mercantil; Catastro; convenios colectivos).
- Los avisos antiguos sobre jurisprudencia que encabezaban diez skills se han fusionado en esa
  sección, para que no haya dos. Se conservan las anclas de cifras (`references/anclas-normativas-penal.md`).
- Las limitaciones conocidas del conector se trasladan a las skills afectadas: artículos con sufijo
  de letra (arts. 588 bis a – 588 septies c y 846 bis a – f LECrim) y el Estatuto de la víctima por
  su ID BOE.

### Gestión documental

- El plugin **deja de incluir el conector de Dropbox**: `.mcp.json` solo declara Jurisprudenciator.
  El despacho puede guardar sus documentos en una carpeta local, OneDrive, Google Drive o Dropbox si
  lo tiene conectado.
- `cold-start-interview` y `customize` comprueban las integraciones llamando a `estado` de
  Jurisprudenciator y, opcionalmente, al gestor documental que el abogado tenga conectado.

### Documentación

- `CLAUDE.md`: describe todo lo que ofrece Jurisprudenciator y añade una tabla «necesidad →
  herramienta» para el orden penal.
- `README.md`: instalación desde el marketplace de Jurisprudenciator e inicio de sesión en el
  primer uso.
- `PROTECCION-DATOS.md`: el gestor documental que conecte el despacho queda sujeto a su propio
  contrato de encargo de tratamiento; las consultas al Registro Mercantil, al Catastro y al BOE
  tampoco llevan datos de personas físicas.

## 0.2.0 — 2026-07-17

Revisión mayor. El plugin era un fork del plugin de litigación **civil** con dieciséis skills penales
añadidas encima, y **estaba construido sobre ley derogada**. Esta versión lo convierte en un plugin
penal real: descontamina las skills heredadas, robustece el núcleo, incorpora dos reformas que el
plugin desconocía y cubre los huecos. Penas, plazos y competencias verificados artículo por artículo
contra el BOE consolidado.

### ⚠️ Actualización normativa — el plugin ignoraba dos reformas

| Norma | En vigor | Qué cambió |
|---|---|---|
| **LO 1/2025**, de 2 de enero | **03-04-2025** y **03-10-2025** | **Reestructura el juicio oral del abreviado** y **renombra los órganos judiciales** |
| **LO 1/2026**, de 8 de abril, **de multirreincidencia** | **10-04-2026** | Reescribe el **art. 248 CP**, crea el hurto agravado de **teléfonos móviles**, da a las **entidades locales** acción penal por hurto y reforma el **art. 544 bis** y el **art. 80 CP** |

Además se incorporaron: **RD-ley 5/2023** (art. 855: la preparación de la casación ya no es un
formulario), **LO 4/2023** (art. 132 CP: suprimido el plazo de 2 meses), **LO 14/2022** (art. 183
LOPJ: inhábil también del 24-dic al 6-ene; art. 249 CP: estafa informática), **LO 5/2024** (habeas
corpus: el abogado defensor pasa a estar legitimado expresamente) y **LO 9/2021** (catálogo del
Jurado).

### Corregido — errores que podían costar un asunto

- **Colisión del directorio de configuración.** Todas las skills escribían el perfil y los asuntos en
  `.../derecho-virtual/**litigacion-civil-espana-pro**/`, el directorio del plugin civil. Mezclaba
  una cartera penal con una civil en un mismo repositorio — con datos del **art. 10 RGPD** de por
  medio, la peor colisión posible. Ahora: `.../litigacion-penal-espana/`.
- **MASC exigido en una jurisdicción donde no existe.** Eliminado de raíz (9 archivos). Es
  requisito de procedibilidad del orden **civil**.
- **🚨 La conformidad ya no está en el art. 787 LECrim.** La LO 1/2025 reordenó los arts. 785-787: el
  **785** es hoy la **audiencia preliminar** (nueva) y aloja la **conformidad** (785.4-785.11); el
  **786** es el señalamiento; el **787**, la celebración del juicio oral. La skill de conformidad
  citaba el 787. **Y las cuestiones previas ya no se plantean al inicio del juicio**: su sede es la
  audiencia preliminar (art. 787.3).
- **🚨 El art. 249 CP no es la penalidad de la estafa.** Desde la **LO 14/2022** es la **estafa
  informática y con instrumentos de pago**; desde la **LO 1/2026** la pena de la estafa común está en
  el **art. 248 párr. 2**. La skill de estafa —una de las «plantillas reales»— citaba la estructura
  anterior a 2023.
- **🚨 El art. 87 ter LOPJ está suprimido.** La competencia de violencia sobre la mujer está hoy en el
  **art. 89 LOPJ**, y la prohibición de MASC es la del **art. 89.9** — que veda **todos los MASC**, no
  solo la mediación.
- **🚨 Nomenclatura de los órganos.** Desde el **3-10-2025** (art. 14 LECrim) no hay «Juzgados de
  Instrucción», «de lo Penal» ni «de Violencia sobre la Mujer»: son **Secciones de los Tribunales de
  Instancia**. Y existe un órgano **nuevo** que el plugin ignoraba: las **Secciones de Violencia
  contra la Infancia y la Adolescencia** (art. 14.6), con la regla de conflicto del 14.7.
- **Los motivos de casación dependen de la resolución recurrida** (art. 847). Contra una sentencia de
  apelación de una **Audiencia Provincial** —el caso más frecuente— **solo cabe el art. 849.1.º**.
  La skill los listaba todos: plantear otro motivo es inadmisión.
- **Prescripción civil aplicada al penal.** El intake calculaba por los arts. 1964/1968/1969 CC. Es
  el **art. 131 CP** (delito) y el **133 CP** (pena). Y el **art. 132.2.2.ª**: la denuncia o querella
  **no interrumpe** — solo **suspende 6 meses**.
- **Ficta confessio aplicada al acusado.** La skill de interrogatorio afirmaba, heredado del civil
  (LEC 304), que el silencio puede valorarse como confesión. **Es al revés**: el acusado tiene
  derecho a guardar silencio y a no declarar contra sí mismo (arts. 24.2 CE, 118 y 520.2 LECrim).
- **Tachas de testigos.** El plugin mandaba plantear tachas del art. 377 LEC. En penal **no existen**:
  la credibilidad se combate en el informe final, y la institución equivalente es la **dispensa del
  art. 416 LECrim**.
- **Carga de la prueba invertida.** `conservacion-documental` razonaba sobre LEC 217 y la presunción
  contra quien destruye prueba. En penal rige la **presunción de inocencia**: el defendido no tiene
  que probar nada.
- **Costas por vencimiento objetivo.** No existe en penal: «**No se impondrán nunca las costas a los
  procesados que fueren absueltos**» (art. 240.2.º LECrim).
- **Cuota litis y cómputo de plazos** heredados del civil (LEC 133): sustituidos por el **art. 183
  LOPJ** y el **art. 201 LECrim** (la instrucción no se paraliza en agosto).

### Añadido — once skills

Urgencia: `asistencia-detenido` · `habeas-corpus` · `juicio-rapido`
Control de riesgo: `computo-plazos-penal` · `ley-penal-en-el-tiempo` · `prueba-ilicita-nulidad`
Procedimientos: `audiencia-preliminar-abreviado` · `delitos-leves` ·
`violencia-genero-orden-proteccion` · `responsabilidad-penal-personas-juridicas` · `tribunal-jurado`

La más urgente no existía: **la asistencia al detenido**, que es lo primero que hace un penalista y
tiene un plazo de **3 horas** (art. 520.5 LECrim).

### Añadido — documentación

- **`references/anclas-normativas-penal.md`** — fuente única de verdad, verificada contra el BOE con
  fecha y regla de caducidad a los 6 meses. Incluye una sección sobre el **riesgo penal del propio
  abogado** (arts. 465-467 CP) que ningún plugin tenía, y la **limitación conocida del conector**
  (§ 12).
- **`PROTECCION-DATOS.md`** — política reforzada por el **art. 10 RGPD**.
- **`CHANGELOG.md`** — este archivo.

### Protección de datos

- Auditoría de los 35 archivos: **cero hallazgos** de DNI, IBAN, correos, teléfonos, direcciones,
  nombres o antecedentes reales.
- Eliminados los ejemplos con apariencia de cliente real heredados del plugin civil. Los **slugs se
  construyen por tipo delictivo, nunca por apellido**: un listado de carpetas que revele quién está
  investigado es una brecha del art. 10 RGPD y un daño irreversible.
- Retirada de `plugin.json` y `README.md` la frase «basadas en plantillas reales del despacho,
  anonimizadas»: documenta por escrito un tratamiento de datos **penales** de clientes.

### Hallazgos incorporados durante la verificación

Reglas verificadas que ninguna skill recogía:

- **Art. 324.3 LECrim:** si no se dictó el auto de prórroga **antes** del vencimiento, o fue revocado,
  **las diligencias acordadas después no son válidas**. El argumento de nulidad más rentable.
- **Art. 132.1 CP:** en delitos contra menores el cómputo se **difiere** — hasta la mayoría de edad, o
  hasta los **35 años** en tentativa de homicidio, lesiones 149/150, maltrato habitual, libertad
  sexual y trata.
- **Art. 701 LECrim (LO 1/2025):** el acusado puede **declarar en último lugar** y el Presidente «así
  lo acordará expresamente». No es discrecional.
- **Art. 785.7 in fine:** deber **nuevo** del letrado de facilitar **por escrito** al defendido la
  información sobre el acuerdo de conformidad.
- **Art. 785.4 párr. 2:** el Fiscal debe **oír a la víctima** antes de la conformidad.
- **El límite de los 6 años de la conformidad NO subsiste** — desapareció con la LO 1/2025, y el
  «seis años» del art. 787.1.a) es otra cosa (juicio en ausencia).
- **Cascada de remisiones rotas:** la LO 1/2025 no actualizó los arts. 784 y 801, que siguen
  apuntando al 787 (y el 801.3, al derogado art. 81.3.ª CP).
- **Art. 855 párr. 2 (RD-ley 5/2023):** en la vía del 847.1.b la preparación de la casación exige
  escrito **motivado**.
- **Art. 80.2.1.ª (LO 1/2026):** no se computan los antecedentes de delitos que «carezcan de
  relevancia para valorar la probabilidad de comisión de delitos futuros». Es **más favorable** y por
  tanto **retroactivo** (art. 2.2 CP): permite **revisar suspensiones denegadas**.
- **Art. 2.2 CP:** la retroactividad favorable opera **aunque haya sentencia firme y el sujeto esté
  cumpliendo condena**, y **debe oírse al reo**.
- **Art. 505.4:** si nadie la insta, libertad — el juez **no puede** acordar prisión provisional de
  oficio. **Art. 792.2:** la prohibición de *reformatio in peius* subsiste; el techo es **anular**.
- **Art. 963:** el sobreseimiento del delito leve **solo** procede si lo pide el Fiscal.
- **Art. 109 bis:** la personación tardía solo permite **adhesión**, sin retroacción.
- **Arts. 465-467 CP:** el abogado que destruye documentos del proceso comete delito con **prisión**;
  el conflicto de interés está **penalmente tipificado**; y el perjuicio al cliente **por imprudencia
  grave** también.

### Limitación conocida

`buscar_articulo` **trunca el sufijo alfabético** de la numeración: `588 bis a` → busca `588 bis` →
«no encontrado». Afecta a todo el bloque de **medidas de investigación tecnológica** (588 bis a –
588 septies c) y a la **apelación del Jurado** (846 bis a – f) — precisamente donde vive la prueba
ilícita. Documentado en las anclas § 12: esos preceptos van marcados `[verificar]`, **no** transcritos
de memoria.

---

## 0.1.0

Versión inicial. Dieciséis skills penales sobre la base de un fork del plugin de litigación civil.
