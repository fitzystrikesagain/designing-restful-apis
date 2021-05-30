import os

import requests

from geocoding import BASE_URL as MAPS_BASE_URL
from geocoding import PREFERRED_FORMAT
from geocoding import format_city
from geocoding import get_coordinates_from_city
from geocoding import handle_request as handle_maps_request
from restaurant_search import BASE_URL as FS_BASE_URL
from restaurant_search import SEARCH_ENDPOINT as FS_SEARCH_ENDPOINT
from restaurant_search import build_params as build_fs_params
from restaurant_search import handle_request as handle_fs_request

DEFAULT_IMAGE = imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
PHOTOS_ENDPOINT = "https://api.foursquare.com/v2/venues/{}/photos"
PHOTO_DIMENSIONS = (300, 300)
FORMATTED_DIMENSIONS = f"{PHOTO_DIMENSIONS[0]}x{PHOTO_DIMENSIONS[1]}"
SEARCH_RADIUS_IN_METERS = 100000


def find_restaurant(fs_query, city):
    # 1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    # 2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
    # 3. Grab the first restaurant
    # 4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value
    # in the URL or replacing it with 'orginal' to get the original picture
    # 5. Grab the first image
    # 6. If no image is available, insert default a image url
    # 7. Return a dictionary containing the restaurant name, address, and image url

    # Get the coordinates from the city name
    maps_url = f"{MAPS_BASE_URL}/{PREFERRED_FORMAT}?address={format_city(city)}"
    body = handle_maps_request(maps_url)
    lat_long = get_coordinates_from_city(body)

    # Search Foursquare for venues
    fs_params = build_fs_params(*lat_long, fs_query)
    fs_params["radius"] = SEARCH_RADIUS_IN_METERS
    fs_api_url = os.path.join(FS_BASE_URL, FS_SEARCH_ENDPOINT)
    fs_response = handle_fs_request(fs_api_url, fs_params)

    # Return the default image if there are no search results.
    if not fs_response["response"]["venues"]:
        return DEFAULT_IMAGE

    # Get and call the photos endpoint from the first venue
    venue_id = fs_response["response"]["venues"][0]["id"]
    photos = PHOTOS_ENDPOINT.format(venue_id)
    r = requests.get(photos, params=fs_params)
    photos_response = r.json()["response"]

    # Return the default photo if there are no photos
    if not photos_response["photos"]["items"]:
        return DEFAULT_IMAGE

    # Otherwise, compose and return a url
    prefix = photos_response["photos"]["items"][0]["prefix"]
    suffix = photos_response["photos"]["items"][0]["suffix"]
    photo_url = f"{prefix}{FORMATTED_DIMENSIONS}{suffix}"
    return photo_url


def main():
    print(find_restaurant("Pizza", "Tokyo, Japan"))
    print(find_restaurant("Tacos", "Jakarta, Indonesia"))
    print(find_restaurant("Tapas", "Maputo, Mozambique"))
    print(find_restaurant("Falafel", "Cairo, Egypt"))
    print(find_restaurant("Spaghetti", "New Delhi, India"))
    print(find_restaurant("Cappuccino", "Geneva, Switzerland"))
    print(find_restaurant("Sushi", "Los Angeles, California"))
    print(find_restaurant("Steak", "La Paz, Bolivia"))
    print(find_restaurant("Gyros", "Sydney, Australia"))


if __name__ == '__main__':
    main()
