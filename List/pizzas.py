pizzas = ["Cheese", "Hawaiian", "Barbeque"]
friend_pizzas = pizzas[:]
pizzas.append("Pepperoni")
friend_pizzas.append("New York Style")
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are: ")
for fpizza in friend_pizzas:
    print(fpizza)