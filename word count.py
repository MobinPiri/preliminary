var = input("your text : ")
Dict={}
for i in var:
    if i!=" ":
        if i not in Dict:
            Dict.setdefault(i,1)
        else :
            Dict[i]+=1
for key , value in Dict.items():
    print(key , " : ", value)
