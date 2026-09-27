---
name: proteccion-internacional-apatridia
description: >-
  Prepara en Word los escritos de protección internacional (asilo y protección subsidiaria) y de
  apatridia - alegaciones para la solicitud y la entrevista, petición de reexamen en frontera o CIE,
  recurso de reposición, recurso contencioso con petición de permanencia o suspensión, razones
  humanitarias subsidiarias y solicitud del estatuto de apátrida. Aplica la Ley 12/2009 y, para
  solicitudes formalizadas desde el 12/06/2026, los Reglamentos (UE) 2024/1347, 2024/1348 y 2024/1351
  del Pacto de Migración y Asilo. Úsala cuando el abogado diga «asilo», «refugiado», «protección
  subsidiaria», «inadmisión a trámite», «solicitud en frontera», «aeropuerto», «CIE», «reexamen», «me
  han denegado el asilo», «razones humanitarias», «Pacto europeo», «apátrida» o «apatridia». Para
  arraigo tras la denegación o expulsión usa las skills de esas materias.
---

# Protección internacional y estatuto de apátrida

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen aplicable según la fecha de formalización** → `buscar_articulo` (`ley="Reglamento (UE) 2024/1348"`, `articulo="79"`; `ley="Reglamento (UE) 2024/1351"`, `articulo="85"`; `ley="Reglamento (UE) 2024/1347"`, `articulo="41"`) y `buscar_boe` (`consulta="protección internacional"`, `desde="2024-06-01"`) para saber si España ha adaptado su ley.
- **Requisitos de refugiado y de protección subsidiaria, exclusión y denegación** → `buscar_articulo` (`ley="Ley 12/2009"`, artículos `"3"`, `"4"`, `"6"` a `"15"` y `"26"`; `ley="Reglamento (UE) 2024/1347"`, artículos `"3"`, `"4"`, `"9"` y `"15"`).
- **Procedimiento: presentación, entrevista, admisión, frontera y CIE, urgencia, plazos y silencio** → `buscar_articulo` (`ley="Ley 12/2009"`, artículos `"16"` a `"25"` y `"27"`; `ley="Reglamento (UE) 2024/1348"`, artículos `"10"` a `"14"`, `"26"` a `"28"`, `"35"`, `"38"`, `"39"`, `"42"` a `"44"`, `"51"`, `"55"` y `"73"`).
- **Recursos, permanencia y suspensión** → `buscar_articulo` (`ley="Ley 12/2009"`, artículos `"21"`, `"22"` y `"29"`; `ley="Reglamento (UE) 2024/1348"`, artículos `"67"` y `"68"`; `ley="LJCA"`, artículos `"9"`, `"11"`, `"46"`, `"78"`, `"130"` y `"135"`; `ley="LOPJ"`, artículos `"66"` y `"95"`; `ley="LPAC"`, artículos `"124"` y `"125"`).
- **Razones humanitarias y apatridia** → `buscar_articulo` (`ley="Ley 12/2009"`, artículos `"37"` y `"46"`; `ley="BOE-A-2024-24099"`, `articulo="128"`; `ley="LOEX"`, `articulo="34"`, base legal del estatuto de apátrida; `ley="Real Decreto 865/2001"`, artículos `"1"` a `"5"`, `"7"` a `"9"`, `"11"`, `"13"`, `"15"` y `"16"`; `ley="LPAC"`, `articulo="66"`, al que hoy remite el art. 3.1 del RD 865/2001).
- **Doctrina y aplicación del Pacto** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`; `base="AN"` con `fecha_desde="12/06/2026"` para ver cómo se aplican los Reglamentos; `base="TS"` para la doctrina; `base="TJUE"` para la interpretación del Derecho de la Unión) y `leer_sentencias` (`parrafos=3`).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación. `verificar_escrito` no reconoce los Reglamentos de la Unión: sus artículos los atribuye a la ley española citada más cerca (Ley 12/2009, Real Decreto 1155/2024) o al Código Penal, y según el número los da por «existentes», con «posible disonancia» o «no localizados». Ninguno de esos resultados vale para una cita de un Reglamento (UE): compruébala siempre con `buscar_articulo`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar o el requisito que hay que comprobar), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Preparar las alegaciones escritas que fundamentan la solicitud y la preparación de la entrevista.
- Reaccionar en horas a una inadmisión o denegación en puesto fronterizo o en un CIE (petición de reexamen).
- Recurrir en reposición o en vía contencioso-administrativa una inadmisión, una denegación o un archivo, pidiendo la permanencia o la suspensión.
- Pedir con carácter subsidiario la autorización por razones humanitarias.
- Solicitar el estatuto de apátrida o recurrir su denegación.

Usa otra skill del plugin cuando:

- el problema sea el internamiento en el CIE en sí (auto, cese, habeas corpus) → `internamiento-cie`; la solicitud de asilo presentada desde el CIE sí se trabaja aquí;
- haya un expediente de expulsión o sancionador abierto → `expulsion-procedimiento-sancionador`;
- el Ministro del Interior ya autorizó la permanencia y hay que pedir la autorización de residencia por razones humanitarias del art. 128, o se invocan otras razones humanitarias ajenas al asilo → `razones-humanitarias`;
- el solicitante denegado busque un arraigo → la skill de arraigo que corresponda (el art. 126 del Reglamento excluye a quien sigue siendo solicitante);
- se trate de la nacionalidad de origen del nacido en España de padres apátridas → `nacionalidad-otras-vias`; de la nacionalidad por residencia del refugiado → `nacionalidad-residencia`.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. Si falta un dato imprescindible, pregunta y espera. La información del procedimiento es confidencial (`Ley 12/2009`, art. 16.4): no la uses en consultas y no incluyas nombres en ellas.

1. **Fase y resolución** (imprescindible): qué se ha presentado, qué se ha notificado, órgano que resuelve, texto íntegro y pie de recursos.
2. **Fechas con hora** (imprescindible): entrada en España o llegada al puesto fronterizo, formulación, registro y formalización de la solicitud, notificación de cada resolución. En frontera y CIE los plazos se cuentan de momento a momento: pide la hora exacta.
3. **Lugar**: territorio, puesto fronterizo, CIE o embajada; si hay orden de expulsión o devolución en curso.
4. **Relato de persecución o daño grave** (imprescindible para el fondo): qué pasó, quién lo hizo, cuándo, por qué motivo (raza, religión, nacionalidad, opinión política, grupo social, género u orientación), si pidió protección a las autoridades, si podía trasladarse dentro de su país, documentos y testigos.
5. **Vulnerabilidad**: menores, víctimas de trata, tortura o violencia sexual, discapacidad, embarazo, edad avanzada (`Ley 12/2009`, art. 46).
6. **Información del país de origen**: informes que aporte el abogado. Jurisprudenciator no la proporciona; no afirmes hechos sobre la situación del país sin una fuente aportada o sin una sentencia leída que los recoja (y entonces cita la sentencia).
7. **Apatridia**: país de nacimiento y de residencia habitual, nacionalidad de los progenitores, gestiones hechas ante consulados, documentos de identidad o de viaje.

## Requisitos y comprobaciones

### Paso cero: qué régimen se aplica

- Lee `Reglamento (UE) 2024/1348`, art. 79: es aplicable desde el 12/06/2026 a las solicitudes **formalizadas** desde esa fecha; las formalizadas antes se rigen por la Directiva 2013/32/UE (y por la Ley 12/2009 interpretada conforme a ella). El art. 79.2 adelanta a febrero de 2026 algunas reglas de país de origen seguro y tercer país seguro: léelas si el caso las toca.
- `Reglamento (UE) 2024/1351`, art. 85: aplicable desde el 12/06/2026; sustituye al sistema de Dublín. La `Ley 12/2009`, art. 20.1.a), aún remite al Reglamento (CE) 343/2003: señala que esa remisión está superada.
- `Reglamento (UE) 2024/1347`: su art. 41 deroga la Directiva 2011/95/UE con efecto desde el 12/06/2026. Si `buscar_articulo` no devuelve un texto legible del artículo final, apóyate en el art. 41 y dilo.
- La Ley 12/2009 conserva su redacción anterior al Pacto. Antes de cada asunto, repite la consulta `buscar_boe` de la lista; si aparece una ley de adaptación, léela y aplícala antes que esta guía.
- Los Reglamentos son directamente aplicables y prevalecen sobre la ley española incompatible. Conflictos ya comprobados que debes señalar en el escrito y al abogado:
  - **Silencio en la admisión:** la Ley dice que la falta de notificación de la inadmisión en un mes determina la admisión (art. 20.2); el Reglamento fija dos meses, prorrogables, y dice expresamente que la solicitud no se considera admisible por falta de resolución en plazo (art. 35.1 y 35.2).
  - **Plazo de recurso:** el Reglamento obliga a los Estados a fijar plazos de entre cinco y diez días (inadmisión, retirada implícita, infundada o manifiestamente infundada en supuestos del art. 42.1 o 42.3) o de entre dos semanas y un mes (resto) (art. 67.7), contados desde la notificación (art. 67.8) y con el cómputo del art. 73. Si no hay ley española que los fije, la ley nacional sigue diciendo un mes para la reposición (`LPAC`, art. 124) y dos meses para el contencioso (`LJCA`, art. 46). No elijas el plazo largo: recomienda actuar dentro del más corto que pueda aplicarse y explica el riesgo.
  - **Permanencia durante el recurso:** regla general y excepciones del art. 68 del Reglamento; en las excepciones, el solicitante dispone al menos de cinco días desde la notificación para pedir al tribunal que le permita permanecer (art. 68.5.a). La Audiencia Nacional ya resuelve estas peticiones con el art. 68 en solicitudes posteriores al 12/06/2026: compruébalo con `buscar_sentencias` (`consulta="Reglamento 2024/1348 artículo 68 medida cautelar permanencia"`, `base="AN"`, `fecha_desde="12/06/2026"`).
  - **Procedimiento fronterizo:** frente a los cuatro días del art. 21 de la Ley, el Reglamento prevé formalización en cinco días y una duración máxima de doce semanas (arts. 43 a 54, en especial 51). No es un conflicto puro: el art. 51.2, párrafo segundo, encarga a los Estados miembros fijar la duración de la fase de examen dentro de esas doce semanas. Mientras no haya ley de adaptación, sostén que esa disposición nacional es el art. 21 de la Ley (cuatro días, reexamen en dos y efecto del art. 21.5), y avisa al abogado de que la Administración puede sostener lo contrario. El Reglamento no prevé un reexamen administrativo: tras su desestimación, la permanencia durante el recurso judicial depende del art. 68.3 a 68.5.

**Cuadro de plazos por fase** (verificado; relee cada precepto antes de dar una fecha al abogado):

| Fase | Ley 12/2009 (formalizadas antes del 12/06/2026) | Reglamento (UE) 2024/1348 (desde el 12/06/2026) |
|---|---|---|
| Presentar la solicitud | Sin demora y máximo un mes desde la entrada o los hechos (art. 17.2) | Registro en cinco días desde la formulación; formalización en veintiún días desde el registro (arts. 27.1 y 28.1) |
| Admisión en territorio | Un mes; sin notificación, admitida (art. 20.2) | Dos meses, prorrogables dos; sin admisión por silencio (art. 35.1 y 35.2) |
| Frontera o CIE | Cuatro días; reexamen en dos días con efecto suspensivo (arts. 21 y 25.2) | Formalización en cinco días; todo el procedimiento en doce semanas (art. 51) |
| Resolver el fondo | Seis meses; desestimación presunta (art. 24.3); urgencia a la mitad (art. 25.4) | Seis meses, prorrogables seis; acelerado tres (art. 35.3 a 35.5) |
| Recurrir | Reposición en un mes (`LPAC`, art. 124); contencioso en dos meses (`LJCA`, art. 46) | Horquillas del art. 67.7 pendientes de fijación nacional: actúa dentro del plazo más corto posible |
| Pedir permanencia durante el recurso | Medida cautelar urgente (`LJCA`, art. 135; Ley, art. 29.2) | Al menos cinco días desde la notificación en las excepciones del art. 68.3 (art. 68.5.a) |

### Requisitos sustantivos

- Refugiado: `Ley 12/2009`, art. 3; `Reglamento (UE) 2024/1347`, arts. 3.5, 9 y siguientes. Actos y motivos de persecución (Ley, arts. 6 y 7), agentes de persecución y de protección (arts. 13 y 14), necesidades surgidas in situ (art. 15).
- Protección subsidiaria: `Ley 12/2009`, arts. 4 y 10; `Reglamento (UE) 2024/1347`, art. 15 (pena de muerte, tortura o tratos inhumanos, amenaza grave e individual por violencia indiscriminada en conflicto armado).
- Exclusión y denegación: `Ley 12/2009`, arts. 8, 9, 11 y 12.
- Prueba: basta que aparezcan indicios suficientes (`Ley 12/2009`, art. 26.2); la persecución ya sufrida es indicio serio y las declaraciones no respaldadas no exigen más prueba si se cumplen las condiciones del `Reglamento (UE) 2024/1347`, art. 4.4 y 4.5. Construye la credibilidad con esas condiciones: esfuerzo auténtico, entrega de todo lo disponible, coherencia y momento de la solicitud.
- Orientación sexual, identidad de género, religión o convicciones: el `Reglamento (UE) 2024/1347`, art. 10.3, prohíbe esperar que el solicitante modifique su comportamiento o identidad, o se abstenga de prácticas inherentes a ella, para evitar la persecución; su art. 10.1.d), párrafo segundo, incluye el grupo definido por la orientación sexual (en la Ley, arts. 3 y 7.1.e). La doctrina del TJUE sobre discreción y sobre credibilidad en estos casos interpreta la Directiva 2004/83/CE: dilo al citarla y conéctala con el artículo del Reglamento que la recoge.
- Alternativa de protección interna (`Reglamento (UE) 2024/1347`, art. 8): si el agente de persecución es el Estado, se presume que no hay protección efectiva y no se examina (art. 8.2); la carga de demostrar la alternativa recae en la autoridad decisoria (art. 8.3); y deben valorarse las circunstancias personales, incluidos la orientación sexual y el género (art. 8.5).
- Motivos típicos de denegación: inverosimilitud o contradicciones, falta de individualización, persecución por particulares sin acreditar falta de protección estatal (contesta con la protección «efectiva y de carácter no temporal» y el acceso a ella del art. 7.2 del Reglamento (UE) 2024/1347), alternativa de protección interna, país de origen seguro, solicitud tardía. Si la resolución califica los hechos de «delincuencia común», recuerda que la protección subsidiaria no exige un motivo de la Convención (Ley, arts. 4 y 10; Reglamento (UE) 2024/1347, arts. 3.6 y 15) y que el daño puede proceder de agentes no estatales (Ley, art. 13.c; Reglamento, art. 6.c).

### Procedimiento (Ley 12/2009 y, desde el 12/06/2026, Reglamento (UE) 2024/1348)

- Presentación: derecho a solicitar y asistencia jurídica gratuita, preceptiva en frontera (Ley, art. 16.2); comparecencia sin demora y como máximo en un mes desde la entrada o desde los hechos (art. 17.2); entrevista individual con tratamiento diferenciado (art. 17.4 y 17.5). Con el Reglamento: registro en cinco días desde la formulación (art. 27.1) y formalización en veintiún días desde el registro (art. 28.1); entrevistas de admisibilidad y sustantiva (arts. 11 y 12) con sus garantías (arts. 13 y 14).
- Efectos: no devolución ni expulsión mientras se resuelve (Ley, art. 19.1); entrevista con abogado en frontera y CIE (art. 19.4); derecho de permanencia (Reglamento, art. 10).
- Inadmisión: causas de la Ley, art. 20.1, y del Reglamento, art. 38 (incluidas las solicitudes posteriores sin datos nuevos, art. 38.2, y arts. 55 y 56).
- Frontera y CIE (régimen de la Ley): inadmisión o denegación notificada en cuatro días (art. 21.1 y 21.2), ampliable a diez a petición del ACNUR (art. 21.3); petición de reexamen en dos días con efecto suspensivo, a resolver en otros dos (art. 21.4); si vencen los plazos sin notificación, procedimiento ordinario y entrada (art. 21.5); permanencia en dependencias (art. 22). Las solicitudes en CIE siguen el art. 21 (art. 25.2). El Supremo ha fijado cómo se computan esos plazos y el alcance de esa remisión: búscalo (`consulta="protección internacional CIE artículo 25.2 remisión artículo 21 cómputo plazo"`, `base="TS"`) y léelo antes de alegar el vencimiento.
  - Los cuatro días corren «desde su presentación» (art. 21.1 y 21.2) y se cuentan de momento a momento, no por días hábiles. La presentación es la comparecencia personal que inicia el procedimiento (art. 17.1), no la formalización mediante entrevista (art. 17.4): pide la hora de ambas y la diligencia policial que las acredite, calcula el vencimiento desde la comparecencia y avisa de que la Administración puede computarlo desde la formalización. La búsqueda de esa doctrina devuelve también autos de admisión de casación de 2026 que pueden revisarla: comprueba si ya hay sentencia.
  - En frontera, la inadmisión solo cabe por las causas del art. 20.1 de la Ley (art. 21.1) o, con el Reglamento, del art. 38 (art. 44.1.a). Si la resolución «inadmite» por razones de fondo (delincuencia común, protección estatal, traslado interno), alega que carece de causa legal y, subsidiariamente, que no es manifiestamente infundada (Ley, art. 21.2.b; Reglamento, art. 42.1; consulta `"inadmisión frontera alegaciones incoherentes inverosímiles"` con `base="TS"`).
- Ordinario y urgencia: propuesta de la Comisión Interministerial y resolución del Ministro del Interior; seis meses y posible desestimación presunta (art. 24.3); urgencia con plazos a la mitad (art. 25). Con el Reglamento: acelerado en tres meses (art. 35.3) y supuestos del art. 42; fondo en seis meses prorrogables (art. 35.4 y 35.5); manifiestamente infundada (art. 39.4).
- Archivo por retirada o desistimiento, presunto a los treinta días en los casos del art. 27 de la Ley; retirada explícita e implícita en el Reglamento (arts. 40 y 41).

### Recursos

- Las resoluciones ponen fin a la vía administrativa (salvo si hubo reexamen: la agota la resolución del reexamen); caben reposición potestativa y recurso contencioso (`Ley 12/2009`, art. 29.1). La petición de suspensión tiene la especial urgencia del `LJCA`, art. 135 (art. 29.2). La revisión por nuevos elementos (art. 29.3) remite a la ley de procedimiento derogada: aplica `LPAC`, art. 125.
- Órgano: la denegación la dicta el Ministro del Interior → Sala de lo Contencioso-Administrativo de la Audiencia Nacional (`LJCA`, art. 11.1.a; `LOPJ`, art. 66.a). La inadmisión está atribuida en primera instancia a los Juzgados Centrales (`LJCA`, art. 9.1.e), que hoy son la Sección de lo Contencioso-Administrativo del Tribunal Central de Instancia (`LOPJ`, art. 95.e), por procedimiento abreviado (`LJCA`, art. 78.1). Confirma el órgano con el pie de recursos y con una resolución reciente leída antes de encabezar.
- Asistencia jurídica gratuita e intérprete: `Ley 12/2009`, art. 16.2; `Reglamento (UE) 2024/1348`, arts. 15 a 19.

### Razones humanitarias

- `Ley 12/2009`, arts. 37.b) y 46.3, y `BOE-A-2024-24099`, art. 128.1.a): el Ministro del Interior puede autorizar la permanencia y abre la autorización de residencia temporal por razones humanitarias. Lee las notas «Téngase en cuenta que se declara la nulidad…» que devuelva `buscar_articulo` en cualquier artículo del Reglamento: el Supremo anuló en julio de 2026 preceptos e incisos (`BOE-A-2026-19632`) y lo anulado no se aplica.
- El Supremo ha fijado en 2026 doctrina sobre el régimen del art. 46.3 y sobre el tratamiento diferenciado, incluso de oficio, de los solicitantes vulnerables: búscala (`consulta="razones humanitarias artículo 46.3 Ley 12/2009 vulnerabilidad tratamiento diferenciado"`, `base="TS"`, `fecha_desde="01/01/2026"`) y léela. Pide siempre las razones humanitarias de forma expresa y subsidiaria, con los hechos de vulnerabilidad: en el régimen general del art. 46.3 la jurisprudencia no las examina si el recurrente no las plantea; en el de las personas vulnerables del art. 46.1 y 46.2, el Supremo obliga a la Administración a actuar de oficio, y conviene invocarlo además de pedirlas.
- La Audiencia Nacional ha dicho que las razones humanitarias quedan fuera del ámbito de los Reglamentos del Pacto: fundamenta la petición en la ley española (arts. 37.b y 46.3) y comprueba esa línea con una búsqueda reciente. El conector no devuelve el texto del Convenio Europeo de Derechos Humanos: invoca su art. 3 solo a través del párrafo literal de una sentencia leída que lo aplique.

### Apatridia (`Real Decreto 865/2001`)

- Base legal: el Ministro del Interior reconoce la condición de apátrida a quien, manifestando carecer de nacionalidad, reúna los requisitos de la Convención de 1954 (`LOEX`, art. 34.1). Cítalo junto al RD 865/2001: es el precepto que aplica la Audiencia Nacional.
- Concepto: persona a la que ningún Estado considera nacional suyo conforme a su legislación, según la Convención de Nueva York de 1954, con las exclusiones de su art. 1.2 (art. 1).
- Inicio de oficio o a instancia, manifestando carecer de nacionalidad; ante Oficinas de Extranjeros, Comisarías o la Oficina de Asilo y Refugio (art. 2). Contenido de la solicitud y domicilio para notificaciones (art. 3; su remisión al art. 70 de la Ley 30/1992 se entiende hecha hoy al `LPAC`, art. 66). Pruebas, informes de asociaciones e informes que puede recabar la Oficina (art. 8).
- Prueba de la falta de nacionalidad: reúne las respuestas escritas de los consulados de cada Estado con el que la persona tenga vínculo (nacimiento, residencia, progenitores) y los documentos de identidad o de viaje que tenga, y explica por qué no acreditan nacionalidad. Busca la doctrina del caso (`consulta="estatuto de apátrida <origen o colectivo> <documento que tiene>"`, `base="TS"` y `base="AN"` de los últimos años; para saharauis de Tinduf, `"estatuto de apátrida saharaui Tinduf pasaporte argelino"`): la Audiencia Nacional deniega cuando falta documentación de las autoridades del país de residencia o hay discrepancias de identidad.
- Plazo de un mes desde la entrada, o antes de que expire una estancia legal más larga, o desde las circunstancias sobrevenidas; fuera de él, o con orden de expulsión incoada, la solicitud se presume manifiestamente infundada (art. 4). Busca si esa presunción admite prueba en contrario (`consulta="apatridia plazo un mes artículo 4 Real Decreto 865/2001 manifiestamente infundada"`, `base="TS"`).
- Permanencia provisional (art. 5); instrucción por la Oficina de Asilo y Refugio con entrevista (art. 7); audiencia de quince días (art. 9); resolución del Ministro del Interior en tres meses, con desestimación si no se resuelve (art. 11.1); la denegación lleva al régimen general de extranjería (art. 11.4).
- Efectos: residencia, trabajo, tarjeta y documento de viaje (art. 13); revocación (art. 15) y cese (art. 16).
- Recurso: reposición y contencioso contra la resolución del Ministro; determina el órgano como en la denegación de asilo y confírmalo con jurisprudencia (`consulta="estatuto de apátrida denegación"`, `base="AN"`).

## Estrategia y jurisprudencia

1. **Plazo primero.** En frontera y CIE, calcula la hora límite del reexamen antes de nada y redacta el reexamen en el acto; el fondo se desarrolla después.
2. **Credibilidad.** Ordena el relato cronológicamente, explica cada contradicción señalada en la resolución, vincula cada hecho con un documento o un informe de país aportado y aplica las condiciones del art. 4.5 del Reglamento (UE) 2024/1347.
3. **Consultas útiles** (`jurisdiccion="CONTENCIOSO"`): `"denegación protección internacional <país> <motivo>"` con `base="AN"` y `fecha_desde` de los dos últimos años; `"inadmisión frontera alegaciones incoherentes inverosímiles"` con `base="TS"`; `"tutela cautelar asilo efecto suspensivo automático"` con `base="TS"`; `"violencia indiscriminada amenaza grave e individual"`, `"persecución por motivos de género grupo social determinado"` o `"alternativa de protección interna"` con `base="TJUE"`. Lee con `parrafos=3` y `terminos` del motivo.
4. **Pacto.** En solicitudes posteriores al 12/06/2026 cita el artículo del Reglamento y, junto a él, la norma española equivalente; si hay contradicción, invoca la primacía y explica cuál aplica.
5. **Cómo usar la doctrina:** premisa normativa con texto vigente, párrafo literal del fundamento con órgano, fecha y ECLI tal como los devolvió `leer_sentencias`, aplicación al relato del cliente y conclusión. Nunca reproduzcas el relato de hechos ni datos de solicitantes de otros pleitos.

## Documento que se entrega

Formato, citas y datos: `references/formato-y-organos.md`. Marca como CONFIDENCIAL en el encabezamiento los escritos de protección internacional (documentos A a D), con cita del art. 16.4 de la `Ley 12/2009`. La solicitud de apátrida (documento E) no lleva esa cita: el art. 16.4 es del procedimiento de asilo y el RD 865/2001 no tiene un precepto equivalente. Todo en Word. Reglas de cita en el texto del escrito:

- El Reglamento de extranjería se cita como «artículo N del Real Decreto 1155/2024»; con otra fórmula, `verificar_escrito` no identifica la norma.
- `verificar_escrito` no reconoce los Reglamentos (UE) 2024/1347, 2024/1348 y 2024/1351: atribuye sus artículos a la ley española más próxima en el texto o al Código Penal, y puede darlos por existentes, con «posible disonancia» o por no localizados. Comprueba cada una de esas citas con `buscar_articulo`, no las retires por el aviso, no des por buena una cita por un «existe» que en realidad es de otra norma, y dilo en el resumen.
- Dentro de una cita literal de una sentencia no corrijas nada, aunque tenga una errata (por ejemplo, una ley mal numerada): aclárala después, fuera de las comillas.
- Escribe siempre la norma junto al número del artículo («artículo 3.3 del Real Decreto 865/2001», no «el artículo 3.3» a secas): cuando falta, `verificar_escrito` atribuye el artículo a la última norma citada.

**A. Alegaciones de la solicitud** (`alegaciones-proteccion-internacional-<apellido>-<AAAAMMDD>.docx`): encabezamiento a la Oficina de Asilo y Refugio; comparecencia con `[NOMBRE Y APELLIDOS]`, `[NACIONALIDAD]`, `[NÚMERO DE EXPEDIENTE]`; hechos numerados (relato cronológico); fundamentos: régimen aplicable, refugio, subsidiariamente protección subsidiaria, subsidiariamente razones humanitarias, necesidades especiales; SOLICITA; relación de documentos e informes de país aportados.

**B. Petición de reexamen** (`reexamen-proteccion-internacional-<apellido>-<AAAAMMDD>.docx`): encabezamiento al Ministro del Interior a través del puesto fronterizo o CIE; resolución y hora de notificación; motivos breves y concretos contra cada razón de la inadmisión o denegación; petición de admisión o de tramitación ordinaria y de efecto suspensivo; firma y hora.

**C. Recurso de reposición** (`recurso-reposicion-proteccion-internacional-<apellido>-<AAAAMMDD>.docx`): órgano que dictó la resolución; hechos; fundamentos (procedencia y plazo, régimen aplicable, fondo, razones humanitarias); SOLICITA; documentos.

**D. Recurso contencioso con petición de permanencia o suspensión** (`recurso-contencioso-proteccion-internacional-<apellido>-<AAAAMMDD>.docx`): encabezamiento al órgano comprobado; comparecencia con representación (`LJCA`, art. 23); acto impugnado y fecha de notificación; petición de que se tenga por interpuesto y se reclame el expediente; OTROSÍ de permanencia (`Reglamento (UE) 2024/1348`, art. 68.4 y 68.5) o de medida cautelar urgente (`LJCA`, arts. 130 y 135; `Ley 12/2009`, art. 29.2) con el perjuicio concreto y la apariencia de buen derecho; documentos.

**E. Solicitud del estatuto de apátrida** (`solicitud-apatridia-<apellido>-<AAAAMMDD>.docx`): encabezamiento a la Oficina de Asilo y Refugio; comparecencia; manifestación expresa de carecer de nacionalidad; hechos (nacimiento, filiación, residencias, documentos de identidad o viaje, gestiones consulares negativas); fundamentos (art. 34.1 de la LOEX y arts. 1 a 4 del RD 865/2001, que remiten a la Convención de 1954; el conector no devuelve el texto de la Convención, así que no lo transcribas); petición de permanencia provisional (art. 5); SOLICITA; documentos.

## Comprobación final

- [ ] `estado` respondió y la puerta se cumplió en todo el trabajo.
- [ ] Régimen aplicable determinado con la fecha de formalización y el art. 79 del Reglamento (UE) 2024/1348; consulta `buscar_boe` repetida en este asunto.
- [ ] Cada artículo citado (Ley 12/2009, Reglamentos, LOEX, RD 865/2001, LJCA, LOPJ) se leyó en esta conversación con `buscar_articulo`; las citas de los Reglamentos de la Unión se comprobaron una a una porque `verificar_escrito` las atribuye a otras normas.
- [ ] En frontera o CIE: hora de la comparecencia y de la formalización, vencimiento de los cuatro días calculado de momento a momento desde la presentación, y causa de inadmisión contrastada con los arts. 20.1 de la Ley y 38 del Reglamento.
- [ ] CONFIDENCIAL con cita del art. 16.4 solo en los escritos de protección internacional, no en la solicitud de apátrida.
- [ ] Conflictos entre la Ley 12/2009 y los Reglamentos señalados en el escrito y al abogado.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; solo fundamentos jurídicos; ningún dato de otros solicitantes.
- [ ] Ninguna afirmación sobre el país de origen sin fuente aportada o sentencia leída.
- [ ] `verificar_escrito` pasado sobre el texto completo y corregidos los avisos. No identifica las citas con letra («artículo 20.1.b)», «artículo 11.1.a)») y las marca como no localizadas: compruébalas con `buscar_articulo` y no las cambies por ese aviso.
- [ ] Marcadores entre corchetes para todo dato no facilitado; ningún dato inventado.
- [ ] Plazo con fecha y, en frontera o CIE, hora inicial, precepto y límite calculado; si hay conflicto de plazos, se indica el más corto posible.
- [ ] Resumen para el abogado según el apartado 7 del formato: documento y órgano, plazo, riesgos (en especial la permanencia y la ejecución del retorno), tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene) y próximo paso.
