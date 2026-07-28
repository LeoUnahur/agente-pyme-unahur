import os
import httpx
from openai import OpenAI

# Leemos la clave de tu .env de forma directa
with open(".env", "r", encoding="utf-8") as f:
    key = f.read().split("=")[1].strip().replace('"', '').replace("'", "")

# Forzamos HTTP/1.1 y desactivamos HTTP/2 para evitar el congelamiento de Anaconda
cliente_compatible = httpx.Client(
    http1=True,
    http2=False,
    trust_env=False,
    verify=False  # Ignoramos alertas de certificados por ahora
)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=key,
    http_client=cliente_compatible
)

print("Enviando un 'Hola' básico con parche HTTP/1.1...")
try:
    completion = client.chat.completions.create(
        model="meta/llama-3.3-70b-instruct",
        messages=[{"role": "user", "content": "Hola, responde únicamente con la palabra 'OK'."}],
        max_tokens=10
    )
    print("-> RESPUESTA DEL SERVIDOR:", completion.choices[0].message.content)
except Exception as e:
    print("-> FALLÓ LA CONEXIÓN:", e)