import requests
import pandas as pd
from bs4 import BeautifulSoup

url = requests.get("https://books.toscrape.com/")

for i in range(1, 51):
    url = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    with open(f"html/page{i}.html", "w", encoding="utf-8") as f:
        f.write(url.text)
        print(f"Download page {i}")
        
with open("html/page1.html") as f:
    content = f.read()

soup = BeautifulSoup(content,"html.parser")

articles = soup.select("article.product_pod")

items = []
for article in articles:
    title = article.find("h3").find("a")["title"]
    price = article.select_one("p.price_color").text.split("£")[1]
    rating_element = article.select_one("p.star-rating")
    rating = rating_element['class'][1]
    items.append([title, price,rating])
    
pd.DataFrame(items, columns=["Book", "Price","Book Rating"])