age = input("Give me your age: ")
age = int(age)
if age < 3:
    price = 0
elif age >= 3 and age <= 12:
    price = 10
elif age >= 12:
    price = 15

print("The price for the ticket is $" + str(price) + ".")