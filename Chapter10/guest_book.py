filename = 'guestBook.txt'
while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + '\n')