from fastapi import FastAPI
from .container import Container
from app.endpoints.users_router import router


def create_app(
        title: str,
        version: str
) -> FastAPI:

    container = Container()

    app = FastAPI(
        title=title,
        version=version
    )
    app.container = container
    app.include_router(router, prefix="/users", tags=["users"])

    return app
