from nie import nopen
from mark import BASE_DIR
from nie.ss.mino import MinioClient
from loguru import logger

# with nopen(BASE_DIR/'') as file:
#     content = file.read()

# with open(BASE_DIR/'001.jpg', 'rb') as file:

#     content = file.read()


# with open(BASE_DIR/'001.txt', 'r') as file:

#     content = file.read()


client = MinioClient(
    end_point='192.168.31.245:9000',
    access_key='ponponon',
    secret_key='ponponon',
    bucket_name='nie',
)

with client.open('test/001.txt', 'w', encoding='utf-8') as file:
    logger.debug(f'开始写入')
    file.write('你好呀')
