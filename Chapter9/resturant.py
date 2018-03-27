class resturant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.numbers_served = 0
        
    def describe_resturant(self):
        print("\nThe resturant sells " + self.cuisine + ".")
        print(self.name.title() + " has a vegan only menu.")

    def open_resturant(self):
        print("The resturant is open on weekends only.")

    def increment_number_served(self, customers):
        self.numbers_served += customers

class IceCreamStand(resturant):
    def __init__(self):
        self.flavors = []
    
    def call_flavors(self):
        print("The flavors are below: ")
        for flavor in self.flavors:
            print(flavor)



call1 = IceCreamStand()
call1.flavors = ['vanilla', 'strawberry', 'chocolate']
call1.call_flavors()