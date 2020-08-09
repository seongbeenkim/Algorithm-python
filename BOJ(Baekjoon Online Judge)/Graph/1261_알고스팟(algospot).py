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

# 재탐색을 허용하기 때문에 시간이 조금 더 오래걸린다.
"""
            if 0 <= nx < n and 0 <= ny < m:
                if (d[nx][ny] == -1 or d[x][y] < d[nx][ny]) and a[nx][ny] == '0':
                    d[nx][ny] = d[x][y]
                    q.append((nx,ny))
                elif (d[nx][ny] == -1 or d[x][y] + 1 < d[nx][ny]) and a[nx][ny] == '1':
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))
"""