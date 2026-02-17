from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class RecollectionQuestController(Controller):
    path = "/recollection_quests"
    tags = [localize("api", "recollection_quest_name")]

    @post(
        path="/all_chara_equip",
        summary=localize("api", "recollection_quest_all_chara_equip_summary"),
        description=localize("api", "recollection_quest_all_chara_equip_desc"),
    )
    async def all_chara_equip_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/all_equip",
        summary=localize("api", "recollection_quest_all_equip_summary"),
        description=localize("api", "recollection_quest_all_equip_desc"),
    )
    async def all_equip_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/custom_chance",
        summary=localize("api", "recollection_quest_custom_chance_summary"),
        description=localize("api", "recollection_quest_custom_chance_desc"),
    )
    async def custom_chance_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/party_update",
        summary=localize("api", "recollection_quest_party_update_summary"),
        description=localize("api", "recollection_quest_party_update_desc"),
    )
    async def party_update_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/quest_list",
        summary=localize("api", "recollection_quest_quest_list_summary"),
        description=localize("api", "recollection_quest_quest_list_desc"),
    )
    async def quest_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/quest_other_status",
        summary=localize("api", "recollection_quest_quest_other_status_summary"),
        description=localize("api", "recollection_quest_quest_other_status_desc"),
    )
    async def quest_other_status_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/result",
        summary=localize("api", "recollection_quest_result_summary"),
        description=localize("api", "recollection_quest_result_desc"),
    )
    async def result_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/result_continue",
        summary=localize("api", "recollection_quest_result_continue_summary"),
        description=localize("api", "recollection_quest_result_continue_desc"),
    )
    async def result_continue_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/retire",
        summary=localize("api", "recollection_quest_retire_summary"),
        description=localize("api", "recollection_quest_retire_desc"),
    )
    async def retire_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/series_rankup_effect_save",
        summary=localize(
            "api", "recollection_quest_series_rankup_effect_save_summary"
        ),
        description=localize(
            "api", "recollection_quest_series_rankup_effect_save_desc"
        ),
    )
    async def series_rankup_effect_save_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/start",
        summary=localize("api", "recollection_quest_start_summary"),
        description=localize("api", "recollection_quest_start_desc"),
    )
    async def start_(self, request: Request) -> Response:
        return offline_response(request)
