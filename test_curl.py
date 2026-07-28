import os
import subprocess
import json

# 1. Leer la clave de forma directa
with open(".env", "r", encoding="utf-8") as f:
    key = f.read().split("=")[1].strip().replace('"', '').replace("'", "")

print("Probando conexión nativa con CURL (Bypasseando Python SSL)...")

# 2. Configurar la petición exacta para NVIDIA
payload = {
    "model": "meta/llama-3.3-70b-instruct",
    "messages": [{"role": "user", "content": "Hola, responde únicamente con la palabra OK."}],
    "max_tokens": 10
}

comando = [
    "curl", "-s", "-X", "POST", "https://integrate.api.nvidia.com/v1/chat/completions",
    "-H", f"Authorization: Bearer {key}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
]

# 3. Ejecutar a nivel sistema operativo
try:
    resultado = subprocess.run(comando, capture_output=True, text=True, timeout=15)
    if resultado.returncode == 0:
        print("\n[¡ÉXITO TOTAL con CURL!]")
        print("Respuesta cruda de NVIDIA:")
        print(resultado.stdout)
    else:
        print("\n[CURL FALLÓ]")
        print("Código de error:", resultado.returncode)
        print("Detalle:", resultado.stderr)
except Exception as e:
    print("Error al ejecutar el comando del sistema:", e)