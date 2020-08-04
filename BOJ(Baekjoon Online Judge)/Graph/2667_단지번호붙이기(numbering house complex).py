#https://www.acmicpc.net/problem/2667

import sys,queue
from collections import deque
sys.setrecursionlimit(10*6)

n = int(sys.stdin.readline())
a = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(n)]
check = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

group = []

def dfs(x,y,c):
    check[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if a[nx][ny] == 1 and check[nx][ny] == False:
                c = dfs(nx,ny,c+1)
    return c

def bfs(x,y,c):
    q = deque()
    q.append((x,y))
    check[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if a[nx][ny] == 1 and check[nx][ny] == False:
                    check[nx][ny] = True
                    q.append((nx,ny))
                    c += 1
    return c

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and check[i][j] == False:
            group.append(bfs(i,j,1)) #dfs(i,j,1)

print(len(group))
group.sort()
for i in group:
    print(i)

"""
n = int(sys.stdin.readline())

a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] * n for _ in range(n)]
d = [[0]* n for _ in range(n)]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    d[i][j] = 1
    cnt = 1
    maximum = 1

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and a[nx][ny] == '1':
                visited[nx][ny] = True
                d[nx][ny] = cnt + 1
                maximum = max(maximum,d[nx][ny])
                q.append((nx,ny))
                cnt += 1

    return maximum

town = 0
ans = []
for i in range(n):
    for j in range(n):
        if a[i][j] == '1' and not visited[i][j]:
            ans.append(bfs(i,j))
            town += 1

ans.sort()
print(town)
print(*ans, sep="\n")
"""