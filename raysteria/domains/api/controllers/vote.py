from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class VoteController(Controller):
    path = "/votes"
    tags = [localize("api", "vote_name")]

    @post(
        path="/reward_list",
        summary=localize("api", "vote_reward_list_summary"),
        description=localize("api", "vote_reward_list_desc"),
    )
    async def reward_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_battle_condition",
        summary=localize("api", "vote_update_battle_condition_summary"),
        description=localize("api", "vote_update_battle_condition_desc"),
    )
    async def update_battle_condition_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_chara_group",
        summary=localize("api", "vote_update_chara_group_summary"),
        description=localize("api", "vote_update_chara_group_desc"),
    )
    async def update_chara_group_(self, request: Request) -> Response:
        return offline_response(request)
