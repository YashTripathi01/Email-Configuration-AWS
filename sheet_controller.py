import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


def add_to_sheet(name, email, phone, msg):
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'creds.json', scope)
    client = gspread.authorize(credentials)

    sheet = client.open('EmailConfig').sheet1

    new_row = [name, email, phone, msg]

    sheet.append_row(new_row)

    pprint(new_row)