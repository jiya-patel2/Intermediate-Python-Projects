import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:

    def search_flight(self, city_code):
        headers = {
            "apikey": API_KEY
        }

        params = {
            "fly_from": "AMD",
            "fly_to": city_code,
            "date_from": "20/04/2026",
            "date_to": "30/04/2026",
            "limit": 1,
            "curr": "INR"
        }

        response = requests.get(
            url="https://tequila-api.kiwi.com/v2/search",
            headers=headers,
            params=params
        )

        response.raise_for_status()

        data = response.json()["data"]

        if len(data) == 0:
            return None

        return data[0]