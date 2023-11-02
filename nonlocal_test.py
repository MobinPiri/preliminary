def outer_func():
    x = "python"
    def inner_func():
        nonlocal x
        x = "html"
        print("inner x: ",x)
    inner_func()
    print("inner x : ",x)
outer_func()
