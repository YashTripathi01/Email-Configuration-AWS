import smtplib
import ssl
from email.message import EmailMessage
from constants import *
from client_controller import *


def client_send_mail(email, first_name, last_name, msg):
    subject = f'Enquiry from: {first_name} {last_name}'
    sender_email = SENDER_EMAIL
    password = PASSWORD
    receiver_email = email

    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # to use html for message
    html = client_email(first_name, last_name, msg)

    message.add_alternative(html, subtype='html')

    print('Sending Client Email...')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print('Client Mail Sent Successfully!')


# client_send_mail('yash@openspaceservices.com', 'Yash',
#           'Hello, Thanks for responding!')
