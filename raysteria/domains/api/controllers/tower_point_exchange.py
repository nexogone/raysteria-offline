from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class TowerPointExchangeController(Controller):
    path = "/tower_point_exchanges"
    tags = [localize("api", "tower_point_exchange_name")]

    @post(
        path="/execute_item",
        summary=localize("api", "tower_point_exchange_execute_item_summary"),
        description=localize("api", "tower_point_exchange_execute_item_desc"),
    )
    async def execute_item_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/execute_skill",
        summary=localize("api", "tower_point_exchange_execute_skill_summary"),
        description=localize("api", "tower_point_exchange_execute_skill_desc"),
    )
    async def execute_skill_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/item_list",
        summary=localize("api", "tower_point_exchange_item_list_summary"),
        description=localize("api", "tower_point_exchange_item_list_desc"),
    )
    async def item_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/shop_list",
        summary=localize("api", "tower_point_exchange_shop_list_summary"),
        description=localize("api", "tower_point_exchange_shop_list_desc"),
    )
    async def shop_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/switch_chara_skill",
        summary=localize("api", "tower_point_exchange_switch_chara_skill_summary"),
        description=localize("api", "tower_point_exchange_switch_chara_skill_desc"),
    )
    async def switch_chara_skill_(self, request: Request) -> Response:
        return offline_response(request)
