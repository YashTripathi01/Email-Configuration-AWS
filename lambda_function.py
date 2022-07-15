from client_email import client_send_mail
from admin_email import admin_send_mail
from sheet_controller import add_to_sheet
from newsletter_controller import news_letter
from response import res
import json


def lambda_handler(event, context):
    if event['email'] != '' and event['first_name'] != '' and event['last_name'] != '' and event['phone'] != '':
        user_email = event['email']
        user_first_name = event['first_name']
        user_last_name = event['last_name']
        user_phone = event['phone']
        user_msg = event['message']

        admin_send_mail(user_email, user_first_name,
                        user_last_name, user_phone, user_msg)

        client_send_mail(user_email, user_first_name, user_last_name, user_msg)

        add_to_sheet(user_email, user_first_name,
                     user_last_name, user_phone, user_msg)

        return res()

    elif event['email'] != '' and event['first_name'] == '' and event['last_name'] == '' and event['phone'] == '':
        user_email = event['email']

        news_letter(user_email)

        return res()

    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Not found!')
        }
