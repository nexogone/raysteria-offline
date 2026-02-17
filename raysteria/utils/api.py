import json
from importlib import import_module
from inspect import getmembers, isclass
from pkgutil import iter_modules
from types import ModuleType
from typing import List

from litestar import Request
from litestar import Response as LitestarResponse
from litestar.status_codes import (
    HTTP_501_NOT_IMPLEMENTED,
    HTTP_200_OK,
)


def dynamic_import(
        package: ModuleType
) -> List[type]:
    package_path = package.__path__
    namespace_prefix = package.__name__ + "."
    controllers = []

    for module_info in iter_modules(package_path, namespace_prefix):
        module = import_module(module_info.name)

        for name, obj in getmembers(module):
            if isclass(obj) and name.endswith("Controller"):
                controllers.append(obj)

    return controllers


class Response(LitestarResponse):
    def __init__(
            self,
            message: str | dict,
            status_code: int = HTTP_200_OK,
            error_code: int = 0,
    ) -> None:
        super().__init__(
            status_code=status_code,
            content={
                "error_code": error_code,
                "message": message,
            },
        )


def not_implemented() -> Response:
    return Response(
        status_code=HTTP_501_NOT_IMPLEMENTED,
        error_code=1001,
        message="not_implemented",
    )


def offline_response(
        request: Request,
) -> Response:
    route_path = request.url.path
    json_path = "raysteria/assets/offline_mode/" + "/".join(route_path.split("/")[3:]) + ".json"
    json_response = json.load(open(json_path, encoding="utf-8"))

    print(f"[DEBUG] route_path: {route_path}, json_path: {json_path}")
    return Response(
        status_code=HTTP_200_OK,
        error_code=0,
        message=json_response,
    )
