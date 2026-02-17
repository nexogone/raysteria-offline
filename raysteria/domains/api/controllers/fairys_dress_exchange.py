from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class FairysDressExchangeController(Controller):
    path = "/fairys_dress_exchanges"
    tags = [localize("api", "fairys_dress_exchange_name")]

    @post(
        path="/chara_list",
        summary=localize("api", "fairys_dress_exchange_chara_list_summary"),
        description=localize("api", "fairys_dress_exchange_chara_list_desc"),
    )
    async def chara_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/item_list",
        summary=localize("api", "fairys_dress_exchange_item_list_summary"),
        description=localize("api", "fairys_dress_exchange_item_list_desc"),
    )
    async def item_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/generate",
        summary=localize("api", "fairys_dress_exchange_generate_summary"),
        description=localize("api", "fairys_dress_exchange_generate_desc"),
    )
    async def generate_(self, request: Request) -> Response:
        return offline_response(request)
