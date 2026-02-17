from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class QuestCurrentController(Controller):
    path = "/quest_currents"
    tags = [localize("api", "quest_current_name")]

    @post(
        path="/status",
        summary=localize("api", "quest_current_status_summary"),
        description=localize("api", "quest_current_status_desc"),
    )
    async def status_(self, request: Request) -> Response:
        return offline_response(request)
