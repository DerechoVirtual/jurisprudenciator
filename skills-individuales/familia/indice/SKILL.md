---
name: indice
description: "Índice de los 216 formularios de familia (divorcio, convenio regulador, medidas, custodia, alimentos, filiación, gananciales). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Familia: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/familia:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (80)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 19 | Demanda de ejecución del convenio regulador del matrimonio de mutuo acuerdo | 2024 | `demanda-ejecucion-convenio-regulador-matrimonio-mutuo-19` |
| 20 | Demanda para pasar de custodia compartida a custodia individual | 2024 | `demanda-pasar-custodia-compartida-custodia-individual-20` |
| 36 | Demanda de modificación de medidas por falta de ratificación (art. 777.3 LEC) | 2024 | `demanda-modificacion-medidas-falta-ratificacion-art-777-36` |
| 39 | Divorcio con ratificación de medidas provisionales: demanda | 2024 | `divorcio-ratificacion-medidas-provisionales-demanda-39` |
| 43 | Demanda por discriminación en las relaciones familiares y lesión del honor | 2024 | `demanda-discriminacion-relaciones-familiares-lesion-43` |
| 64 | Demanda de cantidad tras romper la pareja de hecho | 2023 | `demanda-cantidad-tras-romper-pareja-hecho-64` |
| 80 | Demanda de tenencia y cuidado compartido de un animal de compañía | 2023 | `demanda-tenencia-cuidado-compartido-animal-compania-80` |
| 86 | Demanda de guarda y custodia a favor de un familiar o allegado | 2023 | `demanda-guarda-custodia-favor-familiar-allegado-86` |
| 95 | Divorcio contencioso con custodia individual de hijos menores: demanda | 2022 | `divorcio-contencioso-custodia-individual-hijos-menores-95` |
| 115 | Demanda de divorcio por violencia de género | 2022 | `demanda-divorcio-violencia-genero-115` |
| 122 | Demanda sobre custodia y traslado de restos mortales | 2022 | `demanda-sobre-custodia-traslado-restos-mortales-122` |
| 127 | Divorcio contencioso con custodia compartida de animal de compañía: demanda | 2022 | `divorcio-contencioso-custodia-compartida-animal-compania-127` |
| 152 | Demanda de oposición a la guarda administrativa de un menor con fines de adopción | 2021 | `demanda-oposicion-guarda-administrativa-menor-fines-152` |
| 163 | Divorcio contencioso sin separación previa, con medidas provisionales y litis expensas | 2021 | `divorcio-contencioso-sin-separacion-previa-medidas-163` |
| 179 | Impugnación de testamento por crisis de pareja del heredero instituido (Cataluña) | 2021 | `impugnacion-testamento-crisis-pareja-heredero-instituido-179` |
| 201 | Divorcio de mutuo acuerdo con división de cosa común: demanda (Cataluña) | 2020 | `divorcio-mutuo-acuerdo-division-cosa-comun-demanda-201` |
| 245 | Demanda de impugnación de testamento por ineficacia sobrevenida por divorcio | 2020 | `demanda-impugnacion-testamento-ineficacia-sobrevenida-245` |
| 269 | Demanda ejecutiva de la división de cosa común de finca que fue vivienda familiar | 2020 | `demanda-ejecutiva-division-cosa-comun-finca-fue-vivienda-269` |
| 271 | Demanda sumaria para restablecer el equilibrio en visitas o custodia compartida | 2020 | `demanda-sumaria-restablecer-equilibrio-visitas-custodia-271` |
| 272 | Demanda sumaria de visitas o custodia compartida con modificación de medidas económicas | 2020 | `demanda-sumaria-visitas-custodia-compartida-modificacion-272` |
| 279 | Demanda sumaria de modificación de la pensión de alimentos definitiva | 2020 | `demanda-sumaria-modificacion-pension-alimentos-279` |
| 291 | Demanda de divorcio de extranjeros residentes en Reino Unido y España, con alimentos y compensatoria | 2020 | `demanda-divorcio-extranjeros-residentes-reino-unido-291` |
| 314 | Divorcio contencioso con separación de hecho previa: demanda | 2020 | `divorcio-contencioso-separacion-hecho-previa-demanda-314` |
| 331 | Demanda de liquidación de gananciales con inventario de bienes | 2020 | `demanda-liquidacion-gananciales-inventario-bienes-331` |
| 347 | Modificación de medidas para extinguir el uso de la vivienda familiar por un tercero | 2019 | `modificacion-medidas-extinguir-uso-vivienda-familiar-347` |
| 360 | Nulidad de matrimonio de complacencia: demanda | 2019 | `nulidad-matrimonio-complacencia-demanda-360` |
| 368 | Demanda de modificación para extinguir la pensión de alimentos | 2019 | `demanda-modificacion-extinguir-pension-alimentos-368` |
| 370 | Demanda de filiación no matrimonial de la madre contra los herederos del presunto padre | 2019 | `demanda-filiacion-no-matrimonial-madre-contra-herederos-370` |
| 372 | Demanda verbal especial de alimentos entre hermanos | 2019 | `demanda-verbal-especial-alimentos-entre-hermanos-372` |
| 373 | Demanda verbal especial de extinción de la obligación de alimentos | 2019 | `demanda-verbal-especial-extincion-obligacion-alimentos-373` |
| 379 | Demanda de divorcio con litis expensas | 2019 | `demanda-divorcio-litis-expensas-379` |
| 383 | Demanda verbal de división de cosa común tras divorcio en separación de bienes | 2019 | `demanda-verbal-division-cosa-comun-tras-divorcio-383` |
| 387 | Demanda ordinaria de cantidad entre excónyuges en separación de bienes tras el divorcio | 2019 | `demanda-ordinaria-cantidad-entre-exconyuges-separacion-387` |
| 422 | Demanda de modificación de medidas fijadas por sentencia extranjera | 2018 | `demanda-modificacion-medidas-fijadas-sentencia-422` |
| 423 | Ejecución de auto de medidas provisionales: demanda | 2018 | `ejecucion-auto-medidas-provisionales-demanda-423` |
| 424 | Demanda verbal especial de alimentos del padre a cargo de los hijos | 2018 | `demanda-verbal-especial-alimentos-padre-cargo-hijos-424` |
| 425 | Demanda de guarda, custodia y alimentos de menor tras ruptura de unión de hecho | 2008 | `demanda-guarda-custodia-alimentos-menor-tras-ruptura-425` |
| 434 | Demanda de guarda y custodia a favor de los abuelos | 2018 | `demanda-guarda-custodia-favor-abuelos-434` |
| 435 | Divorcio contencioso con demandado en paradero desconocido: demanda | 2018 | `divorcio-contencioso-demandado-paradero-desconocido-435` |
| 441 | Divorcio contencioso con hijos mayores independientes e inventario de liquidación: demanda | 2018 | `divorcio-contencioso-hijos-mayores-independientes-e-441` |
| 442 | Demanda de modificación de medidas para la custodia compartida | 2018 | `demanda-modificacion-medidas-custodia-compartida-442` |
| 468 | Divorcio de mutuo acuerdo con liquidación de gananciales: demanda | 2017 | `divorcio-mutuo-acuerdo-liquidacion-gananciales-demanda-468` |
| 471 | Demanda de modificación de medidas sobre la patria potestad | 2017 | `demanda-modificacion-medidas-sobre-patria-potestad-471` |
| 477 | Demanda de modificación de medidas sobre uso de la vivienda familiar | 2016 | `demanda-modificacion-medidas-sobre-uso-vivienda-familiar-477` |
| 478 | Demanda de repetición contra el excónyuge por cuotas pagadas de la hipoteca del hogar | 2015 | `demanda-repeticion-contra-exconyuge-cuotas-pagadas-478` |
| 479 | Ejecución forzosa para la entrega del uso de la vivienda familiar | 2004 | `ejecucion-forzosa-entrega-uso-vivienda-familiar-479` |
| 499 | Demanda de modificación de medidas sobre régimen de visitas | 2017 | `demanda-modificacion-medidas-sobre-regimen-visitas-499` |
| 510 | Demanda de mutuo acuerdo sobre custodia, alimentos y relaciones con hijo menor y nasciturus | 2017 | `demanda-mutuo-acuerdo-sobre-custodia-alimentos-510` |
| 520 | Demanda de restitución de menor por sustracción internacional | 2016 | `demanda-restitucion-menor-sustraccion-internacional-520` |
| 529 | Demanda de separación contenciosa con custodia compartida y, subsidiariamente, exclusiva | 2016 | `demanda-separacion-contenciosa-custodia-compartida-529` |
| 530 | Demanda de divorcio contencioso con custodia compartida y, subsidiariamente, exclusiva | 2016 | `demanda-divorcio-contencioso-custodia-compartida-530` |
| 532 | Demanda de divorcio contencioso con custodia compartida | 2016 | `demanda-divorcio-contencioso-custodia-compartida-532` |
| 533 | Demanda de separación contenciosa con custodia compartida | 2016 | `demanda-separacion-contenciosa-custodia-compartida-533` |
| 574 | Divorcio contencioso con división de bienes en comunidad ordinaria: demanda | 2016 | `divorcio-contencioso-division-bienes-comunidad-ordinaria-574` |
| 596 | Demanda de modificación de medidas tras extinguirse la pareja de hecho | 2016 | `demanda-modificacion-medidas-tras-extinguirse-pareja-596` |
| 600 | Divorcio contencioso en separación de bienes con pensión compensatoria: demanda | 2016 | `divorcio-contencioso-separacion-bienes-pension-600` |
| 626 | Separación con división de bienes en comunidad ordinaria indivisa: demanda | 2016 | `separacion-division-bienes-comunidad-ordinaria-indivisa-626` |
| 627 | Divorcio contencioso con custodia compartida (País Vasco): demanda | 2016 | `divorcio-contencioso-custodia-compartida-pais-vasco-627` |
| 644 | Divorcio de mutuo acuerdo con hijos mayores de edad: demanda | 2015 | `divorcio-mutuo-acuerdo-hijos-mayores-edad-demanda-644` |
| 682 | Separación de mutuo acuerdo sin hijos: demanda | 2015 | `separacion-mutuo-acuerdo-sin-hijos-demanda-682` |
| 844 | Demanda de inscripción en el Registro Civil de matrimonio celebrado en el extranjero | 2015 | `demanda-inscripcion-registro-civil-matrimonio-celebrado-844` |
| 892 | Divorcio de mutuo acuerdo: demanda | 2013 | `divorcio-mutuo-acuerdo-demanda-892` |
| 898 | Demanda de separación ante la Sección de Violencia sobre la Mujer | 2013 | `demanda-separacion-ante-seccion-violencia-sobre-mujer-898` |
| 916 | Demanda de divorcio contencioso sin hijos menores ni con capacidad limitada | 2013 | `demanda-divorcio-contencioso-sin-hijos-menores-ni-916` |
| 917 | Demanda de divorcio contencioso con hijos menores o con capacidad limitada | 2013 | `demanda-divorcio-contencioso-hijos-menores-capacidad-917` |
| 918 | Demanda de separación contenciosa sin hijos menores ni con capacidad modificada | 2013 | `demanda-separacion-contenciosa-sin-hijos-menores-ni-918` |
| 919 | Demanda de separación contenciosa con hijos menores o con capacidad modificada | 2013 | `demanda-separacion-contenciosa-hijos-menores-capacidad-919` |
| 921 | Demanda de divorcio de un cónyuge con consentimiento del otro y sin hijos dependientes | 2013 | `demanda-divorcio-conyuge-consentimiento-otro-sin-hijos-921` |
| 922 | Demanda conjunta de separación de mutuo acuerdo con hijos menores o con apoyos | 2013 | `demanda-conjunta-separacion-mutuo-acuerdo-hijos-menores-922` |
| 930 | Demanda de determinación de filiación | 2013 | `demanda-determinacion-filiacion-930` |
| 931 | Demanda contenciosa de modificación de medidas | 2013 | `demanda-contenciosa-modificacion-medidas-931` |
| 932 | Demanda de alimentos: modelo general | 2013 | `demanda-alimentos-modelo-general-932` |
| 933 | Guarda y custodia de mutuo acuerdo: demanda | 2013 | `guarda-custodia-mutuo-acuerdo-demanda-933` |
| 1114 | Ejecución de sentencia por incumplimiento del régimen de visitas | 2013 | `ejecucion-sentencia-incumplimiento-regimen-visitas-1114` |
| 1155 | Demanda de separación de un cónyuge con consentimiento del otro y sin hijos dependientes | 2013 | `demanda-separacion-conyuge-consentimiento-otro-sin-hijos-1155` |
| 1158 | Demanda ejecutiva de gastos extraordinarios previstos en la sentencia de separación o divorcio | 2015 | `demanda-ejecutiva-gastos-extraordinarios-previstos-1158` |
| 1162 | Demanda de modificación de pensión de alimentos (Derecho civil de Cataluña) | 2015 | `demanda-modificacion-pension-alimentos-derecho-civil-1162` |
| 1188 | Demanda de privación de patria potestad instada por los abuelos | 2014 | `demanda-privacion-patria-potestad-instada-abuelos-1188` |
| 1193 | Casación por interés casacional: reparto de cargas en los desplazamientos del régimen de visitas | 2014 | `casacion-interes-casacional-reparto-cargas-1193` |
| 1451 | Nulidad parcial del convenio por vicios del consentimiento en gananciales, o rescisión por lesión | 2014 | `nulidad-parcial-convenio-vicios-consentimiento-1451` |

## Recursos e impugnaciones (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 455 | Apelación contra la formación de inventario para liquidar gananciales | 2018 | `apelacion-contra-formacion-inventario-liquidar-455` |
| 472 | Apelación contra la sentencia de modificación de medidas | 2017 | `apelacion-contra-sentencia-modificacion-medidas-472` |
| 1442 | Apelación para obtener la custodia compartida de hijos menores | 2004 | `apelacion-obtener-custodia-compartida-hijos-menores-1442` |

## Contestaciones, oposiciones y alegaciones (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 109 | Contestación al divorcio con reconvención sobre el animal de compañía | 2022 | `contestacion-divorcio-reconvencion-sobre-animal-compania-109` |
| 188 | Contestación en proceso de menores con guarda compartida y medidas provisionales coetáneas | 2021 | `contestacion-proceso-menores-guarda-compartida-medidas-188` |
| 338 | Contestación a la modificación del uso de la vivienda por convivencia del custodio con un tercero | 2019 | `contestacion-modificacion-uso-vivienda-convivencia-338` |
| 371 | Contestación a la demanda verbal especial de alimentos | 2019 | `contestacion-demanda-verbal-especial-alimentos-371` |
| 375 | Contestación a la demanda de medidas paternofiliales de pareja no casada, con medidas provisionales | 2019 | `contestacion-demanda-medidas-paternofiliales-pareja-no-375` |
| 405 | Contestación al divorcio con medidas provisionales | 2019 | `contestacion-divorcio-medidas-provisionales-405` |
| 432 | Contestación con reconvención a la modificación de medidas definitivas | 2018 | `contestacion-reconvencion-modificacion-medidas-432` |
| 502 | Contestación al divorcio con reconvención (modelo general) | 2017 | `contestacion-divorcio-reconvencion-modelo-general-502` |
| 598 | Contestación y oposición a la modificación de la custodia compartida | 2016 | `contestacion-oposicion-modificacion-custodia-compartida-598` |
| 641 | Oposición a la restitución en sustracción internacional de menores | 2015 | `oposicion-restitucion-sustraccion-internacional-menores-641` |
| 835 | Reconvención en el divorcio o la separación contenciosa | 2013 | `reconvencion-divorcio-separacion-contenciosa-835` |
| 861 | Contestar a las medidas provisionales previas | 2013 | `contestar-medidas-provisionales-previas-861` |
| 897 | Contestación a divorcio contencioso con hijos mayores dependientes económicamente | 2013 | `contestacion-divorcio-contencioso-hijos-mayores-897` |
| 1452 | Contestación a demanda de rescisión por lesión de la liquidación de gananciales del convenio | 2014 | `contestacion-demanda-rescision-lesion-liquidacion-1452` |
| 1489 | Contestación a demanda de privación de patria potestad | 2014 | `contestacion-demanda-privacion-patria-potestad-1489` |
| 1500 | Contestación a demanda de divorcio con reconvención (Derecho civil de Cataluña) | 2014 | `contestacion-demanda-divorcio-reconvencion-derecho-civil-1500` |

## Solicitudes y expedientes (54)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 40 | Intervención judicial (art. 156 CC): retirar imágenes en redes de menor de 14 años | 2024 | `intervencion-judicial-art-156-cc-retirar-imagenes-redes-40` |
| 66 | Solicitud de los progenitores para revocar el desamparo de un menor | 2023 | `solicitud-progenitores-revocar-desamparo-menor-66` |
| 82 | Cambio de la mención registral del sexo en menores de 12 a 13 años, con cambio de nombre | 2023 | `cambio-mencion-registral-sexo-menores-12-13-anos-cambio-82` |
| 83 | Cambio de la mención registral del sexo en menores de 12 a 13 años, sin cambio de nombre | 2023 | `cambio-mencion-registral-sexo-menores-12-13-anos-sin-83` |
| 91 | Jurisdicción voluntaria por desacuerdo en la patria potestad: atención psicológica | 2023 | `jurisdiccion-voluntaria-desacuerdo-patria-potestad-91` |
| 110 | Pedir informe psicosocial en proceso de familia | 2022 | `pedir-informe-psicosocial-proceso-familia-110` |
| 112 | Jurisdicción voluntaria para autorizar el viaje de un menor | 2022 | `jurisdiccion-voluntaria-autorizar-viaje-menor-112` |
| 130 | Autorización judicial de fecundación post mortem con material del cónyuge fallecido | 2022 | `autorizacion-judicial-fecundacion-post-mortem-material-130` |
| 133 | Jurisdicción voluntaria por desacuerdo en la patria potestad: vacunación COVID | 2022 | `jurisdiccion-voluntaria-desacuerdo-patria-potestad-133` |
| 184 | Aprobación judicial del reconocimiento de filiación no matrimonial (art. 23.3.b LJV) | 2021 | `aprobacion-judicial-reconocimiento-filiacion-no-184` |
| 185 | Aprobación judicial del reconocimiento de filiación no matrimonial (art. 23.3.c LJV) | 2021 | `aprobacion-judicial-reconocimiento-filiacion-no-185` |
| 218 | Ampliar la ejecución por impago de pensiones en proceso matrimonial y embargar bienes | 2020 | `ampliar-ejecucion-impago-pensiones-proceso-matrimonial-218` |
| 297 | Suspensión del régimen de visitas por el estado de alarma del COVID-19 | 2020 | `suspension-regimen-visitas-estado-alarma-covid-19-297` |
| 318 | Solicitud de adopción (art. 176.2.3.ª CC) | 2020 | `solicitud-adopcion-art-176-2-3-cc-318` |
| 339 | Nombramiento de coordinador parental | 2019 | `nombramiento-coordinador-parental-339` |
| 429 | Prueba pericial psicológica en proceso de familia | 2018 | `prueba-pericial-psicologica-proceso-familia-429` |
| 453 | Decidir un acto concreto en desacuerdo de progenitores: pasaporte del menor | 2018 | `decidir-acto-concreto-desacuerdo-progenitores-pasaporte-453` |
| 461 | Liquidación de gananciales y división de herencia por fallecimiento de ambos cónyuges | 2017 | `liquidacion-gananciales-division-herencia-fallecimiento-461` |
| 495 | Liquidación de gananciales y división de herencia por fallecimiento de un cónyuge | 2017 | `liquidacion-gananciales-division-herencia-fallecimiento-495` |
| 498 | Solicitud de adopción (art. 176.2.4.ª CC) | 2017 | `solicitud-adopcion-art-176-2-4-cc-498` |
| 505 | Reconducir el divorcio o separación contencioso al mutuo acuerdo | 2017 | `reconducir-divorcio-separacion-contencioso-mutuo-acuerdo-505` |
| 518 | Solicitud de adopción (art. 176.2.1.ª CC) | 2016 | `solicitud-adopcion-art-176-2-1-cc-518` |
| 521 | Solicitud de adopción (art. 176.2.2.ª CC) | 2016 | `solicitud-adopcion-art-176-2-2-cc-521` |
| 528 | Decidir un acto concreto en desacuerdo de progenitores: traslado de domicilio del menor | 2016 | `decidir-acto-concreto-desacuerdo-progenitores-traslado-528` |
| 621 | Dispensa de impedimento matrimonial | 2016 | `dispensa-impedimento-matrimonial-621` |
| 642 | Declarar ilícito el traslado o retención de un menor en otro Estado | 2015 | `declarar-ilicito-traslado-retencion-menor-otro-estado-642` |
| 655 | Emancipación judicial con progenitores separados | 2015 | `emancipacion-judicial-progenitores-separados-655` |
| 656 | Suspensión de la sustracción internacional de menores por intento de mediación | 2015 | `suspension-sustraccion-internacional-menores-intento-656` |
| 658 | Acta de notoriedad del régimen económico matrimonial legal | 2015 | `acta-notoriedad-regimen-economico-matrimonial-legal-658` |
| 659 | Escritura pública de separación o divorcio de mutuo acuerdo: solicitud | 2015 | `escritura-publica-separacion-divorcio-mutuo-acuerdo-659` |
| 672 | Autorización judicial para disponer de la vivienda habitual por desacuerdo de los cónyuges | 2015 | `autorizacion-judicial-disponer-vivienda-habitual-672` |
| 741 | Autorización para disponer de bienes comunes cuando el cónyuge los administra | 2015 | `autorizacion-disponer-bienes-comunes-cuando-conyuge-741` |
| 742 | Autorización para actos sobre bienes comunes ante impedimento o negativa del otro cónyuge | 2015 | `autorizacion-actos-sobre-bienes-comunes-ante-impedimento-742` |
| 743 | Contribución a las cargas del matrimonio por incumplimiento de un cónyuge | 2015 | `contribucion-cargas-matrimonio-incumplimiento-conyuge-743` |
| 744 | Administración de bienes comunes por impedimento, abandono o separación de hecho | 2015 | `administracion-bienes-comunes-impedimento-abandono-744` |
| 745 | Domicilio conyugal y vivienda habitual en desacuerdo de los cónyuges | 2015 | `domicilio-conyugal-vivienda-habitual-desacuerdo-conyuges-745` |
| 750 | Decidir un acto concreto en desacuerdo de progenitores: elección de colegio | 2015 | `decidir-acto-concreto-desacuerdo-progenitores-eleccion-750` |
| 773 | Emancipación judicial por entorpecer gravemente la patria potestad | 2015 | `emancipacion-judicial-entorpecer-gravemente-patria-773` |
| 775 | Conversión de adopción simple en plena: solicitud | 2015 | `conversion-adopcion-simple-plena-solicitud-775` |
| 776 | Autorización judicial para consentir la intromisión en el honor, intimidad e imagen del menor | 2015 | `autorizacion-judicial-consentir-intromision-honor-776` |
| 779 | Autorización judicial para reconocer una filiación no matrimonial | 2015 | `autorizacion-judicial-reconocer-filiacion-no-matrimonial-779` |
| 782 | Aprobación judicial del reconocimiento de filiación no matrimonial (art. 23.3 a) LJV) | 2015 | `aprobacion-judicial-reconocimiento-filiacion-no-782` |
| 783 | Testimonio del auto que concede la dispensa de impedimento matrimonial | 2015 | `testimonio-auto-concede-dispensa-impedimento-matrimonial-783` |
| 785 | Modificación de medidas: solicitud | 2015 | `modificacion-medidas-solicitud-785` |
| 787 | Medidas de averiguación e investigación del ausente | 2015 | `medidas-averiguacion-e-investigacion-ausente-787` |
| 788 | Medidas urgentes de protección del patrimonio del desaparecido antes de la comparecencia | 2015 | `medidas-urgentes-proteccion-patrimonio-desaparecido-788` |
| 830 | Medidas judiciales de aseguramiento del patrimonio del menor (art. 167 CC) | 2015 | `medidas-judiciales-aseguramiento-patrimonio-menor-art-830` |
| 845 | Finalizar el trámite para presentar demanda de asentimiento en la adopción | 2015 | `finalizar-tramite-presentar-demanda-asentimiento-845` |
| 881 | Medidas provisionales previas a la demanda con procurador y abogado | 2013 | `medidas-provisionales-previas-demanda-procurador-abogado-881` |
| 915 | Medidas provisionales solicitadas con la demanda | 2013 | `medidas-provisionales-solicitadas-demanda-915` |
| 955 | Formación de inventario de la sociedad de gananciales | 2013 | `formacion-inventario-sociedad-gananciales-955` |
| 1146 | Declaración de gasto como extraordinario | 2013 | `declaracion-gasto-como-extraordinario-1146` |
| 1443 | Modificación de medidas definitivas sobre guarda y custodia de hijos menores | 2005 | `modificacion-medidas-definitivas-sobre-guarda-custodia-1443` |
| 1512 | Solicitud conjunta de mediación familiar | 2014 | `solicitud-conjunta-mediacion-familiar-1512` |

## Escritos de trámite (19)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 38 | Oposición a medidas por menores en riesgo con tutela de la Generalitat (Cataluña) | 2024 | `oposicion-medidas-menores-riesgo-tutela-generalitat-38` |
| 161 | Otrosí de demanda ejecutiva: notificar al cónyuge el embargo de bienes gananciales | 2021 | `otrosi-demanda-ejecutiva-notificar-conyuge-embargo-161` |
| 421 | Oposición inicial de los progenitores a la declaración de desamparo | 2018 | `oposicion-inicial-progenitores-declaracion-desamparo-421` |
| 427 | Proposición de prueba en proceso de familia | 2018 | `proposicion-prueba-proceso-familia-427` |
| 470 | Embargo de bienes gananciales por insuficiencia de los privativos | 2017 | `embargo-bienes-gananciales-insuficiencia-privativos-470` |
| 497 | Desistimiento del proceso de separación o divorcio de mutuo acuerdo | 2017 | `desistimiento-proceso-separacion-divorcio-mutuo-acuerdo-497` |
| 534 | Propuesta de convenio regulador de separación o divorcio con todas las opciones | 2016 | `propuesta-convenio-regulador-separacion-divorcio-todas-534` |
| 573 | Escrito conjunto comunicando la reconciliación al Tribunal | 2016 | `escrito-conjunto-comunicando-reconciliacion-tribunal-573` |
| 725 | Autorización para repudiar herencia o legados por hijos menores de 16 años | 2015 | `autorizacion-repudiar-herencia-legados-hijos-menores-16-725` |
| 846 | Comparecencia en la adopción pidiendo reconocer la necesidad de asentimiento | 2015 | `comparecencia-adopcion-pidiendo-reconocer-necesidad-846` |
| 1037 | Otrosí: medidas para asegurar la eficacia de la sentencia | 2013 | `otrosi-medidas-asegurar-eficacia-sentencia-1037` |
| 1144 | Otrosí: alimentos | 2013 | `otrosi-alimentos-1144` |
| 1156 | Otrosí: citación de hijos menores | 2013 | `otrosi-citacion-hijos-menores-1156` |
| 1163 | Propuesta de liquidación del consorcio conyugal aragonés | 2015 | `propuesta-liquidacion-consorcio-conyugal-aragones-1163` |
| 1344 | Otrosí: medidas cautelares | 2013 | `otrosi-medidas-cautelares-1344` |
| 1453 | Operaciones liquidatorias de gananciales presentadas por el contador | 2014 | `operaciones-liquidatorias-gananciales-presentadas-1453` |
| 1514 | Transformación del procedimiento matrimonial por acuerdo de mediación | 2014 | `transformacion-procedimiento-matrimonial-acuerdo-1514` |
| 1515 | Homologación de acuerdo de mediación familiar en ejecución de medidas definitivas | 2014 | `homologacion-acuerdo-mediacion-familiar-ejecucion-1515` |
| 1516 | Homologación de acuerdo de mediación familiar en sentencia | 2014 | `homologacion-acuerdo-mediacion-familiar-sentencia-1516` |

## Actos y resoluciones de la Administración o del órgano judicial (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 90 | Acuerdo prematrimonial para prever los efectos de una ruptura | 2023 | `acuerdo-prematrimonial-prever-efectos-ruptura-90` |
| 398 | Certificado de resolución en materia de regímenes económicos matrimoniales | 2019 | `certificado-resolucion-materia-regimenes-economicos-398` |
| 399 | Certificado de documento público en materia de regímenes económicos matrimoniales | 2019 | `certificado-documento-publico-materia-regimenes-399` |
| 400 | Certificado de transacción judicial en materia de regímenes económicos matrimoniales | 2019 | `certificado-transaccion-judicial-materia-regimenes-400` |
| 1227 | Aviso al arrendatario: vivienda necesaria para el cónyuge tras divorcio o nulidad | 2013 | `aviso-arrendatario-vivienda-necesaria-conyuge-tras-1227` |
| 1513 | Acta inicial de mediación familiar | 2014 | `acta-inicial-mediacion-familiar-1513` |

## Contratos, escrituras y documentos (28)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 37 | Convenio de divorcio de mutuo acuerdo con mascota, sin hijos ni bienes (Cataluña) | 2024 | `convenio-divorcio-mutuo-acuerdo-mascota-sin-hijos-ni-37` |
| 85 | Convenio de divorcio con animal de compañía | 2023 | `convenio-divorcio-animal-compania-85` |
| 106 | Convenio de divorcio de mutuo acuerdo con hijos mayores de edad | 2022 | `convenio-divorcio-mutuo-acuerdo-hijos-mayores-edad-106` |
| 261 | Convenio regulador de divorcio: modelo general | 2020 | `convenio-regulador-divorcio-modelo-general-261` |
| 288 | Convenio de divorcio entre españoles con residencia en Gran Bretaña tras el traslado de uno a España | 2020 | `convenio-divorcio-entre-espanoles-residencia-gran-288` |
| 289 | Demanda de alimentos de hijo mayor residente en Reino Unido contra la madre residente en España | 2020 | `demanda-alimentos-hijo-mayor-residente-reino-unido-289` |
| 290 | Demanda de divorcio de británico y española casados en Francia, con hijos mayores | 2020 | `demanda-divorcio-britanico-espanola-casados-francia-290` |
| 292 | Demanda de modificación de medidas por traslado a Reino Unido del progenitor no custodio | 2020 | `demanda-modificacion-medidas-traslado-reino-unido-292` |
| 293 | Demanda de medidas previas al divorcio entre españoles con traslado de uno a Reino Unido | 2020 | `demanda-medidas-previas-divorcio-entre-espanoles-293` |
| 312 | Demanda del art. 158 CC por incumplimiento del régimen de visitas amparado en el estado de alarma | 2020 | `demanda-art-158-cc-incumplimiento-regimen-visitas-312` |
| 313 | Convenio de divorcio entre españoles residentes en Reino Unido | 2020 | `convenio-divorcio-entre-espanoles-residentes-reino-unido-313` |
| 348 | Documento de extinción de pareja estable no casada (Aragón) | 2019 | `documento-extincion-pareja-estable-no-casada-aragon-348` |
| 487 | Capitulaciones del matrimonio: escritura tipo | 2017 | `capitulaciones-matrimonio-escritura-tipo-487` |
| 488 | Compraventa privada de bien ganancial entre cónyuges | 2017 | `compraventa-privada-bien-ganancial-entre-conyuges-488` |
| 509 | Convenio de mutuo acuerdo sobre custodia, alimentos y relaciones con hijo menor y nasciturus | 2017 | `convenio-mutuo-acuerdo-sobre-custodia-alimentos-509` |
| 550 | Pacto de relaciones familiares (Aragón) | 2012 | `pacto-relaciones-familiares-aragon-550` |
| 559 | Escritura de constitución de pareja de hecho y otros pactos (Galicia) | 2016 | `escritura-constitucion-pareja-hecho-otros-pactos-galicia-559` |
| 560 | Pacto de modificación de la inscripción de pareja de hecho con pactos (Galicia) | 2016 | `pacto-modificacion-inscripcion-pareja-hecho-pactos-560` |
| 561 | Constitución privada de pareja de hecho por pacto (Galicia) | 2016 | `constitucion-privada-pareja-hecho-pacto-galicia-561` |
| 563 | Escritura simplificada de constitución de pareja de hecho (Galicia) | 2016 | `escritura-simplificada-constitucion-pareja-hecho-galicia-563` |
| 564 | Extinción conjunta de la pareja de hecho por pacto (Galicia) | 2016 | `extincion-conjunta-pareja-hecho-pacto-galicia-564` |
| 619 | Escritura de reconciliación de cónyuges separados | 2016 | `escritura-reconciliacion-conyuges-separados-619` |
| 847 | Custodia compartida: convenio regulador | 2013 | `custodia-compartida-convenio-regulador-847` |
| 848 | Convenio regulador sin hijos menores o con hijos con apoyos | 2013 | `convenio-regulador-sin-hijos-menores-hijos-apoyos-848` |
| 1153 | Convenio regulador de guarda, custodia y alimentos en pareja more uxorio | 2013 | `convenio-regulador-guarda-custodia-alimentos-pareja-more-1153` |
| 1160 | Cláusula de liquidación de gananciales con bienes adquiridos a plazos antes de la sociedad | 2015 | `clausula-liquidacion-gananciales-bienes-adquiridos-1160` |
| 1190 | Extinción de pareja estable sin hijos: documento privado | 2014 | `extincion-pareja-estable-sin-hijos-documento-privado-1190` |
| 1444 | Cláusula de custodia compartida de mutuo acuerdo | 2008 | `clausula-custodia-compartida-mutuo-acuerdo-1444` |

## Comunicaciones, requerimientos y reclamaciones (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 171 | Reclamación a la aseguradora del cónyuge perjudicado | 2021 | `reclamacion-aseguradora-conyuge-perjudicado-171` |

## Otros (9)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 332 | Plan contradictorio de custodia compartida de un cónyuge | 2019 | `plan-contradictorio-custodia-compartida-conyuge-332` |
| 349 | Plan de relaciones familiares (Aragón) | 2019 | `plan-relaciones-familiares-aragon-349` |
| 562 | Extinción individual de la pareja de hecho (Galicia) | 2016 | `extincion-individual-pareja-hecho-galicia-562` |
| 585 | Custodia de bienes muebles por consenso | 2016 | `custodia-bienes-muebles-consenso-585` |
| 801 | Separación o divorcio de mutuo acuerdo sin hijos menores ni con apoyos dependientes | 2015 | `separacion-divorcio-mutuo-acuerdo-sin-hijos-menores-ni-801` |
| 1053 | Modificar las medidas cautelares | 2013 | `modificar-medidas-cautelares-1053` |
| 1067 | Ejecutar provisionalmente la sentencia que modifica medidas | 2013 | `ejecutar-provisionalmente-sentencia-modifica-medidas-1067` |
| 1148 | Aprobación judicial del acuerdo de las partes en medidas provisionales | 2013 | `aprobacion-judicial-acuerdo-partes-medidas-provisionales-1148` |
| 1454 | Cuaderno particional de gananciales presentado por el contador | 2014 | `cuaderno-particional-gananciales-presentado-contador-1454` |
