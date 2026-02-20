from uuid import UUID

from litestar import Controller, Response, get

from raysteria.utils.api import not_implemented
from raysteria.utils.i18n import localize


class TransfersController(Controller):
    path = "/transfers"
    tags = [localize("api", "transfer_name")]

    @get(
        path="/combine_exec/{combine_uuid: uuid}",
        summary=localize("webview", "transfer_combine_exec_summary"),
        description=localize("webview", "transfer_combine_exec_desc"),
    )
    async def combine_exec_(self, combine_uuid: UUID) -> Response:
        print("[DEBUG] Combine UUID:", combine_uuid)
        return not_implemented()

    @get(
        path="/combine_start/{combine_uuid: uuid}",
        summary=localize("webview", "transfer_combine_start_summary"),
        description=localize("webview", "transfer_combine_start_desc"),
    )
    async def combine_start_(self, combine_uuid: UUID) -> Response:
        print("[DEBUG] Combine UUID:", combine_uuid)
        return not_implemented()

    @get(
        path="/transfer_exec/{transfer_uuid: uuid}",
        summary=localize("webview", "transfer_transfer_exec_summary"),
        description=localize("webview", "transfer_transfer_exec_desc"),
    )
    async def transfer_exec_(self, transfer_uuid: UUID) -> Response:
        print("[DEBUG] Transfer UUID:", transfer_uuid)
        return not_implemented()

    @get(
        path="/transfer_start/{transfer_uuid: uuid}",
        summary=localize("webview", "transfer_transfer_start_summary"),
        description=localize("webview", "transfer_transfer_start_desc"),
    )
    async def transfer_start_(self, transfer_uuid: UUID) -> Response:
        print("[DEBUG] Transfer UUID:", transfer_uuid)
        return not_implemented()
