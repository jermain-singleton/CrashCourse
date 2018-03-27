def read_files(filename):
    try:
        with open(filename) as file_object:
            lines = file_object.read()
    except FileNotFoundError:
        msg = "The file is not in dir: " + filename
        print(msg)
    else:
        print(lines)

files = ['cat.txt', 'dog.txt', 'app.txt']
for file in files:
    read_files(file)





# filename = ['cat.txt', 'dog.txt']
# for file in filename:
#     read_files(filename)