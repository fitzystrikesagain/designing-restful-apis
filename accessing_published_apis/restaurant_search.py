import os
from pprint import pprint
import requests

from dotenv import dotenv_values

BASE_URL = "https://api.foursquare.com/v2"
API_VERSION = "20210530"
SEARCH_ENDPOINT = "venues/search"


def authenticate():
    """
    Authenticate with the Foursquare API. Returns id and secret if successful, otherwise
    exits with exit code -1
    :return: (CLIENT_ID, CLIENT_SECRET)
    """
    config = dotenv_values("../.env")
    creds = config.keys()
    client_id = config.get("FOURSQUARE_CLIENT_ID")
    client_secret = config.get("FOURSQUARE_CLIENT_SECRET")
    try:
        assert (client_id is not None and client_secret is not None)
    except AssertionError:
        if len(config.keys()) == 0:
            exit(f"Unable to locate credentials. Do you have an .env file stored in {os.getcwd()}?")
        exit(f"Found env file but not Foursquare credentials. Found the following credentials: {creds}")
    return client_id, client_secret


def build_params(lat, long, query):
    """
    Builds the query params for an API request
    :param lat: Latitude
    :param long: Longitude
    :param query: The topic of interest, e.g. coffee, restaurants, etc.
    :return: params dict
    """
    client_id, client_secret = authenticate()
    return dict(
        client_id=client_id,
        client_secret=client_secret,
        v=API_VERSION,
        ll=f"{lat},{long}",
        query=f"{query}",
        limit=1
    )


def handle_request(url, params):
    """
    Sends an API request to Foursquare
    :return: json body
    """
    r = requests.get(url=url, params=params)
    if r.ok:
        return r.json()
    else:
        exit(r.json()["meta"]["errorDetail"])


def main():
    """
    Queries Foursquare for recommendations in the following cities for the corresponding categories
    Mountain View, California (37.392971, -122.076044), "pizza"
    Miami, Florida (25.773822, -80.237947), "sushi"
    Washington, DC (38.897478, -77.000147), "donuts"
    New York, New York (40.768349, -73.96575), "salad"
    """
    authenticate()
    api_url = os.path.join(BASE_URL, SEARCH_ENDPOINT)

    mnt_view = build_params(37.392971, -122.076044, "pizza")
    miami = build_params(25.773822, -80.237947, "sushi")
    washington = build_params(38.897478, -77.000147, "donuts")
    new_york = build_params(40.768349, -73.96575, "salad")

    # Change the city to get results for a different city
    body = handle_request(api_url, new_york)
    pprint(body, indent=0)


if __name__ == "__main__":
    main()
