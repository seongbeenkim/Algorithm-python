#https://www.acmicpc.net/problem/11054

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d1 = [0] * n
d2 = [0] * n
d1[0] = 1
d2[0] = 1
for i in range(1,n):
    d1[i] = 1
    for j in range(i):
        if a[i] > a[j] and d1[i] < d1[j] + 1:
            d1[i] = d1[j] + 1

for i in range(n-1,-1,-1):
    d2[i] = 1
    for j in range(i+1,n):
        if a[i] > a[j] and d2[i] < d2[j] + 1:
            d2[i] = d2[j] + 1
d = [d1[i]+d2[i]-1 for i in range(n)]
print(max(d))