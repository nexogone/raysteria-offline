from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class ClessGymController(Controller):
    path = "/cless_gyms"
    tags = [localize("api", "cless_gym_name")]

    @post(
        path="/chara_equip_list",
        summary=localize("api", "cless_gym_chara_equip_list_summary"),
        description=localize("api", "cless_gym_chara_equip_list_desc"),
    )
    async def chara_equip_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/start_training",
        summary=localize("api", "cless_gym_start_training_summary"),
        description=localize("api", "cless_gym_start_training_desc"),
    )
    async def start_training_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/end_training",
        summary=localize("api", "cless_gym_end_training_summary"),
        description=localize("api", "cless_gym_end_training_desc"),
    )
    async def end_training_(self, request: Request) -> Response:
        return offline_response(request)
