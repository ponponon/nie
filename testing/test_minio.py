from minio import Minio
from minio.error import S3Error
from mark import BASE_DIR
import unittest
from loguru import logger
from mark import BASE_DIR
from pathlib import Path
import sys
import io
from urllib3.response import HTTPResponse


class TestMinio(unittest.TestCase):
    def test_put_object(self):
        """
        python -m unittest testing.test_minio.TestMinio.test_put_object
        """

        client = Minio(
            "192.168.26.174:9000",
            access_key="ponponon",
            secret_key="ponponon",
            secure=False
        )

        src_file_path = BASE_DIR/'static/img/94dcb906ff774e7ab4d6e8b1abcc147b.png'

        png_image = Image.open(src_file_path)

        png_stream = png_image_2_png_stream(png_image)
        file_like_obj_png_stream = io.BytesIO(png_stream)
        file_like_obj_png_stream.name = 'ttt001.png'

        jpg_stream = png_image_2_jpg_stream(png_image, quality=50)
        file_like_obj_jpg_stream = io.BytesIO(jpg_stream)
        file_like_obj_jpg_stream.name = 'ttt001.jpg'

        client.put_object(
            bucket_name='snapshot',
            object_name='test001.jpg',
            data=file_like_obj_jpg_stream,
            length=len(jpg_stream),
            content_type='image/jpeg'
        )

        client.put_object(
            bucket_name='snapshot',
            object_name='test002.png',
            data=file_like_obj_png_stream,
            length=len(png_stream),
            content_type='image/png'
        )

    def test_get_object(self):
        """
        python -m unittest testing.test_minio.TestMinio.test_get_object
        """
        client = Minio(
            "192.168.31.245:9000",
            # "192.168.26.174:9000",
            access_key="ponponon",
            secret_key="ponponon",
            secure=False
        )

        object: HTTPResponse = client.get_object(
            'nie', 'test/001.txt', 
            offset=15, 
            length=1000
            )
        
        logger.debug(object.data)
        logger.debug(len(object.data))
