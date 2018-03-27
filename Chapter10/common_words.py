filename = 'Gutenberg.txt'

with open(filename, encoding='utf-8') as f_obj:
    contents = f_obj.read()
    numbers = contents.count('the')


print(numbers)