sandwich_orders = ['pastrami', 'Turkey', 'Ham', 'pastrami', 'Cheese', 'Bacon', 'pastrami']
finished_sandwich = []
print("The deli is out of pastrami!!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    ready = sandwich_orders.pop()

    print("The " + ready.title() + " is done.")
    finished_sandwich.append(ready)

print("\nThe following sandwich are completed: ")
for finish in finished_sandwich:
    print(finish.title())