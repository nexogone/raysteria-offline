from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class MemorialEventController(Controller):
    path = "/memorial_events"
    tags = [localize("api", "memorial_event_name")]

    @post(
        path="/event_list",
        summary=localize("api", "memorial_event_event_list_summary"),
        description=localize("api", "memorial_event_event_list_desc"),
    )
    async def event_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/force_end_event",
        summary=localize("api", "memorial_event_force_end_event_summary"),
        description=localize("api", "memorial_event_force_end_event_desc"),
    )
    async def force_end_event_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/revive_event",
        summary=localize("api", "memorial_event_revive_event_summary"),
        description=localize("api", "memorial_event_revive_event_desc"),
    )
    async def revive_event_(self, request: Request) -> Response:
        return offline_response(request)
