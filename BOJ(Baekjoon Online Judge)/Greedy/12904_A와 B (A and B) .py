#https://www.acmicpc.net/problem/12904

import sys

s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())

if len(s) >= len(t):
    if s == t:
        print(1)
    else:
        print(0)

while len(t) > len(s):
    if t[-1] == "A":
        t.pop()
    else:
        t.pop()
        t.reverse()

if s == t:
    print(1)
else:
    print(0)