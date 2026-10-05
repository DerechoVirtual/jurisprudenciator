"""Mesa de trabajo de la redacción rápida: prepara la carpeta, ensambla las secciones y crea el Word.

Solo usa la biblioteca estándar de Python (funciona en Cowork, Claude Code, Windows, macOS y Linux).

  python escrito.py iniciar --tipo demanda --cliente garcia [--dir .]
      Crea <dir>/redaccion/<tipo>-<cliente>-<AAAAMMDD-HHMMSS>/ con secciones/ y fuentes/,
      apunta la hora de inicio e imprime las rutas en JSON.

  python escrito.py ensamblar <carpeta> [--salida ruta.docx] [--palabras N]
      Une secciones/*.md por orden de nombre, numera los rótulos, comprueba las citas contra
      fuentes/*.md, crea escrito.md, informe.md y el Word. Sale con código 2 si hay errores.

Marcas del texto de las secciones:
  # X              encabezamiento centrado en negrita (órgano)
  ## X             rótulo en negrita (HECHOS, FUNDAMENTOS DE DERECHO, SUPLICO...)
  ### X            subtítulo en negrita
  ### [HECHO] X    se numera solo: «PRIMERO.- X» (también FUNDAMENTO, MOTIVO, ALEGACION,
                   CLAUSULA, ESTIPULACION, OTROSI); la numeración es correlativa en todo el escrito
  > texto          cita literal sangrada en cursiva
  - texto          enumeración
  **texto**        negrita dentro del párrafo
  | a | b |        tabla con bordes
  %% izq | der     firmas en dos columnas sin bordes
  [[salto]]        salto de página
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

PALABRAS_POR_PAGINA = 380

ORDINALES_M = [
    "PRIMERO", "SEGUNDO", "TERCERO", "CUARTO", "QUINTO", "SEXTO", "SÉPTIMO", "OCTAVO", "NOVENO",
    "DÉCIMO", "UNDÉCIMO", "DUODÉCIMO", "DECIMOTERCERO", "DECIMOCUARTO", "DECIMOQUINTO",
    "DECIMOSEXTO", "DECIMOSÉPTIMO", "DECIMOCTAVO", "DECIMONOVENO", "VIGÉSIMO", "VIGÉSIMO PRIMERO",
    "VIGÉSIMO SEGUNDO", "VIGÉSIMO TERCERO", "VIGÉSIMO CUARTO", "VIGÉSIMO QUINTO", "VIGÉSIMO SEXTO",
    "VIGÉSIMO SÉPTIMO", "VIGÉSIMO OCTAVO", "VIGÉSIMO NOVENO", "TRIGÉSIMO", "TRIGÉSIMO PRIMERO",
    "TRIGÉSIMO SEGUNDO", "TRIGÉSIMO TERCERO", "TRIGÉSIMO CUARTO", "TRIGÉSIMO QUINTO",
    "TRIGÉSIMO SEXTO", "TRIGÉSIMO SÉPTIMO", "TRIGÉSIMO OCTAVO", "TRIGÉSIMO NOVENO", "CUADRAGÉSIMO",
]


def ordinal(n: int, femenino: bool) -> str:
    texto = ORDINALES_M[n - 1] if n <= len(ORDINALES_M) else f"{n}.º"
    if not femenino:
        return texto
    # PRIMERO -> PRIMERA, VIGÉSIMO PRIMERO -> VIGÉSIMA PRIMERA
    return " ".join(p[:-1] + "A" if p.endswith("O") else p for p in texto.split(" "))


# clase -> (femenino, plantilla)
CLASES = {
    "HECHO": (False, "{o}.- {t}"),
    "FUNDAMENTO": (False, "{o}.- {t}"),
    "MOTIVO": (False, "{o}.- {t}"),
    "ALEGACION": (True, "{o}.- {t}"),
    "CLAUSULA": (True, "{o}.- {t}"),
    "ESTIPULACION": (True, "{o}.- {t}"),
    "OTROSI": (False, "{o} OTROSÍ DIGO{t}"),
}

RE_ROTULO = re.compile(r"^###\s*\[(?P<clase>[A-ZÁÉÍÓÚ]+)\]\s*(?P<titulo>.*)$")
RE_ECLI = re.compile(r"ECLI:[A-Z]{2}:[A-Z0-9]+:\d{4}:[0-9A-Z.]+", re.I)
RE_ROJ = re.compile(r"\b(?:ROJ:?\s*)?((?:STS|ATS|SAN|AAN|STSJ|ATSJ|SAP|AAP|STC|ATC|SJ[A-Z]*|AJ[A-Z]*)\s+\d{1,6}/\d{4})\b")
RE_PENDIENTE = re.compile(r"\[(?:PENDIENTE|REVISAR|COMPLETAR|VERIFICAR)[^\]]*\]", re.I)
# Huecos de plantilla de las skills: [NOMBRE Y APELLIDOS], [NIE], [PROVINCIA]...
RE_HUECO = re.compile(r"\[(?!\[)[A-ZÁÉÍÓÚÜÑ][A-ZÁÉÍÓÚÜÑ0-9 ,./ºª()-]{1,60}\]")
RE_RESTO = re.compile(r"\{\{|\}\}|\[\[(?!salto\]\])|\bTODO\b|<ECLI>|\bj\d+\b(?=\])")


def sin_tildes(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")


def normalizar_roj(roj: str) -> str:
    return re.sub(r"\s+", " ", roj.upper()).strip()


# ---------------------------------------------------------------- iniciar

def iniciar(args: argparse.Namespace) -> int:
    ahora = dt.datetime.now()
    slug = "-".join(
        re.sub(r"[^a-z0-9]+", "-", sin_tildes(x).lower()).strip("-") or "x" for x in (args.tipo, args.cliente)
    )
    base = Path(args.dir).resolve() / "redaccion" / f"{slug}-{ahora:%Y%m%d-%H%M%S}"
    (base / "secciones").mkdir(parents=True, exist_ok=True)
    (base / "fuentes").mkdir(exist_ok=True)
    (base / "inicio.json").write_text(
        json.dumps({"inicio": ahora.isoformat(timespec="seconds"), "tipo": args.tipo, "cliente": args.cliente}),
        encoding="utf-8",
    )
    salida = Path(args.dir).resolve() / f"{slug}-{ahora:%Y%m%d}.docx"
    print(json.dumps({"carpeta": base.as_posix(), "caso": (base / "caso.md").as_posix(),
                      "secciones": (base / "secciones").as_posix(), "fuentes": (base / "fuentes").as_posix(),
                      "word": salida.as_posix()}, ensure_ascii=False, indent=1))
    return 0


# ---------------------------------------------------------------- fuentes

def leer_fuentes(carpeta: Path) -> list[dict]:
    fuentes = []
    for ruta in sorted((carpeta / "fuentes").glob("*.md")):
        for linea in ruta.read_text(encoding="utf-8", errors="replace").splitlines():
            linea = linea.strip()
            if not linea.startswith("- ") or "|" not in linea:
                continue
            campos = [c.strip() for c in linea[2:].split("|")]
            fuentes.append({"tipo": campos[0].upper(), "campos": campos[1:], "linea": linea[2:], "archivo": ruta.name})
    return fuentes


def ids_de_fuentes(fuentes: list[dict]) -> tuple[set[str], set[str]]:
    eclis, rojs = set(), set()
    for f in fuentes:
        texto = f["linea"]
        eclis.update(e.upper() for e in RE_ECLI.findall(texto))
        rojs.update(normalizar_roj(r) for r in RE_ROJ.findall(texto))
    return eclis, rojs


# ---------------------------------------------------------------- ensamblar

def numerar(lineas: list[str]) -> list[str]:
    contadores: dict[str, int] = {}
    salida = []
    for linea in lineas:
        m = RE_ROTULO.match(linea.strip())
        if m:
            clase = sin_tildes(m.group("clase")).upper()
            if clase in CLASES:
                femenino, plantilla = CLASES[clase]
                contadores[clase] = contadores.get(clase, 0) + 1
                titulo = m.group("titulo").strip()
                orden = ordinal(contadores[clase], femenino)
                if clase == "OTROSI":
                    titulo = (".- " + titulo) if titulo else ""
                    orden = re.sub(r"\b(PRIMER|TERCER)O\b", r"\1", orden)
                salida.append("### " + plantilla.format(o=orden, t=titulo).strip())
                continue
        salida.append(linea)
    return salida


def comprobar(texto: str, fuentes: list[dict]) -> tuple[list[str], list[str], list[str]]:
    errores, avisos = [], []
    eclis_ok, rojs_ok = ids_de_fuentes(fuentes)
    for ecli in sorted({e.upper() for e in RE_ECLI.findall(texto)}):
        if ecli.rstrip(".") not in {e.rstrip(".") for e in eclis_ok}:
            errores.append(f"{ecli} aparece en el escrito pero ningún subagente lo leyó con Jurisprudenciator")
    for roj in sorted({normalizar_roj(r) for r in RE_ROJ.findall(texto)}):
        if roj not in rojs_ok:
            errores.append(f"{roj} aparece en el escrito pero no está en las fuentes leídas")
    for resto in sorted(set(RE_RESTO.findall(texto))):
        errores.append(f"marca sin resolver en el texto: «{resto}»")
    pendientes = sorted(set(RE_PENDIENTE.findall(texto)) | set(RE_HUECO.findall(texto)))
    # Muletillas: el mismo arranque de párrafo repetido tres o más veces delata redacción automática.
    arranques: dict[str, int] = {}
    for parrafo in texto.split("\n"):
        palabras = re.findall(r"\w+", parrafo.lower())
        if len(palabras) > 12:
            clave = " ".join(palabras[:4])
            arranques[clave] = arranques.get(clave, 0) + 1
    for clave, veces in arranques.items():
        if veces >= 3:
            avisos.append(f"{veces} párrafos empiezan igual: «{clave}…»")
    for patron in ("trasladada esta doctrina", "proyectada esta doctrina", "a mayor abundamiento", "en definitiva"):
        veces = texto.lower().count(patron)
        if veces >= 3:
            avisos.append(f"«{patron}» se repite {veces} veces")
    return errores, avisos, pendientes


def ensamblar(args: argparse.Namespace) -> int:
    carpeta = Path(args.carpeta).resolve()
    secciones = sorted(p for p in (carpeta / "secciones").glob("*.md"))
    if not secciones:
        print(json.dumps({"ok": False, "errores": ["no hay secciones en " + str(carpeta / "secciones")]}, ensure_ascii=False))
        return 2
    errores = []
    partes = []
    for ruta in secciones:
        contenido = ruta.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").strip()
        if len(contenido.split()) < 15:
            errores.append(f"la sección {ruta.name} está vacía o incompleta")
        partes.append(contenido)
    texto = "\n".join(numerar("\n\n".join(partes).split("\n")))
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    fuentes = leer_fuentes(carpeta)
    e2, avisos, pendientes = comprobar(texto, fuentes)
    errores += e2

    (carpeta / "escrito.md").write_text(texto + "\n", encoding="utf-8")
    inicio = None
    try:
        inicio = dt.datetime.fromisoformat(json.loads((carpeta / "inicio.json").read_text(encoding="utf-8"))["inicio"])
    except (OSError, ValueError, KeyError):
        pass
    segundos = round((dt.datetime.now() - inicio).total_seconds()) if inicio else None
    palabras = len(re.findall(r"\w+", texto))
    if args.palabras and not 0.8 * args.palabras <= palabras <= 1.2 * args.palabras:
        avisos.append(f"el escrito tiene {palabras} palabras y el plan pedía {args.palabras} (±20 %)")

    salida = Path(args.salida).resolve() if args.salida else carpeta / "escrito.docx"
    if not args.sin_word:
        crear_docx(texto, salida)

    informe = ["# Informe de la redacción", ""]
    informe.append(f"- Secciones: {len(secciones)} · palabras: {palabras} · páginas aprox.: {max(1, round(palabras / PALABRAS_POR_PAGINA))}")
    if segundos is not None:
        informe.append(f"- Tiempo desde el inicio: {segundos // 60} min {segundos % 60:02d} s")
    informe.append(f"- Word: {salida.as_posix() if not args.sin_word else '(no generado)'}")
    informe += ["", "## Fuentes consultadas", ""]
    if fuentes:
        informe += ["| Tipo | Referencia | Sección |", "|---|---|---|"]
        for f in fuentes:
            informe.append(f"| {f['tipo']} | {' · '.join(c for c in f['campos'] if c)} | {f['archivo']} |")
    else:
        informe.append("(ningún subagente dejó fuentes)")
    for titulo, lista in (("Errores (corregir antes de entregar)", errores), ("Avisos de estilo", avisos),
                          ("Datos pendientes en el escrito", pendientes)):
        informe += ["", f"## {titulo}", ""] + ([f"- {x}" for x in lista] or ["- ninguno"])
    (carpeta / "informe.md").write_text("\n".join(informe) + "\n", encoding="utf-8")

    print(json.dumps({
        "ok": not errores, "word": None if args.sin_word else salida.as_posix(),
        "escrito": (carpeta / "escrito.md").as_posix(), "informe": (carpeta / "informe.md").as_posix(),
        "palabras": palabras, "paginas": max(1, round(palabras / PALABRAS_POR_PAGINA)), "segundos": segundos,
        "fuentes": len(fuentes), "errores": errores, "avisos": avisos, "pendientes": pendientes,
    }, ensure_ascii=False, indent=1))
    return 0 if not errores else 2


# ---------------------------------------------------------------- Word (OOXML a mano)

W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" ' \
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'


def runs(texto: str, negrita: bool = False, cursiva: bool = False) -> str:
    salida = []
    for i, trozo in enumerate(re.split(r"\*\*", texto)):
        if not trozo:
            continue
        props = ""
        if negrita or i % 2 == 1:
            props += "<w:b/>"
        if cursiva:
            props += "<w:i/>"
        rpr = f"<w:rPr>{props}</w:rPr>" if props else ""
        salida.append(f'<w:r>{rpr}<w:t xml:space="preserve">{escape(trozo)}</w:t></w:r>')
    return "".join(salida)


def parrafo(contenido: str, alineacion: str = "both", izq: int = 0, der: int = 0, sangria: int = 0,
            antes: int = 0, mantener: bool = False) -> str:
    ppr = f'<w:jc w:val="{alineacion}"/>'
    if izq or der or sangria:
        ppr += f'<w:ind w:left="{izq}" w:right="{der}" w:firstLine="{sangria}"/>'
    if antes:
        ppr += f'<w:spacing w:before="{antes}"/>'
    if mantener:
        ppr = "<w:keepNext/>" + ppr
    return f"<w:p><w:pPr>{ppr}</w:pPr>{contenido}</w:p>"


def tabla(filas: list[list[str]], bordes: bool, cabecera: bool) -> str:
    columnas = max(len(f) for f in filas)
    ancho = 9000 // columnas
    borde = "single" if bordes else "nil"
    tblpr = (f'<w:tblPr><w:tblW w:w="9000" w:type="dxa"/><w:tblBorders>'
             + "".join(f'<w:{b} w:val="{borde}" w:sz="4" w:space="0" w:color="000000"/>'
                       for b in ("top", "left", "bottom", "right", "insideH", "insideV"))
             + "</w:tblBorders></w:tblPr>")
    grid = "<w:tblGrid>" + "".join(f'<w:gridCol w:w="{ancho}"/>' for _ in range(columnas)) + "</w:tblGrid>"
    cuerpo = []
    for r, fila in enumerate(filas):
        celdas = []
        for c in range(columnas):
            texto = fila[c] if c < len(fila) else ""
            alin = "left" if bordes else "center"
            celdas.append(f'<w:tc><w:tcPr><w:tcW w:w="{ancho}" w:type="dxa"/></w:tcPr>'
                          + parrafo(runs(texto, negrita=cabecera and r == 0), alin) + "</w:tc>")
        cuerpo.append("<w:tr>" + "".join(celdas) + "</w:tr>")
    return f"<w:tbl>{tblpr}{grid}{''.join(cuerpo)}</w:tbl>" + parrafo("")


def cuerpo_docx(texto: str) -> str:
    lineas = texto.split("\n")
    bloques = []
    i = 0
    while i < len(lineas):
        linea = lineas[i].rstrip()
        i += 1
        if not linea.strip():
            continue
        if linea.strip() == "[[salto]]":
            bloques.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
            continue
        if linea.startswith("%%"):
            filas = [linea]
            while i < len(lineas) and lineas[i].startswith("%%"):
                filas.append(lineas[i])
                i += 1
            bloques.append(tabla([[c.strip() for c in f[2:].split("|")] for f in filas], bordes=False, cabecera=False))
            continue
        if linea.lstrip().startswith("|"):
            filas = [linea]
            while i < len(lineas) and lineas[i].lstrip().startswith("|"):
                filas.append(lineas[i])
                i += 1
            celdas = [[c.strip() for c in f.strip().strip("|").split("|")] for f in filas
                      if not re.fullmatch(r"[\s|:\-]+", f)]
            if celdas:
                bloques.append(tabla(celdas, bordes=True, cabecera=True))
            continue
        if linea.startswith("### "):
            bloques.append(parrafo(runs(linea[4:].strip(), negrita=True), "both", antes=120, mantener=True))
        elif linea.startswith("## "):
            bloques.append(parrafo(runs(linea[3:].strip(), negrita=True), "left", antes=240, mantener=True))
        elif linea.startswith("# "):
            bloques.append(parrafo(runs(linea[2:].strip(), negrita=True), "center", mantener=True))
        elif linea.startswith(">"):
            bloques.append(parrafo(runs(linea.lstrip("> ").strip(), cursiva=True), "both", izq=850, der=567))
        elif re.match(r"^\s*[-*] ", linea):
            bloques.append(parrafo(runs("– " + re.sub(r"^\s*[-*] ", "", linea).strip()), "both", izq=425))
        else:
            bloques.append(parrafo(runs(linea.strip()), "both"))
    return "".join(bloques)


def crear_docx(texto: str, salida: Path) -> None:
    documento = (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {W}><w:body>'
        + cuerpo_docx(texto)
        + '<w:sectPr><w:footerReference w:type="default" r:id="rIdPie"/>'
          '<w:pgSz w:w="11906" w:h="16838"/>'
          '<w:pgMar w:top="1701" w:right="1701" w:bottom="1701" w:left="1701" w:header="709" w:footer="709" w:gutter="0"/>'
          "</w:sectPr></w:body></w:document>"
    )
    estilos = (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles {W}>'
        "<w:docDefaults><w:rPrDefault><w:rPr>"
        '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>'
        '<w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="es-ES"/></w:rPr></w:rPrDefault>'
        '<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="360" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr></w:pPrDefault>'
        "</w:docDefaults>"
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>'
        "</w:styles>"
    )
    pie = (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr {W}>'
        '<w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
        '<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
        '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>1</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r>'
        "</w:p></w:ftr>"
    )
    tipos = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
        "</Types>"
    )
    rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
        "</Relationships>"
    )
    doc_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rIdEstilos" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        '<Relationship Id="rIdPie" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
        "</Relationships>"
    )
    ahora = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    core = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        "<dc:creator>Despacho</dc:creator>"
        f'<dcterms:created xsi:type="dcterms:W3CDTF">{ahora}</dcterms:created>'
        f'<dcterms:modified xsi:type="dcterms:W3CDTF">{ahora}</dcterms:modified>'
        "</cp:coreProperties>"
    )
    salida.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", tipos)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", documento)
        z.writestr("word/styles.xml", estilos)
        z.writestr("word/footer1.xml", pie)
        z.writestr("word/_rels/document.xml.rels", doc_rels)
        z.writestr("docProps/core.xml", core)


# ---------------------------------------------------------------- main

def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="orden", required=True)
    a = sub.add_parser("iniciar")
    a.add_argument("--tipo", required=True)
    a.add_argument("--cliente", required=True)
    a.add_argument("--dir", default=".")
    b = sub.add_parser("ensamblar")
    b.add_argument("carpeta")
    b.add_argument("--salida")
    b.add_argument("--sin-word", action="store_true")
    b.add_argument("--palabras", type=int, help="extensión total que pedía el plan, para avisar si se desvía")
    args = p.parse_args()
    return iniciar(args) if args.orden == "iniciar" else ensamblar(args)


if __name__ == "__main__":
    sys.exit(main())
