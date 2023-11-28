# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not..
List = ["Mobin", "Kian", "Rayan", "Shiva", "Mohamad", "Ali", "piri", "Hasty"]
result = list(filter(lambda x: len(x) == 4, List))
print(f"your friend is : {result}")
