from nie.aliases import pyminio


class MinioStatus:
    def __init__(
        self, end_point: str, access_key: str, secret_key: str, bucket_name: str
    ):
        self.end_point = end_point
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name

        self.conn = pyminio.Minio(
            self.end_point,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False
        )


class MinioFileStatus:
    def __init__(
        self, file_path: str, mode: str, encoding: str = 'utf-8'
    ):
        self.file_path = file_path
        self.mode = mode
        self.encoding = encoding
