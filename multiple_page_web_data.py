import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

# Create a directory to save HTML files if it doesn't exist
os.makedirs("html", exist_ok=True)

# List to store all book items
all_items = []

# Loop through pages 1 to 50
for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    
    # Save HTML file (optional)
    with open(f"html/page{i}.html", "w", encoding="utf-8") as f:
        f.write(response.text)
        print(f"Downloaded page {i}")
    
    # Parse page content
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select("article.product_pod")
    
    for article in articles:
        title = article.find("h3").find("a")["title"]
        price = article.select_one("p.price_color").text.split("£")[1]
        rating_element = article.select_one("p.star-rating")
        rating = rating_element['class'][1]  # e.g., "One", "Two", etc.
        all_items.append([title, price, rating])

# Create DataFrame
df = pd.DataFrame(all_items, columns=["Book", "Price", "Book Rating"])

# Save to CSV
df.to_csv("books_data.csv", index=False)

print("Scraping complete. Data saved to books_data.csv")
# This code scrapes book data from multiple pages of a website and saves it to a CSV file.