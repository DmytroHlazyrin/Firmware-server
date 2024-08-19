from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class DeviceInfo(BaseModel):
    mac: str
    fw_version: str
    last_seen_time: datetime
    update_time: Optional[datetime] = None
