#https://www.acmicpc.net/problem/17086

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [0,0,1,-1,-1,1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]

MIN = -1
answer = -1

def bfs(i,j):
    check = [[False] * m for _ in range(n)]
    q = deque()
    q.append((i,j,0))
    check[i][j] = True

    while q:
        x, y, d = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:
                if a[nx][ny] == 1:
                    return d + 1
                check[nx][ny] = True
                q.append((nx,ny,d+1))

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            res = bfs(i,j)
            answer = max(res,answer)

print(answer)