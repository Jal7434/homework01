# Generate five random pairs of latitudes between 16.0-18.0 degrees North
# and longitudes between 82.0-84.0 degrees East
import random
import json

def generate_latitude():
    # Use uniform to generate a random float within the ranges specified
    return random.uniform(16.0, 18.0)

def generate_longitude():
    # Use uniform to generate a random float within the ranges specified
    return random.uniform(82.0, 84.0)

def generate_composition():
    # Use comp to select a compostion from the list
    comp = ["stony", "iron", "stony-iron"]
    
    return random.choice(comp) 
def main():
    data = {}
    data["sites"] = []
    for i in range(5):
        data["sites"].append({"site_id" : (i + 1),
            "latitude" : generate_latitude(),
            "longitude" : generate_longitude(),
            "composition" : generate_composition()})
    with open("data.json", "w") as outfile:
        json.dump(data, outfile,indent=4)


main()
