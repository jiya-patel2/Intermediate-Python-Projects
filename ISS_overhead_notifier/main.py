import requests
from datetime import datetime
import smtplib
import os
import time
# Constants
MY_LAT = 23.022505
MY_LNG = 72.571365
TIME_ZONE = "Asia/Kolkata"

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

def is_iss_overhead():
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 ) and (MY_LNG - 5 <= iss_longitude <= MY_LNG + 5):
        return True


def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "tzid": TIME_ZONE,
        "formatted" : 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json",params= parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    now = datetime.now()
    curr_time = now.hour
    
    if (curr_time > sunset and curr_time < sunrise) :
        return True

# main 
while True:
    time.sleep(120)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:ISS overhead!!",
                    )
                connection.close()
