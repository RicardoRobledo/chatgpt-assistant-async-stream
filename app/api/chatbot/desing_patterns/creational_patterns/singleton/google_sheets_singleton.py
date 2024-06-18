import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

from app import config


__author__ = 'Ricardo Robledo'
__version__ = '1.0'


class GoogleSheetSingleton():


    __client = None
    __spreadsheet_id = None


    def __new__(cls, *args, **kwargs):
        
        if cls.__client==None:

            # making connection
            cls.__client = cls.__get_connection()
            cls.__spreadsheet_id = config.SPREADSHEET_ID
        
        return cls.__client


    @classmethod
    def __get_connection(cls):
        """
        This method create our client and give us a new thread
        """

        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        SERVICE_ACCOUNT_FILE = 'keys.json'

        with open(SERVICE_ACCOUNT_FILE, 'w') as file:
            credentials_json = json.loads(config.GOOGLE_CREDENTIALS)
            json.dump(credentials_json, file, indent=4)

        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        client = build("sheets", "v4", credentials=credentials)

        return client


    @classmethod
    async def read_google_sheets(cls):
        """
        This method read the google sheet and return the values
        """

        sheet = cls.__client.spreadsheets()
        
        result = (
            sheet.values()
            .get(spreadsheetId=cls.__spreadsheet_id, range='quejas_clientes!A:B')
            .execute()
        )
        
        values = result.get("values", [])

        return values