available_toppings = ['mushrooms', 'green pepper', 'extra cheese',
                      'pepperoni', 'pinapple', 'olives']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print("Adding " + topping + ".")
    else:
        print('Sorry, we don\'t have ' + topping + ".")
print("\nFinished making your pizza.")