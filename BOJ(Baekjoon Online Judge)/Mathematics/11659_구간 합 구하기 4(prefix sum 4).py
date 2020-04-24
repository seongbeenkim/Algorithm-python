#https://www.acmicpc.net/problem/11659

import sys

n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
d = [0] * n
d[0] = a[0]
for i in range(1,n):
    d[i] = d[i-1] + a[i]

for _ in range(m):
    i, j = map(int,sys.stdin.readline().split())
    if i == 1:
        print(d[j-1])
    else:
        print(d[j - 1] - d[i - 2])