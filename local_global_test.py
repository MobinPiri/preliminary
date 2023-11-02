def outer_func():
    x = "python"
    def inner_func():
        global x
        x = "c#"
        print("x inner : ",x)

    inner_func()
    print("x outer : ",x)
outer_func()
print("x main : ",x)
