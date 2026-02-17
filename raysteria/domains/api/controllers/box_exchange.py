from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class BoxExchangeController(Controller):
    path = "/box_exchanges"
    tags = [localize("api", "box_exchange_name")]

    @post(
        path="/list",
        summary=localize("api", "box_exchange_list_summary"),
        description=localize("api", "box_exchange_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/execute",
        summary=localize("api", "box_exchange_execute_summary"),
        description=localize("api", "box_exchange_execute_desc"),
    )
    async def execute_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/complete",
        summary=localize("api", "box_exchange_complete_summary"),
        description=localize("api", "box_exchange_complete_desc"),
    )
    async def complete_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/reset",
        summary=localize("api", "box_exchange_reset_summary"),
        description=localize("api", "box_exchange_reset_desc"),
    )
    async def reset_(self, request: Request) -> Response:
        return offline_response(request)
