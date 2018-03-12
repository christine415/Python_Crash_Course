class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, raise_amount=0):
        if raise_amount != 0:
            self.salary += raise_amount
        else:
            self.salary += 5000
