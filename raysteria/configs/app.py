from dataclasses import dataclass

@dataclass
class RaysteriaConfig:
    s3_url: str


app_config = RaysteriaConfig(
    s3_url="https://rays-cdn.nexog.one/",
)
