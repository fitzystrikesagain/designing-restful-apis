from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Puppy
from utils.constants import FLASK_APP_PORT

engine = create_engine("sqlite:///puppies.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


# Create the appropriate app.route functions,
# test and see if they work


# Make an app.route() decorator here
@app.route("/")
@app.route("/puppies", methods=["GET", "POST"])
def puppiesFunction():
    if request.method == "GET":
        # Call the method to Get all of the puppies
        return getAllPuppies()
    elif request.method == "POST":
        # Call the method to make a new puppy
        print("Making a New puppy")

        name = request.args.get("name", '')
        description = request.args.get("description", '')
        print(name)
        print(description)
        return makeANewPuppy(name, description)


# Make another app.route() decorator here that takes in an integer
# puppy_id in the URI
@app.route("/puppies/<puppy_id>", methods=["GET", "PUT", "DELETE"])
# Call the method to view a specific puppy
def puppiesFunctionId(puppy_id):
    if request.method == "GET":
        return getPuppy(puppy_id)

    # Call the method to edit a specific puppy
    elif request.method == "PUT":
        name = request.args.get("name", '')
        description = request.args.get("description", '')
        return updatePuppy(puppy_id, name, description)

    # Call the method to remove a puppy
    elif request.method == "DELETE":
        return deletePuppy(puppy_id)


def getAllPuppies():
    puppies = session.query(Puppy).all()
    return jsonify(Puppies=[i.serialize for i in puppies])


def getPuppy(puppy_id):
    puppy = session.query(Puppy).filter_by(puppy_id=puppy_id).one()
    return jsonify(puppy=puppy.serialize)


def makeANewPuppy(name, description):
    puppy = Puppy(name=name, description=description)
    session.add(puppy)
    session.commit()
    return jsonify(Puppy=puppy.serialize)


def updatePuppy(puppy_id, name, description):
    puppy = session.query(Puppy).filter_by(puppy_id=puppy_id).one()
    if not name:
        puppy.name = name
    if not description:
        puppy.description = description
    session.add(puppy)
    session.commit()
    return f"Updated a Puppy with puppy_id {puppy_id}"


def deletePuppy(puppy_id):
    puppy = session.query(Puppy).filter_by(puppy_id=puppy_id).one()
    session.delete(puppy)
    session.commit()
    return f"Removed Puppy with puppy_id {puppy_id}"


if __name__ == "__main__":
    app.debug = False
    app.run(host="0.0.0.0", port=FLASK_APP_PORT)
