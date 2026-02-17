from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class CharaController(Controller):
    path = "/charas"
    tags = [localize("api", "chara_name")]

    @post(
        path="/list",
        summary=localize("api", "chara_list_summary"),
        description=localize("api", "chara_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/reinforce_list",
        summary=localize("api", "chara_reinforce_list_summary"),
        description=localize("api", "chara_reinforce_list_desc"),
    )
    async def reinforce_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/all_equip",
        summary=localize("api", "chara_all_equip_summary"),
        description=localize("api", "chara_all_equip_desc"),
    )
    async def all_equip_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/limit_break",
        summary=localize("api", "chara_limit_break_summary"),
        description=localize("api", "chara_limit_break_desc"),
    )
    async def limit_break_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/material_awake",
        summary=localize("api", "chara_material_awake_summary"),
        description=localize("api", "chara_material_awake_desc"),
    )
    async def material_awake_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/material_reinforce",
        summary=localize("api", "chara_material_reinforce_summary"),
        description=localize("api", "chara_material_reinforce_desc"),
    )
    async def material_reinforce_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/reinforce_equip_lv",
        summary=localize("api", "chara_reinforce_equip_lv_summary"),
        description=localize("api", "chara_reinforce_equip_lv_desc"),
    )
    async def reinforce_equip_lv_(self, request: Request) -> Response:
        return offline_response(request)
