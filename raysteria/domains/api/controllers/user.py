from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class UserController(Controller):
    path = "/users"
    tags = [localize("api", "user_name")]

    @post(
        path="/prepare",
        summary=localize("api", "user_prepare_summary"),
        description=localize("api", "user_prepare_desc"),
    )
    async def prepare_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/create",
        summary=localize("api", "user_create_summary"),
        description=localize("api", "user_create_desc"),
    )
    async def create_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/login",
        summary=localize("api", "user_login_summary"),
        description=localize("api", "user_login_desc"),
    )
    async def login_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/status",
        summary=localize("api", "user_status_summary"),
        description=localize("api", "user_status_desc"),
    )
    async def status_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/request_name",
        summary=localize("api", "user_request_name_summary"),
        description=localize("api", "user_request_name_desc"),
    )
    async def request_name_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_name",
        summary=localize("api", "user_update_name_summary"),
        description=localize("api", "user_update_name_desc"),
    )
    async def update_name_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/request_message",
        summary=localize("api", "user_request_message_summary"),
        description=localize("api", "user_request_message_desc"),
    )
    async def request_message_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_message",
        summary=localize("api", "user_update_message_summary"),
        description=localize("api", "user_update_message_desc"),
    )
    async def update_message_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/update_honor",
        summary=localize("api", "user_update_honor_summary"),
        description=localize("api", "user_update_honor_desc"),
    )
    async def update_honor_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/change_scenario_part",
        summary=localize("api", "user_change_scenario_part_summary"),
        description=localize("api", "user_change_scenario_part_desc"),
    )
    async def change_scenario_part_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/rays_data_order1",
        summary=localize("api", "user_rays_data_order1_summary"),
        description=localize("api", "user_rays_data_order1_desc"),
    )
    async def rays_data_order1_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/rays_data_order2",
        summary=localize("api", "user_rays_data_order2_summary"),
        description=localize("api", "user_rays_data_order2_desc"),
    )
    async def rays_data_order2_(self, request: Request) -> Response:
        return offline_response(request)
