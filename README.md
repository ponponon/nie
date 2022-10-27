# nie

Generic object storage services and distributed file system read and write solutions 💯

The following storage services are supported:

- [minio](https://min.io/) ✅ 
- [oss](https://www.aliyun.com/product/oss) ❌
- [gcs](https://cloud.google.com/storage) ❌
- [s3](https://aws.amazon.com/cn/s3/) ❌
- [cos](https://cloud.tencent.com/product/cos) ❌
- [obs](https://www.huaweicloud.com/product/obs.html) ❌

The following distributed file systems are supported:

- Local Hard Drive ❌
- [hdfs](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html) ❌
- [fastdfs](https://github.com/happyfish100/fastdfs) ❌

Other Features:

- python3.10+


# Getting Started

- Check out the documentation.



# examples

```python
from nie.ss.minio import MinioClient
from loguru import logger

client = MinioClient(
    end_point='192.168.31.1:9000',
    access_key='ak',
    secret_key='sk',
    bucket_name='nie',
)


with client.open('tweets/en32tge57626gh372eb.txt', 'r', encoding='utf-8') as file:
    logger.debug(file.read())

has_obj: bool = client.os.path.exists('tweets/en32tge57626gh372eb.txt'')

logger.debug(has_obj)
```