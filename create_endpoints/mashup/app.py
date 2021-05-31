# -*- coding: utf-8 -*-
import os

from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from find_a_restaurant import find_a_restaurant
from models import Base, Restaurant

google_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
fs_client_id = os.environ.get("FOURSQUARE_CLIENT_ID")
fs_secret = os.environ.get("FOURSQUARE_CLIENT_SECRET")

engine = create_engine('sqlite:///restaurants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@app.route("/restaurants", methods=["GET", "POST"])
def all_restaurants_handler():
    if request.method == "GET":
        restaurants = session.query(Restaurant).all()
        return jsonify(restaurants=[i.serialize for i in restaurants])
    elif request.method == "POST":
        # MAKE A NEW RESTAURANT AND STORE IT IN DATABASE
        location = request.args.get("location", "")
        meal_type = request.args.get("mealType", "")
        restaurant_info = find_a_restaurant(meal_type, location)
        if restaurant_info != "No Restaurants Found":
            restaurant = Restaurant(
                restaurant_name=restaurant_info["name"],
                restaurant_address=(restaurant_info["address"]),
                restaurant_image=restaurant_info["image"])
            session.add(restaurant)
            session.commit()
            return jsonify(restaurant=restaurant.serialize)
        else:
            err = jsonify({"error": f"""No Restaurants Found for {meal_type} 
            in {location}"""})
            return err

        # YOUR CODE HERE


@app.route('/restaurants/<int:restaurant_id>', methods=['GET', 'PUT', 'DELETE'])
def restaurant_handler(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    if request.method == "GET":
        return jsonify(restaurant=restaurant.serialize)
    elif request.method == "PUT":
        name = request.args.get("name")
        address = request.args.get("address")
        image = request.args.get("image")
        if name:
            restaurant.restaurant_name = name
        if address:
            restaurant.restaurant_address = address
        if image:
            restaurant.restaurant_image = image
        session.commit()
        return jsonify(restaurant=restaurant.serialize)
    elif request.method == "DELETE":
        session.delete(restaurant)
        session.commit()
        return f"Restaurant {restaurant_id} deleted"


# YOUR CODE HERE

if __name__ == '__main__':
    print("in the main function")
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
