#https://www.acmicpc.net/problem/16236

import sys
from collections import deque

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

fish = [1,2,3,4,5,6]


def bfs(x,y,size):

    ans = []
    d = [[0] * n for _ in range(n)]
    q = deque()
    q.append((x,y))
    d[x][y] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == 0:
                if a[nx][ny] == 0:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1

                elif a[nx][ny] < size:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    ans.append((d[nx][ny],nx,ny))

                elif a[nx][ny] == size:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
    if not ans:
        return None
    ans.sort(key = lambda x : (x[0],x[1],x[2]))
    return ans[0]

pairs = []
x = 0
y = 0
size = 2
ans = 0
exp = 0

for i in range(n):
    for j in range(n):
        if a[i][j] in fish:
            pairs.append((a[i][j],i,j))
        elif a[i][j] == 9:
            x, y = i,j
            a[i][j] = 0
if len(pairs) == 0:
    print(0)
else:
    for _ in range(len(pairs)):
        p = bfs(x,y,size)
        if p == None:
            break
        dist, nx, ny = p
        a[nx][ny] = 0
        ans += dist
        exp += 1
        if size == exp:
            size += 1
            exp = 0
        x = nx
        y = ny
    print(ans)