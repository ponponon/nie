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


class MinioBaseFileWriter:
    def __init__(self, status: MinioStatus, file_status: MinioFileStatus) -> None:
        self.status = status
        self.file_status = file_status

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass


class MinioBaseFileReader:
    def __init__(self, status: MinioStatus, file_status: MinioFileStatus) -> None:
        self.status = status
        self.file_status = file_status

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass
