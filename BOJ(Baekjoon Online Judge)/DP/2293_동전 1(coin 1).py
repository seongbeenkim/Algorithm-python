#https://www.acmicpc.net/problem/2293

import sys

n, k = map(int,sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
d = [0] * (k+1)
d[0] = 1

for j in range(n):
    for i in range(1,k+1):
        if i-a[j] >= 0:
            d[i] += d[i-a[j]]
print(d[k])