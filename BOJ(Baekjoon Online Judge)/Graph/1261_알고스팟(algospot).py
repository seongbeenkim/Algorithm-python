#https://www.acmicpc.net/problem/1261

import sys
from collections import deque

m, n = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().strip())) for i in range(n)]
d = [[-1]*m for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start,end):
    q = deque()
    q.append((start,end))
    d[start][end] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == -1:
                if a[nx][ny] == 1:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                else:
                    q.appendleft((nx, ny))
                    d[nx][ny] = d[x][y]
bfs(0,0)
print(d[n-1][m-1])