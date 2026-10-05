# Formato, órganos y plazos de laboral y asesoría de empresa

Reglas comunes a todas las skills del plugin. Cada skill dice qué documento produce. Aquí está cómo
se maqueta, a quién se dirige, cómo se cita y cómo se calculan los plazos.

## Contenido

1. Entregables y nombres de archivo
2. Maquetación
3. Órganos y destinatarios
4. Cómo se cita
5. Datos del trabajador y de la empresa
6. Plazos
7. Cálculos (salario, indemnización, finiquito)
8. Cuándo es imprescindible la jurisprudencia
9. Resumen para el abogado

## 1. Entregables y nombres de archivo

Todo documento se entrega en **Word (.docx)**, nunca solo en el chat. Si en el entorno no se pueden
crear archivos, entrega el texto completo maquetado y avisa de que hay que pasarlo a Word.

| Documento | Nombre del archivo |
|---|---|
| Contrato, pacto o acuerdo | `contrato-<tipo>-<apellido-trabajador>-<AAAAMMDD>.docx` |
| Carta a un trabajador (despido, sanción, traslado, modificación) | `carta-<tipo>-<apellido-trabajador>-<AAAAMMDD>.docx` |
| Nota o informe para el abogado o la empresa | `nota-<asunto>-<empresa>-<AAAAMMDD>.docx` |
| Hoja de cálculo en Word (indemnización, finiquito) | `calculo-<concepto>-<apellido-trabajador>-<AAAAMMDD>.docx` |
| Papeleta, demanda o escrito | `<tipo-escrito>-<apellido-cliente>-<AAAAMMDD>.docx` |
| Protocolo, plan o procedimiento interno | `<tipo>-<empresa>-<AAAAMMDD>.docx` |

Las skills que redactan un contrato, una carta o un protocolo pueden entregar además una **nota para el
abogado** (qué se ha hecho y por qué, artículos del ET y del convenio leídos, riesgos y, cuando lo
exija el apartado 8, la jurisprudencia literal), en Word aparte solo si el abogado la pide: si no, ese
contenido va en el resumen de la entrega (apartado 9). Cuando la nota es el único entregable (revisión,
análisis o defensa de la parte para la que no se redacta escrito), se entrega siempre. La carta y el
contrato no llevan jurisprudencia.

## 2. Maquetación

- Times New Roman 12, A4 vertical, márgenes de 3 cm, texto justificado, interlineado 1,5.
- **Contratos y pactos**: título centrado en mayúsculas, lugar y fecha, REUNIDOS, INTERVIENEN, EXPONEN,
  CLÁUSULAS numeradas en ordinales con título, firmas en dos columnas y anexos.
- **Cartas al trabajador**: membrete de la empresa (`[DENOMINACIÓN SOCIAL]`, CIF), destinatario, lugar y
  fecha, asunto, cuerpo con los hechos concretos y fechas, decisión, efectos y fecha de efectos,
  firma de la empresa y **recibí** del trabajador con fecha (o constancia de la negativa a firmar ante
  testigos). Copia a la representación legal cuando la norma o el convenio lo exijan.
- **Escritos procesales** (papeleta, demanda): encabezamiento en mayúsculas al órgano (apartado 3),
  comparecencia, hechos y fundamentos en ordinales (PRIMERO.-, SEGUNDO.-), súplica («SUPLICO» al
  juzgado; «SOLICITO» al servicio de conciliación), otrosíes, lugar, fecha y firma, y relación de
  documentos.
- Prosa forense con forma propia en cada fundamento: premisa normativa, doctrina, hecho y
  conclusión, con conectores variados. Dos fundamentos seguidos no repiten la misma secuencia.

## 3. Órganos y destinatarios

Comprueba la denominación con `buscar_articulo` antes de encabezar.

| Situación | Destinatario |
|---|---|
| Conciliación previa (despido, cantidad, extinción, sanciones…) | Servicio administrativo de mediación, arbitraje y conciliación de la comunidad autónoma del lugar de prestación de servicios o del domicilio del demandado (art. 63 LRJS). El nombre cambia en cada comunidad: búscalo en internet en la sede oficial de la comunidad o pregúntalo al abogado; si no se sabe, encabeza «AL SERVICIO DE MEDIACIÓN, ARBITRAJE Y CONCILIACIÓN DE [COMUNIDAD/PROVINCIA]» y avísalo |
| Demanda en primera instancia | Tribunal de Instancia de [sede], Sección de lo Social (arts. 84 y ss. de la Ley Orgánica del Poder Judicial, tras la LO 1/2025). La competencia territorial, con el art. 10 LRJS: lugar de prestación de servicios o domicilio del demandado, a elección del demandante |
| Recurso de suplicación | Sala de lo Social del Tribunal Superior de Justicia (se anuncia ante la Sección que dictó la sentencia) |
| Actas y requerimientos de la Inspección | Inspección Provincial de Trabajo y Seguridad Social que levantó el acta, o el órgano que indique el acta para las alegaciones |
| Comunicaciones de ERTE y despido colectivo | Autoridad laboral competente (la que corresponda por el ámbito de los centros afectados): compruébala en el propio procedimiento del RD 1483/2012 |

En la oficina judicial, el funcionario que da fe es el **Letrado o Letrada de la Administración de
Justicia**.

## 4. Cómo se cita

- Artículos: con el texto vigente que devuelve `buscar_articulo` y su norma nombrada de forma que
  `verificar_escrito` la reconozca: «artículo 55 del Estatuto de los Trabajadores», «artículo 103 de
  la Ley Reguladora de la Jurisdicción Social», «artículo 267 de la Ley General de la Seguridad
  Social», «artículo 7 de la Ley 10/2021, de 9 de julio, de trabajo a distancia», «artículo 11 del Real
  Decreto 1382/1985», «artículo 8 del Real Decreto Legislativo 5/2000», «artículo 10 de la Ley 2/2023,
  de 20 de febrero», «artículo 12 de la Ley 20/2007, de 11 de julio, del Estatuto del trabajo
  autónomo».
- **Pon la fecha de la ley en cada mención** de las leyes con número repetido (apartado 2 de las
  anclas).
- Apartados con letra: «la letra c) del artículo 52 del Estatuto de los Trabajadores» o «artículo 52
  del Estatuto de los Trabajadores, letra c)». Con «52.c)» pegado, el verificador no enlaza la norma y
  compara con la última que se nombró. Artículos «bis»: «apartado 1 del artículo 47 bis del Estatuto
  de los Trabajadores».
- Cada artículo con su norma: no escribas «(artículo 56.1)» suelto ni «de la misma ley». En una
  enumeración, nombra la norma con cada artículo o cítalos por separado.
- Convenio colectivo: «artículo 32 del Convenio Colectivo de [denominación oficial] (código [14
  dígitos], publicado en [boletín y fecha])», con el texto que devuelva `leer_convenio`.
- Si `verificar_escrito` marca un artículo como no localizado, compruébalo con `buscar_articulo` y el
  valor de `ley` de las anclas: si lo devuelve, el aviso se debe a cómo está nombrada la norma y hay
  que corregir el nombre.
- Jurisprudencia (solo en escritos procesales, notas e informes, nunca en cartas ni contratos):
  párrafo literal entre comillas, seguido de órgano, fecha, número y ECLI tal como los devolvió
  `leer_sentencias`. Cita fundamentos jurídicos (doctrina), nunca el relato de hechos ni los datos de
  las partes de aquel pleito. Comprueba que el párrafo es razonamiento de la Sala.
- Con `parrafos=3`, `leer_sentencias` devuelve a menudo alegaciones de parte o el relato procesal. Si
  no ves el razonamiento de la Sala, repite con `terminos` que apunten a la decisión («la sala
  considera», «debemos», «procede estimar», más la cuestión) antes de buscar otra sentencia.
- No escribas «dicha ley», «la misma ley», «el mismo artículo» ni «en su artículo»: el verificador
  atribuye esos artículos a otra norma. Repite el nombre de la norma. Y no pongas en los anexos de
  fuentes listas de números de artículo de varias normas: cita cada artículo en el texto con su norma.
- La jurisprudencia se atribuye a Jurisprudenciator o a «la base oficial de jurisprudencia».
- Ningún documento contiene un ECLI, un artículo, un plazo o un importe legal que no se haya obtenido
  en esta conversación con una herramienta de Jurisprudenciator o, cuando Jurisprudenciator no lo
  tenga, de una fuente de internet citada con su enlace (punto 3 de la puerta).

## 5. Datos del trabajador y de la empresa

- Marcadores para lo que no se ha facilitado: `[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[DOMICILIO]`,
  `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[CÓDIGO DE CUENTA DE COTIZACIÓN]`, `[CATEGORÍA/GRUPO PROFESIONAL]`,
  `[FECHA DE ANTIGÜEDAD]`, `[SALARIO BRUTO ANUAL]`, `[CENTRO DE TRABAJO]`. Nunca inventes un dato.
- La empresa se identifica con `buscar_empresa_mercantil` (denominación exacta, CIF, domicilio,
  administradores). Si está en disolución o concurso, dilo y valora citar al FOGASA y a la
  administración concursal.
- En las consultas a Jurisprudenciator busca por la cuestión jurídica, nunca por el nombre o el DNI
  del trabajador.

## 6. Plazos

- Calcula cada plazo con el precepto que devuelva `buscar_articulo`. Los que más se usan:
  - despido y extinción del contrato impugnable por esa vía, **20 días hábiles de caducidad** (art. 59.3
    del Estatuto de los Trabajadores y art. 103 de la Ley Reguladora de la Jurisdicción Social),
    suspendidos por la papeleta de conciliación (art. 65 de esa ley);
  - sanciones, 20 días hábiles (art. 114 de la Ley Reguladora de la Jurisdicción Social);
  - movilidad geográfica y modificación sustancial, 20 días hábiles (art. 138 de esa ley);
  - reclamaciones de cantidad y acciones sin plazo especial, **un año de prescripción** (art. 59.1 y
    59.2 del Estatuto de los Trabajadores);
  - prescripción de faltas del trabajador (art. 60.2 del Estatuto de los Trabajadores).
- Días hábiles en el orden social: excluye sábados, domingos y festivos (del lugar del órgano).
  Agosto y del 24 de diciembre al 6 de enero son inhábiles **salvo** en las modalidades que enumera el
  apartado 4 del artículo 43 de la Ley Reguladora de la Jurisdicción Social (despido, extinción de los
  artículos 50, 51 y 52 del Estatuto de los Trabajadores, movilidad geográfica, modificación
  sustancial, ERTE, conciliación de la vida familiar, vacaciones, tutela de derechos fundamentales…):
  en esas, esos días cuentan. Léelo con `buscar_articulo` en cada caso.
- Festivos para contar días hábiles: los nacionales y autonómicos salen de la resolución anual de
  fiestas laborales (BOE) y del boletín de la comunidad; los locales, del boletín de la provincia o de la
  web del ayuntamiento de la sede del órgano. Búscalos en internet y cita la fuente.
- Indica siempre la fecha inicial, el precepto y la fecha final calculada. Si no consta la fecha
  inicial (efectos del despido, notificación de la sanción), pídela; sin ella no se da un plazo.

## 7. Cálculos (salario, indemnización, finiquito)

- Salario del módulo: el **real** que percibía el trabajador en el momento del despido (nóminas de los
  últimos 12 meses, con prorrata de pagas extra y complementos salariales), no el mínimo del convenio,
  salvo que se reclame que el real era inferior al debido.
- Muestra el cálculo en una tabla: salario anual bruto, salario diario (anual / 365), antigüedad en
  años y fracción, días por año del artículo aplicado, tope y resultado. Si la antigüedad es anterior
  al 12/02/2012, aplica la disposición transitoria undécima del Estatuto de los Trabajadores con los
  dos tramos: `buscar_articulo` no devuelve las disposiciones transitorias ni las adicionales, así que
  léela en internet en el texto consolidado del BOE (o en la sentencia del Supremo que la transcribe) y
  cítala con su enlace.
- Finiquito: salario del mes en curso, vacaciones devengadas y no disfrutadas, parte proporcional de
  pagas extra no prorrateadas, otros devengos (convenio) e indemnización si procede. Indica que las
  retenciones de IRPF y cotizaciones las aplica la nómina de liquidación.
- Horas extraordinarias: el precio lo fija el convenio o el contrato y nunca puede ser inferior al valor
  de la hora ordinaria (artículo 35 del Estatuto de los Trabajadores); si el convenio no lo fija, calcúlalo
  con la hora ordinaria y dilo.
- Interés por mora: el 10 % del artículo 29.3 del Estatuto de los Trabajadores es el mínimo; comprueba si el
  convenio fija uno mayor y aplica el más favorable.
- Redondea a céntimos y deja visible cada operación para que el abogado la compruebe.

## 8. Cuándo es imprescindible la jurisprudencia

La puerta de cada skill se aplica siempre a `estado` y a los artículos (y al convenio, cuando la
tarea dependa de él): sin el texto vigente que devuelva Jurisprudenciator no se redacta nada.

- **Imprescindible** (si tras dos reformulaciones no hay ninguna resolución aplicable, se aplica el
  punto 3 de la puerta: búsqueda en internet y localización en Jurisprudenciator; si tampoco así
  aparece, la tarea se detiene): demandas, papeletas con fundamentación, informes de riesgo y toda decisión empresarial
  cuya validez discute la jurisprudencia (audiencia previa al despido disciplinario, suficiencia de la
  carta, causas objetivas y su acreditación, fraude en la contratación temporal, pactos de no
  competencia y su compensación, falso autónomo, sucesión de plantilla, registro de jornada como
  prueba, vulneración de derechos fundamentales).
- **Se busca y se cita si existe**: contratos, pactos y protocolos que se sostienen en el texto de la
  norma. Si no hay doctrina, se redacta sobre el artículo y la nota lo dice.

## 9. Resumen para el abogado

Acompaña cada entrega con un resumen breve en el chat:

1. Qué se ha preparado, para quién y ante qué órgano.
2. Plazo y fecha límite, con su precepto.
3. Cálculos clave (indemnización, cantidades) y de dónde sale cada cifra.
4. Documentos que faltan y riesgos detectados.
5. Tabla de jurisprudencia citada: ECLI · órgano · fecha · qué sostiene.
6. Próximo paso recomendado.
