from nie.aliases import pyminio
from nie.loggers import logger
import io
from typing import overload


from typing import overload, TypeAlias, Literal

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


class MinioClient:
    def __init__(self, end_point: str, access_key: str, secret_key: str, bucket_name: str) -> None:
        self.end_point = end_point
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        
    # def open(self, file_path: str, mode: str, encoding: str = 'utf-8'):
    #     raise Exception(f'无效的 mode: {mode}')

    @overload
    def open(self, file_path: str, mode: WRITE_TEXT_MODE, encoding: str = 'utf-8'):
        self.file_path = file_path
        if mode == 'w':
            self.conn = pyminio.Minio(
                self.end_point,
                access_key=self.access_key,
                secret_key=self.secret_key,
                secure=False
            )
        return MinioTextFileWriter(self)

    @overload
    def open(self, file_path: str, mode: READ_TEXT_MODE, encoding: str = 'utf-8'):
        self.file_path = file_path
        assert mode == 'r'
        self.conn = pyminio.Minio(
            self.end_point,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False
        )
        return MinioTextFileReader(self)

    @overload
    def open(self, file_path: str, mode: WRITE_STREAM_MODE):
        self.file_path = file_path
        if mode == 'w':
            self.conn = pyminio.Minio(
                self.end_point,
                access_key=self.access_key,
                secret_key=self.secret_key,
                secure=False
            )
        return MinioStreamFileWriter(self)

    


class MinioBaseFileWriter:
    def __init__(self, client: MinioClient) -> None:
        self.client = client

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass


class MinioTextFileWriter(MinioBaseFileWriter):
    def __init__(self, client: MinioClient) -> None:
        self.client = client

    def write(self, content: str) -> int:

        stream = content.encode(encoding='utf-8')
        self.client.conn.put_object(
            bucket_name=self.client.bucket_name,
            object_name=self.client.file_path,
            data=io.BytesIO(stream),
            length=len(stream),
            content_type='text/plain'
        )

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        logger.debug(args)
        logger.debug(kwargs)


class MinioStreamFileWriter(MinioBaseFileWriter):
    def __init__(self, client: MinioClient) -> None:
        self.client = client

    def write(self, stream: bytes) -> int:
        self.client.conn.put_object(
            bucket_name=self.client.bucket_name,
            object_name=self.client.file_path,
            data=io.BytesIO(stream),
            length=len(stream),
        )

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        logger.debug(args)
        logger.debug(kwargs)


class MinioBaseFileReader:
    def __init__(self, client: MinioClient) -> None:
        self.client = client

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass


class MinioTextFileReader(MinioBaseFileReader):

    def read(self) -> str:
        object = self.client.conn.get_object(
            bucket_name=self.client.bucket_name,
            object_name=self.client.file_path,
        )
        object.data

        from nie.loggers import logger
        logger.debug(type(object))
        logger.debug(type(object.data))
        logger.debug(type(object.stream))
