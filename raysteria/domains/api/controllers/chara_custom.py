from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class CharaCustomController(Controller):
    path = "/chara_customs"
    tags = [localize("api", "chara_custom_name")]

    @post(
        path="/chara_list",
        summary=localize("api", "chara_custom_chara_list_summary"),
        description=localize("api", "chara_custom_chara_list_desc"),
    )
    async def chara_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/equip_list",
        summary=localize("api", "chara_custom_equip_list_summary"),
        description=localize("api", "chara_custom_equip_list_desc"),
    )
    async def equip_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/item_list",
        summary=localize("api", "chara_custom_item_list_summary"),
        description=localize("api", "chara_custom_item_list_desc"),
    )
    async def item_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/equipments",
        summary=localize("api", "chara_custom_equipments_summary"),
        description=localize("api", "chara_custom_equipments_desc"),
    )
    async def equipments_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/exchanges",
        summary=localize("api", "chara_custom_exchanges_summary"),
        description=localize("api", "chara_custom_exchanges_desc"),
    )
    async def exchanges_(self, request: Request) -> Response:
        return offline_response(request)
