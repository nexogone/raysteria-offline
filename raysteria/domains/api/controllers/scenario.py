from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class ScenarioController(Controller):
    path = "/scenarios"
    tags = [localize("api", "scenario_name")]

    @post(
        path="/list",
        summary=localize("api", "scenario_list_summary"),
        description=localize("api", "scenario_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)
