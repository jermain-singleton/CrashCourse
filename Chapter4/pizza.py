pizzas = ['pepperoni', 'sausage', 'cheese']
friend_pizza = pizzas[:]

pizzas.append('ham')
friend_pizza.append('Triple cheese')
print("My favorite pizza are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizza are:")
for pizza in friend_pizza:
    print(pizza)