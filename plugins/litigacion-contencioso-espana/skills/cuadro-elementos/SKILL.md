---
name: cuadro-elementos
description: Cuadro de elementos de la pretension contencioso-administrativa. Una fila por elemento a probar con articulo de LJCA/LPAC/LRJSP, hecho del caso, folio del expediente y estado. Fila transversal obligatoria de admisibilidad. Deteccion de gaps. Usar con cuadro de elementos o que nos falta para probar.
---

# Cuadro de elementos — contencioso-administrativo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Columna «Artículo» de cada fila** → `buscar_articulo` (`ley="LJCA"`, `"LPAC"` —letra exacta del art. 47.1 y art. 48— y `"LRJSP"`, artículos 25 a 34).
- **Tipo sancionador o requisito previsto en una ordenanza** → `buscar_ordenanzas` + `leer_ordenanza` con `articulo`.
- **Norma sectorial estatal** → `buscar_boe` + `leer_boe`. La autonómica se pide al usuario.
- **Elementos de construcción jurisprudencial** (interés legítimo, indefensión material, lex artis, antijuridicidad) → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Elemento ligado a un inmueble** (licencia, disciplina urbanística, responsabilidad viaria) → `consultar_catastro` (referencia, superficie, uso y localización).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Qué nos falta para probar [pretensión]"
- "¿Tenemos los elementos?"
- "Cuadro de elementos", "matriz de prueba"
- Antes de redactar la demanda o la contestación
- Al recibir el expediente administrativo (es cuando el cuadro se puede llenar de verdad)

## Variantes

- `--ofensivo` (default si el despacho actúa como recurrente): para sostener la pretensión propia
- `--defensivo` (default si se defiende a la Administración o se comparece como codemandado):
  para rebatir la pretensión contraria y explotar la inadmisibilidad
- `--inadmisibilidad`: solo la fila transversal, desarrollada. Es la primera pasada de cualquier
  asunto

## Regla de oro: la fila 0 es la ADMISIBILIDAD

> **De nada sirve tener razón si el recurso se inadmite.** Antes de mapear el fondo, el cuadro
> **siempre** abre con la fila transversal de admisibilidad. Si algo aquí está en 🔴, el fondo
> es irrelevante hasta resolverlo.

| # | Control | Norma | Qué verificar |
|---|---|---|---|
| 0.1 | **Plazo** (caducidad) | art. 46 LJCA; art. 69.e LJCA | Dies a quo desde la notificación; 2 meses (acto expreso) / 6 meses (presunto) / 10 o 20 días (vía de hecho). Agosto no corre (art. 128.2), **salvo DDFF**. Viene resuelto de `/cronologia` |
| 0.2 | **Jurisdicción y competencia** | arts. 8-14 LJCA | Orden contencioso; órgano objetivamente competente (art. 8: sanciones de CCAA ≤ 60.000 €, resp. patrimonial de CCAA ≤ 30.050 €; entidades locales, **excluido el planeamiento urbanístico**) |
| 0.3 | **Acto impugnable** | art. 25 LJCA; art. 69.c LJCA | ¿Pone fin a la vía administrativa? ¿Es de trámite **cualificado** (decide el fondo, impide continuar, produce indefensión o perjuicio irreparable)? ¿Es acto firme y consentido? ¿Meramente confirmatorio? |
| 0.4 | **Agotamiento de la vía administrativa** | art. 25.1 LJCA | ¿Cabía alzada y no se interpuso → prematuro? ¿La reposición era potestativa? **Nunca MASC: no existe en este orden** |
| 0.5 | **Legitimación** | art. 19 LJCA; art. 69.b LJCA | Interés legítimo (no mera legalidad, salvo acción pública — p. ej. urbanismo, con normativa a verificar) |
| 0.6 | 🚨 **Personas jurídicas — art. 45.2.d)** | art. 45.2.d) LJCA; art. 45.3 | Documento que acredite el **cumplimiento de los requisitos estatutarios para entablar acciones** (el «acuerdo corporativo»). **No basta el poder.** Es la causa de inadmisión más frecuente y más evitable. Subsanación: 10 días (art. 45.3) |
| 0.7 | **Sindicatos ex art. 19.1.k)** | art. 45.2.e) LJCA (LO 1/2025) | Afiliación + comunicación al afiliado + **autorización expresa** |
| 0.8 | **Representación y defensa** | art. 23 LJCA | Juzgados: procurador **potestativo**, abogado preceptivo. Órganos colegiados: procurador **preceptivo** + abogado. ⚠️ No aplicar el art. 23 **LEC** (regla civil de los 2.000 €): es otra norma |
| 0.9 | **Cuantía** | art. 40-42 LJCA `[verificar]`; art. 78.1 | Determina abreviado (≤ 30.000 €), acceso a apelación (excluida ≤ 30.000 €, art. 81.1.a) y el tope de costas (1/3, art. 139.4) |
| 0.10 | **Cosa juzgada / litispendencia** | art. 69.d LJCA | — |

## Marco: elementos de las pretensiones contenciosas típicas

> Las pretensiones se formulan al amparo del **art. 31 LJCA**: (1) declaración de no ser conforme a
> Derecho y, en su caso, **anulación** del acto; (2) **reconocimiento de una situación jurídica
> individualizada** y medidas para su pleno restablecimiento, **entre ellas la indemnización** de
> daños y perjuicios, cuando proceda.

| Pretensión | Elementos (resumen) |
|---|---|
| **Nulidad de pleno derecho** (art. 47.1 LPAC) | Encaje en un **motivo tasado** — la lista es cerrada: a) lesión de derechos y libertades susceptibles de **amparo constitucional**; b) órgano **manifiestamente incompetente** por materia o territorio; c) contenido **imposible**; d) constitutivos de **infracción penal** o dictados como consecuencia de ésta; e) **prescindiendo total y absolutamente del procedimiento** legalmente establecido o de las reglas esenciales para la formación de la voluntad de órganos colegiados; f) actos por los que se **adquieren facultades o derechos careciendo de los requisitos esenciales**; g) los que establezca una **norma con rango de Ley**. (Art. 47.2: nulidad de **disposiciones** administrativas) |
| **Anulabilidad** (art. 48 LPAC) | (1) **Cualquier infracción del ordenamiento jurídico**, incluida la **desviación de poder**; (2) si es **defecto de forma**: solo anula cuando el acto **carezca de los requisitos formales indispensables para alcanzar su fin** o **dé lugar a indefensión** (art. 48.2) — este es el filtro que hay que superar; (3) si es **extemporaneidad** de la actuación: solo anula cuando **lo imponga la naturaleza del término o plazo** (art. 48.3) |
| **Responsabilidad patrimonial** (art. 32 Ley 40/2015) | (1) **Lesión efectiva, evaluable económicamente e individualizada**; (2) **nexo causal** con el funcionamiento **normal o anormal** del servicio público; (3) **antijuridicidad** — que no exista deber jurídico de soportar el daño; (4) **ausencia de fuerza mayor** (la fuerza mayor excluye; el **caso fortuito no**); (5) **plazo: 1 año** (art. 67 Ley 39/2015) |
| **Resp. patrimonial SANITARIA** (art. 34.1 Ley 40/2015) | Los anteriores + (6) **infracción de la lex artis**: no son indemnizables los daños que el particular tenga el **deber jurídico de soportar** conforme a la Ley; estándar = lex artis y **estado de los conocimientos de la ciencia o de la técnica** en el momento. ⚠️ Plazo: el año se cuenta desde la **curación o la determinación del alcance de las secuelas** (art. 67 Ley 39/2015) — regla decisiva |
| **Sancionador** | (1) **Tipicidad** — encaje exacto en el tipo, sin analogía; (2) **culpabilidad** — no hay responsabilidad objetiva; (3) **presunción de inocencia** — la carga probatoria es de la Administración; (4) **proporcionalidad** de la sanción y motivación de la graduación; (5) **prescripción de la infracción**; (6) **caducidad del procedimiento**; (7) garantías del procedimiento (separación instructor/órgano decisor, audiencia, motivación). Preceptos concretos de LPAC/LRJSP y **norma sectorial**: `[verificar con buscar_articulo]` |
| **Urbanismo / licencias** | (1) **Competencia del órgano**; (2) **procedimiento debido** (informes preceptivos, audiencia, publicidad); (3) **ajuste al planeamiento** aplicable; (4) motivación del acto denegatorio; (5) en su caso, **silencio** y sus límites. ⚠️ La normativa material es **autonómica y local** — **pedirla al usuario, no inventarla** |
| **Inactividad** (art. 29 LJCA) | **29.1:** (1) obligación de realizar una **prestación concreta** en favor de personas determinadas, nacida de disposición general que no precise actos de aplicación, o de acto, contrato o convenio; (2) **reclamación previa** a la Administración; (3) transcurso de **3 meses** desde la reclamación sin cumplimiento ni acuerdo. **29.2:** (1) **acto firme** no ejecutado; (2) solicitud de ejecución; (3) transcurso de **1 mes** → recurso, que se tramita por el **procedimiento abreviado** del art. 78 |
| **Vía de hecho** (art. 30 LJCA) | (1) **Actuación material** de la Administración **sin cobertura** en acto o al margen del procedimiento; (2) **requerimiento** de cesación (potestativo); (3) si se requirió y no se atendió en **10 días** → recurso (plazo: **10 días** desde el fin de ese plazo); si **no** se requirió → recurso en **20 días** desde el inicio de la actuación material |

> **Pretensión de plena jurisdicción.** Si además de anular se pide el **reconocimiento de una
> situación jurídica individualizada** o **indemnización** (art. 31.2 LJCA), esos son elementos
> **autónomos** que exigen su propia prueba: no se derivan automáticamente de la anulación.
> Añadir filas propias (realidad del daño, cuantificación, nexo).

## Flujo

### 1. Identificar la pretensión

Vía `AskUserQuestion`: ¿qué se pretende — solo anulación, o también reconocimiento de situación
jurídica individualizada e indemnización (art. 31.2 LJCA)? ¿Qué vicio se invoca — nulidad tasada
(art. 47.1 LPAC) o anulabilidad (art. 48 LPAC)?

> **Aviso de encaje.** La nulidad de pleno derecho es de **interpretación restrictiva** y su lista
> es **tasada**. Un vicio de procedimiento ordinario **no** es nulidad del art. 47.1.e): esa letra
> exige haber prescindido **total y absolutamente** del procedimiento. Lo habitual es anulabilidad
> del art. 48, que además debe superar el filtro del 48.2 (indefensión o falta de requisitos
> formales indispensables). **Verificar la letra concreta antes de citarla** — nunca "art. 47 LPAC"
> a secas.

### 2. Correr SIEMPRE la fila 0 (admisibilidad)

Antes que el fondo. Tomar el cómputo de plazo ya resuelto en `/cronologia`.

### 3. Listar elementos del fondo

Aplicar la plantilla de la pretensión. Los preceptos sectoriales y **autonómicos** se piden al
usuario: **no se citan de memoria**.

### 4. Cargar evidencia disponible

- `matters/<slug>/matter.md` (hechos del intake)
- `matters/<slug>/cronologia.md` si existe
- **Expediente administrativo** — la fuente principal de prueba
- Documentos propios del cliente (informe pericial de parte, facturas, justificantes)

### 5. Mapping elemento ↔ prueba

Para CADA elemento:
- **Artículo** que lo sostiene — **LJCA / LPAC (Ley 39/2015) / LRJSP (Ley 40/2015)** + normativa
  sectorial. **Nunca LEC ni CC** salvo remisión supletoria expresa y justificada (DF 1.ª LJCA)
- **Hecho concreto** del caso que materializa el elemento
- **Prueba: el expediente administrativo y su FOLIO** (`EA folio [N]`). Si es prueba propia,
  `Doc. propio nº [N]`. Si el elemento se prueba por **ausencia** en el expediente, decirlo:
  `EA — NO CONSTA (folios [rango] revisados)`
- **Estado**: ✅ probado | 🟡 parcial | 🔴 faltante
- **Si faltante**: qué prueba se necesitaría y por qué vía (ampliación de expediente, pericial,
  testifical del funcionario interviniente)

> **Carga de la prueba — invertir el reflejo civil.** En **sancionador** rige la **presunción de
> inocencia**: no es el recurrente quien debe probar que no cometió la infracción, sino la
> Administración quien debe acreditar los hechos típicos. Un elemento del tipo que **no conste
> acreditado en el expediente** es una victoria, no un gap propio. Marcarlo como
> `EA — NO CONSTA` y ✅ **a nuestro favor**. Además, art. 60.3 LJCA: si el objeto del recurso es una
> **sanción administrativa o disciplinaria**, el proceso **se recibirá siempre a prueba** cuando
> exista disconformidad en los hechos.

### 6. Output

`matters/<slug>/cuadro-elementos.md`:

```markdown
# Cuadro de elementos — [slug]
**Pretensión:** [ej. Anulación de resolución sancionadora (art. 31.1 LJCA) por caducidad del
procedimiento y falta de tipicidad; subsidiariamente, reducción por desproporción]
**Acto impugnado:** [descripción] — [ÓRGANO]
**Variante:** [ofensivo / defensivo / inadmisibilidad]

## 0. ADMISIBILIDAD (transversal — se resuelve primero)

| # | Control | Norma | Situación | Estado |
|---|---|---|---|---|
| 0.1 | Plazo (caducidad) | art. 46.1 LJCA | Notificación [FECHA]; dies a quo [FECHA]; caducidad [FECHA] | ✅ |
| 0.2 | Competencia objetiva | art. 8.2.b) LJCA | Sanción de CCAA de [IMPORTE] € ≤ 60.000 € → Juzgado CA | ✅ |
| 0.3 | Acto impugnable | art. 25.1 LJCA | Resolución que agota la vía | ✅ |
| 0.4 | Agotamiento de vía | art. 25.1 LJCA | Alzada desestimada — EA folio [N] | ✅ |
| 0.5 | Legitimación | art. 19.1.a) LJCA | Destinatario del acto sancionador | ✅ |
| 0.6 | **Acuerdo corporativo (persona jurídica)** | art. 45.2.d) LJCA | **No consta certificación del acuerdo del órgano competente — solo el poder** | 🔴 |
| 0.8 | Postulación | art. 23.1 LJCA | Juzgado: abogado preceptivo; procurador potestativo | ✅ |

🚨 **BLOQUEANTE (0.6):** sin el documento del art. 45.2.d) el recurso se inadmite. Subsanable en
10 días (art. 45.3), pero **mejor aportarlo con la interposición**. Recabar de [CLIENTE]
certificación del acuerdo del órgano social competente para el ejercicio de acciones.

## Elementos del fondo

| # | Elemento | Artículo | Hecho del caso | Prueba (EA folio) | Estado |
|---|---|---|---|---|---|
| 1 | Caducidad del procedimiento | art. [N] LPAC `[verificar]` | Incoación notificada [FECHA]; resolución notificada [FECHA] — transcurso de [N] meses | EA folio 11 (notificación incoación) + EA folio 33 (notificación resolución) | ✅ |
| 2 | Tipicidad — encaje en el tipo | art. [N] norma sectorial `[pedir al usuario]` | La conducta descrita no integra el elemento [X] del tipo | EA folio 27-31 (resolución) | 🟡 |
| 3 | Presunción de inocencia | art. 24.2 CE; LPAC `[verificar]` | El elemento [X] del tipo no está acreditado por prueba alguna | **EA — NO CONSTA (folios 1-33 revisados)** | ✅ (a nuestro favor) |
| 4 | Indefensión por rechazo inmotivado de prueba | art. 48.2 LPAC | Prueba propuesta en alegaciones; la propuesta de resolución no se pronuncia | EA folio 14-19 (alegaciones) + EA folio 22 (propuesta) | ✅ |
| 5 | Proporcionalidad / graduación | LRJSP `[verificar]` | Sanción en grado máximo sin motivar la agravación | EA folio 27-31 | 🟡 |

## Análisis de cobertura

- Admisibilidad: 6/7 ✅ — **1 bloqueante (0.6)**
- Fondo: 3 ✅ / 2 🟡 / 0 🔴

## GAPS

🚨 **(0.6) Acuerdo corporativo del art. 45.2.d) LJCA — BLOQUEANTE.** Recabar antes de interponer.
🟡 **(2) Tipicidad** — depende de la norma sectorial [autonómica]: **pedir al usuario el texto
   vigente**. No citar de memoria.
🟡 **(5) Proporcionalidad** — reforzar con criterios de graduación de la norma sectorial.

## Próximos pasos

1. Recabar la certificación del acuerdo corporativo (0.6) — bloqueante
2. Pedir al usuario la norma sectorial autonómica aplicable (elementos 2 y 5)
3. Si la cobertura está completa → `/redactar-demanda`
4. Otrosí de recibimiento a prueba: art. 60.3 LJCA — al ser sanción, con disconformidad en los
   hechos el recibimiento a prueba es obligado
```

### 7. Decision tree

> 1. **Si hay 🔴 o 🚨 en admisibilidad** — resolverlo antes que nada. Nada del fondo importa.
> 2. **Si todos ✅** — proceder con `/redactar-demanda` o `/redactar-contestacion`
> 3. **Si hay 🔴 en el fondo** — pedir ampliación del expediente, pericial, o reconsiderar viabilidad
> 4. **Si hay 🟡** — preparar prueba y otrosí de recibimiento a prueba (art. 60.1 LJCA: **solo por
>    otrosí** en demanda o contestación)

## Reglas

1. **La admisibilidad es la fila 0 y es obligatoria.** No se entrega un cuadro sin ella. El
   art. 45.2.d) se comprueba **siempre** que el recurrente sea persona jurídica.
2. **Pin-cite al FOLIO del expediente en cada celda.** Sin folio (o sin marca de prueba propia),
   el elemento no se considera probado.
3. **Columna Artículo = LJCA / LPAC / LRJSP + sectorial.** Si aparece un artículo de la **LEC** o
   del **CC**, es contaminación: eliminarlo. La LEC solo entra por remisión supletoria expresa
   (DF 1.ª LJCA) y hay que decir que es supletoria.
4. **Nulidad ≠ anulabilidad.** La nulidad del art. 47.1 LPAC exige encaje en una **letra concreta**
   de una lista **tasada**: identificarla y verificarla con `buscar_articulo` antes de citarla.
   Lo ordinario es la anulabilidad del art. 48, que debe superar el filtro del 48.2.
5. **Cero MASC.** No es requisito en este orden. El equivalente es el agotamiento de la vía
   administrativa (art. 25.1 LJCA).
6. **La ausencia en el expediente es prueba.** Sobre todo en sancionador, donde rige la presunción
   de inocencia. Consignarla expresamente con el rango de folios revisados.
7. **Normativa autonómica y local: pedirla, no inventarla.** El conector cubre **BOE estatal**,
   jurisprudencia, DGT y ordenanzas de los municipios cubiertos. La normativa **autonómica** no es
   accesible. Marcar `[pedir al usuario]` y no citar de memoria.
8. **GAPS son la salida prioritaria.** El propósito del cuadro es detectar lo que falta, no
   presumir lo que hay.
9. **Conservador en el estado.** Si dudoso, ✅ → 🟡. Si claramente faltante, 🔴.
10. **Jurisprudencia solo verificada.** Si un elemento se apoya en doctrina jurisprudencial,
    localizarla con `buscar_sentencias` / `buscar_por_cita`. **No citar ECLI/ROJ de memoria.**
11. **Protección de datos.** `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`. ⚠️ El expediente
    contiene datos de **terceros** (denunciantes, otros interesados) y de **salud** (art. 9 RGPD,
    categoría especial): citar el folio, **nunca reproducir el dato**.
