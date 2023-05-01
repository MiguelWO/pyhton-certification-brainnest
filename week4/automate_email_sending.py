''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.
Here are the steps you can take to automate this process:
    Use the smtplib library to connect to the email server and send the emails.
    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.
    Use the os library to access the report files that need to be sent.
    Use a for loop to iterate through the list of recipients and send the email and attachment.
    Use the schedule library to schedule the script to run daily at a specific time.
    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import os
import smtplib
import time

import schedule
import ssl
from email import encoders

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import logging

subject = "Daily Report"
body = "Dear [Client],\nPlease find attached your daily report. Let us know if you have any questions or concerns. " \
       "\nBest regards, "
sender_email = "test@gmail.com"
password = "password"

recipients = ["miguel@gmail.com", "isabella@gmail.com", "jose@gmail.com", "susana@gmail.com", "marcela@gmail.com"]

report_path = os.path.join(os.getcwd(), "reports", "report.pdf")

logging.basicConfig(filename="log.txt", level=logging.INFO )


def send_email(recipient, report_path):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with open(report_path, "rb") as attachment:
        report_data = attachment.read()

    part = MIMEBase("application", "octet-stream")
    part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(report_path)}", )
    part.set_payload(report_data)

    encoders.encode_base64(part)

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient, text)
            logging.info(f"Email sent to {recipient}")
            server.quit()
    except Exception as e:
        logging.error(f"Error sending the email to {recipient}", exc_info=True)


def send_emails():
    for recipient in recipients:
        send_email(recipient, report_path)


schedule.every().day.at("10:00").do(send_emails)

while True:
    schedule.run_pending()
    time.sleep(100)


