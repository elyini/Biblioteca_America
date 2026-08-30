#!/usr/bin/env python3
"""Biblioteca America — extrae mi parte del informe de Biblioteca Mac.

Versión del repo en la última actualización de este script: v0.2.0

Filtra `elyini_informe_<fecha>.json` (elyini_scanner.py, Biblioteca Mac)
para quedarse solo con las carpetas AMERICANO e IBEROAMERICANO del
volumen AMERICA (excluye YANKI, que pertenece a Biblioteca America
Comics), y genera:

- data/escaneos/america_<fecha>.json — copia filtrada del informe
  original (solo mis archivos), para no depender de que el repo de
  Biblioteca Mac esté disponible/actualizado.
- data/catalogo.csv — catálogo de trabajo derivado, una fila por archivo.

No borra, mueve ni modifica nada en el volumen real; solo lee el JSON de
informe ya entregado por Biblioteca Mac.

Uso: python3 extraer_catalogo.py <ruta_informe_elyini_scanner.json>
"""

import csv
import json
import sys
from pathlib import Path

CARPETAS_PROPIAS = ("AMERICANO", "IBEROAMERICANO")
REPO_ROOT = Path(__file__).resolve().parent.parent


def cargar_archivos_america(ruta_informe: Path):
    with ruta_informe.open(encoding="utf-8") as f:
        informe = json.load(f)
    biblios = {b["nombre"]: b for b in informe["bibliotecas"]}
    america = biblios["AMERICA"]
    archivos = [
        a
        for a in america["archivos"]
        if any(
            a["ruta"].startswith(f"/Volumes/AMERICA/{carpeta}/")
            for carpeta in CARPETAS_PROPIAS
        )
    ]
    return informe, archivos


def region_de(ruta: str) -> str:
    for carpeta in CARPETAS_PROPIAS:
        if ruta.startswith(f"/Volumes/AMERICA/{carpeta}/"):
            return carpeta
    return "desconocida"


def guardar_json_filtrado(informe, archivos, fecha, salida: Path):
    salida.parent.mkdir(parents=True, exist_ok=True)
    filtrado = {
        "fecha_escaneo_original": informe["fecha_escaneo"],
        "fuente": "elyini_scanner.py (Biblioteca Mac)",
        "carpetas_incluidas": list(CARPETAS_PROPIAS),
        "carpetas_excluidas": ["YANKI (Biblioteca America Comics)"],
        "total_archivos": len(archivos),
        "archivos": archivos,
    }
    with salida.open("w", encoding="utf-8") as f:
        json.dump(filtrado, f, ensure_ascii=False, indent=2)


def guardar_catalogo_csv(archivos, salida: Path):
    salida.parent.mkdir(parents=True, exist_ok=True)
    campos = [
        "region",
        "ruta",
        "nombre",
        "extension",
        "tamano_bytes",
        "tamano_h",
        "tipo_detectado",
        "idioma",
        "serie",
        "volumen",
        "numero",
        "patron",
    ]
    with salida.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for a in archivos:
            writer.writerow(
                {
                    "region": region_de(a["ruta"]),
                    "ruta": a["ruta"],
                    "nombre": a["nombre"],
                    "extension": a.get("extension"),
                    "tamano_bytes": a.get("tamano"),
                    "tamano_h": a.get("tamano_h"),
                    "tipo_detectado": a.get("tipo"),
                    "idioma": a.get("idioma"),
                    "serie": a.get("serie"),
                    "volumen": a.get("volumen"),
                    "numero": a.get("numero"),
                    "patron": a.get("patron"),
                }
            )


def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <ruta_informe_elyini_scanner.json>")
        sys.exit(1)

    ruta_informe = Path(sys.argv[1])
    informe, archivos = cargar_archivos_america(ruta_informe)
    fecha = ruta_informe.stem.rsplit("_", 1)[-1]

    json_salida = REPO_ROOT / "data" / "escaneos" / f"america_{fecha}.json"
    csv_salida = REPO_ROOT / "data" / "catalogo.csv"

    guardar_json_filtrado(informe, archivos, fecha, json_salida)
    guardar_catalogo_csv(archivos, csv_salida)

    print(f"{len(archivos)} archivos extraídos (AMERICANO + IBEROAMERICANO).")
    print(f"JSON filtrado: {json_salida}")
    print(f"Catálogo CSV:  {csv_salida}")


if __name__ == "__main__":
    main()
