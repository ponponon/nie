from nie.aliases import pyminio
from nie.loggers import logger
import io
from typing import overload
from typing import Generator
from urllib3.response import HTTPResponse
from nie.aliases import pyminio

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

IO_MODE: TypeAlias = Literal[
    READ_TEXT_MODE,
    WRITE_TEXT_MODE,
    APPEND_TEXT_MODE,
    READ_STREAM_MODE,
    WRITE_STREAM_MODE,
    APPEND_STREAM_MODE
]


class MinioClient:
    def __init__(self, end_point: str, access_key: str, secret_key: str, bucket_name: str) -> None:
        self.end_point = end_point
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name

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

    def open(self, file_path: str, mode: str, encoding: str = 'utf-8'):
        self.file_path = file_path
        self.mod = mode
        self.encoding = encoding

        self.conn = pyminio.Minio(
            self.end_point,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False
        )
        if mode == 'w':
            return MinioTextFileWriter(self)
        elif mode == 'r':
            return MinioTextFileReader(self)


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
        object: HTTPResponse = self.client.conn.get_object(
            bucket_name=self.client.bucket_name,
            object_name=self.client.file_path,
        )
        return object.data.decode(self.client.encoding)

    def readline(self, block_size: int = 2048) -> Generator[str, None, None]:
        def get_block(offset: int = 0, block_size: int = 2048) -> str | None:
            try:
                object: HTTPResponse = self.client.conn.get_object(
                    bucket_name=self.client.bucket_name,
                    object_name=self.client.file_path,
                    offset=offset,
                    length=block_size
                )
                return object.data.decode(self.client.encoding)
            except pyminio.S3Error as error:
                return None

        def parse(content: str, ass: str) -> tuple[list[str], str]:
            content=content if content else ''
            ass=ass if ass else ''
            _rows = (ass+content).split('\n')

            if len(_rows) == 1:
                _safe_rows = []
                ass = _rows[-1]
            else:
                _safe_rows = _rows[:-1]
                ass = _rows[-1]
            return _safe_rows, ass

        rows: list[str] = []
        ass = ''

        offset = 0

        while True:
            if rows:
                yield rows[0]
            else:
                content = get_block(offset, block_size)
                offset += block_size
                if not content:
                    yield ass
                    return None
                _rows, ass = parse(content, ass)
                rows.extend(_rows)
