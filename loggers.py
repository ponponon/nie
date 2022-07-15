from loguru import logger
from mark import BASE_DIR
import settings


# if settings.run_mode != settings.default_run_mode:
#     logger.add(
#         '/logs/svddb_api.log',
#         serialize='json',
#         rotation='100 MB'
#     )
