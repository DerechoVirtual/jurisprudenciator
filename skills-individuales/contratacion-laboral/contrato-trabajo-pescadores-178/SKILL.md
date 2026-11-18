---
name: contrato-trabajo-pescadores-178
description: "Redacta el escrito «Contrato de trabajo de pescadores» (formulario 178 de contratación laboral, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Contrato de trabajo de pescadores

> Formulario 0178 del plugin **Contratación laboral** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Convenio colectivo aplicable** (salario, jornada, categorías, faltas y sanciones) → `buscar_convenio` → `leer_convenio`; si sigue vigente o está denunciado, `vigencia_convenio`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Antes de usarlo: avisos de la revisión

El planteamiento del formulario está desfasado en algo. Corrígelo antes de redactar:

- Contrato de pescadores: el RD 1659/1998 está derogado por el RD 723/2026, cuyo capítulo III (arts. 9-11) fija el contenido mínimo del contrato (art. 11: identidad, buque, viajes, salario o parte, víveres, tiempo de trabajo y descansos, cobertura sanitaria y de Seguridad Social, repatriación, terminación y preaviso no más corto para el armador, convenio con código) y la información del art. 3.2 h)-m); revisar el modelo completo.
- Supuestos de readmisión tras incapacidad permanente: desde la Ley 2/2025 (BOE-A-2025-8567, vigente 1-5-2025) la IP total, absoluta o gran invalidez ya no extingue automáticamente el contrato (art. 49.1.n ET: ajustes razonables o cambio de puesto, 10 días para que la persona manifieste su voluntad y 3 meses para la empresa); revisar la redacción de estos supuestos.

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] NOMBRE Y APELLIDOS (3 veces)
- [ ] C.P. (2 veces)
- [ ] IMPORTE
- [ ] DESCRIBIR
- [ ] Nº (3 veces)
- [ ] ÓRGANO O PERSONA (2 veces)
- [ ] FECHA (3 veces)
- [ ] NÚMERO (4 veces)
- [ ] LOCALIDAD (2 veces)
- [ ] DNI/NIE
- [ ] LUGAR
- [ ] DÍA
- [ ] MES
- [ ] AÑO
- [ ] ÓRGANO
- [ ] Otros 1232 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…CONTRATO DE TRABAJO DE LOS PESCADORES:»; «…TOS DE LA EMPRESA / ARMADOR CIF/NIF/NIE:»; «…D./DÑA. [NOMBRE Y APELLIDOS] NIF/NIE:»; «…PTO NOMBRE O RAZÓN SOCIAL DE LA EMPRESA:»; «…DOMICILIO SOCIAL:»; «…DOMICILIO SOCIAL: [COMPLETAR] MUNICIPIO:»; «…CÓDIGO POSTAL [C.P.] PAÍS:»; «…DATOS DE LA CUENTA DE COTIZACIÓN RÉGIMEN»; «…CÓDIGO CUENTA DE COTIZACIÓN:»; «…ACTIVIDAD ECONÓMICA:»; «…OS BUQUE(S) PESQUERO(S) NOMBRE DEL BUQUE»; «…NÚMERO DE REGISTRO (NIB):»; …

## Elecciones que hay que hacer

- SÍ / NO

## Correcciones de la revisión (1)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículo 10.3 del Real Decreto 723/2026
- artículo 10.g) del Real Decreto 1659/1998
- artículo 16 del Estatuto de los Trabajadores
- artículo 15 del Real Decreto-ley 1/2023
- artículo 21 del Real Decreto-ley 1/2023
- artículo 2.1 de la Ley 44/2007
- artículo 20 del Real Decreto-ley 1/2023
- artículo 23 de la Ley Orgánica 1/2004
- artículo 16 del Real Decreto-ley 1/2023
- artículo 37 de la Ley Orgánica 10/2022
- artículo 47 del Real Decreto-ley 6/2022
- artículo 34 de la Ley 29/2011
- artículo 22 del Real Decreto-ley 1/2023
- artículo 24 del Real Decreto-ley 1/2023
- artículo 215 del Real Decreto Legislativo 8/2015
- artículo 2.2 de la Ley 43/2006
- Real Decreto 618/2020
- Ley Orgánica 3/2018
- Ley 47/2015
- Real Decreto 818/2021
- Real Decreto 368/2021
- Real Decreto 1451/1983

## Flujo

1. **Paso 0**: comprueba Jurisprudenciator (arriba).
2. Lee `formulario.md` entero, con su cabecera, y la parte de `marco.md` que afecte al caso (plazos, órgano, procedimiento, conciliación o mediación previa, reclamación previa o vía administrativa, según el caso).
3. Pide los datos de la lista. Lo que el usuario no sepa se queda como hueco visible.
4. Decide las elecciones y los párrafos opcionales según los hechos. Redacta las partes que el original no traía.
5. Aplica los avisos y las notas de revisión. Comprueba con `buscar_articulo` cada norma citada y, si citas jurisprudencia, localízala con `buscar_sentencias` o `buscar_por_cita` y léela con `leer_sentencias`.
6. Indica el plazo y el cauce: desde cuándo cuenta, cuándo vence y ante qué órgano se presenta.
7. Antes de entregarlo, pasa `verificar_escrito` con las frases del escrito que citan normas o sentencias y corrige lo que señale.
8. Entrega el escrito en **Word (.docx)** con formato de escrito (usa la skill de Word disponible) y, si es corto, también en el chat.
9. Cierra con: datos pendientes, partes redactadas por ti, normas y sentencias comprobadas con Jurisprudenciator y, si algún dato sale de internet, cuál es y su enlace.
