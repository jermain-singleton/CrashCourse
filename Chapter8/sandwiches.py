addons = ['mustard', 'cheese', 'mushroom', 'ketchup']

def sandwich_addon(*add):
    """Print the addons a person needs"""
    print("the adds for the sandwich are: ")
    for ad in add:
        print(ad)
sandwich_addon("mustard", "cheese")
    