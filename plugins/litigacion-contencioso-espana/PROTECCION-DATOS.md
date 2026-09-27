# Protección de datos y secreto profesional

> Política del plugin `litigacion-contencioso-espana`. Vinculante para todas las skills.
> Última auditoría: **2026-07-17**.

---

## 1. Principio rector

**El plugin es una plantilla impersonal.** Todo lo que viaja en este repositorio —skills, perfil,
ejemplos, modelos de escrito— debe poder publicarse, compartirse o entregarse a un tercero **sin
revelar ningún dato personal de ningún cliente, contraparte, tercero o profesional**.

Los datos reales viven **fuera** del plugin, en el directorio de configuración local del usuario:

```
~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/
├── CLAUDE.md          ← perfil real del despacho
└── matters/           ← asuntos reales
    └── <slug>/
```

> ⚠️ Ese directorio **no forma parte del plugin** y nunca debe copiarse dentro de él, ni añadirse
> a un repositorio compartido, ni adjuntarse a una entrega.

---

## 2. Resultado de la auditoría de 2026-07-17

Se auditaron los 34 archivos del plugin buscando identificadores personales:

| Categoría | Resultado |
|---|---|
| DNI / NIE / NIF / CIF | **0 hallazgos** |
| IBAN / datos bancarios | **0 hallazgos** |
| Correos electrónicos | **0 hallazgos** |
| Teléfonos | **0 hallazgos** |
| Direcciones postales | **0 hallazgos** |
| Nombres de clientes o contrapartes reales | **0 hallazgos** |
| Números de colegiado reales | **0 hallazgos** |
| Nº de expediente, autos o acta reales | **0 hallazgos** |

**Correcciones aplicadas en esta revisión:**

1. El `CLAUDE.md` del plugin se mantiene como **plantilla vacía** con marcadores
   `[PLACEHOLDER]`/`[PENDIENTE]`, y se le ha añadido la advertencia explícita de no escribir en él
   datos reales.
2. Se eliminaron los **ejemplos con apariencia de cliente real** heredados del plugin civil
   (nombres de persona física, razón social de contraparte y procurador nominado en el
   `_log.yaml` de ejemplo). Sustituidos por ejemplos **descritos por materia**, sin nombres.
3. Se corrigió la **ruta de configuración**, que apuntaba al directorio de otro plugin
   (`litigacion-civil-espana-pro`). Además de ser un error funcional, mezclaba los asuntos de dos
   materias en un mismo repositorio de datos personales, contra el principio de **minimización**.
4. Se retiró de `plugin.json` y de `README.md` la afirmación de que las skills se basan en
   «plantillas reales del despacho, anonimizadas». Aunque el contenido esté efectivamente
   despersonalizado, esa frase **documenta un tratamiento de datos de clientes** y no aporta nada
   al usuario. El plugin se describe ahora por su contenido normativo.
5. Se añadió a las skills que manejan el expediente administrativo la advertencia sobre **datos de
   terceros** y **datos de salud**.

---

## 3. Reglas que toda skill debe cumplir

1. **Marcadores, nunca datos.** En ejemplos y modelos de escrito, usar siempre
   `[CLIENTE]`, `[DNI]`, `[DOMICILIO]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`, `[EXPEDIENTE]`,
   `[PROCURADOR]`, `[TERCERO]`, `[MATRÍCULA]`. Nunca un valor con forma de dato real.
2. **Slugs sin nombre.** El identificador de un asunto se construye por **materia**, no por
   apellido: `sancion-trafico-2026`, no `apellido-sancion-2026`. Un listado de carpetas no debe
   revelar la cartera de clientes.
3. **Datos de terceros del expediente.** El expediente administrativo contiene habitualmente datos
   de personas ajenas al cliente (denunciantes, otros interesados, testigos, funcionarios). **No
   reproducirlos** en escritos, resúmenes ni cronologías más allá de lo estrictamente necesario
   para la defensa. El acceso del interesado al expediente tiene límites (art. 13.d LPAC y RGPD).
4. **Datos de salud = categoría especial.** En responsabilidad patrimonial sanitaria, la historia
   clínica es **categoría especial del art. 9 RGPD**. Base jurídica del tratamiento: el ejercicio
   del derecho de defensa (art. 9.2.f RGPD). No reproducir historiales completos; extraer solo los
   hitos con relevancia causal, y hacerlo con marcadores.
5. **Minimización.** No pedir al cliente ni almacenar datos que el asunto no necesite.
6. **Secreto profesional.** Todo lo conocido por razón del encargo —incluido lo que resulte del
   expediente— está cubierto por el **art. 542.3 LOPJ** y por el Código Deontológico de la
   Abogacía. El deber persiste tras el fin del encargo.
7. **No exfiltrar.** No subir expedientes, historias clínicas ni documentación de asuntos a
   servicios externos que no estén cubiertos por el encargo y por un contrato de encargo de
   tratamiento (art. 28 RGPD). El conector del plugin (`jurisprudenciator`) consulta **fuentes
   públicas** (jurisprudencia oficial, BOE, Catastro, Registro Mercantil, doctrina administrativa) y
   **no debe recibir datos personales del cliente** en las consultas. El gestor documental que el
   despacho tenga conectado (carpeta local, OneDrive, Google Drive o Dropbox) se usa solo para los
   documentos del asunto y con el contrato de encargo de tratamiento que corresponda.
8. **Consultas de jurisprudencia despersonalizadas.** Al buscar en `jurisprudenciator`, describir
   el **problema jurídico**, nunca los identificadores del cliente. «Responsabilidad patrimonial
   por infección nosocomial», no el nombre del paciente ni el del hospital si es innecesario.

---

## 4. Marco normativo aplicable al despacho

- **RGPD** — Reglamento (UE) 2016/679. Bases del art. 6.1 (ejecución del contrato de encargo,
  obligación legal, interés legítimo) y del art. 9.2.f para categorías especiales (ejercicio del
  derecho de defensa).
- **LOPDGDD** — LO 3/2018, de 5 de diciembre.
- **Art. 542.3 LOPJ** — secreto profesional del abogado.
- **Ley 10/2010** — prevención del blanqueo (identificación del cliente): genera obligación de
  conservar documentación identificativa. Conservarla **fuera** del plugin.
- **Art. 13.d) LPAC** — derecho de acceso al expediente y sus límites.

---

## 5. Antes de compartir o entregar el plugin

Lista de comprobación:

- [ ] `CLAUDE.md` de la raíz contiene solo `[PLACEHOLDER]` — ningún dato real.
- [ ] No existe carpeta `matters/` dentro del plugin.
- [ ] Ningún archivo contiene DNI, IBAN, teléfono, email o dirección.
- [ ] Los ejemplos usan descriptores de materia, no nombres de persona.
- [ ] No hay documentos originales de clientes (`.docx`, `.pdf`) en el árbol del plugin.

Comprobación rápida (desde la raíz del plugin):

```bash
grep -rniE "[0-9]{8}[-]?[A-Za-z]|ES[0-9]{2}[ 0-9]{10,}|[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}" .
```

Cualquier hallazgo debe revisarse antes de compartir. Un resultado vacío es el estado esperado.
