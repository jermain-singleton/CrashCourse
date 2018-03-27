favorite_numbers = {
    'jen': [10,100,50],
    'sarah': [3,7,11],
    'edward': [1001,1],
    'phil': [505,5],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " numbers are:")
    for number in numbers:
        print("\t" + str((number)))