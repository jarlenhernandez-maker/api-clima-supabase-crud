from fastapi import FastAPI

from app.routes import api, pages


def create_app() -> FastAPI:
    app = FastAPI(
        title="API CRUD de Clima con Supabase",
        description=(
            "Proyecto en Python con FastAPI que consulta OpenWeatherMap y guarda, "
            "lee, actualiza y elimina registros en una base de datos Supabase."
        ),
        version="1.0.0",
    )
    app.include_router(pages.router)
    app.include_router(api.router)
    return app
