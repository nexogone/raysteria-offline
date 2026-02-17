from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class TowerSkipTicketShopController(Controller):
    path = "/tower_skip_ticket_shops"
    tags = [localize("api", "tower_skip_ticket_shop_name")]

    @post(
        path="/list",
        summary=localize("api", "tower_skip_ticket_shop_list_summary"),
        description=localize("api", "tower_skip_ticket_shop_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/purchase",
        summary=localize("api", "tower_skip_ticket_shop_purchase_summary"),
        description=localize("api", "tower_skip_ticket_shop_purchase_desc"),
    )
    async def purchase_(self, request: Request) -> Response:
        return offline_response(request)
