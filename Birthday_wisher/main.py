import datetime as dt
import pandas
import smtplib
from random import choice
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
TEMPLATES = [".\\Intermediate-Python-Projects\\Birthday_wisher\\letter_templates\\letter_1.txt",
             ".\\Intermediate-Python-Projects\\Birthday_wisher\\letter_templates\\letter_2.txt",
             ".\\Intermediate-Python-Projects\\Birthday_wisher\\letter_templates\\letter_3.txt"
             ]
PLACE_HOLDER = "[NAME]"

# to check todays date and month
today = dt.datetime.now()
current_date = today.day
current_month = today.month

# to select random letter 

with open (choice(TEMPLATES),"r") as file:
    selected_template =  file.read()


# Using Pandas convert data to dictionary
data = pandas.read_csv(".\\Intermediate-Python-Projects\\Birthday_wisher\\birthday.csv")
info = data.to_dict(orient="records")
# traversing each row and checking the birthday
for row in info :
    if row["month"] == current_month and row["day"] == current_date:
        birthday_letter = selected_template.replace(PLACE_HOLDER,(row["name"]).strip())
        # to send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row["email"],
                msg=f"Subject:Birthday Wishes\n\n{birthday_letter}.",
                )
            connection.close()
