from litestar import Litestar

from raysteria.configs.compression import compression_config
from raysteria.configs.logging import logging_config
from raysteria.configs.openapi import openapi_config
from raysteria.configs.template import template_config
from raysteria.domains.api.router import api_router
from raysteria.domains.webview.router import webview_router
from raysteria.exceptions import exception_handlers


def create_app() -> Litestar:
    app = Litestar(
        route_handlers=[api_router, webview_router],
        compression_config=compression_config,
        exception_handlers=exception_handlers,
        openapi_config=openapi_config,
        template_config=template_config,
        logging_config=logging_config,
    )

    return app
