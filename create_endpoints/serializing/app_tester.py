import httplib2
import json
import sys

from utils.constants import FLASK_APP_PORT

print("Running Endpoint Tester....\n")
print("Please enter the address of the server you want to access.")
print(f"Press Enter to use http://localhost:{FLASK_APP_PORT}: ")
address = input()
if address == "":
    address = f"http://localhost:{FLASK_APP_PORT}" if not address else address

# Making a POST Request
print("Making a POST request to /puppies...")
try:
    url = address + "/puppies?name=Fido&description=Playful+Little+Puppy"
    h = httplib2.Http()
    resp, result = h.request(url, "POST")
    obj = json.loads(result)
    puppyID = obj["Puppy"]["puppy_id"]
    if resp["status"] != "200":
        raise Exception(
            f"Received an unsuccessful status code of {resp['status']}")

except Exception as err:
    print("Test 1 FAILED: Could not make POST Request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 1 PASS: Succesfully Made POST Request to /puppies")

# Making a GET Request
print("Making a GET Request for /puppies...")
try:
    url = address + "/puppies"
    h = httplib2.Http()
    resp, result = h.request(url, "GET")
    if resp["status"] != "200":
        raise Exception(
            f"Received an unsuccessful status code of {resp['status']}")
except Exception as err:
    print("Test 2 FAILED: Could not make GET Request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 2 PASS: Succesfully Made GET Request to /puppies")

# Making GET Requests to /puppies/puppy_id
print("Making GET requests to /puppies/puppy_id ")

try:
    puppy_id = puppyID
    url = address + f"/puppies/{puppy_id}"
    h = httplib2.Http()
    resp, result = h.request(url, "GET")
    if resp["status"] != "200":
        raise Exception(
            f"Received an unsuccessful status code of {resp['status']}")


except Exception as err:
    print("Test 3 FAILED: Could not make GET Requests to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 3 PASS: Succesfully Made GET Request to /puppies/puppy_id")

# Making a PUT Request
print("Making PUT requests to /puppies/puppy_id ")

try:
    puppy_id = puppyID
    description = "+".join("A sleepy bundle of joy")
    url = f"{address}/puppies/{puppy_id}?name=wilma&description={description}"
    h = httplib2.Http()
    resp, result = h.request(url, "PUT")
    if resp["status"] != "200":
        raise Exception(
            f"Received an unsuccessful status code of {resp['status']}")

except Exception as err:
    print("Test 4 FAILED: Could not make PUT Request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 4 PASS: Succesfully Made PUT Request to /puppies/puppy_id")

# Making a DELETE Request
print("Making DELETE requests to /puppies/puppy_id ... ")

try:
    puppy_id = puppyID
    url = address + f"/puppies/{puppy_id}"
    h = httplib2.Http()
    resp, result = h.request(url, "DELETE")
    if resp["status"] != "200":
        raise Exception(
            f"Received an unsuccessful status code of {resp['status']}")


except Exception as err:
    print("Test 5 FAILED: Could not make DELETE Requests to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 5 PASS: Succesfully Made DELETE Request to /puppies/puppy_id")
    print("ALL TESTS PASSED!!")
