from functools import reduce

list1 = [4,5,9,6,10,2,3]

evens = list(filter(lambda n : n % 2 == 0, list1))
doubles = list(map(lambda n : n * 2, evens))
sum_it = reduce(lambda a,b: a + b, doubles)

print("Evens :", evens)
print("Doubles :", doubles)
print("Sum_it :", sum_it)
