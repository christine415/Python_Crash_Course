print("Give me two numbers, and I'll add them up.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("Please input a numerical number.")
    else:
        print(first_number+second_number)
    
