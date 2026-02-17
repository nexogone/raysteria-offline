from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class FriendController(Controller):
    path = "/friends"
    tags = [localize("api", "friend_name")]

    @post(
        path="/follow",
        summary=localize("api", "friend_follow_summary"),
        description=localize("api", "friend_follow_desc"),
    )
    async def follow_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "friend_list_summary"),
        description=localize("api", "friend_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/search",
        summary=localize("api", "friend_search_summary"),
        description=localize("api", "friend_search_desc"),
    )
    async def search_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/unfollow",
        summary=localize("api", "friend_unfollow_summary"),
        description=localize("api", "friend_unfollow_desc"),
    )
    async def unfollow_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/unfollower",
        summary=localize("api", "friend_unfollower_summary"),
        description=localize("api", "friend_unfollower_desc"),
    )
    async def unfollower_(self, request: Request) -> Response:
        return offline_response(request)
