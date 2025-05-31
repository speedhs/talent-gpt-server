FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    fastapi==0.104.1 \
    uvicorn==0.24.0 \
    motor==3.3.1 \
    pymongo==4.6.1 \
    python-dotenv==1.0.0 \
    pydantic==2.4.2 \
    python-multipart==0.0.6 \
    email-validator

EXPOSE 8000

# The actual application code will be mounted as a volume
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 