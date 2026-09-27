---
name: recurso-apelacion-ca
description: Redacta el recurso de apelación contencioso-administrativo contra sentencias y autos de los Juzgados de lo Contencioso-administrativo (arts. 80-85 LJCA), ante la Sala del TSJ o de la Audiencia Nacional. Activar con "apelación contencioso", "recurrir sentencia del Juzgado de lo Contencioso", "art. 85 LJCA", "apelar el auto de medidas cautelares", "oposición a la apelación".
---

# Recurso de apelación contencioso-administrativo (arts. 80-85 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Apelabilidad, plazo y costas** → `buscar_articulo` (`ley="LJCA"`, artículos 80, 81, 85 y 139).
- **Criterio de la Sala ad quem sobre el punto discutido** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia` de la Sala) + `leer_sentencias` (`parrafos=3`).
- **Doctrina del TS para los motivos de fondo** → `buscar_sentencias` (`base="TS"`) + `leer_sentencias`.
- **Citas de la sentencia apelada** → `buscar_por_cita` para comprobar que dicen lo que la sentencia les atribuye.
- **Antes de presentar** → `verificar_escrito` sobre el escrito completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

Redacta la apelación ante la Sala competente (TSJ o AN) contra resoluciones de los Juzgados de lo
Contencioso-administrativo y de los Juzgados Centrales. Plazos y cifras:
`references/anclas-normativas-ca.md`. Lo no anclado, verificarlo con `buscar_articulo` o marcarlo
`[verificar]`.

---

## 1. Bloque de recurribilidad — cerrar ANTES de redactar

### 1.1 ¿Es apelable la sentencia? (art. 81, verificado — redacción RD-ley 6/2023)

**Regla:** las sentencias de los Juzgados de lo Contencioso-administrativo y de los Juzgados Centrales
**son apelables**, **salvo** (art. 81.1):

- **a) Cuantía que NO exceda de 30.000 €.** ✅ **Umbral verificado: 30.000 €.** No es dudoso, no hay que
  «comprobar el umbral»: es el vigente. (Coincide con el techo del **abreviado**, art. 78.1.)
- **b) Materia electoral del art. 8.4** LJCA.

### 1.2 ⚠️ Sentencias SIEMPRE apelables, con independencia de la cuantía (art. 81.2)

Aunque la cuantía no exceda de 30.000 €:

| | Supuesto |
|---|---|
| a) | Las que declaren la **inadmisibilidad** del recurso en el caso de la letra a) del art. 81.1 (es decir, en asuntos de cuantía ≤ 30.000 €). |
| b) | Las dictadas en el procedimiento para la **protección de los derechos fundamentales** de la persona (concuerda con el art. 121.3: apelación **en un solo efecto**). |
| c) | Las que resuelvan **litigios entre Administraciones públicas**. |
| d) | Las que resuelvan **impugnaciones indirectas de disposiciones generales**. |
| e) | ⚠️ **Las que, con independencia de la cuantía, sean susceptibles de EXTENSIÓN DE EFECTOS.** |

> **La letra e) es nueva: la añadió el RD-ley 6/2023 y está en vigor desde el 20-3-2024.** Muchos
> repertorios, formularios y hábitos de despacho **no la conocen**. Es una **puerta de entrada a la
> apelación en asuntos de cuantía baja**: si la sentencia es susceptible de extensión de efectos
> (arts. 110-111 LJCA: materia **tributaria**, de **personal** al servicio de las AAPP y de **unidad de
> mercado**), **es apelable aunque la cuantía sea inferior a 30.000 €**. **Comprobarlo siempre** antes
> de dar por inapelable una sentencia de cuantía baja en esas materias. Ver `ejecucion-sentencias-ca`.

### 1.3 ¿Es apelable el AUTO? (art. 80, verificado)

Son apelables **en un solo efecto** los autos de los Juzgados dictados en procesos de primera
instancia en estos casos:

a) Los que **pongan término a la pieza separada de medidas cautelares**.
b) Los recaídos **en ejecución de sentencia**.
c) Los que **declaren la inadmisión** del recurso o **hagan imposible su continuación**.
d) Los recaídos sobre las **autorizaciones** de los arts. **8.6**, **9.2** y **122 bis**.
e) Los recaídos en aplicación de los **arts. 83 y 84**.

- **Art. 80.2:** la apelación de los autos dictados en los supuestos de los **arts. 110 y 111**
  (extensión de efectos) se rige por **el mismo régimen de admisión que corresponda a la sentencia cuya
  extensión se pretende**.
- **Art. 80.3:** se tramitan conforme a la sección 2.ª del capítulo (es decir, por el art. 85).
- ⚠️ **Recordar:** el auto del **art. 135.1.a)** LJCA (cautelarísima adoptada o denegada inaudita parte)
  **no es recurrible**; sí lo es el auto posterior que resuelve sobre levantamiento, mantenimiento o
  modificación de la medida.

### 1.4 Plazo, legitimación y control final

- **Plazo: 15 días** desde la notificación, **ante el Juzgado a quo** (art. 85.1, verificado).
  Transcurrido sin interponerse, el LAJ **declara la firmeza** de la sentencia.
- **Caducidad**: no se interrumpe por nada. Aplicar el margen de seguridad de la casa.
- **Agosto NO corre** (art. 128.2) — **salvo** que la sentencia se haya dictado en el procedimiento de
  **derechos fundamentales**, donde **agosto es hábil**. ⚠️ Comprobar el cauce antes de computar.
- **Legitimación:** haber sido parte y que la sentencia sea **desfavorable** (gravamen). Sin gravamen no
  hay apelación, aunque no guste la motivación.
- **Representación:** ante la Sala (órgano **colegiado**) el **procurador es preceptivo** (art. 23.2
  LJCA). Preverlo desde la interposición ante el Juzgado.
- **Si se deniega la admisión** por auto del Juzgado: cabe **recurso de queja**, sustanciado conforme a
  la LEC (art. 85.2).

---

## 2. ⚠️ El escrito de interposición YA contiene las alegaciones — no es un anuncio

Art. 85.1 (verificado): el recurso se interpone **mediante escrito razonado que deberá contener las
alegaciones en que se fundamente el recurso**.

- **No hay fase de "preparación" + "interposición"** como en otros regímenes. **Un escrito, y va
  completo.** Un escrito de mero anuncio es un recurso perdido: no hay segunda oportunidad para
  argumentar.
- Este es el error de importación más frecuente (se traslada el esquema de la casación o el hábito de
  regímenes derogados). **Calendar 15 días para redactar un escrito completo, no para anunciar.**

## 3. Tramitación posterior (art. 85, verificado)

| Trámite | Regla |
|---|---|
| Admisión | El LAJ admite por resolución **no recurrible**; si no cumple requisitos o la sentencia no es apelable, lo pone en conocimiento del Juez, que puede denegar por auto → **queja** (art. 85.2). |
| **Oposición** | Traslado a las demás partes: **15 días** comunes para formalizar oposición (art. 85.2). |
| **Prueba** | En los escritos de interposición y de oposición cabe pedir **recibimiento a prueba**, solo para practicar las **denegadas** o **no practicadas debidamente** en primera instancia **por causas no imputables** a la parte (art. 85.3). Es un cauce estrecho: justificar los dos requisitos. |
| **⚠️ Impugnación de la sentencia por el apelado** | Art. 85.4 (redacción **RD-ley 6/2023, en vigor 20-3-2024**): en el escrito de oposición, el apelado puede **impugnar la sentencia apelada en lo que le resulte desfavorable**, razonando los puntos en que le perjudica; se da traslado al apelante por **10 días** al solo efecto de oponerse a la impugnación. También puede alegar la **admisión indebida** de la apelación (vista al apelante por **5 días**). |
| Elevación | El Juzgado eleva autos y expediente y emplaza a las partes por **30 días** ante la Sala (art. 85.5). |
| Vista/conclusiones | Las partes pueden pedir **vista**, **conclusiones** o que el pleito se declare concluso (art. 85.7-8). |
| Sentencia | **10 días** desde que el pleito queda concluso (art. 85.9). |
| **Art. 85.10** ⚠️ | Si la Sala **revoca en apelación** una sentencia que declaró la **inadmisibilidad**, **resuelve al mismo tiempo sobre el fondo**. Consecuencia práctica: **contra una sentencia de inadmisión hay que apelar también el fondo, subsidiariamente y desarrollado** — si no, la Sala revocará la inadmisión y resolverá el fondo sin argumentos del apelante. Es un error caro y silencioso. |

> **Terminología:** el RD-ley 6/2023 sustituyó la **«adhesión a la apelación»** por la **«impugnación de
> la sentencia apelada en lo que le resulte desfavorable»**. Usar la terminología vigente; «adhesión»
> delata escrito desactualizado.

## 4. Motivos — cómo se construyen

La apelación es de **plena jurisdicción**: la Sala puede revisar hechos y Derecho. Pero se gana con
motivos **numerados, autónomos y ordenados por fuerza**, no con una relectura de la demanda.

- **Regla de oro:** el escrito de apelación **no es la demanda otra vez**. Se dirige **contra la
  sentencia**: hay que identificar el **fundamento jurídico concreto** que se combate, citarlo, y
  explicar **por qué yerra**. Copiar la demanda es la forma más común de perder la apelación.
- **Motivos habituales:**
  - **Error en la valoración de la prueba**: identificar el documento o pericial concreto (con folio) y
    demostrar que la conclusión es **ilógica o arbitraria**, no solo que cabía otra lectura.
  - **Infracción de normas sustantivas** del ordenamiento aplicable al fondo.
  - **Infracción de normas procesales con indefensión** (art. 24 CE): acreditar que se pidió la
    subsanación en la instancia si hubo momento oportuno. ⚠️ **Anotarlo también aquí**: si el asunto
    puede acabar en casación, esa acreditación será **requisito del art. 89.2.c) LJCA** — dejarla hecha
    y documentada ya.
  - **Incongruencia** (omisiva, extra petita, ultra petita) y **falta de motivación**.
  - **Inadmisión indebida**: **pro actione** y tutela judicial efectiva (art. 24.1 CE); recordar el
    art. 85.10 → desarrollar **siempre** el fondo subsidiariamente.
  - **Desviación de poder**; **nulidad** (art. 47 Ley 39/2015) o **anulabilidad** (art. 48 Ley 39/2015).
- **Jurisprudencia:** verificar **cada** cita (STS, STC, TSJ) con `buscar_sentencias` /
  `buscar_por_cita` **antes** de incluirla. **Prohibido** citar ECLI/ROJ/fecha/ponente de memoria.

## 5. Costas ⚠️ — art. 139 (verificado, redacción RD-ley 6/2023)

- **En recursos (art. 139.2):** se imponen **al recurrente si se desestima TOTALMENTE** el recurso,
  **salvo** que el órgano, **razonándolo debidamente**, aprecie circunstancias que justifiquen su no
  imposición. ⚠️ **Totalmente**: la estimación parcial, aunque sea mínima, evita la condena.
  **Consecuencia táctica:** un motivo subsidiario sólido y acotado no solo puede ganar algo — puede
  **evitar la condena en costas**.
- **⚠️ TOPE del art. 139.4 (en vigor 20-3-2024) — nadie lo invoca y conviene invocarlo:** en **primera o
  única instancia**, la parte condenada en costas **no pagará más de UN TERCIO de la cuantía del
  proceso por cada uno de los favorecidos** por la condena. A **esos solos efectos**, las pretensiones
  de **cuantía indeterminada** se valoran en **18.000 €**, salvo que el tribunal, **por razón de la
  complejidad del asunto**, disponga razonadamente otra cosa.
  - **En los recursos**, y sin perjuicio de lo anterior, la imposición **puede ser total, parcial o
    hasta una cifra máxima** (art. 139.4, párrafo 2.º).
  - **Uso práctico:** invocar el tope **en el propio escrito**, por otrosí, y **de nuevo** en la
    tasación de costas. Sirve tanto para limitar la condena propia como para calibrar la ajena.
- **Nunca** se imponen al **Ministerio Fiscal** (art. 139.6).
- Exacción frente a particulares: **vía de apremio** (art. 139.5). Tasación conforme a la **LEC**
  (art. 139.7).
- **Deber de información al cliente:** cuantificar el riesgo **antes** de apelar, con el tope del
  art. 139.4 aplicado a la cuantía real del asunto. Dejarlo por escrito.

## 6. Errores típicos que pierden el asunto

1. **Dar por inapelable una sentencia de cuantía ≤ 30.000 € sin comprobar el art. 81.2** — en especial
   la **letra e)** (extensión de efectos), vigente desde el 20-3-2024.
2. **Presentar un escrito de anuncio** sin alegaciones (art. 85.1). Recurso perdido.
3. **Presentarlo ante la Sala** en vez de ante el **Juzgado a quo**.
4. **Copiar la demanda** en lugar de atacar los fundamentos de la sentencia.
5. **Apelar solo la inadmisión** sin desarrollar el fondo subsidiariamente → art. 85.10.
6. **Aplicar la inhabilidad de agosto a una sentencia de DDFF** (allí agosto es hábil, art. 128.2).
7. **Olvidar el procurador** ante la Sala (art. 23.2) y perder días en subsanar.
8. **Pedir prueba en apelación** sin justificar que fue denegada o mal practicada por causa no
   imputable (art. 85.3).
9. **Usar «adhesión a la apelación»** (terminología derogada) en vez de la **impugnación** del art. 85.4.
10. **No advertir al cliente del riesgo de costas** ni invocar el **tope del art. 139.4**.
11. **Apelar sin gravamen** (sentencia estimatoria cuya motivación no gusta).
12. **Citar jurisprudencia no verificada.**

## 7. Anclaje al expediente administrativo y a los autos

- **Todo hecho afirmado va con folio.** Doble anclaje en apelación:
  `(doc. núm. X del expediente administrativo, folio Y)` y `(folio Z de los autos)`.
- Al combatir la valoración de la prueba, **citar el fundamento jurídico de la sentencia por su número**
  y **el documento por su folio**. Sin esos dos datos, el motivo es retórica.
- Si la sentencia da por probado algo que **no consta en el expediente**, decirlo así y señalar el vacío.

## 8. Estructura del escrito

1. **Encabezamiento:** «AL JUZGADO DE LO CONTENCIOSO-ADMINISTRATIVO NÚM. [X] DE [SEDE]» — se presenta
   **ante el a quo** —, con indicación de la Sala **ad quem**; procurador y letrado; autos y P.O./P.A.
2. **Identificación de la sentencia/auto** apelado: fecha, fallo y **fecha de notificación** (para
   acreditar el plazo de 15 días).
3. **Justificación de la apelabilidad**: art. 81.1, o el apartado del **art. 81.2** que abre la puerta
   —**con mención expresa de la letra e) si es el caso**—, o el **art. 80** si es un auto. Cuantía.
4. **ANTECEDENTES** sucintos.
5. **ALEGACIONES / MOTIVOS**, numerados, cada uno con: fundamento de la sentencia que se combate →
   norma o jurisprudencia infringida → razonamiento → efecto sobre el fallo.
6. **SUPLICO.**
7. **OTROSÍES:** recibimiento a prueba (art. 85.3); vista o conclusiones (art. 85.7); **tope de costas
   del art. 139.4**; designación electrónica.

## 9. SUPLICO — modelo (art. 31 LJCA)

> **SUPLICO AL JUZGADO** que, teniendo por presentado este escrito, se sirva admitirlo, tener por
> **interpuesto recurso de apelación** contra la sentencia núm. [X], de [FECHA], y, previos los
> trámites del art. 85 LJCA, elevar los autos a la **Sala de lo Contencioso-administrativo del
> [TSJ DE [CCAA] / AUDIENCIA NACIONAL]**, para que dicte sentencia por la que, **estimando el recurso,
> revoque** la apelada y, en su lugar:
>
> **1.º Declare** no conforme a Derecho y **anule** [ACTO] de [ÓRGANO], de [FECHA] (art. 31.1 LJCA).
> **2.º Reconozca la situación jurídica individualizada** de [CLIENTE] consistente en [SITUACIÓN] y
> acuerde las medidas para su **pleno restablecimiento**, entre ellas [MEDIDA] (art. 31.2 LJCA).
> **3.º Condene** a [ÓRGANO] a **indemnizar** en [IMPORTE] [o conforme a las bases que se fijen para
> ejecución de sentencia] (art. 31.2 LJCA).
> **4.º** Con **imposición de costas** de ambas instancias a la Administración demandada.
>
> **[Si se apela una inadmisión — SIEMPRE:]** **subsidiariamente** y para el caso de que se revoque la
> declaración de inadmisibilidad, que, conforme al **art. 85.10 LJCA**, **resuelva sobre el fondo** en
> los términos interesados en los apartados 1.º a 3.º.
>
> **OTROSÍ DIGO** que, para el caso de imposición de costas a esta parte, **SUPLICO** se haga constar
> el **límite del art. 139.4 LJCA** (un tercio de la cuantía del proceso por cada favorecido; [y, siendo
> la cuantía indeterminada, valoración en 18.000 € a estos solos efectos]).

- **Congruencia:** el suplico de apelación debe pedir **revocación + lo que debió acordar la instancia**.
  Pedir solo «revoque» deja a la Sala sin pretensión que estimar.
- Ajustar siempre al **art. 31 LJCA**: anulación + reconocimiento de situación jurídica individualizada
  + indemnización **cuando proceda**. Omitir el punto 2.º convierte una victoria en una anulación estéril.

## 10. Reglas de la casa

- **Protección de datos:** cero datos reales. Marcadores `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`,
  `[IMPORTE]`, `[TERCERO]`.
- **Jurisprudencia:** verificar con `buscar_sentencias` / `buscar_por_cita` antes de citar. Sin
  verificación → `[verificar]` y decirlo. Prohibido inventar ECLI/ROJ/ponente.
- **Normativa autonómica y local:** el conector no la cubre. Pedírsela al usuario; no citarla de memoria.
- **Nada de MASC:** requisito del orden civil; no existe aquí.
- **Entregable:** Word `.docx` maquetado (skill `docx`).
