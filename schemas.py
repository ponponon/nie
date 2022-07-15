from datetime import datetime
from typing import Optional
from pydantic import BaseModel, BaseSettings, Field
from enum import Enum
import json
# from typing import TypeAlias

class MinioConfig(BaseModel):
    access_key:str
    secret_key:str
    end_point:str
    bucket:str