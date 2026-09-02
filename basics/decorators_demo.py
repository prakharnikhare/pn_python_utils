
def greater_first(func):
    def wrap(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrap

@greater_first
def div(a,b):
    return a/b

def sub(a,b):
    return a-b

res1 = div(5,10)
print("Div", res1)

res2 = sub(5,10)
print("sub", res2)