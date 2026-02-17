from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class TowerController(Controller):
    path = "/towers"
    tags = [localize("api", "tower_name")]

    @post(
        path="/boost_add",
        summary=localize("api", "tower_boost_add_summary"),
        description=localize("api", "tower_boost_add_desc"),
    )
    async def boost_add_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/chara_skill_draw_lot",
        summary=localize("api", "tower_chara_skill_draw_lot_summary"),
        description=localize("api", "tower_chara_skill_draw_lot_desc"),
    )
    async def chara_skill_draw_lot_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/chara_skill_save",
        summary=localize("api", "tower_chara_skill_save_summary"),
        description=localize("api", "tower_chara_skill_save_desc"),
    )
    async def chara_skill_save_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/chara_skill_save_multi",
        summary=localize("api", "tower_chara_skill_save_multi_summary"),
        description=localize("api", "tower_chara_skill_save_multi_desc"),
    )
    async def chara_skill_save_multi_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/drop_out",
        summary=localize("api", "tower_drop_out_summary"),
        description=localize("api", "tower_drop_out_desc"),
    )
    async def drop_out_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/party_organize",
        summary=localize("api", "tower_party_organize_summary"),
        description=localize("api", "tower_party_organize_desc"),
    )
    async def party_organize_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/skip",
        summary=localize("api", "tower_skip_summary"),
        description=localize("api", "tower_skip_desc"),
    )
    async def skip_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/stage_clear",
        summary=localize("api", "tower_stage_clear_summary"),
        description=localize("api", "tower_stage_clear_desc"),
    )
    async def stage_clear_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/stage_start",
        summary=localize("api", "tower_stage_start_summary"),
        description=localize("api", "tower_stage_start_desc"),
    )
    async def stage_start_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/status",
        summary=localize("api", "tower_status_summary"),
        description=localize("api", "tower_status_desc"),
    )
    async def status_(self, request: Request) -> Response:
        return offline_response(request)
