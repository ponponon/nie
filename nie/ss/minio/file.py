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
