#https://www.acmicpc.net/problem/1309

import sys

n = int(sys.stdin.readline())
d = [[0] * 3 for _ in range(n+1)]
d[0][0] = 1
mod = 9901
for i in range(1,n+1):
    d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % mod
    d[i][1] = (d[i-1][0] + d[i-1][2]) % mod
    d[i][2] = (d[i-1][0] + d[i-1][2]) % mod
print(sum(d[n]) % mod)