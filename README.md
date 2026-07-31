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

## 📦 Guía de Instalación y Ejecución Paso a Paso

Si querés clonar este repositorio y ejecutar el proyecto en tu propia computadora, seguí estos pasos:

### 1. Requisitos Previos
* Tener instalado [Python 3.10](https://www.python.org/) o superior.
* Tener instalado [Git](https://git-scm.com/).

### 2. Clonar el Repositorio
Abrí tu terminal o consola de comandos y ejecutá:
```bash
git clone [https://github.com/TU_USUARIO/agente-pyme-unahur.git](https://github.com/TU_USUARIO/agente-pyme-unahur.git)
cd agente-pyme-unahur

(Recordá reemplazar TU_USUARIO por tu usuario de GitHub).

### 3. Crear y Activar el Entorno Virtual

El entorno virtual aísla las librerías del proyecto para evitar conflictos con otros programas de tu sistema.

En Windows (PowerShell / CMD / Terminal de VS Code):

python -m venv venv
.\venv\Scripts\activate

En macOS / Linux:

python3 -m venv venv
source venv/bin/activate

💡 Tip para VS Code: Presioná Ctrl + Shift + P (o Cmd + Shift + P en Mac), buscá Python: Select Interpreter y seleccioná el entorno que acabás de crear (./venv/Scripts/python.exe).

### 4. Instalar las Dependencias
Con el entorno virtual activado, instalá las librerías necesarias:

pip install openai httpx python-dotenv

### 5. Configurar las Claves de Acceso (API Keys):

   Por razones de seguridad, las claves secretas nunca se suben al repositorio público.

   5.1 Creá un archivo llamado .env en la raíz del proyecto.

   5.2 Abrí el archivo .env.example que viene en el proyecto como referencia.

   5.3 Copiá su contenido dentro del nuevo archivo .env y pegá tu API Key real de NVIDIA:

   NVIDIA_API_KEY="nvapi-tu-clave-aqui"

### 6. Ejecutar el Agente de IA
   
   Para iniciar la ejecución del agente, corre:

   python agente_pyme.py

   ### 📄 Licencia y Contacto

   Licencia: Proyecto distribuido bajo la licencia Apache 2.0.

   De Leonardo D. Baldini, estudiante de la Tecnicatura Universitaria en IA de Universidad Nacional de Hurlingham (UNAHUR) - Instituto de Tecnología e Ingeniería.
   

