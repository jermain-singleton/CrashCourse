favorite_poll = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'eric': 'null',
    'sam': 'null',
    }


for name, lang in favorite_poll.items():
    if lang != 'null':
        print(name.title() + " thanks for taking the poll.")
    else:
        print(name.title() + " please take the poll.")