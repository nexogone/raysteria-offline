from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class Rays2ScenarioController(Controller):
    path = "/rays2_scenarios"
    tags = [localize("api", "rays2_scenario_name")]

    @post(
        path="/episode_play",
        summary=localize("api", "rays2_scenario_episode_play_summary"),
        description=localize("api", "rays2_scenario_episode_play_desc"),
    )
    async def episode_play_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/party_update",
        summary=localize("api", "rays2_scenario_party_update_summary"),
        description=localize("api", "rays2_scenario_party_update_desc"),
    )
    async def party_update_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/quest_clear",
        summary=localize("api", "rays2_scenario_quest_clear_summary"),
        description=localize("api", "rays2_scenario_quest_clear_desc"),
    )
    async def quest_clear_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/quest_list",
        summary=localize("api", "rays2_scenario_quest_list_summary"),
        description=localize("api", "rays2_scenario_quest_list_desc"),
    )
    async def quest_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/quest_start",
        summary=localize("api", "rays2_scenario_quest_start_summary"),
        description=localize("api", "rays2_scenario_quest_start_desc"),
    )
    async def quest_start_(self, request: Request) -> Response:
        return offline_response(request)
