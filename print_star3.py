# for example :
# input: 3
# out:        *
#             **
#             ***
#             **
#             *
a=int(input("Enter number : "))
for i in range(1,a+1):
    print("*"*i)
    if i==a:
        i-=1
        while i>=1:
            print("*"*i)
            i-=1