from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class TutorialBeforeController(Controller):
    path = "/tutorial_befores"
    tags = [localize("api", "tutorial_before_name")]

    @post(
        path="/analyze",
        summary=localize("api", "tutorial_before_analyze_summary"),
        description=localize("api", "tutorial_before_analyze_desc"),
    )
    async def analyze_(self, request: Request) -> Response:
        return offline_response(request)
