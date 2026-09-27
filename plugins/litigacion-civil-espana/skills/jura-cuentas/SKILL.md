---
name: jura-cuentas
description: Jura de cuentas del procurador LEC 34 o procedimiento del abogado contra cliente LEC 35 por honorarios no satisfechos. Usar con jurar cuentas o reclamar honorarios al cliente.
---

# Jura de cuentas

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Redacción vigente de los arts. 34 y 35 LEC y del art. 1967 CC (prescripción de honorarios)** → `buscar_articulo`.
- **Derechos del procurador: arancel vigente (RD 1373/2003)** → `buscar_articulo` (por el nombre de la norma) o `buscar_boe` → `leer_boe`.
- **Cliente moroso sociedad: denominación, CIF, domicilio y si está en concurso (en ese caso el crédito se comunica a la administración concursal)** → `buscar_empresa_mercantil` + `novedades_boe` (por NIF) → `leer_boe`.
- **Criterio de las Audiencias sobre la impugnación de la cuenta por indebida o excesiva** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="AN"`, `tipo_organo="AP"`, `tipo_resolucion="AUTO"`) + `leer_sentencias` (`parrafos=3`).
- **Revisión del escrito** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Marco legal

- **LEC 34** — Jura de cuentas del PROCURADOR contra su poderdante por derechos no satisfechos
- **LEC 35** — Procedimiento del ABOGADO contra su cliente por honorarios no satisfechos
- **Plazo de prescripción**: 3 años (art. 1967 CC para honorarios de profesionales)
- **Competencia**: Tribunal donde radique el asunto principal en el que se prestaron los servicios

## Cuándo activar

- "Mi cliente no me paga", "jurar cuentas", "reclamar honorarios"
- "El procurador no ha cobrado"
- Tras impago confirmado y burofax previo de requerimiento (recomendable)

## Flujo

### 1. Identificación

- Profesional acreedor: abogado o procurador
- Cliente moroso: datos
- Asunto principal donde se prestaron los servicios
- Cuantía adeudada (liquidación detallada de actuaciones + minuta o arancel)

### 2. Acreditación

- Hoja de encargo firmada (para abogado) o poder otorgado (para procurador)
- Minuta detallada de actuaciones realizadas
- Si hubo burofax previo de requerimiento, acompañar acuse

### 3. Redacción — Jura de cuentas del Procurador (LEC 34)

```
AL TRIBUNAL DE INSTANCIA, SECCIÓN CIVIL [N], DE [PROVINCIA]
(O EN SU CASO, A LA LETRADA DE LA ADMINISTRACIÓN DE JUSTICIA)

Procedimiento principal: [...]

DON/DOÑA [Procurador], Procurador de los Tribunales y, en su día, de [poderdante moroso],
en uso del derecho que me confiere el artículo 34 de la Ley de Enjuiciamiento Civil,
comparezco y MANIFIESTO:

PRIMERO.- Que en los autos del procedimiento [...] he ejercido la procura representando
a [...] desde [fecha] hasta [fecha de cese / actualidad].

SEGUNDO.- Que [poderdante] no ha satisfecho los derechos que me corresponden por las
actuaciones procesales practicadas, los cuales ascienden a la cantidad de [...] €,
según se acredita en la minuta arancelaria que acompaño como DOCUMENTO Nº 1.

TERCERO.- Que dicha cantidad es líquida, vencida y exigible, y, formulada la presente
JURA DE CUENTAS, JURO bajo mi responsabilidad ser ciertos los derechos reclamados.

CUARTO.- Que pese a haber sido requerido [/ requerimiento previo por burofax como
DOCUMENTO Nº 2], el poderdante no ha satisfecho la deuda.

En su virtud,

SUPLICO al Tribunal/LAJ que, teniendo por presentado este escrito, lo admita, y, al
amparo del artículo 34 LEC, requiera al poderdante [...] para que, en plazo de DIEZ DÍAS,
pague la cantidad de [...] € o impugne la cuenta, bajo apercibimiento de apremio.

[Lugar y fecha]
[Firma del Procurador]
```

### 4. Redacción — Procedimiento del Abogado (LEC 35)

Estructura paralela pero con base en LEC 35:

```
AL TRIBUNAL DE INSTANCIA, SECCIÓN CIVIL [N], DE [PROVINCIA]
(O EN SU CASO, A LA LETRADA DE LA ADMINISTRACIÓN DE JUSTICIA)

DON/DOÑA [Abogado], colegiado del Ilustre Colegio de [...] nº [...], al amparo del
artículo 35 de la Ley de Enjuiciamiento Civil, comparezco y MANIFIESTO:

PRIMERO.- Que en los autos del procedimiento [...] he ejercido la dirección letrada
de [cliente moroso] [, designado de oficio / por libre elección del cliente], desde
[fecha] hasta [fecha].

SEGUNDO.- Que el cliente, pese a la hoja de encargo profesional suscrita el [fecha]
que se acompaña como DOCUMENTO Nº 1, no ha satisfecho los honorarios devengados, los
cuales ascienden a la cantidad de [...] €, según minuta detallada que se acompaña
como DOCUMENTO Nº 2, ajustada a los criterios orientadores del [Colegio].

TERCERO.- Que la deuda es líquida, vencida y exigible. JURO bajo mi responsabilidad
ser cierta la cantidad reclamada.

CUARTO.- Que mediante burofax de fecha [...] (DOCUMENTO Nº 3), se le requirió de pago,
sin atender el requerimiento.

En su virtud,

SUPLICO al Tribunal/LAJ que tenga por presentado este escrito, lo admita y, al amparo
del artículo 35 LEC, requiera al cliente [...] para que en plazo de DIEZ DÍAS pague
la cantidad de [...] € o impugne los honorarios por excesivos, bajo apercibimiento de
apremio.

[Lugar y fecha]
[Firma del Abogado]
```

### 5. Si el cliente impugna honorarios

- Por excesivos: el LAJ pasará al Colegio de Abogados para informe sobre criterios orientadores.
- El Colegio emite dictamen; el LAJ resuelve siguiéndolo salvo motivación expresa.

### 6. Si no impugna ni paga en 10 días

- Apremio: vía ejecutiva sumaria. El propio juzgado despacha ejecución por la cantidad reclamada + costas.

## Salida

- Word .docx en `matters/<slug>/escritos/jura-cuentas-v1.docx`
- Documento separado con la minuta detallada (DOC Nº 1 o 2)

## Reglas

1. **Acreditar el servicio prestado** detalladamente. Sin detalle, riesgo de impugnación.
2. **Hoja de encargo firmada es clave para abogado** (LEC 35) — sin ella, el cliente puede negar el encargo y la jura cae.
3. **Burofax previo recomendable pero no obligatorio** (acelera y evita impugnación temeraria).
4. **Plazo de prescripción: 3 años** desde último servicio (art. 1967 CC).
5. **Aranceles del procurador son regulados** (RD 1373/2003): poco margen de impugnación; **honorarios del abogado son orientativos**: margen mayor pero respaldados por criterios colegiales.
