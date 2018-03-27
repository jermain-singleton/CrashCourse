import json

filename = 'faNumber.json'
with open(filename) as f_obj:
    faNumber = json.load(f_obj)
    print("Welcome back, your favorite number is " + faNumber + "!!!!")