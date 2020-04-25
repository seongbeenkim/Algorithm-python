#https://www.acmicpc.net/problem/1476

import sys

E,S,M = map(int,sys.stdin.readline().split())

E -= 1
S -= 1
M -= 1
i = 0
while True:
    if i % 15 == E and i % 28 == S and i % 19 == M:
        print(i+1)
        break
    i += 1
"""
e,s,m = 1,1,1
year = 1
while True:
    if e == E and s == S and m == M:
        break
    e += 1
    s += 1
    m += 1
    year += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
print(year)
"""