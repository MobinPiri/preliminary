a = input("please enter : ")
var = int(a)
while True:
    var += 1
    a = str(var)
    if len(set(a)) == 4:
        print(var)
        break
