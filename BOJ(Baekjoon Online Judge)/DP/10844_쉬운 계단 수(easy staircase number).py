#https://www.acmicpc.net/problem/10844
import sys

max = 101
d = [[0] * 10 for i in range(max)]
mod = 1000000000
for i in range(1,10):
    d[1][i] = 1

for i in range(2,max):
    for j in range(10):
        if 1 <= j <= 8:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
        elif j == 9:
            d[i][j] = d[i-1][j-1]
        elif j == 0:
            d[i][j] = d[i-1][j+1]
        d[i][j] %= mod

n = int(sys.stdin.readline())
print(sum(d[n])%mod)


"""
n = int(sys.stdin.readline())
d = [[0] * 10 for _ in range(n+1)]
mod = 1000000000
for i in range(1,10):
    d[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j > 0:
            d[i][j] += d[i-1][j-1]
        d[i][j] %= mod
        if j < 9:
            d[i][j] += d[i-1][j+1]
        d[i][j] %= mod
print(sum(d[n])%mod)
"""
