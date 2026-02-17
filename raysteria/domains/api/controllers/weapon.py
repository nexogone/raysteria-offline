from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class WeaponController(Controller):
    path = "/weapons"
    tags = [localize("api", "weapon_name")]

    @post(
        path="/arte_reinforce",
        summary=localize("api", "weapon_arte_reinforce_summary"),
        description=localize("api", "weapon_arte_reinforce_desc"),
    )
    async def arte_reinforce_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/change_auto_available",
        summary=localize("api", "weapon_change_auto_available_summary"),
        description=localize("api", "weapon_change_auto_available_desc"),
    )
    async def change_auto_available_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/list",
        summary=localize("api", "weapon_list_summary"),
        description=localize("api", "weapon_list_desc"),
    )
    async def list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/mirrage_weapon_surface_list",
        summary=localize("api", "weapon_mirrage_weapon_surface_list_summary"),
        description=localize("api", "weapon_mirrage_weapon_surface_list_desc"),
    )
    async def mirrage_weapon_surface_list_(self, request: Request) -> Response:
        return offline_response(request)
