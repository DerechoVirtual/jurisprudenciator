---
name: indice
description: "Índice de los 83 formularios de delitos contra el patrimonio (hurto, robo, estafa, apropiación indebida, administración desleal, usurpación y ocupación, insolvencias, falsedades). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Delitos contra el patrimonio: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Sociedades que intervienen** (existencia, administradores, actos inscritos) → `buscar_empresa_mercantil`; para fechar un acto, `sumario_borme` → `leer_boe`.
- **Inmuebles** (referencia catastral, superficie, uso) → `consultar_catastro` (y `callejero_catastro` para localizar la dirección).

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/delitos-contra-el-patrimonio:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (14)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1 | Hurto de productos agrarios o ganaderos: defensa con conformidad | 2026 | `hurto-productos-agrarios-ganaderos-defensa-conformidad-1` |
| 15 | Estafa multirreincidente o leve agravada: conformidad de la defensa | 2026 | `estafa-multirreincidente-leve-agravada-conformidad-15` |
| 21 | Hurto de móvil: defensa con conformidad | 2026 | `hurto-movil-defensa-conformidad-21` |
| 26 | Delito continuado: conformidad de la defensa admitiendo la unidad natural de acción | 2026 | `delito-continuado-conformidad-defensa-admitiendo-unidad-26` |
| 83 | Estafa del inquilino que no paga el alquiler (inquiokupación): conformidad del arrendatario | 2023 | `estafa-inquilino-no-paga-alquiler-inquiokupacion-83` |
| 140 | Hurto multirreincidente: conformidad de la defensa | 2023 | `hurto-multirreincidente-conformidad-defensa-140` |
| 392 | Insolvencia punible: conformidad de la defensa | 2020 | `insolvencia-punible-conformidad-defensa-392` |
| 402 | Defraudación de fluido eléctrico: conformidad de la defensa | 2020 | `defraudacion-fluido-electrico-conformidad-defensa-402` |
| 406 | Allanamiento de morada por ocupación de inmueble: conformidad de la defensa | 2020 | `allanamiento-morada-ocupacion-inmueble-conformidad-406` |
| 425 | Administración desleal: conformidad de la defensa | 2020 | `administracion-desleal-conformidad-defensa-425` |
| 445 | Alzamiento de bienes (frustración de la ejecución): defensa con conformidad | 2020 | `alzamiento-bienes-frustracion-ejecucion-defensa-445` |
| 447 | Apropiación indebida: defensa con conformidad | 2020 | `apropiacion-indebida-defensa-conformidad-447` |
| 861 | Usurpación de inmueble con violencia (okupas): defensa con conformidad en el abreviado | 2016 | `usurpacion-inmueble-violencia-okupas-defensa-conformidad-861` |
| 864 | Hurto: defensa con conformidad | 2016 | `hurto-defensa-conformidad-864` |

## Recursos e impugnaciones (19)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 3 | Hurto de productos agrarios o ganaderos: apelación del acusado contra la sentencia | 2026 | `hurto-productos-agrarios-ganaderos-apelacion-acusado-3` |
| 5 | Hurto de productos agrarios o ganaderos: apelación de la acusación contra la sentencia | 2026 | `hurto-productos-agrarios-ganaderos-apelacion-acusacion-5` |
| 17 | Estafa multirreincidente o leve agravada: apelación contra la condena | 2026 | `estafa-multirreincidente-leve-agravada-apelacion-contra-17` |
| 19 | Hurto de móvil: apelación del condenado contra la sentencia | 2026 | `hurto-movil-apelacion-condenado-contra-sentencia-19` |
| 20 | Hurto de móvil: apelación de la acusación contra la sentencia | 2026 | `hurto-movil-apelacion-acusacion-contra-sentencia-20` |
| 28 | Delito continuado: apelación contra la condena pidiendo la unidad natural de acción | 2026 | `delito-continuado-apelacion-contra-condena-pidiendo-28` |
| 82 | Estafa del inquilino que no paga el alquiler (inquiokupación): apelación contra la condena | 2023 | `estafa-inquilino-no-paga-alquiler-inquiokupacion-82` |
| 136 | Hurto multirreincidente: apelación contra la condena | 2023 | `hurto-multirreincidente-apelacion-contra-condena-136` |
| 377 | Usurpación de inmueble: el propietario se opone a que se suspenda el desahucio | 2021 | `usurpacion-inmueble-propietario-opone-suspenda-desahucio-377` |
| 391 | Insolvencia punible: apelación contra la condena | 2020 | `insolvencia-punible-apelacion-contra-condena-391` |
| 399 | Defraudación de fluido eléctrico: apelación contra la condena | 2020 | `defraudacion-fluido-electrico-apelacion-contra-condena-399` |
| 404 | Allanamiento de morada por ocupación de inmueble: apelación contra la condena | 2020 | `allanamiento-morada-ocupacion-inmueble-apelacion-contra-404` |
| 424 | Administración desleal: apelación contra la condena | 2020 | `administracion-desleal-apelacion-contra-condena-424` |
| 444 | Apelación contra la condena por alzamiento de bienes (frustración de la ejecución) | 2020 | `apelacion-contra-condena-alzamiento-bienes-frustracion-444` |
| 448 | Apelación contra la condena por apropiación indebida | 2020 | `apelacion-contra-condena-apropiacion-indebida-448` |
| 485 | Apelación contra la condena por robo de uso de vehículo de motor | 2019 | `apelacion-contra-condena-robo-uso-vehiculo-motor-485` |
| 852 | Apelación contra la condena por falsedad en documento privado y estafa | 2016 | `apelacion-contra-condena-falsedad-documento-privado-852` |
| 858 | Apelación contra la condena por usurpación de inmueble con violencia (okupas) | 2016 | `apelacion-contra-condena-usurpacion-inmueble-violencia-858` |
| 862 | Apelación contra la condena por hurto | 2016 | `apelacion-contra-condena-hurto-862` |

## Querellas y denuncias (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 16 | Estafa multirreincidente o leve agravada: querella | 2026 | `estafa-multirreincidente-leve-agravada-querella-16` |
| 27 | Delito continuado: querella | 2026 | `delito-continuado-querella-27` |
| 81 | Estafa del inquilino que no paga el alquiler (inquiokupación): querella | 2023 | `estafa-inquilino-no-paga-alquiler-inquiokupacion-81` |
| 129 | Daños: denuncia escrita ante la policía | 2023 | `danos-denuncia-escrita-ante-policia-129` |
| 138 | Hurto multirreincidente: querella | 2023 | `hurto-multirreincidente-querella-138` |
| 235 | Alteración de lindes: denuncia | 2022 | `alteracion-lindes-denuncia-235` |
| 394 | Insolvencia punible: querella | 2020 | `insolvencia-punible-querella-394` |
| 407 | Ocupación pacífica de inmueble que no es morada: denuncia | 2020 | `ocupacion-pacifica-inmueble-no-es-morada-denuncia-407` |
| 408 | Allanamiento de morada por ocupación de inmueble: denuncia | 2020 | `allanamiento-morada-ocupacion-inmueble-denuncia-408` |
| 410 | Defraudación de fluido eléctrico: denuncia | 2020 | `defraudacion-fluido-electrico-denuncia-410` |
| 423 | Administración desleal: querella | 2020 | `administracion-desleal-querella-423` |
| 520 | Estafa y falsedad en documento público: querella | 2019 | `estafa-falsedad-documento-publico-querella-520` |
| 855 | Usurpación de inmueble con violencia (okupas): querella | 2016 | `usurpacion-inmueble-violencia-okupas-querella-855` |
| 863 | Hurto: denuncia | 2016 | `hurto-denuncia-863` |
| 872 | Hurto de uso de vehículo de motor: querella | 2016 | `hurto-uso-vehiculo-motor-querella-872` |
| 873 | Robo de uso de vehículo de motor: querella | 2016 | `robo-uso-vehiculo-motor-querella-873` |

## Escritos de acusación (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 4 | Hurto de productos agrarios o ganaderos: escrito de acusación | 2026 | `hurto-productos-agrarios-ganaderos-escrito-acusacion-4` |
| 14 | Estafa multirreincidente o leve agravada: escrito de acusación | 2026 | `estafa-multirreincidente-leve-agravada-escrito-acusacion-14` |
| 23 | Hurto de móvil: escrito de acusación | 2026 | `hurto-movil-escrito-acusacion-23` |
| 30 | Delito continuado: escrito de acusación | 2026 | `delito-continuado-escrito-acusacion-30` |
| 80 | Estafa del inquilino que no paga el alquiler (inquiokupación): escrito de acusación | 2023 | `estafa-inquilino-no-paga-alquiler-inquiokupacion-escrito-80` |
| 139 | Hurto multirreincidente: escrito de acusación | 2023 | `hurto-multirreincidente-escrito-acusacion-139` |
| 390 | Insolvencia punible: escrito de acusación | 2020 | `insolvencia-punible-escrito-acusacion-390` |
| 400 | Defraudación de fluido eléctrico: escrito de acusación | 2020 | `defraudacion-fluido-electrico-escrito-acusacion-400` |
| 409 | Allanamiento de morada por ocupación de inmueble: calificación provisional de la acusación | 2020 | `allanamiento-morada-ocupacion-inmueble-calificacion-409` |
| 427 | Administración desleal: escrito de acusación | 2020 | `administracion-desleal-escrito-acusacion-427` |
| 450 | Apropiación indebida: acusación | 2020 | `apropiacion-indebida-acusacion-450` |
| 850 | Falsedad en documento mercantil en concurso medial con estafa: acusación | 2016 | `falsedad-documento-mercantil-concurso-medial-estafa-850` |
| 865 | Hurto: acusación | 2016 | `hurto-acusacion-865` |
| 866 | Usurpación de inmueble con violencia (okupas): acusación | 2016 | `usurpacion-inmueble-violencia-okupas-acusacion-866` |
| 868 | Hurto de uso de vehículo de motor: acusación | 2016 | `hurto-uso-vehiculo-motor-acusacion-868` |
| 870 | Robo de uso de vehículo de motor: acusación | 2016 | `robo-uso-vehiculo-motor-acusacion-870` |

## Escritos de defensa (17)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 2 | Hurto de productos agrarios o ganaderos: escrito de defensa | 2026 | `hurto-productos-agrarios-ganaderos-escrito-defensa-2` |
| 18 | Estafa multirreincidente o leve agravada: escrito de defensa | 2026 | `estafa-multirreincidente-leve-agravada-escrito-defensa-18` |
| 22 | Hurto de móvil: escrito de defensa | 2026 | `hurto-movil-escrito-defensa-22` |
| 29 | Delito continuado: escrito de defensa proponiendo la unidad natural de acción | 2026 | `delito-continuado-escrito-defensa-proponiendo-unidad-29` |
| 84 | Estafa del inquilino que no paga el alquiler (inquiokupación): defensa del arrendatario | 2023 | `estafa-inquilino-no-paga-alquiler-inquiokupacion-defensa-84` |
| 137 | Hurto multirreincidente: escrito de defensa | 2023 | `hurto-multirreincidente-escrito-defensa-137` |
| 393 | Insolvencia punible: escrito de defensa | 2020 | `insolvencia-punible-escrito-defensa-393` |
| 401 | Defraudación de fluido eléctrico: escrito de defensa | 2020 | `defraudacion-fluido-electrico-escrito-defensa-401` |
| 405 | Allanamiento de morada por ocupación de inmueble: calificación provisional de la defensa | 2020 | `allanamiento-morada-ocupacion-inmueble-calificacion-405` |
| 426 | Administración desleal: escrito de defensa | 2020 | `administracion-desleal-escrito-defensa-426` |
| 446 | Alzamiento de bienes (frustración de la ejecución): defensa | 2020 | `alzamiento-bienes-frustracion-ejecucion-defensa-446` |
| 449 | Apropiación indebida: defensa | 2020 | `apropiacion-indebida-defensa-449` |
| 851 | Falsedad en documento público: defensa | 2016 | `falsedad-documento-publico-defensa-851` |
| 860 | Usurpación de inmueble con violencia (okupas): defensa | 2016 | `usurpacion-inmueble-violencia-okupas-defensa-860` |
| 867 | Hurto: defensa | 2016 | `hurto-defensa-867` |
| 869 | Hurto de uso de vehículo de motor: defensa | 2016 | `hurto-uso-vehiculo-motor-defensa-869` |
| 871 | Robo de uso de vehículo de motor: defensa | 2016 | `robo-uso-vehiculo-motor-defensa-871` |

## Solicitudes y escritos de trámite (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 378 | Usurpación de inmueble: pedir que se suspenda el desahucio | 2021 | `usurpacion-inmueble-pedir-suspenda-desahucio-378` |
