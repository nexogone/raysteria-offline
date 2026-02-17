from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class JewelOfferController(Controller):
    path = "/jewel_offer"
    tags = [localize("api", "jewel_offer_name")]

    @post(
        path="/check_popup_offer",
        summary=localize("api", "jewel_offer_check_popup_offer_summary"),
        description=localize("api", "jewel_offer_check_popup_offer_desc"),
    )
    async def check_popup_offer_(self, request: Request) -> Response:
        return offline_response(request)
