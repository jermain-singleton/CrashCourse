def make_car(manufactor, model, **car_info):
    car = {}
    car['type'] = manufactor
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car_profile = make_car('Honda', 'insight',
                    package='LS', doors4=False)
print(car_profile)