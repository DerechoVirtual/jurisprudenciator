# Protección de datos y secreto profesional

> Política del plugin `litigacion-penal-espana`. Vinculante para todas las skills.
> Última auditoría: **2026-07-17**. Revisión de conectores: **2026-09-27** (el plugin solo incluye
> Jurisprudenciator; ya no trae gestor documental).

---

## 1. Por qué el penal es distinto

En litigación penal los datos que se manejan son, casi por definición, **los más sensibles que
existen en un despacho**:

- **Art. 10 RGPD — condenas e infracciones penales.** El tratamiento de datos relativos a
  **condenas e infracciones penales o medidas de seguridad conexas** solo puede hacerse bajo
  **supervisión de las autoridades públicas** o cuando lo autorice el **Derecho de la Unión o de los
  Estados miembros** que establezca garantías adecuadas. No es un dato más: tiene régimen propio,
  **distinto y adicional** al del art. 9 (categorías especiales).
- **Art. 10 LOPDGDD** (LO 3/2018) desarrolla ese régimen en España.
- La sola condición de **investigado** es lesiva por sí misma, aunque el asunto acabe en archivo o
  absolución. La **presunción de inocencia** (art. 24.2 CE) tiene una dimensión extraprocesal: una
  filtración causa un daño que ninguna sentencia absolutoria repara.
- Los expedientes penales contienen además, con frecuencia, **datos del art. 9 RGPD**: salud
  (informes forenses, psiquiátricos, adicciones), vida sexual (delitos contra la libertad sexual),
  origen étnico, y datos de **menores**.

**Conclusión operativa:** en este plugin la protección de datos no es un trámite de cumplimiento.
Es parte de la defensa del cliente.

---

## 2. Principio rector

**El plugin es una plantilla impersonal.** Todo lo que viaja en este repositorio —skills, perfil,
ejemplos, modelos de escrito— debe poder publicarse o entregarse a un tercero **sin revelar ningún
dato de ningún cliente, investigado, víctima, testigo o tercero**.

Los datos reales viven **fuera** del plugin:

```
~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/
├── CLAUDE.md          ← perfil real del despacho
└── matters/           ← asuntos reales
    └── <slug>/
```

> ⚠️ Ese directorio **no forma parte del plugin** y nunca debe copiarse dentro de él, ni añadirse a
> un repositorio compartido, ni adjuntarse a una entrega.

---

## 3. Resultado de la auditoría de 2026-07-17

Se auditaron los 35 archivos del plugin buscando identificadores personales:

| Categoría | Resultado |
|---|---|
| DNI / NIE / NIF / CIF | **0 hallazgos** |
| IBAN / datos bancarios | **0 hallazgos** |
| Correos electrónicos | **0 hallazgos** |
| Teléfonos | **0 hallazgos** |
| Direcciones postales | **0 hallazgos** |
| Nombres de clientes, investigados o víctimas reales | **0 hallazgos** |
| Antecedentes penales reales | **0 hallazgos** |
| Nº de diligencias, ejecutoria o atestado reales | **0 hallazgos** |

**Correcciones aplicadas en esta revisión:**

1. El `CLAUDE.md` del plugin se mantiene como **plantilla vacía** con marcadores, con advertencia
   explícita de no escribir en él datos reales.
2. Se eliminaron los **ejemplos con apariencia de cliente real** heredados del plugin civil (nombre
   de persona física y razón social de contraparte en el `_log.yaml` de ejemplo). Sustituidos por
   ejemplos **descritos por tipo delictivo**, sin nombres.
3. Se corrigió la **ruta de configuración**, que apuntaba al directorio de otro plugin
   (`litigacion-civil-espana-pro`). Además de ser un error funcional, **mezclaba una cartera de
   asuntos penales con una civil** en un mismo repositorio — con datos del art. 10 RGPD de por
   medio, es la peor colisión posible.
4. Se retiró de `plugin.json` y de `README.md` la afirmación de que las skills se basan en
   «plantillas reales del despacho, anonimizadas». Aunque el contenido esté despersonalizado, esa
   frase **documenta por escrito un tratamiento de datos penales de clientes** y no aporta nada al
   usuario.
5. Se añadió a todas las skills la advertencia del **art. 10 RGPD**.

---

## 4. Reglas que toda skill debe cumplir

1. **Marcadores, nunca datos.** `[INVESTIGADO]`, `[ACUSADO]`, `[PENADO]`, `[DETENIDO]`,
   `[VÍCTIMA]`, `[PERJUDICADO]`, `[TESTIGO]`, `[MENOR]`, `[DNI]`, `[DOMICILIO]`, `[ENTIDAD]`,
   `[CIF]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`, `[MATRÍCULA]`, `[COMISARÍA]`. Nunca un valor con
   forma de dato real.
2. **⚠️ Slugs sin nombre — regla reforzada en penal.** El identificador de un asunto se construye
   por **tipo delictivo**, no por apellido: `estafa-inversion-2026`, **nunca**
   `apellido-estafa-2026`. Un listado de carpetas que revele **quién está investigado** es una
   brecha de datos del art. 10 RGPD y un daño reputacional irreversible para el cliente.
3. **Datos de terceros de las actuaciones.** El sumario contiene datos de víctimas, testigos, otros
   investigados y denunciantes. **No reproducirlos** más allá de lo estrictamente necesario para la
   defensa. El acceso a las actuaciones se concede **para ejercer la defensa**, no para cualquier
   uso.
4. **Datos de salud y de vida sexual = art. 9 RGPD**, además del art. 10. Informes forenses,
   psiquiátricos, de adicciones y todo lo relativo a delitos contra la libertad sexual. Base
   jurídica: ejercicio del derecho de defensa (art. 9.2.f RGPD). Extraer solo los hitos con
   relevancia, con marcadores.
5. **⚠️ Menores.** Víctimas o investigados menores: cautela máxima. Nunca datos identificativos,
   ni siquiera indirectos (centro escolar, localidad pequeña, relación familiar).
6. **Secreto profesional.** Art. 542.3 LOPJ y Código Deontológico. En penal se refuerza con la
   **confidencialidad de las comunicaciones abogado-cliente** (arts. **118.4** y **520.7** LECrim) y
   con la **entrevista reservada con el detenido, incluso antes de su declaración**
   (art. **520.6.d** LECrim). El deber persiste tras el fin del encargo.
7. **No exfiltrar.** No subir atestados, sumarios, informes forenses ni historiales a servicios
   externos no cubiertos por el encargo y por un contrato de encargo de tratamiento (art. 28 RGPD).
   El plugin **no incluye gestor documental**: si el despacho guarda el expediente en OneDrive,
   Google Drive o Dropbox (o en una carpeta local sincronizada con alguno de ellos), ese servicio
   debe estar cubierto por su propio contrato de encargo de tratamiento.
8. **⚠️ Consultas de jurisprudencia despersonalizadas.** Al buscar en `jurisprudenciator`, describir
   el **problema jurídico**, nunca los identificadores del cliente. «Dolo antecedente en estafa por
   incumplimiento contractual», no el nombre del investigado. El conector consulta **fuentes
   públicas** (BOE, jurisprudencia oficial) y **no debe recibir datos personales del cliente**.
   Lo mismo vale para el Registro Mercantil, el Catastro o los edictos del BOE: se consulta por la
   sociedad, la referencia catastral, el órgano o el número de procedimiento, nunca por el nombre
   o el DNI de una persona física.
9. **Antecedentes penales.** Con la **LO 1/2026** (multirreincidencia), comprobar antecedentes es
   ahora imprescindible en hurtos y estafas. Esa comprobación **genera tratamiento del art. 10
   RGPD**: hacerla por los cauces legales (certificado del Registro Central de Penados a instancia
   del propio cliente o vía judicial), **nunca** por fuentes informales, y no conservarla más allá
   de lo necesario.

---

## 5. Marco normativo aplicable al despacho

- **RGPD** — Reglamento (UE) 2016/679: **art. 10** (condenas e infracciones penales), art. 9
  (categorías especiales), art. 6.1 (bases), art. 9.2.f (derecho de defensa), art. 28 (encargados).
- **LOPDGDD** — LO 3/2018, **art. 10**.
- **Art. 542.3 LOPJ** — secreto profesional del abogado.
- **Arts. 118.4 y 520.7 LECrim** — confidencialidad de las comunicaciones con el letrado.
- **Ley 4/2015** — Estatuto de la víctima del delito: derecho a la **protección de la intimidad** de
  la víctima.
- **Ley 10/2010** — prevención del blanqueo: identificación del cliente. Conservar la documentación
  identificativa **fuera** del plugin.
- **Art. 24.2 CE** — presunción de inocencia, también en su dimensión extraprocesal.

---

## 6. Antes de compartir o entregar el plugin

- [ ] `CLAUDE.md` de la raíz contiene solo `[PLACEHOLDER]` — ningún dato real.
- [ ] No existe carpeta `matters/` dentro del plugin.
- [ ] Ningún archivo contiene DNI, IBAN, teléfono, email, dirección ni antecedentes.
- [ ] Los ejemplos usan descriptores de tipo delictivo, no nombres de persona.
- [ ] Ningún slug de ejemplo permite identificar a un investigado.
- [ ] No hay atestados, sumarios ni documentos originales (`.docx`, `.pdf`) en el árbol del plugin.

Comprobación rápida (desde la raíz del plugin):

```bash
grep -rniE "[0-9]{8}[-]?[A-Za-z]|ES[0-9]{2}[ 0-9]{10,}|[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}" .
```

Cualquier hallazgo debe revisarse antes de compartir. Un resultado vacío es el estado esperado.
