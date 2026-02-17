from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class AnnounceController(Controller):
    path = "/announces"
    tags = [localize("api", "announce_name")]

    @post(
        path="/list",
        summary=localize("api", "announce_list_summary"),
        description=localize("api", "announce_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)
