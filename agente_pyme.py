import os
import json
import httpx
from openai import OpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Helper para cargar variables de entorno en caso de no contar con python-dotenv
def obtener_env_var(clave: str, ruta_env: str = ".env") -> str:
    val = os.getenv(clave)
    if val:
        return val
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, ruta_env)
    
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    if k.strip() == clave:
                        return v.strip().strip("'").strip('"')
    return None

# 1. Obtener la clave API de forma segura
api_key_segura = obtener_env_var("NVIDIA_API_KEY")

if not api_key_segura:
    raise ValueError("Error: No se encontró la variable NVIDIA_API_KEY en el archivo .env ni en el entorno.")

# 2. Configurar la verificación SSL configurable (default: False para compatibilidad local)
verify_ssl = os.getenv("SSL_VERIFY", "false").lower() in ("true", "1")

cliente_compatible = httpx.Client(
    http1=True,
    http2=False,
    trust_env=False,
    verify=verify_ssl,
    timeout=httpx.Timeout(300.0, connect=60.0, read=300.0)
)

# 3. Inicializar cliente de NVIDIA
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key_segura,
    http_client=cliente_compatible,
    timeout=300.0
)

# 4. Definición de Herramientas (Skills)
def proyectar_inversion_market(rubro: str, presupuesto_usd: float, ubicacion: str) -> dict:
    """Calcula la viabilidad estratégica y proyección de inversión para una PyME."""
    print(f"\n[SKILL ACTIVADA] Procesando datos para: {rubro} en {ubicacion}...")
    if presupuesto_usd < 10000:
        estrategia = "Horizontalización: Cooperar con otras PyMEs locales para compras conjuntas de insumos."
        riesgo = "Alto si se intenta de forma individual."
    else:
        estrategia = "Inversión Directa: Desarrollo de un canal digital propio orientado a exportación regional."
        riesgo = "Moderado."
    return {
        "mercado_objetivo": ubicacion,
        "estrategia_sugerida": estrategia,
        "nivel_de_riesgo": riesgo
    }

AVAILABLE_TOOLS = {
    "proyectar_inversion_market": proyectar_inversion_market
}

TOOLS_SCHEMA = [{
    "type": "function",
    "function": {
        "name": "proyectar_inversion_market",
        "description": "Calcula la viabilidad estratégica y proyección de inversión para una PyME.",
        "parameters": {
            "type": "object",
            "properties": {
                "rubro": {"type": "string"},
                "presupuesto_usd": {"type": "number"},
                "ubicacion": {"type": "string"}
            },
            "required": ["rubro", "presupuesto_usd", "ubicacion"]
        }
    }
}]

# 5. Ejecución del flujo del Agente PyME
def ejecutar_agente_pyme(consulta: str):
    messages = [
        {
            "role": "system",
            "content": "Sos un agente experto en PyMEs y cooperativas. Si necesitas usar una herramienta para calcular/proyectar inversiones o estrategias, activala explícitamente."
        },
        {
            "role": "user",
            "content": consulta
        }
    ]

    print("Enviando consulta al cerebro del Agente (NVIDIA NIM Llama 3.3)...")

    # Pasar `tools` en la llamada a la API
    response = client.chat.completions.create(
        model="meta/llama-3.3-70b-instruct",
        messages=messages,
        tools=TOOLS_SCHEMA,
        tool_choice="auto",
        max_tokens=1024
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        print("\nLa IA determinó que necesita activar una Skill del repositorio.")
        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            if function_name in AVAILABLE_TOOLS:
                try:
                    function_to_call = AVAILABLE_TOOLS[function_name]
                    function_args = json.loads(tool_call.function.arguments)

                    skill_output = function_to_call(
                        rubro=function_args.get("rubro"),
                        presupuesto_usd=function_args.get("presupuesto_usd"),
                        ubicacion=function_args.get("ubicacion")
                    )

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": json.dumps(skill_output)
                    })
                except Exception as e:
                    print(f"Error al ejecutar la herramienta {function_name}: {e}")

        final_response = client.chat.completions.create(
            model="meta/llama-3.3-70b-instruct",
            messages=messages,
            max_tokens=1024
        )
        return final_response.choices[0].message.content
    else:
        return response_message.content

if __name__ == "__main__":
    consulta_pyme = (
        "Hola, somos una pequeña cooperativa textil de Hurlingham. "
        "Tenemos ahorrados unos 4500 dólares y queremos expandir nuestro mercado "
        "para vender ropa de trabajo a municipios vecinos. ¿Qué nos recomiendan hacer?"
    )
    resultado = ejecutar_agente_pyme(consulta_pyme)
    print("\n=== REPORTE ESTRATÉGICO PARA LA PYME ===")
    print(resultado)