'''guessing game
The computer chooses a random number between 0 and 100
The user has to guess which number the computer has guessed
The user has 5 chances'''
from random import randint

value = randint(1, 100)
for i in range(1, 6):
    user_input = int(input(f"Your {i} guess between 0 and 100 = "))
    if user_input == value:
        print("Well done, you guessed right")
        break
    elif i == 5:
        print("you lost")
        print("You took advantage of all your opportunities")
        print(f"The target number of the system was {value}")
    elif user_input > value:
        print("TOO HIGH! try again ")
    else:
        print("TOO LOW! try again ")
