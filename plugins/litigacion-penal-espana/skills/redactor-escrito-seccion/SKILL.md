---
name: redactor-escrito-seccion
description: >-
  Redactar una seccion concreta de un escrito penal — encabezamiento a la Seccion de Instruccion del Tribunal de Instancia, Audiencia Provincial o Sala Segunda del TS; conclusiones numeradas del escrito de calificacion (art. 650 LECrim: hechos, calificacion, participacion, circunstancias modificativas, pena y responsabilidad civil); antecedentes procesales, motivos de recurso, suplico y otrosies. Anclaje al folio de las actuaciones. Usar con redacta las conclusiones, saca el suplico penal, redacta el motivo del recurso.
---

# Redactor de sección — escritos penales

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Encabezamiento con una persona jurídica como parte** → `buscar_empresa_mercantil` (denominación, CIF y domicilio social exactos).
- **Conclusiones del art. 650: tipo, circunstancias y pena** → `buscar_articulo` (`ley="CP"`; `ley="LECrim"`, `articulo="650"`).
- **Motivo de recurso con jurisprudencia** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"` o `base="AN"`; `base="TC"` si el motivo es de derechos fundamentales) + `leer_sentencias` con `parrafos=3`.
- **Cita que se reutiliza de otro escrito** → `buscar_por_cita`.
- **Sección terminada** → `verificar_escrito` sobre el texto de la sección.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

> **Fuente de cifras:** `references/anclas-normativas-penal.md`. Cada precepto se comprueba con
> `buscar_articulo` antes de citarlo.

## Cuándo activar

- "Redacta solo las CONCLUSIONES del escrito de defensa"
- "Redacta la conclusión SEGUNDA (calificación)"
- "Saca el SUPLICO"
- "Redacta los ANTECEDENTES PROCESALES de la apelación"
- "Redacta el MOTIVO de casación"
- Cuando hay que iterar sobre una sección sin reescribir el escrito entero

---

## 1. ENCABEZAMIENTOS PENALES

**Cada órgano tiene su fórmula. Equivocarla marca el escrito desde la primera línea.**

> ## ⭐ REGLA PRÁCTICA — LA MÁS ÚTIL DE ESTA SECCIÓN
>
> **Copia la denominación EXACTA que figure en la resolución que contestas o en la carátula del
> procedimiento.** No la deduzcas de esta tabla ni de memoria.
>
> Es lo que nunca falla: si el órgano se identifica a sí mismo como «Sección de Instrucción nº 3 del
> Tribunal de Instancia de [LUGAR]», eso escribes; si sus notificaciones, su sello o LexNET siguen
> diciendo «Juzgado de Instrucción nº 3 de [LUGAR]», **eso escribes**. Espejar al órgano es
> siempre correcto y evita discutir de nombres con quien te va a resolver.
>
> **Solo cuando no tengas resolución ni carátula** (p. ej., una denuncia o querella iniciales), usa
> la denominación **vigente** de la tabla siguiente.
>
> **Tranquilizador:** equivocarse **no invalida** el escrito. La **DA 1.ª de la LO 1/2025** ordena
> entender las referencias legales a los «Juzgados de Instrucción, de lo Penal, de Violencia sobre la
> Mujer…» hechas **a las Secciones correspondientes** de los Tribunales de Instancia. El nombre no es
> un requisito de admisibilidad. Pero se escribe bien.

### 1.1 Denominación vigente (art. 14 LECrim, desde el 3-10-2025)

La LO 1/2025 sustituyó los Juzgados por **Secciones de los Tribunales de Instancia**. El calendario
de implantación (DT 1.ª) **concluyó el 31-12-2025**: hoy ya no subsisten los Juzgados.

| Órgano | Encabezamiento |
|---|---|
| **Sección de Instrucción** | `A LA SECCIÓN DE INSTRUCCIÓN Nº [X] DEL TRIBUNAL DE INSTANCIA DE [LUGAR]` |
| **Sección de Violencia sobre la Mujer** | `A LA SECCIÓN DE VIOLENCIA SOBRE LA MUJER Nº [X] DEL TRIBUNAL DE INSTANCIA DE [LUGAR]` |
| ⭐ **Sección de Violencia contra la Infancia y la Adolescencia** (órgano NUEVO, art. 14.6) | `A LA SECCIÓN DE VIOLENCIA CONTRA LA INFANCIA Y LA ADOLESCENCIA Nº [X] DEL TRIBUNAL DE INSTANCIA DE [LUGAR]` |
| **Sección de lo Penal** | `A LA SECCIÓN DE LO PENAL Nº [X] DEL TRIBUNAL DE INSTANCIA DE [LUGAR]` |
| Audiencia Provincial | `A LA AUDIENCIA PROVINCIAL DE [PROVINCIA], SECCIÓN [X]` |
| Tribunal Superior de Justicia | `A LA SALA DE LO CIVIL Y PENAL DEL TRIBUNAL SUPERIOR DE JUSTICIA DE [CCAA]` |
| Audiencia Nacional | `A LA SALA DE LO PENAL DE LA AUDIENCIA NACIONAL` |
| **Tribunal Supremo** | `A LA SALA SEGUNDA DEL TRIBUNAL SUPREMO` |
| Juzgado Central de Instrucción / de lo Penal | `AL JUZGADO CENTRAL DE INSTRUCCIÓN Nº [X]` — **[verificar]**, ver nota |
| 🚨 **Sección de Vigilancia Penitenciaria** (art. 84.2.g y **92 LOPJ**) | `A LA SECCIÓN DE VIGILANCIA PENITENCIARIA Nº [X] DEL TRIBUNAL DE INSTANCIA DE [LUGAR]` |
| 🚨 **Sección de Menores** (art. 84.2.f y **91 LOPJ**) | `A LA SECCIÓN DE MENORES Nº [X] DEL TRIBUNAL DE INSTANCIA DE [LUGAR]` |

> **⚠️ Art. 14.7 — regla de conflicto:** si los hechos pueden ser conocidos por la Sección de
> Violencia contra la Infancia y la Adolescencia **y** por la de Violencia sobre la Mujer, la
> competencia es **en todo caso** de esta última. Encabeza a la de **Violencia sobre la Mujer**.

> **🚨 El JVP y el Juzgado de Menores TAMBIÉN son Secciones.** Es la trampa de esta tabla: como el
> art. 14 LECrim no los menciona, se dan por invariables. **No lo son.** El **art. 84.2 LOPJ** los
> lista como Secciones del Tribunal de Instancia —letras **f) De Menores** y **g) De Vigilancia
> Penitenciaria**— y la **DA 1.ª de la LO 1/2025** los cita **expresamente**. Sedes vigentes
> *(verificadas)*: **Sección de Menores → art. 91 LOPJ**; **Sección de Vigilancia Penitenciaria →
> art. 92 LOPJ**.
> ⚠️ **No cites «art. 94 LOPJ» para el JVP**: hoy el 94 es la **Sección de lo Social** y el 93 la de
> lo Contencioso-Administrativo.

> **[verificar] — Órganos centrales.** Hay un desajuste real, no una errata del plugin: el
> **art. 14.2 y 14.3 LECrim** siguen diciendo «**Juez Central de Instrucción**» y «**Juez Central de
> lo Penal**» *(verificado literalmente el 2026-07-17)*, pero la **DT 2.ª de la LO 1/2025**
> transformó los **Juzgados Centrales** en Secciones del **Tribunal Central de Instancia** el
> **31-12-2025**, y la **DA 1.ª** ordena entender las referencias a los Juzgados Centrales hechas a
> esas Secciones. **Aplica aquí la regla práctica sin excepción: copia la denominación exacta de la
> resolución.** No afirmes de memoria cuál es la fórmula correcta del encabezamiento central.

**Cuerpo del encabezamiento:**

```
A LA SECCIÓN DE INSTRUCCIÓN Nº [X] DEL TRIBUNAL DE INSTANCIA DE [LUGAR]

D./Dña. [PROCURADOR], Procurador/a de los Tribunales, en nombre y representación de
D./Dña. [INVESTIGADO], según consta acreditado en las actuaciones, bajo la dirección
letrada de D./Dña. [LETRADO], colegiado/a nº [PENDIENTE] del Ilustre Colegio de la
Abogacía de [LUGAR], ante esa Sección comparezco y, como mejor proceda en Derecho, DIGO:

Que por medio del presente escrito, y dentro del plazo conferido, vengo a [acto procesal],
en las Diligencias Previas nº [N]/[AÑO], con base en las siguientes
```

> **Escrito de defensa (art. 784.3 LECrim, verificado):** va **firmado también por el acusado**.
> Consignarlo en el pie.

---

## 2. ⭐ ESCRITOS DE CALIFICACIÓN — POR CONCLUSIONES NUMERADAS (art. 650 LECrim)

**Esta es la estructura propia del proceso penal y NO tiene nada que ver con la de una demanda
civil.** No hay «HECHOS + FUNDAMENTOS DE DERECHO + SUPLICO»: hay **CONCLUSIONES precisas y
numeradas**.

**Art. 650 LECrim — texto literal verificado:**

> «El escrito de calificación se limitará a determinar **en conclusiones precisas y numeradas**:
> 1.º **Los hechos punibles** que resulten del sumario.
> 2.º **La calificación legal** de los mismos hechos, determinando el delito que constituyan.
> 3.º **La participación** que en ellos hubieren tenido el procesado o procesados, si fueren varios.
> 4.º **Los hechos** que resulten del sumario **y que constituyan circunstancias atenuantes o
> agravantes** del delito **o eximentes** de responsabilidad criminal.
> 5.º **Las penas** en que hayan incurrido el procesado o procesados, si fueren varios, por razón de
> su respectiva participación en el delito.
>
> **El acusador privado, en su caso, y el Ministerio Fiscal cuando sostenga la acción civil,
> expresarán además:**
> 1.º **La cantidad en que aprecien los daños y perjuicios** causados por el delito, o **la cosa que
> haya de ser restituida**.
> 2.º **La persona o personas que aparezcan responsables** de los daños y perjuicios o de la
> restitución de la cosa, y **el hecho en virtud del cual** hubieren contraído esta
> responsabilidad.»

### Plantilla — conclusiones provisionales

```
CONCLUSIONES PROVISIONALES

PRIMERA.- HECHOS PUNIBLES (art. 650.1.º LECrim)

[Relato de hechos en párrafos numerados. Cada hecho:
 - narrado en tercera persona, en pasado, de forma objetiva y sin adjetivación
 - con FECHA, LUGAR y SUJETO
 - ANCLADO AL FOLIO: (f. [N])
 - solo hechos: nada de calificación jurídica ni de valoración probatoria]

  1. El día [FECHA], en [LUGAR], [ACUSADO] [conducta descrita objetivamente] (f. [N]).
  2. Como consecuencia de ello, [VÍCTIMA] [resultado] (f. [N]).
  3. [Hecho relativo al elemento subjetivo, descrito como hecho: «con el propósito de...»,
     «conociendo que...»] (f. [N]).

⚠️ El relato debe contener TODOS los elementos del tipo como HECHOS. Un elemento que no
   esté en la conclusión primera no puede sostenerse después: la calificación no puede
   apoyarse en hechos no relatados (principio acusatorio).

SEGUNDA.- CALIFICACIÓN LEGAL (art. 650.2.º LECrim)

Los hechos relatados son constitutivos de un delito de [TIPO], previsto y penado en el
**art. [N] del Código Penal**, en la redacción dada por [LO X], **vigente a la fecha de los
hechos** (art. 2 CP).

[Si hay ley posterior más favorable → art. 2.2 CP: hacerlo constar aquí y solicitarla]
[Si hay concurso: art. [73-77 CP] — verificar el precepto antes de citarlo]

TERCERA.- PARTICIPACIÓN (art. 650.3.º LECrim)

[ACUSADO] es responsable en concepto de **AUTOR**, conforme al **art. 28 CP**
[«quienes realizan el hecho por sí solos, conjuntamente o por medio de otro del que se
sirven como instrumento»; o inductor —art. 28.a)—; o cooperador necesario —art. 28.b)—;
o CÓMPLICE del art. 29 CP].

[Defensa: aquí es donde se discute cooperador necesario vs. cómplice — la frontera que
 más pena mueve]

CUARTA.- CIRCUNSTANCIAS MODIFICATIVAS (art. 650.4.º LECrim)

[⚠️ El art. 650.4.º pide LOS HECHOS que constituyan las circunstancias, no su etiqueta.
 Redactar el hecho y después nombrarla]

Concurre la circunstancia atenuante de **reparación del daño del art. 21.5.ª CP**: con
fecha [FECHA], y con anterioridad a la celebración del acto del juicio oral, [ACUSADO]
consignó la cantidad de [importe] € (f. [N]).

Concurre la circunstancia atenuante de **dilaciones indebidas del art. 21.6.ª CP**: la
causa permaneció paralizada entre [FECHA] y [FECHA], esto es, [N] meses (f. [N]-[N]),
sin que la dilación sea atribuible a esta parte ni guarde proporción con la complejidad
de la causa.

[Si no concurre ninguna: «No concurren circunstancias modificativas de la responsabilidad
 criminal.»]

QUINTA.- PENAS (art. 650.5.º LECrim)

Procede imponer a [ACUSADO], como autor del referido delito, con la concurrencia de las
circunstancias atenuantes [...], la pena de [pena concreta, con extensión exacta], así
como [penas accesorias — verificar arts. 54-57 CP] y el pago de [las costas / una N-ésima
parte de las costas].

[⚠️ La pena se pide EXACTA: «prisión de un año», no «la pena procedente». Verificar el
 marco con buscar_articulo y aplicar las reglas de determinación de los arts. 61-72 CP]

SEXTA.- RESPONSABILIDAD CIVIL (art. 650, párr. 2.º, 1.º y 2.º LECrim)

[Solo la acusación particular y el MF cuando sostenga la acción civil]

1.º Daños y perjuicios: [importe] €, o restitución de [cosa] (f. [N] — pericial).
2.º Responsable: [ACUSADO], como responsable civil directo (art. 116 CP), y
    [tercero], como responsable civil subsidiario (art. 120 CP) por [el hecho en virtud
    del cual ha contraído esa responsabilidad — art. 650 párr. 2.º 2.º LECrim].

[Verificar arts. 109-126 CP antes de citar. La acción civil derivada del delito se
 ejercita DENTRO del proceso penal: arts. 100, 108-117 LECrim y 109-126 CP]

[Defensa: si procede — «Procede la libre absolución de [ACUSADO], con todos los
 pronunciamientos favorables y declaración de costas de oficio.»]

OTROSÍ DIGO — PROPOSICIÓN DE PRUEBA

Para el acto del juicio oral, esta parte propone los siguientes medios de prueba:

1.º INTERROGATORIO de [ACUSADO].
2.º TESTIFICAL de [TESTIGO], con domicilio a efectos de citación en [...], que deberá
    ser citado judicialmente.
3.º PERICIAL de [perito], autor del dictamen obrante a los f. [N]-[N], que deberá ser
    citado a fin de ratificarlo y someterse a contradicción.
4.º DOCUMENTAL, consistente en la lectura y por reproducidos los f. [N], [N] y [N].

[Art. 784.2 LECrim (verificado): en el escrito de defensa se puede solicitar que el
 órgano recabe documentos o cite peritos o testigos]

⚠️ Art. 784.1 LECrim (verificado): precluido el trámite, la defensa SOLO podrá proponer
   la prueba que aporte en el acto del juicio oral para practicarse en el mismo — sin
   perjuicio del art. 785.1 párr. 2. NO dejar prueba fuera del escrito.
```

> **⚠️ Plazos del escrito de defensa (art. 784.1 LECrim, verificado):** **3 días** para comparecer
> con abogado y procurador desde el emplazamiento; **10 días comunes** para presentar el escrito de
> defensa. **Si no se presenta, se entiende que se opone a las acusaciones** y el procedimiento
> sigue su curso — pero **se pierde la proposición de prueba**, que es lo que importa.
>
> **Conclusiones definitivas:** tras la prueba, las provisionales pueden elevarse a definitivas o
> modificarse (**arts. 732 y 788.3-788.4 LECrim** — *verificar antes de citar*). **Son las
> definitivas las que fijan el objeto del proceso y vinculan a la sentencia.**

---

## 3. OTRAS SECCIONES SOPORTADAS

| Sección | Aplicable a |
|---|---|
| Encabezamiento | Todo escrito |
| **Conclusiones del art. 650** (1.ª a 5.ª + RC) | Escrito de acusación / de defensa |
| Otrosí de proposición de prueba | Escrito de acusación / de defensa |
| Hechos de la denuncia / querella | Denuncia, querella (art. 277 LECrim — *verificar requisitos y fianza del art. 280*) |
| Antecedentes procesales | Apelación, casación |
| Motivos de recurso | Apelación (art. 790), casación (arts. 847, 849-852) |
| Alegaciones para la audiencia preliminar (art. 785) | Cuestiones previas |
| Alegaciones sobre medidas cautelares | Prisión provisional (art. 505), art. 544 bis, 544 ter |
| Suplico | Todo escrito |
| Otrosíes | Donde proceda |

### ANTECEDENTES PROCESALES (recursos)

```
ANTECEDENTES PROCESALES

PRIMERO.- Por el [ÓRGANO] se dictó sentencia de fecha [FECHA], notificada a esta parte
el [FECHA], por la que se condenó a [ACUSADO] como autor de un delito de [TIPO] a la pena
de [pena].

SEGUNDO.- [Hitos procesales relevantes al recurso, con folio]

[⚠️ Fecha de NOTIFICACIÓN, no de la sentencia: es la que computa el plazo.
 Apelación: 10 días (art. 790.1). Preparación de casación: 5 días (art. 856)]
```

### MOTIVO DE RECURSO

```
MOTIVO [N].- [Al amparo del art. 849.1.º LECrim, por infracción de ley, al haberse
aplicado indebidamente el art. [N] CP / por inaplicación del art. [N] CP]

BREVE EXTRACTO DEL CONTENIDO: [una frase]

DESARROLLO:

[1] Norma infringida y sentido de la infracción.
[2] Respeto absoluto a los hechos probados — ⚠️ si el motivo es del 849.1.º, los hechos
    probados son intangibles: el motivo es de PURA SUBSUNCIÓN.
[3] Por qué los hechos probados no realizan el elemento [X] del tipo.
[4] Jurisprudencia de la Sala Segunda [verificar ECLI con buscar_por_cita].
[5] Pronunciamiento que se interesa.
```

> **🚨 Art. 847 LECrim — el error que más casaciones inadmite.** Contra sentencias dictadas **en
> apelación por las Audiencias Provinciales** y por la Sala de lo Penal de la AN, **SOLO cabe el
> motivo de infracción de ley del art. 849.1.º**. **No caben** 849.2.º (error de hecho documental),
> ni 850/851 (quebrantamiento de forma), ni **852 (infracción de precepto constitucional)**.
> Plantear otro motivo → **inadmisión**. Ver `references/anclas-normativas-penal.md` § 4.

### SUPLICO

```
SUPLICO A LA SALA que, teniendo por presentado este escrito, se sirva admitirlo y, en su
virtud, tenga por [interpuesto recurso de [tipo] / formuladas las conclusiones
provisionales de la defensa], y, previos los trámites legales, dicte [sentencia /
resolución] por la que:

1.º [Pretensión principal — concreta]
2.º [Pretensión subsidiaria, por orden]
3.º [Costas — arts. 123-126 CP y 239-241 LECrim: verificar antes de citar]

Es justicia que pido en [LUGAR], a [FECHA].

OTROSÍ DIGO: [petición secundaria]
```

---

## Flujo

1. **Identificar** sección + asunto (slug) + versión + objetivo concreto de la sección.
2. **Cargar contexto:** `matters/<slug>/matter.md`, `matters/<slug>/cronologia.md` (alimenta la
   conclusión primera y la atenuante de dilaciones), `matters/<slug>/cuadro-elementos.md` (alimenta
   las conclusiones segunda a quinta), y las actuaciones por folios.
3. **Paso 0 obligatorio:** identificar la **redacción del CP aplicable a la fecha de los hechos**
   (art. 2 CP) y comprobar si la posterior es **más favorable** (art. 2.2) → `/subsuncion-juridica`.
4. **Aplicar la plantilla** de la sección.
5. **Aplicar el estilo de la casa** → `estilo-escritos-judiciales`.
6. **Verificar:** cada precepto con `buscar_articulo`; cada ECLI/ROJ con `buscar_por_cita`.
7. **Output:** el texto de la sección, listo para pegar en el `.docx`. **No el escrito completo.**

### Decision tree

> 1. **Refinar tono** — indicar ajustes
> 2. **Próxima sección** — indicar cuál
> 3. **Verificar el escrito completo** — `verificar_escrito` (jurisprudenciator)
> 4. **Componer el escrito entero** — skill de redacción que corresponda

## Reglas

1. **Una sección = una pieza.**
2. **El escrito de calificación va por CONCLUSIONES numeradas** (art. 650 LECrim). ⛔ **Nunca la
   estructura de demanda civil.**
3. **La conclusión primera contiene TODOS los elementos del tipo como hechos.** Lo que no esté ahí
   no puede sostenerse en la segunda (principio acusatorio).
4. **Pin-cite al FOLIO.** `(f. [N])`. ⛔ **Nunca «Doc. nº X»** — nomenclatura civil.
5. **La pena se pide EXACTA**, verificada con `buscar_articulo`, en la redacción aplicable.
6. **⛔ NO inventar.** Falta un dato → `[VERIFICAR — pendiente de recuperar]`. **⛔ Prohibido citar
   jurisprudencia concreta** (ECLI/ROJ/fecha) sin `buscar_por_cita`.
7. **Protección de datos.** `[INVESTIGADO]`, `[ACUSADO]`, `[VÍCTIMA]`, `[TESTIGO]`, `[ÓRGANO]`,
   `[FECHA]`, `[PROCURADOR]`, `[LETRADO]`. **Cero datos reales.** Infracciones y condenas =
   **art. 10 RGPD**. Cuidado extremo con **víctimas menores** y **delitos contra la libertad
   sexual**: comprobar el régimen de protección antes de consignar identidad alguna.

## ⛔ Fuera de esta skill

- **`FUNDAMENTOS DE DERECHO — MASC`.** ❌ **ELIMINADO.** El MASC de la LO 1/2025 es requisito de
  procedibilidad del orden **civil** y **no existe en penal**. Cualquier sección de este tipo se
  suprime sin sustituto.
- **Fundamentos de competencia, procedimiento y postulación al modo de la demanda civil**, `SUPLICO
  AL JUZGADO DE PRIMERA INSTANCIA`, `DOCUMENTO Nº X`, burofax.
- **El «fiscal instructor».** Instruye el **Juez de Instrucción**. La reforma que atribuiría la
  instrucción al Ministerio Fiscal está **en tramitación** (prevista **1-1-2028**): **no se redacta
  ningún escrito dirigido a un fiscal instructor** ni se cita como Derecho vigente.
