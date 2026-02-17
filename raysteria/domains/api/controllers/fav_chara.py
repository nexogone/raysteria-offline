from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class FavCharaController(Controller):
    path = "/fav_chara"
    tags = [localize("api", "fav_chara_name")]

    @post(
        path="/list",
        summary=localize("api", "fav_chara_list_summary"),
        description=localize("api", "fav_chara_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update",
        summary=localize("api", "fav_chara_update_summary"),
        description=localize("api", "fav_chara_update_desc"),
    )
    async def update_(self, request: Request) -> Response:
        return offline_response(request)
