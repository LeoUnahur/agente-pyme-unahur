# 🤖 Hub Inteligente de Vinculación y Cohesión Socioproductiva

> **Proyecto de Investigación y Desarrollo — Universidad Nacional de Hurlingham (UNAHUR)**  
> *Agente de Inteligencia Artificial para la Optimización de Recurso Ocioso y Articulación Cooperativa en el Entramado PyME de Hurlingham.*

---

## 📌 Presentación del Proyecto

Este repositorio contiene el prototipo inicial de un **Agente de Inteligencia Artificial** diseñado para actuar como un *clearinghouse* o nodo de intercambio de recursos en el municipio de Hurlingham.

En el contexto económico actual, el objetivo central del proyecto es la **retención de valor en el territorio y la reducción de costos operativos** de las cooperativas y micro-PyMEs locales, transformando la capacidad productiva ociosa en alianzas estratégicas sin requerir erogaciones de capital.

---

## 🚀 Fases de Implementación y Proyección

### **Fase 1: Diagnóstico Territorial y Reactivación por Eficiencia Cruzada (Local)**
* **Mapeo de Capacidad Ociosa:** Relevamiento de horas/máquina detenidas, espacio de acopio subutilizado y capacidad logística sobrante.
* **Reducción de Costos Operativos:** Simbiosis entre unidades productivas (ej. cruce de cuellos de botella con sobrantes de infraestructura).
* **Democratización Tecnológica:** Interfaz de consulta en lenguaje natural orientada a la eliminación de la brecha digital.

### **Fase 2: Red Federada de Subestaciones Universitarias (Regional)**
* Interconexión del modelo local con otras universidades públicas del Conurbano Bonaerense (UNGS, UNM, UNO, UNLaM).
* Creación de un ecosistema intermunicipal federado para la escala de nuevos canales de comercialización y complementariedad regional.

---

## 📊 Matriz Mínima de Datos Relevados

El agente procesa variables territoriales estructuradas en tres dimensiones esenciales:

1. **Dimensión Productiva:** Tipo de equipamiento, disponibilidad horaria de maquinaria y umbrales mínimos de producción.
2. **Dimensión Logística:** Rutas/frecuencias con espacio remanente y metros cuadrados de almacenamiento ocioso.
3. **Dimensión de Insumos:** Stock crítico acumulado y detección de cuellos de botella inmediatos.

---

## 🛠️ Arquitectura Técnica y Soberanía Digital

* **Lenguaje:** Python 3.11+
* **Orquestador de API:** OpenAI Python SDK + Client customizado `httpx` (HTTP/1.1 fallback & extended timeout).
* **Modelo LLM:** Integración vía NVIDIA NIM Client (Llama 3 Instruct Series).
* **Despliegue Objetivo:** Migración proyectada hacia inferencia local (*Ollama / Llama 8B*) en infraestructura de la UNAHUR para garantizar soberanía de datos y costo cero de cómputo.

---

## 📦 Configuración e Instalación Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/agente-pyme-unahur.git](https://github.com/TU_USUARIO/agente-pyme-unahur.git)
   cd agente-pyme-unahur

2. **Crear y activar el entorno virtual**

Bash:
python -m venv .env-skills
# En Windows:
.env-skills\Scripts\activate

3. **Instalar dependencias**

pip install openai httpx python-dotenv

4. **Configurar variables de entorno**

Crea un archivo .env basado en el archivo .env.example:

NVIDIA_API_KEY="tu_api_key_aqui"

**Ejecutar agente**

python agente_pyme.py

---

### Paso 2: Crear los dos archivos de seguridad (si todavía no existen)

Revisa el panel de la izquierda de VS Code:

1. **`.gitignore`**: Crea este archivo si no está en la lista y dentro poné la línea `.env`. Esto es importante para que tu API Key no se suba pública a internet.
2. **`.env.example`**: Crea este archivo si no existe y dentro poné la línea `NVIDIA_API_KEY="tu_api_key_aqui"`.

---

### Paso 3: Guardar y subir los cambios a GitHub

Ahora sí, volvé a la terminal de VS Code y ejecutá los comandos:

```bash
git add .

git commit -m "docs: adaptar README para proyecto institucional de IA UNAHUR"

git push
