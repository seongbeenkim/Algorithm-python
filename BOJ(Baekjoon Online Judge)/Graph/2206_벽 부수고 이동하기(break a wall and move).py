#https://www.acmicpc.net/problem/2206

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

dist = [[[0] * 2 for j in range(m)] for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    dist[0][0][0] = 1
    d = deque()
    d.append((0,0,0))
    while d:
        x, y, z = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0 and dist[nx][ny][z] == 0:
                    d.append((nx,ny,z))
                    dist[nx][ny][z] = dist[x][y][z] + 1

                if z == 0 and a[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
                    d.append((nx,ny,z+1))
                    dist[nx][ny][z+1] = dist[x][y][z] + 1

    if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0:
        print(min(dist[n-1][m-1][0], dist[n-1][m-1][1]))
    elif dist[n-1][m-1][0] != 0:
        print(dist[n-1][m-1][0])
    elif dist[n-1][m-1][1] != 0:
        print(dist[n-1][m-1][1])
    else:
        print(-1)
bfs()