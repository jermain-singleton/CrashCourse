class Employee_Information():
    """Gather first, last name and salary from the user."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = 0
    
    def give_raise(self, raiseA=5000):
        self.annual_salary += raiseA
    
    def read_salary(self):
        print("The salary is " + str(self.annual_salary) + ".")

