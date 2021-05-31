import codecs
import json
import sys

import httplib2

# sys.stdout = codecs.getwriter("utf8")(sys.stdout)
# sys.stderr = codecs.getwriter("utf8")(sys.stderr)
err = "Received an unsuccessful status code of {}"

print("Running Endpoint Tester....\n")
print("Please enter the address of the server you want to access.")
print("Press Enter to use http://localhost:5000: ", end="")
address = input()
if address == "":
    address = "http://localhost:5000"
# TEST ONE -- CREATE NEW RESTAURANTS
base_url = f"{address}/restaurants"
try:
    print("Test 1: Creating new Restaurants......")
    url = f"{base_url}?location=Buenos+Aires+Argentina&mealType=Sushi"
    h = httplib2.Http()
    resp, result = h.request(url, "POST")
    if resp["status"] != "200":
        raise Exception(err.format(resp['status']))
    print(json.loads(result))

    url = f"{base_url}?location=Denver Colorado&mealType=Soup"
    h = httplib2.Http()
    resp, result = h.request(url, "POST")
    if resp["status"] != "200":
        raise Exception(err.format(resp['status']))
    print(json.loads(result))

    url = f"{base_url}?location=Prague+Czech+Republic&mealType=Crepes"
    h = httplib2.Http()
    resp, result = h.request(url, "POST")
    if resp["status"] != "200":
        raise Exception(err.format(resp['status']))
    print(json.loads(result))

    url = f"{base_url}?location=Shanghai+China&mealType=Sandwiches"
    h = httplib2.Http()
    resp, result = h.request(url, "POST")
    if resp["status"] != "200":
        raise Exception(err.format(resp['status']))
    print(json.loads(result))

    url = f"{base_url}?location=Nairobi+Kenya&mealType=Pizza"
    h = httplib2.Http()
    resp, result = h.request(url, "POST")
    if resp["status"] != "200":
        raise Exception(err.format(resp["status"]))
    print(json.loads(result))

except Exception as err:
    print("Test 1 FAILED: Could not add new restaurants")
    print(err.args)
    sys.exit()
else:
    print("Test 1 PASS: Succesfully Made all new restaurants")

# TEST TWO -- READ ALL RESTAURANTS
try:
    print("Attempting Test 2: Reading all Restaurants...")
    url = address + "/restaurants"
    h = httplib2.Http()
    resp, result = h.request(url, "GET")
    print(resp)
    if resp["status"] != "200":
        raise Exception(err.format(resp["status"]))
    all_result = json.loads(result)
    print(result)

except Exception as err:
    print("Test 2 FAILED: Could not retrieve restaurants from server")
    print(err.args)
    sys.exit()
else:
    print("Test 2 PASS: Succesfully read all restaurants")
    # TEST THREE -- READ A SPECIFIC RESTAURANT
    try:
        print("\n\n\n*****************************************************")
        print("Attempting Test 3: Reading the last created restaurant...")
        result = all_result
        restID = result["restaurants"][len(result["restaurants"]) - 1]["restaurant_id"]
        print(restID)
        url = address + f"/restaurants/{restID}"
        print(url)
        h = httplib2.Http()
        resp, result = h.request(url, "GET")
        print(resp)
        if resp["status"] != "200":
            raise Exception(err.format(resp["status"]))
        print(json.loads(result))

    except Exception as err:
        print("Test 3 FAILED: Could not retrieve restaurant from server")
        print(err.args)
        sys.exit()
    else:
        print("Test 3 PASS: Succesfully read last restaurant")

    # TEST FOUR -- UPDATE A SPECIFIC RESTAURANT
    try:
        print("""Attempting Test 4: Changing the name, image, and address of the
        first restaurant to Udacity...""")
        result = all_result
        restID = result["restaurants"][0]["restaurant_id"]
        url = address + f"""/restaurants/{restID}?name=Udacity&address=2465+
        Latham+Street+Mountain+View+CA&image=https://media.glassdoor.com/l/70
        /82/fc/e8/students-first.jpg"""
        h = httplib2.Http()
        resp, result = h.request(url, "PUT")
        if resp["status"] != "200":
            raise Exception(err.format(resp["status"]))
        print(json.loads(result))

    except Exception as err:
        print("Test 4 FAILED: Could not update restaurant from server")
        print(err.args)
        sys.exit()
    else:
        print("Test 4 PASS: Succesfully updated first restaurant")

# TEST FIVE -- DELETE SECOND RESTARUANT
try:
    print(
        "Attempting Test 5: Deleteing the second restaurant from the server...")
    result = all_result
    restID = result["restaurants"][1]["restaurant_id"]
    url = address + f"/restaurants/{restID}"
    h = httplib2.Http()
    resp, result = h.request(url, "DELETE")
    if resp["status"] != "200":
        raise Exception(err.format(resp["status"]))
    print(result)

except Exception as err:
    print("Test 5 FAILED: Could not delete restaurant from server")
    print(err.args)
    sys.exit()
else:
    print("Test 5 PASS: Succesfully updated first restaurant")
    print("ALL TESTS PASSED!")
