#https://www.acmicpc.net/problem/1699

import sys

n = int(sys.stdin.readline())
d = [0] *(n+1)
d[1] = 1

for i in range(1,n+1):
    d[i] = i

for i in range(2,n+1):
    j = 2
    while j*j <= i:
        if d[i] > d[i-(j*j)] + 1:
            d[i] = d[i-(j*j)] + 1
        j += 1
print(d[n])