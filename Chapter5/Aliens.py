import random
alien_color = ['green', 'yellow', 'red']
r = random.choice(alien_color)
if r == 'green':
    print("Player earned 5 points!")
elif r == 'yellow':
    print("Player earned 10 points!")
elif r == 'red':
    print("Player earned 15 points!")
