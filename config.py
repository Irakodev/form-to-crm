from dotenv import load_dotenv
import os

load_dotenv()

CREDENTIALS_FILE = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
SPREADSHEET_NAME = os.getenv("SPREADSHEET_NAME")
