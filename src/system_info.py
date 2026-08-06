import json
import os
import platform
import shutil
import subprocess
import sys

import numpy as np
import psutil


def win_query(consulta):
    """Ejecuta una consulta de PowerShell y devuelve su salida de texto."""
    try:
        resultado = subprocess.run(
            ["powershell", "-NoProfile", "-Command", consulta],
            capture_output=True,
            text=True,
            timeout=15,
            encoding="utf-8",
        )
        linea = resultado.stdout.strip()
        return linea if linea else None
    except Exception:
        return None


def obtener_procesador():
    nombre = win_query("(Get-CimInstance Win32_Processor).Name")
    if nombre:
        return nombre
    return platform.processor() or None


info = {
    "sistema_operativo": platform.system(),
    "version_sistema": platform.release(),
    "arquitectura": platform.machine(),
    "version_python": sys.version.split()[0],
    "version_numpy": np.__version__,
    "procesador": obtener_procesador() or "no disponible",
    "nucleos_fisicos": psutil.cpu_count(logical=False),
    "procesadores_logicos": psutil.cpu_count(),
    "ram_total_bytes": psutil.virtual_memory().total,
    "ram_disponible_bytes": psutil.virtual_memory().available,
    "gpu": win_query("(Get-CimInstance Win32_VideoController).Name") or "no disponible",
    "disco_total_bytes": shutil.disk_usage(".").total,
    "disco_libre_bytes": shutil.disk_usage(".").free,
}

os.makedirs("data", exist_ok=True)
with open("data/system_info.json", "w", encoding="utf-8") as f:
    json.dump(info, f, indent=4, ensure_ascii=False)

print(json.dumps(info, indent=4, ensure_ascii=False))
