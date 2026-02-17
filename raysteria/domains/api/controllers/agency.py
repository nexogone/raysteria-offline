from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class AgencyController(Controller):
    path = "/agencies"
    tags = [localize("api", "agency_name")]

    @post(
        path="/status",
        summary=localize("api", "agency_status_summary"),
        description=localize("api", "agency_status_desc"),
    )
    async def status_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "agency_list_summary"),
        description=localize("api", "agency_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/start",
        summary=localize("api", "agency_start_summary"),
        description=localize("api", "agency_start_desc"),
    )
    async def start_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/receive",
        summary=localize("api", "agency_receive_summary"),
        description=localize("api", "agency_receive_desc"),
    )
    async def receive_(self, request: Request) -> Response:
        return offline_response(request)
