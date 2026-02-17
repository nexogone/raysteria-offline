from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class GiftController(Controller):
    path = "/gifts"
    tags = [localize("api", "gift_name")]

    @post(
        path="/give_gift",
        summary=localize("api", "gift_give_gift_summary"),
        description=localize("api", "gift_give_gift_desc"),
    )
    async def give_gift_(self, request: Request) -> Response:
        return offline_response(request)
