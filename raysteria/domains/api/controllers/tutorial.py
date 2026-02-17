from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class TutorialController(Controller):
    path = "/tutorials"
    tags = [localize("api", "tutorial_name")]

    @post(
        path="/again",
        summary=localize("api", "tutorial_again_summary"),
        description=localize("api", "tutorial_again_desc"),
    )
    async def again_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_phase",
        summary=localize("api", "tutorial_update_phase_summary"),
        description=localize("api", "tutorial_update_phase_desc"),
    )
    async def update_phase_(self, request: Request) -> Response:
        return offline_response(request)
