locations = ["Australia", "Spain", "Sweden", "Japan", "Thai"]
# Print your list in its original order
print(locations)

# Use sorted() to print your list in alphabetical order without modifying the actual list 
print(sorted(locations))

# Show that your list is still in its original order by printing it
print(locations)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
print(sorted(locations, reverse=True))

# Show that your list is still in its original order by printing it again
print(locations)

# Use reverse() to change the order of your list 
locations.reverse()
print(locations)

# Use reverse() to change the order of your list again  
locations.reverse()
print(locations)

# Use sort() to change your list so it’s stored in alphabetical order  
locations.sort()
print(locations)

# Use sort() to change your list so it’s stored in reverse alphabetical order
locations.sort(reverse=True)
print(locations)