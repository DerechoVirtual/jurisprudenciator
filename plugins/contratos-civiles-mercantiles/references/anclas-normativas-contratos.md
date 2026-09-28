# Anclas normativas de contratos civiles y mercantiles

Cómo pedir a Jurisprudenciator cada norma y cada tipo de jurisprudencia. Todas las skills del plugin
usan estos valores. Léelo antes de la primera consulta.

## Contenido

1. Valor de `ley` para `buscar_articulo`
2. Normas que se piden por su identificador BOE (trampa del número)
3. Normas de la Unión Europea
4. Jurisprudencia: filtros
5. Registro Mercantil y Catastro
6. Reformas y vigencia
7. Límites conocidos del conector

## 1. Valor de `ley` para `buscar_articulo`

Comprobados con el conector. Usa exactamente estos valores.

| Norma | `ley=` | Uso típico |
|---|---|---|
| Código Civil | `"CC"` | obligaciones y contratos (arts. 1088-1314), compraventa (1445-1537), arras (1454), saneamiento (1484-1499), arrendamiento de obras y servicios (1542-1603), préstamo (1740-1757), fianza (1822-1856), interpretación (1281-1289), prescripción (1961-1975) |
| Código de Comercio | `"CCom"` | compraventa mercantil (325-345), comisión (244-302), préstamo mercantil (311-324), plazos de denuncia de vicios (336 y 342) |
| Ley de Sociedades de Capital (RDL 1/2010) | `"LSC"` | transmisión de participaciones (106-112), acciones (120-127), pactos reservados (29), administradores (209-241) |
| Ley de Enjuiciamiento Civil | `"LEC"` | monitorio (812-818), competencia territorial (50-52), cuantía (249-253) |
| Ley Orgánica 1/2025 (MASC y Tribunales de Instancia) | `"LO 1/2025"` | requisito de procedibilidad (art. 5), medios adecuados (arts. 2-19) |
| Ley Orgánica del Poder Judicial | `"LOPJ"` | Tribunal de Instancia y sus Secciones (arts. 84 y ss.; Sección de lo Mercantil, art. 87) |
| Constitución Española | `"CE"` | |
| Texto refundido de consumidores (RDL 1/2007) | `"TRLGDCU"` | cláusulas abusivas (82-91), información precontractual (60), desistimiento (68-79), garantías (114-127) |
| Servicios de atención a la clientela (Ley 10/2025) | `"BOE-A-2025-26698"` | reformó los arts. 21, 62 y 97 del TRLGDCU (vigente desde el 28/12/2025) |
| Ley de Arrendamientos Urbanos (Ley 29/1994) | `"LAU"` | vivienda (arts. 6-28), uso distinto (29-35), fianza y garantías (36) |
| Ley 12/2023, por el derecho a la vivienda | `"Ley 12/2023"` | información mínima en compra y alquiler (art. 31), zonas tensionadas |
| Ley de Propiedad Horizontal (Ley 49/1960) | `"Ley 49/1960"` | comunidad, derechos de adquisición |
| Ley Hipotecaria | `"BOE-A-1946-2453"` | fe pública registral (34), inscripción |
| Cantidades anticipadas en compras sobre plano | disposición adicional primera de la LOE | la Ley 57/1968 está **derogada** (Ley 20/2015) aunque el conector la dé por vigente; la adicional no la devuelve `buscar_articulo`: léela en internet en el BOE consolidado |
| Ley de Ordenación de la Edificación (Ley 38/1999) | `"BOE-A-1999-21567"` | responsabilidad de los agentes (17), garantías (19) |
| Condiciones generales de la contratación (Ley 7/1998) | `"BOE-A-1998-8789"` | incorporación (5 y 7), nulidad (8), interpretación (6) |
| Morosidad en operaciones comerciales (Ley 3/2004) | `"BOE-A-2004-21830"` | plazo de pago (4), interés de demora (7), costes de cobro (8), cláusulas abusivas (9) |
| Contrato de agencia (Ley 12/1992) | `"Ley 12/1992"` | preaviso (25), indemnización por clientela (28), daños (29), no competencia (20) |
| Franquicia (Real Decreto 201/2010) | `"RD 201/2010"` | información precontractual (3); el registro de franquiciadores (arts. 5 y ss.) está suprimido desde el RDL 20/2018 aunque el conector lo dé como vigente |
| Comercio minorista (Ley 7/1996) | `"Ley 7/1996"` | |
| Defensa de la Competencia (Ley 15/2007) | `"Ley 15/2007"` | conductas colusorias en distribución (1) |
| Competencia desleal (Ley 3/1991) | `"BOE-A-1991-628"` | |
| Secretos empresariales (Ley 1/2019) | `"BOE-A-2019-2364"` | concepto (1), violación (3) |
| Propiedad intelectual (RDL 1/1996) | `"TRLPI"` | transmisión inter vivos (43-57), programas de ordenador (95-104) |
| Ley de Marcas (Ley 17/2001) | `"Ley 17/2001"` | licencia (48), cesión (47) |
| Protección de datos (LO 3/2018) | `"LOPDGDD"` | encargado del tratamiento (33) |
| Servicios de la sociedad de la información (Ley 34/2002) | `"Ley 34/2002"` | contratación electrónica (23-29) |
| Crédito inmobiliario (Ley 5/2019) | `"BOE-A-2019-3814"` | |
| Préstamos de empresas no entidades de crédito (Ley 2/2009) | `"BOE-A-2009-5391"` | |
| Crédito al consumo (Ley 16/2011) | `"BOE-A-2011-10970"` | |
| Ley de represión de la usura (1908) | `"Ley de 23 de julio de 1908"` | nulidad del préstamo usurario (1) |
| Limitación de pagos en efectivo (Ley 7/2012) | `"BOE-A-2012-13416"` | art. 7 |
| Ley Concursal (RDL 1/2020) | `"TRLC"` | efectos del concurso sobre los contratos: la cláusula que permite resolver por la declaración de concurso se tiene por no puesta (art. 156) |
| Ley de Arbitraje (Ley 60/2003) | `"Ley 60/2003"` | convenio arbitral (9) |
| Catastro Inmobiliario (RDL 1/2004) | `"Real Decreto Legislativo 1/2004"` | referencia catastral en documentos (38, 40, 41) |
| Ley del Suelo (RDL 7/2015) | `"BOE-A-2015-11723"` | transmisión de fincas (27) |
| Haciendas Locales (RDL 2/2004) | `"BOE-A-2004-4214"` | IBI (63-64), plusvalía (104-110) |
| Certificación energética de edificios (RD 390/2021) | `"BOE-A-2021-9176"` | certificado en venta y alquiler |
| Registro único de arrendamientos (RD 1312/2024) | `"BOE-A-2024-26931"` | parcialmente anulado por el Supremo en 2026: lee las notas de nulidad |
| Ley General Tributaria | `"LGT"` | |
| ITP y AJD (RDL 1/1993) | `"BOE-A-1993-25359"` | |
| IRPF (Ley 35/2006) | `"BOE-A-2006-20764"` | |
| Subcontratación en la construcción (Ley 32/2006) | `"BOE-A-2006-18205"` | |
| Venta a plazos de bienes muebles (Ley 28/1998) | `"BOE-A-1998-16717"` | reserva de dominio |
| Convención de Viena sobre compraventa internacional | `"BOE-A-1991-2552"` | (`verificar_escrito` no la identifica) |
| Reglamentos europeos | CELEX: Roma I `"32008R0593"`, Bruselas I bis `"32012R1215"`, exención vertical `"32022R0720"`, transferencia de tecnología `"32026R0877"` (sustituye al 316/2014, que expiró el 30/04/2026) | (`verificar_escrito` no los identifica) |
| Reglamento del Registro Mercantil (RD 1784/1996) | `"BOE-A-1996-17533"` | cítalo como «Real Decreto 1784/1996» (con «Reglamento del Registro Mercantil» a secas el verificador lo atribuye a la LSC) |
| Inversiones exteriores (Ley 19/2003) | `"BOE-A-2003-13471"` | art. 7 bis (con «Ley 19/2003» sale la ley del taxi) |
| Patentes (Ley 24/2015) | `"Ley 24/2015"` | licencias (82-83) |
| Contratos del Sector Público (Ley 9/2017) | `"LCSP"` | |
| Mediación en asuntos civiles y mercantiles (Ley 5/2012) | `"BOE-A-2012-9112"` | |

## 2. Normas que se piden por su identificador BOE (trampa del número)

Con solo el número, el conector puede devolver **otra ley del mismo número**, casi siempre autonómica:
«Ley 7/1998» da una ley andaluza de colegios profesionales, «Ley 3/2004» una ley vasca de
universidades, «Ley 5/2019» una ley gallega, «LOE» la Ley Orgánica de Educación y «Ley Hipotecaria»
un reglamento europeo. Pide esas normas por su identificador BOE de la tabla. **Comprueba siempre el
título que encabeza la respuesta** de `buscar_articulo` antes de usar el texto: si no es la norma que
buscabas, busca su identificador con `buscar_boe` (título completo de la norma) y repite.

## 3. Normas de la Unión Europea

`buscar_articulo` con `ley="RGPD"` devuelve el Reglamento (UE) 2016/679 (texto consolidado, CELEX).
Para otras normas de la Unión, busca con `buscar_boe` (el resultado trae su CELEX) y pide el artículo
con ese CELEX o con su número oficial. `verificar_escrito` **no identifica** reglamentos ni directivas
de la Unión: atribuye su artículo a la última norma española nombrada. Comprueba cada artículo
europeo con `buscar_articulo` e ignora el veredicto de `verificar_escrito` sobre él.

## 4. Jurisprudencia: filtros

- Sala Primera del Tribunal Supremo: `buscar_sentencias` con `base="TS"`, `jurisdiccion="CIVIL"`.
- Audiencias Provinciales y Secciones Civiles de los Tribunales de Instancia: `base="AN"`,
  `jurisdiccion="CIVIL"`, `tipo_organo="AP"` y, si interesa una plaza, `provincia="<provincia>"`.
- Tribunal de Justicia de la UE (cláusulas abusivas, Directiva 93/13, morosidad): `base="TJUE"`, con
  tildes y sin comillas.
- Fechas en formato `dd/mm/aaaa`. Si la materia cambió hace poco (vivienda tras la Ley 12/2023,
  MASC tras la LO 1/2025), usa `fecha_desde` o `anios=3`.
- Lee solo lo que vayas a citar: `leer_sentencias` con `parrafos=3` y `terminos` de la cuestión.
- Prefiere la Sala Primera; cita una Audiencia Provincial cuando no haya doctrina del Supremo sobre
  el punto o cuando el asunto se vaya a litigar en esa plaza, diciendo que es doctrina de Audiencia.

## 5. Registro Mercantil y Catastro

- `buscar_empresa_mercantil` (nombre o CIF): existencia, estado, domicilio, administradores y
  apoderados vigentes, últimos actos (disolución, concurso, cambios de domicilio). Es informativo, sin
  fe pública: para una operación relevante, recomienda nota simple del Registro Mercantil y copia de
  los poderes.
- `consultar_catastro` (referencia catastral o dirección y municipio): referencia, uso, superficie,
  año de construcción, coeficiente. **No da titular ni valor catastral** ni cubre País Vasco y
  Navarra (para esas provincias, busca en internet su catastro foral): la titularidad y las cargas
  salen de la nota simple del Registro de la Propiedad, que ni el conector ni una búsqueda pública dan.
  Pídela al abogado en toda operación sobre inmuebles.
- `buscar_ordenanzas` / `leer_ordenanza` para usos permitidos de un local o normas municipales de
  viviendas de uso turístico.

## 6. Reformas y vigencia

`buscar_articulo` devuelve la línea «vigente desde… redacción vigente dada por…». Léela: dice si el
artículo se ha reformado y por qué norma. Para novedades de una materia, `novedades_boe` o
`buscar_boe` con `desde`. No afirmes que una norma «está en vigor» sin esa línea.

## 7. Límites conocidos del conector

- No consulta el Registro de la Propiedad (titularidad, cargas) ni el contenido de las cuentas
  anuales depositadas en el Registro Mercantil.
- Convenios internacionales: pídelos por su identificador BOE (la Convención de Viena sale con
  `ley="BOE-A-1991-2552"`); si uno no aparece, búscalo en internet (su publicación en el BOE o la
  fuente oficial del tratado) y cítalo con enlace y fecha de consulta, nunca de memoria.
- **Disposiciones adicionales, transitorias y finales** (LAU, Ley 12/2023, LOE): `buscar_articulo` no
  las devuelve y `leer_boe` se corta en las leyes largas. Léelas en internet en el texto consolidado
  del BOE. Lo mismo para datos que el conector no tiene: declaraciones de zona tensionada, índice de
  actualización de rentas del INE, interés legal del dinero (el tipo de la Ley 3/2004 sí sale con
  `novedades_boe`).
- **Versión anterior tras «Téngase en cuenta»**: en algunos artículos (LSC 107, 124, 353; TRLGDCU 120,
  123, 124; LEC 250) el conector devuelve el texto vigente y, detrás de la nota, una redacción anterior
  entre comillas. El vigente es el cuerpo del artículo.
- `verificar_escrito` no identifica la Ley de usura de 1908, la Convención de Viena ni los reglamentos
  europeos: comprueba esos artículos con `buscar_articulo` e ignora su veredicto.
- `verificar_escrito` marca a veces «posible disonancia» cuando el párrafo habla de varias materias:
  compara el artículo con lo que afirma el escrito y decide; no cambies una cita correcta solo por ese
  aviso.
- Normas forales y autonómicas de Derecho civil (Cataluña, Aragón, Navarra, País Vasco, Galicia,
  Baleares): pídelas por su nombre o identificador con `buscar_boe`. `buscar_articulo` no resuelve la
  numeración con guion (Código civil de Cataluña) y con ese nombre devuelve el artículo del Código Civil
  estatal: lee esos preceptos en internet en el texto consolidado oficial (BOE o boletín de la comunidad).
- `buscar_articulo` con `ley="CC"` y `articulo="9"` devuelve por error el artículo 94 bis: para la ley
  aplicable a la capacidad, usa el Reglamento Roma I o lee el artículo 9 del Código Civil en internet
  (texto consolidado del BOE).
- **Lo que el conector no cubre se busca en internet** (punto 3 de la puerta de cada skill): fuentes
  oficiales siempre que existan, con enlace y fecha de consulta, y aviso en el resumen de qué dato no
  sale de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la
  localiza con `buscar_por_cita` y se lee con `leer_sentencias`.
