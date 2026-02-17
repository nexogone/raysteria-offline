from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class KnockoutTowerPointExchangeController(Controller):
    path = "/knockout_tower_point_exchanges"
    tags = [localize("api", "knockout_tower_point_exchange_name")]

    @post(
        path="/execute",
        summary=localize("api", "knockout_tower_point_exchange_execute_summary"),
        description=localize("api", "knockout_tower_point_exchange_execute_desc"),
    )
    async def execute_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/execute_equip_awake",
        summary=localize("api", "knockout_tower_point_exchange_execute_equip_awake_summary"),
        description=localize("api", "knockout_tower_point_exchange_execute_equip_awake_desc"),
    )
    async def execute_equip_awake_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/item_list",
        summary=localize("api", "knockout_tower_point_exchange_item_list_summary"),
        description=localize("api", "knockout_tower_point_exchange_item_list_desc"),
    )
    async def item_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/shop_list",
        summary=localize("api", "knockout_tower_point_exchange_shop_list_summary"),
        description=localize("api", "knockout_tower_point_exchange_shop_list_desc"),
    )
    async def shop_list_(self, request: Request) -> Response:
        return offline_response(request)
