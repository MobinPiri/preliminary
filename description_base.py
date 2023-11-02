# This program takes the encrypted password from the user, decodes it, and prints it
# If the first letter is capital, it prints itself, and if the first letter is small, it reverses and prints
# for exam :
# input : malaS Mobin
# out :  Salam Mobin
text = input("Enter text : ")
rev = ""
m = text.split()
l=""
for i in m:
    count9 = len(i)
    if i[0].islower():
        for f in range(count9):
            l = i[f] + l
    if i[0].isupper():
        l = l + i
    rev = rev +" "+ l
    l=""
print(rev)

