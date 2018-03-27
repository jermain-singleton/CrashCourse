motorcycle = ['honda', 'yamaha', 'suzuki']
motorcycle.insert(1, 'ducati')
print(motorcycle)


too_expensive = 'ducati'
motorcycle.remove(too_expensive)
print(motorcycle)
print("\nA " + too_expensive.title() + " is too expensive for me.")