a = 5

def square(num):
    return num * num

def cube(num):
    return num * num * num

def operate(num, func):       #higher order function
    return func(num)

res = operate(a, square)
print(res)
res1 = operate(a, cube)
print(res1)