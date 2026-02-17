from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class SupportController(Controller):
    path = "/supports"
    tags = [localize("api", "support_name")]

    @post(
        path="/candidate",
        summary=localize("api", "support_candidate_summary"),
        description=localize("api", "support_candidate_desc"),
    )
    async def candidate_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/lock",
        summary=localize("api", "support_lock_summary"),
        description=localize("api", "support_lock_desc"),
    )
    async def lock_(self, request: Request) -> Response:
        return offline_response(request)
