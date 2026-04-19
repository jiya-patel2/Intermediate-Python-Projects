import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:

    def send_email(self, message):
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(email, password)

            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject:Flight Deal Alert!\n\n{message}"
            )