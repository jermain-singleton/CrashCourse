import random
age = random.randint(1, 70)
if age < 2:
    print("baby")
elif age > 2 and age < 4:
    print("toddler")
elif age > 4 and age < 13:
    print("kid")
elif age > 13 and age < 20:
    print("teenager")
elif age > 20 and age < 65:
    print("adult")
elif age > 65:
    print("elder")
