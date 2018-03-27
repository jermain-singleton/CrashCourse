major_rivers = {'nile': 'egypt',
                'congo': 'congo',
                'tana': 'nairobi'}

for rivers, country in major_rivers.items():
    print("The " + rivers.title() + " runs in " + country.title() + ".")