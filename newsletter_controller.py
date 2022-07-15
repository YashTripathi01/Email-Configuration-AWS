import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


def news_letter(email):
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'creds.json', scope)
    client = gspread.authorize(credentials)

    sheet = client.open('EmailConfig').worksheet('Sheet2')

    new_row = [email]

    sheet.append_row(new_row)

    pprint(new_row)
