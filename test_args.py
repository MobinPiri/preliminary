import random
def name(*args):
    b = random.randint(0, 4)
    print("case 1 : ", args[b])
    c = random.randint(0, 4)
    print("case 2 : ", args[c])
    print(args)


name("mobin", "shiva", "ali", "sina", "akbar")
