#https://www.acmicpc.net/problem/14442

import sys
from collections import deque

n, m, k = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
d = [[[0]*(k+1) for i in range(m)] for j in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0,0,0))
    d[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0 and d[nx][ny][z] == 0:
                    q.append((nx,ny,z))
                    d[nx][ny][z] = d[x][y][z] + 1

                if z+1 <= k and a[nx][ny] == 1 and d[nx][ny][z+1] == 0:
                    q.append((nx,ny,z+1))
                    d[nx][ny][z+1] = d[x][y][z] + 1

bfs()
ans = -1
for i in range(k+1):
    if d[n-1][m-1][i] != 0:
        if ans == -1:
            ans = d[n - 1][m - 1][i]
        elif ans > d[n - 1][m - 1][i]:
            ans = d[n - 1][m - 1][i]
print(ans)