from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class ShopController(Controller):
    path = "/shops"
    tags = [localize("api", "shop_name")]

    @post(
        path="/ap_recover",
        summary=localize("api", "shop_ap_recover_summary"),
        description=localize("api", "shop_ap_recover_desc"),
    )
    async def ap_recover_(self, request: Request) -> Response:
        return offline_response(request)
