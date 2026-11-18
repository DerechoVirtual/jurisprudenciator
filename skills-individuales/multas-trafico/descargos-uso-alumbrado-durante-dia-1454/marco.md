# Guía del tema · Multas y expedientes de tráfico

Reglas y plazos vigentes comprobados en el BOE el 17-11-2026. Léela antes de redactar cualquier formulario de este plugin.

## Cuándo usarla

- Hay una **denuncia o multa de tráfico** (DGT o ayuntamiento) y el usuario quiere alegar, pagar con reducción, identificar al conductor o recurrir.
- **Puntos**: pérdida de vigencia del permiso, saldo de puntos, cursos.
- **Notificaciones**: DEV, edictos, notificación defectuosa.
- La Administración **tramita** el expediente (boletín, incoación, notificaciones, propuesta, resolución).
- Si el asunto ya va al juzgado, usa además la skill `organo-y-postulacion` (plugin contencioso) para el encabezamiento: las multas van por **procedimiento abreviado**.


## Marco vigente (comprobado en el BOE el 17-11-2026)

| Trámite | Regla | TR LSV (RDLeg 6/2015) |
|---|---|---|
| Alegaciones / descargos | **20 días naturales** desde la notificación de la denuncia, para alegar y proponer prueba | 93.1 y 95.1 |
| Pago con reducción | En el acto o en **20 días naturales**: **50 %** de descuento. Supone renunciar a alegar, termina el procedimiento y deja abierto el contencioso desde el día siguiente | 94 |
| Identificar al conductor | El titular lo identifica con el nº de su permiso en **20 días naturales**. No hacerlo es muy grave (77.j) y la multa es el doble o el triple | 11 y 93.1 |
| Recurso | **Reposición potestativa en un mes** ante el mismo órgano. No suspende; desestimado si no se resuelve en un mes; agota la vía administrativa. Ya **no** hay alzada ante el Ministro (art. 17 RD 320/1994, inaplicable) | 96 |
| Informe del agente y prueba | Informe del agente en 15 días naturales si el instructor lo pide; la denegación de prueba se motiva | 95.2 |
| Prescripción de la infracción | **3 meses** las leves; **6 meses** las graves y muy graves, desde el día de los hechos; se interrumpe con actuaciones conocidas por el denunciado | 112.1-2 |
| Caducidad | **1 año** desde la iniciación | 112.3 |
| Prescripción de la sanción | Multas en 4 años; suspensión del permiso en 1 año | 112.4 |
| Multas | Leves hasta 100 €; graves 200 €; muy graves 500 €. Velocidad según el anexo IV. La graduación del art. 81 solo permite **subirlas hasta un 30 %** | 80 y 81 |
| Competencia | Jefe Provincial de Tráfico en interurbanas y travesías; Alcalde en vías urbanas | 84 |
| Notificación | En el acto; después solo en los supuestos del 89.2. Por DEV: 10 días naturales sin abrir = rechazada. Luego al domicilio y, en último término, BOE (TESTRA) | 89-92 |
| Pago de la sanción firme | 15 días **naturales**; después, apremio | 110.1 |
| Cancelación de antecedentes | 3 años | 113.4 |
| Puntos | 12 (8 noveles); recuperación total a los **2 años** sin sanción; curso para recuperar hasta 6 | 63-65 |

**RD 320/1994** (reglamento sancionador de tráfico): sigue formalmente vigente, pero solo en lo que no se oponga al TR LSV (art. 83.1 TR LSV). Sus plazos de 15 días, la alzada y la prescripción están superados. El art. 13 (rechazo motivado de la prueba) sigue siendo compatible.

**Reglamento General de Circulación renumerado** (cotejar en boe.es):
- **RD 465/2025** (en vigor desde el 1-7-2025) reescribe la señalización:

  | Antes | Ahora | Materia |
  |---|---|---|
  | 142 | 140 | Retirada, sustitución y alteración de señales |
  | 143 | 141 | Señales y órdenes de los agentes |
  | 144 | 142 | Balizamiento |
  | 145-148 | 143.1.a)-d) | Semáforos |
  | 151-155 | 145.2 | Señales de reglamentación |
  | 159-160 | 146.2 | Señales de indicación |
  | 167-171 | 147 | Marcas viales |
  | 173 | 150 | Señales en los vehículos |

- **RD 518/2026** (en vigor desde el 1-10-2026) añade un título de zonas urbanas en los **arts. 151-158**: los antiguos 151-155 designan hoy otras materias. Suprime el **art. 93** (ordenanzas de estacionamiento, hoy art. 156). El **art. 32** es ahora «carriles de emergencia»: las calzadas de tres o más carriles pasan al 31.2.
- La Ley 18/2021 derogó el **art. 51 RGC**: se acabó el margen de +20 km/h al adelantar.

**Ley 18/2021** (en vigor desde el 21-3-2022), lo que más pesa en los descargos:
- Móvil sujeto con la mano: grave. Llevar un detector de radar también es infracción (76.g).
- Cinturón, SRI o casco: 76.h.
- Tasa 0 de alcohol para los menores.
- Prioridad del peatón también en aceras.
- Adelantar a ciclistas dejando 1,5 m.
- Casco obligatorio en los VMP.
- Nuevas muy graves del 77.s)-x).

**Sin verificar**:
- La tabla de puntos del **anexo II** tras la Ley 18/2021. El conector no la devuelve: cotéjala en boe.es antes de afirmar cuántos puntos quita una infracción.
- El alcance del art. 77.v) respecto del art. 129 RGC.
