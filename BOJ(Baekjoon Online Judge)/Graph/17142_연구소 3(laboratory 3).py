#https://www.acmicpc.net/problem/17142

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split()))for _ in range(n)]
v = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = -1

for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            v.append((i,j))


def bfs():
    q = deque()
    d = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if a[i][j] == 3:
                q.append((i,j))
                d[i][j] = 0

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                if a[nx][ny] != 1:
                    d[nx][ny] = d[x][y] +1
                    q.append((nx,ny))

    cur = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] != 1:
                if d[i][j] == -1:
                    return
                if cur < d[i][j]:
                    cur = d[i][j]
    global ans
    if ans == -1 or ans > cur:
        ans = cur

def go(index,cnt):
    if index == len(v):
        if cnt == m:
            bfs()
    else:
        x,y = v[index]
        a[x][y] = 3
        go(index+1,cnt+1)
        a[x][y] = 2
        go(index+1,cnt)

go(0,0)
print(ans)