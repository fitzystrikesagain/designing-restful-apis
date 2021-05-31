# -*- coding: utf-8 -*-
import codecs
import json
import os

import httplib2

# sys.stdout = codecs.getwriter("utf8")(sys.stdout)
# sys.stderr = codecs.getwriter("utf8")(sys.stderr)
google_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
fs_client_id = os.environ.get("FOURSQUARE_CLIENT_ID")
fs_secret = os.environ.get("FOURSQUARE_CLIENT_SECRET")
default_image = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/" \
                "cheeseburger-34314_1280.png?direct"


def get_geocode_location(input_string):
    # Replace Spaces with "+" in URL
    location_string = input_string.replace(" ", "+")
    api_url = f"https://maps.googleapis.com/maps/api/geocode/json?"
    query_params = f"address={location_string}&key={google_api_key}"
    url = api_url + query_params
    h = httplib2.Http()
    result = json.loads(h.request(url, "GET")[1])
    # print response
    latitude = result["results"][0]["geometry"]["location"]["lat"]
    longitude = result["results"][0]["geometry"]["location"]["lng"]
    return latitude, longitude


# This function takes in a string representation of a location and cuisine type,
# geocodes the location, and then pass in the latitude and longitude coordinates
# to the Foursquare API
def find_a_restaurant(meal_type, location):
    print("wat")
    latitude, longitude = get_geocode_location(location)
    base_url = "https://api.foursquare.com/v2/venues"
    api_url = base_url + "/search?"
    auth_params = f"client_id={fs_client_id}&client_secret={fs_secret}&"
    version = "&v=20130815"
    lat_long = f"&ll={latitude},{longitude}"
    query = f"&query={meal_type}"
    url = api_url + auth_params + version + lat_long + query
    h = httplib2.Http()
    result = json.loads(h.request(url, "GET")[1])
    if result["response"]["venues"]:
        # Grab the first restaurant
        restaurant = result["response"]["venues"][0]
        venue_id = restaurant["id"]
        restaurant_name = restaurant["name"]
        restaurant_address = restaurant["location"]["formattedAddress"]
        # Format the Restaurant Address into one string
        address = ""
        for i in restaurant_address:
            address += i + " "
        restaurant_address = address

        # Get a  300x300 picture of the restaurant using the venue_id (you can
        # change this by altering the 300x300 value in the URL or replacing it
        # with "orginal" to get the original picture
        photos_url = f"{base_url}/{venue_id}/photos?"
        url = base_url + photos_url + auth_params + version
        result = json.loads(h.request(url, "GET")[1])
        # Grab the first image
        # if no image available, insert default image url
        try:
            firstpic = result["response"]["photos"]["items"][0]
            prefix = firstpic["prefix"]
            suffix = firstpic["suffix"]
            image_url = prefix + "300x300" + suffix
        except KeyError:
            image_url = default_image

        restaurant_info = {"name": restaurant_name,
                           "address": restaurant_address, "image": image_url}
        # print "Restaurant Name: %s " % restaurant_info["name"]
        # print "Restaurant Address: %s " % restaurant_info["address"]
        # print "Image: %s \n " % restaurant_info["image"]
        return restaurant_info
    else:
        # print "No Restaurants Found for %s" % location
        return "No Restaurants Found"


if __name__ == "__main__":
    print("db")
    find_a_restaurant("Pizza", "Tokyo, Japan")
    find_a_restaurant("Tacos", "Jakarta, Indonesia")
    find_a_restaurant("Tapas", "Maputo, Mozambique")
    find_a_restaurant("Falafel", "Cairo, Egypt")
    find_a_restaurant("Spaghetti", "New Delhi, India")
    find_a_restaurant("Cappuccino", "Geneva, Switzerland")
    find_a_restaurant("Sushi", "Los Angeles, California")
    find_a_restaurant("Steak", "La Paz, Bolivia")
    find_a_restaurant("Gyros", "Sydney Austrailia")
print("db")
