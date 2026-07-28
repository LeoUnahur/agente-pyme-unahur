import os
import json
import httpx  # Asegúrate de tener este import arriba
from openai import OpenAI

# 1. Obtener la ruta exacta del archivo .env
ruta_del_script = os.path.dirname(os.path.abspath(__file__))
ruta_del_env = os.path.join(ruta_del_script, '.env')

# 2. LEER LA CLAVE COMO TEXTO
api_key_segura = None
try:
    with open(ruta_del_env, 'r', encoding='utf-8') as f:
        for linea in f:
            if "NVIDIA_API_KEY" in linea:
                api_key_segura = linea.split('=')[1].strip().replace('"', '').replace("'", "")
                break
except Exception as e:
    raise RuntimeError(f"No se pudo abrir el archivo .env: {e}")

if not api_key_segura:
    raise ValueError(f"Error: No se encontró la variable NVIDIA_API_KEY en el archivo .env")

## 3. EL PARCHE GANADOR: Configurar el cliente de red HTTP/1.1 con tiempo de espera extendido
cliente_compatible = httpx.Client(
    http1=True,
    http2=False,
    trust_env=False,
    verify=False,   # Evita bloqueos de certificados locales
    timeout=120.0   # <-- LE DAMOS 2 MINUTOS COMPLETOS para que el servidor responda sin apuros
)

# 4. INICIALIZAR EL CLIENTE DE NVIDIA
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key_segura,
    http_client=cliente_compatible
)

# =====================================================================
# A PARTIR DE AQUÍ SIGUE EL RESTO DE TU CÓDIGO (Definición de skills, herramientas y consulta)
# =====================================================================
# =====================================================================
# DEFINICIÓN DE LA SKILL (A partir de aquí el código del agente sigue igual)
# =====================================================================
def proyectar_inversion_market(rubro: str, presupuesto_usd: float, ubicacion: str):
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

tools = [{
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

consulta_pyme = (
    "Hola, somos una pequeña cooperativa textil de Hurlingham. "
    "Tenemos ahorrados unos 4500 dólares y queremos expandir nuestro mercado "
    "para vender ropa de trabajo a municipios vecinos. ¿Qué nos recomiendan hacer?"
)

print("Enviando consulta al cerebro del Agente (NVIDIA NIM Llama 3.3)...")

response = client.chat.completions.create(
    model="meta/llama-3.3-70b-instruct",
   messages=[
        {
            "role": "system", 
            "content": "Sos un agente experto en PyMEs. Si necesitas usar una herramienta, indícalo explícitamente."
        },
        {
            "role": "user", 
            "content": consulta_pyme
        }
    ]
)

response_message = response.choices[0].message
tool_calls = response_message.tool_calls

if tool_calls:
    print("\nLa IA determinó que necesita activar una Skill de tu repositorio.")
    available_functions = {"proyectar_inversion_market": proyectar_inversion_market}
    
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        
        skill_output = function_to_call(
            rubro=function_args.get("rubro"),
            presupuesto_usd=function_args.get("presupuesto_usd"),
            ubicacion=function_args.get("ubicacion")
        )
        
        final_response = client.chat.completions.create(
            model="meta/llama-3.3-70b-instruct",
            messages=[
                {"role": "user", "content": consulta_pyme},
                response_message,
                {"role": "tool", "tool_call_id": tool_call.id, "name": function_name, "content": json.dumps(skill_output)}
            ]
        )
        print("\n=== REPORTE ESTRATÉGICO PARA LA PYME ===")
        print(final_response.choices[0].message.content)
else:
    print("La IA respondió directamente:")
    print(response_message.content)