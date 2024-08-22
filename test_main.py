import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_get_version():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/version.txt", headers={
            "_br_mac_": "00:11:22:33:44:55",
            "_br_fwv_": "v1.0.0"
        })
        assert response.status_code == 200
        assert response.text == "v1.0.0"


@pytest.mark.asyncio
async def test_get_firmware():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/firmware.bin", headers={
            "_br_mac_": "00:11:22:33:44:55",
            "_br_fwv_": "v1.0.0"
        })
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/octet-stream"


@pytest.mark.asyncio
async def test_get_version_missing_headers():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/version.txt")
        assert response.status_code == 400
        assert response.json() == {"detail": "Missing custom headers"}


@pytest.mark.asyncio
async def test_get_firmware_missing_headers():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/firmware.bin")
        assert response.status_code == 400
        assert response.json() == {"detail": "Missing custom headers"}

@pytest.mark.asyncio
async def test_update_device_info():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/version.txt", headers={
            "_br_mac_": "00:11:22:33:44:55",
            "_br_fwv_": "v1.1.0"
        })
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_device_info_invalid_mac():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/version.txt", headers={
            "_br_mac_": "invalid_mac",
            "_br_fwv_": "v1.1.0"
        })
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid MAC address format"}


@pytest.mark.asyncio
async def test_update_device_info_invalid_fw_version():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/version.txt", headers={
            "_br_mac_": "00:11:22:33:44:55",
            "_br_fwv_": "invalid_version"
        })
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid firmware version format"}


@pytest.mark.asyncio
async def test_google_sheets_update_error():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/version.txt", headers={
            "_br_mac_": "00:11:22:33:44:55",
            "_br_fwv_": "v1.1.0"
        })
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_time_format():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/version.txt", headers={
            "_br_mac_": "00:11:22:33:44:55",
            "_br_fwv_": "v1.0.0"
        })
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_last_seen_time_format():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/firmware.bin", headers={
            "_br_mac_": "00:11:22:33:44:55",
            "_br_fwv_": "v1.0.0"
        })
        assert response.status_code == 200
