from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class PartyController(Controller):
    path = "/parties"
    tags = [localize("api", "party_name")]

    @post(
        path="/list",
        summary=localize("api", "party_list_summary"),
        description=localize("api", "party_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/recommend_equip",
        summary=localize("api", "party_recommend_equip_summary"),
        description=localize("api", "party_recommend_equip_desc"),
    )
    async def recommend_equip_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/recommend_equip_tower",
        summary=localize("api", "party_recommend_equip_tower_summary"),
        description=localize("api", "party_recommend_equip_tower_desc"),
    )
    async def recommend_equip_tower_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update",
        summary=localize("api", "party_update_summary"),
        description=localize("api", "party_update_desc"),
    )
    async def update_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_chara_restricted_party",
        summary=localize("api", "party_update_chara_restricted_party_summary"),
        description=localize("api", "party_update_chara_restricted_party_desc"),
    )
    async def update_chara_restricted_party_(self, request: Request) -> Response:
        return offline_response(request)
