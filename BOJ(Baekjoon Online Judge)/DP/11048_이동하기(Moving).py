#https://www.acmicpc.net/problem/11048

import sys

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
d = [[0] * (m+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = max(d[i-1][j],d[i][j-1],d[i-1][j-1]) + a[i-1][j-1]
print(d[n][m])