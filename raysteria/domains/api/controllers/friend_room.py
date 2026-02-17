from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class FriendRoomController(Controller):
    path = "/friend_rooms"
    tags = [localize("api", "friend_room_name")]

    @post(
        path="/random_room",
        summary=localize("api", "friend_room_random_room_summary"),
        description=localize("api", "friend_room_random_room_desc"),
    )
    async def random_room_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/top",
        summary=localize("api", "friend_room_top_summary"),
        description=localize("api", "friend_room_top_desc"),
    )
    async def top_(self, request: Request) -> Response:
        return offline_response(request)
