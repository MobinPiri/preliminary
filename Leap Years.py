
def is_leap_year(year):
    # your code here. Try to do it in one line.
    if 1600 < input_user and input_user < 4000:
        if input_user % 400 == 0:
            return True
        elif input_user % 100 == 0:
            return False
        elif input_user % 4 == 0:
            return True
        else:
            return False
    else:
        print("invalid")
        print("please again!")
        return ("Tested years are in range 1600 ≤ year ≤ 4000")
input_user = int(input("enter year : "))
print(is_leap_year(input_user))
