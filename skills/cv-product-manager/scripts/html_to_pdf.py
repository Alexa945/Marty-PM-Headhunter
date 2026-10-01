#!/usr/bin/env python3
"""Convierte un CV en HTML a PDF con Google Chrome en modo headless.

Uso:
    python3 html_to_pdf.py cv.html cv.pdf

El tamaño de papel lo decide el @page del propio HTML (Letter o A4).
El PDF resultante conserva el texto seleccionable (legible por ATS).
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
]


def find_browser():
    for path in CANDIDATES:
        if os.path.exists(path):
            return path
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    return None


def main():
    if len(sys.argv) != 3:
        sys.exit("Uso: python3 html_to_pdf.py entrada.html salida.pdf")
    src = Path(sys.argv[1]).expanduser().resolve()
    out = Path(sys.argv[2]).expanduser().resolve()
    if not src.exists():
        sys.exit(f"No existe: {src}")
    out.parent.mkdir(parents=True, exist_ok=True)

    browser = find_browser()
    if not browser:
        sys.exit("No encontré Chrome/Chromium/Edge/Brave. Abre el HTML en un navegador y usa Imprimir → Guardar como PDF.")

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={out}",
        src.as_uri(),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if not out.exists() or out.stat().st_size == 0:
        sys.stderr.write(result.stderr)
        sys.exit("No se generó el PDF.")
    print(f"PDF generado: {out}")


if __name__ == "__main__":
    main()
