from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class ProfileController(Controller):
    path = "/profiles"
    tags = [localize("api", "profile_name")]

    @post(
        path="/info",
        summary=localize("api", "profile_info_summary"),
        description=localize("api", "profile_info_desc"),
    )
    async def info_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_profile",
        summary=localize("api", "profile_update_profile_summary"),
        description=localize("api", "profile_update_profile_desc"),
    )
    async def update_profile_(self, request: Request) -> Response:
        return offline_response(request)
