# Agency-b

Un sistema de agentes inteligentes para investigación y generación de contenido en español.

## Características

- Búsqueda y análisis de información en tiempo real
- Generación de contenido basado en investigación
- Comunicación entre agentes para procesamiento de información
- Resultados en español
- Integración con APIs de búsqueda y procesamiento de lenguaje natural

## Requisitos

- Python 3.8+
- OpenAI API key
- Serper API key

## Instalación

1. Clonar el repositorio:
  bash
git clone https://github.com/TU_USUARIO/Agency-b.git
cd Agency-b


2. Crear y activar entorno virtual:
ash
python -m venv nuevo_env
source nuevo_env/bin/activate # En Windows: nuevo_env\Scripts\activate


3. Instalar dependencias:
bash
pip install -r requirements.txt



4. Configurar variables de entorno:
   - Crear archivo `.env` con las siguientes variables:
     ```
     OPENAI_API_KEY=tu_clave_api_openai
     SERPER_API_KEY=tu_clave_api_serper
     
5.  crear un archivo OAI_CONFIG_LIST y agregar la siguiente información:
     ```
     [
        {
            "model": "gpt-3.5-turbo-11",
            "api_key": "TU_API_KEY"
        }
     ]
     ```
   - Configurar `OAI_CONFIG_LIST` con las credenciales necesarias

## Uso

1. Activar el entorno virtual:

bash
nuevo_env\Scripts\activate # En Windows
source nuevo_env/bin/activate # En Linux/Mac

2. Ejecutar el programa:
bash
python main.py

3. Seguir las instrucciones en pantalla:
   - Ingresar el nombre de la marca o compañía
   - Especificar el objetivo o problema a resolver

## Estructura del Proyecto
gency-b/
├── agentcy/
│ ├── init.py
│ ├── main.py
│ └── tools.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md



## Funcionalidades

- **Investigación Automatizada**: Búsqueda y análisis de información relevante en tiempo real
- **Generación de Contenido**: Creación de contenido basado en la investigación realizada
- **Procesamiento en Español**: Toda la interacción y resultados en español
- **Análisis de Mercado**: Capacidad para analizar tendencias y datos del mercado
- **Recomendaciones Estratégicas**: Sugerencias basadas en el análisis de la información

## Contribuir

1. Fork el proyecto
2. Crear una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## Contacto

Bastian-Redt

