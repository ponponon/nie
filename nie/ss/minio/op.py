from nie.aliases import pyminio
from nie.loggers import logger
import io
from typing import overload
from typing import Generator
from urllib3.response import HTTPResponse
from nie.aliases import pyminio
from datetime import datetime
from typing import overload, TypeAlias, Literal
from nie.ss.minio.core import MinioStatus


class MinioPathHandler:
    def __init__(self, status: MinioStatus) -> None:
        self.status = status

    def exists(self, file_path: str) -> bool:
        for obj in self.status.conn.list_objects(
                self.status.bucket_name, prefix=file_path):
            return True
        return False

        # result:Generator=self.status.conn.list_objects(
        #     self.status.bucket_name, prefix=file_path)

        # logger.debug(next(result))
        # logger.debug(result.send(None))
        # logger.debug(result.next())

        # result:list[str] = list(

        # )

        # logger.debug(result)
        # logger.debug(type(result))

        # result = self.bucket.list_objects(object_file_path, max_keys=1)
        # object_list: list[SimplifiedObjectInfo] = result.object_list
        # return bool(object_list)

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
    def path(self):
        if not self._path:
            self._path = MinioPathHandler(self.status)
        return self._path
