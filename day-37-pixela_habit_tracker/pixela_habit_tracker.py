"""
This script interacts with the Pixela API to manage user accounts, graphs, and pixel data.

It includes functions to:
- Create a user account
- Create a graph
- Post a pixel
- Update a pixel
- Delete a pixel

The script uses HTTPS requests and suppresses insecure request warnings.
"""

from datetime import datetime
import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# Suppress only the InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

# Constants
USERNAME = "vikkee"
TOKEN = "fasdfasdrerer3424"
GRAPH_ID = "graph1"
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}
PIXELA_ENDPOINT = "https://pixe.la/v1/users"


def create_user():
    """Creates a user account in Pixela."""
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params, verify=False)
    print("Create User Response:", response.text)


def create_graph():
    """Creates a graph definition in Pixela."""
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Coffee",
        "unit": "commit",
        "type": "int",
        "color": "sora",
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS, verify=False)
    print("Create Graph Response:", response.text)


def post_pixel(date: datetime, quantity: str):
    """Posts a pixel to the graph."""
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_config = {
        "date": date.strftime("%Y%m%d"),
        "quantity": quantity,
    }
    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=HEADERS, verify=False)
    print("Post Pixel Response:", response.text)


def update_pixel(date: datetime, quantity: str):
    """Updates a pixel in the graph."""
    pixel_put_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
    pixel_config = {
        "quantity": quantity,
    }
    response = requests.put(url=pixel_put_endpoint, json=pixel_config, headers=HEADERS, verify=False)
    print("Update Pixel Response:", response.text)


def delete_pixel(date: datetime):
    """Deletes a pixel from the graph."""
    pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
    response = requests.delete(url=pixel_delete_endpoint, headers=HEADERS, verify=False)
    print("Delete Pixel Response:", response.text)


if __name__ == "__main__":
    # Example usage
    pixel_date = datetime(year=2025, month=6, day=30)
    pixel_quantity = "3"

    # Uncomment the desired operations
    # create_user()
    # create_graph()
    # post_pixel(pixel_date, pixel_quantity)
    # update_pixel(pixel_date, pixel_quantity)
    delete_pixel(pixel_date)

