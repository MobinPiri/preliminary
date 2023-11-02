# for example:
# input:3
# out :  *
#       ***
#        *
a = int(input("Enter number : "))
for i in range(1,a+1,2):
    print(("*"*i).center(a))
for m in range(a-2,0,-2):
     print(("*"*m).center(a))