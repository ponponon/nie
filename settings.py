import os
import yaml
from mark import BASE_DIR
from schemas import MinioConfig
from loguru import logger


run_mode = os.environ['RUN_MODE'].lower()

logger.debug(f'当前的运行模式: {run_mode}')


with open(BASE_DIR/'config.yaml', 'r', encoding='utf-8') as f:
    config: dict[str, dict] = yaml.load(f.read(), Loader=yaml.CLoader)
    current_config: dict[str, dict] = config[run_mode]


MINIO_CONFIG = MinioConfig(
    **(current_config['minio'])
)