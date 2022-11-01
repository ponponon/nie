import io
from typing import Generator
from urllib3.response import HTTPResponse
from nie.ss.minio.core import MinioStatus, MinioFileStatus
from nie.ss.minio.file import MinioBaseFileWriter, MinioBaseFileReader


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
        pass


class MinioTextFileReader(MinioBaseFileReader):

    def read(self, size: int | None = None) -> str:
        object: HTTPResponse = self.status.conn.get_object(
            bucket_name=self.status.bucket_name,
            object_name=self.file_status.file_path,
        )
        return object.data.decode(self.file_status.encoding)

    def readline(self, block_size: int = 2048) -> Generator[str, None, None]:
        pass
