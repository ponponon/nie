from datetime import datetime
from nie.ss.minio.core import MinioStatus


class MinioPathHandler:
    def __init__(self, status: MinioStatus) -> None:
        self.status = status

    def exists(self, file_path: str) -> bool:
        for _ in self.status.conn.list_objects(
                self.status.bucket_name, prefix=file_path):
            return True
        return False

    def getctime(self, file_path: str) -> datetime:
        """ 返回文件 path 创建时间 """
        pass

    def getsize(self, file_path: str) -> int:
        """ 返回文件大小，如果文件不存在就返回错误 """
        pass

    def isfile(self, file_path: str) -> bool:
        """ 判断路径是否为文件 """
        pass

    def isdir(self, file_path: str) -> bool:
        """ 判断路径是否为目录 """
        pass


class MinioOSHandler:

    _path: MinioPathHandler = None

    def __init__(self, status: MinioStatus) -> None:
        self.status = status

    @property
    def path(self) -> MinioPathHandler:
        if not self._path:
            self._path = MinioPathHandler(self.status)
        return self._path

    def listdir(self, file_path: str):
        return self.status.conn.list_objects(
            self.status.bucket_name,
            prefix=file_path
        )
