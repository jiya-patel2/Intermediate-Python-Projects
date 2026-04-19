from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

# Create objects
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Get sheet data
sheet_data = data_manager.get_destination_data()

# Loop through each destination
for row in sheet_data:
    # Search flight
    flight = flight_search.search_flight(row["iataCodes"])
    if flight:
        # Store data inside FlightData object
        flight_data = FlightData(
            price=flight["price"],
            origin_city=flight["cityFrom"],
            origin_airport=flight["flyFrom"],
            destination_city=flight["cityTo"],
            destination_airport=flight["flyTo"],
            out_date=flight["local_departure"].split("T")[0],
            return_date=flight["route"][-1]["local_departure"].split("T")[0]
        )
        # Check if cheaper than target price
        if flight_data.price < row["prices"]:

            message = f"""
Cheap Flight Alert! ✈️

₹{flight_data.price}

From: {flight_data.origin_city} ({flight_data.origin_airport})
To: {flight_data.destination_city} ({flight_data.destination_airport})

Departure: {flight_data.out_date}
Return: {flight_data.return_date}
"""

            print(message)
            notification_manager.send_email(message)