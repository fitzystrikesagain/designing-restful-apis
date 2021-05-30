import codecs
import os
import sys

from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from find_a_restaurant import find_a_restaurant
from models import Base, Restaurant

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

google_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
fs_client_id = os.environ.get("FOURSQUARE_CLIENT_ID")
fs_secret = os.environ.get("FOURSQUARE_CLIENT_SECRET")

engine = create_engine('sqlite:///restaurants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@app.route('/restaurants', methods=['GET', 'POST'])
def all_restaurants_handler():
    pass


# YOUR CODE HERE

@app.route('/restaurants/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def restaurant_handler(id):
    pass


# YOUR CODE HERE

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
