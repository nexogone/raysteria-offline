from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class ChallengeTowerController(Controller):
    path = "/challenge_towers"
    tags = [localize("api", "challenge_tower_name")]

    @post(
        path="/status",
        summary=localize("api", "challenge_tower_status_summary"),
        description=localize("api", "challenge_tower_status_desc"),
    )
    async def status_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/party_organize",
        summary=localize("api", "challenge_tower_party_organize_summary"),
        description=localize("api", "challenge_tower_party_organize_desc"),
    )
    async def party_organize_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/party_ranking",
        summary=localize("api", "challenge_tower_party_ranking_summary"),
        description=localize("api", "challenge_tower_party_ranking_desc"),
    )
    async def party_ranking_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/chara_ranking",
        summary=localize("api", "challenge_tower_chara_ranking_summary"),
        description=localize("api", "challenge_tower_chara_ranking_desc"),
    )
    async def chara_ranking_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/start",
        summary=localize("api", "challenge_tower_start_summary"),
        description=localize("api", "challenge_tower_start_desc"),
    )
    async def start_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/clear",
        summary=localize("api", "challenge_tower_clear_summary"),
        description=localize("api", "challenge_tower_clear_desc"),
    )
    async def clear_(self, request: Request) -> Response:
        return offline_response(request)
