def make_shirt(text, size='Large'):
    message = "The shirt size is " + size + " and reads " + text + "."
    print(message)
make_shirt('medium', 'big')
make_shirt(size='small', text='lose some weight!!')
make_shirt(text='default')