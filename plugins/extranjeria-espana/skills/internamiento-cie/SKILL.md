---
name: internamiento-cie
description: >-
  Defensa urgente del extranjero detenido para expulsión, devolución o denegación de entrada y del
  que ya está en un centro de internamiento de extranjeros (CIE): oposición a la solicitud de
  internamiento ante la Sección de Instrucción, recurso de reforma y apelación contra el auto,
  petición de cese, quejas al juez de control, habeas corpus y efectos de pedir protección
  internacional desde el CIE (LOEX arts. 58 y 60-64; Real Decreto 162/2014; LOPJ art. 88). Escritos
  urgentes en Word. Úsala con «está en el CIE», «le van a internar», «auto de internamiento»,
  «detenido para expulsarlo», «juez de control», «habeas corpus», «quiere pedir asilo en el CIE»,
  «se cumplen los 60 días». Para las alegaciones contra la expulsión usa
  expulsion-procedimiento-sancionador; para la prohibición de entrada,
  prohibicion-entrada-antecedentes.
---

# Internamiento en CIE y medidas cautelares

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Supuestos, garantías, derechos del interno y plazo máximo** → `buscar_articulo` (`ley="LOEX"`, artículos 58, 60, 61, 62, 62 bis, 62 ter, 62 quater, 62 quinquies, 62 sexies, 63, 63 bis y 64).
- **Internamiento en cada fase del expediente** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos 23, 223, 234, 235, 243, 245 y 246).
- **Régimen del centro, quejas y cese** → `buscar_articulo` (`ley="Real Decreto 162/2014"`, artículos 1, 2, 16, 19, 21, 23, 29, 31, 37, 38 y 57).
- **Órgano competente y recursos contra el auto** → `buscar_articulo` (`ley="LOPJ"`, artículos 82 y 88; `ley="LECrim"`, artículos 211, 212, 216 a 221 y 766).
- **Habeas corpus y libertad personal** → `buscar_articulo` (`ley="Ley Orgánica 6/1984"`, artículos 1 a 8; `ley="CE"`, artículo 17).
- **Derecho de la Unión y protección internacional** → `buscar_articulo` (`ley="Directiva 2008/115/CE"`, artículos 15, 16 y 17; `ley="Ley 12/2009"`, artículos 19, 21 y 25; `ley="Reglamento (UE) 2024/1348"`, artículos 3, 4, 10, 26, 27 y 79; `ley="Directiva (UE) 2024/1346"`, artículo 10) y `buscar_boe` para la adaptación española.
- **Historia clínica del interno** → `buscar_articulo` (`ley="Ley 41/2002"`, artículo 18).
- **Doctrina de la Audiencia Provincial y del Tribunal Constitucional** → `buscar_sentencias` (`consulta="internamiento extranjero proporcionalidad medidas menos gravosas domicilio"`, `base="AN"`, `jurisdiccion="PENAL"`, `tipo_resolucion="AUTO"`, `provincia` del juzgado) y (`consulta="internamiento extranjero libertad personal motivación"`, `base="TC"`) + `leer_sentencias` (`parrafos=3`).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Cuando el precepto lleve letra o «bis», escribe «el apartado 1 del artículo 62 bis de la Ley Orgánica 4/2000, en su letra f)» o «la letra f) del artículo 37.1 del Real Decreto 162/2014», y pon la norma en cada cita: con «62 bis.1» o «37.1.f)», o sin norma detrás, el verificador no la identifica o la atribuye a la norma citada antes. El verificador no reconoce las normas de la Unión (Directiva 2008/115/CE, Reglamento (UE) 2024/1348, Directiva (UE) 2024/1346): atribuye sus artículos a otra norma del escrito o los da por no localizados. Si el artículo se leyó con `buscar_articulo` en su norma, la cita es correcta y no se cambia; explícalo en el resumen.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar o el requisito que hay que comprobar), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

Elige el escrito según el momento:

| Situación | Escrito |
|---|---|
| Detenido; la policía va a pedir el internamiento o ya lo ha pedido | Oposición a la solicitud de internamiento (para la audiencia ante el juez) |
| Auto de internamiento notificado | Recurso de reforma y subsidiario de apelación, o apelación directa |
| Internado: han dejado de darse las condiciones, la expulsión no es posible, vence el plazo, enfermedad, indicios de minoría | Solicitud de cese del internamiento |
| Vulneración de derechos dentro del CIE (comunicaciones, salud, contenciones, trato) | Petición o queja al juez de control |
| Privación de libertad sin cobertura judicial (más de 72 horas sin ponerlo a disposición del juez, ingreso sin auto, permanencia pasado el plazo del auto) | Solicitud de habeas corpus |
| El interno quiere pedir protección internacional | Comprobación de efectos sobre expulsión e internamiento y petición de cese si procede |

No la uses para:

- Las alegaciones de fondo contra la expulsión o la devolución → `expulsion-procedimiento-sancionador` (puede ir en paralelo).
- La solicitud de protección internacional en sí → `proteccion-internacional-apatridia`.
- La situación del menor no acompañado y la determinación de la edad fuera del CIE → `menores-extranjeros`.
- El internamiento que ordena el juez penal para ejecutar la expulsión sustitutiva de la pena (art. 89 del Código Penal): se recurre en la ejecutoria penal. Esta skill solo sirve ahí para las quejas sobre el régimen del centro. El Real Decreto 162/2014 remite todavía al «artículo 89.6 del Código Penal»; lee el art. 89 vigente con `buscar_articulo` (`ley="CP"`) y cita el apartado que hoy regula ese internamiento.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. Trabaja con rapidez: la detención cautelar no puede durar más de 72 horas antes de la solicitud de internamiento (art. 61.1.d) LOEX) y el juez resuelve tras oír al interesado.

1. **Situación exacta**: detenido (fecha, hora y lugar de la detención), ya oído por el juez, o internado (CIE, fecha de ingreso, juzgado, número de procedimiento, fecha del auto y plazo que fija). Imprescindible.
2. **Fecha y hora de notificación del auto** (para reforma y apelación). Imprescindible si se recurre.
3. **Expediente base**: expulsión (modalidad, infracción imputada, fase: tramitación, resolución o ejecución), devolución, denegación de entrada, reconocimiento de una expulsión de otro Estado. Copia del expediente o de la solicitud policial. Imprescindible.
4. **Internamientos anteriores** en el mismo expediente, con fechas.
5. **Arraigo y alternativas**: domicilio acreditable, pasaporte o documento, familia en España, trabajo, personas que respondan, disposición a cumplir presentaciones.
6. **Vulnerabilidad**: indicios de minoría de edad, enfermedad grave, embarazo, discapacidad, víctima de trata, solicitante de protección internacional.
7. **Perspectiva de expulsión**: nacionalidad acreditada o no, si el país readmite, gestiones consulares, vuelos, intentos fallidos.
8. Para quejas: hechos, fechas, personas intervinientes, prueba (partes médicos, testigos, registros del centro).

Si falta un dato imprescindible, pregúntalo antes de redactar. Lo que no se tenga va con marcador (`[FECHA Y HORA DE LA DETENCIÓN]`, `[NÚMERO DE DILIGENCIAS]`, `[CIE DE ...]`).

## Requisitos y comprobaciones

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo. Si la respuesta trae una nota «Téngase en cuenta…» (nulidad declarada por el Tribunal Supremo, como la sentencia de julio de 2026 publicada en `BOE-A-2026-19632`, o una reforma), léela y aplícala: lo anulado no se aplica ni se cita como vigente. Los autos y sentencias anteriores al 20/05/2025 citan el Reglamento anterior (Real Decreto 557/2011): comprueba qué reglamento aplicó cada resolución y no traslades su numeración.

### 1. Presupuestos legales del internamiento

- **Supuestos que lo permiten**: expediente incoado por las infracciones que enumera el art. 62.1 LOEX en el que pueda proponerse la expulsión; ejecución de una expulsión no cumplida en 72 horas (art. 64.1 LOEX; art. 245.3 del Reglamento); devolución no ejecutable en 72 horas (art. 58.6 LOEX; art. 23.4 del Reglamento); denegación de entrada (art. 60.1 LOEX); expulsión dictada por otro Estado (art. 64.4 LOEX; art. 246.3 del Reglamento). Comprueba que el caso está en uno de ellos.
- **Exclusión en el procedimiento ordinario**: no cabe internamiento durante su tramitación ni durante el plazo de cumplimiento voluntario (art. 63 bis.3 LOEX; arts. 223.2 y 243.1 del Reglamento). Si la solicitud llega en esa fase, es el primer motivo.
- **Arraigo u otra autorización del art. 31.3 LOEX pedida antes del acuerdo de iniciación** (expedientes por las letras a) o b) del art. 53.1): la expulsión debe suspenderse hasta que se resuelva (art. 63.6 LOEX) y, si el preferente continúa, lo hace por el ordinario (art. 240.1 del Reglamento), donde no cabe internamiento. Pide el justificante con la fecha de registro: sin expulsión ejecutable no hay finalidad que asegurar (Directiva 2008/115/CE, art. 15.1 y 15.4).
- **Detención previa**: máximo 72 horas antes de la solicitud (art. 61.1.d) LOEX; art. 17.2 CE).
- **Auto motivado, audiencia del interesado y del Fiscal, proporcionalidad** (art. 62.1 LOEX): riesgo de incomparecencia por falta de domicilio o documentación, actuaciones para dificultar la expulsión, condenas, sanciones y procesos pendientes; en enfermedad grave, riesgo para la salud. La solicitud del instructor debe ser motivada (art. 234.5 del Reglamento; art. 23 del Real Decreto 162/2014).
- **Medidas menos gravosas**: art. 61.1 LOEX (presentaciones, residencia obligatoria, retirada del pasaporte, cualquier otra adecuada); art. 234.6 del Reglamento; Directiva 2008/115/CE, art. 15.1 (último recurso, riesgo de fuga, diligencia debida).
- **Duración**: la imprescindible, con el máximo del art. 62.2 LOEX; el juez puede fijar uno menor (art. 234.5 del Reglamento; art. 21.2 del Real Decreto 162/2014); no cabe un nuevo internamiento por las causas del mismo expediente (art. 62.2 LOEX; art. 245.3 del Reglamento). El art. 21.3 del Real Decreto 162/2014 solo admite nuevos ingresos por causas diferentes (el Tribunal Supremo anuló el inciso que permitía reingresar por las mismas): si la nueva solicitud se apoya en el mismo expediente, alega el art. 62.2 LOEX.
- **Menores**: prohibido su internamiento (art. 62.4 LOEX), salvo acompañar a sus padres en las condiciones del art. 62 bis.1.i). Si hay indicios de minoría, lee el art. 166 del Reglamento (determinación de la edad) con su nota de nulidad parcial y pide la libertad inmediata y la puesta a disposición del servicio de protección de menores.
- **Perspectiva razonable de expulsión**: si ha desaparecido, el internamiento deja de estar justificado (Directiva 2008/115/CE, art. 15.4; art. 62.3 LOEX; causas de cese del art. 37 del Real Decreto 162/2014).

### 2. Órgano competente

- Autorizar y dejar sin efecto el internamiento: juez de instrucción del lugar de la detención (art. 62.6 LOEX), hoy Sección de Instrucción o Sección Única del Tribunal de Instancia (art. 88.2 LOPJ). Control de la estancia, peticiones y quejas: el del lugar donde está el centro (art. 62.6 LOEX; art. 88.2 LOPJ).
- Encabeza con el órgano que conste en las actuaciones. Si el caso llega con denominaciones anteriores a la LO 1/2025 («Juzgado de Instrucción n.º»), usa la del Tribunal de Instancia y deja el número de procedimiento.

### 3. Recursos contra el auto

- El art. 62 LOEX no regula los recursos: se aplica la LECrim. Lee los arts. 211 (reforma: plazo), 212 y 766 (apelación: plazo y tramitación), 216 a 221 (clases, ante quién se interponen, firma de letrado) y el art. 82.1.2.º LOPJ (la Audiencia Provincial conoce de la apelación).
- Busca en la Audiencia Provincial de la provincia qué cauce aplica (reforma previa, apelación directa o ambas) antes de elegir: `consulta="auto internamiento extranjero recurso de reforma apelación"`, `base="AN"`, `jurisdiccion="PENAL"`, `tipo_resolucion="AUTO"`, `provincia`, `fecha_desde="01/01/2020"`. Si no encuentras criterio, interpón reforma y subsidiaria apelación dentro del plazo más corto.
- Calcula el plazo desde la notificación del auto con el precepto leído y da la fecha final. El recurso no suspende el internamiento: pide la libertad o la medida alternativa en el propio escrito.

### 4. Peticiones, quejas y cese

- Peticiones y quejas al juez de control: art. 62.6 LOEX («sin ulterior recurso»), art. 62 quater LOEX, arts. 2.3, 16.2.n) y 19 del Real Decreto 162/2014 (presentación en el registro del centro con copia sellada). Como no hay recurso, incluye en el primer escrito todos los hechos y toda la prueba.
- Salud: arts. 14 (servicio sanitario, asistencia especializada y hospitalización) y 16.2.b) y e) del Real Decreto 162/2014; acceso a la historia clínica, art. 18 de la Ley 41/2002; si la enfermedad hace incompatible el internamiento, pide reconocimiento forense y traslado al juez que lo autorizó (art. 62.3 LOEX; art. 37.1.f) del Real Decreto 162/2014).
- Comunicación reservada con el abogado: art. 62 bis.1.f) LOEX y arts. 15.4 (dependencias que aseguren la confidencialidad), 16.2.h) y 41.1 del Real Decreto 162/2014.
- Jurisprudencia en las quejas: las resoluciones de los juzgados de control apenas se publican. Busca con `base="AN"`, `jurisdiccion="PENAL"`, `tipo_resolucion="AUTO"` y sin `provincia` (por ejemplo, «centro de internamiento de extranjeros asistencia sanitaria interno»). En una queja la jurisprudencia no es imprescindible: si tras dos reformulaciones no aparece nada aplicable, redacta con los preceptos leídos y dilo en el resumen; la puerta solo detiene la tarea si falta un precepto que haya que citar.
- Contenciones y separación: art. 62 quinquies LOEX y art. 57 del Real Decreto 162/2014 (el juez debe decidir su mantenimiento o revocación). Pide la revocación y la remisión de la resolución motivada del director.
- Derechos del interno que suelen vulnerarse: art. 62 bis LOEX y art. 16 del Real Decreto 162/2014 (información, asistencia sanitaria, abogado con comunicación reservada, intérprete, comunicaciones, contacto con organizaciones). Algunas letras tienen incisos anulados por el Tribunal Supremo: el conector lo señala en la nota del artículo; no cites el inciso anulado.
- Cese: art. 62.3 LOEX (libertad inmediata cuando dejan de cumplirse las condiciones; el juez de oficio o a instancia de parte) y art. 37 del Real Decreto 162/2014. Reingreso tras un intento fallido: art. 38.

### 5. Habeas corpus

- Supuestos de detención ilegal: art. 1 de la Ley Orgánica 6/1984 (sin supuesto legal o sin formalidades, internamiento ilícito, plazo superado, derechos no respetados). Competencia: art. 2 y art. 88.1.d) LOPJ. Legitimación del abogado: art. 3. Forma sin abogado ni procurador: art. 4. Tramitación y plazo de resolución: arts. 6 a 8.
- Úsalo cuando la privación de libertad carece de cobertura judicial (72 horas superadas, ingreso sin auto, permanencia más allá del plazo del auto o del máximo legal). Contra un auto de internamiento vigente, el cauce es el recurso, no el habeas corpus.
- Busca en el Tribunal Constitucional la doctrina sobre la inadmisión de plano por razones de fondo (`consulta="habeas corpus inadmisión extranjero"`, `base="TC"`) y cítala en la solicitud.

### 6. Protección internacional desde el CIE

- La solicitud impide la expulsión o devolución hasta que se inadmita o resuelva (art. 19.1 de la Ley 12/2009; art. 64.5 LOEX; art. 245.7 del Reglamento). Derecho a entrevistarse con abogado en el CIE: art. 19.4 de la Ley 12/2009.
- Régimen aplicable según la fecha de formalización: lee el art. 79 del Reglamento (UE) 2024/1348 (fecha de aplicación) y, para las solicitudes anteriores a ella, los arts. 21 y 25.2 de la Ley 12/2009 (tramitación como en frontera, plazos y reexamen). Comprueba con `buscar_boe` (`consulta="protección internacional"`, `desde` = fecha de hace 12 meses en formato AAAA-MM-DD) si España ha adaptado su ley; si no aparece norma de adaptación, dilo al abogado.
- Si rige el Reglamento (UE) 2024/1348, lee sus arts. 3 (definición de solicitante), 4.2 (las autoridades de los centros de internamiento deben recibir solicitudes), 26 (cuándo se entiende formulada), 27 (plazos para comunicar y registrar) y 10 (derecho a permanecer): la petición hecha al personal del centro ya es una solicitud formulada, y la condición de solicitante nace de la formulación, aunque el art. 64.5 LOEX hable de «formalizar». Si el centro no le ha dado curso, pídeselo al juez de control dentro de la queja.
- Motivos que permiten mantener internado a un solicitante: art. 10 de la Directiva (UE) 2024/1346. Comprueba si está transpuesta con `buscar_boe`; si no lo está y el caso depende de ella, aplica la puerta y explica qué falta.
- Si el conector no permite determinar con seguridad qué norma rige la solicitud concreta, detén esa parte del trabajo y díselo al abogado; el resto de escritos pueden seguir.

## Estrategia y jurisprudencia

Ordena los motivos de más a menos fuerte:

1. **Falta de presupuesto legal**: supuesto no incluido en el art. 62.1, procedimiento ordinario o plazo voluntario, segundo internamiento en el mismo expediente, menor de edad, detención previa superior a 72 horas, expulsión que debe suspenderse (arraigo pedido antes de la iniciación, protección internacional formulada).
2. **Falta de motivación individual** de la solicitud o del auto (fórmulas genéricas, sin examen de alternativas).
3. **Desproporción**: domicilio, documento, familia y trabajo acreditados; ausencia de antecedentes; vulnerabilidad.
4. **Sin perspectiva razonable de expulsión**: país que no documenta o no readmite, intentos fallidos, internamientos anteriores sin resultado.
5. **Subsidiario**: medida alternativa concreta (presentaciones con periodicidad, domicilio designado, entrega del pasaporte) y, si se mantiene el internamiento, plazo inferior al máximo.

Consultas:

| Cuestión | `consulta` | Filtros |
|---|---|---|
| Proporcionalidad y alternativas | «internamiento extranjero proporcionalidad medidas menos gravosas domicilio» | `base="AN"`, `jurisdiccion="PENAL"`, `tipo_resolucion="AUTO"`, `provincia` |
| Motivación del auto | «auto internamiento extranjero motivación circunstancias personales» | igual |
| Imposibilidad de expulsión y cese | «libertad internamiento extranjero imposibilidad de expulsión» | igual, con `fecha_desde="01/01/2018"` |
| Libertad personal | «internamiento extranjero libertad personal motivación» | `base="TC"` |
| Habeas corpus | «habeas corpus inadmisión extranjero» | `base="TC"` |
| Perspectiva razonable y límites del internamiento | «internamiento retorno perspectiva razonable de expulsión» | `base="TJUE"` |
| Control judicial de oficio de la legalidad | «internamiento control de oficio requisitos de legalidad del internamiento» | `base="TJUE"` |

- Los autos de la Audiencia tienen ECLI terminado en «A»: cópialo literal al leerlos y al citarlos.
- Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar. Prefiere la Audiencia Provincial que resolverá el recurso y resoluciones de los dos últimos años.
- Cita el párrafo de doctrina; nunca los hechos ni los datos personales del interno de aquel asunto.

## Documento que se entrega

Uno por situación, en Word, según `references/formato-y-organos.md` del plugin. Ante un órgano judicial la súplica es «SUPLICO».

1. **Escrito de oposición a la solicitud de internamiento** — `A LA SECCIÓN DE INSTRUCCIÓN DEL TRIBUNAL DE INSTANCIA DE [SEDE]`, diligencias `[NÚMERO]`. Comparecencia del letrado; HECHOS (detención, expediente, arraigo, vulnerabilidad); FUNDAMENTOS (presupuestos legales, proporcionalidad, alternativas, perspectiva de expulsión); SUPLICO: denegación del internamiento y, subsidiariamente, medida alternativa concreta y plazo inferior al máximo; OTROSÍ con documentos y, si procede, intérprete. Archivo: `oposicion-internamiento-<apellido>-<AAAAMMDD>.docx`.
2. **Recurso de reforma y subsidiario de apelación** (o apelación directa) — ante la misma Sección que dictó el auto, para ante la Audiencia Provincial. Identificación del auto y fecha de notificación; ALEGACIONES por motivos; SUPLICO: revocación del auto y libertad inmediata, subsidiariamente medida alternativa o reducción del plazo; particulares a testimoniar si se apela. Archivo: `recurso-reforma-apelacion-internamiento-<apellido>-<AAAAMMDD>.docx`.
3. **Solicitud de cese del internamiento** — al juez que lo autorizó. Hechos nuevos, causa de cese con su precepto, prueba; SUPLICO: cese y libertad inmediata. Archivo: `solicitud-cese-internamiento-<apellido>-<AAAAMMDD>.docx`.
4. **Petición o queja al juez de control** — `A LA SECCIÓN DE INSTRUCCIÓN DEL TRIBUNAL DE INSTANCIA DE [SEDE DEL CIE], CONTROL DEL CENTRO DE INTERNAMIENTO DE EXTRANJEROS DE [...]`. Hechos concretos con fecha, derecho afectado, prueba y medida que se pide (cese de la práctica, reconocimiento médico, comunicación, revocación de la contención). Archivo: `queja-juez-control-cie-<apellido>-<AAAAMMDD>.docx`.
5. **Solicitud de habeas corpus** — al juez competente del art. 2 de la Ley Orgánica 6/1984. Contenido del art. 4 (identidad, lugar y custodia, motivo concreto); SUPLICO: incoación, comparecencia y libertad o puesta a disposición judicial. Archivo: `habeas-corpus-<apellido>-<AAAAMMDD>.docx`.

Si el abogado necesita presentar dos escritos (por ejemplo, recurso y queja), entrégalos por separado.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» y el resto de normas como indica el apartado 4 de `references/formato-y-organos.md` (por ejemplo, «Ley Orgánica 4/2000», no «Reglamento de Extranjería»), para que `verificar_escrito` las reconozca.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió al empezar.
- [ ] Cada artículo citado se leyó con `buscar_articulo` en esta conversación; los incisos anulados que señala el conector no se citan.
- [ ] Órgano del encabezamiento comprobado con el art. 62.6 LOEX y el art. 88 LOPJ.
- [ ] Cada ECLI se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita` (autos con la «A» final).
- [ ] `verificar_escrito` pasado sobre el texto completo y sus avisos resueltos.
- [ ] Plazos con fecha y hora de inicio, precepto y fecha final: 72 horas de detención, plazo del recurso, días de internamiento consumidos y fecha en que se alcanza el máximo legal o el fijado en el auto.
- [ ] Régimen de protección internacional determinado con el art. 79 del Reglamento (UE) 2024/1348, o parada explicada al abogado.
- [ ] Marcadores en los datos que faltan; ningún dato inventado.
- [ ] Resumen para el abogado según el apartado 7 del formato: escrito y órgano, plazo y fecha u hora límite con su precepto, documentos que faltan y riesgos (ejecución inminente, vuelo programado, vencimiento del máximo), tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene) y próximo paso (presentación inmediata; alegaciones en el expediente con `expulsion-procedimiento-sancionador`).
