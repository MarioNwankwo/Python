import requests
import feedparser

response = requests.get("https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale")

feed = feedparser.parse(response.content)
print(feed)

import pprint
feed = feedparser.parse(response.content)
pprint.pprint(feed, indent =4)

d = {
    'key1': 1,
    'key2': 2,
}
print(d['key1'])

l = [1, 2]
print(l[0])

l = [
    {'key1': 1, 'key2': 2, 'key1': 3},
    dict(key1=11, key2=22),
]

print(len(l))
