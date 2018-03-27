users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, nothing to report.")
        else:
            print("Hello "+ user + "are you ready?")
else:
    print("The list is empty.")