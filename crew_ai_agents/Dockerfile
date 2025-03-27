FROM python:3.11-slim

WORKDIR /app

# Copiar archivos de proyecto
COPY pyproject.toml .
COPY src/ ./src/
COPY .env .
COPY knowledge/ ./knowledge/
COPY uv.lock .

# Instalar dependencias
RUN pip install --no-cache-dir -e .
RUN pip install --no-cache-dir uvicorn fastapi python-dotenv litellm

# Exponer el puerto 8000 para la API FastAPI
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "crew_ai_agents.app:app", "--host", "0.0.0.0", "--port", "8000"] 