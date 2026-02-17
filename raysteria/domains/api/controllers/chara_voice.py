from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class CharaVoiceController(Controller):
    path = "/chara_voices"
    tags = [localize("api", "chara_voice_name")]

    @post(
        path="/edit",
        summary=localize("api", "chara_voice_edit_summary"),
        description=localize("api", "chara_voice_edit_desc"),
    )
    async def edit_(self, request: Request) -> Response:
        return offline_response(request)
