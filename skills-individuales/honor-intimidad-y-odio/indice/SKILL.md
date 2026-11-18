---
name: indice
description: "Índice de los 63 formularios de honor, intimidad y delitos de odio (calumnias, injurias, incitación al odio, difusión de imágenes íntimas, revelación de secretos, ciberbullying, libertad religiosa). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Honor, intimidad y delitos de odio: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/honor-intimidad-y-odio:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 226 | Uso de la imagen ajena sin consentimiento en medios de difusión pública: conformidad de la defensa | 2022 | `uso-imagen-ajena-sin-consentimiento-medios-difusion-226` |
| 255 | Acoso para obstaculizar el aborto: conformidad de la defensa | 2022 | `acoso-obstaculizar-aborto-conformidad-defensa-255` |
| 259 | Asociación ilícita: conformidad de la defensa | 2022 | `asociacion-ilicita-conformidad-defensa-259` |
| 517 | Revenge porn: pedir comparecencia para la conformidad | 2019 | `revenge-porn-pedir-comparecencia-conformidad-517` |
| 529 | Humillación a víctimas del terrorismo por internet: defensa con conformidad | 2018 | `humillacion-victimas-terrorismo-internet-defensa-529` |
| 642 | Libertad de conciencia y sentimientos religiosos: defensa con conformidad | 2017 | `libertad-conciencia-sentimientos-religiosos-defensa-642` |
| 648 | Calumnia en redes sociales: defensa con conformidad | 2017 | `calumnia-redes-sociales-defensa-conformidad-648` |
| 649 | Injurias graves con publicidad en redes sociales: defensa con conformidad | 2017 | `injurias-graves-publicidad-redes-sociales-defensa-649` |
| 655 | Incitación al odio en redes sociales: defensa con conformidad | 2017 | `incitacion-odio-redes-sociales-defensa-conformidad-655` |
| 663 | Denegación discriminatoria de una prestación empresarial o profesional: defensa con conformidad | 2017 | `denegacion-discriminatoria-prestacion-empresarial-663` |
| 673 | Ciberbullying: conformidad del letrado del menor con la acusación del fiscal | 2017 | `ciberbullying-conformidad-letrado-menor-acusacion-fiscal-673` |

## Recursos e impugnaciones (13)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 228 | Uso de la imagen ajena sin consentimiento en medios de difusión pública: apelación contra la condena | 2022 | `uso-imagen-ajena-sin-consentimiento-medios-difusion-228` |
| 254 | Acoso para obstaculizar el aborto: apelación contra la condena | 2022 | `acoso-obstaculizar-aborto-apelacion-contra-condena-254` |
| 260 | Asociación ilícita: apelación contra la condena | 2022 | `asociacion-ilicita-apelacion-contra-condena-260` |
| 514 | Apelación contra la condena por revenge porn | 2019 | `apelacion-contra-condena-revenge-porn-514` |
| 530 | Apelación contra la condena por humillación a víctimas del terrorismo por internet | 2018 | `apelacion-contra-condena-humillacion-victimas-terrorismo-530` |
| 639 | Apelación contra la condena por delito contra la libertad de conciencia y sentimientos religiosos | 2017 | `apelacion-contra-condena-delito-contra-libertad-639` |
| 647 | Apelación contra la condena por calumnia en redes sociales | 2017 | `apelacion-contra-condena-calumnia-redes-sociales-647` |
| 650 | Apelación contra la condena por injurias graves en redes sociales | 2017 | `apelacion-contra-condena-injurias-graves-redes-sociales-650` |
| 658 | Apelación contra la condena por incitación al odio en redes sociales | 2017 | `apelacion-contra-condena-incitacion-odio-redes-sociales-658` |
| 659 | Apelación contra la condena por denegación discriminatoria de prestación empresarial o profesional | 2017 | `apelacion-contra-condena-denegacion-discriminatoria-659` |
| 669 | Apelación contra la condena por ciberbullying | 2017 | `apelacion-contra-condena-ciberbullying-669` |
| 717 | Apelación contra la condena por sexting (difusión o redifusión inconsentida de imágenes) | 2017 | `apelacion-contra-condena-sexting-difusion-redifusion-717` |
| 718 | Apelación contra la absolución por sexting (difusión inconsentida de imágenes por internet) | 2017 | `apelacion-contra-absolucion-sexting-difusion-718` |

## Querellas y denuncias (13)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 237 | Uso de la imagen ajena sin consentimiento en medios de difusión pública: querella | 2022 | `uso-imagen-ajena-sin-consentimiento-medios-difusion-237` |
| 256 | Acoso para obstaculizar el aborto: querella | 2022 | `acoso-obstaculizar-aborto-querella-256` |
| 257 | Asociación ilícita: querella | 2022 | `asociacion-ilicita-querella-257` |
| 262 | Descubrimiento y revelación de secretos: querella | 2022 | `descubrimiento-revelacion-secretos-querella-262` |
| 515 | Revenge porn: denuncia ante la Fiscalía de Menores | 2019 | `revenge-porn-denuncia-ante-fiscalia-menores-515` |
| 528 | Humillación a víctimas del terrorismo por internet (ciberterrorismo): querella | 2018 | `humillacion-victimas-terrorismo-internet-ciberterrorismo-528` |
| 641 | Libertad de conciencia y sentimientos religiosos: querella | 2017 | `libertad-conciencia-sentimientos-religiosos-querella-641` |
| 646 | Calumnia en redes sociales: querella | 2017 | `calumnia-redes-sociales-querella-646` |
| 652 | Injurias graves en redes sociales: querella | 2017 | `injurias-graves-redes-sociales-querella-652` |
| 654 | Incitación al odio con publicidad en redes sociales: querella | 2017 | `incitacion-odio-publicidad-redes-sociales-querella-654` |
| 661 | Denegación discriminatoria de una prestación empresarial o profesional: querella | 2017 | `denegacion-discriminatoria-prestacion-empresarial-661` |
| 670 | Ciberbullying: denuncia ante la Fiscalía de Menores | 2017 | `ciberbullying-denuncia-ante-fiscalia-menores-670` |
| 721 | Sexting (difusión o redifusión inconsentida de imágenes por internet): querella | 2017 | `sexting-difusion-redifusion-inconsentida-imagenes-721` |

## Escritos de acusación (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 227 | Uso de la imagen ajena sin consentimiento en medios de difusión pública: escrito de acusación | 2022 | `uso-imagen-ajena-sin-consentimiento-medios-difusion-227` |
| 252 | Acoso para obstaculizar el aborto: escrito de acusación | 2022 | `acoso-obstaculizar-aborto-escrito-acusacion-252` |
| 261 | Asociación ilícita: escrito de acusación | 2022 | `asociacion-ilicita-escrito-acusacion-261` |
| 516 | Revenge porn: alegaciones de la acusación | 2019 | `revenge-porn-alegaciones-acusacion-516` |
| 527 | Humillación a víctimas del terrorismo por internet (ciberterrorismo): acusación | 2018 | `humillacion-victimas-terrorismo-internet-ciberterrorismo-527` |
| 640 | Libertad de conciencia y sentimientos religiosos: acusación | 2017 | `libertad-conciencia-sentimientos-religiosos-acusacion-640` |
| 645 | Calumnia en redes sociales: acusación | 2017 | `calumnia-redes-sociales-acusacion-645` |
| 653 | Injurias graves en redes sociales: acusación | 2017 | `injurias-graves-redes-sociales-acusacion-653` |
| 656 | Incitación al odio con publicidad en redes sociales: acusación | 2017 | `incitacion-odio-publicidad-redes-sociales-acusacion-656` |
| 662 | Denegación discriminatoria de una prestación empresarial o profesional: acusación | 2017 | `denegacion-discriminatoria-prestacion-empresarial-662` |
| 671 | Ciberbullying: alegaciones de la acusación particular | 2017 | `ciberbullying-alegaciones-acusacion-particular-671` |
| 675 | Sexting (difusión o redifusión inconsentida de imágenes por internet): acusación | 2017 | `sexting-difusion-redifusion-inconsentida-imagenes-675` |

## Escritos de defensa (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 229 | Uso de la imagen ajena sin consentimiento en medios de difusión pública: escrito de defensa | 2022 | `uso-imagen-ajena-sin-consentimiento-medios-difusion-229` |
| 253 | Acoso para obstaculizar el aborto: escrito de defensa | 2022 | `acoso-obstaculizar-aborto-escrito-defensa-253` |
| 258 | Asociación ilícita: escrito de defensa | 2022 | `asociacion-ilicita-escrito-defensa-258` |
| 513 | Revenge porn: alegaciones del letrado del menor acusado | 2019 | `revenge-porn-alegaciones-letrado-menor-acusado-513` |
| 526 | Humillación a víctimas del terrorismo por internet: defensa | 2018 | `humillacion-victimas-terrorismo-internet-defensa-526` |
| 643 | Libertad de conciencia y sentimientos religiosos: defensa | 2017 | `libertad-conciencia-sentimientos-religiosos-defensa-643` |
| 644 | Calumnia en redes sociales: defensa | 2017 | `calumnia-redes-sociales-defensa-644` |
| 651 | Injurias graves en redes sociales: defensa | 2017 | `injurias-graves-redes-sociales-defensa-651` |
| 657 | Incitación al odio en redes sociales: defensa | 2017 | `incitacion-odio-redes-sociales-defensa-657` |
| 660 | Denegación discriminatoria de una prestación empresarial o profesional: defensa | 2017 | `denegacion-discriminatoria-prestacion-empresarial-660` |
| 672 | Ciberbullying: alegaciones de la defensa del menor | 2017 | `ciberbullying-alegaciones-defensa-menor-672` |
| 674 | Sexting (difusión o redifusión inconsentida de imágenes por internet): defensa | 2017 | `sexting-difusion-redifusion-inconsentida-imagenes-674` |

## Medidas cautelares y protección (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 722 | Sexting: la víctima pide la retirada provisional de contenidos de internet como medida cautelar | 2017 | `sexting-victima-pide-retirada-provisional-contenidos-722` |

## Solicitudes y escritos de trámite (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 98 | Calumnias: el investigado pide probar la verdad de la imputación (exceptio veritatis) | 2023 | `calumnias-investigado-pide-probar-verdad-imputacion-98` |
