from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class RecollectionEpisodeController(Controller):
    path = "/recollection_episodes"
    tags = [localize("api", "recollection_episode_name")]

    @post(
        path="/list",
        summary=localize("api", "recollection_episode_list_summary"),
        description=localize("api", "recollection_episode_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/play",
        summary=localize("api", "recollection_episode_play_summary"),
        description=localize("api", "recollection_episode_play_desc"),
    )
    async def play_(self, request: Request) -> Response:
        return offline_response(request)
