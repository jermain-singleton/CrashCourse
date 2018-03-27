def city_function(city, country, population=''):
    if population:
        city_format = city + ', ' + country + ' ' + str(population)
    else:
        city_format = city + ', ' + country
    return city_format.title()
