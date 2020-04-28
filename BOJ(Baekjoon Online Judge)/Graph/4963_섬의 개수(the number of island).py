#https://www.acmicpc.net/problem/4963

import sys
from collections import deque

sys.setrecursionlimit(10**6)

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def dfs(x,y,cnt):

    check[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] == False and a[nx][ny] == 1:
                cnt = dfs(nx,ny,cnt+1)
    return cnt

def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))
    check[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == False and a[nx][ny] == 1:
                    q.append((nx,ny))
                    cnt += 1
                    check[nx][ny] = True
    return cnt

while True:
    m, n = map(int,sys.stdin.readline().split())
    if m == 0 and n == 0:
        break
    a = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
    check = [[False] * m for _ in range(n)]

    group = []

    for i in range(n):
        for j in range(m):
            if check[i][j] == False and a[i][j] == 1:
                group.append(bfs(i,j,1)) #dfs(i,j,1)

    print(len(group))