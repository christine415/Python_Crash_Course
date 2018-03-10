motorcycles = ["Honda", "Yamaha", "Suzuki"]
# Insert Ducati to the beginning of list motorcycles
motorcycles.insert(0, "Ducati")
print(motorcycles)

# Delete the first item in list motorcycles
del motorcycles[0]
print(motorcycles)

# Remove an item by using pop() method
popped_motorcycles = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycles)

# Remove by value
# remove() deletes only the first occurrance of value you specify
motorcycles = ["Honda", "Yamaha", "Suzuki"]
motorcycles.remove("Honda")
print(motorcycles)