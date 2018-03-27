my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods[0:]:
    print(food)

print("\nMy friend's favorite foods are:")
friend_foods.append('ice cream')
for food in friend_foods:
    print(food)