from litestar import Request
from litestar.exceptions import (
    HTTPException as LitestarHTTPException,
    ImproperlyConfiguredException,
    ClientException,
    ValidationException,
    NotAuthorizedException,
    PermissionDeniedException,
    NotFoundException,
    MethodNotAllowedException,
    TooManyRequestsException,
    InternalServerException,
    ServiceUnavailableException,
    NoRouteMatchFoundException,
    TemplateNotFoundException,
)
from litestar.status_codes import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_429_TOO_MANY_REQUESTS,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
)

from raysteria.utils.api import Response


class HTTPException(LitestarHTTPException):
    def __init__(
            self,
            status_code: int,
            error_code: int,
            message: str | dict,
            headers: dict[str, str] = None,
    ) -> None:
        detail = None
        extra = None

        if isinstance(message, str):
            detail = message

        elif isinstance(message, dict):
            extra = message

        super().__init__(
            status_code=status_code,
            headers=headers,
            detail=detail,
            extra=extra,
        )
        self.error_code = error_code


def http_exception_handler(
        _request: Request, exception: HTTPException
) -> Response:
    if exception.extra:
        message = exception.extra
    else:
        message = exception.detail

    return Response(
        status_code=exception.status_code,
        error_code=exception.error_code,
        message=message,
    )


def improperly_configured_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        error_code=1001,
        message="improperly_configured",
    )


def client_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_400_BAD_REQUEST,
        error_code=1001,
        message="bad_request",
    )


def validation_handler(
        _request: Request, exception: HTTPException
) -> Response:
    # errors = []
    # for err in exception.errors:
    #     loc = ".".join(str(i) for i in err["loc"])
    #     msg = err["msg"]
    #     errors.append(f"{loc}: {msg}")

    return Response(
        status_code=HTTP_400_BAD_REQUEST,
        error_code=1001,
        message=f"{exception.detail}",
    )


def not_authorized_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_401_UNAUTHORIZED,
        error_code=1001,
        message="not_authorized",
    )


def permission_denied_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_403_FORBIDDEN,
        error_code=1001,
        message="permission_denied",
    )


def not_found_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_404_NOT_FOUND,
        error_code=1001,
        message="not_found",
    )


def method_not_allowed_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_405_METHOD_NOT_ALLOWED,
        error_code=1001,
        message="method_not_allowed",
    )


def too_many_requests_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_429_TOO_MANY_REQUESTS,
        error_code=1001,
        message="too_many_requests",
    )


def internal_server_error_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        error_code=1001,
        message="internal_server_error",
    )


def service_unavailable_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_503_SERVICE_UNAVAILABLE,
        error_code=1001,
        message="service_unavailable",
    )


def no_route_match_found_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        error_code=1001,
        message="no_route_match_found",
    )


def template_not_found_handler(
        _request: Request, _exception: HTTPException
) -> Response:
    return Response(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        error_code=1001,
        message="template_not_found",
    )


def value_error_handler(
        _request: Request, exception: ValueError
) -> Response:
    return Response(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        error_code=1001,
        message=f"{exception}",
    )


exception_handlers = {
    LitestarHTTPException: http_exception_handler,
    ImproperlyConfiguredException: improperly_configured_handler,
    ClientException: client_handler,
    ValidationException: validation_handler,
    NotAuthorizedException: not_authorized_handler,
    PermissionDeniedException: permission_denied_handler,
    NotFoundException: not_found_handler,
    MethodNotAllowedException: method_not_allowed_handler,
    TooManyRequestsException: too_many_requests_handler,
    InternalServerException: internal_server_error_handler,
    ServiceUnavailableException: service_unavailable_handler,
    NoRouteMatchFoundException: no_route_match_found_handler,
    TemplateNotFoundException: template_not_found_handler,
    ValueError: value_error_handler,
}
