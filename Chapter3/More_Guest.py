guest = ["Buddah", "Mo", "Tia"]
guest[2] = "Malcolm"
print("I have found a bigger table for everyone to use")
guest.insert(0, 'John')
guest.insert(2, 'Mohammad')
guest.append('Antoine')
print(guest)
print("I will only be able to invite two guest to the banquest.")
print(guest.pop() + " the banquet will be for another date.")
print(guest.pop() + " the banquet will be for another date.")
print(guest.pop() + " the banquet will be for another date.")
print(guest.pop() + " the banquet will be for another date.")
print(guest)

print(guest[0] + " the banquet is on Monday.")
print(guest[1] + " the banquet is on Monday.")
del guest[1]
del guest[0]
print(guest)
