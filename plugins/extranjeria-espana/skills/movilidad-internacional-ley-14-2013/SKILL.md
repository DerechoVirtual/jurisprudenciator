---
name: movilidad-internacional-ley-14-2013
description: >-
  Prepara los visados y autorizaciones de residencia de la Ley 14/2013, de emprendedores (arts. 61 y
  siguientes), que tramita la Unidad de Grandes Empresas y Colectivos Estratégicos: teletrabajo de
  carácter internacional (nómadas digitales), profesionales altamente cualificados y Tarjeta
  azul-UE, emprendedores con informe de ENISA, investigadores, traslados intraempresariales y sus
  familiares; también la renovación y el recurso de alzada. Comprueba qué supuestos siguen vigentes:
  la residencia para inversores quedó sin contenido. Úsala con «nómada digital», «visado de
  teletrabajo», «Tarjeta azul», «visado de emprendedor», «traslado intraempresarial», «golden visa»,
  «me ha denegado la Unidad de Grandes Empresas». Para contratar por el régimen general,
  `trabajo-cuenta-ajena`; para un negocio sin informe de ENISA, `trabajo-cuenta-propia`.
---

# Movilidad internacional de la Ley 14/2013

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Supuestos, requisitos generales y familiares** → `buscar_articulo` (`ley="BOE-A-2013-10074"`, artículos 61 y 62).
- **Requisitos de la figura concreta** → `buscar_articulo` (`ley="BOE-A-2013-10074"`): emprendedores, artículos 69 y 70; altamente cualificados, 71 y 71 bis; investigadores, 72; traslados intraempresariales, 73 y 74; teletrabajo, 74 bis, 74 ter, 74 quater y 74 quinquies.
- **Situación de la residencia para inversores** → `buscar_articulo` (`ley="BOE-A-2013-10074"`, artículos 63 a 67) antes de mencionarla.
- **Visado, procedimiento, silencio, renovación y recurso** → `buscar_articulo` (`ley="BOE-A-2013-10074"`, artículos 75 y 76; `ley="LPAC"`, artículos 121 y 122; `ley="LJCA"`, artículos 8, 10 y 46).
- **Empresa que contrata, desplaza o emplea al solicitante** → `buscar_empresa_mercantil` (nombre o CIF) cuando sea una sociedad española; de la extranjera, pide su documentación. Si hay contrato en España (alta cualificación, traslado), `buscar_convenio` + `leer_convenio` para el convenio colectivo aplicable (art. 71 bis.1.c).
- **Doctrina sobre los motivos de denegación** → `buscar_sentencias` (`consulta="teletrabajo de carácter internacional autorización residencia denegación"`, `consulta="Unidad de Grandes Empresas profesional altamente cualificado denegación"` o `consulta="residencia emprendedor informe ENISA desfavorable"`, `jurisdiccion="CONTENCIOSO"`, `base="AN"`, con `fecha_desde` en formato dd/mm/aaaa para centrarte en la redacción vigente; `base="TS"` para doctrina casacional) + `leer_sentencias` (`parrafos=3`).
- **Revisión del documento** → cada redactor del equipo pasa `verificar_escrito` solo sobre sus frases con normas, y el ensamblado rechaza cualquier ECLI o ROJ que ningún redactor leyera; `buscar_por_cita` se usa solo con un ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Cita la ley de emprendedores como «Ley 14/2013, de 27 de septiembre» **en cada mención** (o «la misma ley» justo después): con «Ley 14/2013» a secas `verificar_escrito` la confunde con otra Ley 14/2013 autonómica y da por inexistentes sus artículos. Si citas una letra, escríbela detrás de la norma («artículo 62.3 de la Ley 14/2013, de 27 de septiembre, letra f)»): con «62.3.f) de la Ley…» atribuye el artículo a la norma citada antes. `verificar_escrito` no reconoce los reglamentos de la Unión (por ejemplo, el Código de fronteras Schengen): cítalos sin número de artículo en cifras o comprueba que no atribuya el artículo a otra norma.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

## Cuándo usarla

- Nacional de un tercer país que quiere entrar o residir en España, o que ya reside, en uno de los
  supuestos del art. 61.1 que conserven regulación: emprendedor, profesional altamente cualificado,
  investigador, trabajador en traslado intraempresarial o teletrabajador de carácter internacional.
- Familiares que le acompañan o se reúnen con él (art. 62.4).
- Renovación de estas autorizaciones y recurso contra su denegación.

No la uses para ciudadanos de la Unión ni para quienes tengan derechos de libre circulación
equivalentes (art. 61.2). Para un empleo que no encaja en estas figuras, usa
`trabajo-cuenta-ajena`; para un negocio sin informe de ENISA, `trabajo-cuenta-propia`; para vivir
de rentas sin trabajar, `residencia-no-lucrativa`. Si aún no está claro qué vía conviene, usa
antes `informe-viabilidad-extranjeria`.

## Datos que hay que reunir antes de redactar

Saca estos datos de la documentación aportada, por este orden (paso 2 de `redaccion-rapida`). Si falta un dato imprescindible (★) que bloquee el escrito, pídelos todos a la vez en una única ronda de no más de cuatro preguntas; lo demás queda como `[PENDIENTE: dato]`.

1. ★ Figura que se pretende y trámite: visado desde el extranjero, autorización estando en España
   de forma regular, renovación o recurso. Si hay resolución, texto íntegro y fecha de
   notificación.
2. ★ Solicitante: nacionalidad, edad, país de residencia de los dos últimos años, antecedentes
   penales (dos años y declaración de cinco), situación en España, seguro de enfermedad y recursos
   económicos para él y su familia (art. 62.3).
3. ★ Según la figura:
   - teletrabajo: empresa o empresas extranjeras, antigüedad de su actividad, tipo de relación
     (laboral o profesional), desde cuándo, autorización para trabajar a distancia, porcentaje de
     trabajo para clientes españoles, titulación o años de experiencia, participación en el
     capital de la empresa (arts. 74 bis y 74 ter);
   - altamente cualificado: contrato u oferta firme, duración, salario bruto anual, título y nivel,
     o años de experiencia, profesión regulada y homologación (arts. 71 y 71 bis);
   - emprendedor: proyecto, perfil y participación de cada socio, plan de negocio y financiación
     (art. 70.2);
   - investigador: entidad, convenio de acogida o contrato, doctorado o titulación (art. 72);
   - traslado intraempresarial: grupo, empresa de origen y de destino, relación previa y su
     duración, puesto (directivo, especialista o en formación), duración del traslado (art. 73).
4. ★ Familiares: vínculo, edad, dependencia económica, si solicitan a la vez o después.
5. Solo renovación ★: fecha de caducidad, mantenimiento de las condiciones, periodos sin empleo.

## Requisitos y comprobaciones

### A. Qué supuestos siguen vigentes

- Lee el art. 61.1 y, antes de hablar de inversores, los arts. 63 a 67. A 27/09/2026 el conector
  los devuelve «sin contenido» desde el 3/04/2025 por la disposición final 21.1 de la Ley
  Orgánica 1/2025. El art. 61.1.a) sigue enumerando a los inversores, pero su régimen no existe:
  no ofrezcas la residencia para inversores como vía nueva. La nota del conector reproduce entre
  comillas el texto derogado de cada artículo: no lo cites como vigente.
- Si el cliente pide la «golden visa» o la residencia por inversión (inmueble, depósito, acciones,
  deuda pública) sin solicitud presentada antes del 3/04/2025, no redactes ninguna solicitud:
  entrega la nota de reconducción del apartado «Documento que se entrega» con las vías que sí
  existen según sus hechos (residencia no lucrativa, arts. 61 y 62 del Reglamento; emprendedor,
  arts. 69 y 70; teletrabajo o alta cualificación si hay relación real), leídas con el conector.
  La compra de un inmueble no da derecho a residir, pero puede servir para acreditar patrimonio.
- Solicitudes de inversor anteriores a esa fecha o renovaciones de autorizaciones de inversor ya
  concedidas: su régimen transitorio no lo devuelve el conector (`leer_boe` solo trae el principio
  de la Ley Orgánica 1/2025). Aplica la puerta y dile al abogado qué falta. Si no hubo solicitud
  anterior, el régimen transitorio no hace falta: dilo así, sin describir su contenido.
- El art. 68 (entrada para inicio de actividad empresarial) está suprimido.

### B. Requisitos generales (art. 62)

- Visados de residencia y autorizaciones (art. 62.3): no estar irregular en España, ser mayor de
  dieciocho años, sin antecedentes en España ni en los países de residencia de los dos últimos
  años más declaración responsable de cinco años, no ser rechazable, seguro público o privado de
  entidad autorizada en España, recursos económicos suficientes para él y su familia, tasa.
- Las cuantías de recursos y varios criterios prácticos están en instrucciones dictadas al
  amparo de una disposición adicional de la Ley 14/2013 que el conector no devuelve. Dile al
  abogado que compruebe la instrucción vigente en la sede oficial; no escribas cuantías de
  memoria. Si la cuantía es decisiva y no se aporta, deja el marcador y avisa.
- Denegación o revocación por amenaza para el orden público, la seguridad o la salud pública con
  base en un informe policial, del Centro Nacional de Inteligencia o de Seguridad Nacional
  (art. 62.7).
- Familiares (art. 62.4): cónyuge o pareja, hijos menores o mayores dependientes sin unidad
  familiar propia y ascendientes a cargo; solicitud conjunta y simultánea o sucesiva, con los
  requisitos del art. 62.3.

### C. Requisitos por figura

| Figura | Preceptos | Puntos que deciden |
|---|---|---|
| Teletrabajo internacional | 74 bis a 74 quinquies | Trabajo a distancia solo para empresas radicadas fuera de España; si es actividad profesional, clientes españoles hasta el porcentaje del art. 74 bis.1; titulación de centro de reconocido prestigio o tres años de experiencia; actividad real de la empresa durante al menos un año; relación de al menos tres meses; documento que permite el trabajo en remoto |
| Altamente cualificado | 71 y 71 bis | Tarjeta azul-UE: cualificación del art. 71.2.a), contrato u oferta firme de al menos seis meses y umbral salarial reglamentario; modalidad nacional: titulación o experiencia del art. 71.2.b) según las instrucciones |
| Emprendedor | 69 y 70 | Actividad innovadora o de especial interés económico con informe favorable de ENISA, preceptivo, emitido en diez días hábiles; perfil, plan de negocio y valor añadido |
| Investigador | 72 | Modalidad UE (doctorado o titulación de acceso y convenio de acogida con su contenido mínimo) o nacional; posible prórroga de doce meses para buscar empleo o emprender (art. 72.9) |
| Traslado intraempresarial | 73 y 74 | Actividad empresarial real; titulación o tres años de experiencia; relación previa y continuada de tres meses con el grupo; documentación del traslado; modalidad UE (directivo, especialista, en formación) o nacional |

- Duraciones y renovaciones: léelas en cada artículo (por ejemplo, arts. 69.1, 71.3, 72.3,
  73.3 y 74 quinquies). No las generalices.
- El umbral salarial de la Tarjeta azul-UE se define reglamentariamente (art. 71 bis.1.c): no lo
  cuantifiques sin la norma que lo fije; pide al abogado la fuente oficial. Si el salario puede no
  alcanzarlo, dilo en el resumen y plantea la modalidad nacional (art. 71.2.b) como alternativa
  o petición subsidiaria. Comprueba además el salario de tabla del convenio aplicable.
- En el emprendedor, el art. 69.1 prevé una única instancia de autorización y visado para quien
  está fuera y el art. 70.1 que pida el visado tras concederse la autorización: sigue la hoja
  informativa oficial vigente y explícale al abogado la discrepancia.

### D. Procedimiento, plazos y recursos

- Autorización: se tramita por la Unidad de Grandes Empresas y Colectivos Estratégicos, por medios
  telemáticos, y la concede la Dirección General de Migraciones (art. 76.1). La solicitud prorroga
  la situación de estancia o residencia hasta que se resuelva.
- Si la autorización se pide desde España, el solicitante debe estar en situación regular al
  presentarla (por ejemplo, art. 74 quinquies.1): calcula la fecha en que termina su estancia o
  residencia (estancia de corta duración: noventa días en ciento ochenta, art. 6 del Reglamento (UE)
  2016/399, que `buscar_articulo` devuelve) y da esa fecha como límite de presentación.
- Plazo de resolución de veinte días desde la presentación electrónica; el silencio es
  estimatorio (art. 76.1). Visados: diez días hábiles, salvo consulta previa del Código de
  visados (art. 75.5).
- Tarjeta de identidad de extranjero si la vigencia supera seis meses (art. 76.2). El pasaporte
  basta para el alta en la Seguridad Social durante los seis primeros meses (art. 76.5).
- Renovación: por dos años si se mantienen las condiciones; la solicitud prorroga la autorización
  y cabe presentarla hasta noventa días después de su caducidad, con posible sanción (art. 76.3).
  Comprueba los plazos específicos de cada figura (art. 71.3, sesenta días antes; art. 74 quater.3,
  sesenta días antes de caducar el visado de teletrabajo).
- Recurso: las resoluciones de autorización admiten recurso de alzada (art. 76.1; LPAC arts. 121 y
  122: un mes contra acto expreso; puede presentarse ante el órgano que dictó el acto). Contra la
  resolución de la alzada, contencioso en dos meses (LJCA art. 46). Determina el órgano judicial
  con la LJCA y con jurisprudencia reciente de competencia antes de encabezar. Contra la denegación
  de un visado, sigue el pie de recursos de la resolución consular y compruébalo con la LPAC y la
  LJCA.

### E. Causas de denegación en la jurisprudencia

En teletrabajo: el solicitante controla la empresa extranjera y la Administración niega que exista
relación laboral, relación de menos de tres meses, empresa sin un año de actividad, recursos
inferiores a los de la instrucción o perfil que no encaja con la titulación o la experiencia. En
alta cualificación y traslados: puesto que no es de alta cualificación, falta de relación previa
con el grupo o dudas sobre la empresa. En emprendedores: informe desfavorable de ENISA que el plan
de negocio no rebate.

## Estrategia y jurisprudencia

1. Elige la figura por los hechos, no por el nombre que usa el cliente: quien trabaja para una
   empresa española no es teletrabajador internacional; quien controla la empresa extranjera
   debe acreditar una relación profesional real o elegir otra vía.
2. Prepara la prueba de cada punto de la tabla del apartado C con documentos fechados: contratos,
   certificados de la empresa, cotizaciones o certificados de cobertura de Seguridad Social que
   exija la instrucción, títulos y cartas de experiencia.
3. Busca la doctrina con las consultas de la lista y, según el caso,
   `consulta="traslado intraempresarial autorización residencia denegación"` o
   `consulta="teletrabajo carácter internacional administrador participaciones relación laboral ajenidad"`, con
   `jurisdiccion="CONTENCIOSO"` y `base="AN"`. Lee con `leer_sentencias` (`parrafos=3`) solo lo
   que vayas a citar y cita fundamentos, nunca los hechos de aquellos solicitantes.
4. Si la sentencia reproduce una instrucción administrativa, no tomes sus cifras como vigentes:
   la instrucción puede haber cambiado. Pide al abogado la versión vigente.
5. En la alzada, rebate cada motivo con el precepto leído y el documento que lo prueba y, si la
   resolución llega después del plazo de veinte días, comprueba si ya había silencio estimatorio.

## Documento que se entrega

Formato, destinatario, citas y datos según `references/formato-y-organos.md`. Los formularios, la
presentación electrónica y las tasas se obtienen en la sede oficial: no indiques modelos, códigos
ni importes.

1. **Solicitud** — `solicitud-<figura>-ley-14-2013-<apellido>-<AAAAMMDD>.docx` (por ejemplo,
   `solicitud-teletrabajo-ley-14-2013-...`), escrito de presentación y memoria dirigido a la
   UNIDAD DE GRANDES EMPRESAS Y COLECTIVOS ESTRATÉGICOS (autorización) o a la OFICINA CONSULAR DE
   ESPAÑA EN [CIUDAD] (visado):
   - comparecencia del solicitante o de su representante y, si procede, de la empresa;
   - EXPONE: figura elegida y por qué encaja; un hecho por cada requisito general del art. 62.3 y
     por cada punto de la figura, con su prueba; familiares que acompañan (art. 62.4);
   - FUNDAMENTOS DE DERECHO: Ley 14/2013, arts. 61, 62, los de la figura, 75 (si se pide visado) y
     76, con su texto vigente;
   - SOLICITA la concesión para el titular y los familiares;
   - relación numerada de documentos.
2. **Renovación** — `renovacion-<figura>-ley-14-2013-<apellido>-<AAAAMMDD>.docx`, con el
   mantenimiento de cada condición y su prueba.
3. **Recurso de alzada** — `recurso-alzada-ley-14-2013-<apellido>-<AAAAMMDD>.docx`, dirigido al
   órgano que indique el pie de recursos: acto recurrido y fecha de notificación; hechos; un
   fundamento por motivo de denegación, con doctrina literal y prueba; SOLICITA; otrosí de prueba.
4. **Nota de reconducción** — `nota-reconduccion-ley-14-2013-<apellido>-<AAAAMMDD>.docx`, cuando la
   figura pedida no existe o no encaja (inversores, teletrabajo de quien controla la empresa...):
   consulta; comprobación de vigencia con la nota del conector y su fecha; vías alternativas con
   sus requisitos leídos y su riesgo; conclusión y próximos pasos, remitiendo a la skill que
   corresponda (`residencia-no-lucrativa`, `trabajo-cuenta-propia`, `informe-viabilidad-extranjeria`).
   Es una nota, no un escrito: sin súplica, firma del abogado.

**Reparto para la redacción rápida:** solicitud: 01 comparecencia y hechos (uno por requisito del art. 62.3 y por punto de la figura); 02 fundamentos de derecho (Ley 14/2013, arts. 61, 62, los de la figura, 75 y 76); 03 solicita, familiares y relación de documentos. Renovación y alzada: una sección por condición mantenida o por motivo de denegación, más cierre. La nota de reconducción la redacta el director sin equipo.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Vigencia de la figura comprobada con `buscar_articulo`; nada sobre inversores sin leer los
      arts. 63 a 67; si hubo solicitud anterior al 3/04/2025 o es una renovación, sin el régimen
      transitorio (si no se obtiene, puerta).
- [ ] Cada artículo citado se leyó en esta conversación con su redacción vigente.
- [ ] Ninguna cuantía de recursos ni umbral salarial escrito sin norma o instrucción facilitada.
- [ ] Cada ECLI se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre sus frases con normas y sus avisos corregidos.
- [ ] Marcadores en los datos no facilitados; nada inventado.
- [ ] Plazos con fecha y precepto: fin de la estancia regular si se pide desde España, renovación
      (art. 76.3 y el de la figura) o alzada (LPAC art. 122).
- [ ] Cada mención de la ley de emprendedores lleva «de 27 de septiembre» (o «la misma ley»).
- [ ] Resumen para el abogado según el apartado 7 del formato, con los riesgos y el próximo paso.
