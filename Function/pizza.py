# Use * when we do not know how many arguments will be passed in. 
# All the input arguments will be packed into a tuple.
def make_pizza(*toppings):
    '''Print the list of toppings that have been requested.'''
    print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms","pepperoni","pinapple")