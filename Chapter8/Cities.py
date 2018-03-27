def describe_city(city, state='Iceland'):
    message = "My favorite city is " + city.title() + \
    " and I would like to visit " + state.title() + "."
    print(message)
describe_city('New York City')
describe_city('Columbia')
describe_city('Philly', 'California')