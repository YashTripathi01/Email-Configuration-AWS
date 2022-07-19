import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


def add_to_sheet(email, first_name, last_name, phone, msg):
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'creds.json', scope)
    client = gspread.authorize(credentials)

    sheet = client.open('EmailConfig').sheet1

    new_row = [email, first_name, last_name, phone, msg]

    sheet.append_row(new_row)

    pprint('Successfully added to sheets')
