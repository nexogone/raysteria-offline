from litestar import Router

from raysteria.domains.api import controllers
from raysteria.utils.api import dynamic_import

api_router = Router(
    path="/game_server/api",
    route_handlers=dynamic_import(controllers),
)
