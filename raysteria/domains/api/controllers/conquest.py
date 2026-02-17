from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class ConquestController(Controller):
    path = "/conquests"
    tags = [localize("api", "conquest_name")]

    @post(
        path="/reward_list",
        summary=localize("api", "conquest_reward_list_summary"),
        description=localize("api", "conquest_reward_list_desc"),
    )
    async def reward_list_(self, request: Request) -> Response:
        return offline_response(request)
