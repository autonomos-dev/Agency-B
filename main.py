import os
import openai
import dotenv

from autogen import config_list_from_json, UserProxyAgent, AssistantAgent, GroupChat, GroupChatManager
from tools import research, write_content

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
config_list = config_list_from_json("OAI_CONFIG_LIST")

brand_task = input("Ingresa el nombre de la marca o compañía: ")
user_task = input("Por favor ingresa tu objetivo o problema: ")

llm_config_content_assistant = {
    "functions": [
        {
            "name": "research",
            "description": "Investiga sobre un tema dado y retorna el material de investigación incluyendo enlaces de referencia",
            "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "El tema sobre el cual investigar",
                        }
                    },
                "required": ["query"],
            },
        },
        {
            "name": "write_content",
            "description": "Escribe contenido basado en el material de investigación y tema proporcionados",
            "parameters": {
                    "type": "object",
                    "properties": {
                        "research_material": {
                            "type": "string",
                            "description": "Material de investigación sobre un tema dado, incluyendo enlaces de referencia cuando estén disponibles",
                        },
                        "topic": {
                            "type": "string",
                            "description": "El tema del contenido",
                        }
                    },
                "required": ["research_material", "topic"],
            },
        },
    ],
    "config_list": config_list,
    "timeout": 120,
}

agency_manager = AssistantAgent(
    name="Agency_Manager",
    description="Coordina y desarrolla el plan para los agentes.",
    llm_config={"config_list": config_list},
    system_message=f'''
    Desarrolla tareas paso a paso para {brand_task} y {user_task} con el equipo.
    Actúa como centro de comunicación, mantén entregables de alta calidad y actualiza regularmente a todos los interesados sobre el progreso.
    Termina la conversación con "TERMINATE" cuando todas las tareas estén completadas y no se necesiten más acciones.
    '''
)
os.environ["AUTOGEN_USE_DOCKER"] = "0"

agency_researcher = AssistantAgent(
    name="Agency_Researcher",
    description="Realiza investigación detallada para proporcionar información para ejecutar tareas enfocadas al usuario.",
    llm_config=llm_config_content_assistant,
    system_message=f'''
    Utiliza la función de investigación para recopilar información sobre tendencias del mercado, puntos débiles del usuario y dinámicas culturales relevantes para nuestro proyecto.
    Enfócate en entregar información clara y procesable.
    Concluye tu participación con "TERMINATE" una vez que toda la investigación relevante haya sido proporcionada.
    '''
)
agency_researcher.register_function(
    function_map={
        "research": research
    }
)


agency_strategist = AssistantAgent(
    name="Agency_Strategist",
    description="Desarrolla informes estratégicos basados en análisis de mercado e investigación.",
    llm_config={"config_list": config_list},
    system_message=f'''
    Como Estratega Principal, tu tarea clave es desarrollar informes estratégicos para {brand_task}, guiado por los objetivos de {user_task}.
    Utiliza los conocimientos del Agency_Researcher para informar tus estrategias, enfocándote en posicionamiento de marca, mensajes clave y segmentación de audiencia.
    Asegura que tus informes ofrezcan perspectivas únicas y dirección clara.
    Coordina estrechamente con el Agency_Manager para alinearte con los objetivos del proyecto.
    Concluye con "TERMINATE" una vez que la dirección estratégica esté establecida y comunicada.
    '''
)

agency_writer = AssistantAgent(
    name="Agency_Copywriter",
    description="Crea contenido y narrativas atractivas alineadas con los objetivos del proyecto.",
    llm_config={"config_list": config_list},
    system_message="""
    Como Redactor Principal, tu rol es crear narrativas y contenido convincente.
    Enfócate en entregar mensajes claros, atractivos y relevantes que resuenen con nuestra audiencia objetivo.
    Usa tu creatividad para transformar conocimientos estratégicos y hallazgos de investigación en contenido impactante.
    Asegura que tu escritura mantenga la voz de la marca y se alinee con la estrategia general del proyecto.
    Concluye con "TERMINATE" cuando el contenido esté completo y refinado.
    """,
    function_map={
        "write_content": write_content,
    },
)

writing_assistant = AssistantAgent(
    name="writing_assistant",
    description="Asistente versátil especializado en investigar diversos temas y crear contenido bien escrito.",
    llm_config=llm_config_content_assistant,
    system_message="""
    Como asistente de escritura, tu rol implica usar la función de investigación para mantenerte actualizado en diversos temas y emplear la función write_content para producir prosa pulida.
    Asegura que tu material escrito sea informativo y bien estructurado, atendiendo a las necesidades específicas del tema.
    Concluye tus contribuciones con "TERMINATE" después de completar las tareas de escritura según lo requerido.
    """,
    function_map={
        "research": research,
        "write_content": write_content,
    },
)

agency_marketer = AssistantAgent(
    name="Agency_Marketer",
    description="Desarrolla estrategias y campañas de marketing adaptadas a las necesidades de la audiencia.",
    llm_config={"config_list": config_list},
    system_message=f'''
    Como Responsable de Marketing, utiliza los conocimientos y estrategias para desarrollar ideas que conecten con nuestra audiencia objetivo.
    Para {user_task}, crea campañas e iniciativas que comuniquen claramente el valor de nuestra marca.
    Une estrategia y ejecución, asegurando que nuestro mensaje sea impactante y alineado con nuestra visión.
    Colabora con los equipos para un enfoque unificado y coordina con el Agency Manager para la alineación del proyecto.
    Concluye con "TERMINATE" cuando tus contribuciones de marketing estén completas.
    '''
)

agency_mediaplanner = AssistantAgent(
    name="Agency_Media_Planner",
    description="Identifica canales y estrategias óptimas de medios para la entrega de publicidad.",
    llm_config={"config_list": config_list},
    system_message=f'''
    Como Planificador de Medios Principal, tu tarea es identificar la mezcla ideal de medios para entregar nuestros mensajes publicitarios.
    Utiliza la función de investigación para mantenerte actualizado sobre canales y tácticas de medios efectivos.
    Aplica los conocimientos de {user_task} para formular estrategias que alcancen efectivamente a la audiencia.
    Colabora estrechamente con el Agency Manager para asegurar que tus planes estén sincronizados con la estrategia general.
    Concluye tu rol con "TERMINATE" una vez que la planificación de medios esté completa y alineada.
    '''
)

agency_director = AssistantAgent(
    name="Agency_Director",
    description="Guía la visión creativa del proyecto, asegurando originalidad, excelencia y relevancia en todas las ideas y ejecuciones.",
    llm_config={"config_list": config_list},
    system_message="""
    Como Director Creativo, tu rol es supervisar los aspectos creativos del proyecto.
    Evalúa críticamente todo el trabajo, asegurando que cada idea sea única y se alinee con nuestros estándares de excelencia.
    Anima al equipo a innovar y explorar nuevas avenidas creativas.
    Colabora estrechamente con el Agency_Manager para mantener la alineación con el user_proxy.
    Concluye tu guía con "TERMINATE" una vez que hayas asegurado la integridad creativa y alineación del proyecto.
    """,
)

user_proxy = UserProxyAgent(
   name="user_proxy",
   description="Actúa como proxy para el usuario, ejecutando código y manejando interacciones dentro de pautas predefinidas.",
   is_termination_msg=lambda msg: "TERMINATE" in msg["content"] if msg["content"] else False,
   human_input_mode="TERMINATE",
   max_consecutive_auto_reply=1,
   code_execution_config={
       "work_dir": "/logs",
       "use_docker": False
   },
   system_message='Sé un asistente útil y comunícate siempre en español.',
)

groupchat = GroupChat(
    agents=[user_proxy, agency_manager, agency_researcher, agency_strategist, 
            agency_writer, writing_assistant, agency_marketer, agency_mediaplanner, 
            agency_director], 
    messages=[], 
    max_round=20
)

manager = GroupChatManager(
    groupchat=groupchat, 
    llm_config={"config_list": config_list}
)

user_proxy.initiate_chat(
    manager, 
    message=user_task,
)