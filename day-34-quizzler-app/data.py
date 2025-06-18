
"""
This script fetches trivia questions from the Open Trivia Database API.

It sends a GET request with specified parameters such as amount, type, and category,
and retrieves a list of trivia questions in JSON format.
"""

import requests

params: dict[str, str] = {
    "amount": "10",
    "type": "boolean",
    "category": "18"
}
response: requests.Response = requests.get("https://opentdb.com/api.php", params=params, verify=False)
response.raise_for_status()
data = response.json()
question_data = data["results"]
