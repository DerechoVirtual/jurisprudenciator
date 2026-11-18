---
name: indice
description: "Índice de los 60 formularios de capacidad y medidas de apoyo (Ley 8/2021, curatela, guarda de hecho, defensor judicial, revisión de medidas). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Capacidad y medidas de apoyo: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/capacidad-y-apoyos:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 74 | Demanda de nulidad de compraventa de inmueble sin autorización judicial del tutor o curador | 2023 | `demanda-nulidad-compraventa-inmueble-sin-autorizacion-74` |
| 141 | Demanda de medidas voluntarias de apoyo: autocuratela | 2021 | `demanda-medidas-voluntarias-apoyo-autocuratela-141` |
| 143 | Demanda de medidas judiciales de apoyo a persona con discapacidad: curatela | 2021 | `demanda-medidas-judiciales-apoyo-persona-discapacidad-143` |
| 393 | Sustitución de tutor: demanda | 2019 | `sustitucion-tutor-demanda-393` |
| 855 | Demanda de reintegración de la capacidad | 2013 | `demanda-reintegracion-capacidad-855` |
| 1456 | Demanda de nulidad matrimonial por incapacidad (canon 1095.3) | 2014 | `demanda-nulidad-matrimonial-incapacidad-canon-1095-3-1456` |

## Contestaciones, oposiciones y alegaciones (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 146 | Oposición a la provisión de medidas judiciales de apoyo | 2021 | `oposicion-provision-medidas-judiciales-apoyo-146` |
| 236 | Oposición a la rendición final de cuentas del tutor por fallecimiento del tutelado | 2020 | `oposicion-rendicion-final-cuentas-tutor-fallecimiento-236` |
| 1102 | Contestación a la demanda de medidas judiciales de apoyo a personas con discapacidad | 2013 | `contestacion-demanda-medidas-judiciales-apoyo-personas-1102` |
| 1194 | Contestación a demanda de filiación por defensor judicial del menor | 2014 | `contestacion-demanda-filiacion-defensor-judicial-menor-1194` |

## Solicitudes y expedientes (30)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 47 | Autorización judicial para vender inmuebles de persona con discapacidad (Cataluña) | 2023 | `autorizacion-judicial-vender-inmuebles-persona-47` |
| 113 | Medidas de apoyo con curatela tras suprimirse la patria potestad prorrogada | 2022 | `medidas-apoyo-curatela-tras-suprimirse-patria-potestad-113` |
| 126 | Defensor judicial y autorización para aceptar y adjudicar una herencia | 2022 | `defensor-judicial-autorizacion-aceptar-adjudicar-126` |
| 144 | Aprobación judicial de la partición hecha por un defensor judicial | 2021 | `aprobacion-judicial-particion-hecha-defensor-judicial-144` |
| 145 | Revisión de medidas de capacidad adoptadas antes de la Ley 8/2021: solicitud | 2021 | `revision-medidas-capacidad-adoptadas-antes-ley-8-2021-145` |
| 147 | Jurisdicción voluntaria para medidas judiciales de apoyo: curatela | 2021 | `jurisdiccion-voluntaria-medidas-judiciales-apoyo-147` |
| 148 | Revisión de medidas anteriores a la Ley 8/2021 en proceso de capacidad | 2021 | `revision-medidas-anteriores-ley-8-2021-proceso-capacidad-148` |
| 149 | Medidas por guarda o administración inadecuada de bienes de persona con discapacidad | 2021 | `medidas-guarda-administracion-inadecuada-bienes-persona-149` |
| 150 | Revisión de medidas de apoyo: extinguir la curatela o limitar los actos asistidos | 2021 | `revision-medidas-apoyo-extinguir-curatela-limitar-actos-150` |
| 183 | Gravamen de bienes de menor o persona con apoyos: división de cosa común | 2021 | `gravamen-bienes-menor-persona-apoyos-division-cosa-comun-183` |
| 364 | Defensor judicial como cautelar junto a la demanda de medidas de apoyo | 2019 | `defensor-judicial-como-cautelar-junto-demanda-medidas-364` |
| 377 | Constitución de tutela (art. 213.1º CC) | 2019 | `constitucion-tutela-art-213-1o-cc-377` |
| 392 | Autorización para aceptar una herencia en nombre de persona con discapacidad | 2019 | `autorizacion-aceptar-herencia-nombre-persona-392` |
| 407 | Remoción del tutor | 2018 | `remocion-tutor-407` |
| 474 | Medidas por ejercicio inadecuado de la guarda o administración de bienes (art. 158 CC) | 2017 | `medidas-ejercicio-inadecuado-guarda-administracion-474` |
| 480 | Defensor judicial por conflicto de intereses con un progenitor | 2017 | `defensor-judicial-conflicto-intereses-progenitor-480` |
| 514 | Constitución de tutela (art. 199.2º CC) | 2016 | `constitucion-tutela-art-199-2o-cc-514` |
| 651 | Habilitación de edad y defensor judicial posterior | 2015 | `habilitacion-edad-defensor-judicial-posterior-651` |
| 654 | Autorización para disponer o gravar bienes de persona con discapacidad | 2015 | `autorizacion-disponer-gravar-bienes-persona-discapacidad-654` |
| 738 | Defensor judicial para administrar bienes | 2015 | `defensor-judicial-administrar-bienes-738` |
| 748 | Medidas por ejercicio inadecuado de la guarda o administración de bienes (art. 164 CC) | 2015 | `medidas-ejercicio-inadecuado-guarda-administracion-748` |
| 753 | Autorización de gravamen o extinción de derechos reales de menor o persona con apoyos | 2015 | `autorizacion-gravamen-extincion-derechos-reales-menor-753` |
| 754 | Autorización para enajenar bienes de menores o personas con apoyos | 2015 | `autorizacion-enajenar-bienes-menores-personas-apoyos-754` |
| 755 | Autorización para transigir sobre derechos de menores o personas con apoyos | 2015 | `autorizacion-transigir-sobre-derechos-menores-personas-755` |
| 777 | Defensor judicial por no desempeño de funciones: inicio del expediente | 2015 | `defensor-judicial-no-desempeno-funciones-inicio-777` |
| 781 | Defensor judicial por conflicto de intereses con el curador: inicio del expediente | 2015 | `defensor-judicial-conflicto-intereses-curador-inicio-781` |
| 789 | Autorización judicial para vender bienes de menores o personas con apoyos | 2015 | `autorizacion-judicial-vender-bienes-menores-personas-789` |
| 799 | Autorización judicial para el titular de la patria potestad menor no emancipado | 2015 | `autorizacion-judicial-titular-patria-potestad-menor-no-799` |
| 1052 | Declaración o exhibición de documentos sobre capacidad, representación o legitimación | 2013 | `declaracion-exhibicion-documentos-sobre-capacidad-1052` |
| 1420 | Pedir que se acredite la discapacidad | 2013 | `pedir-acredite-discapacidad-1420` |

## Escritos de trámite (15)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 114 | Rendición de cuentas del tutor nombrado antes de la Ley 8/2021 | 2022 | `rendicion-cuentas-tutor-nombrado-antes-ley-8-2021-114` |
| 117 | Rendición de cuentas del tutor o curador ante el Tribunal | 2022 | `rendicion-cuentas-tutor-curador-ante-tribunal-117` |
| 247 | Excusa para ejercer la tutela (Cataluña) | 2020 | `excusa-ejercer-tutela-cataluna-247` |
| 248 | Excusa para ejercer la tutela: modelo general | 2020 | `excusa-ejercer-tutela-modelo-general-248` |
| 249 | Excusa para ejercer la tutela por causa sobrevenida | 2020 | `excusa-ejercer-tutela-causa-sobrevenida-249` |
| 250 | Excusa sobrevenida para ejercer la tutela y nombramiento de nuevo tutor (Cataluña) | 2020 | `excusa-sobrevenida-ejercer-tutela-nombramiento-nuevo-250` |
| 342 | Exhibición de documentos sobre capacidad o legitimación frente a una comunidad de bienes | 2019 | `exhibicion-documentos-sobre-capacidad-legitimacion-342` |
| 433 | Autorización judicial al curador para demandar en nombre de la persona apoyada | 2018 | `autorizacion-judicial-curador-demandar-nombre-persona-433` |
| 463 | Rendición de cuentas del defensor judicial al concluir su gestión | 2017 | `rendicion-cuentas-defensor-judicial-concluir-gestion-463` |
| 588 | Aprobación judicial de la partición de herencia pedida por el curador | 2016 | `aprobacion-judicial-particion-herencia-pedida-curador-588` |
| 681 | Oposición del tutor o curador a su remoción | 2015 | `oposicion-tutor-curador-remocion-681` |
| 733 | Autorización del tutor o curador para aceptar sin beneficio de inventario o repudiar herencia | 2015 | `autorizacion-tutor-curador-aceptar-sin-beneficio-733` |
| 791 | Informe del guardador de hecho sobre la persona y los bienes del menor o de la persona con apoyos | 2015 | `informe-guardador-hecho-sobre-persona-bienes-menor-791` |
| 793 | Comunicación del defensor judicial de que ha desaparecido la causa de su nombramiento | 2015 | `comunicacion-defensor-judicial-ha-desaparecido-causa-793` |
| 794 | Defensor judicial comunica que los representantes comparecen o acaba la habilitación | 2015 | `defensor-judicial-comunica-representantes-comparecen-794` |

## Contratos, escrituras y documentos (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 294 | Demanda de medidas de apoyo y curador para ciudadana británica residente en España | 2020 | `demanda-medidas-apoyo-curador-ciudadana-britanica-294` |
| 537 | Escritura de autotutela e instrucciones previas (Galicia) | 2016 | `escritura-autotutela-e-instrucciones-previas-galicia-537` |

## Otros (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 986 | Alegación de defecto de capacidad en la audiencia previa | 2013 | `alegacion-defecto-capacidad-audiencia-previa-986` |
| 1304 | Consentimiento del arrendador a obras de persona con discapacidad en la vivienda arrendada | 2013 | `consentimiento-arrendador-obras-persona-discapacidad-1304` |
| 1419 | Discapacidad: acreditación | 2013 | `discapacidad-acreditacion-1419` |
