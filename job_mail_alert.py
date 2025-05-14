import smtplib
from email.mime.text import MIMEText
import os

EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_TO = os.getenv('EMAIL_TO')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def send_test_email():
    msg = MIMEText("🎉 This is a test email from your GitHub Action job alert bot!")
    msg['Subject'] = "✅ GitHub Job Bot Test Email"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

if __name__ == "__main__":
    send_test_email()
