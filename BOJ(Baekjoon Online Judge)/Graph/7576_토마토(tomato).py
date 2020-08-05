#https://www.acmicpc.net/problem/7576

import sys
from collections import deque

m, n = map(int,sys.stdin.readline().split())

a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
d = [[-1] * m for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            d[i][j] = 0
            q.append((i,j))

while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0:
                if d[nx][ny] == -1 or d[nx][ny] > d[x][y] + 1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))

is_ripen = True
ans = 0
for i in range(n):
    for j in range(m):
        if d[i][j] == -1 and a[i][j] == 0:
            is_ripen = False
        ans = max(ans,d[i][j])
if is_ripen:
    print(ans)
else:
    print(-1)

"""
ans = max([max(i) for i in d])
is_ripen = True
for i in range(n):
    for j in range(m):
        if a[i][j] == '0' and d[i][j] == -1:
            is_ripen = False
            ans = -1
            break
    if not is_ripen:
        break

print(ans)

"""