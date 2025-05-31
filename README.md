# Talent GPT Server

This is the FastAPI backend server for the Talent GPT application.

## Setup

### Option 1: Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --reload
```

### Option 2: Docker Development

1. Build and start the containers:
```bash
docker-compose up --build
```

The server will start at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Available Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint

## Development with Docker

The Docker setup includes:
- Hot-reloading enabled (changes to the code will automatically restart the server)
- Volume mounting for live code updates
- Python path configured correctly
- Port 8000 exposed for API access 