from client_email import client_send_mail
from admin_email import admin_send_mail
from sheet_controller import add_to_sheet
import json


def lambda_handler(event, context):
    print(event)
    if not event['email'] or event['email'] == '':
        return {
            'statusCode': 404,
            'body': json.dumps('Not found!')
        }

    user_email = event['email']
    user_name = event['name']
    user_phone = event['phone']
    user_msg = event['message']

    admin_send_mail(user_email, user_name, user_phone, user_msg)

    client_send_mail(user_email, user_name, user_msg)

    add_to_sheet(user_name, user_email, user_phone, user_msg)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            'Access-Control-Allow-Credentials': 'true'
        },
        'body': json.dumps('Success!')
    }
