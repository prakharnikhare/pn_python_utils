import sys
from time import sleep

sys.setrecursionlimit(500)

print(sys.getrecursionlimit())

cnt = 1

def greet():
    global cnt
    print("Hello :", cnt)
    sleep(5)
    cnt += 1
    greet()

greet()