# This file will scrape products from Amazon

# Scrape the following info for each product:

### These are all proxy variables 
# Title
# Brand
# Price
# Rating
# Review count
# Best Sellers Rank (BSR)

# review count	Approximates cumulative sales
# review delta	Daily sales velocity signal
# price trend	Drop might trigger higher volume
# rating trend	Can influence future conversions
# rank trend	Best sellers rank → demand window

# I wil locate this information of these products using Amazon Standard Identification Number (ASIN)
# example1 : CoQ10 https://www.amazon.com/dp/B0D6Z7W1YX
# example2 : Now Foods Omega-3 https://www.amazon.com/dp/B001GCU6KA
# example3 : ELMNT Super Collagen https://www.amazon.com/dp/B0CJB9WKWP


## Packages ## 
# - requests: lets you fetch (GET) the content of a webpage
# - BeautifulSoup: parses and extracts data from HTML
# - pandas: used later to store data in tables (DataFrames)
# - time: for adding delays between scrapes
# - atetime: for adding a timestamp to the data
# - os: for file system operations (like making folders)

from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os



# === 1. Define the product ASINs ===
product_asins = [
    "B0D6Z7W1YX",  # Now CoQ-10
    "B001GCU6KA",  # Now Foods Omega-3
    "B0CJB9WKWP"   # ELMNT Super Collagen
]







# === 2. Scrape one local HTML file ===
def scrape_local_html(asin, date_str):
    filepath = f"data/html/{asin}_{date_str}.html"

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

    soup = BeautifulSoup(html, "html.parser")

    # Extract fields
    title = soup.find(id="productTitle")
    brand = soup.find(id="bylineInfo")
    price = soup.find("span", class_="a-offscreen")
    rating = soup.find("span", class_="a-icon-alt")
    review_count = soup.find("span", id="acrCustomerReviewText")
    bsr = soup.find("span", class_="zg-badge-text")  # Optional

    return {
        "asin": asin,
        "title": title.get_text(strip=True) if title else None,
        "brand": brand.get_text(strip=True) if brand else None,
        "price": price.get_text(strip=True) if price else None,
        "rating": rating.get_text(strip=True) if rating else None,
        "reviews": review_count.get_text(strip=True) if review_count else None,
        "bsr": bsr.get_text(strip=True) if bsr else None,
        "scrape_date": date_str
    }








# === 3. Run the scrape for today's files ===
def run_scraper():
    date_str = datetime.now().strftime("%Y_%m_%d")
    results = []

    for asin in product_asins:
        print(f"Scraping {asin} for {date_str}...")
        product_data = scrape_local_html(asin, date_str)
        if product_data:
            results.append(product_data)

    # Save to CSV
    df = pd.DataFrame(results)
    output_file = f"data/raw/amazon_products_{date_str}.csv"
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    run_scraper()
