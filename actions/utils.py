import requests
from actions.constants import *


def get_joke():
    f"""
    Fetches a random dad joke from {JOKE_API}
    Raises:
        requests.exceptions.RequestException: If there's an issue with the request
    """
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(JOKE_API, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.json()
        return data["joke"]
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return "Couldn't retrieve a joke. Please check your internet connection."
