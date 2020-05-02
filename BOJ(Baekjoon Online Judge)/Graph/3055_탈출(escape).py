#https://www.acmicpc.net/problem/3055

import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int,sys.stdin.readline().split())
a = [list(sys.stdin.readline().strip()) for _ in range(n)]
d = [[-1] * m for _ in range(n)]

q = deque()
r, s = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            q.appendleft((i,j,'*'))
            d[i][j] = 0
        elif a[i][j] == 'S':
            q.append((i,j,'S'))
            d[i][j] = 0
        elif a[i][j] == 'D':
            r = i
            s = j

while q:
    x,y,z = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == -1:
            if z == '*' and a[nx][ny] == '.':
                d[nx][ny] = d[x][y]
                q.append((nx,ny,z))
            if z == 'S' and (a[nx][ny] == '.' or a[nx][ny] == 'D'):
                d[nx][ny] = d[x][y] + 1
                q.append((nx,ny,z))
if d[r][s] == -1:
    print("KAKTUS")
else:
    print(d[r][s])