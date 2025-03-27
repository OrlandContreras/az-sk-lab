import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración para Azure OpenAI via LiteLLM según documentación oficial
# https://docs.crewai.com/concepts/llms#azure

# Obtenemos las variables de entorno para Azure
api_key = os.getenv("AZURE_API_KEY")
api_base = os.getenv("AZURE_API_BASE")
api_version = os.getenv("AZURE_API_VERSION")
deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")

def get_litellm_config():
    """Retorna la configuración para litellm con soporte para Azure OpenAI"""
    return {
        "model": f"azure/{deployment_name}",
        "api_key": api_key,
        "api_base": api_base,
        "api_version": api_version,
    } 