text=input("Enter : ")
Dict={}
for i in text :
    i.lower()
    if i in "aeiou":
        if i in Dict:
            Dict[i]+=1
        else :
            Dict[i]=1
for key , value in Dict.items():
    print(key , " : ", value)


