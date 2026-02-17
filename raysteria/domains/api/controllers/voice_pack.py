from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class VoicePackController(Controller):
    path = "/voice_packs"
    tags = [localize("api", "voice_pack_name")]

    @post(
        path="/list",
        summary=localize("api", "voice_pack_list_summary"),
        description=localize("api", "voice_pack_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)
