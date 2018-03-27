def city_country(city, country):
    format = city + ", " + country
    return format


locales = city_country('Paris', 'France')
print(locales)