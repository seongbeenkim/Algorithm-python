#https://www.acmicpc.net/problem/1890

import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]

d[0][0] = 1

for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            continue
        if j + a[i][j] < n:
            d[i][j+a[i][j]] += d[i][j]
        if i + a[i][j] < n:
            d[i+a[i][j]][j] += d[i][j]

print(d[n-1][n-1])
