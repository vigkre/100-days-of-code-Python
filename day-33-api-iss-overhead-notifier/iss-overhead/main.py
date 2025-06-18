"""API Endpoints & API Parameters - ISS Overhead Notifier."""

import time
import requests
from requests import Response
from datetime import datetime
from smtplib import SMTP

MY_LAT: float = 51.507351 # Your latitude
MY_LONG: float = -0.127758 # Your longitude

def is_iss_overhead() -> bool:
    """
    Check whether the ISS position is near to the current location.
    Use the latitude and longitude value of the ISS position
    
    Returns whether the ISS position is over the current location.
    """
    response: Response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude: float = float(data["iss_position"]["latitude"])
    iss_longitude: float = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night() -> bool:
    """
    Use the latitude and longitude value of the location and get the sunrise
    and sunset time from the database.
    
    Returns whether it is night or not based on the sunrise and sunset time
    obtained.
    """
    parameters: dict = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    
    # Get the sunrise and sunset timing using latitude and longitude value
    response: Response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now: int = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    # Run the function every 60s to find the ISS is overhead
    time.sleep(60)

    # email and password to send notification mail when ISS is overhead
    my_email: str = "savikram007@gmail.com"
    password: str = "jslr rmpp namm gsvx"

    if is_night() and is_iss_overhead():
        connection: SMTP = SMTP(host="smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: Look up 👍\n\n The ISS is above you in the sky."
        )
