import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/28a63f3d436bdaa872ffe3bfe948de31/flightDetails/sheet1"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data
        print(data)
        return self.destination_data