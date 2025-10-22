
import requests
import json

quary = input ("what type of news like  :")
url = f"https://newsapi.org/v2/everything?q={quary}&from=2023-10-19&sortBy=publishedAt&apiKey=4377fbb38c56406797dd1a780dbf8be5"
req = requests.get(url)
news = json.loads(req.text)
i = 0
for article in news['articles']:
    print (article["title"])
    print (article["description"])
    print ("_________________________________________\n")
