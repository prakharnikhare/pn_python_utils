

def outer():
    print("In outer function")

    def inner(n):
        print("In Inner function", n)

    return inner


calling = outer()
calling(5)
