import requests 
import datetime as dt
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
GENDER = "female"
WEIGHT_KG = 40
HEIGHT_CM = 157
AGE = 20
nutrition_push_api_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"


sheety_api_endpoint = os.environ["sheety_api_endpoint"]
excercise_detail = input("Enter you activity with time: ") 
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
    "Content-Type" : "application/json"
}

data = {
    "query" : excercise_detail,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
post_response = requests.post(url = nutrition_push_api_endpoint,headers=headers,json=data)
post_response.raise_for_status()
result = post_response.json()



now = dt.datetime.now()
curr_date = now.strftime("%d/%m/%Y")
curr_time = now.strftime("%H:%M:%S")
for excercise in result['exercises']:
    sheety_parameters = {
        "sheet1" : {
        "Date":curr_date ,
        "Time" : curr_time,
        "Exercise" : excercise['name'].title(),
        "Duration" : excercise['duration_min'],
        "Calories" : excercise['nf_calories']
        }
    }

    sheety_response = requests.post(url = sheety_api_endpoint,json=sheety_parameters)
    sheety_response.raise_for_status()
    print(sheety_response.text)
  


