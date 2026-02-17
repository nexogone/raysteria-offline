from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class GalleryController(Controller):
    path = "/galleries"
    tags = [localize("api", "gallery_name")]

    @post(
        path="/illustration_list",
        summary=localize("api", "gallery_illustration_list_summary"),
        description=localize("api", "gallery_illustration_list_desc"),
    )
    async def illustration_list_(self, request: Request) -> Response:
        return offline_response(request)
