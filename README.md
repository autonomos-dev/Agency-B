# Agente Multiple B

Este proyecto implementa un sistema de agentes múltiples utilizando la biblioteca AutoGen para crear una agencia virtual que ayuda a generar estrategias y contenido de marketing.

## Características

- Múltiples agentes especializados trabajando en conjunto
- Investigación automatizada
- Generación de contenido personalizado
- Análisis de mercado y competencia
- Recomendaciones estratégicas

## Requisitos Previos

- Python 3.8 o superior
- Cuenta en OpenAI (para las claves API)
- Git

## Instalación

1. Clonar el repositorio
bash
git clone https://github.com/autonomos-dev/Agente-Multiple-b.git

2. Crear y activar el entorno virtual
bash
python -m venv env
env\Scripts\activate # En Windows
source env/bin/activate # En Unix o MacOS

3. Instalar dependencias
bash
pip install -r requirements.txt

4. Configurar variables de entorno
   - Crear un archivo `.env` en el directorio raíz
   - Agregar las claves API necesarias:
   OPENAI_API_KEY=tu_clave_api_de_openai_aqu
   SERPER_API_KEY=tu_clave_api_de_serper_aquí

   
5. Configurar OAI_CONFIG_LIST
   - Crear un archivo `OAI_CONFIG_LIST` en el directorio raíz
   - Agregar la siguiente configuración:

   [
    {
        "model": "gpt-3.5-turbo-1106",
        "api_key": "tu_clave_api_de_openai_aquí"
    }
]

## Uso

1. Activar el entorno virtual (si no está activado)
bash
env\Scripts\activate # En Windows
source env/bin/activate # En Unix o MacOS

2. Ejecutar el programa

bash
python main.py

3. Seguir las instrucciones en pantalla
   - Ingresar el nombre de la marca o compañía
   - Especificar el objetivo o problema a resolver

## Estructura del Proyecto

Agente-Multiple-b/
├── main.py # Archivo principal con la lógica de los agentes
├── tools.py # Funciones de utilidad para los agentes
├── requirements.txt # Dependencias del proyecto
├── .env # Variables de entorno (no incluido en git)
├── .gitignore # Archivos ignorados por git
├── README.md # Este archivo
└── OAI_CONFIG_LIST # Configuración de OpenAI (no incluido en git

## Funcionalidad

El proyecto implementa un sistema de agentes múltiples que trabajan en conjunto para proporcionar soluciones de marketing y estrategia empresarial:

### Agentes Principales

1. **Agency Manager**
   - Coordina y supervisa las actividades de todos los agentes
   - Establece objetivos y prioridades
   - Asegura la coherencia en las estrategias propuestas

2. **Agency Researcher**
   - Realiza investigación de mercado
   - Analiza tendencias y competencia
   - Recopila datos relevantes para el proyecto

3. **Agency Copywriter**
   - Genera contenido creativo y persuasivo
   - Adapta el tono y estilo según la marca
   - Crea propuestas de valor únicas

4. **Writing Assistant**
   - Refina y mejora el contenido generado
   - Asegura la calidad y coherencia del texto
   - Optimiza el contenido para diferentes plataformas

### Flujo de Trabajo

1. El usuario ingresa el nombre de la marca y el objetivo
2. El Agency Manager analiza la solicitud y coordina con los demás agentes
3. El Agency Researcher recopila información relevante
4. El Agency Copywriter genera contenido basado en la investigación
5. El Writing Assistant refina y mejora el contenido final
6. El Agency Manager presenta los resultados al usuario

## Contribuir

1. Fork el proyecto
2. Crear una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## Contacto

Bastian Redt 

Link del proyecto: [https://github.com/autonomos-dev/Agente-Multiple-b](https://github.com/autonomos-dev/Agente-Multiple-b)