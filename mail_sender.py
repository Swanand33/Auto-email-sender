import smtplib
import csv
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(filename='email_sender.log', level=logging.INFO)

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Set up SMTP server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send email
        smtp_server.send_message(msg)
        logging.info(f"Email sent successfully to {recipient_email}")

        # Close connection
        smtp_server.quit()
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

if __name__ == "__main__":
    # Email settings (replace with your actual email credentials)
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    subject = "Your Subject"

    # Read recipient information from CSV file (replace with your sample CSV file)
    with open('recipients.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recipient_name = row['Name']
            recipient_email = row['Email']
            message = f"Dear {recipient_name},\n\nYour personalized message goes here."
            
            # Send email
            send_email(sender_email, sender_password, recipient_email, subject, message)
