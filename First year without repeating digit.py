sal = input("Enter : ")  # input year
salint = int(sal) + 1
bol = True
while (bol):
    sal = str(salint)
    if len(set(sal)) == 4:
        print(salint)
        bol = False
    else:
        salint += 1