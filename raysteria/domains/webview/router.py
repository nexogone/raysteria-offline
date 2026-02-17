from litestar import Router

from raysteria.domains.webview import controllers
from raysteria.utils.api import dynamic_import

webview_router = Router(
    path="/game_server/webview",
    route_handlers=dynamic_import(controllers),
)
