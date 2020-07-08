#https://www.acmicpc.net/problem/1935

import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().rstrip()
alphabet = {}

for i in range(n):
    alphabet[chr(65+i)] = int(sys.stdin.readline())
stack = []

for i in arr:
    if i in alphabet:
        stack.append(alphabet[i])
    else:
        second = stack.pop()
        first = stack.pop()
        if i == "+":
            stack.append(first+second)
        elif i == "-":
            stack.append(first-second)
        elif i == "*":
            stack.append(first*second)
        else:
            stack.append(first/second)
print('%.2f' % stack[0])