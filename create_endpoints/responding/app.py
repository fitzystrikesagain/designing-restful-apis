from flask import Flask, request

app = Flask(__name__)


# Create the appropriate app.route functions, test and see if they work, and paste your URIs in the boxes below.

# Make an app.route() decorator here
@app.route("/puppies", methods=["GET", "POST"])
def puppies_function():
    if request.method == 'GET':
        # Call the method to Get all of the puppies
        return get_all_puppies()

    elif request.method == 'POST':
        # Call the method to make a new puppy
        return make_new_puppy()


# Make another app.route() decorator here that takes in an integer id in the
@app.route("/puppies/<puppy_id>", methods=["GET", "PUT", "DELETE"])
def puppies_functionId(puppy_id):
    if request.method == 'GET':
        # Call the method to get a specific puppy based on their id
        return get_puppy(puppy_id)
    if request.method == 'PUT':
        # Call the method to update a puppy
        return update_puppy(puppy_id)
    elif request.method == 'DELETE':
        # Call the method to remove a puppy
        return delete_puppy(puppy_id)


def get_all_puppies():
    return "Getting All the puppies!"


def make_new_puppy():
    return "Creating A New Puppy!"


def get_puppy(puppy_id):
    return f"Getting Puppy with id {puppy_id}"


def update_puppy(puppy_id):
    return f"Updating a Puppy with id {puppy_id}"


def delete_puppy(puppy_id):
    return f"Removing Puppy with id {puppy_id}"
