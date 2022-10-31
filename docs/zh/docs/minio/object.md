对象操作


下面的示例展示了：
- 判断一个文件（对象）是否存在
- 如果存在，读取该文件

```python
from nie.ss.minio import MinioClient
from loguru import logger


client = MinioClient(
    end_point='192.168.31.245:9000',
    access_key='ponponon',
    secret_key='ponponon',
    bucket_name='nie',
)

if client.os.path.exists('pon/god.txt'):
    with client.open('pon/god.txt', 'r', encoding='utf-8') as file:
        logger.debug(file.read())
```

