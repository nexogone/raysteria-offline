from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class JewelShopController(Controller):
    path = "/jewel_shops"
    tags = [localize("api", "jewel_shop_name")]

    @post(
        path="/execute",
        summary=localize("api", "jewel_shop_execute_summary"),
        description=localize("api", "jewel_shop_execute_desc"),
    )
    async def execute_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "jewel_shop_list_summary"),
        description=localize("api", "jewel_shop_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/order",
        summary=localize("api", "jewel_shop_order_summary"),
        description=localize("api", "jewel_shop_order_desc"),
    )
    async def order_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/prepare",
        summary=localize("api", "jewel_shop_prepare_summary"),
        description=localize("api", "jewel_shop_prepare_desc"),
    )
    async def prepare_(self, request: Request) -> Response:
        return offline_response(request)
