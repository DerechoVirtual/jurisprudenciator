# Formato y entrega de los documentos de contratos

Reglas comunes a todas las skills del plugin. Cada skill dice qué documento produce. Aquí está cómo
se maqueta, cómo se justifica y cómo se cita.

## Contenido

1. Entregables y nombres de archivo
2. Maquetación del contrato
3. Nota para el abogado
4. Informes de revisión y contrapropuestas
5. Requerimientos, burofaxes y escritos al juzgado
6. Cómo se cita
7. Datos de las partes
8. Cuándo es imprescindible la jurisprudencia
9. Plazos
10. Resumen para el abogado

## 1. Entregables y nombres de archivo

Todo documento se entrega en **Word (.docx)**, nunca solo en el chat. Si en el entorno no se pueden
crear archivos, entrega el texto completo maquetado y avisa de que hay que pasarlo a Word.

| Documento | Nombre del archivo |
|---|---|
| Contrato | `contrato-<tipo>-<parte-principal>-<AAAAMMDD>.docx` |
| Nota para el abogado | `nota-<tipo>-<parte-principal>-<AAAAMMDD>.docx` |
| Informe de revisión | `revision-<tipo>-<parte-principal>-<AAAAMMDD>.docx` |
| Contrapropuesta | `contrapropuesta-<tipo>-<parte-principal>-<AAAAMMDD>.docx` |
| Requerimiento o burofax | `requerimiento-<destinatario>-<AAAAMMDD>.docx` |
| Escrito judicial | `<tipo-escrito>-<parte>-<AAAAMMDD>.docx` |

Toda skill que redacta un contrato entrega **dos documentos**: el contrato, limpio y listo para
firmar, y la nota para el abogado (apartado 3). El contrato no lleva jurisprudencia.

## 2. Maquetación del contrato

- Times New Roman 12, A4 vertical, márgenes de 3 cm, texto justificado, interlineado 1,5.
- Título centrado en mayúsculas («CONTRATO DE ARRENDAMIENTO DE VIVIENDA»), lugar y fecha.
- **REUNIDOS**: identificación de cada firmante (nombre, DNI/NIE, domicilio).
- **INTERVIENEN**: en nombre propio o en representación. Para sociedades: denominación, CIF,
  domicilio, datos de inscripción y cargo o poder con el que firma (notario, fecha y número de
  protocolo). Cierra con el reconocimiento recíproco de capacidad.
- **EXPONEN**: antecedentes en romanos (I, II, III): titularidad, finalidad, hechos que explican el
  pacto. Solo lo que sirva para interpretar el contrato.
- **ESTIPULACIONES** (o CLÁUSULAS): ordinales en mayúsculas con título («PRIMERA.- Objeto.»),
  subapartados numerados (1.1, 1.2). Orden habitual: objeto, precio y forma de pago, duración,
  obligaciones de cada parte, garantías, incumplimiento y resolución, cláusula penal si la hay,
  confidencialidad y datos, cesión, notificaciones (direcciones y medios), ley aplicable y fuero o
  arbitraje, integridad del acuerdo.
- Una definición por término y un término por concepto: si defines «el Inmueble», no alternes con
  «la vivienda» o «la finca».
- Cierre: «Y en prueba de conformidad, firman el presente contrato por duplicado y a un solo efecto
  en el lugar y fecha indicados.» Bloque de firmas en dos columnas (tabla de dos celdas sin bordes).
- **ANEXOS** numerados: inventario, planos, certificado energético, lista de precios, etc.
- Solo cita artículos en el contrato cuando el efecto jurídico dependa de nombrarlos (arras del
  artículo 1454 del Código Civil, renuncia permitida por un artículo de la LAU). La justificación
  del resto va en la nota.

## 3. Nota para el abogado

Documento breve (normalmente de 3 a 6 páginas) que justifica el contrato:

1. Tipo de contrato y régimen jurídico aplicable, con los artículos leídos (norma imperativa frente a
   lo que es pactable).
2. **Cláusulas críticas**: por cada una, qué dice, por qué así, el artículo que la respalda y, cuando
   la validez dependa de la jurisprudencia (apartado 8), el párrafo literal con órgano, fecha y ECLI.
3. Datos pendientes, marcados en el contrato con `[…]`, y documentos que hay que pedir (nota simple,
   poderes, certificado energético…).
4. Riesgos y alternativas de redacción, si las hay.
5. Tributación y formalidades que el abogado debe comprobar (escritura pública, inscripción,
   depósito de fianza, liquidación de impuestos), sin dar importes que no hayas comprobado con una
   herramienta.

## 4. Informes de revisión y contrapropuestas

- **Informe de revisión (semáforo)**: resumen ejecutivo de 5-10 líneas; tabla con columnas
  `Cláusula | Riesgo | Motivo y base legal | Propuesta`; riesgo en **ROJO** (nula, abusiva o
  gravemente perjudicial, hay que cambiarla), **ÁMBAR** (desequilibrada o ambigua, conviene negociar) o
  **VERDE** (correcta). Después, cláusulas que faltan y conclusión.
- **Contrapropuesta**: tabla `Cláusula | Texto actual | Texto propuesto | Motivo` y, al final, el texto
  íntegro de las cláusulas modificadas en limpio. Añade, si lo pide el abogado, el correo o la carta
  de remisión a la otra parte.
- El análisis de validez de una cláusula va con su artículo y, cuando lo exija el apartado 8, con la
  jurisprudencia literal.

## 5. Requerimientos, burofaxes y escritos al juzgado

- Requerimiento o burofax: remitente y destinatario con domicilio, lugar y fecha, asunto, hechos
  numerados, requerimiento concreto (qué, cuánto y en qué plazo), consecuencias del incumplimiento y
  firma. Sin fundamentos jurídicos extensos: los artículos imprescindibles, citados con su norma. El
  envío fehaciente (burofax con certificación de texto y acuse, conducto notarial) lo decide el
  abogado; no des precios ni límites de páginas del servicio.
- Escrito judicial (monitorio y otros): encabezamiento al órgano en mayúsculas («AL TRIBUNAL DE
  INSTANCIA DE [SEDE], SECCIÓN CIVIL», o «SECCIÓN ÚNICA DE CIVIL Y DE INSTRUCCIÓN» donde no haya
  Sección Civil separada; comprueba la denominación con los arts. 84 y 85 de la Ley Orgánica del Poder
  Judicial: la LEC aún dice «Juzgado de Primera Instancia»),
  comparecencia, hechos y fundamentos en ordinales, súplica («SUPLICO»), otrosíes, lugar, fecha,
  firma y relación de documentos.

## 6. Cómo se cita

- Artículos: con el texto vigente que devuelve `buscar_articulo` y su norma nombrada de forma que
  `verificar_escrito` la reconozca: «artículo 1124 del Código Civil», «artículo 36 de la Ley 29/1994,
  de 24 de noviembre, de Arrendamientos Urbanos», «artículo 107 de la Ley de Sociedades de Capital»,
  «artículo 83 del Real Decreto Legislativo 1/2007», «artículo 8 de la Ley 7/1998, de 13 de abril,
  sobre condiciones generales de la contratación», «artículo 7 de la Ley 3/2004, de 29 de diciembre»,
  «artículo 28 de la Ley 12/1992, de 27 de mayo, sobre Contrato de Agencia», «artículo 17 de la Ley
  38/1999, de 5 de noviembre, de Ordenación de la Edificación».
- **Pon la fecha de la ley en cada mención** de las leyes con número repetido (apartado 2 de las
  anclas): sin la fecha, el verificador puede tomar otra ley del mismo número.
- Apartados con letra: «la letra c) del artículo 85 del Real Decreto Legislativo 1/2007» o «artículo
  85 del Real Decreto Legislativo 1/2007, letra c)». Con «85.c)» pegado, el verificador no enlaza la
  norma y compara con la última que se nombró.
- Cada artículo con su norma: no escribas «(artículo 1101)» suelto ni «de la misma ley». En una
  enumeración («artículos 1101, 1106 y 1107»), el verificador solo enlaza el último: nombra la norma con
  cada uno o cítalos por separado.
- Si `verificar_escrito` marca un artículo como no localizado, compruébalo con `buscar_articulo` y el
  valor de `ley` de las anclas: si lo devuelve, el aviso se debe a cómo está nombrada la norma y hay
  que corregir el nombre.
- Jurisprudencia (solo en notas, informes y escritos, nunca en el contrato): párrafo literal entre
  comillas, seguido de órgano, fecha, número y ECLI tal como los devolvió `leer_sentencias`. Cita
  fundamentos jurídicos (doctrina), nunca el relato de hechos ni los datos de las partes de aquel
  pleito. Comprueba que el párrafo es razonamiento de la Sala y no alegación de parte o voto
  particular.
- Con `parrafos=3`, `leer_sentencias` devuelve a menudo alegaciones de parte o el relato procesal. Si
  no ves el razonamiento de la Sala, repite con `terminos` que apunten a la decisión («la sala
  considera», «debemos», «procede estimar», más la cuestión) antes de buscar otra sentencia.
- No escribas «dicha ley», «la misma ley», «el mismo artículo» ni «en su artículo»: el verificador
  atribuye esos artículos a otra norma. Repite el nombre de la norma. Y no pongas en los anexos de
  fuentes listas de números de artículo de varias normas: cita cada artículo en el texto con su norma.
- La jurisprudencia se atribuye a Jurisprudenciator o a «la base oficial de jurisprudencia».
- Ningún documento contiene un ECLI, un artículo o un plazo que no se haya obtenido en esta
  conversación con una herramienta de Jurisprudenciator o, cuando Jurisprudenciator no lo tenga, de una
  fuente de internet citada con su enlace (punto 3 de la puerta).

## 7. Datos de las partes

- Marcadores para lo que no se ha facilitado: `[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[DOMICILIO]`,
  `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[REFERENCIA CATASTRAL]`, `[DATOS REGISTRALES]`, `[IMPORTE]`,
  `[IBAN]`. Nunca inventes un dato.
- Si una parte es sociedad, comprueba su existencia, estado y administradores con
  `buscar_empresa_mercantil`; si firma alguien que no aparece como administrador o apoderado, dilo en
  la nota.
- En las consultas a Jurisprudenciator busca por la cuestión jurídica, nunca por el nombre o el DNI
  de un particular. Sí puedes buscar por el nombre o el CIF de una sociedad en
  `buscar_empresa_mercantil`.

## 8. Cuándo es imprescindible la jurisprudencia

La puerta de cada skill se aplica siempre a `estado` y a los artículos: sin el texto vigente que
devuelva Jurisprudenciator no se redacta nada.

- **Imprescindible** (si tras dos reformulaciones no hay ninguna resolución aplicable, se aplica el
  punto 3 de la puerta: búsqueda en internet y localización en Jurisprudenciator; si tampoco así
  aparece, la tarea se detiene): informes de revisión, dictámenes, requerimientos y escritos que reclaman o resuelven, y
  toda cláusula cuya validez discute la jurisprudencia (arras penitenciales frente a confirmatorias,
  moderación de la cláusula penal, cláusulas abusivas y transparencia, indemnización por clientela en
  la distribución, pactos de no competencia, vencimiento anticipado, renuncia a derechos del
  arrendatario, usura).
- **Se busca y se cita si existe**: cláusulas ordinarias que se sostienen en el texto de la norma. Si
  no hay doctrina, la cláusula se redacta sobre el artículo y la nota lo dice.

## 9. Plazos

Calcula cada plazo con el precepto que devuelva `buscar_articulo` (prescripción de acciones, caducidad
de la acción de saneamiento, preaviso contractual o legal, plazo del requerimiento). Indica la fecha
inicial, el precepto y la fecha final calculada. Si no consta la fecha inicial, pídela; sin ella no se
da un plazo.

## 10. Resumen para el abogado

Acompaña cada entrega con un resumen breve en el chat:

1. Qué se ha preparado y para quién.
2. Cláusulas críticas y cómo se han resuelto.
3. Datos y documentos que faltan, y riesgos detectados.
4. Tabla de jurisprudencia citada: ECLI · órgano · fecha · qué sostiene (si la hay).
5. Plazos con su precepto, si los hay, y próximo paso recomendado.
