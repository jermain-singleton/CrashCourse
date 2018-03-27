favorite_place = {
    'Donald': ['beach', 'farm', 'zoo'],
    'Effi': ['beach'],
    'Liunt': ['home', 'island'],
}

for name, location in favorite_place.items():
    print("\n" + name.title() + ":")
    for locale in location:
        print("\t" + locale.title())