#acmicpc.net/problem/17070

import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
d = [[[0]*3 for _ in range(n)] for _ in range(n)]

d[0][1][0] = 1
for i in range(n):
    for j in range(n):
        if j+1 < n and a[i][j+1] == 0:
            d[i][j+1][0] += d[i][j][0] + d[i][j][2]
        if i+1 < n and a[i+1][j] == 0:
            d[i+1][j][1] += d[i][j][1] + d[i][j][2]
        if i+1 < n and j+1 < n and a[i+1][j+1] == 0 and a[i][j+1] == 0 and a[i+1][j] == 0:
            d[i+1][j+1][2] += d[i][j][0] + d[i][j][1] + d[i][j][2]
ans = 0
for i in range(3):
    if d[n-1][n-1][i] != 0:
        ans += d[n-1][n-1][i]
print(ans)