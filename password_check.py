def password_check(input_password):
    lower, upper, digit, char = 0, 0, 0, 0
    if len(input_password) >= 8 and len(input_password) <= 18:
        for i in input_password:
            if i.islower() == True:
                lower += 1
            elif i.isupper() == True:
                upper += 1
            elif i.isdigit() == True:
                digit += 1
            elif i.isprintable():
                char += 1
        if lower > 1 and upper > 1 and digit > 1 and char > 1:
            return "Your password is strong "
        else:
            print("Your password is weak")
            return "A strong password must have at least 2 numbers, 2 lowercase letters, 2 uppercase letters and 2 miscellaneous letters"

    else:
        return "The character range is between 8 and 18"


print("A strong password must have at least 2 numbers, 2 lowercase letters, 2 uppercase letters and 2 miscellaneous letters")
input_password = input("password : ")
print(password_check(input_password))
