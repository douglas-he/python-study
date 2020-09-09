import requests
from parsel import Selector

defaultUrl = "http://quotes.toscrape.com/tableful/"

response = requests.get(defaultUrl)
selector = Selector(text=response.text)
tds = selector.css("td[style*='padding-top']::text").getall()
for citation in tds:
    print(citation)