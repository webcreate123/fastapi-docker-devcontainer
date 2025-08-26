# FastAPI TODO API

A simple and modern TODO API built with FastAPI, Docker, and Dev Container support.

## Features

- ✅ CRUD operations for TODO items
- 🚀 FastAPI with automatic API documentation
- 🐳 Docker containerization
- 🔧 Dev Container support for VS Code
- 📝 Pydantic models for data validation
- 🔄 In-memory storage (easily replaceable with database)
- 🏥 Health check endpoint
- 🌐 CORS enabled

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET | `/todos` | Get all todos |
| GET | `/todos/{id}` | Get specific todo |
| POST | `/todos` | Create new todo |
| PUT | `/todos/{id}` | Update todo |
| DELETE | `/todos/{id}` | Delete todo |
| PATCH | `/todos/{id}/toggle` | Toggle completion status |

## Quick Start

### Option 1: Using Dev Container (Recommended for Development)

1. Install [VS Code](https://code.visualstudio.com/) and [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Open this project in VS Code
4. When prompted, click "Reopen in Container"
5. The API will be available at `http://localhost:8002`
6. API documentation at `http://localhost:8002/docs`

### Option 2: Using Docker Compose

```bash
# Build and run the application
docker-compose up --build

# Run in background
docker-compose up -d

# Stop the application
docker-compose down
```

### Option 3: Local Development

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8002
```

## Development

### Debugging in Dev Container

1. Open the project in VS Code using Dev Container
2. Set breakpoints in your code
3. Use the debug configurations in `.vscode/launch.json`:
   - **FastAPI Debug**: Direct debugging of main.py
   - **FastAPI Debug with Uvicorn**: Debug with hot reload

### Project Structure

```
.
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI application
├── .devcontainer/
│   └── devcontainer.json # Dev container configuration
├── .vscode/
│   └── launch.json      # VS Code debug configuration
├── Dockerfile           # Docker image definition
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## API Usage Examples

### Create a TODO

```bash
curl -X POST "http://localhost:8002/todos" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Learn FastAPI",
       "description": "Study FastAPI documentation and build a project"
     }'
```

### Get all TODOs

```bash
curl "http://localhost:8002/todos"
```

### Update a TODO

```bash
curl -X PUT "http://localhost:8002/todos/{id}" \
     -H "Content-Type: application/json" \
     -d '{
       "completed": true
     }'
```

### Toggle completion status

```bash
curl -X PATCH "http://localhost:8002/todos/{id}/toggle"
```

## Environment Variables

- `PYTHONPATH`: Set to `/app` in container
- `PYTHONUNBUFFERED`: Set to `1` for immediate output

## Health Check

The application includes a health check endpoint at `/health` that returns the current status and timestamp.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the API
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
