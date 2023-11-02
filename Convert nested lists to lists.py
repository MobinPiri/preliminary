def func(x):
    temp_List = []
    for i in x:
        if isinstance(i, int):
            temp_List.append(i)
        else:
            temp_List.extend(func(i))
    return temp_List


List = [1, 2, 3, [4, 5, 6], 7, 8, [[9]], 10]
new_List = func(List)
print(new_List)
