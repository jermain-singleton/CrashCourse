import json

filename = 'faNumber.json'
try:
    with open(filename) as f_obj:
        faNumber = json.load(f_obj)
except FileNotFoundError:
    faNumber = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(faNumber, f_obj)
        print("We'll remember your favorite number is " + faNumber  + " when you come back!")
else:
    print("Welcome back, your favorite number is " + faNumber + "!!!!")

    