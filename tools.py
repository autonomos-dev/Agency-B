import os
import json
import requests
from autogen import UserProxyAgent, AssistantAgent, GroupChat, GroupChatManager, config_list_from_json
import dotenv

dotenv.load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
config_list = config_list_from_json("OAI_CONFIG_LIST")

def search(query):
    """
    Realiza una búsqueda web y retorna los resultados en español
    """
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q": query,
        "gl": "es",  # Localización para España/Español
        "hl": "es",  # Idioma español
    })
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def research(query):
    """
    Investiga sobre un tema dado y retorna el material de investigación incluyendo enlaces de referencia
    """
    # Primero realizamos la búsqueda
    search_results = search(query)
    
    # Formateamos los resultados para un mejor procesamiento
    formatted_results = "Resultados de la búsqueda:\n\n"
    
    # Añadimos el featured snippet si existe
    if 'answerBox' in search_results:
        formatted_results += f"Respuesta destacada:\n{search_results['answerBox'].get('snippet', '')}\n\n"
    
    # Añadimos los resultados orgánicos
    if 'organic' in search_results:
        formatted_results += "Resultados principales:\n"
        for result in search_results['organic'][:5]:  # Tomamos los primeros 5 resultados
            formatted_results += f"- {result['title']}\n"
            formatted_results += f"  {result['snippet']}\n"
            formatted_results += f"  Fuente: {result['link']}\n\n"
    
    # Creamos un resumen con la información recopilada
    user_proxy = UserProxyAgent(
        name="researcher",
        system_message="Eres un investigador experto. Analiza la información proporcionada y crea un resumen detallado en español.",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,
        llm_config={"config_list": config_list},
    )

    researcher = AssistantAgent(
        name="researcher",
        system_message="Eres un asistente de investigación experto. Ayuda a crear resúmenes detallados y bien estructurados en español.",
        llm_config={"config_list": config_list},
    )

    # Iniciamos una conversación para crear el resumen
    chat = GroupChat(
        agents=[user_proxy, researcher],
        messages=[],
        max_round=3
    )

    manager = GroupChatManager(groupchat=chat, llm_config={"config_list": config_list})
    
    # Solicitamos el resumen
    final_prompt = f"Por favor, analiza y resume esta información sobre '{query}':\n\n{formatted_results}"
    user_proxy.initiate_chat(manager, message=final_prompt)
    
    # Extraemos el resumen del último mensaje
    summary = ""
    for message in manager.chat_messages[researcher.name]:
        if isinstance(message, dict) and "content" in message:
            summary = message["content"]
            break
    
    return summary

def write_content(research_material, topic):
    """
    Escribe contenido basado en el material de investigación y tema proporcionados
    """
    admin = UserProxyAgent(
        name="admin",
        system_message="Eres un administrador experto. Tu trabajo es coordinar la creación de contenido de alta calidad en español.",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,
    )

    writer = AssistantAgent(
        name="writer",
        system_message="Eres un escritor creativo experto. Tu trabajo es crear contenido atractivo y persuasivo en español.",
        llm_config={"config_list": config_list},
    )

    editor = AssistantAgent(
        name="editor",
        system_message="Eres un editor experto. Tu trabajo es revisar y mejorar el contenido manteniendo un tono profesional y coherente en español.",
        llm_config={"config_list": config_list},
    )

    reviewer = AssistantAgent(
        name="reviewer",
        system_message="Eres un revisor experto. Tu trabajo es proporcionar retroalimentación constructiva para mejorar el contenido en español.",
        llm_config={"config_list": config_list},
    )

    # Creamos el chat grupal
    groupchat = GroupChat(
        agents=[admin, writer, editor, reviewer],
        messages=[],
        max_round=12
    )

    manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})

    # Mensaje inicial para el chat
    prompt = f"Escribe un artículo sobre {topic}, aquí está el material de investigación: {research_material}"
    
    admin.initiate_chat(
        manager,
        message=prompt,
    )

    # Recopilamos el contenido final
    final_content = ""
    for message in manager.chat_messages[writer.name]:
        if isinstance(message, dict) and "content" in message:
            final_content = message["content"]
            break

    return final_content

def get_content_from_chat_history(chat_history):
    """
    Extrae el contenido relevante del historial del chat
    """
    content = []
    for message in chat_history:
        if isinstance(message, dict) and "content" in message:
            content.append(message["content"])
    return "\n".join(content)