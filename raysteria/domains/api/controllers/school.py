from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class SchoolController(Controller):
    path = "/schools"
    tags = [localize("api", "school_name")]

    @post(
        path="/detail",
        summary=localize("api", "school_detail_summary"),
        description=localize("api", "school_detail_desc"),
    )
    async def detail_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "school_list_summary"),
        description=localize("api", "school_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update",
        summary=localize("api", "school_update_summary"),
        description=localize("api", "school_update_desc"),
    )
    async def update_(self, request: Request) -> Response:
        return offline_response(request)
