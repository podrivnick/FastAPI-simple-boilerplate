import uvicorn
from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from src.presentation.api.controllers import setup_controllers
from src.presentation.api.middlewares.main import setup_middleware
from src.presentation.api.providers import setup_providers

from .config import APIConfig


origins = [
    "*",
]


def init_api(
    mediator: Mediator,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
    debug: bool = __debug__,
) -> FastAPI:
    app = FastAPI(
        debug=debug,
        title="User service",
        version="1.0.0",
        default_response_class=ORJSONResponse,
    )
    setup_providers(app, mediator, di_builder, di_state)
    setup_middleware(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
        allow_headers=[
            "Content-Type",
            "Set-Cookie",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin",
            "Authorization",
        ],
    )

    setup_controllers(app)

    return app


async def run_api(
    app: FastAPI,
    api_config: APIConfig,
) -> None:
    config = uvicorn.Config(
        app,
        host=api_config.host,
        port=api_config.port,
        workers=4,
    )
    server = uvicorn.Server(config)

    await server.serve()
