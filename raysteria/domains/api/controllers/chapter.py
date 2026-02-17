from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class ChapterController(Controller):
    path = "/chapters"
    tags = [localize("api", "chapter_name")]

    @post(
        path="/list",
        summary=localize("api", "chapter_list_summary"),
        description=localize("api", "chapter_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/reset_quest_list",
        summary=localize("api", "chapter_reset_quest_list_summary"),
        description=localize("api", "chapter_reset_quest_list_desc"),
    )
    async def reset_quest_list_(self, request: Request) -> Response:
        return offline_response(request)
