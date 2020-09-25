# https://www.acmicpc.net/problem/16954

import sys
from collections import deque

a = [list(sys.stdin.readline()) for _ in range(8)]
wall = []
for i in range(8):
    for j in range(8):
        if a[i][j] == '#':
            wall.append([i, j])

q = deque()
q.append([7, 0, 0])
dx = [0, 0, 0, -1, 1, -1, 1, 1, -1]
dy = [0, 1, -1, 0, 0, 1, 1, -1, -1]

is_arrived = False

if len(wall) == 0:
    print(1)

else:
    while q:
        for _ in range(len(q)):
            x, y, d = q.popleft()

            if x == 0:
                is_arrived = True
                break

            if a[x][y] == '#':
                continue

            for k in range(9):
                nx = x + dx[k]
                ny = y + dy[k]
                nd = d + 1
                if nd == 8:
                    is_arrived = True
                    break
                if 0 <= nx < 8 and 0 <= ny < 8 and a[nx][ny] == '.':
                    q.append([nx, ny, d + 1])

        for i in range(len(wall) - 1, -1, -1):
            mx, my = wall[i]
            if mx >= 8:
                continue
            if mx == 7:
                a[mx][my] = '.'
                wall[i] = [mx + 1, my]

            elif mx < 7:
                a[mx + 1][my] = '#'
                a[mx][my] = '.'
                wall[i] = [mx + 1, my]
        if is_arrived:
            break
    print(1 if is_arrived else 0)