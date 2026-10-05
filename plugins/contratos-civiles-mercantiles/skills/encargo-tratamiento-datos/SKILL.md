---
name: encargo-tratamiento-datos
description: >-
  Redacta el contrato de encargado del tratamiento con el contenido obligatorio del artículo 28 del RGPD y el
  33 de la LOPDGDD, o las cláusulas de datos de otro contrato, con nota para el abogado: papeles (responsable,
  encargado, corresponsables), instrucciones, confidencialidad, seguridad, subencargados, transferencias
  internacionales, asistencia, violaciones de seguridad, devolución o destrucción, auditorías y
  responsabilidad. Úsala cuando el abogado diga «contrato de encargado», «DPA», «acuerdo de tratamiento de
  datos», «el proveedor accede a nuestros datos», «subencargados», «cláusula RGPD» o «los datos van a Estados
  Unidos». Si el proveedor usa los datos para fines propios o ambos deciden los fines, lo detecta y no redacta
  un encargo; para condiciones con consumidores, usa condiciones-generales-consumidores; para información sin
  datos personales, confidencialidad-nda.
---

# Contrato de encargado del tratamiento y cláusulas de datos

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Quién es responsable y quién encargado** → `buscar_articulo` (`ley="RGPD"`, artículos `"4"`, `"24"`, `"26"`, `"28"` y `"29"`) y (`ley="LOPDGDD"`, artículos `"29"` y `"33"`).
- **Contenido obligatorio, confidencialidad y registro** → `buscar_articulo` (`ley="RGPD"`, artículos `"28"`, `"29"`, `"30"`, `"37"` y `"27"`) y (`ley="LOPDGDD"`, artículos `"5"`, `"28"`, `"30"`, `"31"`, `"33"` y `"34"`).
- **Seguridad, violaciones de seguridad y evaluación de impacto** → `buscar_articulo` (`ley="RGPD"`, artículos `"32"`, `"33"`, `"34"`, `"35"` y `"36"`) y (`ley="LOPDGDD"`, `articulo="28"`); si el responsable es del sector público, el Esquema Nacional de Seguridad (`ley="BOE-A-2022-7191"`, `articulo="2"`) y la Ley de Contratos del Sector Público (`ley="LCSP"`, `articulo="122"`).
- **Transferencias internacionales** → `buscar_articulo` (`ley="RGPD"`, artículos `"44"`, `"45"`, `"46"`, `"47"`, `"48"` y `"49"`) y (`ley="LOPDGDD"`, artículos `"40"`, `"41"`, `"42"` y `"43"`); cláusulas tipo de transferencia (`ley="32021D0914"`, `articulo="1"`); decisiones de adecuación vigentes con `buscar_boe` (p. ej., Estados Unidos: `ley="32023D1795"`, `articulo="1"`).
- **Cláusulas tipo entre responsable y encargado (art. 28.7)** → `buscar_articulo` (`ley="32021D0915"`, `articulo="1"`); su anexo solo se lee en parte con `leer_boe` (el texto se corta a los 12.000 caracteres): el texto íntegro, en EUR-Lex (punto 3 de la puerta).
- **Fin del encargo, bloqueo, responsabilidad y sanciones** → `buscar_articulo` (`ley="LOPDGDD"`, artículos `"32"`, `"33"`, `"70"`, `"73"` y `"74"`) y (`ley="RGPD"`, artículos `"82"` y `"83"`).
- **Doctrina sobre calificación de papeles, transferencias y responsabilidad** → `buscar_sentencias` con `base="TJUE"`; Audiencia Nacional, Sala de lo Contencioso (`base="AN"`, `jurisdiccion="CONTENCIOSO"`, `tipo_organo="AN"`); daños civiles, `base="TS"` y `jurisdiccion="CIVIL"`; después `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión). **Partes que son sociedades** → `buscar_empresa_mercantil`.
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...).

**`verificar_escrito` no reconoce el RGPD**: atribuye cada artículo del Reglamento a la última ley española nombrada en el texto (comprobado: el artículo 82 del RGPD lo tomó por el artículo 82 de la LOPDGDD, «derecho a la seguridad digital», y el 28 por otra ley). Cada artículo del RGPD, de las decisiones de la Comisión y de cualquier norma de la Unión se comprueba con `buscar_articulo` en esta conversación, y el veredicto del verificador sobre ellos se ignora. Cita el Reglamento como «artículo 28 del Reglamento (UE) 2016/679» y la ley española como «artículo 33 de la Ley Orgánica 3/2018, de 5 de diciembre».

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Un proveedor (gestoría, asesoría laboral, alojamiento, software en la nube, centro de llamadas, mensajería, desarrollo, mantenimiento, videovigilancia) accede a datos personales para prestar un servicio al cliente.
- Subencargo: el proveedor recurre a otro proveedor.
- Cláusulas de datos para otro contrato (servicios, distribución, arrendamiento, compraventa de empresa) o anexo de encargo a un contrato ya firmado.

Antes de redactar, pasa este **detector** y dile al abogado el resultado con los artículos leídos:

| Situación | Qué procede |
|---|---|
| El proveedor trata los datos solo por cuenta y según instrucciones del cliente | Contrato de encargo: esta skill |
| El proveedor usa los datos también para sus propios fines (mejorar su servicio, analítica propia, entrenar modelos, publicidad) o se relaciona con los interesados en nombre propio | Es responsable respecto de ese tratamiento (art. 28.10 RGPD; art. 33.2 LOPDGDD): necesita base jurídica propia e información a los interesados; limita contractualmente esos usos o prevé una cesión entre responsables |
| Ambos deciden conjuntamente fines y medios | Corresponsables: acuerdo del art. 26 RGPD (y art. 29 LOPDGDD), no contrato de encargo |
| Se comunican datos a otro responsable que los usará para sus fines | Cesión entre responsables: cláusula de base jurídica, información y deber de cada parte |
| Solo se intercambian los datos de contacto de las personas que firman o se relacionan | Cláusula informativa breve; el art. 19 LOPDGDD presume el interés legítimo si se cumplen sus requisitos |
| El responsable es una Administración o entidad del sector público | Esta skill, más el art. 122.2 LCSP y el Esquema Nacional de Seguridad |

| Otra necesidad | Skill |
|---|---|
| Contrato principal de servicios con niveles de servicio y precio | `prestacion-servicios` (esta skill aporta el anexo de encargo) |
| Revisar el DPA que impone un proveedor | `revision-contrato-semaforo`, `negociacion-contrapropuesta` |
| Condiciones generales y política de privacidad para consumidores | `condiciones-generales-consumidores` |
| Licencia de software con tratamiento de datos | `licencia-cesion-propiedad-intelectual` y esta skill |
| El encargado ha sufrido una brecha o incumple: requerir o resolver | `requerimiento-cumplimiento`, `resolucion-por-incumplimiento` |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ **A quién defiende el abogado**: responsable (cliente del servicio) o encargado (proveedor).
2. ★ **Servicio y tratamiento**: contrato principal, operaciones concretas (acceso, alojamiento, consulta, modificación, envío), finalidad, duración.
3. ★ **Datos e interesados**: categorías de datos y de interesados, volumen aproximado; si hay categorías especiales (art. 9 RGPD), datos de condenas o infracciones (art. 10) o menores y personas vulnerables.
4. ★ **Quién decide qué**: si el proveedor usará los datos para algo propio (aplica el detector).
5. ★ **Dónde**: ubicación de servidores y equipos de soporte, subencargados previstos (identidad, servicio, país), empresas del grupo fuera del Espacio Económico Europeo con acceso.
6. ★ **Seguridad**: medidas del proveedor, certificaciones, si el responsable es sector público (Esquema Nacional de Seguridad).
7. **Plazos operativos**: aviso de violaciones de seguridad (horas), respuesta a solicitudes de derechos, preaviso de nuevos subencargados y plazo para oponerse.
8. **Auditorías**: frecuencia, preaviso, a cargo de quién, informes de terceros aceptados.
9. **Fin del servicio**: devolución, destrucción o entrega a un nuevo proveedor; formato y plazo; obligaciones legales de conservación del responsable.
10. **Responsabilidad**: tope entre partes, seguro, indemnidad; ley y tribunales del contrato principal.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la versión que devuelve el conector.

**1. Calificación.** Responsable es quien determina fines y medios; encargado, quien trata por cuenta del responsable (art. 4, puntos 7 y 8, RGPD). El acceso del encargado no es comunicación de datos si se cumple la normativa (art. 33.1 LOPDGDD). Es responsable, y no encargado, quien en su propio nombre y sin constar que actúa por otro se relaciona con los afectados, aunque haya contrato del art. 28.3, salvo los encargos del sector público; y quien, figurando como encargado, usa los datos para sus fines (art. 33.2 LOPDGDD; art. 28.10 RGPD). Busca y lee: `consulta="encargado del tratamiento considerado responsable artículo 28 apartado 10"` (`base="TJUE"`). En las pruebas, el Tribunal de Justicia declaró que puede multarse al responsable por el tratamiento que el encargado hace por su cuenta, salvo que el encargado haya tratado los datos para fines propios o fuera del marco fijado por el responsable. Consecuencia: define con precisión la finalidad y prohíbe cualquier otro uso; si el cliente acepta usos propios del proveedor, sácalos del encargo.

**2. Elección del encargado.** Solo uno que ofrezca garantías suficientes de medidas técnicas y organizativas apropiadas (art. 28.1 RGPD); la adhesión a un código de conducta o certificación sirve como elemento para demostrarlo (art. 28.5). Contratar un encargado sin esas garantías es infracción grave del responsable (art. 73, letra j, LOPDGDD): documenta en la nota la comprobación hecha.

**3. Contenido obligatorio (art. 28.3 RGPD).** Contrato o acto jurídico que vincule al encargado y fije objeto, duración, naturaleza y finalidad, tipo de datos, categorías de interesados y obligaciones y derechos del responsable, y que estipule que el encargado:
- a) trata solo según instrucciones documentadas, también sobre transferencias, salvo obligación legal que debe comunicar;
- b) garantiza la confidencialidad de las personas autorizadas (y el deber de confidencialidad del art. 5 LOPDGDD, que subsiste al terminar la relación);
- c) aplica las medidas del art. 32;
- d) respeta las condiciones para subencargar;
- e) asiste en la respuesta a los derechos de los interesados;
- f) ayuda a cumplir los arts. 32 a 36 (seguridad, violaciones, evaluación de impacto, consulta previa);
- g) suprime o devuelve los datos, a elección del responsable, al terminar, y suprime las copias salvo obligación legal de conservar;
- h) pone a disposición la información necesaria y permite auditorías e inspecciones.
Además, informa inmediatamente si una instrucción infringe la normativa (último párrafo del art. 28.3; no hacerlo es infracción leve del encargado, art. 74, letra j, LOPDGDD). El contrato consta por escrito, también en formato electrónico (art. 28.9). Las personas que actúan bajo la autoridad del responsable o del encargado solo tratan según instrucciones (art. 29). Redacta una cláusula por letra y comprueba al final que ninguna falta.

**4. Subencargados.** Autorización previa por escrito, específica o general; en la general, el encargado informa de cada cambio y el responsable puede oponerse (art. 28.2 RGPD). Al subencargado se le imponen por contrato las mismas obligaciones, y el encargado inicial sigue siendo plenamente responsable de su cumplimiento (art. 28.4). Subencargar sin autorización o sin informar de los cambios es infracción grave (art. 73, letra l, LOPDGDD).

**5. Seguridad.** Medidas apropiadas al riesgo, como seudonimización y cifrado, confidencialidad, integridad, disponibilidad y resiliencia, restauración rápida y verificación periódica (art. 32.1 RGPD). Valora los mayores riesgos que enumera el art. 28.2 LOPDGDD (categorías especiales, perfiles, vulnerables, tratamientos masivos, transferencias habituales sin adecuación). Si el responsable es del sector público, el Esquema Nacional de Seguridad se aplica también al proveedor privado que le presta servicios (art. 2.3 del Real Decreto 311/2022) y los pliegos deben recoger la finalidad, el sometimiento a la normativa, la ubicación de los servidores y los subcontratistas como obligaciones esenciales (art. 122.2 LCSP). Describe las medidas en un anexo concreto, no con fórmulas genéricas.

**6. Violaciones de seguridad.** El encargado notifica al responsable sin dilación indebida (art. 33.2 RGPD); el responsable notifica a la autoridad sin dilación indebida y, de ser posible, en 72 horas desde que tuvo constancia (art. 33.1), con el contenido mínimo del art. 33.3, y comunica a los interesados cuando proceda (art. 34). No notificar al responsable es infracción grave del encargado (art. 73, letra q, LOPDGDD). En el contrato fija un plazo en horas, inferior a 72, para que el responsable pueda cumplir, y el contenido del aviso siguiendo el art. 33.3; el plazo contractual es pacto de las partes: dilo así en la nota.

**7. Transferencias internacionales.** Solo con las condiciones del capítulo V (art. 44 RGPD): decisión de adecuación (art. 45), garantías adecuadas como las cláusulas tipo de la Comisión (art. 46; Decisión de Ejecución (UE) 2021/914, art. 1), normas corporativas vinculantes (art. 47) o, excepcionalmente, las excepciones del art. 49. Régimen español: arts. 40 a 43 LOPDGDD (supuestos de autorización previa o de información previa a la autoridad). El acceso remoto desde fuera del Espacio Económico Europeo por soporte o por empresas del grupo también es transferencia. Para Estados Unidos, la decisión de adecuación de 2023 (art. 1 de la Decisión 2023/1795) cubre solo a las entidades inscritas en la lista del Marco de Privacidad de Datos: comprueba en internet, en la lista oficial, si el importador está inscrito y para qué datos, y cítalo con enlace y fecha de consulta. Si la lista no se puede leer (la página oficial carga los datos con JavaScript), dilo en la nota y exige en el contrato que el encargado acredite la inscripción antes de la transferencia o, en su defecto, las cláusulas tipo con la evaluación del país de destino. Busca con `buscar_boe` si hay decisiones de adecuación posteriores y lee la doctrina: `consulta="cláusulas contractuales tipo transferencia tercer país garantías adecuadas"` (`base="TJUE"`); en las pruebas, el Tribunal de Justicia exige al exportador que se apoya en cláusulas tipo comprobar caso por caso si el Derecho del país de destino garantiza una protección sustancialmente equivalente, añadir garantías si hace falta y, si no es posible, suspender la transferencia. Prepara esa evaluación como anexo a cargo del exportador y prevé en el contrato la suspensión y la resolución si deja de cumplirse.

**8. Fin del encargo y bloqueo.** El responsable decide si los datos se destruyen, se devuelven o se entregan a un nuevo encargado; no se destruyen si una ley obliga a conservarlos, y entonces se devuelven al responsable (art. 33.3 LOPDGDD). El encargado puede conservarlos bloqueados mientras puedan derivarse responsabilidades de su relación con el responsable (art. 33.4); el bloqueo es identificación y reserva que impide el tratamiento salvo para jueces, fiscal y administraciones (art. 32). Fija formato, plazo y certificado de destrucción. Si hay historias clínicas u otra documentación con plazo legal de conservación, lee el precepto (p. ej., `buscar_articulo` con `ley="BOE-A-2002-22188"`, `articulo="17"`, para la documentación clínica): el encargado devuelve y solo después suprime.

**9. Registro, delegado y representante.** El encargado lleva su propio registro de actividades (art. 30.2 RGPD; art. 31 LOPDGDD); designación del delegado de protección de datos (art. 37 RGPD; art. 34 LOPDGDD); representante si el encargado no está establecido en la Unión (art. 27 RGPD; art. 30 LOPDGDD; no designarlo es infracción grave, art. 73, letra h, LOPDGDD).

**10. Responsabilidad y sanciones.** Frente al interesado, el encargado solo responde si incumplió obligaciones dirigidas específicamente a los encargados o actuó al margen o en contra de instrucciones legales; se exime si prueba que no es responsable del hecho; varios responsables o encargados en la misma operación responden de todo frente al interesado y después se reparten (art. 82 RGPD). Multas: art. 83 RGPD; el encargado está sujeto al régimen sancionador (art. 70 LOPDGDD); incumplir el contrato o las instrucciones es infracción leve del encargado salvo obligación legal (art. 74, letra k); si determina fines y medios, grave (art. 73, letra m). El reparto interno (indemnidad, tope, seguro) es pactable, pero no puede limitar los derechos del interesado ni las multas. Para daños reclamados por interesados, busca `consulta="daño inmaterial protección de datos personales indemnización"` con `base="TJUE"` y con `base="TS"` y `jurisdiccion="CIVIL"`.

**11. Cláusulas tipo del art. 28.7.** Las partes pueden basar el contrato, total o parcialmente, en cláusulas tipo (art. 28.6 y 7 RGPD; Decisión de Ejecución (UE) 2021/915, art. 1). El conector no devuelve el anexo completo (`leer_boe` corta el texto): si el cliente quiere usar las cláusulas tipo, búscalas en internet en EUR-Lex (CELEX 32021D0915), incorpora el texto oficial íntegro de las cláusulas y opciones elegidas y cítalo con enlace y fecha de consulta; haz lo mismo con los módulos de las cláusulas tipo de transferencia (CELEX 32021D0914). Nunca las transcribas de memoria ni las reconstruyas. Las directrices del Comité Europeo de Protección de Datos y las guías de la Agencia Española de Protección de Datos (papeles de responsable y encargado, notificación de violaciones, transferencias) tampoco están en el conector: si las necesitas, búscalas en internet en su sede oficial y cítalas con enlace y fecha de consulta.

## Cláusulas clave y jurisprudencia

Para cada cláusula: redacción según a quién defiendas, riesgo y búsqueda. La jurisprudencia se busca y se cita si existe (apartado 8 del formato); es imprescindible si entregas un informe de revisión o un dictamen sobre el encargo, y para la calificación de papeles cuando el proveedor quiera usos propios.

1. **Objeto, finalidad y descripción del tratamiento.** Anexo con operaciones, datos, interesados, duración y ubicación. Responsable: finalidad cerrada y prohibición expresa de cualquier otro uso, incluido el entrenamiento de modelos y la analítica propia. Encargado: descripción exacta para no asumir tratamientos que no controla.
2. **Instrucciones.** El contrato y sus anexos son las instrucciones; las nuevas, por escrito; aviso inmediato si una instrucción infringe la normativa (art. 28.3, último párrafo). Encargado: coste de las instrucciones que excedan el servicio pactado.
3. **Confidencialidad del personal** (art. 28.3.b RGPD; art. 5 LOPDGDD), con compromiso escrito y formación.
4. **Medidas de seguridad.** Anexo técnico concreto y revisión periódica (art. 32). Responsable: derecho a exigir medidas adicionales si cambia el riesgo. Encargado: medidas adicionales a cargo del responsable si no las impone la ley.
5. **Subencargados.** Responsable: autorización específica o lista cerrada, preaviso de cambios con plazo para oponerse y derecho a resolver sin penalización si se opone. Encargado: autorización general con lista pública y preaviso breve. Siempre: mismas obligaciones al subencargado y responsabilidad plena del encargado (art. 28.4).
6. **Transferencias.** Prohibidas salvo instrucción documentada y con uno de los instrumentos del capítulo V identificado por subencargado; anexo de evaluación del país de destino si hay cláusulas tipo.
7. **Asistencia en derechos, evaluación de impacto y consulta previa** (art. 28.3.e y f): plazos de reenvío de solicitudes y de respuesta, y si se factura.
8. **Violaciones de seguridad.** Plazo en horas desde que el encargado tiene constancia, canal, contenido mínimo (art. 33.3), colaboración y prohibición de comunicar a terceros o a la autoridad sin coordinar con el responsable, salvo obligación legal.
9. **Auditorías.** Responsable: auditorías e inspecciones con preaviso razonable, también por auditor externo, y acceso a instalaciones. Encargado: informes de certificación como medio preferente, frecuencia limitada, confidencialidad del auditor y coste a cargo del responsable salvo incumplimiento detectado.
10. **Fin del servicio.** Devolución o destrucción a elección del responsable, entrega a un nuevo encargado, certificado, bloqueo durante la prescripción (arts. 32 y 33 LOPDGDD).
11. **Responsabilidad e indemnidad.** Responsable: indemnidad por multas y reclamaciones causadas por el incumplimiento del encargado, fuera del tope general del contrato principal, y seguro. Encargado: tope, exclusión de daños indirectos y de los derivados de instrucciones del responsable (art. 82.2 RGPD).
12. **Prevalencia y duración.** El encargo prevalece sobre el contrato principal en materia de datos y dura mientras haya tratamiento, más las obligaciones que subsisten (confidencialidad, bloqueo).

**Cláusulas de datos para otros contratos**: (a) datos de contacto de los firmantes y personas de contacto: cláusula informativa con los extremos del art. 13 RGPD y la base del art. 19 LOPDGDD si se cumplen sus requisitos; (b) comunicación entre responsables: base jurídica (art. 6 RGPD), información a los interesados (arts. 13 y 14) y quién la da; (c) encargo: remisión a un anexo con todo lo anterior. Lee esos artículos con `buscar_articulo` antes de usarlos.

## Documentos que se entregan

Según `references/formato-y-entrega-contratos.md`, dos documentos:

1. `contrato-encargo-tratamiento-<parte-principal>-<AAAAMMDD>.docx` (como contrato autónomo o como anexo del contrato principal):
   - Título, lugar y fecha; REUNIDOS e INTERVIENEN (responsable y encargado, con sus delegados de protección de datos si los hay).
   - EXPONEN: contrato principal y necesidad del acceso a los datos.
   - ESTIPULACIONES, en este orden: definiciones; objeto y descripción del tratamiento; instrucciones; confidencialidad; seguridad; subencargados; transferencias; asistencia; violaciones de seguridad; registro y delegado; auditorías; fin del servicio y bloqueo; responsabilidad e indemnidad; duración y prevalencia; notificaciones; ley y tribunales (los del contrato principal).
   - Anexos: I, descripción del tratamiento; II, medidas técnicas y organizativas; III, subencargados autorizados (identidad, servicio, ubicación, instrumento de transferencia); IV, contenido y canal de aviso de violaciones de seguridad.
   - **Reparto para la redacción rápida:** una sección por bloque de estipulaciones (`### [ESTIPULACION]`): comparecencia, expositivos, definiciones, objeto, instrucciones y confidencialidad / seguridad, subencargados, transferencias, asistencia y violaciones de seguridad / registro y delegado, auditorías, fin del servicio, responsabilidad, duración, notificaciones, ley y firmas / anexos I a IV. La nota, con su tabla de correspondencia del art. 28.3: apartado 11 del formato.
   - Si solo se piden cláusulas para otro contrato, entrégalas en un Word propio con la nota.
2. `nota-encargo-tratamiento-<parte-principal>-<AAAAMMDD>.docx`:
   - Resultado del detector con los artículos leídos.
   - Tabla de correspondencia entre cada letra del art. 28.3 RGPD y la cláusula que la cumple.
   - Decisiones negociables y a quién favorecen; transferencias y su instrumento.
   - Riesgos: usos propios del proveedor, subencargados fuera del Espacio Económico Europeo, sector público.
   - Jurisprudencia con párrafo literal, órgano, fecha y ECLI cuando proceda; datos que salen de internet (cláusulas tipo, directrices, listas de adecuación) con enlace y fecha de consulta; datos pendientes.

Marcadores para lo que falte: `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[DOMICILIO]`, `[NOMBRE Y APELLIDOS]`, `[CONTACTO DEL DELEGADO DE PROTECCIÓN DE DATOS]`, `[PAÍS]`, `[PLAZO EN HORAS]`, `[IMPORTE]`.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Detector aplicado y explicado: encargo, corresponsabilidad, cesión entre responsables o usos propios del proveedor.
- [ ] Cada artículo del RGPD y de las decisiones de la Comisión leído con `buscar_articulo` en esta conversación (el verificador no los reconoce); leídos también los de la LOPDGDD y, si procede, el art. 2 del Real Decreto 311/2022 y el art. 122 LCSP.
- [ ] Cada letra del art. 28.3 RGPD, el aviso de instrucciones ilícitas y la forma escrita (art. 28.9) tienen su cláusula; subencargo conforme al art. 28.2 y 4.
- [ ] Transferencias identificadas por destino con su instrumento del capítulo V; decisiones de adecuación comprobadas con `buscar_boe`.
- [ ] Doctrina leída con `leer_sentencias` cuando se usa; cada ECLI citado, leído o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); corregido lo que señale sobre normas españolas e ignorado su veredicto sobre artículos de la Unión.
- [ ] Definiciones únicas, plazos coherentes (aviso de violaciones inferior a 72 horas), marcadores en lugar de datos inventados.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas y cómo se resolvieron, datos que faltan (lista de subencargados, medidas, ubicación de servidores), tabla de jurisprudencia y próximo paso (firma, registro de actividades, comprobación del importador en la lista de adecuación).
