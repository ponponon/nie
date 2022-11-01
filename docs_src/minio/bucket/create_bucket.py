from nie.ss.minio import MinioClient
from loguru import logger


client = MinioClient(
    end_point='192.168.31.245:9000',
    access_key='ponponon',
    secret_key='ponponon',
    bucket_name='nie',
)

if not client.status.conn.bucket_exists(bucket_name='nie'):
    client.status.conn.make_bucket(bucket_name='nie')


client.status.conn.bucket_exists
client.status.conn.make_bucket
client.status.conn.remove_bucket
client.status.conn.list_buckets



