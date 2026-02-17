from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class MemorialEventTicketShopController(Controller):
    path = "/memorial_event_ticket_shops"
    tags = [localize("api", "memorial_event_ticket_shop_name")]

    @post(
        path="/check",
        summary=localize("api", "memorial_event_ticket_shop_check_summary"),
        description=localize("api", "memorial_event_ticket_shop_check_desc"),
    )
    async def check_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "memorial_event_ticket_shop_list_summary"),
        description=localize("api", "memorial_event_ticket_shop_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/purchase",
        summary=localize("api", "memorial_event_ticket_shop_purchase_summary"),
        description=localize("api", "memorial_event_ticket_shop_purchase_desc"),
    )
    async def purchase_(self, request: Request) -> Response:
        return offline_response(request)
