from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class FairysDressController(Controller):
    path = "/fairys_dresses"
    tags = [localize("api", "fairys_dress_name")]

    @post(
        path="/arte_reinforce",
        summary=localize("api", "fairys_dress_arte_reinforce_summary"),
        description=localize("api", "fairys_dress_arte_reinforce_desc"),
    )
    async def arte_reinforce_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "fairys_dress_list_summary"),
        description=localize("api", "fairys_dress_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/rarity_up",
        summary=localize("api", "fairys_dress_rarity_up_summary"),
        description=localize("api", "fairys_dress_rarity_up_desc"),
    )
    async def rarity_up_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/sell_piece",
        summary=localize("api", "fairys_dress_sell_piece_summary"),
        description=localize("api", "fairys_dress_sell_piece_desc"),
    )
    async def sell_piece_(self, request: Request) -> Response:
        return offline_response(request)
