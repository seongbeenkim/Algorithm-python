#https://www.acmicpc.net/problem/2178

import sys
from collections import deque
n, m = map(int,sys.stdin.readline().strip().split())
a = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
check = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x, y))
    check[x][y] = True
    dist[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == False and a[nx][ny] == 1:
                    q.append((nx, ny))
                    check[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1

bfs(0,0)
print(dist[n-1][m-1])

# DFS로 할 경우 모든 경로 다 방문해야 하기 때문에 시간 초과! 최단 거리 문제는 BFS로 풀어야한다.
"""
def dfs(i, j):
    for k in range(4):
        nx = dx[k] + i
        ny = dy[k] + j
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == '1':
            if dist[nx][ny] == 0 or dist[nx][ny] > dist[i][j] + 1:
                dist[nx][ny] = dist[i][j] + 1
                dfs(nx, ny)
dist[0][0] = 1
dfs(0,0)
"""