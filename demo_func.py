"""demo function with arguments"""

def person(name, **kwlargs):     #keyword lenght arguments
    print("Name : ", name)
    for k,v in kwlargs.items():
        print(k, " : ", v)

person(name='Prakhar', age=20, loc='Pune',tech='Python')



# def person(name, age):
#     print("Name : ", name)
#     print("Age : ", age)

# person('Prakhar', 20)
# # person(40, 'Sonal')
# person(age=40, name='Sonal')     #keyword arguments

# def add(num1=0, num2=0): #default argument
#     return num1 + num2

# def add(num1, *num2):      #variable length argument
#     print(num1)
#     print(num2)
#     return 0

# result = add(4,5,6,7,8)

# print(result)
