from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class BattleCharaStampController(Controller):
    path = "/battle_chara_stamps"
    tags = [localize("api", "battle_chara_stamp_name")]

    @post(
        path="/trade_top",
        summary=localize("api", "battle_chara_stamp_trade_top_summary"),
        description=localize("api", "battle_chara_stamp_trade_top_desc"),
    )
    async def trade_top_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/stamp_list",
        summary=localize("api", "battle_chara_stamp_stamp_list_summary"),
        description=localize("api", "battle_chara_stamp_stamp_list_desc"),
    )
    async def stamp_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/random_trade_post",
        summary=localize("api", "battle_chara_stamp_random_trade_post_summary"),
        description=localize("api", "battle_chara_stamp_random_trade_post_desc"),
    )
    async def random_trade_post_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/random_trade_cancel",
        summary=localize("api", "battle_chara_stamp_random_trade_cancel_summary"),
        description=localize("api", "battle_chara_stamp_random_trade_cancel_desc"),
    )
    async def random_trade_cancel_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/random_trade_receive",
        summary=localize("api", "battle_chara_stamp_random_trade_receive_summary"),
        description=localize("api", "battle_chara_stamp_random_trade_receive_desc"),
    )
    async def random_trade_receive_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/friend_trade_post",
        summary=localize("api", "battle_chara_stamp_friend_trade_post_summary"),
        description=localize("api", "battle_chara_stamp_friend_trade_post_desc"),
    )
    async def friend_trade_post_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/friend_trade_cancel",
        summary=localize("api", "battle_chara_stamp_friend_trade_cancel_summary"),
        description=localize("api", "battle_chara_stamp_friend_trade_cancel_desc"),
    )
    async def friend_trade_cancel_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/friend_trade_receive",
        summary=localize("api", "battle_chara_stamp_friend_trade_receive_summary"),
        description=localize("api", "battle_chara_stamp_friend_trade_receive_desc"),
    )
    async def friend_trade_receive_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/friend_trade_search",
        summary=localize("api", "battle_chara_stamp_friend_trade_search_summary"),
        description=localize("api", "battle_chara_stamp_friend_trade_search_desc"),
    )
    async def friend_trade_search_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/friend_trade_exchange",
        summary=localize("api", "battle_chara_stamp_friend_trade_exchange_summary"),
        description=localize("api", "battle_chara_stamp_friend_trade_exchange_desc"),
    )
    async def friend_trade_exchange_(self, request: Request) -> Response:
        return offline_response(request)
