from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import warnings
import os
from dotenv import load_dotenv

# Importar la clase CrewAiAgents
from crew_ai_agents.crew import CrewAiAgents

# Cargar variables de entorno
load_dotenv()

# Ignorar ciertas advertencias
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

app = FastAPI(title="API de CrewAI Agents")

# Modelos de entrada para cada endpoint
class TrainRequest(BaseModel):
    n_iterations: int
    filename: str

class ReplayRequest(BaseModel):
    task_id: str

class TestRequest(BaseModel):
    n_iterations: int

@app.post("/run")
async def run_endpoint():
    """
    Ejecuta la función 'run' que inicia el crew con unos inputs predefinidos.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    try:
        CrewAiAgents().crew().kickoff(inputs=inputs)
        return {"message": "Crew run executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while running the crew: {e}")

@app.post("/train")
async def train_endpoint(request: TrainRequest):
    """
    Entrena el crew por un número de iteraciones, usando un archivo dado.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        CrewAiAgents().crew().train(
            n_iterations=request.n_iterations,
            filename=request.filename,
            inputs=inputs
        )
        return {"message": "Crew training executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while training the crew: {e}")

@app.post("/replay")
async def replay_endpoint(request: ReplayRequest):
    """
    Reproduce la ejecución del crew a partir de un task_id específico.
    """
    try:
        CrewAiAgents().crew().replay(task_id=request.task_id)
        return {"message": "Crew replay executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while replaying the crew: {e}")

@app.post("/test")
async def test_endpoint(request: TestRequest):
    """
    Ejecuta un test del crew con un número limitado de iteraciones.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        # Crear una instancia de CrewAiAgents
        crew_instance = CrewAiAgents()
        crew = crew_instance.crew()
        
        # Usar el mismo LLM configurado en el crew para evaluación
        eval_agent = crew_instance.researcher()
        
        # Ejecutar el test con los parámetros necesarios
        crew.test(
            n_iterations=request.n_iterations,
            inputs=inputs,
            eval_llm=eval_agent.llm
        )
        
        return {"message": "Crew test executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while testing the crew: {e}")
