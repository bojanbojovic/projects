import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

SHEET_END_POINT = "https://api.sheety.co/e23984b1e117976bfb83842bb64e6f50/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 192,
    "age": 26
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=body, headers=headers)
# print(response.text)
data = response.json()

exercise = []
duration = []
calories = []

exercises = data["exercises"]
for i in exercises:
    exercise.append(i["name"].title())
    duration.append(i["duration_min"])
    calories.append(i["nf_calories"])

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")



for i in range(len(exercise)):
    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise[i],
            "duration": duration[i],
            "calories": calories[i]
        }
    }

    response = requests.post(url=SHEET_END_POINT,
                                 json=body, auth=(USERNAME, PASSWORD))
    print(response.text)

