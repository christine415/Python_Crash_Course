class Restaurant():
    '''Model a restaurant'''
    def __init__(self, name, cuisine_type):
        '''Initialize restaurant's name, cuisine type, and the number of customers that have been served'''
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Describe the restaurant's name and cuisiine type'''
        print("The restaurant's name is " + self.name.title() + ".")
        print("The cuisine type that restaurant serves is " + self.cuisine_type.title() + ".")
    
    def open_restaurant(self):
        '''Simulate an restaurant open'''
        print("The restaurant is now open.")
    
    def set_number_served(self, number):
        '''Set the number of customers that have been served'''
        if number >= self.number_served:
            self.number_served = number
        else:
            print("The number of customers that have been served cannot roll back.")
    
    def increment_number_served(self, number):
        '''Increment the number of customers that have been served in a business day'''
        self.number_served += number

restaurant = Restaurant("Gyu_kaku", "Japanese")
#restaurant.number_served = 10
#restaurant.set_number_served(10)
restaurant.increment_number_served(10)
restaurant.increment_number_served(20)
print(restaurant.name)
print(restaurant.cuisine_type)
print("The restaurant has served " + str(restaurant.number_served) + " customers." )
restaurant.describe_restaurant()
restaurant.open_restaurant()
