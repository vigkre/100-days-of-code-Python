from dotenv import load_dotenv, find_dotenv
from pathlib import Path

import os
import smtplib


# Try to find from CWD first; fall back to file-relative
env_path = find_dotenv(usecwd=True)
if not env_path:
    file_env = Path(__file__).resolve().parent / ".env"
    if file_env.exists():
        env_path = str(file_env)

if not env_path:
    raise FileNotFoundError("Could not find a .env file. Place it at project root or next to this script.")

load_dotenv(env_path)


class NotificationManager:
    
    def __init__(self):
        self.smtp_host = os.getenv("SMTP_ADDRESS")
        self.smtp_user = os.getenv("SMTP_MY_EMAIL")
        self.smtp_pass = os.getenv("SMTP_PASSWORD")
    
    def send_emails(self, emails: list[str], message: str):
        for email in emails:
            with smtplib.SMTP(host=self.smtp_host, port=587) as connection:
                connection.starttls()
                connection.login(user=self.smtp_user, password=self.smtp_pass)
                connection.sendmail(
                    from_addr=self.smtp_user,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode("utf-8"),
                )
