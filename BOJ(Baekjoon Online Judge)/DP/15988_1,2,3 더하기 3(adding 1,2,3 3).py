#https://www.acmicpc.net/problem/15988

import sys

t = int(sys.stdin.readline())
mod = 1000000009
d = [0] * (1000001)
d[0] = d[1] = 1
d[2] = 2
for i in range(3, 1000001):
    d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % mod
"""
d[0] = 1
for i in range(1, 1000000+1):
    if i-1 >= 0:
        d[i] += d[i-1]
    if i-2 >= 0:
        d[i] += d[i-2]
    if i-3 >= 0:
        d[i] += d[i-3]
    d[i] %= mod
"""
for _ in range(t):
    n = int(sys.stdin.readline())
    print(d[n])