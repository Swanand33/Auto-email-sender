# Automated Email Sender 

This project is a Python script that automates the process of sending emails using SMTP. It reads recipient information from a CSV file and sends personalized emails to each recipient.

## Project Structure

Auto Mails/
├── email_sender.py
├── recipients.csv
├── venv/
│ ├── Include/
│ ├── Lib/
│ ├── Scripts/
│ ├── pyvenv.cfg
│ └── ...
├── email_sender.log
└── README.md


## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Swanand33/Auto-email-sender.git
    cd Auto-email-sender
    ```

2. **Set up the virtual environment**:
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # On Windows use `.\venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install logging
    ```

4. **Add your email credentials**:
    Update the `sender_email` and `sender_password` variables in `mail_sender.py` with your email and password.

5. **Run the script**:
    ```bash
    mail_sender.py
    ```

## Sample CSV Format

The `recipients.csv` file should look like this:

```csv
Name,Email
John Doe,johndoe@example.com
Jane Smith,janesmith@example.com
Alice Johnson,alicejohnson@example.com
