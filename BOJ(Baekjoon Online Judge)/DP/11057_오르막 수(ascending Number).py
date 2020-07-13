#https://www.acmicpc.net/problem/11057

import sys

mod = 10007
n = 1001
d = [[0]*10 for _ in range(n)]

for i in range(10):
    d[1][i] = 1

for i in range(2,n):
    for j in range(10):
        for k in range(j+1):
            d[i][j] += d[i-1][k]
            d[i][j] %= mod
"""
for i in range(2,n):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][j]
        else:
            temp = j
            while temp >= 0:
                d[i][j] += d[i-1][temp]
                temp -= 1
        d[i][j] %= mod
"""
num = int(sys.stdin.readline())
print(sum(d[num])%mod)