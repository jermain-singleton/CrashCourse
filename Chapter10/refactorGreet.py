import json

def check_name():
    checkName = input("What is your name? ")
    return checkName

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username(checkName):
    """Prompt for a new username."""
    print("Welcome, " + checkName)
    username = checkName
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    checkName = check_name()
    if username == checkName:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username(checkName)
        print("We'll remember you when you come back, " + username + "!")
greet_user()