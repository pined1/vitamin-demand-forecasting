# Vitamin-demand-forecasting

Goal: Build a Python project that scrapes real Amazon supplement data, analyzes trends, trains ML/DL models to forecast demand, and recommends how much to stock — ending with a Streamlit dashboard.

Project: This project simulates how an ecommerce intelligence team (like Pattern) might forecast product demand on Amazon using publicly observable signals. Over a 7-day period, we track multiple health supplement products and build forecasting models to inform inventory buy recommendations — without needing access to internal sales data.


## Data Schema

| Field        | Description                                |
|--------------|--------------------------------------------|
| `asin`       | Amazon product ID                          |
| `title`      | Full product name                          |
| `brand`      | Brand/store name                           |
| `price`      | Listed price (in USD)                      |
| `rating`     | Average rating (e.g., "4.7 out of 5 stars")|
| `reviews`    | Number of customer reviews                 |
| `bsr`        | Best Seller Rank (if available)            |
| `scrape_date`| Collection date (`YYYY_MM_DD`)             |



## Week-by-Week Breakdown

| Week | Focus                                     |
|------|-------------------------------------------|
| 1    | Scraping Amazon HTML snapshots & storing versioned CSVs |
| 2    | Data cleaning, EDA, correlation analysis  |
| 3    | XGBoost regression to predict review growth |
| 4    | LSTM model for time series forecasting    |
| 5    | Prophet + Recommendation logic            |
| 6    | Streamlit dashboard + final reporting     |




### Week 1 Workflow:

steps: 
- created the repo structure 
- /opt/homebrew/bin/python3.x --version
- PIPENV_VERBOSITY=-1 pipenv
- pipenv install packages
- saving the actual html file in data folder (ASIN)_2025-07-03
- created the daily_scraper file to get the ID from the html page and store to /data/raw





## Author

**David Pineda**  
Master’s Student – Computer Science @ BYU  
Aspiring Data Scientist | Forecasting | Ecommerce | AI  