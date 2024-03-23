import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
from datetime import datetime, timedelta

def send_reminder_email():
    conn = sqlite3.connect('translations.db')
    cursor = conn.cursor()
    query = "SELECT email FROM Users WHERE last_practice_date < DATE('now', '-7 days')"
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    subject = "Reminder: Practice Your Language Skills"
    body = "Dear language learner,\n\nThis is a friendly reminder to practice your language skills today!\n\nBest regards,\nYour Language Learning App"
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    password = 'your_password'
    for user in users:
        receiver_email = user[0]
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    send_reminder_email()
