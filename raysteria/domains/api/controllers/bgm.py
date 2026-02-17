from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class BGMController(Controller):
    path = "/bgms"
    tags = [localize("api", "bgm_name")]

    @post(
        path="/list",
        summary=localize("api", "bgm_list_summary"),
        description=localize("api", "bgm_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)
