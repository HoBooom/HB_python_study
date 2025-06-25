import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

STOCK = "TSLA"

COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
STOCK_API = os.environ.get("STOCK_API")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

dates = list(stock_data.keys())

latest_date_data = stock_data[dates[0]]
day_ago_date_data = stock_data[dates[1]]

latest_date_price = float(latest_date_data['1. open'])
day_ago_date_price = float(day_ago_date_data['1. open'])

change_rate = (latest_date_price - day_ago_date_price) / day_ago_date_price * 100
print(change_rate)

NEWS_API = os.environ.get("NEWS_API")

news_params = {
    "q": "tesla",
    "from": dates[0],
    "sortBy": "publishedAt",
    "apiKey": NEWS_API,
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()["articles"][:3]

if abs(change_rate) > 5:
    for article in news_data:
        print(article)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

