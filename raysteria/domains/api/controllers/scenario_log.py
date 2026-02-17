from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class ScenarioLogController(Controller):
    path = "/scenario_logs"
    tags = [localize("api", "scenario_log_name")]

    @post(
        path="/chapters",
        summary=localize("api", "scenario_log_chapters_summary"),
        description=localize("api", "scenario_log_chapters_desc"),
    )
    async def chapters_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/episodes",
        summary=localize("api", "scenario_log_episodes_summary"),
        description=localize("api", "scenario_log_episodes_desc"),
    )
    async def episodes_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/memorial_events",
        summary=localize("api", "scenario_log_memorial_events_summary"),
        description=localize("api", "scenario_log_memorial_events_desc"),
    )
    async def memorial_events_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/rays2_episodes",
        summary=localize("api", "scenario_log_rays2_episodes_summary"),
        description=localize("api", "scenario_log_rays2_episodes_desc"),
    )
    async def rays2_episodes_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/rays2_scenario_play",
        summary=localize("api", "scenario_log_rays2_scenario_play_summary"),
        description=localize("api", "scenario_log_rays2_scenario_play_desc"),
    )
    async def rays2_scenario_play_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/scenario_play",
        summary=localize("api", "scenario_log_scenario_play_summary"),
        description=localize("api", "scenario_log_scenario_play_desc"),
    )
    async def scenario_play_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/sub_episodes",
        summary=localize("api", "scenario_log_sub_episodes_summary"),
        description=localize("api", "scenario_log_sub_episodes_desc"),
    )
    async def sub_episodes_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/sub_scenario_play",
        summary=localize("api", "scenario_log_sub_scenario_play_summary"),
        description=localize("api", "scenario_log_sub_scenario_play_desc"),
    )
    async def sub_scenario_play_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/top",
        summary=localize("api", "scenario_log_top_summary"),
        description=localize("api", "scenario_log_top_desc"),
    )
    async def top_(self, request: Request) -> Response:
        return offline_response(request)
