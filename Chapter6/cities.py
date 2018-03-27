cities = {
    'James Island': {'pop': "50000", 'country': "USA", 'fact': 'has a beach'},
    'Charleston': {'pop': "100000", 'country': "USA", 'fact': 'hateful people'},
}

for town, info in cities.items():
    print("\n" + town.title() + ":")
    population = info['pop']
    country = info['country']
    fact = info['fact']

    print("\t" + "Population: " + population)
    print("\t" + "Country: " + country)
    print("\t" + "Fact: " + fact)