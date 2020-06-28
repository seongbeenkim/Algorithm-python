#https://www.acmicpc.net/problem/10422

import sys

t = int(sys.stdin.readline())
d = [-1] * 5001

def go(L):
    if L == 0:
        return 1
    if d[L] >= 0:
        return d[L]
    d[L] = 0
    for i in range(2, L+1, 2):
        d[L] += go(i-2) * go(L-i)
        d[L] %= 1000000007
    return d[L]

for _ in range(t):
    a = int(sys.stdin.readline())
    if a % 2 != 0:
        print(0)
    else:
        print(go(a))