"""
This script interacts with the NUTRITIONIX and Sheety API endpoints to track workout training
and add it to a google sheet automatically. 

It includes functions to:
    - Get the exercise stats based on the natural query.
    - Add a new exercise to the google worksheet.
    - Uses basic authentication.

The script uses HTTP GET & POST API requests.

DOC: https://docx.syndigo.com/developers/docs/natural-language-for-exercise
"""
from datetime import datetime
import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# Suppress only the InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

# Constants
APP_ID = "a1b13f69"
API_KEY = "1daf44e30c9990405d1a0154f608d0cb"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
BASIC_HEADERS = {
    "Authorization": "Basic VmlrcmFtIFMgQTpWJGtlWTg4ODM2"
}
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


def get_exercise_data_from_sheet():
    """GET API to get the exercise data from the google sheets."""
    sheety_endpoint = "https://api.sheety.co/8b6fb5685aeb23411e17e5b6231062ff/workoutTraining/workouts"
    
    response = requests.get(url=sheety_endpoint, verify=False).json()    
    print(response["workouts"])


def post_exercise_data_sheet(workout: dict):
    """Add a new exercise to the google worksheet."""
    sheety_endpoint = "https://api.sheety.co/8b6fb5685aeb23411e17e5b6231062ff/workoutTraining/workouts"
    
    requests.post(url=sheety_endpoint, json=workout, headers=BASIC_HEADERS, verify=False)


def get_exercise_stats(natural_query: str):
    """Get the exercise stats based on the natural query."""
    endpoint = f"{NUTRITIONIX_ENDPOINT}"
    config_params = {
        "query": natural_query,
    }
    response = requests.post(url=endpoint, json=config_params, headers=HEADERS, verify=False).json()
    
    return response


if __name__ == "__main__":
    # get_exercise_data_from_sheet()
    natural_query: str = input("Tell me which exercise you did: ")

    # Add new exercise based on the natural_query
    exercise_stats = get_exercise_stats(natural_query)
    exercises = exercise_stats["exercises"]

    for exercise in exercises:
        today_date = datetime.now()

        workout = {
            "workout": {
                "date": today_date.strftime("%x"),
                "time": today_date.strftime("%H:%M:%S"),
                "exercise": str(exercise["name"]).title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }
        
        post_exercise_data_sheet(workout)
