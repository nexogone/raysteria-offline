from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class KnockoutTowerController(Controller):
    path = "/knockout_towers"
    tags = [localize("api", "knockout_tower_name")]

    @post(
        path="/party_organize",
        summary=localize("api", "knockout_tower_party_organize_summary"),
        description=localize("api", "knockout_tower_party_organize_desc"),
    )
    async def party_organize_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/result",
        summary=localize("api", "knockout_tower_result_summary"),
        description=localize("api", "knockout_tower_result_desc"),
    )
    async def result_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/stage_clear",
        summary=localize("api", "knockout_tower_stage_clear_summary"),
        description=localize("api", "knockout_tower_stage_clear_desc"),
    )
    async def stage_clear_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/stage_start",
        summary=localize("api", "knockout_tower_stage_start_summary"),
        description=localize("api", "knockout_tower_stage_start_desc"),
    )
    async def stage_start_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/status",
        summary=localize("api", "knockout_tower_status_summary"),
        description=localize("api", "knockout_tower_status_desc"),
    )
    async def status_(self, request: Request) -> Response:
        return offline_response(request)
