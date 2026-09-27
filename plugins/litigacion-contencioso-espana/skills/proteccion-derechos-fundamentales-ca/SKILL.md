---
name: proteccion-derechos-fundamentales-ca
description: Redacta escritos del procedimiento especial para la protección de los derechos fundamentales de la persona (arts. 114-122 LJCA), el amparo judicial preferente y sumario del art. 53.2 CE. Activar con "protección de derechos fundamentales", "procedimiento preferente y sumario", "amparo judicial", "art. 114 LJCA", "me han vulnerado un derecho fundamental", "recurso de 10 días derechos fundamentales".
---

# Protección de derechos fundamentales (arts. 114-122 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo de 10 días, agosto hábil y trámites** → `buscar_articulo` (`ley="LJCA"`, artículos 114 a 122 y 128).
- **Contenido del derecho fundamental invocado** → `buscar_sentencias` (`base="TC"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la facultad concreta vulnerada).
- **Puente causal del art. 121.2 e inadecuación del procedimiento** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Derechos con dimensión europea** (extranjería, protección de datos, igualdad) → `buscar_sentencias` (`base="TJUE"`).
- **Antes de presentar** → `verificar_escrito` sobre el escrito de interposición.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

Amparo judicial ordinario del art. 53.2 CE en vía contencioso-administrativa. Plazos y cifras:
`references/anclas-normativas-ca.md`. Lo que no esté allí, verificarlo con `buscar_articulo` o
marcarlo `[verificar]`.

> # ⚠️ AGOSTO ES HÁBIL AQUÍ — Y SOLO AQUÍ
>
> Art. 128.2 LJCA (texto verificado): «Durante el mes de agosto no correrá el plazo para interponer el
> recurso contencioso-administrativo ni ningún otro plazo de los previstos en esta Ley **salvo para el
> procedimiento para la protección de los derechos fundamentales en el que el mes de agosto tendrá
> carácter de hábil**.»
>
> **La regla está INVERTIDA respecto del resto del plugin.** En todo lo demás agosto no corre; aquí sí.
> El plazo de **10 días** del art. 115.1 **corre en agosto**, sábados y domingos aparte.
>
> **Es la trampa clásica del orden contencioso y la causa evitable número uno de caducidad.**
> Si el asunto entra en despacho en julio o agosto: **calcular el plazo contando agosto**, avisar al
> cliente por escrito y no aplicar por inercia el criterio general. Nunca trasladar aquí el hábito
> civil ni el del resto de la LJCA.

---

## 1. Bloque de admisibilidad — cerrar ANTES de redactar

1. **¿Hay derecho fundamental susceptible de amparo?** Conforme al **art. 53.2 CE** (verificado), el
   procedimiento preferente y sumario ante los Tribunales ordinarios cubre el **art. 14** y la
   **Sección 1.ª del Capítulo II del Título I** (arts. 15 a 29). ⚠️ La **objeción de conciencia del
   art. 30** la refiere el art. 53.2 CE expresamente al **recurso de amparo ante el TC** («este último
   recurso»); si el asunto es de objeción de conciencia, **verificar el cauce** antes de encajarlo aquí.
   Quedan **fuera** los derechos del capítulo III y los principios rectores. El art. 24 CE ampara
   garantías del procedimiento **administrativo sancionador** (por proyección), pero **no** convierte
   en iusfundamental cualquier defecto formal.
2. **⚠️ El filtro real: ¿es una vulneración iusfundamental o una ilegalidad ordinaria disfrazada?**
   Es el motivo dominante de inadmisión o de desestimación. Si lo que hay es una infracción de
   legalidad ordinaria (mala motivación, error de cálculo, incompetencia), **este cauce no sirve**:
   el juez lo dirá y se habrá perdido el asunto **y** el plazo del procedimiento ordinario.
   **Decírselo al usuario con franqueza y valorar el cauce ordinario del art. 25 LJCA.**
3. **¿Plazo?** **10 días** (art. 115.1). Cómputo verificado, según el caso, desde el día siguiente a:
   - la **notificación del acto**;
   - la **publicación** de la disposición impugnada;
   - el **requerimiento para el cese** de la vía de hecho;
   - el **transcurso del plazo** fijado para la resolución.

   ⚠️ **Regla especial de dies a quo (art. 115.1, verificado):** cuando la lesión tenga su origen en
   **inactividad administrativa**, o se hubiera interpuesto **potestativamente un recurso
   administrativo**, o, en **vía de hecho**, **no se hubiera formulado requerimiento**, el plazo de
   10 días **se inicia transcurridos 20 días** desde la reclamación, la presentación del recurso o el
   inicio de la actuación en vía de hecho, respectivamente. **No confundir**: son 20 + 10, no 10.
4. **¿Caducidad?** Como todo plazo de interposición contencioso, es de **caducidad**. No lo interrumpe
   burofax, reclamación ni requerimiento extrajudicial.
5. **¿Legitimación?** Titular del derecho fundamental invocado. Comprobar art. 45.2 LJCA — en especial
   la letra d) para **personas jurídicas** (acuerdo corporativo para entablar acciones): es la causa de
   inadmisión más frecuente y evitable, y **también se aplica aquí**. Subsanación: 10 días (art. 45.3).
6. **¿Se agotó la vía administrativa?** El recurso administrativo aquí es **potestativo**; si se
   interpuso, opera la regla de los 20 + 10 días. **Nunca exigir MASC**: es del orden civil.
7. **¿Conviene la cautelar?** Casi siempre. Ver § 4.

## 2. Marco y tramitación (verificado)

| Norma | Regla |
|---|---|
| **Art. 114.1** | El procedimiento se rige por este capítulo y, en lo no previsto, por las **normas generales** de la LJCA. |
| **Art. 114.2** | Caben las pretensiones de los **arts. 31 y 32** LJCA, **siempre que tengan como finalidad restablecer o preservar** los derechos por razón de los cuales se formuló el recurso. ⚠️ Es el límite del suplico: ver § 6. |
| **Art. 114.3** | Tramitación **preferente** a todos los efectos. |
| **Art. 115.2** | En el escrito de interposición se expresará **con precisión y claridad** el derecho o derechos cuya tutela se pretende y, **de manera concisa**, los argumentos sustanciales del recurso. ⚠️ No es un escrito de mero anuncio: ver § 5. |
| **Art. 116.1** | El LAJ requiere con carácter urgente el **expediente electrónico** el mismo día de la presentación o el siguiente; la Administración lo remite en **5 días** (apercibimiento del art. 48). |
| **Art. 116.2** | Al remitirlo, la Administración emplaza a los interesados para comparecer como demandados en **5 días**. |
| **Art. 116.3** | La Administración y los demás demandados pueden **solicitar razonadamente la inadmisión** y la comparecencia del art. 117.2. |
| **Art. 116.4-5** | La falta de envío del expediente **no suspende** el curso de los autos; si llega tarde, se entrega a las partes por **48 horas** para alegaciones, sin alterar el curso. |
| **Art. 117** | Trámite de admisión: si el LAJ estima que no procede la admisión, da cuenta al Tribunal; **comparecencia** de partes y **Ministerio Fiscal** antes de **5 días**; auto al día siguiente mandando proseguir o inadmitiendo **por inadecuación del procedimiento**. |
| **Art. 121.1** | Sentencia en **5 días** desde que las actuaciones quedan conclusas. |
| **Art. 121.2** | Se estima el recurso cuando el acto, actuación o disposición incurra en **cualquier infracción del ordenamiento jurídico, incluso desviación de poder**, **y como consecuencia de ella vulnere un derecho de los susceptibles de amparo**. ⚠️ Doble requisito acumulativo — ver § 5. |
| **Art. 121.3** | Contra las sentencias de los **Juzgados** procede **siempre** la apelación, **en un solo efecto** (concuerda con el art. 81.2.b: apelables con independencia de la cuantía). |

> **Intervención del Ministerio Fiscal:** es parte en este procedimiento. Redactar sabiendo que el
> Fiscal leerá el escrito: la calidad del planteamiento iusfundamental determina su informe, y su
> informe pesa. Verificar el trámite concreto que corresponda con `buscar_articulo` antes de afirmarlo.

## 3. El art. 121.2 manda sobre la estrategia argumental

La sentencia estima **solo si concurren las dos cosas**: (i) infracción del ordenamiento y (ii) que
**de ella derive** la vulneración del derecho fundamental. Consecuencias prácticas:

- **No basta con probar la ilegalidad.** Hay que construir el **puente causal** hasta el derecho
  fundamental, de forma explícita y en un apartado propio. Un escrito que demuestra la ilegalidad y da
  por supuesta la lesión iusfundamental se desestima.
- **Tampoco basta con invocar el derecho fundamental** en abstracto. Identificar la **facultad concreta**
  del derecho que se ha impedido, y el acto que la impidió, con folio.
- **La desviación de poder** está expresamente admitida como infracción determinante (art. 121.2):
  útil cuando el acto es formalmente correcto pero persigue un fin distinto (p. ej., represalia por el
  ejercicio de un derecho). Exige prueba indiciaria sólida, no sospecha.

## 4. Medidas cautelares — casi siempre, y con habilitación de días

- Rigen los **arts. 129-136** (por remisión del art. 114.1 a las normas generales). Aplicar la skill
  `medidas-cautelares-ca`: eje en el **periculum** (art. 130.1), ponderación del **art. 130.2**, y
  **fumus restrictivo**.
- **Matiz propio:** en DDFF el periculum suele ser más fácil de acreditar, porque la consumación de la
  lesión iusfundamental es por naturaleza difícilmente reversible (manifestación no celebrada, reunión
  disuelta, expulsión ejecutada, información no obtenida a tiempo). **Explotarlo**: describir la
  irreversibilidad temporal.
- **Cautelarísima** del **art. 135** cuando la ejecución sea inminente y datable.
- **⚠️ Art. 128.3 (verificado)**, aplicable aquí de forma señalada: en casos de urgencia o cuando las
  circunstancias lo hagan necesario, las partes pueden pedir la **habilitación de días inhábiles** en
  el procedimiento de DDFF **o** en el incidente cautelar. El órgano **oye a las demás partes y
  resuelve por auto en 3 días**, y **acuerda en todo caso la habilitación cuando su denegación pudiera
  causar perjuicios irreversibles**. Pedirlo expresamente por otrosí cuando el calendario apriete.

## 5. Errores típicos que pierden el asunto

1. **⚠️ Aplicar la inhabilidad de agosto.** El plazo corre. Caducidad. Error irreparable.
2. **Contar 10 días cuando tocaban 20 + 10** (inactividad, recurso potestativo, vía de hecho sin
   requerimiento), o al revés — perder 20 días de margen por no leer el art. 115.1 entero.
3. **Usar este cauce para una ilegalidad ordinaria.** Inadmisión por inadecuación (art. 117.3) y, a esas
   alturas, plazo del ordinario probablemente caducado.
4. **Escrito de interposición vacío.** El art. 115.2 exige ya el derecho **con precisión y claridad** y
   los **argumentos sustanciales**. Un escrito de mero anuncio compromete el asunto desde el minuto uno
   y regala a la Administración la petición de inadmisión del art. 116.3.
5. **Invocar un derecho fuera de los arts. 14-29 y 30 CE** (típico: derechos del capítulo III, o el
   art. 33 CE — propiedad — que **no** es susceptible de amparo).
6. **No tender el puente causal del art. 121.2** entre la infracción y la lesión iusfundamental.
7. **Pedir en el suplico lo que excede del art. 114.2**: pretensiones que no tengan por finalidad
   restablecer o preservar el derecho. Ver § 6.
8. **Olvidar el art. 45.2.d)** en personas jurídicas (acuerdo corporativo) y morir en la subsanación.
9. **Descuidar el expediente tardío**: solo hay **48 horas** para alegar (art. 116.5) y no se suspende
   nada. Tener el escrito preparado.
10. **No pedir cautelar** en un asunto cuya lesión se consuma por el mero paso del tiempo.

## 6. Estructura del escrito y SUPLICO

**Estructura del escrito de interposición (art. 115.2):**

1. **Encabezamiento.** Órgano competente; procurador (preceptivo solo ante órganos colegiados,
   art. 23.2 LJCA) y letrado; mención expresa de que se interpone **por los trámites del procedimiento
   especial para la protección de los derechos fundamentales de la persona, arts. 114 y ss. LJCA**.
2. **Identificación del acto, disposición, inactividad o vía de hecho** y de su fecha de notificación,
   publicación, requerimiento o transcurso.
3. **Justificación del plazo**, con el cómputo explícito. **Si media agosto, hacer constar que se ha
   computado como hábil ex art. 128.2 LJCA** — demuestra dominio y evita el archivo por error del
   propio órgano.
4. **DERECHO FUNDAMENTAL INVOCADO**, con precisión y claridad (art. 115.2): artículo de la CE y
   **facultad concreta** vulnerada.
5. **ARGUMENTOS SUSTANCIALES**, de manera concisa: (i) infracción del ordenamiento; (ii) **puente
   causal** hasta la lesión iusfundamental (art. 121.2).
6. **Documentos** del art. 45.2 LJCA — en personas jurídicas, **el acuerdo corporativo de la letra d)**.
7. **SUPLICO.**
8. **OTROSÍES:** medida cautelar / cautelarísima (arts. 129-135); **habilitación de días inhábiles**
   (art. 128.3); designación electrónica.

**SUPLICO — modelo (ajustado al art. 31 LJCA y al límite del art. 114.2):**

> **SUPLICO AL JUZGADO/A LA SALA** que, teniendo por presentado este escrito, se sirva admitirlo, tener
> por **interpuesto recurso contencioso-administrativo por el procedimiento especial para la protección
> de los derechos fundamentales de la persona** (arts. 114 y ss. LJCA) contra **[ACTO / VÍA DE HECHO /
> INACTIVIDAD]** de **[ÓRGANO]**, de fecha **[FECHA]**, reclamar el expediente conforme al art. 116.1
> LJCA y, seguidos los trámites, dictar sentencia por la que:
>
> **1.º** Se **declare** que la actuación recurrida **no es conforme a Derecho** y que **vulnera el
> derecho fundamental a [DERECHO] (art. [X] CE)**, y se **anule** (art. 31.1 LJCA).
> **2.º** Se **reconozca la situación jurídica individualizada** de **[CLIENTE]** consistente en
> **[SITUACIÓN]** y se acuerden las medidas necesarias para su **pleno restablecimiento**, entre ellas
> **[MEDIDA]** (art. 31.2 LJCA).
> **3.º** Se **condene a [ÓRGANO] a indemnizar** los daños y perjuicios causados, en la cuantía de
> **[IMPORTE]** [o la que se determine en ejecución conforme a las bases que se fijen] (art. 31.2 LJCA).
> **4.º** Con **imposición de costas** a la Administración demandada (art. 139.1 LJCA).

- ⚠️ **Límite del art. 114.2:** las pretensiones de los arts. 31 y 32 solo caben **en cuanto tengan por
  finalidad restablecer o preservar el derecho fundamental**. La indemnización debe presentarse como
  **instrumento de restablecimiento** del derecho, no como pretensión resarcitoria autónoma. Si el
  grueso de lo pretendido es indemnizatorio y desconectado del derecho, **el cauce es el ordinario**
  (y, en su caso, `responsabilidad-patrimonial-ca`).
- **Costas:** rige el art. 139.1 (vencimiento objetivo, salvo serias dudas razonadas), con el **tope del
  art. 139.4**: máximo **un tercio de la cuantía del proceso por cada favorecido**; cuantía
  indeterminada = **18.000 €** a esos solos efectos, salvo que el tribunal razone otra cosa por
  complejidad. **Nunca** se imponen al **Ministerio Fiscal** (art. 139.6). Advertir al cliente del
  riesgo recíproco.

## 7. Anclaje al expediente administrativo

- **Todo hecho afirmado va con folio:** `(doc. núm. X del expediente, folio Y)`.
- El expediente llega en **5 días** (art. 116.1) y puede llegar tarde sin suspender nada (art. 116.4).
  Redactar la interposición con la documentación propia, identificada como anexo, y **reservar
  expresamente** la alegación complementaria a resultas del expediente.
- Si falta un documento decisivo en poder de la Administración, **decirlo y pedirlo**; el apercibimiento
  del **art. 48** respalda la petición.
- Preparar de antemano el escrito de **48 horas** del art. 116.5 por si el expediente llega tarde.

## 8. Reglas de la casa

- **Protección de datos:** cero datos reales. Marcadores `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`,
  `[IMPORTE]`, `[TERCERO]`. Si el asunto roza **categorías especiales del art. 9 RGPD** (salud,
  ideología, afiliación sindical, religión, orientación sexual, datos biométricos) —frecuente en
  DDFF—, **no reproducir el dato real**: construir con marcadores y describir la categoría.
- **Jurisprudencia:** prohibido citar ECLI/ROJ/fecha/ponente de memoria, **también la del TC**.
  Verificar con `buscar_sentencias` / `buscar_por_cita` antes de incluir cualquier cita. Sin
  verificación, `[verificar]` y decirlo.
- **Normativa autonómica y local:** el conector no la cubre. Pedírsela al usuario; no citarla de memoria.
- **Nada de MASC:** requisito del orden civil; no existe aquí.
- **Entregable:** Word `.docx` maquetado (skill `docx`).
