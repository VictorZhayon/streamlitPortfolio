import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(name, sender_email, message):
    try:
        EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            raise ValueError("Email credentials not found in environment variables.")

        msg = EmailMessage()
        msg["Subject"] = "New Contact from Portfolio"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg.set_content(f"From: {name} <{sender_email}>\n\n{message}")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
