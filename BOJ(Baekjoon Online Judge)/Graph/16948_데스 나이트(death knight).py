#https://www.acmicpc.net/problem/16948

import sys
from collections import deque

n = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int,sys.stdin.readline().split())

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

d = [[-1] * n for _ in range(n)]
q = deque()
q.append((r1,c1))
d[r1][c1] = 0

while q:
    x, y = q.popleft()
    for k in range(6):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and (d[nx][ny] == -1 or d[nx][ny] > d[x][y] + 1):
            d[nx][ny] = d[x][y] + 1
            q.append((nx,ny))

print(d[r2][c2])