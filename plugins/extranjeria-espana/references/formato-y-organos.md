# Formato de los documentos y órganos de extranjería

Reglas comunes a todas las skills del plugin. Cada skill dice qué documento produce; aquí está
cómo se maqueta, a quién se dirige y cómo se cita.

## Contenido

1. Entrega
2. Maquetación del Word
3. A quién se dirige cada escrito
4. Cómo se cita
5. Datos del cliente
6. Plazos
7. Resumen para el abogado
8. Cuándo es imprescindible la jurisprudencia

## 1. Entrega

Todo documento para presentar o para el cliente se entrega en **Word (.docx)**, nunca solo en el
chat. Nombre del archivo: `<tipo>-<apellido-cliente>-<AAAAMMDD>.docx` (por ejemplo,
`recurso-reposicion-garcia-20260927.docx`). Si en el entorno no se pueden crear archivos, entrega el
texto completo maquetado con títulos y avisa de que hay que pasarlo a Word.

## 2. Maquetación del Word

- Times New Roman 12, A4 vertical, márgenes de 3 cm, texto justificado, interlineado 1,5.
- Encabezamiento en mayúsculas con el órgano de destino (apartado 3).
- Comparecencia con los datos del interesado y, si actúa abogado, la representación.
- Hechos numerados en ordinales (PRIMERO.-, SEGUNDO.-…) y fundamentos de derecho igual.
- Súplica («SOLICITA» ante la Administración; «SUPLICO» ante un órgano judicial), otrosíes si hacen falta, lugar, fecha y firma.
- Relación numerada de documentos que se acompañan al final.
- Prosa forense con forma propia en cada fundamento: premisa normativa, doctrina, hecho y
  conclusión, con conectores variados. Cada fundamento empieza y se ordena según lo que pida su
  argumento; dos fundamentos seguidos no repiten la misma secuencia de subtítulos.

## 3. A quién se dirige cada escrito

Comprueba la competencia con `buscar_articulo` antes de encabezar el escrito.

| Situación | Destinatario |
|---|---|
| Solicitudes y recursos de reposición contra resoluciones de las oficinas de extranjería | Oficina de Extranjería de la Subdelegación del Gobierno en la provincia; en las comunidades uniprovinciales y en la provincia sede de la Delegación, de la Delegación del Gobierno (compruébalo en la resolución o en la sede oficial) |
| Solicitudes y recursos de las autorizaciones de la Ley 14/2013, de 27 de septiembre (movilidad internacional) | Unidad de Grandes Empresas y Colectivos Estratégicos (comprueba en la sede oficial su denominación vigente) |
| Visados | Oficina consular que lo denegó |
| Nacionalidad por residencia | Ministerio competente en materia de Justicia (hoy de la Presidencia, Justicia y Relaciones con las Cortes), Dirección General de Seguridad Jurídica y Fe Pública; comprueba la denominación en resoluciones recientes |
| Protección internacional | Oficina de Asilo y Refugio del Ministerio del Interior |
| Recurso contencioso contra resoluciones de extranjería de la Administración periférica del Estado (art. 8.4 LJCA) | Tribunal de Instancia de [sede], Sección de lo Contencioso-Administrativo (LOPJ art. 84, tras la LO 1/2025) |
| Internamiento en CIE, control del centro, quejas y habeas corpus | Tribunal de Instancia de [sede], Sección de Instrucción o Sección Única (art. 88 de la Ley Orgánica del Poder Judicial); la apelación, a la Audiencia Provincial |
| Otros actos (ministeriales, consulares, asilo, nacionalidad) | Determina la Sala competente con `buscar_articulo` en la LJCA (arts. 8 a 13 y disposiciones concordantes) y con jurisprudencia reciente de competencia antes de encabezar |

Para confirmar el nombre exacto de la Sección en una sede concreta, busca sentencias recientes del TSJ
de esa comunidad sobre extranjería y lee el órgano de origen que indican; si no aparece, encabeza con
«Tribunal de Instancia de [sede], Sección de lo Contencioso-Administrativo» y avisa al abogado de que
lo compruebe.

En la oficina judicial, el funcionario que da fe es el **Letrado o Letrada de la Administración de
Justicia**.

## 4. Cómo se cita

- Artículos: con el texto vigente que devuelve `buscar_articulo` y su norma, nombrada de forma
  que `verificar_escrito` la reconozca:
  - Reglamento: «artículo 127 del Real Decreto 1155/2024» (la primera vez puede seguir «, de 19 de
    noviembre, por el que se aprueba el Reglamento de la Ley Orgánica 4/2000»). No escribas «del
    Reglamento de Extranjería» ni «del Reglamento aprobado por el Real Decreto…»: el verificador no
    lo identifica y da la cita por inexistente.
  - Ley de emprendedores: «Ley 14/2013, de 27 de septiembre, de apoyo a los emprendedores y su
    internacionalización» la primera vez y «Ley 14/2013, de 27 de septiembre» en **cada** mención
    posterior: sin la fecha, el verificador la confunde con otra Ley 14/2013.
  - Resto: «artículo 31.3 de la Ley Orgánica 4/2000», «artículo 22 del Código Civil», «artículo 3
    del Real Decreto 240/2007», «artículo 4 de la Ley 12/2009».
  - Apartados con letra: «la letra e) del artículo 127 del Real Decreto 1155/2024» o «artículo 127 del
    Real Decreto 1155/2024, letra e)». Con «artículo 127.e)» el verificador no reconoce la norma y
    atribuye la cita a la última que se nombró. Tampoco pongas un «(artículo 85.4)» suelto: nombra
    siempre la norma junto al artículo. En una enumeración («artículos 50, 51 o 52»), el verificador solo enlaza
    el último: nombra la norma con cada artículo o cítalos por separado.
  - Artículos «bis»: «apartado 3 del artículo 31 bis de la Ley Orgánica 4/2000» (con «31 bis.3» no enlaza).
  - LOPJ: «Ley Orgánica del Poder Judicial» (con «Ley Orgánica 6/1985» el verificador no la identifica).
    Evita «de la misma ley»: repite el nombre de la norma.
  - `verificar_escrito` no identifica los reglamentos ni las directivas de la Unión ni las ordenanzas
    municipales: atribuye su artículo a la norma española más cercana y puede darlo por existente, por
    no localizado o con «disonancia». Ignora su veredicto sobre esas normas y comprueba cada artículo con
    `buscar_articulo` (o `leer_ordenanza`).
- Si aun así `verificar_escrito` marca un artículo como no localizado, compruébalo con
  `buscar_articulo` y el valor de `ley` de las anclas: si lo devuelve, la cita es correcta y el aviso
  se debe a cómo está nombrada la norma; corrige el nombre en el escrito.
- Jurisprudencia: párrafo literal entre comillas, seguido de órgano, fecha, número y ECLI tal como
  los devolvió `leer_sentencias`. Cita fundamentos jurídicos (doctrina), nunca el relato de hechos
  ni los datos personales de las partes de aquel pleito.
- Antes de citar un párrafo de `leer_sentencias`, comprueba que es razonamiento de la Sala (fundamento
  jurídico): con `parrafos=3` salen a veces alegaciones de parte, votos particulares o transcripciones de
  preceptos. Si no lo es, afina `terminos` o elige otra resolución.
- La jurisprudencia se atribuye a Jurisprudenciator o a «la base oficial de jurisprudencia».
- Ningún escrito contiene un ECLI, un artículo o un plazo que no se haya obtenido en esta
  conversación con una herramienta de Jurisprudenciator.

## 5. Datos del cliente

- Usa marcadores para lo que no se ha facilitado: `[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`,
  `[DOMICILIO]`, `[FECHA DE ENTRADA EN ESPAÑA]`, `[NÚMERO DE EXPEDIENTE]`. Nunca inventes un dato.
- En las consultas a Jurisprudenciator busca por la cuestión jurídica, nunca por el nombre, el NIE
  o el pasaporte del cliente.

## 6. Plazos

- Calcula cada plazo con el precepto que devuelva `buscar_articulo` (LPAC para la vía
  administrativa, LJCA para la judicial, y la norma especial cuando la haya: protección
  internacional, expulsión preferente, nacionalidad).
- Indica siempre la fecha inicial (notificación o publicación), el precepto aplicado y la fecha
  final calculada. Si un plazo por horas vence en día inhábil, aplica el artículo 31.2 de la Ley 39/2015
  y da la hora límite estricta y la prorrogada; recomienda presentar antes de la más estricta. Si no consta la fecha de notificación, pídela; sin ella no se da un plazo.

## 7. Resumen para el abogado

Acompaña cada entrega con un resumen breve en el chat:

1. Qué se ha preparado y para qué órgano.
2. Plazo y fecha límite, con su precepto.
3. Documentos que faltan o riesgos detectados.
4. Tabla de jurisprudencia citada: ECLI · órgano · fecha · qué sostiene.
5. Próximo paso recomendado.

## 8. Cuándo es imprescindible la jurisprudencia

La puerta de cada skill se aplica siempre a `estado` y a los artículos: sin el texto vigente que
devuelva Jurisprudenciator no se redacta nada.

- **Recursos, demandas y escritos que discuten una interpretación**: la jurisprudencia es
  imprescindible. Si tras dos reformulaciones no hay ninguna resolución aplicable, la tarea se detiene.
- **Solicitudes, alegaciones y escritos urgentes** (frontera, CIE, requerimientos) que se sostienen en
  el texto de la norma: se busca doctrina y se cita si la hay; si no existe todavía (pasa con muchos
  preceptos del Real Decreto 1155/2024), se redacta sin ese fundamento y el resumen lo dice.

Cuando la única doctrina interpreta el Reglamento anterior (Real Decreto 557/2011), se cita solo si
el precepto no ha cambiado, diciendo qué reglamento aplicó la sentencia.

