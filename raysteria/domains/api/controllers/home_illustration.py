from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class HomeIllustrationController(Controller):
    path = "/home_illustrations"
    tags = [localize("api", "home_illustration_name")]

    @post(
        path="/list",
        summary=localize("api", "home_illustration_list_summary"),
        description=localize("api", "home_illustration_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update",
        summary=localize("api", "home_illustration_update_summary"),
        description=localize("api", "home_illustration_update_desc"),
    )
    async def update_(self, request: Request) -> Response:
        return offline_response(request)
