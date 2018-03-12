active = True
filename = 'guest_book.txt'
with open(filename, 'w') as file_object:
    while active:
        name = input("Tell me your name(type 'quit' to exit the program): ")
        if name == 'quit':
            active = False
        else:
            print("Hello, " + name + "!")
            file_object.write(name + '\n')
