 
from __future__ import annotations
from fastapi.openapi.utils import get_openapi

def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Prueba Arkdata",
        version="1.0.0",
        description="Esta API Una prueba para Arkdata",
        routes=app.routes
    )
    try:
        if openapi_schema["components"]["schemas"]["HTTPValidationError"]:
            openapi_schema["components"]["schemas"].pop("HTTPValidationError")
        if openapi_schema["components"]["schemas"]["ValidationError"]:
            openapi_schema["components"]["schemas"].pop("ValidationError")
    except Exception as e:
        # TODO: Logging exception
        ...

    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            if openapi_schema["paths"][path][method]["responses"].get("422"):
                openapi_schema["paths"][path][method]["responses"].pop("422")

    app.openapi_schema = openapi_schema

    return app.openapi_schema