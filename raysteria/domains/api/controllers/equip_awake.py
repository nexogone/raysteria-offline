from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class EquipAwakeController(Controller):
    path = "/equip_awakes"
    tags = [localize("api", "equip_awake_name")]

    @post(
        path="/chara_list",
        summary=localize("api", "equip_awake_chara_list_summary"),
        description=localize("api", "equip_awake_chara_list_desc"),
    )
    async def chara_list_(self, request: Request) -> Response:
        return offline_response(request)
