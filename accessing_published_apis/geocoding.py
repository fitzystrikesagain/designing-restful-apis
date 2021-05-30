import requests
from dotenv import dotenv_values

BASE_URL = "https://maps.googleapis.com/maps/api/geocode"
PREFERRED_FORMAT = "json"
CITIES = [
    "Tokyo, Japan",
    "Jakarta, Indonesia",
    "Maputo, Mozambique",
    "Geneva, Switzerland",
    "Los Angles California, USA",
]


def authenticate():
    """
    Authenticates with the Google Maps API. Expects the key is stored in a file named .env in the current directory in
    the following format:
    GOOGLE_MAPS_API_KEY=YOUR_API_TOKEN_HERE
    :return: API key
    """
    config = dotenv_values("../.env")
    return config.get("GOOGLE_MAPS_API_KEY")


def format_city(city):
    """
    Returns a plus-delimited city string to use as an API query param, e.g. "Tokyo, Japan" -> "Tokyo,+Japan"
    :param city: The name of the city and state/region/country
    :return: Maps API-formatted city query param
    """
    return "+".join(city.split(" "))


def get_coordinates_from_city(json_body):
    """
    Takes a json body from the Geocoding API and returns a tuple of lat/long
    :param json_body: The json response from the API
    :return: tuple (lat, long)
    """
    lat_long = json_body["results"][0]["geometry"]["location"]
    return lat_long.get("lat"), lat_long.get("lng")


def handle_request(url):
    """Handles an API requests for the Google Maps API specifically, which will return a 200 for an invalid key for
    some reason
    :param url: A Google Maps API endpoint without the key, e.g.: https://maps.googleapis.com/maps/api/geocode/json?address=Tokyo,+Japan
    :return: a json body if successful or exit code 1 if not
    """
    api_key = authenticate()
    query_params = f"&key={api_key}"
    full_url = url + query_params
    r = requests.get(full_url)
    if r.json().get("error_message"):
        print(f"Received the following error: {r.json()['status']}")
        exit(1)
    else:
        return r.json()


def main():
    """
    1. Authenticates with the Google Maps API
    2. Iterates through the `CITIES` list to do the following:
    3. Print the URL with the token stripped
    4. Formats the city string and passes it to the handle_request() function, which returns a json body
    5. Sends the json body to `get_coordinates_from_city()`, which returns (lat, long)
    6. Prints the results in the format (City: City, Region; Lat/Long: (lat, long)
    :return: None
    """
    for city in CITIES:
        url = f"{BASE_URL}/{PREFERRED_FORMAT}?address={format_city(city)}"
        print(url)
        body = handle_request(url)
        print(f"City: {city}; Lat/Long: {get_coordinates_from_city(body)}")


if __name__ == "__main__":
    main()
