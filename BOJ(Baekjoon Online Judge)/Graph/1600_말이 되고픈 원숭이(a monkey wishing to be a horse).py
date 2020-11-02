#https://www.acmicpc.net/problem/1600

import sys
from collections import deque

k = int(sys.stdin.readline())
m, n = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

d = [[[-1] * (k+1) for _ in range(m)] for _ in range(n)]

dx = [0,0,1,-1,-2,-1,1,2,2,1,-1,-2]
dy = [1,-1,0,0,1,2,2,1,-1,-2,-2,-1]
cost = [0,0,0,0,1,1,1,1,1,1,1,1]

q = deque()
q.append((0,0,0))
d[0][0][0] = 0

while q:
    x, y, c = q.popleft()

    for l in range(12):
        nx = x + dx[l]
        ny = y + dy[l]
        nc = c + cost[l]
        if 0 <= nx < n and 0 <= ny < m and d[nx][ny][nc] == -1 and a[nx][ny] == 0 and nc <= k:
            d[nx][ny][nc] = d[x][y][c] + 1
            q.append((nx,ny,nc))

MAX = 200*200
answer = MAX
for res in d[n-1][m-1]:
    if res == -1:
        continue
    answer = min(answer,res)

if answer == MAX:
    answer = -1
print(answer)