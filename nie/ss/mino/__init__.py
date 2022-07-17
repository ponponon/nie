from nie.aliases import pyminio
from nie.loggers import logger
import io


class MinioClient:
    def __init__(self, end_point: str, access_key: str, secret_key: str, bucket_name: str) -> None:
        self.end_point = end_point
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name

    def open(self, file_path: str, mode: str, encoding=str):
        self.file_path=file_path
        if mode == 'w':
            self.conn = pyminio.Minio(
                self.end_point,
                access_key=self.access_key,
                secret_key=self.secret_key,
                secure=False
            )
        return MinioFileWriter(self)


class MinioFileWriter:
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


class MinioFileReader:
    def __init__(self) -> None:
        pass

    def read(self, content: str | bytes):
        pass
