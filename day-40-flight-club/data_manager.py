import os
import requests
from requests.auth import HTTPBasicAuth
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Try to find from CWD first; fall back to file-relative
env_path = find_dotenv(usecwd=True)
if not env_path:
    file_env = Path(__file__).resolve().parent / ".env"
    if file_env.exists():
        env_path = str(file_env)

if not env_path:
    raise FileNotFoundError("Could not find a .env file. Place it at project root or next to this script.")

load_dotenv(env_path)


class DataManager:
    
    def __init__(self):
        username = os.getenv("SHEETY_USERNAME")
        if not username:
            raise KeyError("SHEETY_USERNAME is not set. Add it to your .env or export it in your environment.")
        self._user = username
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.user_data = []
        self.sheety_prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.sheety_users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")


    def get_price_data_from_sheet(self):
        """GET API to get the flight price data from the google sheets."""
        response = requests.get(url=self.sheety_prices_endpoint, auth=self._authorization, verify=False).json()        
        self.destination_data = response["prices"]
        return self.destination_data


    def get_customer_emails(self):
        """GET API to get the user emails into a list from the google sheets."""
        response = requests.get(url=self.sheety_users_endpoint, auth=self._authorization, verify=False).json()        
        for user in response["users"]:
            self.user_data.append(user["whatIsYourEmailAddress"])
        return self.user_data

    
    def update_iata_code(self):
        for city in self.destination_data:
            put_sheety_endpoint = f"{self.sheety_prices_endpoint}/{city['id']}"        
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(url=put_sheety_endpoint, json=new_data, auth=self._authorization, verify=False).json()

