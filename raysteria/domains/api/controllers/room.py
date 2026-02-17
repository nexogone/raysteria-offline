from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class RoomController(Controller):
    path = "/rooms"
    tags = [localize("api", "room_name")]

    @post(
        path="/interior_list",
        summary=localize("api", "room_interior_list_summary"),
        description=localize("api", "room_interior_list_desc"),
    )
    async def interior_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/message_delete",
        summary=localize("api", "room_message_delete_summary"),
        description=localize("api", "room_message_delete_desc"),
    )
    async def message_delete_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/message_list",
        summary=localize("api", "room_message_list_summary"),
        description=localize("api", "room_message_list_desc"),
    )
    async def message_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/message_post",
        summary=localize("api", "room_message_post_summary"),
        description=localize("api", "room_message_post_desc"),
    )
    async def message_post_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/poster_list",
        summary=localize("api", "room_poster_list_summary"),
        description=localize("api", "room_poster_list_desc"),
    )
    async def poster_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/receive_bonus",
        summary=localize("api", "room_receive_bonus_summary"),
        description=localize("api", "room_receive_bonus_desc"),
    )
    async def receive_bonus_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/receive_trophy_reward",
        summary=localize("api", "room_receive_trophy_reward_summary"),
        description=localize("api", "room_receive_trophy_reward_desc"),
    )
    async def receive_trophy_reward_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/top",
        summary=localize("api", "room_top_summary"),
        description=localize("api", "room_top_desc"),
    )
    async def top_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/trophy_list",
        summary=localize("api", "room_trophy_list_summary"),
        description=localize("api", "room_trophy_list_desc"),
    )
    async def trophy_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_chara",
        summary=localize("api", "room_update_chara_summary"),
        description=localize("api", "room_update_chara_desc"),
    )
    async def update_chara_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_interior",
        summary=localize("api", "room_update_interior_summary"),
        description=localize("api", "room_update_interior_desc"),
    )
    async def update_interior_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_poster",
        summary=localize("api", "room_update_poster_summary"),
        description=localize("api", "room_update_poster_desc"),
    )
    async def update_poster_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_trophy",
        summary=localize("api", "room_update_trophy_summary"),
        description=localize("api", "room_update_trophy_desc"),
    )
    async def update_trophy_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_welcome_chara_order",
        summary=localize("api", "room_update_welcome_chara_order_summary"),
        description=localize("api", "room_update_welcome_chara_order_desc"),
    )
    async def update_welcome_chara_order_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_room_setting",
        summary=localize("api", "room_update_room_setting_summary"),
        description=localize("api", "room_update_room_setting_desc"),
    )
    async def update_room_setting_(self, request: Request) -> Response:
        return offline_response(request)
