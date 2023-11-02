def func(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return func(x - 1) + func(x - 2)


var = int(input("please enter number : "))
for i in range(1,var):
    print(func(i),end=" ")
