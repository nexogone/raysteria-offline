from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class QuestController(Controller):
    path = "/quests"
    tags = [localize("api", "quest_name")]

    @post(
        path="/clear",
        summary=localize("api", "quest_clear_summary"),
        description=localize("api", "quest_clear_desc"),
    )
    async def clear_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/continue",
        summary=localize("api", "quest_continue_summary"),
        description=localize("api", "quest_continue_desc"),
    )
    async def continue_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "quest_list_summary"),
        description=localize("api", "quest_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/retire",
        summary=localize("api", "quest_retire_summary"),
        description=localize("api", "quest_retire_desc"),
    )
    async def retire_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/skill_quest_prepare",
        summary=localize("api", "quest_skill_quest_prepare_summary"),
        description=localize("api", "quest_skill_quest_prepare_desc"),
    )
    async def skill_quest_prepare_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/start",
        summary=localize("api", "quest_start_summary"),
        description=localize("api", "quest_start_desc"),
    )
    async def start_(self, request: Request) -> Response:
        return offline_response(request)
