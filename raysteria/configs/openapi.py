from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin
from litestar.openapi.spec import Tag

from raysteria.utils.i18n import localize

openapi_config = OpenAPIConfig(
    title="Raysteria API",
    version="0.1.0",
    description=localize("api", "openapi_desc"),
    tags=[
        Tag(
            name=localize("api", "agency_name"),
            description=localize("api", "agency_desc"),
        ),
    ],
    path="/docs",
    render_plugins=[
        ScalarRenderPlugin(),
    ],
)
