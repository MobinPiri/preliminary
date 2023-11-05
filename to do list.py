to_do_list = []
i=1
while True:
    print("your list : ")
    for value in to_do_list:
        print(i , " : " , value)
        i+=1
    print("----------------------------------------------------------")
    print("1 : add task ")
    print("2 : remove task")
    print("3 : exit")
    input_user = input("Which option do you want? ").lower()
    if input_user == "1" or input_user == "add task":
        a = input("add task : ")
        to_do_list.append(a)
        print("task added successful")
    elif input_user == "2" or input_user == "remove task":
        a = int(input("Which one of the task do you want to delete? "))
        if 1<=a and a<=len(input_user):
            to_do_list.pop(a - 1)
            i-=1
        else :
            print("The entered number is incorrect")
    elif input_user == "3" or input_user == "exit":
        break
    else:
        print("The entered number is incorrect")
