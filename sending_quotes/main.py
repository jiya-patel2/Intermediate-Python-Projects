import datetime as dt
import smtplib
import random
import os

# CONSTANTS
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")
DAY = ""

def whichday():
    now = dt.datetime.now()
    today = now.weekday()
    if today == 0:
        return "Monday"


# QUOTES

with open (".\\sending_quotes\\quotes.txt") as file:
    quotes = file.readlines()
    quote = random.choice(quotes)
    print(quote)

# main code
DAY = whichday()
if DAY == "Monday":
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Today's Quote\n\n{quote}.",
            )
        connection.close()
