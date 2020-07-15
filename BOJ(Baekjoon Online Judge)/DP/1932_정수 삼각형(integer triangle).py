#https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline())
d = [[0]*(n+1) for _ in range(n+1)]
a = [0]
for i in range(n):
    a.append([0] + list(map(int,sys.stdin.readline().split())))

d[1][1] = a[1][1]

for i in range(2,n+1):
    for j in range(1,i+1):
        if d[i][j] == 0:
            d[i][j] = a[i][j]

        if j == 1:
            d[i][j] = d[i-1][j] + a[i][j]
            continue

        elif j == i:
            d[i][j] = d[i-1][j-1] + a[i][j]
            continue

        if d[i][j] < d[i-1][j-1] + a[i][j]:
            d[i][j] = d[i-1][j-1] + a[i][j]

        if d[i][j] < d[i-1][j] + a[i][j]:
            d[i][j] = d[i-1][j] + a[i][j]

print(max(d[n]))
