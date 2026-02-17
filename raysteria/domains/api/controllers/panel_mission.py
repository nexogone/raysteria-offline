from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class PanelMissionController(Controller):
    path = "/panel_missions"
    tags = [localize("api", "panel_mission_name")]

    @post(
        path="/receive",
        summary=localize("api", "panel_mission_receive_summary"),
        description=localize("api", "panel_mission_receive_desc"),
    )
    async def receive_(self, request: Request) -> Response:
        return offline_response(request)
