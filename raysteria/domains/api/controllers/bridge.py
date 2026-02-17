from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class BridgeController(Controller):
    path = "/bridges"
    tags = [localize("api", "bridge_name")]

    @post(
        path="/index",
        summary=localize("api", "bridge_index_summary"),
        description=localize("api", "bridge_index_desc"),
    )
    async def index_(self, request: Request) -> Response:
        return offline_response(request)
