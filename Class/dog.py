class Dog():
    '''A simple attempt to model a dog'''

    def __init__(self, name, age):
        '''Initialize name and age'''
        self.age = age
        self.name = name
    
    def sit(self):
        '''Simulate a dog sitting in response to the command'''
        print(self.name.title() + " now is sitting.")

    def roll_over(self):
        '''Simulate a dog rolling over in response to the command'''
        print(self.name.title() + " rolled over.")

my_dog = Dog("william", 6)
print(my_dog.name)
my_dog.sit()
my_dog.roll_over()