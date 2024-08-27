# Firmware-server

## Overview

Firmware-server is an OTA (Over-The-Air) server for devices to check for firmware updates and download them. It is built using FastAPI and Python, and it utilizes Google Sheets to store and manage device information. The server supports handling multiple firmware versions but serves only the current version as specified in the configuration file.

## Features

- **Check Firmware Version**: Devices can check the current firmware version available on the server.
- **Download Firmware**: Devices can download the firmware binary from the server.
- **Device Information Management**: The server collects and reports device information to Google Sheets, including the last seen time, update time, firmware version, and MAC address.
- **Asynchronous Execution**: The server performs I/O operations asynchronously to enhance performance.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Google Sheets API client
- gspread
- decouple
- pytest for testing

## Installation

1. Clone the repository:

```bash
git clone https://github.com/DmytroHlazyrin/Firmware-server.git
cd Firmware-server
```
2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Unix or MacOS
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Configure Google Sheets integration:

    - Place your Google Sheets credentials JSON file in the config/ directory and name it credentials.json.
    - Set up the SPREADSHEET_ID in a .env file or in the environment variables.

## Configuration
- Configuration File: config/config.json

    {
      "current_version": "v1.0.0"
    }

- Environment Variables: Create a .env file in the root directory with the following content:

```
CREDENTIALS_FILE_PATH=config/credentials.json
SPREADSHEET_ID=your_spreadsheet_id
```
    
### Running the Server
To run the server locally, use the following command:

```bash
uvicorn app.main:app --reload
```
To run with Docker:
```bash
docker build -t firmware-server .
docker run -d -p 8000:8000 --name firmware-server firmware-server
```
To stop and remove container:
```bash
docker stop firmware-server
docker rm firmware-server
```

#### Requests
To communicate with a server requests must have the next headers:
- `_br_mac_` - device MAC address
- `_br_fwv_` - current device firmware version

Check firmware version request:
```bash
curl -X GET http://localhost:8000/version.txt -H 'cache-control: no-cache' -H 'Connection: close' -H '_br_mac_: 00:11:22:33:44:55' -H '_br_fwv_: v1.0.0'
```

Download firmware binary request:
```bash
curl -X GET http://localhost:8000/firmware.bin -H 'cache-control: no-cache' -H 'Connection: close' -H '_br_mac_: 00:11:22:33:44:55' -H '_br_fwv_: v1.0.0'
```

### Testing
To run the tests, use:
```bash
pytest
```
### Known Issues
HTTPS: HTTPS is not yet implemented. For security in production, you should set up HTTPS with a valid SSL certificate.

Systemd Service: Systemd service file is not implemented. 

For managing server processes on Linux systems, you would need to create a systemd service file or run with Docker.
### Future Work
Implement HTTPS: Secure the server with HTTPS using a valid SSL certificate.

Create Systemd Service File: Automate the server's start/restart with a systemd service file for Linux systems.

Enhance Testing: Expand tests to cover all edge cases and ensure high code coverage.

### Contact
For any inquiries or issues, please contact dmytro.hlazyrin@gmail.com
