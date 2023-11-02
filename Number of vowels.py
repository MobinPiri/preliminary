text = input("text : ")  # input text
counter = 0  # counter
for i in text:
    i.lower()  # It may be a big word, that's why I changed it to small
    if i == "a" or i == "i" or i == "e" or i == "o" or i == "u":
        counter += 1  # Whenever there is a vowel, one is added
print(counter)  # Print the number of vowels
