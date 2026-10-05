---
name: arraigo-sociolaboral
description: >-
  Prepara la solicitud de autorización de residencia temporal por arraigo sociolaboral (arts. 125.1.b y 127.b
  del Reglamento aprobado por el Real Decreto 1155/2024) con memoria justificativa en Word y relación de
  documentos para la Oficina de Extranjería. Úsala cuando el abogado diga «arraigo sociolaboral», «arraigo
  laboral», «tiene un contrato de trabajo», «dos años en España y le quieren contratar» o «varios contratos a
  tiempo parcial». Comprueba permanencia, antecedentes, contrato con salario mínimo o de convenio y 20 horas
  semanales, y los requisitos del empleador (art. 74). Si no hay contrato pero sí familia residente o informe
  de integración, usa arraigo-social; si va a estudiar, arraigo-socioformativo; si tuvo residencia que no
  renovó, arraigo-segunda-oportunidad; si acredita seis meses de trabajo irregular ante la autoridad laboral o
  judicial, razones-humanitarias (art. 129.2).
---

# Arraigo sociolaboral

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Base legal y requisitos vigentes** → `buscar_articulo` (`ley="LOEX"`, `articulo="31"`) y `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"124"`, `"125"`, `"126"` y `"127"`).
- **Requisitos del empleador y del contrato** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"74"` y `"76"`).
- **Procedimiento, habilitación provisional, trabajo y prórroga** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"130"`, `"131"`, `"132"`, `"193"`, `"197"` y `"191"`).
- **Salario mínimo interprofesional vigente** → `buscar_boe` (`consulta="salario mínimo interprofesional"`, `desde` = 1 de enero del año en curso) y `buscar_articulo` (`ley=` identificador BOE del real decreto que devuelva) con el artículo `"1"` (cuantía mensual), el que fije el **mínimo en cómputo anual** (en el de 2026, el `"3"`) y, si hay empleo de hogar por horas, el que fije su **salario por hora** (en el de 2026, el `"4"`).
- **Salario de convenio de la categoría** → `buscar_convenio` (sector y provincia del puesto), `vigencia_convenio` y `leer_convenio` (`buscar_en="tablas salariales"` o el artículo de retribuciones). Ojo: `leer_convenio` lee la publicación original del convenio; si `vigencia_convenio` muestra «TABLA SALARIAL» inscritas después, la tabla vigente **no** está en ese texto (ver el paso 5 del cálculo).
- **Existencia y actividad del empleador societario** → `buscar_empresa_mercantil` (denominación de la empresa).
- **Doctrina sobre el contrato, el empleador, la permanencia y los antecedentes** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"` para TSJ y juzgados, `base="TS"` para el Supremo) + `leer_sentencias` (`parrafos=3`).
- **Antecedentes y antiguo solicitante de protección internacional** → `buscar_articulo` (`ley="CP"`, `articulo="136"`) si hay condenas; (`ley="Ley 12/2009"`, `articulo="29"`), (`ley="LPAC"`, artículos `"30"` y `"124"`) y (`ley="LJCA"`, artículos `"46"` y `"128"`) si pidió asilo.
- **Revisión del documento** → cada redactor del equipo pasa `verificar_escrito` solo sobre sus frases con normas, y el ensamblado rechaza cualquier ECLI o ROJ que ningún redactor leyera; `buscar_por_cita` se usa solo con un ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, convenio y artículo del que sale el salario...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

## Cuándo usarla

Si aún no está claro qué vía conviene al cliente, empieza por `extranjeria-intake` o `informe-viabilidad-extranjeria`; para revisar un expediente documental ya reunido, `documentacion-expediente`. Si la solicitud ya se presentó y hay requerimiento, denegación o archivo, esta skill no es la herramienta: `recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria`.

- Persona extranjera en España, sin autorización de estancia o residencia, con al menos dos años de permanencia continuada, que aporta **uno o varios contratos de trabajo firmados** que garantizan el salario mínimo interprofesional o el de convenio, en proporción a la jornada, y suman **al menos veinte horas semanales**.
- Varios contratos solo en dos casos (art. 127.b): trabajos de temporada con distintos empleadores concatenados, o trabajo parcial simultáneo para varios empleadores.
- Es el único arraigo que habilita a residir y trabajar **desde la admisión a trámite** (art. 130.5): si el cliente tiene contrato, esta vía suele ser preferible a la del arraigo social.

**Detector** (si encaja otra figura, dilo al abogado con el artículo leído y no redactes este arraigo; si el abogado pide algo para el cliente, entrega una nota breve en Word, `nota-viabilidad-arraigo-sociolaboral-<apellido-cliente>-<AAAAMMDD>.docx`, con el motivo, los artículos leídos y las alternativas):

| Situación del cliente | Figura que procede |
|---|---|
| No hay contrato, pero sí cónyuge, pareja registrada, padres o hijos extranjeros residentes con medios, o informe de integración | arraigo-social (art. 127.c) |
| Va a estudiar FP, bachillerato, certificado profesional o ESO de adultos | arraigo-socioformativo (art. 127.d) |
| Fue titular de residencia no excepcional en los dos últimos años y no la renovó | arraigo-segunda-oportunidad (art. 127.a) |
| Progenitor o tutor de menor de otro Estado de la UE, el EEE o Suiza | arraigo-familiar (art. 127.e) |
| Familiar de español | `familiares-de-espanoles` (arts. 93-99) |
| Trabajó en situación irregular al menos seis meses en los dos años anteriores y colabora con la autoridad laboral o judicial | `razones-humanitarias` (colaboración del art. 129.2): no exige los dos años de permanencia ni contrato |
| Menos de dos años en España pero oferta en ocupación de difícil cobertura | autorización inicial de residencia y trabajo por cuenta ajena (arts. 72-81), por otro cauce: `trabajo-cuenta-ajena` |
| Solicitante de protección internacional sin resolución firme, titular de estancia o con otro procedimiento de autorización en trámite | no puede pedir arraigo (art. 126.a y h) |
| Orden de expulsión vigente o prohibición de entrada | `expulsion-procedimiento-sancionador` (la expulsión archiva cualquier procedimiento de residencia, art. 244.3) |
| Enfermedad grave, víctima de delito o de violencia | `razones-humanitarias` (art. 128), `victimas-violencia-genero-sexual` o `victimas-trata` |

## Datos que hay que reunir antes de redactar

Saca estos datos de la documentación aportada (paso 2 de `redaccion-rapida`). Si falta algún imprescindible (★) que bloquee el escrito, pídelos todos a la vez en una única ronda de no más de cuatro preguntas; lo demás queda como `[PENDIENTE: dato]`:

1. ★ Nacionalidad, pasaporte en vigor y provincia de residencia efectiva (art. 193.2).
2. ★ Fecha de entrada y pruebas de permanencia de cada tramo de los dos años; salidas de España y su duración.
3. ★ Protección internacional: fecha de la solicitud, de la resolución y de su **notificación**, recursos interpuestos y, si hubo recurso judicial, diligencia de firmeza; autorizaciones previas y procedimientos en trámite.
4. ★ Antecedentes penales (España y países de residencia de los cinco años previos a la entrada): pena, firmeza, extinción y, si hubo suspensión, fechas del auto de suspensión y de la remisión definitiva; antecedentes policiales, expulsiones, prohibiciones de entrada, compromiso de no retorno.
5. ★ **Contrato o contratos**: empleador, tipo, fecha de inicio, duración, jornada semanal, categoría profesional, salario bruto, centro de trabajo y provincia. Pide el borrador o el contrato firmado.
6. ★ **Empleador**: persona física o jurídica, NIF, actividad, plantilla, si está al corriente con Hacienda y Seguridad Social, medios económicos (cuentas anuales, declaraciones de impuestos, saldo) y, si es persona física, número de personas a su cargo (art. 76.2).
7. ★ Titulación o capacitación del trabajador si la profesión la exige (art. 74.1.f).
8. Representación del abogado (art. 197.4).

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo; aplica las notas «Téngase en cuenta» sobre nulidad si aparecen.

**Generales (art. 126, acumulativos)**: estar en España sin ser solicitante de protección internacional (a); dos años de permanencia continuada, sin computar el tiempo como solicitante de protección internacional hasta la resolución firme (b); no ser amenaza para el orden público (c); carecer de antecedentes penales en España y en los países de residencia de los cinco años anteriores a la entrada (d, y art. 31.5 LOEX), comprobando con el art. 136 CP si las condenas están canceladas o deberían estarlo (si la pena se extinguió por remisión tras una suspensión, el plazo se retrotrae según su apartado 2: la duración de la pena corre desde el día siguiente al otorgamiento de la suspensión); no ser rechazable en Schengen (e); no estar en plazo de no retorno (f); tasa abonada, sin dar importe ni modelo: remite a la sede oficial (g); no ser titular de autorización de estancia o residencia ni interesado en otro procedimiento de concesión, prórroga, renovación o modificación de autorizaciones en trámite (h); si lo hay, adviértelo y valora con el abogado el desistimiento antes de presentar.

**Antiguo solicitante de protección internacional (letra b)**: cuenta solo la permanencia posterior a la firmeza de la denegación. Sin recurso, la resolución pone fin a la vía administrativa (art. 29.1 de la Ley 12/2009) y es inatacable cuando vence el plazo del contencioso: dos meses desde el día siguiente a la notificación (art. 46.1 LJCA), sin contar agosto (art. 128.2 LJCA). Toma como firmeza el día siguiente a ese vencimiento (lectura prudente) y da al abogado la primera fecha segura de presentación; con recurso judicial, la de la diligencia de firmeza de la sentencia. No sumes la permanencia anterior a la solicitud de asilo ni el trabajo realizado como solicitante. Las vías de las disposiciones adicionales vigésima y vigesimoprimera se cerraron el 30/06/2026.

**Específico (art. 127.b)**:

- **Contrato firmado por trabajador y empleador** (art. 130.1.b).
- **Salario**: al menos el SMI o el salario del convenio colectivo aplicable, el que corresponda, **en el momento de la solicitud y en proporción a la jornada**. Obtén el SMI con `buscar_boe` + `buscar_articulo` y el salario de la categoría con `buscar_convenio` + `leer_convenio`; compara con el salario del contrato y deja el cálculo en la memoria con su fuente.
- **Jornada**: suma semanal no inferior a veinte horas en cómputo global.
- **Varios contratos**: solo en los dos supuestos del art. 127.b.1.º y 2.º. Cada empleador debe cumplir el art. 74.
- **Empleador**: requisitos del art. 74 **salvo el 1.a)** (no se examina la situación nacional de empleo): condiciones ajustadas a la normativa y al convenio (c), al corriente de obligaciones tributarias y de Seguridad Social (d), medios suficientes para el proyecto y el salario (e, y art. 76; si es persona física, además los porcentajes del SMI del art. 76.2 según su unidad familiar), capacitación o cualificación del trabajador (f).
- **Duración**: el art. 74.1.b pide una actividad continuada durante la vigencia de la autorización, que en el arraigo es de un año (art. 125.2). Ajusta el contrato o la cadena de contratos a ese periodo o explica en la memoria por qué el supuesto de temporada del art. 127.b.1.º lo cubre.
- **Choque normativo que debes anticipar**: el art. 74.1.c, párrafo segundo, exige que en el contrato a tiempo parcial la retribución total alcance el SMI de jornada completa en cómputo anual, mientras que el art. 127.b admite el salario **en proporción a la jornada** desde veinte horas. Si el contrato es parcial:
  - calcula la retribución anual total de todos los contratos y compárala con el mínimo anual del real decreto del SMI; si no llega, di al abogado cuánto falta;
  - en la memoria, argumenta que el art. 127.b es la norma especial del arraigo sociolaboral y que su remisión al art. 74 (requisitos del empleador) no alcanza a la cuantía que el propio art. 127.b regula; busca doctrina antes de afirmarlo;
  - en el resumen, avisa del riesgo y ofrece la **vía segura**: reforzar los contratos (horas o salario) hasta superar ese mínimo anual antes de presentar, con un ejemplo de cifras que respete también el mínimo proporcional y el de convenio de cada contrato.
- **Empleo de hogar**: no hay convenio colectivo. Si trabaja por horas en régimen externo, la referencia es el salario mínimo por hora que fija el real decreto del SMI para las empleadas de hogar (incluye todos los conceptos); compáralo con las horas mensuales del contrato (horas semanales × 52 ÷ 12) y también con el SMI mensual prorrateado, y aplica el mayor. Si la empleadora es persona física, calcula además sus medios con el art. 76.2.

**Normas que el conector no devuelve por `buscar_articulo`:**

- Disposiciones adicionales vigésima y vigesimoprimera del Reglamento (arraigo de solicitantes de protección internacional y arraigo extraordinario, que solo podían pedirse hasta el 30/06/2026): léelas con `leer_boe` (`identificador="BOE-A-2026-8284"`, Real Decreto 316/2026). Si el cliente tiene una de esas solicitudes sin resolver, choca con el art. 126.h.
- Solicitudes de arraigo presentadas desde el 20/05/2025 hasta la entrada en vigor del Real Decreto 316/2026 (sus redacciones rigen desde el 16/04/2026) y aún en trámite: su régimen está en la disposición transitoria segunda de ese real decreto, que `leer_boe` no llega a devolver. Si el caso depende de ella, aplica la puerta y di al abogado qué precepto falta.

**Procedimiento y efectos**:

- Solicitud personal (o por representante acreditado, art. 197.4) ante la oficina de la provincia de residencia, sin visado, con pasaporte en vigor, contrato firmado y documentación del empleador (art. 130.1).
- Certificados de antecedentes de los países de residencia de los cinco años previos a la entrada, con las excepciones del art. 130.2; la oficina pide de oficio penados e informe policial; los antecedentes policiales exigen valoración individual (art. 130.2).
- Subsanación: plazo que fije la oficina, máximo quince días (art. 130.3).
- **Habilitación provisional** para residir y trabajar por cuenta ajena desde la admisión a trámite, que constará en la comunicación de inicio (art. 130.5). Redacta la cláusula de inicio del contrato condicionada a esa habilitación o a la concesión (art. 74.1.b), nunca con una fecha anterior.
- Concedida, su eficacia depende del **alta en la Seguridad Social en el plazo de un mes** desde la notificación (art. 130.5). TIE en un mes (art. 130.6). Duración de un año (art. 125.2) con autorización de trabajo por cuenta ajena o propia sin límites (art. 131).
- Prórroga: búsqueda activa de empleo e inscripción en el servicio público de empleo, salvo impedimentos justificados (art. 132.2.a); se pide en los dos meses anteriores o los tres posteriores al vencimiento (art. 132.3). Tras un año trabajando, valora la modificación del art. 191.3.
- Plazo máximo de resolución y silencio: en disposiciones adicionales que el conector no devuelve. No los afirmes; remite al BOE consolidado.

**Causas típicas de denegación y cómo rebatirlas:**

| Causa | Respuesta |
|---|---|
| Salario por debajo del mínimo | Cálculo en proporción a la jornada con SMI y tabla del convenio obtenidos del conector (art. 127.b) |
| Parcial que no llega al SMI anual completo | Especialidad del art. 127.b frente al art. 74.1.c; ver doctrina |
| Empleador sin solvencia o sin estar al corriente | Certificados de AEAT y TGSS, cuentas, saldos; para persona física, cálculo del art. 76.2 |
| Empresa sin actividad real | Datos registrales (`buscar_empresa_mercantil`), plantilla, facturación |
| Contrato de duración inferior a un año | Art. 74.1.b en relación con el 125.2; concatenación del art. 127.b.1.º |
| Más de un contrato fuera de los supuestos admitidos | Reordenar los contratos o reconducir a un solo empleador |
| Permanencia o antecedentes | Igual que en arraigo-social: prueba por tramos y art. 136 CP |

### Cálculo del salario exigible (déjalo por escrito en la memoria)

1. Obtén el SMI mensual vigente de su real decreto (`buscar_articulo`, `articulo="1"`) y la jornada a la que se refiere, que es la legal de la actividad, y el **mínimo en cómputo anual** del mismo real decreto (en el de 2026, su art. 3.1): úsalo para comparar salarios con distinto número de pagas y para el art. 74.1.c.
2. Obtén del convenio la retribución de la categoría del contrato y la jornada ordinaria del convenio (`leer_convenio` con `buscar_en="tablas salariales"` y `buscar_en="jornada"`); comprueba su vigencia con `vigencia_convenio`.
3. Prorratea cada referencia a las horas semanales del contrato: referencia × horas del contrato ÷ horas de la jornada completa correspondiente.
4. El salario del contrato debe igualar o superar el mayor de los dos resultados. Si hay varios contratos, haz el cálculo por contrato y suma las horas.
5. Si el convenio no fija tabla para la categoría o el conector no la devuelve (lo habitual cuando `vigencia_convenio` muestra tablas inscritas después del texto que lee `leer_convenio`, o cuando este devuelve la página del boletín en lugar del texto), reformula dos veces (`buscar_en` con la categoría y con «anexo» o «salario base»). Si sigue sin tabla, esta es la aplicación de la puerta a ese dato: díselo al abogado, pídele la publicación oficial de la tabla vigente (se aporta como documento) y, mientras tanto, deja en la memoria el marcador `[IMPORTE DE LA TABLA SALARIAL VIGENTE PARA LA CATEGORÍA]` sin afirmar que el contrato lo cumple, y advierte en el resumen de que no debe presentarse sin comprobarlo. Nunca uses como vigente una tabla de un año anterior. El cálculo con el SMI sí se completa.

## Estrategia y jurisprudencia

1. Construye el caso sobre el contrato: verifica primero que salario, jornada y convenio cuadran; un contrato defectuoso se corrige antes de presentar, no en la subsanación.
2. Si el empleador es una persona física (servicio doméstico, cuidados), calcula sus medios con el art. 76.2 y aporta la prueba con la solicitud.
3. Consultas en Jurisprudenciator (máximo dos reformulaciones):
   - `buscar_sentencias` (`consulta="arraigo sociolaboral"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="20/05/2025"`).
   - `consulta="arraigo contrato de trabajo solvencia del empleador medios económicos"`, `base="AN"`.
   - `consulta="arraigo contrato a tiempo parcial salario mínimo interprofesional jornada"`, `base="AN"`, y, para la analogía con la autorización inicial, `consulta="contratación a tiempo parcial retribución salario mínimo interprofesional jornada completa cómputo anual autorización residencia"`, `base="AN"`.
   - `consulta="arraigo contrato de trabajo duración un año"`, `base="AN"`.
   - Antecedentes: `consulta="arraigo antecedentes penales cancelados o cancelables artículo 136 Código Penal"`, `base="TS"`.
   - Permanencia: `consulta="arraigo permanencia continuada empadronamiento prueba indiciaria"`, `base="AN"`.
4. Buena parte de la doctrina sobre solvencia del empleador y contrato se dictó bajo el antiguo arraigo social con contrato (art. 124.2 del Real Decreto 557/2011). Úsala para requisitos equivalentes (solvencia, al corriente, condiciones de convenio) y dilo en el escrito; no la uses para la duración o la jornada, que han cambiado.
5. Transcribe solo párrafos de fundamentos leídos con `leer_sentencias`, nunca hechos ni datos de las partes de aquel pleito. Comprueba que ese párrafo es razonamiento de la Sala y no alegaciones de parte ni la transcripción de un precepto (en estas pruebas salieron ambas cosas con `parrafos=3`); si no lo es, afina `terminos` o elige otra resolución.

**Al citar una sentencia**, comprueba qué reglamento aplicó (Real Decreto 557/2011 o Real Decreto 1155/2024: fecha de la solicitud de aquel caso y artículos que cita) y dilo en el escrito. Si aplicó el anterior, cítala solo para requisitos que los arts. 126 y 127 vigentes mantienen iguales. Si la resolución anula o interpreta un precepto del Reglamento vigente, contrasta que la nota «Téngase en cuenta» de `buscar_articulo` lo refleja.

## Documento que se entrega

Un Word maquetado según `references/formato-y-organos.md`: **solicitud de autorización de residencia temporal por circunstancias excepcionales por arraigo sociolaboral con memoria justificativa**. Acompaña al impreso oficial vigente, que el abogado descarga de la sede.

Nombre: `solicitud-arraigo-sociolaboral-<apellido-cliente>-<AAAAMMDD>.docx`.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» (la primera vez, «, de 19 de noviembre, por el que se aprueba el Reglamento de la Ley Orgánica 4/2000») y la ley como «artículo 31.3 de la Ley Orgánica 4/2000», según el apartado 4 del formato: así `verificar_escrito` reconoce cada cita. Nunca «del Reglamento de Extranjería». Dos precauciones más, comprobadas con el verificador: las letras se citan «letra b) del artículo 127 del Real Decreto 1155/2024» o «letra c) del artículo 74.1 del Real Decreto 1155/2024» (con «artículo 127.b) del Real Decreto…» no enlaza la norma y atribuye el artículo a la última norma citada); y como la memoria mezcla el Reglamento con el real decreto del SMI, nombra la norma detrás de cada artículo («artículo 1 del Real Decreto 126/2026», no «(artículo 1)»). Los artículos del convenio, cítalos sin número o como «el convenio, en su cláusula de salarios»: el verificador los atribuiría a otra norma.

Estructura:

1. **Encabezamiento**: «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA] — [DELEGACIÓN / SUBDELEGACIÓN] DEL GOBIERNO» (art. 193.2).
2. **Comparecencia** con marcadores (`[NOMBRE Y APELLIDOS]`, `[PASAPORTE]`, `[NIE]`, `[DOMICILIO]`) y representación (art. 197.4).
3. **EXPONE — HECHOS**: PRIMERO.- Identidad y entrada (`[FECHA DE ENTRADA EN ESPAÑA]`). SEGUNDO.- Permanencia continuada por tramos. TERCERO.- Situación administrativa y ausencia de procedimientos en trámite. CUARTO.- Antecedentes. QUINTO.- Contrato o contratos: empleador, jornada, categoría, salario. SEXTO.- Empleador: actividad, solvencia, cumplimiento de obligaciones.
4. **FUNDAMENTOS DE DERECHO**: I. Marco legal (art. 31.3 LOEX; arts. 124 y 125.1.b). II. Procedimiento y competencia (arts. 130, 193.2, 197). III. Requisitos generales (art. 126). IV. Requisito específico (art. 127.b): tabla de cálculo del salario con SMI y convenio citados por su norma y artículo. V. Requisitos del empleador (arts. 74, salvo 1.a, y 76). VI. Doctrina con párrafo literal y ECLI. VII. Habilitación provisional y efectos (arts. 130.5 y 131).
5. **SOLICITA**: admisión a trámite con habilitación provisional para residir y trabajar (art. 130.5) y concesión por un año.
6. **OTROSÍ**: que en la comunicación de inicio conste la habilitación provisional; que se recaben de oficio los informes del art. 130.2.
7. Lugar, fecha y firma.
8. **RELACIÓN DE DOCUMENTOS** numerada: impreso oficial; justificante de la tasa; pasaporte completo; prueba de permanencia por tramos; certificados de antecedentes (con la legalización o apostilla y traducción que exija la hoja informativa de la oficina); contrato o contratos firmados; documentación del empleador (NIF, escrituras o alta, certificados de estar al corriente, prueba de medios); título o capacitación si procede; representación.

**Reparto para la redacción rápida:** 01 encabezamiento, comparecencia y hechos; 02 fundamentos procesales y requisitos generales del art. 126; 03 requisito específico del art. 127.b con la tabla de cálculo del salario (SMI y convenio, que el director deja calculada en `caso.md`); 04 requisitos del empleador (arts. 74 y 76) con su doctrina; 05 habilitación provisional y efectos, solicita, otrosí, firma y relación de documentos.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: LOEX 31; Reglamento 74, 76, 124, 125, 126, 127, 130, 131, 132, 193 y 197; fechas de vigencia y notas de nulidad revisadas.
- [ ] SMI (mensual, mínimo anual y, en empleo de hogar, por hora) obtenido de su real decreto y salario de convenio obtenido de su texto, con código de convenio; si la tabla vigente no la devuelve el conector, marcador y aviso de no presentar sin comprobarla; cálculo proporcional a la jornada incluido.
- [ ] Si hay contratos parciales: suma anual comparada con el mínimo anual del SMI (art. 74.1.c) y, si no llega, cifras de la vía segura en el resumen.
- [ ] Si pidió asilo, dos años contados desde la firmeza de la denegación; si hay condenas, cálculo del art. 136 CP (apartado 2 si hubo suspensión).
- [ ] Jornada total ≥ 20 h semanales y, si hay varios contratos, supuesto del art. 127.b.1.º o 2.º identificado.
- [ ] Detector pasado; si encaja la colaboración del art. 129.2 u otra figura, se ha dicho al abogado.
- [ ] Riesgos anticipados: contrato parcial (art. 74.1.c frente al 127.b) y duración del contrato.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; `verificar_escrito` pasado por cada redactor sobre sus frases con normas.
- [ ] Cada aviso de «posible disonancia de contenido» de `verificar_escrito` contrastado con el apartado exacto leído con `buscar_articulo` (el verificador compara con el título del artículo, p. ej. «Requisitos específicos» o «Procedimiento»): si el apartado dice lo que afirma el escrito, se mantiene la cita y se explica en el resumen; si no, se corrige.
- [ ] Marcadores para lo que falta; sin importes de tasa, códigos de modelo ni plazos de resolución no obtenidos del conector.
- [ ] Resumen para el abogado (apartado 7 del formato), con estas fechas y su precepto: cumplimiento de los dos años (art. 126.b), subsanación (art. 130.3), alta en la Seguridad Social y TIE en un mes desde la notificación (arts. 130.5 y 130.6).
