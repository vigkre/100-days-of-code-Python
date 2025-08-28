"""
This script interacts with Sheety API endpoints to hold cities and their flight ticket
price in a google sheet and notify the users

It includes functions to:
    - Use Sheety API to read and write data into google sheet
    - Get IATA City code using Amadeus
    - Search and find for cheapest flight
    - Notify the users when there is a good flight deal via email using SMTP
"""
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
notify_manager = NotificationManager()
user_emails = data_manager.get_customer_emails()
sheet_data = data_manager.get_price_data_from_sheet()
flight_search = FlightSearch()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_iata_code()

# ==================== Search for direct Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    message = f"{destination['city']}: £{cheapest_flight.price}"
    notify_manager.send_emails(user_emails, message)
    # Slowing down requests to avoid rate limit
    time.sleep(2)
    
    # ==================== Search for indirect flight if N/A ====================
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct="false",
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        message = f"Cheapest indirect flight price is: £{cheapest_flight.price}"
        notify_manager.send_emails(user_emails, message)
