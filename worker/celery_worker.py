from celery import Celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SMTP_USERNAME = ""
SMTP_PASSWORD = ""

app = Celery(
    'email_tasks',
    broker='pyamqp://guest@localhost//',
    backend='rpc://'
)

@app.task
def send_email_task(email_data):
    sender_email = SMTP_USERNAME
    receiver_email = email_data['email_to']
    subject = email_data['subject']
    body = email_data['body']

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls() 
    server.login(SMTP_USERNAME, SMTP_PASSWORD)

    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

    return "Email sent successfully"
