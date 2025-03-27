# CrewAI Agents en Docker

Este proyecto implementa una API para CrewAI Agents utilizando FastAPI y Docker.

## Requisitos

- Docker
- Docker Compose

## Configuración del Entorno

1. Copia el archivo de ejemplo de variables de entorno y configúralo con tus credenciales:

```bash
cp .env.example .env
```

2. Edita el archivo `.env` con tus credenciales de Azure OpenAI:
   - `AZURE_API_KEY`: Tu clave de API de Azure OpenAI
   - `AZURE_API_BASE`: URL base de tu recurso de Azure OpenAI
   - `AZURE_API_VERSION`: Versión de la API de Azure OpenAI
   - `AZURE_DEPLOYMENT_NAME`: Nombre de tu deployment de modelo en Azure OpenAI

3. La carpeta `knowledge` debe contener los archivos de conocimiento que serán utilizados por los agentes.

## Construcción y ejecución

Para construir y ejecutar la aplicación:

```bash
docker-compose up --build
```

Para ejecutar en segundo plano:

```bash
docker-compose up -d
```

## Uso de la API

La API estará disponible en `http://localhost:8000` con los siguientes endpoints:

- **POST /run**: Ejecuta el crew con parámetros predefinidos
- **POST /train**: Entrena el crew por un número de iteraciones
- **POST /replay**: Reproduce la ejecución desde un task_id específico
- **POST /test**: Ejecuta pruebas con el crew

### Ejemplos de uso

1. Ejecutar el crew:

```bash
curl -X POST http://localhost:8000/run
```

2. Entrenar el crew:

```bash
curl -X POST http://localhost:8000/train \
  -H "Content-Type: application/json" \
  -d '{"n_iterations": 5, "filename": "training_data.json"}'
```

3. Reproducir una ejecución:

```bash
curl -X POST http://localhost:8000/replay \
  -H "Content-Type: application/json" \
  -d '{"task_id": "your-task-id"}'
```

4. Realizar pruebas:

```bash
curl -X POST http://localhost:8000/test \
  -H "Content-Type: application/json" \
  -d '{"n_iterations": 1}'
```

## Documentación de la API

Puede acceder a la documentación completa de la API en `http://localhost:8000/docs`

## Seguridad

- Asegúrese de que el archivo `.env` con sus credenciales no se suba al repositorio.
- Si el proyecto está dentro de un repositorio Git, confirme que el archivo `.gitignore` incluye `.env` para evitar compartir datos sensibles.
- Use siempre el archivo `.env.example` como plantilla sin datos sensibles para compartir en el repositorio. 