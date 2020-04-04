#https://www.acmicpc.net/problem/11048

import sys

n, m = map(int,sys.stdin.readline().split())
a = [[0] * (m+1)] + [[0] + list(map(int,sys.stdin.readline().split())) for i in range(n)]
d = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = max(d[i-1][j],d[i][j-1]) + a[i][j]
print(d[n][m])

"""
def dp(x,y):
    if x>n or y>m:
        return 0
    if d[x][y] >= 0:
        return d[x][y]
    d[x][y] = max(dp(x+1,y),dp(x,y+1)) + a[x][y]
    return d[x][y]
print(dp(1,1))
"""

"""
d[1][1] = a[1][1]
for i in range(1,n+1):
    for j in range(1,m+1):
        if i+1 <= n:
            d[i+1][j] = max(d[i+1][j],d[i][j] + a[i+1][j])
        if j+1 <= m:
            d[i][j+1] = max(d[i][j+1],d[i][j] + a[i][j+1])
print(d[n][m])
"""