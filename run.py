from nie import nopen
from mark import BASE_DIR
from nie.ss.minio import MinioClient
from loguru import logger
from typing import overload
from typing import Generator
from loguru import logger

client = MinioClient(
    end_point='192.168.31.245:9000',
    access_key='ponponon',
    secret_key='ponponon',
    bucket_name='nie',
)

with client.open('test/001.txt', 'w', encoding='utf-8') as file:
    logger.debug(f'开始写入')
    file.write('你好呀哈哈')


with client.open('test/001.txt', 'r', encoding='utf-8') as file:
    logger.debug(f'开始读取')
    logger.debug(file.read())

has_obj = client.os.path.exists('test/001.txt')

logger.debug(has_obj)
