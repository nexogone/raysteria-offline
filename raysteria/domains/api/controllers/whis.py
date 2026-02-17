from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class WhisController(Controller):
    path = "/whises"
    tags = [localize("api", "whis_name")]

    @post(
        path="/start_friend_match",
        summary=localize("api", "whis_start_friend_match_summary"),
        description=localize("api", "whis_start_friend_match_desc"),
    )
    async def start_friend_match_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/start_single",
        summary=localize("api", "whis_start_single_summary"),
        description=localize("api", "whis_start_single_desc"),
    )
    async def start_single_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/status",
        summary=localize("api", "whis_status_summary"),
        description=localize("api", "whis_status_desc"),
    )
    async def status_(self, request: Request) -> Response:
        return offline_response(request)
