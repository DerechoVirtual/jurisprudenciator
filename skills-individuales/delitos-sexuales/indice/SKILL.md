---
name: indice
description: "Índice de los 108 formularios de delitos sexuales (agresión sexual y violación (LO 10/2022 y LO 4/2023), menores de 16 años, sextorsión, grooming, pornografía infantil, acoso sexual). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Delitos sexuales: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/delitos-sexuales:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 170 | Exposición de actos sexuales a menor de 16 años: conformidad de la defensa | 2022 | `exposicion-actos-sexuales-menor-16-anos-conformidad-170` |
| 182 | Agresión sexual atenuada: conformidad de la defensa | 2022 | `agresion-sexual-atenuada-conformidad-defensa-182` |
| 185 | Agresión sexual atenuada (LO 4/2023): conformidad de la defensa | 2022 | `agresion-sexual-atenuada-lo-4-2023-conformidad-defensa-185` |
| 210 | Child grooming (acoso a menores por TIC con fines sexuales): conformidad de la defensa | 2022 | `child-grooming-acoso-menores-tic-fines-sexuales-210` |
| 223 | Acoso callejero o piropo soez (trato degradante sexual): conformidad de la defensa | 2022 | `acoso-callejero-piropo-soez-trato-degradante-sexual-223` |
| 299 | Promover por internet delitos sexuales contra menores o discapacitados: conformidad de la defensa | 2021 | `promover-internet-delitos-sexuales-contra-menores-299` |
| 567 | Corrupción de menores o personas con discapacidad por medios tecnológicos: defensa con conformidad | 2018 | `corrupcion-menores-personas-discapacidad-medios-567` |
| 571 | Utilizar menores o personas con discapacidad en pornografía por internet: defensa con conformidad | 2018 | `utilizar-menores-personas-discapacidad-pornografia-571` |
| 597 | Distribución de pornografía a menores o personas con discapacidad: defensa con conformidad | 2018 | `distribucion-pornografia-menores-personas-discapacidad-597` |
| 610 | Exhibicionismo ante menor o persona con discapacidad en redes sociales: defensa con conformidad | 2018 | `exhibicionismo-ante-menor-persona-discapacidad-redes-610` |
| 823 | Acoso sexual: defensa con conformidad | 2016 | `acoso-sexual-defensa-conformidad-823` |

## Recursos e impugnaciones (19)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 79 | Agresión sexual: casación contra la denegación de la revisión de condena | 2023 | `agresion-sexual-casacion-contra-denegacion-revision-79` |
| 143 | Violación: impugnación y oposición al recurso de casación | 2023 | `violacion-impugnacion-oposicion-recurso-casacion-143` |
| 174 | Exposición de actos sexuales a menor de 16 años: apelación contra la condena | 2022 | `exposicion-actos-sexuales-menor-16-anos-apelacion-contra-174` |
| 184 | Agresión sexual atenuada: apelación contra la condena | 2022 | `agresion-sexual-atenuada-apelacion-contra-condena-184` |
| 188 | Agresión sexual atenuada (LO 4/2023): apelación contra la condena | 2022 | `agresion-sexual-atenuada-lo-4-2023-apelacion-contra-188` |
| 191 | Violación (LO 4/2023): apelación contra la condena | 2022 | `violacion-lo-4-2023-apelacion-contra-condena-191` |
| 192 | Violación por internet (sextorsión, LO 4/2023): apelación contra la condena | 2022 | `violacion-internet-sextorsion-lo-4-2023-apelacion-contra-192` |
| 196 | Violación a menor de 16 años por sextorsión (LO 4/2023): apelación contra la condena | 2022 | `violacion-menor-16-anos-sextorsion-lo-4-2023-apelacion-196` |
| 201 | Violación: apelación contra la condena | 2022 | `violacion-apelacion-contra-condena-201` |
| 207 | Violación por internet (sextorsión): apelación contra la condena | 2022 | `violacion-internet-sextorsion-apelacion-contra-condena-207` |
| 211 | Child grooming (acoso a menores por TIC con fines sexuales): apelación contra la condena | 2022 | `child-grooming-acoso-menores-tic-fines-sexuales-211` |
| 214 | Agresión sexual a menor de 16 años por internet (sextorsión): apelación contra la condena | 2022 | `agresion-sexual-menor-16-anos-internet-sextorsion-214` |
| 225 | Acoso callejero o piropo soez (trato degradante sexual): apelación contra la condena | 2022 | `acoso-callejero-piropo-soez-trato-degradante-sexual-225` |
| 305 | Promover por internet delitos sexuales contra menores o discapacitados: apelación contra la condena | 2021 | `promover-internet-delitos-sexuales-contra-menores-305` |
| 566 | Apelación contra la condena por corrupción de menores o con discapacidad por medios tecnológicos | 2018 | `apelacion-contra-condena-corrupcion-menores-discapacidad-566` |
| 569 | Apelación contra la condena por utilizar menores o con discapacidad en pornografía por internet | 2018 | `apelacion-contra-condena-utilizar-menores-discapacidad-569` |
| 599 | Apelación contra la condena por distribuir pornografía a menores o personas con discapacidad | 2018 | `apelacion-contra-condena-distribuir-pornografia-menores-599` |
| 607 | Apelación contra la condena por exhibicionismo ante menor o persona con discapacidad | 2018 | `apelacion-contra-condena-exhibicionismo-ante-menor-607` |
| 819 | Apelación contra la condena por acoso sexual | 2016 | `apelacion-contra-condena-acoso-sexual-819` |

## Querellas y denuncias (24)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 86 | Violación a menor de 16 años (LO 4/2023): querella | 2023 | `violacion-menor-16-anos-lo-4-2023-querella-86` |
| 90 | Agresión sexual a menor de 16 años (LO 4/2023): querella | 2023 | `agresion-sexual-menor-16-anos-lo-4-2023-querella-90` |
| 93 | Agresión sexual sin acceso carnal (LO 4/2023): querella | 2023 | `agresion-sexual-sin-acceso-carnal-lo-4-2023-querella-93` |
| 172 | Exposición de actos sexuales a menor de 16 años: querella | 2022 | `exposicion-actos-sexuales-menor-16-anos-querella-172` |
| 178 | Violación bajo sumisión química: querella | 2022 | `violacion-bajo-sumision-quimica-querella-178` |
| 183 | Agresión sexual atenuada: querella | 2022 | `agresion-sexual-atenuada-querella-183` |
| 186 | Agresión sexual atenuada (LO 4/2023): querella | 2022 | `agresion-sexual-atenuada-lo-4-2023-querella-186` |
| 193 | Violación por internet (sextorsión, LO 4/2023): querella | 2022 | `violacion-internet-sextorsion-lo-4-2023-querella-193` |
| 198 | Violación a menor de 16 años por sextorsión (LO 4/2023): querella | 2022 | `violacion-menor-16-anos-sextorsion-lo-4-2023-querella-198` |
| 205 | Violación por internet (sextorsión): querella | 2022 | `violacion-internet-sextorsion-querella-205` |
| 206 | Child grooming (acoso a menores por TIC con fines sexuales): querella | 2022 | `child-grooming-acoso-menores-tic-fines-sexuales-querella-206` |
| 212 | Agresión sexual a menor de 16 años por internet (sextorsión): querella | 2022 | `agresion-sexual-menor-16-anos-internet-sextorsion-212` |
| 216 | Violación (LO 4/2023): querella | 2022 | `violacion-lo-4-2023-querella-216` |
| 218 | Violación: querella | 2022 | `violacion-querella-218` |
| 220 | Violación: denuncia | 2022 | `violacion-denuncia-220` |
| 224 | Acoso callejero o piropo soez (trato degradante sexual): querella | 2022 | `acoso-callejero-piropo-soez-trato-degradante-sexual-224` |
| 300 | Promover por internet delitos sexuales contra menores o discapacitados: querella | 2021 | `promover-internet-delitos-sexuales-contra-menores-300` |
| 564 | Corrupción de menores o personas con discapacidad por medios tecnológicos: querella | 2018 | `corrupcion-menores-personas-discapacidad-medios-564` |
| 573 | Utilizar menores o personas con discapacidad en pornografía por internet: querella | 2018 | `utilizar-menores-personas-discapacidad-pornografia-573` |
| 600 | Distribución de pornografía a menores o personas con discapacidad: querella | 2018 | `distribucion-pornografia-menores-personas-discapacidad-600` |
| 609 | Exhibicionismo ante menor o persona con discapacidad en redes sociales: querella | 2018 | `exhibicionismo-ante-menor-persona-discapacidad-redes-609` |
| 822 | Acoso sexual: querella | 2016 | `acoso-sexual-querella-822` |
| 828 | Determinación a ejercer la prostitución: querella | 2016 | `determinacion-ejercer-prostitucion-querella-828` |
| 829 | Corrupción de menores: querella | 2016 | `corrupcion-menores-querella-829` |

## Escritos de acusación (24)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 87 | Violación a menor de 16 años (LO 4/2023): calificación provisional del acusador particular | 2023 | `violacion-menor-16-anos-lo-4-2023-calificacion-87` |
| 88 | Agresión sexual a menor de 16 años, art. 181.2 CP (LO 4/2023): calificación del acusador particular | 2023 | `agresion-sexual-menor-16-anos-art-181-2-cp-lo-4-2023-88` |
| 94 | Agresión sexual sin acceso carnal (LO 4/2023): escrito de acusación | 2023 | `agresion-sexual-sin-acceso-carnal-lo-4-2023-escrito-94` |
| 171 | Exposición de actos sexuales a menor de 16 años: escrito de acusación | 2022 | `exposicion-actos-sexuales-menor-16-anos-escrito-171` |
| 177 | Violación bajo sumisión química: calificación provisional de la acusación | 2022 | `violacion-bajo-sumision-quimica-calificacion-provisional-177` |
| 180 | Agresión sexual atenuada: escrito de acusación | 2022 | `agresion-sexual-atenuada-escrito-acusacion-180` |
| 187 | Agresión sexual atenuada (LO 4/2023): escrito de acusación | 2022 | `agresion-sexual-atenuada-lo-4-2023-escrito-acusacion-187` |
| 195 | Violación a menor de 16 años por sextorsión (LO 4/2023): calificación del acusador particular | 2022 | `violacion-menor-16-anos-sextorsion-lo-4-2023-195` |
| 197 | Violación por internet (sextorsión, LO 4/2023): calificación provisional del acusador particular | 2022 | `violacion-internet-sextorsion-lo-4-2023-calificacion-197` |
| 202 | Violación con agravante de convivencia: calificación provisional de la acusación | 2022 | `violacion-agravante-convivencia-calificacion-provisional-202` |
| 204 | Violación por internet (sextorsión): calificación provisional del acusador particular | 2022 | `violacion-internet-sextorsion-calificacion-provisional-204` |
| 209 | Child grooming (acoso a menores por TIC con fines sexuales): escrito de acusación | 2022 | `child-grooming-acoso-menores-tic-fines-sexuales-escrito-209` |
| 213 | Agresión sexual a menor de 16 años por internet (sextorsión): calificación del acusador particular | 2022 | `agresion-sexual-menor-16-anos-internet-sextorsion-213` |
| 217 | Violación (LO 4/2023): calificación provisional del acusador particular | 2022 | `violacion-lo-4-2023-calificacion-provisional-acusador-217` |
| 219 | Violación: calificación provisional del acusador particular | 2022 | `violacion-calificacion-provisional-acusador-particular-219` |
| 222 | Acoso callejero o piropo soez (trato degradante sexual): escrito de acusación | 2022 | `acoso-callejero-piropo-soez-trato-degradante-sexual-222` |
| 301 | Promover por internet delitos sexuales contra menores o discapacitados: escrito de acusación | 2021 | `promover-internet-delitos-sexuales-contra-menores-301` |
| 565 | Corrupción de menores o personas con discapacidad por medios tecnológicos: acusación | 2018 | `corrupcion-menores-personas-discapacidad-medios-565` |
| 570 | Utilizar menores o personas con discapacidad en pornografía por internet: acusación | 2018 | `utilizar-menores-personas-discapacidad-pornografia-570` |
| 598 | Distribución de pornografía a menores o personas con discapacidad: acusación | 2018 | `distribucion-pornografia-menores-personas-discapacidad-598` |
| 611 | Exhibicionismo ante menor o persona con discapacidad en redes sociales: acusación | 2018 | `exhibicionismo-ante-menor-persona-discapacidad-redes-611` |
| 820 | Acoso sexual: acusación | 2016 | `acoso-sexual-acusacion-820` |
| 826 | Determinación a ejercer la prostitución: acusación | 2016 | `determinacion-ejercer-prostitucion-acusacion-826` |
| 827 | Corrupción de menores: acusación | 2016 | `corrupcion-menores-acusacion-827` |

## Escritos de defensa (26)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 85 | Violación a menor de 16 años (LO 4/2023): calificación provisional de la defensa | 2023 | `violacion-menor-16-anos-lo-4-2023-calificacion-85` |
| 89 | Agresión sexual a menor de 16 años, art. 181.2 CP (LO 4/2023): calificación de la defensa | 2023 | `agresion-sexual-menor-16-anos-art-181-2-cp-lo-4-2023-89` |
| 91 | Agresión sexual atenuada a menor de 16 años (LO 4/2023): escrito de defensa | 2023 | `agresion-sexual-atenuada-menor-16-anos-lo-4-2023-escrito-91` |
| 92 | Agresión sexual sin acceso carnal (LO 4/2023): escrito de defensa | 2023 | `agresion-sexual-sin-acceso-carnal-lo-4-2023-escrito-92` |
| 173 | Exposición de actos sexuales a menor de 16 años: escrito de defensa | 2022 | `exposicion-actos-sexuales-menor-16-anos-escrito-defensa-173` |
| 175 | Agresión sexual a menor de 16 años (LO 4/2023): calificación de la defensa alegando consentimiento | 2022 | `agresion-sexual-menor-16-anos-lo-4-2023-calificacion-175` |
| 176 | Violación bajo sumisión química: calificación provisional de la defensa | 2022 | `violacion-bajo-sumision-quimica-calificacion-provisional-176` |
| 179 | Agresión sexual a menor de 16 años: calificación de la defensa alegando consentimiento | 2022 | `agresion-sexual-menor-16-anos-calificacion-defensa-179` |
| 181 | Agresión sexual atenuada: escrito de defensa | 2022 | `agresion-sexual-atenuada-escrito-defensa-181` |
| 189 | Agresión sexual atenuada (LO 4/2023): escrito de defensa | 2022 | `agresion-sexual-atenuada-lo-4-2023-escrito-defensa-189` |
| 190 | Violación (LO 4/2023): calificación provisional de la defensa | 2022 | `violacion-lo-4-2023-calificacion-provisional-defensa-190` |
| 194 | Violación por internet (sextorsión, LO 4/2023): calificación provisional de la defensa | 2022 | `violacion-internet-sextorsion-lo-4-2023-calificacion-194` |
| 199 | Violación a menor de 16 años por sextorsión (LO 4/2023): calificación provisional de la defensa | 2022 | `violacion-menor-16-anos-sextorsion-lo-4-2023-199` |
| 200 | Violación: calificación provisional de la defensa | 2022 | `violacion-calificacion-provisional-defensa-200` |
| 203 | Violación por internet (sextorsión): calificación provisional de la defensa | 2022 | `violacion-internet-sextorsion-calificacion-provisional-203` |
| 208 | Child grooming (acoso a menores por TIC con fines sexuales): escrito de defensa | 2022 | `child-grooming-acoso-menores-tic-fines-sexuales-escrito-208` |
| 215 | Agresión sexual a menor de 16 años por internet (sextorsión): calificación provisional de la defensa | 2022 | `agresion-sexual-menor-16-anos-internet-sextorsion-215` |
| 221 | Acoso callejero o piropo soez (trato degradante sexual): escrito de defensa | 2022 | `acoso-callejero-piropo-soez-trato-degradante-sexual-221` |
| 298 | Promover por internet delitos sexuales contra menores o discapacitados: escrito de defensa | 2021 | `promover-internet-delitos-sexuales-contra-menores-298` |
| 568 | Corrupción de menores o personas con discapacidad por medios tecnológicos: defensa | 2018 | `corrupcion-menores-personas-discapacidad-medios-568` |
| 572 | Utilizar menores o personas con discapacidad en pornografía por internet: defensa | 2018 | `utilizar-menores-personas-discapacidad-pornografia-572` |
| 601 | Distribución de pornografía a menores o personas con discapacidad: defensa | 2018 | `distribucion-pornografia-menores-personas-discapacidad-601` |
| 608 | Exhibicionismo ante menor o persona con discapacidad en redes sociales: defensa | 2018 | `exhibicionismo-ante-menor-persona-discapacidad-redes-608` |
| 821 | Acoso sexual: defensa | 2016 | `acoso-sexual-defensa-821` |
| 824 | Corrupción de menores: defensa | 2016 | `corrupcion-menores-defensa-824` |
| 825 | Determinación a ejercer la prostitución: defensa | 2016 | `determinacion-ejercer-prostitucion-defensa-825` |

## Solicitudes y escritos de trámite (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 144 | Agresión sexual: pedir revisión de la pena con la casación ya interpuesta | 2023 | `agresion-sexual-pedir-revision-pena-casacion-ya-144` |
| 145 | Agresión sexual: la defensa modifica su calificación para pedir rebaja de pena | 2023 | `agresion-sexual-defensa-modifica-calificacion-pedir-145` |
| 146 | Agresión sexual: pedir en ejecutoria la revisión de la pena | 2023 | `agresion-sexual-pedir-ejecutoria-revision-pena-146` |
| 147 | Agresión sexual: pedir revisión de la pena con la apelación ya interpuesta | 2023 | `agresion-sexual-pedir-revision-pena-apelacion-ya-147` |
