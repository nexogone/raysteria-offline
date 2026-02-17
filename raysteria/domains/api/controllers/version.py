from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class VersionController(Controller):
    path = "/versions"
    tags = [localize("api", "version_name")]

    @post(
        path="/info",
        summary=localize("api", "version_info_summary"),
        description=localize("api", "version_info_desc"),
    )
    async def info_(self, request: Request) -> Response:
        return offline_response(request)
