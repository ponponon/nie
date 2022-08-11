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
from nie.ss.minio.file import MinioBaseFileWriter,MinioBaseFileReader

class MinioTextFileWriter(MinioBaseFileWriter):
    def __init__(self, status: MinioStatus, file_status: MinioFileStatus) -> None:
        self.status = status
        self.file_status = file_status

    def write(self, content: str) -> int:

        stream = content.encode(encoding='utf-8')
        self.status.conn.put_object(
            bucket_name=self.status.bucket_name,
            object_name=self.file_status.file_path,
            data=io.BytesIO(stream),
            length=len(stream),
            content_type='text/plain'
        )

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        logger.debug(args)
        logger.debug(kwargs)
        
class MinioTextFileReader(MinioBaseFileReader):

    def read(self) -> str:
        object: HTTPResponse = self.status.conn.get_object(
            bucket_name=self.status.bucket_name,
            object_name=self.file_status.file_path,
        )
        return object.data.decode(self.file_status.encoding)

    def readline(self, block_size: int = 2048) -> Generator[str, None, None]:
        pass
        # def get_block(offset: int = 0, block_size: int = 2048) -> str | None:
        #     try:
        #         object: HTTPResponse = self.client.conn.get_object(
        #             bucket_name=self.client.bucket_name,
        #             object_name=self.client.file_path,
        #             offset=offset,
        #             length=block_size
        #         )
        #         return object.data.decode(self.client.encoding)
        #     except pyminio.S3Error as error:
        #         return None

        # def parse(content: str, ass: str) -> tuple[list[str], str]:
        #     content = content if content else ''
        #     ass = ass if ass else ''
        #     _rows = (ass+content).split('\n')

        #     if len(_rows) == 1:
        #         _safe_rows = []
        #         ass = _rows[-1]
        #     else:
        #         _safe_rows = _rows[:-1]
        #         ass = _rows[-1]
        #     return _safe_rows, ass

        # rows: list[str] = []
        # ass = ''

        # offset = 0

        # while True:
        #     if rows:
        #         yield rows[0]
        #     else:
        #         content = get_block(offset, block_size)
        #         offset += block_size
        #         if not content:
        #             yield ass
        #             return None
        #         _rows, ass = parse(content, ass)
        #         rows.extend(_rows)