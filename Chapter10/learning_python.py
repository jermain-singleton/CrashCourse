filename = 'learn_python.txt'

with open(filename) as file_object:
    text = file_object.readlines()
    
for line in text:
    line = line.replace('Python', 'C')
    print(line.rstrip())