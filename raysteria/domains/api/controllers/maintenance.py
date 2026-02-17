from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class MaintenanceController(Controller):
    path = "/maintenances"
    tags = [localize("api", "maintenance_name")]

    @post(
        path="/check",
        summary=localize("api", "maintenance_check_summary"),
        description=localize("api", "maintenance_check_desc"),
    )
    async def check_(self, request: Request) -> Response:
        return offline_response(request)
