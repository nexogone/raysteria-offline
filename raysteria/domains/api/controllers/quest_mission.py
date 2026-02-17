from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class QuestMissionController(Controller):
    path = "/quest_missions"
    tags = [localize("api", "quest_mission_name")]

    @post(
        path="/list",
        summary=localize("api", "quest_mission_list_summary"),
        description=localize("api", "quest_mission_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)
