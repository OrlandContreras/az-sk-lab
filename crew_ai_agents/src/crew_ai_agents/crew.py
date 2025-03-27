from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

# Importar nuestra configuración personalizada
from crew_ai_agents.config.litellm_config import get_litellm_config

# Cargar variables de entorno
load_dotenv()

# Obtener configuración LiteLLM para Azure
litellm_config = get_litellm_config()

# Crear una instancia de LLM según la documentación oficial
azure_llm = LLM(
    model=litellm_config["model"],
    api_key=litellm_config["api_key"],
    api_base=litellm_config["api_base"],
    api_version=litellm_config["api_version"],
    temperature=0.7
)

@CrewBase
class CrewAiAgents():
	"""CrewAiAgents crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			llm=azure_llm
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=azure_llm
		)


	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewAiAgents crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
