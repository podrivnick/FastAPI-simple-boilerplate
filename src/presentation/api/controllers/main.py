from fastapi import FastAPI

from .default import default_router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(default_router)
