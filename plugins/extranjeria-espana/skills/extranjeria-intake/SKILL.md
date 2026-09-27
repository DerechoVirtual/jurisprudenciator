---
name: extranjeria-intake
description: >-
  Puerta de entrada del plugin de extranjería para la primera consulta de un cliente extranjero. Reúne
  en orden su situación (nacionalidad, fecha y forma de entrada, situación administrativa,
  antecedentes, familia en España, trabajo, estudios, expedientes o sanciones abiertos y
  notificaciones con su fecha), detecta urgencias (orden de expulsión, internamiento en CIE, plazo de
  recurso corriendo, autorización caducada o a punto de caducar), calcula cada plazo con su precepto y
  deriva a la skill del plugin que corresponde. Entrega la ficha del caso en Word. Úsala con «cliente
  nuevo de extranjería», «primera consulta», «está sin papeles», «le ha llegado una carta de
  extranjería», «qué puede hacer mi cliente». Para comparar vías con requisitos, riesgos y
  jurisprudencia usa informe-viabilidad-extranjeria.
---

# Primera consulta de extranjería: ficha del caso, urgencias y derivación

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Situación administrativa y ventana de renovación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, `articulo="47"` y `articulo="200"`, más el de renovación del título que tenga el cliente: `"64"`, `"71"`, `"80"`, `"86"`, `"95"` o `"132"`; `ley="LOEX"`, `articulo="52"` y `articulo="53"` para la infracción por estancia irregular o renovación tardía).
- **Expediente de expulsión en curso** → `buscar_articulo` (`ley="LOEX"`, artículos `"57"`, `"58"`, `"63"` y `"63 bis"`; `ley="BOE-A-2024-24099"`, artículos `"226"`, `"227"` y `"231"` si es ordinario, `"234"` y `"235"` si es preferente, y `"245"` para la ejecución).
- **Devolución o denegación de entrada en curso** → `buscar_articulo` (`ley="LOEX"`, artículos `"58"` y `"64"`; `ley="BOE-A-2024-24099"`, artículos `"15"` y `"23"`).
- **Detención o internamiento en CIE** → `buscar_articulo` (`ley="LOEX"`, `articulo="62"`; `ley="BOE-A-2024-24099"`, `articulo="234"` y `articulo="245"`; `ley="Real Decreto 162/2014"`, `articulo="1"`).
- **Plazo de recurso que está corriendo** → `buscar_articulo` (`ley="LPAC"`, artículos `"30"`, `"122"` y `"124"`; `ley="LJCA"`, artículos `"46"` y `"128"`).
- **Vía a la que se deriva** → `buscar_articulo` sobre el precepto ancla que indica la tabla de derivación, antes de anotar la vía en la ficha.
- **Riesgo sancionador de la estancia irregular** → `buscar_sentencias` (`consulta="expulsión estancia irregular multa circunstancias agravantes proporcionalidad"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`) + `leer_sentencias` (`parrafos=3`, `terminos="multa expulsión agravantes"`).
- **Qué inciso anuló exactamente el Tribunal Supremo** → `leer_boe` (`identificador="BOE-A-2026-19632"`): devuelve el fallo de la sentencia de 8 de julio de 2026 y el auto de rectificación de 1 de septiembre de 2026 con el texto literal de cada inciso anulado. Úsalo siempre que `buscar_articulo` traiga una nota de nulidad de un «inciso destacado»: el conector no conserva el resaltado y, sin el fallo, no se sabe qué palabras se anularon.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Las letras y los apartados de un artículo «bis» se escriben delante: «letra a) del artículo 53.1 de la Ley Orgánica 4/2000», «apartado 2 del artículo 63 bis de la Ley Orgánica 4/2000», nunca «artículo 53.1.a» ni «63 bis.2»: con la letra pegada al número, `verificar_escrito` no enlaza la norma que sigue y comprueba el artículo en la norma citada antes (da por buena una cita equivocada o por inexistente una correcta).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Primera entrevista con un cliente extranjero, antes de saber qué autorización, recurso o defensa necesita.
- El cliente trae una notificación de extranjería y hay que saber qué es, qué plazo corre y quién la lleva.
- El despacho recibe un caso de otro compañero y hay que ordenarlo antes de trabajarlo.
- No la uses cuando la vía ya está decidida: ve directamente a la skill de esa vía. Si ya sabes que hay varias vías posibles y hay que elegir, usa `informe-viabilidad-extranjeria`. Si solo falta la lista de documentos, usa `documentacion-expediente`.
- Si en las preguntas de urgencia aparece una detención, un CIE o una expulsión con ejecución inminente, deriva en ese mismo momento (apartado «Semáforo de urgencias») y completa la ficha después.

## Datos que hay que reunir antes de redactar

No redactes la ficha al primer mensaje. Pregunta en este orden y, si falta un dato imprescindible (marcado con ★), pregúntalo antes de seguir.

**Paso 1. Tres preguntas de urgencia (siempre primero).**

1. ★ ¿Está ahora detenido, en un Centro de Internamiento de Extranjeros, en una sala de inadmisión de frontera o citado por la policía?
2. ★ ¿Ha recibido alguna notificación de extranjería (acuerdo de incoación, propuesta, resolución de expulsión, devolución, denegación, extinción, requerimiento de documentos)? Pide copia íntegra y la **fecha exacta de notificación** (y la hora, si es un acuerdo de expulsión preferente).
3. ★ ¿Tiene fecha de vuelo, de conducción a frontera o de cita policial?

Si alguna respuesta es afirmativa, aplica el semáforo antes de seguir preguntando.

**Paso 2. Identificación.** ★ Nacionalidad o nacionalidades y ★ fecha de nacimiento (si es menor o lo alega, deriva a `menores-extranjeros`); pasaporte en vigor o caducado; NIE si lo tiene. Usa marcadores (`[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`) para lo que no se facilite.

**Paso 3. Entrada.** ★ Fecha de entrada en España (`[FECHA DE ENTRADA EN ESPAÑA]`) y ★ forma: con visado (tipo), sin visado por estar exento, por puesto no habilitado o por vía marítima; sello de entrada o registro en el sistema de entrada y salida; entradas y salidas posteriores.

**Paso 4. Situación administrativa actual.**
- ★ ¿Tiene o ha tenido autorización? Tipo, fechas de concesión y caducidad, tarjeta de identidad de extranjero.
- ★ ¿Tiene alguna solicitud en trámite? Tipo, fecha de presentación y órgano. Pregunta expresamente si presentó solicitud de protección internacional, de arraigo o por la regularización extraordinaria del Real Decreto 316/2026.
- Empadronamiento: desde cuándo y en qué municipios; otros documentos que prueben la permanencia.

**Paso 5. Antecedentes.** ★ Antecedentes penales en España y en los países de residencia de los últimos cinco años; causas penales abiertas; detenciones o antecedentes policiales; sentencias con sustitución de la pena por expulsión; si hay antecedentes, fechas de extinción de la pena (para valorar cancelación).

**Paso 6. Familia en España.** Cónyuge o pareja (registrada o no), hijos, padres; **nacionalidad y situación de cada uno** (española, de otro Estado de la Unión, extranjero residente, irregular); menores a cargo escolarizados; personas dependientes a cargo.

**Paso 7. Trabajo y medios.** Oferta o contrato firmado (jornada y salario), trabajo actual sin autorización, alta en Seguridad Social, actividad por cuenta propia, medios económicos propios o familiares.

**Paso 8. Estudios.** Matrícula o formación en curso (tipo y centro), estancia por estudios anterior y su fecha de extinción.

**Paso 9. Expedientes, sanciones y bloqueos.** Expulsión o devolución anterior y su prohibición de entrada; multas de extranjería; alertas en el espacio Schengen; compromiso de no retorno por retorno voluntario.

**Paso 10. Circunstancias de protección.** Víctima de violencia de género o sexual, indicios de trata, delitos de odio o explotación laboral, enfermedad grave sobrevenida, temor de persecución o daño grave en su país, apatridia, ascendencia española (padre, madre o abuelos españoles de origen).

**Paso 11. Objetivo del cliente.** Qué quiere conseguir (trabajar, traer a su familia, no ser expulsado, nacionalidad) y en qué plazo.

Datos opcionales: historial laboral en España, cursos de integración, informes sociales, idiomas. Si el cliente no sabe una fecha, anótala como `[FECHA PENDIENTE]` y no calcules el plazo que depende de ella.

## Requisitos y comprobaciones

### Semáforo de urgencias

Lee con `buscar_articulo` el precepto de cada fila antes de escribir el plazo en la ficha. Si el texto devuelto trae una nota «Téngase en cuenta que se declara la nulidad…» (la Sentencia del Tribunal Supremo de 8 de julio de 2026 anuló incisos o apartados de los arts. 94.1.f, 97.4, 98.1, 101.1, 159.1, 160.1, 160.2, 166.1, 196.b y 197.2 del Reglamento), lee el fallo con `leer_boe` (`identificador="BOE-A-2026-19632"`) para saber qué palabras exactas se anularon; lo anulado no se aplica y lo que el fallo declara conforme (por ejemplo, el plazo de seis meses del art. 159.1) sigue vigente: anótalo en la ficha. Si el fallo remite a un fundamento jurídico para interpretar un precepto, el conector no lo devuelve: anótalo como precepto no disponible.

| Nivel | Situación | Precepto que se lee | Qué hacer y a qué skill |
|---|---|---|---|
| Rojo (horas) | Detenido para expulsión o devolución; ingresado en CIE | LOEX 62; Reglamento 234.5 y 245.3; LOEX 58.6 | `internamiento-cie` y, si hay orden de expulsión ejecutable, `recurso-contencioso-extranjeria` (cautelarísima) |
| Rojo (horas) | Resolución de expulsión en procedimiento preferente notificada | LOEX 63.7; Reglamento 235 | `recurso-contencioso-extranjeria` con medida cautelarísima; `expulsion-procedimiento-sancionador` para el fondo |
| Rojo (horas) | Acuerdo de incoación de expulsión preferente | LOEX 63.4; Reglamento 234.1 | `expulsion-procedimiento-sancionador` (alegaciones en el plazo por horas que devuelva el artículo) |
| Rojo (horas) | Denegación de entrada o devolución en frontera | Reglamento 15 y 23; LOEX 58.3 | `denegacion-entrada-devolucion`; si pide protección internacional, `proteccion-internacional-apatridia` |
| Naranja (días) | Acuerdo de incoación en procedimiento ordinario o propuesta de resolución | Reglamento 227 y 231 | `expulsion-procedimiento-sancionador` |
| Naranja (días) | Resolución de expulsión ordinaria con plazo de cumplimiento voluntario | LOEX 63 bis.2; Reglamento 245.2 | `recurso-contencioso-extranjeria` o `recurso-administrativo-extranjeria` |
| Naranja (días) | Resolución denegatoria, de archivo o de extinción notificada | LPAC 122 y 124; LJCA 46; Reglamento 202.4 | `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria` |
| Naranja (días) | Requerimiento de subsanación o trámite de audiencia | Reglamento 130.3, 97.6 o 202.1; LPAC 68 y 82 | `recurso-administrativo-extranjeria` |
| Amarillo (semanas) | Autorización que caduca en menos de dos meses o caducada hace menos de tres | Artículo de renovación del título; Reglamento 200.1; LOEX 52.b y 53.1.a | `renovacion-modificacion-extincion` |
| Amarillo (semanas) | Concesión pendiente de alta en Seguridad Social o de pedir la tarjeta | Reglamento 130.5, 130.6 y 209 | `documentacion-expediente` |

Antes de fijar el nivel de un expediente de expulsión, comprueba en la copia íntegra del acuerdo por qué procedimiento se tramita (ordinario o preferente) y el plazo que indica. Si el cliente no lo sabe o la copia no está, trátalo como preferente (plazo de 48 horas, urgencia roja) hasta verlo, y anótalo.

Comprueba además, siempre que haya expulsión o devolución en curso, si concurre una causa que suspenda o impida su ejecución y anótala: solicitud de protección internacional (LOEX 64.5; Reglamento 245.7 y 23.6), embarazo con riesgo o enfermedad (LOEX 57.6; Reglamento 245.7), solicitud de residencia por circunstancias excepcionales del art. 31.3 LOEX presentada antes (LOEX 63.6: solo suspende el procedimiento preferente por las letras a) y b) del art. 53.1; léelo con el art. 31 LOEX), supuestos del art. 57.5 LOEX (residentes de larga duración, nacidos en España con residencia legal, pensionistas por incapacidad o desempleo y sus familiares) y menores escolarizados a cargo (Reglamento 245.2).

Si el cliente tiene una vía de autorización posible, anota que presentarla no paraliza por sí sola el expediente ordinario y que la expulsión, si se acuerda, archiva cualquier procedimiento de autorización en curso (LOEX 57.4; Reglamento 200.3): la solicitud se presenta cuanto antes y su justificante se aporta en las alegaciones.

### Cálculo de plazos

- Fecha inicial: la de notificación que conste en el acuse, la comparecencia electrónica o la diligencia. Sin fecha de notificación no se da plazo: pídela.
- Notificación electrónica: comprueba con `buscar_articulo` (`ley="LPAC"`, `articulo="43"`) cuándo se entiende practicada o rechazada.
- Vía administrativa: meses de fecha a fecha y días hábiles según el art. 30 LPAC; último día inhábil, al siguiente hábil (art. 30.5).
- Vía judicial: art. 46 LJCA; agosto no corre salvo derechos fundamentales (art. 128.2 LJCA); cómputo según art. 185 LOPJ (`ley="LOPJ"`, `articulo="185"`).
- Plazos por horas (alegaciones en el procedimiento preferente): cuenta desde la hora de notificación y trátalos como urgencia roja.
- Escribe en la ficha, para cada plazo: acto, fecha inicial, precepto leído, fecha final calculada y quién lo vigila.

### Bloqueos que hay que detectar en la primera consulta

Lee el precepto y anota el bloqueo en la ficha; no lo resuelvas aquí.

- Solicitante de protección internacional con procedimiento no firme: no puede pedir arraigo y ese tiempo no computa (Reglamento 126.a y 126.b).
- Titular de otra autorización o interesado en otro procedimiento de autorización en curso (Reglamento 126.h).
- Prohibición de entrada vigente, alerta de rechazable o expulsión dictada (Reglamento 11 y 126.e; LOEX 57.4 y 58). Una resolución de devolución no ejecutada puede revocarse si procede una autorización por circunstancias excepcionales (Reglamento 23.8).
- Compromiso de no retorno por retorno voluntario (Reglamento 126.f y 91).
- Antecedentes penales: comprueba si están cancelados o son cancelables con `buscar_articulo` (`ley="CP"`, `articulo="136"`) y si hubo sustitución de la pena por expulsión (`ley="CP"`, `articulo="89"`).
- Estancia irregular con autorización caducada más de tres meses sin renovación pedida (LOEX 53.1.a) frente a retraso de hasta tres meses (LOEX 52.b).

### Preceptos que el conector no devuelve

`buscar_articulo` no devuelve disposiciones adicionales ni transitorias. Cuando el caso dependa de una de ellas, anótalo en la ficha, aplica la puerta y detén el análisis de ese punto explicando al abogado qué precepto falta:

- Disposiciones adicionales vigésima y vigesimoprimera del Reglamento (arraigo de solicitantes de protección internacional y arraigo extraordinario, añadidas por el Real Decreto 316/2026). `buscar_articulo` no las devuelve, pero `leer_boe` (`identificador="BOE-A-2026-8284"`) sí trae su articulado: la vigésima completa (su apartado 6 fija el plazo de solicitud hasta el 30/06/2026) y la vigesimoprimera hasta su apartado 5 (su plazo, también el 30/06/2026, figura en la exposición de motivos de ese Real Decreto). Léelas cuando el cliente diga que presentó una de esas solicitudes (requisitos, habilitación provisional para trabajar, archivo de la expulsión si se concede) y, si no la presentó, anota en la ficha que el plazo terminó el 30/06/2026. Lo que el conector no devuelva de la vigesimoprimera (desde su apartado 6) es precepto no disponible.
- Disposición transitoria quinta del Real Decreto 1155/2024 (arraigos del régimen anterior). Las transitorias primera y segunda sí salen en `leer_boe` (`identificador="BOE-A-2024-24099"`): léelas si la solicitud del cliente es anterior al 20/05/2025 (transitoria segunda) o si la autorización que hay que renovar o modificar se concedió con el Reglamento anterior (transitoria primera: conserva su validez por el tiempo concedido y la renovación que se pida ahora se rige por el Real Decreto 1155/2024).
- Disposición adicional primera de la LOEX y disposiciones adicionales del Reglamento sobre plazos, silencio y recursos: en la ficha anota solo lo que diga el pie de recursos de la resolución notificada.
- Disposición adicional octava de la Ley 20/2022: si el cliente es nieto o hijo de español de origen, deriva a `nacionalidad-otras-vias`, que aplica la puerta.

## Estrategia y jurisprudencia

- Orden de trabajo: urgencias, después plazos, después vías. No valores a fondo ninguna vía: la ficha solo identifica las candidatas y las deriva.
- Para cada vía candidata, lee el precepto ancla y anota en una línea qué hecho del cliente la hace plausible y qué dato falta para confirmarla.
- Si el cliente está en situación irregular, anota el riesgo sancionador. Busca el criterio vigente sobre la elección entre multa y expulsión con la consulta de la lista de arriba y, para su tribunal, `buscar_sentencias` (`consulta="orden de expulsión estancia irregular proporcionalidad arraigo"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `tipo_organo="TSJ"`, `provincia="[sede de la Sala del TSJ competente]"`). En `provincia` va la sede de la Sala que conoce de la provincia del cliente, no la provincia misma cuando no coinciden (por ejemplo, para Almería, «Granada»; ocurre en las comunidades con varias sedes de Sala, como Andalucía, Canarias o Castilla y León): si la respuesta dice «Sin resultados en [provincia]», repite con la sede antes de caer al Supremo. Anota en la ficha qué circunstancias agravantes o de arraigo ha valorado esa doctrina, sin citar ECLI si no has leído el párrafo.
- Si hay antecedentes penales o policiales, busca `consulta="antecedentes policiales antecedentes penales cancelados denegación autorización residencia"` con `base="TS"` y anota el criterio como riesgo, no como conclusión.

### Tabla de derivación

Lee el precepto ancla antes de anotar la derivación y también antes de descartar una vía en la ficha (por ejemplo, un arraigo descartado por falta de permanencia se descarta con el texto del art. 126.b leído). «Reglamento» es siempre `ley="BOE-A-2024-24099"`.

| Skill | Deriva cuando | Precepto ancla |
|---|---|---|
| `extranjeria-intake` | Primera consulta o caso sin ordenar (esta skill) | — |
| `informe-viabilidad-extranjeria` | Hay dos o más vías posibles o hay que elegir cuándo presentar | Los de cada vía candidata |
| `documentacion-expediente` | La vía está decidida y falta la lista de documentos o revisar el expediente | Reglamento 130 (o el del procedimiento), 197 |
| `arraigo-social` | Dos años de permanencia y familia residente o esfuerzo de integración | Reglamento 126 y 127.c |
| `arraigo-sociolaboral` | Dos años de permanencia y uno o varios contratos | Reglamento 126 y 127.b |
| `arraigo-socioformativo` | Dos años de permanencia y matrícula o compromiso de formación | Reglamento 126 y 127.d |
| `arraigo-familiar` | Padre, madre o tutor de menor de otro Estado de la Unión, del EEE o suizo, o apoyo a persona con discapacidad de esa nacionalidad | Reglamento 127.e |
| `arraigo-segunda-oportunidad` | Fue titular de residencia no excepcional en los dos años anteriores y no pudo renovar | Reglamento 127.a |
| `razones-humanitarias` | Víctima de los delitos del art. 128.2, enfermedad grave sobrevenida o peligro en el traslado | Reglamento 128 |
| `victimas-violencia-genero-sexual` | Víctima de violencia de género o sexual | LOEX 31 bis; Reglamento 133 y 137 |
| `victimas-trata` | Indicios de trata de seres humanos | LOEX 59 bis; Reglamento 150 y 152 |
| `residencia-no-lucrativa` | Quiere residir sin trabajar con medios propios | Reglamento 61 y 62 |
| `reagrupacion-familiar` | Residente que quiere traer a su familia | LOEX 16 y 17; Reglamento 66 y 67 |
| `trabajo-cuenta-ajena` | Oferta de empleo, contratación en origen o paso a residencia y trabajo | Reglamento 74 y 191 |
| `trabajo-cuenta-propia` | Proyecto de actividad por cuenta propia | Reglamento 84 |
| `familiares-de-espanoles` | Cónyuge, pareja, hijo, ascendiente, progenitor de menor español o cuidador de español dependiente | Reglamento 94 y 97 |
| `ciudadanos-ue-y-familiares` | Ciudadano de otro Estado de la Unión o su familiar | `ley="Real Decreto 240/2007"`, arts. 2, 2 bis, 7 y 8 |
| `estudiantes-y-busqueda-empleo` | Estancia por estudios, paso a trabajo o visado de búsqueda de empleo | Reglamento 52, 53, 43 y 190 |
| `movilidad-internacional-ley-14-2013` | Alta cualificación, inversión, emprendimiento, teletrabajo o trámites ante la Unidad de Grandes Empresas | `ley="BOE-A-2013-10074"`, arts. 61 y 62 |
| `larga-duracion` | Cinco años de residencia legal o supuestos especiales | Reglamento 176 y 183 |
| `renovacion-modificacion-extincion` | Renovar, modificar o defender una extinción | Reglamento 191, 199, 200 y 202 |
| `menores-extranjeros` | Menor acompañado, nacido en España, no acompañado, determinación de edad o paso a mayoría de edad | Reglamento 159, 160, 165 y 172; LOEX 35 |
| `nacionalidad-residencia` | Residencia legal y continuada con los años del art. 22 CC | `ley="CC"`, art. 22 |
| `nacionalidad-otras-vias` | Origen, opción, carta de naturaleza, memoria democrática | `ley="CC"`, arts. 17, 20 y 21 |
| `proteccion-internacional-apatridia` | Temor de persecución o daño grave, apatridia | `ley="Ley 12/2009"`, arts. 16 y 17; `ley="Real Decreto 865/2001"`, art. 1 |
| `expulsion-procedimiento-sancionador` | Expediente sancionador abierto o resolución de expulsión o multa | LOEX 53, 57, 63 y 63 bis |
| `internamiento-cie` | Detención para expulsión o devolución, CIE | LOEX 62; Reglamento 234.5 y 245.3 |
| `denegacion-entrada-devolucion` | Rechazo en frontera o devolución | Reglamento 15 y 23; LOEX 58.3 |
| `recurso-administrativo-extranjeria` | Reposición, alzada, silencio, subsanación o audiencia | LPAC 68, 82, 112 y 121 a 124 |
| `recurso-contencioso-extranjeria` | Demanda o cautelar ante el juez contencioso | LJCA 8.4, 46, 78 y 129 a 136 |
| `visados-denegacion` | Visado denegado por un consulado | Reglamento 28 |
| `prohibicion-entrada-antecedentes` | Prohibición de entrada vigente, alerta Schengen o antecedentes que bloquean | Reglamento 11; LOEX 58; `ley="CP"`, art. 136 |

Si un caso encaja en varias filas, anótalas todas por orden de urgencia y deriva primero a la que tenga plazo corriendo.

## Documento que se entrega

**Ficha del caso en Word** (formato de `references/formato-y-organos.md`). Nombre: `ficha-caso-extranjeria-<apellido-cliente>-<AAAAMMDD>.docx`. Es un documento interno del despacho: sin súplica ni firma, con este orden:

Cita las normas en el documento como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca: «artículo N del Real Decreto 1155/2024» (nunca «del Reglamento de extranjería» ni «del Reglamento aprobado por…»), «artículo N de la Ley Orgánica 4/2000» y «Ley 14/2013, de 27 de septiembre». En esta skill, «Reglamento» es solo una abreviatura de trabajo del Real Decreto 1155/2024. Las letras van delante del número («letra c) del artículo 94.1 del Real Decreto 1155/2024»), nunca pegadas («94.1.c»). Cada cita lleva su norma aunque se repita: un «artículo 127» suelto después de citar el Código Civil o la Ley Orgánica 4/2000 lo comprueba `verificar_escrito` en esa otra norma. No cites artículos «del Real Decreto 316/2026»: `verificar_escrito` identifica ese número con otra norma; cita el artículo modificado del Real Decreto 1155/2024 y di que su redacción es la del Real Decreto 316/2026.

1. **Cabecera**: «FICHA DEL CASO — EXTRANJERÍA», fecha de la consulta, abogado responsable, referencia interna.
2. **Alerta de urgencia** (solo si hay rojo o naranja): una línea por urgencia con nivel, acto, precepto y fecha u hora límite.
3. **Identificación**: con marcadores para lo que falte.
4. **Cronología migratoria**: tabla fecha · hecho · documento que lo prueba.
5. **Situación administrativa actual**: clasificación según el art. 47 del Reglamento y el precepto leído.
6. **Antecedentes, expedientes y bloqueos**: con el precepto de cada bloqueo.
7. **Vínculos**: familiares (con nacionalidad y situación de cada uno), laborales y formativos.
8. **Notificaciones y plazos**: tabla acto · órgano · fecha de notificación · recurso indicado en el pie · precepto · fecha final.
9. **Vías candidatas y derivación**: tabla skill · por qué · dato que falta · precepto ancla leído.
10. **Preceptos no disponibles**: disposiciones adicionales o transitorias de las que depende el caso.
11. **Datos y documentos pendientes**: preguntas abiertas y documentos que debe traer el cliente.
12. **Normativa consultada**: artículo, norma y «vigente desde» tal como los devolvió `buscar_articulo`.
13. **Próximo paso**: la primera actuación y su fecha.

Si en el entorno no se pueden crear archivos, entrega el texto completo con esos títulos y avisa de que hay que pasarlo a Word.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió antes de empezar.
- [ ] Las tres preguntas de urgencia se hicieron primero y el semáforo está aplicado.
- [ ] Cada precepto de la ficha se leyó con `buscar_articulo` en esta conversación y consta con su «vigente desde»; si el texto trae una nota de nulidad o de modificación, se ha tenido en cuenta.
- [ ] Cada plazo tiene fecha inicial, precepto y fecha final; ninguno se calculó sin fecha de notificación.
- [ ] Las disposiciones adicionales o transitorias de las que depende el caso figuran como «precepto no disponible» y no se han suplido con memoria.
- [ ] Ningún ECLI en la ficha que no se haya leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] Marcadores en todos los datos no facilitados; ningún dato inventado.
- [ ] `verificar_escrito` pasado sobre el texto de la ficha; cada aviso revisado uno a uno (un «no localizado» o una norma que no es la citada suele venir de una letra pegada al número o de un artículo sin su norma: corrige la forma de citar y vuelve a pasarlo).
- [ ] Resumen en el chat según el apartado 7 del formato: qué se ha preparado, urgencias y fechas límite con su precepto, documentos que faltan y riesgos, tabla de jurisprudencia citada (si la hay) y la skill a la que se deriva como próximo paso.
