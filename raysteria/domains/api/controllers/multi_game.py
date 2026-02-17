from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class MultiGameController(Controller):
    path = "/multi_games"
    tags = [localize("api", "multi_game_name")]

    @post(
        path="/top",
        summary=localize("api", "multi_game_top_summary"),
        description=localize("api", "multi_game_top_desc"),
    )
    async def top_(self, request: Request) -> Response:
        return offline_response(request)
