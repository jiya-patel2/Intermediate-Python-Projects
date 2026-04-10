import requests
import smtplib
import os
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
api_key = os.environ.get("RAIN_ALERT_API")
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

LATITUDE = 23.022505
LONGITUDE = 72.571365

parameters={
    "lat" : LATITUDE,
    "lon" : LONGITUDE,
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(url = api_endpoint ,params=parameters)
response.raise_for_status()
data = response.json()
weather_details = data["list"]


for hour_data in weather_details :
    weather = hour_data["weather"][0]["description"]
    # to send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Birthday Wishes\n\n{weather}.",
            )
        connection.close()