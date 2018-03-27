import json
faNumber = input("What is your favorite number? ")
filename = 'faNumber.json'

with open(filename, 'w') as f_obj:
    json.dump(faNumber, f_obj)
    print("We'll remember your favorite number is " + faNumber  + " when you come back!")