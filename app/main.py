from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse, FileResponse
from datetime import datetime, UTC
from typing import Dict
from app.models import DeviceInfo, device_updated
from app.config import Config

app = FastAPI()
config = Config("config/config.json")
device_data: Dict[str, DeviceInfo] = {}
firmware_path = "data/firmware/"


def get_current_time() -> datetime:
    return datetime.now(UTC)


def validate_headers(request: Request) -> Dict[str, str]:
    """Validate custom headers and return device info."""
    mac = request.headers.get("_br_mac_")
    fw_version = request.headers.get("_br_fwv_")
    if not mac or not fw_version:
        raise HTTPException(status_code=400, detail="Missing custom headers")
    return {"mac": mac, "fw_version": fw_version}


def update_device_info(mac: str, fw_version: str) -> bool:
    """Update device information and trigger save on any update."""
    now = get_current_time()
    is_new_device = mac not in device_data

    if is_new_device:
        device_data[mac] = DeviceInfo(mac=mac, fw_version=fw_version)
        device_data[mac].last_seen_time = now
        device_data[mac].save()  # Signal is sent when save() is called
        print(f"New device {mac} registered.")
        return True
    else:
        device_info = device_data[mac]
        version_changed = False

        if device_info.fw_version != fw_version:
            device_info.fw_version = fw_version
            version_changed = True

        device_info.last_seen_time = now
        device_info.save()  # Signal is sent when save() is called

        return version_changed


def send_report_signal(sender, device, **extra):
    """Signal handler for reporting to Google Sheets."""
    print(
        f"Device {device.mac} updated. "
        f"Current firmware: {device.fw_version}. "
        f"Last seen: {device.last_seen_time}. "
        f"Updated: {device.update_time}"
    )


# Connect signal handler to the device_updated event.
device_updated.connect(send_report_signal)


@app.get("/version.txt")
async def get_version(request: Request) -> PlainTextResponse:
    """Return the current firmware version."""
    device_info = validate_headers(request)
    update_device_info(**device_info)
    return PlainTextResponse(config.current_version)


@app.get("/firmware.bin")
async def get_firmware(request: Request) -> FileResponse:
    """Return the firmware binary file."""
    device_info = validate_headers(request)
    if update_device_info(**device_info):
        device_data[device_info["mac"]].update_time = get_current_time()
        device_data[device_info["mac"]].save()
    return FileResponse(f"{firmware_path}{config.current_version}.bin")
