# java script object notation
# (independent of javascript)
# used in databases and APIS
# used to transfer data

# Serialization : encoding : converting python list to Json
# deserialiation : decoding : reading Json data into a python list

import json
import pprint as pprint

data_recruits = {
    "recruit": {
        "name": "Jim Raynor",
        "age": 18
    }
}

# Serializing JSON data
with open("data_file.json", "w") as write_file:
    json.dump(data_recruits, write_file, indent=4)



json_str = json.dumps(data_recruits, indent=4)
print(json_str)
json_str = json.dumps(data_recruits)
print(json_str)
# deserialiation with JSON data
marine_tuple = (8, "HP")
encoded_marine = json.dumps(marine_tuple)
decoded_marine = json.loads(encoded_marine)
type(decoded_marine)
decoded_marine

marine_tuple == tuple(decoded_marine)

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
                todos_by_user[todo["userId"]] = 1

top_users = sorted(todos_by_user.items(),
                    key=lambda x: x[1], reverse=True
