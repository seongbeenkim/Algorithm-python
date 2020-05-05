#https://www.acmicpc.net/problem/15990

import sys

max = 100001
mod = 1000000009
d = [[0] * 4 for i in range(max)]
#d[0][1] = d[0][2] = d[0][3] = 1
for i in range(1, max):
    if i - 1 >= 0:
        d[i][1] = d[i - 1][2] + d[i - 1][3]
        if i == 1:
            d[i][1] = 1
    if i - 2 >= 0:
        d[i][2] = d[i - 2][1] + d[i - 2][3]
        if i == 2:
            d[i][2] = 1
    if i - 3 >= 0:
        d[i][3] = d[i - 3][1] + d[i - 3][2]
        if i == 3:
            d[i][3] = 1

    d[i][1] %= mod
    d[i][2] %= mod
    d[i][3] %= mod

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    print(sum(d[n]) % mod)