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
        # uniwebview://combine.1.29a6ad32-3113-417b-8ec7-a15b44b51660
        # return render_template("templates/combine_exec.html")
        print("[DEBUG] Combine UUID:", combine_uuid)
        return not_implemented()

    @get(
        path="/combine_start/{combine_uuid: uuid}",
        summary=localize("webview", "transfer_combine_start_summary"),
        description=localize("webview", "transfer_combine_start_desc"),
    )
    async def combine_start_(self, combine_uuid: UUID) -> Response:
        # https://www.bandainamcoid.com/v2/oauth2/auth

        # client_id=tales_of_origin_and
        # redirect_uri=https://rays.toco.tales-ch.jp/game_server/webview/transfers/combine_exec/29a6ad32-3113-417b-8ec7-a15b44b51660
        # scope=JpGroupAll
        # return render_template("templates/combine_start.html")
        print("[DEBUG] Combine UUID:", combine_uuid)
        return not_implemented()

    @get(
        path="/transfer_exec/{transfer_uuid: uuid}",
        summary=localize("webview", "transfer_transfer_exec_summary"),
        description=localize("webview", "transfer_transfer_exec_desc"),
    )
    async def transfer_exec_(self, transfer_uuid: UUID) -> Response:
        # return render_template("templates/transfer_exec.html")
        print("[DEBUG] Transfer UUID:", transfer_uuid)
        return not_implemented()

    @get(
        path="/transfer_start/{transfer_uuid: uuid}",
        summary=localize("webview", "transfer_transfer_start_summary"),
        description=localize("webview", "transfer_transfer_start_desc"),
    )
    async def transfer_start_(self, transfer_uuid: UUID) -> Response:
        # https://www.bandainamcoid.com/v2/oauth2/auth

        # client_id=tales_of_origin_and
        # redirect_uri=https://rays.toco.tales-ch.jp/game_server/webview/transfers/transfer_exec/b99f4dcc-c77c-4000-bc6a-562071073466
        # scope=JpGroupAll
        # return render_template("templates/transfer_start.html")
        print("[DEBUG] Transfer UUID:", transfer_uuid)
        return not_implemented()
