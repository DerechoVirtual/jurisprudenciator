---
name: licencia-cesion-propiedad-intelectual
description: >-
  Redacta la cesión o licencia de propiedad intelectual e industrial, o la cláusula de propiedad intelectual
  de otro contrato, con nota para el abogado: derechos de autor (alcance, modalidades, ámbito, duración y
  remuneración), programas de ordenador y desarrollos a medida, obra por encargo y de trabajadores, marcas
  (cesión, licencia e inscripción) y know-how. Distingue cesión exclusiva y no exclusiva y respeta los derechos
  morales irrenunciables. Úsala cuando el abogado diga «ceder los derechos», «licencia de uso», «licencia de
  software», «desarrollo a medida», «licencia de marca», «royalties» o «transferencia de know-how». Si solo se
  protege información, usa confidencialidad-nda; si es franquicia, agencia-distribucion-franquicia; si es un
  servicio con entrega de obra, prestacion-servicios o contrato-obra, y esta skill para la cláusula.
---

# Cesión y licencia de propiedad intelectual e industrial

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Objeto, autoría, derechos morales y de explotación** → `buscar_articulo` (`ley="TRLPI"`, artículos `"5"`, `"7"`, `"8"`, `"10"`, `"14"`, `"17"`, `"18"`, `"19"`, `"20"`, `"21"`, `"26"` y `"28"`).
- **Cesión inter vivos: alcance, forma, remuneración, exclusiva y trabajadores** → `buscar_articulo` (`ley="TRLPI"`, artículos `"43"`, `"45"`, `"46"`, `"47"`, `"48"`, `"48 bis"`, `"49"`, `"50"`, `"51"`, `"55"`, `"56"` y `"57"`).
- **Programas de ordenador** → `buscar_articulo` (`ley="TRLPI"`, artículos `"95"`, `"96"`, `"97"`, `"98"`, `"99"`, `"100"` y `"101"`); **indemnización por infracción** → (`ley="TRLPI"`, `articulo="140"`).
- **Marcas** → `buscar_articulo` (`ley="Ley 17/2001"`, artículos `"31"`, `"34"`, `"39"`, `"46"`, `"47"`, `"48"` y `"49"`).
- **Know-how, secretos empresariales y patentes** → `buscar_articulo` (`ley="BOE-A-2019-2364"`, artículos `"1"`, `"4"`, `"6"` y `"7"`) y (`ley="Ley 24/2015"`, artículos `"15"`, `"82"` y `"83"`).
- **Competencia en licencias de tecnología** → `buscar_articulo` (`ley="Ley 15/2007"`, `articulo="1"`) y el reglamento de exención de la Unión vigente para acuerdos de transferencia de tecnología: búscalo con `buscar_boe` (`consulta="acuerdos de transferencia de tecnología artículo 101 apartado 3"`) y lee sus artículos con `buscar_articulo` usando el CELEX que devuelva (en septiembre de 2026, el Reglamento (UE) 2026/877, `ley="32026R0877"`, artículos `"2"`, `"3"`, `"4"` y `"5"`; el anterior, 316/2014, expiró).
- **Doctrina sobre alcance de la cesión, transformación, software de trabajadores y encargos, y licencias de marca** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; Audiencias con `base="AN"` y `tipo_organo="AP"`; agotamiento y licencias de software, `base="TJUE"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión). Si alguna parte es sociedad, `buscar_empresa_mercantil`.
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...).

En el documento, cita «artículo 43 del Real Decreto Legislativo 1/1996, de 12 de abril, por el que se aprueba el texto refundido de la Ley de Propiedad Intelectual», «artículo 48 de la Ley 17/2001, de 7 de diciembre, de Marcas» y «artículo 6 de la Ley 1/2019, de 20 de febrero, de Secretos Empresariales»: así las reconoce `verificar_escrito`. El verificador no identifica los reglamentos de la Unión: comprueba cada artículo europeo con `buscar_articulo` e ignora su veredicto sobre él.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Un autor (escritor, diseñador, fotógrafo, programador autónomo) cede derechos a una empresa, o una empresa titular los licencia a otra.
- Desarrollo de software a medida, licencia de uso de un programa, contrato de mantenimiento con cesión de mejoras.
- Cesión (venta) o licencia de una marca registrada o solicitada; licencia de know-how o de patente.
- Cláusula de propiedad intelectual para un contrato de servicios, de obra, laboral o de colaboración.

| Situación | Skill |
|---|---|
| El núcleo es proteger información antes de negociar | `confidencialidad-nda` |
| Franquicia (marca + know-how + asistencia) o distribución con licencia de marca accesoria | `agencia-distribucion-franquicia` |
| Servicio profesional o desarrollo con entregables, niveles de servicio y honorarios | `prestacion-servicios` o `contrato-obra` (esta skill aporta la cláusula de propiedad intelectual) |
| El licenciatario o el licenciante tratará datos personales del otro | `encargo-tratamiento-datos` |
| Condiciones generales de una licencia a consumidores | `condiciones-generales-consumidores` |
| Revisar la licencia que envía la otra parte | `revision-contrato-semaforo`, `negociacion-contrapropuesta` |
| Infracción o impago de regalías | `requerimiento-cumplimiento`, `resolucion-por-incumplimiento`, `reclamacion-deuda-monitorio` |
| Contrato de edición, representación teatral o producción audiovisual | Tienen régimen propio en el TRLPI (art. 57): léelo con `buscar_articulo` antes de usar esta skill y díselo al abogado |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ **A quién defiende el abogado**: cedente o licenciante (autor persona física, empresa titular) o cesionario o licenciatario.
2. ★ **Qué se transmite**: tipo de obra o creación; en software, programa fuente y objeto, documentación, versiones y componentes de terceros o de código abierto (con sus licencias); en marca, número, oficina (española o de la Unión), clases y productos o servicios; en know-how, descripción y soporte; en patente, número y estado.
3. ★ **Cadena de titularidad**: quién es el autor; coautores; trabajadores o colaboradores autónomos que participaron y documentos con los que cedieron sus derechos; cesiones o licencias anteriores; si parte del resultado se generó con herramientas de inteligencia artificial y cuánto aportó el autor humano (el TRLPI considera autor a la persona natural que crea la obra, art. 5.1).
4. ★ **Tipo de negocio**: cesión (transmisión del derecho) o licencia (autorización de uso); exclusiva o no exclusiva; con o sin facultad de sublicenciar o ceder.
5. ★ **Derechos y modalidades concretas**: reproducción, distribución, comunicación pública (incluida la puesta a disposición en internet), transformación; formatos, canales, productos.
6. ★ **Territorio y duración**.
7. ★ **Remuneración**: porcentaje sobre ingresos (y su base), mínimo garantizado, tanto alzado, hitos; liquidación, rendición de cuentas y auditoría.
8. En software: entregables, pruebas de aceptación, mantenimiento, depósito del código fuente, garantía de funcionamiento.
9. En marca: control de calidad, forma de uso, quién mantiene y renueva el registro, quién defiende la marca.
10. Garantías de titularidad y no infracción, indemnidad frente a terceros, mejoras (de quién son), no impugnación, confidencialidad, terminación y periodo de liquidación de existencias, ley y tribunales o arbitraje.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la línea de vigencia.

**1. Qué se protege y de quién es.** Son objeto de propiedad intelectual las creaciones originales (art. 10 TRLPI); autor es la persona natural que crea la obra (art. 5). Obra en colaboración (art. 7) y obra colectiva, cuyos derechos corresponden salvo pacto a quien la edita y divulga con su nombre (art. 8). Derechos de explotación: reproducción, distribución, comunicación pública y transformación (arts. 17 a 21); duración, arts. 26 y 28. Adquirir el soporte no da derechos de explotación (art. 56.1).

**2. Trabajadores y encargos.**
- Obra creada en virtud de relación laboral: rige lo pactado por escrito y, a falta de pacto, se presume cedida en exclusiva con el alcance necesario para la actividad habitual del empresario al entregarla; el empresario no puede usarla para fines distintos (art. 51 TRLPI).
- Programa creado por un trabajador en el ejercicio de sus funciones o siguiendo instrucciones: los derechos de explotación, fuente y objeto, son del empresario salvo pacto (art. 97.4). No basta que se cree «con ocasión» del trabajo: pregunta cuáles eran sus funciones.
- Invenciones del empleado o prestador de servicios fruto de una actividad de investigación que es objeto de su contrato: art. 15 de la Ley 24/2015.
- **Encargo a un autónomo o a una empresa**: no hay presunción; sin cesión expresa, el comitente solo tiene lo que se deduzca necesariamente del contrato para su finalidad (art. 43.2). Por eso todo contrato de encargo lleva cláusula de cesión expresa y el comitente debe exigir las cesiones de los colaboradores del proveedor.
- Busca: `consulta="titularidad de programas de ordenador obra por encargo arrendamiento de obra"` (`base="AN"`, `tipo_organo="AP"`) y `consulta="programa de ordenador creado por trabajador asalariado titularidad del empresario"` (`base="TS"`).

**3. Alcance de la cesión (art. 43 TRLPI).**
- Queda limitada a los derechos cedidos, a las modalidades expresamente previstas y al tiempo y territorio determinados.
- Sin plazo, cinco años; sin territorio, el país en que se cede; sin modalidades concretas, solo las que se deduzcan necesariamente del contrato y sean indispensables para su finalidad.
- Nula la cesión del conjunto de las obras futuras del autor y el compromiso de no crear; no alcanza modalidades o medios inexistentes o desconocidos al ceder.
- Por escrito; si no, el autor puede resolver tras requerimiento fehaciente (art. 45). Si el contrato incluye edición, representación o producción audiovisual, rigen sus disposiciones específicas (art. 57).
- Busca y lee (imprescindible cuando la cesión es amplia o genérica): `consulta="cesión de derechos de explotación modalidades no previstas interpretación restrictiva artículo 43 propiedad intelectual"` (`base="TS"`). En las pruebas, la Sala Primera aplica el art. 43.2 después de interpretar el contrato con los arts. 1281 a 1289 CC, y exige que la cesión del derecho de transformación se refiera a una obra concreta y a actos de transformación determinados, por su conexión con el derecho moral de integridad. Consecuencia: enumera derechos, modalidades, formatos y actos de transformación permitidos; no escribas «todos los derechos, en todas las modalidades» sin concretarlas.

**4. Derechos morales.** Son irrenunciables e inalienables: divulgación, paternidad, integridad, modificación, retirada, acceso (art. 14 TRLPI). El contrato no los renuncia: recoge las adaptaciones que el autor autoriza desde ahora y la forma de mención de su nombre. En software, salvo pacto, el autor no puede oponerse a que el cesionario haga versiones sucesivas y programas derivados (art. 100.4).

**5. Remuneración del autor.**
- Regla: participación proporcional en los ingresos (art. 46.1); tanto alzado solo en los supuestos del art. 46.2 (dificultad grave de determinar o comprobar ingresos, uso accesorio, obra no esencial en la creación en que se integra, primera edición de ciertas obras). Si se pacta tanto alzado fuera de esos casos, dilo en la nota como riesgo.
- Revisión por desproporción manifiesta entre lo pactado y los ingresos del cesionario: dentro de los diez años siguientes a la cesión, salvo pacto expreso o acuerdo sectorial que prevea un procedimiento de revisión; no aplica a autores de programas de ordenador (art. 47).
- Revocación por falta de explotación en la cesión exclusiva: el autor puede resolver o poner fin a la exclusividad pasados cinco años, con una comunicación que fije un plazo no inferior a un año; no aplica a obras colectivas, en colaboración ni programas de ordenador, y es irrenunciable (art. 48 bis).
- Los beneficios que el título de transmisión otorga a los autores son irrenunciables salvo que la ley diga otra cosa (art. 55).
- Estas reglas protegen al **autor**: si quien cede es una empresa titular derivativa, dilo en la nota y ajusta.

**6. Exclusiva y no exclusiva.** La exclusiva debe otorgarse expresamente, excluye incluso al cedente, permite (salvo pacto) dar licencias no exclusivas, legitima al cesionario para perseguir infracciones y le obliga a poner los medios para explotar (art. 48). El cesionario en exclusiva solo transmite con consentimiento expreso del cedente, salvo disolución o cambio de titularidad de la empresa (art. 49). El no exclusivo usa la obra en concurrencia y su derecho es intransmisible salvo esos supuestos (art. 50).

**7. Programas de ordenador.** Incluyen la documentación preparatoria, técnica y manuales; no se protegen ideas y principios ni los de las interfaces (art. 96). Duración si el titular es persona jurídica: art. 98.2. La cesión del derecho de uso se presume no exclusiva e intransferible y para las necesidades del usuario (art. 99); la copia de seguridad necesaria no puede prohibirse por contrato y hay límites de corrección de errores e interoperabilidad (art. 100). Registro voluntario: art. 101. Para reventa de licencias o copias descargadas, busca `consulta="agotamiento del derecho de distribución copia de programa de ordenador licencia de uso descarga"` (`base="TJUE"`). En los componentes de código abierto, las obligaciones de su licencia viajan con el programa: identifica cada una en un anexo, lee su texto oficial en internet (sitio de la organización que publica la licencia) y cítalo con enlace y fecha de consulta; nunca las resumas de memoria.

**8. Marcas (Ley 17/2001).**
- Registro por diez años desde la solicitud, renovable por periodos de diez (art. 31).
- La marca y su solicitud pueden transmitirse, licenciarse o gravarse con independencia de la empresa, y esos actos solo se oponen a terceros de buena fe una vez inscritos (art. 46.2 y 3). En cotitularidad, las licencias se acuerdan como dice el art. 46.1.
- La transmisión de la empresa en su totalidad implica la de la marca salvo pacto o circunstancias que claramente indiquen lo contrario (art. 47).
- Licencia (art. 48): total o parcial por productos y territorio; exclusiva o no; el titular puede actuar contra el licenciatario que infrinja límites de duración, forma, productos o servicios, territorio o calidad; sin pacto, no se cede ni se sublicencia, dura todo el registro y renovaciones, cubre todo el territorio y todos los productos o servicios y se presume no exclusiva; en la exclusiva, el licenciante solo usa la marca si se lo reservó; el licenciatario necesita consentimiento del titular para demandar, salvo el exclusivo si el titular requerido no actúa.
- El uso con consentimiento del titular cuenta como uso del titular (art. 39.4), lo que evita la caducidad por falta de uso en cinco años (art. 39.1): exige en la licencia uso efectivo y conservación de pruebas de uso.
- Inscripción de la cesión o licencia: art. 49 (documentos admitidos).
- Busca: `consulta="licencia de marca inscripción efectos frente a terceros licenciatario"` (`base="TS"`).

**9. Know-how y patentes.** Secreto empresarial: información secreta, con valor empresarial por serlo y protegida con medidas razonables (art. 1 de la Ley 1/2019); es transmisible (art. 4) y licenciable con el alcance que se pacte, presumiéndose no exclusiva, sin cesión ni sublicencia salvo pacto y con obligación del licenciatario de protegerlo (art. 6); quien transmite o licencia sin titularidad responde (art. 7). Patentes: arts. 82 y 83 de la Ley 24/2015 (presunciones análogas). Describe el know-how en un anexo identificable sin revelarlo en el cuerpo del contrato.

**10. Competencia.** Exclusividades territoriales, precios, limitaciones de producción, retrocesión exclusiva de mejoras y cláusulas de no impugnación pueden infringir el art. 1 de la Ley 15/2007. En licencias de tecnología (patente, know-how, software para producir), lee el reglamento de exención vigente: umbrales de cuota de mercado (art. 3), restricciones especialmente graves (art. 4) y restricciones excluidas (art. 5); no calcules cuotas de mercado: pídelas al cliente y dilo en la nota.

**11. Infracción y tributación.** La indemnización por infracción puede fijarse por la regalía que se habría pagado (art. 140.2.b TRLPI; prescripción de cinco años, art. 140.3): úsalo como referencia para la cláusula penal por uso fuera de licencia. Retenciones e IVA de regalías, sobre todo con licenciante no residente: no des tipos; comprueba con `buscar_consultas_hacienda`.

## Cláusulas clave y jurisprudencia

Para cada cláusula: redacción según a quién defiendas, riesgo y búsqueda. La jurisprudencia es **imprescindible** (apartado 8 del formato) cuando la validez de la cláusula depende de ella (alcance de una cesión genérica, remuneración a tanto alzado fuera del art. 46.2, no competencia o no impugnación, cláusula penal).

1. **Objeto y definiciones.** Obra, programa, marca o know-how identificados en anexo (título, versión, número de registro, clases). «Resultados» y «Mejoras» definidos una sola vez.
2. **Cesión o licencia.** Cesionario: cesión exclusiva, mundial, por el máximo plazo legal, con facultad de ceder y sublicenciar, enumerando derechos, modalidades y actos de transformación. Cedente: licencia no exclusiva, territorio y plazo concretos, sin sublicencia, con reserva de las modalidades no mencionadas.
3. **Derechos morales.** Mención del autor y adaptaciones autorizadas; sin renuncias.
4. **Remuneración.** Autor: porcentaje con base definida (ingresos brutos o netos, qué se descuenta), mínimo garantizado, liquidaciones periódicas, derecho de auditoría con coste a cargo del licenciatario si hay diferencias. Explotador: tanto alzado si encaja en el art. 46.2 (dilo en el contrato: qué supuesto), o regalía decreciente. Si el cesionario va a comercializar la obra o el programa (licencias a terceros), sus ingresos son identificables y el tanto alzado difícilmente encaja en el art. 46.2 (el art. 46 no excluye a los autores de programas, a diferencia de los arts. 47.3 y 48 bis.2). Imprescindible si el tanto alzado es dudoso: `consulta="remuneración proporcional tanto alzado cesión derechos de autor artículo 46"` (`base="TS"`; en las pruebas solo devolvió casos de edición musical; reformula en Audiencias). Si no hay doctrina aplicable, la vía segura que no depende de ella es la del art. 46.1: precio fijo más una participación en los ingresos, con liquidaciones y auditoría.
5. **Entrega, aceptación y código fuente (software).** Pruebas de aceptación con plazo y aceptación tácita; entrega del fuente o depósito con un tercero y supuestos de liberación; documentación incluida (art. 96.1).
6. **Obligación de explotar.** En la exclusiva existe por ley (art. 48); fija hitos mínimos. Autor: resolución o fin de la exclusividad si no se explota (y recuerda el art. 48 bis). Explotador: definición objetiva de «explotación».
7. **Garantías e indemnidad.** Licenciatario o cesionario: titularidad, originalidad, ausencia de cargas y de infracción de terceros, cesiones de los colaboradores entregadas, indemnidad plena. Licenciante: garantía limitada a su conocimiento, tope de responsabilidad y exclusión de modificaciones hechas por el licenciatario. Busca doctrina de infracción si el riesgo es alto: `consulta="derecho moral integridad de la obra modificación sin consentimiento del autor"` (`base="TS"`).
8. **Control de calidad y uso de la marca.** Normas de uso, muestras, aprobación de materiales; uso efectivo y pruebas de uso (art. 39); quién renueva y defiende la marca y quién puede demandar (art. 48.7).
9. **Mejoras y retrocesión.** Licenciante: licencia no exclusiva de las mejoras del licenciatario (una retrocesión exclusiva queda fuera de la exención, art. 5 del reglamento vigente). Licenciatario: sus mejoras son suyas.
10. **No competencia y no impugnación.** Comprueba el reglamento de exención y el art. 1 de la Ley 15/2007; en licencia exclusiva, en lugar de prohibir impugnar, prevé la resolución si el licenciatario impugna la validez (art. 5.1.b del reglamento vigente).
11. **Confidencialidad del know-how** y medidas razonables exigidas al licenciatario (art. 6.4 de la Ley 1/2019).
12. **Duración, terminación y efectos.** Causas de resolución (impago, uso fuera de licencia, cambio de control), periodo para agotar existencias, devolución del know-how y del código, cesión de las solicitudes de registro. Cláusula penal por uso fuera de licencia referenciada a la regalía (art. 140.2.b TRLPI); imprescindible: `consulta="cláusula penal moderación improcedente cuando el incumplimiento es el previsto"` (`base="TS"`).
13. **Inscripción.** Obligación y coste de inscribir la cesión o licencia de marca o patente (art. 49 de la Ley 17/2001) y, si se quiere, la cesión de software en el Registro de la Propiedad Intelectual (art. 101 TRLPI). Si el abogado quiere saber las tasas, búscalas en internet en la sede electrónica de la oficina (Oficina Española de Patentes y Marcas, Oficina de Propiedad Intelectual de la Unión Europea o Registro de la Propiedad Intelectual) y cítalas con enlace y fecha de consulta; no las des de memoria.
14. **Ley y tribunales o arbitraje; notificaciones; integridad.**

## Documentos que se entregan

Según `references/formato-y-entrega-contratos.md`, dos documentos:

1. `contrato-cesion-propiedad-intelectual-<parte-principal>-<AAAAMMDD>.docx` (o `licencia-software`, `licencia-marca`, `licencia-know-how`):
   - Título, lugar y fecha; REUNIDOS e INTERVIENEN.
   - EXPONEN: titularidad y cadena de derechos, finalidad de la explotación.
   - ESTIPULACIONES, en este orden: definiciones; objeto; cesión o licencia (derechos, modalidades, exclusividad, territorio, duración, sublicencia); derechos morales; remuneración y liquidaciones; entrega y aceptación; obligación de explotar; control de calidad; mejoras; garantías e indemnidad; confidencialidad; inscripción; duración y terminación; efectos de la terminación; cláusula penal si la hay; notificaciones; ley y tribunales o arbitraje; integridad.
   - Anexos: obras o programas (con versión); componentes de terceros y de código abierto con su licencia; registros de marca o patente; descripción del know-how; normas de uso de la marca; cesiones de los colaboradores.
   - **Reparto para la redacción rápida:** una sección por bloque de estipulaciones (`### [ESTIPULACION]`): comparecencia, expositivos, definiciones y objeto / cesión o licencia (derechos, modalidades, exclusividad, territorio, duración), derechos morales y remuneración / entrega y aceptación, obligación de explotar, control de calidad, mejoras, garantías e indemnidad, confidencialidad e inscripción / duración, terminación y sus efectos, cláusula penal, notificaciones, ley, fuero y firmas / anexos. La nota: apartado 11 del formato.
   - Si solo se pide la cláusula para otro contrato, entrégala en un Word propio con la nota.
2. `nota-cesion-propiedad-intelectual-<parte-principal>-<AAAAMMDD>.docx`:
   - Régimen con los artículos leídos: qué protege al autor de forma irrenunciable (arts. 14, 47, 48 bis y 55 TRLPI) y qué es pactable.
   - Por cada cláusula crítica, qué dice, por qué y su base (artículo y, cuando proceda, párrafo literal con órgano, fecha y ECLI).
   - Riesgos de titularidad (colaboradores sin cesión, contenidos generados con IA, código abierto) y de competencia.
   - Tributación a comprobar sin cifras; datos pendientes.

Marcadores para lo que falte: `[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[DOMICILIO]`, `[TÍTULO DE LA OBRA]`, `[NÚMERO DE REGISTRO]`, `[CLASES]`, `[PORCENTAJE]`, `[IMPORTE]`, `[TERRITORIO]`.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos usados del TRLPI, la Ley 17/2001, la Ley 1/2019, la Ley 24/2015 y la Ley 15/2007; localizado con `buscar_boe` el reglamento de exención vigente y leídos sus artículos por CELEX.
- [ ] Cadena de titularidad documentada: autor, colaboradores y trabajadores con su cesión; lo que falta, listado en el resumen.
- [ ] Derechos, modalidades, territorio y duración expresos (art. 43 TRLPI); ninguna renuncia a derechos morales; remuneración conforme al art. 46 o riesgo explicado.
- [ ] Doctrina leída con `leer_sentencias` (párrafo de fundamentos) cuando es imprescindible; cada ECLI citado, leído o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); los artículos del reglamento de la Unión, comprobados solo con `buscar_articulo`.
- [ ] Definiciones únicas, porcentajes y plazos coherentes, marcadores en lugar de datos inventados.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas y cómo se resolvieron, documentos que faltan (cesiones de colaboradores, títulos de registro, licencias de código abierto), tabla de jurisprudencia, plazos (art. 47 y 48 bis si cede un autor) y próximo paso (firma e inscripción).
