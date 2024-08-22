import gspread
from decouple import config
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetsClient:
    def __init__(self, credentials_file: str, spreadsheet_id: str):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_file,
            scope
        )
        self.client = gspread.authorize(credentials)
        self.sheet = self.client.open_by_key(spreadsheet_id).sheet1

    def update_device_info(self, device_info: dict):
        """Update or insert device information in the Google Sheet."""
        # Find the row with the matching MAC address
        try:
            cell = self.sheet.find(device_info["mac"])
            # Update existing row
            if cell:
                self.sheet.update_cell(cell.row, 2, device_info["fw_version"])
                self.sheet.update_cell(cell.row, 3, device_info["update_time"])
                self.sheet.update_cell(cell.row, 4, device_info["last_seen_time"])
            else:
                self.sheet.append_row([
                    device_info["mac"],
                    device_info["fw_version"],
                    device_info["update_time"],
                    device_info["last_seen_time"]
                ])
        except Exception as e:
            print(f"Unexpected error: {e}")


# Initialize Google Sheets client
google_sheets_client = GoogleSheetsClient(
    credentials_file=config("CREDENTIALS_FILE_PATH"),
    spreadsheet_id=config("SPREADSHEET_ID"),
)
