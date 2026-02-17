from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class DefenseBattleController(Controller):
    path = "/defense_battles"
    tags = [localize("api", "defense_battle_name")]

    @post(
        path="/top",
        summary=localize("api", "defense_battle_top_summary"),
        description=localize("api", "defense_battle_top_desc"),
    )
    async def top_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/start",
        summary=localize("api", "defense_battle_start_summary"),
        description=localize("api", "defense_battle_start_desc"),
    )
    async def start_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/result",
        summary=localize("api", "defense_battle_result_summary"),
        description=localize("api", "defense_battle_result_desc"),
    )
    async def result_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/rental_chara_list",
        summary=localize("api", "defense_battle_rental_chara_list_summary"),
        description=localize("api", "defense_battle_rental_chara_list_desc"),
    )
    async def rental_chara_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_stamp_setting",
        summary=localize("api", "defense_battle_update_stamp_setting_summary"),
        description=localize("api", "defense_battle_update_stamp_setting_desc"),
    )
    async def update_stamp_setting_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/matching_rate_update",
        summary=localize("api", "defense_battle_matching_rate_update_summary"),
        description=localize("api", "defense_battle_matching_rate_update_desc"),
    )
    async def matching_rate_update_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/setting_info",
        summary=localize("api", "defense_battle_setting_info_summary"),
        description=localize("api", "defense_battle_setting_info_desc"),
    )
    async def setting_info_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/latest_matching_rank",
        summary=localize("api", "defense_battle_latest_matching_rank_summary"),
        description=localize("api", "defense_battle_latest_matching_rank_desc"),
    )
    async def latest_matching_rank_(self, request: Request) -> Response:
        return offline_response(request)
