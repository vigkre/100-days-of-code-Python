"""
This script monitors the stock price of a specified company and sends SMS alerts if there is a significant change.
It performs the following steps:

1. Fetches intraday stock data using the Alpha Vantage API.
2. Calculates the percentage change in stock price between two consecutive days at 4 PM.
3. If the change exceeds a defined threshold (e.g., 5%), it retrieves the latest news articles about the company using the News API.
4. Sends SMS alerts with the stock change and news headlines using Twilio.

Usage:
- Configure the STOCK, COMPANY_NAME, and API keys.
- Run the script to monitor stock changes and receive alerts.

Note:
- Ensure that the required libraries (requests, twilio) are installed.
- API keys and Twilio credentials should be kept secure and ideally stored in environment variables.
"""
import os
import requests
from datetime import datetime, time, timedelta
from urllib3.exceptions import InsecureRequestWarning
import urllib3
from twilio.rest import Client

# Suppress only the InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_FROM = "+12537930014"
TWILIO_TO = "+919072129405"


def get_stock_data():
    """
    Fetches intraday stock data for the specified stock symbol.
    
    Returns:
        dict: JSON response containing time series data.
    """
    url = (
        f"http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"
        f"&symbol={STOCK}&interval=60min&apikey={STOCK_API_KEY}"
    )
    response = requests.get(url, verify=False)
    return response.json()


def calculate_percentage_change(data):
    """
    Calculates the percentage change in stock price between yesterday and the day before.

    Args:
        data (dict): Stock time series data.

    Returns:
        float: Percentage change in closing price.
    """
    today = datetime.today()
    yesterday_4pm = str(datetime.combine(today.date() - timedelta(days=1), time(16, 0)))
    day_before_4pm = str(datetime.combine(today.date() - timedelta(days=2), time(16, 0)))

    yesterday_close = float(data['Time Series (60min)'][yesterday_4pm]['4. close'])
    day_before_close = float(data['Time Series (60min)'][day_before_4pm]['4. close'])

    return ((yesterday_close - day_before_close) / day_before_close) * 100


def get_news():
    """
    Fetches the latest news articles related to the company.

    Returns:
        list: List of news articles.
    """
    url = (
        f"https://newsapi.org/v2/everything?q={COMPANY_NAME}"
        f"&apiKey={NEWS_API_KEY}&from=2025-06-01&to=2025-06-25&language=en"
    )
    response = requests.get(url, verify=False)
    return response.json().get("articles", [])


def send_sms(message_body):
    """
    Sends an SMS message using Twilio.

    Args:
        message_body (str): The content of the SMS message.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_FROM,
        to=TWILIO_TO,
    )
    print(f"Message status: {message.status}")


def main():
    """
    Main function to check stock price change, fetch news, and send SMS alerts.
    """
    stock_data = get_stock_data()
    percentage_change = calculate_percentage_change(stock_data)

    print(f"Percentage Change: {percentage_change:.2f}%")

    if abs(percentage_change) >= 5:
        articles = get_news()
        for article in articles[:3]:
            message = (
                f"{STOCK}: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change):.2f}%\n"
                f"Headline: {article['title']}\n"
                f"Brief: {article['description']}\n"
            )
            send_sms(message)


if __name__ == "__main__":
    main()
