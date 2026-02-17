from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class MagicalMirrorController(Controller):
    path = "/magical_mirrors"
    tags = [localize("api", "magical_mirror_name")]

    @post(
        path="/activate_fairys_dress",
        summary=localize("api", "magical_mirror_activate_fairys_dress_summary"),
        description=localize("api", "magical_mirror_activate_fairys_dress_desc"),
    )
    async def activate_fairys_dress_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/burst_limit_unlock",
        summary=localize("api", "magical_mirror_burst_limit_unlock_summary"),
        description=localize("api", "magical_mirror_burst_limit_unlock_desc"),
    )
    async def burst_limit_unlock_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "magical_mirror_list_summary"),
        description=localize("api", "magical_mirror_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/mirrorge_arte_reinforce",
        summary=localize("api", "magical_mirror_mirrorge_arte_reinforce_summary"),
        description=localize("api", "magical_mirror_mirrorge_arte_reinforce_desc"),
    )
    async def mirrorge_arte_reinforce_(self, request: Request) -> Response:
        return offline_response(request)
