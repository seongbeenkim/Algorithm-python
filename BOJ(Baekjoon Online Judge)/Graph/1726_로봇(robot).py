# https://www.acmicpc.net/problem/1726

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [[[-1] * 4 for _ in range(m)] for _ in range(n)]

sx, sy, sway = map(int, sys.stdin.readline().split())
sx -= 1
sy -= 1
sway -= 1
ex, ey, eway = map(int, sys.stdin.readline().split())
ex -= 1
ey -= 1
eway -= 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((sx, sy, sway))
d[sx][sy][sway] = 0

while q:
    x, y, way = q.popleft()
    nx = x
    ny = y

    # Go k
    for k in range(1, 4):
        nx = x + dx[way] * k
        ny = y + dy[way] * k

        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0:
                if d[nx][ny][way] == -1 or d[nx][ny][way] > d[x][y][way] + 1:
                    d[nx][ny][way] = d[x][y][way] + 1
                    q.append((nx, ny, way))
            else:
                break
        else:
            break

    # Turn dir
    for i in range(4):
        if i == way:
            continue
        if (i + way) % 4 == 1:
            if d[x][y][i] == -1 or d[x][y][i] > d[x][y][way] + 1:
                d[x][y][i] = d[x][y][way] + 2
                q.append((x, y, i))
        else:
            if d[x][y][i] == -1 or d[x][y][i] > d[x][y][way] + 1:
                d[x][y][i] = d[x][y][way] + 1
                q.append((x, y, i))
print(d[ex][ey][eway])