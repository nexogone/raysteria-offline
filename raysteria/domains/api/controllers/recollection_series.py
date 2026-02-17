from litestar import Controller, Request, Response, post

from raysteria.utils.api import offline_response
from raysteria.utils.i18n import localize


class RecollectionSeriesController(Controller):
    path = "/recollection_series"
    tags = [localize("api", "recollection_series_name")]

    @post(
        path="/challenge_count_recover",
        summary=localize("api", "recollection_series_challenge_count_recover_summary"),
        description=localize("api", "recollection_series_challenge_count_recover_desc"),
    )
    async def challenge_count_recover_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/chara_equip_list",
        summary=localize("api", "recollection_series_chara_equip_list_summary"),
        description=localize("api", "recollection_series_chara_equip_list_desc"),
    )
    async def chara_equip_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/series_list",
        summary=localize("api", "recollection_series_series_list_summary"),
        description=localize("api", "recollection_series_series_list_desc"),
    )
    async def series_list_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/tutorial_end",
        summary=localize("api", "recollection_series_tutorial_end_summary"),
        description=localize("api", "recollection_series_tutorial_end_desc"),
    )
    async def tutorial_end_(self, request: Request) -> Response:
        return offline_response(request)

    @post(
        path="/unlock_series",
        summary=localize("api", "recollection_series_unlock_series_summary"),
        description=localize("api", "recollection_series_unlock_series_desc"),
    )
    async def unlock_series_(self, request: Request) -> Response:
        return offline_response(request)
