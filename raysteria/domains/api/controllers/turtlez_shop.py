from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class TurtlezShopController(Controller):
    path = "/turtlez_shops"
    tags = [localize("api", "turtlez_shop_name")]

    @post(
        path="/exchange",
        summary=localize("api", "turtlez_shop_exchange_summary"),
        description=localize("api", "turtlez_shop_exchange_desc"),
    )
    async def exchange_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/item_list",
        summary=localize("api", "turtlez_shop_item_list_summary"),
        description=localize("api", "turtlez_shop_item_list_desc"),
    )
    async def item_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/shop_list",
        summary=localize("api", "turtlez_shop_shop_list_summary"),
        description=localize("api", "turtlez_shop_shop_list_desc"),
    )
    async def shop_list_(self, request: Request) -> Response:
        return offline_response(request)
