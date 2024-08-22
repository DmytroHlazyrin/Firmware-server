from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from blinker import signal
from app.google_sheets import google_sheets_client

# Define a custom signal for device updates.
device_updated = signal('device_updated')


class DeviceInfo(BaseModel):
    mac: str
    fw_version: str
    last_seen_time: Optional[datetime] = None
    update_time: Optional[datetime] = None

    def save(self):
        """Save the model to Google Sheets and send a signal."""
        data = {
            "mac": self.mac,
            "fw_version": self.fw_version,
            "last_seen_time": self.last_seen_time.isoformat() if self.last_seen_time else "",
            "update_time": self.update_time.isoformat() if self.update_time else ""
        }
        google_sheets_client.update_device_info(data)
        device_updated.send(self.__class__, device=self)
