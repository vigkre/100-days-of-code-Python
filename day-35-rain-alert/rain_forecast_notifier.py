"""
Weather Forecast Alert Script

This script fetches a 5-day weather forecast for a specified location using the OpenWeatherMap API.
If rain or adverse weather is predicted (weather code < 700), it sends an SMS alert using Twilio.

Environment Variables Required:
- OPENWEATHER_API_KEY: API key for OpenWeatherMap
- TWILIO_ACCOUNT_SID: Twilio account SID
- TWILIO_AUTH_TOKEN: Twilio authentication token
- https_proxy: Proxy server URL for HTTPS requests (if required)
"""

import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Coordinates for the location (Sweden)
MY_LAT = 57.696991
MY_LONG = 11.986500

# Load credentials from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

def get_weather_forecast():
    """
    Fetches the weather forecast and sends an SMS alert if rain is expected.

    Uses OpenWeatherMap's 5-day forecast API to check weather conditions.
    If any forecasted weather condition has a code < 700 (indicating rain, snow, etc.),
    an SMS alert is sent using Twilio.

    Raises:
        requests.RequestException: If the API call fails.
        Exception: For any other unexpected errors.
    """
    params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": API_KEY,
        "cnt": 8,  # Number of forecast entries (3-hour intervals)
    }

    try:
        response = requests.get(
            url="https://api.openweathermap.org/data/2.5/forecast",
            params=params,
        )
        response.raise_for_status()
        weather_data = response.json()

        for data in weather_data["list"]:
            weather_code = data["weather"][0]["id"]
            if int(weather_code) < 700:
                proxy_client = TwilioHttpClient()
                proxy_client.session.proxies = {
                    'https': os.environ.get('https_proxy')
                }

                client = Client(account_sid, auth_token, http_client=proxy_client)
                message = client.messages.create(
                    body="It's going to rain today. Remember to bring an umbrella.",
                    from_="+12537930014",
                    to="+919882822526",
                )
                print(f"Message sent: {message.status}")
                break

    except requests.RequestException as e:
        print(f"Weather API error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
get_weather_forecast()
