import smtplib
import ssl
from email.message import EmailMessage
from constants import *
from admin_controller import *


def admin_send_mail(email, first_name, last_name, phone, msg):
    subject = f'Enquiry from: {first_name} {last_name}'
    sender_email = SENDER_EMAIL
    password = PASSWORD
    receiver_email = email

    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = sender_email
    message['Subject'] = subject

    # to use html for message
    html = admin_email(receiver_email, first_name, last_name, phone, msg)

    message.add_alternative(html, subtype='html')

    print('Sending Admin Email...')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, sender_email, message.as_string())

    print('Admin Mail Sent Successfully!')


# admin_send_mail('vishal@openspaceservices.com', 'Vishal', 123456789,
#                 'Hello, Thanks for responding!')
