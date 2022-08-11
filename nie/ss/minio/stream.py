from nie.aliases import pyminio
from nie.loggers import logger
import io
from typing import overload
from typing import Generator
from urllib3.response import HTTPResponse
from nie.aliases import pyminio
from datetime import datetime
from typing import overload, TypeAlias, Literal
from nie.ss.minio.core import MinioStatus, MinioFileStatus
from nie.ss.minio.file import MinioBaseFileWriter


class MinioStreamFileWriter(MinioBaseFileWriter):
    def __init__(self, status: MinioStatus, file_status: MinioFileStatus) -> None:
        self.status = status
        self.file_status = file_status

    def write(self, stream: bytes) -> int:
        self.status.conn.put_object(
            bucket_name=self.status.bucket_name,
            object_name=self.file_status.file_path,
            data=io.BytesIO(stream),
            length=len(stream),
        )

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        logger.debug(args)
        logger.debug(kwargs)
