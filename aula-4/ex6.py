import requests
from parsel import Selector

defaultUrl = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/"


def requestAllNames(url):
    response = requests.get(defaultUrl+url)
    selector = Selector(text=response.text)
    titles = selector.css(".product_pod > h3 > a::text").getall()
    for title in titles:
        print(title)
    next = selector.css(".next > a::attr(href)").get()
    if(next):
        return requestAllNames(next)


requestAllNames("index.html")
