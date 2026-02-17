from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class AutoLimitBreakController(Controller):
    path = "/auto_limit_breaks"
    tags = [localize("api", "auto_limit_break_name")]

    @post(
        path="/history",
        summary=localize("api", "auto_limit_break_history_summary"),
        description=localize("api", "auto_limit_break_history_desc"),
    )
    async def history_(self, request: Request) -> Response:
        return offline_response(request)
