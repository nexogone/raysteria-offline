from litestar import Controller, Request, get
from litestar.response import Template

from raysteria.domains.webview.services.announce import AnnounceService
from raysteria.utils.i18n import localize


class AnnouncesController(Controller):
    path = "/announces"
    tags = [localize("api", "announce_name")]

    @get(
        path="/{announce_id: int}",
        summary=localize("webview", "announce_announces_summary"),
        description=localize("webview", "announce_announces_desc"),
    )
    async def announce_(
            self, request: Request, announce_id: int,
    ) -> Template:
        announce = AnnounceService(request)
        return await announce.view(announce_id)
