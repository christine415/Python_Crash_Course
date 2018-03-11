magicians = ["David Cooperfield", "Ricky Jay", "Criss Angel"]

def show_magicians(magicians):
    for magician in magicians:
        print (magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "Great " + magicians[i]
    show_magicians(magicians)

# Does not modify the original list magicians
make_great(magicians[:])
print(magicians)