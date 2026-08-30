#!/usr/bin/env python3
"""Biblioteca America — enriquece data/catalogo.csv con campos derivados.

Versión del repo en la última actualización de este script: v0.4.0

Añade, a partir de la ruta y el nombre de archivo (sin tocar el volumen
real ni depender de ningún escáner nuevo):

- `autor_carpeta`: primer segmento de ruta bajo AMERICANO/IBEROAMERICANO
  (convención real del usuario: una carpeta por autor/creador). "Varios"
  para los pocos archivos sueltos en la raíz de la región (antologías).
- `autores`: autor(es) extraídos del "(Fulano & Mengano)" final del
  nombre de archivo cuando existe (93% de los casos); si no hay match, se
  usa `autor_carpeta`. Varios autores separados por " & " o "," en el
  nombre quedan unidos con " ; " tal cual (no se intenta adivinar quién es
  guionista y quién dibujante: el orden en el nombre no es una convención
  fiable para eso — requeriría una base de datos externa, ver ROADMAP).
- `formato`: heurística por patrón en el nombre —
  `numero_suelto` (#NN), `recopilatorio_rango` (#NN-MM),
  `volumen` (Vol.N sin #) u `obra_completa` (ni # ni Vol.: one-shot,
  novela gráfica o recopilatorio integral).

No incluye editorial/sello ni año: no hay ninguna señal fiable de eso ni
en la ruta ni en el nombre de archivo para este dominio (a diferencia de
serie/autor); requeriría metadatos externos (ComicVine/GCD o similar),
fuera de alcance de este script.

Uso: python3 enriquecer_catalogo.py [ruta_catalogo.csv]
(por defecto data/catalogo.csv, se sobrescribe en el sitio)
"""

import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOGO_POR_DEFECTO = REPO_ROOT / "data" / "catalogo.csv"

RE_AUTORES_FINAL = re.compile(r"\(([^()]+)\)\.[A-Za-z0-9]+$")
RE_RANGO = re.compile(r"#\d+\s*-\s*\d+")
RE_ISSUE = re.compile(r"#\d+[a-zA-Z]?\b")
RE_VOL = re.compile(r"\bVol\.?\s*\d+", re.IGNORECASE)

CAMPOS_NUEVOS = ["autor_carpeta", "autores", "formato"]


def autor_carpeta_de(ruta: str, region: str) -> str:
    prefijo = f"/Volumes/AMERICA/{region}/"
    resto = ruta[len(prefijo):] if ruta.startswith(prefijo) else ruta
    partes = resto.split("/")
    return partes[0] if len(partes) > 1 else "Varios"


def autores_de(nombre: str, autor_carpeta: str) -> str:
    m = RE_AUTORES_FINAL.search(nombre)
    if not m:
        return autor_carpeta
    valor = m.group(1).strip()
    if valor.lower() == "varios":
        return "Varios"
    partes = re.split(r"\s*&\s*|\s*,\s*", valor)
    return " ; ".join(p.strip() for p in partes if p.strip())


def formato_de(nombre: str) -> str:
    if RE_RANGO.search(nombre):
        return "recopilatorio_rango"
    if RE_ISSUE.search(nombre):
        return "numero_suelto"
    if RE_VOL.search(nombre):
        return "volumen"
    return "obra_completa"


def enriquecer(ruta_csv: Path):
    with ruta_csv.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        campos_originales = lector.fieldnames
        filas = list(lector)

    campos_nuevos = [c for c in CAMPOS_NUEVOS if c not in campos_originales]
    campos_finales = list(campos_originales) + campos_nuevos

    for fila in filas:
        autor_carpeta = autor_carpeta_de(fila["ruta"], fila["region"])
        fila["autor_carpeta"] = autor_carpeta
        fila["autores"] = autores_de(fila["nombre"], autor_carpeta)
        fila["formato"] = formato_de(fila["nombre"])

    with ruta_csv.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=campos_finales)
        escritor.writeheader()
        escritor.writerows(filas)

    return len(filas)


def main():
    ruta_csv = Path(sys.argv[1]) if len(sys.argv) > 1 else CATALOGO_POR_DEFECTO
    total = enriquecer(ruta_csv)
    print(f"{total} filas enriquecidas en {ruta_csv} "
          f"(campos añadidos: {', '.join(CAMPOS_NUEVOS)}).")


if __name__ == "__main__":
    main()
