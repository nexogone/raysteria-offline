from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class PossessionItemController(Controller):
    path = "/possession_items"
    tags = [localize("api", "possession_item_name")]

    @post(
        path="/possession_items",
        summary=localize("api", "possession_item_possession_items_summary"),
        description=localize("api", "possession_item_possession_items_desc"),
    )
    async def possession_items_(self, request: Request) -> Response:
        return offline_response(request)
