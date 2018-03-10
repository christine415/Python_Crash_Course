# Use a for loop to print the numbers from 1 to 20, inclusive
for num in range(1,21):
    print (num)

# Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and ends at one million  
# Also, use the sum() function to see how quickly Python can add a million numbers 
numbers = [num for num in range(1, 1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20  
# Use a for loop to print each number
for odd in range(1,21,2):
    print(odd)

# Make a list of the multiples of 3 from 3 to 30  
# Use a for loop to print the numbers in your list 
for three in range(3, 31, 3):
    print(three)

# Make a list of the  first 10 cubes (that is, the cube of each integer from 1 through 10), 
# and use a for loop to print out the value of each cube 
for num in range(1,11):
    print(num**3)

# Use a list comprehension to generate a list of the  rst 10 cubes 
cubes = [num**3 for num in range(1,11)]
print (cubes)