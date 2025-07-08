## when I miss the day - I can run this script *data needs to be already saved* 

## pipenv run python scripts/scrape_specific_date.py 2025_07_07


from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import sys

# === Define ASINs ===
product_asins = [
    "B0D6Z7W1YX",  # Now CoQ-10
    "B001GCU6KA",  # Now Omega-3
    "B0CJB9WKWP"   # ELMNT Collagen
]

# === Scrape a single HTML file ===
def scrape_local_html(asin, date_str):
    filepath = f"data/html/{asin}_{date_str}.html"

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find(id="productTitle")
    brand = soup.find(id="bylineInfo")
    price = soup.find("span", class_="a-offscreen")
    rating = soup.find("span", class_="a-icon-alt")
    review_count = soup.find("span", id="acrCustomerReviewText")
    bsr = soup.find("span", class_="zg-badge-text")

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

# === Run scraper for a user-specified date ===
def run_scraper_for_date(date_str):
    print(f"Running scrape for {date_str}")
    results = []

    for asin in product_asins:
        print(f"Scraping ASIN: {asin}")
        data = scrape_local_html(asin, date_str)
        if data:
            results.append(data)

    df = pd.DataFrame(results)
    os.makedirs("data/raw", exist_ok=True)
    output_file = f"data/raw/amazon_products_{date_str}.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scrape_specific_date.py YYYY_MM_DD")
        sys.exit(1)

    date_input = sys.argv[1]
    run_scraper_for_date(date_input)
