---
name: redactor-escrito-seccion
description: >-
  Redactar una seccion concreta de un escrito contencioso-administrativo: encabezamiento a Sala o Juzgado de lo Contencioso, hechos anclados al expediente, fundamentos procesales y de fondo, suplico del art. 31 LJCA y otrosies. Usar con redacta los hechos o saca el suplico.
---

# Redactor de sección concreta — contencioso-administrativo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **FD procesal: jurisdicción, competencia, legitimación, postulación y plazo** → `buscar_articulo` (`ley="LJCA"`, artículos 1, 8, 19, 23, 25, 45 y 46).
- **Cita literal del precepto en el FD de fondo** → `buscar_articulo` (`ley` y `articulo`) antes de transcribirlo.
- **Jurisprudencia del FD con ECLI y párrafo literal** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`; `base="TS"`, o `base="AN"` con `tipo_organo="TSJ"` de la CCAA competente) + `leer_sentencias` (`parrafos=3`, `terminos`); `buscar_por_cita` para las citas que ya trae el borrador.
- **Ordenanza municipal aplicada** → `buscar_ordenanzas` + `leer_ordenanza` con `articulo`.
- **Inmueble en los HECHOS** → `consultar_catastro` (referencia catastral y localización).
- **Verificación de la sección** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

---

> 📕 **Plazos, umbrales y requisitos: `references/anclas-normativas-ca.md`.** Nada de memoria.

## Cuándo activar

- "Redacta solo los HECHOS de la demanda"
- "Redacta el FUNDAMENTO DE DERECHO sobre [punto]"
- "Saca el SUPLICO"
- "Redacta el otrosí de medidas cautelares"
- Cuando necesitas iterar sobre una sección sin reescribir todo

## Secciones soportadas

| Sección | Aplicable a |
|---|---|
| Encabezamiento | Todo escrito |
| Escrito de interposición | Recurso contencioso (art. 45 LJCA) |
| Hechos (anclados al expediente) | Demanda, contestación, recurso |
| Antecedentes procesales | Apelación, casación |
| FD procesal — jurisdicción | Demanda |
| FD procesal — competencia (objetiva y territorial) | Demanda |
| FD procesal — legitimación | Demanda |
| FD procesal — **plazo y agotamiento de vía** | Demanda |
| FD procesal — postulación (art. 23 LJCA) | Demanda |
| FD procesal — cuantía | Demanda |
| FD — fondo | Cualquier escrito |
| FD — costas (art. 139 LJCA) | Cualquier escrito |
| Suplico / Petitum (**art. 31 LJCA**) | Toda demanda / recurso |
| Otrosíes (cuantía, cautelares, prueba, vista o conclusiones) | Donde proceda |
| Motivos de impugnación | Apelación / casación |

> ⛔ **Sección eliminada: «FD — MASC».** El MASC es requisito de procedibilidad del orden **civil**
> (LEC, LO 1/2025) y **no existe** en contencioso. Su equivalente funcional es el **agotamiento de
> la vía administrativa** (art. 25.1 LJCA), que se trata en el FD procesal de plazo y vía. Si un
> escrito trae un fundamento de MASC, es contaminación de plantilla: eliminarlo.

## Flujo

### 1. Identificar sección + asunto

- Sección a redactar
- Asunto (slug)
- **Órgano** destinatario y **cauce** (ordinario / abreviado / DDFF) — condiciona encabezamiento,
  postulación y otrosíes
- Versión del escrito (v1, v2 si itera)
- Objetivo concreto de la sección

### 2. Cargar contexto

- `matters/<slug>/matter.md` (tesis)
- `matters/<slug>/cronologia.md` (hitos y **control de caducidad**)
- `matters/<slug>/cuadro-elementos.md` (admisibilidad + cobertura probatoria)
- **Expediente administrativo** (folios)

### 3. Aplicar plantilla por tipo de sección

#### ENCABEZAMIENTO

Elegir según el órgano (art. 23 LJCA determina la postulación):

```
A LA SALA DE LO CONTENCIOSO-ADMINISTRATIVO DEL TRIBUNAL SUPERIOR DE JUSTICIA
DE [CCAA]
   [Órgano colegiado → procurador PRECEPTIVO + abogado (art. 23.2 LJCA)]

AL JUZGADO DE LO CONTENCIOSO-ADMINISTRATIVO Nº [X] DE [LUGAR]
   [Órgano unipersonal → abogado siempre preceptivo; procurador POTESTATIVO (art. 23.1 LJCA).
    Si se confiere la representación al abogado, a él se le notifican las actuaciones]

A LA SALA DE LO CONTENCIOSO-ADMINISTRATIVO DE LA AUDIENCIA NACIONAL
AL JUZGADO CENTRAL DE LO CONTENCIOSO-ADMINISTRATIVO Nº [X]
A LA SALA DE LO CONTENCIOSO-ADMINISTRATIVO DEL TRIBUNAL SUPREMO
   [Sección [N.ª]]
```

Comparecencia:

```
D./Dña. [PROCURADOR], Procurador/a de los Tribunales, en nombre y representación de
[CLIENTE], según acredito mediante [poder / apud acta / poder electrónico], bajo la
dirección letrada de D./Dña. [LETRADO], colegiado/a nº [Nº] del Ilustre Colegio de la
Abogacía de [LUGAR], ante la Sala comparezco y, como mejor proceda en Derecho, DIGO:

[Si es Juzgado y la representación la ostenta el abogado (art. 23.1 LJCA):]
D./Dña. [LETRADO], abogado/a, colegiado/a nº [Nº] del Ilustre Colegio de la Abogacía de
[LUGAR], actuando en nombre y representación de [CLIENTE] conforme al artículo 23.1 de la
LJCA, según acredito mediante [poder / apud acta], ante el Juzgado comparezco y DIGO:
```

> ⚠️ **Nunca** "AL JUZGADO DE PRIMERA INSTANCIA" ni "A LA AUDIENCIA PROVINCIAL": son órganos del
> orden civil. Si aparecen, es contaminación de plantilla.

#### HECHOS — anclados al expediente

En contencioso los hechos **no** se narran como una historia entre particulares: se narran
siguiendo el **iter del procedimiento administrativo**, folio a folio. La estructura la marca el
expediente, y el hecho final y decisivo es siempre la **notificación**.

```
HECHOS

PRIMERO.- [Acto o actuación de origen: solicitud, denuncia, incoación]
   [Narración en 2-3 frases, neutra, sin adjetivos]
   Consta al folio [N] del expediente administrativo.

SEGUNDO.- Incoación del procedimiento y su notificación a esta parte el [FECHA].
   Folios [rango] del expediente administrativo.

TERCERO.- Escrito de alegaciones presentado el [FECHA], en el que esta parte [...] y propuso
   la práctica de [prueba].
   Folios [rango] del expediente administrativo (copia sellada de registro de entrada).

CUARTO.- Propuesta de resolución de [FECHA]. La propuesta **no se pronuncia** sobre la prueba
   propuesta en el hecho anterior.
   Folio [N] del expediente administrativo.

QUINTO.- Resolución de [FECHA] por la que [ÓRGANO] acuerda [...].
   Folios [rango] del expediente administrativo.

SEXTO.- La resolución fue **notificada a esta parte el [FECHA]**, mediante [medio], poniendo
   fin a la vía administrativa. Se acompaña como DOCUMENTO Nº 1 la notificación con su acuse.
   Folio [N] del expediente administrativo.
   [ESTE ES EL HECHO DEL QUE CUELGA EL PLAZO — art. 46.1 LJCA. Nunca omitirlo ni difuminarlo]

SÉPTIMO.- [Si procede] Recurso de alzada interpuesto el [FECHA] y [resuelto por [...] /
   desestimado por silencio el [FECHA]].
   Folios [rango] del expediente administrativo.

[Numeración ordinal, no arábiga]
[Cada hecho anclado a FOLIO del expediente; los documentos propios, como DOCUMENTO Nº N]
[Estructura por el iter del procedimiento]
[Hechos = hechos. La valoración jurídica va a los fundamentos]
```

> **Documentos propios vs. expediente.** El expediente lo remite la Administración: se cita por
> **folio**. Lo que aporta el cliente (notificación, informe pericial de parte, facturas) se
> acompaña como **DOCUMENTO Nº [N]**. Si un hecho consta en documentación del cliente pero **no**
> en el expediente, decirlo expresamente: es un hallazgo (expediente incompleto → posible
> indefensión).

#### FD PROCESAL — plazo y agotamiento de la vía (el que nunca falta)

```
[N].- JURISDICCIÓN, COMPETENCIA, LEGITIMACIÓN Y PLAZO

Jurisdicción. Corresponde al orden contencioso-administrativo el conocimiento del presente
recurso, dirigido contra [acto] dictado por [ÓRGANO], conforme a los artículos 1 y 25.1 de
la Ley 29/1998, de 13 de julio (LJCA).

Competencia. [ej.: Es competente el Juzgado de lo Contencioso-Administrativo conforme al
artículo 8.2.b) LJCA, por tratarse de sanción impuesta por la Administración de la Comunidad
Autónoma cuya cuantía, de [IMPORTE] €, no excede de 60.000 €.]
   [Verificar el apartado concreto del art. 8 con buscar_articulo — no citar de memoria]

Legitimación. [CLIENTE] ostenta legitimación activa al amparo del artículo 19.1.a) LJCA, por
ser destinatario/a del acto impugnado y titular de un interés legítimo directo.

Agotamiento de la vía administrativa. El acto impugnado pone fin a la vía administrativa
(artículo 25.1 LJCA), al [haber sido desestimado el recurso de alzada interpuesto / ser
resolución del órgano que agota la vía / haberse producido la desestimación presunta].

Plazo. La resolución fue notificada el [FECHA] (folio [N] del expediente). Interponiéndose el
presente recurso el [FECHA], se ha respetado el plazo de DOS MESES del artículo 46.1 LJCA,
computado desde el día siguiente a la notificación.
   [Si agosto media: y sin que corra el mes de agosto, conforme al artículo 128.2 LJCA]
   [Si es silencio: plazo de SEIS MESES desde el día siguiente a producirse el acto presunto]
   [Si es DDFF: plazo de 10 días del art. 115.1 LJCA — y ATENCIÓN: agosto SÍ es hábil]

Postulación. [Juzgado: Esta parte comparece bajo dirección letrada, ostentando la
representación el/la letrado/a que suscribe conforme al artículo 23.1 LJCA. / Sala: representada
por Procurador/a y asistida de Letrado/a conforme al artículo 23.2 LJCA.]

Documentos del artículo 45.2 LJCA. Se acompañan [poder / acreditación de representación],
copia del acto impugnado y, al ser [CLIENTE] persona jurídica, certificación del acuerdo del
órgano competente para el ejercicio de acciones, a los efectos del artículo 45.2.d) LJCA.
   [🚨 Si el recurrente es persona jurídica, esta mención es OBLIGATORIA. Su omisión es la causa
    de inadmisión más frecuente. Subsanable en 10 días (art. 45.3), pero mejor aportarlo ya]
```

#### FD — FONDO

```
[N].- DE [TEMA] (ej. "DE LA CADUCIDAD DEL PROCEDIMIENTO SANCIONADOR")

Es de aplicación el artículo [N] de la [LPAC / LRJSP / norma sectorial], que dispone:

"[Cita literal del precepto — verificada con buscar_articulo]"

[Lectura del precepto con su filtro: qué exige realmente, no lo que conviene que exija]

[Subsunción al expediente: hecho concreto + FOLIO]

[Jurisprudencia — ECLI verificado con buscar_por_cita]
En este sentido, la STS, Sala Tercera, Sección [N.ª], núm. [...]/[año], de [FECHA]
[ECLI: ES:TS:AAAA:NNNN], establece que:

"[Cita literal o paráfrasis del FJ pertinente]"

Doctrina que, aplicada al caso de autos, resulta determinante por cuanto [subsunción a los
hechos concretos del expediente, con folio — aquí NO repetir la sentencia en abstracto].

Por todo ello, [conclusión jurídica en términos del art. 31 LJCA].
```

> **Nulidad vs. anulabilidad.** Si se invoca **nulidad de pleno derecho**, citar la **letra
> concreta** del art. 47.1 LPAC y justificar el encaje: la lista es **tasada** y de interpretación
> restrictiva. Si es **anulabilidad** (art. 48 LPAC), y el vicio es de forma, hay que **superar el
> filtro del art. 48.2**: solo anula el defecto que prive al acto de los requisitos formales
> indispensables para alcanzar su fin **o** cause **indefensión**. Sin ese puente, el fundamento
> no vale.
>
> **Normativa autonómica y local:** `[PEDIR AL USUARIO]`. El conector no cubre boletines
> autonómicos. **No citarla de memoria.**

#### SUPLICO — las pretensiones del art. 31 LJCA

```
SUPLICO A LA SALA / AL JUZGADO que, teniendo por presentado este escrito con los documentos
que se acompañan, se sirva admitirlo, tener por [interpuesto recurso contencioso-administrativo /
formalizada la demanda] contra [acto] dictado por [ÓRGANO], y, previos los trámites legales,
dicte sentencia por la que, estimando el recurso:

1.º DECLARE no ser conforme a Derecho y ANULE [el acto impugnado / la resolución de [FECHA]],
   dejándolo/a sin efecto.
   [Art. 31.1 LJCA — pretensión de anulación]

2.º RECONOZCA la situación jurídica individualizada de [CLIENTE] consistente en [derecho
   concreto: p. ej. el derecho a la licencia solicitada / a la reincorporación / a la devolución
   de [IMPORTE] €] y ADOPTE las medidas necesarias para su pleno restablecimiento, entre ellas
   [medida concreta].
   [Art. 31.2 LJCA — plena jurisdicción. SOLO si se pide y se ha probado como elemento autónomo]

3.º CONDENE a [ÓRGANO] a indemnizar a [CLIENTE] en la cantidad de [IMPORTE] €, más los
   intereses legales devengados desde [FECHA].
   [Art. 31.2 LJCA — indemnización de daños y perjuicios, "cuando proceda"]

4.º [Subsidiariamente, si procede] [Pretensión subsidiaria — p. ej. reduzca la sanción a
   [IMPORTE] € por desproporción]

5.º Con expresa imposición de costas a la Administración demandada.
   [Art. 139.1 LJCA — vencimiento objetivo en 1.ª o única instancia, salvo serias dudas de
    hecho o de derecho apreciadas y razonadas]
```

> ⚠️ **Lo que NO se pide en un suplico contencioso:** resolución contractual, condena dineraria
> "civil" sin anulación previa del acto, ni pretensiones del CC. La anulación es la puerta: el
> reconocimiento de la situación jurídica y la indemnización **cuelgan** de ella (art. 31.2).
> Si solo se anula sin pedir el 31.2, la sentencia estimatoria puede dejar al cliente donde estaba.
> **Preguntarlo siempre.**

#### OTROSÍES

```
PRIMER OTROSÍ DIGO: CUANTÍA. Que la cuantía del presente recurso se fija en [IMPORTE] € /
se estima INDETERMINADA, a los efectos de [procedimiento aplicable / acceso a apelación /
tope de costas].
   [Determina: abreviado ≤ 30.000 € (art. 78.1); apelación excluida ≤ 30.000 € (art. 81.1.a);
    tope de costas de 1/3 de la cuantía, y 18.000 € si es indeterminada, a esos solos efectos
    (art. 139.4)]
SUPLICO A LA SALA / AL JUZGADO que tenga por fijada la cuantía indicada.

SEGUNDO OTROSÍ DIGO: MEDIDAS CAUTELARES. Que al amparo de los artículos 129 y siguientes de
la LJCA, y por resultar que la ejecución del acto impugnado haría perder al recurso su
finalidad legítima (artículo 130.1 LJCA), interesa la suspensión de [...], sin que de su
otorgamiento se siga perturbación grave de los intereses generales o de tercero (artículo
130.2 LJCA).
SUPLICO que se acuerde la formación de PIEZA SEPARADA (artículo 131 LJCA) y, previos los
trámites legales, se acuerde la medida cautelar interesada.
   [Solicitables en cualquier estado del proceso (art. 129). Especial urgencia → cautelarísima
    inaudita parte (art. 135). Caución: art. 133]

TERCER OTROSÍ DIGO: RECIBIMIENTO A PRUEBA. Que interesa el recibimiento del proceso a prueba,
que se solicita por medio del presente otrosí conforme al artículo 60.1 LJCA, versando sobre
los siguientes PUNTOS DE HECHO:
   1.º [Punto de hecho controvertido, concreto]
   2.º [...]
y proponiéndose los siguientes MEDIOS DE PRUEBA:
   a) DOCUMENTAL: la obrante en el expediente administrativo, con expresa designación de los
      folios [rango]; y la que se acompaña como DOCUMENTOS Nº [rango].
   b) PERICIAL: [...]
   c) TESTIFICAL: D./Dña. [FUNCIONARIO], [cargo] de [ÓRGANO], interviniente en el expediente
      a los folios [rango], sobre el punto de hecho [N.º].
   [Justificar por qué cada testigo aporta un punto DISTINTO — en abreviado el juez puede
    limitarlos discrecionalmente si son reiterativos (art. 78.14)]
   [SANCIONADOR: invocar el art. 60.3 LJCA — si el objeto del recurso es una sanción
    administrativa o disciplinaria, el proceso se recibirá SIEMPRE a prueba cuando exista
    disconformidad en los hechos]
SUPLICO que se acuerde el recibimiento del proceso a prueba.
   [⚠️ Art. 60.1: la prueba SOLO se pide por otrosí en demanda, contestación o alegaciones
    complementarias, expresando de forma ordenada los puntos de hecho y los medios. Si no se
    pide aquí, no hay prueba]

CUARTO OTROSÍ DIGO: VISTA O CONCLUSIONES. Que interesa la celebración de VISTA / la
presentación de escrito de CONCLUSIONES.
   [Ordinario: art. 62 LJCA `[verificar]`; conclusiones, 10 días (art. 64.1)]
   [Abreviado: el actor puede pedir por otrosí en la demanda que el recurso se falle SIN
    recibimiento a prueba NI vista (art. 78.3)]
SUPLICO que se acuerde [...].
```

### 4. Aplicar estilo de la casa

Si el CLAUDE.md así lo configura: encadenar con `estilo-escritos-judiciales`.

### 5. Verificación

- Preceptos citados → `buscar_articulo` (texto **vigente**)
- Plazos y umbrales → `references/anclas-normativas-ca.md`
- ECLI/ROJ → `buscar_por_cita`
- Escrito completo → `verificar_escrito` si procede

### 6. Output

Texto de la sección, listo para pegar en el `.docx` final. No el escrito completo.

### 7. Decision tree

> 1. **Refinar tono** — dime ajustes
> 2. **Próxima sección** — dime cuál
> 3. **Componer escrito completo** — `/redactar-demanda` / `/recurso-apelacion`

## Reglas

1. **Una sección = una pieza.** No mezclar HECHOS con FUNDAMENTOS.
2. **Encabezamiento correcto o nada.** Sala de lo Contencioso-Administrativo del TSJ / Juzgado de
   lo Contencioso-Administrativo / AN / TS. **Nunca** Primera Instancia ni Audiencia Provincial.
   El órgano determina además la postulación (art. 23 LJCA).
3. **Los HECHOS se anclan al FOLIO del expediente.** `Folio [N] del expediente administrativo`.
   Los documentos propios, `DOCUMENTO Nº [N]`. La notificación del acto que agota la vía es el
   hecho del que cuelga el plazo: **nunca omitirlo**.
4. **El SUPLICO es el art. 31 LJCA.** Anulación y, en su caso, reconocimiento de situación jurídica
   individualizada + indemnización. Preguntar siempre si se pide el 31.2: sin él, ganar puede no
   servir de nada.
5. **Cero MASC.** No existe en este orden. No hay fundamento de MASC. El equivalente es el
   agotamiento de la vía administrativa (art. 25.1 LJCA), que va en el FD procesal.
6. **Art. 45.2.d) si el recurrente es persona jurídica.** Mención obligatoria en el FD procesal y
   documento aportado. Es la inadmisión más frecuente y más evitable.
7. **La prueba solo por otrosí** (art. 60.1 LJCA), con puntos de hecho y medios. Si no se pide ahí,
   no hay prueba.
8. **Pin-cite obligatorio.** Cada hecho con folio + cada jurisprudencia con ECLI verificado.
9. **NO inventar.** Plazos y umbrales solo desde las anclas o verificados en el momento. Normativa
   **autonómica**: `[PEDIR AL USUARIO]`, nunca de memoria. Si falta un dato (ponente, número de
   sentencia), marcar `[VERIFICAR — pendiente de jurisprudenciator]`.
10. **Protección de datos.** `[CLIENTE]`, `[ÓRGANO]`, `[LETRADO]`, `[PROCURADOR]`, `[FECHA]`,
    `[IMPORTE]`. Cero DNI, IBAN, nombres, direcciones o teléfonos reales en los ejemplos. ⚠️ El
    expediente contiene datos de **terceros** (denunciantes, otros interesados) y de **salud**
    (art. 9 RGPD, categoría especial): en los HECHOS **citar el folio y describir de forma
    despersonalizada**, nunca transcribir el dato. En el escrito real que se presenta, los datos
    identificativos del cliente los cumplimenta el letrado, no la skill.
