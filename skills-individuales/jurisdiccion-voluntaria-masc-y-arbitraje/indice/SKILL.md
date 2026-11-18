---
name: indice
description: "Índice de los 91 formularios de jurisdicción voluntaria, masc, mediación y arbitraje (MASC, conciliación, mediación, arbitraje, expedientes). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Jurisdicción voluntaria, MASC, mediación y arbitraje: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/jurisdiccion-voluntaria-masc-y-arbitraje:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 707 | Demanda de nulidad de lo convenido en la conciliación | 2015 | `demanda-nulidad-lo-convenido-conciliacion-707` |
| 1471 | Demanda de anulación de laudo de arbitraje de consumo | 2014 | `demanda-anulacion-laudo-arbitraje-consumo-1471` |
| 1472 | Demanda de revisión de laudo firme por maquinación fraudulenta | 2014 | `demanda-revision-laudo-firme-maquinacion-fraudulenta-1472` |
| 1473 | Demanda de remoción de árbitro y nombramiento de sustituto | 2014 | `demanda-remocion-arbitro-nombramiento-sustituto-1473` |
| 1474 | Formalización judicial del arbitraje y designación de árbitros | 2014 | `formalizacion-judicial-arbitraje-designacion-arbitros-1474` |
| 1519 | Impugnar un acuerdo de mediación | 2014 | `impugnar-acuerdo-mediacion-1519` |

## Contestaciones, oposiciones y alegaciones (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 650 | Oposición al expediente de fijación del plazo de cumplimiento de la obligación | 2015 | `oposicion-expediente-fijacion-plazo-cumplimiento-650` |
| 670 | Oposición en jurisdicción voluntaria con paso a proceso contencioso: modelo general | 2015 | `oposicion-jurisdiccion-voluntaria-paso-proceso-670` |
| 691 | Oposición del tenedor del título al expediente | 2015 | `oposicion-tenedor-titulo-expediente-691` |
| 722 | Alegaciones del interesado a la notificación de la consignación | 2015 | `alegaciones-interesado-notificacion-consignacion-722` |
| 866 | Oposición escrita a la solicitud de conciliación | 2013 | `oposicion-escrita-solicitud-conciliacion-866` |
| 1480 | Contestación al requerimiento de arbitraje: aceptación total | 2014 | `contestacion-requerimiento-arbitraje-aceptacion-total-1480` |
| 1482 | Contestación al requerimiento de arbitraje: oposición | 2014 | `contestacion-requerimiento-arbitraje-oposicion-1482` |
| 1483 | Contestación al requerimiento de arbitraje: aceptación parcial | 2014 | `contestacion-requerimiento-arbitraje-aceptacion-parcial-1483` |
| 1485 | Contestación a demanda de anulación de laudo (modelo genérico) | 2014 | `contestacion-demanda-anulacion-laudo-modelo-generico-1485` |
| 1486 | Contestación a demanda de anulación de laudo: validez del convenio arbitral | 2014 | `contestacion-demanda-anulacion-laudo-validez-convenio-1486` |
| 1487 | Contestación a demanda de anulación de laudo: no es contrario al orden público | 2014 | `contestacion-demanda-anulacion-laudo-no-es-contrario-1487` |

## Solicitudes y expedientes (34)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 9 | Conciliación ante el Letrado de la Administración de Justicia: solicitud (MASC) | 2025 | `conciliacion-ante-letrado-administracion-justicia-9` |
| 10 | Solicitud de mediación previa a la demanda (MASC) | 2025 | `solicitud-mediacion-previa-demanda-masc-10` |
| 15 | Expediente notarial de conciliación: solicitud (MASC) | 2025 | `expediente-notarial-conciliacion-solicitud-masc-15` |
| 16 | Conciliación ante el juez o la jueza de paz: solicitud (MASC) | 2025 | `conciliacion-ante-juez-jueza-paz-solicitud-masc-16` |
| 138 | Jurisdicción voluntaria para extinguir un poder preventivo | 2021 | `jurisdiccion-voluntaria-extinguir-poder-preventivo-138` |
| 310 | Jurisdicción voluntaria de medidas de protección del art. 158 CC | 2020 | `jurisdiccion-voluntaria-medidas-proteccion-art-158-cc-310` |
| 607 | Reconocimiento de laudo arbitral extranjero | 2016 | `reconocimiento-laudo-arbitral-extranjero-607` |
| 630 | Expediente notarial por robo de título valor | 2015 | `expediente-notarial-robo-titulo-valor-630` |
| 632 | Expediente notarial de conciliación en materia de obligaciones | 2015 | `expediente-notarial-conciliacion-materia-obligaciones-632` |
| 645 | Disolución judicial de sociedad de capital pedida por un socio | 2015 | `disolucion-judicial-sociedad-capital-pedida-socio-645` |
| 646 | Exhibición de libros contables del socio frente al administrador (jurisdicción voluntaria) | 2015 | `exhibicion-libros-contables-socio-frente-administrador-646` |
| 647 | Separación de un liquidador de sociedad de capital | 2015 | `separacion-liquidador-sociedad-capital-647` |
| 657 | Suspensión del expediente de jurisdicción voluntaria por cuestión prejudicial civil | 2015 | `suspension-expediente-jurisdiccion-voluntaria-cuestion-657` |
| 660 | Expediente notarial de consignación | 2015 | `expediente-notarial-consignacion-660` |
| 663 | Conciliación ante el Juez de Paz | 2015 | `conciliacion-ante-juez-paz-663` |
| 675 | Inicio de expediente de jurisdicción voluntaria | 2015 | `inicio-expediente-jurisdiccion-voluntaria-675` |
| 695 | Inicio de expediente de valores mobiliarios | 2015 | `inicio-expediente-valores-mobiliarios-695` |
| 705 | Testimonio del acta que pone fin a la conciliación | 2015 | `testimonio-acta-pone-fin-conciliacion-705` |
| 729 | Consignación ante órgano judicial en jurisdicción voluntaria | 2015 | `consignacion-ante-organo-judicial-jurisdiccion-729` |
| 749 | Declaración de fallecimiento | 2015 | `declaracion-fallecimiento-749` |
| 751 | Declaración de ausencia | 2015 | `declaracion-ausencia-751` |
| 766 | Archivo de los expedientes de jurisdicción voluntaria posteriores con idéntico objeto | 2015 | `archivo-expedientes-jurisdiccion-voluntaria-posteriores-766` |
| 768 | Reconocimiento en España de actos de jurisdicción voluntaria extranjeros | 2015 | `reconocimiento-espana-actos-jurisdiccion-voluntaria-768` |
| 769 | Anotación registral de resolución extranjera de jurisdicción voluntaria | 2015 | `anotacion-registral-resolucion-extranjera-jurisdiccion-769` |
| 772 | Suspensión del expediente de jurisdicción voluntaria por proceso contencioso pendiente | 2015 | `suspension-expediente-jurisdiccion-voluntaria-proceso-772` |
| 778 | Habilitación para comparecer en juicio por ausencia: inicio del expediente | 2015 | `habilitacion-comparecer-juicio-ausencia-inicio-778` |
| 893 | Conciliación encabezada por el propio conciliante | 2013 | `conciliacion-encabezada-propio-conciliante-893` |
| 900 | Solicitud conjunta de mediación | 2013 | `solicitud-conjunta-mediacion-900` |
| 934 | Conciliación encabezada por procurador | 2013 | `conciliacion-encabezada-procurador-934` |
| 1020 | Reconstrucción de actuaciones: inicio del expediente | 2013 | `reconstruccion-actuaciones-inicio-expediente-1020` |
| 1337 | Suspensión del procedimiento para arbitraje o mediación | 2013 | `suspension-procedimiento-arbitraje-mediacion-1337` |
| 1348 | Levantamiento de la suspensión acordada para arbitraje o mediación | 2013 | `levantamiento-suspension-acordada-arbitraje-mediacion-1348` |
| 1475 | Subsanada la solicitud de arbitraje de consumo: continuación del procedimiento | 2014 | `subsanada-solicitud-arbitraje-consumo-continuacion-1475` |
| 1508 | Solicitud de mediación de una parte en cumplimiento de pacto de sometimiento | 2014 | `solicitud-mediacion-parte-cumplimiento-pacto-1508` |

## Escritos de trámite (14)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 649 | Devolución de lo consignado pedida por el promotor | 2015 | `devolucion-lo-consignado-pedida-promotor-649` |
| 661 | Oposición del acreedor a la consignación | 2015 | `oposicion-acreedor-consignacion-661` |
| 669 | Oposición de un interesado en jurisdicción voluntaria | 2015 | `oposicion-interesado-jurisdiccion-voluntaria-669` |
| 693 | Denuncia a la sociedad rectora por robo, hurto o extravío de valores cotizados | 2015 | `denuncia-sociedad-rectora-robo-hurto-extravio-valores-693` |
| 699 | Notificación a la sociedad rectora de la incoación del expediente | 2015 | `notificacion-sociedad-rectora-incoacion-expediente-699` |
| 702 | Mantenimiento de la consignación pedido por el consignatario | 2015 | `mantenimiento-consignacion-pedido-consignatario-702` |
| 704 | Devolución de lo consignado pedida por el consignatario | 2015 | `devolucion-lo-consignado-pedida-consignatario-704` |
| 712 | Cancelación de la consignación declarada bien hecha | 2015 | `cancelacion-consignacion-declarada-bien-hecha-712` |
| 734 | Cancelación de la obligación al retirar los interesados la cosa consignada | 2015 | `cancelacion-obligacion-retirar-interesados-cosa-734` |
| 747 | Aviso del declarado fallecido de que ha reaparecido | 2015 | `aviso-declarado-fallecido-ha-reaparecido-747` |
| 879 | Declinatoria basada en convenio arbitral | 2013 | `declinatoria-basada-convenio-arbitral-879` |
| 1209 | Otrosí: consignación con la demanda | 2013 | `otrosi-consignacion-demanda-1209` |
| 1349 | Declinatoria por mediación pactada | 2013 | `declinatoria-mediacion-pactada-1349` |
| 1470 | Contestación a demanda arbitral con reconvención (arbitraje de equidad) | 2014 | `contestacion-demanda-arbitral-reconvencion-arbitraje-1470` |

## Actos y resoluciones de la Administración o del órgano judicial (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 538 | Acta de notoriedad de ausencia no declarada (Galicia) | 2016 | `acta-notoriedad-ausencia-no-declarada-galicia-538` |
| 648 | Notificación a la sociedad de la solicitud previa de disolución judicial | 2015 | `notificacion-sociedad-solicitud-previa-disolucion-648` |
| 901 | Acta de la sesión informativa en la mediación | 2013 | `acta-sesion-informativa-mediacion-901` |
| 1504 | Acuerdo de confidencialidad en la mediación | 2014 | `acuerdo-confidencialidad-mediacion-1504` |
| 1505 | Acta de mediación intentada sin efecto por inasistencia de una parte a la sesión informativa | 2014 | `acta-mediacion-intentada-sin-efecto-inasistencia-parte-1505` |
| 1518 | Acta de fin de mediación con acuerdo | 2014 | `acta-fin-mediacion-acuerdo-1518` |
| 1520 | Acta de renuncia del mediador | 2014 | `acta-renuncia-mediador-1520` |

## Contratos, escrituras y documentos (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 613 | Modelo normalizado de solicitud de jurisdicción voluntaria (art. 14.3 LJV) | 2016 | `modelo-normalizado-solicitud-jurisdiccion-voluntaria-art-613` |
| 614 | Modelo normalizado de solicitud de conciliación (art. 141.1 LJV) |  | `modelo-normalizado-solicitud-conciliacion-art-141-1-ljv-614` |
| 899 | Pacto para someter las controversias a mediación | 2013 | `pacto-someter-controversias-mediacion-899` |
| 1501 | Acta constitutiva de mediación intraprocesal | 2014 | `acta-constitutiva-mediacion-intraprocesal-1501` |
| 1502 | Acta final de mediación sin acuerdo | 2014 | `acta-final-mediacion-sin-acuerdo-1502` |
| 1503 | Acta constitutiva de mediación | 2014 | `acta-constitutiva-mediacion-1503` |

## Comunicaciones, requerimientos y reclamaciones (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 14 | Reclamación extrajudicial para negociar antes de demandar (MASC) | 2025 | `reclamacion-extrajudicial-negociar-antes-demandar-masc-14` |
| 1476 | Requerimiento al demandado para iniciar el arbitraje con propuesta de árbitro | 2014 | `requerimiento-demandado-iniciar-arbitraje-propuesta-1476` |
| 1506 | Convocatoria de las partes a la sesión informativa de mediación | 2014 | `convocatoria-partes-sesion-informativa-mediacion-1506` |
| 1517 | Comunicación al mediador de la voluntad de terminar la mediación | 2014 | `comunicacion-mediador-voluntad-terminar-mediacion-1517` |

## Otros (9)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 6 | Declaración responsable en el proceso civil (MASC) | 2025 | `declaracion-responsable-proceso-civil-masc-6` |
| 8 | Oferta vinculante confidencial como MASC | 2025 | `oferta-vinculante-confidencial-como-masc-8` |
| 11 | Cumplimiento del requisito de procedibilidad en litigios de consumo (MASC) | 2025 | `cumplimiento-requisito-procedibilidad-litigios-consumo-11` |
| 12 | Cumplimiento del requisito de procedibilidad: supuesto general (MASC) | 2025 | `cumplimiento-requisito-procedibilidad-supuesto-general-12` |
| 13 | Supuesto excluido del requisito de procedibilidad en demandas civiles (MASC) | 2025 | `supuesto-excluido-requisito-procedibilidad-demandas-13` |
| 258 | Laudo final en arbitraje institucional de derecho | 2020 | `laudo-final-arbitraje-institucional-derecho-258` |
| 697 | Reducción de capital o amortización de participaciones o acciones (SL y SA) | 2015 | `reduccion-capital-amortizacion-participaciones-acciones-697` |
| 802 | Disolución judicial de sociedad limitada instada por los administradores | 2015 | `disolucion-judicial-sociedad-limitada-instada-802` |
| 1224 | Consignación de cuotas previa a la impugnación | 2013 | `consignacion-cuotas-previa-impugnacion-1224` |
