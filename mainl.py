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

    html = f"""
        <html>
            <body>
                <h1>{subject}</h1>
                <p>{body}</p>
            </body>
        </html>
    """
    email_message.add_alternative(html, subtype="html")

    ctx = ssl.create_default_context()

    with smtp.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as server :
        server.login(email_endpoint, password)
        server.sendmail(email_endpoint, receive_email, email_message.as_string())


if __name__ == "__main__" :
    main()