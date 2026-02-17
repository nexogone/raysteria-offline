from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class GashaController(Controller):
    path = "/gashas"
    tags = [localize("api", "gasha_name")]

    @post(
        path="/execute_gasha",
        summary=localize("api", "gasha_execute_gasha_summary"),
        description=localize("api", "gasha_execute_gasha_desc"),
    )
    async def execute_gasha_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/grade_exchange_execute",
        summary=localize("api", "gasha_grade_exchange_execute_summary"),
        description=localize("api", "gasha_grade_exchange_execute_desc"),
    )
    async def grade_exchange_execute_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/grade_exchange_item_list",
        summary=localize("api", "gasha_grade_exchange_item_list_summary"),
        description=localize("api", "gasha_grade_exchange_item_list_desc"),
    )
    async def grade_exchange_item_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/grade_list",
        summary=localize("api", "gasha_grade_list_summary"),
        description=localize("api", "gasha_grade_list_desc"),
    )
    async def grade_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/grade_point_replacement",
        summary=localize("api", "gasha_grade_point_replacement_summary"),
        description=localize("api", "gasha_grade_point_replacement_desc"),
    )
    async def grade_point_replacement_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "gasha_list_summary"),
        description=localize("api", "gasha_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/precaution_statement",
        summary=localize("api", "gasha_precaution_statement_summary"),
        description=localize("api", "gasha_precaution_statement_desc"),
    )
    async def precaution_statement_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/rate_list",
        summary=localize("api", "gasha_rate_list_summary"),
        description=localize("api", "gasha_rate_list_desc"),
    )
    async def rate_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/step_rate_list",
        summary=localize("api", "gasha_step_rate_list_summary"),
        description=localize("api", "gasha_step_rate_list_desc"),
    )
    async def step_rate_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/surprise_ticket_precaution_statement",
        summary=localize("api", "gasha_surprise_ticket_precaution_statement_summary"),
        description=localize("api", "gasha_surprise_ticket_precaution_statement_desc"),
    )
    async def surprise_ticket_precaution_statement_(self, request: Request) -> Response:
        return offline_response(request)
