import datetime as dt
import smtplib
import random

# CONSTANTS
my_email = "jiya.advaita@gmail.com"
password = "qxsttzrdmfudigql"
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
            to_addrs="jiya.advaita@gmail.com",
            msg=f"Subject:Today's Quote\n\n{quote}.",
            )
        connection.close()
