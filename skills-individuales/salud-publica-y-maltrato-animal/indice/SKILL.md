---
name: indice
description: "Índice de los 21 formularios de salud pública y maltrato animal (tráfico de drogas, petaqueo, adulteración de alimentos, maltrato animal). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Salud pública y maltrato animal: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/salud-publica-y-maltrato-animal:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 7 | Defraudación de fluido eléctrico en concurso real con tráfico de drogas: conformidad de la defensa | 2026 | `defraudacion-fluido-electrico-concurso-real-trafico-7` |
| 13 | Petaqueo (combustible líquido a narcolancha): conformidad de la defensa | 2026 | `petaqueo-combustible-liquido-narcolancha-conformidad-13` |
| 109 | Lesiones a animales difundidas en redes sociales: conformidad de la defensa | 2023 | `lesiones-animales-difundidas-redes-sociales-conformidad-109` |
| 788 | Adulteración de alimentos o bebidas (salud pública): defensa con conformidad en el abreviado | 2016 | `adulteracion-alimentos-bebidas-salud-publica-defensa-788` |
| 791 | Narcotráfico (salud pública): defensa con conformidad en el abreviado | 2016 | `narcotrafico-salud-publica-defensa-conformidad-abreviado-791` |
| 792 | Narcotráfico: defensa con conformidad en juicio rápido | 2016 | `narcotrafico-defensa-conformidad-juicio-rapido-792` |

## Recursos e impugnaciones (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 8 | Defraudación de fluido eléctrico en concurso real con tráfico de drogas: apelación contra la condena | 2026 | `defraudacion-fluido-electrico-concurso-real-trafico-8` |
| 12 | Petaqueo (combustible líquido a narcolancha): apelación contra la condena | 2026 | `petaqueo-combustible-liquido-narcolancha-apelacion-12` |
| 110 | Lesiones a animales difundidas en redes sociales: apelación contra la condena | 2023 | `lesiones-animales-difundidas-redes-sociales-apelacion-110` |
| 790 | Apelación contra la condena por adulteración de alimentos o bebidas (salud pública) | 2016 | `apelacion-contra-condena-adulteracion-alimentos-bebidas-790` |
| 793 | Apelación contra la condena por narcotráfico (salud pública) | 2016 | `apelacion-contra-condena-narcotrafico-salud-publica-793` |

## Querellas y denuncias (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 6 | Defraudación de fluido eléctrico para cultivo de drogas: querella | 2026 | `defraudacion-fluido-electrico-cultivo-drogas-querella-6` |
| 106 | Lesiones a animales difundidas en redes sociales: querella | 2023 | `lesiones-animales-difundidas-redes-sociales-querella-106` |
| 789 | Adulteración de alimentos o bebidas (salud pública): querella | 2016 | `adulteracion-alimentos-bebidas-salud-publica-querella-789` |

## Escritos de acusación (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 10 | Defraudación de fluido eléctrico en concurso con tráfico de drogas: escrito de acusación | 2026 | `defraudacion-fluido-electrico-concurso-trafico-drogas-10` |
| 108 | Lesiones a animales difundidas en redes sociales: escrito de acusación | 2023 | `lesiones-animales-difundidas-redes-sociales-escrito-108` |
| 786 | Adulteración de alimentos o bebidas (salud pública): acusación | 2016 | `adulteracion-alimentos-bebidas-salud-publica-acusacion-786` |

## Escritos de defensa (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 9 | Defraudación de fluido eléctrico en concurso real con tráfico de drogas: escrito de defensa | 2026 | `defraudacion-fluido-electrico-concurso-real-trafico-9` |
| 11 | Petaqueo (combustible líquido a narcolancha): escrito de defensa | 2026 | `petaqueo-combustible-liquido-narcolancha-escrito-defensa-11` |
| 107 | Lesiones a animales difundidas en redes sociales: escrito de defensa | 2023 | `lesiones-animales-difundidas-redes-sociales-escrito-107` |
| 787 | Adulteración de alimentos o bebidas (salud pública): defensa | 2016 | `adulteracion-alimentos-bebidas-salud-publica-defensa-787` |
