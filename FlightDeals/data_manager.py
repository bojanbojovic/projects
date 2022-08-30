import requests

SHEET_ENDPOINT = "https://api.sheety.co/e23984b1e117976bfb83842bb64e6f50/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destinationData = {}

    def getDestinationData(self):
        response = requests.get(url=SHEET_ENDPOINT)
        self.destinationData = response.json()["prices"]
        return self.destinationData

    def updateDestinationCodes(self):
        for city in self.destinationData:
            newData = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}",
                                    json=newData)




