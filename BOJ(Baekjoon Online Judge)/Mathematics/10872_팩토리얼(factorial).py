#https://www.acmicpc.net/problem/10872

import sys

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)
num = int(sys.stdin.readline())
print(factorial(num))
