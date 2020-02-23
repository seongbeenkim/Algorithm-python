#https://www.acmicpc.net/problem/14502

import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def go():
    b = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]

    for i in range(n):
        for j in range(m):
            if b[i][j] == 2:
                dfs(i, j, b)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt

def dfs(x,y,b):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if b[nx][ny] == 0:
                b[nx][ny] = 2
                dfs(nx,ny,b)

def bfs():

    d = [[0] * m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            d[i][j] = a[i][j]
            if a[i][j] == 2:
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if d[nx][ny] == 0:
                    d[nx][ny] = 2
                    q.append((nx,ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if d[i][j] == 0:
                cnt += 1
    return cnt

ans = -1
for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0:
            continue
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0:
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] == 0:
                            if x1==x2 and y1==y2:
                                continue
                            if x2==x3 and y2==y3:
                                continue
                            if x3==x1 and y3==y1:
                                continue
                            a[x1][y1] = 1
                            a[x2][y2] = 1
                            a[x3][y3] = 1
                            q = deque()
                            result = bfs() #go()
                            if ans < result:
                                ans = result
                            a[x1][y1] = 0
                            a[x2][y2] = 0
                            a[x3][y3] = 0

print(ans)