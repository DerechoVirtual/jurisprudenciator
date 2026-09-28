# Anclas normativas de laboral y asesoría de empresa

Cómo pedir a Jurisprudenciator cada norma, cada convenio y cada tipo de jurisprudencia. Todas las
skills del plugin usan estos valores. Léelo antes de la primera consulta.

## Contenido

1. Valor de `ley` para `buscar_articulo`
2. Normas que se piden por su identificador BOE (trampa del número)
3. Convenios colectivos
4. Jurisprudencia: filtros y doctrina que hay que buscar siempre
5. Registro Mercantil
6. Reformas y vigencia
7. Límites conocidos del conector

## 1. Valor de `ley` para `buscar_articulo`

Comprobados con el conector. Usa exactamente estos valores.

| Norma | `ley=` | Uso típico |
|---|---|---|
| Estatuto de los Trabajadores (RDL 2/2015) | `"ET"` | contratos (8-18), periodo de prueba (14), no competencia y permanencia (21), salario (26-33), jornada y registro (34-38), movilidad y modificaciones (39-41), sucesión y contratas (42-44), suspensión y ERTE (45-48), extinción y despido (49-57), faltas y sanciones (58), prescripción y caducidad (59-60) |
| Ley reguladora de la jurisdicción social (Ley 36/2011) | `"LRJS"` | competencia (10), conciliación previa (63-68), despido (103-113), sanciones (114-115), objetivo (120-123), movilidad y modificación (138), conciliación de la vida familiar (139), tutela (177-184) |
| Ley General de la Seguridad Social (RDL 8/2015) | `"LGSS"` | situación legal de desempleo (267), cotización |
| Ley de Prevención de Riesgos Laborales (Ley 31/1995) | `"LPRL"` | |
| Estatuto del trabajo autónomo (Ley 20/2007) | `"LETA"` | TRADE (11-18) |
| Infracciones y sanciones en el orden social (RDL 5/2000) | `"BOE-A-2000-15060"` | tipos y cuantías (arts. 5-40) |
| Reglamento de sanciones del orden social (RD 928/1998) | `"Real Decreto 928/1998"` | actas, alegaciones y plazos |
| Ordenadora de la Inspección de Trabajo (Ley 23/2015) | `"BOE-A-2015-8168"` | actuaciones y requerimientos (20-22) |
| Trabajo a distancia (Ley 10/2021) | `"BOE-A-2021-11472"` | acuerdo (5-8), derechos (9-19) |
| Alta dirección (RD 1382/1985) | `"BOE-A-1985-17006"` | contrato (4), extinción (10-11) |
| Servicio del hogar familiar (RD 1620/2011) | `"BOE-A-2011-17975"` | |
| Planes de igualdad (RD 901/2020) | `"BOE-A-2020-12214"` | |
| Igualdad retributiva y registro retributivo (RD 902/2020) | `"BOE-A-2020-12215"` | |
| Ley Orgánica de igualdad (LO 3/2007) | `"BOE-A-2007-6115"` | planes (45-49), acoso (7 y 48) |
| Igualdad de trato y no discriminación (Ley 15/2022) | `"BOE-A-2022-11589"` | |
| Libertad sexual (LO 10/2022) | `"LO 10/2022"` | prevención en el ámbito laboral (12) |
| Medidas LGTBI en las empresas (RD 1026/2024) | `"Real Decreto 1026/2024"` | |
| Protección del informante (Ley 2/2023) | `"BOE-A-2023-4513"` | entidades obligadas (10), sistema interno (4-9) |
| Despidos colectivos y ERTE (RD 1483/2012) | `"BOE-A-2012-13419"` | documentación y periodo de consultas |
| Reforma laboral (RDL 32/2021) | `"BOE-A-2021-21788"` | solo sus artículos; sus disposiciones transitorias (contratos anteriores, DT 6.ª de convenios) no las devuelve el conector: léelas en internet en el BOE consolidado |
| Protección de datos (LO 3/2018) | `"LOPDGDD"` | desconexión digital (88), videovigilancia (89), geolocalización (90), dispositivos digitales (87) |
| Reglamento general de protección de datos | `"RGPD"` | |
| Ley Orgánica del Poder Judicial | `"LOPJ"` | Tribunal de Instancia y sus Secciones (84 y ss.) |
| Constitución Española | `"CE"` | derechos fundamentales (14-29) |
| Ley Orgánica de Libertad Sindical (LO 11/1985) | `"LOLS"` | audiencia a los delegados sindicales (10) |
| Secretos empresariales (Ley 1/2019) | `"BOE-A-2019-2364"` | confidencialidad (1-3); con «Ley 1/2019» sale una ley valenciana |
| Registro de jornada: jornadas especiales (RD 1561/1995) | `"BOE-A-1995-21346"` | |
| Encuadramiento de autónomos: TRADE (RD 197/2009) | `"BOE-A-2009-3673"` | registro y contenido del contrato TRADE |
| Directiva de tiempo de trabajo | `"Directiva 2003/88/CE"` | (europea: `verificar_escrito` no la identifica) |
| Directiva de trabajo en plataformas | `"Directiva (UE) 2024/2831"` | plazo de transposición: 2 de diciembre de 2026 |
| Orden TAS/2865/2003 (convenio especial de Seguridad Social) | `"BOE-A-2003-19281"` | mayores de 55 años en despidos colectivos (20) |
| Real Decreto 1484/2012 (aportaciones al Tesoro) | `"BOE-A-2012-13420"` | despidos colectivos con trabajadores de 50 o más años |
| Código Civil | `"CC"` | |

## 2. Normas que se piden por su identificador BOE (trampa del número)

Con solo el número, el conector puede devolver **otra ley del mismo número**, casi siempre autonómica:
«Ley 10/2021» da una ley andaluza de tasas, «Ley 4/2023» una ley balear y la sigla «LISOS» una orden
ministerial sobre alambres. Pide esas normas por su identificador BOE de la tabla. **Comprueba
siempre el título que encabeza la respuesta** de `buscar_articulo` antes de usar el texto: si no es la
norma que buscabas, busca su identificador con `buscar_boe` (título completo) y repite. La Ley
4/2023, de 28 de febrero (LGTBI), se busca así.

## 3. Convenios colectivos

- `buscar_convenio` (`consulta` = sector o actividad, `territorio` = provincia o comunidad del centro de
  trabajo): devuelve el código de 14 dígitos y el enlace al texto oficial. Pedir una provincia añade
  el autonómico y el estatal: elige por el **ámbito funcional** (actividad real de la empresa) y el
  territorial, y explica la elección.
- `leer_convenio` (`codigo`, `articulo="N"` o `buscar_en="materia"`): artículo concreto o pasajes de una
  materia (periodo de prueba, preaviso, faltas y sanciones, jornada, permisos, subrogación,
  complementos).
- `vigencia_convenio` (`codigo`): vigencia y trámites. Comprueba que el texto que usas es el que regía en
  la fecha de los hechos.
- **`leer_convenio` no dice qué texto está en vigor**: puede devolver una publicación antigua aunque el
  registro tenga un texto posterior, la carcasa HTML del boletín, una portada o un error de descarga, y
  con `buscar_en` a veces casa pasajes de otra materia. Contrasta siempre la fecha de la publicación que
  devuelve con la lista de `vigencia_convenio`; si no es el texto vigente o no se lee, búscalo en
  internet en el boletín oficial y, si tampoco aparece, pídelo al abogado.
- **El texto vigente del convenio y sus tablas se buscan en internet** en cuanto `leer_convenio` falle:
  `buscar_boe`, `sumario_boe` y `novedades_boe` no encuentran los convenios (sección III del BOE ni
  boletines autonómicos o provinciales). Del boletín oficial salen también el precio de la hora
  extraordinaria, los pluses, el interés por mora que fije el convenio y el calendario pactado.
- `buscar_convenio` con `ambito="empresa"` devuelve coincidencias aproximadas: confirma que el convenio
  de empresa es el de la sociedad del cliente (denominación y CIF).
- **Tablas salariales: `leer_convenio` no las devuelve de forma fiable** (las búsquedas por «tabla
  salarial» o «salario base» traen otros pasajes, y las revisiones salariales se publican aparte).
  Para el salario: en despidos y finiquitos, las **nóminas** del trabajador; para reclamar diferencias
  con el convenio, busca en internet la tabla salarial publicada del año que toca (revisión salarial en
  el BOE, el boletín autonómico o el BOP; `vigencia_convenio` dice qué publicaciones hay) y cítala con su
  enlace; si no aparece, pídela al abogado. Sin tabla no se calculan diferencias salariales: la tarea se
  detiene en ese punto.

## 4. Jurisprudencia: filtros y doctrina que hay que buscar siempre

- Sala Cuarta del Tribunal Supremo: `buscar_sentencias` con `base="TS"`, `jurisdiccion="SOCIAL"`.
- Salas de lo Social de los TSJ y Secciones de lo Social: `base="AN"`, `jurisdiccion="SOCIAL"`,
  `tipo_organo="TSJ"` y `provincia` con la **sede de la Sala** (no la provincia del cliente si no es
  sede): con una provincia sin Sala el buscador puede no devolver nada.
- Tribunal Constitucional (indicios de discriminación, garantía de indemnidad): `base="TC"`.
- TJUE (tiempo de trabajo, igualdad, despidos colectivos, sucesión de empresa): `base="TJUE"`.
- Fechas en formato `dd/mm/aaaa`. Tras la reforma de 2021 (contratos) y las de 2023-2025 (permisos,
  despido, desempleo) usa `fecha_desde` o `anios=3` para no citar doctrina superada.
- **Audiencia previa al despido disciplinario**: el Pleno de la Sala Cuarta exigió en noviembre de
  2024 dar audiencia al trabajador antes del despido disciplinario (artículo 7 del Convenio 158 de la
  OIT), con efectos para los despidos posteriores a esa sentencia. Búscala siempre en despidos
  disciplinarios: `buscar_sentencias` (`consulta="audiencia previa despido disciplinario artículo 7
  Convenio 158 OIT"`, `base="TS"`, `jurisdiccion="SOCIAL"`) y lee la del Pleno y la más reciente que la
  aplique.
- Lee solo lo que vayas a citar: `leer_sentencias` con `parrafos=3` y `terminos` de la cuestión.
- `guia_escrito` (`jurisdiccion="laboral"`) devuelve el método del despacho para un escrito procesal
  (papeleta, demanda, recurso): úsala en las skills que redactan escritos al juzgado o al servicio de
  conciliación.

## 5. Registro Mercantil

`buscar_empresa_mercantil` (nombre o CIF; busca por CIF siempre que lo tengas, porque por nombre
devuelve coincidencias aproximadas y puede traer otra sociedad): denominación exacta, domicilio social, administradores,
estado (disolución, concurso). Úsalo para identificar a la empresa demandada, detectar grupo de
empresas o sucesión, y decidir si se cita al FOGASA. Es informativo, sin fe pública.

## 6. Reformas y vigencia

`buscar_articulo` devuelve «vigente desde… redacción vigente dada por…». Léela en cada artículo: el
ET y la LRJS se han reformado muchas veces (RDL 32/2021, RDL 5/2023, RDL 6/2023, LO 1/2025, RDL
2/2024). Para novedades de una materia, `buscar_boe` con `desde`; `novedades_boe` solo recorre 31 días
desde la fecha inicial, así que sirve para una ventana concreta, no para rastrear años.

## 7. Límites conocidos del conector

- **Versión anterior tras «Téngase en cuenta»**: en algunos artículos (ET 12, 16, 55.5, 53.4) el
  conector devuelve el texto vigente y, detrás de la nota «Téngase en cuenta», el texto anterior entre
  comillas. El vigente es el de arriba; si la nota anuncia una redacción futura o dudosa, compruébala
  en internet en el texto consolidado del BOE.
- **Autos de inadmisión**: muchos resultados del Supremo son autos que inadmiten el recurso por falta
  de contradicción; no son doctrina y no se citan como tal.
- **Disposiciones adicionales y transitorias** (la transitoria undécima del Estatuto de los
  Trabajadores, las adicionales de la LGSS sobre convenio especial, Mecanismo RED o exoneraciones) y
  los artículos 5 y 6 del Real Decreto 1483/2012: `buscar_articulo` no los devuelve. Léelos en internet
  en el texto consolidado del BOE y cítalos con su enlace.

- **Convenio 158 de la OIT**: el conector no devuelve su texto. Léelo en internet (instrumento de
  ratificación publicado en el BOE o la base oficial de la OIT) y cítalo con su enlace, o a través de la
  sentencia del Supremo que lo aplica (párrafo literal leído); nunca de memoria.
- **Lo que el conector no cubre se busca en internet** (punto 3 de la puerta de cada skill): fuentes
  oficiales siempre que existan, con enlace y fecha de consulta, y aviso en el resumen de qué dato no
  sale de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la
  localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Ejemplos: nombre del servicio autonómico de conciliación, modelos oficiales, SMI o bases de
  cotización del año, criterios técnicos de la Inspección.
- Tablas salariales de los convenios: ver el apartado 3.
- El texto de la LRJS conserva «Juzgados de lo Social» en su articulado; el órgano actual se
  determina con la LOPJ (apartado 3 del formato).
- `verificar_escrito` no identifica los reglamentos ni las directivas de la Unión ni los convenios
  colectivos: atribuye su artículo a la última norma española nombrada. Comprueba cada artículo de
  convenio con `leer_convenio` y cada artículo europeo con `buscar_articulo`, e ignora el veredicto de
  `verificar_escrito` sobre ellos.
- `verificar_escrito` marca a veces «posible disonancia» cuando un párrafo habla de varias materias:
  compara el artículo con lo que afirma el escrito y decide.
