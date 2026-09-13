import json
import os

import pandas_market_calendars as mcal
import requests
from dotenv import load_dotenv
from requests_cache import CachedSession

load_dotenv()

session = CachedSession(expire_after=timedelta(days=1))  # noqa: F821
# requests_cache.install_cache("stock_cache")
# session.cache.delete(older_than=timedelta(days=1))

STOCK_API_KEY = os.environ["STOCK_API_KEY"]
# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"

# Get NYSE calendar
nyse = mcal.get_calendar("NYSE")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_URL_ENDPOINT = "https://www.alphavantage.co/query?"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API_KEY,
}


r_stock = session.get(STOCK_URL_ENDPOINT, params=parameters)
# print(r_stock.headers)

stock_timeseries_data = r_stock.json()
# print(stock_timeseries_data["Time Series (Daily)"])
# json_data = json.dumps(stock_data)
# print(json_data)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the
# SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market
# crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC
# The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
# print("Hello")
