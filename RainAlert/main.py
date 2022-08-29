import os
import requests
from twilio.rest import Client

apiKey = os.environ.get("OWM_API_KEY")
account_sid = "ACb087a90e312b0465fc65f4828bf73419"
auth_token = "a444aca3a5e7b31bcf52e0719ae3c773"

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall?lat=58.06&lon=105.2&exclude=daily,minutely,alerts&appid=ce777cc8e186b58c316652c06683e924")
response.raise_for_status()
data = response.json()["hourly"]

timeAndWeather = {}
willRain = False

for i in data[:12]:
    id = i["weather"][0]["id"]
    if id < 700:
        willRain = True
        break

if willRain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+13252464340',
        to='+38765845127'
    )
    print(message.status)

# I can create daily alert on PythonAnywhere to run my code


