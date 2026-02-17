from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class PassportController(Controller):
    path = "/passports"
    tags = [localize("api", "passport_name")]

    @post(
        path="/list",
        summary=localize("api", "passport_list_summary"),
        description=localize("api", "passport_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/purchase",
        summary=localize("api", "passport_purchase_summary"),
        description=localize("api", "passport_purchase_desc"),
    )
    async def purchase_(self, request: Request) -> Response:
        return offline_response(request)
