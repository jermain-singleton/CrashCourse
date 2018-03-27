filename = "program_poll.txt"

while True:
    poll = input("Why do you like programming? ")
    if poll == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(poll + "\n")