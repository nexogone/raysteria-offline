from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class TransferController(Controller):
    path = "/transfers"
    tags = [localize("api", "transfer_name")]

    @post(
        path="/combine_prepare",
        summary=localize("api", "transfer_combine_prepare_summary"),
        description=localize("api", "transfer_combine_prepare_desc"),
    )
    async def combine_prepare_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/combine_remove",
        summary=localize("api", "transfer_combine_remove_summary"),
        description=localize("api", "transfer_combine_remove_desc"),
    )
    async def combine_remove_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/transfer_prepare",
        summary=localize("api", "transfer_transfer_prepare_summary"),
        description=localize("api", "transfer_transfer_prepare_desc"),
    )
    async def transfer_prepare_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/transfer_complete",
        summary=localize("api", "transfer_transfer_complete_summary"),
        description=localize("api", "transfer_transfer_complete_desc"),
    )
    async def transfer_complete_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/setup_info",
        summary=localize("api", "transfer_setup_info_summary"),
        description=localize("api", "transfer_setup_info_desc"),
    )
    async def setup_info_(self, request: Request) -> Response:
        return offline_response(request)
