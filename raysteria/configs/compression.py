from litestar.config.compression import CompressionConfig

compression_config = CompressionConfig(
    backend="gzip",
    gzip_compress_level=9
)
