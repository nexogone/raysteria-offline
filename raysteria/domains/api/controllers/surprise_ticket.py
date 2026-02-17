from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class SurpriseTicketController(Controller):
    path = "/surprise_tickets"
    tags = [localize("api", "surprise_ticket_name")]

    @post(
        path="/exchange",
        summary=localize("api", "surprise_ticket_exchange_summary"),
        description=localize("api", "surprise_ticket_exchange_desc"),
    )
    async def exchange_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/exchange_list",
        summary=localize("api", "surprise_ticket_exchange_list_summary"),
        description=localize("api", "surprise_ticket_exchange_list_desc"),
    )
    async def exchange_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "surprise_ticket_list_summary"),
        description=localize("api", "surprise_ticket_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)
