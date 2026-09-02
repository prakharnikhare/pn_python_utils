
a = 10              #global variable

def func():
    a = 15          #local variable
    globals()['a'] = 20
    print("Inside func :", a)

func()

print("Outside func :", a)