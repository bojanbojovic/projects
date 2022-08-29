import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 42.879280
MY_LNG = 18.432751

def isClose():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    issPosition = (longitude, latitude)

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True

def isDark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    timeNow = datetime.now()

    if timeNow.hour < sunrise or timeNow.hour > sunset:
        return True

while True:
    time.sleep(60)
    if isClose() and isDark():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user="vukvukovic035@yahoo.com", password="t3LAJDPc@kB-x8%")
        connection.sendmail(from_addr="vukvukovic035@yahoo.com", to_addrs="vukvukovic035@yahoo.com", msg="Look up for ISS")
        connection.close()


