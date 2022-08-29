import requests
from datetime import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

aplphaApiKey = "RESL8Z1X0A8TG5Q3"

response = requests.get(
    url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=RESL8Z1X0A8TG5Q3")
data = response.json()["Time Series (Daily)"]
dataR = list(data.values())
yesterdayClose = float(dataR[0]["4. close"])
beforeYesterdayClose = float(dataR[1]["4. close"])

percentage = (yesterdayClose - beforeYesterdayClose) / ((yesterdayClose + beforeYesterdayClose) / 2)
percentage *= 100

now = str(datetime.now())[:10]

newsApiKey = "93e19a41288940c0a58d032a43f14ffb"

response = requests.get(
    url="https://newsapi.org/v2/everything?q=Tesla%20Inc&from=" + now + "&sortBy=popularity&apiKey=93e19a41288940c0a58d032a43f14ffb")
data = response.json()["articles"]
dataNews = []

for i in data[:3]:
    dataNews.append(i["title"])

if round(percentage, 2) > 5 or round(percentage, 2) < -5:
    print(dataNews)

account_sid = "ACb087a90e312b0465fc65f4828bf73419"
auth_token = "a444aca3a5e7b31bcf52e0719ae3c773"
client = Client(account_sid, auth_token)

mes = ""
if percentage > 0:
    mes += "TSLA: 🔺"
else:
    mes += "TSLA: 🔻"

mes += str(round(percentage, 2))
mes += "\n"
for i in range(3):
    newMes = mes + "Headline: " + dataNews[i]
    message = client.messages \
        .create(
        body=newMes,
        from_='+13252464340',
        to='+38765845127'
    )
    print(message.status)

