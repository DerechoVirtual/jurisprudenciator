---
name: indice
description: "Índice de los 404 formularios de multas y expedientes de tráfico (descargos, recurso de reposición, puntos, identificación del conductor, DEV). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Multas y expedientes de tráfico: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Ordenanzas municipales** (tráfico, urbanismo, tributos locales, convivencia) → `buscar_ordenanzas` → `leer_ordenanza`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/multas-trafico:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 55 | Demanda abreviada contra multa por circular por Madrid Central | 2020 | `demanda-abreviada-contra-multa-circular-madrid-central-55` |
| 1740 | Recurso extraordinario de revisión contra sanciones de tráfico | 2004 | `recurso-extraordinario-revision-contra-sanciones-trafico-1740` |

## Recursos e impugnaciones (139)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 22 | Reposición contra multa por incumplir restricciones de circulación por contaminación | 2022 | `reposicion-contra-multa-incumplir-restricciones-22` |
| 24 | Reposición contra sanción por incumplir las normas del alcoholímetro antiarranque | 2022 | `reposicion-contra-sancion-incumplir-normas-alcoholimetro-24` |
| 25 | Reposición contra sanción por usar dispositivos de intercomunicación en pruebas de permisos | 2022 | `reposicion-contra-sancion-usar-dispositivos-25` |
| 138 | Reposición contra sanción por incumplir normas de transporte terrestre por carretera | 2017 | `reposicion-contra-sancion-incumplir-normas-transporte-138` |
| 1305 | Alzada contra la pérdida de vigencia del permiso declarada por la Jefatura Provincial de Tráfico | 2006 | `alzada-contra-perdida-vigencia-permiso-declarada-1305` |
| 1436 | Reposición contra multa por prioridad de paso en obras y estrechamientos | 2004 | `reposicion-contra-multa-prioridad-paso-obras-1436` |
| 1437 | Reposición contra multa por falta de visibilidad del vehículo | 2004 | `reposicion-contra-multa-falta-visibilidad-vehiculo-1437` |
| 1438 | Reposición contra multa por sentido de circulación en refugios, isletas y dispositivos de guía | 2004 | `reposicion-contra-multa-sentido-circulacion-refugios-1438` |
| 1439 | Reposición contra multa por emplazamiento y acondicionamiento de personas | 2004 | `reposicion-contra-multa-emplazamiento-acondicionamiento-1439` |
| 1440 | Reposición contra multa por arrojar a la vía un objeto que puede causar incendio o peligro | 2004 | `reposicion-contra-multa-arrojar-via-objeto-puede-causar-1440` |
| 1442 | Reposición contra multa por incorporación a la circulación | 2004 | `reposicion-contra-multa-incorporacion-circulacion-1442` |
| 1443 | Reposición contra multa por conducta ante vehículos prioritarios | 2004 | `reposicion-contra-multa-conducta-ante-vehiculos-1443` |
| 1444 | Reposición contra multa por retirar, sustituir o alterar señales | 2004 | `reposicion-contra-multa-retirar-sustituir-alterar-1444` |
| 1445 | Reposición contra multa por alumbrado de cruce | 2004 | `reposicion-contra-multa-alumbrado-cruce-1445` |
| 1446 | Reposición contra multa por otras marcas e inscripciones blancas | 2004 | `reposicion-contra-multa-otras-marcas-e-inscripciones-1446` |
| 1447 | Reposición contra multa por matrículas | 2004 | `reposicion-contra-multa-matriculas-1447` |
| 1448 | Reposición contra multa por semáforos reservados | 2004 | `reposicion-contra-multa-semaforos-reservados-1448` |
| 1449 | Reposición contra multa por señales de indicaciones generales | 2004 | `reposicion-contra-multa-senales-indicaciones-generales-1449` |
| 1450 | Reposición contra multa por señales de restricción de paso | 2004 | `reposicion-contra-multa-senales-restriccion-paso-1450` |
| 1451 | Reposición contra multa por inmovilizaciones | 2004 | `reposicion-contra-multa-inmovilizaciones-1451` |
| 1458 | Reposición contra multa por no auxiliar en accidente | 2004 | `reposicion-contra-multa-no-auxiliar-accidente-1458` |
| 1459 | Reposición contra multa por entorpecer la circulación o causar peligro, molestias o daños | 2004 | `reposicion-contra-multa-entorpecer-circulacion-causar-1459` |
| 1460 | Reposición contra multa por advertencias a otros vehículos | 2004 | `reposicion-contra-multa-advertencias-otros-vehiculos-1460` |
| 1461 | Reposición contra multa por alumbrado inutilizado o averiado | 2004 | `reposicion-contra-multa-alumbrado-inutilizado-averiado-1461` |
| 1462 | Reposición contra multa por advertencias acústicas | 2004 | `reposicion-contra-multa-advertencias-acusticas-1462` |
| 1463 | Reposición contra multa por advertencias ópticas | 2004 | `reposicion-contra-multa-advertencias-opticas-1463` |
| 1464 | Reposición contra multa por puertas del vehículo | 2004 | `reposicion-contra-multa-puertas-vehiculo-1464` |
| 1465 | Reposición contra multa por supuestos especiales de alumbrado | 2004 | `reposicion-contra-multa-supuestos-especiales-alumbrado-1465` |
| 1466 | Reposición contra multa por no apagar el motor | 2004 | `reposicion-contra-multa-no-apagar-motor-1466` |
| 1467 | Reposición contra multa por advertencias de vehículos de urgencia y especiales | 2004 | `reposicion-contra-multa-advertencias-vehiculos-urgencia-1467` |
| 1468 | Reposición contra multa por autorizaciones para conducir | 2004 | `reposicion-contra-multa-autorizaciones-conducir-1468` |
| 1469 | Reposición contra multa por marcas de otros colores | 2004 | `reposicion-contra-multa-marcas-otros-colores-1469` |
| 1470 | Reposición contra multa por señales horizontales de circulación | 2004 | `reposicion-contra-multa-senales-horizontales-circulacion-1470` |
| 1471 | Reposición contra multa por marcas blancas transversales | 2004 | `reposicion-contra-multa-marcas-blancas-transversales-1471` |
| 1472 | Reposición contra multa por marcas blancas longitudinales | 2004 | `reposicion-contra-multa-marcas-blancas-longitudinales-1472` |
| 1473 | Reposición contra multa por autorizaciones administrativas generales | 2004 | `reposicion-contra-multa-autorizaciones-administrativas-1473` |
| 1474 | Reposición contra multa por permiso de circulación y documentación del vehículo | 2004 | `reposicion-contra-multa-permiso-circulacion-1474` |
| 1475 | Reposición contra multa por inmovilizar el vehículo y caída de la carga | 2004 | `reposicion-contra-multa-inmovilizar-vehiculo-caida-carga-1475` |
| 1476 | Reposición contra multa por formato de las señales | 2004 | `reposicion-contra-multa-formato-senales-1476` |
| 1477 | Reposición contra multa por señales de balizamiento | 2004 | `reposicion-contra-multa-senales-balizamiento-1477` |
| 1478 | Reposición contra multa por circulación de animales: normas especiales | 2004 | `reposicion-contra-multa-circulacion-animales-normas-1478` |
| 1479 | Reposición contra multa por semáforo para peatones | 2004 | `reposicion-contra-multa-semaforo-peatones-1479` |
| 1480 | Reposición contra multa por desobedecer señales u órdenes de la autoridad o sus agentes | 2004 | `reposicion-contra-multa-desobedecer-senales-u-ordenes-1480` |
| 1481 | Reposición contra multa por animales en autopistas y autovías | 2004 | `reposicion-contra-multa-animales-autopistas-autovias-1481` |
| 1482 | Reposición contra multa por semáforo circular | 2004 | `reposicion-contra-multa-semaforo-circular-1482` |
| 1483 | Reposición contra multa por deslumbramiento | 2004 | `reposicion-contra-multa-deslumbramiento-1483` |
| 1484 | Reposición contra multa por barreras, semibarreras y semáforos | 2004 | `reposicion-contra-multa-barreras-semibarreras-semaforos-1484` |
| 1485 | Reposición contra multa por alumbrado de carretera | 2004 | `reposicion-contra-multa-alumbrado-carretera-1485` |
| 1486 | Reposición contra multa por detenerse en paso a nivel, puente móvil o túnel | 2004 | `reposicion-contra-multa-detenerse-paso-nivel-puente-1486` |
| 1487 | Reposición contra multa por pasos a nivel y puentes móviles | 2004 | `reposicion-contra-multa-pasos-nivel-puentes-moviles-1487` |
| 1488 | Reposición contra multa por alumbrado de la placa de matrícula | 2004 | `reposicion-contra-multa-alumbrado-placa-matricula-1488` |
| 1489 | Reposición contra multa por no usar el alumbrado durante el día | 2004 | `reposicion-contra-multa-no-usar-alumbrado-durante-dia-1489` |
| 1490 | Reposición contra multa por alumbrado de posición y gálibo | 2004 | `reposicion-contra-multa-alumbrado-posicion-galibo-1490` |
| 1491 | Reposición contra multa por maniobra de parada y estacionamiento | 2004 | `reposicion-contra-multa-maniobra-parada-estacionamiento-1491` |
| 1492 | Reposición contra multa por maniobra de adelantamiento | 2004 | `reposicion-contra-multa-maniobra-adelantamiento-1492` |
| 1493 | Reposición contra multa por colocación del vehículo al estacionar | 2004 | `reposicion-contra-multa-colocacion-vehiculo-estacionar-1493` |
| 1494 | Reposición contra multa por parada y estacionamiento | 2004 | `reposicion-contra-multa-parada-estacionamiento-1494` |
| 1495 | Reposición contra multa por adelantar donde está prohibido | 2004 | `reposicion-contra-multa-adelantar-donde-esta-prohibido-1495` |
| 1496 | Reposición contra multa por parar o estacionar en lugar prohibido | 2004 | `reposicion-contra-multa-parar-estacionar-lugar-prohibido-1496` |
| 1497 | Reposición contra multa por adelantar con obstáculos | 2004 | `reposicion-contra-multa-adelantar-obstaculos-1497` |
| 1498 | Reposición contra multa por adelantamiento en supuestos especiales | 2004 | `reposicion-contra-multa-adelantamiento-supuestos-1498` |
| 1499 | Reposición contra multa por obligaciones del conductor adelantado | 2004 | `reposicion-contra-multa-obligaciones-conductor-1499` |
| 1500 | Reposición contra multa por señales de carriles | 2004 | `reposicion-contra-multa-senales-carriles-1500` |
| 1501 | Reposición contra multa por señales de prioridad | 2004 | `reposicion-contra-multa-senales-prioridad-1501` |
| 1502 | Reposición contra multa por señales de prohibición de entrada | 2004 | `reposicion-contra-multa-senales-prohibicion-entrada-1502` |
| 1503 | Reposición contra multa por otras señales de prohibición o restricción | 2004 | `reposicion-contra-multa-otras-senales-prohibicion-1503` |
| 1504 | Reposición contra multa por señales de obligación | 2004 | `reposicion-contra-multa-senales-obligacion-1504` |
| 1505 | Reposición contra multa por semáforos cuadrados o de carril | 2004 | `reposicion-contra-multa-semaforos-cuadrados-carril-1505` |
| 1506 | Reposición contra multa por cinturón o sistema de retención infantil | 2004 | `reposicion-contra-multa-cinturon-sistema-retencion-1506` |
| 1507 | Reposición contra multa por circulación de animales: normas generales | 2004 | `reposicion-contra-multa-circulacion-animales-normas-1507` |
| 1508 | Reposición contra multa a peatón por circular de noche | 2004 | `reposicion-contra-multa-peaton-circular-noche-1508` |
| 1509 | Reposición contra multa a peatón por circular por calzada o arcén | 2004 | `reposicion-contra-multa-peaton-circular-calzada-arcen-1509` |
| 1510 | Reposición contra multa a peatón por circular en autopista o autovía | 2004 | `reposicion-contra-multa-peaton-circular-autopista-1510` |
| 1511 | Reposición contra multa por circular por zona peatonal | 2004 | `reposicion-contra-multa-circular-zona-peatonal-1511` |
| 1512 | Reposición contra multa por casco y otros elementos de protección | 2004 | `reposicion-contra-multa-casco-otros-elementos-proteccion-1512` |
| 1513 | Reposición contra multa a peatón por cruzar la calzada | 2004 | `reposicion-contra-multa-peaton-cruzar-calzada-1513` |
| 1514 | Reposición contra multa por uso indebido de carriles en poblado con más de un carril por sentido | 2004 | `reposicion-contra-multa-uso-indebido-carriles-poblado-1514` |
| 1515 | Reposición contra multa por conducir con estupefacientes, psicotrópicos o sustancias análogas | 2004 | `reposicion-contra-multa-conducir-estupefacientes-1515` |
| 1516 | Reposición contra multa por incumplimientos del personal sanitario sobre bebidas alcohólicas | 2004 | `reposicion-contra-multa-incumplimientos-personal-1516` |
| 1517 | Reposición contra multa por carriles fuera de poblado con más de un carril por sentido | 2004 | `reposicion-contra-multa-carriles-fuera-poblado-mas-1517` |
| 1518 | Reposición contra multa por utilización de carriles en calzadas de doble sentido | 2004 | `reposicion-contra-multa-utilizacion-carriles-calzadas-1518` |
| 1519 | Reposición contra multa por infracción en carriles de doble sentido de circulación | 2004 | `reposicion-contra-multa-infraccion-carriles-doble-1519` |
| 1520 | Reposición contra multa por tasa de alcohol en sangre o aire espirado | 2004 | `reposicion-contra-multa-tasa-alcohol-sangre-aire-1520` |
| 1521 | Reposición contra multa por carriles fuera de poblado con tres o más carriles por sentido | 2004 | `reposicion-contra-multa-carriles-fuera-poblado-tres-mas-1521` |
| 1522 | Reposición contra multa por la investigación de la alcoholemia | 2004 | `reposicion-contra-multa-investigacion-alcoholemia-1522` |
| 1523 | Reposición contra multa por pruebas de detección de estupefacientes | 2004 | `reposicion-contra-multa-pruebas-deteccion-1523` |
| 1524 | Reposición contra multa por obligaciones de quien adelanta | 2004 | `reposicion-contra-multa-obligaciones-quien-adelanta-1524` |
| 1525 | Reposición contra multa por maniobra de cambio de sentido | 2004 | `reposicion-contra-multa-maniobra-cambio-sentido-1525` |
| 1526 | Reposición contra multa por cambio de dirección en supuestos especiales | 2004 | `reposicion-contra-multa-cambio-direccion-supuestos-1526` |
| 1527 | Reposición contra multa por marcha atrás: normas generales | 2004 | `reposicion-contra-multa-marcha-atras-normas-generales-1527` |
| 1528 | Reposición contra multa por adelantar en calzada de varios carriles | 2004 | `reposicion-contra-multa-adelantar-calzada-varios-1528` |
| 1529 | Reposición contra multa por cambio de sentido en supuestos especiales | 2004 | `reposicion-contra-multa-cambio-sentido-supuestos-1529` |
| 1530 | Reposición contra multa por maniobra de marcha atrás | 2004 | `reposicion-contra-multa-maniobra-marcha-atras-1530` |
| 1531 | Reposición contra multa por adelantar por la izquierda | 2004 | `reposicion-contra-multa-adelantar-izquierda-1531` |
| 1532 | Reposición contra multa por carril de deceleración | 2004 | `reposicion-contra-multa-carril-deceleracion-1532` |
| 1533 | Reposición contra multa por detenerse indebidamente en una intersección | 2004 | `reposicion-contra-multa-detenerse-indebidamente-1533` |
| 1534 | Reposición contra multa por no ceder prioridad a peatones | 2004 | `reposicion-contra-multa-no-ceder-prioridad-peatones-1534` |
| 1535 | Reposición contra multa por no ceder prioridad a animales | 2004 | `reposicion-contra-multa-no-ceder-prioridad-animales-1535` |
| 1536 | Reposición contra multa por prioridad de paso sin señalización | 2004 | `reposicion-contra-multa-prioridad-paso-sin-senalizacion-1536` |
| 1537 | Reposición contra multa por prioridad en puentes y obras señalizadas | 2004 | `reposicion-contra-multa-prioridad-puentes-obras-1537` |
| 1538 | Reposición contra multa por prioridad en intersección sin señalizar | 2004 | `reposicion-contra-multa-prioridad-interseccion-sin-1538` |
| 1539 | Reposición contra multa por prioridad en tramos de gran pendiente | 2004 | `reposicion-contra-multa-prioridad-tramos-gran-pendiente-1539` |
| 1540 | Reposición contra multa por normas generales de prioridad de paso | 2004 | `reposicion-contra-multa-normas-generales-prioridad-paso-1540` |
| 1541 | Reposición contra multa por no guardar la distancia entre vehículos | 2004 | `reposicion-contra-multa-no-guardar-distancia-entre-1541` |
| 1542 | Reposición contra multa por exceso de velocidad en vía urbana o travesía | 2004 | `reposicion-contra-multa-exceso-velocidad-via-urbana-1542` |
| 1543 | Reposición contra multa por velocidades prevalentes sobre la máxima | 2004 | `reposicion-contra-multa-velocidades-prevalentes-sobre-1543` |
| 1544 | Reposición contra multa por velocidad mínima | 2004 | `reposicion-contra-multa-velocidad-minima-1544` |
| 1545 | Reposición contra multa por la forma de reducir la velocidad | 2004 | `reposicion-contra-multa-forma-reducir-velocidad-1545` |
| 1546 | Reposición contra multa por competiciones deportivas | 2004 | `reposicion-contra-multa-competiciones-deportivas-1546` |
| 1547 | Reposición contra multa por prioridad de paso en intersección señalizada | 2004 | `reposicion-contra-multa-prioridad-paso-interseccion-1547` |
| 1548 | Reposición contra multa por carriles en sentido contrario al habitual | 2004 | `reposicion-contra-multa-carriles-sentido-contrario-1548` |
| 1549 | Reposición contra multa por limitaciones a la circulación | 2004 | `reposicion-contra-multa-limitaciones-circulacion-1549` |
| 1550 | Reposición contra multa por uso del arcén | 2004 | `reposicion-contra-multa-uso-arcen-1550` |
| 1551 | Reposición contra multa por uso indebido de vías divididas en dos o tres calzadas | 2004 | `reposicion-contra-multa-uso-indebido-vias-divididas-dos-1551` |
| 1552 | Reposición contra multa por carriles reversibles | 2004 | `reposicion-contra-multa-carriles-reversibles-1552` |
| 1553 | Reposición contra multa por circulación en autopistas y autovías | 2004 | `reposicion-contra-multa-circulacion-autopistas-autovias-1553` |
| 1554 | Reposición contra multa por exceso de velocidad fuera de poblado | 2004 | `reposicion-contra-multa-exceso-velocidad-fuera-poblado-1554` |
| 1555 | Reposición contra multa por no moderar la velocidad | 2004 | `reposicion-contra-multa-no-moderar-velocidad-1555` |
| 1556 | Reposición contra multa por libertad de movimientos, atención, posición, animales y auriculares | 2004 | `reposicion-contra-multa-libertad-movimientos-atencion-1556` |
| 1557 | Reposición contra multa por carga y descarga | 2004 | `reposicion-contra-multa-carga-descarga-1557` |
| 1558 | Reposición contra multa por disposición de la carga | 2004 | `reposicion-contra-multa-disposicion-carga-1558` |
| 1559 | Reposición contra multa por dimensiones del vehículo y su carga | 2004 | `reposicion-contra-multa-dimensiones-vehiculo-carga-1559` |
| 1560 | Reposición contra multa por falta de control del vehículo o los animales | 2004 | `reposicion-contra-multa-falta-control-vehiculo-animales-1560` |
| 1561 | Reposición contra multa por transporte en ciclos, ciclomotores y motocicletas | 2004 | `reposicion-contra-multa-transporte-ciclos-ciclomotores-1561` |
| 1562 | Reposición contra multa por transporte colectivo de personas | 2004 | `reposicion-contra-multa-transporte-colectivo-personas-1562` |
| 1563 | Reposición contra multa por dimensiones de la carga | 2004 | `reposicion-contra-multa-dimensiones-carga-1563` |
| 1565 | Reposición contra multa por perturbaciones y contaminación | 2004 | `reposicion-contra-multa-perturbaciones-contaminacion-1565` |
| 1566 | Reposición contra multa por dejar en la vía objetos que afectan a la seguridad | 2004 | `reposicion-contra-multa-dejar-via-objetos-afectan-1566` |
| 1567 | Reposición contra multa por conducción negligente o temeraria | 2004 | `reposicion-contra-multa-conduccion-negligente-temeraria-1567` |
| 1568 | Reposición contra multa por transporte de personas | 2004 | `reposicion-contra-multa-transporte-personas-1568` |
| 1569 | Reposición contra multa por no señalizar obstáculos o peligros creados en la vía | 2004 | `reposicion-contra-multa-no-senalizar-obstaculos-peligros-1569` |
| 1578 | Reposición contra multa por cambio de dirección: normas generales | 2004 | `reposicion-contra-multa-cambio-direccion-normas-1578` |
| 1579 | Reposición contra multa por facultades de conductores de vehículos prioritarios | 2004 | `reposicion-contra-multa-facultades-conductores-vehiculos-1579` |
| 1580 | Reposición contra multa por maniobra de cambio de dirección | 2004 | `reposicion-contra-multa-maniobra-cambio-direccion-1580` |
| 1581 | Reposición contra multa por incorporación de vehículos de transporte de viajeros | 2004 | `reposicion-contra-multa-incorporacion-vehiculos-1581` |
| 1582 | Reposición contra multa por vehículos prioritarios | 2004 | `reposicion-contra-multa-vehiculos-prioritarios-1582` |
| 1583 | Reposición contra multa por vehículos y transportes especiales | 2004 | `reposicion-contra-multa-vehiculos-transportes-especiales-1583` |
| 1584 | Reposición contra multa por vehículos no prioritarios en servicio de urgencia | 2004 | `reposicion-contra-multa-vehiculos-no-prioritarios-1584` |
| 1743 | Reposición contra sanción de tráfico y seguridad vial | 2004 | `reposicion-contra-sancion-trafico-seguridad-vial-1743` |

## Contestaciones, oposiciones y alegaciones (157)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 21 | Descargos por incumplir restricciones de circulación por contaminación | 2022 | `descargos-incumplir-restricciones-circulacion-21` |
| 23 | Descargos por incumplir las normas del alcoholímetro antiarranque | 2022 | `descargos-incumplir-normas-alcoholimetro-antiarranque-23` |
| 26 | Descargos por usar dispositivos de intercomunicación en pruebas de permisos | 2022 | `descargos-usar-dispositivos-intercomunicacion-pruebas-26` |
| 163 | Alegaciones adicionales en cualquier fase del expediente | 2017 | `alegaciones-adicionales-cualquier-fase-expediente-163` |
| 174 | Alegaciones frente a la propuesta de resolución | 2017 | `alegaciones-frente-propuesta-resolucion-174` |
| 181 | Alegaciones por calificar mal la infracción en el boletín de denuncia | 2016 | `alegaciones-calificar-mal-infraccion-boletin-denuncia-181` |
| 182 | Alegaciones en audiencia sobre medidas cautelares de tráfico y seguridad vial | 2016 | `alegaciones-audiencia-sobre-medidas-cautelares-trafico-182` |
| 183 | Descargos por no identificar al conductor responsable | 2016 | `descargos-no-identificar-conductor-responsable-183` |
| 223 | Contestar a la petición razonada comunicando que no se incoa sancionador de tráfico | 2016 | `contestar-peticion-razonada-comunicando-no-incoa-223` |
| 260 | Alegaciones contra multa de tráfico en sancionador | 2016 | `alegaciones-contra-multa-trafico-sancionador-260` |
| 298 | Alegaciones en sancionador ordinario de tráfico | 2014 | `alegaciones-sancionador-ordinario-trafico-298` |
| 304 | Alegaciones por usar navegador con detector de radares | 2013 | `alegaciones-usar-navegador-detector-radares-304` |
| 318 | Alegaciones: multa al titular sin detener el vehículo ni requerirle identificar al conductor | 2013 | `alegaciones-multa-titular-sin-detener-vehiculo-ni-318` |
| 320 | Alegaciones por denegarse la prueba propuesta | 2013 | `alegaciones-denegarse-prueba-propuesta-320` |
| 590 | Alegaciones por retirada del vehículo | 2011 | `alegaciones-retirada-vehiculo-590` |
| 1304 | Alegaciones del conductor ante la pérdida de vigencia del permiso por perder todos los puntos | 2006 | `alegaciones-conductor-ante-perdida-vigencia-permiso-1304` |
| 1432 | Descargos por no respetar la prioridad en intersección señalizada | 2004 | `descargos-no-respetar-prioridad-interseccion-senalizada-1432` |
| 1433 | Descargos por dejar en la vía objetos que afectan a la seguridad | 2004 | `descargos-dejar-via-objetos-afectan-seguridad-1433` |
| 1434 | Descargos por exceso de velocidad en vía urbana o travesía | 2004 | `descargos-exceso-velocidad-via-urbana-travesia-1434` |
| 1435 | Descargos por tasa de alcohol en sangre o aire espirado | 2004 | `descargos-tasa-alcohol-sangre-aire-espirado-1435` |
| 1441 | Descargos por incumplir señales de restricción de paso | 2004 | `descargos-incumplir-senales-restriccion-paso-1441` |
| 1452 | Descargos por circulación de animales: normas especiales | 2004 | `descargos-circulacion-animales-normas-especiales-1452` |
| 1453 | Descargos por advertencias acústicas | 2004 | `descargos-advertencias-acusticas-1453` |
| 1454 | Descargos por uso del alumbrado durante el día | 2004 | `descargos-uso-alumbrado-durante-dia-1454` |
| 1455 | Descargos por adelantamiento en lugar prohibido | 2004 | `descargos-adelantamiento-lugar-prohibido-1455` |
| 1456 | Descargos por adelantamiento en calzada de varios carriles | 2004 | `descargos-adelantamiento-calzada-varios-carriles-1456` |
| 1457 | Descargos por cambio de sentido en supuestos especiales | 2004 | `descargos-cambio-sentido-supuestos-especiales-1457` |
| 1564 | Descargos por no tener seguro obligatorio del automóvil | 2004 | `descargos-no-tener-seguro-obligatorio-automovil-1564` |
| 1570 | Descargos por centros de reconocimiento de conductores | 2004 | `descargos-centros-reconocimiento-conductores-1570` |
| 1571 | Descargos por escuelas particulares de conductores | 2004 | `descargos-escuelas-particulares-conductores-1571` |
| 1572 | Descargos por señales horizontales de circulación | 2004 | `descargos-senales-horizontales-circulacion-1572` |
| 1573 | Descargos por marcas de otros colores | 2004 | `descargos-marcas-otros-colores-1573` |
| 1574 | Descargos por permisos de conducción | 2004 | `descargos-permisos-conduccion-1574` |
| 1575 | Descargos por otras marcas e inscripciones blancas | 2004 | `descargos-otras-marcas-e-inscripciones-blancas-1575` |
| 1576 | Descargos por matrículas obligatorias | 2004 | `descargos-matriculas-obligatorias-1576` |
| 1577 | Descargos por permiso de circulación y documentación del vehículo | 2004 | `descargos-permiso-circulacion-documentacion-vehiculo-1577` |
| 1585 | Descargos por señales de indicaciones generales | 2004 | `descargos-senales-indicaciones-generales-1585` |
| 1586 | Descargos por marcas blancas longitudinales | 2004 | `descargos-marcas-blancas-longitudinales-1586` |
| 1587 | Descargos por saltarse una señal de prioridad | 2004 | `descargos-saltarse-senal-prioridad-1587` |
| 1588 | Descargos por señales de obligación | 2004 | `descargos-senales-obligacion-1588` |
| 1589 | Descargos por marcas blancas transversales | 2004 | `descargos-marcas-blancas-transversales-1589` |
| 1590 | Descargos por señales de carriles | 2004 | `descargos-senales-carriles-1590` |
| 1591 | Descargos por otras señales de prohibición o restricción | 2004 | `descargos-otras-senales-prohibicion-restriccion-1591` |
| 1592 | Descargos por señales de prohibición de entrada | 2004 | `descargos-senales-prohibicion-entrada-1592` |
| 1593 | Descargos por circulación en autopistas y autovías | 2004 | `descargos-circulacion-autopistas-autovias-1593` |
| 1594 | Descargos por uso indebido de carriles fuera de poblado con tres o más carriles por sentido | 2004 | `descargos-uso-indebido-carriles-fuera-poblado-tres-mas-1594` |
| 1595 | Descargos por infracción en carriles de doble sentido de circulación | 2004 | `descargos-infraccion-carriles-doble-sentido-circulacion-1595` |
| 1596 | Descargos por limitaciones a la circulación | 2004 | `descargos-limitaciones-circulacion-1596` |
| 1597 | Descargos por uso indebido de carriles en poblado con más de un carril por sentido | 2004 | `descargos-uso-indebido-carriles-poblado-mas-carril-1597` |
| 1598 | Descargos por carriles en sentido contrario al habitual | 2004 | `descargos-carriles-sentido-contrario-habitual-1598` |
| 1599 | Descargos por uso del arcén | 2004 | `descargos-uso-arcen-1599` |
| 1600 | Descargos por uso indebido de carriles fuera de poblado con más de un carril por sentido | 2004 | `descargos-uso-indebido-carriles-fuera-poblado-mas-carril-1600` |
| 1601 | Descargos por carriles reversibles | 2004 | `descargos-carriles-reversibles-1601` |
| 1602 | Descargos por conducir con estupefacientes, psicotrópicos o sustancias análogas | 2004 | `descargos-conducir-estupefacientes-psicotropicos-1602` |
| 1603 | Descargos por utilización de carriles en calzadas de doble sentido | 2004 | `descargos-utilizacion-carriles-calzadas-doble-sentido-1603` |
| 1604 | Descargos por pruebas de detección de estupefacientes | 2004 | `descargos-pruebas-deteccion-estupefacientes-1604` |
| 1605 | Descargos por incumplimientos del personal sanitario sobre bebidas alcohólicas | 2004 | `descargos-incumplimientos-personal-sanitario-sobre-1605` |
| 1606 | Descargos por la investigación de la alcoholemia | 2004 | `descargos-investigacion-alcoholemia-1606` |
| 1607 | Descargos por libertad de movimientos, atención, posición, animales y auriculares | 2004 | `descargos-libertad-movimientos-atencion-posicion-1607` |
| 1608 | Descargos por falta de control del vehículo o los animales | 2004 | `descargos-falta-control-vehiculo-animales-1608` |
| 1609 | Descargos por falta de visibilidad del vehículo | 2004 | `descargos-falta-visibilidad-vehiculo-1609` |
| 1610 | Descargos por disposición de la carga | 2004 | `descargos-disposicion-carga-1610` |
| 1611 | Descargos por transporte de personas | 2004 | `descargos-transporte-personas-1611` |
| 1612 | Descargos por dimensiones del vehículo y su carga | 2004 | `descargos-dimensiones-vehiculo-carga-1612` |
| 1613 | Descargos por transporte colectivo de personas | 2004 | `descargos-transporte-colectivo-personas-1613` |
| 1614 | Descargos por emplazamiento y acondicionamiento de personas | 2004 | `descargos-emplazamiento-acondicionamiento-personas-1614` |
| 1615 | Descargos por dimensiones de la carga | 2004 | `descargos-dimensiones-carga-1615` |
| 1616 | Descargos por carga y descarga | 2004 | `descargos-carga-descarga-1616` |
| 1617 | Descargos por transporte en ciclos, ciclomotores y motocicletas | 2004 | `descargos-transporte-ciclos-ciclomotores-motocicletas-1617` |
| 1618 | Descargos por emisión de perturbaciones y contaminantes sobre los límites | 2004 | `descargos-emision-perturbaciones-contaminantes-sobre-1618` |
| 1619 | Descargos por arrojar a la vía un objeto que puede causar incendio o peligro | 2004 | `descargos-arrojar-via-objeto-puede-causar-incendio-1619` |
| 1620 | Descargos por no señalizar obstáculos o peligros creados en la vía | 2004 | `descargos-no-senalizar-obstaculos-peligros-creados-via-1620` |
| 1621 | Descargos por conducción negligente o temeraria | 2004 | `descargos-conduccion-negligente-temeraria-1621` |
| 1622 | Descargos por entorpecer la circulación o causar peligro, molestias o daños | 2004 | `descargos-entorpecer-circulacion-causar-peligro-1622` |
| 1623 | Descargos por velocidades prevalentes sobre la máxima | 2004 | `descargos-velocidades-prevalentes-sobre-maxima-1623` |
| 1624 | Descargos por sentido de circulación en refugios, isletas y dispositivos de guía | 2004 | `descargos-sentido-circulacion-refugios-isletas-1624` |
| 1625 | Descargos por exceso de velocidad fuera de poblado | 2004 | `descargos-exceso-velocidad-fuera-poblado-1625` |
| 1626 | Descargos por la forma de reducir la velocidad | 2004 | `descargos-forma-reducir-velocidad-1626` |
| 1627 | Descargos por no moderar la velocidad | 2004 | `descargos-no-moderar-velocidad-1627` |
| 1628 | Descargos por velocidad mínima en poblado y fuera de poblado | 2004 | `descargos-velocidad-minima-poblado-fuera-poblado-1628` |
| 1629 | Descargos por uso indebido de vías divididas en dos o tres calzadas | 2004 | `descargos-uso-indebido-vias-divididas-dos-tres-calzadas-1629` |
| 1630 | Descargos por inmovilizar el vehículo y caída de la carga | 2004 | `descargos-inmovilizar-vehiculo-caida-carga-1630` |
| 1631 | Descargos por desobedecer señales u órdenes de la autoridad o sus agentes | 2004 | `descargos-desobedecer-senales-u-ordenes-autoridad-1631` |
| 1632 | Descargos por semáforo para peatones | 2004 | `descargos-semaforo-peatones-1632` |
| 1633 | Descargos por formato de las señales | 2004 | `descargos-formato-senales-1633` |
| 1634 | Descargos por semáforos cuadrados o de carril | 2004 | `descargos-semaforos-cuadrados-carril-1634` |
| 1635 | Descargos por semáforos reservados | 2004 | `descargos-semaforos-reservados-1635` |
| 1636 | Descargos por saltarse un semáforo circular | 2004 | `descargos-saltarse-semaforo-circular-1636` |
| 1637 | Descargos por señales de balizamiento | 2004 | `descargos-senales-balizamiento-1637` |
| 1638 | Descargos por retirar, sustituir o alterar señales | 2004 | `descargos-retirar-sustituir-alterar-senales-1638` |
| 1639 | Descargos por adelantar por la izquierda | 2004 | `descargos-adelantar-izquierda-1639` |
| 1640 | Descargos por adelantar con obstáculos | 2004 | `descargos-adelantar-obstaculos-1640` |
| 1641 | Descargos por obligaciones de quien adelanta | 2004 | `descargos-obligaciones-quien-adelanta-1641` |
| 1642 | Descargos por parada y estacionamiento | 2004 | `descargos-parada-estacionamiento-1642` |
| 1643 | Descargos por obligaciones del conductor adelantado | 2004 | `descargos-obligaciones-conductor-adelantado-1643` |
| 1644 | Descargos por maniobra de parada y estacionamiento | 2004 | `descargos-maniobra-parada-estacionamiento-1644` |
| 1645 | Descargos por adelantamiento en supuestos especiales | 2004 | `descargos-adelantamiento-supuestos-especiales-1645` |
| 1646 | Descargos por maniobra de adelantamiento | 2004 | `descargos-maniobra-adelantamiento-1646` |
| 1647 | Descargos por advertencias ópticas | 2004 | `descargos-advertencias-opticas-1647` |
| 1648 | Descargos por supuestos especiales de alumbrado | 2004 | `descargos-supuestos-especiales-alumbrado-1648` |
| 1649 | Descargos por inmovilizaciones | 2004 | `descargos-inmovilizaciones-1649` |
| 1650 | Descargos por alumbrado de la placa de matrícula | 2004 | `descargos-alumbrado-placa-matricula-1650` |
| 1651 | Descargos por alumbrado de cruce | 2004 | `descargos-alumbrado-cruce-1651` |
| 1652 | Descargos por alumbrado inutilizado o averiado | 2004 | `descargos-alumbrado-inutilizado-averiado-1652` |
| 1653 | Descargos por deslumbramiento | 2004 | `descargos-deslumbramiento-1653` |
| 1654 | Descargos por parar o estacionar en lugar prohibido | 2004 | `descargos-parar-estacionar-lugar-prohibido-1654` |
| 1655 | Descargos por pasos a nivel y puentes móviles | 2004 | `descargos-pasos-nivel-puentes-moviles-1655` |
| 1656 | Descargos por barreras, semibarreras y semáforos | 2004 | `descargos-barreras-semibarreras-semaforos-1656` |
| 1657 | Descargos por alumbrado de posición y gálibo | 2004 | `descargos-alumbrado-posicion-galibo-1657` |
| 1658 | Descargos por infringir ordenanzas municipales de parada y estacionamiento | 2004 | `descargos-infringir-ordenanzas-municipales-parada-1658` |
| 1659 | Descargos por detenerse en paso a nivel, puente móvil o túnel | 2004 | `descargos-detenerse-paso-nivel-puente-movil-tunel-1659` |
| 1660 | Descargos por colocación del vehículo al estacionar | 2004 | `descargos-colocacion-vehiculo-estacionar-1660` |
| 1661 | Descargos por alumbrado de carretera | 2004 | `descargos-alumbrado-carretera-1661` |
| 1662 | Descargos por incorporación a la circulación | 2004 | `descargos-incorporacion-circulacion-1662` |
| 1663 | Descargos por vehículos prioritarios | 2004 | `descargos-vehiculos-prioritarios-1663` |
| 1664 | Descargos por no ceder prioridad a animales | 2004 | `descargos-no-ceder-prioridad-animales-1664` |
| 1665 | Descargos por prioridad en tramos de gran pendiente | 2004 | `descargos-prioridad-tramos-gran-pendiente-1665` |
| 1666 | Descargos por no ceder prioridad a peatones | 2004 | `descargos-no-ceder-prioridad-peatones-1666` |
| 1667 | Descargos por vehículos y transportes especiales | 2004 | `descargos-vehiculos-transportes-especiales-1667` |
| 1668 | Descargos por vehículos no prioritarios en servicio de urgencia | 2004 | `descargos-vehiculos-no-prioritarios-servicio-urgencia-1668` |
| 1669 | Descargos por conducta ante vehículos prioritarios | 2004 | `descargos-conducta-ante-vehiculos-prioritarios-1669` |
| 1670 | Descargos por facultades de conductores de vehículos prioritarios | 2004 | `descargos-facultades-conductores-vehiculos-prioritarios-1670` |
| 1671 | Descargos por transportes terrestres por carretera | 2004 | `descargos-transportes-terrestres-carretera-1671` |
| 1672 | Descargos por casco y otros elementos de protección | 2004 | `descargos-casco-otros-elementos-proteccion-1672` |
| 1673 | Descargos por advertencias a otros vehículos | 2004 | `descargos-advertencias-otros-vehiculos-1673` |
| 1674 | Descargos por no apagar el motor | 2004 | `descargos-no-apagar-motor-1674` |
| 1675 | Descargos por advertencias de vehículos de urgencia y especiales | 2004 | `descargos-advertencias-vehiculos-urgencia-especiales-1675` |
| 1676 | Descargos por puertas del vehículo | 2004 | `descargos-puertas-vehiculo-1676` |
| 1677 | Descargos por cinturón o sistema de retención infantil | 2004 | `descargos-cinturon-sistema-retencion-infantil-1677` |
| 1678 | Descargos por no auxiliar en accidente | 2004 | `descargos-no-auxiliar-accidente-1678` |
| 1679 | Descargos de peatón por circular de noche | 2004 | `descargos-peaton-circular-noche-1679` |
| 1680 | Descargos por animales en autopistas y autovías | 2004 | `descargos-animales-autopistas-autovias-1680` |
| 1681 | Descargos por circular por zona peatonal | 2004 | `descargos-circular-zona-peatonal-1681` |
| 1682 | Descargos de peatón por cruzar la calzada | 2004 | `descargos-peaton-cruzar-calzada-1682` |
| 1683 | Descargos de peatón por circular en autopista o autovía | 2004 | `descargos-peaton-circular-autopista-autovia-1683` |
| 1684 | Descargos de peatón por circular por calzada o arcén | 2004 | `descargos-peaton-circular-calzada-arcen-1684` |
| 1685 | Descargos por circulación de animales: normas generales | 2004 | `descargos-circulacion-animales-normas-generales-1685` |
| 1686 | Descargos por cambio de dirección en supuestos especiales | 2004 | `descargos-cambio-direccion-supuestos-especiales-1686` |
| 1687 | Descargos por maniobra de cambio de dirección | 2004 | `descargos-maniobra-cambio-direccion-1687` |
| 1688 | Descargos por marcha atrás: normas generales | 2004 | `descargos-marcha-atras-normas-generales-1688` |
| 1689 | Descargos por carril de deceleración | 2004 | `descargos-carril-deceleracion-1689` |
| 1690 | Descargos por maniobra de marcha atrás | 2004 | `descargos-maniobra-marcha-atras-1690` |
| 1691 | Descargos por incorporación de vehículos de transporte de viajeros | 2004 | `descargos-incorporacion-vehiculos-transporte-viajeros-1691` |
| 1692 | Descargos por cambio de dirección: normas generales | 2004 | `descargos-cambio-direccion-normas-generales-1692` |
| 1693 | Descargos por maniobra de cambio de sentido | 2004 | `descargos-maniobra-cambio-sentido-1693` |
| 1694 | Descargos por prioridad de paso sin señalización | 2004 | `descargos-prioridad-paso-sin-senalizacion-1694` |
| 1695 | Descargos por prioridad de paso en obras y estrechamientos | 2004 | `descargos-prioridad-paso-obras-estrechamientos-1695` |
| 1696 | Descargos por detenerse indebidamente en una intersección | 2004 | `descargos-detenerse-indebidamente-interseccion-1696` |
| 1697 | Descargos por prioridad en intersección sin señalizar | 2004 | `descargos-prioridad-interseccion-sin-senalizar-1697` |
| 1698 | Descargos por no guardar la distancia entre vehículos | 2004 | `descargos-no-guardar-distancia-entre-vehiculos-1698` |
| 1699 | Descargos por prioridad en puentes y obras señalizadas | 2004 | `descargos-prioridad-puentes-obras-senalizadas-1699` |
| 1700 | Descargos por competiciones deportivas | 2004 | `descargos-competiciones-deportivas-1700` |
| 1701 | Descargos por normas generales de prioridad de paso | 2004 | `descargos-normas-generales-prioridad-paso-1701` |
| 1758 | Alegaciones del interesado en la reposición por infracciones de tráfico | 2004 | `alegaciones-interesado-reposicion-infracciones-trafico-1758` |
| 1908 | Alegaciones al inicio por insuficiencia de prueba de cargo en denuncia de tráfico | 2012 | `alegaciones-inicio-insuficiencia-prueba-cargo-denuncia-1908` |
| 1912 | Alegaciones al inicio pidiendo pruebas sobre el aparato medidor de velocidad | 2012 | `alegaciones-inicio-pidiendo-pruebas-sobre-aparato-1912` |
| 1916 | Alegaciones a la propuesta pidiendo pruebas en denuncia de controlador de estacionamiento | 2012 | `alegaciones-propuesta-pidiendo-pruebas-denuncia-1916` |

## Solicitudes y expedientes (24)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 168 | Petición de información al juzgado por proceso penal sobre los mismos hechos | 2017 | `peticion-informacion-juzgado-proceso-penal-sobre-mismos-168` |
| 213 | Reclamar a la Administración por accidente de circulación con vehículo de su propiedad | 2016 | `reclamar-administracion-accidente-circulacion-vehiculo-213` |
| 227 | Petición razonada de otros órganos para iniciar un sancionador de tráfico | 2016 | `peticion-razonada-otros-organos-iniciar-sancionador-227` |
| 321 | Pedir la baja de la dirección electrónica vial | 2013 | `pedir-baja-direccion-electronica-vial-321` |
| 322 | Pedir la dirección electrónica vial | 2013 | `pedir-direccion-electronica-vial-322` |
| 908 | Pedir medidas cautelares en tráfico y seguridad vial | 2009 | `pedir-medidas-cautelares-trafico-seguridad-vial-908` |
| 1711 | Solicitud de autorización administrativa en materia de reglamentación de vehículos | 2004 | `solicitud-autorizacion-administrativa-materia-1711` |
| 1712 | Solicitud de autorización administrativa para actividades sujetas a la reglamentación de conductores | 2004 | `solicitud-autorizacion-administrativa-actividades-1712` |
| 1714 | Petición de dictamen al órgano consultivo en la responsabilidad patrimonial por daños de circulación | 2004 | `peticion-dictamen-organo-consultivo-responsabilidad-1714` |
| 1716 | Solicitud de autorización para una escuela particular de conductores | 2004 | `solicitud-autorizacion-escuela-particular-conductores-1716` |
| 1718 | Solicitud de autorización de apertura de una Inspección Técnica de Vehículos | 2004 | `solicitud-autorizacion-apertura-inspeccion-tecnica-1718` |
| 1721 | Solicitud de autorización para un centro de reconocimiento de conductores | 2004 | `solicitud-autorizacion-centro-reconocimiento-conductores-1721` |
| 1722 | Solicitud de autorización para inscribir, ampliar o trasladar talleres de reparación de vehículos | 2004 | `solicitud-autorizacion-inscribir-ampliar-trasladar-1722` |
| 1723 | Solicitud de autorización para un centro de recogida de vehículos fuera de uso | 2004 | `solicitud-autorizacion-centro-recogida-vehiculos-fuera-1723` |
| 1725 | Solicitud de autorización de pruebas deportivas por el casco urbano | 2004 | `solicitud-autorizacion-pruebas-deportivas-casco-urbano-1725` |
| 1726 | Solicitud de autorización para una prueba deportiva | 2004 | `solicitud-autorizacion-prueba-deportiva-1726` |
| 1730 | Solicitud de incorporación de una entidad privada al Consejo Superior de Tráfico y Seguridad Vial | 2004 | `solicitud-incorporacion-entidad-privada-consejo-superior-1730` |
| 1733 | Pedir la rectificación de errores en una autorización de tráfico | 2004 | `pedir-rectificacion-errores-autorizacion-trafico-1733` |
| 1734 | Solicitud de medalla al mérito de la seguridad vial | 2004 | `solicitud-medalla-merito-seguridad-vial-1734` |
| 1736 | Pedir certificación de sanciones anotadas en Registros | 2004 | `pedir-certificacion-sanciones-anotadas-registros-1736` |
| 1737 | Pedir la cancelación de anotación en el Registro de Conductores e Infractores | 2004 | `pedir-cancelacion-anotacion-registro-conductores-e-1737` |
| 1746 | Pedir que se declare de oficio la nulidad de una sanción de tráfico | 2004 | `pedir-declare-oficio-nulidad-sancion-trafico-1746` |
| 1817 | Pedir la revocación de una sanción dictada por una Jefatura de Tráfico | 2004 | `pedir-revocacion-sancion-dictada-jefatura-trafico-1817` |
| 1824 | Pedir certificación de caducidad del procedimiento sancionador | 2004 | `pedir-certificacion-caducidad-procedimiento-sancionador-1824` |

## Escritos de trámite (20)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 165 | Propuesta de resolución en sancionador de tráfico | 2017 | `propuesta-resolucion-sancionador-trafico-165` |
| 169 | Queja por defectos de tramitación en el expediente sancionador | 2017 | `queja-defectos-tramitacion-expediente-sancionador-169` |
| 171 | Instructor que pide colaboración a otros órganos en el expediente sancionador | 2017 | `instructor-pide-colaboracion-otros-organos-expediente-171` |
| 175 | Comunicar el pago voluntario de la multa y pedir la terminación del procedimiento | 2017 | `comunicar-pago-voluntario-multa-pedir-terminacion-175` |
| 184 | Descargos generales contra denuncia de tráfico ante la Jefatura de Tráfico | 2016 | `descargos-generales-contra-denuncia-trafico-ante-184` |
| 189 | Alegaciones generales contra denuncia de tráfico ante una Alcaldía | 2016 | `alegaciones-generales-contra-denuncia-trafico-ante-189` |
| 194 | Recusación del instructor en un sancionador de tráfico | 2016 | `recusacion-instructor-sancionador-trafico-194` |
| 209 | Contestar excusando la identificación del conductor responsable | 2016 | `contestar-excusando-identificacion-conductor-responsable-209` |
| 212 | Devolver una denuncia de tráfico notificada indebidamente | 2016 | `devolver-denuncia-trafico-notificada-indebidamente-212` |
| 215 | Denuncia de un particular por hechos ajenos a la circulación | 2016 | `denuncia-particular-hechos-ajenos-circulacion-215` |
| 221 | Personación de terceros interesados en un sancionador de tráfico | 2016 | `personacion-terceros-interesados-sancionador-trafico-221` |
| 225 | Contestación al requerimiento de información previa en una denuncia de tráfico | 2016 | `contestacion-requerimiento-informacion-previa-denuncia-225` |
| 297 | Anunciar recurso en sancionador abreviado de tráfico | 2014 | `anunciar-recurso-sancionador-abreviado-trafico-297` |
| 309 | Reposición contra multa de tráfico | 2013 | `reposicion-contra-multa-trafico-309` |
| 325 | Alegaciones generales contra denuncia de tráfico | 2013 | `alegaciones-generales-contra-denuncia-trafico-325` |
| 704 | Alegaciones o descargos en sancionador de tráfico | 2010 | `alegaciones-descargos-sancionador-trafico-704` |
| 1731 | Solicitud de subvención para actividades de seguridad vial o transporte por carretera | 2004 | `solicitud-subvencion-actividades-seguridad-vial-1731` |
| 1735 | Oferta de convenio de colaboración con la Administración de tráfico para fomentar la seguridad vial | 2004 | `oferta-convenio-colaboracion-administracion-trafico-1735` |
| 1747 | Pedir certificado del transcurso del plazo para resolver la reposición contra una sanción de tráfico | 2004 | `pedir-certificado-transcurso-plazo-resolver-reposicion-1747` |
| 1816 | Remisión de la autorización suspendida en un procedimiento sancionador | 2004 | `remision-autorizacion-suspendida-procedimiento-1816` |

## Actos y resoluciones de la Administración o del órgano judicial (42)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 144 | Notificación de la resolución sancionadora de la Jefatura de Tráfico | 2017 | `notificacion-resolucion-sancionadora-jefatura-trafico-144` |
| 145 | Notificación de la resolución sancionadora de tráfico de una Alcaldía | 2017 | `notificacion-resolucion-sancionadora-trafico-alcaldia-145` |
| 150 | Resolución sancionadora de una Jefatura de Tráfico | 2017 | `resolucion-sancionadora-jefatura-trafico-150` |
| 151 | Resolución que declara improcedente sancionar si no se identifica al autor | 2017 | `resolucion-declara-improcedente-sancionar-si-no-151` |
| 152 | Resolución sancionadora de tráfico de una Alcaldía | 2017 | `resolucion-sancionadora-trafico-alcaldia-152` |
| 154 | Resolución que declara inexistente la infracción por hechos no constitutivos de ella | 2017 | `resolucion-declara-inexistente-infraccion-hechos-no-154` |
| 166 | Acuerdo que paraliza el sancionador por proceso penal sobre los mismos hechos | 2017 | `acuerdo-paraliza-sancionador-proceso-penal-sobre-mismos-166` |
| 167 | Traslado de actuaciones del instructor al órgano resolutor | 2017 | `traslado-actuaciones-instructor-organo-resolutor-167` |
| 170 | Notificar al interesado la propuesta de resolución | 2017 | `notificar-interesado-propuesta-resolucion-170` |
| 172 | Resolución que deniega las pruebas propuestas por el inculpado | 2017 | `resolucion-deniega-pruebas-propuestas-inculpado-172` |
| 173 | Informe del instructor que propone sobreseer por no ser infracción los hechos | 2017 | `informe-instructor-propone-sobreseer-no-ser-infraccion-173` |
| 186 | Pedir al agente denunciante que ratifique la denuncia | 2016 | `pedir-agente-denunciante-ratifique-denuncia-186` |
| 188 | Resolución que adopta medidas cautelares en tráfico y seguridad vial | 2016 | `resolucion-adopta-medidas-cautelares-trafico-seguridad-188` |
| 190 | Acuerdo que inicia o reanuda el sancionador tras proceso penal sin responsabilidad penal | 2016 | `acuerdo-inicia-reanuda-sancionador-tras-proceso-penal-190` |
| 203 | Notificación por edictos de denuncia o incoación en sancionador de tráfico | 2016 | `notificacion-edictos-denuncia-incoacion-sancionador-203` |
| 208 | Notificar al inculpado el inicio del sancionador acordado de oficio | 2016 | `notificar-inculpado-inicio-sancionador-acordado-oficio-208` |
| 210 | Diligencia de comparecencia del titular del vehículo que identifica al responsable | 2016 | `diligencia-comparecencia-titular-vehiculo-identifica-210` |
| 211 | Incoación de oficio de sancionador de tráfico y seguridad vial | 2016 | `incoacion-oficio-sancionador-trafico-seguridad-vial-211` |
| 216 | Boletín de denuncia de tráfico y seguridad vial | 2016 | `boletin-denuncia-trafico-seguridad-vial-216` |
| 217 | Requerir al titular que identifique al conductor infractor | 2016 | `requerir-titular-identifique-conductor-infractor-217` |
| 218 | Notificar denuncia y requerir la identificación del conductor | 2016 | `notificar-denuncia-requerir-identificacion-conductor-218` |
| 219 | Acuerdo que declara improcedente iniciar sancionador por prescripción | 2016 | `acuerdo-declara-improcedente-iniciar-sancionador-219` |
| 220 | Requerimiento de información previa a los presuntos responsables de la infracción de tráfico | 2016 | `requerimiento-informacion-previa-presuntos-responsables-220` |
| 222 | Oficio que informa de la incoación al órgano autor de la petición razonada | 2016 | `oficio-informa-incoacion-organo-autor-peticion-razonada-222` |
| 224 | Iniciar sancionador de tráfico por orden superior | 2016 | `iniciar-sancionador-trafico-orden-superior-224` |
| 323 | Requerir la baja o anulación de la dirección electrónica vial | 2013 | `requerir-baja-anulacion-direccion-electronica-vial-323` |
| 1710 | Dictamen del órgano consultivo sobre responsabilidad patrimonial por daños de circulación | 2004 | `dictamen-organo-consultivo-sobre-responsabilidad-1710` |
| 1720 | Autorización para una actividad regulada por la legislación de tráfico y seguridad vial | 2004 | `autorizacion-actividad-regulada-legislacion-trafico-1720` |
| 1744 | Oficio para comprobar la veracidad de una denuncia anónima | 2004 | `oficio-comprobar-veracidad-denuncia-anonima-1744` |
| 1745 | Certificación de descubierto para iniciar la vía de apremio | 2004 | `certificacion-descubierto-iniciar-via-apremio-1745` |
| 1751 | Acuerdo de inicio de oficio de la revisión de sanciones de tráfico nulas | 2004 | `acuerdo-inicio-oficio-revision-sanciones-trafico-nulas-1751` |
| 1753 | Citación para practicar las pruebas del expediente sancionador | 2004 | `citacion-practicar-pruebas-expediente-sancionador-1753` |
| 1755 | Acta de ratificación del agente denunciante | 2004 | `acta-ratificacion-agente-denunciante-1755` |
| 1756 | Traslado al denunciante de las alegaciones del inculpado a la propuesta de resolución | 2004 | `traslado-denunciante-alegaciones-inculpado-propuesta-1756` |
| 1757 | Informe del denunciante frente a las alegaciones del denunciado a la propuesta | 2004 | `informe-denunciante-frente-alegaciones-denunciado-1757` |
| 1762 | Sobreseimiento del expediente por prescripción de la sanción | 2004 | `sobreseimiento-expediente-prescripcion-sancion-1762` |
| 1812 | Acta de la denuncia verbal de un particular | 2004 | `acta-denuncia-verbal-particular-1812` |
| 1813 | Sobreseimiento de una denuncia anónima de tráfico | 2004 | `sobreseimiento-denuncia-anonima-trafico-1813` |
| 1818 | Resolución que anula actos de tráfico gravemente contrarios al ordenamiento | 2004 | `resolucion-anula-actos-trafico-gravemente-contrarios-1818` |
| 1819 | Suspensión de la ejecución de un acto de tráfico en la revisión de actos nulos | 2004 | `suspension-ejecucion-acto-trafico-revision-actos-nulos-1819` |
| 1822 | Traslado de la reposición contra sanción de tráfico a los demás interesados | 2004 | `traslado-reposicion-contra-sancion-trafico-demas-1822` |
| 1823 | Sobreseimiento del expediente sancionador por perención | 2004 | `sobreseimiento-expediente-sancionador-perencion-1823` |

## Contratos, escrituras y documentos (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1708 | Convenio entre una Administración y una entidad privada para fomentar la seguridad vial | 2004 | `convenio-entre-administracion-entidad-privada-fomentar-1708` |
| 1728 | Modelo de estatutos de asociación de seguridad vial o de víctimas de accidentes de tráfico | 2004 | `modelo-estatutos-asociacion-seguridad-vial-victimas-1728` |
| 1729 | Solicitud y adhesión para una distinción honorífica en tráfico, transportes o seguridad vial | 2004 | `solicitud-adhesion-distincion-honorifica-trafico-1729` |

## Comunicaciones, requerimientos y reclamaciones (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 164 | Comunicar a otros órganos indicios de infracción | 2017 | `comunicar-otros-organos-indicios-infraccion-164` |
| 1707 | Reclamación de la aseguradora por lo pagado a su asegurado en un accidente de circulación | 2004 | `reclamacion-aseguradora-lo-pagado-asegurado-accidente-1707` |
| 1719 | Denuncia de un usuario contra un taller por incumplir las condiciones de su autorización | 2004 | `denuncia-usuario-contra-taller-incumplir-condiciones-1719` |
| 1742 | Denuncia de un particular por infracciones de tráfico y seguridad vial | 2004 | `denuncia-particular-infracciones-trafico-seguridad-vial-1742` |
| 1814 | Oposición del interesado a entregar la autorización administrativa | 2004 | `oposicion-interesado-entregar-autorizacion-1814` |

## Otros (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 178 | Remitir al Ministerio Fiscal las actuaciones del sancionador | 2017 | `remitir-ministerio-fiscal-actuaciones-sancionador-178` |
| 591 | Titular que identifica al conductor del vehículo | 2011 | `titular-identifica-conductor-vehiculo-591` |
| 592 | Defecto de tramitación: falta de práctica, solicitud de prueba | 2011 | `defecto-tramitacion-falta-practica-solicitud-prueba-592` |
| 593 | Defecto de tramitación: ausencia de informe del denunciante | 2011 | `defecto-tramitacion-ausencia-informe-denunciante-593` |
| 594 | Alegaciones: multa superior a la prevista | 2011 | `alegaciones-multa-superior-prevista-594` |
| 596 | Defecto de tramitación: no se dio plazo para alegar | 2011 | `defecto-tramitacion-no-dio-plazo-alegar-596` |
| 597 | Alegar la caducidad del procedimiento | 2011 | `alegar-caducidad-procedimiento-597` |
| 598 | Alegaciones por conducir sin la autorización administrativa | 2011 | `alegaciones-conducir-sin-autorizacion-administrativa-598` |
| 599 | Alegaciones por saltarse un semáforo en rojo | 2011 | `alegaciones-saltarse-semaforo-rojo-599` |
| 1732 | Memoria para la incorporación de una entidad privada a un órgano colegiado de seguridad vial | 2004 | `memoria-incorporacion-entidad-privada-organo-colegiado-1732` |
| 1754 | Acuse de recibo e información sobre los trámites de una denuncia de particulares | 2004 | `acuse-recibo-e-informacion-sobre-tramites-denuncia-1754` |
| 1815 | Orden al infractor de entregar el documento de la autorización suspendida | 2004 | `orden-infractor-entregar-documento-autorizacion-1815` |
