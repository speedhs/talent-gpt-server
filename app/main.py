from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

from app.docs.swagger import custom_openapi
from app.routes import profile, company, chat, query, candidates, recruiter
from .database import db

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Talent GPT API",
    description="API for AI-powered recruitment platform",
    version="1.0.0",
    docs_url=None,  # Disable default docs
    redoc_url=None  # Disable default redoc
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
@app.on_event("startup")
async def startup_event():
    """Initialize database connection on startup."""
    mongodb_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    db.init_db(mongodb_url)

@app.on_event("shutdown")
async def shutdown_event():
    """Close database connection on shutdown."""
    db.close_db()

# Custom Swagger UI endpoint
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Talent GPT API Documentation",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css",
    )

# OpenAPI schema endpoint
@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_endpoint():
    return custom_openapi(app)

# Import and include routers
app.include_router(profile.router, prefix="/api", tags=["Profile"])
app.include_router(company.router, prefix="/api", tags=["Company"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(query.router, prefix="/api", tags=["Query"])
app.include_router(candidates.router, prefix="/api", tags=["Candidates"])
app.include_router(recruiter.router, prefix="/api", tags=["Recruiter"])

@app.get("/")
async def root():
    """Root endpoint to verify API is running."""
    return {"message": "Welcome to Talent GPT API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 