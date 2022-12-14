from typing import overload, TypeAlias, Literal
from nie.ss.minio.op import MinioOSHandler
from nie.ss.minio.stream import MinioStreamFileWriter
from nie.ss.minio.text import MinioTextFileWriter, MinioTextFileReader
from nie.ss.minio.core import MinioStatus, MinioFileStatus


READ_TEXT_MODE: TypeAlias = Literal[
    'r',
]
# write
WRITE_TEXT_MODE: TypeAlias = Literal[
    "w",
]

APPEND_TEXT_MODE: TypeAlias = Literal[
    "a",
]

READ_STREAM_MODE: TypeAlias = Literal[
    "rb",
]
# write
WRITE_STREAM_MODE: TypeAlias = Literal[
    "wb",
]

APPEND_STREAM_MODE: TypeAlias = Literal[
    "ab",
]

IO_MODE: TypeAlias = Literal[
    READ_TEXT_MODE,
    WRITE_TEXT_MODE,
    APPEND_TEXT_MODE,
    READ_STREAM_MODE,
    WRITE_STREAM_MODE,
    APPEND_STREAM_MODE
]


class MinioClient:

    _os: MinioOSHandler = None

    @property
    def os(self):
        if not self._os:
            self._os = MinioOSHandler(self.status)
        return self._os

    def __init__(self, end_point: str, access_key: str, secret_key: str, bucket_name: str) -> None:
        """
        client = MinioClient(
            end_point='192.168.31.100:9000',
            access_key='your_access_key',
            secret_key='your_secret_key',
            bucket_name='your_bucket_name',
        )
        """
        self.status = MinioStatus(
            end_point=end_point,
            access_key=access_key,
            secret_key=secret_key,
            bucket_name=bucket_name
        )

    @overload
    def open(self, file_path: str, mode: WRITE_TEXT_MODE, encoding: str = 'utf-8') -> MinioTextFileWriter:
        pass

    @overload
    def open(self, file_path: str, mode: READ_TEXT_MODE, encoding: str = 'utf-8') -> MinioTextFileReader:
        pass

    @overload
    def open(self, file_path: str, mode: WRITE_STREAM_MODE) -> MinioStreamFileWriter:
        pass

    def open(self, file_path: str, mode: str, encoding: str = 'utf-8'):

        file_status = MinioFileStatus(
            file_path=file_path, mode=mode, encoding=encoding)

        if mode == 'w':
            return MinioTextFileWriter(status=self.status, file_status=file_status)
        elif mode == 'r':
            return MinioTextFileReader(status=self.status, file_status=file_status)
