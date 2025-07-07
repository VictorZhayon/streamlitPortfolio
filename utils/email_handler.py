### utils/email_handler.py
import smtplib
from email.message import EmailMessage
# from python_dotenv import dotenv

# load_env()

def send_email(name, sender_email, message):
    try:
        EMAIL_ADDRESS = "victorzion1@gmail.com"
        EMAIL_PASSWORD = "softwareyahoo"

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
