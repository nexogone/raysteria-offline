import os
from pathlib import Path

from litestar import Request
from litestar.response import Template
from litestar.status_codes import HTTP_200_OK, HTTP_404_NOT_FOUND

from raysteria.configs.app import app_config


class AnnounceService:
    def __init__(self, request: Request):
        self.config = app_config

    async def view(self, announce_id: int) -> Template:
        page_path = f"announces/{announce_id}.html.jinja"
        template_path = Path("raysteria/assets/templates", page_path)

        if not os.path.exists(template_path):
            return Template(
                template_name="error.html.jinja",
                context={
                    "title": "404 Not Found",
                    "message": "The publication period has expired.",  # 公開期間が終了しました。
                    "s3_url": self.config.s3_url,
                },
                status_code=HTTP_404_NOT_FOUND,
            )

        return Template(
            template_name=page_path,
            context={
                "title": "TOTR INFORMATION",
                "s3_url": self.config.s3_url,
            },
            status_code=HTTP_200_OK,
        )
