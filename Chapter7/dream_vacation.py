responses = {}
active = True
while active:
    name = input("What is your name? ")
    vacation = input("What is your dream vacation?  ")

    responses[name] = vacation

    print("\nWould you like to exit or repeat?  ")
    repeat = input('y/n')
    if repeat == 'n':
        active = False
for name, vacation in responses.items():
    print("Name: " + name.title() + "\nVacation:" + vacation)