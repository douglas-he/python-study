import requests
from parsel import Selector

defaultUrl = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/"


def requestAllNames(url):
    response = requests.get(defaultUrl+url)
    selector = Selector(text=response.text)
    titles = selector.css(".product_pod > h3 > a::text").getall()
    images = selector.css("img::attr(src)").getall()
    index = 0
    while(index < len(titles)):      
        print(titles[index], images[index])
        index += 1
    next = selector.css(".next > a::attr(href)").get()
    if(next):
        return requestAllNames(next)


requestAllNames("index.html")
