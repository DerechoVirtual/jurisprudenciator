---
name: redactor-escrito-seccion
description: Redactar una seccion concreta de un escrito judicial como hechos, fundamento de derecho sobre un punto, suplico o antecedentes procesales. Usar con redacta los hechos o saca el suplico.
---

# Redactor de sección concreta

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **FUNDAMENTO sobre un punto: cita literal del precepto** → `buscar_articulo` (`ley`, `articulo`).
- **Cita jurisprudencial con órgano, fecha, número, ECLI, ponente y párrafo** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; `base="TC"` o `base="TJUE"` si procede) + `leer_sentencias` (`parrafos=3`, `terminos`), y `buscar_por_cita` para cada ECLI o ROJ.
- **HECHOS y encabezamiento con datos de la empresa y del convenio** → `buscar_empresa_mercantil` (denominación, CIF, domicilio social) y `leer_convenio` (categoría, salario, artículo aplicable).
- **Sección de un escrito que ninguna skill del plugin cubre** (p. ej. impugnación de sanción, vacaciones o modificación sustancial individual) → `escritos_disponibles` + `guia_escrito`.
- **Sección terminada** → `verificar_escrito` con el texto de la sección.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Redacta solo los HECHOS de la demanda"
- "Redacta el FUNDAMENTO DE DERECHO sobre [punto]"
- "Saca el SUPLICO"
- "Redacta los ANTECEDENTES PROCESALES de la apelación"
- Cuando necesitas iterar sobre una sección sin reescribir todo

## Secciones soportadas

| Sección | Aplicable a |
|---|---|
| Encabezamiento | Toda demanda / papeleta / recurso |
| Antecedentes de hecho / Hechos | Demanda, papeleta, recurso |
| Antecedentes procesales | Recurso de suplicación, RCUD |
| Fundamentos de derecho — jurisdicción y competencia | Demanda (arts. 1-2, 6, 10 LRJS) |
| Fundamentos de derecho — procedimiento/modalidad procesal | Demanda (ordinario o modalidad de los arts. 102 ss. LRJS) |
| Fundamentos de derecho — legitimación y postulación | Demanda (arts. 16-21 LRJS) |
| Fundamentos de derecho — conciliación previa / reclamación previa | Demanda (arts. 63-73 LRJS) |
| Fundamentos de derecho — fondo | Cualquier escrito |
| Fundamentos de derecho — costas | Solo recursos (art. 235 LRJS) |
| Suplico / Petitum | Toda demanda / recurso |
| Otrosíes (proposición de prueba, citación de la demandada con apercibimiento art. 91.2 LRJS) | Donde proceda |
| Motivos del recurso (art. 193 LRJS / relación precisa de contradicción art. 224 LRJS) | Suplicación / RCUD |
| Cuestionario de interrogatorio | Guion para el acto del juicio |

## Flujo

### 1. Identificar sección + asunto

- Sección a redactar
- Asunto (slug)
- Versión del escrito (v1, v2 si itera)
- Objetivo concreto de la sección (qué tiene que decir)

### 2. Cargar contexto

- `matters/<slug>/matter.md` (tesis)
- `matters/<slug>/cronologia.md` (eventos para HECHOS)
- `matters/<slug>/cuadro-elementos.md` (cobertura probatoria)
- Documentos del asunto

### 3. Aplicar plantilla por tipo de sección

#### HECHOS

```
HECHOS

Primero.- [Hecho 1 narrado en 2-3 frases, con cita documental al final]
   Se acompaña como DOCUMENTO Nº [N] [descripción del documento].

Segundo.- [Hecho 2 narrado, con cita documental]
   Se acompaña como DOCUMENTO Nº [N] [...]

[...]

[Numeración ordinal romana en hechos, no arábiga]
[Cada hecho con prueba documental anexa]
[Estructura cronológica salvo justificación]
```

#### FUNDAMENTO DE DERECHO sobre X

```
[N].- DE [TEMA] (ej. "DE LA IMPROCEDENCIA DEL DESPIDO POR INSUFICIENCIA DE LA CARTA")

Es de aplicación al presente caso el artículo [N] del [norma], que dispone:

"[Cita literal del precepto si breve, o paráfrasis si extenso]"

[Desarrollo de la subsunción a los hechos del caso]

[Cita jurisprudencial — ECLI verificado]

En este sentido, la STS (Sala IV, de lo Social), núm. [...]/[año], de [fecha]
[ECLI: ES:TS:AAAA:NNNN], ponente [...], establece que:

"[Cita literal o paráfrasis del FJ pertinente]"

Doctrina que aplicada al caso de autos resulta determinante por cuanto [subsunción
a los hechos concretos del asunto: aquí NO mencionar la sentencia abstracta, sino
conectar con el hecho concreto del cliente].

Por todo ello, [conclusión jurídica del fundamento].
```

#### SUPLICO

```
SUPLICO al [Juzgado de lo Social / Sección de lo Social del Tribunal de Instancia /
Sala de lo Social del TSJ / Sala IV del Tribunal Supremo] que, teniendo por presentado
este escrito junto con los documentos acompañados, lo admita, señale día y hora para
los actos de conciliación y juicio, y, en su día, previos los trámites legales, dicte
sentencia por la que:

1.º [Pretensión principal — ej. declare NULO el despido con readmisión y salarios de
    tramitación / concreta + cuantía exacta si dineraria]
2.º [Pretensión subsidiaria si la hay, por orden — ej. subsidiariamente IMPROCEDENTE]
3.º [Accesorios: intereses del art. 29.3 ET, indemnización art. 183 LRJS]

[Si hay otrosíes, ir tras el SUPLICO]

OTROSÍ DIGO: [petición secundaria — ej. proposición anticipada de prueba (art. 90.3
LRJS), citación de la demandada para interrogatorio con apercibimiento del art. 91.2
LRJS, requerimiento de aportación del registro horario, expediente administrativo al
INSS (art. 143 LRJS), etc.]
```

### 4. Aplicar estilo de la casa

Si el CLAUDE.md así lo configura: encadenar con `estilo-escritos-judiciales`. Estructura tripartita, contrastes, explicación del por qué antes del qué.

### 5. Verificación de citas

Si la sección incluye jurisprudencia: verificar cada ECLI/ROJ con `jurisprudenciator` (`buscar_por_cita`).

### 6. Output

Texto de la sección, en formato listo para pegar en el .docx final. No el escrito completo.

### 7. Decision tree

> 1. **Refinar tono** — dime ajustes
> 2. **Próxima sección** — dime cuál
> 3. **Componer escrito completo** — `/redactar-demanda-despido` / `/reclamacion-cantidad` / `/recurso-suplicacion`

## Reglas

1. **Una sección = una pieza.** No mezclar HECHOS con FUNDAMENTOS aunque sean cortos.
2. **Pin-cite obligatorio.** Cada hecho con documento + cada jurisprudencia con ECLI.
3. **NO inventar.** Si falta dato (ej. nombre del ponente de la STS), marcar `[VERIFICAR — pendiente recuperar de jurisprudenciator]`.
4. **Aplicar estilo de la casa** automáticamente si está configurado.
