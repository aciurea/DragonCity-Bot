from dotenv import load_dotenv

import mailtrap as mt
import os

load_dotenv()

class Mail:
    sender = os.getenv("SENDER")
    receiver = os.getenv("RECEIVER")
    

    @staticmethod
    def send(message, subject="DC"):
        mail = mt.Mail(
            sender=mt.Address(email=Mail.sender, name="Mailtrap Test"),
            to=[mt.Address(email=Mail.receiver)],
            subject=subject,
            text=message
        )
        client = mt.MailtrapClient(token=os.getenv(API_TOKEN))
        client.send(mail)
        