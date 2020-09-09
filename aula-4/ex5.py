import requests
from parsel import Selector

response = requests.get(
    "http://books.toscrape.com/catalogue/the-grand-design_405/index.html")


selector = Selector(text=response.text)
titles = selector.css(".product_page > .row > .product_main > h1::text").get()
price = selector.css(
    ".product_page > .row > .product_main > p::text").re_first(r"\d+\.\d{2}")
description = selector.css(".product_page > p::text").get()
url = selector.css("img::attr(src)").get()
quantity = selector.css(".instock").re_first(r"\d{1,}")

suffix = "...more"
if description.endswith(suffix):
    description = description[:-len(suffix)]

print(titles, price, description, url, quantity, sep=",")
