sandwich_orders = ["tuna sandwich", "pastrami", "ham sandwich", "pastrami","beef sandwich", "pastrami", "chicken sandwich"]
finished_sandwiches = []
print("Restaurant is run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
    print(sandwich + " is made.")

