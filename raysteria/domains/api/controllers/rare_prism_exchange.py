from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class RarePrismExchangeController(Controller):
    path = "/rare_prism_exchanges"
    tags = [localize("api", "rare_prism_exchange_name")]

    @post(
        path="/execute",
        summary=localize("api", "rare_prism_exchange_execute_summary"),
        description=localize("api", "rare_prism_exchange_execute_desc"),
    )
    async def execute_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "rare_prism_exchange_list_summary"),
        description=localize("api", "rare_prism_exchange_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)
