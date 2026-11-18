---
name: conduccion-temeraria-manifiesto-desprecio-vida-ajena-365
description: "Redacta el escrito «Conducción temeraria con manifiesto desprecio por la vida ajena: escrito de acusación» (formulario 365 de seguridad vial, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Conducción temeraria con manifiesto desprecio por la vida ajena: escrito de acusación

> Formulario 0365 del plugin **Seguridad vial** · revisado el 17-11-2026. Uso interno.

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

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Lo que el usuario no sepa se queda como hueco visible.

- [ ] Órgano: SEDE del Tribunal de Instancia y Nº DE PLAZA de la Sección de Instrucción; Nº DE PROCEDIMIENTO (abreviado) y FECHA DEL AUTO que da traslado para acusar
- [ ] Partes: procurador, perjudicado (acusación particular) y **acusado** (nombre y apellidos: el escrito tiene que identificarlo, art. 781.1 LECrim)
- [ ] Hechos: FECHA y HORA; vehículo del acusado (MARCA, MODELO Y MATRÍCULA); VÍA Y PUNTO KILOMÉTRICO; descripción de la conducción (sentido contrario, velocidad, maniobras, distancia recorrida)
- [ ] Resultado: MATRÍCULA DEL VEHÍCULO DAÑADO e IMPORTE DE LOS DAÑOS; lesiones, tratamiento y secuelas según el informe forense (FECHA DEL INFORME y folio); baja laboral (fecha de baja y, si lo hay, de alta)
- [ ] Seguro: ASEGURADORA y Nº DE PÓLIZA; folio de la pieza de responsabilidad civil en el que consta el afianzamiento, o si aún no ha afianzado; TITULAR DEL VEHÍCULO si no es el acusado
- [ ] Pena que se pide dentro de la mitad superior (prisión, meses de multa y CUOTA diaria, años de privación del derecho a conducir) y, si la hay, CIRCUNSTANCIA agravante con su ordinal del art. 22 CP
- [ ] Responsabilidad civil: IMPORTE POR LESIONES, IMPORTE POR SECUELAS, IMPORTE TOTAL y AÑO DE LA VALORACIÓN del baremo; IMPORTE DE LA FIANZA si se pide requerir a la aseguradora
- [ ] Prueba: testigos (nombre y qué vieron), agentes del atestado (cuerpo y TIP), médico forense
- [ ] Pensión provisional: si está acordada, FECHA DEL AUTO DE PENSIÓN
- [ ] LUGAR y FECHA DEL ESCRITO

## Elecciones que hay que hacer

- ordinal del art. 152.1 CP según la lesión: 1.º (art. 147.1) / 2.º (art. 149) / 3.º (art. 150)
- sin circunstancias modificativas / con agravante del art. 22 CP
- baja laboral: continúa / alta
- testigos: a continuación / en escrito aparte; citados por medio de la oficina judicial / mediante exhorto

No hay elección sobre el delito que fija la pena: la del art. 381.1 CP es siempre más grave que la del art. 152.1 (ver la nota de revisión de la conclusión quinta).

## Reglas de este formulario que no puedes saltarte

- **Pena (arts. 381.1 y 382 CP).** Mitad superior del art. 381.1: prisión de tres años y seis meses a cinco años y multa de dieciocho a veinticuatro meses. La privación del derecho a conducir va en todo caso en su mitad superior, de ocho a diez años (art. 382, párrafo segundo). Compruébalo con `buscar_articulo("CP", "381")` y `("CP", "382")` antes de escribir las cifras.
- **Competencia.** Con esas penas juzga la Sección de lo Penal del Tribunal de Instancia (art. 14.3 LECrim). No pongas número de plaza del órgano de enjuiciamiento.
- **Plazo.** Diez días comunes desde el traslado (art. 780.1 LECrim), prorrogables otros diez con petición justificada (art. 781.2). Se presenta ante la Sección de Instrucción que tramita las diligencias.
- **Texto refundido del seguro de vehículos.** `buscar_articulo` no lo localiza por «RDLeg. 8/2004» (hay dos normas con ese número): usa el identificador `BOE-A-2004-18911`.
- **Importes del baremo.** Jurisprudenciator no calcula indemnizaciones. Si el usuario no trae la valoración hecha, deja los importes como hueco y dilo en el resumen.

## Párrafos opcionales (9)

Inclúyelos solo si encajan en los hechos:

- Ocupantes del vehículo del perjudicado.
- Baja laboral del perjudicado.
- Responsabilidad civil subsidiaria del titular del vehículo (art. 120.5.º CP), si no es el acusado.
- Requerimiento a la aseguradora para que afiance (solo si aún no lo ha hecho).
- Interrogatorio del acusado.
- Testifical (un párrafo por testigo; quita los que no existan).
- Pericial médico forense.
- Documental.
- Segundo otrosí sobre la pensión provisional (solo si hay auto que la acordó).

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- arts. 14.3, 240, 650, 764.3, 765, 780.1, 781.1 y 783.2 LECrim
- arts. 22, 27, 28, 47, 53, 56, 117, 120.5.º, 123, 152.1, 381.1 y 382 CP
- arts. 7.1, 7.7 y 9 RDLeg. 8/2004 (`BOE-A-2004-18911`)
- art. 20 (reglas 3.ª, 4.ª y 6.ª) de la Ley 50/1980, de Contrato de Seguro

## Flujo

1. **Paso 0**: comprueba Jurisprudenciator (arriba).
2. Lee `formulario.md` entero, con su cabecera, y la parte de `marco.md` que afecte al caso (plazos, órgano, procedimiento, procedimiento aplicable, requisitos de perseguibilidad (denuncia de la persona agraviada, querella con poder especial) y prescripción).
3. Pide los datos de la lista. Lo que el usuario no sepa se queda como hueco visible.
4. Decide las elecciones y los párrafos opcionales según los hechos. Redacta las partes que el original no traía.
5. Aplica los avisos y las notas de revisión. Comprueba con `buscar_articulo` cada norma citada y, si citas jurisprudencia, localízala con `buscar_sentencias` o `buscar_por_cita` y léela con `leer_sentencias`.
6. Indica el plazo y el cauce: desde cuándo cuenta, cuándo vence y ante qué órgano se presenta.
7. Antes de entregarlo, pasa `verificar_escrito` con las frases del escrito que citan normas o sentencias y corrige lo que señale.
8. Entrega el escrito en **Word (.docx)** con formato de escrito (usa la skill de Word disponible) y, si es corto, también en el chat.
9. Cierra con: datos pendientes, partes redactadas por ti, normas y sentencias comprobadas con Jurisprudenciator y, si algún dato sale de internet, cuál es y su enlace.
