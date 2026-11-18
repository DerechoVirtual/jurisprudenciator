---
name: indice
description: "Índice de los 96 formularios de órgano y postulación en el contencioso-administrativo (Tribunales de Instancia, personación, representación de las Administraciones, competencia). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Órgano y postulación en el contencioso-administrativo: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/organo-y-postulacion-contencioso:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Recursos e impugnaciones (10)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 495 | Impugnar por defecto de jurisdicción | 2012 | `impugnar-defecto-jurisdiccion-495` |
| 1067 | Reposición contra el auto que declara falta de competencia a favor del TSJ | 2008 | `reposicion-contra-auto-declara-falta-competencia-favor-1067` |
| 1087 | Reposición contra la orden a la Diputación de comparecer con procurador (órganos colegiados) | 2008 | `reposicion-contra-orden-diputacion-comparecer-procurador-1087` |
| 1088 | Reposición contra la orden al Ayuntamiento de comparecer con procurador (órganos colegiados) | 2008 | `reposicion-contra-orden-ayuntamiento-comparecer-1088` |
| 1089 | Reposición contra exigir procurador al letrado de la Diputación que defiende a un Ayuntamiento | 2008 | `reposicion-contra-exigir-procurador-letrado-diputacion-1089` |
| 1090 | Reposición contra la denegación de personación de la entidad local | 2008 | `reposicion-contra-denegacion-personacion-entidad-local-1090` |
| 1101 | Reposición contra el auto que declara falta de competencia a favor del Tribunal Supremo | 2008 | `reposicion-contra-auto-declara-falta-competencia-favor-1101` |
| 1224 | Reposición contra el auto de incompetencia territorial | 2008 | `reposicion-contra-auto-incompetencia-territorial-1224` |
| 1231 | Reposición contra el auto de falta de jurisdicción | 2008 | `reposicion-contra-auto-falta-jurisdiccion-1231` |
| 1293 | Reposición contra el auto que declara falta de competencia a favor de la Audiencia Nacional | 2008 | `reposicion-contra-auto-declara-falta-competencia-favor-1293` |

## Contestaciones, oposiciones y alegaciones (8)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 649 | Alegaciones ante declinatoria de jurisdicción en contratos públicos | 2010 | `alegaciones-ante-declinatoria-jurisdiccion-contratos-649` |
| 1115 | Alegaciones previas: falta de jurisdicción | 2008 | `alegaciones-previas-falta-jurisdiccion-1115` |
| 1281 | Alegaciones previas: falta de competencia del órgano jurisdiccional | 2008 | `alegaciones-previas-falta-competencia-organo-1281` |
| 1282 | Alegaciones del actor en la admisión del recurso defendiendo la competencia del órgano | 2008 | `alegaciones-actor-admision-recurso-defendiendo-1282` |
| 1765 | Alegaciones ante la falta de jurisdicción apreciada de oficio | 2004 | `alegaciones-ante-falta-jurisdiccion-apreciada-oficio-1765` |
| 1767 | Alegaciones ante la falta de competencia apreciada de oficio | 2004 | `alegaciones-ante-falta-competencia-apreciada-oficio-1767` |
| 8 | Alegaciones de las partes sobre el efecto de la sentencia de casación en el procedimiento | 2023 | `alegaciones-partes-sobre-efecto-sentencia-casacion-8` |
| 10 | Alegaciones sobre suspender el procedimiento por un recurso de casación similar admitido | 2023 | `alegaciones-sobre-suspender-procedimiento-recurso-10` |

## Solicitudes y expedientes (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 659 | Abogado del Estado pide suspender por posible prescripción de la sanción | 2010 | `abogado-estado-pide-suspender-posible-prescripcion-659` |
| 917 | Pedir testimonio al abogado del Estado para el apremio administrativo | 2009 | `pedir-testimonio-abogado-estado-apremio-administrativo-917` |
| 1103 | Nulidad por infracción de las normas de reparto | 2008 | `nulidad-infraccion-normas-reparto-1103` |
| 1828 | Solicitud a un órgano administrativo para promover conflicto de jurisdicción | 2004 | `solicitud-organo-administrativo-promover-conflicto-1828` |
| 1844 | Petición de provisión de fondos cuando el poderdante no la hace al procurador | 2004 | `peticion-provision-fondos-cuando-poderdante-no-hace-1844` |

## Escritos de trámite (28)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 271 | Comparecer como recurrido y oponerse a la admisión de la casación | 2016 | `comparecer-como-recurrido-oponerse-admision-casacion-271` |
| 344 | Impugnar la denegación de asistencia jurídica gratuita | 2013 | `impugnar-denegacion-asistencia-juridica-gratuita-344` |
| 410 | Personación y alegaciones de la Administración en protección de derechos fundamentales | 2012 | `personacion-alegaciones-administracion-proteccion-410` |
| 626 | Personación de un codemandado particular | 2010 | `personacion-codemandado-particular-626` |
| 656 | Personación ante la Audiencia Nacional tras la incompetencia del TSJ | 2010 | `personacion-ante-audiencia-nacional-tras-incompetencia-656` |
| 658 | Personación tras declararse incompetente el órgano por exposición razonada | 2010 | `personacion-tras-declararse-incompetente-organo-658` |
| 663 | Abogado del Estado se opone a ampliar el contencioso | 2010 | `abogado-estado-opone-ampliar-contencioso-663` |
| 666 | Personación y designación de representante de una Entidad Local en el contencioso | 2010 | `personacion-designacion-representante-entidad-local-666` |
| 671 | Personación tras inadmisión por incompetencia del orden contencioso | 2010 | `personacion-tras-inadmision-incompetencia-orden-671` |
| 884 | Personación y alegaciones sobre una cuestión de ilegalidad | 2009 | `personacion-alegaciones-sobre-cuestion-ilegalidad-884` |
| 907 | Codemandado plantea falta de jurisdicción tras la contestación | 2009 | `codemandado-plantea-falta-jurisdiccion-tras-contestacion-907` |
| 914 | Personación de los demandados | 2009 | `personacion-demandados-914` |
| 921 | Codemandado plantea falta de competencia objetiva antes de contestar | 2009 | `codemandado-plantea-falta-competencia-objetiva-antes-921` |
| 923 | Codemandado plantea incompetencia objetiva en personal (nacimiento de la relación funcionarial) | 2009 | `codemandado-plantea-incompetencia-objetiva-personal-923` |
| 931 | Personación del demandado en abreviado y proposición de prueba | 2009 | `personacion-demandado-abreviado-proposicion-prueba-931` |
| 950 | Codemandado plantea falta de jurisdicción antes de contestar | 2009 | `codemandado-plantea-falta-jurisdiccion-antes-contestar-950` |
| 1036 | Personación de la Diputación Provincial | 2008 | `personacion-diputacion-provincial-1036` |
| 1039 | Personación del Ayuntamiento | 2008 | `personacion-ayuntamiento-1039` |
| 1080 | Impugnar la reposición por falta de competencia del Juzgado de lo Contencioso | 2008 | `impugnar-reposicion-falta-competencia-juzgado-lo-1080` |
| 1083 | Impugnar la reposición por falta de jurisdicción | 2008 | `impugnar-reposicion-falta-jurisdiccion-1083` |
| 1084 | Impugnar la reposición por falta de competencia de la Audiencia Nacional | 2008 | `impugnar-reposicion-falta-competencia-audiencia-nacional-1084` |
| 1085 | Impugnar la reposición por falta de competencia ante el Juzgado Central | 2008 | `impugnar-reposicion-falta-competencia-ante-juzgado-1085` |
| 1139 | Personación como codemandado | 2008 | `personacion-como-codemandado-1139` |
| 1140 | Personación del demandado en recurso de lesividad | 2008 | `personacion-demandado-recurso-lesividad-1140` |
| 1270 | Personación del codemandado emplazado por edictos | 2008 | `personacion-codemandado-emplazado-edictos-1270` |
| 1291 | Impugnar la reposición por falta de competencia del TSJ | 2008 | `impugnar-reposicion-falta-competencia-tsj-1291` |
| 1292 | Impugnar la reposición por falta de competencia del Tribunal Supremo | 2008 | `impugnar-reposicion-falta-competencia-tribunal-supremo-1292` |
| 1892 | Personación de codemandado privado | 2004 | `personacion-codemandado-privado-1892` |

## Actos y resoluciones de la Administración o del órgano judicial (40)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 969 | Emplazamiento a los demandados | 2008 | `emplazamiento-demandados-969` |
| 1040 | Certificación del secretario municipal: acuerdo del Pleno e informe previo a las acciones (Aragón) | 2008 | `certificacion-secretario-municipal-acuerdo-pleno-e-1040` |
| 1041 | Certificación de la diputación: acuerdo del pleno e informe previo a acciones (Aragón) | 2008 | `certificacion-diputacion-acuerdo-pleno-e-informe-previo-1041` |
| 1042 | Certificado de la diputación que encomienda a sus letrados la defensa de un ayuntamiento | 2008 | `certificado-diputacion-encomienda-letrados-defensa-1042` |
| 1043 | Certificación de la diputación: acuerdo del presidente de ejercitar acciones (Galicia) | 2008 | `certificacion-diputacion-acuerdo-presidente-ejercitar-1043` |
| 1044 | Decreto de alcaldía que acuerda las acciones y designa letrado municipal y procurador | 2008 | `decreto-alcaldia-acuerda-acciones-designa-letrado-1044` |
| 1045 | Certificación del secretario municipal: acuerdo del alcalde e informe previo a las acciones | 2008 | `certificacion-secretario-municipal-acuerdo-alcalde-e-1045` |
| 1046 | Certificación del secretario municipal: acuerdo del alcalde e informe previo a las acciones (Aragón) | 2008 | `certificacion-secretario-municipal-acuerdo-alcalde-e-1046` |
| 1047 | Certificación del secretario municipal: acuerdo del Pleno e informe previo a las acciones | 2008 | `certificacion-secretario-municipal-acuerdo-pleno-e-1047` |
| 1048 | Certificación del secretario municipal que designa representante procesal | 2008 | `certificacion-secretario-municipal-designa-representante-1048` |
| 1049 | Certificación del secretario municipal: acuerdo del pleno de ejercitar acciones (Cataluña) | 2008 | `certificacion-secretario-municipal-acuerdo-pleno-1049` |
| 1050 | Certificación del secretario municipal: acuerdo del alcalde de ejercitar acciones (Aragón) | 2008 | `certificacion-secretario-municipal-acuerdo-alcalde-1050` |
| 1177 | Certificación de la diputación: acuerdo del presidente e informe previo a acciones | 2008 | `certificacion-diputacion-acuerdo-presidente-e-informe-1177` |
| 1178 | Certificación de la diputación: acuerdo del presidente e informe previo a acciones (Aragón) | 2008 | `certificacion-diputacion-acuerdo-presidente-e-informe-1178` |
| 1179 | Certificación del secretario de la diputación: acuerdo del pleno e informe previo a las acciones | 2008 | `certificacion-secretario-diputacion-acuerdo-pleno-e-1179` |
| 1181 | Certificación de la diputación: acuerdo del presidente de ejercitar acciones (Cataluña) | 2008 | `certificacion-diputacion-acuerdo-presidente-ejercitar-1181` |
| 1182 | Certificación del secretario de la diputación: acuerdo del pleno de ejercitar acciones (Cataluña) | 2008 | `certificacion-secretario-diputacion-acuerdo-pleno-1182` |
| 1184 | Certificación del secretario de la diputación: acuerdo del presidente de ejercitar acciones (Aragón) | 2008 | `certificacion-secretario-diputacion-acuerdo-presidente-1184` |
| 1185 | Certificación del secretario de la diputación: acuerdo del pleno de ejercitar acciones (Galicia) | 2008 | `certificacion-secretario-diputacion-acuerdo-pleno-1185` |
| 1186 | Certificación del secretario de la diputación: acuerdo del pleno de ejercitar acciones (Aragón) | 2008 | `certificacion-secretario-diputacion-acuerdo-pleno-1186` |
| 1187 | Certificación de la Diputación: el Presidente contesta al requerimiento y ordena acciones | 2008 | `certificacion-diputacion-presidente-contesta-1187` |
| 1189 | Certificación del secretario municipal: acuerdo del pleno de ejercitar acciones (Galicia) | 2008 | `certificacion-secretario-municipal-acuerdo-pleno-1189` |
| 1190 | Certificación de la Diputación: el Pleno contesta al requerimiento y ordena acciones | 2008 | `certificacion-diputacion-pleno-contesta-requerimiento-1190` |
| 1191 | Certificación del secretario municipal: acuerdo del pleno de ejercitar acciones (Aragón) | 2008 | `certificacion-secretario-municipal-acuerdo-pleno-1191` |
| 1192 | Certificación del secretario municipal: acuerdo del pleno de ejercitar acciones (Navarra) | 2008 | `certificacion-secretario-municipal-acuerdo-pleno-1192` |
| 1193 | Certificación del secretario municipal: acuerdo del Alcalde de ejercitar acciones (Cataluña) | 2008 | `certificacion-secretario-municipal-acuerdo-alcalde-1193` |
| 1194 | Certificación del secretario municipal: el Pleno contesta al requerimiento y ordena acciones | 2008 | `certificacion-secretario-municipal-pleno-contesta-1194` |
| 1195 | Certificación del secretario municipal: el Alcalde contesta al requerimiento y ordena acciones | 2008 | `certificacion-secretario-municipal-alcalde-contesta-1195` |
| 1196 | Certificación del secretario municipal: acuerdo del alcalde de ejercitar acciones (Galicia) | 2008 | `certificacion-secretario-municipal-acuerdo-alcalde-1196` |
| 1766 | Auto de falta de jurisdicción contencioso-administrativa a favor de la jurisdicción civil | 2004 | `auto-falta-jurisdiccion-contencioso-administrativa-favor-1766` |
| 1805 | Emplazamiento ante el órgano competente (diligencia) | 2004 | `emplazamiento-ante-organo-competente-diligencia-1805` |
| 1806 | Auto que resuelve la cuestión de competencia | 2004 | `auto-resuelve-cuestion-competencia-1806` |
| 1826 | Traslado a las partes para alegar sobre competencia apreciada de oficio | 2004 | `traslado-partes-alegar-sobre-competencia-apreciada-1826` |
| 1838 | Providencia que da traslado para alegar sobre la posible falta de jurisdicción | 2004 | `providencia-da-traslado-alegar-sobre-posible-falta-1838` |
| 1880 | Auto de falta de jurisdicción contencioso-administrativa a favor del orden social | 2004 | `auto-falta-jurisdiccion-contencioso-administrativa-favor-1880` |
| 1887 | Auto de falta de jurisdicción contencioso-administrativa a favor de la jurisdicción penal | 2004 | `auto-falta-jurisdiccion-contencioso-administrativa-favor-1887` |
| 7 | Diligencia que da plazo para alegar sobre suspender el pleito por una casación similar | 2023 | `diligencia-da-plazo-alegar-sobre-suspender-pleito-7` |
| 9 | Auto que alza la suspensión y da traslado para alegar sobre la sentencia de casación | 2023 | `auto-alza-suspension-da-traslado-alegar-sobre-sentencia-9` |
| 11 | Auto que suspende el procedimiento por identidad con un recurso de casación admitido | 2023 | `auto-suspende-procedimiento-identidad-recurso-casacion-11` |
| 12 | Diligencia que reanuda el procedimiento tras la suspensión | 2023 | `diligencia-reanuda-procedimiento-tras-suspension-12` |

## Contratos, escrituras y documentos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 492 | Acreditar los requisitos para que una persona jurídica litigue ante lo contencioso | 2012 | `acreditar-requisitos-persona-juridica-litigue-ante-lo-492` |

## Otros (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 449 | Asistencia jurídica gratuita: impugnación por la parte contraria de la resolución estimatoria | 2012 | `asistencia-juridica-gratuita-impugnacion-parte-contraria-449` |
| 450 | Asistencia jurídica gratuita: pedir suspender el procedimiento hasta resolver la Comisión | 2012 | `asistencia-juridica-gratuita-pedir-suspender-450` |
| 452 | Asistencia jurídica gratuita: renunciar al abogado y procurador de oficio | 2012 | `asistencia-juridica-gratuita-renunciar-abogado-452` |
| 1233 | Conflicto de competencia territorial entre órganos (negativo) | 2008 | `conflicto-competencia-territorial-entre-organos-negativo-1233` |
