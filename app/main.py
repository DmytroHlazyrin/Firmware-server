from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse, FileResponse
from datetime import datetime
from typing import Dict
from app.models import DeviceInfo
from app.config import Config

app = FastAPI()
config = Config("config/config.json")
device_data: Dict[str, DeviceInfo] = {}
firmware_path = "data/firmware/"


def get_current_time() -> str:
    return datetime.utcnow().isoformat()


@app.get("/version.txt")
async def get_version(request: Request) -> PlainTextResponse:
    validate_headers(request)
    return PlainTextResponse(config.current_version)


@app.get("/firmware.bin")
async def get_firmware(request: Request) -> FileResponse:
    validate_headers(request)
    return FileResponse(f"{firmware_path}{config.current_version}.bin")


def validate_headers(request: Request) -> None:
    mac = request.headers.get("_br_mac_")
    fw_version = request.headers.get("_br_fwv_")
    if not mac or not fw_version:
        raise HTTPException(status_code=400, detail="Missing custom headers")
    update_device_info(mac, fw_version)


def update_device_info(mac: str, fw_version: str) -> None:
    now = get_current_time()
    if mac not in device_data:
        device_data[mac] = DeviceInfo(
            mac=mac,
            fw_version=fw_version,
            last_seen_time=now
        )
    else:
        device_info = device_data[mac]
        device_info.last_seen_time = now
        if device_info.fw_version != fw_version:
            device_info.update_time = now
            device_info.fw_version = fw_version
