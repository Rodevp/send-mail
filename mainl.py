import smtplib as smtp
import ssl
from email.message import EmailMessage


def main() :

    subject = ""
    body = ""
    email_endpoint = ""
    receive_email = ""
    password = input("Enter password: ")

    email_message = EmailMessage()
    email_message["From"] = email_endpoint
    email_message["To"] = receive_email
    email_message["Subject"] = subject
    email_message.set_content(body)

    


if __name__ == "__main__" :
    main()