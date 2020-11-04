#https://www.acmicpc.net/problem/2151

import sys
from collections import deque

n = int(sys.stdin.readline())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

door = []

for i in range(n):
    for j in range(n):
        if a[i][j] == '#':
            door.append((i,j))

d = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()

for k in range(4):
    d[door[0][0]][door[0][1]][k] = 0
    q.append((door[0][0], door[0][1], k))

while q:
    x, y, dir = q.popleft()

    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < n and a[nx][ny] != '*':
        if a[nx][ny] == '.':
            if d[nx][ny][dir] == -1 or d[nx][ny][dir] > d[x][y][dir]:
                d[nx][ny][dir] = d[x][y][dir]
                q.append((nx,ny,dir))

        elif a[nx][ny] == '!':
            if dir == 0 or dir == 1:
                if d[nx][ny][2] == -1 or d[nx][ny][2] > d[x][y][dir] + 1:
                    d[nx][ny][2] = d[x][y][dir] + 1
                    q.append((nx,ny,2))
                if d[nx][ny][3] == -1 or d[nx][ny][3] > d[x][y][dir] + 1:
                    d[nx][ny][3] = d[x][y][dir] + 1
                    q.append((nx,ny,3))

            elif dir == 2 or dir == 3:
                if d[nx][ny][0] == -1 or d[nx][ny][0] > d[x][y][dir] + 1:
                    d[nx][ny][0] = d[x][y][dir] + 1
                    q.append((nx, ny, 0))
                if d[nx][ny][1] == -1 or d[nx][ny][1] > d[x][y][dir] + 1:
                    d[nx][ny][1] = d[x][y][dir] + 1
                    q.append((nx, ny, 1))

            if d[nx][ny][dir] == -1 or d[nx][ny][dir] > d[x][y][dir]:
                d[nx][ny][dir] = d[x][y][dir]
                q.append((nx, ny, dir))

        elif nx == door[1][0] and ny == door[1][1]:
            if d[nx][ny][dir] == -1 or d[nx][ny][dir] > d[x][y][dir]:
                d[nx][ny][dir] = d[x][y][dir]

answer = 50 * 50

for res in d[door[1][0]][door[1][1]]:
    if res == -1:
        continue
    answer = min(answer,res)

print(answer)