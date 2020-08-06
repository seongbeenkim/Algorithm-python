#https://www.acmicpc.net/problem/16929

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

a = [sys.stdin.readline().rstrip() for _ in range(n)]
check = [[False] * m for _ in range(n)]
d = [[-1] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i,j,color,cnt):
    if check[i][j]:
        if cnt - d[i][j] >= 4:
            return True
        else:
            return False
    d[i][j] = cnt
    check[i][j] = True

    for k in range(4):
        nx = dx[k] + i
        ny = dy[k] + j

        if 0 <= nx < n and 0 <= ny < m and color == a[nx][ny]:
            if dfs(nx,ny,color,cnt+1):
                return True

    return False

is_cycled = False
for i in range(n):
    for j in range(m):
        if d[i][j] == -1:
            if dfs(i,j,a[i][j],1):
                is_cycled = True
                break

    if is_cycled:
        break

print("Yes" if is_cycled else "No")