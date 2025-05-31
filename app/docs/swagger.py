from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI

def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Talent GPT API",
        version="1.0.0",
        description="""
        Talent GPT API for recruitment automation.
        
        ## Features
        * Recruiter profile management
        * Company information management
        * Chat session handling
        * Candidate matching
        * Recruiter agent integration
        
        ## Authentication
        All endpoints require authentication using JWT tokens.
        """,
        routes=app.routes,
    )

    # Add security scheme
    openapi_schema["components"] = {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
    }

    # Add security requirement to all endpoints
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation["security"] = [{"bearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema 