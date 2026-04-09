import requests
parameters = {
    "amount" : 10,
    "category" : 31,
    "type" : "boolean",
}
respond  = requests.get(url= "https://opentdb.com/api.php?",params=parameters)
respond.raise_for_status()
data = respond.json()
anime_data = data["results"]
