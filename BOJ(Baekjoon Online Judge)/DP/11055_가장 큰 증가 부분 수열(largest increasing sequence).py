#https://www.acmicpc.net/problem/11055

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d = [0] * n
d[0] = a[0]

for i in range(1,n):
    d[i] = a[i]
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + a[i]:
            d[i] = d[j] + a[i]
print(max(d))