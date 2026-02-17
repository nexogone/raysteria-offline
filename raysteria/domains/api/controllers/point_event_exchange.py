from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class PointEventExchangeController(Controller):
    path = "/point_event_exchanges"
    tags = [localize("api", "point_event_exchange_name")]

    @post(
        path="/execute",
        summary=localize("api", "point_event_exchange_execute_summary"),
        description=localize("api", "point_event_exchange_execute_desc"),
    )
    async def execute_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "point_event_exchange_list_summary"),
        description=localize("api", "point_event_exchange_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/top",
        summary=localize("api", "point_event_exchange_top_summary"),
        description=localize("api", "point_event_exchange_top_desc"),
    )
    async def top_(self, request: Request) -> Response:
        return offline_response(request)
