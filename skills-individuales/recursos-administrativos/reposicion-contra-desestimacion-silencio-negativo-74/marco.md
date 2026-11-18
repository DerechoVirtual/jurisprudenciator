# Guía del tema · Recursos administrativos

Reglas y plazos vigentes comprobados en el BOE el 17-11-2026. Léela antes de redactar cualquier formulario de este plugin.

## Cuándo usarla

- Hay un acto o una desestimación por silencio y el usuario quiere **recurrirlo en vía administrativa**.
- Se quiere pedir la **nulidad de pleno derecho** de un acto firme (revisión de oficio) o la **rectificación de un error**.
- La Administración tiene que **tramitar o resolver** un recurso (traslado a interesados, informe, ampliación de plazo, propuesta, resolución).
- Multas de tráfico: `multas-trafico`. Extranjería: `extranjeria`. Recurso ante los tribunales: plugin contencioso.


## Primero, elegir la vía

1. ¿El acto **pone fin a la vía administrativa**? → reposición potestativa (o directamente contencioso). ¿No la pone? → alzada ante el superior.
2. ¿Es **firme** y se da alguna causa del art. 125.1? → recurso extraordinario de revisión.
3. ¿Hay causa de **nulidad del art. 47.1**? → revisión de oficio en cualquier momento (art. 106), además o en lugar del recurso.
4. ¿Solo hay un **error material, de hecho o aritmético**? → rectificación (art. 109.2), en cualquier momento.

Explica al usuario la vía elegida y el plazo.


## Marco vigente (comprobado en el BOE el 17-11-2026)

| Vía | Plazo para interponer | Plazo para resolver / efectos | Precepto |
|---|---|---|---|
| **Alzada** | **1 mes** si el acto es expreso. Si no lo es, **en cualquier momento** desde el día siguiente a que se produzca el silencio. | **3 meses**; si no se resuelve, desestimada (salvo alzada contra una desestimación por silencio: entonces se entiende **estimada**, art. 24.1). Contra la resolución de la alzada solo cabe el extraordinario de revisión. | Arts. 121-122 Ley 39/2015 |
| **Reposición** (potestativa) | **1 mes** si el acto es expreso; si no, en cualquier momento desde el acto presunto. Pasado el mes, solo contencioso (o revisión extraordinaria). | **1 mes**. No cabe reposición contra la resolución de una reposición. | Arts. 123-124 Ley 39/2015 |
| **Extraordinario de revisión** | Causa a) (error de hecho que resulta del expediente): **4 años** desde la notificación. Causas b), c) y d) (documentos esenciales, documentos o testimonios falsos, delito): **3 meses** desde que se conocen los documentos o es firme la sentencia. | Ante el mismo órgano que dictó el acto. | Arts. 125-126 Ley 39/2015 |
| **Revisión de oficio de actos nulos** | En cualquier momento, de oficio o a solicitud; actos que agotan la vía o no recurridos en plazo, por causas del art. 47.1. Dictamen favorable del Consejo de Estado u órgano autonómico. | Se puede inadmitir sin dictamen si no hay causa del 47.1 o carece de fundamento. De oficio: caduca a los **6 meses**; a solicitud: desestimada por silencio a los 6 meses. | Art. 106 Ley 39/2015 |
| **Lesividad** (actos favorables anulables) | La Administración la declara en **4 años** desde que se dictó el acto, con audiencia; luego lo impugna en el contencioso. | Caduca a los **6 meses** de iniciado. No es recurrible. En la Administración local la adopta el Pleno. | Art. 107 Ley 39/2015 |
| **Revocación** de actos de gravamen | Mientras no prescriba, si no es dispensa no permitida ni contraria a la igualdad, al interés público o al ordenamiento. | — | Art. 109.1 Ley 39/2015 |
| **Rectificación de errores** materiales, de hecho o aritméticos | En cualquier momento, de oficio o a instancia. | — | Art. 109.2 Ley 39/2015 |

Cómputo: art. 30 Ley 39/2015 (meses de fecha a fecha desde el día siguiente a la notificación; último día inhábil → primer hábil). Requisitos del escrito de recurso: art. 115; causas de nulidad y anulabilidad: arts. 47 y 48; suspensión de la ejecución: art. 117. Compruébalos con `buscar_articulo` antes de citarlos.


## Errores que la revisión ha encontrado

- Formularios de 2004-2008 que citaban la **Ley 30/1992**: si aparece como fundamento propio, cambia al artículo equivalente de la Ley 39/2015 (alzada 121-122, reposición 123-124, revisión 125-126, revisión de oficio 106, lesividad 107, revocación 109).
- Plazos antiguos de «tres meses» para recurrir actos presuntos: ya no existen; contra el silencio se recurre **en cualquier momento**.
- Las solicitudes de nulidad tienen un formulario por cada causa del art. 47.1: comprueba que la letra citada es la que corresponde a los hechos.
