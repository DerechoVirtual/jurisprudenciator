---
name: indice
description: "Índice de los 54 formularios de víctimas y justicia restaurativa (Estatuto de la víctima, personación, prueba preconstituida de menores, mediación penal, acuerdos de reparación). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Víctimas y justicia restaurativa: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/victimas-y-justicia-restaurativa:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 47 | Acuerdo de reparación: el investigado pide remitir la causa a enjuiciamiento para conformarse | 2025 | `acuerdo-reparacion-investigado-pide-remitir-causa-47` |
| 49 | Acuerdo de reparación: conformidad del acusado ante el órgano de enjuiciamiento | 2025 | `acuerdo-reparacion-conformidad-acusado-ante-organo-49` |
| 59 | Víctima que se opone a la posible conformidad del acusado | 2025 | `victima-opone-posible-conformidad-acusado-59` |

## Recursos e impugnaciones (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 773 | Sobreseimiento libre: reforma y subsidiaria apelación de la víctima | 2016 | `sobreseimiento-libre-reforma-subsidiaria-apelacion-773` |
| 780 | Beneficios penitenciarios sobre el límite de cumplimiento: reforma y apelación de la víctima | 2016 | `beneficios-penitenciarios-sobre-limite-cumplimiento-780` |
| 782 | Libertad condicional del penado: reforma y apelación de la víctima | 2016 | `libertad-condicional-penado-reforma-apelacion-victima-782` |
| 783 | Tercer grado del penado: reforma y apelación de la víctima | 2016 | `tercer-grado-penado-reforma-apelacion-victima-783` |

## Escritos de acusación (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 418 | Prueba preconstituida de menor o discapacitado: la acusación pide reproducirla en juicio | 2020 | `prueba-preconstituida-menor-discapacitado-acusacion-pide-418` |

## Escritos de defensa (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 419 | Menor o discapacitado: la defensa propone que declare en el plenario | 2020 | `menor-discapacitado-defensa-propone-declare-plenario-419` |

## Resoluciones, actas y documentos (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 723 | Mediación penal: traslado inicial del expediente a los letrados de las partes | 2017 | `mediacion-penal-traslado-inicial-expediente-letrados-723` |
| 724 | Mediación penal: entrevista inicial informativa | 2017 | `mediacion-penal-entrevista-inicial-informativa-724` |
| 725 | Mediación penal: traslado del acuerdo a los letrados por el equipo de mediación | 2017 | `mediacion-penal-traslado-acuerdo-letrados-equipo-725` |
| 726 | Mediación penal: oficio del mediador al juez sobre si hubo acuerdo | 2017 | `mediacion-penal-oficio-mediador-juez-sobre-si-hubo-726` |
| 727 | Mediación penal: ficha del expediente | 2017 | `mediacion-penal-ficha-expediente-727` |
| 729 | Mediación penal: citación del abogado mediador a los letrados de las partes | 2017 | `mediacion-penal-citacion-abogado-mediador-letrados-729` |
| 730 | Mediación penal: diligencia de ingreso de cantidad tras el acuerdo | 2017 | `mediacion-penal-diligencia-ingreso-cantidad-tras-acuerdo-730` |
| 731 | Mediación penal: acuerdo por hurto a un familiar | 2017 | `mediacion-penal-acuerdo-hurto-familiar-731` |
| 732 | Mediación penal: acuerdo con cambio de calificación jurídica de los hechos | 2017 | `mediacion-penal-acuerdo-cambio-calificacion-juridica-732` |
| 734 | Mediación penal: acuerdo por impago de pensiones | 2017 | `mediacion-penal-acuerdo-impago-pensiones-734` |
| 738 | Mediación penal: cuestionario del mediador al mediado y su valoración | 2016 | `mediacion-penal-cuestionario-mediador-mediado-valoracion-738` |

## Solicitudes y escritos de trámite (33)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 46 | Acuerdo de reparación: el investigado pide el archivo de la causa penal | 2025 | `acuerdo-reparacion-investigado-pide-archivo-causa-penal-46` |
| 48 | Ejecutoria penal: el condenado pide la derivación a los servicios de justicia restaurativa | 2025 | `ejecutoria-penal-condenado-pide-derivacion-servicios-48` |
| 50 | Ejecutoria penal: alegaciones de la víctima a la impugnación de la liquidación de condena | 2025 | `ejecutoria-penal-alegaciones-victima-impugnacion-50` |
| 57 | Ejecutoria penal: la víctima contesta a las alegaciones del condenado | 2025 | `ejecutoria-penal-victima-contesta-alegaciones-condenado-57` |
| 64 | Menor afectado por un proceso penal: su representante pide que sea oído | 2024 | `menor-afectado-proceso-penal-representante-pide-sea-oido-64` |
| 66 | Persona mayor de edad afectada por un proceso penal: pedir ser oída | 2024 | `persona-mayor-edad-afectada-proceso-penal-pedir-ser-oida-66` |
| 77 | Acusación particular: pedir que la víctima declare por vía telemática (desde el 20 de marzo de 2024) | 2024 | `acusacion-particular-pedir-victima-declare-via-77` |
| 274 | Delito contra menor: la acusación particular niega la prescripción (hasta el 2 de abril de 2025) | 2022 | `delito-contra-menor-acusacion-particular-niega-274` |
| 352 | Menor de 14 años: la acusación pide su declaración como prueba preconstituida | 2021 | `menor-14-anos-acusacion-pide-declaracion-como-prueba-352` |
| 353 | Menor o discapacitado: la acusación pide que no se le cite al juicio oral | 2021 | `menor-discapacitado-acusacion-pide-no-le-cite-juicio-353` |
| 354 | Víctima menor o discapacitada: videoconferencia en el juicio oral (hasta el 19 de marzo de 2024) | 2021 | `victima-menor-discapacitada-videoconferencia-juicio-oral-354` |
| 355 | Víctima o perjudicado: personarse después del escrito de acusación | 2021 | `victima-perjudicado-personarse-despues-escrito-acusacion-355` |
| 356 | Víctima o perjudicado: personarse después de la sentencia | 2021 | `victima-perjudicado-personarse-despues-sentencia-356` |
| 417 | Víctima menor pero mayor de 14 años: la acusación pide su declaración como prueba preconstituida | 2020 | `victima-menor-pero-mayor-14-anos-acusacion-pide-417` |
| 421 | Víctima: videoconferencia en juicio mixto telemático-presencial (hasta el 19 de marzo de 2024) | 2020 | `victima-videoconferencia-juicio-mixto-telematico-421` |
| 728 | Justicia restaurativa: el abogado de la acusación pide al mediador estar presente | 2017 | `justicia-restaurativa-abogado-acusacion-pide-mediador-728` |
| 733 | Pedir la suspensión de la pena aportando acuerdo de reparación (condenado) | 2017 | `pedir-suspension-pena-aportando-acuerdo-reparacion-733` |
| 739 | Justicia restaurativa: el investigado pide derivar la causa penal | 2016 | `justicia-restaurativa-investigado-pide-derivar-causa-739` |
| 740 | Justicia restaurativa: la acusación particular pide derivar la causa penal | 2016 | `justicia-restaurativa-acusacion-particular-pide-derivar-740` |
| 747 | Padres de víctima mayor de edad: personación como acusación particular | 2016 | `padres-victima-mayor-edad-personacion-como-acusacion-747` |
| 748 | Víctima: pedir su evaluación antes de adoptar medidas de protección | 2016 | `victima-pedir-evaluacion-antes-adoptar-medidas-748` |
| 749 | Víctima: pedir que se prohíba a los medios grabar el juicio o difundir información | 2016 | `victima-pedir-prohiba-medios-grabar-juicio-difundir-749` |
| 750 | Víctima: pedir la devolución de bienes concretos incautados | 2016 | `victima-pedir-devolucion-bienes-concretos-incautados-750` |
| 751 | Víctima: pedir ser reconocida por el médico forense | 2016 | `victima-pedir-ser-reconocida-medico-forense-751` |
| 752 | Víctima: pedir que el juicio se celebre a puerta cerrada | 2016 | `victima-pedir-juicio-celebre-puerta-cerrada-752` |
| 753 | Víctima: pedir la traducción de una resolución | 2016 | `victima-pedir-traduccion-resolucion-753` |
| 754 | Víctima: pedir ir acompañada en su declaración ante el juez | 2016 | `victima-pedir-ir-acompanada-declaracion-ante-juez-754` |
| 774 | Víctima: oponerse a la libertad condicional del penado | 2016 | `victima-oponerse-libertad-condicional-penado-774` |
| 775 | Víctima: anunciar que va a recurrir un auto | 2016 | `victima-anunciar-va-recurrir-auto-775` |
| 776 | Víctima: informar al juez sobre la ejecución de la pena, la responsabilidad civil o el comiso | 2016 | `victima-informar-juez-sobre-ejecucion-pena-776` |
| 778 | Víctima: oponerse a los beneficios penitenciarios del penado | 2016 | `victima-oponerse-beneficios-penitenciarios-penado-778` |
| 779 | Víctima: pedir reglas de conducta para el penado en libertad condicional | 2016 | `victima-pedir-reglas-conducta-penado-libertad-779` |
| 781 | Víctima: pedir ser notificada de las resoluciones del proceso (hasta el 6 de octubre de 2022) | 2016 | `victima-pedir-ser-notificada-resoluciones-proceso-hasta-781` |

## Otros (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 777 | Víctima: oponerse a la clasificación en tercer grado del penado | 2016 | `victima-oponerse-clasificacion-tercer-grado-penado-777` |
