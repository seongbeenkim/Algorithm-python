#https://www.acmicpc.net/problem/6087

import sys
from collections import deque

m, n = map(int,sys.stdin.readline().split())
a = [list(sys.stdin.readline()) for _ in range(n)]
d = [[-1] * m for _ in range(n)]

site = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 'C':
            site.append([i,j])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()
q.append((site[0][0],site[0][1]))
d[site[0][0]][site[0][1]] = 0


while q:
    x, y = q.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        while 0 <= nx < n and 0 <= ny < m and a[nx][ny] != '*':
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
            nx += dx[k]
            ny += dy[k]

print(d[site[1][0]][site[1][1]]-1)

for i in d:
    print(*i)