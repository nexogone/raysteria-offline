from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class HonorController(Controller):
    path = "/honors"
    tags = [localize("api", "honor_name")]

    @post(
        path="/list",
        summary=localize("api", "honor_list_summary"),
        description=localize("api", "honor_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)
