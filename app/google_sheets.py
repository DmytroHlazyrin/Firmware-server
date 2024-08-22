import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging
from decouple import config

# Logging configuration
logger = logging.getLogger(__name__)


class GoogleSheetsClient:
    def __init__(self, credentials_file: str, spreadsheet_id: str):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        try:
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                credentials_file,
                scope
            )
            self.client = gspread.authorize(credentials)
            self.sheet = self.client.open_by_key(spreadsheet_id).sheet1
        except Exception as e:
            logger.exception("Error initializing Google Sheets client")
            raise

    def update_device_info(self, device_info: dict):
        """Update or insert device information in the Google Sheet."""
        try:
            cell = self.sheet.find(device_info["mac"])
            if cell:
                self.sheet.update_cell(cell.row, 2, device_info["fw_version"])
                self.sheet.update_cell(cell.row, 3, device_info["update_time"])
                self.sheet.update_cell(cell.row, 4, device_info["last_seen_time"])
                logger.info(f"Device info updated in Google Sheets: {device_info['mac']}")
            else:
                self.sheet.append_row([
                    device_info["mac"],
                    device_info["fw_version"],
                    device_info["update_time"],
                    device_info["last_seen_time"]
                ])
                logger.info(f"New device added to Google Sheets: {device_info['mac']}")
        except gspread.exceptions.APIError as e:
            logger.exception("Google Sheets API error")
        except Exception as e:
            logger.exception("Unexpected error while updating Google Sheets")


# Initialize Google Sheets client
google_sheets_client = GoogleSheetsClient(
    credentials_file=config("CREDENTIALS_FILE_PATH"),
    spreadsheet_id=config("SPREADSHEET_ID"),
)
